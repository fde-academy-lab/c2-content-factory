"""Run the cold-run script through the cases its comment block lists, and check each outcome.

    python3 content/W03/D5/internal/C2_W03_D05_cold_run_cases_INTERNAL.py [script] [data folder]

Run it from the repository root. With no arguments it tests checkpoints/C2_W03_D05_cold_run_STUDENT.py
on the data pack in content/W03/D1/data/. Each case builds a fresh git repository in a temporary
folder, with a small notebook that reads the patient register and prints "6,700 patients" and
"25.4 percent aged 65 and over", runs the script there, and checks the exit code and the lines it
prints. It prints PASS or FAIL per case and a RESULT line, and exits 1 on any FAIL. It needs jupyter,
nbconvert, pandas and git.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
SCRIPT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE.parent / "checkpoints" / "C2_W03_D05_cold_run_STUDENT.py").resolve()
DATA = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else HERE.parents[1] / "D1" / "data").resolve()
FAILS = []

GOOD_CELLS = [
    "import pandas as pd\np = pd.read_csv('data/C2_W03_D01_patients_STUDENT.csv')",
    "print(f'{len(p):,} patients')",
    "share = (p['age_band'] == '65+').mean() * 100\nprint(f'{share:.1f} percent aged 65 and over')",
]


def notebook(cells):
    return {"cells": [{"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [],
                       "source": c} for c in cells],
            "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}},
            "nbformat": 4, "nbformat_minor": 5}


def repo(cells=GOOD_CELLS, slide="6,700 | patients on the register\n25.4 percent | aged 65 and over\n",
         git=True, drop=None, extra_byte=None):
    d = pathlib.Path(tempfile.mkdtemp(prefix="coldcase_"))
    (d / "data").mkdir()
    for f in DATA.glob("C2_W03_D01_*_STUDENT.csv"):
        if f.name != drop:
            shutil.copy(f, d / "data" / f.name)
    if extra_byte:
        with open(d / "data" / extra_byte, "ab") as fh:
            fh.write(b"\n")
    (d / "analysis.ipynb").write_text(json.dumps(notebook(cells)), encoding="utf-8")
    if slide is not None:
        (d / "slide_numbers.txt").write_text(slide, encoding="utf-8")
    shutil.copy(SCRIPT, d / SCRIPT.name)
    if git:
        run = lambda *a: subprocess.run(["git", *a], cwd=d, capture_output=True, text=True, check=True)
        run("init", "-q", "-b", "cold-run-test")
        run("config", "user.email", "t@example.com")
        run("config", "user.name", "t")
        run("add", "-A")
        run("commit", "-q", "-m", "case")
    return d


def go(d, *extra, run="1"):
    args = [sys.executable, SCRIPT.name, "--notebook", "analysis.ipynb", "--slide", "slide_numbers.txt",
            "--data", "data", "--run", run, *extra]
    r = subprocess.run(args, cwd=d, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def case(name, ok, out):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        FAILS.append(name)
        print("      " + out.replace("\n", "\n      ")[:1500])


d = repo()
code, out = go(d)
case("a clean run passes and exits 0", code == 0 and "RESULT: PASS (0 failures)" in out
     and "PASS  slide number 6,700" in out and "Branch and commit: cold-run-test" in out
     and "with uncommitted changes" not in out and "| 2 of 2 | nothing |" in out, out)

d = repo(slide="6,700 | patients\n25.4 percent | aged 65 and over\n99.9 percent | never printed\n")
subprocess.run(["git", "commit", "-qam", "slide"], cwd=d, capture_output=True)
code, out = go(d)
case("a slide number never printed fails that line only", code == 1 and "FAIL  slide number 99.9 percent" in out
     and "PASS  slide number 6,700" in out and "99.9 percent not printed" in out, out)

d = repo(extra_byte="C2_W03_D01_sites_STUDENT.csv")
code, out = go(d)
case("a raw file saved again fails", code == 1 and "raw file changed since the data team dropped it: "
     "C2_W03_D01_sites_STUDENT.csv" in out, out)
code, out = go(d, "--reference", "data")
case("--reference at the same folder passes", code == 0, out)

ref = pathlib.Path(tempfile.mkdtemp(prefix="coldref_"))
for f in DATA.glob("C2_W03_D01_*_STUDENT.csv"):
    if f.name != "C2_W03_D01_sites_STUDENT.csv":
        shutil.copy(f, ref / f.name)
d = repo()
code, out = go(d, "--reference", str(ref))
case("--reference missing a file fails without a traceback", code == 1
     and "raw file missing from the reference folder: C2_W03_D01_sites_STUDENT.csv" in out
     and "Traceback" not in out, out)

d = repo(cells=GOOD_CELLS[:2] + ["raise ValueError('bad cell')"])
code, out = go(d)
case("a stopped notebook fails, checks no number and logs 0 of 2", code == 1
     and "FAIL  the notebook stopped after" in out and "slide number" not in out.split("Branch and commit")[0]
     and "| 0 of 2 |" in out, out)

d = repo(drop="C2_W03_D01_claims_STUDENT.csv")
code, out = go(d)
case("a missing raw file fails", code == 1 and "FAIL  raw file missing: C2_W03_D01_claims_STUDENT.csv" in out, out)

d = repo(slide=None)
code, out = go(d)
case("a missing slide file fails without a traceback", code == 1 and "FAIL  no slide file at slide_numbers.txt" in out
     and "Traceback" not in out and "PASS  the notebook ran top to bottom" in out, out)

d = repo(cells=["print('1,2')"], slide="12\n")
subprocess.run(["git", "commit", "-qam", "x"], cwd=d, capture_output=True)
code, out = go(d)
case("1,2 is no thousands comma, so 12 is not found", code == 1 and "FAIL  slide number 12" in out, out)

d = repo(cells=["print('5.1,7.8')"], slide="5.1\n7.8\n")
code, out = go(d)
case("5.1,7.8 holds two numbers", code == 0 and "PASS  slide number 5.1" in out and "PASS  slide number 7.8" in out, out)

d = repo(cells=["print(112.5); print(12.55)"], slide="12.5\n")
code, out = go(d)
case("12.5 is not found inside 112.5 or 12.55", code == 1 and "FAIL  slide number 12.5" in out, out)

d = repo(cells=["print('12.5%')"], slide="12.5 percent\n")
code, out = go(d)
case("12.5 percent matches 12.5%", code == 0, out)

d = repo(git=False)
code, out = go(d)
case("a folder that is not a git repository says so", code == 0 and "Branch and commit: not a git repository" in out, out)

d = repo(cells=GOOD_CELLS + ["p.head().to_csv('clean_sample.csv')"])
code, out = go(d)
case("a notebook that writes a file into its folder does not read as uncommitted work", code == 0
     and "with uncommitted changes" not in out, out)

d = repo()
(d / "notes.txt").write_text("typed in the Codespace and never pushed\n", encoding="utf-8")
code, out = go(d)
case("a file added in the Codespace and never pushed reads as uncommitted work",
     "with uncommitted changes" in out, out)

d = repo()
r = subprocess.run([sys.executable, SCRIPT.name, "--notebook", "analysis.ipynb", "--slide", "slide_numbers.txt",
                    "--data", "data"], cwd=d, capture_output=True, text=True,
                   env={**os.environ, "PATH": "/nonexistent"})
out = r.stdout + r.stderr
case("no jupyter on the PATH fails with its reason", r.returncode == 1 and "jupyter is not installed here" in out, out)

print(f"\nRESULT: {'FAIL' if FAILS else 'PASS'} ({len(FAILS)} failures)")
sys.exit(1 if FAILS else 0)

# Test inputs and expected outcomes
# ---------------------------------
# With no arguments, on 4 October 2026: sixteen PASS lines, from "a clean run passes and exits 0" to
#   "no jupyter on the PATH fails with its reason", then RESULT: PASS (0 failures).
# Pointed at the script as it stood before 4 October 2026 (commit 00aa2bf), which read git after the
#   run: fifteen PASS lines and FAIL "a notebook that writes a file into its folder does not read as
#   uncommitted work", then RESULT: FAIL (1 failures).
# Pointed at a data folder with nine of the ten files: the five cases that expect a clean exit fail,
#   since each case copies the folder it is given, and RESULT: FAIL (5 failures).

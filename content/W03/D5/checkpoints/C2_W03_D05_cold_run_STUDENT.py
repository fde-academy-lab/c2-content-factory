"""Run your Kalpa Health notebook cold, time it, and check that every number on your one slide appears.

    python3 C2_W03_D05_cold_run_STUDENT.py --notebook analysis.ipynb --slide slide_numbers.txt --data data

What it does, in order:

1. Checks the ten raw Kalpa Health files in --data against the checksums of the files the data team
   dropped, so a raw file edited by hand is caught before the panel catches it. Pass --reference with
   the folder of the files as published if the pack was re-issued after this script was written.
2. Runs the notebook top to bottom in a fresh kernel with jupyter nbconvert, from the notebook's own
   folder, and times the run.
3. Reads every printed output of the executed notebook and looks for each number in --slide, one
   number per line, written exactly as the slide shows it. Anything after a | on a line is your label.
   Commas, "$", "percent" and "%" are ignored in the comparison, so "$180,000" on the slide
   matches 180000 or 180,000 printed by the notebook. A number the notebook computes and never
   prints does not count, so print every slide number in the slide's own format.
4. Prints one line to paste into the cold-run log in the demo checklist.

It exits 0 only when the files match, the run is clean and every slide number was found.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import time

RAW = {
    "C2_W03_D01_appointments_STUDENT.csv": "a4d4e2cd46bc4fc70b5b1a5efe4da618993e8425d23a11af370eec1709f7b470",
    "C2_W03_D01_booking_tests_STUDENT.csv": "830a209b61b95ae97f8ca7ab5a68a7e6d71891befcf2623f96b18dc2e6d3bf29",
    "C2_W03_D01_bookings_legacy_STUDENT.csv": "cf621766222a8a27ef7845e25ef9a5502eecb55b0eb4c87fe82ab6620f50bbb5",
    "C2_W03_D01_bookings_newsys_STUDENT.csv": "f10318c173e2453988e7c2b93c1b11eac97ec485285840885a254fd7e68a8523",
    "C2_W03_D01_campaign_STUDENT.csv": "d908805cb393b270519402cd8622ca4bf228357ba90dfc8fc2244f6a494d8da2",
    "C2_W03_D01_claims_STUDENT.csv": "80ce3072366d3cffd38791608d9a2155ee904223d8d927ddb9416e5f6a829b1b",
    "C2_W03_D01_patients_STUDENT.csv": "bf0ad86a73787a79bd2d12f3b15b2d62af97f9434cfd6fde75b070ba53864623",
    "C2_W03_D01_remittances_STUDENT.csv": "8a2ba957fa9c7108104b33103502cd161647de092fa30dd9d7dd5f2c685d0d12",
    "C2_W03_D01_sites_STUDENT.csv": "10ad6074d49c8504f0b39dcf23a5cb8e545896791aa452eb52555cdd15086a0a",
    "C2_W03_D01_test_catalogue_STUDENT.csv": "00e2faf07da527a140ba008fa1ed71b9768285103126aec37f52c21cced34eee",
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def check_raw(data_dir, reference_dir=None):
    """Return a list of problems with the raw files; an empty list means all ten match."""
    expected = dict(RAW)
    if reference_dir:
        expected = {name: sha256(pathlib.Path(reference_dir) / name) for name in RAW}
    problems = []
    for name, digest in expected.items():
        p = pathlib.Path(data_dir) / name
        if not p.exists():
            problems.append(f"missing: {name}")
        elif sha256(p) != digest:
            problems.append(f"changed since the data team dropped it: {name}")
    return problems


def normalise(text):
    """Drop the decorations a slide and a print() disagree on, and keep the digits."""
    text = text.replace(",", "").replace("$", "")
    text = re.sub(r"\bRs\.?\s*", "", text)
    text = re.sub(r"\s*(percent|%)", "", text)
    return text


def slide_numbers(path):
    """Each non-blank line of the slide file: (the number as normalised, the line as written)."""
    rows = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        shown = line.split("|")[0].strip()
        if not shown or shown.startswith("#"):
            continue
        rows.append((normalise(shown).strip(), line.strip()))
    return rows


def printed_text(executed_nb):
    """Every stream and plain-text output of the executed notebook, joined."""
    nb = json.loads(pathlib.Path(executed_nb).read_text(encoding="utf-8"))
    parts = []
    for cell in nb.get("cells", []):
        for out in cell.get("outputs", []):
            if "text" in out:
                parts.append("".join(out["text"]))
            data = out.get("data", {})
            if "text/plain" in data:
                parts.append("".join(data["text/plain"]))
    return "\n".join(parts)


def found(number, text):
    pattern = r"(?<![\d.])" + re.escape(number) + r"(?![\d])"
    return re.search(pattern, text) is not None


def run_cold(notebook, timeout):
    """Execute the notebook in a fresh kernel from its own folder; return (ok, seconds, executed, error)."""
    nb = pathlib.Path(notebook).resolve()
    out_dir = pathlib.Path(tempfile.mkdtemp(prefix="cold_run_"))
    executed = out_dir / nb.name
    start = time.time()
    r = subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute",
                        f"--ExecutePreprocessor.timeout={timeout}",
                        "--output-dir", str(out_dir), str(nb)],
                       cwd=str(nb.parent), capture_output=True, text=True)
    seconds = time.time() - start
    if r.returncode != 0:
        last = r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "no error text"
        return False, seconds, None, re.sub(r"\x1b\[[0-9;]*m", "", last)
    return True, seconds, executed, ""


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--notebook", required=True)
    ap.add_argument("--slide", required=True, help="one slide number per line, as the slide prints it")
    ap.add_argument("--data", required=True, help="the folder holding the ten raw Kalpa Health files")
    ap.add_argument("--reference", help="the published data folder, if the pack was re-issued")
    ap.add_argument("--run", default="1", help="which cold run this is, 1 or 2")
    ap.add_argument("--timeout", type=int, default=900, help="seconds any one cell may take")
    args = ap.parse_args(argv)

    fails = 0
    problems = check_raw(args.data, args.reference)
    if problems:
        for p in problems:
            print(f"FAIL  raw file {p}")
        fails += len(problems)
    else:
        print("PASS  the ten raw files match the data team's drop")

    ok, seconds, executed, error = run_cold(args.notebook, args.timeout)
    minutes = seconds / 60
    if not ok:
        print(f"FAIL  the notebook stopped after {minutes:.1f} minutes: {error}")
        fails += 1
        missing = ["not checked, since the run stopped"]
        numbers = []
    else:
        print(f"PASS  the notebook ran top to bottom in {minutes:.1f} minutes")
        text = normalise(printed_text(executed))
        numbers = slide_numbers(args.slide)
        missing = [line for number, line in numbers if not found(number, text)]
        for number, line in numbers:
            print(("PASS  " if line not in missing else "FAIL  ") + f"slide number {line}")
        fails += len(missing)

    today = datetime.date.today().isoformat()
    reproduced = len(numbers) - len(missing) if ok else 0
    print("\nPaste into the cold-run log:")
    broke = problems + ([error] if not ok else []) + [m.split("|")[0].strip() + " not printed"
                                                      for m in missing if "|" in m or ok]
    print(f"| {args.run} | {today} | {minutes:.1f} | {reproduced} of {len(numbers)} | "
          f"{'nothing' if not fails else '; '.join(broke)[:160].replace('|', '/')} |  |")
    print("\nRESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

# Test inputs and expected outcomes
# ---------------------------------
# A notebook that reads the ten untouched files and prints 1,250 and 25.4, with a slide file holding
#     $1,250 | example label
#     25.4 percent | example label
#   prints PASS for the raw files, the run and both numbers, and exits 0.
# The same run with a slide file that also holds "99.9 percent", which the notebook never prints,
#   prints FAIL for that line only and exits 1.
# The same run after one raw CSV was saved again from Excel (so its bytes changed)
#   prints FAIL "raw file changed since the data team dropped it: <name>" and exits 1.
# A notebook whose third cell raises an error
#   prints FAIL "the notebook stopped after N minutes: <the last error line>", checks no numbers,
#   and exits 1.
# --data pointing at a folder with nine of the ten files
#   prints FAIL "raw file missing: <name>" for the tenth and exits 1.

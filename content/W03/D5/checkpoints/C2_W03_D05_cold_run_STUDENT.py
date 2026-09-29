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
   Commas, "Rs", "percent" and "%" are ignored in the comparison, so "Rs 12,34,500" on the slide
   matches 1234500 or 12,34,500 printed by the notebook. A number the notebook computes and never
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
    "C2_W03_D01_appointments_STUDENT.csv": "dfb4a573c1f2ea84bf2c3ad01c7cf7c2fef47d370bfdeca3a55ed326d2020e9a",
    "C2_W03_D01_booking_tests_STUDENT.csv": "5c36d8de9c0a57075ef710a8cd0786ba1ab1f85fb9ba293e68fa7ba2d86c8cad",
    "C2_W03_D01_bookings_legacy_STUDENT.csv": "6247e20a808de47747823130409deafae9022519f2f3c7a2f8e28deba869593f",
    "C2_W03_D01_bookings_newsys_STUDENT.csv": "ea6ce4bfd90b29e90d07bde5a1a8b20ee7045e4c82f4e2303f5684b80c1ecbd1",
    "C2_W03_D01_campaign_STUDENT.csv": "2e7744d62491af7df177f9f706f30a8cdb265a89f5018ea8b735f74a47953608",
    "C2_W03_D01_clinics_STUDENT.csv": "cbe836671ce4d0e5d2c0ec431836acf67e5691260a895daf5dd5f6969310a53f",
    "C2_W03_D01_invoices_STUDENT.csv": "425ed3a0f50a4277b1bea43030d79daf6a8fadef28712c9246b1119dd64461c0",
    "C2_W03_D01_patients_STUDENT.csv": "d9bbb67fe65e302112febf6d697ebc2b2690332d522b2879b41b3fa03b91a82b",
    "C2_W03_D01_payments_STUDENT.csv": "f302f4656c3d64f8c9ccee25ad06cd1f832a39c610f5e8cfc289abc8e61771bb",
    "C2_W03_D01_test_catalogue_STUDENT.csv": "3c265cc4db9a7712ee522ab9c02ade4eda1bb635b7e8a40040f7268cb2b08c23",
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
    text = text.replace(",", "")
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
#     Rs 1,250 | example label
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

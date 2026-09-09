"""Verification gate for a day pack. Usage: python3 scripts/verify.py content/W01/D1 [--execute]
--execute additionally cold-runs every notebook via jupyter nbconvert (needs jupyter installed).
Every filename must carry the C2_W{ww}_D{dd} stem matching the day folder it sits in, so a build
pointed at the wrong day fails here rather than overwriting another day's pack.
Exit code 0 means pass; any FAIL line means the pack is not done."""
import sys, re, json, pathlib, subprocess

BANNED = ["Additionally","Moreover","However","Hence","Thus","Nonetheless","Furthermore","Accordingly",
          "Indeed","Dynamic","comprehensive","robust","holistic","seamless","delve",
          "In conclusion","In summary","unlock the power"]
TRAINER_NAMES = ["Akash","Ishu","Anmol","Rushikesh","Navaid","Kanchan","Umashankar","Mithun",
                 "Anupam","Sumit","Anish","Sameer","Debarati"]
CLOCK = re.compile(r"\b\d{1,2}[:.]\d{2}\s?(AM|PM|am|pm)\b")
NXBY = re.compile(r"\bnot\s+\w+[^.\n]{0,40},\s*but\b", re.IGNORECASE)
URL = re.compile(r"https?://\S+")
DAY_FOLDER = re.compile(r"W(\d{1,2})[/\\]D(\d{1,2})$")
DAY_STEM = re.compile(r"^C2_W(\d{2})_D(\d{2})_")
DATED = re.compile(r"(verified|checked)\s+\d{1,2}\s+\w+\s+\d{4}", re.IGNORECASE)

def check_targeting(target, files):
    """Fail when a file's C2_W{ww}_D{dd} stem disagrees with the day folder it sits in.

    The folder is single digit (D2) and the stem is zero padded (D02), so they are compared
    as integers. This catches a build that was pointed at the wrong day, which is otherwise
    invisible: every other check still passes while the files overwrite another day's pack.
    """
    m = DAY_FOLDER.search(str(target).rstrip("/\\"))
    if not m:
        print(f"INFO  {target} is not a W{{ww}}/D{{d}} day folder, so the day-stem check is skipped")
        return 0
    want = f"C2_W{int(m.group(1)):02d}_D{int(m.group(2)):02d}_"
    fails = 0
    for p in files:
        found = DAY_STEM.match(p.name)
        if not found:
            print(f"FAIL  {p.name}: no C2_W{{ww}}_D{{dd}}_ stem in the filename; {target} expects {want}")
            fails += 1
        elif found.group(0) != want:
            print(f"FAIL  {p.name}: stem says week {found.group(1)} day {found.group(2)}, "
                  f"but the file sits in {target}, which expects {want}")
            fails += 1
    if not fails:
        print(f"PASS  every filename carries the {want} stem for {target}")
    return fails


def texts_from(path):
    if path.suffix == ".ipynb":
        try:
            nb = json.loads(path.read_text(encoding="utf-8"))
            for cell in nb.get("cells", []):
                yield "".join(cell.get("source", []))
        except Exception as e:
            yield ""
            print(f"FAIL  {path.name}: notebook does not parse ({e})")
    elif path.suffix in (".md", ".txt", ".py", ".sql", ".csv", ".html"):
        yield path.read_text(encoding="utf-8", errors="replace")

def main():
    target = pathlib.Path(sys.argv[1])
    execute = "--execute" in sys.argv
    fails = 0
    files = [p for p in target.rglob("*") if p.is_file() and p.name != ".gitkeep"]
    if not files:
        print("FAIL  no files found under", target); sys.exit(1)
    fails += check_targeting(target, files)
    for p in files:
        name = p.name
        if not re.search(r"_(STUDENT|TRAINER|INTERNAL)\.", name):
            print(f"FAIL  {name}: missing audience tag in filename"); fails += 1
        student = "_STUDENT." in name
        for txt in texts_from(p):
            if "\u2014" in txt or "\u2013" in txt:
                print(f"FAIL  {name}: em or en dash present"); fails += 1
            for b in BANNED:
                if re.search(r"\b" + re.escape(b) + r"\b", txt, re.IGNORECASE if b[0].islower() else 0):
                    print(f"FAIL  {name}: banned word '{b}'"); fails += 1
            if NXBY.search(txt):
                print(f"FAIL  {name}: 'not X, but Y' construction"); fails += 1
            if CLOCK.search(txt):
                print(f"FAIL  {name}: clock time found (durations only)"); fails += 1
            if "\u20b9" in txt:
                print(f"FAIL  {name}: rupee glyph (use Rs)"); fails += 1
            if student:
                for nm in TRAINER_NAMES:
                    if re.search(r"\b" + nm + r"\b", txt):
                        print(f"FAIL  {name}: person name '{nm}' in a STUDENT file"); fails += 1
                if re.search(r"\b(marks|weightage|graded out of)\b", txt, re.IGNORECASE):
                    print(f"WARN  {name}: marks language in a STUDENT file; confirm the Structure tab allows it")
            for line in txt.splitlines():
                if URL.search(line) and not DATED.search(line) and "to be found" not in line.lower():
                    print(f"WARN  {name}: undated link: {line.strip()[:90]}")
        if execute and p.suffix == ".ipynb":
            r = subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute",
                                "--output", "/tmp/_exec_check.ipynb", str(p)],
                               capture_output=True, text=True)
            if r.returncode != 0:
                print(f"FAIL  {name}: cold run failed\n{r.stderr[-400:]}"); fails += 1
            else:
                print(f"PASS  {name}: cold run clean")
    print("RESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()

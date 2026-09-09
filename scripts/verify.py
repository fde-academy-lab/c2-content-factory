"""Verification gate for a day pack. Usage: python3 scripts/verify.py content/W01/D2 [--execute]
--execute additionally cold-runs every notebook via jupyter nbconvert (needs jupyter installed).

Three things are checked beyond the writing rules. Every filename must carry the
C2_W{ww}_D{dd} or C2_W{ww}_SAT stem matching the folder it sits in, so a build pointed at the
wrong day fails here rather than overwriting another day's pack. Every file must sit in one of
the subfolders its folder type allows, so a pack cannot quietly invent its own layout. And no
file may sit loose at the day folder's root.
"""
import sys, re, json, pathlib, subprocess

BANNED = ["Additionally","Moreover","However","Hence","Thus","Nonetheless","Furthermore","Accordingly",
          "Indeed","Dynamic","comprehensive","robust","holistic","seamless","delve",
          "In conclusion","In summary","unlock the power"]
TRAINER_NAMES = ["Akash","Ishu","Anmol","Rushikesh","Navaid","Kanchan","Umashankar","Mithun",
                 "Anupam","Sumit","Anish","Sameer","Debarati"]
CLOCK = re.compile(r"\b\d{1,2}[:.]\d{2}\s?(AM|PM|am|pm)\b")
NXBY = re.compile(r"\bnot\s+\w+[^.\n]{0,40},\s*but\b", re.IGNORECASE)
URL = re.compile(r"https?://\S+")
DAY_FOLDER = re.compile(r"W(\d{1,2})[/\\](D(\d{1,2})|SAT)$")
DAY_STEM = re.compile(r"^C2_W(\d{2})_(D\d{2}|SAT)_")
DATED = re.compile(r"(verified|checked)\s+\d{1,2}\s+\w+\s+\d{4}", re.IGNORECASE)

# Build weeks per the Structure tab: 3, 6 and 9 in this workbook, then 12 and 15 later in the
# programme. They ship the build-week pack instead of the teaching manifest, so their folders differ.
BUILD_WEEKS = {3, 6, 9, 12, 15}

TEACHING_DIRS = {
    "slides", "notebooks", "demos", "whiteboards", "cheatsheets", "study-notes",
    "exercises", "exercises/guided", "exercises/unguided", "exercises/solutions",
    "takehome", "kahoot", "preread", "extras", "data", "trainer", "internal", "corrections",
}
BUILD_DIRS = {
    "briefs", "rubrics", "gd", "parallel-build", "checkpoints", "mocks", "trainer", "internal",
}
SAT_RECAP_DIRS = {"paper", "answer-key", "discussion"}


def folder_shape(week, day_label):
    """Which subfolders this day folder is allowed to hold, and what to call the shape."""
    if week in BUILD_WEEKS:
        return ("build day" if day_label != "SAT" else "build week Saturday"), BUILD_DIRS
    if day_label == "SAT":
        return "Saturday recap", SAT_RECAP_DIRS
    return "teaching day", TEACHING_DIRS


def check_layout(target, files):
    """Fail on a wrong day stem, a file loose at the root, or a folder outside the shape."""
    m = DAY_FOLDER.search(str(target).rstrip("/\\"))
    if not m:
        print(f"INFO  {target} is not a W{{ww}}/D{{d}} or W{{ww}}/SAT folder, so layout checks are skipped")
        return 0
    week = int(m.group(1))
    day_label = "SAT" if m.group(2) == "SAT" else f"D{int(m.group(3)):02d}"
    want = f"C2_W{week:02d}_{day_label}_"
    shape_name, allowed = folder_shape(week, day_label)
    fails = 0
    for p in files:
        found = DAY_STEM.match(p.name)
        if not found:
            print(f"FAIL  {p.name}: no C2_W{{ww}}_D{{dd}}_ or C2_W{{ww}}_SAT_ stem; {target} expects {want}")
            fails += 1
        elif found.group(0) != want:
            print(f"FAIL  {p.name}: stem says week {found.group(1)} {found.group(2)}, "
                  f"but the file sits in {target}, which expects {want}")
            fails += 1
        rel = p.parent.relative_to(target).as_posix()
        if rel == ".":
            print(f"FAIL  {p.name}: loose at the day folder root; every file belongs in a subfolder")
            fails += 1
        elif rel not in allowed:
            print(f"FAIL  {p.name}: sits in '{rel}', which is not a {shape_name} folder. "
                  f"Allowed: {', '.join(sorted(allowed))}")
            fails += 1
    if not fails:
        print(f"PASS  {len(files)} files, every stem {want} and every folder valid for a {shape_name}")
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
    fails += check_layout(target, files)
    for p in files:
        name = p.name
        if not re.search(r"_(STUDENT|TRAINER|INTERNAL)\.", name):
            print(f"FAIL  {name}: missing audience tag in filename"); fails += 1
        student = "_STUDENT." in name
        for txt in texts_from(p):
            if "—" in txt or "–" in txt:
                print(f"FAIL  {name}: em or en dash present"); fails += 1
            for b in BANNED:
                if re.search(r"\b" + re.escape(b) + r"\b", txt, re.IGNORECASE if b[0].islower() else 0):
                    print(f"FAIL  {name}: banned word '{b}'"); fails += 1
            if NXBY.search(txt):
                print(f"FAIL  {name}: 'not X, but Y' construction"); fails += 1
            if CLOCK.search(txt):
                print(f"FAIL  {name}: clock time found (durations only)"); fails += 1
            if "₹" in txt:
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
            # nbconvert runs the notebook with its own folder as the working directory, which is
            # what makes the ../data paths in a notebook resolve the way they do for a learner.
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

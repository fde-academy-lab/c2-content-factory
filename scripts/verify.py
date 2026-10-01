"""Verification gate for a day pack. Usage: python3 scripts/verify.py content/W01/D2 [--execute]
--execute additionally cold-runs every notebook via jupyter nbconvert (needs jupyter installed).

Three things are checked beyond the writing rules. Every filename must carry the
C2_W{ww}_D{dd} or C2_W{ww}_SAT stem matching the folder it sits in, so a build pointed at the
wrong day fails here rather than overwriting another day's pack. Every file must sit in one of
the subfolders its folder type allows, so a pack cannot quietly invent its own layout. And no
file may sit loose at the day folder's root.

This one command then calls the five proof scripts, so a pack is proved by running one thing:

  nb_check.py          every code cell carries an output, three diagrams and five checks render
  distractor_audit.py  no key is the longest option, keys spread, no format line gives them away
  xlsx_recalc.py       LibreOffice recalculates the workbook and the verdicts move when flipped
  html_sweep.py        a browser clicks every control on every companion page
  deck_md_check.py     the slide markdown's numbering, titles, question pairing and diagram share

Decks route by extension. The markdown source always goes to deck_md_check.py. A built .pptx goes
to deck_check.py only when it is newer than the markdown it came from, since a stale pptx measures
a deck nobody is shipping; a stale one is named and skipped instead. Every built .pptx is also read
for mermaid source printed on a slide, which is what a deck built on a broken mermaid-cli shows in
place of its diagrams.

A proof script that cannot run in this session (no browser, no LibreOffice) reports what it could
not do and does not fail the gate. A proof script that finds a real defect does fail it.
"""
import sys, re, json, pathlib, subprocess, zipfile

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
# Characters a reader cannot see and a diff barely shows: zero-width marks, direction overrides,
# Unicode tag characters (hidden text), the soft hyphen and the exotic spaces. The list follows the
# invisible-character pass of the seo-content skill (AgriciDaniel/claude-seo, MIT).
INVISIBLE = re.compile("[\u200b\u200c\u200d\u2060\ufeff\u200e\u200f\u202a-\u202e\u2066-\u2069"
                       "\u00ad\u00a0\u2000-\u200a\u202f\u205f\u3000\U000e0000-\U000e007f]")
# A STUDENT file may mention an IITGN faculty session only with its status beside it, because every
# session is tentative until IIT Gandhinagar confirms it (data/programme/facts.yaml).
FACULTY_MENTION = re.compile(r"[^.\n]*\b(IITGN faculty|faculty session|faculty block)\b[^.\n]*",
                             re.IGNORECASE)
DAYS_JSON = pathlib.Path(__file__).resolve().parent.parent / "data" / "programme" / "days.json"
MERMAID_SOURCE = re.compile(r"\b(flowchart (LR|RL|TD|TB|BT)|graph (LR|RL|TD|TB|BT)|xychart-beta|"
                            r"sequenceDiagram|classDef \w)")

# Build weeks per the Structure tab: 3, 6 and 9 in this workbook, then 12 and 15 later in the
# programme. They ship the build-week pack instead of the teaching manifest, so their folders differ.
BUILD_WEEKS = {3, 6, 9, 12, 15}

TEACHING_DIRS = {
    "slides", "notebooks", "sql", "demos", "whiteboards", "cheatsheets", "study-notes",
    "exercises", "exercises/guided", "exercises/unguided", "exercises/practice", "exercises/solutions",
    "takehome", "kahoot", "preread", "extras", "data", "trainer", "internal", "corrections",
}
# A build week can open a domain (US healthcare enters on Build 1 Monday, decision four-domains in
# data/programme/facts.yaml), so a build day may also carry the domain's dossier and its card.
BUILD_DIRS = {
    "briefs", "rubrics", "gd", "parallel-build", "checkpoints", "mocks", "trainer", "internal",
    "data", "slides", "study-notes", "cheatsheets",
}
SAT_RECAP_DIRS = {"paper", "answer-key", "discussion", "internal"}


# Week 0 is the baseline week: teaching-day folders plus the diagnostic papers and their keys.
BASELINE_DIRS = TEACHING_DIRS | {"paper", "answer-key"}


def day_kind(week, day_label):
    """The day's kind from the synced calendar (teaching, saturday, build-week, baseline), or None."""
    try:
        plan = json.loads(DAYS_JSON.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    slot = "SAT" if day_label == "SAT" else f"D{int(day_label[1:])}"
    for d in plan.get("days", []):
        if d["week"] == f"W{week:02d}" and d["slot"] == slot:
            return d["kind"]
    return None


def folder_shape(week, day_label):
    """Which subfolders this day folder is allowed to hold, and what to call the shape."""
    kind = day_kind(week, day_label)
    if kind == "baseline" or (kind is None and week == 0):
        return "baseline day", BASELINE_DIRS
    if kind == "teaching" and day_label == "SAT":
        # A Saturday that teaches, which only Week 16 has, takes the teaching-day shape.
        return "teaching day", TEACHING_DIRS
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


def committed_together(source, built):
    """Whether git holds both files exactly as they are on disk.

    Staleness is a question about content, and a modification time only answers it while nobody has
    touched the working tree. `git checkout` rewrites every timestamp it restores, so a fresh clone
    or a branch switch makes a perfectly good PDF look older than the markdown it was built from,
    and the gate then reports four failures nobody can act on except by rebuilding files that were
    already correct. When git says both files match the commit, they went in together and the
    timestamps say nothing.
    """
    try:
        r = subprocess.run(["git", "status", "--porcelain", "--", str(source), str(built)],
                           capture_output=True, text=True, timeout=30)
    except Exception:
        return False
    return r.returncode == 0 and not r.stdout.strip()


def git_ignored(paths):
    """Paths git is told to ignore, so a notebook's generated output/ is not audited as a pack file.

    A day pack is what it ships, and a file the notebook writes when a learner runs it is
    reproducible from the data and the notebook. Without this, verify.py --execute fails on its own
    side effects the second time anybody runs it.
    """
    if not paths:
        return set()
    try:
        r = subprocess.run(["git", "check-ignore", "--stdin"], input="\n".join(str(p) for p in paths),
                           capture_output=True, text=True)
    except Exception:
        return set()
    return {pathlib.Path(line) for line in r.stdout.splitlines() if line.strip()}


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

HERE = pathlib.Path(__file__).resolve().parent


def run_proof(script, args, why):
    """Call one proof script, echo it under its own banner, and return its failure count."""
    path = HERE / script
    if not path.exists():
        print(f"INFO  {script} is not in scripts/, so {why} was not proved")
        return 0
    print(f"\n--- {script}: {why}")
    r = subprocess.run([sys.executable, str(path), *args], capture_output=True, text=True)
    body = (r.stdout or "") + (r.stderr or "")
    for line in body.rstrip().splitlines():
        print(line)
    if r.returncode == 0:
        return 0
    m = re.search(r"RESULT:\s*FAIL\s*\((\d+) failures\)", body)
    return int(m.group(1)) if m else 1


def run_proofs(target):
    """Every proof the pack's own contents ask for, one command, in a fixed order."""
    files = [p for p in target.rglob("*") if p.is_file()]
    fails = 0

    if any(p.suffix == ".ipynb" for p in files):
        fails += run_proof("nb_check.py", [str(target)],
                           "notebooks carry outputs, diagrams and passing checks")

    if any(p.parent.name in ("unguided", "guided", "kahoot", "paper", "exercises") for p in files):
        fails += run_proof("distractor_audit.py", [str(target)],
                           "no option set gives its key away")

    if any(p.suffix == ".xlsx" for p in files) or any("recalc" in p.name for p in files):
        fails += run_proof("xlsx_recalc.py", [str(target)],
                           "the workbook computes and its verdicts move when a decision flips")

    if any(p.suffix == ".html" for p in files):
        fails += run_proof("html_sweep.py", [str(target)],
                           "every control on every companion page does something")

    decks = [p for p in files if p.parent.name == "slides" and p.suffix == ".md"]
    if decks:
        fails += run_proof("deck_md_check.py", [str(target)],
                           "the slide source numbers, pairs and draws what it should")

    sheets = [p for p in files if p.parent.name == "cheatsheets" and p.suffix == ".md"]
    stale_pdf = [p.with_suffix(".pdf") for p in sheets
                 if p.with_suffix(".pdf").exists()
                 and p.with_suffix(".pdf").stat().st_mtime <= p.stat().st_mtime + 1
                 and not committed_together(p, p.with_suffix(".pdf"))]
    missing_pdf = [p for p in sheets if not p.with_suffix(".pdf").exists()]
    if stale_pdf or missing_pdf:
        for pdf in stale_pdf:
            print(f"\nFAIL  {pdf.name} is not newer than its markdown, so the printed sheet and "
                  f"the source disagree. Rebuild it with scripts/build_cheatsheet.py.")
        for md in missing_pdf:
            print(f"\nFAIL  {md.name} has no PDF beside it, and the sheet a learner pins above a "
                  f"desk is the PDF. Build it with scripts/build_cheatsheet.py.")
        fails += len(stale_pdf) + len(missing_pdf)

    # A Saturday paper is handed out as the Word file, so its markdown needs the Word file beside
    # it, built after the markdown's last change, as a cheat sheet needs its PDF.
    papers = [p for p in files if p.suffix == ".md" and "_SAT_" in p.name
              and p.parent.name in ("paper", "answer-key") and ("recap_paper" in p.name or "answer_key" in p.name)]
    # The builder writes the markdown and the Word file in one run, a second apart at most, so only
    # a Word file strictly older than its markdown is behind it.
    stale_doc = [p.with_suffix(".docx") for p in papers
                 if p.with_suffix(".docx").exists()
                 and p.with_suffix(".docx").stat().st_mtime < p.stat().st_mtime
                 and not committed_together(p, p.with_suffix(".docx"))]
    missing_doc = [p for p in papers if not p.with_suffix(".docx").exists()]
    if stale_doc or missing_doc:
        for doc in stale_doc:
            print(f"\nFAIL  {doc.name} is not newer than its markdown, so the handed-out paper and "
                  f"the source disagree. Rebuild it with scripts/build_saturday_paper.py --docx.")
        for md in missing_doc:
            print(f"\nFAIL  {md.name} has no Word file beside it, and the paper a room sits is the "
                  f"Word file. Build it with scripts/build_saturday_paper.py --docx.")
        fails += len(stale_doc) + len(missing_doc)

    built = [p for p in files if p.parent.name == "slides" and p.suffix == ".pptx"]
    for pptx in built:
        code = mermaid_on_slides(pptx)
        if code:
            print(f"\nFAIL  {pptx.name}: slide(s) {', '.join(map(str, code))} print mermaid source "
                  f"where a diagram belongs, so mermaid-cli failed when the deck was built. Rebuild "
                  f"it with scripts/build_deck.py once mmdc renders.")
            fails += 1
    fresh = []
    for pptx in built:
        source = pptx.with_suffix(".md")
        if not source.exists():
            print(f"\nINFO  {pptx.name} has no markdown source beside it, so it was not measured")
        elif (pptx.stat().st_mtime <= source.stat().st_mtime + 1
              and not committed_together(source, pptx)):
            # A pptx no newer than its markdown was either never rebuilt or restored by a
            # checkout. Git tells the two apart: when it holds both files as they are on disk they
            # were committed together, and only an uncommitted edit means the build really is
            # behind its source.
            print(f"\nINFO  {pptx.name} is not newer than {source.name}, so it is stale and was "
                  f"not measured. Rebuild it from the markdown before it ships.")
        else:
            fresh.append(str(pptx))
    if fresh:
        fails += run_proof("deck_check.py", fresh, "every text box on the built deck fits")

    return fails


def mermaid_on_slides(pptx):
    """The slide numbers whose text carries mermaid source, in slide order."""
    try:
        with zipfile.ZipFile(pptx) as z:
            names = [n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)]
            return sorted(int(re.search(r"(\d+)\.xml$", n).group(1)) for n in names
                          if MERMAID_SOURCE.search(z.read(n).decode("utf-8", "ignore")))
    except zipfile.BadZipFile:
        return []


def main():
    target = pathlib.Path(sys.argv[1])
    execute = "--execute" in sys.argv
    fails = 0
    files = [p for p in target.rglob("*") if p.is_file() and p.name != ".gitkeep"]
    files = [p for p in files if p not in git_ignored(files)]
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
            hidden = INVISIBLE.findall(txt)
            if hidden:
                codes = ", ".join(sorted({f"U+{ord(c):04X}" for c in hidden}))
                print(f"FAIL  {name}: invisible or exotic Unicode characters ({codes})"); fails += 1
            if student:
                for nm in TRAINER_NAMES:
                    if re.search(r"\b" + nm + r"\b", txt):
                        print(f"FAIL  {name}: person name '{nm}' in a STUDENT file"); fails += 1
                for m in FACULTY_MENTION.finditer(txt):
                    if not re.search(r"\b(tentative|confirmed)\b", m.group(0), re.IGNORECASE):
                        print(f"FAIL  {name}: an IITGN faculty session is mentioned without its "
                              f"status: '{m.group(0).strip()[:80]}'"); fails += 1
                if re.search(r"\b(marks|weightage|graded out of)\b", txt, re.IGNORECASE):
                    print(f"WARN  {name}: marks language in a STUDENT file; confirm the Structure tab allows it")
            for line in txt.splitlines():
                if URL.search(line) and not DATED.search(line) and "to be found" not in line.lower():
                    print(f"WARN  {name}: undated link: {line.strip()[:90]}")
        if execute and p.suffix == ".ipynb":
            # A TODO twin stops at its first placeholder on purpose, so cold-running it is not a
            # test of anything. Its executed solution twin is the one that has to run clean.
            if "__TODO" in p.read_text(encoding="utf-8", errors="replace"):
                print(f"INFO  {name}: TODO twin, so it is not cold-run; its solution twin is")
                continue
            # nbconvert runs the notebook with its own folder as the working directory, which is
            # what makes the ../data paths in a notebook resolve the way they do for a learner.
            r = subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute",
                                "--output", "/tmp/_exec_check.ipynb", str(p)],
                               capture_output=True, text=True)
            if r.returncode != 0:
                print(f"FAIL  {name}: cold run failed\n{r.stderr[-400:]}"); fails += 1
            else:
                print(f"PASS  {name}: cold run clean")
    fails += run_proofs(target)
    print("\nRESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()

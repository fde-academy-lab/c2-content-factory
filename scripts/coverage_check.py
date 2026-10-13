"""Coverage gate: does a teaching day teach every subtopic its curriculum row names?

Usage: python3 scripts/coverage_check.py content/W04/D1

A teaching day from Week 4 on carries internal/C2_W{ww}_D{dd}_coverage_INTERNAL.yaml, which names,
for every subtopic in the "Subtopics" section of its row (docs/curriculum/W{n}_*.md), the concept
chapter that teaches it, the deck that holds the chapter, the notebook that pairs with it, and the
exercise and Kahoot items that test it:

    chapters:
      - subtopic: "North-star and guardrail metrics"      # verbatim from the row
        chapter: "North-star and guardrail metrics"       # the chapter's own title in the deck
        deck: slides/C2_W04_D01_half1_STUDENT.md
        notebook: notebooks/C2_W04_D01_02_north_star_and_guardrails_STUDENT.ipynb
        exercises: [exercises/unguided/C2_W04_D01_metric_tree_STUDENT.md#Q3]
        kahoot: [kahoot/C2_W04_D01_kahoot_STUDENT.md#Q4]

The gate fails when a row subtopic has no entry, when the chapter title is not a "## " heading of the
named deck, when the notebook is missing or its title cell does not carry the chapter title, when a
named exercise or Kahoot file or item does not exist, or when no concept chapter comes before the
deck's first case chapter (a heading listed under `case_chapters`). Weeks 1 to 3 were built before
the rule, so a day there without the file is reported and passes; from Week 4 on a teaching day
without the file fails. Build weeks and Saturdays carry no such file.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
BUILD_WEEKS = {3, 6, 9, 12, 15}
FIRST_ENFORCED_WEEK = 4


def norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'")).strip().lower()


def row_subtopics(week, day):
    """The bullets under '### Subtopics' in the day's section of the week's curriculum file."""
    files = sorted((ROOT / "docs/curriculum").glob(f"W{week}_*.md"))
    if not files:
        return None, None
    text = files[0].read_text(encoding="utf-8")
    sections = re.split(r"^## ", text, flags=re.M)[1:]
    sec = next((s for s in sections if s.startswith(DAYS[day - 1] + " ")), None)
    if sec is None:
        return files[0], None
    block = re.search(r"^### Subtopics.*?\n(.*?)(?=^### |\Z)", sec, flags=re.M | re.S)
    items = re.findall(r"^\s*[•\-\*]\s+(.+?)\s*$", block.group(1), flags=re.M) if block else []
    return files[0], items


def headings(deck):
    out = []
    for line in deck.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            out.append(norm(re.sub(r"^## (SECTION \w+:\s*|S\d+[a-z]?\.\s*)?", "", line)))
    return out


def notebook_title(nb):
    cells = json.loads(nb.read_text(encoding="utf-8")).get("cells", [])
    for c in cells:
        if c.get("cell_type") == "markdown":
            return norm("".join(c.get("source", "")).splitlines()[0] if c.get("source") else "")
    return ""


def item_exists(day_dir, ref):
    path, _, item = ref.partition("#")
    f = day_dir / path
    if not f.exists():
        return False, f"{path} does not exist"
    if item and not re.search(r"\b" + re.escape(item) + r"\b", f.read_text(encoding="utf-8")):
        return False, f"{path} has no item {item}"
    return True, ""


def main():
    day_dir = pathlib.Path(sys.argv[1]).resolve()
    m = re.search(r"W(\d{2})[/\\]D(\d)$", str(day_dir))
    if not m:
        print("INFO  not a teaching day folder, so coverage is not checked\nRESULT: PASS (0 failures)")
        return 0
    week, day = int(m.group(1)), int(m.group(2))
    if week in BUILD_WEEKS:
        print("INFO  a build week carries no coverage matrix\nRESULT: PASS (0 failures)")
        return 0
    cov = day_dir / "internal" / f"C2_W{week:02d}_D{day:02d}_coverage_INTERNAL.yaml"
    row_file, subtopics = row_subtopics(week, day)
    fails = []
    if not cov.exists():
        msg = f"no coverage matrix ({cov.name}) for {len(subtopics or [])} row subtopics"
        if week >= FIRST_ENFORCED_WEEK:
            print(f"FAIL  {msg}\nRESULT: FAIL (1 failures)")
            return 1
        print(f"INFO  {msg}; Weeks 1 to 3 predate the rule\nRESULT: PASS (0 failures)")
        return 0
    if not subtopics:
        print(f"FAIL  no Subtopics section found for {DAYS[day - 1]} in {row_file}\nRESULT: FAIL (1 failures)")
        return 1
    import yaml
    spec = yaml.safe_load(cov.read_text(encoding="utf-8")) or {}
    entries = spec.get("chapters") or []
    by_sub = {norm(e.get("subtopic", "")): e for e in entries}
    first_concept, first_case = {}, {}
    for sub in subtopics:
        e = by_sub.get(norm(sub))
        if not e:
            fails.append(f"row subtopic has no chapter: '{sub}'")
            continue
        deck = day_dir / e.get("deck", "")
        if not deck.is_file():
            fails.append(f"'{sub}': deck {e.get('deck')} does not exist")
        else:
            hs = headings(deck)
            title = norm(e.get("chapter", ""))
            pos = next((i for i, h in enumerate(hs) if title and title in h), None)
            if pos is None:
                fails.append(f"'{sub}': no '## ' heading in {deck.name} carries the chapter title '{e.get('chapter')}'")
            else:
                first_concept[deck] = min(first_concept.get(deck, pos), pos)
        nb = day_dir / e.get("notebook", "")
        if not nb.is_file():
            fails.append(f"'{sub}': notebook {e.get('notebook')} does not exist")
        elif norm(e.get("chapter", "")) not in notebook_title(nb):
            fails.append(f"'{sub}': {nb.name} opens on '{notebook_title(nb)[:60]}', not the chapter title")
        for ref in (e.get("exercises") or []) + (e.get("kahoot") or []):
            ok, why = item_exists(day_dir, ref)
            if not ok:
                fails.append(f"'{sub}': {why}")
        if not (e.get("exercises") or []):
            fails.append(f"'{sub}': no exercise item tests it")
    for c in spec.get("case_chapters") or []:
        deck = day_dir / c.get("deck", "")
        if deck.is_file():
            hs = headings(deck)
            pos = next((i for i, h in enumerate(hs) if norm(c.get("chapter", "")) in h), None)
            if pos is not None:
                first_case[deck] = min(first_case.get(deck, pos), pos)
    for deck, pos in first_case.items():
        if deck in first_concept and first_concept[deck] > pos:
            fails.append(f"{deck.name}: a case chapter comes before the first concept chapter")
    for f in fails:
        print(f"FAIL  {f}")
    print(f"INFO  {len(subtopics)} row subtopics, {len(entries)} chapters in the matrix")
    print(f"RESULT: {'PASS' if not fails else 'FAIL'} ({len(fails)} failures)")
    return len(fails)


if __name__ == "__main__":
    sys.exit(1 if main() else 0)

# Test inputs and expected outcomes:
#   python3 scripts/coverage_check.py content/W04/D1   -> FAIL until the day carries its matrix;
#                                                         PASS once every subtopic maps to a chapter,
#                                                         a titled notebook and an exercise item
#   python3 scripts/coverage_check.py content/W02/D1   -> PASS with an INFO line (Weeks 1 to 3 predate the rule)
#   python3 scripts/coverage_check.py content/W03/D2   -> PASS with an INFO line (a build week)
#   python3 scripts/coverage_check.py content/W04/SAT  -> PASS with an INFO line (not a teaching day)

"""Prove a day pack teaches every subtopic of its curriculum row, by name.

Usage:
    python3 scripts/coverage_check.py content/W04/D1            # check the pack
    python3 scripts/coverage_check.py content/W04/D1 --matrix   # print the matrix skeleton from the row

The row's Subtopics column is the day's chapter list (decision concept-first-case-second). This
reads the row, reads the pack's coverage matrix in internal/, and fails the pack when a subtopic
has no chapter or no notebook carrying its name, when the matrix names a slide, file or item that
does not exist, when a case chapter applies no subtopic or comes before a concept chapter it
applies, or when half1 opens on anything but a concept chapter. Weeks before the decision's
applies_from_week, build weeks, Saturdays and Week 0 are skipped with an INFO line.

The matrix's shape and every rule applied here are set out in
.claude/skills/day-pack-builder/references/coverage-matrix.md. With --matrix the skeleton goes to
standard output alone, so it can be redirected into internal/C2_W{ww}_D{dd}_coverage_INTERNAL.md,
and any message goes to standard error. Test inputs and expected outcomes close this file.
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
FACTS = ROOT / "data/programme/facts.yaml"
DAYS_JSON = ROOT / "data/programme/days.json"
CURRICULUM = ROOT / "docs/curriculum"
DECISION = "concept-first-case-second"
ADDED = "(added by the spine)"
TO_FILL = "to be filled"
PILL = 24  # the short question's guide length in characters; the warning allows two over
STOP = {"the", "a", "and", "of", "in", "on", "by", "against", "its", "that", "it", "read", "before"}
TARGET = re.compile(r"W(\d+)/(D\d+|SAT)/?$")
SECTION = re.compile(r"^##\s+(SECTION\b.*)$")
SLIDE = re.compile(r"^##\s+[SD](\d+)\.", re.M)
QHEAD = re.compile(r"^#{2,3}\s+Q(\d+)\b", re.M)
QREF = re.compile(r"\bQ(\d+)(?:\s*(?:to|-)\s*Q?(\d+))?")
STEM = re.compile(r"^C2_W\d{2}_(?:D\d{2}|SAT)_(.+)_(?:STUDENT|TRAINER|INTERNAL)\.[A-Za-z0-9]+$")
NB_NUMBER = re.compile(r"^C2_W\d{2}_D\d{2}_(\d{2})_")
SECTION_NUMBER = re.compile(r"^SECTION\s*(\d+)")


class Report:
    """Lines tagged PASS, FAIL, WARN or INFO, and the count of failures."""

    def __init__(self, stream=sys.stdout):
        self.stream, self.fails = stream, 0

    def line(self, tag, text):
        print(f"{tag:<5} {text}", file=self.stream)

    def fail(self, text):
        self.fails += 1
        self.line("FAIL", text)

    def result(self):
        print(f"RESULT: {'FAIL' if self.fails else 'PASS'} ({self.fails} failures)", file=self.stream)
        return 1 if self.fails else 0


# --------------------------------------------------------------------------- words and names
def squash(text):
    """Whitespace collapsed and curly quotes made straight, so a pasted bullet still compares."""
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip()


def words(text):
    """Lower-case words with punctuation read as spaces and a possessive 's dropped."""
    text = re.sub(r"['’]s\b", "", text.lower())
    return [w for w in re.split(r"[^a-z0-9]+", text) if w]


def idea_words(text):
    seen = []
    for w in words(text):
        if w not in STOP and w not in seen:
            seen.append(w)
    return seen


def same(a, b):
    """Two words match when equal, or when one is a prefix of the other and the shorter has four letters."""
    if a == b:
        return True
    short, long_ = sorted((a, b), key=len)
    return len(short) >= 4 and long_.startswith(short)


def holds_phrase(hay, needle):
    """Whether the word list `hay` holds `needle` as a run of words, matched word by word."""
    n = len(needle)
    return n > 0 and any(all(same(hay[i + k], needle[k]) for k in range(n)) for i in range(len(hay) - n + 1))


def starts_with(hay, needle):
    return 0 < len(needle) <= len(hay) and all(same(h, w) for h, w in zip(hay, needle))


def split_title(title):
    """'SECTION 4: Definitions: a, b: which four lines?' gives the topic and the short question."""
    rest = re.sub(r"^SECTION\s*\d*\s*[:.]?\s*", "", title)
    cut = rest.rfind(": ")
    if rest.endswith("?") and cut > 0:
        return rest[:cut].strip(), rest[cut + 2:].strip()
    return rest.strip(), None


def topic_half(path):
    m = STEM.match(path.name)
    return re.sub(r"^\d{2}_", "", m.group(1) if m else path.stem)


def spans(nums):
    """[41, 42, 43, 50] reads '41 to 43, 50'."""
    nums, out = sorted(set(nums)), []
    for n in nums:
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return ", ".join(f"{a} to {b}" if b > a else str(a) for a, b in out)


def unfilled(cell):
    return not cell or cell.strip().lower() in (TO_FILL, "")


def rel(path):
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


# --------------------------------------------------------------------------- the sources
def applies_from():
    facts = yaml.safe_load(FACTS.read_text(encoding="utf-8")) or {}
    for d in facts.get("decisions") or []:
        if d.get("id") == DECISION:
            m = re.fullmatch(r"W?0*(\d+)", str(d.get("applies_from_week", "")).strip())
            return int(m.group(1)) if m else None
    return None


def day_entry(week, slot):
    data = json.loads(DAYS_JSON.read_text(encoding="utf-8"))
    return next((d for d in data.get("days", []) if d.get("week") == f"W{week:02d}"
                 and d.get("slot") == slot), None)


def find_row(week, date):
    """The day's heading line and its Subtopics bullets, or the reason they cannot be found."""
    files = sorted(CURRICULUM.glob(f"W{week}_*.md"))
    if not files:
        return None, None, f"no curriculum file docs/curriculum/W{week}_*.md"
    path = files[0]
    lines = path.read_text(encoding="utf-8").splitlines()
    head = date.strftime("%a %d %b %Y")
    start = next((i for i, x in enumerate(lines) if x.startswith("## ") and x[3:].startswith(head)), None)
    if start is None:
        return path, None, f"{rel(path)} has no day heading '## {head}'"
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    section = lines[start:end]
    at = next((i for i, x in enumerate(section) if x.startswith("### Subtopics")), None)
    if at is None:
        return path, None, f"{rel(path)} has no '### Subtopics' section under '## {head}'"
    bullets = []
    for x in section[at + 1:]:
        if x.startswith("#"):
            break
        m = re.match(r"^\s*[•*-]\s+(.*\S)\s*$", x)
        if m:
            bullets.append(squash(m.group(1)))
    if not bullets:
        return path, None, f"the Subtopics section under '## {head}' in {rel(path)} lists no bullet"
    return path, (lines[start], bullets), None


def skeleton(week, entry, row_path, heading, bullets):
    date = dt.date.fromisoformat(entry["date"])
    title = " · ".join(p.strip() for p in heading[3:].split("·")[:2])
    out = [f"# Coverage matrix, Week {week} {date.strftime('%A')}", "",
           f'Row: {rel(row_path)}, "{title}"', f"Subtopics in the row: {len(bullets)}", "",
           "## The row's subtopics and where each is taught", "",
           "| # | Subtopic (verbatim from the row) | Name in the chapter title and the notebook | Chapter "
           "| Slides | Notebook | Exercise items | Kahoot items | Minutes |",
           "|---|---|---|---|---|---|---|---|---|"]
    for i, b in enumerate(bullets, 1):
        cell = b.replace("|", "\\|")
        out.append(f"| {i} | {cell} | {cell} | " + " | ".join([TO_FILL] * 6) + " |")
    out += ["", "## The case chapters and the subtopics each applies", "",
            "| Chapter | Applies (the # of each subtopic) | Slides | Notebook |", "|---|---|---|---|",
            "| " + " | ".join([TO_FILL] * 4) + " |"]
    return "\n".join(out)


# --------------------------------------------------------------------------- the pack
def tables(text):
    """Every markdown table in the text as (column keys, rows), a key being a header's first word."""
    found, cur = [], None
    for line in text.splitlines() + [""]:
        s = line.strip()
        if not s.startswith("|"):
            if cur:
                found.append(cur)
            cur = None
            continue
        cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s.strip().strip("|"))]
        if cur is None:
            keys = [re.sub(r"[^a-z#]", "", (c.split() or [""])[0].lower()) for c in cells]
            cur = (keys, [])
        elif all(re.fullmatch(r":?-+:?", c) for c in cells if c):
            continue
        else:
            cur[1].append(dict(zip(cur[0], cells + [""] * (len(cur[0]) - len(cells)))))
    return found


def section_headings(day):
    """Every '## SECTION' title of the half decks, whitespace collapsed, with its deck and its place.

    The place is (the half's number, the line), so half1's chapters come before half2's and a deck's
    chapters keep the order they are taught in.
    """
    found = {}
    for deck in sorted((day / "slides").glob("*half*_STUDENT.md")):
        m = re.search(r"half(\d+)", deck.name)
        half = int(m.group(1)) if m else 99
        for i, line in enumerate(deck.read_text(encoding="utf-8").splitlines()):
            h = SECTION.match(line)
            if h:
                found.setdefault(squash(h.group(1)), (deck, (half, i)))
    return found


def deck_slides(day):
    decks = {}
    for f in sorted((day / "slides").glob("*_STUDENT.md")):
        m = STEM.match(f.name)
        if m:
            decks[m.group(1)] = {int(n) for n in SLIDE.findall(f.read_text(encoding="utf-8"))}
    return decks


def q_numbers(cell):
    nums = []
    for a, b in QREF.findall(cell):
        nums += list(range(int(a), int(b) + 1)) if b else [int(a)]
    return nums


def first_heading(nb):
    """The first '# ' line of the notebook's first markdown cell, '' if it has none, None if unreadable."""
    try:
        cells = json.loads(nb.read_text(encoding="utf-8")).get("cells", [])
    except (OSError, ValueError):
        return None
    for c in cells:
        if c.get("cell_type") == "markdown":
            src = c.get("source", "")
            for line in ("".join(src) if isinstance(src, list) else src).splitlines():
                if line.startswith("# "):
                    return line[2:].strip()
            return ""
    return ""


def check_slides(cell, decks, where, out):
    if unfilled(cell):
        out.fail(f"{where}: the Slides cell is not filled")
        return
    names = sorted(decks, key=len, reverse=True)
    marks = [(m.start(), m.group(0)) for m in re.finditer(
        r"\b(" + "|".join(re.escape(n) for n in names) + r")\b", cell)] if names else []
    if not marks or re.search(r"\b[SD]\d+", cell[:marks[0][0]]):
        out.fail(f"{where}: '{cell}' gives slide numbers without a deck from slides/ before them")
        return
    for k, (pos, deck) in enumerate(marks):
        part = cell[pos + len(deck):marks[k + 1][0] if k + 1 < len(marks) else len(cell)]
        nums = []
        for a, b in re.findall(r"\b[SD](\d+)(?:\s*(?:to|-)\s*[SD]?(\d+))?", part):
            nums += list(range(int(a), int(b) + 1)) if b else [int(a)]
        if not nums:
            out.fail(f"{where}: '{deck}' is named with no slide number")
        missing = [n for n in nums if n not in decks[deck]]
        if missing:
            out.fail(f"{where}: {deck} has no slide numbered {spans(missing)}")


def check_items(cell, day, where, out):
    if unfilled(cell):
        out.fail(f"{where}: the Exercise items cell is not filled")
        return 0
    files = [f for f in sorted((day / "exercises").rglob("*.md")) if "solutions" not in f.parts]
    count = 0
    for part in [p.strip() for p in cell.split(";") if p.strip()]:
        m = re.match(r"^(.*?)\s*\bQ\d", part)
        stem = m.group(1).strip(" ,:`").lower() if m else ""
        nums = q_numbers(part)
        if not stem or not nums:
            out.fail(f"{where}: exercise reference '{part}' needs a file stem and a Q number")
            continue
        hits = [f for f in files if stem in re.sub(r"C2_W\d{2}_(D\d{2}|SAT)_", "",
                                                   f.relative_to(day / "exercises").as_posix().lower())]
        if not hits:
            out.fail(f"{where}: no file under exercises/ outside solutions/ matches '{stem}'")
            continue
        have = set().union(*({int(n) for n in QHEAD.findall(f.read_text(encoding="utf-8"))} for f in hits))
        for n in nums:
            if n in have:
                count += 1
            else:
                out.fail(f"{where}: no '{stem}' file holds a Q{n} heading")
    return count


def check_kahoot(cell, day, where, out):
    if unfilled(cell):
        out.fail(f"{where}: the Kahoot items cell is not filled")
        return 0
    nums = q_numbers(cell)
    have = set()
    for f in sorted((day / "kahoot").glob("*.md")):
        have |= {int(n) for n in QHEAD.findall(f.read_text(encoding="utf-8"))}
    if not nums:
        out.fail(f"{where}: '{cell}' names no Kahoot Q number")
    for n in nums:
        if n not in have:
            out.fail(f"{where}: kahoot/ holds no Q{n} heading")
    return len([n for n in nums if n in have])


def check_notebooks(cell, day, name, topics, where, out):
    """The notebooks exist, open on the Name or their chapter's topic, and carry the Name in their file names."""
    if unfilled(cell):
        out.fail(f"{where}: the Notebook cell is not filled")
        return
    paths = [p.strip().strip("`") for p in cell.split(";") if p.strip()]
    if len(topics) > 1 and len(paths) != len(topics):
        out.fail(f"{where}: {len(topics)} chapters but {len(paths)} notebooks; a spanning set pairs them one to one")
    ideas, need_all = idea_words(name), len(idea_words(name)) < 3
    carried = set()
    for i, p in enumerate(paths):
        nb = day / p
        if not nb.is_file():
            out.fail(f"{where}: notebook {p} does not exist")
            continue
        head = first_heading(nb)
        topic = topics[min(i, len(topics) - 1)] if topics else ""
        if head is None:
            out.fail(f"{where}: {nb.name} does not parse as a notebook")
        elif not (starts_with(words(head), words(name)) or (topic and starts_with(words(head), words(topic)))):
            out.fail(f"{where}: {nb.name} opens on '{head[:70]}', which starts with neither the Name nor "
                     f"its chapter's topic")
        tokens = topic_half(nb).lower().split("_")
        got = [w for w in ideas if any(same(w, t) for t in tokens)]
        carried |= set(got)
        if len(paths) == 1:
            need = len(ideas) if need_all else 2
            if len(got) < need:
                out.fail(f"{where}: {nb.name} carries {len(got)} of the Name's words in its file name "
                         f"({', '.join(got) or 'none'}); it needs {need}")
        elif not got:
            out.fail(f"{where}: {nb.name} carries no word of the Name '{name}' in its file name")
    if len(paths) > 1:
        miss = [w for w in ideas if w not in carried]
        if miss:
            out.fail(f"{where}: the notebooks' file names together miss {', '.join(miss)} of the Name")


def check_numbers(chapters, cell, out):
    """Warn where a notebook's number is not its chapter's SECTION number."""
    paths = [p.strip().strip("`") for p in (cell or "").split(";") if p.strip()]
    if not chapters or not paths or paths[0].lower() in ("none", TO_FILL):
        return
    pairs = list(zip(chapters, paths)) if len(chapters) > 1 else [(chapters[0], p) for p in paths]
    for chapter, p in pairs:
        n, s = NB_NUMBER.match(pathlib.Path(p).name), SECTION_NUMBER.match(chapter)
        if n and s and int(n.group(1)) != int(s.group(1)):
            out.line("WARN", f"{pathlib.Path(p).name} is numbered {n.group(1)} and its chapter is "
                             f"SECTION {s.group(1)}; a notebook takes its chapter's SECTION number")


def check_order(heads, concepts, of, cases, out):
    """half1 opens on a concept chapter, and every case chapter comes after the concept chapters it applies."""
    firsts = sorted((place, h) for h, (deck, place) in heads.items() if place[0] == 1)
    if not firsts:
        out.fail("slides/*half1*_STUDENT.md holds no '## SECTION' heading, so no concept chapter opens the day")
    elif firsts[0][1] not in concepts:
        out.fail(f"half1 opens on '{firsts[0][1]}', which is no subtopic's chapter; the concept block opens "
                 f"the day")
    late = 0
    for chapter, applied in cases:
        at = heads[chapter][1]
        for n in applied:
            for e in of.get(n, []):
                if heads[e][1] > at:
                    late += 1
                    out.fail(f"case chapter '{chapter}' applies subtopic {n} before its concept chapter '{e}'")
    if firsts and firsts[0][1] in concepts and not late:
        out.line("PASS", "teaching order: half1 opens on a concept chapter, and every case chapter follows "
                         "the concept chapters it applies")


def check_pack(day, week, slot, bullets, out):
    stem = "SAT" if slot == "SAT" else f"D{int(slot[1:]):02d}"
    matrix = day / "internal" / f"C2_W{week:02d}_{stem}_coverage_INTERNAL.md"
    if not matrix.is_file():
        out.fail(f"no coverage matrix at {rel(matrix)}; write its skeleton with "
                 f"python3 scripts/coverage_check.py {rel(day)} --matrix")
        return
    found = tables(matrix.read_text(encoding="utf-8"))
    first = next((t for t in found if "subtopic" in t[0]), None)
    second = next((t for t in found if "applies" in t[0]), None)
    if first is None:
        out.fail(f"{matrix.name} has no table with a Subtopic column")
        return
    want = ["#", "subtopic", "name", "chapter", "slides", "notebook", "exercise", "kahoot", "minutes"]
    lack = [k for k in want if k not in first[0]]
    if lack:
        out.fail(f"{matrix.name}: the first table has no {', '.join(lack)} column")
        return
    heads, decks = section_headings(day), deck_slides(day)
    rows = first[1]
    by_sub = {}
    for r in rows:
        by_sub.setdefault(squash(r["subtopic"]), []).append(r)
    for i, b in enumerate(bullets, 1):
        if b not in by_sub:
            out.fail(f"row subtopic {i} '{b}' has no row in the matrix")
    added = [r for r in rows if squash(r["subtopic"]) not in bullets]
    for r in added:
        if not squash(r["subtopic"]).endswith(ADDED):
            out.fail(f"matrix row {r['#']} '{r['subtopic']}' is not a bullet of the row and is not marked {ADDED}")
    if len([r for r in added if squash(r["subtopic"]).endswith(ADDED)]) > 1:
        out.line("WARN", f"more than one subtopic is marked {ADDED}; the reference allows one a day")

    named, minutes, uses, of, cases = set(), 0, {}, {}, []
    for r in rows:
        for e in re.split(r";\s*(?=(?:##\s*)?SECTION\b)", r["chapter"]):
            uses.setdefault(squash(e.strip().strip("`").lstrip("#")), []).append(r["#"])
    for r in rows:
        sub, num = squash(r["subtopic"]), r["#"]
        if sub not in bullets and not sub.endswith(ADDED):
            continue
        name = squash(r["name"]) or sub
        where = f"subtopic {num} '{sub}'"
        bare = sub.replace(ADDED, "").strip()
        sub_ideas, name_ideas = idea_words(bare), idea_words(name)
        kept = [w for w in sub_ideas if any(same(w, n) for n in name_ideas)]
        if len(kept) * 2 < len(sub_ideas):
            out.line("WARN", f"Name '{name}' keeps {len(kept)} of the subtopic's {len(sub_ideas)} words")
        topics, fails_before = [], out.fails
        if unfilled(r["chapter"]):
            out.fail(f"{where}: no chapter carries its name, since the Chapter cell is not filled")
        else:
            entries = [squash(e.strip().strip("`").lstrip("#"))
                       for e in re.split(r";\s*(?=(?:##\s*)?SECTION\b)", r["chapter"])]
            if len(entries) == 1 and words(name) != words(bare):
                out.fail(f"{where}: its Name '{name}' is not the subtopic as the row words it; only a "
                         f"subtopic that spans several chapters shortens its Name")
            for e in entries:
                if e not in heads:
                    out.fail(f"{where}: '{e}' is no '## SECTION' heading of slides/*half*_STUDENT.md")
                    continue
                named.add(e)
                of.setdefault(num.strip(), []).append(e)
                topic, question = split_title(e)
                topics.append(topic)
                if question is None:
                    out.line("WARN", f"'{e}' has no short question after its topic")
                elif len(question) > PILL + 2:
                    out.line("WARN", f"'{e}': its short question runs to {len(question)} characters; "
                                     f"the pills print about {PILL}")
            if len(entries) == 1 and topics:
                if not holds_phrase(words(topics[0]), words(name)):
                    shared = [n for n in uses.get(entries[0], []) if n != num]
                    note = f", which it shares with subtopic {', '.join(shared)}" if shared else ""
                    out.fail(f"{where}: chapter '{entries[0]}' does not carry the Name '{name}'{note}")
            elif len(entries) > 1 and topics:
                for e, t in zip([e for e in entries if e in heads], topics):
                    if not any(same(w, x) for w in name_ideas for x in words(t)):
                        out.fail(f"{where}: chapter '{e}' carries no word of the Name '{name}'")
                miss = [w for w in name_ideas if not any(same(w, x) for t in topics for x in words(t))]
                if miss:
                    out.fail(f"{where}: its chapters together miss {', '.join(miss)} of the Name")
        check_notebooks(r["notebook"], day, name, topics, where, out)
        check_numbers([e for e in of.get(num.strip(), [])], r["notebook"], out)
        check_slides(r["slides"], decks, where, out)
        items = check_items(r["exercise"], day, where, out)
        quiz = check_kahoot(r["kahoot"], day, where, out)
        m = re.match(r"\s*(\d+)", r["minutes"] or "")
        minutes += int(m.group(1)) if m else 0
        if out.fails == fails_before:
            out.line("PASS", f"{where}: {len(topics)} chapter(s), {items} exercise item(s), "
                             f"{quiz} Kahoot item(s), {m.group(1) if m else '?'} minutes")
    out.line("INFO", f"the concept block runs {minutes} minutes in the matrix")

    numbers = {r["#"].strip() for r in rows}
    in_second = set()
    if second is None:
        out.fail(f"{matrix.name} has no table with an Applies column for the case chapters")
    else:
        for r in second[1]:
            chapter = squash((r.get("chapter") or "").strip().strip("`").lstrip("#"))
            if unfilled(chapter):
                out.fail("a case chapter row of the second table is not filled")
                continue
            if chapter not in heads:
                out.fail(f"case chapter '{chapter}' is no '## SECTION' heading of slides/*half*_STUDENT.md")
                continue
            in_second.add(chapter)
            topic, question = split_title(chapter)
            if question is None:
                out.line("WARN", f"'{chapter}' has no short question after its topic")
            elif len(question) > PILL + 2:
                out.line("WARN", f"'{chapter}': its short question runs to {len(question)} characters; "
                                 f"the pills print about {PILL}")
            cell = r.get("applies") or ""
            if cell.strip().lower() == "all":
                applied = sorted(numbers)
            else:
                applied = []
                for a, b in re.findall(r"(\d+)(?:\s*(?:to|-)\s*(\d+))?", cell):
                    applied += [str(n) for n in (range(int(a), int(b) + 1) if b else [int(a)])]
            if not applied:
                out.fail(f"case chapter '{chapter}' applies no subtopic")
            bad = [n for n in applied if n not in numbers]
            if bad:
                out.fail(f"case chapter '{chapter}' applies subtopic {', '.join(bad)}, which the first table lacks")
            cases.append((chapter, [n for n in applied if n in numbers]))
            check_slides(r.get("slides", ""), decks, f"case chapter '{chapter}'", out)
            nb = (r.get("notebook") or "").strip()
            if not nb or nb.lower() == "none":
                out.line("WARN", f"case chapter '{chapter}' names no notebook; every case chapter pairs with one")
            elif nb.lower() == TO_FILL:
                out.fail(f"case chapter '{chapter}': the Notebook cell is not filled")
            else:
                for p in [p.strip().strip("`") for p in nb.split(";") if p.strip()]:
                    if not (day / p).is_file():
                        out.fail(f"case chapter '{chapter}': notebook {p} does not exist")
                check_numbers([chapter], nb, out)
    for h, (deck, _) in heads.items():
        if h not in named and h not in in_second:
            out.fail(f"chapter '{h}' in {deck.name} is neither a subtopic's chapter nor a case chapter "
                     f"in the matrix")
    check_order(heads, named, of, cases, out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="a day folder, content/W{ww}/D{d}")
    ap.add_argument("--matrix", action="store_true", help="print the matrix skeleton from the row")
    a = ap.parse_args(argv)
    out = Report(sys.stderr if a.matrix else sys.stdout)
    target = pathlib.Path(a.target)
    m = TARGET.search(target.resolve().as_posix())
    if not m:
        out.line("INFO", f"coverage gate does not apply to {a.target} (not a W{{ww}}/D{{d}} folder)")
        return 0 if a.matrix else out.result()
    week = int(m.group(1))
    slot = "SAT" if m.group(2) == "SAT" else f"D{int(m.group(2)[1:])}"
    start = applies_from()
    if start is None:
        out.fail(f"data/programme/facts.yaml holds no decision {DECISION} with an applies_from_week")
        return out.result()
    reason = None
    entry = day_entry(week, slot)
    if week < start:
        reason = f"week before W{start:02d}"
    elif entry is None:
        reason = "no such day in data/programme/days.json"
    elif entry.get("kind") != "teaching":
        reason = entry.get("kind") or "no kind in data/programme/days.json"
    if reason:
        out.line("INFO", f"coverage gate does not apply to {a.target} ({reason})")
        return 0 if a.matrix else out.result()
    row_path, row, why = find_row(week, dt.date.fromisoformat(entry["date"]))
    if why:
        out.fail(why)
        return out.result()
    heading, bullets = row
    if a.matrix:
        print(skeleton(week, entry, row_path, heading, bullets))
        return 0
    day_label = heading[3:].split("·")[0].strip()
    out.line("INFO", f"row: {rel(row_path)}, '{day_label}', {len(bullets)} subtopics")
    day = target.resolve()
    if not day.is_dir():
        out.fail(f"{a.target} is not a folder")
        return out.result()
    check_pack(day, week, slot, bullets, out)
    return out.result()


if __name__ == "__main__":
    sys.exit(main())

# Test inputs and expected outcomes
# --------------------------------
# python3 scripts/coverage_check.py content/W04/D1           (the pack as merged, before its rebuild)
#     FAIL  no coverage matrix at content/W04/D1/internal/C2_W04_D01_coverage_INTERNAL.md; exit 1.
# The same, after the skeleton alone is written into internal/
#     A FAIL for every cell still "to be filled", six of them saying no chapter carries the subtopic's
#     name, and a FAIL for each SECTION heading the matrix does not name: RESULT: FAIL (n failures),
#     n at least 6.
# python3 scripts/coverage_check.py content/W01/D1   and   content/W03/D2
#     INFO  coverage gate does not apply ... (week before W04); exit 0, with no folder needed.
# python3 scripts/coverage_check.py content/W04/SAT
#     INFO  coverage gate does not apply ... (saturday); exit 0.
# python3 scripts/coverage_check.py content/W04/D3 --matrix
#     Five subtopic rows, the first "Support, confidence and lift, derived by counting", on standard
#     output alone; exit 0.
# A row whose Name is "Guardrails" for "North-star and guardrail metrics", its chapter
# "SECTION 2: North-star and guardrail metrics: which number to chase?"
#     The chapter carries the Name (guardrail matches guardrails), and the run prints
#     WARN  Name 'Guardrails' keeps 1 of the subtopic's 4 words, and, since one chapter teaches it,
#     FAIL  ... its Name 'Guardrails' is not the subtopic as the row words it.
# The same subtopic with the Name in full and the chapter "SECTION 2: Guardrails: which number to chase?"
#     FAIL  ... chapter 'SECTION 2: Guardrails: which number to chase?' does not carry the Name.
# A chapter "SECTION 4: Definitions: numerator, denominator, window, exclusions: which four lines?"
#     Its topic is everything before the last colon, so it carries the whole Name.
# A notebook 04_definition_lines for "Definitions: numerator, denominator, window, exclusions"
#     FAIL: it carries 1 of the Name's words (definitions) in its file name; it needs 2.
# data/programme/facts.yaml without decision concept-first-case-second
#     FAIL naming the missing decision; exit 1 for every target.
# Throwaway packs in a scratch folder whose path ends W04/D1, W04/D3 or W04/D5, each with the two half
# decks, the notebooks, a guided set, a Kahoot and the matrix (run on 13 October 2026, then removed):
#   Monday: SECTIONs 1 to 6 the concept chapters, 7 to 9 the case in half1, 10 and 11 in half2
#     PASS  teaching order ...; RESULT: PASS (0 failures), with a WARN for each case chapter that
#     names no notebook.
#   The same with SECTION 6 moved after SECTION 7, which applies subtopics 1 and 6
#     FAIL  case chapter 'SECTION 7: ...' applies subtopic 6 before its concept chapter 'SECTION 6: ...'.
#   The same with SECTION 7, applying subtopics 1 and 4, first in half1
#     FAIL  half1 opens on 'SECTION 7: ...', which is no subtopic's chapter, and a FAIL for each of
#     subtopics 1 and 4 taught after it: RESULT: FAIL (3 failures).
#   The same with SECTION 7's notebook named C2_W04_D01_10_proxy_test_on_twelve_rows_STUDENT.ipynb
#     WARN  ... is numbered 10 and its chapter is SECTION 7; RESULT: PASS (0 failures).
#   Wednesday: SECTION 9, the cross-sell concept chapter, opens half2 before SECTION 10 applies it
#     RESULT: PASS (0 failures).
#   The same with half1's SECTION 8 applying subtopics 1 to 5
#     FAIL  case chapter 'SECTION 8: ...' applies subtopic 5 before its concept chapter 'SECTION 9: ...'.
#   Friday: subtopics 4 and 5 share SECTION 4 and its notebook 04
#     RESULT: PASS (0 failures).

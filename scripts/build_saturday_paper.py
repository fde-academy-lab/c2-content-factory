"""Render a week's Saturday recap paper and its key from the tracker's item bank.

    python3 scripts/build_saturday_paper.py W01            # write Week 1's paper and key
    python3 scripts/build_saturday_paper.py W01 --docx     # the same, plus both as Word files
    python3 scripts/build_saturday_paper.py --all          # every week with a SAT folder and a paper
    python3 scripts/build_saturday_paper.py W01 --check    # write nothing; exit 1 if either differs

The bank is the 'Saturday papers' tab of docs/curriculum/source.xlsx. A week whose source file
lists `parts` prints in parts, each named for what it shows, opening on its situation and lettered
exhibits, with every item's format and level beside its number; page one carries the blueprint (part,
what it shows, items, minutes and the easy, medium and hard mix) and the rules. A week without parts
prints in the older layout, sections by item type in the bank's order. Either way the paper is
numbered Q1 upward as printed and carries a line for the name and the count of items right and
nothing else. The TRAINER key carries every other column (key, type, part, level, tag, roles, day,
minutes and the interview anchor), the marking rule, what guessing alone would score, and the item
numbers by tag, level, day and part, which is what the Academic TA tallies for Monday's remediation
read. With --docx the builder also writes the item-analysis workbook the TA fills after marking,
with its recalc manifest.

Three sources are laid on the bank before rendering:

  data/programme/paper_edits.yaml    rewords options of one item, never its stem or key
  data/programme/facts.yaml          saturday_papers.paper_minutes, where a paper runs longer than
                                     the tracker's slot
  content/W{ww}/SAT/internal/C2_W{ww}_SAT_paper_source_INTERNAL.yaml, the week's own additions:
      parts       the printed order: a list of parts, each with a title, `shows` (what the part
                  shows about the learner), an optional intro and optional `exhibits`, and `items`,
                  which name bank items by number and additions as new:<id>; every bank item sits
                  in one part or in stretch_bank, and a scenario set stays whole and in order
      stretch_bank  at most six bank items of the recall types (fill in the blank, true or false)
                  moved to the untimed stretch page to make room for harder timed items, a move
                  the requester approved on 30 September 2026
      additions   new timed items, each carrying why, wrong and answer for the key, an `id` that
                  parts name it by, an optional `exhibit` and an optional `label`; listed in the key
                  as waiting for the tracker
      purpose     the paragraph under "What this paper is for" on the Word paper's first page, written
                  for the week: its case, its stakeholders and what the paper finds out
      company     the Rules table's Company row: the week's Kalpa company and the people the items
                  name, as the diagnostic's first page names them
      exhibits    per scenario set number, a mermaid fence, a small table or a code block printed
                  once under the set's situation, drawn only from the situation's own numbers
      notes       per bank item number: why the key holds, what each wrong option catches
                  ({letter: reason}), the interview answer in one breath, and the item's `label`,
                  the two or three words printed beside its level on the Word paper, such as
                  "Predict the output" or "Spot the double count"
      stretch     untimed, unmarked written items for fast finishers, each with its answer
  An exhibit is a mapping with a caption and one of mermaid, table ({head, rows}) or code
  ({lang, text}); exhibits are lettered by part in the order they print, as Exhibit 2A, 2B.
  Write the file in block style: a comma inside an inline {a: ..., b: ...} mapping splits a
  reason in two without any error.

--docx renders every exhibit through mermaid-cli in the diagnostic's palette and writes the paper
and the key as Word files through scripts/saturday_docx.js, in the layout of the requester's
baseline diagnostic: a first page with the purpose, the rules, step one (each part rated 1 to 4
before any item is read), the paper at a glance and a pacing ribbon; open question blocks that never
split across pages, with every exhibit bound to the first item that reads it; and an answer sheet on
one page at the end. The key ends on a marking grid, the answer sheet with the key's boxes marked.
The markdown stays the file the gates read, so --docx follows every change to it.
scripts/sync_programme.py re-renders every week whose paper already exists, so a changed item or a
new edit reaches a built Saturday with one sync; a new Saturday starts with this script.
"""
import argparse
import datetime as dt
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction
import json
import pathlib
import re
import sys

import openpyxl
import yaml

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
TRACKER = ROOT / "docs/curriculum/source.xlsx"
EDITS = ROOT / "data/programme/paper_edits.yaml"
FACTS = ROOT / "data/programme/facts.yaml"
DAYS_JSON = ROOT / "data/programme/days.json"
TAB = "Saturday papers"

# How a learner answers each type, in the words printed on the paper.
HOW = {
    "Fill in the blank": "Write the missing word or number on the line.",
    "True or false": "Write T or F on the line.",
    "One correct option": "Circle the one correct letter.",
    "More than one correct": "Circle every correct letter.",
    "Scenario set": ("Each set opens on one Kalpa situation. Answer each item the way it asks: "
                     "circle a letter, write T or F, or write the number or the word."),
    "Applied maths": "Show the working, then the answer.",
    "Order the steps": "Write the letters in the right order.",
}
OPTION = re.compile(r"^\(([a-f])\)\s*(.+)$")
SET_START = re.compile(r"^SET (\d+)\. SITUATION:\s*(.+)$")
SET_CONT = re.compile(r"^SET \d+, continued\.?$")
TAGS = ["[S]", "[F]", "[SV]", "[D]"]


def clean(v):
    if v is None:
        return ""
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v).strip()


def week_of(paper):
    return f"W{int(paper[1:]):02d}"


def read_bank(path=TRACKER):
    """{paper: {"items": [...], "slot": minutes}} straight from the workbook."""
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb[TAB]
    find = lambda second: next(r for r in range(1, ws.max_row + 1)
                               if clean(ws.cell(r, 1).value) == "Paper"
                               and (clean(ws.cell(r, 2).value) == "No.") == second)
    bank_row, blue_row = find(True), find(False)
    head = [clean(ws.cell(bank_row, c).value) for c in range(1, ws.max_column + 1)]
    col = {h: i + 1 for i, h in enumerate(head) if h}
    out = {}
    for r in range(blue_row + 1, bank_row):
        paper = clean(ws.cell(r, 1).value)
        if re.fullmatch(r"W\d+", paper):
            out.setdefault(paper, {"items": []})["slot"] = int(float(clean(ws.cell(r, 2).value)))
    for r in range(bank_row + 1, ws.max_row + 1):
        paper = clean(ws.cell(r, 1).value)
        if not paper:
            continue
        get = lambda name: clean(ws.cell(r, col[name]).value)
        anchor_col = next(h for h in col if h.startswith("Interview anchor"))
        out.setdefault(paper, {"items": [], "slot": None})["items"].append({
            "no": int(get("No.")), "type": get("Type"), "level": get("Level"), "tag": get("Tag"),
            "roles": get("Roles"), "day": get("Day"), "min": float(get("Min") or 0),
            "key": get("Key"), "text": get("Item"), "anchor": get(anchor_col), "edit": None,
        })
    return out


def apply_edits(bank, edits):
    """Lay the edits on the bank. Returns notes: (paper, no, state, why) with state applied, folded
    (the tracker already carries the wording) or broken (the item or option does not exist)."""
    notes = []
    for paper, by_no in (edits or {}).items():
        items = {i["no"]: i for i in bank.get(paper, {}).get("items", [])}
        for no, edit in (by_no or {}).items():
            item = items.get(int(no))
            if not item:
                notes.append((paper, no, "broken", "no such item in the bank"))
                continue
            lines = item["text"].split("\n")
            changed, missing = False, []
            for letter, new in (edit.get("options") or {}).items():
                idx = next((k for k, ln in enumerate(lines)
                            if (m := OPTION.match(ln.strip())) and m.group(1) == letter), None)
                if idx is None:
                    missing.append(letter)
                    continue
                want = f"({letter}) {str(new).strip()}"
                if lines[idx].strip() != want:
                    lines[idx] = want
                    changed = True
            if missing:
                notes.append((paper, no, "broken", f"option {', '.join(missing)} not found"))
                continue
            item["text"] = "\n".join(lines)
            if changed:
                item["edit"] = edit
                notes.append((paper, no, "applied", edit.get("why", "")))
            else:
                notes.append((paper, no, "folded", "the tracker already carries this wording"))
    return notes


def saturday_date(week):
    try:
        days = json.loads(DAYS_JSON.read_text(encoding="utf-8"))["days"]
        d = next(d for d in days if d["week"] == week and d["slot"] == "SAT")
        return dt.date.fromisoformat(d["date"])
    except (OSError, ValueError, StopIteration, KeyError):
        return None


def source_path(week):
    return ROOT / "content" / week / "SAT" / "internal" / f"C2_{week}_SAT_paper_source_INTERNAL.yaml"


def read_source(week):
    path = source_path(week)
    return (yaml.safe_load(path.read_text(encoding="utf-8")) or {}) if path.exists() else {}


def paper_minutes(week, slot):
    """The paper's length: the requester's override in facts.yaml, or the tracker's slot."""
    try:
        facts = yaml.safe_load(FACTS.read_text(encoding="utf-8"))
        return int((facts.get("saturday_papers") or {}).get("paper_minutes", {}).get(week) or slot)
    except (OSError, ValueError, TypeError, AttributeError):
        return slot


RECALL_TYPES = ("Fill in the blank", "True or false")
MAX_MOVED = 6
SET_ANY = re.compile(r"^SET (\d+)[.,]")
LEVELS = ("Easy", "Medium", "Hard")


def set_of(item):
    """The scenario set an item belongs to, as its number in text, or None."""
    m = SET_ANY.match(item["text"].split("\n")[0].strip())
    return m.group(1) if m else None


def _addition(a, n):
    return {"no": None, "type": a["type"], "level": a["level"], "tag": a["tag"],
            "roles": a.get("roles", ""), "day": a.get("day", ""),
            "min": float(a.get("min", 0)), "key": str(a["key"]),
            "text": str(a["text"]).strip(), "anchor": a.get("anchor", ""), "edit": None,
            "added": True, "id": str(a.get("id") or f"new{n}"), "exhibit": a.get("exhibit"),
            "label": a.get("label"),
            "note": {"why": a.get("why", ""), "wrong": a.get("wrong", {}),
                     "answer": a.get("answer", "")}}


def assemble(data, source):
    """The items in printed order, each carrying q, its printed number, and part, its part number.

    With `parts` in the source file the parts set the order, as the file lists them. Without, the
    sections follow the item types in the bank's order: within a section the bank's items come
    first, in the bank's order, and the source's additions follow in the order the file lists them.
    """
    bank = sorted((dict(i, added=False, exhibit=None) for i in data["items"]), key=lambda i: i["no"])
    notes = {str(k): v for k, v in (source.get("notes") or {}).items()}
    for item in bank:
        item["note"] = notes.get(str(item["no"]), {})
    added = [_addition(a, n) for n, a in enumerate(source.get("additions") or [], 1)]
    if source.get("parts"):
        printed = _by_parts(bank, added, source)
    else:
        order = []
        for item in bank + added:
            if item["type"] not in order:
                order.append(item["type"])
        printed = sorted(bank + added, key=lambda i: (order.index(i["type"]), i["added"]))
        for item in printed:
            item["part"] = None
    for q, item in enumerate(printed, 1):
        item["q"] = q
    return printed


def _by_parts(bank, added, source):
    by_no = {i["no"]: i for i in bank}
    by_id = {a["id"]: a for a in added}
    moved = {int(n) for n in source.get("stretch_bank") or []}
    printed, seen = [], set()
    for p, part in enumerate(source["parts"], 1):
        if not part.get("items"):
            raise SystemExit(f"FAIL  part {p} ({part.get('title', '')}) lists no items")
        for ref in part["items"]:
            ref = str(ref).strip()
            if ref.startswith("new:"):
                item = by_id.get(ref[4:])
            else:
                item = by_no.get(int(ref)) if ref.isdigit() else None
            if item is None:
                raise SystemExit(f"FAIL  part {p} names {ref}, which is neither a bank number nor "
                                 f"an addition's id")
            key = ref if ref.startswith("new:") else int(ref)
            if key in seen or (isinstance(key, int) and key in moved):
                raise SystemExit(f"FAIL  {ref} is placed twice: in part {p} and elsewhere")
            seen.add(key)
            item["part"] = p
            printed.append(item)
    missing = [i["no"] for i in bank if i["no"] not in seen and i["no"] not in moved]
    if missing:
        raise SystemExit(f"FAIL  bank items {missing} sit in no part and not in stretch_bank; every "
                         f"bank item is printed or moved, since the bank is the floor")
    unused = [a["id"] for a in added if f"new:{a['id']}" not in seen]
    if unused:
        raise SystemExit(f"FAIL  additions {unused} are named by no part")
    if len(moved) > MAX_MOVED:
        raise SystemExit(f"FAIL  {len(moved)} bank items moved to the stretch page, and at most "
                         f"{MAX_MOVED} may move")
    wrong_kind = [n for n in sorted(moved) if by_no[n]["type"] not in RECALL_TYPES]
    if wrong_kind:
        raise SystemExit(f"FAIL  bank items {wrong_kind} are not recall items, and only fill in the "
                         f"blank and true or false items may move to the stretch page")
    # A scenario set prints whole, in one part and in the bank's order, under one situation.
    sets = {}
    for pos, item in enumerate(printed):
        n = set_of(item)
        if n and item["type"] == "Scenario set":
            sets.setdefault(n, []).append((pos, item))
    for n, run in sets.items():
        positions = [pos for pos, _ in run]
        if positions != list(range(positions[0], positions[0] + len(run))):
            raise SystemExit(f"FAIL  scenario set {n} is split: its items must print together")
        if len({item["part"] for _, item in run}) > 1:
            raise SystemExit(f"FAIL  scenario set {n} spans two parts")
        first = run[0][1]["text"].split("\n")[0].strip()
        if not SET_START.match(first):
            raise SystemExit(f"FAIL  scenario set {n} does not open on its SITUATION item")
    return printed


def moved_items(data, source):
    """The bank items the source moved to the stretch page, in the bank's order, with their notes."""
    moved = {int(n) for n in source.get("stretch_bank") or []}
    notes = {str(k): v for k, v in (source.get("notes") or {}).items()}
    out = []
    for item in sorted(data["items"], key=lambda i: i["no"]):
        if item["no"] in moved:
            out.append(dict(item, added=False, exhibit=None, note=notes.get(str(item["no"]), {})))
    return out


def guess_chance(item):
    """The chance a blind guess gets the item right, as an exact fraction: 1/k on one of k options,
    1/2 on true or false, 1/(2**k - 1) on a more-than-one item read as any non-empty choice, 1/k! on
    an ordering of k steps, and 0 on a written answer, since a word or a number is not guessed from
    a list."""
    import math
    _, options, answer = parts(item)
    key = item["key"].strip().lower()
    if item["type"] == "Order the steps":
        return Fraction(1, math.factorial(len(options))) if options else Fraction(0)
    if item["type"] == "True or false" or key in ("t", "f", "true", "false"):
        return Fraction(1, 2)
    if options and answer is None:
        k = len(options)
        if item["type"] == "More than one correct" or MULTI.match(key):
            return Fraction(1, 2 ** k - 1)
        return Fraction(1, k)
    return Fraction(0)


MULTI = re.compile(r"^[a-f](\s*,\s*[a-f])+$")


def guessing_floor(printed):
    """(mean, cut): what blind guessing on every item averages, and the smallest score that fewer
    than one guesser in twenty reaches, from the exact distribution of the sum.

    The arithmetic runs in fractions, so the printed mean and the cut are the same on every machine:
    a mean that sits on a rounding boundary in floating point, such as 10.95, rounds one way on one
    runner and the other way on the next."""
    dist = [Fraction(1)]
    for item in printed:
        pr = guess_chance(item)
        nxt = [Fraction(0)] * (len(dist) + 1)
        for k, v in enumerate(dist):
            nxt[k] += v * (1 - pr)
            nxt[k + 1] += v * pr
        dist = nxt
    mean = sum((guess_chance(i) for i in printed), Fraction(0))
    tail, cut = Fraction(0), len(dist) - 1
    for k in range(len(dist) - 1, -1, -1):
        tail += dist[k]
        if tail > Fraction(1, 20):
            cut = k + 1
            break
    return mean, cut


def one_place(x):
    """A fraction to one decimal place, halves rounded up, the same on every machine."""
    d = Decimal(x.numerator) / Decimal(x.denominator)
    return str(d.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def part_rows(printed, source):
    """[(number, title, shows, items, minutes, easy, medium, hard)] in part order."""
    rows = []
    for p, part in enumerate(source.get("parts") or [], 1):
        run = [i for i in printed if i["part"] == p]
        lv = {v: sum(1 for i in run if i["level"] == v) for v in LEVELS}
        rows.append((p, part.get("title", f"Part {p}"), part.get("shows", ""), run,
                     sum(i["min"] for i in run), lv["Easy"], lv["Medium"], lv["Hard"]))
    return rows


def exhibit_plan(printed, source):
    """Where each exhibit prints and its label, in print order, lettered within its part.

    Returns {("part", p, index): label, ("set", n): label, ("item", q): label}."""
    labels, count = {}, {}
    exhibits = {str(k): v for k, v in (source.get("exhibits") or {}).items()}
    for p, part in enumerate(source.get("parts") or [], 1):
        count[p] = 0
        for idx, _ in enumerate(part.get("exhibits") or []):
            labels[("part", p, idx)] = f"Exhibit {p}{'ABCDEFGHIJKLMN'[count[p]]}"
            count[p] += 1
    for item, number, _ in sets_in(printed):
        p = item.get("part")
        if p is None:
            continue
        if number and exhibits.get(number):
            labels[("set", number)] = f"Exhibit {p}{'ABCDEFGHIJKLMN'[count[p]]}"
            count[p] += 1
        if item.get("exhibit"):
            labels[("item", item["q"])] = f"Exhibit {p}{'ABCDEFGHIJKLMN'[count[p]]}"
            count[p] += 1
    return labels


def groups(items):
    """Consecutive runs of one type, in printed order."""
    out = []
    for item in items:
        if out and out[-1][0] == item["type"]:
            out[-1][1].append(item)
        else:
            out.append((item["type"], [item]))
    return out


def count(n, noun="item"):
    """'1 item', '12 items'."""
    return f"{n} {noun}" if n == 1 else f"{n} {noun}s"


def span(items):
    a, b = items[0]["q"], items[-1]["q"]
    return f"Q{a}" if a == b else f"Q{a} to Q{b}"


def parts(item):
    """(stem lines, [(letter, text)], answer kind) for one item, without its set lines."""
    stem, options = [], []
    for ln in item["text"].split("\n"):
        s = ln.strip()
        if not s or SET_START.match(s) or SET_CONT.match(s):
            continue
        m = OPTION.match(s)
        if m:
            options.append((m.group(1), m.group(2)))
        else:
            stem.append(s)
    if item["type"] == "Applied maths":
        answer = "working"
    elif item["type"] == "Order the steps":
        answer = "order"
    elif options:
        answer = None
    else:
        answer = "line"
    return stem, options, answer


FORMAT = {"one": "circle one letter", "multi": "circle every correct letter", "tf": "write T or F",
          "line": "write the word or number", "working": "show the working, then the answer",
          "order": "write the letters in order"}


def answer_kind(item):
    """How the learner answers the item: one of the FORMAT keys."""
    _, options, answer = parts(item)
    key = item["key"].strip().lower()
    if answer in ("working", "order"):
        return answer
    if options:
        return "multi" if item["type"] == "More than one correct" or MULTI.match(key) else "one"
    if item["type"] == "True or false" or key in ("t", "f", "true", "false"):
        return "tf"
    return "line"


def render_item(item, in_parts=False):
    stem, options, answer = parts(item)
    head = f"#### Q{item['q']}"
    if in_parts:
        head += f" · {item['level']} · {FORMAT[answer_kind(item)]}"
    block = [head, ""] + stem
    if options:
        block.append("")
        block += [f"{letter}) {text}" for letter, text in options]
    if answer == "working":
        block += ["", "Working:", "", "Answer: ____________________"]
    elif answer == "order":
        block += ["", "Order: ____________________"]
    elif answer == "line":
        block += ["", "Answer: ____________________"]
    return block + [""]


def exhibit_md(ex, label=None):
    out = []
    if label:
        out += [f"**{label}.** {ex.get('caption', '')}".rstrip(), ""]
    if ex.get("mermaid"):
        out += ["```mermaid", str(ex["mermaid"]).rstrip(), "```", ""]
    if ex.get("table"):
        head, rows = ex["table"]["head"], ex["table"]["rows"]
        out += ["| " + " | ".join(map(str, head)) + " |", "|" + "---|" * len(head)]
        out += ["| " + " | ".join(map(str, r)) + " |" for r in rows] + [""]
    if ex.get("code"):
        code = ex["code"]
        out += [f"```{code.get('lang', '')}", str(code["text"]).rstrip(), "```", ""]
    if ex.get("caption") and not label:
        out += [f"*{ex['caption']}*", ""]
    return out


def sets_in(run):
    """Yield (item, set number or None, situation or None) with each set announced once."""
    current = None
    for item in run:
        m = SET_START.match(item["text"].split("\n")[0].strip())
        if m and m.group(1) != current:
            current = m.group(1)
            yield item, m.group(1), m.group(2)
        else:
            yield item, None, None


def set_display(printed):
    """{set number in the source: the number it prints as}. In parts the sets print in the order the
    parts place them, so the paper numbers them 1 upward as printed, never by the bank's numbering."""
    out = {}
    for _, number, _ in sets_in(printed):
        if number and number not in out:
            out[number] = str(len(out) + 1)
    return out


def when_of(date, sep):
    return date.strftime("%A %d %B %Y").replace(" 0", " ") + sep if date else ""


STRETCH_TITLE = "Stretch: untimed, and not marked"
STRETCH_INTRO = ("For anyone who finishes early. Nothing here is counted; each item is the kind an "
                 "interviewer asks after your first answer, so write the answer you would say.")


def stretch_intro(written, recalled):
    """The stretch page's opening line, naming which items are written answers and which are the
    recall lines moved from the timed paper."""
    if not recalled:
        return STRETCH_INTRO
    last = written + recalled
    lines = "Stretch {} to {}".format(written + 1, last) if recalled > 1 else f"Stretch {last}"
    text = "For anyone who finishes early. Nothing here is counted."
    if written:
        head = f"Stretch 1 to {written}" if written > 1 else "Stretch 1"
        text += (f" {head} {'are' if written > 1 else 'is'} the kind an interviewer asks after your "
                 f"first answer, so write the answer you would say.")
    return text + (f" {lines} {'are one-line recalls' if recalled > 1 else 'is a one-line recall'} of "
                   f"the week's rules, answered on the line.")


RULES_MD = [
    "{minutes} minutes in one sitting. Each part gives its minutes as a guide, not a limit.",
    "Every item names its format beside its number: circle one letter, circle every correct letter, "
    "write T or F, write the word or number, show the working, or write the letters in order.",
    "Every item also names its level, easy, medium or hard, so you can plan your time. A hard item is "
    "several steps on an exhibit, never an obscure fact.",
    "A wrong answer costs nothing, so answer every item on the line under it.",
    "Pen and this paper only: no laptop, no phone, no notes and no assistant.",
    "Afterwards the papers are swapped and marked against the key, and the discussion takes the items "
    "the room missed most. The paper is ungraded and ranks nobody; the room's scores by topic set "
    "Monday's revision.",
]


def render_paper_parts(paper, data, date, printed, source, minutes, moved):
    n, week = len(printed), int(paper[1:])
    exhibits = {str(k): v for k, v in (source.get("exhibits") or {}).items()}
    labels = exhibit_plan(printed, source)
    shown = set_display(printed)
    rows = part_rows(printed, source)
    out = [f"# Week {week} recap paper", "",
           f"{when_of(date, ' · ')}{minutes} minutes · {n} items in {len(rows)} parts · pen and paper, "
           f"no assistant, no notes", "",
           "Name: ____________________    Marked by: ____________________    "
           f"Items right: ____ of {n}", "",
           "## How this paper works", ""]
    out += [f"- {r.format(minutes=minutes)}" for r in RULES_MD] + [""]
    out += ["## The paper at a glance", "",
            "| Part | What it shows | Items | Minutes | Easy | Medium | Hard |",
            "|---|---|---|---|---|---|---|"]
    for p, title, shows, run, mins, e, m, h in rows:
        out.append(f"| {p}. {title} | {shows} | {span(run)} ({len(run)}) | {mins:g} | {e} | {m} | {h} |")
    tot = [sum(r[i] for r in rows) for i in (5, 6, 7)]
    out += [f"| Total | | {n} | {sum(r[4] for r in rows):g} | {tot[0]} | {tot[1]} | {tot[2]} |", ""]
    for p, title, shows, run, mins, e, m, h in rows:
        part = source["parts"][p - 1]
        out += ["---", "", f"## Part {p}. {title} ({span(run)})", "",
                f"*What it shows: {shows}. {count(len(run))}, about {mins:g} minutes.*", ""]
        if part.get("intro"):
            out += [str(part["intro"]).strip(), ""]
        for idx, ex in enumerate(part.get("exhibits") or []):
            out += exhibit_md(ex, labels[("part", p, idx)])
        for item, number, situation in sets_in(run):
            if number:
                out += [f"### Set {shown[number]}", "", f"**Situation.** {situation}", ""]
                if exhibits.get(number):
                    out += exhibit_md(exhibits[number], labels[("set", number)])
            if item.get("exhibit"):
                out += exhibit_md(item["exhibit"], labels[("item", item["q"])])
            out += render_item(item, in_parts=True)
    stretch = source.get("stretch") or []
    if stretch or moved:
        out += ["---", "", f"## {STRETCH_TITLE}", "", stretch_intro(len(stretch), len(moved)), ""]
        for i, s in enumerate(stretch, 1):
            out += [f"### Stretch {i}", "", str(s["text"]).strip(), ""]
        for i, item in enumerate(moved, len(stretch) + 1):
            stem, options, answer = parts(item)
            out += [f"### Stretch {i}", ""] + stem
            if options:
                out += [""] + [f"{letter}) {text}" for letter, text in options]
            out += ["", "Answer: ____________________", ""]
    return "\n".join(out).rstrip() + "\n"


def render_paper(paper, data, date, printed, source, minutes, moved=()):
    if source.get("parts"):
        return render_paper_parts(paper, data, date, printed, source, minutes, list(moved))
    n, week = len(printed), int(paper[1:])
    exhibits = {str(k): v for k, v in (source.get("exhibits") or {}).items()}
    out = [f"# Week {week} recap paper", "",
           f"{when_of(date, ' · ')}{minutes} minutes · {n} items · pen and paper, no assistant, "
           f"no notes", "",
           "Name: ____________________    Marked by: ____________________    "
           f"Items right: ____ of {n}", "",
           "Answer every item in the space it gives you. Each section says how. After the break the "
           "papers are swapped and marked against the key, and the discussion starts with the items "
           "the room missed most.", ""]
    letters = "ABCDEFGHIJ"
    for k, (kind, run) in enumerate(groups(printed)):
        out += ["---", "", f"## {letters[k]}. {kind} ({span(run)})", "", HOW.get(kind, ""), ""]
        for item, number, situation in sets_in(run):
            if number:
                out += [f"### Set {number}", "", f"**Situation.** {situation}", ""]
                out += exhibit_md(exhibits.get(number, {}))
            out += render_item(item)
    stretch = source.get("stretch") or []
    if stretch:
        out += ["---", "", f"## {STRETCH_TITLE}", "", STRETCH_INTRO, ""]
        for i, s in enumerate(stretch, 1):
            out += [f"### Stretch {i}", "", str(s["text"]).strip(), ""]
    return "\n".join(out).rstrip() + "\n"


def cell(v):
    return str(v).replace("|", "\\|").replace("\n", "<br>")


def floor_sentence(printed):
    mean, cut = guessing_floor(printed)
    n = len(printed)
    return (f"A learner who guessed every item blind would average {one_place(mean)} of {n}, since a written "
            f"answer cannot be guessed from a list, and fewer than one guesser in twenty would reach "
            f"{cut}. A score of {cut - 1} or below is therefore within reach of guessing alone, and the "
            f"tally reads such a paper as a conversation to have on Monday, never as a result.")


def render_key(paper, data, date, notes, printed, source, minutes, moved=()):
    n, week = len(printed), int(paper[1:])
    moved = list(moved)
    pace = sum(i["min"] for i in printed)
    levels = {lv: sum(1 for i in printed if i["level"] == lv) for lv in ("Easy", "Medium", "Hard")}
    added = [i for i in printed if i["added"]]
    out = [f"# Week {week} recap paper: key", "",
           "TRAINER. Rendered from the tracker's item bank and the week's source file by "
           "`scripts/build_saturday_paper.py`. Change an item in the tracker, an option in "
           "`data/programme/paper_edits.yaml` or anything in "
           f"`content/{week_of(paper)}/SAT/internal/C2_{week_of(paper)}_SAT_paper_source_INTERNAL.yaml`, "
           "and rebuild; never edit this file by hand.", "",
           f"{when_of(date, '. ')}A {minutes}-minute paper holding {n} items at {pace:g} minutes by "
           f"the blueprint's pace: {levels['Easy']} easy, {levels['Medium']} medium and "
           f"{levels['Hard']} hard."
           + (f" {len(added)} of them are new and not yet in the tracker." if added else ""), "",
           "## Marking", "",
           "1. Papers are swapped, so nobody checks their own.",
           f"2. The Academic TA reads the key out {'part by part' if source.get('parts') else 'section by section'}, "
           "and the marker writes a tick or a cross beside each item.",
           "3. An item is right when its answer matches the key: every correct letter and no other "
           "on a more-than-one item, the number on an applied maths item (the working belongs to the "
           "discussion), and the whole sequence on an ordering item. The programme has set no "
           "partial-credit rule, so this key uses none.",
           f"4. The marker writes the count of ticks as Items right on the front, out of {n}, and "
           "hands the paper back.",
           "5. The TA collects the papers and tallies the misses by tag, using the table below; that "
           "tally is Monday's remediation read. It is never a ranking and never read out by name."]
    in_parts = bool(source.get("parts"))
    if in_parts:
        wb = f"C2_{week_of(paper)}_SAT_item_analysis_TRAINER.xlsx"
        out += [f"6. The TA enters every paper in `{wb}` beside this key, by seat and never by name: 1 "
                "for a tick, 0 for a cross and a blank for an item left empty. The workbook orders the "
                "discussion from the most-missed item, flags any item to check, and gives each tag's "
                "rate for the room and for each seat.", "",
                "## The blueprint", "",
                "| Part | What it shows | Items | Minutes | Easy | Medium | Hard |",
                "|---|---|---|---|---|---|---|"]
        rows = part_rows(printed, source)
        for p, title, shows, run, mins, e, m, h in rows:
            out.append(f"| {p}. {title} | {shows} | {span(run)} ({len(run)}) | {mins:g} | {e} | {m} | {h} |")
        tot = [sum(r[i] for r in rows) for i in (5, 6, 7)]
        out.append(f"| Total | | {n} | {sum(r[4] for r in rows):g} | {tot[0]} | {tot[1]} | {tot[2]} |")
        out += ["", "## What guessing alone would score", "", floor_sentence(printed), "",
                "## Reading the items after marking", "",
                "The workbook flags an item to check when fewer than one learner in five got it right, or "
                "when the bottom third of the room got it right more often than the top third. Both are "
                f"this programme's own working rule for a room of {seats()}. A flagged item is "
                "discussed as usual; the TA also sends it, with the room's rate, to the tracker's owner, "
                "because the fault may sit in the item rather than in the learners."]
    out += ["", "## The key", "",
            "| Q | Key | Type | Part | Level | Tag | Roles | Day | Min | Source | Interview anchor |",
            "|---|---|---|---|---|---|---|---|---|---|---|"]
    for i in printed:
        src = "new" if i["added"] else f"bank {i['no']}"
        part = i.get("part") or ""
        out.append(f"| {i['q']} | {cell(i['key'])} | {i['type']} | {part} | {i['level']} | {i['tag']} | "
                   f"{cell(i['roles'])} | {i['day']} | {i['min']:g} | {src} | {cell(i['anchor'])} |")
    reasoned = [i for i in printed if i["note"].get("why") or i["note"].get("wrong")]
    if reasoned:
        out += ["", "## Why each answer holds", ""]
        for i in reasoned:
            note = i["note"]
            out += [f"### Q{i['q']}, key {i['key']}", ""]
            if note.get("why"):
                out += [f"**Why it holds.** {note['why']}", ""]
            for letter, why in sorted((note.get("wrong") or {}).items()):
                out.append(f"- ({letter}) {why}")
            if note.get("wrong"):
                out.append("")
            if note.get("answer"):
                out += [f"**In the interview.** {note['answer']}", ""]
    out += ["", "## Items by tag, level, day and part, for the tally" if in_parts
            else "## Items by tag, level and day, for the tally", ""]
    for tag in TAGS:
        hit = [f"Q{i['q']}" for i in printed if i["tag"] == tag]
        out.append(f"- {tag} ({len(hit)}): {', '.join(hit) if hit else 'none'}")
    for lv in ("Easy", "Medium", "Hard"):
        hit = [f"Q{i['q']}" for i in printed if i["level"] == lv]
        out.append(f"- {lv} ({len(hit)}): {', '.join(hit)}")
    for day in ("Mon", "Tue", "Wed", "Thu", "Fri"):
        hit = [f"Q{i['q']}" for i in printed if i["day"] == day]
        if hit:
            out.append(f"- {day} ({len(hit)}): {', '.join(hit)}")
    for p, title, *_ in part_rows(printed, source):
        hit = [f"Q{i['q']}" for i in printed if i["part"] == p]
        out.append(f"- Part {p}, {title} ({len(hit)}): {', '.join(hit)}")
    if added:
        out += ["", "## New items waiting for the tracker", "",
                "These items come from the week's source file, not the tracker. Accept one by adding "
                "it to the tracker's Saturday papers tab and deleting it from the source file.", ""]
        for i in added:
            first = next((s for s in parts(i)[0]), "")
            out.append(f"- Q{i['q']} ({i['type']}, {i['level']}, {i['tag']}): {first}")
    mine = [x for x in notes if x[0] == paper and x[2] == "applied"]
    if mine:
        out += ["", "## Option edits laid on the bank, waiting for the tracker", "",
                "These options differ from the tracker's wording, each for the reason given beside "
                "it. The stem and the key are the tracker's. Accept an edit by copying it into the "
                "tracker; reject it by deleting it from `data/programme/paper_edits.yaml`.",
                ""]
        for _, no, _, why in mine:
            item = next(i for i in printed if i["no"] == int(no))
            opts = ", ".join(sorted(item["edit"].get("options", {})))
            out.append(f"- Q{item['q']} (bank {no}), option {opts} "
                       f"({item['edit'].get('status', 'proposed')}): {why}")
    stretch = source.get("stretch") or []
    if stretch or moved:
        out += ["", "## The stretch page", ""]
        for k, s in enumerate(stretch, 1):
            out.append(f"- Stretch {k}: {s.get('answer', '')}")
        for k, item in enumerate(moved, len(stretch) + 1):
            why = (item.get("note") or {}).get("why", "")
            out.append(f"- Stretch {k} (bank {item['no']}, {item['type'].lower()}, moved from the timed "
                       f"paper): {item['key']}" + (f". {why}" if why else ""))
    return "\n".join(out).rstrip() + "\n"


def targets(week):
    base = ROOT / "content" / week / "SAT"
    return (base / "paper" / f"C2_{week}_SAT_recap_paper_STUDENT.md",
            base / "answer-key" / f"C2_{week}_SAT_answer_key_TRAINER.md")


def render_all(tracker=TRACKER, only=None, date_of=saturday_date, existing_only=False):
    """{path: text} for every paper whose week has a SAT folder, plus the edit notes.

    With existing_only, a week is rendered only when its paper file is already there, which is
    how the sync keeps built Saturdays current without starting a Saturday nobody has begun.
    """
    bank = read_bank(tracker)
    edits = yaml.safe_load(EDITS.read_text(encoding="utf-8")) if EDITS.exists() else {}
    notes = apply_edits(bank, edits)
    out = {}
    for paper, data in bank.items():
        week = week_of(paper)
        if only and week not in only:
            continue
        if not (ROOT / "content" / week / "SAT").is_dir():
            continue
        p_path, k_path = targets(week)
        if existing_only and not p_path.exists():
            continue
        date = date_of(week)
        source = read_source(week)
        printed = assemble(data, source)
        moved = moved_items(data, source)
        minutes = paper_minutes(week, data["slot"])
        timed = sum(i["min"] for i in printed)
        if timed > minutes:
            raise SystemExit(f"FAIL  {week}'s timed items take {timed:g} minutes at the blueprint's "
                             f"pace, over the paper's {minutes}")
        out[p_path] = render_paper(paper, data, date, printed, source, minutes, moved)
        out[k_path] = render_key(paper, data, date, notes, printed, source, minutes, moved)
    return out, notes


# --------------------------------------------------------------------------- the Word files
# The room sits the Word paper, so it follows the requester's baseline diagnostic: its palette, its
# fonts, its open question blocks and its answer sheet. scripts/saturday_docx.js draws it; this
# builds the spec it draws from. The markdown paper stays the file the gates read.

# The diagnostic's own palette for the exhibits drawn by mermaid-cli, so a picture on the paper sits
# in the same ink, bronze and warm grey as the page around it.
PAPER_MERMAID = """{
  "theme": "base",
  "htmlLabels": false,
  "themeVariables": {
    "background": "#FFFFFF",
    "primaryColor": "#F3F1EA", "primaryTextColor": "#1C1B16", "primaryBorderColor": "#B37A33",
    "secondaryColor": "#F9F8F3", "secondaryTextColor": "#1C1B16", "secondaryBorderColor": "#D5D0C4",
    "tertiaryColor": "#FFFFFF", "tertiaryTextColor": "#1C1B16", "tertiaryBorderColor": "#D5D0C4",
    "lineColor": "#6B675E", "textColor": "#1C1B16", "mainBkg": "#F3F1EA", "nodeBorder": "#B37A33",
    "clusterBkg": "#F9F8F3", "clusterBorder": "#D5D0C4", "edgeLabelBackground": "#FFFFFF",
    "fontFamily": "Liberation Sans, Arial, DejaVu Sans, sans-serif", "fontSize": "16px"
  },
  "flowchart": {"htmlLabels": false, "curve": "linear", "padding": 6,
                "nodeSpacing": 24, "rankSpacing": 28, "useMaxWidth": true}
}"""

# How each answer kind is labelled beside an item's level when the source file gives no label of
# its own, and how the answer sheet names it.
KIND_LABEL = {"one": "Choose one", "multi": "Choose every correct option", "tf": "True or false",
              "line": "Complete it", "working": "Work it out", "order": "Put the steps in order"}
KIND_SHEET = {"line": "Word or number", "working": "Final answer", "order": "Letters in order"}
SCALE = ("1 = I have not used this; 2 = I can follow it when someone shows me; 3 = I can do it alone "
         "on a small problem; 4 = I can find and fix mistakes in someone else's version")
PURPOSE = ("This paper finds which of the week's decisions you can make cold, with no notes and no "
           "assistant, so Monday's practice starts where each of us needs it. Every item is a Kalpa "
           "business question first and a technique question second, which is the order "
           "interviewers use.")


def paper_header():
    """The running header of every page, as the requester's diagnostic prints it."""
    try:
        facts = yaml.safe_load(FACTS.read_text(encoding="utf-8")) or {}
        return str((facts.get("saturday_papers") or {}).get("header") or "Cohort 2")
    except (OSError, ValueError, TypeError, AttributeError):
        return "Cohort 2"


def upper_key(key):
    """A letter key as the Word files print it: 'a, b, d' becomes 'A, B, D'. Words, numbers and
    true or false stay as the bank writes them."""
    k = str(key).strip()
    return k.upper() if re.fullmatch(r"[a-fA-F](\s*,\s*[a-fA-F])*", k) else k


def tf_key(key):
    return "T" if str(key).strip().lower() in ("t", "true") else "F"


def exhibit_png(ex):
    """The exhibit's mermaid fence as a PNG path with its print size, or None when it has none.

    The room sits the Word paper, so an exhibit that cannot render stops the build: mermaid-cli
    missing raises SystemExit, and one that writes nothing raises MermaidError.
    """
    if not ex.get("mermaid"):
        return None
    from PIL import Image
    sys.path.insert(0, str(HERE))
    from build_cheatsheet import PNG_SCALE, render_mermaid
    png = render_mermaid(str(ex["mermaid"]), "png", config=PAPER_MERMAID)
    if not png:
        raise SystemExit("mermaid-cli is not installed, so the Word paper would lose its exhibits. "
                         "Install it with npm install -g @mermaid-js/mermaid-cli and build again.")
    with Image.open(png) as img:
        w, h = (d / PNG_SCALE for d in img.size)
    # The PNG holds PNG_SCALE pixels per CSS pixel for sharpness; the page prints it at its
    # natural size, capped at the column's width.
    scale = min(1.0, 620 / w)
    return {"path": str(png), "w": round(w * scale), "h": round(h * scale)}


def exhibit_block(ex, label=None, kind="exhibit", **extra):
    code = ex.get("code") or {}
    return dict({"kind": kind, "label": label or "", "image": exhibit_png(ex), "table": ex.get("table"),
                 "code": str(code.get("text", "")).rstrip("\n").split("\n") if code else [],
                 "caption": " ".join(str(ex.get("caption", "")).split())}, **extra)


def item_label(item):
    """The short label beside an item's number: the source file's own, or its answer kind."""
    own = (item.get("note") or {}).get("label") or item.get("label")
    return " ".join(str(own).split()) if own else KIND_LABEL[answer_kind(item)]


def item_block(item):
    stem, options, _ = parts(item)
    kind = answer_kind(item)
    return {"kind": "item", "q": item["q"], "level": item["level"], "label": item_label(item),
            "lines": stem, "options": [[a.upper(), b] for a, b in options], "answer": kind,
            "room": 1500 if kind == "working" else 0}


def sheet_rows(printed, with_key=False):
    """The answer sheet's three kinds of row: lettered items, true or false, and written answers."""
    letters, tf, written = [], [], []
    for i in printed:
        _, options, _ = parts(i)
        kind = answer_kind(i)
        if kind in ("one", "multi"):
            row = {"q": i["q"], "count": len(options), "multi": kind == "multi"}
            if with_key:
                row["key"] = [x.strip().upper() for x in str(i["key"]).split(",")]
            letters.append(row)
        elif kind == "tf":
            row = {"q": i["q"]}
            if with_key:
                row["key"] = tf_key(i["key"])
            tf.append(row)
        else:
            row = {"q": i["q"], "kind": kind, "kindLabel": KIND_SHEET[kind], "steps": len(options)}
            if with_key:
                row["key"] = upper_key(i["key"]) if kind == "order" else str(i["key"])
            written.append(row)
    width = max([r["count"] for r in letters] + [4])
    return {"letters": letters, "tf": tf, "written": written, "letterColumns": list("ABCDEF"[:width])}


def pacing(rows):
    out, start = [], 0.0
    for p, title, shows, run, mins, e, m, h in rows:
        out.append({"part": p, "title": title, "minutes": f"{mins:g}", "start": f"{start:g}"})
        start += mins
    for o in out:
        o["minutes"] = float(o["minutes"])
    return out


def docx_sections(printed, source):
    """The paper's parts as blocks: each part's exhibits, each set's case, each item."""
    exhibits = {str(k): v for k, v in (source.get("exhibits") or {}).items()}
    labels = exhibit_plan(printed, source)
    shown = set_display(printed)
    sections, glance = [], []
    rows = part_rows(printed, source)
    for p, title, shows, run, mins, e, m, h in rows:
        part = source["parts"][p - 1]
        blocks = [exhibit_block(ex, labels[("part", p, idx)])
                  for idx, ex in enumerate(part.get("exhibits") or [])]
        for item, number, situation in sets_in(run):
            if number:
                blocks.append(exhibit_block(exhibits.get(number, {}), labels.get(("set", number)),
                                            kind="set", n=shown[number], situation=situation))
            if item.get("exhibit"):
                blocks.append(exhibit_block(item["exhibit"], labels[("item", item["q"])]))
            blocks.append(item_block(item))
        sections.append({"heading": f"Part {p}. {title}",
                         "intro": f"{count(len(run))}, {span(run)}, about {mins:g} minutes. "
                                  f"What it shows: {shows}.",
                         "situation": " ".join(str(part.get("intro") or "").split()), "blocks": blocks})
        glance.append([str(p), title, f"{span(run)} ({len(run)})", shows, f"{mins:g}", str(e), str(m), str(h)])
    tot = [sum(r[i] for r in rows) for i in (5, 6, 7)]
    glance.append(["", "Total", str(len(printed)), "", f"{sum(r[4] for r in rows):g}", *map(str, tot)])
    return sections, glance, rows


def docx_sections_by_type(printed, source):
    """The older layout, for a week with no parts: one section per item type, in the bank's order."""
    exhibits = {str(k): v for k, v in (source.get("exhibits") or {}).items()}
    sections, glance, letters = [], [], "ABCDEFGHIJ"
    for k, (kind, run) in enumerate(groups(printed)):
        blocks = []
        for item, number, situation in sets_in(run):
            if number:
                blocks.append(exhibit_block(exhibits.get(number, {}), f"Exhibit {letters[k]}",
                                            kind="set", n=number, situation=situation))
            blocks.append(item_block(item))
        mins = sum(i["min"] for i in run)
        lv = {v: sum(1 for i in run if i["level"] == v) for v in LEVELS}
        sections.append({"heading": f"Section {letters[k]}. {kind}",
                         "intro": f"{count(len(run))}, {span(run)}, about {mins:g} minutes. {HOW.get(kind, '')}",
                         "situation": "", "blocks": blocks})
        glance.append([letters[k], kind, f"{span(run)} ({len(run)})", HOW.get(kind, ""), f"{mins:g}",
                       str(lv["Easy"]), str(lv["Medium"]), str(lv["Hard"])])
    return sections, glance


def docx_spec(paper, data, date, printed, source, minutes, notes, moved=()):
    week, n, wk = week_of(paper), len(printed), int(paper[1:])
    in_parts = bool(source.get("parts"))
    if in_parts:
        sections, glance, rows = docx_sections(printed, source)
        pace = pacing(rows)
        areas = "; ".join(f"Part {p}, {t}" for p, t, *_ in rows)
        part_titles = [f"Part {p}. {t}" for p, t, *_ in rows]
    else:
        sections, glance = docx_sections_by_type(printed, source)
        pace, areas = [], "The sections below"
        part_titles = [s["heading"] for s in sections]
    name = f"Week {wk} Recap Paper"
    header = f"{paper_header()}  |  {name}"
    when = when_of(date, "").strip()
    subtitle = (f"Cohort 2 | Week {wk}" + (f" | {when}" if when else "") +
                f" | {minutes} minutes | {count(n)}" + (f" in {len(sections)} parts" if in_parts else "") +
                " | pen and paper | ungraded")
    timed = sum(i["min"] for i in printed)
    company = " ".join(str(source.get("company") or "").split())
    rules = [
        ["Time", f"{minutes} minutes in one sitting for {count(n)}, which the blueprint paces at "
                 f"{timed:g} minutes. Each part gives its minutes as a guide; move on when an item is "
                 f"eating your time, and come back to it at the end."],
        ["Tools", "Pen and this paper only: no laptop, no phone, no notes and no assistant. Rough "
                  "working goes in the margins and in the working boxes."],
        ["Answers", "Every answer goes on the answer sheet at the back, which is the page that is "
                    "marked: one box for a lettered item, every correct box for a starred one, T or F "
                    "for a statement, and the word, the number or the letters in order in the space. "
                    "A wrong answer costs nothing, so answer every item."],
        ["Levels", "Every item shows its level beside its number, easy, medium or hard. A hard item is "
                   "several steps on an exhibit, never an obscure fact."],
        ["Exhibits", "An exhibit is printed once, labelled by its part as Exhibit 2A, 2B, and every item "
                     "that reads it follows it. Read code and queries as written: Python 3 and "
                     "PostgreSQL unless the item says otherwise."],
        ["Afterwards", "Papers are swapped and marked against the key, then the discussion takes the "
                       "items the room missed most. The paper is ungraded and ranks nobody; the room's "
                       "rates by part and by tag set Monday's revision."],
    ]
    if company:
        rules.insert(5, ["Company", company])
    stretch = source.get("stretch") or []
    stretch_items = [{"n": k, "lines": [ln.strip() for ln in str(s["text"]).strip().split("\n") if ln.strip()],
                      "options": [], "short": False} for k, s in enumerate(stretch, 1)]
    for k, item in enumerate(moved, len(stretch) + 1):
        stem, options, _ = parts(item)
        stretch_items.append({"n": k, "lines": stem, "options": [[a.upper(), b] for a, b in options], "short": True})
    sheet = dict(sheet_rows(printed), title="Answer sheet", n=n, parts=part_titles, scale=SCALE,
                 note=(f"{name} | Cohort 2 | Week {wk}. Fill in pen. Mark one box per row, or every "
                       "correct box for a starred item; if you change your mind, cross the old box fully "
                       "and mark the new one. Write words and numbers clearly, one per space."))
    paper_spec = {
        "title": name, "subtitle": subtitle, "header": header,
        "purpose": " ".join(str(source.get("purpose") or PURPOSE).split()),
        "rules": rules,
        "stepOne": {"intro": ("On the answer sheet, rate yourself from 1 to 4 on each part before you read "
                              "any item. Rate yourself as you are today: the comparison between your rating "
                              "and your score in each part is the most useful thing this paper produces "
                              "for Monday."),
                    "areas": areas, "scale": SCALE},
        "glance": {"head": ["Part" if in_parts else "Section", "Title", "Items", "What it shows",
                            "Minutes", "Easy", "Medium", "Hard"], "rows": glance},
        "pacingNote": (f"Each band is as wide as its part's minutes; the timed items fill {timed:g} of "
                       f"the {minutes} minutes, and the minute each part starts is under it."),
        "pacing": pace, "minutes": minutes, "sections": sections,
        "stretch": {"title": STRETCH_TITLE, "intro": stretch_intro(len(stretch), len(moved)),
                    "items": stretch_items},
        "sheet": sheet,
    }
    reasons = []
    for i in printed:
        note = i["note"]
        if note.get("why") or note.get("wrong") or note.get("answer"):
            reasons.append({"q": i["q"], "key": upper_key(i["key"]),
                            "meta": f"{i['type']}, {i['level']}, {i['tag']}, {i['day']}",
                            "why": note.get("why", ""),
                            "wrong": sorted([str(k).upper(), v] for k, v in (note.get("wrong") or {}).items()),
                            "answer": note.get("answer", ""), "anchor": i["anchor"]})
    tally = []
    for tag in TAGS:
        hit = [f"Q{i['q']}" for i in printed if i["tag"] == tag]
        tally.append(f"{tag} ({len(hit)}): {', '.join(hit) if hit else 'none'}")
    for lv in LEVELS:
        hit = [f"Q{i['q']}" for i in printed if i["level"] == lv]
        tally.append(f"{lv} ({len(hit)}): {', '.join(hit)}")
    if in_parts:
        for p, title, *_ in rows:
            hit = [f"Q{i['q']}" for i in printed if i["part"] == p]
            tally.append(f"Part {p}, {title} ({len(hit)}): {', '.join(hit)}")
    added = [i for i in printed if i["added"]]
    marking = [
        "Papers are swapped, so nobody checks their own.",
        f"The Academic TA reads the key out {'part by part' if in_parts else 'section by section'}, and the "
        "marker ticks or crosses each row of the answer sheet against the marking grid at the back of this key.",
        "An item is right when its answer matches the key: every correct box and no other on a starred "
        "item, the number on a work-it-out item (the working belongs to the discussion), and the whole "
        "sequence on an order item. The programme has set no partial-credit rule, so this key uses none.",
        f"The marker writes the count of ticks as Items right, out of {n}, and hands the paper back.",
        "The TA collects the answer sheets and tallies the misses by part and by tag, never a ranking and "
        "never read out by name.",
    ]
    if in_parts:
        marking.append(f"The TA enters every sheet in C2_{week}_SAT_item_analysis_TRAINER.xlsx by seat, never "
                       "by name: 1 for a tick, 0 for a cross, a blank for an item left empty, and each part's "
                       "rating from step one. It orders the discussion from the most-missed item, flags any "
                       "item to check, and sets each part's ratings beside its right rate.")
    key_spec = {
        "title": f"{name}: key", "header": f"{header}  |  Key  |  TRAINER",
        "meta": f"TRAINER | Cohort 2 | Week {wk}" + (f" | {when}" if when else "") + f" | {minutes} minutes | {count(n)}",
        "marking": marking,
        "blueprint": {"head": paper_spec["glance"]["head"], "rows": glance} if in_parts else None,
        "guessing": floor_sentence(printed) if in_parts else "",
        "itemReading": ("The workbook flags an item to check when fewer than one learner in five got it right, "
                        "or when the bottom third of the room got it right more often than the top third. "
                        f"Both are this programme's own working rule for a room of {seats()}. A flagged item "
                        "is discussed as usual; the TA also sends it, with the room's rate, to the tracker's "
                        "owner, because the fault may sit in the item rather than in the learners.") if in_parts else "",
        "rows": [[str(i["q"]), upper_key(i["key"]), i["type"], str(i.get("part") or ""), i["level"], i["tag"],
                  i["day"], "new" if i["added"] else f"bank {i['no']}"] for i in printed],
        "reasons": reasons, "tally": tally,
        "additions": [f"Q{i['q']} ({i['type']}, {i['level']}, {i['tag']}): {next(iter(parts(i)[0]), '')}"
                      for i in added],
        "additionsNote": "These items come from the week's source file, not the tracker. Accept one by "
                         "adding it to the tracker's Saturday papers tab.",
        "stretch": [str(s.get("answer", "")) for s in stretch]
                   + [f"{upper_key(i['key'])} (bank {i['no']}, moved from the timed paper)" for i in moved],
        "grid": dict(sheet_rows(printed, with_key=True), n=n,
                     note=("The answer sheet with every box of the key marked, for the marker to lay "
                           "beside each sheet. A starred item is right only when every marked box, and "
                           "no other, is ticked.")),
    }
    return {"paper": paper_spec, "key": key_spec}


# --------------------------------------------------------------------------- the item analysis
# Six seats marked on the first five items: seat 1 is the top of the room and seat 6 the bottom, Q2
# is right once in six, and on Q3 the bottom third beats the top third. The manifest flips these in
# and asserts both flags, the bands and the discussion order, which starts at Q2.
# The same six seats rate Part 1 before the paper: seat 4 (3, and 2 of 5 right) and seat 6 (4, and
# none right) rated it 3 or 4 and got under half of it right.
DEMO_RATINGS = [3, 4, 2, 3, 1, 4]
DEMO_MARKS = [[1, 1, 0, 1, 1], [1, 0, 0, 1, 1], [1, 0, 0, 1, 0],
              [1, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]


def seats():
    try:
        facts = yaml.safe_load(FACTS.read_text(encoding="utf-8"))
        return int(facts["cohort"]["students"]["value"])
    except (OSError, KeyError, TypeError, ValueError):
        return 35


def write_item_analysis(week, printed, source):
    """The TRAINER workbook the Academic TA fills after marking, and its recalc manifest.

    Marks takes 1, 0 or a blank per seat and item, by seat and never by name. Items computes each
    item's right rate and the top and bottom thirds' rates, and flags an item to check; Discussion
    orders the items from the most missed; Tags gives the room's rate by tag and by part; Seats gives
    each seat's rate by tag, which is Monday's remediation read. Only formulas LibreOffice computes.
    """
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter as col
    n, S = len(printed), seats()
    first, last_row = 5, 4 + S
    last = col(1 + n)
    TOT, ANS, BAND = col(2 + n), col(3 + n), col(4 + n)
    bold, head_fill = Font(bold=True), PatternFill("solid", fgColor="1A0F5C")
    white, input_fill = Font(bold=True, color="FFFFFF"), PatternFill("solid", fgColor="FFF4C2")
    wrap = Alignment(wrap_text=True, vertical="top")
    wb = openpyxl.Workbook()
    readme = wb.active
    readme.title = "Read me"
    lines = [
        f"Week {int(week[1:])} recap paper: item analysis",
        "TRAINER. Fill this after the swap-marking, one row per seat and never a name.",
        "Marks: type 1 for a tick, 0 for a cross and leave a blank for an item left empty. Yellow cells "
        "are the only inputs; everything else is computed.",
        "Items: each item's right rate, the top and bottom thirds' rates (thirds by total, once three "
        "or more seats are in), and a flag when fewer than one in five got it right or the bottom third "
        f"beat the top third. Both are this programme's own working rule for a room of {seats()}.",
        "Discussion: the items from the most missed, which is the order the solution discussion takes.",
        "Tags: the room's rate by tag and by part. Seats: each seat's rate by tag, for Monday's "
        "remediation read. Neither is a ranking, and neither is read out by name.",
    ]
    for r, text in enumerate(lines, 1):
        readme.cell(r, 1, text).font = bold if r == 1 else Font()
        readme.cell(r, 1).alignment = wrap
    readme.column_dimensions["A"].width = 110

    marks = wb.create_sheet("Marks")
    marks["A1"] = "Marks: 1 right, 0 wrong, blank left empty"
    marks["A1"].font = bold
    marks["A2"], marks["A3"], marks["A4"] = "Part", "Tag", "Seat"
    for j, item in enumerate(printed):
        c = col(2 + j)
        marks[f"{c}2"], marks[f"{c}3"], marks[f"{c}4"] = item.get("part") or "", item["tag"], f"Q{item['q']}"
    for c, label in ((TOT, "Total"), (ANS, "Answered"), (BAND, "Band")):
        marks[f"{c}4"] = label
    for c in range(1, 5 + n):
        cell = marks.cell(4, c)
        cell.font, cell.fill = white, head_fill
    tot_rng = f"${TOT}${first}:${TOT}${last_row}"
    for k in range(S):
        r = first + k
        marks[f"A{r}"] = k + 1
        for j in range(n):
            marks[f"{col(2 + j)}{r}"].fill = input_fill
        marks[f"{TOT}{r}"] = f'=IF(COUNT(B{r}:{last}{r})=0,"",SUM(B{r}:{last}{r}))'
        marks[f"{ANS}{r}"] = f"=COUNT(B{r}:{last}{r})"
        third = f"ROUND(COUNT({tot_rng})/3,0)"
        marks[f"{BAND}{r}"] = (f'=IF(OR({TOT}{r}="",COUNT({tot_rng})<3),"",IF(RANK({TOT}{r},{tot_rng},0)<={third},'
                               f'"top",IF(RANK({TOT}{r},{tot_rng},1)<={third},"bottom","middle")))')
    marks.freeze_panes = "B5"

    items = wb.create_sheet("Items")
    items["A1"] = "Items: the room's rate, the thirds, and what to check"
    items["A1"].font = bold
    heads = ["Q", "Part", "Type", "Level", "Tag", "Key", "Right", "Answered", "Right rate",
             "Top third rate", "Bottom third rate", "Top minus bottom", "Flag", "Order key"]
    for c, h in enumerate(heads, 1):
        cell = items.cell(4, c, h)
        cell.font, cell.fill = white, head_fill
    band = f"Marks!${BAND}${first}:${BAND}${last_row}"
    end = 4 + n
    for j, item in enumerate(printed):
        r, c = 5 + j, col(2 + j)
        rng = f"Marks!{c}${first}:{c}${last_row}"
        items[f"A{r}"], items[f"B{r}"] = item["q"], item.get("part") or ""
        items[f"C{r}"], items[f"D{r}"], items[f"E{r}"], items[f"F{r}"] = (item["type"], item["level"],
                                                                         item["tag"], item["key"])
        items[f"G{r}"] = f"=COUNTIF({rng},1)"
        items[f"H{r}"] = f"=COUNT({rng})"
        items[f"I{r}"] = f'=IF(H{r}=0,"",G{r}/H{r})'
        for colname, who in (("J", "top"), ("K", "bottom")):
            den = f'SUMPRODUCT(({band}="{who}")*ISNUMBER({rng}))'
            items[f"{colname}{r}"] = f'=IF({den}=0,"",SUMPRODUCT(({band}="{who}")*({rng}=1))/{den})'
        items[f"L{r}"] = f'=IF(OR(J{r}="",K{r}=""),"",J{r}-K{r})'
        items[f"M{r}"] = (f'=IF(H{r}=0,"",IF(I{r}<0.2,"Check the item: fewer than one in five got it right",'
                          f'IF(AND(L{r}<>"",N(L{r})<0),"Check the item: the bottom third beat the top third","")))')
        items[f"N{r}"] = f'=IF(H{r}=0,"",I{r}+ROW()/1000000)'
        for colname in "IJKL":
            items[f"{colname}{r}"].number_format = "0%"
    items.column_dimensions["M"].width = 52

    disc = wb.create_sheet("Discussion")
    disc["A1"] = "The solution discussion, from the most-missed item"
    disc["A1"].font = bold
    disc["B2"] = f'=IF(SUM(Items!H5:H{end})=0,"No marks entered yet.","Most-missed first: take the items from the top.")'
    for c, h in enumerate(["Order", "Q", "Right rate", "Part", "Tag", "Flag"], 1):
        cell = disc.cell(4, c, h)
        cell.font, cell.fill = white, head_fill
    keys = f"Items!$N$5:$N${end}"
    for k in range(1, n + 1):
        r = 4 + k
        disc[f"A{r}"] = k
        disc[f"B{r}"] = (f'=IF(COUNT({keys})<A{r},"",INDEX(Items!$A$5:$A${end},'
                         f'MATCH(SMALL({keys},A{r}),{keys},0)))')
        for colname, src in (("C", "I"), ("D", "B"), ("E", "E"), ("F", "M")):
            disc[f"{colname}{r}"] = (f'=IF(B{r}="","",INDEX(Items!${src}$5:${src}${end},'
                                     f'MATCH(B{r},Items!$A$5:$A${end},0)))')
        disc[f"C{r}"].number_format = "0%"
    disc.column_dimensions["F"].width = 52

    tags = wb.create_sheet("Tags")
    tags["A1"] = "The room's rate by tag and by part"
    tags["A1"].font = bold
    for c, h in enumerate(["Tag or part", "Name", "Items", "Right rate"], 1):
        cell = tags.cell(4, c, h)
        cell.font, cell.fill = white, head_fill
    present = [t for t in TAGS if any(i["tag"] == t for i in printed)]
    r = 5
    for t in present:
        tags[f"A{r}"], tags[f"B{r}"] = t, "tag"
        tags[f"C{r}"] = f'=COUNTIF(Items!$E$5:$E${end},A{r})'
        den = f"SUMPRODUCT((Items!$E$5:$E${end}=A{r})*Items!$H$5:$H${end})"
        tags[f"D{r}"] = f'=IF({den}=0,"",SUMPRODUCT((Items!$E$5:$E${end}=A{r})*Items!$G$5:$G${end})/{den})'
        tags[f"D{r}"].number_format = "0%"
        r += 1
    for p, title, *_ in part_rows(printed, source):
        tags[f"A{r}"], tags[f"B{r}"] = p, f"Part {p}. {title}"
        tags[f"C{r}"] = f'=COUNTIF(Items!$B$5:$B${end},A{r})'
        den = f"SUMPRODUCT((Items!$B$5:$B${end}=A{r})*Items!$H$5:$H${end})"
        tags[f"D{r}"] = f'=IF({den}=0,"",SUMPRODUCT((Items!$B$5:$B${end}=A{r})*Items!$G$5:$G${end})/{den})'
        tags[f"D{r}"].number_format = "0%"
        r += 1
    tags.column_dimensions["B"].width = 40

    seat_sheet = wb.create_sheet("Seats")
    seat_sheet["A1"] = "Each seat's rate by tag, for Monday's remediation read"
    seat_sheet["A1"].font = bold
    seat_sheet["A4"] = "Seat"
    for c, t in enumerate(present, 2):
        seat_sheet.cell(4, c, t)
    for c in range(1, 2 + len(present)):
        cell = seat_sheet.cell(4, c)
        cell.font, cell.fill = white, head_fill
    tagrow = f"Marks!$B$3:${last}$3"
    for k in range(S):
        r, mr = first + k, first + k
        seat_sheet[f"A{r}"] = k + 1
        row_rng = f"Marks!$B${mr}:${last}${mr}"
        for c in range(2, 2 + len(present)):
            h = f"{col(c)}$4"
            den = f"SUMPRODUCT(({tagrow}={h})*ISNUMBER({row_rng}))"
            seat_sheet.cell(r, c).value = f'=IF({den}=0,"",SUMPRODUCT(({tagrow}={h})*({row_rng}=1))/{den})'
            seat_sheet.cell(r, c).number_format = "0%"

    # Ratings: each seat's step-one rating of each part, 1 to 4, beside that seat's rate in the part,
    # and for the room each part's mean rating, its right rate, and how many seats rated a part 3 or
    # 4 and got under half of it right, which is where confidence ran ahead of the work.
    rows_p = part_rows(printed, source)
    rate = wb.create_sheet("Ratings")
    rate["A1"] = "Step one: each part's rating beside its score"
    rate["A1"].font = bold
    rate["A2"] = "Type each seat's ratings, 1 to 4, from the answer sheet; the rates on the right are computed."
    k_parts = len(rows_p)
    rate.cell(4, 1, "Seat")
    for j, (pn, ptitle, *_) in enumerate(rows_p):
        rate.cell(3, 2 + j, pn)
        rate.cell(4, 2 + j, f"Rating, part {pn}")
        rate.cell(3, 3 + k_parts + j, pn)
        rate.cell(4, 3 + k_parts + j, f"Right rate, part {pn}")
    for c in range(1, 3 + 2 * k_parts):
        if rate.cell(4, c).value:
            rate.cell(4, c).font, rate.cell(4, c).fill = white, head_fill
    partrow = f"Marks!$B$2:${last}$2"
    for k in range(S):
        r = first + k
        rate[f"A{r}"] = k + 1
        row_rng = f"Marks!$B${r}:${last}${r}"
        for j in range(k_parts):
            rate.cell(r, 2 + j).fill = input_fill
            pc = f"{col(3 + k_parts + j)}$3"
            den = f"SUMPRODUCT(({partrow}={pc})*ISNUMBER({row_rng}))"
            cell_ = rate.cell(r, 3 + k_parts + j)
            cell_.value = f'=IF({den}=0,"",SUMPRODUCT(({partrow}={pc})*({row_rng}=1))/{den})'
            cell_.number_format = "0%"
    sr = last_row + 2
    rate[f"A{sr}"] = "The room"
    rate[f"A{sr}"].font = bold
    for c, h in enumerate(["Part", "Mean rating", "Right rate", "Rated 3 or 4, under half right"], 1):
        cell_ = rate.cell(sr + 1, c, h)
        cell_.font, cell_.fill = white, head_fill
    for j, (pn, ptitle, *_) in enumerate(rows_p):
        r = sr + 2 + j
        rc, sc = col(2 + j), col(3 + k_parts + j)
        rate[f"A{r}"] = f"Part {pn}. {ptitle}"
        rate[f"B{r}"] = f'=IF(COUNT({rc}{first}:{rc}{last_row})=0,"",AVERAGE({rc}{first}:{rc}{last_row}))'
        rate[f"B{r}"].number_format = "0.0"
        tag_rows = f"Tags!$A$5:$A${4 + len(present) + len(rows_p)}"
        tag_rates = f"Tags!$D$5:$D${4 + len(present) + len(rows_p)}"
        rate[f"C{r}"] = f'=IFERROR(INDEX({tag_rates},MATCH({pn},{tag_rows},0)),"")'
        rate[f"C{r}"].number_format = "0%"
        rate[f"D{r}"] = (f"=SUMPRODUCT(({rc}{first}:{rc}{last_row}>=3)*ISNUMBER({sc}{first}:{sc}{last_row})"
                         f"*({sc}{first}:{sc}{last_row}<0.5))")
    rate.column_dimensions["A"].width = 44
    rate.freeze_panes = "B5"
    rating_verdict = f"D{sr + 2}"

    base = ROOT / "content" / week / "SAT" / "answer-key"
    base.mkdir(parents=True, exist_ok=True)
    xlsx = base / f"C2_{week}_SAT_item_analysis_TRAINER.xlsx"
    wb.save(xlsx)
    sets = [{"sheet": "Marks", "cell": f"{col(2 + j)}{first + k}", "value": v}
            for k, row in enumerate(DEMO_MARKS) for j, v in enumerate(row)]
    sets += [{"sheet": "Ratings", "cell": f"B{first + k}", "value": v} for k, v in enumerate(DEMO_RATINGS)]
    manifest = {
        "workbook": xlsx.name,
        "verdicts": [{"sheet": "Discussion", "cell": "B2", "expect": "No marks entered yet."},
                     {"sheet": "Ratings", "cell": rating_verdict, "expect": "0"}],
        "flips": [{"name": "six seats marked on the first five items",
                   "set": sets,
                   "verdicts": [
                       {"sheet": "Discussion", "cell": "B2", "contains": "Most-missed first"},
                       {"sheet": "Discussion", "cell": "B5", "expect": str(printed[1]["q"])},
                       {"sheet": "Items", "cell": "M6", "contains": "fewer than one in five"},
                       {"sheet": "Items", "cell": "M7", "contains": "bottom third beat the top third"},
                       {"sheet": "Marks", "cell": f"{BAND}{first}", "expect": "top"},
                       {"sheet": "Marks", "cell": f"{BAND}{first + 5}", "expect": "bottom"},
                       {"sheet": "Marks", "cell": f"{BAND}{first + 2}", "expect": "middle"},
                       {"sheet": "Ratings", "cell": rating_verdict, "expect": "2"}]}],
    }
    body = yaml.safe_dump(manifest, sort_keys=False, width=110, allow_unicode=True)
    (base / f"C2_{week}_SAT_item_analysis_recalc_INTERNAL.md").write_text(
        f"# Recalculation manifest: Week {int(week[1:])} item analysis\n\n"
        "INTERNAL. Written by `scripts/build_saturday_paper.py --docx` beside the workbook and read by "
        "`scripts/xlsx_recalc.py`. As shipped, no marks are entered. The flip marks six seats on the "
        "first five items so that seat 1 tops the room and seat 6 sits at the bottom, Q2 is right once "
        "in six, and on Q3 the bottom third beats the top third; both flags, the bands and the "
        "discussion order must follow. The same six seats rate Part 1 as 3, 4, 2, 3, 1 and 4, so two of "
        "them (seats 4 and 6) rated it 3 or 4 and got under half of it right.\n\n```yaml\n" + body + "```\n",
        encoding="utf-8")
    print(f"wrote {xlsx.relative_to(ROOT)}")


def write_docx(week):
    """Write the week's paper and key as Word files next to their markdown."""
    import subprocess
    import tempfile
    bank = read_bank(TRACKER)
    edits = yaml.safe_load(EDITS.read_text(encoding="utf-8")) if EDITS.exists() else {}
    notes = apply_edits(bank, edits)
    paper = next(p for p in bank if week_of(p) == week)
    data, source = bank[paper], read_source(week)
    printed = assemble(data, source)
    moved = moved_items(data, source)
    spec = docx_spec(paper, data, saturday_date(week), printed, source,
                     paper_minutes(week, data["slot"]), notes, moved)
    p_md, k_md = targets(week)
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
        json.dump(spec, fh)
    r = subprocess.run(["node", str(HERE / "saturday_docx.js"), fh.name,
                        str(p_md.with_suffix(".docx")), str(k_md.with_suffix(".docx"))],
                       capture_output=True, text=True)
    pathlib.Path(fh.name).unlink(missing_ok=True)
    if r.returncode:
        sys.exit(f"FAIL  the Word files were not written: {r.stderr.strip()[-600:]}")
    missing = [s["n"] for sec in spec["paper"]["sections"] for s in sec["blocks"]
               if s["kind"] == "set" and not s["image"] and not s["table"] and not s.get("code")]
    for number in missing:
        print(f"INFO  set {number} has no exhibit in the source file, or mermaid-cli is missing")
    print(r.stdout.strip())
    if source.get("parts"):
        write_item_analysis(week, printed, source)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("weeks", nargs="*", help="weeks as W01; none with --all")
    ap.add_argument("--all", action="store_true", help="every week with a SAT folder and a paper")
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if a file differs")
    ap.add_argument("--docx", action="store_true", help="also write the paper and key as Word files")
    a = ap.parse_args()
    if not a.weeks and not a.all:
        sys.exit("FAIL  name a week, as W01, or pass --all")
    only = None if a.all else {w.upper() for w in a.weeks}
    files, notes = render_all(only=only)
    for paper, no, state, why in notes:
        if state != "applied":
            print(f"{'WARN' if state == 'broken' else 'INFO'}  paper_edits {paper} item {no}: {state}, {why}")
    if only and not files:
        sys.exit(f"FAIL  no paper in the bank for {', '.join(sorted(only))}, or no SAT folder for it")
    stale = [p for p, t in files.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
    for p in stale:
        if a.check:
            print(f"STALE {p.relative_to(ROOT)}")
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(files[p], encoding="utf-8")
            print(f"wrote {p.relative_to(ROOT)}")
    print(f"      {len(files)} file(s), {len(stale)} {'stale' if a.check else 'updated'}")
    if a.check and stale:
        sys.exit(1)
    if a.docx and not a.check:
        for week in sorted({p.parts[-4] for p in files}):
            write_docx(week)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 scripts/build_saturday_paper.py W01
#     With the W01 source file as committed on 30 September 2026: the paper prints 51 items in six
#     parts, page one carrying the rules and the blueprint (113.5 timed minutes, 19 easy, 21 medium,
#     11 hard), every item headed "Q<n> · <level> · <format>", scenario sets numbered 1 to 5 in the
#     order they print, and a stretch page of four written items and six recall lines moved from
#     the bank. The TRAINER key carries 51 rows with a Part column, the blueprint with its total
#     row, the guessing floor (average 10.9 of 51; fewer than one guesser in twenty reaches 16) and
#     the stretch answers, the moved items marked "moved from the timed paper".
# python3 scripts/build_saturday_paper.py W01 --check     (straight after the line above)
#     "2 file(s), 0 stale", exit 0.
# python3 scripts/build_saturday_paper.py W01 --docx
#     Also writes the paper and the key as Word files, and, because W01 has parts,
#     answer-key/C2_W01_SAT_item_analysis_TRAINER.xlsx with its recalc manifest beside it;
#     python3 scripts/xlsx_recalc.py content/W01/SAT then reports 1 verdict computed and 1 decision
#     flipped and re-asserted, PASS.
# W01's parts with bank item 17 deleted from part 2
#     FAIL: bank items [17] sit in no part and not in stretch_bank.
# W01's stretch_bank with 7 swapped for 17 (and 7 placed in part 1)
#     FAIL: bank items [17] are not recall items; only fill in the blank and true or false move.
# W01's stretch_bank with a seventh number added
#     FAIL: 7 bank items moved to the stretch page, and at most 6 may move.
# W01's part 2 with bank item 37 moved to the end of the part
#     FAIL: scenario set 1 is split: its items must print together.
# A part naming new:nothing
#     FAIL: part 1 names new:nothing, which is neither a bank number nor an addition's id.
# python3 scripts/build_saturday_paper.py W03
#     FAIL: no paper in the bank for W03, since build weeks carry no paper.
# paper_edits.yaml naming option e on a four-option item
#     WARN: that edit is broken, option e not found; the item renders with the bank's wording.
# The tracker updated with an edit's exact wording
#     INFO: that edit is folded, and it can be deleted from paper_edits.yaml.
# python3 scripts/build_saturday_paper.py
#     FAIL: name a week, as W01, or pass --all.
# A week whose source file has no parts, or no source file at all
#     The older layout: sections by item type in the bank's order, additions after the bank's
#     items of their type, no levels printed, and no item-analysis workbook.
# An exhibit whose mermaid fence has a syntax error, built with --docx
#     The build stops: the room sits the Word paper, so an exhibit that cannot render is a failure.

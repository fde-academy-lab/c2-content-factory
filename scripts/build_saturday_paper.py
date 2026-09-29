"""Render a week's Saturday recap paper and its key from the tracker's item bank.

    python3 scripts/build_saturday_paper.py W01            # write Week 1's paper and key
    python3 scripts/build_saturday_paper.py W01 --docx     # the same, plus both as Word files
    python3 scripts/build_saturday_paper.py --all          # every week with a SAT folder and a paper
    python3 scripts/build_saturday_paper.py W01 --check    # write nothing; exit 1 if either differs

The bank is the 'Saturday papers' tab of docs/curriculum/source.xlsx. The STUDENT paper prints the
items only, grouped by item type in the bank's order and numbered Q1 upward as printed, with a line
for the name and the count of items right and nothing else. The TRAINER key carries every other
column (key, type, level, tag, roles, day, minutes and the interview anchor), the marking rule, and
the item numbers by tag, level and day, which is what the Academic TA tallies for Monday's
remediation read.

Three sources are laid on the bank before rendering:

  data/programme/paper_edits.yaml    rewords options of one item, never its stem or key
  data/programme/facts.yaml          saturday_papers.paper_minutes, where a paper runs longer than
                                     the tracker's slot
  content/W{ww}/SAT/internal/C2_W{ww}_SAT_paper_source_INTERNAL.yaml, the week's own additions:
      additions   new timed items, printed inside their type's section after the bank's, each
                  carrying why, wrong and answer for the key; listed in the key as waiting for the
                  tracker
      exhibits    per scenario set number, a mermaid fence or a small table printed once under the
                  set's situation, drawn only from the situation's own numbers
      notes       per bank item number: why the key holds, why each wrong option fails
                  ({letter: reason}), and the interview answer in one breath
      stretch     untimed, unmarked written items for fast finishers, each with its answer
  Write the file in block style: a comma inside an inline {a: ..., b: ...} mapping splits a
  reason in two without any error.

--docx renders every exhibit through mermaid-cli and writes the paper and the key as Word files
through scripts/saturday_docx.js, in the layout of the requester's baseline diagnostic. The markdown
stays the file the gates read, so --docx follows every change to it.
scripts/sync_programme.py re-renders every week whose paper already exists, so a changed item or a
new edit reaches a built Saturday with one sync; a new Saturday starts with this script.
"""
import argparse
import datetime as dt
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


def assemble(data, source):
    """The items in printed order, each carrying q, its printed number.

    Sections follow the item types in the bank's order. Within a section the bank's items come
    first, in the bank's order, and the source's additions follow in the order the file lists them.
    """
    bank = sorted((dict(i, added=False) for i in data["items"]), key=lambda i: i["no"])
    notes = {str(k): v for k, v in (source.get("notes") or {}).items()}
    for item in bank:
        item["note"] = notes.get(str(item["no"]), {})
    added = []
    for a in source.get("additions") or []:
        added.append({"no": None, "type": a["type"], "level": a["level"], "tag": a["tag"],
                      "roles": a.get("roles", ""), "day": a.get("day", ""),
                      "min": float(a.get("min", 0)), "key": str(a["key"]),
                      "text": str(a["text"]).strip(), "anchor": a.get("anchor", ""), "edit": None,
                      "added": True, "note": {"why": a.get("why", ""), "wrong": a.get("wrong", {}),
                                              "answer": a.get("answer", "")}})
    order = []
    for item in bank + added:
        if item["type"] not in order:
            order.append(item["type"])
    printed = sorted(bank + added, key=lambda i: (order.index(i["type"]), i["added"]))
    for q, item in enumerate(printed, 1):
        item["q"] = q
    return printed


def groups(items):
    """Consecutive runs of one type, in printed order."""
    out = []
    for item in items:
        if out and out[-1][0] == item["type"]:
            out[-1][1].append(item)
        else:
            out.append((item["type"], [item]))
    return out


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


def render_item(item):
    stem, options, answer = parts(item)
    block = [f"#### Q{item['q']}", ""] + stem
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


def exhibit_md(ex):
    out = []
    if ex.get("mermaid"):
        out += ["```mermaid", str(ex["mermaid"]).rstrip(), "```", ""]
    if ex.get("table"):
        head, rows = ex["table"]["head"], ex["table"]["rows"]
        out += ["| " + " | ".join(map(str, head)) + " |", "|" + "---|" * len(head)]
        out += ["| " + " | ".join(map(str, r)) + " |" for r in rows] + [""]
    if ex.get("caption"):
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


def when_of(date, sep):
    return date.strftime("%A %d %B %Y").replace(" 0", " ") + sep if date else ""


STRETCH_TITLE = "Stretch: untimed, and not marked"
STRETCH_INTRO = ("For anyone who finishes early. Nothing here is counted; each item is the kind an "
                 "interviewer asks after your first answer, so write the answer you would say.")


def render_paper(paper, data, date, printed, source, minutes):
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


def render_key(paper, data, date, notes, printed, source, minutes):
    n, week = len(printed), int(paper[1:])
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
           "1. Papers are swapped, so nobody marks their own.",
           "2. The Academic TA reads the key out section by section, and the marker writes a tick or a "
           "cross beside each item.",
           "3. An item is right when its answer matches the key: every correct letter and no other "
           "on a more-than-one item, the number on an applied maths item (the working belongs to the "
           "discussion), and the whole sequence on an ordering item. The programme has set no "
           "partial-credit rule, so this key uses none.",
           f"4. The marker writes the count of ticks as Items right on the front, out of {n}, and "
           "hands the paper back.",
           "5. The TA collects the papers and tallies the misses by tag, using the table below; that "
           "tally is Monday's remediation read. It is never a ranking and never read out by name.", "",
           "## The key", "",
           "| Q | Key | Type | Level | Tag | Roles | Day | Min | Source | Interview anchor |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for i in printed:
        src = "new" if i["added"] else f"bank {i['no']}"
        out.append(f"| {i['q']} | {cell(i['key'])} | {i['type']} | {i['level']} | {i['tag']} | "
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
    out += ["", "## Items by tag, level and day, for the tally", ""]
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
                "These options differ from the tracker's wording, because the bank's key was the "
                "longest option. The stem and the key are the tracker's. Accept an edit by copying "
                "it into the tracker; reject it by deleting it from `data/programme/paper_edits.yaml`.",
                ""]
        for _, no, _, why in mine:
            item = next(i for i in printed if i["no"] == int(no))
            opts = ", ".join(sorted(item["edit"].get("options", {})))
            out.append(f"- Q{item['q']} (bank {no}), option {opts} "
                       f"({item['edit'].get('status', 'proposed')}): {why}")
    stretch = source.get("stretch") or []
    if stretch:
        out += ["", "## The stretch page", ""]
        for k, s in enumerate(stretch, 1):
            out.append(f"- Stretch {k}: {s.get('answer', '')}")
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
        minutes = paper_minutes(week, data["slot"])
        out[p_path] = render_paper(paper, data, date, printed, source, minutes)
        out[k_path] = render_key(paper, data, date, notes, printed, source, minutes)
    return out, notes


# --------------------------------------------------------------------------- the Word files
RULES = [
    ["Time", "{minutes} minutes in one sitting. Each section gives its minutes as a guide, not a limit."],
    ["Tools", "Pen and this paper only: no laptop, no phone, no notes and no assistant."],
    ["Answers", "Each section says how: a word or a number on the line, T or F, one circled letter, "
                "every correct letter, the working and the answer, or the letters in order. "
                "Copy every answer to the answer sheet at the back."],
    ["Afterwards", "Papers are swapped and marked against the key, then the discussion takes the items "
                   "the room missed most. The paper is ungraded and goes on no record."],
]
PURPOSE = ("Saying the week out loud is the interview skill itself. This paper finds which of the "
           "week's decisions you can make cold, with no notes and no assistant, so Monday's practice "
           "starts where each of us needs it. Every item is a Kalpa business question first and a "
           "technique question second, which is the order interviewers use.")


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
    png = render_mermaid(str(ex["mermaid"]), "png")
    if not png:
        raise SystemExit("mermaid-cli is not installed, so the Word paper would lose its exhibits. "
                         "Install it with npm install -g @mermaid-js/mermaid-cli and build again.")
    with Image.open(png) as img:
        w, h = (d / PNG_SCALE for d in img.size)
    # The PNG holds PNG_SCALE pixels per CSS pixel for sharpness; the page prints it at its
    # natural size, capped at the column's width.
    scale = min(1.0, 610 / w)
    return {"path": str(png), "w": round(w * scale), "h": round(h * scale)}


def docx_spec(paper, data, date, printed, source, minutes, notes):
    week, n = week_of(paper), len(printed)
    exhibits = {str(k): v for k, v in (source.get("exhibits") or {}).items()}
    sections, glance, letters = [], [], "ABCDEFGHIJ"
    for k, (kind, run) in enumerate(groups(printed)):
        blocks = []
        for item, number, situation in sets_in(run):
            if number:
                ex = exhibits.get(number, {})
                blocks.append({"kind": "set", "n": number, "situation": situation,
                               "image": exhibit_png(ex), "table": ex.get("table"),
                               "caption": ex.get("caption", "")})
            stem, options, answer = parts(item)
            blocks.append({"kind": "item", "q": item["q"], "type": item["type"], "lines": stem,
                           "options": [list(o) for o in options], "answer": answer})
        mins = sum(i["min"] for i in run)
        sections.append({"letter": letters[k], "title": kind,
                         "intro": f"{len(run)} items, {span(run)}, about {mins:g} minutes. "
                                  f"{HOW.get(kind, '')}", "blocks": blocks})
        glance.append([f"{letters[k]}. {kind}", HOW.get(kind, ""), span(run), f"{mins:g}"])
    rows = []
    for i in printed:
        _, options, answer = parts(i)
        if i["type"] == "True or false":
            rows.append({"q": i["q"], "kind": "tf"})
        elif options and i["type"] != "Order the steps":
            rows.append({"q": i["q"], "kind": "choice", "count": len(options)})
        else:
            rows.append({"q": i["q"], "kind": "line"})
    stretch = source.get("stretch") or []
    title = f"Week {int(paper[1:])} recap paper"
    meta = (f"Cohort 2  ·  {when_of(date, '  ·  ')}{minutes} minutes  ·  {n} items  ·  "
            "pen and paper  ·  ungraded")
    paper_spec = {"title": title, "meta": meta, "header": f"Cohort 2  ·  {title}", "purpose": PURPOSE,
                  "rules": [[r, d.format(minutes=minutes)] for r, d in RULES], "glance": glance,
                  "sections": sections, "stretchTitle": STRETCH_TITLE, "stretchIntro": STRETCH_INTRO,
                  "stretch": [{"lines": [ln.strip() for ln in str(s["text"]).strip().split(chr(10))
                                         if ln.strip()]} for s in stretch],
                  "sheet": {"n": n, "rows": rows,
                            "note": "Fill in pen. Circle one letter per row, or every correct letter "
                                    "where the item asks for more than one; write the others on the line."}}
    reasons = []
    for i in printed:
        note = i["note"]
        if note.get("why") or note.get("wrong") or note.get("answer"):
            reasons.append({"q": i["q"], "key": i["key"],
                            "meta": f"{i['type']}, {i['level']}, {i['tag']}, {i['day']}",
                            "why": note.get("why", ""),
                            "wrong": sorted([k, v] for k, v in (note.get("wrong") or {}).items()),
                            "answer": note.get("answer", ""), "anchor": i["anchor"]})
    tally = []
    for tag in TAGS:
        hit = [f"Q{i['q']}" for i in printed if i["tag"] == tag]
        tally.append(f"{tag} ({len(hit)}): {', '.join(hit) if hit else 'none'}")
    for lv in ("Easy", "Medium", "Hard"):
        hit = [f"Q{i['q']}" for i in printed if i["level"] == lv]
        tally.append(f"{lv} ({len(hit)}): {', '.join(hit)}")
    added = [i for i in printed if i["added"]]
    key_spec = {"title": f"{title}: key", "header": f"Cohort 2  ·  {title}  ·  key  ·  TRAINER",
                "meta": f"TRAINER.  {when_of(date, '  ·  ')}{minutes} minutes  ·  {n} items",
                "marking": [
                    "Papers are swapped, so nobody marks their own.",
                    "The Academic TA reads the key out section by section, and the marker ticks or "
                    "crosses each item on the answer sheet.",
                    "An item is right when its answer matches the key: every correct letter and no "
                    "other on a more-than-one item, the number on an applied maths item, and the whole "
                    "sequence on an ordering item. No partial credit.",
                    f"The marker writes the count of ticks as Items right, out of {n}, and hands the "
                    "paper back.",
                    "The TA tallies the misses by tag for Monday's remediation read, never a ranking "
                    "and never read out by name."],
                "rows": [[str(i["q"]), i["key"], i["type"], i["level"], i["tag"], i["day"],
                          "new" if i["added"] else f"bank {i['no']}"] for i in printed],
                "reasons": reasons, "tally": tally,
                "additions": [f"Q{i['q']} ({i['type']}, {i['level']}, {i['tag']}): "
                              f"{next(iter(parts(i)[0]), '')}" for i in added],
                "additionsNote": "These items come from the week's source file, not the tracker. "
                                 "Accept one by adding it to the tracker's Saturday papers tab.",
                "stretch": [str(s.get("answer", "")) for s in stretch]}
    return {"paper": paper_spec, "key": key_spec}


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
    spec = docx_spec(paper, data, saturday_date(week), printed, source,
                     paper_minutes(week, data["slot"]), notes)
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
               if s["kind"] == "set" and not s["image"] and not s["table"]]
    for number in missing:
        print(f"INFO  set {number} has no exhibit in the source file, or mermaid-cli is missing")
    print(r.stdout.strip())


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
#     Writes content/W01/SAT/paper/C2_W01_SAT_recap_paper_STUDENT.md (52 items in seven sections,
#     items only) and the TRAINER key with 52 rows, the tally lists and the pending option edits.
# python3 scripts/build_saturday_paper.py W01 --check     (straight after the line above)
#     "2 file(s), 0 stale", exit 0.
# python3 scripts/build_saturday_paper.py W03
#     FAIL: no paper in the bank for W03, since build weeks carry no paper.
# paper_edits.yaml naming option e on a four-option item
#     WARN: that edit is broken, option e not found; the item renders with the bank's wording.
# The tracker updated with an edit's exact wording
#     INFO: that edit is folded, and it can be deleted from paper_edits.yaml.
# python3 scripts/build_saturday_paper.py
#     FAIL: name a week, as W01, or pass --all.
# python3 scripts/build_saturday_paper.py W01 --docx   (no source file in W01/SAT/internal)
#     Writes both markdown files and both Word files from the bank alone, numbered Q1 to Q52,
#     at 120 minutes from facts.yaml, and prints one INFO line per scenario set with no exhibit.
# The same, with a source file carrying one addition of type Scenario set
#     The addition prints as Q46, after the bank's scenario items and before applied maths;
#     the key lists it under New items waiting for the tracker with Source "new".
# The same, with an exhibit whose mermaid fence has a syntax error
#     mermaid-cli draws no PNG, the set prints without a picture, and the INFO line names it.

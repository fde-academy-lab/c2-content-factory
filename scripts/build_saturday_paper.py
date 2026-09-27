"""Render a week's Saturday recap paper and its key from the tracker's item bank.

    python3 scripts/build_saturday_paper.py W01            # write Week 1's paper and key
    python3 scripts/build_saturday_paper.py --all          # every week with a SAT folder and a paper
    python3 scripts/build_saturday_paper.py W01 --check    # write nothing; exit 1 if either differs

The bank is the 'Saturday papers' tab of docs/curriculum/source.xlsx. The STUDENT paper prints the
Item column only, grouped by item type in the bank's order, with a line for the name and the count
of items right and nothing else. The TRAINER key carries every other column (key, type, level, tag,
roles, day, minutes and the interview anchor), the marking rule, and the item numbers by tag, level
and day, which is what the Academic TA tallies for Monday's remediation read.

Edits in data/programme/paper_edits.yaml are laid on top of the bank before rendering. Each one
rewords options of one item and never its stem or key; the key file lists every edit still waiting
for the tracker. scripts/sync_programme.py re-renders every week whose paper already exists, so a changed item or
a new edit reaches a built Saturday with one sync; a new Saturday starts with this script.
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


def groups(items):
    """Consecutive runs of one type, in the bank's order."""
    out = []
    for item in sorted(items, key=lambda i: i["no"]):
        if out and out[-1][0] == item["type"]:
            out[-1][1].append(item)
        else:
            out.append((item["type"], [item]))
    return out


def span(items):
    a, b = items[0]["no"], items[-1]["no"]
    return f"item {a}" if a == b else (f"items {a} and {b}" if b == a + 1 else f"items {a} to {b}")


def render_item(item):
    lines, out, has_options = item["text"].split("\n"), [], False
    for ln in lines:
        s = ln.strip()
        if not s or SET_START.match(s) or SET_CONT.match(s):
            continue
        m = OPTION.match(s)
        if m:
            if not has_options:
                out.append("")
            has_options = True
            out.append(f"{m.group(1)}) {m.group(2)}")
        else:
            out.append(s)
    block = [f"#### {item['no']}", ""] + out
    if item["type"] == "Applied maths":
        block += ["", "Working:", "", "Answer: ____________________"]
    elif item["type"] == "Order the steps":
        block += ["", "Order: ____________________"]
    elif not has_options:
        block += ["", "Answer: ____________________"]
    return block + [""]


def render_paper(paper, data, date):
    items = sorted(data["items"], key=lambda i: i["no"])
    n, week = len(items), int(paper[1:])
    when = date.strftime("%A %d %B %Y").replace(" 0", " ") + " · " if date else ""
    out = [f"# Week {week} recap paper", "",
           f"{when}{data['slot']} minutes · {n} items · pen and paper, no assistant, no notes", "",
           "Name: ____________________    Marked by: ____________________    "
           f"Items right: ____ of {n}", "",
           "Answer every item in the space it gives you. Each section says how. After the break the "
           "papers are swapped and marked against the key, and the discussion starts with the items "
           "the room missed most.", ""]
    letters = "ABCDEFGHIJ"
    for k, (kind, run) in enumerate(groups(items)):
        out += ["---", "", f"## {letters[k]}. {kind} ({span(run)})", "", HOW.get(kind, ""), ""]
        current_set = None
        for item in run:
            first = item["text"].split("\n")[0].strip()
            m = SET_START.match(first)
            if m and m.group(1) != current_set:
                current_set = m.group(1)
                out += [f"### Set {current_set}", "", f"**Situation.** {m.group(2)}", ""]
            out += render_item(item)
    return "\n".join(out).rstrip() + "\n"


def cell(v):
    return str(v).replace("|", "\\|").replace("\n", "<br>")


def render_key(paper, data, date, notes):
    items = sorted(data["items"], key=lambda i: i["no"])
    n, week = len(items), int(paper[1:])
    minutes = sum(i["min"] for i in items)
    levels = {lv: sum(1 for i in items if i["level"] == lv) for lv in ("Easy", "Medium", "Hard")}
    when = date.strftime("%A %d %B %Y").replace(" 0", " ") + ". " if date else ""
    out = [f"# Week {week} recap paper: key", "",
           "TRAINER. Rendered from the tracker's item bank by `scripts/build_saturday_paper.py`. "
           "Change an item in the tracker, or an option in `data/programme/paper_edits.yaml`, and "
           "sync; never edit this file by hand.", "",
           f"{when}A {data['slot']}-minute slot holding {n} items at {minutes:g} minutes by the "
           f"blueprint's pace: {levels['Easy']} easy, {levels['Medium']} medium and {levels['Hard']} "
           f"hard.", "",
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
           "| No. | Key | Type | Level | Tag | Roles | Day | Min | Interview anchor |",
           "|---|---|---|---|---|---|---|---|---|"]
    for i in items:
        out.append(f"| {i['no']} | {cell(i['key'])} | {i['type']} | {i['level']} | {i['tag']} | "
                   f"{cell(i['roles'])} | {i['day']} | {i['min']:g} | {cell(i['anchor'])} |")
    out += ["", "## Items by tag, level and day, for the tally", ""]
    for tag in TAGS:
        hit = [str(i["no"]) for i in items if i["tag"] == tag]
        out.append(f"- {tag} ({len(hit)}): {', '.join(hit) if hit else 'none'}")
    for lv in ("Easy", "Medium", "Hard"):
        hit = [str(i["no"]) for i in items if i["level"] == lv]
        out.append(f"- {lv} ({len(hit)}): {', '.join(hit)}")
    for day in ("Mon", "Tue", "Wed", "Thu", "Fri"):
        hit = [str(i["no"]) for i in items if i["day"] == day]
        if hit:
            out.append(f"- {day} ({len(hit)}): {', '.join(hit)}")
    mine = [x for x in notes if x[0] == paper and x[2] == "applied"]
    if mine:
        out += ["", "## Option edits laid on the bank, waiting for the tracker", "",
                "These options differ from the tracker's wording, because the bank's key was the "
                "longest option. The stem and the key are the tracker's. Accept an edit by copying "
                "it into the tracker; reject it by deleting it from `data/programme/paper_edits.yaml`.",
                ""]
        for _, no, _, why in mine:
            edit = next(i["edit"] for i in items if i["no"] == int(no))
            opts = ", ".join(sorted(edit.get("options", {})))
            out.append(f"- Item {no}, option {opts} ({edit.get('status', 'proposed')}): {why}")
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
        out[p_path] = render_paper(paper, data, date)
        out[k_path] = render_key(paper, data, date, notes)
    return out, notes


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("weeks", nargs="*", help="weeks as W01; none with --all")
    ap.add_argument("--all", action="store_true", help="every week with a SAT folder and a paper")
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if a file differs")
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

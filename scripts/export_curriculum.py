"""Export every tab of docs/curriculum/source.xlsx to markdown, so a build session reads
curriculum rows as text rather than opening a spreadsheet.

Run from the repository root after any workbook change:

    python3 scripts/export_curriculum.py            # write the exports
    python3 scripts/export_curriculum.py --check    # exit 1 if any export is out of date

scripts/sync_programme.py calls this as its first step, so most people never run it alone.

A tab takes one of four shapes, and the exporter reads the shape from the tab's own header row
rather than from its name, so a renamed or moved column cannot silently change the output.

- A day tab (every week from W0 to W16) has a title in row 1, column names in row 2, a one-line
  description of each column in row 3 and one day per row from row 4. The day heading carries the
  day and its focus; every other column becomes a section in the order the workbook puts it, which
  is why the business scenario leads and the technique follows it. A sixteenth column, such as the
  IITGN faculty session column of the teaching weeks, is exported like any other.
- A week-level tab (the capstone) has the same three header rows with 'Week' as its first column
  and one week per row, so the heading is the week and every other column is a section.
- A grid tab (the 20-Week Plan) is a table with prose above and below it, and is exported as a
  markdown table so the columns stay aligned.
- The Saturday papers tab is the INTERNAL item bank with its key. It is exported as the blueprint
  table, then one section per paper, each a table in the bank's own column order.

Structure and anything else keep the plain export: one line per row, cells joined by ' | '.
"""
import argparse
import datetime as dt
import pathlib
import re
import sys

import openpyxl

SRC = pathlib.Path("docs/curriculum/source.xlsx")
OUT = pathlib.Path("docs/curriculum")

DAY_COL = "Day"
FOCUS_COL = "Day focus"
WEEK_COL = "Week"
HEADER_ROW = 2
FIRST_DATA_ROW = 4

# Columns every day tab must carry. A tab missing one of these is a workbook error rather than
# something to export quietly, because a day pack built from a half-read row is worse than no pack.
REQUIRED = [
    "Day",
    "Business scenario of the day",
    "Day focus",
    "Thinking we train, before any tool",
    "Trainer agenda",
    "Learner outcome",
    "Subtopics (technique in service of the scenario)",
    "Trainer notes",
    "Client zero data (TRAINER ONLY)",
    "In-session exercises",
    "After-class tasks",
    "Interview angle",
    "Trainer resources",
    "Student references",
    "Kahoot quiz plan",
]

PLAN_TAB = "20-Week Plan"
PLAN_FIRST_HEADER = "Wk"
PAPERS_TAB = "Saturday papers"
PAPER_FIRST_HEADER = "Paper"
BANK_SECOND_HEADER = "No."


def clean(value):
    if value is None:
        return ""
    if isinstance(value, dt.datetime) and value.time() == dt.time(0, 0):
        value = value.date()
    if isinstance(value, dt.date) and not isinstance(value, dt.datetime):
        return value.strftime("%a %d %b %Y")
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    return str(value).strip()


def cell_md(value):
    """One workbook cell as one markdown table cell: pipes escaped, line breaks kept as <br>."""
    return clean(value).replace("|", "\\|").replace("\n", "<br>")


def md_table(headers, rows):
    out = ["| " + " | ".join(cell_md(h) for h in headers) + " |",
           "|" + "---|" * len(headers)]
    for row in rows:
        out.append("| " + " | ".join(cell_md(v) for v in row) + " |")
    return out


def file_name(title):
    return re.sub(r"[^A-Za-z0-9]+", "_", title).strip("_") + ".md"


def headers_of(ws, row=HEADER_ROW):
    return [clean(ws.cell(row=row, column=c).value) for c in range(1, ws.max_column + 1)]


def is_week_tab(title):
    return bool(re.match(r"^W\d+\b", title.strip()))


def shape_of(ws):
    if is_week_tab(ws.title):
        headers = headers_of(ws)
        if headers and headers[0] == WEEK_COL:
            return "weekly"
        return "days"
    if ws.title == PLAN_TAB:
        return "plan"
    if ws.title == PAPERS_TAB:
        return "papers"
    return "plain"


def export_days(ws):
    headers = headers_of(ws)
    missing = [h for h in REQUIRED if h not in headers]
    if missing:
        sys.exit(f"FAIL  {ws.title}: the workbook is missing {missing}")

    focus_idx = headers.index(FOCUS_COL)
    day_idx = headers.index(DAY_COL)
    body = [i for i in range(len(headers)) if i not in (day_idx, focus_idx) and headers[i]]

    lines = ["# " + ws.title, ""]
    days = 0
    for r in range(FIRST_DATA_ROW, ws.max_row + 1):
        day = clean(ws.cell(row=r, column=day_idx + 1).value).replace("\n", " ")
        if not day:
            continue
        days += 1
        focus = clean(ws.cell(row=r, column=focus_idx + 1).value)
        lines += ["## " + day + (" · " + focus if focus else ""), ""]
        for i in body:
            val = clean(ws.cell(row=r, column=i + 1).value)
            if val:
                lines += ["### " + headers[i], "", val, ""]
    return lines, f"{days} days"


def export_weekly(ws):
    """The capstone tab: one week per row, then standing rules and an hours table below."""
    headers = headers_of(ws)
    width = max(i for i, h in enumerate(headers) if h) + 1
    lines = ["# " + ws.title, "", clean(ws.cell(row=1, column=1).value), ""]
    weeks = 0
    r = FIRST_DATA_ROW
    while r <= ws.max_row:
        vals = [clean(ws.cell(row=r, column=c).value) for c in range(1, width + 1)]
        filled = [v for v in vals if v]
        if not filled:
            r += 1
            continue
        if len(filled) >= 3 and vals[0].startswith("Wk"):
            weeks += 1
            lines += ["## " + " · ".join(p.strip() for p in vals[0].split("\n") if p.strip()), ""]
            for i in range(1, width):
                if vals[i]:
                    lines += ["### " + headers[i], "", vals[i], ""]
        elif len(filled) == 1:
            lines += [filled[0], ""]
        else:
            # A small table below the weeks, such as the hours split: its first row is its header.
            table = [vals]
            r += 1
            while r <= ws.max_row:
                nxt = [clean(ws.cell(row=r, column=c).value) for c in range(1, width + 1)]
                if not any(nxt):
                    break
                table.append(nxt)
                r += 1
            used = max(max(i for i, v in enumerate(row) if v) for row in table) + 1
            lines += md_table(table[0][:used], [row[:used] for row in table[1:]]) + [""]
            continue
        r += 1
    return lines, f"{weeks} weeks"


def export_plan(ws):
    """The 20-Week Plan: prose, then the week grid as a real table, then the notes under it."""
    header_row = next(r for r in range(1, ws.max_row + 1)
                      if clean(ws.cell(row=r, column=1).value) == PLAN_FIRST_HEADER)
    headers = [h for h in headers_of(ws, header_row) if h]
    width = len(headers)
    lines = ["# " + ws.title, ""]
    for r in range(1, header_row):
        text = " ".join(v for v in (clean(ws.cell(row=r, column=c).value)
                                    for c in range(1, ws.max_column + 1)) if v)
        if text:
            lines += [text, ""]
    rows, notes = [], []
    for r in range(header_row + 1, ws.max_row + 1):
        vals = [clean(ws.cell(row=r, column=c).value) for c in range(1, width + 1)]
        if not any(vals):
            continue
        if re.fullmatch(r"\d+", vals[0]) and not notes:
            rows.append(vals)
        else:
            notes.append(vals)
    lines += md_table(headers, rows) + [""]
    for vals in notes:
        # A totals line keeps its numbers beside the column they belong to.
        text = vals[0]
        extra = [f"{headers[i]}: {vals[i]}" for i in range(1, width) if vals[i]]
        lines += [text + (" (" + "; ".join(extra) + ")" if extra else ""), ""]
    return lines, f"{len(rows)} weeks"


def export_papers(ws):
    """The Saturday item bank: blueprint table, minutes per item type, then one table per paper."""
    blueprint_row = next(r for r in range(1, ws.max_row + 1)
                         if clean(ws.cell(row=r, column=1).value) == PAPER_FIRST_HEADER
                         and clean(ws.cell(row=r, column=2).value) != BANK_SECOND_HEADER)
    bank_row = next(r for r in range(1, ws.max_row + 1)
                    if clean(ws.cell(row=r, column=1).value) == PAPER_FIRST_HEADER
                    and clean(ws.cell(row=r, column=2).value) == BANK_SECOND_HEADER)

    lines = ["# " + ws.title, ""]
    for r in range(1, blueprint_row):
        text = clean(ws.cell(row=r, column=1).value)
        if text:
            lines += [text, ""]

    # The blueprint sits in the left block; the minutes-per-item assumptions sit to its right.
    bp_headers = headers_of(ws, blueprint_row)
    right = [i for i, h in enumerate(bp_headers) if h == "Item type"]
    left_width = (right[0] - 1) if right else len(bp_headers)
    left_width = max(i for i, h in enumerate(bp_headers[:left_width]) if h) + 1
    bp_rows, assumptions = [], []
    for r in range(blueprint_row + 1, bank_row):
        vals = [clean(ws.cell(row=r, column=c).value) for c in range(1, ws.max_column + 1)]
        if any(vals[:left_width]):
            bp_rows.append(vals[:left_width])
        if right and vals[right[0]]:
            assumptions.append(vals[right[0]:right[0] + 2])
    lines += ["## Blueprint", ""] + md_table(bp_headers[:left_width], bp_rows) + [""]
    if assumptions:
        lines += ["## Minutes per item type", ""]
        lines += md_table(bp_headers[right[0]:right[0] + 2], assumptions) + [""]

    bank_headers = headers_of(ws, bank_row)
    bank_width = max(i for i, h in enumerate(bank_headers) if h) + 1
    bank_headers = bank_headers[:bank_width]
    papers = {}
    for r in range(bank_row + 1, ws.max_row + 1):
        vals = [clean(ws.cell(row=r, column=c).value) for c in range(1, bank_width + 1)]
        if vals[0]:
            papers.setdefault(vals[0], []).append(vals)
    for paper, rows in papers.items():
        lines += [f"## {paper} paper ({len(rows)} items)", ""]
        lines += md_table(bank_headers[1:], [row[1:] for row in rows]) + [""]
    return lines, f"{sum(len(v) for v in papers.values())} items in {len(papers)} papers"


def export_plain(ws):
    lines = ["# " + ws.title, ""]
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
        vals = [clean(c.value) for c in row]
        if any(vals):
            lines.append(" | ".join(v.replace("\n", " / ") for v in vals if v))
    lines.append("")
    return lines, ""


EXPORTERS = {"days": export_days, "weekly": export_weekly, "plan": export_plan,
             "papers": export_papers, "plain": export_plain}


def export_all(src=SRC):
    """Every export as {file name: text, ...} plus a one-line summary per tab. Writes nothing."""
    if not pathlib.Path(src).exists():
        sys.exit(f"FAIL  {src} not found")
    wb = openpyxl.load_workbook(src, data_only=True)
    files, summary = {}, []
    for ws in wb.worksheets:
        lines, note = EXPORTERS[shape_of(ws)](ws)
        name = file_name(ws.title)
        files[name] = "\n".join(lines)
        summary.append(f"{name}  {note}".rstrip())
    return files, summary


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if out of date")
    ap.add_argument("--source", default=str(SRC), help="the workbook, docs/curriculum/source.xlsx")
    a = ap.parse_args()

    files, summary = export_all(a.source)
    stale_files = []
    for name, text in files.items():
        path = OUT / name
        if path.exists() and path.read_text(encoding="utf-8") == text:
            continue
        stale_files.append(name)
        if not a.check:
            path.write_text(text, encoding="utf-8")
    for line in summary:
        print(("wrote " if not a.check else "      ") + str(OUT / line))

    orphans = sorted(p.name for p in OUT.glob("*.md") if p.name not in files)
    if orphans:
        print("\nThese exports no longer have a tab in the workbook and are now stale:")
        for s in orphans:
            print("   ", s)
        print("Delete them in the same commit, or add the tab back.")
    if a.check and (stale_files or orphans):
        print(f"\nFAIL  {len(stale_files)} export(s) differ from the workbook: {', '.join(stale_files)}"
              if stale_files else "\nFAIL  stale exports on disk")
        sys.exit(1)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 scripts/export_curriculum.py
#     Writes one markdown file per tab into docs/curriculum/: W0 to W16 as day files with six
#     days each, W17_20_Capstone.md with five week headings, 20_Week_Plan.md with a 21-row
#     table, Saturday_papers.md with the blueprint and one table per paper, Structure.md plain.
# python3 scripts/export_curriculum.py --check    (straight after the line above)
#     Prints the same summary and exits 0.
# python3 scripts/export_curriculum.py --check    (after the workbook changes a cell)
#     Names the export that differs and exits 1, writing nothing.
# python3 scripts/export_curriculum.py --source missing.xlsx
#     One FAIL line naming the missing file, exit 1.
# A day tab that has lost its 'Trainer notes' column
#     FAIL naming the tab and the missing column, exit 1, and no file half-written.

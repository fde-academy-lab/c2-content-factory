"""Export every tab of docs/curriculum/source.xlsx to markdown, so a build session reads
curriculum rows as text rather than opening a spreadsheet.

Run from the repository root after any workbook change:

    python3 scripts/export_curriculum.py

A week tab is laid out as a header title in row 1, column names in row 2, a one-line
description of each column in row 3, and one day per row from row 4. The exporter reads the
column names rather than fixed positions, so a column that moves does not silently change the
output. The day heading carries the day and its focus; every other column becomes a section in
the order the workbook puts it, which is why the business scenario leads and the technique
follows it.
"""
import pathlib
import re
import sys

import openpyxl

SRC = pathlib.Path("docs/curriculum/source.xlsx")
OUT = pathlib.Path("docs/curriculum")

DAY_COL = "Day"
FOCUS_COL = "Day focus"
HEADER_ROW = 2
FIRST_DATA_ROW = 4

# Columns every week tab must carry. A tab missing one of these is a workbook error rather than
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


def clean(value):
    return str(value).strip() if value is not None else ""


def is_week_tab(title):
    return bool(re.match(r"^W\d+\b", title.strip()))


def headers_of(ws):
    return [clean(ws.cell(row=HEADER_ROW, column=c).value) for c in range(1, ws.max_column + 1)]


def export_week(ws):
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
    return lines, days


def export_table(ws):
    lines = ["# " + ws.title, ""]
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
        vals = [clean(c.value) for c in row]
        if any(vals):
            lines.append(" | ".join(v.replace("\n", " / ") for v in vals if v))
    lines.append("")
    return lines


def main():
    if not SRC.exists():
        sys.exit(f"FAIL  {SRC} not found")
    wb = openpyxl.load_workbook(SRC, data_only=True)
    kept = set()
    for ws in wb.worksheets:
        name = re.sub(r"[^A-Za-z0-9]+", "_", ws.title).strip("_")
        if is_week_tab(ws.title):
            lines, days = export_week(ws)
            print(f"wrote {OUT / (name + '.md')}  ({days} days)")
        else:
            lines = export_table(ws)
            print(f"wrote {OUT / (name + '.md')}")
        (OUT / (name + ".md")).write_text("\n".join(lines), encoding="utf-8")
        kept.add(name + ".md")

    stale = sorted(p.name for p in OUT.glob("*.md") if p.name not in kept)
    if stale:
        print("\nThese exports no longer have a tab in the workbook and are now stale:")
        for s in stale:
            print("   ", s)
        print("Delete them in the same commit, or add the tab back.")


if __name__ == "__main__":
    main()

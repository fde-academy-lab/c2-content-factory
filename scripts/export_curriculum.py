"""Exports every tab of docs/curriculum/source.xlsx to markdown so Claude Code reads curriculum rows as text.
Run from the repo root after any workbook update: python3 scripts/export_curriculum.py"""
import openpyxl, pathlib, re

SRC = pathlib.Path("docs/curriculum/source.xlsx")
OUT = pathlib.Path("docs/curriculum")

def clean(v):
    return str(v).strip() if v is not None else ""

wb = openpyxl.load_workbook(SRC, data_only=True)
for ws in wb.worksheets:
    name = re.sub(r"[^A-Za-z0-9]+", "_", ws.title).strip("_")
    lines = ["# " + ws.title, ""]
    if ws.title.startswith("W") and "Curriculum" in ws.title or "Build" in ws.title:
        headers = [clean(ws.cell(row=2, column=c).value) for c in range(1, ws.max_column + 1)]
        for r in range(4, ws.max_row + 1):
            day = clean(ws.cell(row=r, column=1).value).replace("\n", " ")
            focus = clean(ws.cell(row=r, column=2).value)
            if not day:
                continue
            lines += ["## " + day + " · " + focus, ""]
            for c in range(3, ws.max_column + 1):
                val = clean(ws.cell(row=r, column=c).value)
                if val:
                    lines += ["### " + headers[c - 1], "", val, ""]
    else:
        for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
            vals = [clean(c.value) for c in row]
            if any(vals):
                lines.append(" | ".join(v.replace("\n", " / ") for v in vals if v))
        lines.append("")
    (OUT / (name + ".md")).write_text("\n".join(lines), encoding="utf-8")
    print("wrote", OUT / (name + ".md"))

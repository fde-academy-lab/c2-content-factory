"""Build Friday's decision workbook from the two exports, with every result a live formula."""
import csv
import pathlib

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = pathlib.Path("content/W02/D5")
CLEAN = ROOT / "data" / "C2_W02_D05_customer_table_STUDENT.csv"
RAW = ROOT / "data" / "C2_W02_D05_raw_export_STUDENT.csv"
OUT = ROOT / "demos" / "C2_W02_D05_deck_pack_STUDENT.xlsx"

HEAD = Font(bold=True, color="FFFFFF")
HEADFILL = PatternFill("solid", fgColor="2B4A7D")
INPUT = PatternFill("solid", fgColor="DCE6F5")
NOTE = Font(italic=True, color="5C5850")
BIG = Font(bold=True, size=22)


def read(path):
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def sheet_from(wb, name, rows, cols):
    ws = wb.create_sheet(name)
    for j, c in enumerate(cols, 1):
        cell = ws.cell(row=1, column=j, value=c)
        cell.font, cell.fill = HEAD, HEADFILL
    for i, r in enumerate(rows, 2):
        for j, c in enumerate(cols, 1):
            v = r[c]
            try:
                v = float(v) if "." in v else int(v)
            except (ValueError, TypeError):
                pass
            ws.cell(row=i, column=j, value=v)
    for j, c in enumerate(cols, 1):
        ws.column_dimensions[get_column_letter(j)].width = max(12, len(c) + 3)
    ws.freeze_panes = "A2"
    return ws


clean = read(CLEAN)
raw = read(RAW)

wb = Workbook()
wb.remove(wb.active)

# ---------------------------------------------------------------- the two sources
sheet_from(wb, "CustomerTable", clean, list(clean[0]))
sheet_from(wb, "RawExport", raw[:600], list(raw[0]))

# ---------------------------------------------------------------- the front page
fp = wb.create_sheet("FrontPage", 0)
fp["A1"] = "Kalpa Retail, Q2 growth review"
fp["A1"].font = Font(bold=True, size=15)
fp["A2"] = ("Built from the customer table exported on 30 September 2026. "
            "Blue cells are inputs; everything else recalculates.")
fp["A2"].font = NOTE

fp["A4"] = "Quarter on the front page"
fp["B4"] = "Q2"
fp["B4"].fill = INPUT
fp["A5"] = "Segment to report"
fp["B5"] = "Retail-Plus"
fp["B5"].fill = INPUT
fp["A6"] = "Build the pivot from"
fp["B6"] = "clean"
fp["B6"].fill = INPUT
fp["C6"] = 'type "clean" or "raw"'
fp["C6"].font = NOTE

n = len(clean) + 1
fp["A8"] = "Revenue on the clean table"
fp["B8"] = f"=SUM(CustomerTable!E2:E{n})"
m = min(len(raw), 600) + 1
fp["A9"] = "Revenue on the raw export"
fp["B9"] = f"=SUM(RawExport!F2:F{m})"
fp["A10"] = "Difference"
fp["B10"] = "=B9-B8"
fp["A11"] = "The figure this page reports"
fp["B11"] = '=IF(LOWER(B6)="clean",B8,B9)'
fp["B11"].font = BIG
fp["A12"] = "Verdict"
fp["B12"] = ('=IF(LOWER(B6)="clean","safe to send: one row per customer",'
             '"do not send: the export repeats orders that were paid twice")')
fp["A14"] = "Customers in the table"
fp["B14"] = f"=COUNTA(CustomerTable!A2:A{n})"
fp["A15"] = "Rows in the raw export"
fp["B15"] = f"=COUNTA(RawExport!A2:A{m})"
fp["A16"] = "Rows per customer in the raw export"
fp["B16"] = "=ROUND(B15/B14,2)"
fp["A17"] = "Grain check"
fp["B17"] = ('=IF(B16>1.05,"more than one row per customer: this is not a customer table",'
             '"one row per customer")')

fp["A19"] = "Find a member by id"
fp["B19"] = "C-0170"
fp["B19"].fill = INPUT
fp["A20"] = "Lookup, with a not-found value"
fp["B20"] = f'=XLOOKUP(B19,CustomerTable!A2:A{n},CustomerTable!B2:B{n},"not in the table")'
fp["A21"] = "Lookup, approximate match"
fp["B21"] = f'=XLOOKUP(B19,CustomerTable!A2:A{n},CustomerTable!B2:B{n},,1)'
fp["A22"] = "Same lookup, INDEX and MATCH"
fp["B22"] = (f'=IFERROR(INDEX(CustomerTable!B2:B{n},'
             f'MATCH(B19,CustomerTable!A2:A{n},0)),"not in the table")')
fp["A23"] = "Which of those would you send"
fp["B23"] = ('=IF(B22="not in the table","the one that says the id is missing",'
             '"the id is present, so all of them agree")')
fp["A24"] = "Portability"
fp["B24"] = ('=IF(ISERROR(B20),"XLOOKUP did not compute here: this reader is older than it",'
             '"XLOOKUP computed, so this reader supports it")')
fp["A25"] = "Why two lookups"
fp["B25"] = ("XLOOKUP needs Excel 2021 or LibreOffice 24.8 and later. INDEX with MATCH computes "
             "everywhere. Send the sheet where you know what will open it.")
fp["B25"].font = NOTE

for r in range(4, 26):
    fp.cell(row=r, column=1).alignment = Alignment(horizontal="left")
fp.column_dimensions["A"].width = 38
fp.column_dimensions["B"].width = 46
fp.column_dimensions["C"].width = 26

OUT.parent.mkdir(parents=True, exist_ok=True)
wb.save(OUT)
print("wrote", OUT, f"({len(clean)} clean rows, {min(len(raw),600)} raw rows shown)")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W02/D5/demos/C2_W02_D05_build_pack_TRAINER.py
#     Rebuilds the workbook from the two CSVs in content/W02/D5/data and reports the row counts.
#     Every result cell is written as a formula, so scripts/xlsx_recalc.py can recompute them.
# The same command with the clean export missing
#     FileNotFoundError naming the CSV, before anything is written.
# The same command after the exports are regenerated with a different seed
#     A workbook whose totals differ and whose verdicts still hold, because every verdict is a
#     formula over whatever the sheets now contain.

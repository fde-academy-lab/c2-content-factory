"""Build Monday's decision workbook: four taught decisions, each a tab ending in a spoken verdict.

Run from the repository root:  python3 content/W01/D1/demos/C2_W01_D01_build_decision_tool_TRAINER.py

Each tab carries one planted formula defect that its own check line exposes, and the Export tab
releases the paste-ready brief only when all four are fixed, so fixing one thing does not clear
the release. The status totals come from the day's order file; every result is a live formula,
which scripts/xlsx_recalc.py proves by recalculating through LibreOffice and flipping each fix.
"""
import pathlib

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = pathlib.Path("content/W01/D1")
DATA = ROOT / "data" / "C2_W01_D01_orders_STUDENT.py"
OUT = ROOT / "demos" / "C2_W01_D01_decision_tool_STUDENT.xlsx"

INK, MUTED, VIOLET = "1A0F5C", "6B6690", "5B3FD6"
HEAD = Font(bold=True, color="FFFFFF")
HEADFILL = PatternFill("solid", fgColor=INK)
INPUT = PatternFill("solid", fgColor="FFF4C2")
TINT = PatternFill("solid", fgColor="EEEAFB")
TITLE = Font(name="Georgia", size=16, color=INK)
NOTE = Font(italic=True, color=MUTED)
BOLD = Font(bold=True, color=INK)
VERDICT = Font(bold=True, size=12, color=INK)
EDGE = Border(*[Side(style="thin", color="CFC9EE")] * 4)
WRAP = Alignment(wrap_text=True, vertical="top")


def orders():
    scope = {}
    exec(compile(DATA.read_text(encoding="utf-8"), str(DATA), "exec"), scope)
    return scope["ORDERS"]


def rs(ref):
    """An Excel formula that prints a cell as rupees with Indian grouping, up to 99,99,999."""
    r = f"ROUND({ref},0)"
    return (f'"Rs "&IF({r}>=100000,INT({r}/100000)&","&TEXT(INT(MOD({r},100000)/1000),"00")&","&'
            f'TEXT(MOD({r},1000),"000"),IF({r}>=1000,INT({r}/1000)&","&TEXT(MOD({r},1000),"000"),{r}&""))')


def sheet(wb, name, title, lede):
    ws = wb.create_sheet(name)
    ws["A1"] = title
    ws["A1"].font = TITLE
    ws["A2"] = lede
    ws["A2"].font = NOTE
    ws.column_dimensions["A"].width = 34
    ws.column_dimensions["B"].width = 40
    ws.column_dimensions["C"].width = 16
    ws.column_dimensions["D"].width = 60
    return ws


def head(ws, row, labels, col=1):
    for j, text in enumerate(labels):
        c = ws.cell(row=row, column=col + j, value=text)
        c.font, c.fill = HEAD, HEADFILL


def put(ws, ref, value, font=None, fill=None, wrap=False):
    ws[ref] = value
    if font:
        ws[ref].font = font
    if fill:
        ws[ref].fill = fill
        ws[ref].border = EDGE
    if wrap:
        ws[ref].alignment = WRAP


def choice(ws, ref, options):
    dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=False)
    ws.add_data_validation(dv)
    dv.add(ws[ref])


rows = orders()
status = {}
for o in rows:
    n, v = status.get(o["status"], (0, 0))
    status[o["status"]] = (n + 1, v + int(o["amount"]))

wb = Workbook()
start = wb.active
start.title = "Start"
start["A1"] = "The question before the budget: the decision tool"
start["A1"].font = TITLE
start.column_dimensions["A"].width = 110
lines = [
    "Kalpa Retail, Week 1, Monday. Four decisions the day taught, one tab each, and an Export tab that assembles the brief.",
    "Yellow cells are inputs; every other number and sentence is a live formula.",
    "Each tab carries one planted defect in one formula. Read the tab's check line first, find the cell, fix it, and watch the verdict change.",
    "The Export tab releases the paste-ready brief only when all four tabs pass their checks, so fixing one tab does not clear it.",
    "Sales: which total is sales. Tree: do the branch moves reach the plan. Average: mean or median. Discount: does the discount pay.",
    "The status totals on the Sales tab come from the day's thirty orders; every other number here is an input you can change.",
]
for i, text in enumerate(lines, 3):
    start.cell(row=i, column=1, value=text).alignment = WRAP

# ---------------------------------------------------------------- Sales
ws = sheet(wb, "Sales", "Which total is sales?",
           "Three honest readings of one word. The parts must add back to the whole before any total leaves the team.")
head(ws, 4, ["Status", "Orders", "Amount (Rs)"])
for i, s in enumerate(["delivered", "returned", "cancelled"], 5):
    ws.cell(row=i, column=1, value=s)
    ws.cell(row=i, column=2, value=status[s][0])
    ws.cell(row=i, column=3, value=status[s][1])
head(ws, 9, ["Reading", "Definition", "Total (Rs)"])
put(ws, "A10", "booked"); put(ws, "B10", "all booked orders"); put(ws, "C10", "=C5+C6")
put(ws, "A11", "not cancelled"); put(ws, "B11", "every order not cancelled"); put(ws, "C11", "=C5+C6")
put(ws, "A12", "delivered"); put(ws, "B12", "delivered orders only"); put(ws, "C12", "=C5")
put(ws, "A14", "Your reading", BOLD); put(ws, "B14", "booked", fill=INPUT)
choice(ws, "B14", ["booked", "not cancelled", "delivered"])
put(ws, "A15", "The check", BOLD)
put(ws, "B15", '=IF(C10=C5+C6+C7,"The parts add up to the booked total.",'
               '"The parts do not add up to the booked total: one total leaves a row out. Fix it first.")',
    wrap=True)
put(ws, "A16", "Chosen total"); put(ws, "B16", "=INDEX(C10:C12,MATCH(B14,A10:A12,0))")
put(ws, "A17", "Its definition"); put(ws, "B17", "=INDEX(B10:B12,MATCH(B14,A10:A12,0))")
put(ws, "A19", "Verdict", VERDICT)
put(ws, "B19", '=IF(C10<>C5+C6+C7,"Fix the total that leaves a row out before any number leaves the team.",'
               f'"Revenue, "&B17&", 1 July to 26 September: "&{rs("B16")}&".")', VERDICT, TINT, True)
put(ws, "A20", "Fixed, for the Export tab", NOTE); put(ws, "B20", "=IF(C10=C5+C6+C7,1,0)")

# ---------------------------------------------------------------- Tree
ws = sheet(wb, "Tree", "Do the branch moves reach the plan?",
           "Change each branch in percent. The tree multiplies its branches, and the extra discount comes off the top.")
head(ws, 4, ["Branch", "Change, percent", "Multiplier"])
branches = [("customers", 10), ("orders per customer", 5), ("items per order", 0), ("price per item", 0)]
for i, (b, v) in enumerate(branches, 5):
    ws.cell(row=i, column=1, value=b)
    put(ws, f"B{i}", v, fill=INPUT)
    put(ws, f"C{i}", f"=1+B{i}/100")
put(ws, "A9", "extra discount, percent of gross"); put(ws, "B9", 0, fill=INPUT); put(ws, "C9", "=1-B9/100")
put(ws, "A11", "Revenue index, today at 100", BOLD); put(ws, "B11", "=100+B5+B6+B7+B8-B9")
put(ws, "A12", "The product of the multipliers"); put(ws, "B12", "=100*C5*C6*C7*C8*C9")
put(ws, "A13", "The check", BOLD)
put(ws, "B13", '=IF(ABS(B11-B12)<0.05,"The index multiplies the branches, as the tree does.",'
               '"The index and the product of the branches disagree: one formula adds what the tree multiplies. '
               'Fix it first.")', wrap=True)
put(ws, "A14", "The plan"); put(ws, "B14", 115, fill=INPUT)
put(ws, "A16", "Verdict", VERDICT)
put(ws, "B16", '=IF(ABS(B11-B12)>=0.05,"Fix the index that adds what the tree multiplies before reading any result.",'
               'IF(B11>=B14,"The moves reach the plan: revenue index "&TEXT(B11,"0.0")&" against "&B14&".",'
               '"The moves fall short: revenue index "&TEXT(B11,"0.0")&", "&TEXT(B14-B11,"0.0")&" points under the plan."))',
    VERDICT, TINT, True)
put(ws, "A17", "Fixed, for the Export tab", NOTE); put(ws, "B17", "=IF(ABS(B11-B12)<0.05,1,0)")

# ---------------------------------------------------------------- Average
ws = sheet(wb, "Average", "Mean or median?",
           "Five invented orders in the yellow cells, room for five more. The job the number does decides the average.")
head(ws, 4, ["Amounts (Rs)"])
for i, v in enumerate([1900, 2100, 2200, 2400, 90000, None, None, None, None, None], 5):
    put(ws, f"A{i}", v, fill=INPUT)
put(ws, "C5", "Count"); put(ws, "D5", "=COUNT(A5:A14)")
put(ws, "C6", "Mean"); put(ws, "D6", "=AVERAGE(A5:A14)")
put(ws, "C7", "Median"); put(ws, "D7", "=AVERAGE(A5:A14)")
put(ws, "C8", "Mean over median"); put(ws, "D8", "=D6/D7")
put(ws, "C9", "The check", BOLD)
put(ws, "D9", '=IF(AND(D7=D6,MAX(A5:A14)>5*MIN(A5:A14)),"The median equals the mean on a list whose largest value '
              'is many times its smallest: check the median formula. Fix it first.",'
              '"The median is the middle of the sorted list.")', wrap=True)
put(ws, "C11", "What is the number for?", BOLD); put(ws, "D11", "a typical order", fill=INPUT)
choice(ws, "D11", ["a typical order", "a total that must add up", "a first look at a file"])
put(ws, "C13", "Verdict", VERDICT)
put(ws, "D13", '=IF(AND(D7=D6,MAX(A5:A14)>5*MIN(A5:A14)),"Fix the median formula before choosing an average.",'
               f'IF(D11="a typical order","Report the median, "&{rs("D7")}&", as the typical order, and name the '
               'largest order on its own line.",'
               f'IF(D11="a total that must add up","Use the mean, "&{rs("D6")}&", because it multiplies back to the '
               'total.",'
               f'"Report both: the mean "&{rs("D6")}&" and the median "&{rs("D7")}&"; a gap of "&TEXT(D8,"0.0")&'
               '" times is itself a finding.")))', VERDICT, TINT, True)
put(ws, "C14", "Fixed, for the Export tab", NOTE); put(ws, "D14", "=IF(D7=MEDIAN(A5:A14),1,0)")

# ---------------------------------------------------------------- Discount
ws = sheet(wb, "Discount", "Does the discount pay?",
           "A discount trades margin for quantity. It pays only when volume rises by more than the price falls.")
head(ws, 4, ["Input", "Value"])
put(ws, "A5", "Discount, percent off"); put(ws, "B5", 15, fill=INPUT)
put(ws, "A6", "Expected volume lift, percent"); put(ws, "B6", 10, fill=INPUT)
put(ws, "A8", "Revenue multiple against today", BOLD); put(ws, "B8", "=(1+B6/100)*(1-B5/100)")
put(ws, "A9", "Break-even volume lift, percent"); put(ws, "B9", "=B5")
put(ws, "A10", "The check", BOLD)
put(ws, "B10", '=IF(ABS((1+B9/100)*(1-B5/100)-1)<0.0005,"At the break-even lift the discount leaves revenue where '
               'it was.","At the stated break-even lift revenue still falls: the break-even formula is wrong. Fix it '
               'first.")', wrap=True)
put(ws, "A12", "Verdict", VERDICT)
put(ws, "B12", '=IF(ABS((1+B9/100)*(1-B5/100)-1)>=0.0005,"Fix the break-even formula before judging the discount.",'
               'IF(B8>=1,"The discount pays: revenue ends at "&TEXT(B8,"0.000")&" of today.",'
               '"The discount loses: revenue ends at "&TEXT(B8,"0.000")&" of today, and it needs "&TEXT(B9,"0.0")&'
               '" percent more volume just to stand still."))', VERDICT, TINT, True)
put(ws, "A13", "Fixed, for the Export tab", NOTE)
put(ws, "B13", "=IF(ABS((1+B9/100)*(1-B5/100)-1)<0.0005,1,0)")

# ---------------------------------------------------------------- Export
ws = sheet(wb, "Export", "The brief, assembled",
           "Released only when every tab's check passes. Paste the brief into the note to Meera.")
ws.column_dimensions["B"].width = 110
put(ws, "A4", "Tabs fixed", BOLD); put(ws, "B4", "=Sales!B20+Tree!B17+Average!D14+Discount!B13")
put(ws, "A5", "Release", VERDICT)
put(ws, "B5", '=IF(B4=4,"Ready to paste into the note to Meera.","Not ready: "&(4-B4)&" of the four tabs still '
              'carry a defect to fix first.")', VERDICT, TINT, True)
put(ws, "A7", "Paste-ready brief", BOLD)
put(ws, "B7", '=IF(B4=4,"Sales: "&Sales!B19&CHAR(10)&"Tree: "&Tree!B16&CHAR(10)&"Average: "&Average!D13&CHAR(10)&'
              '"Discount: "&Discount!B12,"The brief assembles once every tab passes its check.")', wrap=True)
ws.row_dimensions[7].height = 90

wb.save(OUT)
print(f"wrote {OUT}")

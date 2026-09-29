"""Build Thursday's decision workbook: four taught decisions, each a tab ending in a spoken verdict.

Run from the repository root:  python3 content/W01/D4/demos/C2_W01_D04_build_decision_tool_TRAINER.py

Each tab carries one planted formula defect that its own check line exposes, and the Export tab
releases the paste-ready brief only when all four are fixed, so fixing one thing does not clear
the release. Every number is an invented input the learner can change; every result is a live
formula, which scripts/xlsx_recalc.py proves by recalculating through LibreOffice and flipping
each fix.
"""
import pathlib

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = pathlib.Path("content/W01/D4")
OUT = ROOT / "demos" / "C2_W01_D04_decision_tool_STUDENT.xlsx"

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


wb = Workbook()
start = wb.active
start.title = "Start"
start["A1"] = "Before the growth review: the decision tool"
start["A1"].font = TITLE
start.column_dimensions["A"].width = 110
lines = [
    "Kalpa Retail, Week 1, Thursday. Meera asks three things before Monday's growth review: is the Retail-Plus "
    "drop real or the usual wobble, should budget follow a segment that is up 40 percent, and did the monsoon "
    "discount work. Four decisions answer her, one tab each, and an Export tab assembles the note.",
    "Yellow cells are inputs; every other number and sentence is a live formula. Every number here is invented, "
    "so change it and watch the verdict move.",
    "Each tab carries one planted defect in one formula. Read the tab's check line first, find the cell, fix it, "
    "and watch the verdict change.",
    "The Export tab releases the paste-ready note only when all four tabs pass their checks, so fixing one tab "
    "does not clear it.",
    "Share: what a p-value says. Size: whether a real gap is worth acting on. Count: whether a rate is a finding "
    "or a lead. Mix: whether the campaign worked once the segments are split.",
    "The note to Meera runs claim, evidence, caveat, action, and each verdict is written to sit inside it.",
]
for i, text in enumerate(lines, 3):
    start.cell(row=i, column=1, value=text).alignment = WRAP

# ---------------------------------------------------------------- Share
ws = sheet(wb, "Share", "What does the share say?",
           "Shuffle the segment labels many times and count how often chance alone makes a gap this large. "
           "The numbers are invented, change them.")
head(ws, 4, ["Input", "Value"])
put(ws, "A5", "Shuffles run"); put(ws, "B5", 5000, fill=INPUT)
put(ws, "A6", "Shuffles at least as large as the real gap"); put(ws, "B6", 210, fill=INPUT)
put(ws, "A8", "The share (the p-value)", BOLD); put(ws, "B8", "=B6/1000")
put(ws, "A9", "The check", BOLD)
put(ws, "B9", '=IF(AND(B8>=0,B8<=1,ABS(B8-B6/B5)<0.0000001),"The share is the count at least as large, over '
              'the shuffles run.","The share is outside 0 to 1 or differs from the count over the shuffles: it '
              'divides by the wrong cell. Fix it first.")', wrap=True)
put(ws, "A11", "The sentence you would write", BOLD)
put(ws, "B11", "a X percent chance we are wrong", fill=INPUT)
choice(ws, "B11", ["a X percent chance we are wrong", "X of every 100 chance-only worlds", "X percent certain"])
put(ws, "A12", "Is it defensible?")
put(ws, "B12", '=IF(B11="X of every 100 chance-only worlds","Defensible: the share counts chance-only worlds, '
               'which is all a p-value measures.","Indefensible: a p-value is a share of chance-only worlds, '
               'never the chance the finding is wrong. Choose the chance-only worlds sentence.")', wrap=True)
put(ws, "A14", "Verdict", VERDICT)
put(ws, "B14", '=IF(ABS(B8-B6/B5)>=0.0000001,"Fix the share formula before reading the verdict.",'
               'IF(B8<0.05,"Chance makes a gap this large in about "&TEXT(B8*100,"0.0")&" of every 100 shuffles, '
               'so treat it as real and size it next.","Chance makes a gap this large in about "&TEXT(B8*100,"0.0")&'
               '" of every 100 shuffles: inside the usual wobble, so not yet."))', VERDICT, TINT, True)
put(ws, "A15", "Fixed, for the Export tab", NOTE); put(ws, "B15", "=IF(ABS(B8-B6/B5)<0.0000001,1,0)")

# ---------------------------------------------------------------- Size
ws = sheet(wb, "Size", "Is it worth acting on?",
           "Real and worth acting on are two separate calls. Size the fall in rupees against the cost of the fix. "
           "The numbers are invented, change them.")
head(ws, 4, ["Input", "Value"])
put(ws, "A5", "Gap per member in the quarter (Rs)"); put(ws, "B5", 160, fill=INPUT)
put(ws, "A6", "Members in the segment"); put(ws, "B6", 7000, fill=INPUT)
put(ws, "A7", "Company revenue in the quarter (Rs)"); put(ws, "B7", 95000000, fill=INPUT)
put(ws, "A8", "Cost of acting per quarter (Rs)"); put(ws, "B8", 250000, fill=INPUT)
put(ws, "A9", "Share of the fall the fix wins back, percent"); put(ws, "B9", 30, fill=INPUT)
put(ws, "A11", "Segment fall in the quarter (Rs)", BOLD); put(ws, "B11", "=B5/B6")
put(ws, "A12", "Share of company revenue, percent"); put(ws, "B12", "=100*B11/B7")
put(ws, "A13", "Net after the fix (Rs)"); put(ws, "B13", "=B11*B9/100-B8")
put(ws, "A14", "Break-even win-back, percent"); put(ws, "B14", "=100*B8/B11")
put(ws, "A15", "The check", BOLD)
put(ws, "B15", '=IF(ABS(B11/B6-B5)<0.005,"The fall spread over the members gives back the gap per member.",'
               '"The fall spread over the members does not give back the gap per member: the fall formula divides '
               'where it should multiply. Fix it first.")', wrap=True)
put(ws, "A17", "Verdict", VERDICT)
put(ws, "B17", '=IF(ABS(B11/B6-B5)>=0.005,"Fix the segment fall formula before sizing the fix.",'
               f'"The fall is "&{rs("B11")}&" a quarter, "&TEXT(B12,"0.0")&" percent of company revenue, and the fix '
               'breaks even when it wins back "&TEXT(B14,"0.0")&" percent of it. "&'
               f'IF(B13>=0,"At "&B9&" percent it pays, netting "&{rs("B13")}&" a quarter.",'
               f'"At "&B9&" percent it loses "&{rs("ABS(B13)")}&" a quarter, so it waits for a cheaper fix."))',
    VERDICT, TINT, True)
put(ws, "A18", "Fixed, for the Export tab", NOTE); put(ws, "B18", "=IF(ABS(B11/B6-B5)<0.005,1,0)")

# ---------------------------------------------------------------- Count
ws = sheet(wb, "Count", "Is the rate a finding or a lead?",
           "A rate that jumps by 40 percent can stand on a handful of orders. Count what it stands on first. "
           "The numbers are invented, change them.")
head(ws, 4, ["Input", "Value"])
put(ws, "A5", "Orders in the earlier quarter"); put(ws, "B5", 8, fill=INPUT)
put(ws, "A6", "Orders in the later quarter"); put(ws, "B6", 14, fill=INPUT)
put(ws, "A8", "Rate change, percent", BOLD); put(ws, "B8", "=100*(B6-B5)/B5")
put(ws, "A9", "Orders the rate stands on"); put(ws, "B9", "=B5+B6")
put(ws, "A10", "One-order swing, points"); put(ws, "B10", "=100/B9")
put(ws, "A11", "The call"); put(ws, "B11", '=IF(B8<30,"lead","finding")')
put(ws, "A12", "The check", BOLD)
put(ws, "B12", '=IF(B11=IF(B9<30,"lead","finding"),"The call reads the count of orders against thirty.",'
               '"The call and the count disagree: the threshold test reads the rate where it should read the count. '
               'Fix it first.")', wrap=True)
put(ws, "A14", "Verdict", VERDICT)
put(ws, "B14", '=IF(B11<>IF(B9<30,"lead","finding"),"Fix the threshold test before calling the rate.",'
               'IF(B9<30,"A rise of "&TEXT(B8,"0.0")&" percent on "&B9&" orders is a lead: watch it until it carries '
               'thirty or more. One order moves it by about "&TEXT(B10,"0.0")&" points.",'
               '"A rise of "&TEXT(B8,"0.0")&" percent on "&B9&" orders is a finding worth testing."))',
    VERDICT, TINT, True)
put(ws, "A15", "Fixed, for the Export tab", NOTE); put(ws, "B15", '=IF(B11=IF(B9<30,"lead","finding"),1,0)')

# ---------------------------------------------------------------- Mix
ws = sheet(wb, "Mix", "Did the campaign work?",
           "Split the aggregate by segment before crediting a campaign. Two invented groups, spend per customer "
           "in the quarter; change them.")
head(ws, 4, ["Segment", "Not exposed (Rs)", "Exposed (Rs)", "Change (Rs)"])
put(ws, "A5", "big spenders"); put(ws, "B5", 5000, fill=INPUT); put(ws, "C5", 4700, fill=INPUT)
put(ws, "D5", "=C5-B5")
put(ws, "A6", "small spenders"); put(ws, "B6", 900, fill=INPUT); put(ws, "C6", 850, fill=INPUT)
put(ws, "D6", "=C6-B6")
put(ws, "A8", "Big spenders in the not-exposed group, percent"); put(ws, "B8", 25, fill=INPUT)
put(ws, "A9", "Big spenders in the exposed group, percent"); put(ws, "B9", 50, fill=INPUT)
put(ws, "A11", "Blended, not exposed (Rs)", BOLD); put(ws, "B11", "=B8/100*B5+(1-B8/100)*B6")
put(ws, "A12", "Blended, exposed (Rs)", BOLD); put(ws, "B12", "=B9/100*C5+(1-B9/100)*C6")
put(ws, "A13", "Blended change (Rs)"); put(ws, "B13", "=B12-B11")
put(ws, "A14", "Same-mix blend, exposed at the not-exposed mix (Rs)"); put(ws, "B14", "=B9/100*C5+(1-B9/100)*C6")
put(ws, "A15", "Same-mix change (Rs)"); put(ws, "B15", "=B14-B11")
put(ws, "A16", "The check", BOLD)
put(ws, "B16", '=IF(OR(AND(D5<0,D6<0,B15>=0),AND(D5>0,D6>0,B15<=0)),"The same-mix change has a different sign '
               'from every segment\'s change: the same-mix blend uses the wrong group\'s mix. Fix it first.",'
               '"The same-mix change moves with the segments, as a like-for-like comparison must.")', wrap=True)
put(ws, "A18", "Verdict", VERDICT)
put(ws, "B18", '=IF(OR(AND(D5<0,D6<0,B15>=0),AND(D5>0,D6>0,B15<=0)),"Fix the same-mix blend before crediting '
               'the campaign.",IF(AND(D5<0,D6<0,B13>0),"Every group spent less with the campaign; the blend rose '
               'only because the exposed group held more big spenders. Do not repeat it as designed; test it '
               'against a held-back group.",IF(AND(D5>0,D6>0),"Every group spent more with the campaign, "&'
               f'{rs("B15")}&" a customer at the same mix: credit it and size it next.",'
               f'"The groups moved apart, so report the same-mix change of "&IF(B15<0,"minus ","")&{rs("ABS(B15)")}&'
               '" a customer with the split beside it.")))', VERDICT, TINT, True)
put(ws, "A19", "Fixed, for the Export tab", NOTE)
put(ws, "B19", "=IF(ABS(B14-(B8/100*C5+(1-B8/100)*C6))<0.005,1,0)")

# ---------------------------------------------------------------- Export
ws = sheet(wb, "Export", "The note, assembled",
           "Released only when every tab's check passes. Paste the lines into the note to Meera as claim, "
           "evidence, caveat and action.")
ws.column_dimensions["B"].width = 110
put(ws, "A4", "Tabs fixed", BOLD); put(ws, "B4", "=Share!B15+Size!B18+Count!B15+Mix!B19")
put(ws, "A5", "Release", VERDICT)
put(ws, "B5", '=IF(B4=4,"Ready to paste into the note to Meera.","Not ready: "&(4-B4)&" of the four tabs still '
              'carry a defect to fix first.")', VERDICT, TINT, True)
put(ws, "A7", "Paste-ready note", BOLD)
put(ws, "B7", '=IF(B4=4,"Share: "&Share!B14&CHAR(10)&"Size: "&Size!B17&CHAR(10)&"Count: "&Count!B14&CHAR(10)&'
              '"Mix: "&Mix!B18,"The note assembles once every tab passes its check.")', wrap=True)
ws.row_dimensions[7].height = 120

wb.save(OUT)
print(f"wrote {OUT}")

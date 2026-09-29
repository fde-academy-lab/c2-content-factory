"""Build Friday's decision tool: five last-mile decisions, each a tab ending in a spoken verdict.

Run from the repository root:  python3 content/W02/D5/demos/C2_W02_D05_build_decision_tool_TRAINER.py

The tool holds a framework a learner applies to their own sheets, so four tabs run on inputs and on
invented records, and only the Pivot tab's default inputs are the day's numbers. Each tab carries
one planted formula defect that its own check line exposes, and the Export tab releases the
paste-ready rule only when all five are fixed, so fixing the first cell a learner notices does not
clear the release. scripts/xlsx_recalc.py proves every verdict by recalculating through LibreOffice
and applying each fix.

Formulas stay inside what LibreOffice 24.2 computes: INDEX and MATCH, SUBTOTAL, IF, OR, AND, TEXT,
ROUND, ABS, IFERROR. XLOOKUP is taught in the room and never used here.
"""
import pathlib

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

OUT = pathlib.Path("content/W02/D5/demos/C2_W02_D05_decision_tool_STUDENT.xlsx")

INK, MUTED = "1A0F5C", "6B6690"
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
INDIAN = '[>=10000000]##\\,##\\,##\\,##0;[>=100000]##\\,##\\,##0;##,##0'


def rs(ref):
    r = f"ROUND({ref},0)"
    return (f'"Rs "&IF({r}>=100000,INT({r}/100000)&","&TEXT(INT(MOD({r},100000)/1000),"00")&","&'
            f'TEXT(MOD({r},1000),"000"),IF({r}>=1000,INT({r}/1000)&","&TEXT(MOD({r},1000),"000"),{r}&""))')


def crl(ref):
    return (f'IF(ABS({ref})>=10000000,"Rs "&TEXT(ABS({ref})/10000000,"0.00")&" crore",'
            f'IF(ABS({ref})>=100000,"Rs "&TEXT(ABS({ref})/100000,"0.00")&" lakh",{rs(f"ABS({ref})")}))')


def sheet(wb, name, title, lede):
    ws = wb.create_sheet(name)
    ws["A1"], ws["A1"].font = title, TITLE
    ws["A2"], ws["A2"].font = lede, NOTE
    ws.column_dimensions["A"].width = 46
    ws.column_dimensions["B"].width = 70
    ws.column_dimensions["C"].width = 16
    return ws


def head(ws, row, labels, col=1):
    for j, text in enumerate(labels):
        c = ws.cell(row=row, column=col + j, value=text)
        c.font, c.fill = HEAD, HEADFILL


def put(ws, ref, value, font=None, fill=None, wrap=False, fmt=None):
    ws[ref] = value
    if font:
        ws[ref].font = font
    if fill:
        ws[ref].fill = fill
        ws[ref].border = EDGE
    if wrap:
        ws[ref].alignment = WRAP
    if fmt:
        ws[ref].number_format = fmt


def choice(ws, ref, options):
    dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=False)
    ws.add_data_validation(dv)
    dv.add(ws[ref])


wb = Workbook()
start = wb.active
start.title = "Start"
start["A1"], start["A1"].font = "The last mile: the decision tool", TITLE
start.column_dimensions["A"].width = 112
for i, text in enumerate([
    "Kalpa Retail, Week 2, Friday. Five decisions an analyst makes before a sheet reaches a leadership deck, one tab "
    "each, and an Export tab that writes the team's operating rule.",
    "Yellow cells are inputs; every other number and sentence is a live formula.",
    "Each tab carries one planted defect in one formula. Read the tab's check line, find the cell, fix it, and watch "
    "the verdict change.",
    "The Export tab releases the rule only when all five tabs pass their checks, so fixing one tab does not clear it.",
    "Pivot: may this pivot be sliced live. Lookup: what does the lookup answer for a missing id. Visible total: what "
    "does the foot of a filtered list add. Front page: is the card ready. Rule: which tool owns this number.",
    "The Pivot tab starts from Friday's raw export. The Lookup and Visible total tabs run on invented records, "
    "labelled so, and the Front page and Rule tabs take whatever you type.",
], 3):
    start.cell(row=i, column=1, value=text).alignment = WRAP

# ---------------------------------------------------------------- Pivot
ws = sheet(wb, "Pivot", "May this pivot be sliced live?",
           "A pivot is only as honest as the rows under it. It reaches the room only when it reconciles to the warehouse.")
head(ws, 4, ["Input", "Value"])
put(ws, "A5", "Rows in the export the pivot sits on"); put(ws, "B5", 1450, fill=INPUT)
put(ws, "A6", "Distinct order ids in those rows"); put(ws, "B6", 1000, fill=INPUT)
put(ws, "A7", "The pivot's grand total (Rs)"); put(ws, "B7", 394095490, fill=INPUT, fmt=INDIAN)
put(ws, "A8", "The warehouse total for the same period (Rs)"); put(ws, "B8", 198400000, fill=INPUT, fmt=INDIAN)
put(ws, "A10", "Rows per order"); put(ws, "B10", "=B5/B6", fmt="0.00")
put(ws, "A11", "The pivot less the warehouse (Rs)"); put(ws, "B11", "=B7-B7", fmt=INDIAN)
put(ws, "A12", "The check", BOLD, wrap=True)
put(ws, "B12", '=IF(B11<>B7-B8,"The difference reads "&B11&" while the pivot and the warehouse disagree: the formula '
               'compares the pivot with itself. Fix it first.","The difference compares the pivot with the '
               'warehouse.")', wrap=True)
put(ws, "A14", "Verdict", VERDICT, wrap=True)
put(ws, "B14", '=IF(B11<>B7-B8,"Fix the difference formula before trusting the pivot.",IF(ABS(B11)<1,'
               '"Slice it live: the pivot reconciles to the warehouse.",IF(B10>1,"Do not slice this pivot: it is "&'
               + crl("B11") + '&" off the warehouse and carries "&TEXT(B10,"0.00")&" rows per order. Rebuild it on '
               'one row per order.","Do not slice this pivot: it is "&' + crl("B11") + '&" off the warehouse with one '
               'row per order, so orders are missing or extra. Find them first.")))', VERDICT, TINT, True)
put(ws, "A15", "Fixed, for the Export tab", NOTE); put(ws, "B15", "=IF(B11=B7-B8,1,0)")
ws.row_dimensions[12].height = 32; ws.row_dimensions[14].height = 36

# ---------------------------------------------------------------- Lookup
ws = sheet(wb, "Lookup", "What does the lookup answer for a missing id?",
           "Eight invented members, sorted by id. A lookup that cannot find an id must say so, never hand back a neighbour.")
ws.column_dimensions["D"].width = 36
ws.column_dimensions["E"].width = 70
head(ws, 4, ["Member id (invented)", "Revenue (Rs)"])
for i, (mid, rev) in enumerate([("C-0401", 12400), ("C-0402", 9870), ("C-0403", 9120), ("C-0404", 8760),
                                 ("C-0406", 8410), ("C-0407", 7990), ("C-0408", 7650), ("C-0409", 7300)], 5):
    ws.cell(row=i, column=1, value=mid)
    ws.cell(row=i, column=2, value=rev).number_format = INDIAN
put(ws, "D5", "Member id to find", BOLD); put(ws, "E5", "C-0405", fill=INPUT)
put(ws, "D7", "Row returned"); put(ws, "E7", "=INDEX(A5:A12,MATCH(E5,A5:A12,1))")
put(ws, "D8", "Revenue on that row (Rs)")
put(ws, "E8", '=IF(E7="not in the table","",INDEX(B5:B12,MATCH(E7,A5:A12,0)))', fmt=INDIAN)
put(ws, "D9", "The check", BOLD, wrap=True)
put(ws, "E9", '=IF(E7=E5,"The row returned is the member asked for.",IF(E7="not in the table",'
              '"The lookup says the id is missing.","The lookup returned "&E7&" for "&E5&": the match type answers '
              'with a neighbour. Fix it first."))', wrap=True)
put(ws, "D11", "Verdict", VERDICT, wrap=True)
put(ws, "E11", '=IF(AND(E7<>E5,E7<>"not in the table"),"Fix the match type before answering the chief of staff.",'
               'IF(E7="not in the table",E5&" is not in the table: say so, and check the export before anyone '
               'answers.",E5&": "&' + rs("E8") + '&", on the list."))', VERDICT, TINT, True)
put(ws, "D12", "Fixed, for the Export tab", NOTE); put(ws, "E12", '=IF(OR(E7=E5,E7="not in the table"),1,0)')
ws.row_dimensions[9].height = 32; ws.row_dimensions[11].height = 32

# ---------------------------------------------------------------- Visible total
ws = sheet(wb, "Visible total", "What does the foot of a filtered list add?",
           "Eight invented members, filtered to one city. The foot of a filtered list must add only the rows a director "
           "can see.")
ws.column_dimensions["C"].width = 16
head(ws, 4, ["Member id (invented)", "City", "Revenue (Rs)"])
members = [("C-0501", "Delhi", 11000), ("C-0502", "Mumbai", 9200), ("C-0503", "Pune", 8000),
           ("C-0504", "Mumbai", 8400), ("C-0505", "Delhi", 6000), ("C-0506", "Mumbai", 7900),
           ("C-0507", "Chennai", 5500), ("C-0508", "Pune", 4000)]
for i, (mid, city, rev) in enumerate(members, 5):
    ws.cell(row=i, column=1, value=mid)
    ws.cell(row=i, column=2, value=city)
    ws.cell(row=i, column=3, value=rev).number_format = INDIAN
    if city != "Mumbai":
        ws.row_dimensions[i].hidden = True
ws.auto_filter.ref = "A4:C12"
ws.auto_filter.add_filter_column(1, ["Mumbai"])
put(ws, "A14", "The foot: total revenue (Rs)", BOLD); put(ws, "C14", "=SUM(C5:C12)", fmt=INDIAN)
put(ws, "A15", "Rows you can see"); put(ws, "C15", "=SUBTOTAL(103,A5:A12)")
put(ws, "A16", "Rows in the list"); put(ws, "C16", "=COUNTA(A5:A12)")
put(ws, "A17", "The check", BOLD, wrap=True)
put(ws, "B17", '=IF(C14<>SUBTOTAL(109,C5:C12),"The foot adds "&C16&" rows while "&C15&" are visible: it counts '
               'rows the filter hid. Fix it first.","The foot adds only the rows you can see.")', wrap=True)
put(ws, "A19", "Verdict", VERDICT, wrap=True)
put(ws, "B19", '=IF(C14<>SUBTOTAL(109,C5:C12),"Fix the foot total before reading it as the city\'s list.",'
               '"The "&C15&" members you can see spent "&' + rs("C14") + '&".")', VERDICT, TINT, True)
put(ws, "A20", "Fixed, for the Export tab", NOTE); put(ws, "B20", "=IF(C14=SUBTOTAL(109,C5:C12),1,0)")
ws.row_dimensions[17].height = 32

# ---------------------------------------------------------------- Front page
ws = sheet(wb, "Front page", "Is the card ready for the front page?",
           "One number is read correctly only with its period, its comparison and its denominator, and a change is "
           "measured on the earlier period.")
head(ws, 4, ["Input", "Value"])
put(ws, "A5", "The number (Rs)"); put(ws, "B5", 98400000, fill=INPUT, fmt=INDIAN)
put(ws, "A6", "The comparison figure (Rs)"); put(ws, "B6", 100000000, fill=INPUT, fmt=INDIAN)
put(ws, "A7", "The period of the number"); put(ws, "B7", "Q2, July to September 2026", fill=INPUT)
put(ws, "A8", "The period it is compared with"); put(ws, "B8", "Q1, April to June 2026", fill=INPUT)
put(ws, "A9", "Company revenue in the same period (Rs)"); put(ws, "B9", 98400000, fill=INPUT, fmt=INDIAN)
put(ws, "A10", "What the number covers"); put(ws, "B10", "All segments", fill=INPUT)
put(ws, "A12", "Change on the comparison"); put(ws, "B12", "=(B5-B6)/B5", fmt="0.0%")
put(ws, "A13", "The check", BOLD, wrap=True)
put(ws, "B13", '=IF(ABS(B12-(B5-B6)/B6)>0.00001,"The change is divided by the current period; a change is measured '
               'on the earlier one. Fix it first.","The change is measured on the earlier period.")', wrap=True)
put(ws, "A14", "What the card still lacks")
put(ws, "B14", '=IF(B7="","the period",IF(B8="","the comparison",IF(B9=0,"the denominator","")))')
put(ws, "A16", "Verdict", VERDICT, wrap=True)
put(ws, "B16", '=IF(ABS(B12-(B5-B6)/B6)>0.00001,"Fix the change formula before the card is drafted.",IF(B14<>"",'
               '"Not ready for the front page: add "&B14&", or the number is read against whatever the director '
               'remembers.",B10&", "&B7&": "&' + crl("B5") + '&", "&IF(B12<0,"down ","up ")&TEXT(ABS(B12)*100,"0.0")&'
               '" percent on "&B8&" ("&' + crl("B6") + '&"); "&TEXT(B5/B9*100,"0.0")&" percent of company revenue."))',
    VERDICT, TINT, True)
put(ws, "A17", "Fixed, for the Export tab", NOTE); put(ws, "B17", "=IF(ABS(B12-(B5-B6)/B6)<=0.00001,1,0)")
ws.row_dimensions[13].height = 32; ws.row_dimensions[16].height = 48

# ---------------------------------------------------------------- Rule
ws = sheet(wb, "Rule", "Which tool owns this number?",
           "The source of truth is decided first; who presents the number is decided second.")
head(ws, 3, ["Question about the ask", "Answer"])
put(ws, "A4", "The ask"); put(ws, "B4", "The front-page revenue number", fill=INPUT)
put(ws, "A5", "Does Finance audit this number?"); put(ws, "B5", "yes", fill=INPUT)
put(ws, "A6", "Does it need a join, a dedupe or a cleaning step?"); put(ws, "B6", "no", fill=INPUT)
put(ws, "A7", "Is it an analyst's question that changes every day?"); put(ws, "B7", "no", fill=INPUT)
put(ws, "A8", "Will a stakeholder explore a finished table in the room?"); put(ws, "B8", "yes", fill=INPUT)
for ref in ("B5", "B6", "B7", "B8"):
    choice(ws, ref, ["yes", "no"])
put(ws, "A10", "Who owns it"); put(ws, "B10", '=IF(B8="yes","Excel",IF(B5="yes","the warehouse",IF(B6="yes",'
                                               '"the warehouse",IF(B7="yes","pandas","Excel"))))')
put(ws, "A11", "The check", BOLD, wrap=True)
put(ws, "B11", '=IF(AND(OR(B5="yes",B6="yes"),B10<>"the warehouse"),"Finance audits it or it needs cleaning, yet the '
               'rule sends it to "&B10&": the tests run in the wrong order. Fix it first.","The source of truth is '
               'decided before who presents it.")', wrap=True)
put(ws, "A13", "Verdict", VERDICT, wrap=True)
put(ws, "B13", '=IF(AND(OR(B5="yes",B6="yes"),B10<>"the warehouse"),"Fix the order of the tests before the rule is '
               'written down.",B4&": "&IF(B10="the warehouse","the warehouse computes it"&IF(B8="yes",", and Excel '
               'presents it read-only, refreshed from the export",""),IF(B10="pandas","pandas owns the iteration '
               'until Finance relies on it","Excel may own it, because nothing downstream audits it"))&".")',
    VERDICT, TINT, True)
put(ws, "A14", "Fixed, for the Export tab", NOTE)
put(ws, "B14", '=IF(AND(OR(B5="yes",B6="yes"),B10<>"the warehouse"),0,1)')
ws.row_dimensions[11].height = 32; ws.row_dimensions[13].height = 36

# ---------------------------------------------------------------- Export
ws = sheet(wb, "Export", "The operating rule, assembled",
           "Released only when every tab passes its check. Paste it into the team note.")
ws.column_dimensions["B"].width = 118
put(ws, "A4", "Tabs fixed", BOLD)
put(ws, "B4", "=Pivot!B15+Lookup!E12+'Visible total'!B20+'Front page'!B17+Rule!B14")
put(ws, "A5", "Release", VERDICT, wrap=True)
put(ws, "B5", '=IF(B4=5,"Ready to paste into the team note.","Not ready: "&(5-B4)&" of the five tabs still carry a '
              'defect to fix first.")', VERDICT, TINT, True)
put(ws, "A7", "Paste-ready rule", BOLD, wrap=True)
put(ws, "B7", '=IF(B4=5,"Pivot: "&Pivot!B14&CHAR(10)&"Lookup: "&Lookup!E11&CHAR(10)&"Visible total: "&'
              '\'Visible total\'!B19&CHAR(10)&"Front page: "&\'Front page\'!B16&CHAR(10)&"Rule: "&Rule!B13,'
              '"The rule assembles once every tab passes its check.")', wrap=True)
ws.row_dimensions[7].height = 120

wb.save(OUT)
print(f"wrote {OUT}")

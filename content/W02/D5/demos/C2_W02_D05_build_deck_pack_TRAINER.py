"""Build Friday's deck pack: the three things Meera's chief of staff opens on Monday, as live formulas.

Run from the repository root:  python3 content/W02/D5/demos/C2_W02_D05_build_deck_pack_TRAINER.py

The workbook is the escalated case's solution and the trainer's demonstration surface in one file.
Every number on the Tree, Protect and FrontPage tabs is a formula over the two exports pasted in as
values on the Raw and Customers tabs, so a director who changes a yellow cell sees the sheet
recalculate, and scripts/xlsx_recalc.py proves it by recalculating through LibreOffice.

The Tree tab is the pivot written as SUMIFS. A real PivotTable is built live in Excel by the room;
openpyxl cannot write one, and a SUMIFS pivot recalculates without a refresh, which is the point
the day makes about a pivot a director slices in the room.

Formulas are restricted to what LibreOffice 24.2 computes (INDEX, MATCH, SUMIFS, COUNTIFS,
SUBTOTAL, TEXT, IF, IFERROR). The one XLOOKUP cell carries the _xlfn prefix Excel expects and is
labelled as computed in Excel and not proved here, because LibreOffice 24.2 returns #NAME? for it.
"""
import csv
import datetime
import pathlib

from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = pathlib.Path("content/W02/D5")
CLEAN = ROOT / "data" / "C2_W02_D05_customer_table_STUDENT.csv"
RAW = ROOT / "data" / "C2_W02_D05_raw_export_STUDENT.csv"
OUT = ROOT / "demos" / "C2_W02_D05_deck_pack_STUDENT.xlsx"

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

SEGMENTS = ["Business", "Retail-Core", "Retail-Plus", "Student"]
MONTHS = [(202604, "Apr"), (202605, "May"), (202606, "Jun"),
          (202607, "Jul"), (202608, "Aug"), (202609, "Sep")]


def read(path):
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def rs(ref):
    """Rupees with Indian grouping, up to Rs 99,99,999, as a formula fragment."""
    r = f"ROUND({ref},0)"
    return (f'"Rs "&IF({r}>=100000,INT({r}/100000)&","&TEXT(INT(MOD({r},100000)/1000),"00")&","&'
            f'TEXT(MOD({r},1000),"000"),IF({r}>=1000,INT({r}/1000)&","&TEXT(MOD({r},1000),"000"),{r}&""))')


def crl(ref):
    """Rupees in crore or lakh the way a deck says them, as a formula fragment."""
    ref = f"({ref})"  # bracketed, so a sum such as H11+I11 is divided whole
    return (f'IF(ABS({ref})>=10000000,"Rs "&TEXT({ref}/10000000,"0.00")&" crore",'
            f'IF(ABS({ref})>=100000,"Rs "&TEXT({ref}/100000,"0.00")&" lakh",{rs(ref)}))')


def sheet(wb, name, title, lede, widths):
    ws = wb.create_sheet(name)
    ws["A1"], ws["A1"].font = title, TITLE
    ws["A2"], ws["A2"].font = lede, NOTE
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    return ws


def head(ws, row, labels, col=1):
    for j, text in enumerate(labels):
        c = ws.cell(row=row, column=col + j, value=text)
        c.font, c.fill = HEAD, HEADFILL
        c.alignment = Alignment(wrap_text=True, vertical="center")


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


clean = read(CLEAN)
raw = read(RAW)
NR, NC = len(raw) + 1, len(clean) + 1            # last data row on Raw and on Customers


def rr(col):
    return f"Raw!${col}$2:${col}${NR}"


def cr(col):
    return f"Customers!${col}$2:${col}${NC}"


wb = Workbook()
start = wb.active
start.title = "Start"
start["A1"], start["A1"].font = "Monday's growth review: the deck pack", TITLE
start.column_dimensions["A"].width = 118
for i, text in enumerate([
    "Kalpa Retail, Week 2, Friday. Three things Meera's chief of staff opens on a laptop without a login.",
    "Tree: the revenue tree by segment for Q1 and Q2. Protect: the top-fifty protect list and a lookup by member id. "
    "FrontPage: one number with its period, its comparison, its denominator and its monthly trend.",
    "Checks: whether all three may go into the deck. It holds anything that does not reconcile to the warehouse.",
    "Yellow cells are the assumptions a director may change in the room. Every other cell is a live formula over the "
    "Raw and Customers tabs, which hold the two exports exactly as they arrived.",
    "The Tree tab is a pivot written as SUMIFS, so it recalculates the moment a yellow cell changes. A PivotTable "
    "needs a refresh after its source changes.",
    "The XLOOKUP cell on the Protect tab is computed in Excel and not proved here: LibreOffice 24.2 returns #NAME? "
    "for it, so every other lookup uses INDEX and MATCH.",
    "The warehouse owns these numbers. Change an assumption here; never type over a computed cell.",
], 3):
    start.cell(row=i, column=1, value=text).alignment = WRAP

# ---------------------------------------------------------------- Raw: the export as it arrived
ws = wb.create_sheet("Raw")
cols = ["order_id", "customer_id", "segment", "channel", "order_date", "order_amount", "paid_amount",
        "paid_date", "quarter", "month", "first row of this order", "first order of this customer in the quarter",
        "amount counted", "orders counted", "customers counted"]
head(ws, 1, cols)
for i, r in enumerate(raw, 2):
    ws.cell(row=i, column=1, value=r["order_id"])
    ws.cell(row=i, column=2, value=r["customer_id"])
    ws.cell(row=i, column=3, value=r["segment"])
    ws.cell(row=i, column=4, value=r["channel"])
    d = ws.cell(row=i, column=5, value=datetime.date.fromisoformat(r["order_date"]))
    d.number_format = "yyyy-mm-dd"
    ws.cell(row=i, column=6, value=int(r["order_amount"]))
    ws.cell(row=i, column=7, value=int(r["paid_amount"]))
    ws.cell(row=i, column=8, value=r["paid_date"])
    ws.cell(row=i, column=9, value=f'=IF(MONTH(E{i})<=6,"Q1","Q2")')
    ws.cell(row=i, column=10, value=f"=YEAR(E{i})*100+MONTH(E{i})")
    ws.cell(row=i, column=11, value=f"=IF(COUNTIF($A$2:A{i},A{i})=1,1,0)")
    ws.cell(row=i, column=12, value=f"=IF(K{i}=1,IF(COUNTIFS($B$2:B{i},B{i},$I$2:I{i},I{i},$K$2:K{i},1)=1,1,0),0)")
    ws.cell(row=i, column=13, value=f'=IF(Tree!$C$4="once per order",F{i}*K{i},F{i})')
    ws.cell(row=i, column=14, value=f'=IF(Tree!$C$4="once per order",K{i},1)')
    ws.cell(row=i, column=15, value=f'=IF(Tree!$C$4="once per order",L{i},1)')
for col, w in zip("ABCDEFGHIJKLMNO", [11, 12, 12, 9, 12, 13, 12, 12, 9, 9, 12, 14, 13, 11, 11]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "A2"
ws.auto_filter.ref = f"A1:O{NR}"

# ---------------------------------------------------------------- Customers: the clean table
ws = wb.create_sheet("Customers")
head(ws, 1, ["customer_id", "segment", "city", "orders", "revenue", "last_order_date", "rank in the list's segment"])
for i, r in enumerate(clean, 2):
    ws.cell(row=i, column=1, value=r["customer_id"])
    ws.cell(row=i, column=2, value=r["segment"])
    ws.cell(row=i, column=3, value=r["city"])
    ws.cell(row=i, column=4, value=int(r["orders"]))
    ws.cell(row=i, column=5, value=int(r["revenue"])).number_format = INDIAN
    ws.cell(row=i, column=6, value=datetime.date.fromisoformat(r["last_order_date"])).number_format = "yyyy-mm-dd"
    # Rank within the segment the Protect tab asks for; an equal revenue breaks by row, which is id order.
    ws.cell(row=i, column=7, value=f'=IF(B{i}=Protect!$C$4,COUNTIFS($B$2:$B${NC},B{i},$E$2:$E${NC},">"&E{i})'
                                    f'+COUNTIFS($B$2:B{i},B{i},$E$2:E{i},E{i}),"")')
for col, w in zip("ABCDEFG", [12, 13, 12, 8, 13, 14, 14]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "A2"
ws.auto_filter.ref = f"A1:G{NC}"

# ---------------------------------------------------------------- Tree
ws = sheet(wb, "Tree", "The revenue tree by segment, Q1 against Q2",
           "Customers times orders per customer times revenue per order, per segment and quarter, counted from the raw "
           "export. It must reconcile to the warehouse before any number leaves the team.",
           {"A": 30, "B": 11, "C": 20, "D": 11, "E": 11, "F": 15, "G": 11, "H": 9, "I": 11, "J": 11, "K": 15, "L": 12})
put(ws, "A4", "Count each order", BOLD); put(ws, "C4", "once per order", fill=INPUT)
choice(ws, "C4", ["once per order", "once per row"])
put(ws, "A5", "Warehouse total, both quarters (Rs)", BOLD); put(ws, "C5", 198400000, fill=INPUT, fmt=INDIAN)
head(ws, 7, ["Segment", "Q1 customers", "Q1 orders", "Q1 orders per customer", "Q1 revenue per order",
             "Q1 revenue (Rs)", "Q2 customers", "Q2 orders", "Q2 orders per customer", "Q2 revenue per order",
             "Q2 revenue (Rs)", "Revenue change"])
for k, seg in enumerate(SEGMENTS + ["All segments"], 8):
    ws.cell(row=k, column=1, value=seg).font = BOLD if seg == "All segments" else Font(color=INK)
    for q, base in (("Q1", 2), ("Q2", 7)):
        c = [None] + [chr(64 + base + j) for j in range(5)]      # customers, orders, opc, rpo, revenue
        if seg == "All segments":
            ws[f"{c[1]}{k}"] = f"=SUM({c[1]}8:{c[1]}11)"
            ws[f"{c[2]}{k}"] = f"=SUM({c[2]}8:{c[2]}11)"
            ws[f"{c[5]}{k}"] = f"=SUM({c[5]}8:{c[5]}11)"
        else:
            where = f'{rr("C")},$A{k},{rr("I")},"{q}"'
            ws[f"{c[1]}{k}"] = f"=SUMIFS({rr('O')},{where})"
            ws[f"{c[2]}{k}"] = f"=SUMIFS({rr('N')},{where})"
            ws[f"{c[5]}{k}"] = f"=SUMIFS({rr('M')},{where})"
        ws[f"{c[3]}{k}"] = f"=IF({c[1]}{k}=0,0,{c[2]}{k}/{c[1]}{k})"
        ws[f"{c[4]}{k}"] = f"=IF({c[2]}{k}=0,0,{c[5]}{k}/{c[2]}{k})"
        ws[f"{c[3]}{k}"].number_format = "0.00"
        ws[f"{c[4]}{k}"].number_format = INDIAN
        ws[f"{c[5]}{k}"].number_format = INDIAN
    ws[f"L{k}"] = f"=IF(F{k}=0,0,(K{k}-F{k})/F{k})"
    ws[f"L{k}"].number_format = "0.0%"
put(ws, "A14", "Tree total, both quarters (Rs)", BOLD); put(ws, "C14", "=F12+K12", fmt=INDIAN)
put(ws, "A15", "Tree total less the warehouse (Rs)"); put(ws, "C15", "=C14-C5", fmt=INDIAN)
put(ws, "A16", "Rows in the export"); put(ws, "C16", f"=COUNTA({rr('A')})")
put(ws, "A17", "Distinct orders in the export"); put(ws, "C17", f"=SUM({rr('K')})")
put(ws, "A18", "The check", BOLD, wrap=True)
put(ws, "C18", '=IF(ABS(C15)<1,"The tree reconciles to the warehouse to the rupee.",'
               '"The tree is "&' + crl("C15") + '&" over the warehouse: "&C16&" rows carry "&C17&" orders, '
               'so some orders are counted more than once.")', wrap=True)
put(ws, "A20", "Verdict", VERDICT, wrap=True)
put(ws, "C20", '=IF(ABS(C15)>=1,"Do not send: the tree counts an order once per payment row. Count each order once.",'
               '"Send: Q2 revenue "&' + crl("K12") + '&", "&IF(L12<0,"down ","up ")&TEXT(ABS(L12)*100,"0.0")&'
               '" percent on Q1; Retail-Plus orders per customer "&TEXT(D10,"0.00")&" to "&TEXT(I10,"0.00")&'
               '", customers "&B10&" to "&G10&".")', VERDICT, TINT, True)
ws.merge_cells("C18:L18"); ws.merge_cells("C20:L20")
ws.row_dimensions[18].height = 32; ws.row_dimensions[20].height = 48
chart = BarChart()
chart.type = "col"
chart.title = "Orders per customer, Q1 against Q2"
chart.y_axis.title = "orders per customer"
chart.add_data(Reference(ws, min_col=4, min_row=7, max_row=11), titles_from_data=True)
chart.add_data(Reference(ws, min_col=9, min_row=7, max_row=11), titles_from_data=True)
chart.set_categories(Reference(ws, min_col=1, min_row=8, max_row=11))
chart.height, chart.width = 7.5, 16
for series, colour in zip(chart.series, ("CFC9EE", "5B3FD6")):
    series.graphicalProperties.solidFill = colour
    series.graphicalProperties.line.solidFill = colour
ws.add_chart(chart, "B24")

# ---------------------------------------------------------------- Protect
ws = sheet(wb, "Protect", "The protect list, and a lookup by member id",
           "The top members of one segment by revenue across both quarters, from the clean customer table. "
           "The lookup must say so when an id is missing.",
           {"A": 26, "B": 13, "C": 14, "D": 9, "E": 22, "F": 60, "G": 44})
put(ws, "A4", "Segment of the list", BOLD); put(ws, "C4", "Retail-Plus", fill=INPUT); choice(ws, "C4", SEGMENTS)
put(ws, "A5", "List size", BOLD); put(ws, "C5", 50, fill=INPUT)
put(ws, "A6", "Member id to find", BOLD); put(ws, "C6", "C-0152", fill=INPUT)
put(ws, "A7", "Match type", BOLD); put(ws, "C7", "exact", fill=INPUT); choice(ws, "C7", ["exact", "approximate"])
put(ws, "E4", "Row returned", BOLD, wrap=True)
put(ws, "F4", f'=IF(C7="exact",IFERROR(INDEX({cr("A")},MATCH(C6,{cr("A")},0)),"not found"),'
              f'IFERROR(INDEX({cr("A")},MATCH(C6,{cr("A")},1)),"not found"))')
put(ws, "E5", "Revenue (Rs)", BOLD, wrap=True)
put(ws, "F5", f'=IF(F4="not found","",INDEX({cr("E")},MATCH(F4,{cr("A")},0)))', fmt=INDIAN)
put(ws, "E6", "Place on the list", BOLD, wrap=True)
put(ws, "F6", f'=IF(F4="not found","",IFERROR(IF(INDEX({cr("G")},MATCH(F4,{cr("A")},0))<=C5,'
              f'"rank "&INDEX({cr("G")},MATCH(F4,{cr("A")},0))&" of "&C5&" on the "&C4&" list",'
              f'"outside the top "&C5),"not in the "&C4&" segment"))')
put(ws, "E7", "The check", BOLD, wrap=True)
put(ws, "F7", '=IF(F4="not found",C6&" is not in the customer table.",IF(F4=C6,'
              '"The row returned is the member asked for.","The lookup returned "&F4&" for "&C6&": '
              'an approximate match answered with a neighbour."))', wrap=True)
put(ws, "E8", "XLOOKUP, in Excel", BOLD, wrap=True)
put(ws, "F8", f'=_xlfn.XLOOKUP(C6,{cr("A")},{cr("E")},"not in the table",0)')
put(ws, "G8", "Computed in Excel, not proved here: LibreOffice 24.2 returns #NAME? for XLOOKUP.", NOTE, wrap=True)
put(ws, "E9", "Verdict", VERDICT, wrap=True)
put(ws, "F9", '=IF(F4="not found",C6&" is not in the customer table: say so, and check the export before anyone '
              'answers.",IF(F4<>C6,"Do not answer: the lookup returned "&F4&"\'s row for "&C6&". Switch the match '
              'to exact.",C6&": "&' + rs("F5") + '&" across both quarters, "&F6&"."))', VERDICT, TINT, True)
ws.row_dimensions[7].height = 30; ws.row_dimensions[9].height = 32
head(ws, 11, ["Rank", "Member id", "City", "Orders", "Revenue (Rs)", "Last order"])
for k in range(1, 61):
    row = 11 + k
    ws[f"A{row}"] = k
    ws[f"B{row}"] = (f'=IF($A{row}<=$C$5,IFERROR(INDEX({cr("A")},MATCH($A{row},{cr("G")},0)),""),"")')
    for col, src in (("C", "C"), ("D", "D"), ("E", "E"), ("F", "F")):
        ws[f"{col}{row}"] = f'=IF($B{row}="","",INDEX({cr(src)},MATCH($B{row},{cr("A")},0)))'
    ws[f"E{row}"].number_format = INDIAN
    ws[f"F{row}"].number_format = "yyyy-mm-dd"
    ws[f"F{row}"].alignment = Alignment(horizontal="left")
put(ws, "A73", "Members you can see", BOLD); put(ws, "E73", "=SUBTOTAL(102,E12:E71)")
put(ws, "A74", "Total of the rows you can see (Rs)", BOLD); put(ws, "E74", "=SUBTOTAL(109,E12:E71)", fmt=INDIAN)
put(ws, "A75", "Total of the whole list (Rs)"); put(ws, "E75", "=SUM(E12:E71)", fmt=INDIAN)
put(ws, "A76", "List verdict", VERDICT, wrap=True)
put(ws, "B76", '=IF(E73<COUNT(E12:E71),"Filtered: the foot totals the "&E73&" members you can see, "&' + rs("E74") +
               '&"; the whole list is "&' + crl("E75") + '&".","The top "&E73&" "&C4&" members spent "&' + crl("E74") +
               '&" across both quarters.")', VERDICT, TINT, True)
ws.merge_cells("B76:F76"); ws.row_dimensions[76].height = 30
ws.auto_filter.ref = "A11:F71"
ws.freeze_panes = "A12"

# ---------------------------------------------------------------- FrontPage
ws = sheet(wb, "FrontPage", "One number, with its period, comparison, denominator and trend",
           "The card a director reads in two minutes. Change the scope and the number, the sentence and the trend move "
           "together.",
           {"A": 34, "B": 15, "C": 15, "D": 15, "E": 15, "F": 15, "G": 15, "H": 16})
put(ws, "A4", "What the card covers", BOLD); put(ws, "B4", "All segments", fill=INPUT)
choice(ws, "B4", ["All segments", "All except Business"] + SEGMENTS)
head(ws, 6, ["Revenue by month (Rs)"] + [m for _, m in MONTHS] + ["Q1 total", ])
for k, seg in enumerate(SEGMENTS, 7):
    ws.cell(row=k, column=1, value=seg)
    for j, (key, _) in enumerate(MONTHS, 2):
        col = chr(64 + j)
        ws[f"{col}{k}"] = f'=SUMIFS({rr("M")},{rr("C")},$A{k},{rr("J")},{key})'
        ws[f"{col}{k}"].number_format = INDIAN
put(ws, "A11", "All segments", BOLD)
put(ws, "A12", "The card's scope", BOLD)
for j in range(2, 8):
    col = chr(64 + j)
    put(ws, f"{col}11", f"=SUM({col}7:{col}10)", fmt=INDIAN)
    put(ws, f"{col}12", f'=IF($B$4="All segments",{col}11,IF($B$4="All except Business",{col}11-{col}7,'
                        f'INDEX({col}7:{col}10,MATCH($B$4,$A$7:$A$10,0))))', BOLD, TINT, fmt=INDIAN)
put(ws, "H6", "Q1 total"); ws["H6"].font, ws["H6"].fill = HEAD, HEADFILL
put(ws, "I6", "Q2 total"); ws["I6"].font, ws["I6"].fill = HEAD, HEADFILL
for k in range(7, 13):
    put(ws, f"H{k}", f"=SUM(B{k}:D{k})", fmt=INDIAN)
    put(ws, f"I{k}", f"=SUM(E{k}:G{k})", fmt=INDIAN)
ws.column_dimensions["I"].width = 16
put(ws, "A14", "The number", BOLD); put(ws, "B14", "=" + crl("I12"))
put(ws, "A15", "The period", BOLD); put(ws, "B15", "Q2, July to September 2026")
put(ws, "A16", "The comparison", BOLD)
put(ws, "B16", '=IF(H12=0,"no Q1 figure to compare",IF(I12<H12,"down ","up ")&TEXT(ABS(I12-H12)/H12*100,"0.0")&'
               '" percent on Q1, April to June 2026 ("&' + crl("H12") + '&")")')
put(ws, "A17", "The denominator", BOLD)
put(ws, "B17", '=TEXT(I12/I11*100,"0.0")&" percent of company revenue in Q2"')
put(ws, "A18", "The check", BOLD, wrap=True)
put(ws, "B18", '=IF(ABS(H11+I11-Tree!C5)<1,"The card reconciles to the warehouse.",'
               '"The card does not reconcile: its two quarters sum to "&' + crl("H11+I11") +
               '&" against the warehouse\'s "&' + crl("Tree!C5") + '&".")', wrap=True)
put(ws, "A20", "The card", VERDICT, wrap=True)
put(ws, "B20", '=IF(ABS(H11+I11-Tree!C5)>=1,"Hold the card: it is built on a count that does not reconcile to the '
               'warehouse.",B4&", "&B15&": "&B14&", "&B16&"; "&B17&".")', VERDICT, TINT, True)
ws.merge_cells("B18:I18"); ws.merge_cells("B20:I20")
ws.row_dimensions[18].height = 30; ws.row_dimensions[20].height = 40
trend = LineChart()
trend.title = "Monthly revenue for the card's scope, April to September 2026"
trend.y_axis.title = "Rs"
trend.add_data(Reference(ws, min_col=1, max_col=7, min_row=12), from_rows=True, titles_from_data=True)
trend.set_categories(Reference(ws, min_col=2, max_col=7, min_row=6))
trend.height, trend.width = 7.5, 18
for series in trend.series:
    series.smooth = False
    series.graphicalProperties.line.solidFill = "5B3FD6"
    series.graphicalProperties.line.width = 28575
ws.add_chart(trend, "A23")

# ---------------------------------------------------------------- Checks
ws = sheet(wb, "Checks", "What may go into Monday's deck",
           "Each deliverable goes in only when its numbers reconcile to the warehouse. A held item says why.",
           {"A": 48, "B": 12, "C": 90})
head(ws, 4, ["Check", "Passes", "What it found"])
rows = [
    ("The tree reconciles to the warehouse", "=IF(ABS(Tree!C15)<1,1,0)", "=Tree!C18"),
    ("The customer table reconciles to the warehouse",
     f"=IF(ABS(SUM({cr('E')})-Tree!C5)<1,1,0)",
     f'=IF(B6=1,"The customer table sums to the warehouse total.","The customer table is "&'
     + crl(f"Tree!C5-SUM({cr('E')})") + f'&" and "&(Tree!C17-SUM({cr("D")}))&" orders short of the warehouse, '
     f'so the protect list may be missing a member.")'),
    ("The lookup answers with the member asked for", '=IF(OR(Protect!F4="not found",Protect!F4=Protect!C6),1,0)',
     "=Protect!F7"),
    ("The front page reconciles to the warehouse", "=IF(ABS(FrontPage!H11+FrontPage!I11-Tree!C5)<1,1,0)",
     "=FrontPage!B18"),
]
for i, (label, ok, why) in enumerate(rows, 5):
    put(ws, f"A{i}", label)
    put(ws, f"B{i}", ok)
    put(ws, f"C{i}", why, wrap=True)
    ws.row_dimensions[i].height = 30
put(ws, "A10", "Release", VERDICT)
put(ws, "C10", '=IF(SUM(B5:B8)=4,"Ready for Monday\'s deck: the tree, the protect list and the front page.",'
               'IF(B5=0,"Do not send anything: the tree counts an order more than once, and the card inherits it.",'
               'IF(B6=0,"Send the tree and the front page. Hold the protect list until the customer table reconciles to the warehouse.",'
               '"Hold what fails above and send the rest.")))', VERDICT, TINT, True)
ws.row_dimensions[10].height = 46

wb.move_sheet("Checks", offset=-(len(wb.sheetnames) - 2))
wb.save(OUT)
print(f"wrote {OUT}")

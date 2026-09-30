"""Write Build 1's grade closure workbook and the recalc manifest that proves it computes.

    python3 content/W03/SAT/internal/C2_W03_SAT_build_grade_closure_INTERNAL.py

Writes, beside each other in content/W03/SAT/rubrics/:
  C2_W03_SAT_grade_closure_TRAINER.xlsx        35 learner seats by group, never a name
  C2_W03_SAT_grade_closure_recalc_INTERNAL.md  the verdicts and flips scripts/xlsx_recalc.py asserts

The workbook reads the marks per event from data/programme/facts.yaml (evaluation.rubrics.W03.events:
GD 30, mini project 40 including the presentation, mock 30) and takes each event's total from its scoring sheet, so it
carries no criterion itself; the approved criteria live in facts.yaml and in the scoring sheets. Every total and every check is a formula, so LibreOffice or Excel recomputes
them as scores are entered.
"""
import pathlib

import yaml
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.formula import ArrayFormula

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parent / "rubrics"
BOOK = "C2_W03_SAT_grade_closure_TRAINER.xlsx"
MANIFEST = "C2_W03_SAT_grade_closure_recalc_INTERNAL.md"

# The cohort as the handover states it (facts.yaml, cohort: 35 students in nine groups of four), so
# eight groups of four and one of three. Which group holds three is the Programme Head's Monday call.
GROUPS = [(f"G{g}", 4) for g in range(1, 9)] + [("G9", 3)]
facts = yaml.safe_load((ROOT / "data" / "programme" / "facts.yaml").read_text(encoding="utf-8"))
EVENTS = facts["evaluation"]["rubrics"]["W03"]["events"]
MAX = {"GD": EVENTS["gd"]["marks"], "Mini project": EVENTS["mini-project"]["marks"], "Mock": EVENTS["mock"]["marks"]}
assert sum(n for _, n in GROUPS) == facts["cohort"]["students"]["value"]
ABSENT = "ABSENT"
FIRST = 6  # first seat row on the Scores sheet
SIGNERS = [
    ("GD assessor: the industry expert", "The GD scores of the rounds the expert ran, Friday and Saturday"),
    ("GD assessor: the Principal Advisor", "The GD scores of the rounds run online"),
    ("Panel: the industry expert", "The mini project scores of the groups this panel heard"),
    ("Panel: the senior industry leader", "The mini project scores of the groups this panel heard"),
    ("Mock assessor: the Principal Advisor", "The Mock R1 scores this assessor gave"),
    ("Mock assessor: the Programme Head", "The Mock R1 scores this assessor gave"),
    ("Mock assessor: the Academic TA", "The Mock R1 scores this assessor gave"),
    ("Closure: the Programme Head", "Every seat holds three scores, the checks are clear, and the grades are closed"),
]

ARIAL = "Arial"
INK = "1A0F5C"
HEAD = PatternFill("solid", fgColor=INK)
INPUT = PatternFill("solid", fgColor="FFF4B8")
BAND = PatternFill("solid", fgColor="F1EEFA")
thin = Side(style="thin", color="C9C3E6")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)


def font(bold=False, color="000000", size=10, italic=False):
    return Font(name=ARIAL, bold=bold, color=color, size=size, italic=italic)


def header(ws, row, labels, widths=None):
    for i, text in enumerate(labels, start=1):
        c = ws.cell(row=row, column=i, value=text)
        c.font = font(bold=True, color="FFFFFF")
        c.fill = HEAD
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = BOX
    if widths:
        for i, w in enumerate(widths, start=1):
            ws.column_dimensions[ws.cell(row=row, column=i).column_letter].width = w


def build():
    wb = Workbook()

    # ---------------- Read me ----------------
    rm = wb.active
    rm.title = "Read me"
    rm.column_dimensions["A"].width = 26
    rm.column_dimensions["B"].width = 96
    rm["A1"] = "Build 1 grade closure: Week 3, Kalpa Health"
    rm["A1"].font = font(bold=True, color=INK, size=14)
    rm["A2"] = "TRAINER ONLY. The committed file is the empty template; a filled copy holds learners' scores and is never committed."
    rm["A2"].font = font(italic=True)
    rows = [
        ("What it closes", "Three scores per learner: the GD score out of 30, the mini project score out of 40 including the presentation, and the Mock R1 score out of 30. The marks per event are locked (data/programme/facts.yaml). Each total is copied from its scoring sheet, which carries the criteria the requester approved on 29 September 2026: the GD from content/W03/D5/rubrics/C2_W03_D05_gd_scoring_sheet_TRAINER.xlsx, the mini project from C2_W03_SAT_mini_project_scoring_TRAINER.xlsx beside this file, and the mock from content/W03/D4/rubrics/C2_W03_D04_mock_scoring_sheet_TRAINER.xlsx."),
        ("Where to type", "Only the yellow cells on the Scores sheet (columns C to G and J) and the Signed column on the Sign-off sheet. Every other cell is a formula."),
        ("Entered once", "Each score is typed once, by the scribe named on the run sheet, from the assessor's signed sheet. A correction replaces the one cell; it is never typed in a second place."),
        ("Seats, never names", "Seats are labelled by group and seat (G1-S1). The Programme Head keeps the seat-to-learner key outside this repository. Eight groups hold four seats and G9 holds three, as the handover's 35 learners in nine groups give; relabel the seat column if Monday's allocation put the group of three elsewhere."),
        ("Status, per seat", "COMPLETE when all three scores are in and within their maximums. ABSENT names the events the learner missed, when every other score is in. MISSING names the scores still to enter. OVER MAX means a score above its event's maximum. NOT A SCORE means other text or a negative number in a score cell."),
        ("The verdict", "The Checks sheet reads READY TO SIGN only when every seat is COMPLETE or ABSENT, no seat repeats, and no flag remains. It lists the seats still short and the seats with an absence, by seat. The Sign-off sheet reads CLOSED only after that, with every role signed."),
        ("An absence", "A learner who missed an event has ABSENT typed in that event's cell, and the Programme Head's decision goes in Notes. The seat then counts as closed, carries no total, and is listed on the Checks sheet. No make-up rule is published, so this workbook sets none."),
        ("Example, format only", "Seat G1-S1, group G1, sub-problem 2 bookings, panel the industry expert, GD 21, mini project 29.5, mock 22: total 72.5, status COMPLETE. This example is not on the Scores sheet."),
    ]
    for i, (a, b) in enumerate(rows, start=4):
        rm.cell(row=i, column=1, value=a).font = font(bold=True, color=INK)
        c = rm.cell(row=i, column=2, value=b)
        c.font = font()
        c.alignment = Alignment(wrap_text=True, vertical="top")
        rm.row_dimensions[i].height = 44

    # ---------------- Scores ----------------
    ws = wb.create_sheet("Scores")
    ws["A1"] = "Scores: one row per learner seat"
    ws["A1"].font = font(bold=True, color=INK, size=13)
    ws["A2"] = "Type only in the yellow cells. Row 4 holds each event's maximum, which every check reads."
    ws["A2"].font = font(italic=True)
    ws["A4"] = "Maximum"
    ws["A4"].font = font(bold=True)
    for col, key in (("E", "GD"), ("F", "Mini project"), ("G", "Mock")):
        ws[f"{col}4"] = MAX[key]
        ws[f"{col}4"].font = font(bold=True, color="0000FF")
        ws[f"{col}4"].comment = Comment("Locked marks per event, data/programme/facts.yaml, evaluation per_event.", "C2")
    ws["H4"] = "=E4+F4+G4"
    ws["H4"].font = font(bold=True)
    header(ws, 5, ["Seat", "Group", "Sub-problem", "Panel", "GD (of 30)", "Mini project (of 40)",
                   "Mock (of 30)", "Total (of 100)", "Status", "Notes"],
           [10, 8, 16, 26, 11, 13, 11, 12, 30, 44])
    last = FIRST + sum(n for _, n in GROUPS) - 1
    r = FIRST
    for g, n in GROUPS:
        for s in range(1, n + 1):
            ws.cell(row=r, column=1, value=f"{g}-S{s}")
            ws.cell(row=r, column=2, value=g)
            for col in "CDEFGJ":
                ws[f"{col}{r}"].fill = INPUT
                ws[f"{col}{r}"].font = font(color="0000FF")
            e, f, gg = f"E{r}", f"F{r}", f"G{r}"
            bad = ",".join([f'AND({x}<>"",NOT(ISNUMBER({x})),{x}<>"{ABSENT}")' for x in (e, f, gg)]
                           + [f"AND(ISNUMBER({x}),{x}<0)" for x in (e, f, gg)])
            over = f"OR(AND(ISNUMBER({e}),{e}>$E$4),AND(ISNUMBER({f}),{f}>$F$4),AND(ISNUMBER({gg}),{gg}>$G$4))"
            missing = (f'"MISSING "&TRIM(IF({e}="","GD ","")&IF({f}="","mini project ","")'
                       f'&IF({gg}="","mock",""))')
            absent = (f'"{ABSENT} "&TRIM(IF({e}="{ABSENT}","GD ","")&IF({f}="{ABSENT}","mini project ","")'
                      f'&IF({gg}="{ABSENT}","mock",""))')
            nabs = f'COUNTIF({e}:{gg},"{ABSENT}")'
            ws[f"I{r}"] = (f'=IF(OR({bad}),"NOT A SCORE",IF({over},"OVER MAX",'
                           f'IF(COUNT({e}:{gg})+{nabs}<3,{missing},IF({nabs}>0,{absent},"COMPLETE"))))')
            ws[f"H{r}"] = f'=IF(I{r}="COMPLETE",{e}+{f}+{gg},"")'
            for col in "ABHI":
                ws[f"{col}{r}"].font = font()
            for col in "ABCDEFGHIJ":
                ws[f"{col}{r}"].border = BOX
            r += 1
    ws.freeze_panes = f"C{FIRST}"
    rng = f"I{FIRST}:I{last}"
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'I{FIRST}="COMPLETE"'],
                                                   fill=PatternFill("solid", fgColor="D9F2E3")))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'I{FIRST}<>"COMPLETE"'],
                                                   fill=PatternFill("solid", fgColor="FBE0DE")))
    subs = DataValidation(type="list", formula1='"1 revenue,2 bookings,3 billing,4 no-shows,5 campaign"',
                          allow_blank=True)
    panels = DataValidation(type="list", formula1='"the industry expert,the senior industry leader"',
                            allow_blank=True)
    ws.add_data_validation(subs)
    ws.add_data_validation(panels)
    subs.add(f"C{FIRST}:C{last}")
    panels.add(f"D{FIRST}:D{last}")
    for col in "EFG":
        dv = DataValidation(type="decimal", operator="between", formula1="0", formula2=f"${col}$4",
                            allow_blank=True, showErrorMessage=True, errorStyle="warning",
                            errorTitle="Above the event's maximum",
                            error="This score is outside 0 to the maximum in row 4. Check the signed sheet.")
        ws.add_data_validation(dv)
        dv.add(f"{col}{FIRST}:{col}{last}")

    # ---------------- By group ----------------
    bg = wb.create_sheet("By group")
    bg["A1"] = "By group: does every learner in each group hold three scores?"
    bg["A1"].font = font(bold=True, color=INK, size=13)
    header(bg, 3, ["Group", "Seats", "Seats complete", "Seats short", "Group status"], [10, 10, 16, 14, 30])
    for i, (g, _) in enumerate(GROUPS, start=4):
        bg[f"A{i}"] = g
        bg[f"B{i}"] = f'=COUNTIF(Scores!$B${FIRST}:$B${last},A{i})'
        bg[f"C{i}"] = f'=COUNTIFS(Scores!$B${FIRST}:$B${last},A{i},Scores!$I${FIRST}:$I${last},"COMPLETE")'
        bg[f"D{i}"] = f"=B{i}-C{i}"
        bg[f"E{i}"] = f'=IF(D{i}=0,"ALL COMPLETE",D{i}&" seat(s) short")'
        for col in "ABCDE":
            bg[f"{col}{i}"].font = font()
            bg[f"{col}{i}"].border = BOX

    # ---------------- Checks ----------------
    ck = wb.create_sheet("Checks")
    ck.column_dimensions["A"].width = 58
    ck.column_dimensions["B"].width = 34
    ck["A1"] = "Checks: every learner holds three scores, none above its maximum"
    ck["A1"].font = font(bold=True, color=INK, size=13)
    S = f"Scores!$I${FIRST}:$I${last}"
    checks = [
        ("Seats on the Scores sheet", f"=COUNTA(Scores!$A${FIRST}:$A${last})"),
        ("Seats that repeat another seat's label", f"=SUMPRODUCT((COUNTIF(Scores!$A${FIRST}:$A${last},Scores!$A${FIRST}:$A${last})>1)*1)"),
        ("Seats COMPLETE", f'=COUNTIF({S},"COMPLETE")'),
        ("Seats with a score MISSING", f'=COUNTIF({S},"MISSING*")'),
        ("Seats with a score OVER MAX", f'=COUNTIF({S},"OVER MAX")'),
        ("Seats with NOT A SCORE", f'=COUNTIF({S},"NOT A SCORE")'),
        ("GD scores still empty", f"=COUNTBLANK(Scores!$E${FIRST}:$E${last})"),
        ("Mini project scores still empty", f"=COUNTBLANK(Scores!$F${FIRST}:$F${last})"),
        ("Mock scores still empty", f"=COUNTBLANK(Scores!$G${FIRST}:$G${last})"),
        ("Seats with no sub-problem or no panel recorded", f'=COUNTBLANK(Scores!$C${FIRST}:$C${last})+COUNTBLANK(Scores!$D${FIRST}:$D${last})'),
        ("Seats with an event marked ABSENT", f'=COUNTIF({S},"{ABSENT}*")'),
    ]
    header(ck, 3, ["Check", "Count"])
    for i, (label, formula) in enumerate(checks, start=4):
        ck[f"A{i}"] = label
        ck[f"B{i}"] = formula
        ck[f"A{i}"].font = font()
        ck[f"B{i}"].font = font(bold=True)
        ck[f"A{i}"].border = ck[f"B{i}"].border = BOX
    A = f"Scores!$A${FIRST}:$A${last}"
    lists = [
        ("Seats short, by seat", f'_xlfn.TEXTJOIN(", ",TRUE,IF(({S}<>"COMPLETE")*(LEFT({S},6)<>"{ABSENT}"),{A},""))'),
        ("Seats with an absence, by seat", f'_xlfn.TEXTJOIN(", ",TRUE,IF(LEFT({S},6)="{ABSENT}",{A},""))'),
    ]
    first_list = 4 + len(checks)
    for i, (label, formula) in enumerate(lists, start=first_list):
        ck[f"A{i}"] = label
        ck[f"B{i}"] = ArrayFormula(f"B{i}", "=" + formula)
        ck[f"A{i}"].font = font()
        ck[f"B{i}"].font = font(bold=True)
        ck[f"B{i}"].alignment = Alignment(wrap_text=True, vertical="top")
        ck[f"A{i}"].border = ck[f"B{i}"].border = BOX
    SHORT, ABSENCES = f"B{first_list}", f"B{first_list + 1}"
    absent_row = 3 + len(checks)
    v = first_list + len(lists) + 1
    ck[f"A{v}"] = "Verdict"
    ck[f"A{v}"].font = font(bold=True, color=INK, size=12)
    ck[f"B{v}"] = (f'=IF(AND(B6+B{absent_row}=B4,B5=0,B8=0,B9=0),"READY TO SIGN",'
                   f'"NOT READY: "&(B4-B6-B{absent_row})&" seats short")')
    ck[f"B{v}"].font = font(bold=True, size=12)
    VERDICT = f"B{v}"

    # ---------------- Sign-off ----------------
    so = wb.create_sheet("Sign-off")
    so["A1"] = "Sign-off: each assessor role signs for its own column"
    so["A1"].font = font(bold=True, color=INK, size=13)
    header(so, 3, ["Role", "Signs for", "Signed", "Notes"], [40, 70, 10, 40])
    yes = DataValidation(type="list", formula1='"Yes"', allow_blank=True)
    so.add_data_validation(yes)
    for i, (role, what) in enumerate(SIGNERS, start=4):
        so[f"A{i}"] = role
        so[f"B{i}"] = what
        for col in "CD":
            so[f"{col}{i}"].fill = INPUT
            so[f"{col}{i}"].font = font(color="0000FF")
        so[f"A{i}"].font = so[f"B{i}"].font = font()
        for col in "ABCD":
            so[f"{col}{i}"].border = BOX
        yes.add(f"C{i}")
    end = 3 + len(SIGNERS)
    c = end + 2
    so[f"A{c}"] = "Closure"
    so[f"A{c}"].font = font(bold=True, color=INK, size=12)
    so[f"B{c}"] = (f'=IF(Checks!{VERDICT}<>"READY TO SIGN","NOT READY",'
                   f'IF(COUNTIF(C4:C{end},"Yes")={len(SIGNERS)},"CLOSED",'
                   f'"READY: awaiting "&({len(SIGNERS)}-COUNTIF(C4:C{end},"Yes"))&" sign-offs"))')
    so[f"B{c}"].font = font(bold=True, size=12)

    OUT.mkdir(parents=True, exist_ok=True)
    wb.save(OUT / BOOK)
    return last, VERDICT, c, end, SHORT, ABSENCES, f"B{absent_row}"


def manifest(last, verdict, closure, end, short, absences, absent_count):
    rows = range(FIRST, last + 1)
    full = []
    for r in rows:
        full += [f"{{sheet: Scores, cell: E{r}, value: 20}}", f"{{sheet: Scores, cell: F{r}, value: 30}}",
                 f"{{sheet: Scores, cell: G{r}, value: 20}}"]
    absent_mock = f"{{sheet: Scores, cell: G{last}, value: \"{ABSENT}\"}}"
    signs = [f"{{sheet: Sign-off, cell: C{r}, value: \"Yes\"}}" for r in range(4, end + 1)]
    lines = [
        "# Recalc manifest: the Build 1 grade closure workbook",
        "",
        "`scripts/xlsx_recalc.py` recalculates the workbook through LibreOffice, asserts the verdicts of",
        "the empty template, then flips entries and asserts that the checks move. Written by",
        "`internal/C2_W03_SAT_build_grade_closure_INTERNAL.py`; rebuild both together.",
        "",
        "```yaml",
        f"workbook: {BOOK}",
        "verdicts:",
        f"  - {{sheet: Checks, cell: {verdict}, expect: \"NOT READY: 35 seats short\"}}",
        f"  - {{sheet: Checks, cell: B4, expect: \"35\"}}",
        f"  - {{sheet: Checks, cell: {absences}, expect: \"\"}}",
        f"  - {{sheet: Scores, cell: I{FIRST}, expect: \"MISSING GD mini project mock\"}}",
        f"  - {{sheet: Sign-off, cell: B{closure}, expect: \"NOT READY\"}}",
        f"  - {{sheet: By group, cell: E12, expect: \"3 seat(s) short\"}}",
        "flips:",
        "  - name: one GD score above its maximum",
        f"    set: [{{sheet: Scores, cell: E{FIRST}, value: 31}}]",
        "    verdicts:",
        f"      - {{sheet: Scores, cell: I{FIRST}, expect: \"OVER MAX\"}}",
        "      - {sheet: Checks, cell: B8, expect: \"1\"}",
        "  - name: a word typed where a score belongs",
        f"    set: [{{sheet: Scores, cell: G{FIRST}, value: \"twenty\"}}]",
        "    verdicts:",
        f"      - {{sheet: Scores, cell: I{FIRST}, expect: \"NOT A SCORE\"}}",
        "  - name: every score entered, nobody signed",
        f"    set: [{', '.join(full)}]",
        "    verdicts:",
        f"      - {{sheet: Checks, cell: {verdict}, expect: \"READY TO SIGN\"}}",
        f"      - {{sheet: Scores, cell: H{FIRST}, expect: \"70\"}}",
        "      - {sheet: By group, cell: E12, expect: \"ALL COMPLETE\"}",
        f"      - {{sheet: Sign-off, cell: B{closure}, expect: \"READY: awaiting {len(SIGNERS)} sign-offs\"}}",
        "  - name: every score entered, one learner absent for the mock, nobody signed",
        f"    set: [{', '.join(full[:-1] + [absent_mock])}]",
        "    verdicts:",
        f"      - {{sheet: Scores, cell: I{last}, expect: \"{ABSENT} mock\"}}",
        f"      - {{sheet: Checks, cell: {absent_count}, expect: \"1\"}}",
        f"      - {{sheet: Checks, cell: {absences}, expect: \"G9-S3\"}}",
        f"      - {{sheet: Checks, cell: {verdict}, expect: \"READY TO SIGN\"}}",
        "  - name: G1-S1 still missing its mock",
        f"    set: [{', '.join(full[:2] + full[3:])}]",
        "    verdicts:",
        f"      - {{sheet: Checks, cell: {short}, expect: \"G1-S1\"}}",
        f"      - {{sheet: Checks, cell: {verdict}, expect: \"NOT READY: 1 seats short\"}}",
        "  - name: every score entered and every role signed",
        f"    set: [{', '.join(full + signs)}]",
        "    verdicts:",
        f"      - {{sheet: Sign-off, cell: B{closure}, expect: \"CLOSED\"}}",
        "```",
        "",
    ]
    (OUT / MANIFEST).write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    built = build()
    manifest(*built)
    last = built[0]
    print(f"wrote {OUT / BOOK} ({last - FIRST + 1} seats) and {OUT / MANIFEST}")

# Test inputs and expected outcomes (run scripts/xlsx_recalc.py content/W03/SAT after building).
# 1. The empty template: Checks verdict "NOT READY: 35 seats short"; seat G1-S1 reads
#    "MISSING GD mini project mock"; Sign-off closure "NOT READY"; By group G9 "3 seat(s) short".
# 2. G1-S1's GD set to 31: its status reads "OVER MAX" and the OVER MAX count reads 1.
# 3. G1-S1's mock set to "twenty": its status reads "NOT A SCORE".
# 3a. Every score entered but G9-S3's mock typed ABSENT: that seat reads "ABSENT mock", the absence
#     count reads 1, the absence list reads "G9-S3", and the verdict still reads "READY TO SIGN".
# 3b. Every score entered but G1-S1's mock: the short list reads "G1-S1" and the verdict reads
#     "NOT READY: 1 seats short".
# 4. Every seat given GD 20, mini project 30, mock 20: every total reads 70, the verdict reads
#    "READY TO SIGN", G9 reads "ALL COMPLETE", and closure reads "READY: awaiting 8 sign-offs".
# 5. As 4, with every Signed cell set to Yes: closure reads "CLOSED".

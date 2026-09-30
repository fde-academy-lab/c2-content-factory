"""Write Build 1's mini project scoring sheet and the recalc manifest that proves it computes.

    python3 content/W03/SAT/internal/C2_W03_SAT_build_mini_project_scoring_INTERNAL.py

Writes, beside each other in content/W03/SAT/rubrics/:
  C2_W03_SAT_mini_project_scoring_TRAINER.xlsx        nine groups and 35 seats, never a name
  C2_W03_SAT_mini_project_scoring_recalc_INTERNAL.md  the verdicts and flips scripts/xlsx_recalc.py asserts

The criteria are read from data/programme/facts.yaml (evaluation.rubrics.W03.events.mini-project),
which the requester approved on 29 September 2026, so rerunning this after a sync keeps the sheet
true. The first four criteria are scored once per group and every member receives them; presentation
and defence is scored per learner. The layout follows Friday's GD scoring sheet
(content/W03/D5/rubrics/C2_W03_D05_gd_scoring_sheet_TRAINER.xlsx), with 35 seats for the cohort's
35 learners (facts.yaml, cohort.students): eight groups of four and G9 of three, as the grade closure
workbook holds them, and an absent learner's seat marked N.
"""
import pathlib

import yaml
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parent / "rubrics"
BOOK = "C2_W03_SAT_mini_project_scoring_TRAINER.xlsx"
MANIFEST = "C2_W03_SAT_mini_project_scoring_recalc_INTERNAL.md"

facts = yaml.safe_load((ROOT / "data" / "programme" / "facts.yaml").read_text(encoding="utf-8"))
EVENT = facts["evaluation"]["rubrics"]["W03"]["events"]["mini-project"]
CRITERIA = EVENT["criteria"]
GROUP_CRITERIA, LEARNER_CRITERION = CRITERIA[:4], CRITERIA[4]
# The cohort's 35 learners in nine groups: eight of four and G9 of three, as in the closure workbook.
SEATS = [(f"G{g}", 4) for g in range(1, 9)] + [("G9", 3)]
assert sum(n for _, n in SEATS) == facts["cohort"]["students"]["value"]
GROUPS = [g for g, _ in SEATS]

ARIAL = "Arial"
INK = "1A0F5C"
HEAD = PatternFill("solid", fgColor=INK)
INPUT = PatternFill("solid", fgColor="FFF4B8")
thin = Side(style="thin", color="C9C3E6")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)


def font(bold=False, color="000000", size=10, italic=False):
    return Font(name=ARIAL, bold=bold, color=color, size=size, italic=italic)


def header(ws, row, labels, widths):
    for i, (text, w) in enumerate(zip(labels, widths), start=1):
        c = ws.cell(row=row, column=i, value=text)
        c.font = font(bold=True, color="FFFFFF")
        c.fill = HEAD
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = BOX
        ws.column_dimensions[c.column_letter].width = w


def inputs(ws, cells):
    for ref in cells:
        ws[ref].fill = INPUT
        ws[ref].font = font(color="0000FF")


def build():
    wb = Workbook()
    rm = wb.active
    rm.title = "Read me"
    rm.column_dimensions["A"].width = 120
    lines = [
        ("Build 1 mini project scoring sheet (TRAINER ONLY)", font(bold=True, color=INK, size=14)),
        ("", font()),
        (f"The rubric is Build 1's mini project rubric as the requester approved it on 29 September 2026, recorded in data/programme/facts.yaml (evaluation.rubrics.W03). {EVENT['scored']}", font()),
        ("Yellow cells with blue text are the inputs. On Groups: the sub-problem, the panel, the day, and the four group criteria. On Learners: whether the seat is in use and the presentation and defence score. Totals, checks and the summary are formulas.", font()),
        ("Score each group after its slot, never in front of it, from the panel's evidence notes and the question bank (content/W03/SAT/trainer/C2_W03_SAT_question_bank_TRAINER.md). A silent teammate's presentation and defence score waits for the separate question in the room's reserve.", font()),
        ("The demo rule on both expert days: a group's demo runs once, cold, on its raw files. If it fails, the group has two minutes to recover it live, as it would in front of a client. If it still fails, the group presents from its executed notebook, and the panel scores the live demo in presentation and defence as not run cold. The other 34 marks of the mini project are scored from the executed run, so a failed demo costs its own marks and never the analysis.", font()),
        ("The Learners sheet holds 35 seats, one per learner: eight groups of four and G9 of three. Relabel the seats if Monday's allocation put the group of three elsewhere. Mark an absent learner N in the In use column; the row then reads absent and drops out of the counts. An absence is recorded with the Programme Head's decision in the grade closure workbook.", font()),
        ("Each learner's total out of 40 is copied once into the grade closure workbook (C2_W03_SAT_grade_closure_TRAINER.xlsx, Scores, Mini project). Learner names go only into the copy the Programme Head keeps, never into the committed file, because the repository is public.", font()),
    ]
    for i, (text, f) in enumerate(lines, start=1):
        c = rm.cell(row=i, column=1, value=text)
        c.font = f
        c.alignment = Alignment(wrap_text=True, vertical="top")

    ru = wb.create_sheet("Rubric")
    ru["A1"] = f"Mini project rubric, {EVENT['marks']} marks per learner"
    ru["A1"].font = font(bold=True, color=INK, size=13)
    header(ru, 2, ["Criterion", "Marks", "What full marks look like", "Scored"], [30, 8, 90, 16])
    for i, (name, marks, full) in enumerate(CRITERIA, start=3):
        ru[f"A{i}"], ru[f"B{i}"], ru[f"C{i}"] = name, marks, full
        ru[f"D{i}"] = "per learner" if i == 3 + len(GROUP_CRITERIA) else "once per group"
        for col in "ABCD":
            ru[f"{col}{i}"].font = font()
            ru[f"{col}{i}"].border = BOX
            ru[f"{col}{i}"].alignment = Alignment(wrap_text=True, vertical="top")
    t = 3 + len(CRITERIA)
    ru[f"A{t}"] = "Total"
    ru[f"B{t}"] = f"=SUM(B3:B{t - 1})"
    ru[f"A{t + 1}"] = "Group part"
    ru[f"B{t + 1}"] = f"=SUM(B3:B{t - 2})"
    for ref in (f"A{t}", f"B{t}", f"A{t + 1}", f"B{t + 1}"):
        ru[ref].font = font(bold=True)
    ru[f"A{t + 3}"] = "Source: data/programme/facts.yaml, evaluation.rubrics.W03.events.mini-project, approved 29 September 2026."
    ru[f"A{t + 3}"].font = font(italic=True)
    RTOTAL, RGROUP, RLEARN = f"Rubric!$B${t}", f"Rubric!$B${t + 1}", f"Rubric!$B${t - 1}"

    gs = wb.create_sheet("Groups")
    gs["A1"] = "Groups: the four group criteria, scored once per group"
    gs["A1"].font = font(bold=True, color=INK, size=13)
    labels = (["Group", "Sub-problem", "Panel", "Day"]
              + [f"{n} (of {m})" for n, m, _ in GROUP_CRITERIA] + ["Group part (of 34)", "Check"])
    header(gs, 2, labels, [8, 16, 26, 12, 14, 14, 12, 12, 14, 30])
    subs = DataValidation(type="list", formula1='"1 revenue,2 bookings,3 billing,4 no-shows,5 campaign"', allow_blank=True)
    panels = DataValidation(type="list", formula1='"the industry expert,the senior industry leader"', allow_blank=True)
    day = DataValidation(type="list", formula1='"Friday,Saturday"', allow_blank=True)
    for dv in (subs, panels, day):
        gs.add_data_validation(dv)
    for i, g in enumerate(GROUPS, start=3):
        gs[f"A{i}"] = g
        inputs(gs, [f"{c}{i}" for c in "BCDEFGH"])
        subs.add(f"B{i}")
        panels.add(f"C{i}")
        day.add(f"D{i}")
        gs[f"I{i}"] = f'=IF(COUNT(E{i}:H{i})<4,"incomplete",SUM(E{i}:H{i}))'
        over = ",".join(f"{c}{i}>Rubric!$B${3 + k}" for k, c in enumerate("EFGH"))
        gs[f"J{i}"] = f'=IF(OR({over},MIN(E{i}:H{i})<0),"above a maximum or below zero","ok")'
        for c in "ABCDEFGHIJ":
            gs[f"{c}{i}"].border = BOX
        for c in "AIJ":
            gs[f"{c}{i}"].font = font()
    glast = 2 + len(GROUPS)

    ls = wb.create_sheet("Learners")
    ls["A1"] = "Learners: presentation and defence per learner, and each learner's total"
    ls["A1"].font = font(bold=True, color=INK, size=13)
    header(ls, 2, ["Group", "Seat", "In use (Y or N)", f"{LEARNER_CRITERION[0]} (of {LEARNER_CRITERION[1]})",
                   "Group part (of 34)", "Total (of 40)", "Check"], [8, 6, 12, 22, 14, 12, 30])
    yn = DataValidation(type="list", formula1='"Y,N"', allow_blank=False)
    ls.add_data_validation(yn)
    r = 3
    for g, n in SEATS:
        for s in range(1, n + 1):
            ls[f"A{r}"], ls[f"B{r}"], ls[f"C{r}"] = g, s, "Y"
            inputs(ls, [f"C{r}", f"D{r}"])
            yn.add(f"C{r}")
            ls[f"E{r}"] = f"=INDEX(Groups!$I$3:$I${glast},MATCH(A{r},Groups!$A$3:$A${glast},0))"
            ls[f"F{r}"] = (f'=IF(C{r}="N","absent",IF(OR(NOT(ISNUMBER(D{r})),NOT(ISNUMBER(E{r}))),'
                           f'"incomplete",D{r}+E{r}))')
            ls[f"G{r}"] = (f'=IF(AND(ISNUMBER(D{r}),OR(D{r}>{RLEARN},D{r}<0)),'
                           f'"above a maximum or below zero","ok")')
            for c in "ABCDEFG":
                ls[f"{c}{r}"].border = BOX
            for c in "ABEFG":
                ls[f"{c}{r}"].font = font()
            r += 1
    llast = r - 1

    sm = wb.create_sheet("Summary")
    sm["A1"] = "Summary"
    sm["A1"].font = font(bold=True, color=INK, size=13)
    header(sm, 2, ["What", "Result"], [60, 60])
    rows = [
        ("Seats in use", f'=COUNTIF(Learners!C3:C{llast},"Y")'),
        ("Learners fully scored", f"=COUNT(Learners!F3:F{llast})"),
        ("Groups with all four group criteria scored", f"=COUNT(Groups!I3:I{glast})"),
        ("Scores above a criterion's maximum or below zero",
         f'=COUNTIF(Groups!J3:J{glast},"above*")+COUNTIF(Learners!G3:G{llast},"above*")'),
        ("Rubric total checks", f'=IF({RTOTAL}=40,"the rubric adds to 40","the rubric adds to "&{RTOTAL}&", not 40")'),
        ("Group part checks", f'=IF({RGROUP}=34,"the group part adds to 34","the group part adds to "&{RGROUP}&", not 34")'),
    ]
    for i, (a, b) in enumerate(rows, start=3):
        sm[f"A{i}"], sm[f"B{i}"] = a, b
        sm[f"A{i}"].font = font()
        sm[f"B{i}"].font = font(bold=True)
    v = 3 + len(rows)
    sm[f"A{v}"] = "Verdict"
    sm[f"A{v}"].font = font(bold=True, color=INK, size=12)
    sm[f"B{v}"] = ('=IF(B6>0,B6&" score(s) outside the rubric",'
                   'IF(B4=B3,"every learner in use is scored",B3-B4&" learners still to score"))')
    sm[f"B{v}"].font = font(bold=True, size=12)

    OUT.mkdir(parents=True, exist_ok=True)
    wb.save(OUT / BOOK)
    return v, llast


def manifest(v, llast):
    groups = []
    for i in range(3, 12):
        groups += [f"{{sheet: Groups, cell: E{i}, value: 6}}", f"{{sheet: Groups, cell: F{i}, value: 8}}",
                   f"{{sheet: Groups, cell: G{i}, value: 7}}", f"{{sheet: Groups, cell: H{i}, value: 5}}"]
    learners = [f"{{sheet: Learners, cell: D{r}, value: 4}}" for r in range(3, llast + 1)]
    lines = [
        "# Recalc manifest: the Build 1 mini project scoring sheet",
        "",
        "`scripts/xlsx_recalc.py` recalculates the sheet through LibreOffice, asserts the empty template,",
        "then flips entries and asserts that the totals and checks move. Written by",
        "`internal/C2_W03_SAT_build_mini_project_scoring_INTERNAL.py`; rebuild both together.",
        "",
        "```yaml",
        f"workbook: {BOOK}",
        "verdicts:",
        "  - {sheet: Rubric, cell: B8, expect: \"40\"}",
        "  - {sheet: Rubric, cell: B9, expect: \"34\"}",
        f"  - {{sheet: Summary, cell: B{v}, expect: \"35 learners still to score\"}}",
        "  - {sheet: Learners, cell: F3, expect: \"incomplete\"}",
        "flips:",
        "  - name: G1 scored as a group, one member scored alone",
        "    set: [{sheet: Groups, cell: E3, value: 6}, {sheet: Groups, cell: F3, value: 8}, {sheet: Groups, cell: G3, value: 7}, {sheet: Groups, cell: H3, value: 5}, {sheet: Learners, cell: D3, value: 4}]",
        "    verdicts:",
        "      - {sheet: Groups, cell: I3, expect: \"26\"}",
        "      - {sheet: Learners, cell: F3, expect: \"30\"}",
        "      - {sheet: Learners, cell: F4, expect: \"incomplete\"}",
        "  - name: a group criterion above its maximum",
        "    set: [{sheet: Groups, cell: F3, value: 11}]",
        "    verdicts:",
        "      - {sheet: Groups, cell: J3, expect: \"above a maximum or below zero\"}",
        f"      - {{sheet: Summary, cell: B{v}, expect: \"1 score(s) outside the rubric\"}}",
        f"  - name: an absent learner's seat marked unused",
        f"    set: [{{sheet: Learners, cell: C{llast}, value: \"N\"}}]",
        "    verdicts:",
        f"      - {{sheet: Learners, cell: F{llast}, expect: \"absent\"}}",
        "      - {sheet: Summary, cell: B3, expect: \"34\"}",
        "  - name: every group and every learner scored",
        f"    set: [{', '.join(groups + learners)}]",
        "    verdicts:",
        f"      - {{sheet: Summary, cell: B{v}, expect: \"every learner in use is scored\"}}",
        f"      - {{sheet: Learners, cell: F{llast}, expect: \"30\"}}",
        "```",
        "",
    ]
    (OUT / MANIFEST).write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    v, llast = build()
    manifest(v, llast)
    print(f"wrote {OUT / BOOK} and {OUT / MANIFEST}")

# Test inputs and expected outcomes (run scripts/xlsx_recalc.py content/W03/SAT after building).
# 1. The empty template: Rubric totals read 40 and 34; Summary verdict "35 learners still to score".
# 2. G1 scored 6, 8, 7 and 5 as a group and its first member 4: group part 26, that learner 30,
#    the second member still "incomplete".
# 3. A group criterion typed as 11 where the maximum is 10: the row's check and the verdict flag it.
# 4. G9's last seat (G9-S3) set to N for an absence: it reads "absent" and seats in use drop to 34.
# 5. Every group scored 26 and every learner 4: verdict "every learner in use is scored".

"""Write Mock R1's roster and scoring sheet, and the recalc manifests that prove both compute.

    python3 content/W03/D4/internal/C2_W03_D04_build_workbooks_INTERNAL.py

Writes four files into content/W03/D4/:
  mocks/C2_W03_D04_roster_TRAINER.xlsx               who sits when, with whom, on which questions
  mocks/C2_W03_D04_roster_recalc_INTERNAL.md          the verdicts and flips scripts/xlsx_recalc.py asserts
  rubrics/C2_W03_D04_mock_scoring_sheet_TRAINER.xlsx  one row per learner seat, never a name
  rubrics/C2_W03_D04_mock_scoring_recalc_INTERNAL.md  the same, for the scoring sheet

The six criteria and their maximums are read from data/programme/facts.yaml
(evaluation.rubrics.W03.events.mock), which the requester approved on 29 September 2026, so a rerun
after a sync keeps both sheets true. The seats are the cohort's 35 learners (facts.yaml,
cohort.students) in its nine groups (cohort.build_groups), eight of four and G9 of three, the
default every Build 1 workbook uses until Monday's allocation. The technical sets and the swaps
follow the question bank, mocks/C2_W03_D04_mock_question_bank_TRAINER.md, and the slot arithmetic
follows the day sheet. Every computed cell is a formula LibreOffice evaluates, and xlsx_recalc.py
recalculates both workbooks after this script has written them.
"""
import pathlib

import yaml
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
ROOT = HERE.parents[3]
ROSTER = DAY / "mocks" / "C2_W03_D04_roster_TRAINER.xlsx"
ROSTER_MANIFEST = DAY / "mocks" / "C2_W03_D04_roster_recalc_INTERNAL.md"
SCORES = DAY / "rubrics" / "C2_W03_D04_mock_scoring_sheet_TRAINER.xlsx"
SCORES_MANIFEST = DAY / "rubrics" / "C2_W03_D04_mock_scoring_recalc_INTERNAL.md"

facts = yaml.safe_load((ROOT / "data" / "programme" / "facts.yaml").read_text(encoding="utf-8"))
MOCK = facts["evaluation"]["rubrics"]["W03"]["events"]["mock"]
CRITERIA = MOCK["criteria"]
assert len(CRITERIA) == 6 and sum(m for _, _, m in CRITERIA) == MOCK["marks"] == 30
GROUPS = [(f"G{g}", 4) for g in range(1, 9)] + [("G9", 3)]
assert sum(n for _, n in GROUPS) == facts["cohort"]["students"]["value"]
assert len(GROUPS) == facts["cohort"]["build_groups"]["value"]
ASSESSORS = [("Programme Head", "in person"), ("Academic TA", "in person"), ("Principal Advisor", "online")]
SETS = {"A": ("T01-L1", "T04-L2", "T07-L3"), "B": ("T02-L1", "T05-L2", "T08-L3"),
        "C": ("T03-L1", "T06-L2", "T09-L3"), "D": ("T04-L1", "T07-L2", "T10-L3"),
        "E": ("T05-L1", "T08-L2", "T01-L3"), "F": ("T06-L1", "T09-L2", "T02-L3"),
        "G": ("T07-L1", "T10-L2", "T03-L3"), "H": ("T08-L1", "T01-L2", "T04-L3")}
SWAPS = [("T04-L2", "4", "T02-L2"), ("T07-L2", "3", "T02-L2"), ("T09-L2", "3", "T02-L2"),
         ("T04-L3", "5", "T05-L3")]
SUBPROBLEMS = ["1 revenue", "2 bookings", "3 billing", "4 no-shows", "5 campaign"]
# This pack's reading of the approved rubric, as the assessors' guide prints it; it sets no marks.
FULL_MARKS = [
    "All three answers reach the model answer's point, with the mechanism behind the number named",
    "Uses the question's numbers unprompted, each with its denominator, and works out at least one",
    "Moves one step past the first answer on all three follow-ups",
    "Maps the asker's words to the Week 1 or 2 move in their own words, defends one decision with a "
    "count or dollars and its alternative, and shows the cell",
    "Holds the caveat with a number, says what would change it and what to check next, without "
    "dropping it or overclaiming",
    "Names a step from their own log entry, with the time or error it would have saved",
]

HEAD = PatternFill("solid", fgColor="D9D9D9")
INPUT = PatternFill("solid", fgColor="FFF4C2")
WRAP = Alignment(vertical="top", wrap_text=True)


def put(ws, ref, value, fill=None, blue=False, bold=False):
    c = ws[ref]
    c.value = value
    c.font = Font(name="Arial", size=10, color="0000FF" if blue else None, bold=bold)
    c.alignment = WRAP
    if fill is not None:
        c.fill = fill
    return c


def header(ws, row, names):
    for i, name in enumerate(names):
        put(ws, f"{chr(65 + i)}{row}", name, HEAD, bold=True)


def widths(ws, cols):
    for col, w in cols.items():
        ws.column_dimensions[col].width = w


def build_roster():
    wb = Workbook()
    rm = wb.active
    rm.title = "Read me"
    widths(rm, {"A": 120})
    notes = {
        1: "Mock R1 roster, Build 1 (TRAINER ONLY)",
        2: "Seats and groups, never names. Durations only: every time is a minute inside a 180-minute block.",
        4: "Which cells do you edit?",
        5: ("Yellow cells with blue text are the inputs: the slot, changeover, huddle and close minutes on "
            "Settings; each group's sub-problem on Groups, chosen from its list after Monday's allocation; "
            "and each seat's present flag on Seats. Every other cell is a formula."),
        7: "How does the default work?",
        8: ("35 seats in nine groups, eight of four and G9 of three, as data/programme/facts.yaml states the "
            "cohort. The Programme Head changes the group sizes on Seats if Monday's allocation differs."),
        9: ("The call order on Seats takes seat 1 of every group, then seat 2 of every group, and so on, and each "
            "slot fills the three assessors in call order, so the three learners out at once come from three "
            "different groups and every group keeps building while one member is out."),
        10: ("The Programme Head and the Academic TA take 12 learners each in person, and the Principal Advisor "
             "takes 11 online and holds the spare slot at the end of the day. Each assessor meets every member "
             "of the same three groups: the Programme Head G1, G4 and G7, the Academic TA G2, G5 and G8, and the "
             "Principal Advisor G3, G6 and G9, so work carried for a group-mate shows against the others' answers."),
        11: ("Each seat's set letter picks its three technical questions from the Sets sheet, consecutive letters "
             "within a group, so no two group-mates meet the same set. Its seat number picks its viva probe: seat "
             "1 takes P1. Where a set's question sits close to the group's own sub-problem, the Sets sheet's swap "
             "table puts the reserve in its place, and the Seats, Roster and Grid sheets print the swapped question."),
        12: "Print the Grid sheet for the huddle: one row per slot, one column per assessor.",
        14: "What moves when a learner is absent?",
        15: ("Known before the day: set that seat's present flag to no. The queue closes up and the day ends one "
             "slot sooner for one assessor. Then read the clash count on Settings: above zero means two group-mates "
             "now share a slot, so swap two rows' call order on Seats until it reads zero."),
        16: ("Found on the day: do not edit the workbook. The absent learner's slot becomes a free slot for that "
             "assessor. A learner who arrives later takes the spare slot or the first free slot, and a learner "
             "absent all day is listed for a make-up, which the Programme Head schedules."),
        18: "What moves when an assessor is out?",
        19: ("The grid assumes three assessors. If one is out for part of the day, their learners move first to the "
             "other two assessors' free and spare slots, then to the open build time after the second block. The "
             "day sheet carries this plan."),
    }
    for row, text in notes.items():
        put(rm, f"A{row}", text, bold=text.endswith("?") or row == 1)

    st = wb.create_sheet("Settings")
    widths(st, {"A": 44, "B": 30, "C": 18, "D": 18, "E": 22})
    put(st, "A1", "Settings and the day's verdict", bold=True)
    inputs = [(3, "Mock slot, minutes", 20, "The row: roughly 20 minutes each."),
              (4, "Changeover, minutes", 5, "The assessor finishes the evidence note and enters the marks."),
              (5, "Block length, minutes", 180, "data/programme/facts.yaml: two blocks of 180 minutes."),
              (6, "Assessors' huddle at the start of block 1, minutes", 10, "Calibration before the first mock."),
              (7, "Close at the end of block 2, minutes", 15, "The row: the close-out, 15 minutes.")]
    for row, label, value, note in inputs:
        put(st, f"A{row}", label)
        put(st, f"B{row}", value, INPUT, blue=True)
        put(st, f"C{row}", note)
    computed = [(8, "One slot and its changeover, minutes", "=B3+B4"),
                (9, "Slots per assessor in block 1", "=INT((B5-B6)/B8)"),
                (10, "Slots per assessor in block 2", "=INT((B5-B7)/B8)"),
                (11, "Slots per assessor in the day", "=B9+B10"),
                (12, "Assessors", 3),
                (13, "Mock places in the day", "=B11*B12"),
                (14, "Learners present", '=COUNTIF(Seats!G2:G36,"yes")'),
                (15, "Spare places", "=B13-B14"),
                (16, "Verdict", '=IF(B14<=B13,"fits: "&B13&" slots for "&B14&" learners",'
                                '"does not fit: "&(B14-B13)&" learners without a slot")'),
                (17, "Last mock of the day ends at",
                 '=IF(B14>B13,"after the day",IF(ROUNDUP(B14/B12,0)<=B9,"block 1, minute "&(B6+ROUNDUP(B14/B12,0)*B8-B4),'
                 '"block 2, minute "&((ROUNDUP(B14/B12,0)-B9)*B8-B4)))'),
                (18, "Close starts at", '="block 2, minute "&(B5-B7)'),
                (19, "Slots where two group-mates are out at once", '=COUNTIF(Roster!L2:L43,"yes")'),
                (20, "Assessor minutes in mocks", "=B14*B3")]
    for row, label, formula in computed:
        put(st, f"A{row}", label)
        put(st, f"B{row}", formula)
    put(st, "C19", "Zero by default. Above zero after an absence: swap call orders on Seats.")
    put(st, "A22", "Load per assessor", bold=True)
    header(st, 23, ["Assessor", "Mode", "Learners", "Minutes in mocks", "Last mock ends at"])
    for i, (name, mode) in enumerate(ASSESSORS):
        r = 24 + i
        put(st, f"A{r}", name)
        put(st, f"B{r}", mode)
        put(st, f"C{r}", f'=COUNTIFS(Roster!B2:B43,A{r},Roster!H2:H43,"G*")')
        put(st, f"D{r}", f"=C{r}*$B$3")
        last = f'_xlfn.MAXIFS(Roster!M2:M43,Roster!B2:B43,A{r},Roster!H2:H43,"G*")'
        put(st, f"E{r}", f'=IF(C{r}=0,"no mocks",IF({last}>$B$5,"block 2, minute "&({last}-$B$5),'
                         f'"block 1, minute "&{last}))')
    put(st, "A27", "Total")
    put(st, "C27", "=SUM(C24:C26)")
    put(st, "D27", "=SUM(D24:D26)")

    sets = wb.create_sheet("Sets")
    widths(sets, {"A": 8, "B": 12, "C": 12, "D": 12, "F": 16, "G": 14, "I": 90})
    header(sets, 1, ["Set", "L1, the move", "L2, the number", "L3, the judgement"])
    for i, (letter, qs) in enumerate(SETS.items()):
        put(sets, f"A{i + 2}", letter)
        for j, q in enumerate(qs):
            put(sets, f"{'BCD'[j]}{i + 2}", q)
    put(sets, "F1", "Swap key", HEAD, bold=True)
    put(sets, "G1", "Ask instead", HEAD, bold=True)
    for i, (q, sub, instead) in enumerate(SWAPS):
        put(sets, f"F{i + 2}", f"{q}|{sub}")
        put(sets, f"G{i + 2}", instead)
    put(sets, "I1", "What the two tables do", HEAD, bold=True)
    put(sets, "I2", ("A swap key is a question and the first digit of a group's sub-problem. When a seat's set "
                     "holds that question and its group took that sub-problem, the seat is asked the reserve "
                     "beside it, so the technical half never rehearses the learner's own viva."))
    put(sets, "I3", "The reserves are T09-L1, T10-L1, T02-L2, T03-L2, T05-L3 and T06-L3.")
    put(sets, "I4", "T03-L2 is never asked of a learner whose group took sub-problem 2.")

    gr = wb.create_sheet("Groups")
    widths(gr, {"A": 8, "B": 30, "C": 10, "D": 10, "E": 14, "F": 20})
    header(gr, 1, ["Group", "Sub-problem (choose after Monday)", "Seats", "Present", "Mocks placed", "Assessor"])
    dv = DataValidation(type="list", formula1='"' + ",".join(SUBPROBLEMS) + '"', allow_blank=True)
    gr.add_data_validation(dv)
    for i, (g, _) in enumerate(GROUPS):
        r = i + 2
        put(gr, f"A{r}", g)
        put(gr, f"B{r}", None, INPUT, blue=True)
        dv.add(f"B{r}")
        put(gr, f"C{r}", f"=COUNTIF(Seats!B$2:B$36,A{r})")
        put(gr, f"D{r}", f'=COUNTIFS(Seats!B$2:B$36,A{r},Seats!G$2:G$36,"yes")')
        put(gr, f"E{r}", f"=COUNTIF(Roster!I$2:I$43,A{r})")
        put(gr, f"F{r}", ASSESSORS[i % 3][0])
    put(gr, "A11", "Total")
    put(gr, "C11", "=SUM(C2:C10)")
    put(gr, "D11", "=SUM(D2:D10)")
    put(gr, "E11", "=SUM(E2:E10)")

    se = wb.create_sheet("Seats")
    widths(se, {c: 12 for c in "ABCDEFGHIJKL"})
    se.column_dimensions["F"].width = 18
    header(se, 1, ["Call order", "Group", "Seat", "Seat label", "Set", "Sub-problem", "Present",
                   "Queue position", "Viva probe", "L1", "L2", "L3"])
    queue = [(g, s) for s in range(1, 5) for g, n in GROUPS if s <= n]
    for i, (g, s) in enumerate(queue):
        r = i + 2
        put(se, f"A{r}", i + 1)
        put(se, f"B{r}", g)
        put(se, f"C{r}", s)
        put(se, f"D{r}", f'=B{r}&"-S"&C{r}')
        put(se, f"E{r}", f'=MID("ABCDEFGH",MOD(VALUE(MID(B{r},2,2))+C{r}-2,8)+1,1)')
        put(se, f"F{r}", f'=IF(INDEX(Groups!B$2:B$10,VALUE(MID(B{r},2,2)))="","allocate on Monday",'
                         f'INDEX(Groups!B$2:B$10,VALUE(MID(B{r},2,2))))')
        put(se, f"G{r}", "yes", INPUT, blue=True)
        put(se, f"H{r}", f'=IF(G{r}="yes",COUNTIFS(G$2:G$36,"yes",A$2:A$36,"<="&A{r}),"")')
        put(se, f"I{r}", f'="P"&C{r}')
        for col, src in (("J", "B"), ("K", "C"), ("L", "D")):
            base = f"INDEX(Sets!{src}$2:{src}$9,MATCH(E{r},Sets!A$2:A$9,0))"
            put(se, f"{col}{r}", f'=IFERROR(INDEX(Sets!G$2:G$5,MATCH({base}&"|"&LEFT(F{r},1),Sets!F$2:F$5,0)),{base})')

    ro = wb.create_sheet("Roster")
    cols = ["Slot", "Assessor", "Mode", "Block", "Starts, minute of block", "Ends, minute of block",
            "Queue position", "Seat", "Group", "Set", "Sub-problem", "Group-mate in same slot",
            "Ends, minute of day", "Viva probe", "L1", "L2", "L3", "Grid text"]
    header(ro, 1, cols)
    widths(ro, {chr(65 + i): 14 for i in range(len(cols))})
    ro.column_dimensions["R"].width = 44
    look = "MATCH(G{r},Seats!$H$2:$H$36,0)"
    for slot in range(1, 15):
        for a, (name, mode) in enumerate(ASSESSORS):
            r = 1 + (slot - 1) * 3 + a + 1
            m = look.format(r=r)
            put(ro, f"A{r}", slot)
            put(ro, f"B{r}", name)
            put(ro, f"C{r}", mode)
            put(ro, f"D{r}", f'=IF(A{r}<=Settings!$B$9,1,IF(A{r}<=Settings!$B$11,2,"none"))')
            put(ro, f"E{r}", f'=IF(D{r}=1,Settings!$B$6+(A{r}-1)*Settings!$B$8,'
                             f'IF(D{r}=2,(A{r}-Settings!$B$9-1)*Settings!$B$8,""))')
            put(ro, f"F{r}", f'=IF(E{r}="","",E{r}+Settings!$B$3)')
            put(ro, f"G{r}", f"=(A{r}-1)*Settings!$B$12+{a + 1}")
            put(ro, f"H{r}", f'=IF(D{r}="none","outside the day",IF(ISNUMBER({m}),INDEX(Seats!$D$2:$D$36,{m}),"spare"))')
            put(ro, f"I{r}", f'=IF(LEFT(H{r},1)="G",INDEX(Seats!$B$2:$B$36,{m}),"")')
            for col, src in (("J", "E"), ("K", "F"), ("N", "I"), ("O", "J"), ("P", "K"), ("Q", "L")):
                put(ro, f"{col}{r}", f'=IF(I{r}="","",INDEX(Seats!${src}$2:${src}$36,{m}))')
            put(ro, f"L{r}", f'=IF(I{r}="","",IF(COUNTIFS($A$2:$A$43,A{r},$I$2:$I$43,I{r})>1,"yes","no"))')
            put(ro, f"M{r}", f'=IF(D{r}=1,F{r},IF(D{r}=2,Settings!$B$5+F{r},""))')
            put(ro, f"R{r}", f'=IF(I{r}="",H{r},H{r}&", set "&J{r}&", "&N{r}&": "&O{r}&", "&P{r}&", "&Q{r})')

    gd = wb.create_sheet("Grid")
    header(gd, 1, ["Slot", "Block", "Starts", "Ends", "Programme Head, in person", "Academic TA, in person",
                   "Principal Advisor, online"])
    widths(gd, {"A": 6, "B": 7, "C": 8, "D": 8, "E": 44, "F": 44, "G": 44})
    for slot in range(1, 15):
        r = slot + 1
        put(gd, f"A{r}", slot)
        first = (slot - 1) * 3 + 2
        put(gd, f"B{r}", f"=Roster!D{first}")
        put(gd, f"C{r}", f"=Roster!E{first}")
        put(gd, f"D{r}", f"=Roster!F{first}")
        for a, col in enumerate("EFG"):
            put(gd, f"{col}{r}", f"=Roster!R{first + a}")
    wb.save(ROSTER)


def build_scores():
    wb = Workbook()
    rm = wb.active
    rm.title = "Read me"
    widths(rm, {"A": 120})
    notes = {
        1: "Mock R1 scoring sheet, Build 1 (TRAINER ONLY)",
        2: "Seats and groups, never names. One shared copy; each assessor scores only their own rows.",
        4: "Which cells do you edit?",
        5: ("On Scores, the six yellow mark cells of a learner's row, entered in the changeover straight after the "
            "mock, from the evidence note. The assessor column follows the roster's default split and changes "
            "only if a learner was moved to another assessor. Every other cell is a formula."),
        7: "Where do the criteria come from?",
        8: ("The Criteria sheet copies the mock rubric the requester approved on 29 September 2026, held in "
            "data/programme/facts.yaml: 15 marks on the technical half and 15 on the project viva, 30 in all. "
            "If facts.yaml changes, rerun content/W03/D4/internal/C2_W03_D04_build_workbooks_INTERNAL.py rather "
            "than editing the sheet by hand. Its last column is this pack's reading of each criterion, the same "
            "words as the assessors' guide, and it sets no marks."),
        10: "What does the status column say?",
        11: ("not scored: no mark entered yet. incomplete: some marks entered, some missing. scored: all six entered, "
             "each within its maximum. check: a mark is above its maximum, so fix it before anything else is read."),
        13: "Which two checks run at the close?",
        14: ("The Assessors sheet shows each assessor's average on each half. A gap of more than two marks between "
             "assessors on one half is discussed at the close, one sentence each, before any mark moves, and a mark "
             "changes only against its evidence note. The Groups sheet shows each group's average, which the close "
             "reads for patterns and never announces."),
        16: "What is the Example sheet?",
        17: ("One learner's marks with the same formulas, so the format is visible before the first mock. It feeds "
             "no total on any other sheet."),
    }
    for row, text in notes.items():
        put(rm, f"A{row}", text, bold=text.endswith("?") or row == 1)

    cr = wb.create_sheet("Criteria")
    widths(cr, {"A": 7, "B": 14, "C": 52, "D": 10, "E": 90})
    header(cr, 1, ["Code", "Half", "Criterion", "Maximum", "Full marks look like (this pack's reading)"])
    for i, ((half, name, marks), reading) in enumerate(zip(CRITERIA, FULL_MARKS)):
        r = i + 2
        put(cr, f"A{r}", f"C{i + 1}")
        put(cr, f"B{r}", half)
        put(cr, f"C{r}", name)
        put(cr, f"D{r}", marks)
        put(cr, f"E{r}", reading)
    put(cr, "C9", "Technical half")
    put(cr, "D9", '=SUMIF(B2:B7,"Technical",D2:D7)')
    put(cr, "C10", "Project viva")
    put(cr, "D10", '=SUMIF(B2:B7,"Project viva",D2:D7)')
    put(cr, "C11", "The mock")
    put(cr, "D11", "=SUM(D2:D7)")
    put(cr, "C12", "Matches the approved 30 marks")
    put(cr, "D12", f'=IF(D11={MOCK["marks"]},"yes","no: rebuild from facts.yaml")')

    names = ["Seat", "Group", "Assessor"] + [f"C{i + 1} {name} (/{marks})" for i, (_, name, marks) in enumerate(CRITERIA)] \
        + ["Technical (/15)", "Viva (/15)", "Mock (/30)", "Status"]

    def score_row(ws, r, seat, group, assessor, marks=None):
        put(ws, f"A{r}", seat)
        put(ws, f"B{r}", group)
        put(ws, f"C{r}", assessor, INPUT, blue=True)
        for j, col in enumerate("DEFGHI"):
            put(ws, f"{col}{r}", None if marks is None else marks[j], INPUT, blue=True)
        put(ws, f"J{r}", f'=IF(COUNT(D{r}:F{r})=0,"",SUM(D{r}:F{r}))')
        put(ws, f"K{r}", f'=IF(COUNT(G{r}:I{r})=0,"",SUM(G{r}:I{r}))')
        put(ws, f"L{r}", f'=IF(COUNT(D{r}:I{r})=6,SUM(D{r}:I{r}),"")')
        over = "+".join(f"({col}{r}>Criteria!$D${k + 2})" for k, col in enumerate("DEFGHI"))
        put(ws, f"M{r}", f'=IF(({over})>0,"check: a mark is above its maximum",IF(COUNT(D{r}:I{r})=0,"not scored",'
                         f'IF(COUNT(D{r}:I{r})<6,"incomplete","scored")))')

    sc = wb.create_sheet("Scores")
    header(sc, 1, names)
    widths(sc, {"A": 8, "B": 7, "C": 18, **{c: 15 for c in "DEFGHI"}, "J": 11, "K": 11, "L": 11, "M": 34})
    dv = DataValidation(type="decimal", operator="between", formula1="0", formula2="8", allow_blank=True)
    sc.add_data_validation(dv)
    r = 2
    for gi, (g, n) in enumerate(GROUPS):
        for s in range(1, n + 1):
            score_row(sc, r, f"{g}-S{s}", g, ASSESSORS[gi % 3][0])
            r += 1
    dv.add(f"D2:I{r - 1}")
    last = r - 1
    assert last == 36

    asr = wb.create_sheet("Assessors")
    header(asr, 1, ["Assessor", "Learners", "Scored", "Average technical (/15)", "Average viva (/15)",
                    "Average mock (/30)"])
    widths(asr, {"A": 44, "B": 30, "C": 10, "D": 22, "E": 20, "F": 20})
    for i, (name, _) in enumerate(ASSESSORS):
        r = i + 2
        put(asr, f"A{r}", name)
        put(asr, f"B{r}", f"=COUNTIF(Scores!C2:C{last},A{r})")
        put(asr, f"C{r}", f'=COUNTIFS(Scores!C2:C{last},A{r},Scores!M2:M{last},"scored")')
        for col, src in (("D", "J"), ("E", "K"), ("F", "L")):
            put(asr, f"{col}{r}", f'=IF(C{r}=0,"",ROUND(AVERAGEIFS(Scores!{src}2:{src}{last},Scores!C2:C{last},A{r},'
                                  f'Scores!M2:M{last},"scored"),1))')
    rows = [(6, "Learners scored", f'=COUNTIF(Scores!M2:M{last},"scored")&" of "&COUNTA(Scores!A2:A{last})&" scored"'),
            (7, "Rows to fix", f'=COUNTIF(Scores!M2:M{last},"check*")'),
            (8, "Largest gap between assessors, technical", '=IF(COUNT(D2:D4)<2,"",MAX(D2:D4)-MIN(D2:D4))'),
            (9, "Largest gap between assessors, viva", '=IF(COUNT(E2:E4)<2,"",MAX(E2:E4)-MIN(E2:E4))'),
            (10, "Calibration", '=IF(COUNT(D2:E4)<4,"too few scores to compare",IF(MAX(B8:B9)>2,'
                                '"discuss at the close: a gap above two marks","within two marks"))')]
    for r, label, formula in rows:
        put(asr, f"A{r}", label)
        put(asr, f"B{r}", formula)

    gs = wb.create_sheet("Groups")
    header(gs, 1, ["Group", "Members", "Scored", "Average mock (/30)"])
    widths(gs, {"A": 8, "B": 10, "C": 10, "D": 20})
    for i, (g, _) in enumerate(GROUPS):
        r = i + 2
        put(gs, f"A{r}", g)
        put(gs, f"B{r}", f"=COUNTIF(Scores!B2:B{last},A{r})")
        put(gs, f"C{r}", f'=COUNTIFS(Scores!B2:B{last},A{r},Scores!M2:M{last},"scored")')
        put(gs, f"D{r}", f'=IF(C{r}=0,"",ROUND(AVERAGEIFS(Scores!L2:L{last},Scores!B2:B{last},A{r},'
                         f'Scores!M2:M{last},"scored"),1))')

    ex = wb.create_sheet("Example")
    header(ex, 1, names)
    widths(ex, {"A": 8, "B": 7, "C": 18, **{c: 15 for c in "DEFGHI"}, "J": 11, "K": 11, "L": 11, "M": 34})
    score_row(ex, 2, "G1-S1", "G1", "Programme Head", [6, 3, 2, 5, 4, 2])
    put(ex, "A4", "A worked row for the format only. It feeds no total on any other sheet.")
    wb.save(SCORES)


ROSTER_YAML = """# How does Mock R1's roster prove it computes, and that its verdicts move?

Read by `scripts/xlsx_recalc.py`. It recalculates the roster through LibreOffice, asserts the day's
verdicts as shipped, then changes one input at a time and asserts that the verdicts move. The
workbook is written by `content/W03/D4/internal/C2_W03_D04_build_workbooks_INTERNAL.py`.

```yaml
workbook: C2_W03_D04_roster_TRAINER.xlsx
verdicts:
  - {sheet: Settings, cell: B16, expect: "fits: 36 slots for 35 learners"}
  - {sheet: Settings, cell: B17, expect: "block 2, minute 145"}
  - {sheet: Settings, cell: B19, expect: "0"}
  - {sheet: Settings, cell: C27, expect: "35"}
  - {sheet: Settings, cell: E26, expect: "block 2, minute 120"}
  - {sheet: Grid, cell: E2, expect: "G1-S1, set A, P1: T01-L1, T04-L2, T07-L3"}
  - {sheet: Grid, cell: G13, expect: "spare"}
flips:
  - name: the mock slot grows to 25 minutes
    set: [{sheet: Settings, cell: B3, value: 25}]
    verdicts:
      - {sheet: Settings, cell: B16, expect: "does not fit: 5 learners without a slot"}
      - {sheet: Settings, cell: B17, expect: "after the day"}
  - name: one learner is known to be absent before the day
    set: [{sheet: Seats, cell: G2, value: "no"}]
    verdicts:
      - {sheet: Settings, cell: B16, expect: "fits: 36 slots for 34 learners"}
      - {sheet: Settings, cell: C27, expect: "34"}
  - name: the changeover shrinks to 2 minutes
    set: [{sheet: Settings, cell: B4, value: 2}]
    verdicts:
      - {sheet: Settings, cell: B16, expect: "fits: 42 slots for 35 learners"}
  - name: G1 takes the no-show question, so its set A seat is asked the reserve
    set: [{sheet: Groups, cell: B2, value: "4 no-shows"}]
    verdicts:
      - {sheet: Grid, cell: E2, expect: "G1-S1, set A, P1: T01-L1, T02-L2, T07-L3"}
  - name: G6 takes the offer question, so its set H seat is asked the reserve
    set: [{sheet: Groups, cell: B7, value: "5 campaign"}]
    verdicts:
      - {sheet: Grid, cell: G9, expect: "G6-S3, set H, P3: T08-L1, T01-L2, T05-L3"}
```
"""

SCORES_YAML = """# How does Mock R1's scoring sheet prove it computes, and that its checks move?

Read by `scripts/xlsx_recalc.py`. The sheet ships blank, so the checks as shipped read its empty state,
and the flips enter marks and assert that the totals, the status and the calibration check move. The
workbook is written by `content/W03/D4/internal/C2_W03_D04_build_workbooks_INTERNAL.py`, which copies
the criteria from `data/programme/facts.yaml`.

```yaml
workbook: C2_W03_D04_mock_scoring_sheet_TRAINER.xlsx
verdicts:
  - {sheet: Criteria, cell: D11, expect: "30"}
  - {sheet: Criteria, cell: D12, expect: "yes"}
  - {sheet: Scores, cell: M2, expect: "not scored"}
  - {sheet: Assessors, cell: B6, expect: "0 of 35 scored"}
  - {sheet: Assessors, cell: B10, expect: "too few scores to compare"}
  - {sheet: Example, cell: L2, expect: "22"}
flips:
  - name: one learner is scored in full
    set:
      - {sheet: Scores, cell: D2, value: 6}
      - {sheet: Scores, cell: E2, value: 3}
      - {sheet: Scores, cell: F2, value: 2}
      - {sheet: Scores, cell: G2, value: 5}
      - {sheet: Scores, cell: H2, value: 4}
      - {sheet: Scores, cell: I2, value: 2}
    verdicts:
      - {sheet: Scores, cell: L2, expect: "22"}
      - {sheet: Scores, cell: M2, expect: "scored"}
      - {sheet: Assessors, cell: B6, expect: "1 of 35 scored"}
      - {sheet: Groups, cell: D2, expect: "22"}
  - name: a mark is entered above its maximum
    set: [{sheet: Scores, cell: D2, value: 9}]
    verdicts:
      - {sheet: Scores, cell: M2, expect: "check: a mark is above its maximum"}
      - {sheet: Assessors, cell: B7, expect: "1"}
  - name: two assessors score the technical half four marks apart
    set:
      - {sheet: Scores, cell: D2, value: 8}
      - {sheet: Scores, cell: E2, value: 4}
      - {sheet: Scores, cell: F2, value: 3}
      - {sheet: Scores, cell: G2, value: 5}
      - {sheet: Scores, cell: H2, value: 5}
      - {sheet: Scores, cell: I2, value: 2}
      - {sheet: Scores, cell: D6, value: 5}
      - {sheet: Scores, cell: E6, value: 3}
      - {sheet: Scores, cell: F6, value: 3}
      - {sheet: Scores, cell: G6, value: 5}
      - {sheet: Scores, cell: H6, value: 5}
      - {sheet: Scores, cell: I6, value: 2}
    verdicts:
      - {sheet: Assessors, cell: B8, expect: "4"}
      - {sheet: Assessors, cell: B10, expect: "discuss at the close: a gap above two marks"}
```
"""

if __name__ == "__main__":
    build_roster()
    build_scores()
    ROSTER_MANIFEST.write_text(ROSTER_YAML, encoding="utf-8")
    SCORES_MANIFEST.write_text(SCORES_YAML, encoding="utf-8")
    print(f"wrote {ROSTER.relative_to(ROOT)}, {SCORES.relative_to(ROOT)} and their two manifests")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W03/D4/internal/C2_W03_D04_build_workbooks_INTERNAL.py
#     Writes the two workbooks and the two manifests, prints one line naming them, and exits 0.
# python3 scripts/xlsx_recalc.py content/W03/D4
#     Recalculates both workbooks through LibreOffice and reports 7 verdicts and 5 flips for the roster
#     and 6 verdicts and 3 flips for the scoring sheet, all passing.
# The same build after facts.yaml changes a mock criterion's marks so the total is no longer 30
#     The script stops on its assert, because a mock that no longer adds to the approved 30 marks must
#     be settled in facts.yaml before any sheet is rebuilt.

"""Write Build 1's GD roster workbook and the recalc manifest that proves it computes.

    python3 content/W03/D5/internal/C2_W03_D05_build_gd_roster_INTERNAL.py

Writes, beside each other in content/W03/D5/gd/:
  C2_W03_D05_gd_roster_TRAINER.xlsx         the slots, the cards, the clash check and the stretch
  C2_W03_D05_gd_roster_recalc_INTERNAL.md   the verdicts and flips scripts/xlsx_recalc.py asserts

The block length and the group count come from data/programme/facts.yaml (campus_day and cohort),
so a sync that changes either reaches the roster with one rerun. The ten cards, their levels and
the sub-problems each is kept from are the GD prompts file's (gd/C2_W03_D05_gd_prompts_TRAINER.md).
The workbook names no learner: groups are G1 to G9, and the sub-problems on the Inputs sheet are an
example allocation, chosen so that the shipped roster shows no clash, until Monday's allocation
replaces it.
"""
import pathlib

import yaml
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parent / "gd"
BOOK = "C2_W03_D05_gd_roster_TRAINER.xlsx"
MANIFEST = "C2_W03_D05_gd_roster_recalc_INTERNAL.md"

facts = yaml.safe_load((ROOT / "data" / "programme" / "facts.yaml").read_text(encoding="utf-8"))
GROUPS = facts["cohort"]["build_groups"]["value"]
BLOCK = 180
assert "180 minutes" in facts["campus_day"]["shape"]
assert GROUPS == 9, "the slot table below seats nine groups; add slots before changing the count"

# Card, title, level, the sub-problems it is kept from, read minutes then discuss minutes.
CARDS = [
    (1, "Should Kalpa cut the self-pay price of its Whole-body wellness panel from $299 to $249?", 1, "none", "3, then 18"),
    (2, "Should Kalpa stop posting paper statements and bill patients by text and email only?", 1, "none", "3, then 18"),
    (3, "Should Kalpa promise same-day results in all six metros?", 2, "none", "3, then 18"),
    (4, "Should Kalpa close its phone booking line and move every patient online?", 2, "none", "3, then 18"),
    (5, "Is the vendor's 30 percent fall in denials good enough to buy on?", 3, "3 and 5", "3, then 18"),
    (6, "Should the lab director rank the six labs monthly on turnaround?", 3, "4", "3, then 18"),
    (7, "Where should the board's $2 million for growth go?", 4, "none", "4, then 17"),
    (8, "Should Kalpa sign the plan's preferred-lab offer in Dallas? (the spare)", 4, "none", "4, then 17"),
    (9, "What does Dr Menon do in the week the clearinghouse is down?", 5, "3", "4, then 17"),
    (10, "Should Kalpa move its Texas Medicaid claim work to Bengaluru?", 5, "none", "4, then 17"),
]
# Slot, day, block, stream, chair, room, start formula, card. Slots 1 to 7 run in Friday block one;
# slots 8 and 9 open Saturday morning in parallel, before the presentations.
EXPERT, ADVISOR = "The industry expert", "The Principal Advisor, online"
SLOTS = [
    (1, "Friday", "one", "A", EXPERT, "GD room", "=Inputs!$B$4", 1),
    (2, "Friday", "one", "B", ADVISOR, "Second room", "=Inputs!$B$4", 2),
    (3, "Friday", "one", "A", EXPERT, "GD room", "=Inputs!$B$4+Inputs!$B$3", 3),
    (4, "Friday", "one", "B", ADVISOR, "Second room", "=Inputs!$B$4+Inputs!$B$3", 4),
    (5, "Friday", "one", "A", EXPERT, "GD room", "=Inputs!$B$4+2*Inputs!$B$3", 5),
    (6, "Friday", "one", "A", EXPERT, "GD room", "=Inputs!$B$4+3*Inputs!$B$3", 6),
    (7, "Friday", "one", "A", EXPERT, "GD room", "=Inputs!$B$4+4*Inputs!$B$3", 7),
    (8, "Saturday", "morning", "A", EXPERT, "GD room", "=0", 9),
    (9, "Saturday", "morning", "B", ADVISOR, "Second room", "=0", 10),
]
# The example allocation: two groups on each sub-problem and one on the fifth, placed so that the
# draw shown (G1 in slot 1 and so on) meets no card its group is kept from.
EXAMPLE = [("G1", 3), ("G2", 3), ("G3", 1), ("G4", 1), ("G5", 2), ("G6", 2), ("G7", 4), ("G8", 4), ("G9", 5)]

HEAD = PatternFill("solid", fgColor="D9D9D9")
INPUT = PatternFill("solid", fgColor="FFFF00")
WRAP = Alignment(vertical="top", wrap_text=True)


def put(ws, ref, value, fill=None, blue=False, bold=False):
    c = ws[ref]
    c.value = value
    c.font = Font(name="Arial", size=10, color="0000FF" if blue else None, bold=bold)
    c.alignment = WRAP
    if fill is not None:
        c.fill = fill
    return c


def widths(ws, cols):
    for col, w in cols.items():
        ws.column_dimensions[col].width = w


def build():
    wb = Workbook()
    rm = wb.active
    rm.title = "Read me"
    widths(rm, {"A": 120})
    lines = [
        "Build 1 GD roster, Friday and Saturday morning (TRAINER ONLY)",
        "",
        "Yellow cells with blue text are the inputs. Everything else is a formula, so a changed input recomputes every end and every verdict.",
        f"Times are minutes into the block, never clock times. A block runs {BLOCK} minutes (data/programme/facts.yaml, campus_day).",
        "Stream A is the industry expert in the GD room. Stream B is the Principal Advisor online, hosted by the Academic TA in a second room.",
        "On Monday, replace the sub-problem values on Inputs with the Programme Head's allocation. The values shipped are an example, placed so that the shipped draw shows no clash.",
        "At the Friday opening, the Programme Head draws the GD order by lot and types each group's position on Inputs. Slot 1 is the first round; the card each slot carries is fixed on Roster, so complexity climbs with the slot.",
        "Cards 07 to 10 read for four minutes and discuss for seventeen; cards 01 to 06 read for three and discuss for eighteen. Every round is 30 minutes.",
        "Check reads the result: the GD minutes, how the roster stretches for more groups, whether every round ends inside its block, and whether any group meets a card it is kept from.",
        "A clash means swapping the card with the other card of the same level on Roster, if that card's own flag allows, or with the spare, card 08, which is kept from nobody.",
    ]
    for i, text in enumerate(lines, start=1):
        if text:
            put(rm, f"A{i}", text, bold=(i == 1))

    ip = wb.create_sheet("Inputs")
    widths(ip, {"A": 44, "B": 30, "C": 70})
    put(ip, "A1", "Inputs", bold=True)
    for col, text in zip("ABC", ["Setting", "Value", "Source"]):
        put(ip, f"{col}2", text, HEAD)
    settings = [
        ("Round length, minutes", 30, "The row: about 30 minutes per group"),
        ("Opening before the first round, minutes", 15, "The expert's opening to the whole cohort, Friday block one"),
        ("Block length, minutes", BLOCK, "data/programme/facts.yaml, campus_day"),
        ("Groups this build", GROUPS, "data/programme/facts.yaml, cohort.build_groups (stated); the tracker plans fifteen"),
        ("Rounds in the standard roster", 9, "Seven on Friday and two on Saturday morning"),
        ("Saturday rounds per stream, most", 3, "Past three, Saturday's presentations move back more than an hour"),
    ]
    for r, (label, value, source) in enumerate(settings, start=3):
        put(ip, f"A{r}", label)
        put(ip, f"B{r}", value, INPUT, blue=True)
        put(ip, f"C{r}", source)
    put(ip, "A11", "Groups: sub-problem from Monday's allocation, GD position from Friday's draw", bold=True)
    for col, text in zip("ABC", ["Group", "Sub-problem (1 revenue, 2 bookings, 3 billing, 4 no-shows, 5 campaign)",
                                  "GD position drawn (1 to 9)"]):
        put(ip, f"{col}12", text, HEAD)
    for r, (group, sub) in enumerate(EXAMPLE, start=13):
        put(ip, f"A{r}", group)
        put(ip, f"B{r}", sub, INPUT, blue=True)
        put(ip, f"C{r}", r - 12, INPUT, blue=True)
    dv = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=False)
    ip.add_data_validation(dv)
    dv.add("B13:B21")

    pr = wb.create_sheet("Prompts")
    widths(pr, {"A": 7, "B": 80, "C": 7, "D": 22, "E": 18})
    put(pr, "A1", "The ten cards", bold=True)
    for col, text in zip("ABCDE", ["Card", "The card's question", "Level", "Kept from sub-problems",
                                   "Read, then discuss"]):
        put(pr, f"{col}2", text, HEAD)
    for r, (card, title, level, kept, minutes) in enumerate(CARDS, start=3):
        put(pr, f"A{r}", card)
        put(pr, f"B{r}", title)
        put(pr, f"C{r}", level)
        put(pr, f"D{r}", kept)
        put(pr, f"E{r}", minutes)

    ro = wb.create_sheet("Roster")
    widths(ro, {"A": 6, "B": 10, "C": 9, "D": 7, "E": 28, "F": 13, "G": 12, "H": 12, "I": 7, "J": 7,
                "K": 13, "L": 12, "M": 14, "N": 34, "O": 18})
    put(ro, "A1", "GD roster: nine rounds, complexity climbing with the slot", bold=True)
    heads = ["Slot", "Day", "Block", "Stream", "Chair", "Room", "Start, minutes into the block",
             "End, minutes into the block", "Level", "Card", "Group", "Group's sub-problem",
             "Card is kept from", "Clash check", "Block check"]
    for col, text in zip("ABCDEFGHIJKLMNO", heads):
        put(ro, f"{col}3", text, HEAD)
    for r, (slot, day, block, stream, chair, room, start, card) in enumerate(SLOTS, start=4):
        put(ro, f"A{r}", slot)
        put(ro, f"B{r}", day)
        put(ro, f"C{r}", block)
        put(ro, f"D{r}", stream)
        put(ro, f"E{r}", chair)
        put(ro, f"F{r}", room)
        put(ro, f"G{r}", start)
        put(ro, f"H{r}", f"=G{r}+Inputs!$B$3")
        put(ro, f"I{r}", f"=INDEX(Prompts!$C$3:$C$12,MATCH(J{r},Prompts!$A$3:$A$12,0))")
        put(ro, f"J{r}", card, INPUT, blue=True)
        put(ro, f"K{r}", f'=IFERROR(INDEX(Inputs!$A$13:$A$21,MATCH(A{r},Inputs!$C$13:$C$21,0)),"no group drawn")')
        put(ro, f"L{r}", f'=IFERROR(INDEX(Inputs!$B$13:$B$21,MATCH(K{r},Inputs!$A$13:$A$21,0)),"")')
        put(ro, f"M{r}", f"=INDEX(Prompts!$D$3:$D$12,MATCH(J{r},Prompts!$A$3:$A$12,0))")
        put(ro, f"N{r}", f'=IF(L{r}="","no group",IF(ISNUMBER(SEARCH(L{r},M{r})),'
                         f'"swap: the card meets the group\'s own sub-problem","ok"))')
        put(ro, f"O{r}", f'=IF(H{r}>Inputs!$B$5,"over the block end","inside the block")')
    put(ro, "A15", "Slots 1 to 7 run in Friday block one; slots 8 and 9 open Saturday morning, in parallel, before the presentations.")
    put(ro, "A16", "Stream B's rounds 3 to 5 on Friday, and Saturday rounds beyond the first, are the stretch the Check sheet names when more groups run.")

    fb = wb.create_sheet("Friday block two")
    widths(fb, {"A": 60, "B": 46, "C": 16, "D": 16})
    put(fb, "A1", "Friday block two: the first tranche, the cold-run roll call and the draw", bold=True)
    tranche = [
        ("Presentations in the first tranche", 3),
        ("Presentation slot, minutes", 30),
        ("GD notes consolidated by the expert, the Principal Advisor and the trainer, minutes", 20),
        ("Cold-run roll call, minutes per group", 3),
        ("Drawing Saturday's presentation order, minutes", 10),
    ]
    for r, (label, value) in enumerate(tranche, start=3):
        put(fb, f"A{r}", label)
        put(fb, f"B{r}", value, INPUT, blue=True)
    for col, text in zip("ABCD", ["Part", "Minutes", "Start, minutes into the block", "End, minutes into the block"]):
        put(fb, f"{col}9", text, HEAD)
    parts = [
        ("First tranche of presentations, before the expert", "=B3*B4"),
        ("GD notes consolidated (groups run cold run one)", "=B5"),
        ("Cold-run roll call, every group", "=B6*Inputs!B6"),
        ("Saturday's presentation order drawn", "=B7"),
        ("Saturday handover and slack", "=Inputs!B5-SUM(B10:B13)"),
    ]
    for i, (label, formula) in enumerate(parts):
        r = 10 + i
        put(fb, f"A{r}", label)
        put(fb, f"B{r}", formula)
        put(fb, f"C{r}", "=0" if i == 0 else f"=D{r - 1}")
        put(fb, f"D{r}", f"=C{r}+B{r}")
    put(fb, "A16", "Block two check")
    put(fb, "B16", '=IF(B14<0,"block two runs over by "&-B14&" minutes: shorten the tranche",'
                    '"block two fits with "&B14&" minutes of slack")')

    ck = wb.create_sheet("Check")
    widths(ck, {"A": 58, "B": 90})
    put(ck, "A1", "Check", bold=True)
    put(ck, "A2", "What", HEAD)
    put(ck, "B2", "Result", HEAD)
    checks = [
        ("GD minutes this build", "=Inputs!B6*Inputs!B3"),
        ("Rounds one stream can run in Friday block one", "=INT((Inputs!B5-Inputs!B4)/Inputs!B3)"),
        ("Rounds both streams can run in Friday block one", "=2*B4"),
        ("Rounds both streams can run on Saturday morning, at most", "=2*Inputs!B8"),
        ("Most groups the two expert days hold", "=B5+B6"),
        ("The roster for this many groups",
         '=IF(Inputs!B6<=Inputs!B7,"standard roster: nine rounds, seven on Friday and two on Saturday morning",'
         'IF(Inputs!B6<=B5+2,"stretch: stream B runs more Friday rounds, up to "&B5&" rounds across both streams in block one, and Saturday keeps its two",'
         'IF(Inputs!B6<=B7,"stretch: stream B runs all Friday rounds and both streams run up to "&Inputs!B8&" Saturday rounds, which moves Saturday presentations back by up to "&(Inputs!B8-1)*Inputs!B3&" minutes",'
         '"over the two expert days: the Programme Head adds a third chair")))'),
        ("Clashes between a card and its group's sub-problem", '=COUNTIF(Roster!N4:N12,"swap*")'),
        ("Clash verdict", '=IF(B9=0,"no group meets its own sub-problem",B9&" clash: swap within the level or use card 08")'),
        ("Rounds that run past their block", '=COUNTIF(Roster!O4:O12,"over*")'),
        ("Block verdict", '=IF(B11=0,"every round ends inside its block",B11&" round runs past the block end")'),
        ("Groups drawn to one slot each",
         '=IF(SUMPRODUCT((COUNTIF(Inputs!C13:C21,Inputs!C13:C21)>1)*1)=0,"every group sits exactly one GD","two groups share a slot: redraw")'),
    ]
    for r, (label, formula) in enumerate(checks, start=3):
        put(ck, f"A{r}", label)
        put(ck, f"B{r}", formula)

    wb.active = 0
    OUT.mkdir(parents=True, exist_ok=True)
    wb.save(OUT / BOOK)


def manifest():
    lines = [
        "# Recalc manifest for the Build 1 GD roster",
        "",
        "`scripts/xlsx_recalc.py` reads this file, rebuilds the roster through LibreOffice, asserts the",
        "verdicts as shipped, then flips three decisions and asserts that the verdicts move: the group count",
        "rising to the tracker's fifteen, a sub-problem 5 group drawn to the slot carrying card 05, and",
        "rounds running long. Written by `internal/C2_W03_D05_build_gd_roster_INTERNAL.py`; rebuild both",
        "together.",
        "",
        "```yaml",
        f"workbook: {BOOK}",
        "verdicts:",
        '  - {sheet: Check, cell: B3, expect: "270"}',
        '  - {sheet: Check, cell: B8, expect: "standard roster: nine rounds, seven on Friday and two on Saturday morning"}',
        '  - {sheet: Check, cell: B10, expect: "no group meets its own sub-problem"}',
        '  - {sheet: Check, cell: B12, expect: "every round ends inside its block"}',
        '  - {sheet: Check, cell: B13, expect: "every group sits exactly one GD"}',
        '  - {sheet: Roster, cell: H10, expect: "165"}',
        '  - {sheet: Roster, cell: M8, expect: "3 and 5"}',
        '  - {sheet: "Friday block two", cell: B16, expect: "block two fits with 33 minutes of slack"}',
        "flips:",
        "  - name: the Programme Head runs the tracker's fifteen groups",
        "    set: [{sheet: Inputs, cell: B6, value: 15}]",
        "    verdicts:",
        '      - {sheet: Check, cell: B3, expect: "450"}',
        '      - {sheet: Check, cell: B8, contains: "both streams run up to 3 Saturday rounds"}',
        '      - {sheet: "Friday block two", cell: B16, expect: "block two fits with 15 minutes of slack"}',
        "  - name: a sub-problem 5 group is drawn to the slot carrying card 05",
        "    set: [{sheet: Inputs, cell: B17, value: 5}]",
        "    verdicts:",
        '      - {sheet: Roster, cell: N8, contains: "swap"}',
        '      - {sheet: Check, cell: B10, expect: "1 clash: swap within the level or use card 08"}',
        "  - name: rounds run 35 minutes",
        "    set: [{sheet: Inputs, cell: B3, value: 35}]",
        "    verdicts:",
        '      - {sheet: Roster, cell: H10, expect: "190"}',
        '      - {sheet: Check, cell: B12, expect: "1 round runs past the block end"}',
        "```",
    ]
    (OUT / MANIFEST).write_text("\n".join(lines) + "\n", encoding="utf-8")


def store_values(path):
    """Recalculate through LibreOffice with the xlsx skill's recalc.py, so every formula also carries
    its computed value for a reader that does not recalculate. Skipped, and said so, when LibreOffice
    or the script is missing; the workbook still computes when it is opened."""
    import shutil
    import subprocess
    import sys
    script = ROOT / ".claude" / "skills" / "xlsx" / "scripts" / "recalc.py"
    if not script.exists() or not (shutil.which("soffice") or shutil.which("libreoffice")):
        print("values not stored: LibreOffice or the xlsx skill's recalc.py is missing")
        return
    r = subprocess.run([sys.executable, str(script), str(path), "60"], capture_output=True, text=True)
    print("values stored" if '"status": "success"' in r.stdout else f"recalc reported: {r.stdout.strip()[:200]}")


if __name__ == "__main__":
    build()
    store_values(OUT / BOOK)
    manifest()
    print(f"wrote {OUT / BOOK} and {OUT / MANIFEST}")

# Test inputs and expected outcomes
# ---------------------------------
# Run as shipped: the workbook and its manifest are written, and
#   python3 scripts/xlsx_recalc.py content/W03/D5/gd/C2_W03_D05_gd_roster_recalc_INTERNAL.md
#   reports 8 verdicts computed and 3 decisions flipped.
# In the written workbook, type 5 in Inputs!B17 (G5 on the campaign sub-problem): Roster!N8 reads
#   "swap: the card meets the group's own sub-problem" and Check!B10 reads
#   "1 clash: swap within the level or use card 08".
# Type 15 in Inputs!B6: Check!B3 reads 450 and Check!B8 names the Saturday stretch.
# Type 35 in Inputs!B3: the fifth stream A round ends at 190, past the 180-minute block.

"""Build the lab debrief's three chapter notebooks, one per place most rooms break.

    python3 content/W01/D5/internal/C2_W01_D05_build_chapters_INTERNAL.py

Each notebook pairs with one chapter of slides/C2_W01_D05_debrief_STUDENT.md by number and title,
runs cold in notebooks/ on the lab export, and opens only after the lab clock stops. The data is
v3-lab, proposed for client zero v2.3 and not yet locked. No cell prints an order id or a raw
planted value: where a learner needs to see the record, the notebook gives the lines to type and an
empty your-turn cell.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, md, code, empty, build  # noqa: E402

DAY = ROOT / "content" / "W01" / "D5"
NB = DAY / "notebooks"

# The shared opening: the lab export, the control totals and three passes of increasing care, so
# every chapter starts from the same state without importing another notebook.
LOAD = SETUP + '''
import random
import statistics
import time

rows = kit.load_csv("C2_W01_D05_lab_orders_STUDENT.csv")
control = {c["quarter"]: c for c in kit.load_csv("C2_W01_D05_lab_control_STUDENT.csv")}
QUARTERS = ("Q1", "Q2")


def change(a, b):
    """Percentage change from a to b."""
    return 100 * (b / a - 1)


def ctl(q):
    return int(control[q]["amount_rs"]), int(control[q]["orders"])


print(f"{len(rows)} rows read from the lab export; Finance's control totals for {', '.join(sorted(control))}")
'''

HONESTY = """
    **Before you read on.** This notebook runs on this morning's lab export and shows the morning's
    numbers. It opens after the lab clock stops, and it is the debrief's text for self-study too.
"""

# --------------------------------------------------------------------------------- chapter 1
CH1 = [
    md("""
    # 1. The reconciliation, skipped

    **Week 1, Friday. The lab debrief, chapter 1 of 3: do the quarters in your note match the books?**

    Anand Iyer, finance controller, said it on Wednesday and it still holds: "Until your numbers match
    ours, Finance will not act on a drop measured from an ERP export."

    **The metric at stake.** Booked revenue per quarter, and the change from Q1 to Q2 that the note to
    Meera Raghavan leads with. **Who asks.** Anand, before he lets any number reach Meera's growth
    review, and Meera, who acts on the first line of the note. **What a wrong number costs.** A note
    that calls a falling quarter a rising one sends Monday's review home with no investigation, and
    Marketing's Rs 12 crore acquisition request gets judged against a quarter that did not happen.
    Anand returns the note, and the team's next number is read with suspicion.

    **Who else faces this.** Nykaa, the beauty and fashion retailer, reports two numbers for the same quarter:
    for April to June 2025, consolidated GMV of Rs 4,182 crore and revenue from operations of Rs 2,155
    crore (FSN E-Commerce Ventures press release, 12 August 2025). An analyst there who quotes one to
    the owner of the other is out by nearly half, so every internal figure says which it is and bridges
    to the books. A public case shows what an unreconciled pipeline hides: in October 2020 Public Health
    England said 15,841 positive COVID-19 cases from 25 September to 2 October had been left out of the
    reported daily figures because files exceeded a size limit (UK government statement, 4 October 2020).
    No step raised an error; the rows were simply not there.

    **Where this starts.** This morning each of you ran the week's method alone on the lab export. This
    notebook replays the step most rooms dropped when the clock ran, the reconciliation, and shows what
    the note said without it. Chapter 2 picks up the case where a count check passes and the rupees do
    not; chapter 3 takes the clean numbers into the tree.
    """ + HONESTY),
    code(LOAD),
    code('''
kit.side_by_side(
    kit.ladder(["The reconciliation, skipped", "The pass that looks clean", "The headline on too few orders"],
               lit=0, show=False),
    kit.flow(["profile", "clean, with a log", "reconcile", "decompose", "test", "note"], lit=2, show=False),
)
'''),
    md("""
    **The passes, as two small functions.** `quarter_totals` sums each quarter, either reading a value
    with grouping commas or setting any value that will not convert to zero, the way the hurried pass
    did; `first_of_each` keeps one row per order id, Wednesday's identity rule.
    """),
    code('''
def quarter_totals(src, text_to_zero):
    out = {}
    for q in QUARTERS:
        s = n = 0
        for r in src:
            if r["quarter"] != q:
                continue
            v = r["amount"]
            s += (int(v) if v.isdigit() else 0) if text_to_zero else int(v.replace(",", ""))
            n += 1
        out[q] = (s, n)
    return out


def first_of_each(src):
    kept = {}
    for r in src:
        kept.setdefault(r["order_id"], r)
    return list(kept.values())


truth = change(ctl("Q1")[0], ctl("Q2")[0])
print(f"Finance's books: Q1 to Q2 {truth:+.1f}%")
'''),
    md("""
    ## 1. The headline the hurried run sent

    Most notes this morning were built on a pass that kept the rows as they arrived and set any value
    that would not convert to zero. It runs without an error.

    **Predict before you run.** What Q1 to Q2 change does that pass report?

    - a) A fall of a little under a third, the same as Finance's books.
    - b) A rise of about a tenth.
    - c) A fall of about a seventh.
    - d) No change, since both quarters hold about a hundred orders.
    """),
    code('''
hurried = quarter_totals(rows, text_to_zero=True)
h_change = change(hurried["Q1"][0], hurried["Q2"][0])
kit.stats([(kit.rupees(hurried["Q1"][0]), "Q1 as summed", f"{hurried['Q1'][1]} rows"),
           (kit.rupees(hurried["Q2"][0]), "Q2 as summed", f"{hurried['Q2'][1]} rows"),
           (f"{h_change:+.1f}%", "Q1 to Q2", "the line the note led with")])
kit.columns(list(QUARTERS), [("as summed", [hurried[q][0] for q in QUARTERS])], width=460,
            fmt=lambda v: kit.rupees(v), title="The hurried run: Q2 looks bigger than Q1")
'''),
    md("""
    **What happened.** The answer is b. The pass reports Q2 up 11.8 percent.

    **The plausible wrong answer.** "Q2 grew 11.8 percent; no action needed on the top line." The
    arithmetic is right, the file is Finance's own export, and nothing on the screen looks broken.

    **Why it is wrong.** Nobody asked whether the data summed is the data Finance booked. Sent to Meera,
    the line tells her the quarter that fell was a good one, and the review spends its time on
    Marketing's plans instead of on the fall. The check is one comparison with the control file.
    """),
    code('''
kit.table(["quarter", "orders as summed", "Finance's orders", "rupees as summed", "Finance's rupees"],
          [(q, hurried[q][1], ctl(q)[1], kit.rupees(hurried[q][0]), kit.rupees(ctl(q)[0])) for q in QUARTERS],
          caption="The hurried run against the control totals")
kit.check("the hurried run misses Finance in both quarters, in rupees",
          all(hurried[q][0] != ctl(q)[0] for q in QUARTERS))
kit.check("the hurried run points the opposite way to the books", h_change > 0 > truth,
          f"{h_change:+.1f}% against {truth:+.1f}%")
'''),
    md("""
    ## The options

    The question at this step is narrow: before a single branch of the tree is read, is the data you
    cleaned still the data Finance booked? A team has four ways to answer it.

    | Option | What it does | What it needs |
    |---|---|---|
    | A. Trust the pass | Sum what the cleaning pass kept and move on to the tree | Nothing |
    | B. Count check | Rows read equal rows kept plus rows rejected, and orders per quarter equal Finance's order counts | The control file's order counts |
    | C. Counts and rupees, with a bridge | B, plus each quarter's rupees against Finance's control total, and a bridge from what was read to what was kept | The control file's rupee totals |
    | D. Order-level match | Every kept order matched to Finance's ledger line by line | The ledger itself, which the lab did not have |

    You have just seen option A's headline. The cell below sizes all four on this morning's file: it
    runs the hurried pass, then applies each check and fixes only what that check can see. D cannot run
    here, since the lab had no ledger; its row is modelled on C's result, which is what a full match
    would land on. The minutes are the lab brief's pace, and D's is this
    programme's estimate for a request to Finance and a join; the milliseconds are measured here.
    """),
    code('''
truth = change(ctl("Q1")[0], ctl("Q2")[0])
sizing = []
for name, minutes, cells, dedupe, text_fixed in [
        ("A. trust the pass", 0, 0, False, False),
        ("B. count check", 2, 1, True, False),
        ("C. counts and rupees, bridge", 15, 3, True, True),
        ("D. order-level match", 120, 6, True, True)]:
    start = time.perf_counter()
    src = first_of_each(rows) if dedupe else rows
    t = quarter_totals(src, text_to_zero=not text_fixed)
    ms = 1000 * (time.perf_counter() - start)
    reported = change(t["Q1"][0], t["Q2"][0])
    ms_text = "needs the ledger" if name.startswith("D") else f"{ms:.2f}"
    sizing.append((name, minutes, cells, len(rows), ms_text, f"{reported:+.1f}%", abs(reported - truth)))
kit.table(["option", "analyst minutes", "cells", "rows touched", "compute ms", "Q1 to Q2 it reports", "points off"],
          [s[:6] + (f"{s[6]:.1f}",) for s in sizing],
          caption="Four ways to check, sized on the lab export; the books say " + f"{truth:+.1f}%")
kit.bars([(s[0], round(s[6], 1)) for s in sizing], lit=(2,), fmt=lambda v: f"{v:.1f} pts",
         title="How far each option's headline sits from the books, in percentage points")
'''),
    code('''
kit.check("the computer's cost is under a second for every option run here",
          all(float(s[4]) < 1000 for s in sizing[:3]))
kit.check("only options C and D land on the books", [round(s[6], 1) for s in sizing][2:] == [0.0, 0.0]
          and all(s[6] > 1 for s in sizing[:2]))
'''),
    md("""
    **The best-fit call.** C. It costs about fifteen minutes of an analyst's two hours, needs only the
    control file that came with the export, and lands on the books to the rupee; the computer's share
    of the cost is under a millisecond for all four, so the choice is about minutes of thought, never
    about compute. B is the option most people who did check stopped at, and it still leaves the
    headline about 14 points off. D names every order that differs, which C cannot, and costs a request
    to Finance and most of the afternoon.

    **What would change the call.** No control total at all: then C has nothing to land on, and D, or a
    second export pulled from the source system for the same quarters, becomes the check. A bridge
    that does not close: then C has told you there is a gap it cannot explain, and D is how you find it.
    """),
    md("""
    ## 2. The count check catches half of it

    Option B compares orders with Finance's order counts and keeps one row per order id, the identity
    rule from Wednesday.

    **Predict before you run.** After B's fix, what does the headline say?

    - a) Q2 up 11.8 percent, unchanged.
    - b) Q2 down 28.5 percent, the books.
    - c) Q2 down 14.6 percent.
    - d) The check cannot run without the order-level ledger.
    """),
    code('''
once = first_of_each(rows)
counted = quarter_totals(once, text_to_zero=True)
c_change = change(counted["Q1"][0], counted["Q2"][0])
kit.table(["quarter", "orders kept", "Finance's orders", "rupees kept", "Finance's rupees"],
          [(q, counted[q][1], ctl(q)[1], kit.rupees(counted[q][0]), kit.rupees(ctl(q)[0])) for q in QUARTERS],
          caption=f"After the count check: {len(rows)} rows read, {len(once)} kept, {len(rows) - len(once)} rejected")
seen, rejected = set(), []
for r in rows:
    if r["order_id"] in seen:
        rejected.append(r)
    seen.add(r["order_id"])
kit.check("input equals kept plus rejected, each list built on its own", len(rows) == len(once) + len(rejected),
          f"{len(rows)} = {len(once)} + {len(rejected)}")
kit.check("the order counts now land on Finance's in both quarters",
          all(counted[q][1] == ctl(q)[1] for q in QUARTERS))
kit.check("Q1's rupees still miss the control total", counted["Q1"][0] != ctl("Q1")[0],
          kit.rupees(ctl("Q1")[0] - counted["Q1"][0]) + " short")
'''),
    md("""
    **What happened.** The answer is c. Every order count lands, and the headline moves from +11.8 to
    -14.6 percent: the right direction and half the size. A count check proves the rows are there; it
    says nothing about whether each row's value survived the conversion. That is chapter 2's trap, and
    it is the one a pass that "looks clean" leaves behind.
    """),
    md("""
    ## 3. Counts and rupees, and the bridge between them

    Option C adds the rupee comparison and draws the walk from what the hurried run summed to what
    Finance booked, one move per decision in the log.

    **Predict before you run.** Which move in the bridge is the larger?

    - a) The rows the control total does not contain.
    - b) The value that would not convert.
    - c) They are equal.
    - d) Neither; the bridge closes with no moves.
    """),
    code('''
clean = quarter_totals(once, text_to_zero=False)
as_read = sum(hurried[q][0] for q in QUARTERS)
extra_rows = sum(counted[q][0] for q in QUARTERS) - as_read
text_back = sum(clean[q][0] for q in QUARTERS) - sum(counted[q][0] for q in QUARTERS)
kit.bridge(("the hurried sum", as_read), [("rows Finance does not hold", extra_rows),
                                          ("a value read back", text_back)],
           end_label="clean, both quarters", lit=[0], lo=9_000_000,
           title="From the hurried sum to the books (the axis starts at Rs 90 lakh)")
kit.check("the bridge lands on Finance's two quarters together",
          as_read + extra_rows + text_back == ctl("Q1")[0] + ctl("Q2")[0],
          kit.rupees(ctl("Q1")[0] + ctl("Q2")[0]))
kit.check("both quarters land, orders and rupees",
          all(clean[q] == ctl(q) for q in QUARTERS))
'''),
    md("""
    **What happened.** The answer is a. The rows Finance does not hold carry more rupees than the value
    read back, and both moves had to be found before the bridge closed.

    **The fix, and what it changes.** With both quarters on the books, the headline is a fall of 28.5
    percent, from Rs 60,48,000 to Rs 43,25,480. The note changes sign, so the decision changes with it:
    Monday's review now has a fall of Rs 17,22,520 to explain, and chapter 3 finds where it sits.
    """),
    code('''
variants = [("the hurried run", hurried), ("count check only", counted), ("counts and rupees", clean)]
kit.table(["run", "Q1", "Q2", "Q1 to Q2"],
          [(n, kit.rupees(t["Q1"][0]), kit.rupees(t["Q2"][0]), f"{change(t['Q1'][0], t['Q2'][0]):+.1f}%")
           for n, t in variants], caption="One export, three headlines")
kit.columns([n for n, _ in variants], [("Q1", [t["Q1"][0] for _, t in variants]),
                                       ("Q2", [t["Q2"][0] for _, t in variants])],
            fmt=lambda v: kit.rupees(v), lit=(2,), title="The same file, three notes")
'''),
    md("""
    **Your turn.** The bridge says how many rupees Finance does not hold. It does not say which rows
    they are, and Anand will ask. Type these lines into the empty cell below and run it:

    ```python
    seen, extra = set(), []
    for r in rows:
        if r["order_id"] in seen:
            extra.append(r)
        seen.add(r["order_id"])
    kit.table(list(rows[0]), [list(r.values()) for r in extra], caption="Rows Finance does not hold")
    ```

    Read the dates and the segments: what do the rows have in common, and what would you tell the
    person who owns the export?
    """),
    empty(),
    md("""
    ## A second route: from Finance's side back to the export

    The bridge walked from the export to the books. The same answer should come from the other end:
    start at each control total, add back what the log removed, subtract what it read back, and land
    on what the hurried run summed. If the two routes disagree, one of the decisions in the log is
    wrong.
    """),
    code('''
back = {}
for q in QUARTERS:
    removed = sum(int(r["amount"].replace(",", "")) for r in rows if r["quarter"] == q) - clean[q][0]
    read_back = clean[q][0] - counted[q][0]
    back[q] = ctl(q)[0] + removed - read_back
kit.table(["quarter", "Finance", "plus rows removed", "less value read back", "lands on", "the hurried sum"],
          [(q, kit.rupees(ctl(q)[0]), kit.rupees(back[q] - ctl(q)[0] + (clean[q][0] - counted[q][0])),
            kit.rupees(clean[q][0] - counted[q][0]), kit.rupees(back[q]), kit.rupees(hurried[q][0]))
           for q in QUARTERS], caption="The walk from the books back to the export")
kit.equation(["Finance's total", "+", "rows removed", "-", "value read back", "=", "the hurried sum"],
             title="The second route, read left to right")
kit.check("the walk back lands on the hurried sum in both quarters", all(back[q] == hurried[q][0] for q in QUARTERS))

'''),
    md("""
    **When to switch routes.** The forward bridge is the one to show Finance, because it starts from
    their export. The walk back is the one to run when a bridge closes suspiciously neatly: two
    mistakes that cancel pass one route and fail the other.

    ### Depth: the same rows also move a branch

    Rows Finance does not hold inflate a total, and they can move a branch as well. If they sit in one segment, they
    manufacture a rise in orders per customer where nothing changed. Run the tree on the hurried rows
    and on the clean ones for the segment with the most consumer orders and compare the frequency branch.
    """),
    code('''
def tree(src, q, seg):
    rs = [r for r in src if r["quarter"] == q and r["segment"] == seg and r["amount"].isdigit()]
    cust = len({r["customer_id"] for r in rs})
    rev = sum(int(r["amount"]) for r in rs)
    return len(rs), cust, len(rs) / cust, rev / len(rs), rev


seg = "Retail-Core"
h1, h2 = tree(rows, "Q1", seg), tree(rows, "Q2", seg)
c1, c2 = tree(once, "Q1", seg), tree(once, "Q2", seg)
kit.table(["Retail-Core", "orders per customer, Q1 to Q2", "revenue per order, Q1 to Q2", "revenue"],
          [("hurried rows", f"{h1[2]:.2f} to {h2[2]:.2f} ({change(h1[2], h2[2]):+.1f}%)",
            f"{kit.rupees(h1[3])} to {kit.rupees(h2[3])}", f"{change(h1[4], h2[4]):+.1f}%"),
           ("one row per order", f"{c1[2]:.2f} to {c2[2]:.2f} ({change(c1[2], c2[2]):+.1f}%)",
            f"{kit.rupees(c1[3])} to {kit.rupees(c2[3])}", f"{change(c1[4], c2[4]):+.1f}%")],
          caption="On the hurried rows the frequency rise comes from repeated rows")
kit.check("on the hurried rows frequency rises and revenue looks flat",
          change(h1[2], h2[2]) > 15 and abs(change(h1[4], h2[4])) < 1)
'''),
    md("""
    The hurried rows turn a basket problem into a flat segment with loyal customers. Chapter 3 reads the
    clean tree properly.

    > **Kavya's review.** A number that has not been reconciled can point the wrong way, and this
    > morning it did. Put the two checks in a cell before you compute
    > the first number you plan to send, so the clock cannot remove them.

    ### In the interview

    **[S] Walk me through how you clean and check a dataset you have never seen.** "I profile every
    field first: present, convertible and distinct counts, and each count that is not what the field
    should hold is a finding. I clean with a log, one row per decision with its reason, and I keep what
    I reject. Then I reconcile before I analyse: rows read equal rows kept plus rows rejected, and each
    period's value lands on a total from outside the file, Finance's if there is one. On a lab export
    last week the count check alone moved my headline from +11.8 to -14.6 percent, and only the rupee
    check got it to the books' -28.5, so I never stop at counts."

    **[F] You have two hours and a raw export; what do you do first, and what do you skip?** "Profile
    first, twenty minutes. I never skip the reconciliation, because it is the step that can flip the
    sign of the finding and it costs fifteen minutes. I skip anything that does not change today's
    answer: a second chart, a test on every segment, polishing. If there is no control total I say so
    in the caveat and ask for one before the number leaves the room."

    **The design question: which check, and what would make you switch?** "Counts and rupees against a
    control total with a bridge, because it catches both kinds of error for fifteen minutes and needs
    only what comes with the export. I switch to an order-level match against the ledger when the bridge
    will not close or when there is no control total, and I say it will cost the afternoon."

    **Depth: when there is no control total.** Three stand-ins, in the order a careful analyst tries
    them: the same quarters in a second export pulled from the source system on another day; the
    payment gateway's settlement totals for the quarter, which count collected rather than booked
    money and so need their own bridge; last quarter's audited figure for the quarter that overlaps.
    Each is weaker than Finance's number, and the note says which one was used.
    """),
    code("kit.check_summary()"),
]

# --------------------------------------------------------------------------------- chapter 2
CH2 = [
    md("""
    # 2. The pass that looks clean

    **Week 1, Friday. The lab debrief, chapter 2 of 3: the rows reconcile, so is the pass finished?**

    Anand Iyer's analyst audits every note that reaches Meera. Their first question is "show me the
    rupees". A pass that reports zero rejects on a file everyone
    knows is dirty is the one they open first.

    **The metric at stake.** Q1 booked revenue, the base every Q1 to Q2 rate is measured from.
    **Who asks.** Anand's analyst, auditing the note, and Meera, who reads the size of the fall as the
    size of the problem. **What a wrong number costs.** A base that is short by one large order halves
    the fall the note reports, so Monday's review sizes the problem at half its real size and the fix
    gets half the attention; when Finance finds the missing order, every other number in the note is
    doubted with it.

    **Who else faces this.** JPMorgan Chase's own task force, reviewing the 2012 "London Whale" losses, found
    that a risk model run through spreadsheets "divided by their sum instead of their average", which
    "likely had the effect of muting volatility by a factor of two and of lowering the VaR" (the task
    force report of January 2013, as quoted by The Baseline Scenario, 9 February 2013). The trading
    losses came to $6.2 billion (FCA, 19 September 2013). Nothing crashed: the sheet produced a
    plausible number every day.

    **Where this starts.** Chapter 1 left one run at -14.6 percent: the order counts landed and the
    rupees did not. This chapter finds out why, sizes the four ways to handle a value that will not
    convert, and then meets the same shape one step later, where a segment filter drops a row without a
    word. Chapter 3 takes the repaired numbers into the tree.
    """ + HONESTY),
    code(LOAD + '''

def first_of_each(src):
    kept = {}
    for r in src:
        kept.setdefault(r["order_id"], r)
    return list(kept.values())


once = first_of_each(rows)
print(f"{len(once)} orders after the identity rule from chapter 1")
'''),
    code('''
kit.side_by_side(
    kit.ladder(["The reconciliation, skipped", "The pass that looks clean", "The headline on too few orders"],
               lit=1, show=False),
    kit.flow(["profile", "clean, with a log", "reconcile", "decompose", "test", "note"], lit=1, show=False),
)
'''),
    md("""
    ## 1. Zero rejects, and the counts reconcile

    The most natural line of Python in the week wraps the conversion in a `try` and sets a failure to
    zero. It never stops, it reports nothing, and every row survives.

    **Predict before you run.** The pass keeps one row per order and sets any value that will not
    convert to zero. How many orders does Q1 report against Finance's 98, and how many rejects?

    - a) 97 orders and 1 reject.
    - b) 98 orders and 0 rejects.
    - c) 98 orders and 1 reject.
    - d) 108 orders and 0 rejects.
    """),
    code('''
def to_int_or_zero(v):
    try:
        return int(v)
    except ValueError:
        return 0          # the file now "converts" cleanly


zeroed = {q: [to_int_or_zero(r["amount"]) for r in once if r["quarter"] == q] for q in QUARTERS}
kit.stats([(len(zeroed["Q1"]), "Q1 orders", f"Finance: {ctl('Q1')[1]}"),
           (0, "rejects reported", "the try swallowed every failure"),
           (kit.rupees(sum(zeroed["Q1"])), "Q1 as summed", "the base of every rate")])
kit.check("the zeroing pass lands on Finance's order counts", all(len(zeroed[q]) == ctl(q)[1] for q in QUARTERS))
'''),
    md("""
    **What happened.** The answer is b. Every order count lands and nothing is rejected, which is exactly
    what a finished pass looks like.

    ## 2. The trap: the rupees do not

    **The plausible wrong answer.** "Q1 Rs 50,63,000 on 98 orders, zero rejects, counts reconciled; Q2
    fell 14.6 percent." Every word of it can be defended except the first number.

    **Predict before you run.** Q1 against Finance's control total: by how much, and which way?

    - a) It lands to the rupee.
    - b) Over by about Rs 10 lakh.
    - c) Short by about Rs 10 lakh.
    - d) Short by a few thousand rupees of rounding.
    """),
    code('''
gap = {q: ctl(q)[0] - sum(zeroed[q]) for q in QUARTERS}
kit.table(["quarter", "orders", "Finance's orders", "summed", "Finance's rupees", "gap"],
          [(q, len(zeroed[q]), ctl(q)[1], kit.rupees(sum(zeroed[q])), kit.rupees(ctl(q)[0]), kit.rupees(gap[q]))
           for q in QUARTERS], caption="Counts land; rupees do not")
kit.columns(["Q1 summed", "Q1, Finance"], [("rupees", [sum(zeroed["Q1"]), ctl("Q1")[0]])], width=460,
            fmt=lambda v: kit.rupees(v), lit=(1,), title="The base of every rate, short by one order's worth")
kit.check("Q1 is short of the control total while Q2 lands", gap["Q1"] > 0 and gap["Q2"] == 0,
          kit.rupees(gap["Q1"]) + " short in Q1")
'''),
    md("""
    **What happened.** The answer is c. The counts reconcile and Q1 is short by Rs 9,85,000, which is 16.3
    percent of the quarter.

    **Why it is wrong.** The `try` turned "I could not read this value" into "this order was worth
    nothing", and zero is a number, so no later step can tell the difference. A count check cannot see
    it, because the row is still there. The note reports a fall of 14.6 percent where the books show
    28.5: the direction is right, so nobody argues, and the size is half, so nobody acts at the right
    scale. The check that catches it is the one chapter 1 made standard, the rupees against the control
    total.
    """),
    md("""
    ## The options

    One value in 207 will not convert. What a team does with it is a decision, and it goes in the log
    either way. The cell below sizes the four answers on this file: the rows touched, what the log and
    the reconciliation then show, and the headline each one sends. The minutes are this programme's
    estimate, and D's is a wait on another team.

    | Option | What it does |
    |---|---|
    | A. Zero in a try | Sets the value to 0 and says nothing |
    | B. Drop with a reason | Rejects the row and logs why |
    | C. Read it, convert, keep and flag | Reads the value without guessing, logs the text and the number |
    | D. Hold and ask the owner | Leaves the row out of today's totals until the order's owner confirms the amount |
    """),
    code('''
def read_amount(v):
    """Digits only, when every character is a digit or a grouping comma; otherwise None."""
    text = v.strip()
    if text and all(ch.isdigit() or ch == "," for ch in text) and text[0].isdigit():
        return int(text.replace(",", ""))
    return None


def run_option(option):
    kept, log = {q: 0 for q in QUARTERS}, []
    counts = {q: 0 for q in QUARTERS}
    for r in once:
        v = r["amount"]
        if v.isdigit():
            kept[r["quarter"]] += int(v)
            counts[r["quarter"]] += 1
            continue
        if option == "A":
            counts[r["quarter"]] += 1
        elif option == "B":
            log.append("drop: value will not convert")
        elif option == "C":
            kept[r["quarter"]] += read_amount(v)
            counts[r["quarter"]] += 1
            log.append("convert and flag: grouping commas removed")
        else:
            log.append("held: asked the order's owner")
    return kept, counts, log


truth = change(ctl("Q1")[0], ctl("Q2")[0])
opt_rows, pts = [], []
for option, minutes in [("A", 1), ("B", 2), ("C", 3), ("D", 240)]:
    kept, counts, log = run_option(option)
    reported = change(kept["Q1"], kept["Q2"])
    count_ok = all(counts[q] == ctl(q)[1] for q in QUARTERS)
    rupee_ok = all(kept[q] == ctl(q)[0] for q in QUARTERS)
    opt_rows.append((option, minutes, 1, len(log), "passes" if count_ok else "fails",
                     "passes" if rupee_ok else "fails", f"{reported:+.1f}%"))
    pts.append((option, abs(reported - truth)))
kit.table(["option", "analyst minutes", "rows touched", "log lines", "count check", "rupee check", "headline sent"],
          opt_rows, caption="Four answers to one value that will not convert, sized on the lab export")
kit.bars([(f"option {o}", round(p, 1)) for o, p in pts], lit=(2,), fmt=lambda v: f"{v:.1f} pts",
         title="Points between each option's headline and the books")
'''),
    code('''
kit.check("only A leaves no trace in the log", [r[3] for r in opt_rows] == [0, 1, 1, 1])
kit.check("B fails the count check, so its gap is visible", opt_rows[1][4] == "fails")
kit.check("C passes both checks", opt_rows[2][4] == opt_rows[2][5] == "passes")
'''),
    md("""
    **The best-fit call.** C. The value can be read without guessing, since it is digits with the
    grouping commas an Indian ledger prints, so converting it costs a minute and one log line and lands
    both quarters on the books. A is the only option that is never right: it produces the same wrong
    headline as B and hides it. B is honest and still wrong by 14 points; its virtue is that the count
    check now fails, so the gap is visible. D is right on the day the text could be read two ways.

    **What would change the call.** Text that cannot be read without a guess moves the call to D: a
    value written as a word, a decimal whose unit is unclear (lakh or crore), a currency that is not the
    file's. A row that is not an order at all, a test transaction, moves it to B. In every case the log
    line and the reconciliation carry the decision, and zero never does.
    """),
    code('''
kit.vflow(["a value that will not convert",
           "can you read it without guessing?",
           "yes: convert, keep and flag it (C)",
           "no, and the row matters: hold it and ask the owner (D)",
           "no, and it is not an order: drop it with a reason (B)"], lit=2,
          title="Three honest answers, and zero is none of them")
'''),
    md("""
    **Your turn.** Find the row the bridge points at and read its value yourself. Type these lines into
    the empty cell below and run it:

    ```python
    for r in once:
        if not r["amount"].isdigit():
            print(r)
    ```

    Then write the decisions-log line you would hand Anand's analyst: the order id, the decision and the
    reason, in one row.
    """),
    empty(),
    md("""
    ## 3. The fix, and what it changes

    **Predict before you run.** With option C, what does the note's first line become?

    - a) Q2 down 14.6 percent, unchanged.
    - b) Q2 down 28.5 percent.
    - c) Q2 up 11.8 percent.
    - d) Q2 down 16.3 percent.
    """),
    code('''
fixed, fixed_counts, fixed_log = run_option("C")
kit.table(["", "Q1", "Q2", "Q1 to Q2"],
          [("zero in a try", kit.rupees(sum(zeroed["Q1"])), kit.rupees(sum(zeroed["Q2"])),
            f"{change(sum(zeroed['Q1']), sum(zeroed['Q2'])):+.1f}%"),
           ("read, convert, flag", kit.rupees(fixed["Q1"]), kit.rupees(fixed["Q2"]),
            f"{change(fixed['Q1'], fixed['Q2']):+.1f}%")], caption="The same rows, two decisions about one value")
kit.check("the fixed pass lands on both control totals", all(fixed[q] == ctl(q)[0] for q in QUARTERS))
'''),
    md("""
    **What happened.** The answer is b. One log line moves the reported fall from 14.6 to 28.5 percent,
    which is Rs 17,22,520 of fall where the zeroing pass reported Rs 7,37,520. In the review, that is the
    difference between "a soft quarter" and "a quarter to explain".

    ## 4. The same shape one step later: a segment that quietly loses a row

    A pass looks clean whenever a step can lose something without saying so. The next place it happens
    is the tree: a filter on the segment name never sees a row whose segment is empty.

    **Predict before you run.** The four named segments are summed per quarter. Do they add back to the
    quarter's total?

    - a) Yes, in orders and in rupees.
    - b) In orders, but not in rupees.
    - c) No, one quarter is short by one order and its value.
    - d) No, both quarters are short by several orders.
    """),
    code('''
SEGS = ("Retail-Core", "Retail-Plus", "Student", "Business")
amt = lambda r: int(r["amount"].replace(",", ""))
seg_sum = {q: sum(amt(r) for r in once if r["quarter"] == q and r["segment"] in SEGS) for q in QUARTERS}
seg_n = {q: sum(1 for r in once if r["quarter"] == q and r["segment"] in SEGS) for q in QUARTERS}
kit.table(["quarter", "named segments, orders", "Finance's orders", "named segments, rupees", "Finance's rupees"],
          [(q, seg_n[q], ctl(q)[1], kit.rupees(seg_sum[q]), kit.rupees(ctl(q)[0])) for q in QUARTERS],
          caption="Segments summed against the quarter")
kit.check("Q2's named segments fall one order short of the quarter",
          ctl("Q2")[1] - seg_n["Q2"] == 1 and seg_n["Q1"] == ctl("Q1")[1])
'''),
    md("""
    **What happened.** The answer is c. Q2's named segments hold one order fewer than the quarter.

    **The plausible wrong answer.** Read one tier on the named rows only, and a tier that grew shows as a
    second falling segment. The cell below computes Retail-Plus both ways: on the named rows, and with
    the unnamed order restored to the only segment its customer's other orders carry.
    """),
    code('''
def plus(q, restore):
    rs = [r for r in once if r["quarter"] == q and r["segment"] == "Retail-Plus"]
    if restore:
        seg_of = {}
        for r in once:
            if r["segment"]:
                seg_of.setdefault(r["customer_id"], set()).add(r["segment"])
        rs += [r for r in once if r["quarter"] == q and not r["segment"]
               and seg_of.get(r["customer_id"]) == {"Retail-Plus"}]
    return len(rs), sum(amt(r) for r in rs)


p1, p2n, p2r = plus("Q1", False), plus("Q2", False), plus("Q2", True)
kit.columns(["Q1", "Q2, named rows", "Q2, restored"], [("Retail-Plus", [p1[1], p2n[1], p2r[1]])],
            fmt=lambda v: kit.rupees(v), lit=(2,), width=560,
            title=f"Retail-Plus: {change(p1[1], p2n[1]):+.1f}% on named rows, {change(p1[1], p2r[1]):+.1f}% restored")
kit.check("the empty cell flips Retail-Plus from a fall to a rise",
          change(p1[1], p2n[1]) < 0 < change(p1[1], p2r[1]))
'''),
    md("""
    **Why it is wrong, and the fix.** Nobody decided to drop the order; the filter did. The check is one
    line, that the segments add back to the quarter in orders and in rupees, and it fails by exactly one
    order. The fix is a logged decision: restore the segment from the customer's other orders when all of
    them carry one segment, flag it, and name it in the caveat; keep it as "segment unknown" when they do
    not.

    ## A second route: account for every value

    The rupee check found the gap from the outside. The second route finds it from the inside, and it
    should land on the same number: every value present in the file is either summed as it came, or
    appears in the log with the number it was read as. Present equals convertible plus logged, and the
    logged values add up to the gap.
    """),
    code('''
present = sum(1 for r in once if r["amount"] != "")
convertible = sum(1 for r in once if r["amount"].isdigit())
logged = [read_amount(r["amount"]) for r in once if not r["amount"].isdigit()]
kit.equation([f"values present\\n{present}", "=", f"convertible\\n{convertible}", "+", f"in the log\\n{len(logged)}"],
              title="The second route: every value is summed or logged")
kit.check("present equals convertible plus logged", present == convertible + len(logged))
kit.check("the logged values add up to the gap the rupee check found", sum(logged) == gap["Q1"],
          kit.rupees(sum(logged)))
'''),
    md("""
    **When to switch routes.** The rupee check needs a control total and tells you how much is missing;
    the value accounting needs nothing outside the file and tells you where. On a file with no control
    total, the value accounting is the check you still have.

    > **Kavya's review.** A count check proves the rows are there. Only a rupee check proves the values
    > survived. Zero is a claim that the order was worth nothing, so never let a `try` make it for you.

    ### In the interview

    **[S] Your cleaning pass reports zero rejects. What do you check?** "I distrust the zero before I
    trust it. First, rows against distinct ids, because a repeated batch is the commonest reason a total
    runs high. Second, how my code handled a value that would not convert: if a `try` set it to zero,
    the rejects count is hiding it. Third, the rupees per period against a control total, with a bridge
    from my number to theirs. On a lab export a zeroing pass reconciled every count and still left the
    base quarter Rs 9,85,000 short, which halved the fall the note reported."

    **[F] How do you handle a value that will not convert?** "Three honest answers: read it and convert
    it when it can be read without guessing, hold it and ask the owner when it cannot, drop it with a
    reason when the row is not an order. Every one gets a log line and shows in the reconciliation.
    Setting it to zero is the one answer I never give, because zero is a number and nothing later can
    tell it from a real one."

    **The design question: when would you drop the row rather than read it?** "When the row is not the
    thing being counted, a test order or a cancelled draft, and the log says so. When the value matters
    and I cannot read it without guessing, I hold it and ask, and the note says the quarter is
    provisional by that amount."

    ### Depth: where else a pass looks clean

    Any step that can lose something silently: a join that drops rows without a match, a date parse
    that sends a bad date to a default, a `groupby` that leaves out a missing key (Week 2 meets that
    one in pandas), a filter on a name that is sometimes blank. The pattern is always the same check:
    what went in equals what came out plus what was set aside, in rows and in value.
    """),
    code("kit.check_summary()"),
]

# --------------------------------------------------------------------------------- chapter 3
CH3 = [
    md("""
    # 3. The headline on too few orders

    **Week 1, Friday. The lab debrief, chapter 3 of 3: which finding leads the note, and how sure is it?**

    Meera Raghavan reads the first line of a note and acts on it. With the data reconciled, the question
    becomes which of the right numbers deserves the first line.

    **The metric at stake.** The Q1 to Q2 fall of Rs 17,22,520, split along the revenue tree by segment:
    customers, orders per customer and revenue per order. **Who asks.** Meera, who needs to know which
    branch to open, and Marketing, who will attack any rate that rests on a handful of orders. **What a
    wrong number costs.** A trend claimed from a few orders sends a team to fix a segment that did
    nothing, while the branch that did move goes unopened for a quarter; and the first time Marketing
    asks "on how many orders?", the whole note loses the room.

    **Who else faces this.** IMDb will not rank a film in its Top 250 until it has at least 25,000 ratings from
    regular voters, and its weighted rating pulls a title with few votes toward the average of all
    titles (IMDb Help, ratings FAQ, updated 9 February 2026): a 9.4 on a few hundred votes is not
    allowed to beat a 9.0 on a million. A public case shows the cost of ignoring it: Howard Wainer's
    "The Most Dangerous Equation" shows small schools over-represented among both the best and the
    worst performers, because small samples vary more, after the Gates Foundation had put about $1.7
    billion into education grants by 2001, with small schools central to them (Wainer, Picturing the
    Uncertain World, Princeton University Press, 2009, chapter 1).

    **Where this starts.** Chapters 1 and 2 put both quarters on the books to the rupee and restored the
    one order a filter dropped. This chapter reads the clean tree, sizes four ways to choose the lead,
    and closes on the week's shuffle test run on the right unit.
    """ + HONESTY),
    code(LOAD + '''

amt = lambda r: int(r["amount"].replace(",", ""))
kept = {}
for r in rows:
    kept.setdefault(r["order_id"], dict(r))
clean = list(kept.values())
seg_of = {}
for r in clean:
    if r["segment"]:
        seg_of.setdefault(r["customer_id"], set()).add(r["segment"])
for r in clean:
    r["amount"] = amt(r)
    if not r["segment"] and len(seg_of.get(r["customer_id"], ())) == 1:
        r["segment"] = next(iter(seg_of[r["customer_id"]]))
kit.check("the clean data lands on both control totals, from chapters 1 and 2",
          all(sum(r["amount"] for r in clean if r["quarter"] == q) == ctl(q)[0] for q in QUARTERS))
'''),
    code('''
kit.side_by_side(
    kit.ladder(["The reconciliation, skipped", "The pass that looks clean", "The headline on too few orders"],
               lit=2, show=False),
    kit.flow(["profile", "clean, with a log", "reconcile", "decompose", "test", "note"], lit=3, show=False),
)
'''),
    md("""
    ## 1. The tree, segment by segment

    **Predict before you run.** Which segment carries most of the Rs 17,22,520 fall?

    - a) Retail-Core, the segment with the most orders.
    - b) Retail-Plus, the members' tier.
    - c) Business, the corporate book.
    - d) Student, the smallest segment.
    """),
    code('''
SEGS = ("Retail-Core", "Retail-Plus", "Student", "Business")


def tree(q, seg):
    rs = [r for r in clean if r["quarter"] == q and r["segment"] == seg]
    cust = len({r["customer_id"] for r in rs})
    rev = sum(r["amount"] for r in rs)
    return {"orders": len(rs), "customers": cust, "freq": len(rs) / cust, "basket": rev / len(rs), "rev": rev}


T = {(q, s): tree(q, s) for q in QUARTERS for s in SEGS}
kit.table(["segment", "orders Q1 / Q2", "customers", "orders per customer", "revenue per order", "revenue change",
           "rupees moved"],
          [(s, f"{T['Q1', s]['orders']} / {T['Q2', s]['orders']}",
            f"{T['Q1', s]['customers']} / {T['Q2', s]['customers']}",
            f"{T['Q1', s]['freq']:.2f} / {T['Q2', s]['freq']:.2f}",
            f"{kit.rupees(T['Q1', s]['basket'])} / {kit.rupees(T['Q2', s]['basket'])}",
            f"{change(T['Q1', s]['rev'], T['Q2', s]['rev']):+.1f}%",
            kit.rupees(T['Q2', s]['rev'] - T['Q1', s]['rev'])) for s in SEGS],
          caption="The clean tree, Q1 against Q2")
fall = ctl("Q1")[0] - ctl("Q2")[0]
biz = T["Q1", "Business"]["rev"] - T["Q2", "Business"]["rev"]
kit.bars([(s, abs(T['Q2', s]['rev'] - T['Q1', s]['rev'])) for s in SEGS], lit=(3,), fmt=lambda v: kit.rupees(v),
         title="Rupees moved per segment, Q1 to Q2, either direction")
kit.check("the segments add back to the quarter", all(sum(T[q, s]["rev"] for s in SEGS) == ctl(q)[0] for q in QUARTERS))
'''),
    md("""
    **What happened.** The answer is c. Business carries Rs 17,10,000 of the Rs 17,22,520 fall, which is
    99.3 percent of it. Business revenue fell 29.2 percent.

    ## 2. The trap: the headline on too few orders

    **The plausible wrong answer.** "The corporate book fell 29.2 percent from Q1 to Q2 and drove the
    whole decline; we recommend a corporate retention plan." It is true to the rupee, it is the biggest
    number on the page, and it is the headline many notes led with.

    **Predict before you run.** How many orders does that 29.2 percent rest on?

    - a) About 200, the whole file.
    - b) About 90, the corporate share of orders.
    - c) Ten: six in Q1 and four in Q2.
    - d) It cannot be counted from the export.
    """),
    code('''
b1, b2 = T["Q1", "Business"], T["Q2", "Business"]
kit.stats([(f"{change(b1['rev'], b2['rev']):+.1f}%", "Business revenue", "the rate the note led with"),
           (f"{b1['orders']} then {b2['orders']}", "orders", "what the rate rests on"),
           (kit.rupees(biz), "the fall it carries", f"{100 * biz / fall:.1f}% of the quarter's fall")])
kit.check("the corporate rate rests on fewer than thirty orders", b1["orders"] + b2["orders"] < 30,
          f"{b1['orders'] + b2['orders']} orders")
'''),
    md("""
    **What happened.** The answer is c. The rate rests on ten orders. A corporate order here is worth
    several lakh, so two fewer of them move the book by 29 percent.

    **Why it is wrong.** The rupees are real and Meera should hear them. What the ten orders cannot carry
    is the word "trend", or a plan built on it. The check is to count before you rate: put the order count
    beside every rate before deciding which one leads, and ask how often chance alone moves six orders to
    four. If each of the ten corporate orders were equally likely to land in either quarter, the cell
    below counts how often the split comes out at least as uneven as six and four.
    """),
    code('''
from math import comb
n = b1["orders"] + b2["orders"]
even = comb(n, n // 2) / 2 ** n
p_split = 1 - even if abs(b1["orders"] - b2["orders"]) >= 2 else 1.0
kit.columns(["as even as 5 and 5", "at least as uneven as 6 and 4"], [("share of coin-flip worlds", [even, p_split])],
            fmt=lambda v: f"{v:.3f}", lit=(1,), width=520,
            title=f"Ten orders split by coin flips: uneven by two or more in {p_split:.1%} of worlds")
kit.check("chance alone gives a split this uneven in most worlds", p_split > 0.5, f"{p_split:.3f}")
'''),
    md("""
    **The fix, and what it changes.** The corporate fall goes into the note as counts, never as a rate:
    "Rs 17,10,000 of the fall is two fewer corporate orders, six in Q1 and four in Q2." Its action is a
    question to whoever owns those accounts (which two did not reorder, and why), which costs a phone call.
    The lead moves to the branch that moved on enough orders to read.

    ## The options

    How does a team choose which finding leads? Four ways, each sized below on the clean tree: the claim
    it leads with, the orders behind that claim, how often chance alone produces it, and the analyst
    minutes it costs at the lab brief's pace.

    | Option | How it picks the lead |
    |---|---|
    | A. The biggest rupee move | Whatever moved most in rupees leads |
    | B. The total, unsplit | The quarter's change leads and the split is left out |
    | C. Count before rate | Every rate carries its order count; a rate on fewer than about thirty orders goes to the caveat as counts, and the lead is the branch that moved on enough orders and survives one test |
    | D. Test everything | A shuffle test on every segment, and the smallest p-value leads |
    """),
    code('''
def basket_change(rs):
    a = [r["amount"] for r in rs if r["quarter"] == "Q1"]
    b = [r["amount"] for r in rs if r["quarter"] == "Q2"]
    return change(sum(a) / len(a), sum(b) / len(b))


core = [r for r in clean if r["segment"] == "Retail-Core"]
plus = [r for r in clean if r["segment"] == "Retail-Plus"]
observed = basket_change(core) - basket_change(plus)
groups = {}
for r in core + plus:
    groups.setdefault(r["customer_id"], []).append(r)
members = sorted(groups)
n_core = len({r["customer_id"] for r in core})


def shuffled_gap(rng):
    m = members[:]
    rng.shuffle(m)
    return basket_change([r for c in m[:n_core] for r in groups[c]]) - basket_change([r for c in m[n_core:] for r in groups[c]])


rng = random.Random(7)
gaps = [shuffled_gap(rng) for _ in range(2000)]
p_core = sum(1 for g in gaps if abs(g) >= abs(observed)) / 2000
false_alarm = 1 - 0.95 ** 4
kit.table(["option", "leads with", "orders behind it", "chance alone", "analyst minutes"], [
    ("A. biggest rupee move", f"Business {change(b1['rev'], b2['rev']):+.1f}%", n, f"{p_split:.2f} (coin flips)", 5),
    ("B. the total, unsplit", f"revenue {change(ctl('Q1')[0], ctl('Q2')[0]):+.1f}%", ctl("Q1")[1] + ctl("Q2")[1],
     "not asked", 2),
    ("C. count before rate", f"Retail-Core basket {basket_change(core):+.1f}%, "
     f"{kit.rupees(T['Q1', 'Retail-Core']['rev'] - T['Q2', 'Retail-Core']['rev'])}", len(core), f"{p_core:.4f} (shuffle)", 15),
    ("D. test everything", "the smallest of four p-values", "10 to 88", f"{false_alarm:.2f} false alarm", 45),
], caption="Four ways to choose the lead, sized on the clean tree")
kit.matrix(["enough orders", "too few orders"], ["moved in rupees", "moved in rate only"],
           [["lead with it, tested", "lead only if it survives a test"],
            ["say it as counts, ask the owner", "leave it out of the claim"]],
           title="Where each finding goes in the note")
'''),
    code('''
kit.check("Retail-Core's basket rests on more than thirty orders", len(core) > 30, f"{len(core)} orders")
kit.check("the Retail-Core gap is one chance rarely produces, at the customer level", p_core < 0.05, f"p = {p_core:.4f}")
'''),
    md("""
    **The best-fit call.** C. It costs about fifteen minutes and one test, and it leads with a finding
    that rests on 88 orders and that came up as large in only about 2 of every 100 chance-only worlds.
    It is small in rupees, Rs 15,400 of the fall, about 0.9 percent of it, so it leads among consumers
    as the one move on enough orders to test, while the corporate Rs 17,10,000 sits beside it in the
    claim as counts.
    A leads on ten orders. B hides the one thing Meera most needs, that 99 percent of the fall is two
    orders. D spends three times the minutes to run four tests, and with four tests at 0.05 the chance
    that at least one looks real by luck is about 19 percent.

    **What would change the call.** A question about accounts rather than rates: if Meera asked "what
    happened to our corporate revenue?", the lead is the corporate fall, said as counts, with the two
    accounts named by their owner. A corporate book of hundreds of orders a quarter would let its rate
    lead. And a second quarter of the same move in Business would turn a phone call into a trend worth
    testing.

    ## 3. The branch that moved, tested on the right unit

    Retail-Core keeps its 30 customers and orders about 1.47 times each in both quarters, while its
    revenue per order falls. Thursday's test asks whether that fall differs from Retail-Plus's by more
    than chance produces. The label is shuffled across customers, because a customer's orders belong
    together.

    **Predict before you run.** Where does the observed gap sit among 2,000 customer-level shuffles?

    - a) In the middle of the pile.
    - b) At the edge: only a few dozen shuffles are as large.
    - c) Beyond every shuffle.
    - d) The test cannot run with segments of different sizes.
    """),
    code('''
print(f"observed gap {observed:+.1f} points; {round(p_core * 2000)} of 2,000 customer shuffles as large; p = {p_core:.4f}")
kit.strip(gaps, markers=[("observed", observed, "bad"), ("its mirror", -observed, "plain")], lo=-24, hi=24,
          fmt=lambda v: f"{v:+.0f}", title="2,000 chance-only worlds against Retail-Core's basket gap")
kit.check("Retail-Core's customers and frequency hold while its basket falls",
          T["Q1", "Retail-Core"]["customers"] == T["Q2", "Retail-Core"]["customers"]
          and abs(T["Q1", "Retail-Core"]["freq"] - T["Q2", "Retail-Core"]["freq"]) < 0.01)
'''),
    md("""
    **What happened.** The answer is b. Only 39 of 2,000 shuffles produce a gap as large, p = 0.0195:
    a gap this size turns up in about 2 of every 100 worlds where segment made no difference. That is a
    share of chance-only worlds, never the chance the finding is wrong.

    **The note, with the right lead.** Claim: booked revenue fell 28.5 percent, Rs 60,48,000 to Rs
    43,25,480; Rs 17,10,000 of it is two fewer corporate orders (six, then four), and among consumers the
    branch that moved is Retail-Core's revenue per order, down 17.1 percent with its 30 customers and
    their frequency unchanged. Evidence: both quarters reconcile to Finance's control totals; the basket
    gap came up in 39 of 2,000 customer-level shuffles. Caveat: the corporate move rests on ten orders.
    Action: ask the corporate account owner which two accounts did not reorder, and open Retail-Core's
    basket (items per order and price per item) before any spend.

    ## A second route: customer by customer

    The shuffle compares averages. A second route reads each customer on their own: of Retail-Core's
    customers who ordered in both quarters, how many saw their own average order fall? If the basket
    fall is real and broad, most of them should.
    """),
    code('''
per = {}
for r in core:
    per.setdefault(r["customer_id"], {"Q1": [], "Q2": []})[r["quarter"]].append(r["amount"])
both = {c: v for c, v in per.items() if v["Q1"] and v["Q2"]}
fell = sum(1 for v in both.values() if sum(v["Q2"]) / len(v["Q2"]) < sum(v["Q1"]) / len(v["Q1"]))
rose = sum(1 for v in both.values() if sum(v["Q2"]) / len(v["Q2"]) > sum(v["Q1"]) / len(v["Q1"]))
kit.columns(["own basket fell", "own basket rose", "unchanged"], [("customers", [fell, rose, len(both) - fell - rose])],
            lit=(0,), width=520, title=f"Retail-Core customers who ordered in both quarters: {len(both)}")
kit.check("most customers who ordered in both quarters saw their own basket fall", fell > len(both) / 2,
          f"{fell} of {len(both)}")
kit.check("the second route points the same way as the shuffle", (fell > rose) == (basket_change(core) < 0))
'''),
    md("""
    **When to switch routes.** The shuffle says whether the gap is bigger than chance; the customer count
    says whether it is broad or carried by a few people. When the two disagree, a handful of customers
    moved the average, and the note says so.

    > **Kavya's review.** Say the count before the rate, every time. "Six orders, then four" is honest.
    > "Down 29 percent" alone is a headline, and Marketing will take it apart with one question.

    ### In the interview

    **[S] Tell me about an analysis you did: what did you find, and how sure are you?** "On a two-quarter
    export, revenue fell 28.5 percent after I reconciled it to Finance's control totals. Almost all of it
    was two fewer corporate orders, six against four, which I reported as counts and passed to the account
    owner rather than calling a trend. The finding I led with was Retail-Core's revenue per order, down
    17.1 percent on 88 orders with customers and frequency flat; a customer-level shuffle put the gap at
    p = 0.02, and 21 of its 30 customers saw their own basket fall. My caveat was the ten corporate
    orders."

    **[D] A stakeholder attacks your caveat in front of the room.** "I restate the claim with its count,
    bound what the data can say, and offer the test that would settle it with its size and time. For the
    corporate book: ten orders cannot tell a trend from two accounts pausing; a call to the account owner
    settles which it is by Monday."

    **The design question: four segments moved; which do you test?** "One: the branch the tree says moved
    on enough orders to read. Testing all four at 0.05 gives about a one-in-five chance that something
    looks real by luck, and a test on ten orders cannot say anything a count does not."

    ### Depth: the wrong unit, and the typical order

    Shuffling orders instead of customers treats a customer's orders as independent and builds worlds that
    could not exist. The wrong unit can move p either way. Most often it makes p too small, because
    correlated orders count as extra evidence and a chance gap looks real. Here the gap is each
    customer's own change from Q1 to Q2, and the order shuffle breaks that pairing, so p comes out
    larger. The cell below reruns the test that way.
    """),
    code('''
both_rows = core + plus
rng = random.Random(7)
ext = 0
for _ in range(2000):
    idx = list(range(len(both_rows)))
    rng.shuffle(idx)
    a = [both_rows[i] for i in idx[:len(core)]]
    b = [both_rows[i] for i in idx[len(core):]]
    if abs(basket_change(a) - basket_change(b)) >= abs(observed):
        ext += 1
amounts = sorted(r["amount"] for r in clean)
kit.table(["measure", "value"], [("p, shuffling customers", f"{p_core:.4f}"), ("p, shuffling orders", f"{ext / 2000:.4f}"),
                                 ("mean order, clean", kit.rupees(statistics.mean(amounts))),
                                 ("median order, clean", kit.rupees(statistics.median(amounts)))],
          caption="Two more ways a clean file still misleads")
kit.check("shuffling the wrong unit moves the verdict across 0.05", ext / 2000 > 0.05 > p_core)
'''),
    md("""
    The mean order is pulled up by the corporate orders, so it describes no order anybody placed; the
    median is the typical one, and the mean belongs in anything that must reconcile.
    """),
    code("kit.check_summary()"),
]

CHAPTERS = [
    ("C2_W01_D05_01_reconciliation_skipped_STUDENT.ipynb", CH1),
    ("C2_W01_D05_02_pass_that_looks_clean_STUDENT.ipynb", CH2),
    ("C2_W01_D05_03_headline_on_few_orders_STUDENT.ipynb", CH3),
]

if __name__ == "__main__":
    for name, cells in CHAPTERS:
        build(NB / name, cells)
        print("built", name, len(cells), "cells")

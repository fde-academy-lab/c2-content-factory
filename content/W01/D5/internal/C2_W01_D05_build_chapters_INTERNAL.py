"""Build the lab debrief's three chapter notebooks, one per place most rooms break.

    python3 content/W01/D5/internal/C2_W01_D05_build_chapters_INTERNAL.py

Each notebook pairs with one chapter of slides/C2_W01_D05_debrief_STUDENT.md by number and title,
runs cold in notebooks/ on the lab export, and opens only after the lab clock stops. The data is
v3-lab, proposed for client zero v2.3 and not yet locked.

No saved output and no markdown line names a planted value: not an order id, a raw value, a count,
a rupee amount, the form of a value or the quarter or segment a plant sits in. Where a learner needs
to see one, the markdown gives the lines to type and the cell below it ships empty; where a
mechanism needs numbers to show, it is drawn on the invented export of
internal/C2_W01_D05_invented_export_INTERNAL.py, labelled invented. The file names describe what
each chapter examines, so a folder listing during the lab names no trap.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, md, code, empty, build  # noqa: E402

DAY = ROOT / "content" / "W01" / "D5"
NB = DAY / "notebooks"

# The shared opening: the lab export and the control totals, so every chapter starts from the same
# state without importing another notebook.
LOAD = SETUP + '''
import random
import statistics
from math import comb

rows = kit.load_csv("C2_W01_D05_lab_orders_STUDENT.csv")
control = {c["quarter"]: c for c in kit.load_csv("C2_W01_D05_lab_control_STUDENT.csv")}
QUARTERS = ("Q1", "Q2")


def change(a, b):
    """Percentage change from a to b."""
    return 100 * (b / a - 1)


def ctl(q):
    return int(control[q]["amount_rs"]), int(control[q]["orders"])


def read_value(text):
    """The number a person reads without a guess from a value typed with grouping commas, spaces,
    a Rs prefix or paise; None when reading it would need a guess."""
    t = str(text).strip().replace("Rs", "").replace(",", "").replace(" ", "")
    try:
        return round(float(t))
    except ValueError:
        return None


print(f"{len(rows)} rows read from the lab export; Finance's control totals for {', '.join(sorted(control))}")
'''

HONESTY = """
    **Before you read on.** This notebook runs on this morning's lab export. A cell that would show
    what sits in the file ships empty, with the lines to type in the markdown above it, so the file
    keeps its findings for whoever meets it cold; type them and run them. Where a mechanism needs
    numbers before yours, it is drawn on the debrief deck's invented export and labelled invented.
    The notebook opens after the lab clock stops, and it is the debrief's text for self-study too.
"""

MAP = '''
kit.side_by_side(
    kit.ladder(["The reconciliation, skipped", "The pass that looks clean", "The headline on too few orders"],
               lit={lit}, show=False),
    kit.flow(["profile", "clean, with a log", "reconcile", "decompose", "test", "note"], lit={step}, show=False),
)
'''

# --------------------------------------------------------------------------------- chapter 1
CH1 = [
    md("""
    # 1. The reconciliation, skipped

    **Week 1, Friday. The lab debrief, chapter 1 of 3: do the quarters in your note match the books?**

    Anand Iyer, finance controller, said it on Wednesday and it still holds: "Until your numbers match
    ours, Finance will not act on a drop measured from an ERP export."

    **The metric at stake.** Booked revenue per quarter, the rupees of the orders recorded as sales in
    it, and the change from Q1 to Q2 that the note to Meera Raghavan leads with. **Who asks.** Anand,
    before he lets any number reach Meera's growth review, and Meera, who acts on the first line of the
    note. **What a wrong number costs.** A first line that points the wrong way sends Monday's review
    after the wrong question, and Marketing's Rs 12 crore acquisition request gets judged against a
    quarter that did not happen. Anand returns the note, and the team's next number is read with
    suspicion.

    **Who else faces this.** Nykaa, the beauty and fashion retailer, reports two numbers for the same
    quarter: gross merchandise value (GMV), the value of everything customers ordered at the prices
    charged, before cancellations, returns and tax come out, and revenue from operations, the income the
    company books in its own accounts. For April to June 2025 they were Rs 4,182 crore and Rs 2,155
    crore (FSN E-Commerce Ventures press release, 12 August 2025). An analyst there who quotes one to
    the owner of the other is out by nearly half, so every internal figure says which it is and bridges
    to the books. A public case shows what an unreconciled pipeline hides: in October 2020 Public Health
    England said 15,841 positive COVID-19 cases from 25 September to 2 October had been left out of the
    reported daily figures because files exceeded a size limit (UK government statement, 4 October
    2020). No step raised an error; the rows were simply not there.

    **Where this starts.** This morning each of you ran the week's method alone on the lab export. This
    notebook replays the step most rooms dropped when the clock ran, the reconciliation, and shows what
    the note said without it. Chapter 2 picks up the case where a count check passes and the rupees do
    not; chapter 3 takes the clean numbers into the tree.
    """ + HONESTY),
    code(LOAD),
    code(MAP.format(lit=0, step=2)),
    md("""
    **The passes, as two small functions.** `quarter_totals` sums each quarter, either reading every
    value with `read_value` from the first cell, which reads the forms a person reads without a guess,
    or setting any value that will not convert to zero, the way the hurried pass did; `first_of_each`
    keeps one row per order id, Wednesday's identity rule.
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
            s += (int(v) if v.isdigit() else 0) if text_to_zero else read_value(v)
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
kit.stats([(f"{h_change:+.1f}%", "Q1 to Q2, the hurried run", "the line the note led with"),
           (f"{truth:+.1f}%", "Q1 to Q2, Finance's books", "from the control file"),
           ("0", "errors raised", "the pass ran to the end")])
kit.bars([("the hurried run: a rise", round(abs(h_change), 1)), ("Finance's books: a fall", round(abs(truth), 1))],
         fmt=lambda v: f"{v:.1f}%", lit=(1,), width=640,
         title="One export, two first lines that point opposite ways (the size of each change)")
'''),
    md("""
    **What happened.** The answer is b. The pass reports Q2 up 11.8 percent, and Finance's own control
    file says the quarter fell 28.5 percent.

    **The plausible wrong answer.** "Q2 grew 11.8 percent; no action needed on the top line." The
    arithmetic is right, the file is Finance's own export, and nothing on the screen looks broken.

    **Why it is wrong.** Nobody asked whether the data summed is the data Finance booked. Sent to Meera,
    the line tells her the quarter that fell was a good one, and the review spends its time on
    Marketing's plans instead of on the fall. The check is one comparison with the control file.

    **Your turn.** Put the hurried run beside Finance's control totals, quarter by quarter, in orders
    and in rupees. Type these lines into the empty cell below and run it:

    ```python
    kit.table(["quarter", "rows summed", "Finance's orders", "rupees summed", "Finance's rupees"],
              [(q, hurried[q][1], ctl(q)[1], kit.rupees(hurried[q][0]), kit.rupees(ctl(q)[0]))
               for q in QUARTERS], caption="The hurried run against the control totals")
    ```

    Which misses does each quarter show: in orders, in rupees, or both?
    """),
    empty(),
    code('''
kit.check("the hurried run misses Finance's rupee totals", any(hurried[q][0] != ctl(q)[0] for q in QUARTERS))
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

    The cell below sizes the options on what separates them: the minutes and cells each costs, what it
    needs from outside the file, the kind of error it can see, and how far the headline it lets through
    sits from the books. It runs the hurried pass and then applies each check, fixing only what that
    check can see. D cannot run here, since the lab had no ledger, so its row says what it would need
    and find and claims no headline. The minutes are the lab brief's pace, and D's is this programme's
    estimate for a request to Finance and a join.
    """),
    code('''
sizing = []
for name, minutes, cells, needs, sees, dedupe, text_fixed in [
        ("A. trust the pass", 0, 0, "nothing", "nothing", False, False),
        ("B. count check", 2, 1, "Finance's order counts", "rows beyond Finance's orders", True, False),
        ("C. counts and rupees, bridge", 15, 3, "Finance's rupee totals too",
         "extra rows, and rupees the kept rows lost", True, True)]:
    t = quarter_totals(first_of_each(rows) if dedupe else rows, text_to_zero=not text_fixed)
    reported = change(t["Q1"][0], t["Q2"][0])
    sizing.append((name, minutes, cells, needs, sees, f"{reported:+.1f}%", round(abs(reported - truth), 1)))
sizing.append(("D. order-level match", "about 120", 6, "Finance's ledger", "every order that differs, by id",
               "not run: no ledger", "not run"))
kit.table(["option", "analyst minutes", "cells", "what it needs", "what it can see", "Q1 to Q2 it lets through",
           "points off the books"], sizing,
          caption=f"Four ways to check, sized on the lab export; the books say {truth:+.1f}%")
kit.bars([(s[0], s[6]) for s in sizing[:3]], lit=(2,), fmt=lambda v: f"{v:.1f} pts",
         title="How far each option's headline sits from the books, in percentage points")
'''),
    code('''
kit.check("only C, of the options that can run here, lands on the books",
          sizing[2][6] == 0 and all(s[6] > 1 for s in sizing[:2]))
kit.check("the count check moves the headline and still misses the books",
          sizing[1][5] != sizing[0][5] and sizing[1][6] > 1)
'''),
    md("""
    **The best-fit call.** C. It costs about fifteen minutes of an analyst's two hours, needs only the
    control file that came with the export, and is the only option run here that lands on the books to
    the rupee. B is the option most people who did check stopped at, and it still leaves the headline
    about 14 points off. D would name every order that differs, which C cannot, and it costs a request
    to Finance and most of the afternoon.

    **What would change the call.** No control total at all: then C has nothing to land on, and D, or a
    second export pulled from the source system for the same quarters, becomes the check. A bridge that
    does not close: then C has told you there is a gap it cannot explain, and D is how you find it.
    """),
    md("""
    ## 2. The count check

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
seen, rejected = set(), []
for r in rows:
    if r["order_id"] in seen:
        rejected.append(r)
    seen.add(r["order_id"])
kit.check("input equals kept plus rejected, each list built on its own", len(rows) == len(once) + len(rejected))
kit.check("the order counts now land on Finance's in both quarters",
          all(counted[q][1] == ctl(q)[1] for q in QUARTERS))
kit.check("the rupees still miss Finance's control totals", any(counted[q][0] != ctl(q)[0] for q in QUARTERS))
print(f"Q1 to Q2 after the count check: {c_change:+.1f}%; the books say {truth:+.1f}%")
'''),
    md("""
    **What happened.** The answer is c. Every order count lands, and the headline moves from +11.8 to
    -14.6 percent: the right direction and half the size. A count check proves the rows are there; it
    says nothing about whether each row's value survived the conversion. That is chapter 2's trap, and it
    is the one a pass that "looks clean" leaves behind.

    **Your turn.** See what the count check kept and set aside. Type these lines into the empty cell
    below and run it:

    ```python
    kit.table(["quarter", "orders kept", "Finance's orders", "rupees kept", "Finance's rupees"],
              [(q, counted[q][1], ctl(q)[1], kit.rupees(counted[q][0]), kit.rupees(ctl(q)[0]))
               for q in QUARTERS],
              caption=f"After the count check: {len(rows)} rows read, {len(once)} kept, {len(rejected)} set aside")
    ```
    """),
    empty(),
    md("""
    ## 3. Counts and rupees, and the bridge between them

    Option C adds the rupee comparison and draws the walk from what the hurried run summed to what
    Finance booked, one move per decision in the log. The first bridge below is drawn on invented
    numbers, the invented export on the debrief's slides, so the shape is visible before you draw your
    own: an export as a hurried pass summed it, the rows Finance does not hold taken out, the value that
    would not convert read back in, and the walk landing on Finance's two quarters. None of its numbers
    is Kalpa's or this morning's.

    **Predict before you run.** On the invented export, which move is the larger?

    - a) The rows the control total does not contain.
    - b) The value that would not convert.
    - c) They are equal.
    - d) Neither; the bridge closes with no moves.
    """),
    code('''
# Invented numbers: the debrief deck's invented export, labelled invented wherever they appear.
kit.bridge(("the hurried sum", 6_966_420), [("rows Finance does not hold", -1_216_420),
                                            ("a value read back", 850_000)],
           end_label="clean, both quarters", lit=[0], lo=5_000_000,
           title="Invented numbers: from a hurried sum to the books (the axis starts at Rs 50 lakh)")
'''),
    code('''
clean = quarter_totals(once, text_to_zero=False)
as_read = sum(hurried[q][0] for q in QUARTERS)
extra_rows = sum(counted[q][0] for q in QUARTERS) - as_read
text_back = sum(clean[q][0] for q in QUARTERS) - sum(counted[q][0] for q in QUARTERS)
kit.check("this morning's bridge lands on Finance's two quarters together",
          as_read + extra_rows + text_back == ctl("Q1")[0] + ctl("Q2")[0], kit.rupees(ctl("Q1")[0] + ctl("Q2")[0]))
kit.check("both quarters land, orders and rupees", all(clean[q] == ctl(q) for q in QUARTERS))
'''),
    md("""
    **What happened.** The answer is a, on the invented export: the rows Finance does not hold carry
    Rs 12,16,420 against the Rs 8,50,000 read back, and both moves had to be found before the walk
    landed. The checks above say this morning's bridge lands too.

    **Your turn.** Draw this morning's bridge and read which move is the larger on this file. Type these
    lines into the empty cell below and run it:

    ```python
    kit.bridge(("the hurried sum", as_read), [("rows Finance does not hold", extra_rows),
                                              ("a value read back", text_back)],
               end_label="clean, both quarters", lit=[0], lo=9_000_000,
               title="From the hurried sum to the books (the axis starts at Rs 90 lakh)")
    ```
    """),
    empty(),
    md("""
    **The fix, and what it changes.** With both quarters on the books, the headline is a fall of 28.5
    percent, from Rs 60,48,000 to Rs 43,25,480. The note changes sign, so the decision changes with it:
    Monday's review now has a fall of Rs 17,22,520 to explain, and chapter 3 finds where it sits.
    """),
    code('''
variants = [("the hurried run", hurried), ("count check only", counted), ("counts and rupees", clean)]
heads = [(n, change(t["Q1"][0], t["Q2"][0])) for n, t in variants]
kit.table(["run", "Q1 to Q2"], [(n, f"{h:+.1f}%") for n, h in heads], caption="One export, three headlines")
kit.bars([(f"{n}: {'a rise' if h > 0 else 'a fall'}", round(abs(h), 1)) for n, h in heads], lit=(2,),
         fmt=lambda v: f"{v:.1f}%", width=640, title="The same file, three first lines (the size of each change)")
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
    ## A second route: sum the decisions themselves

    The bridge's two moves were found by subtracting one total from another. The second route builds the
    evidence on its own and sums it: every row set aside as a repeat of an order already kept, summed
    from the set-aside list, and every value read back from text, summed from the decisions log. Each
    must equal its move in the bridge. The first route is arithmetic on totals, and this one is a sum of
    the decisions themselves, so a row set aside without its log line, or a value zeroed where it should
    have been read, makes the two disagree.
    """),
    code('''
set_aside, log, kept_ids = [], [], set()
for r in rows:
    if r["order_id"] in kept_ids:
        set_aside.append(r)
        continue
    kept_ids.add(r["order_id"])
    if not r["amount"].isdigit():
        log.append({"order_id": r["order_id"], "decision": "convert and flag", "read_as": read_value(r["amount"])})
set_aside_rupees = sum(read_value(r["amount"]) for r in set_aside)
read_back = sum(e["read_as"] for e in log)
kit.equation(["the set-aside list\\nsummed", "+", "the log's values\\nsummed", "=", "the bridge's\\ntwo moves"],
             title="The second route: the decisions, summed on their own")
kit.check("the rows set aside add up to the rupees the bridge took out", set_aside_rupees == -extra_rows)
kit.check("the values in the log add up to the rupees the bridge read back", read_back == text_back)
'''),
    md("""
    **When to switch routes.** Show Finance the forward bridge, because it starts from their export.
    Run this second route before you send it: it proves every rupee the bridge moved is a row in the
    set-aside list or a value in the log, each summed on its own. It cannot tell you whether each
    decision was right, whether a row set aside really repeats an order or a value was read correctly;
    the order-level match is what answers that.

    ### Depth: the same rows can move a branch

    Rows Finance does not hold inflate a total, and when they sit in one segment they can move a branch
    as well: extra rows for the same customers read as customers ordering more often. **Your turn.** Run
    the tree on the hurried rows and on the one-row-per-order list for each consumer segment, and compare
    the orders-per-customer branch:

    ```python
    def branch(src, q, seg):
        rs = [r for r in src if r["quarter"] == q and r["segment"] == seg and r["amount"].isdigit()]
        return len(rs) / len({r["customer_id"] for r in rs}), sum(int(r["amount"]) for r in rs) / len(rs)

    for seg in ("Retail-Core", "Retail-Plus", "Student"):
        (fh1, _), (fh2, _) = branch(rows, "Q1", seg), branch(rows, "Q2", seg)
        (fc1, bc1), (fc2, bc2) = branch(once, "Q1", seg), branch(once, "Q2", seg)
        print(f"{seg}: orders per customer {fh1:.2f} to {fh2:.2f} on the hurried rows, "
              f"{fc1:.2f} to {fc2:.2f} one row per order; revenue per order {change(bc1, bc2):+.1f}%")
    ```

    Where do the rows Finance does not hold sit, and which branch would a note built on the hurried rows
    have named?
    """),
    empty(),
    md("""
    > **Kavya's review.** A number that has not been reconciled can point the wrong way, and this
    > morning it did. Put the two checks in a cell before you compute the first number you plan to
    > send, so the clock cannot remove them.

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
    rupees". A pass that reports zero rejects on a file everyone knows is dirty is the one they open
    first.

    **The metric at stake.** Q1 booked revenue, the base every Q1 to Q2 rate is measured from.
    **Who asks.** Anand's analyst, auditing the note, and Meera, who reads the size of the fall as the
    size of the problem. **What a wrong number costs.** A base that is short by one large order can halve
    the fall the note reports, so Monday's review sizes the problem at half its real size and the fix
    gets half the attention; when Finance finds the missing order, every other number in the note is
    doubted with it.

    **Who else faces this.** JPMorgan Chase's own task force reviewed the losses from the 2012 "London
    Whale" trades, as the high-risk trading in the Synthetic Credit Portfolio of the bank's Chief
    Investment Office became known (FCA, 19 September 2013). It found that a risk model run through
    spreadsheets "divided by their sum instead of their average", which "likely had the effect of
    muting volatility by a factor of two and of lowering the VaR" (the task force report of January
    2013, as quoted by The Baseline Scenario, 9 February 2013). Muting volatility means the model showed
    prices swinging half as much as they did, and VaR, value at risk, is a bank's estimate of how much a
    portfolio could lose on a bad day, so the error made the book look safer than it was. The trading
    losses came to $6.2 billion (FCA, 19 September 2013). Nothing crashed: the sheet produced a plausible
    number every day.

    **Where this starts.** Chapter 1 left one run at -14.6 percent: the order counts landed and the
    rupees did not. This chapter finds out why, sizes the four ways to handle a value that will not
    convert, and then meets the same shape one step later, where a segment filter can drop a row without
    a word. Chapter 3 takes the repaired numbers into the tree.
    """ + HONESTY),
    code(LOAD + '''

def first_of_each(src):
    kept = {}
    for r in src:
        kept.setdefault(r["order_id"], r)
    return list(kept.values())


once = first_of_each(rows)
truth = change(ctl("Q1")[0], ctl("Q2")[0])
print("one row per order id, the identity rule from chapter 1")
'''),
    code(MAP.format(lit=1, step=1)),
    md("""
    ## 1. Zero rejects, and the counts reconcile

    The most natural line of Python in the week wraps the conversion in a `try` and sets a failure to
    zero. It never stops, it reports nothing, and every row survives.

    **Predict before you run.** The pass keeps one row per order and sets any value that will not
    convert to zero. How many orders does Q1 report against Finance's 98, and how many rejects?

    - a) 97 orders and 1 reject.
    - b) 98 orders and 0 rejects.
    - c) 98 orders and 1 reject.
    - d) 96 orders and 2 rejects.
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
           ("all", "rows kept", "nothing set aside")])
kit.check("the zeroing pass lands on Finance's order counts", all(len(zeroed[q]) == ctl(q)[1] for q in QUARTERS))
'''),
    md("""
    **What happened.** The answer is b. Every order count lands and nothing is rejected, which is exactly
    what a finished pass looks like.

    ## 2. The trap: the rupees do not

    **The plausible wrong answer.** "Q1 on 98 orders, zero rejects, counts reconciled; Q2 fell 14.6
    percent." Every word of it can be defended except the number the rate is built on.

    **Predict before you run.** Against Finance's rupee totals, what does the zeroing pass show?

    - a) Both quarters land to the rupee.
    - b) One quarter over, the other landing.
    - c) One quarter short, the other landing.
    - d) Both quarters short by a few rupees of rounding.
    """),
    code('''
z_change = change(sum(zeroed["Q1"]), sum(zeroed["Q2"]))
misses = [q for q in QUARTERS if sum(zeroed[q]) != ctl(q)[0]]
kit.check("every order count lands on Finance's", all(len(zeroed[q]) == ctl(q)[1] for q in QUARTERS))
kit.check("the rupees miss Finance's in one quarter and land in the other",
          len(misses) == 1 and all(sum(zeroed[q]) <= ctl(q)[0] for q in QUARTERS))
kit.bars([("the zeroing pass: a fall", round(abs(z_change), 1)), ("Finance's books: a fall", round(abs(truth), 1))],
         fmt=lambda v: f"{v:.1f}%", lit=(1,), width=640, title="The fall the note reports, against the books")
'''),
    md("""
    **What happened.** The answer is c. The counts reconcile, one quarter's rupees come up short, and the
    note reports a fall of 14.6 percent where the books show 28.5.

    **Your turn.** Which quarter, and by how much? Type these lines into the empty cell below and run it:

    ```python
    gap = {q: ctl(q)[0] - sum(zeroed[q]) for q in QUARTERS}
    kit.table(["quarter", "orders", "Finance's orders", "summed", "Finance's rupees", "gap"],
              [(q, len(zeroed[q]), ctl(q)[1], kit.rupees(sum(zeroed[q])), kit.rupees(ctl(q)[0]), kit.rupees(gap[q]))
               for q in QUARTERS], caption="Counts land; rupees do not")
    ```
    """),
    empty(),
    md("""
    **Why it is wrong.** The `try` turned "I could not read this value" into "this order was worth
    nothing", and zero is a number, so no later step can tell the difference. A count check cannot see
    it, because the row is still there. The note reports a fall of 14.6 percent where the books show
    28.5: the direction is right, so nobody argues, and the size is half, so nobody acts at the right
    scale. The check that catches it is the one chapter 1 made standard, the rupees against the control
    total.

    ## The options

    A value that will not convert is a decision, and it goes in the log either way. The cell below sizes
    four answers on this file on what separates them: what each assumes about the value, the minutes,
    what the log and the reconciliation then show, and the headline each one lets through. The minutes
    are this programme's estimate, and D's is a wait on another team.

    | Option | What it does |
    |---|---|
    | A. Zero in a try | Sets the value to 0 and says nothing |
    | B. Drop with a reason | Rejects the row and logs why |
    | C. Read it, convert, keep and flag | Reads the value without guessing, logs the text and the number |
    | D. Hold and ask the owner | Leaves the row out of today's totals until the order's owner confirms the amount, and the note says it is provisional |
    """),
    code('''
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
            kept[r["quarter"]] += read_value(v)
            counts[r["quarter"]] += 1
            log.append("convert and flag: read without a guess")
        else:
            log.append("held: asked the order's owner")
    return kept, counts, log


opt_rows, pts = [], []
for option, assumes, minutes in [("A", "the order was worth nothing", 1),
                                 ("B", "the row is not an order", 2),
                                 ("C", "the value can be read without a guess", 3),
                                 ("D", "only the order's owner can say", "a wait")]:
    kept, counts, log = run_option(option)
    reported = change(kept["Q1"], kept["Q2"])
    count_ok = all(counts[q] == ctl(q)[1] for q in QUARTERS)
    rupee_ok = all(kept[q] == ctl(q)[0] for q in QUARTERS)
    opt_rows.append((option, assumes, minutes, len(log), "passes" if count_ok else "fails",
                     "passes" if rupee_ok else "fails", "provisional" if option == "D" else f"{reported:+.1f}%"))
    if option != "D":
        pts.append((f"option {option}", round(abs(reported - truth), 1)))
kit.table(["option", "assumes", "analyst minutes", "log lines", "count check", "rupee check", "headline sent"],
          opt_rows, caption="Four answers to a value that will not convert, sized on the lab export")
kit.bars(pts, lit=(2,), fmt=lambda v: f"{v:.1f} pts",
         title="Points between each headline sent and the books (D sends a provisional note)")
'''),
    code('''
kit.check("only A leaves no trace in the log", [r[3] for r in opt_rows] == [0, 1, 1, 1])
kit.check("B fails the count check, so its gap is visible", opt_rows[1][4] == "fails")
kit.check("C passes both checks", opt_rows[2][4] == opt_rows[2][5] == "passes")
'''),
    md("""
    **The best-fit call.** C, when the value can be read without a guess: converting it costs a minute
    and one log line and lands both quarters on the books. A is the only option that is never right: it
    produces the same wrong headline as B and hides it. B is honest and still wrong by 14 points; its
    virtue is that the count check now fails, so the gap is visible. D is right on the day the text could
    be read two ways.

    **What would change the call.** Text that cannot be read without a guess moves the call to D: a
    value written as a word, a decimal whose unit is unclear (lakh or crore), a currency that is not the
    file's. A row that is not an order at all, a test transaction, moves it to B. In every case the decision
    lives in a log line and shows in the reconciliation.
    """),
    code('''
kit.vflow(["a value that will not convert",
           "can you read it without guessing?",
           "yes: convert, keep and flag it (C)",
           "no, and the row matters: hold it and ask the owner (D)",
           "no, and it is not an order: drop it with a reason (B)"], lit=2,
          title="Three honest answers to a value that will not convert")
'''),
    md("""
    **Your turn.** Find the row the rupee check points at and read its value yourself. Type these lines
    into the empty cell below and run it:

    ```python
    for r in once:
        if not r["amount"].isdigit():
            print(r)
    ```

    Can this value be read without a guess, and so which option does it call for? Write the
    decisions-log line you would hand Anand's analyst: the order id, the decision and the reason, in one
    row.
    """),
    empty(),
    md("""
    ## 3. The fix, and what it changes

    **Predict before you run.** With option C, what does the note's first line become?

    - a) Q2 down 14.6 percent, unchanged.
    - b) Q2 down 28.5 percent.
    - c) Q2 up 11.8 percent.
    - d) Q2 down about a fifth.
    """),
    code('''
fixed, fixed_counts, fixed_log = run_option("C")
kit.table(["the decision about the value", "Q1 to Q2"],
          [("zero in a try", f"{change(sum(zeroed['Q1']), sum(zeroed['Q2'])):+.1f}%"),
           ("read, convert, flag", f"{change(fixed['Q1'], fixed['Q2']):+.1f}%")],
          caption="The same rows, two decisions about one value")
kit.check("the fixed pass lands on both control totals", all(fixed[q] == ctl(q)[0] for q in QUARTERS))
'''),
    md("""
    **What happened.** The answer is b. One log line moves the reported fall from 14.6 to 28.5 percent,
    which is Rs 17,22,520 of fall on the books. In the review, that is the difference between "a soft
    quarter" and "a quarter to explain".

    ## 4. The same shape one step later: a segment that quietly loses a row

    A pass looks clean whenever a step can lose something without saying so. The next place it happens
    is the tree: a filter on the segment name never sees a row whose segment is empty. The mechanism
    first, on the debrief deck's invented export: one Q1 Retail-Core order there has no segment, so on
    named rows Retail-Core's Q1 is Rs 73,250 and the segment reads up 2.2 percent to Q2's Rs 74,880;
    with the order restored from its customer's other order, Q1 is Rs 75,600 and the segment fell 1.0
    percent. A segment that fell reads as a rise, and nobody decided it.
    """),
    code('''
# Invented numbers: the debrief deck's invented export, labelled invented wherever they appear.
kit.columns(["Q1, named rows", "Q1, order restored", "Q2"], [("Retail-Core, invented", [73_250, 75_600, 74_880])],
            fmt=lambda v: kit.rupees(v), lit=(1,), width=560,
            title="Invented: one unnamed Q1 order turns a small fall into a rise")
'''),
    md("""
    **Your turn.** Do this file's named segments add back to each quarter, in orders and in rupees?
    Predict first: a) yes; b) in orders, not in rupees; c) no, one quarter is short by an order; d) no,
    both quarters are short by several. Then type these lines into the empty cell below and run it:

    ```python
    SEGS = ("Retail-Core", "Retail-Plus", "Student", "Business")
    amt = lambda r: read_value(r["amount"])
    kit.table(["quarter", "named segments, orders", "Finance's orders", "named segments, rupees", "Finance's rupees"],
              [(q, sum(1 for r in once if r["quarter"] == q and r["segment"] in SEGS), ctl(q)[1],
                kit.rupees(sum(amt(r) for r in once if r["quarter"] == q and r["segment"] in SEGS)),
                kit.rupees(ctl(q)[0])) for q in QUARTERS], caption="Segments summed against the quarter")
    ```
    """),
    empty(),
    md("""
    **Your turn, if a quarter falls short.** Find the unnamed row, restore it from its customer's other
    orders when they all carry one segment, and read that segment both ways:

    ```python
    blank = [r for r in once if not r["segment"]]
    for r in blank:
        others = {o["segment"] for o in once if o["customer_id"] == r["customer_id"] and o["segment"]}
        print(r["order_id"], r["quarter"], "customer's other segments:", others)
        if len(others) == 1:
            seg = next(iter(others))
            q1 = sum(amt(o) for o in once if o["quarter"] == "Q1" and o["segment"] == seg)
            q2 = sum(amt(o) for o in once if o["quarter"] == "Q2" and o["segment"] == seg)
            extra = amt(r)
            b1, b2 = (q1 + extra, q2) if r["quarter"] == "Q1" else (q1, q2 + extra)
            print(f"{seg}: {change(q1, q2):+.1f}% on named rows, {change(b1, b2):+.1f}% with the order restored")
    ```
    """),
    empty(),
    md("""
    **Why it is wrong, and the fix.** Nobody decided to drop the order; the filter did. The check is one
    line, that the segments add back to the quarter in orders and in rupees, and it fails by exactly the
    rows the filter never saw. The fix is a logged decision: restore the segment from the customer's other
    orders when all of them carry one segment, flag it, and name it in the caveat; keep it as "segment
    unknown" when they do not, with the segment sums reconciled to the quarter.

    ## A second route: account for every value

    The rupee check found the gap from the outside. The second route finds it from the inside, and it
    should land on the same number: every value present in the file is either summed as it came, or
    appears in the log with the number it was read as. Present equals convertible plus logged, and the
    logged values add up to the gap. The rupee check uses Finance's total and this uses only the file,
    so each can fail where the other passes.
    """),
    code('''
present = sum(1 for r in once if r["amount"] != "")
convertible = sum(1 for r in once if r["amount"].isdigit())
logged = [read_value(r["amount"]) for r in once if not r["amount"].isdigit()]
rupee_gap = sum(ctl(q)[0] - sum(zeroed[q]) for q in QUARTERS)
kit.equation(["values present", "=", "convertible", "+", "in the log"],
             title="The second route: every value is summed as it came or logged with the number it was read as")
kit.check("present equals convertible plus logged", present == convertible + len(logged))
kit.check("the logged values add up to the gap the rupee check found", sum(logged) == rupee_gap)
'''),
    md("""
    **When to switch routes.** The rupee check needs a control total and tells you how much is missing;
    the value accounting needs nothing outside the file and tells you where. On a file with no control
    total, the value accounting is the check you still have.

    > **Kavya's review.** A count check proves the rows are there. Only a rupee check proves the values
    > survived. Setting a value to zero claims the order was worth nothing, so that decision belongs in
    > the log with a reason.

    ### In the interview

    **[S] Your cleaning pass reports zero rejects. What do you check?** "I distrust the zero before I
    trust it. First, rows against distinct ids, because a repeated batch is the commonest reason a total
    runs high. Second, how my code handled a value that would not convert: if a `try` set it to zero,
    the rejects count is hiding it. Third, the rupees per period against a control total, with a bridge
    from my number to theirs. On a lab export a zeroing pass reconciled every count and still left the
    base quarter short by the one value it could not read, which halved the fall the note reported."

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

    Any step that can lose something silently: a date parse that sends a bad date to a default, a
    currency converter that returns zero for a code it does not know, a filter on a name that is
    sometimes blank. The pattern is always the same check: what went in equals what came out plus what
    was set aside, in rows and in value.
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

    **Who else faces this.** IMDb will not rank a film in its Top 250 until it has at least 25,000 ratings
    from regular voters, and its weighted rating pulls a title with few votes toward the average of all
    titles (IMDb Help, ratings FAQ, updated 9 February 2026): a 9.4 on a few hundred votes is not
    allowed to beat a 9.0 on a million. A public case shows the cost of ignoring it: Howard Wainer's
    "The Most Dangerous Equation" shows small schools over-represented among both the best and the
    worst performers, because small samples vary more, after the Gates Foundation had put about $1.7
    billion into education grants by 2001, with small schools central to them (Wainer, Picturing the
    Uncertain World, Princeton University Press, 2009, chapter 1).

    **Where this starts.** Chapters 1 and 2 put both quarters on the books to the rupee and showed how a
    segment filter can drop a row. This chapter reads the clean tree, sizes four ways to choose the lead
    and runs every one of them, and tests the lead on each customer's own two quarters.
    """ + HONESTY),
    code(LOAD + '''

amt = lambda r: read_value(r["amount"])
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
    code(MAP.format(lit=2, step=3)),
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
CONSUMER = SEGS[:3]


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
            kit.rupees(T['Q2', s]['rev'] - T['Q1', s]['rev'])) for s in CONSUMER],
          caption="The clean tree for the three consumer segments, Q1 against Q2")
fall = ctl("Q1")[0] - ctl("Q2")[0]
biz = T["Q1", "Business"]["rev"] - T["Q2", "Business"]["rev"]
kit.stats([(f"{change(T['Q1', 'Business']['rev'], T['Q2', 'Business']['rev']):+.1f}%", "the corporate book",
            "revenue, Q1 to Q2"),
           (kit.rupees(biz), "the fall it carries", f"{100 * biz / fall:.1f}% of the quarter's fall")])
kit.bars([(s, abs(T['Q2', s]['rev'] - T['Q1', s]['rev'])) for s in SEGS], lit=(3,), fmt=lambda v: kit.rupees(v),
         title="Rupees moved per segment, Q1 to Q2, either direction")
kit.check("the segments add back to the quarter", all(sum(T[q, s]["rev"] for s in SEGS) == ctl(q)[0] for q in QUARTERS))
'''),
    md("""
    **What happened.** The answer is c. Business carries Rs 17,10,000 of the Rs 17,22,520 fall, which is
    99.3 percent of it, and its revenue fell 29.2 percent. The table leaves the corporate book's counts
    out on purpose: you count them yourself below.

    ## 2. The trap: the headline on too few orders

    **The plausible wrong answer.** "The corporate book fell 29.2 percent from Q1 to Q2 and drove the
    whole decline; we recommend a corporate retention plan." It is true to the rupee, it is the biggest
    number on the page, and it is the headline many notes led with.

    **Predict before you run.** How many orders does that 29.2 percent rest on?

    - a) About 200, the whole file.
    - b) About 90, the corporate share of orders.
    - c) Fewer than thirty.
    - d) It cannot be counted from the export.
    """),
    code('''
b1, b2 = T["Q1", "Business"], T["Q2", "Business"]
n = b1["orders"] + b2["orders"]
kit.check("the corporate rate rests on fewer than thirty orders", n < 30)
kit.check("the corporate book carries more than nine tenths of the fall", biz / fall > 0.9)
'''),
    md("""
    **What happened.** The answer is c. A corporate order here is worth several lakh, so a change of two
    or three orders moves the book by a quarter or more.

    **Why it is wrong.** The rupees are real and Meera should hear them. What a handful of orders cannot
    carry is the word "trend", or a plan built on it. The check is to count before you rate: put the order
    count beside every rate before deciding which one leads, and ask how often chance alone moves that
    many orders as unevenly between the quarters. The mechanism first, on the debrief deck's invented
    export, whose corporate book fell from five orders to two: if each of the seven orders were equally
    likely to land in either quarter, how often would the split come out at least that uneven?
    """),
    code('''
# Invented counts: the debrief deck's invented export, labelled invented wherever they appear.
inv_n, inv_gap = 7, 3            # seven corporate orders, split five and two
closer = sum(comb(inv_n, k) for k in range(inv_n + 1) if abs(2 * k - inv_n) < inv_gap) / 2 ** inv_n
kit.columns(["closer than 5 and 2", "at least as uneven as 5 and 2"],
            [("share of coin-flip worlds, invented", [closer, 1 - closer])],
            fmt=lambda v: f"{v:.3f}", lit=(1,), width=560,
            title=f"Invented: seven orders split by coin flips, at least as unevenly as five and two in {1 - closer:.0%} of worlds")
'''),
    md("""
    **Your turn.** Count this file's corporate orders in each quarter and run the same coin flips on
    them. Type these lines into the empty cell below and run it:

    ```python
    print("corporate orders:", b1["orders"], "in Q1 and", b2["orders"], "in Q2")
    gap = abs(b1["orders"] - b2["orders"])
    share = sum(comb(n, k) for k in range(n + 1) if abs(2 * k - n) >= gap) / 2 ** n
    print(f"coin flips split {n} orders at least that unevenly in {share:.1%} of worlds")
    ```

    Then write the corporate line of your note as counts: the orders in each quarter, then the rupees.
    """),
    empty(),
    md("""
    **The fix, and what it changes.** The corporate fall goes into the note as counts, the orders in each
    quarter from your turn above, beside the Rs 17,10,000 it carries. Its action is a question to
    whoever owns those accounts about why fewer corporate orders came in, which costs a phone call. The
    lead moves to the branch that moved on enough orders to read.

    ## The options

    How does a team choose which finding leads? Four ways, each sized below on the clean tree: the claim
    it leads with, the orders behind that claim, how often chance alone produces it, and the analyst
    minutes it costs at the lab brief's pace. Option D is run, not described: one test per segment, each
    on that segment's own customers' two quarters.

    | Option | How it picks the lead |
    |---|---|
    | A. The biggest rupee move | Whatever moved most in rupees leads |
    | B. The total, unsplit | The quarter's change leads and the split is left out |
    | C. Count before rate | Every rate carries its order count; a rate on fewer than about thirty orders goes to the caveat as counts, and the lead is the branch that moved on enough orders and survives one test |
    | D. Test everything | A test on every segment, and the smallest p-value leads |
    """),
    code('''
def members_of(seg):
    """Each customer of a segment with their own Q1 and Q2 orders, in customer order."""
    per = {}
    for r in clean:
        if r["segment"] == seg:
            per.setdefault(r["customer_id"], {"Q1": [], "Q2": []})[r["quarter"]].append(r["amount"])
    return dict(sorted(per.items()))


def flipped_change(per, swaps, basket=True):
    """The segment's change from Q1 to Q2 with the swapped customers' two quarters exchanged."""
    q1r = q1n = q2r = q2n = 0
    for v, s in zip(per.values(), swaps):
        a, b = (v["Q2"], v["Q1"]) if s else (v["Q1"], v["Q2"])
        q1r, q1n, q2r, q2n = q1r + sum(a), q1n + len(a), q2r + sum(b), q2n + len(b)
    return change(q1r / q1n, q2r / q2n) if basket else change(q1r, q2r)


def paired_test(seg, basket=True, flips=2000, seed=7):
    """Flip each customer's two quarters at random; the share of worlds as extreme, either way."""
    per = members_of(seg)
    observed = flipped_change(per, [False] * len(per), basket)
    rng = random.Random(seed)
    worlds = [flipped_change(per, [rng.random() < 0.5 for _ in per], basket) for _ in range(flips)]
    return observed, worlds, sum(1 for w in worlds if abs(w) >= abs(observed) - 1e-9) / flips


core = [r for r in clean if r["segment"] == "Retail-Core"]
obs_core, worlds_core, p_core = paired_test("Retail-Core")
four = [(s, *paired_test(s, basket=False)[::2]) for s in SEGS]
false_alarm = 1 - 0.95 ** 4
lead_d = min(four, key=lambda f: f[2])
split_share = sum(comb(n, k) for k in range(n + 1) if abs(2 * k - n) >= abs(b1["orders"] - b2["orders"])) / 2 ** n
kit.table(["option", "leads with", "orders behind it", "chance alone", "analyst minutes"], [
    ("A. biggest rupee move", f"Business {change(b1['rev'], b2['rev']):+.1f}%", "fewer than thirty",
     "more than half of coin-flip worlds" if split_share > 0.5 else "under half of coin-flip worlds", 5),
    ("B. the total, unsplit", f"revenue {change(ctl('Q1')[0], ctl('Q2')[0]):+.1f}%", ctl("Q1")[1] + ctl("Q2")[1],
     "not asked", 2),
    ("C. count before rate", f"Retail-Core revenue per order {obs_core:+.1f}%, "
     f"{kit.rupees(T['Q1', 'Retail-Core']['rev'] - T['Q2', 'Retail-Core']['rev'])}", len(core),
     f"{p_core:.3f}, each customer's quarters flipped", 15),
    ("D. test every segment", f"{lead_d[0]}, the smallest of four p-values", f"fewer than thirty to {len(core)}",
     f"{lead_d[2]:.3f}, with a {false_alarm:.2f} chance that one of four looks real by luck", 45),
], caption="Four ways to choose the lead, sized on the clean tree")
kit.table(["segment", "revenue change", "p, each customer's quarters flipped, 2,000 times"],
          [(s, f"{o:+.1f}%", f"{p:.3f}") for s, o, p in four], caption="Option D, run: one test per segment")
kit.matrix(["enough orders", "too few orders"], ["moved in rupees", "moved in rate only"],
           [["lead with it, tested", "lead only if it survives a test"],
            ["say it as counts, ask the owner", "leave it out of the claim"]],
           title="Where each finding goes in the note")
'''),
    code('''
kit.check("Retail-Core's basket rests on more than thirty orders", len(core) > 30, f"{len(core)} orders")
kit.check("Retail-Core's fall is one chance rarely produces on its customers' own quarters", p_core < 0.05,
          f"p = {p_core:.3f}")
kit.check("testing every segment turns up no second finding under 0.05", sum(1 for f in four if f[2] < 0.05) == 1)
'''),
    md("""
    **The best-fit call.** C. It costs about fifteen minutes and one test, and it leads with a finding
    that rests on 88 orders and that came up as large, in either direction, in only 12 of 2,000 worlds
    where each Retail-Core customer's two quarters were swapped at random. It is small in rupees, Rs
    15,400 of the fall, about 0.9 percent of it, so it leads among consumers as the one move on enough
    orders to test, while the corporate Rs 17,10,000 sits beside it in the claim as counts. A leads on
    too few orders to call a trend. B hides the one thing Meera most needs, that 99 percent of the fall
    is the corporate book. D, run here, finds the same lead at three times the minutes, and it spent four
    tests to do it: with four tests at 0.05 the chance that at least one looks real by luck is about 19
    percent, so on another file D leads with a fluke about one time in five.

    **What would change the call.** A question about accounts rather than rates: if Meera asked "what
    happened to our corporate revenue?", the lead is the corporate fall, said as counts, with the
    accounts named by their owner. A corporate book of hundreds of orders a quarter would let its rate
    lead. And a second quarter of the same move in Business would turn a phone call into a trend worth
    testing.

    ## 3. The branch that moved, tested on each customer's own two quarters

    Retail-Core keeps its 30 customers and orders about 1.47 times each in both quarters, while its
    revenue per order falls 17.1 percent. The claim is about the same 30 customers in both quarters, so
    the fair test keeps each customer's own two quarters together. In a world where the quarter made no
    difference, each customer's Q1 and Q2 are as likely either way round, so the test swaps them at
    random for each customer, recomputes Retail-Core's revenue per order, and counts the worlds with a
    change at least as large. The fall was found by looking at the tree, so a rise of that size counts
    as well: the note reports both directions.

    **Predict before you run.** Where does the real change sit among 2,000 worlds with each customer's
    quarters flipped at random?

    - a) In the middle of the pile.
    - b) At the edge: about a dozen worlds are as extreme.
    - c) Beyond every flipped world.
    - d) The test cannot run, since some customers ordered twice in a quarter.
    """),
    code('''
one_way = sum(1 for w in worlds_core if w <= obs_core + 1e-9) / 2000
print(f"Retail-Core revenue per order {obs_core:+.1f}%; {round(p_core * 2000)} of 2,000 flipped worlds as large "
      f"either way, p = {p_core:.4f}; counted one way, {one_way:.4f}")
kit.strip(worlds_core, markers=[("observed", obs_core, "bad"), ("its mirror", -obs_core, "plain")], lo=-24, hi=24,
          fmt=lambda v: f"{v:+.0f}%",
          title="2,000 worlds with each customer's two quarters flipped, against Retail-Core's real change")
kit.check("Retail-Core's customers and frequency hold while its basket falls",
          T["Q1", "Retail-Core"]["customers"] == T["Q2", "Retail-Core"]["customers"]
          and abs(T["Q1", "Retail-Core"]["freq"] - T["Q2", "Retail-Core"]["freq"]) < 0.01)
'''),
    md("""
    **What happened.** The answer is b. Only 12 of 2,000 flipped worlds show a change as large as
    Retail-Core's, in either direction: p = 0.006, a share of chance-only worlds, never the chance the
    finding is wrong. Counted one way, a fall at least as large, it is 0.001, the number a note would
    quote only if the fall had been predicted before the data was seen; it was found in the tree, so the
    note reports both directions. The share wobbles at 2,000 flips, and at 20,000 it settles near 0.004.

    **A different question, a different test.** "Did Retail-Core's basket move differently from
    Retail-Plus's?" compares two groups of different customers. There the fair test shuffles the segment
    label across whole customers, each carrying all their orders with them, and asks how often a gap as
    large as the real one turns up.
    """),
    code('''
plus = [r for r in clean if r["segment"] == "Retail-Plus"]


def basket_change(rs):
    a = [r["amount"] for r in rs if r["quarter"] == "Q1"]
    b = [r["amount"] for r in rs if r["quarter"] == "Q2"]
    return change(sum(a) / len(a), sum(b) / len(b))


gap = basket_change(core) - basket_change(plus)
groups = {}
for r in core + plus:
    groups.setdefault(r["customer_id"], []).append(r)
ids = sorted(groups)
n_core = len({r["customer_id"] for r in core})
rng = random.Random(7)
between = []
for _ in range(2000):
    m = ids[:]
    rng.shuffle(m)
    between.append(basket_change([r for c in m[:n_core] for r in groups[c]])
                   - basket_change([r for c in m[n_core:] for r in groups[c]]))
p_between = sum(1 for g in between if abs(g) >= abs(gap)) / 2000
kit.table(["the question", "the fair test", "p, both directions"], [
    ("did Retail-Core's revenue per order fall?", "each customer's two quarters flipped", f"{p_core:.4f}"),
    ("did it move differently from Retail-Plus's?", "segment label shuffled across whole customers", f"{p_between:.4f}")],
    caption=f"Two questions about one finding; the gap to Retail-Plus is {gap:+.1f} points")
kit.check("both fair tests put the finding outside what chance usually does", p_core < 0.05 and p_between < 0.05)
'''),
    md("""
    **The note, with the right lead.** Claim: booked revenue fell 28.5 percent, Rs 60,48,000 to Rs
    43,25,480; Rs 17,10,000 of it is the corporate book, and among consumers the branch that moved is
    Retail-Core's revenue per order, down 17.1 percent with its 30 customers and their frequency
    unchanged. Evidence: both quarters reconcile to Finance's control totals; with each Retail-Core
    customer's two quarters flipped at random, a change this large in either direction came up in 12 of
    2,000 worlds, p = 0.006. Caveat: the corporate move rests on too few orders to call a trend, and the
    note gives its count in each quarter. Action: ask the corporate account owner why fewer corporate
    orders came in, and open Retail-Core's basket (items per order and price per item) before any spend.

    ## A second route: customer by customer

    The flips compare the segment's average. A second route reads each customer on their own: of
    Retail-Core's customers who ordered in both quarters, how many saw their own average order fall? If
    the fall is real and broad, most of them should, and a sign test says how often coin flips alone
    would split the customers at least that unevenly.
    """),
    code('''
per = members_of("Retail-Core")
fell = sum(1 for v in per.values() if sum(v["Q2"]) / len(v["Q2"]) < sum(v["Q1"]) / len(v["Q1"]))
rose = sum(1 for v in per.values() if sum(v["Q2"]) / len(v["Q2"]) > sum(v["Q1"]) / len(v["Q1"]))
moved = fell + rose
sign_p = 2 * sum(comb(moved, k) for k in range(min(fell, rose) + 1)) / 2 ** moved
kit.columns(["own basket fell", "own basket rose", "unchanged"], [("customers", [fell, rose, len(per) - moved])],
            lit=(0,), width=560,
            title=f"Retail-Core's {len(per)} customers: {fell} fell and {rose} rose; sign test p = {sign_p:.3f} either way")
kit.check("most customers who ordered in both quarters saw their own basket fall", fell > len(per) / 2,
          f"{fell} of {len(per)}")
kit.check("the sign test puts the split outside what coin flips usually do", sign_p < 0.05, f"p = {sign_p:.3f}")
kit.check("the second route points the same way as the flips", (fell > rose) == (obs_core < 0))
'''),
    md("""
    **When to switch routes.** The flips say whether the segment's change is bigger than chance; the
    customer count says whether it is broad or carried by a few people. When the two disagree, a handful
    of customers moved the average, and the note says so. The sign test uses only the direction of each
    customer's change, never its size, which is why its p of 0.043 sits above the flips' 0.006.

    > **Kavya's review.** Say the count before the rate, every time: the orders in each quarter, then
    > the percentage. "Down 29 percent" alone is a headline, and Marketing will take it apart with one
    > question.

    ### In the interview

    **[S] Tell me about an analysis you did: what did you find, and how sure are you?** "On a two-quarter
    export, revenue fell 28.5 percent after I reconciled it to Finance's control totals. Almost all of it
    was the corporate book, on too few orders to call a trend, which I reported as counts and passed to
    the account owner. The finding I led with was Retail-Core's revenue per order, down 17.1 percent on
    88 orders with customers and frequency flat. The same 30 customers were in both quarters, so I tested
    it by flipping each customer's two quarters at random: p = 0.006 counting either direction, and 21 of
    the 30 saw their own basket fall. My caveat was the corporate book's count."

    **[D] A stakeholder attacks your caveat in front of the room.** "I restate the claim with its count,
    bound what the data can say, and offer the test that would settle it with its size and time. For the
    corporate book: a handful of orders cannot tell a trend from an account or two pausing; a call to the
    account owner settles which it is by Monday."

    **The design question: four segments moved; which do you test?** "One: the branch the tree says moved
    on enough orders to read, tested on its own customers' two quarters. Testing all four at 0.05 gives
    about a one-in-five chance that something looks real by luck, and a test on a handful of orders cannot
    say anything a count does not."

    ### Depth: the tests that break the pairing, and the typical order

    Two tests a hurried analyst reaches for split what belongs together. Pooling the customers' Q1 and
    Q2 figures and dealing the quarter labels at random treats a customer's own two quarters as two
    strangers; shuffling segment labels across single orders splits one customer's orders between the
    groups. Either can move p either way. On this file both come out larger than the fair test's,
    because each customer's own change from Q1 to Q2 is steadier than the spread between customers, and
    a test that splits the pair throws that steadiness away. On a file where the question compares
    groups and a customer's orders are alike, splitting them most often makes p too small instead,
    because correlated orders count as extra evidence. The cell below runs each fair test beside its
    hurried twin, on the same measure.
    """),
    code('''
r1 = [sum(v["Q1"]) for v in per.values()]
r2 = [sum(v["Q2"]) for v in per.values()]
real = sum(r1) / len(r1) - sum(r2) / len(r2)
rng = random.Random(7)
pool, dealt = r1 + r2, []
for _ in range(2000):
    rng.shuffle(pool)
    dealt.append(sum(pool[:len(r1)]) / len(r1) - sum(pool[len(r1):]) / len(r2))
p_pooled = sum(1 for g in dealt if abs(g) >= abs(real) - 1e-9) / 2000
p_pooled_one = sum(1 for g in dealt if g >= real - 1e-9) / 2000
rng = random.Random(7)
d = [b - a for a, b in zip(r1, r2)]
p_flip_rev = sum(1 for _ in range(2000)
                 if abs(sum(x if rng.random() < 0.5 else -x for x in d)) >= abs(sum(d)) - 1e-9) / 2000
both_rows = core + plus
rng = random.Random(7)
ext = 0
for _ in range(2000):
    idx = list(range(len(both_rows)))
    rng.shuffle(idx)
    a = [both_rows[i] for i in idx[:len(core)]]
    b = [both_rows[i] for i in idx[len(core):]]
    ext += abs(basket_change(a) - basket_change(b)) >= abs(gap)
p_orders = ext / 2000
amounts = sorted(r["amount"] for r in clean)
kit.table(["measure", "the test", "what it keeps together", "p, both directions"], [
    ("revenue per customer, Q1 to Q2", "each customer's two quarters flipped", "each customer's own pair",
     f"{p_flip_rev:.4f}"),
    ("revenue per customer, Q1 to Q2", "Q1 and Q2 figures pooled and dealt", "nothing",
     f"{p_pooled:.4f} ({p_pooled_one:.4f} one way)"),
    ("revenue per order, gap to Retail-Plus", "segment label across whole customers", "each customer's orders",
     f"{p_between:.4f}"),
    ("revenue per order, gap to Retail-Plus", "segment label across single orders", "nothing", f"{p_orders:.4f}")],
    caption="Each fair test beside the hurried twin that splits the pair")
kit.table(["measure", "value"], [("mean order, clean", kit.rupees(statistics.mean(amounts))),
                                 ("median order, clean", kit.rupees(statistics.median(amounts)))],
          caption="The typical order")
kit.check("splitting the pairs pushes both verdicts past 0.05 on this file",
          p_pooled > 0.05 > p_flip_rev and p_orders > 0.05 > p_between)
'''),
    md("""
    The mean order is pulled up by the corporate orders, so it describes no order anybody placed; the
    median is the typical one, and the mean belongs in anything that must reconcile.
    """),
    code("kit.check_summary()"),
]

CHAPTERS = [
    ("C2_W01_D05_01_debrief_quarters_STUDENT.ipynb", CH1),
    ("C2_W01_D05_02_debrief_values_STUDENT.ipynb", CH2),
    ("C2_W01_D05_03_debrief_segments_STUDENT.ipynb", CH3),
]

if __name__ == "__main__":
    for name, cells in CHAPTERS:
        build(NB / name, cells)
        print("built", name, len(cells), "cells")

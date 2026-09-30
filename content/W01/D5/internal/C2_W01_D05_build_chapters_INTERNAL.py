"""Build the lab debrief's three chapter notebooks, one per place most rooms break.

    python3 content/W01/D5/internal/C2_W01_D05_build_chapters_INTERNAL.py

Each notebook pairs with one chapter of slides/C2_W01_D05_debrief_STUDENT.md by number and question,
and runs cold in notebooks/ on the invented export that
internal/C2_W01_D05_invented_export_INTERNAL.py writes to data/, labelled invented wherever its
numbers appear. No saved output and no markdown line carries a number computed from the lab export
(v3-lab, proposed for client zero v2.3 and not yet locked): after each step, the markdown gives the
lines that run the same step on the lab file and the cell below it ships empty, so the lab's numbers
appear only on the screen of a learner who types them after the lab. The file names describe what
each chapter examines, so a folder listing during the lab names no trap.
"""
import pathlib
import sys
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, md, code, empty, build  # noqa: E402

DAY = ROOT / "content" / "W01" / "D5"
NB = DAY / "notebooks"


def mdj(*parts):
    """One markdown cell from several pieces, each dedented on its own before they are joined."""
    return md("\n\n".join(textwrap.dedent(p).strip("\n") for p in parts))


# The shared opening: the invented export and its control totals, and the loader that fetches this
# morning's file only when a your-turn cell asks for it.
LOAD = SETUP + '''
import random
import statistics
from math import comb

QUARTERS = ("Q1", "Q2")
SEGS = ("Retail-Core", "Retail-Plus", "Student", "Business")


def load_export(which):
    """An export and Finance's control totals for it: "invented" for this debrief, "lab" for this morning's file."""
    orders = kit.load_csv(f"C2_W01_D05_{which}_orders_STUDENT.csv")
    book = {c["quarter"]: c for c in kit.load_csv(f"C2_W01_D05_{which}_control_STUDENT.csv")}
    return orders, book


def change(a, b):
    """Percentage change from a to b."""
    return 100 * (b / a - 1)


def ctl(q, book=None):
    """Finance's rupees and orders for a quarter, from the invented export's book unless another is given."""
    book = book or control
    return int(book[q]["amount_rs"]), int(book[q]["orders"])


def read_value(text):
    """The number an amount stored as text holds, read the way a person reads it in the forms this
    week's exports used; None when reading it would take a guess."""
    t = str(text).strip().replace("Rs", "").replace(",", "").replace(" ", "")
    try:
        return round(float(t))
    except ValueError:
        return None


rows, control = load_export("invented")
print(f"The invented export: {len(rows)} rows over two quarters, with Finance's control totals for "
      f"{' and '.join(sorted(control))}. Every number it gives is invented.")
'''

HONESTY = """
**Before you read on.** This notebook runs on an invented export built for the debrief: 175 rows
over two quarters, with Finance's control totals beside it. Its numbers are labelled invented
wherever they appear, and none of them is Kalpa's or this morning's. After each step, the lines under
**Your turn** run the same step on this morning's lab export: once the lab is over, type them into the
empty cell below them and run the cells in order.
"""


def map_cell(lit, step):
    return code(f'''
kit.side_by_side(
    kit.ladder(["Do the quarters tie?", "Is a clean pass done?", "Which number leads?"], lit={lit}, show=False),
    kit.flow(["profile", "clean, with a log", "reconcile", "decompose", "test", "note"], lit={step}, show=False),
)
''')


# --------------------------------------------------------------------------------- chapter 1
CH1 = [
    mdj("""
    # 1. Do the two quarters in your note match Finance's books?

    **Week 1, Friday. The lab debrief, chapter 1 of 3.** This morning each of you took a raw
    two-quarter export to a four-part note, alone, in two hours. This chapter replays the step most
    rooms dropped when the clock ran: the check that the data you analysed is still the data Finance
    booked.

    **Who needs the answer.** Anand Iyer, Kalpa Retail's finance controller, checks the note's first
    line against his control totals before any number reaches Meera Raghavan, the CEO, at Monday's
    growth review. A first line that points the wrong way sends the review after the wrong question,
    and Marketing's Rs 12 crore request to win new customers gets judged against a quarter that did not
    happen. Anand returns the note, and the team's next number is read with suspicion.

    **The questions on the way.**

    1. What headline does a pass that skips the reconciliation send?
    2. Which check should run before the number is sent, and what does each one cost?
    3. What does the count check fix, and what does it leave behind?
    4. Which two moves walk the hurried sum to Finance's total?
    5. Does a sum of the decisions themselves land on the bridge's two moves?

    **The metric at stake.** Booked revenue per quarter, the rupees of the orders recorded as sales
    in that quarter, and its change from Q1 to Q2, which the note leads with. A control total is the
    source system's own count of orders and sum of rupees for a period; a clean pass must land on it.

    **Who else faces this.** Nykaa, the beauty and fashion retailer, reports two numbers for the same
    quarter: gross merchandise value (GMV), the value of everything customers ordered at the prices
    charged, before cancellations, returns and tax come out, and revenue from operations, the income the
    company books in its own accounts. For April to June 2025 they were Rs 4,182 crore and Rs 2,155
    crore (FSN E-Commerce Ventures press release, 12 August 2025), so an analyst there who quotes one
    to the owner of the other is out by nearly half, and every internal figure says which it is and
    bridges to the books. A public case shows what an unreconciled pipeline hides: in October 2020
    Public Health England said 15,841 positive COVID-19 cases from 25 September to 2 October had been
    left out of the reported daily figures because files exceeded a size limit (UK government
    statement, 4 October 2020). No step raised an error, and the rows were simply missing.
    """, HONESTY),
    code(LOAD),
    map_cell(0, 2),
    mdj("""
    **Two passes, as small functions.** `quarter_totals` sums each quarter of an export, either
    reading every value with `read_value` from the first cell or setting any value that will not
    convert to zero, the way a hurried pass does; `first_of_each` keeps one row per order id,
    Wednesday's identity rule. Both take the export as an argument, so the your-turn cells can hand
    them this morning's file.
    """),
    code('''
def quarter_totals(src, text_to_zero):
    """Each quarter's rupees and rows, with unreadable values set to zero or read."""
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
    """One row per order id, the first to arrive."""
    kept = {}
    for r in src:
        kept.setdefault(r["order_id"], r)
    return list(kept.values())


truth = change(ctl("Q1")[0], ctl("Q2")[0])
print(f"Invented: Finance's books say Q1 to Q2 {truth:+.1f}%, "
      f"from {kit.rupees(ctl('Q1')[0])} to {kit.rupees(ctl('Q2')[0])}")
'''),
    mdj("""
    ## 1. What headline does a pass that skips the reconciliation send?

    A hurried pass keeps the rows as they arrived and sets to zero any value that will not convert. It
    runs to the end without an error, so nothing on the screen says to stop.

    **Predict before you run.** On the invented export, what Q1 to Q2 change does that pass report?

    - a) A fall of about a third, the same as Finance's books.
    - b) A rise of about a fifth.
    - c) A fall of about a sixth.
    - d) No change, since both quarters hold about eighty orders.
    """),
    code('''
hurried = quarter_totals(rows, text_to_zero=True)
h_change = change(hurried["Q1"][0], hurried["Q2"][0])
kit.stats([(f"{h_change:+.1f}%", "Q1 to Q2, the hurried run", "invented"),
           (f"{truth:+.1f}%", "Q1 to Q2, Finance's books", "invented, from the control file"),
           ("0", "errors raised", "the pass ran to the end")])
kit.bars([("the hurried run: a rise", round(abs(h_change), 1)), ("Finance's books: a fall", round(abs(truth), 1))],
         fmt=lambda v: f"{v:.1f}%", lit=(1,), width=640,
         title="Invented: one export, two first lines that point opposite ways (the size of each change)")
'''),
    code('''
kit.check("the hurried run misses Finance's rupee totals", any(hurried[q][0] != ctl(q)[0] for q in QUARTERS))
kit.check("the hurried run points the opposite way to the books", h_change > 0 > truth,
          f"{h_change:+.1f}% against {truth:+.1f}%")
'''),
    mdj("""
    **What happened.** The answer is b. On the invented export the hurried pass reports Q2 up 21.2
    percent, from Rs 31,50,000 on 83 rows to Rs 38,16,420 on 92 rows, and Finance's control file says
    the quarter fell 35.0 percent.

    **The plausible wrong answer.** "Q2 grew 21.2 percent; the top line needs no action." The
    arithmetic is right, the file is Finance's own export, and nothing on the screen looks broken.

    **Why it is wrong.** Nobody asked whether the data summed is the data Finance booked. Sent to
    Meera, the line tells her that a quarter which fell was a good one, and the review spends its time
    on Marketing's plans while the fall goes unexplained. The check that catches it is one comparison
    with the control file, in orders and in rupees.

    **Your turn, on this morning's file.** Load the lab export and its control totals, run the same
    hurried pass on it, and put it beside Finance's totals. Type these lines into the empty cell below
    and run it:

    ```python
    lab, lab_book = load_export("lab")
    lab_hurried = quarter_totals(lab, text_to_zero=True)
    kit.table(["quarter", "rows summed", "Finance's orders", "rupees summed", "Finance's rupees"],
              [(q, lab_hurried[q][1], ctl(q, lab_book)[1], kit.rupees(lab_hurried[q][0]),
                kit.rupees(ctl(q, lab_book)[0])) for q in QUARTERS],
              caption="This morning's hurried run against Finance's control totals")
    print(f"hurried headline {change(lab_hurried['Q1'][0], lab_hurried['Q2'][0]):+.1f}%, "
          f"the books {change(ctl('Q1', lab_book)[0], ctl('Q2', lab_book)[0]):+.1f}%")
    ```

    Does this morning's hurried headline point the same way as the books, and where does each quarter
    miss them, if it does?
    """),
    empty(),
    mdj("""
    ## 2. Which check should run before the number is sent, and what does each one cost?

    The question at this step is narrow: before any branch of the tree is read, is the data you
    cleaned still the data Finance booked? A team has four ways to answer it.

    | Option | What it does | What it needs from outside the file |
    |---|---|---|
    | A. Trust the pass | Sum what the cleaning pass kept and move on to the tree | Nothing |
    | B. Count check | Rows read equal rows kept plus rows rejected, and orders per quarter equal Finance's order counts | Finance's order counts |
    | C. Counts and rupees, with a bridge | B, plus each quarter's rupees against Finance's control total, and a bridge from what was read to what was kept | Finance's rupee totals too |
    | D. Order-level match | Every kept order matched to Finance's ledger, line by line | The ledger itself, which no export here carries |

    The cell below sizes the options on what separates them: the analyst's minutes and cells, what
    each can see, and how far the headline it lets through sits from the books. The computer's share
    of every option is under a millisecond, so the minutes are an analyst's at the lab brief's pace,
    and D's is this programme's estimate for a request to Finance and a join. D cannot run on an
    export that came without a ledger, so its row says what it would need and find and claims no
    headline.
    """),
    code('''
SIZING_HEADERS = ["option", "analyst minutes", "cells", "what it needs", "what it can see",
                  "Q1 to Q2 it lets through", "points off the books"]


def size_options(src, book):
    """Run the hurried pass, apply each check, and fix only what that check can see."""
    books = change(ctl("Q1", book)[0], ctl("Q2", book)[0])
    out = []
    for name, minutes, cells, needs, sees, dedupe, read in [
            ("A. trust the pass", 0, 0, "nothing", "nothing", False, False),
            ("B. count check", 2, 1, "Finance's order counts", "rows beyond Finance's orders", True, False),
            ("C. counts and rupees, bridge", 15, 3, "Finance's rupee totals too",
             "extra rows, and rupees the kept rows lost", True, True)]:
        t = quarter_totals(first_of_each(src) if dedupe else src, text_to_zero=not read)
        sent = change(t["Q1"][0], t["Q2"][0])
        out.append((name, minutes, cells, needs, sees, f"{sent:+.1f}%", round(abs(sent - books), 1)))
    out.append(("D. order-level match", "about 120", 6, "Finance's ledger", "every order that differs, by id",
                "not run: no ledger", "not run"))
    return out


sizing = size_options(rows, control)
kit.table(SIZING_HEADERS, sizing, caption=f"Invented: four ways to check, sized; the books say {truth:+.1f}%")
kit.bars([(s[0], s[6]) for s in sizing[:3]], lit=(2,), fmt=lambda v: f"{v:.1f} pts",
         title="Invented: how far each option's headline sits from the books, in percentage points")
'''),
    code('''
kit.check("only C, of the options that can run here, lands on the books",
          sizing[2][6] == 0 and all(s[6] > 1 for s in sizing[:2]))
kit.check("the count check moves the headline and still misses the books",
          sizing[1][5] != sizing[0][5] and sizing[1][6] > 1)
'''),
    mdj("""
    **What happened, and the best-fit call.** C. It costs about fifteen of an analyst's 120 minutes,
    needs only the control file that came with the export, and is the one option run here that lands
    on the books to the rupee. A lets the invented export's +21.2 percent through, 56.2 points off. B
    is where most people who did check stopped, and it still leaves the headline 17.5 points off. D
    would name every order that differs, which C cannot, at the cost of a request to Finance and most
    of the afternoon.

    **What would change the call.** No control total at all: C then has nothing to land on, and D, or
    a second export pulled from the source system for the same quarters, becomes the check. A bridge
    that will not close: C has found a gap it cannot explain, and D is how you find which orders make
    it.

    **Your turn, on this morning's file.** Size the same four options on the lab export. Type this
    line into the empty cell below and run it:

    ```python
    kit.table(SIZING_HEADERS, size_options(lab, lab_book), caption="The four checks on this morning's file")
    ```

    Where did your own lab run sit in this table?
    """),
    empty(),
    mdj("""
    ## 3. What does the count check fix, and what does it leave behind?

    Option B keeps one row per order id and compares the orders in each quarter with Finance's order
    counts. The rows it sets aside go to a rejected list, so rows read equal rows kept plus rows
    rejected.

    **Predict before you run.** Once every order count lands on Finance's, what can still be wrong in
    the invented export?

    - a) The rows that repeat an order, which the check has not yet removed.
    - b) A value inside a kept row, which the check cannot see.
    - c) Nothing, since the counts now land on the books.
    - d) The order ids, which the check trusts without reading.
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
kit.table(["quarter", "orders kept", "Finance's orders", "rupees kept", "Finance's rupees"],
          [(q, counted[q][1], ctl(q)[1], kit.rupees(counted[q][0]), kit.rupees(ctl(q)[0])) for q in QUARTERS],
          caption=f"Invented, after the count check: {len(rows)} rows read, {len(once)} kept, {len(rejected)} set aside")
kit.check("input equals kept plus rejected, each list built on its own", len(rows) == len(once) + len(rejected))
kit.check("the order counts now land on Finance's in both quarters", all(counted[q][1] == ctl(q)[1] for q in QUARTERS))
kit.check("the rupees still miss Finance's control totals", any(counted[q][0] != ctl(q)[0] for q in QUARTERS),
          f"Q1 to Q2 after the count check {c_change:+.1f}%")
'''),
    mdj("""
    **What happened.** The answer is b. Every order count lands, and the invented headline moves from
    +21.2 to -17.5 percent: the right direction at half the size. A count check proves the rows are
    there and says nothing about whether each row's value survived the conversion; Q1 still sums to Rs
    31,50,000 against Finance's Rs 40,00,000. That gap is chapter 2's question.

    **Your turn, on this morning's file.** Run the count check on the lab export. Type these lines into
    the empty cell below and run it:

    ```python
    lab_once = first_of_each(lab)
    lab_counted = quarter_totals(lab_once, text_to_zero=True)
    kit.table(["quarter", "orders kept", "Finance's orders", "rupees kept", "Finance's rupees"],
              [(q, lab_counted[q][1], ctl(q, lab_book)[1], kit.rupees(lab_counted[q][0]),
                kit.rupees(ctl(q, lab_book)[0])) for q in QUARTERS],
              caption=f"This morning's file after the count check: {len(lab)} rows read, {len(lab_once)} kept")
    ```

    Do the counts land, and do the rupees?
    """),
    empty(),
    mdj("""
    ## 4. Which two moves walk the hurried sum to Finance's total?

    Option C adds the rupee comparison and draws the walk from what the hurried run summed to what
    Finance booked, one move per decision in the log: the rows Finance does not hold come out, and the
    value that would not convert is read back in.

    **Predict before you run.** On the invented export, which move is the larger?

    - a) The rows Finance does not hold.
    - b) The value that would not convert.
    - c) They are equal.
    - d) Neither; the walk closes with no moves.
    """),
    code('''
def bridge_moves(src):
    """The hurried sum of both quarters, the rupees the count check removed, and the rupees read back."""
    as_read = sum(t for t, _ in quarter_totals(src, text_to_zero=True).values())
    counted_sum = sum(t for t, _ in quarter_totals(first_of_each(src), text_to_zero=True).values())
    clean_sum = sum(t for t, _ in quarter_totals(first_of_each(src), text_to_zero=False).values())
    return as_read, counted_sum - as_read, clean_sum - counted_sum


as_read, extra_rows, text_back = bridge_moves(rows)
kit.bridge(("the hurried sum", as_read), [("rows Finance does not hold", extra_rows), ("a value read back", text_back)],
           end_label="clean, both quarters", lit=[0], lo=5_000_000,
           title="Invented: from the hurried sum to the books (the axis starts at Rs 50 lakh)")
clean = quarter_totals(once, text_to_zero=False)
kit.check("the bridge lands on Finance's two quarters together",
          as_read + extra_rows + text_back == ctl("Q1")[0] + ctl("Q2")[0], kit.rupees(ctl("Q1")[0] + ctl("Q2")[0]))
kit.check("both quarters land, orders and rupees", all(clean[q] == ctl(q) for q in QUARTERS))
'''),
    mdj("""
    **What happened.** The answer is a. On the invented export the rows Finance does not hold carry Rs
    12,16,420 and the value read back carries Rs 8,50,000, and the walk from Rs 69,66,420 lands on Rs
    66,00,000, Finance's two quarters together.

    **The fix, and what it changes.** With both quarters on the books the invented headline is a fall
    of 35.0 percent, from Rs 40,00,000 to Rs 26,00,000. The note changes sign, so the decision changes
    with it: Monday's review now has a fall of Rs 14,00,000 to explain, and chapter 3 finds where it
    sits.

    **Your turn, on this morning's file.** Draw this morning's bridge and read which move is the
    larger there. Type these lines into the empty cell below and run it:

    ```python
    lab_read, lab_extra, lab_back = bridge_moves(lab)
    floor = 0.9 * min(lab_read, lab_read + lab_extra, lab_read + lab_extra + lab_back)
    kit.bridge(("the hurried sum", lab_read), [("rows Finance does not hold", lab_extra),
                                               ("a value read back", lab_back)],
               end_label="clean, both quarters", lit=[0], lo=int(floor // 100_000) * 100_000,
               title="This morning's file: from the hurried sum to the books")
    ```
    """),
    empty(),
    code('''
variants = [("the hurried run", hurried), ("count check only", counted), ("counts and rupees", clean)]
heads = [(n, change(t["Q1"][0], t["Q2"][0])) for n, t in variants]
kit.table(["run", "Q1 to Q2"], [(n, f"{h:+.1f}%") for n, h in heads], caption="Invented: one export, three headlines")
kit.bars([(f"{n}: {'a rise' if h > 0 else 'a fall'}", round(abs(h), 1)) for n, h in heads], lit=(2,),
         fmt=lambda v: f"{v:.1f}%", width=640, title="Invented: the same file, three first lines (the size of each change)")
'''),
    mdj("""
    ## 5. Does a sum of the decisions themselves land on the bridge's two moves?

    The bridge's two moves were found by subtracting one total from another. The second route builds
    the evidence on its own: every row set aside as a repeat of an order already kept, summed from the
    set-aside list, and every value read back from text, summed from the decisions log. Each sum must
    equal its move in the bridge. The first route is arithmetic on totals and this one sums the
    decisions themselves, so a row set aside without its log line, or a value set to zero where it
    should have been read, makes the two disagree.
    """),
    code('''
def decisions(src):
    """The rows set aside as repeats, and one log line per value read back from text."""
    set_aside, log, kept_ids = [], [], set()
    for r in src:
        if r["order_id"] in kept_ids:
            set_aside.append(r)
            continue
        kept_ids.add(r["order_id"])
        if not r["amount"].isdigit():
            log.append({"order_id": r["order_id"], "decision": "convert and flag", "read_as": read_value(r["amount"])})
    return set_aside, log


set_aside, log = decisions(rows)
set_aside_rupees = sum(read_value(r["amount"]) for r in set_aside)
read_back = sum(e["read_as"] for e in log)
kit.equation(["the set-aside list\\nsummed", "+", "the log's values\\nsummed", "=", "the bridge's\\ntwo moves"],
             title="The second route: the decisions, summed on their own")
kit.check("the rows set aside add up to the rupees the bridge took out", set_aside_rupees == -extra_rows,
          f"{len(set_aside)} rows, {kit.rupees(set_aside_rupees)}")
kit.check("the values in the log add up to the rupees the bridge read back", read_back == text_back,
          f"{len(log)} line, {kit.rupees(read_back)}")
'''),
    mdj("""
    **What happened.** Both sums land: on the invented export the 8 rows set aside come to Rs
    12,16,420 and the one log line reads back Rs 8,50,000, each equal to its move in the bridge.

    **When to switch routes.** Show Finance the forward bridge, because it starts from their export.
    Run this second route before you send it: it proves every rupee the bridge moved is a row in the
    set-aside list or a value in the log, each summed on its own. It cannot tell you whether each
    decision was right, whether a row set aside really repeats an order or a value was read correctly;
    the order-level match is what answers that.

    **Your turn, on this morning's file.** The bridge says how many rupees Finance does not hold. It
    does not say which rows they are, and Anand will ask. Type these lines into the empty cell below
    and run it:

    ```python
    lab_set_aside, lab_log = decisions(lab)
    kit.check("this morning's set-aside rows add up to the bridge's first move",
              sum(read_value(r["amount"]) for r in lab_set_aside) == -lab_extra)
    kit.check("this morning's log adds up to the bridge's second move", sum(e["read_as"] for e in lab_log) == lab_back)
    kit.table(list(lab[0]), [list(r.values()) for r in lab_set_aside], caption="Rows Finance does not hold")
    ```

    Read the rows the table lists, and write what you would tell the person who owns the export.
    """),
    empty(),
    mdj("""
    ## Depth: can the same repeated rows move a branch of the tree as well?

    Rows Finance does not hold inflate a total, and when they sit in one segment they can move a branch
    too: extra rows for the same customers read as customers ordering more often. The cell below runs
    the tree's two lower branches for each consumer segment of the invented export, on the hurried rows
    and on one row per order.
    """),
    code('''
def branch(src, q, seg):
    """Orders per customer and revenue per order for one segment and quarter, on the rows that convert."""
    rs = [r for r in src if r["quarter"] == q and r["segment"] == seg and r["amount"].isdigit()]
    return len(rs) / len({r["customer_id"] for r in rs}), sum(int(r["amount"]) for r in rs) / len(rs)


out = []
for seg in SEGS[:3]:
    (fh1, _), (fh2, _) = branch(rows, "Q1", seg), branch(rows, "Q2", seg)
    (fc1, bc1), (fc2, bc2) = branch(once, "Q1", seg), branch(once, "Q2", seg)
    out.append((seg, f"{fh1:.2f} to {fh2:.2f}", f"{fc1:.2f} to {fc2:.2f}", f"{change(bc1, bc2):+.1f}%"))
kit.table(["segment", "orders per customer, hurried rows", "orders per customer, one row per order",
           "revenue per order, one row per order"], out, caption="Invented: the same rows, two readings of a branch")
kit.check("the repeated rows make one segment's customers look as if they order more often",
          any(o[1] != o[2] for o in out))
'''),
    mdj("""
    **What happened.** On the invented export the repeated batch sits in Retail-Plus: its members seem to
    order 2.44 times each in Q2 against 2.00 in Q1 on the hurried rows, a fifth more often, while one
    row per order shows frequency flat at 2.00 and revenue per order down 15.0 percent. A note built on
    the hurried rows would have named a frequency rise that never happened and missed the basket fall.
    Retail-Core reads 1.46 orders per customer in Q1 in this table, where chapter 3's clean tree gives
    1.50, because one of its Q1 orders has no segment until chapter 2 restores it.

    **Your turn, on this morning's file.** Run the same comparison on the lab export. Type these lines
    into the empty cell below and run it:

    ```python
    for seg in SEGS[:3]:
        (fh1, _), (fh2, _) = branch(lab, "Q1", seg), branch(lab, "Q2", seg)
        (fc1, bc1), (fc2, bc2) = branch(lab_once, "Q1", seg), branch(lab_once, "Q2", seg)
        print(f"{seg}: orders per customer {fh1:.2f} to {fh2:.2f} hurried, {fc1:.2f} to {fc2:.2f} one row "
              f"per order; revenue per order {change(bc1, bc2):+.1f}%")
    ```

    Do this morning's hurried rows move any segment's orders per customer, and which branch would a
    note built on them have named?
    """),
    empty(),
    mdj("""
    > **Kavya's review.** A number that has not been reconciled can point the wrong way, as the invented
    > export's hurried run did. Put the two checks in a cell before you compute the first number you
    > plan to send, so the clock cannot remove them.

    ### How would you answer this in an interview?

    **[S] Walk me through how you clean and check a dataset you have never seen.** "I profile every
    field first: present, convertible and distinct counts, and each count that is not what the field
    should hold is a finding. I clean with a log, one row per decision with its reason, and I keep what
    I reject. Then I reconcile before I analyse: rows read equal rows kept plus rows rejected, and each
    period's value lands on a total from outside the file, Finance's if there is one. On a two-quarter
    export in training, the count check alone moved my headline from +21.2 to -17.5 percent, and only
    the rupee check reached the books' -35.0, so I never stop at counts."

    **[F] You have two hours and a raw export; what do you do first, and what do you skip?** "Profile
    first, twenty minutes. I never skip the reconciliation, because it is the step that can flip the
    sign of the finding and it costs fifteen minutes. I skip anything that does not change today's
    answer: a second chart, a test on every segment, polishing. If there is no control total, I say so
    in the caveat and ask for one before the number leaves the room."

    **The design question: which check, and what would make you switch?** "Counts and rupees against a
    control total, with a bridge, because it catches both kinds of error for fifteen minutes and needs
    only what comes with the export. I switch to an order-level match against the ledger when the bridge
    will not close or when there is no control total, and I say it will cost the afternoon."

    ### What do you check against when there is no control total?

    A careful analyst tries three stand-ins, in this order: the same quarters in a second export
    pulled from the source system on another day; the payment gateway's settlement totals for the
    quarter, which count collected money and so need their own bridge to booked money; last quarter's
    audited figure for the quarter that overlaps. Each is weaker than Finance's number, and the note
    says which one was used.
    """),
    mdj("""
    ## So, do the two quarters in your note match Finance's books?

    They match only once both checks have run. On the invented export:

    1. A pass that skips the reconciliation sends Q2 up 21.2 percent, where the books say down 35.0.
    2. Counts and rupees with a bridge (C) is the best fit: fifteen minutes, the only option run here
       that lands to the rupee, and D takes over when there is no control total or the bridge will not
       close.
    3. The count check lands every order and leaves the headline at -17.5 percent, half its size.
    4. Rs 12,16,420 of rows Finance does not hold come out and Rs 8,50,000 is read back, and the walk
       lands on Rs 66,00,000.
    5. The set-aside list and the log, each summed on its own, equal the two moves.

    The your-turn cells put this morning's file through the same five steps. Chapter 2 asks the
    question the count check left open: when every count lands and nothing was rejected, what else can
    a pass have lost?
    """),
    code('kit.check_summary()\nprint("Next, chapter 2: every count reconciles and nothing was rejected, so is the pass finished?")'),
]

# --------------------------------------------------------------------------------- chapter 2
CH2 = [
    mdj("""
    # 2. Every count reconciles and nothing was rejected: is the pass finished?

    **Week 1, Friday. The lab debrief, chapter 2 of 3.** Chapter 1 put the room's hurried headline
    beside Finance's books, on an invented export: the hurried pass sent Q2 up 21.2 percent, a count
    check moved it to -17.5 percent with every order landing, and only the rupee check reached the
    books' -35.0. This chapter asks what else a pass can lose when every count lands, sizes four ways
    to handle a value that will not convert, and follows the same silence one step later, into a
    segment filter.

    **Who needs the answer.** Anand Iyer's analyst audits every note before it reaches Meera Raghavan,
    and asks for the rupees before the rows. A base quarter short by one large order can halve the fall
    the note reports: nobody argues with the direction, so nobody acts at the right scale, and when
    Finance finds the missing order every other number in the note is doubted with it.

    **The questions on the way.**

    1. What does a pass that sets unreadable values to zero report?
    2. What do the rupees say when every count lands?
    3. Which of four answers fits a value that will not convert?
    4. What does reading the value change in the note?
    5. Can a segment filter drop a row without a word, as the zero did?
    6. Can the file alone, with no control total, find the gap?

    **The metric at stake.** Q1 booked revenue, the base every Q1 to Q2 rate is measured from.

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
    """, HONESTY),
    code(LOAD + '''

def first_of_each(src):
    """One row per order id, the first to arrive: the identity rule from chapter 1."""
    kept = {}
    for r in src:
        kept.setdefault(r["order_id"], r)
    return list(kept.values())


once = first_of_each(rows)
truth = change(ctl("Q1")[0], ctl("Q2")[0])
print(f"{len(once)} orders after one row per order id; the books say Q1 to Q2 {truth:+.1f}% (invented)")
'''),
    map_cell(1, 1),
    mdj("""
    ## 1. What does a pass that sets unreadable values to zero report?

    The most natural line of Python in the week wraps the conversion in a `try` and sets a failure to
    zero, and it runs to the end without an error.

    **Predict before you run.** The pass keeps one row per order and sets any value that will not
    convert to zero. On the invented export, how many orders does Q1 report against Finance's 83, and
    how many rejects?

    - a) 82 orders and 1 reject.
    - b) 83 orders and 0 rejects.
    - c) 83 orders and 1 reject.
    - d) 81 orders and 2 rejects.
    """),
    code('''
def to_int_or_zero(v):
    try:
        return int(v)
    except ValueError:
        return 0          # the file now "converts" cleanly


def zeroing_pass(src):
    return {q: [to_int_or_zero(r["amount"]) for r in src if r["quarter"] == q] for q in QUARTERS}


zeroed = zeroing_pass(once)
kit.stats([(len(zeroed["Q1"]), "Q1 orders", f"Finance: {ctl('Q1')[1]}, invented"),
           (0, "rejects reported", "the try swallowed every failure"),
           ("all", "rows kept", "nothing set aside")])
kit.check("the zeroing pass lands on Finance's order counts", all(len(zeroed[q]) == ctl(q)[1] for q in QUARTERS))
'''),
    mdj("""
    **What happened.** The answer is b. Every order count lands and nothing is rejected, which is
    exactly what a finished pass looks like.

    **Your turn, on this morning's file.** Run the same zeroing pass on the lab export. Type these
    lines into the empty cell below and run it; later your-turn cells use `lab` and `lab_once`, so run
    this one first:

    ```python
    lab, lab_book = load_export("lab")
    lab_once = first_of_each(lab)
    lab_zeroed = zeroing_pass(lab_once)
    print({q: (len(lab_zeroed[q]), ctl(q, lab_book)[1]) for q in QUARTERS}, "orders against Finance's; 0 rejects")
    ```
    """),
    empty(),
    mdj("""
    ## 2. What do the rupees say when every count lands?

    **The plausible wrong answer.** "Q1 on 83 orders, zero rejects, counts reconciled; Q2 fell 17.5
    percent." Every word of it can be defended except the number the rate is built on.

    **Predict before you run.** Against Finance's rupee totals, what does the zeroing pass show on the
    invented export?

    - a) Both quarters land to the rupee.
    - b) One quarter over, the other landing.
    - c) One quarter short, the other landing.
    - d) Both quarters short by a few rupees of rounding.
    """),
    code('''
z_change = change(sum(zeroed["Q1"]), sum(zeroed["Q2"]))
gap = {q: ctl(q)[0] - sum(zeroed[q]) for q in QUARTERS}
kit.table(["quarter", "orders", "Finance's orders", "summed", "Finance's rupees", "gap"],
          [(q, len(zeroed[q]), ctl(q)[1], kit.rupees(sum(zeroed[q])), kit.rupees(ctl(q)[0]), kit.rupees(gap[q]))
           for q in QUARTERS], caption="Invented: counts land, rupees do not")
kit.bars([("the zeroing pass: a fall", round(abs(z_change), 1)), ("Finance's books: a fall", round(abs(truth), 1))],
         fmt=lambda v: f"{v:.1f}%", lit=(1,), width=640, title="Invented: the fall the note reports, against the books")
kit.check("every order count lands on Finance's", all(len(zeroed[q]) == ctl(q)[1] for q in QUARTERS))
kit.check("the rupees miss Finance's in one quarter and land in the other",
          sum(1 for q in QUARTERS if gap[q] != 0) == 1 and all(gap[q] >= 0 for q in QUARTERS))
'''),
    mdj("""
    **What happened.** The answer is c. The counts reconcile, Q1's rupees come up Rs 8,50,000 short,
    about a fifth of the quarter, and the note reports a fall of 17.5 percent where the books show
    35.0.

    **Why it is wrong.** The `try` turned "I could not read this value" into "this order was worth
    nothing", and zero is a number, so no later step can tell the difference. A count check cannot see
    it, because the row is still there. The direction is right, so nobody argues, and the size is half,
    so nobody acts at the right scale. The check that catches it is the one chapter 1 made standard:
    the rupees against the control total.

    **Your turn, on this morning's file.** Which quarter misses, and by how much? Type these lines into
    the empty cell below and run it:

    ```python
    lab_gap = {q: ctl(q, lab_book)[0] - sum(lab_zeroed[q]) for q in QUARTERS}
    kit.table(["quarter", "orders", "Finance's orders", "summed", "Finance's rupees", "gap"],
              [(q, len(lab_zeroed[q]), ctl(q, lab_book)[1], kit.rupees(sum(lab_zeroed[q])),
                kit.rupees(ctl(q, lab_book)[0]), kit.rupees(lab_gap[q])) for q in QUARTERS],
              caption="This morning's file: counts against rupees")
    ```
    """),
    empty(),
    mdj("""
    ## 3. Which of four answers fits a value that will not convert?

    A value that will not convert is a decision, and it goes in the log whichever way it goes. The
    cell below sizes four answers on the invented export, on what separates them: what each assumes
    about the value, the analyst's minutes, what the log and the reconciliation then show, and the
    headline each lets through. The minutes are this programme's estimate, and D's is a wait on
    another team.

    | Option | What it does |
    |---|---|
    | A. Zero in a try | Sets the value to 0 and says nothing |
    | B. Drop with a reason | Rejects the row and logs why |
    | C. Read it, convert, keep and flag | Reads the value without guessing, and logs the text and the number |
    | D. Hold and ask the owner | Leaves the row out of today's totals until the order's owner confirms the amount, and the note says it is provisional |
    """),
    code('''
def run_option(src, option):
    """Each quarter's rupees and orders, and the log, under one answer to a value that will not convert."""
    kept, counts, log = {q: 0 for q in QUARTERS}, {q: 0 for q in QUARTERS}, []
    for r in src:
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


def size_answers(src, book):
    table_rows, points = [], []
    books = change(ctl("Q1", book)[0], ctl("Q2", book)[0])
    for option, assumes, minutes in [("A", "the order was worth nothing", 1), ("B", "the row is not an order", 2),
                                     ("C", "the value can be read without a guess", 3),
                                     ("D", "only the order's owner can say", "a wait")]:
        kept, counts, log = run_option(src, option)
        sent = change(kept["Q1"], kept["Q2"])
        count_ok = all(counts[q] == ctl(q, book)[1] for q in QUARTERS)
        rupee_ok = all(kept[q] == ctl(q, book)[0] for q in QUARTERS)
        table_rows.append((option, assumes, minutes, len(log), "passes" if count_ok else "fails",
                           "passes" if rupee_ok else "fails", "provisional" if option == "D" else f"{sent:+.1f}%"))
        if option != "D":
            points.append((f"option {option}", round(abs(sent - books), 1)))
    return table_rows, points


ANSWER_HEADERS = ["option", "assumes", "analyst minutes", "log lines", "count check", "rupee check", "headline sent"]
opt_rows, pts = size_answers(once, control)
kit.table(ANSWER_HEADERS, opt_rows, caption="Invented: four answers to a value that will not convert, sized")
kit.bars(pts, lit=(2,), fmt=lambda v: f"{v:.1f} pts",
         title="Invented: points between each headline sent and the books (D sends a provisional note)")
'''),
    code('''
kit.check("only A leaves no trace in the log", [r[3] for r in opt_rows] == [0, 1, 1, 1])
kit.check("B fails the count check, so its gap is visible", opt_rows[1][4] == "fails")
kit.check("C passes both checks", opt_rows[2][4] == opt_rows[2][5] == "passes")
'''),
    mdj("""
    **What happened, and the best-fit call.** C, when the value can be read without a guess: reading it
    costs a minute and one log line and lands both quarters on the books. A is the only option that is
    never right: it sends the same -17.5 percent as B and hides it. B is honest and still wrong by 17.5
    points; what it has going for it is that the count check now fails, so its gap is visible. D is
    right on the day the text could be read two ways.

    **What would change the call.** Text that cannot be read without a guess moves the call to D: a
    value written as a word, a decimal whose unit is unclear (lakh or crore), a currency that is not
    the file's. A row that is not an order at all, a test transaction, moves it to B. Whichever way it
    goes, the decision lives in a log line and shows in the reconciliation.
    """),
    code('''
kit.vflow(["a value that will not convert",
           "can you read it without guessing?",
           "yes: convert, keep and flag it (C)",
           "no, and the row matters: hold it and ask the owner (D)",
           "no, and it is not an order: drop it with a reason (B)"], lit=2,
          title="Three honest answers to a value that will not convert")
'''),
    mdj("""
    **Your turn, on this morning's file.** Size the same four answers on the lab export, then find the
    row the rupee check points at and read its value yourself. Type these lines into the empty cell
    below and run it:

    ```python
    kit.table(ANSWER_HEADERS, size_answers(lab_once, lab_book)[0], caption="The four answers on this morning's file")
    for r in lab_once:
        if not r["amount"].isdigit():
            print(r)
    ```

    Can this value be read without a guess, and so which option does it call for? Write the
    decisions-log line you would hand Anand's analyst: the order id, the decision and the reason, in one
    row.
    """),
    empty(),
    mdj("""
    ## 4. What does reading the value change in the note?

    **Predict before you run.** Reading the value moves the invented headline from -17.5 to -35.0
    percent. How many more rupees of fall does Monday's review now have to explain?

    - a) Rs 5,50,000.
    - b) Rs 8,50,000.
    - c) Rs 14,00,000.
    - d) Rs 26,00,000.
    """),
    code('''
fixed, fixed_counts, fixed_log = run_option(once, "C")
kit.table(["the decision about the value", "Q1", "Q1 to Q2"],
          [("zero in a try", kit.rupees(sum(zeroed["Q1"])), f"{change(sum(zeroed['Q1']), sum(zeroed['Q2'])):+.1f}%"),
           ("read, convert, flag", kit.rupees(fixed["Q1"]), f"{change(fixed['Q1'], fixed['Q2']):+.1f}%")],
          caption="Invented: the same rows, two decisions about one value")
kit.check("the fixed pass lands on both control totals", all(fixed[q] == ctl(q)[0] for q in QUARTERS))
kit.check("one log line records the decision", len(fixed_log) == 1)
'''),
    mdj("""
    **What happened.** The answer is b. One log line adds Rs 8,50,000 of fall to the note: the
    invented export's reported fall grows from Rs 5,50,000, 17.5 percent, to Rs 14,00,000, 35.0 percent,
    on the books. In the review, that is the difference between "a soft quarter" and "a quarter to
    explain".

    ## 5. Can a segment filter drop a row without a word, as the zero did?

    A pass looks clean whenever a step can lose something without saying so. The next place it happens
    is the tree: a filter on the segment name never sees a row whose segment is empty. On the invented
    export one Q1 order has no segment, and its customer's other orders are all Retail-Core.

    **Predict before you run.** Read on named rows only, what does Retail-Core's change from Q1 to Q2
    look like?

    - a) A fall of 1.0 percent.
    - b) A rise of 2.2 percent.
    - c) No change at all.
    - d) A fall of about 3 percent.
    """),
    code('''
def named_and_restored(src, seg):
    """A segment's quarters on named rows, and with each unnamed row restored from its customer's other orders."""
    named = {q: sum(read_value(r["amount"]) for r in src if r["quarter"] == q and r["segment"] == seg) for q in QUARTERS}
    restored = dict(named)
    for r in src:
        if r["segment"]:
            continue
        others = {o["segment"] for o in src if o["customer_id"] == r["customer_id"] and o["segment"]}
        if others == {seg}:
            restored[r["quarter"]] += read_value(r["amount"])
    return named, restored


named, restored = named_and_restored(once, "Retail-Core")
blank = [r for r in once if not r["segment"]]
kit.columns(["Q1, named rows", "Q1, order restored", "Q2"],
            [("Retail-Core, invented", [named["Q1"], restored["Q1"], named["Q2"]])],
            fmt=lambda v: kit.rupees(v), lit=(1,), width=560,
            title="Invented: one unnamed Q1 order turns a small fall into a rise")
kit.check("the named segments fall one order short of the quarter",
          sum(1 for r in once if r["quarter"] == "Q1" and r["segment"] in SEGS) == ctl("Q1")[1] - len(blank))
kit.check("named rows read a rise where the restored segment fell",
          change(named["Q1"], named["Q2"]) > 0 > change(restored["Q1"], restored["Q2"]),
          f"{change(named['Q1'], named['Q2']):+.1f}% against {change(restored['Q1'], restored['Q2']):+.1f}%")
'''),
    mdj("""
    **What happened.** The answer is b. On named rows the invented Retail-Core's Q1 is Rs 73,250, so the
    segment seems to rise 2.2 percent to Q2's Rs 74,880; with the order restored from its customer's
    other orders Q1 is Rs 75,600 and the segment fell 1.0 percent, so the named rows turned a fall into
    a rise.

    **Why it is wrong, and the fix.** The filter dropped the order, and nobody chose to drop it. The
    check is one line, that the segments add back to the quarter in orders and in rupees, and it fails by exactly
    the rows the filter never saw. The fix is a logged decision: restore the segment from the customer's
    other orders when all of them carry one segment, flag it and name it in the caveat, or keep the row
    as "segment unknown", named and flagged, with the segment sums reconciled to the quarter.

    **Your turn, on this morning's file.** Do the lab file's named segments add back to each quarter,
    and if a quarter falls short, which segment moves when the row is restored? Type these lines into
    the empty cell below and run it:

    ```python
    for q in QUARTERS:
        n = sum(1 for r in lab_once if r["quarter"] == q and r["segment"] in SEGS)
        print(q, "named orders", n, "against Finance's", ctl(q, lab_book)[1])
    for r in lab_once:
        if not r["segment"]:
            others = {o["segment"] for o in lab_once if o["customer_id"] == r["customer_id"] and o["segment"]}
            print(r["order_id"], r["quarter"], "customer's other segments:", others)
            if len(others) == 1:
                seg = next(iter(others))
                n_, r_ = named_and_restored(lab_once, seg)
                print(f"{seg}: {change(n_['Q1'], n_['Q2']):+.1f}% on named rows, "
                      f"{change(r_['Q1'], r_['Q2']):+.1f}% with the order restored")
    ```
    """),
    empty(),
    mdj("""
    ## 6. Can the file alone, with no control total, find the gap?

    The rupee check found the gap from outside the file. The second route finds it from inside, and it
    should land on the same number: every value present is either summed as it came or appears in the
    log with the number it was read as. Values present equal values that convert plus values logged,
    and the logged values add up to the gap. The rupee check uses Finance's total and this uses only the
    file, so each can fail where the other passes.
    """),
    code('''
def value_accounting(src):
    present = sum(1 for r in src if r["amount"] != "")
    convertible = sum(1 for r in src if r["amount"].isdigit())
    logged = [read_value(r["amount"]) for r in src if not r["amount"].isdigit()]
    return present, convertible, logged


present, convertible, logged = value_accounting(once)
rupee_gap = sum(gap.values())
kit.equation(["values present", "=", "convertible", "+", "in the log"],
             title="The second route: every value is summed as it came or logged with the number it was read as")
kit.check("present equals convertible plus logged", present == convertible + len(logged),
          f"{present} = {convertible} + {len(logged)}")
kit.check("the logged values add up to the gap the rupee check found", sum(logged) == rupee_gap, kit.rupees(rupee_gap))
'''),
    mdj("""
    **What happened.** On the invented export 167 values are present, 166 convert and 1 is logged, and
    the logged value, Rs 8,50,000, is exactly the gap the rupee check found.

    **When to switch routes.** The rupee check needs a control total and tells you how much is missing;
    the value accounting needs nothing outside the file and tells you where. On a file with no control
    total, the value accounting is the check you still have.

    **Your turn, on this morning's file.** Type this line into the empty cell below and run it:

    ```python
    lab_present, lab_convertible, lab_logged = value_accounting(lab_once)
    print(lab_present, "=", lab_convertible, "+", len(lab_logged), "| logged", [kit.rupees(v) for v in lab_logged],
          "| the gap", kit.rupees(sum(lab_gap.values())))
    ```

    > **Kavya's review.** A count check proves the rows are there. Only a rupee check proves the values
    > survived. Setting a value to zero claims the order was worth nothing, so that decision belongs in
    > the log with a reason.
    """),
    empty(),
    mdj("""
    ### How would you answer this in an interview?

    **[D] Your cleaning pass reports zero rejects. What do you check?** "I distrust the zero before I
    trust it. First, rows against distinct ids, because a repeated batch is the commonest reason a total
    runs high. Second, how my code handled a value that would not convert: if a `try` set it to zero,
    the rejects count is hiding it. Third, the rupees per period against a control total, with a bridge
    from my number to theirs. On a training export a zeroing pass reconciled every count and still left
    the base quarter Rs 8,50,000 short, which halved the fall the note reported."

    **[F] How do you handle a value that will not convert?** "Three honest answers: read it and convert
    it when it can be read without guessing, hold it and ask the owner when it cannot, drop it with a
    reason when the row is not an order. Every one gets a log line and shows in the reconciliation. I
    never set it to zero, because zero is a number and nothing later can tell it from a real one."

    **The design question: when would you drop the row instead of reading it?** "When the row is not
    the thing being counted, a test order or a cancelled draft, and the log says so. When the value
    matters and I cannot read it without guessing, I hold it and ask, and the note says the quarter is
    provisional by that amount."

    ### Where else can a pass look clean?

    A pass can look clean at any step that loses something silently: a date parse that sends a bad date to a default, a
    currency converter that returns zero for a code it does not know, a filter on a name that is
    sometimes blank. The check is always the same: what went in equals what came out plus what was
    set aside, in rows and in value.

    ## So, when every count reconciles, is the pass finished?

    It is finished only once the rupees land too. On the invented export:

    1. The zeroing pass reports 83 Q1 orders against Finance's 83, and 0 rejects.
    2. The rupees show Q1 Rs 8,50,000 short, and the note's fall reads 17.5 percent where the books say
       35.0.
    3. Reading the value, keeping it and flagging it (C) is the best fit when it can be read without a
       guess; D fits when it cannot, B when the row is not an order, and A never does.
    4. One log line moves the fall to 35.0 percent, Rs 14,00,000 on the books.
    5. A segment filter drops the unnamed order, and Retail-Core reads +2.2 percent where it fell 1.0.
    6. Values present, 167, equal 166 that convert plus 1 logged, and the logged Rs 8,50,000 is the gap.

    Chapter 3 takes the reconciled numbers into the tree and asks which of the right numbers leads.
    """),
    code('kit.check_summary()\nprint("Next, chapter 3: which finding leads the note, and how sure can Meera be of it?")'),
]

# --------------------------------------------------------------------------------- chapter 3
CH3 = [
    mdj("""
    # 3. Which finding leads the note, and how sure can Meera be of it?

    **Week 1, Friday. The lab debrief, chapter 3 of 3.** Chapters 1 and 2 put both quarters of an
    invented export on the books to the rupee: Q1 Rs 40,00,000 on 83 orders and Q2 Rs 26,00,000 on 84,
    a fall of 35.0 percent, once 8 repeated rows were set aside, one value stored as text was read and
    one order with no segment was restored to its customer's segment. This chapter reads the clean tree, sizes
    four ways to choose the lead and runs every one of them, and tests the lead on each member's own
    two quarters.

    **Who needs the answer.** Meera Raghavan, Kalpa Retail's CEO, reads the first line of the note and
    acts on it, and
    Marketing will attack any rate that rests on a handful of orders. A trend claimed from a few orders
    sends a team to fix a segment that did nothing while the branch that moved goes unopened for a
    quarter, and the first time Marketing asks "on how many orders?", the whole note loses the room.

    **The questions on the way.**

    1. Where in the tree does the fall sit?
    2. How many orders does the biggest move rest on?
    3. How should a team choose the lead, and what does each way cost?
    4. Is the lead's fall more than chance on its members' own two quarters?
    5. Is the fall broad, or carried by a few members?

    **The metric at stake.** The Q1 to Q2 fall split along the revenue tree, segment by segment:
    revenue is customers, times orders per customer (how often each buys, the frequency), times revenue
    per order (the basket). Retail-Plus is the paid members' tier and Business is the corporate book.

    **Who else faces this.** IMDb will not rank a film in its Top 250 until it has at least 25,000
    ratings from regular voters, and its weighted rating pulls a title with few votes toward the average
    of all titles (IMDb Help, ratings FAQ, updated 9 February 2026), so a 9.4 on a few hundred votes is
    not allowed to beat a 9.0 on a million. A public case shows the cost of ignoring it: Howard Wainer's
    "The Most Dangerous Equation" shows small schools over-represented among both the best and the
    worst performers, because small samples vary more, after the Gates Foundation had put about $1.7
    billion into education grants by 2001, with small schools central to them (Wainer, Picturing the
    Uncertain World, Princeton University Press, 2009, chapter 1).
    """, HONESTY),
    code(LOAD + '''

def tidy(src):
    """One row per order, every value read, and an unnamed order restored to its customer's one segment."""
    kept = {}
    for r in src:
        kept.setdefault(r["order_id"], dict(r))
    out = list(kept.values())
    seg_of = {}
    for r in out:
        if r["segment"]:
            seg_of.setdefault(r["customer_id"], set()).add(r["segment"])
    for r in out:
        r["amount"] = read_value(r["amount"])
        if not r["segment"] and len(seg_of.get(r["customer_id"], ())) == 1:
            r["segment"] = next(iter(seg_of[r["customer_id"]]))
    return out


clean = tidy(rows)
kit.check("the clean invented data lands on both control totals, as chapters 1 and 2 left it",
          all(sum(r["amount"] for r in clean if r["quarter"] == q) == ctl(q)[0] for q in QUARTERS))
'''),
    map_cell(2, 3),
    mdj("""
    ## 1. Where in the tree does the fall sit?

    **Predict before you run.** Which segment carries most of the invented export's Rs 14,00,000 fall?

    - a) Retail-Core, the segment with the most orders.
    - b) Retail-Plus, the members' tier.
    - c) Business, the corporate book.
    - d) Student, the smallest segment.
    """),
    code('''
def tree(src, q, seg):
    rs = [r for r in src if r["quarter"] == q and r["segment"] == seg]
    cust = len({r["customer_id"] for r in rs})
    rev = sum(r["amount"] for r in rs)
    return {"orders": len(rs), "customers": cust, "freq": len(rs) / cust, "basket": rev / len(rs), "rev": rev}


def tree_table(src, caption):
    T = {(q, s): tree(src, q, s) for q in QUARTERS for s in SEGS}
    kit.table(["segment", "orders Q1 / Q2", "customers", "orders per customer", "revenue per order",
               "revenue change", "rupees moved"],
              [(s, f"{T['Q1', s]['orders']} / {T['Q2', s]['orders']}",
                f"{T['Q1', s]['customers']} / {T['Q2', s]['customers']}",
                f"{T['Q1', s]['freq']:.2f} / {T['Q2', s]['freq']:.2f}",
                f"{kit.rupees(T['Q1', s]['basket'])} / {kit.rupees(T['Q2', s]['basket'])}",
                f"{change(T['Q1', s]['rev'], T['Q2', s]['rev']):+.1f}%",
                kit.rupees(T['Q2', s]['rev'] - T['Q1', s]['rev'])) for s in SEGS], caption=caption)
    return T


T = tree_table(clean, "Invented: the clean tree, Q1 against Q2")
fall = ctl("Q1")[0] - ctl("Q2")[0]
biz = T["Q1", "Business"]["rev"] - T["Q2", "Business"]["rev"]
kit.stats([(f"{change(T['Q1', 'Business']['rev'], T['Q2', 'Business']['rev']):+.1f}%", "the corporate book",
            "revenue, Q1 to Q2, invented"),
           (kit.rupees(biz), "the fall it carries", f"{100 * biz / fall:.1f}% of the quarter's fall")])
kit.bars([(s, abs(T['Q2', s]['rev'] - T['Q1', s]['rev'])) for s in SEGS], lit=(3,), fmt=lambda v: kit.rupees(v),
         title="Invented: rupees moved per segment, Q1 to Q2, either direction")
kit.check("the segments add back to the quarter", all(sum(T[q, s]["rev"] for s in SEGS) == ctl(q)[0] for q in QUARTERS))
'''),
    mdj("""
    **What happened.** The answer is c. On the invented export Business carries Rs 13,88,200 of the Rs
    14,00,000 fall, 99.2 percent of it, and its revenue fell 36.3 percent. Among consumers, Retail-Plus
    kept its 16 members and their 2.00 orders each while its revenue per order fell 15.0 percent, from
    Rs 3,000 to Rs 2,550.

    **Your turn, on this morning's file.** Build the same tree on the lab export. Type these lines into
    the empty cell below and run it; the later your-turn cells use `lab_clean`, so run this one first:

    ```python
    lab, lab_book = load_export("lab")
    lab_clean = tidy(lab)
    LT = tree_table(lab_clean, "This morning's file: the clean tree, Q1 against Q2")
    ```

    Which segment carries most of this morning's fall, and which consumer branch moved?
    """),
    empty(),
    mdj("""
    ## 2. How many orders does the biggest move rest on?

    **The plausible wrong answer.** "The corporate book fell 36.3 percent and drove the whole decline;
    we recommend a corporate retention plan." It is true to the rupee and the biggest move on the page,
    so a hurried note leads with it.

    **Predict before you run.** The tree above puts five corporate orders in Q1 and two in Q2. If each
    of the seven were equally likely to land in either quarter, how often would a split at least that
    uneven come up?

    - a) About 5 percent of the time.
    - b) About 20 percent.
    - c) About 45 percent.
    - d) About 90 percent.
    """),
    code('''
def coin_flip_share(n1, n2):
    """How often coin flips split n1 + n2 orders between two quarters at least as unevenly."""
    n, gap = n1 + n2, abs(n1 - n2)
    return sum(comb(n, k) for k in range(n + 1) if abs(2 * k - n) >= gap) / 2 ** n


b1, b2 = T["Q1", "Business"]["orders"], T["Q2", "Business"]["orders"]
uneven = coin_flip_share(b1, b2)
kit.columns(["closer than the real split", "at least as uneven"], [("share of coin-flip worlds, invented", [1 - uneven, uneven])],
            fmt=lambda v: f"{v:.3f}", lit=(1,), width=560,
            title=f"Invented: {b1 + b2} corporate orders split by coin flips, at least as unevenly as {b1} and {b2} in {uneven:.0%} of worlds")
kit.check("the corporate rate rests on fewer than thirty orders", b1 + b2 < 30, f"{b1} then {b2}")
kit.check("the corporate book carries more than nine tenths of the fall", biz / fall > 0.9)
'''),
    mdj("""
    **What happened.** The answer is c. If each of the seven orders were equally likely to land in
    either quarter, a split at least as uneven as five and two would come up in 45 percent of worlds,
    and a corporate order here is worth several lakh, so a change of two or three orders moves the book
    by a third.

    **Why it is wrong.** The rupees are real and Meera should hear them. What a handful of orders cannot
    carry is the word "trend", or a plan built on it. The check is to count before you rate: put the
    order count beside every rate before deciding which one leads, and ask how often chance alone moves
    that many orders as unevenly.

    **The fix, and what it changes.** The corporate fall goes into the note as counts, five orders then
    two, beside the Rs 13,88,200 it carries, and its action is a question to whoever owns those
    accounts, which costs a phone call. The lead moves to the branch that moved on enough orders to
    read.

    **Your turn, on this morning's file.** Count the lab file's corporate orders in each quarter and run
    the same coin flips on them. Type these lines into the empty cell below and run it:

    ```python
    lb1, lb2 = LT["Q1", "Business"]["orders"], LT["Q2", "Business"]["orders"]
    print("corporate orders:", lb1, "in Q1 and", lb2, "in Q2;",
          f"coin flips split them at least that unevenly in {coin_flip_share(lb1, lb2):.1%} of worlds")
    ```

    Then write the corporate line of your note as counts: the orders in each quarter, then the rupees.
    """),
    empty(),
    mdj("""
    ## 3. How should a team choose the lead, and what does each way cost?

    The cell below sizes four ways on the invented clean tree: the claim each leads with, the orders behind
    that claim, how often chance alone produces it, and the analyst's minutes at the lab brief's pace.
    Option D is run here, one test per segment on that segment's own customers' two quarters, so its
    cost shows as a number.

    | Option | How it picks the lead |
    |---|---|
    | A. The biggest rupee move | Whatever moved most in rupees leads |
    | B. The total, unsplit | The quarter's change leads, and the split is left out |
    | C. Count before rate | Every rate carries its order count; a rate on fewer than about thirty orders goes to the caveat as counts, and the lead is the branch that moved on enough orders and survives one test |
    | D. Test everything | A test on every segment, and the smallest p-value leads |
    """),
    code('''
def members_of(src, seg):
    """Each customer of a segment with their own Q1 and Q2 orders, in customer order."""
    per = {}
    for r in src:
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


def paired_test(src, seg, basket=True, flips=2000, seed=7):
    """Flip each customer's own two quarters at random; the share of worlds as extreme, either way."""
    per = members_of(src, seg)
    observed = flipped_change(per, [False] * len(per), basket)
    rng = random.Random(seed)
    worlds = [flipped_change(per, [rng.random() < 0.5 for _ in per], basket) for _ in range(flips)]
    return observed, worlds, sum(1 for w in worlds if abs(w) >= abs(observed) - 1e-9) / flips


plus = [r for r in clean if r["segment"] == "Retail-Plus"]
obs_plus, worlds_plus, p_plus = paired_test(clean, "Retail-Plus")
four = [(s, *paired_test(clean, s, basket=False)[::2]) for s in SEGS]
false_alarm = 1 - 0.95 ** 4
kit.table(["option", "leads with", "orders behind it", "chance alone", "analyst minutes"], [
    ("A. biggest rupee move", f"Business {change(T['Q1', 'Business']['rev'], T['Q2', 'Business']['rev']):+.1f}%",
     b1 + b2, f"{uneven:.0%} of coin-flip worlds as uneven", 5),
    ("B. the total, unsplit", f"revenue {change(ctl('Q1')[0], ctl('Q2')[0]):+.1f}%", ctl("Q1")[1] + ctl("Q2")[1],
     "not asked", 2),
    ("C. count before rate", f"Retail-Plus revenue per order {obs_plus:+.1f}%, "
     f"{kit.rupees(T['Q1', 'Retail-Plus']['rev'] - T['Q2', 'Retail-Plus']['rev'])}", len(plus),
     "one test on its members' own two quarters, run at level 4", 15),
    ("D. test every segment", "the smallest of four p-values",
     f"{min(len([r for r in clean if r['segment'] == s]) for s in SEGS)} to "
     f"{max(len([r for r in clean if r['segment'] == s]) for s in SEGS)}",
     f"four tests, with a {false_alarm:.2f} chance that one looks real by luck; run at level 4", 45),
], caption="Invented: four ways to choose the lead, sized")
kit.matrix(["enough orders", "too few orders"], ["moved in rupees", "moved in rate only"],
           [["lead with it, tested", "lead only if it survives a test"],
            ["say it as counts, ask the owner", "leave it out of the claim"]],
           title="Where each finding goes in the note")
'''),
    code('''
kit.check("Retail-Plus's basket rests on more than thirty orders", len(plus) > 30, f"{len(plus)} orders")
kit.check("two segments rest on thirty or more orders, and the other two on fewer",
          sorted(len([r for r in clean if r["segment"] == s]) >= 30 for s in SEGS) == [False, False, True, True])
'''),
    mdj("""
    **What happened, and the best-fit call.** C. It costs about fifteen minutes and one test, and on the
    invented export it leads with Retail-Plus's revenue per order, down 15.0 percent on 64 orders, the
    one consumer move on enough orders to test; level 4 runs that test. The move is small in rupees, Rs
    14,400 of the fall, about 1 percent of it, so it leads among consumers while the corporate Rs
    13,88,200 sits beside it in the claim as counts. A leads on seven orders, too few to call a trend. B
    hides the one thing Meera most needs, that 99.2 percent of the fall is the corporate book. D spends
    four tests at three times the minutes, and with four tests at 0.05 the chance that at least one
    looks real by luck is about 19 percent, so on another file D leads with a fluke about one time in
    five; level 4 runs it on this file.

    **What would change the call.** A question about accounts: if Meera asked "what
    happened to our corporate revenue?", the lead is the corporate fall, said as counts, with the
    accounts named by their owner. A corporate book of hundreds of orders a quarter would let its rate
    lead. And a second quarter of the same move in Business would turn a phone call into a trend worth
    testing.

    **Your turn, on this morning's file.** Run option D's four tests on the lab file and read which
    segment each option would lead with there. Type these lines into the empty cell below and run it:

    ```python
    for s in SEGS:
        o, _, p = paired_test(lab_clean, s, basket=False)
        print(f"{s}: revenue {o:+.1f}%, p = {p:.3f} with each customer's quarters flipped")
    ```
    """),
    empty(),
    mdj("""
    ## 4. Is the lead's fall more than chance on its members' own two quarters?

    Retail-Plus keeps its 16 members in both quarters, each placing the same number of orders in each
    (one, two or three), while its revenue per order falls 15.0 percent. The claim is about the same
    members in both quarters, so the fair test keeps each member's own two quarters together. In a world
    where the quarter made no difference, each member's Q1 and Q2 are as likely either way round, so the
    test swaps them at random for each member, recomputes the tier's revenue per order, and counts the
    worlds with a change at least as large. The fall was found by reading the tree, so a rise of that
    size counts as well, and the note reports both directions.

    **Predict before you run.** Where does the real change sit among 2,000 worlds with each member's
    quarters flipped at random?

    - a) In the middle of the pile.
    - b) At the edge: about two dozen worlds are as extreme.
    - c) Beyond every flipped world.
    - d) The test cannot run, since members placed different numbers of orders.
    """),
    code('''
one_way = sum(1 for w in worlds_plus if w <= obs_plus + 1e-9) / 2000
per_plus = members_of(clean, "Retail-Plus")
diffs = [sum(v["Q2"]) - sum(v["Q1"]) for v in per_plus.values()]
total_rev = sum(sum(v["Q1"]) + sum(v["Q2"]) for v in per_plus.values())
dist = {0: 1}                       # every one of the 2^16 flip patterns, counted exactly
for d in diffs:
    nxt = {}
    for s, c in dist.items():
        nxt[s + d] = nxt.get(s + d, 0) + c
        nxt[s - d] = nxt.get(s - d, 0) + c
    dist = nxt
exact = sum(c for s, c in dist.items()
            if abs(change((total_rev - s) / 2, (total_rev + s) / 2)) >= abs(obs_plus) - 1e-9) / 2 ** len(diffs)
print(f"Invented: Retail-Plus revenue per order {obs_plus:+.1f}%; {round(p_plus * 2000)} of 2,000 flipped worlds as "
      f"large either way, p = {p_plus:.4f}; counted one way, {one_way:.4f}; exact over all "
      f"{2 ** len(diffs):,} flip patterns, {exact:.4f}")
edges = list(range(3 * (int(min(worlds_plus)) // 3 - 1), 3 * (int(max(worlds_plus)) // 3 + 2), 3))
extreme = [i for i, e in enumerate(edges) if e + 3 <= -abs(obs_plus) + 1e-9 or e >= abs(obs_plus) - 1e-9]
kit.bars([(f"{e:+d}% to {e + 3:+d}%", sum(1 for w in worlds_plus if e <= w < e + 3)) for e in edges], lit=extreme,
         width=820, title=f"Invented: 2,000 flipped worlds; the {round(p_plus * 2000)} in dark bars are as extreme "
                          f"as the real {obs_plus:+.1f}%")
kit.check("Retail-Plus's members and their frequency hold while its basket falls",
          T["Q1", "Retail-Plus"]["customers"] == T["Q2", "Retail-Plus"]["customers"]
          and abs(T["Q1", "Retail-Plus"]["freq"] - T["Q2", "Retail-Plus"]["freq"]) < 0.01)
kit.check("the sampled share and the exact share agree within the wobble of 2,000 flips", abs(p_plus - exact) < 0.005,
          f"{p_plus:.4f} against {exact:.4f}")
kit.check("the dark bars hold exactly the worlds counted as extreme",
          sum(sum(1 for w in worlds_plus if edges[i] <= w < edges[i] + 3) for i in extreme) == round(p_plus * 2000))
'''),
    mdj("""
    **What happened.** The answer is b. Only 22 of 2,000 flipped worlds show a change as large as the
    invented Retail-Plus's, in either direction: p = 0.011, a share of chance-only worlds, never the
    chance the finding is wrong. Counting every one of the 65,536 ways to flip sixteen members gives
    0.0107, so 2,000 flips land close. Counted one way, a fall at least as large, it is 0.0015, the
    number a note would quote only if the fall had been predicted before the data was seen; it was found
    in the tree, so the note reports both directions.

    **Option D, run.** One test per segment, each on its own customers' two quarters, now that the
    lead's own test is in: the cell below shows whether any second segment comes in under 0.05.
    """),
    code('''
kit.table(["segment", "revenue change", "p, each customer's quarters flipped, 2,000 times"],
          [(s, f"{o:+.1f}%", f"{p:.3f}") for s, o, p in four], caption="Invented: option D, run, one test per segment")
kit.check("Retail-Plus's fall is one chance rarely produces on its members' own quarters", p_plus < 0.05,
          f"p = {p_plus:.3f}")
kit.check("testing every segment turns up no second finding under 0.05", sum(1 for f in four if f[2] < 0.05) == 1)
'''),
    mdj("""
    **What happened.** Only Retail-Plus comes in under 0.05, so D finds the same lead as C, at three
    times the minutes and with four chances of a fluke where C took one.

    **A different question needs a different test.** "Did Retail-Plus's basket move differently from
    Retail-Core's?" compares two groups of different customers. There the fair test shuffles the segment
    label across whole customers, each carrying all their orders with them, and asks how often a gap as
    large as the real one turns up.
    """),
    code('''
def basket_change(rs):
    a = [r["amount"] for r in rs if r["quarter"] == "Q1"]
    b = [r["amount"] for r in rs if r["quarter"] == "Q2"]
    return change(sum(a) / len(a), sum(b) / len(b))


def between_test(src, seg_a, seg_b, shuffles=2000, seed=7):
    """The gap in basket change between two segments, and the share of label shuffles across whole customers as large."""
    a_rows = [r for r in src if r["segment"] == seg_a]
    b_rows = [r for r in src if r["segment"] == seg_b]
    gap = basket_change(a_rows) - basket_change(b_rows)
    groups = {}
    for r in a_rows + b_rows:
        groups.setdefault(r["customer_id"], []).append(r)
    ids, n_a = sorted(groups), len({r["customer_id"] for r in a_rows})
    rng = random.Random(seed)
    hits = 0
    for _ in range(shuffles):
        m = ids[:]
        rng.shuffle(m)
        hits += abs(basket_change([r for c in m[:n_a] for r in groups[c]])
                    - basket_change([r for c in m[n_a:] for r in groups[c]])) >= abs(gap)
    return gap, hits / shuffles


gap_core, p_between = between_test(clean, "Retail-Plus", "Retail-Core")
kit.table(["the question", "the fair test", "p, both directions"], [
    ("did Retail-Plus's revenue per order fall?", "each member's two quarters flipped", f"{p_plus:.4f}"),
    ("did it move differently from Retail-Core's?", "segment label shuffled across whole customers", f"{p_between:.4f}")],
    caption=f"Invented: two questions about one finding; the gap to Retail-Core is {gap_core:+.1f} points")
kit.check("both fair tests put the finding outside what chance usually does", p_plus < 0.05 and p_between < 0.05)
'''),
    mdj("""
    **What happened.** Both fair tests put the invented finding outside what chance usually does: 0.011
    for the fall itself, and 0.0385 for a gap of 14.0 points to Retail-Core, a different question with
    its own fair test.

    **The note, with the right lead, on the invented export.** Claim: booked revenue fell 35.0 percent,
    from Rs 40,00,000 to Rs 26,00,000; Rs 13,88,200 of it is the corporate book, and among consumers
    the branch that moved is Retail-Plus's revenue per order, down 15.0 percent from Rs 3,000 to Rs
    2,550 with its 16 members and their frequency unchanged. Evidence: both quarters reconcile to
    Finance's control totals; with each member's two quarters flipped at random, a change this large in
    either direction came up in 22 of 2,000 worlds, p = 0.011. Caveat: the corporate move rests on five
    orders then two, too few to call a trend. Action: ask the corporate account owner why fewer
    corporate orders came in, and open Retail-Plus's basket (items per order and price per item) before
    any spend.

    **Your turn, on this morning's file.** Test the consumer branch your lab tree says moved on enough
    orders, on its own customers' two quarters, and then against another segment. Put that segment's
    name in `LEAD` and the one you compare it with in `OTHER`, then type these lines into the empty
    cell below and run it:

    ```python
    LEAD, OTHER = "...", "..."
    lab_obs, lab_worlds, lab_p = paired_test(lab_clean, LEAD)
    print(f"{LEAD} revenue per order {lab_obs:+.1f}%, p = {lab_p:.4f} both ways")
    print("gap to", OTHER, "and its p across whole customers:", between_test(lab_clean, LEAD, OTHER))
    ```
    """),
    empty(),
    mdj("""
    ## 5. Is the fall broad, or carried by a few members?

    The flips compare the tier's average. A second route reads each member on their own: of Retail-Plus's
    members, how many saw their own average order fall? If the fall is real and broad, most of them
    should, and a sign test says how often coin flips alone would split the members at least that
    unevenly.
    """),
    code('''
def sign_test(src, seg):
    per = members_of(src, seg)
    fell = sum(1 for v in per.values() if sum(v["Q2"]) / len(v["Q2"]) < sum(v["Q1"]) / len(v["Q1"]))
    rose = sum(1 for v in per.values() if sum(v["Q2"]) / len(v["Q2"]) > sum(v["Q1"]) / len(v["Q1"]))
    moved = fell + rose
    return fell, rose, len(per) - moved, 2 * sum(comb(moved, k) for k in range(min(fell, rose) + 1)) / 2 ** moved


fell, rose, same, sign_p = sign_test(clean, "Retail-Plus")
kit.columns(["own basket fell", "own basket rose", "unchanged"], [("members, invented", [fell, rose, same])],
            lit=(0,), width=560,
            title=f"Invented: Retail-Plus's {fell + rose + same} members, {fell} fell and {rose} rose; sign test p = {sign_p:.3f} either way")
kit.check("most members saw their own basket fall", fell > (fell + rose + same) / 2, f"{fell} of {fell + rose + same}")
kit.check("the sign test puts the split outside what coin flips usually do", sign_p < 0.05, f"p = {sign_p:.3f}")
kit.check("the second route points the same way as the flips", (fell > rose) == (obs_plus < 0))
'''),
    mdj("""
    **What happened.** Of the invented Retail-Plus's 16 members, 13 saw their own average order fall
    and 3 saw it rise. Coin flips split sixteen members at least that unevenly in 2.1 percent of
    worlds, either way, so the sign test agrees with the flips.

    **When to switch routes.** The flips say whether the tier's change is bigger than chance; the
    member count says whether it is broad or carried by a few people. When the two disagree, a handful
    of members moved the average, and the note says so. The sign test uses only the direction of each
    member's change, which is why its p of 0.021 sits above the flips' 0.011.

    **Your turn, on this morning's file.** Run the sign test on your lab lead. Type this line into the
    empty cell below and run it:

    ```python
    print(LEAD, "fell, rose, unchanged and the sign test's p:", sign_test(lab_clean, LEAD))
    ```

    > **Kavya's review.** Say the count before the rate, every time: the orders in each quarter, then
    > the percentage. "Down 36 percent" alone is a headline, and Marketing will take it apart with one
    > question.
    """),
    empty(),
    mdj("""
    ### How would you answer this in an interview?

    **[S] Tell me about an analysis you did: what did you find, and how sure are you?** "On a
    two-quarter export in training, revenue fell 35.0 percent after I reconciled it to Finance's control
    totals. Almost all of it was the corporate book, on seven orders, which I reported as counts and
    passed to the account owner. The finding I led with was one tier's revenue per order, down 15.0
    percent on 64 orders with its members and their frequency flat. The same 16 members were in both
    quarters, so I tested it by flipping each member's two quarters at random: p = 0.011 counting either
    direction, and 13 of the 16 saw their own basket fall. My caveat was the corporate book's count."

    **[D] A stakeholder attacks your caveat in front of the room; how do you hold it without
    overclaiming?** "I restate the claim with its count, bound what the data can say, and offer the test
    that would settle it with its size and time. For the corporate book: seven orders cannot tell a trend
    from an account or two pausing; a call to the account owner settles which it is by Monday."

    **The design question: four segments moved; which do you test?** "One: the branch the tree says
    moved on enough orders to read, tested on its own customers' two quarters. Testing all four at 0.05
    gives about a one-in-five chance that something looks real by luck, and a test on a handful of
    orders cannot say anything a count does not."

    ## Depth: what happens when a test splits a member's two quarters?

    Two tests a hurried analyst reaches for split what belongs together. Pooling the members' Q1 and Q2
    figures and dealing the quarter labels at random treats a member's own two quarters as two
    strangers; shuffling segment labels across single orders splits one customer's orders between the
    groups. Either can move p in either direction. On the invented export both come out larger than the
    fair test's, because members differ in size far more than each member's own quarters differ from
    each other, and a test that splits the pair throws that pairing away. Where a question compares
    groups and a customer's orders are alike, splitting them more often makes p too small, because
    correlated orders count as extra evidence. The cell below runs each fair test beside its hurried
    twin, on the same measure.
    """),
    code('''
def split_tests(src, seg, other, seed=7):
    """Each fair test beside the hurried twin that splits the pair, on one segment and one comparison."""
    per = members_of(src, seg)
    r1 = [sum(v["Q1"]) for v in per.values()]
    r2 = [sum(v["Q2"]) for v in per.values()]
    real = sum(r1) / len(r1) - sum(r2) / len(r2)
    rng = random.Random(seed)
    pool, dealt = r1 + r2, []
    for _ in range(2000):
        rng.shuffle(pool)
        dealt.append(sum(pool[:len(r1)]) / len(r1) - sum(pool[len(r1):]) / len(r2))
    p_pooled = sum(1 for g in dealt if abs(g) >= abs(real) - 1e-9) / 2000
    d = [b - a for a, b in zip(r1, r2)]
    rng = random.Random(seed)
    p_flip = sum(1 for _ in range(2000) if abs(sum(x if rng.random() < 0.5 else -x for x in d)) >= abs(sum(d)) - 1e-9) / 2000
    a_rows = [r for r in src if r["segment"] == seg]
    b_rows = [r for r in src if r["segment"] == other]
    gap, p_whole = between_test(src, seg, other)
    both_rows = a_rows + b_rows
    rng = random.Random(seed)
    ext = 0
    for _ in range(2000):
        idx = list(range(len(both_rows)))
        rng.shuffle(idx)
        ext += abs(basket_change([both_rows[i] for i in idx[:len(a_rows)]])
                   - basket_change([both_rows[i] for i in idx[len(a_rows):]])) >= abs(gap)
    return [("revenue per customer, Q1 to Q2", "each customer's two quarters flipped", "each customer's own pair", f"{p_flip:.4f}"),
            ("revenue per customer, Q1 to Q2", "Q1 and Q2 figures pooled and dealt", "nothing", f"{p_pooled:.4f}"),
            (f"revenue per order, gap to {other}", "segment label across whole customers", "each customer's orders", f"{p_whole:.4f}"),
            (f"revenue per order, gap to {other}", "segment label across single orders", "nothing", f"{ext / 2000:.4f}")]


depth = split_tests(clean, "Retail-Plus", "Retail-Core")
kit.table(["measure", "the test", "what it keeps together", "p, both directions"], depth,
          caption="Invented: each fair test beside the hurried twin that splits the pair")
kit.check("splitting the pairs pushes both verdicts past 0.05 on the invented export",
          float(depth[1][3]) > 0.05 > float(depth[0][3]) and float(depth[3][3]) > 0.05 > float(depth[2][3]))
'''),
    mdj("""
    **What happened.** On the invented export, flipping each member's two quarters puts the fall in
    revenue per member at p = 0.0025, and pooling the same figures and dealing them reads it as chance,
    p = 0.222; shuffling the label across whole customers puts the gap to Retail-Core at 0.0385, and
    shuffling single orders reads it as chance too, 0.0945, so the test that splits the pair reached the
    wrong verdict both times on the same data.

    **Your turn, on this morning's file.** Run the same four tests on your lab lead and the segment you
    compared it with. Type this line into the empty cell below and run it:

    ```python
    kit.table(["measure", "the test", "what it keeps together", "p, both directions"], split_tests(lab_clean, LEAD, OTHER),
              caption="This morning's file: each fair test beside its hurried twin")
    ```

    Which way did the hurried twins move p on this morning's file, and would either have changed the
    verdict?
    """),
    empty(),
    mdj("""
    ### Which number describes a typical order in this file?

    A note that says "the typical order" needs one number, and a file with a few corporate orders among
    the consumer ones pulls its mean far from what most customers spend.
    """),
    code('''
amounts = sorted(r["amount"] for r in clean)
typical = [("mean order, clean", round(statistics.mean(amounts))), ("median order, clean", statistics.median(amounts))]
kit.table(["measure", "value"], [(m, kit.rupees(v)) for m, v in typical], caption="Invented: the typical order")
kit.check("the mean sits more than ten times above the median", typical[0][1] > 10 * typical[1][1],
          f"{kit.rupees(typical[0][1])} against {kit.rupees(typical[1][1])}")
'''),
    mdj("""
    **What happened.** The mean order, Rs 39,521, is pulled up by seven corporate orders and describes no
    order anybody placed; the median, Rs 2,350, is the typical one, and the mean belongs in anything that
    must reconcile.
    """),
    mdj("""
    ## So, which finding leads the note, and how sure can Meera be of it?

    The branch that moved on enough orders to test leads, said beside the biggest move as counts. On
    the invented export:

    1. Business carries Rs 13,88,200 of the Rs 14,00,000 fall, 99.2 percent, with its revenue down 36.3
       percent.
    2. That rate rests on five orders then two, and coin flips split seven orders at least that unevenly
       in 45 percent of worlds.
    3. Count before rate (C) is the best fit: Retail-Plus's revenue per order, down 15.0 percent on 64
       orders, leads among consumers, and D finds the same lead at three times the minutes with a 19
       percent chance of a fluke.
    4. With each member's two quarters flipped, 22 of 2,000 worlds are as extreme either way, p = 0.011
       (0.0107 counted exactly).
    5. 13 of the 16 members saw their own basket fall, a sign test p of 0.021, so the fall is broad.

    Meera can act on it as a finding worth opening, sized at Rs 14,400 a quarter, with the corporate
    book beside it as a question to its account owner. The your-turn cells put this morning's file
    through the same five questions, and Saturday's paper asks for the p-value sentence from memory.
    """),
    code('kit.check_summary()\nprint("Next: the rehearsal, where the note is said aloud and Marketing pushes on it.")'),
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

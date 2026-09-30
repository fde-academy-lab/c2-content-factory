"""Write the afternoon's two case notebooks as TODO twins and executed solutions.

    python3 content/W01/D2/internal/C2_W01_D02_build_cases_INTERNAL.py

A code cell holds [[n|solution]] where a learner picks a lettered option: the TODO twin prints
__TODOn__ there and ships unexecuted, and the solution twin prints the solution and runs cold in its
own folder. A cell wrapped in SOL(...) appears only in the solution twin.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, md, code, build  # noqa: E402

DAY = ROOT / "content" / "W01" / "D2"
SLOT = re.compile(r"\[\[(\d+)\|(.+?)\]\](?!\])", re.S)


# Chart titles that state a finding stay in the solution twin; the exercise twin names only what is drawn.
NEUTRAL = {
    "The delivered fall along the tree: the customers branch moves now": "The delivered bridge, one leaf at a time in the tree's order",
    "The 'lost' delivered customers all ordered again in Q2": "Q1 delivered customers missing from Q2, and what they did in Q2",
    "Delivered revenue per order: here the rate carries more than the mix": "Delivered revenue per order, split into mix and rate",
    "Retail-Plus revenue: half the orders at 7 percent more each": "Retail-Plus revenue, Q1 and Q2",
    "Your set's Q2 orders: every one cancelled or returned": "Your set's Q2 orders, by how each ended",
    "Retail-Plus members by orders in Q1 to orders in Q2": "Retail-Plus members, by orders in Q1 and in Q2",
}


NEUTRAL_MD = {
    "This case climbs the same ladder alone, on a harder definition, where one\nbranch that held in the morning moves.":
        "This case climbs the same ladder alone, on a harder definition.",
    "Change the definition and rerun every rung. If a branch that held starts to move, find out what it\n> is made of before anyone else names it.":
        "Change the definition and rerun every rung; say what moved and what you\n> would check next.",
}


class SOL:
    def __init__(self, cell):
        self.cell = cell


def twin(cells, solution):
    out = []
    for c in cells:
        if isinstance(c, SOL):
            if solution:
                out.append(c.cell)
            continue
        if c.cell_type == "code":
            src = SLOT.sub((lambda m: m.group(2)) if solution else (lambda m: f"__TODO{m.group(1)}__"), c.source)
            if not solution:
                src = re.sub(r'\nprint\("Answer string[^\n]*', "", src)
                for claim, plain in NEUTRAL.items():
                    src = src.replace(claim, plain)
            c = code(src)
        elif c.cell_type == "markdown" and not solution:
            c = md(re.sub(r"This is the solution twin:.*?options fail\.",
                          "This is the exercise twin: each placeholder is a lettered choice in the comment above it. "
                          "Run it from the top; it stops at the first placeholder you have not filled, which is intended.",
                          c.source, flags=re.S))
            for claim, plain in NEUTRAL_MD.items():
                c = md(c.source.replace(claim, plain))
            c = md(re.sub(r"\*\*Item (\d) in your brief\.?\*\*.*?(?=\n\n|$)",
                          lambda m: f"**Item {m.group(1)} in your brief** goes in now, from what this part printed.",
                          c.source, flags=re.S))
        out.append(c)
    return out


TOOLS = '''

def tree_for(rows):
    """The revenue tree's leaves for any list of orders, returned as a dictionary (chapter 3)."""
    revenue = 0
    seen = {}
    for order in rows:
        revenue += order["amount"]
        seen[order["customer_id"]] = True
    orders = len(rows)
    customers = len(seen)
    return {"revenue": revenue, "orders": orders, "customers": customers,
            "orders_per_customer": orders / customers if customers else 0,
            "revenue_per_order": revenue / orders if orders else 0}


def pct_change(before, after):
    """Chapter 5's fixed helper: the change every time, in the same type."""
    return round(100 * (after - before) / before, 1)
'''


# --------------------------------------------------------------------------------------------- ex1
def escalated(solution):
    cells = [
        md("""
# Escalated case: the ladder again, on the orders that reached customers

**Week 1, Tuesday afternoon. The escalated case, unguided, fifty minutes.** The morning climbed six
chapters on booked orders. This case climbs the same ladder alone, on a harder definition, where one
branch that held in the morning moves.

The board pack is the set of numbers Kalpa's board reads every quarter.

> **The client asks.** "The board pack reports revenue on orders that reached the customer and
> stayed there. Monday you taught me that cancelled orders are not sales. Does your story survive on
> delivered orders? Which branch, which segment, and what would you bet on?"
>
> Meera Raghavan, CEO, Kalpa Retail

> **Kavya's review of the morning.** "Every number you gave Meera this morning was on booked orders.
> Change the definition and rerun every rung. If a branch that held starts to move, find out what it
> is made of before anyone else names it."

This is the solution twin: every placeholder is filled, every cell has run, and under each step a
line says why the other three options fail.
"""),
        code(SETUP + 'ORDERS = kit.load_records("C2_W01_D02_orders_STUDENT.py")\nSEGMENTS = ["Retail-Core", "Retail-Plus", "Business", "Student"]\n' + TOOLS + '\nprint(len(ORDERS), "booked orders loaded")'),
        code("""
kit.side_by_side(
    kit.ladder(["Is the delivered drop real?", "The tree on delivered", "Are those lost customers?",
                "Four segments on delivered", "Mix or rate on delivered"], show=False),
    kit.flow(["booked\\n200 orders", "delivered only", "the same ladder", "the sentence"], lit=1, show=False),
)"""),
        md("""
## Part 1. Is the delivered drop real?

Keep only the orders that reached the customer and stayed, then compare the two closed quarters.
"""),
        code('''
delivered = []
for order in ORDERS:
    # TODO 1. Which condition keeps the orders that reached the customer and stayed there?
    #   a) order["status"] != "cancelled"
    #   b) order["status"] == "delivered"
    #   c) order["status"] in ("delivered", "returned")
    #   d) order["amount"] > 0
    if [[1|order["status"] == "delivered"]]:
        delivered.append(order)
dq = {q: [o for o in delivered if o["quarter"] == q] for q in ("Q1", "Q2")}
d1, d2 = tree_for(dq["Q1"]), tree_for(dq["Q2"])
d_change = pct_change(d1["revenue"], d2["revenue"])
kit.columns(["booked", "delivered"], [("Q1", [21000000, d1["revenue"]]), ("Q2", [18700000, d2["revenue"]])],
            fmt=lambda v: f"Rs {v / 1e7:.2f} cr", title="Revenue by quarter on both definitions")
kit.check("138 of the 200 orders were delivered", len(delivered) == 138, f"{len(delivered)}")
by_month = {}
for o in delivered:
    by_month[o["order_date"][:7]] = by_month.get(o["order_date"][:7], 0) + o["amount"]
q1_months = sum(v for m, v in by_month.items() if m <= "2026-06")
kit.check("the delivered change matches a second route by month", d_change == pct_change(q1_months, sum(by_month.values()) - q1_months), f"{d_change}")
'''),
        SOL(md("""
**Why the other three fail.** a) keeps returned orders, which reached the customer and came back.
c) keeps them on purpose. d) keeps every order, since every amount is positive, which is the booked
file again.
""")),
        md("""
**Item 1 in your brief** asks which figure answers Meera. The fall on delivered orders is
Rs 16,40,290, 11.3 percent, on two closed quarters of thirteen weeks: the drop survives the
definition.

## Part 2. The tree on delivered orders

Put rupees on each branch with the bridge in the tree's order: customers first, then orders per
customer, then revenue per order.
"""),
        code('''
c1, f1, v1 = d1["customers"], d1["orders_per_customer"], d1["revenue_per_order"]
c2, f2, v2 = d2["customers"], d2["orders_per_customer"], d2["revenue_per_order"]
# TODO 2. Which expression is the customers step of the bridge?
#   a) (c2 - c1) * f1 * v1
#   b) c2 * (f2 - f1) * v1
#   c) (c2 - c1) * f2 * v2
#   d) (c2 - c1) / c1
move_customers = [[2|(c2 - c1) * f1 * v1]]
move_frequency = c2 * (f2 - f1) * v1
move_value = c2 * f2 * (v2 - v1)
kit.bridge(("Q1 delivered", d1["revenue"]), [("customers", round(move_customers)), ("orders per customer", round(move_frequency)),
           ("revenue per order", round(move_value))], end_label="Q2 delivered", lit=[0],
           title="The delivered fall along the tree: the customers branch moves now")
kit.check("the bridge lands on Q2 delivered revenue", abs(d1["revenue"] + move_customers + move_frequency + move_value - d2["revenue"]) < 1)
kit.check("the delivered customer counts match the file", (c1, c2) == (54, 50), f"{c1} and {c2}")
'''),
        SOL(md("""
**Why the other three fail.** b) is the frequency step. c) prices the lost customers at Q2's leaves,
which charges them for the overlap and breaks the order the bridge promised. d) is a rate, which does
not add along a bridge in rupees.
""")),
        md("""
**Item 2 in your brief.** On delivered orders the customers branch takes Rs 10,74,442, frequency
Rs 32,23,327, and revenue per order gives back Rs 26,57,479. Marketing will read the first number as
lost customers. Part 3 finds out what it is.

## Part 3. Are those lost customers?

Four fewer customers had a delivered order in Q2. The morning showed all 69 customers booked in both
quarters. Compare the two views.
"""),
        code('''
booked_ids = {q: {o["customer_id"] for o in ORDERS if o["quarter"] == q} for q in ("Q1", "Q2")}
deliv_ids = {q: {o["customer_id"] for o in dq[q]} for q in ("Q1", "Q2")}
# TODO 3. Marketing will call the customers who dropped out of the delivered count lost. Which set holds
# the ones among them who still placed an order in Q2?
#   a) deliv_ids["Q1"] & booked_ids["Q2"]
#   b) booked_ids["Q1"] - booked_ids["Q2"]
#   c) (deliv_ids["Q1"] - deliv_ids["Q2"]) & booked_ids["Q2"]
#   d) deliv_ids["Q2"] - deliv_ids["Q1"]
still_booked = [[3|(deliv_ids["Q1"] - deliv_ids["Q2"]) & booked_ids["Q2"]]]
print(len(still_booked), "customers in your set")
'''),
        code('''
their_q2 = {}
for o in ORDERS:
    if o["quarter"] == "Q2" and o["customer_id"] in still_booked:
        their_q2[o["status"]] = their_q2.get(o["status"], 0) + 1
kit.bars([(status, n) for status, n in sorted(their_q2.items())] + [("lost on booked orders", len(booked_ids["Q1"] - booked_ids["Q2"]))],
         title="Your set's Q2 orders: every one cancelled or returned")
kit.table(["Their Q2 orders ended as", "Orders"], sorted(their_q2.items()), caption="What happened to your set's Q2 orders")
kit.check("your set placed orders in Q2", sum(their_q2.values()) > 0, f"{sum(their_q2.values())} orders")
kit.check("none of your set's Q2 orders counts as delivered", their_q2.get("delivered", 0) == 0)
'''),
        SOL(md("""
**Why the other three fail.** a) is every delivered Q1 customer who booked in Q2, 54 people, including those whose Q2 orders were delivered. b) is the booked
churn, which is empty. d) is the customers delivered in Q2 and not Q1, the other side of the
overlap.
""")),
        md("""
**Item 3 in your brief.** The customers branch on delivered orders is cancellations and returns rather than acquisition:
the 19 customers who "disappeared" all ordered in Q2, and their orders were cancelled or returned.
Split by reason, those orders go to the teams that own fulfilment, getting orders to customers
intact, and the product, and the Rs 12 crore still has nothing to replace.

## Part 4. Four segments on delivered orders

Run `tree_for` per segment on delivered orders, roll the rate up to the company, and count the groups
that come back.
"""),
        code('''
seg1 = {s: tree_for([o for o in dq["Q1"] if o["segment"] == s]) for s in SEGMENTS}
seg2 = {s: tree_for([o for o in dq["Q2"] if o["segment"] == s]) for s in SEGMENTS}
averaged = {q: sum(t["orders_per_customer"] for t in seg.values()) / 4 for q, seg in (("Q1", seg1), ("Q2", seg2))}
# TODO 4. Which roll-up gives the company's delivered orders per customer from the segments?
#   a) sum(t["orders_per_customer"] for t in seg.values()) / 4
#   b) sum(t["customers"] for t in seg.values()) / sum(t["orders"] for t in seg.values())
#   c) sorted(t["orders_per_customer"] for t in seg.values())[2]
#   d) sum(t["orders"] for t in seg.values()) / sum(t["customers"] for t in seg.values())
def roll_up(seg):
    return [[4|sum(t["orders"] for t in seg.values()) / sum(t["customers"] for t in seg.values())]]
weighted = {"Q1": roll_up(seg1), "Q2": roll_up(seg2)}
changes = {s: pct_change(seg1[s]["orders_per_customer"], seg2[s]["orders_per_customer"]) for s in SEGMENTS}
kit.columns(SEGMENTS, [("Q1", [round(seg1[s]["orders_per_customer"], 2) for s in SEGMENTS]),
                       ("Q2", [round(seg2[s]["orders_per_customer"], 2) for s in SEGMENTS])],
            fmt=lambda v: f"{v:.2f}", title="Delivered orders per customer by segment")
kit.check("the roll-up reproduces the company figure", abs(weighted["Q1"] - d1["orders_per_customer"]) < 1e-9 and abs(weighted["Q2"] - d2["orders_per_customer"]) < 1e-9)
kit.check("averaging the averages gives a different figure", pct_change(averaged["Q1"], averaged["Q2"]) != pct_change(d1["orders_per_customer"], d2["orders_per_customer"]))
# TODO 5. Which test proves that no segment came back without a number?
#   a) None not in summary.values() and len(summary) == 4
#   b) min(summary.values()) < 0 and len(summary) > 0
#   c) "Business" in summary and len(summary) == 4
#   d) len(summary) == 4 and "Retail-Core" in summary
def all_numbers(summary):
    return [[5|None not in summary.values() and len(summary) == 4]]


broken = {"Retail-Core": -5.3, "Retail-Plus": None, "Business": -15.0, "Student": None}   # invented, last quarter's shape
try:
    catches = all_numbers(broken) is False
except TypeError:
    catches = False
kit.check("the test passes on today's four changes", all_numbers(changes) is True)
kit.check("the test fails on the invented broken summary", catches)
kit.check("every segment has its change on delivered orders", len(changes) == 4)
'''),
        SOL(md("""
**Why the other three fail.** TODO 4: a) is the average of averages, minus 9.2 percent against the
true minus 24.0. b) is the reciprocal, customers per order. c) ignores every segment's size. TODO 5:
b) raises a TypeError on a None instead of reporting it. c) and d) look for one segment by name and pass on the broken summary.
""")),
        md("""
**Item 4 in your brief.** On delivered orders Retail-Plus falls furthest again, 1.85 to 1.06 orders
per member, minus 42.6 percent; Business and Retail-Core fall about 11.5 percent each; Student rises.
The segment survives the definition.

## Part 5. Mix or rate, on delivered orders

Delivered revenue per order rose 26.0 percent. Split it the way chapter 4 did: price Q2's mix at Q1's
segment rates.
"""),
        code('''
share1 = {s: seg1[s]["orders"] / d1["orders"] for s in SEGMENTS}
share2 = {s: seg2[s]["orders"] / d2["orders"] for s in SEGMENTS}
at_q2_mix = 0
for s in SEGMENTS:
    # TODO 6. What adds up to revenue per order at Q2's mix and Q1's segment rates?
    #   a) share1[s] * seg2[s]["revenue_per_order"]
    #   b) share2[s] * seg1[s]["revenue_per_order"]
    #   c) share2[s] * seg2[s]["revenue_per_order"]
    #   d) (seg1[s]["revenue_per_order"] + seg2[s]["revenue_per_order"]) / 2
    at_q2_mix += [[6|share2[s] * seg1[s]["revenue_per_order"]]]
mix, rate = at_q2_mix - v1, v2 - at_q2_mix
kit.bridge(("Q1 revenue per order", round(v1)), [("mix", round(mix)), ("rate inside segments", round(rate))],
           end_label="Q2 revenue per order", lo=150000, fmt=kit.rupees, lit=[1],
           title="Delivered revenue per order: here the rate carries more than the mix")
kit.check("mix and rate add back to the whole rise", abs(mix + rate - (v2 - v1)) < 1e-6)
kit.check("on delivered orders the mix explains 44 percent", round(mix / (v2 - v1) * 100) == 44, f"{mix / (v2 - v1) * 100:.1f}")
'''),
        SOL(md("""
**Why the other three fail.** a) prices Q1's mix at Q2's rates, which measures the rate part. c) is
Q2's actual revenue per order. d) averages two rates and weights no segment, the average of averages
again.
""")),
        md("""
**Item 5 in your brief.** On booked orders the mix explained 69 percent of the rise; on delivered
orders 44 percent, because Business's delivered orders grew in size, from Rs 10,24,651 to
Rs 11,60,405 each on average. The consumer segments still paid about the same. The definition moved
the split; it did not create a price signal in the consumer business.

## The sentence
"""),
        code('''
# TODO 7. Which segment leads the sentence as the behaviour finding on delivered orders?
#   a) "Business"
#   b) "Student"
#   c) "all four segments"
#   d) "Retail-Plus"
lead = [[7|"Retail-Plus"]]
kit.check("your lead matches a second route over the segment changes", lead in changes and lead == min(changes, key=changes.get))
kit.flow([f"drop real\\n{d_change}% delivered", f"branch\\nfrequency {kit.rupees(round(move_frequency))}",
          f"customers branch\\n{len(still_booked)} still booked", f"segment\\n{lead} {changes.get(lead, '?')}%", "two hypotheses\\nand their evidence"],
         kinds=["known", "bad", "unknown", "bad", "known"], title="The sentence to Meera, on delivered orders")
'''),
        SOL(md("""
**Why the other three fail.** a) is the rupee finding on three lumpy orders. b) rose. c) spreads a
fall that sits in one segment across four.

**The sentence.** "On delivered orders the story holds: revenue fell 11.3 percent between closed
quarters, and frequency carries the most rupees, Rs 32,23,327. Four fewer customers had a delivered
order, but all 19 who dropped out of the delivered count booked again in Q2 and saw their orders
cancelled or returned, so that branch is cancellations and returns, to be split by reason, and not acquisition. Retail-Plus members
ordered 42.6 percent less often. The two hypotheses stand as this morning: the reorder button after
25 August, settled by the app's logs, and a change for members in July, settled by the tier's change
log."

### In the interview

**[D] You change the definition of revenue and a branch that held starts to move; what do you do?**
"I decompose the new movement before anyone names it. Here customers with a delivered order fell from
54 to 50, which looks like churn, but every one of the 19 who left the delivered count booked again
and had orders cancelled or returned. So the branch is cancellations and returns, which I would split by reason. I show both definitions side by
side and say which owner each branch goes to." The interviewer is listening for the definition named
and the moved branch explained.
""")),
        code("""
kit.check_summary()
print("Answer string for the TODOs: b a c d a b d.")"""),
    ]
    return twin(cells, solution)


# --------------------------------------------------------------------------------------------- ex2
def second(solution):
    cells = [
        md("""
# Second case: the tier's question and Marketing's pushback, argued from the same numbers

**Week 1, Tuesday afternoon. The second case, in pairs, forty minutes.** One of you answers Marketing,
the other answers the head of Retail-Plus, from the same file, and together you write the reply.

> **Marketing comes back with a new deck.** "Retail-Plus members spend 7 percent more every time they
> order, so the tier is healthy and the answer is still acquisition. And Retail-Plus web orders fell
> hardest, 24 to 9, so this is the website team's problem, not the tier's and not the app's."
>
> The marketing lead, Kalpa Retail

> **The tier asks.** "Fine. Which of my members do I call first?"
>
> The head of Retail-Plus

> **Kavya's review of the escalated case.** "You found a branch that moved for a reason nobody
> guessed. Do the same with Marketing's two new numbers: find what each is made of before you agree
> or disagree."

This is the solution twin: every placeholder is filled, every cell has run, and under each step a
line says why the other three options fail.
"""),
        code(SETUP + 'ORDERS = kit.load_records("C2_W01_D02_orders_STUDENT.py")\nSEGMENTS = ["Retail-Core", "Retail-Plus", "Business", "Student"]\n' + TOOLS + '\nprint(len(ORDERS), "orders loaded")'),
        code("""
kit.side_by_side(
    kit.ladder(["7 percent more per order: a healthy tier?", "Web fell hardest: the website?",
                "Who to call first", "The reply and the evidence"], show=False),
    kit.matrix(["Marketing", "the head of Retail-Plus"], ["claim", "test"],
               [["a healthy tier; the website", "the tier's own tree; web in another segment"], ["which members", "orders per member, Q1 to Q2"]],
               show=False),
)"""),
        md("""
## Part 1. "Members spend 7 percent more per order, so the tier is healthy"

Revenue per order is one leaf of the tree. Build the tier's tree for both quarters, then put the
leaves back together into the tier's revenue.
"""),
        code('''
plus = {q: [o for o in ORDERS if o["segment"] == "Retail-Plus" and o["quarter"] == q] for q in ("Q1", "Q2")}
t1, t2 = tree_for(plus["Q1"]), tree_for(plus["Q2"])
ratio = {leaf: t2[leaf] / t1[leaf] for leaf in ("customers", "orders_per_customer", "revenue_per_order")}
kit.table(["Leaf", "Q1", "Q2", "Q2 over Q1"],
          [("members", t1["customers"], t2["customers"], f'{ratio["customers"]:.3f}'),
           ("orders per member", f'{t1["orders_per_customer"]:.2f}', f'{t2["orders_per_customer"]:.2f}', f'{ratio["orders_per_customer"]:.3f}'),
           ("revenue per order", kit.rupees(round(t1["revenue_per_order"])), kit.rupees(round(t2["revenue_per_order"])),
            f'{ratio["revenue_per_order"]:.3f}')],
          caption="Retail-Plus, leaf by leaf")
# TODO 1. Which expression gives the tier's Q2 revenue as a share of its Q1 revenue, from the leaves?
#   a) ratio["customers"] * ratio["orders_per_customer"] * ratio["revenue_per_order"]
#   b) ratio["orders_per_customer"] + ratio["revenue_per_order"] - 1
#   c) ratio["revenue_per_order"]
#   d) (ratio["orders_per_customer"] + ratio["revenue_per_order"]) / 2
tier_share = [[1|ratio["customers"] * ratio["orders_per_customer"] * ratio["revenue_per_order"]]]
kit.columns(["Q1", "Q2, from your expression"], [("tier revenue", [t1["revenue"], round(t1["revenue"] * tier_share)])],
            fmt=kit.rupees, width=520, title="Retail-Plus revenue: half the orders at 7 percent more each")
'''),
        code('''
kit.check("your expression gives back the tier's Q2 revenue, counted order by order",
          abs(t1["revenue"] * tier_share - t2["revenue"]) < 1, kit.rupees(round(t1["revenue"] * tier_share)))
'''),
        SOL(md("""
**Why the other three fail.** b) adds two changes, minus 49.0 and plus 7.0 percent, as if percentages
added, which is Monday's two lifts called 20 percent turned round. c) is the one leaf Marketing
quoted. d) averages two ratios, which is no quantity in the tree.

**The answer to Marketing.** The same 22 members spent 7.0 percent more per order and placed about
half as many orders, 2.32 each to 1.18, so the tier's revenue fell to 0.546 of Q1, Rs 1,43,550 to
Rs 78,300, about 45 percent down. One leaf that rose inside a tier whose orders halved says nothing
about the tier's health.
""")),
        md("""
**Item 1 in your brief** goes in now, from what this part printed.

## Part 2. "Retail-Plus web orders fell hardest, so it is the website"

A broken website hurts every customer who uses it. If the website were the cause, what would another
segment's web orders show?
"""),
        code('''
web = {(o["segment"], o["quarter"]): 0 for o in ORDERS}
for o in ORDERS:
    if o["channel"] == "web":
        web[(o["segment"], o["quarter"])] += 1
# TODO 2. If the website were broken for everyone, which other segment's web orders would also have fallen hard?
#   a) "Retail-Plus"
#   b) "Student"
#   c) "Retail-Core"
#   d) "none"
also_falls = [[2|"Retail-Core"]]
picked = also_falls if also_falls in SEGMENTS else "Retail-Plus"
kit.columns(["Retail-Plus", picked], [("Q1 web orders", [web[("Retail-Plus", "Q1")], web[(picked, "Q1")]]),
                                      ("Q2 web orders", [web[("Retail-Plus", "Q2")], web[(picked, "Q2")]])],
            width=560, title="Web orders: the members against the segment you chose")
'''),
        code('''
comparison = (web[(also_falls, "Q1")], web[(also_falls, "Q2")]) if also_falls in SEGMENTS else (0, 0)
kit.check("the segment you drew is not the members, and had enough web orders in Q1 to show a fall",
          also_falls != "Retail-Plus" and comparison[0] >= 10, f"{comparison[0]} and {comparison[1]}")
kit.check("Retail-Plus web orders fell 24 to 9", (web[("Retail-Plus", "Q1")], web[("Retail-Plus", "Q2")]) == (24, 9))
'''),
        SOL(md("""
**Why the other three fail.** a) is the pattern Marketing already saw; it cannot tell a website fault
from anything else that hits members. b) Student placed one web order in Q1, so it has no fall to
show either way. d) a website fault shows on the website.

**The answer to Marketing.** Retail-Core's web orders held at 13 and 12 on the same website, so a
site-wide fault does not fit. Something hit members, on every channel: chapter 6 showed the store and
the app fell too.
""")),
        md("""
**Item 2 in your brief** goes in now, from what this part printed.

## Part 3. "Which of my members do I call first?"

Count each member's orders in Q1 and Q2, and decide who goes first.
"""),
        code('''
per = {q: {} for q in ("Q1", "Q2")}
for o in ORDERS:
    if o["segment"] == "Retail-Plus":
        per[o["quarter"]][o["customer_id"]] = per[o["quarter"]].get(o["customer_id"], 0) + 1
pairs = {}
for cid in per["Q1"]:
    key = (per["Q1"][cid], per["Q2"].get(cid, 0))
    pairs[key] = pairs.get(key, 0) + 1
call_first = []
for cid in per["Q1"]:
    q1n, q2n = per["Q1"][cid], per["Q2"].get(cid, 0)
    # TODO 3. Which members go to the top of the call list?
    #   a) q2n == 0
    #   b) q1n - q2n >= 2
    #   c) q2n > q1n
    #   d) q1n == 1
    if [[3|q1n - q2n >= 2]]:
        call_first.append(cid)
labels = [f"{a} to {b}" for a, b in sorted(pairs, reverse=True)]
kit.bars([(l, pairs[k]) for l, k in zip(labels, sorted(pairs, reverse=True))],
         title="Retail-Plus members by orders in Q1 to orders in Q2")
'''),
        code('''
lost_by_list = sum(per["Q1"][c] - per["Q2"].get(c, 0) for c in call_first)
lost_by_tier = sum(per["Q1"].values()) - sum(per["Q2"].values())
kit.check("the members on your list carry more than half of the tier's lost orders", 2 * lost_by_list > lost_by_tier,
          f"{lost_by_list} of {lost_by_tier}")
kit.check("the per-member counts add back to the tier's orders", sum(per["Q1"].values()) + sum(per["Q2"].values()) == sum(1 for o in ORDERS if o["segment"] == "Retail-Plus"))
'''),
        SOL(md("""
**Why the other three fail.** a) selects nobody, since every member ordered in Q2. c) selects the
members who grew, and there are none. d) selects the members who ordered once in Q1, the ones with
least to lose.

**The answer to the head of Retail-Plus.** Seven members went from three orders a quarter to one;
call them first, and ask each whether they tried to reorder and what happened. Eleven more fell by
one order. Nobody stopped altogether, which fits a habit that broke more than a tier people left.
""")),
        md("""
**Item 3 in your brief** goes in now, from what this part printed.

## Part 4. The reply, and the one request that tests the most

Item 4 in your brief goes in once this part has run.
"""),
        code('''
EVIDENCE = {
    "campaigns": "Marketing's new-member sign-ups by month from July",
    "export": "this export again, cut by city, channel and week from July",
    "app_logs": "the app's reorder logs by week since the 25 August release",
    "tier_log": "the tier's July change log, renewals and support tickets",
}
# TODO 4. The tier lost 25 orders and chapter 6 capped the button at about 4 of them. Which request goes first?
#   a) "campaigns"
#   b) "export"
#   c) "app_logs"
#   d) "tier_log"
first_request = [[4|"tier_log"]]
kit.tree({"label": "the reply", "kind": "lit", "branches": [
    ("to Marketing", {"label": f"tier revenue x {tier_share:.2f}\\nweb tested on {also_falls}", "kind": "known"}),
    ("to the tier", {"label": f"call the {len(call_first)}\\nat the top of the list", "kind": "known"}),
    ("first request", {"label": EVIDENCE[first_request][:34], "kind": "unknown"})]},
    title="The pair's reply, in three branches")
import hashlib
kit.check("your pick matches the key, stored as a fingerprint", hashlib.sha256(first_request.encode()).hexdigest()[:10] == "a49850fe17")
kit.check("your pick names one of the four sources", first_request in EVIDENCE)
'''),
        SOL(md("""
**Why the other three fail.** a) measures acquisition, which chapter 5's overlap ruled out. b) is
the data that raised the question. c) settles the button, which chapter 6 capped at about 4 of the
25 lost orders, the smaller part.

**The pair's reply.** "To Marketing: the tier's members did spend 7 percent more per order, but the
same 22 members placed about half as many orders, so the tier's revenue fell about 45 percent; and
Retail-Core's web orders held at 13 and 12 on the same website, so a site-wide fault does not fit. To the head of Retail-Plus: call the seven members
who went from three orders to one first, and ask what changed for them in July. We are asking for the
tier's July change log, renewals and support tickets first, and the app's reorder logs second."

### In the interview

**[F] A stakeholder says customers spend more per order, so the business is healthy; what do you
check?** "What that rate multiplies with: how many customers there are and how often they buy.
Revenue per order is one leaf of the tree. Here the tier's members spent 7 percent more per order and
ordered about half as often, so the tier's revenue fell about 45 percent. I put the leaves back
together before I agree that anything is healthy." The interviewer is listening for the tree and the
product of its leaves.
""")),
        code("""
kit.check_summary()
print("Answer string for the TODOs: a c b d.")"""),
    ]
    return twin(cells, solution)


if __name__ == "__main__":
    build(DAY / "notebooks" / "C2_W01_D02_ex1_escalated_case_STUDENT.ipynb", escalated(False), execute=False)
    build(DAY / "exercises" / "solutions" / "C2_W01_D02_ex1_escalated_case_solution_STUDENT.ipynb", escalated(True))
    build(DAY / "notebooks" / "C2_W01_D02_ex2_second_case_STUDENT.ipynb", second(False), execute=False)
    build(DAY / "exercises" / "solutions" / "C2_W01_D02_ex2_second_case_solution_STUDENT.ipynb", second(True))
    print("built both cases, each as a TODO twin and an executed solution")

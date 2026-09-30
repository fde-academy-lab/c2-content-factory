"""Write and execute the six chapter notebooks of Week 1 Thursday.

Run from the repository root:

    python3 content/W01/D4/internal/C2_W01_D04_build_notebooks_INTERNAL.py          # all six
    python3 content/W01/D4/internal/C2_W01_D04_build_notebooks_INTERNAL.py 3 4      # some

Each notebook is assembled by scripts/nb_make.py and executed cold in its own folder, so the saved
outputs are the ones a learner's Codespace produces. Each one carries forward the helpers of the
notebook before it and adds one, which is how the toolkit grows across the day.

The Retail-Plus comparison sets the same 22 members' Q1 spend against their own Q2 spend, so the
day's chance reference flips each member's own two quarters (flip_gaps). The label shuffle that
deals every total into two piles (shuffle_gaps) stays for groups of different customers: chapter
6's segments, practice lab problem 3 and the take-home.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, build, code, empty, md  # noqa: E402

OUT = ROOT / "content" / "W01" / "D4" / "notebooks"
CHAPTERS = ["Real, or the usual wobble", "Real, and worth acting on", "The count behind 40 percent",
            "The discount, split by segment", "The note that may say not yet",
            "The fair comparison"]

# --------------------------------------------------------------------------- the toolkit, by chapter
T1 = '''
import itertools
import random
import statistics

ORDERS = kit.load_csv("C2_W01_D04_orders_STUDENT.csv")
SEGMENTS = ["Retail-Core", "Retail-Plus", "Student", "Business"]


def mean(values):
    return sum(values) / len(values)


def member_totals(segment, quarter):
    """Delivered revenue per member of one segment in one quarter, members always in the same order."""
    members = sorted({o["customer_id"] for o in ORDERS if o["segment"] == segment})
    totals = {m: 0 for m in members}
    for o in ORDERS:
        if o["segment"] == segment and o["quarter"] == quarter and o["status"] == "delivered":
            totals[o["customer_id"]] += int(o["amount"])
    return [totals[m] for m in members]


def flip_gaps(q1, q2, times, seed):
    """The same members measured twice: a coin per member decides which of its two quarters is Q1."""
    random.seed(seed)                              # the same coins on every laptop
    diffs = [a - b for a, b in zip(q1, q2)]        # each member's own Q1 less Q2
    gaps = []
    for _ in range(times):
        flipped = [d if random.random() < 0.5 else -d for d in diffs]   # heads keeps, tails swaps
        gaps.append(mean(flipped))
    return gaps


def shuffle_gaps(q1, q2, times, seed):
    """Two groups of different customers: deal every value to two piles at random, many times."""
    random.seed(seed)
    pool = q1 + q2                                 # all the values, labels ignored
    gaps = []
    for _ in range(times):
        random.shuffle(pool)                       # deal at random
        gaps.append(mean(pool[:len(q1)]) - mean(pool[len(q1):]))
    return gaps


def share_at_least(gaps, real):
    """Counting one direction: the share of chance-only worlds with a gap at least as large as the real one."""
    return sum(1 for g in gaps if g >= real) / len(gaps)


def share_either(gaps, real):
    """Counting either direction: the share of chance-only worlds with a gap that large, up or down."""
    return sum(1 for g in gaps if abs(g) >= abs(real)) / len(gaps)
'''

T2 = '''

def delivered(segment, quarter):
    """A segment's delivered revenue in one quarter, in rupees."""
    return sum(int(o["amount"]) for o in ORDERS
               if o["segment"] == segment and o["quarter"] == quarter and o["status"] == "delivered")


def bootstrap_gaps(q1, q2, times, seed):
    """The same members twice: redraw the members' own Q1 less Q2 differences with replacement."""
    random.seed(seed)
    diffs = [a - b for a, b in zip(q1, q2)]
    return [mean([random.choice(diffs) for _ in diffs]) for _ in range(times)]
'''

T3 = '''

def orders_in(segment, quarter):
    return sum(1 for o in ORDERS if o["segment"] == segment and o["quarter"] == quarter)


def flip_rises(n_orders, times, seed):
    """Deal each of n orders to Q1 or Q2 by a fair coin, many times, and keep each rise."""
    random.seed(seed)
    rises = []
    for _ in range(times):
        q2 = sum(1 for _ in range(n_orders) if random.random() < 0.5)
        q1 = n_orders - q2
        rises.append(float("inf") if q1 == 0 else q2 / q1 - 1)
    return rises
'''

T4 = '''

EXPOSURE = kit.load_csv("C2_W01_D04_exposure_STUDENT.csv")
CAMPAIGNS = kit.load_csv("C2_W01_D04_campaigns_STUDENT.csv")


def spend(rows):
    """August spend per customer across a list of exposure rows."""
    return mean([int(r["august_revenue"]) for r in rows])


def group(flag, segment=None):
    """The exposure rows for one group, exposed "yes" or "no", optionally inside one segment."""
    return [r for r in EXPOSURE if r["exposed"] == flag and (segment is None or r["segment"] == segment)]
'''

T6 = '''

def month_delivered(segment, month):
    """A segment's delivered revenue in one calendar month, month as "2026-08"."""
    return sum(int(o["amount"]) for o in ORDERS if o["segment"] == segment
               and o["order_date"][:7] == month and o["status"] == "delivered")


def month_orders(segment, month):
    return [o for o in ORDERS if o["segment"] == segment and o["order_date"][:7] == month
            and o["status"] == "delivered"]
'''


def setup(*parts, extra=""):
    return code(SETUP + "".join(parts) + extra)


def the_map(lit, levels):
    steps = ", ".join(repr(s) for s in levels)
    return code(f'''
kit.side_by_side(
    kit.ladder({CHAPTERS!r}, lit={lit}, show=False),
    kit.vflow([{steps}], show=False),
)
''')


# =========================================================================== chapter 1
def chapter1():
    return [
        md('''
# Real, or the usual wobble?

**Week 1, Thursday. Chapter 1 of 6.** By the end of this notebook you can test a fall in the same
members' spend by flipping each member's own two quarters, read the share in both directions,
choose between four ways of asking "is it real?", and reach the same reading a second way.

> **The client asks.** "Retail-Plus is down, smaller than first reported. Real, or the wobble we see
> every quarter?"
>
> Meera Raghavan, CEO, Kalpa Retail

**The metric at stake.** Delivered revenue per Retail-Plus member per quarter. Retail-Plus is
Kalpa's membership tier, the customers who buy most often (the domain dossier,
`content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`, tells its story). **Who asks and
what rides on it.** Meera, before Monday's growth review: a real fall opens a retention budget for
the tier, and a wobble read as real spends that budget chasing noise. **Who else faces it.**
Booking.com runs about 25,000 tests a year and, by the account of the Harvard researcher who
studied it, about nine in ten of its experiments improve nothing, so every change there is read
against what chance alone produces before anyone acts (the sources are in the study notes).

Wednesday reconciled the quarters with Finance and left Retail-Plus standing, but smaller. The file
holds the same 22 Retail-Plus members in both quarters, so this chapter asks whether their fall is
bigger than chance makes on its own when each member is compared with themselves.
'''),
        md('''
**Setup.** Find the helper and load the cleaned two quarters. Five helpers start the day's
toolkit: `member_totals` turns orders into one number per member, always in the same member order;
`flip_gaps` keeps each member's two quarters together and tosses a coin per member to decide which
quarter is which; `shuffle_gaps` deals the values of two groups of different customers into two
piles; and `share_at_least` and `share_either` count the chance-only worlds that match the real
gap, in one direction or in both. Every later chapter carries these forward and adds its own.
'''),
        setup(T1, extra='''
print(len(ORDERS), "orders,", len({o["customer_id"] for o in ORDERS}), "customers, two quarters")
'''),
        the_map(0, ["the options\\nfour ways to ask 'is it real?'",
                    "1. five members, two cards each\\na gap of Rs 880 by hand",
                    "2. Retail-Core\\nwhat the usual wobble looks like",
                    "3. Retail-Plus\\nthe gap Meera asked about",
                    "4. the plausible wrong answer\\nwhat a p-value never says",
                    "a second route\\nthe textbook paired test"]),
        md('''
## The options

Four ways a team could answer "is the fall real?" before Monday. What separates them is the design
of the data and what each one assumes about it, so the sizing cell below measures those on this
file.

| Option | What it does | What it needs |
|---|---|---|
| A. Flip each member's own two quarters | A coin per member decides which quarter is which, thousands of times, and counts how often chance makes a fall this large | The members in the same order in both quarters, and a loop |
| B. Pool all 44 totals and deal two piles | Treats the 44 member-quarters as 44 different customers and deals them at random | A loop, and two groups of different people, which this file does not have |
| C. The textbook paired test | One library call on the 22 differences, from a formula for bell-shaped data | A statistics library, and differences that behave like a bell curve |
| D. Wait for Q3 | Look again when another quarter has landed | Thirteen weeks, and a Monday meeting with no answer |
'''),
        code('''
plus_q1, plus_q2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
real = mean(plus_q1) - mean(plus_q2)
pairs = len(plus_q1)
zeros = sum(1 for v in plus_q1 + plus_q2 if v == 0)
link = statistics.correlation(plus_q1, plus_q2)            # does a member's Q1 predict their Q2?
wobble = [share_at_least(flip_gaps(plus_q1, plus_q2, 5000, seed=s), real) for s in (1, 2, 3, 4, 5)]
spread = max(wobble) - min(wobble)                          # printed as a spread only: the share waits for section 3

rows = [
    ("A. Flip each member's pair", f"{pairs} members, one Q1 less Q2 each",
     "if nothing changed, either order of a member's two quarters was as likely", f"the share moves by {spread:.3f} across five seeds"),
    ("B. Pool and deal two piles", f"{2 * pairs} totals, treated as {2 * pairs} people",
     "the two quarters hold different customers", f"counts the gaps between members as chance; how far that strays rests on how well a member's Q1 predicts their Q2, {link:.2f} here"),
    ("C. Textbook paired test", f"{pairs} differences, one call",
     "the average difference behaves like a bell curve", f"a formula on lumpy totals: {zeros} of {2 * pairs} are zero"),
    ("D. Wait for Q3", f"{pairs} more member-quarters", "nothing new", "Monday passes with no answer"),
]
kit.table(["Option", "What it stands on here", "What it assumes", "The error it risks"], rows,
          caption="The four options sized on Kalpa's file by what separates them")
kit.matrix(["the same members twice", "different customers"], ["small or lumpy", "large and well-behaved"],
           [["A. flip each pair", "C. textbook paired test"], ["B. shuffle the labels", "the two-sample test"]],
           title="Which chance reference fits which design")
kit.check("the file holds the same 22 members in both quarters, in one order", pairs == len(plus_q2) == 22)
kit.check("8 of the 44 member totals are zero", zeros == 8, f"{zeros}")
kit.check("the flip test's share moves by under 0.005 across five seeds", spread < 0.005, f"{spread:.4f}")
'''),
        md('''
**The best-fit call for Meera's Monday: A, flip each member's own two quarters.** The file holds
the same 22 members in both quarters, so a fair chance reference keeps each member's pair together
and asks only which quarter is which. B treats 22 people as 44 strangers: it counts the gaps between
members as chance, which is the right test for two groups of different customers and the wrong one
here, whatever it prints on this file. C is A's design written as a formula, so it becomes the
second route. D costs a quarter for a question the data can already answer.

**The fact that would change the call.** Thousands of members whose differences behave, which is
what a dashboard at Booking.com's scale sees: C then gives the same answer in one line and is the
house standard. Two groups of different customers, such as Retail-Plus against Retail-Core, switch
the design to B, the label shuffle, which is what chapter 6 runs.
'''),
        md('''
## 1. Five members, two cards each: is a gap of Rs 880 surprising?

Five members' Q1 and Q2 spend, **invented for the table**, one member per row. Every one of them
spent less in Q2, and the real gap is the Q1 mean less the Q2 mean. If the quarter made no
difference, each member's two cards could have come in either order, so a coin per member decides:
heads keeps the pair as recorded, tails swaps it. One toss of the five coins is one chance-only
world, and its gap is the five signed differences added up and divided by five. The room does this
by hand before this cell runs.

| Member | Q1, Rs | Q2, Rs | Q1 less Q2, Rs |
|---|---|---|---|
| A | 3,400 | 2,400 | 1,000 |
| B | 2,900 | 2,200 | 700 |
| C | 4,100 | 3,100 | 1,000 |
| D | 2,500 | 1,900 | 600 |
| E | 3,800 | 2,700 | 1,100 |

**Predict before you run.** Out of 1,000 tosses of the five coins, how many make a gap of Rs 880 or
more? a) about 500, since half of all gaps are positive; b) about 125; c) about 30; d) none, since
the real gap is the largest a toss can make.
'''),
        code('''
q1_cards = [3400, 2900, 4100, 2500, 3800]
q2_cards = [2400, 2200, 3100, 1900, 2700]                  # the same five members, one row each
card_gap = mean(q1_cards) - mean(q2_cards)
card_gaps = flip_gaps(q1_cards, q2_cards, 1000, seed=2026)
card_share, card_either = share_at_least(card_gaps, card_gap), share_either(card_gaps, card_gap)

print(f"Q1 mean Rs {mean(q1_cards):,.0f}, Q2 mean Rs {mean(q2_cards):,.0f}, real gap Rs {card_gap:,.0f}")
print("the first ten tosses:", [round(g) for g in card_gaps[:10]])
kit.strip(card_gaps[:150], markers=[("real gap", card_gap, "bad")], lo=-1000, hi=1000,
          title="150 of the 1,000 tosses on the five invented members, with the real gap marked")
kit.stats([("1,000", "tosses", "a coin per member each time"),
           (f"{round(card_share * 1000)}", "gaps of Rs 880 or more", "in chance-only worlds"),
           (f"{card_share:.3f}", "the share, one direction", f"{card_either:.3f} counting either way")])
'''),
        md('''
**What happened.** The answer is c. Thirty-five tosses in a thousand reached Rs 880, a share of
0.035, and 64 made a gap of Rs 880 in either direction. Ten hand tosses usually show none, which is
why ten is too few. The exact count explains the number: a gap of Rs 880 needs every member to keep
the order they were recorded in, because swapping any one of them pulls the gap down by at least
Rs 240. Only one of the 32 ways five coins can land does that, so the exact share is 1 in 32, 0.031,
and 2 in 32 counting a gap of Rs 880 either way.
'''),
        code('''
card_diffs = [a - b for a, b in zip(q1_cards, q2_cards)]
patterns = list(itertools.product([1, -1], repeat=len(card_diffs)))
exact_hits = sum(1 for p in patterns if sum(s * d for s, d in zip(p, card_diffs)) >= sum(card_diffs))
kit.check("the real gap on the cards is Rs 880", round(card_gap) == 880, f"{card_gap:,.0f}")
kit.check("35 of 1,000 tosses reach it, with seed 2026", round(card_share * 1000) == 35, f"{card_share:.3f}")
kit.check("exactly 1 of the 32 coin patterns reaches it", exact_hits == 1 and len(patterns) == 32, f"{exact_hits} of {len(patterns)}")
'''),
        md('''
## 2. Retail-Core: what the usual wobble looks like

Before judging Retail-Plus, see an ordinary quarter. Retail-Core members also spent a little less
in Q2, and the same 34 members sit in both quarters. The measure is the day's: delivered revenue per
member, one number per member, with a zero for a member who had no delivered order that quarter.

**Predict before you run.** Retail-Core fell by about Rs 110 per member. What share of 5,000 flips
will make a fall at least that large? a) under 0.01; b) about 0.05; c) about a third; d) all of them.
'''),
        code('''
core_q1, core_q2 = member_totals("Retail-Core", "Q1"), member_totals("Retail-Core", "Q2")
core_gap = mean(core_q1) - mean(core_q2)
core_gaps = flip_gaps(core_q1, core_q2, 5000, seed=2026)
core_share, core_either = share_at_least(core_gaps, core_gap), share_either(core_gaps, core_gap)
kit.strip(core_gaps[:150], markers=[("real gap", core_gap, "bad")], lo=-1200, hi=1200,
          title="Retail-Core: 150 of the 5,000 flips, with the real gap marked")
print(f"{len(core_q1)} members, Q1 Rs {mean(core_q1):,.0f}, Q2 Rs {mean(core_q2):,.0f}, gap Rs {core_gap:,.0f}; "
      f"falls at least as large {core_share:.3f}, a move that large either way {core_either:.3f}")
'''),
        md('''
**What happened.** The answer is c. About a third of chance-only worlds make a fall of Rs 110 or
more (0.358), and about seven in ten make a move that large in either direction (0.723), so
Retail-Core's dip is what Meera calls the usual wobble: the real gap sits inside the pile. Keep this
picture, because it is what "nothing happened" looks like.
'''),
        code('''
kit.check("Retail-Core has 34 members in both quarters", len(core_q1) == len(core_q2) == 34)
kit.check("counting falls only, 1,789 of 5,000 flips reach Retail-Core's gap", round(core_share * 5000) == 1789, f"{core_share:.4f}")
kit.check("counting either way, 3,617 of 5,000 flips reach it", round(core_either * 5000) == 3617, f"{core_either:.4f}")
'''),
        md('''
## 3. Retail-Plus: the gap Meera asked about

The same flips, pointed at the segment in Meera's question.

**Predict before you run.** Compared with Retail-Core's share of about a third, Retail-Plus's share
will be: a) about the same; b) larger, since Retail-Plus is a smaller segment; c) much smaller, if
its fall is bigger than chance makes; d) impossible to compute, since some members have zeros.
'''),
        code('''
plus_gaps = flip_gaps(plus_q1, plus_q2, 5000, seed=2026)
plus_share, plus_either = share_at_least(plus_gaps, real), share_either(plus_gaps, real)
kit.columns(["Q1", "Q2"], [("per member, Rs", [round(mean(plus_q1)), round(mean(plus_q2))])],
            fmt=kit.rupees, width=520, title=f"Retail-Plus, {len(plus_q1)} members: delivered revenue per member")
kit.strip(plus_gaps[:200], markers=[("real gap", real, "bad")], lo=-2500, hi=2500,
          title="Retail-Plus: 200 of the 5,000 flips, with the real gap marked")
print(f"real gap Rs {real:,.0f}; falls at least as large: {round(plus_share * 5000)} of 5,000, {plus_share:.3f}; "
      f"a move that large either way: {round(plus_either * 5000)} of 5,000, {plus_either:.3f}")
'''),
        md('''
**What happened.** The answer is c. Retail-Plus members delivered Rs 3,279 each in Q1 and Rs 2,169
in Q2, a fall of Rs 1,110 per member. Counting falls only, 145 of 5,000 flips made a fall that
large, a share of 0.029; counting a move that large in either direction, 286 did, 0.057. Which of
the two is the p-value is a choice that belongs before the test is run. Meera's question arrived
after the fall had been seen, so the honest report gives both and calls the result borderline:
well outside Retail-Core's third, and at the edge of what chance makes.
'''),
        code('''
kit.check("Retail-Plus has 22 members in both quarters", len(plus_q1) == len(plus_q2) == 22)
kit.check("the Retail-Plus gap is Rs 1,110 a member", round(real) == 1110, f"{real:.1f}")
kit.check("counting falls only, 145 of 5,000 flips reach it, with seed 2026", round(plus_share * 5000) == 145, f"{plus_share:.4f}")
kit.check("counting either way, 286 of 5,000 flips reach it, with seed 2026", round(plus_either * 5000) == 286, f"{plus_either:.4f}")
kit.check("the either-way share is about twice the one-direction share, since the flips are symmetric",
          1.8 < plus_either / plus_share < 2.2, f"{plus_either / plus_share:.2f}")
'''),
        md('''
## 4. The plausible wrong answer

**The plausible wrong answer.** The hurried draft turns the one-direction share straight into a
sentence about being wrong. Here it is, computed exactly the way it gets written, and the decision
it invites is Meera treating the fall as 97 percent certain and funding a fix on that basis.
'''),
        code('''
draft = f"p = {plus_share:.2f}, so there is a {plus_share:.0%} chance we are wrong about the drop."
print(draft)
'''),
        md('''
**Why it is wrong.** Every one of the 5,000 flips was tossed in a world where the quarter made no
difference. The share counts how often *that* world makes a fall this large. It says nothing about
the chance that this finding is wrong, which depends on things the flips never saw: how plausible a
fall was before the data, what else changed, how many segments were tested, and whether the
direction was chosen before or after the fall was seen.

**The check.** Build twenty **invented** segments of twenty members in which nothing changed at
all, each member's two quarters drawn from the same range, and run the same test on each. Any
segment that comes back small is a finding that is wrong for certain, whatever its share says.
'''),
        code('''
invented_shares = []
for s in range(20):
    maker = random.Random(100 + s)                       # invented members, same range both quarters
    values = [maker.randint(1500, 4500) for _ in range(40)]
    q1, q2 = values[:20], values[20:]
    invented_shares.append(share_at_least(flip_gaps(q1, q2, 1000, seed=2026), mean(q1) - mean(q2)))

small = [p for p in invented_shares if p <= 0.05]
kit.bars([(f"segment {i + 1}", round(p, 3)) for i, p in enumerate(invented_shares)],
         lit=[i for i, p in enumerate(invented_shares) if p <= 0.05], fmt=lambda v: f"{v:.3f}",
         title="Twenty invented segments where nothing changed; one came back small anyway")
print(f"{len(small)} of 20 came back at 0.05 or below: {small}")
'''),
        md('''
One invented segment came back at 0.003 although nothing happened in it. Its draft note would say
"a 0.3 percent chance we are wrong", and it would be wrong with certainty.

**The fix.** Say the share, the world it was counted in, both directions, and what they let you
conclude.
'''),
        code('''
fixed = (f"If nothing had changed between the quarters, a fall of Rs {real:,.0f} per member or more would turn up "
         f"in about {round(plus_share * 100)} of every 100 flips, and a move that large either way in about "
         f"{round(plus_either * 100)}; the question came after the fall was seen, so we read it as borderline.")
print(fixed)
kit.flow(["the shares\\n" + f"{plus_share:.3f} and {plus_either:.3f}", "the world\\nnothing changed",
          "the direction\\nchosen after the fall", "the reading\\nborderline", "next question\\nhow big is it?"],
         lit=3, title="The sentence a p-value supports, in order")
kit.check("one of twenty no-change segments still came back at 0.05 or below", len(small) == 1, f"{small}")
kit.check("the fixed sentence carries two shares, since both directions were counted", plus_either > plus_share)
'''),
        md('''
What changed: the numbers are the same 0.029 and 0.057, and the claim shrank from "97 percent
certain" to "borderline". That is the claim the evidence carries.

## A second route: the textbook paired test, and every coin pattern counted

Option C, run now as the cross-check, beside the exact count of every one of the 4,194,304 ways 22
coins can land. The library call is the paired test a statistics course teaches first; its formula
is for a later week, and today it is a second opinion. The two unpaired numbers, the pooled shuffle
and the textbook two-sample (Welch) test, are shown beside them as what ignoring the pairing gives.

**Predict before you run.** The textbook paired test's p-value for Retail-Plus, counting falls
only, will be: a) about 0.03, the same reading; b) about 0.3, the opposite reading; c) exactly
0.029, since it is the same method; d) impossible, since the totals are not bell-shaped.
'''),
        code('''
from scipy import stats                                  # the textbook route, named today and taught later
paired_one = stats.ttest_rel(plus_q1, plus_q2, alternative="greater").pvalue
paired_two = stats.ttest_rel(plus_q1, plus_q2).pvalue

diffs = [a - b for a, b in zip(plus_q1, plus_q2)]
counts = {0: 1}                                          # every coin pattern, tallied by the sum it gives
for d in diffs:
    step = {}
    for total, n in counts.items():
        step[total + d] = step.get(total + d, 0) + n
        step[total - d] = step.get(total - d, 0) + n
    counts = step
patterns = 2 ** len(diffs)
exact_one = sum(n for total, n in counts.items() if total >= sum(diffs)) / patterns
exact_two = sum(n for total, n in counts.items() if abs(total) >= sum(diffs)) / patterns

pooled = shuffle_gaps(plus_q1, plus_q2, 5000, seed=2026)
pooled_one, pooled_two = share_at_least(pooled, real), share_either(pooled, real)
welch_one = stats.ttest_ind(plus_q1, plus_q2, equal_var=False, alternative="greater").pvalue
welch_two = stats.ttest_ind(plus_q1, plus_q2, equal_var=False).pvalue

routes = [("flip each pair, 5,000 flips", plus_share, plus_either),
          (f"every coin pattern, {patterns:,}", exact_one, exact_two),
          ("textbook paired test", paired_one, paired_two),
          ("pooled shuffle, pairing ignored", pooled_one, pooled_two),
          ("two-sample test, pairing ignored", welch_one, welch_two)]
kit.table(["Route", "Falls only", "Either way"], [(r, f"{a:.4f}", f"{b:.4f}") for r, a, b in routes],
          caption="Retail-Plus by five routes: the first three keep each member's pair, the last two ignore it")
kit.columns(["flips", "every pattern", "paired test", "pooled", "two-sample"],
            [("falls only", [round(a, 3) for _, a, _ in routes]), ("either way", [round(b, 3) for _, _, b in routes])],
            fmt=lambda v: f"{v:.3f}", width=760, title="The Retail-Plus share by five routes, in both directions")
print(f"paired t = {stats.ttest_rel(plus_q1, plus_q2).statistic:.2f} on {len(diffs) - 1} degrees of freedom")
kit.check("the three paired routes agree on falls only within 0.002",
          max(plus_share, exact_one, paired_one) - min(plus_share, exact_one, paired_one) < 0.002,
          f"{plus_share:.4f}, {exact_one:.4f}, {paired_one:.4f}")
kit.check("the three paired routes agree either way within 0.003",
          max(plus_either, exact_two, paired_two) - min(plus_either, exact_two, paired_two) < 0.003,
          f"{plus_either:.4f}, {exact_two:.4f}, {paired_two:.4f}")
kit.check("on this file, ignoring the pairing moves the share by under 0.005", abs(pooled_one - plus_share) < 0.005,
          f"{pooled_one:.4f} against {plus_share:.4f}")
'''),
        md('''
**What happened.** The answer is a. The textbook paired test says 0.0275 counting falls only and
0.055 either way, the exact count of every coin pattern says 0.0274 and 0.0549, and the flips said
0.029 and 0.057: three routes, one borderline reading. The unpaired numbers sit close here, 0.027
from the pooled shuffle and 0.026 from the two-sample test, because a member's Q1 spend barely
predicts their Q2 spend in this file (0.04). On a tier where heavy buyers stay heavy, pooling would
count the gaps between members as chance, sit far higher, and could miss a real fall; the extras
sheet shows one. **When to switch.** Use the textbook paired call when the members number in the
thousands and a team standard expects it; keep the flips when the members are few or the totals
lumpy, or when the person reading the answer needs to see how it was made.

> **Kavya's review.** "Retail-Core's third is the wobble. Retail-Plus sits at about 3 in 100
> counting falls and 6 in 100 either way, three routes that keep each member's pair agree, and you
> said which direction you counted and why. Borderline is an honest answer. Now tell me how much
> money it is."

### In the interview

**[S] What does p = 0.03 mean, and not mean?** "It means that if there were no real difference, a
difference at least as large as the one we saw, in the direction we saw, would turn up about 3 times
in 100 by chance alone; counting either direction it would be about 6 in 100, and I say which I
counted and whether I chose it before seeing the data. It does not mean a 3 percent chance the
finding is wrong, and it says nothing about whether the effect is large or worth acting on." The
interviewer is listening for the conditional, "if there were no difference", and for the refusal to
call it the probability of being wrong.

**[S] How do you know whether a change in a metric is significant?** "I build a reference for what
chance alone does, and the design of the data decides how. When the same customers are measured
twice, I keep each customer's two numbers together and flip which is which at random; when the two
groups are different customers, I shuffle the group labels. Then I count how often chance makes a
change as large as the real one, in one direction and in both, check the count behind it, and size
it in money, because significant only means larger than noise." A sharp follow-up: why not pool the
two quarters? Pooling counts the gaps between members as chance. Here it happens to land close,
because Q1 barely predicts Q2; on a tier where heavy buyers stay heavy, it would overstate chance.

**[D] Four ways to ask whether a fall is real: which do you run for a CEO's Monday, and what would
make you switch?** "The same 22 members sit in both quarters, so I flip each member's pair: it
respects the design, and I can show it with cards. I cross-check with the textbook paired test,
which becomes the default on thousands of well-behaved members. Pooling the 44 totals treats 22
people as 44 and is the right test only for different customers. I would wait a quarter only if
both routes came back unclear, because then more data is the only thing that helps."

### Depth: one direction or both

The chapter counted both directions because the question arrived after the fall was seen. Had
Meera asked before Q2 closed, "is Retail-Plus falling?", counting falls only would have been
decided before the test, and 0.029 would carry the reading alone. The rule the glossary keeps: the
direction is decided before the test is run. The flips move a little with the seed, in both
directions, and the reading never does.
'''),
        code('''
seeds = (1, 2, 3, 4, 5)
one_way = [round(share_at_least(flip_gaps(plus_q1, plus_q2, 5000, seed=s), real), 4) for s in seeds]
both_ways = [round(share_either(flip_gaps(plus_q1, plus_q2, 5000, seed=s), real), 4) for s in seeds]
kit.line([f"seed {s}" for s in seeds], [("falls only", one_way, "plain"), ("either way", both_ways, "bad")], lo=0,
         fmt=lambda v: f"{v:.3f}", title="The Retail-Plus shares under five other seeds, counted both ways")
print(f"falls only {one_way}; either way {both_ways}")
kit.check("across five seeds, falls only stays between 0.025 and 0.031", all(0.025 <= s <= 0.031 for s in one_way), f"{one_way}")
kit.check("across five seeds, either way stays between 0.050 and 0.060", all(0.050 <= s <= 0.060 for s in both_ways), f"{both_ways}")
'''),
        code('''
kit.check_summary()
print("Next: chapter 2. The fall is borderline against chance; is it worth acting on?")
'''),
    ]


# =========================================================================== chapter 2
def chapter2():
    return [
        md('''
# Real, and worth acting on?

**Week 1, Thursday. Chapter 2 of 6.** By the end of this notebook you can size a borderline gap in
rupees against the segment, the company and the cost of acting, keep "significant" and "important"
in two separate sentences, and read a range of plausible falls as the second route.

> **The client asks.** "So my tier really is slipping. What do I get to fix it?"
>
> The head of Retail-Plus, before the growth review

**The metric at stake.** The same delivered revenue per member, now multiplied out to rupees a
quarter. **Who asks and what rides on it.** The head of Retail-Plus wants a retention budget, and
Meera has to weigh it against every other line in the quarter: fund a Rs 11,000 offer that cannot
pay back and the money is gone; ignore a fall that is growing and the tier drains. **Who else faces
it.** At Microsoft, a small change to how Bing showed ad headlines raised revenue by 12 percent,
more than 100 million dollars a year in the United States alone, while the company's own
researchers found that only about a third of experiments built to improve a metric did improve it.
Size in money, beside the share, is what told one change from the rest.

Chapter 1 found the Retail-Plus fall, Rs 1,110 per member, borderline against chance: about 3 in
100 flips counting falls, about 6 in 100 either way. This chapter adds two helpers: `delivered`, a
segment's revenue in a quarter, and `bootstrap_gaps`, which redraws the members' own differences to
give the range the second route reads.
'''),
        md('**Setup.** The toolkit from chapter 1, plus the two new helpers.'),
        setup(T1, T2, extra='''
plus_q1, plus_q2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
real = mean(plus_q1) - mean(plus_q2)
print(f"{len(plus_q1)} Retail-Plus members; gap Rs {real:,.0f} per member, carried from chapter 1")
'''),
        the_map(1, ["the options\\nbreak-even, range, test, benchmark",
                    "1. per member and per segment\\nthe fall in rupees",
                    "2. against the company\\nwhere the quarter's money sits",
                    "3. the plausible wrong answer\\nranked by p-value",
                    "4. against the cost\\nthe retention offer priced",
                    "a second route\\nthe range of the members' falls"]),
        md('''
## The options

Four ways a team could answer "is it worth acting on?". Each one reaches a decision by a different
kind of evidence.

| Option | What it does | What it needs |
|---|---|---|
| A. Break-even on the estimate | The fall in rupees beside the company's quarter and the offer's cost, and the share of the fall the offer must win back | One pass over the orders, and a cost, assumed today |
| B. The low end of a range | Redraw the members' own falls many times and ask whether even a small plausible fall clears the cost | A loop, and a reader who takes a range |
| C. Test the offer on half the tier | Offer it to a coin-chosen half for a quarter and hold back the other half | Money, a quarter's wait, and enough members a side |
| D. A past offer's recovery rate | Read what an earlier retention offer won back | A measured rate, which Kalpa does not have |
'''),
        code('''
offer_per_member = 500                                   # assumed for the chapter; no Kalpa figure exists
tier_cost = offer_per_member * len(plus_q1)
half_cost = offer_per_member * (len(plus_q1) // 2)
low_ends = [sorted(bootstrap_gaps(plus_q1, plus_q2, 5000, seed=s))[125] for s in (1, 2, 3, 4, 5)]
rows = [
    ("A. Break-even on the estimate", f"{len(ORDERS)} orders, one pass", "the Rs 1,110 per member is the true fall",
     "a fall that is really smaller turns a paying offer into a loss"),
    ("B. The low end of a range", f"{len(plus_q1)} differences x 5,000 redraws", "22 members stand for the tier",
     f"a rough low end: it moves by Rs {max(low_ends) - min(low_ends):,.0f} across five seeds"),
    ("C. Test the offer on half", f"{len(plus_q1) // 2} members a side, {kit.rupees(half_cost)} a quarter",
     "a coin picks the half, so the halves start alike", "a quarter's wait, and eleven a side can show only a large recovery"),
    ("D. A past offer's rate", "a recovery measured on an earlier offer", "that offer's members were like these",
     "no Kalpa offer has been measured, so it cannot run today"),
]
kit.table(["Option", "What it stands on", "What it assumes", "What it risks"], rows,
          caption="The options sized on Kalpa's file by what separates them")
kit.matrix(["decides from today's files", "needs a new measurement"], ["one number", "a range or a test"],
           [["A. break-even", "B. the range's low end"], ["D. a past offer's rate", "C. a half-tier test"]],
           title="What each option stands on")
kit.check("the offer costs Rs 11,000 for the tier and Rs 5,500 for half of it", tier_cost == 11000 and half_cost == 5500)
kit.check("the range's low end moves by under Rs 100 across five seeds", max(low_ends) - min(low_ends) < 100,
          f"Rs {min(low_ends):,.0f} to Rs {max(low_ends):,.0f}")
'''),
        md('''
**The best-fit call: A for Monday's number, with B as the second route.** Meera's decision is a
budget line, so the answer has to be in rupees beside the company's quarter and the offer's cost,
with the share of the fall the offer must win back. B asks whether even a small plausible fall
clears that cost, which is the honest follow-up to a borderline fall. C spends money and a quarter,
so it is where the answer can lead once it is reached. **The fact that would
change the call.** A recovery rate measured on an earlier offer to members like these, which is D:
with it, the break-even alone decides, and the range matters less.
'''),
        md('''
## 1. The fall in rupees, per member and for the segment

A per-member gap is a rate. The budget holder needs the total: the gap times the members who exist
in both quarters.

**Predict before you run.** Retail-Plus lost Rs 1,110 per member. In total, per quarter, that is
roughly: a) Rs 2,400; b) Rs 24,000; c) Rs 2.4 lakh; d) Rs 24 lakh.
'''),
        code('''
plus_fall = round(real * len(plus_q1))
kit.bridge(("Retail-Plus, Q1", sum(plus_q1)), [("the fall", -plus_fall)], end_label="Retail-Plus, Q2",
           title="Retail-Plus delivered revenue, Q1 to Q2")
kit.stats([(kit.rupees(real), "per member", "Q1 mean less Q2 mean"),
           (f"{len(plus_q1)}", "members", "in both quarters"),
           (kit.rupees(plus_fall), "a quarter", "the segment's fall")])
kit.check("Retail-Plus lost Rs 24,420 of delivered revenue in a quarter", plus_fall == 24420, kit.rupees(plus_fall))
'''),
        md('''
**What happened.** The answer is b. Rs 1,110 times 22 members is Rs 24,420 a quarter: the tier
delivered Rs 72,130 in Q1 and Rs 47,710 in Q2. For the segment that is a third of its money, which is
why the head of Retail-Plus is worried.

## 2. Against the company's quarter

Meera runs the company, so the second size is the fall against the company's delivered revenue,
with every segment's move side by side.

**Predict before you run.** As a share of the company's Q2 delivered revenue, the Retail-Plus fall
is: a) about 30 percent; b) about 3 percent; c) under half of one percent; d) impossible to say
without Business.
'''),
        code('''
company_q1 = sum(delivered(s, "Q1") for s in SEGMENTS)
company_q2 = sum(delivered(s, "Q2") for s in SEGMENTS)
moves = [(s, delivered(s, "Q2") - delivered(s, "Q1")) for s in SEGMENTS]
kit.bridge(("company, Q1", company_q1), moves, end_label="company, Q2", lo=12_000_000, lit=[1],
           title="Delivered revenue, Q1 to Q2, by segment (the axis starts at Rs 1.2 crore so the moves show)")
share_of_company = plus_fall / company_q2
print(f"company delivered: Q1 {kit.rupees(company_q1)}, Q2 {kit.rupees(company_q2)}; "
      f"the Retail-Plus fall is {share_of_company:.2%} of Q2")
kit.check("the bridge lands: Q1 plus every segment's move is Q2", company_q1 + sum(m for _, m in moves) == company_q2)
kit.check("the Retail-Plus fall is under half of one percent of the company's Q2", share_of_company < 0.005,
          f"{share_of_company:.2%}")
'''),
        md('''
**What happened.** The answer is c. The company delivered Rs 1,28,64,680 in Q2, and the
Retail-Plus fall is 0.19 percent of it, less than one rupee in five hundred. The fall is borderline
against chance and small against the company; both are true, and the note needs both.

## 3. The plausible wrong answer

**The plausible wrong answer.** A hurried draft runs the flip test on every segment with enough
members, sorts by the share, and lets the order of the shares set the order of the growth review.
Student waits for chapter 3. The shares count a move that large in either direction, since no
direction was fixed before the quarter was seen.
'''),
        code('''
ranked = []
for s in ["Retail-Core", "Retail-Plus", "Business"]:
    q1, q2 = member_totals(s, "Q1"), member_totals(s, "Q2")
    share = share_either(flip_gaps(q1, q2, 5000, seed=2026), mean(q1) - mean(q2))
    ranked.append((s, share, delivered(s, "Q2") - delivered(s, "Q1")))
by_share = sorted(ranked, key=lambda r: r[1])
for n, (s, share, _) in enumerate(by_share, 1):
    print(f"  {n}. {s:12s} p = {share:.3f}, either way")
print(f"Draft: '{by_share[0][0]} is the surest move of the quarter, so it opens the growth review: fund its retention programme first.'")
'''),
        md('''
**Why it is wrong.** The share says how surely a move beats chance. It never says how big the move
is, and the draft ordered the review by the wrong column: the review would open on a borderline fall
of Rs 24,420 and fund a programme because a share was small, before anyone asked where the
quarter's money moved or what the fix costs. **The check** puts the rupees beside the share and
orders the same three segments by money, and an invented example shows why the two columns can
disagree so far: with enough orders, even a trivial gap beats chance.
'''),
        code('''
by_money = sorted(ranked, key=lambda r: -abs(r[2]))
kit.table(["Segment", "p, either way", "Delivered revenue, Q2 less Q1", "Place by share", "Place by rupees"],
          [(s, f"{share:.3f}", kit.rupees(move), by_share.index((s, share, move)) + 1, by_money.index((s, share, move)) + 1)
           for s, share, move in ranked],
          caption="The same three segments with the money beside the share")
maker = random.Random(11)                                  # invented orders: two quarters of different orders
base = [maker.randint(1000, 3400) for _ in range(40000)]
sizes, shares = [100, 1000, 5000, 20000], []
for n in sizes:
    later = base[:n]
    earlier = base[20000:20000 + n]
    lift = 20 - (mean(earlier) - mean(later))              # set the earlier quarter exactly Rs 20 above the later one
    earlier = [v + lift for v in earlier]
    shares.append(share_at_least(shuffle_gaps(earlier, later, 500, seed=2026), 20))
kit.line([f"{n:,}" for n in sizes], [("share, Rs 20 gap", shares, "bad")], fmt=lambda v: f"{v:.3f}",
         title="Invented: the same Rs 20 gap tested on more and more orders a quarter")
print(dict(zip(sizes, [round(s, 3) for s in shares])))
kit.check("ordered by share, Retail-Plus comes first; ordered by rupees moved, it does not",
          by_share[0][0] == "Retail-Plus" and by_money[0][0] != "Retail-Plus", f"{by_money[0][0]} leads by rupees")
kit.check("an invented Rs 20 gap goes from chance-sized to significant on sample size alone",
          shares[0] > 0.2 and shares[-1] < 0.01, f"{[round(s, 3) for s in shares]}")
'''),
        md('''
**The fix.** Two sentences where the draft had one, and the review ordered by money: "The
Retail-Plus fall is borderline against chance, about 3 in 100 flips counting falls and 6 in 100
either way. It is worth Rs 24,420 a quarter, 0.19 percent of the company's delivered revenue."
Ordered by rupees moved, Business opens the review and Retail-Plus comes second. Business's rise
does not shrink the Retail-Plus fall: the fall is judged on its own terms, against the company's
quarter and against what the offer costs. What changed: the order of the review and the size of the
claim. The Retail-Plus programme now has to justify itself against Rs 24,420 a quarter and the
offer's cost.

## 4. Against the cost: the retention offer priced

The head of Retail-Plus proposes a retention offer. **The cost is an assumption for this chapter,
since no Kalpa figure exists for it:** Rs 500 per member per quarter, offered to all 22 members.

**Predict before you run.** What share of the Rs 24,420 fall would the offer have to win back just
to pay for itself in revenue? a) all of it; b) about 45 percent; c) about 5 percent; d) none, since
any recovery is a gain.
'''),
        code('''
offer_cost = tier_cost
break_even = offer_cost / plus_fall
scenarios = [("wins back a quarter", 0.25), ("wins back the break-even", break_even),
             ("wins back three quarters", 0.75)]
kit.bars([(label, max(0, round(plus_fall * r - offer_cost))) for label, r in scenarios], fmt=kit.rupees,
         lit=[2], title="Revenue won back less the offer's cost, per quarter (a loss is drawn at zero)")
for label, r in scenarios:
    print(f"  {label:26s} net {kit.rupees(round(plus_fall * r - offer_cost))}")
kit.check("the offer costs Rs 11,000 a quarter", offer_cost == 11000, kit.rupees(offer_cost))
kit.check("it pays only above a 45 percent recovery", round(break_even, 2) == 0.45, f"{break_even:.3f}")
'''),
        md('''
**What happened.** The answer is b. The offer costs Rs 11,000 a quarter, so it has to win back 45
percent of the fall before it breaks even on revenue. Winning back a quarter loses about Rs 4,900;
winning back three quarters gains about Rs 7,300. The decision rests on a recovery rate nobody has
measured, on a fall that is itself borderline, which is what the note should say.

## A second route: the range of the members' own falls

Option B. The Rs 1,110 is one estimate from 22 members. Redraw the 22 members' own Q1 less Q2
differences with replacement 5,000 times and read the middle 95 percent of the averages. That range
is called a **confidence interval**; how to build one properly is a later week's topic, and today it
arrives as a picture.

**Predict before you run.** Where does the range's low end sit, against zero and against the
offer's Rs 500 per member? a) above both; b) just above zero, and far below Rs 500; c) below zero,
so the fall cannot be real; d) exactly Rs 1,110 every time.
'''),
        code('''
boot = bootstrap_gaps(plus_q1, plus_q2, 5000, seed=2026)
ordered = sorted(boot)
low, high = ordered[125], ordered[4874]
at_or_below_zero = sum(1 for g in boot if g <= 0) / len(boot)
kit.strip(boot[:200], markers=[("zero", 0, "bad"), ("offer per member", offer_per_member, "plain"),
                               ("real gap", real, "good")], lo=-1000, hi=3000,
          title="200 of the 5,000 redrawn averages per member, with zero, the offer and the real gap marked")
print(f"middle 95 percent: Rs {low:,.0f} to Rs {high:,.0f} per member, "
      f"or {kit.rupees(low * 22)} to {kit.rupees(high * 22)} a quarter; share at or below zero {at_or_below_zero:.3f}")
kit.check("the range's low end sits above zero and far below the offer's Rs 500 a member", 0 < low < offer_per_member / 2, f"Rs {low:,.0f}")
kit.check("consistency: the share of redraws at or below zero sits within 0.02 of the flips' falls-only 0.029",
          abs(at_or_below_zero - 0.029) < 0.02, f"{at_or_below_zero:.3f}")
'''),
        md('''
**What happened.** The answer is b. This approximate 95 percent range runs from about Rs 80 to Rs
2,160 per member, and its low end moves between about Rs 15 and Rs 100 with the seed, so it sits
close to zero; under 2 in 100 redraws land at or below zero, a consistency check beside the flips'
0.029 rather than a second p-value. At its low end the fall is about Rs 1,780 a quarter for the whole
tier. The offer's Rs 500 per member sits far above that low end, which is the arithmetic behind
"worth watching, and not worth acting on alone": if the head of Retail-Plus wants to act, the cheap
way is the offer on a coin-chosen half. **When to switch.** Read the range whenever the decision has
a cost to beat; the share alone is enough only when the question is "real or not".

> **Kavya's review.** "Borderline against chance by two routes, worth Rs 24,420 a quarter, 0.19
> percent of the company and a third of the tier. The range's low end sits far below what the offer
> costs, so this is a watch item. If the head of Retail-Plus wants to act, offer it to a coin-chosen
> half and hold back the other half, knowing that eleven members a side will show only a large
> recovery."

### In the interview

**[F] A metric moved and the test says significant; how do you decide whether the business should
act?** "Significant only tells me the move is bigger than noise, and here it is borderline. To act
I need three more things: the size in money against the business and the segment, the cost of the
action, and how much of the gap the action could recover. If the break-even recovery is higher than
anything we have seen, or the range of the effect dips below the cost, I recommend a small test with
a held-back group rather than a rollout."

**[S] Explain a finding to a non-technical stakeholder.** "I lead with the decision the finding
supports, in one sentence, with one number and its denominator. Then the evidence, the caveat that
would change my view, and the action with what it costs. For example: Retail-Plus is spending less
by a borderline amount, about Rs 24,000 a quarter, which is a third of the tier and a fifth of one
percent of the company; an offer pays only if it wins back 45 percent, so we watch it, and if we act
we test on half the members first."

**[D] Break-even, a range, a test on half the tier, or a past offer's recovery rate: which do you
take to the budget meeting, and what would change it?** "The break-even on the estimate, checked
against the low end of the range, because the meeting decides money and the range says how small
the fall could be. The half-tier test is what I recommend if they want to act. A measured recovery
rate from an earlier offer would let the break-even decide alone."

### Depth: revenue is not margin

The break-even above compares the offer with revenue won back. Kalpa keeps only its margin on that
revenue, so the true break-even is higher. **The margin is an assumption for the depth section,
since no Kalpa margin figure exists:** at 30 percent, the offer would have to win back more than the
whole fall.
'''),
        code('''
assumed_margin = 0.30                                    # assumed; no Kalpa figure exists
margin_break_even = offer_cost / (plus_fall * assumed_margin)
kit.columns(["on revenue", "on a 30% margin"], [("recovery needed", [round(break_even * 100), round(margin_break_even * 100)])],
            fmt=lambda v: f"{v:.0f}%", width=520, title="Share of the fall the offer must win back to break even")
kit.check("on an assumed 30 percent margin the offer cannot pay back from this fall", margin_break_even > 1,
          f"{margin_break_even:.0%}")
'''),
        code('''
kit.check_summary()
print("Next: chapter 3. Student is up 40 percent; how many orders stand behind it?")
'''),
    ]


# =========================================================================== chapter 3
def chapter3():
    return [
        md('''
# The count behind 40 percent

**Week 1, Thursday. Chapter 3 of 6.** By the end of this notebook you can count what a rate stands
on, run a chance reference for a small count, choose between trusting, testing and waiting, and
reach the same share a second way, then check the idea itself on orders that did not rise.

> **The client asks.** "Student is up 40 percent; should I move budget there?"
>
> Meera Raghavan, CEO, Kalpa Retail

**The metric at stake.** Orders per quarter in the Student segment, Q2 against Q1. **Who asks and
what rides on it.** Meera, deciding whether acquisition money follows the fastest-growing segment:
move it on a rate that chance made and the budget is spent on a segment that may be flat next
quarter. **Who else faces it.** In the 1990s the Gates Foundation put money behind small schools,
partly because small schools were over-represented among the best performers. The statistician
Howard Wainer showed they were over-represented among the worst as well, which is what small
counts do: by 2001 the Foundation had given about 1.7 billion dollars to education projects, and
Wainer's essay calls that a costly lesson in how far small groups swing.

Chapters 1 and 2 found the Retail-Plus fall borderline and small against the company. Meera's
second question is about a rise, the biggest on the page. This chapter adds `orders_in` and
`flip_rises`, a chance reference built for a count.
'''),
        md('**Setup.** The toolkit so far, plus the two new helpers.'),
        setup(T1, T2, T3, extra='''
print("toolkit ready:", ", ".join(["member_totals", "flip_gaps", "shuffle_gaps", "share_at_least",
                                   "share_either", "delivered", "bootstrap_gaps", "orders_in", "flip_rises"]))
'''),
        the_map(2, ["the options\\ntrust, test, rule, wait",
                    "1. the headline\\nevery segment's orders, Q2 against Q1",
                    "2. the plausible wrong answer\\nthe fastest rise wins the budget",
                    "3. chance on the count\\na coin flip per order",
                    "4. 42 percent on 12\\nthe interview's version",
                    "a second route\\nevery deal, and real handfuls"]),
        md('''
## The options

Four ways a team could answer "should budget follow the 40 percent?". What separates them is what
each needs to know first and what it assumes; the count itself is yours to find in section 2, so
the option that depends on it is sized after that.

| Option | What it does | What it risks |
|---|---|---|
| A. Trust the headline | Rank segments by growth and fund the fastest | Moving money on a rate a coin could make |
| B. A chance reference for the count | Deal each order to a quarter by coin flip and see how often chance makes a 40 percent rise | Nothing, once the count is found |
| C. The rule of thumb | Treat any rate standing on fewer than thirty customers as a lead, however many orders they placed | A blunt line: it says careful and stops there |
| D. Wait for thirty customers | Hold the decision until thirty or more customers stand behind the rate | Time, which depends on how fast new customers arrive |
'''),
        code('''
order_segments = ["Retail-Core", "Retail-Plus", "Business", "Student"]
rows = [
    ("A. Trust the headline", f"{len(order_segments)} segments x 2 quarters", "the rate is the rise",
     "budget follows a rise a coin could make"),
    ("B. Coin flips on the count", "the count behind the rate, found in section 2",
     "each order was as likely to land in either quarter", "none, once the count is known"),
    ("C. The rule of thumb", "the customers behind the rate, against thirty",
     "thirty independent buyers is roughly where a rate settles", "it says careful and stops there"),
    ("D. Wait for thirty customers", "the customers behind the rate and how fast new ones arrive, sized after section 2",
     "new customers keep arriving", "the chance to invest early"),
]
kit.table(["Option", "What it needs", "What it assumes", "What it risks"], rows,
          caption="The options sized by what each needs and assumes")
kit.flow(["A. trust\\nthe rate", "B. chance on\\nthe count", "C. the rule\\nof thumb", "D. wait for\\nthirty"], lit=1,
         title="The best-fit call for Monday is B, with C as its one-line summary")
kit.check("every segment carries orders in both quarters, so every rate exists",
          all(orders_in(s, "Q1") > 0 and orders_in(s, "Q2") > 0 for s in order_segments))
'''),
        md('''
**The best-fit call: B, said with C.** The coin flips tell Meera how often chance alone makes her
headline, which is the question; the rule of thumb is the sentence she remembers. The rule counts
customers, because more orders from the same few customers add orders and no new evidence: thirty
orders from three people are still three people's habits. D is the action the answer may lead to, and
how long it takes depends on how many customers stand behind the rate, so you size it once you have
found them. **The fact that would change the call.** A cheap way to buy more orders fast, such
as a small paid test aimed only at students: then D stops being a wait and becomes a two-week
experiment.
'''),
        md('''
## 1. The headline: every segment's orders, Q2 against Q1

Meera's 40 percent is about orders placed, whatever their status. Put every segment on the same
footing: Q2 orders for every 100 orders in Q1.

**Predict before you run.** Which segment shows the biggest rise? a) Business, since it carries the
revenue; b) Retail-Core; c) Student; d) none rose.
'''),
        code('''
index = {s: round(100 * orders_in(s, "Q2") / orders_in(s, "Q1")) for s in order_segments}
kit.columns(order_segments, [("Q2 orders per 100 in Q1", [index[s] for s in order_segments])], lit=[3], width=620,
            title="Q2 orders for every 100 in Q1: Student is the only segment above 100")
for s in order_segments:
    print(f"{s:12s} {index[s] - 100:+d} percent")
kit.check("Student's orders rose 40 percent", index["Student"] == 140, f"{index['Student']}")
kit.check("Student is the only segment above 100", [s for s in order_segments if index[s] > 100] == ["Student"])
'''),
        md('''
**What happened.** The answer is c. Student is the only segment whose orders rose, by 40 percent,
while Retail-Plus fell 35 and the other two slipped a few points. Read as a leaderboard, Student
wins.

## 2. The plausible wrong answer

**The plausible wrong answer.** The draft reads the leaderboard as a plan.
'''),
        code('''
fastest = max(order_segments, key=lambda s: index[s])
draft = f"{fastest} is up {index[fastest] - 100} percent, the fastest on the page: move acquisition budget to {fastest}."
print(draft)
'''),
        md('''
**Why it is wrong.** The rate is correct arithmetic and it travels without its count. A rise of 40
percent on four hundred orders and on a handful of orders are different facts: on a handful, one or
two orders landing in one quarter rather than the other makes the whole rise, and the budget would
follow them.

**Your turn: the check.** Type these lines into the empty cell below and run them. Then write, in
one sentence, how many orders and how many customers stand behind Meera's 40 percent:

```python
student = [o for o in ORDERS if o["segment"] == "Student"]
print(len(student), "Student orders across both quarters")
print({q: sum(1 for o in student if o["quarter"] == q) for q in ("Q1", "Q2")})
print(len({o["customer_id"] for o in student}), "distinct Student customers")
```
'''),
        empty(),
        md('''
**Your turn, continued: size option D.** Option D waits until thirty or more customers stand
behind the rate, since more orders from the same customers settle nothing. How fast are new Student
customers arriving? Type these lines into the next empty cell:

```python
q1_buyers = {o["customer_id"] for o in student if o["quarter"] == "Q1"}
q2_buyers = {o["customer_id"] for o in student if o["quarter"] == "Q2"}
print(len(q1_buyers | q2_buyers), "customers behind the rise;", len(q2_buyers - q1_buyers), "of them new in Q2")
```

Then write one sentence on how long waiting for thirty customers would take at that pace, and one on
what a two-week paid test aimed at new students would change.
'''),
        empty(),
        md('''
The mechanism, on **invented** segments: how many points one extra order moves a rate, at four
sizes.
'''),
        code('''
sizes = [10, 30, 100, 400]
kit.bars([(f"{n} orders", round(100 / n, 2)) for n in sizes], fmt=lambda v: f"{v:g} points",
         title="Invented: how far one order moves a rate, by the number of orders behind it")
kit.check("on ten orders, one order is ten points", 100 / sizes[0] == 10)
'''),
        md('''
## 3. Chance on the count: a coin flip per order

Chapter 1's flips swapped each member's two quarters. For a count, the chance reference is simpler
still: if Student's ordering had not changed, each Student order was as likely to land in Q1 as in
Q2. Flip a coin per order, 5,000 times, and count how often chance alone makes a rise of 40 percent
or more.

**Predict before you run.** For Student's own orders, what share of coin-flip worlds show a rise of
40 percent or more? a) under 1 percent; b) about 5 percent; c) about 40 percent; d) all of them.
'''),
        code('''
student_orders = sum(1 for o in ORDERS if o["segment"] == "Student")
flips = flip_rises(student_orders, 5000, seed=2026)


def bucket(rises):
    """Three plain buckets, so the chart says what the decision needs and nothing else."""
    return [sum(1 for r in rises if r < 0), sum(1 for r in rises if 0 <= r < 0.4 - 1e-9),
            sum(1 for r in rises if r >= 0.4 - 1e-9)]


student_share = sum(1 for r in flips if r >= 0.4 - 1e-9) / len(flips)
kit.columns(["fell", "rose under 40%", "rose 40% or more"], [("coin-flip worlds", bucket(flips))],
            lit=[2], width=620, title="Student's orders dealt to quarters by coin flip, 5,000 times")
print(f"share of chance-only worlds with a rise of 40 percent or more: {student_share:.3f}")
'''),
        md('''
**What happened.** The answer is c. About four in ten coin-flip worlds make a rise of 40 percent or
more from Student's orders alone. Chance makes Meera's headline almost as often as not, and the flips
are generous: they treat each order as its own draw, while Student's orders come from very few
customers, whose orders move together. Now the same 40 percent on bigger counts: a segment with
Retail-Core's orders, and an **invented** segment of 400.
'''),
        code('''
core_n = sum(1 for o in ORDERS if o["segment"] == "Retail-Core")
compare = {"Student": student_share}
core_label = "Retail-Core's count"
for label, n in [(core_label, core_n), ("invented, 400 orders", 400)]:
    rises = flip_rises(n, 5000, seed=2026)
    compare[label] = sum(1 for r in rises if r >= 0.4 - 1e-9) / len(rises)
kit.columns(list(compare), [("share of worlds with a 40% rise", [round(v, 3) for v in compare.values()])],
            fmt=lambda v: f"{v:.3f}", width=620, title="The same 40 percent rise: how often chance makes it, by the count behind it")
kit.check("chance makes Student's rise in more than a third of worlds", student_share > 0.33, f"{student_share:.3f}")
kit.check("on Retail-Core's count the same rise is rare", compare[core_label] < 0.10, f"{compare[core_label]:.3f}")
kit.check("on 400 orders chance almost never makes it", compare["invented, 400 orders"] < 0.002)
'''),
        md('''
**The fix.** The rate, its count, and whether chance makes it, with the decision that follows:
"Student orders rose 40 percent, on a count so small that chance alone makes a rise that size in
about 40 percent of coin-flip worlds. Not yet: we watch Student until more customers buy, thirty or
more behind the rise, before any budget moves." What changed: the decision. The draft moved budget;
the fix moves nothing and names the count that would reopen the question, in customers, since
orders from the same few customers are one habit counted again.

## 4. 42 percent on 12 users, or 31 percent on 1,200?

The interview's version of Student, **invented** with the interview's numbers. Suppose the true
rate for everyone were 31 percent. How often would a group of only 12 users show 42 percent or more,
by chance alone?

**Predict before you run.** a) almost never; b) about 1 time in 20; c) about 1 time in 3; d) always.
'''),
        code('''
random.seed(2026)
small_rates = [sum(1 for _ in range(12) if random.random() < 0.31) / 12 for _ in range(5000)]
large_rates = [sum(1 for _ in range(1200) if random.random() < 0.31) / 1200 for _ in range(300)]
small_share = sum(1 for r in small_rates if r >= 5 / 12 - 1e-9) / len(small_rates)
kit.strip(small_rates[:120], markers=[("42%", 5 / 12, "bad"), ("true 31%", 0.31, "good")], lo=0, hi=1,
          fmt=lambda v: f"{v:.0%}", title="Invented: 120 groups of 12 users at a true 31 percent")
kit.strip(large_rates[:120], markers=[("42%", 5 / 12, "bad"), ("true 31%", 0.31, "good")], lo=0, hi=1,
          fmt=lambda v: f"{v:.0%}", title="Invented: 120 groups of 1,200 users at the same true 31 percent")
print(f"groups of 12 at 42% or more: {small_share:.1%}; groups of 1,200: {min(large_rates):.1%} to {max(large_rates):.1%}")
kit.check("a true 31 percent reads 42 or more on 12 users about a third of the time", 0.25 < small_share < 0.37,
          f"{small_share:.3f}")
kit.check("on 1,200 users it never reaches 42 percent", max(large_rates) < 5 / 12, f"{max(large_rates):.3f}")
'''),
        md('''
**What happened.** The answer is c. A true 31 percent shows up as 42 percent or more in about 31
percent of groups of twelve, while groups of 1,200 all land between about 28 and 35 percent. One
user out of twelve is 8.3 points; one out of 1,200 is under a tenth of a point.

## A second route: every deal counted, and real handfuls

The coin flips sampled 5,000 worlds. Two checks follow. The first recounts the same coin model
exactly: with a count this small, every possible way of dealing the orders to the two quarters can
be listed. The second checks the idea rather than the arithmetic, on real orders: Retail-Core's
orders fell 3 percent between the quarters, so draw handfuls of them the size of Student's count
and see how often a handful shows a 40 percent rise anyway.

**Predict before you run.** How often will a Student-sized handful of Retail-Core's real orders show
a rise of 40 percent or more? a) never, since Retail-Core fell; b) about 1 time in 20; c) about 1
time in 3; d) about 9 times in 10.
'''),
        code('''
deals = list(itertools.product(["Q1", "Q2"], repeat=student_orders))
rising = 0
for deal in deals:
    q2 = deal.count("Q2")
    q1 = student_orders - q2
    if q1 == 0 or q2 / q1 - 1 >= 0.4 - 1e-9:
        rising += 1
exact_share = rising / len(deals)

core_orders = [o for o in ORDERS if o["segment"] == "Retail-Core"]


def handful_share(size, times=5000, seed=2026):
    """Draw handfuls of Retail-Core's real orders and count how often a handful shows a 40 percent rise."""
    random.seed(seed)
    hits = 0
    for _ in range(times):
        hand = random.sample(core_orders, size)
        q1 = sum(1 for o in hand if o["quarter"] == "Q1")
        if q1 == 0 or (size - q1) / q1 - 1 >= 0.4 - 1e-9:
            hits += 1
    return hits / times


handfuls = handful_share(student_orders)
bigger = handful_share(60)
kit.columns(["coin flips", "every deal, counted", "Retail-Core handfuls"],
            [("share with a 40% rise", [round(student_share, 3), round(exact_share, 3), round(handfuls, 3)])],
            fmt=lambda v: f"{v:.3f}", width=620, title="Three routes to how often chance makes the rise on Student's count")
print(f"exact share {exact_share:.3f}; the flips said {student_share:.3f}; Student-sized handfuls of Retail-Core's orders "
      f"{handfuls:.3f}; handfuls of sixty {bigger:.4f}")
kit.check("the exact count and the flips agree within two points", abs(exact_share - student_share) < 0.02,
          f"{exact_share:.3f} against {student_share:.3f}")
kit.check("real handfuls from a segment that fell show the rise about a third of the time", 0.25 < handfuls < 0.45,
          f"{handfuls:.3f}")
kit.check("handfuls of sixty almost never show it", bigger < 0.01, f"{bigger:.4f}")
'''),
        md('''
**What happened.** The answer is c. Counting every deal gives 0.387 where the flips gave 0.397, so
the flips were computed right. The handfuls check the idea: Retail-Core's orders fell 3 percent, yet
a handful of them the size of Student's count shows a 40 percent rise about a third of the time
(0.344), and a handful of sixty almost never does. The swing belongs to small counts, whatever
segment they come from, so the verdict holds: chance makes Meera's headline about four times in
ten. **When to switch.** Count every deal while the count is small enough to list; on a few dozen
orders the list runs into the billions, and the flips are the only practical route.

> **Kavya's review.** "Student's rise is real arithmetic on too few orders, from too few customers,
> to act on. Count both, say how often chance makes the rise, and give Meera the number of customers
> that would reopen it. That is a complete answer, and it costs nothing to be right later."

### In the interview

**[F] 42 percent on 12 users against 31 percent on 1,200; which do you trust?** "The 31 percent, as
the working estimate. On 12 users one person moves the rate by more than 8 points, so 42 percent is
well inside what chance produces around a true rate near 31. I keep the 42 as a lead: find out what
is different about that group and measure it on more users before acting."

**[D] A segment is up 40 percent and the CEO wants to move budget; you can trust it, test it on the
count, or wait. Which, and what would change your mind?** "Test it on the count first: how often do
coin flips make that rise on that many orders, and how many customers placed them? If chance makes it
often, or a few customers made it, the answer is not yet, with the number of customers that would
reopen it. A cheap, fast way to reach new customers in that segment would turn the wait into a short
experiment, and I would propose that."

### Depth: where thirty comes from

Thirty is a habit, and no law: it is roughly where a count of independent observations stops
swinging wildly from one extra. Orders from the same customer are not independent, since a customer
who orders once tends to order again, so the observations that count are customers: thirty orders
from three customers are three observations. The curve below is the coin-flip chance of a 40 percent
rise at growing counts of independent buyers, each buying once, the same simulation as section 3.
'''),
        code('''
counts = [10, 20, 30, 50, 100, 200, 400]
curve = []
for n in counts:
    rises = flip_rises(n, 3000, seed=2026)
    curve.append(sum(1 for r in rises if r >= 0.4 - 1e-9) / len(rises))
kit.line([str(n) for n in counts], [("chance of a 40% rise", curve, "bad")], fmt=lambda v: f"{v:.2f}",
         title="Chance of a 40 percent rise from coin flips alone, by the independent buyers behind the rate")
kit.check("the chance falls below one in five by thirty independent buyers", curve[2] < 0.2, f"{curve[2]:.3f}")
'''),
        code('''
kit.check_summary()
print("Next: chapter 4. Marketing says the monsoon sale lifted revenue 6 percent; split it by segment.")
'''),
    ]


# =========================================================================== chapter 4
def chapter4():
    return [
        md('''
# The discount, split by segment

**Week 1, Thursday. Chapter 4 of 6.** By the end of this notebook you can reproduce a campaign's
headline lift, split it by segment, say why the blend and the segments disagree, and say what
putting both groups on one mix checks and what it cannot.

> **The client asks.** "Marketing ran a monsoon-sale discount for Retail-Plus in August, says it
> lifted revenue 6 percent, and wants to repeat it for Diwali. Did the discount work, or did those
> customers buy anyway?"
>
> Meera Raghavan, CEO, Kalpa Retail, with the marketing lead's report open beside her

**The metric at stake.** August spend per customer, for customers who got the sale against
customers who did not. **Who asks and what rides on it.** The marketing lead owns the campaign and
wants it repeated at 15 percent off; Meera signs the Diwali budget. Monday's rule applies: at 15
percent off, orders must rise about 17.6 percent just for revenue to stand still, so a sale that
did not lift spend gives margin away. **Who else faces it.** eBay measured its search ads in large
controlled experiments and split the result by customer: new and infrequent users bought more after
seeing an ad, while frequent users, whose buying the ads did not change, took most of the ad spend,
so the average return was negative (Blake, Nosko and Tadelis, NBER working paper 20171). The classic
public case of a blend reversing is UC Berkeley's 1973 graduate admissions: 44 percent of men and 35
percent of women were admitted overall, and department by department the small bias ran in favour
of women.

Chapters 1 to 3 answered Meera's first two questions. This chapter opens the campaigns table and
the exposure table, and adds `spend` and `group` to the toolkit.

**Where the exposure table comes from.** The exposure table is the campaign platform's August
list: the 160 Retail-Plus and Retail-Core customers the platform held, under the platform's own
customer ids, with one average August spend for each group. It records who received the sale,
whatever the sale was aimed at, which is why it counts Retail-Core customers among them although the
campaigns table aimed the sale at Retail-Plus: the campaigns table is the plan, and the list is what
the platform sent. It cannot be matched to Finance's order file, whose 22 Retail-Plus members and
discount column carry no record of the sale. So read it for who got the sale and how the two groups
differ. The Diwali hold-back is sized on the platform's list, and the retention offer on Finance's
order file.
'''),
        md('**Setup.** The toolkit so far, plus the two campaign tables and two new helpers.'),
        setup(T1, T2, T3, T4, extra='''
print(len(EXPOSURE), "customers on the platform's list;", CAMPAIGNS[0]["name"], CAMPAIGNS[0]["discount_pct"],
      "percent off,", CAMPAIGNS[0]["starts"], "to", CAMPAIGNS[0]["ends"], "; target", CAMPAIGNS[0]["target_segment"])
'''),
        the_map(3, ["the options\\nbefore-after, blend, split, one mix",
                    "1. Marketing's number\\nreproduced first",
                    "2. the plausible wrong answer\\nthe blend trusted",
                    "3. the split\\ninside each segment",
                    "4. the fix\\nwhat to tell Meera",
                    "a second route\\nboth groups on one mix"]),
        md('''
## The options

Four ways a team could answer "did the discount work?". They differ in which list they stand on and
in what each takes on trust, so the sizing cell measures those.

| Option | What it compares | What it risks |
|---|---|---|
| A. Before and after | The targeted segment's revenue in the sale month against the month before, in Finance's order file | Everything else that changed that month |
| B. Exposed against not exposed, blended | August spend for everyone who got the sale against everyone who did not, on the platform's list | Two groups built from different mixes of customers |
| C. Exposed against not exposed, inside each segment | The same comparison run separately in each segment | Anything that differs between the groups inside a segment |
| D. Both groups on one mix | Each group's segment averages weighted to the same mix of segments | The same as C; it is C said as one number |
'''),
        code('''
mix_yes = len(group("yes", "Retail-Plus")) / len(group("yes"))
mix_no = len(group("no", "Retail-Plus")) / len(group("no"))
stand_still = 1 / (1 - int(CAMPAIGNS[0]["discount_pct"]) / 100) - 1
july_august = sum(1 for o in ORDERS if o["segment"] == "Retail-Plus" and o["status"] == "delivered"
                  and o["order_date"][:7] in ("2026-07", "2026-08"))
rows = [
    ("A. Before and after", f"Finance's order file: {july_august} Retail-Plus orders in July and August",
     "nothing else changed between the months", "credits the sale with the month"),
    ("B. Blended", f"the platform's list: {len(EXPOSURE)} customers in 2 groups",
     "both groups hold the same mix of customers", f"the mixes differ: {mix_yes:.0%} against {mix_no:.0%} Retail-Plus"),
    ("C. Inside each segment", f"the platform's list: {len(EXPOSURE)} customers in 4 cells",
     "who got it inside a segment was as good as random", "whatever else differs inside a segment"),
    ("D. Both groups on one mix", "the same 4 cells, reweighted", "the same as C",
     "nothing beyond C: it agrees with C by construction"),
]
kit.table(["Option", "What it stands on", "What it assumes", "What it risks"], rows,
          caption="The options sized on Kalpa's files by what separates them")
kit.columns(["exposed", "not exposed"], [("share who are Retail-Plus", [round(100 * mix_yes), round(100 * mix_no)])],
            fmt=lambda v: f"{v:.0f}%", width=520, title="Before choosing: the two groups are not built from the same customers")
print(f"at {CAMPAIGNS[0]['discount_pct']} percent off, orders must rise {stand_still:.1%} for revenue to stand still")
kit.check("the two groups differ in mix", abs(mix_yes - mix_no) > 0.05, f"{mix_yes:.0%} against {mix_no:.0%}")
kit.check("Monday's rule: 15 percent off needs about 17.6 percent more volume", round(stand_still, 3) == 0.176)
'''),
        md('''
**The best-fit call: C, with D as its one-line form.** The two groups hold different mixes of
customers, which the chart above shows before any spend is compared, so the blend in B compares
Retail-Plus-heavy against Retail-Core-heavy as much as sale against no sale. C compares like with
like inside each segment. A comes back in chapter 6, where the question is what else changed in
August. **The fact that would change the call.** A group chosen at random: if Marketing had decided
who got the sale by coin flip, the two groups would share one mix and B would be fair.
'''),
        md('''
## 1. Marketing's number, reproduced first

Before disagreeing with anyone's number, rebuild it. Marketing compared everyone who got the sale
with everyone who did not.

**Predict before you run.** Marketing's lift will come out at: a) about 6 percent, as reported;
b) about 3 percent; c) negative; d) impossible to reproduce from these tables.
'''),
        code('''
blend_yes, blend_no = spend(group("yes")), spend(group("no"))
blend = blend_yes / blend_no - 1
kit.columns(["got the sale", "did not"], [("August spend per customer", [round(blend_yes), round(blend_no)])],
            fmt=kit.rupees, width=520, title="Marketing's comparison: everyone exposed against everyone not")
print(f"exposed {kit.rupees(blend_yes)} against {kit.rupees(blend_no)}: {blend:+.1%}")
kit.check("Marketing's 6 percent reproduces from the tables", 0.05 < blend < 0.07, f"{blend:+.1%}")
'''),
        md('''
**What happened.** The answer is a. Customers who got the sale spent Rs 3,395 in August against
Rs 3,200 for those who did not, a lift of 6.1 percent. Marketing's arithmetic is right, which is why
the next step matters.

## 2. The plausible wrong answer

**The plausible wrong answer.** The draft trusts the reproduced number and writes the plan.
'''),
        code('''
draft = (f"The discount worked: exposed customers spent {kit.rupees(blend_yes)} against {kit.rupees(blend_no)}, "
         f"up {blend:.1%}; repeat it for Diwali.")
print(draft)
'''),
        md('''
**Why it is wrong.** The comparison is correct arithmetic on an unfair pair of groups. The exposed
group holds more Retail-Plus members, who spend more whatever happens, so part or all of the 6.1
percent could be who got the sale rather than what the sale did. If the draft goes to Meera, a
Diwali sale at 15 percent off is repeated on a lift that may not exist, and it needs 17.6 percent
more orders just to stand still.

## 3. The check: split by segment

Run the same comparison inside each segment, where the customers are alike.

**Predict before you run.** Inside Retail-Plus and inside Retail-Core, customers who got the sale
spent: a) more, by about 6 percent in each; b) more in one segment and less in the other; c) less in
both; d) the same in both.
'''),
        code('''
cells = {}
for s in ["Retail-Plus", "Retail-Core"]:
    cells[s] = (spend(group("no", s)), spend(group("yes", s)), len(group("no", s)), len(group("yes", s)))
kit.columns(["Retail-Plus", "Retail-Core", "blended"],
            [("did not get it", [round(cells["Retail-Plus"][0]), round(cells["Retail-Core"][0]), round(blend_no)]),
             ("got the sale", [round(cells["Retail-Plus"][1]), round(cells["Retail-Core"][1]), round(blend_yes)])],
            fmt=kit.rupees, lit=[2], title="August spend per customer: each segment against the blend")
kit.table(["Segment", "Did not get it", "Got the sale", "Change", "Customers, not / got"],
          [(s, kit.rupees(a), kit.rupees(b), f"{b / a - 1:+.1%}", f"{n} / {m}") for s, (a, b, n, m) in cells.items()],
          caption="The same comparison inside each segment, with the count behind every average")
within = {s: b / a - 1 for s, (a, b, _, _) in cells.items()}
kit.check("inside every segment the exposed spent less", all(v < 0 for v in within.values()), f"{within}")
kit.check("the blend rises while the segments fall", blend > 0 and max(within.values()) < 0)
'''),
        md('''
**What happened.** The answer is c. Inside Retail-Plus the customers who got the sale spent Rs
4,850 against Rs 5,000, and inside Retail-Core Rs 1,940 against Rs 2,000: about 3 percent less in
both. The blend rose because half of the exposed group were Retail-Plus members against 40 percent
of the others, and Retail-Plus members spend more than twice as much. Each segment says one thing
and the blend says the opposite; the segments are the fair comparison.
'''),
        code('''
kit.vflow(["the exposed group\\nhalf Retail-Plus", "Retail-Plus spends more\\nwhatever the sale does",
           "the blend rises\\n+6.1 percent", "inside each segment\\nabout 3 percent less"],
          kinds=["plain", "plain", "bad", "good"], title="Why the blend and the segments disagree")
'''),
        md('''
## 4. The fix: what to tell Meera

"The monsoon sale did not lift spend: inside each segment, customers who got it spent about 3
percent less than customers who did not, on 30 exposed and 40 or 60 unexposed customers per segment.
Marketing's 6 percent comes from who got the sale, since the exposed group held more Retail-Plus
members. Do not repeat it as designed; if Diwali runs a sale, hold back a random slice of each
segment so the comparison is fair." What changed: the decision, from repeat to redesign. The reason
is the mix of customers; Marketing's arithmetic was right.

## A second route: both groups on one mix, and what it checks

Put the exposed group's segment averages into the unexposed group's mix, and the other way round.
This route reuses the four cells the split used, so it cannot disagree with the split and cannot
catch an error in those cells. What it checks is the explanation: if the mix of customers is the
whole reason the blend rose, putting both groups on one mix must remove the whole 6.1 percent, both
ways round. The independent check comes in chapter 6, from Finance's order file.

**Predict before you run.** Reweighted to one mix, the exposed group's spend against the unexposed
group's will be: a) about 6 percent higher, as Marketing said; b) about 3 percent lower in both
directions; c) higher one way and lower the other; d) equal.
'''),
        code('''
w_no = {s: len(group("no", s)) / len(group("no")) for s in cells}
w_yes = {s: len(group("yes", s)) / len(group("yes")) for s in cells}
yes_in_no_mix = sum(w_no[s] * cells[s][1] for s in cells)
no_in_yes_mix = sum(w_yes[s] * cells[s][0] for s in cells)
one = yes_in_no_mix / blend_no - 1
two = blend_yes / no_in_yes_mix - 1
kit.columns(["in the unexposed mix", "in the exposed mix"],
            [("did not get it", [round(blend_no), round(no_in_yes_mix)]), ("got the sale", [round(yes_in_no_mix), round(blend_yes)])],
            fmt=kit.rupees, width=620, title="Both groups on one mix, each way round")
print(f"unexposed mix: {kit.rupees(yes_in_no_mix)} against {kit.rupees(blend_no)}, {one:+.1%}; "
      f"exposed mix: {kit.rupees(blend_yes)} against {kit.rupees(no_in_yes_mix)}, {two:+.1%}")
kit.check("the mix accounts for the whole blended lift, both ways round", abs(one - two) < 0.005 and one < 0,
          f"{one:+.1%} and {two:+.1%}")
'''),
        md('''
**What happened.** The answer is b. On the unexposed group's mix the exposed spend Rs 3,104 against
Rs 3,200; on the exposed group's mix, Rs 3,395 against Rs 3,500. Both are 3.0 percent less, as they
must be if the mix is the whole story: the 6.1 percent is gone once both groups share one mix.
**When to switch.** Split by segment when the stakeholder reads a table; put both groups on one mix
when the answer has to be one number on one line of the note, or when there are too many segments to
show.

> **Kavya's review.** "You rebuilt Marketing's number before disagreeing with it, which is what
> keeps Monday civil. The split says 3 percent less in both segments, one mix says the same by
> construction, and the reason is who got the sale. Now tell me what else changed in August,
> because neither of them can see that."

### In the interview

**[F] Revenue rose after a discount; did the campaign work, and what would you need to know?** "Who
got it and against whom. I would reproduce the claimed lift, then compare customers who got it with
customers who did not inside each segment, and check the mix of the two groups. If the segments
disagree with the total, the total is a mix effect. To know properly I would want a random held-back
group next time, agreed before the campaign."

**[F] The campaign lifted revenue overall but every segment fell; how, and which do you report?**
"The exposed group leaned toward high spenders, so the blend rose on mix while each segment did
worse. I report the segments, and name the mix as the reason the blend rose, so nobody thinks I
picked the flattering cut."

**[D] Before and after, the blend, the split or one mix: which do you use for a campaign readout,
and what would make the blend acceptable?** "The split, with one mix as the one-line version, said
plainly to be the split restated. Before and after sees every August effect, and the blend mixes
customers. The blend becomes fair only when a coin decided who got the campaign."

### Depth: how big a mix shift it takes

Keep the segment averages fixed and move only the share of Retail-Plus members in the exposed
group. The blend's lift is invented from there, since only the mix changes.
'''),
        code('''
shares = [0.40, 0.45, 0.50, 0.55, 0.60]
lifts = []
for p in shares:
    mixed_yes = p * cells["Retail-Plus"][1] + (1 - p) * cells["Retail-Core"][1]
    lifts.append(round(100 * (mixed_yes / blend_no - 1), 1))
kit.line([f"{int(p * 100)}%" for p in shares], [("blended lift, percent", lifts, "bad")], lo=-5,
         fmt=lambda v: f"{v:+.1f}%", title="Invented from the real cells: the blended lift as the exposed group's Retail-Plus share moves")
kit.check("with the same mix as the unexposed group the blend shows the segments' fall", lifts[0] < 0, f"{lifts}")
'''),
        code('''
kit.check_summary()
print("Next: chapter 5. Three answers, one page, and room for 'not yet'.")
'''),
    ]


# =========================================================================== chapter 5
NOTE = '''
NUMBERS = {}
plus_q1, plus_q2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
real = mean(plus_q1) - mean(plus_q2)
plus_flips = flip_gaps(plus_q1, plus_q2, 5000, seed=2026)
NUMBERS["share"] = share_at_least(plus_flips, real)
NUMBERS["either"] = share_either(plus_flips, real)
NUMBERS["fall"] = round(real * len(plus_q1))
NUMBERS["company"] = sum(delivered(s, "Q2") for s in SEGMENTS)
NUMBERS["tier_q1"] = delivered("Retail-Plus", "Q1")
NUMBERS["offer"] = 500 * len(plus_q1)
NUMBERS["low"] = sorted(bootstrap_gaps(plus_q1, plus_q2, 5000, seed=2026))[125]
student_n = sum(1 for o in ORDERS if o["segment"] == "Student")
student_buyers = len({o["customer_id"] for o in ORDERS if o["segment"] == "Student"})
flips = flip_rises(student_n, 5000, seed=2026)
NUMBERS["student_rise"] = round(100 * orders_in("Student", "Q2") / orders_in("Student", "Q1")) - 100
NUMBERS["student_chance"] = sum(1 for r in flips if r >= 0.4 - 1e-9) / len(flips)
NUMBERS["blend"] = spend(group("yes")) / spend(group("no")) - 1
NUMBERS["within"] = spend(group("yes", "Retail-Plus")) / spend(group("no", "Retail-Plus")) - 1
NUMBERS["within_core"] = spend(group("yes", "Retail-Core")) / spend(group("no", "Retail-Core")) - 1
'''


def chapter5():
    return [
        md('''
# The note that may say not yet

**Week 1, Thursday. Chapter 5 of 6.** By the end of this notebook you can turn four chapters of
numbers into one page Meera reads in two minutes: claim, evidence with its base, the caveat that
would change the claim, and the action with its cost, with "not yet" where the evidence says so.

> **The client asks.** "One page, two minutes. If the honest answer is 'we do not know yet', say so
> and tell me what would tell us."
>
> Meera Raghavan, CEO, Kalpa Retail

**The metric at stake.** Every number chapters 1 to 4 produced, each now carried with its base.
**Who asks and what rides on it.** Meera, before Monday's growth review, where Marketing will
defend its campaign against the note: a line that loses its base sends money the wrong way, and a
line that hedges everything gives her nothing to decide. **Who else faces it.** Amazon's meetings
run on narrative memos, read in silence at the start: "We don't do PowerPoint (or any other
slide-oriented) presentations at Amazon," Jeff Bezos wrote in his 2017 letter to shareholders; the
team writes six-page memos instead. A narrative forces the writer to connect each claim to its
evidence, which is this chapter's job on one page.

Chapters 1 to 4 each left a number. This chapter adds no statistics: it gathers the numbers into
one dictionary, `NUMBERS`, and writes from it.
'''),
        md('''
**Setup.** The whole toolkit, and the day's numbers recomputed into `NUMBERS` from the same helpers
and the same seeds, so every figure in the note traces to a chapter.
'''),
        setup(T1, T2, T3, T4, NOTE, extra='''
print(len(NUMBERS), "numbers gathered from chapters 1 to 4")
'''),
        the_map(4, ["the options\\nyes-no, dashboard, note, deck",
                    "1. the numbers\\none table, four chapters",
                    "2. the plausible wrong answer\\nthree numbers without a base",
                    "3. the fix\\nthe four-part note, guided",
                    "4. not yet\\nthe Student and discount lines",
                    "a second route\\nthe day's rules, applied"]),
        md('''
## The options

Four ways a team could answer Meera in writing. The sizing cell counts what each asks her to read
and what each carries.

| Option | What it is | What it risks |
|---|---|---|
| A. A yes or no per question | Three words she asked for | Every caveat, and the "not yet" she explicitly allowed |
| B. The dashboard | Every number the chapters produced, in one table | Two minutes spent reading, and no decision on the page |
| C. The four-part note | Claim, evidence with its base, caveat, action with its cost, per question | The discipline to keep it under 200 words |
| D. A slide deck | Ten slides for Monday | A meeting to present it; the logic lives in the talk and leaves the page |
'''),
        code('''
import json

option_a = "Retail-Plus: yes, it is down. Student: yes, move budget. Discount: yes, it worked."
printed = []                                             # the dashboard: everything chapters 1 to 4 printed
for path in sorted(pathlib.Path.cwd().glob("C2_W01_D04_0[1-4]_*_STUDENT.ipynb")):
    for cell in json.loads(path.read_text())["cells"]:
        for out in cell.get("outputs", []):
            printed.append("".join(out.get("text", "")))
option_b = " ".join(printed)
option_c_limit = 200
rows = [("A. Yes or no", len(option_a.split()), "none", "every caveat"),
        ("B. Dashboard", len(option_b.split()), "all of them, unsorted", "the decision"),
        ("C. Four-part note", option_c_limit, "each claim's", "only length"),
        ("D. Slide deck", "ten slides", "what the slides draw", "a meeting to present")]
kit.table(["Option", "Words", "Bases carried", "What it loses"], rows,
          caption="The options sized in words and in what they carry")
kit.bars([(r[0], r[1]) for r in rows[:3]], fmt=lambda v: f"{v} words", lit=[2],
         title="Words each written option asks Meera to read; C is the ceiling she set")
kit.check("the yes-or-no option is short and drops the caveats", len(option_a.split()) < 20 and "not yet" not in option_a)
'''),
        md('''
**The best-fit call: C, the four-part note under 200 words.** It is the only option that carries
each number with its base and a decision in the same place, which is what Meera asked for. A drops
what she explicitly allowed; B and D hand her the analysis instead of the answer. **The fact that
would change the call.** A standing weekly review with the same three metrics: then a small
dashboard with fixed bases beats rewriting the note each week, and the note shrinks to what moved.
'''),
        md('''
## 1. The numbers, in one table

**Predict before you run.** How many of the day's key numbers need a second number beside them
before they can go in a sentence? a) none, they are all final; b) one; c) most of them; d) only the
percentages.
'''),
        code('''
table = [
    ("Retail-Plus fall, share counting falls only", f"{NUMBERS['share']:.3f}", "the world it was counted in"),
    ("Retail-Plus fall, share counting either way", f"{NUMBERS['either']:.3f}", "why both directions are reported"),
    ("Retail-Plus fall, rupees a quarter", kit.rupees(NUMBERS["fall"]), "the company's quarter"),
    ("Company delivered revenue, Q2", kit.rupees(NUMBERS["company"]), "the window"),
    ("Retention offer, rupees a quarter", kit.rupees(NUMBERS["offer"]), "an assumption, said as one"),
    ("Student orders, rise", f"{NUMBERS['student_rise']}%", "the count, and chance on it"),
    ("Student, coin-flip share for that rise", f"{NUMBERS['student_chance']:.3f}", "what it means for the decision"),
    ("Monsoon sale, blended lift", f"{NUMBERS['blend']:+.1%}", "who got it"),
    ("Monsoon sale, inside Retail-Plus", f"{NUMBERS['within']:+.1%}", "the counts per group"),
]
kit.table(["Number", "Value", "What must sit beside it"], table, caption="The day's numbers, each with the base it needs")
kit.check("nine numbers carry forward from chapters 1 to 4", len(table) == 9)
kit.check("every number has a base named beside it", all(t[2] for t in table))
'''),
        md('''
**What happened.** The answer is c. Every number needs a partner: a share needs its world and its
direction, a rupee figure its whole, a rate its count, a lift its groups. A number without its
partner is the next section's trap.

## 2. The plausible wrong answer

**The plausible wrong answer.** A hurried note uses the three headline percentages, each correct
arithmetic, and each written the way it first appeared.
'''),
        code('''
tier_fall = NUMBERS["fall"] / NUMBERS["tier_q1"]
headline = (f"Retail-Plus revenue fell {tier_fall:.0%}. Student is up {NUMBERS['student_rise']}%. "
            f"The monsoon sale lifted revenue {NUMBERS['blend']:.0%}. We recommend a retention offer for "
            f"Retail-Plus, budget to Student, and the sale again for Diwali.")
print(headline)
'''),
        md('''
**Why it is wrong.** Three true numbers lead to three wrong decisions. "Fell 34 percent" is 34
percent of a tier that delivered under one percent of the company's revenue, so Meera hears a crisis
worth Rs 24,420 a quarter. "Up 40 percent" travels without the count chance makes it on. "Lifted 6
percent" is the blend chapter 4 took apart. **The check** is an audit every note line has to pass:
does each number carry its base, its count or chance, and a caveat?
'''),
        code('''
def audit(line):
    """Three yes-or-no questions per line of a note: base, count or chance, caveat."""
    import re
    low = line.lower()
    base = any(w in low for w in ["of the company", "a quarter", "quarter on quarter", "against rs", "per member",
                                  "than customers"])
    count = any(w in low for w in ["in 100", "chance", "count", "worlds"]) or bool(re.search(r"\\b\\d+ (customers|orders|members)", low))
    caveat = any(w in low for w in ["if ", "unless", "until", "not yet", "caveat", "because"])
    return ["yes" if x else "missing" for x in (base, count, caveat)]


lines = [s.strip() + "." for s in headline.split(".") if s.strip()][:3]
kit.matrix([l[:34] for l in lines], ["a base", "count or chance", "a caveat"], [audit(l) for l in lines],
           title="The headline note, audited line by line")
missing = sum(a.count("missing") for a in map(audit, lines))
print(f"{missing} of 9 audit cells missing")
kit.check("the headline note fails the audit on most cells", missing >= 7, f"{missing} missing")
'''),
        md('''
## 3. The fix: the four-part note, guided on Retail-Plus

The row asks for the Retail-Plus line to be built together, in four parts, before the other two
are written alone.

**Predict before you run.** Which part does a hurried analyst leave out most often? a) the claim;
b) the evidence; c) the caveat; d) the action.
'''),
        code('''
DECISIONS = {"Retail-Plus": "watch, and test before funding", "Student": "not yet",
             "Discount": "do not repeat as designed"}      # the decision each line carries, kept as data
plus_line = {
    "claim": "Retail-Plus is spending less by a borderline amount, and it is small against the company.",
    "evidence": (f"Members delivered Rs 1,110 less each, {kit.rupees(NUMBERS['fall'])} a quarter, "
                 f"{NUMBERS['fall'] / NUMBERS['company']:.2%} of the company's quarter; if nothing had changed, a fall that "
                 f"large turns up in about {round(NUMBERS['share'] * 100)} in 100 flips, and a move that large either way in "
                 f"about {round(NUMBERS['either'] * 100)}."),
    "caveat": f"We asked after seeing the fall, and it could be as small as Rs {round(NUMBERS['low'], -1):,.0f} a member.",
    "action": (f"Watch it; if we act, test the Rs 500-a-member offer on a coin-chosen half of the tier, "
               f"{kit.rupees(NUMBERS['offer'] // 2)} a quarter, holding back the rest."),
}
kit.flow([f"{k}\\n{len(v.split())} words" for k, v in plus_line.items()], lit=2,
         title="The Retail-Plus line in four parts, with the caveat lit")
print("\\n".join(f"{k.upper()}: {v}" for k, v in plus_line.items()))
kit.check("the Retail-Plus line passes the audit", audit(" ".join(plus_line.values())) == ["yes", "yes", "yes"])
'''),
        md('''
**What happened.** The answer is c: the caveat is the part most often missing, and it is the part a
CEO keeps an analyst for. The Retail-Plus line now carries its base (the company's quarter), its
chance in both directions (about 3 and 6 in 100), its caveat (a question asked after the fall was
seen, and a fall that could be small) and its action with a cost.

## 4. Not yet: the Student and discount lines

"Not yet" is a claim, a caveat and an action in one sentence, provided it names what would turn it
into a yes. Write both lines and audit the whole note.

**Predict before you run.** How many words will the three answers take? a) under 50; b) under 200;
c) about 400; d) over 1,000.
'''),
        code('''
student_line = (f"Student orders rose {NUMBERS['student_rise']} percent quarter on quarter, on a count so small that chance alone makes "
                f"that rise in about {round(NUMBERS['student_chance'] * 100)} in 100 worlds. Not yet: no budget moves "
                f"until more customers buy, thirty or more behind the rise.")
discount_line = (f"The monsoon sale did not lift spend: inside each segment, the {len(group('yes', 'Retail-Plus'))} customers who got it spent about "
                 f"{abs(NUMBERS['within']):.0%} less than customers who did not; the {NUMBERS['blend']:.0%} blend "
                 f"is higher only because the exposed group held more Retail-Plus members. Do not repeat it as "
                 f"designed; at Diwali, hold back a random slice of each segment.")
note = " ".join(plus_line.values()) + " " + student_line + " " + discount_line
kit.matrix(["Retail-Plus", "Student", "Discount"], ["a base", "count or chance", "a caveat"],
           [audit(" ".join(plus_line.values())), audit(student_line), audit(discount_line)],
           title="The fixed note, audited line by line")
kit.bars([("headline note", len(headline.split())), ("four-part note", len(note.split())), ("Meera's ceiling", 200)],
         fmt=lambda v: f"{v} words", lit=[1], title="Words on the page")
print(student_line)
print(discount_line)
print(f"the whole note: {len(note.split())} words")

import re
found = re.findall(r"Rs [\\d,]+|\\d+\\.\\d+%|\\d+ percent|\\d+ in 100|\\d+%", note)
known = {kit.rupees(NUMBERS["fall"]), kit.rupees(NUMBERS["offer"] // 2), "Rs 500", "Rs 1,110",
         f"Rs {round(NUMBERS['low'], -1):,.0f}", f"{NUMBERS['fall'] / NUMBERS['company']:.2%}",
         f"{NUMBERS['student_rise']} percent", f"{round(NUMBERS['share'] * 100)} in 100",
         f"{round(NUMBERS['student_chance'] * 100)} in 100",
         f"{abs(NUMBERS['within']):.0%}", f"{NUMBERS['blend']:.0%}"}
traced = [f for f in found if f in known]
print(f"figures in the note: {len(found)}; traced to a chapter's number: {len(traced)}")
kit.check("the full note is under 200 words", len(note.split()) < 200, f"{len(note.split())}")
kit.check("every line of the fixed note passes the audit",
          all(a == ["yes", "yes", "yes"] for a in [audit(student_line), audit(discount_line)]))
kit.check("every figure in the note traces to a number a chapter computed", found and len(found) == len(traced),
          f"{len(traced)} of {len(found)}")
'''),
        md('''
**What happened.** The answer is b: the three answers fit under Meera's 200 words with their
bases, caveats and actions, against the headline note's 30 words and three wrong decisions, and
every figure in them traces to a number a chapter computed. What changed: three decisions.
Retail-Plus becomes a watch item with a cheap test if anyone acts, Student becomes a watch with a
threshold, and the Diwali sale becomes a redesign with a hold-back.

## A second route: the day's rules, applied to the numbers

The note was written by hand from the chapters. Reach its three decisions a second way: apply the
rule each chapter ended on to that chapter's numbers, mechanically, and compare the decisions with
the ones the note carries. A note whose action does not follow from its own numbers would pass every
figure check and fail here.

**Predict before you run.** How many of the note's three decisions will the rules reach on their
own? a) none, since rules cannot write; b) one; c) two; d) all three.
'''),
        code('''
rules = [
    ("Retail-Plus", "chapter 2: the range's low end sits below the offer's cost per member",
     NUMBERS["low"] < 500, "watch, and test before funding", "fund the offer"),
    ("Student", "chapter 3: fewer than thirty customers stand behind the rise",
     student_buyers < 30, "not yet", "move the budget"),
    ("Discount", "chapter 4: the blend rose while every segment fell",
     NUMBERS["blend"] > 0 and max(NUMBERS["within"], NUMBERS["within_core"]) < 0, "do not repeat as designed", "repeat it"),
]
reached = {q: (yes if test else no) for q, _, test, yes, no in rules}
kit.table(["Question", "The rule", "Does it hold?", "Decision the rule gives", "Decision the note carries"],
          [(q, rule, "yes" if test else "no", reached[q], DECISIONS[q]) for q, rule, test, _, _ in rules],
          caption="The note's decisions, reached a second way from the numbers alone")
kit.flow(["the numbers\\nfrom NUMBERS", "the rule\\neach chapter's last line", "the decision\\nreached mechanically",
          "the note's decision\\ncompared"], lit=3, title="The second route, step by step")
kit.check("the rules reach all three of the note's decisions", reached == DECISIONS, f"{sum(reached[q] == DECISIONS[q] for q in DECISIONS)} of 3")
'''),
        md('''
**What happened.** The answer is d. Applied to the numbers alone, the rules reach the note's three
decisions, so the note's actions follow from its evidence and from nothing else. **When to switch.**
Apply the rules by hand for a one-off note; write them as code, as this cell does, when the same
note is produced every week, because a rule in code cannot drift toward the answer someone wants.

> **Kavya's review.** "Three answers, each with its base, its caveat and a cost, and two of them say
> not yet with the thing that would change them. Marketing will push on the third on Monday; the
> next chapter is the ground you will stand on."

### In the interview

**[S] Explain a finding to a non-technical stakeholder.** "Claim first, in one sentence, with one
number and its base. Then the evidence, the caveat that would change the claim, and the action with
what it costs. If the honest answer is not yet, I say so and name what would turn it into a yes, and
by when."

**[D] The CEO wants a yes or no and the honest answer is 'not yet'; what do you say, and how do you
hold the line when marketing pushes?** "Not yet, and here is what would tell us by when. I offer the
cheapest test that settles it, such as a held-back group at Diwali. I hold the line with the split
and leave authority out of it: I show their number reproduced, then the segments, and invite them to
find the flaw."

**[D] One-line answers, a dashboard or a written note: which do you send a CEO before a review, and
when would you switch?** "A written note under a page, each claim with its base and its caveat. I
switch to a small dashboard when the same metrics are reviewed every week, so the note only covers
what moved."

### Depth: the fact that would flip each line

A note is stronger when it says, per line, what would change it. The table is the caveat column
made explicit.
'''),
        code('''
flips_table = [("Retail-Plus", "borderline, small, watch it", "a second quarter with a larger fall, or a recovery rate from a past offer"),
               ("Student", "not yet", "thirty or more customers behind the rise, with the rise holding"),
               ("Discount", "do not repeat as designed", "a random hold-back at Diwali showing a lift inside segments")]
kit.table(["Question", "Today's line", "The fact that would flip it"], flips_table)
kit.vflow(["claim", "evidence with its base", "caveat: what would flip it", "action with its cost"], lit=2,
          title="The note's four parts, top to bottom")
kit.check("every line names the fact that would flip it", all(r[2] for r in flips_table))
'''),
        code('''
kit.check_summary()
print("Next: chapter 6, this afternoon. Who got the discount, who did not, and what else changed?")
'''),
    ]


# =========================================================================== chapter 6
def chapter6():
    return [
        md('''
# The fair comparison

**Week 1, Thursday. Chapter 6 of 6, the afternoon.** By the end of this notebook you can ask the
three questions every campaign readout needs (who got it, who did not, what else changed), see why
a before-and-after number misleads, reach the verdict a second way on a quarter with no sale, and
design the comparison that would settle it at Diwali.

> **The client asks.** "Diwali is five weeks away. I want the monsoon sale again, and I want it for
> more of the base."
>
> The marketing lead, Kalpa Retail, answering the morning's note

**The metric at stake.** Revenue from the targeted segment in the sale month, and the question
under it: what would these customers have spent without the sale? **Who asks and what rides on
it.** The marketing lead wants the Diwali budget; Meera needs to know whether a sale at 15 percent
off makes money or gives margin to customers who would have bought anyway. **Who else faces it.**
eBay stopped buying search ads on its own brand name in a controlled test and found that almost
all of the lost clicks arrived through ordinary search results instead; the researchers reported
that those ads had no measurable short-term benefit, and that the returns a controlled test showed
were a fraction of what the usual before-and-after readings had credited.

Chapter 4 split the blend by segment on the campaign platform's August list, and chapter 5 wrote the
note. The platform's list holds 160 customers under its own ids, records who received the sale
whatever it was aimed at, and cannot be matched to Finance's order file, so this chapter reads each
file for what it can answer: the platform's list for who got the sale and for sizing the Diwali
hold-back, and Finance's order file for what the months did. It adds `month_delivered` and
`month_orders`.
'''),
        md('**Setup.** The whole toolkit, plus the two month helpers.'),
        setup(T1, T2, T3, T4, T6, extra='''
MONTHS = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]
print("orders by month ready for", len(MONTHS), "months; the sale ran", CAMPAIGNS[0]["starts"], "to", CAMPAIGNS[0]["ends"])
'''),
        the_map(5, ["the options\\nbefore-after, beside, inside, hold-back",
                    "1. who got it\\nthe target against the platform's list",
                    "2. the plausible wrong answer\\nAugust against July",
                    "3. what else changed\\nthe segment beside it",
                    "4. the design\\na hold-back at Diwali",
                    "a second route\\nthe same test, no sale"]),
        md('''
## The options

Four ways a team could answer "did the sale cause the lift?". They stand on different files and
take different things on trust.

| Option | What it compares | What it assumes |
|---|---|---|
| A. Before and after | The targeted segment in August against July, in Finance's order file | Nothing else changed between the months |
| B. The change beside the change | The targeted segment's move against an untargeted segment's move over the same months | Both segments would have moved alike without the sale |
| C. Inside each segment | Customers who got it against customers who did not, in the same month, on the platform's list (chapter 4) | Who got it inside a segment was as good as random |
| D. A random hold-back | A coin decides, before the sale, which customers on the platform's list do not get it | Nothing, which is why it costs a campaign cycle |
'''),
        code('''
plus_jul, plus_aug = month_orders("Retail-Plus", "2026-07"), month_orders("Retail-Plus", "2026-08")
core_jul, core_aug = month_orders("Retail-Core", "2026-07"), month_orders("Retail-Core", "2026-08")
rp_listed = len(group("yes", "Retail-Plus")) + len(group("no", "Retail-Plus"))
held_back = rp_listed // 5
forgone = round(held_back * spend(group("no", "Retail-Plus")) * 0.06)
rows = [
    ("A. Before and after", f"Finance's file: {len(plus_jul) + len(plus_aug)} delivered orders", "the season, the tier's own drift"),
    ("B. Beside an untargeted segment", f"Finance's file: {len(plus_jul) + len(plus_aug) + len(core_jul) + len(core_aug)} delivered orders", "that the two segments move alike"),
    ("C. Inside each segment", f"the platform's list: {len(EXPOSURE)} customers", "who got it was chosen by a rule"),
    ("D. Random hold-back at Diwali", f"the platform's list: a fifth of its {rp_listed} Retail-Plus customers", f"about {kit.rupees(forgone)} forgone if Marketing's 6 percent were real"),
]
kit.table(["Option", "What it stands on", "What it risks"], rows, caption="The options sized on Kalpa's files")
kit.bars([("A. before and after", len(plus_jul) + len(plus_aug)),
          ("B. beside Retail-Core", len(plus_jul) + len(plus_aug) + len(core_jul) + len(core_aug)),
          ("C. inside each segment", len(EXPOSURE))], lit=[2],
         title="What each option stands on: orders for A and B, customers for C")
kit.check("before and after stands on fewer than thirty orders", len(plus_jul) + len(plus_aug) < 30)
'''),
        md('''
**The best-fit call: D for Diwali, with C as today's best evidence.** A and B stand on a handful of
orders a month, and chapter 3 already said what a handful is worth. C is the fairest comparison the
files hold, and it still assumes who got the sale was as good as random inside each segment. D is
the only option where a coin decides, and its cost is small: if Marketing's 6 percent were real,
holding back a fifth of the platform's Retail-Plus customers forgoes a few thousand rupees. **The
fact that would change the call.** A campaign so large, or a hold-back so politically hard, that
the forgone lift runs into lakhs: then B, on a longer run of months, becomes the working answer with
its caveat said aloud.
'''),
        md('''
## 1. Who got it

The campaigns table says whom the sale was aimed at, which is the plan; the platform's list records
who received it, whatever it was aimed at, so where the two disagree the list is the one to trust for
who got the sale.

**Predict before you run.** Of the customers who got the monsoon sale, the share who are
Retail-Plus members is: a) all of them, since it targeted Retail-Plus; b) about half; c) about a
tenth; d) none.
'''),
        code('''
got = {s: len(group("yes", s)) for s in ["Retail-Plus", "Retail-Core"]}
kit.columns(list(got), [("customers who got the sale", list(got.values()))], width=520,
            title=f"Target: {CAMPAIGNS[0]['target_segment']}. Received by:")
print(f"target {CAMPAIGNS[0]['target_segment']}; received by {got}")
kit.check("the sale reached customers outside its target segment", got["Retail-Core"] > 0, f"{got}")
kit.check("the platform's list covers both segments' customers", sum(got.values()) == len(group("yes")))
'''),
        md('''
**What happened.** The answer is b. The sale was aimed at Retail-Plus and half of the customers who
got it were Retail-Core. Whatever chose them was a rule, and a rule can pick the customers who were
going to buy anyway. That is the first of the three questions, and it is already an answer: the
groups were chosen.

## 2. The plausible wrong answer

**The plausible wrong answer.** A hurried readout opens Finance's order file and compares
Retail-Plus in the sale month with the month before.
'''),
        code('''
rp_jul, rp_aug = month_delivered("Retail-Plus", "2026-07"), month_delivered("Retail-Plus", "2026-08")
before_after = rp_aug / rp_jul - 1
draft = (f"Retail-Plus delivered {kit.rupees(rp_aug)} in August against {kit.rupees(rp_jul)} in July, "
         f"up {before_after:.0%}: the monsoon sale worked, so run it for more of the base at Diwali.")
print(draft)
'''),
        md('''
**Why it is wrong.** A before-and-after number credits the sale with everything else that happened
between July and August, and it stands on a handful of orders. If the draft wins, Diwali's sale is
widened on a jump that may belong to the month. **The check** asks what else changed: put the
untargeted segment beside it over the same months, and count what each month stands on.

## 3. What else changed

**Predict before you run.** Between July and August, Retail-Core's delivered revenue: a) fell, as
the sale pulled buyers to Retail-Plus; b) stayed flat; c) rose by a large share as well; d) cannot
be compared.
'''),
        code('''
rp = [month_delivered("Retail-Plus", m) for m in MONTHS]
core = [month_delivered("Retail-Core", m) for m in MONTHS]
kit.line(["Apr", "May", "Jun", "Jul", "Aug", "Sep"], [("Retail-Plus", rp, "bad"), ("Retail-Core", core, "plain")],
         fmt=kit.rupees, title="Delivered revenue by month: both segments jump in August, and both swing without any sale")
core_jump = core[4] / core[3] - 1
may_june = rp[2] / rp[1] - 1
kit.table(["Segment", "July", "August", "Change", "Delivered orders, July / August"],
          [("Retail-Plus", kit.rupees(rp[3]), kit.rupees(rp[4]), f"{before_after:+.0%}", f"{len(plus_jul)} / {len(plus_aug)}"),
           ("Retail-Core", kit.rupees(core[3]), kit.rupees(core[4]), f"{core_jump:+.0%}", f"{len(core_jul)} / {len(core_aug)}")],
          caption="July against August, with the orders behind each month")
print(f"Retail-Plus May to June, no sale running: {may_june:+.0%}")
kit.check("the untargeted segment also jumped in August", core_jump > 0.5, f"{core_jump:+.0%}")
kit.check("Retail-Plus swung by more than half between two months with no sale", abs(may_june) > 0.5, f"{may_june:+.0%}")
kit.check("July's Retail-Plus figure stands on fewer than ten orders", len(plus_jul) < 10, f"{len(plus_jul)}")
'''),
        md('''
**What happened.** The answer is c. Retail-Core rose 73 percent from July to August although the
sale was aimed elsewhere, and Retail-Plus fell 58 percent from May to June with no sale at all. A
month's revenue on a few orders swings by half on its own, and August was a big month for both
segments.

**The fix.** Compare like with like in time as well: take August's share of each segment's
quarter, then ask how often chance alone makes a gap that large between the two segments, dealing
the segment labels at random across both segments' delivered Q2 orders. These are different
customers in each segment, so the labels are shuffled, as chapter 1's options table said they would
be. As in chapter 1, both directions are reported, since neither direction was fixed before August
was seen: a gap that large either way, and a Retail-Plus share that much higher, which is the
direction Marketing's claim points.
'''),
        code('''
def month_share_test(months, target, times=5000, seed=2026):
    """The target month's share of each segment's quarter, and how often shuffled segment labels make that gap."""
    plus = [month_delivered("Retail-Plus", m) for m in months]
    other = [month_delivered("Retail-Core", m) for m in months]
    at = months.index(target)
    gap = plus[at] / sum(plus) - other[at] / sum(other)
    rows = ([(int(o["amount"]), o["order_date"][:7]) for m in months for o in month_orders("Retail-Plus", m)]
            + [(int(o["amount"]), o["order_date"][:7]) for m in months for o in month_orders("Retail-Core", m)])
    n_plus = sum(len(month_orders("Retail-Plus", m)) for m in months)

    def share(part):
        return sum(a for a, m in part if m == target) / sum(a for a, _ in part)

    random.seed(seed)
    chance = []
    for _ in range(times):
        random.shuffle(rows)                      # deal the segment labels at random
        chance.append(share(rows[:n_plus]) - share(rows[n_plus:]))
    either = sum(1 for c in chance if abs(c) >= abs(gap)) / times
    up = sum(1 for c in chance if c >= gap) / times
    return plus[at] / sum(plus), other[at] / sum(other), gap, either, up, chance


aug_share_rp, aug_share_core, real_gap, chance_either, chance_up, chance = month_share_test(MONTHS[3:], "2026-08")
kit.strip(chance[:200], markers=[("real gap", real_gap, "bad")], lo=-0.5, hi=0.5, fmt=lambda v: f"{v:+.0%}",
          title="Targeted less untargeted August share, in 200 deals of the segment labels, with the real gap marked")
print(f"August's share of Q2: Retail-Plus {aug_share_rp:.1%}, Retail-Core {aug_share_core:.1%}, a gap of "
      f"{100 * real_gap:.1f} points; shuffled labels make a gap that large either way in {chance_either:.2f} of deals, "
      f"and a Retail-Plus share that much higher in {chance_up:.2f}")
kit.check("August's share is within a few points for the targeted and the untargeted segment",
          abs(aug_share_rp - aug_share_core) < 0.06, f"{aug_share_rp:.1%} against {aug_share_core:.1%}")
kit.check("counting either way, 4,124 of 5,000 deals make the gap (seed 2026)", round(chance_either * 5000) == 4124, f"{chance_either:.4f}")
kit.check("counting Marketing's direction only, 2,006 of 5,000 do", round(chance_up * 5000) == 2006, f"{chance_up:.4f}")
'''),
        md('''
What changed: the jump of 170 percent becomes an August that took 52 percent of Retail-Plus's
quarter against 49 percent of Retail-Core's, about four points apart, and shuffling the segment
labels makes a gap that large either way in about eight deals in ten, and a gap that large in
Marketing's direction in about four in ten. The month file shows no sign of the sale beyond a busy
August for everyone. One more caveat keeps this honest: Retail-Core is the segment the sale was not
aimed at, yet step 1 showed the platform's list counting Retail-Core customers among those who got
it. If the sale lifted both segments, similar Augusts would look like this too, so Retail-Core is an
imperfect comparison, which is one more reason only a coin can settle it.

## 4. The design: a hold-back at Diwali

The only comparison that answers "would they have bought anyway?" is one where a coin decides who
gets the sale. Decide before the sale, inside each segment of the platform's list, and agree the
measure and the window in advance.

**Predict before you run.** If Marketing's 6 percent were the true lift, holding back a random
fifth of the platform's Retail-Plus customers would forgo about: a) Rs 4,000; b) Rs 40,000; c) Rs 4
lakh; d) nothing, since held-back customers still buy.
'''),
        code('''
kit.vflow(["before Diwali: list each segment's customers on the platform",
           "a coin per customer: one in five held back",
           "the sale runs for the rest, same window",
           "after: spend per customer, held back against got it, inside each segment",
           "the label shuffle on the gap, both directions reported"],
          lit=1, title="The Diwali comparison, decided before the sale")
finance_members = len({o["customer_id"] for o in ORDERS if o["segment"] == "Retail-Plus"})
finance_aug = month_delivered("Retail-Plus", "2026-08") / finance_members
kit.table(["List", "Retail-Plus customers", "August, per customer", "What it sizes"],
          [("the platform's August list", rp_listed, kit.rupees(spend(group("no", "Retail-Plus"))) + " spend, not exposed", "the Diwali hold-back"),
           ("Finance's order file", finance_members, kit.rupees(finance_aug) + " delivered", "the retention offer")],
          caption="Two lists, two sizes: each decision is sized on the list it acts on")
kit.stats([(f"{held_back}", "held back", f"a fifth of the platform's {rp_listed} Retail-Plus customers"),
           (kit.rupees(forgone), "forgone", "if Marketing's 6 percent were real"),
           ("0", "rupees of discount", "given to the held-back customers")])
kit.check("the hold-back forgoes under Rs 10,000 even at Marketing's own lift", forgone < 10000, kit.rupees(forgone))
kit.check("the two lists hold different numbers of Retail-Plus customers", rp_listed != finance_members,
          f"{rp_listed} against {finance_members}")
'''),
        md('''
**What happened.** The answer is a. Fourteen held-back Retail-Plus customers at Rs 5,000 each and a
6 percent lift is about Rs 4,200, the cost of the hold-back, and nothing if the lift is not real.

**Two lists, met head-on.** The morning priced the retention offer on "the whole tier" of 22 and
tests it on a coin-chosen half of them, and this hold-back takes 14 of 70. Both are right, because
they are different lists. The 22 are
Finance's order file, where Retail-Plus members delivered about Rs 1,139 each in August; the 70 are
the platform's list, where Retail-Plus customers who did not get the sale averaged Rs 5,000. The
lists use different ids and different measures, delivered revenue per member in Finance's file and
the platform's own average spend per customer, so neither number can check the other. Each decision
is sized on the list it acts on: the offer on Finance's members, the hold-back on the platform's
customers.

Fourteen customers are too few to measure a lift as small as 6 percent, since spend swings far more
than that from customer to customer; how many a hold-back needs is a question of power, which comes
in a later week, and the honest design holds back a random slice of every segment the sale reaches.

## A second route: the same test on a quarter with no sale

Step 3 read August's four points against shuffled labels. A placebo checks the reading from outside
it: run the same month-share test on the three months of Q1, when no sale ran. If months with no sale
produce gaps as large as August's, or larger, then August's gap carries no sign of the sale. This
route uses a different quarter of Finance's file and shares nothing with chapter 4's split.

**Predict before you run.** Across April, May and June, the gaps between the two segments' monthly
shares will be: a) all near zero, since no sale ran; b) about as large as August's, or larger; c)
larger only in the month before a sale; d) impossible to compute without a sale.
'''),
        code('''
placebo = {m: month_share_test(MONTHS[:3], m) for m in MONTHS[:3]}
labels = ["Apr, no sale", "May, no sale", "Jun, no sale", "Aug, the sale"]
gaps = [abs(100 * placebo[m][2]) for m in MONTHS[:3]] + [abs(100 * real_gap)]
kit.columns(labels, [("gap between the segments' shares, points", [round(g, 1) for g in gaps])], lit=[3],
            fmt=lambda v: f"{v:.1f}", width=680, title="The same test on months with no sale, beside August")
kit.table(["Month", "Retail-Plus share", "Retail-Core share", "Gap, points", "Either way", "Retail-Plus higher"],
          [(m, f"{p[0]:.1%}", f"{p[1]:.1%}", f"{100 * p[2]:+.1f}", f"{p[3]:.3f}", f"{p[4]:.3f}") for m, p in placebo.items()]
          + [("2026-08", f"{aug_share_rp:.1%}", f"{aug_share_core:.1%}", f"{100 * real_gap:+.1f}", f"{chance_either:.3f}", f"{chance_up:.3f}")],
          caption="Each month's share of its own quarter, with how often shuffled labels make that gap")
kit.check("every month of the quarter with no sale shows a gap at least as large as August's",
          all(abs(p[2]) >= abs(real_gap) for p in placebo.values()), f"{[round(100 * p[2], 1) for p in placebo.values()]}")
kit.check("the largest no-sale gap is more than five times August's", max(abs(p[2]) for p in placebo.values()) > 5 * abs(real_gap))
'''),
        md('''
**What happened.** The answer is b. In the quarter with no sale, the gaps between the segments'
monthly shares run 4, 22 and 26 points, and shuffled labels make May's and June's gaps in about 15
and 7 deals in 100 counting either way. Months with no sale produce gaps as large as August's four
points and far larger, so August's gap carries no sign of the sale. Chapter 4's split, on the
platform's list, found the exposed spending 3 percent less in both segments: neither route shows
the lift Marketing claimed, and neither is a fair comparison, because nobody tossed a coin. That is
why the line to Meera stays "do not repeat it as designed" and the action is the hold-back. **When to
switch.** Use the change beside the change when months of data exist and no hold-back was run; use
the split when an exposure list exists; run the hold-back whenever the next campaign can still be
designed.

> **Kavya's review.** "Who got it: a rule chose them. Who did not: a different mix. What else
> changed: August, for everyone, and a quarter with no sale swings further. Two routes find no lift,
> and you priced the hold-back at about Rs 4,200 on the list it acts on. Take that to Marketing as an
> offer, and keep any verdict on their work out of it."

### In the interview

**[F] Revenue rose after a discount; did the campaign work, and what would you need to know?** "Three
things: who got it, who did not, and what else changed. A before-and-after number credits the
campaign with the season. I would compare against customers who did not get it in the same window,
inside each segment, run the same test on months with no campaign to see what an ordinary month
does, and ask for a random hold-back next time, because that is the only comparison where the
customers who would have bought anyway are in both groups."

**[F] How would you set up the Diwali campaign so you can tell whether it worked?** "Before the sale,
a coin per customer inside each segment holds back about one in five. Agree the measure, the window
and the direction of the test in advance, run the sale for the rest, then compare spend per customer
inside each segment and test the gap against chance. At Marketing's own claimed lift the hold-back
costs a few thousand rupees, and the size of the hold-back is set by how small a lift we need to see,
which is a later week's question."

**[S] What is a confounder? Give an example from a campaign.** "Something that differs between the
groups and moves the outcome on its own. Here the sale went to a group with more high-spending
Retail-Plus members, and August was a big month for everyone, so both the mix and the month move
revenue whether or not the sale did anything."

**[D] Before and after, the change beside the change, the split, or a hold-back: which would you
defend to a CFO, and when would you settle for less?** "The hold-back, because only a coin removes
the customers who would have bought anyway from the comparison. I would settle for the change
beside the change on a long run of months when a hold-back is impossible, and say its assumption
aloud: that both segments would have moved alike."

### Depth: the change beside the change, named

Analysts call option B a difference in differences: the targeted segment's change less the
untargeted segment's change over the same window. Here it is in rupees, and why it cannot settle
this question.
'''),
        code('''
did = (rp[4] - rp[3]) - (core[4] - core[3])
kit.bridge(("Retail-Plus, July to August", rp[4] - rp[3]), [("less Retail-Core's move", -(core[4] - core[3]))],
           end_label="the change beside the change", title="The difference in differences, in rupees, on a handful of orders a month")
print(f"Retail-Plus moved {kit.rupees(rp[4] - rp[3])}, Retail-Core {kit.rupees(core[4] - core[3])}; difference {kit.rupees(did)}")
kit.check("the difference rests on fewer than thirty orders in the targeted segment", len(plus_jul) + len(plus_aug) < 30)
'''),
        md('''
It says Retail-Plus rose about Rs 6,000 more than Retail-Core, on 13 orders across the two months,
from a segment whose months swing by half with no sale running. The route assumes the two segments
move alike without the sale, and the months before it say they do not: from May to June Retail-Plus
fell 58 percent while Retail-Core rose 63 percent. That makes it a lead to follow up, and it points
the same way as everything else in this chapter: run the hold-back.
'''),
        code('''
kit.check_summary()
print("Next: the escalated case. Everything the six chapters built, alone, on all three questions.")
'''),
    ]


BUILDERS = {1: ("01_real_or_wobble", chapter1), 2: ("02_worth_acting_on", chapter2),
            3: ("03_count_behind_the_rate", chapter3), 4: ("04_discount_by_segment", chapter4),
            5: ("05_the_note", chapter5), 6: ("06_fair_comparison", chapter6)}

if __name__ == "__main__":
    wanted = [int(a) for a in sys.argv[1:]] or list(BUILDERS)
    for n in wanted:
        stem, fn = BUILDERS[n]
        path = OUT / f"C2_W01_D04_{stem}_STUDENT.ipynb"
        nb = build(path, fn(), timeout=300)
        print(f"built {path.name}: {len(nb.cells)} cells")

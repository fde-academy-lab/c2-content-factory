"""Write and execute the six chapter notebooks of Week 1 Thursday.

Run from the repository root:

    python3 content/W01/D4/internal/C2_W01_D04_build_notebooks_INTERNAL.py          # all six
    python3 content/W01/D4/internal/C2_W01_D04_build_notebooks_INTERNAL.py 3 4      # some

Each notebook is assembled by scripts/nb_make.py and executed cold in its own folder, so the saved
outputs are the ones a learner's Codespace produces. Each one carries forward the helpers of the
notebook before it and adds one, which is how the toolkit grows across the day.
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
import random
import time

ORDERS = kit.load_csv("C2_W01_D04_orders_STUDENT.csv")
SEGMENTS = ["Retail-Core", "Retail-Plus", "Student", "Business"]


def mean(values):
    return sum(values) / len(values)


def member_totals(segment, quarter):
    """Delivered revenue per member of one segment in one quarter, one number per member."""
    members = sorted({o["customer_id"] for o in ORDERS if o["segment"] == segment})
    totals = {m: 0 for m in members}
    for o in ORDERS:
        if o["segment"] == segment and o["quarter"] == quarter and o["status"] == "delivered":
            totals[o["customer_id"]] += int(o["amount"])
    return [totals[m] for m in members]


def shuffle_gaps(q1, q2, times, seed):
    """Deal the pooled values to two piles at random, many times, and keep each gap."""
    random.seed(seed)                  # the same shuffles on every laptop
    pool = q1 + q2                     # all the cards, labels ignored
    gaps = []
    for _ in range(times):
        random.shuffle(pool)           # deal at random
        gaps.append(mean(pool[:len(q1)]) - mean(pool[len(q1):]))
    return gaps


def share_at_least(gaps, real):
    """The share of chance-only worlds whose gap is at least as large as the real one."""
    return sum(1 for g in gaps if g >= real) / len(gaps)
'''

T2 = '''

def delivered(segment, quarter):
    """A segment's delivered revenue in one quarter, in rupees."""
    return sum(int(o["amount"]) for o in ORDERS
               if o["segment"] == segment and o["quarter"] == quarter and o["status"] == "delivered")


def bootstrap_gaps(q1, q2, times, seed):
    """Redraw each quarter's members with replacement, many times, and keep each gap."""
    random.seed(seed)
    return [mean([random.choice(q1) for _ in q1]) - mean([random.choice(q2) for _ in q2])
            for _ in range(times)]
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
    """August revenue per customer across a list of exposure rows."""
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

**Week 1, Thursday. Chapter 1 of 6.** By the end of this notebook you can run a shuffle test on
two quarters, read its share as a p-value, choose between four ways of asking "is it real?", and
reach the same verdict a second way.

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
studied it, about nine in ten of its experiments improve nothing, so every change there is read against
what chance alone produces before anyone acts (the sources are in the study notes).

Wednesday reconciled the quarters with Finance and left Retail-Plus standing, but smaller. This
chapter asks whether what is left is bigger than chance makes on its own.
'''),
        md('''
**Setup.** Find the helper and load the cleaned two quarters. Three helpers start the day's
toolkit: `member_totals` turns orders into one number per member, `shuffle_gaps` deals the numbers
to two piles at random, and `share_at_least` counts how many chance-only worlds match the real gap.
Every later chapter carries these forward and adds one of its own.
'''),
        setup(T1, extra='''
print(len(ORDERS), "orders,", len({o["customer_id"] for o in ORDERS}), "customers, two quarters")
'''),
        the_map(0, ["the options\\nfour ways to ask 'is it real?'",
                    "1. ten cards\\na gap of Rs 880 by hand",
                    "2. Retail-Core\\nwhat the usual wobble looks like",
                    "3. Retail-Plus\\nthe gap Meera asked about",
                    "4. the plausible wrong answer\\nwhat a p-value never says",
                    "a second route\\nthe textbook test"]),
        md('''
## The options

Four ways a team could answer "is the fall real?" before Monday. The sizing cell below times each
one on this file and names what it risks.

| Option | What it does | What it needs |
|---|---|---|
| A. Shuffle test | Deal the quarter labels at random thousands of times and count how often chance makes a gap this large | The member totals and a loop |
| B. Textbook two-sample test | One library call that returns a p-value from a formula about bell-shaped data | A statistics library, and data that behaves like a bell curve |
| C. Bootstrap interval | Redraw each quarter's members many times and read the range of gaps | A loop, and a stakeholder who reads a range |
| D. Wait for Q3 | Look again when another quarter has landed | Thirteen weeks, and a Monday meeting with no answer |
'''),
        code('''
plus_q1, plus_q2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
real = mean(plus_q1) - mean(plus_q2)

t0 = time.perf_counter(); a = share_at_least(shuffle_gaps(plus_q1, plus_q2, 5000, seed=2026), real); t_a = time.perf_counter() - t0
from scipy import stats                                   # the textbook route, named today and taught later
t0 = time.perf_counter(); b = stats.ttest_ind(plus_q1, plus_q2, equal_var=False, alternative="greater").pvalue; t_b = time.perf_counter() - t0
t0 = time.perf_counter()
random.seed(2026)
boot = sorted(mean([random.choice(plus_q1) for _ in plus_q1]) - mean([random.choice(plus_q2) for _ in plus_q2]) for _ in range(5000))
t_c = time.perf_counter() - t0
zeros = sum(1 for v in plus_q1 + plus_q2 if v == 0)

rows = [
    ("A. Shuffle test", f"{len(plus_q1) * 2} member totals x 5,000 deals", f"{t_a:.2f} s", "the share moves a few thousandths between seeds"),
    ("B. Textbook test", f"{len(plus_q1) * 2} member totals, one call", f"{t_b:.3f} s", f"assumes bell-shaped totals; {zeros} of 44 are zero"),
    ("C. Bootstrap interval", f"{len(plus_q1) * 2} member totals x 5,000 redraws", f"{t_c:.2f} s", "answers how big, and says less about how rare"),
    ("D. Wait for Q3", "22 more member-quarters", "one quarter", "Monday passes with no answer"),
]
kit.table(["Option", "Rows it touches", "Time on this file", "What it risks"], rows,
          caption="The four options sized on Kalpa's file")
kit.bars([("A. Shuffle", round(t_a * 1000)), ("B. Textbook", max(1, round(t_b * 1000))),
          ("C. Bootstrap", round(t_c * 1000))], fmt=lambda v: f"{v:,} ms",
         title="Compute time on this file, in milliseconds: every option is instant at this size")
kit.check("the three computed options each finish in under five seconds", max(t_a, t_b, t_c) < 5)
'''),
        md('''
**The best-fit call for Meera's Monday: A, the shuffle test.** At 44 member totals every option
runs in well under a second, so compute decides nothing. What decides is the file and the reader:
eight of the 44 member totals are zero (six members bought nothing in Q2 and two nothing in
Q1), which is exactly the lumpy shape B's formula
assumes away, and the shuffle can be explained to Meera with ten cards on a table. C comes in
chapter 2, where the question becomes how big. D costs a quarter for a question the data can
already answer.

**The fact that would change the call.** Tens of thousands of members a quarter and a metric that
behaves, which is what a dashboard at Booking.com's scale sees: B then gives the same answer in
one line and is the house standard. And if the shuffle came back unclear, D becomes the honest
answer, because more members is the only thing that sharpens it.
'''),
        md('''
## 1. Ten cards: is a gap of Rs 880 surprising?

Five members' Q1 spend and five members' Q2 spend, **invented for the table**, in rupees. The real
gap is the Q1 mean less the Q2 mean. If the quarter made no difference, the labels are arbitrary:
shuffle the ten cards, deal five to each pile, and the gap you get is one chance-only world. The
room does this by hand before this cell runs.

**Predict before you run.** Out of 1,000 shuffles, how many make a gap of Rs 880 or more?
a) about 500, since half of all gaps are positive; b) about 200; c) about 20; d) none, since 880 is
the real gap and shuffling destroys it.
'''),
        code('''
q1_cards = [3400, 2900, 4100, 2500, 3800]
q2_cards = [2200, 3100, 1900, 2700, 2400]
card_gap = mean(q1_cards) - mean(q2_cards)
card_gaps = shuffle_gaps(q1_cards, q2_cards, 1000, seed=2026)
card_share = share_at_least(card_gaps, card_gap)

print(f"Q1 mean Rs {mean(q1_cards):,.0f}, Q2 mean Rs {mean(q2_cards):,.0f}, real gap Rs {card_gap:,.0f}")
print("the first ten shuffled gaps:", [round(g) for g in card_gaps[:10]])
kit.strip(card_gaps[:150], markers=[("real gap", card_gap, "bad")], lo=-1500, hi=1500,
          title="150 of the 1,000 shuffled gaps on the ten cards, with the real gap marked")
kit.stats([("1,000", "shuffles", "the same ten cards"),
           (f"{round(card_share * 1000)}", "gaps of Rs 880 or more", "in chance-only worlds"),
           (f"{card_share:.3f}", "the share", "this is the p-value")])
'''),
        md('''
**What happened.** The answer is c. Twenty-one shuffles in a thousand reached Rs 880, a share of
0.021. Ten hand shuffles showed one in ten, which is why ten is too few: a share needs hundreds of
worlds before it settles. The dots pile up around zero, because most deals mix big and small cards
into both piles, and the real gap sits out on the right edge of the pile.
'''),
        code('''
kit.check("the real gap on the cards is Rs 880", round(card_gap) == 880, f"{card_gap:,.0f}")
kit.check("21 of 1,000 shuffles reach it, with seed 2026", round(card_share * 1000) == 21, f"{card_share:.3f}")
'''),
        md('''
## 2. Retail-Core: what the usual wobble looks like

Before judging Retail-Plus, see an ordinary quarter. Retail-Core members also spent a little less
in Q2. The measure is the day's: delivered revenue per member, one number per member, with a zero
for a member who had no delivered order that quarter.

**Predict before you run.** Retail-Core fell by about Rs 110 per member. What share of 5,000
shuffles will make a gap at least that large? a) under 0.01; b) about 0.05; c) about a third;
d) all of them.
'''),
        code('''
core_q1, core_q2 = member_totals("Retail-Core", "Q1"), member_totals("Retail-Core", "Q2")
core_gap = mean(core_q1) - mean(core_q2)
core_gaps = shuffle_gaps(core_q1, core_q2, 5000, seed=2026)
core_share = share_at_least(core_gaps, core_gap)
kit.strip(core_gaps[:150], markers=[("real gap", core_gap, "bad")], lo=-1200, hi=1200,
          title="Retail-Core: 150 of the 5,000 shuffled gaps, with the real gap marked")
print(f"{len(core_q1)} members, Q1 Rs {mean(core_q1):,.0f}, Q2 Rs {mean(core_q2):,.0f}, "
      f"gap Rs {core_gap:,.0f}; share at least as large {core_share:.3f}")
'''),
        md('''
**What happened.** The answer is c. About a third of chance-only worlds make a fall of Rs 110 or
more, so Retail-Core's dip is what Meera calls the usual wobble: the real gap sits inside the pile.
Keep this picture, because it is what "nothing happened" looks like.
'''),
        code('''
kit.check("Retail-Core has 34 members in both quarters", len(core_q1) == len(core_q2) == 34)
kit.check("chance makes Retail-Core's gap often", core_share > 0.25, f"{core_share:.3f}")
'''),
        md('''
## 3. Retail-Plus: the gap Meera asked about

The same loop, pointed at the segment in Meera's question.

**Predict before you run.** Compared with Retail-Core's share of about a third, Retail-Plus's share
will be: a) about the same; b) larger, since Retail-Plus is a smaller segment; c) much smaller, if
its fall is bigger than chance makes; d) impossible to compute, since some members have zeros.
'''),
        code('''
plus_gaps = shuffle_gaps(plus_q1, plus_q2, 5000, seed=2026)
plus_share = share_at_least(plus_gaps, real)
kit.columns(["Q1", "Q2"], [("per member, Rs", [round(mean(plus_q1)), round(mean(plus_q2))])],
            fmt=kit.rupees, width=520, title=f"Retail-Plus, {len(plus_q1)} members: delivered revenue per member")
kit.strip(plus_gaps[:200], markers=[("real gap", real, "bad")], lo=-2500, hi=2500,
          title="Retail-Plus: 200 of the 5,000 shuffled gaps, with the real gap marked")
print(f"real gap Rs {real:,.0f}; {round(plus_share * 5000)} of 5,000 at least as large; share {plus_share:.3f}")
'''),
        md('''
**What happened.** The answer is c. Retail-Plus members delivered Rs 3,279 each in Q1 and Rs 2,169
in Q2, a fall of Rs 1,110 per member. Only 135 of 5,000 shuffles made a fall that large, a share of
0.027, which reads as 0.03 to two places. Against Retail-Core's third, this is a gap chance rarely
makes, so the first line of the note can say the fall is larger than the usual wobble.
'''),
        code('''
kit.check("Retail-Plus has 22 members in both quarters", len(plus_q1) == len(plus_q2) == 22)
kit.check("the Retail-Plus gap is Rs 1,110 a member", round(real) == 1110, f"{real:.1f}")
kit.check("with seed 2026, 135 of 5,000 shuffles reach it", round(plus_share * 5000) == 135, f"{plus_share:.4f}")
kit.check("Retail-Plus beats the wobble that Retail-Core sits inside", plus_share < 0.05 < core_share)
'''),
        md('''
## 4. The plausible wrong answer

**The plausible wrong answer.** The hurried draft turns the share straight into a sentence about
being wrong. Here it is, computed exactly the way it gets written, and the decision it invites is
Meera treating the fall as 97 percent certain and funding a fix on that basis.
'''),
        code('''
draft = f"p = {plus_share:.2f}, so there is a {plus_share:.0%} chance we are wrong about the drop."
print(draft)
'''),
        md('''
**Why it is wrong.** Every one of the 5,000 shuffles was dealt in a world where the quarter made no
difference. The share counts how often *that* world makes a fall this large. It says nothing about
the chance that this finding is wrong, which depends on things the shuffle never saw: how plausible
a fall was before the data, what else changed, and how many segments were tested.

**The check.** Build twenty **invented** segments in which nothing changed at all, both quarters
drawn from the same range, and run the same test on each. Any segment that comes back small is a
finding that is wrong for certain, whatever its share says.
'''),
        code('''
invented_shares = []
for s in range(20):
    maker = random.Random(100 + s)                       # invented members, same range both quarters
    values = [maker.randint(1500, 4500) for _ in range(40)]
    q1, q2 = values[:20], values[20:]
    invented_shares.append(share_at_least(shuffle_gaps(q1, q2, 1000, seed=2026), mean(q1) - mean(q2)))

small = [p for p in invented_shares if p <= 0.05]
kit.bars([(f"segment {i + 1}", round(p, 3)) for i, p in enumerate(invented_shares)],
         lit=[i for i, p in enumerate(invented_shares) if p <= 0.05], fmt=lambda v: f"{v:.3f}",
         title="Twenty invented segments where nothing changed; one came back small anyway")
print(f"{len(small)} of 20 came back at 0.05 or below: {small}")
'''),
        md('''
One invented segment came back at 0.005 although nothing happened in it. Its draft note would say
"a 0.5 percent chance we are wrong", and it would be wrong with certainty.

**The fix.** Say the share, the world it was counted in, and what it lets you conclude.
'''),
        code('''
fixed = (f"If nothing had changed between the quarters, a fall of Rs {real:,.0f} per member or more "
         f"would turn up in about {round(plus_share * 100)} of every 100 shuffles, so we treat the Retail-Plus drop as real.")
print(fixed)
kit.flow(["the share\\n" + f"{plus_share:.3f}", "the world\\nnothing changed", "the conclusion\\nbeats the wobble",
          "next question\\nhow big is it?"], lit=2, title="The sentence a p-value supports, in order")
kit.check("the fixed sentence names the chance-only world", fixed.startswith("If nothing had changed"))
kit.check("one of twenty no-change segments still came back small", len(small) == 1, f"{small}")
'''),
        md('''
What changed: the number is the same 0.027, and the claim shrank from "97 percent certain" to
"larger than the usual wobble". That is the claim the evidence carries.

## A second route: the textbook test

Option B, run now as the cross-check. The library call is the two-sample test a statistics course
teaches first; its formula is for a later week, and today it is a second opinion.

**Predict before you run.** The textbook test's p-value for Retail-Plus will be: a) about 0.03, the
same verdict; b) about 0.3, the opposite verdict; c) exactly 0.027, since it is the same method;
d) impossible, since the totals are not bell-shaped.
'''),
        code('''
text_plus = stats.ttest_ind(plus_q1, plus_q2, equal_var=False, alternative="greater").pvalue
text_core = stats.ttest_ind(core_q1, core_q2, equal_var=False, alternative="greater").pvalue
kit.columns(["Retail-Core", "Retail-Plus"],
            [("shuffle test", [round(core_share, 3), round(plus_share, 3)]),
             ("textbook test", [round(text_core, 3), round(text_plus, 3)])],
            fmt=lambda v: f"{v:.3f}", width=620, title="Two routes to the same verdict: the share for each segment")
print(f"Retail-Plus: shuffle {plus_share:.3f}, textbook {text_plus:.3f}; Retail-Core: shuffle {core_share:.3f}, textbook {text_core:.3f}")
kit.check("the two routes agree on Retail-Plus within a hundredth", abs(text_plus - plus_share) < 0.01,
          f"{plus_share:.3f} against {text_plus:.3f}")
kit.check("the two routes agree on Retail-Core's verdict", text_core > 0.25 and core_share > 0.25)
'''),
        md('''
**What happened.** The answer is a. The textbook test says 0.026 where the shuffle said 0.027, and
both put Retail-Core near a third. Two routes built on different ideas reach one verdict, so the
note can carry it. **When to switch.** Use the textbook call when the data is large and
well-behaved and a team standard expects it; keep the shuffle when the data is small or lumpy, or
when the person reading the answer needs to see how it was made.

> **Kavya's review.** "Retail-Core's third is the baseline, Retail-Plus's 0.03 is the gap against
> it, the textbook test agrees, and your sentence would still be true if the drop turned out to be
> a fluke. Now tell me how much money it is."

### In the interview

**[S] What does p = 0.03 mean, and not mean?** "It means that if there were no real difference, a
difference at least as large as the one we saw would turn up about 3 times in 100 by chance alone.
It does not mean there is a 3 percent chance the finding is wrong, and it does not say the effect is
large or worth acting on. I say it as: chance rarely makes a gap this big, so I treat it as real,
and then I size it." The interviewer is listening for the conditional, "if there were no
difference", and for the refusal to call it the probability of being wrong.

**[S] How do you know whether a change in a metric is significant?** "I build a reference for what
chance alone does. The simplest is a shuffle test: pool the values from the two periods, deal them
back at random thousands of times, and see how often the shuffled gap is as large as the real one.
If that share is small, the change is bigger than the usual wobble. Then I check the count behind it
and size it in money, because significant only means larger than noise." A sharp follow-up: the
same 22 members sit in both quarters, so the data are paired. Flipping the sign of each member's own
Q1 less Q2 difference is the paired shuffle, and it gives about the same share here (the extras sheet
runs it), because a member's Q1 spend barely predicts their Q2 spend in this file.

**[D] A shuffle test, a textbook test, or wait a quarter: which do you run for a CEO's Monday, and
what would make you switch?** "On a few dozen customers with lumpy spend, the shuffle: it runs in a
second, assumes nothing about shape and I can show it with cards. I cross-check with the textbook
test. I would make the textbook test the default on large, well-behaved data, and I would wait a
quarter only if both came back unclear, because then more data is the only thing that helps."

### Depth: one direction or both

The chapter counted falls at least as large, because Meera asked about a drop. Counting falls *or*
rises at least as large asks whether chance makes a move this big in either direction, and it
roughly doubles the share. A note that tested both directions says so.
'''),
        code('''
both = sum(1 for g in plus_gaps if abs(g) >= abs(real)) / len(plus_gaps)
seeds = [round(share_at_least(shuffle_gaps(plus_q1, plus_q2, 5000, seed=s), real), 4) for s in (1, 2, 3, 4, 5)]
kit.line([f"seed {s}" for s in (1, 2, 3, 4, 5)], [("one-direction share", seeds, "plain")], lo=0,
         fmt=lambda v: f"{v:.3f}", title="The Retail-Plus share under five other seeds: it moves a little and the verdict never")
print(f"both directions {both:.3f}; five seeds {seeds}")
kit.check("counting both directions roughly doubles the share", 1.6 < both / plus_share < 2.4, f"{both:.3f}")
kit.check("another seed never changes the verdict", all(0.02 < s < 0.035 for s in seeds), f"{seeds}")
'''),
        code('''
kit.check_summary()
print("Next: chapter 2. The drop beats the wobble; is it worth acting on?")
'''),
    ]


# =========================================================================== chapter 2
def chapter2():
    return [
        md('''
# Real, and worth acting on?

**Week 1, Thursday. Chapter 2 of 6.** By the end of this notebook you can size a real gap in rupees
against the segment, the company and the cost of acting, keep "significant" and "important" in two
separate sentences, and read a bootstrap range as the second route.

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

Chapter 1 established that the Retail-Plus fall, Rs 1,110 per member, is bigger than the usual
wobble, and the textbook test agreed. This chapter adds two helpers: `delivered`, a segment's
revenue in a quarter, and `bootstrap_gaps`, the range the second route reads.
'''),
        md('**Setup.** The toolkit from chapter 1, plus the two new helpers.'),
        setup(T1, T2, extra='''
plus_q1, plus_q2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
real = mean(plus_q1) - mean(plus_q2)
print(f"{len(plus_q1)} Retail-Plus members; gap Rs {real:,.0f} per member, carried from chapter 1")
'''),
        the_map(1, ["the options\\nrank, size, price, range",
                    "1. per member and per segment\\nthe fall in rupees",
                    "2. against the company\\nwhere the quarter's money sits",
                    "3. the plausible wrong answer\\nranked by p-value",
                    "4. against the cost\\nthe retention offer priced",
                    "a second route\\nthe bootstrap range"]),
        md('''
## The options

Four ways a team could answer "is it worth acting on?"

| Option | What it does | What it misses |
|---|---|---|
| A. Rank by p-value | Test every segment and fix the smallest share first | Size: a share says how sure, never how big |
| B. Size against the segment | The fall as a share of the tier's own revenue | The company: a third of a small tier can be a rounding error for Meera |
| C. Size against the company and the cost | The fall in rupees beside the quarter and beside what a fix costs, with its break-even | Nothing the decision needs, if the cost is known |
| D. A range for the fall | Redraw the members many times and read how small or large the fall could be | Nothing, and it answers a sharper question than C alone |
'''),
        code('''
t0 = time.perf_counter()
company_q2 = sum(delivered(s, "Q2") for s in SEGMENTS)
t_c = time.perf_counter() - t0
t0 = time.perf_counter(); boot = bootstrap_gaps(plus_q1, plus_q2, 5000, seed=2026); t_d = time.perf_counter() - t0
rows = [
    ("A. Rank by p-value", "3 segments x 5,000 shuffles", "about a second", "reads the smallest share as the biggest money"),
    ("B. Against the segment", "the tier's 2 quarters", "instant", "reads a third of the tier as a crisis"),
    ("C. Against company and cost", f"{len(ORDERS)} orders, one pass", f"{t_c * 1000:.1f} ms", "needs a cost; today's is assumed"),
    ("D. Bootstrap range", "44 member totals x 5,000 redraws", f"{t_d:.2f} s", "a stakeholder has to read a range"),
]
kit.table(["Option", "Rows it touches", "Time on this file", "What it risks"], rows,
          caption="The options sized on Kalpa's file")
kit.matrix(["cheap to run", "needs a range"], ["answers how sure", "answers how big"],
           [["A. rank by p-value", "B, C. rupees"], ["", "D. bootstrap range"]],
           title="What each option answers")
kit.check("every option runs in under five seconds here", max(t_c, t_d) < 5)
'''),
        md('''
**The best-fit call: C, with D as the second route.** Meera's decision is a budget line, so the
answer has to be in rupees beside the company's quarter and beside the offer's cost, and the
break-even says what the offer must win back. D then asks whether the range of plausible falls
clears that break-even. **The fact that would change the call.** A known recovery rate from an
earlier retention offer: with it, C alone decides, and the range matters less.
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
Retail-Plus fall is 0.19 percent of it. Business rose by Rs 6,18,460 in the same quarter, twenty-five
times the Retail-Plus fall. The fall is real and small against the company; both are true, and the
note needs both.

## 3. The plausible wrong answer

**The plausible wrong answer.** A hurried draft runs the shuffle on every segment with enough
members, sorts by the share, and names the smallest share the biggest problem. Student waits for
chapter 3.
'''),
        code('''
ranked = []
for s in ["Retail-Core", "Retail-Plus", "Business"]:
    q1, q2 = member_totals(s, "Q1"), member_totals(s, "Q2")
    share = share_at_least(shuffle_gaps(q1, q2, 5000, seed=2026), mean(q1) - mean(q2))
    ranked.append((s, share, delivered(s, "Q2") - delivered(s, "Q1")))
ranked.sort(key=lambda r: r[1])
for n, (s, share, move) in enumerate(ranked, 1):
    print(f"  {n}. {s:12s} p = {share:.3f}")
print(f"Draft: '{ranked[0][0]} is our biggest problem; fund its retention programme first.'")
'''),
        md('''
**Why it is wrong.** The share says how surely a move beats chance. It never says how big the move
is, and the draft ranked by the wrong column: a retention programme would be funded because a share
was small, before anyone asked how much money the fall is against the company or what fixing it
costs. **The check** puts the rupees beside the share, and an invented
example shows why the two columns can disagree so far: with enough orders, even a trivial gap beats
chance.
'''),
        code('''
kit.table(["Segment", "p, a fall this large", "Delivered revenue, Q2 less Q1"],
          [(s, f"{share:.3f}", kit.rupees(move)) for s, share, move in ranked],
          caption="The same three segments with the money beside the share")
maker = random.Random(11)                                  # invented orders, a Rs 20 gap at every size
base = [maker.randint(1000, 3400) for _ in range(20000)]
sizes, shares = [100, 1000, 5000, 20000], []
for n in sizes:
    q2 = base[:n]
    shares.append(share_at_least(shuffle_gaps([v + 20 for v in q2], q2, 500, seed=2026), 20))
kit.line([f"{n:,}" for n in sizes], [("share, Rs 20 gap", shares, "bad")], fmt=lambda v: f"{v:.3f}",
         title="Invented: the same Rs 20 gap tested on more and more orders a quarter")
print(dict(zip(sizes, shares)))
kit.check("the segment with the smallest share moved under half of one percent of the company's Q2",
          abs(dict((s, m) for s, _, m in ranked)[ranked[0][0]]) / company_q2 < 0.005)
kit.check("an invented Rs 20 gap goes from chance-sized to significant on sample size alone",
          shares[0] > 0.2 and shares[-1] < 0.01, f"{shares}")
'''),
        md('''
**The fix.** Two sentences where the draft had one, and any ranking done by money: "The
Retail-Plus fall is larger than the usual wobble. It is worth Rs 24,420 a quarter, 0.19 percent of
the company's delivered revenue, while Business moved Rs 6,18,460 the same quarter." What changed:
the size. By share Retail-Plus looked like the biggest problem; in rupees its fall is 0.19 percent of
the company's quarter, a twenty-fifth of the rise Business delivered, and the programme has to
justify itself against Rs 24,420 a quarter and the offer's cost, never against a share.

## 4. Against the cost: the retention offer priced

The head of Retail-Plus proposes a retention offer. **The cost is an assumption for this chapter,
since no Kalpa figure exists for it:** Rs 500 per member per quarter, offered to all 22 members.

**Predict before you run.** What share of the Rs 24,420 fall would the offer have to win back just
to pay for itself in revenue? a) all of it; b) about 45 percent; c) about 5 percent; d) none, since
any recovery is a gain.
'''),
        code('''
offer_per_member = 500                                   # assumed for the chapter
offer_cost = offer_per_member * len(plus_q1)
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
measured, which is what the note should say.

## A second route: the bootstrap range

Option D. The Rs 1,110 is one estimate from 22 members. Redraw each quarter's members with
replacement 5,000 times and read the middle 95 percent of the gaps. That range is called a
**confidence interval**; how to build one properly is a later week's topic, and today it arrives
as a picture.

**Predict before you run.** Does the range of plausible falls per member stay above zero, and does
it stay above the offer's Rs 500 per member? a) above both; b) above zero, and it dips below Rs 500;
c) below zero, so the fall may not be real; d) exactly Rs 1,110 every time.
'''),
        code('''
ordered = sorted(boot)
low, high = ordered[125], ordered[4874]
at_or_below_zero = sum(1 for g in boot if g <= 0) / len(boot)
kit.strip(boot[:200], markers=[("zero", 0, "bad"), ("offer per member", offer_per_member, "plain"),
                               ("real gap", real, "good")], lo=-1000, hi=3000,
          title="200 of the 5,000 bootstrap gaps per member, with zero, the offer and the real gap marked")
print(f"middle 95 percent: Rs {low:,.0f} to Rs {high:,.0f} per member, "
      f"or {kit.rupees(low * 22)} to {kit.rupees(high * 22)} a quarter; share at or below zero {at_or_below_zero:.3f}")
kit.check("the bootstrap range stays above zero, the same verdict as the shuffle", low > 0, f"{low:,.0f}")
kit.check("consistency: the share of redraws at or below zero sits near the shuffle's share",
          abs(at_or_below_zero - 0.027) < 0.01, f"{at_or_below_zero:.3f}")
kit.check("the range dips below the offer's Rs 500 per member", low < offer_per_member < high)
'''),
        md('''
**What happened.** The answer is b. This approximate 95 percent range runs from about Rs 40 to Rs
2,200 per member (its low end moves by a few tens of rupees with the seed), so the fall is real by a
second route: the range stays above zero, and about 2 in 100 redraws land at or below zero, a
consistency check beside the shuffle's 0.027 rather than a second p-value, and it could be as small as about Rs 900 a quarter for the tier. The offer's Rs 500
per member sits inside the range, which is the arithmetic behind "test it on half the members
first". **When to switch.** Use the range whenever the decision has a cost to beat; the share alone
is enough only when the question is "real or not".

> **Kavya's review.** "Real, yes, by two routes. Worth Rs 24,420 a quarter, small against Business
> and a third of the tier. The range dips below what the offer costs, so do not fund it for all 22:
> offer it to half, hold back half, and measure. That is a watch item with a test attached, never a
> budget line."

### In the interview

**[F] A metric moved and the test says significant; how do you decide whether the business should
act?** "Significant only tells me the move is bigger than noise. To act I need three more things:
the size in money against the business and the segment, the cost of the action, and how much of
the gap the action could recover. If the break-even recovery is higher than anything we have seen,
or the range of the effect dips below the cost, I recommend a small test with a held-back group
rather than a rollout."

**[S] Explain a finding to a non-technical stakeholder.** "I lead with the decision the finding
supports, in one sentence, with one number and its denominator. Then the evidence, the caveat that
would change my view, and the action with what it costs. For example: Retail-Plus really is
spending less, about Rs 24,000 a quarter, which is a third of the tier and a fifth of one percent of
the company; an offer pays only if it wins back 45 percent, so test it on half the members first."

**[D] You can rank segments by p-value, by rupees or by rupees against the cost of fixing; which do
you take to the budget meeting, and what would change it?** "Rupees against the cost, because the
meeting decides money. The p-value only filters out noise. If a past offer had told me the recovery
rate, the break-even alone would decide, and I would skip the range."

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
reach the same share a second way by counting every possible deal.

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

Chapters 1 and 2 found the Retail-Plus fall real and small against the company. Meera's second
question is about a rise, the biggest on the page. This chapter adds `orders_in` and `flip_rises`,
a chance reference built for a count.
'''),
        md('**Setup.** The toolkit so far, plus the two new helpers.'),
        setup(T1, T2, T3, extra='''
print("toolkit ready:", ", ".join(["member_totals", "shuffle_gaps", "share_at_least", "delivered",
                                   "bootstrap_gaps", "orders_in", "flip_rises"]))
'''),
        the_map(2, ["the options\\ntrust, test, rule, wait",
                    "1. the headline\\nevery segment's orders, Q2 against Q1",
                    "2. the plausible wrong answer\\nthe fastest rise wins the budget",
                    "3. chance on the count\\na coin flip per order",
                    "4. 42 percent on 12\\nthe interview's version",
                    "a second route\\nevery possible deal, counted"]),
        md('''
## The options

Four ways a team could answer "should budget follow the 40 percent?"

| Option | What it does | What it risks |
|---|---|---|
| A. Trust the headline | Rank segments by growth and fund the fastest | Moving money on a rate a coin could make |
| B. A chance reference for the count | Deal each order to a quarter by coin flip and see how often chance makes a 40 percent rise | Nothing, if the count is found first |
| C. The rule of thumb | Treat any rate on fewer than thirty observations as a lead | A blunt line: it says "careful", never how careful |
| D. Wait for thirty orders | Hold the decision until the segment carries thirty orders a quarter | Time: at today's pace that is a long wait |
'''),
        code('''
t0 = time.perf_counter()
student_orders = sum(1 for o in ORDERS if o["segment"] == "Student")
flips = flip_rises(student_orders, 5000, seed=2026)
t_b = time.perf_counter() - t0
pace = orders_in("Student", "Q2")
below_thirty = pace < 30
rows = [
    ("A. Trust the headline", "4 segments x 2 quarters", "instant", "budget follows a coin"),
    ("B. Coin-flip reference", "the segment's orders x 5,000", f"{t_b:.2f} s", "none once the count is known"),
    ("C. Rule of thumb", "one count", "instant", "says careful, never how careful"),
    ("D. Wait for thirty a quarter", "one more count a quarter", "today's pace is far below thirty", "the chance to invest early"),
]
kit.table(["Option", "What it touches", "Cost on this file", "What it risks"], rows,
          caption="The options sized on Kalpa's file")
kit.flow(["A. trust\\nthe rate", "B. chance on\\nthe count", "C. the rule\\nof thumb", "D. wait for\\nthirty"], lit=1,
         title="The best-fit call for Monday is B, with C as its one-line summary")
kit.check("the coin-flip reference runs in under five seconds", t_b < 5)
kit.check("Student places far fewer than thirty orders a quarter today, so waiting is long", below_thirty)
'''),
        md('''
**The best-fit call: B, said with C.** The coin flips tell Meera how often chance alone makes her
headline, which is the question; the rule of thumb is the sentence she remembers. D is the action
the answer leads to, and it takes a while at the segment's pace, which is why the note says what
count would reopen the question. **The fact that would change the call.** A cheap way to buy more
orders fast, such as a small paid test aimed only at students: then D stops being a wait and
becomes a two-week experiment.
'''),
        md('''
## 1. The headline: every segment's orders, Q2 against Q1

Meera's 40 percent is about orders placed, whatever their status. Put every segment on the same footing: Q2 orders for every 100
orders in Q1.

**Predict before you run.** Which segment shows the biggest rise? a) Business, since it carries the
revenue; b) Retail-Core; c) Student; d) none rose.
'''),
        code('''
order_segments = ["Retail-Core", "Retail-Plus", "Business", "Student"]
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

Chapter 1's shuffle mixed labels between two quarters. For a count, the chance reference is
simpler: if Student's ordering had not changed, each Student order was as likely to land in Q1 as in
Q2. Flip a coin per order, 5,000 times, and count how often chance alone makes a rise of 40 percent
or more.

**Predict before you run.** For Student's own orders, what share of coin-flip worlds show a rise of
40 percent or more? a) under 1 percent; b) about 5 percent; c) about 40 percent; d) all of them.
'''),
        code('''
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
more from Student's orders alone. Chance makes Meera's headline almost as often as not. Now the same
40 percent on bigger counts: a segment with Retail-Core's orders, and an **invented** segment of
400.
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
about 40 percent of coin-flip worlds. Not yet: we watch Student until it carries thirty orders a
quarter before any budget moves." What changed: the decision. The draft moved budget; the fix moves
nothing and names the count that would reopen the question.

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

## A second route: count every possible deal

The coin flips sampled 5,000 worlds. With a count this small, every possible way of dealing the
orders to the two quarters can be listed and counted exactly, which is the check on the flips.

**Predict before you run.** How close will the exact share be to the flips' share? a) exactly
equal; b) within about two points; c) about half of it; d) no relation, since the flips are random.
'''),
        code('''
import itertools

deals = list(itertools.product(["Q1", "Q2"], repeat=student_orders))
rising = 0
for deal in deals:
    q2 = deal.count("Q2")
    q1 = student_orders - q2
    if q1 == 0 or q2 / q1 - 1 >= 0.4 - 1e-9:
        rising += 1
exact_share = rising / len(deals)
kit.columns(["coin flips, 5,000", "every deal, counted"], [("share with a 40% rise", [round(student_share, 3), round(exact_share, 3)])],
            fmt=lambda v: f"{v:.3f}", width=520, title="Two routes to the same share")
print(f"exact share {exact_share:.3f}; the flips said {student_share:.3f}")
kit.check("the exact count and the flips agree within two points", abs(exact_share - student_share) < 0.02,
          f"{exact_share:.3f} against {student_share:.3f}")
'''),
        md('''
**What happened.** The answer is b. Counting every deal gives 0.387 where the flips gave 0.397, so
the flips were right and the verdict holds: chance makes Meera's headline about four times in ten.
**When to switch.** Count every deal while the count is small enough to list; on a few dozen orders
the list runs into the billions, and the flips are the only practical route.

> **Kavya's review.** "Student's rise is real arithmetic on too few orders to act on. Count them,
> say how often chance makes the rise, and give Meera the count that would reopen it. That is a
> complete answer, and it costs nothing to be right later."

### In the interview

**[F] 42 percent on 12 users against 31 percent on 1,200; which do you trust?** "The 31 percent, as
the working estimate. On 12 users one person moves the rate by more than 8 points, so 42 percent is
well inside what chance produces around a true rate near 31. I keep the 42 as a lead: find out what
is different about that group and measure it on more users before acting."

**[D] A segment is up 40 percent and the CEO wants to move budget; you can trust it, test it on the
count, or wait. Which, and what would change your mind?** "Test it on the count first: how often do
coin flips make that rise on that many orders? If chance makes it often, the answer is not yet, with
the count that would reopen it. A cheap, fast way to get more orders from that segment would turn
the wait into a short experiment, and I would propose that."

### Depth: where thirty comes from

Thirty is a habit, never a law: it is roughly where a count stops swinging wildly from one extra
observation. The curve below is the coin-flip chance of a 40 percent rise at growing counts, the
same simulation as section 3.
'''),
        code('''
counts = [10, 20, 30, 50, 100, 200, 400]
curve = []
for n in counts:
    rises = flip_rises(n, 3000, seed=2026)
    curve.append(sum(1 for r in rises if r >= 0.4 - 1e-9) / len(rises))
kit.line([str(n) for n in counts], [("chance of a 40% rise", curve, "bad")], fmt=lambda v: f"{v:.2f}",
         title="Chance of a 40 percent rise from coin flips alone, by the count behind it")
kit.check("the chance falls below one in five by thirty orders", curve[2] < 0.2, f"{curve[2]:.3f}")
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
headline lift, split it by segment, say why the blend and the segments disagree, and reach the
segments' answer a second way by putting both groups on one mix.

> **The client asks.** "Marketing ran a monsoon-sale discount for Retail-Plus in August, says it
> lifted revenue 6 percent, and wants to repeat it for Diwali. Did the discount work, or did those
> customers buy anyway?"
>
> Meera Raghavan, CEO, Kalpa Retail, with the marketing lead's report open beside her

**The metric at stake.** August revenue per customer, for customers who got the sale against
customers who did not. **Who asks and what rides on it.** The marketing lead owns the campaign and
wants it repeated at 15 percent off; Meera signs the Diwali budget. Monday's rule applies: at 15
percent off, orders must rise about 17.6 percent just for revenue to stand still, so a sale that
did not lift spend gives margin away. **Who else faces it.** Every marketplace that runs a sale
reads its lift this way: Flipkart's Big Billion Days sale ran from 23 to 30 September 2022 and
passed a billion customer visits for the first time, and a number that size is only useful once
someone asks which customers it came from. The classic public case of a blend reversing is UC
Berkeley's 1973 graduate admissions: 44 percent of men and 35 percent of women were admitted
overall, and department by department the small bias ran in favour of women.

Chapters 1 to 3 answered Meera's first two questions. This chapter opens the campaigns table and
the exposure table, and adds `spend` and `group` to the toolkit. The exposure table is Marketing's
own campaign extract of 160 customers, listed separately from the order sample the morning used, so
its customers and totals do not reconcile with the orders file; it records one August figure per
group of customers, so it can show who got the sale and how the mix differs, and it cannot say how
much spend varies from customer to customer.
'''),
        md('**Setup.** The toolkit so far, plus the two campaign tables and two new helpers.'),
        setup(T1, T2, T3, T4, extra='''
print(len(EXPOSURE), "customers in the exposure table;", CAMPAIGNS[0]["name"], CAMPAIGNS[0]["discount_pct"],
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

Four ways a team could answer "did the discount work?"

| Option | What it compares | What it risks |
|---|---|---|
| A. Before and after | The targeted segment's revenue in the sale month against the month before | Everything else that changed that month |
| B. Exposed against not exposed, blended | Revenue per customer for everyone who got the sale against everyone who did not | Two groups built from different mixes of customers |
| C. Exposed against not exposed, inside each segment | The same comparison run separately in each segment | Anything that differs between the groups inside a segment |
| D. Both groups on one mix | Each group's segment averages weighted to the same mix of segments | The same as C; it is C said as one number |
'''),
        code('''
t0 = time.perf_counter()
blend = spend(group("yes")) / spend(group("no")) - 1
t_b = time.perf_counter() - t0
mix_yes = len(group("yes", "Retail-Plus")) / len(group("yes"))
mix_no = len(group("no", "Retail-Plus")) / len(group("no"))
stand_still = 1 / (1 - int(CAMPAIGNS[0]["discount_pct"]) / 100) - 1
rows = [
    ("A. Before and after", "the orders file, two months", "instant", "an August bump from anything"),
    ("B. Blended", f"{len(EXPOSURE)} customers, 2 groups", f"{t_b * 1000:.2f} ms", "the groups' mixes differ"),
    ("C. Inside each segment", f"{len(EXPOSURE)} customers, 4 cells", "instant", "who got it inside a segment"),
    ("D. One mix", "the 4 cells, reweighted", "instant", "the same as C"),
]
kit.table(["Option", "Rows it touches", "Time on this file", "What it risks"], rows,
          caption="The options sized on Kalpa's campaign tables")
kit.columns(["exposed", "not exposed"], [("share who are Retail-Plus", [round(100 * mix_yes), round(100 * mix_no)])],
            fmt=lambda v: f"{v:.0f}%", width=520, title="Before choosing: the two groups are not built from the same customers")
print(f"at {CAMPAIGNS[0]['discount_pct']} percent off, orders must rise {stand_still:.1%} for revenue to stand still")
kit.check("the two groups differ in mix", abs(mix_yes - mix_no) > 0.05, f"{mix_yes:.0%} against {mix_no:.0%}")
kit.check("Monday's rule: 15 percent off needs about 17.6 percent more volume", round(stand_still, 3) == 0.176)
'''),
        md('''
**The best-fit call: C, with D as the second route.** The two groups hold different mixes of
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
kit.columns(["got the sale", "did not"], [("August revenue per customer", [round(blend_yes), round(blend_no)])],
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
            fmt=kit.rupees, lit=[2], title="August revenue per customer: each segment against the blend")
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
segment so the comparison is fair." What changed: the decision, from repeat to redesign, and the
reason is a mix of customers, never a mistake in Marketing's arithmetic.

## A second route: both groups on one mix

Put the exposed group's segment averages into the unexposed group's mix, and the other way round.
If the mix is the whole story, both directions give the same answer as the split.

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
kit.check("both directions agree with the split, about 3 percent less", abs(one - two) < 0.005 and one < 0,
          f"{one:+.1%} and {two:+.1%}")
'''),
        md('''
**What happened.** The answer is b. On the unexposed group's mix the exposed spend Rs 3,104 against
Rs 3,200; on the exposed group's mix, Rs 3,395 against Rs 3,500. Both are 3.0 percent less, the same
as the split. **When to switch.** Split by segment when the stakeholder reads a table; put both
groups on one mix when the answer has to be one number on one line of the note, or when there are
too many segments to show.

> **Kavya's review.** "You rebuilt Marketing's number before disagreeing with it, which is what
> keeps Monday civil. The split says 3 percent less in both segments, one mix says the same, and the
> reason is who got the sale. Now tell me what else changed in August, because the split cannot see
> that."

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
and what would make the blend acceptable?** "The split, with one mix as the one-line version.
Before and after sees every August effect, and the blend mixes customers. The blend becomes fair
only when a coin decided who got the campaign."

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
NUMBERS["share"] = share_at_least(shuffle_gaps(plus_q1, plus_q2, 5000, seed=2026), real)
NUMBERS["fall"] = round(real * len(plus_q1))
NUMBERS["company"] = sum(delivered(s, "Q2") for s in SEGMENTS)
NUMBERS["tier_q1"] = delivered("Retail-Plus", "Q1")
NUMBERS["offer"] = 500 * len(plus_q1)
student_n = sum(1 for o in ORDERS if o["segment"] == "Student")
flips = flip_rises(student_n, 5000, seed=2026)
NUMBERS["student_rise"] = round(100 * orders_in("Student", "Q2") / orders_in("Student", "Q1")) - 100
NUMBERS["student_chance"] = sum(1 for r in flips if r >= 0.4 - 1e-9) / len(flips)
NUMBERS["blend"] = spend(group("yes")) / spend(group("no")) - 1
NUMBERS["within"] = spend(group("yes", "Retail-Plus")) / spend(group("no", "Retail-Plus")) - 1
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
line that hedges everything gives her nothing to decide. **Who else faces it.** Amazon banned slide
presentations from its meetings and replaced them with six-page narrative memos read in silence at
the start of each meeting, which Jeff Bezos described in his 2017 letter to shareholders. A
narrative forces the writer to connect each claim to its evidence, which is this chapter's job on
one page.

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
                    "a second route\\nevery figure traced back"]),
        md('''
## The options

Four ways a team could answer Meera in writing.

| Option | What it is | What it risks |
|---|---|---|
| A. A yes or no per question | Three words she asked for | Every caveat, and the "not yet" she explicitly allowed |
| B. The dashboard | Every number the chapters produced, in one table | Two minutes spent reading, and no decision on the page |
| C. The four-part note | Claim, evidence with its base, caveat, action with its cost, per question | The discipline to keep it under 200 words |
| D. A slide deck | Ten slides for Monday | A meeting to present it; the logic lives in the talk, never on the page |
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
        ("D. Slide deck", "about ten slides", "what the slides draw", "a meeting to present")]
kit.table(["Option", "Words, about", "Bases carried", "What it loses"], rows,
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
    ("Retail-Plus fall, share of chance-only worlds", f"{NUMBERS['share']:.3f}", "the world it was counted in"),
    ("Retail-Plus fall, rupees a quarter", kit.rupees(NUMBERS["fall"]), "the company's quarter"),
    ("Company delivered revenue, Q2", kit.rupees(NUMBERS["company"]), "the window"),
    ("Retention offer, rupees a quarter", kit.rupees(NUMBERS["offer"]), "an assumption, said as one"),
    ("Student orders, rise", f"{NUMBERS['student_rise']}%", "the count, and chance on it"),
    ("Student, coin-flip share for that rise", f"{NUMBERS['student_chance']:.3f}", "what it means for the decision"),
    ("Monsoon sale, blended lift", f"{NUMBERS['blend']:+.1%}", "who got it"),
    ("Monsoon sale, inside Retail-Plus", f"{NUMBERS['within']:+.1%}", "the counts per group"),
]
kit.table(["Number", "Value", "What must sit beside it"], table, caption="The day's numbers, each with the base it needs")
kit.check("eight numbers carry forward from chapters 1 to 4", len(table) == 8)
kit.check("every number has a base named beside it", all(t[2] for t in table))
'''),
        md('''
**What happened.** The answer is c. Every number needs a partner: a share needs its world, a rupee
figure its whole, a rate its count, a lift its groups. A number without its partner is the next
section's trap.

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
    base = any(w in low for w in ["of the company", "a quarter", "against rs", "per member", "than customers"])
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
plus_line = {
    "claim": "Retail-Plus really is spending less, and it is small against the company.",
    "evidence": (f"Members delivered Rs 1,110 less each, {kit.rupees(NUMBERS['fall'])} a quarter, "
                 f"{NUMBERS['fall'] / NUMBERS['company']:.2%} of the company's quarter; if nothing had changed, "
                 f"a fall that large turns up in about {round(NUMBERS['share'] * 100)} in 100 shuffles."),
    "caveat": "The size could be much smaller than Rs 1,110 a member, so an offer may not pay back.",
    "action": (f"Test the Rs 500-a-member offer on half the tier, {kit.rupees(NUMBERS['offer'] // 2)} a quarter, "
               f"and hold back the other half, rather than funding it for all."),
}
kit.flow([f"{k}\\n{len(v.split())} words" for k, v in plus_line.items()], lit=2,
         title="The Retail-Plus line in four parts, with the caveat lit")
print("\\n".join(f"{k.upper()}: {v}" for k, v in plus_line.items()))
kit.check("the Retail-Plus line passes the audit", audit(" ".join(plus_line.values())) == ["yes", "yes", "yes"])
'''),
        md('''
**What happened.** The answer is c: the caveat is the part most often missing, and it is the part a
CEO keeps an analyst for. The Retail-Plus line now carries its base (the company's quarter), its
chance (3 in 100), its caveat (the size could be smaller) and its action with a cost.

## 4. Not yet: the Student and discount lines

"Not yet" is a claim, a caveat and an action in one sentence, provided it names what would turn it
into a yes. Write both lines and audit the whole note.

**Predict before you run.** How many words will the three answers take? a) under 50; b) about 170;
c) about 400; d) over 1,000.
'''),
        code('''
student_line = (f"Student orders rose {NUMBERS['student_rise']} percent on a count so small that chance alone makes "
                f"that rise in about {round(NUMBERS['student_chance'] * 100)} in 100 worlds. Not yet: no budget moves "
                f"until Student carries thirty orders a quarter.")
discount_line = (f"The monsoon sale did not lift spend: inside each segment, the {len(group('yes', 'Retail-Plus'))} customers who got it spent about "
                 f"{abs(NUMBERS['within']):.0%} less than customers who did not, and the {NUMBERS['blend']:.0%} blend "
                 f"is higher only because the exposed group held more Retail-Plus members. Do not repeat it as "
                 f"designed; if Diwali has a sale, hold back a random slice of each segment.")
note = " ".join(plus_line.values()) + " " + student_line + " " + discount_line
kit.matrix(["Retail-Plus", "Student", "Discount"], ["a base", "count or chance", "a caveat"],
           [audit(" ".join(plus_line.values())), audit(student_line), audit(discount_line)],
           title="The fixed note, audited line by line")
kit.bars([("headline note", len(headline.split())), ("four-part note", len(note.split())), ("Meera's ceiling", 200)],
         fmt=lambda v: f"{v} words", lit=[1], title="Words on the page")
print(student_line)
print(discount_line)
print(f"the whole note: {len(note.split())} words")
kit.check("the full note is under 200 words", len(note.split()) < 200, f"{len(note.split())}")
kit.check("every line of the fixed note passes the audit",
          all(a == ["yes", "yes", "yes"] for a in [audit(student_line), audit(discount_line)]))
'''),
        md('''
**What happened.** The answer is b: about 170 words carry all three answers with their bases,
caveats and actions, against the headline note's 30 words and three wrong decisions. What changed:
three decisions. Retail-Plus becomes a test on half the tier, Student becomes a watch with a
threshold, and the Diwali sale becomes a redesign with a hold-back.

## A second route: every figure traced back

Read the note as a stranger would. Pull every number out of the text and trace each one to
`NUMBERS`. A figure that traces nowhere was typed by hand and is the likeliest to be wrong.
'''),
        code('''
import re

found = re.findall(r"Rs [\\d,]+|\\d+\\.\\d+%|\\d+ percent|\\d+ in 100|\\d+%", note)
known = {kit.rupees(NUMBERS["fall"]), kit.rupees(NUMBERS["offer"] // 2), "Rs 500", "Rs 1,110",
         f"{NUMBERS['fall'] / NUMBERS['company']:.2%}", f"{NUMBERS['student_rise']} percent",
         f"{round(NUMBERS['share'] * 100)} in 100", f"{round(NUMBERS['student_chance'] * 100)} in 100",
         f"{abs(NUMBERS['within']):.0%}", f"{NUMBERS['blend']:.0%}"}
traced = [f for f in found if f in known]
kit.columns(["figures in the note", "traced to a chapter"], [("figures", [len(found), len(traced)])],
            width=520, title="Every figure in the note, traced back to the numbers")
print("figures found:", found)
kit.check("every figure in the note traces to a chapter's number", len(found) == len(traced) and found,
          f"{len(traced)} of {len(found)}")
'''),
        md('''
**What happened.** Every figure in the note traces to a number a chapter computed, so the text and
the analysis agree. **When to switch.** Trace by hand for a one-off note; generate the note from the
numbers, as this chapter's cells did, when it repeats weekly, because a template cannot mistype.

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
cheapest test that settles it, such as a held-back group at Diwali. I hold the line with the split,
never with authority: I show their number reproduced, then the segments, and invite them to find
the flaw."

**[D] One-line answers, a dashboard or a written note: which do you send a CEO before a review, and
when would you switch?** "A written note under a page, each claim with its base and its caveat. I
switch to a small dashboard when the same metrics are reviewed every week, so the note only covers
what moved."

### Depth: the fact that would flip each line

A note is stronger when it says, per line, what would change it. The table is the caveat column
made explicit.
'''),
        code('''
flips_table = [("Retail-Plus", "real, small, test the offer", "a second quarter with a larger fall, or a recovery rate from a past offer"),
               ("Student", "not yet", "thirty orders a quarter with the rise holding"),
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
a before-and-after number misleads, reach the verdict a second way, and design the comparison that
would settle it at Diwali.

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
that those ads had no measurable short-term benefit, and that the frequent buyers who saw most of
eBay's other search ads would have bought anyway, which made the average return negative.

Chapter 4 split the blend by segment and chapter 5 wrote the note. This chapter adds
`month_delivered` and `month_orders`, and opens the orders file by month.
'''),
        md('**Setup.** The whole toolkit, plus the two month helpers.'),
        setup(T1, T2, T3, T4, T6, extra='''
MONTHS = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]
print("orders by month ready for", len(MONTHS), "months; the sale ran", CAMPAIGNS[0]["starts"], "to", CAMPAIGNS[0]["ends"])
'''),
        the_map(5, ["the options\\nbefore-after, beside, inside, hold-back",
                    "1. who got it\\nthe target against the exposure",
                    "2. the plausible wrong answer\\nAugust against July",
                    "3. what else changed\\nthe segment beside it",
                    "4. the design\\na hold-back at Diwali",
                    "a second route\\nthe split from chapter 4"]),
        md('''
## The options

Four ways a team could answer "did the sale cause the lift?"

| Option | What it compares | What it assumes |
|---|---|---|
| A. Before and after | The targeted segment in August against July | Nothing else changed between the months |
| B. The change beside the change | The targeted segment's move against an untargeted segment's move over the same months | Both segments would have moved alike without the sale |
| C. Inside each segment | Customers who got it against customers who did not, in the same month (chapter 4) | Who got it inside a segment was as good as random |
| D. A random hold-back | A coin decides, before the sale, which customers do not get it | Nothing, which is why it costs a campaign cycle |
'''),
        code('''
plus_jul, plus_aug = month_orders("Retail-Plus", "2026-07"), month_orders("Retail-Plus", "2026-08")
core_jul, core_aug = month_orders("Retail-Core", "2026-07"), month_orders("Retail-Core", "2026-08")
rp_customers = len(group("yes", "Retail-Plus")) + len(group("no", "Retail-Plus"))
held_back = rp_customers // 5
forgone = round(held_back * spend(group("no", "Retail-Plus")) * 0.06)
rows = [
    ("A. Before and after", f"{len(plus_jul) + len(plus_aug)} delivered orders", "the season, the tier's own drift"),
    ("B. Beside an untargeted segment", f"{len(plus_jul) + len(plus_aug) + len(core_jul) + len(core_aug)} delivered orders", "that the two segments move alike"),
    ("C. Inside each segment", f"{len(EXPOSURE)} customers", "who got it was chosen, never random"),
    ("D. Random hold-back at Diwali", f"a fifth of {rp_customers} Retail-Plus customers", f"about {kit.rupees(forgone)} forgone if Marketing's 6 percent were real"),
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
holding back a fifth of Retail-Plus forgoes a few thousand rupees. **The fact that would change the
call.** A campaign so large, or a hold-back so politically hard, that the forgone lift runs into
lakhs: then B, on a longer run of months, becomes the working answer with its caveat said aloud.
'''),
        md('''
## 1. Who got it

The campaigns table says who the sale was aimed at; the exposure table says who received it.

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
kit.check("the exposure table covers both segments' customers", sum(got.values()) == len(group("yes")))
'''),
        md('''
**What happened.** The answer is b. The sale was aimed at Retail-Plus and half of the customers who
got it were Retail-Core. Whatever rule chose them, it was a rule, never a coin, and a rule can pick
the customers who were going to buy anyway. That is the first of the three questions, and it is
already an answer: the groups were chosen.

## 2. The plausible wrong answer

**The plausible wrong answer.** A hurried readout opens the orders file and compares Retail-Plus in
the sale month with the month before.
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
**What happened.** The answer is c. Retail-Core rose 73 percent from July to August with no sale
aimed at it, and Retail-Plus fell 58 percent from May to June with no sale at all. A month's revenue
on a few orders swings by half on its own, and August was a big month for both segments.

**The fix.** Compare like with like in time as well: take August's share of each segment's
quarter, then ask how often chance alone makes a gap that large between the two segments, dealing
the segment labels at random across both segments' delivered Q2 orders.
'''),
        code('''
aug_share_rp = rp[4] / sum(rp[3:])
aug_share_core = core[4] / sum(core[3:])
pool = ([("Retail-Plus", int(o["amount"]), o["order_date"][:7]) for m in MONTHS[3:] for o in month_orders("Retail-Plus", m)]
        + [("Retail-Core", int(o["amount"]), o["order_date"][:7]) for m in MONTHS[3:] for o in month_orders("Retail-Core", m)])
n_plus = sum(1 for p in pool if p[0] == "Retail-Plus")
real_gap = aug_share_rp - aug_share_core


def aug_share(rows):
    return sum(a for a, m in rows if m == "2026-08") / sum(a for a, _ in rows)


random.seed(2026)
chance = []
orders = [(a, m) for _, a, m in pool]
for _ in range(5000):
    random.shuffle(orders)                        # deal the segment labels at random
    chance.append(aug_share(orders[:n_plus]) - aug_share(orders[n_plus:]))
chance_share = sum(1 for c in chance if abs(c) >= abs(real_gap)) / len(chance)
kit.strip(chance[:200], markers=[("real gap", real_gap, "bad")], lo=-0.5, hi=0.5, fmt=lambda v: f"{v:+.0%}",
          title="Targeted less untargeted August share, in 200 deals of the segment labels, with the real gap marked")
print(f"August's share of Q2: Retail-Plus {aug_share_rp:.1%}, Retail-Core {aug_share_core:.1%}, a gap of "
      f"{100 * real_gap:.1f} points; shuffling the segment labels makes a gap that large either way in {chance_share:.2f} of deals")
kit.check("August's share is within a few points for the targeted and the untargeted segment",
          abs(aug_share_rp - aug_share_core) < 0.06, f"{aug_share_rp:.1%} against {aug_share_core:.1%}")
kit.check("chance makes a gap that large often, so the months show no sale effect", chance_share > 0.2, f"{chance_share:.2f}")
'''),
        md('''
What changed: the jump of 170 percent becomes an August that took 52 percent of Retail-Plus's
quarter against 49 percent of Retail-Core's, about four points apart, and shuffling the segment
labels makes a gap that large in about eight deals in ten. The month file shows no sign of the sale
beyond a busy August for everyone.

## 4. The design: a hold-back at Diwali

The only comparison that answers "would they have bought anyway?" is one where a coin decides who
gets the sale. Decide before the sale, inside each segment, and agree the measure and the window in
advance.

**Predict before you run.** If Marketing's 6 percent were the true lift, holding back a random
fifth of the Retail-Plus customers in the comparison would forgo about: a) Rs 4,000; b) Rs 40,000;
c) Rs 4 lakh; d) nothing, since held-back customers still buy.
'''),
        code('''
kit.vflow(["before Diwali: list each segment's customers",
           "a coin per customer: one in five held back",
           "the sale runs for the rest, same window",
           "after: spend per customer, held back against got it, inside each segment",
           "the shuffle test from chapter 1 on the gap"],
          lit=1, title="The Diwali comparison, decided before the sale")
kit.stats([(f"{held_back}", "held back", f"a fifth of {rp_customers} Retail-Plus customers"),
           (kit.rupees(forgone), "forgone", "if Marketing's 6 percent were real"),
           ("0", "rupees of discount", "given to the held-back customers")])
kit.check("the hold-back forgoes under Rs 10,000 even at Marketing's own lift", forgone < 10000, kit.rupees(forgone))
'''),
        md('''
**What happened.** The answer is a. Fourteen held-back Retail-Plus customers at Rs 5,000 each and a 6
percent lift is about Rs 4,200, the cost of the hold-back, and nothing if the lift is not real.
Fourteen customers are too few to measure a lift as small as 6 percent, since spend swings far more
than that from customer to customer; how many a hold-back needs is a question of power, which comes
in a later week, and the honest design holds back a random slice of every segment the sale reaches.

## A second route: the split from chapter 4

Chapter 4's comparison inside each segment used a different table and a different idea. Do the two
routes agree that the monsoon sale did not show a lift?

**Predict before you run.** a) yes, both find no lift the sale can claim; b) no, the months say it
worked; c) no, the split says it worked; d) they cannot be compared at all.
'''),
        code('''
split = {s: spend(group("yes", s)) / spend(group("no", s)) - 1 for s in ["Retail-Plus", "Retail-Core"]}
month_gap = aug_share_rp - aug_share_core
kit.columns(["months: August share gap, points", "split: Retail-Plus, percent", "split: Retail-Core, percent"],
            [("the two routes", [round(100 * month_gap, 1), round(100 * split["Retail-Plus"], 1), round(100 * split["Retail-Core"], 1)])],
            fmt=lambda v: f"{v:+.1f}", width=660, title="Two routes to one verdict: no lift the sale can claim")
print(f"months: August took {100 * month_gap:+.1f} points more of Retail-Plus's quarter than of Retail-Core's, "
      f"a gap the label shuffle makes in about {round(chance_share * 100)} deals in 100; "
      f"split: " + ", ".join(f"{s} {v:+.1%}" for s, v in split.items()))
kit.check("the split finds the exposed spending less in both segments", all(v < 0 for v in split.values()))
kit.check("the months find no gap chance does not make", chance_share > 0.2)
'''),
        md('''
**What happened.** The answer is a, with an honest difference. The months say "no sign": an
August share four points above the untargeted segment's, a gap the label shuffle makes about eight
times in ten. The split says "3 percent less in both segments". Neither shows the lift Marketing claimed, and neither is a fair comparison, because
nobody tossed a coin. That is why the line to Meera stays "do not repeat it as designed" and the
action is the hold-back. **When to switch.** Use the change beside the change when months of data
exist and no hold-back was run; use the split when an exposure table exists; run the hold-back
whenever the next campaign can still be designed.

> **Kavya's review.** "Who got it: a rule, never a coin. Who did not: a different mix. What else
> changed: August, for everyone. Two routes find no lift, and you priced the hold-back that would settle
> it at about Rs 4,200. Take that to Marketing as an offer, never as a verdict on their work."

### In the interview

**[F] Revenue rose after a discount; did the campaign work, and what would you need to know?** "Three
things: who got it, who did not, and what else changed. A before-and-after number credits the
campaign with the season. I would compare against customers who did not get it in the same window,
inside each segment, and I would ask for a random hold-back next time, because that is the only
comparison where the customers who would have bought anyway are in both groups."

**[F] How would you set up the Diwali campaign so you can tell whether it worked?** "Before the sale,
a coin per customer inside each segment holds back about one in five. Agree the measure and the
window in advance, run the sale for the rest, then compare spend per customer inside each segment
and test the gap against chance. At Marketing's own claimed lift the hold-back costs a few thousand
rupees, and the size of the hold-back is set by how small a lift we need to see, which is a later
week's question."

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
fell 58 percent while Retail-Core rose 63 percent. That is a lead, never an answer,
and it points the same way as everything else in this chapter: run the hold-back.
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

"""Write the three case notebooks of Week 1 Thursday, each as a TODO twin and an executed solution.

Run from the repository root:

    python3 content/W01/D4/internal/C2_W01_D04_build_case_notebooks_INTERNAL.py            # all three
    python3 content/W01/D4/internal/C2_W01_D04_build_case_notebooks_INTERNAL.py ex1        # one
    python3 content/W01/D4/internal/C2_W01_D04_build_case_notebooks_INTERNAL.py --verify   # prove the checks

Both twins come from one source, so they never drift. The TODO twin keeps each `__TODOn__`
placeholder under its lettered options; the solution replaces it with the keyed option's line, adds
the reason for each letter under the cell that carries it, and is executed cold in its own folder.

Every check sits in the cell after the choices it tests and compares a computed value with the value
it should reach. No check names or quotes an option's line, so reading the checks gives no key away.
`--verify` proves that: for every TODO it swaps in each wrong option in turn, runs the solution's
code as a plain script, and reports whether some check in the notebook fails. A wrong option that no
check catches, or that only crashes, is printed so it can be reworded.
"""
import json
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, build, code, md  # noqa: E402

NOTEBOOKS = ROOT / "content" / "W01" / "D4" / "notebooks"
SOLUTIONS = ROOT / "content" / "W01" / "D4" / "exercises" / "solutions"
OPTION = re.compile(r"^\s*#\s+([a-d])\)\s(.+)$")
HEAD = re.compile(r"^\s*#\s+TODO (\d+)\.")

FLIPS = '''

def flip_gaps(q1, q2, times, seed):
    """A coin for each pair decides which of its two values counts in the first list; the gap in means, many times."""
    random.seed(seed)
    diffs = [a - b for a, b in zip(q1, q2)]
    return [mean([d if random.random() < 0.5 else -d for d in diffs]) for _ in range(times)]


def shuffle_gaps(q1, q2, times, seed):
    """Every value in one pool, dealt at random into two piles of the original sizes; the gap in means, many times."""
    random.seed(seed)
    pool = q1 + q2
    gaps = []
    for _ in range(times):
        random.shuffle(pool)
        gaps.append(mean(pool[:len(q1)]) - mean(pool[len(q1):]))
    return gaps


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


def options_of(src):
    """{todo number: {letter: line}} for every lettered option block in a code cell."""
    found, current = {}, None
    for line in src.splitlines():
        head = HEAD.match(line)
        if head:
            current = int(head.group(1))
            found[current] = {}
            continue
        opt = OPTION.match(line)
        if opt and current is not None:
            found[current][opt.group(1)] = opt.group(2)
    return found


def fill(src, choice):
    """The code with each placeholder replaced by the chosen option's line."""
    opts = options_of(src)
    for n, letter in choice.items():
        if n in opts:
            src = src.replace(f"__TODO{n}__", opts[n][letter])
    return src


# =========================================================================== the escalated case
EX1_TITLE = ("# Can you answer Meera's three questions alone in fifty minutes, and ship a note under 200 words "
             "that survives Marketing?")

EX1_HEAD = '''
**Week 1, Thursday afternoon. The escalated case: 50 minutes, alone, straight after chapter 6.** Five
parts, twelve lettered choices, and a note of under 200 words at the end.

> **The client asks.** "One: Retail-Plus is down, smaller than first reported. Real, or the wobble we
> see every quarter? Two: Student is up 40 percent; should I move budget there? Three: marketing ran a
> monsoon-sale discount for Retail-Plus in August, says it lifted revenue 6 percent, and wants to
> repeat it for Diwali. Did the discount work, or did those customers buy anyway? One page, two
> minutes. If the honest answer is 'we do not know yet', say so and tell me what would tell us."
>
> Meera Raghavan, CEO, Kalpa Retail

**Who needs the answer.** Meera reads the page in two minutes before Monday's growth review, with the
marketing lead in the room ready to defend the monsoon sale. A line without its base sends money the
wrong way: a retention budget for a fall chance could have made, acquisition budget moved on a rate
whose count nobody checked, or a Diwali sale at 15 percent off for customers who would have bought
anyway.

**The questions on the way.**

1. Is the Retail-Plus fall larger than the wobble chance makes, counted in both directions?
2. How big is the fall against the company's quarter, and who gets the first test of the offer?
3. How many orders stand behind Student's 40 percent, and how often does chance make the rise?
4. Did the monsoon sale lift spend, and for whom?
5. How many customers does the Diwali hold-back keep out, and what does the note say?

Kalpa Retail sells through its app, its website and its stores, to four segments: Retail-Core and
Retail-Plus, its two consumer tiers, of which Retail-Plus is the paid membership; Student; and
Business, its sales to companies. The setup cell below loads the day's three files: Finance's
cleaned orders, 186 orders across Q1 and Q2; the campaign platform's August list, the exposure
table, 160 customers flagged by whether they got the sale; and the campaigns table, one campaign.
Revenue here is the money Kalpa kept, as Monday defined it, and recalling which orders that covers
is marker 1's question. The six chapters answered Meera's questions one at a time on these files,
and this case asks you to rebuild the answers alone, choosing every step, and to write them up.
Chapter 1 set a chance reference against the Retail-Plus fall and read its share both ways, chapter
2 sized the fall in rupees against the company and against a retention offer, chapter 3 counted what
Student's rate stands on, chapter 4 rebuilt Marketing's 6 percent and asked who got the sale,
chapter 5 wrote the four-part note, and chapter 6 asked what else changed in August and priced a
hold-back for Diwali.

A chance reference is a set of invented worlds in which nothing changed. The setup cell's `flip_gaps`
builds them by letting a coin decide, for each pair of values, which one counts as the first;
`shuffle_gaps` pools every value and deals it into two piles at random; `flip_rises` deals a count of
orders between two quarters by a coin per order. The share is the fraction of those worlds that make
a gap at least as large as the real one, counted for falls only or for a move that large in either
direction. A retention offer is a payment or perk meant to win back members' spend, assumed at Rs 500
a member a quarter. The rule of thumb from chapter 3 is to distrust a rate with fewer than thirty
customers behind it. A blend is one average across segments mixed together, a group's mix is its
make-up by segment, and a lift is how much more one group spent than another, as a share of the
other's spend. A hold-back is a group that a coin keeps out of a sale, so the rest can be compared
with it afterwards. The note has four parts: claim, evidence, caveat and action.
'''

EX1 = [
    ("todo_md", EX1_TITLE + "\n" + EX1_HEAD + '''
Each `__TODOn__` is a choice between the four lines in the comment above it: replace the placeholder
with the line you choose and run the cell. The check cell after each part compares what your choices
computed with the numbers they should reach, so a failing check sends you back to a choice in the part
above it. Run All stops at the first placeholder with a NameError until you replace it; that is
expected. Post the twelve letters in order at the end. The brief,
`exercises/unguided/C2_W01_D04_escalated_STUDENT.md`, carries the same case and its rules.
'''),
    ("solution_md", EX1_TITLE + "\n" + EX1_HEAD + '''
**This is the solution.** Every choice is filled with its key line, the notebook runs clean from a fresh
kernel, and the reason for each letter follows the cell that carries it.
'''),
    ("code", SETUP + '''
import random

ORDERS = kit.load_csv("C2_W01_D04_orders_STUDENT.csv")
EXPOSURE = kit.load_csv("C2_W01_D04_exposure_STUDENT.csv")
CAMPAIGNS = kit.load_csv("C2_W01_D04_campaigns_STUDENT.csv")
SEGMENTS = ["Retail-Core", "Retail-Plus", "Student", "Business"]


def mean(values):
    return sum(values) / len(values)
''' + FLIPS + '''

print(len(ORDERS), "orders in Finance's file,", len(EXPOSURE), "customers on the platform's list,", len(CAMPAIGNS), "campaign")
'''),
    ("md", '''
## Part 1. Is the Retail-Plus fall larger than the wobble chance makes, counted in both directions?

Used at work whenever a metric moves between two reviews and someone asks whether it moved at all.

The same 22 Retail-Plus members sit in both quarters. Choose which orders count, the chance
reference that fits members measured twice, and the count for a move that large in either direction.
Meera's question arrived after the fall was seen, so both directions go in the note.
'''),
    ("todo", '''
def kept(o):
    # TODO 1. Which orders count as money Kalpa kept?
    #   a) o["status"] != "cancelled"
    #   b) o["status"] == "delivered"
    #   c) o["amount"] != ""
    #   d) o["status"] in ("delivered", "returned")
    return __TODO1__


def member_totals(segment, quarter):
    members = sorted({o["customer_id"] for o in ORDERS if o["segment"] == segment})
    totals = {m: 0 for m in members}
    for o in ORDERS:
        if o["segment"] == segment and o["quarter"] == quarter and kept(o):
            totals[o["customer_id"]] += int(o["amount"])
    return [totals[m] for m in members]


plus_q1, plus_q2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
plus_gap = mean(plus_q1) - mean(plus_q2)
# TODO 2. The same 22 members sit in both quarters. Which chance reference fits?
#   a) shuffle_gaps(plus_q1, plus_q2, 5000, seed=2026)
#   b) flip_rises(len(plus_q1), 5000, seed=2026)
#   c) flip_gaps(plus_q1, plus_q2, 5000, seed=2026)
#   d) shuffle_gaps(plus_q1, plus_q1, 5000, seed=2026)
gaps = __TODO2__
falls_share = sum(1 for g in gaps if g >= plus_gap) / len(gaps)
# TODO 3. Which count gives the share of a move that large in either direction?
#   a) sum(1 for g in gaps if g <= plus_gap) / len(gaps)
#   b) sum(1 for g in gaps if abs(g) >= abs(plus_gap)) / len(gaps)
#   c) sum(1 for g in gaps if abs(g) <= abs(plus_gap)) / len(gaps)
#   d) 2 * sum(1 for g in gaps if g >= plus_gap) / len(gaps)
either_share = __TODO3__
kit.strip(gaps[:150], markers=[("real gap", plus_gap, "bad")], lo=-2500, hi=2500,
          title="Retail-Plus: 150 of the 5,000 chance-only worlds, with the real gap marked")
print(f"real gap Rs {plus_gap:,.0f} per member; falls only {falls_share:.3f}; either way {either_share:.3f}")
''', {1: ("b", "Monday settled that delivered orders are the money Kalpa kept. a keeps returned orders, whose money went back; c keeps every order, cancelled ones included; d counts returns as sales."),
      2: ("c", "The same members sit in both quarters, so the chance reference flips each member's own pair. a pools the 44 totals as if they were 44 different customers, which is the test for two groups of strangers; b deals orders by coin, the reference for a count of orders; d shuffles Q1 against itself, so no gap can appear."),
      3: ("b", "A move that large either way is a flip whose size, up or down, reaches the real gap. a counts every gap at or below the real one, which is nearly every world; c counts moves at most that large, the complement; d doubles the one-direction share, which lands near the count here (0.058) and is still an estimate where the count is exact.")}),
    ("code", '''
kit.check("the real gap is Rs 1,110 per member", round(plus_gap) == 1110, f"{plus_gap:,.1f}")
kit.check("counting falls only, the share is 0.029 with seed 2026", round(falls_share, 3) == 0.029, f"{falls_share:.4f}")
kit.check("counting either way, the share is 0.057 with seed 2026", round(either_share, 3) == 0.057, f"{either_share:.4f}")
'''),
    ("md", '''
## Part 2. How big is the fall against the company's quarter, and who gets the first test of the offer?

Used at work whenever a team asks for a budget to fix a fall, before anyone signs it off.

The retention offer is assumed at Rs 500 a member a quarter. It is sized on Finance's order file,
where the tier is these 22 members, and the fall is borderline, so the first step is a test.
'''),
    ("todo", '''
def revenue(segment, quarter):
    return sum(int(o["amount"]) for o in ORDERS
               if o["segment"] == segment and o["quarter"] == quarter and kept(o))


company_q1 = sum(revenue(s, "Q1") for s in SEGMENTS)
company_q2 = sum(revenue(s, "Q2") for s in SEGMENTS)
# TODO 4. What is the segment's fall in rupees a quarter?
#   a) plus_gap * len(plus_q1)
#   b) plus_gap
#   c) plus_gap / len(plus_q1)
#   d) sum(plus_q1) - plus_gap * 100
plus_fall = __TODO4__
# TODO 5. What is the fall measured against, for Meera?
#   a) sum(plus_q1)
#   b) len(ORDERS)
#   c) revenue("Retail-Core", "Q2")
#   d) company_q2
share_of_company = plus_fall / __TODO5__

members = sorted({o["customer_id"] for o in ORDERS if o["segment"] == "Retail-Plus"})
fall_by_member = dict(zip(members, [a - b for a, b in zip(plus_q1, plus_q2)]))
random.seed(2026)
coin_half = sorted(random.sample(members, len(members) // 2))
fell_most = sorted(members, key=lambda m: -fall_by_member[m])[:len(members) // 2]
# TODO 6. The fall is borderline and the offer costs Rs 500 a member. Who gets it in the first test?
#   a) members
#   b) fell_most
#   c) coin_half
#   d) members[:len(members) // 2]
offered = __TODO6__
held_back = [m for m in members if m not in offered]
kit.bridge(("company, Q1", company_q1), [(s, revenue(s, "Q2") - revenue(s, "Q1")) for s in SEGMENTS],
           end_label="company, Q2", lo=12_000_000, lit=[1], title="Revenue kept by segment, Q1 to Q2 (axis from Rs 1.2 crore)")
print(f"the fall {kit.rupees(round(plus_fall))} a quarter; the test offers {len(offered)} members and holds back {len(held_back)}")
''', {4: ("a", "A per-member gap times the members who exist in both quarters is the segment's fall. b is still per member; c divides again; d mixes a total with a gap."),
      5: ("d", "Meera runs the company, so the fall is set against the company's quarter. a sizes it against the tier's own Q1, which is the head of Retail-Plus's view; b is a count of orders; c sets it against another segment."),
      6: ("c", "A borderline fall and an offer that must win back 45 percent call for a test, and a coin makes the two halves alike before the offer, so any gap after it belongs to the offer. a spends Rs 11,000 and leaves nobody to compare with; b offers it to the members who fell most, who also spent most in Q1, so the halves start Rs 2,490 apart and drift back toward the average whatever the offer does; d splits by customer id, which here puts the bigger Q1 spenders on one side, Rs 1,025 apart.")}),
    ("code", '''
q1_by_member = dict(zip(members, plus_q1))
apart = (abs(mean([q1_by_member[m] for m in offered]) - mean([q1_by_member[m] for m in held_back]))
         if offered and held_back else float("inf"))
kit.check("the fall is Rs 24,420 a quarter", round(plus_fall) == 24420, kit.rupees(round(plus_fall)))
kit.check("the fall is 0.19 percent of the base Meera sets it against", round(share_of_company, 4) == 0.0019,
          f"{share_of_company:.2%}")
kit.check("the first test costs Rs 5,500 a quarter and holds back as many members as it offers",
          500 * len(offered) == 5500 and len(held_back) == len(offered), kit.rupees(500 * len(offered)))
kit.check("the offered and held-back halves spent within Rs 500 of each other in Q1", apart < 500,
          "nobody held back" if apart == float("inf") else f"Rs {apart:,.0f} apart")
'''),
    ("md", '''
## Part 3. How many orders stand behind Student's 40 percent, and how often does chance make the rise?

Used at work on every leaderboard of stores, cities or segments ranked by a rate.

The count is yours to find, and nothing below prints it: the check cell reaches it through the shares
it drives. The coin flips count orders; the rule of thumb counts customers, since more orders from the
same few customers add no new evidence.
'''),
    ("todo", '''
def orders_in(segment, quarter):
    return sum(1 for o in ORDERS if o["segment"] == segment and o["quarter"] == quarter)


index_student = round(100 * orders_in("Student", "Q2") / orders_in("Student", "Q1"))
# TODO 7. How many orders stand behind Student's 40 percent, for the coin flips?
#   a) orders_in("Student", "Q2")
#   b) sum(1 for o in ORDERS if o["segment"] == "Student")
#   c) index_student
#   d) orders_in("Student", "Q2") - orders_in("Student", "Q1")
student_n = __TODO7__
# TODO 8. Which chance reference fits a count of orders?
#   a) flip_rises(student_n, 5000, seed=2026)
#   b) flip_gaps([student_n], [0], 5000, seed=2026)
#   c) flip_rises(400, 5000, seed=2026)
#   d) [0.4] * 5000
rises = __TODO8__
student_share = sum(1 for r in rises if r >= 0.4 - 1e-9) / len(rises)
kit.columns(["fell", "rose under 40%", "rose 40% or more"],
            [("coin-flip worlds", [sum(1 for r in rises if r < 0), sum(1 for r in rises if 0 <= r < 0.4 - 1e-9),
                                   sum(1 for r in rises if r >= 0.4 - 1e-9)])],
            lit=[2], width=620, title="Student's orders dealt to quarters by coin flip, 5,000 times")
''', {7: ("b", "The coin flips deal every order the rate stands on, both quarters together. a counts only Q2; c is the rate itself; d is the change between the quarters. The rule of thumb then asks how many customers placed those orders, which the note reports in words."),
      8: ("a", "A coin flip per order on Student's own count is the chance reference for a count. b treats the count as one member's two quarters; c deals 400 orders, the size chapter 3 invented for a large segment; d assumes the answer.")}),
    ("code", '''
from math import comb

exact = sum(comb(student_n, k) for k in range(student_n + 1)
            if k == student_n or k / (student_n - k) - 1 >= 0.4 - 1e-9) / 2 ** student_n
kit.check("Student's orders rose 40 percent", index_student == 140)
kit.check("every deal of your count, listed exactly, makes the rise in 0.387 of them", round(exact, 3) == 0.387,
          f"{exact:.3f}")
kit.check("your chance reference makes the rise in 0.397 of worlds with seed 2026", round(student_share, 3) == 0.397,
          f"{student_share:.3f}")
'''),
    ("md", '''
## Part 4. Did the monsoon sale lift spend, and for whom?

Used at work on every campaign readout, before anyone runs the campaign again.

The exposure table is the campaign platform's August list: the 160 Retail-Plus and Retail-Core
customers the platform held, under the platform's own customer ids, with one average August spend
for each group. It records who received the sale, whatever the sale was aimed at, which is why it
counts Retail-Core customers among them although the campaigns table aimed the sale at Retail-Plus.
It cannot be matched to Finance's order file, whose 22 Retail-Plus members and discount column carry
no record of the sale. Read it for who got the sale and how the two groups differ.
'''),
    ("todo", '''
# TODO 9. Which rows are the customers who got the discount?
#   a) r["campaign_id"] == ""
#   b) r["segment"] == "Retail-Plus"
#   c) int(r["august_revenue"]) > 3200
#   d) r["exposed"] == "yes"
exposed = [r for r in EXPOSURE if __TODO9__]
others = [r for r in EXPOSURE if r not in exposed]
blend_yes = mean([int(r["august_revenue"]) for r in exposed])
blend_no = mean([int(r["august_revenue"]) for r in others])
blend_lift = blend_yes / blend_no - 1
print(f"blended: exposed {kit.rupees(blend_yes)} against {kit.rupees(blend_no)}, {blend_lift:+.1%}")


def avg(segment, flag):
    return mean([int(r["august_revenue"]) for r in EXPOSURE if r["segment"] == segment and r["exposed"] == flag])


def count(flag, segment=None):
    return sum(1 for r in EXPOSURE if r["exposed"] == flag and (segment is None or r["segment"] == segment))


# TODO 10. Marketing will read this comparison first. Which one is fair?
#   a) {s: avg(s, "yes") / blend_no - 1 for s in ["Retail-Plus", "Retail-Core"]}
#   b) {s: avg(s, "yes") / avg(s, "no") - 1 for s in ["Retail-Plus", "Retail-Core"]}
#   c) {"everyone": blend_lift}
#   d) {s: avg(s, "yes") / avg("Retail-Plus", "no") - 1 for s in ["Retail-Plus", "Retail-Core"]}
within = __TODO10__
# TODO 11. What share of the exposed customers are Retail-Plus members?
#   a) count("yes", "Retail-Plus") / count("yes")
#   b) count("no", "Retail-Plus") / count("no")
#   c) count("yes", "Retail-Plus") / len(EXPOSURE)
#   d) count("yes") / len(EXPOSURE)
plus_mix_exposed = __TODO11__
plus_mix_others = count("no", "Retail-Plus") / count("no")
kit.columns(["Retail-Plus", "Retail-Core", "blended"],
            [("not exposed", [avg("Retail-Plus", "no"), avg("Retail-Core", "no"), round(blend_no)]),
             ("exposed", [avg("Retail-Plus", "yes"), avg("Retail-Core", "yes"), round(blend_yes)])],
            fmt=kit.rupees, lit=[2], title="August spend per customer: each segment, and the blend")
kit.columns(["exposed", "not exposed"], [("share who are Retail-Plus", [round(100 * plus_mix_exposed), round(100 * plus_mix_others)])],
            fmt=lambda v: f"{v:.0f}%", width=560, title="Who got the discount: the mix of the two groups")
''', {9: ("d", "The exposure flag records who got the discount. a picks the customers with no campaign, the opposite group; b picks a segment; c picks customers by what they spent, which is the outcome being measured."),
      10: ("b", "The fair comparison runs inside each segment, exposed against unexposed customers of the same kind. a sets each segment's exposed against every unexposed customer, the comparison Marketing makes in the second case; c is the blend again; d sets Retail-Core's exposed against Retail-Plus's unexposed."),
      11: ("a", "Retail-Plus members over all exposed customers is the mix of the exposed group. b is the unexposed group's mix; c divides by every customer on the list; d is the exposed share of the list.")}),
    ("code", '''
kit.check("the blend rises 6.1 percent, as Marketing reported", round(blend_lift, 3) == 0.061, f"{blend_lift:+.1%}")
kit.check("the fair comparison finds 3.0 percent less in each of the two segments",
          sorted(round(v, 3) for v in within.values()) == [-0.03, -0.03],
          ", ".join(f"{s} {v:+.1%}" for s, v in within.items()))
kit.check("half of the exposed customers are Retail-Plus members", round(plus_mix_exposed, 2) == 0.5, f"{plus_mix_exposed:.0%}")
'''),
    ("md", '''
## Part 5. How many customers does the Diwali hold-back keep out, and what does the note say?

Used at work whenever a team plans a campaign it will have to prove afterwards, and whenever a CEO
wants the answer on one page.

Marketing wants the sale again at Diwali. A coin will keep one in five customers out of it, inside
each segment, so the rest can be compared with them afterwards. Choose whom the coin draws from.
'''),
    ("todo", '''
finance_members = plus_q1                                  # Finance's order file: one total per Retail-Plus member
platform_plus = [r for r in EXPOSURE if r["segment"] == "Retail-Plus"]
platform_plus_exposed = [r for r in platform_plus if r["exposed"] == "yes"]
# TODO 12. How many Retail-Plus customers does the coin hold back?
#   a) len(finance_members) // 5
#   b) len(platform_plus_exposed) // 5
#   c) len(platform_plus) // 5
#   d) len(EXPOSURE) // 5
held = __TODO12__
forgone = round(held * avg("Retail-Plus", "no") * 0.06)
kit.vflow(["before Diwali: a coin per customer on the list the sale runs on", "one in five held back, inside each segment",
           "the sale runs for the rest, same window", "after: held back against got it, inside each segment"],
          lit=1, title="The Diwali comparison, decided before the sale")
kit.stats([(f"{held}", "Retail-Plus held back", "one in five"),
           (kit.rupees(forgone), "forgone", "if Marketing's 6 percent were real")])
''', {12: ("c", "The sale runs on the platform's list, so the hold-back is one in five of its Retail-Plus customers, exposed last time or not. a takes Finance's members, a different list with different ids; b samples only the customers Marketing picked last time; d takes both segments at once, so Retail-Plus's slice is no longer one in five.")}),
    ("code", '''
kit.check("the hold-back forgoes about Rs 4,200 at Marketing's own 6 percent", forgone == 4200, kit.rupees(forgone))
'''),
    ("todo_md", '''
**Your note.** Replace the text in the cell below with your note: claim, evidence, caveat, action,
under 200 words, for Retail-Plus, Student and the discount, with both directions beside the
Retail-Plus share.
'''),
    ("todo_code", '''
note = """Paste your note here."""
words = len(note.split())
print(words, "words")
kit.check("the note is under 200 words", words < 200, f"{words}")
kit.check("the note gives each question a line", all(k in note for k in ("Retail-Plus", "Student", "sale")))
kit.check_summary()
print("Post the twelve letters in order, then read your note aloud to your partner.")
'''),
    ("solution_md", '''
## So what does the note to Meera say, in 190 words?

**Claim.** Retail-Plus is down by a borderline amount and small against the company; Student is too
thin to fund yet; the monsoon sale did not work as designed.

**Evidence.** Retail-Plus members delivered Rs 1,110 less each in Q2; if nothing had changed, a fall
that large turns up in about 3 of 100 flips, and a move that large either way in about 6. It is Rs
24,420 a quarter, 0.19 percent of delivered revenue. Student's 40 percent rise comes from very few
customers, and coin flips make it in four worlds of ten. The sale's 6 percent is a blend: inside
Retail-Plus and Retail-Core, exposed customers spent 3 percent less.

**Caveat.** We asked after seeing the fall. The group who got the sale was half Retail-Plus against
40 percent of the rest, and Retail-Plus spends more anyway; the platform's list gives one August
figure per group, so we cannot see the spread.

**Action.** Watch Retail-Plus, and if we act, test the offer on a coin-chosen half; watch Student until
more customers buy, thirty or more; do not repeat the sale as designed, and hold back a random slice
of each segment at Diwali.
'''),
    ("solution_code", '''
note = """Retail-Plus is down by a borderline amount and small against the company; Student is too thin to
fund yet; the monsoon sale did not work as designed. Retail-Plus members delivered Rs 1,110 less each in
Q2; if nothing had changed, a fall that large turns up in about 3 of 100 flips, and a move that large
either way in about 6. It is Rs 24,420 a quarter, 0.19 percent of delivered revenue. Student's 40 percent
rise comes from very few customers, and coin flips make it in four worlds of ten. The sale's 6 percent is
a blend: inside Retail-Plus and Retail-Core, exposed customers spent 3 percent less. We asked after seeing
the fall. The group who got the sale was half Retail-Plus against 40 percent of the rest, and Retail-Plus
spends more anyway; the platform's list gives one August figure per group, so we cannot see the spread.
Watch Retail-Plus, and if we act, test the offer on a coin-chosen half; watch Student until more
customers buy, thirty or more; do not repeat the sale as designed, and hold back a random slice of each
segment at Diwali."""
words = len(note.split())
print(words, "words")
kit.check("the note is under 200 words", words < 200, f"{words}")
kit.check("the note gives each question a line", all(k in note for k in ("Retail-Plus", "Student", "sale")))
kit.check_summary()
print("Post the twelve letters in order, then read your note aloud to your partner.")
'''),
]

# =========================================================================== the second case
EX2_TITLE = ("# Marketing calls the segment split cherry-picking and brings Rs 4,850 against Rs 3,200: is their "
             "comparison fair, and how do you hold the line?")

EX2_HEAD = '''
**Week 1, Thursday afternoon. The second case: 34 minutes in pairs, inside a 40-minute slot.** Four
parts and eight lettered choices, then the reply spoken aloud to a partner playing Marketing.

> **The client asks.** "Your segment split is slicing the data until it says what you want. Exposed
> Retail-Plus members spent Rs 4,850 in August. That is far above the Rs 3,200 our unexposed customers
> averaged. The sale works. We repeat it for Diwali."
>
> The marketing lead, Kalpa Retail, in the growth review with Meera listening

**Who needs the answer.** Meera Raghavan, Kalpa Retail's CEO, is listening, and she signs off the
Diwali sale. If the pair cannot answer a correct number that rests on an unfair comparison, the sale
goes out again at 15 percent off to customers who would have bought anyway; if the pair calls
Marketing's arithmetic wrong, it loses the room with a reading that was right.

**The questions on the way.**

1. Can you make Marketing's Rs 4,850 and Rs 3,200 appear from the platform's list?
2. Who sits in each of Marketing's two groups, and what else differs between them?
3. Compared like for like, how do exposed and unexposed customers differ, and how many stand behind each?
4. If the list's August spend is at list price, what did the exposed pay Kalpa, and what would a Diwali
   hold-back cost?

Kalpa Retail's monsoon sale ran 15 percent off in August, aimed at Retail-Plus, Kalpa's paid
membership tier; Retail-Core is Kalpa's other consumer tier. The setup cell below loads the
campaigns table and the table this case reads. The table is the campaign platform's August list: 160
Retail-Plus and Retail-Core customers under the platform's own ids, with one average August spend
for each group. A customer is exposed if the monsoon sale reached them and unexposed if it did not.
Chapter 4 split this list by segment and found that inside Retail-Plus and inside Retail-Core the
exposed customers spent 3.0 percent less than the unexposed, while the blend, one average over both
segments mixed together, rose 6.1 percent. Marketing now calls that split cherry-picking. A group's
mix is its make-up by segment; like for like means the same segment on both sides of a comparison;
list price is the price before any discount; and a hold-back is a slice of customers that a coin
keeps out of a sale, so the rest can be compared with them afterwards.
'''

EX2 = [
    ("todo_md", EX2_TITLE + "\n" + EX2_HEAD + '''
Replace each `__TODOn__` with the line you choose from the comment above it; the check cell after each
part compares what your choices computed with the numbers they should reach. Run All stops at the
first placeholder until you do. The brief, `exercises/unguided/C2_W01_D04_pushback_STUDENT.md`,
carries the same case and the pair's rules.
'''),
    ("solution_md", EX2_TITLE + "\n" + EX2_HEAD + '''
**This is the solution.** Every choice is filled with its key line, the notebook runs clean from a fresh
kernel, and the reason for each letter follows the cell that carries it.
'''),
    ("code", SETUP + '''
EXPOSURE = kit.load_csv("C2_W01_D04_exposure_STUDENT.csv")
CAMPAIGN = kit.load_csv("C2_W01_D04_campaigns_STUDENT.csv")[0]
PAIR = ["Retail-Plus", "Retail-Core"]


def mean(values):
    return sum(values) / len(values)


def avg(segment, flag):
    return mean([int(r["august_revenue"]) for r in EXPOSURE if r["segment"] == segment and r["exposed"] == flag])


def count(flag, segment=None):
    return sum(1 for r in EXPOSURE if r["exposed"] == flag and (segment is None or r["segment"] == segment))


print(CAMPAIGN["name"], CAMPAIGN["starts"], "to", CAMPAIGN["ends"], "at", CAMPAIGN["discount_pct"], "percent off,",
      "targeted at", CAMPAIGN["target_segment"], ";", len(EXPOSURE), "customers on the platform's list")
'''),
    ("md", '''
## Part 1. Can you make Marketing's Rs 4,850 and Rs 3,200 appear from the platform's list?

Used at work as the first reply to any stakeholder who brings a number into a meeting.

A pushback is answered from the same table, so first make both numbers appear.
'''),
    ("todo", '''
# TODO 1. Which line reproduces Marketing's Rs 4,850?
#   a) avg("Retail-Plus", "no")
#   b) avg("Retail-Plus", "yes")
#   c) avg("Retail-Core", "yes")
#   d) mean([int(r["august_revenue"]) for r in EXPOSURE])
marketing_yes = __TODO1__
# TODO 2. Which line reproduces Marketing's Rs 3,200?
#   a) avg("Retail-Core", "no")
#   b) avg("Retail-Plus", "no")
#   c) mean([int(r["august_revenue"]) for r in EXPOSURE if r["exposed"] == "no"])
#   d) mean([int(r["august_revenue"]) for r in EXPOSURE if r["exposed"] == "no" and r["segment"] == "Retail-Plus"])
marketing_no = __TODO2__
kit.columns(["exposed Retail-Plus", "all unexposed"], [("August spend per customer", [marketing_yes, round(marketing_no)])],
            fmt=kit.rupees, width=560, title="Marketing's comparison, reproduced")
''', {1: ("b", "Marketing quoted exposed Retail-Plus members. a is the unexposed Retail-Plus average; c is exposed Retail-Core; d averages the whole list."),
      2: ("c", "Marketing's Rs 3,200 is every unexposed customer, both segments together. a and b are one segment each; d keeps only unexposed Retail-Plus, which gives Rs 5,000.")}),
    ("code", '''
kit.check("Marketing's Rs 4,850 is reproduced", marketing_yes == 4850, kit.rupees(marketing_yes))
kit.check("Marketing's Rs 3,200 is reproduced", round(marketing_no) == 3200, kit.rupees(marketing_no))
'''),
    ("md", '''
## Part 2. Who sits in each of Marketing's two groups, and what else differs between them?

Used at work whenever two groups are compared on an average.

Look at who sits in each of Marketing's two groups before judging the gap between them.
'''),
    ("todo", '''
mix_yes = {s: count("yes", s) / count("yes") for s in PAIR}
mix_no = {s: count("no", s) / count("no") for s in PAIR}
kit.table(["Group", "Customers", "Retail-Plus", "Retail-Core"],
          [("exposed", count("yes"), count("yes", "Retail-Plus"), count("yes", "Retail-Core")),
           ("not exposed", count("no"), count("no", "Retail-Plus"), count("no", "Retail-Core"))],
          caption="Who is in each group")
kit.columns(PAIR, [("share of exposed", [round(100 * mix_yes[s]) for s in PAIR]),
                   ("share of not exposed", [round(100 * mix_no[s]) for s in PAIR])],
            fmt=lambda v: f"{v:.0f}%", width=560, title="The mix of the two groups")
# TODO 3. Marketing's Rs 3,200 averages every unexposed customer. What share of them are Retail-Core?
#   a) count("no", "Retail-Core") / len(EXPOSURE)
#   b) count("yes", "Retail-Core") / count("yes")
#   c) mix_no["Retail-Plus"]
#   d) count("no", "Retail-Core") / count("no")
core_share_unexposed = __TODO3__
''', {3: ("d", "Retail-Core customers over all unexposed customers is the unexposed group's make-up: three in five. a divides by the whole list; b is the exposed group's Retail-Core share; c is the unexposed Retail-Plus share, the other two in five.")}),
    ("code", '''
kit.check("three in five of Marketing's unexposed customers are Retail-Core", round(core_share_unexposed, 2) == 0.6,
          f"{core_share_unexposed:.0%}")
'''),
    ("md", '''
## Part 3. Compared like for like, how do exposed and unexposed customers differ, and how many stand behind each?

Used at work on every campaign readout that reaches a budget meeting.

Two fair versions: each segment's exposed customers against the same segment's unexposed, and the
exposed group reweighted so that its average compares fairly with Marketing's Rs 3,200. Every
average you quote carries the customers behind it.
'''),
    ("todo", '''
def like_for_like(s):
    # TODO 4. Like for like, what does each segment's exposed average go against?
    #   a) avg(s, "no")
    #   b) marketing_no
    #   c) avg("Retail-Core", "no")
    #   d) avg(s, "yes")
    return avg(s, "yes") / __TODO4__ - 1


plus_like, core_like = like_for_like("Retail-Plus"), like_for_like("Retail-Core")
# TODO 5. Which weights make the exposed group's average comparable with Marketing's Rs 3,200?
#   a) mix_yes[s]
#   b) mix_no[s]
#   c) 0.5
#   d) count("yes", s) / len(EXPOSURE) * 2
reweighted_yes = sum(__TODO5__ * avg(s, "yes") for s in PAIR)
fair_lift = reweighted_yes / marketing_no - 1
# TODO 6. How many customers stand behind the like-for-like Retail-Plus comparison, exposed and not?
#   a) (count("yes"), count("no"))
#   b) (count("yes", "Retail-Plus"), count("no", "Retail-Core"))
#   c) (len(EXPOSURE), 0)
#   d) (count("yes", "Retail-Plus"), count("no", "Retail-Plus"))
like_counts = __TODO6__
kit.columns(PAIR, [("not exposed", [avg(s, "no") for s in PAIR]), ("exposed", [avg(s, "yes") for s in PAIR])],
            fmt=kit.rupees, width=560, title="Like for like: each segment, exposed against not exposed")
kit.bridge(("Marketing's Rs 3,200", round(marketing_no)), [("the sale, reweighted", round(reweighted_yes - marketing_no))],
           end_label="exposed, reweighted", lo=2500, title="The exposed group reweighted to compare with Rs 3,200 (axis from Rs 2,500)")
print(f"Retail-Plus {plus_like:+.1%} on {like_counts}, Retail-Core {core_like:+.1%}, reweighted {fair_lift:+.1%}")
''', {4: ("a", "Like for like sets each segment's exposed customers against the same segment's unexposed customers: Retail-Plus Rs 4,850 against Rs 5,000. b is Marketing's mixed group again; c sets every segment against Retail-Core's unexposed customers; d divides the group by itself."),
      5: ("b", "Marketing's Rs 3,200 averages the unexposed group in its own mix, 40 percent Retail-Plus and 60 percent Retail-Core, so weighting the exposed segment averages by that mix removes the mix difference. a keeps the exposed mix, which rebuilds the blend; c is an even split, which on this list is the exposed mix again; d divides by the whole list and doubles, which matches neither group."),
      6: ("d", "The like-for-like comparison stands on 30 exposed and 40 unexposed Retail-Plus customers. a counts the two whole groups, the blend's base; b sets exposed Retail-Plus against unexposed Retail-Core; c counts the list with nobody against it.")}),
    ("code", '''
kit.check("the like-for-like Retail-Plus comparison comes to 3.0 percent less", round(plus_like, 3) == -0.03,
          f"{plus_like:+.1%}")
kit.check("reweighted to compare with Rs 3,200, the exposed group comes to 3.0 percent less", round(fair_lift, 3) == -0.03,
          f"{fair_lift:+.1%}")
kit.check("the like-for-like comparison stands on 30 exposed and 40 unexposed customers", like_counts == (30, 40),
          f"{like_counts}")
'''),
    ("md", '''
## Part 4. If the list's August spend is at list price, what did the exposed pay Kalpa, and what would a Diwali hold-back cost?

Used at work whenever a discount's cost has to be set against the lift claimed for it.

The platform's list does not say whether its August spend is counted before or after the 15 percent
off. Suppose it is counted at list price, before the discount, and size what the exposed customers
actually paid Kalpa. Then size the Diwali hold-back the pair will offer, on the same list. The
hold-back is priced at Marketing's own 6 percent lift on the unexposed averages: each customer a coin
keeps out of the sale forgoes 6 percent of what an unexposed customer of the same segment spent.
'''),
    ("todo", '''
off = int(CAMPAIGN["discount_pct"]) / 100
blend_yes = mean([int(r["august_revenue"]) for r in EXPOSURE if r["exposed"] == "yes"])
# TODO 7. At list price, how did what the exposed paid Kalpa compare with what the unexposed paid?
#   a) blend_yes * (1 - off) / marketing_no - 1
#   b) blend_yes / marketing_no - 1 - off
#   c) blend_yes / (marketing_no * (1 - off)) - 1
#   d) (blend_yes - off) / marketing_no - 1
paid_gap = __TODO7__
# TODO 8. A coin keeps one in five out of the Diwali sale inside each segment on the list. How many is that?
#   a) {s: count("yes", s) // 5 for s in PAIR}
#   b) {s: (count("yes", s) + count("no", s)) // 5 for s in PAIR}
#   c) {s: count("no", s) for s in PAIR}
#   d) {"Retail-Plus": (count("yes", "Retail-Plus") + count("no", "Retail-Plus")) // 5}
held = __TODO8__
forgone = round(sum(held[s] * avg(s, "no") * 0.06 for s in held))
kit.flow(["reproduce\\nRs 4,850 and Rs 3,200", "mismatch\\nwho is in each group", "like for like\\n3 percent less",
          "the offer\\na coin, one in five"], lit=3, title="The pair's four parts")
print(f"at list price the exposed paid {paid_gap:+.1%} against the unexposed; the hold-back {held}, "
      f"forgoing {kit.rupees(forgone)} if Marketing's 6 percent were real")
''', {7: ("a", "At list price an exposed customer paid 85 percent of the figure on the list, so the exposed group paid about Rs 2,886 per customer against Rs 3,200: 9.8 percent less. b subtracts a price cut from a spend gap, two different quantities; c discounts the unexposed group, who paid full price; d takes 0.15 of a rupee off the average."),
      8: ("b", "One in five of each segment's customers on the list, exposed last time or not, is 14 Retail-Plus and 18 Retail-Core. a samples only the customers Marketing picked last time; c holds back every unexposed customer, which is the old unfair split; d leaves Retail-Core out, so a lift there could never be checked.")}),
    ("code", '''
kit.check("counted at list price, the exposed paid Kalpa about 9.8 percent less per customer than the unexposed",
          round(paid_gap, 3) == -0.098, f"{paid_gap:+.1%}")
kit.check("the hold-back forgoes about Rs 6,360 across both segments at Marketing's own 6 percent", forgone == 6360,
          kit.rupees(forgone))
'''),
    ("md", '''
**The reply.** Say it aloud to your partner playing Marketing, in two sentences: the like-for-like
comparison with its counts, the list-price question Marketing has to answer, and the Diwali hold-back
with what it costs.
'''),
    ("solution_md", '''
## So is Marketing's comparison fair, and what reply holds the line?

Marketing's arithmetic is right and its comparison is not: the unexposed group is three in five
Retail-Core, who spend less anyway, and like for like the exposed spent 3.0 percent less, on 30 and
40 Retail-Plus customers. What the pair says in the meeting: "We split it because the sale reached
more Retail-Plus members, who spend more anyway: inside Retail-Plus, the 30 customers who got the sale
spent 3 percent less than the 40 who did not, and if your August figures are at list price, the
exposed group paid Kalpa about 10 percent less per customer. Let us hold back one in five of each
segment at Diwali, which costs about Rs 6,360 even at your 6 percent, and we will know."
'''),
    ("code", '''
kit.check_summary()
print("Post the eight letters in order, then say the reply aloud to your partner playing Marketing.")
'''),
]

# =========================================================================== the practice lab's problem 3
EX3_TITLE = ("# On Monday's 24-order sample, do Retail-Plus baskets beat Retail-Core's, or is the lead the wobble "
             "chance makes?")

EX3_HEAD = '''
**Week 1, Thursday. The TA-led practice lab, problem 3: 20 minutes, in pairs.** Five lettered choices
on Monday's take-home sample.

> **The client asks.** "Do Retail-Plus members really buy bigger baskets than Retail-Core, or is that
> just what we expect of a paid tier?" The head of Retail-Plus

**Who needs the answer.** The head of Retail-Plus, who watches whether members' fees cover what their
benefits cost and would put bigger baskets into that case. A lead that chance or a definition made
would carry the case on a difference that is not there.

**The questions on the way.**

1. Do Retail-Plus baskets lead on every booked order, and how often does chance make that lead?
2. Does the lead survive on the money Kalpa kept, and which share goes in the line?

The setup cell below loads Monday's take-home sample, 24 orders you have already counted once.
Retail-Plus and Retail-Core are Kalpa Retail's two consumer tiers, of which Retail-Plus is the paid
membership; the sample also holds Student orders and Business orders, Business being Kalpa's sales
to companies. A basket is one order's amount. Booked orders are every order placed, whatever
happened to it afterwards. Which orders count as the money Kalpa kept is Monday's definition, and
recalling it is marker 4's question, so it is not repeated here. Chapter 1 flipped each Retail-Plus
member's two quarters because the same members sat in both; the two tiers' baskets are different
customers' orders, with no pairs to flip, so the chance reference here is the label shuffle, as in
chapter 6: `shuffle_gaps` pools every basket and deals the baskets at random into two piles of the
tiers' sizes, 5,000 times, and the share, the p-value, is the fraction of deals that make a lead at
least as large as the real one; a lead that chance makes often is part of the usual wobble, the
movement chance alone makes between two groups. Chapter 3's rule of thumb is to distrust a
comparison with fewer than thirty customers behind it.
'''

EX3 = [
    ("todo_md", EX3_TITLE + "\n" + EX3_HEAD + '''
Replace each `__TODOn__` with the line you choose; the check cell after each step compares what your
choices computed with the numbers they should reach. Run All stops at the first placeholder until you
do. Post the five letters on their own line; problem 4 of the lab is on paper.
'''),
    ("solution_md", EX3_TITLE + "\n" + EX3_HEAD + '''
**This is the solution.** Every choice is filled with its key line, the notebook runs clean from a fresh
kernel, and the reason for each letter follows the cell that carries it.
'''),
    ("code", SETUP + '''
import random

ORDERS = kit.load_records("C2_W01_D04_monday_sample_STUDENT.py")


def mean(values):
    return sum(values) / len(values)


def shuffle_gaps(q1, q2, times, seed):
    """Two groups of different customers: deal every value to two piles at random, many times."""
    random.seed(seed)
    pool = q1 + q2
    gaps = []
    for _ in range(times):
        random.shuffle(pool)
        gaps.append(mean(pool[:len(q1)]) - mean(pool[len(q1):]))
    return gaps


print(len(ORDERS), "orders in Monday's sample")
'''),
    ("md", '''
## Step 1. Do Retail-Plus baskets lead on every booked order, and how often does chance make that lead?

Used at work whenever two customer groups are compared on a small file.
'''),
    ("todo", '''
# TODO 1. Which orders belong in a basket comparison between the two consumer tiers?
#   a) r["segment"] != "Student"
#   b) True
#   c) r["segment"] in ("Retail-Plus", "Retail-Core")
#   d) r["segment"] in ("Retail-Plus", "Retail-Core", "Business")
tiers = [r for r in ORDERS if __TODO1__]
# TODO 2. How does each amount become a number the loop can average?
#   a) int(r["amount"])
#   b) r["amount"]
#   c) int(r["amount"]) if r["status"] == "delivered" else 0
#   d) len(str(r["amount"]))
plus = [__TODO2__ for r in tiers if r["segment"] == "Retail-Plus"]
core = [__TODO2__ for r in tiers if r["segment"] == "Retail-Core"]
real = mean(plus) - mean(core)
gaps = shuffle_gaps(plus, core, 5000, seed=2026)
# TODO 3. Which share is the p-value for a Retail-Plus lead at least as large?
#   a) sum(1 for g in gaps if g <= real) / len(gaps)
#   b) sum(1 for g in gaps if g >= real) / len(gaps)
#   c) real / max(gaps)
#   d) sum(1 for g in gaps if abs(g) >= abs(real) * 2) / len(gaps)
share_booked = __TODO3__
kit.strip(gaps[:150], markers=[("real lead", real, "bad")], lo=-2500, hi=2500,
          title="Booked orders: 150 of 5,000 shuffled gaps, with the real Retail-Plus lead marked")
print(f"Retail-Plus {len(plus)} orders at {kit.rupees(mean(plus))}, Retail-Core {len(core)} at {kit.rupees(mean(core))}; "
      f"lead {kit.rupees(real)}, share {share_booked:.3f}")
''', {1: ("c", "The question is about the two consumer tiers. a keeps Business, whose lakh-rupee orders would swamp any basket comparison; b keeps everyone; d names Business outright."),
      2: ("a", "Every amount in this file converts cleanly with int(), including the one stored as text, which is Monday's lesson. b leaves text in the list, so the average stops with a TypeError; c zeroes every order that was not delivered, which answers step 2's question in step 1 and keeps the cancelled orders in the count at zero; d measures the length of the text."),
      3: ("b", "A Retail-Plus lead at least as large as the real one is a shuffled gap at or above it. a counts every shuffled gap at or below the real lead, which is nearly every deal; c is a ratio with no count of worlds; d asks for a gap twice as large.")}),
    ("code", '''
kit.check("the comparison holds the 19 booked orders of the two tiers", len(tiers) == 19, f"{len(tiers)}")
kit.check("on booked orders Retail-Plus leads by Rs 1,326 an order", round(real) == 1326, kit.rupees(real))
kit.check("counting leads at least as large, the booked share is 0.002 with seed 2026", round(share_booked, 3) == 0.002,
          f"{share_booked:.3f}")
'''),
    ("md", '''
## Step 2. Does the lead survive on the money Kalpa kept, and which share goes in the line?

Used at work whenever a definition decides which orders count.
'''),
    ("todo", '''
# TODO 4. Which filter keeps only the money kept?
#   a) r["status"] != "cancelled"
#   b) r["status"] == "returned" or r["status"] == "delivered"
#   c) r["amount"] != ""
#   d) r["status"] == "delivered"
kept = [r for r in tiers if __TODO4__]
plus_k = [int(r["amount"]) for r in kept if r["segment"] == "Retail-Plus"]
core_k = [int(r["amount"]) for r in kept if r["segment"] == "Retail-Core"]
real_k = mean(plus_k) - mean(core_k)
gaps_k = shuffle_gaps(plus_k, core_k, 5000, seed=2026)
share_kept = sum(1 for g in gaps_k if g >= real_k) / len(gaps_k)
kit.columns(["booked", "money kept"], [("orders behind Retail-Plus", [len(plus), len(plus_k)]),
                                       ("orders behind Retail-Core", [len(core), len(core_k)])],
            width=560, title="The count behind each comparison")
kit.columns(["booked", "money kept"], [("share", [round(share_booked, 3), round(share_kept, 3)])],
            fmt=lambda v: f"{v:.3f}", width=560, title="How often chance makes the Retail-Plus lead")
# TODO 5. The head of Retail-Plus asked about the money kept. Which share goes in the line?
#   a) share_booked
#   b) share_kept
#   c) 1 - share_kept
#   d) min(share_booked, share_kept)
reported = __TODO5__
print(f"on the money kept, Retail-Plus has {len(plus_k)} orders and leads by {kit.rupees(real_k)}; "
      f"the line reports a share of {reported:.3f}, about {round(reported * 100)} times in 100")
''', {4: ("d", "Delivered orders are the money kept. a keeps returns; b says the same as a in more words; c keeps everything."),
      5: ("b", "The question is about the money kept, so the share is the one on the money kept, and with it the line says not yet. a is the booked share, computed on a definition nobody asked about; c is its complement, the share of deals with a smaller lead; d picks whichever share flatters the claim.")}),
    ("code", '''
kit.check("the money kept leaves Retail-Plus with only three orders", len(plus_k) == 3, f"{len(plus_k)}")
kit.check("counting leads at least as large, the share on the money kept is 0.15 with seed 2026",
          round(share_kept, 2) == 0.15, f"{share_kept:.3f}")
kit.check("the line reports the share for the money kept", round(reported, 2) == 0.15, f"{reported:.3f}")
'''),
    ("solution_md", '''
## So do Retail-Plus baskets beat Retail-Core's, or is the lead the wobble chance makes?

Not yet. The booked comparison looks decisive, a Rs 1,326 lead that chance makes 2 times in 1,000,
because five of Retail-Plus's eight booked orders were cancelled or returned, and they averaged about
Rs 3,800. On delivered orders, the money kept, Retail-Plus has three orders, the lead is Rs 671, and
chance makes it about 15 times in 100. The definition decided the verdict, and the count decided how
far to trust it.
'''),
    ("code", '''
kit.check_summary()
print("Post the five letters in order; then problem 4 is on paper.")
'''),
]

CASES = {
    "ex1": (EX1, "C2_W01_D04_ex1_escalated_case"),
    "ex2": (EX2, "C2_W01_D04_ex2_second_case"),
    "ex3": (EX3, "C2_W01_D04_ex3_practice_lab"),
}


def keys_of(spec):
    return {n: key for entry in spec if entry[0] == "todo" for n, (key, _) in entry[2].items()}


def twins(spec):
    """The TODO twin's cells and the solution's cells, from one spec."""
    todo, solution = [], []
    keys = keys_of(spec)
    for entry in spec:
        kind, text = entry[0], entry[1]
        if kind == "md":
            todo.append(md(text)); solution.append(md(text))
        elif kind == "todo_md":
            todo.append(md(text))
        elif kind == "solution_md":
            solution.append(md(text))
        elif kind == "code":
            todo.append(code(text)); solution.append(code(text))
        elif kind == "todo_code":
            todo.append(code(text))
        elif kind == "solution_code":
            solution.append(code(text))
        elif kind == "todo":
            todo.append(code(text))
            solution.append(code(fill(text, keys)))
            for n, (key, why) in entry[2].items():
                solution.append(md(f"**TODO {n} is {key}.** {why}"))
    return todo, solution


def script_of(spec, choice):
    """The solution's code as one plain script with the given choices, recording every check."""
    parts = []
    for i, entry in enumerate(spec):
        kind, text = entry[0], entry[1]
        if kind in ("code", "solution_code"):
            parts.append(text)
        elif kind == "todo":
            parts.append(fill(text, choice))
        if kind == "code" and i <= 2 and "import c2kit as kit" in text:
            parts.append('''
_RESULTS = []
def _record(label, condition, detail=""):
    _RESULTS.append((label, bool(condition)))
kit.check = _record
kit.check_summary = lambda: None
''')
    body = "\n\n".join(parts)
    return ("import sys, json\n"
            "try:\n" + "\n".join("    " + line for line in body.splitlines()) + "\n"
            "except Exception as e:\n"
            "    print('@@CRASH@@', type(e).__name__)\n"
            "    sys.exit(0)\n"
            "print('@@RESULTS@@' + json.dumps(_RESULTS))\n")


def run_script(src):
    with tempfile.NamedTemporaryFile("w", suffix=".py", dir=NOTEBOOKS, delete=False) as fh:
        fh.write(src)
        path = pathlib.Path(fh.name)
    try:
        r = subprocess.run([sys.executable, str(path)], cwd=NOTEBOOKS, capture_output=True, text=True, timeout=600)
    finally:
        path.unlink()
    out = r.stdout
    if "@@CRASH@@" in out:
        return "crash", out.split("@@CRASH@@")[1].strip()
    marker = out.rfind("@@RESULTS@@")
    if marker < 0:
        return "crash", (r.stderr or "no output")[-300:]
    return "ran", json.loads(out[marker + len("@@RESULTS@@"):].strip().splitlines()[0])


def verify(name):
    spec = CASES[name][0]
    keys = keys_of(spec)
    status, results = run_script(script_of(spec, keys))
    failing = [label for label, ok in results if not ok] if status == "ran" else results
    print(f"{name}: with every key, {status}; failing checks: {failing or 'none'}")
    problems = 0
    todo_opts = {n: opts for entry in spec if entry[0] == "todo" for n, opts in options_of(entry[1]).items()}
    for n in sorted(keys):
        for letter in sorted(todo_opts[n]):
            if letter == keys[n]:
                continue
            choice = dict(keys)
            choice[n] = letter
            status, results = run_script(script_of(spec, choice))
            if status == "crash":
                print(f"  TODO {n} option {letter}: crashes ({results})")
                continue
            caught = [label for label, ok in results if not ok]
            if caught:
                print(f"  TODO {n} option {letter}: caught by '{caught[0]}'")
            else:
                print(f"  TODO {n} option {letter}: NOT CAUGHT by any check")
                problems += 1
    return problems


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    wanted = args or list(CASES)
    if "--verify" in sys.argv:
        bad = sum(verify(n) for n in wanted)
        print("verify:", "every wrong option is caught" if not bad else f"{bad} wrong options slip through")
        sys.exit(1 if bad else 0)
    for n in wanted:
        spec, stem = CASES[n]
        todo, solution = twins(spec)
        build(NOTEBOOKS / f"{stem}_STUDENT.ipynb", todo, execute=False)
        nb = build(SOLUTIONS / f"{stem}_solution_STUDENT.ipynb", solution, timeout=300)
        print(f"built {stem}: TODO twin {len(todo)} cells, solution {len(nb.cells)} cells, key "
              f"{''.join(keys_of(spec)[k] for k in sorted(keys_of(spec)))}")

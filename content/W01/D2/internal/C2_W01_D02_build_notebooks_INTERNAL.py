"""Write and execute the six chapter notebooks of Week 1 Tuesday, each cold in its own folder.

    python3 content/W01/D2/internal/C2_W01_D02_build_notebooks_INTERNAL.py          # all six
    python3 content/W01/D2/internal/C2_W01_D02_build_notebooks_INTERNAL.py 3 4      # chapters 3 and 4

Each chapter notebook pairs with one `## SECTION n:` of the decks, carries the need, the options with
their sizing, the build in levels, the trap, the second route and Kavya's review, and carries forward
the tools the notebook before it built. The real-company lines come from COMPANY below, whose every
fact is recorded with its URL and check date in the provenance.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, md, code, empty, build  # noqa: E402

DAY = ROOT / "content" / "W01" / "D2"
NB = DAY / "notebooks"

LADDER = ["Is the drop real", "Which branch moved", "Which segment", "Mix or rate",
          "Marketing's hypothesis", "The memo and its evidence"]

# The real company per chapter. Each fact is checked on 30 Sep 2026; the provenance holds the URLs.
COMPANY = {
    1: """**Who else faces this.** Avenue Supermarts, which runs DMart, reports like-for-like growth only
on stores that have been open for at least 24 months at the end of the financial year, so a new store
never inflates the comparison; its like-for-like growth was 8.1 percent in FY26 (Avenue Supermarts,
investor presentation, May 2026, checked 30 Sep 2026). Target, in the United States, defines comparable
sales against a prior-year period "of equivalent length": its fiscal 2023 ran 53 weeks against 52, and
it reported that the extra week alone added $1,715 million of sales (Target, fourth quarter and full
year 2023 results, checked 30 Sep 2026). The National Retail Federation's 4-5-4 calendar exists for the
same reason: comparable months hold the same number of weeks and weekends (NRF, checked 30 Sep 2026).""",
    2: """**Who else faces this.** Blinkit, the quick-commerce app, reports its orders and its net average
order value, the average order after discounts, side by side, so its net order value can be read as the two branches of this tree: in the
fourth quarter of FY26 it reported 273.9 million orders at Rs 525 each, about Rs 14,386 crore
(Eternal, shareholders' letter, 28 April 2026, checked 30 Sep 2026). Walmart splits the growth of its
U.S. comparable sales the same way every quarter: in the quarter ended 31 July 2026, comparable sales
excluding fuel rose 2.6 percent, made of transactions up 1.5 percent and average ticket, the spend per transaction, up 1.1 percent
(Walmart earnings release, second quarter of fiscal 2027, checked 30 Sep 2026). The question each
answers is Meera's: did more visits move the number, or bigger baskets?""",
    3: """**Who else faces this.** Costco reports its membership renewal rate twice: for the United States
and Canada, and worldwide. At the end of its fiscal 2025 the first stood at 92.3 percent and the second
at 89.8 percent (Costco, fourth quarter fiscal 2025 results filed with the SEC, checked 30 Sep 2026).
One blended rate would hide where renewals are weaker, so the segments are reported beside the whole,
which is what the head of Retail-Plus needs from us.""",
    4: """**Who else faces this.** Swiggy, the food and grocery delivery app, reported the average order
value of Instamart, its quick-commerce store, up 14 percent in a single quarter to Rs 697 in the
quarter to September 2025. It did not call that a price rise: it put the rise down to non-grocery
categories and large packs taking a larger share of gross order value, the value of orders before
discounts, while the net average order value after discounts stood at Rs 485 (Swiggy, Q2 FY2026
shareholder letter, checked 30 Sep 2026). The average order grew because the mix of what people
bought moved, which is the reading Marketing's price claim skips for Kalpa's revenue per order.""",
    5: """**Who else faces this.** Every membership business runs Marketing's argument against the
frequency argument. Harvard Business Review summarised the studies behind it: depending on the study
and the industry, acquiring a new customer costs 5 to 25 times more than retaining an existing one,
and Bain's Frederick Reichheld found that a 5 percent rise in retention lifts profits by 25 to 95
percent (Amy Gallo, HBR, 29 October 2014, checked 30 Sep 2026). Those are estimates across
industries, never Kalpa's figures, so the reply asks Finance for Kalpa's own acquisition cost. Swiggy
shows why the two branches are reported apart: in the quarter to September 2025 its monthly
transacting users, the people who ordered at least once in a month, rose 34.0 percent in a year to 22.9 million while orders per user a month fell from
4.53 to 4.10 (Swiggy, Q2 FY2026 shareholder letter, checked 30 Sep 2026). A count and a frequency can move apart, which is why each is reported on its own, the reverse of Kalpa's quarter and the same lesson.""",
    6: """**Who else faces this.** Sonos rolled out a redesigned app in 2024. Its chief executive said the problems customers and partners met with the new app had
required the company to reduce its fiscal 2024 guidance, the revenue it had told investors to
expect, and its annual report set aside short-term
costs of up to $30 million to fix the app (Sonos, third quarter fiscal 2024 results and fiscal 2024
annual report, checked 30 Sep 2026). A loyal customer base, an app whose rollout went wrong, and a company that put it into its guidance: the head of Retail-Plus is asking whether his
tier is the same story.""",
}


def head(n, title, promise):
    return md(f"""
# {n}. {title}

**Week 1, Tuesday. Chapter {n} of 6.** {promise}
""")


def mapcell(n, steps):
    lit = n - 1
    return code(f"""
kit.side_by_side(
    kit.ladder({LADDER!r}, lit={lit}, show=False),
    kit.vflow({steps!r}, show=False),
)""")


# --------------------------------------------------------------------------------------------- 1
def chapter1():
    cells = [
        head(1, "Is the drop real",
             "By the end of this notebook you can say whether Kalpa's revenue fell between the two "
             "quarters, by how much, and on which windows, before anyone explains why."),
        md("""
> **The client asks.** "So revenue is customers, times how often they buy, times basket, times
> price. Now: which of those moved? Q2 was Rs 1.9 crore, Q1 was 2.1. Are we losing customers, or
> are the ones we have buying less? Marketing says more customers. Prove it or disprove it."
>
> Meera Raghavan, CEO, Kalpa Retail

**What Monday established, and what this adds.** Monday drew the revenue tree on thirty orders from
one window and ended on Anand's warning that one large order can move an average. Today's export
holds both quarters, 1 April to 30 September, 200 orders. This chapter builds the first tool of the
day, a dictionary that adds revenue up by a key, and uses it to confirm the drop on windows that
match. Every later chapter grows that tool.
"""),
        md("""
**Setup.** The first lines walk up from this folder until they find the programme's helper, `c2kit`,
and import it as `kit`. The export loads as a list of dictionaries, one per booked order, and `date`
arrives so that a window can be measured in days.
"""),
        code(SETUP + """from datetime import date, timedelta   # calendar days, so a window can be measured

ORDERS = kit.load_records("C2_W01_D02_orders_STUDENT.py")
print(len(ORDERS), "orders loaded")
print("fields:", ", ".join(ORDERS[0]))"""),
        mapcell(1, ["the need: which number is the fall?", "the options, sized",
                    "the build: closed quarters", "the trap: 11 weeks against 13",
                    "rates with their window", "a second route: by month"]),
        md("""
## The need

Meera is about to answer Marketing's request for Rs 12 crore to acquire new customers, and the
request rests on one slide: revenue fell by about a quarter. The metric at stake is the change in
booked revenue, every order placed before any cancellation or return, between two quarters, and the
decision riding on it is whether the fall is a crisis
that needs money now. A wrong number here costs in two directions: overstate the fall and Kalpa
spends crores in a hurry on a lever nobody has checked; understate it and a real leak runs another
quarter. Kalpa's financial year opens in April, so Q1 is April to June and Q2 is July to
September, and both closed on 30 September.

The retail and e-commerce story behind these words is in the domain dossier,
`content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`, which tells why a store chain
compares periods like with like before it reads any change.
"""),
        md(COMPANY[1]),
        md("""
## The options

Four ways a team could put a number on "revenue fell", each answering a slightly different question.

| Option | What it compares | What it controls for | What it needs |
|---|---|---|---|
| A. Closed quarters as totals | 1 Apr to 30 Jun against 1 Jul to 30 Sep | The length of the window, once both quarters have closed | Both quarters closed |
| B. The same weeks of both quarters | The first 11 weeks of each | Length and position in the quarter, while a quarter is still open | A cut date |
| C. A rate per week or per day | Revenue divided by the weeks or days each window covers | Length, whatever the windows | The window stated beside the rate |
| D. The same quarter last year | Q2 this year against Q2 last year | Length and the season | Last year's export, which this file does not hold |

The cell below sizes each one on this file: how many rows it reads, what answer it gives, how far
that answer sits from option A, and what it leaves out.
"""),
        code("""
def revenue_between(start, end):
    total, rows = 0, 0
    for order in ORDERS:
        d = date.fromisoformat(order["order_date"])
        if start <= d <= end:
            total += order["amount"]
            rows += 1
    return total, rows

a1, n1 = revenue_between(date(2026, 4, 1), date(2026, 6, 30))
a2, n2 = revenue_between(date(2026, 7, 1), date(2026, 9, 30))
option_a = (a2 - a1) / a1 * 100
b1, m1 = revenue_between(date(2026, 4, 1), date(2026, 6, 16))
b2, m2 = revenue_between(date(2026, 7, 1), date(2026, 9, 15))
option_b = (b2 - b1) / b1 * 100
option_c = (a2 / 92 - a1 / 91) / (a1 / 91) * 100

left_out = len(ORDERS) - (m1 + m2)
rows = [("A. closed quarters", n1 + n2, f"{option_a:.1f}%", "+0.0 points", "nothing, once both quarters have closed"),
        ("B. same 11 weeks", m1 + m2, f"{option_b:.1f}%", f"{option_b - option_a:+.1f} points",
         f"the last two weeks of each quarter, {left_out} orders"),
        ("C. per day, closed", n1 + n2, f"{option_c:.1f}%", f"{option_c - option_a:+.1f} points",
         "nothing; it spreads each total over 91 and 92 days"),
        ("D. same quarter last year", 0, "cannot run", "no last-year rows", "everything, until last year's export arrives")]
kit.table(["Option", "Rows read", "Answer", "Gap from A", "What it leaves out"], rows,
          caption="Four ways to size the fall, on the export as it stands")
kit.bars([("A. closed quarters", round(-option_a, 1)), ("B. same 11 weeks", round(-option_b, 1)),
          ("C. per day, closed", round(-option_c, 1))],
         fmt=lambda v: f"down {v:.1f}%", lit=[0], title="Three honest options, three answers on one file")
kit.check("options A and C read all 200 rows", n1 + n2 == len(ORDERS), f"{n1 + n2}")
kit.check("option B reads fewer rows, because it drops two weeks of each quarter", m1 + m2 < len(ORDERS), f"{m1 + m2}")
"""),
        md("""
**The best-fit call.** Option A, closed quarters as totals, because both quarters closed on
30 September and each holds thirteen weeks, so the totals already compare like with like and every
reader can rebuild the number from the rows. What separates the options is the question each answers
and what each leaves out, and on a closed pair of quarters A leaves out nothing. **The fact that would
change the call:** if Q2 were still open, option B, the same weeks of both quarters, would take
over; if Meera asked whether the monsoon explains the fall, only option D answers, and it needs last
year's export.

## 1. Revenue fell 11.0 percent between the two closed quarters

A dictionary keyed by quarter collects revenue and orders in one pass. A key that is new starts at
zero, and every order adds to its own quarter's total. This accumulator is the tool the whole day
grows.

**Predict before you run.** On the two closed quarters, how far did revenue move? a) it fell about
26 percent; b) it fell about 11 percent; c) it fell about 5 percent; d) it rose.
"""),
        code("""
revenue = {}     # quarter -> rupees booked
orders = {}      # quarter -> number of orders
for order in ORDERS:
    q = order["quarter"]
    if q not in revenue:
        revenue[q] = 0
        orders[q] = 0
    revenue[q] += order["amount"]
    orders[q] += 1

change = (revenue["Q2"] - revenue["Q1"]) / revenue["Q1"] * 100
kit.table(["Quarter", "Window", "Orders", "Revenue"],
          [("Q1", "1 Apr to 30 Jun, 13 weeks", orders["Q1"], kit.rupees(revenue["Q1"])),
           ("Q2", "1 Jul to 30 Sep, 13 weeks", orders["Q2"], kit.rupees(revenue["Q2"]))],
          caption=f"Booked orders by quarter: revenue moved {change:.1f} percent")
kit.columns(["Q1, 13 weeks", "Q2, 13 weeks"], [("revenue booked", [revenue["Q1"], revenue["Q2"]])],
            fmt=kit.rupees, title="Two closed quarters of equal length")
"""),
        md("""
**What happened.** The answer is b. Revenue fell from Rs 2,10,00,000 to Rs 1,87,00,000, which is
Rs 23,00,000 less and 11.0 percent down, on two windows of thirteen weeks. That is the number Meera's
question starts from, and it is less than half the fall on Marketing's slide.
"""),
        code("""
kit.check("every order sits in one of the two quarters", orders["Q1"] + orders["Q2"] == len(ORDERS),
          f'{orders["Q1"]} + {orders["Q2"]} = {len(ORDERS)}')
kit.check("the closed-quarter change rounds to minus 11.0 percent", round(change, 1) == -11.0, f"{change:.2f}")
kit.check("the accumulator agrees with option A in the sizing cell", round(change, 6) == round(option_a, 6))
"""),
        md("""
## 2. The trap: Marketing's 25.9 percent compares 11 weeks with 13

Marketing's deck reads the Q2 figure from the dashboard tile, which somebody screenshotted on
15 September, and sets it against the whole of Q1.

**Predict before you run.** Marketing's slide says revenue fell by about a quarter. What do you
check first? a) the segment mix of each quarter; b) the median order in each quarter; c) the first
and last date inside each window; d) whether discounts changed.

**The plausible wrong answer.** A hurried analyst takes the tile's number as Q2 and divides.
"""),
        code("""
TILE_CUT = "2026-09-15"     # the day the dashboard tile was read

tile_revenue = 0
tile_orders = 0
for order in ORDERS:
    if order["quarter"] == "Q2" and order["order_date"] <= TILE_CUT:
        tile_revenue += order["amount"]
        tile_orders += 1

wrong = (tile_revenue - revenue["Q1"]) / revenue["Q1"] * 100
kit.stats([(kit.rupees(tile_revenue), "Q2 on the tile", f"{tile_orders} orders to 15 September"),
           (kit.rupees(revenue["Q1"]), "Q1, whole quarter", f'{orders["Q1"]} orders'),
           (f"{wrong:.1f}%", "Marketing's change", "the tile against the whole of Q1")])
"""),
        md("""
**Why it is wrong.** The answer to the prediction is c. The tile stopped on 15 September, so its
window holds eleven weeks of trading, and it is set against thirteen. Two weeks of Q2 that nobody had
counted yet show up as lost revenue. Read as a crisis, a 25.9 percent fall pushes Meera to release
the Rs 12 crore acquisition budget in a hurry, on a gap that is mostly the calendar.

**The check** prints, for each window, where it starts and ends, the first and last order inside it,
and the weeks it covers.
"""),
        code("""
windows = {
    "Q1, whole quarter": (date(2026, 4, 1), date(2026, 6, 30), "Q1"),
    "Q2 on the tile":    (date(2026, 7, 1), date(2026, 9, 15), "Q2"),
    "Q2, whole quarter": (date(2026, 7, 1), date(2026, 9, 30), "Q2"),
}
first, last, days = {}, {}, {}
rows = []
for name in windows:
    start, end, q = windows[name]
    for order in ORDERS:
        d = date.fromisoformat(order["order_date"])
        if order["quarter"] == q and start <= d <= end:
            first[name] = min(first.get(name, d), d)
            last[name] = max(last.get(name, d), d)
    days[name] = (end - start).days + 1
    rows.append((name, f"{start:%d %b} to {end:%d %b}", f"{first[name]:%d %b}", f"{last[name]:%d %b}",
                 days[name], days[name] // 7))
kit.table(["Window", "Covers", "First order", "Last order", "Days", "Whole weeks"], rows,
          caption="The check: where each side of the comparison starts and stops")

start = {"Q1": date(2026, 4, 1), "Q2": date(2026, 7, 1)}
weekly = {"Q1": [0] * 13, "Q2": [0] * 13}      # revenue by week of the quarter
for order in ORDERS:
    q = order["quarter"]
    week = (date.fromisoformat(order["order_date"]) - start[q]).days // 7
    weekly[q][min(week, 12)] += order["amount"]
cumulative = {"Q1": [], "Q2": []}
for q in cumulative:
    running = 0
    for amount in weekly[q]:
        running += amount
        cumulative[q].append(running)
tile_line = cumulative["Q2"][:11] + [None, None]
kit.line([str(w) for w in range(1, 14)],
         [("Q1, all 13 weeks", cumulative["Q1"], "plain"),
          ("Q2 as the tile saw it, cut after week 11", tile_line, "bad")],
         fmt=lambda v: f"Rs {v / 1e7:.2f} cr",
         title="Cumulative revenue by week of the quarter: the tile stops at week 11")
kit.check("Q1 covers 13 whole weeks and the tile 11", (days["Q1, whole quarter"] // 7, days["Q2 on the tile"] // 7) == (13, 11))
kit.check("Marketing's figure rounds to minus 25.9 percent", round(wrong, 1) == -25.9, f"{wrong:.2f}")
"""),
        md("""
**The fix.** Compare the closed quarters, thirteen weeks each: minus 11.0 percent, Rs 23,00,000. The
bridge below shows where Marketing's extra fall went: Q2's last two weeks, which the tile had not
reached, carried Rs 31,40,050 of revenue.
"""),
        code("""
late = revenue["Q2"] - tile_revenue
kit.bridge(("Q1, 13 weeks", revenue["Q1"]),
           [("Q2's first 11 weeks fall short", tile_revenue - revenue["Q1"]),
            ("Q2's last 2 weeks, after the tile", late)],
           end_label="Q2, 13 weeks", lit=[1],
           title="Marketing's gap, reconciled: two weeks the tile had not counted")
kit.check("the bridge lands on the closed Q2 total", revenue["Q1"] + (tile_revenue - revenue["Q1"]) + late == revenue["Q2"],
          kit.rupees(revenue["Q2"]))
kit.check("the uncounted weeks hold 16 orders and Rs 31,40,050", (orders["Q2"] - tile_orders, late) == (16, 3140050),
          f'{orders["Q2"] - tile_orders} orders, {kit.rupees(late)}')
"""),
        md("""
**What changed.** The fall Meera is asked to act on shrank from Rs 54,40,050 to Rs 23,00,000, and
from 25.9 percent to 11.0 percent. Sixteen orders worth Rs 31,40,050 were never missing; they had not
happened yet when the tile was read.

## 3. A rate carries its numerator, its denominator and its window

Option C in action. A rate per week puts windows of different length on one scale, provided the
rate says what was counted, what it was divided by, and over which dates.

**Predict before you run.** Revenue per week, Q1's thirteen weeks against the tile's eleven: how far
apart are they? a) minus 25.9 percent, the same as the totals; b) minus 12.4 percent; c) no change;
d) plus 5 percent.
"""),
        code("""
per_week_q1 = revenue["Q1"] / 13
per_week_tile = tile_revenue / 11
per_week_change = (per_week_tile - per_week_q1) / per_week_q1 * 100
kit.equation(["revenue per week", "=", "revenue booked\\nthe numerator", "/",
              "weeks covered\\nthe denominator", "in", "one window\\nits first and last date"],
             title="A rate is three things, and a rate missing any of them is a rumour")
kit.table(["Rate", "Numerator", "Denominator", "Window", "Value"],
          [("Q1 revenue per week", kit.rupees(revenue["Q1"]), "13 weeks", "1 Apr to 30 Jun", kit.rupees(round(per_week_q1))),
           ("Q2 revenue per week, tile", kit.rupees(tile_revenue), "11 weeks", "1 Jul to 15 Sep", kit.rupees(round(per_week_tile)))],
          caption=f"Per week on the cut window: {per_week_change:.1f}%")
kit.check("revenue per week falls 12.4 percent on the cut window", round(per_week_change, 1) == -12.4, f"{per_week_change:.2f}")
kit.check("per day on the closed quarters, the fall is 11.9 percent", round(option_c, 1) == -11.9, f"{option_c:.2f}")
"""),
        md("""
**What happened.** The answer is b. Per week, the tile's eleven weeks sit 12.4 percent below Q1, at
Rs 14,14,541 a week against Rs 16,15,385. On the closed quarters per day the fall is 11.9 percent,
because Q2 has 92 days and Q1 has 91. Each figure is honest because it says what it divided and over
which dates, and none of them is 25.9 percent.

## 4. The same eleven weeks of both quarters give a different answer again

Option B in action: suppose Q2 were still open on 15 September. The like-with-like comparison is
then the first eleven weeks of each quarter, 1 April to 16 June against 1 July to 15 September.

**Predict before you run.** Q1's first eleven weeks against Q2's first eleven weeks: a) minus
12.4 percent, the same as the per-week rate; b) minus 11.0 percent, the same as the closed quarters;
c) a fall larger than both; d) a rise.
"""),
        code("""
kit.line([str(w) for w in range(1, 14)],
         [("Q1", weekly["Q1"], "plain"), ("Q2", weekly["Q2"], "lit")],
         fmt=lambda v: f"Rs {v / 1e5:.0f} lakh",
         title="Revenue in each week of the quarter: a few large orders make the weeks lumpy")
kit.table(["Window", "Orders", "Revenue"],
          [("Q1, 1 Apr to 16 Jun", m1, kit.rupees(b1)), ("Q2, 1 Jul to 15 Sep", m2, kit.rupees(b2))],
          caption=f"The same eleven weeks of each quarter: {option_b:.1f}%")
kit.check("the same-weeks comparison is minus 17.0 percent", round(option_b, 1) == -17.0, f"{option_b:.2f}")
kit.check("the weekly figures add back to each quarter's total",
          sum(weekly["Q1"]) == revenue["Q1"] and sum(weekly["Q2"]) == revenue["Q2"])
"""),
        md("""
**What happened.** The answer is c. The same eleven weeks give minus 17.0 percent. That differs from
the per-week minus 12.4 because Kalpa's weekly revenue is lumpy: a week with no large business order
books ten or fifteen thousand rupees, and a week with three of them books lakhs, so which weeks a cut
happens to include moves the answer. Once a quarter has closed, compare closed quarters; a
quarter-to-date comparison uses the same weeks of both quarters and says so.

## A second route: the same fall, added up by month

The accumulator keyed by quarter trusted the `quarter` field in each record. A second route ignores
that field, keys the accumulator by the month in `order_date`, and adds the months back into
quarters. If the two routes disagree, one of them is reading the file wrongly.
"""),
        code("""
by_month = {}
for order in ORDERS:
    month = order["order_date"][:7]          # "2026-04"
    by_month[month] = by_month.get(month, 0) + order["amount"]

q1_months = by_month["2026-04"] + by_month["2026-05"] + by_month["2026-06"]
q2_months = by_month["2026-07"] + by_month["2026-08"] + by_month["2026-09"]
route_two = (q2_months - q1_months) / q1_months * 100
kit.columns(["Apr", "May", "Jun", "Jul", "Aug", "Sep"], [("revenue by month", [by_month[m] for m in sorted(by_month)])],
            fmt=lambda v: f"Rs {v / 1e5:.0f} L", lit=[3, 4, 5], title="The same revenue, by month: Q2's months in bold")
kit.check("the months add to the same Q1 and Q2 totals", (q1_months, q2_months) == (revenue["Q1"], revenue["Q2"]),
          f"{kit.rupees(q1_months)} and {kit.rupees(q2_months)}")
kit.check("both routes give minus 11.0 percent", round(route_two, 6) == round(change, 6), f"{route_two:.2f}")
"""),
        md("""
**When to switch.** Keep the quarter key for the headline; switch to the month key when the question
moves inside the quarter, as it will in chapter 6, where the head of Retail-Plus dates a cause to a
week in August.

> **Kavya's review.** "Marketing's arithmetic was correct on a quarter that had not finished. Say
> both windows out loud with their first and last dates before you say a percentage, and say which
> option you picked and what would make you pick another. If the windows do not match, nothing you
> say after that counts."

### In the interview

**[S] Sales dropped 15 percent last month; how would you investigate?** "In a fixed order. First I
confirm the drop is real: the same window on both sides, closed periods or the same days of each,
the same definition of a sale, and an export that is complete. Then I decompose revenue along a
tree, customers times orders per customer times revenue per order, and see which branch moved. Then
I split the moving branch by segment, and inside a segment I check whether a mix shift or a real
change in rate is behind it. Only then do I name a cause, as a hypothesis, with the evidence that
would settle it, and timing is the first test: a cause cannot come after its effect." The
interviewer is listening for the order, and above all for the first step, which most candidates skip.

**[F] What has to match before a quarter-on-quarter comparison is fair?** "The window length, and
whether both periods have closed; if not, the same weeks of each, or a rate per week with its window
stated. The definition of what is counted, booked or delivered. The population, the same segments
and customers in scope. The denominator behind any rate. And the export itself, pulled when the later
period was complete. Today a dashboard tile read on 15 September and set against a full quarter
turned an 11.0 percent fall into 25.9." The interviewer is listening for window, definition,
population and denominator named without prompting.

**The design question. Q2 is still open; which comparison do you send, and what would make you
switch?** "The same weeks of both quarters, with the cut date in the sentence, because it controls
for length and for where in the quarter the weeks sit, and a rate per week beside it. On Kalpa's
file those two disagree, minus 17.0 against minus 12.4, because a few business orders make weeks
lumpy, so I say both and wait for the close. I switch to closed quarters the day the quarter closes,
and to the same quarter last year if the question becomes the season." The interviewer is listening
for a choice, its reason, and the fact that would change it.

### Depth: calendars that do not line up

Weeks and days are only the first level of matching. A quarter can hold one more weekend than
another, or a festival that falls in a different month from one year to the next, and a business
that trades mostly on weekends then shows a change that is only the calendar. Try it here: count the
Saturdays and Sundays in each quarter with `date` and `timedelta`, and decide whether Kalpa's gap
could be a weekend effect.

References for the chapter:

- Brit Institute, data analyst case study questions, including "Sales dropped last month. How would you investigate?": https://britinstitute.uk/blog/data-analyst-case-study-interview-questions (verified 29 Sep 2026)
- Exponent, data analyst interview questions: https://www.tryexponent.com/blog/top-data-analyst-interview-questions (verified 29 Sep 2026)
"""),
        code("""
kit.check_summary()
print("Next: chapter 2, which branch of the tree carries the Rs 23,00,000.")"""),
    ]
    build(NB / "C2_W01_D02_01_is_the_drop_real_STUDENT.ipynb", cells)


# --------------------------------------------------------------------------------------------- 2
CH2_SETUP = SETUP + """ORDERS = kit.load_records("C2_W01_D02_orders_STUDENT.py")
by_quarter = {"Q1": [], "Q2": []}           # chapter 1's accumulator, now holding the orders themselves
for order in ORDERS:
    by_quarter[order["quarter"]].append(order)
print(len(by_quarter["Q1"]), "orders in Q1 and", len(by_quarter["Q2"]), "in Q2")"""


def chapter2():
    cells = [
        head(2, "Which branch moved",
             "By the end of this notebook you can split the quarter's fall along the revenue tree, "
             "say in rupees how much each branch carries, and answer Marketing's claim about "
             "customers with a count."),
        md("""
> **The client asks.** "Are we losing customers, or are the ones we have buying less? Marketing
> says more customers. Prove it or disprove it."
>
> Meera Raghavan, CEO, Kalpa Retail

**What chapter 1 established, and what this adds.** The drop is real on matched windows: two closed
quarters of thirteen weeks, Rs 2,10,00,000 to Rs 1,87,00,000, a fall of Rs 23,00,000 and 11.0 percent.
Chapter 1's tool added rupees up by quarter; this chapter grows it to count customers and orders per
customer, puts rupees on each branch of the tree, and opens the price branch, where Marketing's
monsoon discount plan lives.

> **Kavya's review of chapter 1.** "Good: you said both windows before you said a percentage. Now
> stop describing the fall and start taking it apart."
"""),
        code(CH2_SETUP),
        mapcell(2, ["the need: which lever moved?", "the options: four ways to split Rs 23 lakh",
                    "customers, counted", "the leaves, multiplied back", "rupees per branch",
                    "the trap: a blank discount read as zero", "a second route: the symmetric split"]),
        md("""
## The need

Meera's tree has four branches: customers, how often they buy, basket, and price. Each branch has an
owner and a price tag. Customers belong to Marketing and cost acquisition spend; how often they buy
belongs to the tier and product owners and costs retention work on people already won; basket
belongs to merchandising, the team that picks the range and the pack sizes; price and discounts
belong to Finance with Marketing, who trade margin for volume, giving up some profit on each order to
sell more of them. The metric at stake is the rupees each branch carries of the Rs 23,00,000 fall, and the
decision riding on it is which owner gets the problem, and whether Marketing's Rs 12 crore is aimed
at a branch that moved. A wrong split sends crores to the wrong owner for a quarter.
"""),
        md(COMPANY[2]),
        md("""
## The options

Four ways to split the fall across the branches.

| Option | How it splits | What it gives Meera |
|---|---|---|
| A. Each leaf's percentage change | Customers, orders per customer and revenue per order, Q1 against Q2 | Direction, and no rupees, since percentages multiply and do not add |
| B. A bridge in the tree's order | Change one leaf at a time, customers first, holding the rest at Q1 | Rupees per branch that add exactly to the fall, for the order chosen |
| C. A symmetric split | Share the fall in proportion to each leaf's logarithmic change | Rupees that do not depend on any order |
| D. Customer by customer | Each of the 69 customers' Q1 and Q2 orders side by side | Who moved, at 69 rows of reading before any total |

The cell below sizes B, C and a reversed bridge on this file, since the order of the steps is where
the choice bites, and says for each option whether its rupees add to the fall and what Meera would
have to read.
"""),
        code("""
import math

def leaves(rows):
    seen = {}
    revenue = 0
    for order in rows:
        seen[order["customer_id"]] = True
        revenue += order["amount"]
    return len(seen), len(rows) / len(seen), revenue / len(rows), revenue

c1, f1, v1, r1 = leaves(by_quarter["Q1"])
c2, f2, v2, r2 = leaves(by_quarter["Q2"])
b_freq = c2 * (f2 - f1) * v1                       # B: frequency moved before order value
rev_freq = c2 * (f2 - f1) * v2                     # B reversed: order value first, frequency second
log_mean = (r2 - r1) / math.log(r2 / r1)
c_freq = log_mean * math.log(f2 / f1)              # C: symmetric
kit.table(["Option", "Frequency's rupees", "Adds to the fall?", "Depends on order?", "What Meera reads"],
          [("A. percentages only", "none: percentages do not add", "no", "no", "three percentages"),
           ("B. bridge, tree order", kit.rupees(round(b_freq)), "yes, exactly", "yes", "three rupee steps"),
           ("B. bridge, order reversed", kit.rupees(round(rev_freq)), "yes, exactly", "yes", "three rupee steps"),
           ("C. symmetric split", kit.rupees(round(c_freq)), "yes, exactly", "no", "three rupee figures and a logarithm"),
           ("D. customer by customer", "a total only after 69 rows", "after summing", "no", "69 rows")],
          caption="Sizing the split on the Rs 23,00,000 fall")
kit.bars([("B, tree order", round(-b_freq)), ("C, symmetric", round(-c_freq)), ("B, reversed", round(-rev_freq))],
         fmt=kit.rupees, lit=[0], title="What frequency is charged depends on the order of the steps")
kit.check("the three rupee figures sit within Rs 10 lakh of each other", abs(rev_freq - b_freq) < 1000000,
          kit.rupees(round(abs(rev_freq - b_freq))))
"""),
        md("""
**The best-fit call.** Option B, the bridge in the tree's order, because its rupees add exactly to
the fall, a CEO can follow it one step at a time, and in every order frequency carries the fall, so
the choice of order changes the size and never the decision. Write the order beside the bridge.
**The fact that would change the call:** if Finance will rebuild the split every month and two
branches keep moving together, option C removes the argument about order; if Meera asks which
customers slowed, option D is the one that names them, and chapter 5 comes back to it.

## 1. Customers held at 69 in both quarters

Marketing's claim is about the first branch, so it is counted first. A dictionary per quarter maps
each customer id to the orders that customer placed. `.get(cid, 0)` reads the count so far and
supplies 0 when the id has not appeared yet, and that default is right for a reason worth writing
down: a customer not seen yet in the quarter has placed no orders in it so far.

**Predict before you run.** How did the number of distinct customers move from Q1 to Q2? a) it fell;
b) it held; c) it rose, as Marketing says; d) it cannot be told without the segments.
"""),
        code("""
orders_by_customer = {"Q1": {}, "Q2": {}}      # quarter -> {customer_id: orders placed}
for q in by_quarter:
    for order in by_quarter[q]:
        cid = order["customer_id"]
        # default: a customer not seen yet in this quarter has placed zero orders in it so far
        orders_by_customer[q][cid] = orders_by_customer[q].get(cid, 0) + 1

customers = {q: len(orders_by_customer[q]) for q in by_quarter}
orders = {q: len(by_quarter[q]) for q in by_quarter}
kit.columns(["Q1", "Q2"], [("distinct customers", [customers["Q1"], customers["Q2"]]),
                           ("orders", [orders["Q1"], orders["Q2"]])],
            title="Customers held while orders fell")
kit.check("customers held at 69 in both quarters", customers["Q1"] == customers["Q2"] == 69,
          f'{customers["Q1"]} and {customers["Q2"]}')
kit.check("the per-customer counts add back to each quarter's orders",
          all(sum(orders_by_customer[q].values()) == orders[q] for q in by_quarter))
"""),
        md("""
**What happened.** The answer is b. Kalpa had 69 distinct customers in each quarter, so the count
does not support "more customers". Orders fell from 114 to 86 on the same count, which already points
at the second branch. Whether the 69 are the same people is a separate question, and chapter 5 asks it.

## 2. Orders per customer carries the fall, and revenue per order rose

The tree multiplies three leaves: customers, orders per customer, and revenue per order. Price and
basket fold into revenue per order today, because the file has no order lines.

**Predict before you run.** Which leaf moved against Kalpa? a) customers; b) orders per customer;
c) revenue per order; d) all three fell a little.
"""),
        code("""
revenue = {"Q1": r1, "Q2": r2}
opc = {"Q1": f1, "Q2": f2}          # orders per customer
rpo = {"Q1": v1, "Q2": v2}          # revenue per order
kit.driver_tree({"label": "revenue", "note": f'Q1 {kit.rupees(r1)}\\nQ2 {kit.rupees(r2)}', "kind": "lit", "children": [
    {"label": "customers", "note": f'Q1 {customers["Q1"]}\\nQ2 {customers["Q2"]}', "kind": "known"},
    {"label": "orders per customer", "note": f'Q1 {f1:.2f}\\nQ2 {f2:.2f}', "kind": "bad"},
    {"label": "revenue per order", "note": f'Q1 {kit.rupees(round(v1))}\\nQ2 {kit.rupees(round(v2))}', "kind": "good"}]},
    title="The tree with both quarters: the fall sits on orders per customer", width_per=190)
ratio_c, ratio_f, ratio_v = c2 / c1, f2 / f1, v2 / v1
kit.equation([f"{ratio_c:.3f}\\ncustomers", "x", f"{ratio_f:.3f}\\norders per customer", "x",
              f"{ratio_v:.3f}\\nrevenue per order", "=", f"{ratio_c * ratio_f * ratio_v:.3f}\\nQ2 over Q1 revenue"],
             title="The leaves multiply back to the change in revenue")
kit.check("the three ratios multiply to Q2 over Q1 revenue", abs(ratio_c * ratio_f * ratio_v - r2 / r1) < 1e-9,
          f"{ratio_c * ratio_f * ratio_v:.3f}")
kit.check("orders per customer fell 24.6 percent and revenue per order rose 18.0",
          (round((ratio_f - 1) * 100, 1), round((ratio_v - 1) * 100, 1)) == (-24.6, 18.0))
"""),
        md("""
**What happened.** The answer is b. Orders per customer fell from 1.65 to 1.25, down 24.6 percent,
while revenue per order rose 18.0 percent, from Rs 1,84,211 to Rs 2,17,442. The same count of
customers placed fewer orders, and the orders they placed were larger on average. Adding the two
percentages would say minus 6.6 percent; multiplying says 0.754 times 1.180, which is 0.890, the
11.0 percent fall. Chapter 4 asks why the orders got larger.

## 3. In rupees, frequency costs Rs 51,57,895 and bigger orders give back Rs 28,57,895

Option B, built. The bridge changes one leaf at a time in the order of the tree: first customers,
holding the other two at Q1; then orders per customer; then revenue per order.

**Predict before you run.** How many rupees does the fall in orders per customer take away?
a) Rs 23,00,000; b) Rs 51,57,895; c) Rs 28,57,895; d) nothing, because customers held.
"""),
        code("""
move_customers = (c2 - c1) * f1 * v1
move_frequency = c2 * (f2 - f1) * v1
move_order_value = c2 * f2 * (v2 - v1)
kit.bridge(("Q1 revenue", r1),
           [("customers", round(move_customers)), ("orders per customer", round(move_frequency)),
            ("revenue per order", round(move_order_value))],
           end_label="Q2 revenue", lit=[1], title="The Rs 23,00,000 fall along the tree, one leaf at a time")
kit.check("the bridge lands on Q2 revenue", abs(r1 + move_customers + move_frequency + move_order_value - r2) < 1,
          kit.rupees(r2))
kit.check("the customers move is zero", move_customers == 0)
"""),
        md("""
**What happened.** The answer is b. Holding customers and order value at Q1, the fall in orders per
customer takes away Rs 51,57,895, and larger orders give back Rs 28,57,895. The customer branch
contributes nothing, so Marketing's case for acquisition has no rupees behind it on this file.

## 4. The trap: the price branch, read the hurried way

Meera's fourth branch is price, and Marketing's monsoon plan starts from one number on it: the share
of orders that carry a discount. If half the orders go without one, they want the discount extended
to the other half. The export carries a `discount` field in rupees, so the first attempt counts the
orders where it is above zero.
"""),
        code("""
with kit.expect_error() as err:
    with_discount = 0
    for order in ORDERS:
        if order["discount"] > 0:
            with_discount += 1
kit.check("the loop stopped on a missing key", err.name == "KeyError", f"{err.name}: {err.message}")
"""),
        md("""
That is a runtime error, and it takes two minutes: some records carry no `discount` key at all, and
indexing a dictionary with a key it lacks raises `KeyError`. A `try` and `except KeyError` around the
line would also get past it. The question that matters is what a missing discount means.

**Predict before you run.** A hurried analyst reads every missing discount as zero. What share of
Q2's 86 orders will carry a discount? a) about a quarter; b) about half; c) about seven in ten;
d) every order.

**The plausible wrong answer.** `.get("discount", 0)` makes the error go away and gives a number.
"""),
        code("""
with_disc = {"Q1": 0, "Q2": 0}
for q in by_quarter:
    for order in by_quarter[q]:
        if order.get("discount", 0) > 0:          # the hurried default: missing becomes zero
            with_disc[q] += 1
as_zero_share = {q: with_disc[q] / orders[q] * 100 for q in by_quarter}
kit.stats([(f'{as_zero_share["Q1"]:.1f}%', "orders with a discount, Q1", "missing read as zero"),
           (f'{as_zero_share["Q2"]:.1f}%', "orders with a discount, Q2", "missing read as zero"),
           (f'{orders["Q2"] - with_disc["Q2"]} of {orders["Q2"]}', "Q2 orders read as no discount", "so, extend it to them?")])
"""),
        md("""
**Why it is wrong.** The answer to the prediction is b, and it is the wrong number. The 43 Q2 orders
the hurried reading files under "no discount" are two different things: orders where someone
recorded Rs 0 off, and orders where nobody wrote the discount down at all. The second kind is
unknown, and a default of zero counts every one of them as an order that went without. The decision
it misleads is expensive: Marketing extends the monsoon discount to "the other half" of orders,
spending margin on orders that may already carry one.

The mechanism on three **invented** orders, one with Rs 100 off, one with Rs 0 off, and one with no
field at all:
"""),
        code("""
invented = [{"order_id": "INVENTED-1", "discount": 100},
            {"order_id": "INVENTED-2", "discount": 0},
            {"order_id": "INVENTED-3"}]                      # invented records, no discount field on the third
as_zero_with = sum(1 for o in invented if o.get("discount", 0) > 0)
recorded = [o for o in invented if "discount" in o]
recorded_with = sum(1 for o in recorded if o["discount"] > 0)
kit.bars([("read as zero, 1 of 3", round(as_zero_with / 3 * 100)), ("recorded only, 1 of 2", round(recorded_with / len(recorded) * 100))],
         fmt=lambda v: f"{v}%", title="Invented orders: a blank read as zero shrinks the share")
kit.check("on the invented orders, read-as-zero gives 33 percent and recorded-only 50 percent",
          (round(as_zero_with / 3 * 100), round(recorded_with / len(recorded) * 100)) == (33, 50))
"""),
        md("""
**Your turn.** Count the Kalpa records that carry no `discount` field, in each quarter. Type these
lines into the empty cell below and run them, then say in one sentence how many of the orders the
hurried reading called "no discount" were never recorded:

```python
missing = {"Q1": 0, "Q2": 0}
for order in ORDERS:
    if "discount" not in order:
        missing[order["quarter"]] += 1
print(missing)
```
"""),
        empty(),
        md("""
**The check.** Split the orders the hurried reading called "no discount" into the ones that record
Rs 0 and the ones with no field at all, and find the largest discount anyone recorded.
"""),
        code("""
kinds = {q: {"above": 0, "zero": 0, "blank": 0} for q in by_quarter}
largest = 0
for q in by_quarter:
    for order in by_quarter[q]:
        if "discount" not in order:
            kinds[q]["blank"] += 1
        elif order["discount"] > 0:
            kinds[q]["above"] += 1
            largest = max(largest, order["discount"])
        else:
            kinds[q]["zero"] += 1
kit.columns(["Q1", "Q2"], [("discount above Rs 0", [kinds["Q1"]["above"], kinds["Q2"]["above"]]),
                           ("Rs 0 recorded", [kinds["Q1"]["zero"], kinds["Q2"]["zero"]]),
                           ("no field", [kinds["Q1"]["blank"], kinds["Q2"]["blank"]])],
            fmt=lambda v: f"{v}", title="What the hurried 'no discount' was made of")
kit.check("the three kinds add up to every order in each quarter", all(sum(kinds[q].values()) == orders[q] for q in kinds))
kit.check("Q2's 'no discount' orders are recorded zeros plus blanks",
          orders["Q2"] - with_disc["Q2"] == kinds["Q2"]["zero"] + kinds["Q2"]["blank"],
          f'{orders["Q2"] - with_disc["Q2"]} = {kinds["Q2"]["zero"]} + {kinds["Q2"]["blank"]}')
kit.check("the largest recorded discount is Rs 150", largest == 150, kit.rupees(largest))
"""),
        md("""
**The fix.** Treat a blank as unknown. Write the rule where the next person will read it, report
the share over the orders that record the field, give the range the blanks allow, and bound the
branch in rupees: the largest recorded discount is Rs 150, so even if every one of Q2's 86 orders had
carried Rs 150 off, the branch could hold at most Rs 12,900 against a fall of Rs 23,00,000.
"""),
        code("""
DISCOUNT_RULE = "absent means not recorded; reported separately; never counted as zero"
recorded_n = {q: kinds[q]["above"] + kinds[q]["zero"] for q in kinds}
share_recorded = {q: kinds[q]["above"] / recorded_n[q] * 100 for q in kinds}
share_top = {q: (kinds[q]["above"] + kinds[q]["blank"]) / orders[q] * 100 for q in kinds}
kit.table(["Share of orders with a discount", "Q1", "Q2"],
          [("hurried: blanks read as zero", f'{as_zero_share["Q1"]:.1f}%', f'{as_zero_share["Q2"]:.1f}%'),
           ("over the orders that record the field", f'{share_recorded["Q1"]:.1f}% of {recorded_n["Q1"]}', f'{share_recorded["Q2"]:.1f}% of {recorded_n["Q2"]}'),
           ("range over all orders, blanks unknown", f'{as_zero_share["Q1"]:.1f}% to {share_top["Q1"]:.1f}%', f'{as_zero_share["Q2"]:.1f}% to {share_top["Q2"]:.1f}%')],
          caption="The hurried share is the floor of the range, reported as the fact")
bound = orders["Q2"] * largest
kit.bars([("the Q2 revenue fall", r1 - r2), ("discount branch, at most", bound)],
         fmt=kit.rupees, lit=[1], title="Even at its largest, the discount branch is a sliver of the fall")
kit.check("where the field is recorded, 71.7 percent of Q2's orders carry a discount", round(share_recorded["Q2"], 1) == 71.7)
kit.check("the discount branch is under one percent of the fall", bound / (r1 - r2) < 0.01, f"{kit.rupees(bound)}")
print("The rule, written down:", DISCOUNT_RULE)
"""),
        md("""
**What changed.** "Half of Q2's orders had no discount, extend it to them" became "where the field
is recorded, 71.7 percent of Q2's orders carried a discount; 17 of 86 are known to have had none, and
26 are unknown". The extension loses its premise until someone finds which system left those records
blank, and the whole branch is worth at most Rs 12,900, so discounts leave the list of causes.

## A second route: the symmetric split, which chooses no order

The bridge charged the part where two leaves moved together to whichever leaf moved second. The
second route splits the same fall a different way: each leaf takes a share in proportion to its
logarithmic change, so no order is chosen at all. It is an independent method, so if the bridge had
put the fall on the wrong branch, this split would say so. The rupees per branch will differ by that
joint part; the branch that carries the fall must not.
"""),
        code("""
weight = (r2 - r1) / math.log(r2 / r1)          # the log-mean of the two quarters' revenue
symmetric = {"customers": weight * math.log(c2 / c1),
             "orders per customer": weight * math.log(f2 / f1),
             "revenue per order": weight * math.log(v2 / v1)}
bridge_moves = {"customers": move_customers, "orders per customer": move_frequency,
                "revenue per order": move_order_value}
kit.columns(list(symmetric), [("bridge, tree order", [round(bridge_moves[k]) for k in symmetric]),
                              ("symmetric split", [round(symmetric[k]) for k in symmetric])],
            fmt=kit.rupees, width=620, title="The fall split two ways: the same branch carries it")
kit.check("the symmetric split adds to the same fall", round(sum(symmetric.values())) == round(r2 - r1),
          kit.rupees(round(sum(symmetric.values()))))
kit.check("both routes charge the largest fall to orders per customer",
          min(symmetric, key=symmetric.get) == min(bridge_moves, key=bridge_moves.get) == "orders per customer")
"""),
        md("""
**When to switch.** Keep the bridge for Meera, with its order written beside it, because a CEO can
follow one leaf at a time. Switch to the symmetric split when two branches keep moving together and
someone else rebuilds the split every month, since then nobody argues about order. Here the two
differ by Rs 4,30,585 on frequency, the joint part, and agree on the branch.

> **Kavya's review.** "Meera asked two questions and you answered both with a count: customers held
> at 69, and the ones we have bought less often. Put the bridge in front of her with its order
> written beside it, and do not call the rise in order value good news until you know where it came
> from."

### In the interview

**[F] Revenue fell 11 percent; how do you split the change between customers, frequency and order
value?** "I write revenue as customers times orders per customer times revenue per order and compute
each leaf in both periods. The ratios multiply back to the revenue ratio, which proves the leaves are
consistent. To put rupees on each, I change one leaf at a time in the tree's order, holding the
others at the earlier period, so the moves add exactly to the total. On Kalpa's quarters that gave
customers nothing, frequency minus Rs 51,57,895 and order value plus Rs 28,57,895. I say that the
split depends on the order, and I keep the order fixed across reports." The interviewer is listening
for the multiplicative check and for rupees in place of percentages that do not add.

**[S] Why is a rate without a denominator meaningless?** "Because a rate is a count divided by
something over a window, and changing either of the other two changes the number. Orders per
customer of 1.25 over 69 customers on booked orders becomes 1.14 over 50 customers with a delivered order. When someone quotes a rate, I ask what was counted, what it was divided by and over
which dates." The interviewer is listening for all three parts.

**[S] A field is missing on some records; do you fill it with zero?** "Only if zero is what missing
means, and someone has written down why. Usually missing means not recorded, which is unknown.
Filling with zero makes a total into a floor, and if the blank share changes between periods it
manufactures a trend. So I count the blanks, report them separately, compute on the recorded rows
and bound what the unknowns could do." The interviewer is listening for "unknown", the count of
blanks, and a bound.

**The design question. Which way do you split a revenue change for a CEO, and when would you
change it?** "A bridge in the tree's order, with the order written beside it, because it adds
exactly and a CEO can follow it. On Kalpa's quarters the order moves frequency's charge between
Rs 51.6 lakh and Rs 60.9 lakh and never changes which branch is guilty. If the split is rebuilt
monthly by someone else, I switch to the symmetric split so nobody argues about order." The
interviewer is listening for a reason and the fact that would switch it.

### Depth: the order of the bridge, with three branches moving

With three branches moving at once, a sequential bridge has six possible orders, and the symmetric
split still gives one answer, because the logarithms of the three ratios add exactly to the logarithm
of the revenue ratio (B. W. Ang, "The LMDI approach to decomposition analysis: a practical guide",
Energy Policy, 2005, checked through Crossref 29 Sep 2026). Try it: in the escalated case this
afternoon customers move too; run the second route's split there and count how many of the six
bridge orders put the most rupees on the same branch.

References for the chapter:

- Python docs, built-in types, `dict.get`: https://docs.python.org/3/library/stdtypes.html (verified 29 Sep 2026)
- Corey Schafer, "Python Tutorial: Using Try/Except Blocks for Error Handling": https://www.youtube.com/watch?v=NIWwJbo-9_8 (verified 29 Sep 2026)
"""),
        code("""
kit.check_summary()
print("Next: chapter 3, which segment carries the fall in orders per customer.")"""),
    ]
    build(NB / "C2_W01_D02_02_which_branch_STUDENT.ipynb", cells)


# --------------------------------------------------------------------------------------------- 3
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
            "orders_per_customer": orders / customers,
            "revenue_per_order": revenue / orders}


def describe(amounts):
    """A group's typical value and spread: median, min, max and range (chapter 3)."""
    ordered = sorted(amounts)
    n = len(ordered)
    if n % 2 == 1:
        median = ordered[n // 2]
    else:
        median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2
    return {"median": median, "min": ordered[0], "max": ordered[-1], "range": ordered[-1] - ordered[0]}
'''

GROUPS = '''ORDERS = kit.load_records("C2_W01_D02_orders_STUDENT.py")
SEGMENTS = ["Retail-Core", "Retail-Plus", "Business", "Student"]
groups = {"Q1": {}, "Q2": {}}       # quarter -> segment -> list of orders
by_quarter = {"Q1": [], "Q2": []}
for order in ORDERS:
    q, seg = order["quarter"], order["segment"]
    groups[q].setdefault(seg, []).append(order)
    by_quarter[q].append(order)
'''


def chapter3():
    cells = [
        head(3, "Which segment",
             "By the end of this notebook you can write two functions that return the tree and the "
             "shape of any group of orders, run them on any segment and quarter, and roll a rate up to "
             "the company figure without averaging the averages."),
        md("""
> **The client asks.** "One of my members says the app's reorder button has been broken for six
> weeks. Is my tier the one slipping?"
>
> The head of Retail-Plus, Kalpa's paid membership tier

**What chapter 2 established, and what this adds.** Customers held at 69, orders per customer fell
from 1.65 to 1.25 and took Rs 51,57,895 with it, revenue per order rose 18.0 percent, and the discount
branch is worth at most Rs 12,900. Chapter 2's loop counted customers and orders for one group at a
time. This chapter needs the same numbers for four segments in two quarters, eight groups, and the
loop becomes a function: one tool, written once, called for any group.

> **Kavya's review of chapter 2.** "You have written the same accumulating loop three times since
> this morning. The fourth time, write it once, give it a name, and make it hand back its answer."
"""),
        code(SETUP + GROUPS + 'print(len(SEGMENTS), "segments,", len(ORDERS), "orders grouped by quarter and segment")'),
        mapcell(3, ["the need: is one tier slipping?", "the options: copy, function or group by key",
                    "tree_for returns the leaves", "describe: typical value and spread",
                    "the trap: averages averaged", "a second route: one pass by key", "your turn: all four"]),
        md("""
## The need

Kalpa sells to four kinds of customer. Retail-Core buys a few thousand rupees at a time; Retail-Plus
pays a membership fee for benefits and is meant to order more often; Business buys in bulk, lakhs per
order; Student is a small discounted segment. The head of Retail-Plus owns the paid tier's renewals,
so his question is the metric of his job: orders per member, this quarter against last. The decision
riding on it is whether his team gets the problem, and the fund to fix it, or whether it sits
elsewhere. A wrong number costs either a tier nobody protects, or a quarter spent fixing a tier that
was fine.
"""),
        md(COMPANY[3]),
        md("""
## The options

The same five numbers, revenue, orders, customers, orders per customer and revenue per order, are
needed for eight groups. Three ways a team could produce them.

| Option | How | The cost that matters |
|---|---|---|
| A. Copy the loop per group | Paste chapter 2's loop eight times, one per segment and quarter | Eight places to edit when the definition changes, and eight chances to edit seven |
| B. Write a function | `tree_for(rows)` takes any list of orders and returns the five numbers | One place to edit; each call reads its own group |
| C. Group by a key in one pass | One loop over all 200 orders adds into `totals[(quarter, segment)]` | One pass over the rows; the code is shaped for these eight groups only |

The cell below sizes each: lines of code, places to edit when Anand changes the definition to
delivered orders, and rows read.
"""),
        code(TOOLS.strip() + '''

import time
copy_lines = 8 * 9                                # the chapter 2 loop is nine lines, pasted eight times
function_lines = 13 + 8                           # tree_for once, then one call per group
key_lines = 14
reads = {"A": 0, "B": 0, "C": 0}
t0 = time.perf_counter()
for q in ("Q1", "Q2"):
    for seg in SEGMENTS:
        reads["A"] += len(ORDERS)                 # each pasted loop filters the whole export
        tree_for(groups[q][seg]); reads["B"] += len(groups[q][seg])
secs_b = time.perf_counter() - t0
reads["C"] = len(ORDERS)
kit.table(["Option", "Lines of code", "Places to edit for a new definition", "Rows read", "Reuse later today"],
          [("A. copy per group", copy_lines, 8, reads["A"], "paste again for channel and month"),
           ("B. a function", function_lines, 1, reads["B"], "any list: a channel, a month, delivered only"),
           ("C. group by key", key_lines, 1, reads["C"], "these eight groups; a new key means a new loop")],
          caption=f"Sizing three ways to get eight trees; the eight function calls ran in {secs_b * 1000:.2f} ms")
kit.bars([("A. copy per group", copy_lines), ("B. a function", function_lines), ("C. group by key", key_lines)],
         fmt=lambda v: f"{v} lines", lit=[1], title="Lines to write, before anyone edits the definition")
kit.check("a function reads each order once across the eight groups", reads["B"] == len(ORDERS), f'{reads["B"]}')
kit.check("copying reads the export eight times over", reads["A"] == 8 * len(ORDERS), f'{reads["A"]}')
'''),
        md("""
**The best-fit call.** Option B, a function, because the same five numbers will be asked for a
channel, a month and delivered orders before the day ends, and a function answers every one of them
with one line; on 200 rows the speed of each option is a matter of milliseconds and decides nothing.
**The fact that would change the call:** if the export grew to millions of rows and every group were
needed at once, option C, one pass by key, would win on rows read, which is what `groupby` in pandas
does in Week 2.

## 1. A function returns the tree for any list of orders

`tree_for(rows)` returns rather than prints, so the caller can put the answer in a table, a chart or
a check.

**Predict before you run.** What will `tree_for(by_quarter["Q1"])["orders_per_customer"]` give,
rounded? a) 1.65; b) 1.25; c) `None`; d) 1.94.
"""),
        code('''
q1 = tree_for(by_quarter["Q1"])
q2 = tree_for(by_quarter["Q2"])
kit.driver_tree({"label": "revenue", "note": f'Q1 {kit.rupees(q1["revenue"])}\\nQ2 {kit.rupees(q2["revenue"])}', "kind": "lit", "children": [
    {"label": "customers", "note": f'Q1 {q1["customers"]}\\nQ2 {q2["customers"]}', "kind": "known"},
    {"label": "orders per customer", "note": f'Q1 {q1["orders_per_customer"]:.2f}\\nQ2 {q2["orders_per_customer"]:.2f}', "kind": "bad"},
    {"label": "revenue per order", "note": f'Q1 {kit.rupees(round(q1["revenue_per_order"]))}\\nQ2 {kit.rupees(round(q2["revenue_per_order"]))}'}]},
    title="Chapter 2's tree, now drawn from what tree_for returned", width_per=190)
kit.check("tree_for reproduces chapter 2's orders per customer",
          (round(q1["orders_per_customer"], 2), round(q2["orders_per_customer"], 2)) == (1.65, 1.25))
kit.check("tree_for returns all five leaves", len(q1) == 5 and "revenue_per_order" in q1, ", ".join(q1))
'''),
        md("""
**What happened.** The answer is a. The function reproduces chapter 2: 1.65 in Q1 and 1.25 in Q2, on
69 customers each. Option c is what a function hands back when it prints its answer and returns
nothing; chapter 5 meets a colleague's function that does exactly that.

## 2. Retail-Core: frequency slipped a little, and the typical order fell

A segment gets a typical value and a spread, and `describe(amounts)` returns both: the median, the
smallest and largest order, and the range between them.

**Predict before you run.** Retail-Core's orders per customer, Q1 against Q2: a) it fell by about a
quarter, like the company; b) it rose; c) it fell by about 5 percent; d) it did not move.
"""),
        code('''
core = {q: tree_for(groups[q]["Retail-Core"]) for q in ("Q1", "Q2")}
core_amounts = {q: [o["amount"] for o in groups[q]["Retail-Core"]] for q in ("Q1", "Q2")}
core_shape = {q: describe(core_amounts[q]) for q in core_amounts}
core_change = (core["Q2"]["orders_per_customer"] / core["Q1"]["orders_per_customer"] - 1) * 100
kit.table(["Retail-Core", "Orders", "Customers", "Orders per customer", "Median", "Min", "Max", "Range"],
          [(q, core[q]["orders"], core[q]["customers"], f'{core[q]["orders_per_customer"]:.2f}',
            kit.rupees(round(core_shape[q]["median"])), kit.rupees(core_shape[q]["min"]),
            kit.rupees(core_shape[q]["max"]), kit.rupees(core_shape[q]["range"])) for q in ("Q1", "Q2")],
          caption=f"Retail-Core orders per customer moved {core_change:.1f} percent")
kit.strip(core_amounts["Q2"], lo=0, hi=3500,
          title=f'Retail-Core, Q2 orders on one axis; median {kit.rupees(core_shape["Q2"]["median"])}, against {kit.rupees(core_shape["Q1"]["median"])} in Q1')
kit.check("Retail-Core customers held at 34", core["Q1"]["customers"] == core["Q2"]["customers"] == 34)
kit.check("Retail-Core orders per customer fell 5.3 percent", round(core_change, 1) == -5.3, f"{core_change:.2f}")
'''),
        md("""
**What happened.** The answer is c. The same 34 Retail-Core customers placed 36 orders against 38, so
orders per customer moved from 1.12 to 1.06, down 5.3 percent, and the typical order fell from
Rs 2,325 to Rs 2,080. Retail-Core slipped a little, far short of the company's 24.6 percent.

## 3. Business: the median barely moves while the range grows by nearly three quarters

**Predict before you run.** Business revenue fell from Rs 2,07,71,180 to Rs 1,85,41,460. What does
`describe` show about the typical Business order? a) the median fell by about a tenth, like revenue;
b) the median barely moved and the largest order grew a lot; c) every order got smaller; d) the
median rose sharply.
"""),
        code('''
biz = {q: tree_for(groups[q]["Business"]) for q in ("Q1", "Q2")}
biz_amounts = {q: [o["amount"] for o in groups[q]["Business"]] for q in ("Q1", "Q2")}
biz_shape = {q: describe(biz_amounts[q]) for q in biz_amounts}
biz_change = (biz["Q2"]["orders_per_customer"] / biz["Q1"]["orders_per_customer"] - 1) * 100
kit.columns(["median", "smallest", "largest", "range"],
            [(q, [biz_shape[q]["median"], biz_shape[q]["min"], biz_shape[q]["max"], biz_shape[q]["range"]]) for q in ("Q1", "Q2")],
            fmt=lambda v: f"{v / 1e5:.1f}", lit=[2],
            title="Business orders in lakh of rupees: the middle holds, the top end moves")
kit.check("Business customers held at 11", biz["Q1"]["customers"] == biz["Q2"]["customers"] == 11)
kit.check("Business orders per customer fell 15.0 percent", round(biz_change, 1) == -15.0, f"{biz_change:.2f}")
kit.check("the Business range grew more than 70 percent while the median moved under 4 percent",
          biz_shape["Q2"]["range"] / biz_shape["Q1"]["range"] > 1.7
          and abs(biz_shape["Q2"]["median"] / biz_shape["Q1"]["median"] - 1) < 0.04)
'''),
        md("""
**What happened.** The answer is b. The median Business order moved from Rs 9,83,780 to Rs 9,52,000,
while the largest grew from Rs 17,84,000 to Rs 29,45,460 and the range rose about 73 percent. One large
order sets the range. The eleven Business customers placed 17 orders against 20, down 15.0 percent
per customer, on three orders. Neither segment shown falls 24.6 percent, so before guessing where the
rest sits, roll the segments back up.

## 4. The trap: rolling the segments up by averaging their averages

With `tree_for` in hand, the company figure looks one line away: run it on all four segments and
average their orders per customer.

**Predict before you run.** Averaged over the four segments, how far does orders per customer fall?
a) 24.6 percent, the same as chapter 2; b) much less than chapter 2; c) more than chapter 2; d) it
rises.

**The plausible wrong answer.** A hurried analyst averages the four segment rates in each quarter.
"""),
        code('''
averaged = {}
for q in ("Q1", "Q2"):
    total = 0
    for seg in SEGMENTS:
        total += tree_for(groups[q][seg])["orders_per_customer"]
    averaged[q] = total / len(SEGMENTS)
averaged_change = (averaged["Q2"] / averaged["Q1"] - 1) * 100
kit.stats([(f'{averaged["Q1"]:.2f}', "Q1, average of 4 segments", "each segment counted once"),
           (f'{averaged["Q2"]:.2f}', "Q2, average of 4 segments", "each segment counted once"),
           (f"{averaged_change:.1f}%", "the hurried change", "so frequency is not the branch?")])
'''),
        md("""
**Why it is wrong.** The answer to the prediction is b, and it is the wrong conclusion. Averaging
the averages gives every segment one vote, so a segment of 2 customers counts as much as one of 34.
"Frequency fell only 6.0 percent, so it is not the branch, and Marketing may be right" would send
Meera back to the acquisition budget on a number that describes no customer. **The check:** a roll-up
of the segments must reproduce the company figure, 1.65 and 1.25, and this one does not.

The mechanism on **invented** numbers: 30 customers who order 1.1 times each, and 2 who order 3.5
times each.
"""),
        code('''
small_group = {"customers": 2, "orders_per_customer": 3.5}     # invented, not Kalpa's
large_group = {"customers": 30, "orders_per_customer": 1.1}    # invented, not Kalpa's
avg_of_avgs = (small_group["orders_per_customer"] + large_group["orders_per_customer"]) / 2
orders_all = sum(g["customers"] * g["orders_per_customer"] for g in (small_group, large_group))
weighted_inv = orders_all / (small_group["customers"] + large_group["customers"])
kit.bars([("average of the averages", round(avg_of_avgs, 2)), ("orders over customers", round(weighted_inv, 2))],
         fmt=lambda v: f"{v:.2f}", lit=[1], title="Invented groups: 2 customers outvote 30 when averages are averaged")
kit.check("the averaged roll-up misses chapter 2's Q1 figure", round(averaged["Q1"], 2) != round(q1["orders_per_customer"], 2),
          f'{averaged["Q1"]:.2f} against {q1["orders_per_customer"]:.2f}')
kit.check("the hurried change is minus 6.0 percent", round(averaged_change, 1) == -6.0, f"{averaged_change:.2f}")
'''),
        md("""
**The fix.** Weight by customers: add the orders across segments and divide by the customers across
segments. Count the groups in and out as you do it: four segments go in, and their customers must add
back to 69.
"""),
        code('''
weighted, groups_used, customers_used = {}, {}, {}
for q in ("Q1", "Q2"):
    all_orders = all_customers = 0
    groups_used[q] = 0
    for seg in SEGMENTS:
        t = tree_for(groups[q][seg])
        all_orders += t["orders"]
        all_customers += t["customers"]
        groups_used[q] += 1
    weighted[q] = all_orders / all_customers
    customers_used[q] = all_customers
weighted_change = (weighted["Q2"] / weighted["Q1"] - 1) * 100
kit.columns(["Q1", "Q2"], [("average of the averages", [round(averaged["Q1"], 2), round(averaged["Q2"], 2)]),
                           ("weighted by customers", [round(weighted["Q1"], 2), round(weighted["Q2"], 2)])],
            fmt=lambda v: f"{v:.2f}", width=520, title="Rolled up with its weights, the rate falls 24.6 percent again")
kit.check("the weighted roll-up reproduces chapter 2", abs(weighted["Q1"] - q1["orders_per_customer"]) < 1e-12
          and abs(weighted["Q2"] - q2["orders_per_customer"]) < 1e-12)
kit.check("four groups in, four out, and their customers add back to 69",
          groups_used["Q1"] == groups_used["Q2"] == 4 and customers_used["Q1"] == customers_used["Q2"] == 69)
'''),
        md("""
**What changed.** "Frequency fell 6.0 percent, so Marketing may be right" became "orders per customer
fell from 1.65 to 1.25, 24.6 percent, across the same count of 69 customers", which keeps frequency
as the branch and keeps the acquisition budget shut. Retail-Core and Business carry part of it, and
the weighted roll-up says the rest sits in the segments not yet opened.

## A second route: one pass, grouped by key

Option C, built as the check on option B. One loop over the 200 orders adds each order into
`totals[(quarter, segment)]`; if every one of the eight groups gives the same five numbers as
`tree_for`, the function is right. The comparison runs inside a check, so it prints agreement and no
segment's numbers.
"""),
        code('''
totals = {}
for order in ORDERS:
    key = (order["quarter"], order["segment"])
    t = totals.setdefault(key, {"revenue": 0, "orders": 0, "ids": set()})
    t["revenue"] += order["amount"]
    t["orders"] += 1
    t["ids"].add(order["customer_id"])

agree = 0
for (q, seg), t in totals.items():
    via_function = tree_for(groups[q][seg])
    if (t["revenue"], t["orders"], len(t["ids"])) == (via_function["revenue"], via_function["orders"], via_function["customers"]):
        agree += 1
kit.flow(["200 orders\\none pass", "key: (quarter, segment)", "8 groups\\nrevenue, orders, ids", "compare with\\ntree_for"],
         lit=1, title="The second route: one pass by key, then a comparison group by group")
kit.check("both routes give the same numbers for all eight groups", agree == len(totals) == 8, f"{agree} of {len(totals)}")
'''),
        md("""
**When to switch.** Keep the function while groups are asked for one at a time; switch to the pass
by key when every group is needed at once on a large file, which is Week 2's `groupby`.

**Your turn.** Run the tree for all four segments in both quarters. Type these lines into the empty
cell below and run them:

```python
rows, opc_q1, opc_q2 = [], [], []
for seg in SEGMENTS:
    t1, t2 = tree_for(groups["Q1"][seg]), tree_for(groups["Q2"][seg])
    rows.append((seg, t1["customers"], t2["customers"], t1["orders"], t2["orders"],
                 f'{t1["orders_per_customer"]:.2f}', f'{t2["orders_per_customer"]:.2f}'))
    opc_q1.append(round(t1["orders_per_customer"], 2))
    opc_q2.append(round(t2["orders_per_customer"], 2))
kit.table(["Segment", "Customers Q1", "Customers Q2", "Orders Q1", "Orders Q2", "Per customer Q1", "Per customer Q2"], rows)
kit.columns(SEGMENTS, [("Q1", opc_q1), ("Q2", opc_q2)], fmt=lambda v: f"{v:.2f}", title="Orders per customer by segment")
```

Then write one sentence for the head of Retail-Plus that answers his question with a number and its
denominator.
"""),
        empty(),
        md("""
> **Kavya's review.** "Two functions, eight groups, no copied loops. Retail-Core slipped 5.3 percent
> and Business 15.0, and neither is 24.6. The segment that carries the rest is on your screen now,
> in your own cell. Say it with its denominator before anyone draws a conclusion from it."

### In the interview

**[F] You have orders per customer for four segments; why can't you average them for the company
figure?** "Because each segment's rate has its own denominator, and averaging the rates gives every
segment the same weight whatever its size. The company figure is total orders over total customers,
which is the segment rates weighted by their customers. On Kalpa's quarters the unweighted average
said frequency fell 6.0 percent and the weighted figure says 24.6. The test I run on any roll-up is
that it reproduces the company total." The interviewer is listening for denominators, weights and
the reproduce-the-total test.

**The design question. The same metrics are needed for every segment and quarter; do you copy the
code, write a function or group by a key?** "A function, when the groups will be asked for one at a
time and the definition may change, since there is one place to edit and it answers any subset: a
channel, a month, delivered orders. Copying eight times means eight edits and one forgotten. I would
group by a key in one pass when the file is large and every group is needed at once; that is what
`groupby` does." The interviewer is listening for the cost that decides it: edits and reuse on a
small file, rows read on a large one.

### Depth: what a range can and cannot say

A range is set by two orders, the smallest and the largest, so one order can stretch it, as Business showed with a rise of about 73 percent; a median is set by the middle of the list, so it barely moves. Between the two, the middle
half of the sorted values says how wide the ordinary orders sit. Try it on Business: sort each
quarter's amounts, drop the lowest and highest quarter of the list, and take the range of what is
left. Whether differences of this size are real is Thursday's question.

References for the chapter:

- Corey Schafer, "Python Tutorial for Beginners 8: Functions": https://www.youtube.com/watch?v=9Os0o3wzS_I (verified 29 Sep 2026)
- Python docs, "4. More Control Flow Tools", defining functions and return: https://docs.python.org/3/tutorial/controlflow.html (verified 29 Sep 2026)
- Khan Academy, mean, median and mode review: https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review (verified 29 Sep 2026)
"""),
        code("""
kit.check_summary()
print("Next: chapter 4, whether revenue per order rose because of mix or because of rate.")"""),
    ]
    build(NB / "C2_W01_D02_03_which_segment_STUDENT.ipynb", cells)


# --------------------------------------------------------------------------------------------- 4
def chapter4():
    cells = [
        head(4, "Mix or rate",
             "By the end of this notebook you can say how much of the rise in revenue per order came "
             "from the mix of orders and how much from customers paying more inside their segment."),
        md("""
> **The client asks.** "Revenue per order is up 18 percent. Our customers are happy to pay more, so
> the premium range is working. Put a price rise into the plan."
>
> The marketing lead, Kalpa Retail, reading chapter 2's tree

**What chapter 3 established, and what this adds.** Your own cell at the end of chapter 3 ran all
four segments. Retail-Plus, the paid tier, is the segment where orders per customer fell furthest:
the same 22 members placed 26 orders in Q2 against 51 in Q1. Retail-Core slipped 5.3 percent,
Business 15.0 percent on three orders, and Student rose. This chapter reuses `tree_for` on every
segment and adds the one question the tree cannot answer alone: why the average order got bigger.

> **Kavya's review of chapter 3.** "You rolled the segments up with their weights and got 1.65 and
> 1.25 back. Now the same weights answer Marketing's price question."
"""),
        code(SETUP + GROUPS + TOOLS + '''
q1 = {seg: tree_for(groups["Q1"][seg]) for seg in SEGMENTS}
q2 = {seg: tree_for(groups["Q2"][seg]) for seg in SEGMENTS}
all1, all2 = tree_for(by_quarter["Q1"]), tree_for(by_quarter["Q2"])
print("revenue per order:", kit.rupees(round(all1["revenue_per_order"])), "to", kit.rupees(round(all2["revenue_per_order"])))'''),
        mapcell(4, ["the need: are customers paying more?", "the options, sized",
                    "orders lost, by segment", "each segment's own revenue per order",
                    "the trap: 18 percent read as a price rise", "the split: mix and rate",
                    "a second route: two groups on an envelope"]),
        md("""
## The need

Revenue per order rose from Rs 1,84,211 to Rs 2,17,442. Marketing reads that as customers paying
more, and wants a price rise in the growth plan. The metric at stake is revenue per order, a blend
across segments whose orders differ several hundredfold: a Business order runs to lakhs and a Retail-Plus
order to about three thousand rupees. The decision riding on it is a price rise across the range. A
wrong reading costs volume: raise prices on customers who never paid more, and the fall in orders
per customer, the branch that actually moved, gets worse.
"""),
        md(COMPANY[4]),
        md("""
## The options

| Option | How | What it can say |
|---|---|---|
| A. Read the blended change | Q2 revenue per order against Q1, all orders | The size of the rise, and nothing about why |
| B. Each segment's own revenue per order | `tree_for` per segment, Q1 against Q2 | Whether any segment's customers paid more, one segment at a time |
| C. Split the rise into mix and rate | Price Q2's order mix at Q1's segment rates; the rest is rate | Rupees of the rise from mix and from rate, adding to the whole |
| D. Each segment's median order | `describe` per segment | The typical order, which one lakh-sized order cannot move |

The cell below sizes each on this file: how much of the Rs 33,231 rise each can put rupees on,
whether one lakh-sized order can move it, and what it leaves open.
"""),
        code('''
rise = all2["revenue_per_order"] - all1["revenue_per_order"]
share1 = {seg: q1[seg]["orders"] / all1["orders"] for seg in SEGMENTS}
share2 = {seg: q2[seg]["orders"] / all2["orders"] for seg in SEGMENTS}
at_q2_mix = sum(share2[seg] * q1[seg]["revenue_per_order"] for seg in SEGMENTS)
mix = at_q2_mix - all1["revenue_per_order"]
rate = all2["revenue_per_order"] - at_q2_mix
kit.table(["Option", "Rupees of the rise it explains", "Can one lakh-sized order move it?", "What it leaves open"],
          [("A. blended change", "none: it is the rise", "yes", "why"),
           ("B. per segment", "none: a direction per segment", "yes, inside Business", "how the segments add up"),
           ("C. mix and rate", f"all {kit.rupees(round(rise))}, split", "the rate part, yes", "which prices moved, if any"),
           ("D. medians per segment", "none: the typical order", "no", "rupees")],
          caption="Sizing four readings of one rise")
kit.bars([("A. blended change", 0), ("B. per segment", 0), ("C. mix and rate", round(rise)), ("D. medians", 0)],
         fmt=kit.rupees, lit=[2], title="Rupees of the rise each option attributes to a cause")
kit.check("option C's two parts add back to the whole rise", abs(mix + rate - rise) < 1e-6, kit.rupees(round(rise)))
'''),
        md("""
**The best-fit call.** Option C, the split, built on option B's per-segment rates, because it is the
only reading that puts rupees on "customers paid more" and on "the mix changed" and makes them add to
the rise. **The fact that would change the call:** if the segments' orders were similar in size, mix
would barely move the blend and option B alone would do; if Marketing wanted to know which products'
prices moved, only order lines, which this file does not carry, would answer.

## 1. Twenty-five of the twenty-eight lost orders were Retail-Plus

**Predict before you run.** Of the 28 orders lost between the quarters, how many were Retail-Plus
orders? a) about 7, a quarter; b) about 14, half; c) 25; d) all 28.
"""),
        code('''
order_moves = {seg: q2[seg]["orders"] - q1[seg]["orders"] for seg in SEGMENTS}
kit.bridge(("Q1 orders", all1["orders"]), [(seg, order_moves[seg]) for seg in SEGMENTS],
           end_label="Q2 orders", lit=[1], fmt=lambda v: f"{v:,.0f}",
           title="Orders, 114 to 86, by segment: Retail-Plus is 25 of the 28")
kit.check("the orders bridge lands on 86", all1["orders"] + sum(order_moves.values()) == all2["orders"])
kit.check("Retail-Plus is 25 of the 28 lost orders", order_moves["Retail-Plus"] == -25, f'{order_moves["Retail-Plus"]}')
'''),
        md("""
**What happened.** The answer is c. Retail-Plus lost 25 orders, Business 3 and Retail-Core 2, while
Student gained 2. The orders that vanished were small ones, about three thousand rupees each, which
already hints at why the average order grew.

## 2. Inside each segment, revenue per order moved a little

**Predict before you run.** Which segment's own revenue per order rose by about 18 percent? a)
Business; b) Retail-Plus; c) every segment; d) none of them.
"""),
        code('''
seg_rpo_change = {seg: (q2[seg]["revenue_per_order"] / q1[seg]["revenue_per_order"] - 1) * 100 for seg in SEGMENTS}
kit.table(["Segment", "Q1 revenue per order", "Q2 revenue per order", "Change"],
          [(seg, kit.rupees(round(q1[seg]["revenue_per_order"])), kit.rupees(round(q2[seg]["revenue_per_order"])),
            f"{seg_rpo_change[seg]:+.1f}%") for seg in SEGMENTS] +
          [("all orders, blended", kit.rupees(round(all1["revenue_per_order"])), kit.rupees(round(all2["revenue_per_order"])),
            f'{(all2["revenue_per_order"] / all1["revenue_per_order"] - 1) * 100:+.1f}%')],
          caption="Revenue per order inside each segment, and the blend")
kit.bars([(seg, round(seg_rpo_change[seg], 1)) for seg in SEGMENTS] + [("blended", 18.0)],
         fmt=lambda v: f"{v:+.1f}%", lit=[4], title="No segment rose 18 percent; the blend did")
kit.check("no segment's own revenue per order rose as far as 18 percent", max(seg_rpo_change.values()) < 18.0,
          f"largest {max(seg_rpo_change.values()):.1f}%")
'''),
        md("""
**What happened.** The answer is d. Business rose 5.0 percent, Retail-Plus 7.0, Student 14.8, and
Retail-Core fell 4.9. The blend rose 18.0 percent while no segment rose that far, so the blend moved
because the mix of orders moved.

## 3. The trap: 18 percent read as customers paying more

**The plausible wrong answer.** A hurried analyst reads the blended rise straight into the plan.
"""),
        code('''
wrong_rise = (all2["revenue_per_order"] / all1["revenue_per_order"] - 1) * 100
kit.stats([(f"{wrong_rise:+.1f}%", "revenue per order, blended", "read as: customers pay 18 percent more"),
           (kit.rupees(round(rise)), "more per order", "read as: room for a price rise"),
           ("0", "segments that rose 18 percent", "the check")])
kit.check("the hurried figure is plus 18.0 percent", round(wrong_rise, 1) == 18.0)
'''),
        md("""
**Why it is wrong.** Revenue per order is a blend. It rises whenever small orders fall away, even if
no customer pays a rupee more, and 25 small Retail-Plus orders fell away. Reading it as a price
signal would put a price rise on customers who never paid more, in the tier whose orders already
halved. **The check** is the table above: no segment's own revenue per order rose 18 percent.
**The fix** is option C: price Q2's order mix at Q1's revenue per order in each segment, and call
what is left the rate.
"""),
        code('''
s1 = [round(share1[seg] * 100, 1) for seg in SEGMENTS]
s2 = [round(share2[seg] * 100, 1) for seg in SEGMENTS]
kit.columns(SEGMENTS, [("Q1 share of orders", s1), ("Q2 share of orders", s2)], fmt=lambda v: f"{v:.1f}%", lit=[1],
            title="The order mix: Retail-Plus fell from 44.7 to 30.2 percent of orders")
kit.bridge(("Q1 revenue per order", round(all1["revenue_per_order"])), [("mix: fewer small orders", round(mix)), ("rate inside segments", round(rate))],
           end_label="Q2 revenue per order", lit=[0], lo=150000, fmt=kit.rupees,
           title="Revenue per order, split into mix and rate; the axis starts at Rs 1.5 lakh")
kit.check("at Q2's mix and Q1's rates, revenue per order is Rs 2,07,112", round(at_q2_mix) == 207112, kit.rupees(round(at_q2_mix)))
kit.check("mix explains about 69 percent of the rise", round(mix / rise * 100) == 69, f"{mix / rise * 100:.1f}")
'''),
        md("""
**What changed.** "Customers pay 18 percent more, raise prices" became "at Q2's mix and Q1's prices,
revenue per order would already have been Rs 2,07,112: the mix explains Rs 22,902 of the Rs 33,231
rise, about 69 percent, and the rate inside segments Rs 10,330". The price rise loses its evidence.

## 4. What the rate part is made of

The Rs 10,330 of rate is itself a blend of four segments' own changes, each weighted by its share of
Q2's orders. Business, whose orders are lakh-sized, dominates it.

**Predict before you run.** Which segment carries most of the rate part? a) Retail-Plus; b)
Retail-Core; c) Business; d) Student.
"""),
        code('''
rate_parts = {seg: share2[seg] * (q2[seg]["revenue_per_order"] - q1[seg]["revenue_per_order"]) for seg in SEGMENTS}
kit.bars([(seg, round(rate_parts[seg])) for seg in SEGMENTS], fmt=kit.rupees, lit=[2],
         title="The rate part by segment: Business carries almost all of it")
kit.check("the rate parts add back to the rate", abs(sum(rate_parts.values()) - rate) < 1e-6, kit.rupees(round(rate)))
kit.check("Business carries more than nine tenths of the rate part", rate_parts["Business"] / rate > 0.9,
          f'{rate_parts["Business"] / rate * 100:.1f}%')
'''),
        md("""
**What happened.** The answer is c. The rate part is almost all Business, whose 17 orders each grew
about Rs 52,000 on average, and one large order drives that, as chapter 3's range showed. The
consumer segments' own prices moved by a few hundred rupees at most.

## A second route: two groups on the back of an envelope

The split above priced four segments. An independent check treats Kalpa as two groups, Business and
everyone else, and asks how far the blend moves when only Business's share of orders moves: the
change in that share times the gap between a Business order and a consumer order, both at Q1's
values. It uses no rate inside the consumer business, so if the four-segment split had mispriced a
consumer segment, the two routes would disagree.
"""),
        code('''
consumer_q1 = [o for o in by_quarter["Q1"] if o["segment"] != "Business"]
consumer_rpo_q1 = sum(o["amount"] for o in consumer_q1) / len(consumer_q1)
gap_q1 = q1["Business"]["revenue_per_order"] - consumer_rpo_q1
envelope = (share2["Business"] - share1["Business"]) * gap_q1
kit.stats([(f'{share1["Business"] * 100:.1f}% to {share2["Business"] * 100:.1f}%', "Business's share of orders", "Q1 to Q2"),
           (kit.rupees(round(gap_q1)), "a Business order less a consumer order", "both at Q1's values"),
           (kit.rupees(round(envelope)), "the mix, from two groups", f"four segments gave {kit.rupees(round(mix))}")])
kit.columns(["four segments", "two groups"], [("mix", [round(mix), round(envelope)])], fmt=kit.rupees, width=520,
            title="The mix part of the Rs 33,231 rise, reached two ways")
kit.check("the two routes agree within 2 percent", abs(envelope - mix) / mix < 0.02, f"{envelope:.0f} and {mix:.0f}")
kit.check("both routes put more than two thirds of the rise on the mix", mix / rise > 2 / 3 and envelope / rise > 2 / 3,
          f"{mix / rise * 100:.1f} and {envelope / rise * 100:.1f}")
'''),
        md("""
**When to switch.** Report the four-segment split, since it names each segment's part. The envelope
is the check a senior runs in a meeting with no laptop, and it stops agreeing when the consumer
segments' own shares move a lot against each other, since it cannot see inside them.

> **Kavya's review.** "Marketing looked at a blend and saw a price signal. You opened the blend and
> found 25 small orders missing. Say it that way to Meera: no consumer segment paid meaningfully more,
> Business's share of orders rose from 17.5 to 19.8 percent as the small member orders left, and they
> left from the tier we are about to ask about."

### In the interview

**[F] Revenue per order rose 18 percent while revenue fell; did prices go up?** "Not necessarily,
and here mostly not. Revenue per order is a blend across segments whose orders differ in size, so it
rises whenever the small orders fall away. I split the change into mix and rate: price the later
period's mix at the earlier period's segment rates. On Kalpa's quarters mix explains Rs 22,902 of the
Rs 33,231 rise, about 69 percent, because small Retail-Plus orders disappeared, and Business carries
almost all of the rest. Then I check prices directly if the question matters." The interviewer is
listening for mix, the split, and a number for each part.

**The design question. When does a mix split matter, and when is a per-segment table enough?** "It
matters when the segments' rates differ a lot and their shares moved, since then the blend can move
with no segment moving; Kalpa's orders differ several hundredfold between Business and consumers, so it
matters here. When the segments look alike, or their shares held, the per-segment table says it all.
And I report the order of the split, since the joint part moves with it." The interviewer is
listening for the two conditions and the order.

### Depth: a mix inside one segment

Retail-Plus's own revenue per order rose 7.0 percent. That can be a mix as well: if the members who
place small orders are the ones who slowed, the tier's average order grows with no member paying
more. Try it: split the tier's rise by channel, the way this chapter split the company's by segment,
and say how much of the 7.0 percent is mix.

References for the chapter:

- Swiggy, Q2 FY2026 shareholder letter: https://www.swiggy.com/corporate/wp-content/uploads/2025/10/Q2-FY2026-Shareholder-letter.pdf (verified 30 Sep 2026)
- Khan Academy, summarizing quantitative data: https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data (verified 29 Sep 2026)
"""),
        code("""
kit.check_summary()
print("Next: chapter 5, Marketing's hypothesis tested on the same numbers.")"""),
    ]
    build(NB / "C2_W01_D02_04_mix_or_rate_STUDENT.ipynb", cells)


# --------------------------------------------------------------------------------------------- 5
def chapter5():
    cells = [
        head(5, "Marketing's hypothesis",
             "By the end of this notebook you can test Marketing's acquisition claim in its own terms, "
             "catch a helper that drops a segment without a word, and size the paid tier's fall "
             "against the business it belongs to."),
        md("""
> **Marketing pushes back.** "A flat count can hide churn replaced by new customers, which is why we
> need acquisition. And Retail-Plus is Rs 65,250 out of a Rs 23 lakh fall. Last quarter's summary
> script says Business fell most; it does not matter."
>
> The marketing lead, Kalpa Retail

**What chapter 4 established, and what this adds.** The rise in revenue per order is about 69
percent mix: 25 small Retail-Plus orders disappeared, and no consumer segment paid meaningfully more. Marketing now attacks the
finding on three fronts. This chapter adds two tools: a set of customer ids per quarter, which
answers the churn claim, and a small helper that turns two numbers into a percentage change, which
has to be checked before anyone trusts its summary.

> **Kavya's review of chapter 4.** "You told Marketing the consumer segments did not pay more. Expect them to come back
> with a better argument, and answer it with a check they can run themselves."
"""),
        code(SETUP + GROUPS + TOOLS + '''
q1 = {seg: tree_for(groups["Q1"][seg]) for seg in SEGMENTS}
q2 = {seg: tree_for(groups["Q2"][seg]) for seg in SEGMENTS}
print("segments carried from chapter 3:", ", ".join(SEGMENTS))'''),
        mapcell(5, ["the need: is acquisition the answer?", "the options: four ways to test churn",
                    "the id overlap", "customer by customer", "the trap: a helper that returns nothing",
                    "the consumer business", "a second route: first and last dates"]),
        md("""
## The need

Marketing's Rs 12 crore rests on one claim: Kalpa is losing customers, which is churn, and must
replace them. The
metric at stake is retention, the customers of Q1 who bought again in Q2, and its mirror, the new
customers of Q2. The decision riding on it is the acquisition budget itself. A wrong answer costs
either Rs 12 crore spent replacing customers who never left, or a retention problem left to run
while the money goes elsewhere.
"""),
        md(COMPANY[5]),
        md("""
## The options

Four ways to test "a flat count hides churn replaced by new customers".

| Option | How | Can it see churn? |
|---|---|---|
| A. Compare the counts | 69 in Q1 against 69 in Q2 | No: a count is net, so 20 lost and 20 new also give 69 and 69 |
| B. The id overlap | A set of ids per quarter; in both, only in Q1, only in Q2 | Yes, lost and new named separately |
| C. Customer by customer | Each id's Q1 and Q2 orders side by side | Yes, and who slowed down as well |
| D. Ask Marketing's CRM | New sign-ups by month from the campaign system | Only new customers, from a second system to reconcile |

The cell below sizes each on this file.
"""),
        code('''
ids = {"Q1": set(), "Q2": set()}
per_customer = {"Q1": {}, "Q2": {}}
for order in ORDERS:
    q, cid = order["quarter"], order["customer_id"]
    ids[q].add(cid)
    per_customer[q][cid] = per_customer[q].get(cid, 0) + 1
kit.table(["Option", "Output to read", "Sees lost and new?", "What it assumes"],
          [("A. counts", "2 numbers", "no", "nothing: a count is net"),
           ("B. id overlap", "3 numbers", "yes", "one id per person"),
           ("C. customer by customer", f"{len(ids['Q1'] | ids['Q2'])} rows", "yes, and who slowed", "one id per person"),
           ("D. Marketing's CRM", "sign-ups by month", "new only", "the CRM and the export share their ids")],
          caption="Sizing four tests of the churn claim")
kit.matrix(["A. counts", "B. overlap", "C. per customer"], ["sees lost", "sees new", "sees who slowed"],
           [["no", "no", "no"], ["yes", "yes", "no"], ["yes", "yes", "yes"]],
           title="What each test can see")
kit.check("the two quarters hold 69 distinct customer ids between them", len(ids["Q1"] | ids["Q2"]) == 69)
'''),
        md("""
**The best-fit call.** Option B, the id overlap, because it answers Marketing's claim exactly, lost
and new, in three numbers anyone can rerun; option C follows it because the next question is who
slowed. **The fact that would change the call:** if the ids were not stable, for example if the
store and the app gave the same person two ids, the overlap would invent churn, and the CRM, option
D, would be needed to join them first.

## 1. All 69 customers bought in both quarters

**Predict before you run.** How many of Q1's 69 customers are missing from Q2? a) about 20, replaced
by 20 new ones; b) about 5; c) none; d) it cannot be told from one export.
"""),
        code('''
both = ids["Q1"] & ids["Q2"]
lost = ids["Q1"] - ids["Q2"]
new = ids["Q2"] - ids["Q1"]
kit.bars([("bought in both quarters", len(both)), ("lost after Q1", len(lost)), ("new in Q2", len(new))],
         title="Customer ids across the two quarters: nobody lost, nobody new")
kit.check("all 69 customers bought in both quarters", len(both) == 69, f"{len(both)}")
kit.check("no customer was lost and none was new", len(lost) == 0 and len(new) == 0, f"{len(lost)} lost, {len(new)} new")
'''),
        md("""
**What happened.** The answer is c. Every one of the 69 Q2 customers bought in Q1: none lost, none
new. The flat count hides no churn, and acquisition has nothing to replace on this file.

## 2. Customer by customer, 23 slowed down and 18 of them are members

Option C: each customer's orders in Q2 minus their orders in Q1.

**Predict before you run.** Of the customers who placed fewer orders in Q2, how many are Retail-Plus
members? a) about a quarter; b) about half; c) most of them; d) none.
"""),
        code('''
segment_of = {o["customer_id"]: o["segment"] for o in ORDERS}
change_count = {}
slowed_by_segment = {}
for cid in ids["Q1"]:
    d = per_customer["Q2"].get(cid, 0) - per_customer["Q1"][cid]
    change_count[d] = change_count.get(d, 0) + 1
    if d < 0:
        slowed_by_segment[segment_of[cid]] = slowed_by_segment.get(segment_of[cid], 0) + 1
kit.columns([f"{d:+d}" for d in sorted(change_count)], [("customers", [change_count[d] for d in sorted(change_count)])],
            title="Customers by the change in their orders, Q2 minus Q1")
kit.bars([(seg, slowed_by_segment.get(seg, 0)) for seg in SEGMENTS], lit=[1],
         title="The customers who slowed down, by segment")
kit.check("23 customers placed fewer orders in Q2", sum(slowed_by_segment.values()) == 23)
kit.check("18 of the 23 are Retail-Plus members", slowed_by_segment.get("Retail-Plus", 0) == 18)
'''),
        md("""
**What happened.** The answer is c. Twenty-three customers placed fewer orders, and eighteen of them
are Retail-Plus members; 44 customers ordered exactly as often as before. The fall is people Kalpa
already has, buying less often, and most of them pay for membership.

## 3. The trap: last quarter's summary script says Business fell most

Marketing's third point comes from a colleague's script, left over from last quarter's report. Run it
exactly as it is, then read what the summary says.

**Predict before you run.** The script summarises the fall in orders per customer by segment. Which
segment will it say fell most? a) Retail-Plus; b) Business; c) Retail-Core; d) Student.

**The plausible wrong answer.** The script runs, prints a tidy summary, and nobody counts what came
back.
"""),
        code('''
def pct_change(before, after):
    change = 100 * (after - before) / before
    if abs(change) > 30:
        print(f"  check by hand: {change:+.1f}%")
    else:
        return round(change, 1)

changes = {}
for seg in SEGMENTS:
    changes[seg] = pct_change(q1[seg]["orders_per_customer"], q2[seg]["orders_per_customer"])
falls = {}
for seg, ch in changes.items():
    if ch and ch < 0:
        falls[seg] = ch
print("summary:", falls)
print("orders per customer fell in every segment, most in Business,", min(falls.values()), "percent")
kit.check("the summary names Business as the largest fall", min(falls, key=falls.get) == "Business")
'''),
        md("""
**Why it is wrong.** The answer to the prediction is b, and it is the wrong answer. `pct_change`
prints its warning for any change larger than 30 percent and returns nothing, so Python hands back
`None`. The filter `if ch and ch < 0` then drops every `None` without a word. Retail-Plus, whose
orders per member halved, is exactly the kind of large change the script was written to flag, and it
fell out of the summary. The decision it misleads: Meera opens Business accounts first, and the head
of Retail-Plus is told his tier is not in the table.

**The check** counts the groups in and the groups out: four segments went in.
"""),
        code('''
none_back = [seg for seg, ch in changes.items() if ch is None]
kit.flow(["4 segments in", "pct_change", f"{len(SEGMENTS) - len(none_back)} numbers back\\n{len(none_back)} None",
          f"{len(falls)} falls in the summary"], kinds=["plain", "bad", "bad", "bad"],
         title="Groups in, groups out: two segments came back with no number")
kit.check("two of the four segments came back as None", len(none_back) == 2, ", ".join(none_back))
'''),
        md("""
**The fix.** Return the change every time, in the same type, and put the "check by hand" flag in a
column of its own, so large moves are flagged instead of dropped.
"""),
        code('''
def pct_change_fixed(before, after):
    return round(100 * (after - before) / before, 1)

fixed = {seg: pct_change_fixed(q1[seg]["orders_per_customer"], q2[seg]["orders_per_customer"]) for seg in SEGMENTS}
kit.table(["Segment", "Q1", "Q2", "Change", "Flag"],
          [(seg, f'{q1[seg]["orders_per_customer"]:.2f}', f'{q2[seg]["orders_per_customer"]:.2f}', f"{fixed[seg]:+.1f}%",
            "check by hand" if abs(fixed[seg]) > 30 else "") for seg in SEGMENTS],
          caption="Orders per customer: every segment, every change")
kit.columns(SEGMENTS, [("Q1", [round(q1[s]["orders_per_customer"], 2) for s in SEGMENTS]),
                       ("Q2", [round(q2[s]["orders_per_customer"], 2) for s in SEGMENTS])],
            fmt=lambda v: f"{v:.2f}", lit=[1], title="Orders per customer by segment, with nothing dropped")
kit.check("the fixed summary has a number for every segment", None not in fixed.values() and len(fixed) == 4)
kit.check("Retail-Plus fell 49.0 percent and Student rose 40.0", (fixed["Retail-Plus"], fixed["Student"]) == (-49.0, 40.0))
'''),
        md("""
**What changed.** "Business fell most, 15.0 percent" became "Retail-Plus fell 49.0 percent, 2.32 to
1.18 orders per member, and Business 15.0 percent on three orders". Student, which rose, also came
back as `None` from the broken script, and the filter would have dropped it anyway because it rose.

## 4. Too small to matter? The consumer business, in its own terms

Marketing's rupee point is correct arithmetic and the wrong comparison. Business orders run to lakhs
and consumer orders to a few thousand rupees, so a consumer segment is judged against the consumer
business.

**Predict before you run.** What share of the consumer business's fall is Retail-Plus? a) about 3
percent; b) about a third; c) about 93 percent; d) all of it.
"""),
        code('''
CONSUMER = ["Retail-Core", "Retail-Plus", "Student"]
consumer_q1 = sum(q1[s]["revenue"] for s in CONSUMER)
consumer_q2 = sum(q2[s]["revenue"] for s in CONSUMER)
consumer_fall = consumer_q1 - consumer_q2
plus_fall = q1["Retail-Plus"]["revenue"] - q2["Retail-Plus"]["revenue"]
kit.bridge(("consumer revenue, Q1", consumer_q1), [(s, q2[s]["revenue"] - q1[s]["revenue"]) for s in CONSUMER],
           end_label="consumer revenue, Q2", lit=[1],
           title="The consumer business, Rs 2,28,820 to Rs 1,58,540: Retail-Plus is most of the fall")
kit.check("the consumer business fell Rs 70,280", consumer_fall == 70280, kit.rupees(consumer_fall))
kit.check("Retail-Plus is 93 percent of the consumer fall", round(plus_fall / consumer_fall * 100) == 93,
          f"{plus_fall / consumer_fall * 100:.1f}")
'''),
        md("""
**What happened.** The answer is c. Retail-Plus is Rs 65,250 of the Rs 70,280 consumer fall, 93
percent, and 25 of the 28 lost orders. The rupee fall in Business is three orders out of twenty,
each worth lakhs, so one account ordering early or late moves it by lakhs. The two
findings go to Meera side by side: the rupees in Business, with their caveat, and the behaviour in
Retail-Plus, with its count.

## A second route: each customer's first and last order

Section 1's overlap trusted the `quarter` field and set arithmetic. A second route uses only the
dates: each customer's first and last order in the export. A customer whose first order falls in Q2
is new, and one whose last order falls in Q1 was lost. If the quarter field were wrong, or the sets
had been built on the wrong field, the two routes would disagree.
"""),
        code('''
first, last = {}, {}
for order in ORDERS:
    cid, d = order["customer_id"], order["order_date"]
    first[cid] = min(first.get(cid, d), d)
    last[cid] = max(last.get(cid, d), d)
new_by_date = [cid for cid in first if first[cid] >= "2026-07-01"]
lost_by_date = [cid for cid in last if last[cid] <= "2026-06-30"]
MONTHS = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]
firsts = [sum(1 for d in first.values() if d[:7] == m) for m in MONTHS]
lasts = [sum(1 for d in last.values() if d[:7] == m) for m in MONTHS]
kit.columns(["Apr", "May", "Jun", "Jul", "Aug", "Sep"], [("first order", firsts), ("last order", lasts)],
            title="Customers by the month of their first and their last order in the export")
kit.table(["Route", "New in Q2", "Lost after Q1"],
          [("the id overlap, section 1", len(new), len(lost)), ("first and last dates", len(new_by_date), len(lost_by_date))],
          caption="Lost and new, counted two ways")
kit.check("the dates find the same lost and new counts as the overlap", (len(new_by_date), len(lost_by_date)) == (len(new), len(lost)))
'''),
        md("""
**When to switch.** Show Marketing the overlap, since it names lost and new in three numbers. The
dates add a warning the overlap cannot: a first order in this export is only the first since
1 April, so on a longer question "new" needs each customer's whole history, which the CRM holds.

> **Kavya's review.** "Three attacks, three checks anyone can rerun: the overlap for churn, groups in
> and out for the script, and the consumer business for size. And you nearly shipped a summary that
> lost the one segment that matters. Count what comes back from every helper you did not write."

### In the interview

**[D] Marketing insists the answer is acquisition and your data says frequency; how do you make the
case in the room?** "I take their claim seriously and test it in its own terms, with a check they can
repeat. Acquisition predicts more customers, or churn replaced by new ones, so I show the count, 69
and 69, and the overlap: every Q2 customer bought in Q1, none lost, none new. Then I show where the
fall is, orders per customer from 1.65 to 1.25, and in the consumer business Retail-Plus is 93
percent of the fall. I end on what would change my mind, which keeps it a question of evidence."
The interviewer is listening for the test that would falsify Marketing's claim, and a calm tone.

**[F] Why does a function that prints instead of returning break a pipeline?** "Printing sends the
answer to the screen and returns `None` to the caller. The next step receives `None` and either
crashes or, worse, carries on: here a filter dropped every `None` and two of four segments vanished
from the summary, including the one that fell 49 percent. A function returns its answer every time,
in the same type, and a flag goes in its own column." The interviewer is listening for `None`, the
silent case, and computing kept apart from showing.

**[SV] The customer count is flat quarter on quarter; does that prove no customers were lost?** "No;
a count is net. The test is the overlap of ids: in both periods, only in the first, only in the
second. Here it came out 69, 0 and 0." The interviewer is listening for overlap, lost and new.

**The design question. How would you test "a flat count hides churn", and what would make you
distrust your own test?** "The id overlap, because it names lost and new separately in three numbers.
I would distrust it if one person can hold two ids, say one from the store and one from the app,
since then the overlap invents churn; I would join the ids through the CRM first." The interviewer
is listening for the assumption under the test.

### Depth: when ids are not people

Try it: invent five orders where one customer shops in the store as `C-9001` and in the app as
`C-9002`, and show that the overlap reports one lost and one new customer who is the same person.

References for the chapter:

- Amy Gallo, "The Value of Keeping the Right Customers", Harvard Business Review, 29 October 2014: https://hbr.org/2014/10/the-value-of-keeping-the-right-customers (verified 30 Sep 2026)
- Python docs, sets: https://docs.python.org/3/tutorial/datastructures.html#sets (verified 30 Sep 2026)
"""),
        code("""
kit.check_summary()
print("Next: chapter 6, the head of Retail-Plus hands us a cause, and the memo says what would test it.")"""),
    ]
    build(NB / "C2_W01_D02_05_marketings_hypothesis_STUDENT.ipynb", cells)


# --------------------------------------------------------------------------------------------- 6
def chapter6():
    cells = [
        head(6, "The memo and its evidence",
             "By the end of this notebook you can test a stakeholder's cause with the data in hand, "
             "put a ceiling on what it could explain, and write the memo's claim with two hypotheses "
             "and the evidence that would settle each."),
        md("""
> **The tier offers a cause.** "It is the broken reorder button. One of my members says it has been
> broken for six weeks."
>
> The head of Retail-Plus

> **And the CEO wants one page.** "Which branch, which segment, and what you would bet on. Tell me
> what you know and what you are guessing."
>
> Meera Raghavan, CEO, Kalpa Retail

**What chapter 5 established, and what this adds.** Nobody was lost and nobody was new; 18 of the 23
customers who slowed are members; Retail-Plus is 93 percent of the consumer fall, 51 orders to 26 on
the same 22 members. This chapter grows chapter 1's accumulator into a counting function that takes
any key, by month or by channel, and uses it to test the cause the head of Retail-Plus hands us.
"""),
        code(SETUP + GROUPS + TOOLS + '''
from datetime import date, timedelta


def pct_change(before, after):
    """Chapter 5's fixed helper: the change every time, in the same type."""
    return round(100 * (after - before) / before, 1)


def count_by(rows, key):
    """Chapter 1's accumulator, grown: count the rows under whatever key(row) returns."""
    counts = {}
    for row in rows:
        k = key(row)
        counts[k] = counts.get(k, 0) + 1
    return counts

plus = [o for o in ORDERS if o["segment"] == "Retail-Plus"]
core = [o for o in ORDERS if o["segment"] == "Retail-Core"]
print(len(plus), "Retail-Plus orders and", len(core), "Retail-Core orders across both quarters")'''),
        mapcell(6, ["the need: is it the button?", "the options: four tests of a cause",
                    "orders by month", "the trap: the button blamed for 25 orders",
                    "the season, a rival", "the channel the cause predicts", "a second route: the pace, corrected",
                    "the memo"]),
        md("""
## The need

The head of Retail-Plus wants engineering to fix the reorder button now and wants the fall in his
tier put down to it. The metric at stake is Retail-Plus orders per week, before and after the date
the button broke. The decision riding on it is two things: what goes to engineering first, and what
Meera is told caused the fall. A wrong answer costs a quarter: blame the button for everything, fix
it, and the tier keeps falling for a reason nobody looked for; or dismiss it, and members keep
failing to reorder.
"""),
        md(COMPANY[6]),
        md("""
## The options

Four ways to test a cause with the data in hand, and one way beyond it.

| Option | How | What it can rule out |
|---|---|---|
| A. Before and after the break | Retail-Plus orders per week before 25 August and after | The button as the whole story, if the fall began before it broke |
| B. A comparison segment | Retail-Core over the same months | A season or a market that hit every customer |
| C. The channel it predicts | A broken app feature can only stop app orders | An app-only cause, if the web and the store fell too |
| D. The app's logs | Reorder attempts and failures by week, and the release that broke it | Nothing today: a data request, days away |

The cell below sizes each on this file: rows read, and the verdict each one can reach today.
"""),
        code('''
BREAK = (date(2026, 10, 6) - timedelta(weeks=6)).isoformat()      # "six weeks", taken at its word
kit.table(["Option", "Rows read", "Needs", "Can reach today"],
          [("A. before and after", len([o for o in plus if o["quarter"] == "Q2"]) + len([o for o in plus if o["quarter"] == "Q1"]), "the break date", "a ceiling on the button's share"),
           ("B. comparison segment", len(plus) + len(core), "a segment the cause cannot touch", "season in or out"),
           ("C. the channel", len(plus), "the channel field", "app-only in or out"),
           ("D. the app's logs", 0, "a data request", "the settlement, later")],
          caption=f"Sizing four tests; the break is taken as {BREAK}")
kit.decision_ladder(["D. the app's logs: settles it, days away", "C. the channel: rules app-only in or out",
                     "B. a comparison segment: rules the season in or out", "A. before and after: timing first"],
                    cut_at=0, title="Run the cheap tests in order, and request the one that settles it")
kit.check("the break date is 25 August", BREAK == "2026-08-25")
'''),
        md("""
**The best-fit call.** A, B and C now, in that order, because each reads the export already open and
timing comes first, since a cause cannot come after its effect; D requested today, because only the
logs settle it. **The fact that would change the call:** if the complaint's date turned out to be
wrong, say the button broke in June, option A's verdict flips, and the request for the release date
in option D is how we would find out.

## 1. Orders by month: the tier stepped down in July

**Predict before you run.** When did Retail-Plus orders drop below every Q1 month? a) in September,
after the break; b) in August, when the button broke; c) in July, before it broke; d) they never did.
"""),
        code('''
plus_month = count_by(plus, lambda o: o["order_date"][:7])
core_month = count_by(core, lambda o: o["order_date"][:7])
months = sorted(plus_month)
kit.line(["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
         [("Retail-Plus", [plus_month[m] for m in months], "bad"), ("Retail-Core", [core_month.get(m, 0) for m in months], "plain")],
         title="Orders by month: Retail-Plus steps down in July; the complaint dates the break to late August")
kit.check("the months run April to September", months == ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"])
kit.check("Retail-Plus July sits below every Q1 month", plus_month["2026-07"] < min(plus_month[m] for m in months[:3]))
'''),
        md("""
**What happened.** The answer is c. Retail-Plus orders were down in July, weeks before the late-August
break the complaint dates. The button may still matter; it cannot be the whole story.

## 2. The trap: the button blamed for all 25 orders

**The plausible wrong answer.** A hurried analyst puts the tier's whole fall in the memo as the
button's cost: 51 orders in Q1, 26 in Q2, so the button cost 25 orders and Rs 65,250.
"""),
        code('''
q1_plus = len([o for o in plus if o["quarter"] == "Q1"])
q2_plus = len([o for o in plus if o["quarter"] == "Q2"])
wrong_orders = q1_plus - q2_plus
wrong_rupees = sum(o["amount"] for o in plus if o["quarter"] == "Q1") - sum(o["amount"] for o in plus if o["quarter"] == "Q2")
kit.stats([(str(wrong_orders), "orders the button 'cost'", "Q1 total less Q2 total"),
           (kit.rupees(wrong_rupees), "rupees the button 'cost'", "the whole tier's fall"),
           ("0", "days checked before the break", "the check that is missing")])
kit.check("the hurried memo blames the button for 25 orders and Rs 65,250", (wrong_orders, wrong_rupees) == (25, 65250))
'''),
        md("""
**Why it is wrong.** The comparison spans the whole quarter, so it charges the button with every
order lost since 1 July, including the eight weeks or so before it broke. Engineering would be told the fix
recovers 25 orders a quarter, and when it ships and recovers a handful, the tier's real problem has
had another quarter to run. **The check** splits Q2 at the break and gives each side its window, as
chapter 1 taught: a rate per week, with dates.
"""),
        code('''
days_q1 = 91
days_before = (date.fromisoformat(BREAK) - date(2026, 7, 1)).days
days_after = (date(2026, 9, 30) - date.fromisoformat(BREAK)).days + 1
before = len([o for o in plus if o["quarter"] == "Q2" and o["order_date"] < BREAK])
after = q2_plus - before
per_week = {"Q1": q1_plus / days_q1 * 7, "before": before / days_before * 7, "after": after / days_after * 7}
kit.table(["Window", "Days", "Orders", "Orders per week"],
          [("Q1, 1 Apr to 30 Jun", days_q1, q1_plus, f'{per_week["Q1"]:.2f}'),
           ("Q2, 1 Jul to 24 Aug", days_before, before, f'{per_week["before"]:.2f}'),
           ("Q2, 25 Aug to 30 Sep", days_after, after, f'{per_week["after"]:.2f}')],
          caption="Retail-Plus orders per week, split at the break")
kit.columns(["Q1", "Q2 before the break", "Q2 after the break"],
            [("orders per week", [round(per_week["Q1"], 2), round(per_week["before"], 2), round(per_week["after"], 2)])],
            fmt=lambda v: f"{v:.2f}", width=560, title="Most of the fall happened before the break the complaint dates")
kit.check("18 Retail-Plus orders before the break and 8 after", (before, after) == (18, 8))
kit.check("the weekly rate had already fallen by more than a third before the break",
          per_week["before"] < per_week["Q1"] * 2 / 3, f'{per_week["Q1"]:.2f} to {per_week["before"]:.2f}')
'''),
        md("""
**The fix.** Charge the button with no more than the fall after the break beyond the pace the tier
had already dropped to. At the pre-break pace of 18 orders in 55 days, the 37 days after the break
would have carried about 12.1 orders; the tier placed 8. So the button explains at most about 4 orders
in the quarter, about Rs 12,400 at Q2's Retail-Plus revenue per order, and it is a ceiling, since
anything else that kept worsening would claim part of it.
"""),
        code('''
ceiling = (before / days_before - after / days_after) * days_after
plus_rpo_q2 = tree_for(groups["Q2"]["Retail-Plus"])["revenue_per_order"]
kit.bars([("hurried memo: the whole tier's fall", wrong_orders), ("ceiling after the fix", round(ceiling, 1))],
         fmt=lambda v: f"{v:g} orders", lit=[1], title="What the button can be charged with, in orders")
kit.check("the button explains at most about 4.1 orders", round(ceiling, 1) == 4.1, f"{ceiling:.2f}")
kit.check("the ceiling is worth about Rs 12,400", round(ceiling * plus_rpo_q2, -2) == 12400, kit.rupees(round(ceiling * plus_rpo_q2)))
'''),
        md("""
**What changed.** "The button cost 25 orders, Rs 65,250" became "the fall began in July, before the
break; the button can explain at most about 4 orders, about Rs 12,400, and the rest needs another
cause". Engineering still fixes the button; the memo stops promising it fixes the tier.

## 3. The season, a rival to every cause

July opens the monsoon quarter, so a seasonal dip would also begin in July. A season that hit every
customer would move the comparison segment too.

**Predict before you run.** Retail-Core kept what share of its Q1 orders in Q2? a) about half, like
Retail-Plus; b) about three quarters; c) about 95 percent; d) more than all of them.
"""),
        code('''
core_ratio = len([o for o in core if o["quarter"] == "Q2"]) / len([o for o in core if o["quarter"] == "Q1"])
plus_ratio = q2_plus / q1_plus
kit.columns(["Retail-Plus", "Retail-Core"], [("share of Q1 orders kept in Q2", [round(plus_ratio * 100), round(core_ratio * 100)])],
            fmt=lambda v: f"{v}%", width=520, title="A season that hit everyone would have moved Retail-Core too")
kit.check("Retail-Core kept more than nine tenths of its Q1 orders", core_ratio > 0.9, f"{core_ratio:.2f}")
kit.check("Retail-Plus kept about half", 0.45 < plus_ratio < 0.55, f"{plus_ratio:.2f}")
'''),
        md("""
**What happened.** The answer is c. Retail-Core kept 95 percent of its Q1 orders and Retail-Plus 51,
so a season that hit every customer does not fit. A season that hit members harder still fits, and
only last year's Q2 by segment rules it out; it goes on the data request.

## 4. The channel the cause predicts

A broken app feature can only stop orders placed through the app. If it were the whole cause, the app
would have fallen and the web and the store would have held.

**Predict before you run.** Which Retail-Plus channels fell between Q1 and Q2? a) only the app; b)
the app and the web; c) every channel; d) none.
"""),
        code('''
by_channel = {q: count_by([o for o in plus if o["quarter"] == q], lambda o: o["channel"]) for q in ("Q1", "Q2")}
CHANNELS = ["web", "store", "app"]
fell = {ch: by_channel["Q2"][ch] < by_channel["Q1"][ch] for ch in CHANNELS}
kit.columns(CHANNELS, [("Q1 orders", [by_channel["Q1"][c] for c in CHANNELS]), ("Q2 orders", [by_channel["Q2"][c] for c in CHANNELS])],
            lit=[2], title="Retail-Plus orders by channel: every channel fell, the app no more than the others")
kit.check("every channel fell", fell == {"web": True, "store": True, "app": True}, str(fell))
kit.check("the app fell by a smaller share than the web", by_channel["Q2"]["app"] / by_channel["Q1"]["app"] > by_channel["Q2"]["web"] / by_channel["Q1"]["web"])
'''),
        md("""
**What happened.** The answer is c. The web fell from 24 to 9, the store from 14 to 9, and the app
from 13 to 8. An app-only cause predicts the app falling first and alone, and it did not; something
touched members in every channel.

## A second route: the pace, corrected by a segment the button cannot touch

Section 2's ceiling assumed the tier would have kept its pre-break pace. An independent check asks
what happened across the same date to Retail-Core, which the button did not touch because the
complaint is about members' reorders. If every customer slowed a little after 25 August, part of the
tier's shortfall belongs to that and not to the button. Scale the tier's expected orders by
Retail-Core's own change in pace across the break, then compare with what the tier placed. If the
button were the only thing moving, this route would give the same 4.1 orders; if something else
slowed every customer, it gives fewer, which is why section 2's figure is a ceiling.
"""),
        code('''
core_before = len([o for o in core if o["quarter"] == "Q2" and o["order_date"] < BREAK])
core_after = len([o for o in core if o["quarter"] == "Q2"]) - core_before
core_change = (core_after / days_after) / (core_before / days_before)
route_two = before / days_before * days_after * core_change - after
cum_days = list(range(1, 93))
q2_dates = sorted(date.fromisoformat(o["order_date"]) for o in plus if o["quarter"] == "Q2")
actual_cum = [sum(1 for d in q2_dates if (d - date(2026, 7, 1)).days < n) for n in cum_days]
pace_cum = [round(before / days_before * n, 2) for n in cum_days]
kit.line([str(n) if n % 15 == 1 else "" for n in cum_days],
         [("pre-break pace, carried on", pace_cum, "plan"), ("Retail-Plus orders, Q2", actual_cum, "bad")],
         fmt=lambda v: f"{v:.0f}", title="Section 2's reading: Q2 orders against the pace set before the break (day 56 is 25 August)")
kit.bars([("section 2: the pre-break pace", round(ceiling, 1)), ("second route: corrected by Retail-Core", round(route_two, 1))],
         fmt=lambda v: f"{v:g} orders", lit=[1], title="What the button can be charged with, reached two ways")
kit.check("Retail-Core placed 22 orders before the break and 14 after", (core_before, core_after) == (22, 14))
kit.check("the corrected route charges the button no more than the ceiling", 0 < route_two <= ceiling, f"{route_two:.2f}")
'''),
        md("""
**When to switch.** Write section 2's ceiling in the memo, since it assumes nothing about any other
segment; bring the corrected route when someone argues for the season, since it takes out what hit
Retail-Core as well. Here it charges the button with about 3.5 orders, inside the ceiling of about 4.

## The memo: the claim and the evidence that settles each hypothesis

Neither cause is proved or disproved by this export. Each is a hypothesis, and each is settled by data
Kalpa holds elsewhere.
"""),
        code('''
EVIDENCE = {
    "export": "orders per customer by segment from this export, again",
    "campaigns": "Marketing's new-customer campaign reach by month",
    "app_logs": "the app's reorder attempts and failures by week, the release that broke it, and whether members who used reorder in Q1 fell more",
    "tier_log": "the tier's change log for benefits, prices and delivery terms in July, renewals, and members' support tickets",
    "last_year": "last year's Q1 and Q2 orders by segment",
}
HYPOTHESES = {"H1, the reorder button deepened the fall after 25 August": "app_logs",
              "H2, something changed for members in July": "tier_log",
              "Rival, a monsoon dip that hit members harder": "last_year"}
kit.tree({"label": "Retail-Plus: the same 22 members, 51 orders to 26", "kind": "lit", "branches": [
    ("H1", {"label": "reorder button, from 25 Aug\\nat most about 4 orders", "kind": "unknown", "branches": [
        ("settled by", {"label": "reorder logs by week;\\nthe release date", "kind": "known"})]}),
    ("H2", {"label": "a change for members\\nin July", "kind": "unknown", "branches": [
        ("settled by", {"label": "tier change log, renewals,\\nsupport tickets", "kind": "known"})]})]},
    title="Two hypotheses, each with the evidence that would settle it")
kit.check("every hypothesis is settled by data this export does not carry",
          all(v not in ("export", "campaigns") for v in HYPOTHESES.values()))
kit.check("no two hypotheses share their evidence", len(set(HYPOTHESES.values())) == len(HYPOTHESES))
'''),
        md("""
**The memo's claim, as it goes to Meera and the head of Retail-Plus.** "Revenue fell 11.0 percent
between two closed quarters, Rs 2.10 crore to Rs 1.87 crore on the export as it stands. Customers held
at 69, all of them buying in both quarters, so acquisition is not the branch that moved; orders per
customer fell from 1.65 to 1.25. In behaviour the fall sits in Retail-Plus, where the same 22 members
placed 26 orders against 51, and revenue per order rose mainly because those small orders
disappeared. In rupees most of the fall is three fewer Business orders, each worth lakhs, so one account's timing moves it by lakhs. The fall began in July, before the reorder button broke,
and hit every channel, so the button can explain at most about 4 orders. Two hypotheses remain: the
button deepened the fall after 25 August, settled by the app's reorder logs by week and the release
date; and something changed for members in July, settled by the tier's change log, renewals and
support tickets. Last year's Q2 by segment rules the season in or out. We are asking for all three."

> **Kavya's review.** "You gave the head of Retail-Plus a number for his cause, a ceiling of about 4
> orders, instead of a yes or a no. That is what a hypothesis looks like when it is handled well.
> Now say what you know and what you are guessing, in that order, and stop."

### In the interview

**[D] A stakeholder hands you a cause; how do you test it with the data you have and name the data
you need?** "I restate it as a hypothesis with a mechanism and test what the mechanism predicts,
timing first, since a cause cannot come after its effect. The broken reorder button predicted a fall
starting in late August and sitting in the app; the data shows a fall that began in July and hit
every channel. That does not rule the button out; it caps it, here at about 4 orders. Then I name the
data that settles it, the reorder logs by week and the release date, and a second hypothesis with its
own evidence." The interviewer is listening for predictions tested against timing, a ceiling, and a
named data request.

**[S] Sales dropped; what goes in the one-page memo?** "The confirmed size on matched windows, the
branch with its rupees, the segment with its denominator, what the obvious readings got wrong, and
each cause as a hypothesis with the evidence that would settle it. What we know comes first and what
we are guessing second, and each guess carries its test." The interviewer is listening for the
separation of fact from hypothesis.

**The design question. Which test of a cause do you run first, and when do you stop testing and ask
for new data?** "Timing first, because it is cheap and can rule a cause out outright; then a
comparison group, for the season; then the channel the cause predicts. I stop when the export can only
cap a cause, not settle it, and then the request names the exact data: here the reorder logs by week."
The interviewer is listening for an order with a reason, and a stopping rule.

### Depth: logs that cannot see their own failures

A failure log that records only the attempts that reached the server misses every member whose tap
never got that far, so the members most hurt by a break may be the ones the log cannot see. That
absence is not random, which is chapter 2's missing discount field in a new place. Ask which system
writes the log, and what it does when the app never calls it.

The ceiling also rests on a baseline: the tier's pace over all 55 days from 1 July to the break. Try
it: take only the 37 days just before the break as the baseline, the same length as the window after
it, and recompute the ceiling. Say which baseline you would defend to the head of Retail-Plus, and
why the memo has to name the one it used.

References for the chapter:

- Sonos, "Sonos Reports Third Quarter Fiscal 2024 Results": https://investors.sonos.com/news-and-events/investor-news/latest-news/2024/Sonos-Reports-Third-Quarter-Fiscal-2024-Results/ (verified 30 Sep 2026)
- Brit Institute, data analyst case study questions: https://britinstitute.uk/blog/data-analyst-case-study-interview-questions (verified 29 Sep 2026)
"""),
        code("""
kit.check_summary()
print("Next: the escalated case, the whole ladder again on the orders that reached customers.")"""),
    ]
    build(NB / "C2_W01_D02_06_the_memo_STUDENT.ipynb", cells)


if __name__ == "__main__":
    import importlib
    wanted = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 5, 6]
    for n in wanted:
        fn = globals().get(f"chapter{n}")
        if fn is None:
            print("no builder yet for chapter", n)
            continue
        fn()
        print("built chapter", n)

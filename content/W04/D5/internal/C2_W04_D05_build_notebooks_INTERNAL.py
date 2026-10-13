"""Write Friday's eight notebooks and execute each cold in its own folder.

Notebooks 01 to 04 teach the row's five subtopics on the invented chai stall; 05 to 07 apply them
to the Flipkart case, one per case chapter; 08 runs the same method on Kalpa in the lab.

    python3 content/W04/D5/internal/C2_W04_D05_build_notebooks_INTERNAL.py

The markdown here is the notebooks' prose, so the humanizer's file-mode read runs on this script.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import md, code, empty, build  # noqa: E402

NB = ROOT / "content" / "W04" / "D5" / "notebooks"
LABEL = ("Illustrative case: the company is real, the situation and the data are synthetic, built "
         "for this class.")
TICKET = f"""**The ticket.** Flipkart, the Lucknow fulfilment centre (FC), the warehouse where orders are packed
and shipped. The centre has 104 weeks of outbound shipments, the weeks beginning Monday 30 September
2024 to Monday 21 September 2026. Diwali fell on Thursday 31 October 2024 and Monday 20 October 2025,
and falls on Sunday 8 November 2026; the festive sale runs in the third and second weeks before
Diwali's week. A packer packs about 120 shipments a shift, and a packer-shift is one packer working
one shift. The planner must book packer shifts for the eight weeks beginning 12 October to 30
November 2026, the festive window. A vendor's demand model promises the window 22 percent above the
same weeks last year; finance's rule is those weeks plus 4 percent: eighteen percentage points apart.
A late shipment costs Rs 25 (assumed, Rs 15 to 40). A spare shipment, planned for and never shipped,
leaves part of a packer-shift idle: Rs 650 a shift (assumed, Rs 500 to 800) over 120 shipments, Rs
5.42 a shipment. {LABEL}"""

SETUP = '''import math
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"figure.figsize": (9, 3.8), "font.size": 11,
                     "axes.spines.top": False, "axes.spines.right": False})

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
'''


STALL = ("The chai stall is invented: it sits at a hostel gate, and every cup in this notebook is an "
         "invented number written by the day's seeded generator.")


def nb01():
    return [
        md(f"""
        # Trend and seasonality, read before modelling: what does a series tell you before any rule is chosen?

        **Week 4, Friday, concept notebook 1 of 4, beside chapter 1 of the deck.** {STALL}

        **Who needs the answer.** The stall's owner (invented), who orders milk every evening for
        the next three days, and Flipkart's FC planner, who books packer shifts weeks ahead. A
        reading that takes the weekly dip for a fall, or a weekday rise for growth, orders milk
        that sours and packers who stand idle.

        **The questions on the way.** What repeats, and how often? Is the stall growing? What
        repeats once a year? What is left over?
        """),
        code(SETUP + '''
# the invented stall's first fourteen days, and the same fourteen days 52 weeks later
two = pd.read_csv("../data/C2_W04_D05_chai_stall_fortnights_STUDENT.csv")
check("fourteen days in each year", len(two) == 14)
check("each 2025 day is the same weekday 364 days on",
      ((pd.to_datetime(two.date_2025) - pd.to_datetime(two.date_2024)).dt.days == 364).all())
two                                           # the whole table; every number in it is invented
'''),
        md("""
        ## What repeats, and how often?

        A **time series** is one number per equal period, in time order: cups a day at the stall
        (invented), shipments a week at Flipkart, revenue a month at Kalpa. A **forecast** is a
        number for a period nobody has seen yet.

        **Predict before you run.** The stall (invented) sold 60 cups on Sunday 6 October 2024 and
        100 on Monday 7 October. What does that say?

        a) The stall is growing fast: Monday is 67 percent above the day before.
        b) That is the weekly beat: Sundays always sell less, and nothing has grown.
        c) Two days are too few to say anything.
        d) Weekdays rose while Sundays did not.
        """),
        code('''
cups = two.set_index("date_2024").cups_2024                  # the 2024 fortnight, one number a day
labels = pd.to_datetime(two.date_2024).dt.strftime("%a %d %b")
fig, ax = plt.subplots()
ax.bar(labels, two.cups_2024, edgecolor="slateblue",
       color=["crimson" if d == "Sun" else "lavender" for d in two.weekday])
ax.tick_params(axis="x", rotation=60)
ax.set_ylabel("cups sold")
ax.set_title("The stall's first fourteen days, Sundays in red (invented numbers)")
plt.show()
by_hand = 100 / 60 - 1                                       # Monday over Sunday, counted by hand
by_code = cups["2024-10-07"] / cups["2024-10-06"] - 1
print(f"Monday over Sunday: {by_code:.0%} up")
print(f"Monday against the Monday before: {cups['2024-10-07']} against {cups['2024-09-30']}")
check("by hand and by code, Monday reads 67 percent above Sunday", round(by_hand, 4) == round(by_code, 4))
check("against the Monday before, the stall did not move", cups["2024-10-07"] == cups["2024-09-30"])
'''),
        md("""
        **What happened.** The answer is b. Both Sundays sold about 60 (60 and 61) and every other
        day about 100. A repeat on a fixed beat is a **season**, and its **length** is the number of
        periods before it repeats: 7 days here, 52 weeks in Flipkart's year. Monday against the
        Monday before reads 100 against 100, so nothing grew this week.

        ## Is the stall growing?

        Count it by hand first, comparing the same point a season apart. Monday 6 October 2025
        sold 110 against Monday 7 October 2024's 100: 110 over 100 is 1.10, up 10 percent in a
        year. Sunday 5 October 2025 sold 66 against 60: 1.10 again. The **trend** is that slow
        climb, and the function below reads it for any pair of points.
        """),
        code('''
def season_apart(now, before):
    """Growth read the chapter's way: the same point one season apart, as a share."""
    return now / before - 1

monday = season_apart(two.cups_2025[7], two.cups_2024[7])            # Mon 6 Oct 2025 against Mon 7 Oct 2024
fortnight = season_apart(two.cups_2025.sum(), two.cups_2024.sum())    # all fourteen days at once
share = [two.cups_2024[6] / two.cups_2024[7], two.cups_2025[6] / two.cups_2025[7]]   # Sunday over Monday
print(f"Monday a season apart: {monday:.0%}")
print(f"the two fortnights: {two.cups_2025.sum():,} over {two.cups_2024.sum():,}, {fortnight:.1%}")
print(f"Sunday's share of Monday: {share[0]:.1f} in 2024 and {share[1]:.1f} in 2025")
ax = two[["cups_2024", "cups_2025"]].set_axis(["2024", "2025"], axis=1).plot.bar(color=["lavender", "slateblue"],
                                                                                 edgecolor="slateblue")
ax.set_xticklabels(two.weekday, rotation=0)
ax.set_ylim(0, 140)
ax.legend(ncol=2, loc="upper left")
ax.set_ylabel("cups sold")
ax.set_title("The same fourteen days a year apart: same shape, about 10 percent higher (invented)")
plt.show()
check("by hand and by code, Monday grew 10 percent in a year", round(monday, 2) == round(110 / 100 - 1, 2))
check("Sunday's share stays 0.6 in both years", [round(s, 1) for s in share] == [0.6, 0.6])
'''),
        md("""
        **What happened.** The stall (invented) grew 10 percent a year on the Mondays and 10.3
        percent across the fortnight, while Sunday stayed 0.6 of a Monday in both years: the beat
        keeps its shape as the level climbs.

        ## What repeats once a year?

        The full record (invented) runs 730 days. Each semester closes with an exam fortnight, and
        the hostel empties for Diwali week, the week that held Diwali on 31 October 2024 and on 20
        October 2025.

        **Predict before you run.** At the stall, is Diwali week a peak, like the exams, or a dip?
        """),
        code('''
stall = pd.read_csv("../data/C2_W04_D05_chai_stall_daily_STUDENT.csv", parse_dates=["date"])
weekdays = stall[stall.weekday != "Sun"]

def season_ratio(start, days):
    """A season's weekdays against the fortnight of weekdays just before it."""
    start = pd.Timestamp(start)
    inside = weekdays[(weekdays.date >= start) & (weekdays.date < start + pd.Timedelta(days=days))]
    before = weekdays[(weekdays.date >= start - pd.Timedelta(days=14)) & (weekdays.date < start)]
    return inside.cups.mean() / before.cups.mean()

exam = [season_ratio("2024-11-27", 14), season_ratio("2025-11-26", 14)]     # the November exam fortnights
diwali = [season_ratio("2024-10-28", 7), season_ratio("2025-10-20", 7)]     # the weeks holding Diwali
stall["week"] = (stall.date - stall.date[0]).dt.days // 7                    # the stall's week, from Mon 30 Sep 2024
weekly = stall[stall.week < 104].groupby("week").cups.sum()
fig, ax = plt.subplots()
ax.plot(range(52), weekly.iloc[:52].values, color="plum", label="2024-25, from Mon 30 Sep 2024")
ax.plot(range(52), weekly.iloc[52:].values, color="slateblue", label="2025-26, from Mon 29 Sep 2025")
ax.set_xlabel("week of the stall's year")
ax.set_ylabel("cups in the week")
ax.set_title("Two years of the stall's weeks, laid over each other (invented numbers)")
ax.legend()
plt.show()
print(f"the exam fortnight over the fortnight before: {exam[0]:.2f} and {exam[1]:.2f}")
print(f"Diwali week over the fortnight before: {diwali[0]:.2f} and {diwali[1]:.2f}")
check("the exam fortnight is about 1.4 times an ordinary fortnight, both years", all(abs(r - 1.4) < 0.1 for r in exam))
check("Diwali week is about 0.4 times an ordinary fortnight, both years", all(abs(r - 0.4) < 0.1 for r in diwali))
'''),
        md("""
        **What happened.** Diwali week is a dip, about 0.4 of an ordinary week in both years (0.40
        and 0.40), and the exam fortnight a peak, about 1.4 (1.39 and 1.41). A season repeats on a
        fixed beat, up or down, so seasonal never means only a spike. Diwali's dip also lands a
        week earlier in 2025, since the festival came eleven days earlier in the calendar, which
        notebook 02 will need.

        Named last: a series is a **trend** times its **seasons** times a **remainder**, what is
        left over. Forecasting: Principles and Practice writes the parts as a sum, y = T + S + R,
        when the seasons keep their size as the level grows, and as a product when they grow with
        it, as the stall's do (section 3.2, checked 13 October 2026). A **cycle**, a rise and fall
        with no fixed length, needs more than two years to see.

        ## What is left over?

        Copy each day of the second year from the same weekday 364 days back, times 1.10 for the
        year's growth; what the copy misses is the remainder. The fortnight Diwali moved into is
        set aside, because there the copy lands the festival on the wrong days.
        """),
        code('''
cups = stall.set_index("date").cups
year2 = cups[cups.index >= "2025-09-29"]                             # the second year
left = year2 - cups.shift(364).loc[year2.index] * 1.10               # what the trend and the beats leave
moved = (left.index >= "2025-10-20") & (left.index < "2025-11-03")   # the fortnight Diwali moved into
rest = left[~moved]
fig, ax = plt.subplots()
ax.hist(rest, bins=20, color="lavender", edgecolor="slateblue")
ax.set_xlabel("cups left over: sold minus (the same day last year x 1.10)")
ax.set_ylabel("days")
ax.set_title("What is left after the trend and the beats, Diwali's fortnight aside (invented)")
plt.show()
print(f"{len(rest)} days: mean {rest.mean():.1f} cups, spread {rest.std():.1f} cups either way")
print(f"in the fortnight Diwali moved into, the worst day is {left[moved].abs().max():.0f} cups off")
check("what is left has a mean near zero", abs(rest.mean()) < 1)
check("what is left wobbles by a few cups", rest.std() < 6)
'''),
        md("""
        **The plausible wrong answer.** "Monday sold 100 and Sunday 60, so the stall (invented) is
        up 67 percent." **The decision it misleads:** two-thirds more milk ordered, which sours.
        **The check:** the same point a season apart, Monday against the Monday before (100
        against 100) or against the same Monday a year earlier (110 against 100). **The fix:** read
        the beat first; the stall grows 10 percent a year, and this week it grew nothing.

        The remainder shows the next trap. Inside the fortnight Diwali moved into, the copy of the
        same weekday a year back misses by up to 70 cups, because the festival came eleven days
        earlier in 2025. Notebook 02 copies by distance from the festival instead.
        """),
        md("""
        **Your turn.** Read the Sundays a season apart with `season_apart`. In the table at the top,
        row 6 is Sunday 6 October 2024 and its 2025 twin sits in the same row. Fill the blanks, type
        the lines into the empty cell below and run them; the check prints PASS when the reading is
        right.

        ```python
        sunday_then = two.cups_2024[6]          # Sunday 6 October 2024 (invented)
        sunday_now = two.cups_2025[___]         # the same Sunday, 52 weeks later
        growth = season_apart(___, ___)
        check("Sundays grew about 10 percent a year", round(growth, 2) == 0.10)
        ```
        """),
        empty(),
        md("""
        ## Which rules does the chapter leave?

        1. Read the series' shape before choosing any rule that copies it.
        2. A season repeats on a fixed beat, up or down, so count its length before using it.
        3. Read growth by comparing the same point a season apart, never neighbours.
        4. What is left after the trend and the seasons is the remainder, and a cycle needs years
           to see.

        **In the interview.** "Before any model I plot the series and read its trend, its seasons
        with their lengths, and what is left, because the baseline I must beat depends on them."
        """),
        code('''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
y = weekly.set_index("week_start").shipments                   # Flipkart Lucknow, the case's 104 weeks
growth = season_apart(y.iloc[52:91].sum(), y.iloc[:39].sum())    # the latest 39 training weeks against a year earlier
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.plot(y.index, y.values, color="slateblue")
for d in ["2024-10-28", "2025-10-20"]:
    ax.axvline(pd.Timestamp(d), color="crimson", ls="--")
ax.set_ylabel("shipments in the week")
ax.set_title("Flipkart Lucknow (illustrative; synthetic data): dashed, the weeks holding Diwali")
plt.show()
print(f"{len(y)} weeks; growth a season apart on the latest 39 training weeks: {growth:.1%}")
check("Flipkart's weeks grow about 4 percent a year", round(growth, 2) == 0.04)
'''),
        md("""
        ## What did the chapter answer?

        | Question | The stall's answer, in invented numbers |
        |---|---|
        | What repeats, and how often? | A Sunday dip every 7 days: Sunday sells 0.6 of a Monday |
        | Is the stall growing? | By 10 percent a year, read a season apart; Monday's 67 percent over Sunday is the beat |
        | What repeats once a year? | The exam fortnight, about 1.4 times an ordinary one, and Diwali week, about 0.4 |
        | What is left over? | A wobble of 4.7 cups either way, except where the festival moved: up to 70 |

        Flipkart's 104 weeks read the same way: a level near 210,000 shipments a week, growth of
        about 4 percent a year and a festive peak each year. Chapter 5's notebook,
        `C2_W04_D05_05_case_shape_and_baselines_STUDENT.ipynb`, applies this reading to them;
        notebook 02 copies the stall's past three ways.
        """),
    ]


def nb02():
    return [
        md(f"""
        # Naive, seasonal naive and drift baselines: what does each copy, and when does the copy fail?

        **Week 4, Friday, concept notebook 2 of 4, beside chapter 2 of the deck.** {STALL} Notebook
        01 found its weekly beat of 7 days and its growth of 10 percent a year.

        **Who needs the answer.** The stall's owner (invented), who needs a rule a person can run on
        paper before any spreadsheet opens, and Flipkart's FC planner, whose house bot is one of
        these rules.

        **The questions on the way.** What does each rule copy? Which wins next Sunday? What does a
        yearly copy miss? What breaks when the festival moves? Where does drift do its job?
        """),
        code(SETUP + '''
# eight days of the invented stall, Sunday 12 to Sunday 19 January 2025
week = pd.read_csv("../data/C2_W04_D05_chai_stall_week_STUDENT.csv")
check("eight days, Sunday to Sunday", len(week) == 8 and week.weekday.iloc[0] == week.weekday.iloc[-1] == "Sun")
week                                          # every number invented
'''),
        md("""
        ## What does each rule copy?

        A **baseline** is the simplest rule that could be right, and its job is to be beaten: any
        cleverer forecast must do better than it. Three rules copy the past in three ways, each
        one line of arithmetic. Stand on Saturday 18 January and forecast Sunday 19 January, by
        hand first:

        - **Naive** repeats the last day: 103.
        - **Drift** takes the last value and adds the average step so far, here over the last four
          days, 98, 104, 101 and 103: 103 + (103 - 98) / 3, about 104.7.
        - **Seasonal naive** copies the value one season back. The beat is 7 days, so next Sunday
          copies last Sunday: 61.

        **Predict before you run.** Which rule lands nearest next Sunday's cups?

        a) Naive, 103
        b) Drift, about 105
        c) Seasonal naive, 61
        d) All three land within five cups of each other
        """),
        code('''
def naive(history):
    return history[-1]                                        # the last value

def seasonal_naive(history, m):
    return history[-m]                                        # the value one season of m periods back

def drift(history, h=1):
    step = (history[-1] - history[0]) / (len(history) - 1)    # the average step so far
    return history[-1] + h * step                             # the line, extended h periods

seen, actual = week.cups.iloc[:7].tolist(), week.cups.iloc[-1]    # Sun 12 to Sat 18 Jan, and Sun 19 Jan
forecasts = {"naive": naive(seen), "drift": drift(seen[-4:]), "seasonal naive": seasonal_naive(seen, 7)}
for name, f in forecasts.items():
    print(f"{name}: {round(f, 1)}, miss {round(f - actual, 1):+}")
fig, ax = plt.subplots()
ax.bar(range(8), week.cups, color=["lavender"] * 7 + ["white"], edgecolor="slateblue")
for (name, f), mark, at in zip(forecasts.items(), ["o", "D", "s"], [6.8, 7.0, 7.2]):
    ax.plot(at, f, marker=mark, ls="", markersize=9, label=f"{name}: {round(f, 1)}")
ax.set_xticks(range(8), week.weekday + " " + week.date.str[8:])
ax.set_ylim(0, 140)
ax.set_ylabel("cups sold")
ax.set_title(f"Next Sunday from three rules (invented numbers): it sold {actual}")
ax.legend(ncol=3, loc="upper left")
plt.show()
check("by hand and by code, naive says 103", naive(seen) == 103)
check("by hand and by code, drift says about 104.7", round(drift(seen[-4:]), 1) == round(103 + (103 - 98) / 3, 1))
check("the seasonal naive copies last Sunday", seasonal_naive(seen, 7) == seen[0])
check("the seasonal naive lands nearest", min(forecasts, key=lambda k: abs(forecasts[k] - actual)) == "seasonal naive")
'''),
        md("""
        **What happened.** The answer is c. Next Sunday sold 60: naive said 103 and missed by 43,
        drift said 104.7 and missed by 44.7, and the seasonal naive said 61 and missed by 1. When a
        beat is strong, the plainest copy that respects it wins.

        Named last, as Forecasting: Principles and Practice writes them (section 5.2, checked 13
        October 2026), with T the last period a rule may see, h the periods ahead and m the
        season's length:

        - naive: forecast(T + h) = y(T), the last value;
        - seasonal naive: forecast(T + h) = y(T + h - m), the value one season back, for h up to m;
        - drift: forecast(T + h) = y(T) + h x (y(T) - y(1)) / (T - 1), the line from the first
          value to the last, extended.

        ## What does a yearly copy miss?

        The stall (invented) has a yearly beat too. The November exam fortnight began on Wednesday
        27 November 2024 at 140 cups and on Wednesday 26 November 2025 at 154. Stand on Tuesday 25
        November 2025, which sold 110. Naive copies it and falls 44 cups short on the first exam
        day. The yearly copy, the same weekday 364 days back, says 140 and falls 14 short, the
        year's growth; times 1.10 it says 154.
        """),
        code('''
stall = pd.read_csv("../data/C2_W04_D05_chai_stall_daily_STUDENT.csv", parse_dates=["date"])
cups = stall.set_index("date").cups
days = pd.date_range("2025-11-12", periods=28)              # the fortnight before the exams, and the exams
rules = pd.DataFrame({"naive: yesterday": cups.shift(1).loc[days],
                      "yearly copy, 364 days back": cups.shift(364).loc[days],
                      "yearly copy x 1.10": (cups.shift(364) * 1.10).round().loc[days]})
mae = {name: (rules[name] - cups.loc[days]).abs().mean() for name in rules}
fig, axes = plt.subplots(1, 3, figsize=(13, 3.6), sharey=True, constrained_layout=True)
for ax, name in zip(axes, rules):
    ax.plot(range(1, 29), cups.loc[days].values, color="black", label="sold")
    ax.plot(range(1, 29), rules[name].values, color="crimson", ls="--", label="forecast")
    ax.axvline(15, color="grey", lw=1)                         # day 15: the first exam day, 26 November
    ax.set_title(f"{name}\\naverage miss {mae[name]:.1f} cups")
    ax.set_xlabel("day, from 12 November 2025")
axes[0].legend(loc="lower right")
fig.suptitle("The November 2025 exam fortnight under three rules (invented numbers); grey: the first exam day")
plt.show()
first = pd.Timestamp("2025-11-26")
print("first exam day sold", cups[first], "; naive said", int(rules.loc[first].iloc[0]),
      "; the yearly copy", int(rules.loc[first].iloc[1]), "; with growth", int(rules.loc[first].iloc[2]))
print("average miss over the 28 days, cups: " + "; ".join(f"{name} {m:.1f}" for name, m in mae.items()))
check("naive falls more than 30 cups short on the first exam day", cups[first] - rules.loc[first].iloc[0] > 30)
check("the yearly copy with growth lands within 2 cups", abs(rules.loc[first].iloc[2] - cups[first]) <= 2)
'''),
        md("""
        **What happened.** Across the 28 days naive misses by 20.6 cups a day, since it copies an
        ordinary day into the first exam day; the yearly copy misses by 10.5, the year's growth;
        the yearly copy times 1.10 by 3.0. The copy reaches 364 days back, never a calendar year of
        days, because 364 is 52 whole weeks: a Wednesday lands on a Wednesday and the weekly beat
        stays in step. Finance's habit at Flipkart, "last year plus 4 percent", is this rule: the
        seasonal naive times a growth factor, read as notebook 01 reads trend.

        ## What breaks when the festival moves?

        **The plausible wrong answer.** "The yearly copy knows the season, so it is the safe rule
        for Diwali." Diwali came eleven days earlier in 2025, on Monday 20 October against
        Thursday 31 October 2024. The copy for Monday 20 October 2025 reads Monday 21 October 2024,
        an ordinary day of 100 cups; the copy for Thursday 30 October 2025 reads Thursday 31
        October 2024, Diwali day, 40 cups.
        """),
        code('''
def festival_aligned(cups, day, festival_week, gap, reach=14):
    """Near the festival, copy the day at the same distance from last year's festival week;
    elsewhere, the same weekday 364 days back."""
    near = festival_week - pd.Timedelta(days=reach) <= day < festival_week + pd.Timedelta(days=7 + reach)
    return cups[day - pd.Timedelta(days=gap if near else 364)]

week_now, week_then = pd.Timestamp("2025-10-20"), pd.Timestamp("2024-10-28")   # the Mondays of the weeks holding Diwali
gap = (week_now - week_then).days                                                # 357 days, 51 weeks
days = pd.date_range("2025-10-13", periods=21)                                   # the three weeks around Diwali's week
calendar = cups.shift(364).loc[days] - cups.loc[days]                            # the calendar copy's misses
aligned = pd.Series([festival_aligned(cups, d, week_now, gap) for d in days], index=days) - cups.loc[days]
fig, axes = plt.subplots(1, 2, figsize=(12, 3.8), sharey=True, constrained_layout=True)
for ax, (name, miss) in zip(axes, [("calendar copy, 364 days back", calendar), (f"festival-aligned, {gap} days back", aligned)]):
    ax.plot(days, cups.loc[days], color="black", marker="o", label="sold")
    ax.plot(days, cups.loc[days] + miss, color="crimson", ls="--", marker="s", label="the copy")
    ax.axvspan(week_now, week_now + pd.Timedelta(days=6), color="plum", alpha=0.3)
    ax.set_title(f"{name}\\nworst miss {miss.abs().max():.0f} cups")
    ax.set_xticks(days[::4], days[::4].strftime("%d %b"))
axes[0].legend(loc="lower left")
fig.suptitle("Diwali came eleven days earlier in 2025 (invented numbers); shaded, the week holding it")
plt.show()
print(f"Diwali 2025, Monday 20 October: sold {cups['2025-10-20']}, the calendar copy said {cups['2024-10-21']}")
print(f"the calendar copy: worst miss {calendar.abs().max():.0f} cups, average {calendar.abs().mean():.1f}")
print(f"festival-aligned: worst miss {aligned.abs().max():.0f} cups, average {aligned.abs().mean():.1f}")
check("the calendar copy misses the moved festival by more than 50 cups", calendar.abs().max() > 50)
check("festival-aligned misses by less than 15", aligned.abs().max() < 15)
'''),
        md("""
        **Why it is wrong.** The calendar copy misses by up to 71 cups, 41.1 a day on average
        across the three weeks around Diwali's week; the festival-aligned copy by at most 13 and 6.5
        on average. **The decision it misleads:** milk 70 cups short on 30 October and 56 cups too
        much on Diwali itself, which sours. **The check:** the calendar. **The fix:** near the
        festival, copy the day at the same distance from last year's festival, 357 days back here,
        since Diwali's week came 51 weeks after 2024's. The fix is this programme's own extension of
        the seasonal naive, which it calls **festival-aligned**; away from the festival it is the
        plain seasonal naive.

        ## Where does drift do its job?

        Drift draws the line from the first value to the last and extends it, so it suits a plain
        climb with no beat. The stall's weekly totals (invented) carry no weekly beat, since each
        total holds one of every weekday.
        """),
        code('''
start = pd.Timestamp("2024-12-30")                                    # a Monday in an ordinary stretch
totals = [int(cups.loc[start + pd.Timedelta(weeks=w):start + pd.Timedelta(weeks=w, days=6)].sum()) for w in range(13)]
history, week13 = totals[:12], totals[12]
by_hand = history[-1] + (history[-1] - history[0]) / 11
fig, ax = plt.subplots()
ax.plot(range(1, 13), history, marker="o", color="slateblue", label="twelve weekly totals")
ax.plot([1, 13], [history[0], drift(history)], ls="--", color="goldenrod", label="drift's line, extended")
ax.plot(13, week13, marker="s", color="black", ls="", label="what week 13 sold")
ax.set_xlabel("week, from Monday 30 December 2024")
ax.set_ylabel("cups in the week")
ax.set_title("Drift on the stall's weekly totals (invented numbers)")
ax.legend()
plt.show()
print("weekly totals:", history)
print(f"drift's step: {(history[-1] - history[0]) / 11:.1f} a week; week 13: forecast {drift(history):.0f}, sold {week13}")
check("by hand and by code, drift says 686 for week 13", round(drift(history)) == round(by_hand) == 686)
'''),
        md("""
        **Your turn.** Forecast Monday 20 January 2025, the day after next Sunday, with two of the
        rules. The eight rows of `week` run from Sunday 12 to Sunday 19 January (invented). Fill the
        blanks, type the lines into the empty cell below and run them; the checks print PASS when
        both forecasts are right, and the misses show which rule respects the beat.

        ```python
        eight = week.cups.tolist()                    # Sunday 12 to Sunday 19 January
        monday = cups["2025-01-20"]                   # what Monday 20 January sold
        by_naive = naive(___)
        by_season = seasonal_naive(___, 7)
        print("naive misses by", by_naive - monday, "and the seasonal naive by", by_season - monday)
        check("naive copies Sunday's 60 into Monday", by_naive == 60)
        check("the seasonal naive copies last Monday's 103", by_season == 103)
        ```
        """),
        empty(),
        md("""
        ## Which rules does the chapter leave?

        1. A baseline is the simplest rule that could be right, and every forecast must beat it.
        2. Naive repeats the last value, the seasonal naive the value one season back, and drift
           extends the line from the first value to the last.
        3. When a beat is strong, the copy that respects it wins, and a yearly copy needs the year's
           growth added.
        4. A festival that moves breaks every calendar copy, so copy by distance from the festival.

        **In the interview.** "Naive, seasonal naive and drift are the baselines any forecast must
        beat, and on seasonal data the seasonal naive is the one to beat."
        """),
        code('''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
y = weekly.set_index("week_start").shipments                    # Flipkart Lucknow, the case's 104 weeks
train = y.iloc[:91]                                             # the weeks before chapter 6's hidden weeks
house_bot = y.shift(52)                                         # the seasonal naive with m = 52: the house bot
print(pd.DataFrame({"shipments": y, "seasonal naive, same week last year": house_bot}).iloc[52:55].to_string())
step = (train.iloc[-1] - train.iloc[0]) / (len(train) - 1)
print(f"drift's step on the 91 training weeks: {step:.0f} shipments a week")
check("drift's step is about 70 shipments a week", round(step) == 70)
check("the house bot holds the week 52 rows up", house_bot.iloc[52] == y.iloc[0])
'''),
        md("""
        ## What did the chapter answer?

        | Question | The stall's answer, in invented numbers |
        |---|---|
        | What does each rule copy? | Naive the last value, 103; drift the line extended, 104.7; the seasonal naive last Sunday, 61 |
        | Which wins next Sunday? | The seasonal naive, a miss of 1 cup against 43 and 44.7 |
        | What does a yearly copy miss? | The year's growth: 10.5 cups a day around the exams, 3.0 once it is times 1.10 |
        | What breaks when the festival moves? | The calendar copy, by up to 71 cups; festival-aligned misses by at most 13 |
        | Where does drift do its job? | On a plain climb: 686 for week 13 against 688 sold |

        At Flipkart the seasonal naive with m = 52 is "the same week last year", which the
        tournament calls the house bot; finance's rule is the house bot times 1.04; drift's step is
        about 70 shipments a week. Chapter 5's notebook,
        `C2_W04_D05_05_case_shape_and_baselines_STUDENT.ipynb`, runs these rules on Diwali 2025's
        week; notebook 03 scores a rule on days it never saw.
        """),
    ]


def nb03():
    return [
        md(f"""
        # Holding out; MAE and MAPE in the business's units: how is a forecast scored honestly, in cups and in rupees?

        **Week 4, Friday, concept notebook 3 of 4, beside chapter 3 of the deck.** {STALL} Notebook
        02 built three copy rules; this notebook scores a rule on days it never saw.

        **Who needs the answer.** The stall's owner (invented), who wants to know how wrong the milk
        order could be before trusting a rule, and Flipkart's regional operations head, who must
        say yes or no to a vendor's curve before a shift is booked.

        **The questions on the way.** Which days do we hide? How is a miss counted? When does a
        percent mislead? Which way is the rule wrong, and what does that cost?
        """),
        code(SETUP + '''
# fourteen days of the invented stall, Saturday 1 to Friday 14 February 2025; the last three are hidden
days = pd.read_csv("../data/C2_W04_D05_chai_stall_hidden_days_STUDENT.csv")
unsold_rs, short_rs = 6, 12      # a cup unsold wastes Rs 6 of milk; a cup short loses Rs 12 of margin (invented)
check("fourteen days, the last three hidden", len(days) == 14 and days.hidden.tolist() == [0] * 11 + [1] * 3)
days                             # every number invented
'''),
        md("""
        ## Which days do we hide?

        The owner orders milk for the next three days. To judge a rule, hide some days, forecast
        them as if each were tomorrow, and count the misses.

        **Predict before you run.** To judge a three-day milk order, which three of the fourteen
        days do you hide?

        a) The last three: days 12, 13 and 14
        b) Three days at random, so any weekday may be tested
        c) The three busiest, since they cost the most
        d) Any three; it makes no difference which
        """),
        code('''
train, hidden = days[days.hidden == 0], days[days.hidden == 1]
origin = int(train.cups.iloc[-1])                         # day 11, the last day a rule may see
forecast = [origin] * len(hidden)                         # naive: day 11 repeated for each hidden day
fig, ax = plt.subplots()
ax.bar(days.day, days.cups, color=["lavender"] * len(train) + ["plum"] * len(hidden), edgecolor="slateblue")
ax.plot(hidden.day, forecast, color="crimson", ls="--", marker="o", label="naive, made from day 11")
ax.set_xticks(days.day, days.day.astype(str) + " " + days.weekday, rotation=60)
ax.set_ylim(0, 135)
ax.set_ylabel("cups sold")
ax.set_title("Fourteen days, the last three hidden (invented numbers)")
ax.legend(loc="upper left")
plt.show()
print(f"training days: {len(train)}; hidden days: {len(hidden)}, which sold {hidden.cups.tolist()}; "
      f"naive says {origin} for each")
check("the hidden days are the latest", hidden.day.min() > train.day.max())
check("as many hidden days as the order reaches ahead", len(hidden) == 3)
'''),
        md("""
        **What happened.** The answer is a. Hide the latest days, at least as many as the forecast
        must reach ahead: three here. Day 11 is the **origin**, the last day a rule may see; three
        days ahead is the **horizon**; days 1 to 11 are the **training** days and days 12 to 14 the
        **hidden** days, also called the hold-out or the test set. Tomorrow looks most like the
        newest days, and a random hole would let a rule borrow days that come after the one it
        forecasts, which a real tomorrow never offers. The test set should be "at least as large
        as the maximum forecast horizon required" (Forecasting: Principles and Practice, section
        5.8, checked 13 October 2026).

        ## How is a miss counted?

        By hand first. Naive says 100 for each hidden day, and days 12 to 14 sold 110, 95 and 100.
        A **miss** here is the forecast minus what sold, so a positive miss is cups unsold and a
        negative one cups short: -10, +5 and 0.

        - **MAE**, the mean absolute error, drops the signs and averages: (10 + 5 + 0) / 3 = 5.0
          cups.
        - **MAPE**, the mean absolute percentage error, divides each miss by what sold before
          averaging: (10/110 + 5/95 + 0/100) / 3, about 4.8 percent.
        - **The lean** keeps the signs: (-10 + 5 + 0) / 3, about -1.7 cups, so the rule runs low.
        - **In rupees:** 10 cups short at Rs 12 and 5 unsold at Rs 6, Rs 120 + Rs 30 = Rs 150.

        Forecasting: Principles and Practice writes the error the other way round, sold minus
        forecast, so its signs flip and its sizes stay the same.
        """),
        code('''
def mae(misses):
    return sum(abs(m) for m in misses) / len(misses)                      # sizes, signs dropped, averaged

def mape(misses, sold):
    return sum(abs(m) / s for m, s in zip(misses, sold)) / len(misses)    # each miss over what sold

def lean(misses):
    return sum(misses) / len(misses)                                      # signs kept: below zero runs low

def rupees(misses):
    return sum(m * unsold_rs if m > 0 else -m * short_rs for m in misses)  # unsold at Rs 6, short at Rs 12

sold = [int(s) for s in hidden.cups]
misses = [f - s for f, s in zip(forecast, sold)]
print(f"misses {misses}: MAE {mae(misses):.1f} cups, MAPE {mape(misses, sold):.1%}, "
      f"lean {lean(misses):+.1f} cups, cost Rs {rupees(misses)}")
check("by hand and by code, MAE is 5.0 cups", mae(misses) == (10 + 5 + 0) / 3)
check("by hand and by code, MAPE is about 4.8 percent", round(mape(misses, sold), 4) == round((10 / 110 + 5 / 95 + 0 / 100) / 3, 4))
check("the rule runs low, and its misses cost Rs 150", lean(misses) < 0 and rupees(misses) == 10 * 12 + 5 * 6)
'''),
        md("""
        **What happened.** Both scores, named last: MAE is the mean of the misses' sizes, in the
        unit the cost is counted in, cups here; MAPE is the mean of each miss's size over what
        sold, in percent, which lets you compare stalls of different sizes. A percent cannot be
        priced, which is why the owner's score is the MAE, priced in rupees.

        ## When does a percent mislead?

        **Predict before you run.** Two invented days, apart from the stall's record: an ordinary
        day forecast at 100 that sold 85, and a rain day, the stall shut after an hour, forecast at
        20 that sold 5. Each misses by 15 cups. What percent miss does the rain day score?
        """),
        code('''
what_if = pd.read_csv("../data/C2_W04_D05_chai_stall_what_ifs_STUDENT.csv")   # invented what-ifs
pair = what_if[what_if.example == "mape"]
print(pair.to_string(index=False))
miss = (pair.forecast - pair.sold).tolist()
pct = [abs(m) / s for m, s in zip(miss, pair.sold)]
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), constrained_layout=True)
for ax, values, title in [(axes[0], [abs(m) for m in miss], "the miss in cups"),
                          (axes[1], [p * 100 for p in pct], "the miss in percent of what sold")]:
    ax.bar(["ordinary day", "rain day"], values, color=["lavender", "crimson"], edgecolor="slateblue")
    ax.set_title(title)
fig.suptitle("The same 15-cup miss, two ways (invented numbers): MAE treats the days alike, MAPE does not")
plt.show()
print(f"MAE {mae(miss):.0f} cups; percent misses {pct[0]:.1%} and {pct[1]:.0%}; MAPE {mape(miss, pair.sold.tolist()):.1%}")
check("both days miss by the same 15 cups", abs(miss[0]) == abs(miss[1]) == 15)
check("the rain day's percent swamps the ordinary day's", pct[1] > 10 * pct[0])
'''),
        md("""
        **What happened.** The rain day scores 300 percent and the ordinary day 17.6 percent, so
        their MAPE is 158.8 percent while their MAE stays 15 cups. MAPE divides by what sold, so a
        day that sells close to zero swamps it: percentage errors are "infinite or undefined if
        y_t = 0" and take "extreme values if any y_t is close to zero" (Forecasting: Principles and
        Practice, section 5.8, checked 13 October 2026). Keep MAE for the order and MAPE for
        comparing stalls of different sizes, on periods that never sell close to zero.

        ## Which way is the rule wrong, and what does that cost?

        **Predict before you run.** Two rules each miss two days by 10 cups. Rule P runs over on
        both days (+10, +10); rule Q runs over, then short (+10, -10). Both score an MAE of 10.
        Which costs more, at Rs 6 a cup unsold and Rs 12 a cup short?
        """),
        code('''
rows = []
for name in ["rule P", "rule Q"]:
    r = what_if[what_if.example == name]
    m = (r.forecast - r.sold).tolist()
    rows.append({"rule": name, "misses": m, "MAE": mae(m), "lean": lean(m), "cost Rs": rupees(m)})
table = pd.DataFrame(rows).set_index("rule")
print(table.to_string())
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6), sharey=True, constrained_layout=True)
for ax, (name, row) in zip(axes, table.iterrows()):
    ax.bar(["day 1", "day 2"], row.misses, color=["crimson" if m < 0 else "plum" for m in row.misses])
    ax.axhline(0, color="black", lw=1)
    ax.set_title(f"{name}: MAE {row.MAE:.0f}, costs Rs {row['cost Rs']}")
axes[0].set_ylabel("forecast minus sold, cups")
fig.suptitle("Same MAE, different rupees (invented numbers): short costs Rs 12 a cup, unsold Rs 6")
plt.show()
check("both rules share an MAE of 10", table.MAE.tolist() == [10, 10])
check("rule P costs Rs 120 and rule Q Rs 180", table["cost Rs"].tolist() == [120, 180])
'''),
        md("""
        **What happened.** Rule Q costs more. Rule P, always over, wastes 20 cups of milk at Rs 6:
        Rs 120. Rule Q runs short on day 2, and a cup short costs Rs 12: Rs 60 + Rs 120 = Rs 180.

        **The plausible wrong answer.** "Both rules score MAE 10, so they are equally good." **The
        decision it misleads:** milk ordered at the forecast when the misses run short. **The
        check:** the sign of each miss, the lean. **The fix:** report the MAE and the lean together,
        and price each direction.
        """),
        md("""
        **Your turn.** Score the seasonal naive on the same three hidden days. With a beat of 7 days
        it copies days 5, 6 and 7, the same weekdays a week before days 12, 13 and 14. Fill the
        blanks, type the lines into the empty cell below and run them; the checks print PASS when
        the scores are right.

        ```python
        week_back = days.cups.iloc[4:7].tolist()          # days 5 to 7 (invented)
        misses = [f - s for f, s in zip(___, sold)]
        print(misses, mae(misses), lean(misses), rupees(misses))
        check("the seasonal naive's MAE is about 5.7 cups", round(mae(___), 1) == 5.7)
        check("its misses cost Rs 138", rupees(___) == 138)
        ```

        Then compare it with naive's 5.0 cups: which rule scores better on these three days, and
        why can the weekly beat add nothing when no Sunday sits among the hidden days?
        """),
        empty(),
        md("""
        ## Which rules does the chapter leave?

        1. Hide the latest periods, at least as many as the forecast must reach ahead, and forecast
           them all from one origin.
        2. Fix the measure before anyone scores, in the unit the cost is in.
        3. Keep MAPE for comparing series of different sizes, and never on periods that sell close
           to zero.
        4. Report which way a rule leans beside how far it misses, because a miss short and a miss
           over cost different amounts.

        **In the interview.** [S] "How do you evaluate a forecast?" A hire-grade answer holds four
        moves: hold out the latest periods, as many as the horizon; fix the error measure in the
        business's unit before scoring; compare with the naive and the seasonal naive; price each
        direction of the miss.
        """),
        code('''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
costs = pd.read_csv("../data/C2_W04_D05_costs_STUDENT.csv").set_index("item").rs
y = weekly.set_index("week_start").shipments                    # Flipkart Lucknow, the case's 104 weeks
train, held = y.iloc[:91], y.iloc[91:]                          # the training weeks, and the hidden ones
fig, ax = plt.subplots(figsize=(10, 3.4))
ax.plot(y.index, y.values, color="slateblue")
ax.axvspan(held.index[0], held.index[-1], color="plum", alpha=0.3)
ax.set_ylabel("shipments in the week")
ax.set_title("Flipkart Lucknow (illustrative; synthetic data): the last thirteen weeks hidden")
plt.show()
print(f"hidden: {held.index[0].date()} to {held.index[-1].date()}; origin: {train.index[-1].date()}")
print(f"a spare shipment costs Rs {costs['idle_packer_shift'] / 120:.2f} and a late one Rs {costs['late_shipment']}")
check("thirteen hidden weeks, the latest", len(held) == 13 and held.index[-1] == y.index[-1])
check("the hidden weeks cover the plan's ten-week horizon", len(held) >= 10)
'''),
        md("""
        ## What did the chapter answer?

        | Question | The stall's answer, in invented numbers |
        |---|---|
        | Which days do we hide? | The latest three, as many as the order reaches ahead, all forecast from day 11 |
        | How is a miss counted? | MAE 5.0 cups; MAPE about 4.8 percent |
        | When does a percent mislead? | On a day that sells close to zero: 300 percent for a 15-cup miss |
        | Which way is the rule wrong, and what does that cost? | Low, by 1.7 cups a day; Rs 150 over the three days, and the same MAE can cost Rs 120 or Rs 180 |

        At Flipkart the latest thirteen weeks, 29 June to 21 September 2026, are hidden, the origin
        is the week of 22 June and the horizon ten weeks; a spare shipment costs Rs 5.42 and a late
        one Rs 25. Chapter 6's notebook, `C2_W04_D05_06_case_holdout_scoreboard_STUDENT.ipynb`,
        scores every rule and the vendor's curve there; notebook 04 asks when a forecast earns
        trust.
        """),
    ]


def nb04():
    return [
        md(f"""
        # Beating the baseline; the vendor curve tested; the good-enough call and the forecast note: when does a forecast earn trust, and what do you send?

        **Week 4, Friday, concept notebook 4 of 4, beside chapter 4 of the deck.** {STALL} Notebook
        03 fixed how a rule is scored: on hidden days, in cups and in rupees.

        **Who needs the answer.** The stall's owner (invented), offered a "model" by a nephew with a
        laptop, and Flipkart's regional operations head, offered a vendor's curve that fits history
        within 2 percent.

        **The questions on the way.** What does a perfect fit say about tomorrow? Does the clever
        rule beat the baseline? Is a better forecast worth having? What goes to the milkman?
        """),
        code(SETUP + '''
# fourteen days of the invented stall, Monday 3 to Sunday 16 March 2025; the last seven are hidden
days = pd.read_csv("../data/C2_W04_D05_chai_stall_nephew_STUDENT.csv")
can = 40                          # cups of tea one milk can makes (invented)
unsold_rs, short_rs = 6, 12       # Rs a cup unsold, Rs a cup short (invented)
check("fourteen days, the last seven hidden", len(days) == 14 and days.hidden.sum() == 7)
days                              # every number invented
'''),
        md("""
        ## What does a perfect fit say about tomorrow?

        **Fit** is how close a rule sits to the days it was built on; **forecast error** is how far
        it misses days it never saw. The nephew's first offer is a curve through the first four
        days, 100, 104, 98 and 110 cups, which passes through every one of them exactly.

        **Predict before you run.** Which forecast for day 5 lands closest?

        a) The straight line: the best line through the four days, about 109
        b) The exact curve: it passes through all four days exactly
        c) Naive: repeat the last day, 110
        d) They land within five cups of each other
        """),
        code('''
four, day5 = days.cups.iloc[:4].tolist(), days.cups.iloc[4]
x = [1, 2, 3, 4]

def line_through(values):
    """The least-squares straight line through the days: its slope and its value at day 0."""
    xm, ym = sum(x) / len(x), sum(values) / len(values)
    slope = sum((a - xm) * (b - ym) for a, b in zip(x, values)) / sum((a - xm) ** 2 for a in x)
    return slope, ym - slope * xm

def curve_at(t, values):
    """The one curve that passes through every day exactly, read at day t."""
    total = 0
    for i, v in zip(x, values):
        term = v
        for j in x:
            if j != i:
                term *= (t - j) / (i - j)
        total += term
    return total

slope, start = line_through(four)
line5, curve5 = start + slope * 5, curve_at(5, four)
line_fit = sum(abs(start + slope * a - b) for a, b in zip(x, four)) / len(x)
curve_fit = sum(abs(curve_at(a, four) - b) for a, b in zip(x, four)) / len(x)
grid = [1 + k / 20 for k in range(81)]                       # day 1 to day 5 in small steps
fig, ax = plt.subplots()
ax.plot(grid, [curve_at(t, four) for t in grid], color="crimson", label="the curve through all four days")
ax.plot([1, 5], [start + slope, line5], color="slateblue", ls="--", label="the straight line")
ax.plot(x, four, "o", color="black", label="the four days the rules saw")
ax.plot(5, day5, "s", color="seagreen", markersize=9, label="day 5, what sold")
ax.set_xlabel("day")
ax.set_ylabel("cups")
ax.set_title("A perfect fit on four days, and its forecast for day 5 (invented numbers)")
ax.legend()
plt.show()
print(f"the line: slope {slope:.1f}, value at day 0 {start:.0f}, {line_fit:.1f} cups from the four days on average; day 5: {line5:.0f}")
print(f"the curve: {curve_fit:.0f} cups from the four days; day 5: {curve5:.0f}")
print(f"day 5 sold {day5}: the line misses by {abs(line5 - day5):.0f}, the curve by {abs(curve5 - day5):.0f}, naive by {abs(four[-1] - day5)}")
check("by hand and by code, the curve says 168", round(curve5) == 110 + 12 + 18 + 28)
check("the curve fits the four days exactly", curve_fit < 1e-9)
check("its forecast misses day 5 by more than 50", abs(curve5 - day5) > 50)
check("the line, which fits worse, misses by less than 10", abs(line5 - day5) < 10)
'''),
        md("""
        **What happened.** The answer is a, with naive a cup behind. Day 5 sold 102. The curve
        through all four days fits them perfectly, with an error of 0, and said 168: a miss of 66,
        the worst in the room. The straight line sits about 3.1 cups from the four days on average,
        said 109 and missed by 7; naive said 110 and missed by 8. The curve's 168 needs no algebra:
        the four days' differences are 4, -6 and 12, their differences -10 and 18, and theirs 28;
        carry each last difference down and the curve climbs to 110 + 12 + 18 + 28 = 168. An
        interviewer calls fit in-sample and forecast error out-of-sample: "A model which fits the
        training data well will not necessarily forecast well" (Forecasting: Principles and
        Practice, section 5.8, checked 13 October 2026).

        ## Does the clever rule beat the baseline?

        The nephew's second offer is the mean of the last seven days, 97.6 cups every day. Score
        it against the seasonal naive, the same day last week, on the seven hidden days, 10 to 16
        March, by the measure notebook 03 fixed.

        **Predict before you run.** Which rule scores the lower MAE on the hidden days, and by how
        much?
        """),
        code('''
seen, hidden = days.cups.iloc[:7].tolist(), days.cups.iloc[7:].tolist()     # 3 to 9 March, and 10 to 16 March
mean_rule = sum(seen) / 7
rules = {"the nephew's mean": [mean_rule] * 7, "seasonal naive": seen}       # hidden day k copies seen day k
scores = {}
for name, f in rules.items():
    misses = [a - b for a, b in zip(f, hidden)]
    scores[name] = sum(abs(m) for m in misses) / 7
    print(f"{name}: MAE {scores[name]:.1f} cups, lean {sum(misses) / 7:+.1f}")

def earns_a_place(rule_mae, baseline_mae):
    """The chapter's rule: nothing goes to the order unless it beats the seasonal naive on hidden days."""
    return rule_mae < baseline_mae

labels = days.weekday.iloc[7:].tolist()
fig, axes = plt.subplots(1, 2, figsize=(12, 3.6), sharey=True, constrained_layout=True)
for ax, (name, f) in zip(axes, rules.items()):
    ax.plot(labels, hidden, color="black", marker="o", label="sold")
    ax.plot(labels, f, color="crimson", ls="--", marker="s", label="forecast")
    ax.set_title(f"{name}: MAE {scores[name]:.1f} cups")
axes[0].legend()
fig.suptitle("Two rules on seven hidden days, 10 to 16 March 2025 (invented numbers)")
plt.show()
print(f"the mean's miss on the hidden Sunday: {mean_rule - hidden[-1]:+.1f} cups")
check("the seasonal naive wins on the hidden days", scores["seasonal naive"] < scores["the nephew's mean"])
check("the nephew's mean earns no place", not earns_a_place(scores["the nephew's mean"], scores["seasonal naive"]))
'''),
        md("""
        **What happened.** The seasonal naive misses by 4.0 cups a day and the nephew's mean by
        12.4: the mean ignores the Sunday dip and misses that Sunday by 34.6 cups. Both lean low by
        the same 2.6 cups, so here the lean cannot separate them and the size does. Named last:
        nothing goes to the order unless it beats the seasonal naive on hidden days, by the
        measure fixed before either rule ran.

        ## Is a better forecast worth having?

        Milk comes in cans of 40 cups (invented), so the owner orders whole cans: the forecast over
        40, rounded up.

        **Predict before you run.** A forecast that knew the future exactly would beat the
        seasonal naive's 4.0 cups a day. On how many of the seven hidden days would it order a
        different number of cans?
        """),
        code('''
def cans(cups):
    return math.ceil(cups / can)                         # whole cans, rounded up

order = pd.DataFrame({"seasonal naive": [cans(v) for v in seen],
                      "perfect forecast": [cans(v) for v in hidden],
                      "nephew's mean": [cans(mean_rule)] * 7}, index=labels)
print(order.T.to_string())
differ = {name: int((order[name] != order["perfect forecast"]).sum()) for name in order}
print("days that order differently from a perfect forecast:", differ)
ax = order.plot.bar(color=["slateblue", "black", "crimson"], rot=0)
ax.set_ylim(0, 4.2)
ax.set_yticks(range(5))
ax.legend(ncol=3, loc="upper center")
ax.set_ylabel("cans of milk")
ax.set_title("Cans ordered for the seven hidden days, 40 cups a can (invented numbers)")
plt.show()
check("the seasonal naive orders a perfect forecast's cans on all seven days", differ["seasonal naive"] == 0)
check("the nephew's mean orders a third can on the Sunday", differ["nephew's mean"] == 1 and order["nephew's mean"].iloc[-1] == 3)
'''),
        md("""
        **What happened.** On none: the seasonal naive orders 3 cans a weekday and 2 on Sunday,
        exactly what a forecast that knew the future would order, on all seven days. The nephew's
        mean orders a third can on Sunday, milk that sours. Named last: **good enough** is a claim
        about the decision, never about the model. A better forecast is worth having only if it
        would change what gets ordered, so the owner stops improving here.

        ## What goes to the milkman?

        The **forecast note** carries four lines: the number, the method (what it copies), the
        error bar (the MAE on hidden days, in the unit and in rupees, each direction priced) and
        what would make it wrong. The cell below prints it from the notebook's own variables, so
        every number in it is one the notebook computed.
        """),
        code('''
bar = scores["seasonal naive"]
note = [
    f"The number: {order['seasonal naive'].iloc[0]} cans a day Monday to Saturday, {order['seasonal naive'].iloc[-1]} on Sunday.",
    "The method: the same day last week, the seasonal naive, which beat the nephew's mean on seven hidden days.",
    f"The error bar: {bar:.1f} cups a day on those days, about Rs {bar * unsold_rs:.0f} a day if it runs high "
    f"and Rs {bar * short_rs:.0f} if it runs short.",
    "What would make it wrong: exams starting early, or the hostel emptying for a holiday.",
]
print("\\n".join(note))
check("the note holds four lines", len(note) == 4)
check("the error bar is in cups and in rupees", "cups" in note[2] and "Rs" in note[2])
'''),
        md("""
        **The plausible wrong answer.** "The model fits 100 percent of history; order for 168
        cups." **The decision it misleads:** 168 cups is 5 cans against the 3 that day 5 needed,
        two cans of milk that sour. **The check:** the score on hidden days. **The fix:** the
        baseline's number with its error bar.
        """),
        md("""
        **Your turn.** Price the nephew's Sunday. Its mean orders one can more than a perfect
        forecast on Sunday; a can makes 40 cups, and a cup unsold wastes Rs 6 of milk (invented).
        Fill the blanks, type the lines into the empty cell below and run them; the check prints
        PASS when the price is right.

        ```python
        extra = order["nephew's mean"].iloc[-1] - order["perfect forecast"].iloc[-1]   # cans beyond the need
        waste_rs = extra * ___ * ___
        check("the nephew's Sunday wastes Rs 240 of milk", waste_rs == 240)
        ```
        """),
        empty(),
        md("""
        ## Which rules does the chapter leave?

        1. Fit is measured on the days a rule was built on, and it proves nothing about tomorrow.
        2. Nothing goes to the order unless it beats the seasonal naive on hidden days, by the
           measure fixed first.
        3. Good enough is a claim about the decision: stop improving when a better forecast would
           order the same.
        4. The note carries the number, the method, the error bar in the unit and in rupees, and
           what would make it wrong.

        **In the interview.** [F] "What baseline must any forecast beat, and why?" [F] "A vendor
        promises 22 percent growth; how do you test the claim?" Each is answered with the hidden
        periods and the seasonal naive, never with the fit.
        """),
        code('''
vendor = pd.read_csv("../data/C2_W04_D05_vendor_forecast_STUDENT.csv", parse_dates=["week_start"])
print(vendor.kind.value_counts().to_string())                  # the vendor's fits, hidden-week forecasts, weeks ahead
aligned_mae, bot_mae, vendor_mae = 6615, 9831, 16400           # notebook 06's scoreboard, shipments a week
per_shift = 120                                                # shipments a packer packs in a shift
print(f"against festival-aligned, the house bot misses by {(bot_mae - aligned_mae) / per_shift:.0f} more shifts "
      f"a week and the vendor by {(vendor_mae - aligned_mae) / per_shift:.0f}")
check("the vendor's file labels fits, hidden-week forecasts and the weeks ahead",
      set(vendor.kind) == {"fitted", "holdout", "forecast"})
check("a rule better by 100 shipments a week gains less than one shift", 100 < per_shift)
'''),
        md("""
        ## What did the chapter answer?

        | Question | The stall's answer, in invented numbers |
        |---|---|
        | What does a perfect fit say about tomorrow? | Nothing: the curve fits with an error of 0 and misses day 5 by 66 |
        | Does the clever rule beat the baseline? | No: the nephew's mean scores 12.4 cups against the seasonal naive's 4.0 |
        | Is a better forecast worth having? | Not here: the seasonal naive orders the cans a perfect forecast would |
        | What goes to the milkman? | 3 cans a weekday and 2 on Sunday, from last week's same day, give or take 4.0 cups, Rs 24 to Rs 48 a day |

        At Flipkart the vendor's curve fits its 91 weeks within 1.4 percent and misses the thirteen
        hidden weeks by 16,400 a week. The decision unit is a shift of 120 shipments, so the house
        bot's gap is 27 shifts a week and the vendor's 82. Chapter 6's notebook,
        `C2_W04_D05_06_case_holdout_scoreboard_STUDENT.ipynb`, tests the vendor's curve, and
        chapter 7's, `C2_W04_D05_07_case_good_enough_forecast_note_STUDENT.ipynb`, makes the
        good-enough call and books the plan.
        """),
    ]


def nb05():
    return [
        md(f"""
        # Trend, seasonality and baselines on Flipkart's weeks: where is the peak, and what do three rules say for one week?

        **Week 4, Friday, chapter 5, the case's first chapter.** It applies two of the day's
        topics: trend and seasonality, read before modelling (concept notebook 01), and naive,
        seasonal naive and drift baselines (concept notebook 02). On the chai stall (invented)
        those notebooks found a weekly beat of 7 days, growth of 10 percent a year read a season
        apart, and a seasonal naive that missed next Sunday by 1 cup where naive missed by 43.

        {TICKET}

        **Who needs the answer.** The FC planner, who books packer shifts weeks before the festival
        and cannot add a shift on the day, and the regional operations head, who signs the plan. A
        rule that puts the busiest week in the wrong place books packers for a week that is quiet.

        **The questions on the way.** Where is each year's peak on twelve real weeks? What do three
        rules say for Diwali 2025's own week? Which week does a copy of last year put the peak in?
        How far does Diwali's week move into 2026? Does the full series show the same shape?
        """),
        code(SETUP + '''
rows = pd.read_csv("../data/C2_W04_D05_twelve_rows_STUDENT.csv", parse_dates=["week_start"])
s = rows.set_index("week_start").shipments          # shipments, looked up by the week's Monday
rows
'''),
        md("""
        ## Where is each year's busiest week on the twelve rows?

        The twelve rows are six weeks around Diwali 2024 and six around Diwali 2025, straight from
        the centre's data. Notebook 01 read a series' shape before any rule; this is the same
        reading on Flipkart's weeks.

        **Predict before you run.** In each year, which week ships the most?

        a) Diwali's own week
        b) the week before Diwali's week
        c) two weeks before Diwali's week
        d) the week after Diwali's week
        """),
        code('''
diwali = pd.to_datetime(["2024-10-28", "2025-10-20"])   # the weeks holding Diwali
colours = ["crimson" if d in diwali else "lavender" for d in rows.week_start]
fig, ax = plt.subplots()
labels = rows.week_start.dt.strftime("%d %b %y")                 # each date as text, such as 14 Oct 24
ax.bar(labels, rows.shipments, color=colours, edgecolor="slateblue")
ax.tick_params(axis="x", rotation=60)
ax.set_title("Twelve weeks around two Diwalis (red: the week holding Diwali)")
plt.show()
peaks = []
for year in [2024, 2025]:
    one_year = rows[rows.week_start.dt.year == year]          # that year's six rows
    top = one_year.loc[one_year.shipments.idxmax()]           # the row with the most shipments
    print(year, "busiest week:", top.week_start.date(), f"{top.shipments:,} shipments")
    peaks.append(top.week_start)
check("both peaks sit two weeks before Diwali's week", peaks == list(pd.to_datetime(["2024-10-14", "2025-10-06"])))
'''),
        md("""
        **What happened.** The answer is c. The busiest week is two weeks before Diwali's week in
        both years: 401,000 shipments in the week of 14 October 2024 and 418,200 in the week of 6
        October 2025. Both fall in the festive sale, which runs in the third and second weeks before
        Diwali's week, and parcels leave the centre with the sale so they arrive before the
        festival. Diwali's own week ships less (296,900 and 308,900), and the week after falls
        lowest.

        ## What do three rules forecast for Diwali 2025's own week?

        Stand in the week of 13 October 2025 and forecast the next week, 20 October 2025, with the
        rules notebook 02 built on the stall. **Naive** repeats the week before. **The seasonal
        naive** with a season of 52 weeks copies the week 52 weeks back, the week of 21 October
        2024; the planners call it **same week last year**, and the tournament calls it **the house
        bot**. **Festival-aligned** copies the week at the same distance from last year's Diwali,
        which is Diwali 2024's own week, 28 October 2024, and adds the 4 percent a year the centre
        grew.

        **Predict before you run.** Which rule lands closest to the 308,900 that shipped?

        a) naive
        b) the seasonal naive, same week last year
        c) festival-aligned
        d) all three land within 10,000
        """),
        code('''
actual = s[pd.Timestamp("2025-10-20")]                    # Diwali 2025's own week
naive = s[pd.Timestamp("2025-10-13")]                     # the week before
seasonal = s[pd.Timestamp("2024-10-21")]                  # 52 weeks back: same week last year
aligned = round(s[pd.Timestamp("2024-10-28")] * 1.04)     # Diwali 2024's own week, plus 4 percent
for name, forecast in [("naive", naive), ("seasonal naive", seasonal), ("festival-aligned", aligned)]:
    print(f"{name}: forecast {forecast:,}, miss {forecast - actual:+,}")
check("festival-aligned lands closest",
      abs(aligned - actual) < min(abs(naive - actual), abs(seasonal - actual)))
'''),
        md("""
        **What happened.** The answer is c. Naive misses by 60,100 and the seasonal naive by
        47,300, both too high; festival-aligned misses by 124. A miss here is the forecast minus
        what shipped, so a positive miss is too high. The week 52 weeks back looks like "the same
        week", but in 2024 it was the week before Diwali, and the week before Diwali ships more than
        Diwali's own week.

        ## Which week does a copy of last year put the peak in?

        **The plausible wrong answer.** "Same week last year already knows the season, so it is the
        safe rule for a festival." Copy every 2025 week from 52 weeks back with the seasonal naive
        and see where its peak lands. Beside it, festival-aligned reaches back 51 weeks, because
        Diwali 2025's week came 51 weeks after Diwali 2024's.
        """),
        code('''
y25 = s[s.index.year == 2025]                             # the six 2025 rows
copy52, copy51 = {}, {}
for d in y25.index:
    copy52[d] = s.get(d - pd.Timedelta(weeks=52))           # blank when that week is not in the twelve rows
    copy51[d] = round(s[d - pd.Timedelta(weeks=51)] * 1.04)  # the week at the same distance from Diwali
table = pd.DataFrame({"actual": y25, "seasonal naive": pd.Series(copy52).astype("Int64"),
                      "festival-aligned": pd.Series(copy51)})
print(table.to_string())
ax = table.astype(float).plot(marker="o", title="2025's festive weeks against two copies of 2024")
ax.set_xlabel("week beginning")
plt.show()
check("the copy of last year peaks on 13 Oct 2025", table["seasonal naive"].idxmax() == pd.Timestamp("2025-10-13"))
check("the actual peak is 6 Oct 2025", y25.idxmax() == pd.Timestamp("2025-10-06"))
'''),
        md("""
        **Why it is wrong.** Diwali's week came one week earlier in 2025, so the copy of the same
        calendar week put 2024's peak (401,000) on 13 October 2025, a week late, and left the real
        peak week short. The check that catches it is the calendar: line up each year's weeks by
        their distance from Diwali before copying, as notebook 02 did for the stall's days. The
        week of 29 September 2025 shows a blank in the copy, because its source, 30 September 2024,
        is not one of the twelve rows.

        ## How far does Diwali's week move between 2025 and 2026?

        Diwali 2026 falls on Sunday 8 November, so its week begins Monday 2 November 2026. Count the
        weeks from Diwali 2025's week, and set them beside the 52 weeks a copy of last year steps
        back. Where that puts this year's rush is chapter 7's question, so hold your answer.
        """),
        code('''
diwali_2025, diwali_2026 = pd.Timestamp("2025-10-20"), pd.Timestamp("2026-11-02")
gap = (diwali_2026 - diwali_2025).days // 7                # weeks from one Diwali week to the next
print("weeks from Diwali 2025's week to Diwali 2026's:", gap)
print("weeks a copy of last year steps back: 52")
check("Diwali's week moves 54 weeks on, more than a year of weeks", gap == 54)
'''),
        md("""
        ## Does the full series show the same shape?

        The twelve rows came from 104 weeks. The ticket's `calendar` table flags each week that
        holds Diwali and each sale week, so the full series can be read against both.
        """),
        code('''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
calendar = pd.read_csv("../data/C2_W04_D05_calendar_STUDENT.csv", parse_dates=["week_start"])
sale = calendar.loc[calendar.sale_week == 1, "week_start"]          # every sale week the calendar flags
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.plot(weekly.week_start, weekly.shipments, color="slateblue")
for d in diwali:
    ax.axvline(d, color="crimson", ls="--")
for d in sale[sale <= weekly.week_start.max()]:
    ax.axvspan(d, d + pd.Timedelta(days=7), color="gold", alpha=0.4)
ax.set_title("104 weeks of outbound shipments; dashed: Diwali's week; gold: sale weeks")
plt.show()
festive_sale = [d for d in sale if d.month in (9, 10)]               # the festive sale, without August's
expected = []
for w in calendar.loc[calendar.diwali_week == 1, "week_start"]:
    expected += [w - pd.Timedelta(weeks=3), w - pd.Timedelta(weeks=2)]
print("festive sale weeks:", [str(d.date()) for d in festive_sale])
check("104 weeks", len(weekly) == 104)
check("the twelve rows are rows of the full series",
      rows.merge(weekly, on=["week_start", "shipments"]).shape[0] == 12)
check("each festive sale runs three and two weeks before Diwali's week", sorted(expected) == sorted(festive_sale))
'''),
        md("""
        ## What did chapter 5 answer?

        - **Where is the peak?** Two weeks before Diwali's week in both years, in the sale weeks:
          401,000 and 418,200.
        - **What do three rules say for 20 October 2025?** Naive 369,000, the seasonal naive (same
          week last year) 356,200, festival-aligned 308,776 against 308,900 shipped.
        - **Where does a copy of last year put the peak?** A week late in 2025. In 2026 Diwali's
          week comes 54 weeks after 2025's, where a copy steps back 52; chapter 7 asks what that
          does to this year's rush.
        - **Does the full series agree?** Yes: two festive peaks in the sale weeks, an August sale,
          ordinary weeks a little above 210,000.

        Chapter 6 asks the question one week cannot settle: how does each rule score on thirteen
        weeks it never saw?
        """),
    ]


def nb06():
    return [
        md(f"""
        # Holding out and the vendor curve tested, on thirteen hidden weeks: which rule wins, and which way is each wrong?

        **Week 4, Friday, chapter 6, the case's second chapter.** It applies three of the day's
        topics: naive, seasonal naive and drift baselines (concept notebook 02); holding out, MAE
        and MAPE in the business's units (concept notebook 03); and beating the baseline, the
        vendor curve tested (concept notebook 04). On the chai stall (invented) those notebooks
        scored naive at an MAE of 5.0 cups with a lean of -1.7, and the nephew's mean lost to the
        seasonal naive, 12.4 cups against 4.0.

        {TICKET}

        Chapter 5 found the peak two weeks before Diwali's week and showed that a copy of the same
        calendar week lands it a week late in 2025. This notebook scores every rule, and the
        vendor's curve, on weeks none of them saw.

        **Who needs the answer.** The FC planner, who may send only a forecast that has beaten the
        house bot on weeks it never saw, and the regional operations head, who must say yes or no
        to the vendor's plus 22 percent before a shift is booked.

        **The questions on the way.** Which weeks do we hide, and from which week do we forecast?
        What does each rule forecast for them? Which rule scores best? What did the vendor score,
        and what does its fit to the past say? Which way is each rule wrong, and what does that
        cost in rupees? Does the score match the printed error table?
        """),
        code(SETUP + '''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
vendor = pd.read_csv("../data/C2_W04_D05_vendor_forecast_STUDENT.csv", parse_dates=["week_start"])
y = weekly.set_index("week_start").shipments
split = 91                                    # the row of the first hidden week, 29 Jun 2026
train, hold = y.iloc[:split], y.iloc[split:]  # the weeks the rules may see, and the weeks they forecast
print(f"training weeks: {len(train)}, {train.index[0].date()} to {train.index[-1].date()}")
print(f"hidden weeks: {len(hold)}, {hold.index[0].date()} to {hold.index[-1].date()}")
print(vendor.kind.value_counts().to_string())
check("the hidden weeks are the latest ones", hold.index[-1] == y.index[-1])
check("no week is lost or counted twice", len(train) + len(hold) == len(y))
check("the vendor's rows for the hidden weeks are forecasts made from 22 June, never fits",
      set(vendor.set_index("week_start").loc[hold.index, "kind"]) == {"holdout"})
'''),
        md("""
        ## Which weeks do we hide, and how is the score counted?

        The plan's last week, 30 November, sits ten weeks past the last week of data; that reach is
        the **horizon**. The test hides at least as many weeks at the end of the data: the last
        thirteen, 29 June to 21 September 2026, the **hidden weeks** (also called the hold-out, or
        the test set). The rules may see only the 91 **training weeks** before them, and every rule
        forecasts all thirteen from the last of those, the week of 22 June 2026, called the
        **origin**. The vendor's file labels its rows three ways: **fitted** rows are its answers
        for weeks it was built on, **holdout** rows its forecasts for the hidden weeks, made from
        22 June, and **forecast** rows the weeks ahead.

        The score is the **mean absolute error** (MAE): each week's miss in shipments, sign dropped,
        averaged. Its cousin, the **mean absolute percentage error** (MAPE), averages each miss as a
        percent of what shipped: it compares centres of different sizes, and it divides by the
        actual, so a week that ships almost nothing makes it explode. Notebook 03 counted both by
        hand on the stall's three hidden days (invented): MAE 5.0 cups, MAPE about 4.8 percent.
        """),
        md("""
        ## What does each rule forecast for the hidden weeks?

        Each rule in one line, all from the week of 22 June 2026. **Naive** repeats that week.
        **Drift** draws the straight line from the first week through that week and extends it.
        **The seasonal naive**, the house bot, copies the week 52 weeks back. **Finance's rule** is
        the house bot plus 4 percent. **Festival-aligned**, from five weeks before Diwali's week to
        four after, copies the week at the same distance from last year's Diwali; on every other
        week it copies the same calendar week; then it adds the 4 percent a year the centre grew.
        No hidden week falls in that stretch around a Diwali, so on these weeks festival-aligned and
        finance's rule are one rule.

        Two pieces of code are new. `y.shift(52)` slides the whole series down 52 rows, so each
        week's row holds the value from 52 weeks earlier. `h` counts the weeks ahead of the origin,
        1 to 13. The growth line compares the latest 39 training weeks, 29 September 2025 to 22
        June 2026, with the same 39 weeks a year earlier.
        """),
        code('''
origin = train.index[-1]                                         # the last week the rules may see
h = pd.Series(range(1, len(hold) + 1), index=hold.index)         # weeks ahead: 1, 2, 3 and so on
slope = (train.iloc[-1] - train.iloc[0]) / (len(train) - 1)       # drift: the average change a week
growth = y.iloc[52:split].sum() / y.iloc[0:split - 52].sum() - 1  # a year's growth on the same weeks
factor = round(1 + growth, 2)                                     # 1.04, the same 4 percent finance uses
last_year = y.shift(52).loc[hold.index]                           # each hidden week's same week last year
rules = pd.DataFrame({
    "naive": train.iloc[-1],
    "drift": (train.iloc[-1] + h * slope).round(),
    "house bot": last_year,
    "finance": (last_year * 1.04).round(),
    "festival-aligned": (last_year * factor).round(),
}).astype(int)
nearest = min(abs((d - pd.Timestamp("2026-11-02")).days) // 7 for d in hold.index)
print(f"origin {origin.date()}, drift {slope:.0f} a week, growth a year {growth:.1%}")
print(f"the hidden week nearest Diwali 2026 is {nearest} weeks before it")
print(rules.head(3).to_string())
check("the growth the training weeks show rounds to 4 percent", factor == 1.04)
check("no hidden week falls in the stretch around a Diwali", nearest > 5)
'''),
        md("""
        **Predict before you run.** Which rule has the lowest MAE on the thirteen hidden weeks?

        a) naive
        b) drift
        c) the seasonal naive, the house bot
        d) festival-aligned, tied with finance's rule
        """),
        code('''
scores = pd.Series({name: (rules[name] - hold).abs().mean()     # each rule's misses, signs dropped, averaged
                    for name in rules.columns}).round().astype(int).sort_values()
weeks_ahead = range(1, len(hold) + 1)
fig, axes = plt.subplots(1, 4, figsize=(13, 3.2), sharey=True)
for ax, name in zip(axes, ["naive", "drift", "house bot", "festival-aligned"]):
    ax.plot(weeks_ahead, hold.values, color="black", label="actual")
    ax.plot(weeks_ahead, rules[name].values, ls="--", color="slateblue", label=name)
    ax.set_title(f"{name}: MAE {scores[name]:,}")
axes[0].legend()
plt.show()
print(scores.to_string())
check("festival-aligned and finance tie", scores["festival-aligned"] == scores["finance"])
check("the house bot beats naive and drift", scores["house bot"] < min(scores["naive"], scores["drift"]))
'''),
        md("""
        **What happened.** The answer is d. Festival-aligned and finance's rule tie at 6,615
        shipments a week, the house bot scores 9,831, and naive and drift miss by 14,923 and
        14,842. The house bot beats naive because it carries the August sale and the summer dip
        from last year; it loses to the 4 percent rules because a growing series makes last year's
        week too low. The tie is honest: on weeks this far from Diwali the two rules are the same
        arithmetic.

        **Predict before you run.** The vendor's sponsor says the curve sits within 2 percent of
        every past week. On the thirteen hidden weeks, how does it score against the house bot's
        9,831?

        a) far below the bot, since it fits the past best
        b) about the same as the bot
        c) above the bot: it misses by more

        **Your turn.** Score the vendor on the same hidden weeks. Type these lines into the empty
        cell below and run it:

        ```python
        v = vendor.set_index("week_start").vendor_shipments
        print(f"vendor MAE: {(v.loc[hold.index] - hold).abs().mean():,.0f}")
        ```
        """),
        empty(),
        md("""
        ## What does the vendor's fit to the past say about its forecast?

        **The plausible wrong answer.** The vendor's sponsor, the manager who brought the model in,
        says: "The curve sits within 2 percent of every week of history, so its plus 22 percent can
        be trusted." A fit is drawn through weeks the model has seen; a forecast is made for weeks
        it has not. Within 2 percent is the sponsor's claim; the cell below measures the worst
        fitted week.
        """),
        code('''
v = vendor.set_index("week_start").vendor_shipments
fitted = vendor[vendor.kind == "fitted"].set_index("week_start").vendor_shipments
fit_gap = ((fitted - y.loc[fitted.index]) / y.loc[fitted.index]).abs().max()   # the worst fitted week
hold_gap = (v.loc[hold.index] - hold) / hold                                    # each hidden week, as a share
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.bar(fitted.index, (fitted - y.loc[fitted.index]) / y.loc[fitted.index] * 100, width=5, color="plum", label="fitted")
ax.bar(hold.index, hold_gap * 100, width=5, color="crimson", label="hidden weeks")
ax.set_ylabel("vendor minus actual, percent")
ax.legend()
plt.show()
print(f"largest miss on the {len(fitted)} fitted weeks: {fit_gap:.1%}")
vendor_mae = (v.loc[hold.index] - hold).abs().mean()                            # the same measure as the rules
print(f"vendor MAE on the hidden weeks: {vendor_mae:,.0f}")
k = len(hold) // 2                                                              # six of thirteen
print(f"too high by {hold_gap.iloc[:k].mean():.1%} on average in hidden weeks 1 to {k}, "
      f"{hold_gap.iloc[-k:].mean():.1%} in weeks {len(hold) - k + 1} to {len(hold)}")
check("the fit stays within 2 percent", fit_gap <= 0.02)
check("the vendor's MAE is at least 30 percent above festival-aligned",
      vendor_mae >= 1.3 * scores["festival-aligned"])
'''),
        md("""
        **Why it is wrong.** The answer is c. The vendor never misses its fitted weeks by more than
        1.4 percent, and it misses the hidden weeks by 16,400 a week, 148 percent worse than
        festival-aligned and 67 percent worse than the house bot. The check is the one the room
        fixed before scoring: error on the weeks it never saw. The fix is to send nothing to the
        plan that loses to the house bot there, as the stall's owner sent nothing that lost to the
        seasonal naive in notebook 04.

        ## Which way is each rule wrong, and what does each direction cost?

        **Predict before you run.** Which rule's misses cost the least once a late shipment costs
        Rs 25 and a spare shipment Rs 5.42?

        a) festival-aligned, since its MAE is lowest
        b) the vendor
        c) the house bot
        d) naive
        """),
        code('''
rules["vendor"] = v.loc[hold.index]
rows = []
for name in rules.columns:
    miss = rules[name] - hold                                     # forecast minus actual: positive is too high
    spare_rs = miss[miss > 0].sum() * 650 / 120                    # planned and never shipped, Rs 5.42 each
    late_rs = -miss[miss < 0].sum() * 25                           # shipped late, Rs 25 each
    rows.append({"rule": name, "MAE": round(miss.abs().mean()), "weeks too high": int((miss > 0).sum()),
                 "spare Rs lakh": round(spare_rs / 100_000, 1),     # 100,000 rupees make a lakh
                 "late Rs lakh": round(late_rs / 100_000, 1),
                 "cost Rs lakh": round((spare_rs + late_rs) / 100_000, 1)})
priced = pd.DataFrame(rows).set_index("rule").sort_values("cost Rs lakh")
print(priced.to_string())
priced[["late Rs lakh", "spare Rs lakh"]].sort_values("late Rs lakh").plot.barh(stacked=True,
    color=["crimson", "plum"], title="The same misses in rupees, added over the hidden weeks")
plt.show()
check("the vendor errs high on most hidden weeks", priced.loc["vendor", "weeks too high"] > len(hold) / 2)
check("on these hidden weeks, priced, the vendor costs less than festival-aligned",
      priced.loc["vendor", "cost Rs lakh"] < priced.loc["festival-aligned", "cost Rs lakh"])
'''),
        md("""
        **What happened.** The answer is b, and it is the uncomfortable result. The vendor's
        misses cost Rs 11.9 lakh, festival-aligned's Rs 13.5 lakh, the house bot's Rs 30.5 lakh,
        each added over the thirteen weeks. The vendor errs high on 12 of 13 weeks, and a spare
        shipment costs Rs 5.42 against Rs 25 for a late one, so its bigger misses are the cheaper
        kind. The house bot's misses are the dear kind: 11 of its 13 weeks are too low, which is why
        it costs more than naive while scoring a lower MAE. The stall showed the same in notebook
        03: one MAE, two prices.

        This says that erring high pays at these costs. It does not hand the vendor the plan:
        nobody chose how far high it runs, it runs higher the further ahead it looks (3.6 percent
        too high in hidden weeks 1 to 6, 11.5 percent in weeks 8 to 13), and no hidden week holds a
        festival, where the vendor copies the wrong weeks. Chapter 7 books the plan at
        festival-aligned's forecast and prices its error bar each way; how far above the forecast a
        plan should sit, the plan quantile, goes beyond today's curriculum row and runs in the
        fallback hour and in notebook 07's depth section.

        ## Does the score match the printed error table?

        A second route to the same number: print festival-aligned's thirteen misses as a table and
        average them by hand.
        """),
        code('''
table = pd.DataFrame({"actual": hold, "festival-aligned": rules["festival-aligned"]})
table["miss"] = table["festival-aligned"] - table["actual"]        # positive: too high
print(table.to_string())
by_hand = sum(abs(m) for m in table["miss"]) / len(table)
print(f"too high: {table.miss[table.miss > 0].sum():,}; too low: {-table.miss[table.miss < 0].sum():,}")
print(f"MAE from the printed misses: {by_hand:,.0f}")
check("the printed table gives the same MAE", round(by_hand) == scores["festival-aligned"])
'''),
        md("""
        ## How would you answer "how do you evaluate a forecast?" in an interview?

        Hold out the latest weeks as a test set, at least as many as the forecast must reach
        ahead, and forecast them from one origin; then roll the origin, since one origin is one
        draw. Fix two measures before anyone scores: the miss in shipments, and the misses priced
        by direction, which is what the plan pays. Compare every candidate with the naive and the
        seasonal naive, here the house bot, and send nothing that loses to them. The trap the
        interviewer fishes for is judging by the fit.
        """),
        md("""
        ## What did chapter 6 answer?

        - **Which weeks are hidden?** The last thirteen, 29 June to 21 September 2026, forecast
          from the week of 22 June 2026.
        - **Which rule scores best?** Festival-aligned and finance's rule, tied at 6,615 a week;
          the house bot 9,831; naive 14,923; drift 14,842.
        - **What did the vendor score?** 16,400, after fitting history within 1.4 percent: fit is
          not forecast.
        - **Which way is each wrong, and at what cost?** The vendor errs high on 12 of 13 weeks and
          costs Rs 11.9 lakh; festival-aligned Rs 13.5 lakh; the house bot errs low and costs Rs
          30.5 lakh.
        - **Does the table agree?** Yes, 6,615 from the printed misses.
        - **Is festival-aligned good enough?** Good enough is a claim about the decision: a better
          forecast is worth having only if it would book different shifts. Chapter 7 asks where the
          festival falls this year and how many packer shifts the plan books, which these weeks
          cannot test.
        """),
    ]


def nb07():
    return [
        md(f"""
        # The good-enough call and the staffing note, for the festive window: which forecast goes to the plan, and how many packer shifts a week?

        **Week 4, Friday, chapter 7, the case's third chapter.** It applies four of the day's
        topics: trend and seasonality, read before modelling, for the windows a growth figure is
        read against (concept notebook 01); naive, seasonal naive and drift baselines, for the
        calendar copy (notebook 02); holding out, MAE and MAPE in the business's units, for a
        hold-out that holds a festival and the misses priced (notebook 03); and the good-enough call
        and the forecast note (notebook 04). On the chai stall (invented) those notebooks found that
        a perfect forecast would order the same cans as the seasonal naive, so the owner stopped
        improving and sent a four-line note.

        {TICKET}

        Chapter 6 scored every rule on thirteen hidden summer weeks: festival-aligned and finance's
        rule tied at 6,615 a week, the house bot scored 9,831, the vendor 16,400. None of those
        weeks held a festival, so the hold-out could not test the festive weeks the plan depends on.

        **Who needs the answer.** The FC planner, who books the shifts, and the regional operations
        head, who answers for late parcels in the festival's busiest weeks. A plan that puts the
        peak in the wrong week pays for idle packers and late shipments in the same month.

        **The questions on the way.** How did each rule do on 2025's festival? Which week does each
        forecast put this year's peak in? How do the four forecasts compare with last year's two
        windows? How many packer shifts a week, and how wrong could the plan be? Is a better
        forecast worth having? What would the other plans cost?
        """),
        code(SETUP + '''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
vendor = pd.read_csv("../data/C2_W04_D05_vendor_forecast_STUDENT.csv", parse_dates=["week_start"])
costs = pd.read_csv("../data/C2_W04_D05_costs_STUDENT.csv").set_index("item").rs
y = weekly.set_index("week_start").shipments
v = vendor.set_index("week_start").vendor_shipments
spare_rs = costs["idle_packer_shift"] / 120          # an idle shift's Rs 650 over 120 shipments: Rs 5.42
late_rs = costs["late_shipment"]                      # Rs 25 a late shipment
diwali = {2024: pd.Timestamp("2024-10-28"), 2025: pd.Timestamp("2025-10-20"), 2026: pd.Timestamp("2026-11-02")}

source = {}                                           # week -> the week festival-aligned copies for it
for d in pd.date_range(y.index[52], "2026-11-30", freq="7D"):   # every week with a year of weeks behind it
    source[d] = d - pd.Timedelta(weeks=52)            # outside the stretch: the same calendar week
    for year, w in diwali.items():
        gap = (d - w).days // 7                       # weeks from that year's Diwali week; -5 is five before
        if -5 <= gap <= 4 and year - 1 in diwali:
            source[d] = diwali[year - 1] + pd.Timedelta(weeks=gap)   # the same distance from last year's Diwali

print(f"a spare shipment costs Rs {spare_rs:.2f}; a late one Rs {late_rs}")
print(source[pd.Timestamp("2026-10-19")].date(), "is the source for the week of 19 Oct 2026")
check("the week of 19 Oct 2026 copies 6 Oct 2025", source[pd.Timestamp("2026-10-19")] == pd.Timestamp("2025-10-06"))
'''),
        md("""
        ## How did each rule do on 2025's festival?

        The only festival the data can test the rules on is 2025's. A **back-test** stands at an
        earlier date and forecasts what came next as if the later weeks were unknown: stand in the
        week of 22 September 2025 and forecast the eight weeks from 29 September to 17 November
        2025. Festival-aligned copies, from five weeks before Diwali's week to four after, the week
        at the same distance from last year's Diwali. The 4 percent growth was measured later, on
        weeks up to June 2026, so the cell also runs festival-aligned with no growth, as a planner
        in September 2025 could have.

        **Predict before you run.** By how many weeks does the house bot, the seasonal naive, miss
        2025's peak?

        a) none: same week last year knows the season
        b) one week late
        c) one week early
        d) two weeks late
        """),
        code('''
weeks25 = pd.date_range("2025-09-29", periods=8, freq="7D")        # 29 Sep to 17 Nov 2025
back = pd.DataFrame({
    "actual": y.loc[weeks25],
    "house bot": [y[d - pd.Timedelta(weeks=52)] for d in weeks25],
    "finance": [round(y[d - pd.Timedelta(weeks=52)] * 1.04) for d in weeks25],
    "festival-aligned": [round(y[source[d]] * 1.04) for d in weeks25],
    "aligned, no growth": [y[source[d]] for d in weeks25],
}, index=weeks25)
back[["actual", "house bot", "festival-aligned"]].plot(marker="o", title="2025's festival, forecast from 22 Sep 2025")
plt.show()
for rule in ["house bot", "finance", "festival-aligned", "aligned, no growth"]:
    miss = back[rule] - back.actual                                  # positive: too high
    spare = miss[miss > 0].sum() * spare_rs
    late = -miss[miss < 0].sum() * late_rs
    print(f"{rule}: MAE {miss.abs().mean():,.0f}; spare Rs {spare / 100_000:.1f} lakh, "
          f"late Rs {late / 100_000:.1f} lakh, total Rs {(spare + late) / 100_000:.1f} lakh")
overtime = weekly.set_index("week_start").overtime_shifts
print(f"overtime shifts: {overtime['2025-10-06']:,} in the week of 6 Oct 2025, {overtime['2025-11-24']} in the week of 24 Nov 2025")
check("the bot's peak is 13 Oct 2025, a week late", back["house bot"].idxmax() == pd.Timestamp("2025-10-13"))
check("festival-aligned peaks on 6 Oct 2025 with the actual", back["festival-aligned"].idxmax() == back.actual.idxmax())
'''),
        md("""
        **What happened.** The answer is b. The house bot put 2024's peak on 13 October 2025, a
        week late: MAE 58,250 and Rs 79.8 lakh of misses, Rs 69.6 lakh of it late shipments in the
        weeks where 2025's rush came before the copy expected it. Finance's rule, the same copy plus
        4 percent, missed by 60,488 a week. Festival-aligned missed by 4,034 a week and Rs 4.6 lakh,
        and with no growth added it still missed by only 10,575. One festival is a thin test, so the
        plan treats this as evidence about placement, never as a precise error.

        ## Which week does each forecast put this year's peak in?

        Diwali 2026 falls on Sunday 8 November, so its week begins 2 November, and the sale, and
        with it the peak, should come two weeks before, in the week of 19 October.

        **Predict before you run.** Which week does the house bot's copy of 2025 make the busiest
        week of the festive season?

        a) 5 October 2026
        b) 19 October 2026
        c) 26 October 2026
        d) 2 November 2026
        """),
        code('''
weeks26 = pd.date_range("2026-09-28", periods=10, freq="7D")        # 28 Sep to 30 Nov 2026
ahead = pd.DataFrame({
    "house bot": [y[d - pd.Timedelta(weeks=52)] for d in weeks26],
    "finance": [round(y[d - pd.Timedelta(weeks=52)] * 1.04) for d in weeks26],
    "vendor": v.loc[weeks26].values,
    "festival-aligned": [round(y[source[d]] * 1.04) for d in weeks26],
}, index=weeks26)
ahead.plot(marker="o", title="Four forecasts, 28 Sep to 30 Nov 2026")
plt.show()
print(ahead.idxmax().dt.date.to_string())
check("the bot's busiest week is 5 Oct 2026", ahead["house bot"].idxmax() == pd.Timestamp("2026-10-05"))
check("festival-aligned's busiest week is 19 Oct 2026", ahead["festival-aligned"].idxmax() == pd.Timestamp("2026-10-19"))
'''),
        md("""
        **What happened.** The answer is a. The house bot, finance's rule and the vendor all make 5
        October 2026 the busiest week, because each copies 2025's calendar weeks; festival-aligned
        puts it on 19 October, two weeks before Diwali's week. The window the planner books starts
        a week after 5 October, so inside it the calendar copies book the most for 12 October
        (369,000 from the house bot) and far too little for 19 and 26 October (308,900 and 188,600),
        when festival-aligned expects 434,928 and 383,760. The vendor's model never knew the
        festival moved.

        ## How do the four forecasts compare with last year's window?

        "Last year's window" has two readings, as notebook 01 read the stall's growth only against
        the same point a season apart. The same calendar weeks, 13 October to 1 December 2025, hold
        only the tail of 2025's festival. The same weeks counted from Diwali, 29 September to 17
        November 2025, hold all of it.

        **Predict before you run.** Finance's eight weeks sit 4 percent above the same calendar
        weeks of 2025. Where do they sit against 2025's weeks counted from Diwali?

        a) 4 percent above, the same as on the calendar weeks
        b) between 0 and 4 percent above
        c) below them
        """),
        code('''
window = weeks26[2:]                                    # 12 Oct to 30 Nov 2026, the weeks to book
calendar_2025 = y.loc[window - pd.Timedelta(weeks=52)].sum()
festival_2025 = y.loc[[source[d] for d in window]].sum()
totals = ahead.loc[window].sum()
compare = pd.DataFrame({"eight weeks": totals.map("{:,}".format),
                        "vs same calendar weeks": (totals / calendar_2025 - 1).map("{:+.1%}".format),
                        "vs same weeks from Diwali": (totals / festival_2025 - 1).map("{:+.1%}".format)})
print(f"2025, same calendar weeks: {calendar_2025:,}   2025, same weeks from Diwali: {festival_2025:,}")
print(compare.to_string())
print(f"finance below festival-aligned: {totals['festival-aligned'] - totals['finance']:,} shipments")
check("finance is plus 4 percent on the calendar window", round(totals["finance"] / calendar_2025 - 1, 3) == 0.04)
check("the vendor is plus 22 percent on the calendar window", round(totals["vendor"] / calendar_2025 - 1, 3) == 0.22)
check("finance sits below festival-aligned", totals["finance"] < totals["festival-aligned"])
'''),
        md("""
        **What happened.** The answer is c. Against the calendar weeks, festival-aligned reads 19.5
        percent above last year, close to the vendor's 22.0, because 2026's peak weeks fall inside
        the window and 2025's fell before it. Against the weeks counted from Diwali it reads 4.0
        percent. Finance's plus 4 is plus 4 only on the calendar window: against last year's
        festival weeks it sits 9.5 percent below, and against festival-aligned's forecast it is
        308,048 shipments short, on the costly side. The vendor's total sits 2.1 percent above
        festival-aligned, with its busiest week on 5 October.

        ## How many packer shifts does each week need, and how wrong could the plan be?

        The plan books festival-aligned's forecast: each week's shipments over 120 a shift, rounded
        up, since a shipment that does not fill a shift still needs one. The error bar is chapter
        6's MAE in the business's unit, then priced each way, as notebook 03 priced the stall's
        misses.
        """),
        code('''
forecast = ahead.loc[window, "festival-aligned"]
shifts = (forecast / 120).apply(math.ceil)                       # whole shifts, rounded up
staffing = pd.DataFrame({"festival-aligned forecast": forecast, "packer shifts": shifts})
print(staffing.to_string())
error_bar = 6615                                                 # chapter 6's MAE, shipments a week
print(f"Book {shifts.sum():,} packer shifts for 12 October to 30 November, peaking at {shifts.max():,} "
      f"in the week of {shifts.idxmax():%d %B}.")
print(f"The error bar: {error_bar:,} shipments a week, about {error_bar / 120:.0f} shifts; about "
      f"Rs {round(error_bar * spare_rs, -2):,.0f} of idle shifts a week if it runs that far high, "
      f"Rs {error_bar * late_rs / 100_000:.2f} lakh of late shipments if that far low.")
staffing["packer shifts"].plot.bar(color="lavender", edgecolor="slateblue", title="Packer shifts a week, at the forecast")
plt.show()
check("the plan books 19,760 packer shifts", shifts.sum() == 19760)
check("the busiest week of the plan is 19 Oct 2026", shifts.idxmax() == pd.Timestamp("2026-10-19"))
'''),
        md("""
        **What happened.** The plan books 19,760 packer shifts over the eight weeks, peaking at
        3,625 in the week of 19 October; the error bar is 6,615 shipments a week, about 55 shifts.
        A late shipment costs 4.6 times a spare one, so the same miss is dear when the plan runs
        short and cheap when it runs high, which is why the note prices both.

        ## Is a better forecast worth having?

        Good enough is a claim about the decision, as the stall's cans showed in notebook 04. Here
        the decision unit is a shift of 120 shipments. A forecast earns its place only if it would
        book different shifts.
        """),
        code('''
gaps = {"house bot": (9831 - 6615) / 120, "vendor": (16400 - 6615) / 120}    # chapter 6's MAEs, over a shift
print("extra miss against festival-aligned, shifts a week:", {k: round(g) for k, g in gaps.items()})
moved = shifts - ((forecast - 100) / 120).apply(math.ceil)                    # a rule better by 100 shipments a week
print("shifts that rule would book differently, week by week:", moved.tolist())
print(f"weeks it moves a shift at all: {(moved > 0).sum()} of {len(moved)}, against {shifts.min():,} to {shifts.max():,} booked")
check("the house bot and the vendor each miss by more than a shift a week more", min(gaps.values()) > 1)
check("a rule 100 shipments better moves at most one shift in any week", moved.max() <= 1)
'''),
        md("""
        **What happened.** Festival-aligned is good enough: the house bot misses by 27 more shifts a
        week and the vendor by 82, so both lose real shifts, while a rule 100 shipments a week
        better would move one shift in 7 of the 8 weeks against 1,635 to 3,625 booked. The next
        model must earn its place by more than a shift a week, on hidden weeks.

        ## What would the other plans cost if demand follows the festival-aligned forecast?

        A scenario, never a measurement: if festival-aligned is right about where the rush falls,
        what does booking by each other forecast cost? Each plan is priced against festival-aligned's
        weeks, Rs 5.42 for every spare shipment and Rs 25 for every shipment short. The 2025
        back-test is the evidence that festival-aligned places the rush well; this table prices
        being wrong about it.
        """),
        code('''
booked = {"house bot": ahead.loc[window, "house bot"], "finance": ahead.loc[window, "finance"],
          "vendor": ahead.loc[window, "vendor"]}
scenario = {}
for name, b in booked.items():
    gap = b - forecast                                         # positive: spare capacity
    scenario[name] = (gap[gap > 0].sum() * spare_rs - gap[gap < 0].sum() * late_rs) / 100_000
    print(f"{name}: Rs {scenario[name]:.1f} lakh")
check("every calendar-copied plan costs more than Rs 80 lakh in this scenario", min(scenario.values()) > 80)
'''),
        md("""
        **What happened.** If demand follows festival-aligned, the house bot's weeks cost Rs 111.6
        lakh, finance's Rs 103.6 lakh and the vendor's Rs 82.2 lakh, mostly late shipments in the
        weeks of 19 October to 2 November.

        ## What can two years of weeks not tell us?

        - **The festival moves, and the sale moves with it.** Tested on one festival only: the 2025
          back-test.
        - **Two years hold only two festivals,** so the festival's shape rests on two examples; no
          check inside the data closes that.
        - **The hidden weeks hold no festive week,** so their 6,615 is an ordinary-week error; the
          2025 festival gave 4,034 on one festival.
        - **Capacity caps the peak.** Overtime reached 1,638 shifts in the week of 6 October 2025
          against 5 in the week of 24 November 2025, as the back-test cell printed, so peak demand
          may have run above what shipped.
        - **The 4 percent growth** is two years' evidence; a third year could move it.
        - **The vendor's model has never forecast a Lucknow festival it had not seen,** so its
          festive numbers are an untested assumption.

        ## Depth, beyond the row: how far above the forecast should the plan sit?

        This section goes beyond the five topics of Friday's curriculum row. It is the plan
        quantile, which the fallback hour teaches; the plan above books the forecast itself. It
        opens on the chai stall (invented): a cup short costs Rs 12 and a cup unsold Rs 6, so one
        more cup of milk pays off whenever the stall would sell it on more than one day in three,
        and the owner should cover demand on two days in three, 12 over 12 plus 6.

        **Predict before you run.** At Flipkart a late shipment costs Rs 25 and a spare one Rs
        5.42. Where should the plan sit?

        a) at the forecast, covering demand in about half the weeks
        b) above the forecast, covering demand in about four weeks of five
        c) far enough above to cover every week
        d) below the forecast, since spare shipments waste money

        The cell below works out the share of weeks the plan should cover from the two costs, then
        reads that point off festival-aligned's own misses on chapter 6's hidden weeks. Here the
        miss is measured the other way round: how far demand came **above** the forecast, as a
        share of it, so a positive number is a week the forecast was too low.
        """),
        code('''
hold = y.iloc[91:]                                              # chapter 6's thirteen hidden weeks
fa_hold = (y.shift(52).loc[hold.index] * 1.04).round()          # festival-aligned on them
above = (hold - fa_hold) / fa_hold                              # demand above the forecast, as a share
print("demand above the forecast, percent, smallest first:")
print((above * 100).round(1).sort_values().to_list())
q = late_rs / (late_rs + spare_rs)                              # the share of weeks to cover
cushion = round(above.quantile(q), 3)                           # 0.82 of the way along the sorted thirteen
covered = (above <= cushion).sum()
print(f"cover {q:.2f} of weeks: raise the forecast by {cushion:.1%}, which covers {covered} of the 13 weeks")
raised = fa_hold * (1 + cushion)
gap = raised - hold                                             # positive: spare
raised_cost = (gap[gap > 0].sum() * spare_rs - gap[gap < 0].sum() * late_rs) / 100_000
print(f"raised by {cushion:.1%}, these weeks' misses cost Rs {raised_cost:.1f} lakh, read from the same weeks")
check("the plan share is about 0.82", round(q, 2) == 0.82)
check("the cushion sits between the 10th and 11th sorted weeks",
      sorted(above)[9] <= cushion <= sorted(above)[10])
'''),
        md("""
        **What happened.** The answer is b. Raise the plan by one shipment and two things can happen.
        If demand turns out higher, that shipment is no longer late, which saves Rs 25. If demand
        turns out lower, it is a spare shipment, which wastes Rs 5.42. Picture 100 weeks. If demand
        beats the plan in 18 of them, one more shipment of plan saves 18 x Rs 25 = Rs 450 and wastes
        82 x Rs 5.42 = Rs 444: about even, so stop there. That is the rule, called the newsvendor
        rule after a seller deciding how many papers to stock: plan so that demand is covered in
        this share of weeks.

        $$\\text{share covered} = \\frac{\\text{late cost}}{\\text{late cost} + \\text{spare cost}} = \\frac{25}{25 + 5.42} \\approx 0.82$$

        Sorted, the thirteen weeks run from 5.9 percent below the forecast to
        7.8 percent above. The 0.82 point sits between the 10th week, 2.1 percent, and the 11th,
        2.7 percent; `quantile` reads it 0.82 of the way along the list, at 2.6 percent. The raised
        forecast covers 10 of the 13 weeks, and the 11th misses by a hair. With thirteen weeks the
        point is loose: read by another common convention it lands at 4.1 percent. The curve below
        shows why that matters little: the busiest week costs about Rs 1.4 lakh anywhere from 2 to
        4 percent above the forecast, against Rs 2.1 lakh booked at the forecast itself.

        For one possible demand the week costs the spare shipments, `max(0, plan_level - demand)`,
        at Rs 5.42, plus the late ones, `max(0, demand - plan_level)`, at Rs 25; at most one of the
        two is above zero.
        """),
        code('''
base = forecast["2026-10-19"]                                 # the plan's busiest week
levels = [i / 1000 for i in range(-80, 101, 2)]               # 8 percent below to 10 percent above
cost_at = []
for g in levels:                                              # each way the plan could be raised
    plan_level = base * (1 + g)
    total = 0
    for a in above:                                           # each past miss, as a possible demand
        demand = base * (1 + a)
        total += max(0, plan_level - demand) * spare_rs + max(0, demand - plan_level) * late_rs
    cost_at.append(total / len(above) / 100_000)              # the week's average cost, Rs lakh
plt.plot([g * 100 for g in levels], cost_at, color="black")
plt.axvline(cushion * 100, ls="--", color="slateblue")
plt.xlabel("plan above the forecast for the week of 19 Oct 2026, percent")
plt.ylabel("average cost of the week, Rs lakh")
plt.title("Too little plan costs more than too much, so the lowest point sits above the forecast")
plt.show()
lowest = levels[cost_at.index(min(cost_at))]
raised_shifts = (forecast * (1 + cushion)).round().div(120).apply(math.ceil)
print(f"the lowest cost sits {lowest:.1%} above the forecast; the plan takes {cushion:.1%}")
print(f"raised, the plan books {raised_shifts.sum():,} shifts, {raised_shifts.sum() - shifts.sum():,} more than the "
      f"{shifts.sum():,} at the forecast, and {raised_shifts.max():,} in the week of 19 October")
check("the cheapest plan sits above the forecast", lowest > 0)
check("the raised plan books 20,275 shifts", raised_shifts.sum() == 20275)
'''),
        md("""
        **What happened.** Raised by the 2.6 percent cushion, the plan books 20,275 packer shifts,
        515 more than at the forecast, and 3,719 in the week of 19 October. If demand lands exactly
        on the forecast, the extra shifts cost Rs 3.3 lakh: the price of the insurance. This is a
        refinement beyond the row; the plan the chapter sends books the forecast and prices its
        error bar each way.

        ## The same method at an AI company: how much inference capacity does a launch need?

        **Inference** is the computing a model does each time it answers a user. A product launch
        is the festival: a known date, a spike, little history. Line the last launch up by days from
        launch day, hide as many days as the plan covers, score in requests a minute, beat the last
        launch's shape, and set capacity above the forecast, because a timeout costs more than an
        idle server.

        ## What did chapter 7 answer?

        - **2025's festival:** the house bot landed the peak a week late (Rs 79.8 lakh of misses);
          festival-aligned missed by Rs 4.6 lakh.
        - **This year's peak:** the house bot, finance and the vendor put it on 5 October 2026;
          festival-aligned on 19 October.
        - **Last year's windows:** festival-aligned is 19.5 percent above the calendar weeks and 4.0
          percent above the weeks from Diwali; finance is 9.5 percent below the festival weeks.
        - **Shifts, and how wrong:** 19,760 over eight weeks, 3,625 in the week of 19 October, with
          an error bar of 6,615 shipments a week, about Rs 35,800 if it runs high and Rs 1.65 lakh
          if low.
        - **Is a better forecast worth having?** Only one that moves more than a shift a week; a
          rule 100 shipments better moves at most one.
        - **The others' cost:** Rs 82.2 to 111.6 lakh if demand follows festival-aligned.
        - **Beyond the row:** cover 0.82 of weeks with a 2.6 percent cushion, 20,275 shifts.
        """),
    ]


def nb08():
    return [
        md("""
        # Kalpa's board number, by the day's method of shape, baselines, hold-out and the note: which revenue forecast goes to the board, and how wrong could it be?

        **Week 4, Friday, the TA lab: the same method on Kalpa Retail.** It applies all five of the
        day's topics, from concept notebooks 01 to 04: read the shape, run the baselines, hold out
        and score in rupees, beat the baseline, and write the note. Kalpa Retail's growth plan goes
        to the board and needs a number: revenue for October 2026 to March 2027, against a plan line
        15 percent above the same months a year earlier, with Diwali inside the window. Finance's
        forecast is last year plus 4 percent; marketing's vendor curve promises 22 percent. Anand
        Iyer, the finance controller: "Two forecasts, eighteen points apart. Which one do I put in
        front of the board, and how wrong could it be?" The data hold 24 months of revenue, October
        2024 to September 2026; April to September 2026 are the monthly sums of the 1,000 orders in
        the Week 2 data warehouse, the class's database of Kalpa's orders. Diwali fell on 31 October
        2024 and 20 October 2025, and falls on 8 November 2026.

        **Who needs the answer.** Anand, who signs the board number, and the head of Retail-Plus,
        whose stock and staff follow it. A number the board holds Kalpa to for two quarters costs
        either a missed promise or idle stock.

        **The questions on the way.** What shape do the two winters have? How do naive and drift
        score on April to September 2026? How do the seasonal copy and the vendor score? Which month
        does each copy put Diwali in this year? What error bar goes beside the board number?
        """),
        code(SETUP + '''
rev = pd.read_csv("../data/C2_W04_D05_kalpa_monthly_revenue_STUDENT.csv").set_index("month").revenue_rs
vendor = pd.read_csv("../data/C2_W04_D05_kalpa_vendor_forecast_STUDENT.csv").set_index("month")
plan = pd.read_csv("../data/C2_W04_D05_kalpa_plan_line_STUDENT.csv").set_index("month").plan_rs
print(f"{len(rev)} months, {rev.index[0]} to {rev.index[-1]}")
# 1e5 is 100,000 rupees, a lakh; 1e7 is a hundred lakh, a crore
print(f"Apr to Jun 2026: Rs {rev['2026-04':'2026-06'].sum() / 1e7:.2f} crore; Jul to Sep: Rs {rev['2026-07':'2026-09'].sum() / 1e7:.2f} crore")
check("24 months", len(rev) == 24)
check("the two quarters match the warehouse", (rev['2026-04':'2026-06'].sum(), rev['2026-07':'2026-09'].sum()) == (100_000_000, 98_400_000))
'''),
        md("""
        ## What shape do the two winters have?

        Twelve rows: October to March of 2024-25 and of 2025-26, in Rs lakh (a lakh is 100,000).

        **Predict before you run.** Which month is the biggest of each winter?

        a) October
        b) November
        c) December
        d) March
        """),
        code('''
winters = pd.DataFrame({"2024-25": rev["2024-10":"2025-03"].values, "2025-26": rev["2025-10":"2026-03"].values},
                       index=["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]) / 1e5
print(winters.round(1).to_string())
(rev / 1e5).plot(marker="o", title="Kalpa Retail revenue, Rs lakh a month", figsize=(10, 3.6))
plt.show()
check("October is each winter's biggest month", list(winters.idxmax()) == ["Oct", "Oct"])
'''),
        md("""
        ## How do naive and drift score on April to September 2026?

        Hide the last six months and forecast them from March 2026: the board's horizon is six
        months, so the test hides six. Naive repeats March; drift extends the line from October
        2024 through March 2026, 17 months of steps. The score is MAE in Rs lakh. The chart above
        also shows tall Aprils and Julys in both years; they repeat, so a copy of last year carries
        them, and the board's six months, October to March, do not include them.
        """),
        code('''
hold = rev["2026-04":"2026-09"]
months_ahead = pd.Series(range(1, 7), index=hold.index)
naive = pd.Series(rev["2026-03"], index=hold.index)
drift = rev["2026-03"] + months_ahead * (rev["2026-03"] - rev["2024-10"]) / 17   # 17 months, Oct 2024 to Mar 2026

naive_mae = (naive - hold).abs().mean() / 1e5                # misses, signs dropped, averaged: Rs lakh a month
drift_mae = (drift - hold).abs().mean() / 1e5
print(f"naive MAE: Rs {naive_mae:.1f} lakh   drift MAE: Rs {drift_mae:.1f} lakh")
pd.DataFrame({"actual": hold, "naive": naive, "drift": drift}).div(1e5).plot(marker="o", title="Six hidden months, Rs lakh")
plt.show()
check("naive misses by more than Rs 50 lakh a month", naive_mae > 50)
'''),
        md("""
        ## How do the seasonal copy and the vendor score on the same six months?

        **Your turn.** Score the seasonal copy (the same month a year earlier, Kalpa's house bot)
        and the vendor's forecast on the same six months. Type these lines into the empty cell below
        and run them; the vendor's `kind` column says which of its rows are fits and which are
        forecasts for the hidden months:

        ```python
        seasonal = rev.shift(12).loc[hold.index]
        vendor_hold = vendor.loc[hold.index, "vendor_rs"]
        print(vendor.loc[hold.index, "kind"].unique())
        seasonal_mae = (seasonal - hold).abs().mean() / 1e5
        vendor_mae = (vendor_hold - hold).abs().mean() / 1e5
        print(f"seasonal MAE: Rs {seasonal_mae:.1f} lakh   vendor MAE: Rs {vendor_mae:.1f} lakh")
        ```
        """),
        empty(),
        md("""
        ## Which month does each copy put Diwali in this year?

        Diwali 2026 falls on Sunday 8 November. Kalpa's revenue is booked when shoppers buy, in the
        days just before Diwali, so its spike sits in Diwali's own month: October in 2024 and 2025,
        and November in 2026, since the days before 8 November fall in November. Flipkart's
        shipments peaked two weeks earlier because parcels leave the centre in the sale weeks. The
        seasonal copy takes each month from the same month last year. The festival-aligned copy
        swaps two months: this November gets last year's Diwali month, October 2025, and this
        October gets last year's November; then it adds 4 percent.

        **Your turn.** Type these lines into the empty cell below:

        ```python
        months = ["2026-10", "2026-11", "2026-12", "2027-01", "2027-02", "2027-03"]
        year_before = ["2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03"]
        swapped = ["2025-11", "2025-10", "2025-12", "2026-01", "2026-02", "2026-03"]
        table = pd.DataFrame({"same month last year": [rev[m] for m in year_before],
                              "finance: plus 4 percent": [round(rev[m] * 1.04) for m in year_before],
                              "festival-aligned": [round(rev[m] * 1.04) for m in swapped],
                              "vendor": vendor.loc[months, "vendor_rs"].values,
                              "plan line": plan.loc[months].values}, index=months) / 1e5
        print(table.round(1).to_string())
        print((table.sum() / 100).round(2).to_string())          # six months, Rs crore
        ```
        """),
        empty(),
        code('''
growth = rev["2025-10":"2026-09"].sum() / rev["2024-10":"2025-09"].sum() - 1
print(f"the second year grew {growth:.1%} on the first")
print(f"plan line, Oct 2026 to Mar 2027: Rs {plan.sum() / 1e7:.2f} crore")
copy_plus4 = (rev.shift(12).loc[hold.index] * 1.04).round()        # festival-aligned on the hidden months
aligned_mae = (copy_plus4 - hold).abs().mean() / 1e5
print(f"festival-aligned's own miss on Apr to Sep 2026: Rs {aligned_mae:.1f} lakh a month")
(plan / 1e5).plot.bar(color="lavender", edgecolor="slateblue", title="The plan line, Rs lakh a month")
plt.show()
check("the plan line is 15 percent above last year's same months",
      abs(plan.sum() / rev["2025-10":"2026-03"].sum() - 1.15) < 0.001)
'''),
        md("""
        ## What do you bring to the TA, in rupees?

        Anand's board number in one paragraph: the forecast you would send, the month it puts the
        spike in, its error bar in Rs lakh, and the gap to the plan line. The unguided exercise
        `exercises/unguided/C2_W04_D05_kalpa_board_STUDENT.md` asks the same decision in lettered
        items.

        - **The two winters:** October is the biggest month of each.
        - **Naive and drift:** they miss April to September 2026 by Rs 59.4 and Rs 58.8 lakh a month.
        - **The seasonal copy and the vendor:** your first cell.
        - **Diwali this year, and the six months' totals:** your second cell.
        - **The error bar:** festival-aligned, the seasonal copy plus 4 percent, missed the six
          hidden months by Rs 3.5 lakh a month, about Rs 21 lakh if all six miss the same way. No
          hidden month holds Diwali, so the spike month itself is untested.
        - **Why 4 percent:** finance's rule adds 4; the data's own growth, 3.7 percent, is close, so
          festival-aligned keeps finance's 4 percent and differs from it only in the month that
          carries Diwali.
        """),
    ]


if __name__ == "__main__":
    names = [("01_trend_and_seasonality", nb01), ("02_naive_seasonal_naive_drift", nb02),
             ("03_holdout_mae_mape", nb03), ("04_beating_the_baseline_good_enough", nb04),
             ("05_case_shape_and_baselines", nb05), ("06_case_holdout_scoreboard", nb06),
             ("07_case_good_enough_forecast_note", nb07), ("08_kalpa_lab_forecast_note", nb08)]
    keep = {f"C2_W04_D05_{name}_STUDENT.ipynb" for name, _ in names}
    for old in NB.glob("C2_W04_D05_*_STUDENT.ipynb"):
        if old.name not in keep:
            old.unlink()
            print("removed", old.name)
    for name, make in names:
        path = NB / f"C2_W04_D05_{name}_STUDENT.ipynb"
        cells = make()
        build(path, cells)
        print("built", path.name, len(cells), "cells")

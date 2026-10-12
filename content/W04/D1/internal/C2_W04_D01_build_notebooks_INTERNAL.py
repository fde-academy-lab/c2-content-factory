"""Build the four Week 4 Monday notebooks and execute each cold in its own folder.

    python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py          all four
    python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 02 03    some of them

01 counts the twelve rows by hand (14 cells); 02 runs the full driver_weeks, the trap and the
your-turn cell (21 cells); 03 prices the gaming, builds the definition and runs the caveats and the
SQL second route (16 cells); 04 is the Kalpa lab, whose two finding cells ship empty (11 cells).
Plain pandas, the standard library and matplotlib; each notebook defines its own three-line check.
Every number a cell prints sits in internal/C2_W04_D01_facts_INTERNAL.yaml under its id.
"""
import pathlib
import sys

sys.path.insert(0, "scripts")
from nb_make import build, code, empty, md  # noqa: E402

NB = pathlib.Path("content/W04/D1/notebooks")
NB.mkdir(parents=True, exist_ok=True)
LABEL = ("> *Illustrative case: the company is real, the situation and the data are synthetic, "
         "built for this class.*")

TICKET = f"""
**The ticket. Uber, Hyderabad, the driver app's peak-hour earnings guarantee.**

{LABEL}

On Monday 31 August 2026 the Hyderabad city team launched a peak-hour earnings guarantee for
enrolled drivers: a driver who stays online through a whole peak window (two windows a day, each
three hours long, set by the city team) is guaranteed a floor of Rs 300 per peak online hour, and
Uber pays the gap between the driver's trip earnings in the window and the floor as a top-up. The
goal written in the launch note was "more drivers on the road at peak, so riders are picked up
faster". The terms are synthetic.

Six weeks after the launch (the weeks beginning 31 August to 5 October 2026, so 31 August to 11
October) against the six weeks before (the weeks beginning 20 July to 24 August, so 20 July to 30
August):

| Measure | Before | After | Change |
|---|---|---|---|
| Peak online hours, all enrolled drivers | 118,000 | 146,300 | up 24 percent |
| Completed peak trips | 224,200 | 230,900 | up 3 percent |
| Trips per peak online hour | 1.90 | 1.58 | 1.9 to 1.6 |
| Offers accepted over offers shown, at peak | 0.86 | 0.73 | down 13 points |
| Accepted trips the driver then cancelled, share | 0.04 | 0.09 | up 5 points |
| Peak online hours with no completed trip, share | 0.22 | 0.38 | up 16 points |
| Median rider wait at peak, minutes | 4.8 | 4.6 | down 0.2 minutes |
| Rider requests at peak that went unfulfilled, share | 0.11 | 0.10 | down 1 point |
| Top-up paid | Rs 0 | Rs 1.9 crore | |

A point is one hundredth of a share, so 0.86 to 0.73 is 13 points down.

**Data the analyst has.**

| Table | Columns | Rows |
|---|---|---|
| `drivers` | `driver_id`, `home_zone`, `joined_month`, `enrolled` | 1,200 drivers, 140 of them joined after the launch |
| `driver_weeks` | `driver_id`, `week_start`, `zone_mode` (the zone where most online time was), `peak_online_hours`, `peak_offers`, `peak_accepted`, `peak_driver_cancels`, `peak_trips`, `peak_hours_no_trip`, `peak_bookings_rs`, `topup_rs`, `offpeak_trips` | one row for every driver on the app that week, twelve weeks |
| `zone_weeks` | `zone`, `week_start`, `peak_requests`, `peak_fulfilled`, `median_wait_min` | 12 zones by twelve weeks |

A rider's request that one driver declines is offered to the next driver, so `driver_weeks` counts
offers (every time a driver was shown a request) and `zone_weeks` counts rider requests.

**The ask, due Friday, to the city head.** Is the scheme working? Which metric should it pay for? Is
anyone gaming it, and how would we know?

**Known caveats.** The monsoon ended inside the after window. 140 drivers joined after the launch.
The app logs a driver as online whenever the driver app is open and the driver is marked available,
wherever the phone is. The three outer zones (Shamshabad, Rajendranagar, Patancheru) get few
requests at any hour. Drivers can be online on more than one platform at once, and Uber cannot see
the other platforms. A driver's trip earnings (the driver's share of the fares) and the window-by-window
record are not in the tables, so a week's top-up cannot be rebuilt from its bookings.
"""

SETUP = '''
import pandas as pd
import matplotlib.pyplot as plt

def check(name, ok):
    print("PASS" if ok else "FAIL", name)
'''
STYLE = '''
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False, "font.size": 11})
INK, VIOLET, ROSE, LAV, MUTED = "#1A0F5C", "#5B3FD6", "#D63A6A", "#D9A7FF", "#6B6690"
'''


def nb01():
    build(NB / "C2_W04_D01_01_twelve_rows_STUDENT.ipynb", [
        md(f'''
        # What does "peak online hours up 24 percent" stand for, and what happened to six drivers we can count by hand?

        Week 4, Monday, chapter 1 of 3. Level 1 of the day's six, which climb from a hand count (L1)
        to interview depth (L6): read the ticket, say what the number stands for, and count it by
        hand on twelve rows of the case's own data.
        {TICKET}
        **Who needs the answer.** The Hyderabad city head decides on Friday whether the scheme is
        working and whether to extend it. If "hours up 24 percent" is read as "more riders served"
        and it is not, the same top-up goes to two more cities.

        **The questions on the way.**

        1. What happens to a number that stands in for the goal once people are paid for it?
        2. What did six drivers' hours and trips do between one week before and one week after?
        3. What is trips per peak online hour on those twelve rows, before and after?
        4. Which drivers moved it, and why do the six fall further than the city?
        '''),
        md('''
        ## What happens to a number that stands in for the goal once people are paid for it?

        A **proxy** is a number that stands in for the thing somebody wants. A canteen, with
        **invented numbers**, wants plates served to hungry diners and pays its servers per token
        printed, because tokens are easy to count. Tokens go from 200 to 400 a day while plates stay
        at 200, because each plate now gets two tokens.

        **Predict before you run.** What does tokens per plate do? a) stays at 1.0, since plates did
        not change; b) rises to 2.0, since every plate now carries two tokens; c) falls to 0.5;
        d) cannot be told without the menu.

        This cell sets up the notebook and draws the canteen's two numbers side by side.
        '''),
        code(SETUP + STYLE + '''
canteen = pd.DataFrame({"day": ["before", "after"], "tokens": [200, 400], "plates": [200, 200]})
canteen["tokens_per_plate"] = canteen["tokens"] / canteen["plates"]
fig, ax = plt.subplots(figsize=(6.4, 3.2))
ax.bar([0, 1], canteen["tokens"], width=0.35, color=VIOLET, label="tokens printed (the proxy)")
ax.bar([0.38, 1.38], canteen["plates"], width=0.35, color=LAV, label="plates served (the goal)")
ax.set_xticks([0.19, 1.19], ["before", "after"])
ax.set_title("A canteen, invented numbers: the proxy doubled, the goal did not", loc="left")
ax.legend(frameon=False)
plt.show()
canteen
'''),
        md('''
        **What happened.** The answer is b: tokens per plate went from 1.0 to 2.0 and not one more
        diner ate. That is the **proxy test**: could a team hit this number while the thing it
        stands for got worse, or stayed the same? The ticket's "peak online hours" counts an hour
        whenever the driver app is open, so it can fail the same test on the road.

        ## What did six drivers' hours and trips do between one week before and one week after?

        The twelve rows are six drivers, A to F, each in two weeks: the week beginning 10 August 2026
        (before the launch) and the week beginning 21 September 2026 (after). This cell picks those
        twelve driver-weeks out of `driver_weeks`. New in it: `.isin(...)` keeps the rows whose value
        is in a list, `.map(...)` swaps each value for the one a dictionary gives it, and
        `sort_values` puts the rows in order.
        '''),
        code('''
dw = pd.read_csv("../data/C2_W04_D01_driver_weeks_STUDENT.csv")
names = {"d_0001": "A", "d_0002": "B", "d_0003": "C", "d_0004": "D", "d_0881": "E", "d_0882": "F"}
twelve = dw[dw["driver_id"].isin(names) & dw["week_start"].isin(["2026-08-10", "2026-09-21"])].copy()
twelve["driver"] = twelve["driver_id"].map(names)
twelve["week"] = twelve["week_start"].map({"2026-08-10": "before", "2026-09-21": "after"})
twelve = twelve.sort_values(["driver", "week"], ascending=[True, False])
twelve[["driver", "week", "zone_mode", "peak_online_hours", "peak_offers", "peak_accepted", "peak_trips"]]
'''),
        md('''
        **Predict before you run.** On these six drivers, what happens to trips per peak online hour
        between the two weeks? a) holds near 1.9; b) falls to about 1.6, as the city's did; c) falls
        to about 1.2; d) rises above 2.0.

        This cell adds up the hours and the trips in each week, then divides the two sums.
        '''),
        code('''
totals = twelve.groupby("week")[["peak_online_hours", "peak_trips"]].sum().loc[["before", "after"]]
totals["trips_per_hour"] = (totals["peak_trips"] / totals["peak_online_hours"]).round(2)
totals
'''),
        md('''
        **What happened.** The answer is c. The six drivers logged 60 hours and 114 trips before,
        74 hours and 88 trips after: hours up 23 percent, trips down 23 percent, and trips per peak
        online hour from 1.90 to 1.19. The city fell to 1.58, and the six fall further because they
        were chosen to show the mechanism: two of them, E and F, logged hours with almost no trips,
        a third of this sample. How common such drivers are in the city is chapter 2's question.

        ## Which drivers moved the ratio, and in which direction?

        This cell takes each driver's own trips per hour in both weeks and draws one line per driver.
        New in it: `.pivot` turns the two weeks into two columns with one row per driver, and
        `.iterrows()` walks those rows one at a time to draw each line.
        '''),
        code('''
wide = twelve.pivot(index="driver", columns="week", values=["peak_online_hours", "peak_trips"])
rate = (wide["peak_trips"] / wide["peak_online_hours"]).round(2)[["before", "after"]]
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for driver, row in rate.iterrows():
    colour = ROSE if driver in "EF" else VIOLET
    ax.plot([0, 1], [row["before"], row["after"]], marker="o", color=colour)
    ax.text(1.04, row["after"], driver, color=colour, va="center")
ax.set_xticks([0, 1], ["week of 10 Aug", "week of 21 Sep"])
ax.set_ylim(0, 2.4)
ax.set_ylabel("trips per peak online hour")
ax.set_title("Four drivers held near 2; E and F fell close to zero", loc="left")
plt.show()
rate
'''),
        md('''
        **What happened.** A to D held between 1.80 and 2.10 trips an hour. E went from 10 hours and
        18 trips to 16 hours and 3 trips, accepting 4 of the 14 offers it was shown; F went from 10
        hours and 17 trips to 14 hours and 2 trips, accepting 3 of 12. Both sit in outer zones
        (Shamshabad and Rajendranagar), where riders ask for few trips at any hour. Their hours went
        up and their trips nearly vanished: the proxy rose while the thing it stands for fell.

        This cell draws the six drivers' hours and trips as two pairs of bars, the picture the
        hand count makes.
        '''),
        code('''
fig, ax = plt.subplots(figsize=(6.4, 3.4))
ax.bar([0, 1], totals["peak_online_hours"], width=0.35, color=VIOLET, label="peak online hours")
ax.bar([0.38, 1.38], totals["peak_trips"], width=0.35, color=LAV, label="completed peak trips")
for x, v in zip([0, 1, 0.38, 1.38], list(totals["peak_online_hours"]) + list(totals["peak_trips"])):
    ax.text(x, v + 2, str(v), ha="center")
ax.set_xticks([0.19, 1.19], ["before", "after"])
ax.set_title("Six drivers: hours up 23 percent, trips down 23 percent", loc="left")
ax.legend(frameon=False, loc="upper left")
plt.show()
'''),
        md('''
        This cell checks the claims the chapter makes about its own numbers.
        '''),
        code('''
check("the canteen's tokens per plate went from 1.0 to 2.0", list(canteen["tokens_per_plate"]) == [1.0, 2.0])
check("the twelve rows are six drivers in two weeks", len(twelve) == 12 and twelve["driver"].nunique() == 6)
check("hours 60 before and 74 after", list(totals["peak_online_hours"]) == [60, 74])
check("trips 114 before and 88 after", list(totals["peak_trips"]) == [114, 88])
check("trips per peak online hour 1.90 before and 1.19 after", list(totals["trips_per_hour"]) == [1.90, 1.19])
check("E and F fell below 0.25 trips an hour after the launch", (rate.loc[["E", "F"], "after"] < 0.25).all())
'''),
        md('''
        ## What does chapter 1 answer?

        1. A paid proxy drifts: the canteen's tokens doubled while plates stayed at 200 (invented).
        2. The six drivers' hours rose from 60 to 74 while their trips fell from 114 to 88.
        3. Trips per peak online hour on the twelve rows fell from 1.90 to 1.19.
        4. E and F moved it: their hours rose while their trips fell to 3 and 2. The six fall further
           than the city's 1.58 because they were chosen to show the mechanism.

        **The check a senior analyst runs before trusting a rate.** Read its baseline (1.90 before),
        its denominator (hours the app was open, which a driver controls) and the evidence that the
        thing it stands for moved (trips rose only 3 percent across the city).

        **In the interview.** [S] How would you measure the success of a new feature? ([S] tags a
        staple question; [F] tags one frequent in product interviews.) A hire-grade
        answer starts from what the feature is for and names a number that cannot rise while that
        thing gets worse. Notebook 02 runs the same count on all 12,860 driver-weeks.
        '''),
    ])


def nb02():
    build(NB / "C2_W04_D01_02_full_data_trap_STUDENT.ipynb", [
        md(f'''
        # What do the city totals say over twelve weeks, and which drivers and zones drive the fall?

        Week 4, Monday, chapter 2 of 3. Levels 2 and 3 of the day's six: the same count on the full
        data in the smallest code, then the trap, the denominator and the segment that drives the
        number. New in the setup cell: `.lt("2026-08-31")` asks whether each week starts before the
        launch, and `.map` turns True and False into before and after.

        **The case.** Uber's Hyderabad city team launched a peak-hour earnings guarantee on Monday
        31 August 2026, a floor of Rs 300 per peak online hour with Uber paying the gap as a top-up.
        Peak online hours rose 24 percent over the six weeks after the launch, completed peak trips 3
        percent, and the city head asks whether the scheme is working, what it should pay for and
        whether anyone is gaming it.

        {LABEL}

        Notebook 01 counted six drivers by hand: their hours rose from 60 to 74, their trips fell from
        114 to 88, and trips per peak online hour fell from 1.90 to 1.19, pulled down by two drivers in
        outer zones. This notebook runs the count on every driver-week.

        **Who needs the answer.** The city head, before a proposal to extend the scheme to two more
        cities goes out. A fall read as weak demand, or measured with the wrong denominator, sends the
        same top-up further.

        **The questions on the way.**

        1. What are the city's totals before and after the launch?
        2. Did rider demand fall?
        3. What does a quick average of each driver-week's rate say, and why is it wrong?
        4. Which drivers sit under 1.0 trip per peak online hour after the launch?
        5. Where did their new hours go, and does a second route find the same drivers?
        '''),
        code(SETUP + STYLE + '''
dw = pd.read_csv("../data/C2_W04_D01_driver_weeks_STUDENT.csv")
zw = pd.read_csv("../data/C2_W04_D01_zone_weeks_STUDENT.csv")
dw["window"] = dw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
zw["window"] = zw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
print(f"{len(dw):,} driver-weeks and {len(zw)} zone-weeks, twelve weeks from {dw.week_start.min()}")
'''),
        md('''
        ## What are the city's totals before and after the launch?

        A rate is a ratio of two sums: add up every trip, add up every hour, then divide. This cell
        sums the six weeks on each side of the launch and takes each rate that way.
        '''),
        code('''
city = dw.groupby("window")[["peak_online_hours", "peak_trips", "peak_offers", "peak_accepted",
                             "peak_driver_cancels", "peak_hours_no_trip"]].sum().loc[["before", "after"]]
city["trips_per_hour"] = (city["peak_trips"] / city["peak_online_hours"]).round(2)
city["acceptance"] = (city["peak_accepted"] / city["peak_offers"]).round(3)
city["driver_cancel_share"] = (city["peak_driver_cancels"] / city["peak_accepted"]).round(3)
city["no_trip_share"] = (city["peak_hours_no_trip"] / city["peak_online_hours"]).round(2)
city.T
'''),
        md('''
        **What happened.** Peak online hours rose from 118,000 to 146,300 and completed peak trips from
        224,200 to 230,900, so trips per peak online hour fell from 1.90 to 1.58. The share of offers
        accepted fell from 0.863 to 0.730, the share of accepted trips the driver then cancelled rose
        from 0.037 to 0.090, and the share of online hours with no completed trip rose from 0.22 to
        0.38.

        ## Did rider demand fall?

        If riders asked for fewer trips, trips per online hour would fall with nobody gaming
        anything. Demand lives in `zone_weeks`, which counts rider requests.

        **Predict before you run.** From the six weeks before to the six weeks after, rider requests
        a) fell by about a tenth; b) held about level; c) rose a little; d) rose by a quarter, as
        hours did.

        This cell sums requests and fulfilled requests by window, takes the city's wait as the median
        of the 72 zone-week median waits in each window (12 zones for six weeks), and sets offers
        beside requests. New in it: `.agg(name=(column, "sum"))` makes several named totals in one
        step.
        '''),
        code('''
demand = zw.groupby("window").agg(requests=("peak_requests", "sum"), fulfilled=("peak_fulfilled", "sum"),
                                  median_wait=("median_wait_min", "median")).loc[["before", "after"]]
demand["unfulfilled_share"] = (1 - demand["fulfilled"] / demand["requests"]).round(2)
demand["offers_per_request"] = (city["peak_offers"] / demand["requests"]).round(2)
demand
'''),
        md('''
        **What happened.** The answer is c: rider requests rose from 251,910 to 256,556, up 1.8
        percent, and the share left unfulfilled went from 0.11 to 0.10, while the median wait moved
        from 4.8 to 4.6 minutes. The fall is not demand. Offers per request rose from 1.07 to 1.35,
        because a request that one driver declines is offered to the next and counted again in
        `driver_weeks`: more declining shows up as more offers for the same riders.

        This cell draws the twelve weeks, hours on the left axis and trips per hour on the right
        (`ax.twinx()` adds the second axis), to
        see whether the after window is two odd weeks or a level that held.
        '''),
        code('''
weekly = dw.groupby("week_start")[["peak_online_hours", "peak_trips"]].sum()
weekly["trips_per_hour"] = weekly["peak_trips"] / weekly["peak_online_hours"]
fig, ax = plt.subplots(figsize=(8.0, 3.8))
ax.plot(range(12), weekly["peak_online_hours"], marker="o", color=VIOLET)
ax.set_ylabel("peak online hours", color=VIOLET)
right = ax.twinx()
right.plot(range(12), weekly["trips_per_hour"], marker="s", color=ROSE)
right.set_ylabel("trips per peak online hour", color=ROSE)
right.spines["right"].set_visible(True)
ax.axvline(5.5, color=MUTED, linestyle="--")
ax.set_xticks(range(12), [w[5:] for w in weekly.index], rotation=45)
ax.set_title("Hours jumped at the launch; trips per hour fell and stayed down", loc="left")
plt.show()
weekly["trips_per_hour"].round(2).to_frame().T
'''),
        md('''
        **What happened.** Before the launch, trips per hour wandered between 1.88 and 1.93. In the
        launch week it read 1.64, and from then on it stayed between 1.55 and 1.59. Hours rose from
        about 20,000 a week to about 24,000. The fall held for six weeks.

        ## What does a quick average of each driver-week's rate say?

        **The plausible wrong answer.** A colleague in a hurry works out trips per hour for each
        driver-week, then takes the plain average of those rates for each window.

        **Predict before you run.** What does that average print for the after window? a) 1.58;
        b) 1.71; c) 1.19; d) 1.90.

        This cell computes the colleague's number beside the ratio of the sums.
        '''),
        code('''
online = dw[dw["peak_online_hours"] > 0].copy()
online["rate"] = online["peak_trips"] / online["peak_online_hours"]
compare = pd.DataFrame({"mean_of_rates": online.groupby("window")["rate"].mean().round(2),
                        "ratio_of_sums": city["trips_per_hour"]}).loc[["before", "after"]]
compare
'''),
        md('''
        **Why it is wrong.** The answer is b: the average of rates prints 1.71, against 1.58 from the
        sums. The true fall is 0.32, from 1.90 to 1.58; the average shows 0.19 of it and hides 0.13,
        about two-fifths. An average of rates gives a 42-hour driver-week the same weight as a 10-hour
        one, so the long, slow weeks of the drivers online longest count no more than anyone's short,
        busy ones. With **invented numbers**: a driver at 2.0 trips an hour for 10 hours (20 trips)
        and a driver at 0.5 for 40 hours (20 trips) made 40 trips in 50 hours, which is 0.80 an hour,
        while the average of their two rates is 1.25: too high, in the same direction as the city's
        1.71. The fix is the ratio of the sums, with its denominator named: trips per peak online
        hour, all hours in the window.

        ## Which drivers sit under 1.0 trip per peak online hour after the launch?

        **Predict before you run.** Of the 1,200 drivers, how many made fewer than one trip per peak
        online hour across the six weeks after the launch? a) about 30; b) about 100; c) about 180;
        d) about 400.

        **Your turn.** Type these lines into the empty cell below and run it:

        ```python
        after = dw[dw["window"] == "after"]
        per_driver = after.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
        per_driver["rate"] = per_driver["peak_trips"] / per_driver["peak_online_hours"]
        (per_driver["rate"] < 1.0).sum()
        ```
        '''),
        empty(),
        md('''
        Your cell prints a count of drivers. The next cell builds the same group so the rest of the
        notebook can use it, and sets their hours and trips before and after; `:.0%` prints a share as
        a whole percent.
        '''),
        code('''
after = dw[dw["window"] == "after"]
per_driver = after.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
slow = set(per_driver.index[per_driver["peak_trips"] / per_driver["peak_online_hours"] < 1.0])
tail = dw[dw["driver_id"].isin(slow)].groupby("window")[["peak_online_hours", "peak_trips"]].sum()
tail = tail.loc[["before", "after"]]
print(f"{len(slow)} drivers, {len(slow) / 1200:.0%} of the 1,200")
print("hours, after over before:", round(tail.loc["after", "peak_online_hours"] / tail.loc["before", "peak_online_hours"], 2))
print("trips, after over before:", round(tail.loc["after", "peak_trips"] / tail.loc["before", "peak_trips"], 2))
'''),
        md('''
        **What happened.** The answer is c: 180 drivers, 15 percent of the 1,200. Their peak online
        hours after the launch were 2.1 times their hours before, while their trips were 0.88 times,
        down 12 percent. Call them the **idle tail**: drivers who stayed online without driving. The
        six of chapter 1 held two such drivers, a third of the sample against 15 percent city-wide,
        which is why the six fell to 1.19 while the city fell to 1.58.

        ## Where did the idle tail's new hours go?

        This cell compares the idle tail's hours in the three outer zones before and after, then
        draws every driver-week after the launch, hours against trips.
        '''),
        code('''
OUTER = ["Shamshabad", "Rajendranagar", "Patancheru"]
idle = dw[dw["driver_id"].isin(slow)]
outer_hours = idle[idle["zone_mode"].isin(OUTER)].groupby("window")["peak_online_hours"].sum()
new_hours = tail.loc["after", "peak_online_hours"] - tail.loc["before", "peak_online_hours"]
outer_share = (outer_hours["after"] - outer_hours["before"]) / new_hours
print(f"new hours {new_hours:,}; share logged in the outer zones {outer_share:.2f}")
mark = after["driver_id"].isin(slow)
fig, ax = plt.subplots(figsize=(7.4, 4.2))
ax.scatter(after.loc[~mark, "peak_online_hours"], after.loc[~mark, "peak_trips"], s=6, color=LAV,
           label="every other driver-week")
ax.scatter(after.loc[mark, "peak_online_hours"], after.loc[mark, "peak_trips"], s=8, color=ROSE,
           label="the idle tail's driver-weeks")
ax.plot([0, 36], [0, 36 * 1.9], linestyle=":", color=VIOLET, label="1.9 trips per hour")
ax.set_xlim(0, 45)
ax.set_xlabel("peak online hours in the week")
ax.set_ylabel("completed peak trips")
ax.set_title("After the launch: the idle tail sits far right and low", loc="left")
ax.legend(frameon=False)
plt.show()
'''),
        md('''
        **What happened.** The idle tail logged 22,000 new hours, and 72 percent of them sat in the
        three outer zones, where requests are thin at any hour: a driver parked there stays online,
        is shown few requests, and is paid the floor. A week holds at most 42 peak hours (two
        three-hour windows a day, seven days), and many idle-tail weeks sit near that edge.

        ## Does a second route find the same drivers?

        The first route sorted drivers by trips per hour. The second ignores trips and asks only how
        often each driver accepted what the app offered: this cell keeps every driver whose accepted
        share stayed under 0.5 in every week they worked after the launch, then draws requests by
        zone to show how thin the outer zones are.
        '''),
        code('''
weeks_after = after[after["peak_offers"] > 0]
low_every_week = (weeks_after["peak_accepted"] / weeks_after["peak_offers"] < 0.5).groupby(weeks_after["driver_id"]).all()
second = set(low_every_week.index[low_every_week])
print(f"{len(second)} drivers by acceptance; the same drivers as the first route: {second == slow}")
by_zone = zw.groupby("zone")["peak_requests"].sum().sort_values()
fig, ax = plt.subplots(figsize=(7.4, 3.8))
ax.barh(by_zone.index, by_zone.values, color=[ROSE if z in OUTER else VIOLET for z in by_zone.index])
ax.set_xlabel("rider requests at peak, twelve weeks")
ax.set_title("The three outer zones get a fraction of the requests", loc="left")
plt.show()
'''),
        code('''
check("hours 118,000 before and 146,300 after", list(city["peak_online_hours"]) == [118000, 146300])
check("trips per peak online hour 1.90 before and 1.58 after", list(city["trips_per_hour"]) == [1.90, 1.58])
check("rider requests rose, 251,910 to 256,556", list(demand["requests"]) == [251910, 256556])
check("the average of rates prints 1.71 after, above the true 1.58", compare.loc["after", "mean_of_rates"] == 1.71)
check("180 drivers under 1.0 trip per hour after the launch", len(slow) == 180)
check("the idle tail's hours 2.1 times, trips 0.88 times",
      round(tail.loc["after", "peak_online_hours"] / tail.loc["before", "peak_online_hours"], 2) == 2.1
      and round(tail.loc["after", "peak_trips"] / tail.loc["before", "peak_trips"], 2) == 0.88)
check("72 percent of the new hours in the outer zones", round(outer_share, 2) == 0.72)
check("the acceptance route finds the same 180 drivers", second == slow)
'''),
        md('''
        ## What does chapter 2 answer?

        1. Hours rose from 118,000 to 146,300 and trips from 224,200 to 230,900: 1.90 to 1.58 trips an hour.
        2. Demand did not fall: rider requests rose 1.8 percent, and waits moved from 4.8 to 4.6 minutes.
        3. An average of each week's rate prints 1.71 and hides two-fifths of the fall; the ratio of
           the sums, 1.58, is the number.
        4. 180 drivers, 15 percent, sit under 1.0 trip an hour after the launch, with hours 2.1 times
           and trips 0.88 times their level before.
        5. 72 percent of their new hours sat in the three thin outer zones, and the acceptance route
           finds the same 180 drivers.

        **The check a senior analyst runs.** Before celebrating hours, set the baseline (1.90) beside
        the new rate (1.58), name the denominator (hours the app was open), look for the evidence in
        a second table (rider requests rose), and reach the segment a second way (acceptance finds
        the same 180).

        **In the interview.** [F] What makes a metric gameable? The measured person controls the
        count: here a driver decides when the app is open. Notebook 03 prices what that cost and
        writes the number the scheme should pay for.
        '''),
    ])


def nb03():
    build(NB / "C2_W04_D01_03_definition_and_cost_STUDENT.ipynb", [
        md(f'''
        # Which number should the scheme pay for, what did paying for hours cost, and what can the data not show?

        Week 4, Monday, chapter 3 of 3. Levels 3 to 5: the trap priced in rupees, the definition that
        resists it, the caveats an engineer names aloud, and a second route in SQL.

        **The case.** Uber's Hyderabad city team launched a peak-hour earnings guarantee on Monday
        31 August 2026: a floor of Rs 300 per peak online hour, with Uber paying the gap between a
        driver's trip earnings and the floor as a top-up. Six weeks on, peak online hours are up 24
        percent, completed peak trips up 3 percent, and the top-up has cost Rs 1.9 crore.

        {LABEL}

        Notebook 02 found the fall in the full data: trips per peak online hour fell from 1.90 to 1.58
        while rider requests rose, and 180 drivers (15 percent) logged 2.1 times their hours with 12
        percent fewer trips, 72 percent of their new hours in the three thin outer zones.

        **Who needs the answer.** The city head, who must say by Friday what the scheme pays for, and
        the finance partner, who holds the top-up budget. A scheme that keeps paying for hours keeps
        paying drivers to sit online in zones with no riders.

        **The questions on the way.**

        1. How much of the Rs 1.9 crore went to driver-weeks that accepted fewer than half their offers?
        2. What would the redesign save, under a stated assumption about how drivers respond?
        3. What do the north star and its three guardrails read, before and after?
        4. Which number moved first?
        5. Which doubts does the fall survive, and which stay open?
        6. Does SQL reach the same totals as pandas?
        '''),
        code(SETUP + STYLE + '''
dw = pd.read_csv("../data/C2_W04_D01_driver_weeks_STUDENT.csv")
zw = pd.read_csv("../data/C2_W04_D01_zone_weeks_STUDENT.csv")
dw["window"] = dw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
zw["window"] = zw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
after = dw[dw["window"] == "after"].copy()
after["acceptance"] = after["peak_accepted"] / after["peak_offers"]
print(f"{len(after):,} driver-weeks after the launch; top-up paid Rs {after['topup_rs'].sum() / 1e7:.2f} crore")
'''),
        md('''
        ## How much of the Rs 1.9 crore went to driver-weeks that accepted fewer than half their offers?

        **Predict before you run.** What share of the top-up went to driver-weeks whose accepted share
        was under 0.5? a) 15 percent; b) 39 percent; c) 61 percent; d) 88 percent.

        This cell splits the top-up at an accepted share of 0.5 and draws the two parts.
        '''),
        code('''
low = after.loc[after["acceptance"] < 0.5, "topup_rs"].sum()
high = after.loc[after["acceptance"] >= 0.5, "topup_rs"].sum()
fig, ax = plt.subplots(figsize=(7.0, 2.6))
ax.barh(["accepted under 0.5", "accepted 0.5 or more"], [low / 1e5, high / 1e5], color=[ROSE, VIOLET])
for y, v in enumerate([low, high]):
    ax.text(v / 1e5 + 2, y, f"Rs {v / 1e5:.0f} lakh", va="center")
ax.set_xlabel("top-up paid over six weeks, Rs lakh")
ax.set_title("Where the Rs 1.9 crore top-up went", loc="left")
plt.show()
print(f"share to driver-weeks under 0.5: {low / (low + high):.2f}")
'''),
        md('''
        **What happened.** The answer is c: Rs 1.159 crore, 61 percent of the Rs 1.9 crore, went to
        driver-weeks that accepted fewer than half the offers they were shown, and Rs 74 lakh went to
        the rest. Had only the driver-weeks at or above 0.5 been paid, and had every driver behaved the
        same, the six weeks would have cost Rs 74 lakh. A new rule changes behaviour, so Rs 74 lakh is
        the least the six weeks would have cost under it.

        ## What would the redesign save, under a stated assumption about how drivers respond?

        The driver-weeks under 0.5 are the idle tail's: its highest week after the launch accepted
        0.46 of its offers and every other driver's lowest accepted 0.78, so the Rs 1.159 crore is the
        idle tail's top-up. Some idle-tail drivers would start accepting enough to qualify under a rule
        that pays for trips. The share of the idle tail's top-up that would still be paid is an **assumption**:
        0.2 at the low end, 0.5 at the high end. A test of the redesign, which this afternoon's
        tentative faculty block designs, is what settles it. This cell prices both ends.
        '''),
        code('''
saving = pd.DataFrame({"still_paid_share": [0.2, 0.5]})
saving["saving_rs"] = (low * (1 - saving["still_paid_share"])).round()
saving["saving_lakh"] = (saving["saving_rs"] / 1e5).round(1)
saving
'''),
        md('''
        **What happened.** If a fifth of the idle tail's top-up were still paid, the redesign saves
        Rs 92.7 lakh over six weeks; if half were, Rs 58.0 lakh. The range is the honest answer to
        finance until the test reports.

        ## What do the north star and its three guardrails read, before and after?

        The redesign's definition, line by line:

        | Line | What it says |
        |---|---|
        | Numerator | Trips completed inside the peak windows, one per paying rider: Uber's annual report counts an UberX Share ride with three paying riders as three trips |
        | Denominator | Enrolled drivers online at least one peak hour that week, with the count printed beside the rate |
        | Window | The calendar week |
        | Exclusions | Trips cancelled by either side, test accounts, trips outside the windows |
        | What it does not reward | Hours online; offers declined; a shrinking enrolled base, since fewer drivers in the count would raise the rate with no extra trip |
        | Guardrails | For riders: offers accepted over offers shown, at or above a floor the city sets, and the median rider wait at peak. For the budget: top-up per completed trip |
        | Gaming note | Guardrail 1 catches declining and cherry-picking; guardrail 2, supply that stops serving riders; guardrail 3, a top-up that runs away from the trips it pays for |

        This cell computes the north star and the three guardrails for each window.
        '''),
        code('''
online = dw[dw["peak_online_hours"] > 0]
board = pd.DataFrame({
    "north_star_trips_per_online_driver_week": (online.groupby("window")["peak_trips"].sum()
                                                / online.groupby("window").size()).round(2),
    "online_driver_weeks": online.groupby("window").size(),
    "acceptance": (dw.groupby("window")["peak_accepted"].sum() / dw.groupby("window")["peak_offers"].sum()).round(3),
    "median_wait": zw.groupby("window")["median_wait_min"].median(),
    "topup_per_trip_rs": (dw.groupby("window")["topup_rs"].sum() / dw.groupby("window")["peak_trips"].sum()).round(1),
}).loc[["before", "after"]]
board.T
'''),
        md('''
        **What happened.** The north star read 35.76 trips per online driver-week before and 35.89
        after: hours rose 24 percent and the number the scheme exists for barely moved. Acceptance
        fell from 0.863 to 0.730, the median wait went from 4.8 to 4.6 minutes, and the top-up cost
        Rs 82.3 per completed trip after the launch, against nothing before.

        ## Which number moved first?

        A **leading** input moves before the number the plan is judged on; a **lagging** one confirms
        it later. This cell draws the weekly share of offers accepted beside bookings per online hour.
        '''),
        code('''
wk = dw.groupby("week_start")[["peak_accepted", "peak_offers", "peak_bookings_rs", "peak_online_hours"]].sum()
wk["acceptance"] = wk["peak_accepted"] / wk["peak_offers"]
wk["rs_per_hour"] = wk["peak_bookings_rs"] / wk["peak_online_hours"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.0, 3.2))
a1.plot(range(12), wk["acceptance"], marker="o", color=VIOLET)
a1.set_title("Offers accepted, share", loc="left")
a2.plot(range(12), wk["rs_per_hour"], marker="s", color=ROSE)
a2.set_title("Bookings per online hour, Rs", loc="left")
for a in (a1, a2):
    a.axvline(5.5, color=MUTED, linestyle="--")
    a.set_xticks([0, 6, 11], ["20 Jul", "31 Aug", "5 Oct"])
plt.show()
wk.loc[["2026-08-31", "2026-09-07", "2026-09-14"], ["acceptance", "rs_per_hour"]].round(3)
'''),
        md('''
        **What happened.** Acceptance dropped to its new level in the launch week (0.729) and stayed
        there; bookings per online hour fell to Rs 271 in the launch week and kept falling to Rs 262
        and Rs 259 over the next two. Acceptance settled two weeks before bookings per hour did, which
        is what a leading input is for: a city team watching it would have seen the gaming in week one.

        ## Which doubts does the fall survive, and which stay open?

        **Predict before you run.** Take out the 140 drivers who joined after the launch. What does
        trips per peak online hour read for the six weeks after? a) 1.90; b) 1.79; c) 1.58; d) 1.19.

        This cell restates the after-window rate under each cut the data can make. New in it: a
        dictionary holds each slice of the table under its name, and
        `{name: ... for name, d in slices.items()}` runs the same division, trips over hours, on every
        slice; `.nlargest(3)` picks the three weeks with the most requests, and the drivers who joined
        before the launch are the ids up to `d_1060`.
        '''),
        code('''
OUTER = ["Shamshabad", "Rajendranagar", "Patancheru"]
busiest = zw.groupby("week_start")["peak_requests"].sum().nlargest(3).index
slices = {
    "before, every driver": dw[dw["window"] == "before"],
    "after, every driver": after,
    "after, drivers who joined before the launch": after[after["driver_id"] <= "d_1060"],
    "after, the three weeks with most requests": dw[dw["week_start"].isin(busiest)],
    "after, core zones only": after[~after["zone_mode"].isin(OUTER)],
}
cuts = pd.Series({name: round(d["peak_trips"].sum() / d["peak_online_hours"].sum(), 2)
                  for name, d in slices.items()})
fig, ax = plt.subplots(figsize=(7.4, 3.2))
ax.barh(cuts.index[::-1], cuts.values[::-1], color=[VIOLET, VIOLET, VIOLET, ROSE, LAV])
ax.set_xlim(0, 2.2)
ax.set_xlabel("trips per peak online hour")
ax.set_title("The fall under each cut the data can make", loc="left")
plt.show()
cuts
'''),
        md('''
        **What happened.** The answer is c: without the 140 new drivers the rate after the launch is
        still 1.58, so the new drivers do not explain the fall. In the three weeks with the most rider
        requests of all twelve (the first three after the launch, still in the rains) the rate was
        already 1.60, so the monsoon's end cannot explain the fall: demand was at its highest and the
        fall was there. In the nine core zones the rate fell from 1.90 to 1.79, so most of the fall
        sits in the three outer zones. Three doubts stay open: drivers on two apps (the data holds
        weekly totals, so it cannot show a decline made because another app's trip was under way),
        who chose to enrol (every driver here enrolled, so no group stayed out to compare with), and
        cause (only a test of the redesign settles whether the scheme or the season moved the
        number).

        ## Does SQL reach the same totals as pandas?

        This cell loads `driver_weeks` into an in-memory SQLite database (a small database that lives
        inside Python) and sums the same columns with one `GROUP BY`, then compares the two routes;
        `1.0 *` makes SQL divide with decimals.
        '''),
        code('''
import sqlite3
con = sqlite3.connect(":memory:")
dw.to_sql("driver_weeks", con, index=False)
sql = pd.read_sql("""
    SELECT window, SUM(peak_online_hours) AS hours, SUM(peak_trips) AS trips,
           ROUND(1.0 * SUM(peak_trips) / SUM(peak_online_hours), 2) AS trips_per_hour
    FROM driver_weeks GROUP BY window ORDER BY window DESC""", con).set_index("window")
sql
'''),
        code('''
check("61 percent of the top-up went to driver-weeks under 0.5", round(low / (low + high), 2) == 0.61)
check("Rs 1.159 crore and Rs 74 lakh", (low, high) == (11590000, 7410000))
check("the north star reads 35.76 before and 35.89 after", list(board.iloc[:, 0]) == [35.76, 35.89])
check("acceptance settled in the launch week at 0.729", round(wk.loc["2026-08-31", "acceptance"], 3) == 0.729)
check("the fall survives without the 140 new drivers", cuts["after, drivers who joined before the launch"] == 1.58)
check("the three weeks with most requests already read 1.60", cuts["after, the three weeks with most requests"] == 1.60)
check("SQL and pandas agree on hours and trips", list(sql["hours"]) == [118000, 146300] and list(sql["trips"]) == [224200, 230900])
'''),
        md('''
        ## What does chapter 3 answer?

        1. Rs 1.159 crore, 61 percent of the top-up, went to driver-weeks that accepted fewer than
           half their offers; Rs 74 lakh went to the rest.
        2. Under a stated assumption about how idle drivers respond, the redesign saves Rs 92.7 lakh
           over six weeks if a fifth of the idle tail's top-up is still paid and Rs 58 lakh if half
           is; the test settles where.
        3. The north star barely moved (35.76 to 35.89 trips per online driver-week); acceptance fell
           from 0.863 to 0.730, waits went from 4.8 to 4.6 minutes, and the top-up cost Rs 82.3 a trip.
        4. Acceptance settled in the launch week, two weeks before bookings per hour did.
        5. The fall survives the new drivers (1.58) and the three weeks with most requests (1.60);
           drivers on two apps, who chose to enrol and cause stay open.
        6. SQL's `GROUP BY` returns the same hours and trips as pandas.

        **The check a senior analyst runs.** Price the trap in rupees, write every line of the
        definition, name what the data cannot show and the fact that would settle it, and reach the
        totals a second way before anything leaves the team.

        **In the interview.** [F] North star against guardrail, with one example pair: completed
        peak trips per enrolled driver per week, guarded by the share of offers accepted, which
        catches a driver who stays online and declines. The tentative faculty block this afternoon
        designs the test that would settle cause.
        '''),
    ])


def nb04():
    build(NB / "C2_W04_D01_04_kalpa_lab_STUDENT.ipynb", [
        md('''
        # Does "reorders per member" reward what the head of Retail-Plus needs from the tier?

        Week 4, Monday, the TA-led practice lab. The method of the morning, moved to Kalpa Retail,
        the programme's fictional client: Kalpa and its people are invented, and the data are
        synthetic.

        **The situation.** The head of Retail-Plus, who owns Kalpa's paid membership tier, wants a
        growth number for the tier: reorders placed per member. The app can place a reorder on its own
        (an auto-reorder) as well as when a member taps it, and an auto-reorder window ran from 10 to
        30 September 2026. The comparison is the three weeks before it, 20 August to 9 September 2026;
        both sit after the monsoon sale's last day, 19 August. The table `kalpa_app_reorders` has one
        row per reorder placement: `reorder_id`, `customer_id`, `placed_ts`, `product_id`, `value_rs`
        (the reorder's booked value, whatever happened to it), `auto` (True when the app placed it on
        its own) and `status`: delivered, cancelled, merged (its items joined the member's next order)
        or pending.

        **Who needs the answer.** The head of Retail-Plus, who is about to take "reorders per member"
        to the growth review, the meeting where each team's numbers are judged, as the tier's number. If it can rise while the tier earns less, the
        review rewards the app for placing orders nobody receives.

        **The questions on the way.**

        1. What does the table hold, before anything is counted?
        2. What do seven members' rows say, counted by hand?
        3. What do reorders placed per member and booked value per member do across the two windows?
        4. Which reorders are these, and what happened to them?
        '''),
        code(SETUP + STYLE + '''
members = pd.read_csv("../data/C2_W04_D01_kalpa_members_STUDENT.csv")
reorders = pd.read_csv("../data/C2_W04_D01_kalpa_app_reorders_STUDENT.csv")
reorders["day"] = reorders["placed_ts"].str[:10]
print(f"{len(members)} Retail-Plus members; {len(reorders)} reorder placements from {reorders.day.min()} to {reorders.day.max()}")
'''),
        md('''
        ## What does the table hold, before anything is counted?

        This cell draws three plain views of the whole table, both windows together: what a
        placement is worth, how many each member made, and when the members joined the tier.
        '''),
        code('''
fig, ax = plt.subplots(figsize=(6.4, 2.8))
ax.hist(reorders["value_rs"], bins=30, color=VIOLET)
ax.set_xlabel("booked value of one placement, Rs")
ax.set_title("What a placement is worth, both windows together", loc="left")
plt.show()
fig, ax = plt.subplots(figsize=(6.4, 2.8))
ax.hist(reorders.groupby("customer_id").size(), bins=range(0, 16), color=LAV, edgecolor="white")
ax.set_xlabel("placements per member, both windows together")
ax.set_title("How many placements each member made", loc="left")
plt.show()
fig, ax = plt.subplots(figsize=(6.4, 2.8))
members["member_since"].str[:7].value_counts().sort_index().plot.bar(ax=ax, color=MUTED)
ax.set_title("When the 120 members joined Retail-Plus", loc="left")
plt.show()
'''),
        md('''
        ## What do seven members' rows say, counted by hand?

        Your TA hands out a sheet with seven members' placements and booked values in the two
        windows: RP-0002, RP-0012, RP-0014, RP-0021, RP-0023, RP-0031 and RP-0040. Before the ratio
        code runs, add up each window's placements and booked value for the seven, divide by seven,
        and write the two ratios (window over comparison) on the sheet. The seven cancels out of each
        ratio, so the per-member form gives the same answer as the totals; it is the form the head of
        Retail-Plus reports. Working without the sheet, type these two lines into the empty cell
        below first and run them, where False is the comparison window and True the auto-reorder
        window:

        ```python
        seven = ["RP-0002", "RP-0012", "RP-0014", "RP-0021", "RP-0023", "RP-0031", "RP-0040"]
        print(reorders[reorders["customer_id"].isin(seven)].groupby(["customer_id", reorders["day"] >= "2026-09-10"])["value_rs"].agg(["size", "sum"]))
        ```

        ## What do reorders placed per member and booked value per member do across the two windows?

        **Predict before you run.** From the comparison window to the auto-reorder window, reorders
        placed per member a) fell; b) held about level; c) rose by up to a third; d) rose by more than
        a third. And booked value per member a) fell; b) held about level; c) rose by up to a third;
        d) rose by more than a third.

        **Your turn.** Then type these lines into the same empty cell and run it again:

        ```python
        comparison = reorders[reorders["day"].between("2026-08-20", "2026-09-09")]
        window = reorders[reorders["day"].between("2026-09-10", "2026-09-30")]
        placed = (len(window) / 120) / (len(comparison) / 120)
        booked = window["value_rs"].sum() / comparison["value_rs"].sum()
        print(round(placed, 2), round(booked, 2))
        ```

        `.between(start, end)` keeps the days from the first date to the second, both included.
        '''),
        empty(),
        md('''
        ## Which reorders are these, and what happened to them?

        **Your turn.** Type these lines into the empty cell below and run it, then say in one
        sentence to your neighbour what the window's placements were and what became of them:

        ```python
        print(window.groupby(["auto", "status"]).size())
        print(comparison.groupby(["auto", "status"]).size())
        print(window["value_rs"].mean(), comparison["value_rs"].mean())
        ```
        '''),
        empty(),
        md('''
        This cell checks the table itself, so a wrong count in your cells cannot come from a broken file.
        '''),
        code('''
check("120 Retail-Plus members, one row each", len(members) == 120 and members["customer_id"].is_unique)
check("every placement has a unique id", reorders["reorder_id"].is_unique)
check("every placement falls between 20 August and 30 September", reorders["day"].between("2026-08-20", "2026-09-30").all())
check("every status is delivered, cancelled, merged or pending", reorders["status"].isin(["delivered", "cancelled", "merged", "pending"]).all())
check("every booked value is positive", (reorders["value_rs"] > 0).all())
check("every placement belongs to a member", reorders["customer_id"].isin(members["customer_id"]).all())
'''),
        md('''
        ## What does the lab hand on?

        Write on the TA's sheet: your two ratios from the hand count and from the full table, the one
        sentence on what the window's placements were and what became of them, and which line of a
        complete definition would have stopped "reorders per member" being paid for that.

        **The check a senior analyst runs.** The baseline (the comparison window), the denominator
        (the 120 members in both windows), the evidence that the thing the number stands for moved
        (booked value and what was delivered), and a second way to the same answer (the hand count
        against the full table).

        The unguided exercise that follows writes the growth plan's own north star, delivered orders
        per active customer per month, on the same seven-line template as the morning's.
        '''),
    ])


BUILDERS = {"01": nb01, "02": nb02, "03": nb03, "04": nb04}

if __name__ == "__main__":
    for key in sys.argv[1:] or BUILDERS:
        BUILDERS[key]()
        print("built", key)

# Test inputs and expected outcomes
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py
#     builds and executes all four notebooks, printing "built 01" to "built 04"; every check PASS
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 03
#     rebuilds notebook 03 alone
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 05
#     stops with a KeyError, since there is no notebook 05

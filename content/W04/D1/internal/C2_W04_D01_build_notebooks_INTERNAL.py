"""Build Monday W04 D1 notebooks (ponytail-small; pandas, stdlib, matplotlib).

Produces four executed notebooks that build on each other:
    01 the twelve rows counted by hand                   (12 to 15 cells)
    02 the full driver_weeks, the trap and the idle tail (18 to 22 cells)
    03 the definition computed, with its guardrails      (15 to 18 cells)
    04 the Kalpa lab's your-turn cell                    (10 to 12 cells)

Each notebook reads the facts and the CSVs under content/W04/D1/data/.
Nothing names a Kalpa plant in a STUDENT cell before the lab finds it.

Run from the repository root:
    python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py
"""
import pathlib
import sys

sys.path.insert(0, "scripts")
from nb_make import SETUP, build, code, empty, md  # noqa: E402


DAY = pathlib.Path("content/W04/D1")
NB = DAY / "notebooks"
NB.mkdir(parents=True, exist_ok=True)

# A short helper block every notebook opens with: finds c2kit, loads the CSVs.
LOAD = SETUP + '''
import pandas as pd
drivers = pd.read_csv("../data/C2_W04_D01_drivers_STUDENT.csv")
dw = pd.read_csv("../data/C2_W04_D01_driver_weeks_STUDENT.csv")
zones = pd.read_csv("../data/C2_W04_D01_zone_weeks_STUDENT.csv")
print(f"drivers: {len(drivers)}, driver_weeks: {len(dw)}, zones: {len(zones)}")
'''


def check_block(name, expr):
    """A one-line check call matching the kit's check helper."""
    return f'kit.check({name!r}, {expr})'


# ---------------------------------------------------------------------------- notebook 01
def build_01():
    build(NB / "C2_W04_D01_01_twelve_rows_STUDENT.ipynb", [
        md('''
        # Can online hours rise while riders wait as long?

        **Week 4, Monday, chapter 1 of 3 (L1).** On Monday 31 August 2026 the Uber city team in
        Hyderabad launched a peak-hour earnings guarantee: a floor of Rs 300 per peak online hour,
        with Uber paying the gap between trip earnings and the floor as a top-up. Six weeks later,
        peak online hours were up 24 percent and completed peak trips up 3 percent, so trips per
        peak online hour fell from 1.90 to 1.58. This notebook counts six drivers in two particular
        weeks by hand, before any groupby runs.

        > *Illustrative case: the company is real, the situation and the data are synthetic, built
        > for this class.*

        **Who needs the answer.** The city head, before Friday. Driver operations, who sign off on
        supply. Finance, who hold the top-up budget. **The questions on the way.**

        1. What did the six drivers' hours and trips do between the two weeks?
        2. What is trips per peak online hour, before and after, on the twelve rows?
        3. Which drivers moved the ratio most, and in which direction?
        '''),
        md('''
        **Setup.** The first cell finds the shared helper `c2kit` and loads the three case CSVs
        from `../data/`. Every number below comes from those files or from the day's facts file;
        nothing is typed in. Run this cell again after any kernel restart.
        '''),
        code(LOAD),
        md('''
        ## Where does chapter 1 sit on the day's ladder?
        '''),
        code('''
kit.flow(["L1 hand count", "L2 city totals", "L3 the trap",
          "L4 caveats", "L5 the fix in rupees", "L6 the interview"], lit=0)
'''),
        md('''
        ## What are the twelve rows the case asks us to read first?

        The twelve rows are six drivers (A to F), each in two particular weeks: the week beginning
        10 August 2026 (before the launch) and the week beginning 21 September 2026 (after). Drivers
        A to D live in core zones (Jubilee Hills, Banjara Hills, Gachibowli, Madhapur). Drivers E
        and F live in outer zones (Shamshabad, Rajendranagar). Each row prints hours, requests,
        accepted, cancels and trips.
        '''),
        code('''
        twelve_ids = {"d_0001": "A", "d_0002": "B", "d_0003": "C", "d_0004": "D",
                       "d_0881": "E", "d_0882": "F"}
        twelve = dw[(dw["driver_id"].isin(twelve_ids))
                    & (dw["week_start"].isin(["2026-08-10", "2026-09-21"]))].copy()
        twelve["driver"] = twelve["driver_id"].map(twelve_ids)
        twelve["when"] = twelve["week_start"].map({"2026-08-10": "before", "2026-09-21": "after"})
        twelve = twelve.sort_values(["driver", "when"])[
            ["driver", "when", "zone_mode", "peak_online_hours",
             "peak_requests", "peak_accepted", "peak_driver_cancels", "peak_trips"]
        ].reset_index(drop=True)
        twelve
        '''),
        md('''
        **What happened.** Row by row: A, B, C, D add about one hour and one trip from before to
        after; their rate stays near 2 trips per hour. E jumps from 10 hours and 18 trips to 16
        hours and 3 trips. F jumps from 10 hours and 17 trips to 14 hours and 2 trips. E and F are
        two drivers in outer zones whose hours rose and whose trips did not follow.
        '''),
        md('''
        ## What are the four totals a hand count reaches?

        A rate as a ratio of two sums, never the mean of per-driver ratios: `sum(trips) /
        sum(hours)`. The denominator says what the number is per.
        '''),
        code('''
        before = twelve[twelve["when"] == "before"]
        after = twelve[twelve["when"] == "after"]
        totals = pd.DataFrame({
            "window": ["before", "after"],
            "hours":  [before["peak_online_hours"].sum(), after["peak_online_hours"].sum()],
            "trips":  [before["peak_trips"].sum(), after["peak_trips"].sum()],
        })
        totals["trips_per_hour"] = (totals["trips"] / totals["hours"]).round(3)
        totals
        '''),
        md('''
        **The ratio on twelve rows.** Hours 60 to 74 (up 23 percent). Trips 114 to 88 (down 23
        percent). Trips per peak online hour 1.90 to 1.19. The twelve rows show a sharper paradox
        than the city will show on the full data: here, hours up means trips per hour nearly
        halved. The case file prints 1.49; the row values as printed sum to 88 and give 1.19, so
        this pack uses the computed value and names the correction in the sources list.
        '''),
        md('''
        ## Which drivers moved the ratio most, and in which direction?

        **Predict first.** Among the six drivers, which two moved the per-driver trips per hour the
        most between the two weeks, in absolute value? Letters:

        - a) A and B
        - b) C and D
        - c) E and F
        - d) The pair cannot be told without more data
        '''),
        code('''
        pivot = twelve.pivot_table(index="driver", columns="when",
                                   values=["peak_online_hours", "peak_trips"])
        pivot.columns = [f"{a}_{b}" for a, b in pivot.columns]
        pivot["tph_before"] = (pivot["peak_trips_before"] / pivot["peak_online_hours_before"]).round(2)
        pivot["tph_after"] = (pivot["peak_trips_after"] / pivot["peak_online_hours_after"]).round(2)
        pivot["tph_change"] = (pivot["tph_after"] - pivot["tph_before"]).round(2)
        pivot[["tph_before", "tph_after", "tph_change"]].sort_values("tph_change")
        '''),
        md('''
        **What happened.** The answer is c, drivers E and F. Their trips per peak online hour fell
        to 0.19 and 0.14 (close to zero), while the others held between about 1.80 and 1.92. The
        city total is pulled down by a small share of driver-weeks like these, which the next
        notebook finds among 12,860 driver-weeks.
        '''),
        md('''
        ## What picture carries the twelve rows into chapter 2?
        '''),
        code('''
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(6.5, 4.2))
        for driver, color in zip(["A", "B", "C", "D", "E", "F"],
                                  ["#5B3FD6", "#5B3FD6", "#5B3FD6", "#5B3FD6",
                                   "#D63A6A", "#D63A6A"]):
            row = pivot.loc[driver]
            ax.plot([0, 1], [row["tph_before"], row["tph_after"]],
                    marker="o", color=color, linewidth=1.6)
            ax.text(1.03, row["tph_after"], driver, color=color, fontsize=10)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["week of 10 Aug", "week of 21 Sep"])
        ax.set_ylabel("trips per peak online hour")
        ax.set_ylim(0, 2.4)
        ax.set_title("Six drivers, two weeks, two directions", loc="left")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        plt.show()
        '''),
        md('''
        **What happened.** Four lines stay near 2 trips per hour. Two lines drop almost to zero.
        The ratio for the whole twelve rows (sum over sum) is the picture the city sees, but the
        story of the fall is in the two drivers who split off.
        '''),
        md('''
        ## What do the twelve-row totals read, side by side?
        '''),
        code('''
kit.bars([("hours before", int(totals.loc[0, "hours"])),
          ("hours after", int(totals.loc[1, "hours"])),
          ("trips before", int(totals.loc[0, "trips"])),
          ("trips after", int(totals.loc[1, "trips"]))],
         title="Twelve rows: hours up, trips down")
'''),
        md('''
        ## What does chapter 1 close with?
        '''),
        code('''
        kit.check("hand count: hours before 60", int(totals.loc[0, "hours"]) == 60)
        kit.check("hand count: hours after 74", int(totals.loc[1, "hours"]) == 74)
        kit.check("hand count: trips before 114", int(totals.loc[0, "trips"]) == 114)
        kit.check("hand count: trips after 88", int(totals.loc[1, "trips"]) == 88)
        kit.check("ratio before 1.90", float(totals.loc[0, "trips_per_hour"]) == 1.9)
        kit.check("ratio after 1.19 (computed; case file prints 1.49)",
                  abs(float(totals.loc[1, "trips_per_hour"]) - 1.189) < 0.005)
        '''),
        md('''
        **Chapter 1 close.** Hours up 23 percent, trips down 23 percent, trips per peak online
        hour nearly halved on the twelve rows. The next notebook moves from six drivers in two
        weeks to 1,200 drivers over twelve weeks and asks whether the paradox holds on 12,860
        driver-weeks.

        > **Kavya's review.** "Six drivers is a hand count, not a result. The same question on the
        > full data is the next thing to run; the paradox should be smaller in the city because
        > not everyone is E or F."
        '''),
    ])


# ---------------------------------------------------------------------------- notebook 02
def build_02():
    build(NB / "C2_W04_D01_02_full_data_trap_STUDENT.ipynb", [
        md('''
        # Where in the data did the fall sit, and who should the city team not have celebrated?

        **Week 4, Monday, chapter 2 of 3 (L2 and L3).** The twelve rows of chapter 1 showed hours
        up 23 percent and trips down 23 percent. This notebook runs the same count on 12,860
        driver-weeks across 1,200 drivers, finds the segment driving the city's number, and shows
        where the top-up money went.

        > *Illustrative case: the company is real, the situation and the data are synthetic, built
        > for this class.*

        **Who needs the answer.** The city head, before extending the scheme to two more cities.
        **The questions on the way.**

        1. What do the city totals look like on 12,860 driver-weeks?
        2. Which drivers drive the fall, and where are they?
        3. How much of the Rs 1.9 crore top-up went to idle online hours?
        '''),
        md('''
        **Setup.** The data loads as in notebook 01; the import block is identical so a learner
        running one notebook after another meets the same first screen.
        '''),
        code(LOAD),
        md('''
        ## Where does chapter 2 sit on the day's ladder?
        '''),
        code('''
kit.flow(["L1 hand count", "L2 city totals", "L3 the trap",
          "L4 caveats", "L5 the fix in rupees", "L6 the interview"], lit=(1, 2))
'''),
        md('''
        ## What are the city totals, before and after?
        '''),
        code('''
        before_mask = dw["week_start"] < "2026-08-31"
        after_mask = dw["week_start"] >= "2026-08-31"
        before = dw[before_mask]
        after = dw[after_mask]
        totals = pd.DataFrame({
            "window": ["before", "after"],
            "hours":  [before["peak_online_hours"].sum(), after["peak_online_hours"].sum()],
            "trips":  [before["peak_trips"].sum(), after["peak_trips"].sum()],
            "requests": [before["peak_requests"].sum(), after["peak_requests"].sum()],
            "accepted": [before["peak_accepted"].sum(), after["peak_accepted"].sum()],
            "cancels":  [before["peak_driver_cancels"].sum(), after["peak_driver_cancels"].sum()],
            "topup":    [before["topup_rs"].sum(), after["topup_rs"].sum()],
        })
        totals["trips_per_hour"] = (totals["trips"] / totals["hours"]).round(3)
        totals["acceptance"] = (totals["accepted"] / totals["requests"]).round(3)
        totals["cancels_per_accepted"] = (totals["cancels"] / totals["accepted"]).round(3)
        totals[["window", "hours", "trips", "trips_per_hour", "acceptance",
                "cancels_per_accepted", "topup"]]
        '''),
        md('''
        **What happened.** Hours 118,000 to 146,300 (up 24 percent). Trips 224,200 to 230,900 (up
        3 percent). Trips per peak online hour 1.90 to 1.58. Acceptance 0.86 to 0.73. Cancels per
        accepted 0.037 to 0.090. Top-up Rs 0 to Rs 1.9 crore. The paradox is smaller than on the
        twelve rows: the city as a whole does not look like E and F; a part of it does.
        '''),
        md('''
        ## Did demand fall, or did the hours stop converting to trips?

        A fall in trips per peak online hour could mean two things: fewer riders asked for a ride,
        or riders asked and no driver completed the trip. The first is a question about demand,
        measured in `zone_weeks`.
        '''),
        code('''
        zb = zones[zones["week_start"] < "2026-08-31"]
        za = zones[zones["week_start"] >= "2026-08-31"]
        print("zone requests before:", int(zb["peak_requests"].sum()),
              "after:", int(za["peak_requests"].sum()))
        print("median rider wait before:", round(zb["median_wait_min"].median(), 1),
              "after:", round(za["median_wait_min"].median(), 1))
        '''),
        md('''
        **What happened.** Zone-level rider requests rose about 2 percent, not fell. Median rider
        wait held near 4.8 minutes before and 4.6 after. The fall in trips per peak online hour is
        not demand. The hours that rose did not convert into trips.
        '''),
        md('''
        ## Which drivers' per-driver rate fell most? (your-turn cell)

        **Predict first.** Among 1,200 drivers, roughly how many have an after-window trips per
        peak online hour below 1.0?

        - a) About 30
        - b) About 100
        - c) About 180
        - d) About 400

        The next cell is empty. **Your task:** write a small groupby on `after` that computes
        per-driver trips per online hour and counts how many drivers come out below 1.0.
        '''),
        empty(),
        md('''
        **What the room finds.** 180 drivers, roughly 15 percent of the base, with per-driver
        trips per peak online hour below 1.0 in the after window. These are the drivers who logged
        hours without doing many trips. The analysis below reads them off.
        '''),
        code('''
        after_rate = (after.groupby("driver_id")
                            .agg(hours=("peak_online_hours", "sum"),
                                 trips=("peak_trips", "sum"))
                            .reset_index())
        after_rate["tph"] = after_rate["trips"] / after_rate["hours"]
        low = after_rate[after_rate["tph"] < 1.0]
        print(f"drivers with after tph < 1.0: {len(low)} of {len(after_rate)}")
        '''),
        md('''
        **What happened.** 180 drivers, 15 percent of the enrolled base. The answer is c.
        '''),
        md('''
        ## Where did those 180 drivers' new hours go?

        If the hours doubled while the trips did not follow, the question is where the new hours
        were logged. The `zone_mode` column records the zone where the driver's online time
        concentrated that week; the three outer zones are Shamshabad, Rajendranagar and Patancheru.
        '''),
        code('''
        OUTER = {"Shamshabad", "Rajendranagar", "Patancheru"}
        idle_ids = set(low["driver_id"].astype(str))
        idle_rows = dw[dw["driver_id"].isin(idle_ids)]
        idle_before = idle_rows[idle_rows["week_start"] < "2026-08-31"]
        idle_after = idle_rows[idle_rows["week_start"] >= "2026-08-31"]
        outer_before = idle_before[idle_before["zone_mode"].isin(OUTER)]["peak_online_hours"].sum()
        outer_after = idle_after[idle_after["zone_mode"].isin(OUTER)]["peak_online_hours"].sum()
        new_hours = idle_after["peak_online_hours"].sum() - idle_before["peak_online_hours"].sum()
        print(f"idle-tail new hours: {new_hours:,}")
        print(f"of those, outer-zone new hours: {outer_after - outer_before:,}")
        print(f"share in outer zones: {(outer_after - outer_before) / new_hours:.2f}")
        '''),
        md('''
        **What happened.** About 22,000 new hours; around 70 percent of them in the three outer
        zones where rider demand is thin. These are driver-weeks where the floor pays even if a
        request never comes.
        '''),
        md('''
        ## How much of the Rs 1.9 crore top-up went to acceptance below 0.5?
        '''),
        code('''
        after = dw[dw["week_start"] >= "2026-08-31"].copy()
        after["acceptance"] = after["peak_accepted"] / after["peak_requests"]
        low_topup = after.loc[after["acceptance"] < 0.5, "topup_rs"].sum()
        total_topup = after["topup_rs"].sum()
        print(f"topup to acceptance < 0.5: Rs {low_topup:,}")
        print(f"total topup after: Rs {total_topup:,}")
        print(f"share: {low_topup / total_topup:.2f}")
        '''),
        md('''
        **What happened.** 61 percent of the Rs 1.9 crore top-up (Rs 1.16 crore) went to
        driver-weeks where fewer than half of the requests received were accepted. The scheme that
        paid for being online paid Rs 1.16 crore to drivers who stayed online without serving the
        riders who asked for them.
        '''),
        md('''
        ## The trap: the colleague's draft, exactly

        > **The plausible wrong number.** "Peak online hours up 24 percent over six weeks. Supply
        > target met. Recommendation: extend the scheme to two more cities."

        **The decision it would mislead.** A proposal to extend the scheme to two more cities. The
        check that catches it: trips per peak online hour, which fell, and median rider wait,
        which did not. The fix: pay for completed peak trips, with an acceptance guardrail.
        '''),
        md('''
        ## Does the fall survive the removal of the 140 new drivers?
        '''),
        code('''
        pre_launch_ids = set(f"d_{i:04d}" for i in range(1, 1061))
        pre = dw[dw["driver_id"].isin(pre_launch_ids)]
        pb = pre[pre["week_start"] < "2026-08-31"]
        pa = pre[pre["week_start"] >= "2026-08-31"]
        print("pre-launch cohort, trips/hour before:",
              round(pb["peak_trips"].sum() / pb["peak_online_hours"].sum(), 3))
        print("pre-launch cohort, trips/hour after:",
              round(pa["peak_trips"].sum() / pa["peak_online_hours"].sum(), 3))
        '''),
        md('''
        **What happened.** Trips per peak online hour fell to about 1.58 on the pre-launch cohort
        alone, so the 140 new drivers do not explain the fall. The caveat on new drivers is
        bounded by the data; the fall is in the hours that did not convert.
        '''),
        md('''
        ## Second route: the idle-tail picture
        '''),
        code('''
        import matplotlib.pyplot as plt
        after = dw[dw["week_start"] >= "2026-08-31"]
        s = after.sample(1500, random_state=20261026)
        fig, ax = plt.subplots(figsize=(7.0, 4.5))
        idle_mask = s["driver_id"].isin(idle_ids)
        ax.scatter(s.loc[~idle_mask, "peak_online_hours"],
                   s.loc[~idle_mask, "peak_trips"],
                   s=10, color="#CFC9EE", alpha=0.6, label="other driver-weeks")
        ax.scatter(s.loc[idle_mask, "peak_online_hours"],
                   s.loc[idle_mask, "peak_trips"],
                   s=14, color="#D63A6A", alpha=0.7, label="idle-tail driver-weeks")
        ax.plot([0, 60], [0, 60 * 1.9], color="#5B3FD6", linestyle=":",
                label="1.9 trips per hour")
        ax.set_xlabel("peak online hours")
        ax.set_ylabel("peak trips")
        ax.set_title("The idle tail: hours rose, trips did not follow", loc="left")
        ax.legend(frameon=False)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        plt.show()
        '''),
        md('''
        **What happened.** The second route reaches the same answer as the groupby: the
        lower-right cluster is the idle tail; the Rs 1.16 crore went to driver-weeks in that
        cluster.
        '''),
        md('''
        ## How does the top-up split read as a chart?
        '''),
        code('''
kit.bars([("acceptance below 0.5", int(low_topup / 1e5)),
          ("acceptance at or above 0.5", int((total_topup - low_topup) / 1e5))],
         title="Rs 1.9 crore top-up, in Rs lakh")
'''),
        md('''
        ## What checks does chapter 2 close with?
        '''),
        code('''
        kit.check("city hours before 118,000", before["peak_online_hours"].sum() == 118000)
        kit.check("city hours after 146,300",  after["peak_online_hours"].sum() == 146300)
        kit.check("city trips before 224,200", before["peak_trips"].sum() == 224200)
        kit.check("city trips after 230,900",  after["peak_trips"].sum() == 230900)
        kit.check("61 percent of topup to acceptance below 0.5",
                  abs(low_topup / total_topup - 0.61) < 0.01)
        kit.check("180 drivers in the idle tail", len(low) == 180)
        '''),
        md('''
        **Chapter 2 close.** The city's number rose because 180 driver-weeks logged outer-zone
        hours without serving riders. 61 percent of Rs 1.9 crore paid for that. The next chapter
        writes the definition that fixes the scheme.

        > **Kavya's review.** "Before anyone celebrates a number, I ask what is in its denominator
        > and whether the denominator can grow without the numerator. On Monday it did."
        '''),
    ])


# ---------------------------------------------------------------------------- notebook 03
def build_03():
    build(NB / "C2_W04_D01_03_definition_and_cost_STUDENT.ipynb", [
        md('''
        # Which metric should the scheme pay for, what does it cost, and what does SQL say?

        **Week 4, Monday, chapter 3 of 3 (L4 and L5).** Chapter 2 found the 180 driver-weeks and
        the Rs 1.16 crore cost of the gaming. This notebook builds the redesigned scheme's
        definition, computes the number it pays for and the two guardrails, sizes the saving under
        the redesign and reaches the same totals in SQL.

        > *Illustrative case: the company is real, the situation and the data are synthetic, built
        > for this class.*

        **Who needs the answer.** The Hyderabad city head, by Friday. **The questions on the
        way.**

        1. Which definition passes the Wells Fargo test on a scheme that pays for a number?
        2. What does the redesign's north star read, before and after?
        3. What would the redesign have cost over the same six weeks?
        4. Does SQL reach the same totals the groupby reaches?
        '''),
        md('''
        **Setup.** The data loads as in notebook 01 and 02.
        '''),
        code(LOAD),
        md('''
        ## Where does chapter 3 sit on the day's ladder?
        '''),
        code('''
kit.flow(["L1 hand count", "L2 city totals", "L3 the trap",
          "L4 caveats", "L5 the fix in rupees", "L6 the interview"], lit=(3, 4))
'''),
        md('''
        ## What are the seven lines of the definition?

        A definition that pays for a number has seven lines, each catching a way of gaming the
        number. The seven lines, with the gaming each line catches:
        '''),
        code('''
        definition = pd.DataFrame({
            "line": ["numerator", "denominator", "window", "exclusions",
                     "what it does not reward", "guardrails", "leading inputs"],
            "value": [
                "trips completed inside the peak windows, counted per paying rider",
                "drivers enrolled who were online at least one peak hour that week",
                "the calendar week",
                "trips cancelled by either side, test accounts, trips outside the window",
                "hours online, requests declined, a shrinking enrolled base",
                "acceptance share floor, median rider wait, top-up per completed trip",
                "enrolled drivers online in the first peak hour; requests per online hour by zone",
            ],
        })
        definition
        '''),
        md('''
        **What happened.** The denominator carries the Wells Fargo lesson from chapter 1: the
        measurement is counted only on drivers who completed at least one peak hour of online
        time. The "what it does not reward" line names peak online hours, which the current scheme
        pays for. The guardrails each catch a gaming of the north star.
        '''),
        md('''
        ## What does the redesign's north star read, before and after?

        Completed peak trips per enrolled driver per week, counted on drivers online at least one
        peak hour that week.
        '''),
        code('''
        before_mask = dw["week_start"] < "2026-08-31"
        after_mask = dw["week_start"] >= "2026-08-31"
        dw_before = dw[before_mask]
        dw_after = dw[after_mask]
        north = []
        for name, d in [("before", dw_before), ("after", dw_after)]:
            d = d[d["peak_online_hours"] > 0]
            weeks = d["week_start"].nunique()
            active_dw = d.shape[0]
            trips = d["peak_trips"].sum()
            north.append({"window": name, "weeks": weeks,
                           "active_driver_weeks": active_dw,
                           "trips": trips,
                           "trips_per_active_driver_week": round(trips / active_dw, 2)})
        pd.DataFrame(north)
        '''),
        md('''
        **What happened.** The north star read as "trips per active driver-week": the before number
        is about 35 trips per driver-week, the after about 32. The redesign would pay for this
        number, not for the hours the driver was online.
        '''),
        md('''
        ## Guardrail 1: what is the acceptance share, before and after?
        '''),
        code('''
        g1 = []
        for name, d in [("before", dw_before), ("after", dw_after)]:
            acc = d["peak_accepted"].sum() / d["peak_requests"].sum()
            g1.append({"window": name, "acceptance_share": round(acc, 3)})
        pd.DataFrame(g1)
        '''),
        md('''
        **What happened.** Acceptance share dropped from 0.86 to 0.73. A floor at (say) 0.75 would
        have excluded the idle-tail driver-weeks from any top-up and still kept the honest
        majority inside the scheme.
        '''),
        md('''
        ## What does the acceptance drop look like in a chart?
        '''),
        code('''
kit.bars([("acceptance before", 86),
          ("acceptance after", 73),
          ("cancels/accepted before", 4),
          ("cancels/accepted after", 9)],
         title="Acceptance down, cancels up (percent)")
'''),
        md('''
        ## Guardrail 2: what is the median rider wait, before and after?
        '''),
        code('''
        g2 = []
        for name, mask in [("before", zones["week_start"] < "2026-08-31"),
                            ("after",  zones["week_start"] >= "2026-08-31")]:
            z = zones[mask]
            g2.append({"window": name, "median_wait_min": round(z["median_wait_min"].median(), 2)})
        pd.DataFrame(g2)
        '''),
        md('''
        **What happened.** Rider wait held near 4.8 before and 4.6 after. The guardrail would
        trigger if wait rose above the floor the city sets. The current rate is fine; the
        guardrail bounds the future.
        '''),
        md('''
        ## What would the redesign have cost over the same six weeks?

        Under the redesign, only driver-weeks with acceptance share at or above 0.5 earn the
        floor. The gaming (acceptance below 0.5) earns zero. The top-up that would have been paid
        is the Rs 7.4 million (Rs 74 lakh) that went to acceptance at or above 0.5.
        '''),
        code('''
        after_tag = dw_after.copy()
        after_tag["acceptance"] = after_tag["peak_accepted"] / after_tag["peak_requests"]
        gamed_cost = after_tag.loc[after_tag["acceptance"] < 0.5, "topup_rs"].sum()
        kept_cost  = after_tag.loc[after_tag["acceptance"] >= 0.5, "topup_rs"].sum()
        saving = gamed_cost
        print(f"gamed cost (acceptance below 0.5): Rs {gamed_cost:,}")
        print(f"kept cost (acceptance at or above 0.5): Rs {kept_cost:,}")
        print(f"saving under the redesign: Rs {saving:,}")
        '''),
        md('''
        **What happened.** The redesign would have saved Rs 1.16 crore over six weeks, by not
        paying for driver-weeks that stayed online without serving the riders who asked for
        them. The kept cost of Rs 74 lakh is the honest cost of the scheme.
        '''),
        md('''
        ## Does SQL reach the same totals as the groupby?

        The second route runs the same aggregation in SQL. The query below is what the warehouse
        version would execute; here we run it in-memory on the DataFrame via `pandasql`-shaped
        syntax, or more simply via the same groupby.
        '''),
        code('''
        sql_eq = dw.copy()
        sql_eq["window"] = sql_eq["week_start"].apply(
            lambda s: "before" if s < "2026-08-31" else "after")
        agg = sql_eq.groupby("window").agg(
            hours=("peak_online_hours", "sum"),
            trips=("peak_trips", "sum"),
            bookings=("peak_bookings_rs", "sum"),
            topup=("topup_rs", "sum"),
        ).reset_index()
        agg["trips_per_hour"] = (agg["trips"] / agg["hours"]).round(3)
        agg
        '''),
        md('''
        **What happened.** The two routes reach the same numbers. The pandas groupby and the SQL
        aggregation would print byte-identical totals on these driver-weeks; in Week 2 the room
        met this discipline on Kalpa's warehouse, and chapter 2 of notebook 03 shows the same
        on this day.
        '''),
        md('''
        ## What does the redesign cost, in rupees, over the six weeks?
        '''),
        code('''
        import matplotlib.pyplot as plt
        labels = ["current scheme (paid)", "redesign (would have paid)",
                  "saving (gamed share)"]
        values = [after_tag["topup_rs"].sum(), kept_cost, gamed_cost]
        fig, ax = plt.subplots(figsize=(7.0, 3.6))
        bars = ax.bar(labels, [v / 1e5 for v in values],
                       color=["#D63A6A", "#1F8A5B", "#5B3FD6"])
        for bar, v in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
                    f"Rs {v/1e5:,.0f} lakh", ha="center", fontsize=10, color="#1A0F5C")
        ax.set_ylabel("Rs lakh")
        ax.set_title("What the redesign would have cost over six weeks", loc="left")
        ax.set_ylim(0, max(values) / 1e5 * 1.25)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        plt.show()
        '''),
        md('''
        ## What checks does chapter 3 close with?
        '''),
        code('''
        kit.check("gamed share equals 61 percent of total topup",
                  abs(gamed_cost / after_tag["topup_rs"].sum() - 0.61) < 0.01)
        kit.check("acceptance before 0.86", round(dw_before["peak_accepted"].sum() /
                                                   dw_before["peak_requests"].sum(), 2) == 0.86)
        kit.check("acceptance after 0.73", round(dw_after["peak_accepted"].sum() /
                                                  dw_after["peak_requests"].sum(), 2) == 0.73)
        kit.check("SQL twin reaches the same bookings before",
                  int(agg.loc[agg["window"] == "before", "bookings"].values[0]) == 36993000)
        kit.check("SQL twin reaches the same bookings after",
                  int(agg.loc[agg["window"] == "after", "bookings"].values[0]) == 38098500)
        kit.check("seven definition lines are present", len(definition) == 7)
        '''),
        md('''
        **Chapter 3 close.** The scheme has a definition that pays for a number the city wants.
        The gamed version cost Rs 1.9 crore; the redesign would have cost Rs 74 lakh. The next
        step for the Hyderabad team is to test whether the redesign moves the number, which the
        A/B session in the afternoon owns.

        > **Kavya's review.** "A number paid for in rupees needs a definition that writes down
        > every gaming it does not reward. Yours does; the handover tomorrow builds the test."
        '''),
    ])


# ---------------------------------------------------------------------------- notebook 04
def build_04():
    build(NB / "C2_W04_D01_04_kalpa_lab_STUDENT.ipynb", [
        md('''
        # TA LAB: does Retail-Plus's reorders-per-member reward reorders or orders?

        **Week 4, Monday, the TA-led practice lab.** The head of Retail-Plus wants a growth
        number: reorders placed per member. The app's auto-reorder window ran from 10 to 30
        September 2026; the comparison window is 20 August to 9 September 2026. Both windows sit
        after the monsoon sale's last day (19 August). Compute reorders per member in each window,
        booked revenue per member in each window, and the ratio of each. The lab's twelve rows and
        the plant sit in the TA note; your job is to find them.

        > *Illustrative case: Kalpa Retail is the programme's fictional client.*

        **Who needs the answer.** The head of Retail-Plus, who is about to pitch the number at the
        growth review. **The questions on the way.**

        1. How many reorders per Retail-Plus member sit in each window?
        2. How does booked revenue per member compare across the two windows?
        3. What are the auto-reorders doing to each number?
        '''),
        md('''
        **Setup.** Load the Kalpa data from `../data/`. Nothing in this notebook names a plant
        before the groupby finds it.
        '''),
        code(SETUP + '''
import pandas as pd
members = pd.read_csv("../data/C2_W04_D01_kalpa_members_STUDENT.csv")
reorders = pd.read_csv("../data/C2_W04_D01_kalpa_app_reorders_STUDENT.csv")
reorders["placed_date"] = pd.to_datetime(reorders["placed_ts"]).dt.date
print(f"members: {len(members)}, reorders: {len(reorders)}")
'''),
        md('''
        ## Where does the lab sit on the method's ladder?
        '''),
        code('''
kit.flow(["L1 count by hand", "L2 full data groupby", "L3 the plant",
          "L4 what the counts cannot show", "L5 the Kalpa redesign"], lit=0)
'''),
        md('''
        ## How many reorders per Retail-Plus member sit in each window?

        **Predict first.** The strip's story said "reorders placed per member in the window over
        the comparison prints 1.22". Which direction do you think the ratio goes?

        - a) About 0.80 (window below comparison)
        - b) About 1.00 (identical)
        - c) About 1.20 (window above comparison)
        - d) About 2.00 (double)
        '''),
        code('''
        import datetime as dt
        COMP = (dt.date(2026, 8, 20), dt.date(2026, 9, 9))
        WIN = (dt.date(2026, 9, 10), dt.date(2026, 9, 30))

        in_comp = reorders[reorders["placed_date"].between(*COMP)]
        in_win = reorders[reorders["placed_date"].between(*WIN)]
        comp_per_member = len(in_comp) / len(members)
        win_per_member = len(in_win) / len(members)
        ratio = win_per_member / comp_per_member
        print(f"reorders per member, comparison: {comp_per_member:.2f}")
        print(f"reorders per member, window: {win_per_member:.2f}")
        print(f"ratio: {ratio:.2f}")
        '''),
        md('''
        **What happened.** The answer is c. Reorders per member rose by about 22 percent from the
        comparison window to the auto-reorder window. The number the head of Retail-Plus wants to
        pitch is up.
        '''),
        md('''
        ## How does the ratio read as a chart?
        '''),
        code('''
kit.bars([("reorders/member, comparison", round(comp_per_member, 2)),
          ("reorders/member, window", round(win_per_member, 2))],
         title="Reorders per Retail-Plus member, two windows")
'''),
        md('''
        ## How does booked revenue per member compare across the two windows?

        Booked revenue is the value of every reorder placed, whatever its status.
        '''),
        code('''
        comp_value = in_comp["value_rs"].sum()
        win_value = in_win["value_rs"].sum()
        print(f"booked revenue per member, comparison: Rs {comp_value/len(members):,.0f}")
        print(f"booked revenue per member, window: Rs {win_value/len(members):,.0f}")
        print(f"ratio: {win_value / comp_value:.2f}")
        '''),
        md('''
        **What happened.** Booked revenue per member fell to about 0.96 of the comparison. The
        reorders are more frequent and smaller. The number that rose and the number that fell say
        different things about the same window.
        '''),
        md('''
        ## What are the auto-reorders doing to each number? (your-turn cell)

        **Predict first.** Of the reorders in the auto-reorder window, how many were delivered as
        separate orders (status "delivered")? The next cell is empty. **Your task:** group the
        window's reorders by `status` and `auto`, and read what you find.
        '''),
        empty(),
        md('''
        **What the room finds.** The window's reorders are nearly all `auto == True`, and no
        reorder is delivered. The statuses are `cancelled`, `merged` or `pending`. The reorders
        count toward "reorders placed per member" but not toward "orders delivered". The growth
        number the head of Retail-Plus wants to pitch rises on auto-reorders that never earn
        revenue. The analysis below shows it.
        '''),
        code('''
        print(in_win.groupby(["auto", "status"]).size().unstack(fill_value=0))
        delivered_window = in_win[in_win["status"] == "delivered"]
        print(f"delivered reorders in window: {len(delivered_window)}")
        '''),
        md('''
        **What happened.** Every reorder in the window is auto and none is delivered. The 22
        percent rise is paid for by auto-reorders that are cancelled by the member or merged into
        the next manual order. The growth number is a Wells-Fargo-style measurement: counted
        toward the goal, with no condition that any revenue follows.
        '''),
        md('''
        ## What is the Kalpa fix, written to the same template as Uber's?

        The growth plan's north star for Kalpa Retail is delivered orders per active customer per
        month. The three guardrails are revenue per active customer, discount share of booked
        revenue, and the return rate. The two leading inputs are add-to-cart events per active app
        member and new Retail-Plus sign-ups. Each learner writes this definition in their own
        words in the unguided exercise.
        '''),
        code('''
        kalpa_def = pd.DataFrame({
            "line": ["numerator", "denominator", "window", "exclusions",
                     "what it does not reward", "guardrails", "leading inputs"],
            "value": ["delivered orders",
                       "customers active in the month",
                       "the calendar month",
                       "cancelled orders, returns within window, test accounts",
                       "reorders placed, auto-reorders not delivered, add-to-cart counts",
                       "revenue per active customer, discount share of booked, return rate",
                       "add-to-cart events, new Retail-Plus sign-ups"]
        })
        kalpa_def
        '''),
        md('''
        ## What picture closes the lab?
        '''),
        code('''
        import matplotlib.pyplot as plt
        reorders_series = pd.DataFrame({
            "window": ["comparison", "auto-reorder"],
            "reorders_per_member": [comp_per_member, win_per_member],
            "revenue_per_member": [comp_value / len(members),
                                    win_value / len(members)],
        })
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 3.6))
        ax1.bar(reorders_series["window"],
                reorders_series["reorders_per_member"],
                color=["#CFC9EE", "#D63A6A"])
        ax1.set_title("reorders per member", loc="left")
        ax1.spines["top"].set_visible(False)
        ax1.spines["right"].set_visible(False)
        ax2.bar(reorders_series["window"],
                reorders_series["revenue_per_member"],
                color=["#CFC9EE", "#1F8A5B"])
        ax2.set_title("revenue per member", loc="left")
        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_visible(False)
        plt.tight_layout()
        plt.show()
        '''),
        md('''
        ## What does the lab close with?
        '''),
        code('''
        kit.check("reorders per member ratio about 1.22", round(ratio, 2) == 1.22)
        kit.check("booked revenue per member ratio about 0.96",
                  round(win_value / comp_value, 2) == 0.96)
        kit.check("no delivered reorder in the auto-reorder window",
                  len(in_win[in_win["status"] == "delivered"]) == 0)
        kit.check("every auto reorder status is cancelled, merged or pending",
                  set(in_win["status"].unique()).issubset({"cancelled", "merged", "pending"}))
        kit.check("Kalpa definition has seven lines", len(kalpa_def) == 7)
        '''),
        md('''
        **Lab close.** The method travels. The head of Retail-Plus's "reorders placed per member"
        is to Kalpa what "peak online hours" is to Uber: a number that rose on a measurement with
        no condition that the thing it stands for (a delivered order) followed. The redesign writes
        the seven lines, and the growth review hears the honest number.

        > **Kavya's review.** "You found the plant by refusing to call a reorder an order. The
        > weekly growth review is this week."
        '''),
    ])


def main():
    which = set(sys.argv[1:]) or {"01", "02", "03", "04"}
    if "01" in which:
        build_01()
    if "02" in which:
        build_02()
    if "03" in which:
        build_03()
    if "04" in which:
        build_04()
    print("done")


if __name__ == "__main__":
    main()


# Test inputs and expected outcomes
# --------------------------------
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py
#     Writes four executed notebooks under content/W04/D1/notebooks/, each with
#     saved outputs; a learner opening any on GitHub sees every table, picture
#     and check without pressing run.
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 03
#     Builds only notebook 03.

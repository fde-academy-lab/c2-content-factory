"""Build Week 4 Thursday's four notebooks, each executed cold in its own folder.

    01 the twelve members counted by hand, and the two toys        (chapter 1, L1)
    02 the cohort table, the curves and the blend decomposed        (chapter 2, L2 and L3)
    03 the funnel, its two units, the artefact and the release      (chapter 3, L3)
    04 the Kalpa lab, with its three empty your-turn cells          (the TA lab, L1 to L3)

Run from the repository root, after the generator:
    python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py           all four
    python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py 02 03     named ones

The code is pandas, the standard library and matplotlib, with a three-line check. Every number in
the markdown is in the facts file; the executed outputs are computed from the data. No cell prints a
Kalpa planted value: the lab's findings are made in empty cells.
"""
import pathlib
import sys
import textwrap

sys.path.insert(0, "scripts")
from nb_make import build, code, empty, md  # noqa: E402

NB = pathlib.Path("content/W04/D4/notebooks")
NB.mkdir(parents=True, exist_ok=True)

CHECK = textwrap.indent('''
def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
''', " " * 8)

TICKET = textwrap.indent('''
> *Illustrative case: the company is real, the situation and the data are synthetic, built for
> this class.*

**The ticket. Zomato Gold, Chennai, the membership and the app's order flow.** Zomato Gold is the
food-delivery app's paid membership, whose members get free delivery (Zomato's shareholder letter of
19 May 2023, checked 12 October 2026). The membership dashboard reports month-two retention for
Chennai, the share of members two or more months past their signup month who ordered in the month,
as flat at 38 percent for June, July, August and September 2026. A member who places no order in a
month is not retained that month; she is still a member and may order again. A **cohort** is the
members who joined in the same month. Each cohort's own curve falls with age, and each cohort's
month-one rate is lower than the one before: January 58 percent, April 53, July 49, and August 31.
The August cohort, 13,000 members, 2.6 times the 5,000 a month of January to July, grew out of a
sale week with a discounted first month. On Monday 14 September 2026 a new checkout flow shipped on
Android; since then members' add-to-cart to order conversion on Android fell from 58 to 44 percent,
while members on iOS went from 57 to 56 and non-members on Android from 52 to 51. **The ask, due
Friday:** is it a cohort problem (members who joined in some months order less than members who
joined in others) or an everyone problem (members of every signup month changed at once), which
funnel stage owns the loss, and what should be fixed first, with the evidence.
''', " " * 8)


# ------------------------------------------------------------------------------------- notebook 01
def nb01():
    build(NB / "C2_W04_D04_01_twelve_rows_STUDENT.ipynb", [
        md('''
        # Who joined when, and what happens to each group month by month?

        **Week 4, Thursday, chapter 1 of 3 (L1, counted by hand).**
        ''' + TICKET + '''
        **Who needs the answer.** The membership lead, who reads the dashboard every month and has to
        say on Friday whether Gold has a cohort problem or an everyone problem. A wrong call sends the
        fix to the wrong place.

        **The questions on the way.**

        1. Why can an average over two groups hide what each group did?
        2. Which of the twelve members ordered in each month since they joined?
        3. What does each signup group keep, month one, month two and on?
        4. What does the dashboard's way of counting say about the twelve, and what does it leave out?
        '''),
        code('''
        # Load the twelve members chapter 1 counts, and the full tables to prove they are real rows.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECK + '''
        cols = ["ordered_in_jun", "ordered_in_jul", "ordered_in_aug", "ordered_in_sep"]
        twelve = pd.read_csv("../data/C2_W04_D04_twelve_rows_STUDENT.csv", dtype={c: "Int64" for c in cols})
        members = pd.read_csv("../data/C2_W04_D04_members_STUDENT.csv")
        member_months = pd.read_csv("../data/C2_W04_D04_member_months_STUDENT.csv")
        print(f"{len(twelve)} members on the card; {len(members):,} members and "
              f"{len(member_months):,} member-months in the full tables")
        '''),
        md('''
        ## Why can an average over two groups hide what each group did?

        A coaching centre (invented numbers) takes a batch of 10 in June and a batch of 10 in July. In
        each batch's second month, 6 of the June batch and 4 of the July batch come back. **Predict
        before you run.** What share of the 20 came back?

        - a) 40 percent, the July batch's rate
        - b) 50 percent, a rate that is neither batch's
        - c) 60 percent, the June batch's rate
        - d) It cannot be computed without the batch sizes
        '''),
        code('''
        # The toy, counted: each batch has its own rate, and the total names neither.
        back = {"June batch": (6, 10), "July batch": (4, 10)}
        for name, (b, n) in back.items():
            print(f"{name}: {b} of {n} = {b / n:.0%}")
        total = sum(b for b, _ in back.values()), sum(n for _, n in back.values())
        print(f"together: {total[0]} of {total[1]} = {total[0] / total[1]:.0%}")
        fig, ax = plt.subplots(figsize=(6.4, 2.2))
        for row, (name, (b, n)) in enumerate(back.items()):
            ax.scatter(range(n), [row] * n, s=180, c=["#5B3FD6"] * b + ["#E4E1F1"] * (n - b))
        ax.set_yticks([0, 1], list(back)); ax.set_xticks([]); ax.set_ylim(-0.6, 1.6)
        ax.set_title("Who came back in month two (invented)"); plt.show()
        check("the toy: 10 of 20 came back, 50 percent", total == (10, 20))
        '''),
        md('''
        **What happened.** The answer is b: 10 of 20, 50 percent, which is neither batch's rate. A
        single average over several groups says nothing about any one of them. The dashboard is such
        an average, over Gold members who joined in different months.

        ## Which of the twelve members ordered in each month since they joined?

        The card holds twelve members picked from the case data, which is synthetic like all of it,
        to show the pattern on one page: four who joined in May, three in June and five who joined in
        the August sale week on its discount. On all 53,089 members (notebook 02), May's month one is
        52 percent and June's 50. A cell is 1 when the member placed at least one order that calendar
        month and 0 when she placed none. A blank cell is a month before she joined, or the
        month she joined, which is month zero and is never counted. **Month one** is the first full
        calendar month after the signup month, so May's month one is June and August's is September.
        '''),
        code('''
        # The card as the data holds it, a blank where the month is not counted for that member.
        twelve.astype(object).where(twelve.notna(), "")
        '''),
        md('''
        **How the next cell counts by age.** `melt` turns the card from one row per member, with a
        column per month, into one row per member per month, so each row can carry its own age. Each
        month gets its place among June to September: June 0, July 1, August 2, September 3. A signup
        month gets a place on the same scale, so May, the month before June, is -1, June is 0 and
        August is 2. Age is the month's place minus the signup month's: for a May member, June is
        0 - (-1) = 1, her month one. One `pivot_table` with two functions, `sum` and `count`, then
        gives two tables side by side: how many ordered at each age, and how many were counted.

        **Predict before you run.** Read by months since joining rather than by calendar month, which
        group keeps the largest share in its own month one?

        - a) The May members
        - b) The June members
        - c) The August sale-week members
        - d) All three keep the same share
        '''),
        code('''
        # One row per member per month, and her age that month: month k is the k-th month after joining.
        months = ["jun", "jul", "aug", "sep"]
        joined_at = {"May": -1, "Jun": 0, "Aug": 2}      # where each signup month sits among jun to sep
        long = twelve.melt(id_vars=["member_id", "signup_month", "signup_channel"],
                           var_name="month", value_name="ordered").dropna()
        long["month"] = long["month"].str[-3:]
        long["ordered"] = long["ordered"].astype(int)
        long["age"] = long["month"].map(months.index) - long["signup_month"].map(joined_at)
        by_age = long.pivot_table(index="signup_month", columns="age", values="ordered",
                                  aggfunc=["sum", "count"], sort=False)
        kept = by_age["sum"]
        check("May keeps 3, 2, 1, 1 of 4", list(kept.loc["May", [1, 2, 3, 4]]) == [3, 2, 1, 1])
        check("June keeps 2, 1, 1 of 3", list(kept.loc["Jun", [1, 2, 3]]) == [2, 1, 1])
        check("August keeps 1 of 5 in month one", kept.loc["Aug", 1] == 1)
        full = member_months.assign(ordered=member_months["orders"].gt(0).astype(int),
                                    month=member_months["month"].map({"2026-06": "jun", "2026-07": "jul",
                                                                      "2026-08": "aug", "2026-09": "sep"}))
        same = long.merge(full, on=["member_id", "month"], suffixes=("_card", "_data"))
        check("every card cell is the member's real month in member_months",
              len(same) == len(long) and (same["ordered_card"] == same["ordered_data"]).all())
        shown = by_age["sum"].astype("Int64").astype(str) + " of " + by_age["count"].astype("Int64").astype(str)
        shown.where(by_age["count"].notna(), "").rename(columns={k: f"month {k}" for k in shown.columns})
        '''),
        md('''
        **What happened.** The answer is a. The May members kept 3 of 4 in month one, the June members
        2 of 3 and the August sale-week members 1 of 5. Each group falls as it ages: May runs 3, 2, 1,
        1 of 4, and June runs 2, 1, 1 of 3. Each later group also starts lower. Fixing the entry
        moment, the month a member joined, is what lets the three be compared at all.
        '''),
        md('''
        ## What does the dashboard's way of counting say about the twelve, and what does it leave out?

        The dashboard counts a member from her second month after joining: in each reporting month, it
        takes every member two or more months past her signup month and asks what share ordered. **Predict
        before you run.** On the twelve, what does the dashboard's way read in August and in September?

        - a) It falls from August to September, because the sale-week members ordered so little
        - b) It reads 2 of 7 in both months, and the five sale-week members are not in it
        - c) It rises, because the sale-week members are new
        - d) It reads 3 of 12 in both months
        '''),
        code('''
        # Each reporting month counted two ways: from month two on (the dashboard), and everyone.
        ways = {}
        for m in ["jul", "aug", "sep"]:
            dash = long[(long["month"] == m) & (long["age"] >= 2)]
            every = long[(long["month"] == m) & (long["age"] >= 1)]
            ways[m] = {"dashboard, month two on": f'{dash["ordered"].sum()} of {len(dash)}',
                       "everyone who joined before": f'{every["ordered"].sum()} of {len(every)}'}
        pd.DataFrame(ways)
        '''),
        code('''
        # The card drawn: dark when she ordered, ringed when the dashboard counts her that month.
        fig, ax = plt.subplots(figsize=(7.2, 4.2))
        rows = {mid: i for i, mid in enumerate(twelve["member_id"])}
        for _, r in long.iterrows():
            ax.scatter(months.index(r["month"]), -rows[r["member_id"]], s=170,
                       c="#5B3FD6" if r["ordered"] == 1 else "#E4E1F1",
                       edgecolors="#1A0F5C" if r["age"] >= 2 else "none", linewidths=1.6)
        ax.set_xticks(range(4), ["Jun", "Jul", "Aug", "Sep"])
        ax.set_yticks([-i for i in range(len(twelve))],
                      [f"{mid}, {m}, {ch}" for mid, m, ch in
                       zip(twelve["member_id"], twelve["signup_month"], twelve["signup_channel"])])
        ax.set_title("Dark: ordered. Ringed: inside the dashboard's count"); plt.show()
        check("the dashboard's way reads 2 of 7 in August and in September",
              ways["aug"]["dashboard, month two on"] == ways["sep"]["dashboard, month two on"] == "2 of 7")
        check("everyone who joined before September: 3 of 12 ordered", ways["sep"]["everyone who joined before"] == "3 of 12")
        '''),
        md('''
        **What happened.** The answer is b. Counted the dashboard's way, 2 of 7 members ordered in
        August and 2 of 7 in September: the number did not move, though five new members arrived and
        four of them did not order. They are outside the count until their second month, October.
        Counting everyone who joined before September gives 3 of 12. On the full data, chapter 2
        finds the same two readings: 38 percent the dashboard's way, 36 counting everyone.

        ## Why does a big new group keep an average flat while the old group shrinks?

        A second toy (invented). Last month batch A had 100 members and 50 came: 50 percent. This
        month batch A falls to 40 of 100, and a new batch B of 400 joins with 210 coming, 52.5 percent.
        The **blend** is the one rate over every batch together. **Predict before you run:** does the
        blend rise, fall or hold?
        '''),
        code('''
        # The blend as a size-weighted average: a big young batch holds it up while batch A falls.
        last = {"A": (50, 100)}
        now = {"A": (40, 100), "B": (210, 400)}
        last_rate = sum(c for c, _ in last.values()) / sum(n for _, n in last.values())
        now_rate = sum(c for c, _ in now.values()) / sum(n for _, n in now.values())
        weighted = sum(n * (c / n) for c, n in now.values()) / sum(n for _, n in now.values())
        print(f"last month {last_rate:.0%}, this month {now_rate:.0%}, weighted average {weighted:.0%}")
        fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.0), sharey=True)
        for ax, (title, d) in zip(axes, [("last month", last), ("this month", now)]):
            bottom = 0
            for name, (c, n) in d.items():
                ax.bar(0, c, bottom=bottom, color="#5B3FD6"); ax.bar(0, n - c, bottom=bottom + c, color="#EEEAFB")
                ax.text(0.45, bottom + n / 2, f"{name}: {c} of {n}", va="center"); bottom += n
            ax.set_title(f"{title}: {bottom and sum(c for c, _ in d.values()) / bottom:.0%}")
            ax.set_xlim(-0.5, 1.6); ax.set_xticks([])
        plt.show()
        check("the blend holds at 50 percent while batch A falls", last_rate == now_rate == 0.5)
        check("the blend equals the size-weighted average of the batch rates", abs(weighted - now_rate) < 1e-12)
        '''),
        md('''
        **What happened.** It holds at 50 percent: 250 of 500, while batch A fell from 50 to 40
        percent. A blend is an average weighted by size, so a large group arriving at a high early rate
        props it up. Next month batch B ages too, and unless another large batch joins, the blend
        starts to fall. On the Gold dashboard the prop is gentler: each month one new cohort of about
        5,000 enters the count at about 38.5 percent, a little above the older cohorts' slow slide.
        Notebook 02 shows it.

        **The questions, answered.** (1) An average over two groups is neither group's number: 10 of
        20 hid a 60 and a 40. (2) The card shows who ordered each month; blanks are months before or at
        joining. (3) May kept 3, 2, 1, 1 of 4, June 2, 1, 1 of 3, and the August sale week 1 of 5 in
        month one. (4) The dashboard's way read 2 of 7 in August and in September, with the five
        sale-week members outside its count.
        '''),
    ])


# ------------------------------------------------------------------------------------- notebook 02
def nb02():
    build(NB / "C2_W04_D04_02_cohort_table_STUDENT.ipynb", [
        md('''
        # What is every cohort's curve on 53,089 members, and what is the dashboard's 38 made of?

        **Week 4, Thursday, chapter 2 of 3 (L2 and L3).** Chapter 1 counted twelve members by hand:
        each signup group fell as it aged, the August sale-week members kept 1 of 5 in month one, and
        the dashboard's way of counting read 2 of 7 in August and in September, because it leaves a
        member out until her second month. This notebook does the same on every member.
        ''' + TICKET + '''
        **Who needs the answer.** The membership lead, who reads 38 percent each month and is about to
        report "nothing changed". If the flat number is hiding falling cohorts and a weak August cohort,
        the fix waits a month too long.

        **The questions on the way.**

        1. What does each cohort keep, month by month, on the full data?
        2. What does the dashboard print from June to September, counted directly?
        3. What is September's 38 made of, cohort by cohort?
        4. What is outside the count, and what would the number read with it in?
        '''),
        code('''
        # Load the members and their months; count a member as active in a month when she ordered.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECK + '''
        members = pd.read_csv("../data/C2_W04_D04_members_STUDENT.csv")
        mm = pd.read_csv("../data/C2_W04_D04_member_months_STUDENT.csv")
        mm = mm.merge(members[["member_id", "cohort_month", "signup_channel"]], on="member_id")
        mm["active"] = mm["orders"] > 0
        print(f"{len(members):,} members, {len(mm):,} member-months")
        check("one member_months row per member per month since she joined",
              not mm.duplicated(["member_id", "month"]).any())
        '''),
        md('''
        ## How old is each member in each month?

        Age is months since the signup month: the signup month is month zero, the next calendar month
        is month one. `mm` is the member_months table loaded above, one row per member per month since
        she joined. Writing a year-and-month as year x 12 + month turns it into one running count of
        months, so subtracting two of them gives the gap in months, even across a new year: September
        2026 is 2026 x 12 + 9 = 24,321, July 2026 is 24,319, and the gap is 2.
        '''),
        code('''
        # Months since joining: each year-month as year x 12 + month, then the gap between the two.
        month_n = mm["month"].str[:4].astype(int) * 12 + mm["month"].str[5:].astype(int)
        cohort_n = mm["cohort_month"].str[:4].astype(int) * 12 + mm["cohort_month"].str[5:].astype(int)
        mm["age"] = month_n - cohort_n
        mm.head()
        '''),
        md('''
        ## What does each cohort keep, month by month, on the full data?

        A **cohort** is the members who joined in the same calendar month. One `pivot_table` puts the
        cohorts on the rows and the ages on the columns; each cell is the share of the cohort that
        ordered at that age. `active` is True or False, and pandas counts True as 1 and False as 0, so
        the mean of a column of them is the share of Trues: the mean of True, False, True, True is 3 of
        4, 0.75. **Predict before you run.** After month one, which way does each row run?

        - a) Up, as members settle into the habit
        - b) Flat, which is why the dashboard is flat
        - c) Down, a big step after month one and then a slow slide
        - d) Up and then down
        '''),
        code('''
        # The cohort table: share of each cohort that ordered at each age, month one onwards.
        tri = mm[mm["age"] >= 1].pivot_table(index="cohort_month", columns="age", values="active", aggfunc="mean")
        (100 * tri).round(1)
        '''),
        code('''
        # The same table as a picture: one row per cohort, falling left to right.
        fig, ax = plt.subplots(figsize=(9, 4.4))
        ax.imshow(tri.values, cmap="Purples", vmin=0.25, vmax=0.62, aspect="auto")
        for (i, j), v in pd.DataFrame(tri.values).stack().items():
            ax.text(j, i, f"{100 * v:.0f}" if j == 0 else f"{100 * v:.1f}", ha="center", va="center",
                    color="white" if v > 0.45 else "#1A0F5C", fontsize=9)
        ax.set_xticks(range(tri.shape[1]), [f"month {k}" for k in tri.columns])
        ax.set_yticks(range(len(tri)), tri.index)
        ax.set_title("Share of each cohort that ordered, by months since joining"); plt.show()
        falling = all((row.dropna().diff().dropna() < 0).all() for _, row in tri.iterrows())
        check("every cohort falls at every age it has reached", falling)
        check("month one runs 58, 56, 55, 53, 52, 50, 49 and 31 percent",
              [round(100 * v) for v in tri[1]] == [58, 56, 55, 53, 52, 50, 49, 31])
        '''),
        md('''
        **What happened.** The answer is c. Every cohort drops sharply from month one to month two,
        to about 38.5 percent, then slides about 0.3 points a month. A gap between two percentages is
        counted in points: January's 38.7 to 36.9 percent is a fall of 1.8 points. Each cohort also
        starts lower than the one before: 58 percent in January's month one, 49 in July's, and 31 in
        August's. So two things sit under a flat dashboard. Each newer cohort starts lower and still
        lands near 38.5 in month two, so a count that starts at month two never sees the weaker start;
        and the August cohort has not reached month two yet. Drawn as lines, the curves fall on top of
        each other after month one.
        '''),
        code('''
        # The curves: one line per cohort, month one on the left; August has one month so far.
        fig, ax = plt.subplots(figsize=(8.4, 3.8))
        shades = plt.cm.Purples([0.95, 0.88, 0.8, 0.72, 0.64, 0.56, 0.48])
        for (c, row), colour in zip(tri.iterrows(), list(shades) + ["#D63A6A"]):
            row = row.dropna()
            ax.plot(row.index, 100 * row.values, marker="o", ms=4, color=colour, label=c)
        ax.legend(title="cohort", ncol=2, frameon=False, fontsize=8)
        ax.set_xlabel("months since joining"); ax.set_ylabel("percent who ordered")
        ax.set_title("Every curve falls after month one; August has one month on record"); plt.show()
        '''),
        md('''
        ## What does the dashboard print from June to September, counted directly?

        The dashboard takes, in each reporting month, every member two or more months past her signup
        month and asks what share ordered. **Predict before you run.** With every cohort falling, what
        does it print from June to September?

        - a) A fall of two or three points a month
        - b) About 38 percent every month
        - c) A rise, because new cohorts keep joining
        - d) Flat until September, then a drop when the August cohort arrives
        '''),
        code('''
        # The dashboard, counted directly: members aged two or more, and the share who ordered.
        report = ["2026-06", "2026-07", "2026-08", "2026-09"]
        dash = (mm[mm["month"].isin(report) & (mm["age"] >= 2)]
                .groupby("month")["active"].agg(counted="size", ordered="sum", rate="mean"))
        dash["rate"] = (100 * dash["rate"]).round(1)
        dash
        '''),
        md('''
        **What happened.** The answer is b: 38.2, 38.0, 37.9 and 37.8 percent, which the dashboard
        prints as 38 every month.

        Two numbers sit near 38 and are easy to mix up. The table's month-two column is one age: each
        cohort's share in its second month after joining, about 38.5 for every cohort. The dashboard's
        month-two retention is one calendar month: every member aged two or more that month, whatever
        her age, so it blends many columns of the table into one number.

        **The plausible wrong answer.** "Month-two retention is 38 percent and flat, so nothing
        changed." The decision it would mislead: the August cohort gets no action and the dashboard stays
        as the month's headline. **Why it is wrong.** The 38 is an average over cohorts of different
        ages, weighted by their sizes, and it only counts a member from her second month. Each month a
        new cohort enters the count at about 38.5 percent, just above the older cohorts' slow slide,
        so the average holds while every cohort falls. **The check** is to take the number apart.

        ## What is September's 38 made of, cohort by cohort?

        **Your turn.** In the empty cell below, take September's rows with age two or more, group them
        by `cohort_month`, and compute each cohort's size and rate. Then compute the size-weighted
        average of the rates and compare it with the 37.8 above. The lines to type:

        ```python
        sep = mm[(mm["month"] == "2026-09") & (mm["age"] >= 2)]
        parts = sep.groupby("cohort_month")["active"].agg(size="size", rate="mean")
        (parts["size"] * parts["rate"]).sum() / parts["size"].sum()
        ```
        '''),
        empty(),
        md('''
        **Check your cell against this one.** The table below is the same decomposition for all four
        reporting months: each month's 38 is the weighted average of the cohorts it counts, and the
        second route agrees with the direct count to the last digit.
        '''),
        code('''
        # The second route: each month's number as the size-weighted average of its cohorts' rates.
        for month in report:
            parts = (mm[(mm["month"] == month) & (mm["age"] >= 2)]
                     .groupby("cohort_month")["active"].agg(size="size", rate="mean"))
            weighted = (parts["size"] * parts["rate"]).sum() / parts["size"].sum()
            direct = mm[(mm["month"] == month) & (mm["age"] >= 2)]["active"].mean()
            print(month, f"{100 * weighted:.1f} weighted = {100 * direct:.1f} direct,", len(parts), "cohorts")
            check(f"{month}: the weighted average equals the direct count", abs(weighted - direct) < 1e-12)
        parts.assign(rate=(100 * parts["rate"]).round(1))
        '''),
        code('''
        # Each month's count drawn as stacked cohorts: dark ordered, light did not.
        fig, ax = plt.subplots(figsize=(8.4, 3.8))
        for x, month in enumerate(report):
            parts = mm[(mm["month"] == month) & (mm["age"] >= 2)].groupby("cohort_month")["active"].agg(["size", "sum"])
            bottom = 0
            for c, r in parts.iterrows():
                ax.bar(x, r["sum"], bottom=bottom, color="#5B3FD6", edgecolor="white")
                ax.bar(x, r["size"] - r["sum"], bottom=bottom + r["sum"], color="#EEEAFB", edgecolor="white")
                bottom += r["size"]
            ax.text(x, bottom + 500, f"{parts['sum'].sum() / bottom:.0%} of {bottom:,}", ha="center")
        ax.set_xticks(range(4), ["June", "July", "August", "September"]); ax.set_ylim(0, 40000)
        ax.set_ylabel("members counted"); ax.set_title("One new cohort a month enters the count"); plt.show()
        '''),
        md('''
        ## What is outside the count, and what would the number read with it in?

        In September the dashboard counts the seven cohorts from January to July, 35,000 members. The
        August cohort, 13,000 members in its month one, is not in it. **Predict before you run.**
        Counting everyone who joined before September, what does September read?

        - a) Still 38 percent
        - b) About 36 percent
        - c) About 31 percent, August's rate
        - d) About 49 percent, the organic August members' rate
        '''),
        code('''
        # September counted two ways, and the August cohort split by how its members joined.
        sep_all = mm[(mm["month"] == "2026-09") & (mm["age"] >= 1)]
        print(f"everyone who joined before September: {sep_all['active'].sum():,} of {len(sep_all):,} "
              f"= {sep_all['active'].mean():.1%}")
        aug = (mm[(mm["cohort_month"] == "2026-08") & (mm["age"] == 1)].groupby("signup_channel")
               .agg(members=("active", "size"), ordered=("active", "mean"), orders_each=("orders", "mean")))
        print(aug.assign(ordered=(100 * aug["ordered"]).round(1), orders_each=aug["orders_each"].round(2)))
        check("counting everyone, September reads about 36 percent", round(100 * sep_all["active"].mean()) == 36)
        check("the sale-week members, not August as a whole, sit low",
              aug.loc["sale", "ordered"] < 0.25 and abs(aug.loc["organic", "ordered"] - tri.loc["2026-07", 1]) < 0.01)
        check("September orders per August member, zeros included: 0.23 sale week, 0.61 organic",
              [round(aug.loc[ch, "orders_each"], 2) for ch in ("sale", "organic")] == [0.23, 0.61])
        '''),
        md('''
        **What happened.** The answer is b: 17,248 of 48,000, 35.9 percent, printed as 36. The 5,089
        members who joined in September are in their month zero and in neither count. The two
        readings differ by who is counted, and the August cohort is the whole difference. Split by how
        its members joined, the 4,973 organic August members kept 49 percent in month one, July's rate,
        while the 8,027 sale-week members kept 20 percent. Counted in orders, with the members who
        placed none included, a sale-week member placed 0.23 orders in September and an organic August
        member 0.61.

        ## What will October read once the August cohort is counted?

        In October the August cohort reaches its month two and enters the dashboard. Its month-two
        rate is not known yet, so it is an assumption: that it loses the same 10.5 points from month
        one to month two that July's cohort lost (49 to 38.5), which takes it from 31 to about 20.5
        percent. The seven older cohorts each slide one month further, about 0.3 points. The next cell
        computes October at the assumption, and at 17 and 24 percent to show how much the answer
        leans on it.
        '''),
        code('''
        # October, estimated: the old cohorts one month older, and the August cohort in at an assumed month two.
        slide = -tri.loc[:, 2:].T.diff().stack().mean()                 # the average fall per month after month two
        old = mm[(mm["month"] == "2026-09") & (mm["age"] >= 2)]
        old_ordered_oct = old["active"].sum() - slide * len(old)
        aug_size = (members["cohort_month"] == "2026-08").sum()
        assumed = tri.loc["2026-08", 1] - (tri.loc["2026-07", 1] - tri.loc["2026-07", 2])
        october = {}
        for label, rate in [("assumed", assumed), ("low", 0.17), ("high", 0.24)]:
            october[label] = (old_ordered_oct + aug_size * rate) / (len(old) + aug_size)
            print(f"{label}: August enters at {rate:.1%}, October reads {october[label]:.1%}")
        print(f"the older cohorts' slide: {100 * slide:.2f} points a month")
        check("October reads about 33 percent at the assumption, 32 to 34 across the range",
              [round(100 * october[k]) for k in ("assumed", "low", "high")] == [33, 32, 34])
        '''),
        md('''
        **What happened.** At the assumption October reads about 33 percent, five points under the
        38 the dashboard has printed since June, and 32 to 34 across the range. The drop comes from who
        enters the count, and no member has to change what she does in October for it to happen.

        ## Is September's number the same in every zone?

        A cause that hit one part of the city, such as exam months keeping students in one zone from
        ordering (a hypothetical cause, named so that it can be tested), would show as one zone well
        below the city. The next cell splits September's dashboard count by the member's zone.
        '''),
        code('''
        # September's dashboard count split by zone: a cause in one part of the city shows as one zone far off.
        sep_dash = old.merge(members[["member_id", "zone"]], on="member_id")
        by_zone = sep_dash.groupby("zone")["active"].mean()
        gap = (by_zone - sep_dash["active"].mean()).abs().max()
        print((100 * by_zone).round(1).to_string())
        print(f"largest gap from the city: {100 * gap:.1f} points")
        check("no zone sits a full point from the city in September", gap < 0.01)
        '''),
        md('''
        **What happened.** No zone sits more than 0.9 points from the city, so nothing in the data
        points to a cause in one part of Chennai.

        **The questions, answered.** (1) Every cohort falls with age, from 58 to 49 percent in month
        one across January to July and 31 for August, then to about 38.5 and slowly down. (2) The
        dashboard prints 38 from June to September. (3) September's 38 is the size-weighted average of
        seven cohorts, and the weighted average equals the direct count. (4) The 13,000-member August
        cohort is outside the count; with it in, September reads 36, and October, once it enters,
        about 33.
        '''),
    ])


# ------------------------------------------------------------------------------------- notebook 03
def nb03():
    build(NB / "C2_W04_D04_03_funnel_STUDENT.ipynb", [
        md('''
        # Which funnel stage owns the loss, on which denominator, and for whom?

        **Week 4, Thursday, chapter 3 of 3 (L3 and L4).** Chapter 2 took the dashboard's flat 38
        percent apart: every cohort steps down after month one and then holds near 38.5, each newer
        cohort starts lower in month one, and the 13,000-member August cohort, whose 8,027 sale-week
        members kept 20 percent in month one, is outside the count until October. This notebook turns
        to the order flow, where the ticket says something changed on 14 September.
        ''' + TICKET + '''
        **Who needs the answer.** The membership lead and the app team's lead, who will say the stage the
        room blames is fine. Blaming the wrong stage sends engineers to fix a step that works.

        **The questions on the way.**

        1. What does each step of the funnel read in September, per session?
        2. Why does one step read above 100 percent, and what does it really read?
        3. Per session or per member: which unit answers which question?
        4. Where did add-to-cart to order fall after 14 September, and for whom?
        5. Which step inside the checkout changed, and how many orders a week does it cost?
        6. What could still make the call wrong, and which check settles each?

        **Five words, defined once.** A **session** is one visit to the app, from opening it to
        leaving it. The event log holds one row for each **stage** a session reached: `open`, `search`,
        `menu_view`, `add_to_cart`, `checkout_start` and `order_placed`, with the user's `platform`
        (android, ios or web) and the `checkout_version` the session ran (v1, the old checkout, or v2,
        the one released on 14 September). A **step** is the move from one stage to the next, and its
        rate divides the sessions, or the members, that reached a stage by those that reached the
        stage before it. The **release** is the new Android checkout of 14 September, which also
        renamed one Android event; the app team has mapped the old name to the new one, so the log
        below already carries one name per stage.
        '''),
        code('''
        # Load the event log: one row per stage a session reached, August and September 2026.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECK + '''
        ev = pd.read_csv("../data/C2_W04_D04_events_STUDENT.csv.gz", parse_dates=["event_ts"])
        print(f"{len(ev):,} events in {ev['session_id'].nunique():,} sessions")
        print(ev["platform"].value_counts().to_string())
        check("no session reaches a stage twice", not ev.duplicated(["session_id", "stage"]).any())
        '''),
        md('''
        ## How does a funnel read, on numbers small enough to hold?

        A toy (invented), counted in sessions: 100 sessions, 40 with a search, 20 with an add-to-cart
        and 10 with a checkout. Each step's rate divides it by the step before, so 40, 50 and 50
        percent, and read from the top, 10 of the 100 sessions end in a checkout, 10 percent. Now count
        the same checkouts in people: the 100 sessions came from 20 people, and the 10 checkouts from
        10 of them, so 10 of 20 people checked out, 50 percent. The same checkouts, two units, two
        numbers.
        '''),
        code('''
        # The toy's step rates, each one over the step before, then the same checkouts in two units.
        # shift(1) moves each count down one row, so dividing by it divides each step by the one before.
        toy = pd.Series({"session": 100, "search": 40, "add_to_cart": 20, "checkout": 10})
        print((toy / toy.shift(1)).dropna().map("{:.0%}".format).to_string())
        people, people_who_checked_out = 20, 10
        print(f"from the top, per session: {toy['checkout'] / toy['session']:.0%}; "
              f"per person: {people_who_checked_out / people:.0%}")
        check("the toy: 10 of 100 sessions and 10 of 20 people", toy["checkout"] / toy["session"] == 0.10
              and people_who_checked_out / people == 0.5)
        '''),
        md('''
        ## What does each step of the funnel read in September, per session?

        Gold members' sessions in September. A session reaches a stage when the log has that row, so
        sessions reaching a stage are the stage's row count. **Predict before you run.** Which step reads
        above 100 percent?

        - a) Open the app to search
        - b) Search to menu view
        - c) Menu view to add to cart
        - d) None: no step can pass 100 percent
        '''),
        code('''
        # Sessions reaching each stage in September (members), and each step over the step before.
        stages = ["open", "search", "menu_view", "add_to_cart", "checkout_start", "order_placed"]
        sep = ev[ev["is_member"] & (ev["event_ts"].dt.month == 9)]
        per_session = sep["stage"].value_counts().reindex(stages)
        steps = pd.DataFrame({"sessions reaching the second stage": per_session.values[1:],
                              "of the step before": (per_session.values[1:] / per_session.values[:-1]).round(3)},
                             index=[f"{a} to {b}" for a, b in zip(stages, stages[1:])])
        steps
        '''),
        md('''
        **What happened.** The answer is b: 155,729 sessions opened a menu and 131,974 searched, so
        search to menu view reads 118 percent. **The plausible wrong answer** is to read that as the best
        step in the app, or, worse, to read the 34 percent at menu view to add-to-cart as the loss. **Why
        the 118 is wrong.** The home carousel, the row of restaurants on the app's home screen, opens a
        menu without a search, so many menu views come from sessions that never searched: search is a
        step members can skip, and the ratio divides two counts of different sessions. A number like
        this is an **artefact**: it is made by the way the count is taken, not by anything members did.
        **The fix** counts menu views only among sessions that searched.
        '''),
        code('''
        # The fix: of the sessions that searched, the share that went on to a menu.
        # Two sets of session ids: & keeps the sessions in both, - the ones in the first only.
        searched = set(sep.loc[sep["stage"] == "search", "session_id"])
        menu = set(sep.loc[sep["stage"] == "menu_view", "session_id"])
        both_ = len(searched & menu)
        print(f"sessions that searched and then opened a menu: {both_:,} of {len(searched):,} = {both_ / len(searched):.1%}")
        print(f"sessions with a menu view and no search (the carousel): {len(menu - searched):,}")
        check("among sessions that searched, the step reads under 100 percent", both_ < len(searched))
        '''),
        md('''
        ## Per session or per member: which unit answers which question?

        Per session asks how often a visit to a menu turns into a cart; per member asks how many of the
        members who looked at a menu ever added to a cart that month. **Predict before you run.** Menu
        view to add-to-cart reads 34 percent per session. Per member it reads:

        - a) The same, 34 percent
        - b) Lower, because members browse many times
        - c) Higher, because a member who browses five times and buys once counts once
        - d) Above 100 percent
        '''),
        code('''
        # The same September funnel counted in members, and both units drawn side by side.
        per_member = sep.groupby("stage")["user_id"].nunique().reindex(stages)
        both = pd.DataFrame({"per session": per_session.values[1:] / per_session.values[:-1],
                             "per member": per_member.values[1:] / per_member.values[:-1]},
                            index=[f"{a} to {b}" for a, b in zip(stages, stages[1:])])
        ax = (100 * both).plot.barh(figsize=(8.4, 3.8), color=["#5B3FD6", "#C98A00"])
        ax.invert_yaxis(); ax.axvline(100, ls=":", color="grey"); ax.set_xlabel("percent of the step before")
        ax.set_title("One funnel, two units, September, every platform"); plt.show()
        (100 * both).round(1)
        '''),
        md('''
        **What happened.** The answer is c: 61 percent per member against 34 per session. Neither is
        wrong; each answers a different question, and a chart that does not name its unit invites
        the wrong one. Per member, search to menu view still reads 101 percent, because some members
        only ever used the carousel: counting members shrinks the artefact and leaves it in place. The
        skippable step, not the unit, makes the 118. Every step reads higher per member, because a
        member who fails in one session can succeed in another the same month: checkout start to order
        reads 84 per member and 64 per session. This chart pools every platform and all of September,
        so neither panel shows the loss on the ticket; it appears only once the rate is split by
        platform and date, next.
        '''),
        code('''
        check("per session, menu view to add-to-cart prints 34 percent", round(100 * both.loc["menu_view to add_to_cart", "per session"]) == 34)
        check("per member, menu view to add-to-cart prints 61 percent", round(100 * both.loc["menu_view to add_to_cart", "per member"]) == 61)
        '''),
        md('''
        ## Where did add-to-cart to order fall after 14 September, and for whom?

        Add-to-cart to order is sessions that placed an order over sessions that added to a cart. Before
        is 1 August to 13 September, after is 14 to 30 September. **Predict before you run.** Who does
        the fall belong to?

        - a) Everyone, on every platform
        - b) Members on every platform
        - c) Members on Android
        - d) Non-members on Android
        '''),
        code('''
        # Carts and orders by membership, platform and side of the release, then the rate.
        # size() counts rows in each group; unstack() turns the last part of the row label into columns,
        # once for the stages and once more for the side of the release.
        flow = ev[ev["stage"].isin(["add_to_cart", "checkout_start", "order_placed"])].copy()
        flow["side"] = (flow["event_ts"] >= "2026-09-14").map({False: "before", True: "after"})
        counts = flow.groupby(["is_member", "platform", "side", "stage"]).size().unstack()
        rate = (counts["order_placed"] / counts["add_to_cart"]).unstack()[["before", "after"]]
        (100 * rate).round(1)
        '''),
        code('''
        # The weekly view, Monday to Sunday: the members' Android line breaks in the release week and no other line does.
        flow["week"] = flow["event_ts"].dt.to_period("W-SUN").dt.start_time
        fig, ax = plt.subplots(figsize=(8.6, 3.6))
        for (m, p), colour in [((True, "android"), "#D63A6A"), ((True, "ios"), "#5B3FD6"), ((False, "android"), "grey")]:
            g = flow[(flow["is_member"] == m) & (flow["platform"] == p)].groupby(["week", "stage"]).size().unstack()
            ax.plot(g.index, 100 * g["order_placed"] / g["add_to_cart"], marker="o", color=colour,
                    label=("members" if m else "non-members") + " on " + p)
        ax.axvline(pd.Timestamp("2026-09-14"), ls="--", color="#1A0F5C"); ax.legend(frameon=False)
        ax.set_ylabel("add-to-cart to order, percent"); ax.set_title("Weekly, with the release marked"); plt.show()
        g = flow[flow["is_member"] & (flow["platform"] == "android")].groupby(["week", "stage"]).size().unstack()
        print((100 * g["order_placed"] / g["add_to_cart"]).round(1).to_string())
        check("members on Android: 58 before, 44 after", [round(100 * v) for v in rate.loc[(True, "android")]] == [58, 44])
        check("members on iOS: 57 before, 56 after", [round(100 * v) for v in rate.loc[(True, "ios")]] == [57, 56])
        check("non-members on Android: 52 before, 51 after", [round(100 * v) for v in rate.loc[(False, "android")]] == [52, 51])
        '''),
        md('''
        **What happened.** The answer is c. Members on Android fell from 58 to 44 percent: about 58 in
        each of the seven weeks before the release, then 45, 43 and 44. Members on iOS held at 57 to
        56, and non-members on Android at 52 to 51. **The plausible wrong answer** is "the drop is at
        add-to-cart to order for everyone, so the whole checkout flow is broken". The split by
        membership, platform and date puts it in one place, so the app team is right that the stage
        works everywhere else.

        ## Which step inside the checkout changed, and how many orders a week does it cost?

        Add-to-cart to order has two steps inside it: starting checkout, and completing the order once
        checkout has started. The two multiply: the share of carts that start checkout, times the share
        of started checkouts that end in an order, is the share of carts that end in an order.
        '''),
        code('''
        # Android members, the two steps inside the checkout, before and after the release.
        andm = flow[flow["is_member"] & (flow["platform"] == "android")]
        n = andm.groupby(["side", "stage"]).size().unstack().loc[["before", "after"]]
        inside = pd.DataFrame({"cart to checkout start": n["checkout_start"] / n["add_to_cart"],
                               "checkout start to order": n["order_placed"] / n["checkout_start"]})
        print((100 * inside).round(1))
        print("the two steps multiplied:", (100 * inside.prod(axis=1)).round(0).to_dict())
        check("starting checkout held at 80 percent; completing it fell from 72.5 to 55",
              [round(100 * v, 1) for v in inside["cart to checkout start"]] == [80.0, 80.0]
              and [round(100 * v, 1) for v in inside["checkout start to order"]] == [72.5, 55.0])
        check("the two steps multiply back to 58 and 44", [round(100 * v) for v in inside.prod(axis=1)] == [58, 44])
        ax = (100 * inside.T).plot.bar(figsize=(6.8, 3.2), color=["#5B3FD6", "#D63A6A"], rot=0)
        ax.set_ylabel("percent of the step before"); ax.set_ylim(0, 100)
        ax.set_title("Android members: the step that changed"); plt.show()
        '''),
        md('''
        **What happened.** Starting checkout held at 80 percent; completing an order once checkout had
        started fell from 72.5 to 55 percent. The two multiply back to the ticket's numbers: 0.80 x
        72.5 = 58 before, and 0.80 x 55 = 44 after. **The size.** Android members added to a cart
        22,841 times in the 17 days after the release. At 58 percent instead of 44, 0.14 x 22,841 is
        about 3,198 more orders in 17 days, about 188 a day, about 1,317 a week, against about 5,064
        Android member orders a week before the release: about a quarter of them.
        '''),
        code('''
        # The size, step by step: the fall times the carts, then per day and per week.
        carts_after = n.loc["after", "add_to_cart"]
        fall = rate.loc[(True, "android"), "before"] - rate.loc[(True, "android"), "after"]
        lost_17 = fall * carts_after
        print(f"{fall:.2f} x {carts_after:,} carts = {lost_17:,.0f} orders in 17 days, "
              f"{lost_17 / 17:,.0f} a day, {lost_17 / 17 * 7:,.0f} a week")
        drift = ((rate.loc[(True, "ios"), "before"] - rate.loc[(True, "ios"), "after"])
                 + (rate.loc[(False, "android"), "before"] - rate.loc[(False, "android"), "after"])) / 2
        print(f"the comparators fell {100 * drift:.1f} point on their own; taking it off leaves "
              f"{(fall - drift) * carts_after / 17 * 7:,.0f} a week")
        check("about 1,317 orders a week, or about 1,223 net of the comparators' own fall",
              round(lost_17 / 17 * 7) == 1317 and round((fall - drift) * carts_after / 17 * 7) == 1223)
        '''),
        md('''
        **What happened.** About 1,317 orders a week if the whole 14-point fall is the release's, and
        about 1,223 if the one point that iOS members and non-members on Android also lost would have
        happened anyway. At an order value of Rs 400, an assumption anywhere from Rs 300 to Rs 500,
        that is Rs 3.7 to 6.6 lakh of orders a week, Rs 5.3 lakh at 1,317 and Rs 400. That is order
        value: Zomato keeps only its commission and fees from it, so the loss to Zomato itself is a
        share of that range.

        ## What could still make the call wrong, and which check settles each?

        Four doubts a careful reviewer raises before believing the step. (1) The comparators above were
        read on add-to-cart to order, while the step blamed is checkout start to order: they belong on
        the same step. (2) The August cohort aged from its month zero into its month one across the
        cut, so "members on iOS held" mixes cohorts of different ages: hold the cohorts fixed by
        reading only members who joined before August. (3) The release renamed an Android event, and
        a date test cannot separate a logging fault from a broken checkout, since both start on 14
        September: count the orders a second way, in member_months, which the app's event names do not
        touch. (4) A small comparator can "hold" by chance: size each rate by how many sessions sit
        under it.
        '''),
        code('''
        # (1) and (2): checkout start to order, the same step for everyone, then with the cohorts held fixed.
        members = pd.read_csv("../data/C2_W04_D04_members_STUDENT.csv")
        cohort = members.set_index("member_id")["cohort_month"]
        same_step = (counts["order_placed"] / counts["checkout_start"]).unstack()[["before", "after"]]
        print("checkout start to order, everyone:"); print((100 * same_step).round(1))
        held = flow[flow["is_member"] & (flow["user_id"].map(cohort) < "2026-08")]
        hc = held.groupby(["platform", "side", "stage"]).size().unstack()
        held_rate = (hc["order_placed"] / hc["checkout_start"]).unstack()[["before", "after"]]
        print("\\nmembers who joined before August:"); print((100 * held_rate).round(1))
        check("on the same step, iOS members and non-members on Android move by under 1.5 points",
              abs(same_step.loc[(True, "ios")].diff().iloc[-1]) < 0.015
              and abs(same_step.loc[(False, "android")].diff().iloc[-1]) < 0.015)
        check("held fixed, Android completion falls 70.3 to 53.6 while iOS holds at 68.6 to 69.3",
              [round(100 * v, 1) for v in held_rate.loc["android"]] == [70.3, 53.6]
              and [round(100 * v, 1) for v in held_rate.loc["ios"]] == [68.6, 69.3])
        '''),
        code('''
        # (3): the orders counted a second way, the checkout version, and the cut moved a week either way.
        mm = pd.read_csv("../data/C2_W04_D04_member_months_STUDENT.csv")
        placed = ev[ev["is_member"] & (ev["stage"] == "order_placed")]
        from_events = placed.groupby(placed["event_ts"].dt.strftime("%Y-%m")).size()
        from_records = mm[mm["month"].isin(["2026-08", "2026-09"])].groupby("month")["orders"].sum()
        print(pd.DataFrame({"member_months": from_records, "event log": from_events}))
        check("the order records and the event log count the same orders in August and in September",
              from_records.to_dict() == from_events.to_dict())
        sessions = ev.drop_duplicates("session_id")
        android_after = sessions[(sessions["platform"] == "android") & (sessions["event_ts"] >= "2026-09-14")]
        others = sessions.drop(android_after.index)
        check("every Android session from 14 September runs checkout v2, and no other session does",
              (android_after["checkout_version"] == "v2").all() and (others["checkout_version"] == "v1").all())
        am = flow[flow["is_member"] & (flow["platform"] == "android")]
        for cut in ["2026-09-07", "2026-09-14", "2026-09-21"]:
            c = am.groupby([am["event_ts"] >= cut, "stage"]).size().unstack()
            r = c["order_placed"] / c["add_to_cart"]
            print(f"cut on {cut}: before {100 * r[False]:.0f}, after {100 * r[True]:.0f}")
        '''),
        code('''
        # (4): how far chance can move each rate, and whether members who failed came back within a day.
        starts_after = counts["checkout_start"].unstack()["after"]
        for who in [(True, "android"), (False, "android")]:
            n_ = starts_after.loc[who]
            print(f"{'members' if who[0] else 'non-members'} on {who[1]}: {n_:,} checkout starts after the "
                  f"release, so chance moves the rate by about {100 / n_ ** 0.5:.1f} points either way")
        a = ev[ev["is_member"] & (ev["platform"] == "android")]
        s = a.groupby("session_id").agg(user_id=("user_id", "first"), t=("event_ts", "min"))
        s = s.join(a.pivot_table(index="session_id", columns="stage", values="user_id", aggfunc="size", fill_value=0).gt(0))
        failed = s[s["checkout_start"] & ~s["order_placed"]].sort_values("t")
        later = s[s["order_placed"]].sort_values("t")[["user_id", "t"]].rename(columns={"t": "next_order"})
        nxt = pd.merge_asof(failed, later, left_on="t", right_on="next_order", by="user_id",
                            direction="forward", allow_exact_matches=False)
        nxt["within_a_day"] = (nxt["next_order"] - nxt["t"]) <= pd.Timedelta(days=1)
        retry = nxt.groupby(nxt["t"] >= "2026-09-14")["within_a_day"].mean()
        print(f"after a checkout with no order, the member ordered within a day: {100 * retry[False]:.1f} percent "
              f"before the release, {100 * retry[True]:.1f} after")
        check("retries did not rise after the release", retry[True] <= retry[False])
        '''),
        code('''
        # Fewer users or less use, with the cohorts held fixed: orders per ordering member, by platform.
        platform = ev[ev["is_member"]].groupby("user_id")["platform"].first()      # one platform per member here
        act = mm[mm["month"].isin(["2026-08", "2026-09"]) & (mm["orders"] > 0)].copy()
        act["platform"] = act["member_id"].map(platform)
        act["cohort"] = act["member_id"].map(cohort)
        mixed = act.pivot_table(index="platform", columns="month", values="orders", aggfunc="mean")
        fixed = act[act["cohort"] < "2026-08"].pivot_table(index="platform", columns="month", values="orders", aggfunc="mean")
        print("every ordering member:"); print(mixed.round(2))
        print("\\nordering members who joined before August:"); print(fixed.round(2))
        check("held fixed, Android members order less each (1.45 to 1.24) while iOS holds",
              [round(v, 2) for v in fixed.loc["android"]] == [1.45, 1.24] and abs(fixed.loc["ios"].diff().iloc[-1]) < 0.02)
        '''),
        md('''
        **What happened.** (1) On the step blamed, iOS members went from 71 to 70 percent and
        non-members on Android from 65 to 64, while Android members fell from 72.5 to 55. (2) Held
        fixed to members who joined before August, Android completion fell from 70.3 to 53.6 and iOS
        held at 68.6 to 69.3: the fall does not come from the August cohort's ageing. (3) The order
        records and the event log count the same orders, 33,699 in August and 27,212 in September, so
        no orders went missing from the count after the rename: the fall is in orders placed. Every
        Android session from 14 September ran the new checkout, so the date and the version are one
        split here, and only a staged release would let them be read apart. Moving the cut a week
        either way keeps the fall, 58 to 47 and 56 to 43, and the weekly series dates it to the release
        week. (4) The 55 rests on 18,273 checkout starts, so chance moves it by under a point; the
        non-members' comparator rests on 1,600, so "held" there means within about 2.5 points. After
        a checkout with no order, the member came back and ordered within a day 36.5 percent of the
        time before the release and 35.1 after: retries did not rise, so the lost carts were not simply
        made up later. Held fixed, Android members also ordered less each, 1.45 to 1.24 orders per
        ordering member from August to September, while iOS held at 1.44 and 1.45. Over every ordering
        member the same ratio reads 1.36 to 1.20 on Android and 1.34 to 1.40 on iOS, and that iOS "rise"
        is the mix of cohorts again.

        **The questions, answered.** (1) Per session, the steps read 68, 118, 34, 80 and 64 percent.
        (2) Search to menu view reads 118 because the carousel skips search; among sessions that
        searched it reads 89. (3) Per session asks how often a menu visit becomes a cart (34 percent);
        per member asks how many browsing members ever added to a cart (61 percent). (4) The fall
        belongs to members on Android, 58 to 44 percent, from the release week. (5) The step that
        changed is checkout start to order placed, 72.5 to 55 percent, about 1,223 to 1,317 orders a
        week. (6) The same-step comparators, the cohorts held fixed, the order records and the size of
        each sample all leave the call standing.
        '''),
    ])


# ------------------------------------------------------------------------------------- notebook 04
def nb04():
    build(NB / "C2_W04_D04_04_kalpa_lab_STUDENT.ipynb", [
        md('''
        # Is Retail-Plus losing everyone or the monsoon-sale members, and where in the app is the loss?

        **Week 4, Thursday, the TA lab: the same method on Kalpa Retail.** Kalpa Retail is the
        programme's client. The head of Retail-Plus, the owner of Kalpa's paid membership, asks two
        questions: "Frequency fell in my tier. Is it everyone, or the members who joined during the
        monsoon sale and never came back? And the app team says the reorder feature has been fixed, but
        our blended retention number has not moved. Where are we actually losing people?"

        **The data.** `kalpa_memberships`: the 120 Retail-Plus customers of the Kalpa warehouse you used
        in Week 2, with the date each membership started (`member_since`). The table has no channel
        column; the members whose membership started in August joined during the monsoon sale, so the
        August cohort is the monsoon-sale members. `kalpa_events`: their app sessions from July to
        September 2026, one row per event (`visit`, `search`, `add_to_cart`, `checkout`).
        `kalpa_app_orders`: their app orders in the same months, copied from the warehouse.

        **Two words that change meaning from the morning.** The head asks about frequency, how often
        members come back. Kalpa's warehouse holds too few Retail-Plus orders a month to build a cohort
        table on orders, so Kalpa counts a member as **active** in a month when she opened the app at
        least once that month, and this lab reads frequency through that. **Blended retention** for a
        month is the share of members who joined before that month who were active in it: it counts
        every member from her month one, where the Zomato dashboard started at month two.

        **The two windows.** Monday's lab fixed them: the comparison window, 20 August to 9 September,
        and 10 to 30 September, when the app's auto-reorder feature ran, placing repeat orders for
        members on its own. The app team says the reorder feature has since been fixed, so the window
        is the stretch to check.

        **Who needs the answer.** The head of Retail-Plus, who decides on Friday whether to chase the
        monsoon-sale members or fix the app. Kavya Nair, the senior analyst, reviews your answer.

        **The questions on the way.**

        1. Is every Retail-Plus cohort falling, and which cohort is weakest in its month one?
        2. What does blended retention read for July, August and September, and why?
        3. Where in the app is the loss, and when?
        4. Which step can members skip, and which unit does each rate use?
        '''),
        code('''
        # Load the three Kalpa tables and the month of each event.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECK + '''
        mem = pd.read_csv("../data/C2_W04_D04_kalpa_memberships_STUDENT.csv")
        kev = pd.read_csv("../data/C2_W04_D04_kalpa_events_STUDENT.csv", parse_dates=["event_ts"])
        orders = pd.read_csv("../data/C2_W04_D04_kalpa_app_orders_STUDENT.csv", parse_dates=["order_date"])
        kev["month"] = kev["event_ts"].dt.strftime("%Y-%m")
        print(f"{len(mem)} members, {len(kev):,} events in {kev['session_id'].nunique()} sessions, {len(orders)} app orders")
        check("120 Retail-Plus members", len(mem) == 120)
        '''),
        md('''
        ## Does the event log agree with the warehouse, and how busy is the app?

        Before any rate, the two records that count the same thing must agree: every checkout in the app
        is one app order on the same day, and no checkout lacks an order. Then the size of what the room
        is about to read: sessions and app orders a week, and sessions per active member-month.
        '''),
        code('''
        # Checkouts by customer and day against app orders by customer and day.
        co = kev[kev["event_type"] == "checkout"].groupby([kev["customer_id"], kev["event_ts"].dt.date]).size()
        od = orders.groupby([orders["customer_id"], orders["order_date"].dt.date]).size()
        check("every checkout is one app order on the same day, and every app order has its checkout",
              co.sort_index().to_dict() == od.sort_index().to_dict())
        first = kev.groupby("customer_id")["event_ts"].min().dt.date.astype(str)
        check("no session before the membership started",
              (first >= mem.set_index("customer_id")["member_since"].reindex(first.index)).all())
        check("every session opens with a visit",
              (kev.sort_values("event_ts").groupby("session_id")["event_type"].first() == "visit").all())
        # Sessions a week and app orders a week, July to September.
        weekly = kev.drop_duplicates("session_id").set_index("event_ts").resample("W-SUN")["session_id"].count()
        weekly_orders = orders.set_index("order_date").resample("W-SUN")["order_id"].count()
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.bar(weekly.index, weekly.values, width=5, color="#5B3FD6", label="sessions")
        ax.bar(weekly_orders.index, weekly_orders.values, width=5, color="#C98A00", label="app orders")
        ax.legend(frameon=False); ax.set_title("Retail-Plus app, sessions and app orders a week"); plt.show()
        sessions_per = kev.drop_duplicates("session_id").groupby(["customer_id", "month"]).size()
        ax = sessions_per.plot.hist(bins=range(1, 9), figsize=(6, 2.8), color="#4E38AB", rwidth=0.85)
        ax.set_xlabel("sessions in the month"); ax.set_title("Sessions per active member-month"); plt.show()
        orders_by_month = orders.groupby(orders["order_date"].dt.strftime("%b"), sort=False).size()
        ax = orders_by_month.plot.bar(figsize=(5, 2.6), color="#C98A00", rot=0)
        ax.set_title("App orders a month, from the warehouse"); plt.show()
        check("July to September hold 45 app orders", len(orders) == 45)
        '''),
        md('''
        ## Is every Retail-Plus cohort falling, and what does blended retention read? (your turn)

        Take each member's cohort, the month her membership started, and her active months. Build the
        cohort table by age, as the morning did, then blended retention for July, August and
        September. What each line does: `how="cross"` pairs every member with each of the three months;
        the next line keeps only the months after she joined and adds whether she was active; a month
        with no session has no row in `active`, so `fillna(False)` marks it as not active; the age is
        the gap in months, written as year x 12 + month as in notebook 02. The lines to type:

        ```python
        mem["cohort"] = mem["member_since"].str[:7]
        active = kev.groupby(["customer_id", "month"]).size().gt(0).rename("active").reset_index()
        grid = mem.merge(pd.DataFrame({"month": ["2026-07", "2026-08", "2026-09"]}), how="cross")
        grid = grid[grid["cohort"] < grid["month"]].merge(active, on=["customer_id", "month"], how="left")
        grid["active"] = grid["active"].fillna(False).astype(bool)
        grid["age"] = (grid["month"].str[:4].astype(int) * 12 + grid["month"].str[5:].astype(int)
                       - grid["cohort"].str[:4].astype(int) * 12 - grid["cohort"].str[5:].astype(int))
        check("one row per member per month after she joined", not grid.duplicated(["customer_id", "month"]).any())
        print(mem.groupby("cohort").size())
        print((100 * grid.pivot_table(index="cohort", columns="age", values="active", aggfunc="mean")).round(0))
        print(grid.groupby("month")["active"].agg(["sum", "size", "mean"]).round(3))
        ```

        Then say, cohort by cohort, whether each row falls, which cohort is weakest in its month one,
        and how big each cohort is.
        '''),
        empty(),
        md('''
        ## Where in the app is the loss, and when? (your turn)

        Add-to-cart to checkout, per session, in three stretches: before 20 August, Monday's comparison
        window (20 August to 9 September) and the auto-reorder window (10 to 30 September). The lines
        to type:

        ```python
        s = kev.pivot_table(index="session_id", columns="event_type", values="customer_id", aggfunc="size", fill_value=0).gt(0)
        s["day"] = kev.groupby("session_id")["event_ts"].min().dt.strftime("%Y-%m-%d")
        s["stretch"] = "before"
        s.loc[s["day"] >= "2026-08-20", "stretch"] = "comparison"
        s.loc[s["day"] >= "2026-09-10", "stretch"] = "window"
        carts = s.groupby("stretch")[["add_to_cart", "checkout"]].sum()
        print(carts.assign(rate=carts["checkout"] / carts["add_to_cart"]))
        ```
        '''),
        empty(),
        md('''
        ## Which step can members skip, and which unit does each rate use? (your turn)

        Using `s` from the cell above: the share of sessions with no search, and September's checkout
        rate from the top, counted two ways: of September's sessions, the share that reached a checkout,
        and of September's active members, the share who checked out at least once. Both run from
        opening the app to checkout, end to end, so neither is a step over the step before. The lines
        to type:

        ```python
        print(1 - s["search"].mean())
        sep = s[s["day"].str[:7] == "2026-09"].join(kev.drop_duplicates("session_id").set_index("session_id")["customer_id"])
        print(sep["checkout"].mean(), sep.groupby("customer_id")["checkout"].any().mean())
        ```
        '''),
        empty(),
        md('''
        **Kavya's review.** Kavya Nair, the senior analyst, asks: "Show me the rate before the window,
        show me the evidence, and reach the blend a second way: as the weighted average of your cohort
        rows, it has to match your direct count." The second route, typed into the cell below, must
        print the same three numbers as your direct count, to the last digit:

        ```python
        rows = grid.groupby(["month", "cohort"])["active"].agg(size="size", rate="mean").reset_index()
        rows["active_members"] = rows["size"] * rows["rate"]
        print(rows.groupby("month")["active_members"].sum() / rows.groupby("month")["size"].sum())
        ```
        '''),
        empty(),
        md('''
        **What to bring to the TA.** Three sentences: whether it is a cohort problem or an everyone
        problem, with the cohort that drives it and its size; the stage that owns the loss, the dates
        and the size of the fall; and the unit each of your rates uses. Then answer the head of
        Retail-Plus's second question, about the blended number that has not moved, in one line.

        **What comes next.** These sentences become the first lines of the Kalpa set's second page
        (`exercises/unguided/C2_W04_D04_kalpa_retail_plus_STUDENT.md`): sit its items 2 to 4, write the
        page, then sit the practice set.
        '''),
    ], timeout=300)


ALL = {"01": nb01, "02": nb02, "03": nb03, "04": nb04}

if __name__ == "__main__":
    for key in (sys.argv[1:] or ALL):
        ALL[key]()
        print(f"built notebook {key}")

# Test inputs and expected outcomes
# python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py
#     executes all four notebooks cold in content/W04/D4/notebooks/ and prints "built notebook 01" to "04"
# python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py 03
#     rebuilds notebook 03 alone
# python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py 05
#     KeyError: '05', since only 01 to 04 exist

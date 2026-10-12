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

**The ticket. Zomato Gold, Chennai, the membership and the app's order flow.** The membership
dashboard reports month-two retention for Chennai, the share of members two or more months past
their signup month who ordered in the month, as flat at 38 percent for June, July, August and
September 2026. Each signup cohort's own curve falls with age, and each cohort's month-one rate is
lower than the one before: January 58 percent, April 53, July 49, and August 31. The August cohort,
13,000 members, 2.6 times the 5,000 a month of January to July, grew out of a sale week with a
discounted first month. On Monday 14 September 2026 a new checkout flow shipped on Android; since
then members' add-to-cart to order conversion on Android fell from 58 to 44 percent, while members
on iOS went from 57 to 56 and non-members on Android from 52 to 51. **The ask, due Friday:** is it
a cohort problem or an everyone problem, which funnel stage owns the loss, and what should be fixed
first, with the evidence.
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

        The card holds twelve real members of the case data: four who joined in May, three in June
        and five in the August sale week. A cell is 1 when the member placed at least one order that
        calendar month and 0 when she placed none. A blank cell is a month before she joined, or the
        month she joined, which is month zero and is never counted. **Month one** is the first full
        calendar month after the signup month, so May's month one is June and August's is September.
        '''),
        code('''
        # The card as the data holds it, a blank where the month is not counted for that member.
        twelve.astype(object).where(twelve.notna(), "")
        '''),
        md('''
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
                      [f"{m} {ch}" for m, ch in zip(twelve["signup_month"], twelve["signup_channel"])])
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

        ## Why does a big new group keep an average flat while every group shrinks?

        A second toy (invented). Last month batch A had 100 members and 50 came: 50 percent. This
        month batch A falls to 40 of 100, and a new batch B of 400 joins with 210 coming, 52.5 percent.
        **Predict before you run:** does the blend rise, fall or hold?
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
        starts to fall.

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
        is month one. Two year-and-month strings become one count of months each, and the gap is the age.
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
        ordered at that age. **Predict before you run.** After month one, which way does each row run?

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
        to about 38.5 percent, then slides about 0.3 points a month. Each cohort also starts lower than
        the one before: 58 percent in January's month one, 49 in July's, and 31 in August's. Drawn as
        lines, the curves fall on top of each other after month one.
        '''),
        code('''
        # The curves: one line per cohort, month one on the left.
        fig, ax = plt.subplots(figsize=(8.4, 3.8))
        for c, row in tri.iterrows():
            row = row.dropna()
            ax.plot(row.index, 100 * row.values, marker="o", ms=3,
                    color="#D63A6A" if c == "2026-08" else "#5B3FD6", alpha=0.9 if c in ("2026-01", "2026-08") else 0.4)
        ax.axhline(38, ls="--", color="#C98A00"); ax.text(7.6, 38.6, "dashboard 38", color="#C98A00")
        ax.set_xlabel("months since joining"); ax.set_ylabel("percent who ordered")
        ax.set_title("Every curve falls; August starts at 31"); plt.show()
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
            print(month, f"{100 * weighted:.2f} weighted = {100 * direct:.2f} direct,", len(parts), "cohorts")
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
        aug = mm[(mm["cohort_month"] == "2026-08") & (mm["age"] == 1)].groupby("signup_channel")["active"].agg(["size", "mean"])
        print(aug.assign(mean=(100 * aug["mean"]).round(1)))
        check("counting everyone, September reads about 36 percent", round(100 * sep_all["active"].mean()) == 36)
        check("the sale-week members, not August as a whole, sit low",
              aug.loc["sale", "mean"] < 0.25 and abs(aug.loc["organic", "mean"] - tri.loc["2026-07", 1]) < 0.01)
        '''),
        md('''
        **What happened.** The answer is b: 17,248 of 48,000, 35.9 percent, printed as 36. The two
        readings differ by who is counted, and the August cohort is the whole difference. Split by how
        its members joined, the 4,973 organic August members kept 49 percent in month one, July's rate,
        while the 8,027 sale-week members kept 20 percent. When the August cohort reaches its second
        month in October, it enters the dashboard. If it falls from month one to month two as July's
        did, it enters at about 20 percent, and the dashboard drops to about 33 (between 32 and 34 if
        it enters anywhere from 17 to 24 percent).

        **The questions, answered.** (1) Every cohort falls with age, from 58 to 49 percent in month
        one across January to July and 31 for August, then to about 38.5 and slowly down. (2) The
        dashboard prints 38 from June to September. (3) September's 38 is the size-weighted average of
        seven cohorts, and the weighted average equals the direct count. (4) The 13,000-member sale
        cohort is outside the count; with it in, September reads 36.
        '''),
    ])


# ------------------------------------------------------------------------------------- notebook 03
def nb03():
    build(NB / "C2_W04_D04_03_funnel_STUDENT.ipynb", [
        md('''
        # Which funnel stage owns the loss, on which denominator, and for whom?

        **Week 4, Thursday, chapter 3 of 3 (L3).** Chapter 2 took the dashboard's flat 38 percent apart:
        every cohort falls with age, and the 13,000-member August cohort, whose 8,027 sale-week members
        kept 20 percent in month one, is outside the count until October. This notebook turns to the order flow,
        where the ticket says something changed on 14 September.
        ''' + TICKET + '''
        **Who needs the answer.** The membership lead and the app team's lead, who will say the stage the
        room blames is fine. Blaming the wrong stage sends engineers to fix a step that works.

        **The questions on the way.**

        1. What does each step of the funnel read in September, per session?
        2. Why does one step read above 100 percent, and what does it really read?
        3. Per session or per member: which unit answers which question?
        4. Where did add-to-cart to order fall after 14 September, and for whom?
        5. Which step inside the checkout changed, and how many orders a week does it cost?
        '''),
        code('''
        # Load the event log: one row per stage a session reached, August and September 2026.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECK + '''
        ev = pd.read_csv("../data/C2_W04_D04_events_STUDENT.csv.gz", parse_dates=["event_ts"])
        print(f"{len(ev):,} events in {ev['session_id'].nunique():,} sessions")
        check("no session reaches a stage twice", not ev.duplicated(["session_id", "stage"]).any())
        '''),
        md('''
        ## How does a funnel read, on numbers small enough to hold?

        A toy (invented): 100 app visits, 40 searches, 20 add-to-carts, 10 checkouts. Each step's rate
        divides it by the step before, so 40, 50 and 50 percent, and 10 percent of visits end in a
        checkout. If those 10 checkouts came from 50 sessions of 20 people, checkout is 10 of 50 per
        session and 10 of 20 per person: the same checkouts, two units, two numbers.
        '''),
        code('''
        # The toy's step rates, each one over the step before.
        toy = pd.Series({"visit": 100, "search": 40, "add_to_cart": 20, "checkout": 10})
        print((toy / toy.shift(1)).dropna().map("{:.0%}".format).to_string())
        check("the toy: 10 percent of visits end in a checkout", toy["checkout"] / toy["visit"] == 0.10)
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
        steps = pd.DataFrame({"sessions": per_session, "of the step before": (per_session / per_session.shift(1)).round(3)})
        steps
        '''),
        md('''
        **What happened.** The answer is b: 155,729 sessions opened a menu and 131,974 searched, so
        search to menu view reads 118 percent. **The plausible wrong answer** is to read that as the best
        step in the app, or, worse, to read the 34 percent at menu view to add-to-cart as the loss. **Why
        the 118 is wrong.** The home carousel opens a restaurant's menu without a search, so many menu
        views come from sessions that never searched: the step is skippable, and the ratio divides two
        counts of different sessions. **The fix** counts menu views only among sessions that searched.
        '''),
        code('''
        # The fix: of the sessions that searched, the share that went on to a menu.
        searched = set(sep.loc[sep["stage"] == "search", "session_id"])
        menu = set(sep.loc[sep["stage"] == "menu_view", "session_id"])
        print(f"sessions that searched and then opened a menu: {len(searched & menu) / len(searched):.1%}")
        print(f"menu sessions with no search (the carousel): {len(menu - searched):,}")
        check("among sessions that searched, the step reads under 100 percent", len(searched & menu) < len(searched))
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
        both = pd.DataFrame({"per session": (per_session / per_session.shift(1)),
                             "per member": (per_member / per_member.shift(1))}).dropna()
        ax = (100 * both).plot.bar(figsize=(8.4, 3.6), color=["#5B3FD6", "#4E38AB"], rot=0)
        ax.axhline(100, ls=":", color="grey"); ax.set_ylabel("percent of the step before")
        ax.set_title("One funnel, two units, September"); plt.show()
        (100 * both).round(1)
        '''),
        md('''
        **What happened.** The answer is c: 61 percent per member against 34 per session. Neither is
        wrong; each answers a different question, and a chart that does not name its unit invites
        the wrong one. Per member, search to menu view still reads 101 percent, because some members
        only ever used the carousel: counting members shrinks the artefact and leaves it in place. The
        skippable step, not the unit, makes the 118.
        '''),
        code('''
        check("per session, menu view to add-to-cart prints 34 percent", round(100 * both.loc["add_to_cart", "per session"]) == 34)
        check("per member, menu view to add-to-cart prints 61 percent", round(100 * both.loc["add_to_cart", "per member"]) == 61)
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
        flow = ev[ev["stage"].isin(["add_to_cart", "order_placed"])].copy()
        flow["side"] = (flow["event_ts"] >= "2026-09-14").map({False: "before", True: "after"})
        counts = flow.groupby(["is_member", "platform", "side", "stage"]).size().unstack()
        rate = (counts["order_placed"] / counts["add_to_cart"]).unstack()[["before", "after"]]
        (100 * rate).round(1)
        '''),
        code('''
        # The weekly view: the members' Android line breaks in the release week and no other line does.
        flow["week"] = flow["event_ts"].dt.to_period("W-SUN").dt.start_time
        fig, ax = plt.subplots(figsize=(8.6, 3.6))
        for (m, p), colour in [((True, "android"), "#D63A6A"), ((True, "ios"), "#5B3FD6"), ((False, "android"), "grey")]:
            g = flow[(flow["is_member"] == m) & (flow["platform"] == p)].groupby(["week", "stage"]).size().unstack()
            ax.plot(g.index, 100 * g["order_placed"] / g["add_to_cart"], marker="o", color=colour,
                    label=("members" if m else "non-members") + " on " + p)
        ax.axvline(pd.Timestamp("2026-09-14"), ls="--", color="#1A0F5C"); ax.legend(frameon=False)
        ax.set_ylabel("add-to-cart to order, percent"); ax.set_title("Weekly, with the release marked"); plt.show()
        check("members on Android: 58 before, 44 after", [round(100 * v) for v in rate.loc[(True, "android")]] == [58, 44])
        check("members on iOS: 57 before, 56 after", [round(100 * v) for v in rate.loc[(True, "ios")]] == [57, 56])
        check("non-members on Android: 52 before, 51 after", [round(100 * v) for v in rate.loc[(False, "android")]] == [52, 51])
        '''),
        md('''
        **What happened.** The answer is c. Members on Android fell from 58 to 44 percent, in the release
        week and not before; members on iOS held at 57 to 56, and non-members on Android at 52 to 51.
        **The plausible wrong answer** is "the drop is at add-to-cart to order for everyone, so the whole
        checkout flow is broken". The split by membership, platform and date puts it in one place, so
        the app team is right that the stage works everywhere else.

        ## Which step inside the checkout changed, and how many orders a week does it cost?

        Add-to-cart to order has two steps inside it: starting checkout, and completing the order once
        checkout has started.
        '''),
        code('''
        # Android members, the two steps inside the checkout, before and after the release.
        andm = ev[ev["is_member"] & (ev["platform"] == "android")].copy()
        andm["side"] = (andm["event_ts"] >= "2026-09-14").map({False: "before", True: "after"})
        n = andm.groupby(["side", "stage"]).size().unstack().loc[["before", "after"]]
        inside = pd.DataFrame({"cart to checkout start": n["checkout_start"] / n["add_to_cart"],
                               "checkout start to order": n["order_placed"] / n["checkout_start"]})
        fall = rate.loc[(True, "android"), "before"] - rate.loc[(True, "android"), "after"]
        lost_per_week = fall * n.loc["after", "add_to_cart"] / (17 / 7)
        print(f"orders a week not placed after the release: about {lost_per_week:,.0f}")
        check("starting checkout held at 80 percent; completing it fell", abs(inside.iloc[0, 0] - inside.iloc[1, 0]) < 0.01
              and inside.iloc[0, 1] - inside.iloc[1, 1] > 0.15)
        ax = (100 * inside.T).plot.bar(figsize=(6.8, 3.2), color=["#5B3FD6", "#D63A6A"], rot=0)
        ax.set_ylabel("percent of the step before"); ax.set_ylim(0, 100)
        ax.set_title("Android members: the step that changed"); plt.show()
        (100 * inside).round(1)
        '''),
        md('''
        **What happened.** Starting checkout held at 80 percent; completing an order once checkout had
        started fell from 72.5 to 55 percent. The loss sits in the last step of the new Android checkout,
        for members only, since non-members on Android held. That points at something in the new flow
        that only members see, which the app team can check. Android members added to a cart 22,841
        times in the 17 days after the release; at the old rate of 58 percent, about 1,317 more orders a
        week would have been placed. At an order value of Rs 400, an assumption anywhere from Rs 300 to
        Rs 500, that is about Rs 5.3 lakh of orders a week (Rs 4.0 to 6.6 lakh).

        **The questions, answered.** (1) Per session, the steps read 68, 118, 34, 80 and 64 percent.
        (2) Search to menu view reads 118 because the carousel skips search; among sessions that
        searched it reads 89. (3) Per session asks how often a menu visit becomes a cart (34 percent);
        per member asks how many browsing members ever added to a cart (61 percent). (4) The fall
        belongs to members on Android, 58 to 44 percent, from the release week. (5) The step that
        changed is checkout start to order placed, 72.5 to 55 percent, about 1,317 orders a week.
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
        in Week 2, with the date each membership started (`member_since`). `kalpa_events`: their app
        sessions from July to September 2026, one row per event (`visit`, `search`, `add_to_cart`,
        `checkout`). `kalpa_app_orders`: their app orders in the same months, copied from the
        warehouse. Kalpa counts a member as **active** in a month when she opened the app at least once
        that month, and **blended retention** for a month is the share of members who joined before
        that month who were active in it. Monday's lab fixed two windows: 20 August to 9 September,
        and 10 to 30 September, when the app's auto-reorder ran.

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
        cohort table, then blended retention for July, August and September. The lines to type:

        ```python
        mem["cohort"] = mem["member_since"].str[:7]
        active = kev.groupby(["customer_id", "month"]).size().gt(0).rename("active").reset_index()
        grid = mem.merge(pd.DataFrame({"month": ["2026-07", "2026-08", "2026-09"]}), how="cross")
        grid = grid[grid["cohort"] < grid["month"]].merge(active, on=["customer_id", "month"], how="left")
        grid["active"] = grid["active"].fillna(False).astype(bool)
        print(grid.pivot_table(index="cohort", columns="month", values="active", aggfunc=["sum", "count"]))
        print(grid.groupby("month")["active"].mean().round(3))
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
        rate counted per session and per member. The lines to type:

        ```python
        print(1 - s["search"].mean())
        sep = s[s["day"].str[:7] == "2026-09"].join(kev.drop_duplicates("session_id").set_index("session_id")["customer_id"])
        print(sep["checkout"].mean(), sep.groupby("customer_id")["checkout"].any().mean())
        ```
        '''),
        empty(),
        md('''
        **What to bring to the TA.** Three sentences: whether it is a cohort problem or an everyone
        problem, with the cohort that drives it and its size; the stage that owns the loss, the dates
        and the size of the fall; and the unit each of your rates uses. Then answer the head of
        Retail-Plus's second question, about the blended number that has not moved, in one line.

        **Kavya's review.** "Show me the baseline, show me the evidence, and reach it a second way:
        the blend as the weighted average of your cohort rows has to match your direct count."
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

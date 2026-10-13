"""Build Week 4 Thursday's nine notebooks, each executed cold in its own folder.

Each notebook takes its chapter's SECTION number. The five concept notebooks teach the row's
subtopics on invented examples read from the toy files in data/; the case notebooks apply them to
Zomato Gold; the lab re-runs them on Kalpa.

    01 Cohort construction, on the gym's register                         (SECTION 1, concept)
    02 Retention curves: shape and floor, on the same gym                 (SECTION 2, concept)
    03 Blended numbers against cohort truth, on the gym's dashboard       (SECTION 3, concept)
    04 Funnel stages, drop-off, denominators, on a college's admissions   (SECTION 4, concept)
    05 the twelve Gold members counted by hand                            (SECTION 5, case, L1)
    06 the cohort table, the curves and the blend decomposed              (SECTION 6, case, L2 and L3)
    07 the funnel, its two units, the artefact and the release            (SECTION 7, case, L3 and L4)
    08 The fix-first decision and its evidence, on the same college       (SECTION 8, concept)
    12 the Kalpa lab, with its three empty your-turn cells                (the TA lab, L1 to L3)

Run from the repository root, after the generator:
    python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py           all nine
    python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py 01 08     named ones

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


# The concept notebooks keep every check they run, so the last code cell can count them.
CHECKS = textwrap.indent('''
RESULTS = []
def check(name, ok):
    RESULTS.append(bool(ok)); print(("PASS  " if ok else "FAIL  ") + name)
''', " " * 8)


def step_map(steps, title):
    """The MAP cell of a concept notebook: the chapter's steps as a strip of boxes, the first one lit."""
    names = ", ".join('"' + s.replace("\n", "\\n") + '"' for s in steps)
    return code(f'''
    # The map: the chapter's steps in order; this notebook starts on the lit one and walks them all.
    steps = [{names}]
    fig, ax = plt.subplots(figsize=(8.8, 1.4))
    for i, s in enumerate(steps):
        ax.text(i, 0, s, ha="center", va="center", fontsize=10, color="white" if i == 0 else "#1A0F5C",
                bbox=dict(boxstyle="round,pad=0.6", fc="#1A0F5C" if i == 0 else "#EEEAFB", ec="#5B3FD6"))
    for i in range(1, len(steps)):
        ax.annotate("", xy=(i - 0.33, 0), xytext=(i - 0.67, 0), arrowprops=dict(arrowstyle="->", color="#5B3FD6"))
    ax.set_xlim(-0.6, len(steps) - 0.4); ax.set_ylim(-0.7, 0.7); ax.axis("off")
    ax.set_title("{title}"); plt.show()
    ''')


# ------------------------------------------------------------------------- notebook 01 (SECTION 1)
def nb01():
    build(NB / "C2_W04_D04_01_cohort_construction_STUDENT.ipynb", [
        md('''
        # Cohort construction: who joined when?

        **Week 4, Thursday, SECTION 1, the first of five concept notebooks.** The gym, its thirty
        members and their visits are invented for this chapter. Week 2 Thursday reshaped tables with
        `melt` and `pivot_table`; this notebook uses both to fix the month each member joined and to
        count every group at the same age. The case notebooks, 05 to 07, apply the same moves to
        Zomato Gold.

        **Who needs the answer.** The owner of a neighbourhood gym, who wants to know which month's
        joiners keep coming, so that a retention offer reaches the batch that needs it. Read by
        calendar month, the offer goes to the wrong batch.

        **The questions on the way.**

        1. Which batch looks best in April?
        2. What does each batch keep at each age?
        3. Why is the table a triangle?
        4. How does code count the same table?
        '''),
        code('''
        # Load the register: one row per member, one column per month, 1 if she visited, blank before she joined.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECKS + '''
        MONTHS = ["jan", "feb", "mar", "apr", "may", "jun"]
        roster = pd.read_csv("../data/C2_W04_D04_toy_gym_roster_STUDENT.csv", dtype={m: "Int64" for m in MONTHS})
        print("One branch's register, January to June 2026 (invented), in full:")
        print(roster.astype(object).where(roster.notna(), "").to_string(index=False))
        '''),
        step_map(["the register", "one row per\nmember-month", "the age of\neach row", "the cohort\ntable",
                  "compare at\nthe same age"], "Cohort construction in five steps"),
        md('''
        ## Which batch looks best in April?

        In April the owner reads the register's April row: 5 of the 10 January joiners visited, 5 of
        the 10 February joiners and 6 of the 10 March joiners, so the owner calls March the best
        batch. **Month one** is the first full calendar month after joining. The joining month is
        **month zero** and is never counted, since everyone visits the month they join. **Predict before
        you run.** Counted by months since joining, which batch keeps the most in its own month one?

        - a) March, as the owner reads it
        - b) February
        - c) January
        - d) All three keep the same share
        '''),
        code('''
        # The register drawn: dark visited, light did not, ringed the joining month; April, the owner's row, shaded.
        fig, ax = plt.subplots(figsize=(9.0, 3.2))
        for x, (_, r) in enumerate(roster.iterrows()):
            for y, m in enumerate(MONTHS):
                if pd.notna(r[m]):
                    ax.scatter(x, y, s=70, c="#5B3FD6" if r[m] == 1 else "#E4E1F1",
                               edgecolors="#D63A6A" if m == r["joined"] else "none", linewidths=1.6)
        ax.axhspan(2.5, 3.5, color="#FFF2D6", zorder=0)
        ax.set_yticks(range(6), ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]); ax.invert_yaxis()
        ax.set_xticks([4.5, 14.5, 24.5], ["joined in January", "joined in February", "joined in March"])
        ax.set_title("The register, one column per member (invented)"); plt.show()
        april = roster.groupby("joined", sort=False)["apr"].agg(visited="sum", members="count")
        print(april)
        check("April's row reads 5, 5 and 6 of 10, 16 of 30 in all",
              list(april["visited"]) == [5, 5, 6] and (april["visited"].sum(), april["members"].sum()) == (16, 30))
        '''),
        md('''
        ## What does each batch keep at each age?

        Count by hand before any code. A member's **age** in a month is how many months after her
        joining month it is, so a January joiner is at age one in February, and a March joiner is at
        age one in April. January's ten joiners are G01 to G10 in the printed register: down the `feb`
        column for those ten rows, 8 read 1; down `mar`, 6; down `apr`, `may` and `jun`, 5 each.
        February's ten, G11 to G20, start in `mar`, and March's ten, G21 to G30, start in `apr`. The
        next cell holds the hand count as numbers, counts the same table in code, and checks that the
        two agree.
        '''),
        code('''
        # The hand count, typed in; the same count in code; and the check that the two agree.
        by_hand = {"jan": [8, 6, 5, 5, 5], "feb": [7, 5, 3, 3], "mar": [6, 4, 3]}
        PLACE = {"jan": 0, "feb": 1, "mar": 2, "apr": 3, "may": 4, "jun": 5}
        long = roster.melt(id_vars=["member_id", "joined"], var_name="month",
                           value_name="visited").dropna()                 # one row per member per month
        long["visited"] = long["visited"].astype(int)
        long["age"] = long["month"].map(PLACE) - long["joined"].map(PLACE)  # joining month = age 0
        counted = long[long["age"] >= 1].pivot_table(index="joined", columns="age", values="visited",
                                                     aggfunc=["sum", "count"], sort=False)
        by_code = {c: [int(v) for v in row.dropna()] for c, row in counted["sum"].iterrows()}
        print(counted["sum"].astype("Int64"))
        check("the code's counts equal the hand count, batch by batch", by_code == by_hand)
        check("every cell divides by the whole batch of 10", set(counted["count"].stack().dropna()) == {10})
        '''),
        md('''
        **What happened.** The answer is c. At age one the batches keep 8, 7 and 6 of 10: January 80
        percent, February 70 and March 60. March, best in April, is the weakest at the same age, because
        April's row mixed January at age three, February at age two and March at age one, and its 16 of
        30 names no batch.

        ## Why is the table a triangle?

        Each row is a **cohort**, everyone who joined in the same month, and each column is an age. By
        June, March's joiners have lived only three ages, so their row is short, and a newer cohort's
        row is always shorter: that is why a cohort table is a triangle. **Named last, the formula:**
        retention of cohort c at age k = members of c who visited at age k ÷ the members of c. January
        at age two: 6 ÷ 10 = 60 percent. The next cell computes the shares with the same `pivot_table`
        and `aggfunc="mean"`: each cell is the mean of ones and zeros, which is the share who visited.
        '''),
        code('''
        # The cohort table as shares, drawn as a triangle: rows by joining month, columns by age.
        tri = long[long["age"] >= 1].pivot_table(index="joined", columns="age", values="visited",
                                                 aggfunc="mean", sort=False)
        fig, ax = plt.subplots(figsize=(6.4, 2.6))
        ax.imshow(tri.values, cmap="Purples", vmin=0.1, vmax=0.95, aspect="auto")
        for (c, a), v in tri.stack().dropna().items():
            ax.text(a - 1, list(tri.index).index(c), f"{100 * v:.0f}", ha="center", va="center",
                    color="white" if v >= 0.6 else "#1A0F5C")
        ax.set_xticks(range(tri.shape[1]), [f"age {a}" for a in tri.columns])
        ax.set_yticks(range(3), ["January", "February", "March"])
        ax.set_title("Percent of each batch who visited, by age (invented)"); plt.show()
        check("January's row reads 0.8, 0.6, 0.5, 0.5, 0.5", [round(v, 2) for v in tri.loc["jan"]] == [0.8, 0.6, 0.5, 0.5, 0.5])
        check("no batch's row rises with age", all((row.dropna().diff().dropna() <= 0).all() for _, row in tri.iterrows()))
        (100 * tri).round(0)
        '''),
        md('''
        **The plausible wrong answer.** "March is our best batch: 6 of 10 came in April." The decision
        it would mislead: the retention offer goes to the January and February joiners, while the batch
        that keeps the least at the same age gets nothing. **Why it is wrong.** One calendar month holds
        three ages at once. **The check** is the same-age column: at age one, March is last.

        **The rule as a function, and a second route.** The next cell wraps the count in `cohort_table`,
        then recounts January's row with a plain loop over its ten members and no `pivot_table`; the two
        must agree before the table is trusted. It ends by drawing the two readings side by side.
        '''),
        code('''
        # The rule as a function; January's row recounted by a loop; the two readings side by side.
        def cohort_table(register):
            """Share of each joining month's members who visited at each age; age zero left out."""
            rows = register.melt(id_vars=["member_id", "joined"], var_name="month", value_name="visited").dropna()
            rows["visited"] = rows["visited"].astype(int)
            rows["age"] = rows["month"].map(PLACE) - rows["joined"].map(PLACE)
            return rows[rows["age"] >= 1].pivot_table(index="joined", columns="age", values="visited",
                                                      aggfunc="mean", sort=False)

        jan = roster[roster["joined"] == "jan"]
        loop = [sum(1 for v in jan[m] if v == 1) / len(jan) for m in MONTHS[1:]]
        check("a loop over January's ten members gives the function's row",
              [round(v, 9) for v in loop] == [round(v, 9) for v in cohort_table(roster).loc["jan"]])
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 2.8), sharey=True)
        names = ["January", "February", "March"]
        a1.bar(names, 100 * april["visited"].astype(int).values / 10, color="#B8B2D6")
        a1.set_title("April, one calendar month")
        a2.bar(names, 100 * tri[1].values, color="#5B3FD6"); a2.set_title("Age one, the same age for each")
        a1.set_ylabel("percent who visited"); plt.show()
        '''),
        md('''
        ## Your turn: what does May's row say, read both ways?

        In May the owner reads the register again. **Your turn.** In the empty cell, count May's row by
        joining month, give each count its age, and say which batch a calendar reading of May ranks
        above which, and whether the same-age table agrees. Two lines to start from:

        ```python
        roster.groupby("joined", sort=False)["may"].sum()
        {j: PLACE["may"] - PLACE[j] for j in ["jan", "feb", "mar"]}
        ```
        '''),
        empty(),
        md('''
        **Check your cell against this one.** It prints May's row by joining month with the age of each
        count, then counts every check this notebook has run.
        '''),
        code('''
        # May's row by joining month, each count with its age; then every check in this notebook counted.
        may = roster.groupby("joined", sort=False)["may"].sum().astype(int)
        age_in_may = pd.Series({j: PLACE["may"] - PLACE[j] for j in may.index})
        print(pd.DataFrame({"visited in May, of 10": may, "age in May": age_in_may}))
        check("May's row reads 5, 3 and 4 of 10, at ages 4, 3 and 2",
              list(may) == [5, 3, 4] and list(age_in_may) == [4, 3, 2])
        print(f"{sum(RESULTS)} of {len(RESULTS)} checks pass")
        '''),
        md('''
        ## What does an analyst do every time a cohort table is built?

        1. A cohort is everyone who joined in the same month, and a member keeps her cohort for good.
        2. The joining month is age zero and is never counted; age one is the first full month after it.
        3. Every cell divides by the whole cohort, never by the members who visited the month before.
        4. Cohorts are compared at the same age, since one calendar month mixes ages and names no cohort.

        May's row says it again: read by calendar month it ranks March above February, 4 of 10 against
        3, while at the same age February keeps more, 7 against 6 at age one and 5 against 4 at age two.

        **In the interview.** [S] "Retention dropped; walk me through your investigation." The first
        move a strong candidate makes: "I'd fix each member's joining month and compare cohorts at the
        same age before I read any blended number."

        **What comes next.** Notebook 02 reads each row of this table as a curve and finds where it
        stops falling. Notebook 05 counts twelve Zomato Gold members the same way, by hand and then in
        code.
        '''),
    ])


# ------------------------------------------------------------------------- notebook 02 (SECTION 2)
def nb02():
    build(NB / "C2_W04_D04_02_retention_curves_STUDENT.ipynb", [
        md('''
        # Retention curves: shape and floor: where is the floor?

        **Week 4, Thursday, SECTION 2, the second of five concept notebooks.** The gym and its thirty
        members are invented, the same branch as notebook 01, which built its cohort table: January's
        joiners kept 80, 60, 50, 50 and 50 percent at ages one to five. This notebook reads each row as
        a curve.

        **Who needs the answer.** The gym's owner, who staffs the floor for the regulars. The level a
        batch stops falling at says how many joiners became regulars, and a level read too early staffs
        for members who are about to leave.

        **The questions on the way.**

        1. How fast does a batch fall?
        2. Where does it stop falling?
        3. When can a floor be called?
        4. Which batch is strongest, fairly?
        '''),
        code('''
        # Load the same register (invented), print it, and rebuild notebook 01's cohort table in one cell.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECKS + '''
        MONTHS = ["jan", "feb", "mar", "apr", "may", "jun"]
        roster = pd.read_csv("../data/C2_W04_D04_toy_gym_roster_STUDENT.csv", dtype={m: "Int64" for m in MONTHS})
        print("One branch's register, January to June 2026 (invented), in full:")
        print(roster.astype(object).where(roster.notna(), "").to_string(index=False))
        PLACE = {"jan": 0, "feb": 1, "mar": 2, "apr": 3, "may": 4, "jun": 5}
        long = roster.melt(id_vars=["member_id", "joined"], var_name="month", value_name="visited").dropna()
        long["visited"] = long["visited"].astype(int)
        long["age"] = long["month"].map(PLACE) - long["joined"].map(PLACE)
        tri = long[long["age"] >= 1].pivot_table(index="joined", columns="age", values="visited",
                                                 aggfunc="mean", sort=False)
        check("the rebuilt table is notebook 01's: 8, 6, 5, 5, 5 of 10 in January's row",
              [round(10 * v) for v in tri.loc["jan"]] == [8, 6, 5, 5, 5])
        (100 * tri).round(0)
        '''),
        step_map(["a row as\na curve", "its shape", "its floor", "churn,\ntwo ways", "rank at\nthe same age"],
                 "Reading a retention curve in five steps"),
        md('''
        ## How fast does a batch fall, and where does it stop?

        A **retention curve** is one cohort's row of the table, drawn by age. **Predict before you
        run.** January's ten joiners read 80, 60 and then 50 percent at ages one to three. What do they
        read at age five?

        - a) About 25 percent, the fall carrying on
        - b) 50 percent
        - c) Under 10 percent
        - d) Back up to 80 percent
        '''),
        code('''
        # The three batches as curves, one line each, age on the bottom.
        names = {"jan": "January", "feb": "February", "mar": "March"}
        colours = {"jan": "#1A0F5C", "feb": "#5B3FD6", "mar": "#D63A6A"}
        fig, ax = plt.subplots(figsize=(7.2, 3.4))
        for c, row in tri.iterrows():
            row = row.dropna()
            ax.plot(row.index, 100 * row.values, marker="o", color=colours[c], label=names[c])
        ax.set_xticks(range(1, 6)); ax.set_xlabel("age, months since joining"); ax.set_ylabel("percent who visited")
        ax.legend(frameon=False); ax.set_title("Three batches (invented): steep, then flat"); plt.show()
        print("January:", [round(100 * v) for v in tri.loc["jan"]])
        '''),
        md('''
        **What happened.** The answer is b: 80, 60, 50, 50, 50. A curve's **shape** is how fast it falls
        in its first ages: January lost 20 points, then 20, then 10, then none. A point is the gap
        between two percentages, so 80 to 60 is a fall of 20 points. Its **floor** is the level where it
        stops falling: January's is 50, the five of ten who made visiting a habit, and February's is 30.
        March reads 60, 40, 30 and is still falling, so its floor is not known yet.

        ## What share of a batch has stopped, counted two ways?

        **Churn** is the share lost. Counted so far, it is 100 less the retention: January has lost 20
        percent of its joiners by age one, 40 by age two and 50 by age three. Counted month to month, it
        divides those who stopped by those still visiting the month before: at age two, 2 of the 8 who
        visited at age one stopped, 25 percent. By hand, January's month-to-month churn reads 20, 25,
        16.7, 0 and 0. In this branch no member came back after stopping, which is what lets the
        month-to-month count divide by last month's visitors.
        '''),
        code('''
        # Churn two ways for January, against the hand count, and drawn side by side.
        jan = tri.loc["jan"]
        so_far = (100 * (1 - jan)).round(1)
        visiting = 10 * jan                                           # members still visiting, of 10
        before = pd.concat([pd.Series({0: 10.0}), visiting.iloc[:-1]]).values
        month_to_month = (100 * (before - visiting.values) / before).round(1)
        by_hand = [20, 25, 16.7, 0, 0]
        print(pd.DataFrame({"still visiting": (100 * jan).round(0), "churned so far": so_far,
                            "stopped since the month before": month_to_month}).T)
        check("month-to-month churn matches the hand count: 20, 25, 16.7, 0, 0", list(month_to_month) == by_hand)
        check("churn so far plus retention is 100 at every age", ((so_far + (100 * jan).round(1)) == 100).all())
        ax = pd.DataFrame({"churned so far": so_far.values, "stopped since the month before": month_to_month},
                          index=[f"age {a}" for a in jan.index]).plot.bar(figsize=(7.2, 3.0), rot=0,
                                                                         color=["#5B3FD6", "#D63A6A"])
        ax.set_ylim(0, 75); ax.legend(frameon=False, ncol=2, loc="upper left")
        ax.set_ylabel("percent"); ax.set_title("January's churn, counted two ways (invented)"); plt.show()
        '''),
        md('''
        ## When can a floor be called?

        **The plausible wrong answer.** After February's age two, 5 of 10, the owner staffed for a floor
        of five regulars. Ages three and four read 3 of 10, so the plan counted two regulars too many.
        **Why it is wrong.** One age after a big drop looks settled and is not. **The rule we use, this
        programme's own:** call a floor only when two ages in a row read the same share; until then the
        curve is still falling. The next cell writes the rule as a function, `floor_of`, and tests it on
        January's row and on February's row as the owner saw it after age two.
        '''),
        code('''
        # The two-ages rule as a function, tested on January and on February cut at age two.
        def floor_of(row):                                       # row: shares at ages 1, 2, 3, ...
            pairs = zip(row, row[1:])
            return next((a for a, b in pairs if a == b), None)   # None: still falling

        jan_row, feb_row = list(tri.loc["jan"].dropna()), list(tri.loc["feb"].dropna())
        print("January:", jan_row, "floor:", floor_of(jan_row))
        print("February as the owner saw it after age two:", feb_row[:2], "floor:", floor_of(feb_row[:2]))
        check("January's floor is 0.5, first read at age three", floor_of(jan_row) == 0.5 and jan_row.index(0.5) + 1 == 3)
        check("February cut at age two has no floor yet", floor_of(feb_row[:2]) is None)
        fig, ax = plt.subplots(figsize=(7.2, 3.0))
        ax.plot(range(1, len(feb_row) + 1), [100 * v for v in feb_row], marker="o", color="#5B3FD6", label="February")
        ax.axhline(100 * feb_row[1], ls="--", color="#D63A6A", label="the floor the owner read after age two")
        ax.set_xticks(range(1, len(feb_row) + 1)); ax.set_ylim(0, 90); ax.legend(frameon=False, loc="lower left")
        ax.set_xlabel("age"); ax.set_ylabel("percent who visited")
        ax.set_title("February (invented): a floor called too early"); plt.show()
        '''),
        md('''
        ## Which batch is strongest, fairly?

        The owner's April reading ranked March first, 6 of 10 against 5 and 5. Age two is the oldest
        age that all three batches have lived. **Predict before you run.** Ranked at age two, in which
        order do the batches fall?

        - a) March, then February, then January, as April's row ranked them
        - b) January, then February, then March
        - c) All three tie
        - d) February, then January, then March
        '''),
        code('''
        # The ranking at the same age, beside the ranking by one calendar month.
        april = roster.groupby("joined", sort=False)["apr"].sum().astype(int)
        age_two = tri[2]
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 2.8), sharey=True)
        a1.bar(list(names.values()), 10 * april.values, color="#B8B2D6"); a1.set_title("April, one calendar month")
        a2.bar(list(names.values()), 100 * age_two.values, color="#5B3FD6"); a2.set_title("Age two, the same age for all")
        a1.set_ylabel("percent who visited"); plt.show()
        print("age two:", {names[c]: round(100 * v) for c, v in age_two.items()})
        check("at age two the order is January, February, March: 60, 50, 40",
              [round(100 * v) for v in age_two] == [60, 50, 40])
        '''),
        md('''
        **What happened.** The answer is b: 60, 50 and 40 percent at age two. Ranked at the same age,
        January is strongest and March weakest, the reverse of April's calendar row. March reads 60, 40,
        30: it has lived only three ages and is still falling, so its floor is open. A batch that has not
        lived enough ages to show its floor is the plain-words version of what the IITGN faculty session
        W4-3 (tentative) calls censoring.

        ## Your turn: which floors can be called today?

        **Your turn.** In the empty cell, apply `floor_of` to February's full row and to March's row, and
        say which floor can be called and from which age.

        ```python
        floor_of(list(tri.loc["feb"].dropna())), floor_of(list(tri.loc["mar"].dropna()))
        ```
        '''),
        empty(),
        md('''
        **Check your cell against this one.** It prints both floors, then counts every check this
        notebook has run.
        '''),
        code('''
        # February's floor and March's open end; then every check in this notebook counted.
        feb_floor, mar_floor = floor_of(list(tri.loc["feb"].dropna())), floor_of(list(tri.loc["mar"].dropna()))
        print("February's floor:", feb_floor, "   March's floor:", mar_floor)
        check("February's floor is 0.3, read where ages three and four agree; March has none yet",
              feb_floor == 0.3 and mar_floor is None)
        check("March is still falling at its last age", tri.loc["mar"].dropna().diff().iloc[-1] < 0)
        print(f"{sum(RESULTS)} of {len(RESULTS)} checks pass")
        '''),
        md('''
        ## What does an analyst read off every retention curve?

        1. A retention curve is one cohort's row of the table, drawn by age.
        2. The shape says how fast a cohort leaves, and the floor says how many stay.
        3. Cohorts are ranked at the same age, never by the latest calendar month.
        4. A young cohort has no floor yet, since it has not lived the ages that would show one.

        **In the interview.** [F] "How would you use cohort analysis to find a retention issue?" Read
        each cohort's shape and floor, rank cohorts at the same age, and look for the cohort whose curve
        starts lower or never flattens.

        **What comes next.** Notebook 03 puts one number over every cohort and asks what it is made of.
        Notebook 06 draws Gold's eight curves on 53,089 members.
        '''),
    ])


# ------------------------------------------------------------------------- notebook 03 (SECTION 3)
def nb03():
    build(NB / "C2_W04_D04_03_blended_vs_cohort_truth_STUDENT.ipynb", [
        md('''
        # Blended numbers against cohort truth: what is a blend made of?

        **Week 4, Thursday, SECTION 3, the third of five concept notebooks.** The gym's dashboard and
        every count on it are invented. Notebook 02 read each batch's row as a curve: every batch falls,
        then holds at its floor. This notebook puts one number over all the gym's members and takes it
        apart.

        **Who needs the answer.** The gym's owner, who reads one dashboard number each month, the share
        of members who visited. A flat number read as "nothing changed" leaves a falling cohort with no
        action.

        **The questions on the way.**

        1. What does February's dashboard read?
        2. What are the cohorts doing under it?
        3. What is the dashboard's number made of?
        4. Which quick average is wrong?
        '''),
        code('''
        # Load the dashboard's counts (invented): one row per month and cohort, with members and visitors.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECKS + '''
        dash = pd.read_csv("../data/C2_W04_D04_toy_gym_dashboard_STUDENT.csv")
        print("The gym's dashboard counts, and a second gym's (invented), in full:")
        print(dash.to_string(index=False))
        gym = dash[dash["example"] == "gym"].assign(rate=lambda d: d["visited"] / d["members"])
        '''),
        step_map(["the direct\ncount", "each cohort's\nown rate", "the weighted\naverage", "the plain\nmean",
                  "a second\ngym"], "Taking a blended number apart in five steps"),
        md('''
        ## What does February's dashboard read?

        The dashboard counts a member from the month after she joins. January read 50 of 100 older
        members, 50 percent. In February the older members fall to 40 of 100, and the 400 January
        joiners, in their month one, visit at 52.5 percent. **Predict before you run.** What does
        February read?

        - a) It falls, because the older members fell
        - b) It rises, because 400 members joined
        - c) It holds at 50 percent
        - d) It cannot be read without more months
        '''),
        code('''
        # The direct count: everyone the dashboard counts each month, and the share who visited.
        direct = gym.groupby("month")[["visited", "members"]].sum()
        direct["percent"] = (100 * direct["visited"] / direct["members"]).round(2)
        print(direct)
        check("January reads 50 of 100 and February 250 of 500, 50 percent in both",
              direct["visited"].tolist() == [50, 250] and direct["members"].tolist() == [100, 500]
              and set(direct["percent"]) == {50.0})
        '''),
        md('''
        **What happened.** The answer is c. February counts 40 older members plus 210 January joiners
        who visited: 250 of 500, 50 percent, the same as January's 50 of 100. The older members fell ten
        points, from 50 to 40 percent, and the one number over everyone did not move, because 400
        joiners at their high early rate now carry four votes in five.

        ## What are the cohorts doing under it?

        The next cell prints each cohort's own rate and draws it under the dashboard's line.
        '''),
        code('''
        # Each cohort's own rate by month, drawn under the dashboard's flat line.
        print(gym[["month", "cohort", "members", "visited", "rate"]].to_string(index=False))
        older = gym[gym["cohort"] == "joined before 2026"].set_index("month")["rate"]
        joiners = gym[gym["cohort"] == "joined in January 2026"].set_index("month")["rate"]
        fig, ax = plt.subplots(figsize=(6.8, 3.2))
        ax.plot(["January", "February"], 100 * older.values, marker="o", color="#D63A6A", label="older members, 100")
        ax.plot(["February"], 100 * joiners.values, marker="s", ls="none", color="#5B3FD6", label="January joiners, 400")
        ax.plot(["January", "February"], direct["percent"].values, ls="--", color="#1A0F5C", label="the dashboard")
        ax.set_ylim(30, 60); ax.set_ylabel("percent who visited"); ax.legend(frameon=False, loc="lower left")
        ax.set_title("The dashboard holds while the older members fall (invented)"); plt.show()
        check("the older members fell ten points, 50 to 40 percent", round(100 * (older.iloc[0] - older.iloc[1])) == 10)
        '''),
        md('''
        ## What is the dashboard's number made of?

        By hand, February's 50 rebuilt from its two cohorts: 100 older members at 40 percent are 40
        visitors, and 400 joiners at 52.5 percent are 210; together 250 of 500. **Named last, the
        formula:** blend = sum of (cohort size × cohort rate) ÷ sum of cohort sizes = (100 × 0.40 + 400 ×
        0.525) ÷ 500 = 50 percent. The next cell writes the rule as a function, `blend`, and checks it
        against the hand count and the direct count; a rebuild that misses the count has left a cohort
        out or counted one twice.
        '''),
        code('''
        # The rule as a function, checked against the hand count and the direct count; then the stack drawn.
        def blend(sizes, rates):
            """One number over several cohorts: their rates averaged with each cohort's size as its weight."""
            return sum(n * r for n, r in zip(sizes, rates)) / sum(sizes)

        feb = gym[gym["month"] == "2026-02"]
        by_hand = (100 * 0.40 + 400 * 0.525) / 500
        weighted = blend(feb["members"], feb["rate"])
        check("the weighted average equals the hand count and the direct count, 0.5",
              abs(weighted - by_hand) < 1e-12 and abs(weighted - 250 / 500) < 1e-12)
        fig, ax = plt.subplots(figsize=(7.4, 3.4))
        for x, (month, part) in zip([0, 1.5], gym.groupby("month")):
            bottom = 0
            for _, r in part.iterrows():
                shade = "#D63A6A" if r["cohort"] == "joined before 2026" else "#5B3FD6"
                ax.bar(x, r["visited"], bottom=bottom, width=0.5, color=shade, edgecolor="white")
                ax.bar(x, r["members"] - r["visited"], bottom=bottom + r["visited"], width=0.5, color="#EEEAFB",
                       edgecolor="white")
                ax.text(x + 0.3, bottom + r["members"] / 2, f'{r["cohort"]}: {r["visited"]} of {r["members"]}',
                        va="center", fontsize=9)
                bottom += r["members"]
        ax.set_xticks([0, 1.5], ["January", "February"]); ax.set_xlim(-0.4, 3.2)
        ax.set_ylabel("members counted"); ax.set_title("Each month's count by cohort; dark visited (invented)"); plt.show()
        '''),
        md('''
        ## Which quick average is wrong?

        **The plausible wrong answer.** Averaging the two rates, (40 + 52.5) ÷ 2 = 46.25 percent, gives
        100 older members the same vote as 400 joiners. It is neither the count, 50 percent, nor the
        older members' own 40, and a report of "46.25 percent, down 3.75 points" describes no group in
        the gym. **The check that catches it:** the weighted average must equal the direct count, and
        the plain mean does not. The plain mean equals the blend only when every cohort is the same size.
        '''),
        code('''
        # The plain mean beside the blend, and the one case where the two agree: cohorts of equal size.
        plain = feb["rate"].mean()
        print(f"plain mean of the rates {100 * plain:.2f} percent; blend {100 * weighted:.0f} percent")
        check("the plain mean, 46.25, misses the blend", round(100 * plain, 2) == 46.25 and abs(plain - weighted) > 0.01)
        check("with two cohorts of 100 each, the plain mean and the blend agree",
              abs(blend([100, 100], feb["rate"]) - plain) < 1e-12)
        '''),
        md('''
        ## Where has this arithmetic been met before?

        Week 1 Thursday met it as a reversal: a total moved one way while each segment moved the other.
        A total that runs against its parts is called Simpson's paradox, after E. H. Simpson's 1951 paper
        in the Journal of the Royal Statistical Society; a flat blend over falling cohorts is its
        retention form.

        ## Your turn: what does a second gym's dashboard read?

        A second gym (invented) counts cohorts X and Y in its first month, and X, Y and a new cohort Z in
        its second. **Your turn.** In the empty cell, compute each month's blend twice, as the direct
        count and with `blend`, then the plain mean of the three rates in the second month, and say
        whether the dashboard moved and which cohorts fell.

        ```python
        second = dash[dash["example"] == "second gym"].assign(rate=lambda d: d["visited"] / d["members"])
        second.groupby("month")[["visited", "members"]].sum()
        ```
        '''),
        empty(),
        md('''
        **Check your cell against this one.** It computes both months both ways, draws the three cohorts
        under the blend, and counts every check this notebook has run.
        '''),
        code('''
        # The second gym both ways and its plain mean; the cohorts drawn; then every check counted.
        second = dash[dash["example"] == "second gym"].assign(rate=lambda d: d["visited"] / d["members"])
        blends = {}
        for month, part in second.groupby("month", sort=False):
            blends[month] = blend(part["members"], part["rate"])
            print(f"{month}: direct {100 * part['visited'].sum() / part['members'].sum():.1f}, "
                  f"weighted {100 * blends[month]:.1f}, plain mean {100 * part['rate'].mean():.1f}")
        last = second[second["month"] == "second month"]
        check("the second gym reads 48.0 then 47.8 percent, the same both ways",
              [round(100 * b, 1) for b in blends.values()] == [48.0, 47.8]
              and abs(blends["second month"] - last["visited"].sum() / last["members"].sum()) < 1e-12)
        fig, ax = plt.subplots(figsize=(6.8, 3.0))
        for c, colour in [("X", "#D63A6A"), ("Y", "#C98A00"), ("Z", "#5B3FD6")]:
            rows = second[second["cohort"] == c]
            ax.plot(rows["month"], 100 * rows["rate"], marker="o", color=colour, label=f"cohort {c}")
        ax.plot(list(blends), [100 * b for b in blends.values()], ls="--", color="#1A0F5C", label="the blend")
        ax.set_ylim(30, 65); ax.set_ylabel("percent who visited"); ax.legend(frameon=False, ncol=2)
        ax.set_title("A second gym (invented): X and Y fall, Z arrives"); plt.show()
        print(f"{sum(RESULTS)} of {len(RESULTS)} checks pass")
        '''),
        md('''
        ## What does an analyst do before believing one number over many cohorts?

        1. A number over several cohorts is their average weighted by cohort size.
        2. It moves when the mix of young and old cohorts moves, as well as when behaviour does.
        3. Rebuild it from its cohorts, and check the rebuild equals the direct count, before believing it.
        4. A plain mean of cohort rates is never the blend unless every cohort is the same size.

        The second gym says it again: X fell from 60 to 55 percent and Y from 40 to 36, while the
        dashboard moved only from 48.0 to 47.8, because Z joined 500 strong at 52.

        **In the interview.** [F] "Blended retention is flat while every cohort declines; how?" A
        growing young cohort at its high early rate carries more weight each month, so the average holds
        while each cohort falls; the fix is to read the cohorts at the same age.

        **What comes next.** Notebook 04 turns from who stays to which step people pass. Notebook 06
        rebuilds Gold's flat 38 from its cohorts the same way.
        '''),
    ])


# ------------------------------------------------------------------------- notebook 04 (SECTION 4)
def nb04():
    build(NB / "C2_W04_D04_04_funnel_denominators_STUDENT.ipynb", [
        md('''
        # Funnel stages, drop-off, denominators: which step owns a loss?

        **Week 4, Thursday, SECTION 4, the fourth of five concept notebooks.** The college, its two
        programmes and every count are invented. Notebook 03 rebuilt one number over all members as an
        average weighted by cohort size; this notebook turns from who stays to which step people pass.
        A **funnel** is a chain of steps people pass through, fewer at each, as every learner here passed
        through one to be admitted: applied, sat a test, shortlisted, accepted an offer, joined.

        **Who needs the answer.** The dean of the college, who has one admissions team for one fix this
        year. A step blamed because it is low sends the team to a step that works.

        **The questions on the way.**

        1. Which step owns this cycle's loss?
        2. What does each step read?
        3. Why does one step pass 100 percent?
        4. Per application or per applicant?
        '''),
        code('''
        # Load the admissions counts (invented): one row per programme, cycle, unit, group and stage.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECKS + '''
        adm = pd.read_csv("../data/C2_W04_D04_toy_admissions_STUDENT.csv")
        print("The college's admissions counts (invented), in full:")
        print(adm.to_string(index=False))
        STAGES = ["applied", "sat_test", "shortlisted", "accepted", "joined"]
        STEPS = ["test", "shortlist", "accept", "join"]
        '''),
        step_map(["the stages,\ncounted", "each step over\nthe step before", "the step\nthat moved",
                  "a step people\ncan skip", "the unit,\nnamed"], "Reading a funnel in five steps"),
        md('''
        ## Which step owns this cycle's loss?

        The college's main programme, last cycle against this one, counted in applications. **Predict
        before you run.** The next cell draws both cycles; which step owns this cycle's loss?

        - a) Shortlisting, the lowest step at 50 percent
        - b) Offer acceptance, 90 to 75 percent
        - c) Joining, at 80 percent
        - d) The test, which 200 applications skip
        '''),
        code('''
        # The two cycles' funnels as bars, counted in applications.
        main = adm.query("programme == 'main' and unit == 'applications' and group == 'all'")
        counts = main.pivot_table(index="stage", columns="cycle", values="count", aggfunc="sum", sort=False).reindex(STAGES)
        print(counts)
        ax = counts[[2025, 2026]].rename(columns={2025: "last cycle", 2026: "this cycle"}).plot.bar(
            figsize=(7.2, 3.2), rot=0, color=["#B8B2D6", "#5B3FD6"])
        ax.set_xticklabels(["applied", "sat the test", "shortlisted", "accepted", "joined"])
        ax.set_ylabel("applications"); ax.set_title("Last cycle and this cycle, stage by stage (invented)"); plt.show()
        '''),
        md('''
        ## What does each step read?

        By hand, this cycle, each step over the step before: 800 of 1,000 sat the test, 80 percent; 400
        of 800 were shortlisted, 50; 300 of 400 accepted, 75; 240 of 300 joined, 80. **Drop-off** is 100
        less the step rate: 20, 50, 25 and 20. The next cell writes the rule as a function, `step_rates`,
        runs it on both cycles and checks it against the hand count.
        '''),
        code('''
        # The rule as a function: each stage over the stage before; then drop-off and the overall rate.
        def step_rates(stage_counts):
            """Each stage's count over the stage before it, in the same unit."""
            c = list(stage_counts)
            return [b / a for a, b in zip(c, c[1:])]

        by_hand = [0.80, 0.50, 0.75, 0.80]
        table = (100 * pd.DataFrame({cycle: step_rates(counts[cycle]) for cycle in [2025, 2026]}, index=STEPS)).round(1)
        table["drop-off this cycle"] = 100 - table[2026]
        print(table)
        overall = {cycle: counts[cycle].iloc[-1] / counts[cycle].iloc[0] for cycle in [2025, 2026]}
        print("overall, last stage over the first:", {k: round(100 * float(v), 1) for k, v in overall.items()})
        check("the code's step rates equal the hand count: 80, 50, 75, 80",
              [round(r, 2) for r in step_rates(counts[2026])] == by_hand)
        product = 1.0
        for r in step_rates(counts[2026]):
            product *= r
        check("the step rates multiply to the overall, 0.24", abs(product - overall[2026]) < 1e-12 and round(overall[2026], 2) == 0.24)
        check("drop-off plus the step rate is 100 at every step", (table["drop-off this cycle"] + table[2026] == 100).all())
        '''),
        md('''
        **What happened.** The answer is b. Offer acceptance fell from 90 to 75 percent of those
        shortlisted, and every other step read the same in both cycles. Shortlisting reads 50 percent
        because the college selects half by design, and it did not move: a low step is a loss only when
        it moves. **Named last, the formulas.** Step rate = those who reached a step ÷ those who reached
        the step before, in one unit. Drop-off = 100 less the step rate. Overall conversion = the last
        step ÷ the first: 240 ÷ 1,000 = 24 percent this cycle against 28.8 last cycle, and the step
        rates multiply to it, 0.80 × 0.50 × 0.75 × 0.80 = 0.24.
        '''),
        code('''
        # Each step this cycle against the same step last cycle: one pair of bars differs.
        ax = table[[2025, 2026]].rename(columns={2025: "last cycle", 2026: "this cycle"}).plot.bar(
            figsize=(7.2, 3.0), rot=0, color=["#B8B2D6", "#5B3FD6"])
        ax.set_ylabel("percent of the step before"); ax.set_ylim(0, 120); ax.legend(frameon=False, ncol=2, loc="upper left")
        ax.set_title("Only offer acceptance moved (invented)"); plt.show()
        moved = (table[2026] - table[2025]).abs()
        check("only the acceptance step moved, by 15 points", list(moved[moved > 1].index) == ["accept"] and moved["accept"] == 15)
        '''),
        md('''
        ## Why does one step pass 100 percent?

        The college's sister programme (invented) makes its entrance test optional: of 1,000
        applications, 300 sat the test, and 320 were shortlisted, 230 who sat the test and 90 on board
        marks alone. **The plausible wrong answer.** "Test to shortlist reads 107 percent, our best
        step." 320 ÷ 300 puts 90 students who never sat the test over the test-takers. A rate above 100
        says the numerator holds people who never passed the denominator's step, so the step is one
        people can skip, and the 107 is an **artefact**, a number made by the way the count is taken.
        **The fix** counts the shortlist among those who sat the test.
        '''),
        code('''
        # The sister programme: the artefact, the fix, and a true number that answers another question.
        sis = adm.query("programme == 'sister'").set_index(["group", "stage"])["count"]
        artefact = sis[("all", "shortlisted")] / sis[("all", "sat_test")]
        fixed = sis[("sat the test", "shortlisted")] / sis[("all", "sat_test")]
        print(f"test to shortlist as printed: {100 * artefact:.1f} percent")
        print(f"shortlisted among those who sat the test: {100 * fixed:.1f} percent")
        print(f"shortlisted over applications: {100 * sis[('all', 'shortlisted')] / sis[('all', 'applied')]:.0f} percent")
        check("the printed step is above 100 percent and the fixed one below it", artefact > 1 > fixed)
        check("the fix reads 77 percent among test-takers", round(100 * fixed) == 77)
        '''),
        md('''
        ## Per application or per applicant?

        This cycle's 1,000 applications came from 900 applicants, since some applied in two rounds.
        **Predict before you run.** Joined over the top of the funnel, per applicant against per
        application, reads:

        - a) Higher per applicant
        - b) Lower per applicant
        - c) The same, since the joiners are the same 240
        - d) Above 100 percent per applicant
        '''),
        code('''
        # The same funnel in two units, side by side, with the overall rate in each.
        this = adm.query("programme == 'main' and cycle == 2026 and group == 'all'")
        units = this.pivot_table(index="stage", columns="unit", values="count", aggfunc="sum", sort=False).reindex(STAGES)
        print(units)
        by_unit = pd.DataFrame({u: step_rates(units[u]) for u in units.columns}, index=STEPS)
        fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.0), sharey=True)
        for ax, u, colour in zip(axes, ["applications", "applicants"], ["#5B3FD6", "#C98A00"]):
            ax.bar(STEPS, 100 * by_unit[u], color=colour)
            ax.set_title(f"per {u[:-1]}: overall {100 * units[u].iloc[-1] / units[u].iloc[0]:.1f} percent")
        axes[0].set_ylabel("percent of the step before"); plt.show()
        print((100 * by_unit).round(1))
        check("per applicant every step reads at least as high as per application",
              (by_unit["applicants"] >= by_unit["applications"]).all())
        check("joined per applicant 26.7 percent against 24.0 per application",
              [round(100 * units[u].iloc[-1] / units[u].iloc[0], 1) for u in ("applicants", "applications")] == [26.7, 24.0])
        '''),
        md('''
        **What happened.** The answer is a: 240 joiners are 24 percent of applications and 26.7 percent
        of applicants. A person can try more than once, so a funnel read per person reads at least as high
        at every step, and a chart names its unit.

        ## Your turn: did any step move in the cycle before last?

        **Your turn.** The file also holds 2024, the cycle before last. In the empty cell, run
        `step_rates` on 2024's counts, compute its overall rate, and say whether any step differs from
        2025's by more than a point.

        ```python
        step_rates(counts[2024]), counts[2024].iloc[-1] / counts[2024].iloc[0]
        ```
        '''),
        empty(),
        md('''
        **Check your cell against this one.** It sets 2024 beside 2025 step by step, then counts every
        check this notebook has run.
        '''),
        code('''
        # 2024 against 2025, step by step; then every check in this notebook counted.
        r24, r25 = step_rates(counts[2024]), step_rates(counts[2025])
        print(pd.DataFrame({"2024": [round(100 * r, 1) for r in r24], "2025": [round(100 * r, 1) for r in r25]}, index=STEPS))
        check("every 2024 step is within a point of 2025's, so the acceptance fall is new this cycle",
              all(abs(a - b) <= 0.01 for a, b in zip(r24, r25)))
        print(f"{sum(RESULTS)} of {len(RESULTS)} checks pass")
        '''),
        md('''
        ## What does an analyst check at every step of a funnel?

        1. Each step divides by the step before, in one named unit, and drop-off is 100 less that rate.
        2. The overall rate divides the last step by the first, and the step rates multiply to it.
        3. A low step is a loss only when it moves against its own past.
        4. A rate above 100 percent is a step people can skip, so count only those who passed the step before.

        **In the interview.** [D] "The team that owns the step says it is fine; what do you bring?" The
        step's rate against its own past, split by group and date, in a named unit, with a step beside it
        that held.

        **What comes next.** Notebook 07 reads Gold's order flow on the event log with the same four
        rules. Notebook 08 asks which of the college's two problems the dean fixes first.
        '''),
    ])


# ------------------------------------------------------------------------- notebook 08 (SECTION 8)
def nb08():
    build(NB / "C2_W04_D04_08_fix_first_evidence_STUDENT.ipynb", [
        md('''
        # The fix-first decision and its evidence: what does a call carry?

        **Week 4, Thursday, SECTION 8, the last of five concept notebooks.** The college and its counts
        are invented, the same as notebook 04, which found this cycle's loss at one step: offer
        acceptance fell from 90 to 75 percent while the lowest step, shortlisting, held at 50. The fee of
        Rs 1 to 1.5 lakh a year is an assumption, given with its range.

        **Who needs the answer.** The college's dean, who has one admissions team for one fix before the
        next cycle. The wrong fix leaves the lost students lost for another year.

        **The questions on the way.**

        1. Which of two problems goes first?
        2. Whom does the loss hurt, since when?
        3. How big is it, and what does it cost?
        4. What answers the objection?
        '''),
        code('''
        # Load the admissions counts (invented) and the fee assumption; print the rows split by home state.
        import pandas as pd
        import matplotlib.pyplot as plt
        ''' + CHECKS + '''
        adm = pd.read_csv("../data/C2_W04_D04_toy_admissions_STUDENT.csv")
        FEE_LAKH = {"low": 1.0, "middle": 1.2, "high": 1.5}       # an assumption: a first-year fee, in Rs lakh
        groups = adm.query("programme == 'main' and group in ['in-state', 'other states']")
        print("Shortlisted and accepted by home state, three cycles (invented), in full:")
        print(groups.to_string(index=False))
        '''),
        step_map(["the call", "the evidence", "the cost", "the objection", "what would\nchange it"],
                 "A fix-first page in five lines"),
        md('''
        ## Which of two problems goes first?

        The dean has two problems: 200 of 1,000 applications skip the entrance test every cycle, and
        offer acceptance fell from 90 to 75 percent this cycle. **Predict before you run.** Which goes
        first?

        - a) Both at once, split across the team
        - b) The test's no-show, the bigger count at 200
        - c) Offer acceptance
        - d) Neither, until the next cycle confirms it
        '''),
        code('''
        # The two problems across three cycles: the share that sat the test, and the share of offers accepted.
        main = adm.query("programme == 'main' and unit == 'applications' and group == 'all'")
        c = main.pivot_table(index="cycle", columns="stage", values="count", aggfunc="sum")
        two = pd.DataFrame({"sat the test": c["sat_test"] / c["applied"], "offers accepted": c["accepted"] / c["shortlisted"]})
        print((100 * two).round(1))
        ax = (100 * two).plot(marker="o", figsize=(6.8, 3.0), color=["#C98A00", "#5B3FD6"])
        ax.set_xticks(two.index); ax.set_ylim(60, 100); ax.set_ylabel("percent")
        ax.set_title("One problem never moved; one moved this cycle (invented)"); plt.show()
        check("the share that sat the test is 80 percent in every cycle", set((100 * two["sat the test"]).round(1)) == {80.0})
        check("acceptance read 90 for two cycles and 75 this cycle",
              list((100 * two["offers accepted"]).round(1)) == [90.0, 90.0, 75.0])
        '''),
        md('''
        **What happened.** The answer is c. The test's no-show has read 20 percent for three cycles, so it
        is how the test runs, and nothing changed there. A problem goes first when its step moved against
        its own past; a bigger count that never moved waits.

        ## Whom does the loss hurt, since when?

        The next cell splits acceptance by the student's home state, cycle by cycle, with the number of
        days each cycle allowed to pay the fee after the offer.
        '''),
        code('''
        # Acceptance by home state and cycle, with the days each cycle allowed to pay the fee.
        g = groups.pivot_table(index=["cycle", "group"], columns="stage", values="count", aggfunc="sum")
        rate = (g["accepted"] / g["shortlisted"]).unstack("group")
        deadline = groups.groupby("cycle")["fee_deadline_days"].first()
        print((100 * rate).round(1))
        ax = (100 * rate).plot.bar(figsize=(6.8, 3.0), rot=0, color=["#5B3FD6", "#D63A6A"])
        ax.set_xticklabels([f"{cy}, {d} days to pay" for cy, d in deadline.items()])
        ax.set_ylabel("offers accepted, percent"); ax.set_ylim(0, 120); ax.legend(frameon=False, ncol=2, loc="upper left")
        ax.set_title("Other-state acceptance fell when the deadline was cut (invented)"); plt.show()
        check("in-state acceptance held, 92 to 90", (100 * rate["in-state"]).max() - (100 * rate["in-state"]).min() < 2.5)
        check("other-state acceptance fell from 87 to 50", [round(100 * v) for v in rate["other states"].loc[[2025, 2026]]] == [87, 50])
        '''),
        md('''
        ## How big is it, and what does it cost?

        By hand: at last cycle's rates, the 250 in-state students shortlisted this cycle would have
        accepted 230, and the 150 from other states 130, so 360 in all; 300 accepted, so 60 fewer, 5
        in-state and 55 from other states. Since 80 percent of those who accept join, 60 fewer
        acceptances are 48 fewer students, and fees come from students who join. The next cell writes the
        size as a function, checks it against the hand count, reaches 48 a second way from the joiners
        counted directly, and prices it at the assumed fee.
        '''),
        code('''
        # The size as a function, the hand count checked, the second route, and the cost with its range.
        def lost_at_old_rates(shortlisted_now, accepted_now, old_rate):
            """Acceptances lost: what last cycle's rate would have kept, less what this cycle kept."""
            return (shortlisted_now * old_rate - accepted_now).round()

        by_hand = {"in-state": 5, "other states": 55}
        now, last = g.loc[2026], g.loc[2025]
        lost = lost_at_old_rates(now["shortlisted"], now["accepted"], last["accepted"] / last["shortlisted"])
        print(lost)
        check("the code's size equals the hand count: 5 in-state, 55 from other states", lost.to_dict() == by_hand)
        joiners_lost = lost.sum() * 0.8
        joined = c["joined"]
        check("two routes to 48 fewer students agree: 60 x 0.8, and 288 less 240",
              joiners_lost == joined[2025] - joined[2026] == 48)
        cost = {k: joiners_lost * v for k, v in FEE_LAKH.items()}
        print({k: f"Rs {v:.1f} lakh" for k, v in cost.items()})
        fig, ax = plt.subplots(figsize=(6.4, 2.2))
        ax.barh(["fee income lost a year"], [cost["middle"]], color="#5B3FD6")
        ax.errorbar([cost["middle"]], [0], xerr=[[cost["middle"] - cost["low"]], [cost["high"] - cost["middle"]]],
                    color="#1A0F5C", capsize=8)
        ax.text(cost["high"] + 1, 0.25, f"Rs {cost['low']:.0f} to {cost['high']:.0f} lakh", va="center")
        ax.set_xlabel("Rs lakh"); ax.set_xlim(0, 95)
        ax.set_title("The cost at the assumed fee, with its range"); plt.show()
        '''),
        md('''
        **The plausible wrong answer.** "Fix the test first: 200 applications never sit it." The decision
        it would mislead: the one admissions team spends a cycle on a step that has read 80 percent for
        three cycles, while 55 students from other states a cycle keep turning the offer down. **Why it is
        wrong.** The step never moved, so fixing it wins back nothing lost this cycle.

        ## What answers the objection?

        The admissions office says: "Our offers go out within two days of the shortlist, every one, so
        acceptance is not our problem." **What is true.** The offers held: every shortlisted student got
        an offer on time in both cycles. **What answers it.** The fall sits after the offer, in the days
        allowed to pay, for one group, from the cycle the deadline shrank from 21 to 7 days. Concede the
        true part, then bring the split.

        ## Your turn: was other-state acceptance falling before the deadline changed?

        The page's last line names the fact that would change the call: other-state acceptance already
        falling before the deadline was cut. **Your turn.** In the empty cell, print other-state
        acceptance for 2024 and 2025 from `rate`, and say whether the fall began before 2026.

        ```python
        rate["other states"]
        ```
        '''),
        empty(),
        md('''
        **Check your cell against this one.** It prints the two cycles before the cut, then the five-line
        page written from the numbers, then counts every check this notebook has run.
        '''),
        code('''
        # The two cycles before the cut; the five-line page printed from the numbers; every check counted.
        before = (100 * rate["other states"].loc[[2024, 2025]]).round(1)
        print(before)
        check("other-state acceptance read 86.4 and 86.7 before the cut, so it was not already falling",
              list(before) == [86.4, 86.7])
        acc = 100 * two["offers accepted"]
        page = [
            "The call. Give other-state offers a longer fee deadline first; the test's no-show waits, since it never moved.",
            f"The evidence. Offer acceptance fell from {acc[2025]:.0f} to {acc[2026]:.0f} percent; for other-state students "
            f"from {100 * rate['other states'][2025]:.0f} to {100 * rate['other states'][2026]:.0f}, while in-state held at "
            f"{100 * rate['in-state'][2025]:.0f} to {100 * rate['in-state'][2026]:.0f} on the same step, from the cycle the "
            f"deadline went from {deadline[2025]} to {deadline[2026]} days.",
            f"The cost. {lost.sum():.0f} fewer acceptances, {joiners_lost:.0f} fewer students, Rs {cost['low']:.0f} to "
            f"{cost['high']:.0f} lakh of first-year fees at an assumed Rs 1 to 1.5 lakh.",
            "The objection. Offers did go out in two days, which is true; the fall came after the offer, for one group, after one change.",
            f"What would change it. Other-state acceptance falling before the deadline changed; it read {before.iloc[0]:.0f} "
            f"and {before.iloc[1]:.0f} in the two cycles before.",
        ]
        print("\\n".join(f"{i}. {line}" for i, line in enumerate(page, 1)))
        print(f"\\n{sum(RESULTS)} of {len(RESULTS)} checks pass")
        '''),
        md('''
        ## What does a fix-first call carry to survive the meeting?

        1. **The call**, in one sentence: what gets fixed first, and what waits.
        2. **The evidence**: the step against its own past, the group it hurts and the date it started,
           with a comparator on the same step that held.
        3. **The cost**, counted in the unit the business is paid in, with every assumption named and
           ranged.
        4. **The objection**, with its true part conceded before the split that answers it.
        5. **What would change it**: the one fact that would reverse the order.

        **In the interview.** [D] "What evidence do you bring when the owning team says its step is
        fine?" The step against its own past, the group and the date, a comparator that held, the size
        with its range, and the true part of their claim conceded.

        **What comes next.** SECTION 9 writes the same five lines for Zomato Gold's two problems, from
        notebooks 06 and 07, and the lab's Kalpa set asks for them on Kalpa.
        '''),
    ])


# ------------------------------------------------------------------- notebook 05 (SECTION 5, case)
def nb05():
    build(NB / "C2_W04_D04_05_case_cohort_construction_STUDENT.ipynb", [
        md('''
        # Cohort construction on twelve Gold members: who entered when?

        **Week 4, Thursday, SECTION 5, the first case notebook (L1, counted by hand).** It applies
        Cohort construction, which notebook 01 taught on an invented gym: fix the month each member
        joined, leave that month out as month zero, and compare every group at the same age, since one
        calendar month mixes ages.
        ''' + TICKET + '''
        **Who needs the answer.** The membership lead, who reads the dashboard every month and has to
        say on Friday whether Gold has a cohort problem or an everyone problem. A wrong call sends the
        fix to the wrong place.

        **The questions on the way.**

        1. Which of the twelve members ordered in each month since they joined?
        2. What does each signup group keep, month one, month two and on?
        3. What does the dashboard's way of counting say about the twelve, and what does it leave out?
        '''),
        code('''
        # Load the twelve members SECTION 5 counts, and the full tables to prove they are real rows.
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
        ## Which of the twelve members ordered in each month since they joined?

        The card holds twelve members picked from the case data, which is synthetic like all of it,
        to show the pattern on one page: four who joined in May, three in June and five who joined in
        the August sale week on its discount. On all 53,089 members (notebook 06), May's month one is
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
        column per month, into one row per member per month, so each row can carry its own age, as
        notebook 01 did with the gym's register. Each month gets its place among June to September:
        June 0, July 1, August 2, September 3. A signup month gets a place on the same scale, so May,
        the month before June, is -1, June is 0 and August is 2. Age is the month's place minus the
        signup month's: for a May member, June is 0 - (-1) = 1, her month one. One `pivot_table` with
        two functions, `sum` and `count`, then gives two tables side by side: how many ordered at each
        age, and how many were counted.

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
        check("August keeps 0 of 5 in month one", kept.loc["Aug", 1] == 0)
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
        2 of 3 and the August sale-week members 0 of 5. Each group falls as it ages: May runs 3, 2, 1,
        1 of 4, and June runs 2, 1, 1 of 3. Each later group also starts lower. Fixing the entry
        moment, the month a member joined, is what lets the three be compared at all. Drawn by age, as
        notebook 01 drew the gym's batches:
        '''),
        code('''
        # Each signup group's share by age: every group falls, and each later group starts lower.
        share = by_age["sum"] / by_age["count"]
        names = {"May": "May, 4 members", "Jun": "June, 3 members", "Aug": "August sale week, 5 members"}
        fig, ax = plt.subplots(figsize=(7.0, 3.0))
        for g, colour in [("May", "#1A0F5C"), ("Jun", "#5B3FD6"), ("Aug", "#D63A6A")]:
            row = share.loc[g].dropna()
            ax.plot(row.index, 100 * row.values, marker="o", color=colour, label=names[g])
        ax.set_xticks(range(1, 5)); ax.set_xlabel("months since joining"); ax.set_ylabel("percent who ordered")
        ax.set_ylim(-5, 100); ax.legend(frameon=False)
        ax.set_title("The card's three groups at the same age"); plt.show()
        '''),
        md('''
        ## What does the dashboard's way of counting say about the twelve, and what does it leave out?

        The dashboard counts a member from her second month after joining: in each reporting month, it
        takes every member two or more months past her signup month and asks what share ordered. **Predict
        before you run.** On the twelve, what does the dashboard's way read in August and in September?

        - a) It falls from August to September, because the sale-week members ordered so little
        - b) It reads 2 of 7 in both months, and the five sale-week members are not in it
        - c) It rises, because the sale-week members are new
        - d) It reads 2 of 12 in both months
        '''),
        code('''
        # Each reporting month counted two ways: from month two on (the dashboard), and everyone.
        ways, shares = {}, {}
        for m in ["jul", "aug", "sep"]:
            dash = long[(long["month"] == m) & (long["age"] >= 2)]
            every = long[(long["month"] == m) & (long["age"] >= 1)]
            ways[m] = {"dashboard, month two on": f'{dash["ordered"].sum()} of {len(dash)}',
                       "everyone who joined before": f'{every["ordered"].sum()} of {len(every)}'}
            shares[m] = {"dashboard, month two on": 100 * dash["ordered"].mean(),
                         "everyone who joined before": 100 * every["ordered"].mean()}
        ax = pd.DataFrame(shares).T.plot.bar(figsize=(7.0, 3.0), rot=0, color=["#5B3FD6", "#C98A00"])
        ax.set_xticklabels(["July", "August", "September"]); ax.set_ylabel("percent who ordered")
        ax.set_ylim(0, 100); ax.legend(frameon=False)
        ax.set_title("The twelve, counted two ways"); plt.show()
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
        check("everyone who joined before September: 2 of 12 ordered", ways["sep"]["everyone who joined before"] == "2 of 12")
        '''),
        md('''
        **What happened.** The answer is b. Counted the dashboard's way, 2 of 7 members ordered in
        August and 2 of 7 in September: the number did not move, though five new members arrived and
        none of them ordered. They are outside the count until their second month, October.
        Counting everyone who joined before September gives 2 of 12. On the full data, notebook 06
        finds the same two readings: 38 percent the dashboard's way, 36 counting everyone, and takes
        the 38 apart as notebook 03 took the gym's dashboard apart.

        **The questions, answered.** (1) The card shows who ordered each month; blanks are months
        before or at joining. (2) May kept 3, 2, 1, 1 of 4, June 2, 1, 1 of 3, and the August sale week
        0 of 5 in month one. (3) The dashboard's way read 2 of 7 in August and in September, with the
        five sale-week members outside its count.
        '''),
    ])


# ------------------------------------------------------------------- notebook 06 (SECTION 6, case)
def nb06():
    build(NB / "C2_W04_D04_06_case_retention_and_blend_STUDENT.ipynb", [
        md('''
        # Retention curves and blended numbers on 53,089 members: what is the 38 made of?

        **Week 4, Thursday, SECTION 6, the second case notebook (L2 and L3).** It applies three of the
        morning's topics to every Gold member: Cohort construction (notebook 01), Retention curves:
        shape and floor (notebook 02) and Blended numbers against cohort truth (notebook 03). SECTION 5
        counted twelve members by hand: each signup group fell as it aged, the August sale-week members
        kept 0 of 5 in month one, and the dashboard's way of counting read 2 of 7 in August and in
        September, because it leaves a member out until her second month. This notebook does the same
        on every member.
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
        print(parts.assign(rate=(100 * parts["rate"]).round(1)))
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

        ## Depth, for self-study: what will October read once the August cohort is counted?

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

        ## Depth, for self-study: is September's number the same in every zone?

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


# ------------------------------------------------------------------- notebook 07 (SECTION 7, case)
def nb07():
    build(NB / "C2_W04_D04_07_case_funnel_denominators_STUDENT.ipynb", [
        md('''
        # Funnel stages, drop-off, denominators on the event log: which stage owns the loss?

        **Week 4, Thursday, SECTION 7, the third case notebook (L3 and L4).** It applies Funnel stages,
        drop-off, denominators, which notebook 04 taught on an invented college. SECTION 6 took the
        dashboard's flat 38
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
        ## Which rules from SECTION 4 does the event log need?

        Funnel stages, drop-off, denominators, on the college in notebook 04, left four rules. Each step
        divides by the step before, in one named unit, and drop-off is 100 less that rate. The overall
        rate divides the last step by the first, and the step rates multiply to it. A low step is a loss
        only when it moves against its own past. A rate above 100 percent is a step people can skip.
        Gold's event log needs all four, in that order.

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
        check("per session, menu view to add-to-cart prints 34 percent", round(100 * both.loc["menu_view to add_to_cart", "per session"]) == 34)
        check("per member, menu view to add-to-cart prints 61 percent", round(100 * both.loc["menu_view to add_to_cart", "per member"]) == 61)
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
        print((100 * rate).round(1))
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
        # The size, step by step: the fall times the carts, then per day and per week.
        carts_after = n.loc["after", "add_to_cart"]
        fall = rate.loc[(True, "android"), "before"] - rate.loc[(True, "android"), "after"]
        lost_17 = fall * carts_after
        print(f"{fall:.2f} x {carts_after:,} carts = {lost_17:,.0f} orders in 17 days, "
              f"{lost_17 / 17:,.0f} a day, {lost_17 / 17 * 7:,.0f} a week")
        # The same loss counted in orders placed, which keeps any failed cart that came back as a later order:
        # Android members' orders a week against the change iOS members and non-members on Android showed.
        per_week = flow[flow["stage"] == "order_placed"].groupby(["is_member", "platform", "side"]).size().unstack()
        per_week = per_week.assign(before=per_week["before"] / 44 * 7, after=per_week["after"] / 17 * 7)
        change = per_week["after"] / per_week["before"] - 1
        for who, name in [((True, "ios"), "iOS members"), ((False, "android"), "non-members on Android")]:
            expected = per_week.loc[(True, "android"), "before"] * (1 + change.loc[who])
            print(f"against {name} ({change.loc[who]:+.0%}): {expected - per_week.loc[(True, 'android'), 'after']:,.0f} "
                  f"orders a week lost")
        check("about 1,317 a week from the carts; 1,133 to 1,266 counted in orders placed",
              round(lost_17 / 17 * 7) == 1317 and round(per_week.loc[(True, "android"), "before"] * (1 + change.loc[(False, "android")])
                                                        - per_week.loc[(True, "android"), "after"]) == 1133)
        '''),
        md('''
        **What happened.** Starting checkout held at 80 percent; completing an order once checkout had
        started fell from 72.5 to 55 percent. The two multiply back to the ticket's numbers: 0.80 x
        72.5 = 58 before, and 0.80 x 55 = 44 after. **The size.** Android members added to a cart
        22,841 times in the 17 days after the release. At 58 percent instead of 44, 0.14 x 22,841 is
        about 3,198 more orders in 17 days, about 188 a day, about 1,317 a week, against about 5,064
        Android member orders a week before the release: about a quarter of them.

        **What happened.** About 1,317 orders a week if none of the failed carts came back as a later
        order. Counted in orders placed, which keeps the ones that did, Android members' weekly orders
        fell 18 percent while iOS members' rose 7 and non-members' on Android 4: a loss of 1,266 a week
        against iOS members and 1,133 against non-members, so the range is 1,133 to 1,317. At an order
        value of Rs 400, an assumption anywhere from Rs 300 to Rs 500, that is Rs 3.4 to 6.6 lakh of
        orders a week, Rs 5.3 lakh at 1,317 and Rs 400. That is order value: Zomato keeps only its
        commission and fees from it, so the loss to Zomato itself is a share of that range.

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
        after = nxt["t"] >= "2026-09-14"
        retry = nxt.groupby(after)["within_a_day"].agg(["mean", "size", "sum"])
        retry = retry.assign(failed_a_week=retry["size"] / [44, 17] * 7, came_back_a_week=retry["sum"] / [44, 17] * 7)
        print(retry.round(3))
        check("the share of failures followed by an order within a day did not rise",
              retry.loc[True, "mean"] <= retry.loc[False, "mean"])
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
        a checkout with no order, the member ordered within a day 36.5 percent of the time before the
        release and 35.1 after; failures nearly doubled, from 1,921 to 3,386 a week, so more came back,
        1,189 a week against 701, which is why the size's floor is counted in orders placed. Held
        fixed, Android members also ordered less each, 1.45 to 1.24 orders per
        ordering member from August to September, while iOS held at 1.44 and 1.45. Over every ordering
        member the same ratio reads 1.36 to 1.20 on Android and 1.34 to 1.40 on iOS, and that iOS "rise"
        is the mix of cohorts again.

        **The questions, answered.** (1) Per session, the steps read 68, 118, 34, 80 and 64 percent.
        (2) Search to menu view reads 118 because the carousel skips search; among sessions that
        searched it reads 89. (3) Per session asks how often a menu visit becomes a cart (34 percent);
        per member asks how many browsing members ever added to a cart (61 percent). (4) The fall
        belongs to members on Android, 58 to 44 percent, from the release week. (5) The step that
        changed is checkout start to order placed, 72.5 to 55 percent, about 1,133 to 1,317 orders a
        week. (6) The same-step comparators, the cohorts held fixed, the order records and the size of
        each sample all leave the call standing.
        '''),
    ])


# ------------------------------------------------------------------------ notebook 12 (the TA lab)
def nb12():
    build(NB / "C2_W04_D04_12_kalpa_lab_cohort_and_funnel_STUDENT.ipynb", [
        md('''
        # The Kalpa lab, cohort and funnel: is Retail-Plus losing everyone or the monsoon-sale members?

        **Week 4, Thursday, the TA lab: the day's five topics on Kalpa Retail.** It re-runs Cohort
        construction (notebook 01), Retention curves: shape and floor (02), Blended numbers against
        cohort truth (03), Funnel stages, drop-off, denominators (04) and The fix-first decision and its
        evidence (08), as SECTIONs 5 to 9 ran them on Zomato Gold. Kalpa Retail is the
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
        ## Is every Retail-Plus cohort falling, and what does blended retention read?

        **Your turn.** Take each member's cohort, the month her membership started, and her active months. Build the
        cohort table by age, as the morning did, then blended retention for July, August and
        September. What each line does: `how="cross"` pairs every member with each of the three months;
        the next line keeps only the months after she joined and adds whether she was active; a month
        with no session has no row in `active`, so `fillna(False)` sets it to not active; the age is
        the gap in months, written as year x 12 + month as in notebook 06. The lines to type:

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
        ## Where in the app is the loss, and when?

        **Your turn.** Add-to-cart to checkout, per session, in three stretches: before 20 August, Monday's comparison
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
        ## Which step can members skip, and which unit does each rate use?

        **Your turn.** Using `s` from the cell above: the share of sessions with no search, and September's checkout
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
        rows, it has to match your direct count." The second route, typed into the last cell, must
        print the same three numbers as your direct count, to the last digit:

        ```python
        rows = grid.groupby(["month", "cohort"])["active"].agg(size="size", rate="mean").reset_index()
        rows["active_members"] = rows["size"] * rows["rate"]
        print(rows.groupby("month")["active_members"].sum() / rows.groupby("month")["size"].sum())
        ```

        **What to bring to the TA.** Three sentences: whether it is a cohort problem or an everyone
        problem, with the cohort that drives it and its size; the stage that owns the loss, the dates
        and the size of the fall; and the unit each of your rates uses. Then answer the head of
        Retail-Plus's second question, about the blended number that has not moved, in one line.

        **What comes next.** These sentences become the first lines of the Kalpa set's second page
        (`exercises/unguided/C2_W04_D04_kalpa_retail_plus_STUDENT.md`): sit its items 2 to 4, write the
        page, then sit the practice set.
        '''),
        empty(),
    ], timeout=300)


ALL = {"01": nb01, "02": nb02, "03": nb03, "04": nb04, "05": nb05, "06": nb06, "07": nb07, "08": nb08, "12": nb12}

if __name__ == "__main__":
    for key in (sys.argv[1:] or ALL):
        ALL[key]()
        print(f"built notebook {key}")

# Test inputs and expected outcomes
# python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py
#     executes all nine notebooks cold in content/W04/D4/notebooks/ and prints "built notebook 01" to "12"
# python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py 03 08
#     rebuilds notebooks 03 and 08 alone
# python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py 09
#     KeyError: '09', since the notebooks are 01 to 08 and 12

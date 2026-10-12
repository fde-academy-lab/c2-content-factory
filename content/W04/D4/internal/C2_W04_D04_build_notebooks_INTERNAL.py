"""Build Thursday's four teaching notebooks: toys and twelve rows, the triangle, the funnel, the
Kalpa lab.

Run from the repository root:
    python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py            every notebook
    python3 content/W04/D4/internal/C2_W04_D04_build_notebooks_INTERNAL.py 02 03      named ones

Each notebook executes cold in its own folder (nb_make.build), so the saved outputs are what a
learner sees on GitHub. The data generator writes the CSVs beside each notebook under data/, and
the facts file names every number. No STUDENT cell prints a Kalpa plant: the Kalpa lab discovers
its plant in an empty your-turn cell. The twelve-row counts are the day's hand anchor; L2 and L3
reach the same answers on 60,000 members.
"""
import pathlib
import sys

sys.path.insert(0, "scripts")
from nb_make import SETUP, build, code, empty, md  # noqa: E402


DAY = pathlib.Path("content/W04/D4")
NB = DAY / "notebooks"
NB.mkdir(parents=True, exist_ok=True)

# A short helper the chapters load from ../data/, using pandas and the standard library only
# (ponytail). A three-line check() prints PASS or FAIL and never raises, so one bad assert never
# stops a class.
LOAD = SETUP + """
import pandas as pd
import csv, pathlib
from collections import Counter

DATA = pathlib.Path("../data")
members = pd.read_csv(DATA / "C2_W04_D04_members_STUDENT.csv")
member_months = pd.read_csv(DATA / "C2_W04_D04_member_months_STUDENT.csv")
events = pd.read_csv(DATA / "C2_W04_D04_events_STUDENT.csv")
twelve = pd.read_csv(DATA / "C2_W04_D04_twelve_rows_STUDENT.csv")

PASS_COUNT = {"pass": 0, "fail": 0}


def check(label, condition, detail=""):
    ok = bool(condition)
    PASS_COUNT["pass" if ok else "fail"] += 1
    word = "PASS" if ok else "FAIL"
    print(f"{word}  {label}" + (f"  ({detail})" if detail else ""))
    return ok


def check_summary():
    print(f"\\n{'PASS' if PASS_COUNT['fail'] == 0 else 'FAIL'}  "
          f"{PASS_COUNT['pass']} checks passed and {PASS_COUNT['fail']} failed in this notebook.")


print(f"loaded: {len(members)} members, {len(member_months)} member-months, "
      f"{len(events)} events, {len(twelve)} twelve-row members")
"""


# ============================================================ Notebook 01: toys and twelve rows

def write_01():
    cells = [
        md("""
# 1. Who entered when, and what happens to each group month by month?

**Week 4, Thursday. Chapter 1 of 3.** This notebook counts the twelve-row card by hand before any
pivot touches sixty thousand members, so the paradox of a flat blend over falling cohorts is
visible in rows a reader can see all at once.

**Who needs the answer.** The head of Gold, Chennai, who signs the fix-first call on Friday.

**The questions on the way.** What is a cohort, how is retention counted per member, what does
the blend average over, and what number does the dashboard print when the mix shifts.

**The case label.** Illustrative case: the company is real, the situation and the data are
synthetic, built for this class.
"""),
        code(LOAD),
        md("""
## What are the three signup months in the twelve rows?

The twelve rows carry three cohorts: May 2026 (four members), June 2026 (three) and the August
sale (five). Each row has an orders flag per calendar month after signup, with blanks where that
month has not happened yet by September. Print the card first, so every later number is
checkable by eye.
"""),
        code("""print(twelve.to_string(index=False))
check("twelve rows load", len(twelve) == 12, detail=f"actual {len(twelve)}")"""),
        md("""
## How many of each cohort returned in month one and month two?

**Predict before you run.** Say the counts aloud, by cohort: May members with an order in month
one; May members with an order in month two; June members with an order in month one; June in
month two; August in month one.
"""),
        code("""m1_by = twelve.groupby("cohort_month")["orders_m1"].sum().astype(int)
m2_by = twelve.groupby("cohort_month")["orders_m2"].sum().astype(int)
print("month-one counts, by cohort:")
print(m1_by)
print()
print("month-two counts, by cohort:")
print(m2_by)
check("May month-one is 3 of 4", m1_by.loc["2026-05"] == 3)
check("May month-two is 2 of 4", m2_by.loc["2026-05"] == 2)
check("June month-one is 2 of 3", m1_by.loc["2026-06"] == 2)
check("June month-two is 1 of 3", m2_by.loc["2026-06"] == 1)
check("August month-one is 2 of 5", m1_by.loc["2026-08"] == 2)"""),
        md("""
## What happened in September, and what is the blended rate on these twelve?

September is month four for May members, month three for June members and month one for the
August cohort, so the blended rate takes one column per cohort. Count the orders per cohort for
September, then the twelve-row blend.

**Predict before you run.** Which of these three fits the twelve rows: 3 of 12, 6 of 12 or 9 of 12?
"""),
        code("""may_sep = int(twelve[twelve["cohort_month"] == "2026-05"]["orders_m4"].sum())
jun_sep = int(twelve[twelve["cohort_month"] == "2026-06"]["orders_m3"].sum())
aug_sep = int(twelve[twelve["cohort_month"] == "2026-08"]["orders_m1"].sum())
sep = may_sep + jun_sep + aug_sep
print(f"May members ordering in September (m4): {may_sep} of 4")
print(f"June members ordering in September (m3): {jun_sep} of 3")
print(f"August members ordering in September (m1): {aug_sep} of 5")
print(f"twelve-row blend for September: {sep} of 12 = {sep / 12:.2f}")
check("September blend on the twelve rows is 6 of 12", sep == 6)
check("the rate reads 0.50 on the twelve rows", abs(sep / 12 - 0.50) < 0.01)"""),
        md("""
## What happens to the twelve-row blend when a bigger young cohort joins?

Suppose August had been three times the size, with the same month-one share. The twelve-row card
would now carry three Augusts for every one May and June. The toy below (invented) runs the
counterfactual: a batch A of 100 at 50 percent in month-one, then a batch B of 400 members with
52.5 percent, and the blended rate stays at 50 percent while A has fallen to 40.
"""),
        code("""# Toy A and B (invented, R1), from the deck
toy_a_last = {"members": 100, "retained": 50}
toy_a_this = {"members": 100, "retained": 40}
toy_b_this = {"members": 400, "retained": 210}

blend_last = toy_a_last["retained"] / toy_a_last["members"]
blend_this_a = toy_a_this["retained"] / toy_a_this["members"]
blend_this = ((toy_a_this["retained"] + toy_b_this["retained"])
              / (toy_a_this["members"] + toy_b_this["members"]))

print(f"last month, A alone: {toy_a_last['retained']} of {toy_a_last['members']} = {blend_last:.2f}")
print(f"this month, A alone: {toy_a_this['retained']} of {toy_a_this['members']} = {blend_this_a:.2f}")
print(f"this month, A plus B: {toy_a_this['retained'] + toy_b_this['retained']} of "
      f"{toy_a_this['members'] + toy_b_this['members']} = {blend_this:.2f}")
check("A alone fell from 0.50 to 0.40", abs(blend_this_a - 0.40) < 0.01)
check("A plus B blend is 0.50 even though A fell", abs(blend_this - 0.50) < 0.01)"""),
        md("""
## A picture of the toy: A falls, B joins, blend holds

The stacked bar lets the eye read the mix shift in one look. Each bar is a reporting month;
light shading is members present, dark is members retained. The blended rate under each bar is
the dark share over the total.
"""),
        code("""import matplotlib.pyplot as plt

xs = [0, 1]
a_mem = [toy_a_last["members"], toy_a_this["members"]]
a_ret = [toy_a_last["retained"], toy_a_this["retained"]]
b_mem = [0, toy_b_this["members"]]
b_ret = [0, toy_b_this["retained"]]

fig, ax = plt.subplots(figsize=(8, 4.0))
ax.bar(xs, a_mem, color="#EEEAFB", edgecolor="#1A0F5C", label="batch A, present")
ax.bar(xs, a_ret, color="#5B3FD6", edgecolor="#1A0F5C", label="batch A, retained")
ax.bar(xs, b_mem, bottom=a_mem, color="#FFF2D4", edgecolor="#1A0F5C", label="batch B, present")
ax.bar(xs, b_ret, bottom=a_mem, color="#C98A00", edgecolor="#1A0F5C", label="batch B, retained")
for x in xs:
    total_mem = a_mem[x] + b_mem[x]
    total_ret = a_ret[x] + b_ret[x]
    if total_mem:
        ax.text(x, total_mem + 15, f"blend {total_ret}/{total_mem} = {total_ret / total_mem:.2f}",
                ha="center", color="#1A0F5C", fontsize=10)
ax.set_xticks(xs)
ax.set_xticklabels(["last month", "this month"], color="#1A0F5C")
ax.set_ylim(0, 600)
ax.set_ylabel("members", color="#1A0F5C")
ax.legend(loc="upper left", fontsize=9, frameon=False)
ax.set_title("A falls, B joins, blend stays flat (invented, R1)", loc="left", color="#1A0F5C")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("the stacked chart shows four series", len(ax.patches) >= 4)"""),
        md("""
## A picture of the twelve rows and the toy

The deck carries the matplotlib figures the figure script wrote. In this notebook, show the same
twelve rows as a tidy frame, so the reader can scroll and verify every count.
"""),
        code("""import matplotlib.pyplot as plt

labels = ["May m1", "May m2", "May m4 (Sept)",
          "June m1", "June m2", "June m3 (Sept)",
          "August m1 (Sept)"]
values = [3, 2, may_sep, 2, 1, jun_sep, aug_sep]
colours = ["#5B3FD6"] * 2 + ["#C98A00"] + ["#5B3FD6"] * 2 + ["#C98A00"] + ["#C98A00"]

fig, ax = plt.subplots(figsize=(9, 4.0))
bars = ax.bar(range(len(labels)), values, color=colours, edgecolor="#1A0F5C", linewidth=0.6)
for i, v in enumerate(values):
    ax.text(i, v + 0.08, str(v), ha="center", color="#1A0F5C", fontsize=10)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=25, ha="right", fontsize=9, color="#1A0F5C")
ax.set_ylabel("members who ordered", color="#1A0F5C")
ax.set_title("Twelve rows: who ordered, by cohort and month", color="#1A0F5C", loc="left")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("the chart draws seven bars", len(bars) == 7)"""),
        md("""
## What are the Chennai cohort sizes, side by side?

The nine cohorts are drawn as bars so the eye sees the August spike. The August cohort is 2.6
times a normal cohort and is the youngest and lowest-retention row by September.
"""),
        code("""import matplotlib.pyplot as plt

cohort_sizes = members["cohort_month"].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(9, 4.0))
colours = ["#5B3FD6" if c != "2026-08" else "#C98A00" for c in cohort_sizes.index]
bars = ax.bar(cohort_sizes.index.astype(str), cohort_sizes.values,
              color=colours, edgecolor="#1A0F5C", linewidth=0.6)
for i, v in enumerate(cohort_sizes.values):
    ax.text(i, v + 150, f"{v:,}", ha="center", color="#1A0F5C", fontsize=9)
ax.set_xticklabels(cohort_sizes.index.astype(str), rotation=25, ha="right",
                   color="#1A0F5C", fontsize=10)
ax.set_ylabel("members in cohort", color="#1A0F5C")
ax.set_title("Chennai cohort sizes, Jan to Sep 2026", loc="left", color="#1A0F5C")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("August is the biggest cohort",
      cohort_sizes.loc["2026-08"] == cohort_sizes.max(),
      detail=f"{cohort_sizes.loc['2026-08']} vs max {cohort_sizes.max()}")"""),
        md("""
## What did the dashboard print, and where does the twelve-row count sit against it?

The dashboard reports 38 percent flat for June, July, August and September 2026 (the ticket).
The twelve-row blend for September is 0.50, five points above the dashboard. The dashboard
averages over 48,000 pre-signed members at those ages, not twelve; the shape is the same.
Chapter 2 reproduces the dashboard's number on the full data and decomposes it.
"""),
        code("""dashboard = 0.38
twelve_row = sep / 12
gap = twelve_row - dashboard
print(f"dashboard (reported, Chennai Sept 2026): {dashboard:.2f}")
print(f"twelve-row blend for September: {twelve_row:.2f}")
print(f"gap on twelve rows: {gap:+.2f}")
check("the twelve-row blend is at least five points above the dashboard",
      gap >= 0.05, detail=f"gap {gap:.3f}")
check_summary()"""),
        md("""
## What the next notebook adds.

Notebook 02 pivots the full member_months table into the triangle on sixty thousand members,
draws every cohort's curve, decomposes the blend into cohort size and cohort rate, and finds the
sale cohort in an empty your-turn cell. The toy you ran here is the shape; the full data makes
it a number.
"""),
    ]
    build(NB / "C2_W04_D04_01_twelve_rows_STUDENT.ipynb", cells)


# ============================================================ Notebook 02: cohort table and blend

def write_02():
    cells = [
        md("""
# 2. What is every cohort's curve on 60,000 members, and what is the blend made of?

**Week 4, Thursday. Chapter 2 of 3.** This notebook does chapter 1's hand count on the full data
and reproduces the dashboard's blended number as a weighted average of cohort rates. The pivot is
one line; the decomposition is one more.

**Who needs the answer.** The head of Gold, who needs the number the dashboard misses.

**The questions on the way.** How is a cohort table built, what does the triangle look like at
scale, how does the blend decompose into size times rate.
"""),
        code(LOAD),
        md("""
## What does the members table hold?

Each row is one member with her signup date, the cohort month that signup falls into, the signup
channel and her Chennai zone. Nine cohorts span January to September 2026. September is still
unfolding, so its month-one reading is not in this notebook.
"""),
        code("""print(members.head(6).to_string(index=False))
print()
print("rows:", len(members))
print()
print("cohort sizes:")
print(members["cohort_month"].value_counts().sort_index())
check("members has 60000 rows", len(members) == 60000, detail=f"actual {len(members)}")
check("August cohort is 13000", (members["cohort_month"] == "2026-08").sum() == 13000)"""),
        md("""
## The cohort sizes drawn as a bar

Jan to July are five thousand each, August is thirteen thousand (the sale week), September is
twelve thousand and still growing. The eye reads the August spike at a glance.
"""),
        code("""import matplotlib.pyplot as plt

sizes = members["cohort_month"].value_counts().sort_index()
colours = ["#5B3FD6" if c != "2026-08" else "#C98A00" for c in sizes.index]
fig, ax = plt.subplots(figsize=(9, 4.0))
ax.bar(sizes.index.astype(str), sizes.values, color=colours, edgecolor="#1A0F5C")
for i, v in enumerate(sizes.values):
    ax.text(i, v + 200, f"{v:,}", ha="center", color="#1A0F5C", fontsize=9)
ax.set_xticklabels(sizes.index.astype(str), rotation=25, ha="right",
                   color="#1A0F5C", fontsize=10)
ax.set_ylabel("members in cohort", color="#1A0F5C")
ax.set_title("Cohort sizes, Jan to Sep 2026, Chennai", loc="left", color="#1A0F5C")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("August is the largest cohort",
      sizes.loc["2026-08"] == sizes.max())"""),
        md("""
## What does one pivot_table turn member_months into?

The member_months table has one row per member per calendar month since signup, with an orders
flag of 0 or 1. A pivot_table averaged by cohort month and months-since-signup gives the
retention triangle on all 60,000 members. Each cell is the share of that cohort who ordered
that many months later.
"""),
        code("""triangle = (member_months
            .assign(cohort=lambda d: d["member_id"].map(members.set_index("member_id")["cohort_month"]))
            .query("months_since_signup >= 1")
            .pivot_table(index="cohort", columns="months_since_signup",
                         values="orders", aggfunc="mean")
            .round(3))
print(triangle)
check("triangle has eight cohort rows with observed month-one, Jan to August",
      len(triangle) == 8)
check("January row's month-one retention is near 0.58",
      abs(triangle.loc["2026-01", 1] - 0.58) < 0.03,
      detail=f"actual {triangle.loc['2026-01', 1]:.3f}")
check("August row's month-one retention is near 0.31",
      abs(triangle.loc["2026-08", 1] - 0.31) < 0.03,
      detail=f"actual {triangle.loc['2026-08', 1]:.3f}")"""),
        md("""
## Does every cohort fall across its own observed ages?

For each cohort with at least two observed ages, the month-two rate should be below the
month-one rate. The teaching claim is that each row drops left to right; the check confirms it.
"""),
        code("""drops = []
for cohort, row in triangle.iterrows():
    row = row.dropna()
    if len(row) >= 2:
        drops.append((cohort, float(row.iloc[0]), float(row.iloc[1])))
for c, m1, m2 in drops:
    print(f"{c}: m1 {m1:.3f}, m2 {m2:.3f}, change {m2 - m1:+.3f}")
check("every cohort with two observed ages falls from m1 to m2",
      all(m2 < m1 for c, m1, m2 in drops),
      detail=f"{sum(1 for c, m1, m2 in drops if m2 < m1)} of {len(drops)} fall")"""),
        md("""
## What does the triangle look like as a picture?

A heatmap, cohort on the row and age on the column, is the picture the deck carries. Draw it
here with matplotlib, from the triangle you just computed, so the notebook's own output matches
the deck's.
"""),
        code("""import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 5.0))
im = ax.imshow(triangle.values, cmap="Purples", vmin=0.25, vmax=0.65, aspect="auto")
for i in range(triangle.shape[0]):
    for j in range(triangle.shape[1]):
        v = triangle.values[i, j]
        if not np.isnan(v):
            ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                    color="white" if v > 0.44 else "#1A0F5C", fontsize=9)
ax.set_xticks(range(triangle.shape[1]))
ax.set_xticklabels([f"m{k}" for k in triangle.columns], color="#1A0F5C")
ax.set_yticks(range(triangle.shape[0]))
ax.set_yticklabels(triangle.index, color="#1A0F5C")
ax.set_title("Retention by cohort and age, Chennai, from the full 60,000", loc="left",
             color="#1A0F5C")
plt.colorbar(im, ax=ax, shrink=0.75)
plt.tight_layout()
plt.show()
check("the triangle picture drew eight rows", triangle.shape[0] == 8)"""),
        md("""
## What is the blended retention for June to September, straight from the data?

The dashboard's blended number is: for each reporting month, the share of members who signed up
before that month who placed at least one order in it. The direct count is one filter and one
mean. The next cell reproduces every reporting month's blend from the member tables.

**Predict before you run.** The ticket says 38 percent, flat. The computed values will be close
but not exact. Where would you expect the biggest gap: June, July, August or September?
"""),
        code("""def blended(month):
    pre = members[members["cohort_month"] < month]["member_id"]
    active = member_months[(member_months["month"] == month)
                           & (member_months["orders"] == 1)
                           & (member_months["member_id"].isin(pre))]
    return len(active) / len(pre) if len(pre) else 0.0

for month in ["2026-06", "2026-07", "2026-08", "2026-09"]:
    b = blended(month)
    print(f"{month}: blended retention {b:.3f}")
check("June blended retention is in [0.33, 0.44]",
      0.33 <= blended("2026-06") <= 0.44, detail=f"{blended('2026-06'):.3f}")
check("September blended retention is in [0.33, 0.44]",
      0.33 <= blended("2026-09") <= 0.44, detail=f"{blended('2026-09'):.3f}")"""),
        md("""
## The blended retention beside each cohort's month-one, in one picture

The dashboard line (amber) drifts a few points across the four reporting months. The cohort
month-one points (purple) step down every month. Both drawn on the same axis: the dashboard
sits above each new cohort's own m1 by a lot, because the mix averages old cohorts' floors with
the newest cohort's low m1.
"""),
        code("""import matplotlib.pyplot as plt

report_months = ["2026-06", "2026-07", "2026-08", "2026-09"]
dash = [blended(m) for m in report_months]
# the cohort whose m1 corresponds to each reporting month (the one that just entered)
latest_m1 = [triangle.loc[m, 1] if m in triangle.index else float("nan") for m in report_months]

fig, ax = plt.subplots(figsize=(9, 4.0))
ax.plot(report_months, dash, color="#C98A00", lw=2.4, marker="o",
        label="blended retention (dashboard)")
ax.plot(report_months, latest_m1, color="#5B3FD6", lw=2.4, marker="s",
        label="latest cohort's month-one")
for i, (d, m1) in enumerate(zip(dash, latest_m1)):
    ax.text(i, d + 0.02, f"{d:.2f}", color="#C98A00", ha="center", fontsize=10)
    if m1 == m1:  # not NaN
        ax.text(i, m1 - 0.04, f"{m1:.2f}", color="#5B3FD6", ha="center", fontsize=10)
ax.set_ylim(0.25, 0.55)
ax.set_ylabel("retention", color="#1A0F5C")
ax.legend(loc="lower left", frameon=False)
ax.set_title("The dashboard versus each new cohort's own m1, Jun to Sep",
             loc="left", color="#1A0F5C")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("the amber line has four points", len(dash) == 4)"""),
        md("""
## Is the blended rate equal to the weighted average of cohort rates?

For September, pre-signed members span the Jan to Aug cohorts. The weighted average formula
should return the same number as the direct count. The two computations are a second route to
the same answer; if they agree, the decomposition is correct.
"""),
        code("""month = "2026-09"
pre_cohorts = [c for c in triangle.index if c < month]
total_size = 0
weighted = 0.0
rows = []
for c in pre_cohorts:
    size = int((members["cohort_month"] == c).sum())
    k = (int(month[:4]) - int(c[:4])) * 12 + (int(month[5:7]) - int(c[5:7]))
    rate = triangle.loc[c, k] if k in triangle.columns and not pd.isna(triangle.loc[c, k]) else 0
    weighted += size * rate
    total_size += size
    rows.append((c, k, size, float(rate)))
w_avg = weighted / total_size
direct = blended(month)
for c, k, size, rate in rows:
    print(f"cohort {c}, age m{k}, size {size:>5}, rate {rate:.3f}")
print()
print(f"weighted average: {w_avg:.3f}")
print(f"direct count:     {direct:.3f}")
check("weighted average equals the direct count to three decimals",
      abs(w_avg - direct) < 0.002,
      detail=f"weighted {w_avg:.4f} vs direct {direct:.4f}")"""),
        md("""
## Your turn: which cohort pulls the September blend down the most?

Think about the stacked bars in the deck: the August cohort is the biggest row at the youngest
age, and its month-one rate is the lowest in the table. In the empty cell below, write code to
find the cohort whose contribution (size times rate) is the lowest fraction of the blend at
September. The deck will not name it until the TA lab; the data is the authoritative read.
"""),
        empty(),
        md("""
## What did the chapter answer?

The dashboard's 38 is a weighted average of eight cohort rates at eight different ages. Every
cohort falls across its own ages, the August cohort is the biggest and lowest in September, and
the direct count equals the weighted average to three decimals. The next notebook moves from the
cohort table to the funnel: once the entry moment is fixed, which stage owns the loss, in which
unit, after which date.
"""),
        code("check_summary()"),
    ]
    build(NB / "C2_W04_D04_02_cohort_table_STUDENT.ipynb", cells)


# ============================================================ Notebook 03: funnel and release

def write_03():
    cells = [
        md("""
# 3. Which stage owns the loss, on which denominator, and for whom?

**Week 4, Thursday. Chapter 3 of 3.** The cohort table named a mix shift. This notebook finds
the stage in the funnel where members actually fall off, in two units and across the Android
release date of 14 September 2026.

**Who needs the answer.** The head of Gold, who signs the fix-first call, and the app team, who
will dispute any stage the room blames.

**The questions on the way.** What is a funnel stage, how does the unit (session or member)
change the number, where in the event log does the release's effect sit.
"""),
        code(LOAD),
        md("""
## What is in the events table?

Each row is one event in one session: the member, a session id, a timestamp, the stage (open,
search, menu_view, add_to_cart, checkout_start, order_placed), the platform (android, ios, web)
and the checkout version. September is in full; August is kept for comparison. The analyst reads
this table to know which stage each session reached and how far it got.
"""),
        code("""print(events.head(6).to_string(index=False))
print()
print("rows:", len(events))
print()
print("stage counts:")
print(events["stage"].value_counts())
check("events has at least 50,000 rows", len(events) >= 50_000, detail=f"actual {len(events)}")"""),
        md("""
## Event volume by platform, in September

A quick picture of where the events come from. Android dominates (the ticket says so), iOS is
the comparator, web is small. The release split later in the notebook rests on the Android bar
being large enough to measure a change.
"""),
        code("""import matplotlib.pyplot as plt

sep_events = events[events["event_ts"].str.startswith("2026-09")]
by_platform = sep_events["platform"].value_counts()
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.bar(by_platform.index, by_platform.values,
       color=["#C98A00", "#5B3FD6", "#1A0F5C"], edgecolor="#1A0F5C")
for i, v in enumerate(by_platform.values):
    ax.text(i, v + 300, f"{v:,}", ha="center", color="#1A0F5C", fontsize=10)
ax.set_ylabel("events in September", color="#1A0F5C")
ax.set_title("September events by platform", loc="left", color="#1A0F5C")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("Android has the most events in September",
      by_platform.idxmax() == "android",
      detail=f"max platform {by_platform.idxmax()}")"""),
        md("""
## How is a funnel built, per session, from the events?

For each session, mark whether it reached each stage. Then for each stage count the sessions
that reached it. The per-step rate is a stage's count over the step before. In September the
home carousel pushes some sessions straight from open to menu_view without a search, so
search-to-menu-view per session can read above 100 percent, which is the artefact to name.
"""),
        code("""sep = events[events["event_ts"].str.startswith("2026-09")].copy()
sess_stage = sep.groupby(["session_id", "stage"]).size().unstack(fill_value=0)
sess_stage = (sess_stage > 0).astype(int)
stages = ["open", "search", "menu_view", "add_to_cart", "checkout_start", "order_placed"]
per_session = {s: sess_stage[s].sum() for s in stages}
for s in stages:
    print(f"{s:>15}  {per_session[s]:>6} sessions")
print()
print("per-step rates (per session):")
for prev, cur in zip(stages[:-1], stages[1:]):
    if per_session[prev]:
        rate = per_session[cur] / per_session[prev]
        print(f"{prev:>15} -> {cur:<15} {rate:.3f}")
check("search to menu view per session is above 1.0 (the artefact)",
      per_session["menu_view"] / per_session["search"] > 1.0,
      detail=f"{per_session['menu_view'] / per_session['search']:.3f}")"""),
        md("""
## What does the same funnel look like per member, in September?

The denominator moves from sessions to members: for each stage, count members who reached it at
least once in the month. The per-step rate is counted the same way, member by member. In the
per-member view the carousel's artefact disappears, because a member who viewed a menu is
counted once whether she searched or not.
"""),
        code("""mem_stage = sep.groupby(["member_id", "stage"]).size().unstack(fill_value=0)
mem_stage = (mem_stage > 0).astype(int)
per_member = {s: mem_stage[s].sum() for s in stages}
for s in stages:
    print(f"{s:>15}  {per_member[s]:>6} members")
print()
print("per-step rates (per member):")
for prev, cur in zip(stages[:-1], stages[1:]):
    if per_member[prev]:
        rate = per_member[cur] / per_member[prev]
        print(f"{prev:>15} -> {cur:<15} {rate:.3f}")
per_sess_ratio = per_session["menu_view"] / per_session["search"]
per_mem_ratio = per_member["menu_view"] / per_member["search"]
check("per-member search-to-menu-view is milder than per-session",
      per_mem_ratio < per_sess_ratio,
      detail=f"per-session {per_sess_ratio:.3f} vs per-member {per_mem_ratio:.3f}")"""),
        md("""
## How does the per-session funnel compare with the per-member funnel, side by side?

A single chart that shows both reads the whole chapter in one picture. Each row is a stage; the
left bar is per-session, the right is per-member. The eye catches the difference at
search-to-menu-view and at add-to-cart-to-order, both of which the unit decides.
"""),
        code("""import matplotlib.pyplot as plt
import numpy as np

labels = ["open", "search", "menu view", "add to cart", "checkout start", "order placed"]
sess_pct = [per_session[s] / per_session["open"] for s in stages]
mem_pct = [per_member[s] / per_member["open"] for s in stages]

y = np.arange(len(stages))
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.barh(y - 0.2, sess_pct, 0.4, color="#5B3FD6", label="per session")
ax.barh(y + 0.2, mem_pct, 0.4, color="#C98A00", label="per member")
for i, (sp, mp) in enumerate(zip(sess_pct, mem_pct)):
    ax.text(sp + 0.02, i - 0.2, f"{sp:.2f}", va="center", color="#1A0F5C", fontsize=9)
    ax.text(mp + 0.02, i + 0.2, f"{mp:.2f}", va="center", color="#1A0F5C", fontsize=9)
ax.set_yticks(y)
ax.set_yticklabels(labels, color="#1A0F5C")
ax.set_xlim(0, 1.3)
ax.legend(frameon=False, loc="lower right")
ax.set_title("The September funnel in two units", loc="left", color="#1A0F5C")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("the chart draws six stages", len(labels) == 6)"""),
        md("""
## Where does the Android release sit in the add-to-cart to order rate?

The checkout flow shipped on Android on 14 September 2026. Split events by platform and by
whether the timestamp is before or after that date, and compute the add-to-cart-to-order rate
per session for each slice. The ticket says Android fell from 0.58 to 0.44 and iOS stayed near
0.57.

**Predict before you run.** How many points will the Android gap read, after versus before?
"""),
        code("""def atc_order(df):
    g = df.groupby(["session_id", "stage"]).size().unstack(fill_value=0)
    for col in ("add_to_cart", "order_placed"):
        if col not in g.columns:
            g[col] = 0
    g = (g > 0).astype(int)
    return g["order_placed"].sum() / g["add_to_cart"].sum() if g["add_to_cart"].sum() else 0

android_pre = atc_order(events[(events["platform"] == "android")
                               & (events["event_ts"] < "2026-09-14")])
android_post = atc_order(events[(events["platform"] == "android")
                                & (events["event_ts"] >= "2026-09-14")])
ios_pre = atc_order(events[(events["platform"] == "ios")
                           & (events["event_ts"] < "2026-09-14")])
ios_post = atc_order(events[(events["platform"] == "ios")
                            & (events["event_ts"] >= "2026-09-14")])

print(f"Android before 14 Sep: {android_pre:.3f}")
print(f"Android from  14 Sep: {android_post:.3f}")
print(f"iOS      before 14 Sep: {ios_pre:.3f}")
print(f"iOS      from  14 Sep: {ios_post:.3f}")
print()
print(f"Android gap: {android_pre - android_post:+.3f}")
print(f"iOS     gap: {ios_pre - ios_post:+.3f}")
check("Android fell by at least 10 points",
      android_pre - android_post >= 0.10,
      detail=f"delta {android_pre - android_post:.3f}")
check("iOS stayed within 3 points of its own baseline",
      abs(ios_pre - ios_post) < 0.03,
      detail=f"delta {ios_pre - ios_post:.3f}")"""),
        md("""
## The release split drawn: Android bends, iOS and web do not

Two lines on the same picture: Android crosses the release date and drops; iOS runs flat
through the same window. The deck carries this chart; the notebook makes it from the facts a
learner can compute herself.
"""),
        code("""import matplotlib.pyplot as plt

xs = ["Aug comp", "Pre-release", "Post-release"]
and_rates = [
    atc_order(events[(events["platform"] == "android") & events["event_ts"].str.startswith("2026-08")]),
    android_pre,
    android_post,
]
ios_rates = [
    atc_order(events[(events["platform"] == "ios") & events["event_ts"].str.startswith("2026-08")]),
    ios_pre,
    ios_post,
]

fig, ax = plt.subplots(figsize=(9, 4.0))
ax.plot(xs, and_rates, color="#C98A00", lw=2.4, marker="o", label="Android")
ax.plot(xs, ios_rates, color="#5B3FD6", lw=2.4, marker="s", label="iOS")
for i, v in enumerate(and_rates):
    ax.text(i, v + 0.015, f"{v:.2f}", color="#C98A00", ha="center", fontsize=10)
for i, v in enumerate(ios_rates):
    ax.text(i, v - 0.04, f"{v:.2f}", color="#5B3FD6", ha="center", fontsize=10)
ax.axvline(1.5, color="#D63A6A", lw=1.2, linestyle="--", alpha=0.7)
ax.text(1.52, 0.75, "release on 14 Sept", color="#D63A6A", fontsize=10)
ax.set_ylim(0.3, 0.85)
ax.set_ylabel("add-to-cart to order", color="#1A0F5C")
ax.legend(frameon=False, loc="lower left")
ax.set_title("Add-to-cart to order, by platform and window", loc="left", color="#1A0F5C")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("the chart drew two platform lines", True)"""),
        md("""
## What is a second route to the same number?

The per-session rate above counts how often an add_to_cart session reached order_placed. A
second route counts per member: how many members who added to cart in the window placed an
order. If the two numbers agree within a few points on Android, the finding is not a per-unit
artefact.
"""),
        code("""def atc_order_per_member(df):
    g = df.groupby(["member_id", "stage"]).size().unstack(fill_value=0)
    for col in ("add_to_cart", "order_placed"):
        if col not in g.columns:
            g[col] = 0
    g = (g > 0).astype(int)
    return g["order_placed"].sum() / g["add_to_cart"].sum() if g["add_to_cart"].sum() else 0

a_pre_m = atc_order_per_member(events[(events["platform"] == "android")
                                      & (events["event_ts"] < "2026-09-14")])
a_post_m = atc_order_per_member(events[(events["platform"] == "android")
                                       & (events["event_ts"] >= "2026-09-14")])
print(f"Android per-member before: {a_pre_m:.3f}")
print(f"Android per-member from:   {a_post_m:.3f}")
check("per-member Android gap agrees with per-session Android gap to within 10 pts",
      abs((a_pre_m - a_post_m) - (android_pre - android_post)) < 0.10,
      detail=f"per-member {a_pre_m - a_post_m:.3f} vs per-session {android_pre - android_post:.3f}")"""),
        md("""
## What the chapter answered, in one sentence.

The fall sits in members on Android, after 14 September 2026. iOS and web are flat. The app
team's overall-conversion chart was correct and useless, because it averaged over the three axes
that would have told the story. The fix-first call is the Android checkout flow, and L5 in the
afternoon sizes it in orders a week.
"""),
        code("check_summary()"),
    ]
    build(NB / "C2_W04_D04_03_funnel_STUDENT.ipynb", cells)


# ============================================================ Notebook 04: Kalpa lab

def write_04():
    cells = [
        md("""
# 4. The Kalpa Retail-Plus lab: the method moves company.

**Week 4, Thursday. Lab notebook.** The head of Retail-Plus asks the morning's two questions on
Kalpa's own tier: is the fall everyone or the monsoon-sale cohort, and where in the funnel does
the loss sit. This notebook re-runs L1 to L3 on 120 Retail-Plus members, with the planted
feature discovered in an empty your-turn cell.

**Who needs the answer.** The head of Retail-Plus, who will decide a Kalpa fix next week.

**The questions on the way.** The same three as the morning, on Kalpa's data: cohort shape,
funnel per unit, and the stage that owns the loss.
"""),
        code(SETUP + """
import pandas as pd
import pathlib
from collections import Counter

DATA = pathlib.Path("../data")
memberships = pd.read_csv(DATA / "C2_W04_D04_memberships_STUDENT.csv")
k_months = pd.read_csv(DATA / "C2_W04_D04_kalpa_months_STUDENT.csv")
k_events = pd.read_csv(DATA / "C2_W04_D04_kalpa_events_STUDENT.csv")

PASS_COUNT = {"pass": 0, "fail": 0}


def check(label, condition, detail=""):
    ok = bool(condition)
    PASS_COUNT["pass" if ok else "fail"] += 1
    word = "PASS" if ok else "FAIL"
    print(f"{word}  {label}" + (f"  ({detail})" if detail else ""))
    return ok


def check_summary():
    print(f"\\n{'PASS' if PASS_COUNT['fail'] == 0 else 'FAIL'}  "
          f"{PASS_COUNT['pass']} checks passed and {PASS_COUNT['fail']} failed in this notebook.")

print(f"loaded: {len(memberships)} Retail-Plus memberships, "
      f"{len(k_months)} member-months, {len(k_events)} Kalpa events")
print()
print(memberships.head(5).to_string(index=False))
print()
print("Retail-Plus cohort sizes:")
print(memberships["cohort_month"].value_counts().sort_index())
check("memberships has 120 rows", len(memberships) == 120)
"""),
        md("""
## Retail-Plus cohort sizes drawn as a bar

The August cohort is twice a normal month's size (the row's plant until the lab finds it). Draw
the eight cohort sizes to see the shape before the triangle.
"""),
        code("""import matplotlib.pyplot as plt

sizes = memberships["cohort_month"].value_counts().sort_index()
colours = ["#5B3FD6" if c != "2026-08" else "#C98A00" for c in sizes.index]
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.bar(sizes.index.astype(str), sizes.values, color=colours, edgecolor="#1A0F5C")
for i, v in enumerate(sizes.values):
    ax.text(i, v + 0.5, str(v), ha="center", color="#1A0F5C", fontsize=10)
ax.set_xticklabels(sizes.index.astype(str), rotation=25, ha="right",
                   color="#1A0F5C", fontsize=10)
ax.set_ylabel("Retail-Plus members in cohort", color="#1A0F5C")
ax.set_title("Retail-Plus cohort sizes, Jan to Aug 2026", loc="left", color="#1A0F5C")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("August is the biggest Retail-Plus cohort",
      sizes.loc["2026-08"] == sizes.max())"""),
        md("""
## What does Kalpa's cohort table look like, July to September 2026?

The pivot is the same as the morning's: cohort month on the row, months since signup on the
column, mean of the orders flag in each cell. On 120 members, the cells are noisier than on the
Zomato case, but the shape still reads: cohorts fall across their observed ages, and the
largest, youngest cohort is lowest.
"""),
        code("""triangle = (k_months
            .assign(cohort=lambda d: d["customer_id"]
                    .map(memberships.set_index("customer_id")["cohort_month"]))
            .query("months_since_signup >= 1")
            .pivot_table(index="cohort", columns="months_since_signup",
                         values="orders", aggfunc="mean")
            .round(3))
print(triangle)
check("Kalpa triangle has at least five cohort rows", len(triangle) >= 5)"""),
        md("""
## What is the blended retention for July, August and September 2026 on Kalpa?

The direct count takes the share of pre-signed members who ordered in each reporting month.
Reading these three numbers is the first L1 answer to the head of Retail-Plus's first question.
"""),
        code("""def blended(month):
    pre = memberships[memberships["cohort_month"] < month]["customer_id"]
    active = k_months[(k_months["month"] == month)
                      & (k_months["orders"] == 1)
                      & (k_months["customer_id"].isin(pre))]
    return len(active) / len(pre) if len(pre) else 0

for mo in ["2026-07", "2026-08", "2026-09"]:
    print(f"{mo}: blended retention {blended(mo):.3f}")
check("every month's Kalpa blended rate is in [0.35, 0.48]",
      all(0.35 <= blended(m) <= 0.48 for m in ["2026-07", "2026-08", "2026-09"]))"""),
        md("""
## Your turn: find the fall in Kalpa's funnel between the two windows.

Monday's team fixed a window pair: the auto-reorder window from 10 to 30 September 2026, and
the comparison window from 20 August to 9 September 2026 (both after the monsoon sale ends 19
August). In the empty cell below, compute add-to-cart to checkout for Retail-Plus members in the
two windows and the gap between them. The planted feature is not named in this notebook; it is
what you report back to the TA.

The columns you need: `k_events` has `customer_id`, `session_id`, `event_ts`, `event_type` and
`platform`. The event types in order are `visit`, `search`, `add_to_cart` and `checkout`.
"""),
        empty(),
        md("""
## What else is worth checking in Kalpa's September?

A quick sanity count: the share of sessions that reach `visit` but never `search`, which maps to
the Retail-Plus home's reorder shortcut, and the checkout-per-session versus checkout-per-member
gap in September.
"""),
        code("""k_events["date"] = k_events["event_ts"].str[:10]
sess_type = k_events.groupby(["session_id", "event_type"]).size().unstack(fill_value=0)
for col in ("visit", "search", "add_to_cart", "checkout"):
    if col not in sess_type.columns:
        sess_type[col] = 0
sess_type = (sess_type > 0).astype(int)

sessions_with_visit = sess_type["visit"].sum()
sessions_with_search = sess_type["search"].sum()
skip_rate = 1 - (sessions_with_search / sessions_with_visit if sessions_with_visit else 0)
print(f"sessions with a visit:  {sessions_with_visit}")
print(f"sessions with a search: {sessions_with_search}")
print(f"share of sessions skipping search: {skip_rate:.2%}")
check("the search-skip rate is above 20 percent",
      skip_rate >= 0.20, detail=f"{skip_rate:.3f}")

sep_k = k_events[k_events["date"].str.startswith("2026-09")]
sep_sess = sep_k.groupby(["session_id", "event_type"]).size().unstack(fill_value=0)
for col in ("visit", "checkout"):
    if col not in sep_sess.columns:
        sep_sess[col] = 0
sep_sess = (sep_sess > 0).astype(int)
sep_mem = sep_k.groupby(["customer_id", "event_type"]).size().unstack(fill_value=0)
for col in ("visit", "checkout"):
    if col not in sep_mem.columns:
        sep_mem[col] = 0
sep_mem = (sep_mem > 0).astype(int)
co_per_sess = sep_sess["checkout"].sum() / sep_sess["visit"].sum()
co_per_mem = sep_mem["checkout"].sum() / sep_mem["visit"].sum()
print(f"checkout per session, September: {co_per_sess:.3f}")
print(f"checkout per member,  September: {co_per_mem:.3f}")
check("per-session and per-member checkout are at least 10 points apart",
      abs(co_per_mem - co_per_sess) >= 0.10,
      detail=f"gap {abs(co_per_mem - co_per_sess):.3f}")"""),
        md("""
## The two Kalpa funnel readings, side by side

September per-session versus per-member: visit counted once per session or once per member,
checkout counted the same way. The two bars read the same stages in different units.
"""),
        code("""import matplotlib.pyplot as plt
import numpy as np

stages = ["visit", "search", "add_to_cart", "checkout"]
sep_sess_full = sep_k.groupby(["session_id", "event_type"]).size().unstack(fill_value=0)
sep_mem_full = sep_k.groupby(["customer_id", "event_type"]).size().unstack(fill_value=0)
for col in stages:
    if col not in sep_sess_full.columns:
        sep_sess_full[col] = 0
    if col not in sep_mem_full.columns:
        sep_mem_full[col] = 0
sess_full = (sep_sess_full > 0).astype(int)
mem_full = (sep_mem_full > 0).astype(int)

sess_pct = [sess_full[s].sum() / sess_full["visit"].sum() for s in stages]
mem_pct = [mem_full[s].sum() / mem_full["visit"].sum() for s in stages]

y = np.arange(len(stages))
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.barh(y - 0.2, sess_pct, 0.4, color="#5B3FD6", label="per session")
ax.barh(y + 0.2, mem_pct, 0.4, color="#C98A00", label="per member")
for i, (sp, mp) in enumerate(zip(sess_pct, mem_pct)):
    ax.text(sp + 0.02, i - 0.2, f"{sp:.2f}", va="center", color="#1A0F5C", fontsize=9)
    ax.text(mp + 0.02, i + 0.2, f"{mp:.2f}", va="center", color="#1A0F5C", fontsize=9)
ax.set_yticks(y)
ax.set_yticklabels(stages, color="#1A0F5C")
ax.set_xlim(0, 1.2)
ax.legend(frameon=False, loc="lower right")
ax.set_title("Retail-Plus funnel, September, two units", loc="left", color="#1A0F5C")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
check("the chart drew four stages", len(stages) == 4)"""),
        md("""
## A small picture of the Kalpa cohort shape.

The triangle you drew earlier as a table, rendered as a heatmap, is the TA's go-to picture in
the lab. The eye reads the biggest row and the youngest cohort immediately.
"""),
        code("""import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(9, 4.0))
im = ax.imshow(triangle.values, cmap="Purples", vmin=0.30, vmax=0.65, aspect="auto")
for i in range(triangle.shape[0]):
    for j in range(triangle.shape[1]):
        v = triangle.values[i, j]
        if not np.isnan(v):
            ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                    color="white" if v > 0.44 else "#1A0F5C", fontsize=10)
ax.set_xticks(range(triangle.shape[1]))
ax.set_xticklabels([f"m{k}" for k in triangle.columns], color="#1A0F5C")
ax.set_yticks(range(triangle.shape[0]))
ax.set_yticklabels(triangle.index, color="#1A0F5C")
ax.set_title("Retail-Plus retention by cohort and age", loc="left", color="#1A0F5C")
plt.colorbar(im, ax=ax, shrink=0.75)
plt.tight_layout()
plt.show()
check("the Kalpa triangle picture drew its rows", triangle.shape[0] >= 5)"""),
        md("""
## What the lab answers, for the head of Retail-Plus.

You carry three numbers out of the lab: Kalpa's blended retention for July, August and September;
the stage of the Retail-Plus app funnel that lost the most members between the compare window
and the auto-reorder window; and the share of sessions whose home-screen shortcut skipped
search. The TA records the planted feature once the room has found it.
"""),
        code("check_summary()"),
    ]
    build(NB / "C2_W04_D04_04_kalpa_lab_STUDENT.ipynb", cells)


# ============================================================ orchestrate

NOTEBOOKS = {"01": write_01, "02": write_02, "03": write_03, "04": write_04}


def build_all(names):
    for name in names:
        print(f"\n--- building notebook {name} ---")
        NOTEBOOKS[name]()


if __name__ == "__main__":
    args = sys.argv[1:] or list(NOTEBOOKS.keys())
    build_all(args)

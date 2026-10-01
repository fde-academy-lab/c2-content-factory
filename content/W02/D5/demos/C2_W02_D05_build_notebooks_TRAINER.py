"""Build and execute Friday's notebooks: six chapters, the escalated case and the second case.

Run from the repository root, with the Kalpa warehouse loaded (bash .devcontainer/load_warehouse.sh):
    python3 content/W02/D5/demos/C2_W02_D05_build_notebooks_TRAINER.py            every notebook
    python3 content/W02/D5/demos/C2_W02_D05_build_notebooks_TRAINER.py c1 c4       named ones only

Each chapter notebook pairs with the deck section of the same number and question, and each starts
from what the one before it found. Every chapter runs the need, the options with their sizing, the
build with each step predicted, the trap, a second route and Kavya's review, and every heading is a
question the section answers. Each is executed cold in its own folder by scripts/nb_make.py. The case
notebooks are written twice: the TODO twin in notebooks/, which stops at its first placeholder on
purpose, and the executed solution twin in exercises/solutions/.

No learner file names the member the customer table is missing, prints the table's grand total to
the rupee or prints its gap to the warehouse. The tie that finds it is an empty your-turn cell in
chapter 3, the lookup trap runs on C-0195 (a Retail-Plus member with no orders in the two quarters),
and the one check that needs a failing source tie runs on five invented records labelled invented.
"""
import pathlib
import sys

sys.path.insert(0, "scripts")
from nb_make import SETUP, build, code, empty, md  # noqa: E402

DAY = pathlib.Path("content/W02/D5")
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"

CHAPTERS = ["Which segment carries it?", "Where did Q2 fall?", "Find any member by id?",
            "Read right in two minutes?", "What must Excel never do?", "Can a director break it?"]

ASK = '''> **The client asks.** "Monday's growth review deck needs three things I can open on my laptop
> without a login: the revenue tree by segment for both quarters, the top-fifty protect list with a
> lookup so I can find any member by id, and one number on the front page with its trend. Nothing
> that needs Python. If a director changes an assumption in the room, the sheet must recalculate in
> front of them."
>
> Meera's chief of staff, Kalpa Retail'''

HELPERS = '''
import csv
import pandas as pd

DATA = kit.data_dir()
SEGMENTS = ["Business", "Retail-Core", "Retail-Plus", "Student"]


def crore(n):
    return f"Rs {n / 1e7:.2f} crore"


def lakh(n):
    return f"Rs {n / 1e5:.2f} lakh"


def money(n):
    """Rupees the way Kalpa's finance team reads them: crore, lakh, or rupees in full."""
    sign, a = ("-" if n < 0 else ""), abs(n)
    return sign + (crore(a) if a >= 1e7 else lakh(a) if a >= 1e5 else kit.rupees(round(a)))


def change(before, after):
    """The change from before to after, measured on before, in percent."""
    return (after - before) / before * 100
'''

LOAD_TABLE = '''
table = pd.read_csv(DATA / "C2_W02_D05_customer_table_STUDENT.csv")
'''

LOAD_RAW = '''
raw = pd.read_csv(DATA / "C2_W02_D05_raw_export_STUDENT.csv", keep_default_na=False)
raw["quarter"] = raw["order_date"].str[5:7].astype(int).map(lambda m: "Q1" if m <= 6 else "Q2")
'''

WAREHOUSE = '''

def warehouse(query):
    """Ask the Kalpa warehouse itself, the source of truth every sheet ties back to."""
    return [{k: (int(v) if hasattr(v, "as_integer_ratio") and not isinstance(v, float) else v)
             for k, v in row.items()} for row in kit.sql(query)]
'''

COUNT_ONCE = '''
raw["first_row"] = (raw.groupby("order_id").cumcount() == 0).astype(int)   # =IF(COUNTIF($A$2:A2,A2)=1,1,0)
orders = raw[raw["first_row"] == 1]                                      # one row per order
'''


def setup(*parts, last=""):
    return code(SETUP + "".join(parts) + ("\n" + last if last else ""))


def mapcell(n, steps, lit=None):
    ladder = ", ".join(repr(c) for c in CHAPTERS)
    flow = ", ".join(repr(s) for s in steps)
    lit_arg = "" if lit is None else f", lit={lit}"
    return code(f'''
kit.side_by_side(
    kit.ladder([{ladder}], lit={n - 1}, show=False),
    kit.vflow([{flow}]{lit_arg}, show=False),
)''')


# ============================================================================= chapter 1
def ch1():
    return [
        md(f'''
# 1. Which segment carries Kalpa's revenue, and which leaf of the tree separates the segments?

**Week 2, Friday. Chapter 1 of 6.** Monday's growth review deck is built today, and this chapter
builds its second page: the revenue tree by segment, from the customer table the team exported on
Thursday.

{ASK}

**Who needs the answer.** Meera's chief of staff puts the tree by segment on page two of Monday's
deck, and the directors decide from it which segment the growth plan talks about. A leaf computed the
wrong way puts a tree on the page that does not multiply back to its own revenue, and the first
director who checks the arithmetic stops trusting every page after it.

**The questions on the way.**
1. Which way should a director get the tree: a PivotTable, a formula grid, pasted numbers or a live dashboard?
2. What does one row of the customer table stand for?
3. Which segment carries the revenue?
4. Which leaf separates Retail-Plus from Retail-Core?
5. What does a leaf averaged customer by customer say?
6. Can this table split Q1 from Q2, and does a second calculator agree with the pivot?

**The metric at stake.** Revenue here is booked order value in rupees: every order at the price
charged, whatever became of it, over April to September 2026. The revenue tree splits it into three
leaves that multiply back to it: customers, times orders per customer, times revenue per order.
Kalpa's segments are Retail-Core (everyday shoppers), Retail-Plus (the paid membership tier),
Business (corporate buyers invoiced in large amounts) and Student. The retail dossier,
`content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`, carries the tree and the segments
in more depth; nothing here needs it.

Monday's queries on the warehouse, the Postgres database that holds one row per order and that every
sheet ties back to, put Kalpa's revenue at Rs 10,00,00,000
in Q1 (April to June 2026) and Rs 9,84,00,000 in Q2 (July to September 2026). Thursday built one row
per customer in pandas and exported it as a CSV for Marketing. This chapter opens that export the
way a director's Excel does.

**Who else faces it.** Costco, the membership warehouse retailer, reports its sales by member tier.
Its 10-K for the year to 31 August 2025 counts 81.0 million paid members, 38.7 million of them on
the Executive tier, the paid upgrade, and says Executive members made up "approximately 73.6% of
worldwide net sales in 2025" (Costco Form 10-K, fiscal 2025, sec.gov, checked 30 September 2026).
That is the question Kalpa asks of Retail-Plus: how much of the revenue does the paid tier carry, and
through which leaf.
'''),
        md('''
**Setup.** The cell finds the shared helper `kit`, loads the customer table from `../data/` exactly as
Excel opens it, and defines `money()`, which prints rupees in crore, lakh or in full with Indian digit
grouping. Nothing is computed yet.
'''),
        setup(HELPERS, LOAD_TABLE, last='print(len(table), "rows and", len(table.columns), "columns:", ", ".join(table.columns))'),
        mapcell(1, ["the options\nfour ways to hand over a tree", "1. what one row stands for",
                    "2. which segment carries revenue", "3. which leaf separates the tiers",
                    "4. the trap\na leaf averaged per customer", "5. can it split the quarters",
                    "a second route\nthe same cells another way"]),
        md('''
## Which ways could the team hand a director the tree, and what does each cost on this table?

The chief of staff wants the tree by segment on a laptop with no login, and wants a director to be
able to slice it in the room. Four ways a team could hand it over:

| Option | What the director gets | What it assumes |
|---|---|---|
| a) A PivotTable on the table | A grid a director can re-slice by any column in seconds | The table is right, and someone presses Refresh when it changes |
| b) A SUMIFS and COUNTIFS grid | One formula per cell, each visible and each recalculating at once | The grid holds every slice anyone will ask for |
| c) Values pasted from pandas | The numbers, typed in as values | Nobody asks a new question in the room |
| d) A live dashboard on the warehouse | The warehouse's own numbers | Every director has a login, which the brief rules out |
'''),
        code('''
rows, cols = len(table), len(table.columns)
grid = 4 * 3                     # four segments, three measures: customers, orders, revenue
city_split = 6 * 4 * 3           # the same grid again for each of the six cities
sizing = [
    ("a) PivotTable", "1 pivot and 8 leaf formulas", "any of the 6 columns, in seconds", "on Refresh"),
    ("b) SUMIFS grid", f"{grid} formulas reading {grid * rows:,} cells", f"only what was built; a city split adds {city_split}", "at once"),
    ("c) pasted values", "0 formulas", "none", "never"),
    ("d) live dashboard", "a query per view", "anything", "at once, with a login"),
]
kit.table(["option", "what it takes on this table", "what a director can slice", "recalculates"], sizing,
          caption=f"Each option sized on this table: {rows} rows, {cols} columns")
kit.bars([("a) PivotTable", 8), ("b) SUMIFS grid", grid), ("b) with a city split", grid + city_split),
          ("c) pasted values", 0)], lit=(0,),
         title="Formulas each option needs for the tree by segment, and for a city split as well")
'''),
        md('''
**The best-fit call: a, the PivotTable, with each leaf computed beside it from the pivot's sums.** The
first thing a director does in the room is re-slice (by city, by segment), and only the pivot answers
a question nobody built in advance. Its leaves sit beside it as two ratios of its own sums, so they
move when it moves. **The fact that would change it:** a director who changes an assumption rather
than a slice. A PivotTable recalculates only when someone presses Refresh, while a SUMIFS grid
recalculates at once, so the numbers a director's input feeds go in formulas. Chapter 6 builds those.
'''),
        md('''
## 1. What does one row of the customer table stand for?

A Sum in a pivot adds one value per row, so what a row stands for decides what the pivot counts. Say
the grain, what one row stands for, before any pivot.

**Predict before you run.** One row of this table is: a) one order; b) one customer; c) one payment;
d) one customer in one quarter.
'''),
        code('''
ids = table["customer_id"].nunique()
kit.stats([(f"{len(table):,}", "rows", "in the CSV"),
           (f"{ids:,}", "distinct customer ids", "one per row if the grain is a customer"),
           ("6", "columns", "id, segment, city, orders, revenue, last order date")])
kit.table(list(table.columns), table.head(4).values.tolist(), caption="The first four rows, as Excel shows them")
kit.check("one row per customer: rows equal distinct ids", len(table) == ids, f"{len(table)} rows, {ids} ids")
'''),
        md('''
**What happened.** The answer is b. Three hundred rows carry three hundred distinct ids, so one row is
one customer who ordered in the two quarters, with that customer's orders and revenue summed across
April to September. A Sum over this table adds each customer once, which is what the tree needs.
'''),
        md('''
## 2. Which segment carries the revenue?

In Excel: select the table, **Insert, PivotTable**, drag `segment` to Rows, `customer_id` to Values
(Excel counts text, so it shows Count of customer_id), and `orders` and `revenue` to Values (Excel sums
numbers by default). The cell below builds the same grid.

**Predict before you run.** Which segment carries most of the revenue? a) Retail-Core, the most
customers; b) Retail-Plus, the paid tier; c) Business, the corporate buyers; d) no segment carries
more than a third.
'''),
        code('''
pivot = (table.groupby("segment")
         .agg(customers=("customer_id", "count"), orders=("orders", "sum"), revenue=("revenue", "sum"))
         .reindex(SEGMENTS))
pivot["share"] = pivot["revenue"] / pivot["revenue"].sum() * 100
kit.table(["Segment", "Customers", "Orders", "Revenue", "Share of revenue"],
          [(s, int(r.customers), int(r.orders), kit.rupees(r.revenue), f"{r.share:.1f}%")
           for s, r in pivot.iterrows()],
          caption="The customer table as a pivot by segment, April to September together")
kit.bars([(s, int(r.revenue)) for s, r in pivot.iterrows()], fmt=money, lit=(0,),
         title="Revenue by segment: the Business bar is the page")
'''),
        code('''
kit.check("the four segments count every customer once", int(pivot["customers"].sum()) == len(table),
          f"{int(pivot['customers'].sum())} customers")
kit.check("the four segments add back to the table's own revenue", int(pivot["revenue"].sum()) == int(table["revenue"].sum()))
kit.check("Business carries more than 95 percent of the revenue", pivot.loc["Business", "share"] > 95,
          f"{pivot.loc['Business', 'share']:.1f} percent")
'''),
        md('''
**What happened.** The answer is c. Business, 39 corporate buyers with 188 orders, carries
Rs 19,65,99,040, 99.1 percent of the half-year's revenue. The three consumer segments together carry
under 1 percent, so any number the page shows for the whole company is a Business number, and a
consumer segment can fall by a third without moving it. The front page in chapter 4 has to live with
that.
'''),
        md('''
## 3. Which leaf separates Retail-Plus from Retail-Core?

A member of Retail-Plus spends more than a Retail-Core shopper across the half-year. The tree says
why: more orders each, a bigger basket each time, or both. Each leaf is a ratio of the pivot's own
sums: orders per customer is orders over customers, and revenue per order is revenue over orders. In
Excel they are two formulas beside the pivot, or a calculated field.

**Predict before you run.** Which leaf explains most of the gap in revenue per customer? a) customers;
b) orders per customer; c) revenue per order; d) the two tiers spend the same per customer.
'''),
        code('''
tree = pivot.assign(orders_per_customer=pivot["orders"] / pivot["customers"],
                    revenue_per_order=pivot["revenue"] / pivot["orders"],
                    revenue_per_customer=pivot["revenue"] / pivot["customers"])
kit.table(["Segment", "Customers", "Orders per customer", "Revenue per order", "Revenue per customer"],
          [(s, int(r.customers), f"{r.orders_per_customer:.2f}", kit.rupees(round(r.revenue_per_order)),
            kit.rupees(round(r.revenue_per_customer))) for s, r in tree.iterrows()],
          caption="The leaves per segment, each a ratio of the pivot's sums")
core, plus = tree.loc["Retail-Core"], tree.loc["Retail-Plus"]
kit.columns(["orders per customer", "revenue per order", "revenue per customer"],
            [("Retail-Core = 100", [100, 100, 100]),
             ("Retail-Plus", [round(plus.orders_per_customer / core.orders_per_customer * 100),
                              round(plus.revenue_per_order / core.revenue_per_order * 100),
                              round(plus.revenue_per_customer / core.revenue_per_customer * 100)])],
            title="Retail-Plus against Retail-Core, with Core set at 100")
'''),
        code('''
kit.driver_tree({"label": "Retail-Plus revenue", "note": kit.rupees(plus.revenue), "kind": "lit", "children": [
    {"label": "customers", "note": f"{int(plus.customers)}"},
    {"label": "orders per customer", "note": f"{plus.orders_per_customer:.2f}"},
    {"label": "revenue per order", "note": kit.rupees(round(plus.revenue_per_order)), "kind": "known"}]},
    title="The tree for Retail-Plus: three leaves that multiply to its revenue")
for s, r in tree.iterrows():
    rebuilt = r.customers * r.orders_per_customer * r.revenue_per_order
    kit.check(f"{s}: the leaves multiply back to the revenue", abs(rebuilt - r.revenue) < 1)
'''),
        md('''
**What happened.** The answer is c. A Retail-Plus member spends Rs 9,221 across the half-year against
Retail-Core's Rs 5,644, 63 percent more. Orders per customer explain a little of it (3.29 against
2.99, 10 percent more); revenue per order explains most (Rs 2,801 against Rs 1,886, 48.5 percent
more). The paid tier's members fill bigger baskets. Every leaf multiplies back to its segment's
revenue, which is the check each tree on the page has to pass.
'''),
        md('''
## 4. What does a leaf averaged customer by customer say?

**The plausible wrong answer.** A hurried analyst wants revenue per order in the pivot itself. They
add a column to the table, `=revenue/orders`, one value per customer, and drag it into Values. Excel
sums numbers by default, so the first attempt reads as nonsense and is switched to Average, which
looks right.

**Predict before you run.** For Business, the Average of the per-customer column reads: a) exactly
the tree's Rs 10,45,740; b) a little below it; c) about 12 percent above it; d) about twice it.
'''),
        code('''
table["revenue_per_order"] = table["revenue"] / table["orders"]          # the helper column, per customer
by_seg = table.groupby("segment")["revenue_per_order"].agg(["sum", "mean"]).reindex(SEGMENTS)
kit.table(["Segment", "Sum of the column (the default)", "Average of the column", "The tree's leaf"],
          [(s, kit.rupees(round(r["sum"])), kit.rupees(round(r["mean"])), kit.rupees(round(tree.loc[s, "revenue_per_order"])))
           for s, r in by_seg.iterrows()],
          caption="Revenue per order three ways; only the last is revenue divided by orders")
avg_b, true_b = by_seg.loc["Business", "mean"], tree.loc["Business", "revenue_per_order"]
b_orders, b_rev = int(tree.loc["Business", "orders"]), int(tree.loc["Business", "revenue"])
kit.stats([(kit.rupees(round(avg_b)), "Business, averaged per customer", "what the hurried pivot shows"),
           (kit.rupees(round(true_b)), "Business, revenue over orders", "the tree's leaf"),
           (f"{change(true_b, avg_b):+.1f}%", "the averaged leaf's error", "on every Business order")])
'''),
        md('''
**What happened.** The answer is c: Rs 11,66,786, 11.6 percent above revenue over orders,
Rs 10,45,740.

**Why it is wrong.** The average gives every customer one vote, whatever they bought. Business
customers differ twentyfold in basket size, from Rs 3.34 lakh to Rs 66.98 lakh an order, and a
customer with two huge orders counts as much as a customer with eleven ordinary ones. Revenue per
order is the page's claim about orders, so each order should weigh the same, and only revenue
divided by orders does that. **The check that catches it** is the multiply-back from the question on
which leaf separates the tiers: with the averaged leaf, Business no longer multiplies back to its own
revenue.
'''),
        code('''
rebuilt_avg = b_orders * avg_b
kit.strip(table.loc[table["segment"] == "Business", "revenue_per_order"].round().tolist(),
          markers=[("averaged per customer", round(avg_b), "bad"), ("revenue over orders", round(true_b), "good")],
          fmt=money, title="Revenue per order for each of the 39 Business customers, and the two leaves")
kit.bridge(("Business revenue in the table", b_rev),
           [("what the averaged leaf adds", round(rebuilt_avg) - b_rev)],
           end_label="Business rebuilt with the averaged leaf", fmt=money, lit=(0,),
           title="The averaged leaf rebuilds Business at Rs 2.28 crore more than it sold")
kit.check("the averaged leaf fails the multiply-back by more than a crore", rebuilt_avg - b_rev > 1e7,
          f"{kit.rupees(round(rebuilt_avg))} against {kit.rupees(b_rev)}")
'''),
        md('''
**The fix.** Revenue per order is the pivot's Sum of revenue divided by its Sum of orders, as a
formula beside the pivot or as a calculated field. Microsoft's page on PivotTable calculations says
"Formulas for calculated fields operate on the sum of the underlying data for any fields in the
formula" (Microsoft Support, Calculate values in a PivotTable, checked 30 September 2026), which is
exactly the ratio of sums. **What changed:** Business revenue per order falls from Rs 11,66,786 to
Rs 10,45,740, and the tree multiplies back to Rs 19,65,99,040 to the rupee. The consumer segments
barely move (Retail-Core Rs 1,884 against Rs 1,886, Retail-Plus Rs 2,810 against Rs 2,801), because
their members' baskets are alike; the averaged leaf is wrong everywhere and badly wrong where
customers differ most in size.
'''),
        md('''
## 5. Can this table split Q1 from Q2?

The chief of staff asked for the tree **for both quarters**. The table's revenue is summed across
April to September, and its only date is `last_order_date`.

**Predict before you run.** How does this table give Q1 against Q2? a) split each customer's revenue
on the quarter of their last order; b) halve each customer's revenue; c) it cannot, since a quarter
split needs one row per order; d) the orders column counts per quarter.
'''),
        code('''
last_q = table["last_order_date"].str[5:7].astype(int).map(lambda m: "Q1" if m <= 6 else "Q2")
split = table.groupby(last_q)["revenue"].sum()
kit.columns(["Q1", "Q2"], [("revenue split on the last order date", [int(split["Q1"]), int(split["Q2"])]),
                          ("the warehouse's quarters (Monday)", [100_000_000, 98_400_000])],
            fmt=money, title="Splitting on the last order date against the quarters Monday's warehouse gave")
kit.check("the table carries no column that says which quarter an order fell in",
          not {"quarter", "order_date"} & set(table.columns))
kit.check("a split on the last order date puts most of the half-year in Q2", split["Q2"] > 5 * split["Q1"],
          f"{money(split['Q2'])} in Q2 against {money(split['Q1'])} in Q1")
'''),
        md('''
**What happened.** The answer is c. `last_order_date` is a recency: it says when a customer last
bought. Split on it, and a customer who bought every month from April and once more in September moves
the whole half-year into Q2, so Q2 reads Rs 17.88 crore against Monday's Rs 9.84 crore. The quarter
split needs one row per order, and only the raw export carries order dates. That is chapter 2.
'''),
        md('''
## A second route: does a plain count of the CSV reach every number the pivot shows?

A second route has to be able to fail when the first is wrong, so it cannot reuse the pivot. This one
reads the CSV as text, line by line, with Python's `csv` module and a running total per segment,
the accumulator from Week 1 Monday. In Excel the same second route is a COUNTIF and two SUMIFS per
segment beside the pivot.
'''),
        code('''
counts = {s: {"customers": 0, "orders": 0, "revenue": 0} for s in SEGMENTS}
with open(DATA / "C2_W02_D05_customer_table_STUDENT.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        c = counts[row["segment"]]
        c["customers"] += 1
        c["orders"] += int(row["orders"])
        c["revenue"] += int(row["revenue"])
kit.table(["Segment", "Customers", "Orders", "Revenue"],
          [(s, c["customers"], c["orders"], kit.rupees(c["revenue"])) for s, c in counts.items()],
          caption="The same grid, counted from the CSV's text without pandas")
agree = all(counts[s][k] == int(pivot.loc[s, k]) for s in SEGMENTS for k in ("customers", "orders", "revenue"))
kit.check("every cell of the pivot matches the plain count", agree, "12 cells compared")
'''),
        md('''
> **Kavya's review.** "Say what one row is before you pivot, and make every leaf a ratio of the pivot's
> own sums, then multiply the tree back before it goes on a page. A director who multiplies 39 by 4.82
> by Rs 11.67 lakh gets more than Business sold, and after that nobody reads page three."
'''),
        md('''
### In the interview: why does a leaf fail to multiply back, and why hand a director a pivot?

**[D] A leaf of your tree does not multiply back to the revenue. What happened, and what do you fix?**
The leaf was averaged over the rows instead of divided over the totals. An average of per-customer
ratios gives each customer one vote, so a few customers with huge single orders pull it up; here
Business read Rs 11,66,786 an order where revenue over orders is Rs 10,45,740, and the tree came back
Rs 2.28 crore over. I recompute the leaf as the sum of revenue divided by the sum of orders and keep
the multiply-back as the check on every tree I publish.

**[S] SQL, pandas or Excel for a tree a director will slice in the room?** Excel, as a PivotTable on a
table that has already been reconciled upstream, because slicing live is the one thing a director
asks for that neither a query nor a notebook gives them without a login. The numbers themselves come
from the warehouse or pandas; the pivot only presents them.

**[F] Why is a pivot's total only as honest as the table under it?** A pivot adds one value per row,
so the table's grain decides what it counts, and it never checks the table against anything. That is
why the first thing I say before pivoting is what one row stands for, and the last thing I do is tie
the grand total to a number someone upstream owns.
'''),
        md('''
### Depth: why is the average of ratios furthest out where customers differ most in size?

Revenue over orders is an average of each customer's revenue per order, weighted by that customer's
orders: a customer with eleven orders counts eleven times. The plain Average weights every customer
once. The two agree only when every customer has the same number of orders, or when how often a
customer orders has nothing to do with how big the basket is. Retail-Core members order anywhere from
once to fourteen times, at baskets between Rs 820 and Rs 3,000, and the number of orders tells you
nothing about the basket (a correlation of 0.01), so the two leaves differ by Rs 2. Business accounts
order between once and eleven times at baskets twentyfold apart, and the accounts with fewer orders
lean towards larger baskets (a correlation of -0.18; the two largest belong to accounts with two and
four orders), so the unweighted average runs 11.6 percent high.

**A spreadsheet that divided by the wrong total.** In January 2013 JPMorgan Chase's own task force
reported on the 2012 losses in its Chief Investment Office. In the spreadsheet behind a new risk
model, "after subtracting the old rate from the new rate, the spreadsheet divided by their sum
instead of their average, as the modeler had intended", which "likely had the effect of muting
volatility by a factor of two and of lowering the VaR" (Report of JPMorgan Chase & Co. Management
Task Force Regarding 2012 CIO Losses, 16 January 2013, page 128, read from the Yale Program on
Financial Stability archive, checked 30 September 2026). The bank divided by the wrong total, and the
averaged leaf weights its customers wrongly; both are ratios that nobody checked against their parts,
the bank's at a far larger scale.
'''),
        md('''
## Which segment carries the revenue, and which leaf separates the tiers, question by question?

1. The PivotTable, with each leaf computed beside it from its sums, because a director re-slices in the room; formulas take over where a director's input must recalculate at once.
2. One row of the customer table is one customer who ordered in the two quarters: 300 rows, 300 ids.
3. Business carries 99.1 percent of the half-year's revenue: 39 customers, Rs 19,65,99,040.
4. Revenue per order separates the tiers: Retail-Plus Rs 2,801 against Retail-Core's Rs 1,886, where orders per customer differ by 10 percent.
5. A leaf averaged per customer reads Business at Rs 11,66,786 an order, 11.6 percent high, and the tree multiplies back Rs 2.28 crore over; revenue over orders fixes it.
6. The table cannot split the quarters, since a split on the last order date puts Rs 17.88 crore in Q2; a plain count of the CSV matches all 12 cells of the pivot.

The next question is chapter 2's: the chief of staff wants both quarters, so the tree has to come from
the export that carries order dates.
'''),
        code("kit.check_summary()"),
    ]


# ============================================================================= chapter 2
def ch2():
    return [
        md(f'''
# 2. How much did revenue fall from Q1 to Q2, and in which segment and which leaf?

**Week 2, Friday. Chapter 2 of 6.** Chapter 1 built the tree by segment for the half-year from the
customer table: Business carries 99.1 percent of the revenue, and Retail-Plus's basket, Rs 2,801 an
order against Retail-Core's Rs 1,886, separates the two consumer tiers. That table has no quarter, and
a split on each customer's last order date put Rs 17.88 crore in Q2, so this chapter opens the other
export the data team sent: the raw one, which carries each order's date.

{ASK}

**Who needs the answer.** The chief of staff needs the tree for both quarters on page two; Meera
decides from it which branch of the tree the growth plan funds. A pivot that counts some orders twice
puts nearly twice Finance's revenue in front of the directors and can call a falling segment healthy,
which sends the plan after the wrong segment.

**The questions on the way.**
1. Which way should the team split revenue by quarter, and what does each way cost?
2. What does the pivot say for Q1 and Q2?
3. Why does it read nearly double, and does Remove Duplicates fix it?
4. What does the tree say when each order counts once?
5. Which segment and which leaf fell?
6. Does the warehouse reach the same quarters by its own route?

**The metric at stake.** Revenue by quarter, booked order value in rupees: Q1 is April to June 2026 and
Q2 is July to September 2026, Kalpa's own quarters. Monday's warehouse queries put them at
Rs 10,00,00,000 and Rs 9,84,00,000, and every number on the deck has to tie to those.

**Who else faces it.** Every business that takes money through a payment gateway holds orders and
payments at different grains. Razorpay, the Indian payment gateway, says its orders feature
"Combines multiple payment attempts for a single order", and on part payments that "each partial
payment would have a unique payment_id, but will be tied to the same order_id" (Razorpay
documentation, Orders and Payment Links partial payments, checked 30 September 2026). An export of
payments therefore repeats its orders, and every merchant's finance team meets the question this
chapter answers.
'''),
        md('''
**Setup.** The cell loads the raw export from `../data/` as text, adds Kalpa's quarter from each order
date (April to June is Q1), and defines `warehouse()`, which asks the Kalpa warehouse a question in
SQL and returns its rows. The warehouse is the Postgres database this Codespace loaded when it was
created; Monday and Tuesday queried it.
'''),
        setup(HELPERS, LOAD_RAW, WAREHOUSE,
              last='print(f"{len(raw):,} rows and {len(raw.columns) - 1} columns:", ", ".join(c for c in raw.columns if c != "quarter"))'),
        mapcell(2, ["the options\nfour ways to split by quarter", "1. which quarter each row is in",
                    "2. the trap\nthe pivot on the raw export", "3. why it doubles\nand Remove Duplicates",
                    "4. each order counted once", "5. which segment and leaf fell",
                    "a second route\nthe warehouse's own quarters"]),
        md('''
## Which way should the team split revenue by quarter, and what does each way cost?

| Option | How it splits | What it assumes |
|---|---|---|
| a) Split the customer table on the last order date | A customer's revenue goes to the quarter of their last order | Nobody bought in both quarters |
| b) A SUMIFS grid over the raw export, one formula per segment and quarter | Each formula adds the rows between a quarter's first and last date | The grid holds every slice anyone will ask for |
| c) Add Kalpa's quarter as a column, then pivot the raw export | April to June is Q1, July to September is Q2 | A director will want to re-slice it |
| d) Ask the data platform lead for the tree from the warehouse | The warehouse's own quarter column | The answer arrives before Monday, and again for every change a director asks for |
'''),
        code('''
first_rows = raw.drop_duplicates("order_id")
bought = first_rows.groupby("customer_id")["quarter"].agg(set)
both = sum(1 for s in bought if s == {"Q1", "Q2"})
moved = int(first_rows[first_rows["customer_id"].isin(bought[bought.map(len) == 2].index)
                       & (first_rows["quarter"] == "Q1")]["order_amount"].sum())
sizing = [
    ("a) last order date", "300 customer rows", f"{both} customers bought in both quarters; their Q1 revenue, {money(moved)}, lands in Q2"),
    ("b) SUMIFS grid", f"8 formulas, each reading {len(raw):,} rows on 3 conditions ({8 * len(raw) * 3:,} tests)", "recalculates at once; slices only the 8 cells built"),
    ("c) quarter column and pivot", f"{len(raw):,} formulas once, then 1 pivot", "slices any column; recalculates on Refresh"),
    ("d) ask the warehouse", "the warehouse's orders", "exact, and a day's wait for every question a director asks"),
]
kit.table(["option", "what it reads", "what it risks on this data"], sizing, caption="The four options sized on this export")
kit.bars([("a) Q1 revenue moved to Q2", moved), ("Q1 as Finance books it", 100_000_000)], fmt=money,
         title="Option a would move most of Q1 into Q2 before anything else went wrong")
'''),
        md('''
**The best-fit call: c, a column with Kalpa's own quarter, then the pivot.** It reads the order dates
the export carries, labels the quarters the way Finance does, and lets a director re-slice by
channel or city in the room, which b's eight fixed cells cannot. Option a moves Rs 8.04 crore of Q1
into Q2 before anything else goes wrong, and d is exact and too slow for a meeting. **The fact that
would change it:** a deadline far enough away for the warehouse team to answer, which makes d exact
and repeatable. Chapter 5 comes back to who owns which number.
'''),
        md('''
## 1. Which quarter does each row of the export belong to?

In Excel the column is one formula filled down: `=IF(MONTH(E2)<=6,"Q1","Q2")`, where column E holds
`order_date`. The setup cell already added it here.

**Predict before you run.** Of the 1,450 rows, how many fall in Q1? a) about half; b) about a
quarter; c) all of them; d) none, the dates are text.
'''),
        code('''
per_q = raw["quarter"].value_counts().reindex(["Q1", "Q2"])
kit.columns(["Q1", "Q2"], [("rows in the export", per_q.tolist())], title="Rows per quarter in the raw export")
kit.check("every row has a quarter", raw["quarter"].isin(["Q1", "Q2"]).all(), f"{per_q['Q1']} in Q1, {per_q['Q2']} in Q2")
'''),
        md('''
**What happened.** The answer is a: 772 rows fall in Q1 and 678 in Q2. The dates read cleanly, and the
quarter column now matches Finance's labels, so the pivot is one drag away.
'''),
        md('''
## 2. What does the pivot say for Q1 and Q2?

Build the chapter 1 pivot again on this export: `segment` in Rows, `quarter` in Columns, `order_amount`
in Values as Sum.

**Predict before you run.** The pivot's Q2 total reads about: a) Rs 9.84 crore, like the warehouse;
b) Rs 4.9 crore; c) Rs 19.5 crore; d) Rs 98 crore.
'''),
        code('''
hurried = raw.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum").reindex(SEGMENTS)
rows = [(s, kit.rupees(r.Q1), kit.rupees(r.Q2), f"{change(r.Q1, r.Q2):+.1f}%") for s, r in hurried.iterrows()]
rows.append(("All segments", kit.rupees(hurried.Q1.sum()), kit.rupees(hurried.Q2.sum()),
             f"{change(hurried.Q1.sum(), hurried.Q2.sum()):+.1f}%"))
kit.table(["Segment", "Q1", "Q2", "Change"], rows, caption="The pivot on the raw export: Sum of order_amount")
kit.stats([(crore(hurried.Q1.sum()), "Q1, as the pivot shows it", "the warehouse: Rs 10.00 crore"),
           (crore(hurried.Q2.sum()), "Q2, as the pivot shows it", "the warehouse: Rs 9.84 crore"),
           (f"{change(hurried.loc['Retail-Core', 'Q1'], hurried.loc['Retail-Core', 'Q2']):+.1f}%",
            "Retail-Core, Q1 to Q2", "the pivot calls it growing")])
'''),
        md('''
**What happened: the plausible wrong answer.** The answer is c. The pivot reads Rs 19,94,36,150 for
Q1 and Rs 19,46,59,340 for Q2, Rs 39,40,95,490 in all, and says Retail-Core grew 1.0 percent. Nothing
is red and every row is a real row of the export. The deck would carry Rs 19.47 crore for Q2, nearly
twice Finance's Rs 9.84 crore, and call Retail-Core the healthy segment the growth plan can leave
alone.
'''),
        md('''
## 3. Why does it read nearly double, and does Remove Duplicates fix it?

**Why it is wrong.** A Sum adds one value per row, and the question is what one row of this export
stands for. **The check that catches it** takes a minute: count the rows against the distinct order
ids, then tie the grand total to the warehouse.

**Predict before you run.** After Excel's **Data, Remove Duplicates** with every column ticked, the
grand total reads: a) Rs 19.84 crore, the warehouse; b) still about Rs 39.4 crore; c) about half the
warehouse; d) nothing, because the tool refuses repeated ids.
'''),
        code('''
rows_per_order = raw.groupby("order_id").size()
kit.stats([(f"{len(raw):,}", "rows", "in the export"),
           (f"{raw['order_id'].nunique():,}", "distinct order ids", "what the warehouse holds"),
           (f"{len(raw) / raw['order_id'].nunique():.2f}", "rows per order", "above 1.00 inflates a Sum")])
kit.columns(["one row", "two rows"], [("orders", [int((rows_per_order == 1).sum()), int((rows_per_order == 2).sum())])],
            title="How many rows each order takes in the export")
deduped = raw.drop(columns="quarter").drop_duplicates()
kit.table(["Version of the export", "Rows", "Grand total"],
          [("As exported", f"{len(raw):,}", kit.rupees(raw["order_amount"].sum())),
           ("After Remove Duplicates, every column", f"{len(deduped):,}", kit.rupees(deduped["order_amount"].sum())),
           ("The warehouse, Monday", "1,000 orders", kit.rupees(100_000_000 + 98_400_000))],
          caption="What Remove Duplicates changes")
kit.check("the export repeats orders: more rows than order ids", len(raw) > raw["order_id"].nunique(),
          f"{len(raw):,} rows, {raw['order_id'].nunique():,} ids")
kit.check("Remove Duplicates leaves the total nearly double the warehouse",
          deduped["order_amount"].sum() > 1.9 * 198_400_000, money(deduped["order_amount"].sum()))
'''),
        md('''
**What happened.** The answer is b. The export has one row per **payment**, with the order's amount
repeated on each: 550 orders sit on one row and 450 on two. Remove Duplicates removes only rows that
are identical in every column, and 50 orders' two rows are identical, a payment the gateway posted
twice. The other 400 orders were paid in two instalments, so their two rows differ in `paid_amount`
and both stay. The total barely moves, from Rs 39,40,95,490 to Rs 39,40,57,740 on 1,400 rows, and the
analyst now believes the export is clean.
'''),
        md('''
## 4. What does the tree say when each order counts once?

The fix names the grain: flag the first row of each order and add only flagged rows. In Excel the flag
is `=IF(COUNTIF($A$2:A2,A2)=1,1,0)` filled down column A's order ids, with the pivot or a SUMIFS reading
only rows where the flag is 1. The code below builds the same flag: a running count per order that
is 1 on the order's first row.

**Predict before you run.** Counted once per order, what is the Q2 total? a) Rs 9.84 crore; b) Rs 9.74
crore; c) Rs 19.47 crore; d) Rs 4.92 crore.
'''),
        code(COUNT_ONCE + '''
once = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum").reindex(SEGMENTS)
rows = [(s, kit.rupees(r.Q1), kit.rupees(r.Q2), f"{change(r.Q1, r.Q2):+.1f}%") for s, r in once.iterrows()]
rows.append(("All segments", kit.rupees(once.Q1.sum()), kit.rupees(once.Q2.sum()), f"{change(once.Q1.sum(), once.Q2.sum()):+.1f}%"))
kit.table(["Segment", "Q1", "Q2", "Change"], rows, caption="The same pivot, each order counted once")
kit.bridge(("Pivot on the rows", int(raw["order_amount"].sum())),
           [("second rows of 400 instalment orders", -int(raw[(raw["first_row"] == 0) & (raw["paid_amount"] != raw["order_amount"])]["order_amount"].sum())),
            ("second rows of 50 gateway copies", -int(raw[(raw["first_row"] == 0) & (raw["paid_amount"] == raw["order_amount"])]["order_amount"].sum()))],
           end_label="Each order once", fmt=money, lit=(0,),
           title="From the pivot's Rs 39.41 crore to one row per order")
kit.check("each order is flagged exactly once", int(raw["first_row"].sum()) == raw["order_id"].nunique(), f"{int(raw['first_row'].sum()):,} flags")
kit.check("Retail-Core falls once each order counts once", once.loc["Retail-Core", "Q2"] < once.loc["Retail-Core", "Q1"],
          f"{change(once.loc['Retail-Core', 'Q1'], once.loc['Retail-Core', 'Q2']):+.1f}%")'''),
        md('''
**What happened.** The answer is a. Counted once per order, Q1 is Rs 10,00,00,000 and Q2 is
Rs 9,84,00,000, down 1.6 percent. **What changed:** the grand total falls by Rs 19,56,95,490 to the
warehouse's figure, and Retail-Core turns from a 1.0 percent rise into a 1.8 percent fall, Rs 3,73,070
to Rs 3,66,250. Most of the excess was instalment orders, which are the largest invoices; the 50
gateway copies are small consumer orders worth Rs 37,750.
'''),
        md('''
## 5. Which segment and which leaf fell?

The company fell Rs 16,00,000, 1.6 percent. Two readings answer "where": the rupees each segment lost,
and the share of its own revenue each segment lost. The bridge below takes the rupees; the tree per
segment and quarter takes the leaves, using chapter 1's: customers who ordered, orders per customer
and revenue per order.

**Predict before you run.** Which Retail-Plus leaf moved most from Q1 to Q2? a) customers; b) orders
per customer; c) revenue per order; d) all three by about the same amount.
'''),
        code('''
seg_q = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum").reindex(SEGMENTS)
kit.bridge(("Q1, all segments", int(seg_q["Q1"].sum())),
           [(s, int(seg_q.loc[s, "Q2"] - seg_q.loc[s, "Q1"])) for s in SEGMENTS],
           end_label="Q2, all segments", fmt=money, lit=(0, 2), lo=97_000_000,
           title="Q1 to Q2 by segment, in rupees; the axis starts at Rs 9.70 crore so the moves show")
leaves = (orders.groupby(["segment", "quarter"])
          .agg(customers=("customer_id", "nunique"), orders=("order_id", "count"), revenue=("order_amount", "sum")))
leaves["orders_per_customer"] = leaves["orders"] / leaves["customers"]
leaves["revenue_per_order"] = leaves["revenue"] / leaves["orders"]
p1, p2 = leaves.loc[("Retail-Plus", "Q1")], leaves.loc[("Retail-Plus", "Q2")]
kit.table(["Retail-Plus", "Q1", "Q2", "Change"],
          [("Customers", int(p1.customers), int(p2.customers), f"{change(p1.customers, p2.customers):+.1f}%"),
           ("Orders per customer", f"{p1.orders_per_customer:.2f}", f"{p2.orders_per_customer:.2f}", f"{change(p1.orders_per_customer, p2.orders_per_customer):+.1f}%"),
           ("Revenue per order", kit.rupees(round(p1.revenue_per_order)), kit.rupees(round(p2.revenue_per_order)), f"{change(p1.revenue_per_order, p2.revenue_per_order):+.1f}%"),
           ("Revenue", kit.rupees(p1.revenue), kit.rupees(p2.revenue), f"{change(p1.revenue, p2.revenue):+.1f}%")],
          caption="The Retail-Plus tree, each order counted once")
kit.columns(SEGMENTS, [("Q1", [round(leaves.loc[(s, "Q1"), "orders_per_customer"], 2) for s in SEGMENTS]),
                       ("Q2", [round(leaves.loc[(s, "Q2"), "orders_per_customer"], 2) for s in SEGMENTS])],
            fmt=lambda v: f"{v:.2f}", lit=(2,), title="Orders per customer by segment: Retail-Plus is the one that fell")
rebuilt = p2.customers * p2.orders_per_customer * p2.revenue_per_order
kit.check("the Retail-Plus Q2 tree multiplies back", abs(rebuilt - p2.revenue) < 1, kit.rupees(round(rebuilt)))
'''),
        md('''
**What happened.** The answer is b. In rupees, Business carries most of the fall: Rs 14,29,840 of the
Rs 16,00,000, which is 1.4 percent of its own Q1, the size of a few corporate invoices landing in one
quarter or the next. The steepest fall is Retail-Plus, down 29.4 percent, from Rs 5,85,770 to
Rs 4,13,380. Its customers who ordered fell from 91 to 76 (16.5 percent), orders per customer fell from
2.36 to 1.84 (22.0 percent), and the basket grew from Rs 2,725 to Rs 2,953 (8.4 percent). Members kept
buying big baskets and bought less often, the frequency branch Week 1 found, now read from the export
the directors will see. Both readings are true, and chapter 4 decides how each goes on the front page.
'''),
        md('''
## A second route: does the warehouse reach the same quarters by its own query?

The export was written from the warehouse, and a second route must be able to disagree with it, so it
asks the warehouse's own orders table, which holds one row per order and never saw the export. The
query is Monday's.
'''),
        code('''
wq = warehouse("SELECT quarter, count(*) AS orders, sum(amount) AS revenue FROM orders GROUP BY quarter ORDER BY quarter")
kit.table(["Quarter", "Orders in the warehouse", "Revenue in the warehouse", "The export, once per order"],
          [(r["quarter"], r["orders"], kit.rupees(r["revenue"]), kit.rupees(int(once[r["quarter"]].sum()))) for r in wq])
kit.columns(["Q1", "Q2"], [("pivot on the rows", [int(hurried.Q1.sum()), int(hurried.Q2.sum())]),
                          ("each order once", [int(once.Q1.sum()), int(once.Q2.sum())]),
                          ("the warehouse", [r["revenue"] for r in wq])],
            fmt=money, title="Three readings of the quarters: only the pivot on the rows disagrees")
kit.check("the export counted once ties to the warehouse to the rupee, both quarters",
          all(int(once[r["quarter"]].sum()) == r["revenue"] for r in wq))
kit.check("the order counts tie too", all(int(orders[orders["quarter"] == r["quarter"]]["order_id"].nunique()) == r["orders"] for r in wq))
'''),
        md('''
> **Kavya's review.** "The two exports came at two grains. Say the grain before you pivot, count rows
> against ids, and tie the grand total to the warehouse before the pivot goes anywhere. Remove
> Duplicates is a cleaning step with no record, and here it did not even clean."
'''),
        md('''
### In the interview: where do you look first when a pivot disagrees with the warehouse?

**[F] Your pivot shows a different total from the warehouse. Where do you look first?** At the grain:
rows against distinct keys. A payment, item or event export repeats its parent's amount, and a Sum
adds every repeat. Here 1,450 rows held 1,000 orders and the pivot read Rs 39.41 crore against
Rs 19.84 crore. If the grain is right, I look at the period and the filters next, then at keys present
on one side and missing on the other.

**[S] Why does Remove Duplicates not fix an export at the payment grain?** It removes rows identical in
every column. Two instalments of one order differ in the amount paid, so both stay; only the 50 exact
gateway copies went, and the total moved from Rs 39,40,95,490 to Rs 39,40,57,740. The fix names the
grain: count each order once by its key.

**[D] The export grows a hundredfold. Which of today's formulas do you replace, and with what?** The
running COUNTIF flag. It compares each row with every row from the first down to its own, so 1,450 rows cost 1,051,975
comparisons and 145,000 rows cost about 10.5 billion, which freezes a laptop. I sort by order id and
flag a row whose id differs from the row above, one comparison a row, or I ask the warehouse for an
order-grain export and stop fixing the grain in a sheet at all.
'''),
        md('''
### Depth: what does a payment gateway's own data say about orders and payments?

**What an order with two payments looks like.** Razorpay's Orders API returns an `attempts` field,
"The number of payment attempts, successful and failed, that have been made against this order",
and an `amount_paid` beside the order's `amount` (Razorpay API reference, Create an order, checked 30
September 2026). A merchant's analyst who exports payments and pivots on the order amount meets
this chapter's trap; one who sums `amount_paid` per order answers a collections question instead,
which is chapter 5's.


'''),
        md('''
## How far did revenue fall, where, and does the warehouse agree, question by question?

1. A quarter column and the pivot, since a split on the last order date moves Rs 8.04 crore of Q1 into Q2; the column puts 772 rows in Q1 and 678 in Q2.
2. The pivot on the export's rows reads Rs 19,94,36,150 for Q1 and Rs 19,46,59,340 for Q2, and calls Retail-Core up 1.0 percent.
3. It doubles because one row is one payment: 1,450 rows for 1,000 orders; Remove Duplicates removes only the 50 identical gateway copies and leaves Rs 39,40,57,740.
4. Each order counted once: Q1 Rs 10,00,00,000, Q2 Rs 9,84,00,000, down 1.6 percent; Retail-Core is down 1.8 percent.
5. In rupees Business carries Rs 14.30 lakh of the Rs 16.00 lakh fall; the steepest fall is Retail-Plus, down 29.4 percent, because orders per customer fell from 2.36 to 1.84 while its basket grew 8.4 percent.
6. The warehouse's own query gives the same two quarters to the rupee.

The next question is chapter 3's: Retail-Plus members are ordering less often, so which of them does
the head of Retail-Plus protect first, and can the chief of staff look any of them up?
'''),
        code("kit.check_summary()"),
    ]


PROTECT = '''
plus = (table[table["segment"] == "Retail-Plus"]
        .sort_values(["revenue", "customer_id"], ascending=[False, True]).reset_index(drop=True))
plus["rank"] = plus.index + 1
protect = plus.head(50).copy()                       # the protect list, rank 1 to 50
'''


# ============================================================================= chapter 3
def ch3():
    return [
        md(f'''
# 3. Which fifty Retail-Plus members go on the protect list, and when the chief of staff types an id, does the sheet answer for that member?

**Week 2, Friday. Chapter 3 of 6.** Chapter 2 counted each order once and tied the raw export to the
warehouse to the rupee: revenue fell 1.6 percent, from Rs 10.00 crore to Rs 9.84 crore, and the
steepest fall was Retail-Plus, down 29.4 percent, because its members ordered less often, 2.36 orders
each in Q1 and 1.84 in Q2. The head of Retail-Plus wants to protect the members who matter most before
more of them drift, so this chapter builds the protect list and the lookup the chief of staff asked for.

{ASK}

**Who needs the answer.** The head of Retail-Plus sends the fifty members on the list a retention
offer, and the chief of staff reads a member's line aloud when a director names one. A lookup that
answers with the wrong member's row tells a director that someone who has stopped buying is one of the
best, and spends an offer on the wrong person.

**The questions on the way.**
1. Which lookup should answer "find this member"?
2. Who makes the list, and where does it stop?
3. Does the list's source table tie to the warehouse?
4. What does a lookup with its fourth argument left out return for an id the table does not hold?
5. What does an exact match with a not-found path return, and what if the list is re-sorted?
6. Does an independent count agree with the lookup?

**The metric at stake.** Each member's revenue across the two quarters, April to September 2026, and
the list's cut-off, the revenue of the fiftieth member. The head of Retail-Plus sizes the retention
budget on the fifty.

**Who else faces it.** Any team that ranks a list and then reads rows off it by name. In 2003 TransAlta,
the Canadian power company, lost 24 million US dollars on bids for electricity transmission contracts
in New York when "someone preparing the electronic file of bids ... misaligned the rows of information
in the spreadsheet". Its president, Steve Snyder, said: "It was literally a cut-and-paste error in an
Excel spreadsheet that we did not detect when we did our final sorting and ranking of bids prior to
submission" (The Globe and Mail, 4 June 2003, checked 30 September 2026). A row that answers for the
wrong item is expensive at any scale.
'''),
        md('''
**Setup.** The cell loads the customer table and the raw export from `../data/`, the same two CSVs
chapters 1 and 2 used, and defines `warehouse()`, which asks the Kalpa warehouse a question in SQL for
the second route. The protect list is built from the customer table, one row per customer, since that
is the table the chief of staff will refresh every Monday.
'''),
        setup(HELPERS, LOAD_TABLE, LOAD_RAW, WAREHOUSE, last='print(len(table), "customer rows and", f"{len(raw):,}", "export rows loaded")'),
        mapcell(3, ["the options\nfour lookups", "1. who makes the list", "2. your turn\ndoes its source tie",
                    "3. the trap\nthe fourth argument left out", "4. an exact match, found or not",
                    "5. the list re-sorted", "a second route\nan independent count"]),
        md('''
## Which lookup should answer "find this member", and what does each return?

The chief of staff types a member id into a cell and wants that member's revenue and rank back. Four
lookups a team could write, with the table's ids in column A and revenue in column E:

| Option | The formula | What it assumes |
|---|---|---|
| a) VLOOKUP as most people type it | `=VLOOKUP(id, A:F, 5)` | The id is always in the table |
| b) VLOOKUP, exact | `=VLOOKUP(id, A:F, 5, FALSE)` | A director reads #N/A as "not found" |
| c) INDEX and MATCH, exact, with a not-found path | `=IFERROR(INDEX(E:E, MATCH(id, A:A, 0)), "not in the table")` | Nothing beyond the id column |
| d) XLOOKUP with its fourth argument | `=XLOOKUP(id, A:A, E:E, "not in the table")` | The laptop runs Excel 2021, 2024 or Microsoft 365 |
'''),
        code('''
ids_sorted = sorted(table["customer_id"])
revenue_of = dict(zip(table["customer_id"], table["revenue"]))


def vlookup_approx(member):
    """VLOOKUP with the fourth argument left out: the largest id not above the one asked for."""
    below = [i for i in ids_sorted if i <= member]
    return (below[-1], revenue_of[below[-1]]) if below else ("#N/A", None)


present, absent = "C-0152", "C-0195"
sizing = [
    ("a) VLOOKUP as typed", f"{kit.rupees(vlookup_approx(present)[1])}", f"another member's row: {vlookup_approx(absent)[0]}", "wrong rows if the ids are not sorted", "yes"),
    ("b) VLOOKUP, exact", kit.rupees(revenue_of[present]), "#N/A", "right", "yes"),
    ("c) INDEX and MATCH", kit.rupees(revenue_of[present]), "not in the table", "right", "yes"),
    ("d) XLOOKUP", kit.rupees(revenue_of[present]), "not in the table", "right", "Excel 2021, 2024, 365 only"),
]
kit.table(["option", f"a present id, {present}", f"an absent id, {absent}", "table re-sorted by revenue", "opens in Excel 2016"],
          sizing, caption="Each lookup tried on this table")
kit.matrix(["a) VLOOKUP as typed", "b) VLOOKUP exact", "c) INDEX and MATCH", "d) XLOOKUP"],
           ["present id", "absent id", "re-sorted list"],
           [["right", "a neighbour, silently", "unreliable"], ["right", "#N/A", "right"],
            ["right", "says not found", "right"], ["right", "says not found", "right"]],
           title="What each lookup does in the three situations a room creates")
'''),
        md('''
**The best-fit call: d on the room's Microsoft 365, c wherever the file must open.** Both answer for
the member asked for, say so when the id is missing, and survive a re-sorted list. Microsoft's page
says XLOOKUP "is not available in Excel 2016 and Excel 2019" (Microsoft Support, XLOOKUP function,
checked 30 September 2026), and LibreOffice 24.2 shows #NAME? for it, so a file that travels uses
INDEX and MATCH. **The fact that would change it:** the Excel version on the chief of staff's laptop.
Option b is honest and ugly: a director reads #N/A as a broken sheet.
'''),
        md('''
## 1. Who makes the list, and where does it stop?

Filter the table to Retail-Plus, sort by revenue from largest to smallest, keep fifty. In Excel: copy
the 106 Retail-Plus rows to their own sheet, **Sort Largest to Smallest** on `revenue`, and add a rank
column, `=RANK.EQ(E2, E$2:E$107)`.

**Predict before you run.** The fiftieth member's revenue, the list's cut-off, is about: a) Rs 25,000;
b) Rs 8,600; c) Rs 2,800; d) there is no cut-off, since ties decide the list.
'''),
        code(PROTECT + '''
cut, nxt = int(protect["revenue"].iloc[-1]), int(plus["revenue"].iloc[50])
kit.stats([(f"{len(plus)}", "Retail-Plus members", "in the customer table"),
           (kit.rupees(int(protect["revenue"].iloc[0])), "rank 1", protect["customer_id"].iloc[0]),
           (kit.rupees(cut), "rank 50, the cut-off", "the last member on the list"),
           (kit.rupees(int(protect["revenue"].sum())), "the fifty together", "April to September")])
kit.strip(plus["revenue"].tolist(), markers=[("the cut-off, rank 50", cut, "bad")], fmt=kit.rupees,
          title="Revenue of all 106 Retail-Plus members; the fifty to the right of the line make the list")
kit.table(["Rank", "City", "Revenue"],
          [(int(r["rank"]), r.city, kit.rupees(r.revenue)) for _, r in plus.iloc[47:52].iterrows()],
          caption="Either side of the boundary")
kit.check("the list holds exactly fifty members", len(protect) == 50)
kit.check("no tie sits across the boundary, so the list ships fifty", cut > nxt, f"{kit.rupees(cut)} against {kit.rupees(nxt)}")
'''),
        md('''
**What happened.** The answer is b. Fifty of the 106 Retail-Plus members make the list, from C-0152 at
Rs 25,840 down to the cut-off at Rs 8,580. The fifty-first member spent Rs 8,520, so no tie sits
across the boundary and the list ships exactly fifty rows; Wednesday's tie rule has nothing to decide
here. The fifty together spent Rs 7,14,890.
'''),
        md('''
## 2. Does the list's source table tie to the warehouse?

Chapter 2 tied the raw export to the warehouse to the rupee: Rs 10,00,00,000 in Q1 and Rs 9,84,00,000
in Q2, 1,000 orders. The protect list is built from the other export, the customer table, which has to
tie on its own before a list built on it ships.

**Your turn.** Type these lines into the empty cell below and run it:

```python
once = raw.drop_duplicates("order_id")
print("customer table:", int(table["orders"].sum()), "orders,", kit.rupees(int(table["revenue"].sum())))
print("raw export, each order once:", once["order_id"].nunique(), "orders,", kit.rupees(int(once["order_amount"].sum())))
print("ids in the export and not in the table:", sorted(set(once["customer_id"]) - set(table["customer_id"])))
```

Then write one sentence in your notes: what does your answer mean for the list, and for any lookup the
chief of staff runs on it?
'''),
        empty(),
        md('''
## 3. What does a lookup with its fourth argument left out return for an id the table does not hold?

C-0195 is a Retail-Plus member in Delhi who placed no orders in the two quarters, so the customer
table, one row per customer who ordered, has no row for C-0195. A hurried sheet types
`=VLOOKUP("C-0195", A2:F301, 5)` and leaves the fourth argument out.

**Predict before you run.** What comes back? a) #N/A; b) zero; c) the revenue of the member whose id
sits just before C-0195; d) the revenue of the top member on the list.
'''),
        code('''
got_id, got_rev = vlookup_approx("C-0195")
rank = plus.loc[plus["customer_id"] == got_id, "rank"]
kit.table(["Asked for", "Row returned", "Revenue returned", "What the sheet tells the room"],
          [("C-0195", got_id, kit.rupees(got_rev), f"on the protect list at rank {int(rank.iloc[0])}")],
          caption="VLOOKUP with the fourth argument left out, on the table sorted by id")
kit.flow(["C-0193\\nRs 1,580", f"{got_id}\\n{kit.rupees(got_rev)}", "C-0195\\nno row", "C-0196\\nRs 2,380"],
         kinds=["plain", "bad", "unknown", "plain"],
         title="An approximate match settles on the largest id not above the one asked for")
'''),
        md('''
**What happened: the plausible wrong answer.** The answer is c. The sheet returns C-0194's revenue,
Rs 16,740, a member at rank 15 on the protect list, and nothing on the screen is red. Microsoft's page
says of the fourth argument, `range_lookup`: "If you don't specify anything, the default value will
always be TRUE or approximate match" (Microsoft Support, VLOOKUP function, checked 30 September 2026),
and an approximate match finds "the largest value less than or equal to" the one asked for (Microsoft
Support, Look up values with VLOOKUP, INDEX, or MATCH, checked 30 September 2026).

**Why it is wrong.** The chief of staff tells a director that C-0195 is one of Kalpa's best members and
spent Rs 16,740, and a retention offer goes to someone who placed no order between April and September. Nobody asks why
the id was missing, because the sheet never said it was. **The check that catches it:** test every
lookup with an id you know is missing, and print the id returned beside the id asked for.
'''),
        code('''
kit.check("the check catches it: the row returned is not the id asked for", got_id != "C-0195",
          f"asked C-0195, got {got_id}")
kit.check("the neighbour's row sits inside the top fifty, so the answer looks plausible", int(rank.iloc[0]) <= 50,
          f"rank {int(rank.iloc[0])}")
'''),
        md('''
## 4. What does an exact match with a not-found path return, and what if the list is re-sorted?

The fix is an exact match that says so when an id is missing: `=XLOOKUP(id, A:A, E:E, "not in the
table")`, or `=IFERROR(INDEX(E:E, MATCH(id, A:A, 0)), "not in the table")` where the file must open in
older Excel or LibreOffice. The cell below writes the same rule as a function.

**Predict before you run.** For C-0195, C-0152 and C-0194, the exact lookup returns: a) three revenues;
b) not found, Rs 25,840 and Rs 16,740; c) three not-founds; d) Rs 16,740 three times.
'''),
        code('''
def find(member):
    """An exact match with a not-found path: that member's revenue, or a sentence saying it is missing."""
    hit = table.loc[table["customer_id"] == member, "revenue"]
    return int(hit.iloc[0]) if len(hit) else "not in the table"


asked = ["C-0195", "C-0152", "C-0194"]
kit.table(["Asked for", "Exact match with a not-found path", "Approximate match"],
          [(m, find(m) if isinstance(find(m), str) else kit.rupees(find(m)),
            f"{vlookup_approx(m)[0]}: {kit.rupees(vlookup_approx(m)[1])}") for m in asked],
          caption="The two lookups side by side")
kit.tree({"label": "an id typed in", "branches": [
    ("in the table", {"label": "that member's revenue", "kind": "good"}),
    ("not in the table", {"label": "the words: not in the table", "kind": "good"})]},
    taken=("not in the table",), title="An exact match has two exits, and C-0195 takes the second")
kit.check("the exact lookup says when an id is missing", isinstance(find("C-0195"), str))
kit.check("the exact lookup finds a member who is there", find("C-0152") == 25840)
'''),
        md('''
**What happened.** The answer is b. **What changed:** C-0195's line moves from "rank 15, Rs 16,740" to
"not in the table", which is the answer that makes somebody check the export. For members who are in
the table the two lookups agree, which is why a lookup tested only on present ids looks fine.

The room will see the list sorted by revenue, and an exact match gives the same answer in any order.
An approximate match assumes the ids are sorted: Microsoft's page says "If range_lookup
is TRUE or left out, the first column needs to be sorted alphabetically or numerically. If the first
column isn't sorted, the return value might be something you don't expect" (Microsoft Support, VLOOKUP
function, checked 30 September 2026). The cell below counts how far the list's ids are from sorted.
'''),
        code('''
along = protect["customer_id"].tolist()
steps_down = sum(1 for a, b in zip(along, along[1:]) if b < a)
reordered = protect.sample(frac=1, random_state=16).reset_index(drop=True)   # the director re-sorts the list
same = all(find(m) == revenue_of[m] for m in reordered["customer_id"])
kit.stats([(f"{steps_down}", "times the next id is smaller", "walking down the list sorted by revenue"),
           ("50 of 50", "exact lookups still right", "after the list is shuffled")])
kit.check("the list sorted by revenue is far from sorted by id", steps_down > 10, f"{steps_down} of 49 steps go down")
kit.check("an exact match returns the same answers in any order", same)
'''),
        md('''
## A second route: does the warehouse's own count agree with the lookup?

The lookup and the check must not share a method or a source, so the second route counts orders in
the warehouse, which never saw the customer table. In Excel, with no login, the same idea is
`=COUNTIF` of the id in the raw export's customer column, a different export from the list's. No
orders has to meet a not-found answer, and an order count has to meet the same revenue.
'''),
        code('''
def orders_in_warehouse(member):
    """The warehouse's own count and revenue for one id, from the orders table."""
    row = warehouse(f"SELECT count(*) AS n, coalesce(sum(amount), 0) AS revenue FROM orders WHERE customer_id = '{member}'")[0]
    return int(row["n"]), int(row["revenue"])


kit.table(["Id", "Orders in the warehouse", "Revenue in the warehouse", "The lookup"],
          [(m, *orders_in_warehouse(m)[:1], kit.rupees(orders_in_warehouse(m)[1]),
            find(m) if isinstance(find(m), str) else kit.rupees(find(m))) for m in ["C-0195", "C-0152"]])
kit.check("no orders in the warehouse meets a not-found answer",
          orders_in_warehouse("C-0195")[0] == 0 and isinstance(find("C-0195"), str))
kit.check("the warehouse's revenue meets the lookup's for a member who is there",
          orders_in_warehouse("C-0152")[1] == find("C-0152"))
'''),
        md('''
> **Kavya's review.** "A lookup that cannot find an id says so. A lookup that answers with somebody
> else's row is worse than no lookup, because nobody in the room can tell. Test with an id you know is
> missing, and tie the list's table before anyone reads from it."
'''),
        md('''
### In the interview: which argument returns a neighbour, and how do you test a lookup?

**[F] Your lookup returned a member for an id that does not exist. Which argument was wrong?** The
match type. VLOOKUP's fourth argument, left out, means an approximate match, which returns the
largest key not above the one asked for; here C-0195 came back as C-0194 at rank 15 of the protect
list. I use an exact match with a not-found path, XLOOKUP's fourth argument or IFERROR around INDEX and
MATCH, and I test every lookup with an id I know is missing.

**[S] What do you test a lookup with before a director uses it?** Three ids: one I know is present,
one I know is missing, and the first id on a re-sorted list. The present id proves the found path, the
missing id proves the not-found path, and the re-sort proves the lookup does not depend on order. When
the ids come from another system I add three more: one stored as text where the table holds numbers,
one with a trailing space, and one that appears twice, since each breaks an exact match in its own way.

**[D] XLOOKUP or INDEX and MATCH for a file that goes to the CEO's office?** XLOOKUP where every laptop
runs Excel 2021, 2024 or Microsoft 365, since it is exact by default and takes a not-found message.
INDEX and MATCH with IFERROR where the file might open in Excel 2016 or 2019 or in LibreOffice, which
do not have XLOOKUP. The answer turns on one fact about the office's software, and I ask for it.
'''),
        md('''
### Depth: where is an approximate match the right tool?

Approximate match exists for bands: a price list with quantity breaks, an income tax slab, a discount
tier by order value. There the table holds the lower edge of each band, sorted, and "the largest value
less than or equal to" the amount is exactly the band it falls in. An order of Rs 2,700 against
invented tiers starting at Rs 0, Rs 1,000 and Rs 2,500 falls in the Rs 2,500 tier. The same rule on
member ids, which are labels and not amounts, returns a neighbour, so the question before typing a
lookup is whether the key is a band edge or a name.
'''),
        md('''
## Who is on the protect list, and does the lookup answer for the member typed, question by question?

1. XLOOKUP with its fourth argument on Microsoft 365, and IFERROR around INDEX and MATCH where the file must open anywhere.
2. Fifty of 106 Retail-Plus members make the list, from Rs 25,840 down to a cut-off of Rs 8,580; the fifty-first spent Rs 8,520, so no tie crosses the boundary.
3. Whether the list's source ties is the room's own answer, from the your-turn cell, and it decides whether the list ships.
4. VLOOKUP with its fourth argument left out returned C-0194's Rs 16,740, rank 15, for C-0195, which has no row.
5. The exact match says "not in the table" for C-0195 and finds C-0152 at Rs 25,840; it gives the same answers on the re-sorted list.
6. COUNTIF finds zero rows for C-0195 and one for C-0152, agreeing with the lookup both times.

The next question is chapter 4's: the chief of staff's third ask is the one number on the front page.
'''),
        code("kit.check_summary()"),
    ]


CARD = '''
seg_q = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum").reindex(SEGMENTS)
SCOPES = {"All segments": SEGMENTS, "All except Business": ["Retail-Core", "Retail-Plus", "Student"],
          "Retail-Plus": ["Retail-Plus"]}


def card(scope):
    """The front-page card for a scope: the number, its period, its comparison and its base."""
    q1, q2 = int(seg_q.loc[SCOPES[scope], "Q1"].sum()), int(seg_q.loc[SCOPES[scope], "Q2"].sum())
    share = q2 / int(seg_q["Q2"].sum()) * 100
    words = "down" if q2 < q1 else "up"
    return {"scope": scope, "Q1": q1, "Q2": q2, "change": change(q1, q2), "share": share,
            "sentence": f"{scope}, Q2, July to September 2026: {money(q2)}, {words} {abs(change(q1, q2)):.1f} percent "
                        f"on Q1, April to June 2026 ({money(q1)}); {share:.1f} percent of company revenue in Q2."}
'''


# ============================================================================= chapter 4
def ch4():
    return [
        md(f'''
# 4. What must sit beside the front-page number so a director reads it right in two minutes?

**Week 2, Friday. Chapter 4 of 6.** Chapter 2 tied the quarters to the warehouse: Rs 10.00 crore in Q1
and Rs 9.84 crore in Q2, down 1.6 percent; in rupees Business carries Rs 14.30 lakh of the Rs 16.00
lakh fall, and the steepest fall is Retail-Plus, down 29.4 percent. Chapter 3 built the protect list,
fifty members from C-0152 at Rs 25,840 down to Rs 8,580, with a lookup that answers "not in the table"
for C-0195. The chief of staff's third ask is one number on the front page with its trend, and the number is
revenue, Q2 against Q1. Which metric belongs on a growth review's front page at all is a question for a
later week; this chapter is about making the one asked for impossible to misread.

{ASK}

**Who needs the answer.** Meera and the directors read the front page first and may read nothing else;
the chief of staff presents it and answers for it. A card without its period reads two quarters as one,
and a percentage without its base turns a Rs 1.72 lakh fall into a crisis the meeting spends its time
on.

**The questions on the way.**
1. Which form should the card take?
2. What does a director read in a card that says "Revenue Rs 19.84 crore"?
3. What does the card say with its period, comparison and base?
4. What does "Retail-Plus revenue down 29.4 percent" leave out?
5. What does the trend beside the number show, and what happens when a director changes the scope?
6. Does the warehouse reach the same change by its own route?

**The metric at stake.** Q2 revenue against Q1, booked order value in rupees, with Q1 April to June
2026 and Q2 July to September 2026.

**Who else faces it.** Every listed company writes this card each quarter. DMart's owner, Avenue
Supermarts, headlined its results for the quarter to 30 June 2025 as "Standalone Total Revenue up by
16.2% at Rs.15,932 Crore", and its release adds that revenue "stood at Rs.15,932 crore, as compared to
Rs.13,712 crore in the same period last year" (Avenue Supermarts press release, 11 July 2025, checked 30
September 2026). The number, its period, its comparison and its base are all in the first two lines.
'''),
        md('''
**Setup.** The cell loads the raw export, adds Kalpa's quarter, counts each order once the way chapter 2
did, and defines `card()`, which writes the front-page card for a scope. It also defines `warehouse()`
for the second route.
'''),
        setup(HELPERS, LOAD_RAW, WAREHOUSE, COUNT_ONCE, CARD,
              last='print(f"{len(orders):,} orders, each counted once, from {len(raw):,} export rows")'),
        mapcell(4, ["the options\nfour cards", "1. the trap\na number with no period", "2. the card, built",
                    "3. the trap\na percentage with no base", "4. the trend beside it",
                    "5. the scope a director changes", "a second route\nthe warehouse's change"]),
        md('''
## Which form should the front-page card take, and what does each ask the director to remember?

| Option | The card | What the director must bring to read it right |
|---|---|---|
| a) The total | "Revenue Rs 19.84 crore" | That it covers two quarters, and what the last figure was |
| b) The quarter | "Q2 revenue Rs 9.84 crore" | Q1's figure, from memory |
| c) The quarter against the last | "Q2, July to September 2026: Rs 9.84 crore, down 1.6 percent on Q1 (Rs 10.00 crore)" | Nothing |
| d) c, with its sentence and its trend | c, plus where the change sits and six months drawn as a line | Nothing, and it answers the next question too |
'''),
        code('''
SENTENCE = ("Business invoices carry Rs 14.30 lakh of the Rs 16.00 lakh fall; Retail-Plus, the paid tier, "
            "fell 29.4 percent because members ordered less often.")
cards = {"a) the total": "Revenue Rs 19.84 crore",
         "b) the quarter": "Q2 revenue Rs 9.84 crore",
         "c) against the last": card("All segments")["sentence"],
         "d) with sentence and trend": card("All segments")["sentence"] + " " + SENTENCE}
remember = ["two facts: the period, and the last figure", "one fact: Q1's figure", "nothing", "nothing"]
kit.table(["option", "words on the card", "what a director must bring"],
          [(k, len(v.split()), m) for (k, v), m in zip(cards.items(), remember)], caption="Four cards, counted")
kit.bars([(k, len(v.split())) for k, v in cards.items()], lit=(3,),
         title="Words on each card; d adds a line drawn beside it as well")
'''),
        md('''
**The best-fit call: d.** About fifty words and one small line chart, read in the two minutes a
director gives the front page, and nothing left to memory. **The fact that would change it:** a board that
reviews every month against the plan line, where the comparison on the card becomes the plan and not
the previous quarter.
'''),
        md('''
## 1. What does a director read in a card that says "Revenue Rs 19.84 crore"?

The fastest card is the export's grand total in big type. It is correct: Rs 19.84 crore is Kalpa's
revenue for April to September.

**Predict before you run.** A director who remembers Q1 at Rs 10.00 crore reads this card as: a) two
quarters of revenue; b) revenue nearly doubled this quarter; c) a number to check later; d) nothing
wrong, since the number is right.
'''),
        code('''
half_year = int(orders["order_amount"].sum())
read_as = change(100_000_000, half_year)
kit.stats([(crore(half_year), "the card", "April to September, two quarters"),
           (f"{read_as:+.1f}%", "what a director reads", "against Q1's remembered Rs 10.00 crore"),
           (crore(int(seg_q["Q2"].sum())), "Q2 alone", "the quarter the review is about")])
kit.columns(["Q1", "the card, read as Q2", "Q2"], [("revenue", [100_000_000, half_year, int(seg_q["Q2"].sum())])],
            fmt=money, lit=(1,), title="The card beside the quarters it is read against")
kit.check("the card's number is the two quarters added", half_year == int(seg_q["Q1"].sum() + seg_q["Q2"].sum()))
'''),
        md('''
**What happened: the plausible wrong answer.** The answer is b. Read against Q1's Rs 10.00 crore, a
bare Rs 19.84 crore looks like revenue up 98.4 percent in a quarter when it fell 1.6 percent. The number
is right and its period is missing, so the reader supplies one. **Why it is wrong:** a director carries
that growth into the meeting's decisions, and the minutes record a boom that never happened. **The check
that catches it:** read the card aloud and ask which months, and against what; a card that cannot
answer is not ready. **The fix:** the period and the comparison on the card itself.
'''),
        md('''
## 2. What does the card say with its period, comparison and base?

The card's change is measured on the earlier quarter: Q2 minus Q1, divided by Q1.

**Predict before you run.** The change on the card reads: a) down 1.6 percent; b) down 1.6 points; c) up
1.6 percent; d) down 16 percent.
'''),
        code('''
company = card("All segments")
print(company["sentence"])
kit.stats([(money(company["Q2"]), "Q2, July to September 2026", "the number"),
           (f"{company['change']:+.1f}%", "on Q1", "the comparison"),
           (money(company["Q1"]), "Q1, April to June 2026", "the base")])
kit.check("the card's quarters add back to the half-year", company["Q1"] + company["Q2"] == half_year)
kit.check("the change is measured on Q1", abs(company["change"] - (company["Q2"] - company["Q1"]) / company["Q1"] * 100) < 1e-9)
'''),
        md('''
**What happened.** The answer is a. The card reads: "All segments, Q2, July to September 2026: Rs 9.84
crore, down 1.6 percent on Q1, April to June 2026 (Rs 10.00 crore); 100.0 percent of company revenue
in Q2." The sentence beside it says where the change sits, and chapter 2 gave both halves: Business
invoices carry Rs 14.30 lakh of the Rs 16.00 lakh fall, and Retail-Plus, the paid tier, fell 29.4
percent because members ordered less often.
'''),
        md('''
## 3. What does "Retail-Plus revenue down 29.4 percent" leave out?

The second slot on the front page is drafted as "Retail-Plus revenue down 29.4 percent". The
percentage is right.

**Predict before you run.** What must sit beside it? a) nothing, since it is correct; b) its rupee
base and its share of company revenue; c) the Business figure for comparison; d) the protect list.
'''),
        code('''
rp = card("Retail-Plus")
fall = rp["Q1"] - rp["Q2"]
wrong_base = (rp["Q2"] - rp["Q1"]) / rp["Q2"] * 100
kit.stats([(f"{rp['change']:+.1f}%", "Retail-Plus, as drafted", "no base, no share"),
           (lakh(fall), "the fall in rupees", "on a Rs 10.00 crore quarter"),
           (f"{rp['share']:.1f}%", "Retail-Plus's share of Q2", "the base the draft left out"),
           (f"{wrong_base:+.1f}%", "the same change divided by Q2", "the slip that makes it worse")])
kit.bridge(("Q1, all segments", company["Q1"]),
           [(s, int(seg_q.loc[s, "Q2"] - seg_q.loc[s, "Q1"])) for s in SEGMENTS],
           end_label="Q2, all segments", fmt=money, lit=(2,), lo=97_000_000,
           title="Where the Rs 16.00 lakh went; the axis starts at Rs 9.70 crore so the moves show")
kit.check("the drafted percentage is right on its own base", abs(rp["change"] + 29.43) < 0.01, f"{rp['change']:.2f} percent")
kit.check("Retail-Plus is under half a percent of Q2 revenue", rp["share"] < 0.5, f"{rp['share']:.2f} percent")
'''),
        md('''
**What happened: the plausible wrong answer.** The answer is b. Read without its base, "down 29.4
percent" sounds like the business collapsing, and the meeting argues about a panic instead of about
members who order less often. It is 29.4 percent of Rs 5.86 lakh: a fall of Rs 1.72 lakh on a Rs 10.00
crore quarter, where Retail-Plus is 0.4 percent of revenue. A second slip makes it worse: divide the
same change by Q2 instead of Q1 and it reads 41.7 percent. **The check:** the rupee base and the share
beside every percentage, and the change divided by the earlier period. **The fix:** "Retail-Plus, Q2:
Rs 4.13 lakh, down 29.4 percent on Q1 (Rs 5.86 lakh); 0.4 percent of company revenue."
'''),
        md('''
## 4. What does the trend beside the number show, and what happens when a director changes the scope?

The chief of staff asked for the number "with its trend". Six months of revenue, drawn as a line, for
the scope the card states. The scope is an input a director can change: all segments, all except
Business, or Retail-Plus alone.

**Predict before you run.** Taking Business out, the change on the card reads: a) down 1.6 percent; b)
down 17.3 percent; c) down 29.4 percent; d) up 33.9 percent.
'''),
        code('''
orders["month"] = orders["order_date"].str[:7]
months = sorted(orders["month"].unique())
labels = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]
by_month = {scope: [int(orders[(orders["month"] == m) & orders["segment"].isin(segs)]["order_amount"].sum()) for m in months]
            for scope, segs in SCOPES.items()}
kit.line(labels, [("All segments", by_month["All segments"], "lit")], fmt=money,
         title="Company revenue by month: Business invoices make the line jump")
kit.line(labels, [("All except Business", by_month["All except Business"], "bad"),
                  ("Retail-Plus", by_month["Retail-Plus"], "")], fmt=money,
         title="The consumer segments by month: a slide from June to September")
kit.table(["The director asks for", "The card says"], [(s, card(s)["sentence"]) for s in SCOPES], caption="One input, three honest cards")
kit.check("July's company revenue sits above June's", by_month["All segments"][3] > by_month["All segments"][2])
kit.check("the consumer line ends lower than it stood in June", by_month["All except Business"][-1] < by_month["All except Business"][2])
'''),
        md('''
**What happened.** The answer is b. Taking Business out, revenue fell from Rs 9.86 lakh to Rs 8.15 lakh,
down 17.3 percent, 0.8 percent of company revenue. The company line jumps in July to Rs 4.51 crore, 45
percent above June, because corporate invoices landed in it, and then falls; the consumer line slides
from Rs 3.32 lakh in June to Rs 2.48 lakh in September. Two directors asking for two scopes get two
honest cards, each saying which scope it shows, so down 1.6 percent and down 17.3 percent are never
compared as one number.
'''),
        md('''
## A second route: does the warehouse reach the same change by its own query?

The card was computed from the export. The second route asks the warehouse's orders table, joined to
its customers for the segment, and asserts the same two changes.
'''),
        code('''
wq = {r["quarter"]: r["revenue"] for r in warehouse("SELECT quarter, sum(amount) AS revenue FROM orders GROUP BY quarter")}
wp = {r["quarter"]: r["revenue"] for r in warehouse(
    "SELECT o.quarter, sum(o.amount) AS revenue FROM orders o JOIN customers c USING (customer_id) "
    "WHERE c.segment = 'Retail-Plus' GROUP BY o.quarter")}
kit.table(["Scope", "Card, from the export", "Warehouse"],
          [("All segments", f"{company['change']:+.2f}%", f"{change(wq['Q1'], wq['Q2']):+.2f}%"),
           ("Retail-Plus", f"{rp['change']:+.2f}%", f"{change(wp['Q1'], wp['Q2']):+.2f}%")])
kit.check("the company change matches the warehouse", abs(company["change"] - change(wq["Q1"], wq["Q2"])) < 1e-9)
kit.check("the Retail-Plus change matches the warehouse", abs(rp["change"] - change(wp["Q1"], wp["Q2"])) < 1e-9)
'''),
        md('''
> **Kavya's review.** "A number without its period is read against whatever the director remembers. A
> percentage without its base is read as whatever the director fears. If the card cannot say which
> months, against what and out of how much, it goes back."
'''),
        md('''
### In the interview: how do you present one number so a director cannot misread it?

**[F] How do you present one number so it is not misread?** With its period, its comparison and its
base, and one sentence on what moved it. Here: Q2, July to September 2026, Rs 9.84 crore, down 1.6
percent on Q1's Rs 10.00 crore; Business invoices carry most of the rupees, and Retail-Plus fell 29.4
percent because members ordered less often. I compare with the previous quarter because the warehouse
holds two quarters; with a year of history I would set the quarter beside the same quarter a year
earlier, as DMart's release does, since a retailer's quarters have seasons.

**[F] A director says revenue doubled; your card says Rs 19.84 crore. What is missing?** The period. It
is two quarters added together, read against one quarter from memory; the card needs its months and its
comparison, and then it reads down 1.6 percent.

**[D] A segment fell 29 percent and is 0.4 percent of revenue. How do you write it so the room reads
its size right?** With its base and its share, in the sentence beside the headline: Rs 4.13 lakh, down
29.4 percent on Rs 5.86 lakh, 0.4 percent of revenue. It matters because it is the paid tier and the
fall is in how often members buy; it is small in rupees, and the sentence says both.
'''),
        md('''
### Depth: when is a change in a share said in points, and when in percent?

A change in a rate is quoted in points, a change in an amount in percent. If the share of revenue from
the consumer segments moved from 0.99 percent in Q1 to 0.83 percent in Q2, it fell by 0.16 percentage
points, which is a 16 percent fall in the share. Both are true and they read very differently, so a
card that shows a share says which it means. The consumer shares here come from this notebook's own
quarters: Rs 9.86 lakh of Rs 10.00 crore, and Rs 8.15 lakh of Rs 9.84 crore.
'''),
        md('''
## What does the card carry so a director reads it right, question by question?

1. Option d: the quarter against the last, with its base, its sentence and its trend.
2. "Revenue Rs 19.84 crore" is two quarters, and a director who remembers Q1's Rs 10.00 crore reads it as up 98.4 percent.
3. "Q2, July to September 2026: Rs 9.84 crore, down 1.6 percent on Q1, April to June 2026 (Rs 10.00 crore)."
4. The base and the share: Rs 1.72 lakh on Rs 5.86 lakh, 0.4 percent of revenue; divided by Q2 by mistake it reads 41.7 percent.
5. The company line jumps in July on corporate invoices; without Business, revenue is down 17.3 percent, and each scope prints its own name.
6. The warehouse gives the same -1.6 percent and -29.4 percent.

The next question is chapter 5's: Kavya wants to know which of the week's steps may live in this workbook
at all.
'''),
        code("kit.check_summary()"),
    ]


# ============================================================================= chapter 5
def ch5():
    return [
        md('''
# 5. Which of the week's steps belong in the workbook, which must never be done there, and how do the two stay in step?

**Week 2, Friday. Chapter 5 of 6.** Chapters 1 to 4 built the chief of staff's three deliverables: the
tree by segment for both quarters, tied to the warehouse's Rs 10.00 crore and Rs 9.84 crore; the protect
list of fifty with a lookup that says when an id is missing; and the front-page card with its period,
comparison and base, which reads down 1.6 percent and prints Retail-Plus's 29.4 percent fall as
Rs 1.72 lakh, 0.4 percent of revenue. Kavya's challenge is the rule behind them.

Three tools did the week's work. The warehouse is the Postgres database that holds one row per order
and one per payment, the source of truth anyone can query and rerun. pandas is the Python library for
tables, where an analyst tries an idea, checks it and tries again before anyone relies on the result;
that trying is what this chapter calls the analyst's iteration. The workbook is the Excel file a
director opens. A dedupe is any step that makes each order or payment count once.

> **Kavya asks.** "Everything you built this week has to survive a room that only has Excel. Which parts
> belong in Excel, which parts must never be in Excel, and how do you keep the two from drifting apart?"
>
> Kavya Nair, senior analyst, Kalpa Retail data team

**Who needs the answer.** Kavya signs the team's operating rule; Anand Iyer, the finance controller,
has an analyst who audits every number Finance relies on; the data platform lead owns the warehouse. A
step done in the wrong tool ships a number nobody can rerun, and a join done in a sheet can report as
unpaid money that customers have paid.

**The questions on the way.**
1. Where could the week's work live?
2. What did each day of the week build, and what does each step touch?
3. What does booked against collected say when a lookup does the join?
4. Why is it wrong, and what does adding every payment say?
5. Where does each of the week's steps belong?
6. How do the workbook and the warehouse stay in step?

**The metric at stake.** Collected against booked, Tuesday's report for Anand: booked is the value of
the orders, collected is the money received against them. It is the test case for the rule, because it
needs a join, one order to several payments.

**Who else faces it.** In October 2020 Public Health England reported that "15,841 cases between 25
September and 2 October were not included in the reported daily COVID-19 cases" (GOV.UK, PHE statement
on delayed reporting of COVID-19 cases, 4 October 2020, checked 30 September 2026). The BBC explained
that the files passed through templates in the old XLS format, so "each template could handle only
about 65,000 rows of data rather than the one million-plus rows that Excel is actually capable of" (BBC
News, 5 October 2020, checked 30 September 2026). A step of a data pipeline was running in a
spreadsheet.
'''),
        md('''
**Setup.** The cell loads the raw export, one row per payment with the order's amount repeated on each,
counts each order once the way chapter 2 did, and defines `warehouse()`.
'''),
        setup(HELPERS, LOAD_RAW, WAREHOUSE, COUNT_ONCE,
              last='print(f"{len(raw):,} payment rows, {len(orders):,} orders")'),
        mapcell(5, ["the options\nfour places the work could live", "1. what each day's step touches",
                    "2. the trap\na lookup doing a join", "3. every payment added once",
                    "4. where each step belongs", "a second route\nbooked less unpaid",
                    "5. how the two stay in step"]),
        md('''
## Where could the week's work live, and what does each arrangement cost?

| Option | Who does what | What it assumes |
|---|---|---|
| a) Everything in the workbook | Joins, dedupes, ranks and the card, all as formulas over the exports | The author reruns every step by hand each Monday |
| b) The split | The warehouse computes and cleans; pandas iterates; the workbook presents | Each tool does only what it is best at, and the three are tied on every refresh |
| c) pandas does it all and pastes values | A notebook writes the numbers into the workbook as values | Nobody changes an assumption in the room |
| d) A dashboard on the warehouse | Every number live from the warehouse | Every director has a login, which the brief rules out |
'''),
        code('''
payments = warehouse("SELECT count(*) AS n FROM payments")[0]["n"]
sizing = [
    ("a) all in the workbook", f"{len(orders):,} SUMIFS x {len(raw):,} rows = {len(orders) * len(raw):,} tests a recalculation", "its author, by hand", "none beyond the cells"),
    ("b) the split", f"one GROUP BY over {payments:,} payments", "anyone with the query", "the query, in version control"),
    ("c) pandas pastes values", f"one groupby over {len(raw):,} rows", "the analyst, with the notebook", "the notebook"),
    ("d) dashboard", "a query a view", "the dashboard's owner", "the queries"),
]
kit.table(["option", "collected per order costs", "who can rerun it", "what an auditor can trace"], sizing,
          caption="The four arrangements, sized on one step: collected per order")
kit.bars([("a) SUMIFS in the workbook", len(orders) * len(raw)), ("b) warehouse GROUP BY", payments),
          ("c) pandas groupby", len(raw))], lit=(0,),
         title="Rows or tests touched each time collected per order is computed")
'''),
        md('''
**The best-fit call: b, the split.** The warehouse owns every join, dedupe and rank, because a query
can be rerun and audited; pandas owns the analyst's iteration; the workbook owns what a director
sees and changes in the meeting. **The fact
that would change it:** a one-off question nobody audits and nobody reruns can live in a sheet, and a
question Finance will rely on every week cannot.
'''),
        md('''
## 1. What did each day of the week build, and what does each step touch?

**Predict before you run.** Which of the week's steps touches the most rows? a) the tree by segment and
quarter; b) booked against collected; c) the top fifty per segment; d) Friday's pivot.
'''),
        code('''
steps = [
    ("Monday", "the tree by segment and quarter", "orders", "a GROUP BY"),
    ("Tuesday", "booked against collected", "orders and payments", "a join, one order to several payments"),
    ("Wednesday", "the top fifty per segment, falling spend", "orders", "window functions: a rank or a running total over rows, in SQL"),
    ("Thursday", "the customer table", "orders, customers, campaign exposure", "a merge in pandas, checked to stay one row per customer"),
    ("Friday", "the pivot, the lookup, the card", "the two exports", "presentation in the workbook"),
]
counts = {"orders": warehouse("SELECT count(*) AS n FROM orders")[0]["n"], "payments": payments}
kit.table(["Day", "Step", "Tables it reads", "How"], steps, caption="The week's steps and what each reads")
kit.bars([("Tuesday: orders and payments", counts["orders"] + counts["payments"]), ("Monday: orders", counts["orders"]),
          ("Wednesday: orders", counts["orders"]), ("Friday: the export's rows", len(raw))], lit=(0,),
         title="Rows each step reads; Tuesday's join reads two tables at once")
kit.check("Tuesday's join reads more rows than any single table", counts["orders"] + counts["payments"] > len(raw))
'''),
        md('''
**What happened.** The answer is b. Tuesday's report joins 1,000 orders to 1,428 payment rows, eight of
which match no order, and it is
the one step where one row on one side meets several on the other. That is the step to watch when
somebody offers to "just do it in the sheet".
'''),
        md('''
## 2. What does booked against collected say when a lookup does the join?

Anand asks whether the deck pack could carry Tuesday's collected figure as well, computed in the
workbook so nobody needs a login. A hurried analyst fills a lookup beside each order in the raw export:
`=VLOOKUP(A2, RawExport!A:H, 7, FALSE)`, the exact match on the order id that fetches `paid_amount`.

**Predict before you run.** Collected, added up over the 1,000 orders, reads about: a) Rs 19.7 crore; b)
Rs 11.8 crore; c) Rs 39 crore; d) exactly booked.
'''),
        code('''
first_paid = raw.drop_duplicates("order_id").set_index("order_id")["paid_amount"]    # what a lookup returns
booked = int(orders["order_amount"].sum())
looked_up = int(first_paid.sum())
kit.stats([(money(booked), "booked", "the orders' value"),
           (money(looked_up), "collected, by lookup", "one payment per order"),
           (money(booked - looked_up), "outstanding, it says", f"{(booked - looked_up) / booked * 100:.1f} percent of booked")])
by_channel = orders.groupby("channel")["order_amount"].sum()
lk_channel = raw.drop_duplicates("order_id").groupby("channel")["paid_amount"].sum()
kit.columns(["app", "store", "web"], [("booked", [int(by_channel[c]) for c in ["app", "store", "web"]]),
                                      ("collected, by lookup", [int(lk_channel[c]) for c in ["app", "store", "web"]])],
            fmt=money, title="By channel, the lookup says every channel collected about 60 percent")
'''),
        md('''
**What happened: the plausible wrong answer.** The answer is b. The lookup says Rs 11,83,81,974
collected against Rs 19,84,00,000 booked, Rs 8.00 crore outstanding, 40.3 percent. Every formula is an
exact match and every row looks right. On that figure Anand's collections team
chases Rs 8 crore from accounts that have paid, most of them corporate buyers, and the board pack
reports a cash problem Kalpa does not have.
'''),
        md('''
## 3. Why is it wrong, and what does adding every payment say?

**Why it is wrong.** A lookup returns the first row that matches and stops. The export has one row per
payment, and 450 orders sit on two rows: 400 paid in two instalments, whose second payment the lookup
never reads, and 50 that the gateway posted twice, whose two rows are the same payment. **The check
that catches it:** count the rows each order has, and read any order with two rows before trusting its
first. **The fix:** add every payment once. In the sheet that is `=SUMIFS(G:G, A:A, A2)` over the rows
left once the gateway's exact copies are gone; in the warehouse it is Tuesday's join, one row per
payment.

**Predict before you run.** With every payment added once, collected is short of booked by about: a)
Rs 8.00 crore; b) Rs 17.5 lakh; c) nothing; d) Rs 39 crore.
'''),
        code('''
paid_rows = raw.drop(columns=["quarter", "first_row"]).drop_duplicates()   # a gateway copy is one payment, posted twice
collected = int(paid_rows["paid_amount"].sum())                             # =SUMIFS(G:G, A:A, A2), every payment once
copies = len(raw) - len(paid_rows)
second_inst = collected - looked_up
kit.bridge(("collected, by lookup", looked_up), [("second instalments of 400 orders", second_inst)],
           end_label="collected, every payment once", fmt=money, lit=(0,),
           title="What the lookup left out: the second instalments")
kit.stats([(money(collected), "collected, every payment once", "the warehouse's join, or SUMIFS on the payments"),
           (money(booked - collected), "short of booked", f"{(booked - collected) / booked * 100:.1f} percent"),
           (f"{copies}", "gateway copies set aside", "the same payment, posted twice")])
kit.check("the lookup and the sum differ on exactly the orders with two rows",
          int((raw.groupby("order_id").size() > 1).sum()) == 450)
kit.check("every payment added once leaves collected within 1 percent of booked", (booked - collected) / booked < 0.01)
'''),
        md('''
**What happened.** The answer is b. Every payment added once gives Rs 19,66,45,070 collected,
Rs 17,54,930 short of booked, 0.9 percent, which is exactly Tuesday's list of orders nobody has paid
for. **What changed:** Rs 7,82,63,096 of "outstanding" money disappears, the second instalments of 400
orders, and the 50 gateway copies count once, as the payments they are. The join belongs where Tuesday
did it, in the warehouse, and a SUMIFS in the sheet is only a check against it.
'''),
        md('''
## 4. Where does each of the week's steps belong?

**Predict before you run.** Counting each order once in the raw export belongs: a) in the workbook, as
the first-row flag; b) in the warehouse, as an export at the order grain; c) in pandas, as a
drop_duplicates; d) anywhere, since all three give Rs 19.84 crore.
'''),
        code('''
rule = [
    ("the tree by segment and quarter", "warehouse", "Finance audits it; a GROUP BY anyone can rerun"),
    ("counting each order once", "warehouse", "a grain fix is cleaning; the export should arrive at the order grain"),
    ("booked against collected", "warehouse", "a join, one order to several payments"),
    ("the top fifty, with a rule for members tied at fifty", "warehouse", "a rank Finance and Marketing both rely on"),
    ("the customer table", "pandas", "the analyst's weekly iteration, until Finance relies on it"),
    ("the pivot, the lookup, the card", "workbook", "presentation on an export that ties"),
    ("a director's what-if", "workbook", "a labelled input beside the actual, never over it"),
]
kit.table(["Step", "Where it lives", "Why"], rule, caption="The week's steps, placed")
tools = ["warehouse", "pandas", "workbook"]
kit.matrix([r[0] for r in rule], tools, [["owns it" if r[1] == t else "" for t in tools] for r in rule],
           title="Each step in one place: the warehouse owns anything Finance audits")
kit.check("every step lives in exactly one place", all(sum(r[1] == t for t in tools) == 1 for r in rule))
'''),
        md('''
**What happened.** The answer is b. The first-row flag in chapter 2 was the right move for Friday's
deadline, and it is a cleaning step with no record; next week the export should arrive at the order
grain from the warehouse, and the flag becomes a check. Written as the team's rule, in three lines: the warehouse owns
the number and every join, dedupe and rank Finance relies on; pandas owns the analyst's iteration until
Finance relies on it; the workbook owns the last mile, presenting, slicing, looking up and taking
what-ifs as labelled inputs, on an export that ties, and nobody types over the source.
'''),
        md('''
## A second route: does booked less the orders nobody paid for give the same collected figure?

A second route has to be able to disagree, so it never adds a payment. It starts from the warehouse's
booked revenue and takes away the orders that have no payment at all, Tuesday's unpaid list, found
with an anti-join: every order with no matching row in the payments table.
'''),
        code('''
wb = warehouse("SELECT sum(amount) AS booked FROM orders")[0]["booked"]
unpaid = warehouse("SELECT count(*) AS n, sum(amount) AS amount FROM orders o "
                   "WHERE NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)")[0]
kit.table(["Figure", "The export, every payment once", "The warehouse, booked less unpaid"],
          [("booked", kit.rupees(booked), kit.rupees(wb)),
           ("unpaid orders", "", f"{unpaid['n']} orders, {kit.rupees(unpaid['amount'])}"),
           ("collected", kit.rupees(collected), kit.rupees(wb - unpaid["amount"]))])
kit.bridge(("booked, the warehouse", wb), [("orders nobody has paid for", -unpaid["amount"])],
           end_label="collected", fmt=money, lo=196_000_000,
           title="Booked less the unpaid list; the axis starts at Rs 19.60 crore")
kit.check("collected ties to booked less the unpaid list, to the rupee", collected == wb - unpaid["amount"])
kit.check("booked ties too", booked == wb)
'''),
        md('''
## 5. How do the workbook and the warehouse stay in step?

With a drift check that runs on every refresh. The workbook needs no login for it: the data platform
lead sends the warehouse's control totals, orders and booked revenue per quarter, on a small tab
beside each export, and the Checks tab compares the workbook's own totals with them, live. A mismatch
holds the deck until someone knows why. The cell below
runs it twice: on this export, and on the same export as it would have looked if it had been pulled a
week early, before the last week of September's orders arrived.

**Predict before you run.** The check on the early export: a) passes, since every row in it is real; b)
holds the deck, since Q2 falls short of the warehouse; c) holds only the protect list; d) cannot run.
'''),
        code('''
def drift(export_orders):
    """The workbook's quarters against the warehouse's, as the Checks tab would compare them."""
    wq = {r["quarter"]: r for r in warehouse("SELECT quarter, count(*) AS n, sum(amount) AS revenue FROM orders GROUP BY quarter")}
    rows = []
    for q in ["Q1", "Q2"]:
        mine = export_orders[export_orders["quarter"] == q]
        rows.append((q, len(mine), wq[q]["n"], int(mine["order_amount"].sum()), wq[q]["revenue"]))
    ok = all(r[1] == r[2] and r[3] == r[4] for r in rows)
    return rows, ("ship" if ok else "hold")


today, verdict_today = drift(orders)
early = orders[orders["order_date"] < "2026-09-22"]
week_early, verdict_early = drift(early)
kit.table(["Export", "Quarter", "Orders in it", "Warehouse orders", "Revenue in it", "Warehouse revenue", "Verdict"],
          [("today", *r[:3], kit.rupees(r[3]), kit.rupees(r[4]), verdict_today) for r in today]
          + [("a week early", *r[:3], kit.rupees(r[3]), kit.rupees(r[4]), verdict_early) for r in week_early])
kit.flow(["refresh the export", "control totals\\nagainst the warehouse", f"today: {verdict_today}", f"a week early: {verdict_early}"],
         kinds=["plain", "lit", "good", "bad"], title="The drift check, run on every refresh")
kit.check("today's export ties, so the deck ships", verdict_today == "ship")
kit.check("the early export is caught", verdict_early == "hold")
'''),
        md('''
**What happened.** The answer is b. Every row in the early export is real, and Q2 still falls short of
the warehouse, so the check holds the deck until someone pulls a fresh export. The same check catches a
number typed over in the workbook, since the workbook's totals would no longer match; chapter 6 hands the
workbook to a director and builds the tab that runs it.
'''),
        md('''
> **Kavya's review.** "Excel presents; it does not clean, join or compute the source of truth, because a
> sheet with a typed-over cell has no audit trail. The warehouse owns the numbers, pandas owns your
> iteration, Excel owns the last mile, and the drift check holds the deck whenever the workbook stops
> tying to the warehouse."
'''),
        md('''
### In the interview: SQL, pandas or Excel, and why can a lookup not stand in for a join?

**[S] SQL, pandas or Excel: how do you choose?** By who has to trust the number and who has to rerun
it. Anything Finance relies on, and every join, dedupe or rank behind it, is SQL in the warehouse,
rerun by anyone with the query. The analyst's iteration is pandas until Finance relies on it, so
Thursday's customer table could be built in pandas and moves upstream once Marketing depends on it
every Monday. The room's last mile is Excel on an export that ties, where a director can slice and
ask what-ifs.

**[F] A lookup does a join in a sheet and collected falls by 40 percent. What happened?** The lookup
returned the first payment of each order and ignored the rest. Here 450 orders had two payment rows, so
collected read Rs 11.84 crore against Rs 19.84 crore booked; adding every payment once gives Rs 19.66
crore, 0.9 percent short, which is exactly the orders nobody has paid for. One-to-many relations are
joined in the warehouse, and a SUMIFS in the sheet is only a check.

**[D] Kavya asks for the operating rule in three lines. Say it.** The warehouse owns the number and every
join, dedupe and rank Finance relies on. pandas owns the analyst's iteration until Finance relies on it.
Excel owns the last mile, on an export that ties, with what-ifs as labelled inputs, and a drift check on
every refresh ties the sheet back to the warehouse.
'''),
        md('''
### Depth: why did a row limit lose cases instead of stopping the job?

The BBC's account of the Public Health England loss says each XLS template "could handle only about
65,000 rows", and that "since each test result created several rows of data, in practice it meant that
each template was limited to about 1,400 cases" (BBC News, 5 October 2020, checked 30 September 2026).
Microsoft's documentation gives the old format's limit exactly: "Excel 2003 supports a maximum of 65,536
rows per worksheet" (Microsoft Learn, Work around the Excel 2003 row limitation, checked 30 September
2026). Rows past the limit were dropped with no error, and a lookup that takes one payment of two
fails the same way: nothing turns red, and the total comes out smaller than the truth. A drift check
against an upstream count is what turns a silent loss into a held release.
'''),
        md('''
## Where does each of the week's steps live, and how do the two stay in step, question by question?

1. Option b, the split: the warehouse computes and cleans, pandas iterates, the workbook presents.
2. Tuesday's booked against collected is the heaviest step, a join of 1,000 orders to 1,428 payment rows, eight of which match no order; the rest read one table.
3. A lookup doing the join says Rs 11,83,81,974 collected, "Rs 8.00 crore outstanding", 40.3 percent.
4. It took the first payment of 450 two-row orders; every payment added once gives Rs 19,66,45,070, Rs 17,54,930 short, 0.9 percent, exactly the orders nobody has paid for.
5. Joins, dedupes, ranks and anything Finance audits live in the warehouse; the customer table in pandas; the pivot, lookup, card and what-ifs in the workbook.
6. A drift check on every refresh ties the workbook's quarters to the warehouse: today's export ships, a week-early export is held.

The next question is chapter 6's: what happens when a director takes the workbook in the room.
'''),
        code("kit.check_summary()"),
    ]


# ============================================================================= chapter 6
def ch6():
    return [
        md(f'''
# 6. When a director takes the workbook in the room, what can they break, and which checks catch it before anyone reads a wrong number?

**Week 2, Friday. Chapter 6 of 6.** Chapters 1 to 4 built the three deliverables: the tree for both
quarters tied to the warehouse, the protect list of fifty from Rs 25,840 down to Rs 8,580 with a lookup
that says when an id is missing, and the front-page card with its period, comparison and base. Chapter 5
set the rule: the warehouse owns the number, pandas the iteration, the workbook the last mile, with a
drift check on every refresh. The chief of staff's last condition is the hardest: "If a director changes
an assumption in the room, the sheet must recalculate in front of them."

{ASK}

**Who needs the answer.** The chief of staff hands the laptop across the table mid-meeting; the
directors will filter, sort, type and ask what-ifs; the head of Retail-Plus sizes each city's retention
budget from the list. A total that keeps counting rows a filter has hidden sizes a city's budget on the
whole list, and a number typed over a formula becomes a figure nobody can trace.

**The questions on the way.**
1. How could the team protect it?
2. What will a director do to the workbook?
3. What does the list's total say when a director filters it to one city?
4. What do SUBTOTAL(109) and SUBTOTAL(103) say?
5. Where does a director's assumption go, so the sheet recalculates honestly?
6. Which checks does the Checks tab run, and what does its release hold?

**The metric at stake.** The protect list's total by city, which sizes each city's retention budget, and
the release sentence that says what ships on Monday.

**Who else faces it.** In September 2008 Barclays bought parts of the bankrupt Lehman Brothers. A law
firm reformatting a spreadsheet of the contracts into a PDF for the court's website exposed rows that
had been hidden, and "contracts that had been marked as "hidden" in the spreadsheet when it was
received by the law firm were added to the purchase offer during the reformatting process"; Barclays
then asked the court to exclude 179 contracts it said were included by mistake (Computerworld, 14
October 2008, checked 30 September 2026). Rows a person could not see still counted.
'''),
        md('''
**Setup.** The cell loads the customer table and the raw export from `../data/`, rebuilds chapter 3's
protect list (the 106 Retail-Plus members sorted by revenue, the top fifty kept), and defines
`warehouse()`, which the Checks tab uses to tie the sheet to the warehouse.
'''),
        setup(HELPERS, LOAD_TABLE, LOAD_RAW, WAREHOUSE, PROTECT, last='print(len(protect), "members on the list,", kit.rupees(int(protect["revenue"].sum())), "together")'),
        mapcell(6, ["the options\nfour ways to protect it", "1. what a director will do",
                    "2. the trap\na total under a filter", "3. SUBTOTAL, visible rows only",
                    "a second route\nSUMIFS by city", "4. an assumption as an input",
                    "5. the Checks tab and the release"]),
        md('''
## How could the team protect the workbook, and what does each way cost?

| Option | What the director can still do | What a mistake looks like |
|---|---|---|
| a) Protect every cell | Read it; filter and sort only if the protection allows them | Nothing can go wrong, and no what-if can be asked |
| b) Send a PDF | Read it | Nothing can go wrong, and nothing recalculates |
| c) Yellow input cells, every other cell a formula, and a Checks tab | Filter, sort and change any yellow input | A red line on the Checks tab, and a release that holds |
| d) A copy for each director | Anything | Copies that disagree by the end of the meeting, with no way to tell which is right |
'''),
        code('''
actions = ["filter", "sort", "type over a cell", "change an assumption", "paste a new export"]
allowed = {"a) protect every cell": [1, 1, 0, 0, 0], "b) PDF": [0, 0, 0, 0, 0],
           "c) inputs and a Checks tab": [1, 1, 1, 1, 1], "d) a copy each": [1, 1, 1, 1, 1]}
caught = {"a) protect every cell": "nothing to catch", "b) PDF": "nothing to catch",
          "c) inputs and a Checks tab": "each check turns red", "d) a copy each": "nothing: copies drift apart"}
kit.table(["option", "director actions it allows, of 5", "a wrong number is caught by"],
          [(k, sum(v), caught[k]) for k, v in allowed.items()], caption="The four ways, sized on the five things a director does")
kit.matrix(list(allowed), actions, [["allowed" if a else "blocked" for a in v] for v in allowed.values()],
           title="What each way lets a director do in the room")
'''),
        md('''
**The best-fit call: c.** It is the only way that lets a director do all five things and still turns a
wrong number red before it is read. Protecting every cell (a) or sending a PDF (b) fails the brief, since
nothing recalculates; a copy each (d) ends the meeting with several versions of the truth. **The fact
that would change it:** a board pack nobody is meant to change goes as a PDF.
'''),
        md('''
## 1. What will a director do to the workbook?

**Predict before you run.** Which of these changes what a number on the sheet means without any error
appearing? a) filtering the list; b) typing a figure over a formula; c) changing a yellow input; d) a
and b, and neither shows an error.
'''),
        code('''
effects = [("filter the list to a city", "the rows on screen change; a SUM below them does not", "silent"),
           ("sort one column on its own", "the rows' values separate from their ids", "silent"),
           ("type a figure over a formula", "the cell stops following its source", "silent"),
           ("change a yellow input", "every formula reading it recalculates", "honest"),
           ("paste in a new export", "the formulas read the new rows, if their ranges reach them", "checked by the drift check")]
kit.table(["What a director does", "What happens to the sheet", "Error shown?"], effects)
kit.vflow([e[0] + "\\n" + e[2] for e in effects], kinds=["bad", "bad", "bad", "good", "plain"],
          title="Three of the five change a number's meaning silently")
'''),
        md('''
**What happened.** The answer is d. A filter and a typed-over cell both change what a number means,
and neither shows an error; a one-column sort is the third silent one. A yellow input is the honest way to
change a number, because every formula that reads it recalculates in front of the room. The next two
questions take the filter, and question 5 takes the input.
'''),
        md('''
## 2. What does the list's total say when a director filters it to one city?

The protect list has a total at its foot, `=SUM(E2:E51)`. The head of Retail-Plus asks to see the
Mumbai members, and a director filters the city column to Mumbai.

**Predict before you run.** With eleven Mumbai members on screen, the foot reads: a) Rs 1,56,790; b)
Rs 7,14,890; c) 11; d) #VALUE!.
'''),
        code('''
visible = protect["city"] == "Mumbai"                 # the rows the filter leaves on screen
foot_sum = int(protect["revenue"].sum())              # =SUM(E2:E51) adds every row, hidden or not
on_screen = int(protect.loc[visible, "revenue"].sum())
kit.stats([(kit.rupees(foot_sum), "the foot, SUM", "all fifty rows"),
           (kit.rupees(on_screen), "what the eleven on screen spent", "Mumbai's list"),
           (f"{foot_sum / on_screen:.1f} times", "the overstatement", "read as Mumbai's list")])
by_city = protect.groupby("city")["revenue"].sum().sort_values(ascending=False)
kit.bars([(c, int(v)) for c, v in by_city.items()], fmt=kit.rupees, lit=(list(by_city.index).index("Mumbai"),),
         title="The protect list's revenue by city: Mumbai is one bar, and SUM reports all six")
kit.check("SUM under the filter still adds all fifty rows", foot_sum == int(protect["revenue"].sum()))
kit.check("the eleven on screen are a small part of it", on_screen < foot_sum / 4, kit.rupees(on_screen))
'''),
        md('''
**What happened: the plausible wrong answer.** The answer is b. The foot still reads Rs 7,14,890, the
whole list, while the eleven Mumbai members on screen spent Rs 1,56,790. **Why it is wrong:** the Mumbai
store head is told the members on their list spent Rs 7.15 lakh, and a retention budget sized on that is
4.6 times too big. SUM adds every row in its range, hidden or not. **The check that catches it:** count
the rows on screen beside the rows the total adds; if the two differ, the total is adding rows nobody can
see.
'''),
        md('''
## 3. What do SUBTOTAL(109) and SUBTOTAL(103) say?

`=SUBTOTAL(109, E2:E51)` adds only the rows a filter leaves visible, and `=SUBTOTAL(103, A2:A51)` counts
them. Microsoft's page says SUBTOTAL "ignores any rows that are not included in the result of a filter,
no matter which function_num value you use", and that 101 to 111 also ignore rows hidden by hand, while
1 to 11 include them (Microsoft Support, SUBTOTAL function, checked 30 September 2026).

**Predict before you run.** A director also hides Delhi's rows by hand, with no filter on. Which foot
still adds Delhi? a) SUM only; b) SUM and SUBTOTAL(9); c) SUBTOTAL(109) only; d) none of them.
'''),
        code('''
def foot(values, filtered_out, hidden_by_hand, how):
    """What a foot formula adds: SUM adds everything; SUBTOTAL drops filtered rows, and 109 drops hand-hidden rows too."""
    keep = []
    for v, f, h in zip(values, filtered_out, hidden_by_hand):
        if how == "SUM" or (how == "SUBTOTAL(9)" and not f) or (how == "SUBTOTAL(109)" and not f and not h):
            keep.append(v)
    return sum(keep)


rev = protect["revenue"].tolist()
no = [False] * 50
mumbai_filter = (~visible).tolist()
delhi_hidden = (protect["city"] == "Delhi").tolist()
rows = []
for how in ["SUM", "SUBTOTAL(9)", "SUBTOTAL(109)"]:
    rows.append((how, kit.rupees(foot(rev, mumbai_filter, no, how)), kit.rupees(foot(rev, no, delhi_hidden, how))))
kit.table(["The foot", "Filtered to Mumbai", "Delhi hidden by hand"], rows, caption="Three foot formulas, two ways of hiding rows")
kit.stats([(kit.rupees(foot(rev, mumbai_filter, no, "SUBTOTAL(109)")), "SUBTOTAL(109)", "the eleven on screen"),
           (f"{int(visible.sum())} of 50", "SUBTOTAL(103)", "the rows on screen")])
kit.check("SUBTOTAL(109) follows the filter", foot(rev, mumbai_filter, no, "SUBTOTAL(109)") == on_screen)
kit.check("only SUBTOTAL(109) drops rows hidden by hand",
          foot(rev, no, delhi_hidden, "SUBTOTAL(9)") == foot_sum and foot(rev, no, delhi_hidden, "SUBTOTAL(109)") < foot_sum)
'''),
        md('''
**What happened.** The answer is b. SUM and SUBTOTAL(9) both keep adding Delhi's hand-hidden rows;
SUBTOTAL(109) drops them, and drops Mumbai's filtered-out rows too. **The fix:** the foot is
`=SUBTOTAL(109, E2:E51)` with `=SUBTOTAL(103, A2:A51)` beside it, and the list's label says which rows it
adds. **What changed:** Mumbai's foot moves from Rs 7,14,890 to Rs 1,56,790, and the count beside it reads
11 of 50. On LibreOffice 24.2.7.2, SUM over three rows with one hidden by hand gave 60 and SUBTOTAL(109)
gave 40, the same rule.
'''),
        md('''
## A second route: does a total that ignores the filter altogether agree?

The second route must not depend on what is on screen, so it reads the whole list and picks Mumbai by
its city: `=SUMIFS(E2:E51, C2:C51, "Mumbai")` in Excel.
'''),
        code('''
sumifs_mumbai = int(protect.loc[protect["city"] == "Mumbai", "revenue"].sum())
kit.table(["Route", "Mumbai's total"], [("SUBTOTAL(109) under the filter", kit.rupees(foot(rev, mumbai_filter, no, "SUBTOTAL(109)"))),
                                       ("SUMIFS on the city, no filter", kit.rupees(sumifs_mumbai))])
kit.check("the visible total and the SUMIFS agree", sumifs_mumbai == foot(rev, mumbai_filter, no, "SUBTOTAL(109)"))
'''),
        md('''
## 4. Where does a director's assumption go, so the sheet recalculates honestly?

A director asks: "What would a Rs 500 voucher for every member on the list cost, city by city?" The
voucher is an assumption, so it goes in a yellow input cell, and the cost is a formula that reads it and
the count of rows on screen: `=B1*SUBTOTAL(103, A2:A51)`, with the voucher in B1.

**Predict before you run.** With the list filtered to Mumbai and the voucher at Rs 500, the cost reads: a)
Rs 25,000; b) Rs 5,500; c) Rs 500; d) Rs 7,14,890.
'''),
        code('''
def voucher_cost(voucher, on_screen_mask):
    """The cost formula: the yellow input times the rows a director can see."""
    return voucher * int(sum(on_screen_mask))


for v in [500, 750]:
    print(f"voucher {kit.rupees(v)}: Mumbai {kit.rupees(voucher_cost(v, visible))}, the whole list {kit.rupees(voucher_cost(v, [True] * 50))}")
kit.flow(["yellow input\\nvoucher Rs 500", "formula\\ninput x rows on screen", "the cost\\nRs 5,500 for Mumbai"],
         kinds=["known", "plain", "good"], title="An assumption the room can change, and the number that follows it")
kit.check("the cost follows the input", voucher_cost(750, visible) == 1.5 * voucher_cost(500, visible))
kit.check("the cost follows the filter", voucher_cost(500, visible) == 500 * 11)
'''),
        md('''
**What happened.** The answer is b: Rs 500 times the eleven on screen. The director changes B1 to Rs 750
and the cost becomes Rs 8,250 in front of the room; the list's figures never change, because the
assumption sits beside them and never over them. That is the chief of staff's condition met: the sheet
recalculates, and the source is untouched.
'''),
        md('''
## 5. Which checks does the Checks tab run, and what does its release hold?

The Checks tab turns every trap of the day into a line that reads PASS or HOLD, and one release sentence
reads all of them. Each check compares a number on the sheet with one that comes from somewhere else:

| Check | It compares | It catches |
|---|---|---|
| The tree ties | The tree's two quarters against the warehouse's | A pivot adding payment rows |
| The list's source ties | The customer table's orders and revenue against the warehouse's | A list built on an export that is short |
| The lookup is honest | The lookup's answer for an id known to be missing | An approximate match |
| The foot follows the filter | SUBTOTAL(103) against the rows the foot adds | SUM under a filter |
| No typed-over formula | ISFORMULA on every cell outside the yellow inputs | A director's figure typed over a formula |

The cell below runs the checks in two passes. The first runs the three that read Kalpa's tree, lookup
and foot. The second shows the release deciding, on **invented** inputs: five invented records that fall
short of an invented control total, and a two-cell sheet with one figure typed over its formula.
Chapter 3's your-turn cell runs the source comparison on the real customer table, and that answer is
yours.

**Predict before you run.** In the second pass the invented list's source is short, and the typed-over
sheet is clean. The release: a) ships everything, since four of five checks pass; b) holds the list and
ships the rest; c) holds everything; d) cannot decide.
'''),
        code('''
import openpyxl

once = raw.drop_duplicates("order_id")
wq = {r["quarter"]: r["revenue"] for r in warehouse("SELECT quarter, sum(amount) AS revenue FROM orders GROUP BY quarter")}


def find(member):
    hit = table.loc[table["customer_id"] == member, "revenue"]
    return int(hit.iloc[0]) if len(hit) else "not in the table"


kalpa = {"the tree ties": all(int(once.loc[once["quarter"] == q, "order_amount"].sum()) == wq[q] for q in ["Q1", "Q2"]),
         "the lookup is honest": isinstance(find("C-0195"), str),
         "the foot follows the filter": foot(rev, mumbai_filter, no, "SUBTOTAL(109)") == on_screen}
kit.table(["Check on Kalpa's workbook", "Result"], [(k, "PASS" if ok else "HOLD") for k, ok in kalpa.items()],
          caption="First pass: the three checks that read the tree, the lookup and the foot")


def typed_over(sheet, cells):
    """ISFORMULA, cell by cell: the cells outside the yellow inputs that hold a typed figure."""
    return [c for c in cells if not str(sheet[c].value).startswith("=")]


def release(checks):
    holds = {"the list's source ties": "protect list", "the lookup is honest": "protect list",
             "the foot follows the filter": "protect list", "the tree ties": "tree and card",
             "no typed-over formula": "whole workbook"}
    held = sorted({holds[k] for k, ok in checks.items() if not ok})
    if "whole workbook" in held:
        return "Hold the whole workbook until the typed figure is traced."
    return "Ship everything." if not held else f"Hold the {' and the '.join(held)}; ship the rest."


invented_table = [("X-01", 3000), ("X-02", 2500), ("X-03", 2200), ("X-04", 1800), ("X-05", 1500)]   # invented records
invented_control = 12200                                                                           # invented control total
clean_sheet = openpyxl.Workbook().active
clean_sheet["B2"], clean_sheet["B3"] = '=SUMIFS(F:F, C:C, "Retail-Plus", I:I, "Q1")', '=SUMIFS(F:F, C:C, "Retail-Plus", I:I, "Q2")'
edited_sheet = openpyxl.Workbook().active
edited_sheet["B2"], edited_sheet["B3"] = '=SUMIFS(F:F, C:C, "Retail-Plus", I:I, "Q1")', 500000   # a figure typed over B3's formula

second = dict(kalpa, **{"the list's source ties": sum(r for _, r in invented_table) == invented_control,
                        "no typed-over formula": not typed_over(clean_sheet, ["B2", "B3"])})
third = dict(kalpa, **{"the list's source ties": True, "no typed-over formula": not typed_over(edited_sheet, ["B2", "B3"])})
kit.table(["Inputs", "Checks passing", "The release"],
          [("Kalpa's three checks and the invented short source", f"{sum(second.values())} of 5", release(second)),
           ("Kalpa's three checks and a figure typed over B3", f"{sum(third.values())} of 5", release(third))],
          caption="Second pass: the release reads every check, on invented inputs")
kit.flow(["each check\\nPASS or HOLD", "each HOLD names\\nwhat it holds", "one release sentence"],
         kinds=["plain", "lit", "good"], title="The Checks tab: the release reads the checks and nothing else")
kit.check("Kalpa's tree, lookup and foot checks all pass", all(kalpa.values()))
kit.check("a short source holds the list and nothing else", release(second) == "Hold the protect list; ship the rest.")
kit.check("a typed-over formula holds the whole workbook", typed_over(edited_sheet, ["B2", "B3"]) == ["B3"])
'''),
        md('''
**What happened.** The answer is b. Kalpa's tree, lookup and foot pass. The invented source falls
Rs 1,200 short of its control total, so the list check reads HOLD and the release says: "Hold the
protect list; ship the rest." A figure typed over a formula holds the whole workbook, because nobody can
say which other numbers it has moved. A formula recalculating is never the same as the number being
right, which is why the release reads the checks and nothing else, and why the note that goes with a
HOLD names what does not tie and asks for the export to be rerun.
'''),
        md('''
> **Kavya's review.** "Give the room a sheet it can change and cannot break silently: inputs in yellow,
> every other cell a formula, SUBTOTAL at every foot, and a Checks tab whose release holds whatever does
> not tie. A director who filters, sorts or asks a what-if should see the right numbers move, and see
> a wrong one turn red before anyone reads it out."
'''),
        md('''
### In the interview: what do you give a stakeholder who wants to poke the numbers?

**[S] A stakeholder wants to poke the numbers themselves. What do you give them, and what do you never
give them?** A workbook on a reconciled export, with the inputs they may change in yellow, a lookup that
says "not in the table", a foot that follows the filter and a Checks tab that holds what does not tie. I
never give them the source to edit, a lookup that can answer with somebody else's row, or a number
without its period and base.

**[F] You filter a list and its total does not move. What is the foot doing?** Adding hidden rows: it is
a SUM. SUBTOTAL(109) adds only what is on screen, and SUBTOTAL(103) beside it counts those rows. Filtered
to Mumbai, the protect list's SUM said Rs 7,14,890 and SUBTOTAL(109) said Rs 1,56,790 for eleven members.

**[D] Two directors change assumptions in the room and the sheet recalculates differently for each.
What did you get right, and what do you fix?** Right: the assumptions are inputs and every number
recomputes from one source, so both answers are honest for their assumptions. Fix: each answer prints its
assumption and its scope beside the number, so down 1.6 percent for all segments and down 17.3 percent
without Business are never compared as one figure, and the scenario never replaces the actual.
'''),
        md('''
### Depth: can a protected sheet still let a director filter?

Excel's sheet protection has options that allow filtering and sorting on a protected sheet, so a team
can lock the formulas and leave the yellow inputs unlocked. It narrows what a director can break and
does not replace the checks: a locked sheet still shows a SUM under a filter, and it cannot tell anyone
that the export under it is short. Protection limits what a director can change; the Checks tab says
whether the numbers can be trusted.
'''),
        md('''
## What can a director break, and which checks catch it, question by question?

1. Option c: yellow inputs, every other cell a formula, and a Checks tab; locking or a PDF fails the brief.
2. A director filters, sorts, types over cells, changes inputs and pastes new exports; three of the five change a number's meaning with no error.
3. Filtered to Mumbai, SUM at the foot still reads Rs 7,14,890 while the eleven on screen spent Rs 1,56,790.
4. SUBTOTAL(109) reads Rs 1,56,790 and SUBTOTAL(103) counts 11 of 50; SUMIFS on the city agrees.
5. An assumption goes in a yellow input that formulas read: a Rs 500 voucher costs Rs 5,500 for Mumbai's eleven.
6. Five checks, each comparing the sheet with something outside it, and a release that holds what a failing check names.

The afternoon's escalated case builds all three deliverables and this Checks tab alone, from the two
exports.
'''),
        code("kit.check_summary()"),
    ]


# ============================================================================= the escalated case
EX1_STEPS = [
    ('''## Part 1. Does your tree for both quarters tie to the warehouse to the rupee?

**Where this is used at work:** every tree a director sees has to reproduce the number Finance owns,
before anyone slices it. The raw export has one row per payment, so the tree starts from one row per
order, then counts customers who ordered in each segment and quarter.''',
     '''# TODO 1. Which line leaves exactly one row per order?
#   a) orders = raw.drop_duplicates()
#   b) orders = raw.drop_duplicates("customer_id")
#   c) orders = raw.drop_duplicates("order_id")
#   d) orders = raw[raw["paid_amount"] > 0]
orders = __TODO1__

# TODO 2. How are customers counted in each segment and quarter?
#   a) ("customer_id", "count")
#   b) ("customer_id", "nunique")
#   c) ("order_id", "nunique")
#   d) ("customer_id", "size")
tree = orders.groupby(["segment", "quarter"]).agg(customers=__TODO2__,
                                                  orders=("order_id", "size"),
                                                  revenue=("order_amount", "sum"))
tree["orders_per_customer"] = tree["orders"] / tree["customers"]
tree["revenue_per_order"] = tree["revenue"] / tree["orders"]
kit.columns(SEGMENTS, [(q, [round(tree.loc[(s, q), "orders_per_customer"], 2) for s in SEGMENTS]) for q in ["Q1", "Q2"]],
            fmt=lambda v: f"{v:.2f}", title="Your orders per customer, Q1 against Q2")''',
     '''wq = {r["quarter"]: r for r in warehouse("SELECT quarter, count(*) AS n, sum(amount) AS revenue FROM orders GROUP BY quarter")}
yours = orders.groupby("quarter").agg(n=("order_id", "size"), revenue=("order_amount", "sum"))
kit.check("your quarters tie to the warehouse, orders and rupees", all(int(yours.loc[q, "n"]) == wq[q]["n"] and int(yours.loc[q, "revenue"]) == wq[q]["revenue"] for q in ["Q1", "Q2"]))
w_cust = {r["quarter"]: r["n"] for r in warehouse("SELECT o.quarter, count(DISTINCT o.customer_id) AS n FROM orders o JOIN customers c USING (customer_id) WHERE c.segment = 'Retail-Plus' GROUP BY o.quarter")}
kit.check("your Retail-Plus customer counts match the warehouse's", all(int(tree.loc[("Retail-Plus", q), "customers"]) == w_cust[q] for q in ["Q1", "Q2"]))''',
     {1: 'raw.drop_duplicates("order_id")', 2: '("customer_id", "nunique")'},
     "TODO 1: a keeps the 400 instalment orders twice, since their two rows differ in paid_amount; b keeps one order per customer; d drops the unpaid orders and keeps every repeat. TODO 2: a and d count rows, so a customer with three orders counts three times; c counts orders."),
    ('''## Part 2. Does your protect list hold the right fifty, and does your lookup say when an id is missing?

**Where this is used at work:** a list a manager acts on, and a lookup a director types into, are read
aloud in rooms where nobody can see the formula. The list comes from the customer table, one row per
customer who ordered, since that is the table the chief of staff refreshes.''',
     '''plus = table[table["segment"] == "Retail-Plus"]

# TODO 3. Which line gives the fifty Retail-Plus members with the highest revenue?
#   a) protect = table.nlargest(50, "revenue")
#   b) protect = plus.nsmallest(50, "revenue")
#   c) protect = plus.head(50)
#   d) protect = plus.nlargest(50, "revenue")
protect = __TODO3__

by_id = table.set_index("customer_id")
# TODO 4. Which lookup returns a member's revenue, or a sentence when the id is not in the table?
#   a) lookup = lambda m: by_id["revenue"].get(m, "not in the table")
#   b) lookup = lambda m: by_id["revenue"].iloc[by_id.index.searchsorted(m, "right") - 1]
#   c) lookup = lambda m: by_id["revenue"].iloc[0]
#   d) lookup = lambda m: by_id["revenue"].asof(m)
lookup = __TODO4__
kit.strip(protect["revenue"].tolist(), fmt=kit.rupees, title="Your list's fifty revenues")''',
     '''outside = plus[~plus["customer_id"].isin(protect["customer_id"])]
kit.check("your list is fifty Retail-Plus members, none below anyone left off",
          len(protect) == 50 and set(protect["segment"]) == {"Retail-Plus"} and protect["revenue"].min() >= outside["revenue"].max())
kit.check("your lookup finds a member who is in the table", lookup("C-0152") == int(table.loc[table["customer_id"] == "C-0152", "revenue"].sum()))
kit.check("your lookup returns no number for C-0195, who placed no orders", not isinstance(lookup("C-0195"), (int, float)))''',
     {3: 'plus.nlargest(50, "revenue")', 4: 'lambda m: by_id["revenue"].get(m, "not in the table")'},
     "TODO 3: a ranks every segment together, so 39 Business buyers take most of the places; b keeps the fifty lowest; c keeps the first fifty rows in id order, which is no ranking. TODO 4: b and d are approximate matches, each returning the member just below a missing id, which is VLOOKUP with its fourth argument left out; c returns the first member for every id."),
    ('''## Part 3. Does your front-page card carry its period, its comparison and its base, for any scope a director picks?

**Where this is used at work:** the front page is read in two minutes by people who read nothing else.
The card's scope (all segments, all except Business, Retail-Plus) is the input a director changes.''',
     '''seg_q = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")
SCOPES = {"All segments": SEGMENTS, "All except Business": ["Retail-Core", "Retail-Plus", "Student"], "Retail-Plus": ["Retail-Plus"]}
company_q2 = int(seg_q["Q2"].sum())


def card(scope):
    q1, q2 = int(seg_q.loc[SCOPES[scope], "Q1"].sum()), int(seg_q.loc[SCOPES[scope], "Q2"].sum())
    # TODO 5. Which is the change from Q1 to Q2?
    #   a) (q2 - q1) / q2 * 100
    #   b) (q1 - q2) / (q1 + q2) * 100
    #   c) q2 / q1 * 100
    #   d) (q2 - q1) / q1 * 100
    change = __TODO5__
    # TODO 6. Which share goes beside the number?
    #   a) q2 / company_q2 * 100
    #   b) q2 / (q1 + q2) * 100
    #   c) (q2 - q1) / company_q2 * 100
    #   d) q2 / q1 * 100
    share = __TODO6__
    return {"scope": scope, "Q1": q1, "Q2": q2, "change": change, "share": share}


kit.table(["Scope", "Q2", "Change on Q1", "Share of Q2 revenue"],
          [(s, money(card(s)["Q2"]), f"{card(s)['change']:+.1f}%", f"{card(s)['share']:.1f}%") for s in SCOPES])''',
     '''w = {r["quarter"]: r["revenue"] for r in warehouse("SELECT quarter, sum(amount) AS revenue FROM orders GROUP BY quarter")}
wp = {r["quarter"]: r["revenue"] for r in warehouse("SELECT o.quarter, sum(o.amount) AS revenue FROM orders o JOIN customers c USING (customer_id) WHERE c.segment = 'Retail-Plus' GROUP BY o.quarter")}
kit.check("your company change matches the warehouse's, measured on Q1", abs(card("All segments")["change"] - (w["Q2"] - w["Q1"]) / w["Q1"] * 100) < 1e-9)
kit.check("your Retail-Plus share matches its part of the warehouse's Q2", abs(card("Retail-Plus")["share"] - wp["Q2"] / w["Q2"] * 100) < 1e-9)''',
     {5: "(q2 - q1) / q1 * 100", 6: "q2 / company_q2 * 100"},
     "TODO 5: a divides by the current quarter, which reads Retail-Plus at 41.7 percent where it fell 29.4; b is a share of the two quarters together; c is a ratio of about 98 that a card would misprint as a percentage. TODO 6: b shares out the scope's own two quarters; c is the change's share, not the scope's; d is the ratio again."),
    ('''## Part 4. What ships on Monday, and what, if anything, is held?

**Where this is used at work:** a release note says what a stakeholder can rely on and what waits, and
why. The tree was tied in part 1. The protect list comes from a different export, which has to tie on
its own before the list ships.''',
     '''once = raw.drop_duplicates("order_id")
# TODO 7. Which comparison says whether the list's source table ties?
#   a) source_ties = len(table) == 300
#   b) source_ties = int(protect["revenue"].sum()) == int(plus.nlargest(50, "revenue")["revenue"].sum())
#   c) source_ties = (int(table["orders"].sum()), int(table["revenue"].sum())) == (len(once), int(once["order_amount"].sum()))
#   d) source_ties = int(table["revenue"].sum()) > int(seg_q["Q2"].sum())
source_ties = __TODO7__

checks = {"tree ties": all(int(yours.loc[q, "revenue"]) == wq[q]["revenue"] for q in ["Q1", "Q2"]),
          "source ties": source_ties,
          "lookup honest": not isinstance(lookup("C-0195"), (int, float))}
needs = {"tree": ["tree ties"], "front page": ["tree ties"], "protect list": ["source ties", "lookup honest"]}
# TODO 8. Which rule turns the checks into Monday's release?
#   a) release = {part: ("ship" if sum(checks.values()) >= 2 else "hold") for part in needs}
#   b) release = {part: ("ship" if all(checks[c] for c in needs[part]) else "hold") for part in needs}
#   c) release = {part: ("ship" if all(checks.values()) else "hold") for part in needs}
#   d) release = {part: "ship" for part in needs}  # every number here is a formula, so all of it recalculates
release = __TODO8__
print(release)''',
     '''expected = {}
for part, behind in needs.items():
    expected[part] = "hold" if any(not checks[c] for c in behind) else "ship"
kit.check("your release holds exactly the parts whose checks fail, and ships the rest", release == expected)
kit.check("your tree and your front page ship on your own checks", release["tree"] == release["front page"] == ("ship" if checks["tree ties"] else "hold"))''',
     {7: '(int(table["orders"].sum()), int(table["revenue"].sum())) == (len(once), int(once["order_amount"].sum()))',
      8: '{part: ("ship" if all(checks[c] for c in needs[part]) else "hold") for part in needs}'},
     "TODO 7: a counts rows against a number the table itself gave; b compares the list with itself; d compares a half-year with a quarter. TODO 8: a ships everything when most checks pass, whatever sits behind each part; c holds everything when one check fails; d confuses recalculating with being right."),
    ('''## Part 5. Do your numbers agree when reached a second way?

**Where this is used at work:** a number that matters is reached twice, by routes that could disagree.
Two second routes: the warehouse's own query for the quarters, and a count on the city for the total
a filtered list shows.''',
     '''visible = protect["city"] == "Mumbai"
# TODO 9. Which total is what SUBTOTAL(109) shows at the foot of the list filtered to Mumbai?
#   a) foot = int(protect["revenue"].sum())
#   b) foot = int(protect.loc[visible, "revenue"].sum())
#   c) foot = int(protect.loc[~visible, "revenue"].sum())
#   d) foot = int(table.loc[table["city"] == "Mumbai", "revenue"].sum())
foot = __TODO9__

# TODO 10. Which query is the warehouse's own route to the two quarters of booked revenue?
#   a) "SELECT quarter, sum(amount) AS revenue FROM orders GROUP BY quarter"
#   b) "SELECT o.quarter, sum(p.amount) AS revenue FROM payments p JOIN orders o USING (order_id) GROUP BY o.quarter"
#   c) "SELECT quarter, count(*) AS revenue FROM orders GROUP BY quarter"
#   d) "SELECT quarter, sum(amount) AS revenue FROM orders WHERE status = 'delivered' GROUP BY quarter"
query = __TODO10__
second = {r["quarter"]: int(r["revenue"]) for r in warehouse(query)}
kit.table(["Quarter", "Your tree", "The query you picked"], [(q, kit.rupees(int(yours.loc[q, "revenue"])), kit.rupees(second[q])) for q in ["Q1", "Q2"]])
kit.columns(["Q1", "Q2"], [("your tree", [int(yours.loc[q, "revenue"]) for q in ["Q1", "Q2"]]), ("the query you picked", [second[q] for q in ["Q1", "Q2"]])],
            fmt=money, title="Your tree against the warehouse's own route")''',
     '''by_loop = sum(r for c, r in zip(protect["city"], protect["revenue"]) if c == "Mumbai")
kit.check("your foot equals a SUMIFS on the city, which ignores the filter", foot == by_loop)
kit.check("the query you picked agrees with your tree, both quarters", all(second[q] == int(yours.loc[q, "revenue"]) for q in ["Q1", "Q2"]))''',
     {9: 'int(protect.loc[visible, "revenue"].sum())', 10: '"SELECT quarter, sum(amount) AS revenue FROM orders GROUP BY quarter"'},
     "TODO 9: a is SUM, which adds the rows the filter hid; c adds exactly the hidden rows; d adds every Mumbai customer in every segment. TODO 10: b is collected money, which differs from booked; c counts orders; d leaves out returned and cancelled orders, which booked revenue counts."),
]
EX1_KEY = "cbdadacbba"


# ============================================================================= the second case
EX2_STEPS = [
    ('''## Step 1. What does the card show after the director's figure goes into the cell?

**Where this is used at work:** a sheet recalculates from whatever sits in its cells, so a typed figure
moves every number that reads it. The director types Rs 5,00,000 over Retail-Plus's Q2 cell.''',
     '''sheet = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")
export_q1, export_q2 = int(sheet.loc["Retail-Plus", "Q1"]), int(sheet.loc["Retail-Plus", "Q2"])
typed_q2 = 500000
edited = sheet.copy()
edited.loc["Retail-Plus", "Q2"] = typed_q2
# TODO 1. Which line is the card the room now sees for Retail-Plus?
#   a) shown = change(export_q1, typed_q2)
#   b) shown = change(export_q1, export_q2)
#   c) shown = change(typed_q2, export_q2)
#   d) shown = typed_q2 / export_q2 * 100
shown = __TODO1__
kit.bars([("from the export", round(-change(export_q1, export_q2), 1)), ("after the typed figure", round(-shown, 1))],
         fmt=lambda v: f"down {v:.1f}%", title="Retail-Plus, Q2 on Q1, before and after the edit")''',
     '''kit.check("the card you computed moved when the cell changed", shown != change(export_q1, export_q2))
kit.check("the card you computed reads the typed figure", abs(shown - (typed_q2 - export_q1) / export_q1 * 100) < 1e-9)''',
     {1: "change(export_q1, typed_q2)"},
     "b is the card before the edit; the sheet reads the cell, not the export. c measures the typed figure against the export's Q2. d is a ratio of the two Q2 figures, which no card prints."),
    ('''## Step 2. Which comparison catches the edit?

**Where this is used at work:** a drift check compares the sheet with the source of truth on every
refresh. It must stay quiet on a clean sheet and fire on an edited one.''',
     '''wq = {r["quarter"]: r["revenue"] for r in warehouse("SELECT quarter, sum(amount) AS revenue FROM orders GROUP BY quarter")}
# TODO 2. Which comparison catches a figure typed into the sheet?
#   a) drift = lambda s: len(s) - 4
#   b) drift = lambda s: int(s["Q1"].sum()) - wq["Q1"]
#   c) drift = lambda s: int(s["Q2"].sum()) - wq["Q2"]
#   d) drift = lambda s: 0 if s is sheet else 1
drift = __TODO2__
kit.bridge(("the warehouse, Q2", wq["Q2"]), [("the typed figure", int(drift(edited)))],
           end_label="the sheet, Q2", fmt=kit.rupees, lo=97_000_000,
           title="The drift, in rupees; the axis starts at Rs 9.70 crore")''',
     '''kit.check("your check stays quiet on the sheet as exported", drift(sheet) == 0)
kit.check("your check fires on the edited sheet", drift(edited) != 0, kit.rupees(int(drift(edited))))''',
     {2: 'lambda s: int(s["Q2"].sum()) - wq["Q2"]'},
     "a counts segments, which an edit never changes; b looks at the quarter nobody touched; d compares the sheet with itself by name, so it fires on any copy and catches nothing about the numbers."),
    ('''## Step 3. Which cells does the typed-over check flag?

**Where this is used at work:** ISFORMULA tells a cell holding a formula from a cell holding a typed
figure. Outside the yellow inputs, every cell should hold a formula. The sheet below is a two-cell
model of the tree's Retail-Plus row.''',
     '''import openpyxl
clean_ws = openpyxl.Workbook().active
clean_ws["B2"], clean_ws["B3"] = '=SUMIFS(F:F, C:C, "Retail-Plus", I:I, "Q1")', '=SUMIFS(F:F, C:C, "Retail-Plus", I:I, "Q2")'
edited_ws = openpyxl.Workbook().active
edited_ws["B2"], edited_ws["B3"] = '=SUMIFS(F:F, C:C, "Retail-Plus", I:I, "Q1")', typed_q2
cells, inputs = ["B2", "B3"], set()          # the yellow inputs on this sheet: none
# TODO 3. Which rule flags a figure typed over a formula?
#   a) flagged = lambda ws: [c for c in cells if isinstance(ws[c].value, (int, float))]
#   b) flagged = lambda ws: [c for c in cells if c not in inputs and not str(ws[c].value).startswith("=")]
#   c) flagged = lambda ws: [c for c in cells if ws[c].value != clean_ws[c].value]
#   d) flagged = lambda ws: [c for c in cells if c in inputs]
flagged = __TODO3__
kit.table(["Cell", "Clean sheet", "Edited sheet"], [(c, str(clean_ws[c].value), str(edited_ws[c].value)) for c in cells],
          caption="The two-cell model of the tree's Retail-Plus row")''',
     '''kit.check("your rule flags nothing on the clean sheet", flagged(clean_ws) == [])
kit.check("your rule flags the one cell typed over", len(flagged(edited_ws)) == 1 and flagged(edited_ws)[0] in cells)''',
     {3: 'lambda ws: [c for c in cells if c not in inputs and not str(ws[c].value).startswith("=")]'},
     "a flags numbers, and would flag every yellow input too; c compares with one saved copy, so it breaks after any honest change; d flags the inputs, which are the cells a director is allowed to change."),
    ('''## Step 4. What does Monday's refresh do to the typed figure?

**Where this is used at work:** a refresh rebuilds the sheet from a fresh export. Whatever was typed
over is gone, and so is any record of why.''',
     '''# TODO 4. Which line is Monday's refresh?
#   a) refreshed = edited.copy()
#   b) refreshed = edited.fillna(0)
#   c) refreshed = sheet.where(edited == sheet, edited)
#   d) refreshed = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")
refreshed = __TODO4__
kit.bars([("after the edit", int(edited.loc["Retail-Plus", "Q2"])), ("after the refresh", int(refreshed.loc["Retail-Plus", "Q2"]))],
         fmt=kit.rupees, title="Retail-Plus Q2: the refresh restores the export and loses the edit")''',
     '''kit.check("your refreshed sheet ties to the warehouse again", drift(refreshed) == 0)
kit.check("the typed figure left no trace after your refresh", int(refreshed.loc["Retail-Plus", "Q2"]) != typed_q2)''',
     {4: 'orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")'},
     "a and b keep the typed figure, which is the drift the rule exists to stop; c keeps the edited value wherever the two differ, which is exactly the typed cell."),
    ('''## Step 5. Where does the director's assumption go?

**Where this is used at work:** the director's question is fair: what would the card say if
Retail-Plus came back to Rs 5,00,000? It goes in a yellow input beside the actual, never over it, and
the card shows both lines, each labelled.''',
     '''scenario_input = 500000                       # the yellow input cell
# TODO 5. Which card answers the director and keeps the number Finance signs?
#   a) card = {"actual": change(export_q1, export_q2), "director's scenario": change(export_q1, scenario_input)}
#   b) card = {"actual": change(export_q1, scenario_input)}
#   c) card = {"actual": change(export_q1, export_q2)}
#   d) card = {"actual": change(export_q1, scenario_input), "director's scenario": change(export_q1, export_q2)}
card = __TODO5__
kit.table(["Line on the card", "Retail-Plus, Q2 on Q1"], [(k, f"{v:+.1f}%") for k, v in card.items()])''',
     '''wp = {r["quarter"]: r["revenue"] for r in warehouse("SELECT o.quarter, sum(o.amount) AS revenue FROM orders o JOIN customers c USING (customer_id) WHERE c.segment = 'Retail-Plus' GROUP BY o.quarter")}
kit.check("your actual line is the warehouse's change", abs(card["actual"] - (wp["Q2"] - wp["Q1"]) / wp["Q1"] * 100) < 1e-9)
kit.check("your card carries a second, labelled line for the director", len(card) == 2 and "actual" in card)''',
     {5: '{"actual": change(export_q1, export_q2), "director\'s scenario": change(export_q1, scenario_input)}'},
     "b puts the director's figure where the actual belongs, which is the edit again under a new name; c refuses a fair question and sends the director back to typing over cells; d swaps the labels, so the page calls the scenario actual."),
]
EX2_KEY = "acbda"


def case_cells(steps, solution):
    cells = []
    for text, body, check, fill, why in steps:
        cells.append(md(text))
        src = body
        if solution:
            for k, v in fill.items():
                src = src.replace(f"__TODO{k}__", v)
        cells.append(code(src))
        cells.append(code(check))
        if solution:
            cells.append(md(f"**Why the other letters fail.** {why}"))
    return cells


def ex1(solution):
    head = md(f'''
# The escalated case: can Monday's deck pack be trusted, part by part?

**Week 2, Friday. The escalated case, alone.**

> **The client asks.** "Build me the file I open on Monday: the tree by segment for both quarters, the
> protect list with the lookup, and the front-page number with its trend. I will change things in the
> room. Tell me what I can trust it for."
>
> Meera's chief of staff, Kalpa Retail

**Who needs the answer.** The chief of staff opens this file in front of Meera and her directors on
Monday. A number that does not tie, a lookup that answers with a neighbour, or a card without its
period goes into the meeting's decisions, and the release note is what tells the chief of staff which
parts to rely on.

**The questions on the way.** Five parts, each a question: does the tree tie; does the list hold the
right fifty and does the lookup say when an id is missing; does the card carry its period, comparison
and base; what ships and what, if anything, is held; do the numbers agree a second way.

**What you have.** Two exports in `../data/`: the customer table, one row per customer who ordered
between April and September 2026 with that customer's orders and revenue summed, and the raw export,
one row per payment with the order's amount repeated on each. The warehouse, which Monday's queries
read, holds one row per order and is the source of truth. Kalpa's Q1 is April to June 2026 and Q2 is
July to September 2026. Revenue is booked order value in rupees. C-0195 is a Retail-Plus member who
placed no orders in the two quarters.

**How it works.** Ten lettered `TODO` markers across five parts. Replace each `__TODOn__` with the line
of the letter you pick; the checks after each part test what your lines computed.
{"This is the executed solution." if solution else "Run it from the top: it stops at the first placeholder with a NameError until you fill it in, which is intended."}
''')
    setup_cell = setup(HELPERS, LOAD_TABLE, LOAD_RAW, WAREHOUSE,
                       last='print(len(table), "customer rows and", f"{len(raw):,}", "export rows loaded")')
    close = md(f'''
## What do you post, and what can the chief of staff trust?

Post your ten letters in order as one line, then two sentences to the chief of staff: what Monday's
file can be relied on for, and anything held, with its reason.{" The key is `" + EX1_KEY + "`." if solution else ""}
''')
    route = code('''
kit.vflow(["1. does the tree tie to the warehouse", "2. the right fifty, and an honest lookup",
           "3. a card with its period, comparison and base", "4. what ships on Monday",
           "5. the same numbers a second way"], title="The five parts of Monday's file")''')
    return [head, setup_cell, route] + case_cells(EX1_STEPS, solution) + [close, code("kit.check_summary()")]


def ex2(solution):
    head = md(f'''
# The second case: can the sheet show the director's number and still be the one Finance signs?

**Week 2, Friday. The second case, in pairs.**

> **The director says.** "Retail-Plus will be back at five lakh next quarter; I have spoken to the team.
> Type five lakh into Q2 so the card stops frightening people, and fix the source later."
>
> A director of Kalpa Retail, in the room, with the sheet on the projector

**Who needs the answer.** The director wants a number to discuss; the chief of staff needs a card that
still matches Finance's books after the meeting; Anand's analyst will compare the deck with the
warehouse next week. A figure typed over the source gives the room a fall that Finance's books do not
show, and the next refresh wipes the figure and its reason.

**The questions on the way.** What the card shows after the edit; which comparison catches it; which
cells the typed-over check flags; what Monday's refresh does to the figure; and where the director's
assumption belongs.

**What you have.** The raw export in `../data/`, one row per payment with the order's amount repeated
on each; counted once per order it ties to the warehouse, Rs 10,00,00,000 in Q1 (April to June 2026) and
Rs 9,84,00,000 in Q2 (July to September 2026). Retail-Plus, Kalpa's paid membership tier, booked
Rs 5,85,770 in Q1 and Rs 4,13,380 in Q2, down 29.4 percent.

**How it works.** Five lettered `TODO` markers. Replace each `__TODOn__` with the line of the letter you
pick; the checks after each step test what your lines computed.
{"This is the executed solution." if solution else "Run it from the top: it stops at the first placeholder with a NameError until you fill it in, which is intended."}
''')
    setup_cell = setup(HELPERS, LOAD_RAW, WAREHOUSE, COUNT_ONCE,
                       last='print(f"{len(orders):,} orders, each counted once, from {len(raw):,} export rows")')
    close = md(f'''
## What do you say to the director, in three lines?

Post your five letters in order as one line, then the three lines one partner says to the director:
yes to the question, no to the edit, and the check that keeps the sheet honest.{" The key is `" + EX2_KEY + "`." if solution else ""}
''')
    route = code('''
kit.flow(["the director's figure", "the card moves", "the drift check fires", "the refresh wipes it", "a labelled scenario"],
         kinds=["bad", "bad", "good", "plain", "good"], title="The scene, step by step")''')
    return [head, setup_cell, route] + case_cells(EX2_STEPS, solution) + [close, code("kit.check_summary()")]


BUILDERS = {"c1": ("C2_W02_D05_01_segment_tree_STUDENT.ipynb", ch1),
            "c2": ("C2_W02_D05_02_both_quarters_STUDENT.ipynb", ch2),
            "c3": ("C2_W02_D05_03_member_lookup_STUDENT.ipynb", ch3),
            "c4": ("C2_W02_D05_04_front_page_STUDENT.ipynb", ch4),
            "c5": ("C2_W02_D05_05_operating_rule_STUDENT.ipynb", ch5),
            "c6": ("C2_W02_D05_06_director_proof_STUDENT.ipynb", ch6)}


CASES = {"ex1": ("C2_W02_D05_ex1_escalated_case", ex1), "ex2": ("C2_W02_D05_ex2_second_case", ex2)}


def main(names):
    for key in names or list(BUILDERS) + list(CASES):
        if key in BUILDERS:
            name, fn = BUILDERS[key]
            build(NB / name, fn())
            print("built", NB / name)
        else:
            stem, fn = CASES[key]
            build(NB / f"{stem}_STUDENT.ipynb", fn(False), execute=False)
            build(SOL / f"{stem}_solution_STUDENT.ipynb", fn(True))
            print("built", stem, "twin and solution")


if __name__ == "__main__":
    main(sys.argv[1:])

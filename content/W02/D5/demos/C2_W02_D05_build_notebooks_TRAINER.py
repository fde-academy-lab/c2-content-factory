"""Build and execute Friday's notebooks: three rounds, the escalated case and the second case.

Run from the repository root:  python3 content/W02/D5/demos/C2_W02_D05_build_notebooks_TRAINER.py

Each notebook is assembled by scripts/nb_make.py and executed cold in its own folder, so the saved
outputs are what a learner's Run All produces. The case notebooks are written twice: the TODO twin
in notebooks/, which stops at its first placeholder on purpose, and the executed solution twin in
exercises/solutions/. Excel is the tool the room holds; pandas here is the second way to reach the
same number, which is Kavya's review, and every level names the Excel move beside the code.

No learner file names the member the clean table is missing. Round 1 leaves the reconciliation to
an empty your-turn cell, and round 2 teaches the approximate-match trap on C-0195, a Retail-Plus
member with no orders in the two quarters, whose neighbour C-0194 sits at rank 15 of the list.
"""
import pathlib
import sys

sys.path.insert(0, "scripts")
from nb_make import SETUP, build, code, empty, md  # noqa: E402

DAY = pathlib.Path("content/W02/D5")
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"

LOAD = SETUP + '''import pandas as pd

clean = pd.read_csv(kit.data_dir() / "C2_W02_D05_customer_table_STUDENT.csv")
raw = pd.read_csv(kit.data_dir() / "C2_W02_D05_raw_export_STUDENT.csv")
WAREHOUSE = {"Q1": 100_000_000, "Q2": 98_400_000}   # Monday's warehouse totals, from Week 2 Monday
SEGMENTS = ["Business", "Retail-Core", "Retail-Plus", "Student"]


def crore(n):
    return f"Rs {n / 1e7:.2f} crore"


def lakh(n):
    return f"Rs {n / 1e5:.2f} lakh"


def money(n):
    """Crore, lakh or rupees, whichever reads the size of the number, with the sign in front."""
    sign, a = ("-" if n < 0 else ""), abs(n)
    return sign + (crore(a) if a >= 1e7 else lakh(a) if a >= 1e5 else kit.rupees(round(a)))


print(len(clean), "customer rows and", len(raw), "export rows loaded")
'''

LADDER = ["The pivot", "The lookup", "The front page", "Case: the three deliverables", "Case: the operating rule"]


def ladder(lit, steps):
    return code(f'''
kit.side_by_side(
    kit.ladder({LADDER!r}, lit={lit}, show=False),
    kit.vflow({steps!r}, show=False),
)''')


# =========================================================================== round 1
round1 = [
    md('''
# The pivot a director slices live

**Week 2, Friday. Round 1 of 3.** By the end of this notebook you can build the revenue tree by
segment as a pivot, say why the same pivot on the raw export shows nearly twice the revenue, prove
it with one count, and rebuild it so it reconciles to the warehouse to the rupee.

> **The client asks.** "Monday's growth review deck needs three things I can open on my laptop
> without a login: the revenue tree by segment for both quarters, the top-fifty protect list with a
> lookup so I can find any member by id, and one number on the front page with its trend."
>
> Meera's chief of staff, Kalpa Retail

> **Kavya's review.** "A pivot is only as honest as the rows under it. Before it reaches a director,
> its grand total matches Monday's warehouse number, or it does not leave the team."

Thursday ended on the customer table, one row per customer, exported as a CSV. This round opens that
table the way Excel does, pivots it, and then meets the other export the data team sent: the raw
one, one row per payment.'''),
    md('''
**Setup.** The helper, pandas, the two exports from `../data/`, and Monday's warehouse totals, which
are the control every number in this notebook is reconciled against. In Excel the same two files open
from the Codespace's file panel; nothing here is typed in.'''),
    code(LOAD),
    ladder(0, ["the clean table, pivoted by segment", "the tree per segment",
               "the question the clean table cannot answer", "the trap: the same pivot on the raw export",
               "the fix: one row per order"]),
    md('''
## 1. The clean table, pivoted by segment

The customer table has one row per customer, so a pivot with segment in Rows and revenue in Values
adds each customer once. In Excel: select the table, **Insert, PivotTable**, drag `segment` to Rows,
`revenue` to Values as Sum, `customer_id` to Values as Count, and `orders` as Sum.

**Predict before you run.** Which segment carries most of the revenue? a) Retail-Plus, the paid
tier; b) Retail-Core, the largest by customers; c) Business, the corporate buyers; d) no segment
carries more than a third.'''),
    code('''
pivot = clean.pivot_table(index="segment", values=["customer_id", "orders", "revenue"],
                          aggfunc={"customer_id": "count", "orders": "sum", "revenue": "sum"})
pivot = pivot.rename(columns={"customer_id": "customers"})
kit.table(["Segment", "Customers", "Orders", "Revenue"],
          [(s, int(r.customers), int(r.orders), kit.rupees(r.revenue)) for s, r in pivot.iterrows()],
          caption="The clean customer table, pivoted by segment, both quarters together")
kit.bars([(s, int(r.revenue)) for s, r in pivot.sort_values("revenue", ascending=False).iterrows()],
         fmt=kit.rupees, title="Revenue by segment: Business carries almost all of it")'''),
    md('''
**What happened.** The answer is c. Business, 39 corporate buyers, carries about 99 percent of the
revenue, which is why a pivot's grand total is a Business number and why a consumer segment's
movement is invisible in it. Keep that in mind for the front page in round 3.'''),
    code('''
kit.check("the pivot holds one row per segment", len(pivot) == 4, f"{len(pivot)} rows")
kit.check("every customer is counted once", int(pivot.customers.sum()) == clean.customer_id.nunique(),
          f"{int(pivot.customers.sum())} customers")
kit.check("Business carries more than 95 percent of the revenue",
          pivot.revenue["Business"] / pivot.revenue.sum() > 0.95,
          f"{pivot.revenue['Business'] / pivot.revenue.sum():.1%}")'''),
    md('''
## 2. The tree, one segment at a time

The pivot gives the leaves of Week 1's tree per segment: customers, orders per customer and revenue
per order, which multiply back to revenue. In Excel these are two calculated columns beside the
pivot, `=orders/customers` and `=revenue/orders`, or a calculated field.

**Predict before you run.** Retail-Plus members buy bigger baskets than Retail-Core. Which leaf
explains most of the gap between the two segments' revenue per customer? a) customers; b) orders per
customer; c) revenue per order; d) the two segments are equal per customer.'''),
    code('''
tree = pivot.assign(orders_per_customer=pivot.orders / pivot.customers,
                    revenue_per_order=pivot.revenue / pivot.orders)
tree["revenue_per_customer"] = tree.revenue / tree.customers
kit.table(["Segment", "Customers", "Orders per customer", "Revenue per order", "Revenue per customer"],
          [(s, int(r.customers), f"{r.orders_per_customer:.2f}", kit.rupees(round(r.revenue_per_order)),
            kit.rupees(round(r.revenue_per_customer))) for s, r in tree.iterrows()],
          caption="The leaves per segment, both quarters together")
consumer = ["Retail-Core", "Retail-Plus", "Student"]
kit.columns(consumer, [("orders per customer", [round(tree.orders_per_customer[s], 2) for s in consumer])],
            fmt=lambda v: f"{v:.2f}", title="Orders per customer, the consumer segments")
kit.columns(consumer, [("revenue per order", [round(tree.revenue_per_order[s]) for s in consumer])],
            fmt=kit.rupees, title="Revenue per order, the consumer segments")'''),
    md('''
**What happened.** The answer is c. Retail-Plus orders a little more often than Retail-Core (3.29
against 2.99) and pays about half as much again per order (Rs 2,801 against Rs 1,886), so the basket
does most of the work. The tree multiplies, so the check below multiplies it back.'''),
    code('''
plus = tree.loc["Retail-Plus"]
kit.driver_tree({"label": "Retail-Plus revenue", "note": kit.rupees(plus.revenue), "children": [
    {"label": "customers", "note": f"{int(plus.customers)}"},
    {"label": "orders per customer", "note": f"{plus.orders_per_customer:.2f}"},
    {"label": "revenue per order", "note": kit.rupees(round(plus.revenue_per_order))}]},
    title="The tree for Retail-Plus: three leaves multiply to the revenue")
rebuilt = plus.customers * plus.orders_per_customer * plus.revenue_per_order
kit.check("the three leaves multiply back to the revenue", abs(rebuilt - plus.revenue) < 1,
          f"{kit.rupees(round(rebuilt))} against {kit.rupees(plus.revenue)}")
kit.check("Retail-Plus pays more per order than Retail-Core",
          tree.revenue_per_order["Retail-Plus"] > tree.revenue_per_order["Retail-Core"])'''),
    md('''
## 3. The question the clean table cannot answer

The chief of staff asked for the tree **for both quarters**. The customer table has a
`last_order_date` and a `revenue` summed across April to September, and no column that splits a
customer's revenue by quarter.

**Predict before you run.** Can the clean table give Q1 against Q2 by segment? a) yes, split on
`last_order_date`; b) yes, halve each customer's revenue; c) no, the split lives only at the order
grain; d) yes, since `orders` counts per quarter.'''),
    code('''
print(list(clean.columns))
months = pd.to_datetime(clean.last_order_date).dt.month
kit.columns(["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
            [("customers whose last order fell in the month", [int((months == m).sum()) for m in range(4, 10)])],
            title="Last order dates: a recency, never a quarter split")'''),
    md('''
**What happened.** The answer is c. `last_order_date` says when a customer last bought, so splitting
on it would move a customer's whole two-quarter revenue into Q2 the moment they bought once in
September. Most customers last bought in Q2, so that split would invent a Q2 boom. The quarter split
needs the order grain, which only the raw export carries.'''),
    code('''
kit.check("the clean table carries no quarter column", "quarter" not in clean.columns and "order_date" not in clean.columns)
kit.check("most customers last bought in Q2, so a split on it would inflate Q2", (months >= 7).mean() > 0.5,
          f"{(months >= 7).mean():.0%} of customers")'''),
    md('''
## 4. The trap: the same pivot on the raw export

The raw export has an `order_date`, so the quarter split looks one drag away. Build the pivot the way
a hurried analyst does: quarter in Columns, segment in Rows, `order_amount` as Sum.

**The plausible wrong answer.**'''),
    code('''
raw["quarter"] = pd.to_datetime(raw.order_date).dt.month.map(lambda m: "Q1" if m <= 6 else "Q2")
hurried = raw.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")
kit.table(["Segment", "Q1", "Q2", "Change"],
          [(s, kit.rupees(r.Q1), kit.rupees(r.Q2), f"{(r.Q2 - r.Q1) / r.Q1:+.1%}") for s, r in hurried.iterrows()]
          + [("All segments", kit.rupees(hurried.Q1.sum()), kit.rupees(hurried.Q2.sum()),
              f"{(hurried.Q2.sum() - hurried.Q1.sum()) / hurried.Q1.sum():+.1%}")],
          caption="The hurried pivot on the raw export: Sum of order_amount")
kit.stats([(crore(hurried.Q1.sum()), "Q1, as the pivot shows it", "the warehouse says Rs 10.00 crore"),
           (crore(hurried.Q2.sum()), "Q2, as the pivot shows it", "the warehouse says Rs 9.84 crore"),
           (f"{(hurried.Q2['Retail-Core'] - hurried.Q1['Retail-Core']) / hurried.Q1['Retail-Core']:+.1%}",
            "Retail-Core, Q1 to Q2", "the pivot says it grew")])'''),
    md('''
**Why it is wrong.** The export holds one row per **payment**, and `order_amount` repeats on every
row of an order. An order paid in two instalments appears twice, and so does an order the gateway
posted twice, so the pivot adds each of those orders two times. In business terms: the deck would
put Rs 19.47 crore on Q2, nearly twice what Finance booked, and it would say Retail-Core grew 1.0
percent when it fell. A growth plan built on that leaves Core alone. The check is one count: rows
against distinct order ids, then the grand total against the warehouse.'''),
    code('''
rows, orders = len(raw), raw.order_id.nunique()
kit.stats([(f"{rows:,}", "rows in the export", "one per payment"),
           (f"{orders:,}", "distinct orders", "what the warehouse holds"),
           (f"{rows / orders:.2f}", "rows per order", "anything above 1.00 inflates a Sum")])
per = raw.groupby("order_id").size()
kit.bars([("orders with one row", int((per == 1).sum())), ("orders with two rows", int((per == 2).sum()))],
         title="How many rows each order occupies in the raw export")
kit.check("the export carries more rows than orders", rows > orders, f"{rows} rows, {orders} orders")
kit.check("the hurried pivot does not reconcile to the warehouse",
          abs(hurried.values.sum() - sum(WAREHOUSE.values())) > 1,
          f"{crore(hurried.values.sum())} against {crore(sum(WAREHOUSE.values()))}")'''),
    md('''
**Excel's Remove Duplicates is not the fix.** The first instinct is **Data, Remove Duplicates** on
every column. Predict before you run: after it, what does the grand total read? a) Rs 19.84 crore,
the warehouse; b) still about Rs 39.4 crore; c) about half the warehouse; d) the tool refuses a file
with repeated ids.'''),
    code('''
deduped = raw.drop_duplicates()
kit.table(["Version of the export", "Rows", "Grand total"],
          [("as exported", len(raw), crore(raw.order_amount.sum())),
           ("after Remove Duplicates on every column", len(deduped), crore(deduped.order_amount.sum())),
           ("the warehouse", orders, crore(sum(WAREHOUSE.values())))],
          caption="Removing exact copies clears only the rows that are identical in every column")
kit.check("Remove Duplicates leaves more rows than orders", len(deduped) > orders, f"{len(deduped)} rows")'''),
    md('''
**What happened.** The answer is b. Remove Duplicates took out 50 rows, the copies identical in every
column, and left 1,400 rows, because an instalment's two rows differ in `paid_amount` and are not
duplicates. The total barely moved. The grain is the problem, and the fix names the grain.

**The fix.** Count each order once. In Excel, a helper column in the export,
`=IF(COUNTIF($A$2:A2,A2)=1,1,0)`, flags the first row of each order; the pivot then filters on it, or
a `SUMIFS` over it builds the tree. In pandas it is one line.'''),
    code('''
orders_once = raw.drop_duplicates("order_id")
fixed = orders_once.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")
copies = int(raw.order_amount.sum() - deduped.order_amount.sum())
second_rows = int(raw.order_amount.sum() - orders_once.order_amount.sum()) - copies
kit.bridge(("the warehouse, both quarters", sum(WAREHOUSE.values())),
           [("second rows of instalment orders", second_rows),
            ("exact copies of the same row", copies)],
           end_label="the hurried pivot", fmt=money,
           title="From the warehouse to the hurried pivot: every extra rupee is a repeated row")
kit.check("the fixed pivot reconciles to the warehouse to the rupee",
          int(fixed.values.sum()) == sum(WAREHOUSE.values()), crore(fixed.values.sum()))
kit.check("Q2 lands on Monday's number", int(fixed.Q2.sum()) == WAREHOUSE["Q2"], crore(fixed.Q2.sum()))'''),
    md('''
**What changed.** The grand total falls from Rs 39.41 crore to Rs 19.84 crore, which is the
warehouse to the rupee, and Retail-Core turns from a 1.0 percent rise into a 1.8 percent fall. Every
segment moves, since instalment orders sit in every segment. Now the tree per quarter can be read.'''),
    code('''
q = orders_once.groupby(["segment", "quarter"]).agg(customers=("customer_id", "nunique"),
                                                   orders=("order_id", "size"),
                                                   revenue=("order_amount", "sum"))
q["orders_per_customer"] = q.orders / q.customers
q["revenue_per_order"] = q.revenue / q.orders
kit.table(["Segment", "Quarter", "Customers", "Orders per customer", "Revenue per order", "Revenue"],
          [(s, qq, int(r.customers), f"{r.orders_per_customer:.2f}", kit.rupees(round(r.revenue_per_order)),
            kit.rupees(r.revenue)) for (s, qq), r in q.iterrows()],
          caption="The tree by segment and quarter, each order counted once")
kit.columns(consumer, [("Q1", [round(q.loc[(s, "Q1"), "orders_per_customer"], 2) for s in consumer]),
                       ("Q2", [round(q.loc[(s, "Q2"), "orders_per_customer"], 2) for s in consumer])],
            fmt=lambda v: f"{v:.2f}", lit=[1], title="Orders per customer, Q1 against Q2")
kit.columns(consumer, [("hurried pivot", [int(hurried.Q2[s]) for s in consumer]),
                       ("each order once", [int(fixed.Q2[s]) for s in consumer])],
            fmt=kit.rupees, title="Q2 revenue in the consumer segments, hurried against fixed")'''),
    code('''
kit.check("Retail-Core falls once each order is counted once", fixed.Q2["Retail-Core"] < fixed.Q1["Retail-Core"],
          f"{kit.rupees(fixed.Q1['Retail-Core'])} to {kit.rupees(fixed.Q2['Retail-Core'])}")
kit.check("Retail-Plus orders per customer fall from Q1 to Q2",
          q.loc[("Retail-Plus", "Q2"), "orders_per_customer"] < q.loc[("Retail-Plus", "Q1"), "orders_per_customer"],
          f"{q.loc[('Retail-Plus', 'Q1'), 'orders_per_customer']:.2f} to {q.loc[('Retail-Plus', 'Q2'), 'orders_per_customer']:.2f}")'''),
    md('''
**Your turn: reconcile the clean table too.** The tree now reconciles, and the protect list in round
2 will come from the clean customer table, so that table has to reconcile as well. Type these lines
into the empty cell below, run them, and say in one sentence what you find and what it means for the
list:

```python
print(clean.revenue.sum(), sum(WAREHOUSE.values()))
print(clean.orders.sum(), orders)
missing = set(orders_once.customer_id) - set(clean.customer_id)
print(missing)
```'''),
    empty(),
    md('''
> **Kavya's review.** "Two exports, two grains. The customer table is one row per customer and the
> raw export is one row per payment. Say the grain before you pivot, count rows against ids, and
> tie the grand total to Monday's number. A pivot that has not been reconciled has not been built."

### In the interview

**[F] Your pivot shows a different total from the warehouse. Where do you look first?** At the
grain. I count the rows under the pivot against the distinct keys the warehouse counts; if rows
outnumber keys, something repeats, usually a join or an export at a finer grain such as payments or
line items, and a Sum adds each repeat. Second, the filters and the period: a date window cut
differently, or a status the warehouse excludes. Third, what is missing: keys in the warehouse and
not in the sheet. Here the export had 1,450 rows for 1,000 orders; counting each order once brought
Rs 39.41 crore back to Rs 19.84 crore, the warehouse to the rupee.

**[S] SQL, pandas or Excel: how do you choose?** By who has to trust the number and how often it is
rebuilt. Anything Finance audits is computed where it can be reviewed and rerun: the warehouse, in
SQL. The analyst's exploration, rerun and changed daily, is pandas. The last mile, where a
stakeholder slices a finished table in a room, is Excel, fed from the warehouse's export and never
typed over.

### Depth: why a PivotTable needs a refresh

A PivotTable keeps its own cache of the source. Microsoft's own page says a PivotTable built on a
source "need[s] to be refreshed" when data is added (Create a PivotTable, verified 29 September 2026),
so a director who edits a source cell sees nothing move until somebody presses Refresh. A tree
written as `SUMIFS` over the export recalculates at once. The deck pack in `demos/` does it that way
for that reason.'''),
    code('''
kit.flow(["say the grain", "count rows against ids", "tie the total to the warehouse", "then slice"],
         lit=2, title="Before any pivot reaches a director")
kit.table(["What this round established", "The number"],
          [("the clean table, pivoted", "one row per customer, 300 customers"),
           ("the hurried pivot on the raw export", "Rs 39.41 crore, 1,450 rows for 1,000 orders"),
           ("after Remove Duplicates", "Rs 39.41 crore, 1,400 rows"),
           ("each order counted once", "Rs 19.84 crore, the warehouse to the rupee"),
           ("Retail-Plus orders per customer", "2.36 in Q1 to 1.84 in Q2")])
kit.check_summary()'''),
    md('''
Round 2 takes the clean table to the protect list, and asks what a lookup should say when an id is
not there.'''),
]

# =========================================================================== round 2
round2 = [
    md('''
# The protect list, and a lookup that must fail out loud

**Week 2, Friday. Round 2 of 3.** By the end of this notebook you can build the top-fifty protect
list, find a member by id with an exact match, show why an approximate match hands back a neighbour
for a missing id, and total a filtered list so it adds only the rows a director can see.

> **The client asks.** "The top-fifty protect list, with a lookup so I can find any member by id."
>
> Meera's chief of staff, Kalpa Retail

> **Kavya's review.** "A lookup that cannot find an id says so. A lookup that answers with somebody
> else's row is worse than no lookup, because nobody in the room can tell."

Round 1 ended on a tree that reconciles and a clean table you reconciled yourself. The protect list is
Wednesday's list for the head of Retail-Plus, now read from the customer table across both quarters.'''),
    md('''
**Setup.** The same two exports and the same control totals as round 1.'''),
    code(LOAD),
    ladder(1, ["the top fifty Retail-Plus members", "an exact lookup by member id",
               "the trap: an approximate lookup on a missing id", "the trap: a total that counts hidden rows",
               "the list the chief of staff can filter"]),
    md('''
## 1. The top fifty

The head of Retail-Plus asked on Wednesday who to protect first. The list is the fifty Retail-Plus
members with the highest revenue across both quarters. In Excel: filter `segment` to Retail-Plus,
sort `revenue` largest to smallest, and keep the first fifty rows; in the deck pack a rank column
does it with `COUNTIFS`, so a director who changes the list size sees it recalculate.

**Predict before you run.** How many Retail-Plus members are in the customer table, and so how deep
does a top fifty reach? a) about half of them; b) all of them; c) the top tenth; d) fewer than fifty
exist.'''),
    code('''
plus = clean[clean.segment == "Retail-Plus"].sort_values(["revenue", "customer_id"], ascending=[False, True])
plus = plus.reset_index(drop=True)
plus["rank"] = plus.index + 1
top = plus.head(50)
kit.stats([(f"{len(plus)}", "Retail-Plus members", "in the customer table"),
           (kit.rupees(top.revenue.sum()), "the top fifty's revenue", "both quarters"),
           (kit.rupees(top.revenue.iloc[-1]), "the fiftieth member", "the cut-off")])
kit.bars([(r.customer_id, int(r.revenue)) for r in top.head(10).itertuples()], fmt=kit.rupees,
         title="The ten members at the top of the protect list")
kit.strip(plus.revenue.tolist(), markers=[("cut-off at rank 50", int(top.revenue.iloc[-1]), "bad")],
          title="Every Retail-Plus member's revenue, with the protect list's cut-off")'''),
    md('''
**What happened.** The answer is a. There are 106 members, so the list keeps a little under half,
from Rs 25,840 at the top to Rs 8,580 at rank fifty. The next member spent Rs 8,520, so there is no
tie at the boundary this time, and the list ships exactly fifty rows.'''),
    code('''
kit.check("the list holds fifty members", len(top) == 50)
kit.check("every member on the list is Retail-Plus", set(top.segment) == {"Retail-Plus"})
kit.check("no tie sits across the fiftieth place", plus.revenue.iloc[49] != plus.revenue.iloc[50],
          f"{plus.revenue.iloc[49]} against {plus.revenue.iloc[50]}")'''),
    md('''
## 2. Find a member by id, exactly

The chief of staff types an id and wants the member's row. In Excel the lookup is
`=INDEX(revenue, MATCH(id, customer_id, 0))`, where the `0` asks for an exact match, or in the
room's Excel `=XLOOKUP(id, customer_id, revenue, "not in the table")`, whose match mode is exact by
default (Microsoft Support, XLOOKUP, verified 29 September 2026). In pandas, the id becomes the index.

**Predict before you run.** What should the lookup return for C-0152? a) the first row of the table;
b) C-0152's row; c) the nearest id below C-0152; d) an error, since ids are text.'''),
    code('''
by_id = clean.set_index("customer_id")


def find(member):
    """An exact lookup that says so when the id is missing."""
    if member not in by_id.index:
        return "not in the table"
    row = by_id.loc[member]
    rank = plus.set_index("customer_id")["rank"].get(member)
    place = f"rank {rank} of 50" if rank is not None and rank <= 50 else "not on the list"
    return f"{member}: {row.segment}, {row.city}, {kit.rupees(row.revenue)}, {place}"


print(find("C-0152"))
kit.tree({"label": "MATCH(id, ids, 0)", "branches": [
    ("found", {"label": "the member's row"}),
    ("missing", {"label": "not in the table", "kind": "good"})]},
    title="An exact lookup has two exits, and both are visible")'''),
    code('''
kit.check("the exact lookup returns the member asked for", find("C-0152").startswith("C-0152"))
kit.check("the exact lookup says so for an id that is not there", find("C-0195") == "not in the table")'''),
    md('''
**What happened.** The answer is b. C-0152 is the top of the list at Rs 25,840. The second check
tried C-0195, a Retail-Plus member with no orders in these two quarters, so the customer table has
no row for them, and the exact lookup says so.

## 3. The trap: an approximate lookup on a missing id

**The plausible wrong answer.** A hurried sheet uses `=VLOOKUP(id, table, 5)`. Its fourth argument
is left out, and Microsoft's page says the argument defaults to an approximate match (VLOOKUP,
verified 29 September 2026). On a table sorted by id, an approximate match returns the largest id not
above the one asked for.'''),
    code('''
ids = sorted(clean.customer_id)


def vlookup_approximate(member):
    """What VLOOKUP with its fourth argument left out returns on a table sorted by id."""
    below = [i for i in ids if i <= member]
    return below[-1] if below else "#N/A"


returned = vlookup_approximate("C-0195")
row = by_id.loc[returned]
rank = int(plus.set_index("customer_id").loc[returned, "rank"])
kit.table(["Asked for", "Row returned", "Revenue", "City", "What the sheet says"],
          [("C-0195", returned, kit.rupees(row.revenue), row.city, f"on the protect list at rank {rank}")],
          caption="The approximate lookup answers without a warning")'''),
    md('''
**Why it is wrong.** The member asked for is not in the table, and the sheet answers with their
neighbour's row: Rs 16,740, Hyderabad, rank 15. In business terms, the chief of staff tells a director
that C-0195 is one of Kalpa's best members and on the list, and a retention offer goes to someone who
has not bought in six months, while nobody asks why the id was missing. Nothing on the screen looks
wrong. The check is to compare the id returned with the id asked for.'''),
    code('''
kit.sequence(["Chief of staff", "The sheet", "Customer table"],
             [("Chief of staff", "The sheet", "find C-0195"),
              ("The sheet", "Customer table", "largest id not above C-0195"),
              ("Customer table", "The sheet", "C-0194's row"),
              ("The sheet", "Chief of staff", "Rs 16,740, rank 15")],
             title="The approximate lookup, message by message")
kit.check("the approximate lookup returns a different member", returned != "C-0195", returned)
kit.check("the neighbour it returns sits on the protect list", rank <= 50, f"rank {rank}")'''),
    md('''
**The fix.** An exact match with a visible not-found path: `=IFERROR(INDEX(revenue, MATCH(id, ids,
0)), "not in the table")`, or `XLOOKUP` with its fourth argument filled in. The fix changes one answer
from "rank 15, Rs 16,740" to "not in the table", which is the answer that makes somebody check the
export.'''),
    code('''
answers = [("C-0152", find("C-0152"), vlookup_approximate("C-0152")),
           ("C-0195", find("C-0195"), vlookup_approximate("C-0195")),
           ("C-0999", find("C-0999"), vlookup_approximate("C-0999"))]
kit.table(["Id asked for", "Exact lookup", "Approximate lookup returns"], answers,
          caption="Three ids, both lookups: only the exact one says when an id is missing")
kit.check("both lookups agree on an id that is there", answers[0][2] == "C-0152")
kit.check("an id past the end also gets a neighbour from the approximate lookup", answers[2][2] == ids[-1],
          answers[2][2])'''),
    md('''
**Your turn.** The head of Retail-Plus will read out one member id in the room, a member she knows
well. Type the id into the empty cell below with both lookups, run it, and say what each one tells you
and which one you would let the chief of staff read aloud:

```python
member = "..."          # the id read out in the room
print(find(member))
print(vlookup_approximate(member))
```'''),
    empty(),
    md('''
## 4. The trap: a total that counts rows a filter hid

The chief of staff filters the protect list to Mumbai before a call with the Mumbai store head and
reads the total at the foot of the list.

**The plausible wrong answer.** The foot is `=SUM(E12:E61)`. In Excel, rows hidden by a filter drop
out of `SUBTOTAL`, and `SUM` still adds them; with rows hidden by hand, `SUBTOTAL(109)` ignores them
and `SUBTOTAL(9)` does not (SUBTOTAL, verified 29 September 2026). On LibreOffice 24.2.7.2, `SUM`
over three rows with one hidden returned 60 where `SUBTOTAL(109)` returned 40.'''),
    code('''
top = top.assign(visible=top.city == "Mumbai")
foot_sum = int(top.revenue.sum())
foot_visible = int(top.loc[top.visible, "revenue"].sum())
kit.stats([(kit.rupees(foot_sum), "SUM at the foot", "all fifty rows"),
           (kit.rupees(foot_visible), "SUBTOTAL(109)", f"the {int(top.visible.sum())} Mumbai rows you can see"),
           (f"{foot_sum / foot_visible:.1f} times", "the overstatement", "read as Mumbai's list")])
by_city = top.groupby("city").revenue.sum().sort_values(ascending=False)
kit.bars([(c, int(v)) for c, v in by_city.items()], fmt=kit.rupees, lit=[list(by_city.index).index("Mumbai")],
         title="The protect list's revenue by city: Mumbai is one bar, the SUM is all six")'''),
    md('''
**Why it is wrong.** The Mumbai store head is told the members on their list spent Rs 7.15 lakh, when
the eleven on screen spent Rs 1.57 lakh, and a retention budget sized on the first number is four and
a half times too big. The check is to count what the foot counts: `=SUBTOTAL(102, E12:E61)` counts
only visible numbers, and if that count is smaller than the rows the total adds, the total is adding
hidden rows. The fix is `=SUBTOTAL(109, E12:E61)`, which the deck pack uses.'''),
    code('''
kit.bars([("SUM at the foot", foot_sum), ("SUBTOTAL(109) at the foot", foot_visible)],
         fmt=kit.rupees, lit=[1], title="Two formulas at the foot of the list filtered to Mumbai")
kit.check("the foot SUM counts rows the filter hid", foot_sum > foot_visible)
kit.check("the visible total is Mumbai's eleven members", int(top.visible.sum()) == 11, f"{int(top.visible.sum())} rows")
kit.check("the visible total is less than a quarter of the SUM", foot_visible / foot_sum < 0.25,
          f"{foot_visible / foot_sum:.1%}")'''),
    md('''
> **Kavya's review.** "Two checks before a list leaves the team. Ask the lookup for an id you know is
> missing and watch it say so. Filter the list and count what the foot adds. Neither takes a minute,
> and both failures are silent."

### In the interview

**[S] A stakeholder wants to poke the numbers themselves. What do you give them, and what do you never
give them?** I give them a finished table that reconciles to the source of truth, with the inputs
they may change marked and everything else computed: a list they can filter, a lookup that says
"not in the table", a total that follows their filter. I never give them the source itself to edit,
a lookup that can answer with the wrong row, or a number whose definition is not on the sheet,
because each of those lets the room change the answer without anybody seeing it change.

**[F] Your lookup returned a member for an id that does not exist. What went wrong?** The match type.
`VLOOKUP` with its fourth argument left out, or `MATCH` with 1, returns the nearest id below on a
sorted table. The fix is an exact match with a not-found path, and the habit is to test every lookup
with an id you know is missing before anyone else uses it.

### Depth: why XLOOKUP is taught and INDEX and MATCH ship

`XLOOKUP` defaults to an exact match and takes an `if_not_found` argument, which makes the safe
lookup the short one. It arrived after the LibreOffice this programme proves workbooks on: LibreOffice
24.2.7.2 returns `#NAME?` for it, checked on 29 September 2026. So the workbooks compute with `INDEX`
and `MATCH`, and the one `XLOOKUP` cell in the deck pack is labelled as computed in Excel and not
proved here.'''),
    code('''
kit.flow(["test a missing id", "exact match, visible not-found", "filter, then count the foot",
          "SUBTOTAL(109) at the foot"], lit=1, title="Before a list reaches a director")
kit.table(["What this round established", "The number"],
          [("the protect list", "50 Retail-Plus members, Rs 7,14,890, cut-off Rs 8,580"),
           ("an approximate lookup on C-0195", "C-0194's row, rank 15, Rs 16,740"),
           ("the exact lookup on C-0195", "not in the table"),
           ("the list filtered to Mumbai, SUM", "Rs 7,14,890"),
           ("the list filtered to Mumbai, SUBTOTAL(109)", "Rs 1,56,790 for 11 members")])
kit.check_summary()'''),
    md('''
Round 3 puts one number on the front page and asks what it needs beside it to be read correctly.'''),
]

# =========================================================================== round 3
round3 = [
    md('''
# One number on the front page

**Week 2, Friday. Round 3 of 3.** By the end of this notebook you can choose the front-page number,
give it its period, its comparison and its denominator, show its trend without letting one lumpy
segment write the story, and recompute it the moment a director changes what it covers.

> **The client asks.** "One number on the front page with its trend. If a director changes an
> assumption in the room, the sheet must recalculate in front of them."
>
> Meera's chief of staff, Kalpa Retail

> **Kavya's review.** "A number without its period is read against whatever the director remembers.
> A percentage without its base is read as whatever the director fears."

Round 1 left a tree that reconciles by segment and quarter, and round 2 a list that fails out loud.
This round turns the tree into one card.'''),
    md('''
**Setup.** The two exports and the control totals. The quarter and month are added to the raw export,
and each order is counted once, which round 1 proved reconciles.'''),
    code(LOAD + '''
raw["quarter"] = pd.to_datetime(raw.order_date).dt.month.map(lambda m: "Q1" if m <= 6 else "Q2")
raw["month"] = pd.to_datetime(raw.order_date).dt.strftime("%b")
orders = raw.drop_duplicates("order_id")
by_q = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")
print(crore(by_q.Q1.sum()), "in Q1 and", crore(by_q.Q2.sum()), "in Q2")'''),
    ladder(2, ["the candidates for the front page", "the trap: a number with no period",
               "the trap: a percentage with no base", "the trend, and what makes it lie",
               "the card, recomputed per assumption"]),
    md('''
## 1. Which number goes on the front page

Meera's question since Week 1 is where growth comes from and where it leaks. The front page carries
one number that answers the first half and points at the second.

**Predict before you run.** Which is the front-page number for Monday's growth review? a) revenue
across both quarters, the biggest; b) Q2 revenue against Q1; c) the number of customers; d) Retail-Plus
orders per member.'''),
    code('''
q1, q2 = int(by_q.Q1.sum()), int(by_q.Q2.sum())
kit.stats([(crore(q1 + q2), "both quarters", "April to September"),
           (crore(q2), "Q2 revenue", "July to September"),
           (f"{(q2 - q1) / q1:+.1%}", "Q2 on Q1", "the trend Meera asked about")])
kit.columns(["Q1, April to June", "Q2, July to September"], [("revenue", [q1, q2])], fmt=crore,
            title="Revenue by quarter, each order counted once")'''),
    md('''
**What happened.** The answer is b. The growth review asks what moved, so the number is the latest
quarter against the one before: Rs 9.84 crore in Q2, down 1.6 percent on Rs 10.00 crore in Q1.
Option d is the finding under it, which the sentence beside the number carries.'''),
    code('''
kit.check("Q2 matches Monday's warehouse number", q2 == WAREHOUSE["Q2"], crore(q2))
kit.check("Q2 fell against Q1", q2 < q1, f"{(q2 - q1) / q1:+.2%}")'''),
    md('''
## 2. The trap: a number with no period

**The plausible wrong answer.** The fastest card is the grand total of the customer table in big
type: **Revenue Rs 19.84 crore.**'''),
    code('''
bare = int(clean.revenue.sum())
kit.stats([(crore(bare), "Revenue", "the card as drafted, with nothing beside it")])
kit.bars([("the bare card, read as Q2", bare), ("Q2, like with like", q2), ("Q1, as the director remembers it", q1)],
         fmt=crore, lit=[0], title="Read as a quarter, the bare number doubles revenue")'''),
    md('''
**Why it is wrong.** A director who remembers Rs 10.00 crore for Q1 reads Rs 19.84 crore as this
quarter and says revenue nearly doubled, and the growth review celebrates a quarter in which revenue
fell. The number is two quarters added together, and nothing on the card says so. The check is to
read the card aloud and ask "which months?" and "against what?"; if the card cannot answer, it is not
ready. The fix names the period and the comparison on the card itself.'''),
    code('''
card = f"Q2, July to September 2026: {crore(q2)}, down {abs(q2 - q1) / q1:.1%} on Q1, April to June 2026 ({crore(q1)})"
print(card)
kit.check("the bare number is roughly two quarters", abs(bare / q2 - 2) < 0.05, f"{bare / q2:.2f} times Q2")
kit.check("the fixed card names its months", "July to September" in card and "April to June" in card)'''),
    md('''
## 3. The trap: a percentage with no base

The tree says the fall sits in Retail-Plus, so the draft card for the second slot is the segment's
change.

**Predict before you run.** "Retail-Plus revenue down 29.4 percent." What does a director hear? a) a
small tier had a bad quarter; b) the business is collapsing; c) nothing, a percentage is complete; d)
that Business fell too.'''),
    code('''
p1, p2 = int(by_q.Q1["Retail-Plus"]), int(by_q.Q2["Retail-Plus"])
kit.stats([(f"{(p2 - p1) / p1:.1%}", "Retail-Plus, the card as drafted", "no base, no share"),
           (lakh(p1 - p2), "what the fall is in rupees", f"on a {crore(q1)} quarter"),
           (f"{p2 / q2:.1%}", "Retail-Plus's share of Q2", "the denominator the card left out")])
moves = [(s, int(by_q.Q2[s] - by_q.Q1[s])) for s in ["Business", "Retail-Core", "Retail-Plus", "Student"]]
kit.bridge(("Q1 revenue", q1), moves, end_label="Q2 revenue", fmt=money, lo=96_000_000, lit=[2],
           title="Q1 to Q2 by segment: the axis starts at Rs 9.60 crore so the small moves show")'''),
    md('''
**What happened.** The answer is b, and that is the trap. The 29.4 percent is real, and it is 29.4
percent of Rs 5.86 lakh, a segment worth 0.4 percent of the quarter. The rupee fall of the whole
company is mostly Business, which moves in lumps of corporate invoices. Read without its base, the card
sends the room to rescue the wrong thing, or to panic. The check is to put the rupee base and the share
beside every percentage. A second check catches a formula slip that makes it worse: a change divided by
the current quarter instead of the earlier one.'''),
    code('''
right = (p2 - p1) / p1
wrong_base = (p2 - p1) / p2
kit.table(["How the change is computed", "Retail-Plus, Q1 to Q2"],
          [("on the earlier quarter, (Q2 - Q1) / Q1", f"{right:.1%}"),
           ("on the current quarter, (Q2 - Q1) / Q2", f"{wrong_base:.1%}")],
          caption="The base of a change is the period you are comparing against")
plus_card = (f"Retail-Plus, Q2, July to September 2026: {lakh(p2)}, down {abs(right):.1%} on Q1 ({lakh(p1)}); "
             f"{p2 / q2:.1%} of company revenue")
print(plus_card)
kit.check("the change on the wrong base overstates the fall", abs(wrong_base) > abs(right),
          f"{wrong_base:.1%} against {right:.1%}")
kit.check("Retail-Plus is under one percent of the quarter", p2 / q2 < 0.01, f"{p2 / q2:.2%}")'''),
    md('''
## 4. The trend, and what makes it lie

The chief of staff wants the number **with its trend**. Month by month, the company line is Business's
invoices, and a consumer segment's drift is invisible under it.

**Predict before you run.** July's company revenue is 45 percent above June's. Is July growth? a)
yes, the best month of the half-year; b) no, one segment's invoices landed in it; c) yes, the monsoon
sale worked; d) it cannot be told from months.'''),
    code('''
order = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]
monthly = orders.pivot_table(index="month", columns="segment", values="order_amount", aggfunc="sum").reindex(order)
company = monthly.sum(axis=1)
consumer = company - monthly["Business"]
kit.line(order, [("all segments", [int(v) for v in company], "plain")], fmt=crore,
         title="Company revenue by month: the shape is Business's invoices")
kit.line(order, [("all except Business", [int(v) for v in consumer], "bad"),
                 ("Retail-Plus", [int(v) for v in monthly["Retail-Plus"]], "plain")], fmt=lakh,
         title="The consumer segments by month: a steady slide from June")'''),
    md('''
**What happened.** The answer is b. Business's corporate invoices land in lumps, so the company line
jumps in April and July and tells you when invoices were booked. Take Business out and the consumer
revenue falls in each of the last three months, from Rs 3.32 lakh in June to Rs 2.48 lakh in
September, and Retail-Plus carries most of that fall. So the trend beside the front-page number is
the consumer line, labelled as such.'''),
    code('''
kit.check("July looks like growth on the company line", company["Jul"] > company["Jun"] * 1.3,
          f"{company['Jul'] / company['Jun'] - 1:+.0%}")
kit.check("the consumer line falls every month from June", consumer["Jul"] < consumer["Jun"] and
          consumer["Aug"] < consumer["Jul"] and consumer["Sep"] < consumer["Aug"])'''),
    md('''
## 5. The card, recomputed when a director changes an assumption

A director says, "Take Business out, it is lumpy." Another says, "Show me Retail-Plus." The card has to
recompute its number, its comparison and its denominator from the same source, which is what the
yellow scope cell on the deck pack's FrontPage tab does. Here the card is one function.'''),
    code('''
def card_for(scope):
    """The front-page card for a scope, computed from the orders, never typed."""
    if scope == "All segments":
        a, b = q1, q2
    elif scope == "All except Business":
        a, b = q1 - int(by_q.Q1["Business"]), q2 - int(by_q.Q2["Business"])
    else:
        a, b = int(by_q.Q1[scope]), int(by_q.Q2[scope])
    money = crore if b >= 1e7 else lakh
    word = "down" if b < a else "up"
    return (f"{scope}, Q2, July to September 2026: {money(b)}, {word} {abs(b - a) / a:.1%} on Q1 "
            f"({money(a)}); {b / q2:.1%} of company revenue"), (b - a) / a


cards = {s: card_for(s) for s in ["All segments", "All except Business", "Retail-Plus"]}
for s, (text, _) in cards.items():
    print(text)
kit.columns(list(cards), [("fall on Q1, percent", [round(-c * 100, 1) for _, c in cards.values()])],
            fmt=lambda v: f"{v:.1f}%", title="One card, three scopes: how far each fell on Q1")'''),
    code('''
kit.check("taking Business out turns a 1.6 percent fall into a 17.3 percent fall",
          round(cards["All except Business"][1] * 100, 1) == -17.3, f"{cards['All except Business'][1]:.1%}")
kit.check("every card carries its period, its comparison and its share",
          all("July to September" in t and "on Q1" in t and "of company revenue" in t for t, _ in cards.values()))'''),
    md('''
> **Kavya's review.** "Read the card aloud to someone who has not seen the sheet. If they ask which
> months, against what, or out of how much, the card answers on its face or it goes back."

### In the interview

**[F] How do you present one number so it is not misread?** With four things beside it: the period it
covers, the comparison it moved against, the base or share that says how big it is, and one sentence
saying what it means for the decision. "Q2, July to September: Rs 9.84 crore, down 1.6 percent on
Q1's Rs 10.00 crore; the fall sits in Retail-Plus, where orders per member fell from 2.36 to 1.84."
A bare Rs 19.84 crore gets read as a doubled quarter; a bare 29.4 percent gets read as a collapse.

**[D] Two directors change assumptions in the room and the sheet recalculates differently for each.
What did you get right, and what do you fix?** What I got right: the assumptions are inputs, and every
number recomputes from the same source, so both answers are honest for their assumptions. What I fix:
the card must say which assumption it is showing, so the two answers are never compared as if they
were one number. Taking Business out moves the change from minus 1.6 to minus 17.3 percent, and the
scope has to be printed on the card, which is why the deck pack writes it into the sentence.

### Depth: why the trend is a line of months and the number is a quarter

The front-page number is a quarter because Finance closes quarters and the warehouse reconciles them.
The trend is monthly because three points in a quarter show a direction a single change cannot. Both
come from the same orders, so they cannot disagree, and the card's check ties the two quarters of the
trend back to the warehouse.'''),
    code('''
kit.vflow(["the number: Q2 revenue", "its period: July to September 2026", "its comparison: Q1, down 1.6%",
           "its base: share of company revenue", "its sentence: where the fall sits"], lit=4,
          title="A front-page card, top to bottom")
kit.table(["What this round established", "The number"],
          [("the front-page number", "Q2 Rs 9.84 crore, down 1.6 percent on Q1"),
           ("the bare total, read as a quarter", "Rs 19.84 crore"),
           ("Retail-Plus with no base", "down 29.4 percent, 0.4 percent of the quarter"),
           ("the same change on the wrong base", "41.7 percent"),
           ("all except Business, the director's scope", "down 17.3 percent")])
kit.check_summary()'''),
    md('''
The afternoon runs the three deliverables end to end on the escalated case, then defends the operating
rule against a director who wants to edit the source.'''),
]

# =========================================================================== case 1: the three deliverables
case1_steps = [
    ("""## Step 1. One row per order

The raw export has one row per payment. Pick the line that leaves one row per order.""",
     '''# TODO 1. Which line leaves exactly one row per order?
#   a) orders = raw.drop_duplicates()
#   b) orders = raw.drop_duplicates("customer_id")
#   c) orders = raw.drop_duplicates("order_id")
#   d) orders = raw[raw.paid_amount > 0]
orders = __TODO1__
orders = orders.assign(quarter=pd.to_datetime(orders.order_date).dt.month.map(lambda m: "Q1" if m <= 6 else "Q2"))
print(len(raw), "rows in the export,", len(orders), "rows after this step")''',
     "orders = raw.drop_duplicates(\"order_id\")",
     '''kit.check("one row per order", len(orders) == orders.order_id.nunique() == 1000, f"{len(orders)} rows")
kit.check("the two quarters reconcile to the warehouse", int(orders.order_amount.sum()) == sum(WAREHOUSE.values()),
          crore(orders.order_amount.sum()))''',
     "a keeps the 400 instalment orders twice, since their rows differ in paid_amount. b keeps one order per customer and loses 700 orders. d drops the 30 unpaid orders and keeps every repeat."),
    ("""## Step 2. The tree by segment and quarter

Customers, orders and revenue per segment and quarter, then the two rates.""",
     '''# TODO 2. How are customers counted in each segment and quarter?
#   a) ("customer_id", "count")
#   b) ("customer_id", "nunique")
#   c) ("order_id", "nunique")
#   d) ("customer_id", "size")
tree = orders.groupby(["segment", "quarter"]).agg(customers=__TODO2__,
                                                  orders=("order_id", "size"),
                                                  revenue=("order_amount", "sum"))
# TODO 3. Orders per customer is which division?
#   a) tree.customers / tree.orders
#   b) tree.revenue / tree.customers
#   c) tree.orders / tree.customers
#   d) tree.orders / tree.customers.sum()
tree["orders_per_customer"] = __TODO3__
tree["revenue_per_order"] = tree.revenue / tree.orders
kit.columns(["Retail-Core", "Retail-Plus", "Student"],
            [(qq, [round(tree.loc[(s, qq), "orders_per_customer"], 2) for s in ["Retail-Core", "Retail-Plus", "Student"]])
             for qq in ["Q1", "Q2"]], fmt=lambda v: f"{v:.2f}", title="Orders per customer, Q1 against Q2")''',
     None,
     '''kit.check("Retail-Plus has 76 customers in Q2", tree.loc[("Retail-Plus", "Q2"), "customers"] == 76,
          f"{tree.loc[('Retail-Plus', 'Q2'), 'customers']}")
kit.check("Retail-Plus orders per customer fall from 2.36 to 1.84",
          round(tree.loc[("Retail-Plus", "Q1"), "orders_per_customer"], 2) == 2.36 and
          round(tree.loc[("Retail-Plus", "Q2"), "orders_per_customer"], 2) == 1.84)''',
     "TODO 2: a and d count rows, so a customer with three orders counts three times; c counts orders. TODO 3: a inverts the rate; b is revenue per customer; d divides by every customer in every segment and quarter."),
    ("""## Step 3. The protect list

The fifty Retail-Plus members with the highest revenue across both quarters, from the clean table.""",
     '''# TODO 4. Which line gives the fifty Retail-Plus members with the highest revenue?
#   a) clean.nlargest(50, "revenue")
#   b) clean[clean.segment == "Retail-Plus"].nsmallest(50, "revenue")
#   c) clean[clean.segment == "Retail-Plus"].head(50)
#   d) clean[clean.segment == "Retail-Plus"].nlargest(50, "revenue")
protect = __TODO4__
kit.strip(protect.revenue.tolist(), title="The protect list's fifty revenues")''',
     None,
     '''kit.check("fifty members, all Retail-Plus", len(protect) == 50 and set(protect.segment) == {"Retail-Plus"})
kit.check("the cut-off is Rs 8,580", int(protect.revenue.min()) == 8580, kit.rupees(protect.revenue.min()))''',
     "a ranks every segment together, so 39 Business buyers take most of the fifty places. b keeps the fifty lowest. c keeps the first fifty by id order, which is no ranking at all."),
    ("""## Step 4. A lookup that fails out loud

The lookup the chief of staff types an id into. It must say so when the id is missing.""",
     '''by_id = clean.set_index("customer_id")
# TODO 5. Which lookup returns the revenue for an id, or the words "not in the table"?
#   a) lambda m: by_id.revenue.get(m, "not in the table")
#   b) lambda m: by_id.revenue.iloc[by_id.index.searchsorted(m) - 1]
#   c) lambda m: by_id.revenue.iloc[0]
#   d) lambda m: by_id.revenue.asof(m)
lookup = __TODO5__
kit.table(["Id", "Answer"], [(m, lookup(m)) for m in ["C-0152", "C-0195"]])''',
     None,
     '''kit.check("a present id returns its revenue", lookup("C-0152") == 25840)
kit.check("a missing id says so", lookup("C-0195") == "not in the table", str(lookup("C-0195")))''',
     "b and d are approximate matches: each returns the neighbour below a missing id, which is VLOOKUP with its fourth argument left out. c returns the first member for every id."),
    ("""## Step 5. The front-page card

Q2 revenue with its comparison, measured on the earlier quarter.""",
     '''q1 = int(orders.loc[orders.quarter == "Q1", "order_amount"].sum())
q2 = int(orders.loc[orders.quarter == "Q2", "order_amount"].sum())
# TODO 6. Which is the change from Q1 to Q2?
#   a) (q2 - q1) / q2
#   b) (q2 - q1) / q1
#   c) (q1 - q2) / (q1 + q2)
#   d) q2 / q1
change = __TODO6__
card = (f"Q2, July to September 2026: {crore(q2)}, {'down' if change < 0 else 'up'} {abs(change):.1%} "
        f"on Q1, April to June 2026 ({crore(q1)})")
print(card)''',
     None,
     '''kit.check("the change is minus 1.6 percent", round(change * 100, 1) == -1.6, f"{change:.2%}")
kit.check("the card names both periods", "July to September" in card and "April to June" in card)''',
     "a divides by the current quarter and reads minus 1.63 percent; on Retail-Plus the same slip reads 41.7 against 29.4. c is a share of the two quarters together. d is a ratio, 0.984, which a card would print as 98 percent."),
    ("""## Step 6. The total a filter shows

The chief of staff filters the list to Mumbai. What does the foot say?""",
     '''visible = protect.city == "Mumbai"
# TODO 7. Which total is what SUBTOTAL(109) shows at the foot of the filtered list?
#   a) protect.revenue.sum()
#   b) protect.loc[visible, "revenue"].sum()
#   c) protect.loc[~visible, "revenue"].sum()
#   d) clean.loc[clean.city == "Mumbai", "revenue"].sum()
foot = __TODO7__
kit.stats([(kit.rupees(foot), "the foot", f"{int(visible.sum())} rows visible")])''',
     None,
     '''kit.check("the foot adds only the eleven Mumbai members", int(foot) == 156790, kit.rupees(foot))
kit.check("the foot is less than the whole list", foot < protect.revenue.sum())''',
     "a is SUM, which adds the rows the filter hid. c adds exactly the hidden rows. d adds every Mumbai customer in every segment, Business included."),
]

case2_steps = [
    ("""## Step 1. A director types over a cell

In the room, a director overwrites Retail-Plus Q2 revenue in the tree with the Rs 5,00,000 he expects
next quarter, so the card looks better. The sheet recalculates.""",
     '''sheet = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")
edited = sheet.copy()
edited.loc["Retail-Plus", "Q2"] = 500000
# TODO 1. Which number does the edited card now show for Retail-Plus, Q1 to Q2?
#   a) the true change, since the source did not move
#   b) the edited change, computed from the typed value
#   c) an error, since a typed value breaks the formula
#   d) no change, since Q1 was not edited
shown = __TODO1__
kit.bars([("Retail-Plus Q2, from the export", int(sheet.loc["Retail-Plus", "Q2"])),
          ("Retail-Plus Q2, after the edit", int(edited.loc["Retail-Plus", "Q2"]))],
         fmt=kit.rupees, lit=[1], title="One typed cell moves the card")''',
     '"b"',
     '''kit.check("the edited card shows a smaller fall", shown == "b" and
          edited.loc["Retail-Plus", "Q2"] > sheet.loc["Retail-Plus", "Q2"])
kit.check("the edit leaves no trace in the source", int(orders.order_amount.sum()) == sum(WAREHOUSE.values()))''',
     "The card recomputes from whatever sits in the cell, so it shows a fall of 14.6 percent where the export says 29.4. a assumes the sheet reads the source; it reads the cell. c is what people hope; a typed number is a valid input. d ignores that the change uses Q2."),
    ("""## Step 2. The check that catches drift

A drift check compares the sheet with the source of truth. Pick the comparison that fires here.""",
     '''# TODO 2. Which comparison catches the director's edit?
#   a) the sheet's Q2 total against the warehouse's Q2 total
#   b) the sheet's number of segments against four
#   c) the Q1 column against the warehouse's Q1
#   d) the card's sentence against yesterday's sentence
drift = {"a": int(edited.Q2.sum()) - WAREHOUSE["Q2"], "b": len(edited) - 4,
         "c": int(edited.Q1.sum()) - WAREHOUSE["Q1"], "d": 0}[__TODO2__]
kit.bridge(("the warehouse, Q2", WAREHOUSE["Q2"]), [("the typed-over cell", int(drift))],
           end_label="the sheet, Q2", fmt=kit.rupees, lo=98_000_000,
           title="The drift, in rupees: exactly the edit")''',
     '"a"',
     '''kit.check("the drift check fires", drift != 0, kit.rupees(drift))
kit.check("the drift equals the edit", drift == 500000 - int(sheet.loc["Retail-Plus", "Q2"]))''',
     "b counts rows, which an edit never changes. c looks at the quarter nobody touched. d compares wording, which moves whenever anybody improves a sentence."),
    ("""## Step 3. What the next refresh does

On Monday the tree is rebuilt from a fresh export.""",
     '''refreshed = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")
# TODO 3. After the refresh, what happened to the director's number?
#   a) it survived, since Excel keeps typed values
#   b) it moved into the warehouse
#   c) it doubled, since the export has two rows per payment
#   d) it was wiped without a trace, and so was its reason
after = __TODO3__
kit.bars([("Retail-Plus Q2, after the edit", int(edited.loc["Retail-Plus", "Q2"])),
          ("Retail-Plus Q2, after the refresh", int(refreshed.loc["Retail-Plus", "Q2"]))],
         fmt=kit.rupees, lit=[1], title="The refresh restores the export and loses the edit")''',
     '"b"',
     '''kit.check("the refresh restores the export's number", refreshed.loc["Retail-Plus", "Q2"] == sheet.loc["Retail-Plus", "Q2"])
kit.check("the refreshed sheet reconciles again", int(refreshed.values.sum()) == sum(WAREHOUSE.values()) and after == "d")''',
     "a is the drift the rule exists to stop: a typed value that survives a refresh is a second source of truth. b never happens; the warehouse does not read the sheet. c confuses the refresh with round 1's grain."),
    ("""## Step 4. Where the director's assumption belongs

The director's expectation is a real question: what would the card say if Retail-Plus recovered to
Rs 5,00,000? It belongs in the sheet, as an input beside the source, never over it.""",
     '''# TODO 4. Where does the what-if go?
#   a) over the Q2 cell, with a comment saying it was edited
#   b) in a yellow input cell, feeding a separate scenario line on the card
#   c) in the export, before it is loaded
#   d) nowhere; directors do not get what-ifs
scenario_q2 = 500000
place = __TODO4__
actual = sheet.loc["Retail-Plus", "Q2"] / sheet.loc["Retail-Plus", "Q1"] - 1
what_if = scenario_q2 / sheet.loc["Retail-Plus", "Q1"] - 1
kit.bars([("actual, from the export", round(-actual * 100, 1)),
          ("the director's scenario", round(-what_if * 100, 1))],
         fmt=lambda v: f"down {v:.1f}%", title="Retail-Plus, Q2 on Q1: two lines on one card, each labelled")''',
     '"b"',
     '''kit.check("the actual line still reconciles", int(sheet.values.sum()) == sum(WAREHOUSE.values()))
kit.check("the scenario is labelled and separate", place == "b" and round(what_if * 100, 1) == -14.6, f"{what_if:.1%}")''',
     "a keeps the edit and adds a note nobody reads on a projector. c edits the source of truth, which is the thing the rule forbids. d refuses a legitimate question and sends the director to type over cells anyway."),
]


def case_notebook(title, intro, steps, solution):
    cells = [md(title), md(intro), code(LOAD + '''
raw["quarter"] = pd.to_datetime(raw.order_date).dt.month.map(lambda m: "Q1" if m <= 6 else "Q2")
orders = raw.drop_duplicates("order_id")''' if steps is case2_steps else LOAD)]
    names = [t.split("\n")[0].replace("## ", "") for t, *_ in steps]
    cells.append(code(f"kit.vflow({names!r}, title='The steps in this notebook')"))
    for n, (text, body, fixed, check, why) in enumerate(steps):
        cells.append(md(text))
        src = body
        if solution:
            for k in range(1, 12):
                token = f"__TODO{k}__"
                if token in src:
                    src = src.replace(token, SOLUTIONS[steps is case2_steps][k])
        cells.append(code(src))
        cells.append(code(check))
        if solution:
            cells.append(md(f"**Why the other letters fail.** {why}"))
    return cells


# The keyed answers, as code, per notebook: False is case 1, True is case 2.
SOLUTIONS = {
    False: {1: 'raw.drop_duplicates("order_id")', 2: '("customer_id", "nunique")', 3: "tree.orders / tree.customers",
            4: 'clean[clean.segment == "Retail-Plus"].nlargest(50, "revenue")',
            5: 'lambda m: by_id.revenue.get(m, "not in the table")', 6: "(q2 - q1) / q1",
            7: 'protect.loc[visible, "revenue"].sum()'},
    True: {1: '"b"', 2: '"a"', 3: '"d"', 4: '"b"'},
}
KEY1, KEY2 = "cbcdabb", "badb"


def case1(solution):
    cells = case_notebook(
        "# Hands-on: the three deliverables, proved a second way",
        f"""**Week 2, Friday. The escalated case, part 5.** You built the three deliverables in Excel. This
notebook reaches the same numbers in pandas, which is Kavya's review: a second way to the same number.
Seven lettered `TODO` markers across six steps; each step ends on checks that tell you whether you
picked right. {"This is the executed solution." if solution else "Run it from the top: it stops at the first placeholder with a NameError until you fill it in, which is intended."}""",
        case1_steps, solution)
    cells.append(md(f"""**Post.** Your seven letters in order, as one line, and the three numbers your checks confirmed:
the Q2 revenue, the protect list's cut-off and the Mumbai foot.{" The key is `" + KEY1 + "`." if solution else ""}"""))
    cells.append(code("kit.check_summary()"))
    return cells


def case2(solution):
    cells = case_notebook(
        "# Hands-on: the operating rule, defended",
        f"""**Week 2, Friday. The second case.** A director wants to edit the source in the room. This
notebook plays it out on the tree: the edit, the check that catches it, the refresh that wipes it, and
where the director's assumption belongs. Four lettered `TODO` markers; each answer is the letter
itself, as a string. {"This is the executed solution." if solution else "Run it from the top: it stops at the first placeholder until you fill it in, which is intended."}""",
        case2_steps, solution)
    cells.append(md(f"""**Post.** Your four letters in order, as one line, then the one rule you would put on the sheet's
Start tab.{" The key is `" + KEY2 + "`." if solution else ""}"""))
    cells.append(code("kit.check_summary()"))
    return cells


if __name__ == "__main__":
    only = sys.argv[1:] or ["1", "2", "3", "ex1", "ex2"]
    if "1" in only:
        build(NB / "C2_W02_D05_01_pivot_STUDENT.ipynb", round1)
    if "2" in only:
        build(NB / "C2_W02_D05_02_lookup_STUDENT.ipynb", round2)
    if "3" in only:
        build(NB / "C2_W02_D05_03_front_page_STUDENT.ipynb", round3)
    if "ex1" in only:
        build(NB / "C2_W02_D05_ex1_hands_on_STUDENT.ipynb", case1(False), execute=False)
        build(SOL / "C2_W02_D05_ex1_hands_on_solution_STUDENT.ipynb", case1(True))
    if "ex2" in only:
        build(NB / "C2_W02_D05_ex2_hands_on_STUDENT.ipynb", case2(False), execute=False)
        build(SOL / "C2_W02_D05_ex2_hands_on_solution_STUDENT.ipynb", case2(True))
    print("built", ", ".join(only))

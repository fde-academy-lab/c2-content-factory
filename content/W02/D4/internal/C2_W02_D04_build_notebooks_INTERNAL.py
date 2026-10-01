"""Build Thursday's notebooks: six chapters, the escalated case and the second case.

Run from the repository root, with the warehouse loaded (bash .devcontainer/load_warehouse.sh):
    python3 content/W02/D4/internal/C2_W02_D04_build_notebooks_INTERNAL.py            every notebook
    python3 content/W02/D4/internal/C2_W02_D04_build_notebooks_INTERNAL.py c1 c4       named ones only
    python3 content/W02/D4/internal/C2_W02_D04_build_notebooks_INTERNAL.py sql         the sql/ files only

Each chapter notebook pairs with the deck section of the same number and question, and each starts
from the state the one before it reached: chapter 2 opens on chapter 1's table of 340 customers,
chapter 4 on chapter 2's reach, chapter 6 on everything. Every chapter runs the need, the options
with their sizing, the build with each step predicted, the trap, the second route and Kavya's
review. Each notebook is executed cold in its own folder by scripts/nb_make.py. The TODO twins are
written unexecuted and their solution twins executed.

No saved output names a planted record. The exposure feed's repeated customers are found by the
room in an empty your-turn cell; the mechanism is shown on four invented customers, labelled
invented; no cell prints the feed's row count beside its distinct customers. The falling flag is
checked against SQL as a set and never listed.

Every query a notebook runs is written once, in SQL below, and the same text is written to the
day's sql/ folder, so a learner in psql and a learner in the notebook read the same query.
"""
import pathlib
import sys
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, build, code, empty, md  # noqa: E402

DAY = ROOT / "content" / "W02" / "D4"
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"
SQLDIR = DAY / "sql"

CHAPTERS = ["One row per customer?", "Who did the sale reach?", "Is Retail-Plus slipping?",
            "Do three tools agree?", "Which tool for which job?", "Will Monday rebuild it?"]

ASK = '''
> **The client asks.** "One table, one row per customer, refreshed every Monday: how recently each
> customer bought, how often, how much, their segment, whether the monsoon sale reached them, and
> the flags we act on. Marketing's analysts live in Python, so build it in pandas, from the
> warehouse, and make it refresh in one run."
>
> The growth team, with the data platform lead, Kalpa Retail
'''

DOSSIER = ("`content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`, the retail dossier, "
           "has the business behind these numbers: section 3 for GMV, section 5 for frequency and "
           "repeat rate, and section 2 for Retail-Plus, the paid tier.")

# ----------------------------------------------------------------------------- the carried code
LOAD = SETUP + '''import pandas as pd

ENG = kit.engine()                  # the Kalpa warehouse in Postgres, read only
orders = pd.read_sql(
    "SELECT order_id, customer_id, order_date, quarter, channel, amount, status FROM orders",
    ENG, parse_dates=["order_date"])
customers = pd.read_sql("SELECT customer_id, segment, city FROM customers", ENG)
print(f"{len(orders):,} orders and {len(customers):,} customers read from the warehouse")
'''

TABLE = '''
# Chapter 1's table: one row per customer on the list, with the three numbers.
rfm = (orders.groupby("customer_id")
             .agg(last_order=("order_date", "max"), frequency=("order_id", "count"),
                  spend=("amount", "sum"))
             .reset_index())
table = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
table = table.assign(frequency=table["frequency"].fillna(0).astype("int64"),
                     spend=table["spend"].fillna(0))
print(f"chapter 1's table: {len(table)} customers, {int((table['frequency'] == 0).sum())} never ordered")
'''

FEED = '''
exposure = pd.read_csv(kit.data_dir() / "C2_W02_D04_exposure_STUDENT.csv", parse_dates=["exposed_date"])
print("the campaign platform's exposure feed, columns:", list(exposure.columns))
'''

REACH = '''
# Chapter 2's rule: one row per reached customer, their first exposure, and a merge that refuses
# to run if the rule is ever broken.
first_touch = (exposure.sort_values("exposed_date")
                       .drop_duplicates("customer_id", keep="first")[["customer_id", "exposed_date"]])
table = table.merge(first_touch, on="customer_id", how="left", validate="one_to_one")
table = table.assign(reached=table["exposed_date"].notna())
print(f"chapter 2's table: {len(table)} rows, {int(table['reached'].sum())} customers reached by the sale")
'''

# ----------------------------------------------------------------------------- the day's queries
# Each entry: (file stem, the question the file answers, [(block title, query), ...]).
SQL = {
    "c1": ("01_customer_table", "How recently, how often and how much has each customer bought?", [
        ("Option b: the warehouse groups the orders and sends one row per customer who ordered", '''
SELECT customer_id,
       max(order_date) AS last_order,
       count(*)        AS frequency,
       sum(amount)     AS spend
FROM   orders
GROUP  BY customer_id
ORDER  BY customer_id;'''),
        ("The second route: every customer on the list, including those who never ordered", '''
SELECT c.customer_id,
       c.segment,
       max(o.order_date)          AS last_order,
       count(o.order_id)          AS frequency,
       coalesce(sum(o.amount), 0) AS spend
FROM   customers c
LEFT   JOIN orders o ON o.customer_id = c.customer_id
GROUP  BY c.customer_id, c.segment
ORDER  BY c.customer_id;'''),
    ]),
    "c2": ("02_exposure", "Which customers did the monsoon sale reach, and what did they spend?", [
        ("The second route, part 1: customers the sale reached, each counted once", '''
SELECT count(DISTINCT customer_id) AS reached
FROM   campaign_exposure;'''),
        ("The second route, part 2: what the reached customers ordered, with no join that can multiply rows", '''
SELECT sum(amount) AS reached_spend
FROM   orders
WHERE  customer_id IN (SELECT customer_id FROM campaign_exposure);'''),
    ]),
    "c3": ("03_months", "How far did Retail-Plus members' spend fall from Q1 to Q2?", [
        ("Option c: one column per month, written out by hand", '''
SELECT o.customer_id,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-04-01' AND o.order_date < DATE '2026-05-01') AS apr,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-05-01' AND o.order_date < DATE '2026-06-01') AS may,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-06-01' AND o.order_date < DATE '2026-07-01') AS jun,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-07-01' AND o.order_date < DATE '2026-08-01') AS jul,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-08-01' AND o.order_date < DATE '2026-09-01') AS aug,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-09-01' AND o.order_date < DATE '2026-10-01') AS sep
FROM   orders o
JOIN   customers c ON c.customer_id = o.customer_id
WHERE  c.segment = 'Retail-Plus'
GROUP  BY o.customer_id
ORDER  BY o.customer_id;'''),
        ("The second route: the tier's two quarters, summed where the data lives, with no pivot", '''
SELECT o.quarter, sum(o.amount) AS spend
FROM   orders o
JOIN   customers c ON c.customer_id = o.customer_id
WHERE  c.segment = 'Retail-Plus'
GROUP  BY o.quarter
ORDER  BY o.quarter;'''),
    ]),
    "c4": ("04_three_tools", "Of the customers the sale reached, how many bought?", [
        ("The hurried version: each reached customer's segment read from their orders", '''
WITH reached AS (SELECT DISTINCT customer_id FROM campaign_exposure),
     buyers  AS (SELECT o.customer_id, min(c.segment) AS segment, count(*) AS orders
                 FROM   orders o
                 JOIN   customers c ON c.customer_id = o.customer_id
                 GROUP  BY o.customer_id)
SELECT b.segment,
       count(*)        AS reached,
       count(b.orders) AS bought
FROM   reached r
LEFT   JOIN buyers b ON b.customer_id = r.customer_id
GROUP  BY b.segment
ORDER  BY b.segment NULLS LAST;'''),
        ("The fix: each reached customer's segment read from the customer list", '''
WITH reached AS (SELECT DISTINCT customer_id FROM campaign_exposure),
     buyers  AS (SELECT customer_id, count(*) AS orders FROM orders GROUP BY customer_id)
SELECT c.segment,
       count(*)        AS reached,
       count(b.orders) AS bought
FROM   reached r
JOIN   customers c ON c.customer_id = r.customer_id
LEFT   JOIN buyers b ON b.customer_id = r.customer_id
GROUP  BY c.segment
ORDER  BY c.segment;'''),
    ]),
    "c5": ("05_finance", "Where should Finance's Monday revenue by segment and quarter be computed?", [
        ("Finance's number, computed where the data lives: eight rows come back", '''
SELECT c.segment, o.quarter, sum(o.amount) AS revenue
FROM   orders o
JOIN   customers c ON c.customer_id = o.customer_id
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;'''),
    ]),
    "c6": ("06_refresh", "Can the table rebuild itself every Monday and refuse to ship when something breaks?", [
        ("The control totals every Monday's run is checked against", '''
SELECT (SELECT count(*)        FROM customers) AS customers,
       (SELECT sum(amount)     FROM orders)    AS spend,
       (SELECT max(order_date) FROM orders)    AS last_order_loaded;'''),
        ("The second route: the win-back list, counted by the warehouse to its own last date", '''
WITH last  AS (SELECT customer_id, max(order_date) AS last_order FROM orders GROUP BY customer_id),
     as_of AS (SELECT max(order_date) AS d FROM orders)
SELECT count(*) AS win_back
FROM   last, as_of
WHERE  as_of.d - last.last_order > 60;'''),
        ("The falling flag, Wednesday's rule: less in August than in July, and less again in September, with a real month between each reading", '''
WITH monthly AS (
         SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
         FROM   orders
         GROUP  BY customer_id, date_trunc('month', order_date)),
     lagged AS (
         SELECT customer_id, month, spend,
                lag(spend, 1) OVER w AS spend_before, lag(spend, 2) OVER w AS spend_two_before,
                lag(month, 1) OVER w AS month_before, lag(month, 2) OVER w AS month_two_before
         FROM   monthly
         WINDOW w AS (PARTITION BY customer_id ORDER BY month))
SELECT count(*) AS falling
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  month_before = DATE '2026-08-01' AND month_two_before = DATE '2026-07-01'
  AND  spend < spend_before AND spend_before < spend_two_before;'''),
    ]),
    "x2": ("07_second_case", "Did Retail-Plus members order less often in Q2 than in Q1?", [
        ("Orders per member, by quarter, for Retail-Plus", '''
SELECT o.quarter,
       count(*)                    AS orders,
       count(DISTINCT o.customer_id) AS members,
       round(count(*)::numeric / count(DISTINCT o.customer_id), 3) AS orders_per_member
FROM   orders o
JOIN   customers c ON c.customer_id = o.customer_id
WHERE  c.segment = 'Retail-Plus'
GROUP  BY o.quarter
ORDER  BY o.quarter;'''),
    ]),
}


def q(key, i):
    """The text of one query, exactly as the sql/ file carries it."""
    return SQL[key][2][i][1].strip()


def write_sql():
    """Write every query to the day's sql/ folder, one file per chapter, each block commented."""
    SQLDIR.mkdir(exist_ok=True)
    for key, (stem, question, blocks) in SQL.items():
        lines = [f"-- Kalpa Retail, Week 2, Thursday. {question}",
                 "-- Runs unchanged against the Kalpa warehouse: psql -d kalpa -f <this file>.",
                 "-- The notebook of the same number runs these same queries through pandas.", ""]
        for title, text in blocks:
            lines += [f"-- {title}.", text.strip(), ""]
        (SQLDIR / f"C2_W02_D04_{stem}_STUDENT.sql").write_text("\n".join(lines), encoding="utf-8")
        print("wrote", f"sql/C2_W02_D04_{stem}_STUDENT.sql")


# ----------------------------------------------------------------------------- the frame
def mapcell(n, levels, lit=None):
    ladder = ", ".join(f'"{c}"' for c in CHAPTERS)
    steps = ", ".join(f'"{s}"' for s in levels)
    lit_arg = "" if lit is None else f", lit={lit}"
    return code(f'''kit.side_by_side(
    kit.ladder([{ladder}], lit={n - 1}, show=False),
    kit.vflow([{steps}]{lit_arg}, show=False),
)''')


def opener(n, question, ask, who, ladder, metric, company, prev):
    """The first cell: the chapter's question, the ask, who needs it, the ladder, the metric, the
    real company and what the chapter before found."""
    steps = "\n".join(f"{i}. {s}" for i, s in enumerate(ladder, start=1))
    body = "\n\n".join(textwrap.dedent(p).strip() for p in (ask, who))
    return md(f"# {n}. {question}\n\n**Week 2, Thursday. Chapter {n} of 6.** {prev}\n\n{body}\n\n"
              f"**The questions on the way.**\n\n{steps}\n\n"
              f"**The metric at stake.** {textwrap.dedent(metric).strip()}\n\n"
              f"**Who else faces it.** {textwrap.dedent(company).strip()}\n\n{DOSSIER}")


def cq(src, **subs):
    """A code cell whose @NAME@ tokens are filled after the indentation is removed, so a query
    pasted in at the left margin cannot break the dedent."""
    text = textwrap.dedent(src).strip("\n")
    for name, value in subs.items():
        text = text.replace(f"@{name}@", value)
    return code(text)


# ============================================================================= chapter 1
C1_LADDER = [
    "Which of three ways should build one row per customer, and what does each cost on 1,000 orders?",
    "Does the frame pandas reads hold every order the warehouse holds?",
    "Does one line of `groupby` give the same totals as Week 1's loop?",
    "How many customers on the list have never ordered?",
    "Does SQL, run on its own, give all 340 customers the same three numbers?",
]


def ch1():
    return [
        opener(1, "How recently, how often and how much has each of Kalpa's 340 customers bought?", ASK, '''
        **Who needs the answer.** The growth team, which decides every Monday who gets Kalpa Retail's
        offers: a win-back code for customers who have gone quiet, a first-order nudge for customers
        who signed up and never bought, and nothing for everyone else. A customer missing from the
        table gets no offer at all, and a customer counted wrongly gets the wrong one, so every
        customer has to be on the table and every number has to add back to the warehouse.
        ''', C1_LADDER, '''
        Three numbers per customer: the date of the last order (how recently), the count of orders
        (how often) and spend, the value of the orders at the prices charged, whatever became of each
        order afterwards (how much). Spend is the retail dossier's GMV at the grain of one customer, so
        the table's spend must add back to the Rs 19,84,00,000 that Monday's warehouse queries
        totalled for April to September 2026. Retailers call the three numbers RFM, for recency,
        frequency and monetary value.
        ''', '''
        Shopify builds this table for every merchant on its platform. Its customer reports score each
        customer from 1 to 5 on "the days from a customer's most recent purchase (recency), the total
        number of orders (frequency), and the total amount spent (monetary value)", and they keep the
        customers with no orders yet in a group of their own, Prospects, instead of leaving them off
        (Shopify Help Center, Customers reports, checked 1 Oct 2026).
        ''', "Monday rebuilt Week 1's revenue tree from the Kalpa warehouse: 1,000 orders over two "
             "quarters and Rs 19,84,00,000 at the prices charged. Tuesday and Wednesday worked at the "
             "grain of an order and of a customer's month. This chapter starts the growth team's table "
             "at the grain of one customer, in pandas."),
        md('''
        **Setup.** The next cell finds the shared helper `kit` by walking up from this notebook's
        folder, opens a read-only connection to the Kalpa warehouse in Postgres, and reads two tables
        into pandas: `orders`, one row per order, and `customers`, the customer list with each
        customer's segment. If the connection fails, run `bash .devcontainer/load_warehouse.sh` in the
        terminal and run the cell again.
        '''),
        code(LOAD),
        mapcell(1, ["1. the options\\nloop, SQL or pandas", "2. the frame\\n1,000 orders, pandas 3 types",
                    "3. groupby\\nWeek 1's loop in one line", "4. the trap\\nwho never ordered",
                    "5. a second route\\nSQL on its own"]),

        md('''
        ## 1. Which of three ways should build one row per customer, and what does each cost on 1,000 orders?

        Three ways a team could build the table, each sized on Kalpa's orders in the next cell.

        | Option | How it works | Rows it moves out of the warehouse | What it leaves in memory |
        |---|---|---|---|
        | a) Week 1's loop | Fetch every order as a row and add each amount to its customer's running total in a dictionary | Every order | Three dictionaries, one per number |
        | b) SQL in the warehouse | Postgres groups the orders by customer and sends back one row per customer who ordered | One per customer who ordered | The three numbers and nothing else |
        | c) pandas | Read the orders into a DataFrame, pandas' table, and split them by customer with `groupby` | Every order | The three numbers, with every order still in memory |
        '''),
        cq('''
        LOOP = """last, freq, spend = {}, {}, {}
        for o in rows:
            cid = o["customer_id"]
            last[cid] = max(last.get(cid, o["order_date"]), o["order_date"])
            freq[cid] = freq.get(cid, 0) + 1
            spend[cid] = spend.get(cid, 0) + o["amount"]"""
        SQL_B = """@SQLB@"""
        PANDAS = """rfm = (orders.groupby("customer_id")
                     .agg(last_order=("order_date", "max"), frequency=("order_id", "count"),
                          spend=("amount", "sum")))"""
        sent_b = pd.read_sql(SQL_B, ENG)          # what option b actually sends back
        sizing = [("a) Week 1's loop", len(orders), len(LOOP.splitlines()), "by hand, one dictionary at a time"),
                  ("b) SQL in the warehouse", len(sent_b), len(SQL_B.splitlines()), "a new query for every new view"),
                  ("c) pandas", len(orders), len(PANDAS.splitlines()), "in memory: merge, pivot and recount")]
        shown = [(name, f"{rows:,}", lines, then) for name, rows, lines, then in sizing]
        kit.table(["option", "rows moved", "lines of logic", "the next five chapters, done"], shown,
                  caption="Each option sized on Kalpa's orders")
        kit.bars([(name, rows) for name, rows, _, _ in sizing], lit=(2,),
                 title="Rows each option moves out of the warehouse to build the table")
        ''', SQLB=q("c1", 0)),
        md('''
        **The best-fit call: c, pandas.** The growth team's analysts work in Python, and the next five
        chapters need the orders in memory: chapter 2 attaches the monsoon sale to them, chapter 3
        turns them into months and chapter 4 counts them three ways. Moving 1,000 orders takes a
        fraction of a second. **The fact that would change it:** an orders table too large to move to
        a laptop every Monday, in the crores of rows. Then b wins, because the warehouse sends one row
        per customer whatever the size of the orders table, and pandas reads those rows instead of
        the orders.
        '''),

        md('''
        ## 2. Does the frame pandas reads hold every order the warehouse holds?

        `pd.read_sql` sends the query to Postgres and builds a DataFrame from the rows that come back,
        one column per field. Monday's first query counted 1,000 orders in the warehouse, so the frame
        has to hold 1,000 before anything built on it is trusted. The types matter as much: a date
        read as text cannot be subtracted, and an amount read as text cannot be summed.

        **Predict before you run.** What does pandas 3 report as the type of `customer_id` and of
        `amount`? a) `object` and `object`; b) `str` and `float64`; c) `str` and `int64`;
        d) `object` and `Decimal`.
        '''),
        code('''
        kit.table(["column", "type in pandas 3", "what the type allows"],
                  [("customer_id", str(orders["customer_id"].dtype), "matching and grouping by customer"),
                   ("order_date", str(orders["order_date"].dtype), "subtracting one date from another"),
                   ("amount", str(orders["amount"].dtype), "summing and averaging"),
                   ("status", str(orders["status"].dtype), "filtering by delivered, returned or cancelled")],
                  caption="What read_sql built from the warehouse's orders table")
        segments = ["Retail-Core", "Retail-Plus", "Business", "Student"]
        with_seg = orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
        per_q = with_seg.groupby(["segment", "quarter"]).size()
        kit.columns(segments, [("Q1 orders", [int(per_q[s, "Q1"]) for s in segments]),
                               ("Q2 orders", [int(per_q[s, "Q2"]) for s in segments])],
                    title="Orders read into pandas, by segment and quarter")
        '''),
        md('''
        **What happened.** The answer is b. Postgres stores `amount` as `numeric(12,2)`, which pandas
        reads as `float64`, a number it can sum. pandas 3 reads text as its own `str` type, where
        pandas 2 said `object`, so a tutorial that looks for text columns with `dtype == object` finds
        none on pandas 3. `parse_dates` made `order_date` a real date, which chapter 6 subtracts. The
        frame holds 1,000 orders, 538 in Q1 and 462 in Q2, and Retail-Plus is the segment whose orders
        fell furthest between the quarters, the frequency drop Week 1 found.
        '''),
        code('''
        in_postgres = kit.sql("SELECT count(*) AS n FROM orders")[0]["n"]
        kit.check("the frame holds every order the warehouse holds", len(orders) == in_postgres,
                  f"{len(orders):,} in pandas, {in_postgres:,} in Postgres")
        kit.check("amount arrived as a number pandas can sum", orders["amount"].dtype == "float64")
        kit.check("customer_id arrived as pandas 3's str, which is not object",
                  orders["customer_id"].dtype == "str" and orders["customer_id"].dtype != object)
        kit.check("order_date arrived as a date", pd.api.types.is_datetime64_any_dtype(orders["order_date"]))
        '''),

        md('''
        ## 3. Does one line of `groupby` give the same totals as Week 1's loop?

        In Week 1 you built spend per customer with a dictionary: start empty, visit every order, add
        its amount to that customer's running total. `groupby` makes the same three moves. It splits
        the orders into one group per customer, applies a sum to each group and combines the results
        into one row per customer, which is why the move is called split, apply, combine. The cell
        below runs the loop and the one line side by side and compares them customer by customer.

        **Predict before you run.** How many rows will spend per customer have? a) 1,000, one per
        order; b) 340, one per customer on the list; c) 301; d) 4, one per segment.
        '''),
        code('''
        spend_loop = {}                                   # Week 1's accumulator
        for row in orders.itertuples():
            spend_loop[row.customer_id] = spend_loop.get(row.customer_id, 0) + row.amount

        spend_grouped = orders.groupby("customer_id")["amount"].sum()   # the same, in one line

        kit.table(["customer_id", "the loop", "groupby"],
                  [(cid, kit.rupees(spend_loop[cid]), kit.rupees(spend_grouped[cid]))
                   for cid in spend_grouped.sort_values(ascending=False).index[:5]],
                  caption="The five largest spenders, two ways")
        kit.check("the loop and groupby agree for every customer",
                  all(spend_loop[c] == v for c, v in spend_grouped.items()), f"{len(spend_grouped)} customers")
        kit.check("both return one row per customer who ordered", len(spend_grouped) == len(spend_loop) == 301)
        '''),
        md('''
        **What happened.** The answer is c, 301 rows. `groupby` can only make a group for a customer it
        meets in the rows it was given, and the rows are orders. The loop has the same limit, since it
        only touches customers who appear in an order, and the two agree on all 301 to the rupee.

        One call can compute all three numbers at once. Each name on the left of `agg` becomes a
        column, and each pair says which column to read and what to do with it: the latest
        `order_date`, the count of `order_id` and the sum of `amount`. SQL says the same thing with
        `max`, `count` and `sum` after `GROUP BY customer_id`.
        '''),
        code('''
        rfm = (orders.groupby("customer_id")
                     .agg(last_order=("order_date", "max"), frequency=("order_id", "count"),
                          spend=("amount", "sum"))
                     .reset_index())
        bands = rfm["frequency"].clip(upper=6).value_counts().sort_index()
        kit.columns([str(k) if k < 6 else "6 or more" for k in bands.index], [("customers", bands.tolist())],
                    title="Orders per customer across two quarters, among the 301 who ordered")
        top = rfm.merge(customers, on="customer_id", validate="one_to_one").nlargest(6, "spend")
        kit.bars([(f"{r.customer_id}, {r.segment}", r.spend) for r in top.itertuples()], fmt=kit.rupees,
                 title="The six largest spenders are Business accounts, which buy in lakhs")
        '''),
        code('''
        kit.check("the three numbers came back for 301 customers", len(rfm) == 301 and
                  list(rfm.columns) == ["customer_id", "last_order", "frequency", "spend"])
        kit.check("spend adds back to the warehouse's two quarters", rfm["spend"].sum() == orders["amount"].sum(),
                  kit.rupees(rfm["spend"].sum()))
        '''),

        md('''
        ## 4. How many customers on the list have never ordered?

        The growth team's first use of the table is the first-order nudge: a welcome offer to every
        customer who signed up and never bought. The hurried analyst filters the table just built for
        a frequency of zero.

        **The plausible wrong answer.**

        **Predict before you run.** How many customers does the filter find? a) 0; b) 39; c) 301;
        d) 340.
        '''),
        code('''
        never_hurried = rfm[rfm["frequency"] == 0]
        kit.stats([(len(never_hurried), "customers who never ordered", "the hurried filter's count"),
                   (len(rfm), "rows in the table", "one per customer, or so it seems")],
                  caption="The first-order nudge list, as the hurried analyst would send it")
        '''),
        md('''
        **What happened.** The answer is a: none, and the growth team would send the welcome offer to
        nobody.

        **Why it is wrong.** The table was built from the order rows, so a customer who never ordered
        has no row in it at all, and a filter cannot find a row that is not there. The customer list
        holds 340 customers and the table holds 301. The check that catches it compares the table's
        rows with the customer list before anything is filtered.

        A half-fix makes it worse in a way that is easy to miss. Merging the three numbers onto the
        customer list brings the 39 back as rows, but their frequency arrives as a missing value,
        `NaN`, and a missing value is never equal to 0. The column's type also changes on the way,
        from whole numbers to `float64`, because pandas cannot hold a missing value in a column of
        whole numbers.
        '''),
        code('''
        half = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
        kit.table(["the table", "rows", "frequency's type", "frequency == 0", "frequency missing"],
                  [("built from the orders", len(rfm), str(rfm["frequency"].dtype),
                    int((rfm["frequency"] == 0).sum()), int(rfm["frequency"].isna().sum())),
                   ("merged onto the customer list", len(half), str(half["frequency"].dtype),
                    int((half["frequency"] == 0).sum()), int(half["frequency"].isna().sum()))],
                  caption="The count check, and the half-fix that still finds nobody")
        kit.check("the order-built table is 39 rows short of the customer list", len(customers) - len(rfm) == 39)
        kit.check("after the merge the 39 are there, and == 0 still finds none of them",
                  int(half["frequency"].isna().sum()) == 39 and int((half["frequency"] == 0).sum()) == 0)
        '''),
        md('''
        **The fix, and what changed.** The customer list is the table's spine: start from it, merge the
        three numbers on with `how="left"` so every customer stays, and say what a missing number means
        in this business. A customer with no orders has a frequency of 0 and a spend of 0, and their
        last order date stays empty, since there is no date to give. `validate="one_to_one"` makes the
        merge stop if either side ever holds a customer twice, which chapter 2 explains. The frequency
        goes back to a whole number.
        '''),
        code('''
        table = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
        table = table.assign(frequency=table["frequency"].fillna(0).astype("int64"),
                             spend=table["spend"].fillna(0))
        never = table[table["frequency"] == 0]
        by_seg = table.assign(never=table["frequency"] == 0).groupby("segment")["never"].agg(["size", "sum"])
        kit.columns(by_seg.index.tolist(), [("on the list", by_seg["size"].tolist()),
                                            ("never ordered", by_seg["sum"].astype(int).tolist())],
                    title="Every segment has customers who signed up and never ordered")
        kit.check("the table holds every customer on the list", len(table) == len(customers) == 340)
        kit.check("the first-order nudge list holds 39 customers", len(never) == 39, f"{len(never)}")
        kit.check("frequency is a whole number again", table["frequency"].dtype == "int64")
        kit.check("spend still adds back to Rs 19,84,00,000", table["spend"].sum() == 198_400_000,
                  kit.rupees(table["spend"].sum()))
        '''),
        md('''
        The nudge list moves from 0 to 39 customers: 19 in Retail-Core, 13 in Retail-Plus, 6 among the
        Students and 1 Business account. Spend does not move, since a customer who never ordered adds
        nothing to it, which is exactly why a spend check alone would not have caught the gap.

        > **Kavya's review.** "The table's spine is the customer list, never the orders. Every Monday I
        > want three numbers before the table leaves: rows against the customer list, spend against
        > the warehouse, and the count of customers who never ordered, which should never fall to zero
        > by accident."
        '''),

        md('''
        ## 5. Does SQL, run on its own, give all 340 customers the same three numbers?

        The pandas table came from `groupby`, a merge and two fills. The warehouse can build the same
        table with none of that code: a `LEFT JOIN` from the customer list to the orders, grouped by
        customer, counts each customer's orders, sums them and takes the latest date, and `coalesce`
        turns the missing sum of a customer with no orders into 0. `count(o.order_id)` counts only the
        rows that found an order, so it gives 0 where `count(*)` would give 1. If the two routes
        disagree on any customer, one of them is wrong.
        '''),
        cq('''
        SECOND = """@SQL2@"""
        by_sql = pd.read_sql(SECOND, ENG, parse_dates=["last_order"])
        both = table.merge(by_sql, on="customer_id", suffixes=("_pandas", "_sql"), validate="one_to_one")
        agree = {
            "frequency": (both["frequency_pandas"] == both["frequency_sql"]).all(),
            "spend": (both["spend_pandas"] == both["spend_sql"].astype(float)).all(),
            "last order": (both["last_order_pandas"].fillna(pd.Timestamp(0)) == both["last_order_sql"].fillna(pd.Timestamp(0))).all(),
        }
        kit.table(["number", "customers compared", "pandas and SQL agree on all"],
                  [(k, len(both), "yes" if v else "no") for k, v in agree.items()],
                  caption="The table built twice, by two routes that share no code")
        kit.bridge(("spend, SQL route", float(by_sql["spend"].sum())),
                   [("pandas route less SQL route", float(table["spend"].sum() - by_sql["spend"].sum()))],
                   end_label="spend, pandas route", title="Both routes land on Rs 19,84,00,000")
        ''', SQL2=q("c1", 1)),
        code('''
        kit.check("SQL returns one row for each of the 340 customers", len(by_sql) == 340 and len(both) == 340)
        kit.check("frequency, spend and last order agree for every customer", all(agree.values()))
        kit.check("SQL also finds 39 customers with no orders", int((by_sql["frequency"] == 0).sum()) == 39)
        '''),
        md('''
        **When to switch.** The pandas route is the one to build on, because the next five chapters
        add columns to it. The SQL route is the one to hand an auditor, because it runs in the
        warehouse and shares no code with the notebook, so a slip in the merge or in a fill cannot
        move it. Chapter 5 turns that difference into the tool-choice note.

        ### How would you answer this chapter's questions in an interview?

        **[S] Describe `groupby` in the split-apply-combine sentence.** "`groupby` splits the rows
        into one group per key, applies a calculation to each group and combines the results into
        one row per key. For a customer table: split the orders by `customer_id`, apply the latest
        date, a count and a sum, and combine one row per customer. It is SQL's `GROUP BY`, and it is
        the accumulator dictionary from a plain Python loop, written once."

        **[F] Your customer table has fewer rows than the customer list. Why, and what do you do?**
        "`groupby` only knows the keys it meets in the rows it is given, and I gave it orders, so
        customers who never ordered never formed a group. I start from the customer list, merge the
        aggregates with `how='left'` and `validate='one_to_one'`, and fill the missing count and spend
        with 0 on purpose, because a missing count is never equal to 0 and a filter would miss those
        customers."

        **[D] Design. The orders table grows to 5 crore rows. Where do you build the customer
        table?** "In the warehouse. A loop or pandas moves every order to my machine each Monday, 5
        crore rows, while `GROUP BY` sends one row per customer, however many orders there are. I
        would still read that result into pandas to merge the campaign feed and iterate. What would
        switch me back is a question that needs the order rows themselves, such as a months view,
        and then I pull only the columns and the date range it needs."

        ### Going deeper: how does pandas give every customer a share of their segment, the way a window function does?

        `agg` shrinks each group to one row, like `GROUP BY`. `transform` returns one value for every
        original row, like Wednesday's `SUM(...) OVER (PARTITION BY ...)`. Each customer's share of
        their segment's spend is one line, and the shares within a segment add up to 1.
        '''),
        code('''
        share = table.assign(share_of_segment=table["spend"] / table.groupby("segment")["spend"].transform("sum"))
        totals = share.groupby("segment")["share_of_segment"].sum().round(9)
        kit.check("every segment's shares add up to 1, as a window SUM over a partition would",
                  bool((totals == 1).all()), totals.to_dict())
        '''),
        md('''
        **The answers, question by question.**

        1. pandas builds the table, reading 1,000 orders; SQL grouping would send 301 rows, and it
           takes over when the orders run to crores.
        2. The frame holds all 1,000 orders the warehouse holds, with amounts as numbers and dates as
           dates.
        3. One line of `groupby` agrees with Week 1's loop on all 301 customers who ordered.
        4. 39 of the 340 customers never ordered; the table built from orders showed 0, because they
           had no rows.
        5. SQL, run on its own, gives all 340 customers the same last order, frequency and spend.
        '''),
        code('''
        kit.flow(["customer list\\n340 rows, the spine", "+ groupby on orders\\n301 with orders",
                  "left merge, validated\\n340 rows", "fill 0 on purpose\\n39 never ordered"], lit=3,
                 title="Chapter 1's table: every customer, three numbers each")
        kit.check_summary()
        print("Next: chapter 2 attaches the monsoon sale to these 340 rows without letting one row become two.")
        '''),
    ]


# ============================================================================= chapter 2
C2_LADDER = [
    "Which of four ways should attach the sale to the table, and what does each risk?",
    "Which customers does a merge keep when `how` is left out?",
    "What does one re-sent row do to the reached customers' spend?",
    "Which argument stops the merge before a wrong table exists?",
    "Which exposure should a customer keep, and does the table stay at 340 rows?",
    "Does a count with no merge at all give the same reach and spend?",
]

INVENTED = '''
# Invented customers and an invented feed, to show the mechanism. They are not Kalpa's.
small = pd.DataFrame({"customer_id": ["C-9001", "C-9002", "C-9003", "C-9004"],
                      "segment": ["Retail-Plus", "Retail-Core", "Retail-Plus", "Student"],
                      "spend": [12400, 8600, 5100, 1900]})
small_feed = pd.DataFrame({"customer_id": ["C-9001", "C-9002", "C-9002", "C-9003"],
                           "exposed_date": pd.to_datetime(["2026-08-03", "2026-08-03",
                                                           "2026-08-12", "2026-08-03"])})
'''


def ch2():
    return [
        opener(2, "Which customers did the monsoon sale reach, and what did the reached customers spend?", '''
        > **The client asks.** "Put the monsoon sale on the customer table. I want to see, per segment,
        > whom it reached and what they spent, because I am asking for the same budget in November."
        >
        > The marketing lead, Kalpa Retail
        ''', '''
        **Who needs the answer.** The marketing lead, who owns acquisition and campaigns and is about to
        ask for the monsoon sale's budget again for November. The sale ran in August 2026 at 15 percent
        off. If the table overstates what the reached customers spent, the case for November is made
        with money nobody paid, and the gap surfaces the day Finance ties the table back to the
        warehouse.
        ''', C2_LADDER, '''
        Reach, the number of customers the sale reached, and those customers' spend over the two
        quarters, taken from chapter 1's table. The campaign platform sends a feed of the customers it
        reached, one row per customer with the date the sale reached them, or so the platform says,
        and the table has to take the sale from that feed.
        ''', '''
        Meta, whose ads report the purchases they led to, meets the same problem in its own events. An
        advertiser can send one purchase twice, once from the Meta Pixel in the shopper's browser and
        once from its own server through the Conversions API. Meta's documentation says an advertiser
        with that setup "must set up a deduplication method" so the ad system can tell distinct events
        from overlapping ones. Under the method Meta recommends, when the same event ID and event name
        reach the same Pixel within 48 hours, Meta keeps the first copy and discards the rest (Meta for
        Developers, Handling Duplicate Pixel and Conversions API Events, checked 1 Oct 2026).
        ''', "Chapter 1 built the growth team's table from the warehouse: 340 customers, one row each, "
             "with the last order date, the count of orders and spend, which adds back to Rs 19,84,00,000; "
             "39 customers never ordered. This chapter attaches a second source to it, the campaign "
             "platform's feed."),
        md('''
        **Setup.** The next cell finds the helper, reads the orders and the customer list from the
        warehouse, rebuilds chapter 1's table in a few lines, and reads the campaign platform's feed,
        a file in the day's `data/` folder.
        '''),
        code(LOAD + TABLE + FEED),
        mapcell(2, ["1. the options\\nflag, merge, count, rule", "2. how= left out\\nwho survives",
                    "3. the trap\\none re-sent row, invented", "4. validate=\\nthe count check made loud",
                    "5. the rule\\nfirst exposure, 340 rows", "6. a second route\\nno merge at all"]),

        md('''
        ## 1. Which of four ways should attach the sale to the table, and what does each risk?

        The feed names the Retail-Core and Retail-Plus customers the sale reached. Four ways a team
        could put it on the table:

        | Option | How it works | Keeps the date the sale reached them |
        |---|---|---|
        | a) A yes-or-no flag | `isin` marks each customer whose id appears anywhere in the feed | No |
        | b) A plain merge | `merge(how="left")` on `customer_id` adds the feed's columns to each customer's row | Yes |
        | c) A merge, counted | The same merge, with the rows counted before and after, Tuesday's habit | Yes |
        | d) A rule, then a guarded merge | Keep one feed row per customer, the first date, then merge with `validate="one_to_one"`, which refuses to run if a customer appears twice | Yes |

        What separates them is what happens when the platform sends a customer twice: a flag is set
        once whatever the feed repeats, a plain merge gives that customer a second row, and so a second
        copy of their spend. The next cell sizes that risk on the table's own customers.
        '''),
        code('''
        consumer = table[table["segment"].isin(["Retail-Core", "Retail-Plus"])]
        typical, largest = consumer["spend"].median(), consumer["spend"].max()
        sizing = [("a) a yes-or-no flag", "340, always", "Rs 0", "never", "no"),
                  ("b) a plain merge", "340 plus one per re-sent row", f"{kit.rupees(typical)} to {kit.rupees(largest)}", "never", "yes"),
                  ("c) a merge, counted", "340 plus one per re-sent row", f"{kit.rupees(typical)} to {kit.rupees(largest)}", "after the table exists", "yes"),
                  ("d) a rule and a guarded merge", "340, or the run stops", "Rs 0", "before the table exists", "yes")]
        kit.table(["option", "rows out", "spend overstated per re-sent row", "the problem shows", "keeps the date"],
                  sizing, caption="Each option sized on the 270 Retail-Core and Retail-Plus customers the feed can name")
        kit.bars([("a typical customer", typical), ("the largest spender", largest)], fmt=kit.rupees,
                  title="What one re-sent row adds to the reached customers' spend under b or c")
        '''),
        md('''
        **The best-fit call: d, the rule and the guarded merge.** The marketing lead's case for November
        needs the date the sale reached each customer as well as the flag, because the next question is
        whether they bought after it, and a feed that breaks the one-row rule should stop Monday's run
        rather than inflate it. **The fact that would change it:** a table that only ever needs yes or
        no. Then a, the flag, is simpler, cannot multiply a row and needs no rule.
        '''),

        md('''
        ## 2. Which customers does a merge keep when `how` is left out?

        A merge is a join, with the same four shapes Tuesday drew in SQL.

        | SQL, Tuesday | pandas, today | What survives |
        |---|---|---|
        | `INNER JOIN` | `merge(how="inner")` | Only keys found on both sides |
        | `LEFT JOIN` | `merge(how="left")` | Every row of the left table |
        | `RIGHT JOIN` | `merge(how="right")` | Every row of the right table |
        | `FULL OUTER JOIN` | `merge(how="outer")` | Every key from either side |

        The customer table is the spine, so the merge the growth team needs is left: every customer
        stays, and the feed adds a date where it has one.

        **Predict before you run.** `merge` with no `how` keeps which customers? a) every customer on
        the table; b) only the customers the feed names, since the default is inner; c) every row of
        the feed, even customers the table does not know; d) none, because `how` is required.
        '''),
        code('''
        inner = table.merge(exposure, on="customer_id")           # how= left out
        kept = inner["customer_id"].nunique()
        named = inner.drop_duplicates("customer_id").groupby("segment").size()
        kit.columns(named.index.tolist(), [("customers the default merge keeps", named.tolist())],
                    title="The default merge keeps only the Retail-Core and Retail-Plus customers the feed names")
        kit.check("the default merge keeps only customers the feed names",
                  kept == exposure["customer_id"].nunique(), f"{kept} of {len(table)} customers")
        kit.check("every customer the feed names is on the table", exposure["customer_id"].isin(table["customer_id"]).all())
        '''),
        md('''
        **What happened.** The answer is b. `merge` defaults to an inner join, so it drops every
        customer the sale did not reach, 210 of the 340, and the unreached are exactly the comparison
        the marketing lead's case needs. Write `how=` on every merge, so the reader of the code knows
        which rows survive.
        '''),

        md('''
        ## 3. What does one re-sent row do to the reached customers' spend?

        The campaign platform sends its feed in batches, and a batch sent again brings its customers
        twice. The mechanism shows best on a handful of rows. **These four customers and their feed are
        invented for the mechanism; they are not Kalpa's.**
        '''),
        code(INVENTED + textwrap.dedent('''
        kit.side_by_side(
            kit.flow(["C-9001\\nRs 12,400", "C-9002\\nRs 8,600", "C-9003\\nRs 5,100", "C-9004\\nRs 1,900"],
                     title="Invented customers: 4 rows", show=False),
            kit.flow(["C-9001\\n3 Aug", "C-9002\\n3 Aug", "C-9002\\n12 Aug, sent again", "C-9003\\n3 Aug"],
                     kinds=[None, None, "bad", None], title="Invented feed: 4 rows, 3 customers", show=False),
        )
        ''')),
        md('''
        **The plausible wrong answer.** The analyst merges, keeps the customers the sale reached, and
        sums their spend for the marketing lead's slide.

        **Predict before you run.** What does the slide say the reached customers spent?
        a) Rs 26,100; b) Rs 28,000; c) Rs 34,700; d) Rs 17,200.
        '''),
        code('''
        naive = small.merge(small_feed, on="customer_id", how="left")
        wrong_spend = int(naive.loc[naive["exposed_date"].notna(), "spend"].sum())
        kit.table(["customer_id", "spend", "exposed_date"],
                  [(r.customer_id, kit.rupees(r.spend), "" if pd.isna(r.exposed_date) else str(r.exposed_date.date()))
                   for r in naive.itertuples()], caption=f"{len(small)} customers in, {len(naive)} rows out")
        kit.stats([(kit.rupees(wrong_spend), "spend of reached customers", "what the slide would say"),
                   (len(naive), "rows after the merge", "from 4 customers")])
        '''),
        md('''
        **What happened.** The answer is c, Rs 34,700.

        **Why it is wrong.** C-9002 appears twice in the feed, so the merge gives C-9002 two rows and
        the sum counts its Rs 8,600 twice. Every row looks right on its own, which is why reading the
        table never catches it. The slide overstates what the reached customers spent by a third, and
        the case for November rests on money nobody paid. The check that catches it is Tuesday's: four
        customers went in and five rows came out.
        '''),
        code('''
        right_spend = int(small.loc[small["customer_id"].isin(small_feed["customer_id"]), "spend"].sum())
        kit.check("the count check: rows grew from 4 to 5", len(small) == 4 and len(naive) == 5)
        kit.check("the reached customers truly spent Rs 26,100", right_spend == 26100, kit.rupees(right_spend))
        kit.check("the slide's excess is exactly C-9002's spend", wrong_spend - right_spend == 8600)
        '''),

        md('''
        ## 4. Which argument stops the merge before a wrong table exists?

        The count check reports the problem after the wrong table exists. `validate` states what the
        merge promises and raises an error the moment the data breaks the promise, before any table is
        built. `"one_to_one"` promises each key once on both sides, `"many_to_one"` allows repeats on
        the left but none on the right, and `"one_to_many"` the reverse.

        **Predict before you run.** Which argument stops the invented merge? a) `how="left"`;
        b) `validate="one_to_one"`; c) `indicator=True`; d) `sort=True`.
        '''),
        code('''
        with kit.expect_error() as err:
            small.merge(small_feed, on="customer_id", how="left", validate="one_to_one")
        kit.bridge(("reached, counted once", right_spend), [("C-9002 counted again", wrong_spend - right_spend)],
                   end_label="what the slide said", lit=(0,),
                   title="Invented records: one re-sent row adds a customer's whole spend again")
        kit.check("validate='one_to_one' raises pandas.errors.MergeError", err.name == "MergeError",
                  err.message.splitlines()[0])
        kit.check("the error names the right-hand side, the feed", "not unique in right dataset" in err.message)
        '''),
        md('''
        **What happened.** The answer is b. The merge stops with `pandas.errors.MergeError`, whose first
        line reads *Merge keys are not unique in right dataset; not a one-to-one merge*; pandas 3.0.6
        then lists the repeated keys beneath it. It is the row-count check made loud: nothing wrong is
        built, so nothing wrong can be sent.

        **Your turn, on Kalpa's feed, five minutes.** Type these lines into the empty cell and read each
        answer aloud before you run the next.

        ```python
        len(exposure), exposure["customer_id"].nunique()
        len(table), len(table.merge(exposure, on="customer_id", how="left"))
        table.merge(exposure, on="customer_id", how="left", validate="one_to_one")
        ```

        Then say, in one sentence to the marketing lead, what a plain merge would have done to the
        reached customers' spend, and by how many rupees.
        '''),
        empty(),

        md('''
        ## 5. Which exposure should a customer keep, and does the table stay at 340 rows?

        A repeated customer is a business question before it is a pandas one: a customer the sale
        reached twice was still reached. The rule for this table is one row per customer, the date the
        sale first reached them. Sort the feed by date, keep each customer's first row, and merge with
        `validate="one_to_one"`, so a feed that ever breaks the rule stops Monday's refresh instead of
        inflating it.

        **Predict before you run.** After sorting by date, which argument keeps each customer's first
        exposure? a) `keep="last"`; b) `keep=False`; c) `keep="first"`; d) none, since the merge
        ignores repeats.
        '''),
        code('''
        first_touch = (exposure.sort_values("exposed_date")
                               .drop_duplicates("customer_id", keep="first")[["customer_id", "exposed_date"]])
        with kit.expect_error() as clean:
            merged = table.merge(first_touch, on="customer_id", how="left", validate="one_to_one")
        merged = merged.assign(reached=merged["exposed_date"].notna())
        kit.check("the guarded merge runs once the rule is applied", clean.name is None)
        kit.check("340 rows in, 340 rows out", len(merged) == len(table) == 340)
        kit.check("spend did not move: Rs 19,84,00,000 before and after",
                  merged["spend"].sum() == table["spend"].sum(), kit.rupees(merged["spend"].sum()))
        kit.check("every customer the feed names is marked reached, once",
                  int(merged["reached"].sum()) == exposure["customer_id"].nunique(), int(merged["reached"].sum()))
        '''),
        md('''
        **What happened.** The answer is c. `keep="last"` would keep a later date wherever a customer
        repeats, and `keep=False` drops every copy of a repeated customer, so a customer the platform
        sent twice would read as never reached. The table stays at 340 rows, spend stays at
        Rs 19,84,00,000, and 130 customers carry the date the sale first reached them.
        '''),
        code('''
        reached = merged[merged["reached"]]
        per_seg = merged.groupby("segment")["reached"].sum().astype(int)
        kit.stats([(int(merged["reached"].sum()), "customers reached", "one row each"),
                   (kit.rupees(reached["spend"].sum()), "their spend", "two quarters, at the prices charged"),
                   (int((~merged["reached"]).sum()), "not reached", "the comparison group")])
        cons = merged[merged["segment"].isin(["Retail-Core", "Retail-Plus"])]
        avg = cons.groupby(["segment", "reached"])["spend"].mean().unstack()
        kit.columns(avg.index.tolist(), [("not reached", avg[False].round(0).tolist()),
                                         ("reached", avg[True].round(0).tolist())], fmt=kit.rupees,
                    title="Average two-quarter spend per customer, reached or not")
        '''),
        md('''
        **What the chart does not say.** Reached Retail-Plus customers spent more on average than the
        members the sale missed, and reached Retail-Core customers a little less. Week 1 Thursday found
        that the customers the monsoon sale reached skewed towards those who were buying anyway, so an
        average among the reached says who was chosen before it says what the sale did. The table
        records whom the sale reached; whether it changed their spending is a separate question with a
        separate test.

        > **Kavya's review.** "A merge is a join, so I want Tuesday's two numbers before this table goes
        > to Marketing: 340 rows in and 340 out, and Rs 19,84,00,000 before and after. A merge that
        > moves either is wrong until you can say why, and the rule you chose goes in writing beside
        > the table."
        '''),

        md('''
        ## 6. Does a count with no merge at all give the same reach and spend?

        The reach and the reached spend came from a sorted feed, a rule and a merge. Two routes share
        none of that code. `isin` marks each customer whose id appears anywhere in the feed, and a flag
        cannot multiply a row. The warehouse keeps its own copy of the feed, `campaign_exposure`: it
        counts the distinct customers in it, and it sums the orders of customers `IN` it, and `IN` only
        asks whether a customer is there, however often.
        '''),
        cq('''
        flag = table["customer_id"].isin(exposure["customer_id"])
        REACHED = """@R1@"""
        SPEND = """@R2@"""
        sql_reached = int(kit.sql(REACHED)[0]["reached"])
        sql_spend = float(kit.sql(SPEND)[0]["reached_spend"])
        routes = [("the rule and the merge", int(merged["reached"].sum()), float(reached["spend"].sum())),
                  ("the isin flag", int(flag.sum()), float(table.loc[flag, "spend"].sum())),
                  ("SQL in the warehouse", sql_reached, sql_spend)]
        kit.table(["route", "customers reached", "their spend"],
                  [(name, n, kit.rupees(s)) for name, n, s in routes], caption="Reach and spend, three ways")
        kit.bars([(name, s) for name, _, s in routes], fmt=kit.rupees,
                 title="The reached customers' spend lands on the same number three ways")
        ''', R1=q("c2", 0), R2=q("c2", 1)),
        code('''
        kit.check("the flag and the merge reach the same 130 customers", routes[0][1] == routes[1][1] == 130)
        kit.check("SQL reaches the same customers", sql_reached == routes[0][1])
        kit.check("all three routes agree on the reached customers' spend",
                  routes[0][2] == routes[1][2] == routes[2][2], kit.rupees(routes[0][2]))
        '''),
        md('''
        **When to switch.** The rule and the guarded merge are the route for the table, because the
        date rides along with the customer. `isin` is the route whenever the question is only yes or
        no. The SQL is the route for anyone who wants the number without the notebook, such as Finance
        checking the marketing lead's slide.

        ### How would you answer this chapter's questions in an interview?

        **[S] Merge against join: what is the same and what differs?** "The same: both match rows on a
        key, both come in inner, left, right and outer, and both multiply rows when a key repeats on
        the side you did not expect. The differences: pandas defaults to inner, so I always write
        `how=`; pandas runs in memory on data I have already pulled, where the warehouse joins where
        the data lives; and pandas can refuse the wrong shape with `validate=`, which SQL has no single
        argument for."

        **[F] Which merge argument raises on duplicate keys, and which error does it raise?**
        "`validate`, set to `one_to_one`, `one_to_many` or `many_to_one`. When the keys break the
        promise it raises `pandas.errors.MergeError`, naming the side whose keys are not unique. It is
        the row-count check made loud: it stops the table being built instead of reporting afterwards."

        **[F] Your Monday refresh stopped with a `MergeError`. What do you do?** "I do not delete the
        repeats to make it pass. I read the repeated keys, find out why the source sent them, apply a
        business rule, here the first exposure per customer, and keep `validate` on so the next
        surprise also stops the run. Then I tell the owner of the feed."

        ### Going deeper: how does pandas list the customers on one side only, the way Tuesday's anti-join did?

        Tuesday's anti-join, rows on one side with no match on the other, is one argument in pandas:
        `indicator=True` adds a `_merge` column saying where each row came from.
        '''),
        code('''
        sides = table.merge(first_touch, on="customer_id", how="outer", indicator=True, validate="one_to_one")
        counts = sides["_merge"].value_counts()
        kit.table(["_merge", "customers", "reads as"],
                  [("both", int(counts.get("both", 0)), "on the list, and reached"),
                   ("left_only", int(counts.get("left_only", 0)), "on the list, never reached"),
                   ("right_only", int(counts.get("right_only", 0)), "in the feed, unknown to the list")],
                  caption="indicator=True on an outer merge of the list and the first-touch feed")
        kit.check("no customer in the feed is unknown to the warehouse", int(counts.get("right_only", 0)) == 0)
        '''),
        md('''
        **The answers, question by question.**

        1. The rule and a guarded merge attach the sale: it keeps the date and stops on a repeat, where
           a plain merge overstates spend by a customer's whole spend for every re-sent row.
        2. With `how` left out, the merge keeps only the 130 customers the feed names and drops the 210
           the sale missed.
        3. One re-sent row made the invented slide say Rs 34,700 where the reached customers spent
           Rs 26,100.
        4. `validate="one_to_one"` stops the merge with a `MergeError` before a wrong table exists.
        5. Each customer keeps their first exposure; the table stays at 340 rows and Rs 19,84,00,000,
           with 130 customers reached.
        6. The flag, the merge and the warehouse agree: 130 customers reached, who spent Rs 8,78,980.
        '''),
        code('''
        kit.flow(["customer table\\n340 rows", "first exposure per customer\\nthe rule",
                  "merge, validate one_to_one\\n340 rows out", "reached flag\\n130 customers"], lit=2,
                 title="The exposure merge, as it runs every Monday")
        kit.check_summary()
        print("Next: chapter 3 turns the orders into months, for the head of Retail-Plus.")
        '''),
    ]


# ============================================================================= chapter 3
C3_LADDER = [
    "Which of three shapes should answer the head of Retail-Plus, and what does each cost?",
    "In how many member-months did Retail-Plus actually buy?",
    "How far did the tier fall, read from a one-line pivot?",
    "What does one row of the pivot stand for?",
    "Which shape compares a member's quarters, and which follows the tier's trend?",
    "Does a query that never pivots give the same fall?",
]

MONTHS_SETUP = '''
orders = orders.assign(month=orders["order_date"].dt.to_period("M").astype(str))
plus = (orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
              .query("segment == 'Retail-Plus'"))
MONTHS = sorted(orders["month"].unique())
print(f"{len(plus)} Retail-Plus orders from {plus['customer_id'].nunique()} members, {MONTHS[0]} to {MONTHS[-1]}")
'''


def ch3():
    return [
        opener(3, "How far did Retail-Plus members' spend fall from Q1 to Q2, month by month?", '''
        > **The client asks.** "Give me one row per member and one column per month. I want to read
        > along a row and see who is drifting, and I want the tier's fall from Q1 to Q2 in one number
        > I can take to the growth review."
        >
        > The head of Retail-Plus, Kalpa Retail
        ''', '''
        **Who needs the answer.** The head of Retail-Plus, Kalpa's paid membership tier, who takes one
        number to the growth review and uses the rows to decide which members to protect. A number
        that is too small argues the tier's problem down to a fraction of its size, and rows that
        stand for the wrong thing protect the wrong members while the right ones lapse.
        ''', C3_LADDER, '''
        Retail-Plus spend by month, April to September 2026, and the change in the tier's spend from
        Q1, April to June, to Q2, July to September. A month's spend is every order the member placed
        in it, at the prices charged, added up.
        ''', '''
        Costco, whose business rests on paid memberships, reports its sales in the two parts this
        chapter has to keep apart. On the call for its fourth quarter of fiscal 2026, its chief
        financial officer reported that "traffic or shopping frequency increased 3.3% worldwide" and
        that "our average transaction or ticket was up 5.9% worldwide": how often members shop, and
        what each trip is worth, as two numbers (Costco's earnings call and the supplemental information
        it filed with the SEC, both 24 Sep 2026, checked 1 Oct 2026). The same call put the renewal rate in the
        US and Canada at 92.3 percent, the number the head of a paid tier watches first.
        ''', "Chapter 2 put the monsoon sale on the growth team's table: 130 customers reached, one row "
             "each, and the table still 340 rows and Rs 19,84,00,000. Week 1 found that Retail-Plus "
             "members ordered less often in Q2 than in Q1. This chapter turns their orders into months "
             "for the head of the tier."),
        md('''
        **Setup.** The next cell reads the orders and the customer list from the warehouse, labels
        every order with its month, and keeps the Retail-Plus members' orders.
        '''),
        code(LOAD + MONTHS_SETUP),
        mapcell(3, ["1. the options\\nlong, wide, or a query", "2. the long table\\nmember and month",
                    "3. the trap\\na one-line pivot", "4. the index\\nwhat one row is",
                    "5. compare or follow\\nwide and long", "6. a second route\\nno pivot at all"]),

        md('''
        ## 1. Which of three shapes should answer the head of Retail-Plus, and what does each cost?

        | Option | Shape | What it answers directly |
        |---|---|---|
        | a) The long table | One row per member per month with orders: `groupby(["customer_id", "month"])` | How the tier moves from month to month, a trend |
        | b) The wide table | One row per member, one column per month: `pivot_table`, which turns the values of one column into columns | How a member's months compare, read along a row |
        | c) A query per month | SQL with one column per month, each written out by hand with `FILTER` | The wide table, straight from the warehouse |

        The next cell sizes each on the Retail-Plus orders: the rows and cells it holds, the empty cells
        it carries, and what adding October would cost.
        '''),
        cq('''
        long_ = plus.groupby(["customer_id", "month"], as_index=False)["amount"].sum()
        members = plus["customer_id"].nunique()
        BY_MONTH = """@SQLC@"""
        sent_c = pd.read_sql(BY_MONTH, ENG)
        sizing = [("a) the long table", f"{len(long_)} rows by 3", len(long_) * 3, 0, "nothing"),
                  ("b) the wide table", f"{members} rows by 6", members * 6, members * 6 - len(long_), "nothing"),
                  ("c) a query per month", f"{len(sent_c)} rows by 7", len(sent_c) * 7, int(sent_c.isna().sum().sum()),
                   "a new FILTER line, typed by hand")]
        kit.table(["option", "shape", "cells", "empty cells", "adding October costs"], sizing,
                  caption="Each shape sized on the 355 Retail-Plus orders")
        kit.bars([(name, cells) for name, _, cells, _, _ in sizing], lit=(0, 1),
                 title="Cells each shape holds for the same 355 orders")
        ''', SQLC=q("c3", 0)),
        md('''
        **The best-fit call: a and b together, in pandas.** The long table keeps every rupee in 266
        rows and is the easiest to group and plot; the wide table is the one the head of Retail-Plus
        reads along a row, and its 376 empty cells are member-months with no order. The query per month
        builds the wide table too, but it fixes the six months in its text, so every new month is an
        edit and a place for a typo. **The fact that would change it:** the view moving into the
        warehouse to run every Monday for Finance. Then c returns, with a calendar table of months,
        Wednesday's idea, in place of the hand-written columns.
        '''),

        md('''
        ## 2. In how many member-months did Retail-Plus actually buy?

        Before any pivot, the grain the head of Retail-Plus asked about is member and month. Two keys
        in the `groupby` give one row for each member and month that actually has orders, with that
        month's orders added up.

        **Predict before you run.** How many rows does the long table have? a) 355, one per order;
        b) 642, 107 members times 6 months; c) 266; d) 107, one per member.
        '''),
        code('''
        tier = long_.groupby("month")["amount"].sum()
        kit.line(MONTHS, [("Retail-Plus spend", tier.tolist(), "lit")], fmt=kit.rupees,
                 title="Retail-Plus spend by month, April to September 2026, every order added up")
        kit.table(["customer_id", "month", "amount"],
                  [(r.customer_id, r.month, kit.rupees(r.amount)) for r in long_.head(5).itertuples()],
                  caption="The long table's first rows: one member, one month, that month's orders added")
        '''),
        code('''
        q1, q2 = tier[MONTHS[:3]].sum(), tier[MONTHS[3:]].sum()
        kit.check("the long table keeps every rupee", long_["amount"].sum() == plus["amount"].sum(),
                  kit.rupees(long_["amount"].sum()))
        kit.check("one row per member-month that has orders", len(long_) == 266, f"{len(long_)} rows")
        kit.check("the tier took Rs 5,85,770 in Q1 and Rs 4,13,380 in Q2", q1 == 585770 and q2 == 413380,
                  f"{kit.rupees(q1)} and {kit.rupees(q2)}")
        '''),
        md('''
        **What happened.** The answer is c, 266 rows. A member-month with no order has no row at all, so
        the long table is shorter than 107 members times 6 months, and the 13 Retail-Plus members who
        never ordered, chapter 1's never-ordered customers, are in no row. The line is the number to
        hold on to: the tier took Rs 5,85,770 in Q1 and Rs 4,13,380 in Q2.
        '''),

        md('''
        ## 3. How far did the tier fall, read from a one-line pivot?

        **The plausible wrong answer.** The analyst asks for months as columns in one line, members as
        rows, amounts in the cells, then adds up each month's column for the tier's monthly spend.

        **Predict before you run.** What fall from Q1 to Q2 does that pivot report? a) 29 percent;
        b) 18 percent; c) 0 percent; d) it raises an error.
        '''),
        code('''
        wide_wrong = plus.pivot_table(index="customer_id", columns="month", values="amount")
        col_wrong = wide_wrong.sum()
        q1_w, q2_w = col_wrong[MONTHS[:3]].sum(), col_wrong[MONTHS[3:]].sum()
        kit.stats([(kit.rupees(round(q1_w)), "Q1, from the pivot", "April to June"),
                   (kit.rupees(round(q2_w)), "Q2, from the pivot", "July to September"),
                   (f"{q2_w / q1_w - 1:.0%}", "the change it reports", "what the review would hear")])
        '''),
        md('''
        **What happened.** The answer is b, a fall of 18 percent.

        **Why it is wrong.** `pivot_table` has to put one number in each cell, and when a member placed
        several orders in a month it combines them with its default, which is the mean. A member who
        ordered four times in June shows the average of the four, and the column sums add up
        averages. An average order hides how often members bought, and how often is the lever Week 1
        found moving in Retail-Plus. The head of Retail-Plus would walk into the review defending a
        fall well under two-thirds of its real size. The check that catches it: a pivot of spend must
        hold the same total as the orders it came from.
        '''),
        code('''
        grand_wrong = wide_wrong.sum().sum()
        member = "C-0152"
        row = [(m, int((plus["customer_id"].eq(member) & plus["month"].eq(m)).sum()),
                "" if pd.isna(wide_wrong.loc[member, m]) else f"Rs {wide_wrong.loc[member, m]:,.2f}",
                kit.rupees(plus.loc[plus["customer_id"].eq(member) & plus["month"].eq(m), "amount"].sum()))
               for m in MONTHS]
        kit.table(["month", "orders", "the pivot shows", "the member spent"], row,
                  caption=f"One member, {member}, read along the row")
        kit.bars([("the orders, added", plus["amount"].sum()), ("the pivot's grand total", round(grand_wrong))],
                 fmt=kit.rupees, lit=(1,), title="The grand-total check: the pivot is short by a quarter")
        kit.check("the default pivot does not add back to the orders", round(grand_wrong) != plus["amount"].sum(),
                  f"{kit.rupees(round(grand_wrong))} against {kit.rupees(plus['amount'].sum())}")
        june = plus.loc[plus["customer_id"].eq(member) & plus["month"].eq("2026-06"), "amount"]
        kit.check("in June the pivot shows the member's average order, a quarter of the month's spend",
                  len(june) == 4 and wide_wrong.loc[member, "2026-06"] * 4 == june.sum())
        '''),
        md('''
        **The fix, and what changed.** Say what a cell means. `aggfunc="sum"` adds a member's orders in
        the month, and `fill_value=0` writes a month with no orders as 0 spend instead of a gap. The
        tier's fall moves from 18 percent to 29 percent, and in rupees from Rs 74,752 to Rs 1,72,390.
        '''),
        code('''
        wide = plus.pivot_table(index="customer_id", columns="month", values="amount", aggfunc="sum", fill_value=0)
        col = wide.sum()
        q1_s, q2_s = col[MONTHS[:3]].sum(), col[MONTHS[3:]].sum()
        kit.line(MONTHS, [("summed, the true monthly spend", col.tolist(), "lit"),
                          ("averaged, the default", col_wrong.round(0).tolist(), "bad")], fmt=kit.rupees,
                 title="The same months, two aggfuncs: the default hides a quarter of the spend")
        fall_w = round(q1_w) - round(q2_w)                 # the fall the averaged pivot reports, in whole rupees
        kit.bridge(("fall, averaged pivot", fall_w), [("fall the average hid", round(q1_s - q2_s) - fall_w)],
                   end_label="fall, summed pivot", lit=(0,),
                   title="The fall from Q1 to Q2 in rupees: the averaged pivot shows well under half of it")
        kit.check("the summed pivot adds back to every Retail-Plus order", wide.values.sum() == plus["amount"].sum(),
                  kit.rupees(wide.values.sum()))
        kit.check("the true fall from Q1 to Q2 is 29.4 percent", round(q2_s / q1_s - 1, 3) == -0.294, f"{q2_s / q1_s - 1:.1%}")
        '''),
        md('''
        > **Kavya's review.** "Q1 Rs 5,85,770, Q2 Rs 4,13,380, a fall of 29 percent, from a pivot whose
        > grand total equals the orders. The averaged pivot would have told the review 18. Write
        > `aggfunc=` on every pivot, the way you write `how=` on every merge."

        **Your turn, three minutes.** Kavya asks for the same view of the Retail-Core segment.
        In the empty cell, build it with `aggfunc="sum"` and `fill_value=0` from the orders of
        segment `Retail-Core`, check its grand total against those orders before you read a single
        month, then say the Q1 to Q2 change aloud and whether the averaged pivot even gets its
        direction right.
        '''),
        empty(),

        md('''
        ## 4. What does one row of the pivot stand for?

        The index decides what one row is. Index the pivot by `order_id` and every order becomes a row:
        a table of orders with five empty cells in each, which looks like a months view until someone
        reads the row labels aloud.

        **Predict before you run.** What shape is the pivot indexed by `order_id`? a) 107 rows by 6
        columns; b) 355 rows by 6 columns; c) 6 rows by 107 columns; d) 120 rows by 6 columns.
        '''),
        code('''
        by_order = plus.pivot_table(index="order_id", columns="month", values="amount", aggfunc="sum")
        kit.table(["index", "shape", "first row label", "one row is"],
                  [("customer_id", str(wide.shape), wide.index[0], "a member"),
                   ("order_id", str(by_order.shape), by_order.index[0], "an order")],
                  caption="Read the row labels aloud before reading any number")
        kit.columns(["members on the list", "members who ordered", "rows under the order index"],
                    [("rows", [int((customers["segment"] == "Retail-Plus").sum()), len(wide), len(by_order)])],
                    title="Three row counts, and only one answers the head of Retail-Plus")
        kit.check("the member view has one row per member who ordered", len(wide) == plus["customer_id"].nunique() == 107)
        kit.check("the order-indexed pivot has one row per order", len(by_order) == len(plus) == 355)
        kit.check("its total is right, which is why it survives a glance", by_order.sum().sum() == plus["amount"].sum())
        '''),
        md('''
        **What happened.** The answer is b, 355 rows, one per Retail-Plus order. Its totals are right,
        which is why it survives a glance, but its rows are orders, so "who is drifting" cannot be read
        from it at all. The member view has 107 rows. The 13 members on the list who never ordered are
        in neither view, which is a decision to state when the view goes to the head of Retail-Plus.
        '''),

        md('''
        ## 5. Which shape compares a member's quarters, and which follows the tier's trend?

        Months as columns answer a comparison: did this member spend less in Q2 than in Q1? Months as
        rows answer a trend, and `melt` folds the wide table back into long, one row per member per
        month, zeros included, which is the shape a chart of the months needs.

        **Predict before you run.** How many rows does `melt` give from the 107-by-6 wide table?
        a) 266, as the long table had; b) 642; c) 107; d) 6.
        '''),
        code('''
        q = wide.assign(Q1=wide[MONTHS[:3]].sum(axis=1), Q2=wide[MONTHS[3:]].sum(axis=1))
        fell, rose = int((q["Q2"] < q["Q1"]).sum()), int((q["Q2"] > q["Q1"]).sum())
        kit.table(["customer_id", "Q1", "Q2", "change"],
                  [(cid, kit.rupees(r.Q1), kit.rupees(r.Q2), kit.rupees(r.Q2 - r.Q1))
                   for cid, r in q.sort_values("Q1", ascending=False).head(5).iterrows()],
                  caption="The comparison view: the five largest Q1 members, their quarters side by side")
        back = wide.reset_index().melt(id_vars="customer_id", var_name="month", value_name="spend")
        buying = back[back["spend"] > 0].groupby("month")["customer_id"].nunique()
        kit.line(MONTHS, [("members who ordered that month", buying.tolist(), "lit")],
                 title="The trend view, from the melted table: fewer members order each month")
        '''),
        code('''
        kit.check("melt gives 107 members times 6 months", len(back) == 107 * 6, f"{len(back)} rows")
        kit.check("melt keeps every rupee", back["spend"].sum() == plus["amount"].sum())
        kit.check("67 members spent less in Q2 than in Q1, and 40 spent more", fell == 67 and rose == 40)
        '''),
        md('''
        **What happened.** The answer is b, 642 rows, because the wide table held a 0 for every month a
        member did not order and `melt` keeps them. The comparison view shows 67 of 107 members spending
        less in Q2 than in Q1, and the trend view shows the members who ordered each month falling from
        56 in April to 37 in September: how often, again.
        '''),

        md('''
        ## 6. Does a query that never pivots give the same fall?

        The fall came from a pivot's columns. The warehouse can reach the tier's two quarters with no
        pivot and no months at all: join each order to its customer, keep Retail-Plus, and add up each
        quarter. If this route disagrees with the pivot, one of them is wrong.
        '''),
        cq('''
        QUARTERS = """@SQL6@"""
        by_sql = {r["quarter"]: float(r["spend"]) for r in kit.sql(QUARTERS)}
        kit.columns(["Q1", "Q2"], [("summed pivot", [q1_s, q2_s]), ("SQL, no pivot", [by_sql["Q1"], by_sql["Q2"]])],
                    fmt=kit.rupees, title="The tier's two quarters, reached two ways")
        kit.check("SQL and the summed pivot agree on Q1", by_sql["Q1"] == q1_s, kit.rupees(by_sql["Q1"]))
        kit.check("SQL and the summed pivot agree on Q2", by_sql["Q2"] == q2_s, kit.rupees(by_sql["Q2"]))
        kit.check("both give a fall of 29.4 percent", round(by_sql["Q2"] / by_sql["Q1"] - 1, 3) == -0.294)
        ''', SQL6=q("c3", 1)),
        md('''
        **When to switch.** The pivot is the route for the head of Retail-Plus's rows, since it keeps
        each member's months. The quarter query is the route for the one number, and the route to
        trust when the pivot's arguments are in doubt: it has no `aggfunc` to forget.

        ### How would you answer this chapter's questions in an interview?

        **[F] Pivot against melt: which widens and which lengthens?** "`pivot` and `pivot_table`
        widen: the values of one column become new columns, so a long table of member and month becomes
        one row per member with a column per month. `melt` lengthens: it folds columns back into rows,
        one row per member per month. I pivot to compare along a row and melt to plot or group a trend."

        **[F] Your pivot's totals look low. Where do you look first?** "At `aggfunc`. `pivot_table`
        averages by default, so where the cells should be totals I pass `aggfunc='sum'`, and I check
        the pivot's grand total against the source before I read a single cell."

        **[S] Pivot or pivot_table?** "`pivot` only reshapes, so it raises an error when a row and
        column pair repeats; `pivot_table` combines the repeats, with the mean unless told otherwise.
        When I expect one value per cell, `pivot` is the loud check."

        ### Going deeper: when does `pivot` refuse where `pivot_table` averages?
        '''),
        code('''
        with kit.expect_error() as loud:
            plus.pivot(index="customer_id", columns="month", values="amount")
        kit.check("pivot refuses to reshape when a member has two orders in a month",
                  loud.name == "ValueError" and "duplicate entries" in loud.message, loud.message)
        '''),
        md('''
        **The answers, question by question.**

        1. The long table and the wide table together answer the head of Retail-Plus; a query per month
           would fix six months in its text.
        2. Retail-Plus bought in 266 member-months, Rs 5,85,770 in Q1 and Rs 4,13,380 in Q2.
        3. The one-line pivot reported a fall of 18 percent, because it averaged; summed, the fall is
           29.4 percent, Rs 1,72,390.
        4. One row of the member pivot is a member, 107 of them; indexed by order it is an order, 355.
        5. The wide table compares, with 67 members spending less in Q2; the long table follows, with
           members ordering each month falling from 56 to 37.
        6. The warehouse, with no pivot, gives the same two quarters and the same fall of 29.4 percent.
        '''),
        code('''
        kit.flow(["long\\n266 member-months", "pivot_table, aggfunc='sum'\\n107 by 6",
                  "grand total = orders\\nRs 9,99,150", "melt\\n642 rows"], lit=1,
                 title="The months view, with the aggregation said out loud")
        kit.check_summary()
        print("Next: chapter 4 asks one question in plain Python, SQL and pandas, and checks whether they agree.")
        '''),
    ]


# ============================================================================= chapter 4
C4_LADDER = [
    "Which tool should answer the marketing lead's question, and what does each cost on this data?",
    "What does plain Python count, with a set of reached customers and a dictionary of segments?",
    "What does SQL say when it groups the same customers by segment?",
    "Why does pandas report that every reached customer bought?",
    "Where should the segment come from, so that all three tools agree?",
    "Does counting sets, with no grouping at all, find the same customers who never bought?",
]


def ch4():
    return [
        opener(4, "Of the 130 customers the sale reached, how many bought, and do plain Python, SQL and pandas agree?", '''
        > **The client asks.** "You did the tree in plain Python in Week 1 and in SQL on Monday. Take
        > the marketing lead's next question, how many of the customers the sale reached went on to
        > buy, and answer it three ways. Then tell me why the three agree, or why they do not."
        >
        > Kavya Nair, senior analyst, Kalpa Retail data team
        ''', '''
        **Who needs the answer.** The marketing lead, through Kavya. The share of reached customers
        who bought is the second line of the November budget case, after the reach itself. A share that
        leaves out the reached customers who never bought makes the sale look perfect, and Kavya will
        not let a number reach Marketing until two tools that share no code agree on it.
        ''', C4_LADDER, '''
        The share of reached customers who bought, by segment: reached customers with at least one
        order in the two quarters, over reached customers. It says who bought at some point; whether
        they bought because of the sale is Week 1 Thursday's question. The 130 reached customers are
        chapter 2's, one row each.
        ''', '''
        Uber found one metric giving different answers in different tools. Its engineering blog
        describes the Operations team computing completed trips as a Presto/Hive SQL query for daily
        dashboards while the Pricing Engineering team built its own completed-trips metric from a
        Cassandra table for real-time services, and it names the goal Uber set: a metric and its
        business logic in "a strictly ONE to ONE mapping" (Uber Blog, The Journey Towards Metric
        Standardization, 12 January 2021, checked 1 Oct 2026).
        ''', "Chapter 2 found that the monsoon sale reached 130 customers, all in Retail-Core and "
             "Retail-Plus, and chapter 3 found the Retail-Plus tier's spend down 29.4 percent from Q1 "
             "to Q2. This chapter answers the marketing lead's next question in three tools and makes "
             "them agree."),
        md('''
        **Setup.** The next cell reads the orders and the customer list from the warehouse, rebuilds
        chapter 1's table, reads the campaign platform's feed and applies chapter 2's rule: one row per
        reached customer, the first date the sale reached them, merged with a guard that refuses a
        repeat.
        '''),
        code(LOAD + TABLE + FEED + REACH),
        mapcell(4, ["1. the options\\nPython, SQL or pandas", "2. plain Python\\nsets and a dictionary",
                    "3. SQL\\nGROUP BY segment", "4. the trap\\npandas says 100 percent",
                    "5. the fix\\nthe segment from the list", "6. a second route\\nsets, no grouping"]),

        md('''
        ## 1. Which tool should answer the marketing lead's question, and what does each cost on this data?

        | Option | How it works | Where it runs |
        |---|---|---|
        | a) Plain Python | Fetch the orders as rows, then count with a set of reached customers and a dictionary of segments | On the analyst's machine, every step visible |
        | b) SQL | The warehouse joins the reached customers to their orders and groups by segment | In the warehouse, next to the data |
        | c) pandas | Group chapter 2's table, which is already in memory | On the analyst's machine, in one chain |

        The next cell sizes each: the rows it moves out of the warehouse, and the lines of logic a
        reviewer has to read.
        '''),
        cq('''
        PY = """seg_of = {r["customer_id"]: r["segment"] for r in rows}
        counts = {}
        for cid in reached_ids:
            c = counts.setdefault(seg_of.get(cid), {"reached": 0, "bought": 0})
            c["reached"] += 1
            c["bought"] += cid in buyers"""
        SQL_FIX = """@FIX@"""
        PD = """fixed = (table[table["reached"]].assign(bought=table["frequency"] > 0)
                     .groupby("segment").agg(reached=("customer_id", "count"),
                                             bought=("bought", "sum")))"""
        py_rows = kit.sql("SELECT customer_id FROM orders")
        sql_rows = kit.sql(SQL_FIX)
        sizing = [("a) plain Python", len(py_rows), len(PY.splitlines()), "the analyst's machine"),
                  ("b) SQL", len(sql_rows), len(SQL_FIX.splitlines()), "the warehouse"),
                  ("c) pandas", 0, len(PD.splitlines()), "the analyst's machine, already loaded")]
        kit.table(["option", "rows moved for this question", "lines of logic", "where it runs"],
                  [(n, f"{r:,}", l, w) for n, r, l, w in sizing],
                  caption="Each tool sized on the marketing lead's question")
        kit.bars([(name, rows) for name, rows, _, _ in sizing], lit=(1,),
                 title="Rows each tool moves out of the warehouse to answer it")
        ''', FIX=q("c4", 1)),
        md('''
        **The best-fit call: c, pandas, checked by b.** The growth team's table is already in memory,
        so pandas answers in four lines and moves nothing more. SQL moves only its answer, two rows,
        and shares no code with the notebook, which makes it the check Kavya asked for. Plain Python
        moves every order and is the route for explaining the count line by line. **The fact that
        would change it:** the number going to Finance or to an auditor. Then SQL owns it, which is
        chapter 5's question.
        '''),

        md('''
        ## 2. What does plain Python count, with a set of reached customers and a dictionary of segments?

        The hurried version starts from the buyers, since the question is about buying: it reads each
        customer's segment from their orders into a dictionary, then walks the reached customers and
        counts, by segment, how many were reached and how many bought. `seg_of_buyer.get(cid)` returns
        `None` for a customer the dictionary does not hold.

        **Predict before you run.** How many keys does the counting dictionary end with? a) 2; b) 3;
        c) 4; d) 130.
        '''),
        code('''
        rows = kit.sql("SELECT o.customer_id, c.segment FROM orders o JOIN customers c ON c.customer_id = o.customer_id")
        seg_of_buyer = {r["customer_id"]: r["segment"] for r in rows}   # a segment, read from the orders
        reached_ids = set(first_touch["customer_id"])
        counts_py = {}
        for cid in sorted(reached_ids):
            c = counts_py.setdefault(seg_of_buyer.get(cid), {"reached": 0, "bought": 0})
            c["reached"] += 1
            c["bought"] += cid in seg_of_buyer
        kit.table(["segment key", "reached", "bought"],
                  [("None" if k is None else k, v["reached"], v["bought"]) for k, v in counts_py.items()],
                  caption="Plain Python, segment read from the orders")
        keys = ["None" if k is None else k for k in counts_py]
        kit.columns(keys, [("reached", [v["reached"] for v in counts_py.values()]),
                           ("bought", [v["bought"] for v in counts_py.values()])],
                    title="Plain Python's three keys: the None key holds reached customers with no orders")
        '''),
        code('''
        kit.check("the dictionary holds three keys, one of them None", len(counts_py) == 3 and None in counts_py)
        kit.check("plain Python still counts all 130 reached customers",
                  sum(v["reached"] for v in counts_py.values()) == 130)
        '''),
        md('''
        **What happened.** The answer is b: Retail-Core, Retail-Plus and `None`. The `None` key holds 23
        reached customers who never ordered, so the dictionary had no segment for them, and not one of
        them bought. The totals are still whole: 130 reached, 107 bought.
        '''),

        md('''
        ## 3. What does SQL say when it groups the same customers by segment?

        The same hurried logic in SQL: take the distinct reached customers, attach each buyer's segment
        from their orders with a `LEFT JOIN`, and group by that segment.

        **Predict before you run.** How many rows does the query return? a) 2, one per segment the sale
        reached; b) 3, one of them with no segment; c) none, since a `NULL` cannot be grouped; d) 4.
        '''),
        cq('''
        HURRIED = """@HUR@"""
        counts_sql = kit.sql(HURRIED)
        kit.table(["segment", "reached", "bought"],
                  [("NULL" if r["segment"] is None else r["segment"], r["reached"], r["bought"]) for r in counts_sql],
                  caption="SQL, segment read from the orders")
        kit.check("SQL returns three groups, one of them NULL",
                  len(counts_sql) == 3 and any(r["segment"] is None for r in counts_sql))
        kit.check("SQL agrees with plain Python group by group",
                  {(r["segment"], r["reached"], r["bought"]) for r in counts_sql}
                  == {(k, v["reached"], v["bought"]) for k, v in counts_py.items()})
        ''', HUR=q("c4", 0)),
        md('''
        **What happened.** The answer is b. `GROUP BY` puts every row whose segment is `NULL` into one
        group of its own, so SQL shows the same 23 reached customers with no orders that plain Python
        filed under `None`. Two tools, one logic, one answer.
        '''),

        md('''
        ## 4. Why does pandas report that every reached customer bought?

        **The plausible wrong answer.** The same hurried logic in pandas: build one row per buyer with
        its segment from the orders, attach the reached customers with a right merge so every reached
        customer is kept, and group by segment.

        **Predict before you run.** What share of the reached customers does pandas say bought?
        a) 82 percent; b) 100 percent; c) 50 percent; d) it cannot be computed.
        '''),
        code('''
        buyers = (orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
                        .groupby("customer_id")
                        .agg(segment=("segment", "first"), frequency=("order_id", "count"))
                        .reset_index())
        reach_wrong = buyers.merge(first_touch, on="customer_id", how="right", validate="one_to_one")
        by_seg_wrong = reach_wrong.groupby("segment").agg(reached=("customer_id", "count"),
                                                          bought=("frequency", "count"))
        kit.table(["segment", "reached", "bought", "share"],
                  [(s, r.reached, r.bought, f"{r.bought / r.reached:.0%}") for s, r in by_seg_wrong.iterrows()],
                  caption="pandas, segment read from the orders: what the slide would say")
        kit.stats([(f"{by_seg_wrong['bought'].sum() / by_seg_wrong['reached'].sum():.0%}", "of reached customers bought",
                    "the pandas headline"),
                   (int(by_seg_wrong["reached"].sum()), "customers reached", "by the pandas count")])
        '''),
        md('''
        **What happened.** The answer is b: 100 percent, on 107 customers reached.

        **Why it is wrong.** The segment came from the order rows, so the 23 reached customers with no
        orders have no segment, which pandas holds as a missing value. `groupby` drops a missing key by
        default (`dropna=True`), where SQL's `GROUP BY` and the Python dictionary each kept a group for
        it. The customers who were reached and never bought are exactly the ones that vanished, so the
        slide reports perfect results to a marketing lead about to ask for the same budget again. The
        check that catches it: the groups must add back to the rows. 107 against the 130 reached shows
        the gap without reading a single row, and `dropna=False` shows where it went.
        '''),
        code('''
        shown = reach_wrong.groupby("segment", dropna=False)["customer_id"].count()
        kit.table(["segment", "customers"], [("(missing)" if pd.isna(k) else k, v) for k, v in shown.items()],
                  caption="The same groupby with dropna=False")
        kit.check("the default groupby lost 23 reached customers", len(reach_wrong) - int(by_seg_wrong["reached"].sum()) == 23)
        kit.check("the lost customers are exactly the reached customers with no orders",
                  int(reach_wrong["segment"].isna().sum()) == int(reach_wrong["frequency"].isna().sum()) == 23)
        kit.check("pandas disagrees with SQL and plain Python on the reach", int(by_seg_wrong["reached"].sum()) != 130)
        '''),

        md('''
        ## 5. Where should the segment come from, so that all three tools agree?

        **The fix, and what changed.** Every customer on the list has a segment, whether or not they
        ever ordered, so the segment comes from the customer list. In pandas that is chapter 2's table,
        which already carries it; in SQL a join to `customers`; in plain Python a dictionary built from
        the customer list. The reach moves from 107 to 130 and the share who bought from 100 percent to
        82 percent.

        **Predict before you run.** Once all three read the segment from the customer list, what share
        of Retail-Plus's reached members bought? a) 100 percent; b) 85 percent; c) 80 percent;
        d) 51 percent.
        '''),
        cq('''
        seg_of = {r["customer_id"]: r["segment"] for r in kit.sql("SELECT customer_id, segment FROM customers")}
        fixed_py = {}
        for cid in sorted(reached_ids):
            c = fixed_py.setdefault(seg_of[cid], {"reached": 0, "bought": 0})
            c["reached"] += 1
            c["bought"] += cid in seg_of_buyer
        fixed_sql = {r["segment"]: r for r in kit.sql("""@FIX@""")}
        reached_rows = table[table["reached"]]
        fixed_pd = (reached_rows.assign(bought=reached_rows["frequency"] > 0)
                                .groupby("segment").agg(reached=("customer_id", "count"), bought=("bought", "sum")))
        segs = ["Retail-Core", "Retail-Plus"]
        kit.columns(segs, [("plain Python", [fixed_py[s]["bought"] / fixed_py[s]["reached"] * 100 for s in segs]),
                           ("SQL", [fixed_sql[s]["bought"] / fixed_sql[s]["reached"] * 100 for s in segs]),
                           ("pandas", [fixed_pd.loc[s, "bought"] / fixed_pd.loc[s, "reached"] * 100 for s in segs])],
                    fmt=lambda v: f"{v:.0f}%", title="Share of reached customers who bought: three tools, one answer")
        ''', FIX=q("c4", 1)),
        code('''
        same = all(fixed_py[s]["reached"] == fixed_sql[s]["reached"] == fixed_pd.loc[s, "reached"]
                   and fixed_py[s]["bought"] == fixed_sql[s]["bought"] == fixed_pd.loc[s, "bought"] for s in segs)
        kit.check("plain Python, SQL and pandas agree segment by segment", same)
        kit.check("130 reached and 107 bought: 82 percent, where the hurried pandas said 100",
                  int(fixed_pd["reached"].sum()) == 130 and int(fixed_pd["bought"].sum()) == 107,
                  f"{fixed_pd['bought'].sum() / fixed_pd['reached'].sum():.1%}")
        kit.check("Retail-Plus: 51 of 60 reached members bought", fixed_pd.loc["Retail-Plus", "bought"] == 51 and
                  fixed_pd.loc["Retail-Plus", "reached"] == 60)
        '''),
        md('''
        **What happened.** The answer is b, 85 percent: 51 of Retail-Plus's 60 reached members bought,
        and 56 of Retail-Core's 70, which is 80 percent. Across both, 107 of 130, 82 percent. The three
        tools agree once they share one definition of a customer's segment; the disagreement was never
        about the tools' arithmetic.

        > **Kavya's review.** "When two tools disagree, look for the rows one of them dropped before you
        > look at the code. Check that the groups add back to the rows, and take every attribute of a
        > customer from the customer list, never from their orders."
        '''),

        md('''
        ## 6. Does counting sets, with no grouping at all, find the same customers who never bought?

        Grouping put the missing customers in a group or lost them. Sets need no group: the reached
        customers minus the customers with at least one order are the reached customers who never
        bought, whatever their segment, and the reached minus those is the reached who bought. The
        route shares no code with any of the three above.
        '''),
        code('''
        with_orders = set(orders["customer_id"])
        never = reached_ids - with_orders
        bought_n = len(reached_ids) - len(never)
        kit.bridge(("reached", len(reached_ids)), [("reached, never ordered", -len(never))],
                   end_label="reached and bought", fmt=lambda v: f"{v:,.0f}", lit=(0,),
                   title="Sets alone: 130 reached, 23 of them never ordered, 107 bought")
        kit.check("sets find the same 23 reached customers who never ordered", len(never) == 23)
        kit.check("sets find the same 107 who bought", bought_n == int(fixed_pd["bought"].sum()) == 107)
        '''),
        md('''
        **When to switch.** The pandas group is the route for the slide, since it splits by segment.
        The set difference is the route to trust when a group count looks too good: it cannot drop a
        missing segment, because it never asks for one.

        ### How would you answer this chapter's questions in an interview?

        **[F] What does SQL's `GROUP BY` do with a `NULL` key, and what does pandas' `groupby` do with
        a missing one?** "SQL puts every `NULL` into one group of its own. pandas drops rows whose key is
        missing, because `dropna` defaults to `True`, so the same logic can report fewer rows in pandas
        than in SQL. I check that the groups add back to the rows, and I pass `dropna=False` when a
        missing group is information."

        **[D] A dashboard shows that 100 percent of the customers a campaign reached went on to buy.
        What do you check first?** "Whether the customers who did not buy are missing from the
        denominator. I count the reached customers straight from the campaign's feed and compare with
        the dashboard's total; if they differ, I look for a join or a group that dropped them, such as a
        segment read from the orders, which non-buyers do not have."

        **[S] Why can the same question give different answers in two tools?** "Because each copy of
        the logic makes its own choices, here where the segment comes from and what happens to a missing
        key. The fix is one definition, used by every tool, which is what Uber's metric platform was
        built for."

        ### Going deeper: does a pandas merge treat a missing key the way a SQL join does?

        It does not. The pandas documentation's comparison with SQL warns that if both key columns hold
        rows whose key is missing, pandas matches those rows to each other, "different from usual SQL
        join behaviour" (pandas 3.0.6 documentation, Comparison with SQL, checked 1 Oct 2026). SQL
        never matches `NULL` to `NULL`. The records below are invented to show it.
        '''),
        code('''
        left = pd.DataFrame({"segment": ["Retail-Plus", None], "reached": [60, 23]})
        right = pd.DataFrame({"segment": ["Retail-Plus", None], "target": [70, 5]})
        in_pandas = left.merge(right, on="segment", how="inner")
        in_sql = kit.sql("""SELECT l.segment, l.reached, r.target
                            FROM (VALUES ('Retail-Plus', 60), (NULL, 23)) AS l(segment, reached)
                            JOIN (VALUES ('Retail-Plus', 70), (NULL, 5)) AS r(segment, target)
                              ON l.segment = r.segment""")
        kit.table(["tool", "rows the inner join returns"], [("pandas merge", len(in_pandas)), ("SQL join", len(in_sql))],
                  caption="Invented rows: two keys, one of them missing on both sides")
        kit.check("pandas matches the missing key to itself; SQL does not", len(in_pandas) == 2 and len(in_sql) == 1)
        '''),
        md('''
        **The answers, question by question.**

        1. pandas answers on the table already in memory, checked by SQL, which moves two rows; plain
           Python moves every order and explains the count line by line.
        2. Plain Python kept three keys, and the `None` key held the 23 reached customers who never
           ordered.
        3. SQL returned three groups, one of them `NULL` with the same 23, matching plain Python.
        4. pandas dropped the missing segment by default and reported 100 percent on 107 customers.
        5. With the segment from the customer list, all three tools agree: 130 reached, 107 bought,
           82 percent, Retail-Plus 51 of 60.
        6. Sets alone find the same 23 who never ordered and the same 107 who bought.
        '''),
        code('''
        kit.flow(["reached customers\\n130, chapter 2's rule", "segment from the list\\nevery customer has one",
                  "group, check the groups add up\\n130 = 130", "three tools agree\\n107 bought, 82%"], lit=1,
                 title="One question, three tools, one definition")
        kit.check_summary()
        print("Next: chapter 5 decides which tool should own each of Marketing's and Finance's numbers.")
        '''),
    ]


# ============================================================================= chapter 5
C5_LADDER = [
    "Which of three tools should compute Finance's Monday revenue, and what does each cost?",
    "Does speed separate the three tools on 1,000 orders?",
    "How many rows does each tool move to answer an eight-row question?",
    "Which tool should own each of the day's recurring asks, and which would you refuse for Finance?",
    "Does the growth team's table reconcile with Finance's query to the rupee?",
]


def ch5():
    return [
        opener(5, "Which tool should own each of Marketing's and Finance's recurring numbers, and which would you refuse for Finance?", '''
        > **The client asks.** "Now tell me honestly which tool you would pick for which job. I will ask
        > you which one you would refuse to use for Finance's numbers, so have a reason ready."
        >
        > Kavya Nair, senior analyst, Kalpa Retail data team
        ''', '''
        **Who needs the answer.** Kavya, and behind Kavya, Anand Iyer, the finance controller, whose
        analyst reruns every number the team sends, line by line. The note decides where each recurring
        number lives. A number that lives in two tools drifts into two numbers, and two numbers for one
        metric is how Week 1 Wednesday began, with the dashboard's Rs 2.1 crore against the books' Rs
        1.9 crore and a month lost to the argument.
        ''', C5_LADDER, '''
        The day's recurring numbers and the tool that owns each. The one the chapter tests is Finance's
        Monday revenue by segment and quarter: eight numbers, four segments by two quarters, adding up
        to Rs 19,84,00,000, which Anand's analyst reruns every week.
        ''', '''
        LinkedIn met the cost of one metric living in many places. The page for its Unified Metrics
        Platform says that "multiple stakeholders come up with different ways to calculate the same
        metric arriving at slightly different results", and that the platform now "serves as the single
        source of truth for all business metrics at Linkedin" (LinkedIn Engineering, Unified Metrics
        Platform, checked 1 Oct 2026).
        ''', "Chapter 4 found that plain Python, SQL and pandas agree, 130 reached and 107 bought, once "
             "they share one definition of a customer's segment. This chapter decides where each of the "
             "day's recurring numbers should live, starting with Finance's."),
        md('''
        **Setup.** The next cell reads the orders and the customer list from the warehouse and rebuilds
        chapter 1's table, so the growth team's frame is in memory as it would be on a working Monday.
        '''),
        code(LOAD + TABLE),
        mapcell(5, ["1. the options\\nSQL, pandas or plain Python", "2. speed\\non 1,000 orders",
                    "3. the trap\\nrows returned or rows moved", "4. the note\\na tool for every ask",
                    "5. a second route\\nthe table against Finance"]),

        md('''
        ## 1. Which of three tools should compute Finance's Monday revenue, and what does each cost?

        | Option | How it works | Where the logic lives |
        |---|---|---|
        | a) SQL | The warehouse joins orders to customers, groups by segment and quarter, and sends back the answer | In a query file anyone with read access can run |
        | b) pandas | The growth team's notebook reads the orders and the customer list, merges and groups them | In a notebook on the analyst's machine |
        | c) Plain Python | A script fetches the rows and adds them up in a dictionary keyed by segment and quarter | In a script on the analyst's machine |

        The next cell writes each out and sizes it on what Finance cares about: the lines a reviewer
        must read, where the number can be rerun, and what the number depends on besides the data.
        '''),
        cq('''
        import inspect

        FIN_SQL = """@FIN@"""

        def finance_sql():
            answer = pd.read_sql(FIN_SQL, ENG)
            return answer, len(answer)                  # the answer, and the rows that left the warehouse

        def finance_pandas():
            o = pd.read_sql("SELECT customer_id, quarter, amount FROM orders", ENG)
            c = pd.read_sql("SELECT customer_id, segment FROM customers", ENG)
            answer = (o.merge(c, on="customer_id", how="left", validate="many_to_one")
                       .groupby(["segment", "quarter"], as_index=False)["amount"].sum())
            return answer, len(o) + len(c)

        def finance_python():
            rows = kit.sql("SELECT o.quarter, o.amount, c.segment FROM orders o "
                           "JOIN customers c ON c.customer_id = o.customer_id")
            answer = {}
            for r in rows:
                key = (r["segment"], r["quarter"])
                answer[key] = answer.get(key, 0) + r["amount"]
            return answer, len(rows)

        routes = {"a) SQL": finance_sql, "b) pandas": finance_pandas, "c) plain Python": finance_python}
        lines = {"a) SQL": len(FIN_SQL.splitlines()),
                 "b) pandas": len(inspect.getsource(finance_pandas).splitlines()) - 2,
                 "c) plain Python": len(inspect.getsource(finance_python).splitlines()) - 2}
        sizing = [("a) SQL", lines["a) SQL"], "anywhere with read access", "the warehouse only"),
                  ("b) pandas", lines["b) pandas"], "on the analyst's machine", "the notebook's state and environment"),
                  ("c) plain Python", lines["c) plain Python"], "on the analyst's machine", "the script's environment")]
        kit.table(["option", "lines of logic", "where Anand's analyst can rerun it", "what it depends on besides the data"],
                  sizing, caption="Three ways to compute Finance's Monday revenue")
        kit.matrix(["a) SQL", "b) pandas", "c) plain Python"], ["rerun by Finance", "audited where the data lives", "iterate on a question"],
                   [["yes, from the query file", "yes", "a new query each time"],
                    ["needs the analyst's notebook", "no, a copy in memory", "yes, the analyst's bench"],
                    ["needs the script", "no, a copy in memory", "slow to change"]],
                   title="What each tool gives the person who reruns the number")
        ''', FIN=q("c5", 0)),
        md('''
        **The best-fit call: a, SQL.** Anand's analyst has to rerun the number every Monday without the
        growth team's machine, and only the query runs where the data lives, on nothing but the data.
        **The fact that would change it:** a Finance question that needs iteration, such as a new cut
        tried five ways in an afternoon. Then pandas reads the query's answer and works on that, and the
        definition still lives in one place. Speed and rows are the two sizes still missing; the next
        two questions measure them.
        '''),

        md('''
        ## 2. Does speed separate the three tools on 1,000 orders?

        A hurried note ranks tools by speed. The cell below runs all three routes end to end, from the
        warehouse to the eight numbers, and times each.

        **Predict before you run.** Which is true on Kalpa's 1,000 orders? a) SQL is ten times faster
        than the rest; b) pandas is ten times faster than the rest; c) all three finish well inside a
        second; d) plain Python takes over a minute.
        '''),
        code('''
        import time
        timings = {}
        for name, route in routes.items():
            start = time.perf_counter()
            route()
            timings[name] = time.perf_counter() - start
        kit.bars([(k, round(v, 3)) for k, v in timings.items()], fmt=lambda v: f"{v:.3f} s",
                 title="Seconds from the warehouse to the eight numbers, this run; they vary from run to run")
        kit.check("every route finishes well inside a second on 1,000 orders", all(v < 1 for v in timings.values()),
                  ", ".join(f"{k} {v:.3f} s" for k, v in timings.items()))
        '''),
        md('''
        **What happened.** The answer is c. On a thousand orders every route finishes in a fraction of a
        second, and the ranking changes from one run to the next, so speed separates nothing here. A
        sizing column where every option scores the same is no reason to choose.
        '''),

        md('''
        ## 3. How many rows does each tool move to answer an eight-row question?

        **The plausible wrong answer.** The hurried note sizes each tool by its answer: each returns the
        same eight rows, four segments by two quarters, so the note calls the cost equal and picks
        pandas for Finance, because its chain is short and the growth team already uses it.

        **Predict before you run.** How many rows did the pandas route actually move out of the
        warehouse to produce its eight? a) 8; b) 340; c) 1,000; d) 1,340.
        '''),
        code('''
        (fin_sql, moved_sql), (fin_pd, moved_pd), (fin_py, moved_py) = (finance_sql(), finance_pandas(),
                                                                  finance_python())
        returned = [("a) SQL", len(fin_sql)), ("b) pandas", len(fin_pd)), ("c) plain Python", len(fin_py))]
        kit.table(["option", "rows in the answer"], returned, caption="The hurried note's sizing: the answer's rows")
        moved = [("a) SQL", moved_sql), ("b) pandas", moved_pd), ("c) plain Python", moved_py)]
        kit.bars(moved, lit=(1,), title="Rows each tool moved out of the warehouse to produce the same eight")
        '''),
        md('''
        **What happened.** The answer is d, 1,340: the pandas route pulled every order and every
        customer, 1,000 and 340, to add them up on the analyst's machine. Plain Python pulled 1,000.
        SQL moved 8, the answer itself.

        **Why it is wrong.** The rows an answer holds say nothing about the work of producing it. Sized
        by rows returned, the three tools tie at 8; sized by rows moved, SQL moves 8 and pandas 1,340,
        and the gap grows with the orders table: at a hundred times Kalpa's orders the pandas route
        moves a hundred times the rows while SQL still sends 8. A note that picked pandas for Finance on
        the tie would also have put Finance's number where Anand's analyst cannot rerun it. The check
        that catches it: count the rows each route fetched, which the cell below does, before comparing
        anything else.
        '''),
        code('''
        kit.check("all three answers hold eight rows", len(fin_sql) == len(fin_pd) == len(fin_py) == 8)
        kit.check("the pandas route moved 1,340 rows for those eight", moved_pd == 1340)
        kit.check("plain Python moved 1,000 and SQL only its answer", moved_py == 1000 and moved_sql == 8)
        kit.check("the three routes agree on every one of the eight numbers",
                  all(fin_py[(r.segment, r.quarter)] == r.revenue == fin_pd.set_index(["segment", "quarter"]).loc[(r.segment, r.quarter), "amount"]
                      for r in fin_sql.itertuples()))
        '''),
        md('''
        **The fix, and what changed.** Size a route by the rows it moves and by who must rerun it. Moved
        rows put SQL at 8 against pandas at 1,340, about 168 times as many on today's data, and the rerun
        question had already put Finance's number in SQL. The note's line for Finance does not change;
        its reason is now a number instead of a preference.
        '''),

        md('''
        ## 4. Which tool should own each of the day's recurring asks, and which would you refuse for Finance?

        The note Kavya asked for, one line per ask, each with its owner and its reason. The four asks
        are the day's: Finance's Monday revenue, the growth team's customer table, the head of
        Retail-Plus's months view, and an auditor who wants one customer's spend explained step by step.

        **Predict before you run.** Which ask should plain Python own? a) Finance's Monday revenue;
        b) the growth team's customer table; c) the head of Retail-Plus's months view; d) the auditor's
        one customer, step by step.
        '''),
        code('''
        note = [("Finance's revenue by segment and quarter", "SQL", "Anand's analyst reruns it where the data lives; it moves 8 rows"),
                ("The growth team's customer table", "pandas, reading the warehouse", "the analysts add columns every week; merge and validate are one line each"),
                ("The head of Retail-Plus's months view", "pandas", "a pivot and a melt on data already in memory"),
                ("One customer's spend, for an auditor", "plain Python", "every step is a line the auditor can read")]
        kit.table(["the ask", "the owner", "the reason"], note, caption="The tool-choice note")
        kit.matrix(["SQL", "pandas", "plain Python"], ["owns", "reads from", "refused for"],
                   [["Finance's revenue", "the warehouse", "exploring a new question"],
                    ["the customer table", "SQL's answers", "Finance's revenue"],
                    ["an auditor's one-off", "rows fetched once", "anything rerun weekly"]],
                   title="The note as a grid: what each tool owns and what it is refused")
        kit.check("every ask has one owner", len(note) == 4 and all(owner for _, owner, _ in note))
        kit.check("Finance's number is owned by SQL", note[0][1] == "SQL")
        '''),
        md('''
        **What happened.** The answer is d. The auditor's question is asked once and has to be read line
        by line, which is what a plain loop offers. The refusal the note carries: **never a pandas
        notebook for Finance's number.** It moves every order to one machine, it runs on a copy, and
        Anand's analyst cannot rerun it without the growth team's notebook and its state. pandas stays
        the growth team's bench, reading what SQL computes.

        > **Kavya's review.** "Choose by who has to trust the number and rerun it, and size by the rows
        > a route moves. Finance's number lives in the warehouse, the growth team's table reads from it,
        > and plain Python is for the question you must explain line by line."
        '''),

        md('''
        ## 5. Does the growth team's table reconcile with Finance's query to the rupee?

        A number that lives in one place still has to agree with every copy made from it. The growth
        team's table carries spend per customer over both quarters; adding it up by segment must give
        Finance's query, summed over the two quarters, to the rupee. The two share no code: one is
        chapter 1's `groupby` and merge, the other is SQL.
        '''),
        code('''
        from_table = table.groupby("segment")["spend"].sum()
        from_finance = fin_sql.groupby("segment")["revenue"].sum().astype(float)
        segs = from_table.index.tolist()
        kit.table(["segment", "the growth team's table", "Finance's query, both quarters"],
                  [(s, kit.rupees(from_table[s]), kit.rupees(from_finance[s])) for s in segs],
                  caption="The table against Finance, segment by segment")
        kit.bars([(s, from_table[s]) for s in segs if s != "Business"], fmt=kit.rupees,
                 title="Consumer segments' two-quarter spend, from the table; Business is Rs 19,65,99,040 on its own")
        kit.check("every segment agrees to the rupee", all(from_table[s] == from_finance[s] for s in segs))
        kit.check("both add up to Rs 19,84,00,000", from_table.sum() == from_finance.sum() == 198_400_000)
        '''),
        md('''
        **When to switch.** This reconciliation is the check that lets two tools share one number: run it
        every Monday, and when it fails, the warehouse is right and the table is wrong until someone
        can say why. Chapter 6 puts it inside the refresh.

        ### How would you answer this chapter's questions in an interview?

        **[D] Same question, three tools: how do you choose, and defend one choice?** "When they agree,
        I choose by who has to trust and rerun the number. Finance's number goes in SQL, because it runs
        where the data lives, moves only its answer and Finance can rerun it from the query. The
        analyst's iterative work goes in pandas, reading SQL's answers. A one-off I must explain line by
        line goes in plain Python. On 1,000 rows speed separates nothing, so I size by rows moved: SQL 8,
        pandas 1,340."

        **[D] Which tool would you refuse for Finance's numbers, and why?** "A pandas notebook run by
        hand. It moves every order to one machine, depends on the order its cells were run in, and
        Finance cannot rerun it without my environment. I would give Finance the query and let my
        notebook read the query's answer."

        **[F] When would you move a pandas step into SQL?** "When the step aggregates a large table
        into a small answer, when someone else must rerun it, or when two teams need the same
        definition. The warehouse sends the answer, and pandas works on the answer."

        ### Going deeper: how can pandas read Finance's definition instead of copying it?

        A view is a named query stored in the database. Once Finance's query is a view, the growth
        team's notebook reads the view and never retypes the logic, so the two cannot drift. The cell
        below makes a temporary view, which lasts only as long as its connection, so it changes nothing
        in the shared warehouse; a permanent view is the data platform lead's to create.
        '''),
        cq('''
        from sqlalchemy import text
        with ENG.connect() as con:
            con.execute(text("CREATE TEMP VIEW finance_revenue AS " + FIN_SQL.rstrip(";")))
            from_view = pd.read_sql("SELECT * FROM finance_revenue", con)
        kit.check("pandas reading the view gets Finance's eight numbers exactly",
                  from_view.equals(fin_sql), f"{len(from_view)} rows")
        '''),
        md('''
        **The answers, question by question.**

        1. SQL computes Finance's Monday revenue, because Anand's analyst reruns it where the data lives;
           pandas and plain Python would put it on the analyst's machine.
        2. Speed separates nothing on 1,000 orders: all three routes finish well inside a second.
        3. Each route returns 8 rows, but SQL moves 8 and pandas 1,340, which is the size that separates
           them.
        4. SQL owns Finance's revenue, pandas the customer table and the months view, plain Python the
           auditor's one-off; a pandas notebook is refused for Finance.
        5. The growth team's table reconciles with Finance's query in every segment, Rs 19,84,00,000 in
           all.
        '''),
        code('''
        kit.flow(["warehouse\\nFinance's query, 8 rows", "pandas reads the answer\\nthe growth team's bench",
                  "reconciled every Monday\\nRs 19,84,00,000"], lit=0,
                 title="One number, one owner, every copy checked against it")
        kit.check_summary()
        print("Next: chapter 6 makes the growth team's table rebuild itself every Monday and stop when a check fails.")
        '''),
    ]


# ============================================================================= chapter 6
C6_LADDER = [
    "Which of four ways should run the Monday refresh, and what does each catch?",
    "What does the refresh need to be told, and what can it read from the data itself?",
    "How many customers land on the win-back list when the refresh runs on Monday 19 October?",
    "Which guards stop a bad Monday, and does each one fire when it should?",
    "Do two runs on the same data give the same table?",
    "Does the warehouse, counting on its own, find the same win-back list?",
]

REFRESH = '''
def build_table(engine, feed_path):
    """Chapters 1 and 2 in one call: every customer, three numbers each, the sale's first touch."""
    o = pd.read_sql("SELECT order_id, customer_id, order_date, amount FROM orders", engine,
                    parse_dates=["order_date"])
    c = pd.read_sql("SELECT customer_id, segment FROM customers", engine)
    e = pd.read_csv(feed_path, parse_dates=["exposed_date"])
    agg = (o.groupby("customer_id")
            .agg(last_order=("order_date", "max"), frequency=("order_id", "count"), spend=("amount", "sum"))
            .reset_index())
    t = c.merge(agg, on="customer_id", how="left", validate="one_to_one")
    first = e.sort_values("exposed_date").drop_duplicates("customer_id", keep="first")
    t = t.merge(first[["customer_id", "exposed_date"]], on="customer_id", how="left", validate="one_to_one")
    return t.assign(frequency=t["frequency"].fillna(0).astype("int64"), spend=t["spend"].fillna(0),
                    reached=t["exposed_date"].notna()), o

FEED_PATH = kit.data_dir() / "C2_W02_D04_exposure_STUDENT.csv"
'''


def ch6():
    return [
        opener(6, "Can the table rebuild itself every Monday and refuse to ship when something breaks?", '''
        > **The client asks.** "The warehouse queries are fine for Finance, but Marketing's analysts
        > live in Python. Build them the table in pandas, from the warehouse, and make it refreshable in
        > one run."
        >
        > The data platform lead, Kalpa Retail
        ''', '''
        **Who needs the answer.** The growth team, who act on Monday's table with no analyst watching
        the run: the win-back code goes to every customer the table marks as lapsed. A refresh that
        counts days from the wrong date sends the code to customers who bought a few weeks ago, and a
        refresh that ships a broken table sends Monday's offers to the wrong people before anyone
        looks.
        ''', C6_LADDER, '''
        The win-back list: customers whose last order is more than 60 days before the table's as-of
        date, the last date the data covers. The number of days since a customer's last order is their
        recency in days. A customer who never ordered has nothing to win back and belongs on chapter
        1's first-order list instead. The 60-day line is the growth team's.
        ''', '''
        England's public health agency ran a daily refresh that dropped rows without an error. Its own
        statement said "15,841 cases between 25 September and 2 October were not included in the
        reported daily COVID-19 cases" (Public Health England, 4 October 2020). The Register reported
        the cause: test results were "automatically fetched in CSV format" from commercial laboratories
        and stored in the older .XLS format, "that limited the number of rows to 65,536 per
        spreadsheet" (The Register, 5 October 2020; both checked 1 Oct 2026). A count of rows in
        against rows out on every run would have stopped it on the first day.
        ''', "Chapter 5 gave Finance's number to SQL and the growth team's table to pandas, reading from "
             "the warehouse, and the table reconciles with Finance's query in every segment. This chapter "
             "makes the table rebuild itself every Monday and stop when a check fails."),
        md('''
        **Setup.** The next cell finds the helper and opens the warehouse connection. Everything else
        this chapter needs is built inside the refresh function, which is the point.
        '''),
        code(SETUP + "import pandas as pd\n\nENG = kit.engine()\nprint(\"connected to the warehouse\", kit.WAREHOUSE[\"dbname\"])\n"),
        mapcell(6, ["1. the options\\nby hand, report, guard or view", "2. the function\\ntold two things",
                    "3. the trap\\ndays counted from the run day", "4. the guards\\neach one made to fire",
                    "5. two runs\\none table", "6. a second route\\nthe warehouse counts"]),

        md('''
        ## 1. Which of four ways should run the Monday refresh, and what does each catch?

        | Option | How it runs | When a check fails |
        |---|---|---|
        | a) Rerun the notebooks by hand | An analyst runs chapters 1 to 5 and reads the numbers | The table ships if the analyst misses it |
        | b) One function that reports | One call builds the table and prints PASS or FAIL for each check | The table ships, with a FAIL printed beside it |
        | c) One function with guards | One call builds the table, and every check that fails raises an error | The table is not written, and the error says why |
        | d) The table as a SQL view | The warehouse builds the table whenever it is read | There is nothing to fail: a view returns whatever its query gives |

        The next cell sizes each against the failures the day has already met: a customer missing from
        the table, a customer the feed sends twice, spend that no longer adds up to the warehouse, and a
        key that repeats.
        '''),
        code('''
        failures = ["a customer missing", "a customer sent twice", "spend off the warehouse", "a repeated key"]
        stops = {"a) by hand": [0, 0, 0, 0], "b) reports": [0, 0, 0, 0],
                 "c) guards": [1, 1, 1, 1], "d) a SQL view": [0, 0, 0, 0]}
        kit.matrix(list(stops), failures,
                   [["only if noticed"] * 4, ["reported, shipped"] * 4, ["stopped"] * 4,
                    ["no check runs", "no validate in SQL", "no check runs", "no check runs"]],
                   title="Which failure each option stops before Marketing sees the table")
        kit.bars([(k, sum(v)) for k, v in stops.items()], lit=(2,),
                 title="Failures stopped before the table ships, out of four")
        '''),
        md('''
        **The best-fit call: c, one function with guards.** It is the only option that stops a bad
        Monday before the growth team acts on it, and it keeps the table in pandas, where chapter 5 put
        it. **The fact that would change it:** the table's readers querying it from the warehouse, such
        as a dashboard. Then d, with the same checks moved into the warehouse's own tests.
        '''),

        md('''
        ## 2. What does the refresh need to be told, and what can it read from the data itself?

        A refresh that runs unattended should be told as little as possible, because every input is a
        chance to be told something wrong. The function below is chapters 1 and 2 in one call: the
        customer list as the spine, the three numbers from the orders, the sale's first exposure, both
        merges validated.

        **Predict before you run.** What must the function be told? a) the day to count recency from;
        b) the warehouse connection and the feed's path; c) the number of customers; d) the total spend.
        '''),
        code(REFRESH + textwrap.dedent('''
        table, o = build_table(ENG, FEED_PATH)
        kit.table(["the function is told", "it reads from the data"],
                  [("the warehouse connection", "the orders and the customer list"),
                   ("the feed's path", "the first exposure of every reached customer"),
                   ("", f"{len(table)} customers, {kit.rupees(table['spend'].sum())} of spend")],
                  caption="What build_table needs, and what it finds for itself")
        kit.flow(["connection and feed path", "build_table()", f"{len(table)} rows"], lit=1,
                 title="Two inputs in, one table out")
        kit.check("the function rebuilds chapter 2's table", len(table) == 340 and int(table["reached"].sum()) == 130)
        kit.check("spend adds back to the warehouse", table["spend"].sum() == 198_400_000)
        ''')),
        md('''
        **What happened.** The answer is b. Everything else, the customers, their numbers and the sale,
        the function reads from the data, so it cannot be told a stale count. Recency is the one column
        still missing, and it needs a date to count to.
        '''),

        md('''
        ## 3. How many customers land on the win-back list when the refresh runs on Monday 19 October?

        **The plausible wrong answer.** Recency is the days since a customer's last order, and the
        hurried analyst counts them to `pd.Timestamp.today()`, so the refresh looks current whenever it
        runs. The table first ships on Monday 19 October, the first Monday after this session; the cell
        pins that date so the number below is exactly what that refresh would have sent.

        **Predict before you run.** How many customers land on the win-back list, no order in 60 days?
        a) 111; b) 166; c) 301; d) 55.
        '''),
        code('''
        RUN_DAY = pd.Timestamp("2026-10-19")      # what pd.Timestamp.today() returns on the first Monday refresh
        wrong = (RUN_DAY - table["last_order"]).dt.days
        wrong_list = int((wrong > 60).sum())
        kit.stats([(wrong_list, "on the win-back list", "no order in 60 days, counted to the run day"),
                   (int(wrong.min()), "smallest recency, in days", "the most recent buyer, as the table says")],
                  caption="The Monday 19 October refresh, as the hurried function would ship it")
        '''),
        md('''
        **What happened.** The answer is b, 166 customers.

        **Why it is wrong.** The warehouse's last order is dated 28 September 2026; nothing after it has
        been loaded. Counted to 19 October, every customer looks 21 days staler than the data says, so
        customers who bought in the weeks before the data ends are sent a win-back code. Run the same
        refresh a week later with no new data and the list grows again, because the table has become a
        function of the calendar. The check that catches it: somebody always bought on the data's last
        day, so the smallest recency in an honest table is 0. Here it is 21.
        '''),
        code('''
        AS_OF = o["order_date"].max()
        kit.check("the data's last date is 28 September 2026", AS_OF == pd.Timestamp("2026-09-28"), str(AS_OF.date()))
        kit.check("the hurried recency's smallest value is 21 days, the gap between the two dates",
                  int(wrong.min()) == (RUN_DAY - AS_OF).days, f"{int(wrong.min())} days")
        mondays = pd.to_datetime(["2026-10-19", "2026-10-26", "2026-11-02"])
        grows = [int(((m - table["last_order"]).dt.days > 60).sum()) for m in mondays]
        kit.check("with no new data, the hurried list grows every Monday", grows == sorted(grows) and grows[0] < grows[-1],
                  ", ".join(f"{m.date()}: {n}" for m, n in zip(mondays, grows)))
        '''),
        md('''
        **The fix, and what changed.** Count to the data's own last date, `o["order_date"].max()`, and
        write that date into the table as its `as_of` column, so the growth team can see what "60 days"
        was counted from. The list falls from 166 to 111; the 55 customers who came off it had ordered
        within 60 days of 28 September.
        '''),
        code('''
        table = table.assign(as_of=AS_OF, recency_days=(AS_OF - table["last_order"]).dt.days)
        table = table.assign(lapsed=table["recency_days"] > 60)
        right_list = int(table["lapsed"].sum())
        kit.line(["19 Oct", "26 Oct", "2 Nov"], [("counted to the run day", grows, "bad"),
                                                 ("counted to 28 September", [right_list] * 3, "lit")],
                 title="The win-back list on three Mondays with no new data")
        by_seg = pd.DataFrame({"counted to the run day": (wrong > 60).groupby(table["segment"]).sum(),
                               "counted to 28 September": table["lapsed"].groupby(table["segment"]).sum()})
        kit.columns(by_seg.index.tolist(), [(c, by_seg[c].astype(int).tolist()) for c in by_seg.columns],
                    title="The win-back list by segment, both ways")
        kit.check("the honest smallest recency is 0 days", table["recency_days"].min() == 0)
        kit.check("the honest win-back list holds 111 customers", right_list == 111, f"{right_list}")
        '''),

        md('''
        ## 4. Which guards stop a bad Monday, and does each one fire when it should?

        A guard is a check that raises an error, so a table that fails it is never written. Four guards
        cover the failures the day has met, each against a number the warehouse gives independently:
        one row per customer, as many rows as the customer list, spend equal to the warehouse's, and a
        smallest recency of 0. Each guard is proved the only way a guard can be, by making it fire: the
        cell breaks a copy of the table in one way at a time.

        **Predict before you run.** A copy with one customer's row repeated: which guards fire?
        a) only the unique-key guard; b) the unique-key and row-count guards; c) the unique-key,
        row-count and spend guards; d) all four.
        '''),
        code('''
        controls = kit.sql("SELECT (SELECT count(*) FROM customers) AS customers, "
                           "(SELECT sum(amount) FROM orders) AS spend")[0]

        def guard_failures(t):
            """The guards that fail on a table, each checked against the warehouse's own numbers."""
            failed = []
            if not t["customer_id"].is_unique:
                failed.append("one row per customer")
            if len(t) != controls["customers"]:
                failed.append("rows equal the customer list")
            if t["spend"].sum() != float(controls["spend"]):
                failed.append("spend equals the warehouse")
            if t["recency_days"].min() != 0:
                failed.append("smallest recency is 0")
            return failed

        repeated = pd.concat([table, table[table["customer_id"] == "C-0152"]])
        wall_clock = table.assign(recency_days=(RUN_DAY - table["last_order"]).dt.days)
        dropped = table[table["frequency"] > 0]
        trials = [("the honest table", table), ("one customer's row repeated", repeated),
                  ("recency counted to the run day", wall_clock), ("customers with no orders dropped", dropped)]
        kit.table(["the table", "guards that fire"],
                  [(name, ", ".join(guard_failures(t)) or "none") for name, t in trials],
                  caption="Each broken copy, and the guards it trips")
        kit.bars([(name, len(guard_failures(t))) for name, t in trials], lit=(0,),
                 title="Guards that fire on each copy: none on the honest table")
        '''),
        code('''
        kit.check("the honest table passes every guard", guard_failures(table) == [])
        kit.check("a repeated row trips the key, row-count and spend guards",
                  guard_failures(repeated) == ["one row per customer", "rows equal the customer list", "spend equals the warehouse"])
        kit.check("recency counted to the run day trips the recency guard", guard_failures(wall_clock) == ["smallest recency is 0"])
        kit.check("dropping customers with no orders trips the row-count guard",
                  guard_failures(dropped) == ["rows equal the customer list"])
        '''),
        md('''
        **What happened.** The answer is c: a repeated row breaks the unique key, adds a row and adds
        that customer's spend a second time, so three guards fire; the recency guard does not, because
        the repeated customer's recency is the same. Each broken copy trips at least one guard and the
        honest table trips none, which is what makes the guards worth running. In the refresh, a guard
        that fails raises an error, so the table is not written.
        '''),

        md('''
        ## 5. Do two runs on the same data give the same table?

        The whole refresh is now one function: build, count recency to the data's last date, flag, and
        run every guard, raising an error on the first that fails. A refresh the growth team can trust
        gives the same table whenever it runs on the same data, whatever the calendar says.

        **Predict before you run.** The honest refresh runs on two different Mondays with no new data.
        How many customers differ between the two tables? a) 55; b) 14; c) 0; d) 111.
        '''),
        code('''
        def refresh(engine, feed_path):
            """The Monday refresh: the table, counted to the data's own last date, and every guard."""
            t, orders_read = build_table(engine, feed_path)
            as_of = orders_read["order_date"].max()
            t = t.assign(as_of=as_of, recency_days=(as_of - t["last_order"]).dt.days)
            t = t.assign(lapsed=t["recency_days"] > 60)
            failed = guard_failures(t)
            if failed:
                raise ValueError("the refresh stopped; guards failed: " + ", ".join(failed))
            return t

        monday_1 = refresh(ENG, FEED_PATH)          # run on one Monday
        monday_2 = refresh(ENG, FEED_PATH)          # and again, a week later, with no new data
        hurried = [int(((m - monday_1["last_order"]).dt.days > 60).sum()) for m in mondays[:2]]
        kit.columns(["first Monday", "a week later"], [("counted to the run day", hurried),
                                                      ("the honest refresh", [int(monday_1["lapsed"].sum()), int(monday_2["lapsed"].sum())])],
                    title="The win-back list on two Mondays with no new data")
        kit.check("two honest runs give the same table, cell for cell", monday_1.equals(monday_2))
        kit.check("the hurried version gives two different lists", hurried[0] != hurried[1], f"{hurried[0]} and {hurried[1]}")
        '''),
        md('''
        **What happened.** The answer is c: the two honest tables are equal cell for cell, because
        nothing in the refresh reads the calendar. The hurried version, counting to the run day, sent
        166 codes on the first Monday and 180 a week later, with no new data at all.

        > **Kavya's review.** "The table carries its as-of date, the smallest recency is 0, and a run that
        > fails a guard writes nothing. That is a refresh I will let Marketing act on without me."
        '''),

        md('''
        ## 6. Does the warehouse, counting on its own, find the same win-back list?

        The refresh counted the list with pandas: a `groupby`, a merge and a subtraction. The warehouse
        can count it with none of that code: each customer's last order, the table's own last date, and
        the customers more than 60 days apart. Subtracting two dates in Postgres gives whole days.
        '''),
        cq('''
        WIN_BACK = """@WB@"""
        by_sql = int(kit.sql(WIN_BACK)[0]["win_back"])
        kit.bars([("pandas refresh", int(monday_1["lapsed"].sum())), ("SQL, on its own", by_sql)],
                 title="The win-back list, counted twice")
        kit.check("SQL finds the same 111 customers the refresh flagged", by_sql == int(monday_1["lapsed"].sum()) == 111)
        ''', WB=q("c6", 1)),
        md('''
        **When to switch.** The refresh is the route for the table; the query is the route for anyone
        who wants to confirm the list's size without Python, such as the growth team's lead before a
        send.

        ### How would you answer this chapter's questions in an interview?

        **[F] How do you compute recency in a job that runs every week?** "From the data's last loaded
        date, carried in the table as its as-of date, never from the wall clock. Otherwise two runs on
        the same data disagree, and the list grows every week with nothing new loaded. The check is that
        the smallest recency is 0."

        **[D] What would you guard in a weekly refresh, and why those?** "The invariants a wrong table
        breaks: one row per key, rows equal to the source list, the money equal to the warehouse's
        total, and the as-of check. Each is compared with a number the warehouse gives on its own, and
        each raises an error, because a check that only prints lets the table ship."

        **[F] Your refresh stopped on a guard on Monday, before the send. What do you tell Marketing?** "That
        this Monday's table did not ship, which guard stopped it and what it found, and that last week's
        table is still the one to use until I fix the cause. A late table is a delay; a wrong table is a
        wrong send."

        ### Going deeper: how does pandas mirror Wednesday's falling flag?

        Wednesday flagged members whose monthly spend fell two months running with `LAG` in SQL, and
        found two traps on the way: reading another customer's month without `PARTITION BY`, and counting
        a skipped month as a fall. In pandas, `groupby("customer_id")["spend"].shift(1)` is `LAG`
        partitioned by customer, and shifting the month the same way lets the check require that the two
        earlier readings are really the two calendar months before. The cell compares the pandas flag with
        the warehouse's, customer by customer, without listing anyone.
        '''),
        cq('''
        monthly = (o.assign(month=o["order_date"].dt.to_period("M"))
                    .groupby(["customer_id", "month"], as_index=False)["amount"].sum()
                    .rename(columns={"amount": "spend"})
                    .sort_values(["customer_id", "month"]))
        g = monthly.groupby("customer_id")
        monthly = monthly.assign(spend_1=g["spend"].shift(1), spend_2=g["spend"].shift(2),
                                 month_1=g["month"].shift(1), month_2=g["month"].shift(2))
        sep = pd.Period("2026-09", "M")
        is_falling = ((monthly["month"] == sep) & (monthly["month_1"] == sep - 1) & (monthly["month_2"] == sep - 2)
                      & (monthly["spend"] < monthly["spend_1"]) & (monthly["spend_1"] < monthly["spend_2"]))
        flag_pd = set(monthly.loc[is_falling, "customer_id"])
        FALLING = """@FALL@"""
        flag_sql_count = int(kit.sql(FALLING)[0]["falling"])
        LIST = FALLING.replace("SELECT count(*) AS falling", "SELECT customer_id")
        flag_sql = {r["customer_id"] for r in kit.sql(LIST)}
        kit.check("pandas and SQL flag the same customers, customer by customer", flag_pd == flag_sql)
        kit.check("and the same number of them", len(flag_pd) == flag_sql_count)
        ''', FALL=q("c6", 2)),
        md('''
        **The answers, question by question.**

        1. One function with guards runs the refresh: it is the only option that stops all four of the
           day's failures before the table ships.
        2. The refresh is told two things, the warehouse connection and the feed's path, and reads the
           340 customers and their numbers from the data.
        3. Counted to the run day, 19 October, the win-back list holds 166 customers and the smallest
           recency is 21 days; counted to the data's last date, 28 September, it holds 111.
        4. Four guards stop a bad Monday, and each broken copy trips at least one while the honest table
           trips none.
        5. Two honest runs give the same table cell for cell; the hurried version gave 166 and then 180.
        6. The warehouse, counting on its own, finds the same 111.
        '''),
        code('''
        import pathlib
        out = pathlib.Path("output")
        out.mkdir(exist_ok=True)
        monday_1.to_csv(out / "C2_W02_D04_customer_table_STUDENT.csv", index=False)
        kit.flow(["warehouse + feed", "refresh()\\nbuild, count to as-of, guard", "output/ CSV\\n340 rows for Friday"],
                 lit=1, title="The Monday refresh, one call")
        kit.check("the refreshed table was written for Friday", (out / "C2_W02_D04_customer_table_STUDENT.csv").exists())
        kit.check_summary()
        print("Next: the escalated case builds the full Monday table alone, with both flags and one reshaped view.")
        '''),
    ]


# ============================================================================= the TODO twins
def twin(cells, answers, why, solution):
    """The TODO version, or the solution with every placeholder filled and a why-line after it.

    cells is a list of (kind, text, step) where kind is md or code; answers maps n to the code
    that fills __TODOn__; why maps a step number to the markdown that follows its code cell.
    """
    out, explained = [], set()
    for kind, text, step in cells:
        if kind == "md":
            text = textwrap.dedent(text).strip("\n")
            if solution and "__TODO" in text:
                paras = [x for x in text.split("\n\n") if "__TODO" not in x]
                paras.insert(1, "**The solution twin.** Every placeholder is filled with its key, the "
                                "notebook runs clean from a fresh kernel, and a line under each step says "
                                "why the other letters fail.")
                text = "\n\n".join(paras)
            out.append(md(text))
            continue
        src = textwrap.dedent(text).strip("\n")
        if solution:
            for n in sorted(answers, reverse=True):          # __TODO10__ before __TODO1__
                src = src.replace(f"__TODO{n}__", answers[n])
        out.append(code(src))
        if solution and step in why and step not in explained and "__TODO" in textwrap.dedent(text):
            out.append(md(why[step]))                    # once per step, after the cell it explains
            explained.add(step)
    return out


# ----------------------------------------------------------------------------- the escalated case
def escalated(solution):
    cells = [
        ("md", """
        # Can you build the growth team's Monday table alone, end to end?

        **Week 2, Thursday. The escalated case, unguided, 50 minutes.** The brief is
        `exercises/unguided/C2_W02_D04_escalated_case_STUDENT.md`, and this notebook is where its five
        parts run. Each step carries lettered choices written as comments above a `__TODOn__`
        placeholder: replace the placeholder with the code of the option you choose and run the step's
        check. Run as shipped, the notebook stops at `__TODO1__` with a `NameError`, which is how it is
        meant to start.

        > **The client asks.** "One table, one row per customer, refreshed every Monday: how recently,
        > how often, how much, the segment, whether the monsoon sale reached them, and the two flags we
        > act on. And one view of it by month that we can put on a slide."
        >
        > The growth team, Kalpa Retail

        **The data.** Kalpa Retail's warehouse holds 1,000 orders placed between April and September
        2026, Q1 (April to June) and Q2 (July to September), worth Rs 19,84,00,000 at the prices
        charged, and a customer list of 340 customers in four segments: Retail-Core and Retail-Plus,
        the two consumer tiers, of which Retail-Plus is the paid membership; Student; and Business,
        Kalpa's sales to companies. The campaign platform's feed lists the customers the monsoon sale
        reached in August 2026, with the date it reached each one. Spend is the value of a customer's
        orders at the prices charged, whatever became of each order afterwards.

        **The growth team's rules.** One row per customer on the list. A customer the feed names more
        than once was reached once, on the first date the feed gives. *Lapsed:* no order in the 60
        days to the table's as-of date, which step 3 asks you to choose; a customer who never ordered
        is not lapsed, since there is nothing to win back, and gets the first-order nudge instead. *Falling:* Wednesday's rule, spend lower in August than in July and lower again in
        September than in August, each reading a real calendar month after the one before, so a month
        with no order breaks the run.

        > **Kavya's review.** "It ships when the checks pass, not when it runs. Post your letters and
        > the four numbers the last cell prints."
        """, 0),
        ("md", "**Setup.** The next cell reads the orders and the customer list from the warehouse and "
               "the campaign platform's feed from the day's `data/` folder.", 0),
        ("code", LOAD + FEED, 0),
        ("code", """
        kit.side_by_side(
            kit.ladder(["every customer, three numbers", "the sale, one row each", "the two flags",
                        "one view for a slide", "one run, with guards"], show=False),
            kit.vflow(["the warehouse and the feed", "one table, one row per customer", "a slide, and a CSV for Friday"],
                      title="Five steps, each with its checks", show=False),
        )
        """, 0),
        ("md", """
        ## Step 1. Does the table hold every customer, with the three numbers each?

        Where it is used at work: every table a growth team acts on is a list of the people it acts on,
        and a person missing from it gets nothing.
        """, 0),
        ("code", """
        rfm = (orders.groupby("customer_id")
                     .agg(last_order=("order_date", "max"), frequency=("order_id", "count"),
                          spend=("amount", "sum"))
                     .reset_index())

        # TODO 1. Which frame should the table start from?
        #   a) orders
        #   b) rfm
        #   c) customers
        #   d) exposure.drop_duplicates("customer_id")
        table = __TODO1__.merge(rfm, on="customer_id", how="left", validate="one_to_one")

        # TODO 2. What goes in the frequency of a customer who never ordered?
        #   a) table["frequency"]
        #   b) table["frequency"].fillna(0).astype("int64")
        #   c) table["frequency"].fillna(table["frequency"].median())
        #   d) table["frequency"].dropna()
        table = table.assign(frequency=__TODO2__, spend=table["spend"].fillna(0))
        print(f"{len(table)} rows")
        """, 1),
        ("code", """
        in_list = kit.sql("SELECT count(*) AS n FROM customers")[0]["n"]
        kit.check("one row for every customer on the list", len(table) == in_list, f"{len(table)} rows")
        kit.check("spend adds back to the warehouse", table["spend"].sum() == orders["amount"].sum())
        kit.check("frequency is a whole number with no gaps", table["frequency"].dtype == "int64")
        """, 1),
        ("md", """
        ## Step 2. Which customers did the sale reach, one row each, and does a second count agree?

        Where it is used at work: any feed from another team's system is checked against the promise
        it makes before it is joined to a table other people act on.
        """, 0),
        ("code", """
        # TODO 3. After sorting by date, which argument applies the growth team's rule for a customer the feed names twice?
        #   a) keep="last"
        #   b) keep=False
        #   c) keep="first"
        #   d) ignore_index=True
        first_touch = (exposure.sort_values("exposed_date")
                               .drop_duplicates("customer_id", __TODO3__)[["customer_id", "exposed_date"]])

        # TODO 4. Which validate value should the merge carry?
        #   a) "one_to_many"
        #   b) "many_to_many"
        #   c) None
        #   d) "one_to_one"
        table = table.merge(first_touch, on="customer_id", how="left", validate=__TODO4__)
        table = table.assign(reached=table["exposed_date"].notna())

        # TODO 5. Which count, sharing no code with the rule or the merge, should equal the reached flags?
        #   a) len(first_touch)
        #   b) int(table["exposed_date"].notna().sum())
        #   c) exposure["customer_id"].nunique()
        #   d) len(exposure)
        second_count = __TODO5__
        print(f"{len(table)} rows after the merge")
        """, 2),
        ("code", """
        kit.check("still one row per customer after the merge", len(table) == in_list and table["customer_id"].is_unique)
        kit.check("spend did not move in the merge", table["spend"].sum() == orders["amount"].sum())
        kit.check("the second count agrees with the reached flags", int(second_count) == int(table["reached"].sum()))
        reach = table.groupby("segment")["reached"].sum().astype(int)
        kit.columns(reach.index.tolist(), [("reached by the sale", reach.tolist())],
                    title="Reached customers per segment, one row each")
        """, 2),
        ("md", """
        ## Step 3. Who has gone quiet, and whose monthly spend is falling?

        Where it is used at work: a retention team's weekly list is two flags, one for customers who
        stopped and one for customers who are slowing, and each has to mean the same thing every week.
        """, 0),
        ("code", """
        # TODO 6. Which date is the table's as-of date, the date recency is counted to?
        #   a) pd.Timestamp.today()
        #   b) orders["order_date"].max()
        #   c) orders["order_date"].min()
        #   d) pd.Timestamp.today().normalize()
        AS_OF = __TODO6__
        table = table.assign(as_of=AS_OF, recency_days=(AS_OF - table["last_order"]).dt.days)

        # TODO 7. Which condition flags a lapsed customer?
        #   a) table["recency_days"] > 60
        #   b) table["frequency"] == 0
        #   c) table["recency_days"].isna()
        #   d) (pd.Timestamp.today() - table["last_order"]).dt.days > 60
        table = table.assign(lapsed=__TODO7__)

        monthly = (orders.assign(month_num=orders["order_date"].dt.year * 12 + orders["order_date"].dt.month)
                         .groupby(["customer_id", "month_num"], as_index=False)["amount"].sum()
                         .rename(columns={"amount": "spend"})
                         .sort_values(["customer_id", "month_num"]))
        g = monthly.groupby("customer_id")
        # TODO 8. Which expression gives each row's previous monthly reading?
        #   a) monthly["spend"].shift(1)
        #   b) monthly.groupby("customer_id")["spend"].shift(1)
        #   c) monthly.groupby("month_num")["spend"].shift(1)
        #   d) monthly.groupby(["customer_id", "month_num"])["spend"].shift(1)
        monthly = monthly.assign(spend_1=__TODO8__, spend_2=g["spend"].shift(2),
                                 month_num_2=g["month_num"].shift(2))
        SEPTEMBER = 2026 * 12 + 9

        # TODO 9. Which test keeps a fall only when the two readings before September are July and August?
        #   a) monthly["month_num"] - monthly["month_num_2"] >= 2
        #   b) monthly["month_num_2"].notna()
        #   c) monthly["month_num"] - monthly["month_num_2"] <= 3
        #   d) monthly["month_num"] - monthly["month_num_2"] == 2
        real_months = __TODO9__
        falling = monthly[(monthly["month_num"] == SEPTEMBER) & real_months
                          & (monthly["spend"] < monthly["spend_1"]) & (monthly["spend_1"] < monthly["spend_2"])]
        table = table.assign(falling=table["customer_id"].isin(falling["customer_id"]))
        print("both flags are set")
        """, 3),
        ("code", """
        kit.check("the smallest recency is 0 days", table["recency_days"].min() == 0)
        by_sql = int(kit.sql(\"\"\"@WINBACK@\"\"\")[0]["win_back"])
        kit.check("the win-back list matches the warehouse's own count", int(table["lapsed"].sum()) == by_sql)
        wednesday = {r["customer_id"] for r in kit.sql(\"\"\"@FALLING_LIST@\"\"\")}
        kit.check("pandas flags exactly the customers Wednesday's calendar-checked LAG flags",
                  set(table.loc[table["falling"], "customer_id"]) == wednesday)
        kit.check("both flags are booleans", table["lapsed"].dtype == bool and table["falling"].dtype == bool)
        lap = table.groupby("segment")["lapsed"].sum().astype(int)
        kit.columns(lap.index.tolist(), [("lapsed, as of the table's as-of date", lap.tolist())],
                    title="The win-back list per segment")
        """, 3),
        ("md", """
        ## Step 4. How does spend move month by month in each segment?

        Where it is used at work: the slide a growth review opens on is a trend by segment, and the
        trend is only as right as the number behind each point.
        """, 0),
        ("code", """
        seg_orders = (orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
                            .assign(month=orders["order_date"].dt.to_period("M").astype(str)))
        # TODO 10. Which call builds the slide's view, months down the side and one column per segment?
        #   a) seg_orders.pivot_table(index="segment", columns="month", values="amount", aggfunc="sum")
        #   b) seg_orders.pivot_table(index="month", columns="segment", values="amount", aggfunc="sum")
        #   c) seg_orders.pivot_table(index="month", columns="segment", values="amount")
        #   d) seg_orders.pivot_table(index="month", columns="segment", values="amount", aggfunc="count")
        view = __TODO10__
        print("view shape:", view.shape)
        """, 4),
        ("code", """
        kit.check("the view adds back to the warehouse", view.values.sum() == orders["amount"].sum())
        kit.check("one row per month, April to September", list(view.index) == sorted(seg_orders["month"].unique()))
        kit.line(list(view.index), [(s, view[s].tolist(), "lit" if s == "Retail-Plus" else "")
                                    for s in ["Retail-Core", "Retail-Plus", "Student"]], fmt=kit.rupees,
                 title="The slide: consumer spend by month and segment")
        """, 4),
        ("md", """
        ## Step 5. Will the table rebuild itself next Monday and stop if something breaks?

        Where it is used at work: a scheduled job that feeds a campaign is trusted only when it
        refuses to write a table that fails its checks.
        """, 0),
        ("code", """
        def guard(t):
            # TODO 11. Which guard stops a table that has stopped being one row per customer?
            #   a) t["customer_id"].is_unique
            #   b) len(t) > 0
            #   c) t["spend"].sum() > 0
            #   d) t["customer_id"].notna().all()
            assert __TODO11__, "the customer table is no longer one row per customer"
            assert len(t) == in_list, "the table no longer holds every customer on the list"
            assert t["spend"].sum() == orders["amount"].sum(), "spend no longer adds to the warehouse"
            # TODO 12. Which guard catches recency counted to the wrong date?
            #   a) t["recency_days"].max() <= 180
            #   b) t["recency_days"].notna().all()
            #   c) t["as_of"].nunique() == 1
            #   d) t["recency_days"].min() == 0
            assert __TODO12__, "recency was not counted to the table's as-of date"
            return t

        run_1 = guard(table.copy())
        run_2 = guard(table.copy())
        print(len(run_1), "rows passed every guard")
        """, 5),
        ("code", """
        kit.check("two guarded runs give the same table", run_1.equals(run_2))
        broken = pd.concat([table, table.iloc[[150]]])
        with kit.expect_error() as stopped:
            guard(broken)
        kit.check("a repeated customer stops the run", stopped.name == "AssertionError")
        out = pathlib.Path("output"); out.mkdir(exist_ok=True)
        run_1.to_csv(out / "C2_W02_D04_customer_table_STUDENT.csv", index=False)
        kit.stats([(len(run_1), "customers", "one row each"), (kit.rupees(run_1["spend"].sum()), "spend", "adds to the warehouse"),
                   (int(run_1["reached"].sum()), "reached by the sale", "once each"),
                   (int(run_1["lapsed"].sum()), "on the win-back list", "as of the table's as-of date")])
        kit.flow(["warehouse + feed", "the table, guarded", "output/ CSV\\nfor Friday"], lit=1,
                 title="The Monday table, one guarded run")
        """, 5),
        ("md", """
        **The last question: what changes when the orders run to crores?** Next year the orders table
        may hold 5 crore rows, too many to read into pandas every Monday, while the growth team still
        wants the same three numbers for every customer who ordered. Step 1 would then read a
        query's answer in place of the orders.
        """, 0),
        ("code", """
        # TODO 13. Which query should step 1 read instead, so the three numbers still arrive?
        #   a) "SELECT customer_id, order_date, amount FROM orders"
        #   b) "SELECT customer_id, max(order_date) AS last_order, count(*) AS frequency, sum(amount) AS spend FROM orders GROUP BY customer_id"
        #   c) "SELECT customer_id, order_date, amount FROM orders WHERE order_date >= DATE '2026-07-01'"
        #   d) "SELECT customer_id, count(*) AS frequency FROM orders GROUP BY customer_id"
        at_scale = pd.read_sql(__TODO13__, ENG)
        print(len(at_scale), "rows came back from the warehouse")
        """, 6),
        ("code", """
        both = rfm.merge(at_scale, on="customer_id", how="outer", suffixes=("", "_sql"), indicator=True)
        same = (len(at_scale) == len(rfm) and (both["_merge"] == "both").all()
                and {"last_order", "frequency", "spend"} <= set(at_scale.columns)
                and (both["frequency"] == both["frequency_sql"]).all()
                and (both["spend"] == both["spend_sql"].astype(float)).all()
                and (both["last_order"] == pd.to_datetime(both["last_order_sql"])).all())
        kit.check("the warehouse's answer gives every ordering customer step 1's three numbers", same)
        kit.check("it sends one row per customer who ordered, whatever the orders' size", len(at_scale) == len(rfm))
        kit.check_summary()
        """, 6),
        ("md", """
        **Post:** your thirteen letters in order, and the four numbers above. The CSV in `output/` is
        what you bring to Friday.
        """, 0),
    ]
    subs = {"WINBACK": q("c6", 1), "FALLING_LIST": q("c6", 2).replace("SELECT count(*) AS falling", "SELECT customer_id")}
    cells = [(k, _fill(textwrap.dedent(t), subs), s) for k, t, s in cells]
    answers = {1: "customers", 2: 'table["frequency"].fillna(0).astype("int64")', 3: 'keep="first"',
               4: '"one_to_one"', 5: 'exposure["customer_id"].nunique()', 6: 'orders["order_date"].max()',
               7: 'table["recency_days"] > 60',
               8: 'monthly.groupby("customer_id")["spend"].shift(1)',
               9: 'monthly["month_num"] - monthly["month_num_2"] == 2',
               10: 'seg_orders.pivot_table(index="month", columns="segment", values="amount", aggfunc="sum")',
               11: 't["customer_id"].is_unique', 12: 't["recency_days"].min() == 0',
               13: '"SELECT customer_id, max(order_date) AS last_order, count(*) AS frequency, sum(amount) AS spend FROM orders GROUP BY customer_id"'}
    why = {
        1: "**Keys 1c and 2b.** 1a gives one row per order and 1b holds only the 301 customers who "
           "ordered; 1d holds only the customers the sale reached. 2a leaves 39 missing counts, which "
           "a filter for 0 never finds; 2c invents orders for customers who placed none; 2d removes "
           "nothing from the table's rows, since `assign` lines the shorter column up by index and "
           "leaves the gaps missing.",
        2: "**Keys 3c, 4d and 5c.** 3a keeps a later date wherever a customer repeats; 3b drops every "
           "copy of a repeated customer, so they read as never reached; 3d renumbers the rows and "
           "removes nothing. 4d is the only promise that the table stays one row per customer: 4c "
           "checks nothing, 4a allows repeats on the feed's side and 4b allows anything. 5c counts the "
           "distinct customers in the raw feed with no sort, no rule and no merge, so a wrong `keep` or "
           "a merge that lost someone makes it disagree with the flags. 5a counts the rows the rule "
           "kept, so it shares the rule: with `keep=False` it would shrink with the flags and still "
           "agree. 5b reads the merged table's own column, which is the flags again. 5d counts the "
           "feed's rows, one for every time the platform sent a customer, so it disagrees with a "
           "correct table.",
        3: "**Keys 6b, 7a, 8b and 9d.** 6a and 6d count to the day the notebook runs, so every "
           "customer looks staler than the data says and the list grows each Monday; 6c counts from "
           "April. 7b and 7c flag the customers who never ordered, who belong on the first-order list; "
           "7d is the wall-clock count again. 8a reads the previous row even when it belongs to another "
           "customer, Wednesday's LAG without PARTITION; 8c compares different customers in the same "
           "month; 8d puts each customer-month in a group of its own, so there is no previous row. 9d "
           "holds because the months are distinct and sorted: if the reading two back is exactly two "
           "months back, the one between is the month in between. 9b counts a skipped month as a "
           "fall, Wednesday's holiday member; 9a allows a gap; 9c allows one missing month.",
        4: "**Key 10b.** 10a puts segments on the rows when the slide wants months; 10c averages the "
           "orders in each cell, which is `pivot_table`'s default, so each point is a typical order "
           "and the view falls short of the warehouse; 10d counts orders instead of adding their value.",
        5: "**Keys 11a and 12d.** 11b and 11c pass on a table whose rows have doubled, and 11d passes "
           "on repeated ids, since a repeated id is not a missing one. 12a passes on a table counted "
           "to the wrong day as long as nobody is older than 180 days; 12b fails on every honest run, "
           "because customers who never ordered have no recency; 12c passes whatever single date was "
           "used.",
        6: "**Key 13b.** The warehouse groups the orders and sends one row per customer who ordered, "
           "301 today and the same 301 or so however many crores of orders sit behind them, so the "
           "pandas table reads that answer and merges it onto the list as before. 13a still sends every "
           "order, only with fewer columns; 13c sends only Q2's orders, so every number covers half the "
           "period; 13d sends the count and drops the last order date and spend. The check compares the "
           "query's answer with step 1's `groupby` customer by customer, so it is also a second route "
           "to the three numbers.",
    }
    return twin(cells, answers, why, solution)


def _fill(text, subs):
    for name, value in subs.items():
        text = text.replace(f"@{name}@", value)
    return text


# ----------------------------------------------------------------------------- the second case
def second_case(solution):
    cells = [
        ("md", """
        # Did Retail-Plus members order less often in Q2, in plain Python, SQL and pandas, and which tool would you sign?

        **Week 2, Thursday. The second case, in pairs, 40 minutes.** The brief is
        `exercises/unguided/C2_W02_D04_second_case_STUDENT.md`. Replace each `__TODOn__` with the code of
        the option you choose; run as shipped, the notebook stops at `__TODO1__` with a `NameError`.

        > **The client asks.** "You did the tree in plain Python in Week 1, in SQL on Monday. Do it a
        > third way now, and tell me honestly which tool you would pick for which job, and which one you
        > would refuse for Finance's numbers."
        >
        > Kavya Nair, senior analyst, Kalpa Retail data team

        The question all three tools answer is the branch of Week 1's revenue tree that moved:
        **Retail-Plus orders per member, Q1 against Q2**, where Q1 is April to June 2026 and Q2 is July
        to September. Retail-Plus is Kalpa Retail's paid membership tier, and a member counts in a
        quarter if they ordered in it. Orders per member is a quarter's orders divided by the members
        who ordered in that quarter, the retail dossier's frequency. Finance, under Anand Iyer, reruns
        its own numbers every Monday from the warehouse, Kalpa's Postgres database.
        """, 0),
        ("code", SETUP + "import pandas as pd\nENG = kit.engine()\nprint(\"connected to\", kit.WAREHOUSE[\"dbname\"])\n", 0),
        ("code", """
        kit.side_by_side(
            kit.ladder(["plain Python", "SQL", "pandas", "the note"], show=False),
            kit.flow(["plain Python\\nevery step visible", "SQL\\nwhere the data lives",
                      "pandas\\nthe analyst's bench"], title="Three tools, one number each", show=False),
        )
        """, 0),
        ("md", """
        ## Step 1. What does plain Python count, one row at a time?

        The rows arrive as a list of dictionaries, the shape of Week 1's orders: one per Retail-Plus
        order, with its customer and its quarter.
        """, 0),
        ("code", """
        rows = kit.sql('''SELECT o.order_id, o.customer_id, o.quarter FROM orders o
                          JOIN customers c ON c.customer_id = o.customer_id
                          WHERE c.segment = 'Retail-Plus' ''')
        orders_n = {"Q1": 0, "Q2": 0}
        ids = {"Q1": [], "Q2": []}
        for r in rows:
            orders_n[r["quarter"]] += 1
            ids[r["quarter"]].append(r["customer_id"])

        # TODO 1. How many members ordered in each quarter?
        #   a) {qq: len(ids[qq]) for qq in ids}
        #   b) {qq: len(set(ids[qq])) for qq in ids}
        #   c) {qq: len(set(ids["Q1"]) | set(ids["Q2"])) for qq in ids}
        #   d) {qq: len(set(ids["Q1"]) & set(ids["Q2"])) for qq in ids}
        members_n = __TODO1__
        py = {qq: orders_n[qq] / members_n[qq] for qq in ("Q1", "Q2")}
        print("plain Python:", {qq: round(v, 3) for qq, v in py.items()})
        """, 1),
        ("code", """
        kit.check("plain Python counts every Retail-Plus order", sum(orders_n.values()) == len(rows))
        kit.check("each quarter's members are fewer than its orders", all(members_n[qq] < orders_n[qq] for qq in orders_n))
        kit.table(["quarter", "orders", "members", "orders per member"],
                  [(qq, orders_n[qq], members_n[qq], f"{py[qq]:.3f}") for qq in ("Q1", "Q2")], caption="Plain Python")
        """, 1),
        ("md", """
        ## Step 2. Does SQL, where the data lives, give the same number?
        """, 0),
        ("code", """
        # TODO 2. Which expression gives orders per member, to three places?
        #   a) orders / members
        #   b) orders::numeric / members
        #   c) members::numeric / orders
        #   d) orders::numeric / (SELECT count(*) FROM customers)
        # TODO 3. Which line keeps only Retail-Plus?
        #   a) WHERE c.segment = 'Retail-Plus'
        #   b) HAVING c.segment = 'Retail-Plus'
        #   c) WHERE c.segment LIKE 'Retail%'
        #   d) WHERE c.segment <> 'Business'
        SQL = '''WITH q AS (SELECT o.quarter, count(*) AS orders, count(DISTINCT o.customer_id) AS members
                            FROM orders o JOIN customers c ON c.customer_id = o.customer_id
                            __TODO3__
                            GROUP BY o.quarter)
                 SELECT quarter, orders, members, round(__TODO2__, 3) AS per_member
                 FROM q ORDER BY quarter'''
        sql_rows = kit.sql(SQL)
        sq = {r["quarter"]: float(r["per_member"]) for r in sql_rows}
        print("SQL:", sq)
        """, 2),
        ("code", """
        kit.check("SQL returns one row per quarter", [r["quarter"] for r in sql_rows] == ["Q1", "Q2"])
        kit.check("SQL agrees with plain Python to three places", all(abs(sq[qq] - py[qq]) < 0.001 for qq in sq), sq)
        """, 2),
        ("md", """
        ## Step 3. Does pandas, the analyst's bench, give the same number?
        """, 0),
        ("code", """
        df = pd.read_sql('''SELECT o.order_id, o.customer_id, o.quarter, c.segment FROM orders o
                            JOIN customers c ON c.customer_id = o.customer_id''', ENG)
        rp = df[df["segment"] == "Retail-Plus"]
        orders_pd = rp.groupby("quarter")["order_id"].count()
        # TODO 4. Which method gives each quarter's members?
        #   a) count
        #   b) size
        #   c) value_counts
        #   d) nunique
        members_pd = rp.groupby("quarter")["customer_id"].__TODO4__()
        pn = (orders_pd / members_pd).to_dict()
        print("pandas:", {qq: round(v, 3) for qq, v in pn.items()})
        """, 3),
        ("code", """
        kit.check("pandas agrees with plain Python", all(abs(pn[qq] - py[qq]) < 1e-9 for qq in ("Q1", "Q2")))
        kit.check("pandas agrees with SQL to three places", all(abs(pn[qq] - sq[qq]) < 0.001 for qq in ("Q1", "Q2")))
        kit.columns(["Q1", "Q2"], [("plain Python", [round(py[qq], 3) for qq in ("Q1", "Q2")]),
                                   ("SQL", [sq[qq] for qq in ("Q1", "Q2")]),
                                   ("pandas", [round(pn[qq], 3) for qq in ("Q1", "Q2")])],
                    fmt=lambda v: f"{v:.3f}", title="Retail-Plus orders per member: three tools, one number")
        """, 3),
        ("md", """
        ## Step 4. Which tool would you sign for each job, and which size tells the three apart?

        The three agree, so the choice is about who has to trust, rerun or audit the number, and about
        what each route cost to reach it. A size that gives all three the same score separates nothing.
        """, 0),
        ("code", """
        # TODO 5. Which size tells the three routes apart, listed as plain Python, SQL, pandas?
        #   a) [len(py), len(sq), len(pn)]                      the rows in each answer
        #   b) [sum(orders_n.values()), sum(r["orders"] for r in sql_rows), int(orders_pd.sum())]
        #                                                       the orders each route counted
        #   c) [len(rows), len(sql_rows), len(rp)]              the rows each route held after keeping Retail-Plus
        #   d) [len(rows), len(sql_rows), len(df)]              the rows each route fetched from the warehouse
        size = dict(zip(["plain Python", "SQL", "pandas"], __TODO5__))
        kit.bars(list(size.items()), title="The size you chose, route by route, for the same two numbers")

        # TODO 6. Where should a number Finance reruns every Monday be computed?
        #   a) "a pandas notebook on the analyst's machine"
        #   b) "a plain Python loop"
        #   c) "a SQL query in the warehouse"
        #   d) "a CSV export refreshed every Monday"
        finance_home = __TODO6__
        kit.matrix(["plain Python", "SQL", "pandas"], ["explain line by line", "rerun where the data lives", "iterate on a question"],
                   [["best: every step visible", "no: runs on a copy", "slow to change"],
                    ["reads as one statement", "best: Finance reruns it", "a new query each time"],
                    ["reads as a chain", "no: runs on a copy", "best: the analyst's bench"]],
                   title="The tool-choice note, as a grid")
        """, 4),
        ("code", """
        kit.check("the three tools agree on both quarters",
                  all(abs(py[qq] - pn[qq]) < 1e-9 and abs(py[qq] - sq[qq]) < 0.001 for qq in ("Q1", "Q2")))
        kit.check("the size you chose tells the three routes apart", len(set(size.values())) == 3)
        kit.check("on that size, SQL is the smallest", min(size, key=size.get) == "SQL")
        kit.check("a home was chosen for Finance's number", isinstance(finance_home, str) and len(finance_home) > 0)
        fall = pn["Q2"] / pn["Q1"] - 1
        kit.bridge(("Q1, orders per member", round(pn["Q1"], 3)), [("the change", round(pn["Q2"] - pn["Q1"], 3))],
                   end_label="Q2", fmt=lambda v: f"{v:.3f}", lit=(0,),
                   title=f"Retail-Plus orders per member changed {fall:.0%} from Q1 to Q2: the branch Week 1 found")
        kit.check_summary()
        """, 4),
        ("md", """
        **Post:** your six letters, and your tool-choice note in the brief's format: one line per tool
        with the job it owns and the rows it fetched, and the tool you would refuse for Finance's
        numbers, with the reason.
        """, 0),
    ]
    answers = {1: "{qq: len(set(ids[qq])) for qq in ids}", 2: "orders::numeric / members",
               3: "WHERE c.segment = 'Retail-Plus'", 4: "nunique",
               5: "[len(rows), len(sql_rows), len(df)]", 6: '"a SQL query in the warehouse"'}
    why = {
        1: "**Key 1b.** 1a counts every order as a member, so orders per member reads 1.000 in both "
           "quarters: rows counted as customers, Week 1 Monday's trap. 1c divides both quarters by the "
           "107 members who ordered in either quarter, and 1d by the 60 who ordered in both, so each "
           "rate stands on members who did not order in that quarter; SQL, which counts each quarter's "
           "members on their own, disagrees with both in the next step.",
        2: "**Keys 2b and 3a.** 2a is Monday's trap: Postgres divides two whole numbers and returns 2 "
           "and 1. 2c turns the rate upside down. 2d divides by all 340 customers on the list, every "
           "segment, whoever ordered. 3b fails, because `HAVING` filters groups and the segment is not "
           "one of them; 3c keeps Retail-Core as well, since `LIKE 'Retail%'` matches both consumer "
           "tiers; 3d keeps Retail-Core and the Students.",
        3: "**Key 4d.** `count` (a) and `size` (b) count rows, which are orders, so the rate reads "
           "1.000; `value_counts` (c) returns one count per member, a Series the division cannot line "
           "up with the quarters.",
        4: "**Keys 5d and 6c.** 5d counts the rows each route fetched from the warehouse: plain Python "
           "355, SQL 2 and pandas 1,000, since pandas read every order before keeping Retail-Plus. 5a "
           "gives 2, 2 and 2, the answers themselves, which tie; 5b gives 355 three times, the orders "
           "every route counted; 5c gives 355, 2 and 355, the rows pandas kept after its filter, which "
           "hides the 645 other orders it fetched. Finance's number lives where Finance can rerun and "
           "audit it, in the warehouse, as a query that sends only its answer (6c). A notebook (6a) and "
           "a loop (6b) run on a copy on one machine; an export (6d) is a copy that ages from the "
           "moment it is written.",
    }
    return twin(cells, answers, why, solution)


def case1():
    build(NB / "C2_W02_D04_ex1_escalated_case_STUDENT.ipynb", escalated(False), execute=False)
    build(SOL / "C2_W02_D04_ex1_escalated_case_solution_STUDENT.ipynb", escalated(True))


def case2():
    build(NB / "C2_W02_D04_ex2_second_case_STUDENT.ipynb", second_case(False), execute=False)
    build(SOL / "C2_W02_D04_ex2_second_case_solution_STUDENT.ipynb", second_case(True))


if __name__ == "__main__":
    wanted = set(sys.argv[1:]) or {"sql", "c1", "c2", "c3", "c4", "c5", "c6", "x1", "x2"}
    names = {"c1": "C2_W02_D04_01_customer_table_STUDENT.ipynb",
             "c2": "C2_W02_D04_02_exposure_merge_STUDENT.ipynb",
             "c3": "C2_W02_D04_03_months_pivot_STUDENT.ipynb",
             "c4": "C2_W02_D04_04_three_tools_STUDENT.ipynb",
             "c5": "C2_W02_D04_05_tool_choice_STUDENT.ipynb",
             "c6": "C2_W02_D04_06_monday_refresh_STUDENT.ipynb"}
    chapters = {"c1": ch1, "c2": ch2, "c3": ch3, "c4": ch4, "c5": ch5, "c6": ch6}
    if "sql" in wanted:
        write_sql()
    for key, fn in chapters.items():
        if key in wanted:
            build(NB / names[key], fn())
            print("built", names[key])
    if "x1" in wanted:
        case1()
        print("built the escalated case and its solution")
    if "x2" in wanted:
        case2()
        print("built the second case and its solution")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W02/D4/internal/C2_W02_D04_build_notebooks_INTERNAL.py
#     Writes seven sql/ files and eight notebooks plus two solution twins; each chapter notebook
#     executes cold and ends with every check passing.
# python3 content/W02/D4/internal/C2_W02_D04_build_notebooks_INTERNAL.py c3
#     Rebuilds only notebook 03; nothing else is touched.
# Running it with the warehouse down
#     Stops in the first chapter's setup cell with the helper's message naming load_warehouse.sh.

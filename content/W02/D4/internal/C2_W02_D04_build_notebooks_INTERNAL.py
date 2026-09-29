"""Write and execute every notebook of Week 2 Thursday from one place.

    python3 content/W02/D4/internal/C2_W02_D04_build_notebooks_INTERNAL.py          # all
    python3 content/W02/D4/internal/C2_W02_D04_build_notebooks_INTERNAL.py 1 2      # rounds 1 and 2

Needs the warehouse running (bash .devcontainer/load_warehouse.sh) and pandas, SQLAlchemy and
psycopg2 installed. Each notebook is executed cold in its own folder by scripts/nb_make.py, so the
saved outputs are the ones a learner's Codespace produces.
"""
import pathlib
import sys
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, md, code, empty, build  # noqa: E402

DAY = ROOT / "content" / "W02" / "D4"
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"

LOAD = SETUP + '''import pandas as pd

ENG = kit.engine()
orders = pd.read_sql(
    "SELECT order_id, customer_id, order_date, quarter, channel, amount, status FROM orders",
    ENG, parse_dates=["order_date"])
customers = pd.read_sql("SELECT customer_id, segment, city FROM customers", ENG)
print(f"{len(orders):,} orders and {len(customers):,} customers read from the warehouse")
'''

ROUNDS = ["Round 1: one row per customer", "Round 2: the exposure merge",
          "Round 3: the months view", "Afternoon: the Monday table",
          "Afternoon: three tools, one question"]


def ladder(lit):
    return f"kit.ladder({ROUNDS!r}, lit={lit}, show=False)"


# --------------------------------------------------------------------------- round 1
def round1():
    cells = [
        md("""
        # One row per customer, from the warehouse

        **Week 2, Thursday. Round 1 of 3.** The question: who are Kalpa Retail's customers, as one
        row each, with how recently they bought, how often and how much?

        > **The client's ask.** The growth team wants one table, refreshed every Monday, with one row
        > per customer. The data platform lead is blunt: "The warehouse queries are fine for Finance,
        > but Marketing's analysts live in Python. Build them the table in pandas, from the warehouse,
        > and make it refreshable in one run."

        > **Kavya's review.** "Before the table goes to Marketing I want three things: the row count
        > against the customer list, the spend total against Monday's revenue, and the date every
        > recency was measured from."

        What the week has established: Monday's queries rebuilt the revenue tree from the warehouse,
        Tuesday made the join fan-out visible, and Wednesday ranked members and flagged falling spend
        with window functions. Today every one of those moves comes back in pandas, and each one is
        something you have already done by hand.
        """),
        md("""
        **Setup.** Find the shared helper, connect to the warehouse and read two tables into pandas.
        If the connection fails, run `bash .devcontainer/load_warehouse.sh` in the terminal and run
        this cell again.
        """),
        code(LOAD),
        code(f"""
        kit.side_by_side(
            {ladder(0)},
            kit.vflow(["split\\nthe 1,000 order rows, by customer_id",
                       "apply\\nlast date, count, sum, to each group",
                       "combine\\none row per customer"],
                      title="groupby is the Week 1 accumulator, automated", show=False),
        )
        """),
        md("""
        ## 1. The warehouse arrives as a DataFrame, and its count matches Monday's

        `pd.read_sql` runs the query in Postgres and hands back a DataFrame, one column per selected
        field. Monday's first query counted 1,000 orders in the warehouse, so that is the number the
        frame has to hold before anything else is trusted.

        **Predict before you run.** What does `orders.dtypes` report for `amount` and `customer_id`?
        a) both `object`; b) `float64` and `str`; c) `int64` and `str`; d) `Decimal` and `object`.
        """),
        code("""
        kit.table(["column", "dtype in pandas 3", "what it means for the table"],
                  [("order_id", str(orders["order_id"].dtype), "text: one row per order"),
                   ("customer_id", str(orders["customer_id"].dtype), "text: the key the table groups on"),
                   ("order_date", str(orders["order_date"].dtype), "a real date, so days can be subtracted"),
                   ("amount", str(orders["amount"].dtype), "a number pandas can sum"),
                   ("status", str(orders["status"].dtype), "text: delivered, returned or cancelled")],
                  caption="What read_sql built from the warehouse's orders table")
        sql_count = kit.sql("SELECT count(*) AS n FROM orders")[0]["n"]
        kit.check("the frame holds every order the warehouse holds", len(orders) == sql_count,
                  f"{len(orders):,} rows in pandas, {sql_count:,} in Postgres")
        kit.check("amount arrived as a number", orders["amount"].dtype == "float64")
        """),
        md("""
        **What happened.** The answer is b. Postgres stores `amount` as `numeric(12,2)`, which pandas
        reads as `float64`, and pandas 3 reads text as its own `str` dtype, where pandas 2 said
        `object`. Old tutorials that test `dtype == object` for text now miss every text column.
        `parse_dates=["order_date"]` is what turned the date into a real date; without it the
        subtraction in section 4 would fail.
        """),
        code("""
        by_q = orders.groupby("quarter").agg(orders=("order_id", "count"), revenue=("amount", "sum"))
        kit.columns(["Q1", "Q2"], [("orders", by_q["orders"].tolist())],
                    width=640, title="Orders per quarter, read into pandas: the same counts as Monday's query")
        kit.check("the two quarters add back to 1,000 orders", by_q["orders"].sum() == 1000)
        kit.check("booked revenue is Rs 19,84,00,000, Monday's two-quarter total",
                  orders["amount"].sum() == 198_400_000, kit.rupees(orders["amount"].sum()))
        """),
        md("""
        ## 2. groupby is the accumulator you wrote in Week 1

        In Week 1 you built spend per customer with a dictionary: start empty, visit every order,
        add its amount to that customer's running total. `groupby` does the same three moves, split,
        apply and combine, in one line.

        **Predict before you run.** How many rows will spend per customer have?
        a) 1,000, one per order; b) 340, one per customer in the warehouse; c) 301; d) 4, one per
        segment.
        """),
        code("""
        spend = {}                                   # the Week 1 accumulator
        for row in orders.itertuples():
            spend[row.customer_id] = spend.get(row.customer_id, 0) + row.amount

        per_customer = orders.groupby("customer_id")["amount"].sum()   # the same, automated

        kit.table(["customer_id", "the loop", "groupby"],
                  [(cid, kit.rupees(spend[cid]), kit.rupees(per_customer[cid]))
                   for cid in per_customer.sort_values(ascending=False).index[:5]],
                  caption="The five biggest spenders, two ways")
        kit.check("the loop and groupby agree for every customer",
                  all(spend[c] == v for c, v in per_customer.items()), f"{len(per_customer)} customers")
        kit.check("groupby returns one row per customer who ordered", len(per_customer) == len(spend))
        """),
        code("""
        top = per_customer.sort_values(ascending=False).head(8)
        kit.bars([(cid, int(v)) for cid, v in top.items()], fmt=kit.rupees,
                 title="The eight biggest spenders: every one a Business account")
        consumer = orders.merge(customers, on="customer_id", validate="many_to_one")
        consumer = consumer[consumer["segment"] != "Business"].groupby("customer_id")["amount"].sum()
        bands = pd.cut(consumer, [0, 2500, 5000, 10000, 20000, 60000],
                       labels=["up to 2.5k", "2.5k to 5k", "5k to 10k", "10k to 20k", "over 20k"])
        counts = bands.value_counts().sort_index()
        kit.columns(counts.index.tolist(), [("consumer customers", counts.tolist())],
                    width=640, title="Spend per consumer customer over two quarters, in rupee bands")
        """),
        md("""
        **What happened.** The answer is c: 301 rows. `groupby` can only make a group for a key it
        sees, and 39 customers in the warehouse never placed an order, so the order rows never
        mention them. The loop had the same blind spot in Week 1. For a table that must hold every
        customer, the list of customers is the spine and the order totals are attached to it,
        which is section 3.
        """),
        md("""
        ## 3. Named aggregations build recency, frequency and spend in one call

        Three questions per customer, answered in one pass over the groups. The SQL you wrote on
        Monday and the pandas line say the same thing:

        | SQL | pandas |
        |---|---|
        | `GROUP BY customer_id` | `orders.groupby("customer_id")` |
        | `max(order_date) AS last_order` | `last_order=("order_date", "max")` |
        | `count(*) AS frequency` | `frequency=("order_id", "count")` |
        | `sum(amount) AS monetary` | `monetary=("amount", "sum")` |
        | `customers LEFT JOIN ...` | `customers.merge(..., how="left", validate="one_to_one")` |

        **Predict before you run.** After the left merge onto the customer list, what dtype does
        `frequency` have? a) `int64`, since counts are whole numbers; b) `float64`; c) `str`;
        d) `bool`.
        """),
        code("""
        rfm = (orders.groupby("customer_id")
                     .agg(last_order=("order_date", "max"),
                          frequency=("order_id", "count"),
                          monetary=("amount", "sum"))
                     .reset_index())
        table = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
        print(table.dtypes.to_string())
        kit.check("one row per customer in the warehouse", len(table) == len(customers),
                  f"{len(table)} rows against {len(customers)} customers")
        kit.check("spend still adds to Monday's total after the merge",
                  table["monetary"].sum() == orders["amount"].sum(), kit.rupees(table["monetary"].sum()))
        """),
        md("""
        **What happened.** The answer is b. The 39 customers with no orders get `NaN` for
        `frequency`, and a column holding `NaN` cannot stay `int64`, so pandas quietly made it
        `float64`. Nothing errors; the dtype just changed on the way through the chain. The fix says
        what a missing count means in this business: a customer with no orders has frequency 0 and
        spend 0.
        """),
        code("""
        table = table.assign(frequency=table["frequency"].fillna(0).astype("int64"),
                             monetary=table["monetary"].fillna(0))
        seg = table.groupby("segment").agg(customers=("customer_id", "count"),
                                           buyers=("frequency", lambda s: int((s > 0).sum())))
        kit.columns(seg.index.tolist(), [("customers", seg["customers"].tolist()),
                                         ("bought at least once", seg["buyers"].tolist())],
                    width=640, title="Every segment holds customers who never ordered")
        kit.check("frequency is a whole number again", table["frequency"].dtype == "int64")
        kit.check("39 customers carry frequency 0", int((table["frequency"] == 0).sum()) == 39)
        """),
        md("""
        ## 4. The trap: recency measured from today

        The growth team's first use of the table is a win-back list: every customer with no order in
        the last 60 days gets a discount code. Recency is days since the last order. The obvious
        line measures it from today, and the table first ships on Monday 19 October.

        **The plausible wrong answer.** A hurried analyst writes `pd.Timestamp.today()`. On the
        first Monday refresh that returns 19 October 2026, so the cell below pins that date to show
        exactly what the refresh would have shipped.

        **Predict before you run.** How many customers land on the win-back list?
        a) 111; b) 166; c) 301; d) 55.
        """),
        code("""
        RUN_DAY = pd.Timestamp("2026-10-19")   # what pd.Timestamp.today() returns on the first refresh
        wrong = (RUN_DAY - table["last_order"]).dt.days
        wrong_list = int((wrong > 60).sum())
        kit.stats([(wrong_list, "on the win-back list", "no order in 60 days, measured from the run day"),
                   (int(wrong.min()), "smallest recency, days", "the most recent buyer, as the table says")])
        """),
        md("""
        **What happened.** The answer is b: 166 customers. **Why it is wrong.** The warehouse's last
        order is dated 28 September; nothing after it has been loaded. Measured from the run day,
        every customer looks 21 days staler than the data says, so customers who bought a fortnight
        before the extract closed are sent a win-back discount. Run the same notebook next Monday and
        the list grows again with no new data, which makes the table a function of the calendar.

        **The check that catches it.** Somebody always bought on the data's last day, so the
        smallest recency in an honest table is 0. Here it is 21.
        """),
        code("""
        AS_OF = orders["order_date"].max()
        kit.check("the data's last date is 28 September 2026", AS_OF == pd.Timestamp("2026-09-28"), str(AS_OF.date()))
        kit.check("the wrong recency's smallest value is 21 days, the gap between the two dates",
                  int(wrong.min()) == (RUN_DAY - AS_OF).days, f"{int(wrong.min())} days")
        """),
        md("""
        **The fix.** Measure recency from the data's own last date, `orders["order_date"].max()`,
        and write that date into the table so the growth team sees what "as of" means.
        """),
        code("""
        table = table.assign(recency_days=(AS_OF - table["last_order"]).dt.days, as_of=AS_OF)
        right_list = int((table["recency_days"] > 60).sum())
        kit.bridge(("from the run day", wrong_list),
                   [("active, wrongly listed", right_list - wrong_list)],
                   end_label="from 28 September", fmt=lambda v: f"{v:,.0f}", lit=(0,),
                   title="The win-back list: 55 active customers were about to get a discount")
        kit.check("the honest smallest recency is 0 days", table["recency_days"].min() == 0)
        kit.check("the honest win-back list holds 111 customers", right_list == 111, f"{right_list}")
        """),
        code("""
        edges = [-1, 30, 60, 90, 120, 200]
        names = ["0 to 30", "31 to 60", "61 to 90", "91 to 120", "over 120"]
        right_b = pd.cut(table["recency_days"].dropna(), edges, labels=names).value_counts().sort_index()
        wrong_b = pd.cut(wrong.dropna(), edges, labels=names).value_counts().sort_index()
        kit.columns(names, [("from the run day", wrong_b.tolist()), ("from 28 September", right_b.tolist())],
                    title="Days since the last order: the whole table slides right by 21 days", lit=(2, 3, 4))
        lapsed = pd.DataFrame({"from the run day": (wrong > 60).groupby(table["segment"]).sum(),
                               "from the data's last date": (table["recency_days"] > 60).groupby(table["segment"]).sum()})
        kit.columns(lapsed.index.tolist(), [(c, lapsed[c].astype(int).tolist()) for c in lapsed.columns],
                    title="The win-back list by segment, both ways")
        """),
        md("""
        > **Kavya's review.** "The table now carries its as-of date, and the smallest recency is 0,
        > which is the check I will run every Monday. Tell Marketing the list is 111 customers and why
        > it is not 166, in one sentence, before they ask."

        ### In the interview

        **[S] groupby in the split-apply-combine sentence.** "groupby splits the rows into one group
        per key, applies a calculation to each group, and combines the results into one row per key.
        For a customer table: split the orders by customer_id, apply max of the date, a count and a
        sum, and combine into one row per customer. It is SQL's GROUP BY, and it is the accumulator
        dictionary from a Python loop, written once."

        **Follow-up an interviewer adds: why did your table have fewer rows than the customer
        list?** "groupby only knows the keys it sees in the rows it was given, so customers with no
        orders never form a group. I start from the customer list and left-merge the aggregates,
        with validate set, then fill the missing counts with 0 on purpose."

        **Follow-up: how would you compute recency in a job that runs every week?** "From the
        data's last loaded date, stored in the table as its as-of date, never from the wall clock,
        or two runs on the same data disagree."

        ### Depth: `transform`, the pandas mirror of a window function

        `agg` shrinks each group to one row, like GROUP BY. `transform` returns one value per
        original row, like Wednesday's `SUM(...) OVER (PARTITION BY ...)`. Each customer's share of
        their segment's spend is one line.
        """),
        code("""
        table = table.assign(share_of_segment=table["monetary"] / table.groupby("segment")["monetary"].transform("sum"))
        shares = table.groupby("segment")["share_of_segment"].sum().round(6)
        kit.check("every segment's shares add to 1, as a window SUM over a partition would",
                  bool((shares == 1).all()), shares.to_dict())
        kit.table(["customer_id", "segment", "recency_days", "frequency", "monetary", "share_of_segment"],
                  [(r.customer_id, r.segment, int(r.recency_days), r.frequency, kit.rupees(r.monetary),
                    f"{r.share_of_segment:.1%}")
                   for r in table.sort_values("monetary", ascending=False).head(6).itertuples()],
                  caption="The table so far, largest spenders first")
        """),
        code("""
        kit.table(["What this round established", "The evidence"],
                  [("read_sql brings the warehouse into pandas, and the count must match", "1,000 orders, as on Monday"),
                   ("groupby is the Week 1 accumulator, automated", "loop and groupby agree for 301 customers"),
                   ("the customer list is the spine of the table", "340 rows, 39 of them with no orders"),
                   ("a merge with NaN silently changes a dtype", "frequency became float64, fixed to int64"),
                   ("recency is measured from the data's last date", "win-back list 111, not 166")],
                  caption="Round 1")
        kit.flow(["customers\\n340 rows", "+ groupby aggregates\\nleft merge, validated",
                  "recency\\nfrom 28 September"], lit=2, title="The spine of the Monday table")
        kit.check_summary()
        print("Next: round 2 attaches the monsoon sale's exposure feed to this table.")
        """),
    ]
    build(NB / "C2_W02_D04_01_customer_table_STUDENT.ipynb", cells)


TABLE = '''
AS_OF = orders["order_date"].max()
rfm = (orders.groupby("customer_id")
             .agg(last_order=("order_date", "max"), frequency=("order_id", "count"),
                  monetary=("amount", "sum"))
             .reset_index())
table = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
table = table.assign(frequency=table["frequency"].fillna(0).astype("int64"),
                     monetary=table["monetary"].fillna(0),
                     recency_days=(AS_OF - table["last_order"]).dt.days)
print(f"round 1's table: {len(table)} customers, as of {AS_OF.date()}")
'''

FEED = '''
exposure = pd.read_csv(kit.data_dir() / "C2_W02_D04_exposure_STUDENT.csv", parse_dates=["exposed_date"])
print("exposure feed columns:", list(exposure.columns))
'''


# --------------------------------------------------------------------------- round 2
def round2():
    cells = [
        md("""
        # The exposure merge: did the monsoon sale reach who we think?

        **Week 2, Thursday. Round 2 of 3.** The question: which customers did August's monsoon sale
        reach, and how many of them bought?

        > **The client's ask.** The marketing lead, owner of acquisition and campaigns: "Put the
        > monsoon sale on the customer table. I want to see, per segment, who it reached and how many
        > of them bought, because I am asking for the same budget in November."

        > **Kavya's review.** "A merge is a join, so I want Tuesday's habit: the row count before and
        > after, and the spend total before and after. If either moves, the merge is wrong until
        > you can say why."

        Round 1 built one row per customer: 340 rows, spend adding to Rs 19,84,00,000, recency
        measured from 28 September. This round attaches a second source to it.
        """),
        md("""
        **Setup.** The warehouse tables, round 1's table rebuilt in a few lines, and the exposure
        feed. The feed arrives as a file from the campaign platform, one row per customer the sale
        reached, or so the platform says.
        """),
        code(LOAD + TABLE + FEED),
        code(f"""
        kit.side_by_side(
            {ladder(1)},
            kit.vflow(["the customer table\\none row per customer",
                       "the exposure feed\\none row per customer? check it",
                       "merge on customer_id\\nwith the count before and after",
                       "validate='one_to_one'\\nthe count check, made loud"],
                      title="A merge is a join, and a join can multiply rows", show=False),
        )
        """),
        md("""
        ## 1. A merge is a join, with the same four shapes

        | SQL on Tuesday | pandas today | keeps |
        |---|---|---|
        | `INNER JOIN` | `merge(how="inner")`, the default | only keys on both sides |
        | `LEFT JOIN` | `merge(how="left")` | every row of the left table |
        | `RIGHT JOIN` | `merge(how="right")` | every row of the right table |
        | `FULL OUTER JOIN` | `merge(how="outer")` | every key from either side |

        The customer table is the spine, so the merge is `how="left"`: every customer stays, and the
        feed adds a date where it has one.

        **Predict before you run.** `merge` with no `how` keeps which customers?
        a) every customer; b) only customers in the feed, since the default is inner; c) every feed
        row, even unknown customers; d) none, because `how` is required.
        """),
        code("""
        inner = table.merge(exposure[["customer_id"]].drop_duplicates(), on="customer_id")
        reached = exposure.groupby(
            exposure["customer_id"].map(table.set_index("customer_id")["segment"]))["customer_id"].nunique()
        kit.columns(reached.index.tolist(), [("customers the feed names", reached.tolist())],
                    width=640, title="The feed only names Retail-Core and Retail-Plus customers")
        kit.check("the default merge is inner: only customers named in the feed survive",
                  inner["customer_id"].nunique() == exposure["customer_id"].nunique(),
                  f"{inner['customer_id'].nunique()} of {len(table)} customers")
        kit.check("every customer the feed names is in the customer table",
                  exposure["customer_id"].isin(table["customer_id"]).all())
        """),
        md("""
        **What happened.** The answer is b. `merge` defaults to an inner join, which silently drops
        every customer the sale did not reach, and the unreached are exactly the comparison group
        Marketing needs. Write `how=` every time, so the reader of the code knows which rows
        survive.

        ## 2. The trap: a merge that doubles a customer's spend

        The mechanism first, on four invented customers so it can be seen whole. **These records are
        invented for the mechanism; they are not Kalpa's.** The campaign platform sends its feed in
        batches, and when a batch is re-sent, a customer arrives twice.
        """),
        code("""
        small = pd.DataFrame({"customer_id": ["C-9001", "C-9002", "C-9003", "C-9004"],
                              "segment": ["Retail-Plus", "Retail-Core", "Retail-Plus", "Student"],
                              "monetary": [12400, 8600, 5100, 1900]})
        small_feed = pd.DataFrame({"customer_id": ["C-9001", "C-9002", "C-9002", "C-9003"],
                                   "exposed_date": pd.to_datetime(["2026-08-03", "2026-08-03",
                                                                   "2026-08-11", "2026-08-03"])})
        kit.side_by_side(
            kit.flow(["C-9001\\nRs 12,400", "C-9002\\nRs 8,600", "C-9003\\nRs 5,100", "C-9004\\nRs 1,900"],
                     title="Invented customers: 4 rows", show=False),
            kit.flow(["C-9001\\n3 Aug", "C-9002\\n3 Aug", "C-9002\\n11 Aug, re-sent", "C-9003\\n3 Aug"],
                     kinds=[None, None, "bad", None], title="Invented feed: 4 rows, 3 customers", show=False),
        )
        """),
        md("""
        **The plausible wrong answer.** The analyst merges, filters to the customers the sale
        reached, and sums their spend for the marketing lead's slide.

        **Predict before you run.** What does the slide say the reached customers spent?
        a) Rs 26,100; b) Rs 28,000; c) Rs 34,700; d) Rs 17,200.
        """),
        code("""
        naive = small.merge(small_feed, on="customer_id", how="left")
        wrong_spend = int(naive.loc[naive["exposed_date"].notna(), "monetary"].sum())
        kit.table(["customer_id", "monetary", "exposed_date"],
                  [(r.customer_id, kit.rupees(r.monetary), "" if pd.isna(r.exposed_date) else str(r.exposed_date.date()))
                   for r in naive.itertuples()], caption=f"{len(small)} customers in, {len(naive)} rows out")
        kit.stats([(kit.rupees(wrong_spend), "spend of reached customers", "what the slide would say"),
                   (len(naive), "rows after the merge", "from 4 customers")])
        """),
        md("""
        **What happened.** The answer is c: Rs 34,700. **Why it is wrong.** C-9002 appears twice in
        the feed, so the merge gives C-9002 two rows and the sum counts Rs 8,600 twice. Every row
        looks right on its own, which is why nobody spots it by reading the table. The slide
        overstates what the reached customers spent by a third and makes the case for the November
        budget with money nobody paid.

        **The check that catches it.** Tuesday's habit, the row count before and after. Four
        customers went in and five rows came out. `validate=` makes the same check loud: it raises
        before a wrong table exists.
        """),
        code("""
        with kit.expect_error() as err:
            small.merge(small_feed, on="customer_id", how="left", validate="one_to_one")
        kit.check("the count check: rows grew from 4 to 5", len(small) == 4 and len(naive) == 5)
        kit.check("validate='one_to_one' raises pandas.errors.MergeError",
                  err.name == "MergeError", err.message.splitlines()[0])
        kit.check("the error says the right-hand keys are not unique",
                  "not unique in right dataset" in err.message)
        """),
        code("""
        right_spend = int(small.loc[small["customer_id"].isin(small_feed["customer_id"]), "monetary"].sum())
        kit.bridge(("reached, counted once", right_spend), [("C-9002 counted again", wrong_spend - right_spend)],
                   end_label="what the slide said", lit=(0,),
                   title="Invented records: one re-sent row adds a customer's whole spend again")
        kit.check("the gap is exactly C-9002's spend", wrong_spend - right_spend == 8600)
        """),
        md("""
        **Your turn, on Kalpa's feed.** Type these three lines into the empty cell and read each
        answer aloud before the next:

        ```python
        exposure["customer_id"].duplicated().sum()
        len(table), len(table.merge(exposure, on="customer_id", how="left"))
        table.merge(exposure, on="customer_id", how="left", validate="one_to_one")
        ```

        Then say, in one sentence to the marketing lead, what the naive merge would have done to the
        spend of the customers the sale reached.
        """),
        empty(),
        md("""
        ## 3. The fix: decide what one exposure means, then let validate guard it

        A duplicate is a business question before it is a pandas one: a customer the sale reached
        twice was still reached once. The rule for this table is **one row per customer, their
        first exposure date**. Sort by date, keep the first row per customer, and merge with
        `validate="one_to_one"` so a feed that breaks the rule next Monday stops the refresh.
        """),
        code("""
        first_touch = (exposure.sort_values("exposed_date")
                               .drop_duplicates("customer_id", keep="first")[["customer_id", "exposed_date"]])
        with kit.expect_error() as clean:
            merged = table.merge(first_touch, on="customer_id", how="left", validate="one_to_one")
        merged = merged.assign(exposed=merged["exposed_date"].notna())
        kit.check("validate passes once the rule is applied", clean.name is None)
        kit.check("the row count did not move: 340 in, 340 out", len(merged) == len(table) == 340)
        kit.check("spend did not move: Rs 19,84,00,000 before and after",
                  merged["monetary"].sum() == table["monetary"].sum(), kit.rupees(merged["monetary"].sum()))
        kit.check("exposed customers equal the distinct customers in the feed",
                  int(merged["exposed"].sum()) == exposure["customer_id"].nunique(), int(merged["exposed"].sum()))
        """),
        code("""
        cons = merged[merged["segment"].isin(["Retail-Core", "Retail-Plus"])]
        avg = cons.groupby(["segment", "exposed"])["monetary"].mean().unstack()
        kit.columns(avg.index.tolist(), [("not reached", avg[False].round(0).tolist()),
                                         ("reached", avg[True].round(0).tolist())], fmt=kit.rupees,
                    width=640, title="Average two-quarter spend per customer, reached or not")
        """),
        md("""
        **What the chart does not say.** Reached customers spent more on average in both segments.
        Week 1 Thursday already showed why that is not the sale's effect: the platform targets
        customers who were buying anyway. The table records exposure; it does not prove the sale
        worked, and the marketing lead will hear that from Kavya if not from you.

        ## 4. The trap: groupby drops the customers with no segment

        The marketing lead's second question: of the customers the sale reached, how many bought?
        A hurried analyst starts from the feed, since those are the customers the question is about,
        and attaches round 1's order totals, which carry the segment from the order rows.

        **The plausible wrong answer.**

        **Predict before you run.** What share of reached customers does the table say bought?
        a) 82 percent; b) 100 percent; c) 50 percent; d) it cannot be computed.
        """),
        code("""
        buyers = (orders.merge(customers, on="customer_id", validate="many_to_one")
                        .groupby("customer_id")
                        .agg(segment=("segment", "first"), frequency=("order_id", "count"))
                        .reset_index())
        reach_wrong = buyers.merge(first_touch, on="customer_id", how="right", validate="one_to_one")
        by_seg_wrong = reach_wrong.groupby("segment").agg(reached=("customer_id", "count"),
                                                          bought=("frequency", "count"))
        kit.table(["segment", "reached", "bought", "share"],
                  [(s, r.reached, r.bought, f"{r.bought / r.reached:.0%}") for s, r in by_seg_wrong.iterrows()],
                  caption="What the slide would say")
        kit.stats([(f"{by_seg_wrong['bought'].sum() / by_seg_wrong['reached'].sum():.0%}", "of reached customers bought",
                    "the wrong table's headline"),
                   (int(by_seg_wrong["reached"].sum()), "customers reached", "by the wrong table's count")])
        """),
        md("""
        **What happened.** The answer is b: 100 percent, on 107 customers reached. **Why it is
        wrong.** The segment came from the order rows. A customer the sale reached who never ordered
        has no order rows, so the right merge gives them a row with no segment, and `groupby` drops
        a missing key by default (`dropna=True`). The customers who were reached and did not buy
        are exactly the ones that vanished, so the table reports perfect conversion to a marketing
        lead who is about to ask for the same budget again.

        **The check that catches it.** The groups must add back to the rows. `dropna=False` shows
        the missing group, and the sum of `reached` against the feed's distinct customers shows the
        gap without looking at a single row.
        """),
        code("""
        shown = reach_wrong.groupby("segment", dropna=False)["customer_id"].count()
        kit.table(["segment", "customers"], [("(missing)" if pd.isna(k) else k, v) for k, v in shown.items()],
                  caption="The same groupby with dropna=False")
        kit.check("the default groupby lost 23 reached customers",
                  len(reach_wrong) - int(by_seg_wrong["reached"].sum()) == 23)
        kit.check("the lost customers are exactly the reached customers with no orders",
                  int(reach_wrong["segment"].isna().sum()) == int(reach_wrong["frequency"].isna().sum()) == 23)
        """),
        md("""
        **The fix.** Take the segment from the customer list, which has one for every customer,
        which means starting from `merged`, the validated table from section 3.
        """),
        code("""
        conv = merged[merged["exposed"]].groupby("segment").agg(
            reached=("customer_id", "count"), bought=("frequency", lambda s: int((s > 0).sum())))
        kit.bridge(("reached, the wrong table", int(by_seg_wrong["reached"].sum())),
                   [("reached, never ordered", int(conv["reached"].sum() - by_seg_wrong["reached"].sum()))],
                   end_label="reached, the customer list", fmt=lambda v: f"{v:,.0f}", lit=(0,),
                   title="Reach: 23 customers were missing from the wrong table")
        kit.columns(conv.index.tolist(), [("reached", conv["reached"].tolist()), ("bought", conv["bought"].tolist())],
                    width=640, title="Reached and bought, per segment, from the customer list")
        share = conv["bought"].sum() / conv["reached"].sum()
        kit.check("130 reached and 107 bought: 82 percent, where the wrong table said 100",
                  conv["reached"].sum() == 130 and conv["bought"].sum() == 107, f"{share:.1%}")
        """),
        md("""
        > **Kavya's review.** "Two numbers moved in this round and neither raised an error on its
        > own: spend that a re-sent row inflated, and reach that a missing key shrank. The row
        > count before and after, and groups that add back to their rows, caught both. Put both
        > checks in the refresh."

        ### In the interview

        **[S] merge against join: what is the same and what differs?** "The same: both match rows
        on a key, both come in inner, left, right and outer, and both multiply rows when a key
        repeats on the side you did not expect. The differences: pandas defaults to inner, so I
        always write `how=`; pandas runs in memory on data I already pulled, where the warehouse
        joins where the data lives; and pandas can refuse the wrong shape with `validate=`, which
        SQL has no single argument for."

        **[F] Which merge argument raises on duplicate keys, and which error?** "`validate`, with
        `one_to_one`, `one_to_many` or `many_to_one`. When the keys break the promise it raises
        `pandas.errors.MergeError`, saying which side's keys are not unique. It is the row-count
        check made loud: it stops the table being built instead of reporting after the fact."

        **Follow-up: your merge raised MergeError on Monday's refresh. What do you do?** "I do not
        drop duplicates to make it pass. I look at the duplicated keys, find out why the source
        sent them, and apply a business rule, here first exposure per customer, then keep
        `validate` so the next surprise also stops the run."

        **Follow-up: why did your groupby lose customers?** "`groupby` drops missing keys by
        default. I check that the groups add back to the rows, and I pass `dropna=False` when a
        missing group is information."

        ### Depth: `indicator=True`, the anti-join in pandas

        Tuesday's anti-join, rows on one side with no match on the other, is one argument in pandas:
        `indicator=True` adds a `_merge` column saying where each row came from.
        """),
        code("""
        both = table.merge(first_touch, on="customer_id", how="left", indicator=True, validate="one_to_one")
        counts = both["_merge"].value_counts()
        kit.table(["_merge", "customers", "reads as"],
                  [("both", int(counts.get("both", 0)), "the sale reached them"),
                   ("left_only", int(counts.get("left_only", 0)), "on the customer list, never reached"),
                   ("right_only", int(counts.get("right_only", 0)), "in the feed, unknown to the customer list")],
                  caption="indicator=True on the customer list against the first-touch feed")
        kit.check("no customer in the feed is unknown to the warehouse", int(counts.get("right_only", 0)) == 0)
        """),
        code("""
        kit.table(["What this round established", "The evidence"],
                  [("merge is a join, and its default is inner", "the unreached disappear without how='left'"),
                   ("a repeated key multiplies rows and money", "invented: Rs 26,100 became Rs 34,700"),
                   ("validate= turns the count check into a MergeError", "raised before a wrong table existed"),
                   ("a duplicate needs a business rule", "first exposure per customer: 340 rows, spend unchanged"),
                   ("groupby drops missing keys by default", "reach 107 at 100 percent, truly 130 at 82 percent")],
                  caption="Round 2")
        kit.flow(["customer table\\n340 rows", "first touch per customer\\nthe rule",
                  "merge, validate one_to_one\\n340 rows out", "group from the customer list\\nno missing keys"],
                 lit=2, title="The exposure merge, as it runs every Monday")
        kit.check_summary()
        print("Next: round 3 turns the orders into a months view, and meets pivot_table's default.")
        """),
    ]
    build(NB / "C2_W02_D04_02_exposure_merge_STUDENT.ipynb", cells)


# --------------------------------------------------------------------------- round 3
def round3():
    cells = [
        md("""
        # The months view: is Retail-Plus the tier that is slipping?

        **Week 2, Thursday. Round 3 of 3.** The question: what did each Retail-Plus member spend in
        each month from April to September, and how far did the tier fall from Q1 to Q2?

        > **The client's ask.** The head of Retail-Plus: "Give me one row per member and one column
        > per month. I want to read along a row and see who is drifting, and I want the tier's fall
        > from Q1 to Q2 in one number I can take to the review."

        > **Kavya's review.** "A reshape changes the question a table answers, and a pivot also
        > aggregates, whether you asked it to or not. Show me the grand total of your pivot next to
        > the total of the orders it came from."

        Round 1 built the table, round 2 attached the sale. This round changes its shape: months as
        columns to compare, months as rows to follow a trend.
        """),
        md("**Setup.** The warehouse tables, a month label on every order, and the Retail-Plus orders."),
        code(LOAD + '''
orders = orders.assign(month=orders["order_date"].dt.to_period("M").astype(str))
plus = orders.merge(customers, on="customer_id", validate="many_to_one").query("segment == 'Retail-Plus'")
MONTHS = sorted(orders["month"].unique())
print(f"{len(plus)} Retail-Plus orders from {plus['customer_id'].nunique()} members, months {MONTHS[0]} to {MONTHS[-1]}")
'''),
        code(f"""
        kit.side_by_side(
            {ladder(2)},
            kit.flow(["long\\none row per member per month", "wide\\none column per month",
                      "long again\\nmelt"], lit=1, title="pivot widens, melt lengthens", show=False),
        )
        """),
        md("""
        ## 1. The long table: one row per member per month

        Before any pivot, the grain the head of Retail-Plus asked about is member and month. Two
        keys in the `groupby` give one row per pair that actually has orders.

        **Predict before you run.** How many rows does the long table have?
        a) 355, one per order; b) 642, members times months; c) 266; d) 107.
        """),
        code("""
        long = plus.groupby(["customer_id", "month"], as_index=False)["amount"].sum()
        tier = long.groupby("month")["amount"].sum()
        kit.line(MONTHS, [("Retail-Plus spend, the true monthly total", tier.tolist(), "lit")], fmt=kit.rupees,
                 title="Retail-Plus spend by month, April to September")
        kit.check("the long table keeps every rupee", long["amount"].sum() == plus["amount"].sum(),
                  kit.rupees(long["amount"].sum()))
        kit.check("one row per member-month that has orders", len(long) == 266, f"{len(long)} rows")
        """),
        code("""
        kit.table(["customer_id", "month", "amount"],
                  [(r.customer_id, r.month, kit.rupees(r.amount)) for r in long.head(6).itertuples()],
                  caption="The long table's first rows: one member, one month, one total")
        kit.columns(["Q1", "Q2"], [("Retail-Plus spend", [int(tier[MONTHS[:3]].sum()), int(tier[MONTHS[3:]].sum())])],
                    fmt=kit.rupees, width=640, title="The tier by quarter, from the long table")
        """),
        md("""
        **What happened.** The answer is c: 266. A member-month with no orders has no row at all, so
        the long table is shorter than 107 members times 6 months. The line is the number to hold
        on to: the tier took Rs 5,85,770 in Q1 and Rs 4,13,380 in Q2.

        ## 2. The trap: pivot_table averages unless you tell it to add

        **The plausible wrong answer.** The analyst asks for months as columns in one line and sums
        each column for the tier's monthly spend.

        **Predict before you run.** What fall from Q1 to Q2 does that pivot report?
        a) 29 percent; b) 18 percent; c) 0 percent; d) it raises an error.
        """),
        code("""
        wide_wrong = plus.pivot_table(index="customer_id", columns="month", values="amount")
        col_wrong = wide_wrong.sum()
        q1_w, q2_w = col_wrong[MONTHS[:3]].sum(), col_wrong[MONTHS[3:]].sum()
        kit.stats([(kit.rupees(round(q1_w)), "Q1, from the pivot", "April to June"),
                   (kit.rupees(round(q2_w)), "Q2, from the pivot", "July to September"),
                   (f"{q2_w / q1_w - 1:.0%}", "the fall it reports", "what the review would hear")])
        """),
        md("""
        **What happened.** The answer is b: a fall of 18 percent. **Why it is wrong.**
        `pivot_table`'s default `aggfunc` is `"mean"`, so a member who ordered four times in June
        shows the average of the four orders, and the column sums add up averages. The average
        order hides how often members bought, and frequency is the lever Week 1 found moving in
        Retail-Plus. The true fall is 29 percent, so the head of Retail-Plus would walk into the
        review defending a problem two-thirds of its real size.

        **The check that catches it.** A pivot of spend must hold the same total as the orders it
        came from. Here the grand total is short by a quarter.
        """),
        code("""
        grand_wrong = wide_wrong.sum().sum()
        kit.check("the averaged pivot does not add back to the orders", round(grand_wrong) != plus["amount"].sum(),
                  f"{kit.rupees(round(grand_wrong))} against {kit.rupees(plus['amount'].sum())}")
        kit.bars([("orders, summed", int(plus["amount"].sum())), ("pivot, default aggfunc", round(grand_wrong))],
                 fmt=kit.rupees, lit=(1,), title="The grand-total check: the pivot is short by a quarter")
        """),
        code("""
        member = "C-0152"
        kit.table(["month", "orders", "the pivot shows", "the member spent"],
                  [(m, int((plus["customer_id"].eq(member) & plus["month"].eq(m)).sum()),
                    "" if pd.isna(wide_wrong.loc[member, m]) else kit.rupees(wide_wrong.loc[member, m]),
                    kit.rupees(plus.loc[plus["customer_id"].eq(member) & plus["month"].eq(m), "amount"].sum()))
                   for m in MONTHS], caption=f"One member, {member}, read along the row")
        kit.check("in June the pivot shows this member's average order, a quarter of the month's spend",
                  wide_wrong.loc[member, "2026-06"] * 4 == plus.loc[plus["customer_id"].eq(member)
                                                                    & plus["month"].eq("2026-06"), "amount"].sum())
        """),
        md("""
        **The fix.** Say what the cell means: `aggfunc="sum"` adds a member's orders in the month,
        and `fill_value=0` writes a month with no orders as 0 spend rather than a gap.
        """),
        code("""
        wide = plus.pivot_table(index="customer_id", columns="month", values="amount", aggfunc="sum", fill_value=0)
        col = wide.sum()
        q1, q2 = col[MONTHS[:3]].sum(), col[MONTHS[3:]].sum()
        kit.line(MONTHS, [("summed, the true total", col.tolist(), "lit"),
                          ("averaged, the default", col_wrong.round(0).tolist(), "bad")], fmt=kit.rupees,
                 title="The same months, two aggfuncs: the default hides a quarter of the spend")
        kit.bridge(("Q1 to Q2, averaged pivot", round(q2_w - q1_w)), [("frequency the mean hid", round((q2 - q1) - (q2_w - q1_w)))],
                   end_label="Q1 to Q2, summed", title="The fall in rupees: the averaged pivot understates it",
                   lit=(0,))
        kit.check("the summed pivot adds back to every Retail-Plus order", wide.values.sum() == plus["amount"].sum(),
                  kit.rupees(wide.values.sum()))
        kit.check("the true fall from Q1 to Q2 is 29 percent", round(q2 / q1 - 1, 3) == -0.294, f"{q2 / q1 - 1:.1%}")
        """),
        md("""
        **Your turn.** The head of Retail-Core asks for the same view of her members. In the empty
        cell, build it with `aggfunc="sum"` and `fill_value=0`, then check its grand total against
        the Retail-Core orders before you read a single month. Say the Q1 to Q2 change aloud.
        """),
        empty(),
        md("""
        ## 3. A pivot on the wrong index answers a question nobody asked

        The index decides what one row is. Index by `order_id` and every order becomes a row,
        which is a table of orders with five empty cells in each, and it looks like a months view
        until somebody reads the row labels aloud.

        **Predict before you run.** What shape is the pivot indexed by `order_id`?
        a) 107 rows by 6 columns; b) 355 rows by 6 columns; c) 6 rows by 107 columns;
        d) 120 rows by 6 columns.
        """),
        code("""
        by_order = plus.pivot_table(index="order_id", columns="month", values="amount", aggfunc="sum")
        kit.table(["index", "shape", "first row label", "one row is"],
                  [("customer_id", str(wide.shape), wide.index[0], "a member"),
                   ("order_id", str(by_order.shape), by_order.index[0], "an order")],
                  caption="Read the row labels aloud before reading any number")
        kit.columns(["members on the list", "members who ordered", "rows, order index"],
                    [("rows", [int((customers["segment"] == "Retail-Plus").sum()), len(wide), len(by_order)])],
                    width=640, title="Three row counts, and only one answers the head of Retail-Plus")
        kit.check("the member view has one row per member who ordered", len(wide) == plus["customer_id"].nunique())
        kit.check("the order-indexed pivot has one row per order", len(by_order) == len(plus))
        """),
        md("""
        **What happened.** The answer is b: 355 rows, one per Retail-Plus order. Its totals are
        right, which is why it survives a glance; its rows are orders, so "who is drifting" cannot
        be read from it at all. The member view has 107 rows, and the 13 members on the list who
        never ordered are absent from both, which is a decision to state when the view goes out.

        ## 4. Two shapes, two questions: compare wide, follow long

        Months as columns answer a comparison: did this member spend less in Q2 than in Q1? Months
        as rows answer a trend, and `melt` turns the wide table back into long.
        """),
        code("""
        q = wide.assign(Q1=wide[MONTHS[:3]].sum(axis=1), Q2=wide[MONTHS[3:]].sum(axis=1))
        kit.table(["customer_id", "Q1", "Q2", "change"],
                  [(cid, kit.rupees(r.Q1), kit.rupees(r.Q2), kit.rupees(r.Q2 - r.Q1))
                   for cid, r in q.sort_values("Q1", ascending=False).head(5).iterrows()],
                  caption="The comparison view: the five biggest Q1 members, Q1 against Q2")
        fell = int((q["Q2"] < q["Q1"]).sum())
        kit.columns(["spent less in Q2", "spent more in Q2"], [("members", [fell, int((q["Q2"] > q["Q1"]).sum())])],
                    width=640, title="The comparison view: members whose Q2 spend fell below their Q1 spend")
        back = wide.reset_index().melt(id_vars="customer_id", var_name="month", value_name="spend")
        kit.check("melt gives 107 members times 6 months", len(back) == 107 * 6, f"{len(back)} rows")
        kit.check("melt keeps every rupee", back["spend"].sum() == plus["amount"].sum())
        """),
        code("""
        seg = (orders.merge(customers, on="customer_id", validate="many_to_one")
                     .pivot_table(index="month", columns="segment", values="amount", aggfunc="sum"))
        kit.line(MONTHS, [(s, seg[s].tolist(), "lit" if s == "Retail-Plus" else "") for s in
                          ["Retail-Core", "Retail-Plus", "Student"]], fmt=kit.rupees,
                 title="The trend view, months as rows: Retail-Plus is the consumer tier that fell")
        kit.check("the segment view adds to the book, Rs 19,84,00,000", seg.values.sum() == 198_400_000)
        """),
        md("""
        > **Kavya's review.** "Q1 Rs 5,85,770, Q2 Rs 4,13,380, a fall of 29 percent, from a pivot
        > whose grand total equals the orders. The averaged version would have told the review 18.
        > Write `aggfunc=` every time, the way you write `how=` on a merge."

        ### In the interview

        **[F] pivot against melt: which widens and which lengthens?** "`pivot` and `pivot_table`
        widen: the values of one column become new columns, so a long table of member and month
        becomes one row per member with a column per month. `melt` lengthens: it folds columns back
        into rows, giving one row per member per month. I pivot to compare across a row and melt to
        plot or group a trend."

        **Follow-up: your pivot's totals look low. Where do you look first?** "At `aggfunc`.
        `pivot_table` averages by default, so if the cells should be totals I pass `aggfunc='sum'`
        and check the grand total against the source."

        **Follow-up: pivot or pivot_table?** "`pivot` only reshapes, so it raises when a row and
        column pair repeats; `pivot_table` aggregates repeats, silently, with the mean unless told
        otherwise. When I expect one value per cell, `pivot` is the loud check."

        ### Depth: `pivot` is the loud version of `pivot_table`
        """),
        code("""
        with kit.expect_error() as loud:
            plus.pivot(index="customer_id", columns="month", values="amount")
        kit.check("pivot refuses to reshape when a member has two orders in a month",
                  loud.name == "ValueError" and "duplicate entries" in loud.message, loud.message)
        """),
        code("""
        kit.table(["What this round established", "The evidence"],
                  [("the long table is the member-month grain", "266 rows, every rupee kept"),
                   ("pivot_table averages by default", "the tier's fall read 18 percent; it is 29"),
                   ("a pivot's grand total must equal its source", "Rs 7,49,286 against Rs 9,99,150"),
                   ("the index decides what one row is", "355 order rows against 107 members"),
                   ("wide compares, long follows a trend", "67 members spent less in Q2; melt gives 642 rows")],
                  caption="Round 3")
        kit.flow(["long\\n266 rows", "pivot_table, aggfunc='sum'\\n107 by 6", "melt\\n642 rows"], lit=1,
                 title="The months view, with the aggregation said out loud")
        kit.check_summary()
        print("Next: the afternoon builds the whole Monday table unguided, then asks the question a third way.")
        """),
    ]
    build(NB / "C2_W02_D04_03_months_pivot_STUDENT.ipynb", cells)


# --------------------------------------------------------------------------- the TODO twins
def twin(cells, answers, why, solution):
    """The TODO version, or the solution with every placeholder filled and a why-line after it.

    cells is a list of (kind, text, step) where kind is md or code; answers maps n to the code
    that fills __TODOn__; why maps a step number to the markdown that follows its code cell.
    """
    out = []
    for kind, text, step in cells:
        if kind == "md":
            if solution and "__TODO" in text:
                paras = [x for x in textwrap.dedent(text).strip("\n").split("\n\n") if "__TODO" not in x]
                paras.insert(1, "**The solution twin.** Every placeholder is filled with its key, the "
                                "notebook runs clean from a fresh kernel, and a line under each step says "
                                "why the other letters fail.")
                text = "\n\n".join(paras)
            out.append(md(text))
            continue
        src = text
        if solution:
            for n, fill in answers.items():
                src = src.replace(f"__TODO{n}__", fill)
        out.append(code(src))
        if solution and step in why:
            out.append(md(why[step]))
    return out


def escalated(solution):
    cells = [
        ("md", """
        # The Monday table, end to end

        **Week 2, Thursday. The escalated case, unguided, 60 minutes.** The brief is
        `exercises/unguided/C2_W02_D04_escalated_STUDENT.md`. Each step below has one or two
        lettered choices written as comments above a `__TODOn__` placeholder: replace the
        placeholder with the option you choose and run the step's check. Run as shipped, the
        notebook stops at `__TODO1__` with a NameError, which is how it is meant to start.

        > **The client's ask.** The growth team: "One table, one row per customer, refreshed every
        > Monday: how recently, how often, how much, the segment, whether the monsoon sale reached
        > them, and the flags. And one view of it by month we can put on a slide."

        > **Kavya's review.** "It ships when the checks pass, not when it runs. Post your letters
        > and the four numbers the last cell prints."
        """, 0),
        ("md", "**Setup.** The same warehouse read as the morning, and the exposure feed.", 0),
        ("code", LOAD + FEED, 0),
        ("code", f"""
        kit.side_by_side(
            {ladder(3)},
            kit.vflow(["1. the spine and the aggregates", "2. the exposure, validated",
                       "3. the two flags", "4. one reshaped view", "5. one run, the same answer"],
                      title="Five steps, five checks", show=False),
        )
        """, 0),
        ("md", """
        ## Step 1. The spine and the aggregates

        One row per customer in the warehouse, with recency, frequency and spend, recency measured
        so that two runs on the same data agree.
        """, 0),
        ("code", """
        rfm = (orders.groupby("customer_id")
                     .agg(last_order=("order_date", "max"), frequency=("order_id", "count"),
                          monetary=("amount", "sum"))
                     .reset_index())

        # TODO 1. Which frame is the spine of a table that must hold every customer?
        #   a) orders
        #   b) rfm
        #   c) customers
        #   d) exposure
        table = __TODO1__.merge(rfm, on="customer_id", how="left", validate="one_to_one")

        # TODO 2. Recency is measured from which date?
        #   a) pd.Timestamp.today()
        #   b) orders["order_date"].max()
        #   c) orders["order_date"].min()
        #   d) pd.Timestamp("2026-10-15")
        AS_OF = __TODO2__
        table = table.assign(frequency=table["frequency"].fillna(0).astype("int64"),
                             monetary=table["monetary"].fillna(0),
                             recency_days=(AS_OF - table["last_order"]).dt.days)
        print(f"{len(table)} rows, recency as of {AS_OF.date()}")
        """, 1),
        ("code", """
        kit.check("one row per customer in the warehouse", len(table) == 340, f"{len(table)} rows")
        kit.check("spend adds to Monday's book", table["monetary"].sum() == orders["amount"].sum())
        kit.check("the smallest recency is 0 days", table["recency_days"].min() == 0)
        """, 1),
        ("md", """
        ## Step 2. The exposure, validated

        One exposure per customer, the first date the sale reached them, and a merge that stops the
        refresh if the feed ever breaks that rule.
        """, 0),
        ("code", """
        # TODO 3. Which argument keeps one row per customer, their first exposure?
        #   a) keep="last"
        #   b) keep=False
        #   c) keep="first"
        #   d) ignore_index=True
        first_touch = (exposure.sort_values("exposed_date")
                               .drop_duplicates("customer_id", __TODO3__)[["customer_id", "exposed_date"]])

        # TODO 4. Which validate value guards a table that must stay one row per customer?
        #   a) "one_to_many"
        #   b) "many_to_many"
        #   c) None
        #   d) "one_to_one"
        table = table.merge(first_touch, on="customer_id", how="left", validate=__TODO4__)
        table = table.assign(exposed=table["exposed_date"].notna())
        print(f"{int(table['exposed'].sum())} customers reached by the sale")
        """, 2),
        ("code", """
        kit.check("still 340 rows after the merge", len(table) == 340)
        kit.check("spend did not move in the merge", table["monetary"].sum() == orders["amount"].sum())
        kit.check("every customer the feed names is marked exposed",
                  int(table["exposed"].sum()) == exposure["customer_id"].nunique())
        reach = table.groupby("segment")["exposed"].sum().astype(int)
        kit.columns(reach.index.tolist(), [("reached by the sale", reach.tolist())], width=640,
                    title="Reached customers per segment, one row each")
        """, 2),
        ("md", """
        ## Step 3. The two flags

        **Lapsed:** no order in the 60 days to the data's last date; a customer who never ordered
        is not lapsed, since there is nothing to win back. **Falling:** Q2 monthly spend fell twice
        running, the pandas mirror of Wednesday's LAG query, which the check runs beside it.
        """, 0),
        ("code", """
        # TODO 5. Which condition flags a lapsed customer?
        #   a) table["recency_days"] > 60
        #   b) table["recency_days"] >= 6
        #   c) table["frequency"] == 0
        #   d) table["recency_days"].isna()
        table = table.assign(lapsed=__TODO5__)

        monthly = (orders[orders["quarter"] == "Q2"]
                   .assign(month=orders["order_date"].dt.to_period("M").astype(str))
                   .groupby(["customer_id", "month"], as_index=False)["amount"].sum()
                   .rename(columns={"amount": "spend"})
                   .sort_values(["customer_id", "month"]))
        # TODO 6. The previous month's spend for the same customer is:
        #   a) monthly["spend"].shift(1)
        #   b) monthly.groupby("customer_id")["spend"].shift(1)
        #   c) monthly["spend"].diff()
        #   d) monthly.groupby("month")["spend"].shift(1)
        monthly = monthly.assign(prev=__TODO6__)
        falls = (monthly["spend"] < monthly["prev"]).groupby(monthly["customer_id"]).sum()

        # TODO 7. Which customers carry the falling flag?
        #   a) falls[falls >= 2].index
        #   b) falls[falls == 1].index
        #   c) falls[falls > 2].index
        #   d) falls[falls > 0].index
        table = table.assign(falling=table["customer_id"].isin(__TODO7__))
        print(f"{int(table['lapsed'].sum())} customers lapsed; the falling flag is set")
        """, 3),
        ("code", """
        LAG_SQL = '''
        WITH m AS (SELECT customer_id, date_trunc('month', order_date) AS month, sum(amount) AS spend
                   FROM orders WHERE quarter = 'Q2' GROUP BY 1, 2),
             l AS (SELECT *, LAG(spend) OVER (PARTITION BY customer_id ORDER BY month) AS prev FROM m)
        SELECT customer_id FROM l GROUP BY customer_id
        HAVING count(*) FILTER (WHERE spend < prev) >= 2'''
        wednesday = {r["customer_id"] for r in kit.sql(LAG_SQL)}
        kit.check("pandas flags exactly the customers Wednesday's LAG query flags",
                  set(table.loc[table["falling"], "customer_id"]) == wednesday)
        kit.check("the win-back list is 111 customers", int(table["lapsed"].sum()) == 111, int(table["lapsed"].sum()))
        kit.check("the flags are booleans", table["lapsed"].dtype == bool and table["falling"].dtype == bool)
        lap = table.groupby("segment")["lapsed"].sum().astype(int)
        kit.columns(lap.index.tolist(), [("lapsed, as of 28 September", lap.tolist())], width=640,
                    title="The win-back list per segment")
        """, 3),
        ("md", """
        ## Step 4. One reshaped view

        The slide the growth team asked for: spend by month and segment, months as rows so each
        segment reads as a line.
        """, 0),
        ("code", """
        seg_orders = orders.merge(customers, on="customer_id", validate="many_to_one").assign(
            month=orders["order_date"].dt.to_period("M").astype(str))
        # TODO 8. What goes in each cell of a spend view?
        #   a) aggfunc="mean"
        #   b) aggfunc="count"
        #   c) aggfunc="max"
        #   d) aggfunc="sum"
        # TODO 9. Months as rows means the index is:
        #   a) "customer_id"
        #   b) "month"
        #   c) "order_id"
        #   d) "segment"
        view = seg_orders.pivot_table(index=__TODO9__, columns="segment", values="amount", __TODO8__)
        print("view shape:", view.shape)
        """, 4),
        ("code", """
        kit.check("the view adds back to the book", view.values.sum() == orders["amount"].sum())
        kit.check("one row per month, April to September", list(view.index) == sorted(seg_orders["month"].unique()))
        kit.line(list(view.index), [(s, view[s].tolist(), "lit" if s == "Retail-Plus" else "")
                                    for s in ["Retail-Core", "Retail-Plus", "Student"]], fmt=kit.rupees,
                 title="The slide: consumer spend by month and segment")
        """, 4),
        ("md", """
        ## Step 5. One run, the same answer

        Refreshable in one run means a function: everything above in one call, with guards that
        stop a bad Monday before the table reaches Marketing.
        """, 0),
        ("code", """
        def build_customer_table(engine, feed_path):
            o = pd.read_sql("SELECT order_id, customer_id, order_date, amount FROM orders", engine,
                            parse_dates=["order_date"])
            c = pd.read_sql("SELECT customer_id, segment FROM customers", engine)
            e = pd.read_csv(feed_path, parse_dates=["exposed_date"])
            as_of = o["order_date"].max()
            agg = o.groupby("customer_id").agg(last_order=("order_date", "max"),
                                               frequency=("order_id", "count"), monetary=("amount", "sum"))
            t = c.merge(agg.reset_index(), on="customer_id", how="left", validate="one_to_one")
            first = e.sort_values("exposed_date").drop_duplicates("customer_id", keep="first")
            t = t.merge(first[["customer_id", "exposed_date"]], on="customer_id", how="left",
                        validate="one_to_one")
            t = t.assign(frequency=t["frequency"].fillna(0).astype("int64"), monetary=t["monetary"].fillna(0),
                         recency_days=(as_of - t["last_order"]).dt.days, exposed=t["exposed_date"].notna(),
                         as_of=as_of)
            # TODO 10. Which guard stops a table that has stopped being one row per customer?
            #   a) t["customer_id"].is_unique
            #   b) len(t) > 0
            #   c) t["monetary"].sum() > 0
            #   d) t.notna().all().all()
            assert __TODO10__, "the customer table is no longer one row per customer"
            assert t["monetary"].sum() == o["amount"].sum(), "spend no longer adds to the book"
            return t

        FEED_PATH = kit.data_dir() / "C2_W02_D04_exposure_STUDENT.csv"
        run_a = build_customer_table(ENG, FEED_PATH)
        run_b = build_customer_table(ENG, FEED_PATH)
        print(len(run_a), "rows in the first run and", len(run_b), "in the second")
        """, 5),
        ("code", """
        kit.check("two runs on the same data give the same table", run_a.equals(run_b))
        kit.check("the function's table matches the one built step by step",
                  run_a[["customer_id", "recency_days", "frequency", "monetary", "exposed"]].equals(
                      table[["customer_id", "recency_days", "frequency", "monetary", "exposed"]]))
        out = pathlib.Path("output"); out.mkdir(exist_ok=True)
        table.to_csv(out / "C2_W02_D04_customer_table_STUDENT.csv", index=False)
        kit.stats([(len(table), "customers", "one row each"), (kit.rupees(table["monetary"].sum()), "spend", "adds to the book"),
                   (int(table["exposed"].sum()), "reached by the sale", "first exposure per customer"),
                   (int(table["lapsed"].sum()), "on the win-back list", "as of 28 September")])
        kit.flow(["warehouse + feed", "build_customer_table()\\nguards inside", "output/ CSV\\nfor Friday"], lit=1,
                 title="The Monday refresh, one call")
        kit.check_summary()
        """, 5),
        ("md", """
        **Post:** your ten letters in order, and the four numbers above. The CSV in `output/` is
        what you bring to Friday's Excel day.
        """, 0),
    ]
    answers = {1: "customers", 2: 'orders["order_date"].max()', 3: 'keep="first"', 4: '"one_to_one"',
               5: 'table["recency_days"] > 60', 6: 'monthly.groupby("customer_id")["spend"].shift(1)',
               7: "falls[falls >= 2].index", 8: 'aggfunc="sum"', 9: '"month"', 10: 't["customer_id"].is_unique'}
    why = {
        1: "**Keys 1c, 2b.** 1a would give one row per order, and 1b and 1d hold only customers who "
           "ordered or who were reached. 2a and 2d move with the calendar, so two runs disagree and "
           "everyone looks 21 days staler on the first Monday; 2c measures from April.",
        2: "**Keys 3c, 4d.** 3a keeps the re-sent date, which is a later exposure; 3b drops every "
           "customer who was re-sent, so they read as unreached; 3d changes the index and removes "
           "nothing. 4d is the only promise that the table stays one row per customer: 4c checks "
           "nothing, 4a allows the fan-out and 4b allows anything.",
        3: "**Keys 5a, 6b, 7a.** 5b is a typo that flags almost everyone; 5c flags the customers who "
           "never ordered, and 5d flags the same customers. 6a and 6c read the previous row even when "
           "it belongs to another customer, the LAG-without-PARTITION trap from Wednesday; 6d compares "
           "different customers in the same month. 7b and 7d flag a single dip; 7c is impossible with "
           "three months, since at most two comparisons exist.",
        4: "**Keys 8d, 9b.** 8a is the default, which averages orders; 8b counts orders; 8c shows the "
           "biggest order. 9a and 9c give a row per customer or per order; 9d puts segments on the rows "
           "when the ask was months.",
        5: "**Key 10a.** 10b and 10c pass on a table that has doubled; 10d fails on every honest run, "
           "since customers who never ordered have no recency.",
    }
    return twin(cells, answers, why, solution)


def three_tools(solution):
    cells = [
        ("md", """
        # One question, three tools

        **Week 2, Thursday. The second case, in pairs, 45 minutes.** The brief is
        `exercises/guided/C2_W02_D04_three_tools_STUDENT.md`. Replace each `__TODOn__` with the
        option you choose; run as shipped, the notebook stops at `__TODO1__`.

        > **The client's ask.** Kavya Nair, senior analyst: "You did the tree in plain Python in Week
        > 1, in SQL on Monday. Do it a third way now, and tell me honestly which tool you would pick
        > for which job."

        The question all three tools answer is the tree node that moved in Week 1: **Retail-Plus
        orders per customer, Q1 against Q2.**
        """, 0),
        ("code", SETUP + """import pandas as pd
ENG = kit.engine()
print("connected to", kit.WAREHOUSE["dbname"])
""", 0),
        ("code", f"""
        kit.side_by_side(
            {ladder(4)},
            kit.flow(["plain Python\\nevery step visible", "SQL\\nwhere the data lives",
                      "pandas\\nthe analyst's bench"], title="Three tools, one number each", show=False),
        )
        """, 0),
        ("md", """
        ## Step 1. Plain Python: the accumulator, every step visible

        The rows arrive as a list of dictionaries, exactly the shape of Week 1's orders.
        """, 0),
        ("code", """
        rows = kit.sql('''SELECT o.order_id, o.customer_id, o.quarter FROM orders o
                          JOIN customers c ON c.customer_id = o.customer_id
                          WHERE c.segment = 'Retail-Plus' ''')
        orders_n = {"Q1": 0, "Q2": 0}
        # TODO 1. What holds each quarter's distinct customers?
        #   a) a list, appended once per row
        #   b) a count of rows, added once per row
        #   c) a set, added to once per row
        #   d) the length of rows
        # Fill with: [], 0, set() or len(rows)
        seen = {"Q1": __TODO1__, "Q2": __TODO1__}
        for r in rows:
            orders_n[r["quarter"]] += 1
            seen[r["quarter"]].add(r["customer_id"])
        py = {q: orders_n[q] / len(seen[q]) for q in ("Q1", "Q2")}
        print("plain Python:", {q: round(v, 3) for q, v in py.items()})
        """, 1),
        ("code", """
        kit.check("plain Python counts 355 Retail-Plus orders", sum(orders_n.values()) == 355)
        kit.check("Q1: 215 orders from 91 members", orders_n["Q1"] == 215 and len(seen["Q1"]) == 91)
        kit.table(["quarter", "orders", "members", "orders per member"],
                  [(q, orders_n[q], len(seen[q]), f"{py[q]:.3f}") for q in ("Q1", "Q2")], caption="Plain Python")
        """, 1),
        ("md", "## Step 2. SQL: the same number, where the data lives", 0),
        ("code", """
        # TODO 2. Which expression avoids Monday's integer-division trap?
        #   a) count(*) / count(DISTINCT o.customer_id)
        #   b) count(*)::numeric / count(DISTINCT o.customer_id)
        #   c) avg(count(*))
        #   d) count(DISTINCT o.order_id) / count(*)
        # TODO 3. Where does the Retail-Plus filter go?
        #   a) WHERE c.segment = 'Retail-Plus'
        #   b) HAVING c.segment = 'Retail-Plus'
        #   c) ORDER BY c.segment
        #   d) LIMIT 120
        SQL = '''SELECT o.quarter, count(*) AS orders, count(DISTINCT o.customer_id) AS members,
                        round(__TODO2__, 3) AS per_member
                 FROM orders o JOIN customers c ON c.customer_id = o.customer_id
                 __TODO3__
                 GROUP BY o.quarter ORDER BY o.quarter'''
        sql_rows = kit.sql(SQL)
        sq = {r["quarter"]: float(r["per_member"]) for r in sql_rows}
        print("SQL:", sq)
        """, 2),
        ("code", """
        kit.check("SQL returns one row per quarter", [r["quarter"] for r in sql_rows] == ["Q1", "Q2"])
        kit.check("SQL agrees with plain Python to three places", all(abs(sq[q] - py[q]) < 0.001 for q in sq), sq)
        """, 2),
        ("md", "## Step 3. pandas: the analyst's bench", 0),
        ("code", """
        df = pd.read_sql('''SELECT o.order_id, o.customer_id, o.quarter, c.segment FROM orders o
                            JOIN customers c ON c.customer_id = o.customer_id''', ENG)
        # TODO 4. Which named aggregation counts members, each once?
        #   a) members=("customer_id", "count")
        #   b) members=("order_id", "nunique")
        #   c) members=("customer_id", "size")
        #   d) members=("customer_id", "nunique")
        pd_view = (df[df["segment"] == "Retail-Plus"]
                   .groupby("quarter")
                   .agg(orders=("order_id", "count"), __TODO4__))
        pd_view = pd_view.assign(per_member=pd_view["orders"] / pd_view["members"])
        print(pd_view.round(3).to_string())
        """, 3),
        ("code", """
        pn = pd_view["per_member"].to_dict()
        kit.check("pandas agrees with plain Python", all(abs(pn[q] - py[q]) < 1e-9 for q in pn))
        kit.check("Retail-Plus orders per member fell from 2.363 to 1.842",
                  round(pn["Q1"], 3) == 2.363 and round(pn["Q2"], 3) == 1.842)
        kit.columns(["Q1", "Q2"], [("plain Python", [round(py[q], 3) for q in ("Q1", "Q2")]),
                                   ("SQL", [sq[q] for q in ("Q1", "Q2")]),
                                   ("pandas", [round(pn[q], 3) for q in ("Q1", "Q2")])],
                    fmt=lambda v: f"{v:.3f}", width=640,
                    title="Retail-Plus orders per member: three tools, one number")
        """, 3),
        ("md", """
        ## Step 4. The choice, with a reason per tool

        The three agree, so the choice between them is about who has to trust, rerun or audit the
        number. Finance's Monday revenue number is the one Kavya will ask you to defend.
        """, 0),
        ("code", """
        # TODO 5. Where should Finance's Monday revenue number be computed?
        #   a) a pandas notebook on an analyst's laptop
        #   b) a plain Python script with a loop
        #   c) a SQL view in the warehouse
        #   d) a spreadsheet exported every Monday
        finance_home = __TODO5__
        criteria = ["explain line by line", "audited where the data lives", "iterate fast on a question"]
        kit.matrix(["plain Python", "SQL", "pandas"], criteria,
                   [["best: every step visible", "no: runs off a copy", "slow to change"],
                    ["reads as a statement", "best: Finance can rerun it", "fine for fixed asks"],
                    ["reads as a chain", "no: runs off a copy", "best: the analyst's bench"]],
                   title="The tool-choice note, as a grid")
        """, 4),
        ("code", """
        kit.check("the choice was made", finance_home is not None)
        kit.check("the three tools agree on both quarters",
                  all(abs(py[q] - pn[q]) < 1e-9 and abs(py[q] - sq[q]) < 0.001 for q in ("Q1", "Q2")))
        fall = pn["Q2"] / pn["Q1"] - 1
        kit.bridge(("Q1, orders per member", round(pn["Q1"], 3)), [("the fall", round(pn["Q2"] - pn["Q1"], 3))],
                   end_label="Q2", fmt=lambda v: f"{v:.3f}", lit=(0,),
                   title=f"Retail-Plus orders per member fell {abs(fall):.0%}: the lever Week 1 found")
        kit.check_summary()
        """, 4),
        ("md", """
        **Post:** your five letters, and your tool-choice note in the brief's format: one sentence
        per tool, and the tool you would refuse for Finance's numbers, with the reason.
        """, 0),
    ]
    answers = {1: "set()", 2: "count(*)::numeric / count(DISTINCT o.customer_id)",
               3: "WHERE c.segment = 'Retail-Plus'", 4: 'members=("customer_id", "nunique")',
               5: '"a SQL view in the warehouse"'}
    why = {
        1: "**Key 1c.** A list (a) has no `.add` and would count a member once per order; a count (b) "
           "counts rows, which is orders again; `len(rows)` (d) is a number, not a container.",
        2: "**Keys 2b, 3a.** 2a is Monday's trap: Postgres divides two integers and returns 2 and 1. "
           "2c nests aggregates, which Postgres refuses; 2d inverts the rate. 3b fails because HAVING "
           "filters groups and segment is not one; 3c only sorts; 3d cuts rows at random.",
        3: "**Key 4d.** 4a and 4c count rows, which are orders, so the rate reads 1.000; 4b counts "
           "distinct orders.",
        4: "**Key 5c.** Finance's number lives where Finance can rerun and audit it: in the warehouse, "
           "as a view. A notebook (a) and a script (b) run off a copy on one laptop; a spreadsheet (d) "
           "is a copy that someone can edit by hand, which is Friday's lesson.",
    }
    return twin(cells, answers, why, solution)


def case1():
    build(NB / "C2_W02_D04_hands_on_STUDENT.ipynb", escalated(False), execute=False)
    build(SOL / "C2_W02_D04_hands_on_solution_STUDENT.ipynb", escalated(True))


def case2():
    build(NB / "C2_W02_D04_three_tools_STUDENT.ipynb", three_tools(False), execute=False)
    build(SOL / "C2_W02_D04_three_tools_solution_STUDENT.ipynb", three_tools(True))


if __name__ == "__main__":
    wanted = set(sys.argv[1:]) or {"1", "2", "3", "4", "5"}
    for key, fn in [("1", round1), ("2", round2), ("3", round3), ("4", case1), ("5", case2)]:
        if key in wanted:
            fn()
            print("built", fn.__name__)

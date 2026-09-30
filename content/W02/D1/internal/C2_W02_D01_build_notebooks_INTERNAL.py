"""Build Week 2 Monday's notebooks: six chapters, the escalated case and the second case.

Run from the repository root, with the warehouse loaded (bash .devcontainer/load_warehouse.sh):
    python3 content/W02/D1/internal/C2_W02_D01_build_notebooks_INTERNAL.py            every notebook
    python3 content/W02/D1/internal/C2_W02_D01_build_notebooks_INTERNAL.py ch3 case   named ones only

Names: ch1 to ch6, case (the escalated case twin and its solution), second (the second case twin
and its solution). Each chapter notebook is executed cold in its own folder by scripts/nb_make.py,
so the saved outputs are the ones a learner sees on GitHub. Every query a notebook runs is a named
block of a .sql file in ../sql/, read at run time, so the notebook and VS Code run the same text.
The TODO twins are written unexecuted and their solution twins executed. No cell prints a planted
record, and the one mechanism that needs a missing value runs on three invented values labelled
invented.
"""
import pathlib
import re
import sys

sys.path.insert(0, "scripts")
from nb_make import SETUP, build, code, empty, md  # noqa: E402,F401

DAY = pathlib.Path("content/W02/D1")
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"

CHAPTERS = ["What does the book say?", "Same story as Week 1?", "Which segment moved?",
            "Which branch moved?", "Does the suite add up?", "Same answer next week?"]

# The setup every notebook runs: the helper, the warehouse, and the named blocks of one .sql file.
WAREHOUSE = SETUP + r'''
import re
from decimal import Decimal
SQL_DIR = kit.data_dir().parent / "sql"

def blocks(stem):
    """Every named block of a .sql file in ../sql/, keyed by the name on its '-- name:' line."""
    text = (SQL_DIR / f"C2_W02_D01_{stem}_STUDENT.sql").read_text(encoding="utf-8")
    parts = re.split(r"^-- name: (\w+)\s*$", text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}

def statements(block):
    """A block's statements with its comment lines removed, for a block that runs several."""
    bare = "\n".join(l for l in block.splitlines() if not l.strip().startswith("--"))
    return [s.strip() for s in bare.split(";") if s.strip()]

def num(v):
    """A database number as a Python int or float."""
    if isinstance(v, Decimal):
        return int(v) if v == v.to_integral_value() else float(v)
    return v

def show(rows, caption="", money=(), limit=12):
    """Rows from kit.sql as the kit's table, with the columns named in money set in rupees."""
    if not rows:
        kit.table(["result"], [["no rows"]], caption)
        return
    heads = list(rows[0])
    def cell(h, v):
        v = num(v)
        if v is None:
            return "NULL"
        if h in money:
            return kit.rupees(v)
        return f"{v:,}" if isinstance(v, int) and abs(v) >= 10000 else str(v)
    body = [[cell(h, r[h]) for h in heads] for r in rows[:limit]]
    if len(rows) > limit:
        body.append(["..." for _ in heads])
    kit.table(heads, body, caption)

def run(name, caption="", money=(), limit=12):
    """Print a named block, run it, show its rows and hand them back."""
    print(Q[name])
    rows = kit.sql(Q[name])
    show(rows, caption, money, limit)
    return rows

def pct(before, after):
    """The change from before to after, in percent."""
    return 100 * (float(after) - float(before)) / float(before)
'''


def setup(stem, extra=""):
    """The setup cell: the helper, the warehouse, and this chapter's named blocks."""
    return code(WAREHOUSE + f'''
Q = blocks("{stem}")
print(len(Q), "named queries read from", "C2_W02_D01_{stem}_STUDENT.sql;",
      kit.sql("select version()")[0]["version"].split(",")[0])
''' + extra)


def where(n, levels):
    """The day's chapter ladder beside this chapter's steps, the map every notebook opens on."""
    steps = ", ".join(repr(s) for s in levels)
    return code(f'''
        kit.side_by_side(
            kit.ladder({CHAPTERS!r}, lit={n - 1}, show=False),
            kit.vflow([{steps}], lit=0, show=False),
        )''')


def setup_note(stem):
    return md(f"""
        **Setup.** The next cell finds the shared helper, `c2kit`, by walking up from this folder
        until it reaches `scripts/`, connects to the Kalpa warehouse and reads the named queries in
        `../sql/C2_W02_D01_{stem}_STUDENT.sql`. Every query below is a block of that file, so what
        runs here is exactly what runs from VS Code. If no database answers, the error names the
        command that loads the warehouse: `bash .devcontainer/load_warehouse.sh`.
        """)


def twin(path_todo, path_sol, cells, answers):
    """Write the TODO twin unexecuted and the solution executed, from one list of cells.

    A cell's source may hold __TODOn__ placeholders; the solution replaces each with answers[n].
    A cell whose source starts with SOLUTION ONLY is kept in the solution alone, and one starting
    TODO ONLY in the twin alone, with the marker line removed.
    """
    todo, sol = [], []
    for cell in cells:
        src = cell.source
        if src.startswith("SOLUTION ONLY"):
            cell.source = src.split("\n", 1)[1]
            sol.append(cell)
            continue
        if src.startswith("TODO ONLY"):
            cell.source = src.split("\n", 1)[1]
            todo.append(cell)
            continue
        todo.append(cell)
        if "__TODO" in src:
            filled = re.sub(r"__TODO(\d+)__", lambda m: answers[int(m.group(1))], src)
            sol.append(code(filled) if cell.cell_type == "code" else md(filled))
        else:
            sol.append(cell)
    build(path_todo, [c.copy() for c in todo], execute=False)
    build(path_sol, sol)


# ----------------------------------------------------------------------------------- chapter 1
def ch1():
    return [
        md("""
        # How many orders, rupees and customers did each quarter book, counted where the book lives?

        **Week 2, Monday. Chapter 1 of 6.** The day climbs one case, Anand's Monday numbers straight
        from the warehouse, and this is its first chapter.

        > "I want these numbers every Monday, for every segment and channel, computed from the
        > warehouse itself. No notebooks, no exports, nothing a person can mistype. Our data team will
        > give you read access to Postgres."
        > Anand Iyer, finance controller, Kalpa Retail

        **Who needs the answer.** Anand Iyer, Kalpa Retail's finance controller, puts these numbers on
        the Monday sheet, and Anand's analyst audits every line of the query that made them. A figure
        restated in front of the board costs the finance controller's word with it. A customer count
        that is really a count of orders says that nobody ever buys twice, which would reopen the
        Rs 12 crore acquisition budget that Meera Raghavan, Kalpa Retail's CEO, parked last week.

        **The questions on the way.**
        1. Where could the Monday numbers be computed: an export, a query or a view?
        2. What does the warehouse hold, and where does each leaf of the tree live?
        3. How many orders and rupees did each quarter book?
        4. How many customers bought in each quarter?
        5. Do the raw rows, counted in Python, give the same leaves?

        **The metric at stake.** The revenue tree from Week 1: revenue is customers, times orders per
        customer, times revenue per order. Customers means the customers who bought in the quarter,
        each counted once, as the retail dossier defines it
        (`content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`, section 5, has the long
        version). Revenue here is booked revenue: every order at its amount, whatever its status.
        Q1 is April to June 2026 and Q2 is July to September 2026.

        **Where last week left off.** Week 1 answered Meera from an extract: 186 cleaned orders,
        Rs 1,90,00,000 booked in Q1 and Rs 1,87,00,000 in Q2, with frequency as the branch that fell.
        She accepted "real, modest, fix frequency". The warehouse is Kalpa's Postgres database, and
        the data platform lead's note says it holds the same two quarters, about one thousand orders,
        already de-duplicated. This notebook asks the warehouse the first questions of the tree.

        **A real company with the same question.** JPMorgan Chase's task force on its 2012 trading
        losses found that a risk model "operated through a series of Excel spreadsheets, which had to
        be completed manually, by a process of copying and pasting data from one spreadsheet to
        another" (the task force's report of 16 January 2013, page 124). By 30 June 2012 those losses
        had grown to about $5.8 billion (page 7). A number that a person moves by hand can be moved
        wrongly, and Anand's rule keeps Kalpa's book away from that.
        """),
        setup_note("01_book"),
        setup("01_book"),
        where(1, ["where to compute\nan export, a query or a view",
                  "the schema\nwhat each table holds",
                  "the book\norders and rupees per quarter",
                  "the customers\nwhich count is a customer",
                  "a second route\nthe raw rows in Python"]),
        md("""
        ## The options: where could the Monday numbers be computed, and what does each way cost?

        Three ways a team could put Anand's numbers on the Monday sheet. They differ in what moves each
        Monday, in whether Anand's analyst can rerun exactly what the team ran, and in what
        happens when the platform team renames a column in the warehouse.

        | Option | What runs each Monday | Can the analyst rerun it? | When a column is renamed |
        |---|---|---|---|
        | A. Export the tables and compute in pandas, as Week 1 did | A copy of the tables leaves the warehouse, then Python runs on the copy | Only on the copy, which may no longer match the book | An old export keeps answering from old data; a fresh one breaks the pandas code |
        | B. Query the warehouse from a `.sql` file | The file runs on the book and returns a few rows | Yes: the same file on the same book | The query stops with an error that names the missing column |
        | C. Save the query as a view in the warehouse | The saved query runs on the book whenever the view is read | Yes: one line reads the view | The view follows a rename, and Postgres refuses to drop a column the view reads |

        **Predict before you run.** For the quarter totals alone, how many rows does option A copy out
        of the warehouse each Monday, against option B?

        - a) The same number, since both answer the same question.
        - b) A few more for A, since pandas needs a header row.
        - c) Every row of the two tables the tree needs for A, and one row per quarter for B.
        - d) Fewer for A, since an export is compressed.
        """),
        code(r'''
            orders_rows =kit.sql("SELECT count(*) AS n FROM orders")[0]["n"]
            customers_rows = kit.sql("SELECT count(*) AS n FROM customers")[0]["n"]
            query_rows = len(kit.sql(Q["c1_book"]))
            sizing = [("A. export and pandas", orders_rows + customers_rows),
                      ("B. a .sql file", query_rows),
                      ("C. a saved view", query_rows)]
            kit.table(["option", "rows that leave the warehouse each Monday"],
                      [(o, f"{n:,}") for o, n in sizing],
                      caption="Sized on this warehouse: the rows each option moves for the quarter totals")
            kit.bars(sizing, title="Rows moved each Monday: the export copies both tables the tree needs",
                     lit=(1,))
            '''),
        md("""
        **What happened.** The answer is c. An export copies all 1,000 order rows and all 340 customer
        rows, 1,340 in all, before Python adds anything up; the query and the view send back two rows,
        one per quarter. The copy is also a second version of the book, and the analyst cannot tell
        whether it still matches the first.

        **The best-fit call.** Option B, a `.sql` file queried every Monday. The platform lead granted
        read access, and saving a view needs the right to create objects in the warehouse. The file
        moves two rows where an export moves 1,340, the analyst reruns the same file on the same book,
        and a renamed column stops it with an error instead of a quiet wrong number. The notebook you
        are reading runs the same file, so it is where the team thinks, and the number on Anand's sheet
        still comes from the query. **What would change the call:** once the suite stops changing and
        the platform lead grants a schema to save it in, option C is better, because Postgres then
        records which columns the Monday numbers depend on and refuses a change that would break them.
        """),
        code(r'''
            kit.check("an export moves every row of both tables", sizing[0][1] == 1340, f"{sizing[0][1]:,} rows")
            kit.check("the query moves one row per quarter", query_rows == 2, f"{query_rows} rows")
            '''),
        md("""
        ## 1. What does the warehouse hold, and where does each leaf of the tree live?

        A new source is read before it is used. Last week's file was one table of orders. The
        warehouse keeps each kind of record in its own table, and a number you cannot trace to a table
        and a column is a number the analyst cannot audit.

        **Predict before you run.** How many tables does the warehouse hold?

        - a) One, the orders.
        - b) Two, the orders and the customers.
        - c) Seven.
        - d) It cannot be known without asking the data team.
        """),
        code(r'''
            tables = run("c1_tables", "The warehouse's tables and how many columns each carries")
            kit.bars([(t["table_name"], int(t["columns"])) for t in tables],
                     title="Columns per table: orders and customers carry today's tree",
                     lit=tuple(i for i, t in enumerate(tables) if t["table_name"] in ("orders", "customers")))
            '''),
        md("""
        **What happened.** The answer is c: seven tables. Today's tree needs two of them, `orders` and
        `customers`; the others arrive later in the week, each with its own question. The query that
        listed them reads `information_schema`, the catalogue every Postgres database keeps about
        itself, so nobody had to be asked.
        """),
        code(r'''
            cols = {r["column_name"]: r["data_type"] for r in run("c1_order_columns", "One order: its columns and their types")}
            run("c1_peek", "The first five orders, by order id", money=("amount",))
            kit.check("orders carries seven columns", len(cols) == 7, ", ".join(cols))
            kit.check("amount is stored as a number, so SUM can add it", cols["amount"] == "numeric", cols["amount"])
            kit.check("the segment is not on the order", "segment" not in cols, "it lives on the customer")
            '''),
        md("""
        The segment lives on the customer, which chapter 3 needs: to report Retail-Plus, each order
        looks up its customer's segment. Every leaf of today's tree comes from `orders`, and the count
        of customers Kalpa holds comes from `customers`.

        ## 2. How many orders and rupees did each quarter book?

        Week 1's extract said Rs 1,90,00,000 for Q1 and Rs 1,87,00,000 for Q2. The warehouse is the
        whole book of the two quarters, so its totals are the ones Anand's sheet will carry.

        **Predict before you run.** What will the warehouse say?

        - a) Exactly the extract's two totals.
        - b) Larger totals, falling the same 1.6 percent.
        - c) Larger totals, falling by a different amount.
        - d) Smaller totals, because the warehouse is de-duplicated.
        """),
        code(r'''
            book = {r["quarter"]: {k: num(v) for k, v in r.items()}
                    for r in run("c1_book", "The book, one row per quarter", money=("revenue", "revenue_per_order"))}
            q1, q2 = book["Q1"], book["Q2"]
            kit.columns(["orders", "revenue per order, Rs thousand"],
                        [("Q1", [q1["orders"], q1["revenue_per_order"] / 1000]),
                         ("Q2", [q2["orders"], q2["revenue_per_order"] / 1000])],
                        title="Fewer orders in Q2, each worth more", fmt=lambda v: f"{v:,.0f}")
            print(f"Revenue {kit.rupees(q1['revenue'])} to {kit.rupees(q2['revenue'])}, "
                  f"{pct(q1['revenue'], q2['revenue']):.1f} percent")
            '''),
        md("""
        **What happened.** The answer is b. Q1 booked Rs 10,00,00,000 on 538 orders and Q2 booked
        Rs 9,84,00,000 on 462: about five times the extract's totals, falling the same 1.6 percent.
        Revenue per order rose from Rs 1,85,874 to Rs 2,12,987. One leaf agrees with Week 1, and
        chapter 2 sets every other leaf beside last week's.
        """),
        code(r'''
            kit.check("the book holds 1,000 orders", q1["orders"] + q2["orders"] == 1000,
                      f"{q1['orders']} and {q2['orders']}")
            kit.check("Q1 booked Rs 10 crore", q1["revenue"] == 100000000, kit.rupees(q1["revenue"]))
            kit.check("the fall is 1.6 percent", round(pct(q1["revenue"], q2["revenue"]), 1) == -1.6)
            kit.check("revenue per order times orders gives the revenue back, to the rupee rounding",
                      abs(q2["revenue_per_order"] * q2["orders"] - q2["revenue"]) <= q2["orders"],
                      f"{q2['revenue_per_order']} x {q2['orders']}")
            '''),
        md("""
        ## 3. How many customers bought in each quarter?

        The next leaf is customers, then orders per customer. A hurried analyst asks the table for its
        customers the quickest way:

        ```sql
        SELECT quarter, count(*) AS customers FROM orders GROUP BY quarter;
        ```

        **Predict before you run.** What does that query count?

        - a) The customers who bought in each quarter.
        - b) The customers on Kalpa's customer table.
        - c) The order rows in each quarter.
        - d) The customers who bought more than once.
        """),
        code(r'''
            hurried = {r["quarter"]: int(r["customers"]) for r in run("c1_customers_hurried",
                        "The hurried query, exactly as it would reach Anand's sheet")}
            kit.stats([(f"{hurried['Q1']:,}", "Q1 customers", "the column's own label"),
                       (f"{hurried['Q2']:,}", "Q2 customers", "the column's own label"),
                       (f"{q1['orders'] / hurried['Q1']:.2f}", "orders per customer", "Q1 orders over that count"),
                       (f"{q2['orders'] / hurried['Q2']:.2f}", "orders per customer", "Q2 orders over that count")],
                      caption="The hurried reading of the customer leaf")
            '''),
        md("""
        **The plausible wrong answer.** 538 customers in Q1 and 462 in Q2, each placing 1.00 order:
        every customer bought once and never came back. On Anand's sheet the frequency branch, the one
        Meera was told to fix, reads as if there were nothing to fix, and the case for spending the
        Rs 12 crore on new customers comes back.

        **Why it is wrong.** `count(*)` counts rows, and a row of `orders` is an order. The label
        `AS customers` is a promise the query does not keep, because the database prints whatever name
        it is given. The answer is c.

        **The check that exposes it.** Count the same table three ways, each count named for what it
        counts, and set the customer table's own count beside them.
        """),
        code(r'''
            three = {k: int(v) for k, v in run("c1_three_counts", "One table, counted two ways")[0].items()}
            members =int(run("c1_members", "The customer table's own count")[0]["members_on_the_book"])
            kit.bars([("order rows, count(*)", three["order_rows"]),
                      ("members on the book", members),
                      ("customers who bought", three["customers_who_bought"])],
                     title="Three counts, three questions: only one is the tree's customers", lit=(2,))
            '''),
        code(r'''
            kit.check("order rows and customers are different counts",
                      three["order_rows"] != three["customers_who_bought"],
                      f"{three['order_rows']:,} rows, {three['customers_who_bought']} customers")
            kit.check("301 customers bought across the two quarters", three["customers_who_bought"] == 301)
            kit.check("39 members on the book bought nothing in either quarter",
                      members - three["customers_who_bought"] == 39, f"{members} less {three['customers_who_bought']}")
            '''),
        md("""
        **The fix, and what it changed.** `count(DISTINCT customer_id)` counts each customer once. Run
        per quarter, it gives the leaf the tree needs.
        """),
        code(r'''
            fixed = {r["quarter"]: {k: num(v) for k, v in r.items()}
                     for r in run("c1_customers", "The customer leaf, beside the order rows it was confused with")}
            kit.columns(["Q1", "Q2"],
                        [("order rows", [fixed["Q1"]["order_rows"], fixed["Q2"]["order_rows"]]),
                         ("customers", [fixed["Q1"]["customers"], fixed["Q2"]["customers"]])],
                        title="Order rows against customers: the gap is the repeat buying Meera cares about")
            for q in ("Q1", "Q2"):
                print(f"{q}: {fixed[q]['customers']} customers, "
                      f"{fixed[q]['order_rows'] / fixed[q]['customers']:.2f} orders each")
            '''),
        md("""
        **What happened.** 244 customers bought in Q1 and 227 in Q2, where the hurried query said 538
        and 462. The fix takes 294 customers who do not exist out of Q1 and 235 out of Q2, and orders
        per customer moves from 1.00 to 2.20 in Q1 and 2.04 in Q2: customers do come back, and the
        frequency branch is on the sheet again. The customer table's 340 answers a different question,
        how many members Kalpa holds, and 39 of them bought nothing in either quarter.
        """),
        code(r'''
            kit.check("244 customers bought in Q1 and 227 in Q2",
                      (fixed["Q1"]["customers"], fixed["Q2"]["customers"]) == (244, 227))
            kit.check("orders per customer is above 1 in both quarters",
                      all(fixed[q]["order_rows"] / fixed[q]["customers"] > 1 for q in ("Q1", "Q2")))
            kit.check("the fix removes 294 and 235 customers who do not exist",
                      (hurried["Q1"] - fixed["Q1"]["customers"], hurried["Q2"] - fixed["Q2"]["customers"]) == (294, 235))
            '''),
        md("""
        ## A second route: do the raw rows, counted in Python, give the same leaves?

        The second route answers the same three leaves without SQL's `count` and `sum`: it pulls every
        order row into Python and counts with a set of customer ids and a running sum. It is option A
        from the sizing, done once, so it also shows what an export costs.

        **Predict before you run.** Will Python's set of ids per quarter give 244 and 227?

        - a) Yes, since a set keeps each id once, as `count(DISTINCT ...)` does.
        - b) No, since Python counts the rows.
        - c) No, since Python rounds the amounts.
        - d) Only if the rows arrive sorted.
        """),
        code(r'''
            rows = kit.sql(Q["c1_rows_for_python"])
            py = {}
            for r in rows:
                q = py.setdefault(r["quarter"], {"orders": 0, "ids": set(), "revenue": 0})
                q["orders"] += 1
                q["ids"].add(r["customer_id"])
                q["revenue"] += r["amount"]
            kit.table(["leaf", "Q1, SQL", "Q1, Python", "Q2, SQL", "Q2, Python"],
                      [("orders", q1["orders"], py["Q1"]["orders"], q2["orders"], py["Q2"]["orders"]),
                       ("customers", fixed["Q1"]["customers"], len(py["Q1"]["ids"]),
                        fixed["Q2"]["customers"], len(py["Q2"]["ids"])),
                       ("revenue", kit.rupees(q1["revenue"]), kit.rupees(py["Q1"]["revenue"]),
                        kit.rupees(q2["revenue"]), kit.rupees(py["Q2"]["revenue"]))],
                      caption=f"Two routes, one book: Python moved {len(rows):,} rows to agree with two")
            '''),
        code(r'''
            kit.check("Python's order counts agree with SQL's", (py["Q1"]["orders"], py["Q2"]["orders"]) == (538, 462))
            kit.check("Python's sets of ids agree with count(DISTINCT)",
                      (len(py["Q1"]["ids"]), len(py["Q2"]["ids"])) == (fixed["Q1"]["customers"], fixed["Q2"]["customers"]))
            kit.check("Python's sums agree with SUM to the rupee",
                      (py["Q1"]["revenue"], py["Q2"]["revenue"]) == (q1["revenue"], q2["revenue"]))
            kit.check("the second route moved every order row", len(rows) == 1000, f"{len(rows):,} rows")
            '''),
        md("""
        **What happened.** The answer is a. Both routes agree on 538 and 462 orders, 244 and 227
        customers, and Rs 10,00,00,000 and Rs 9,84,00,000. The Python route moved 1,000 rows out of the
        warehouse to reach what the query reached with two, which is why it is the check and the query
        is the Monday way.

        > **Kavya's review.** Every count says what it counts, in its name and in the comment above
        > it. On Anand's sheet, customers means customers who bought in the quarter, each counted
        > once, and the query's first line says so. A count named `customers` that counts rows is the
        > one number an auditor finds first.

        ### In the interview: why compute a number in the warehouse, and how do you count customers there?

        **[F] Why would you compute a KPI in the warehouse rather than in a notebook?** Because the
        warehouse holds the one copy everybody reads. A query runs on that copy every time, so
        Monday's number and the auditor's rerun come from the same book, and a renamed column stops
        the query with an error. An export is a second copy that starts ageing the moment it lands,
        and every number computed from it has to be traced back to it. On this warehouse the export
        moves 1,340 rows to answer what the query answers with two. Exploration and charts stay in a
        notebook that reads the warehouse; the reported number comes from the saved query.

        **[F] What is the difference between `count(*)`, `count(customer_id)` and
        `count(DISTINCT customer_id)`?** `count(*)` counts rows. `count(customer_id)` counts the rows
        where `customer_id` is not missing. `count(DISTINCT customer_id)` counts the different ids
        that are present. On Kalpa's orders the first two both give 1,000, since no order lacks a
        customer, and the third gives 301 across the two quarters.

        ### Depth: what happens to a query and a view when the platform team renames a column?

        The sizing table claimed that a query stops with an error and a view follows a rename. Your
        Codespace's copy of the warehouse lets you watch both inside a transaction that is rolled
        back, so the warehouse is left exactly as it was. The real warehouse would refuse these
        statements to a read-only user; here they show the behaviour the table priced.
        """),
        code(r'''
            conn = kit.connect()
            try:
                kit.sql("CREATE VIEW monday_book AS SELECT quarter, sum(amount) AS revenue FROM orders GROUP BY quarter", conn=conn)
                kit.sql("ALTER TABLE orders RENAME COLUMN amount TO amount_rs", conn=conn)
                view_after = kit.sql("SELECT pg_get_viewdef('monday_book') AS definition", conn=conn)[0]["definition"]
                with kit.expect_error() as renamed:
                    kit.sql("SELECT sum(amount) FROM orders", conn=conn)
                conn.rollback()
                kit.sql("CREATE VIEW monday_book AS SELECT quarter, sum(amount) AS revenue FROM orders GROUP BY quarter", conn=conn)
                with kit.expect_error() as dropped:
                    kit.sql("ALTER TABLE orders DROP COLUMN amount", conn=conn)
            finally:
                conn.rollback()
                conn.close()
            print("The view's definition after the rename:\n" + view_after)
            kit.check("a query naming the old column stops with an error", renamed.name is not None, renamed.name)
            kit.check("the view follows the rename", "amount_rs" in view_after)
            kit.check("Postgres refuses to drop a column a view reads", dropped.name is not None, dropped.name)
            kit.check("the warehouse is left as it was",
                      "amount" in {r["column_name"] for r in kit.sql(Q["c1_order_columns"])})
            '''),
        md("""
        The query naming `amount` stopped with an error the moment the column was renamed, the view
        followed the rename, and Postgres refused to drop a column the view reads. That refusal is the
        view's value and its cost: it protects Anand's number, and it makes the platform team ask
        before changing anything the Monday numbers depend on.

        ## What did this chapter answer?

        1. **Where should the Monday numbers be computed?** In a `.sql` file queried every Monday: two
           rows reach the screen where an export copies 1,340, the analyst reruns the same file on the
           same book, and a view takes over once the suite settles and a schema is granted.
        2. **What does the warehouse hold?** Seven tables; today's tree needs `orders` and `customers`,
           and the segment lives on the customer.
        3. **How many orders and rupees did each quarter book?** 538 orders and Rs 10,00,00,000 in Q1,
           462 orders and Rs 9,84,00,000 in Q2: down 1.6 percent, as Week 1 found.
        4. **How many customers bought in each quarter?** 244 in Q1 and 227 in Q2, each counted once;
           `count(*)` said 538 and 462 because it counts orders.
        5. **Do the raw rows in Python agree?** Yes, on every leaf, after moving 1,000 rows to do it.

        Chapter 2 sets each of these leaves beside the ones Week 1's note to Meera rested on.
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 2
def ch2():
    return [
        md("""
        # Does the warehouse tell the same story as the file Meera's decision rested on?

        **Week 2, Monday. Chapter 2 of 6.** Chapter 1 counted the book's first leaves; this chapter
        sets every leaf beside the ones last week's note was built on.

        > "Before your numbers go in my book, show me they match the ones you gave Meera."
        > Anand Iyer, finance controller, Kalpa Retail

        **Who needs the answer.** Anand wants to know which numbers the sheet is signing for, and Meera Raghavan,
        Kalpa Retail's CEO, parked a Rs 12 crore acquisition budget last week on the team's finding
        that customers held steady while each ordered less often. If the book tells a different story
        and nobody says so, a Rs 12 crore decision stays parked on a number the warehouse does not
        support, and the team's next number is doubted before anyone reads it.

        **The questions on the way.**
        1. How can two sources of different sizes be compared fairly?
        2. Does last week's file still give last week's numbers?
        3. Which leaves agree once each is read as a change from Q1 to Q2?
        4. Did the customer leaf agree?
        5. Where did the book's 17 fewer Q2 customers come from?
        6. What goes on Anand's sheet about last week's note?

        **The metric at stake.** Every leaf of the tree and its change from Q1 (April to June 2026) to
        Q2 (July to September 2026): revenue, orders, customers who bought, orders per customer and
        revenue per order. Revenue is booked revenue, every status included.

        **What chapter 1 found.** The warehouse books 538 orders and Rs 10,00,00,000 in Q1 and 462
        orders and Rs 9,84,00,000 in Q2, with 244 and 227 customers who bought, each counted once.
        Last week's extract held 186 cleaned orders: 100 and 86 orders, Rs 1,90,00,000 and
        Rs 1,87,00,000, and 69 customers in each quarter. Meera accepted "real, modest, fix frequency"
        from it.

        **A real company with the same question.** Airbnb's data team wrote in April 2021 that, years
        earlier, when the chief executive asked which city had the most bookings in the previous week,
        "Data Science and Finance would sometimes provide diverging answers using slightly different
        tables, metric definitions, and business logic" (The Airbnb Tech Blog, "How Airbnb achieved
        metric consistency at scale", 30 April 2021). Two sources that answer one question differently
        are settled leaf by leaf before either reaches a decision maker.
        """),
        setup_note("02_same_story"),
        setup("02_same_story", r'''
import csv
W1_FILE = kit.data_dir() / "C2_W02_D01_week1_orders_STUDENT.csv"
w1_rows = list(csv.DictReader(W1_FILE.open(encoding="utf-8")))
print(len(w1_rows), "rows read from last week's extract,", W1_FILE.name)
'''),
        where(2, ["the options\nfour ways to compare", "last week's leaves\nrecomputed from its file",
                  "every leaf\nas a change", "the customer leaf\nthe one that moved",
                  "a second route\nthe customer bridge", "Anand's sheet\nthe line for Meera"]),
        md("""
        ## The options: how can two sources of different sizes be compared fairly?

        The extract held 186 orders and the warehouse holds 1,000, so their totals were never going to
        match. Four ways a team could compare them:

        | Option | What it compares | What it can catch | What it assumes |
        |---|---|---|---|
        | A. The two totals | Q1 and Q2 revenue in each source | A different fall | That matching totals mean matching leaves |
        | B. Every leaf, as a change from Q1 to Q2 | Five leaves in each quarter in each source | Any branch that moved differently | That both sources use the same definitions |
        | C. Order by order, on the order id | Each of the extract's orders looked up in the warehouse | A missing or altered order | That the two sources share order ids |
        | D. Last week's notebook rerun on an export | Everything Week 1 computed | Anything Week 1's code checks | An export, which the platform lead ruled out |

        **Predict before you run.** Option C is the strictest. How many of the extract's 186 order ids
        will it find in the warehouse?

        - a) All 186, since the warehouse holds the same two quarters.
        - b) About 150, since the extract was cleaned.
        - c) None at all.
        - d) It cannot be known without the ERP.
        """),
        code(r'''
            wh_orders = {r["order_id"] for r in kit.sql(Q["c2_order_ids"])}
            wh_customers = {r["customer_id"] for r in kit.sql(Q["c2_customer_ids"])}
            shared_orders = len({r["order_id"] for r in w1_rows} & wh_orders)
            shared_customers = len({r["customer_id"] for r in w1_rows} & wh_customers)
            sizing = [("A. the two totals", "4 numbers", "a different fall only"),
                      ("B. every leaf, as a change", "20 numbers", "any branch that moved"),
                      ("C. order by order", f"{len(w1_rows)} lookups, {shared_orders} found", "nothing: no shared ids"),
                      ("D. rerun on an export", "1,340 rows exported", "ruled out by the platform lead")]
            kit.table(["option", "what it touches here", "what it can catch here"], sizing,
                      caption="The four ways sized on these two sources")
            kit.stats([(str(shared_orders), "order ids shared", f"the extract's {len(w1_rows)} against the book's {len(wh_orders):,}"),
                       (str(shared_customers), "customer ids shared", f"the extract's 69 against the book's {len(wh_customers)}")],
                      caption="The two sources hold different records of the same two quarters")
            '''),
        md("""
        **What happened.** The answer is c: none. The extract and the warehouse share no order id and
        no customer id, so option C finds nothing and option D would need an export. Option A compares
        four numbers and can only catch a different fall.

        **The best-fit call.** Option B, every leaf read as a change from Q1 to Q2. A change survives a
        difference in size, and five leaves in each source are twenty numbers to set side by side.
        **What would change the call:** if the two sources shared order ids, option C would prove or
        disprove every order, and it would win.
        """),
        code(r'''
            kit.check("the sources share no order id", shared_orders == 0)
            kit.check("the sources share no customer id", shared_customers == 0)
            '''),
        md("""
        ## 1. Does last week's file still give last week's numbers?

        Before last week's leaves are compared with anything, they are recomputed from last week's own
        file, so both columns of the comparison come from a computation rather than from memory.

        **Predict before you run.** How many of the extract's 69 customers bought in both quarters?

        - a) All 69.
        - b) About half, 35.
        - c) None, since each quarter held different customers.
        - d) It cannot be counted from one file.
        """),
        code(r'''
            def leaves(rows):
                """Customers, orders and revenue per quarter, plus the customers who bought in both."""
                out = {}
                for q in ("Q1", "Q2"):
                    r = [x for x in rows if x["quarter"] == q]
                    out[q] = {"customers": len({x["customer_id"] for x in r}), "orders": len(r),
                              "revenue": sum(float(x["amount"]) for x in r)}
                ids = [{x["customer_id"] for x in rows if x["quarter"] == q} for q in ("Q1", "Q2")]
                out["both"] = len(ids[0] & ids[1])
                out["anyone"] = len(ids[0] | ids[1])
                return out

            w1 = leaves(w1_rows)
            kit.table(["quarter", "orders", "customers", "revenue"],
                      [(q, w1[q]["orders"], w1[q]["customers"], kit.rupees(w1[q]["revenue"])) for q in ("Q1", "Q2")],
                      caption="Last week's extract, recomputed from its own file")
            print(f"Customers who bought in both quarters: {w1['both']} of {w1['anyone']}")
            '''),
        code(r'''
            kit.check("the file holds last week's 186 orders", len(w1_rows) == 186)
            kit.check("it reproduces Rs 1,90,00,000 and Rs 1,87,00,000",
                      (w1["Q1"]["revenue"], w1["Q2"]["revenue"]) == (19000000, 18700000))
            kit.check("it reproduces 69 customers in each quarter", (w1["Q1"]["customers"], w1["Q2"]["customers"]) == (69, 69))
            '''),
        md("""
        **What happened.** The answer is a: all 69 of the extract's customers bought in both quarters.
        The file reproduces last week's numbers, so the comparison below starts from what Meera was
        told, recomputed.

        ## 2. Which leaves agree once each is read as a change from Q1 to Q2?

        The book's own leaves come from one query, and each leaf is read as Q2 over Q1 in both sources.

        **Predict before you run.** Revenue fell 1.6 percent in both. How many of the other four leaves
        will agree to within a point?

        - a) All four.
        - b) Two: orders and revenue per order.
        - c) One.
        - d) None, since the sources share no record.
        """),
        code(r'''
            book = {r["quarter"]: {k: num(v) for k, v in r.items()}
                    for r in run("c2_leaves", "The book's leaves, one row per quarter", money=("revenue",))}

            def branch(d, name):
                q1, q2 = d["Q1"], d["Q2"]
                if name == "orders per customer":
                    return q1["orders"] / q1["customers"], q2["orders"] / q2["customers"]
                if name == "revenue per order":
                    return q1["revenue"] / q1["orders"], q2["revenue"] / q2["orders"]
                return q1[name], q2[name]

            LEAVES = ["revenue", "orders", "customers", "orders per customer", "revenue per order"]
            compare = []
            for name in LEAVES:
                a, b = branch(w1, name), branch(book, name)
                compare.append((name, pct(*a), pct(*b)))
            kit.table(["leaf", "last week's extract, Q1 to Q2", "the warehouse, Q1 to Q2", "gap, points"],
                      [(n, f"{a:+.1f}%", f"{b:+.1f}%", f"{round(b - a, 1) + 0.0:+.1f}") for n, a, b in compare],
                      caption="Every leaf as a change: two sources of different sizes, compared fairly")
            kit.columns([n for n, *_ in compare],
                        [("last week's extract", [round(100 + a, 1) for _, a, _ in compare]),
                         ("the warehouse", [round(100 + b, 1) for _, _, b in compare])],
                        title="Q2 as an index on Q1 = 100: the customer leaves part company",
                        fmt=lambda v: f"{v:.1f}", lit=(2, 3))
            '''),
        md("""
        **What happened.** The answer is b. Revenue (down 1.6 percent in both), orders (down 14.0 and
        14.1) and revenue per order (up 14.4 and 14.6) agree to within half a point. Customers and
        orders per customer do not: the extract's customers held flat and each ordered 14.0 percent
        less often, while the book's customers fell 7.0 percent and each ordered 7.7 percent less
        often.
        """),
        code(r'''
            gap = {n: b - a for n, a, b in compare}
            kit.check("revenue, orders and revenue per order agree to within a point",
                      all(abs(gap[n]) < 1 for n in ("revenue", "orders", "revenue per order")))
            kit.check("the customer leaf differs by 7 points", round(gap["customers"]) == -7, f"{gap['customers']:+.1f}")
            kit.check("orders per customer differs by about 6 points", 5 < gap["orders per customer"] < 7,
                      f"{gap['orders per customer']:+.1f}")
            '''),
        md("""
        ## 3. Did the customer leaf agree?

        A hurried analyst stops at the totals: both sources fall 1.6 percent, so "the warehouse
        confirms last week", and Anand's sheet carries last week's branch story unchanged.

        **Predict before you run.** If the sheet copies the customer leaf from last week, what does it
        say customers did from Q1 to Q2?

        - a) Fell 7.0 percent.
        - b) Held flat, 0.0 percent.
        - c) Fell 14.0 percent.
        - d) Rose 1.6 percent.
        """),
        code(r'''
            hurried = {"customers": pct(w1["Q1"]["customers"], w1["Q2"]["customers"]),
                       "orders per customer": pct(*branch(w1, "orders per customer"))}
            honest = {"customers": pct(book["Q1"]["customers"], book["Q2"]["customers"]),
                      "orders per customer": pct(*branch(book, "orders per customer"))}
            kit.table(["leaf on Anand's sheet", "the hurried sheet, copied from last week", "the book"],
                      [(n, f"{hurried[n]:+.1f}%", f"{honest[n]:+.1f}%") for n in hurried],
                      caption="The plausible wrong answer beside the book's own leaves")
            '''),
        md("""
        **The plausible wrong answer.** "Customers held flat, 0.0 percent; each ordered 14.0 percent
        less often." It is last week's branch story, carried onto the book because the totals matched.
        On Anand's sheet it keeps the Rs 12 crore parked on a customer count the book does not show.

        **Why it is wrong.** Two trees can multiply to the same total with different branches. The
        extract's revenue ratio is 1.000 for customers times 0.860 for frequency times 1.144 for order
        value, and the book's is 0.930 times 0.923 times 1.146; both come to 0.984. A matching total is
        one leaf matching. The answer is b.

        **The check that exposes it.** Count, in each source, how many customers bought in both
        quarters.
        """),
        code(r'''
            both = len(kit.sql(Q["c2_bought_in_both"]))
            only_q1 = len(kit.sql(Q["c2_bought_q1_only"]))
            only_q2 = len(kit.sql(Q["c2_bought_q2_only"]))
            print(Q["c2_bought_in_both"])
            anyone = both + only_q1 + only_q2
            kit.columns(["last week's extract", "the warehouse"],
                        [("bought in both quarters", [w1["both"], both]),
                         ("bought in one quarter only", [w1["anyone"] - w1["both"], only_q1 + only_q2])],
                        title="The extract held only customers who bought in both quarters")
            def branch_ratios(d):
                """Q2 over Q1 for the three branches of the tree, to three places."""
                return tuple(round(b / a, 3) for a, b in (branch(d, "customers"), branch(d, "orders per customer"),
                                                          branch(d, "revenue per order")))
            ratios = {"extract": branch_ratios(w1), "book": branch_ratios(book)}
            kit.table(["source", "customers", "orders per customer", "revenue per order", "product"],
                      [(s, *r, f"{r[0] * r[1] * r[2]:.3f}") for s, r in ratios.items()],
                      caption="Two trees, one total: different branches multiply to the same 0.984")
            '''),
        code(r'''
            kit.check("every customer in the extract bought in both quarters", w1["both"] == w1["anyone"] == 69)
            kit.check("170 of the book's 301 customers bought in both quarters", (both, anyone) == (170, 301))
            kit.check("both trees multiply to the same revenue ratio",
                      abs(ratios["book"][0] * ratios["book"][1] * ratios["book"][2] - 0.984) < 0.001)
            '''),
        md("""
        **The fix, and what it changed.** The sheet carries the book's own leaves: 244 customers bought
        in Q1 and 227 in Q2, 7.0 percent fewer, and each ordered 7.7 percent less often. Every one of
        the extract's 69 customers bought in both quarters, so its customer count could not fall; the
        book holds 131 customers who bought in only one of them.

        ## A second route: where did the book's 17 fewer Q2 customers come from?

        The first route subtracted two distinct counts, 244 less 227. The second route builds the same
        change from each customer's own history: Q1's customers, less the ones who bought in Q1 and not
        in Q2, plus the ones who bought in Q2 and not in Q1. It uses three `HAVING` filters on one row
        per customer, with no distinct count per quarter anywhere in it.

        **Predict before you run.** How many of Q1's 244 customers bought nothing in Q2?

        - a) 17, the net fall.
        - b) 74.
        - c) 57.
        - d) 244, since the quarters are separate.
        """),
        code(r'''
            print(Q["c2_bought_q1_only"])
            kit.bridge(("Q1 customers", book["Q1"]["customers"]),
                       [("bought in Q1, not in Q2", -only_q1), ("bought in Q2, not in Q1", only_q2)],
                       end_label="Q2 customers", fmt=lambda v: f"{v:,.0f}", lit=(0,),
                       title="The customer leaf's own bridge, from each customer's history")
            print(f"{book['Q1']['customers']} - {only_q1} + {only_q2} = {book['Q1']['customers'] - only_q1 + only_q2}")
            '''),
        code(r'''
            kit.check("the bridge lands on Q2's 227", book["Q1"]["customers"] - only_q1 + only_q2 == book["Q2"]["customers"])
            kit.check("both-quarter customers plus Q1-only customers make Q1", both + only_q1 == book["Q1"]["customers"])
            kit.check("both-quarter customers plus Q2-only customers make Q2", both + only_q2 == book["Q2"]["customers"])
            '''),
        md("""
        **What happened.** The answer is b. 74 of Q1's customers bought nothing in Q2 and 57 customers
        bought in Q2 who had not bought in Q1: 244 less 74 plus 57 is 227, the same number the first
        route reached by subtracting two counts. The net fall of 17 hides 131 customers moving.

        ## 4. What goes on Anand's sheet about last week's note?

        Meera's decision rested on the extract's story: customers held, and each ordered 14.0 percent
        less often. The sheet now carries the book, and it has to say what that means for her.

        **Predict before you run.** Which line belongs under the customer leaf on Anand's sheet?

        - a) "The warehouse confirms last week: revenue fell 1.6 percent in both."
        - b) "On the whole book, 7.0 percent fewer customers bought in Q2, and each ordered 7.7 percent
          less often; last week's extract held only customers who bought in both quarters."
        - c) "Last week's note was wrong, so the Rs 12 crore budget should be released."
        - d) Nothing, since the revenue leaf agrees.
        """),
        code(r'''
            kit.driver_tree({"label": "revenue", "note": f"{pct(book['Q1']['revenue'], book['Q2']['revenue']):+.1f}% on the book",
                             "kind": "lit", "children": [
                {"label": "customers who bought", "note": f"244 to 227, {honest['customers']:+.1f}%", "kind": "bad"},
                {"label": "orders per customer", "note": f"2.20 to 2.04, {honest['orders per customer']:+.1f}%", "kind": "bad"},
                {"label": "revenue per order", "note": f"{pct(*branch(book, 'revenue per order')):+.1f}%", "kind": "good"}]},
                title="The book's tree, Q1 to Q2: two branches fell and one rose")
            kit.table(["what this chapter established", "the evidence"],
                      [("revenue, orders and revenue per order agree with last week", "within half a point each"),
                       ("the customer leaf does not", "flat in the extract, 244 to 227 in the book"),
                       ("the extract held only two-quarter customers", "69 of 69, against 170 of 301 in the book")],
                      caption="The comparison, in three lines")
            '''),
        md("""
        **What happened.** The answer is b. The line names both branches the book shows falling and
        says why the extract could not show the first: its 69 customers all bought in both quarters.
        Option a repeats the one leaf that agrees, c goes further than one chapter's evidence, and d
        leaves Meera deciding on a story the book does not tell. Chapters 3 and 4 find which segment
        carries each branch.
        """),
        code(r'''
            kit.check("the sheet's customer line comes from the book, 244 to 227",
                      (book["Q1"]["customers"], book["Q2"]["customers"]) == (244, 227), f"{honest['customers']:+.1f}%")
            kit.check("the sheet's frequency line comes from the book, not the extract",
                      round(honest["orders per customer"], 1) == -7.7 and round(hurried["orders per customer"], 1) == -14.0)
            '''),
        md("""

        > **Kavya's review.** A matching total is one leaf matching. Set every leaf beside its twin
        > before you say two sources agree, and when they disagree, say which one is the book and put
        > the difference in writing, in the line under the number.

        ### In the interview: what do you do when two sources disagree?

        **[D] Two analysts report different customer counts for the same quarter; how do you settle
        it?** Put the two definitions side by side before the two numbers. Most disagreements are
        definitions: rows against people, customers who bought against customers on the book, one
        window against another. Recompute both from the source of record with each definition written
        in the query, agree which definition answers the question in front of you, and store that
        query so the next count comes from the same place. Here the extract and the warehouse agreed on
        revenue and disagreed on customers because the extract held only customers who bought in both
        quarters.

        **[F] Your total matches last week's; is your analysis the same as last week's?** Only on that
        leaf. A total is a product of branches, and different branches can multiply to the same
        product: here 1.000 times 0.860 times 1.144 and 0.930 times 0.923 times 1.146 both give 0.984.
        Check every leaf as a change before saying two sources tell the same story.

        ### Depth: what can an extract that holds only two-quarter customers never show?

        A customer who stopped buying after Q1, or started in Q2, has orders in one quarter only. An
        extract drawn from customers present in both quarters leaves every such customer out, so its
        customer count is flat by the way it was drawn, and every branch divided by customers carries
        the error forward. On the book those customers are 131 of 301. Whenever a file arrives from
        somewhere else, count how many of its customers appear in both windows, and compare it with the
        book before a branch built on customers goes anywhere.

        ## What did this chapter answer?

        1. **How can two sources of different sizes be compared fairly?** Every leaf as a change from
           Q1 to Q2, since the sources differ five times in size and share no order or customer id.
        2. **Does last week's file still give last week's numbers?** Yes: 186 orders, Rs 1,90,00,000
           and Rs 1,87,00,000, and 69 customers in each quarter, all 69 of whom bought in both.
        3. **Which leaves agree?** Revenue (down 1.6 percent in both), orders (down 14.0 and 14.1) and
           revenue per order (up 14.4 and 14.6).
        4. **Did the customer leaf agree?** No: the extract's customers held flat, and the book's fell
           7.0 percent, from 244 to 227, with orders per customer down 7.7 percent where the extract
           said 14.0.
        5. **Where did the 17 fewer customers come from?** 74 bought in Q1 and not in Q2, and 57 bought
           in Q2 and not in Q1: 244 less 74 plus 57 is 227.
        6. **What goes on Anand's sheet?** The book's leaves, with one line saying that on the whole
           book 7.0 percent fewer customers bought in Q2 as well as each buying 7.7 percent less often.

        Chapter 3 splits the book by segment, to find which one carried the fall.
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 3
def ch3():
    return [
        md("""
        # Which segment carried the fall from Q1 to Q2, and how often did its customers order?

        **Week 2, Monday. Chapter 3 of 6.** Chapters 1 and 2 answered the tree for the whole book;
        this chapter answers it for each segment.

        > "I want these numbers every Monday, for every segment and channel."
        > Anand Iyer, finance controller, Kalpa Retail

        **Who needs the answer.** Anand's sheet carries one line per segment, and the head of
        Retail-Plus reads the Retail-Plus line to decide which members the team works to keep. A wrong
        frequency on that line sends the retention budget to the wrong segment: a tier whose members
        seem to order half as often gets an emergency plan, and a segment that seems to order twice as
        often gets money it does not need.

        **The questions on the way.**
        1. One query per segment, one grouped query, or pandas?
        2. How many orders, customers and rupees did each segment book in each quarter?
        3. Which segment-quarters hold too few customers to quote a rate on?
        4. How often did each segment's customers order?
        5. Does the average of each customer's own order count agree?

        **The metric at stake.** Revenue per segment and quarter, and orders per customer per segment:
        orders in the quarter divided by the customers who bought in it. Kalpa sells to four segments:
        Business (corporate buyers), Retail-Core (everyday shoppers), Retail-Plus (the paid membership
        tier) and Student. Revenue is booked revenue. Q1 is April to June 2026 and Q2 is July to
        September 2026.

        **What chapters 1 and 2 found.** The book fell 1.6 percent, from Rs 10,00,00,000 on 538 orders
        to Rs 9,84,00,000 on 462. The customers who bought fell from 244 to 227, and each ordered 7.7
        percent less often. Last week's note said Retail-Plus members were ordering less often; the
        book has not yet been asked about any single segment.

        **A real company with the same question.** Eternal, the company behind Zomato and Blinkit,
        reported that its consumer businesses' net order value grew 54 percent year on year to
        Rs 31,120 crore in the quarter to 30 June 2026, and in the same letter that food delivery grew
        a little over 20 percent (Rs 10,769 crore), quick commerce 86 percent (Rs 17,132 crore) and
        going-out 60 percent (Rs 3,218 crore) (Eternal, shareholders' letter for Q1 FY27, 22 July 2026).
        The group's 54 percent is three different stories, and the letter tells each one. Kalpa's 1.6
        percent is four.
        """),
        setup_note("03_which_segment"),
        setup("03_which_segment"),
        where(3, ["the options\nfour ways to split by segment", "each segment's leaves\none GROUP BY",
                  "the thin groups\nHAVING", "orders per customer\nthe division",
                  "a second route\neach customer's own count"]),
        md("""
        ## The options: one query per segment, one grouped query, or pandas?

        Four ways a team could put every segment's leaves on Anand's sheet. They differ in how many
        queries someone has to keep correct, in the rows each moves, and in what happens the day Kalpa
        adds a fifth segment.

        | Option | Queries to keep | Rows it moves | When a fifth segment appears |
        |---|---|---|---|
        | A. One query per segment, `WHERE c.segment = '...'` | Four, one per segment | One row per quarter from each | It is silently missing: no query asks for it |
        | B. One query, `GROUP BY c.segment, o.quarter` | One | One row per segment and quarter | It appears as two new rows |
        | C. Pull the order rows into pandas and group there | One query and a Python step | Every order row | It appears, on a copy of the book |
        | D. One wide row per segment, a column per quarter and measure | One | One row per segment | It appears, and every new measure adds two columns |

        The segment lives on the customer, so each option looks up every order's segment with one line,
        `JOIN customers c USING (customer_id)`. Joins are Tuesday's topic; today the line is only that
        lookup.

        **Predict before you run.** Option A's Retail-Plus query is below. How many rows does it
        return, and how many would option C move to answer the same question for every segment?

        - a) 2 rows, and 1,000.
        - b) 8 rows, and 8.
        - c) 2 rows, and 8.
        - d) 1 row, and 1,000.
        """),
        code(r'''
            one = run("c3_one_segment", "Option A for Retail-Plus: one query, one segment", money=("revenue",))
            segments = [r["segment"] for r in kit.sql("SELECT DISTINCT segment FROM customers ORDER BY segment")]
            order_rows = kit.sql("SELECT count(*) AS n FROM orders")[0]["n"]
            sizing = [("A. a query per segment", f"{len(segments)} queries", f"{len(one) * len(segments)} rows"),
                      ("B. one GROUP BY", "1 query", f"{2 * len(segments)} rows"),
                      ("C. pandas on the rows", "1 query and Python", f"{order_rows:,} rows"),
                      ("D. one wide row per segment", "1 query", f"{len(segments)} rows")]
            kit.table(["option", "queries to keep", "rows moved"], sizing,
                      caption=f"Sized on this warehouse, which holds {len(segments)} segments")
            '''),
        md("""
        **What happened.** The answer is a. Option A returns two rows for Retail-Plus, one per quarter,
        and needs four queries for the four segments; option C moves all 1,000 order rows to group them
        in Python.

        **The best-fit call.** Option B, one `GROUP BY c.segment, o.quarter`. One query to keep
        correct, eight rows back, and a new segment appears on the sheet the Monday it is created
        instead of going missing. **What would change the call:** a one-off question about a single
        segment, such as the head of Retail-Plus asking about the tier alone, is option A's job, and
        one `WHERE` is the clearest way to write it.
        """),
        code(r'''
            kit.check("the warehouse holds four segments", len(segments) == 4, ", ".join(segments))
            kit.check("option A returns one row per quarter", len(one) == 2)
            '''),
        md("""
        ## 1. How many orders, customers and rupees did each segment book in each quarter?

        The first try selects the segment and groups only by the quarter. Postgres refuses it, and the
        refusal is worth two minutes of reading.
        """),
        code(r'''
            print(Q["c3_group_error"])
            with kit.expect_error() as err:
                kit.sql(Q["c3_group_error"])
            '''),
        md("""
        The last line says `column "c.segment" must appear in the GROUP BY clause or be used in an
        aggregate function`. In the order a query runs, `GROUP BY` forms the groups before `SELECT`
        picks the columns, so each group, here one quarter, holds orders from four segments, and
        `SELECT c.segment` has four values to print on one row. There are two fixes: group by the
        segment too, or put the segment inside an aggregate such as `min(c.segment)`. The first is the
        one the question asks for.

        The order a query runs in is the day's one picture. It is written SELECT, FROM, WHERE, GROUP
        BY, HAVING, ORDER BY, LIMIT, and it runs as the arrows below show, so SELECT sees groups that
        already exist.
        """),
        code(r'''
            kit.flow(["FROM\nthe table and\nthe lookup", "WHERE\nkeep rows", "GROUP BY\nform groups",
                      "HAVING\nkeep groups", "SELECT\npick and compute", "ORDER BY\nsort", "LIMIT\ncut"],
                     lit=4, title="The order a query runs in: SELECT comes fifth")
            '''),
        md("""
        **Predict before you run.** With `GROUP BY c.segment, o.quarter`, how many rows come back?

        - a) 2, one per quarter.
        - b) 4, one per segment.
        - c) 8, one per segment and quarter.
        - d) 1,000, one per order.
        """),
        code(r'''
            seg = run("c3_segments", "Each segment's leaves in each quarter", money=("revenue",))
            by = {(r["segment"], r["quarter"]): {k: num(v) for k, v in r.items()} for r in seg}
            kit.columns(segments,
                        [("Q1 orders", [by[(s, "Q1")]["orders"] for s in segments]),
                         ("Q2 orders", [by[(s, "Q2")]["orders"] for s in segments])],
                        title="Orders per segment: Retail-Plus lost 75 of the book's 76", lit=(2,))
            '''),
        code(r'''
            fall = [(s, by[(s, "Q2")]["revenue"] - by[(s, "Q1")]["revenue"]) for s in segments]
            kit.bridge(("Q1 revenue", sum(by[(s, "Q1")]["revenue"] for s in segments)), fall,
                       end_label="Q2 revenue", lo=96000000, lit=(0, 2),
                       title="Where the Rs 16 lakh fall sits: Business in rupees, Retail-Plus in orders")
            for s, f in fall:
                print(f"{s:12} {kit.rupees(f):>16}  {pct(by[(s, 'Q1')]['revenue'], by[(s, 'Q2')]['revenue']):+.1f}%")
            '''),
        md("""
        **What happened.** The answer is c: eight rows. The chart's floor starts at Rs 9.6 crore so the
        segment moves are visible against the totals. Business books 99 percent of the rupees, so it
        carries Rs 14,29,840 of the Rs 16,00,000 fall on only 6 fewer orders, a 1.4 percent dip.
        Retail-Plus lost 75 of the book's 76 fewer orders and 29.4 percent of its revenue, Rs 1,72,390.
        Retail-Core fell 1.8 percent and Student rose 33.9 percent. The segment the total hides is
        Retail-Plus.
        """),
        code(r'''
            kit.check("eight rows, one per segment and quarter", len(seg) == 8)
            kit.check("the segments add back to the book's 538 and 462 orders",
                      (sum(by[(s, "Q1")]["orders"] for s in segments), sum(by[(s, "Q2")]["orders"] for s in segments)) == (538, 462))
            kit.check("Retail-Plus lost 75 of the 76 fewer orders",
                      by[("Retail-Plus", "Q1")]["orders"] - by[("Retail-Plus", "Q2")]["orders"] == 75)
            kit.check("Retail-Plus revenue fell 29.4 percent",
                      round(pct(by[("Retail-Plus", "Q1")]["revenue"], by[("Retail-Plus", "Q2")]["revenue"]), 1) == -29.4)
            '''),
        md("""
        ## 2. Which segment-quarters hold too few customers to quote a rate on?

        Kavya's rule from Week 1 holds here: a rate built on fewer than 30 customers moves a long way
        when one customer changes, so it goes on the sheet flagged. The test is on a group, the
        customers in a segment and quarter, so it sits in `HAVING`, which runs after the groups exist;
        `WHERE` runs before them and tests one order at a time.

        **Predict before you run.** Which segment-quarters have fewer than 30 customers?

        - a) None.
        - b) Student in both quarters.
        - c) Student in Q1 only.
        - d) Student and Business in both quarters.
        """),
        code(r'''
            thin = run("c3_thin", "Segment-quarters to flag on the sheet")
            kit.bars([(f"{s} {q}", by[(s, q)]["customers"]) for s in segments for q in ("Q1", "Q2")],
                     title="Customers per segment and quarter; the flag sits below 30",
                     lit=tuple(i for i, (s, q) in enumerate((s, q) for s in segments for q in ("Q1", "Q2"))
                               if by[(s, q)]["customers"] < 30))
            '''),
        md("""
        **What happened.** The answer is b. Student had 15 customers in Q1 and 20 in Q2, so its 33.9
        percent rise goes on the sheet with the flag beside it. Business, with 36 and 35, clears the
        bar.
        """),
        code(r'''
            kit.check("two segment-quarters are flagged", len(thin) == 2)
            kit.check("both flags are Student", {r["segment"] for r in thin} == {"Student"})
            '''),
        md("""
        ## 3. How often did each segment's customers order?

        Orders per customer is orders divided by customers, so the quickest query divides the two
        counts it already has:

        ```sql
        count(*) / count(DISTINCT o.customer_id) AS orders_per_customer
        ```

        **Predict before you run.** Retail-Plus placed 215 orders from 91 customers in Q1 and 140 from
        76 in Q2. What does the query print for its two quarters?

        - a) 2.36 and 1.84.
        - b) 2 and 1.
        - c) 2.4 and 1.8.
        - d) An error, since a count cannot be divided.
        """),
        code(r'''
            hurried = {(r["segment"], r["quarter"]): int(r["orders_per_customer"])
                       for r in run("c3_frequency_hurried", "The hurried frequency, exactly as the query returns it")}
            kit.table(["segment", "Q1", "Q2", "what the sheet would say"],
                      [(s, hurried[(s, "Q1")], hurried[(s, "Q2")],
                        "halved" if hurried[(s, "Q2")] * 2 == hurried[(s, "Q1")]
                        else "doubled" if hurried[(s, "Q2")] == 2 * hurried[(s, "Q1")] else "no change")
                       for s in segments], caption="The plausible wrong answer, segment by segment")
            '''),
        md("""
        **The plausible wrong answer.** Retail-Plus 2 then 1: its members' frequency halved. Retail-Core
        1 then 2: its customers' frequency doubled. On Anand's sheet the head of Retail-Plus sees an
        emergency, and the retention budget moves to Retail-Core, whose customers seem to be ordering
        twice as often.

        **Why it is wrong.** `count(*)` and `count(DISTINCT ...)` return whole numbers, and Postgres
        divides two whole numbers as whole numbers: "for integral types, division truncates the result
        towards zero" (PostgreSQL 16 documentation, mathematical functions and operators), so 5 / 2 is
        2. The query dropped the fraction without a word. `sum(amount) / count(*)` in chapter 1 kept its
        decimals because `amount` is stored as `numeric`. The answer is b.
        """),
        code(r'''
            run("c3_integer_division", "The same two divisions, whole and numeric")
            '''),
        md("""
        **The check that exposes it.** A ratio multiplied by what it divides by gives back what it
        divided. Orders per customer times customers must give the orders.
        """),
        code(r'''
            back = [(s, q, hurried[(s, q)], by[(s, q)]["customers"], hurried[(s, q)] * by[(s, q)]["customers"],
                     by[(s, q)]["orders"]) for s in segments for q in ("Q1", "Q2")]
            kit.table(["segment", "quarter", "ratio", "customers", "ratio x customers", "orders"], back,
                      caption="Multiplied back, the hurried ratios lose orders in every row")
            kit.check("the hurried ratio multiplied back misses the orders in every row",
                      all(r[4] != r[5] for r in back), f"Retail-Plus Q2: 1 x 76 = 76 against 140")
            '''),
        md("""
        **The fix, and what it changed.** Divide in `numeric`, round on purpose to two places, and keep
        the counts beside the ratio so anyone can multiply it back.
        """),
        code(r'''
            freq = {(r["segment"], r["quarter"]): {k: num(v) for k, v in r.items()}
                    for r in run("c3_frequency", "The fix: numeric division, rounded on purpose",
                                 money=("revenue_per_order",))}
            kit.columns(segments,
                        [("Q1", [freq[(s, "Q1")]["orders_per_customer"] for s in segments]),
                         ("Q2", [freq[(s, "Q2")]["orders_per_customer"] for s in segments])],
                        title="Orders per customer: Retail-Plus fell 22 percent, Retail-Core rose 3",
                        fmt=lambda v: f"{v:.2f}", lit=(2,))
            for s in segments:
                a, b = freq[(s, "Q1")], freq[(s, "Q2")]
                change = pct(a["orders"] / a["customers"], b["orders"] / b["customers"])
                print(f"{s:12} {a['orders_per_customer']:.2f} to {b['orders_per_customer']:.2f}, "
                      f"{change:+.1f}% from the unrounded counts")
            '''),
        code(r'''
            plus = (freq[("Retail-Plus", "Q1")]["orders_per_customer"], freq[("Retail-Plus", "Q2")]["orders_per_customer"])
            kit.check("Retail-Plus ordered 2.36 then 1.84 times", plus == (2.36, 1.84), f"{plus}")
            kit.check("Retail-Core rose, from 1.95 to 2.01",
                      (freq[("Retail-Core", "Q1")]["orders_per_customer"], freq[("Retail-Core", "Q2")]["orders_per_customer"]) == (1.95, 2.01))
            kit.check("every fixed ratio multiplies back to its orders within half an order",
                      all(abs(freq[k]["orders_per_customer"] * freq[k]["customers"] - freq[k]["orders"]) < 0.5 for k in freq))
            '''),
        md("""
        **What happened.** Retail-Plus members ordered 2.36 times in Q1 and 1.84 times in Q2, a fall of
        22.0 percent where the hurried query said 50. Retail-Core rose from 1.95 to 2.01, 3.0 percent
        where it said 100. Business went from 2.69 to 2.60, down 3.5 percent, and Student from 1.80 to
        1.90, up 5.6 percent; each change is computed from the counts before rounding. The frequency
        branch that fell is Retail-Plus's, as last week's note said, and on the book it fell 22.0
        percent.

        ## A second route: does the average of each customer's own order count agree?

        The first route divided two counts. The second route never divides counts: it asks the
        warehouse for each customer's own number of orders in each quarter, one row per customer and
        quarter, and averages those numbers in Python. If the division was right, the average of the
        individual counts must equal it.

        **Predict before you run.** For Retail-Plus in Q2, what is the average of the 76 customers' own
        order counts?

        - a) 1, since most bought once.
        - b) 1.84.
        - c) 2, the median customer.
        - d) 140, the orders.
        """),
        code(r'''
            per = kit.sql(Q["c3_per_customer_counts"])
            print(f"{len(per)} rows, one per customer and quarter")
            groups = {}
            for r in per:
                groups.setdefault((r["segment"], r["quarter"]), []).append(int(r["orders"]))
            route2 = {k: round(sum(v) / len(v), 2) for k, v in groups.items()}
            kit.table(["segment", "quarter", "division of counts", "average of own counts"],
                      [(s, q, f"{freq[(s, q)]['orders_per_customer']:.2f}", f"{route2[(s, q)]:.2f}")
                       for s in segments for q in ("Q1", "Q2")],
                      caption="Two routes to orders per customer")
            kit.strip([float(v) for v in groups[("Retail-Plus", "Q2")]],
                      markers=[("average 1.84", route2[("Retail-Plus", "Q2")], "good")],
                      fmt=lambda v: f"{v:.0f}", lo=0, hi=6,
                      title="Retail-Plus Q2: each dot is one member's orders; their average is the ratio")
            '''),
        code(r'''
            kit.check("the second route agrees with the numeric division in all eight rows",
                      all(route2[k] == freq[k]["orders_per_customer"] for k in freq))
            kit.check("the per-customer rows number the customers of the eight groups, 471",
                      len(per) == sum(freq[k]["customers"] for k in freq) == 471, f"{len(per)} rows")
            '''),
        md("""
        **What happened.** The answer is b. The average of the 76 members' own order counts is 1.84, and
        all eight segment-quarters agree with the numeric division to two places. The division was
        right once it was done in `numeric`.

        > **Kavya's review.** Divide in numeric and round on purpose, and keep the counts beside every
        > ratio, so anyone reading the sheet can multiply it back. A ratio that cannot be multiplied
        > back to its orders is a number nobody should sign.

        ### In the interview: what do you check when a ratio looks wrong, and what do WHERE and HAVING each do?

        **[F] Orders per customer reads 1 for a segment; what do you check first?** Whether the
        database divided two whole numbers. In Postgres `count(*) / count(DISTINCT customer_id)` is
        integer division and drops the fraction, so 140 orders over 76 customers prints 1. Multiply
        the ratio back by the customers: 1 times 76 is 76, not 140. Cast one side to `numeric`, round
        to the places the reader needs, and show the counts beside the ratio.

        **[S] WHERE against HAVING, one sentence each.** `WHERE` keeps or drops rows before any group
        is formed, so it can test a column of one order; `HAVING` keeps or drops groups after they are
        formed, so it can test an aggregate such as `count(DISTINCT customer_id) < 30`.

        **[S] Explain the logical order in which a SQL query runs.** `FROM` and the lookup first, then
        `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, `ORDER BY` and `LIMIT`. It explains the day's refusals:
        `SELECT` cannot print a column the groups do not pin down, and `WHERE` cannot test an aggregate
        that does not exist yet.

        ### Depth: why does Postgres divide integers this way, when a spreadsheet does not?

        A spreadsheet stores every number as a floating-point value, so 140 / 76 gives 1.84 whatever
        you typed. Postgres keeps the type of each value, and an operation on two integers returns an
        integer, which is why `215 / 91` is 2 and `215::numeric / 91` is 2.3626. Other databases differ:
        some return a decimal from the same division. The habit that survives every database is the
        same: say the type you want, and multiply the result back.

        ## What did this chapter answer?

        1. **One query per segment, one grouped query, or pandas?** One `GROUP BY c.segment,
           o.quarter`: one query, eight rows, and a new segment appears by itself.
        2. **What did each segment book?** Business Rs 9,90,14,440 then Rs 9,75,84,600, down 1.4
           percent; Retail-Plus Rs 5,85,770 then Rs 4,13,380, down 29.4 percent on 75 fewer orders;
           Retail-Core down 1.8 percent; Student up 33.9 percent.
        3. **Which groups are too thin?** Student in both quarters, with 15 and 20 customers.
        4. **How often did each segment's customers order?** Retail-Plus 2.36 then 1.84, down 22.0
           percent; the integer division said 2 then 1, "halved", and put Retail-Core at 1 then 2.
        5. **Does the second route agree?** Yes: the average of each customer's own count matches the
           numeric division in all eight rows.

        Chapter 4 sets Q1 beside Q2 for every branch in one query, and asks how much less each
        Retail-Plus member spent.
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 4
def ch4():
    return [
        md("""
        # Which branch of each segment's tree moved, and how much less did each Retail-Plus member spend?

        **Week 2, Monday. Chapter 4 of 6.** Chapter 3 put each segment's leaves on their own rows;
        this chapter sets Q1 beside Q2 for every branch in one query, and prices the fall per member.

        > "How much less is each of my members spending, and is it fewer members buying or each one
        > buying less?"
        > The head of Retail-Plus, Kalpa Retail

        **Who needs the answer.** Anand's analyst wants the quarter comparison as one query that reads
        from top to bottom, and the head of Retail-Plus decides how hard to work to keep the tier's
        members. An average that quietly leaves out the members who stopped buying says the tier's
        spend per member fell 15.5 percent when it fell 29.4, and says Retail-Core and Business members
        spent more when they spent less. The tier would get a light touch while it lost nearly a third
        of its spend.

        **The questions on the way.**
        1. Nested subqueries, named steps or temporary tables?
        2. How did customers, frequency and order value move in each segment?
        3. How much less did each Retail-Plus member spend?
        4. Does a member count taken from the customer table give the same change?

        **The metric at stake.** Each branch of the tree as a ratio, Q2 over Q1: customers who bought,
        orders per customer and revenue per order, which multiply to revenue. And spend per member, the
        rupees a member spent in a quarter, averaged over the tier's members. Revenue is booked
        revenue; Q1 is April to June 2026 and Q2 is July to September 2026.

        **What chapter 3 found.** Retail-Plus lost 75 of the book's 76 fewer orders and 29.4 percent of
        its revenue, from Rs 5,85,770 to Rs 4,13,380, and its members' orders per customer fell from
        2.36 to 1.84 once the division was done in `numeric`. Business carries most of the rupees and
        fell 1.4 percent.

        **A real company with the same question.** GitLab's data team publishes the SQL style guide it
        writes to: "Prefer CTEs over sub-queries as CTEs make SQL more readable ...", each CTE should
        "perform a single, logical unit of work", and a calculation should carry "a brief description
        of what's going on" (GitLab handbook, SQL Style Guide, checked 30 September 2026). A team whose
        queries are read by other people writes them as named steps. The guide also calls CTEs more
        performant on GitLab's own warehouse; on Postgres the reason to name steps is the reader.
        """),
        setup_note("04_which_branch"),
        setup("04_which_branch"),
        where(4, ["the options\nsubquery, CTE or temporary table", "each branch\nQ2 over Q1 per segment",
                  "spend per member\nwho is inside the average", "a second route\nthe tier's own count"]),
        md("""
        ## The options: nested subqueries, named steps or temporary tables?

        The comparison needs the same leaves computed twice, once per quarter, and then set side by
        side. Three ways to write it:

        | Option | How the analyst reads it | Rows written into the warehouse | What a rerun needs |
        |---|---|---|---|
        | A. Nested subqueries, each quarter inside the main query | From the innermost bracket outwards | None | The one statement |
        | B. CTEs, `WITH book AS (...), q1 AS (...), q2 AS (...)`, each a named step | From the top down, one step at a time, each with its comment | None: Postgres works each step out while the query runs | The one statement |
        | C. Temporary tables, one `CREATE TEMP TABLE` per step | Several statements, run in order | One temporary table per step, for the session | Every statement, in the same session, in order |

        **Predict before you run.** Option C writes the Q1 leaves into a temporary table. The analyst
        opens a new session and reads it. What happens?

        - a) The analyst sees the same four rows.
        - b) The analyst sees an empty table.
        - c) The table does not exist in the analyst's session.
        - d) The analyst sees the rows as they stand in the warehouse now.
        """),
        code(r'''
            nested = kit.sql(Q["c4_nested"])
            print(Q["c4_temp_step"])
            conn = kit.connect()
            try:
                kit.sql(Q["c4_temp_step"], conn=conn)
                same_session = kit.sql(Q["c4_temp_read"], conn=conn)
            finally:
                conn.close()
            with kit.expect_error() as gone:
                kit.sql(Q["c4_temp_read"])
            kit.table(["option", "statements to run", "rows written", "a rerun in a new session"],
                      [("A. nested subqueries", 1, 0, "works"),
                       ("B. CTEs", 1, 0, "works"),
                       ("C. temporary tables", 2, len(same_session), gone.name or "works")],
                      caption="Sized on this warehouse: the three ways to write the comparison")
            '''),
        md("""
        **What happened.** The answer is c. In the session that made it, the temporary table held four
        rows, one per segment; a new session, which is what the analyst opens, finds no such table and
        stops with `UndefinedTable`. Nested subqueries and CTEs are single statements, so the analyst
        reruns exactly what the team ran.

        **The best-fit call.** Option B, CTEs. The analyst reads the steps in the order they happen,
        each with a name and a one-line comment, and one statement reruns anywhere. Postgres computes a
        CTE once per run even when two later steps read it, and writes nothing into the warehouse.
        **What would change the call:** a step that many queries reuse over millions of rows in one long
        session is cheaper as a temporary table, computed once and read many times; that is a
        performance choice for the platform team, and Anand's suite is not there.
        """),
        code(r'''
            kit.check("the temporary table answered in its own session", len(same_session) == 4)
            kit.check("a new session cannot see it", gone.name == "UndefinedTable", gone.name)
            kit.check("the nested version returns one row per segment", len(nested) == 4)
            '''),
        md("""
        ## 1. How did customers, frequency and order value move in each segment?

        The CTE version names four steps: `book` looks up each order's segment, `q1` and `q2` compute
        each quarter's leaves per segment, and the last step divides Q2 by Q1 for each branch. The tree
        says the three branch ratios multiply to the revenue ratio, so the query checks itself.

        **Predict before you run.** Which branch fell furthest in Retail-Plus?

        - a) Customers who bought.
        - b) Orders per customer.
        - c) Revenue per order.
        - d) All three fell by the same amount.
        """),
        code(r'''
            ratios = {r["segment"]: {k: num(v) for k, v in r.items()}
                      for r in run("c4_branches", "Each branch as Q2 over Q1, per segment")}
            segs = list(ratios)
            names = [("customers_ratio", "customers"), ("frequency_ratio", "orders per customer"),
                     ("order_value_ratio", "revenue per order"), ("revenue_ratio", "revenue")]
            kit.columns(segs, [(label, [round(100 * ratios[s][k], 1) for s in segs]) for k, label in names],
                        title="Q2 as an index on Q1 = 100: Retail-Plus lost customers and frequency",
                        fmt=lambda v: f"{v:.0f}", lit=(2,))
            '''),
        md("""
        **What happened.** The answer is b. In Retail-Plus, customers who bought fell to 0.835 of Q1 (91
        to 76, down 16.5 percent), orders per customer to 0.780 (down 22.0 percent) and revenue per
        order rose to 1.084 (up 8.4 percent); together they multiply to 0.706, the 29.4 percent fall.
        Frequency is the branch that fell furthest, and fewer members buying comes second. Business
        moved about 3 percent on each branch, and Student grew on customers.
        """),
        code(r'''
            p = ratios["Retail-Plus"]
            kit.check("the three branches multiply back to the revenue ratio in every segment",
                      all(abs(r["customers_ratio"] * r["frequency_ratio"] * r["order_value_ratio"] - r["revenue_ratio"]) < 0.002
                          for r in ratios.values()))
            kit.check("in Retail-Plus, frequency fell further than customers",
                      p["frequency_ratio"] < p["customers_ratio"], f"{p['frequency_ratio']} against {p['customers_ratio']}")
            kit.check("Retail-Plus revenue is 0.706 of Q1", p["revenue_ratio"] == 0.706)
            '''),
        md("""
        ## 2. How much less did each Retail-Plus member spend?

        The head of Retail-Plus asks for one number per quarter: the average member's spend. A hurried
        analyst builds one row per member with a `CASE` per quarter, `sum(CASE WHEN o.quarter = 'Q1'
        THEN o.amount END)`, and averages each column.

        **Predict before you run.** How does the average member's spend move from Q1 to Q2?

        - a) Down about 15 percent.
        - b) Down about 29 percent, as revenue did.
        - c) Up, since revenue per order rose.
        - d) It cannot be averaged, since some members have no Q2 orders.
        """),
        code(r'''
            hurried = {k: num(v) for k, v in run("c4_member_spend_hurried", "The hurried averages",
                                                money=("q1_average", "q2_average"))[0].items()}
            every = {r["segment"]: {k: num(v) for k, v in r.items()}
                     for r in kit.sql(Q["c4_every_segment"])}
            kit.table(["segment", "Q1 to Q2, the hurried average"],
                      [(s, f"{pct(every[s]['q1_skipping'], every[s]['q2_skipping']):+.1f}%") for s in every],
                      caption="The same hurried average for every segment")
            '''),
        md("""
        **The plausible wrong answer.** A Retail-Plus member spent Rs 6,437 in Q1 and Rs 5,439 in Q2,
        down 15.5 percent, and Retail-Core and Business members each spent more in Q2 than in Q1. The
        head of Retail-Plus reads a modest dip and plans a light touch, and the sheet says two segments
        grew per member.

        **Why it is wrong.** A `CASE` with no `ELSE` gives a missing value, `NULL`, for a member with no
        order in that quarter, and `avg` skips missing values without saying so: the PostgreSQL
        documentation says `avg` "computes the average (arithmetic mean) of all the non-null input
        values". So the Q1 average is over the members who bought in Q1 and the Q2 average over the
        members who bought in Q2: two different groups of people. The 31 members who bought in Q1 and
        stopped are left out of Q2's average, which is the fall the head of Retail-Plus most needs to
        see. The answer the query gave was a; the honest answer is b.

        **The check that exposes it.** Count who is inside each average.
        """),
        code(r'''
            who = {k: int(v) for k, v in run("c4_who_is_averaged", "Who is inside each average")[0].items()}
            kit.bars([("members in the step", who["members_in_the_step"]),
                      ("inside the Q1 average", who["inside_the_q1_average"]),
                      ("inside the Q2 average", who["inside_the_q2_average"])],
                     title="The two averages are taken over different members", lit=(2,))
            run("c4_invented_null", "The mechanism on three invented values: 100, a missing value and 200")
            '''),
        code(r'''
            kit.check("the step holds 107 members", who["members_in_the_step"] == 107)
            kit.check("the two averages cover different members",
                      who["inside_the_q1_average"] != who["inside_the_q2_average"],
                      f"{who['inside_the_q1_average']} and {who['inside_the_q2_average']}")
            '''),
        md("""
        On the three invented values, `avg` returns 150, the mean of the two values present, where 100
        is the mean once the missing value is read as zero; `count(*)` sees three rows and `count(x)`
        two. The same thing happened to the members: 107 in the step, 91 inside the Q1 average and 76
        inside the Q2 average.

        **The fix, and what it changed.** A member who bought nothing in a quarter spent Rs 0 in it, so
        say so on purpose with `coalesce(..., 0)`, and both averages cover the same 107 members.
        """),
        code(r'''
            fixed = {k: num(v) for k, v in run("c4_member_spend", "The fix: Rs 0 said on purpose",
                                              money=("q1_average", "q2_average"))[0].items()}
            kit.bars([("the hurried average", abs(pct(hurried["q1_average"], hurried["q2_average"]))),
                      ("Rs 0 said on purpose", abs(pct(fixed["q1_average"], fixed["q2_average"])))],
                     fmt=lambda v: f"down {v:.1f}%", lit=(1,),
                     title="How far Retail-Plus spend per member fell: the hurried average halves it")
            kit.table(["segment", "the hurried average, Q1 to Q2", "Rs 0 said on purpose, Q1 to Q2"],
                      [(s, f"{pct(every[s]['q1_skipping'], every[s]['q2_skipping']):+.1f}%",
                        f"{pct(every[s]['q1_with_zero'], every[s]['q2_with_zero']):+.1f}%") for s in every],
                      caption="Every segment: Retail-Core and Business flip from a rise to a fall")
            print(f"Retail-Plus: {kit.rupees(fixed['q1_average'])} to {kit.rupees(fixed['q2_average'])}, "
                  f"{pct(fixed['q1_average'], fixed['q2_average']):+.1f}% over {fixed['members']} members")
            '''),
        code(r'''
            kit.check("both averages now cover the same 107 members", fixed["members"] == 107)
            kit.check("spend per member falls 29.4 percent, as revenue does",
                      round(pct(fixed["q1_average"], fixed["q2_average"]), 1) == -29.4)
            kit.check("Retail-Core and Business flip from a rise to a fall",
                      all(every[s]["q2_skipping"] > every[s]["q1_skipping"] and every[s]["q2_with_zero"] < every[s]["q1_with_zero"]
                          for s in ("Retail-Core", "Business")))
            '''),
        md("""
        **What happened.** Over the same 107 members, a Retail-Plus member spent Rs 5,474 in Q1 and
        Rs 3,863 in Q2, down 29.4 percent, twice the hurried 15.5. Retail-Core moves from up 4.3 percent
        to down 1.8, and Business from up 1.4 to down 1.4. Only Student rose, by 33.9 percent, on 24
        members, which chapter 3 flagged as too few for a rate.

        ## A second route: does a member count taken from the customer table give the same change?

        The first route averaged one row per member built from the orders. The second never averages:
        it divides each quarter's Retail-Plus revenue by the tier's members on the customer table,
        bought or not, counted in a subquery. Its base is 120 members where the first route's was 107,
        so its levels differ, and if both are fair its change must match.

        **Predict before you run.** Over the tier's members on the customer table, how does spend per
        member move?

        - a) Down 15.5 percent.
        - b) Down 29.4 percent.
        - c) Down more than 29.4 percent, since the base is larger.
        - d) It cannot be computed without a join.
        """),
        code(r'''
            tier = {r["quarter"]: {k: num(v) for k, v in r.items()}
                    for r in run("c4_per_member_of_the_tier", "Retail-Plus revenue over every member of the tier",
                                 money=("revenue", "spend_per_member"))}
            kit.line(["Q1", "Q2"],
                     [("over the 107 who bought, Rs 0 said", [fixed["q1_average"], fixed["q2_average"]], "good"),
                      ("over the tier's 120 members", [tier["Q1"]["spend_per_member"], tier["Q2"]["spend_per_member"]], "lit"),
                      ("the hurried average", [hurried["q1_average"], hurried["q2_average"]], "bad")],
                     fmt=lambda v: kit.rupees(v), title="Two fair bases fall together; the hurried average falls half as far")
            '''),
        code(r'''
            route2 = pct(tier["Q1"]["spend_per_member"], tier["Q2"]["spend_per_member"])
            kit.check("the tier holds 120 members", tier["Q1"]["members_on_the_book"] == 120)
            kit.check("the second route falls 29.4 percent, as the fixed average does", round(route2, 1) == -29.4, f"{route2:.1f}%")
            kit.check("the product of the branches gives the same fall",
                      round(100 * (p["customers_ratio"] * p["frequency_ratio"] * p["order_value_ratio"] - 1), 1) == -29.4)
            '''),
        md("""
        **What happened.** The answer is b. Over the tier's 120 members, spend per member went from
        Rs 4,881 to Rs 3,445, down 29.4 percent: the same change as the fixed average over 107 members,
        and the same as the product of the three branches. Any fixed group of members gives the same
        change; only an average whose members change between quarters gives a different one.

        > **Kavya's review.** An average names who is inside it. Put the zero in on purpose, and write
        > the count of members beside the average, so the reader sees that Q1 and Q2 are over the same
        > people.

        ### In the interview: why can an average move when the total does not, and when is a CTE better than a subquery?

        **[F] An average moved but the total did not, or moved differently; how?** The denominator
        changed. `avg` counts only the rows whose value is present, so if a quarter's missing values
        stand for members who bought nothing, those members drop out of that quarter's average. Count
        the rows inside the average with `count(column)` beside `count(*)`, decide what a missing value
        means, and say it with `coalesce`. Here the Retail-Plus average fell 15.5 percent while revenue
        fell 29.4, because 31 members who stopped buying left the Q2 average.

        **[F] When would you use a CTE instead of a subquery?** When a step deserves a name, when the
        same step is read more than once, or when someone else has to read the query from the top down.
        A CTE runs as part of one statement and writes nothing, so an auditor reruns it whole; a
        temporary table lives only in the session that made it.

        ### Depth: why is a quarter with no orders a NULL and not a zero?

        `sum` over no rows returns `NULL`, not zero, and a `CASE` with no `ELSE` returns `NULL` for every
        row it does not match: "sum of no rows returns null, not zero as one might expect" (PostgreSQL
        16 documentation, aggregate functions). A missing value can mean zero, unknown or not
        applicable, and SQL cannot tell which, so the query has to say. For spend, a member who bought
        nothing spent Rs 0. For a rating, a member who gave none has no rating, and an average that
        skips them is right. The habit is the same: decide what the missing value means, and write it.

        ## What did this chapter answer?

        1. **Nested subqueries, named steps or temporary tables?** Named steps, CTEs: one statement the
           analyst reads from the top and reruns anywhere; a temporary table disappeared in a new
           session.
        2. **How did each branch move?** In Retail-Plus, customers 0.835, orders per customer 0.780 and
           revenue per order 1.084, which multiply to 0.706: frequency fell furthest, 22.0 percent.
        3. **How much less did each Retail-Plus member spend?** Rs 5,474 then Rs 3,863 over the same 107
           members, down 29.4 percent; the average that skipped missing quarters said 15.5 percent.
        4. **Does the customer table's count agree?** Yes: Rs 4,881 then Rs 3,445 over the tier's 120
           members, down 29.4 percent, the same change.

        Chapter 5 adds the suite's numbers up the way Anand's analyst will.
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 5
def ch5():
    return [
        md("""
        # Do the suite's numbers add up the way Anand's analyst will add them?

        **Week 2, Monday. Chapter 5 of 6.** Chapters 1 to 4 built every number the Monday suite
        reports; this chapter adds them up the way an auditor does, before the auditor does.

        > "My analyst will add your rows before reading a single query. If they do not add up, the
        > suite does not reach me."
        > Anand Iyer, finance controller, Kalpa Retail

        **Who needs the answer.** Anand's analyst audits the Monday suite, and the first thing an
        auditor does is add: the segments against the book, the two quarters against the half-year. A
        half-year line that shows more Retail-Plus customers than the tier has members fails the audit
        on sight, and every other number in the suite is doubted with it. The head of Retail-Plus would
        read that every member was active and never see the members who bought nothing all half-year.

        **The questions on the way.**
        1. How should the suite produce its half-year column?
        2. Do the segments add back to the book in each quarter?
        3. How many Retail-Plus customers bought in the half-year?
        4. Does the overlap between the two quarters explain the gap?

        **The metric at stake.** Customers who bought in a window, each counted once, for each quarter
        and for the half-year, April to September 2026; and the tie-outs, the sums an auditor checks.
        Orders and booked revenue come along in every line.

        **What chapters 3 and 4 found.** Retail-Plus had 91 customers in Q1 and 76 in Q2, and its
        revenue fell 29.4 percent, from Rs 5,85,770 to Rs 4,13,380; its spend per member fell 29.4
        percent once both averages covered the same members. The tier holds 120 members on Kalpa's
        customer table.

        **A real company with the same question.** Meta reports its daily active people across
        Facebook, Instagram, Messenger and WhatsApp: 3.58 billion on average in December 2025. Its
        annual report defines a daily active person as a logged-in user "who visited at least one of
        these Family products" that day, and says it matches accounts to people, "counting such group
        of accounts as one person" (Meta Platforms, Form 10-K for 2025). A person who opens two of the
        apps is one person, and adding each app's daily users would count them twice.
        """),
        setup_note("05_does_it_add_up"),
        setup("05_does_it_add_up"),
        where(5, ["the options\nfour ways to a half-year column", "the segments\nadded back to the book",
                  "the half-year\ncustomers, added and counted", "a second route\nthe overlap"]),
        md("""
        ## The options: how should the suite produce its half-year column?

        Anand's sheet shows Q1, Q2 and the half-year for every segment. The quarter rows already exist,
        so there is more than one way to reach the half-year:

        | Option | What it reads | What it assumes | What the analyst audits |
        |---|---|---|---|
        | A. Add each segment's two quarter rows in a last step | The 8 quarter rows | That every measure adds across the quarters | One more step, a `sum` |
        | B. Count the half-year from the orders, like each quarter | All 1,000 order rows again | Nothing new: the same definition, a wider window | The same query as the quarters, without the quarter |
        | C. `GROUPING SETS`: one query returns the quarter rows and the half-year rows | All 1,000 order rows, once | Nothing new, and one more feature to read | One query, with a `NULL` quarter marking the half-year |
        | D. Report the quarters and no half-year | Nothing | That nobody wants the half-year | Nothing, until the analyst adds the two quarters by hand |

        **Predict before you run.** Option A reads 8 rows and option B reads 1,000. Why might a team
        still read the 1,000?

        - a) Because Postgres cannot add rows from a CTE.
        - b) So that every number in the half-year column comes from its own window, the way each
          quarter's does.
        - c) Because 1,000 rows are faster to read than 8.
        - d) Because option A cannot add rupees.
        """),
        code(r'''
            per_q = run("c5_per_quarter", "The suite's middle table: every segment and quarter", money=("revenue",))
            order_rows = kit.sql("SELECT count(*) AS n FROM orders")[0]["n"]
            kit.table(["option", "rows it reads for the half-year column"],
                      [("A. add the quarter rows", len(per_q)), ("B. count from the orders", f"{order_rows:,}"),
                       ("C. GROUPING SETS", f"{order_rows:,}, once for both columns"), ("D. no half-year", 0)],
                      caption="Sized on this warehouse")
            kit.bars([("A. add the quarter rows", len(per_q)), ("B. count from the orders", order_rows),
                      ("C. GROUPING SETS", order_rows)],
                     title="Rows read for the half-year column: A is the cheapest by a factor of 125", lit=(0,))
            '''),
        md("""
        **What happened.** The answer is b. Option A reads 8 rows where B reads 1,000, and on a book
        this size neither costs a noticeable second. What separates them is what each assumes. B counts
        the half-year from the orders with the same definition as each quarter, a wider window and
        nothing else, so the analyst audits one definition. A assumes that every measure in the quarter
        rows can be added.

        **The best-fit call.** Option B, the half-year counted from the orders. **What would change the
        call:** if Anand wants several windows at once, months and quarters and the half-year, option C
        returns them all from one query that reads the book once, and it is worth one more feature for
        the analyst to learn.
        """),
        code(r'''
            kit.check("the middle table has one row per segment and quarter", len(per_q) == 8)
            kit.check("option B reads every order", order_rows == 1000)
            '''),
        md("""
        ## 1. Do the segments add back to the book in each quarter?

        The first tie-out adds the four segment rows of each quarter and sets the sums beside the book's
        own totals from chapter 1.

        **Predict before you run.** Will the four segments' Q1 customers add up to the book's 244?

        - a) Yes, since each customer belongs to exactly one segment.
        - b) No, the segments add to more than 244.
        - c) No, the segments add to fewer than 244.
        - d) Only orders and rupees can be added, never customers.
        """),
        code(r'''
            tie = {r["quarter"]: {k: num(v) for k, v in r.items()}
                   for r in run("c5_tie_out_segments", "The first tie-out: segments added, beside the book",
                                money=("segments_revenue", "book_revenue"))}
            seg_q1 = [(r["segment"], int(r["customers"])) for r in per_q if r["quarter"] == "Q1"]
            kit.bridge(seg_q1[0], seg_q1[1:], end_label="the book's Q1 customers", fmt=lambda v: f"{v:,.0f}",
                       title="Each segment adds its own customers: the four land on the book's 244")
            '''),
        code(r'''
            for q in ("Q1", "Q2"):
                kit.check(f"{q}: the segments' orders, customers and rupees equal the book's",
                          (tie[q]["segments_orders"], tie[q]["segments_customers"], tie[q]["segments_revenue"]) ==
                          (tie[q]["book_orders"], tie[q]["book_customers"], tie[q]["book_revenue"]),
                          f"{tie[q]['segments_customers']} customers")
            '''),
        md("""
        **What happened.** The answer is a. In each quarter the four segments add back to the book on
        orders (538 and 462), on rupees (Rs 10,00,00,000 and Rs 9,84,00,000) and on customers (244 and
        227). Customers add across segments because a customer belongs to one segment, so no customer
        sits in two of the rows being added.

        ## 2. How many Retail-Plus customers bought in the half-year?

        A hurried analyst builds the half-year the cheap way, option A: the quarter rows are already in a
        step, so a last step sums each segment's two rows.

        **Predict before you run.** What does the half-year line say for Retail-Plus customers?

        - a) 91, the larger quarter.
        - b) 107.
        - c) 167.
        - d) 120, the tier.
        """),
        code(r'''
            added = {r["segment"]: {k: num(v) for k, v in r.items()}
                     for r in run("c5_half_year_hurried", "The half-year, the quickest way: two quarter rows added",
                                  money=("revenue",))}
            p = added["Retail-Plus"]
            kit.stats([(str(p["customers"]), "Retail-Plus customers", "the half-year line, added"),
                       (str(sum(r["customers"] for r in added.values())), "customers in the book", "the four segments, added"),
                       (kit.rupees(round(p["revenue"] / p["customers"])), "revenue per customer", "Retail-Plus half-year, on that count")],
                      caption="The hurried half-year line, as it would reach the analyst")
            '''),
        md("""
        **The plausible wrong answer.** 167 Retail-Plus customers bought in the half-year, and 471 across
        the book, so a Retail-Plus customer brought in Rs 5,983 over the six months. The orders (355)
        and the rupees (Rs 9,99,150) in the same line are right, which is what makes the customer count
        look right beside them.

        **Why it is wrong.** A customer who bought in both quarters sits in the Q1 row and in the Q2
        row, and adding the rows counts that customer twice. Orders and rupees add across quarters,
        because an order belongs to one quarter; customers add only across groups a customer cannot
        share, such as segments. The answer the query gave was c.

        **The check that exposes it.** A count of customers who bought can never exceed the customers
        who exist. Set the half-year line beside each segment's members on the customer table.
        """),
        code(r'''
            members = {r["segment"]: int(r["members_on_the_book"])
                       for r in run("c5_members", "Members per segment on the customer table")}
            segs = list(members)
            kit.columns(segs, [("half-year, added", [added[s]["customers"] for s in segs]),
                               ("members on the book", [members[s] for s in segs])],
                        title="The added half-year exceeds the members in every segment", lit=(2,))
            '''),
        code(r'''
            kit.check("the added count exceeds the members in every segment",
                      all(added[s]["customers"] > members[s] for s in segs),
                      ", ".join(f"{s} {added[s]['customers']} of {members[s]}" for s in segs))
            kit.check("Retail-Plus shows 167 customers from a tier of 120", (p["customers"], members["Retail-Plus"]) == (167, 120))
            kit.check("the added orders and rupees are right: they equal the book's two quarters",
                      sum(r["orders"] for r in added.values()) == 1000 and sum(r["revenue"] for r in added.values()) == 198400000)
            '''),
        md("""
        **The fix, and what it changed.** Count the half-year's customers from the orders, each counted
        once, with the same definition as each quarter and a wider window: option B.
        """),
        code(r'''
            half = {r["segment"]: {k: num(v) for k, v in r.items()}
                    for r in run("c5_half_year", "The fix: the half-year counted from the orders", money=("revenue",))}
            kit.table(["segment", "added", "counted", "counted twice", "members on the book"],
                      [(s, added[s]["customers"], half[s]["customers"], added[s]["customers"] - half[s]["customers"], members[s])
                       for s in segs], caption="What the fix changed, segment by segment")
            hp = half["Retail-Plus"]
            print(f"Retail-Plus revenue per customer over the half-year: {kit.rupees(round(hp['revenue'] / hp['customers']))}, "
                  f"not {kit.rupees(round(p['revenue'] / p['customers']))}")
            '''),
        code(r'''
            kit.check("107 Retail-Plus customers bought in the half-year", hp["customers"] == 107)
            kit.check("the book's half-year holds 301 customers, as chapter 1 counted",
                      sum(h["customers"] for h in half.values()) == 301)
            kit.check("every counted half-year fits inside its members", all(half[s]["customers"] <= members[s] for s in segs))
            '''),
        md("""
        **What happened.** Retail-Plus had 107 customers in the half-year, not 167: 60 customers were
        counted twice. The book had 301, not 471, the same 301 that chapter 1 counted over both quarters.
        Revenue per Retail-Plus customer over the half-year is Rs 9,338, not Rs 5,983. And 13 of the
        tier's 120 members bought nothing in either quarter, which the added line could never have
        shown.

        ## A second route: does the overlap between the two quarters explain the gap?

        The fix counted the half-year directly. The second route builds it from the quarters and the
        overlap: customers in Q1, plus customers in Q2, less the customers who bought in both, since
        those are the ones counted twice. The overlap comes from one row per customer with the number
        of quarters that customer bought in.

        **Predict before you run.** How many Retail-Plus customers bought in both quarters?

        - a) 16.
        - b) 31.
        - c) 60.
        - d) 76.
        """),
        code(r'''
            both = {r["segment"]: int(r["bought_in_both"]) for r in run("c5_overlap", "Customers who bought in both quarters")}
            q = {(r["segment"], r["quarter"]): int(r["customers"]) for r in per_q}
            route2 = {s: q[(s, "Q1")] + q[(s, "Q2")] - both[s] for s in segs}
            kit.bridge((f"Q1 + Q2, added", q[("Retail-Plus", "Q1")] + q[("Retail-Plus", "Q2")]),
                       [("bought in both, counted twice", -both["Retail-Plus"])], end_label="the half-year",
                       fmt=lambda v: f"{v:,.0f}", lit=(0,),
                       title="Retail-Plus: 91 + 76 less the 60 counted twice lands on 107")
            kit.table(["segment", "Q1 + Q2 - both", "counted directly"],
                      [(s, f"{q[(s, 'Q1')]} + {q[(s, 'Q2')]} - {both[s]} = {route2[s]}", half[s]["customers"]) for s in segs],
                      caption="The second route, every segment")
            '''),
        code(r'''
            kit.check("the second route matches the direct count in every segment",
                      all(route2[s] == half[s]["customers"] for s in segs))
            kit.check("the customers counted twice are exactly the ones who bought in both quarters",
                      all(added[s]["customers"] - half[s]["customers"] == both[s] for s in segs))
            '''),
        md("""
        **What happened.** The answer is c: 60 Retail-Plus customers bought in both quarters, and 91 plus
        76 less 60 is 107, the direct count. In every segment the customers counted twice are exactly
        the customers who bought in both quarters, which is why the added line ran over.

        > **Kavya's review.** Before you add a column, ask whether one customer can sit in two of its
        > rows. Orders and rupees add. People add only across groups they cannot share, so a
        > half-year of customers is counted from the orders, never added from the quarters.

        ### In the interview: what may you add, and what must an auditable query carry?

        **[F] Why can you not add two quarters' customer counts to get the half-year's?** Because a
        count of distinct customers is taken inside its own window, and a customer who bought in both
        windows is in both counts. The half-year's customers equal Q1's plus Q2's less the customers in
        both: for Retail-Plus 91 plus 76 less 60, which is 107, not 167. The same holds for daily users
        added into a month. Orders and revenue add, because each order sits in one window.

        **[D] A stakeholder's analyst must audit your query; what changes in how you write it, and what
        would you refuse to compute in a notebook?** Each number gets a named step and a comment that
        states its question and its definition, divisions are done in `numeric` and rounded on purpose,
        every list is ordered on a unique key, and the suite carries its own tie-outs: segments against
        the book, windows counted from the orders. The reported number is never computed on an export in
        a notebook, because the analyst cannot rerun it on the book.

        ### Depth: can one query return the quarters and the half-year together?

        `GROUP BY GROUPING SETS ((c.segment, o.quarter), (c.segment))` groups the orders twice in one
        pass: once by segment and quarter, once by segment alone. Each count is taken from the orders
        in its own set, so the half-year rows are counted, never added. A `NULL` in the quarter column
        stands for the half-year row.
        """),
        code(r'''
            sets = run("c5_grouping_sets", "Quarters and half-year from one query", money=("revenue",))
            half_rows = {r["segment"]: int(r["customers"]) for r in sets if r["quarter"] is None}
            kit.check("the half-year rows from GROUPING SETS match the direct count",
                      all(half_rows[s] == half[s]["customers"] for s in segs))
            '''),
        md("""
        ## What did this chapter answer?

        1. **How should the suite produce its half-year column?** Counted from the orders with the
           quarters' own definition, option B; `GROUPING SETS` returns every window in one query when
           Anand wants several.
        2. **Do the segments add back to the book?** Yes, on orders, rupees and customers in each
           quarter: 538 orders, Rs 10,00,00,000 and 244 customers in Q1, because a customer belongs to
           one segment.
        3. **How many Retail-Plus customers bought in the half-year?** 107, not the 167 that adding the
           quarters gives; the tier holds 120 members, and the book 301 customers, not 471.
        4. **Does the overlap explain the gap?** Yes: 60 Retail-Plus customers bought in both quarters,
           and 91 plus 76 less 60 is 107; in every segment the double count equals the overlap.

        Chapter 6 asks whether next Monday's run will give the analyst the same answers from the same
        book.
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 6
def ch6():
    return [
        md("""
        # Will next Monday's run give Anand's analyst the same answer from the same book?

        **Week 2, Monday. Chapter 6 of 6.** Chapters 1 to 5 built the Monday suite and made it add up;
        this chapter makes it repeat.

        > "Every Monday I rerun your suite and trace five delivered app orders against the ERP. If my
        > rerun differs from yours, I need to know whether the book changed or your query did."
        > Anand's analyst, finance, Kalpa Retail

        **Who needs the answer.** Anand's analyst reruns the suite every Monday and checks a sample of
        orders against the ERP, the system Finance books orders in. A rerun that disagrees with the
        team's run on a sample that should be identical, even by a few hundred rupees, makes every
        number in the suite suspect, because nobody can say whether the book moved or the query did.

        **The questions on the way.**
        1. How can a run show that it computed the same thing as last week's?
        2. What fingerprint does this Monday's run leave?
        3. Which five orders will the analyst trace against the ERP?
        4. Does a sort in Python pick the same five?
        5. What does the Monday suite tell Anand?

        **The metric at stake.** The run itself: the book's fingerprint (row counts, rupees and distinct
        customers per table) printed beside the numbers, and the audit sample of five delivered Q2 app
        orders. Q2 is July to September 2026.

        **What chapters 1 to 5 found.** The book fell 1.6 percent, Rs 10,00,00,000 to Rs 9,84,00,000,
        with 244 then 227 customers who bought. Retail-Plus lost 29.4 percent of its revenue, with
        customers down 16.5 percent and orders per customer down 22.0 percent. The segments add back to
        the book, and the half-year counts each customer once: 301 in the book, 107 in Retail-Plus.

        **A real company with the same question.** Netflix's data engineering team described a pattern
        it called write, audit, publish: each run's new data is written first to an audit table,
        checked against the runs before it on measures such as its row count and its count of missing
        values, and published only when the checks set to fail the job pass, while a check set to warn
        raises an alert (Michelle Ufford, "Whoops, The Numbers Are Wrong! Scaling Data Quality @
        Netflix", DataWorks Summit, San Jose, 13 June 2017). A number that is published every week
        checks itself against last week before anyone reads it.
        """),
        setup_note("06_same_answer"),
        setup("06_same_answer"),
        where(6, ["the options\nfour ways a run proves itself", "the fingerprint\nwhat the book holds",
                  "the sample\nfive orders to trace", "a second route\nPython's own sort",
                  "the sentence\nwhat Anand hears"]),
        md("""
        ## The options: how can a run show that it computed the same thing as last week's?

        Next Monday the analyst reruns the suite. Four ways a team could make a difference between the
        two runs explain itself:

        | Option | Stored with each run | Access it needs | What it can tell apart |
        |---|---|---|---|
        | A. Rerun and compare by eye | Nothing | Read | Whatever someone happens to notice |
        | B. A fingerprint block that runs with the suite: rows, rupees and distinct customers per table, printed beside the numbers | A handful of numbers, kept with the run's output | Read | A changed book from a changed query |
        | C. Snapshot each Monday's outputs into a table | Every output row | Write, to a schema the team owns | What changed in any output, row by row |
        | D. Write, audit, publish: compute into a hidden table, check it, then release it | A staging table per run | Write, and a scheduler | A bad run, stopped before anyone reads it |

        **Predict before you run.** Option B's fingerprint for the two tables the suite reads: how many
        numbers does it store?

        - a) 2, one row count per table.
        - b) About 8: four numbers for each of the two tables.
        - c) About 20, one per output row.
        - d) 1,340, one per row read.
        """),
        code(r'''
            fp = run("c6_fingerprint", "The book's fingerprint", money=("rupees",))
            numbers = sum(1 for r in fp for k, v in r.items() if k != "table_name" and v is not None)
            outputs = 8 + 4 + 4 + 2
            kit.table(["option", "numbers stored per run", "access"],
                      [("A. by eye", 0, "read"), ("B. fingerprint", numbers, "read"),
                       ("C. snapshot", f"about {outputs} rows", "write"), ("D. write, audit, publish", "a staging table", "write and a scheduler")],
                      caption="Sized on this suite: its outputs are about 18 rows a Monday")
            kit.flow(["the fingerprint\nwhat the book holds", "the suite\nevery number", "the sample\nfive ordered orders",
                      "next Monday\nfingerprints compared"], kinds=["lit", None, None, "good"],
                     title="Option B: the run carries the book's fingerprint beside its numbers")
            '''),
        md("""
        **What happened.** The answer is b: seven numbers, four for `orders` and three for `customers`,
        whose rupee column is empty. They are cheap to keep and they answer the analyst's first
        question: if next Monday's fingerprint matches this one, the book has not changed, so any
        difference in the numbers is the query's.

        **The best-fit call.** Option B, a fingerprint block at the top of the suite, together with an
        `ORDER BY` on a unique column in every list. The team has read access, which rules out C and D,
        and B tells a changed book from a changed query, which is the analyst's question. **What would
        change the call:** once the platform lead grants a schema the team can write to, option D runs
        the audit before the numbers are released, which is better than finding the problem after
        Anand has read them.
        """),
        code(r'''
            orders_fp = next(r for r in fp if r["table_name"] == "orders")
            kit.check("the fingerprint stores seven numbers", numbers == 7)
            kit.check("the orders fingerprint matches the book the suite reports",
                      (orders_fp["rows"], num(orders_fp["rupees"]), orders_fp["distinct_customers"]) == (1000, 198400000, 301))
            '''),
        md("""
        ## 1. What fingerprint does this Monday's run leave?

        The fingerprint reads each table once: its rows, its rupees, its distinct customers and its
        latest date. Printed at the top of each Monday's run, it is the first thing the analyst compares.

        **Predict before you run.** Overnight the warehouse reloads, and two order rows are rewritten
        with the values they already hold. Does the fingerprint change?

        - a) Yes: two rows were written, so the row count moves.
        - b) Yes: the rupees move, since the rows were rewritten.
        - c) No: the rows, the rupees and the customers are all the same.
        - d) It cannot be read during a reload.
        """),
        code(r'''
            conn = kit.connect()
            try:
                steps = statements(Q["c6_sample_after_reload"])
                update = next(s for s in steps if s.upper().startswith("UPDATE"))
                kit.sql(update, conn=conn)
                fp_after = kit.sql(Q["c6_fingerprint"], conn=conn)
            finally:
                conn.rollback()
                conn.close()
            before = {r["table_name"]: (r["rows"], num(r["rupees"]), r["distinct_customers"]) for r in fp}
            after = {r["table_name"]: (r["rows"], num(r["rupees"]), r["distinct_customers"]) for r in fp_after}
            kit.table(["table", "this Monday", "after the reload"],
                      [(t, f"{before[t][0]:,} rows, {kit.rupees(before[t][1]) if before[t][1] else 'no rupees'}, {before[t][2]} customers",
                        f"{after[t][0]:,} rows, {kit.rupees(after[t][1]) if after[t][1] else 'no rupees'}, {after[t][2]} customers")
                       for t in before], caption="The fingerprint before and after the reload")
            kit.columns(["rows", "customers"], [("this Monday", [before["orders"][0], before["orders"][2]]),
                                                ("after the reload", [after["orders"][0], after["orders"][2]])],
                        title="The orders fingerprint does not move: the book is the same book")
            '''),
        code(r'''
            kit.check("the reload leaves the fingerprint unchanged", before == after)
            kit.check("the warehouse is back as it was after the rollback",
                      kit.sql("SELECT count(*) AS n, sum(amount) AS s FROM orders")[0]["n"] == 1000)
            '''),
        md("""
        **What happened.** The answer is c. The reload rewrote two rows with their own values, so the
        book holds the same 1,000 orders, the same Rs 19,84,00,000 and the same 301 customers. Whatever
        differs between the two runs after this reload cannot be the book.

        ## 2. Which five orders will the analyst trace against the ERP?

        The analyst traces five delivered Q2 app orders. The quickest query asks for five:

        ```sql
        SELECT order_id, amount FROM orders
        WHERE quarter = 'Q2' AND channel = 'app' AND status = 'delivered'
        LIMIT 5;
        ```

        **Predict before you run.** With no `ORDER BY`, which five rows come back?

        - a) The five with the smallest order ids.
        - b) The five most recent orders.
        - c) Whichever five the database reaches first, which can change between runs.
        - d) Five chosen at random on every run.
        """),
        code(r'''
            first = run("c6_sample_hurried", "Your five, on Monday", money=("amount",))
            conn = kit.connect()
            try:
                kit.sql(update, conn=conn)
                select = next(s for s in statements(Q["c6_sample_after_reload"]) if s.upper().startswith("SELECT"))
                second = kit.sql(select, conn=conn)
            finally:
                conn.rollback()
                conn.close()
            show(second, "The analyst's five, the same query after the overnight reload", money=("amount",))
            t1, t2 = sum(num(r["amount"]) for r in first), sum(num(r["amount"]) for r in second)
            kit.bars([("your sample, Monday", t1), ("the analyst's rerun", t2)], fmt=kit.rupees,
                     title="The same query on the same book: two audit totals")
            '''),
        md("""
        **The plausible wrong answer.** Your five orders total Rs 3,900 and the analyst's rerun totals
        Rs 4,590. The audit reports a Rs 690 disagreement on a sample that should have been identical,
        and with it every other number in the suite comes under question.

        **Why it is wrong.** A table has no order. Without `ORDER BY` the rows come back "in an
        unspecified order", which "will depend on the scan and join plan types and the order on disk,
        but it must not be relied on" (PostgreSQL 16 documentation, sorting rows), so `LIMIT` returns
        "an unpredictable subset of the query's rows" (the same documentation, `LIMIT` and `OFFSET`).
        Postgres writes a rewritten row as a new version in a new place, so after the reload the first
        five rows the database reaches are a different five. The answer is c.

        **The check that exposes it.** The fingerprint said the book did not change; the samples say the
        five did.
        """),
        code(r'''
            ids1, ids2 = [r["order_id"] for r in first], [r["order_id"] for r in second]
            kit.flow(["LIMIT 5\nno ORDER BY", "rows in the order\nthe disk holds them", "a reload moves\ntwo rows",
                      "a different five\nRs 690 apart"], kinds=[None, None, None, "bad"],
                     title="Why an unordered sample drifts while the book stands still")
            kit.check("the book did not change", before == after)
            kit.check("the unordered sample changed", ids1 != ids2, f"{len(set(ids1) - set(ids2))} of 5 orders differ")
            '''),
        md("""
        **The fix, and what it changed.** Order by a column no two rows share, then limit. `order_id` is
        the table's key, so `ORDER BY order_id LIMIT 5` names the same five orders on every run.
        """),
        code(r'''
            fixed = run("c6_sample", "The fix, on Monday", money=("amount",))
            conn = kit.connect()
            try:
                steps = statements(Q["c6_sample_after_reload_fixed"])
                kit.sql(next(s for s in steps if s.upper().startswith("UPDATE")), conn=conn)
                fixed_after = kit.sql(next(s for s in steps if s.upper().startswith("SELECT")), conn=conn)
            finally:
                conn.rollback()
                conn.close()
            show(fixed_after, "The fix, after the same reload", money=("amount",))
            kit.check("the ordered sample is the same five after the reload",
                      [r["order_id"] for r in fixed] == [r["order_id"] for r in fixed_after])
            kit.check("the ordered sample totals Rs 3,900", sum(num(r["amount"]) for r in fixed) == 3900)
            '''),
        md("""
        **What happened.** Ordered by `order_id`, the five are KR-00542, KR-00544, KR-00545, KR-00546
        and KR-00547 before and after the reload, Rs 3,900 both times. The analyst now traces the orders
        you traced.

        ## A second route: does a sort in Python pick the same five?

        The first route asked the database to sort and cut. The second route asks it for every
        delivered Q2 app order, in whatever order it reaches them, and sorts them in Python before
        taking five. If the fixed query is right, both routes name the same orders.

        **Predict before you run.** How many candidate orders does Python sort before it takes five?

        - a) 5.
        - b) About 20.
        - c) About 100.
        - d) All 1,000 orders.
        """),
        code(r'''
            candidates = kit.sql(Q["c6_candidates"])
            python_five = sorted(candidates, key=lambda r: r["order_id"])[:5]
            kit.table(["the database's ORDER BY", "Python's sorted()"],
                      [(a["order_id"], b["order_id"]) for a, b in zip(fixed, python_five)],
                      caption=f"Two routes to the audit sample, from {len(candidates)} candidates")
            small = [num(r["amount"]) for r in candidates if num(r["amount"]) < 5000]
            kit.strip(small, markers=[("the five, Rs 3,900 in all", 780, "good")], fmt=kit.rupees, lo=0, hi=5000,
                      lit=tuple(i for i, r in enumerate(r for r in candidates if num(r["amount"]) < 5000)
                                if r["order_id"] in {f["order_id"] for f in fixed}),
                      title="The consumer-sized candidates, one dot each; the five sampled are drawn dark")
            print(f"{len(candidates)} candidates, {len(small)} of them under Rs 5,000")
            '''),
        code(r'''
            kit.check("Python's five are the database's five",
                      [r["order_id"] for r in python_five] == [r["order_id"] for r in fixed])
            kit.check("Python's five total the same Rs 3,900", sum(num(r["amount"]) for r in python_five) == 3900)
            '''),
        md("""
        **What happened.** The answer is c: Python sorted 94 delivered Q2 app orders and took the same
        five, Rs 3,900. The dots are the 80 candidates under Rs 5,000, with the sampled five drawn dark
        and the marker at their average, Rs 780; the other 14 are Business orders worth lakhs, off this
        scale.

        ## 3. What does the Monday suite tell Anand?

        The day's answer is one message, with its evidence and its caveat, that Anand can forward
        without rewriting.
        """),
        code(r'''
            kit.vflow(["the book\nRs 10.00 crore to Rs 9.84 crore, down 1.6%",
                       "the segment\nRetail-Plus down 29.4%, 75 of the 76 fewer orders",
                       "the branches\ncustomers down 16.5%, orders each down 22.0%",
                       "the audit\nsegments add up; each customer counted once",
                       "the run\nthe fingerprint printed; every list ordered"],
                      kinds=["lit", None, "bad", "good", "good"],
                      title="The Monday suite, from the book to the run")
            kit.table(["what Anand asked", "what the suite now does"],
                      [("computed from the warehouse itself", "every number is a named query on the book"),
                       ("every segment", "one grouped query, ratios in numeric, thin groups flagged"),
                       ("nothing a person can mistype", "no export, no copied value; the run checks its own sums"),
                       ("an analyst who audits every line", "a comment on every step, and a fingerprint beside every run")],
                      caption="The ask, answered line by line")
            '''),
        md("""
        **The sentence to Anand.** "Anand, the Monday suite now runs on the warehouse itself. Booked
        revenue fell 1.6 percent, from Rs 10.00 crore to Rs 9.84 crore, and Retail-Plus carries the fall
        in orders: its revenue is down 29.4 percent because 16.5 percent fewer members bought and each
        ordered 22.0 percent less often. Every count says what it counts, every ratio multiplies back,
        and each run prints the book's fingerprint, so a rerun on the same book gives the same answer.
        One caveat: last week's extract showed customers flat, and the full book shows 7.0 percent fewer
        customers in Q2."

        > **Kavya's review.** A run that cannot be repeated cannot be audited. Order every list on a
        > column no two rows share, and print the book's fingerprint beside the numbers, so a difference
        > next Monday says whether the book moved or the query did.

        ### In the interview: what does LIMIT without ORDER BY return, and what do you suspect when a number moves overnight?

        **[F] What does LIMIT without ORDER BY return?** Whichever rows the database reaches first, which
        depends on the plan and on where rows sit on disk, so it can change between runs with no change
        to the data. Postgres documents it as an unpredictable subset. Order by a column, or a set of
        columns, that no two rows share, and then limit.

        **[F] Your KPI moved 30 percent overnight and the data did not change; what do you suspect?**
        The query. Check the book's fingerprint first: if the rows and rupees are the same, look for an
        unordered `LIMIT`, a definition that changed between runs, a denominator that shifted (a count of
        rows where people were meant, an average that skips missing values), or integer division.

        ### Depth: what does Netflix's audit check, and what would Kalpa's add?

        In the Netflix talk the audit step sets each new batch beside the runs before it. One slide
        puts a new batch of 17,240 rows with 17,240 missing values beside the previous day's 16,135
        rows with 21: every value of the column was missing. In the talk's rules the row-count checks
        fail the job, while the missing-value check only warns, and its walk-through flags that batch
        with a warning. A fingerprint that stores the count of missing amounts and customer ids beside
        the rows and rupees would put the same failure in front of the team at Kalpa before Anand read
        a number built on it. Kalpa's warehouse holds no missing value in any column today, which is
        exactly what the fingerprint would prove each Monday.

        ## What did this chapter answer?

        1. **How can a run show it computed the same thing?** A fingerprint block that runs with the
           suite and prints seven numbers about the book, with an `ORDER BY` on a unique column in every
           list; write, audit, publish once the team can write to a schema.
        2. **What fingerprint does this run leave?** 1,000 orders, Rs 19,84,00,000 and 301 customers in
           `orders`, and 340 rows in `customers`; the overnight reload left it unchanged.
        3. **Which five orders will the analyst trace?** KR-00542, KR-00544, KR-00545, KR-00546 and
           KR-00547, Rs 3,900, once the query orders by `order_id`; without it the rerun drew a
           different five worth Rs 4,590.
        4. **Does Python's sort agree?** Yes: sorting the 94 candidates in Python gives the same five.
        5. **What does the suite tell Anand?** The book fell 1.6 percent; Retail-Plus carries the fall
           in orders, down 29.4 percent on fewer members buying and each buying less often; and every
           number now reruns the same on the same book.

        Tomorrow Anand asks the next question: how much of what was booked was actually collected.
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- the escalated case
CASE_SETUP = WAREHOUSE + r'''
def rows(query):
    """Run a query and hand back its rows with every number as a Python number."""
    return [{k: num(v) for k, v in r.items()} for r in kit.sql(query)]
print("connected:", kit.sql("select version()")[0]["version"].split(",")[0])
'''


def case():
    """The escalated case: the Monday suite on Anand's definition, delivered orders only."""
    cells = [
        md("""
        # Does the Monday suite hold on Anand's definition, the orders that were delivered?

        **Week 2, Monday. The escalated case, alone, in five parts.** Parts 1 and 2 run in the
        afternoon session; parts 3 to 5 run in the practice lab.

        > "Finance counts the orders that reached the customer and stayed there. Run me the same suite
        > on delivered orders, and tell me whether the story changes."
        > Anand Iyer, finance controller, Kalpa Retail

        **The situation.** The chapters built the Monday suite on booked revenue, every order at its
        amount whatever its status: Rs 10,00,00,000 in Q1 (April to June 2026) and Rs 9,84,00,000 in Q2
        (July to September 2026), 244 then 227 customers who bought, and Retail-Plus carrying the fall
        with its revenue down 29.4 percent. Finance counts only delivered orders; cancelled and
        returned orders are not revenue on Anand's books. This notebook reruns the suite on that
        definition. Its numbers are new, so nothing from the chapters can be copied.

        **The data.** The Kalpa warehouse, as in the chapters: `orders` (1,000 rows: order id, customer
        id, date, quarter, channel, amount, status) and `customers` (340 rows, one per member, with the
        segment). The segment is looked up with `JOIN customers c USING (customer_id)`.
        """),
        md("""
        TODO ONLY
        **How to answer.** Each step holds one or more `TODO` markers. Each marker is a choice, lettered
        a to d, written as a comment above a placeholder whose name starts with `__TODO` and ends in the
        marker's number. Replace the placeholder with the letter in quotes, for example `"a"`, and run
        the step; the check after it tells you whether the step behaves. Running the notebook before you
        fill a marker stops at that marker with a `NameError`, which is expected. Post your ten letters
        in order when you finish.
        """),
        md("""
        SOLUTION ONLY
        **This is the solution.** Every marker is filled with its key and the notebook runs clean from the
        top; the reasons for each key are at the end.
        """),
        code(CASE_SETUP),
        code(r'''
            kit.side_by_side(
                kit.ladder(["The book on delivered orders", "Each segment's frequency", "The branches and spend per member",
                            "The tie-outs", "The run that repeats"], lit=0, show=False),
                kit.flow(["booked: every status", "delivered: Anand's books"], kinds=["plain", "lit"], show=False),
            )
            '''),
        md("""
        ## Part 1. What does the book say on Anand's definition?

        Where this is used at work: every finance number starts from a definition of revenue, and the
        filter that states it is the first line an auditor reads.
        """),
        code(r'''
            # TODO 1. Which filter keeps Anand's definition, the orders that reached the customer and stayed?
            #   a) WHERE status <> 'cancelled'
            #   b) WHERE status IN ('delivered', 'returned')
            #   c) HAVING status = 'delivered'
            #   d) WHERE status = 'delivered'
            FILTER = {"a": "WHERE status <> 'cancelled'", "b": "WHERE status IN ('delivered', 'returned')",
                      "c": "HAVING status = 'delivered'", "d": "WHERE status = 'delivered'"}[__TODO1__]

            # TODO 2. Which expression counts the customers who took delivery, each once?
            #   a) count(DISTINCT customer_id)
            #   b) count(*)
            #   c) count(customer_id)
            #   d) sum(1)
            CUSTOMERS = {"a": "count(DISTINCT customer_id)", "b": "count(*)", "c": "count(customer_id)",
                         "d": "sum(1)"}[__TODO2__]

            book_sql = f"""SELECT quarter, count(*) AS orders, {CUSTOMERS} AS customers, sum(amount) AS revenue
            FROM orders {FILTER} GROUP BY quarter ORDER BY quarter"""
            print(book_sql)
            book = {r["quarter"]: r for r in rows(book_sql)}
            kit.columns(["orders", "customers"], [(q, [book[q]["orders"], book[q]["customers"]]) for q in ("Q1", "Q2")],
                        title="The delivered book, per quarter")
            '''),
        code(r'''
            leftover = rows(f"SELECT count(*) AS n FROM orders {FILTER} AND status <> 'delivered'")[0]["n"]
            kit.check("the filter keeps no order that was cancelled or returned", leftover == 0, f"{leftover} left in")
            kit.check("customers are fewer than orders in each quarter",
                      all(book[q]["customers"] < book[q]["orders"] for q in ("Q1", "Q2")))
            kit.check("no quarter shows more customers than the 340 on the book",
                      all(book[q]["customers"] <= 340 for q in ("Q1", "Q2")))
            print(f"Revenue {kit.rupees(book['Q1']['revenue'])} to {kit.rupees(book['Q2']['revenue'])}, "
                  f"{pct(book['Q1']['revenue'], book['Q2']['revenue']):+.1f}%; customers {book['Q1']['customers']} "
                  f"to {book['Q2']['customers']}, {pct(book['Q1']['customers'], book['Q2']['customers']):+.1f}%")
            '''),
        md("""
        ## Part 2. Which segment's frequency fell on delivered orders, and which groups are too thin?

        Where this is used at work: a per-segment rate is the line a business head reads first, and a
        rate on too few customers is the line that misleads them most.
        """),
        code(r'''
            # TODO 3. Which grouping gives one row per segment and quarter?
            #   a) GROUP BY o.quarter
            #   b) GROUP BY c.segment
            #   c) GROUP BY c.segment, o.quarter
            #   d) GROUP BY o.customer_id
            GROUPING = {"a": "GROUP BY o.quarter", "b": "GROUP BY c.segment", "c": "GROUP BY c.segment, o.quarter",
                        "d": "GROUP BY o.customer_id"}[__TODO3__]

            # TODO 4. Which expression gives orders per customer that multiplies back to the orders?
            #   a) round(count(*) / count(DISTINCT o.customer_id), 2)
            #   b) round(count(*)::numeric / count(DISTINCT o.customer_id), 2)
            #   c) count(*) / count(DISTINCT o.customer_id)
            #   d) round(count(DISTINCT o.customer_id)::numeric / count(*), 2)
            RATIO = {"a": "round(count(*) / count(DISTINCT o.customer_id), 2)",
                     "b": "round(count(*)::numeric / count(DISTINCT o.customer_id), 2)",
                     "c": "count(*) / count(DISTINCT o.customer_id)",
                     "d": "round(count(DISTINCT o.customer_id)::numeric / count(*), 2)"}[__TODO4__]

            seg_sql = f"""SELECT c.segment, o.quarter, count(*) AS orders, count(DISTINCT o.customer_id) AS customers,
                   {RATIO} AS orders_per_customer
            FROM orders o JOIN customers c USING (customer_id) {FILTER} {GROUPING} ORDER BY 1, 2"""
            print(seg_sql)
            seg = rows(seg_sql)
            show(seg, "Each segment on delivered orders")
            '''),
        code(r'''
            kit.check("eight rows, one per segment and quarter", len(seg) == 8, f"{len(seg)} rows")
            kit.check("every ratio multiplies back to its orders within half an order",
                      all(abs(float(r["orders_per_customer"]) * r["customers"] - r["orders"]) < 0.5 for r in seg))
            by = {(r["segment"], r["quarter"]): r for r in seg}
            kit.columns(sorted({r["segment"] for r in seg}),
                        [(q, [float(by[(s, q)]["orders_per_customer"]) for s in sorted({r["segment"] for r in seg})])
                         for q in ("Q1", "Q2")], title="Orders per customer on delivered orders", fmt=lambda v: f"{v:.2f}")
            '''),
        code(r'''
            # TODO 5. Which clause keeps only the segment-quarters with fewer than 30 customers?
            #   a) WHERE count(DISTINCT o.customer_id) < 30
            #   b) HAVING count(*) < 30
            #   c) WHERE o.customer_id < 30
            #   d) HAVING count(DISTINCT o.customer_id) < 30
            THIN = {"a": "WHERE count(DISTINCT o.customer_id) < 30", "b": "HAVING count(*) < 30",
                    "c": "WHERE o.customer_id < 30", "d": "HAVING count(DISTINCT o.customer_id) < 30"}[__TODO5__]
            thin_sql = f"""SELECT c.segment, o.quarter, count(DISTINCT o.customer_id) AS customers
            FROM orders o JOIN customers c USING (customer_id) {FILTER} GROUP BY c.segment, o.quarter {THIN} ORDER BY 1, 2"""
            thin = rows(thin_sql)
            show(thin, "The segment-quarters to flag")
            flagged = {(r["segment"], r["quarter"]) for r in thin}
            kit.check("every flagged group has fewer than 30 customers", all(by[k]["customers"] < 30 for k in flagged))
            kit.check("every group with fewer than 30 customers is flagged",
                      all(k in flagged for k, r in by.items() if r["customers"] < 30))
            '''),
        md("""
        ## Part 3. Which branch of Retail-Plus's tree moved furthest, and how much less did each member spend?

        Where this is used at work: a head of a customer tier asks what each member is worth now, and
        the answer has to count the members who stopped.
        """),
        code(r'''
            branches = rows(f"""
            WITH book AS (
                SELECT o.customer_id, o.quarter, o.amount, c.segment
                FROM orders o JOIN customers c USING (customer_id) {FILTER}),
            q1 AS (SELECT segment, count(DISTINCT customer_id) AS customers, count(*) AS orders, sum(amount) AS revenue
                   FROM book WHERE quarter = 'Q1' GROUP BY segment),
            q2 AS (SELECT segment, count(DISTINCT customer_id) AS customers, count(*) AS orders, sum(amount) AS revenue
                   FROM book WHERE quarter = 'Q2' GROUP BY segment)
            SELECT segment,
                   round(q2.customers::numeric / q1.customers, 3) AS customers_ratio,
                   round((q2.orders::numeric / q2.customers) / (q1.orders::numeric / q1.customers), 3) AS frequency_ratio,
                   round((q2.revenue / q2.orders) / (q1.revenue / q1.orders), 3) AS order_value_ratio,
                   round(q2.revenue / q1.revenue, 3) AS revenue_ratio
            FROM q1 JOIN q2 USING (segment) ORDER BY segment""")
            show(branches, "Each branch, Q2 over Q1, on delivered orders")
            plus = next(r for r in branches if r["segment"] == "Retail-Plus")
            kit.bars([("customers", plus["customers_ratio"]), ("orders per customer", plus["frequency_ratio"]),
                      ("revenue per order", plus["order_value_ratio"])], fmt=lambda v: f"{v:.3f}",
                     title="Retail-Plus on delivered orders: each branch as Q2 over Q1")
            kit.check("the branches multiply back to the revenue ratio in every segment",
                      all(abs(r["customers_ratio"] * r["frequency_ratio"] * r["order_value_ratio"] - r["revenue_ratio"]) < 0.002
                          for r in branches))
            '''),
        code(r'''
            # TODO 6. Which expression gives the average member's Q2 spend over the same members as Q1's?
            #   a) avg(coalesce(q2_spend, 0))
            #   b) avg(q2_spend)
            #   c) sum(q2_spend) / count(q2_spend)
            #   d) max(q2_spend)
            SPEND = {"a": "avg(coalesce({col}, 0))", "b": "avg({col})", "c": "sum({col}) / count({col})",
                     "d": "max({col})"}[__TODO6__]

            # TODO 7. Which pair of counts shows who is inside each quarter's average?
            #   a) sum(q1_spend) and sum(q2_spend)
            #   b) count(DISTINCT q1_spend) and count(DISTINCT q2_spend)
            #   c) count(q1_spend) and count(q2_spend), beside count(*)
            #   d) avg(q1_spend) and avg(q2_spend)
            WHO = {"a": "sum(q1_spend) AS inside_q1, sum(q2_spend) AS inside_q2",
                   "b": "count(DISTINCT q1_spend) AS inside_q1, count(DISTINCT q2_spend) AS inside_q2",
                   "c": "count(q1_spend) AS inside_q1, count(q2_spend) AS inside_q2",
                   "d": "avg(q1_spend) AS inside_q1, avg(q2_spend) AS inside_q2"}[__TODO7__]

            spend_sql = f"""WITH member_spend AS (
                SELECT o.customer_id,
                       sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END) AS q1_spend,
                       sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END) AS q2_spend
                FROM orders o JOIN customers c USING (customer_id)
                {FILTER} AND c.segment = 'Retail-Plus'
                GROUP BY o.customer_id)
            SELECT count(*) AS members, {WHO},
                   round({SPEND.format(col='q1_spend')}) AS q1_average, round({SPEND.format(col='q2_spend')}) AS q2_average
            FROM member_spend"""
            print(spend_sql)
            spend = rows(spend_sql)[0]
            show([spend], "Retail-Plus spend per member on delivered orders", money=("q1_average", "q2_average"))
            '''),
        code(r'''
            tier = rows(f"""SELECT o.quarter, sum(o.amount) AS revenue FROM orders o JOIN customers c USING (customer_id)
                           {FILTER} AND c.segment = 'Retail-Plus' GROUP BY o.quarter ORDER BY o.quarter""")
            tier_change = pct(tier[0]["revenue"], tier[1]["revenue"])
            kit.check("the pair of counts reads at most the members in the step",
                      spend["inside_q1"] <= spend["members"] and spend["inside_q2"] <= spend["members"])
            kit.check("the average moves as the tier's revenue does, so both quarters cover the same members",
                      abs(pct(spend["q1_average"], spend["q2_average"]) - tier_change) < 0.2,
                      f"{pct(spend['q1_average'], spend['q2_average']):+.1f}% against {tier_change:+.1f}%")
            '''),
        md("""
        ## Part 4. Does the suite add up the way the analyst will add it?

        Where this is used at work: every report that shows a total beside its parts is added up by
        someone before it is believed.
        """),
        code(r'''
            per_q = rows(f"""SELECT c.segment, o.quarter, count(DISTINCT o.customer_id) AS customers
                           FROM orders o JOIN customers c USING (customer_id) {FILTER}
                           GROUP BY c.segment, o.quarter ORDER BY 1, 2""")
            # TODO 8. Which expression counts each segment's customers over the half-year?
            #   a) the sum of the segment's two quarter counts
            #   b) count(DISTINCT o.customer_id) over both quarters' delivered orders
            #   c) the larger of the two quarter counts
            #   d) count(*) over both quarters' delivered orders
            HALF = {"a": "added", "b": "count(DISTINCT o.customer_id)", "c": "larger", "d": "count(*)"}[__TODO8__]
            quarters = {}
            for r in per_q:
                quarters.setdefault(r["segment"], []).append(r["customers"])
            if HALF == "added":
                half = {s: sum(v) for s, v in quarters.items()}
            elif HALF == "larger":
                half = {s: max(v) for s, v in quarters.items()}
            else:
                half = {r["segment"]: r["customers"] for r in rows(
                    f"""SELECT c.segment, {HALF} AS customers FROM orders o JOIN customers c USING (customer_id)
                        {FILTER} GROUP BY c.segment ORDER BY 1""")}
            members = {r["segment"]: r["members"] for r in rows(
                "SELECT segment, count(*) AS members FROM customers GROUP BY segment ORDER BY segment")}
            kit.columns(sorted(half), [("half-year customers", [half[s] for s in sorted(half)]),
                                       ("members on the book", [members[s] for s in sorted(half)])],
                        title="The half-year beside the members each segment holds")
            '''),
        code(r'''
            both = {r["segment"]: r["both"] for r in rows(f"""
                WITH per AS (SELECT c.segment, o.customer_id, count(DISTINCT o.quarter) AS quarters
                             FROM orders o JOIN customers c USING (customer_id) {FILTER} GROUP BY 1, 2)
                SELECT segment, count(*) FILTER (WHERE quarters = 2) AS both FROM per GROUP BY 1""")}
            kit.check("no segment's half-year exceeds its members", all(half[s] <= members[s] for s in half))
            kit.check("each half-year equals Q1 plus Q2 less the customers in both",
                      all(half[s] == sum(quarters[s]) - both[s] for s in half))
            '''),
        md("""
        ## Part 5. Will the analyst's rerun draw the same sample, and what does the run print beside it?

        Where this is used at work: an audit sample that cannot be drawn twice cannot be audited, and a
        fingerprint is what tells a changed book from a changed query.
        """),
        code(r'''
            # TODO 9. Which ordering makes five delivered Q2 web orders the same five on every run?
            #   a) ORDER BY customer_id
            #   b) no ORDER BY, only LIMIT 5
            #   c) ORDER BY quarter
            #   d) ORDER BY order_id
            ORDERING = {"a": "ORDER BY customer_id", "b": "", "c": "ORDER BY quarter", "d": "ORDER BY order_id"}[__TODO9__]

            # TODO 10. What should the fingerprint beside the delivered suite hold?
            #   a) the delivered book's rows, rupees and distinct customers
            #   b) the row count of orders only
            #   c) the time the query took to run
            #   d) the date the suite was run
            FINGER = {"a": "count(*) AS rows, sum(amount) AS rupees, count(DISTINCT customer_id) AS customers",
                      "b": "count(*) AS rows", "c": "0 AS milliseconds", "d": "0 AS run_date"}[__TODO10__]

            sample_sql = f"""SELECT order_id, amount FROM orders
            WHERE quarter = 'Q2' AND channel = 'web' AND status = 'delivered' {ORDERING} LIMIT 5"""
            first = rows(sample_sql)
            conn = kit.connect()
            try:
                kit.sql("UPDATE orders SET status = status WHERE order_id IN "
                        "(SELECT order_id FROM orders WHERE quarter = 'Q2' AND channel = 'web' AND status = 'delivered' "
                        "ORDER BY order_id LIMIT 2)", conn=conn)
                second = [{k: num(v) for k, v in r.items()} for r in kit.sql(sample_sql, conn=conn)]
            finally:
                conn.rollback()
                conn.close()
            finger = rows(f"SELECT {FINGER} FROM orders {FILTER}")[0]
            show(first, "The sample on this run", money=("amount",))
            show([finger], "The delivered book's fingerprint", money=("rupees",))
            kit.bars([("this run", sum(r["amount"] for r in first)), ("the rerun after a reload", sum(r["amount"] for r in second))],
                     fmt=kit.rupees, title="The sample's total on two runs")
            '''),
        code(r'''
            kit.check("the rerun after a reload draws the same five", [r["order_id"] for r in first] == [r["order_id"] for r in second])
            kit.check("the fingerprint's rows equal the delivered book's orders",
                      finger.get("rows") == book["Q1"]["orders"] + book["Q2"]["orders"])
            kit.check("the fingerprint carries rupees and customers as well as rows", {"rupees", "customers"} <= set(finger))
            '''),
        md("""
        **Post your answer.** Ten letters, in the order of the markers, as one line, and beside them the
        three numbers the brief asks for: Q2's delivered revenue, Retail-Plus's Q2 orders per customer,
        and Retail-Plus's half-year customers.
        """),
        code("kit.check_summary()"),
    ]
    answers = {1: '"d"', 2: '"a"', 3: '"c"', 4: '"b"', 5: '"d"', 6: '"a"', 7: '"c"', 8: '"b"', 9: '"d"', 10: '"a"'}
    cells.insert(-2, md("""
        SOLUTION ONLY
        **Why each key holds.** 1 d keeps only delivered orders; a keeps the returns, b keeps them on
        purpose, and c tests a row inside `HAVING`, which Postgres refuses. 2 a counts each customer once;
        b and d count rows and c counts rows with a customer id, which is every row. 3 c groups by both;
        a stops with the GROUP BY error and b and d give the wrong grain. 4 b divides in `numeric`; a
        rounds an integer division that already dropped the fraction, c is the integer division itself,
        and d divides the wrong way round. 5 d tests each group's customers after grouping; a and c test
        rows in `WHERE`, where a group's count does not exist yet, and b counts orders. 6 a says Rs 0 on
        purpose; b and c skip the members with no Q2 delivery, and d reads one member. 7 c counts the
        values inside each average; a and d add or average, and b counts distinct amounts. 8 b counts
        each customer once over both quarters; a counts the 41 two-quarter members twice, c undercounts,
        and d counts orders. 9 d orders on the table's key, a column no two rows share; a orders on a
        column two orders from one customer share, b is the unordered sample, and c orders on a value
        every row here shares. 10 a is the fingerprint; b cannot tell a change
        in rupees, and c and d describe the run, not the book.
        """))
    twin(NB / "C2_W02_D01_ex1_escalated_case_STUDENT.ipynb",
         SOL / "C2_W02_D01_ex1_escalated_case_solution_STUDENT.ipynb", cells, answers)
    print("built the escalated case twin and its solution")


# ----------------------------------------------------------------------------------- the second case
def second():
    """The second case: the same tree by channel, and which channel is losing Kalpa's consumers."""
    cells = [
        md("""
        # Which channel is losing Kalpa's consumers, once the Business orders are read apart?

        **Week 2, Monday. The second case, in pairs or alone.** It runs in the take-home.

        > "The same numbers for every channel: app, web and store. Marketing says the store is booming
        > and the web is collapsing, and wants the budget moved. Is that what the book says?"
        > Anand Iyer, finance controller, Kalpa Retail

        **The situation.** Kalpa sells through three channels: its app, its website and its stores.
        Booked revenue, every order at its amount, was Rs 10,00,00,000 in Q1 (April to June 2026) and
        Rs 9,84,00,000 in Q2 (July to September 2026). Business, the corporate segment, books about 99
        percent of those rupees in orders worth lakhs each, while the other three segments, Retail-Core,
        Retail-Plus and Student, are Kalpa's consumers, whose orders are worth hundreds or a few thousand.
        Marketing read the channel totals and wants budget moved from the web to the stores.

        """),
        md("""
        TODO ONLY
        **How to answer.** Each step holds `TODO` markers: lettered choices in a comment above a
        placeholder whose name starts with `__TODO` and ends in the marker's number. Replace each
        placeholder with the letter in quotes and run the step; the check after it tells you whether the
        step behaves. Running the notebook before a marker is filled stops at that marker with a
        `NameError`, as expected. Post your seven letters in order.
        """),
        md("""
        SOLUTION ONLY
        **This is the solution.** Every marker is filled with its key and the notebook runs clean from the
        top; the reasons for each key are at the end.
        """),
        code(CASE_SETUP),
        code(r'''
            kit.side_by_side(
                kit.ladder(["The channel totals", "Business and consumers apart", "The consumers' tree per channel",
                            "The tie-out", "The line for Anand"], lit=0, show=False),
                kit.driver_tree({"label": "a channel's revenue", "kind": "lit", "children": [
                    {"label": "Business", "note": "a few large orders"},
                    {"label": "consumers", "note": "many small orders"}]}, show=False),
            )
            '''),
        md("""
        ## Step 1. What do the channel totals say from Q1 to Q2?

        Where this is used at work: a channel manager's budget follows the channel's total, so the
        total is the first number anyone reads.
        """),
        code(r'''
            # TODO 1. Which grouping gives one row per channel and quarter?
            #   a) GROUP BY channel, quarter
            #   b) GROUP BY channel
            #   c) GROUP BY quarter
            #   d) GROUP BY customer_id, channel
            GROUPING = {"a": "GROUP BY channel, quarter", "b": "GROUP BY channel", "c": "GROUP BY quarter",
                        "d": "GROUP BY customer_id, channel"}[__TODO1__]
            totals = rows(f"SELECT channel, quarter, count(*) AS orders, sum(amount) AS revenue FROM orders {GROUPING} ORDER BY 1, 2")
            show(totals, "The channel totals", money=("revenue",))
            t = {(r["channel"], r["quarter"]): r for r in totals}
            channels = sorted({r["channel"] for r in totals})
            kit.columns(channels, [(q, [t[(c, q)]["revenue"] / 1e5 for c in channels]) for q in ("Q1", "Q2")],
                        title="Booked revenue per channel, Rs lakh", fmt=lambda v: f"{v:,.0f}")
            '''),
        code(r'''
            kit.check("six rows, one per channel and quarter", len(totals) == 6)
            kit.check("the channels add back to the book in each quarter",
                      sum(t[(c, "Q1")]["revenue"] for c in channels) == 100000000
                      and sum(t[(c, "Q2")]["revenue"] for c in channels) == 98400000)
            '''),
        md("""
        ## Step 2. How much of each channel is Business, and how much is consumers?

        Where this is used at work: a total made of a few very large orders and many small ones is two
        businesses, and each is read on its own before the total is.
        """),
        code(r'''
            # TODO 2. Which expression labels each order as Business or consumer?
            #   a) c.segment
            #   b) CASE WHEN c.segment = 'Business' THEN 'Business' ELSE 'consumer' END
            #   c) CASE WHEN o.amount > 100000 THEN 'Business' ELSE 'consumer' END
            #   d) WHERE c.segment <> 'Business'
            KIND = {"a": "c.segment", "b": "CASE WHEN c.segment = 'Business' THEN 'Business' ELSE 'consumer' END",
                    "c": "CASE WHEN o.amount > 100000 THEN 'Business' ELSE 'consumer' END",
                    "d": "WHERE c.segment <> 'Business'"}[__TODO2__]
            split = rows(f"""SELECT o.channel, {KIND} AS kind, o.quarter, count(*) AS orders,
                                    count(DISTINCT o.customer_id) AS customers, sum(o.amount) AS revenue
                             FROM orders o JOIN customers c USING (customer_id)
                             GROUP BY 1, 2, 3 ORDER BY 1, 2, 3""")
            show(split, "Each channel, Business and consumers apart", money=("revenue",))
            '''),
        code(r'''
            kinds = {r["kind"] for r in split}
            biz = {(r["channel"], r["quarter"]): r["revenue"] for r in split if r["kind"] == "Business"}
            if biz:
                kit.columns(channels, [(q, [biz.get((c, q), 0) / 1e5 for c in channels]) for q in ("Q1", "Q2")],
                            title="Business revenue per channel, Rs lakh: where the large orders went", fmt=lambda v: f"{v:,.0f}")
            kit.check("every order is labelled one of two kinds", len(kinds) == 2, ", ".join(sorted(kinds)))
            kit.check("the two kinds add back to each channel's total",
                      all(sum(r["revenue"] for r in split if r["channel"] == c and r["quarter"] == q) == t[(c, q)]["revenue"]
                          for c in channels for q in ("Q1", "Q2")))
            '''),
        md("""
        ## Step 3. How did each channel's consumers move, branch by branch?

        Where this is used at work: a channel's consumer health is its consumers' tree, customers times
        orders each times revenue per order, read as a change.
        """),
        code(r'''
            # TODO 3. Which expression counts each channel's consumers, each once?
            #   a) count(*)
            #   b) sum(1)
            #   c) count(DISTINCT o.customer_id)
            #   d) count(o.customer_id)
            CUST = {"a": "count(*)", "b": "sum(1)", "c": "count(DISTINCT o.customer_id)",
                    "d": "count(o.customer_id)"}[__TODO3__]

            # TODO 4. Which expression gives orders per consumer that multiplies back?
            #   a) count(*) / {cust}
            #   b) round(count(*) / {cust}, 2)
            #   c) round({cust}::numeric / count(*), 2)
            #   d) round(count(*)::numeric / {cust}, 2)
            FREQ = {"a": "count(*) / {cust}", "b": "round(count(*) / {cust}, 2)", "c": "round({cust}::numeric / count(*), 2)",
                    "d": "round(count(*)::numeric / {cust}, 2)"}[__TODO4__].format(cust=CUST)
            consumers = rows(f"""SELECT o.channel, o.quarter, count(*) AS orders, {CUST} AS customers,
                                        {FREQ} AS orders_per_customer, sum(o.amount) AS revenue
                                 FROM orders o JOIN customers c USING (customer_id)
                                 WHERE c.segment <> 'Business'
                                 GROUP BY o.channel, o.quarter ORDER BY 1, 2""")
            show(consumers, "Consumers only, per channel and quarter", money=("revenue",))
            cons = {(r["channel"], r["quarter"]): r for r in consumers}
            kit.columns(channels, [(q, [cons[(c, q)]["revenue"] / 1000 for c in channels]) for q in ("Q1", "Q2")],
                        title="Consumer revenue per channel, Rs thousand", fmt=lambda v: f"{v:,.0f}")
            '''),
        code(r'''
            kit.check("consumers are fewer than their orders in every row", all(r["customers"] < r["orders"] for r in consumers))
            kit.check("every ratio multiplies back to its orders within half an order",
                      all(abs(float(r["orders_per_customer"]) * r["customers"] - r["orders"]) < 0.5 for r in consumers))
            '''),
        md("""
        ## Step 4. Which line goes on Anand's channel sheet?

        Where this is used at work: the line a budget is moved on has to read the part of the business
        the budget is for.
        """),
        code(r'''
            change = {c: pct(cons[(c, "Q1")]["revenue"], cons[(c, "Q2")]["revenue"]) for c in channels}
            total_change = {c: pct(t[(c, "Q1")]["revenue"], t[(c, "Q2")]["revenue"]) for c in channels}
            kit.table(["channel", "booked total, Q1 to Q2", "consumers only, Q1 to Q2"],
                      [(c, f"{total_change[c]:+.1f}%", f"{change[c]:+.1f}%") for c in channels],
                      caption="The channel totals beside the consumers' own change")
            kit.bars([(c, abs(change[c])) for c in channels], fmt=lambda v: f"down {v:.1f}%",
                     title="How far each channel's consumer revenue fell, Q1 to Q2")

            # TODO 5. Which channel lost the largest share of its consumer revenue?
            #   a) web
            #   b) store
            #   c) none: every channel held its consumers
            #   d) app
            WORST = {"a": "web", "b": "store", "c": None, "d": "app"}[__TODO5__]

            # TODO 6. Which line goes on Anand's sheet for the store?
            #   a) Store revenue rose 61.1 percent: move budget to the stores.
            #   b) Store consumer revenue fell 18.8 percent; the store total rose on Business orders.
            #   c) The store is flat once the Business orders are removed.
            #   d) Store revenue cannot be reported until Business is removed from the book.
            LINE = {"a": 61.1, "b": -18.8, "c": 0.0, "d": None}[__TODO6__]

            # TODO 7. Which fact would move the budget question back to the channel totals?
            #   a) If the web's consumer orders fell further next quarter
            #   b) If Anand asked for the channels in rupees rather than orders
            #   c) If Business placed its orders through whichever channel its buyer chose on the day
            #   d) If Business orders were placed through a channel because of that channel's own service
            REASON = {"a": "consumers", "b": "rupees", "c": "chance", "d": "service"}[__TODO7__]
            '''),
        code(r'''
            kit.check("no channel lost a larger share of its consumer revenue than the one named",
                      WORST is not None and all(change[WORST] <= v for v in change.values()))
            kit.check("the store line carries the store's consumer change", LINE is not None and abs(LINE - change["store"]) < 0.05)
            kit.check("every channel's consumers fell", all(v < 0 for v in change.values()))
            '''),
        md("""
        **Post your answer.** Seven letters, in the order of the markers, and one line for Anand that
        names the channel losing its consumers fastest, with its number.
        """),
        code("kit.check_summary()"),
    ]
    answers = {1: '"a"', 2: '"b"', 3: '"c"', 4: '"d"', 5: '"d"', 6: '"b"', 7: '"d"'}
    cells.insert(-2, md("""
        SOLUTION ONLY
        **Why each key holds.** 1 a gives the six rows; b and c lose a dimension and d gives one row per
        customer and channel. 2 b labels by segment; a keeps four segments, c labels by size and would
        call a large consumer order Business, and d is a filter, which removes Business instead of
        labelling it. 3 c counts each consumer once; a, b and d count orders. 4 d divides in `numeric`;
        a and b divide integers and c divides the wrong way round. 5 d: app consumer revenue fell 24.1
        percent, against 18.8 for the store and 7.4 for the web; c is what the store and web totals
        suggest if Business is left in. 6 b reads the store's consumers and names why the total rose; a
        is Marketing's reading of the total, c is wrong on the numbers, and d refuses a report the book
        can give. 7 d: only if Business chose a channel for that channel's own service would the
        channel's total say something about the channel; a is about consumers and would not move the
        question, b changes the unit, and c is the reason the totals mislead.
        """))
    twin(NB / "C2_W02_D01_ex2_second_case_STUDENT.ipynb",
         SOL / "C2_W02_D01_ex2_second_case_solution_STUDENT.ipynb", cells, answers)
    print("built the second case twin and its solution")


# ----------------------------------------------------------------------------------- the build
STEMS = {
    "ch1": ("01_what_the_book_says", ch1),
    "ch2": ("02_same_story_as_week1", ch2),
    "ch3": ("03_which_segment_moved", ch3),
    "ch4": ("04_which_branch_moved", ch4),
    "ch5": ("05_does_the_suite_add_up", ch5),
    "ch6": ("06_same_answer_next_week", ch6),
}


def main(names):
    NB.mkdir(parents=True, exist_ok=True)
    for name in names or list(STEMS) + ["case", "second"]:
        if name in STEMS:
            stem, cells = STEMS[name]
            path = NB / f"C2_W02_D01_{stem}_STUDENT.ipynb"
            build(path, cells())
            print("built", path)
        elif name == "case":
            case()
        elif name == "second":
            second()


if __name__ == "__main__":
    main(sys.argv[1:])

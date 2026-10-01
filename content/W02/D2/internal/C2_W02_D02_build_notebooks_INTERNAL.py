"""Write and execute the six chapter notebooks of Week 2 Tuesday, and the sql/ file of each chapter.

    python3 content/W02/D2/internal/C2_W02_D02_build_notebooks_INTERNAL.py          # all six
    python3 content/W02/D2/internal/C2_W02_D02_build_notebooks_INTERNAL.py 3 4      # chapters 3 and 4

Each chapter notebook pairs with one `## SECTION n:` of the decks and carries the need, the options
with their sizing, the build in levels, the trap, the second route and Kavya's review. The queries
live once, in the Q dictionaries below: the notebook runs them and the chapter's .sql file prints
them, so the two cannot drift.

The warehouse's unpaid orders, gateway retries and orphan payments are planted, and the room finds
them. So every Kalpa number that would name one (a count, a total, an id, or two printed numbers
whose difference gives one) is left to an empty your-turn cell and a check that prints PASS without
the value. The mechanism is shown on the invented tiny tables, where every number may print. The
Kalpa numbers that do print are Monday's booked figures, the fan-out's row counts, the first
draft's Rs 19,29,04,410, the DISTINCT option's Rs 9,63,67,220 and the 216 orders the order-level
HAVING list flags; no pair of them subtracts to a planted value (the provenance shows the working).

Needs the warehouse loaded (bash .devcontainer/load_warehouse.sh) and psycopg2-binary.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, md, code, empty, build  # noqa: E402

DAY = ROOT / "content" / "W02" / "D2"
NB = DAY / "notebooks"
SQL = DAY / "sql"

LADDER = ["What does a join keep?", "Why twice the bookings?", "Is every order there?",
          "Which orders, exactly?", "What does Anand sign?", "Can the number leave?"]

QUESTIONS = {
    1: "When payments are attached to orders, which rows does each join keep, drop or repeat?",
    2: "Why does the first join on Kalpa's Q2 report nearly twice the bookings as collected, and "
       "how do we attach payments so that nothing counts twice?",
    3: "Once nothing counts twice, is every booked order still in the report, and can every rupee "
       "between booked and posted be named?",
    4: "Which Q2 orders were never paid, and which payments did the gateway post twice?",
    5: "What goes on the report by channel that Anand signs, and does its gap column tell the truth?",
    6: "Which checks must pass before the collected number leaves the team, and what does Anand "
       "get when one fails at the end of reporting day?",
}

SLUGS = {1: "what_a_join_keeps", 2: "why_twice_booked", 3: "every_order_there",
         4: "which_orders", 5: "what_anand_signs", 6: "can_it_leave"}

ASK = """> **The client asks.** "Booked revenue is not collected revenue. Some orders are paid in two
> instalments, some are refunded, some were never paid at all. Show me, order by order, what we
> actually collected against what we booked in Q2. If there is a gap, I want to know which orders
> and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

The data platform lead added the payments table to the team's access and said, in passing, that
the payments feed "sometimes double-posts when the gateway retries"."""

DOSSIER = ("The retail story behind Anand's role, how a sale becomes cash and who checks it, is in the "
           "domain dossier, `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`, "
           "sections 3 and 4.")

# The real company per chapter, each fact checked on 1 Oct 2026; the provenance holds the URLs.
COMPANY = {
    1: """**Who else faces this.** Razorpay, the Indian payment gateway, documents the same shape from a
merchant's side. Its Orders API "combines multiple payment attempts for a single order"; an order
stays attempted until a payment is captured and then moves to paid; and a merchant who asks for the
payments of one order gets "all the authorised or failed payments for that order", so one order id
appears once in the merchant's orders and several times in the payments list (Razorpay
documentation, About Orders and Fetch Payments for an Order, checked 1 Oct 2026). Every merchant
who puts the two lists side by side has to decide which rows a join keeps, drops or repeats.""",
    2: """**Who else faces this.** Shopify creates a transaction "for every order that results in an
exchange of money", and one order can carry several: an authorization, which is money the customer
has agreed to pay, a capture of that same money, a sale, a void or a refund (Shopify developer
documentation, the REST Admin API's Transaction resource, a legacy API since 1 October 2024, checked 1 Oct 2026).
A report that adds every transaction of an order counts an authorised and captured payment twice.""",
    3: """**Who else faces this.** Stripe's payout reconciliation report lets a merchant match each payout
in the bank with "the batches of payments and other transactions that they relate to", itemizing
every payment, refund, dispute and fee inside it (Stripe documentation, Payout reconciliation report,
checked 1 Oct 2026). The public case of a missing-row failure is Public Health England, which left
15,841 positive COVID-19 cases out of the daily figures reported between 25 September and 2 October
2020 (PHE statement, GOV.UK, 4 October 2020). The results arrived as CSV files and were pulled into
Excel templates in the old XLS format; each result took several rows, so a template held about 1,400
cases, and once it was full further cases were left off (BBC News, 5 October 2020; both checked 1 Oct
2026). No row that arrived was wrong; what was lost were the rows that never loaded, which is what a
count of rows sent against rows loaded measures.""",
    4: """**Who else faces this.** Stripe builds its payments API so that a retried request cannot charge
twice: the client sends an idempotency key, Stripe saves the result of the first request made with
it, and "subsequent requests with the same key return the same result" (Stripe API reference,
Idempotent requests, checked 1 Oct 2026). India's regulator sets a deadline for the other side of
the same problem. Under the Reserve Bank of India's circular of 20 September 2019, when a customer's
account is debited for an online card payment and the merchant's system never receives the
confirmation, the debit must be reversed automatically within five days of the transaction, with compensation of
Rs 100 for every day of delay after that (RBI/2019-20/67, in force from 15 October 2019, checked 1
Oct 2026).""",
    5: """**Who else faces this.** Infosys reports the gap between what it has billed and what it has
collected every quarter, as days sales outstanding, which is money owed by customers divided by
revenue per day: 63 days for the quarter ended 30 June 2026, against 67 at 31 March 2026 and 70 a
year earlier, on the last twelve months' revenue (Infosys fact sheet, Exhibit 99.4 to the Form 6-K
furnished to the US Securities and Exchange Commission on 28 July 2026, checked 1 Oct 2026). A finance team that
publishes a collections figure every quarter answers for it, which is the position Anand is in when
he signs this report.""",
    6: """**Who else faces this.** Wirecard, a German payments company, collapsed in June 2020 over cash it
reported and did not have. On 18 June its auditor, EY, refused to sign off on the accounts, saying it
was unable to confirm that the money existed; on 22 June Wirecard said there was "a prevailing likelihood"
that 1.9 billion euros of trust account balances did not exist; on 25 June it filed for insolvency
(BBC News, 18, 22 and 25 June 2020, checked 1 Oct 2026). People with first-hand knowledge told the
Financial Times that from 2016 to 2018 the auditor had not checked directly with Singapore's OCBC
Bank, where Wirecard claimed it had up to 1 billion euros in cash, and relied instead on documents
and screenshots from a third-party trustee and from Wirecard itself (FT, republished by the Irish
Times, 26 June 2020, checked 1 Oct 2026).""",
}

# ------------------------------------------------------------------------------------------ data
TINY = """DROP TABLE IF EXISTS pg_temp.tiny_orders, pg_temp.tiny_payments;
CREATE TEMP TABLE tiny_orders (
    order_id  text PRIMARY KEY,
    channel   text NOT NULL,
    amount    numeric(12, 2) NOT NULL
);
CREATE TEMP TABLE tiny_payments (
    payment_id    text PRIMARY KEY,
    order_id      text NOT NULL,
    paid_date     date NOT NULL,
    amount        numeric(12, 2) NOT NULL,
    instalment_no integer NOT NULL
);
INSERT INTO tiny_orders VALUES
    ('T-1', 'app',   1000),
    ('T-2', 'web',   2000),
    ('T-3', 'store', 1500),
    ('T-4', 'app',    800),
    ('T-5', 'store',  500);
INSERT INTO tiny_payments VALUES
    ('P-1', 'T-1', '2026-07-03', 1000, 1),
    ('P-2', 'T-2', '2026-07-05', 1200, 1),
    ('P-3', 'T-2', '2026-08-05',  800, 2),
    ('P-4', 'T-3', '2026-07-09', 1500, 1),
    ('P-5', 'T-3', '2026-07-09', 1500, 1),
    ('P-6', 'T-5', '2026-07-12',  500, 1),
    ('P-7', 'T-9', '2026-07-14',  600, 1);"""

TINY_NOTE = """**The two invented tables.** They hold five orders and seven payments, invented to carry every
case Anand named and the one the platform lead mentioned, so every row can be checked by hand:

| order_id | channel | amount | What happened to it |
|---|---|---|---|
| T-1 | app | 1,000 | Paid once, in full (P-1) |
| T-2 | web | 2,000 | Paid in two instalments, 1,200 and 800 (P-2, P-3) |
| T-3 | store | 1,500 | Paid once, and the gateway posted that payment twice (P-4, P-5) |
| T-4 | app | 800 | Never paid |
| T-5 | store | 500 | Paid once, in full (P-6) |

P-7 is a payment of 600 against T-9, an order that is not in the orders table."""

HELPERS = SETUP + '''from decimal import Decimal

TINY = """''' + TINY + '''"""

conn = kit.connect()
conn.autocommit = True
with conn.cursor() as cur:
    cur.execute(TINY)            # invented, TEMP, so they vanish when this notebook stops


def run(query, params=None):
    """Run a query on this notebook's one connection and return its rows as dictionaries."""
    return kit.sql(query, params, conn=conn)


def one(query, params=None):
    """The first value of the first row, for a query that returns a single number."""
    row = run(query, params)[0]
    return next(iter(row.values()))


def show(rows, caption="", money=()):
    """Rows as the kit's table; columns named in money print as rupees."""
    if not rows:
        return kit.table(["result"], [["no rows"]], caption)
    heads = list(rows[0])
    body = []
    for r in rows:
        line = []
        for h in heads:
            v = r[h]
            if v is None:
                line.append("NULL")
            elif h in money:
                line.append(kit.rupees(v))
            elif isinstance(v, Decimal):
                line.append(f"{int(v):,}" if v == v.to_integral_value() else f"{float(v):,.2f}")
            else:
                line.append(str(v))
        body.append(line)
    kit.table(heads, body, caption)
'''


def title_cell(n, who, steps, metric, before):
    q = "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    return md(f"""
# Chapter {n}. {QUESTIONS[n]}

**Week 2, Tuesday · Chapter {n} of 6 · Booked against collected.**

{ASK}

**Who needs the answer.** {who}

**The questions on the way.**
{q}

**The metric at stake.** {metric}

**What came before, and what this adds.** {before}
""")


def map_cell(n, steps):
    return code(f"""
kit.side_by_side(
    kit.ladder({LADDER!r}, lit={n - 1}, show=False),
    kit.vflow({steps!r}, show=False),
)""")


def write_sql(n, header, steps):
    """The chapter's .sql file: the question, then each step's question and query."""
    lines = [f"-- Week 2, Tuesday. Chapter {n}: {QUESTIONS[n]}"]
    lines += [f"-- {h}" for h in header]
    lines.append("-- Run it against the warehouse: psql -d kalpa -f this_file.sql")
    lines.append("")
    for label, query in steps:
        lines.append(f"-- {label}")
        lines.append(query.strip().rstrip(";") + ";")
        lines.append("")
    path = SQL / f"C2_W02_D02_0{n}_{SLUGS[n]}_STUDENT.sql"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def nb_path(n):
    return NB / f"C2_W02_D02_0{n}_{SLUGS[n]}_STUDENT.ipynb"


# ============================================================================================== 1
Q1 = {
    "grain": """
SELECT 'orders' AS source, count(*) AS row_count, count(DISTINCT order_id) AS order_ids
FROM orders
UNION ALL
SELECT 'payments', count(*), count(DISTINCT order_id)
FROM payments""",
    "most_rows": """
SELECT max(rows_per_id) AS most_rows_for_one_order_id
FROM (SELECT order_id, count(*) AS rows_per_id FROM payments GROUP BY order_id) AS per_id""",
    "inner": """
SELECT o.order_id, o.amount AS booked, p.payment_id, p.amount AS paid, p.instalment_no
FROM tiny_orders o
JOIN tiny_payments p ON p.order_id = o.order_id
ORDER BY o.order_id, p.payment_id""",
    "counts": """
SELECT 'INNER' AS join_type, count(*) AS row_count
FROM tiny_orders o JOIN tiny_payments p ON p.order_id = o.order_id
UNION ALL
SELECT 'LEFT', count(*)
FROM tiny_orders o LEFT JOIN tiny_payments p ON p.order_id = o.order_id
UNION ALL
SELECT 'RIGHT', count(*)
FROM tiny_orders o RIGHT JOIN tiny_payments p ON p.order_id = o.order_id
UNION ALL
SELECT 'FULL', count(*)
FROM tiny_orders o FULL JOIN tiny_payments p ON p.order_id = o.order_id""",
    "payments_first": """
SELECT p.payment_id, p.order_id AS paid_for, p.amount AS paid, o.order_id, o.amount AS booked
FROM tiny_payments p
LEFT JOIN tiny_orders o ON o.order_id = p.order_id
ORDER BY p.payment_id""",
    "orders_first": """
SELECT o.order_id, o.amount AS booked, p.payment_id, p.amount AS paid
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
ORDER BY o.order_id, p.payment_id""",
    "key_counts": """
SELECT k.order_id,
       (SELECT count(*) FROM tiny_orders o WHERE o.order_id = k.order_id)   AS rows_in_orders,
       (SELECT count(*) FROM tiny_payments p WHERE p.order_id = k.order_id) AS rows_in_payments
FROM (SELECT order_id FROM tiny_orders UNION SELECT order_id FROM tiny_payments) AS k
ORDER BY k.order_id""",
}

CH1_STEPS = ["the need: which rows survive a join?", "the options: four joins, sized",
             "one row of each table", "INNER traced by hand", "LEFT, RIGHT and FULL",
             "the trap: a statement that starts from payments", "a second route: the keys alone"]


def chapter1():
    n = 1
    ladder = ["Which join answers Anand's question about every booked order?",
              "What is one row of `orders`, and one row of `payments`?",
              "On five orders and seven payments, how many rows does each of the four joins return?",
              "What does a statement that starts from the payments table tell Anand?",
              "Can the row counts be predicted from the keys alone, before any join runs?"]
    cells = [
        title_cell(
            n,
            "Anand's analyst will audit the statement order by order, and you sign the collected "
            "number. A join that drops an unpaid order hides it from the collections "
            "team, and a join that repeats a paid order sends the team after a customer who paid in "
            "full.",
            ladder,
            "Collected revenue is the cash that reached Kalpa against its booked orders, each payment "
            "counted once. Booked revenue is Monday's number, every Q2 order at its amount whatever "
            "its status: Rs 9,84,00,000 over 462 orders.",
            "Monday answered every question from one table, `orders`, where one row is one order, so "
            "a sum was a sum of orders. Today a second table arrives, and a join between two tables "
            "can change how many rows you are adding up. This chapter traces that on two tables small "
            "enough to check by hand, and every later chapter uses what it finds."),
        md("""
**Setup.** The next cell finds the programme's helper, `c2kit`, by walking up from this folder,
connects to the Kalpa warehouse, and creates the two invented tables as TEMP tables on this
notebook's own connection, so they vanish when the notebook stops and the warehouse is never
changed. The same tables and every query below are in `sql/C2_W02_D02_01_what_a_join_keeps_STUDENT.sql`.
"""),
        code(HELPERS + """
print(one("SELECT count(*) FROM tiny_orders"), "invented orders and",
      one("SELECT count(*) FROM tiny_payments"), "invented payments are ready;",
      f'the warehouse holds {one("SELECT count(*) FROM orders"):,} orders.')"""),
        map_cell(n, CH1_STEPS),
        md(f"""
## Why must the join be chosen before any total is read?

Anand wants two numbers per order, booked and collected, and they live in two tables. `orders` holds
what was booked: one row per order, with its channel, quarter, status and amount. `payments` holds
what arrived: one row per payment event, with the order it pays, the date, the amount, the method
and the instalment number. Putting the two side by side is a join, and a join has to decide two
things before it adds anything up: what to do with an order that found no payment, and what to do
with an order that found two.

The decision rides on money Anand can act on. An order the statement drops is an order nobody
chases, and at Kalpa's size one large business invoice can be worth several lakh rupees. An order
the statement lists twice looks short-paid on one of its lines, and a collections clerk who
follows the statement rings a customer who has paid in full. {DOSSIER}
"""),
        md(COMPANY[1] or "**Who else faces this.** (filled from the provenance)"),
        md(TINY_NOTE),
        md("""
## Which of the four joins answers Anand, and what does each cost on five orders?

There are four ways to attach payments to orders, and each keeps a different set of rows. The cell
below measures each one on the invented tables: how many rows it returns, how many of the five booked
orders reach the statement, what happens to T-4 (never paid) and to P-7 (a payment with no order),
and how long it takes.

| Option | What it keeps | The question it answers |
|---|---|---|
| A. INNER JOIN | Only the pairs that match | What do the orders that were paid look like? |
| B. LEFT JOIN, orders first | Every order, matched or not | What happened to each order we booked? |
| C. RIGHT JOIN, payments kept | Every payment, matched or not | Which order does each payment belong to? |
| D. FULL OUTER JOIN | Every order and every payment | Where do the two tables fail to meet, on either side? |
"""),
        code("""
import time
sizing = []
for name, join in [("A. INNER", "JOIN"), ("B. LEFT, orders first", "LEFT JOIN"),
                   ("C. RIGHT, payments kept", "RIGHT JOIN"), ("D. FULL OUTER", "FULL JOIN")]:
    t0 = time.perf_counter()
    rows = run(f\"\"\"
        SELECT o.order_id, p.payment_id
        FROM tiny_orders o {join} tiny_payments p ON p.order_id = o.order_id\"\"\")
    secs = time.perf_counter() - t0
    booked_ids = {r["order_id"] for r in rows if r["order_id"]}
    repeated = sorted({i for i in booked_ids if sum(1 for r in rows if r["order_id"] == i) > 1})
    sizing.append((name, len(rows), f"{len(booked_ids)} of 5",
                   "kept" if "T-4" in booked_ids else "dropped",
                   "kept" if any(r["payment_id"] == "P-7" for r in rows) else "dropped",
                   ", ".join(repeated), f"{secs * 1000:.1f} ms"))
kit.table(["Option", "Rows out", "Booked orders on it", "T-4, never paid", "P-7, no order",
           "Orders listed twice", "Time"], sizing,
          caption="Four joins on the invented tables: 5 orders in, 7 payments in")
kit.bars([(s[0], s[1]) for s in sizing], lit=[1],
         title="Rows each join returns from 5 orders and 7 payments")
kit.check("only B and D keep all five booked orders",
          [s[2] for s in sizing] == ["4 of 5", "5 of 5", "4 of 5", "5 of 5"], [s[2] for s in sizing])
"""),
        md("""
**The best-fit call.** Option B, the LEFT JOIN with orders on the left, fits best, because Anand's
question is about every order Kalpa booked: B is the only option that keeps all five orders and
nothing that is not an order. Every option runs in a few milliseconds here, so the choice rests on
the rows each one keeps. The table also shows what B does not fix: T-2 and T-3 come out twice,
which chapter 2 has to deal with before any total is read.

**The fact that would change the call.** The data platform lead asks a different question: is
every payment in the feed explained by a booked order? That question keeps every payment, so it
starts from `payments` (option C, or a LEFT JOIN with payments first). Asked about both sides at
once, before the feed is repaired, it becomes option D.
"""),
        md("""
## 1. What is one row of `orders`, and one row of `payments`?

The grain of a table is what one row stands for. If the key on one side of a join repeats, every
row it matches on the other side comes out once per repeat.

**Predict before you run.** In the warehouse, does an `order_id` ever appear on more than one row of
`payments`? a) never, each order is paid once; b) yes, up to twice; c) yes, up to five times;
d) only for cancelled orders.
"""),
        code(f"""
grain = run(\"\"\"{Q1['grain']}\"\"\")
most = one(\"\"\"{Q1['most_rows']}\"\"\")
show([{{"table": g["source"], "rows": g["row_count"],
        "one row is": "one order" if g["source"] == "orders" else "one payment event"}} for g in grain],
     "The grain of the two warehouse tables")
kit.flow(["orders\\none row per order", "join on order_id", "payments\\none row per payment event"],
         kinds=["known", "plain", "bad"], title="Two grains meet in one join")"""),
    ]
    cells += [
        md("""
**What happened.** The answer is b. `orders` has as many rows as order ids, 1,000 of each, so an
order is one row. `payments` has 1,428 rows, and the check below finds fewer distinct order ids than
rows, with one order id holding at most two of them, so an order can own two payment rows. Anand named one reason, instalments; the
platform lead named another, a gateway retry. Either way a join to `payments` can repeat an order.
"""),
        code("""
kit.check("orders holds one row per order id", grain[0]["row_count"] == grain[0]["order_ids"],
          f'{grain[0]["row_count"]:,} rows, {grain[0]["order_ids"]:,} ids')
kit.check("payments holds more rows than order ids, so an order id repeats",
          grain[1]["row_count"] > grain[1]["order_ids"], f'{grain[1]["row_count"]:,} rows')
kit.check("no order id holds more than two payment rows", most == 2, f"{most}")"""),
        md("""
## 2. How many rows does the INNER join return on five orders and seven payments?

**Predict before you run.** Join `tiny_orders` to `tiny_payments` on `order_id` with an INNER JOIN.
How many rows come back? a) 5, one per order; b) 6; c) 7, one per payment; d) 8.
"""),
        code(f"""
inner_rows = run(\"\"\"{Q1['inner']}\"\"\")
show(inner_rows, "INNER JOIN on the invented tables: one row per matching pair", money=["booked", "paid"])"""),
        md("""
**What happened.** The answer is b, six rows. An INNER JOIN writes one row for every pair of an order
and a payment that share an `order_id`: T-1 once, T-2 twice (two instalments), T-3 twice (one
payment posted twice), T-5 once. T-4 is gone because no payment matched it, and P-7 is gone because
no order matched it. Nothing in the join asked whether T-4 belonged in Anand's statement; it simply
did not match.
"""),
        md("""
## 3. What do LEFT, RIGHT and FULL do with the rows that find no partner?

The other three joins keep the same six matched pairs and differ only in the unmatched rows they
add back.

**Predict before you run.** How many rows do the LEFT, RIGHT and FULL joins return, in that order?
a) 5, 7 and 8; b) 7, 7 and 8; c) 5, 5 and 7; d) 7, 6 and 8.
"""),
        code(f"""
counts = {{r["join_type"]: r["row_count"] for r in run(\"\"\"{Q1['counts']}\"\"\")}}
kit.bars([(f"{{k}} JOIN", v) for k, v in counts.items()], lit=[1],
         title="Rows returned by each join on the invented tables")
kit.matrix(["INNER", "LEFT", "RIGHT", "FULL"],
           ["T-4, an order with no payment", "P-7, a payment with no order"],
           [["dropped", "dropped"], ["kept, payment side NULL", "dropped"],
            ["dropped", "kept, order side NULL"], ["kept", "kept"]],
           title="What each join does with the rows that find no partner")"""),
        md("""
**What happened.** The answer is b: LEFT returns 7, the six pairs plus T-4 with NULL where its payment
would be; RIGHT returns 7, the six pairs plus P-7 with NULL where its order would be; FULL returns
8, the six plus both. Every join repeats T-2 and T-3, because the repeat comes from the key, and no
choice of join type removes it.
"""),
        code("""
kit.check("INNER returns 6 rows: every matching pair", counts["INNER"] == 6, f'{counts["INNER"]}')
kit.check("LEFT adds exactly the one order with no payment", counts["LEFT"] - counts["INNER"] == 1,
          f'{counts["LEFT"]} against {counts["INNER"]}')
kit.check("RIGHT adds exactly the one payment with no order", counts["RIGHT"] - counts["INNER"] == 1,
          f'{counts["RIGHT"]} against {counts["INNER"]}')
kit.check("FULL keeps both kinds of orphan", counts["FULL"] == counts["INNER"] + 2, f'{counts["FULL"]}')"""),
        md("""
## 4. What does a statement that starts from the payments table tell Anand?

**The plausible wrong answer.** A hurried analyst reasons that collected money lives in `payments`,
so the statement should start there: every payment, with its order attached. That is a LEFT JOIN
with `payments` first, which returns the same rows as option C.

**Predict before you run.** On the invented tables, how many of the five booked orders appear on
that statement, and how much cash does it total? a) 5 orders, 5,800; b) 4 orders, 7,100;
c) 5 orders, 6,500; d) 4 orders, 5,000.
"""),
        code(f"""
pay_first = run(\"\"\"{Q1['payments_first']}\"\"\")
show(pay_first, "The statement started from payments: every payment, its order attached",
     money=["paid", "booked"])
on_statement = {{r["order_id"] for r in pay_first if r["order_id"]}}
cash = sum(r["paid"] for r in pay_first)
booked_total = one("SELECT sum(amount) FROM tiny_orders")
kit.stats([(f"{{len(on_statement)}} of 5", "booked orders on it", "T-4 is missing"),
           (f"{{int(cash):,}}", "cash on the statement", "every payment row"),
           (f"{{int(booked_total):,}}", "booked", "five orders"),
           (f"{{cash / booked_total:.0%}}", "collected, as it reads", "of booked")])
kit.columns(["booked", "cash on the statement"],
            [("invented tables", [float(booked_total), float(cash)])],
            title="Invented: the payments-first statement shows more cash than was booked")"""),
        md("""
**What happened.** The answer is b: four of the five booked orders, and 7,100 of cash against 5,800
booked, so the statement reads as 122 percent collected.

**Why it is wrong.** Anand asked about the orders Kalpa booked, and this statement answers a
different question, which payment belongs to which order. T-4, the one order nobody paid, never
reaches it, so the collections team has nothing to chase. The cash total carries 600 from P-7,
which pays an order that is not in Kalpa's books, and 1,500 from P-5, T-3's payment posted a second
time. A finance controller who reads "we collected more than we booked" stands his collections
team down.

**The check that catches it.** Count the booked orders on the statement against the orders table,
and count the lines with no booked order behind them. Neither check reads a rupee.
"""),
        code(f"""
orders_first = run(\"\"\"{Q1['orders_first']}\"\"\")
missing = one("SELECT count(*) FROM tiny_orders") - len(on_statement)
no_order = sum(1 for r in pay_first if r["order_id"] is None)
kit.check("the payments-first statement misses a booked order", missing == 1, f"{{missing}} missing")
kit.check("the payments-first statement carries a line with no booked order", no_order == 1,
          f"{{no_order}} line, P-7")
fixed_ids = {{r["order_id"] for r in orders_first}}
kit.check("the fix, orders first, puts all five booked orders on the statement", len(fixed_ids) == 5,
          f"{{len(fixed_ids)}} of 5 across {{len(orders_first)}} lines")
show(orders_first, "The fix: orders first, so every booked order is on the statement",
     money=["booked", "paid"])"""),
        md("""
**The fix, and what changed.** With `orders` first, all five booked orders are on the statement and
T-4 shows NULL where its payment would be, which is exactly the line Anand needs to see. P-7 left
the statement, since it belongs to the platform lead's question. The statement still has seven
lines for five orders, with T-2 and T-3 listed twice each. Read line by line, T-2 looks short-paid
on both of its lines, 1,200 of 2,000 on one and 800 of 2,000 on the other, when it was paid in full.
Before any total is read from this join, chapter 2 has to answer what a total does to an order
that appears twice.

Kavya Nair, the team's senior analyst, reviews every number before it leaves the team.

> **Kavya's review.** "Tell me the grain of each table, and which rows your join drops, before you
> tell me any total. Start from the table whose every row must survive."
"""),
        md("""
## Can the row counts be predicted from the keys alone, before any join runs?

A join's row count follows from how often each key appears on each side. For a key that appears
`a` times in `orders` and `b` times in `payments`, an INNER JOIN writes `a x b` rows. LEFT adds one
row for every order key that matched nothing, RIGHT one for every payment key that matched nothing,
and FULL both. The cell below counts the keys on each side without joining anything, predicts all
four counts, and compares them with the joins run above.
"""),
        code(f"""
keys = run(\"\"\"{Q1['key_counts']}\"\"\")
show(keys, "How often each key appears on each side, counted without a join")
inner_p = sum(k["rows_in_orders"] * k["rows_in_payments"] for k in keys)
left_p = inner_p + sum(k["rows_in_orders"] for k in keys if k["rows_in_payments"] == 0)
right_p = inner_p + sum(k["rows_in_payments"] for k in keys if k["rows_in_orders"] == 0)
full_p = left_p + right_p - inner_p
predicted = {{"INNER": inner_p, "LEFT": left_p, "RIGHT": right_p, "FULL": full_p}}
kit.columns(list(predicted), [("predicted from the keys", list(predicted.values())),
                              ("returned by the join", [counts[k] for k in predicted])],
            title="The keys predict every join's row count")
kit.check("the key counts predict all four joins exactly", predicted == counts, str(predicted))"""),
        md("""
**What happened.** The keys predict 6, 7, 7 and 8, the same four counts the joins returned, and the
prediction never ran a join. This is the second route to use before any join on real data: count
the keys on each side first, and the join's row count is known before it runs. It fails in one
place only, when the join condition is more than key equality, such as the date condition chapter 4
meets; there the prediction has to include the condition.

### In the interview: what does each join keep, and when is an INNER join the honest choice?

The tags mark how often a question comes up: [S] a staple asked everywhere, [F] frequent in GCC and product screens, [D] a differentiator.

**[S] INNER against LEFT join: what does each drop or keep?** An INNER JOIN keeps only the rows that match on both sides and drops the rest from both tables. A
LEFT JOIN keeps every row of the left table and fills the right-hand columns with NULL where nothing
matched. Both repeat a left row once for every matching right row, and that last clause is the one
an interviewer is listening for, because it is where a total goes wrong.

**[S] When is an INNER join the honest choice?** It is honest when the unmatched rows are outside the question by definition, and the report says so: "for the
orders that were paid, how many days passed before the first payment?" asks only about matches. For
Anand's question it is dishonest, since his question is about every booked order, paid or not.

### Depth: why does a RIGHT JOIN rarely appear in production code?

A RIGHT JOIN is a LEFT JOIN with the two tables swapped, so most teams write every outer join as a
LEFT JOIN with the table whose rows must all survive written first. The query then reads in the
order of the question: start from what must be kept, attach what may be missing.
"""),
        md("""
## What did this chapter answer, one line per question?

1. The LEFT JOIN with orders first answers Anand, since it alone keeps all five booked orders and
   nothing that is not an order.
2. One row of `orders` is one order, 1,000 of them; one row of `payments` is one payment event, and
   an order id holds up to two of the 1,428 payment rows.
3. On five orders and seven payments, INNER returns 6 rows, LEFT 7, RIGHT 7 and FULL 8.
4. A statement started from payments shows 4 of the 5 booked orders and 7,100 of cash against 5,800
   booked, because it drops the unpaid order and carries a retry and a payment with no order.
5. The key counts predict all four row counts without a join: 6, 7, 7 and 8.

**The question this leaves.** The chosen LEFT JOIN still lists T-2 and T-3 twice, so chapter 2 asks
what a total over those rows reports on Kalpa's Q2.
"""),
        code("kit.check_summary()"),
    ]
    build(nb_path(n), cells)
    write_sql(n, ["Two invented tables first, traced by hand, then the warehouse's grain.",
                  "The tiny tables are TEMP tables, so they vanish when the session ends."],
              [("Setup: the two invented tables", TINY),
               ("What is one row of each warehouse table?", Q1["grain"]),
               ("How many payment rows does one order id hold at most?", Q1["most_rows"]),
               ("How many rows does the INNER join return, and which?", Q1["inner"]),
               ("How many rows does each of the four joins return?", Q1["counts"]),
               ("The trap: what does a statement started from payments show?", Q1["payments_first"]),
               ("The fix: what does the statement show with orders first?", Q1["orders_first"]),
               ("The second route: how often does each key appear on each side?", Q1["key_counts"])])
    print("chapter 1 written")


# ============================================================================================== 2
Q2 = {
    "largest": """
SELECT o.order_id, o.channel, o.status, o.amount AS booked,
       count(p.payment_id) AS payment_rows,
       string_agg(p.instalment_no::text, ' and ' ORDER BY p.instalment_no) AS instalments
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.order_id, o.channel, o.status, o.amount
ORDER BY o.amount DESC
LIMIT 10""",
    "booked": """
SELECT count(*) AS orders, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q2'""",
    "draft": """
SELECT count(*)                                              AS rows_out,
       sum(o.amount) FILTER (WHERE p.payment_id IS NOT NULL) AS collected
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'""",
    "draft_by_channel": """
SELECT o.channel,
       count(*)                                              AS rows_out,
       sum(o.amount) FILTER (WHERE p.payment_id IS NOT NULL) AS collected
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.channel
ORDER BY o.channel""",
    "booked_by_channel": """
SELECT channel, count(*) AS orders, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q2'
GROUP BY channel
ORDER BY channel""",
    "one_order": """
SELECT o.order_id, o.amount AS booked, p.payment_id, p.instalment_no, p.amount AS paid
FROM orders o
JOIN payments p ON p.order_id = o.order_id
WHERE o.order_id = 'KR-00595'
ORDER BY p.instalment_no""",
    "option_a": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted, count(*) AS payment_rows
    FROM payments
    GROUP BY order_id
)
SELECT o.order_id, o.channel, o.amount AS booked, pp.posted, pp.payment_rows
FROM orders o
LEFT JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2'""",
    "option_b": """
SELECT count(*) AS rows_out, sum(DISTINCT o.amount) AS booked_distinct
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'""",
    "shared_amounts": """
SELECT count(*) AS orders_sharing_an_amount, count(DISTINCT amount) AS distinct_amounts
FROM orders o
WHERE quarter = 'Q2'
  AND (SELECT count(*) FROM orders o2 WHERE o2.quarter = 'Q2' AND o2.amount = o.amount) > 1""",
    "posted_alone": """
SELECT sum(amount) AS posted
FROM payments
WHERE order_id IN (SELECT order_id FROM orders WHERE quarter = 'Q2')""",
}

CH2_STEPS = ["the need: what does a double count cost Anand?", "which orders own two payment rows",
             "the first draft: Rs 19.29 crore collected", "why every right row adds up wrong",
             "the options: four ways, sized", "the fix: one row per order, then join",
             "a second route: each table summed alone"]


def chapter2():
    n = 2
    ladder = ["Which Kalpa orders own two payment rows, and why?",
              "What does a first draft of collected report for Q2?",
              "Why is the first draft wrong when every row on it is right?",
              "Which of four ways stops the double count, and what does each cost on this data?",
              "Does the chosen way keep 462 orders and Rs 9,84,00,000 booked?",
              "Do the two tables, each summed alone, agree with the fixed join?"]
    cells = [
        title_cell(
            n,
            "Anand would read a collected figure twice his books as a quarter of collections running "
            "ahead and stand his collections team down. The data platform lead hears about a wrong "
            "number from the warehouse before anyone else does, and you need it because the way "
            "chosen here carries every later chapter of the day.",
            ladder,
            "Collected revenue for Q2 is set against booked revenue for Q2. Booked is every Q2 "
            "order at its amount, whatever its status, Rs 9,84,00,000 over 462 orders, and "
            "collected can never honestly exceed it.",
            "Chapter 1 traced five invented orders and seven invented payments. The LEFT JOIN with "
            "orders first was the only join that kept every booked order, and it still listed two "
            "orders twice: T-2, paid in two instalments, and T-3, whose payment the gateway posted "
            "twice, so seven lines described five orders. This chapter runs the same join on Kalpa's "
            "Q2 and reads a total from it."),
        md("""
**Setup.** The next cell finds the helper and connects to the warehouse; it also creates chapter 1's
invented tables, as every chapter's setup does, though this chapter runs on Kalpa's Q2 alone. Every
query below is also in `sql/C2_W02_D02_02_why_twice_booked_STUDENT.sql`.
"""),
        code(HELPERS + f"""
booked_q2 = run(\"\"\"{Q2['booked']}\"\"\")[0]
print(f'Q2 books {{booked_q2["orders"]}} orders and {{kit.rupees(booked_q2["booked"])}}, '
      "counted from the orders table alone, as on Monday.")"""),
        map_cell(n, CH2_STEPS),
        md(f"""
## What does Anand lose if collected is counted twice?

A finance controller reads collected against booked to decide where his collections team spends
the next week. If collected comes out above booked, the sentence that follows is "we are collecting
ahead of bookings", and the team is stood down in the very quarter Anand is asking about. If a
figure twice his books ever reaches Meera Raghavan, the CEO, in the Monday pack, it has to be
withdrawn in front of her, and every later number from the warehouse is read with doubt. The cost
of this chapter's mistake is the week of collections work lost and the trust spent. {DOSSIER}
"""),
        md(COMPANY[2] or "**Who else faces this.** (filled from the provenance)"),
        md("""
## 1. Which Kalpa orders own two payment rows, and why?

Chapter 1 found that an order id holds up to two payment rows in the warehouse. Which orders are
they?

**Predict before you run.** Among Q2's ten largest orders, how many carry two payment rows?
a) none, large orders are paid once; b) all ten, with instalments 1 and 2; c) the cancelled ones
only; d) about half, at random.
"""),
        code(f"""
largest = run(\"\"\"{Q2['largest']}\"\"\")
show([{{"rank by amount": i, "channel": r["channel"], "status": r["status"],
        "payment rows": r["payment_rows"], "instalments": r["instalments"]}} for i, r in enumerate(largest, 1)],
     "Q2's ten largest orders and their payment rows")
kit.columns(["1 payment row", "2 payment rows"],
            [("Q2's ten largest orders", [sum(1 for r in largest if r["payment_rows"] == 1),
                                         sum(1 for r in largest if r["payment_rows"] == 2)])],
            title="Q2's ten largest orders, counted by payment rows")"""),
        md("""
**What happened.** The answer is b. Every one of Q2's ten largest orders carries two payment rows,
instalment 1 and instalment 2: large business invoices at Kalpa are settled in two parts, as Anand
said, so each order owns two payment rows and comes out of a join twice.
"""),
        code("""
kit.check("each of the ten largest Q2 orders carries two payment rows",
          all(r["payment_rows"] == 2 for r in largest), f'{len(largest)} orders')
kit.check("every one of the ten is paid in instalments 1 and 2",
          all(r["instalments"] == "1 and 2" for r in largest), "instalments 1 and 2")"""),
        md("""
## 2. What does a first draft of collected report for Q2?

**The plausible wrong answer.** A teammate writes the first draft. It keeps every Q2 order, as
chapter 1 taught, with a LEFT JOIN to `payments`, and it counts an order as collected, at its booked
amount, whenever a payment row sits beside it. `FILTER (WHERE ...)`, which Monday used, restricts one
aggregate to the rows that meet a condition.

```sql
SELECT count(*)                                              AS rows_out,
       sum(o.amount) FILTER (WHERE p.payment_id IS NOT NULL) AS collected
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2';
```

**Predict before you run.** Against Rs 9,84,00,000 booked, what does the draft report as collected?
a) a little under Rs 9.84 crore, since some orders may be unpaid; b) exactly Rs 9.84 crore;
c) about Rs 19.3 crore; d) about Rs 4.9 crore.
"""),
        code(f"""
draft = run(\"\"\"{Q2['draft']}\"\"\")[0]
kit.stats([(kit.rupees(draft["collected"]), "collected, first draft", "the order amount beside each payment row"),
           (kit.rupees(booked_q2["booked"]), "booked", "Monday's number, orders alone"),
           (f'{{draft["collected"] / booked_q2["booked"]:.2f}} x', "collected over booked", "which cannot be")])
by_ch = run(\"\"\"{Q2['draft_by_channel']}\"\"\")
bk_ch = {{r["channel"]: r for r in run(\"\"\"{Q2['booked_by_channel']}\"\"\")}}
kit.columns([r["channel"] for r in by_ch],
            [("booked", [float(bk_ch[r["channel"]]["booked"]) / 1e7 for r in by_ch]),
             ("collected, first draft", [float(r["collected"]) / 1e7 for r in by_ch])],
            fmt=lambda v: f"{{v:.2f}} cr", title="The first draft reports every channel near twice its bookings")"""),
        md("""
**What happened.** The answer is c: Rs 19,29,04,410 collected against Rs 9,84,00,000 booked, 1.96
times, and every channel sits near twice its bookings. Read as it stands, the draft says Kalpa
collected Rs 9.45 crore more than it sold, and a finance controller who believes it stops chasing
anything this quarter.
"""),
        md("""
## 3. Why is the first draft wrong when every row on it is right?

**Why it is wrong.** Every row of the draft is a real order beside a real payment, and no row is
wrong. The error lives in the sum: an order that owns two payment rows is written twice, and its
booked amount rides along on both rows, so `sum(o.amount)` counts it twice. A sum over a join is a
sum at the join's grain, which here is the payment, whatever column it names. This is a fan-out: a
key that repeats on one side multiplies the rows of the other. dbt Labs names the same mechanism in
its MetricFlow documentation: "Fan-out joins are when one row in a table is joined to multiple rows
in another table, resulting in more output rows than input rows", and MetricFlow "restricts the use
of fan-out and chasm joins" (docs.getdbt.com, Joins, last updated 8 Sep 2026, checked 1 Oct 2026).

**The check that catches it.** Either of two checks is enough. Count the rows the join returns
against the orders that went in, and compare collected with booked, since cash against bookings can
never honestly exceed them.
"""),
        code(f"""
kr595 = run(\"\"\"{Q2['one_order']}\"\"\")
show(kr595, "KR-00595, one order, two payment rows after the join", money=["booked", "paid"])
kit.flow(["KR-00595\\nbooked once, Rs 4,01,000", "row 1\\ninstalment 1", "row 2\\ninstalment 2",
          "sum(o.amount)\\ncounts Rs 8,02,000"], kinds=["known", "plain", "plain", "bad"],
         title="The order amount rides along on every payment row")
kit.check("the join returns more rows than Q2 has orders", draft["rows_out"] > booked_q2["orders"],
          f'{{booked_q2["orders"]}} orders in, {{draft["rows_out"]}} rows out')
kit.check("the draft's collected exceeds booked, which cash cannot do",
          draft["collected"] > booked_q2["booked"], f'{{draft["collected"] / booked_q2["booked"]:.2f}} times')
kit.check("KR-00595 alone is summed twice by the draft",
          sum(r["booked"] for r in kr595) == 2 * kr595[0]["booked"], kit.rupees(2 * kr595[0]["booked"]))"""),
        md("""
## Which of four ways stops the double count, and what does each cost on this data?

The doubling has two possible sources, and a fix has to say which one it removes: legitimate second
instalments, which are real cash, and repeated postings of one payment, which the platform lead
warned about. A team could stop the double count in four ways:

| Option | How it works | What it assumes |
|---|---|---|
| A. Bring payments to one row per order, then join | A CTE sums each order's payment rows into one row, `posted`, and keeps `payment_rows`; the LEFT JOIN then meets orders at their own grain | Nothing beyond the key |
| B. DISTINCT after the join | `sum(DISTINCT o.amount)` adds each different amount once | That no two orders share an amount |
| C. A window dedupe | Keep the first posting of each order and instalment with a window function, which Wednesday teaches | That a repeat of the same instalment is a retry |
| D. Fix the feed | The platform lead makes the gateway post a retried payment once, with an idempotency key, a request id the gateway uses to refuse a repeat | Weeks of platform work, and nothing done to Q2 as posted |

The cell below runs A and B on Kalpa's Q2 and times them; C needs a tool this room meets tomorrow and
D is a request, so their columns say what each would do.
"""),
        code(f"""
import time
t0 = time.perf_counter()
fixed = run(\"\"\"{Q2['option_a']}\"\"\")
t_a = time.perf_counter() - t0
t0 = time.perf_counter()
opt_b = run(\"\"\"{Q2['option_b']}\"\"\")[0]
t_b = time.perf_counter() - t0
shared = run(\"\"\"{Q2['shared_amounts']}\"\"\")[0]
booked_a = sum(r["booked"] for r in fixed)
kit.table(["Option", "Rows out for 462 orders", "Booked after it", "Error against booked", "Time"],
          [("A. one row per order, then join", len(fixed), kit.rupees(booked_a),
            kit.rupees(booked_a - booked_q2["booked"]), f"{{t_a * 1000:.1f}} ms"),
           ("B. sum(DISTINCT o.amount)", f'{{opt_b["rows_out"]}}, one sum', kit.rupees(opt_b["booked_distinct"]),
            kit.rupees(opt_b["booked_distinct"] - booked_q2["booked"]), f"{{t_b * 1000:.1f}} ms"),
           ("C. window dedupe", "more than 462", "still inflated", "every two-instalment order keeps two rows",
            "needs Wednesday's tool"),
           ("D. fix the feed", "no change to Q2", "no change", "Q2 stays as posted", "weeks of platform work")],
          caption="Four ways to stop the double count, sized on Kalpa's Q2")
kit.bars([("Monday's booked", float(booked_q2["booked"]) / 1e7), ("A. one row per order", float(booked_a) / 1e7),
          ("B. DISTINCT amount", float(opt_b["booked_distinct"]) / 1e7)], lit=[1],
         fmt=lambda v: f"Rs {{v:.4f}} cr", title="Booked after each fix, against Monday's Rs 9.84 crore")
print(f'{{shared["orders_sharing_an_amount"]}} of Q2\\'s 462 orders share their amount with another order, '
      f'across {{shared["distinct_amounts"]}} amounts that repeat.')"""),
        md("""
**The best-fit call.** Option A fits best. It returns one row for each of the 462 orders with booked exactly
Monday's figure, it keeps every order whether paid or not, and it keeps `payment_rows`, so a
repeated posting stays visible for chapter 4 instead of vanishing. B looks as if it works and loses
Rs 20,32,780 of real bookings, because DISTINCT removes repeated values and a repeated value is not
a repeated order: 243 of the 462 orders share their amount with another. C removes only repeats of
the same instalment, so every order paid in two instalments still comes out twice and the draft
stays inflated. D is the right request to make of the platform lead, and it changes nothing about
the quarter Anand asked for. Both A and B take a few milliseconds, so the choice is about what each
gets wrong.

**The fact that would change the call.** A feed that carried the gateway's own transaction reference
on every row, repeated on a retry, would let a DISTINCT on that reference remove retries before any
join, exactly. And if Anand asked per payment, say to match each line of the bank statement, the
payment would be the right grain and nothing would be summed first.
"""),
        md("""
## 4. Does the chosen way keep 462 orders and Rs 9,84,00,000 booked?

```sql
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted, count(*) AS payment_rows
    FROM payments
    GROUP BY order_id
)
SELECT o.order_id, o.channel, o.amount AS booked, pp.posted, pp.payment_rows
FROM orders o
LEFT JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2';
```

`posted` is everything the feed holds against an order, instalments and any repeat alike, and an
order with no payment row gets NULL there.

**Predict before you run.** How many rows does it return? a) 678; b) 462; c) 216; d) 1,000.
"""),
        code("""
kit.stats([(f"{len(fixed)}", "rows out", "one per Q2 order"),
           (kit.rupees(booked_a), "booked after the join", "Monday's figure"),
           (f'{len({r["order_id"] for r in fixed})}', "distinct orders", "none repeated")])
kit.flow(["payments\\nmany rows per order", "GROUP BY order_id\\none row per order",
          "LEFT JOIN\\norders first", "462 rows out\\nequals 462 in"],
         kinds=["bad", "plain", "plain", "good"], title="The fix: meet orders at their own grain")
kit.check("the fixed join returns one row per Q2 order", len(fixed) == booked_q2["orders"],
          f'{len(fixed)} out, {booked_q2["orders"]} in')
kit.check("booked after the fixed join equals Monday's booked", booked_a == booked_q2["booked"],
          kit.rupees(booked_a))
kit.check("no order appears twice", len({r["order_id"] for r in fixed}) == len(fixed), f"{len(fixed)}")"""),
        md("""
**What happened.** The answer is b: 462 rows for 462 orders, and booked after the join is
Rs 9,84,00,000, Monday's figure to the rupee. The 216 extra rows are gone, and the order amount is
summed once per order. The `posted` column now holds what the feed recorded against each order.

**Your turn.** Read the total yourself. In the empty cell below, type these lines and run them:

```python
posted_total = sum(r["posted"] for r in fixed if r["posted"] is not None)
print(kit.rupees(posted_total))
```

Write the figure down as "posted against Q2 orders". Chapter 3 asks what it is made of, and whether
it is the collected figure Anand asked for.
"""),
        empty(),
        md("""
Kavya Nair, the team's senior analyst, reviews every number before it leaves the team.

> **Kavya's review.** "A join is a multiplication until you prove it is not. Bring the many side to
> the grain of the question before you join, and show me rows in and rows out beside the total."
"""),
        md("""
## Do the two tables, each summed alone, agree with the fixed join?

The second route never joins. Booked comes from `orders` alone; posted comes from `payments` alone,
restricted to Q2's order ids with `IN`, so no order can be counted twice by a join. If the fixed
join added or lost anything, one of the two would disagree with it.
"""),
        code(f"""
posted_alone = one(\"\"\"{Q2['posted_alone']}\"\"\")
posted_join = sum(r["posted"] for r in fixed if r["posted"] is not None)
kit.side_by_side(
    kit.vflow(["orders alone\\nQ2 rows", "sum(amount)\\nbooked", "compare"],
              kinds=["known", "plain", "good"], show=False),
    kit.vflow(["payments alone\\norder_id IN Q2's orders", "sum(amount)\\nposted", "compare"],
              kinds=["known", "plain", "good"], show=False),
    kit.vflow(["the fixed join\\n462 rows", "booked and posted\\nsummed once per order", "compare"],
              kinds=["bad", "plain", "good"], show=False),
)
kit.check("booked from orders alone equals booked after the fixed join", booked_a == booked_q2["booked"],
          kit.rupees(booked_q2["booked"]))
kit.check("posted from payments alone equals posted after the fixed join", posted_alone == posted_join,
          "equal to the rupee")"""),
        md("""
**What happened.** Both routes agree: booked is Rs 9,84,00,000 by each, and posted from `payments`
alone equals the fixed join's posted to the rupee. The second route would catch a fan-out the first
missed, because it sums each table at its own grain and never multiplies anything.

### In the interview: why did revenue double after a join, and what made the row count grow?

The tags mark how often a question comes up: [S] a staple asked everywhere, [F] frequent in GCC and product screens, [D] a differentiator.

**[F] Revenue doubled after a join and every row looks fine; where do you look?** Look at the grain. Each row is right, and the sum runs at the join's grain, so the first
question is which key repeats on the many side. Count rows before and after the join, list the keys
that repeat with `GROUP BY key HAVING count(*) > 1` on the many side, then bring that side to the
key's grain in a CTE before joining, and prove it with rows in equal to rows out and the total
recomputed from the source table alone.

**[S] Your join grew the row count; name the cause and the check.** The cause is a key that is unique on one side and repeats on the other, usually a one-to-many
relationship read as one-to-one. The check is the count before and after the join, plus a count of
the repeated keys on the many side; the growth must equal the extra rows those keys explain, or
something else is wrong too.

### Depth: why is SUM(DISTINCT ...) a tempting fix that fails?

It makes the doubled number go away, which feels like proof. It removes repeated values, and two
different orders of the same amount are two orders: on Kalpa's Q2 it loses Rs 20,32,780 of real
bookings. It would also remove a genuine second payment that happened to match the first. A fix
that works on the grain says which rows it merged and why; DISTINCT cannot say either.
"""),
        md("""
## What did this chapter answer, one line per question?

1. Kalpa's large business invoices are paid in two instalments, so every one of Q2's ten largest
   orders owns two payment rows, instalment 1 and instalment 2.
2. The first draft reports Rs 19,29,04,410 collected against Rs 9,84,00,000 booked, 1.96 times.
3. It is wrong because the order amount rides on every payment row, so 462 orders become 678 rows
   and the sum runs at the payment's grain.
4. Bringing payments to one row per order before the join is the best fit; DISTINCT loses
   Rs 20,32,780 of bookings, a window dedupe leaves the instalments doubled, and a feed fix changes
   nothing about Q2.
5. The fixed join returns 462 rows and Rs 9,84,00,000 booked, Monday's figures exactly.
6. Each table summed alone agrees with it, for booked and for posted.

**The question this leaves.** The fixed join keeps every order, and its `posted` column is what the
feed recorded. Chapter 3 asks whether every booked order is still there when the report is written,
and what, rupee by rupee, separates booked from posted.
"""),
        code("kit.check_summary()"),
    ]
    build(nb_path(n), cells)
    write_sql(n, ["The warehouse's Q2 orders joined to payments: the first draft, why it doubles, "
                  "and the fix at order grain."],
              [("Q2's booked, from orders alone (Monday's number)", Q2["booked"]),
               ("Which Q2 orders own two payment rows, and why?", Q2["largest"]),
               ("The trap: what does the first draft report as collected?", Q2["draft"]),
               ("The first draft by channel", Q2["draft_by_channel"]),
               ("Booked by channel, from orders alone", Q2["booked_by_channel"]),
               ("One order, two payment rows: KR-00595", Q2["one_order"]),
               ("Option B, sized: what does DISTINCT on the amount return?", Q2["option_b"]),
               ("Why DISTINCT fails: how many Q2 orders share an amount?", Q2["shared_amounts"]),
               ("The fix, option A: one row per order, then join", Q2["option_a"]),
               ("The second route: posted from payments alone, Q2 order ids", Q2["posted_alone"])])
    print("chapter 2 written")



# ============================================================================================== 3
# One per-order table carries the whole bridge: booked from orders, and from payments the cash
# collected (each order and instalment counted once) and everything posted (every row).
PER_ORDER = """
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount
    FROM {payments}
    GROUP BY order_id, instalment_no
),
collected_per_order AS (
    SELECT order_id, sum(amount) AS collected
    FROM per_instalment
    GROUP BY order_id
),
posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM {payments}
    GROUP BY order_id
)
SELECT o.order_id, o.channel, o.amount AS booked, c.collected, p.posted
FROM {orders} o
LEFT JOIN collected_per_order c ON c.order_id = o.order_id
LEFT JOIN posted_per_order p    ON p.order_id = o.order_id
{where}"""

BRIDGE_SQL = """
WITH per_order AS ({per_order})
SELECT sum(booked)                                                    AS booked,
       sum(booked) FILTER (WHERE collected IS NULL)                   AS never_paid,
       coalesce(sum(booked - collected) FILTER (WHERE collected < booked), 0) AS paid_short,
       sum(collected)                                                 AS collected,
       sum(posted - collected)                                        AS posted_twice,
       sum(posted)                                                    AS posted
FROM per_order"""


def per_order(orders, payments, where=""):
    return PER_ORDER.format(orders=orders, payments=payments, where=where).strip("\n")


def bridge_sql(orders, payments, where=""):
    return BRIDGE_SQL.format(per_order="\n" + per_order(orders, payments, where) + "\n").strip("\n")


Q3 = {
    "order_grain": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM payments
    GROUP BY order_id
)
SELECT count(*) AS rows_out, count(DISTINCT o.order_id) AS orders_out, sum(o.amount) AS booked
FROM orders o
LEFT JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2'""",
    "tiny_inner": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS posted,
       sum(o.amount) - sum(pp.posted) AS gap
FROM tiny_orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id""",
    "tiny_left": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS posted,
       sum(o.amount) - sum(pp.posted) AS gap
FROM tiny_orders o
LEFT JOIN posted_per_order pp ON pp.order_id = o.order_id""",
    "kalpa_inner": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS posted
FROM orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2'""",
    "tiny_per_order": per_order("tiny_orders", "tiny_payments", "ORDER BY o.order_id"),
    "tiny_bridge": bridge_sql("tiny_orders", "tiny_payments"),
    "kalpa_bridge": bridge_sql("orders", "payments", "WHERE o.quarter = 'Q2'"),
    "posted_alone": """
SELECT sum(amount) AS posted
FROM payments
WHERE order_id IN (SELECT order_id FROM orders WHERE quarter = 'Q2')""",
    "tiny_cap": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT o.order_id, o.amount AS booked, pp.posted, least(pp.posted, o.amount) AS capped
FROM tiny_orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id
ORDER BY o.order_id""",
    "kalpa_cap": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM payments
    GROUP BY order_id
)
SELECT sum(least(pp.posted, o.amount)) AS collected_by_cap
FROM orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2'""",
}

CH3_STEPS = ["the need: which order is missing?", "the options: four proofs, sized",
             "rows in, rows out at order grain", "the trap: a plain JOIN reports a surplus",
             "the check that reads no rupee", "the bridge: booked to posted",
             "a second route: cap each order at its booked"]


def chapter3():
    n = 3
    ladder = ["Which of four proofs shows Anand the gap is honest, and which runs first?",
              "Once payments are one row per order, can the report gain rows, or only lose them?",
              "What does a first draft with a plain JOIN report on the invented tables?",
              "Which check catches the dropped order without reading a rupee?",
              "Which moves carry booked to what the feed posted, and does the bridge close on Kalpa's Q2?",
              "Does collected come out the same when each order's posted cash is capped at its "
              "booked amount?"]
    cells = [
        title_cell(
            n,
            "Anand asked which orders make the gap, so an order missing from the report is an "
            "order nobody chases, and Anand's analyst reads the reconciliation written above "
            "the number before the number itself. A report that loses an order and carries a "
            "repeated payment can show a surplus, or a gap that looks closed, and nobody chases an "
            "order on a page that reads fully collected.",
            ladder,
            "The gap between booked and collected is at stake, with what can sit inside it: orders "
            "never paid, orders paid short and payments posted twice. Collected is the cash that "
            "arrived, each payment counted once; posted is every payment row the feed holds, "
            "repeats included.",
            "Chapter 2 found that the first draft of collected, Rs 19,29,04,410 against Rs 9,84,00,000 "
            "booked, counted every two-instalment order twice, and fixed it by bringing payments to "
            "one row per order before the join: 462 Q2 orders in, 462 rows out, booked equal to "
            "Monday's figure, and a `posted` column holding what the feed recorded against each order. "
            "This chapter proves the fixed report kept every order and names every rupee between "
            "booked and posted."),
        md("""
**Setup.** The next cell finds the helper, connects to the warehouse and creates the invented tables
of chapter 1. Every query below is also in `sql/C2_W02_D02_03_every_order_there_STUDENT.sql`.
"""),
        code(HELPERS + """
print("Invented: T-1 to T-5 booked 5,800 in all; P-1 to P-7 are the feed's rows.")"""),
        map_cell(n, CH3_STEPS),
        md(f"""
## Why is a missing order worse for Anand than a wrong total?

A wrong total is visible: it disagrees with Monday's booked figure, or it breaks a rule such as cash
exceeding bookings, and someone asks. A missing order is invisible, because every number left in the
report is correct for the orders that remain. Anand asked "which orders", and the one order a report
drops is precisely the order his collections team never rings. When a repeated payment inside
collected offsets the dropped order, the report can show a surplus, or a gap that looks closed, and
either reads as "fully collected". {DOSSIER}
"""),
        md(COMPANY[3]),
        md(TINY_NOTE),
        md("""
## Which of four proofs shows Anand the gap is honest, and what does each catch?

A team could prove the report in four ways before Anand reads it. The cell below runs each one
against a first draft on the invented tables that carries two errors at once: it joined with a
plain JOIN, and it counts T-3's repeated payment inside collected.

| Option | What Anand reads | What it assumes |
|---|---|---|
| A. One number, booked less posted | A single gap | That the join kept every order and posted nothing twice |
| B. The count reconciliation: rows in, rows out, the difference named | Four comment lines above the number | That a correct count means a correct total |
| C. The bridge: booked, each move named, down to what the feed posted, with a list behind each move | Five bars and the lists | That every move has a definition |
| D. The whole statement, one line per order | Every order | That someone reads every line |
"""),
        code(f"""
draft = run(\"\"\"{Q3['tiny_inner']}\"\"\")[0]
tiny_orders_n = one("SELECT count(*) FROM tiny_orders")
tiny_booked = one("SELECT sum(amount) FROM tiny_orders")
sizing = [
    ("A. one number", f'gap {{int(draft["gap"]):,}}', "1", "no", "no"),
    ("B. count reconciliation", f'{{draft["orders"]}} of {{tiny_orders_n}} orders', "4", "yes", "no"),
    ("C. the bridge with its lists", "never paid 800, posted twice 1,500", "5 bars and 2 lists", "yes", "yes"),
    ("D. the whole statement", "5 lines, T-4 empty, T-3 twice", "every line", "if read", "if read"),
]
kit.table(["Option", "What it shows on the draft", "Lines Anand reads", "Catches the dropped order",
           "Catches the repeat inside"], sizing, caption="Four proofs, run against a draft with two errors")
kit.matrix(["A. one number", "B. count", "C. bridge", "D. statement"],
           ["the dropped order", "the repeat inside collected"],
           [["missed", "missed"], ["caught", "missed"], ["caught", "caught"], ["caught if read", "caught if read"]],
           title="What each proof catches on the invented draft")
kit.check("the draft reports fewer orders than the table holds", draft["orders"] < tiny_orders_n,
          f'{{draft["orders"]}} of {{tiny_orders_n}}')"""),
        md("""
**The best-fit call.** Run B, then C: the count reconciliation first, because it needs no rupee and
catches a dropped or repeated order in one line, then the bridge, because it is the only proof here
that separates an unpaid order from a payment posted twice and puts a list of orders behind each
move. A single number hides both errors, and the whole statement catches everything only if Anand's
analyst reads 462 lines. All four cost seconds to compute, so they differ in what the reader can
check.

**The fact that would change the call.** If Anand's analyst had to tick every order for the audit
file at the quarter's close, D would travel with the report as an appendix; chapter 4's two lists
are its short form.
"""),
        md("""
## 1. Once payments are one row per order, can the report gain rows, or only lose them?

**Predict before you run.** After chapter 2's fix, `payments` meets `orders` one row per order.
What can the join now do to the row count? a) gain rows, whenever an order has two instalments;
b) only lose rows, and only if the join drops an order; c) nothing, a join always returns the left
table's rows; d) gain rows, whenever a payment has no order.
"""),
        code(f"""
grain_q2 = run(\"\"\"{Q3['order_grain']}\"\"\")[0]
booked_q2 = one("SELECT sum(amount) FROM orders WHERE quarter = 'Q2'")
orders_q2 = one("SELECT count(*) FROM orders WHERE quarter = 'Q2'")
kit.table(["Reconciliation line", "What it says on Kalpa's Q2"],
          [("Rows in", f"{{orders_q2}} Q2 orders, {{kit.rupees(booked_q2)}} booked, from orders alone"),
           ("Rows out", f'{{grain_q2["rows_out"]}} rows, {{grain_q2["orders_out"]}} distinct orders, at order grain'),
           ("Booked after the join", f'{{kit.rupees(grain_q2["booked"])}}, equal to booked before it'),
           ("The gap", "booked less collected, each rupee named: yours to fill in level 5")],
          caption="The reconciliation, written above the number")
kit.vflow(["rows in\\n462 orders", "the join at order grain", "rows out\\nequal, or name the difference",
           "then the number"], kinds=["known", "plain", "good", "plain"],
          title="A join at the same grain can only lose rows")"""),
        md("""
**What happened.** The answer is b. A row of `orders` now meets at most one row of payments, so no
order can come out twice; the only way the count can move is down, when the join drops an order
that found no match. On Kalpa's Q2 the LEFT JOIN returns 462 rows for 462 orders and booked after
the join equals Rs 9,84,00,000, so nothing was dropped or repeated.
"""),
        code("""
kit.check("rows out equal rows in at order grain", grain_q2["rows_out"] == orders_q2,
          f'{grain_q2["rows_out"]} out, {orders_q2} in')
kit.check("no order appears twice", grain_q2["orders_out"] == grain_q2["rows_out"], f'{grain_q2["orders_out"]}')
kit.check("booked after the join equals booked from orders alone", grain_q2["booked"] == booked_q2,
          kit.rupees(booked_q2))"""),
        md("""
## 2. What does a first draft with a plain JOIN report on the invented tables?

**The plausible wrong answer.** A teammate takes chapter 2's fix and writes `JOIN`, which in SQL
means INNER JOIN, instead of `LEFT JOIN`: a very common first draft, since `JOIN` is the shortest
thing to type. Payments are one row per order, so nothing is counted twice by the join.

```sql
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted FROM tiny_payments GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS posted,
       sum(o.amount) - sum(pp.posted) AS gap
FROM tiny_orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id;
```

**Predict before you run.** Booked across the five invented orders is 5,800. What gap does the draft
report? a) 800; b) 0; c) minus 1,500; d) minus 700.
"""),
        code("""
kit.stats([(f'{draft["orders"]}', "orders in the report", "of 5 in the table"),
           (f'{int(draft["booked"]):,}', "booked, as reported", "of 5,800"),
           (f'{int(draft["posted"]):,}', "posted, as reported", "every payment row matched"),
           (f'{int(draft["gap"]):,}', "gap, as reported", "reads as fully collected, with a surplus")])
kit.columns(["booked", "posted"], [("the draft", [float(draft["booked"]), float(draft["posted"])]),
                                   ("the table", [float(tiny_booked), float(draft["posted"])])],
            title="Invented: the draft's booked lost 800 and its posted kept a repeat")"""),
        md("""
**What happened.** The answer is c: four orders, booked 5,000, posted 6,500, a gap of minus 1,500. The
report says Kalpa collected everything it booked and 1,500 more.

**Why it is wrong.** Two errors cancel into a comfortable number. The plain JOIN dropped T-4, the
one order nobody paid, so 800 of booked vanished with it; and T-3's payment, posted twice by the
gateway, puts 1,500 inside posted that never came in twice. Anand, reading "no gap, and a surplus",
stops chasing T-4 and never asks why the feed shows more cash than was booked.
"""),
        md("""
## 3. Which check catches the dropped order without reading a rupee?

**The check that catches it.** Count the orders in the report against the orders in the table. The
report holds 4; the table holds 5. The count needs no rupee at all, which is why it runs first and
every time: a LEFT JOIN at order grain must return exactly the orders it was given.

**The fix, and what changed.** `LEFT JOIN` in place of `JOIN` brings T-4 back, with NULL where its
posted cash would be.
"""),
        code(f"""
fixed = run(\"\"\"{Q3['tiny_left']}\"\"\")[0]
kit.table(["Draft", "Orders", "Booked", "Posted", "Gap"],
          [("plain JOIN", draft["orders"], f'{{int(draft["booked"]):,}}', f'{{int(draft["posted"]):,}}', f'{{int(draft["gap"]):,}}'),
           ("LEFT JOIN", fixed["orders"], f'{{int(fixed["booked"]):,}}', f'{{int(fixed["posted"]):,}}', f'{{int(fixed["gap"]):,}}')],
          caption="Invented: the LEFT JOIN brings back T-4; the gap is still one number for two things")
kit.check("the count check fails the plain JOIN draft", draft["orders"] != tiny_orders_n,
          f'{{draft["orders"]}} of {{tiny_orders_n}}')
kit.check("the LEFT JOIN keeps all five orders and all 5,800 of booked",
          fixed["orders"] == tiny_orders_n and fixed["booked"] == tiny_booked, f'{{fixed["orders"]}} orders')"""),
        md("""
**What happened.** The LEFT JOIN keeps all five orders and all 5,800 of booked, and the count closes.
The gap now reads minus 700, which is still wrong: it is 800 never paid less 1,500 posted twice, two
different things netted into one figure that describes neither. The next level separates them.

**Your turn.** Run the plain JOIN version on Kalpa's Q2 and count its orders against the 462 in the
quarter. Type this in the empty cell below and write what you see in your reconciliation lines,
before you read any rupee:

```python
kalpa_inner = run(\"\"\"
WITH posted_per_order AS (SELECT order_id, sum(amount) AS posted FROM payments GROUP BY order_id)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS posted
FROM orders o JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2'\"\"\")[0]
print(kalpa_inner["orders"], "orders against", orders_q2)
```
"""),
        empty(),
        md("""
## 4. Which moves carry booked to what the feed posted?

A bridge walks from one total to another in named moves, each with the list of orders behind it,
which is Week 1 Wednesday's revenue bridge one tool later. From booked to posted there are three
moves, and each has a definition that a query can compute order by order:

| Move | Definition, per order | Invented tables |
|---|---|---|
| Never paid | Booked, where the order has no payment row at all | T-4, 800 |
| Paid short | Booked less collected, where collected is below booked | none |
| Posted twice | Posted less collected: the same instalment written more than once | T-3, 1,500 |

Collected counts each order and instalment once, at its amount; posted adds every row the feed holds.
So booked, less never paid, less paid short, is collected; and collected, plus posted twice, is
posted.

**Predict before you run.** On the invented tables, what is collected, each payment counted once?
a) 6,500; b) 5,800; c) 5,000; d) 4,200.
"""),
        code(f"""
tiny_rows = run(\"\"\"{Q3['tiny_per_order']}\"\"\")
show(tiny_rows, "Invented: booked, collected and posted, one row per order")
tb = run(\"\"\"{Q3['tiny_bridge']}\"\"\")[0]
tb = {{k: (v or 0) for k, v in tb.items()}}
kit.bridge(("booked", float(tb["booked"])),
           [("never paid", -float(tb["never_paid"])), ("paid short", -float(tb["paid_short"])),
            ("posted twice", float(tb["posted_twice"]))],
           end_label="posted", fmt=lambda v: f"{{v:,.0f}}", lit=[0, 2],
           title="Invented: from booked to posted in three named moves")"""),
        md("""
**What happened.** The answer is c, 5,000: T-1's 1,000, T-2's two instalments of 1,200 and 800, T-3's
one instalment of 1,500 counted once, and T-5's 500. The bridge reads booked 5,800, less 800 never
paid (T-4), less nothing paid short, is collected 5,000; plus 1,500 posted twice (T-3's instalment
1 written a second time) is posted 6,500. Each move has one order behind it, and each is a question
for a different person: T-4 for the collections team, T-3 for the platform lead.
"""),
        code("""
kit.check("booked less never paid less paid short equals collected",
          tb["booked"] - tb["never_paid"] - tb["paid_short"] == tb["collected"], f'{int(tb["collected"]):,}')
kit.check("collected plus posted twice equals posted", tb["collected"] + tb["posted_twice"] == tb["posted"],
          f'{int(tb["posted"]):,}')
kit.check("posted equals the payment rows that match a booked order",
          tb["posted"] == one("SELECT sum(amount) FROM tiny_payments WHERE order_id IN (SELECT order_id FROM tiny_orders)"),
          f'{int(tb["posted"]):,}')"""),
        md("""
## 5. Does the bridge close on Kalpa's Q2?

**Your turn.** The same bridge on the warehouse is the reconciliation Anand's analyst will audit. In
the empty cell below, type these lines, run them, and copy the six figures into your reconciliation
lines before reading them aloud:

```python
kb = run(Q_BRIDGE)[0]
for move, value in kb.items():
    print(f"{move:>13}: {kit.rupees(value or 0)}")
```

`Q_BRIDGE` is defined in the cell after it, which also checks, without printing any figure, that
your bridge closes.
"""),
        empty(),
        code(f"""
Q_BRIDGE = \"\"\"{Q3['kalpa_bridge']}\"\"\"
kb = {{k: (v or 0) for k, v in run(Q_BRIDGE)[0].items()}}
posted_alone = one(\"\"\"{Q3['posted_alone']}\"\"\")
kit.vflow(["booked\\nfrom orders", "less never paid", "less paid short", "collected",
           "plus posted twice", "posted\\nfrom payments"],
          kinds=["known", "bad", "bad", "good", "bad", "known"], title="The bridge you are closing on Kalpa's Q2")
kit.check("Kalpa's booked in the bridge equals Monday's", kb["booked"] == booked_q2, kit.rupees(booked_q2))
kit.check("booked less never paid less paid short equals collected, on Kalpa's Q2",
          kb["booked"] - kb["never_paid"] - kb["paid_short"] == kb["collected"], "equal to the rupee")
kit.check("collected plus posted twice equals posted, on Kalpa's Q2",
          kb["collected"] + kb["posted_twice"] == kb["posted"], "equal to the rupee")
kit.check("the bridge's posted equals the payments table's own total for Q2 orders",
          kb["posted"] == posted_alone, "equal to the rupee")"""),
        md("""
**What happened.** The four checks pass: the bridge starts at Monday's Rs 9,84,00,000, closes at each
step, and lands on what the payments table holds against Q2's orders, counted without a join. The
figures in between are yours, from the cell above; each move now needs the list of orders behind
it, which is chapter 4.

Kavya Nair, the team's senior analyst, reviews every number before it leaves the team.

> **Kavya's review.** "Rows in, rows out and the difference explained, written above the number. If
> the count does not close, the number does not leave the team, and if the gap has two causes, it
> gets two bars."
"""),
        md("""
## Does collected come out the same when each order's posted cash is capped at its booked amount?

The bridge counted collected by instalment: each order and instalment once. A second method never
looks at instalment numbers at all. For every order that was paid, it takes the smaller of what the
feed posted and what was booked, since no order can honestly collect more than it was booked for,
and adds those up. Here the INNER JOIN is the honest choice, because the question is about paid
orders only; an unpaid order adds nothing to collected either way.

The two methods fail in different places: the instalment method would count a retry that the feed
wrote under a new instalment number, and the cap method would throw away a genuine overpayment.
Agreement rules out either one alone. It cannot rule out a retry under a new instalment number on an
order that is also paid short, which both methods count, or two errors that happen to be the same
size.
"""),
        code(f"""
cap_rows = run(\"\"\"{Q3['tiny_cap']}\"\"\")
show(cap_rows, "Invented: each paid order's posted cash, capped at its booked amount")
by_cap = sum(r["capped"] for r in cap_rows)
kit.columns([r["order_id"] for r in cap_rows],
            [("collected by instalment", [float(next(t["collected"] for t in tiny_rows if t["order_id"] == r["order_id"])) for r in cap_rows]),
             ("collected by the cap", [float(r["capped"]) for r in cap_rows])],
            title="Invented: two methods, one collected figure per order")
kit.check("the cap method reaches the bridge's collected on the invented tables", by_cap == tb["collected"],
          f"{{int(by_cap):,}}")
kalpa_cap = one(\"\"\"{Q3['kalpa_cap']}\"\"\")
kit.check("the cap method reaches the bridge's collected on Kalpa's Q2", kalpa_cap == kb["collected"],
          "equal to the rupee")"""),
        md("""
**What happened.** Both methods give 5,000 on the invented tables, order by order, and they agree to
the rupee on Kalpa's Q2. So the feed holds no retry under a new instalment number and no genuine
overpayment, and collected can be trusted on either count.

### In the interview: how do you reconcile a joined total, and find two errors that cancel?

The tags mark how often a question comes up: [S] a staple asked everywhere, [F] frequent in GCC and product screens, [D] a differentiator.

**[F] How do you reconcile a total after a join back to its source table?** Recompute the total from the source table alone, without the join, and compare. Booked after the
join must equal booked from `orders`; posted after the join must equal the payments table's own
total for the same orders. Any difference is explained as a named move in a bridge, with the rows
behind it listed, or the join is wrong.

**[D] Two errors cancel and the total looks right: how would you find them?** A total that balances can still hide two errors, so count first: rows in against rows out finds a dropped or
repeated row even when the rupees balance. Then split the difference into moves that each have a
definition, so an unpaid order and a repeated payment each get their own bar, and each bar is checked
against the list of orders behind it.

### Depth: why does a bridge list its moves in a fixed order?

The bars in between depend on the order. Starting from booked, "never paid" is measured on booked
amounts and "posted twice" on posted amounts; list them in another order and the running totals
between them change even though the ends do not. A finance team fixes the order once and writes it
above the chart, so two analysts produce the same bridge.
"""),
        md("""
## What did this chapter answer, one line per question?

1. The count reconciliation runs first, since it needs no rupee, and the bridge follows, the one
   proof that gives an unpaid order and a repeated payment each its own bar with a list behind it.
2. Once payments are one row per order, the report can lose rows and cannot gain them; on Kalpa's
   Q2 it keeps all 462 orders and Rs 9,84,00,000 of booked.
3. A plain JOIN draft on the invented tables reports 4 orders, booked 5,000, posted 6,500 and a gap
   of minus 1,500: fully collected, with a surplus.
4. Counting orders in the report against the table, 4 against 5, catches it without reading a rupee;
   the LEFT JOIN restores all five, and the gap reads minus 700 until its two causes are separated.
5. Booked 5,800, less 800 never paid, less nothing paid short, is collected 5,000; plus 1,500 posted
   twice is posted 6,500. The same bridge closes on Kalpa's Q2 at every step, and its posted equals
   the payments table's own total for Q2 orders.
6. Capping each paid order's posted cash at its booked amount gives the same collected, 5,000 on the
   invented tables and the same figure on Kalpa's Q2.

**The question this leaves.** Each bar of the bridge is a total, and Anand asked which orders.
Chapter 4 asks which Q2 orders were never paid, and which payments were posted twice.
"""),
        code("kit.check_summary()"),
    ]
    build(nb_path(n), cells)
    write_sql(n, ["Rows in, rows out at order grain, the plain JOIN draft on the invented tables, and the bridge",
                  "from booked to posted, first invented, then on Kalpa's Q2."],
              [("Setup: the two invented tables", TINY),
               ("Rows in, rows out: the order-grain LEFT JOIN on Kalpa's Q2", Q3["order_grain"]),
               ("The trap: the plain JOIN draft on the invented tables", Q3["tiny_inner"]),
               ("The fix: LEFT JOIN on the invented tables", Q3["tiny_left"]),
               ("Your turn: the plain JOIN on Kalpa's Q2; count its orders against 462", Q3["kalpa_inner"]),
               ("Booked, collected and posted per order, invented", Q3["tiny_per_order"]),
               ("The bridge, invented", Q3["tiny_bridge"]),
               ("Your turn: the bridge on Kalpa's Q2", Q3["kalpa_bridge"]),
               ("Its end, from payments alone", Q3["posted_alone"]),
               ("The second route: capped at booked, invented", Q3["tiny_cap"]),
               ("The second route on Kalpa's Q2", Q3["kalpa_cap"])])
    print("chapter 3 written")


# ============================================================================================== 4
Q4 = {
    "tiny_anti": """
SELECT o.order_id, o.channel, o.amount AS booked
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.order_id IS NULL
ORDER BY o.order_id""",
    "tiny_not_exists": """
SELECT o.order_id, o.channel, o.amount AS booked
FROM tiny_orders o
WHERE NOT EXISTS (SELECT 1 FROM tiny_payments p WHERE p.order_id = o.order_id)
ORDER BY o.order_id""",
    "tiny_not_in": """
SELECT o.order_id
FROM tiny_orders o
WHERE o.order_id NOT IN (SELECT order_id FROM tiny_payments)""",
    "tiny_not_in_null": """
SELECT o.order_id
FROM tiny_orders o
WHERE o.order_id NOT IN (SELECT order_id FROM tiny_payments
                         UNION ALL
                         SELECT NULL)""",
    "tiny_except": """
SELECT order_id FROM tiny_orders
EXCEPT
SELECT order_id FROM tiny_payments""",
    "kalpa_anti": """
SELECT o.order_id, o.channel, o.order_date, o.amount AS booked
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
  AND p.order_id IS NULL
ORDER BY o.amount DESC""",
    "kalpa_not_exists": """
SELECT o.order_id
FROM orders o
WHERE o.quarter = 'Q2'
  AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)""",
    "kalpa_not_in": """
SELECT o.order_id
FROM orders o
WHERE o.quarter = 'Q2'
  AND o.order_id NOT IN (SELECT order_id FROM payments)""",
    "kalpa_except": """
SELECT order_id FROM orders WHERE quarter = 'Q2'
EXCEPT
SELECT order_id FROM payments""",
    "tiny_where_join": """
SELECT o.order_id, p.payment_id, p.paid_date
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
ORDER BY o.order_id, p.payment_id""",
    "tiny_where_list": """
SELECT o.order_id, o.amount AS booked
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
  AND p.order_id IS NULL""",
    "tiny_on_join": """
SELECT o.order_id, p.payment_id, p.paid_date
FROM tiny_orders o
LEFT JOIN tiny_payments p
       ON p.order_id = o.order_id
      AND p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
ORDER BY o.order_id, p.payment_id""",
    "tiny_on_list": """
SELECT o.order_id, o.amount AS booked
FROM tiny_orders o
LEFT JOIN tiny_payments p
       ON p.order_id = o.order_id
      AND p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
WHERE p.order_id IS NULL""",
    "kalpa_having_order": """
SELECT o.order_id, count(*) AS payment_rows
FROM orders o
JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.order_id
HAVING count(*) > 1""",
    "tiny_having_order": """
SELECT p.order_id, count(*) AS payment_rows, sum(p.amount) - max(p.amount) AS beyond_one_payment
FROM tiny_payments p
JOIN tiny_orders o ON o.order_id = p.order_id
GROUP BY p.order_id
HAVING count(*) > 1
ORDER BY p.order_id""",
    "tiny_having_inst": """
SELECT p.order_id, p.instalment_no, count(*) AS times_posted,
       sum(p.amount) - max(p.amount) AS posted_twice
FROM tiny_payments p
JOIN tiny_orders o ON o.order_id = p.order_id
GROUP BY p.order_id, p.instalment_no
HAVING count(*) > 1
ORDER BY p.order_id""",
    "kalpa_having_inst": """
SELECT p.order_id, o.channel, p.instalment_no, count(*) AS times_posted,
       sum(p.amount) - max(p.amount) AS posted_twice
FROM payments p
JOIN orders o ON o.order_id = p.order_id
WHERE o.quarter = 'Q2'
GROUP BY p.order_id, o.channel, p.instalment_no
HAVING count(*) > 1
ORDER BY p.order_id""",
    "tiny_orphans": """
SELECT p.payment_id, p.order_id AS paid_for, p.paid_date, p.amount
FROM tiny_payments p
LEFT JOIN tiny_orders o ON o.order_id = p.order_id
WHERE o.order_id IS NULL""",
    "kalpa_orphans": """
SELECT p.payment_id, p.order_id AS paid_for, p.paid_date, p.method, p.amount
FROM payments p
LEFT JOIN orders o ON o.order_id = p.order_id
WHERE o.order_id IS NULL
ORDER BY p.payment_id""",
    "kalpa_rows_by_home": """
SELECT coalesce(o.quarter, 'no order') AS home, count(*) AS payment_rows
FROM payments p
LEFT JOIN orders o ON o.order_id = p.order_id
GROUP BY coalesce(o.quarter, 'no order')""",
    "tiny_by_subtraction": """
SELECT (SELECT count(*) FROM tiny_orders)
         - (SELECT count(DISTINCT order_id) FROM tiny_payments
             WHERE order_id IN (SELECT order_id FROM tiny_orders)) AS unpaid_orders,
       (SELECT sum(amount) FROM tiny_orders)
         - (SELECT sum(amount) FROM tiny_orders
             WHERE order_id IN (SELECT order_id FROM tiny_payments)) AS unpaid_booked""",
    "kalpa_by_subtraction": """
SELECT (SELECT count(*) FROM orders WHERE quarter = 'Q2')
         - (SELECT count(DISTINCT order_id) FROM payments
             WHERE order_id IN (SELECT order_id FROM orders WHERE quarter = 'Q2')) AS unpaid_orders,
       (SELECT sum(amount) FROM orders WHERE quarter = 'Q2')
         - (SELECT sum(amount) FROM orders
             WHERE quarter = 'Q2' AND order_id IN (SELECT order_id FROM payments)) AS unpaid_booked""",
    "kalpa_cap_list": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted FROM payments GROUP BY order_id
)
SELECT o.order_id
FROM orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2' AND pp.posted > o.amount""",
}

CH4_STEPS = ["the need: whom to chase, whom to refund", "the options: four ways to find the unpaid",
             "the anti-join: orders nothing matched", "the trap: a quarter filter in WHERE",
             "the fix: the condition goes in ON", "the trap: two rows are not two payments",
             "the fix: order and instalment", "a second route: subtraction, and the cap"]


def chapter4():
    n = 4
    ladder = ["Which orders have no payment at all?",
              "What happens to the unpaid list when \"paid in Q2\" goes into the WHERE clause?",
              "Where does a condition on the payments table belong?",
              "Which orders does HAVING COUNT(*) > 1 flag, and are they double-paid?",
              "What makes a retry a retry, and does each list match its bar?",
              "Do a second method and a second list reach the same orders?"]
    cells = [
        title_cell(
            n,
            "Anand's collections team rings the customers on the unpaid list, and the data "
            "platform lead and Finance reverse or refund what is on the double-paid list. A "
            "wrong unpaid list chases a customer who paid or misses one who did not; a wrong "
            "double-paid list reverses a legitimate second instalment and rings a business buyer "
            "who paid on time.",
            ladder,
            "Two moves of the bridge carry names: the booked value of orders never paid, and "
            "the cash posted twice. Each list is right only when its total equals its bar.",
            "Chapter 3 proved the report keeps every Q2 order, 462 rows for 462 orders, and built the "
            "bridge from booked to posted. On the invented tables it reads booked 5,800, less 800 "
            "never paid, is collected 5,000, plus 1,500 posted twice, is posted 6,500; on Kalpa's Q2 "
            "you ran it and it closed at every step. Each bar is a total, and Anand asked for names. "
            "This chapter writes the list behind each bar."),
        md("""
**Setup.** The next cell finds the helper, connects to the warehouse and creates the invented tables
of chapter 1. Every query below is also in `sql/C2_W02_D02_04_which_orders_STUDENT.sql`.
"""),
        code(HELPERS + f"""
Q_BRIDGE = \"\"\"{Q3['kalpa_bridge']}\"\"\"
kb = {{k: (v or 0) for k, v in run(Q_BRIDGE)[0].items()}}
tb = {{k: (v or 0) for k, v in run(\"\"\"{Q3['tiny_bridge']}\"\"\")[0].items()}}
print("Chapter 3's bridge is rebuilt for Kalpa's Q2 and for the invented tables; its figures stay unprinted.")"""),
        map_cell(n, CH4_STEPS),
        md(f"""
## Whom does Anand chase, and whom does he refund?

Each list goes to a different desk and triggers an action with a cost. The unpaid list goes to the
collections team, who ring every customer on it, and every order on it is cash Kalpa is owed. The double-paid list goes to the platform lead, who fixes the
feed, and to Finance, who checks with the bank whether the customer was charged twice and, if so,
refunds them. A name on the wrong list is a phone call to a customer who did nothing wrong, and a
name missing is money left where it is. {DOSSIER}
"""),
        md(COMPANY[4]),
        md(TINY_NOTE),
        md("""
## Which of four ways finds the unpaid orders, and what does each cost here?

An order that nothing matched is found with an anti-join: keep the rows of one table that have no
partner in the other. SQL offers four ways to write one.

| Option | Written as | What it assumes |
|---|---|---|
| A. LEFT JOIN, then keep the misses | `LEFT JOIN payments p ... WHERE p.order_id IS NULL` | The right table's key is never NULL on a real match |
| B. NOT EXISTS | `WHERE NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)` | Nothing |
| C. NOT IN | `WHERE o.order_id NOT IN (SELECT order_id FROM payments)` | The subquery never returns a NULL |
| D. EXCEPT | `SELECT order_id FROM orders EXCEPT SELECT order_id FROM payments` | Only the ids are wanted |

The cell below runs all four on Kalpa's Q2 and times them, checks that they agree without printing
the list, and then shows on the invented tables what happens to C when a single payment arrives
with no order reference, which a feed can send.
"""),
        code(f"""
import time
timed = {{}}
for name, q in [("A. LEFT JOIN ... IS NULL", \"\"\"{Q4['kalpa_anti']}\"\"\"),
                ("B. NOT EXISTS", \"\"\"{Q4['kalpa_not_exists']}\"\"\"),
                ("C. NOT IN", \"\"\"{Q4['kalpa_not_in']}\"\"\"),
                ("D. EXCEPT", \"\"\"{Q4['kalpa_except']}\"\"\")]:
    t0 = time.perf_counter()
    ids = {{r["order_id"] for r in run(q)}}
    timed[name] = (ids, time.perf_counter() - t0)
not_in_clean = run(\"\"\"{Q4['tiny_not_in']}\"\"\")
not_in_null = run(\"\"\"{Q4['tiny_not_in_null']}\"\"\")
kit.table(["Option", "Carries the order's columns", "With one NULL payment, invented", "Time on Kalpa's Q2"],
          [("A. LEFT JOIN ... IS NULL", "yes", "still finds T-4", f'{{timed["A. LEFT JOIN ... IS NULL"][1] * 1000:.1f}} ms'),
           ("B. NOT EXISTS", "yes", "still finds T-4", f'{{timed["B. NOT EXISTS"][1] * 1000:.1f}} ms'),
           ("C. NOT IN", "yes", f"finds {{len(not_in_null)}} orders, where it found {{len(not_in_clean)}}",
            f'{{timed["C. NOT IN"][1] * 1000:.1f}} ms'),
           ("D. EXCEPT", "ids only", "still finds T-4", f'{{timed["D. EXCEPT"][1] * 1000:.1f}} ms')],
          caption="Four anti-joins, sized")
kit.matrix(["A. LEFT ... IS NULL", "B. NOT EXISTS", "C. NOT IN", "D. EXCEPT"],
           ["a clean feed", "a feed with one NULL order id"],
           [["finds T-4", "finds T-4"], ["finds T-4", "finds T-4"], ["finds T-4", "finds nothing"],
            ["finds T-4, ids only", "finds T-4, ids only"]],
           title="Invented: NOT IN goes silent when the subquery holds a NULL")
lists = [v[0] for v in timed.values()]
kit.check("all four anti-joins return the same Q2 list on Kalpa", all(l == lists[0] for l in lists),
          "same ids, unprinted")
kit.check("NOT IN returns nothing once the subquery holds a NULL", len(not_in_null) == 0 and len(not_in_clean) == 1,
          f"{{len(not_in_clean)}} then {{len(not_in_null)}}")"""),
        md("""
**The best-fit call.** Option A, the LEFT JOIN that keeps only the misses, fits best, because it is
the same LEFT JOIN the report already runs: the unpaid list is the report's rows with nothing on the
payments side, and it carries every column Anand wants beside each order, the channel, the date and
the amount. All four take a few milliseconds and agree on today's warehouse, so they differ in what
each assumes. Avoid C: `NOT IN` compares against every value in the subquery, a
comparison with NULL is unknown, and one NULL order id in the feed makes it return no rows at all,
without an error.

**The fact that would change the call.** If the list were read as SQL by Anand's analyst, B would
read closest to his sentence, "the orders for which no payment exists"; and if the payments table
ever allowed a NULL order id, which a change to the feed could bring, C would stop being safe even
where it works today.
"""),
        md("""
## 1. Which orders have no payment at all?

**Predict before you run.** On the invented tables, which orders does the LEFT JOIN that keeps only
the misses return? a) T-4; b) T-4 and T-9; c) T-2 and T-3; d) none, since every order has an id.
"""),
        code(f"""
anti = run(\"\"\"{Q4['tiny_anti']}\"\"\")
show(anti, "Invented: the orders nothing matched", money=["booked"])
kit.flow(["LEFT JOIN\\nevery order kept", "WHERE p.order_id IS NULL\\nonly the misses", "the unpaid list\\nits total must equal the bar"],
         kinds=["plain", "plain", "good"], title="The anti-join, in two steps")
kit.check("the invented unpaid list's total equals the bridge's never-paid bar",
          sum(r["booked"] for r in anti) == tb["never_paid"], f'{{int(tb["never_paid"]):,}}')"""),
        md("""
**What happened.** The answer is a, T-4 alone, booked at 800, which is exactly the bridge's
never-paid bar. T-9 is not an order, so it cannot be on a list of orders; it belongs to the
platform lead's list at level 5.

**Your turn.** Run the same anti-join on Kalpa's Q2. In the empty cell below, type:

```python
unpaid = run(Q_UNPAID)
show(unpaid, "Q2 orders with no payment at all", money=["booked"])
print(len(unpaid), "orders,", kit.rupees(sum(r["booked"] for r in unpaid)))
```

`Q_UNPAID` is defined in the cell after it, which checks, without printing anything, that your
list's total equals the never-paid bar you computed in chapter 3.
"""),
        empty(),
        code(f"""
Q_UNPAID = \"\"\"{Q4['kalpa_anti']}\"\"\"
unpaid_rows = run(Q_UNPAID)
kit.check("Kalpa's unpaid list totals the never-paid bar of the bridge",
          sum(r["booked"] for r in unpaid_rows) == kb["never_paid"], "equal to the rupee")
paid_on_list = one("SELECT count(*) FROM payments WHERE order_id = ANY(%s)", ([r["order_id"] for r in unpaid_rows],))
kit.check("no order on Kalpa's unpaid list has a payment row", paid_on_list == 0, "checked against payments")"""),
        md("""
## 2. What happens to the unpaid list when "paid in Q2" goes into the WHERE clause?

**The plausible wrong answer.** Anand talks about the cash that came in during Q2, so a teammate adds
the quarter's dates to the unpaid list, in the WHERE clause, beside the anti-join's condition:

```sql
SELECT o.order_id, o.amount AS booked
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
  AND p.order_id IS NULL;
```

**Predict before you run.** How many orders does it list? a) 1, T-4; b) 0; c) 5; d) 2, T-2 and T-3.
"""),
        code(f"""
where_join = run(\"\"\"{Q4['tiny_where_join']}\"\"\")
where_list = run(\"\"\"{Q4['tiny_where_list']}\"\"\")
show(where_join, "Invented: the LEFT JOIN with the quarter in WHERE")
kit.stats([(f"{{len(where_join)}}", "rows after the WHERE", "the INNER JOIN's count"),
           (f"{{len(where_list)}}", "orders on the unpaid list", "the bar says 800 is unpaid"),
           ("T-4", "missing", "its paid_date is NULL")])
kit.vflow(["LEFT JOIN\\nT-4 kept, paid_date NULL", "WHERE paid_date BETWEEN ...\\nNULL BETWEEN is unknown",
           "T-4 dropped\\nthe same rows as INNER", "the unpaid list\\nempty"],
          kinds=["plain", "bad", "bad", "bad"], title="Invented: a WHERE on the right-hand table undoes the LEFT JOIN")"""),
        md("""
**What happened.** The answer is b: no orders. The join itself returns 6 rows, the same count as the
INNER JOIN in chapter 1, and T-4 is gone from them.

**Why it is wrong.** After the LEFT JOIN, T-4's row carries NULL in every payments column, including
`paid_date`. `NULL BETWEEN` two dates evaluates to unknown, and WHERE keeps only rows that are true,
so T-4 is thrown away after the join has kept it. A condition on the right-hand
table in the WHERE clause turns the LEFT JOIN into an INNER one without a word, and the anti-join
condition that follows can never be met. The list supports the sentence "every Q2 order was paid
within the quarter", which is false, and the collections team gets an empty list.

**The check that catches it.** The list's total must equal its bar: 0 against the bridge's 800 never
paid. Counting the join's rows against the orders, 6 rows where the LEFT JOIN returns 7, points at
the same fault.
"""),
        md("""
## 3. Where does a condition on the payments table belong?

It belongs in the ON clause. ON decides which payment rows count as a match, before the join; WHERE decides
which joined rows survive, after it. The PostgreSQL manual says that a restriction placed in the ON
clause "is processed before the join, while a restriction placed in the WHERE clause is processed
after the join", and that the difference "matters a lot with outer joins" (PostgreSQL 16
documentation, section 7.2.1.1, Joined Tables, checked 1 Oct 2026).

**Predict before you run.** With the dates moved into ON, how many rows does the join return, and
which orders does the unpaid list hold? a) 6 rows, no orders; b) 7 rows, T-4; c) 7 rows, T-4 and T-9;
d) 8 rows, T-4.
"""),
        code(f"""
on_join = run(\"\"\"{Q4['tiny_on_join']}\"\"\")
on_list = run(\"\"\"{Q4['tiny_on_list']}\"\"\")
kit.columns(["rows after the join", "orders on the unpaid list"],
            [("date in WHERE", [len(where_join), len(where_list)]), ("date in ON", [len(on_join), len(on_list)])],
            title="Invented: the same condition, two places, two answers")
show(on_list, "Invented: the unpaid list with the date condition in ON", money=["booked"])
kit.check("with the condition in ON, the join keeps every order", len({{r["order_id"] for r in on_join}}) == 5,
          f"{{len(on_join)}} rows")
kit.check("with the condition in ON, the list holds T-4 and matches the bar",
          [r["order_id"] for r in on_list] == ["T-4"] and sum(r["booked"] for r in on_list) == tb["never_paid"], "T-4, 800")"""),
        md("""
**What happened.** The answer is b: 7 rows and T-4 on the list, booked at 800, the bar exactly.
Moving one condition from WHERE to ON changed the whole list. The rule to keep is that in a LEFT
JOIN a condition on the right-hand table goes in ON, and the one WHERE condition that belongs on the
right table is the anti-join's `IS NULL`, unless the question wants matched rows only.

The two lists answer different questions. With the dates in ON, the list holds the orders not paid
within Q2, so an order paid on 3 October would be on it; for "never paid", no date condition belongs
on payments at all. On the invented tables and on Kalpa's Q2 the two lists hold the same orders, only
because no payment in the warehouse lands after 30 September.

## 4. Which orders does HAVING COUNT(*) > 1 flag, and are they double-paid?

**The plausible wrong answer.** For the double-paid list, a teammate reaches for what Monday taught:
group Q2's payments by order and keep the orders with more than one row.

```sql
SELECT o.order_id, count(*) AS payment_rows
FROM orders o
JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.order_id
HAVING count(*) > 1;
```

**Predict before you run.** Anand will ask the payments team to reverse the second payment on every
order this returns. How long is the list? a) a handful of orders, each paid twice; b) 216 orders,
including every one of Q2's ten largest invoices; c) no rows, since payment ids are unique; d) all
462 Q2 orders.
"""),
        code(f"""
flagged = run(\"\"\"{Q4['kalpa_having_order']}\"\"\")
top_ten = [r["order_id"] for r in run(\"\"\"{Q2['largest']}\"\"\")]
flagged_ids = {{r["order_id"] for r in flagged}}
tiny_flagged = run(\"\"\"{Q4['tiny_having_order']}\"\"\")
show(tiny_flagged, "Invented: the same query on the tiny tables, with what lies beyond one payment",
     money=["beyond_one_payment"])
kit.stats([(f"{{len(flagged)}}", "Q2 orders flagged", "more than one payment row each"),
           (f"{{sum(1 for t in top_ten if t in flagged_ids)}} of 10", "largest Q2 orders on it", "all paid in instalments 1 and 2"),
           (f'{{int(sum(r["beyond_one_payment"] for r in tiny_flagged)):,}}', "invented surplus it claims", "the bar says 1,500")])
kit.bars([(r["order_id"], float(r["beyond_one_payment"])) for r in tiny_flagged] + [("bar: posted twice", float(tb["posted_twice"]))],
         lit=[2], fmt=lambda v: f"{{v:,.0f}}", title="Invented: the order-level list claims more than the bar")"""),
        md("""
**What happened.** The answer is b: 216 Q2 orders, and every one of the ten largest Q2 invoices is on
it, each paid in instalments 1 and 2. On the invented tables the same query flags T-2 and T-3 and
claims 2,300 posted beyond one payment, against a bar of 1,500.

**Why it is wrong.** Two payment rows can be two instalments or one payment posted twice, and a count
of rows cannot tell them apart. T-2's second row is its second instalment, real cash; T-3's second
row is the retry. A note asking the payments team to reverse the second payment on all 216 orders
would reverse legitimate second instalments on Kalpa's largest business invoices and put a call to
every corporate buyer who paid on time.

**The check that catches it.** The list's surplus must equal the bridge's posted-twice bar, and on
the invented tables it claims 2,300 against 1,500.
"""),
        code("""
kit.check("the order-level list flags every one of Q2's ten largest orders",
          all(t in flagged_ids for t in top_ten), f"{len(flagged)} orders flagged")
kit.check("on the invented tables, the order-level list's surplus disagrees with the bar",
          sum(r["beyond_one_payment"] for r in tiny_flagged) != tb["posted_twice"],
          f'{int(sum(r["beyond_one_payment"] for r in tiny_flagged)):,} against {int(tb["posted_twice"]):,}')"""),
        md("""
## 5. What makes a retry a retry, and does each list match its bar?

A gateway retry posts the same instalment of the same order twice; a second instalment has its own
instalment number. So the double-paid grain is the order and the instalment, and the amount posted
twice is what lies beyond one payment of that instalment.

**Predict before you run.** Grouped by `order_id` and `instalment_no`, which invented orders stay on
the list, and what is posted twice? a) T-2 and T-3, 2,300; b) T-3, 1,500; c) T-2, 800; d) none.
"""),
        code(f"""
retries = run(\"\"\"{Q4['tiny_having_inst']}\"\"\")
show(retries, "Invented: one order and instalment posted more than once", money=["posted_twice"])
kit.matrix(["instalment 1 only", "instalments 1 and 2", "instalment 1, twice"],
           ["what it is", "which list"],
           [["paid once, in full", "neither"], ["paid in two parts", "neither"], ["a gateway retry", "double-paid"]],
           title="Reading a pattern of payment rows")
kit.check("the invented double-paid list is T-3's instalment 1", [(r["order_id"], r["instalment_no"]) for r in retries] == [("T-3", 1)],
          "T-3, instalment 1")
kit.check("its surplus equals the bridge's posted-twice bar", sum(r["posted_twice"] for r in retries) == tb["posted_twice"],
          f'{{int(tb["posted_twice"]):,}}')"""),
        md("""
**What happened.** The answer is b: T-3's instalment 1, posted twice, 1,500 posted beyond one payment,
which is the bar exactly. T-2 left the list, because its two rows carry two instalment numbers.

**Your turn.** Build both of Kalpa's remaining lists. In the empty cell below, type:

```python
double_paid = run(Q_RETRIES)
show(double_paid, "Q2 instalments posted more than once", money=["posted_twice"])
orphans = run(Q_ORPHANS)
show(orphans, "Payments whose order is not in the orders table", money=["amount"])
```

The double-paid list goes to the platform lead and Finance. The last query is a third finding:
payments that match no order at all, which goes back to the platform lead with its payment ids.
The cell after it defines both queries and checks, without printing, that the double-paid list
matches its bar and that every one of the 1,428 payment rows is accounted for.
"""),
        empty(),
        code(f"""
Q_RETRIES = \"\"\"{Q4['kalpa_having_inst']}\"\"\"
Q_ORPHANS = \"\"\"{Q4['kalpa_orphans']}\"\"\"
retry_rows = run(Q_RETRIES)
orphan_rows = run(Q_ORPHANS)
homes = {{r["home"]: r["payment_rows"] for r in run(\"\"\"{Q4['kalpa_rows_by_home']}\"\"\")}}
total_rows = one("SELECT count(*) FROM payments")
kit.check("Kalpa's double-paid list totals the bridge's posted-twice bar",
          sum(r["posted_twice"] for r in retry_rows) == kb["posted_twice"], "equal to the rupee")
kit.check("every payment row is on a Q1 order, a Q2 order or no order, and they add to the table",
          sum(homes.values()) == total_rows, f"{{total_rows:,}} rows accounted for")
kit.check("the orphan query finds exactly the rows on no order", len(orphan_rows) == homes.get("no order", 0),
          "count unprinted")"""),
        md("""
Kavya Nair, the team's senior analyst, reviews every number before it leaves the team.

> **Kavya's review.** "Two payment rows are not a double payment. Show me what makes a retry a retry
> before anyone rings a customer, and show me that each list adds up to its bar."
"""),
        md("""
## Do a second method and a second list reach the same orders?

The unpaid list is checked a way that builds no anti-join at all: count the orders, take away the
orders that appear in payments, and do the same with their booked amounts. What is left must equal
the list's count and total; a WHERE that empties the anti-join, or a NULL that silences it, cannot
reach this route. The double-paid list is found a second way that never reads an instalment number:
an order whose posted cash exceeds what it was booked for has been paid more than once. The
instalment method would miss a retry the feed wrote under a new instalment number, and the booked
method would miss a retry on an order paid short. When both find the same orders, the only retry
that could still hide is one with both blind spots at once, a new instalment number on an order
that is also paid short.
"""),
        code(f"""
sub_tiny = run(\"\"\"{Q4['tiny_by_subtraction']}\"\"\")[0]
cap_tiny = run(\"\"\"
WITH posted_per_order AS (SELECT order_id, sum(amount) AS posted FROM tiny_payments GROUP BY order_id)
SELECT o.order_id FROM tiny_orders o JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE pp.posted > o.amount\"\"\")
kit.side_by_side(
    kit.vflow(["unpaid, route 1\\nLEFT JOIN ... IS NULL", "unpaid, route 2\\nall orders less the paid", "same count and total?"],
              kinds=["plain", "plain", "good"], show=False),
    kit.vflow(["double-paid, route 1\\norder and instalment", "double-paid, route 2\\nposted above booked", "same orders?"],
              kinds=["plain", "plain", "good"], show=False),
)
kit.check("invented: all orders less the paid ones leave the unpaid list's count and total",
          (sub_tiny["unpaid_orders"], sub_tiny["unpaid_booked"]) == (len(anti), sum(r["booked"] for r in anti)),
          "1 order, 800, both ways")
kit.check("invented: posted above booked flags the same order as the instalment method",
          [r["order_id"] for r in cap_tiny] == [r["order_id"] for r in retries], "T-3 both ways")
sub_kalpa = run(\"\"\"{Q4['kalpa_by_subtraction']}\"\"\")[0]
cap_kalpa = {{r["order_id"] for r in run(\"\"\"{Q4['kalpa_cap_list']}\"\"\")}}
kit.check("Kalpa: all Q2 orders less the paid ones leave the unpaid list's count and total",
          (sub_kalpa["unpaid_orders"], sub_kalpa["unpaid_booked"]) == (len(unpaid_rows), sum(r["booked"] for r in unpaid_rows)),
          "equal, unprinted")
kit.check("Kalpa: posted above booked flags the same orders as the instalment method",
          cap_kalpa == {{r["order_id"] for r in retry_rows}}, "same ids, unprinted")"""),
        md("""
**What happened.** Both second routes agree with the first, on the invented tables and on Kalpa's Q2:
the same count and total of unpaid orders by subtraction, and the same double-paid orders whether
the retry is found by its instalment number or by its cash exceeding its booking.

### In the interview: how do you find the unpaid orders and the double-paid ones?

The tags mark how often a question comes up: [S] a staple asked everywhere, [F] frequent in GCC and product screens, [D] a differentiator.

**[F] How do you find orders with no payment?** Use an anti-join: a LEFT JOIN from orders to payments that keeps the rows where the payment side is
NULL, or NOT EXISTS, which says the same thing in the order of the sentence. Then check the list
against figures computed without it: its booked total must equal total booked less total collected,
less anything paid in part, or the list is wrong. Avoid NOT IN, which returns nothing once the
subquery holds a single NULL.

**[F] A filter on the right-hand table of a LEFT JOIN: WHERE or ON, and what changes?** It goes in ON. In ON the filter decides which right-hand rows count as a match, and every left row survives; in
WHERE it runs after the join, the unmatched rows carry NULL, NULL fails the filter, and the LEFT
JOIN behaves as an INNER one. The only right-table condition that belongs in WHERE is the anti-join's
`IS NULL`, unless the question wants matched rows only, where the INNER result is the honest one.

**[F] HAVING COUNT(*) > 1 on payments by order: what does it find, and what does it wrongly include?** It finds every order with more than one payment row, which includes orders legitimately paid in
instalments. The retry grain is the order and the instalment, and the proof is that the list's
surplus equals posted less collected.

### Depth: why does NOT IN return nothing when the subquery holds a NULL?

`x NOT IN (a, b, NULL)` means `x <> a AND x <> b AND x <> NULL`. The last comparison is unknown for
every x, so the whole condition is never true, and WHERE keeps no row. It is the same three-valued
logic that made the WHERE clause drop T-4 at level 2.
"""),
        md("""
## What did this chapter answer, one line per question?

1. The orders with no payment are found by an anti-join; on the invented tables it is T-4 at 800,
   the never-paid bar exactly, and on Kalpa's Q2 your list matches its bar too.
2. With "paid in Q2" in the WHERE clause the join shrinks to the INNER JOIN's 6 rows and the unpaid
   list comes back empty, because NULL fails the date test.
3. A condition on the payments table belongs in ON, which restores 7 rows and T-4.
4. HAVING COUNT(*) > 1 by order flags 216 Q2 orders, every one of the ten largest invoices among
   them, because two instalments are two rows too.
5. A retry is the same order and instalment posted twice; grouped that way the invented list is
   T-3's 1,500, the bar exactly, and Kalpa's list matches its bar.
6. All orders less the paid ones leave the unpaid list's count and total, and posted above booked
   flags the same double-paid orders, on both sets of tables.

**The question this leaves.** Anand has the bridge and its two lists, so chapter 5 asks what goes on
the one page he signs, by channel, and whether its gap column tells the truth.
"""),
        code("kit.check_summary()"),
    ]
    build(nb_path(n), cells)
    write_sql(n, ["The unpaid list, the double-paid list and the payments with no order: first on the invented",
                  "tables, then on Kalpa's Q2. The Kalpa lists are yours to read."],
              [("Setup: the two invented tables", TINY),
               ("The anti-join, invented: which orders have no payment?", Q4["tiny_anti"]),
               ("Your turn: the unpaid list on Kalpa's Q2", Q4["kalpa_anti"]),
               ("Option B, NOT EXISTS, on Kalpa's Q2", Q4["kalpa_not_exists"]),
               ("Option C, NOT IN, on Kalpa's Q2", Q4["kalpa_not_in"]),
               ("Option D, EXCEPT, on Kalpa's Q2", Q4["kalpa_except"]),
               ("Why not NOT IN: one NULL in the subquery, invented", Q4["tiny_not_in_null"]),
               ("The trap: the quarter's dates in WHERE, invented", Q4["tiny_where_join"]),
               ("The trap's unpaid list, invented", Q4["tiny_where_list"]),
               ("The fix: the dates in ON, invented", Q4["tiny_on_join"]),
               ("The fix's unpaid list, invented", Q4["tiny_on_list"]),
               ("The trap: HAVING COUNT(*) > 1 by order on Kalpa's Q2", Q4["kalpa_having_order"]),
               ("The same, invented, with what lies beyond one payment", Q4["tiny_having_order"]),
               ("The fix: order and instalment, invented", Q4["tiny_having_inst"]),
               ("Your turn: the double-paid list on Kalpa's Q2", Q4["kalpa_having_inst"]),
               ("Your turn: payments whose order is not in the orders table", Q4["kalpa_orphans"]),
               ("Every payment row accounted for", Q4["kalpa_rows_by_home"]),
               ("The second route: all Q2 orders less the paid ones, count and total", Q4["kalpa_by_subtraction"]),
               ("The second route: posted above booked, Kalpa's Q2", Q4["kalpa_cap_list"])])
    print("chapter 4 written")


# ============================================================================================== 5
REPORT = """
WITH per_order AS ({per_order})
SELECT channel,
       count(*)                                  AS orders,
       sum(booked)                               AS booked,
       sum(collected)                            AS collected,
       sum(booked - {collected})                 AS gap
FROM per_order
GROUP BY channel
ORDER BY channel"""


def report_sql(orders, payments, where="", fixed=True):
    col = "coalesce(collected, 0)" if fixed else "collected"
    return REPORT.format(per_order="\n" + per_order(orders, payments, where) + "\n",
                         collected=col).strip("\n")


FULL_REPORT = """
WITH per_order AS ({per_order})
SELECT channel,
       count(*)                                                AS orders,
       sum(booked)                                             AS booked,
       sum(coalesce(collected, 0))                             AS collected,
       sum(booked - coalesce(collected, 0))                    AS gap,
       round(100 * sum(coalesce(collected, 0)) / sum(booked), 2) AS collected_pct,
       count(*) FILTER (WHERE collected IS NULL)               AS unpaid_orders,
       sum(coalesce(posted, 0) - coalesce(collected, 0))       AS posted_twice
FROM per_order
GROUP BY channel
ORDER BY channel"""

Q5 = {
    "tiny_hurried": report_sql("tiny_orders", "tiny_payments", fixed=False),
    "tiny_fixed": report_sql("tiny_orders", "tiny_payments", fixed=True),
    "kalpa_hurried": report_sql("orders", "payments", "WHERE o.quarter = 'Q2'", fixed=False),
    "kalpa_full": FULL_REPORT.format(per_order="\n" + per_order("orders", "payments", "WHERE o.quarter = 'Q2'")
                                     + "\n").strip("\n"),
    "tiny_per_order_gap": """
WITH per_order AS ({})
SELECT order_id, channel, booked, collected, booked - collected AS gap
FROM per_order
ORDER BY order_id""".format("\n" + per_order("tiny_orders", "tiny_payments") + "\n").strip("\n"),
    "tiny_unpaid_by_channel": """
SELECT o.channel, sum(o.amount) AS never_paid
FROM tiny_orders o
WHERE NOT EXISTS (SELECT 1 FROM tiny_payments p WHERE p.order_id = o.order_id)
GROUP BY o.channel""",
    "kalpa_unpaid_by_channel": """
SELECT o.channel, sum(o.amount) AS never_paid
FROM orders o
WHERE o.quarter = 'Q2'
  AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)
GROUP BY o.channel""",
    "refunds": """
SELECT o.quarter, count(*) AS refund_rows
FROM refunds r
JOIN orders o ON o.order_id = r.order_id
GROUP BY o.quarter
ORDER BY o.quarter""",
}

CH5_STEPS = ["the need: a page Anand can sign", "the options: four report forms, sized",
             "what a line per channel carries", "the trap: a gap column of zeros",
             "why NULL leaves the sum", "the fix, and the bridge it must add to",
             "a second route: the unpaid list by channel"]


def chapter5():
    n = 5
    ladder = ["Which of four report forms fits a finance controller?",
              "What must a line per channel carry for Anand to sign it?",
              "What does the gap column say when each order's gap is added up?",
              "Why does the gap column read zero, and which check catches it?",
              "Does the fixed report add back to the bridge on Kalpa's Q2?",
              "Does the unpaid list, grouped by channel, give the same gap?"]
    cells = [
        title_cell(
            n,
            "Anand signs the report and sends it on to the CEO's Monday page, and the channel "
            "heads chase their own unpaid orders from it. A gap column that reads zero stands "
            "every one of them down, and a report that does not add back to the bridge cannot be "
            "defended when Anand's analyst audits it.",
            ladder,
            "The page carries booked, collected and the gap between them, by channel: app, store and "
            "web. The gap is "
            "booked less collected, order by order, and it must add up to the bridge's never-paid "
            "and paid-short bars.",
            "Chapter 4 put names behind the bridge. On the invented tables the unpaid list is T-4, 800, "
            "and the double-paid list is T-3's instalment 1 posted twice, 1,500; on Kalpa's Q2 you built "
            "both lists and each matched its bar, and every one of the 1,428 payment rows was accounted "
            "for. This chapter turns all of it into the page Anand signs."),
        md("""
**Setup.** The next cell finds the helper, connects to the warehouse and creates the invented tables
of chapter 1. Every query below is also in `sql/C2_W02_D02_05_what_anand_signs_STUDENT.sql`.
"""),
        code(HELPERS + f"""
kb = {{k: (v or 0) for k, v in run(\"\"\"{Q3['kalpa_bridge']}\"\"\")[0].items()}}
booked_ch = run(\"\"\"{Q2['booked_by_channel']}\"\"\")
print("Kalpa's Q2 booked by channel, from orders alone:",
      ", ".join(f'{{r["channel"]}} {{kit.rupees(r["booked"])}}' for r in booked_ch))"""),
        map_cell(n, CH5_STEPS),
        md(f"""
## What does Anand need on the page before he signs it?

Anand signs the report and it goes on to Meera Raghavan's Monday page, so every figure on it becomes
his figure. He needs the gap split by channel, because the store team, the app team and the web team
each chase their own customers; the orders behind the gap, because a channel total cannot be chased;
and the proof above the number, because his analyst will audit it. {DOSSIER}
"""),
        md(COMPANY[5]),
        md(TINY_NOTE),
        md("""
## Which of four report forms fits a finance controller, and what does each cost?

| Option | What Anand reads | What he can act on | What he can audit |
|---|---|---|---|
| A. One number: the total gap | 1 line | Nothing: no channel, no order | Nothing |
| B. A table by channel | 3 channels and a total | Which channel to chase | The totals, against booked |
| C. The table by channel, with the reconciliation above it and the two lists beneath | The table, 4 reconciliation lines, 2 lists | Which channel, and which orders | Every figure, back to the bridge |
| D. The whole statement, one line per order | 462 lines on Kalpa's Q2 | Anything, once found | Everything, if read |

The cell below sizes each form on Kalpa's Q2 by what it asks of the reader.
"""),
        code("""
orders_q2 = sum(r["orders"] for r in booked_ch)
forms = [("A. one number", 1, "none", "none"), ("B. by channel", len(booked_ch) + 1, "channel", "totals"),
         ("C. by channel, reconciled, with lists", len(booked_ch) + 1 + 4, "channel and order", "every figure"),
         ("D. the whole statement", orders_q2, "order, once found", "every line")]
kit.table(["Form", "Lines Anand reads, before any list", "He can act on", "He can audit"], forms,
          caption="Four report forms, sized on Kalpa's Q2")
kit.bars([(f[0], f[1]) for f in forms], lit=[2], title="Lines Anand reads before he can act")
kit.check("the statement form asks Anand to read one line per Q2 order", forms[3][1] == 462, f"{orders_q2} lines")"""),
        md("""
**The best-fit call.** Form C fits best: the table by channel, with the reconciliation written above
it and the two lists beneath. It is the smallest page on which Anand can both act, by channel and
by order, and audit, since every figure ties back to the bridge. A alone hides where the gap sits; B tells the
store team to chase without telling them whom; D answers everything and asks Anand to find it in
462 lines.

**The fact that would change the call.** At the quarter's close, when the auditors ask for evidence
order by order, D travels with the signed page as an appendix file; the page itself stays C.
"""),
        md("""
## 1. What must a line per channel carry for Anand to sign it?

Each channel gets one line with the orders booked, booked, collected and the gap, and a definition
line sits above the table, "collected: cash received against Q2 orders, each payment counted once;
posted twice and refunds are shown separately", so no reader has to guess which of the day's numbers
this is. The report is built from chapter 3's table of one row per order, grouped by channel.

**Predict before you run.** On the invented tables, which channel carries booked of 1,800?
a) web; b) store; c) app; d) none, every channel books 2,000.
"""),
        code(f"""
fixed_tiny = run(\"\"\"{Q5['tiny_fixed']}\"\"\")
kit.columns([r["channel"] for r in fixed_tiny],
            [("booked", [float(r["booked"]) for r in fixed_tiny]),
             ("collected", [float(r["collected"] or 0) for r in fixed_tiny])],
            fmt=lambda v: f"{{v:,.0f}}", title="Invented: booked and collected by channel")
kit.columns([r["channel"] for r in booked_ch], [("booked, Rs crore", [float(r["booked"]) / 1e7 for r in booked_ch])],
            fmt=lambda v: f"{{v:.2f}}", title="Kalpa's Q2 booked by channel, from orders alone")
kit.check("the channels' booked adds to Monday's Rs 9,84,00,000",
          sum(r["booked"] for r in booked_ch) == 98400000, kit.rupees(sum(r["booked"] for r in booked_ch)))"""),
        md("""
**What happened.** The answer is c: app books 1,800, T-1's 1,000 and T-4's 800, and collects 1,000;
web and store each book 2,000 and collect it. On Kalpa's Q2, app books Rs 4,25,90,270 over 153
orders, store Rs 3,21,48,730 over 159 and web Rs 2,36,61,000 over 150, adding to Monday's
Rs 9,84,00,000.

## 2. What does the gap column say when each order's gap is added up?

**The plausible wrong answer.** Anand asked "order by order", so a teammate computes each order's
gap, booked less collected, and adds the gaps up by channel:

```sql
SELECT channel, count(*) AS orders, sum(booked) AS booked, sum(collected) AS collected,
       sum(booked - collected) AS gap
FROM per_order
GROUP BY channel;
```

**Predict before you run.** On the invented tables, what does the gap column say for app?
a) 800; b) 0; c) NULL; d) 1,800.
"""),
        code(f"""
hurried_tiny = run(\"\"\"{Q5['tiny_hurried']}\"\"\")
show(hurried_tiny, "Invented: the gap column, each order's gap added up")
hurried_kalpa = run(\"\"\"{Q5['kalpa_hurried']}\"\"\")
kit.table(["Channel", "Gap, as the hurried report states it"],
          [(r["channel"], kit.rupees(r["gap"] or 0)) for r in hurried_kalpa],
          caption="Kalpa's Q2: the gap column the teammate would send")
kit.bars([(r["channel"], float(r["gap"] or 0)) for r in hurried_kalpa] or [("none", 0)],
         fmt=lambda v: kit.rupees(v), title="Kalpa's Q2: nothing outstanding on any channel, as reported")"""),
        md("""
**What happened.** The answer is b: the gap column says 0 for app, and 0 for every channel, on the
invented tables and on Kalpa's Q2 alike. Read as it stands, the report says Kalpa collected every
rupee it booked, on every channel, and Anand signs a page that stands his collections team down.
"""),
        md("""
## 3. Why does the gap column read zero, and which check catches it?

**Why it is wrong.** An order nobody paid has no collected figure: its `collected` is NULL, since the
LEFT JOIN found no payment for it. `booked - NULL` is NULL, which loses the booked amount, and
`sum()` skips NULLs without saying so, the same way Monday's AVG skipped them. So the unpaid
orders, the very orders the gap exists to show, drop out of the gap, and every paid order at Kalpa
was paid in full, so what remains adds to zero.

**The check that catches it.** The gap column must equal booked less collected computed as two
separate sums, which `sum()` handles correctly because each column is summed on its own; and no
order may reach the report with a NULL gap. On the invented tables the gap column says 0 for app,
two separate sums say 1,800 less 1,000, which is 800, and one order, T-4, carries a NULL gap.
"""),
        code(f"""
gaps = run(\"\"\"{Q5['tiny_per_order_gap']}\"\"\")
show(gaps, "Invented: one row per order, where T-4's gap is NULL")
app = next(r for r in hurried_tiny if r["channel"] == "app")
two_sums = app["booked"] - app["collected"]
null_gaps = sum(1 for r in gaps if r["gap"] is None)
kit.flow(["T-4\\nbooked 800", "collected\\nNULL, never paid", "booked - collected\\nNULL", "sum()\\nskips it"],
         kinds=["known", "unknown", "bad", "bad"], title="Invented: how an unpaid order leaves the gap")
kit.check("the check catches it: app's gap column disagrees with booked less collected",
          (app["gap"] or 0) != two_sums, f'{{int(app["gap"] or 0):,}} against {{int(two_sums):,}}')
kit.check("the check catches it: one invented order reaches the report with a NULL gap", null_gaps == 1, "T-4")"""),
        md("""
**The fix, and what changed.** `coalesce(collected, 0)` says on purpose that an order with no payment
collected nothing, so its gap is its whole booked amount:

```sql
sum(booked - coalesce(collected, 0)) AS gap
```

On the invented tables app's gap becomes 800, T-4, and every other channel stays at 0. The report now
agrees with the bridge: its gaps add to the never-paid bar, since nothing was paid short.
"""),
        code(f"""
kit.bridge(("gap, as reported", 0.0),
           [("T-4 back in, app", float(next(r["gap"] for r in fixed_tiny if r["channel"] == "app")))],
           end_label="gap, fixed", fmt=lambda v: f"{{v:,.0f}}", lit=[0],
           title="Invented: coalesce puts the unpaid order back in the gap")
kit.check("the fixed invented report's gaps add to the never-paid bar",
          sum(r["gap"] for r in fixed_tiny) == 800, f'{{int(sum(r["gap"] for r in fixed_tiny)):,}}')"""),
        md("""
## 4. Does the fixed report add back to the bridge on Kalpa's Q2?

**Your turn.** Build the page Anand signs. In the empty cell below, type:

```python
page = run(Q_REPORT)
show(page, "Booked against collected, Q2, by channel",
     money=["booked", "collected", "gap", "posted_twice"])
```

`Q_REPORT` adds, beside the gap, the share collected, the orders never paid and the amount posted
twice, per channel. The cell after it defines the query and checks, without printing any figure,
that the page adds back to the bridge from chapter 3.
"""),
        empty(),
        code(f"""
Q_REPORT = \"\"\"{Q5['kalpa_full']}\"\"\"
page_rows = run(Q_REPORT)
kit.vflow(["the page: one line per channel", "orders add to 462, booked to Rs 9,84,00,000",
           "gaps add to never paid plus paid short", "posted twice adds to its bar"],
          kinds=["plain", "good", "good", "good"], title="What the page must add back to")
kit.check("the page's orders add to Q2's 462", sum(r["orders"] for r in page_rows) == 462, "462")
kit.check("the page's booked adds to Monday's figure", sum(r["booked"] for r in page_rows) == kb["booked"],
          kit.rupees(kb["booked"]))
kit.check("the page's gaps add to never paid plus paid short",
          sum(r["gap"] for r in page_rows) == kb["never_paid"] + kb["paid_short"], "equal to the rupee")
kit.check("the page's posted twice adds to its bar", sum(r["posted_twice"] for r in page_rows) == kb["posted_twice"],
          "equal to the rupee")"""),
        md("""
Kavya Nair, the team's senior analyst, reviews every number before it leaves the team.

> **Kavya's review.** "Every rupee on the page ties back to a bar, and every bar to a list. Write the
> definition of collected above the table, so nobody reads it as posted."
"""),
        md("""
## Does the unpaid list, grouped by channel, give the same gap?

The second route builds the gap by channel from a different place: chapter 4's unpaid list, written
with NOT EXISTS, grouped by channel. It never computes a per-order gap, so a NULL cannot fall out of
it. Nothing on Kalpa's Q2 was paid short, so the gap by channel must equal the unpaid list by
channel, channel for channel.
"""),
        code(f"""
un_tiny = {{r["channel"]: r["never_paid"] for r in run(\"\"\"{Q5['tiny_unpaid_by_channel']}\"\"\")}}
kit.columns([r["channel"] for r in fixed_tiny],
            [("gap, the page", [float(r["gap"]) for r in fixed_tiny]),
             ("unpaid list, grouped", [float(un_tiny.get(r["channel"], 0)) for r in fixed_tiny])],
            fmt=lambda v: f"{{v:,.0f}}", title="Invented: two routes to the gap by channel")
kit.check("invented: the gap by channel equals the unpaid list by channel",
          all(r["gap"] == un_tiny.get(r["channel"], 0) for r in fixed_tiny), "app 800, web 0, store 0")
un_kalpa = {{r["channel"]: r["never_paid"] for r in run(\"\"\"{Q5['kalpa_unpaid_by_channel']}\"\"\")}}
kit.check("Kalpa's Q2: the gap by channel equals the unpaid list by channel, on every channel",
          all(r["gap"] == un_kalpa.get(r["channel"], 0) for r in page_rows), "equal to the rupee, unprinted")
refunds = run(\"\"\"{Q5['refunds']}\"\"\")
kit.check("the refunds table holds no refund against a Q2 order", all(r["quarter"] != "Q2" for r in refunds),
          ", ".join(f'{{r["quarter"]}}: {{r["refund_rows"]}} rows' for r in refunds))"""),
        md("""
**What happened.** The two routes agree channel for channel, on the invented tables and on Kalpa's Q2.
The last check answers the one part of Anand's message the report has not touched, refunds: every
refund row in the warehouse sits on a Q1 order, so the Q2 page says so in one line under the table.

**The sentence to Anand.** The page ends on one sentence he can repeat, with the figures you read
from your own page. Its last clause is earned in chapter 6, where the checks are built and each is
seen to fail:

> "Q2 booked Rs 9,84,00,000 and collected Rs ___, each payment counted once. The gap of Rs ___ is
> ___ orders nobody has paid, listed by channel, largest first. Separately, Rs ___ was posted twice
> by gateway retries and ___ payments match no order; both lists go to the platform lead. Every
> figure ties back to the orders and payments tables through checks that have each been seen to
> fail."

### In the interview: is a small gap worth chasing?

The tags mark how often a question comes up: [S] a staple asked everywhere, [F] frequent in GCC and product screens, [D] a differentiator.

**[D] Anand says the gap is too small to matter: how do you decide whether to chase it?** Size it before judging it. Put it as a share of booked, then split it by channel and by order, since a
small total can be one large invoice, and ask whether the unpaid orders cluster in one channel;
check how old each unpaid order is, since at Kalpa a paid order is paid within days of being booked,
so an unpaid order from July is already overdue; and set the cost of chasing, a call or a reminder,
against the cash each order carries. Then recommend chasing the large and old ones first, and say
what you would drop. Keep booked and collected beside the gap while you argue it, since a gap on its
own cannot be checked: the subtraction that shows it is right also exposes a NULL that fell out of
it.

### Depth: why does SQL let NULL fall out of a sum without a warning?

The SQL standard defines aggregate functions such as SUM and AVG to ignore NULLs, so a column with
missing values still sums. The price is that a missing value and a zero look the same in a total.
The defence is to decide, per column, what a NULL means in the business, and to write that decision
into the query with `coalesce`, which Monday met in its NULL trap.
"""),
        md("""
## What did this chapter answer, one line per question?

1. The table by channel, reconciled above and with the two lists beneath, fits a finance controller:
   he can act by channel and order and audit every figure.
2. A line per channel carries the orders, booked, collected and the gap, under a definition line; on
   Kalpa's Q2 booked is app Rs 4,25,90,270, store Rs 3,21,48,730 and web Rs 2,36,61,000.
3. Adding each order's gap reports 0 on every channel, on the invented tables and on Kalpa's Q2.
4. It is wrong because an unpaid order's gap is NULL and `sum()` skips it; the gap column against
   booked less collected as two sums catches it, and `coalesce(collected, 0)` fixes it.
5. The fixed page adds back to the bridge on Kalpa's Q2: 462 orders, Rs 9,84,00,000 booked, the gaps
   and the amount posted twice each equal to their bars.
6. The unpaid list grouped by channel gives the same gap on every channel.

**The question this leaves.** The page is right today, so chapter 6 asks what must pass, every
Monday, before the collected number leaves the team, and what Anand gets when a check fails at the
end of reporting day.
"""),
        code("kit.check_summary()"),
    ]
    build(nb_path(n), cells)
    write_sql(n, ["The report by channel Anand signs: the hurried gap column, the fix, and the full page.",
                  "Run the Kalpa page yourself; the figures are yours to read."],
              [("Setup: the two invented tables", TINY),
               ("Booked by channel, Kalpa's Q2, from orders alone", Q2["booked_by_channel"]),
               ("The trap, invented: each order's gap added up", Q5["tiny_hurried"]),
               ("The trap on Kalpa's Q2", Q5["kalpa_hurried"]),
               ("Why: one row per order, invented, where T-4's gap is NULL", Q5["tiny_per_order_gap"]),
               ("The fix, invented: coalesce(collected, 0)", Q5["tiny_fixed"]),
               ("Your turn: the page Anand signs, Kalpa's Q2", Q5["kalpa_full"]),
               ("The second route: the unpaid list by channel, Kalpa's Q2", Q5["kalpa_unpaid_by_channel"]),
               ("Refunds, by the quarter of their order", Q5["refunds"])])
    print("chapter 5 written")

# ============================================================================================== 6
# The day's five wrong pages on the invented tables, each written with the mistake its chapter staged,
# then the true page. Each returns orders, booked, collected, gap
# and the channels it covers. Chapter 3's per-order table becomes a TEMP view for the last three.
VIEWS = """
CREATE TEMP VIEW tiny_per_order AS
{tiny};
CREATE TEMP VIEW q2_per_order AS
{kalpa};""".format(tiny=PER_ORDER.format(orders="tiny_orders", payments="tiny_payments", where="").strip("\n"),
                   kalpa=PER_ORDER.format(orders="orders", payments="payments",
                                          where="WHERE o.quarter = 'Q2'").strip("\n"))

WRONG_REPORTS = {
    "fan-out draft": """
SELECT count(*) AS orders,
       (SELECT sum(amount) FROM tiny_orders) AS booked,
       sum(o.amount) FILTER (WHERE p.payment_id IS NOT NULL) AS collected,
       (SELECT sum(amount) FROM tiny_orders)
           - sum(o.amount) FILTER (WHERE p.payment_id IS NOT NULL) AS gap,
       array_agg(DISTINCT o.channel) AS channels
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id""",
    "plain JOIN draft": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS collected,
       sum(o.amount) - sum(pp.posted) AS gap, array_agg(DISTINCT o.channel) AS channels
FROM tiny_orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id""",
    "posted as collected": """
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS collected,
       sum(o.amount) - sum(pp.posted) AS gap, array_agg(DISTINCT o.channel) AS channels
FROM tiny_orders o
LEFT JOIN posted_per_order pp ON pp.order_id = o.order_id""",
    "quarter in WHERE": """
WITH per_order AS (
    SELECT o.order_id, o.channel, o.amount AS booked, sum(i.amount) AS collected
    FROM tiny_orders o
    LEFT JOIN (SELECT order_id, instalment_no, max(amount) AS amount, max(paid_date) AS paid_date
               FROM tiny_payments
               GROUP BY order_id, instalment_no) i ON i.order_id = o.order_id
    WHERE i.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
    GROUP BY o.order_id, o.channel, o.amount
)
SELECT count(*) AS orders, sum(booked) AS booked, sum(collected) AS collected,
       sum(booked) - sum(collected) AS gap, array_agg(DISTINCT channel) AS channels
FROM per_order""",
    "gap summed per order": """
SELECT count(*) AS orders, sum(booked) AS booked, sum(collected) AS collected,
       sum(booked - collected) AS gap, array_agg(DISTINCT channel) AS channels
FROM tiny_per_order""",
    "true report": """
SELECT count(*) AS orders, sum(booked) AS booked, sum(coalesce(collected, 0)) AS collected,
       sum(booked - coalesce(collected, 0)) AS gap, array_agg(DISTINCT channel) AS channels
FROM tiny_per_order""",
}

# Where the room met each wrong page, printed beside its figures.
ORIGIN = {
    "fan-out draft": "Chapter 2: the order amount summed on every payment row",
    "plain JOIN draft": "Chapter 3: an INNER JOIN, posted read as collected",
    "posted as collected": "Chapter 3: the join fixed to LEFT, posted still read as collected",
    "quarter in WHERE": "Chapter 4: the quarter's dates on payments, placed in WHERE",
    "gap summed per order": "Chapter 5: each order's gap added up, T-4's NULL skipped",
    "true report": "Chapter 5: the page Anand signs",
}

SOURCES = """
SELECT (SELECT count(*) FROM {orders} o{where})                           AS orders,
       (SELECT sum(amount) FROM {orders} o{where})                        AS booked,
       (SELECT sum(amount) FROM {payments}
         WHERE order_id IN (SELECT order_id FROM {orders} o{where}))      AS posted,
       (SELECT sum(amount) FROM {orders} o {where_and}
            NOT EXISTS (SELECT 1 FROM {payments} p
                        WHERE p.order_id = o.order_id))                   AS never_paid,
       (SELECT sum(o.amount - c.collected)
          FROM {orders} o
          JOIN (SELECT order_id, sum(amount) AS collected
                  FROM (SELECT order_id, instalment_no, max(amount) AS amount
                          FROM {payments}
                         GROUP BY order_id, instalment_no) AS once
                 GROUP BY order_id) AS c ON c.order_id = o.order_id
         {where_and} c.collected < o.amount)                              AS paid_short,
       (SELECT sum(extra)
          FROM (SELECT sum(p.amount) - max(p.amount) AS extra
                FROM {payments} p JOIN {orders} o ON o.order_id = p.order_id{where}
                GROUP BY p.order_id, p.instalment_no) AS repeats)         AS posted_twice"""


def sources_sql(orders, payments, where=""):
    where_and = (where + " AND") if where else "WHERE"
    spaced = (" " + where) if where else ""
    return SOURCES.format(orders=orders, payments=payments, where=spaced, where_and=where_and).strip("\n")


Q6 = {name: q.strip("\n") for name, q in WRONG_REPORTS.items()}
Q6_SOURCES_TINY = sources_sql("tiny_orders", "tiny_payments")
Q6_SOURCES_KALPA = sources_sql("orders", "payments", "WHERE o.quarter = 'Q2'")
Q6_TRUE_KALPA = WRONG_REPORTS["true report"].replace("tiny_per_order", "q2_per_order").strip("\n")

SUITES = '''
PLAUSIBLE = [
    ("collected is at most booked", lambda r, s: r["collected"] <= r["booked"]),
    ("the gap is not negative", lambda r, s: r["gap"] is not None and r["gap"] >= 0),
    ("all three channels are on it", lambda r, s: set(r["channels"]) >= {"app", "store", "web"}),
]
TIE_BACK = [
    ("orders on the report equal orders in the table", lambda r, s: r["orders"] == s["orders"]),
    ("booked equals booked from orders alone", lambda r, s: r["booked"] == s["booked"]),
    ("the gap equals booked less collected", lambda r, s: r["gap"] == r["booked"] - r["collected"]),
    ("the gap equals the never-paid and paid-short lists",
     lambda r, s: r["gap"] == (s["never_paid"] or 0) + (s["paid_short"] or 0)),
    ("collected plus posted twice equals posted from payments alone",
     lambda r, s: r["collected"] + (s["posted_twice"] or 0) == s["posted"]),
]


def validate(report, source, suite):
    """Every check in the suite, run on one report against the single-table sources."""
    return [(name, bool(test(report, source))) for name, test in suite]
'''

CH6_STEPS = ["the need: a PASS that cannot fail", "the options: four ways to validate, sized",
             "the trap: three checks, three passes", "the tie-back suite",
             "every wrong report of the day, tested", "Kalpa's report, tested",
             "a second route: another tool, the raw rows", "the reporting-day rule"]


def chapter6():
    n = 6
    ladder = ["Do the checks a hurried analyst writes pass a report that hides an unpaid order?",
              "Which checks tie the report back to the two tables?",
              "Does the suite fail every wrong report the day has met?",
              "Does the tie-back suite pass Kalpa's Q2 report?",
              "Does a second tool, working from the raw rows, reach the same numbers?",
              "What does Anand get when a check fails at the end of reporting day?"]
    cells = [
        title_cell(
            n,
            "Kavya Nair, the team's senior analyst, reviews every number before it leaves the team, "
            "Anand forwards it to "
            "the CEO's Monday page, and you sign it. A validation that cannot fail puts a PASS "
            "stamp on a wrong number, and a stamped wrong number is harder to withdraw than an "
            "unstamped one.",
            ladder,
            "At stake are the collected figure and its gap, every Monday, and the checks that stand "
            "between them and Anand, each measured by which of the day's wrong reports it would stop.",
            "Chapter 5 built the page Anand signs: one line per channel, with orders, booked, collected "
            "and a gap that uses `coalesce(collected, 0)`, so an unpaid order counts as nothing paid. "
            "On the invented tables app's gap is 800, T-4; on Kalpa's Q2 you built the page and it added "
            "back to the bridge. Over the day five wrong pages appeared, each plausible: chapter 2's "
            "fan-out draft, chapter 3's plain JOIN draft and its LEFT JOIN that still read posted as "
            "collected, chapter 4's quarter in WHERE, and chapter 5's gap added up order by order. This "
            "chapter builds the checks that stop all five, every Monday, before the number leaves."),
        md("""
**Setup.** The next cell finds the helper, connects to the warehouse, creates the invented tables of
chapter 1, and writes on them the day's five wrong pages, each with the mistake its chapter staged.
Every query below is also in `sql/C2_W02_D02_06_can_it_leave_STUDENT.sql`.
"""),
        code(HELPERS + SUITES + f'''
with conn.cursor() as cur:
    cur.execute("""{VIEWS}""")   # chapter 3's per-order table, as TEMP views
''' + "\nWRONG = {}\n"
             + "".join(f'WRONG[{name!r}] = """{q}"""\n' for name, q in Q6.items()) + f"""
reports = {{name: run(q)[0] for name, q in WRONG.items()}}
src_tiny = run(\"\"\"{Q6_SOURCES_TINY}\"\"\")[0]
print("Written on the invented tables:", ", ".join(reports), sep="\\n  ")"""),
        map_cell(n, CH6_STEPS),
        md(f"""
## What does a PASS stamp cost when the check behind it could not fail?

The Monday number is refreshed every week, by whoever is on the rota, sometimes late on reporting
day. Checks let a number leave without Kavya reading every query. A check is useful only if it can
fail, and a suite that passes a wrong report does worse than no suite, because the PASS line travels
with the number and Anand forwards it with more confidence than he would forward an
unchecked one. {DOSSIER}
"""),
        md(COMPANY[6]),
        md(TINY_NOTE),
        md("""
**The day's five wrong pages.** Each is one of the day's mistakes, written on the invented tables into
a page of orders, booked, collected and gap. The true page from chapter 5 sits last. Every page
carries all three channels.
"""),
        code(f"""
ORIGIN = {ORIGIN!r}
kit.table(["Page", "Where the day met it", "Orders", "Booked", "Collected", "Gap"],
          [(name, ORIGIN[name], r["orders"], f'{{int(r["booked"]):,}}', f'{{int(r["collected"]):,}}',
            f'{{int(r["gap"]):,}}') for name, r in reports.items()],
          caption="Invented: the day's five wrong pages and the true one")"""),
        md("""
## Which of four ways to validate stops the day's wrong reports, and what does each cost?

| Option | What it does | What it needs |
|---|---|---|
| A. Read the report before sending it | A person looks at the page | Someone who knows the numbers, every Monday |
| B. Plausibility checks | Collected at most booked, no negative gap, every channel present | Only the report itself |
| C. Tie-back checks | Every figure on the report recomputed from the source tables and compared | The two source tables |
| D. An independent recomputation | The same figures from the raw rows by another tool, or from the gateway's settlement file | A second method, or a second source |

The cell below runs B, C and D against the five wrong reports rebuilt above, counts how many each
stops, and times each on Kalpa's Q2. A is not sized, since what it catches depends on who reads.
"""),
        code(f"""
import time


def recompute_in_python(orders_rows, payment_rows):
    \"\"\"Orders, booked, collected and the gap from the raw rows, with no join: Week 1's accumulator.\"\"\"
    booked = {{o["order_id"]: o["amount"] for o in orders_rows}}
    once = {{}}
    for p in payment_rows:                      # a repeat of one instalment overwrites, so it counts once
        if p["order_id"] in booked:
            once[(p["order_id"], p["instalment_no"])] = p["amount"]
    collected = sum(once.values())
    return {{"orders": len(booked), "booked": sum(booked.values()), "collected": collected,
            "gap": sum(booked.values()) - collected}}


py_tiny = recompute_in_python(run("SELECT order_id, channel, amount FROM tiny_orders"),
                              run("SELECT order_id, instalment_no, amount FROM tiny_payments"))
wrong_names = [k for k in reports if k != "true report"]
stops = {{"B. plausibility": 0, "C. tie-back": 0, "D. recompute": 0}}
for name in wrong_names:
    r = reports[name]
    stops["B. plausibility"] += not all(ok for _, ok in validate(r, src_tiny, PLAUSIBLE))
    stops["C. tie-back"] += not all(ok for _, ok in validate(r, src_tiny, TIE_BACK))
    stops["D. recompute"] += any(r[k] != py_tiny[k] for k in ("orders", "booked", "collected", "gap"))
t0 = time.perf_counter(); rep_k = run(\"\"\"{Q6_TRUE_KALPA}\"\"\")[0]; t_report = time.perf_counter() - t0
t0 = time.perf_counter(); src_k = run(\"\"\"{Q6_SOURCES_KALPA}\"\"\")[0]; t_src = time.perf_counter() - t0
t0 = time.perf_counter()
py_k = recompute_in_python(run("SELECT order_id, channel, amount FROM orders WHERE quarter = 'Q2'"),
                           run("SELECT order_id, instalment_no, amount FROM payments"))
t_py = time.perf_counter() - t0
kit.table(["Option", "Wrong reports it stops, of 5", "Time on Kalpa's Q2"],
          [("A. read it", "depends on the reader", "minutes of a person"),
           ("B. plausibility", stops["B. plausibility"], f"{{t_report * 1000:.0f}} ms, the report alone"),
           ("C. tie-back", stops["C. tie-back"], f"{{(t_report + t_src) * 1000:.0f}} ms, report and sources"),
           ("D. recompute in Python", stops["D. recompute"], f"{{t_py * 1000:.0f}} ms, the raw rows")],
          caption="Four ways to validate, sized on the day's five wrong reports and on Kalpa's Q2")
kit.bars([(k, v) for k, v in stops.items()], lit=[1], title="Wrong reports stopped, of the day's five")
kit.check("the tie-back suite stops all five wrong reports", stops["C. tie-back"] == 5, f'{{stops["C. tie-back"]}} of 5')"""),
        md("""
**The best-fit call.** Option C, the tie-back suite, fits best, with D beside it. The tie-back
suite stops all five of the day's wrong reports and runs in milliseconds, because each check compares a figure on the report
with the same figure computed outside it: booked from orders alone, posted from payments alone, and
the gap from lists no join can multiply.
The Python recomputation reaches the numbers by a different tool and a different rule for counting a
payment once, so an error in the SQL and the same error in the checks would still be caught.
Plausibility checks cost the same and stop three of the five.

**The fact that would change the call.** A settlement file from the gateway, the list of what
actually reached Kalpa's bank, would be a source outside Kalpa's own tables, and reconciling to it
would become the strongest check of all; until the platform lead supplies one, every check here
reads Kalpa's own records.
"""),
        md("""
## 1. Do the checks a hurried analyst writes pass a report that hides an unpaid order?

**The plausible wrong answer.** A hurried validation checks what a finance reader expects to be true
of any collections report: collected is at most booked, the gap is not negative, and all three
channels are on the page. It runs on the page written with chapter 4's mistake, the quarter's dates
on payments placed in WHERE, which dropped T-4.

**Predict before you run.** How many of the three checks pass? a) none; b) one; c) two; d) all three.
"""),
        code("""
hidden = reports["quarter in WHERE"]
verdicts = validate(hidden, src_tiny, PLAUSIBLE)
kit.table(["Plausibility check", "On the quarter-in-WHERE page"], [(n_, "PASS" if ok else "FAIL") for n_, ok in verdicts],
          caption=f'Invented: a page of {hidden["orders"]} orders, booked {int(hidden["booked"]):,}, gap {int(hidden["gap"]):,}')
kit.flow(["the quarter-in-WHERE page\\nT-4 dropped", "3 plausibility checks", "3 of 3 pass", "the number leaves"],
         kinds=["bad", "plain", "bad", "bad"], title="Invented: a suite that cannot see a missing order")
kit.check("the plausibility suite passes the report that hides T-4", all(ok for _, ok in verdicts), "3 of 3")"""),
        md("""
**What happened.** The answer is d: all three pass. The page shows 4 orders, booked 5,000, collected
5,000 and a gap of 0, and every one of those is internally consistent.

**Why it is wrong.** Each check tests the report against itself. The missing order took its booked
amount with it, so collected is still at most booked, the gap is still not negative, and T-4's
channel, app, is still on the page through T-1. A suite that never looks outside the report cannot
see what the report left out, and it stamps "3 of 3 passed" on a page that hides the one order
nobody paid.
"""),
        md("""
## 2. Which checks tie the report back to the two tables?

Each tie-back check recomputes one figure outside the report and compares it with the report:

| Check | Computed from | Catches |
|---|---|---|
| Orders on the report equal orders in the table | `orders` alone | A dropped or repeated order |
| Booked equals booked from orders alone | `orders` alone | A fan-out, a dropped order |
| The gap equals booked less collected | The report's own columns | A NULL that fell out of a sum |
| The gap equals the never-paid and paid-short lists | The anti-join, and each order's instalments against its booked | A dropped order, a NULL gap, a wrong list |
| Collected plus posted twice equals posted from payments alone | `payments` alone | A retry inside collected, a fan-out |

**Predict before you run.** On the same page, which checks fail? a) none; b) orders, booked and the
two lists; c) only the gap; d) all five.
"""),
        code("""
tie = validate(hidden, src_tiny, TIE_BACK)
kit.table(["Tie-back check", "On the quarter-in-WHERE page"], [(n_, "PASS" if ok else "FAIL") for n_, ok in tie],
          caption="Invented: the same page, checked against the two tables")
kit.check("the tie-back suite fails the quarter-in-WHERE page on orders, booked and the two lists",
          [ok for _, ok in tie] == [False, False, True, False, True], "3 checks fail")"""),
        md("""
**What happened.** The answer is b: orders (4 against 5), booked (5,000 against 5,800) and the two
lists (a gap of 0 against 800 never paid and nothing paid short) all fail, while the page's own
arithmetic and its collected figure pass. The page is internally correct and externally wrong, and
only a check that looks outside it can say so.

## 3. Does the suite fail every wrong report the day has met?

**Predict before you run.** The plausibility suite stops three of the day's five wrong pages. Which
two does it let through? a) the fan-out and plain JOIN drafts; b) the quarter in WHERE and the summed
gap; c) posted as collected and the quarter in WHERE; d) the fan-out draft and the summed gap.
"""),
        code("""
grid, rows = [], []
for name in wrong_names:
    p_ok = all(ok for _, ok in validate(reports[name], src_tiny, PLAUSIBLE))
    t_fail = [n_ for n_, ok in validate(reports[name], src_tiny, TIE_BACK) if not ok]
    grid.append(["passes" if p_ok else "fails", f"fails {len(t_fail)} of 5"])
    rows.append(name)
kit.matrix(rows, ["plausibility suite", "tie-back suite"], grid,
           title="Invented: the day's five wrong reports, against both suites")
through = [name for name, g in zip(rows, grid) if g[0] == "passes"]
kit.check("the plausibility suite lets through only the two wrong pages that hide T-4",
          sorted(through) == ["gap summed per order", "quarter in WHERE"], f"{len(through)} of 5")
kit.check("the tie-back suite fails every wrong report on at least one check",
          all(g[1] != "fails 0 of 5" for g in grid), "5 of 5 stopped")
kit.check("the tie-back suite passes the true report",
          all(ok for _, ok in validate(reports["true report"], src_tiny, TIE_BACK)), "5 of 5 pass")"""),
        md("""
**What happened.** The answer is b: the plausibility suite lets through the quarter in WHERE and the
gap summed per order, the two pages that hide T-4. It stops the other three because each puts more
cash on the page than was booked: the fan-out draft's 8,500 against 5,800, and posted read as
collected, 6,500 against 5,000 in the plain JOIN draft and against 5,800 after the LEFT JOIN. A page
that hides an order lowers its figures together, or loses the gap to a NULL, so nothing on it looks
wrong. The tie-back suite fails every wrong page on at least one check, the fan-out draft on orders,
the two lists and posted, and passes the true page on all five.

## 4. Does the tie-back suite pass Kalpa's Q2 report?

The same suite runs on Kalpa's Q2 page from chapter 5. The verdicts print; the figures that would
name what the room is finding stay unprinted.
"""),
        code("""
tie_k = validate(rep_k, src_k, TIE_BACK)
detail = {
    "orders on the report equal orders in the table": f'{rep_k["orders"]} against {src_k["orders"]}',
    "booked equals booked from orders alone": f'{kit.rupees(rep_k["booked"])} against {kit.rupees(src_k["booked"])}',
}
kit.table(["Tie-back check, Kalpa's Q2", "Verdict", "Detail"],
          [(n_, "PASS" if ok else "FAIL", detail.get(n_, "equal, unprinted")) for n_, ok in tie_k],
          caption="The suite on Kalpa's Q2 report")
kit.vflow(["Kalpa's Q2 page", "5 tie-back checks", "5 of 5 pass", "the number may leave"],
          kinds=["known", "plain", "good", "good"], title="Kalpa's Q2: the number may leave")
kit.check("every tie-back check passes on Kalpa's Q2 report", all(ok for _, ok in tie_k), "5 of 5")
homes = run(\"\"\"SELECT coalesce(o.quarter, 'no order') AS home, count(*) AS n FROM payments p
                 LEFT JOIN orders o ON o.order_id = p.order_id GROUP BY 1\"\"\")
kit.check("every payment row sits on a Q1 order, a Q2 order or no order, and they add to the table",
          sum(h["n"] for h in homes) == one("SELECT count(*) FROM payments"), "1,428 rows, split unprinted")"""),
        md("""
**What happened.** Every check passes on Kalpa's Q2 report: 462 orders against 462, booked
Rs 9,84,00,000 against Rs 9,84,00,000, the gap equal to the never-paid and paid-short lists, and the
retries equal to posted less collected. This report may leave the team.

> **Kavya's review.** "A check that cannot fail is decoration. For every check, tell me which wrong
> report it would have stopped, and do not send me a PASS you have never seen fail."
"""),
        md("""
## Does a second tool, working from the raw rows, reach the same numbers?

The second route leaves SQL's joins behind. Two plain SELECTs fetch the raw rows, one table each, and
Python counts them with Week 1's accumulator: booked per order from `orders`, and each order's
instalments from `payments`, keyed by order and instalment so that a repeat of the same instalment
overwrites itself and counts once. It shares no join, no GROUP BY and no NULL rule with the SQL
report, so a mistake in one is unlikely to repeat in the other.
"""),
        code("""
true_tiny = reports["true report"]
kit.columns(["orders", "booked", "collected", "gap"],
            [("SQL report", [float(true_tiny[k]) for k in ("orders", "booked", "collected", "gap")]),
             ("Python, raw rows", [float(py_tiny[k]) for k in ("orders", "booked", "collected", "gap")])],
            fmt=lambda v: f"{v:,.0f}", title="Invented: two tools, one set of numbers")
kit.check("invented: Python from the raw rows matches the SQL report on all four figures",
          all(true_tiny[k] == py_tiny[k] for k in ("orders", "booked", "collected", "gap")), "5 orders, 5,800, 5,000, 800")
kit.check("Kalpa's Q2: Python from the raw rows matches the SQL report on all four figures",
          all(rep_k[k] == py_k[k] for k in ("orders", "booked", "collected", "gap")), "equal, unprinted")"""),
        md("""
**What happened.** The two tools agree on all four figures, on the invented tables (5 orders, booked
5,800, collected 5,000, gap 800) and on Kalpa's Q2. The Python route has its own blind spot, since
it assumes a retry repeats the same amount, which chapter 3's cap method checked; each route covers
a place the other cannot see.

## 5. What does Anand get when a check fails at the end of reporting day?

The day a check fails matters, because late on reporting day there may be no time to fix it.

**Predict before you run.** Which does the team send? a) nothing until the check is fixed; b) booked,
which ties to orders alone, with the open line named and collected held; c) the collected figure with
a footnote saying one check failed; d) last week's collected figure.
"""),
        code("""
kit.tree({"label": "a check fails\\non reporting day", "branches": [
    ("booked checks pass", {"label": "send booked\\nwith the open line", "kind": "good"}),
    ("booked checks fail", {"label": "send booked from\\norders alone; hold collected", "kind": "bad"}),
]}, taken=["booked checks pass"], title="The reporting-day rule: booked leaves, an unreconciled collected never does")"""),
        md("""
**What happened.** The answer is b. The team works to one rule: booked always leaves, because it ties
to the orders table alone; an unreconciled collected figure never leaves; and the open line, which
check failed, what it means and when it will be fixed, goes with it. Option c is the one people send,
and it puts an unreconciled figure on the CEO's page.

| The check that fails | What it means | What Anand gets that day | Who fixes it |
|---|---|---|---|
| Orders on the report against the table | The join dropped or repeated an order | Booked, and "collected held: the join lost or repeated orders" | You |
| Booked against orders alone | A fan-out or a dropped order | Booked from orders alone; collected held | You |
| The gap against booked less collected | A NULL fell out of a sum | The page, with the gap recomputed from the two columns | You |
| The gap against the never-paid and paid-short lists | A list or a bar is wrong | Booked and collected, the gap marked provisional | You, with Kavya |
| Collected plus posted twice against posted | The feed changed, or a retry arrived in a new shape | Booked; collected held; the platform lead told the same day | The platform lead |
"""),
        code("""
owners = {"orders on the report equal orders in the table": "you", "booked equals booked from orders alone": "you",
          "the gap equals booked less collected": "you", "the gap equals the never-paid and paid-short lists": "you, with Kavya",
          "collected plus posted twice equals posted from payments alone": "the platform lead"}
kit.check("every tie-back check has a named owner for the day it fails", set(owners) == {n_ for n_, _ in TIE_BACK},
          f"{len(owners)} checks, {len(set(owners.values()))} owners")"""),
        md("""
### In the interview: what runs before a joined number reaches Finance, and which one check would you keep?

The tags mark how often a question comes up: [S] a staple asked everywhere, [F] frequent in GCC and product screens, [D] a differentiator.

**[D] Design the validation you run before a joined number reaches Finance, and say what you do when it fails at the end of reporting day.** The validation has four layers, each run every time. The counts come first: rows in against rows out, and orders on
the report against orders in the table, with the join key unique on its one side and the keys that
match nothing counted on the other. The tie-backs follow: booked recomputed from `orders` alone,
posted from `payments` alone, and each bar of the bridge equal to the total of its named list. The
third layer is one independent recomputation, in another tool from the raw rows, or against the
gateway's settlement file when there is one, after checking that the feed is complete up to the
quarter's cut-off. The last tests the suite itself: run it against the known wrong reports, the
fan-out, the dropped order, the NULL gap, and show that each fails. When a
check fails late on reporting day, send what is reconciled, booked, which ties to orders alone, with the open line
stated, which check failed, what it means and when it will close; hold the collected figure; and
tell the owner the same day. An unreconciled number never leaves with a PASS on it.

**[S] If you could keep only one check before a joined number leaves, which would you keep?** Keep orders on the report against orders in the source table. A join goes wrong in two ways, a
fan-out and a dropped order, and this check catches both without reading a rupee, in a millisecond.
It misses what goes wrong after the join: on the day's five wrong pages it stops three, and lets
through posted read as collected and the gap summed past a NULL, which is why the gap's tie-back to
the never-paid and paid-short lists is the second check added.

### Depth: why is a settlement file stronger than any check on Kalpa's own tables?

Every check in this suite reads Kalpa's own records, so a record that is wrong at the source, a
payment the feed invented or lost, passes all of them. A settlement file comes from the gateway and
the bank, outside Kalpa, and a difference between it and the payments table is evidence nobody at
Kalpa wrote. By the FT's account above, Wirecard's auditor relied on documents from Wirecard and its
trustee instead of checking directly with OCBC Bank.
"""),
        md("""
## What did this chapter answer, one line per question?

1. Three plausibility checks pass the quarter-in-WHERE page that hides T-4, 3 of 3, because each
   tests the page against itself.
2. Five tie-back checks compare the page's orders, booked, gap and collected with figures computed
   outside it; on that page three of them fail.
3. The plausibility suite lets through two of the day's five wrong pages, the two that hide T-4; the
   tie-back suite stops all five and passes the true page.
4. On Kalpa's Q2 report every tie-back check passes: 462 orders against 462, Rs 9,84,00,000 against
   Rs 9,84,00,000, the gap tied to the never-paid and paid-short lists, the retries to posted.
5. Python, counting the raw rows with no join, reaches the same orders, booked, collected and gap, on
   the invented tables and on Kalpa's Q2.
6. When a check fails at the end of reporting day, Anand gets booked with the open line named, the
   collected figure is held, and the check's owner hears the same day.

**The day's answer, for Anand.** Q2 booked Rs 9,84,00,000; collected, each payment counted once, is
the figure on your own page; the gap is the orders nobody paid, named by channel; the retries and
the payments with no order go to the platform lead; and every figure ties back to the orders and
payments tables through checks that have each been seen to fail.
"""),
        code("kit.check_summary()"),
    ]
    build(nb_path(n), cells)
    write_sql(n, ["The day's wrong reports rebuilt on the invented tables, the single-table sources the tie-back",
                  "checks compare with, and Kalpa's Q2 report with its sources."],
              [("Setup: the two invented tables", TINY),
               ("Setup: chapter 3's per-order table as TEMP views, invented and Kalpa's Q2", VIEWS)]
              + [(f"A report to test, invented: {name}", q) for name, q in Q6.items()]
              + [("The single-table sources, invented", Q6_SOURCES_TINY),
                 ("Kalpa's Q2 report, totals", Q6_TRUE_KALPA),
                 ("Kalpa's Q2 single-table sources", Q6_SOURCES_KALPA)])
    print("chapter 6 written")


CHAPTERS = {1: chapter1, 2: chapter2, 3: chapter3, 4: chapter4, 5: chapter5, 6: chapter6}

if __name__ == "__main__":
    wanted = [int(a) for a in sys.argv[1:]] or sorted(CHAPTERS)
    for n in wanted:
        CHAPTERS[n]()

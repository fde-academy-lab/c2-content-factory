"""Prove every key on the Week 2 Saturday recap paper.

    python3 content/W02/SAT/internal/C2_W02_SAT_key_proofs_INTERNAL.py

Runs cold from the repository root. It creates a scratch schema on the local Postgres
(PGHOST, PGPORT, PGUSER, PGPASSWORD; localhost, 5432, postgres and postgres by default), loads the
week's warehouse into it from content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql, and drops
the schema at the end, whatever happens. Every code exhibit is read from the week's source file,
content/W02/SAT/internal/C2_W02_SAT_paper_source_INTERNAL.yaml, and run as printed: SQL on
Postgres, Python with its printed output captured. Every Kalpa number a stem or an exhibit prints
is recomputed from the warehouse or from the week's own files, and every arithmetic key is
asserted. The Excel items are reasoned in comments, with their arithmetic asserted in Python on
the week's own exports. It prints one line per item and exits 1 on the first failed assertion.
"""
import contextlib
import io
import os
import pathlib
import sys
from bisect import bisect_right
from decimal import Decimal

import pandas as pd
import psycopg2
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[4]
SOURCE = ROOT / "content/W02/SAT/internal/C2_W02_SAT_paper_source_INTERNAL.yaml"
WAREHOUSE = ROOT / "content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql"
EXPOSURE = ROOT / "content/W02/D4/data/C2_W02_D04_exposure_STUDENT.csv"
CLEAN_TABLE = ROOT / "content/W02/D5/data/C2_W02_D05_customer_table_STUDENT.csv"
RAW_EXPORT = ROOT / "content/W02/D5/data/C2_W02_D05_raw_export_STUDENT.csv"
SCHEMA = "w02_sat_proof"

SRC = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
ADD = {a["id"]: a for a in SRC["additions"]}
LINES = []


def show(q, name, key, detail, keyed=None):
    """One line per item: its printed number, its id, its key and what was checked. For an
    addition, the key must be the one the source file prints, and `keyed`, when given, must be the
    text of the keyed option, so a relabelled or reworded option cannot pass unnoticed."""
    if name in ADD:
        assert str(ADD[name]["key"]) == key, (name, ADD[name]["key"], key)
        if keyed is not None:
            assert options_of(name)[key] == keyed, (name, options_of(name)[key], keyed)
    line = f"PASS  Q{q:<3} {name:<18} key {key:<24} {detail}"
    LINES.append(line)
    print(line)


def code_of(item_id):
    return ADD[item_id]["exhibit"]["code"]["text"]


def options_of(item_id):
    """{letter: option text} as the item prints them."""
    out = {}
    for ln in ADD[item_id]["text"].split("\n"):
        ln = ln.strip()
        if ln[:1] == "(" and ln[2:3] == ")":
            out[ln[1]] = ln[4:]
    return out


def run_python(text):
    """Run a printed Python exhibit and return what it prints, stripped."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(text, "<exhibit>", "exec"), {})
    return buf.getvalue().strip()


def connect():
    return psycopg2.connect(host=os.environ.get("PGHOST", "localhost"),
                            port=int(os.environ.get("PGPORT", "5432")),
                            user=os.environ.get("PGUSER", "postgres"),
                            password=os.environ.get("PGPASSWORD", "postgres"),
                            dbname=os.environ.get("PGDATABASE", "postgres"))


def rows(cur, sql):
    cur.execute(sql)
    return cur.fetchall()


def one(cur, sql):
    return rows(cur, sql)[0]


def frame(cur, sql):
    cur.execute(sql)
    cols = [c.name for c in cur.description]
    return pd.DataFrame(cur.fetchall(), columns=cols)


def lakh(x):
    return round(float(x) / 100000, 1)


def load_warehouse(cur, text):
    """Run the warehouse file as psql would: plain SQL runs as it comes, and each
    COPY ... FROM stdin block is fed its data lines, up to the line holding a single backslash and
    full stop, through copy_expert."""
    def flush(sql):
        # psycopg2 refuses text that is only comments, as the file's closing notes are.
        if any(ln.strip() and not ln.strip().startswith("--") for ln in sql):
            cur.execute("\n".join(sql))

    sql, lines = [], iter(text.splitlines())
    for line in lines:
        if line.startswith("COPY ") and line.rstrip().endswith("FROM stdin;"):
            flush(sql)
            sql = []
            data = []
            for row in lines:
                if row == "\\.":
                    break
                data.append(row)
            cur.copy_expert(line.rstrip().rstrip(";"), io.StringIO("\n".join(data) + "\n"))
        else:
            sql.append(line)
    flush(sql)


def main():
    con = connect()
    con.autocommit = True
    cur = con.cursor()
    print(f"Postgres: {one(cur, 'SHOW server_version')[0]}; pandas {pd.__version__}; "
          f"Python {sys.version.split()[0]}")
    cur.execute(f"DROP SCHEMA IF EXISTS {SCHEMA} CASCADE")
    cur.execute(f"CREATE SCHEMA {SCHEMA}")
    try:
        cur.execute(f"SET search_path TO {SCHEMA}")
        load_warehouse(cur, WAREHOUSE.read_text(encoding="utf-8"))
        prove(cur)
    finally:
        cur.execute(f"DROP SCHEMA IF EXISTS {SCHEMA} CASCADE")
        con.close()
    print(f"RESULT: PASS ({len(LINES)} items proved)")


def prove(cur):
    assert one(cur, "SELECT count(*) FROM orders")[0] == 1000
    assert one(cur, "SELECT count(*) FROM payments")[0] == 1428

    # ------------------------------------------------------------------ Part 1, Monday
    # Q1 int-div: the tree's numbers and the query in the stem.
    rp = ("SELECT o.* FROM orders o JOIN customers c USING (customer_id) "
          "WHERE c.segment = 'Retail-Plus'")
    tree = rows(cur, f"""SELECT quarter, count(*), count(DISTINCT customer_id), sum(amount),
                                round(sum(amount) / count(*))
                         FROM ({rp}) r GROUP BY quarter ORDER BY quarter""")
    assert [tuple(t) for t in tree] == [("Q1", 215, 91, Decimal("585770.00"), Decimal("2725")),
                                        ("Q2", 140, 76, Decimal("413380.00"), Decimal("2953"))]
    printed = rows(cur, f"""SELECT quarter, count(*) / count(DISTINCT customer_id)
                            FROM ({rp}) rp_orders GROUP BY quarter ORDER BY quarter""")
    true = rows(cur, f"""SELECT quarter, round(count(*)::numeric / count(DISTINCT customer_id), 2)
                         FROM ({rp}) rp_orders GROUP BY quarter ORDER BY quarter""")
    assert [p[1] for p in printed] == [2, 1]
    assert [t[1] for t in true] == [Decimal("2.36"), Decimal("1.84")]
    assert round((1 - 140 / 76 / (215 / 91)) * 100) == 22
    assert ADD["int-div"]["key"] == "c" and options_of("int-div")["c"].startswith("2 and 1;")
    show(1, "int-div", "c", "prints 2 and 1; numeric gives 2.36 and 1.84, a fall of 22 percent",
         "2 and 1; the counts divide as integers, and the true 2.36 and 1.84 fell 22 percent")

    # Q2 bank 57: the logical order FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY is the
    # documented order of evaluation (PostgreSQL manual, SELECT); nothing to compute.
    show(2, "bank 57", "c, b, e, f, a, d", "FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY")

    # Q3 bank 2: the room's LIMIT trap, reproduced on a fresh load of the warehouse.
    sample = ("SELECT sum(amount) FROM (SELECT order_id, amount FROM orders WHERE quarter = 'Q2' "
              "AND channel = 'app' AND status = 'delivered' {order} LIMIT 5) s")
    first = one(cur, sample.format(order=""))[0]
    cur.execute("BEGIN")
    cur.execute("UPDATE orders SET status = status WHERE order_id IN ('KR-00542', 'KR-00544')")
    after = one(cur, sample.format(order=""))[0]
    cur.execute("ROLLBACK")
    fixed = one(cur, sample.format(order="ORDER BY order_id"))[0]
    assert (first, after, fixed) == (Decimal("3900.00"), Decimal("4590.00"), Decimal("3900.00"))
    words = SRC["banks"]["mon-words"]["options"]
    assert "abcde"[words.index("guarantee")] == "d" and "abcde"[words.index("CTE")] == "b"
    show(3, "bank 2", "d (guarantee)", "LIMIT 5 with no ORDER BY: Rs 3,900, then Rs 4,590 after a reload")

    # Q4 bank 3: a definition; CTE matches the tracker's key by the word before its bracket.
    show(4, "bank 3", "b (CTE)", "the word bank's option b is the tracker key's head word")

    # Q5 monday-fact: a judgement on the operating rule; its reason is Friday's rule.
    assert ADD["monday-fact"]["key"] == "a"
    show(5, "monday-fact", "a", "a what-if the room changes is Excel's job; the rest stay in the warehouse")

    # Q6 facebook: run the exhibit as printed.
    reported, per_view = one(cur, code_of("facebook"))
    assert (reported, per_view) == (Decimal("10.0"), Decimal("6.0"))
    over = (reported - per_view) / per_view
    assert round(over * 100, 1) == Decimal("66.7")                 # about 67 percent, option d
    assert round((reported - per_view) / reported * 100) == 40     # the wrong base, option a
    assert (14 + 9 + 4) / 3 == 9.0 and round((9.0 / 6.0 - 1) * 100) == 50   # option b
    assert 60 <= float(over) * 100 <= 80                            # inside TechCrunch's range
    show(6, "facebook", "d", "returns 10.0 and 6.0; 10 over 6 is 66.7 percent too high",
         "10.0 and 6.0; the reported figure is about 67 percent too high")

    # ------------------------------------------------------------------ Part 2, Tuesday
    # The set's situation: 462 orders, 216 + 188 + 28 + 30, and 8 orphan payments.
    split = dict(rows(cur, """
        WITH per AS (SELECT o.order_id, count(p.payment_id) AS n,
                            count(DISTINCT p.instalment_no) AS inst
                     FROM orders o LEFT JOIN payments p ON p.order_id = o.order_id
                     WHERE o.quarter = 'Q2' GROUP BY o.order_id)
        SELECT n::text || '/' || inst::text, count(*) FROM per GROUP BY 1"""))
    assert split == {"0/0": 30, "1/1": 216, "2/1": 28, "2/2": 188}
    assert one(cur, "SELECT sum(amount) FROM orders WHERE quarter = 'Q2'")[0] == Decimal("98400000.00")
    assert one(cur, "SELECT count(*) FROM payments p WHERE NOT EXISTS "
                    "(SELECT 1 FROM orders o WHERE o.order_id = p.order_id)")[0] == 8
    assert one(cur, """SELECT count(*) FROM orders o WHERE o.quarter = 'Q2' AND o.status = 'delivered'
                       AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)""")[0] == 30

    # Q7 join-counts: run the exhibit as printed.
    got = one(cur, code_of("join-counts"))
    assert got == (678, 462, 648)
    assert 216 + 2 * 188 + 2 * 28 + 30 == 678 and 678 - 30 == 648
    assert (678 + 8, 462 + 8, 648 + 8) == (686, 470, 656)          # option d counts the orphans
    show(7, "join-counts", "b", "678 rows out, 462 orders, 648 payment rows", "678, 462 and 648")

    # Q8 report-steps: run the steps in the keyed order and check what the key's reason says.
    posted, collected = one(cur, """
        WITH q2p AS (SELECT p.* FROM payments p JOIN orders o USING (order_id)
                     WHERE o.quarter = 'Q2')
        SELECT (SELECT sum(amount) FROM q2p),
               (SELECT sum(amount) FROM (SELECT DISTINCT ON (order_id, instalment_no) *
                                         FROM q2p ORDER BY order_id, instalment_no, payment_id) d)""")
    assert (posted, collected) == (Decimal("96665820.00"), Decimal("96645070.00"))
    assert posted - collected == Decimal("20750.00")
    rows_out, gap = one(cur, """
        WITH dedup AS (SELECT DISTINCT ON (order_id, instalment_no) order_id, amount
                       FROM payments ORDER BY order_id, instalment_no, payment_id),
        per_order AS (SELECT order_id, sum(amount) AS paid FROM dedup GROUP BY order_id)
        SELECT count(*), sum(o.amount) - sum(coalesce(p.paid, 0))
        FROM orders o LEFT JOIN per_order p ON p.order_id = o.order_id
        WHERE o.quarter = 'Q2'""")
    unpaid = one(cur, """SELECT sum(amount) FROM orders o WHERE quarter = 'Q2'
                         AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)""")[0]
    assert rows_out == 462 and gap == unpaid == Decimal("1754930.00")
    by_order = one(cur, """SELECT count(*) FROM (SELECT p.order_id FROM payments p
                           JOIN orders o USING (order_id) WHERE o.quarter = 'Q2'
                           GROUP BY p.order_id HAVING count(*) > 1) x""")[0]
    by_instalment = one(cur, """SELECT count(*) FROM (SELECT p.order_id, p.instalment_no FROM payments p
                                JOIN orders o USING (order_id) WHERE o.quarter = 'Q2'
                                GROUP BY 1, 2 HAVING count(*) > 1) y""")[0]
    assert (by_order, by_instalment) == (216, 28)
    # Summing before the repeats are dropped leaves the Rs 20,750 in collected (the wrong order).
    short_gap = one(cur, """
        WITH per_order AS (SELECT order_id, sum(amount) AS paid FROM payments GROUP BY order_id)
        SELECT sum(o.amount) - sum(coalesce(p.paid, 0))
        FROM orders o LEFT JOIN per_order p ON p.order_id = o.order_id WHERE o.quarter = 'Q2'""")[0]
    assert short_gap == Decimal("1734180.00") and unpaid - short_gap == Decimal("20750.00")
    show(8, "report-steps", "c, e, a, d, b", "462 rows out; gap Rs 17,54,930 equals the unpaid list")

    # Q9 where-on-payments: run the exhibit, then the ON version the reason names.
    assert one(cur, code_of("where-on-payments")) == (2, 2400)
    on_version = code_of("where-on-payments").replace(
        "LEFT JOIN payments p ON p.order_id = o.order_id\nWHERE p.paid_date",
        "LEFT JOIN payments p ON p.order_id = o.order_id\nAND p.paid_date")
    assert one(cur, on_version) == (4, 3700)
    show(9, "where-on-payments", "b", "2 rows, booked 2,400; the filter in ON gives 4 and 3,700",
         "2 rows, booked Rs 2,400")

    # Q10 reporting-day: the exhibit's figures are illustrative; the failed check's size.
    assert 1754930 - 1733180 == 21750
    show(10, "reporting-day", "c", "the gap check fails by Rs 21,750; booked passed both of its checks")

    # Q11 phe-checks: quoted facts (GOV.UK, 4 October 2020; The Register, 5 October 2020).
    assert 2 ** 16 == 65536
    show(11, "phe-checks", "b, d", "only checks that compare arrived with loaded see a truncation")

    # ------------------------------------------------------------------ Part 3, Wednesday
    ranked = frame(cur, """
        WITH m AS (SELECT o.customer_id, sum(o.amount) AS q2 FROM orders o
                   JOIN customers c USING (customer_id)
                   WHERE c.segment = 'Retail-Plus' AND o.quarter = 'Q2' GROUP BY o.customer_id)
        SELECT customer_id, q2,
               row_number() OVER (ORDER BY q2 DESC, customer_id) AS rn,
               rank()       OVER (ORDER BY q2 DESC)              AS rk,
               dense_rank() OVER (ORDER BY q2 DESC)              AS dr
        FROM m ORDER BY rn""")
    assert len(ranked) == 76
    top45 = ranked[ranked.rn <= 45]
    assert top45.q2.nunique() == 45 and top45.q2.min() > 3600
    shown = [(int(a), b, int(c.replace(",", ""))) for a, b, c in SRC["exhibits"]["5"]["table"]["rows"]]
    window = ranked[(ranked.rn >= 46) & (ranked.rn <= 53)]
    assert shown == [(int(r.rn), r.customer_id, int(r.q2)) for r in window.itertuples()]

    # Q12 rows-shipped.
    counts = ((ranked.rk <= 50).sum(), (ranked.dr <= 50).sum(), (ranked.rn <= 50).sum())
    assert counts == (51, 52, 50)
    show(12, "rows-shipped", "a", "RANK keeps 51, DENSE_RANK 52, ROW_NUMBER 50", "51, 52 and 50")

    # Q13 tie-rule: the pair at fiftieth, the member DENSE_RANK adds, and ROW_NUMBER's drop.
    tied = ranked[ranked.q2 == 3350].customer_id.tolist()
    assert tied == ["C-0185", "C-0242"] and set(ranked[ranked.rk == 50].customer_id) == set(tied)
    assert ranked[ranked.dr == 50].customer_id.tolist() == ["C-0259"]
    assert ranked[ranked.rn == 51].customer_id.item() == "C-0242"
    show(13, "tie-rule", "d", "RANK: 51, C-0185 and C-0242 tie at fiftieth on Rs 3,350")

    # Q14 bank 27: the whole-table top fifty the reworded stem quotes.
    whole = dict(rows(cur, """
        WITH m AS (SELECT o.customer_id, c.segment, sum(o.amount) AS q2 FROM orders o
                   JOIN customers c USING (customer_id) WHERE o.quarter = 'Q2'
                   GROUP BY o.customer_id, c.segment),
        top AS (SELECT * FROM m ORDER BY q2 DESC, customer_id LIMIT 50)
        SELECT segment, count(*) FROM top GROUP BY segment"""))
    assert whole == {"Business": 35, "Retail-Plus": 11, "Retail-Core": 4}
    show(14, "bank 27", "b", "the whole-table fifty is 35, 11, 4 and no Student")

    # Q15 lag-gap: the exhibit's months are the warehouse's, and the flag as the stem states it.
    months = frame(cur, """
        SELECT customer_id, to_char(date_trunc('month', order_date), 'Mon') AS mon,
               date_trunc('month', order_date)::date AS month, sum(amount) AS spend
        FROM orders WHERE customer_id IN ('C-0161', 'C-0171', 'C-0185', 'C-0216')
        GROUP BY 1, 2, 3 ORDER BY 1, 3""")
    table = SRC["additions"][[a["id"] for a in SRC["additions"]].index("lag-gap")]["exhibit"]["table"]
    heads = table["head"][1:]
    for member, *cells in table["rows"]:
        mine = months[months.customer_id == member]
        want = {m: int(c.replace(",", "")) for m, c in zip(heads, cells) if c}
        assert dict(zip(mine.mon, mine.spend.astype(int))) == want, member
    flag = frame(cur, """
        WITH mm AS (SELECT customer_id, date_trunc('month', order_date)::date AS month,
                           sum(amount) AS spend FROM orders GROUP BY 1, 2),
        m AS (SELECT customer_id, month, spend,
                     lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS prev1,
                     lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS prev2,
                     lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS m1,
                     lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS m2
              FROM mm)
        SELECT customer_id, (m1 = DATE '2026-08-01' AND m2 = DATE '2026-07-01') AS calendar_ok
        FROM m WHERE month = DATE '2026-09-01' AND spend < prev1 AND prev1 < prev2
          AND customer_id IN ('C-0161', 'C-0171', 'C-0185', 'C-0216') ORDER BY 1""")
    assert flag.customer_id.tolist() == ["C-0161", "C-0171", "C-0185", "C-0216"]
    assert flag[flag.calendar_ok].customer_id.tolist() == ["C-0161", "C-0171"]
    show(15, "lag-gap", "c", "all four flagged; the calendar check keeps C-0161 and C-0171")

    # Q16 run-rate: the chart's bars are the week's own weekly booked revenue, in Rs lakh.
    weeks = frame(cur, """
        SELECT p.week_start, p.plan_revenue,
               (SELECT sum(amount) FROM orders o WHERE o.quarter = 'Q2'
                AND o.order_date BETWEEN p.week_start AND p.week_start + 6) AS booked,
               (SELECT sum(amount) FROM orders o WHERE o.quarter = 'Q2'
                AND o.order_date <= p.week_start + 6) AS to_date,
               sum(p.plan_revenue) OVER (ORDER BY p.week_start) AS plan_to_date
        FROM plan_line p ORDER BY p.week_start""")
    chart = SRC["additions"][[a["id"] for a in SRC["additions"]].index("run-rate")]["exhibit"]["mermaid"]
    bars = [float(x) for x in chart.split("bar [")[1].split("]")[0].split(",")]
    last7 = weeks[(weeks.week_start >= pd.Timestamp("2026-08-10").date())
                  & (weeks.week_start <= pd.Timestamp("2026-09-21").date())]
    assert [lakh(b) for b in last7.booked] == bars
    plan = float(weeks.plan_revenue.iloc[0])
    assert lakh(plan) == 75.7 and sum(float(b) < plan for b in last7.booked) == 6
    assert one(cur, "SELECT sum(plan_revenue) FROM plan_line")[0] == Decimal("98399990.00")
    mid = weeks[weeks.week_start == pd.Timestamp("2026-08-17").date()].iloc[0]
    assert mid.to_date - mid.plan_to_date == Decimal("15751980.00")      # Rs 1.58 crore
    july = weeks[weeks.week_start == pd.Timestamp("2026-07-13").date()].iloc[0]
    assert july.booked == Decimal("26628920.00")
    show(16, "run-rate", "a", "six of seven weeks below Rs 75.69 lakh; Q2 closes Rs 10 over plan")

    # ------------------------------------------------------------------ Part 4, Thursday
    customers = frame(cur, "SELECT * FROM customers")
    orders = frame(cur, "SELECT * FROM orders")
    orders["amount"] = orders["amount"].astype(float)
    spend = orders.groupby("customer_id").agg(spend=("amount", "sum")).reset_index()
    table = customers.merge(spend, on="customer_id", how="left", validate="one_to_one")
    table["spend"] = table["spend"].fillna(0)
    feed = pd.read_csv(EXPOSURE)
    assert len(table) == 340 and table.spend.sum() == 198400000.0
    assert len(feed) == 136 and feed.customer_id.nunique() == 130
    repeats = feed[feed.customer_id.duplicated(keep=False)]
    assert repeats.customer_id.nunique() == 6 and set(repeats.exposed_date) == {"2026-08-03", "2026-08-11"}
    merged = table.merge(feed, on="customer_id", how="left")

    # Q17 merge-rows.
    assert len(merged) == 346 == 334 + 12
    show(17, "merge-rows", "346", "340 customers, 6 of them twice, 346 rows")

    # Q18 pivot-total: the pivot sums spend over the merged rows.
    assert merged.spend.sum() == 198445800.0 and merged.spend.sum() - 198400000.0 == 45800.0
    assert (340 - 130) == 210
    show(18, "pivot-total", "d", "the pivot reads Rs 19,84,45,800, Rs 45,800 over the book")

    # Q19 stop-line: which guards stop the run.
    try:
        table.merge(feed, on="customer_id", how="left", validate="one_to_one")
        raise AssertionError("validate did not raise")
    except pd.errors.MergeError as e:
        assert "not unique in right dataset" in str(e)
    assert len(merged) != len(table)                                   # option e fires
    assert len(merged.drop_duplicates()) == 346                        # option b stops nothing
    ind = table.merge(feed, on="customer_id", how="left", indicator=True)
    assert len(ind) == 346 and (ind["_merge"] == "both").sum() == 136  # option c flags nothing
    inner = table.merge(feed, on="customer_id", how="inner")
    assert len(inner) == 136 and inner.customer_id.nunique() == 130    # option d
    show(19, "stop-line", "a, e", "validate raises MergeError and the row assert fails; b, c, d pass")

    # Q20 first-touch: one exposure per customer, the first by date, validate kept on.
    first = feed.sort_values(["customer_id", "exposed_date"]).drop_duplicates("customer_id", keep="first")
    fixed = table.merge(first, on="customer_id", how="left", validate="one_to_one")
    assert len(fixed) == 340 and fixed.spend.sum() == 198400000.0 and fixed.campaign_id.notna().sum() == 130
    show(20, "first-touch", "c", "340 rows, spend on the book, 130 reached")

    # Q21 months-view: run the exhibit as printed.
    assert run_python(code_of("months-view")) == "2000.0 4 6200.0"
    show(21, "months-view", "b", "prints 2000.0 4 6200.0", "2000.0 4 6200.0")

    # Q22 genes: run the exhibit as printed.
    assert run_python(code_of("genes")) == "4 2"
    show(22, "genes", "a", "prints 4 2",
         "4 2; two genes lose their annotation with no error, so go back to the lab")

    # ------------------------------------------------------------------ Part 5, Friday
    fixes = SRC["banks"]["fri-fix"]["options"]
    letter = {o: "abcdef"[k] for k, o in enumerate(fixes)}
    assert letter["XLOOKUP with a message for a missing id"] == ADD["fix-lookup"]["key"] == "d"
    assert letter["SUBTOTAL(109, ...) at the foot of the list"] == ADD["fix-foot"]["key"] == "a"
    assert letter["a first-row flag per order, summed with SUMIFS"] == ADD["fix-tree"]["key"] == "f"
    assert letter["a labelled input cell beside the actual figure"] == ADD["fix-whatif"]["key"] == "c"
    clean = pd.read_csv(CLEAN_TABLE)
    raw = pd.read_csv(RAW_EXPORT)

    # Q23 fix-lookup. Excel reasoning: VLOOKUP with its fourth argument left out looks for an
    # approximate match, which on a table sorted by id returns the largest id not above the one
    # asked for; XLOOKUP matches exactly by default and shows its fourth argument, if_not_found,
    # for a missing id (Microsoft Support, VLOOKUP and XLOOKUP, verified 29 September 2026).
    # Emulated here on Friday's clean table.
    ids = sorted(clean.customer_id)
    assert "C-0195" not in ids
    neighbour = ids[bisect_right(ids, "C-0195") - 1]
    assert neighbour == "C-0194"
    assert int(clean.set_index("customer_id").loc[neighbour, "revenue"]) == 16740
    show(23, "fix-lookup", "d", "an approximate match returns C-0194's Rs 16,740 for C-0195")

    # Q24 fix-foot. Excel reasoning: SUM adds every row in its range, hidden or not; SUBTOTAL(109)
    # adds only the rows on screen. The protect list is Friday's fifty Retail-Plus members.
    plus = clean[clean.segment == "Retail-Plus"].sort_values(["revenue", "customer_id"],
                                                             ascending=[False, True]).head(50)
    mumbai = plus[plus.city == "Mumbai"]
    assert int(plus.revenue.sum()) == 714890 and len(mumbai) == 11 and int(mumbai.revenue.sum()) == 156790
    assert round(714890 / 156790, 1) == 4.6
    show(24, "fix-foot", "a", "SUBTOTAL(109) reads Rs 1,56,790 for Mumbai's 11; SUM Rs 7,14,890")

    # Q25 fix-tree. Excel reasoning: =IF(COUNTIF($A$2:A2,A2)=1,1,0) is 1 on the first row of each
    # order_id, and SUMIFS over the rows flagged 1 counts each order once. Remove Duplicates
    # removes only rows identical in every column.
    assert len(raw) == 1450 and raw.order_id.nunique() == 1000
    assert raw.order_amount.sum() == 394095490
    dedup = raw.drop_duplicates()
    assert len(dedup) == 1400 and dedup.order_amount.sum() == 394057740
    flagged = raw[~raw.order_id.duplicated(keep="first")]
    assert flagged.order_amount.sum() == 198400000
    show(25, "fix-tree", "f", "the first-row flag ties to Rs 19,84,00,000; Remove Duplicates leaves 1,400 rows")

    # Q26 fix-whatif: Rs 5,00,000 typed over Retail-Plus Q2 against Q1's Rs 5,85,770.
    assert round((500000 - 585770) / 585770 * 100, 1) == -14.6
    assert round((413380 - 585770) / 585770 * 100, 1) == -29.4
    show(26, "fix-whatif", "c", "the typed value reads down 14.6 percent against Finance's 29.4")

    # Q27 range-check: a range that ends at row 301 covers 300 customers of 311.
    assert 301 - 1 == 300 and 311 - 300 == 11
    show(27, "range-check", "d", "a control total and a row count both fail the day 11 rows fall outside")

    # Q28 var-formula: the sheet's formula and the one the modeller meant.
    old, new = 2.00, 2.60
    sheet = (new - old) / (old + new)
    meant = (new - old) / ((old + new) / 2)
    assert round(sheet, 3) == 0.130 and round(meant, 3) == 0.261
    assert abs(sheet / meant - 0.5) < 1e-12 and round((new - old) / old, 3) == 0.300
    show(28, "var-formula", "a", "0.130 against the intended 0.261, a factor of two",
         "0.130, half the intended 0.261; recompute one row a second way")

    # Q29 gross-fare: 25 percent of the gross fare against 25 percent of the net fare.
    extra = round(0.25 * 30.00 - 0.25 * (30.00 - 2.40), 2)
    assert extra == 0.60 == round(0.25 * 2.40, 2)
    show(29, "gross-fare", "0.60 dollars a trip", "7.50 on the gross fare against 6.90 on the net")

    # ------------------------------------------------------------------ Part 6, the AI team
    # Q30 eval-fanout: run the exhibit as printed.
    assert run_python(code_of("eval-fanout")) == "7 0.43"
    assert 3 / 5 == 0.6
    show(30, "eval-fanout", "c", "prints 7 0.43 against a true 0.6",
         "7 0.43; the model's two misses now count twice, against a true 0.6")

    # Q31 latest-run: the table's rows, and each approach in the options.
    runs = ("WITH eval_runs (model, run_id, finished_on, accuracy) AS (VALUES "
            "('bot-a', 'r1', DATE '2026-09-01', 0.81), ('bot-a', 'r2', DATE '2026-09-08', 0.78), "
            "('bot-b', 'r3', DATE '2026-09-02', 0.84), ('bot-b', 'r4', DATE '2026-09-09', 0.86), "
            "('bot-b', 'r5', DATE '2026-09-09', 0.79)) ")
    table31 = SRC["additions"][[a["id"] for a in SRC["additions"]].index("latest-run")]["exhibit"]["table"]
    assert [r[1] for r in table31["rows"]] == ["r1", "r2", "r3", "r4", "r5"]
    grouped = rows(cur, runs + "SELECT model, max(finished_on)::text, max(accuracy) FROM eval_runs "
                               "GROUP BY model ORDER BY model")
    assert grouped[0] == ("bot-a", "2026-09-08", Decimal("0.81"))      # a pairing no run produced
    keyed = rows(cur, runs + """SELECT model, run_id, accuracy FROM (
        SELECT *, row_number() OVER (PARTITION BY model ORDER BY finished_on DESC, run_id DESC) AS rn
        FROM eval_runs) x WHERE rn = 1 ORDER BY model""")
    assert keyed == [("bot-a", "r2", Decimal("0.78")), ("bot-b", "r5", Decimal("0.79"))]
    ranked31 = rows(cur, runs + """SELECT model, run_id FROM (
        SELECT *, rank() OVER (PARTITION BY model ORDER BY finished_on DESC) AS rk
        FROM eval_runs) x WHERE rk = 1 ORDER BY model, run_id""")
    assert ranked31 == [("bot-a", "r2"), ("bot-b", "r4"), ("bot-b", "r5")]
    loose = rows(cur, runs + """SELECT model, run_id FROM (
        SELECT *, row_number() OVER (PARTITION BY model ORDER BY finished_on DESC) AS rn
        FROM eval_runs) x WHERE rn = 1 ORDER BY model""")
    assert len(loose) == 2 and loose[1][1] in ("r4", "r5")               # the tie is the database's pick
    show(31, "latest-run", "d", "row 1 by date then run_id: r2 and r5; RANK keeps r4 and r5")

    # Q32 low-ratings: run the exhibit as printed, and the two misreadings.
    assert rows(cur, code_of("low-ratings")) == [("bot-a", 2)]
    body = code_of("low-ratings").split("SELECT model")[0]
    having_first = rows(cur, body + """SELECT model, count(*) FILTER (WHERE rating <= 2) FROM replies
        GROUP BY model HAVING count(*) >= 2 AND count(*) FILTER (WHERE rating <= 2) > 0 ORDER BY model""")
    assert having_first == [("bot-a", 2), ("bot-b", 1)]                  # option a
    no_where = rows(cur, body + "SELECT model, count(*) FROM replies GROUP BY model ORDER BY model")
    assert no_where == [("bot-a", 3), ("bot-b", 2), ("bot-c", 2)]        # option d
    show(32, "low-ratings", "b", "returns bot-a 2 alone", "bot-a 2 alone")

    # Q33 not-in: run the exhibit as printed, and the anti-join that works.
    assert one(cur, code_of("not-in")) == (0,)
    works = code_of("not-in").replace(
        "WHERE conversation_id NOT IN (SELECT conversation_id FROM handoffs)",
        "WHERE NOT EXISTS (SELECT 1 FROM handoffs h WHERE h.conversation_id = conversations.conversation_id)")
    assert one(cur, works) == (2,)
    show(33, "not-in", "c", "NOT IN returns 0; NOT EXISTS returns 2",
         "0; the review concludes the assistant resolved nothing without a person")

    # Q34 token-peers: run the exhibit as printed, and the two variants the reasons name.
    assert [r[1] for r in rows(cur, code_of("token-peers"))] == [400, 1200, 1200, 1400]
    tiebreak = code_of("token-peers").replace("OVER (ORDER BY day)", "OVER (ORDER BY day, call_id)")
    assert [r[1] for r in rows(cur, tiebreak)] == [400, 700, 1200, 1400]
    whole = code_of("token-peers").replace("OVER (ORDER BY day)", "OVER ()")
    assert [r[1] for r in rows(cur, whole)] == [1400, 1400, 1400, 1400]
    show(34, "token-peers", "a", "400, 1200, 1200, 1400; peers share the day's figure",
         "400, 1200, 1200 and 1400")

    # Q35 weekly-users: the chart's bars, and Kalpa's own distinct counts the reason cites.
    chart35 = SRC["additions"][[a["id"] for a in SRC["additions"]].index("weekly-users")]["exhibit"]["mermaid"]
    daily = [int(x) for x in chart35.split("bar [")[1].split("]")[0].split(",")]
    assert sum(daily) == 5200 and round(sum(daily) / 7) == 743 and max(daily) == 810
    buyers = one(cur, """SELECT count(DISTINCT customer_id) FILTER (WHERE quarter = 'Q1'),
                                count(DISTINCT customer_id) FILTER (WHERE quarter = 'Q2'),
                                count(DISTINCT customer_id) FROM orders""")
    assert buyers == (244, 227, 301) and 244 + 227 == 471
    show(35, "weekly-users", "d", "the days add to 5,200; the week's distinct users are 2,100",
         "2,100, since someone active on several days counts once")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W02/SAT/internal/C2_W02_SAT_key_proofs_INTERNAL.py, with Postgres 16 on
# localhost and the default credentials
#     Prints the versions, then 35 lines, PASS Q1 to PASS Q35, each with the item's id, its key
#     and what was checked, then "RESULT: PASS (35 items proved)", and leaves no schema behind.
# The same run with the source file's facebook exhibit changed to count(*) in the reported line
#     The assertion on 10.0 and 6.0 fails with a traceback at Q6 and the exit code is 1; the
#     scratch schema is still dropped by the finally block.
# The same run with join-counts' key changed to a in the source file
#     The run still passes Q7's arithmetic; the key letter is checked by the distractor audit and
#     the build, so the audit is the gate for a relabelled key.
# Postgres not running
#     psycopg2.OperationalError at connect, exit code 1, and nothing is created.
# A fresh warehouse file whose Retail-Plus tie at fiftieth has gone
#     Q12's counts assertion fails, naming no value, and the paper's Set 2 must be rebuilt.

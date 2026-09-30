"""Prove every key on the Week 2 Saturday recap paper.

    python3 content/W02/SAT/internal/C2_W02_SAT_key_proofs_INTERNAL.py

Runs cold from the repository root. It creates a scratch schema on the local Postgres
(PGHOST, PGPORT, PGUSER, PGPASSWORD; localhost, 5432, postgres and postgres by default), loads the
week's warehouse into it from content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql, and drops
the schema at the end, whatever happens. Every code exhibit is read from the week's source file,
content/W02/SAT/internal/C2_W02_SAT_paper_source_INTERNAL.yaml, and run as printed: SQL on
Postgres, Python with its printed output captured. Every Kalpa number a stem or an exhibit prints
is recomputed from the warehouse or from the week's own files, every table exhibit is read back
from the source file and worked, and every arithmetic key is asserted. The Excel items are reasoned
in comments, with their arithmetic asserted in Python on the week's own exports. It prints one line
per item and exits 1 on the first failed assertion.
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
EDITS = ROOT / "data/programme/paper_edits.yaml"
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
        assert " ".join(str(ADD[name]["key"]).split()) == key, (name, ADD[name]["key"], key)
        if keyed is not None:
            assert options_of(name)[key] == keyed, (name, options_of(name)[key], keyed)
    line = f"PASS  Q{q:<3} {name:<18} key {key[:24]:<24} {detail}"
    LINES.append(line)
    print(line)


def code_of(item_id):
    return ADD[item_id]["exhibit"]["code"]["text"]


def table_of(item_id):
    return ADD[item_id]["exhibit"]["table"]


def options_of(item_id):
    """{letter: option text} as the item prints them."""
    out = {}
    for ln in ADD[item_id]["text"].split("\n"):
        ln = ln.strip()
        if ln[:1] == "(" and ln[2:3] == ")":
            out[ln[1]] = ln[4:]
    return out


def num(cell):
    """A printed figure as a number: Indian digit groups and a leading minus both read."""
    return float(str(cell).replace(",", ""))


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


def crore(x):
    return round(float(x) / 10000000, 2)


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
    edits = yaml.safe_load(EDITS.read_text(encoding="utf-8"))["W2"]

    # The quarters the Part 1 intro names: 'Q1' is April to June and 'Q2' July to September.
    span = dict((q, (str(a), str(b))) for q, a, b in rows(
        cur, "SELECT quarter, min(order_date), max(order_date) FROM orders GROUP BY 1"))
    assert span == {"Q1": ("2026-04-01", "2026-06-28"), "Q2": ("2026-07-01", "2026-09-28")}

    # ------------------------------------------------------------------ Part 1, Monday
    # Q1 int-div: the tree's numbers, the query in the stem, the true figures and the fall.
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
    fall = (1 - (140 / 76) / (215 / 91)) * 100
    assert 21 <= fall <= 22.5 and round(fall) == 22
    show(1, "int-div", "It prints 2 and 1. The true figures are 2.36 and 1.84, a fall of about 22 "
         "percent.", "prints 2 and 1; numeric gives 2.36 and 1.84, a fall of 22 percent")

    # Q2 bank 57: the logical order FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY is the
    # documented order of evaluation (PostgreSQL manual, SELECT); nothing to compute.
    show(2, "bank 57", "c, b, e, f, a, d", "FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY")

    # Q3 bank 2: the room's LIMIT trap, reproduced on a fresh load of the warehouse, and the stem
    # edit whose blank takes a noun, so every word in the bank fits it.
    sample = ("SELECT sum(amount) FROM (SELECT order_id, amount FROM orders WHERE quarter = 'Q2' "
              "AND channel = 'app' AND status = 'delivered' {order} LIMIT 5) s")
    first = one(cur, sample.format(order=""))[0]
    cur.execute("BEGIN")
    cur.execute("UPDATE orders SET status = status WHERE order_id IN ('KR-00542', 'KR-00544')")
    after = one(cur, sample.format(order=""))[0]
    cur.execute("ROLLBACK")
    fixed = one(cur, sample.format(order="ORDER BY order_id"))[0]
    assert (first, after, fixed) == (Decimal("3900.00"), Decimal("4590.00"), Decimal("3900.00"))
    assert "makes no ____ about which five rows" in edits[2]["stem"]["text"]
    words = SRC["banks"]["mon-words"]["options"]
    assert "abcde"[words.index("guarantee")] == "d" and "abcde"[words.index("CTE")] == "b"
    show(3, "bank 2", "d (guarantee)", "LIMIT 5 with no ORDER BY: Rs 3,900, then Rs 4,590 after a reload")

    # Q4 bank 3: a definition; CTE matches the tracker's key by the word before its bracket.
    show(4, "bank 3", "b (CTE)", "the word bank's option b is the tracker key's head word")

    # Q5 first-look: a judgement on Monday's rule, which governs the reported number and leaves
    # exploration in a notebook (Monday's study notes, "Anand's ask, and what it rules out").
    show(5, "first-look", "b", "a first look reports nothing, so it belongs in a notebook on the warehouse",
         "In a notebook that reads the warehouse, since a first look reports no number to anyone")

    # Q6 facebook: run the exhibit as printed.
    calculated, defined = one(cur, code_of("facebook"))
    assert (calculated, defined) == (Decimal("10.0"), Decimal("6.0"))
    over = (calculated - defined) / defined
    assert round(over * 100, 1) == Decimal("66.7")                    # about 67 percent, option d
    assert round((calculated - defined) / calculated * 100) == 40     # the wrong base, option a
    assert (14 + 9 + 4) / 3 == 9.0 and round((9.0 / 6.0 - 1) * 100) == 50   # option b
    assert 60 <= float(over) * 100 <= 80                               # inside TechCrunch's range
    show(6, "facebook", "d", "returns 10.0 and 6.0; 10 over 6 is 66.7 percent too high",
         "It returns 10.0 and 6.0, so the calculated average is about 67 percent too high")

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

    # Q8 report-steps: e, f, b, c, a, with d left out. Each claim of the key's reason is run.
    dedup = """(SELECT DISTINCT ON (order_id, instalment_no) order_id, instalment_no, amount
                FROM payments ORDER BY order_id, instalment_no, payment_id)"""
    posted, collected = one(cur, f"""
        SELECT (SELECT sum(p.amount) FROM payments p JOIN orders o USING (order_id)
                WHERE o.quarter = 'Q2'),
               (SELECT sum(d.amount) FROM {dedup} d JOIN orders o USING (order_id)
                WHERE o.quarter = 'Q2')""")
    assert (posted, collected) == (Decimal("96665820.00"), Decimal("96645070.00"))
    assert posted - collected == Decimal("20750.00")                # e before f: the repeats' surplus
    joined_first = one(cur, f"""SELECT count(*) FROM orders o LEFT JOIN {dedup} d USING (order_id)
                                WHERE o.quarter = 'Q2'""")[0]
    assert joined_first == 650 == 462 + 188                         # b before f fails check c
    rows_out, gap = one(cur, f"""
        WITH per_order AS (SELECT order_id, sum(amount) AS paid FROM {dedup} d GROUP BY order_id)
        SELECT count(*), sum(o.amount) - sum(coalesce(p.paid, 0))
        FROM orders o LEFT JOIN per_order p ON p.order_id = o.order_id
        WHERE o.quarter = 'Q2'""")
    unpaid = one(cur, """SELECT sum(amount) FROM orders o WHERE quarter = 'Q2'
                         AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)""")[0]
    assert rows_out == 462 and gap == unpaid == Decimal("1754930.00")   # e, f, b then check c
    by_order = one(cur, """SELECT count(*) FROM (SELECT p.order_id FROM payments p
                           JOIN orders o USING (order_id) WHERE o.quarter = 'Q2'
                           GROUP BY p.order_id HAVING count(*) > 1) x""")[0]
    by_instalment = one(cur, """SELECT count(*) FROM (SELECT p.order_id, p.instalment_no FROM payments p
                                JOIN orders o USING (order_id) WHERE o.quarter = 'Q2'
                                GROUP BY 1, 2 HAVING count(*) > 1) y""")[0]
    assert (by_order, by_instalment) == (216, 28)                  # step d drops 188 real invoices
    assert ADD["report-steps"]["key"] == "e, f, b, c, a" and "d" not in ADD["report-steps"]["key"]
    show(8, "report-steps", "e, f, b, c, a", "650 rows if joined before the sum; 462 and a gap of "
         "Rs 17,54,930 in the key's order")

    # Q9 where-on-payments: run the exhibit, then the ON version the reason names.
    assert one(cur, code_of("where-on-payments")) == (2, 2400)
    on_version = code_of("where-on-payments").replace(
        "LEFT JOIN payments p ON p.order_id = o.order_id\nWHERE p.paid_date",
        "LEFT JOIN payments p ON p.order_id = o.order_id\nAND p.paid_date")
    assert one(cur, on_version) == (4, 3700)
    show(9, "where-on-payments", "b", "2 rows, booked 2,400; the filter in ON gives 4 and 3,700",
         "2 rows, booked Rs 2,400")

    # Q10 reporting-day: app and store are Kalpa's own figures; web's collected is Kalpa's less an
    # illustrative Rs 21,750, so web's bridge alone fails, by that amount.
    report = {r[0]: r[1:] for r in rows(cur, f"""
        WITH per AS (SELECT order_id, sum(amount) AS paid FROM {dedup} d GROUP BY 1)
        SELECT o.channel, sum(o.amount), sum(coalesce(p.paid, 0)),
               coalesce(sum(o.amount) FILTER (WHERE p.order_id IS NULL), 0)
        FROM orders o LEFT JOIN per p USING (order_id) WHERE o.quarter = 'Q2' GROUP BY 1""")}
    shown = {r[0].lower(): tuple(num(c) for c in r[1:]) for r in table_of("reporting-day")["rows"]}
    for ch in ("app", "store"):
        assert shown[ch] == tuple(float(x) for x in report[ch]), ch
    assert shown["web"][0] == float(report["web"][0]) and shown["web"][2] == float(report["web"][2])
    assert float(report["web"][1]) - shown["web"][1] == 21750
    gaps = {ch: b - c - u for ch, (b, c, u) in shown.items()}
    assert gaps == {"app": 0, "store": 0, "web": 21750}
    assert sum(b for b, _, _ in shown.values()) == 98400000       # booked ties to Monday's figure
    assert max(shown, key=lambda ch: shown[ch][0] - shown[ch][1]) == "store"   # option b's pull
    show(10, "reporting-day", "c", "app and store close to the rupee; web's gap exceeds its list by Rs 21,750",
         "Booked for every channel, collected for app and store, and web's collected held back")

    # Q11 phe-checks: each check worked on Lab B's row of the exhibit; b and d fire.
    labs = {r[0]: [num(c) for c in r[1:]] for r in table_of("phe-checks")["rows"]}
    csv, sheet, loaded, before = labs["Lab B"]
    fires = {"a": loaded != sheet, "b": loaded != csv, "c": False,
             "d": sheet == 65536 - 1, "e": loaded < before}
    assert [k for k, v in fires.items() if v] == ["b", "d"] and csv - loaded == 5365
    assert all(r[0] == r[1] == r[2] for k, r in labs.items() if k != "Lab B")   # A and C lost nothing
    show(11, "phe-checks", "b, d", "only the CSV count and the limit check see Lab B's 5,365 lost records")

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
    shown5 = [(int(a), b, int(c.replace(",", ""))) for a, b, c in SRC["exhibits"]["5"]["table"]["rows"]]
    window = ranked[(ranked.rn >= 46) & (ranked.rn <= 53)]
    assert shown5 == [(int(r.rn), r.customer_id, int(r.q2)) for r in window.itertuples()]

    # Q12 rows-shipped.
    counts = ((ranked.rk <= 50).sum(), (ranked.dr <= 50).sum(), (ranked.rn <= 50).sum())
    assert counts == (51, 52, 50)
    show(12, "rows-shipped", "a", "RANK keeps 51, DENSE_RANK 52, ROW_NUMBER 50", "51, 52 and 50")

    # Q13 tie-rule: the head's rule is every member who spent as much as the fiftieth, and nobody
    # who spent less; only RANK's list is exactly that set.
    fiftieth = ranked[ranked.rn == 50].q2.item()
    rule = set(ranked[ranked.q2 >= fiftieth].customer_id)
    assert set(ranked[ranked.rk <= 50].customer_id) == rule                     # c
    assert set(ranked[ranked.dr <= 50].customer_id) - rule == {"C-0259"}        # a adds C-0259
    assert rule - set(ranked[ranked.rn <= 50].customer_id) == {"C-0242"}       # b drops C-0242
    assert ranked[ranked.q2 == fiftieth].customer_id.tolist() == ["C-0185", "C-0242"]   # d: a coin toss
    show(13, "tie-rule", "c", "RANK keeps exactly the members at or above the fiftieth's Rs 3,350",
         "RANK, keeping every member ranked 50 or better")

    # Q14 bank 27: the whole-table top fifty and the share the reworded stem quotes.
    whole = dict(rows(cur, """
        WITH m AS (SELECT o.customer_id, c.segment, sum(o.amount) AS q2 FROM orders o
                   JOIN customers c USING (customer_id) WHERE o.quarter = 'Q2'
                   GROUP BY o.customer_id, c.segment),
        top AS (SELECT * FROM m ORDER BY q2 DESC, customer_id LIMIT 50)
        SELECT segment, count(*) FROM top GROUP BY segment"""))
    assert whole == {"Business": 35, "Retail-Plus": 11, "Retail-Core": 4}
    share = one(cur, """SELECT round(100 * sum(o.amount) FILTER (WHERE c.segment = 'Business')
                                 / sum(o.amount)) FROM orders o JOIN customers c USING (customer_id)
                        WHERE o.quarter = 'Q2'""")[0]
    assert share == 99 and "99 percent" in edits[27]["stem"]["text"]
    assert edits[27]["options"]["b"].startswith("A rank within PARTITION BY segment")
    show(14, "bank 27", "b", "the whole-table fifty is 35, 11, 4 and no Student; Business is 99 percent")

    # Q15 lag-gap: the exhibit's months are the warehouse's; the flag as the stem states it; the
    # calls that say something untrue; and the counts the two misreadings give.
    months = frame(cur, """
        SELECT customer_id, to_char(date_trunc('month', order_date), 'Mon') AS mon,
               date_trunc('month', order_date)::date AS month, sum(amount) AS spend
        FROM orders WHERE customer_id IN ('C-0161', 'C-0171', 'C-0185', 'C-0216')
        GROUP BY 1, 2, 3 ORDER BY 1, 3""")
    table = table_of("lag-gap")
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
    calls = flag.customer_id.tolist()
    untrue = flag[~flag.calendar_ok].customer_id.tolist()
    assert calls == ["C-0161", "C-0171", "C-0185", "C-0216"] and untrue == ["C-0185", "C-0216"]
    assert (len(calls), len(untrue)) == (4, 2)
    assert len(flag[flag.calendar_ok]) == 2                         # option a: LAG read as the calendar
    assert len([c for c in calls if c != "C-0216"]) == 3            # option b: C-0216 wrongly dropped
    show(15, "lag-gap", "c", "4 flagged; C-0185 and C-0216 had no August, so 2 calls are untrue",
         "4 calls, and two of them untrue")

    # Q16 run-rate: the chart's bars and line and the table are the week's own running totals.
    weeks = frame(cur, """
        SELECT p.week_start, p.plan_revenue,
               (SELECT sum(amount) FROM orders o WHERE o.quarter = 'Q2'
                AND o.order_date BETWEEN p.week_start AND p.week_start + 6) AS booked,
               (SELECT sum(amount) FROM orders o WHERE o.quarter = 'Q2'
                AND o.order_date <= p.week_start + 6) AS to_date,
               sum(p.plan_revenue) OVER (ORDER BY p.week_start) AS plan_to_date
        FROM plan_line p ORDER BY p.week_start""")
    ex16 = ADD["run-rate"]["exhibit"]
    bars = [float(x) for x in ex16["mermaid"].split("bar [")[1].split("]")[0].split(",")]
    line = [float(x) for x in ex16["mermaid"].split("line [")[1].split("]")[0].split(",")]
    every_other = weeks.iloc[::2]
    assert len(every_other) == 7
    assert [crore(x) for x in every_other.to_date] == bars
    assert [crore(x) for x in every_other.plan_to_date] == line
    assert [float(x) for x in ex16["table"]["rows"][0][1:]] == bars
    assert [float(x) for x in ex16["table"]["rows"][1][1:]] == line
    labels16 = [w.strftime("%-d %b") for w in every_other.week_start]
    assert labels16 == ex16["table"]["head"][1:]
    lead = [round(b - p, 2) for b, p in zip(bars, line)]
    assert lead == [-0.25, 1.95, 2.17, 1.57, 0.73, 0.79, 0.0]
    assert max(lead) == lead[2] and lead[-1] == 0.0 and all(x > 0 for x in lead[1:-1])
    assert weeks.to_date.iloc[-1] == Decimal("98400000.00")
    assert one(cur, "SELECT sum(plan_revenue) FROM plan_line")[0] == Decimal("98399990.00")
    plan = float(weeks.plan_revenue.iloc[0])
    last7 = weeks[(weeks.week_start >= pd.Timestamp("2026-08-10").date())
                  & (weeks.week_start <= pd.Timestamp("2026-09-21").date())]
    assert lakh(plan) == 75.7 and sum(float(b) < plan for b in last7.booked) == 6
    july = weeks[weeks.week_start == pd.Timestamp("2026-07-13").date()].iloc[0]
    assert july.booked == Decimal("26628920.00")
    show(16, "run-rate", "a", "the lead peaks at Rs 2.17 crore in early August and is 0.00 at the close",
         "Level with plan at the close, having given back the lead it built in July")

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
    assert list(feed.columns) == ["customer_id", "campaign_id", "exposed_date"]
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

    # Q20 first-touch: the same feed sent newest first; each option applied to it.
    newest = feed.sort_values("exposed_date", ascending=False, kind="stable").reset_index(drop=True)
    shown20 = [tuple(r) for r in table_of("first-touch")["rows"]]
    picked = newest[newest.customer_id.isin(["C-0001", "C-0002", "C-0012"])]
    assert shown20 == [tuple(r) for r in picked.itertuples(index=False)]
    first_day = feed.groupby("customer_id").exposed_date.min()
    def first_exposures(f):
        return (f.set_index("customer_id").exposed_date == first_day.reindex(f.customer_id).values).all()
    a20 = newest.drop_duplicates()
    assert len(a20) == 136                                             # a keeps both sends
    b20 = newest.drop_duplicates("customer_id")
    assert len(b20) == 130 and not first_exposures(b20)                # b keeps 11 August
    c20 = table.merge(newest, on="customer_id", how="left").drop_duplicates("customer_id")
    assert len(c20) == 340 and set(c20[c20.customer_id.isin(repeats.customer_id)].exposed_date) == {"2026-08-11"}
    d20 = newest.sort_values("exposed_date", kind="stable").drop_duplicates("customer_id")
    assert len(d20) == 130 and first_exposures(d20)
    fixed = table.merge(d20, on="customer_id", how="left", validate="one_to_one")
    assert len(fixed) == 340 and fixed.spend.sum() == 198400000.0 and fixed.campaign_id.notna().sum() == 130
    show(20, "first-touch", "d", "sorted earliest first: 130 first exposures, 340 rows, spend on the book",
         "Sort by exposed_date from the earliest, then keep each customer's first row")

    # Q21 months-view: run the exhibit as printed.
    assert run_python(code_of("months-view")) == "2000.0 4 6200.0"
    show(21, "months-view", "b", "prints 2000.0 4 6200.0", "2000.0 4 6200.0")

    # Q22 genes: run the exhibit as printed.
    assert run_python(code_of("genes")) == "4 2"
    show(22, "genes", "a", "prints 4 2",
         "4 2: two genes lost their annotation, so the list goes back to the lab")

    # ------------------------------------------------------------------ Part 5, Friday
    fixes = SRC["banks"]["fri-fix"]["options"]
    letter = {o: "abcdef"[k] for k, o in enumerate(fixes)}
    assert letter["XLOOKUP with its if_not_found argument set"] == ADD["fix-lookup"]["key"] == "d"
    assert letter["SUBTOTAL with function number 109"] == ADD["fix-foot"]["key"] == "a"
    assert letter["a first-row flag per order, then SUMIFS"] == ADD["fix-tree"]["key"] == "f"
    assert letter["a labelled input cell feeding a scenario line"] == ADD["fix-whatif"]["key"] == "c"
    clean = pd.read_csv(CLEAN_TABLE)
    raw = pd.read_csv(RAW_EXPORT)

    # Q23 fix-lookup. Excel reasoning: VLOOKUP with its fourth argument left out looks for an
    # approximate match, which on a table sorted by id returns the largest id not above the one
    # asked for; XLOOKUP matches exactly by default and shows its fourth argument, if_not_found,
    # for a missing code (Microsoft Support, VLOOKUP and XLOOKUP, verified 29 September 2026).
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
    # removes only rows identical in every column. The Part 5 exhibit's two rows are the export's.
    assert len(raw) == 1450 and raw.order_id.nunique() == 1000
    assert (raw.groupby("order_id").order_amount.nunique() == 1).all()   # booked value on every row
    part5 = SRC["parts"][4]["exhibits"][0]["table"]
    kr28 = raw[raw.order_id == "KR-00028"][["order_id", "segment", "order_amount", "paid_amount"]]
    assert [[a, b, num(c), num(d)] for a, b, c, d in part5["rows"]] == \
        [[a, b, float(c), float(d)] for a, b, c, d in kr28.itertuples(index=False)]
    assert raw.order_amount.sum() == 394095490
    dedup_raw = raw.drop_duplicates()
    assert len(dedup_raw) == 1400 and dedup_raw.order_amount.sum() == 394057740
    flagged = raw[~raw.order_id.duplicated(keep="first")]
    assert flagged.order_amount.sum() == 198400000
    show(25, "fix-tree", "f", "the first-row flag ties to Rs 19,84,00,000; Remove Duplicates leaves 1,400 rows")

    # Q26 fix-whatif: Rs 5,00,000 typed over Retail-Plus in July to September against April to
    # June's Rs 5,85,770.
    assert round((500000 - 585770) / 585770 * 100, 1) == -14.6
    assert round((413380 - 585770) / 585770 * 100, 1) == -29.4
    show(26, "fix-whatif", "c", "the typed value reads down 14.6 percent against Finance's 29.4")

    # Q27 range-check: the exhibit's sheet, worked; the formula's range stops at row 5.
    sheet27 = {int(r[0]): r[2] for r in table_of("range-check")["rows"]}
    assert sheet27[8] == "=AVERAGE(B2:B5)"
    values = [num(sheet27[r]) for r in range(2, 8)]
    formula = sum(num(sheet27[r]) for r in range(2, 6)) / 4
    full = sum(values) / len(values)
    assert (formula, full, full - formula) == (-0.5, 1.0, 1.5)
    show(27, "range-check", "B8 returns -0.5; the six rows average 1.0; the formula understates growth "
         "by 1.5 points and turns growth into a fall.", "B2:B5 averages -0.5 against the six rows' 1.0")

    # Q28 var-formula: the sheet's formula and the one the modeller meant, on the three rows.
    sheet28 = [(num(r[1]), num(r[2])) for r in table_of("var-formula")["rows"]]
    got28 = [(round((n - o) / (o + n), 3), round((n - o) / ((o + n) / 2), 3)) for o, n in sheet28]
    assert got28 == [(0.130, 0.261), (-0.111, -0.222), (0.091, 0.182)]
    assert all(abs((n - o) / (o + n) / ((n - o) / ((o + n) / 2)) - 0.5) < 1e-12 for o, n in sheet28)
    show(28, "var-formula", "b", "every change is half the one meant, rising or falling",
         "Every change comes out at half its size, so the model understates how far rates move")

    # Q29 gross-fare: 25 percent of the gross fare against 25 percent of the fare after tax and fees.
    trips = [(num(r[1]), num(r[2]), num(r[3])) for r in table_of("gross-fare")["rows"]]
    assert all(round(0.25 * g, 2) == c for g, _, c in trips)             # the commission charged
    due = [round(0.25 * (g - f), 2) for g, f, _ in trips]
    extra = round(sum(c for _, _, c in trips) - sum(due), 2)
    assert due == [6.90, 4.60, 10.00] and extra == 2.00 == round(0.25 * sum(f for _, f, _ in trips), 2)
    assert sum(c for _, _, c in trips) == 23.50 and round(extra / 23.50 * 100, 1) == 8.5
    show(29, "gross-fare", "2.00 dollars, about 8.5 percent of the 23.50 dollars charged",
         "0.60 + 0.40 + 1.00 over-charged, 8.5 percent of 23.50")

    # ------------------------------------------------------------------ Part 6, the AI team
    # Q30 eval-fanout: run the exhibit as printed.
    assert run_python(code_of("eval-fanout")) == "7 0.43"
    assert 3 / 5 == 0.6
    show(30, "eval-fanout", "c", "prints 7 0.43 against a true 0.6", "7 0.43")

    # Q31 latest-run: the table's rows, and each approach in the options.
    runs = ("WITH eval_runs (model, run_id, finished_on, accuracy) AS (VALUES "
            "('bot-a', 'r1', DATE '2026-09-01', 0.81), ('bot-a', 'r2', DATE '2026-09-08', 0.78), "
            "('bot-b', 'r3', DATE '2026-09-02', 0.84), ('bot-b', 'r4', DATE '2026-09-09', 0.86), "
            "('bot-b', 'r5', DATE '2026-09-09', 0.79)) ")
    assert [r[1] for r in table_of("latest-run")["rows"]] == ["r1", "r2", "r3", "r4", "r5"]
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
    show(31, "latest-run", "d", "row 1 by date then run_id: r2 and r5; RANK keeps r4 and r5",
         "ROW_NUMBER partitioned by model, ordered by finished_on descending, then run_id "
         "descending, keeping row 1")

    # Q32 low-ratings: run the exhibit as printed, the three misreadings and the query the lead
    # asked for.
    assert rows(cur, code_of("low-ratings")) == [("bot-a", 3)]
    body = code_of("low-ratings").split("SELECT model")[0]
    having_all = rows(cur, body + """SELECT model, count(*) FILTER (WHERE rating <= 2) FROM replies
        GROUP BY model HAVING count(*) >= 3 ORDER BY model""")
    assert having_all == [("bot-a", 3), ("bot-b", 1)]                    # option b, and the ask
    no_where = rows(cur, body + """SELECT model, count(*) FROM replies GROUP BY model
        HAVING count(*) >= 3 ORDER BY model""")
    assert no_where == [("bot-a", 4), ("bot-b", 3)]                      # option c
    no_having = rows(cur, body + """SELECT model, count(*) FROM replies WHERE rating <= 2
        GROUP BY model ORDER BY model""")
    assert no_having == [("bot-a", 3), ("bot-b", 1), ("bot-c", 1)]       # option d
    show(32, "low-ratings", "a", "returns bot-a 3 alone; the ask is bot-a 3 and bot-b 1",
         "bot-a 3 alone, which misses bot-b and its three replies")

    # Q33 not-in: run the exhibit as printed, and the anti-join that works.
    assert one(cur, code_of("not-in")) == (0,)
    works = code_of("not-in").replace(
        "WHERE conversation_id NOT IN (SELECT conversation_id FROM handoffs)",
        "WHERE NOT EXISTS (SELECT 1 FROM handoffs h WHERE h.conversation_id = conversations.conversation_id)")
    assert one(cur, works) == (2,)
    show(33, "not-in", "c", "NOT IN returns 0; NOT EXISTS returns 2",
         "0, so the review concludes the assistant resolved nothing on its own")

    # Q34 token-peers: run the exhibit as printed, and the two variants the reasons name.
    assert [r[1] for r in rows(cur, code_of("token-peers"))] == [400, 1200, 1200, 1400]
    tiebreak = code_of("token-peers").replace("OVER (ORDER BY day)", "OVER (ORDER BY day, call_id)")
    assert [r[1] for r in rows(cur, tiebreak)] == [400, 700, 1200, 1400]
    whole = code_of("token-peers").replace("OVER (ORDER BY day)", "OVER ()")
    assert [r[1] for r in rows(cur, whole)] == [1400, 1400, 1400, 1400]
    show(34, "token-peers", "a", "400, 1200, 1200, 1400; peers share the day's figure",
         "400, 1200, 1200 and 1400")

    # Q35 weekly-users: the log worked four ways, and Kalpa's own distinct counts the reason cites.
    t35 = table_of("weekly-users")
    log = {day: [u.strip() for u in cell.split(",")]
           for day, cell in zip(t35["head"][1:], t35["rows"][0][1:])}
    assert list(log) == ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    daily = [len(v) for v in log.values()]
    assert (sum(daily), round(sum(daily) / 7, 1), max(daily)) == (16, 2.3, 3)
    assert len({u for v in log.values() for u in v}) == 6
    assert sum("U1" in v for v in log.values()) == 4
    buyers = one(cur, """SELECT count(DISTINCT customer_id) FILTER (WHERE quarter = 'Q1'),
                                count(DISTINCT customer_id) FILTER (WHERE quarter = 'Q2'),
                                count(DISTINCT customer_id) FROM orders""")
    assert buyers == (244, 227, 301) and 244 + 227 == 471
    show(35, "weekly-users", "d", "the days add to 16; the week's distinct users are 6", "6")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W02/SAT/internal/C2_W02_SAT_key_proofs_INTERNAL.py, with Postgres 16 on
# localhost and the default credentials
#     Prints the versions, then 35 lines, PASS Q1 to PASS Q35, each with the item's id, its key
#     and what was checked, then "RESULT: PASS (35 items proved)", and leaves no schema behind.
# The same run with the source file's facebook exhibit changed to count(*) in the calculated line
#     The assertion on 10.0 and 6.0 fails with a traceback at Q6 and the exit code is 1; the
#     scratch schema is still dropped by the finally block.
# The same run with a figure in the reporting-day table retyped
#     Q10's comparison with the warehouse fails for app or store, or the web gap is no longer
#     Rs 21,750, and the run exits 1.
# The same run with join-counts' key changed to a in the source file
#     show() fails at Q7, because the key it asserts is no longer the one the source prints.
# Postgres not running
#     psycopg2.OperationalError at connect, exit code 1, and nothing is created.
# A fresh warehouse file whose Retail-Plus tie at fiftieth has gone
#     Q12's counts assertion fails, naming no value, and the paper's Set 2 must be rebuilt.

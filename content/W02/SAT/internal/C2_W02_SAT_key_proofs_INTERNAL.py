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
    show(1, "int-div", "It prints 2 and 1. The note should say orders per member fell about 22 percent, "
         "from 2.36 to 1.84.", "prints 2 and 1; numeric gives 2.36 and 1.84, a fall of 22 percent")

    # Q2 bank 2: the room's LIMIT trap, reproduced on a fresh load of the warehouse, and the stem
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
    show(2, "bank 2", "d (guarantee)", "LIMIT 5 with no ORDER BY: Rs 3,900, then Rs 4,590 after a reload")

    # Q3 bank 3: a definition; CTE matches the tracker's key by the word before its bracket.
    show(3, "bank 3", "b (CTE)", "the word bank's option b is the tracker key's head word")

    # Q4 avg-spend: run the exhibit on the warehouse, and the coalesce version the reason names.
    assert one(cur, "SELECT count(*) FROM customers WHERE segment = 'Retail-Plus'")[0] == 120
    assert one(cur, code_of("avg-spend"))[0] == Decimal("5439")
    nulls = one(cur, code_of("avg-spend").replace(
        "SELECT round(avg(spend)) AS avg_spend", "SELECT count(*), count(spend)"))
    assert nulls == (120, 76)                                          # 44 members carry NULL
    zeroed = code_of("avg-spend").replace("sum(o.amount) AS spend", "coalesce(sum(o.amount), 0) AS spend")
    assert one(cur, zeroed)[0] == Decimal("3445")                      # option b, the head's figure
    show(4, "avg-spend", "c", "avg skips the 44 NULL spends: 5439 over 76; over 120 it is 3445",
         "5439, the average over the 76 members who ordered")

    # Q5 tool-choice: a judgement on Monday's rule, which names the figures it governs and leaves
    # exploration in a notebook (Monday's study notes, "Anand's ask, and what it rules out").
    show(5, "tool-choice", "a", "the chart is none of the Monday figures, so it is exploration",
         "In a notebook that reads the warehouse, since this chart is none of the Monday figures "
         "the rule governs")

    # Q6 facebook: run the exhibit as printed.
    calculated, defined = one(cur, code_of("facebook"))
    assert (calculated, defined) == (Decimal("10.0"), Decimal("6.0"))
    over = (calculated - defined) / defined
    assert round(over * 100, 1) == Decimal("66.7")                    # about 67 percent, option d
    assert round((calculated - defined) / calculated * 100) == 40     # the wrong base, option a
    assert (14 + 9 + 4) / 3 == 9.0 and round((9.0 / 6.0 - 1) * 100) == 50   # option b
    assert 60 <= float(over) * 100 <= 80                               # inside TechCrunch's range
    show(6, "facebook", "d", "returns 10.0 and 6.0; 10 over 6 is 66.7 percent too high",
         "About 67 percent")

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

    # Q7 join-counts: run the exhibit as printed, and each distractor's reading.
    got = one(cur, code_of("join-counts"))
    assert got == (678, 648)
    assert 216 + 2 * 188 + 2 * 28 + 30 == 678 and 678 - 30 == 648
    assert (462, 462 - 30) == (462, 432)                               # b: one row per order
    collapsed = one(cur, """SELECT count(*), count(p.order_id) FROM orders o LEFT JOIN
        (SELECT DISTINCT order_id, instalment_no, amount, paid_date, method FROM payments) p
        ON p.order_id = o.order_id WHERE o.quarter = 'Q2'""")
    assert collapsed == (650, 620)                                     # c: each retry's two rows kept once
    retry_cols = one(cur, """SELECT count(*) FROM (SELECT order_id, instalment_no FROM payments
        GROUP BY 1, 2 HAVING count(*) > 1 AND count(DISTINCT (paid_date, amount, method)) = 1) r""")[0]
    assert retry_cols == 50                       # every retry's two rows differ only in payment_id
    assert (678 + 8, 648 + 8) == (686, 656)                            # d: the orphans counted
    show(7, "join-counts", "a", "678 rows out and 648 payment rows", "678 and 648")

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
    assert joined_first == 650 == 462 + 188                         # b reads f's figures, not raw rows
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
    # The stem states Tuesday's chapter 6 rule: booked always leaves; a collected figure that does
    # not reconcile is held, with the open line; a channel reconciles when its gap equals its list.
    assert "booked always leaves" in ADD["reporting-day"]["text"]
    assert "a collected figure that does not reconcile never leaves" in ADD["reporting-day"]["text"]
    show(10, "reporting-day", "c", "app and store close to the rupee; web's gap exceeds its list by Rs 21,750",
         "Booked for every channel, collected for app and store, and web's collected held back")

    # Q11 phe-checks: each check worked on Lab B's row of the exhibit; c and e fire.
    labs = {r[0]: [num(c) for c in r[1:]] for r in table_of("phe-checks")["rows"]}
    csv, sheet, loaded, before = labs["Lab B"]
    fires = {"a": loaded != sheet, "b": False, "c": loaded != csv,
             "d": loaded < before, "e": sheet == 65536 - 1}
    assert [k for k, v in fires.items() if v] == ["c", "e"] and csv - loaded == 5365
    assert all(r[0] == r[1] == r[2] for k, r in labs.items() if k != "Lab B")   # A and C lost nothing
    show(11, "phe-checks", "c, e", "only the CSV count and the limit check see Lab B's 5,365 lost rows")

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
    shown12 = [(int(a), b, int(c.replace(",", ""))) for a, b, c in table_of("rows-shipped")["rows"]]
    window = ranked[(ranked.rn >= 46) & (ranked.rn <= 53)]
    assert shown12 == [(int(r.rn), r.customer_id, int(r.q2)) for r in window.itertuples()]

    # Q12 rows-shipped: the head's rule is every member who spent at least as much as the fiftieth,
    # and nobody who spent less; only RANK's list is exactly that set.
    counts = ((ranked.rk <= 50).sum(), (ranked.dr <= 50).sum(), (ranked.rn <= 50).sum())
    assert counts == (51, 52, 50)
    fiftieth = ranked[ranked.rn == 50].q2.item()
    rule = set(ranked[ranked.q2 >= fiftieth].customer_id)
    assert set(ranked[ranked.rk <= 50].customer_id) == rule and len(rule) == 51       # d
    assert set(ranked[ranked.dr <= 50].customer_id) - rule == {"C-0259"}              # a adds C-0259
    assert rule - set(ranked[ranked.rn <= 50].customer_id) == {"C-0242"}              # b drops C-0242
    whole_ties = ranked[ranked.q2 > fiftieth]
    assert len(whole_ties) == 49                                                      # c
    show(12, "rows-shipped", "d", "RANK keeps the 51 members at or above the fiftieth's Rs 3,350",
         "RANK, keeping every member ranked 50 or better: 51 members")

    # Q13 bank 27: the whole-table top fifty and the reason the reworded stem gives.
    whole = frame(cur, """
        WITH m AS (SELECT o.customer_id, c.segment, sum(o.amount) AS q2 FROM orders o
                   JOIN customers c USING (customer_id) WHERE o.quarter = 'Q2'
                   GROUP BY o.customer_id, c.segment)
        SELECT * FROM m ORDER BY q2 DESC, customer_id""")
    top = whole.head(50)
    assert top.segment.value_counts().to_dict() == {"Business": 35, "Retail-Plus": 11, "Retail-Core": 4}
    assert (whole.segment == "Business").sum() == 35                   # every Business buyer made it
    smallest_business = whole[whole.segment == "Business"].q2.min()
    largest_retail = whole[whole.segment != "Business"].q2.max()
    assert (smallest_business, largest_retail) == (Decimal("225000.00"), Decimal("21740.00"))
    assert smallest_business / largest_retail >= 10
    assert "ten times the largest retail spend" in edits[27]["stem"]["text"]
    assert edits[27]["options"]["b"].startswith("A rank within PARTITION BY segment")
    show(13, "bank 27", "b", "all 35 Business buyers top the list; the smallest is ten times any retail spend")

    # Q14 share-window: the four queries on member_step, built from the warehouse.
    member_step = ("WITH member_step AS (SELECT o.customer_id, sum(o.amount) AS spend FROM orders o "
                   "JOIN customers c USING (customer_id) WHERE c.segment = 'Retail-Plus' "
                   "AND o.quarter = 'Q2' GROUP BY o.customer_id) ")
    opts14 = options_of("share-window")
    results = {}
    for letter, query in opts14.items():
        got14 = rows(cur, member_step + query + " ORDER BY spend DESC")
        results[letter] = [float(r[2]) for r in got14]
    assert abs(sum(results["a"]) - 1) < 1e-9 and len(results["a"]) == 76     # a: shares add to 1
    assert all(abs(s - 1) < 1e-9 for s in results["b"])                      # b: every share 1
    assert abs(results["c"][0] - 1) < 1e-9 and results["c"][1] < 1           # c: a running total
    assert all(abs(s - 1) < 1e-9 for s in results["d"])                      # d: every share 1
    show(14, "share-window", "a", "OVER () shares add to 1; GROUP BY and PARTITION BY give 1 each",
         "SELECT customer_id, spend, spend / sum(spend) OVER () FROM member_step")

    # Q15 lag-gap: the exhibit's months are the warehouse's, the flag as the stem states it, the
    # untrue calls, and the counts each misreading gives.
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
    assert (len(calls), len(untrue)) == (4, 2)                              # b
    assert len(flag[flag.calendar_ok]) == 2                                 # a: LAG read as the calendar
    assert len([c for c in calls if c != "C-0216"]) == 3                    # c: C-0216 wrongly dropped
    no_gap = [m for m, *cells in table["rows"]
              if all(c for c in cells[next(k for k, c in enumerate(cells) if c):])]
    assert no_gap == ["C-0171"]                                             # d: any gap drops a member
    show(15, "lag-gap", "b", "4 flagged; C-0185 and C-0216 had no August, so 2 calls are untrue",
         "4 calls, two of them untrue")

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
    # The chart reads every other plan week, named by its Monday as Wednesday's chapter 5 names them,
    # and the close, the week of 28 September, which holds one day.
    starts = [w.strftime("%-d %b") for w in pd.to_datetime(every_other.week_start)]
    head16 = ex16["table"]["head"]
    assert head16[0] == "Plan week of" and starts[:-1] == head16[1:-1]
    assert starts[-1] == "28 Sep" and head16[-1] == "28 Sep, the close"
    assert ex16["mermaid"].count('"') and all(f'"{s}"' in ex16["mermaid"] for s in starts[:-1])
    assert weeks.to_date.iloc[-1] == one(cur, "SELECT sum(amount) FROM orders WHERE quarter = 'Q2'")[0]
    # The plan line the Part 3 opening describes: 13 weeks from Monday 6 July at Rs 75,69,230 each,
    # and the 25 orders of 1 to 5 July that fall before it, which the first plan week carries.
    plan_shape = one(cur, """SELECT count(*), min(week_start), max(week_start), min(plan_revenue),
                                    max(plan_revenue) FROM plan_line""")
    assert plan_shape == (13, pd.Timestamp("2026-07-06").date(), pd.Timestamp("2026-09-28").date(),
                          Decimal("7569230.00"), Decimal("7569230.00"))
    early = one(cur, """SELECT count(*), sum(amount) FROM orders
                        WHERE order_date BETWEEN DATE '2026-07-01' AND DATE '2026-07-05'""")
    assert early == (25, Decimal("1539820.00"))
    lead = [round(b - p, 2) for b, p in zip(bars, line)]
    assert lead == [-0.25, 1.95, 2.17, 1.57, 0.73, 0.79, 0.0]               # read from the table
    exact = [int(t - p) for t, p in zip(every_other.to_date, every_other.plan_to_date)]
    assert exact == [-2469050, 19536790, 21669660, 15751980, 7273670, 7970130, 10]
    assert max(lead) == lead[2] and starts[2] == "3 Aug"                   # c: furthest ahead, 3 Aug
    assert lead[5] == 0.79 and round(exact[5] / 1e7, 1) == 0.8 and starts[5] == "14 Sep"   # c: 0.8
    assert lead[1] < lead[2] and lead[4] == 0.73                            # a is false twice
    assert all(x > 0 for x in lead[1:-1])                                   # b is false
    assert lead[3] < lead[2]                                                # d is false
    assert one(cur, "SELECT sum(plan_revenue) FROM plan_line")[0] == Decimal("98399990.00")
    plan = float(weeks.plan_revenue.iloc[0])
    last7 = weeks[(weeks.week_start >= pd.Timestamp("2026-08-10").date())
                  & (weeks.week_start <= pd.Timestamp("2026-09-21").date())]
    assert plan == 7569230.0 and sum(float(b) < plan for b in last7.booked) == 6
    july = weeks[weeks.week_start == pd.Timestamp("2026-07-13").date()].iloc[0]
    assert july.booked == Decimal("26628920.00")
    show(16, "run-rate", "c", "the lead peaks at Rs 2,16,69,660 in the week of 3 Aug; 0.8 crore on 14 Sep",
         "Furthest ahead in the week of 3 August, by about Rs 2.2 crore, and about Rs 0.8 crore ahead "
         "in the week of 14 September")

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
    # The Part 4 opening: recency counts to the data's last date, and the sale ran in August.
    assert str(orders.order_date.max()) == "2026-09-28"
    sale = one(cur, "SELECT name, start_date, end_date FROM campaigns WHERE campaign_id = 'CMP-MONSOON-26'")
    assert sale[0] == "Monsoon Sale" and sale[1].month == sale[2].month == 8

    # Q17 merge-guard: the rows, the guard that stops them, and each distractor's reading.
    assert len(merged) == 346 == 340 + (136 - 130)
    assert merged.spend.sum() - 198400000.0 == 45800.0                 # the pivot's overstatement
    try:
        table.merge(feed, on="customer_id", how="left", validate="one_to_one")
        raise AssertionError("validate did not raise")
    except pd.errors.MergeError as e:
        assert "not unique in right dataset" in str(e)
    assert 340 + 2 * 6 == 352 and len(merged.drop_duplicates()) == 346  # c: nothing to drop
    ind = table.merge(feed, on="customer_id", how="left", indicator=True)
    assert len(ind) == 346 and set(ind["_merge"]) <= {"both", "left_only"}   # d: labels, no stop
    assert len(table.merge(feed, on="customer_id", how="inner")) == 136
    show(17, "merge-guard", "a", "346 rows; validate raises MergeError; drop_duplicates keeps all 346",
         "346 rows, and validate='one_to_one' on the merge, which raises a MergeError")

    # Q18 first-touch: the exhibit's rows are the week's feed in the order the tool sends it; the
    # exhibit's step run on them, each option's reading, the credit it costs, and the sort that fixes it.
    sent = feed.sort_values("exposed_date", ascending=False, kind="stable").reset_index(drop=True)
    t18 = table_of("first-touch")
    shown18 = pd.DataFrame(t18["rows"], columns=t18["head"])
    picked = sent[sent.customer_id.isin(["C-0001", "C-0002", "C-0012"])].reset_index(drop=True)
    assert shown18.equals(picked)
    step = code_of("first-touch")
    assert step == 'first = feed.drop_duplicates(subset="customer_id")'
    scope = {"feed": shown18}
    exec(step, scope)
    kept18 = dict(zip(scope["first"].customer_id, scope["first"].exposed_date))
    assert kept18 == {"C-0001": "2026-08-11", "C-0002": "2026-08-11", "C-0012": "2026-08-03"}   # d
    first_day = feed.groupby("customer_id").exposed_date.min()
    assert first_day["C-0001"] == "2026-08-03" != kept18["C-0001"]          # a: first as listed is not first
    assert len(shown18.drop_duplicates()) == 5 and len(scope["first"]) == 3  # b: subset keeps one row each
    assert "C-0001" not in set(shown18.drop_duplicates("customer_id", keep=False).customer_id)
    assert "C-0001" in kept18                                                 # c: keep='first' is the default
    lost = one(cur, """SELECT count(*), sum(amount) FROM orders WHERE customer_id = 'C-0001'
                        AND order_date BETWEEN DATE '2026-08-03' AND DATE '2026-08-10'""")
    assert lost == (1, Decimal("1200.00"))                                    # the order of 6 August
    assert (pd.Timestamp("2026-08-11") - pd.Timestamp("2026-08-03")).days == 8

    def first_exposures(f):
        return (f.set_index("customer_id").exposed_date == first_day.reindex(f.customer_id).values).all()

    scope = {"feed": sent}
    exec(step, scope)
    assert len(scope["first"]) == 130 and not first_exposures(scope["first"])  # the week's feed, same step
    d18 = sent.sort_values("exposed_date", kind="stable").drop_duplicates("customer_id")
    assert len(d18) == 130 and first_exposures(d18)                           # the answer line's sort
    fixed = table.merge(d18, on="customer_id", how="left", validate="one_to_one")
    assert len(fixed) == 340 and fixed.spend.sum() == 198400000.0 and fixed.campaign_id.notna().sum() == 130
    show(18, "first-touch", "d", "the step keeps 11 August for C-0001; its 6 August order goes uncredited",
         "The 11 August send, so the orders C-0001 placed in the eight days before it go uncredited")

    # Q19 months-view: run the exhibit as printed, and the misreadings behind the distractors.
    assert run_python(code_of("months-view")) == "2000.0 4 5600.0"
    plus = pd.DataFrame({"member": ["M1", "M1", "M1", "M2", "M2"],
                         "month": ["Jun", "Jun", "Jul", "Jun", "Jun"],
                         "amount": [3000, 1000, 2400, 1800, 600]})
    summed = plus.pivot_table(index="member", columns="month", values="amount", aggfunc="sum")
    firsts = plus.pivot_table(index="member", columns="month", values="amount", aggfunc="first")
    assert (summed.loc["M1", "Jun"], summed.sum().sum(), len(plus)) == (4000, 8800, 5)   # a, d
    assert (firsts.loc["M1", "Jun"], firsts.sum().sum()) == (3000, 7200)                 # c
    # The reason's Kalpa figures, Thursday's chapter 3: the default pivot over Retail-Plus's months
    # reads a fall of 18 percent where the orders fell 29.4.
    rp_orders = orders.merge(customers[["customer_id", "segment"]], on="customer_id")
    rp_orders = rp_orders[rp_orders.segment == "Retail-Plus"].copy()
    rp_orders["month"] = pd.to_datetime(rp_orders.order_date).dt.month
    averaged = rp_orders.pivot_table(index="customer_id", columns="month", values="amount")
    q1_avg, q2_avg = averaged[[4, 5, 6]].sum().sum(), averaged[[7, 8, 9]].sum().sum()
    assert (round(q1_avg), round(q2_avg)) == (412019, 337267)
    assert round((1 - q2_avg / q1_avg) * 100) == 18
    assert round((1 - 413380 / 585770) * 100, 1) == 29.4
    show(19, "months-view", "b", "prints 2000.0 4 5600.0", "2000.0 4 5600.0")

    # Q20 genes: run the exhibit as printed, and the readings behind the distractors.
    assert run_python(code_of("genes")) == "5 3"
    outer = run_python(code_of("genes").replace('how="left"', 'how="outer"'))
    assert outer == "7 5"                                                  # c: the outer reading
    show(20, "genes", "b", "prints 5 3: TP53 twice, two dates unmatched", "5 3")

    # ------------------------------------------------------------------ Part 5, Friday
    fixes = SRC["banks"]["fri-fix"]["options"]
    letter = {o: "abcdef"[k] for k, o in enumerate(fixes)}
    assert letter["XLOOKUP with its if_not_found argument set"] == ADD["fix-lookup"]["key"] == "d"
    assert letter["SUBTOTAL with function number 109"] == ADD["fix-foot"]["key"] == "a"
    assert letter["a first-row flag per order, then SUMIFS"] == ADD["fix-tree"]["key"] == "f"
    assert letter["a labelled input cell feeding a scenario line"] == ADD["fix-whatif"]["key"] == "c"
    clean = pd.read_csv(CLEAN_TABLE)
    raw = pd.read_csv(RAW_EXPORT)

    # Q21 fix-lookup. Excel reasoning: VLOOKUP with its fourth argument left out looks for an
    # approximate match, which on a table sorted by id returns the largest id not above the one
    # asked for; XLOOKUP matches exactly by default and shows its fourth argument, if_not_found,
    # for a missing code (Microsoft Support, VLOOKUP and XLOOKUP, verified 29 September 2026).
    # Emulated here on Friday's clean table.
    ids = sorted(clean.customer_id)
    assert "C-0195" not in ids
    neighbour = ids[bisect_right(ids, "C-0195") - 1]
    assert neighbour == "C-0194"
    assert int(clean.set_index("customer_id").loc[neighbour, "revenue"]) == 16740
    show(21, "fix-lookup", "d", "an approximate match returns C-0194's Rs 16,740 for C-0195")

    # Q22 fix-foot. Excel reasoning: SUM adds every row in its range, hidden or not; SUBTOTAL(109)
    # adds only the rows on screen. The protect list is Friday's fifty Retail-Plus members.
    plus_list = clean[clean.segment == "Retail-Plus"].sort_values(["revenue", "customer_id"],
                                                                  ascending=[False, True]).head(50)
    mumbai = plus_list[plus_list.city == "Mumbai"]
    assert int(plus_list.revenue.sum()) == 714890 and len(mumbai) == 11 and int(mumbai.revenue.sum()) == 156790
    assert round(714890 / 156790, 1) == 4.6
    show(22, "fix-foot", "a", "SUBTOTAL(109) reads Rs 1,56,790 for Mumbai's 11; SUM Rs 7,14,890")

    # Q23 fix-tree. Excel reasoning: =IF(COUNTIF($A$2:A2,A2)=1,1,0) is 1 on the first row of each
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
    show(23, "fix-tree", "f", "the first-row flag ties to Rs 19,84,00,000; Remove Duplicates leaves 1,400 rows")

    # Q24 fix-whatif: Rs 5,00,000 typed over Retail-Plus in July to September against April to
    # June's Rs 5,85,770.
    assert round((500000 - 585770) / 585770 * 100, 1) == -14.6
    assert round((413380 - 585770) / 585770 * 100, 1) == -29.4
    show(24, "fix-whatif", "c", "the typed value reads down 14.6 percent against Finance's 29.4")

    # Q25 range-check: the exhibit's sheet, worked; B8's range stops at row 5 and C8's does not.
    sheet25 = {int(r[0]): r[2:] for r in table_of("range-check")["rows"]}
    assert sheet25[8] == ["=AVERAGE(B2:B5)", "=AVERAGE(C2:C7)"]
    b_col = [num(sheet25[r][0]) for r in range(2, 8)]
    c_col = [num(sheet25[r][1]) for r in range(2, 8)]
    b8 = sum(b_col[:4]) / 4
    c8 = sum(c_col) / 6
    b_all = sum(b_col) / 6
    assert (b8, c8, b_all) == (-0.5, 1.5, 1.5) and c8 - b8 == 2.0
    show(25, "range-check", "The sheet reports -0.5 against 1.5, a gap of 2 points; B8 stops at row 5, "
         "and over all six countries both columns average 1.5, so the gap disappears.",
         "B2:B5 gives -0.5; all six rows give 1.5 in both columns")

    # Q26 var-formula: the sheet's formula against the documented one, and the value at risk.
    sheet26 = [(num(r[1]), num(r[2])) for r in table_of("var-formula")["rows"]]
    got26 = [(round((n - o) / (o + n), 3), round((n - o) / ((o + n) / 2), 3)) for o, n in sheet26]
    assert got26 == [(0.130, 0.261), (-0.111, -0.222), (0.091, 0.182)]
    assert all(abs((n - o) / (o + n) / ((n - o) / ((o + n) / 2)) - 0.5) < 1e-12 for o, n in sheet26)
    var_sheet, limit = 70, 120
    var_true = var_sheet * 2
    assert (var_true, var_true - limit) == (140, 20)
    show(26, "var-formula", "Column D halves every change, 0.130 against 0.261, so the value at risk "
         "should read 140 million dollars, 20 million over the limit.", "half-size changes: 70 reads 140, over 120")

    # Q27 gross-fare: 25 percent of the gross fare against 25 percent of the fare after tax and fees.
    trips = [(num(r[1]), num(r[2]), num(r[3])) for r in table_of("gross-fare")["rows"]]
    assert all(round(0.25 * g, 2) == c for g, _, c in trips)             # charged on the gross fare
    due = [round(0.25 * (g - f), 2) for g, f, _ in trips]
    extra = round(sum(c for _, _, c in trips) - sum(due), 2)
    assert due == [6.90, 4.60, 10.00] and extra == 2.00 == round(0.25 * sum(f for _, f, _ in trips), 2)
    assert sum(c for _, _, c in trips) == 23.50 and round(extra / 23.50 * 100, 1) == 8.5
    show(27, "gross-fare", "2.00 dollars, about 8.5 percent of the 23.50 dollars charged",
         "0.60 + 0.40 + 1.00 over-charged, 8.5 percent of 23.50")

    # ------------------------------------------------------------------ Part 6, the AI team
    # Q28 eval-fanout: run the exhibit as printed, and the readings behind the distractors.
    assert run_python(code_of("eval-fanout")) == "0.43"
    assert (3 / 5, round(5 / 7, 2)) == (0.6, 0.71)                       # a, and b counting repeats right
    try:
        run_python(code_of("eval-fanout").replace('on="ticket")', 'on="ticket", validate="many_to_one")'))
        raise AssertionError("validate did not raise")
    except pd.errors.MergeError:
        pass                                                             # d: raises only when asked to
    assert 0.43 < 0.5 <= 0.6                                             # held back on 0.43; 0.6 would ship
    show(28, "eval-fanout", "c", "prints 0.43 against a true 0.6; the bar is 0.5",
         "0.43, so the model falls short of the bar and is held back")

    # Q29 latest-run: the table's rows, and each option's query and call.
    t29 = table_of("latest-run")["rows"]
    values = ", ".join(f"('{m}', {int(r)}, DATE '2026-09-{int(d.split()[0]):02d}', {a})"
                       for m, r, d, a in t29)
    runs = f"WITH eval_runs (model, run_id, finished_on, accuracy) AS (VALUES {values}) "
    latest = rows(cur, runs + """SELECT model, run_id, accuracy FROM (
        SELECT *, row_number() OVER (PARTITION BY model ORDER BY finished_on DESC, run_id DESC) AS rn
        FROM eval_runs) x WHERE rn = 1 ORDER BY model""")
    assert latest == [("bot-a", 9, Decimal("0.78")), ("bot-b", 11, Decimal("0.74"))]   # a: bot-a stays
    ascending = rows(cur, runs + """SELECT model, run_id, accuracy FROM (
        SELECT *, row_number() OVER (PARTITION BY model ORDER BY finished_on DESC, run_id ASC) AS rn
        FROM eval_runs) x WHERE rn = 1 ORDER BY model""")
    assert ascending[1] == ("bot-b", 10, Decimal("0.86"))                     # b: promotes bot-b
    grouped = rows(cur, runs + "SELECT model, max(accuracy) FROM eval_runs GROUP BY model ORDER BY model")
    assert grouped == [("bot-a", Decimal("0.81")), ("bot-b", Decimal("0.86"))]  # c: promotes bot-b
    ranked29 = rows(cur, runs + """SELECT model, run_id FROM (
        SELECT *, rank() OVER (PARTITION BY model ORDER BY finished_on DESC) AS rk
        FROM eval_runs) x WHERE rk = 1 ORDER BY model, run_id""")
    assert ranked29 == [("bot-a", 9), ("bot-b", 10), ("bot-b", 11)]            # d: two rows for bot-b
    assert sorted(["11", "9"]) == ["11", "9"] and sorted([11, 9]) == [9, 11]   # text sorts '11' first
    show(29, "latest-run", "a", "run 11 is bot-b's latest at 0.74 against bot-a's 0.78",
         "ROW_NUMBER partitioned by model, by finished_on descending, then run_id descending, "
         "keeping row 1: bot-b's latest scores 0.74, so bot-a stays")

    # Q30 low-ratings: run the exhibit as printed, the three misreadings and the lead's ask.
    assert rows(cur, code_of("low-ratings")) == [("bot-a", 3)]
    body = code_of("low-ratings").split("SELECT model")[0]
    asked = rows(cur, body + """SELECT model, count(*) FILTER (WHERE rating <= 2) FROM replies
        GROUP BY model HAVING count(*) >= 3 ORDER BY model""")
    assert asked == [("bot-a", 3), ("bot-b", 1)]                       # a: the lead's list, two models
    no_where = rows(cur, body + """SELECT model, count(*) FROM replies GROUP BY model
        HAVING count(*) >= 3 ORDER BY model""")
    assert no_where == [("bot-a", 4), ("bot-b", 3)]                    # b
    no_having = rows(cur, body + """SELECT model, count(*) FROM replies WHERE rating <= 2
        GROUP BY model ORDER BY model""")
    assert no_having == [("bot-a", 3), ("bot-b", 1), ("bot-c", 1)]     # c
    show(30, "low-ratings", "d", "returns bot-a 3 alone; the lead asked for bot-a and bot-b",
         "bot-a alone, beside its count of 3 low ratings, so the lead retrains bot-a")

    # Q31 not-in: run the exhibit as printed, the anti-join that works, and the budget rule.
    assert one(cur, code_of("not-in")) == (0,)
    works = code_of("not-in").replace(
        "WHERE conversation_id NOT IN (SELECT conversation_id FROM handoffs)",
        "WHERE NOT EXISTS (SELECT 1 FROM handoffs h WHERE h.conversation_id = conversations.conversation_id)")
    assert one(cur, works) == (2,)
    assert 0 / 4 < 0.40 <= 2 / 4                                        # cut on 0; kept on 2
    show(31, "not-in", "b", "NOT IN returns 0, under 40 percent; NOT EXISTS returns 2, half",
         "0, none of the conversations, so the budget is cut")

    # Q32 token-peers: run the exhibit as printed, and the first call over 1,000 under each reading.
    def first_over(totals):
        return next((k for k, t in enumerate(totals, 1) if t > 1000), None)

    peers = [r[1] for r in rows(cur, code_of("token-peers"))]
    assert peers == [400, 1200, 1200, 1400] and first_over(peers) == 2          # a
    tiebreak = code_of("token-peers").replace("OVER (ORDER BY day)", "OVER (ORDER BY day, call_id)")
    stepped = [r[1] for r in rows(cur, tiebreak)]
    assert stepped == [400, 700, 1200, 1400] and first_over(stepped) == 3       # b
    before = code_of("token-peers").replace(
        "OVER (ORDER BY day)", "OVER (ORDER BY day RANGE BETWEEN UNBOUNDED PRECEDING AND '1 day' PRECEDING)")
    earlier = [r[1] or 0 for r in rows(cur, before)]
    assert earlier == [0, 400, 400, 1200] and first_over(earlier) == 4          # c
    by_day = code_of("token-peers").replace("OVER (ORDER BY day)", "OVER (PARTITION BY day)")
    assert first_over([r[1] for r in rows(cur, by_day)]) is None                # d
    show(32, "token-peers", "a", "peers read 1200 at call 2; with call_id the switch comes at call 3",
         "Call 2")

    # Q33 weekly-users: the log worked four ways, and Kalpa's own distinct counts the reason cites.
    t33 = table_of("weekly-users")
    log = {day: [u.strip() for u in cell.split(",")]
           for day, cell in zip(t33["head"][1:], t33["rows"][0][1:])}
    assert list(log) == ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    daily = [len(v) for v in log.values()]
    assert (sum(daily), round(sum(daily) / 7, 1), max(daily)) == (16, 2.3, 3)
    assert len({u for v in log.values() for u in v}) == 6
    assert sum("U1" in v for v in log.values()) == 4
    buyers = one(cur, """SELECT count(DISTINCT customer_id) FILTER (WHERE quarter = 'Q1'),
                                count(DISTINCT customer_id) FILTER (WHERE quarter = 'Q2'),
                                count(DISTINCT customer_id) FROM orders""")
    assert buyers == (244, 227, 301) and 244 + 227 == 471
    show(33, "weekly-users", "d", "the days add to 16; the week's distinct users are 6", "6")

    # ------------------------------------------------------------------ The stretch answers
    # Stretch 1: every paid order paid within two days, instalments on one day, and the payment
    # rows on July to September orders that land in a week other than their order's.
    timing = one(cur, """SELECT max(lag), max(n_dates) FROM (SELECT o.order_id,
                             max(p.paid_date - o.order_date) AS lag, count(DISTINCT p.paid_date) AS n_dates
                         FROM orders o JOIN payments p USING (order_id) GROUP BY 1) x""")
    assert timing == (2, 1)
    crossing = one(cur, """SELECT count(*) FILTER (WHERE date_trunc('week', p.paid_date)
                                                  <> date_trunc('week', o.order_date)), count(*)
                           FROM payments p JOIN orders o USING (order_id) WHERE o.quarter = 'Q2'""")
    assert crossing == (169, 648)
    # Stretch 2: Retail-Plus members who bought in both quarters, of those who bought in either.
    both = one(cur, f"""SELECT count(*) FILTER (WHERE q1 > 0 AND q2 > 0), count(*) FROM (
                           SELECT customer_id, count(*) FILTER (WHERE quarter = 'Q1') AS q1,
                                  count(*) FILTER (WHERE quarter = 'Q2') AS q2
                           FROM ({rp}) r GROUP BY customer_id) x""")
    assert both == (60, 107)
    print("PASS  stretch answers: paid within 2 days, 169 of 648 rows cross a week; 60 of 107 in both")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W02/SAT/internal/C2_W02_SAT_key_proofs_INTERNAL.py, with Postgres 16 on
# localhost and the default credentials
#     Prints the versions, then 33 lines, PASS Q1 to PASS Q33, each with the item's id, its key
#     and what was checked, a line for the stretch answers' figures, then "RESULT: PASS (33 items
#     proved)", and leaves no schema behind.
# The same run with the source file's facebook exhibit changed to count(*) in the calculated line
#     The assertion on 10.0 and 6.0 fails with a traceback at Q6 and the exit code is 1; the
#     scratch schema is still dropped by the finally block.
# The same run with a figure in the reporting-day table retyped
#     Q10's comparison with the warehouse fails for app or store, or the web gap is no longer
#     Rs 21,750, and the run exits 1.
# The same run with join-counts' key changed to b in the source file
#     show() fails at Q7, because the key it asserts is no longer the one the source prints.
# Postgres not running
#     psycopg2.OperationalError at connect, exit code 1, and nothing is created.
# A fresh warehouse file whose Retail-Plus tie at fiftieth has gone
#     Q12's counts assertion fails, naming no value, and the item must be rebuilt.

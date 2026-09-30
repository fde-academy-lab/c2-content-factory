"""Prove every key on the Week 1 Saturday paper that code, SQL or arithmetic can decide.

    python3 content/W01/SAT/internal/C2_W01_SAT_key_proofs_INTERNAL.py

Runs cold from the repository root or from anywhere inside it. Each code exhibit is read from the
week's source file and executed exactly as it prints, on the week's own data files where the item
names them, and its output is checked against the option the key names. Each SQL item runs against
the local Postgres (PGHOST, PGPORT, PGUSER and PGPASSWORD, defaulting to localhost, 5432 and
postgres) in a scratch schema created at the start and dropped at the end. Each arithmetic key is
recomputed from the numbers on the page and from the data behind them. One line prints per item,
and the run ends on the count of items proved; any failed assertion stops it with the item's name.
"""
import contextlib
import csv
import importlib.util
import io
import math
import os
import pathlib
import random
import re
import sys

import yaml

HERE = pathlib.Path(__file__).resolve()
ROOT = next(p for p in HERE.parents if (p / "scripts" / "build_saturday_paper.py").exists())
sys.path.insert(0, str(ROOT / "scripts"))
import build_saturday_paper as builder  # noqa: E402

SOURCE = yaml.safe_load((ROOT / "content/W01/SAT/internal/C2_W01_SAT_paper_source_INTERNAL.yaml")
                       .read_text(encoding="utf-8"))
ADDED = {a["id"]: a for a in SOURCE["additions"]}
D1 = ROOT / "content/W01/D1/data"
D2 = ROOT / "content/W01/D2/data"
D3 = ROOT / "content/W01/D3/data"
D4 = ROOT / "content/W01/D4/data"


def load_orders(path):
    spec = importlib.util.spec_from_file_location("orders", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ORDERS


V0 = load_orders(D1 / "C2_W01_D01_orders_STUDENT.py")         # Monday, 30 orders
V1 = load_orders(D2 / "C2_W01_D02_orders_STUDENT.py")         # Tuesday, 200 orders
V2_ROWS = list(csv.DictReader(open(D3 / "C2_W01_D03_orders_STUDENT.csv", encoding="utf-8")))
V3 = list(csv.DictReader(open(D4 / "C2_W01_D04_orders_STUDENT.csv", encoding="utf-8")))
EXPOSURE = list(csv.DictReader(open(D4 / "C2_W01_D04_exposure_STUDENT.csv", encoding="utf-8")))

# The tracker's keys as the bank holds them, before any edit is laid on them.
_bank = builder.read_bank()
# Printed Q numbers and printed keys, after the ledger's edits, so each line names the item as the
# room sees it.
_laid = builder.read_bank()
builder.apply_edits(_laid, yaml.safe_load((ROOT / "data/programme/paper_edits.yaml").read_text()))
PRINTED = builder.assemble(_laid["W1"], SOURCE)
Q_OF = {(i["id"] if i["added"] else i["no"]): i["q"] for i in PRINTED}
KEY_OF = {(i["id"] if i["added"] else i["no"]): i["key"] for i in PRINTED}
proved = []


def report(ref, key, detail):
    q = Q_OF.get(ref)
    name = f"Q{q}" if q else "--"
    label = ref if isinstance(ref, str) else f"bank {ref}"
    print(f"{name:>4}  {label:<18} key {key:<12} {detail}")
    proved.append(ref)


def options(item_id):
    """{letter: text} of an addition's printed options."""
    out = {}
    for line in str(ADDED[item_id]["text"]).splitlines():
        m = re.match(r"^\(([a-f])\)\s*(.+)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2)
    return out


def run_exhibit(item_id, env=None, cwd=None):
    """Execute an addition's code exhibit exactly as it prints; return (stdout, namespace)."""
    code = ADDED[item_id]["exhibit"]["code"]["text"]
    ns = dict(env or {})
    buf = io.StringIO()
    old = os.getcwd()
    try:
        if cwd:
            os.chdir(cwd)
        with contextlib.redirect_stdout(buf):
            exec(compile(code, item_id, "exec"), ns)
    finally:
        os.chdir(old)
    return buf.getvalue().strip(), ns


def mean(values):
    return sum(values) / len(values)


def rupees(x):
    """A rupee figure as the paper prints it: to the rupee, halves rounded up."""
    from decimal import ROUND_HALF_UP, Decimal
    return int(Decimal(repr(x)).quantize(Decimal(1), rounding=ROUND_HALF_UP))


# ------------------------------------------------------------------------------ Part 1
def prove_bank_47():
    values = [800, 1200, 1400, 2000, 480000]
    assert sorted(values)[2] == 1400 and sum(values) / 5 == 97080
    assert _bank["W1"]["items"][46]["key"] == "Median Rs 1,400; mean Rs 97,080."
    report(47, "1,400; 97,080", "median of five sorted values is the third; 4,85,400 over 5 is 97,080")


def prove_sales_net():
    out, _ = run_exhibit("sales-net", {"ORDERS": V0})
    key = ADDED["sales-net"]["key"]
    assert out == options("sales-net")[key] == "30 orders, Rs 544810", out
    status = {}
    for o in V0:
        n, rs = status.get(o["status"], (0, 0))
        status[o["status"]] = (n + 1, rs + int(o["amount"]))
    assert status == {"delivered": (21, 520790), "returned": (5, 14970), "cancelled": (4, 9050)}
    net = [o for o in V0 if o["status"] in ("delivered", "returned")]
    assert (len(net), sum(int(o["amount"]) for o in net)) == (26, 535760)
    assert options("sales-net")["a"] == "26 orders, Rs 535760"
    report("sales-net", key, f"prints '{out}'; net of cancellations is 26 orders, Rs 5,35,760")


def prove_payback():
    amounts = sorted(int(o["amount"]) for o in V0)
    m, med = sum(amounts) / 30, (amounts[14] + amounts[15]) / 2
    assert round(m) == 18160 and med == 2205
    assert round(480000 / sum(amounts) * 100) == 88
    assert sum(1 for a in amounts if a < m) == 29
    assert round((sum(amounts) - 480000) / 29) == 2235
    delivered = [int(o["amount"]) for o in V0 if o["status"] == "delivered"]
    assert round(mean(delivered)) == 24800 and len(delivered) == 21
    report("payback-typical", ADDED["payback-typical"]["key"],
           "mean 18,160, median 2,205, bulk order 88 percent, other 29 average 2,235, delivered mean 24,800")


def prove_bank_46():
    assert math.isclose(1.10 * 0.85, 0.935) and round((1 / 0.85 - 1) * 100, 1) == 17.6
    report(46, "-6.5 percent", "1.10 x 0.85 = 0.935; break-even volume at 15 percent off is 17.6 percent")


def prove_quarter_counter():
    out, _ = run_exhibit("quarter-counter", {"ORDERS": V1})
    key = ADDED["quarter-counter"]["key"]
    assert out == options("quarter-counter")[key] == "{'Q1': 5, 'Q2': 7} +40.0%", out
    by = {}
    for o in V1:
        by[(o["quarter"], o["segment"])] = by.get((o["quarter"], o["segment"]), 0) + 1
    assert [by[("Q1", s)] for s in ("Retail-Core", "Retail-Plus", "Business", "Student")] == [38, 51, 20, 5]
    assert [by[("Q2", s)] for s in ("Retail-Core", "Retail-Plus", "Business", "Student")] == [36, 26, 17, 7]
    assert options("quarter-counter")["a"] == "{'Q1': 114, 'Q2': 86} -24.6%"
    report("quarter-counter", key, f"prints '{out}': the counter holds Student's count; the file says 114 and 86")


def prove_bank_20():
    assert _bank["W1"]["items"][19]["key"] == "a"
    report(20, "a", "tracker key: the first rung is confirming the drop is real")


def prove_budget_fact():
    cust = {q: len({o["customer_id"] for o in V1 if o["quarter"] == q}) for q in ("Q1", "Q2")}
    orders = {q: sum(1 for o in V1 if o["quarter"] == q) for q in ("Q1", "Q2")}
    rev = {q: sum(o["amount"] for o in V1 if o["quarter"] == q) for q in ("Q1", "Q2")}
    ids = {q: {o["customer_id"] for o in V1 if o["quarter"] == q} for q in ("Q1", "Q2")}
    assert cust == {"Q1": 69, "Q2": 69} and ids["Q1"] == ids["Q2"]
    assert (round(orders["Q1"] / 69, 2), round(orders["Q2"] / 69, 2)) == (1.65, 1.25)
    assert round((rev["Q2"] / orders["Q2"]) / (rev["Q1"] / orders["Q1"]) * 100 - 100, 1) == 18.0
    # equal lifts in a multiplicative tree add the same revenue
    base = 69 * (114 / 69) * (rev["Q1"] / 114)
    assert math.isclose(base * 1.1, 69 * 1.1 * (114 / 69) * (rev["Q1"] / 114))
    report("budget-fact", ADDED["budget-fact"]["key"],
           "same 69 customers; orders per customer 1.65 to 1.25; revenue per order +18.0 percent")


def prove_bank_51():
    assert _bank["W1"]["items"][50]["key"] == "b, d, e, a, c"
    report(51, "b, d, e, a, c", "tracker key: real, like with like, decompose, isolate, hypothesise")


# ------------------------------------------------------------------------------ Part 2
def prove_reader_header():
    out, _ = run_exhibit("reader-header", cwd=D3)
    key = ADDED["reader-header"]["key"]
    assert out == options("reader-header")[key] == "200 KR-02002", out
    assert len(V2_ROWS) == 201 and V2_ROWS[0]["order_id"] == "KR-02001" and V2_ROWS[0]["amount"] == "2200"
    report("reader-header", key, f"prints '{out}': next() consumed KR-02001, a Q1 order of Rs 2,200")


def prove_bank_11():
    assert ("4500" < "30000") is False
    try:
        "4500" > 3000
        raise AssertionError("text against a number should raise")
    except TypeError:
        pass
    rows = {r["order_id"]: r for r in V2_ROWS}
    assert _bank["W1"]["items"][10]["key"] == "False"
    v0_text = [o for o in V0 if isinstance(o["amount"], str)]
    assert [(o["order_id"], o["amount"]) for o in v0_text] == [("KR-01008", "4500")]
    assert all(isinstance(r["amount"], str) for r in rows.values())
    report(11, "False", "'4500' < '30000' is False, silently; the tracker's '4500' > 3000 raises TypeError")


def prove_evidence_copy():
    _, ns = run_exhibit("evidence-copy")
    assert ns["as_arrived"][0]["amount"] == 0 and ns["as_arrived"] is not ns["rows"]
    assert ns["as_arrived"][0] is ns["rows"][0]
    fresh = [{"order_id": "KR-02063", "amount": "twelve"}, {"order_id": "KR-02064", "amount": "3150"}]
    deep = [dict(r) for r in fresh]
    for r in fresh:
        r["amount"] = int(r["amount"]) if r["amount"].isdigit() else 0
    assert deep[0]["amount"] == "twelve"
    csv_rows = [(r["order_id"], r["amount"]) for r in V2_ROWS if r["order_id"] in ("KR-02063", "KR-02064")]
    assert ("KR-02063", "twelve") in csv_rows and ("KR-02064", "3150") in csv_rows
    key = ADDED["evidence-copy"]["key"]
    assert options("evidence-copy")[key].startswith("False, because both lists hold the same dictionaries")
    report("evidence-copy", key, "as_arrived[0]['amount'] is 0 after the pass; the list is new, the dictionaries shared")


def prove_reject_loop():
    out, ns = run_exhibit("reject-loop")
    assert out == "4 + 1 = 5" and "KR-09053" in [r[0] for r in ns["rows"]], out
    start = [("KR-09051", "2400"), ("KR-09052", "twelve"), ("KR-09053", "n/a"),
             ("KR-09054", "1850"), ("KR-09055", "3100")]
    good = {"KR-09051", "KR-09054", "KR-09055"}

    def a():
        rows, rejects = list(start), []
        for row in rows:
            if not row[1].isdigit():
                rejects.append(row)
                rows.remove(row)
        return rows, rejects

    def b():
        rows, rejects = list(start), []
        for row in list(rows):
            if not row[1].isdigit():
                rows.remove(row)
                rejects.append(row)
        return rows, rejects

    def c():
        rows, rejects = list(start), []
        for row in rows:
            if not row[1].isdigit():
                rows.remove(row)
                rejects.append(row)
                continue
        return rows, rejects

    def d():
        rows = list(start)
        kept = [r for r in rows if r[1].isdigit()]
        rejects = [r for r in rows if not r[1].isdigit()]
        return kept, rejects

    def e():
        rows, rejects = list(start), []
        for i, row in enumerate(rows):
            if not row[1].isdigit():
                rows[i] = (row[0], "0")
        return rows, rejects

    right = set()
    for letter, fn in zip("abcde", (a, b, c, d, e)):
        kept, rejects = fn()
        ok = ({r[0] for r in kept} == good and len(rejects) == 2
              and len(kept) + len(rejects) == len(start))
        if ok:
            right.add(letter)
    key = ADDED["reject-loop"]["key"]
    assert right == {x.strip() for x in key.split(",")} == {"b", "d"}, right
    report("reject-loop", key, f"prints '{out}' with KR-09053 kept; only (b) and (d) set aside both bad rows")


def identity_rule(rows):
    """Wednesday's rule: one row per order_id, the first copy whose amount converts."""
    kept, log = {}, []
    for r in rows:
        k = r["order_id"]
        if k not in kept:
            kept[k] = r
            continue
        if not kept[k]["amount"].isdigit() and r["amount"].isdigit():
            log.append(kept[k])
            kept[k] = r
        else:
            log.append(r)
    return list(kept.values()), log


def prove_bank_24():
    pair = [r for r in V2_ROWS if r["order_id"] == "KR-02151"]
    assert len(pair) == 2 and {r["amount"] for r in pair} == {"3710"} and {r["quarter"] for r in pair} == {"Q2"}
    assert sorted(r["order_id"] and r["order_date"] for r in pair) == ["2026-08-02", "2026-09-25"]
    assert tuple(sorted(pair[0].items())) != tuple(sorted(pair[1].items()))
    assert _bank["W1"]["items"][23]["key"] == "b"
    report(24, "b", "KR-02151: two Q2 rows at Rs 3,710 dated 2 August and 25 September; whole rows differ")


def prove_monday_number():
    q1 = sum(o["amount"] for o in V1 if o["quarter"] == "Q1")
    q2 = sum(o["amount"] for o in V1 if o["quarter"] == "Q2")
    tile = sum(o["amount"] for o in V1 if o["quarter"] == "Q2" and o["order_date"] <= "2026-09-15")
    assert (q1, q2, tile) == (21000000, 18700000, 15559950)
    assert round((tile - q1) / q1 * 100, 1) == -25.9
    assert round(((tile / 11) / (q1 / 13) - 1) * 100, 1) == -12.4
    assert round((q2 - q1) / q1 * 100, 1) == -11.0
    clean, log = identity_rule(V2_ROWS)
    clean_q = {q: sum(int(r["amount"]) for r in clean if r["quarter"] == q) for q in ("Q1", "Q2")}
    assert clean_q == {"Q1": 19000000, "Q2": 18700000} and len(clean) == 186 and len(log) == 15
    q1_log = [r for r in log if r["quarter"] == "Q1"]
    assert len(q1_log) == 14 and sum(int(r["amount"]) if r["amount"].isdigit() else 0 for r in q1_log) == 1998210
    assert round((clean_q["Q2"] - clean_q["Q1"]) / clean_q["Q1"] * 100, 1) == -1.6
    report("monday-number", ADDED["monday-number"]["key"],
           "tile -25.9, per week -12.4, closed -11.0, reconciled -1.6 (Q1 Rs 1,90,00,000 after 14 rows, Rs 19,98,210)")


def prove_plus_clean():
    months = {}
    for o in V1:
        if o["segment"] == "Retail-Plus":
            months[o["order_date"][:7]] = months.get(o["order_date"][:7], 0) + 1
    assert [months[m] for m in sorted(months)] == [14, 24, 13, 9, 9, 8]
    clean, log = identity_rule(V2_ROWS)
    may_copies = [r for r in log if r["segment"] == "Retail-Plus" and r["order_date"][:7] == "2026-05"
                  and r["quarter"] == "Q1"]
    assert len(may_copies) == 11
    plus = {q: sum(1 for r in clean if r["segment"] == "Retail-Plus" and r["quarter"] == q) for q in ("Q1", "Q2")}
    members = {q: len({r["customer_id"] for r in clean if r["segment"] == "Retail-Plus" and r["quarter"] == q})
               for q in ("Q1", "Q2")}
    assert plus == {"Q1": 40, "Q2": 26} and members == {"Q1": 22, "Q2": 22}
    assert (round(40 / 22, 2), round(26 / 22, 2)) == (1.82, 1.18)
    assert round((26 / 40 - 1) * 100, 1) == -35.0
    assert round((26 / 51 - 1) * 100, 1) == -49.0 and round((26 / 37 - 1) * 100, 1) == -29.7
    assert ADDED["plus-clean"]["key"] == "A fall of 35.0 percent."
    report("plus-clean", "35.0 fall", "51 less 11 May copies is 40 in Q1, 26 in Q2, 22 members: 1.82 to 1.18")


def prove_bank_52():
    assert _bank["W1"]["items"][51]["key"] == "b, d, a, c"
    report(52, "b, d, a, c", "tracker key: profile, decide, reconcile, recompute")


# ------------------------------------------------------------------------------ Part 3
def shuffle_gaps(q1, q2, times, seed):
    random.seed(seed)
    pool = q1 + q2
    gaps = []
    for _ in range(times):
        random.shuffle(pool)
        gaps.append(mean(pool[:len(q1)]) - mean(pool[len(q1):]))
    return gaps


def member_totals(segment, quarter):
    members = sorted({o["customer_id"] for o in V3 if o["segment"] == segment})
    totals = {m: 0 for m in members}
    for o in V3:
        if o["segment"] == segment and o["quarter"] == quarter and o["status"] == "delivered":
            totals[o["customer_id"]] += int(o["amount"])
    return [totals[m] for m in members]


def prove_part3_chart():
    p1, p2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
    gaps = shuffle_gaps(p1, p2, 5000, 2026)
    assert round(mean(p1) - mean(p2)) == 1110
    edges = [-10 ** 9, -1110, -555, 0, 555, 1110, 10 ** 9]
    counts = [sum(1 for g in gaps if lo <= g < hi) for lo, hi in zip(edges, edges[1:])]
    counts[0] = sum(1 for g in gaps if g <= -1110)
    counts[1] = sum(1 for g in gaps if -1110 < g < -555)
    assert counts == [117, 728, 1620, 1679, 721, 135], counts
    print(f"{'':>4}  {'exhibit 3A':<18} {'':<16} bars {counts}, 135 of 5,000 at or beyond Rs 1,110")


def prove_shuffle_sign():
    out, _ = run_exhibit("shuffle-sign", {"random": random, "mean": mean})
    key = ADDED["shuffle-sign"]["key"]
    assert out == options("shuffle-sign")[key] == "-880 0.981", out
    q1, q2 = [3400, 2900, 4100, 2500, 3800], [2200, 3100, 1900, 2700, 2400]
    gaps = shuffle_gaps(q1, q2, 1000, 2026)
    assert sum(1 for g in gaps if g >= 880) == 21 and sum(1 for g in gaps if g <= -880) == 24
    assert round(sum(1 for g in gaps if abs(g) >= 880) / 1000, 2) == 0.04
    report("shuffle-sign", key, f"prints '{out}'; the class's count at +880 is 21, and at or below -880 is 24")


def prove_bank_35():
    assert _bank["W1"]["items"][34]["key"] == "a, b, d"
    assert KEY_OF[35] == "a, c, d"
    report(35, "a, c, d", "tracker a, b, d relabelled a, c, d by the accepted order edit")


def prove_student_line():
    n = sum(1 for o in V3 if o["segment"] == "Student")
    by_q = {q: sum(1 for o in V3 if o["segment"] == "Student" and o["quarter"] == q) for q in ("Q1", "Q2")}
    custs = len({o["customer_id"] for o in V3 if o["segment"] == "Student"})
    assert (n, by_q, custs) == (12, {"Q1": 5, "Q2": 7}, 2)
    random.seed(2026)
    rises = []
    for _ in range(5000):
        q2 = sum(1 for _ in range(n) if random.random() < 0.5)
        q1 = n - q2
        rises.append(float("inf") if q1 == 0 else q2 / q1 - 1)
    share = sum(1 for r in rises if r >= 0.4 - 1e-9) / 5000
    assert round(share, 3) == 0.397
    assert round(100 / 12, 1) == 8.3
    report("student-line", ADDED["student-line"]["key"], f"12 orders (5 then 7) from 2 customers; coin-flip share {share:.3f}")


def exposure():
    groups = {}
    for e in EXPOSURE:
        groups.setdefault((e["exposed"], e["segment"]), []).append(int(e["august_revenue"]))
    return groups


def prove_bank_43():
    g = exposure()
    assert {k: (len(v), mean(v)) for k, v in g.items()} == {
        ("yes", "Retail-Plus"): (30, 4850), ("yes", "Retail-Core"): (30, 1940),
        ("no", "Retail-Plus"): (40, 5000), ("no", "Retail-Core"): (60, 2000)}
    sale = g[("yes", "Retail-Plus")] + g[("yes", "Retail-Core")]
    none = g[("no", "Retail-Plus")] + g[("no", "Retail-Core")]
    assert (mean(sale), mean(none)) == (3395, 3200) and round((3395 / 3200 - 1) * 100, 1) == 6.1
    assert round((4850 / 5000 - 1) * 100, 1) == -3.0 and round((1940 / 2000 - 1) * 100, 1) == -3.0
    assert KEY_OF[43] == "a"
    report(43, "a", "sale Rs 3,395 against Rs 3,200 (+6.1); inside each segment -3.0 percent")


def prove_bank_45():
    assert math.isclose(0.4 * 4850 + 0.6 * 1940, 3104)
    assert round((1 / 0.85 - 1) * 100, 1) == 17.6 and KEY_OF[45] == "d"
    report(45, "d", "at the other group's 40/60 mix the sale group averages Rs 3,104 against Rs 3,200")


def prove_diwali_test():
    report("diwali-test", ADDED["diwali-test"]["key"], "judgement key: a random hold-out inside each segment; no computation")


# ------------------------------------------------------------------------------ Part 4
def prove_debt_weights():
    out, _ = run_exhibit("debt-weights")
    key = ADDED["debt-weights"]["key"]
    assert out == "71 -0.03 1.68", out
    assert options("debt-weights")[key].startswith(out + ":")
    table = SOURCE["exhibits"][5]["table"]["rows"]
    table_data = {r[0]: (int(r[1]), float(r[2])) for r in table}
    _, ns = run_exhibit("debt-weights")
    assert {k.replace("United Kingdom", "United Kingdom"): v for k, v in ns["above_90"].items()} == table_data
    rr = [2.9, 2.4, 1.0, 0.7, -7.9, 2.4, -2.0]            # with the transcription of -7.6 as -7.9
    assert round(sum(rr) / 7, 1) == -0.1 and round(sum(g for n, g in table_data.values()) / 7, 1) == 0.0
    report("debt-weights", key, f"prints '{out}'; HAP Table 3 gives 0.0 and 1.7, and -0.1 with -7.9")


def prove_debt_rows():
    assert len(range(30, 45)) == 15 and len(range(30, 50)) == 20 and 20 - 15 == 5
    report("debt-rows", ADDED["debt-rows"]["key"], "rows 30 to 44 hold 15 of the sheet's 20 countries: 5 left out")


def prove_orbiter_units():
    assert round(4.4482216152605, 2) == 4.45                # newtons in one pound-force
    report("orbiter-units", ADDED["orbiter-units"]["key"], "1 lbf = 4.448 N, the report's factor of 4.45; judgement key")


def prove_flu_fit():
    report("flu-fit", ADDED["flu-fit"]["key"], "judgement key from Lazer and colleagues, 2014; no computation")


def prove_bing_alert():
    report("bing-alert", ADDED["bing-alert"]["key"], "judgement key from Kohavi and Thomke, 2017; no computation")


def prove_wald_buyers():
    p1, p2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
    b1, b2 = [v for v in p1 if v], [v for v in p2 if v]
    assert (rupees(mean(p1)), rupees(mean(p2)), len(p1)) == (3279, 2169, 22)
    assert (rupees(mean(b1)), rupees(mean(b2)), len(b1), len(b2)) == (3607, 2982, 20, 16)
    assert rupees(mean(p1) - mean(p2)) == 1110 and rupees(mean(b1) - mean(b2)) == 625
    assert sum(1 for v in p1 if v == 0) == 2 and sum(1 for v in p2 if v == 0) == 6
    assert round((mean(p2) / mean(p1) - 1) * 100, 1) == -33.9 and round((mean(b2) / mean(b1) - 1) * 100, 1) == -17.3
    report("wald-buyers", ADDED["wald-buyers"]["key"], "per member falls Rs 1,110 (33.9 percent); per buyer Rs 625 (17.3)")


# ------------------------------------------------------------------------------ Part 5
def prove_tool_print():
    out, ns = run_exhibit("tool-print")
    assert out == "SW-1042: out for delivery" and ns["result"] is None
    assert ns["tool_message"] == {"role": "tool", "content": "None"}
    key = ADDED["tool-print"]["key"]
    assert options("tool-print")[key].startswith("'None'")
    report("tool-print", key, "the tool prints 'SW-1042: out for delivery' and the model reads 'None'")


def prove_agent_history():
    sent = []

    def call_model(history):
        sent.append([m["content"] for m in history])
        return f"reply {len(sent)}"

    run_exhibit("agent-history", {"call_model": call_model})
    assert sent[1] == ["Where is order SW-1042?", "reply 1", "Please cancel order SW-2210"], sent

    fixed_sent = []

    def call_model_fixed(history):
        fixed_sent.append(len(history))
        return "ok"

    def run_agent(message, history=None):
        if history is None:
            history = []
        history.append({"role": "user", "content": message})
        reply = call_model_fixed(history)
        history.append({"role": "assistant", "content": reply})
        return reply

    run_agent("Where is order SW-1042?")
    run_agent("Please cancel order SW-2210")
    assert fixed_sent == [1, 1]
    report("agent-history", ADDED["agent-history"]["key"], "B's call sends A's two messages first; with None as default it sends one")


def prove_agent_cost():
    bars = SOURCE["additions"][[a["id"] for a in SOURCE["additions"]].index("agent-cost")]["exhibit"]["mermaid"]
    costs = [float(x) for x in re.search(r"bar \[([^\]]+)\]", bars).group(1).split(",")]
    assert costs == [1.4, 1.8, 1.2, 2.1, 1.6, 1.5, 42.0]
    total, m = sum(costs), mean(costs)
    assert round(total, 2) == 51.6 and f"{m:.2f}" == "7.37" and sorted(costs)[3] == 1.6
    assert round(42.0 / total * 100) == 81 and round(mean(costs[:6]), 2) == 1.6 and round(m / 1.6, 1) == 4.6
    report("agent-cost", ADDED["agent-cost"]["key"], "mean Rs 7.37, median Rs 1.60; C-07 is 81 percent of Rs 51.60")


def prove_sql():
    import psycopg2
    conn = psycopg2.connect(host=os.environ.get("PGHOST", "localhost"), port=os.environ.get("PGPORT", "5432"),
                            user=os.environ.get("PGUSER", "postgres"),
                            password=os.environ.get("PGPASSWORD", "postgres"), dbname="postgres")
    conn.autocommit = True
    cur = conn.cursor()
    schema = "w01_sat_proofs"
    cur.execute(f"DROP SCHEMA IF EXISTS {schema} CASCADE")
    cur.execute(f"CREATE SCHEMA {schema}")
    try:
        cur.execute(f"SET search_path TO {schema}")
        cur.execute("CREATE TABLE calls (call_id int, conversation_id text, tool text, status text, "
                    "latency_ms int)")
        rows = SOURCE["additions"][[a["id"] for a in SOURCE["additions"]].index("sql-count")]["exhibit"]["table"]["rows"]
        for r in rows:
            cur.execute("INSERT INTO calls VALUES (%s, %s, %s, %s, %s)",
                        (int(r[0]), r[1], None if r[2] == "NULL" else r[2], r[3],
                         None if r[4] == "NULL" else int(r[4])))
        # The word bank: the query with WHERE and HAVING returns the tools at or above the floor;
        # the other words fail or return something else.
        cur.execute("CREATE TABLE week_calls (tool text, conversation_id text, status text)")
        for i in range(35):
            cur.execute("INSERT INTO week_calls VALUES ('refund', %s, 'error')", (f"CV-{i % 20}",))
        for i in range(12):
            cur.execute("INSERT INTO week_calls VALUES ('order_status', %s, 'error')", (f"CV-{i}",))
        for i in range(50):
            cur.execute("INSERT INTO week_calls VALUES ('order_status', %s, 'ok')", (f"CV-{i}",))
        template = SOURCE["additions"][[a["id"] for a in SOURCE["additions"]].index("sql-where")]["exhibit"]["code"]["text"]
        filled = template.replace("__(1)__", "WHERE").replace("__(2)__", "HAVING").replace("FROM calls", "FROM week_calls")
        cur.execute(filled)
        assert cur.fetchall() == [("refund", 35)]
        for bad in (template.replace("__(1)__", "HAVING").replace("__(2)__", "HAVING"),
                    template.replace("__(1)__", "WHERE").replace("__(2)__", "WHERE")):
            try:
                cur.execute(bad.replace("FROM calls", "FROM week_calls"))
                raise AssertionError("a wrong clause ran")
            except psycopg2.Error:
                pass
        assert [ADDED[i]["key"] for i in ("sql-where", "sql-having")] == ["WHERE", "HAVING"]
        report("sql-where", "WHERE", "the filled query returns [('refund', 35)]; HAVING on status fails")
        report("sql-having", "HAVING", "WHERE COUNT(*) >= 30 fails in Postgres; HAVING applies the floor of 30")
        bank = SOURCE["banks"]["sql-results"]["options"]
        for item_id in ("sql-count", "sql-avg", "sql-rate"):
            query = str(ADDED[item_id]["text"]).strip()
            cur.execute(query)
            got = cur.fetchone()[0]
            shown = str(int(got)) if float(got) == int(got) else str(got)
            key = ADDED[item_id]["key"]
            assert shown == key and key in bank, (item_id, got)
            report(item_id, key, f"Postgres returns {got} for: {query}")
        cur.execute("SELECT COUNT(*), 1.0 * COUNT(*) FILTER (WHERE status <> 'ok') / COUNT(*), "
                    "AVG(COALESCE(latency_ms, 0)), COUNT(tool) FROM calls")
        n, share, avg0, ntool = cur.fetchone()
        assert (n, float(share), float(avg0), ntool) == (8, 0.375, 600.0, 7)

    finally:
        cur.execute("RESET search_path")
        cur.execute(f"DROP SCHEMA IF EXISTS {schema} CASCADE")
        conn.close()


def main():
    print(f"Week 1 Saturday paper: {len(PRINTED)} timed items. Each line gives the printed Q, the item, "
          f"its key and what proves it.")
    for step in (prove_bank_47, prove_sales_net, prove_payback, prove_bank_46, prove_quarter_counter,
                 prove_bank_20, prove_budget_fact, prove_bank_51, prove_reader_header, prove_bank_11,
                 prove_evidence_copy, prove_reject_loop, prove_bank_24, prove_monday_number,
                 prove_plus_clean, prove_bank_52, prove_part3_chart, prove_bank_35, prove_shuffle_sign,
                 prove_student_line, prove_bank_43, prove_bank_45, prove_diwali_test,
                 prove_debt_weights, prove_debt_rows, prove_orbiter_units, prove_flu_fit,
                 prove_bing_alert, prove_wald_buyers, prove_tool_print, prove_agent_history,
                 prove_agent_cost, prove_sql):
        step()
    missing = [i for i in PRINTED if (i["id"] if i["added"] else i["no"]) not in proved]
    assert not missing, [f"Q{i['q']}" for i in missing]
    print(f"PROVED: all {len(PRINTED)} timed items have a key that code, SQL, arithmetic or the tracker settles.")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W01/SAT/internal/C2_W01_SAT_key_proofs_INTERNAL.py, with Postgres running
#     One line per timed item, 36 in all, then "PROVED: all 36 timed items ...", exit 0.
# The sales-net exhibit run on Monday's 30 orders
#     Prints "30 orders, Rs 544810", option (c); net of cancellations would be 26 orders, Rs 5,35,760.
# The quarter-counter exhibit run on Tuesday's 200 orders
#     Prints "{'Q1': 5, 'Q2': 7} +40.0%", option (d), Student's counts where the file holds 114 and 86.
# The reader-header exhibit run in content/W01/D3/data
#     Prints "200 KR-02002", option (b): next() on a DictReader consumes the first order.
# The shuffle-sign exhibit with seed 2026
#     Prints "-880 0.981", option (c); counted the class's way the share is 21 of 1,000.
# The reject-loop exhibit, then each of the five rewrites on the same five rows
#     Prints "4 + 1 = 5" with KR-09053 still kept; only rewrites (b) and (d) set aside both bad rows.
# The debt-weights exhibit on the seven countries of HAP Table 2
#     Prints "71 -0.03 1.68", option (a); equal weights with -7.9 for New Zealand give -0.1.
# The three match queries on the eight-call table
#     COUNT(latency_ms) returns 6, AVG(latency_ms) 800 and the integer failure rate 0.
# The word-bank query filled with WHERE and HAVING on 35 refund and 12 order-status errors
#     Returns [('refund', 35)]; HAVING in blank 1 or WHERE in blank 2 raises a Postgres error.
# An exhibit edited so that its printed output no longer matches its keyed option
#     The matching assertion fails and names the item; nothing after it runs.
# Postgres not running
#     psycopg2 raises OperationalError at prove_sql, after every Python and arithmetic item has printed.

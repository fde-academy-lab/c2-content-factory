"""Prove every key on the Week 1 Saturday paper that code, SQL or arithmetic can decide.

    python3 content/W01/SAT/internal/C2_W01_SAT_key_proofs_INTERNAL.py

Runs cold from the repository root or from anywhere inside it. Each code exhibit is read from the
week's source file and executed exactly as it prints, on the week's own data files where the item
names them, and its output is checked against the option the key names. Each SQL item runs against
the local Postgres (PGHOST, PGPORT, PGUSER and PGPASSWORD, defaulting to localhost, 5432 and
postgres) in a scratch schema created at the start and dropped at the end. Each arithmetic key is
recomputed from the numbers on the page and from the data behind them, and each table an item
reads is checked against that data. One line prints per item, and the run ends on the count of
items proved; any failed assertion stops it with the item's name.
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
import shutil
import sys
import tempfile
from decimal import ROUND_HALF_UP, Decimal

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
V1 = load_orders(D2 / "C2_W01_D02_orders_STUDENT.py")         # Tuesday, 200 rows
V2_ROWS = list(csv.DictReader(open(D3 / "C2_W01_D03_orders_STUDENT.csv", encoding="utf-8")))
V3 = list(csv.DictReader(open(D4 / "C2_W01_D04_orders_STUDENT.csv", encoding="utf-8")))

# The tracker's keys as the bank holds them, before any edit is laid on them.
_bank = builder.read_bank()
# Printed Q numbers, stems and keys, after the ledger's edits, so each line names the item as the
# room sees it.
_laid = builder.read_bank()
builder.apply_edits(_laid, yaml.safe_load((ROOT / "data/programme/paper_edits.yaml").read_text()))
PRINTED = builder.assemble(_laid["W1"], SOURCE)
Q_OF = {(i["id"] if i["added"] else i["no"]): i["q"] for i in PRINTED}
KEY_OF = {(i["id"] if i["added"] else i["no"]): i["key"] for i in PRINTED}
TEXT_OF = {(i["id"] if i["added"] else i["no"]): i["text"] for i in PRINTED}
proved = []


def report(ref, key, detail):
    q = Q_OF.get(ref)
    name = f"Q{q}" if q else "--"
    label = ref if isinstance(ref, str) else f"bank {ref}"
    print(f"{name:>4}  {label:<16} key {key:<12} {detail}")
    proved.append(ref)


def options(item_id):
    """{letter: text} of an addition's printed options."""
    out = {}
    for line in str(ADDED[item_id]["text"]).splitlines():
        m = re.match(r"^\(([a-f])\)\s*(.+)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2)
    return out


def table(item_id=None, set_no=None, part=None):
    """The rows of an addition's, a set's or a part's exhibit table."""
    if item_id:
        return ADDED[item_id]["exhibit"]["table"]["rows"]
    if set_no:
        return SOURCE["exhibits"][set_no]["table"]["rows"]
    return SOURCE["parts"][part - 1]["exhibits"][0]["table"]["rows"]


def num(text):
    """A number as the paper prints it, commas and all."""
    return float(str(text).replace(",", ""))


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
    return int(Decimal(repr(x)).quantize(Decimal(1), rounding=ROUND_HALF_UP))


def pct(x):
    """A percentage to one decimal place, halves rounded away from zero, as the paper prints it."""
    return float(Decimal(repr(x * 100)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


# ------------------------------------------------------------------------------ Part 1
def prove_bank_50():
    customers, frequency, items, price, discounts = 50000, 2, 3, 400, 1_00_00_000
    before = customers * frequency * items * price
    assert before == 12_00_00_000 and before - discounts == 11_00_00_000          # Rs 12 crore, Rs 11 crore
    assert customers * frequency * price - discounts == 3_00_00_000               # items left out
    assert _bank["W1"]["items"][49]["key"] == KEY_OF[50] == "Rs 11 crore (Rs 12 crore before discounts)."
    report(50, "Rs 11 crore", "50,000 x 2 x 3 x Rs 400 is Rs 12 crore; less Rs 1 crore of discounts")


def status_table():
    status = {}
    for o in V0:
        n, rs = status.get(o["status"], (0, 0))
        status[o["status"]] = (n + 1, rs + int(o["amount"]))
    return status


def prove_sales_net():
    consumer = [o for o in V0 if o["segment"] != "Business"]
    assert len(consumer) == 29 and len(V0) - len(consumer) == 1
    out, _ = run_exhibit("sales-net", {"CONSUMER_ORDERS": consumer})
    assert out == "{'app': 18600, 'web': 27290, 'store': 18920}", out
    cells = {}
    for o in consumer:
        n, rs = cells.get((o["channel"], o["status"]), (0, 0))
        cells[(o["channel"], o["status"])] = (n + 1, rs + int(o["amount"]))
    for channel, *by_status in table("sales-net"):
        for status, cell in zip(("delivered", "returned", "cancelled"), by_status):
            want = cells.get((channel, status))
            shown = None if cell == "none" else tuple(int(num(x)) for x in
                                                      re.match(r"(\d+) orders?, Rs ([\d,]+)", cell).groups())
            assert shown == want, (channel, status, cell, want)
    stood = {ch: sum(int(o["amount"]) for o in consumer if o["channel"] == ch and o["status"] != "cancelled")
             for ch in ("app", "web", "store")}
    assert stood == {"app": 18600, "web": 27290, "store": 9870}
    assert stood["app"] > stood["store"] and 18920 > stood["app"]      # the printed store figure flips it
    key = ADDED["sales-net"]["key"]
    opts = options("sales-net")
    assert opts[key] == f"{out}; her rule backs the app."
    assert opts["a"] == f"{out}; her rule backs the store."
    report("sales-net", key, f"prints {out}; on orders not cancelled the app's Rs 18,600 beats the store's Rs 9,870")


def prove_first_order():
    by = {s: sorted(int(o["amount"]) for o in V0 if o["status"] == s) for s in ("delivered", "returned", "cancelled")}
    shown, places = {}, {}
    for status, span, amounts in table("first-order"):
        values = [int(num(x)) for x in amounts.split(", ")]
        lo, hi = (int(x) for x in span.split(" to "))
        assert hi - lo + 1 == len(values) and lo == len(shown.get(status, [])) + 1
        shown.setdefault(status, []).extend(values)
    assert shown == by and {k: len(v) for k, v in shown.items()} == {"delivered": 21, "returned": 5, "cancelled": 4}
    d = by["delivered"]
    assert d[10] == 2060 and len(d) == 21 and ADDED["first-order"]["key"] == "Rs 2,060."
    everything = sorted(d + by["returned"] + by["cancelled"])
    assert rupees(mean(everything)) == 18160 and (everything[14] + everything[15]) / 2 == 2205
    assert rupees(mean(d)) == 24800 and round(480000 / sum(d) * 100) == 92 and round(24800 / 2060) == 12
    paid_or_refunded = sorted(d + by["returned"])
    assert (paid_or_refunded[12] + paid_or_refunded[13]) / 2 == 2100
    assert (d[9] + d[10]) / 2 == 2040 and d[11] == 2090          # the bulk order deleted; one place late
    zeros = sorted(d + [0] * (len(by["returned"]) + len(by["cancelled"])))
    assert (zeros[14] + zeros[15]) / 2 == 1480                     # cancelled and returned counted as zero
    stem = ADDED["first-order"]["text"]
    assert "business buyers included" in stem and "their own rates" in stem and "stays paid for" not in stem
    report("first-order", "Rs 2,060", "median of the 21 delivered orders, the 11th; mean 24,800, all-30 median 2,205")


def prove_quarter_counter():
    out, _ = run_exhibit("quarter-counter", {"ORDERS": V1})
    key = ADDED["quarter-counter"]["key"]
    assert out == options("quarter-counter")[key] == "{'Q1': 38, 'Q2': 36} -5.3%", out
    by = {}
    for o in V1:
        by[(o["quarter"], o["segment"])] = by.get((o["quarter"], o["segment"]), 0) + 1
    rows = [(r[0], int(r[1]), int(r[2])) for r in table("quarter-counter")]
    order = ["Student", "Retail-Plus", "Business", "Retail-Core"]
    assert [r[0] for r in rows[:4]] == order and f"SEGMENTS = {order}".replace("'", '"') in \
        ADDED["quarter-counter"]["exhibit"]["code"]["text"]
    for seg, n1, n2 in rows[:4]:
        assert (n1, n2) == (by[("Q1", seg)], by[("Q2", seg)])
    assert rows[4] == ("all", 114, 86) and len(V1) == 200
    once = ADDED["quarter-counter"]["exhibit"]["code"]["text"].replace(
        "orders_in = {}\n", "orders_in = {}\nn = 0\n").replace("        n = 0\n", "")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(once, "counter-once", "exec"), {"ORDERS": V1})
    assert buf.getvalue().strip() == options("quarter-counter")["c"] == "{'Q1': 114, 'Q2': 200} +75.4%"
    assert options("quarter-counter")["a"] == "{'Q1': 114, 'Q2': 86} -24.6%"
    report("quarter-counter", key, f"prints '{out}': the counter holds Retail-Core's count; the file says 114 and 86")


def prove_bank_20():
    assert _bank["W1"]["items"][19]["key"] == KEY_OF[20] == "a"
    report(20, "a", "tracker key: the first rung is confirming the drop is real")


def prove_budget_flip():
    ids = {q: {o["customer_id"] for o in V1 if o["quarter"] == q} for q in ("Q1", "Q2")}
    orders = {q: sum(1 for o in V1 if o["quarter"] == q) for q in ("Q1", "Q2")}
    assert len(ids["Q1"]) == len(ids["Q2"]) == 69
    assert (round(orders["Q1"] / 69, 2), round(orders["Q2"] / 69, 2)) == (1.65, 1.25)
    members = {q: {o["customer_id"] for o in V1 if o["quarter"] == q and o["segment"] == "Retail-Plus"}
               for q in ("Q1", "Q2")}
    assert len(members["Q1"]) == len(members["Q2"]) == 22        # nobody lapsed: members buy less often
    est = {r[0]: (num(r[1].replace("Rs ", "")), num(r[2].replace("Rs ", ""))) for r in table("budget-flip")}
    new, back = est["A new customer won"], est["A member brought back to Q1's buying"]
    ratio = lambda cost_rev: cost_rev[1] / cost_rev[0]
    assert (ratio(new), ratio(back)) == (2.0, 2.5)
    changes = {"a": ((new[0], 2800), back), "b": ((1000, new[1]), back),
               "c": (new, (800, back[1])), "d": (new, (back[0], 1300))}
    flips = {k for k, (n, b) in changes.items() if ratio(n) > ratio(b)}
    key = ADDED["budget-flip"]["key"]
    assert flips == {key} == {"c"}, flips
    assert [round(ratio(changes[k][0 if k in "ab" else 1]), 2) for k in "abcd"] == [2.33, 2.4, 1.88, 2.17]
    assert back[1] / ratio(new) == 750
    report("budget-flip", key, "Rs 2.00 a rupee against Rs 2.50; only a Rs 800 route back, Rs 1.88, flips it")


def prove_bank_51():
    assert _bank["W1"]["items"][50]["key"] == KEY_OF[51] == "b, d, e, a, c"
    assert "Confirm that the drop is real" in TEXT_OF[20] and "Confirm that the drop is real" not in TEXT_OF[51]
    assert "(b) Check each quarter's figure on its own" in TEXT_OF[51]
    assert "(d) Set the two checked figures side by side" in TEXT_OF[51]
    report(51, "b, d, e, a, c", "tracker key: checked, like with like, decompose, isolate, hypothesise")


# ------------------------------------------------------------------------------ Part 2
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


def prove_reader_header():
    with tempfile.TemporaryDirectory() as tmp:            # the file as the stem names it
        shutil.copy(D3 / "C2_W01_D03_orders_STUDENT.csv", pathlib.Path(tmp) / "orders.csv")
        out, ns = run_exhibit("reader-header", cwd=tmp)
    key = ADDED["reader-header"]["key"]
    assert out == "200 KR-02002", out
    assert len(V2_ROWS) == 201 and [r["order_id"] for r in V2_ROWS[:2]] == ["KR-02001", "KR-02002"]
    clean, log = identity_rule(ns["rows"])
    assert (len(ns["rows"]), len(clean), len(log)) == (200, 185, 15)     # the pass's own report closes
    assert all(r["order_id"] != "KR-02001" for r in clean + log)
    opts = options("reader-header")
    assert opts[key].startswith(out + "; only a count of the file's own rows")
    assert opts["b"].startswith(out + "; the pass's own report")
    report("reader-header", key, f"prints '{out}'; the pass closes 200 = 185 + 15 and KR-02001 is in neither")


def prove_text_compare():
    assert ("4500" < "30000") is False and ("9" > "10000") is True
    v0_text = [o for o in V0 if isinstance(o["amount"], str)]
    assert [(o["order_id"], o["amount"]) for o in v0_text] == [("KR-01008", "4500")]
    assert all(isinstance(r["amount"], str) for r in V2_ROWS)
    key = ADDED["text-compare"]["key"]
    assert options("text-compare")[key].startswith("False, because text compares character by character")
    report("text-compare", key, "'4500' < '30000' is False, silently; every CSV amount is text")


def prove_evidence_copy():
    out, ns = run_exhibit("evidence-copy")
    assert out == "2 + 0 = 2 []", out
    assert ns["as_arrived"][0] is ns["rows"][0] and ns["as_arrived"][0]["amount"] == 0
    code = ADDED["evidence-copy"]["exhibit"]["code"]["text"]
    deep_code = code.replace("rows.copy()", "[dict(r) for r in rows]")
    assert deep_code != code
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(deep_code, "evidence-deep", "exec"), {})
    assert buf.getvalue().strip() == "2 + 1 = 2 ['KR-02063']"
    csv_rows = [(r["order_id"], r["amount"]) for r in V2_ROWS if r["order_id"] in ("KR-02063", "KR-02064")]
    assert ("KR-02063", "twelve") in csv_rows and ("KR-02064", "3150") in csv_rows
    books = {r["order_id"]: int(r["amount"]) for r in identity_rule(V2_ROWS)[0]
             if r["order_id"] in ("KR-02063", "KR-02064")}
    assert books == {"KR-02063": 1790, "KR-02064": 3150}
    assert sum(r["amount"] for r in ns["rows"]) == 3150 < sum(books.values()) == 4940
    key = ADDED["evidence-copy"]["key"]
    opts = options("evidence-copy")
    assert opts[key].startswith(out + "; only a rupee total") and opts["b"].startswith("2 + 1 = 2")
    report("evidence-copy", key, f"prints '{out}'; with copies of the dictionaries it prints 2 + 1 = 2; "
                                 f"rupees 3,150 against 4,940")


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


def prove_dup_rule():
    fields = ("order_id", "customer_id", "order_date", "amount", "quarter")
    shown = [dict(zip(fields, (r[1], r[2], r[3], r[4].replace(",", ""), r[5]))) for r in table("dup-rule")]
    full = []
    for s in shown:                                     # each printed row is a row of the export, in order
        match = [i for i, v in enumerate(V2_ROWS) if all(v[f] == s[f] for f in fields)]
        assert match, s
        full.append(match)
    lines = [m[0] if len(m) == 1 else None for m in full]
    # the two exact copies of KR-02006 match both lines; assign them in file order
    kr02006 = [i for i, v in enumerate(V2_ROWS) if v["order_id"] == "KR-02006"]
    k = iter(kr02006)
    lines = [next(k) if ln is None else ln for ln in lines]
    assert lines == sorted(lines) and len(set(lines)) == 7
    rows = [V2_ROWS[i] for i in lines]
    for oid in {r["order_id"] for r in rows}:          # the unshown columns match within an order_id
        rs = [r for r in rows if r["order_id"] == oid]
        for f in ("segment", "channel", "city", "status", "discount"):
            assert len({r[f] for r in rs}) == 1, (oid, f)

    def totals(kept):
        return {q: sum(int(r["amount"]) for r in kept if r["quarter"] == q and r["amount"].isdigit())
                for q in ("Q1", "Q2")}

    kept, log = identity_rule(rows)
    whole = []
    for r in rows:
        if r not in whole:
            whole.append(r)
    first = list({r["order_id"]: r for r in reversed(rows)}.values())      # the first copy of each
    assert len(rows) - len(whole) == 1                                     # the whole-row check finds one
    assert totals(kept) == {"Q1": 4680, "Q2": 7410} and len(log) == 3
    assert totals(whole) == {"Q1": 4680, "Q2": 11120}
    assert totals(first) == {"Q1": 2890, "Q2": 7410}
    assert totals(rows) == {"Q1": 7570, "Q2": 11120}
    assert ADDED["dup-rule"]["key"] == "Q1 Rs 4,680 and Q2 Rs 7,410."
    report("dup-rule", "4,680; 7,410", "one row per order_id, the copy that converts; whole rows leave Q2 at "
                                       "Rs 11,120, first copies leave Q1 at Rs 2,890")


def prove_monday_number():
    q1 = sum(o["amount"] for o in V1 if o["quarter"] == "Q1")
    q2 = sum(o["amount"] for o in V1 if o["quarter"] == "Q2")
    tile = sum(o["amount"] for o in V1 if o["quarter"] == "Q2" and o["order_date"] <= "2026-09-15")
    assert (q1, q2, tile) == (21000000, 18700000, 15559950)
    assert pct((tile - q1) / q1) == -25.9 and pct((tile / 11) / (q1 / 13) - 1) == -12.4
    assert pct((q2 - q1) / q1) == -11.0
    seen, copies = set(), 0
    for o in V1:
        if o["quarter"] == "Q1" and o["order_id"] in seen:
            copies += o["amount"]
        seen.add(o["order_id"])
    assert copies == 2000000
    clean, log = identity_rule(V2_ROWS)
    clean_q = {q: sum(int(r["amount"]) for r in clean if r["quarter"] == q) for q in ("Q1", "Q2")}
    assert clean_q == {"Q1": q1 - copies, "Q2": q2} == {"Q1": 19000000, "Q2": 18700000}
    assert sum(1 for r in log if r["quarter"] == "Q1") == 14
    assert pct((clean_q["Q2"] - clean_q["Q1"]) / clean_q["Q1"]) == -1.6 and pct((1.9 - 2.1) / 2.1) == -9.5
    assert ADDED["monday-number"]["key"].startswith("A fall of 1.6 percent")
    assert "found Tuesday's Q2 clean at Rs 1,87,00,000" in ADDED["monday-number"]["text"]
    report("monday-number", "1.6 fall", "tile -25.9, weekly -12.4, closed -11.0; Q1 less Rs 20,00,000 of copies gives -1.6")


def prove_plus_clean():
    months = {}
    for o in V1:
        if o["segment"] == "Retail-Plus":
            months[o["order_date"][:7]] = months.get(o["order_date"][:7], 0) + 1
    bars = [months[m] for m in sorted(months)]
    assert bars == [14, 24, 13, 9, 9, 8] == [int(x) for x in table(set_no=4)[0][1:]]
    assert f"bar {bars}".replace(" ", "") in SOURCE["exhibits"][4]["mermaid"].replace(" ", "")
    clean, log = identity_rule(V2_ROWS)
    may_copies = [r for r in log if r["segment"] == "Retail-Plus" and r["order_date"][:7] == "2026-05"
                  and r["quarter"] == "Q1"]
    assert len(may_copies) == 11 and sum(1 for r in log if r["quarter"] == "Q1") == 14
    count = lambda rows, q, seg=None: sum(1 for r in rows if r["quarter"] == q and (seg is None or r["segment"] == seg))
    plus = {q: count(clean, q, "Retail-Plus") for q in ("Q1", "Q2")}
    members = {q: len({r["customer_id"] for r in clean if r["segment"] == "Retail-Plus" and r["quarter"] == q})
               for q in ("Q1", "Q2")}
    assert plus == {"Q1": 40, "Q2": 26} and members == {"Q1": 22, "Q2": 22}
    assert (round(40 / 22, 2), round(26 / 22, 2)) == (1.82, 1.18)
    assert pct(26 / 40 - 1) == -35.0 and pct(26 / 51 - 1) == -49.0
    company = {q: count(clean, q) for q in ("Q1", "Q2")}
    exported = {q: count(V1, q) for q in ("Q1", "Q2")}
    assert company == {"Q1": 100, "Q2": 86} and exported == {"Q1": 114, "Q2": 86}
    assert plus["Q1"] - plus["Q2"] == company["Q1"] - company["Q2"] == 14      # the tier carries all of it
    assert count(V1, "Q1", "Retail-Plus") - count(V1, "Q2", "Retail-Plus") == 25 and 114 - 86 == 28
    key = ADDED["plus-clean"]["key"]
    assert options("plus-clean")[key] == ("Orders per member fall 35.0 percent, and Retail-Plus carries all 14 "
                                          "of the company's 14 lost orders.")
    report("plus-clean", key, "Retail-Plus 40 to 26 over 22 members is -35.0; the company falls 100 to 86, "
                              "all 14 in Retail-Plus")


def prove_bank_52():
    assert _bank["W1"]["items"][51]["key"] == KEY_OF[52] == "b, d, a, c"
    assert "(c) Recompute the revenue tree on the clean data, and send it to Anand." in TEXT_OF[52]
    assert "nothing is computed from the clean file" not in TEXT_OF[52]
    report(52, "b, d, a, c", "tracker key: profile, decide, reconcile, recompute and send")


# ------------------------------------------------------------------------------ Part 3
def member_totals(segment, quarter):
    members = sorted({o["customer_id"] for o in V3 if o["segment"] == segment})
    totals = {m: 0 for m in members}
    for o in V3:
        if o["segment"] == segment and o["quarter"] == quarter and o["status"] == "delivered":
            totals[o["customer_id"]] += int(o["amount"])
    return [totals[m] for m in members]


def flip_gaps(q1, q2, times, seed):
    """Kavya's paired shuffle: each member keeps both quarters, and a coin decides whether they swap."""
    random.seed(seed)
    diffs = [a - b for a, b in zip(q1, q2)]
    return [rupees(sum(x if random.random() < 0.5 else -x for x in diffs) / len(diffs))
            for _ in range(times)]


def prove_plus_real():
    p1, p2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
    assert len(p1) == 22 and rupees(mean(p1) - mean(p2)) == 1110
    gaps = flip_gaps(p1, p2, 5000, 2026)
    bins = [sum(1 for g in gaps if g <= -1110), sum(1 for g in gaps if -1109 <= g <= -555),
            sum(1 for g in gaps if -554 <= g <= -1), sum(1 for g in gaps if 0 <= g <= 554),
            sum(1 for g in gaps if 555 <= g <= 1109), sum(1 for g in gaps if g >= 1110)]
    assert bins == [141, 766, 1526, 1683, 739, 145], bins
    assert [int(num(r[1])) for r in table(part=3)] == bins
    assert f"bar {bins}".replace(" ", "") in SOURCE["parts"][2]["exhibits"][0]["mermaid"].replace(" ", "")
    assert (145 / 5000, (145 + 141) / 5000, round((739 + 145) / 5000, 3)) == (0.029, 0.0572, 0.177)
    assert 22 * 1110 == 24420 and round(24420 / 12864680 * 100, 2) == 0.19
    delivered_q2 = sum(int(o["amount"]) for o in V3 if o["quarter"] == "Q2" and o["status"] == "delivered")
    assert delivered_q2 == 12864680
    key = ADDED["plus-real"]["key"]
    opts = options("plus-real")
    assert opts[key].startswith("Real: 145 of 5,000") and opts[key].endswith("Rs 24,420 a quarter across the tier.")
    assert sum(1 for t in opts.values() if t.startswith("Real: 145")) == 2
    assert "shows a fall at least as large as the real one" in ADDED["plus-real"]["text"]
    report("plus-real", key, f"paired shuffle bars {bins}; 145 of 5,000 reach the fall, 0.029; both ways 0.057")


def prove_wald_kalpa():
    p1, p2 = member_totals("Retail-Plus", "Q1"), member_totals("Retail-Plus", "Q2")
    b1, b2 = [v for v in p1 if v], [v for v in p2 if v]
    assert (rupees(mean(p1)), rupees(mean(p2)), len(p1)) == (3279, 2169, 22)
    assert (rupees(mean(b1)), rupees(mean(b2)), len(b1), len(b2)) == (3607, 2982, 20, 16)
    assert rupees(mean(p1) - mean(p2)) == 1110 and rupees(mean(b1) - mean(b2)) == 625
    assert pct(mean(p2) / mean(p1) - 1) == -33.9 and pct(mean(b2) / mean(b1) - 1) == -17.3
    assert (sum(1 for a in p1 if not a), sum(1 for b in p2 if not b)) == (2, 6)
    assert sum(1 for a, b in zip(p1, p2) if not a and not b) == 0
    key = ADDED["wald-kalpa"]["key"]
    assert options("wald-kalpa")[key].startswith("False: per buyer it falls a sixth and per member a third; "
                                                  "6 members had nothing delivered in Q2, against 2 in Q1")
    report("wald-kalpa", key, "per member falls Rs 1,110 (33.9 percent); per buyer Rs 625 (17.3); bases 22, "
                              "then 20 and 16")


def shuffle_gaps(q1, q2, times, seed):
    random.seed(seed)
    pool = q1 + q2
    gaps = []
    for _ in range(times):
        random.shuffle(pool)
        gaps.append(mean(pool[:len(q1)]) - mean(pool[len(q1):]))
    return gaps


def prove_bank_35():
    assert _bank["W1"]["items"][34]["key"] == "a, b, d"
    assert KEY_OF[35] == "a, c, d"
    report(35, "a, c, d", "tracker a, b, d relabelled a, c, d by the accepted order edit")


def prove_shuffle_sign():
    out, _ = run_exhibit("shuffle-sign", {"random": random, "mean": mean})
    key = ADDED["shuffle-sign"]["key"]
    assert out == "-880 0.981", out
    assert options("shuffle-sign")[key] == f"{out}; the note still calls the fall real."
    q1, q2 = [3400, 2900, 4100, 2500, 3800], [2200, 3100, 1900, 2700, 2400]
    gaps = shuffle_gaps(q1, q2, 1000, 2026)
    assert sum(1 for g in gaps if g >= 880) == 21 and sum(1 for g in gaps if g <= -880) == 24
    assert round(sum(1 for g in gaps if abs(g) >= 880) / 1000, 2) == 0.04 and 21 / 1000 < 0.05
    report("shuffle-sign", key, f"prints '{out}'; the class's count at +880 is 21 of 1,000, under 0.05, so the "
                                f"call stays real")


def prove_student_line():
    st = [o for o in V3 if o["segment"] == "Student"]
    by_q = {q: sum(1 for o in st if o["quarter"] == q) for q in ("Q1", "Q2")}
    assert (len(st), by_q, len({o["customer_id"] for o in st})) == (12, {"Q1": 5, "Q2": 7}, 2)
    random.seed(2026)
    q2s = [sum(1 for _ in range(12) if random.random() < 0.5) for _ in range(5000)]
    rows = [sum(1 for k in q2s if k <= 4)] + [q2s.count(k) for k in (5, 6, 7, 8)] + [sum(1 for k in q2s if k >= 9)]
    assert rows == [918, 964, 1133, 1034, 595, 356] == [int(num(r[1])) for r in table("student-line")]
    rise40 = sum(1 for k in q2s if k == 12 or k / (12 - k) - 1 >= 0.4 - 1e-9)
    assert rise40 == sum(1 for k in q2s if k >= 7) == 1985 and round(1985 / 5000, 3) == 0.397
    assert sum(1 for k in q2s if k >= 8) == 951 and q2s.count(7) == 1034
    key = ADDED["student-line"]["key"]
    assert "1,985 of 5,000" in options("student-line")[key] and "a lead" in options("student-line")[key]
    report("student-line", key, "12 orders (5 then 7) from 2 customers; 7 or more in Q2 in 1,985 of 5,000 worlds")


def prove_diwali_test():
    opts = options("diwali-test")
    key = ADDED["diwali-test"]["key"]
    assert "random tenth of each segment" in opts[key] and "spend per customer" in opts[key]
    assert sum("random tenth of each segment" in t for t in opts.values()) == 2
    assert sum("spend per customer" in t for t in opts.values()) == 2
    report("diwali-test", key, "judgement key: a random hold-back inside each segment, compared per customer")


# ------------------------------------------------------------------------------ Part 4
def prove_debt_weights():
    out, ns = run_exhibit("debt-weights")
    key = ADDED["debt-weights"]["key"]
    assert out == "71 -0.07 1.68", out
    assert options("debt-weights")[key] == f"{out}; New Zealand's single year carries a seventh of that weight."
    table_data = {r[0]: (int(r[1]), float(r[2])) for r in table(set_no=5)}
    assert ns["above_90"] == table_data
    growth = [g for n, g in table_data.values()]
    assert round(sum(growth) / 7, 1) == -0.1                  # the published -0.1, with New Zealand at -7.9
    with_nz_as_sheet = [g if g != -7.9 else -7.6 for g in growth]
    assert round(sum(with_nz_as_sheet) / 7, 1) == 0.0        # HAP Table 3 without the transcription
    assert round(sum(n * g for n, g in table_data.values()) / 71, 1) == 1.7
    assert len(table_data) == 7 and sum(n for n, g in table_data.values()) == 71     # a seventh against a 71st
    assert "PERI Working Paper 322, April 2013" in SOURCE["exhibits"][5]["caption"]
    report("debt-weights", key, f"prints '{out}'; -0.07 rounds to the published -0.1; HAP Table 3 gives 1.7")


def prove_debt_rows():
    assert len(range(30, 45)) == 15 and len(range(30, 50)) == 20 and 20 - 15 == 5
    report("debt-rows", ADDED["debt-rows"]["key"], "the formula spans rows 30 to 44, 15 of the sheet's 20 country rows")


def prove_orbiter_units():
    assert round(4.4482216152605, 2) == 4.45                # newtons in one pound-force
    report("orbiter-units", ADDED["orbiter-units"]["key"], "1 lbf = 4.448 N, the report's factor of 4.45; judgement key")


def prove_flu_fit():
    report("flu-fit", ADDED["flu-fit"]["key"], "judgement key from Lazer and colleagues, 2014; no computation")


def prove_bing_alert():
    report("bing-alert", ADDED["bing-alert"]["key"], "judgement key from Kohavi and Thomke, 2017; the lift was real")


# ------------------------------------------------------------------------------ Part 5
def prove_sale_mix():
    rows = {r[0]: (int(num(r[1])), int(num(r[2]))) for r in table(set_no=6)}
    m_o, m_n = rows["Members with the offer"], rows["Members without it"]
    r_o, r_n = rows["Regular with the offer"], rows["Regular without it"]
    offer = (m_o[0] * m_o[1] + r_o[0] * r_o[1]) / (m_o[0] + r_o[0])
    none = (m_n[0] * m_n[1] + r_n[0] * r_n[1]) / (m_n[0] + r_n[0])
    assert (offer, none) == (1025, 960) == (rows["All with the offer"][1], rows["All without it"][1])
    assert pct(offer / none - 1) == 6.8
    effect = m_o[0] * (m_o[1] - m_n[1]) + r_o[0] * (r_o[1] - r_n[1])
    assert effect == -12500
    assert (offer - none) * (m_o[0] + r_o[0]) == 32500                       # the blend
    share = m_n[0] / (m_n[0] + r_n[0])
    at_none_mix = share * m_o[1] + (1 - share) * r_o[1]
    assert math.isclose((at_none_mix - none) * 500, -12000)                  # the other group's mix
    assert m_o[0] * (m_o[1] - m_n[1]) == -7500 and r_o[0] * (r_o[1] - r_n[1]) == -5000
    assert "bar [1470, 1500, 580, 600, 1025, 960]" in SOURCE["exhibits"][6]["mermaid"]
    assert ADDED["sale-mix"]["key"].startswith("A fall of Rs 12,500")
    report("sale-mix", "Rs 12,500 fall", "250 x -30 + 250 x -20 = -12,500 tier against tier; the blend says "
                                         "+32,500")


def prove_sale_advice():
    assert math.isclose(1 / 0.75, 4 / 3) and math.isclose(1 / 0.8, 1.25)
    key = ADDED["sale-advice"]["key"]
    opts = options("sale-advice")
    assert opts[key].startswith("Do not send it as it ran") and "rise by a third" in opts[key]
    assert sum("a third" in t for t in opts.values()) == 2 and sum(t.startswith("Do not") for t in opts.values()) == 2
    assert 1470 < 1500 and 580 < 600 and round(1470 / 580, 1) == 2.5
    report("sale-advice", key, "at 25 percent off orders must rise by 1 over 0.75, a third; each tier fell")


def prove_tool_print():
    out, ns = run_exhibit("tool-print")
    assert out == "order 1099: not found" and ns["results"] == ["out for delivery", "None", "delivered"]
    assert ns["found"] == 3 and sum(1 for r in [ns["results"][0], None, ns["results"][2]] if r) == 2
    key = ADDED["tool-print"]["key"]
    assert options("tool-print")[key] == "'None', and found holds 3 of the 3 lookups."
    report("tool-print", key, "the model reads 'None' for 1099; 'None' is non-empty, so found holds 3")


def prove_agent_history():
    sent = []

    def call_model(history):
        sent.append(len(history))
        return f"reply {len(sent)}"

    run_exhibit("agent-history", {"call_model": call_model})
    assert sent == [1, 3, 5], sent

    def cleared(turns):
        """The default list, cleared at the end of every call, with calls taken in turn."""
        shared, seen = [], []
        for convo, message in turns:
            shared.append((convo, message))
            seen.append((convo, list(shared)))
            shared.clear()
        return seen

    def keyed(turns):
        """Each conversation's messages kept under its id and passed in."""
        store, seen = {}, []
        for convo, message in turns:
            store.setdefault(convo, []).append((convo, message))
            seen.append((convo, list(store[convo])))
            store[convo].append((convo, "reply"))
        return seen

    turns = [("A", "Where is order 1042?"), ("B", "Please cancel order 2210"), ("A", "It says delivered")]
    assert len(cleared(turns)[2][1]) == 1                       # A's second turn has forgotten its first
    assert len(keyed(turns)[2][1]) == 3 and all(c == "A" for c, _ in keyed(turns)[2][1])
    key = ADDED["agent-history"]["key"]
    assert options("agent-history")[key].startswith("5; keep each conversation's messages under its conversation id")
    report("agent-history", key, "the three calls send 1, 3 and 5 messages; a cleared list forgets a second turn")


def prove_agent_cost():
    rows = table("agent-cost")
    calls = [int(r[1]) for r in rows]
    costs = [num(r[2]) for r in rows]
    assert all(math.isclose(c * 0.40, x) for c, x in zip(calls, costs))
    assert sorted(costs)[3] == 1.6 and f"{mean(costs):.2f}" == "7.26" and math.isclose(sum(costs), 50.8)
    typical_calls = sorted(calls)[3]
    assert typical_calls == 4 and round(mean(calls), 1) == 18.1

    def saved(cap):
        return round(sum(max(0, c - cap) for c in calls) * 0.40, 2)

    assert saved(2 * typical_calls) == 38.80 and saved(int(2 * mean(calls))) == 27.60
    assert int(2 * mean(calls)) == 36
    key = ADDED["agent-cost"]["key"]
    assert options("agent-cost")[key] == "Rs 1.60 is the typical cost, and the cap would have saved Rs 38.80."
    report("agent-cost", key, "median cost Rs 1.60; median calls 4, so a cap of 8 saves Rs 38.80; from the mean, "
                              "Rs 27.60")


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
        # The failing-tools query, on a call-level log built from the exhibit's counts.
        cur.execute("CREATE TABLE calls (call_id serial, tool text, status text, called_on date)")
        for tool, status, this_week, last_week in table("sql-failing"):
            for n, day in ((int(this_week), "2026-09-23"), (int(last_week), "2026-09-16")):
                for _ in range(n):
                    cur.execute("INSERT INTO calls (tool, status, called_on) VALUES (%s, %s, %s)",
                                (tool, status, day))
        query = ADDED["sql-failing"]["exhibit"]["code"]["text"]
        cur.execute(query)
        got = sorted(cur.fetchall())
        assert got == [("order_status", 34), ("refund", 38)], got
        variants = {
            "b": query.replace("status <> 'ok'", "status = 'error'"),
            "c": query.replace("\n  AND called_on BETWEEN '2026-09-21' AND '2026-09-27'", ""),
            "d": query.replace("\nHAVING COUNT(*) >= 30", ""),
        }
        want = {"b": [("refund", 35)], "c": [("handover", 63), ("order_status", 49), ("refund", 80)],
                "d": [("handover", 27), ("order_status", 34), ("refund", 38)]}
        for letter, q in variants.items():
            assert q != query
            cur.execute(q)
            assert sorted(cur.fetchall()) == want[letter], letter
        key = ADDED["sql-failing"]["key"]
        assert options("sql-failing")[key] == "Two rows, order_status 34 and refund 38."
        report("sql-failing", key, "Postgres returns order_status 34 and refund 38; 'error' alone gives refund 35")

        # The match table, on the eight calls of its exhibit.
        cur.execute("CREATE TABLE eight (call_id int, conversation_id text, tool text, status text, "
                    "latency_ms int)")
        for r in table("sql-count"):
            cur.execute("INSERT INTO eight VALUES (%s, %s, %s, %s, %s)",
                        (int(r[0]), r[1], None if r[2] == "NULL" else r[2], r[3],
                         None if r[4] == "NULL" else int(r[4])))
        bank = SOURCE["banks"]["sql-results"]["options"]
        for item_id in ("sql-count", "sql-avg", "sql-rate"):
            q = str(ADDED[item_id]["text"]).strip()
            cur.execute(q.replace("FROM calls", "FROM eight"))
            got = cur.fetchone()[0]
            shown = str(int(got)) if float(got) == int(got) else str(got)
            key = ADDED[item_id]["key"]
            assert shown == key and key in bank, (item_id, got)
            report(item_id, key, f"Postgres returns {got} for: {q}")
        cur.execute("SELECT COUNT(*), 1.0 * COUNT(*) FILTER (WHERE status <> 'ok') / COUNT(*), "
                    "AVG(COALESCE(latency_ms, 0)), COUNT(tool) FROM eight")
        n, share, avg0, ntool = cur.fetchone()
        assert (n, float(share), float(avg0), ntool) == (8, 0.375, 600.0, 7)
    finally:
        cur.execute("RESET search_path")
        cur.execute(f"DROP SCHEMA IF EXISTS {schema} CASCADE")
        conn.close()


def main():
    print(f"Week 1 Saturday paper: {len(PRINTED)} timed items. Each line gives the printed Q, the item, "
          f"its key and what proves it.")
    for step in (prove_bank_50, prove_sales_net, prove_first_order, prove_quarter_counter, prove_bank_20,
                 prove_budget_flip, prove_bank_51, prove_reader_header, prove_text_compare,
                 prove_evidence_copy, prove_reject_loop, prove_dup_rule, prove_monday_number,
                 prove_plus_clean, prove_bank_52, prove_plus_real, prove_wald_kalpa, prove_bank_35,
                 prove_shuffle_sign, prove_student_line, prove_diwali_test, prove_debt_weights,
                 prove_debt_rows, prove_orbiter_units, prove_flu_fit, prove_bing_alert, prove_sale_mix,
                 prove_sale_advice, prove_tool_print, prove_agent_history, prove_agent_cost, prove_sql):
        step()
    missing = [i for i in PRINTED if (i["id"] if i["added"] else i["no"]) not in proved]
    assert not missing, [f"Q{i['q']}" for i in missing]
    hard = sum(1 for i in PRINTED if i["level"] == "Hard")
    print(f"PROVED: all {len(PRINTED)} timed items have a key that code, SQL, arithmetic or the tracker "
          f"settles; {hard} are hard.")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W01/SAT/internal/C2_W01_SAT_key_proofs_INTERNAL.py, with Postgres running
#     One line per timed item, 35 in all, then "PROVED: all 35 timed items ...; 21 are hard.", exit 0.
# The sales-net exhibit run on Monday's 29 consumer orders
#     Prints the store at 18920 with its cancelled orders; on orders not cancelled the app leads, option (c).
# The first-order table checked against Monday's 30 orders
#     The 11th of the 21 sorted delivered amounts is Rs 2,060, the key; with zeros the median is Rs 1,480.
# The quarter-counter exhibit on Tuesday's 200 rows, and the same cell with the counter set once
#     Prints {'Q1': 38, 'Q2': 36} -5.3%, option (d); the counter set once prints option (c).
# The budget-flip estimates, each change applied alone
#     Only option (c), a Rs 800 route back at Rs 1.88 a rupee, falls below acquisition's Rs 2.00.
# The reader-header exhibit run on a copy of the export named orders.csv
#     Prints "200 KR-02002"; the pass closes 200 = 185 + 15 and KR-02001 is in neither file.
# The evidence-copy exhibit, and the same cell with copies of the dictionaries
#     Prints "2 + 0 = 2 []", option (a); with copies it prints "2 + 1 = 2 ['KR-02063']".
# The dup-rule rows matched line by line to the export and put through the identity rule
#     Q1 Rs 4,680 and Q2 Rs 7,410; whole rows leave Q2 at Rs 11,120; first copies leave Q1 at Rs 2,890.
# The reconciled file by quarter and segment
#     Retail-Plus 40 to 26, -35.0 percent a member; the company 100 to 86, all 14 in Retail-Plus, option (a).
# Kavya's paired shuffle of the 22 Retail-Plus members, seed 2026, gaps rounded to the rupee
#     Bars 141, 766, 1,526, 1,683, 739 and 145; 145 of 5,000 reach the fall, 0.029, option (c).
# The Student coin tosses, seed 2026, 5,000 worlds of 12 orders
#     Rows 918, 964, 1,133, 1,034, 595 and 356; 1,985 worlds hold 7 or more Q2 orders, option (b).
# The debt-weights exhibit on the seven countries as the spreadsheet carried them
#     Prints "71 -0.07 1.68", option (d); one year of seven carries a seventh of the first average.
# The offer table
#     Rs 12,500 less tier against tier; the blend says Rs 32,500 more.
# The tool-print and agent-history exhibits
#     The model reads 'None' and found holds 3; the three calls send 1, 3 and 5 messages.
# The cost table
#     Median Rs 1.60; median calls 4, a cap of 8 saves Rs 38.80; a cap of 36 from the mean saves Rs 27.60.
# The failing-tools query on a call-level log built from the exhibit's counts
#     Returns order_status 34 and refund 38; status = 'error' alone returns refund 35.
# The three match queries on the eight-call table
#     COUNT(latency_ms) returns 6, AVG(latency_ms) 800 and the integer failure rate 0.
# An exhibit edited so that its printed output no longer matches its keyed option
#     The matching assertion fails and names the item; nothing after it runs.
# Postgres not running
#     psycopg2 raises OperationalError at prove_sql, after every Python and arithmetic item has printed.

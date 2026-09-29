"""Build Friday's two notebooks: the lab workspace (a TODO twin) and the trainer's reference run.

    python3 content/W01/D5/internal/C2_W01_D05_build_notebooks_INTERNAL.py

The reference run executes cold in trainer/, reading ../data/ the way a learner's notebook does,
and every number the lab key quotes is printed and checked there. The data is v3-lab, proposed for
client zero v2.3 and not yet locked.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, md, code, build  # noqa: E402

DAY = ROOT / "content" / "W01" / "D5"

# --------------------------------------------------------------------------- the reference run
REFERENCE = [
    md("""
    # The lab key, run end to end

    **TRAINER ONLY.** Week 1, Friday. The data is `v3-lab`, **proposed for client zero v2.3** and
    not yet locked, so a number here can still move when the lock lands; rerun this notebook then.

    Kavya's terms for the day: "Before anything goes to Meera, rebuild the week from a raw export
    with no assistant and no notes. Then say it to me the way you will say it to her."

    This notebook is the run a careful analyst makes in about ninety minutes, with each trap a
    hurried run falls into computed beside it, exactly, so a TA can recognise a wrong number on a
    learner's screen from across the room. Every figure in the lab key and the day sheet comes from
    a printed cell below.
    """),
    code(SETUP + '''
import random
import statistics

rows = kit.load_csv("C2_W01_D05_lab_orders_STUDENT.csv")
control = {c["quarter"]: c for c in kit.load_csv("C2_W01_D05_lab_control_STUDENT.csv")}
print(f"{len(rows)} rows read; control totals for {sorted(control)}")
print(rows[0])
'''),
    code('''
kit.flow(["profile", "clean, with a decisions log", "reconcile to the control totals",
          "decompose along the tree", "one shuffle test", "the four-part note"], lit=2,
         title="The week's method, in the order the lab runs it; the lit step is the one most rooms skip")
'''),
    md("""
    ## 1. Profile before touching anything

    Three counts per field: present, convertible where a number is expected, distinct. The finding
    of the profile is every place where a count disagrees with what the field should hold.
    """),
    code('''
def profile(records, field, numeric=False):
    present = [r[field] for r in records if r.get(field, "") != ""]
    convertible = None
    if numeric:
        convertible = 0
        for v in present:
            try:
                int(v)
                convertible += 1
            except ValueError:
                pass
    return len(present), convertible, len(set(present))


fields = list(rows[0])
prof = {f: profile(rows, f, numeric=(f == "amount")) for f in fields}
kit.table(["field", "present", "convertible", "distinct"],
          [(f, p, "" if c is None else c, d) for f, (p, c, d) in prof.items()],
          caption=f"The profile of {len(rows)} rows, before any decision")
'''),
    code('''
ids = [r["order_id"] for r in rows]
kit.check("207 rows carry 197 distinct order ids, so ten rows repeat an id",
          len(rows) == 207 and len(set(ids)) == 197, f"{len(rows)} rows, {len(set(ids))} ids")
kit.check("one amount will not convert and one segment is empty",
          prof["amount"][1] == 206 and prof["segment"][0] == 206)
'''),
    md("""
    **The first trap: the typical order.** A hurried profile reports the mean order as the typical
    one. The median is the honest answer, because ten corporate orders sit above Rs 7 lakh while
    every consumer order sits under Rs 4,000.
    """),
    code('''
amounts_all = sorted(int(r["amount"]) for r in rows if r["amount"].isdigit())
kit.table(["measure", "on the rows that convert, duplicates still in"],
          [("mean order", kit.rupees(statistics.mean(amounts_all))),
           ("median order", kit.rupees(statistics.median(amounts_all)))],
          caption="The mean is the wrong typical order by a factor of about 25")
'''),
    md("""
    ## 2. Clean, with a reason written for every decision

    Three decisions, each logged with its row count as it is made. The identity rule is the order
    id: two rows with one id are one order. The corporate amount written with Indian digit grouping
    is a real order stored as text, so it is converted and flagged, never set to zero. The empty
    segment is restored from the same customer's other orders, flagged, because every one of that
    customer's other orders carries one segment.
    """),
    code('''
log, clean, rejected, seen, first_raw = [], [], [], {}, {}
customer_segment = {}
for r in rows:
    if r["segment"]:
        customer_segment.setdefault(r["customer_id"], set()).add(r["segment"])

for r in rows:
    r = dict(r)
    first_raw.setdefault(r["order_id"], dict(r))
    if r["order_id"] in seen:
        same = first_raw[r["order_id"]] == r
        rejected.append(r)
        log.append({"order_id": r["order_id"], "decision": "drop",
                    "reason": "second row of an order already kept" + ("" if same else ", fields differ")})
        continue
    if not r["amount"].isdigit():
        digits = r["amount"].replace(",", "")
        log.append({"order_id": r["order_id"], "decision": "convert and flag",
                    "reason": f"amount stored as text {r['amount']!r}, read as {digits}"})
        r["amount"] = digits
    if r["segment"] == "":
        segs = customer_segment.get(r["customer_id"], set())
        log.append({"order_id": r["order_id"], "decision": "default and flag",
                    "reason": f"segment empty; the customer's other orders are all {sorted(segs)}"})
        r["segment"] = sorted(segs)[0]
    r["amount"] = int(r["amount"])
    seen[r["order_id"]] = r
    clean.append(r)

kit.table(["decision", "rows"],
          [(d, sum(1 for e in log if e["decision"] == d)) for d in ("drop", "convert and flag", "default and flag")],
          caption="The decisions log, counted")
'''),
    code('''
kit.check("every dropped row repeats an order kept, field for field",
          all("differ" not in e["reason"] for e in log if e["decision"] == "drop"))
kit.check("the restored segment comes from a customer with one segment only",
          all(len(customer_segment[r["customer_id"]]) == 1 for r in clean))
'''),
    md("""
    **The second trap: the pass that looks clean.** A hurried pass wraps `int()` in a try and sets a
    failure to zero. It reports no rejects, the row count reconciles, and Q1 is short by the whole
    corporate order.
    """),
    code('''
def coerce(v):
    try:
        return int(v)
    except ValueError:
        return 0


zeroed_q1 = sum(coerce(r["amount"]) for r in {r["order_id"]: r for r in rows}.values() if r["quarter"] == "Q1")
print(f"Q1 on the zero-coercing pass: {kit.rupees(zeroed_q1)}, 98 orders, 0 rejects")
print(f"Q1 in Finance's control totals: {kit.rupees(int(control['Q1']['amount_rs']))}, {control['Q1']['orders']} orders")
kit.check("the counts reconcile while the rupees do not",
          zeroed_q1 != int(control["Q1"]["amount_rs"]), kit.rupees(int(control["Q1"]["amount_rs"]) - zeroed_q1))
'''),
    md("""
    ## 3. Reconcile: input equals clean plus rejected, and the rupees land on the control totals

    This is the step most rooms skip when the clock runs, and it is the only one that catches both
    the batch posted twice and the amount lost as text.
    """),
    code('''
by_q = {q: [r for r in clean if r["quarter"] == q] for q in ("Q1", "Q2")}
kit.table(["quarter", "clean orders", "control orders", "clean rupees", "control rupees"],
          [(q, len(by_q[q]), control[q]["orders"], kit.rupees(sum(r["amount"] for r in by_q[q])),
            kit.rupees(int(control[q]["amount_rs"]))) for q in ("Q1", "Q2")],
          caption="Clean against Finance's control totals")
kit.check("input equals clean plus rejected", len(rows) == len(clean) + len(rejected),
          f"{len(rows)} = {len(clean)} + {len(rejected)}")
kit.check("both quarters land on the control totals, orders and rupees",
          all(len(by_q[q]) == int(control[q]["orders"]) and
              sum(r["amount"] for r in by_q[q]) == int(control[q]["amount_rs"]) for q in by_q))
'''),
    code('''
as_read = sum(int(r["amount"]) for r in rows if r["amount"].isdigit())
dupes = -sum(int(r["amount"]) for r in rejected)
text_back = sum(r["amount"] for r in clean if any(e["order_id"] == r["order_id"] and
                e["decision"] == "convert and flag" for e in log))
kit.bridge(("summed as read", as_read),
           [("rows posted twice", dupes), ("amount stored as text", text_back)],
           end_label="clean, both quarters",
           title="From the export as a hurried sum reads it to the books", lit=[0], lo=9_000_000)
print(f"as read {kit.rupees(as_read)}, duplicates {kit.rupees(dupes)}, text amount +{kit.rupees(text_back)}, "
      f"lands on {kit.rupees(as_read + dupes + text_back)}")
'''),
    md("""
    **The third trap, the one most rooms fall into: the reconciliation skipped.** A run that keeps
    the repeated rows and loses the text amount compares two wrong quarters and reports growth. Each
    half of the mistake on its own gives a different wrong number, and all three are below.
    """),
    code('''
def total(q, keep_dupes, text_ok):
    src = rows if keep_dupes else list({r["order_id"]: r for r in rows}.values())
    out = 0
    for r in src:
        if r["quarter"] != q:
            continue
        v = r["amount"]
        out += int(v.replace(",", "")) if text_ok else (int(v) if v.isdigit() else 0)
    return out


def change(a, b):
    return 100 * (b / a - 1)


variants = [("the reconciled run", False, True), ("duplicates kept, text read correctly", True, True),
            ("duplicates removed, text set to zero", False, False), ("both mistakes, the hurried run", True, False)]
kit.table(["run", "Q1", "Q2", "Q1 to Q2"],
          [(name, kit.rupees(total("Q1", d, t)), kit.rupees(total("Q2", d, t)),
            f"{change(total('Q1', d, t), total('Q2', d, t)):+.1f}%") for name, d, t in variants],
          caption="One export, four headlines")
honest = change(total("Q1", False, True), total("Q2", False, True))
hurried = change(total("Q1", True, False), total("Q2", True, False))
kit.check("the hurried run reports growth where the books show a fall", hurried > 0 > honest,
          f"{hurried:+.1f}% against {honest:+.1f}%")
'''),
    md("""
    ## 4. Decompose along the tree, segment by segment

    Revenue is customers, times orders per customer, times revenue per order. The total moved; the
    tree says which branch, in which segment.
    """),
    code('''
SEGS = ("Retail-Core", "Retail-Plus", "Student", "Business")


def tree(src, q, seg):
    rs = [r for r in src if r["quarter"] == q and r["segment"] == seg]
    cust = len({r["customer_id"] for r in rs})
    rev = sum(int(r["amount"]) for r in rs)
    return len(rs), cust, len(rs) / cust, rev / len(rs), rev


rows_out = []
for seg in SEGS:
    a, b = tree(clean, "Q1", seg), tree(clean, "Q2", seg)
    rows_out.append((seg, f"{a[1]} / {b[1]}", f"{a[2]:.2f} / {b[2]:.2f}",
                     f"{kit.rupees(a[3])} / {kit.rupees(b[3])}", f"{change(a[4], b[4]):+.1f}%", f"{a[0]} / {b[0]}"))
kit.table(["segment", "customers Q1 / Q2", "orders per customer", "revenue per order", "revenue", "orders"],
          rows_out, caption="The tree, clean, Q1 against Q2")
'''),
    code('''
consumer = SEGS[:3]
kit.columns(list(consumer), [("Q1", [tree(clean, "Q1", s)[3] for s in consumer]),
                             ("Q2", [tree(clean, "Q2", s)[3] for s in consumer])],
            title="Revenue per order by consumer segment: Retail-Core's basket is the branch that moved",
            fmt=lambda v: kit.rupees(v), lit=[0])
biz = tree(clean, "Q1", "Business")[4] - tree(clean, "Q2", "Business")[4]
whole = int(control["Q1"]["amount_rs"]) - int(control["Q2"]["amount_rs"])
print(f"The fall is {kit.rupees(whole)}; Business carries {kit.rupees(biz)} of it, {100 * biz / whole:.1f} percent, "
      f"on {tree(clean, 'Q1', 'Business')[0]} orders then {tree(clean, 'Q2', 'Business')[0]}")
'''),
    code('''
core1, core2 = tree(clean, "Q1", "Retail-Core"), tree(clean, "Q2", "Retail-Core")
kit.check("Retail-Core's customers and frequency hold while its basket falls",
          core1[1] == core2[1] and abs(core1[2] - core2[2]) < 0.01 and change(core1[3], core2[3]) < -15,
          f"{change(core1[3], core2[3]):+.1f}% per order")
kit.check("the corporate fall rests on fewer than thirty orders",
          tree(clean, "Q1", "Business")[0] + tree(clean, "Q2", "Business")[0] < 30)
'''),
    md("""
    **The fourth trap: the wrong branch.** On the uncleaned rows Retail-Core's customers seem to
    order about a fifth more often in Q2, which cancels the basket fall and reads the segment as
    flat. The frequency rise is the repeated batch and nothing else.
    """),
    code('''
h1 = tree([r for r in rows if r["segment"] and r["amount"].isdigit()], "Q1", "Retail-Core")
h2 = tree([r for r in rows if r["segment"] and r["amount"].isdigit()], "Q2", "Retail-Core")
kit.table(["Retail-Core", "orders per customer", "revenue per order", "revenue"],
          [("hurried Q1", f"{h1[2]:.2f}", kit.rupees(h1[3]), kit.rupees(h1[4])),
           ("hurried Q2", f"{h2[2]:.2f}", kit.rupees(h2[3]), kit.rupees(h2[4])),
           ("hurried change", f"{change(h1[2], h2[2]):+.1f}%", f"{change(h1[3], h2[3]):+.1f}%", f"{change(h1[4], h2[4]):+.1f}%"),
           ("clean change", f"{change(core1[2], core2[2]):+.1f}%", f"{change(core1[3], core2[3]):+.1f}%",
            f"{change(core1[4], core2[4]):+.1f}%")],
          caption="The repeated rows turn a basket problem into a flat segment")
kit.check("the hurried run shows frequency up and revenue flat in Retail-Core",
          change(h1[2], h2[2]) > 15 and abs(change(h1[4], h2[4])) < 1)
'''),
    md("""
    ## 5. One shuffle test, on the customer

    Thursday's test, rerun: does Retail-Core's change in revenue per order differ from Retail-Plus's
    by more than chance produces? The labels are shuffled across **customers**, because a
    customer's orders belong together. 2,000 shuffles, `random.Random(7)`.
    """),
    code('''
def basket_change(rs):
    a = [r["amount"] for r in rs if r["quarter"] == "Q1"]
    b = [r["amount"] for r in rs if r["quarter"] == "Q2"]
    return change(sum(a) / len(a), sum(b) / len(b))


core = [r for r in clean if r["segment"] == "Retail-Core"]
plus = [r for r in clean if r["segment"] == "Retail-Plus"]
observed = basket_change(core) - basket_change(plus)
by_customer = {}
for r in core + plus:
    by_customer.setdefault(r["customer_id"], []).append(r)
members = sorted(by_customer)
n_core = len({r["customer_id"] for r in core})


def shuffled(rng):
    m = members[:]
    rng.shuffle(m)
    return (basket_change([r for c in m[:n_core] for r in by_customer[c]])
            - basket_change([r for c in m[n_core:] for r in by_customer[c]]))


rng = random.Random(7)
gaps = [shuffled(rng) for _ in range(2000)]
extreme = sum(1 for g in gaps if abs(g) >= abs(observed))
print(f"observed gap {observed:+.1f} points; {extreme} of 2,000 shuffles as extreme; p = {extreme / 2000:.4f}")
kit.strip(gaps, markers=[("observed", observed, "bad"), ("its mirror", -observed, "plain")],
          lo=-24, hi=24, fmt=lambda v: f"{v:+.0f}", title="2,000 chance-only worlds against the real gap")
'''),
    code('''
band = []
for seed in range(1, 21):
    r2 = random.Random(seed)
    band.append(sum(1 for _ in range(2000) if abs(shuffled(r2)) >= abs(observed)) / 2000)
print(f"Twenty other seeds at 2,000 shuffles: p from {min(band):.4f} to {max(band):.4f}")
kit.check("the gap is one chance rarely produces, on every seed tried", max(band) < 0.05,
          f"p = {extreme / 2000:.4f} on seed 7")
'''),
    md("""
    **The fifth trap: the wrong unit.** Shuffling orders instead of customers splits each customer's
    orders across the two groups, builds worlds that could not exist, widens the chance spread, and
    turns a real gap into "could be chance".
    """),
    code('''
both = core + plus
rng = random.Random(7)
ext_orders = 0
for _ in range(2000):
    idx = list(range(len(both)))
    rng.shuffle(idx)
    a = [both[i] for i in idx[:len(core)]]
    b = [both[i] for i in idx[len(core):]]
    if abs(basket_change(a) - basket_change(b)) >= abs(observed):
        ext_orders += 1
print(f"shuffling orders: {ext_orders} of 2,000, p = {ext_orders / 2000:.4f}")
kit.check("shuffling the wrong unit moves the verdict across 0.05", ext_orders / 2000 > 0.05 > extreme / 2000)
'''),
    md("""
    ## 6. The note, in four parts, as a correct run writes it

    **Claim.** From Q1 to Q2 booked revenue fell 28.5 percent, from Rs 60,48,000 to Rs 43,25,480,
    and Rs 17,10,000 of the Rs 17,22,520 fall is two fewer corporate orders; among consumers the
    one branch that moved is Retail-Core's revenue per order, down 17.1 percent from Rs 2,050 to
    Rs 1,700, with its 30 customers and 1.47 orders each unchanged.

    **Evidence.** 197 distinct orders reconcile to Finance's control totals in both quarters, 98
    and 99 orders to the rupee, after dropping 10 rows posted twice and converting one amount
    stored as text; the Retail-Core gap against Retail-Plus came up as large in only 39 of
    2,000 customer-level shuffles, p = 0.02.

    **Caveat.** The corporate fall rests on six orders against four, too few to call a trend, and
    one Q2 order's segment was restored from the customer's other orders.

    **Action.** Open Retail-Core's basket first, items per order and price per item, before any
    spend; treat the corporate fall as noise until a third quarter says otherwise.

    **The sixth trap: the headline on ten orders.** "Corporate revenue fell 29 percent" is true to
    the rupee and rests on ten orders; a note that leads with it sends Meera after two invoices.
    """),
    code('''
kit.table(["trap", "the wrong number", "the right number", "the check that catches it"], [
    ("the typical order", kit.rupees(statistics.mean(amounts_all)) + " (mean)",
     kit.rupees(statistics.median(amounts_all)) + " (median)", "sort, read the top ten"),
    ("the pass that looks clean", "Q1 " + kit.rupees(zeroed_q1) + ", 0 rejects",
     "Q1 " + kit.rupees(int(control["Q1"]["amount_rs"])), "rupees against the control total"),
    ("the reconciliation skipped", f"Q2 {hurried:+.1f}%", f"Q2 {honest:+.1f}%", "input = clean + rejected; control totals"),
    ("the wrong branch", f"Retail-Core frequency {change(h1[2], h2[2]):+.1f}%, revenue flat",
     f"basket {change(core1[3], core2[3]):+.1f}%, frequency flat", "distinct ids against rows, per segment"),
    ("the wrong unit", f"p = {ext_orders / 2000:.4f}", f"p = {extreme / 2000:.4f}", "shuffle customers"),
    ("the headline on ten orders", "corporate revenue -29.2%", "6 orders then 4", "count before rate"),
], caption="Every trap in the lab, with its exact wrong number")
'''),
    md("""
    ## The practice export, for the practice lab

    The same method on the practice file, so the TA holds every number a learner reruns toward.
    Its defects sit in yet other places.
    """),
    code('''
prac = kit.load_csv("C2_W01_D05_practice_orders_STUDENT.csv")
pctl = {c["quarter"]: c for c in kit.load_csv("C2_W01_D05_practice_control_STUDENT.csv")}
pids = [r["order_id"] for r in prac]
pclean, pseen = [], set()
for r in prac:
    if r["order_id"] in pseen:
        continue
    pseen.add(r["order_id"])
    r = dict(r)
    r["amount"] = int(r["amount"].replace("Rs", "").replace(",", "").strip())
    pclean.append(r)
odd = [r for r in prac if not r["amount"].isdigit()]
blank = [r for r in prac if not r["customer_id"]]
kit.table(["measure", "value"], [
    ("rows", len(prac)), ("distinct order ids", len(set(pids))), ("amounts that will not convert", len(odd)),
    ("rows with no customer_id", len(blank)),
    ("Q1 clean / control", f"{kit.rupees(sum(r['amount'] for r in pclean if r['quarter'] == 'Q1'))} / {kit.rupees(int(pctl['Q1']['amount_rs']))}"),
    ("Q2 clean / control", f"{kit.rupees(sum(r['amount'] for r in pclean if r['quarter'] == 'Q2'))} / {kit.rupees(int(pctl['Q2']['amount_rs']))}"),
], caption="The practice export, reconciled")
ptab = []
for seg in SEGS:
    a = [r for r in pclean if r["quarter"] == "Q1" and r["segment"] == seg]
    b = [r for r in pclean if r["quarter"] == "Q2" and r["segment"] == seg]
    ca = len({r["customer_id"] for r in a if r["customer_id"]})
    cb = len({r["customer_id"] for r in b if r["customer_id"]})
    ptab.append((seg, f"{ca} / {cb}", f"{len(a) / ca:.2f} / {len(b) / cb:.2f}",
                 f"{kit.rupees(sum(r['amount'] for r in a) / len(a))} / {kit.rupees(sum(r['amount'] for r in b) / len(b))}",
                 f"{len(a)} / {len(b)}"))
kit.table(["segment", "customers", "orders per customer", "revenue per order", "orders"], ptab,
          caption="The practice tree, Q1 / Q2 (customers counted on rows that carry an id)")
kit.check("the practice export reconciles to its control totals",
          all(sum(r["amount"] for r in pclean if r["quarter"] == q) == int(pctl[q]["amount_rs"]) and
              sum(1 for r in pclean if r["quarter"] == q) == int(pctl[q]["orders"]) for q in ("Q1", "Q2")))
'''),
    code("kit.check_summary()"),
]

# --------------------------------------------------------------------------- the lab workspace
LAB = [
    md("""
    # The AI-free lab: the week, rebuilt alone

    Kavya Nair, senior analyst, to the team: "Before anything goes to Meera, rebuild the week from a
    raw export with no assistant and no notes. Then say it to me the way you will say it to her,
    because I will push the way Marketing will."

    **The export.** `C2_W01_D05_lab_orders_STUDENT.csv`: two quarters of orders you have not seen,
    Kalpa-shaped and re-keyed for the drill, so nothing you find in it belongs in Monday's note.
    Finance's control totals for the same export are in `C2_W01_D05_lab_control_STUDENT.csv`.

    **The rules.** No assistant, notes closed, no other day's notebook open. 120 minutes on the clock.
    Save as you go. A TA watches the room and writes down where each person is at each mark; nothing
    is scored and nothing goes on a wall.

    **What you hand in**, written into `output/` by the last cell: the cleaned orders, the decisions
    log, and the note.

    Every `__TODO__` is yours. The six sections follow the week's order, and the minutes beside each
    are a pace, not a limit.
    """),
    code(SETUP + '''
import csv
import random

rows = kit.load_csv("C2_W01_D05_lab_orders_STUDENT.csv")
control = kit.load_csv("C2_W01_D05_lab_control_STUDENT.csv")
print(len(rows), "rows read")
'''),
    code('''
# The map of the lab. Light the step you are on when you start it.
kit.flow(["profile", "clean, with a decisions log", "reconcile", "decompose along the tree",
          "one shuffle test", "the four-part note"], lit=__TODO1__)
'''),
    md("""
    ## 1. Profile (about 20 minutes)

    Before you change anything: for every field, how many values are present, how many convert
    where a number belongs, and how many are distinct. Write down each count that is not what the
    field should hold.
    """),
    code('''
__TODO2__
'''),
    code('''
kit.check("I profiled every field", __TODO3__)
'''),
    md("""
    ## 2. Clean, with a decisions log (about 30 minutes)

    Every change is a decision: drop, default, or keep and flag. Each gets a row in `log` as you
    make it, with the order id, the decision and the reason. Keep what you remove in `rejected`.
    """),
    code('''
log = []        # {"order_id": ..., "decision": ..., "reason": ...}
clean = []
rejected = []
__TODO4__
'''),
    md("""
    ## 3. Reconcile (about 15 minutes)

    Prove the clean data is the same data. Write the checks you would show Finance, then draw the
    bridge from what you read to what you kept.
    """),
    code('''
kit.check("__TODO5__", __TODO6__)
kit.check("__TODO7__", __TODO8__)
'''),
    code('''
kit.bridge(__TODO9__, __TODO10__, end_label="clean", title="From the export to the clean data")
'''),
    md("""
    ## 4. Decompose along the tree (about 25 minutes)

    Q1 against Q2, segment by segment: customers, orders per customer, revenue per order, revenue.
    Name the branch and the segment that moved, and how many orders each rate rests on.
    """),
    code('''
__TODO11__
'''),
    code('''
kit.columns(__TODO12__, __TODO13__, title="__TODO14__")
kit.check("my segments add back to the total, in orders and in rupees", __TODO15__)
'''),
    md("""
    ## 5. One shuffle test (about 15 minutes)

    Test the one gap your decomposition says matters. Decide what you shuffle and why, use 2,000
    shuffles and `random.Random(7)`, and write the p-value as one sentence that says what it is a
    share of.
    """),
    code('''
__TODO16__
'''),
    code('''
kit.strip(__TODO17__, markers=[("observed", __TODO18__, "bad")], lo=-30, hi=30,
          fmt=lambda v: f"{v:+.0f}", title="Chance-only worlds against the real gap")
kit.check("__TODO19__", __TODO20__)
'''),
    md("""
    ## 6. The note (about 15 minutes)

    Four parts, in order, as it would reach Meera: the claim with its number and denominator, the
    evidence, the caveat that would change the claim, and the action with its cost. Under 150 words.
    """),
    code('''
note = """
Claim: __TODO21__
Evidence: __TODO22__
Caveat: __TODO23__
Action: __TODO24__
"""
out = pathlib.Path("output")
out.mkdir(exist_ok=True)
with (out / "clean_orders.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(clean[0]))
    w.writeheader()
    w.writerows(clean)
with (out / "decisions_log.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["order_id", "decision", "reason"])
    w.writeheader()
    w.writerows(log)
(out / "note.md").write_text(note, encoding="utf-8")
print("written:", sorted(p.name for p in out.iterdir()))
'''),
    code("kit.check_summary()"),
]

if __name__ == "__main__":
    build(DAY / "trainer" / "C2_W01_D05_lab_reference_TRAINER.ipynb", REFERENCE)
    build(DAY / "notebooks" / "C2_W01_D05_lab_STUDENT.ipynb", LAB, execute=False)
    print("built both notebooks")

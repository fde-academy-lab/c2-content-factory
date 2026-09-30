"""The invented export behind every number the debrief deck and the study notes show for a trap.

    python3 content/W01/D5/internal/C2_W01_D05_invented_export_INTERNAL.py

The lab export's plants are named in no learner file (decision plants-once-found in
data/programme/facts.yaml, and the fix pass of 30 September 2026), so the debrief deck and the study
notes show each trap's mechanism on this export instead, labelled invented wherever its numbers
appear. It is built record by record, so every figure the deck and the notes quote is computed here
and asserted, never written by hand.

It carries the same four defect families as the lab export in other places and at other sizes: the
batch posted twice sits in Retail-Plus and one corporate order (the lab's sat in Retail-Core), the
amount that will not convert is a corporate order exported with its paise, "850000.00" (the lab's
used grouping commas), the empty segment is a Q1 Retail-Core order (the lab's was a Q2 Retail-Plus
order), and the corporate book falls from five orders to two (the lab's from six to four). Its
finding is Retail-Plus's basket, where the lab's is Retail-Core's. Nothing here is a Kalpa record.
"""
import math
import random
from collections import Counter

SEGMENTS = ("Retail-Core", "Retail-Plus", "Student", "Business")
PLAN = {  # orders per quarter
    "Q1": {"Retail-Core": 36, "Retail-Plus": 32, "Student": 10, "Business": 5},
    "Q2": {"Retail-Core": 36, "Retail-Plus": 32, "Student": 14, "Business": 2},
}
TOTALS = {  # consumer rupees per quarter
    "Q1": {"Retail-Core": 75600, "Retail-Plus": 96000, "Student": 9000},
    "Q2": {"Retail-Core": 74880, "Retail-Plus": 81600, "Student": 12320},
}
BANDS = {
    ("Q1", "Retail-Core"): (1300, 2900), ("Q2", "Retail-Core"): (1300, 2900),
    ("Q1", "Retail-Plus"): (2000, 4000), ("Q2", "Retail-Plus"): (1600, 3500),
    ("Q1", "Student"): (500, 1300), ("Q2", "Student"): (500, 1300),
}
BUSINESS = {"Q1": [940000, 850000, 729400, 600000, 700000], "Q2": [1200000, 1231200]}
CUSTOMERS = {"Retail-Core": 24, "Retail-Plus": 16, "Student": 10, "Business": 5}
PREFIX = {"Retail-Core": "C", "Retail-Plus": "P", "Student": "S", "Business": "B"}
TEXT_AMOUNT = "850000.00"
SEED = 2020


def amounts(rng, n, band, total):
    low, high = band
    vals = [rng.randrange(low, high + 1, 10) for _ in range(n)]
    step = 10 if total > sum(vals) else -10
    i = 0
    while sum(vals) != total:
        j = i % n
        if low <= vals[j] + step <= high:
            vals[j] += step
        i += 1
    return vals


def clean_orders():
    rng = random.Random(SEED)
    rows = []
    for q in ("Q1", "Q2"):
        for seg in SEGMENTS:
            n = PLAN[q][seg]
            vals = list(BUSINESS[q]) if seg == "Business" else amounts(rng, n, BANDS[(q, seg)], TOTALS[q][seg])
            for i in range(n):
                rows.append({"order_id": f"INV-{len(rows) + 1:04d}", "quarter": q, "segment": seg,
                             "customer_id": f"{PREFIX[seg]}{i % CUSTOMERS[seg] + 1:02d}", "amount": vals[i]})
    return rows


def as_exported(clean):
    rows = [dict(r) for r in clean]
    # The corporate order exported with its paise.
    text = next(r for r in rows if r["quarter"] == "Q1" and r["amount"] == 850000)
    text["amount"] = TEXT_AMOUNT
    # A Q1 Retail-Core order whose segment is missing; its customer's other order is Retail-Core.
    core_q1 = [r for r in rows if r["quarter"] == "Q1" and r["segment"] == "Retail-Core"]
    blank = core_q1[3]
    blank["segment"] = ""
    # A Q2 batch posted twice: seven Retail-Plus orders and the larger of the two corporate orders.
    plus_q2 = [r for r in rows if r["quarter"] == "Q2" and r["segment"] == "Retail-Plus"]
    batch = plus_q2[20:27] + [next(r for r in rows if r["amount"] == 1200000)]
    return rows + [dict(r) for r in batch], text, blank, batch


def change(a, b):
    return 100 * (b / a - 1)


def value(r):
    v = r["amount"]
    return v if isinstance(v, int) else round(float(v))


def main():
    clean = clean_orders()
    rows, text, blank, batch = as_exported(clean)
    ctl = {q: (sum(r["amount"] for r in clean if r["quarter"] == q), sum(1 for r in clean if r["quarter"] == q))
           for q in ("Q1", "Q2")}
    assert ctl == {"Q1": (4000000, 83), "Q2": (2600000, 84)}, ctl
    truth = change(ctl["Q1"][0], ctl["Q2"][0])

    def total(src, q, zero_text):
        s = n = 0
        for r in src:
            if r["quarter"] != q:
                continue
            n += 1
            s += 0 if (zero_text and not isinstance(r["amount"], int)) else value(r)
        return s, n

    first = list({r["order_id"]: r for r in rows}.values())
    hurried = {q: total(rows, q, True) for q in ("Q1", "Q2")}
    counted = {q: total(first, q, True) for q in ("Q1", "Q2")}
    fixed = {q: total(first, q, False) for q in ("Q1", "Q2")}
    assert all(fixed[q] == ctl[q] for q in fixed)
    h, c = change(hurried["Q1"][0], hurried["Q2"][0]), change(counted["Q1"][0], counted["Q2"][0])
    repeats = sum(r["amount"] for r in batch)
    as_read = hurried["Q1"][0] + hurried["Q2"][0]
    assert as_read - repeats + 850000 == ctl["Q1"][0] + ctl["Q2"][0]

    out = []
    say = out.append
    say(f"profile: rows {len(rows)}, distinct ids {len({r['order_id'] for r in rows})}, amount convertible "
        f"{sum(1 for r in rows if isinstance(r['amount'], int))}, segment present {sum(1 for r in rows if r['segment'])}")
    say(f"control: Q1 Rs {ctl['Q1'][0]:,} on {ctl['Q1'][1]}, Q2 Rs {ctl['Q2'][0]:,} on {ctl['Q2'][1]}, {truth:+.1f}%")
    say(f"hurried: Q1 Rs {hurried['Q1'][0]:,} on {hurried['Q1'][1]} rows, Q2 Rs {hurried['Q2'][0]:,} on "
        f"{hurried['Q2'][1]} rows, {h:+.1f}%, points off {abs(h - truth):.1f}")
    say(f"count check only: Q1 Rs {counted['Q1'][0]:,}, Q2 Rs {counted['Q2'][0]:,}, {c:+.1f}%, points off {abs(c - truth):.1f}")
    say(f"repeated batch: {len(batch)} rows, Rs {repeats:,} (Plus Rs {repeats - 1200000:,} on 7 rows, corporate Rs 12,00,000)")
    say(f"bridge: as read Rs {as_read:,} less Rs {repeats:,} plus Rs 8,50,000 = Rs {as_read - repeats + 850000:,}")
    say(f"text amount: {TEXT_AMOUNT!r} in Q1, {100 * 850000 / ctl['Q1'][0]:.2f}% of the quarter")

    # The wrong branch: Retail-Plus on the hurried rows against the clean ones.
    def seg_tree(src, q, seg):
        rs = [r for r in src if r["quarter"] == q and r["segment"] == seg and isinstance(r["amount"], int)]
        cust = len({r["customer_id"] for r in rs})
        rev = sum(r["amount"] for r in rs)
        return len(rs), cust, len(rs) / cust, rev / len(rs), rev

    ph1, ph2 = seg_tree(rows, "Q1", "Retail-Plus"), seg_tree(rows, "Q2", "Retail-Plus")
    pc1, pc2 = seg_tree(first, "Q1", "Retail-Plus"), seg_tree(first, "Q2", "Retail-Plus")
    say(f"wrong branch, Plus hurried: frequency {ph1[2]:.2f} to {ph2[2]:.2f} ({change(ph1[2], ph2[2]):+.1f}%), "
        f"revenue Rs {ph1[4]:,} to Rs {ph2[4]:,} ({change(ph1[4], ph2[4]):+.1f}%)")
    say(f"Plus clean: frequency {pc1[2]:.2f} to {pc2[2]:.2f}, basket Rs {pc1[3]:,.0f} to Rs {pc2[3]:,.0f} "
        f"({change(pc1[3], pc2[3]):+.1f}%), revenue Rs {pc1[4]:,} to Rs {pc2[4]:,}")

    # The empty segment: Retail-Core's Q1 on named rows only against the order restored.
    core_named = sum(r["amount"] for r in first if r["quarter"] == "Q1" and r["segment"] == "Retail-Core"
                     and isinstance(r["amount"], int))
    core_q2 = TOTALS["Q2"]["Retail-Core"]
    say(f"empty segment: Q1 order Rs {blank['amount']:,}; Core Q1 named Rs {core_named:,} on "
        f"{PLAN['Q1']['Retail-Core'] - 1} orders ({change(core_named, core_q2):+.1f}% to Q2), restored Rs "
        f"{TOTALS['Q1']['Retail-Core']:,} ({change(TOTALS['Q1']['Retail-Core'], core_q2):+.1f}%)")

    # The clean tree.
    for seg in SEGMENTS:
        a, b = seg_tree(clean, "Q1", seg), seg_tree(clean, "Q2", seg)
        say(f"tree {seg}: customers {a[1]} / {b[1]}, freq {a[2]:.2f} / {b[2]:.2f}, basket Rs {a[3]:,.0f} / "
            f"Rs {b[3]:,.0f}, revenue Rs {a[4]:,} / Rs {b[4]:,} ({change(a[4], b[4]):+.1f}%), orders {a[0]} / {b[0]}")
    fall = ctl["Q1"][0] - ctl["Q2"][0]
    biz = sum(BUSINESS["Q1"]) - sum(BUSINESS["Q2"])
    say(f"fall Rs {fall:,}; corporate Rs {biz:,} ({100 * biz / fall:.1f}%); Plus Rs "
        f"{TOTALS['Q1']['Retail-Plus'] - TOTALS['Q2']['Retail-Plus']:,} ({100 * 14400 / fall:.1f}%)")
    n = 7
    even = sum(math.comb(n, k) for k in (3, 4)) / 2 ** n
    say(f"coin flips on 7 corporate orders: at least as uneven as 5 and 2 in {1 - even:.3f}")

    # The lead tested on the members' own two quarters, and the two tests that break that pairing.
    plus = [r for r in clean if r["segment"] == "Retail-Plus"]
    per = {}
    for r in plus:
        per.setdefault(r["customer_id"], {"Q1": [], "Q2": []})[r["quarter"]].append(r["amount"])
    members = sorted(per)

    def basket(swaps):
        q1r = q1n = q2r = q2n = 0
        for m, s in zip(members, swaps):
            a, b = per[m]["Q1"], per[m]["Q2"]
            if s:
                a, b = b, a
            q1r, q1n, q2r, q2n = q1r + sum(a), q1n + len(a), q2r + sum(b), q2n + len(b)
        return change(q1r / q1n, q2r / q2n)

    obs = basket([False] * len(members))
    rng = random.Random(7)
    both = one = 0
    for _ in range(2000):
        s = basket([rng.random() < 0.5 for _ in members])
        both += abs(s) >= abs(obs) - 1e-9
        one += s <= obs + 1e-9
    say(f"paired flips on Plus's {len(members)} members, 2,000 on Random(7): basket {obs:+.1f}%, "
        f"{both} as large either way, p = {both / 2000:.4f}; one way {one / 2000:.4f}")
    fell = sum(1 for m in members if sum(per[m]["Q2"]) / len(per[m]["Q2"]) < sum(per[m]["Q1"]) / len(per[m]["Q1"]))
    rose = sum(1 for m in members if sum(per[m]["Q2"]) / len(per[m]["Q2"]) > sum(per[m]["Q1"]) / len(per[m]["Q1"]))
    k = min(fell, rose)
    sign_p = 2 * sum(math.comb(fell + rose, i) for i in range(k + 1)) / 2 ** (fell + rose)
    say(f"members whose own basket fell {fell}, rose {rose}; sign test both ways {sign_p:.4f}")
    r1 = [sum(per[m]["Q1"]) for m in members]
    r2 = [sum(per[m]["Q2"]) for m in members]
    pool, real = r1 + r2, sum(r1) / len(r1) - sum(r2) / len(r2)
    rng = random.Random(7)
    hits_both = hits_one = 0
    for _ in range(2000):
        rng.shuffle(pool)
        g = sum(pool[:len(r1)]) / len(r1) - sum(pool[len(r1):]) / len(r2)
        hits_both += abs(g) >= abs(real) - 1e-9
        hits_one += g >= real - 1e-9
    say(f"pooled member-quarters dealt, 2,000 on Random(7): fall Rs {real:,.0f} per member, "
        f"p = {hits_both / 2000:.4f} either way, {hits_one / 2000:.4f} one way")
    rng = random.Random(7)
    d = [b - a for a, b in zip(r1, r2)]
    flips_both = 0
    for _ in range(2000):
        s = sum(x if rng.random() < 0.5 else -x for x in d)
        flips_both += abs(s) >= abs(sum(d)) - 1e-9
    say(f"paired flips on revenue per member, 2,000 on Random(7): p = {flips_both / 2000:.4f} either way")
    amts = sorted(r["amount"] for r in clean)
    mid = (amts[len(amts) // 2] + amts[(len(amts) - 1) // 2]) / 2
    say(f"typical order, clean: mean Rs {sum(amts) / len(amts):,.0f}, median Rs {mid:,.0f}")
    print("\n".join(out))


if __name__ == "__main__":
    main()

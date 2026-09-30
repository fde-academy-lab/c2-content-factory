"""The invented export behind every number the debrief shows: deck, chapter notebooks and study notes.

    python3 content/W01/D5/internal/C2_W01_D05_invented_export_INTERNAL.py

No learner file carries a number computed from the lab export (the fix pass of 30 September 2026
and the standard v3 recheck), so the debrief deck, the three chapter notebooks and the study notes
show each trap on this export instead, labelled invented wherever its numbers appear, and leave the
lab file's numbers to empty your-turn cells. It is built record by record, written to
data/C2_W01_D05_invented_orders_STUDENT.csv and data/C2_W01_D05_invented_control_STUDENT.csv for
the notebooks to load, read back from those files the way a notebook reads them, and every figure a
learner file quotes is computed here and asserted, never written by hand.

It carries the lab export's four defect families in other places and at other sizes: the batch
posted twice sits in Retail-Plus and one corporate order (the lab's sat in Retail-Core), the amount
that will not convert is a corporate order exported with its paise, "850000.00" (the lab's used
another form), the empty segment is a Q1 Retail-Core order (the lab's was a Q2 Retail-Plus order),
and the corporate book falls from five orders to two (the lab's from six to four). Its finding is
Retail-Plus's basket, where the lab's is Retail-Core's.

Retail-Plus's sixteen members place one, two or three orders a quarter, the same number in both
quarters, so members differ in size the way real customers do. That is what lets every chapter-3
mechanism show here: the paired test on each member's own two quarters finds the fall, pooling the
members' quarters reads it as chance, and shuffling single orders between segments blurs the gap.
The draw that deals Plus's orders to its members is seeded (MEMBER_SEEDS), and it was chosen with
that property, among the forty seeds tried, as recorded in the provenance. Nothing here is a Kalpa
record.
"""
import csv
import math
import pathlib
import random

DAY = pathlib.Path(__file__).resolve().parents[1]
ORDERS_CSV = DAY / "data" / "C2_W01_D05_invented_orders_STUDENT.csv"
CONTROL_CSV = DAY / "data" / "C2_W01_D05_invented_control_STUDENT.csv"

SEGMENTS = ("Retail-Core", "Retail-Plus", "Student", "Business")
QUARTERS = ("Q1", "Q2")
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
PLUS_ORDERS_PER_MEMBER = [1] * 4 + [2] * 8 + [3] * 4      # the same in both quarters
MEMBER_SEEDS = {"Q1": 36, "Q2": 1036}
TEXT_AMOUNT = "850000.00"
SEED = 2020
FLIPS, FLIP_SEED = 2000, 7


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
    for q in QUARTERS:
        for seg in SEGMENTS:
            n = PLAN[q][seg]
            vals = list(BUSINESS[q]) if seg == "Business" else amounts(rng, n, BANDS[(q, seg)], TOTALS[q][seg])
            for i in range(n):
                rows.append({"order_id": f"INV-{len(rows) + 1:04d}", "customer_id": f"{PREFIX[seg]}{i % CUSTOMERS[seg] + 1:02d}",
                             "segment": seg, "quarter": q, "amount": vals[i]})
    # Retail-Plus's orders dealt to its members: one, two or three a quarter each, the same in both.
    for q in QUARTERS:
        plus = [r for r in rows if r["quarter"] == q and r["segment"] == "Retail-Plus"]
        order = list(range(len(plus)))
        random.Random(MEMBER_SEEDS[q]).shuffle(order)
        k = 0
        for m, n in enumerate(PLUS_ORDERS_PER_MEMBER):
            for _ in range(n):
                plus[order[k]]["customer_id"] = f"P{m + 1:02d}"
                k += 1
    return rows


def as_exported(clean):
    rows = [dict(r) for r in clean]
    text = next(r for r in rows if r["quarter"] == "Q1" and r["amount"] == 850000)
    text["amount"] = TEXT_AMOUNT                      # a corporate order exported with its paise
    core_q1 = [r for r in rows if r["quarter"] == "Q1" and r["segment"] == "Retail-Core"]
    blank = core_q1[3]
    blank["segment"] = ""                              # its customer's other orders are Retail-Core
    plus_q2 = [r for r in rows if r["quarter"] == "Q2" and r["segment"] == "Retail-Plus"]
    batch = plus_q2[20:27] + [next(r for r in rows if r["amount"] == 1200000)]
    return rows + [dict(r) for r in batch], text, blank, batch


def write(rows, clean):
    ORDERS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with ORDERS_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["order_id", "customer_id", "segment", "quarter", "amount"])
        w.writeheader()
        w.writerows(rows)
    with CONTROL_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["quarter", "orders", "amount_rs"])
        for q in QUARTERS:
            w.writerow([q, sum(1 for r in clean if r["quarter"] == q), sum(r["amount"] for r in clean if r["quarter"] == q)])


def change(a, b):
    return 100 * (b / a - 1)


def read_value(text):
    t = str(text).strip().replace("Rs", "").replace(",", "").replace(" ", "")
    try:
        return round(float(t))
    except ValueError:
        return None


def members_of(rs):
    per = {}
    for r in rs:
        per.setdefault(r["customer_id"], {"Q1": [], "Q2": []})[r["quarter"]].append(r["amount"])
    return dict(sorted(per.items()))


def flipped(per, swaps, basket=True):
    q1r = q1n = q2r = q2n = 0
    for v, s in zip(per.values(), swaps):
        a, b = (v["Q2"], v["Q1"]) if s else (v["Q1"], v["Q2"])
        q1r, q1n, q2r, q2n = q1r + sum(a), q1n + len(a), q2r + sum(b), q2n + len(b)
    return change(q1r / q1n, q2r / q2n) if basket else change(q1r, q2r)


def paired(rs, basket=True, flips=FLIPS, seed=FLIP_SEED):
    per = members_of(rs)
    obs = flipped(per, [False] * len(per), basket)
    rng = random.Random(seed)
    worlds = [flipped(per, [rng.random() < 0.5 for _ in per], basket) for _ in range(flips)]
    both = sum(1 for w in worlds if abs(w) >= abs(obs) - 1e-9)
    one = sum(1 for w in worlds if w <= obs + 1e-9)
    return obs, both, one


def basket_change(rs):
    a = [r["amount"] for r in rs if r["quarter"] == "Q1"]
    b = [r["amount"] for r in rs if r["quarter"] == "Q2"]
    return change(sum(a) / len(a), sum(b) / len(b))


def main():
    clean = clean_orders()
    exported, text, blank, batch = as_exported(clean)
    write(exported, clean)

    # Everything below reads the two files back, the way a notebook meets them.
    with ORDERS_CSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    with CONTROL_CSV.open(encoding="utf-8") as f:
        book = {c["quarter"]: (int(c["amount_rs"]), int(c["orders"])) for c in csv.DictReader(f)}
    assert book == {"Q1": (4000000, 83), "Q2": (2600000, 84)}, book
    truth = change(book["Q1"][0], book["Q2"][0])
    out = []
    say = out.append

    def totals(src, zero_text):
        t = {}
        for q in QUARTERS:
            rs = [r for r in src if r["quarter"] == q]
            t[q] = (sum((int(r["amount"]) if r["amount"].isdigit() else 0) if zero_text else read_value(r["amount"])
                        for r in rs), len(rs))
        return t

    once = [r for i, r in enumerate(rows) if r["order_id"] not in {x["order_id"] for x in rows[:i]}]
    hurried, counted, fixed = totals(rows, True), totals(once, True), totals(once, False)
    assert fixed == book
    h, c = change(hurried["Q1"][0], hurried["Q2"][0]), change(counted["Q1"][0], counted["Q2"][0])
    set_aside = [r for i, r in enumerate(rows) if r["order_id"] in {x["order_id"] for x in rows[:i]}]
    repeats = sum(int(r["amount"]) for r in set_aside)
    as_read = hurried["Q1"][0] + hurried["Q2"][0]
    logged = [read_value(r["amount"]) for r in once if not r["amount"].isdigit()]
    say(f"profile: rows {len(rows)}, distinct ids {len({r['order_id'] for r in rows})}, amounts that convert "
        f"{sum(1 for r in rows if r['amount'].isdigit())}, distinct amounts {len({r['amount'] for r in rows})}, "
        f"segment present {sum(1 for r in rows if r['segment'])}")
    say(f"control: Q1 Rs {book['Q1'][0]:,} on {book['Q1'][1]}, Q2 Rs {book['Q2'][0]:,} on {book['Q2'][1]}, {truth:+.1f}%")
    say(f"hurried: Q1 Rs {hurried['Q1'][0]:,} on {hurried['Q1'][1]} rows, Q2 Rs {hurried['Q2'][0]:,} on "
        f"{hurried['Q2'][1]} rows, {h:+.1f}%, points off {abs(h - truth):.1f}")
    say(f"count check only: Q1 Rs {counted['Q1'][0]:,}, Q2 Rs {counted['Q2'][0]:,}, {c:+.1f}%, points off {abs(c - truth):.1f}")
    say(f"set aside: {len(set_aside)} rows, Rs {repeats:,}; the log: {len(logged)} line, Rs {sum(logged):,}")
    say(f"bridge: as read Rs {as_read:,} less Rs {repeats:,} plus Rs {sum(logged):,} = Rs {as_read - repeats + sum(logged):,}")
    say(f"text amount: {TEXT_AMOUNT!r} in Q1, {100 * sum(logged) / book['Q1'][0]:.2f}% of the quarter")
    say(f"value accounting: present {sum(1 for r in once if r['amount'])} = convertible "
        f"{sum(1 for r in once if r['amount'].isdigit())} + logged {len(logged)}")

    def seg_tree(src, q, seg):
        rs = [r for r in src if r["quarter"] == q and r["segment"] == seg and r["amount"].isdigit()]
        cust = len({r["customer_id"] for r in rs})
        rev = sum(int(r["amount"]) for r in rs)
        return len(rs), cust, len(rs) / cust, rev / len(rs), rev

    ph1, ph2 = seg_tree(rows, "Q1", "Retail-Plus"), seg_tree(rows, "Q2", "Retail-Plus")
    pc1, pc2 = seg_tree(once, "Q1", "Retail-Plus"), seg_tree(once, "Q2", "Retail-Plus")
    say(f"wrong branch, Plus hurried: frequency {ph1[2]:.2f} to {ph2[2]:.2f} ({change(ph1[2], ph2[2]):+.1f}%), "
        f"revenue Rs {ph1[4]:,} to Rs {ph2[4]:,} ({change(ph1[4], ph2[4]):+.1f}%)")
    say(f"Plus clean: frequency {pc1[2]:.2f} to {pc2[2]:.2f}, basket Rs {pc1[3]:,.0f} to Rs {pc2[3]:,.0f} "
        f"({change(pc1[3], pc2[3]):+.1f}%)")
    core_named = sum(int(r["amount"]) for r in once if r["quarter"] == "Q1" and r["segment"] == "Retail-Core")
    core_q2 = sum(int(r["amount"]) for r in once if r["quarter"] == "Q2" and r["segment"] == "Retail-Core")
    say(f"empty segment: Q1 order Rs {blank['amount']:,}; Core Q1 named Rs {core_named:,} on "
        f"{sum(1 for r in once if r['quarter'] == 'Q1' and r['segment'] == 'Retail-Core')} orders "
        f"({change(core_named, core_q2):+.1f}% to Q2's Rs {core_q2:,}), restored Rs {core_named + blank['amount']:,} "
        f"({change(core_named + blank['amount'], core_q2):+.1f}%)")

    # The clean data of chapter 3: one row per order, every value read, the empty segment restored.
    seg_of = {}
    for r in once:
        if r["segment"]:
            seg_of.setdefault(r["customer_id"], set()).add(r["segment"])
    tidy = []
    for r in once:
        r = dict(r, amount=read_value(r["amount"]))
        if not r["segment"] and len(seg_of.get(r["customer_id"], ())) == 1:
            r["segment"] = next(iter(seg_of[r["customer_id"]]))
        tidy.append(r)
    seg_rows = {s: [r for r in tidy if r["segment"] == s] for s in SEGMENTS}
    for s in SEGMENTS:
        t = {}
        for q in QUARTERS:
            rs = [r for r in seg_rows[s] if r["quarter"] == q]
            t[q] = (len(rs), len({r["customer_id"] for r in rs}), sum(r["amount"] for r in rs))
        say(f"tree {s}: orders {t['Q1'][0]} / {t['Q2'][0]}, customers {t['Q1'][1]} / {t['Q2'][1]}, "
            f"freq {t['Q1'][0] / t['Q1'][1]:.2f} / {t['Q2'][0] / t['Q2'][1]:.2f}, basket Rs {t['Q1'][2] / t['Q1'][0]:,.0f} / "
            f"Rs {t['Q2'][2] / t['Q2'][0]:,.0f}, revenue Rs {t['Q1'][2]:,} / Rs {t['Q2'][2]:,} ({change(t['Q1'][2], t['Q2'][2]):+.1f}%)")
    fall = book["Q1"][0] - book["Q2"][0]
    biz = sum(BUSINESS["Q1"]) - sum(BUSINESS["Q2"])
    plus_fall = TOTALS["Q1"]["Retail-Plus"] - TOTALS["Q2"]["Retail-Plus"]
    say(f"fall Rs {fall:,}; corporate Rs {biz:,} ({100 * biz / fall:.1f}%); Plus Rs {plus_fall:,} ({100 * plus_fall / fall:.1f}%)")
    n = 7
    uneven = sum(math.comb(n, k) for k in range(n + 1) if abs(2 * k - n) >= 3) / 2 ** n
    say(f"coin flips on 7 corporate orders: at least as uneven as 5 and 2 in {uneven:.3f}")

    plus = seg_rows["Retail-Plus"]
    obs, both, one = paired(plus)
    say(f"paired flips on Plus's members, 2,000 on Random(7): basket {obs:+.1f}%, {both} as large either way, "
        f"p = {both / FLIPS:.4f}; one way {one / FLIPS:.4f}")
    _, both20, one20 = paired(plus, flips=20000)
    per = members_of(plus)
    assert all(len(v["Q1"]) == len(v["Q2"]) for v in per.values())
    diffs = [sum(v["Q2"]) - sum(v["Q1"]) for v in per.values()]
    total_rev = sum(sum(v["Q1"]) + sum(v["Q2"]) for v in per.values())
    dist = {0: 1}
    for d in diffs:
        nxt = {}
        for s, k in dist.items():
            nxt[s + d] = nxt.get(s + d, 0) + k
            nxt[s - d] = nxt.get(s - d, 0) + k
        dist = nxt
    exact_both = sum(k for s, k in dist.items() if abs(change((total_rev - s) / 2, (total_rev + s) / 2)) >= abs(obs) - 1e-9)
    exact_one = sum(k for s, k in dist.items() if change((total_rev - s) / 2, (total_rev + s) / 2) <= obs + 1e-9)
    band = [paired(plus, seed=s)[1] / FLIPS for s in range(1, 21)]
    say(f"  20,000 flips {both20 / 20000:.4f} ({one20 / 20000:.4f} one way); exact over 2^16 {exact_both} of 65,536, "
        f"{exact_both / 2 ** 16:.4f} ({exact_one / 2 ** 16:.4f} one way); seeds 1 to 20 {min(band):.4f} to {max(band):.4f}")
    fell = sum(1 for v in per.values() if sum(v["Q2"]) / len(v["Q2"]) < sum(v["Q1"]) / len(v["Q1"]))
    rose = sum(1 for v in per.values() if sum(v["Q2"]) / len(v["Q2"]) > sum(v["Q1"]) / len(v["Q1"]))
    sign_p = 2 * sum(math.comb(fell + rose, i) for i in range(min(fell, rose) + 1)) / 2 ** (fell + rose)
    say(f"members whose own basket fell {fell}, rose {rose}; sign test both ways {sign_p:.4f}")
    r1 = [sum(v["Q1"]) for v in per.values()]
    r2 = [sum(v["Q2"]) for v in per.values()]
    real = sum(r1) / len(r1) - sum(r2) / len(r2)
    rng = random.Random(FLIP_SEED)
    pool, dealt = r1 + r2, []
    for _ in range(FLIPS):
        rng.shuffle(pool)
        dealt.append(sum(pool[:len(r1)]) / len(r1) - sum(pool[len(r1):]) / len(r2))
    p_pooled = sum(1 for g in dealt if abs(g) >= abs(real) - 1e-9) / FLIPS
    p_pooled_one = sum(1 for g in dealt if g >= real - 1e-9) / FLIPS
    rng = random.Random(FLIP_SEED)
    p_rev = sum(1 for _ in range(FLIPS)
                if abs(sum(d if rng.random() < 0.5 else -d for d in diffs)) >= abs(sum(diffs)) - 1e-9) / FLIPS
    say(f"revenue per member Rs {sum(r1) / len(r1):,.0f} to Rs {sum(r2) / len(r2):,.0f}: flipped p = {p_rev:.4f}; "
        f"pooled and dealt p = {p_pooled:.4f} ({p_pooled_one:.4f} one way)")
    q1o = [r["amount"] for r in plus if r["quarter"] == "Q1"]
    q2o = [r["amount"] for r in plus if r["quarter"] == "Q2"]
    rng = random.Random(FLIP_SEED)
    po, hits = q1o + q2o, 0
    for _ in range(FLIPS):
        rng.shuffle(po)
        hits += abs(change(sum(po[:len(q1o)]) / len(q1o), sum(po[len(q1o):]) / len(q2o))) >= abs(obs) - 1e-9
    p_qorders = hits / FLIPS
    say(f"quarter label dealt across Plus's {len(q1o) + len(q2o)} single orders: p = {p_qorders:.4f}")
    core = seg_rows["Retail-Core"]
    gap = basket_change(plus) - basket_change(core)
    groups = {}
    for r in plus + core:
        groups.setdefault(r["customer_id"], []).append(r)
    ids = sorted(groups)
    n_plus = len({r["customer_id"] for r in plus})
    rng = random.Random(FLIP_SEED)
    between = 0
    for _ in range(FLIPS):
        m = ids[:]
        rng.shuffle(m)
        between += abs(basket_change([r for c in m[:n_plus] for r in groups[c]])
                       - basket_change([r for c in m[n_plus:] for r in groups[c]])) >= abs(gap)
    both_rows = plus + core
    rng = random.Random(FLIP_SEED)
    singles = 0
    for _ in range(FLIPS):
        idx = list(range(len(both_rows)))
        rng.shuffle(idx)
        singles += abs(basket_change([both_rows[i] for i in idx[:len(plus)]])
                       - basket_change([both_rows[i] for i in idx[len(plus):]])) >= abs(gap)
    say(f"Plus against Core, gap {gap:+.1f} points: label across whole customers p = {between / FLIPS:.4f}; "
        f"across single orders p = {singles / FLIPS:.4f}")
    four = {s: paired(seg_rows[s], basket=False) for s in SEGMENTS}
    say("option D, one test per segment on revenue: " + "; ".join(
        f"{s} {o:+.1f}% p = {b / FLIPS:.4f}" for s, (o, b, _) in four.items()) + f"; one of four by luck {1 - 0.95 ** 4:.3f}")
    amts = sorted(r["amount"] for r in tidy)
    mid = (amts[len(amts) // 2] + amts[(len(amts) - 1) // 2]) / 2
    say(f"typical order, clean: mean Rs {sum(amts) / len(amts):,.0f}, median Rs {mid:,.0f}")
    print("\n".join(out))

    # Every figure a learner file quotes, asserted, so a change here cannot drift from them.
    assert (len(rows), len({r["order_id"] for r in rows}), len({r["amount"] for r in rows})) == (175, 167, 130)
    assert (hurried["Q1"], hurried["Q2"]) == ((3150000, 83), (3816420, 92))
    assert (round(h, 1), round(c, 1), round(truth, 1), round(abs(h - truth), 1)) == (21.2, -17.5, -35.0, 56.2)
    assert (len(set_aside), repeats, as_read, logged) == (8, 1216420, 6966420, [850000])
    assert (blank["amount"], core_named, core_q2, round(change(core_named, core_q2), 1)) == (2350, 73250, 74880, 2.2)
    assert (round(ph2[2], 2), round(change(ph1[4], ph2[4]), 1), round(change(pc1[3], pc2[3]), 1)) == (2.44, 2.1, -15.0)
    assert (biz, round(100 * biz / fall, 1), plus_fall, round(uneven, 3)) == (1388200, 99.2, 14400, 0.453)
    assert (both, one, both20, exact_both, fell, rose, round(sign_p, 4)) == (22, 3, 218, 704, 13, 3, 0.0213)
    assert (round(min(band), 4), round(max(band), 4)) == (0.0065, 0.0165)
    assert (round(p_rev, 4), round(p_pooled, 4), round(p_pooled_one, 4), round(p_qorders, 4)) == (0.0025, 0.222, 0.1125, 0.003)
    assert (round(gap, 1), between, singles) == (-14.0, 77, 189)
    assert [round(b / FLIPS, 4) for _, b, _ in four.values()] == [0.8275, 0.011, 0.06, 0.3705]
    assert (round(sum(amts) / len(amts)), mid) == (39521, 2350)


if __name__ == "__main__":
    main()

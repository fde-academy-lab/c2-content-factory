"""Write every Week 1 dataset for Kalpa Retail, deterministically, from one seed.

Section 7 of docs/07_Client_Zero.md fixes the versions and their planted witnesses. This script is
the only place those numbers exist, so a day pack reads data rather than inventing it, and all sixty
learners hold byte-identical files.

    python3 data/generate_client_zero.py --list
    python3 data/generate_client_zero.py --version v0 --out content/W01/D1/data --stem C2_W01_D01
    python3 data/generate_client_zero.py --all
    python3 data/generate_client_zero.py --contract

The world, so the numbers are readable
--------------------------------------
The extract is Kalpa Retail India for Q1 and Q2 of the current financial year. Kalpa Retail sells to
consumers through its app, website and stores, and it also sells in bulk to corporate buyers,
resellers and institutional accounts through the Business segment. A consumer order sits inside the
Rs 800 to Rs 3,000 band the locked file describes as the ordinary population. A Business order runs
from Rs 2 lakh to Rs 30 lakh, which is why one corporate customer can move an average and why the
finance controller says so on the first morning.

Every figure below is asserted at the end of generation. A change that misses a target fails loudly
rather than shipping a dataset whose story no longer matches the curriculum row.
"""
import argparse
import datetime
import csv
import json
import pathlib
import random
import sys

SEED = 20260928

SEGMENTS = ("Retail-Core", "Retail-Plus", "Business", "Student")
CHANNELS = ("app", "web", "store")
CITIES = ("Bengaluru", "Mumbai", "Delhi", "Chennai", "Hyderabad", "Pune")
STATUSES = ("delivered", "delivered", "delivered", "delivered", "returned", "cancelled")

# Consumer bands, in Rs. Retail-Plus members buy bigger baskets than Retail-Core, and Student is the
# thinnest. Business is the tail that carries the revenue.
BANDS = {
    "Retail-Core": (800, 3000),
    "Retail-Plus": (1200, 4500),
    "Student": (400, 1500),
    "Business": (200000, 1800000),
}

# The contract. Every one of these is asserted after generation.
Q1_RAW = 21000000        # Rs 2.10 crore, what the dashboard reports from the ERP export
Q1_CLEAN = 19000000      # Rs 1.90 crore, what Finance's books say once the duplicates go
Q2_TOTAL = 18700000      # Rs 1.87 crore, so the real drop is 1.6 percent rather than 9.5
DUPLICATE_ROWS = 14      # rows the Q1 migration duplicated
DISTINCT_ORDERS = 186
RAW_ROWS = 200
STUDENT_ORDERS = 12      # so an impressive Student rate rests on twelve observations
V0_ORDERS = 30
V0_BULK = 480000         # the corporate order that splits mean from median on the first morning

# Q1 and Q2 order counts per segment. Customers stay flat quarter on quarter; what moves is how
# often Retail-Plus members order.
PLAN = {
    "Q1": {"Student": 5, "Business": 18, "Retail-Plus": 40, "Retail-Core": 37},
    "Q2": {"Student": 7, "Business": 17, "Retail-Plus": 26, "Retail-Core": 36},
}

WITNESSES = {
    "v0": [
        ("one corporate bulk order of Rs 4,80,000", "W1 Mon, the mean sits far above the median"),
        ('one amount stored as the text "4500"', "W1 Mon, the type break in the accumulator"),
    ],
    "v1": [
        ("customer count flat quarter on quarter", "W1 Tue, acquisition is not the branch that moved"),
        ("orders per customer falls in Retail-Plus only", "W1 Tue, the frequency lever"),
        ("the discount field absent on a known subset", "W1 Tue, KeyError and .get() with a stated default"),
    ],
    "v2": [
        ("14 duplicated Q1 rows carrying Rs 20,00,000", "W1 Wed, the dashboard's 2.1 crore against Finance's 1.9"),
        ('one amount spelled "twelve"', "W1 Wed, a conversion that must not crash the pass"),
        ("one record missing a required field", "W1 Wed, the three-way missingness decision"),
        ("a near-duplicate pair sharing an order_id, differing on order_date", "W1 Wed, the identity rule"),
        ("a truncated line in the JSON feed", "W1 Wed, JSONDecodeError read aloud"),
        ("a companion export with the header row repeated", "W1 Wed, profiling before analysing"),
    ],
    "v3": [
        ("the Student segment holds exactly 12 orders", "W1 Thu, the sample-size rule of thumb"),
        ("the Retail-Plus gap is real but modest", "W1 Thu, statistically real against worth acting on"),
        ("the monsoon sale lifts the aggregate 6 percent while every segment falls",
         "W1 Thu, the confounder and Simpson's reversal in one table"),
    ],
    "v4": [
        ("the warehouse holds 1,000 orders where last week's extract held 186",
         "W2 Mon, the sample is not the book and the first query says so"),
        ("400 large invoices settled in two instalments, 50 more posted twice by the gateway",
         "W2 Tue, a LEFT JOIN grows 1,000 rows to 1,450 and the naive total doubles"),
        ("30 delivered orders never paid, and 8 payments whose order is not in the table",
         "W2 Tue, the anti-join both ways"),
        ("an exact Q2 revenue tie at the fiftieth Retail-Plus position",
         "W2 Wed, RANK ships 51 rows where ROW_NUMBER ships 50"),
        ("three Retail-Plus members whose monthly spend falls in each of the three Q2 months",
         "W2 Wed, two LAGs and a comparison"),
        ("6 duplicated customer keys in the exposure feed",
         "W2 Thu, validate='one_to_one' raises where the count check only reported"),
        ("one member id absent from the clean customer table",
         "W2 Fri, an approximate lookup returns the neighbour"),
    ],
}


# --------------------------------------------------------------------------- small helpers
def _rng():
    return random.Random(SEED)


def _date(rng, quarter, i):
    """A date inside the quarter. Q1 is April to June, Q2 is July to September."""
    month = {"Q1": (4, 5, 6), "Q2": (7, 8, 9)}[quarter][i % 3]
    day = 1 + (rng.randrange(28))
    return f"2026-{month:02d}-{day:02d}"


def _amount(rng, segment):
    low, high = BANDS[segment]
    if segment == "Business":
        return rng.randrange(low // 1000, high // 1000) * 1000
    return rng.randrange(low, high + 1, 10)


def _order_id(n):
    return f"KR-{n:05d}"


def _customer_id(n):
    return f"C-{n:04d}"


# --------------------------------------------------------------------------- v0, Monday
def build_v0():
    """Thirty orders pulled to get moving on the first morning.

    Twenty-nine ordinary consumer orders and one corporate order of Rs 4,80,000, so the mean lands
    an order of magnitude above the median. One amount is stored as text, which breaks the running
    total the first time the room writes one.
    """
    rng = _rng()
    rows = []
    mix = (["Retail-Core"] * 14) + (["Retail-Plus"] * 10) + (["Student"] * 5)
    rng.shuffle(mix)
    for i, seg in enumerate(mix):
        rows.append({
            "order_id": _order_id(1001 + i),
            "customer_id": _customer_id(101 + (i % 22)),
            "segment": seg,
            "channel": CHANNELS[i % 3],
            "order_date": _date(rng, "Q2", i),
            "amount": _amount(rng, seg),
            "status": STATUSES[i % len(STATUSES)],
        })
    rows.append({
        "order_id": _order_id(1031),
        "customer_id": _customer_id(140),
        "segment": "Business",
        "channel": "store",
        "order_date": "2026-08-14",
        "amount": V0_BULK,
        "status": "delivered",
    })
    # The type break. One amount arrives as text from the store terminal.
    rows[7]["amount"] = "4500"
    return rows


def build_v0b():
    """A second sample of the same shape for the take-home, with a different tail.

    Twenty-four orders, two corporate orders rather than one, so the mean-against-median gap is
    still there and the learner cannot reuse Monday's numbers.
    """
    rng = random.Random(SEED + 7)
    rows = []
    mix = (["Retail-Core"] * 11) + (["Retail-Plus"] * 8) + (["Student"] * 3)
    rng.shuffle(mix)
    for i, seg in enumerate(mix):
        rows.append({
            "order_id": _order_id(1501 + i),
            "customer_id": _customer_id(201 + (i % 17)),
            "segment": seg,
            "channel": CHANNELS[(i + 1) % 3],
            "order_date": _date(rng, "Q2", i),
            "amount": _amount(rng, seg),
            "status": STATUSES[(i + 2) % len(STATUSES)],
        })
    # The same type break as the class file, in a different row, so the defensive habit is rewarded.
    rows[12]["amount"] = str(rows[12]["amount"])
    for j, amt in enumerate((312000, 205000)):
        rows.append({
            "order_id": _order_id(1525 + j),
            "customer_id": _customer_id(240 + j),
            "segment": "Business",
            "channel": "store",
            "order_date": "2026-09-0%d" % (3 + j),
            "amount": amt,
            "status": "delivered",
        })
    return rows


# --------------------------------------------------------------------------- v1 and v2, the two quarters
def _customer_pool():
    """Customers per segment, fixed across both quarters so the count is flat.

    The Retail-Plus pool is the one the room is meant to find: the same members, ordering less often
    in Q2 than in Q1.
    """
    return {
        "Retail-Core": [_customer_id(2000 + i) for i in range(34)],
        "Retail-Plus": [_customer_id(3000 + i) for i in range(22)],
        "Business": [_customer_id(4000 + i) for i in range(11)],
        "Student": [_customer_id(5000 + i) for i in range(6)],
    }


def build_quarters():
    """186 distinct orders across Q1 and Q2, hitting the clean revenue targets exactly.

    Consumer amounts are drawn inside their bands. The Business amounts are drawn first and then one
    designated Business order per quarter absorbs the residual, so the quarter total lands on the
    figure the stakeholders quote rather than near it.
    """
    rng = _rng()
    pool = _customer_pool()
    rows, n = [], 0
    targets = {"Q1": Q1_CLEAN, "Q2": Q2_TOTAL}

    for quarter in ("Q1", "Q2"):
        plan = PLAN[quarter]
        quarter_rows, business_rows = [], []
        for seg in ("Retail-Core", "Retail-Plus", "Student", "Business"):
            for i in range(plan[seg]):
                n += 1
                customers = pool[seg]
                # Retail-Plus members order less often in Q2, so the same members spread thinner.
                idx = (i * 3) % len(customers) if seg != "Retail-Plus" else i % len(customers)
                row = {
                    "order_id": _order_id(2000 + n),
                    "customer_id": customers[idx],
                    "segment": seg,
                    "channel": CHANNELS[(n + i) % 3],
                    "city": CITIES[(n + i) % len(CITIES)],
                    "order_date": _date(rng, quarter, i),
                    "amount": _amount(rng, seg),
                    "status": STATUSES[n % len(STATUSES)],
                    "quarter": quarter,
                }
                if seg != "Student" and n % 4 != 0:
                    row["discount"] = rng.choice((0, 0, 50, 100, 150))
                quarter_rows.append(row)
                if seg == "Business":
                    business_rows.append(row)

        # Land the quarter exactly on its target by moving the residual into the last Business order.
        current = sum(r["amount"] for r in quarter_rows)
        residual = targets[quarter] - current
        anchor = business_rows[-1]
        anchor["amount"] += residual
        if not (BANDS["Business"][0] <= anchor["amount"] <= BANDS["Business"][1] * 3):
            sys.exit(f"FAIL  {quarter} residual put the anchor order at Rs {anchor['amount']:,}, "
                     f"which is outside a believable corporate order. Adjust PLAN or the bands.")
        rows.extend(quarter_rows)
    return rows


def build_v1():
    """The 200 rows as the ERP exported them: 186 distinct orders plus 14 duplicated Q1 rows.

    Tuesday reads this as a list of dictionaries because files arrive on Wednesday. The duplicates
    are already here and are not found until Wednesday, which is the point: Tuesday's conclusion is
    drawn on dirty data and Wednesday moves it.
    """
    rows = build_quarters()
    q1 = [r for r in rows if r["quarter"] == "Q1"]

    # Twelve ordinary duplicates and two large ones, summing to exactly the Rs 20 lakh gap.
    consumer_q1 = [r for r in q1 if r["segment"] != "Business"]
    business_q1 = [r for r in q1 if r["segment"] == "Business"]
    # A migration re-runs a batch, and a batch is not a random sample of the quarter. This one
    # re-ran the membership tier, so the duplicates sit almost entirely in Retail-Plus. That is what
    # makes Tuesday's finding overstated rather than wrong, and it is why Wednesday's clean pass
    # leaves Retail-Plus standing but smaller. Indices 0 to 36 are Retail-Core, 37 to 76 are
    # Retail-Plus, 77 onward are Student.
    picks = [consumer_q1[i] for i in (5, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68)]
    small = sum(r["amount"] for r in picks)
    gap = Q1_RAW - Q1_CLEAN
    big = [business_q1[3], business_q1[9]]
    # Give the two duplicated corporate orders the amounts that make the gap exact.
    half = (gap - small) // 2
    big[0]["amount"] = half
    big[1]["amount"] = (gap - small) - half
    # Those two orders are part of the clean quarter too, so the clean total has to be restored.
    anchor = [r for r in business_q1 if r is not big[0] and r is not big[1]][-1]
    anchor["amount"] = Q1_CLEAN - sum(r["amount"] for r in q1 if r is not anchor)

    duplicated = picks + big
    out = rows + [dict(r) for r in duplicated]
    return out


def build_v2():
    """Wednesday's raw exports: the same rows, plus the defects an ERP migration leaves behind."""
    rows = [dict(r) for r in build_v1()]
    rows[62]["amount"] = "twelve"                 # a word where a number belongs
    rows[118].pop("status", None)                  # a required field missing on one record
    near = dict(rows[150])                         # same order_id, different date
    near["order_date"] = "2026-08-02"
    rows.append(near)
    return rows


def build_v2b():
    """A second export for the take-home, with different defects from the class file.

    The learner cannot reuse Wednesday's reject counts, because the defects are not the same ones:
    a header row pasted into the middle of the body, a negative amount, a date in a second format,
    and duplicates that sit in a different segment.
    """
    rows = [dict(r) for r in build_quarters()][:90]
    for r in rows:
        r["amount"] = r["amount"]
    header = {k: k for k in rows[0]}          # the header line, read as a record
    rows.insert(44, header)
    rows[17]["amount"] = -2400                # a refund posted as a negative order
    rows[29]["order_date"] = "12/05/2026"     # the other date format, silently
    rows[52]["status"] = ""                   # nothing to classify it by
    dupes = [dict(rows[i]) for i in (3, 8, 21, 36, 61, 70)]
    return rows + dupes


# --------------------------------------------------------------------------- v3, Thursday
def build_v3():
    """The cleaned two quarters, and the campaigns table the discount question needs."""
    rows = [r for r in build_quarters()]
    return rows


def build_campaigns():
    """August's monsoon sale, and the exposure that makes the aggregate disagree with every segment.

    Revenue per exposed customer is 3 percent lower than per unexposed customer inside Retail-Plus,
    and 3 percent lower inside Retail-Core. The exposed group is half Retail-Plus against the
    control's 40 percent, and Retail-Plus spends more, so the blended figure comes out 6 percent
    higher. The campaign looks like it worked and every segment says it did not.
    """
    plus_ctrl, plus_treat = 5000, 4850
    core_ctrl, core_treat = 2000, 1940
    treated = [("Retail-Plus", 30, plus_treat), ("Retail-Core", 30, core_treat)]
    control = [("Retail-Plus", 40, plus_ctrl), ("Retail-Core", 60, core_ctrl)]

    rows = []
    cid = 6000
    for group, spec in (("treated", treated), ("control", control)):
        for seg, count, per in spec:
            for i in range(count):
                rows.append({
                    "customer_id": _customer_id(cid),
                    "segment": seg,
                    "exposed": "yes" if group == "treated" else "no",
                    "august_revenue": per,
                    "campaign_id": "CMP-MONSOON-26" if group == "treated" else "",
                })
                cid += 1
    return rows


CAMPAIGN_MASTER = [{
    "campaign_id": "CMP-MONSOON-26",
    "name": "Monsoon Sale",
    "target_segment": "Retail-Plus",
    "discount_pct": 15,
    "starts": "2026-08-05",
    "ends": "2026-08-19",
}]


# --------------------------------------------------------------------------- writing
# --------------------------------------------------------------------------- v4, Week 2
# The warehouse. Week 1 worked from a 200-row extract the data team sent before the room had
# database access, and the warehouse holds the whole two-quarter book those rows were sampled
# from. That is why Monday's first query does not match last week's note, and reconciling the two
# is Monday's opening move.
V4_ORDERS = 1000
V4_Q1_TOTAL = 100000000      # Rs 10.00 crore for Q1
V4_Q2_TOTAL = 98400000       # Rs 9.84 crore, the same 1.6 percent fall the sample showed
V4_UNPAID = 30               # delivered and never paid
V4_INSTALMENT = 400          # large invoices settled in two instalments
V4_RETRY = 50                # gateway retries that posted the same instalment a second time
V4_SINGLE = 520              # paid once, in full
V4_JOIN_ROWS = 1450          # 520 + 400x2 + 50x2 rows, plus the 30 unpaid on the NULL side
V4_ORPHANS = 8               # payments whose order_id is not in the orders table
V4_REFUNDS = 12              # refunds, kept in their own table so the join count stays exact
V4_TIE_RANK = 50             # an exact Q2 revenue tie at the fiftieth Retail-Plus position
V4_FALLING = 3               # members whose monthly spend fell two months running
V4_EXPOSURE_DUPES = 6        # duplicate customer keys so validate='one_to_one' raises

# Order counts per segment per quarter, the Week 1 plan at warehouse scale. Customers stay flat;
# what moves is how often Retail-Plus members order, which falls 34.9 percent.
V4_PLAN = {
    "Q1": {"Student": 27, "Business": 97, "Retail-Plus": 215, "Retail-Core": 199},
    "Q2": {"Student": 38, "Business": 91, "Retail-Plus": 140, "Retail-Core": 193},
}
V4_CUSTOMERS = {"Retail-Core": 150, "Retail-Plus": 120, "Business": 40, "Student": 30}
V4_METHODS = ("card", "upi", "netbanking", "wallet")


def _v4_month(quarter, i):
    return {"Q1": (4, 5, 6), "Q2": (7, 8, 9)}[quarter][i % 3]


def _v4_customers():
    """One stable pool used by both quarters, so customer count is flat and frequency is the mover."""
    rng = random.Random(SEED + 4)
    rows, n = [], 1
    for segment, count in V4_CUSTOMERS.items():
        for _ in range(count):
            rows.append({
                "customer_id": _customer_id(n),
                "segment": segment,
                "city": rng.choice(CITIES),
                "country": "IN",
                "joined_date": f"202{rng.randrange(3, 6)}-{rng.randrange(1, 13):02d}-"
                               f"{rng.randrange(1, 29):02d}",
            })
            n += 1
    return rows


def _v4_orders(customers):
    """1,000 orders whose quarter totals land exactly on the contract."""
    rng = random.Random(SEED + 5)
    by_segment = {}
    for c in customers:
        by_segment.setdefault(c["segment"], []).append(c)

    orders, n = [], 1
    for quarter in ("Q1", "Q2"):
        for segment, count in V4_PLAN[quarter].items():
            pool = by_segment[segment]
            for i in range(count):
                # A skewed draw: most orders spread across the pool, a third concentrated on
                # the heavy buyers, so a top-fifty list has a real shape to rank.
                cust = pool[rng.randrange(len(pool) // 3)] if rng.random() < 0.33 \
                    else pool[rng.randrange(len(pool))]
                orders.append({
                    "order_id": _order_id(n),
                    "customer_id": cust["customer_id"],
                    "order_date": f"2026-{_v4_month(quarter, i):02d}-{1 + rng.randrange(28):02d}",
                    "quarter": quarter,
                    "channel": rng.choice(CHANNELS),
                    "amount": _amount(rng, segment),
                    "status": rng.choice(STATUSES),
                    "_segment": segment,
                })
                n += 1
    return orders


def _v4_plant_falling(orders, customers):
    """Three Retail-Plus members whose monthly spend falls in each of the three Q2 months.

    Three Q2 orders are reassigned to each of them, one per month, on a descending ladder, so the
    order count does not move. Wednesday's LAG finds them. Nothing says so in a learner file.
    """
    # Members who have no Q2 order of their own, so the ladder is their whole quarter and the
    # month totals are not polluted by an order the draw happened to give them.
    busy = {o["customer_id"] for o in orders if o["quarter"] == "Q2"}
    plus = [c["customer_id"] for c in customers
            if c["segment"] == "Retail-Plus" and c["customer_id"] not in busy]
    chosen = plus[:V4_FALLING]
    ladders = [(4200, 3100, 1900), (3800, 2600, 1400), (4400, 2900, 1600)]
    pool = [o for o in orders
            if o["quarter"] == "Q2" and o["_segment"] == "Retail-Plus"
            and o["customer_id"] not in chosen]
    for k, (cid, ladder) in enumerate(zip(chosen, ladders)):
        for slot in range(3):
            o = pool[k * 3 + slot]
            o["customer_id"] = cid
            o["order_date"] = f"2026-{(7 + slot):02d}-{12 + slot:02d}"
            o["amount"] = ladder[slot]
    return orders, chosen


def _v4_plant_tie(orders, customers):
    """An exact Q2 revenue tie at the fiftieth Retail-Plus position.

    The head of Retail-Plus asks for the top fifty and for ties to rank the same, so the tie has to
    sit exactly on the boundary: RANK ships fifty-one rows and ROW_NUMBER ships fifty.
    """
    plus = {c["customer_id"] for c in customers if c["segment"] == "Retail-Plus"}
    spend = {}
    for o in orders:
        if o["quarter"] == "Q2" and o["customer_id"] in plus:
            spend[o["customer_id"]] = spend.get(o["customer_id"], 0) + o["amount"]
    ranked = sorted(spend.items(), key=lambda kv: (-kv[1], kv[0]))
    if len(ranked) <= V4_TIE_RANK:
        return None
    fiftieth, next_one = ranked[V4_TIE_RANK - 1], ranked[V4_TIE_RANK]
    gap = fiftieth[1] - next_one[1]
    theirs = [o for o in orders if o["customer_id"] == next_one[0] and o["quarter"] == "Q2"]
    theirs[0]["amount"] += gap
    return fiftieth[0], next_one[0], fiftieth[1]


def _v4_settle(orders):
    """Push each quarter's last Business order so the quarter total lands exactly on target."""
    for quarter, target in (("Q1", V4_Q1_TOTAL), ("Q2", V4_Q2_TOTAL)):
        here = [o for o in orders if o["quarter"] == quarter]
        anchor = [o for o in here if o["_segment"] == "Business"][-1]
        anchor["amount"] += target - sum(o["amount"] for o in here)
    return orders


def build_v4():
    """The warehouse: customers, orders, payments, refunds, campaign exposure and the plan line."""
    rng = random.Random(SEED + 6)
    customers = _v4_customers()
    orders = _v4_orders(customers)
    orders, falling = _v4_plant_falling(orders, customers)
    tie = _v4_plant_tie(orders, customers)
    orders = _v4_settle(orders)

    # Who pays how. The instalment set is the large invoices, because a corporate buyer settles a
    # big order in two parts, which is exactly why the fan-out doubles the number rather than
    # nudging it. The retries land on small orders so the doubling stays the fan-out's doing.
    delivered = [o for o in orders if o["status"] == "delivered"]
    by_value = sorted(orders, key=lambda o: -o["amount"])
    unpaid = {o["order_id"] for o in delivered[-V4_UNPAID:]}
    paid = [o for o in by_value if o["order_id"] not in unpaid]
    instalment = {o["order_id"] for o in paid[:V4_INSTALMENT]}
    rest = [o for o in paid[V4_INSTALMENT:]]
    retry = {o["order_id"] for o in rest[-V4_RETRY:]}

    payments, n = [], 1
    for o in orders:
        oid = o["order_id"]
        if oid in unpaid:
            continue
        base = f"2026-{int(o['order_date'][5:7]):02d}-{min(28, int(o['order_date'][8:10]) + 2):02d}"
        if oid in instalment:
            first = (o["amount"] * 6) // 10
            for k, amt in enumerate((first, o["amount"] - first)):
                payments.append({"payment_id": f"P-{n:05d}", "order_id": oid, "paid_date": base,
                                 "amount": amt, "method": rng.choice(V4_METHODS),
                                 "instalment_no": k + 1})
                n += 1
        elif oid in retry:
            for k in range(2):                     # the gateway posted the same amount twice
                payments.append({"payment_id": f"P-{n:05d}", "order_id": oid, "paid_date": base,
                                 "amount": o["amount"], "method": "card", "instalment_no": 1})
                n += 1
        else:
            payments.append({"payment_id": f"P-{n:05d}", "order_id": oid, "paid_date": base,
                             "amount": o["amount"], "method": rng.choice(V4_METHODS),
                             "instalment_no": 1})
            n += 1

    for k in range(V4_ORPHANS):                    # a payment whose order never reached this table
        payments.append({"payment_id": f"P-{n:05d}", "order_id": _order_id(90000 + k),
                         "paid_date": "2026-08-14", "amount": 2000 + 310 * k,
                         "method": "wallet", "instalment_no": 1})
        n += 1

    returned = [o for o in orders if o["status"] == "returned"][:V4_REFUNDS]
    refunds = [{"refund_id": f"R-{i + 1:04d}", "order_id": o["order_id"],
                "refund_date": o["order_date"], "amount": -o["amount"],
                "reason": rng.choice(("damaged", "wrong item", "late delivery"))}
               for i, o in enumerate(returned)]

    exposure, seen = [], []
    for c in customers:
        if c["segment"] in ("Retail-Plus", "Retail-Core") and rng.random() < 0.55:
            exposure.append({"customer_id": c["customer_id"], "campaign_id": "CMP-MONSOON-26",
                             "exposed_date": "2026-08-03"})
            seen.append(c["customer_id"])
    for cid in seen[:V4_EXPOSURE_DUPES]:           # the second feed re-sent the same customers
        exposure.append({"customer_id": cid, "campaign_id": "CMP-MONSOON-26",
                         "exposed_date": "2026-08-11"})

    plan = []
    week = datetime.date(2026, 7, 6)
    weekly = V4_Q2_TOTAL // 13
    for w in range(13):
        plan.append({"week_start": week.isoformat(), "plan_revenue": weekly})
        week += datetime.timedelta(days=7)

    for o in orders:
        o.pop("_segment", None)
    return {"customers": customers, "orders": orders, "payments": payments, "refunds": refunds,
            "campaign_exposure": exposure, "plan_line": plan,
            "_meta": {"unpaid": sorted(unpaid), "instalment": sorted(instalment),
                      "retry": sorted(retry), "tie": tie, "falling": falling}}



# --------------------------------------------------------------------------- the warehouse file
V4_SCHEMA = """-- Kalpa Retail warehouse, the two-quarter book Anand asks for every Monday.
-- Built by data/generate_client_zero.py. Load with: psql -f data/warehouse_v4.sql
-- payments carries no foreign key on purpose: the feed holds payments whose order never arrived.
-- campaign_exposure carries no primary key on purpose: the second feed re-sent some customers.
DROP TABLE IF EXISTS campaign_exposure, plan_line, refunds, payments, orders, campaigns, customers;

CREATE TABLE customers (
    customer_id  text PRIMARY KEY,
    segment      text NOT NULL,
    city         text NOT NULL,
    country      text NOT NULL,
    joined_date  date NOT NULL
);

CREATE TABLE orders (
    order_id     text PRIMARY KEY,
    customer_id  text NOT NULL REFERENCES customers (customer_id),
    order_date   date NOT NULL,
    quarter      text NOT NULL,
    channel      text NOT NULL,
    amount       numeric(12, 2) NOT NULL,
    status       text NOT NULL
);

CREATE TABLE payments (
    payment_id    text PRIMARY KEY,
    order_id      text NOT NULL,
    paid_date     date NOT NULL,
    amount        numeric(12, 2) NOT NULL,
    method        text NOT NULL,
    instalment_no integer NOT NULL
);

CREATE TABLE refunds (
    refund_id    text PRIMARY KEY,
    order_id     text NOT NULL,
    refund_date  date NOT NULL,
    amount       numeric(12, 2) NOT NULL,
    reason       text NOT NULL
);

CREATE TABLE campaigns (
    campaign_id  text PRIMARY KEY,
    name         text NOT NULL,
    start_date   date NOT NULL,
    end_date     date NOT NULL,
    segment      text NOT NULL
);

CREATE TABLE campaign_exposure (
    customer_id  text NOT NULL,
    campaign_id  text NOT NULL,
    exposed_date date NOT NULL
);

CREATE TABLE plan_line (
    week_start    date PRIMARY KEY,
    plan_revenue  numeric(14, 2) NOT NULL
);
"""

V4_TABLES = [
    ("customers", ("customer_id", "segment", "city", "country", "joined_date")),
    ("orders", ("order_id", "customer_id", "order_date", "quarter", "channel", "amount", "status")),
    ("campaigns", ("campaign_id", "name", "start_date", "end_date", "segment")),
    ("payments", ("payment_id", "order_id", "paid_date", "amount", "method", "instalment_no")),
    ("refunds", ("refund_id", "order_id", "refund_date", "amount", "reason")),
    ("campaign_exposure", ("customer_id", "campaign_id", "exposed_date")),
    ("plan_line", ("week_start", "plan_revenue")),
]

V4_CAMPAIGNS = [{"campaign_id": "CMP-MONSOON-26", "name": "Monsoon Sale",
                 "start_date": "2026-08-05", "end_date": "2026-08-19", "segment": "Retail-Plus"}]


def _v4_sql(tables):
    """The whole warehouse as one loadable file: schema, then a COPY block per table."""
    out = [V4_SCHEMA]
    for name, cols in V4_TABLES:
        rows = tables[name]
        out.append(f"COPY {name} ({', '.join(cols)}) FROM stdin;")
        for r in rows:
            out.append("\t".join(str(r[c]) for c in cols))
        out.append("\\.")
        out.append("")
    out.append("-- Row counts this file must load, which Monday's first query checks.")
    for name, _ in V4_TABLES:
        out.append(f"--   {name}: {len(tables[name])}")
    return "\n".join(out) + "\n"


def _v4_exports(tables):
    """Friday's two CSVs: the clean customer table, and the raw export that still double-counts."""
    seg = {c["customer_id"]: c for c in tables["customers"]}
    per_order = {}
    for p in tables["payments"]:
        per_order.setdefault(p["order_id"], []).append(p)

    clean, raw = {}, []
    for o in tables["orders"]:
        c = seg[o["customer_id"]]
        rec = clean.setdefault(o["customer_id"], {
            "customer_id": o["customer_id"], "segment": c["segment"], "city": c["city"],
            "orders": 0, "revenue": 0, "last_order_date": "2026-01-01"})
        rec["orders"] += 1
        rec["revenue"] += o["amount"]
        rec["last_order_date"] = max(rec["last_order_date"], o["order_date"])
        for p in per_order.get(o["order_id"], [{"amount": 0, "paid_date": ""}]):
            raw.append({"order_id": o["order_id"], "customer_id": o["customer_id"],
                        "segment": c["segment"], "channel": o["channel"],
                        "order_date": o["order_date"], "order_amount": o["amount"],
                        "paid_amount": p["amount"], "paid_date": p["paid_date"]})

    rows = sorted(clean.values(), key=lambda r: r["customer_id"])
    # One member id is absent from the clean table on purpose, so Friday's lookup has something
    # to fail on and the room sees an approximate match return the neighbour.
    missing = rows[len(rows) // 2]["customer_id"]
    rows = [r for r in rows if r["customer_id"] != missing]
    return rows, raw, missing


def _py_literal(name, rows):
    lines = [f"# Kalpa Retail, generated by data/generate_client_zero.py. Do not edit by hand.",
             f"{name} = ["]
    for r in rows:
        parts = []
        for k, v in r.items():
            parts.append(f'"{k}": ' + (f'"{v}"' if isinstance(v, str) else str(v)))
        lines.append("    {" + ", ".join(parts) + "},")
    lines.append("]")
    return "\n".join(lines) + "\n"


def _fieldnames(rows):
    seen = []
    for r in rows:
        for k in r:
            if k not in seen:
                seen.append(k)
    return seen


def _write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=_fieldnames(rows), extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write(version, out_dir, stem):
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    written = []

    if version == "v0":
        p = out / f"{stem}_orders_STUDENT.py"
        p.write_text(_py_literal("ORDERS", build_v0()), encoding="utf-8")
        written.append(p)
        q = out / f"{stem}_takehome_STUDENT.py"
        q.write_text(_py_literal("ORDERS", build_v0b()), encoding="utf-8")
        written.append(q)

    elif version == "v1":
        p = out / f"{stem}_orders_STUDENT.py"
        p.write_text(_py_literal("ORDERS", build_v1()), encoding="utf-8")
        written.append(p)

    elif version == "v2":
        rows = build_v2()
        p = out / f"{stem}_orders_STUDENT.csv"
        _write_csv(p, rows)
        written.append(p)

        # The app's JSON feed, truncated mid-string on one line the way a cut transfer leaves it.
        j = out / f"{stem}_orders_STUDENT.json"
        body = json.dumps(rows[:120], indent=1)
        cut = body.rfind('"order_id"')
        j.write_text(body[:cut + 18], encoding="utf-8")
        written.append(j)

        # The companion export whose header row was pasted in twice.
        tk = out / f"{stem}_takehome_STUDENT.csv"
        _write_csv(tk, build_v2b())
        written.append(tk)

        c = out / f"{stem}_vendor_STUDENT.csv"
        text = (out / f"{stem}_orders_STUDENT.csv").read_text(encoding="utf-8").splitlines()
        c.write_text("\n".join([text[0], text[0]] + text[1:40]) + "\n", encoding="utf-8")
        written.append(c)

    elif version == "v3":
        p = out / f"{stem}_orders_STUDENT.csv"
        _write_csv(p, build_v3())
        written.append(p)
        e = out / f"{stem}_exposure_STUDENT.csv"
        _write_csv(e, build_campaigns())
        written.append(e)
        m = out / f"{stem}_campaigns_STUDENT.csv"
        _write_csv(m, CAMPAIGN_MASTER)
        written.append(m)

    elif version == "v4":
        tables = build_v4()
        tables["campaigns"] = V4_CAMPAIGNS
        p = out / f"{stem}_warehouse_v4_STUDENT.sql"
        p.write_text(_v4_sql(tables), encoding="utf-8")
        written.append(p)

        # Thursday reads the exposure feed as a file, because the fan-out has to be met in pandas
        # as well as in SQL, and Friday reads the two exports.
        thu = pathlib.Path("content/W02/D4/data")
        thu.mkdir(parents=True, exist_ok=True)
        e = thu / "C2_W02_D04_exposure_STUDENT.csv"
        _write_csv(e, tables["campaign_exposure"])
        written.append(e)

        clean, raw, missing = _v4_exports(tables)
        fri = pathlib.Path("content/W02/D5/data")
        fri.mkdir(parents=True, exist_ok=True)
        c = fri / "C2_W02_D05_customer_table_STUDENT.csv"
        _write_csv(c, clean)
        written.append(c)
        r = fri / "C2_W02_D05_raw_export_STUDENT.csv"
        _write_csv(r, raw)
        written.append(r)

    else:
        sys.exit(f"FAIL  unknown version {version}")

    for p in written:
        print("wrote", p)
    return written


# --------------------------------------------------------------------------- the contract
def contract():
    """Assert every figure the Week 1 rows quote. Any miss is a FAIL with the two numbers."""
    fails = 0

    def want(label, got, expected):
        nonlocal fails
        ok = got == expected
        print(f"  {'PASS' if ok else 'FAIL'}  {label}: {got:,} against {expected:,}")
        if not ok:
            fails += 1

    v0 = build_v0()
    nums = sorted(int(r["amount"]) for r in v0)
    mid = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
    mean = sum(nums) / len(nums)
    print("v0, Monday")
    want("orders", len(v0), V0_ORDERS)
    want("the corporate order", max(nums), V0_BULK)
    print(f"  INFO  mean Rs {mean:,.0f} against median Rs {mid:,.0f}, "
          f"a factor of {mean / mid:.0f}")
    if mean / mid < 5:
        print("  FAIL  the mean does not sit far enough above the median to carry the lesson")
        fails += 1
    if sum(1 for r in v0 if isinstance(r["amount"], str)) != 1:
        print("  FAIL  exactly one amount must be stored as text")
        fails += 1

    v1 = build_v1()
    q1 = [r for r in v1 if r["quarter"] == "Q1"]
    q2 = [r for r in v1 if r["quarter"] == "Q2"]
    ids = [r["order_id"] for r in v1]
    print("v1 and v2, the two quarters")
    want("rows in the export", len(v1), RAW_ROWS)
    want("distinct order ids", len(set(ids)), DISTINCT_ORDERS)
    want("duplicated rows", len(ids) - len(set(ids)), DUPLICATE_ROWS)
    want("Q1 as exported", sum(r["amount"] for r in q1), Q1_RAW)
    want("Q2 total", sum(r["amount"] for r in q2), Q2_TOTAL)

    seen, clean = set(), []
    for r in v1:
        if r["order_id"] not in seen:
            seen.add(r["order_id"])
            clean.append(r)
    want("Q1 once deduplicated", sum(r["amount"] for r in clean if r["quarter"] == "Q1"), Q1_CLEAN)

    def per_customer(rows, seg):
        rs = [r for r in rows if r["segment"] == seg]
        return len(rs) / len(set(r["customer_id"] for r in rs))

    c1 = len(set(r["customer_id"] for r in clean if r["quarter"] == "Q1"))
    c2 = len(set(r["customer_id"] for r in clean if r["quarter"] == "Q2"))
    print(f"  INFO  customers Q1 {c1} against Q2 {c2}")
    if abs(c1 - c2) > 2:
        print("  FAIL  the customer count has to read as flat quarter on quarter")
        fails += 1
    q1c = [r for r in clean if r["quarter"] == "Q1"]
    q2c = [r for r in clean if r["quarter"] == "Q2"]
    for seg in ("Retail-Core", "Retail-Plus"):
        a, b = per_customer(q1c, seg), per_customer(q2c, seg)
        print(f"  INFO  orders per customer, {seg}: {a:.2f} then {b:.2f}, {100 * (b - a) / a:+.1f}%")
    overall_1 = len(q1c) / len(set(r["customer_id"] for r in q1c))
    overall_2 = len(q2c) / len(set(r["customer_id"] for r in q2c))
    print(f"  INFO  orders per customer overall: {overall_1:.2f} then {overall_2:.2f}, "
          f"{100 * (overall_2 - overall_1) / overall_1:+.1f}%")
    plus = per_customer(q2c, "Retail-Plus") / per_customer(q1c, "Retail-Plus")
    core = per_customer(q2c, "Retail-Core") / per_customer(q1c, "Retail-Core")
    if overall_2 >= overall_1:
        print("  FAIL  orders per customer has to fall overall, or there is no drop to investigate")
        fails += 1
    if not (plus < 0.80 and core > 0.90):
        print("  FAIL  the frequency fall has to sit in Retail-Plus and not in Retail-Core")
        fails += 1
    def opc(rows, seg=None):
        rs = [r for r in rows if seg is None or r["segment"] == seg]
        return len(rs) / len(set(r["customer_id"] for r in rs))

    raw_q1 = [r for r in v1 if r["quarter"] == "Q1"]
    raw_q2 = [r for r in v1 if r["quarter"] == "Q2"]
    print("  INFO  as exported, before anybody cleans it:")
    for seg in ("Retail-Core", "Retail-Plus", "Business", "Student"):
        a, b = opc(raw_q1, seg), opc(raw_q2, seg)
        print(f"          {seg:14s} {a:.2f} then {b:.2f}, {100 * (b - a) / a:+.1f}%")
    dirty_plus = 100 * (opc(raw_q2, "Retail-Plus") / opc(raw_q1, "Retail-Plus") - 1)
    dirty_core = 100 * (opc(raw_q2, "Retail-Core") / opc(raw_q1, "Retail-Core") - 1)
    if not (dirty_plus < -35 and dirty_core > -10):
        print("  FAIL  on the exported file the fall has to read as Retail-Plus, with Core near flat")
        fails += 1
    clean_plus = 100 * (per_customer(q2c, "Retail-Plus") / per_customer(q1c, "Retail-Plus") - 1)
    print(f"  INFO  Retail-Plus falls {dirty_plus:.0f}% as exported and {clean_plus:.0f}% once "
          f"deduplicated, so Wednesday leaves it standing but smaller")
    if not clean_plus > dirty_plus:
        print("  FAIL  cleaning has to shrink the Retail-Plus fall rather than deepen it")
        fails += 1

    missing_discount = sum(1 for r in clean if "discount" not in r)
    print(f"  INFO  records with no discount field: {missing_discount}")
    if missing_discount < 20:
        print("  FAIL  the absent discount field needs a large enough subset to be met by accident")
        fails += 1

    v2 = build_v2()
    print("v2 defects")
    for label, ok in (
        ('one amount spelled "twelve"', sum(1 for r in v2 if r.get("amount") == "twelve") == 1),
        ("one record missing a required field", sum(1 for r in v2 if "status" not in r) == 1),
        ("a near-duplicate pair on one id", len(v2) == RAW_ROWS + 1),
    ):
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        fails += 0 if ok else 1

    print("v3, Thursday")
    v3 = build_v3()
    want("Student orders", sum(1 for r in v3 if r["segment"] == "Student"), STUDENT_ORDERS)
    camp = build_campaigns()

    def blended(flag):
        rs = [r for r in camp if r["exposed"] == flag]
        return sum(r["august_revenue"] for r in rs) / len(rs)

    def within(flag, seg):
        rs = [r for r in camp if r["exposed"] == flag and r["segment"] == seg]
        return sum(r["august_revenue"] for r in rs) / len(rs)

    lift = 100 * (blended("yes") / blended("no") - 1)
    print(f"  INFO  blended revenue per customer: exposed Rs {blended('yes'):,.0f} against "
          f"Rs {blended('no'):,.0f}, {lift:+.1f}%")
    if not 5.0 <= lift <= 7.0:
        print("  FAIL  the aggregate lift has to read as about 6 percent")
        fails += 1
    for seg in ("Retail-Plus", "Retail-Core"):
        d = 100 * (within("yes", seg) / within("no", seg) - 1)
        print(f"  INFO  within {seg}: {d:+.1f}%")
        if d >= 0:
            print(f"  FAIL  {seg} has to fall when the aggregate rises")
            fails += 1

    print()
    # ---------------------------------------------------------------- v4, the Week 2 warehouse
    from collections import Counter
    w = build_v4()
    orders, payments, customers = w["orders"], w["payments"], w["customers"]
    seg = {c["customer_id"]: c["segment"] for c in customers}
    ids = {o["order_id"] for o in orders}
    amount = {o["order_id"]: o["amount"] for o in orders}
    per = Counter(p["order_id"] for p in payments)

    want("v4 orders in the warehouse", len(orders), V4_ORDERS)
    want("v4 Q1 revenue", sum(o["amount"] for o in orders if o["quarter"] == "Q1"), V4_Q1_TOTAL)
    want("v4 Q2 revenue", sum(o["amount"] for o in orders if o["quarter"] == "Q2"), V4_Q2_TOTAL)
    want("v4 rows a LEFT JOIN to payments returns",
         sum(max(1, per.get(i, 0)) for i in ids), V4_JOIN_ROWS)
    want("v4 orders with no payment at all", sum(1 for i in ids if per.get(i, 0) == 0), V4_UNPAID)
    want("v4 payments whose order is not in the table",
         sum(1 for p in payments if p["order_id"] not in ids), V4_ORPHANS)
    want("v4 orders carrying more than one payment row",
         sum(1 for i in ids if per.get(i, 0) > 1), V4_INSTALMENT + V4_RETRY)

    paid_book = sum(amount[i] for i in ids if per.get(i, 0) > 0)
    naive = sum(amount[i] * per[i] for i in ids if per.get(i, 0) > 0)
    ratio = naive / paid_book
    ok = 1.95 <= ratio <= 2.05
    print(f"  {'PASS' if ok else 'FAIL'}  v4 the naive total over the join against the true book: "
          f"{ratio:.4f} times, and the day needs it to read as double")
    if not ok:
        fails += 1

    plus_q2 = {}
    for o in orders:
        if o["quarter"] == "Q2" and seg[o["customer_id"]] == "Retail-Plus":
            plus_q2[o["customer_id"]] = plus_q2.get(o["customer_id"], 0) + o["amount"]
    ranked = sorted(plus_q2.values(), reverse=True)
    want("v4 Retail-Plus members with a Q2 spend to rank", len(ranked) > V4_TIE_RANK, True)
    tie = ranked[V4_TIE_RANK - 1] == ranked[V4_TIE_RANK]
    print(f"  {'PASS' if tie else 'FAIL'}  v4 an exact tie at the fiftieth Retail-Plus position: "
          f"{ranked[V4_TIE_RANK - 1]:,} against {ranked[V4_TIE_RANK]:,}")
    if not tie:
        fails += 1

    falling = 0
    for cid in {o["customer_id"] for o in orders if seg[o["customer_id"]] == "Retail-Plus"}:
        months = {}
        for o in orders:
            if o["customer_id"] == cid and o["quarter"] == "Q2":
                months[o["order_date"][5:7]] = months.get(o["order_date"][5:7], 0) + o["amount"]
        v = [months.get(mm) for mm in ("07", "08", "09")]
        if all(v) and v[0] > v[1] > v[2]:
            falling += 1
    want("v4 Retail-Plus members whose spend fell in each of the three Q2 months",
         falling, V4_FALLING)

    ec = Counter(e["customer_id"] for e in w["campaign_exposure"])
    want("v4 duplicated customer keys in the exposure feed",
         sum(1 for n in ec.values() if n > 1), V4_EXPOSURE_DUPES)

    w["campaigns"] = V4_CAMPAIGNS
    clean, raw, missing = _v4_exports(w)
    want("v4 rows in Friday's raw export", len(raw), V4_JOIN_ROWS)
    gone = missing not in {r["customer_id"] for r in clean}
    print(f"  {'PASS' if gone else 'FAIL'}  v4 one member id absent from the clean table "
          f"so Friday's lookup has something to fail on: {missing}")
    if not gone:
        fails += 1

    print("RESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    return fails


TARGETS = {
    "v0": ("content/W01/D1/data", "C2_W01_D01"),
    "v1": ("content/W01/D2/data", "C2_W01_D02"),
    "v2": ("content/W01/D3/data", "C2_W01_D03"),
    "v3": ("content/W01/D4/data", "C2_W01_D04"),
    "v4": ("content/W02/D1/data", "C2_W02_D01"),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--version", choices=sorted(TARGETS))
    ap.add_argument("--out")
    ap.add_argument("--stem")
    ap.add_argument("--all", action="store_true", help="write every version to its day folder")
    ap.add_argument("--list", action="store_true", help="print every version and what is planted")
    ap.add_argument("--contract", action="store_true",
                    help="assert every figure the Week 1 curriculum rows quote")
    a = ap.parse_args()

    if a.list:
        for v, items in WITNESSES.items():
            print(v)
            for what, why in items:
                print(f"    {what:62s} {why}")
        return
    if a.contract:
        sys.exit(1 if contract() else 0)
    if a.all:
        for v, (out, stem) in TARGETS.items():
            write(v, out, stem)
        return
    if not (a.version and a.out and a.stem):
        sys.exit("FAIL  give --version with --out and --stem, or --all, or --contract")
    write(a.version, a.out, a.stem)


if __name__ == "__main__":
    main()

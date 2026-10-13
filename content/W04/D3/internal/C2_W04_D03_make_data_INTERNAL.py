"""Generate the Wednesday case data and the Kalpa transfer tables, then write the facts file.

Run from the repository root:
    python3 content/W04/D3/internal/C2_W04_D03_make_data_INTERNAL.py

One seeded, deterministic generator; pandas and the standard library only. Every target the case
file sets is built as an exact count and then asserted, so a second run writes the same bytes.

The case, Swiggy Instamart in Pune (illustrative: the company is real, the data are synthetic):
    C2_W04_D03_carts_STUDENT.csv          40,000 carts, every September cart of 12,000 sampled customers
    C2_W04_D03_cart_items_STUDENT.csv     one line per item in a cart, 59 items, price and margin per unit
    C2_W04_D03_strip_log_STUDENT.csv      the strip's daily impressions, clicks and adds, 17 Aug to 27 Sep
    C2_W04_D03_twelve_rows_STUDENT.csv    twelve real carts from the 40,000, for the hand count

The concept chapters' invented examples, each labelled invented wherever it appears:
    C2_W04_D03_canteen_order_lines_STUDENT.csv  a hostel canteen's twelve lunch orders, 33 lines (SECTIONs 1 to 6)
    C2_W04_D03_canteen_month_STUDENT.csv        600 orders of the same canteen, no item depending on another (SECTION 6)
    C2_W04_D03_kirana_month_STUDENT.csv         Sharma Kirana's month and its combo card, as eleven lines (SECTION 9)

The Kalpa transfer, Kalpa Retail's v5 additions on v4's own 1,000 orders (TRAINER until the lab):
    C2_W04_D03_kalpa_products_STUDENT.csv     fifteen products, the Rs 199 charger among them
    C2_W04_D03_kalpa_orders_STUDENT.csv       v4's 1,000 orders as data/generate_client_zero.py builds them
    C2_W04_D03_kalpa_order_items_STUDENT.csv  every order's lines, summing to its amount exactly

Corrections to the case file, each recorded in the facts file:
    milk's share of slot impressions after the change is 50 percent, since 44 percent beside the
    1.2 and 6.4 percent slot rates blends to 4.1 percent and the ticket's after rate is 3.8;
    the twelve carts put milk in all four bread carts (confidence 1.00, lift 1.50), since the case
    file's 0.75 sits 0.01 from the full-data 0.74 and the spine wants five points between them;
    the three-slot rupee figure is what re-ranking recovers on milk's half of the impressions
    (Rs 6.3 lakh a month), since the case file's Rs 12.6 lakh assumed every slot showed milk.
"""
import math
import random
import re
import sys
from collections import Counter
from datetime import date, timedelta
from itertools import combinations
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
DATA = HERE.parent / "data"
FACTS = HERE / "C2_W04_D03_facts_INTERNAL.yaml"
sys.path.insert(0, str(REPO / "data"))
import generate_client_zero as cz  # noqa: E402

SEED = 20261028
N_CARTS = 40_000
MONTH = [date(2026, 9, 1) + timedelta(days=i) for i in range(28)]   # 1 to 28 September 2026
CHANGE_DAY = date(2026, 9, 7)
LOG_DAYS = [date(2026, 8, 17) + timedelta(days=i) for i in range(42)]  # 17 Aug to 27 Sep 2026

ZONES = {"Kothrud": 16, "Baner": 14, "Hinjewadi": 14, "Hadapsar": 13, "Viman Nagar": 12,
         "Aundh": 12, "Kalyani Nagar": 11, "Camp": 8}
STOCKOUT_ZONES = ("Hadapsar", "Viman Nagar")
STOCKOUT_DAYS = (date(2026, 9, 15), date(2026, 9, 21))              # week three
BANDS = {"morning": 10_000, "afternoon": 10_000, "evening": 15_000, "night": 5_000}
MILK_BY_BAND = {"morning": 0.80, "afternoon": 0.69, "evening": 0.68, "night": 0.66}

# The catalogue: item, price per unit in Rs, margin per unit in Rs, carts holding it (of 40,000).
CATALOGUE = [
    ("toned milk", 29, 2.0, 28_400), ("bread", 45, 6.3, 13_600), ("eggs", 48, 5.8, 11_600),
    ("curd", 40, 4.8, 10_400), ("bananas", 45, 9.0, 9_200), ("onions", 38, 7.6, 8_800),
    ("tomatoes", 22, 4.4, 8_000), ("potatoes", 34, 6.8, 7_200), ("coriander", 15, 4.5, 6_000),
    ("chips", 20, 4.0, 4_800), ("cold drink", 40, 8.0, 4_920), ("green chillies", 10, 3.0, 3_200),
    ("paneer", 90, 10.8, 3_200), ("butter", 58, 4.6, 2_400), ("ice cream", 160, 40.0, 1_600),
    ("chocolate sauce", 175, 35.0, 544), ("biscuits", 30, 4.5, 4_000), ("atta", 240, 14.4, 3_600),
    ("sugar", 46, 2.8, 2_800), ("ginger", 18, 4.5, 2_800), ("tea", 140, 14.0, 2_600),
    ("rice", 80, 6.4, 2_400), ("lemons", 20, 5.0, 2_400), ("garlic", 30, 6.0, 2_400),
    ("apples", 120, 21.6, 2_400), ("maggi noodles", 56, 5.6, 2_400), ("toor dal", 160, 9.6, 2_000),
    ("cucumber", 25, 5.0, 2_000), ("spinach", 25, 6.3, 2_000), ("namkeen", 55, 9.9, 2_000),
    ("poha", 40, 5.2, 1_800), ("chocolate bar", 50, 9.0, 1_800), ("capsicum", 30, 6.0, 1_600),
    ("carrots", 35, 7.0, 1_600), ("sunflower oil", 155, 9.3, 1_600), ("pav", 35, 5.3, 1_600),
    ("dish soap", 99, 17.8, 1_400), ("ketchup", 110, 13.2, 1_200), ("cheese slices", 120, 12.0, 1_200),
    ("rusk", 45, 6.8, 1_200), ("detergent", 210, 29.4, 1_200), ("bath soap", 160, 24.0, 1_200),
    ("curry leaves", 10, 3.0, 1_200), ("ghee", 320, 22.4, 1_000), ("peanuts", 60, 7.2, 1_000),
    ("toothpaste", 105, 15.8, 1_000), ("coffee", 190, 22.8, 800), ("shampoo", 180, 27.0, 800),
    ("tissues", 99, 19.8, 800), ("sanitary pads", 199, 29.9, 800), ("green peas", 45, 9.0, 800),
    ("mint", 10, 3.0, 800), ("jaggery", 70, 8.4, 600), ("diapers", 450, 49.5, 600),
    ("mosquito repellent", 85, 14.5, 600), ("sabudana", 60, 7.2, 480), ("ice cubes", 40, 10.0, 400),
    ("paper cups", 60, 15.0, 360), ("batteries", 120, 24.0, 320),
]
PRICE = {name: p for name, p, _, _ in CATALOGUE}
TARGET = {name: n for name, _, _, n in CATALOGUE}
# Margins scaled so a line in cart_items, milk aside, earns Rs 9 on average: the slot's margin per add.
_raw = {name: m for name, _, m, _ in CATALOGUE}
_lines = sum(TARGET[x] for x in TARGET if x != "toned milk")
_scale = 9.0 / (sum(TARGET[x] * _raw[x] for x in TARGET if x != "toned milk") / _lines)
MARGIN = {x: (_raw[x] if x == "toned milk" else round(_raw[x] * _scale, 1)) for x in _raw}

# Carts holding both items of each designed pair, and the share of those carts that hold milk.
BREAD_MILK, EGGS_MILK, CURD_MILK, BANANAS_MILK = 10_064, 8_468, 7_436, 6_624
PAIRS = {("chips", "cold drink"): 2_000, ("coriander", "green chillies"): 1_440,
         ("bread", "butter"): 1_800, ("onions", "tomatoes"): 3_000,
         ("chocolate sauce", "ice cream"): 100}

# The twelve printed carts, kept as the drafting session designed them: milk in 8, bread in 4 and
# every bread cart with milk, chips and cold drink in 3 each and together in 2, ice cream and
# chocolate sauce together in one cart. They are real carts of the 40,000.
TWELVE = [
    ["toned milk", "bread", "eggs", "bananas", "coriander", "onions", "potatoes"],
    ["toned milk", "bread", "eggs", "curd", "bananas"],
    ["toned milk", "bread", "curd", "paneer", "onions"],
    ["toned milk", "bread", "eggs", "tomatoes"],
    ["toned milk", "eggs", "chips", "cold drink", "onions"],
    ["toned milk", "chips", "cold drink", "coriander"],
    ["toned milk", "bananas", "onions", "potatoes"],
    ["toned milk", "paneer", "coriander", "tomatoes"],
    ["chips", "coriander", "onions", "potatoes"],
    ["cold drink", "curd", "bananas", "tomatoes"],
    ["eggs", "ice cream", "chocolate sauce"],
    ["curd", "onions"],
]
TWELVE_ITEMS = sorted({i for cart in TWELVE for i in cart})


# =========================================================================== small helpers
def pick(rng, pool, k, weight=None):
    """k distinct members of pool, weighted when a weight function is given (Efraimidis-Spirakis)."""
    if k < 0 or k > len(pool):
        raise AssertionError(f"cannot pick {k} from {len(pool)}")
    if weight is None:
        return rng.sample(pool, k)
    keyed = [(rng.random() ** (1.0 / weight(i)), i) for i in pool]
    keyed.sort(reverse=True)
    return [i for _, i in keyed[:k]]


def split_counts(total, weights, rng=None, noise=0.0):
    """Integers proportional to weights (times a little seeded noise) that sum to total exactly."""
    w = [x * (1 + (rng.uniform(-noise, noise) if rng else 0)) for x in weights]
    raw = [total * x / sum(w) for x in w]
    out = [math.floor(r) for r in raw]
    order = sorted(range(len(raw)), key=lambda i: raw[i] - out[i], reverse=True)
    for i in order[:total - sum(out)]:
        out[i] += 1
    return out


def check(label, ok, shown=""):
    if not ok:
        raise AssertionError(f"FAIL {label} {shown}")
    print(f"PASS {label} {shown}".rstrip())


# =========================================================================== the carts
def build_carts(rng):
    """Customers, dates, zones and time bands for 40,000 carts, before any item is placed."""
    heavy = [12] * 520 + [13] * 560 + [14] * 120                      # 1,200 customers, 15,200 carts
    light = [1] * 3_750 + [2] * 3_000 + [3] * 1_950 + [4] * 1_300 + [5] * 800   # 10,800 and 24,800
    counts = heavy + light
    ids = [f"PC{n:05d}" for n in range(1, len(counts) + 1)]
    rng.shuffle(ids)
    customers = [{"customer_id": cid, "heavy": i < len(heavy), "carts": n,
                  "zone": rng.choices(list(ZONES), weights=list(ZONES.values()))[0]}
                 for i, (cid, n) in enumerate(zip(ids, counts))]
    slots = [c for c in customers for _ in range(c["carts"])]
    rng.shuffle(slots)

    # Daily carts move with the week (weekends busier) and a few percent of noise.
    dow = {0: 0.96, 1: 0.95, 2: 0.97, 3: 0.98, 4: 1.03, 5: 1.08, 6: 1.10}
    per_day = split_counts(N_CARTS, [dow[d.weekday()] for d in MONTH], rng, noise=0.04)
    days = [d for d, n in zip(MONTH, per_day) for _ in range(n)]
    bands = [b for b, n in BANDS.items() for _ in range(n)]
    rng.shuffle(bands)
    band_rank = {b: i for i, b in enumerate(BANDS)}
    carts = [{"customer": c, "day": d, "band": b, "tie": rng.random()}
             for c, d, b in zip(slots, days, bands)]
    carts.sort(key=lambda r: (r["day"], band_rank[r["band"]], r["tie"]))
    for n, r in enumerate(carts, start=1):
        r["cart_id"] = f"C{n:06d}"
        r["zone"] = r["customer"]["zone"]
        r["stockout"] = (r["zone"] in STOCKOUT_ZONES
                         and STOCKOUT_DAYS[0] <= r["day"] <= STOCKOUT_DAYS[1])
    return customers, carts


def place_items(rng, carts):
    """Every item placed as an exact count, stratified by milk so its lift to milk stays near one."""
    n = len(carts)
    items = [set() for _ in range(n)]
    # The twelve carts: spread across the month, outside the stock-out, never edited afterwards.
    eligible = [i for i in range(n) if not carts[i]["stockout"]]
    twelve = sorted(eligible[k * len(eligible) // 12 + 97] for k in range(12))
    for i, cart in zip(twelve, TWELVE):
        items[i] = set(cart)
    reserved = set(twelve)
    pool = [i for i in range(n) if i not in reserved]

    def in12(*names):
        return sum(1 for c in TWELVE if all(x in c for x in names))

    # Milk, by time band: morning carts hold it more often.
    milk = []
    by_band = {b: [i for i in pool if carts[i]["band"] == b] for b in BANDS}
    want = {b: round(MILK_BY_BAND[b] * BANDS[b]) - sum(1 for i in twelve if carts[i]["band"] == b
                                                       and "toned milk" in items[i]) for b in BANDS}
    want["evening"] += TARGET["toned milk"] - in12("toned milk") - sum(want.values())
    for b in BANDS:
        milk += pick(rng, by_band[b], want[b])
    for i in milk:
        items[i].add("toned milk")
    M = sorted(i for i in pool if "toned milk" in items[i])
    N = sorted(i for i in pool if "toned milk" not in items[i])

    def place(name, k_milk, k_none, weight=None, among_m=None, among_n=None):
        for i in pick(rng, among_m if among_m is not None else M, k_milk, weight):
            items[i].add(name)
        for i in pick(rng, among_n if among_n is not None else N, k_none, weight):
            items[i].add(name)

    # Bread, eggs, curd and bananas carry the case file's confidences toward milk.
    for name, with_milk in (("bread", BREAD_MILK), ("eggs", EGGS_MILK), ("bananas", BANANAS_MILK)):
        km = with_milk - in12(name, "toned milk")
        kn = TARGET[name] - with_milk - (in12(name) - in12(name, "toned milk"))
        place(name, km, kn)
    # Curd: near zero in two zones for week three, the stock-out the ticket names.
    km = CURD_MILK - in12("curd", "toned milk")
    kn = TARGET["curd"] - CURD_MILK - (in12("curd") - in12("curd", "toned milk"))
    place("curd", km, kn, weight=lambda i: 0.012 if carts[i]["stockout"] else 1.0)

    # Designed pairs: both, then each side alone, each cell 71 percent milk.
    def pair(a, b, both, weight_both=None, weight_one=None, among=None):
        free_m = [i for i in M if a not in items[i] and b not in items[i]]
        free_n = [i for i in N if a not in items[i] and b not in items[i]]
        if among is not None:
            free_m = [i for i in free_m if among(i)]
            free_n = [i for i in free_n if among(i)]
        k = both - in12(a, b)
        km = round(0.71 * both) - in12(a, b, "toned milk")
        for i in pick(rng, free_m, km, weight_both) + pick(rng, free_n, k - km, weight_both):
            items[i].update((a, b))
        for name, other in ((a, b), (b, a)):
            alone = TARGET[name] - both - (in12(name) - in12(name, other))
            free_m = [i for i in M if name not in items[i] and other not in items[i]]
            free_n = [i for i in N if name not in items[i] and other not in items[i]]
            km = round(0.71 * (TARGET[name] - both)) - (in12(name, "toned milk")
                                                       - in12(name, other, "toned milk"))
            for i in pick(rng, free_m, km, weight_one) + pick(rng, free_n, alone - km, weight_one):
                items[i].add(name)

    # Party shoppers: the top tenth place three in four of the carts holding both, while carts
    # holding only one of the two lean the other way, so counting each customer once shrinks lift.
    party = lambda i: (4.9 if carts[i]["customer"]["heavy"] else 1.0) * \
        (1.4 if carts[i]["band"] in ("evening", "night") else 1.0)
    lean = lambda i: (0.8 if carts[i]["customer"]["heavy"] else 1.0)
    pair("chips", "cold drink", PAIRS[("chips", "cold drink")], party, lean)
    pair("coriander", "green chillies", PAIRS[("coriander", "green chillies")])
    pair("onions", "tomatoes", PAIRS[("onions", "tomatoes")])
    pair("chocolate sauce", "ice cream", PAIRS[("chocolate sauce", "ice cream")])
    # Butter: 1,800 of its 2,400 carts hold bread, so it follows bread's milk share.
    bread_m = [i for i in M if "bread" in items[i]]
    bread_n = [i for i in N if "bread" in items[i]]
    with_bread = PAIRS[("bread", "butter")]
    km = round(with_bread * len(bread_m) / (len(bread_m) + len(bread_n)))
    place("butter", km, with_bread - km, among_m=bread_m, among_n=bread_n)
    rest_m = [i for i in M if "bread" not in items[i]]
    rest_n = [i for i in N if "bread" not in items[i]]
    alone = TARGET["butter"] - with_bread
    km = round(alone * len(rest_m) / (len(rest_m) + len(rest_n)))
    place("butter", km, alone - km, among_m=rest_m, among_n=rest_n)

    # Every other item: an exact count, its milk share drawn between 0.70 and 0.735.
    done = {"toned milk", "bread", "eggs", "curd", "bananas", "butter"} | {x for p in PAIRS for x in p}
    for name, _, _, total in CATALOGUE:
        if name in done:
            continue
        k = total - in12(name)
        km = round(rng.uniform(0.70, 0.735) * total) - in12(name, "toned milk")
        place(name, km, k - km)

    # A cart with no item cannot exist: move one free-standing item into it from a full cart
    # without milk, which keeps every count and every milk share exactly as placed.
    movable = [name for name, _, _, _ in CATALOGUE if name not in done]
    empties = [i for i in N if not items[i]]
    donors = [i for i in N if len(items[i]) >= 4 and any(x in movable for x in items[i])]
    rng.shuffle(donors)
    if len(donors) < len(empties):
        raise AssertionError("too few full carts to repair the empty ones")
    for i, d in zip(empties, donors):
        name = sorted(x for x in items[d] if x in movable)[0]
        items[d].discard(name)
        items[i].add(name)
    if any(not s for s in items):
        raise AssertionError("an empty cart survived the repair")
    return items, twelve


def write_case(rng):
    customers, carts = build_carts(rng)
    items, twelve = place_items(rng, carts)
    cart_rows, line_rows = [], []
    for r, held in zip(carts, items):
        value = 0
        for name in sorted(held):
            if name == "toned milk":
                q = rng.choices([1, 2, 3], weights=[55, 35, 10])[0]
            elif name == "eggs":
                q = rng.choices([1, 2], weights=[85, 15])[0]
            else:
                q = rng.choices([1, 2], weights=[90, 10])[0]
            value += q * PRICE[name]
            line_rows.append({"cart_id": r["cart_id"], "item": name, "quantity": q,
                              "price_rs": PRICE[name], "margin_rs": MARGIN[name]})
        cart_rows.append({"cart_id": r["cart_id"], "customer_id": r["customer"]["customer_id"],
                          "placed_date": r["day"].isoformat(), "zone": r["zone"],
                          "time_band": r["band"], "cart_value_rs": value})
    cart_df = pd.DataFrame(cart_rows)
    item_df = pd.DataFrame(line_rows)
    cart_df.to_csv(DATA / "C2_W04_D03_carts_STUDENT.csv", index=False)
    item_df.to_csv(DATA / "C2_W04_D03_cart_items_STUDENT.csv", index=False, float_format="%.2f")
    rows = []
    for k, i in enumerate(twelve):
        row = {"cart_id": carts[i]["cart_id"]}
        row.update({name: int(name in items[i]) for name in TWELVE_ITEMS})
        rows.append(row)
    twelve_df = pd.DataFrame(rows)
    twelve_df.to_csv(DATA / "C2_W04_D03_twelve_rows_STUDENT.csv", index=False)
    return cart_df, item_df, twelve_df


# =========================================================================== the strip log
# Each anchor's suggestions for slots 1, 2 and 3: the curated list before 7 September, and the
# best non-milk partner by co-occurrence after it (milk's share of each slot is set separately).
ANCHORS = {"bread": 0.22, "eggs": 0.16, "curd": 0.14, "onions": 0.14, "bananas": 0.10,
           "paneer": 0.10, "chips": 0.08, "atta": 0.06}
CURATED = {"bread": ["butter", "eggs", "cheese slices"], "eggs": ["bread", "butter", "onions"],
           "curd": ["cucumber", "sugar", "mint"], "onions": ["tomatoes", "potatoes", "green chillies"],
           "bananas": ["apples", "biscuits", "poha"], "paneer": ["capsicum", "green peas", "butter"],
           "chips": ["cold drink", "namkeen", "ice cubes"], "atta": ["ghee", "sunflower oil", "toned milk"]}
COUNT_RANKED = {"bread": ["eggs", "curd", "bananas"], "eggs": ["bread", "curd", "bananas"],
                "curd": ["bread", "eggs", "bananas"], "onions": ["tomatoes", "potatoes", "bread"],
                "bananas": ["bread", "eggs", "curd"], "paneer": ["onions", "tomatoes", "bread"],
                "chips": ["cold drink", "bread", "eggs"], "atta": ["onions", "potatoes", "bread"]}
MILK_SLOT_SHARE = {1: 0.70, 2: 0.50, 3: 0.30}
MILK_ANCHOR_TILT = {"bread": 1.06, "eggs": 1.04, "curd": 1.0, "onions": 1.0, "bananas": 1.02,
                    "paneer": 0.97, "chips": 0.80, "atta": 1.0}
SLOT_PULL = {1: 1.22, 2: 1.00, 3: 0.80}          # the position effect on click-through
TARGETS = {("before", "milk"): 0.0120, ("before", "other"): 0.0620,
           ("after", "milk"): 0.0120, ("after", "other"): 0.0640}
ADD_RATE = 0.50


def write_strip_log(rng):
    """Impressions, clicks and adds by day, slot, anchor and suggestion, calibrated to the ticket."""
    dow = {0: 0.96, 1: 0.95, 2: 0.96, 3: 0.98, 4: 1.02, 5: 1.10, 6: 1.12}
    views = [dow[d.weekday()] * (1 + 0.004 * k) * (1 + rng.uniform(-0.03, 0.03))
             for k, d in enumerate(LOG_DAYS)]
    before, after = views[:21], views[21:]
    views = ([round(v * 58_800 * 21 / sum(before)) for v in before]
             + [round(v * 60_000 * 21 / sum(after)) for v in after])
    views[-1] += 60_000 * 21 - sum(views[21:])                        # the after mean is 60,000
    rows = []
    for d, v in zip(LOG_DAYS, views):
        window = "after" if d >= CHANGE_DAY else "before"
        day_pull = (1.05 if d.weekday() >= 5 else 1.0) * (1 + rng.uniform(-0.04, 0.04))
        shares = split_counts(v, list(ANCHORS.values()), rng, noise=0.08)
        for slot in (1, 2, 3):
            for (anchor, _), imp in zip(ANCHORS.items(), shares):
                if window == "before":
                    parts = [(CURATED[anchor][slot - 1], imp)]
                else:
                    m = round(imp * min(0.95, MILK_SLOT_SHARE[slot] * MILK_ANCHOR_TILT[anchor]
                                        * (1 + rng.uniform(-0.05, 0.05))))
                    parts = [("toned milk", m), (COUNT_RANKED[anchor][slot - 1], imp - m)]
                for item, k in parts:
                    group = "milk" if item == "toned milk" else "other"
                    pull = SLOT_PULL[slot] * day_pull * (1 + rng.uniform(-0.06, 0.06))
                    rows.append({"date": d.isoformat(), "slot": slot, "anchor_item": anchor,
                                 "suggested_item": item, "impressions": k,
                                 "_window": window, "_group": group, "_pull": pull})
    log = pd.DataFrame(rows)
    # Calibrate clicks so each window and group lands on its target rate, then adds at half.
    for (window, group), target in TARGETS.items():
        sel = (log._window == window) & (log._group == group)
        raw = log.loc[sel, "impressions"] * log.loc[sel, "_pull"]
        scale = target * log.loc[sel, "impressions"].sum() / raw.sum()
        log.loc[sel, "clicks"] = (raw * scale).round()
        gap = round(target * log.loc[sel, "impressions"].sum()) - int(log.loc[sel, "clicks"].sum())
        top = log.loc[sel, "impressions"].idxmax()
        log.loc[top, "clicks"] += gap
    log["clicks"] = log["clicks"].astype(int)
    noise = [1 + rng.uniform(-0.08, 0.08) for _ in range(len(log))]
    log["adds"] = [round(c * ADD_RATE * z) for c, z in zip(log.clicks, noise)]
    for window in ("before", "after"):
        for group in ("milk", "other"):
            sel = (log._window == window) & (log._group == group)
            if not sel.any():
                continue
            gap = round(ADD_RATE * log.loc[sel, "clicks"].sum()) - int(log.loc[sel, "adds"].sum())
            top = log.loc[sel, "clicks"].idxmax()
            log.loc[top, "adds"] += gap
    log = log.drop(columns=["_window", "_group", "_pull"])
    log = log[log.impressions > 0].reset_index(drop=True)
    log.to_csv(DATA / "C2_W04_D03_strip_log_STUDENT.csv", index=False)
    return log


# =========================================================================== the Kalpa transfer
KALPA_PRODUCTS = [
    ("P001", "phone charger 20W", "Electronics", 199, 120),
    ("P002", "screen protector", "Accessories", 149, 85),
    ("P003", "earphone jack adapter", "Accessories", 89, 50),
    ("P004", "wireless earphones", "Electronics", 1499, 950),
    ("P005", "earphone case", "Accessories", 299, 170),
    ("P006", "car phone mount", "Accessories", 399, 230),
    ("P007", "car charger", "Electronics", 349, 200),
    ("P008", "power bank 10000mAh", "Electronics", 1199, 780),
    ("P009", "phone grip", "Accessories", 99, 55),
    ("P010", "cable organiser", "Accessories", 149, 80),
    ("P011", "notebook A5", "Stationery", 79, 40),
    ("P012", "pen set", "Stationery", 99, 50),
    ("P013", "LED desk lamp", "Lighting", 699, 420),
    ("P014", "extension cord", "Electronics", 499, 290),
    ("P015", "USB-C cable", "Electronics", 249, 140),
]
KP = {p[0]: p for p in KALPA_PRODUCTS}
FILLERS = {"P003": 1.0, "P008": 0.9, "P009": 1.1, "P010": 1.0, "P011": 1.3, "P012": 1.2,
           "P013": 0.9, "P014": 1.0, "P015": 1.2}
KALPA = {"charger": 686, "screen": 100, "screen_with_charger": 82,
         "earphones": 110, "case": 116, "earphones_and_case": 49, "pair_retail_plus": 37,
         "mount": 14, "car_charger": 29, "mount_and_car_charger": 2}


def kalpa_tables():
    """v4's customers and orders, exactly as the client-zero generator builds them."""
    t = cz.build_v4()
    segment = {c["customer_id"]: c["segment"] for c in t["customers"]}
    orders = [dict(o, segment=segment[o["customer_id"]]) for o in t["orders"]]
    return sorted(orders, key=lambda o: o["order_id"])


def write_kalpa(rng):
    """Order lines for v4's 1,000 orders: consumer baskets of one to eight lines, Business orders
    of one product in bulk, every order's lines summing to its amount."""
    orders = kalpa_tables()
    consumer = [o for o in orders if o["segment"] != "Business"]
    business = [o for o in orders if o["segment"] == "Business"]
    basket = {o["order_id"]: [] for o in consumer}
    amount = {o["order_id"]: o["amount"] for o in orders}
    ids = [o["order_id"] for o in consumer]

    def listed(oid):
        return sum(KP[p][3] for p in basket[oid])

    def place(pid, pool, k, need_room=0):
        fits = [oid for oid in pool if pid not in basket[oid]
                and listed(oid) + KP[pid][3] + need_room <= amount[oid]]
        for oid in pick(rng, sorted(fits), k):
            basket[oid].append(pid)

    charger = set(pick(rng, ids, KALPA["charger"]))
    with_c = sorted(charger)
    without_c = sorted(set(ids) - charger)
    share = len(with_c) / len(ids)
    plus = {o["order_id"] for o in consumer if o["segment"] == "Retail-Plus"}

    # The strongest pair, mostly Retail-Plus, each cell split by the charger's share.
    both = KALPA["earphones_and_case"]
    k_plus_c = round(KALPA["pair_retail_plus"] * share)
    k_rest_c = round(both * share) - k_plus_c
    room = 1499 + 299 + 199
    place("P004", [o for o in with_c if o in plus], k_plus_c, 299 + 199)
    place("P004", [o for o in without_c if o in plus], KALPA["pair_retail_plus"] - k_plus_c, 299)
    place("P004", [o for o in with_c if o not in plus], k_rest_c, 299 + 199)
    place("P004", [o for o in without_c if o not in plus],
          both - KALPA["pair_retail_plus"] - k_rest_c, 299)
    paired = [oid for oid in ids if "P004" in basket[oid]]
    for oid in paired:
        basket[oid].append("P005")
    for pid, total in (("P004", KALPA["earphones"]), ("P005", KALPA["case"])):
        alone = total - both
        kc = round(total * share) - sum(1 for o in paired if o in charger)
        free_c = [o for o in with_c if "P004" not in basket[o] and "P005" not in basket[o]]
        free_n = [o for o in without_c if "P004" not in basket[o] and "P005" not in basket[o]]
        place(pid, free_c, kc, 199)
        place(pid, free_n, alone - kc)
    # The thin pair: two baskets hold the car phone mount and the car charger together.
    k = KALPA["mount_and_car_charger"]
    duo = pick(rng, sorted(o for o in with_c if listed(o) + 399 + 349 + 199 <= amount[o]), k)
    for oid in duo:
        basket[oid] += ["P006", "P007"]
    for pid, other, total in (("P006", "P007", KALPA["mount"]), ("P007", "P006", KALPA["car_charger"])):
        kc = round(total * share) - k
        free_c = [o for o in with_c if other not in basket[o]]
        free_n = [o for o in without_c if other not in basket[o]]
        place(pid, free_c, kc, 199)
        place(pid, free_n, total - k - kc)
    # The charger's partner: confidence toward the charger 0.82.
    place("P002", with_c, KALPA["screen_with_charger"], 199)
    place("P002", without_c, KALPA["screen"] - KALPA["screen_with_charger"])
    for oid in with_c:
        basket[oid].append("P001")

    # Fill each basket from the free-standing products until its list total covers the amount,
    # balancing every filler between baskets with and without the charger.
    seen = {s: Counter() for s in (True, False)}
    size = {True: len(with_c), False: len(without_c)}
    lines = {}
    for oid in ids:
        a, s = amount[oid], oid in charger
        qty = Counter(basket[oid])
        total = sum(KP[p][3] * q for p, q in qty.items())
        while total < a:
            room_left = a / 0.85 - total
            options = [p for p in FILLERS if p not in qty and KP[p][3] <= room_left
                       and len(qty) < 8]
            if options:
                p = min(options, key=lambda p: ((seen[s][p] + 1) / (size[s] * FILLERS[p]))
                        * (1 + rng.uniform(0, 0.35)))
                seen[s][p] += 1
            else:
                # Another unit of a cheap line, never of the dearest, which stays a single unit.
                top = max(qty, key=lambda p: (KP[p][3], p))
                cheap = sorted((p for p in qty if p != top), key=lambda p: KP[p][3])
                fit = [p for p in cheap if KP[p][3] <= room_left] or cheap[:1] or [top]
                p = fit[0]
            qty[p] += 1
            total += KP[p][3]
        lines[oid] = qty
    item_rows = []
    for oid in ids:
        qty = lines[oid]
        a = amount[oid]
        total = sum(KP[p][3] * q for p, q in qty.items())
        # The discount from list to amount, shared in whole rupees: each multi-unit line takes its
        # proportional share per unit, and the single-unit lines absorb what is left.
        cut = total - a
        off = {p: (cut * KP[p][3] // total if qty[p] > 1 else 0) for p in qty}
        left = cut - sum(off[p] * qty[p] for p in qty)
        singles = sorted((p for p in qty if qty[p] == 1), key=lambda p: (-KP[p][3], p))
        room = sum(KP[p][3] for p in singles)
        for p in singles:
            off[p] = left * KP[p][3] // room
        off[singles[0]] += left - sum(off[p] for p in singles)
        price = {p: KP[p][3] - off[p] for p in qty}
        if sum(price[p] * q for p, q in qty.items()) != a:
            raise AssertionError(f"cannot settle {oid}")
        for p in sorted(qty):
            item_rows.append({"order_id": oid, "product_id": p, "quantity": qty[p],
                              "unit_price": price[p]})
    # Business: one product in bulk at a unit price within a quarter of its list price.
    for o in business:
        a = o["amount"]
        for pid in pick(rng, sorted(KP), len(KP)):
            lp = KP[pid][3]
            fits = [u for u in range(lp, int(0.75 * lp) - 1, -1) if a % u == 0]
            if fits:
                u = fits[0]
                item_rows.append({"order_id": o["order_id"], "product_id": pid,
                                  "quantity": a // u, "unit_price": u})
                break
        else:
            raise AssertionError(f"no bulk price settles {o['order_id']}")
    products = pd.DataFrame(KALPA_PRODUCTS, columns=["product_id", "name", "category",
                                                      "list_price", "unit_cost"])
    order_df = pd.DataFrame([{k: o[k] for k in ("order_id", "customer_id", "segment", "order_date",
                                                "channel", "amount", "status")} for o in orders])
    item_df = pd.DataFrame(item_rows).sort_values(["order_id", "product_id"]).reset_index(drop=True)
    products.to_csv(DATA / "C2_W04_D03_kalpa_products_STUDENT.csv", index=False)
    order_df.to_csv(DATA / "C2_W04_D03_kalpa_orders_STUDENT.csv", index=False)
    item_df.to_csv(DATA / "C2_W04_D03_kalpa_order_items_STUDENT.csv", index=False)
    return products, order_df, item_df


# =========================================================================== measuring
def measures(baskets, a, b):
    """Support, the two confidences and lift for one pair over a list of item sets."""
    n = len(baskets)
    na = sum(1 for s in baskets if a in s)
    nb = sum(1 for s in baskets if b in s)
    nab = sum(1 for s in baskets if a in s and b in s)
    return {"n": n, "na": na, "nb": nb, "nab": nab, "support": nab / n, "conf_ab": nab / na,
            "conf_ba": nab / nb, "lift": nab * n / (na * nb)}


def pairs_table(baskets):
    """Every pair that appears in at least one basket, with support and lift."""
    n = len(baskets)
    single = Counter(x for s in baskets for x in s)
    double = Counter(p for s in baskets for p in combinations(sorted(s), 2))
    rows = [{"a": a, "b": b, "both": k, "support": k / n,
             "conf_ab": k / single[a], "conf_ba": k / single[b],
             "lift": k * n / (single[a] * single[b])} for (a, b), k in double.items()]
    return pd.DataFrame(rows).sort_values(["lift", "a", "b"], ascending=[False, True, True])


def weighted_lift(carts, baskets, a, b):
    """Lift with every customer counted once: each cart weighs one over its customer's cart count."""
    w = 1 / carts.groupby("customer_id").cart_id.transform("count")
    has_a = baskets.apply(lambda s: a in s).values
    has_b = baskets.apply(lambda s: b in s).values
    total = w.sum()
    pa, pb = (w * has_a).sum() / total, (w * has_b).sum() / total
    pab = (w * (has_a & has_b)).sum() / total
    return pab / (pa * pb)


def size_adjusted_lift(baskets, a, b, w=None):
    """Lift with chance sized by cart: carts of each item count give their own expected count.
    With weights w (one over the customer's cart count), every customer also counts once."""
    sizes = baskets.map(len).values
    has_a = baskets.apply(lambda s: a in s).values
    has_b = baskets.apply(lambda s: b in s).values
    w = pd.Series(1.0, index=range(len(sizes))).values if w is None else w.values
    expected = 0.0
    for k in sorted(set(sizes)):
        m = sizes == k
        expected += (w[m] * has_a[m]).sum() * (w[m] * has_b[m]).sum() / w[m].sum()
    return (w * (has_a & has_b)).sum() / expected


def verify_case(cart_df, item_df, twelve_df):
    out = {}
    n = len(cart_df)
    check("40,000 carts", n == N_CARTS)
    baskets = item_df.groupby("cart_id").item.apply(set).reindex(cart_df.cart_id)
    check("every cart holds at least one item", baskets.notna().all() and baskets.map(len).min() >= 1)
    single = Counter(x for s in baskets for x in s)
    for name, _, _, total in CATALOGUE:
        if single[name] != total:
            raise AssertionError(f"FAIL {name} in {single[name]} carts, target {total}")
    check("every one of the 59 items sits in exactly its target number of carts",
          len(single) == len(CATALOGUE) == 59)
    out["items"] = len(single)
    out["lines"] = len(item_df)
    out["share"] = {name: single[name] / n for name in single}
    out["count"] = dict(single)
    pairs = pairs_table(list(baskets))
    out["pairs_seen"] = len(pairs)
    sizes = baskets.map(len)
    out["pair_increments"] = int((sizes * (sizes - 1) // 2).sum())
    out["items_per_cart"] = float(sizes.mean())
    for (a, b), k in PAIRS.items():
        m = measures(list(baskets), a, b)
        check(f"{a} with {b} in {k:,} carts", m["nab"] == k)
    for name, k in (("bread", BREAD_MILK), ("eggs", EGGS_MILK), ("curd", CURD_MILK),
                    ("bananas", BANANAS_MILK)):
        check(f"{name} with milk in {k:,} carts", measures(list(baskets), name, "toned milk")["nab"] == k)
    out["m"] = {}
    for a, b in (("bread", "toned milk"), ("eggs", "toned milk"), ("curd", "toned milk"),
                 ("bananas", "toned milk"), ("chips", "cold drink"), ("ice cream", "chocolate sauce"),
                 ("coriander", "green chillies"), ("bread", "butter"), ("onions", "tomatoes")):
        out["m"][(a, b)] = measures(list(baskets), a, b)
    bm, em = out["m"][("bread", "toned milk")], out["m"][("eggs", "toned milk")]
    check("bread to milk confidence 0.74, lift 1.04",
          round(bm["conf_ab"], 2) == 0.74 and round(bm["lift"], 2) == 1.04)
    check("eggs to milk confidence 0.73, lift 1.03",
          round(em["conf_ab"], 2) == 0.73 and round(em["lift"], 2) == 1.03)
    cc = out["m"][("chips", "cold drink")]
    check("chips and cold drink: support 5.0 percent, confidences 0.42 and 0.41, lift 3.4",
          round(cc["support"], 3) == 0.050 and round(cc["conf_ab"], 2) == 0.42
          and round(cc["conf_ba"], 2) == 0.41 and round(cc["lift"], 1) == 3.4)
    ic = out["m"][("ice cream", "chocolate sauce")]
    check("ice cream and chocolate sauce: 100 carts, support 0.25 percent, lift 4.6",
          ic["nab"] == 100 and round(ic["lift"], 1) == 4.6)
    # Every item in at least 2 percent of carts: confidence to milk 0.68 to 0.78, lift 0.96 to 1.08.
    common = sorted(x for x in single if x != "toned milk" and single[x] / n >= 0.02)
    lo_c = lo_l = 9.0
    hi_c = hi_l = 0.0
    for x in common:
        m = measures(list(baskets), x, "toned milk")
        lo_c, hi_c = min(lo_c, m["conf_ab"]), max(hi_c, m["conf_ab"])
        lo_l, hi_l = min(lo_l, m["lift"]), max(hi_l, m["lift"])
    check(f"{len(common)} items in at least 2 percent of carts: confidence to milk "
          f"{lo_c:.2f} to {hi_c:.2f}, lift {lo_l:.2f} to {hi_l:.2f}",
          0.68 <= lo_c and hi_c <= 0.78 and 0.96 <= lo_l and hi_l <= 1.08)
    out["common"] = (len(common), lo_c, hi_c, lo_l, hi_l)
    # The floor, the ranking and the watch list.
    floor = pairs[pairs.support >= 0.01]
    top = floor.head(4)
    names = [(r.a, r.b) for r in top.itertuples()]
    check("above the 1 percent floor, the ranking by lift opens chips and cold drink, coriander "
          "and green chillies, bread and butter, onions and tomatoes",
          names == [("chips", "cold drink"), ("coriander", "green chillies"), ("bread", "butter"),
                    ("onions", "tomatoes")])
    nxt = floor.iloc[4]
    check("every other pair above the floor sits below lift 1.15", nxt.lift < 1.15,
          f"(next is {nxt.a} and {nxt.b} at {nxt.lift:.2f})")
    out["floor_pairs"] = len(floor)
    out["pairs_plotted"] = int((pairs.support >= 0.001).sum())
    out["floor_above_1_5"] = int((floor.lift >= 1.5).sum())
    out["next_after_four"] = (nxt.a, nxt.b, nxt.lift)
    band = pairs[(pairs.support >= 0.002) & (pairs.support < 0.01)]
    best = band.iloc[0]
    check("between 0.2 and 1 percent support, ice cream and chocolate sauce has the highest lift",
          (best.a, best.b) == ("chocolate sauce", "ice cream"))
    out["watch_band_pairs"] = len(band)
    thin = pairs[pairs.support < 0.002]
    out["tiny"] = (len(thin), thin.lift.max())
    # The top tenth.
    per_cust = cart_df.customer_id.value_counts()
    top_n = len(per_cust) // 10
    share = per_cust.iloc[:top_n].sum() / n
    check("12,000 customers, and the top tenth place 38 percent of carts",
          len(per_cust) == 12_000 and round(share, 4) == 0.38)
    out["customers"] = len(per_cust)
    out["heavy_share"] = share
    out["heavy_min"], out["light_max"] = int(per_cust.iloc[top_n - 1]), int(per_cust.iloc[top_n])
    # Per customer: each customer counted once.
    out["cc_cust"] = weighted_lift(cart_df, baskets, "chips", "cold drink")
    out["bm_cust"] = weighted_lift(cart_df, baskets, "bread", "toned milk")
    check(f"per customer, chips and cold drink fall to {out['cc_cust']:.2f} and bread with milk "
          f"stays at {out['bm_cust']:.2f}",
          out["cc_cust"] < cc["lift"] - 0.5 and abs(out["bm_cust"] - bm["lift"]) < 0.03)
    # Sized by cart: bigger carts hold any pair by chance, so chance is counted within each cart size.
    out["size_lift"] = {pr: size_adjusted_lift(baskets, *pr) for pr in
                        (("chips", "cold drink"), ("coriander", "green chillies"), ("bread", "butter"),
                         ("onions", "tomatoes"))}
    w_cust = 1 / cart_df.groupby("customer_id").cart_id.transform("count")
    out["both_lift"] = {pr: size_adjusted_lift(baskets, *pr, w=w_cust) for pr in
                        (("chips", "cold drink"), ("onions", "tomatoes"))}
    check("corrected for both, each customer once and chance sized by cart, chips and cold drink read "
          "1.95 and onions and tomatoes 1.38",
          [round(v, 2) for v in out["both_lift"].values()] == [1.95, 1.38])
    sl = out["size_lift"]
    check("sized by each cart's item count, chips and cold drink read 2.48, coriander and green chillies "
          "2.25, bread and butter 1.74, and onions and tomatoes 1.38, below the 1.5 bar",
          [round(v, 2) for v in sl.values()] == [2.48, 2.25, 1.74, 1.38])
    line_margin = item_df.margin_rs * item_df.quantity
    cart_margin = line_margin.groupby(item_df.cart_id).sum()
    ic_ids = set(item_df.loc[item_df.item == "ice cream", "cart_id"])
    out["ic_margin_sd"] = float(cart_margin[cart_margin.index.isin(ic_ids)].std())
    heavy_ids = set(per_cust.index[:top_n])
    pair_carts = item_df[item_df.item.isin(["chips", "cold drink"])].groupby("cart_id").item.nunique()
    both_ids = set(pair_carts[pair_carts == 2].index)
    owner = cart_df.set_index("cart_id").customer_id
    out["cc_heavy_share"] = sum(1 for c in both_ids if owner[c] in heavy_ids) / len(both_ids)
    # Time band.
    milk_ids = set(item_df.loc[item_df.item == "toned milk", "cart_id"])
    cart_df = cart_df.assign(milk=cart_df.cart_id.isin(milk_ids))
    by_band = cart_df.groupby("time_band").milk.mean()
    out["milk_by_band"] = by_band.to_dict()
    check("morning carts hold milk most often", by_band.idxmax() == "morning"
          and by_band["morning"] - by_band.drop("morning").max() >= 0.09)
    out["bm_by_band"] = {}
    for b in BANDS:
        ids = cart_df.loc[cart_df.time_band == b, "cart_id"]
        out["bm_by_band"][b] = measures(list(baskets.loc[ids]), "bread", "toned milk")["lift"]
    check("bread with milk reads lift 1.02 to 1.06 in every band",
          all(1.01 <= v <= 1.07 for v in out["bm_by_band"].values()))
    # The stock-out.
    cart_df = cart_df.assign(day=pd.to_datetime(cart_df.placed_date))
    curd_ids = set(item_df.loc[item_df.item == "curd", "cart_id"])
    cart_df = cart_df.assign(curd=cart_df.cart_id.isin(curd_ids),
                             week=(cart_df.day.dt.day - 1) // 7 + 1)
    hit = cart_df.zone.isin(STOCKOUT_ZONES) & (cart_df.week == 3)
    out["stock_carts"] = int(hit.sum())
    out["stock_curd"] = int(cart_df.loc[hit, "curd"].sum())
    out["curd_in_stock"] = cart_df.loc[hit, "curd"].mean()
    out["curd_elsewhere"] = cart_df.loc[~hit, "curd"].mean()
    by_cell = cart_df.groupby(["zone", "week"]).curd.mean()
    others = by_cell.drop([(z, 3) for z in STOCKOUT_ZONES])
    check(f"curd near zero in {', '.join(STOCKOUT_ZONES)} in week three "
          f"({out['stock_curd']} of {out['stock_carts']} carts) and above 0.22 in every other zone-week",
          out["curd_in_stock"] < 0.02 and others.min() > 0.22)
    out["curd_cell_min"], out["curd_cell_max"] = others.min(), others.max()
    kept = list(baskets.loc[cart_df.loc[~hit, "cart_id"]])
    out["curd_kept"] = measures(kept, "curd", "toned milk")
    out["curd_all"] = measures(list(baskets), "curd", "toned milk")
    # The twelve rows.
    t = twelve_df
    def cnt(*cols):
        return int(t[list(cols)].all(axis=1).sum())
    check("twelve rows: milk 8, bread 4, bread with milk 4, chips 3, cold drink 3, both 2, "
          "ice cream with chocolate sauce 1",
          (cnt("toned milk"), cnt("bread"), cnt("bread", "toned milk"), cnt("chips"),
           cnt("cold drink"), cnt("chips", "cold drink"), cnt("ice cream", "chocolate sauce"))
          == (8, 4, 4, 3, 3, 2, 1))
    real = set(cart_df.cart_id)
    check("the twelve rows are real carts of the 40,000", set(t.cart_id) <= real)
    by_count = pairs.sort_values(["both", "a", "b"], ascending=[False, True, True]).head(6)
    out["top_by_count"] = [(r.a, r.b, r.both) for r in by_count.itertuples()]
    out["floor_rows"] = [(r.a, r.b, r.both, r.support, r.lift) for r in floor.head(5).itertuples()]
    out["band_rows"] = [(r.a, r.b, r.both, r.support, r.lift) for r in band.head(4).itertuples()]
    out["curd_grid"] = by_cell.to_dict()
    nm = item_df[item_df.item != "toned milk"]
    out["margin_line"] = nm.margin_rs.mean()
    bread = item_df[item_df.item == "bread"]
    check("every bread line sells at Rs 45 with a margin of Rs 6.70",
          set(bread.price_rs) == {45} and set(bread.margin_rs.round(2)) == {6.7})
    check(f"a cart_items line earns Rs {out['margin_line']:.2f} on average, milk aside",
          8.95 <= out["margin_line"] <= 9.05)
    # The fallback's slices: the city's ranking held up, and thin ground in the smallest slice.
    out["slices"] = {}
    for name, mask in (("Kothrud, morning", (cart_df.zone == "Kothrud") & (cart_df.time_band == "morning")),
                       ("Kothrud, evening", (cart_df.zone == "Kothrud") & (cart_df.time_band == "evening")),
                       ("Baner, morning", (cart_df.zone == "Baner") & (cart_df.time_band == "morning")),
                       ("Hinjewadi, night", (cart_df.zone == "Hinjewadi") & (cart_df.time_band == "night")),
                       ("Hadapsar, week three", (cart_df.zone == "Hadapsar") & (cart_df.week == 3)),
                       ("Hadapsar, week four", (cart_df.zone == "Hadapsar") & (cart_df.week == 4)),
                       ("Viman Nagar, week three", (cart_df.zone == "Viman Nagar") & (cart_df.week == 3))):
        part = list(baskets.loc[cart_df.loc[mask, "cart_id"]])
        table = pairs_table(part)
        above = table[table.support >= 0.01]
        out["slices"][name] = (len(part), [(r.a, r.b, r.lift, r.both) for r in above.head(6).itertuples()])
    lead = [("chips", "cold drink"), ("coriander", "green chillies")]
    check("chips with cold drink and coriander with chillies lead every slice",
          all({(a, b) for a, b, _, _ in rows[:2]} == set(lead)
              for name, (_, rows) in out["slices"].items() if name != "Viman Nagar, week three"))
    n_small, rows = out["slices"]["Hinjewadi, night"]
    bb = [i for i, r in enumerate(rows) if r[:2] == ("bread", "butter")][0]
    out["thin_slips"] = rows[2:bb]
    check(f"in the smallest slice, {len(out['thin_slips'])} thin pairs slip in above bread with butter",
          n_small < 700 and len(out["thin_slips"]) >= 2 and all(r[3] <= 12 for r in out["thin_slips"]))
    out["curd_hadapsar"] = by_cell.loc[("Hadapsar", 3)], by_cell.loc[("Hadapsar", 4)]
    # Quantities and value.
    out["value_median"] = cart_df.cart_value_rs.median()
    out["value_mean"] = cart_df.cart_value_rs.mean()
    out["per_day"] = cart_df.groupby("placed_date").size()
    out["zones"] = cart_df.zone.value_counts().to_dict()
    return out


def verify_strip(log):
    out = {}
    log = log.assign(window=(log.date >= CHANGE_DAY.isoformat()).map({True: "after", False: "before"}),
                     milk=log.suggested_item == "toned milk")
    for w in ("before", "after"):
        part = log[log.window == w]
        out[(w, "ctr")] = part.clicks.sum() / part.impressions.sum()
        out[(w, "milk_share")] = part[part.milk].impressions.sum() / part.impressions.sum()
        for g, sel in (("milk", part.milk), ("other", ~part.milk)):
            sub = part[sel]
            out[(w, g)] = sub.clicks.sum() / sub.impressions.sum()
            out[(w, g, "add")] = sub.adds.sum() / sub.clicks.sum()
            out[(w, g, "slot")] = (sub.groupby("slot").clicks.sum()
                                   / sub.groupby("slot").impressions.sum()).to_dict()
        out[(w, "milk_by_slot")] = (part[part.milk].groupby("slot").impressions.sum()
                                    / part.groupby("slot").impressions.sum()).to_dict()
        daily = part.groupby("date")[["impressions", "clicks"]].sum()
        out[(w, "daily_ctr")] = (daily.clicks / daily.impressions)
        views = part[part.slot == 1].groupby("date").impressions.sum()
        out[(w, "views")] = views
    check("strip click-through 6.1 percent before and 3.8 after",
          round(out[("before", "ctr")], 3) == 0.061 and round(out[("after", "ctr")], 3) == 0.038)
    check("after the change: milk slots 1.2 percent, every other suggestion 6.4, milk on half the "
          "slot impressions",
          round(out[("after", "milk")], 3) == 0.012 and round(out[("after", "other")], 3) == 0.064
          and round(out[("after", "milk_share")], 2) == 0.50)
    check("before the change: milk on 2 percent of slot impressions, everything else 6.2 percent",
          round(out[("before", "milk_share")], 2) == 0.02 and round(out[("before", "other")], 3) == 0.062)
    check("cart-page views average 60,000 a day after the change",
          out[("after", "views")].mean() == 60_000)
    for w in ("before", "after"):
        for g in ("milk", "other"):
            s = out[(w, g, "slot")]
            if len(s) == 3:
                check(f"{w}, {g}: slot 1 draws more clicks than slot 2, slot 2 more than slot 3",
                      s[1] > s[2] > s[3])
        d = out[(w, "daily_ctr")]
        check(f"{w}: daily click-through moves (spread {d.min():.4f} to {d.max():.4f})",
              d.std() / d.mean() > 0.01 and d.nunique() == len(d))
    check("adds are half of clicks in each window, row by row they vary",
          abs(out[("after", "other", "add")] - 0.5) < 0.002
          and log.assign(r=log.adds / log.clicks.where(log.clicks > 0)).r.std() > 0.02)
    # What an added item sells for, from the items the strip suggested after the change.
    after = log[(log.date >= CHANGE_DAY.isoformat()) & (log.suggested_item != "toned milk")]
    w = after.groupby("suggested_item").adds.sum()
    out["price_per_add"] = sum(PRICE[i] * k for i, k in w.items()) / w.sum()
    milk_after = log[(log.date >= CHANGE_DAY.isoformat()) & (log.suggested_item == "toned milk")]
    out["milk_imp_day"] = milk_after.groupby("date").impressions.sum().mean()
    part = log[log.date >= CHANGE_DAY.isoformat()]
    out["after_ctr_exact"] = part.clicks.sum() / part.impressions.sum()
    # The same anchor, suggestion and slot in both windows, milk aside: like against like.
    cells = (log[~log.milk].groupby(["anchor_item", "suggested_item", "slot", "window"])
             [["impressions", "clicks"]].sum().unstack("window").dropna())
    rise = (cells[("clicks", "after")] / cells[("impressions", "after")]) / \
           (cells[("clicks", "before")] / cells[("impressions", "before")]) - 1
    out["same_cells"] = (len(rise), float(rise.min()), float(rise.max()))
    check(f"the {len(rise)} cells other than milk shown in both windows each clicked better after the "
          f"change, by {rise.min():.0%} to {rise.max():.0%}", len(rise) == 4 and (rise > 0).all())
    out["rows"] = len(log)
    return out


def verify_kalpa(products, orders, items):
    out = {}
    lines = items.groupby("order_id").apply(lambda g: (g.quantity * g.unit_price).sum())
    check("every one of the 1,000 v4 orders has lines that sum to its amount",
          len(orders) == 1000 and (lines.reindex(orders.order_id).values == orders.amount.values).all())
    q1 = orders[orders.order_date < "2026-07-01"].amount.sum()
    q2 = orders[orders.order_date >= "2026-07-01"].amount.sum()
    check("v4's quarters still sum to Rs 10.00 crore and Rs 9.84 crore",
          q1 == cz.V4_Q1_TOTAL and q2 == cz.V4_Q2_TOTAL)
    lp = products.set_index("product_id").list_price
    disc = items.unit_price / items.product_id.map(lp)
    check("every unit price sits between 75 and 100 percent of its list price",
          disc.min() >= 0.75 and disc.max() <= 1.0, f"({disc.min():.3f} to {disc.max():.3f})")
    consumer = orders[orders.segment != "Business"].order_id
    business = orders[orders.segment == "Business"].order_id
    per = items.groupby("order_id").size()
    check("consumer baskets hold one to eight lines; Business orders one line",
          per.reindex(consumer).between(1, 8).all() and (per.reindex(business) == 1).all())
    name = products.set_index("product_id").name
    baskets = items[items.order_id.isin(consumer)].groupby("order_id").product_id.apply(
        lambda s: set(name[p] for p in s)).reindex(consumer)
    out["baskets"] = len(baskets)
    out["business"] = len(business)
    out["lines_min"], out["lines_max"] = int(per.reindex(consumer).min()), int(per.reindex(consumer).max())
    b = list(baskets)
    n = len(b)
    single = Counter(x for s in b for x in s)
    out["charger"] = single["phone charger 20W"] / n
    charger_id = products.set_index("name").product_id["phone charger 20W"]
    out["charger_all"] = items[items.product_id == charger_id].order_id.nunique() / len(orders)
    check(f"the charger in {single['phone charger 20W']} of {n} baskets, 84 to 85 percent",
          0.84 <= out["charger"] <= 0.85)
    sc = measures(b, "screen protector", "phone charger 20W")
    out["screen"] = sc
    check("screen protector to charger: confidence prints 0.82, lift prints 0.97",
          f"{sc['conf_ab']:.2f}" == "0.82" and f"{sc['lift']:.2f}" == "0.97")
    lo_c = lo_l = 9.0
    hi_c = hi_l = 0.0
    for x in single:
        if x == "phone charger 20W" or single[x] / n < 0.02:
            continue
        m = measures(b, x, "phone charger 20W")
        lo_c, hi_c = min(lo_c, m["conf_ab"]), max(hi_c, m["conf_ab"])
        lo_l, hi_l = min(lo_l, m["lift"]), max(hi_l, m["lift"])
    out["charger_band"] = (lo_c, hi_c, lo_l, hi_l)
    check(f"every product in at least 2 percent of baskets: confidence to the charger {lo_c:.2f} to "
          f"{hi_c:.2f}, lift {lo_l:.2f} to {hi_l:.2f}",
          0.78 <= lo_c and hi_c <= 0.86 and 0.93 <= lo_l and hi_l <= 1.02)
    pairs = pairs_table(b)
    floor = pairs[pairs.support >= 0.05]
    top = floor.iloc[0]
    ec = measures(b, "earphone case", "wireless earphones")
    out["pair"] = ec
    seg = orders.set_index("order_id").segment
    pair_ids = [oid for oid, s in baskets.items() if {"wireless earphones", "earphone case"} <= s]
    out["pair_plus"] = sum(1 for o in pair_ids if seg[o] == "Retail-Plus") / len(pair_ids)
    check(f"above a 5 percent floor the strongest pair is earphones with their case, lift prints 3.1 "
          f"at support {ec['support']:.1%}, {out['pair_plus']:.0%} of it Retail-Plus",
          {top.a, top.b} == {"wireless earphones", "earphone case"} and f"{top.lift:.1f}" == "3.1"
          and round(ec["support"], 2) == 0.06 and out["pair_plus"] >= 0.70)
    thin = pairs[(pairs.support >= 0.002) & (pairs.support <= 0.004) & (pairs.lift >= 3.5)]
    check("exactly one pair in two or three baskets at lift 4.0", len(thin) == 1
          and {thin.iloc[0].a, thin.iloc[0].b} == {"car phone mount", "car charger"}
          and round(thin.iloc[0].lift, 1) == 4.0)
    out["thin"] = measures(b, "car phone mount", "car charger")
    out["floor_pairs"] = len(floor)
    out["pairs_plotted"] = int((pairs.support >= 0.001).sum())
    # The lab's twelve baskets: chosen by pattern, every value five points from the plants.
    want = [({"phone charger 20W", "screen protector", "wireless earphones", "earphone case"}, set()),
            ({"phone charger 20W", "screen protector"}, {"wireless earphones", "earphone case"}),
            ({"screen protector"}, {"phone charger 20W", "wireless earphones", "earphone case"}),
            ({"phone charger 20W", "wireless earphones", "earphone case"}, {"screen protector"}),
            (set(), {"phone charger 20W", "screen protector", "wireless earphones", "earphone case"}),
            ({"phone charger 20W", "wireless earphones"}, {"earphone case", "screen protector"}),
            ({"earphone case"}, {"phone charger 20W", "wireless earphones", "screen protector"})] + \
        [({"phone charger 20W"}, {"screen protector", "wireless earphones", "earphone case"})] * 5
    plain = {"car phone mount", "car charger"}
    chosen = []
    for has, lacks in want:
        for oid, s in baskets.items():
            if oid in chosen or not has <= s or s & lacks or plain & s or len(s) > 6:
                continue
            chosen.append(oid)
            break
    if len(chosen) != 12:
        raise AssertionError("the lab's twelve baskets could not be found")
    chosen.sort()
    t = [baskets[o] for o in chosen]
    tc = measures(t, "screen protector", "phone charger 20W")
    te = measures(t, "wireless earphones", "earphone case")
    share12 = sum(1 for s in t if "phone charger 20W" in s) / 12
    check("the lab's twelve baskets: charger in 9, screen protector to charger 0.67 and lift 0.89, "
          "earphones with case lift 2.67",
          share12 == 0.75 and round(tc["conf_ab"], 2) == 0.67 and round(tc["lift"], 2) == 0.89
          and round(te["lift"], 2) == 2.67)
    out["twelve"] = chosen
    out["twelve_sets"] = t
    out["twelve_m"] = (share12, tc, te)
    return out


# =========================================================================== the concept chapters' toys
# Each concept chapter teaches its subtopic on one invented example before the case applies it.
# The hostel canteen's twelve lunch orders carry the counting (SECTIONs 1 to 6), a month of the
# same canteen's orders in which no item depends on another carries the support floor's luck
# (SECTION 6), and Sharma Kirana's month carries the rupees (SECTION 9). Every value below is
# invented, labelled invented wherever it appears, and recorded under a toy_ id.
SUB1 = "Support, confidence and lift, derived by counting"
SUB2 = "The confidence trap; lift near one"
SUB3 = "Basket analysis on the order items"
SUB4 = "The support floor and the watch list"
SUB5 = "Cross-sell and upsell reasoning; expected value in rupees"
CANTEEN = [
    ("T01", ["dal rice", "papad", "chaas"]), ("T02", ["dal rice", "papad", "chaas"]),
    ("T03", ["dal rice", "papad", "chaas"]), ("T04", ["dal rice", "sabzi", "chaas"]),
    ("T05", ["dal rice", "chaas"]), ("T06", ["dal rice", "curd", "chaas"]),
    ("T07", ["roti", "papad", "pickle"]), ("T08", ["papad", "pickle"]),
    ("T09", ["roti", "sabzi", "chaas"]), ("T10", ["roti", "sabzi", "chaas"]),
    ("T11", ["roti", "sabzi", "chaas"]), ("T12", ["gulab jamun", "curd"]),
]
# The month: each item joins an order on its own coin, with these chances, whatever else is in
# the order, so any pull between two items in it is luck. An order that draws nothing is drawn
# again, since an order holds at least one item.
MONTH_MENU = {"chaas": 0.70, "dal rice": 0.50, "roti": 0.40, "sabzi": 0.40, "papad": 0.35,
              "curd": 0.04, "pickle": 0.04, "gulab jamun": 0.03, "kheer": 0.015, "jalebi": 0.012,
              "lassi": 0.012, "boiled egg": 0.010, "fruit plate": 0.008, "rasgulla": 0.008}
MONTH_ORDERS = 600
# Sharma Kirana, a Pune corner shop, one invented month, and a Rs 1-off tea-and-rusk combo card.
KIRANA = {"bills": 1000, "bills_with_tea": 600, "bills_with_rusk": 200, "bills_with_both": 150,
          "rusk_price_rs": 30, "rusk_cost_rs": 18, "combo_discount_rs": 1, "card_printing_rs": 20,
          "response_low": 0.02, "response_mid": 0.04, "response_high": 0.06}
KIRANA_NOTES = {
    "bills": "bills rung up in the month",
    "bills_with_tea": "bills holding a tea pack",
    "bills_with_rusk": "bills holding a rusk pack",
    "bills_with_both": "bills holding both",
    "rusk_price_rs": "what a rusk pack sells for",
    "rusk_cost_rs": "what a rusk pack costs the shop",
    "combo_discount_rs": "taken off every bill that holds tea and rusk once the card is up",
    "card_printing_rs": "printing the combo cards for the month",
    "response_low": "assumption, low end: share of tea bills without rusk that add a pack",
    "response_mid": "assumption, middle: the same share",
    "response_high": "assumption, high end: the same share",
}


def measures_of(baskets, a, b):
    """Counts, support, both confidences, expected and lift for one pair, from a list of sets."""
    n = len(baskets)
    na = sum(a in x for x in baskets)
    nb = sum(b in x for x in baskets)
    nab = sum(a in x and b in x for x in baskets)
    expected = n * (na / n) * (nb / n)
    return {"n": n, "na": na, "nb": nb, "nab": nab, "support": nab / n,
            "conf_ab": nab / na, "conf_ba": nab / nb, "expected": expected,
            "lift": nab / expected if expected else float("nan")}


def write_toys():
    """Write the three invented tables to data/ and return what the facts file needs."""
    lines = pd.DataFrame([(oid, item) for oid, items in CANTEEN for item in items],
                         columns=["order_id", "item"])
    lines.to_csv(DATA / "C2_W04_D03_canteen_order_lines_STUDENT.csv", index=False)
    rng = random.Random(SEED + 3)
    month = []
    while len(month) < MONTH_ORDERS:
        order = [x for x, p in MONTH_MENU.items() if rng.random() < p]
        if order:
            month.append(order)
    month_df = pd.DataFrame([(f"M{i:03d}", item) for i, order in enumerate(month, start=1)
                             for item in order], columns=["order_id", "item"])
    month_df.to_csv(DATA / "C2_W04_D03_canteen_month_STUDENT.csv", index=False)
    kirana = pd.DataFrame([(k, v, KIRANA_NOTES[k]) for k, v in KIRANA.items()],
                          columns=["line", "value", "what_it_is"], dtype=object)
    kirana.to_csv(DATA / "C2_W04_D03_kirana_month_STUDENT.csv", index=False)
    return lines, month_df, kirana


def verify_toys(lines, month_df, kirana):
    """Recount every toy from its CSV and assert the numbers the concept chapters print."""
    print("  the canteen's twelve lunch orders (invented)")
    baskets = [set(g) for _, g in lines.groupby("order_id").item]
    t = {"orders": len(baskets), "lines": len(lines), "items": lines.item.nunique()}
    t["count"] = Counter(x for b in baskets for x in b)
    pairs = Counter(p for b in baskets for p in combinations(sorted(b), 2))
    unsorted = Counter(p for b in baskets for p in combinations(b, 2)) + \
        Counter(p for b in baskets for p in combinations(sorted(b, reverse=True), 2))
    t["pair_lines"], t["distinct_pairs"] = sum(pairs.values()), len(pairs)
    t["pair_lines_both_orders"] = sum(unsorted.values())
    t["possible_pairs"] = t["items"] * (t["items"] - 1) // 2
    sizes = Counter(len(b) for b in baskets)
    t["three_line_orders"], t["two_line_orders"] = sizes[3], sizes[2]
    key = {"roti_sabzi": ("roti", "sabzi"), "dal_papad": ("dal rice", "papad"),
           "roti_chaas": ("roti", "chaas"), "dal_chaas": ("dal rice", "chaas"),
           "sabzi_chaas": ("sabzi", "chaas"), "papad_chaas": ("papad", "chaas"),
           "papad_pickle": ("papad", "pickle"), "gulab_curd": ("gulab jamun", "curd"),
           "curd_chaas": ("curd", "chaas"), "roti_pickle": ("roti", "pickle"),
           "dal_curd": ("dal rice", "curd"), "roti_papad": ("roti", "papad"),
           "dal_sabzi": ("dal rice", "sabzi")}
    t["m"] = {k: measures_of(baskets, a, b) for k, (a, b) in key.items()}
    rs = t["m"]["roti_sabzi"]
    t["roti_only"] = rs["na"] - rs["nab"]
    t["sabzi_only"] = rs["nb"] - rs["nab"]
    t["neither"] = 12 - rs["na"] - rs["nb"] + rs["nab"]
    t["roti_or_sabzi"] = rs["na"] + rs["nb"] - rs["nab"]
    four = [x for x in t["count"] if x != "chaas" and t["count"][x] >= 4]
    conf_chaas = {x: measures_of(baskets, x, "chaas")["conf_ab"] for x in four}
    lift_chaas = {x: measures_of(baskets, x, "chaas")["lift"] for x in four}
    t["chaas_four"], t["chaas_conf"], t["chaas_lift"] = four, conf_chaas, lift_chaas
    by_count = sorted(pairs.items(), key=lambda kv: (-kv[1], kv[0]))
    t["top_by_count"] = by_count[0]
    by_lift = sorted(((k * 12 / (t["count"][a] * t["count"][b]), (a, b), k) for (a, b), k in pairs.items()),
                     reverse=True)
    t["top_by_lift"] = by_lift[:3]
    m = t["m"]
    check("canteen: 12 orders, 33 lines, 8 items", (t["orders"], t["lines"], t["items"]) == (12, 33, 8))
    check("canteen: item counts as the plan gives them",
          dict(t["count"]) == {"chaas": 9, "dal rice": 6, "papad": 5, "roti": 4, "sabzi": 4,
                                "curd": 2, "pickle": 2, "gulab jamun": 1})
    check("canteen: 30 pairs from 33 lines, 13 distinct, 60 if every pair is counted both ways",
          (t["pair_lines"], t["distinct_pairs"], t["pair_lines_both_orders"]) == (30, 13, 60))
    check("canteen: nine three-line orders and three two-line orders", (sizes[3], sizes[2]) == (9, 3))
    check("roti and sabzi: support 0.25, confidence 0.75 both ways, expected 1.33, lift 2.25",
          (rs["nab"], rs["support"], rs["conf_ab"], rs["conf_ba"], round(rs["expected"], 2), rs["lift"])
          == (3, 0.25, 0.75, 0.75, 1.33, 2.25))
    check("roti and sabzi: the 2 by 2 reads 3, 1, 1 and 7",
          (rs["nab"], t["roti_only"], t["sabzi_only"], t["neither"]) == (3, 1, 1, 7))
    dp = m["dal_papad"]
    check("dal rice and papad: support 0.25, confidence 0.50 and 0.60, expected 2.5, lift 1.20",
          (dp["support"], dp["conf_ab"], dp["conf_ba"], dp["expected"], round(dp["lift"], 2))
          == (0.25, 0.5, 0.6, 2.5, 1.2))
    rc = m["roti_chaas"]
    check("roti and chaas: confidence 0.75, expected 3.0, lift exactly 1.00",
          (rc["conf_ab"], rc["expected"], rc["lift"]) == (0.75, 3.0, 1.0))
    dc = m["dal_chaas"]
    check("dal rice and chaas: 6 orders, confidence 1.00, expected 4.5, lift 1.33",
          (dc["nab"], dc["conf_ab"], dc["expected"], round(dc["lift"], 2)) == (6, 1.0, 4.5, 1.33))
    check("dal rice and chaas is the most frequent pair", t["top_by_count"] == (("chaas", "dal rice"), 6))
    sc = m["sabzi_chaas"]
    check("sabzi to chaas 1.00, chaas to sabzi 0.44", (sc["conf_ab"], round(sc["conf_ba"], 2)) == (1.0, 0.44))
    pc = m["papad_chaas"]
    check("papad and chaas: expected 3.75, lift 0.80", (pc["expected"], round(pc["lift"], 2)) == (3.75, 0.8))
    check("papad and pickle 2.40 on two orders", (m["papad_pickle"]["nab"], round(m["papad_pickle"]["lift"], 2)) == (2, 2.4))
    gc = m["gulab_curd"]
    check("gulab jamun and curd: 6.0 on one order, confidence 1.00 one way and 0.50 the other",
          (gc["nab"], round(gc["lift"], 2), gc["conf_ab"], gc["conf_ba"]) == (1, 6.0, 1.0, 0.5))
    check("by lift: gulab jamun and curd, then papad and pickle, then roti and sabzi",
          [p for _, p, _ in t["top_by_lift"]] == [("curd", "gulab jamun"), ("papad", "pickle"), ("roti", "sabzi")])
    check("the four items in four or more orders read confidence toward chaas 0.60 to 1.00",
          sorted(four) == ["dal rice", "papad", "roti", "sabzi"]
          and (round(min(conf_chaas.values()), 2), max(conf_chaas.values())) == (0.6, 1.0))
    check("...and lift with chaas 0.80 to 1.33",
          (round(min(lift_chaas.values()), 2), round(max(lift_chaas.values()), 2)) == (0.8, 1.33))

    print("  the canteen's month, no item depending on another (invented)")
    mb = [set(g) for _, g in month_df.groupby("order_id").item]
    n = len(mb)
    single = Counter(x for b in mb for x in b)
    mp = Counter(p for b in mb for p in combinations(sorted(b), 2))
    rows = [{"a": a, "b": b, "both": k, "support": k / n, "lift": k * n / (single[a] * single[b])}
            for (a, b), k in mp.items()]
    thin = sorted((r for r in rows if r["both"] <= 2), key=lambda r: -r["lift"])
    one = sorted((r for r in rows if r["both"] == 1), key=lambda r: -r["lift"])
    thick = [r for r in rows if r["both"] >= 30]
    mo = {"orders": n, "items": len(single), "lines": len(month_df), "pairs": len(rows),
          "pair_lines": sum(mp.values()), "thin": thin, "one": one, "thick": thick,
          "single": single, "thin_count": len(thin), "one_count": len(one),
          "two_count": sum(1 for r in rows if r["both"] == 2), "thick_count": len(thick),
          "thin_above_6": sum(1 for r in thin if r["lift"] > 6)}
    mo["thick_low"] = min(r["lift"] for r in thick)
    mo["thick_high"] = max(r["lift"] for r in thick)
    top = thin[0]
    mo["top"] = top
    check("month: 600 orders, 14 items", (n, len(single)) == (MONTH_ORDERS, len(MONTH_MENU)))
    check("month: the strongest pair on one or two orders reads lift above 6", top["lift"] > 6)
    check("month: every pair on 30 or more orders sits between 0.8 and 1.25",
          0.8 <= mo["thick_low"] and mo["thick_high"] <= 1.25)
    check("month: the most common pair sits near one", abs(max(thick, key=lambda r: r["both"])["lift"] - 1) < 0.1)

    print("  Sharma Kirana's month (invented)")
    k = dict(zip(kirana.line, kirana.value))
    ko = {key: k[key] for key in k}
    ko["tea_only"] = k["bills_with_tea"] - k["bills_with_both"]
    ko["support"] = k["bills_with_both"] / k["bills"]
    ko["tea_share"] = k["bills_with_tea"] / k["bills"]
    ko["rusk_share"] = k["bills_with_rusk"] / k["bills"]
    ko["conf_tea_rusk"] = k["bills_with_both"] / k["bills_with_tea"]
    ko["conf_rusk_tea"] = k["bills_with_both"] / k["bills_with_rusk"]
    ko["expected"] = k["bills"] * ko["tea_share"] * ko["rusk_share"]
    ko["lift"] = k["bills_with_both"] / ko["expected"]
    ko["margin"] = k["rusk_price_rs"] - k["rusk_cost_rs"]

    def worth(response, discount):
        packs = round(ko["tea_only"] * response)
        combos = k["bills_with_both"] + packs
        return packs, combos, packs * ko["margin"] - combos * discount - k["card_printing_rs"]

    ko["packs"], ko["combos"], ko["ev"] = worth(k["response_mid"], k["combo_discount_rs"])
    ko["packs_low"], _, ko["ev_low"] = worth(k["response_low"], k["combo_discount_rs"])
    ko["packs_high"], _, ko["ev_high"] = worth(k["response_high"], k["combo_discount_rs"])
    ko["ev_rs2"] = worth(k["response_mid"], 2)[2]
    ko["incremental_margin"] = ko["packs"] * ko["margin"]
    ko["discount_back"] = ko["combos"] * k["combo_discount_rs"]
    ko["sales_wrong"] = ko["combos"] * k["rusk_price_rs"]
    ko["every_combo_wrong"] = ko["combos"] * ko["margin"]
    ko["no_discount_wrong"] = ko["incremental_margin"] - k["card_printing_rs"]
    ko["before"] = k["bills_with_rusk"] * ko["margin"]
    ko["after"] = (k["bills_with_rusk"] + ko["packs"]) * ko["margin"] - ko["discount_back"] - k["card_printing_rs"]
    ko["breakeven"] = (ko["incremental_margin"] - k["card_printing_rs"]) / ko["combos"]
    # the same Rs 28 as a weighted average: a tea-only bill earns Rs 12 less Rs 1 with probability 0.04
    ko["net_new_pack"] = ko["margin"] - k["combo_discount_rs"]
    ko["per_bill"] = round(k["response_mid"] * ko["net_new_pack"], 4)
    ko["tea_only_total"] = round(ko["tea_only"] * ko["per_bill"])
    ko["both_cost"] = k["bills_with_both"] * k["combo_discount_rs"]
    check("kirana: support 0.15, confidence 0.25 from tea, rusk's share 0.20, lift 1.25",
          (ko["support"], ko["conf_tea_rusk"], ko["rusk_share"], ko["lift"]) == (0.15, 0.25, 0.2, 1.25))
    check("kirana: 450 tea bills without rusk, 18 packs, 168 combos",
          (ko["tea_only"], ko["packs"], ko["combos"]) == (450, 18, 168))
    check("kirana: Rs 216 of margin, Rs 168 handed back, Rs 20 of printing, Rs 28 a month",
          (ko["incremental_margin"], ko["discount_back"], k["card_printing_rs"], ko["ev"]) == (216, 168, 20, 28))
    check("kirana: Rs 2 off loses Rs 140", ko["ev_rs2"] == -140)
    check("kirana: the overstatements Rs 5,040, Rs 2,016 and Rs 196",
          (ko["sales_wrong"], ko["every_combo_wrong"], ko["no_discount_wrong"]) == (5040, 2016, 196))
    check("kirana: the second route, Rs 2,428 against Rs 2,400, is the same Rs 28",
          (ko["before"], ko["after"], ko["after"] - ko["before"]) == (2400, 2428, 28))
    check("kirana: 2 and 6 percent give -Rs 71 and Rs 127", (ko["ev_low"], ko["ev_high"]) == (-71, 127))
    check("kirana: the weighted average, Rs 0.44 on each of 450 bills, less Rs 150 and Rs 20, is Rs 28",
          (ko["per_bill"], ko["tea_only_total"], ko["tea_only_total"] - ko["both_cost"] - k["card_printing_rs"]) == (0.44, 198, 28))
    return t, mo, ko


def toy_facts(f, t, mo, ko):
    """The toy_ ids: every number of every invented example, each with its chapter and its use."""
    def inv(sub, why):
        return f"invented for the concept chapter on {sub}: {why}"

    S = "toy"
    s1, s2, s3, s4, s5 = (f"half1 SECTION {n}" for n in (1, 2, 3, 4, 5))
    f(S, "toy_canteen_orders", t["orders"], "12", inv(SUB1, "a hostel canteen's lunch orders, table data/C2_W04_D03_canteen_order_lines_STUDENT.csv"), f"{s1} to SECTION 6, notebooks 01 to 06, notes, cheat sheet, canteen_concepts set")
    f(S, "toy_canteen_lines", t["lines"], "33", inv(SUB3, "order lines, one row per item in an order"), f"{s5}, notebook 05, notes, cheat sheet")
    f(S, "toy_canteen_items", t["items"], "eight", inv(SUB1, "items on the canteen's menu"), f"{s1}, notebook 01, notebook 05")
    f(S, "toy_canteen_pair_lines", t["pair_lines"], "30", inv(SUB3, "pairs counted once per order: 9 three-line orders give 27, 3 two-line orders give 3"), f"{s5}, notebook 05, Kahoot, notes, cheat sheet, canteen_concepts Q5")
    f(S, "toy_canteen_distinct_pairs", t["distinct_pairs"], "13", inv(SUB3, "distinct pairs found in at least one order"), f"{s5}, notebook 05")
    f(S, "toy_canteen_pair_lines_both_orders", t["pair_lines_both_orders"], "60", inv(SUB3, "the trap: every pair counted once in each order of its two names"), f"{s5}, notebook 05")
    f(S, "toy_canteen_possible_pairs", t["possible_pairs"], "28", inv(SUB3, "pairs eight items could form, 8 x 7 / 2 (a distractor)"), f"{s5}, notebook 05")
    f(S, "toy_canteen_three_line_orders", t["three_line_orders"], "nine", inv(SUB3, "orders with three lines"), f"{s5}, notebook 05")
    f(S, "toy_canteen_two_line_orders", t["two_line_orders"], "three", inv(SUB3, "orders with two lines"), f"{s5}, notebook 05")
    f(S, "toy_canteen_pairs_from_three", t["three_line_orders"] * 3, "27", inv(SUB3, "nine three-line orders, three pairs each"), f"{s5}, notebook 05")
    f(S, "toy_canteen_four_item_pairs", 6, "six", inv(SUB3, "a basket of four items adds 4 x 3 / 2 pairs"), f"{s5}, notebook 05, canteen_concepts Q5")
    for item, fid in (("chaas", "chaas"), ("dal rice", "dal_rice"), ("papad", "papad"), ("roti", "roti"),
                      ("sabzi", "sabzi"), ("curd", "curd"), ("pickle", "pickle"), ("gulab jamun", "gulab_jamun")):
        c = t["count"][item]
        f(S, f"toy_canteen_{fid}_orders", c, str(c), inv(SUB1, f"orders, of the twelve, holding {item}"), f"{s1} to SECTION 6, notebooks 01 to 06")
        f(S, f"toy_canteen_{fid}_share", round(c / 12, 4), f"{c / 12:.2f}", inv(SUB1, f"{item}'s share of the twelve orders, {c} of 12"), f"{s1} to SECTION 4, notebooks 01 to 04")
    names = {"roti_sabzi": "roti and sabzi", "dal_papad": "dal rice and papad", "roti_chaas": "roti and chaas",
             "dal_chaas": "dal rice and chaas", "sabzi_chaas": "sabzi and chaas", "papad_chaas": "papad and chaas",
             "papad_pickle": "papad and pickle", "gulab_curd": "gulab jamun and curd", "curd_chaas": "curd and chaas",
             "roti_pickle": "roti and pickle", "dal_curd": "dal rice and curd", "roti_papad": "roti and papad",
             "dal_sabzi": "dal rice and sabzi"}
    sub_of = {"roti_sabzi": SUB1, "dal_papad": SUB1, "roti_chaas": SUB1, "dal_chaas": SUB2, "sabzi_chaas": SUB2,
              "papad_chaas": SUB2, "papad_pickle": SUB4, "gulab_curd": SUB4, "curd_chaas": SUB3,
              "roti_pickle": SUB3, "dal_curd": SUB3, "roti_papad": SUB3, "dal_sabzi": SUB3}
    for key, x in t["m"].items():
        nm, sub = names[key], sub_of[key]
        a, b = nm.split(" and ")
        f(S, f"toy_canteen_{key}_both", x["nab"], str(x["nab"]), inv(sub, f"orders holding {nm}"), "notebooks 01 to 06, half1 SECTIONs 1 to 6")
        f(S, f"toy_canteen_{key}_support", round(x["support"], 4), f"{x['support']:.2f}", inv(sub, f"{x['nab']} of 12 orders hold {nm}"), "notebooks 01 and 05, half1 SECTIONs 1 and 5")
        f(S, f"toy_canteen_{key}_conf_ab", round(x["conf_ab"], 4), f"{x['conf_ab']:.2f}", inv(sub, f"confidence from {a} to {b}, {x['nab']} of {x['na']}"), "notebooks 02 to 05, half1 SECTIONs 2 to 5")
        f(S, f"toy_canteen_{key}_conf_ba", round(x["conf_ba"], 4), f"{x['conf_ba']:.2f}", inv(sub, f"confidence from {b} to {a}, {x['nab']} of {x['nb']}"), "notebooks 02 to 05, half1 SECTIONs 2 to 5")
        f(S, f"toy_canteen_{key}_expected", round(x["expected"], 4), f"{x['expected']:.2f}".rstrip("0").rstrip("."), inv(sub, f"12 x {x['na']}/12 x {x['nb']}/12, the orders chance alone gives {nm}"), "notebooks 03 to 06, half1 SECTIONs 3 to 6")
        f(S, f"toy_canteen_{key}_lift", round(x["lift"], 4), f"{x['lift']:.2f}", inv(sub, f"{x['nab']} seen over {x['expected']:.2f} expected for {nm}"), "notebooks 03 to 06, half1 SECTIONs 3 to 6, notes, cheat sheet")
    f(S, "toy_canteen_roti_only", t["roti_only"], "1", inv(SUB1, "orders with roti and no sabzi"), f"{s1}, notebook 01, cheat sheet panel 1")
    f(S, "toy_canteen_sabzi_only", t["sabzi_only"], "1", inv(SUB1, "orders with sabzi and no roti"), f"{s1}, notebook 01, cheat sheet panel 1")
    f(S, "toy_canteen_neither", t["neither"], "7", inv(SUB1, "orders with neither roti nor sabzi"), f"{s1}, notebook 01, cheat sheet panel 1")
    f(S, "toy_canteen_roti_or_sabzi", t["roti_or_sabzi"], "5", inv(SUB1, "orders holding roti or sabzi or both (a distractor)"), f"{s1}, notebook 01")
    f(S, "toy_canteen_roti_plus_sabzi", 8, "8", inv(SUB1, "the trap: roti's 4 orders plus sabzi's 4, added without looking inside the orders"), f"{s1}, notebook 01, canteen_concepts Q1")
    lo_c, hi_c = min(t["chaas_conf"].values()), max(t["chaas_conf"].values())
    lo_l, hi_l = min(t["chaas_lift"].values()), max(t["chaas_lift"].values())
    f(S, "toy_canteen_chaas_conf_low", round(lo_c, 4), f"{lo_c:.2f}", inv(SUB2, "lowest confidence toward chaas among the four items in four or more orders (papad)"), f"{s4}, notebook 04, notes, cheat sheet panel 2")
    f(S, "toy_canteen_chaas_conf_high", round(hi_c, 4), f"{hi_c:.2f}", inv(SUB2, "highest, dal rice and sabzi"), f"{s4}, notebook 04, notes, cheat sheet panel 2")
    f(S, "toy_canteen_chaas_lift_low", round(lo_l, 4), f"{lo_l:.2f}", inv(SUB2, "lowest lift with chaas among the same four (papad)"), f"{s4}, notebook 04, notes, cheat sheet panel 2")
    f(S, "toy_canteen_chaas_lift_high", round(hi_l, 4), f"{hi_l:.2f}", inv(SUB2, "highest, dal rice and sabzi"), f"{s4}, notebook 04, notes, cheat sheet panel 2")
    f(S, "toy_canteen_items_four_or_more", 4, "four", inv(SUB2, "items other than chaas in four or more of the twelve orders"), f"{s4}, notebook 04")
    f(S, "toy_canteen_floor_orders", 3, "3", inv(SUB4, "the floor on the twelve orders: a pair must sit in three before its lift is read"), "half1 SECTION 6, notebook 06, canteen_concepts Q6")
    f(S, "toy_canteen_lift_bar", 1.5, "1.5", inv(SUB4, "the lift a pair needs above the floor to be promoted, as the case uses"), "half1 SECTION 6, notebook 06")
    f(S, "toy_check_popular_share", 0.6, "60 percent", inv(SUB2, "the chapter's check question: an item in 60 percent of a shop's bills"), f"{s4}, notebook 04")
    f(S, "toy_check_partner_conf", 0.66, "0.66", inv(SUB2, "the partner's confidence toward it"), f"{s4}, notebook 04")
    f(S, "toy_check_partner_lift", 1.1, "1.10", inv(SUB2, "0.66 over 0.60"), f"{s4}, notebook 04")
    f(S, "toy_sweep_share_low", 0.2, "0.2", inv(SUB2, "the sweep's lowest share for the popular item, lift held at one"), "notebook 04")
    f(S, "toy_sweep_share_high", 0.9, "0.9", inv(SUB2, "the sweep's highest share"), "notebook 04")
    top = mo["top"]
    f(S, "toy_month_orders", mo["orders"], "600", inv(SUB4, "a month of the canteen's orders in which no item depends on another, data/C2_W04_D03_canteen_month_STUDENT.csv"), "half1 SECTION 6, notebook 06, notes")
    f(S, "toy_month_items", mo["items"], "14", inv(SUB4, "items on the month's menu, the eight plus six rarer specials"), "notebook 06")
    f(S, "toy_month_lines", mo["lines"], f"{mo['lines']:,}", inv(SUB4, "order lines in the month"), "notebook 06")
    f(S, "toy_month_pairs", mo["pairs"], str(mo["pairs"]), inv(SUB4, "distinct pairs found in at least one of the 600 orders"), "notebook 06")
    f(S, "toy_month_thin_pairs", mo["thin_count"], str(mo["thin_count"]), inv(SUB4, "pairs on one or two orders"), "notebook 06")
    f(S, "toy_month_thin_above_6", mo["thin_above_6"], str(mo["thin_above_6"]), inv(SUB4, "of those, pairs reading lift above 6"), "notebook 06")
    f(S, "toy_month_thin_top_lift", round(top["lift"], 4), f"{top['lift']:.2f}", inv(SUB4, f"{top['a']} and {top['b']}, the strongest pair on one or two orders"), "half1 SECTION 6, notebook 06, notes")
    f(S, "toy_month_thin_top_orders", top["both"], str(top["both"]), inv(SUB4, f"orders holding {top['a']} and {top['b']}"), "half1 SECTION 6, notebook 06, notes")
    for item in (top["a"], top["b"]):
        f(S, f"toy_month_{item.replace(' ', '_')}_orders", mo["single"][item], str(mo["single"][item]), inv(SUB4, f"orders of the 600 holding {item}"), "notebook 06")
    f(S, "toy_month_thin_top_expected", round(mo["single"][top["a"]] * mo["single"][top["b"]] / mo["orders"], 4),
      f"{mo['single'][top['a']] * mo['single'][top['b']] / mo['orders']:.2f}", inv(SUB4, "what chance alone gives the pair"), "notebook 06")
    one = mo["one"][0]
    f(S, "toy_month_one_top_lift", round(one["lift"], 4), f"{one['lift']:.2f}", inv(SUB4, f"{one['a']} and {one['b']}, the strongest pair on a single order"), "notebook 06")
    f(S, "toy_month_thick_floor", 30, "30", inv(SUB4, "orders a pair needs to count as thick in the month, Week 1 Thursday's thirty"), "half1 SECTION 6, notebook 06")
    f(S, "toy_month_thick_pairs", mo["thick_count"], str(mo["thick_count"]), inv(SUB4, "pairs on 30 or more orders"), "half1 SECTION 6, notebook 06")
    f(S, "toy_month_thick_low", round(mo["thick_low"], 4), f"{mo['thick_low']:.2f}", inv(SUB4, "lowest lift among them"), "half1 SECTION 6, notebook 06, notes")
    f(S, "toy_month_thick_high", round(mo["thick_high"], 4), f"{mo['thick_high']:.2f}", inv(SUB4, "highest lift among them"), "half1 SECTION 6, notebook 06, notes")
    s9 = "half2 SECTION 9"
    for key, val, shown, why in (
            ("bills", ko["bills"], "1,000", "Sharma Kirana's bills in one month"),
            ("tea_bills", ko["bills_with_tea"], "600", "bills holding tea"),
            ("rusk_bills", ko["bills_with_rusk"], "200", "bills holding rusk"),
            ("both_bills", ko["bills_with_both"], "150", "bills holding both"),
            ("tea_only", ko["tea_only"], "450", "tea bills with no rusk, the ones a combo card could reach"),
            ("support", ko["support"], "0.15", "150 of 1,000"),
            ("tea_share", ko["tea_share"], "0.60", "600 of 1,000"),
            ("rusk_share", ko["rusk_share"], "0.20", "200 of 1,000"),
            ("conf_tea_rusk", ko["conf_tea_rusk"], "0.25", "150 of 600"),
            ("conf_rusk_tea", ko["conf_rusk_tea"], "0.75", "150 of 200"),
            ("expected", ko["expected"], "120", "1,000 x 0.60 x 0.20"),
            ("lift", ko["lift"], "1.25", "150 over 120"),
            ("rusk_price", ko["rusk_price_rs"], "Rs 30", "a rusk pack's price"),
            ("rusk_cost", ko["rusk_cost_rs"], "Rs 18", "a rusk pack's cost to the shop"),
            ("margin", ko["margin"], "Rs 12", "Rs 30 less Rs 18"),
            ("discount", ko["combo_discount_rs"], "Rs 1", "the combo card's discount on a bill holding both"),
            ("printing", ko["card_printing_rs"], "Rs 20", "printing the cards for the month"),
            ("response", ko["response_mid"], "4 percent", "assumption: share of the 450 that add a pack, range 2 to 6 percent"),
            ("response_low", ko["response_low"], "2 percent", "assumption, low end"),
            ("response_high", ko["response_high"], "6 percent", "assumption, high end"),
            ("packs", ko["packs"], "18", "450 x 4 percent, the incremental packs"),
            ("packs_low", ko["packs_low"], "9", "450 x 2 percent"),
            ("packs_high", ko["packs_high"], "27", "450 x 6 percent"),
            ("combos", ko["combos"], "168", "150 who bought both anyway plus the 18 new ones"),
            ("incremental_margin", ko["incremental_margin"], "Rs 216", "18 packs x Rs 12"),
            ("discount_back", ko["discount_back"], "Rs 168", "Rs 1 on each of 168 combo bills"),
            ("ev", ko["ev"], "Rs 28", "Rs 216 less Rs 168 less Rs 20, the expected value a month"),
            ("ev_low", ko["ev_low"], "-Rs 71", "the same at 2 percent: 9 x 12 less 159 less 20"),
            ("ev_high", ko["ev_high"], "Rs 127", "the same at 6 percent: 27 x 12 less 177 less 20"),
            ("ev_rs2", ko["ev_rs2"], "-Rs 140", "the same card at Rs 2 off, response held at 4 percent"),
            ("sales_wrong", ko["sales_wrong"], "Rs 5,040", "the trap: 168 combo bills x Rs 30 of rusk sales"),
            ("every_combo_wrong", ko["every_combo_wrong"], "Rs 2,016", "a distractor: every combo counted as incremental, 168 x Rs 12"),
            ("no_discount_wrong", ko["no_discount_wrong"], "Rs 196", "a distractor: the discount forgotten, Rs 216 less Rs 20"),
            ("before", ko["before"], "Rs 2,400", "rusk margin before the card, 200 x Rs 12"),
            ("after", ko["after"], "Rs 2,428", "rusk margin after it, 218 x Rs 12 less Rs 168 less Rs 20"),
            ("breakeven", round(ko["breakeven"], 4), "Rs 1.17", "the discount at which the card earns nothing, Rs 196 over 168"),
            ("sales_multiple", 180, "180 times", "Rs 5,040 over Rs 28"),
            ("net_new_pack", ko["net_new_pack"], "Rs 11", "a new pack's margin less the Rs 1 its bill takes back"),
            ("per_bill", ko["per_bill"], "Rs 0.44", "the expected value of one tea-only bill: 0.04 x Rs 11 plus 0.96 x Rs 0"),
            ("no_response", round(1 - ko["response_mid"], 2), "0.96", "the share of tea-only bills that add nothing, 1 less 0.04"),
            ("tea_only_total", ko["tea_only_total"], "Rs 198", "450 tea-only bills x Rs 0.44"),
            ("both_cost", ko["both_cost"], "Rs 150", "Rs 1 on each of the 150 bills that held both before the card")):
        f(S, f"toy_kirana_{key}", val, shown, inv(SUB5, why), f"{s9}, notebook 09, notes, cheat sheet panel 5, canteen_concepts Q7")
    for key, val, shown, why in (
            ("bills", 2000, "2,000", "the check question: bills a combo card reaches"),
            ("response", 0.05, "5 percent", "the share that add one extra pack"),
            ("margin", 10, "Rs 10", "the margin on that pack"),
            ("cost", 600, "Rs 600", "the cards' cost"),
            ("packs", 100, "100", "2,000 x 5 percent"),
            ("ev", 400, "Rs 400", "100 x Rs 10 less Rs 600")):
        f(S, f"toy_check_ev_{key}", val, shown, inv(SUB5, why), f"{s9}, notebook 09")


# =========================================================================== the facts file
def lakh(rs):
    return f"Rs {rs / 1e5:.1f} lakh"


def indian(n):
    """Rs amounts in the Indian grouping: 12,64,000."""
    s = f"{int(round(n))}"
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    groups = []
    while len(head) > 2:
        groups.insert(0, head[-2:])
        head = head[:-2]
    if head:
        groups.insert(0, head)
    return ",".join(groups + [tail])


OLD_CHAPTER = {"1": "SECTION 7", "2": "SECTION 8", "3": "SECTION 10"}
OLD_NOTEBOOK = {"1": "07", "2": "08", "3": "10", "4": "11"}


def renumber(used):
    """The case chapters moved behind the concept block on 13 October 2026: chapter 1 is SECTION 7,
    chapter 2 SECTION 8, chapter 3 SECTION 10, and notebooks 01 to 04 became 07, 08, 10 and 11."""
    used = re.sub(r"\bchapter 2 and 3\b", "SECTIONs 8 and 10", used)
    used = re.sub(r"\bchapter (\d)\b", lambda m: OLD_CHAPTER[m.group(1)], used)
    return re.sub(r"\bnotebook 0([1-4])\b", lambda m: "notebook " + OLD_NOTEBOOK[m.group(1)], used)


def write_facts(case, strip, kalpa, toys):
    """Every number a learner sees, with how it was computed and the form it is printed in."""
    sh, m = case["share"], case["m"]
    bm, em = m[("bread", "toned milk")], m[("eggs", "toned milk")]
    cc, ic = m[("chips", "cold drink")], m[("ice cream", "chocolate sauce")]
    cg, bb, ot = m[("coriander", "green chillies")], m[("bread", "butter")], m[("onions", "tomatoes")]
    views, add, margin = 60_000, 0.5, 9
    other_day = views * 0.064 * add * margin
    milk_day = views * 0.012 * add * margin
    gap_day = other_day - milk_day
    gap_month = gap_day * 30
    share_after = strip[("after", "milk_share")]
    recover = gap_day * 3 * 0.5 * 30            # milk on half the impressions, 1.5 slots' worth
    ceiling = gap_day * 3 * 30
    adds_day = views * 0.064 * add
    gross_day = adds_day * strip["price_per_add"]
    F = []

    def f(section, fid, value, shown, how, used):
        # a toy names the new chapter and notebook numbers already; only the case's old ones move
        F.append((section, fid, value, shown, how, used if fid.startswith("toy_") else renumber(used)))

    S = "ticket"
    f(S, "before_strip_ctr", 0.061, "6.1 percent", "clicks over impressions, 17 August to 6 September 2026, strip_log", "every file's ticket")
    f(S, "after_strip_ctr", 0.038, "3.8 percent", "clicks over impressions, 7 to 27 September 2026, strip_log", "every file's ticket")
    f(S, "change_date", "2026-09-07", "Monday 7 September 2026", "the day the ranking switched", "the ticket")
    f(S, "total_carts", N_CARTS, "40,000", "carts in the carts table", "the ticket, notebook 02")
    f(S, "customers", case["customers"], "12,000", "customers in the sample, every September cart of each", "notebook 02, notes")
    f(S, "zones", len(ZONES), "eight", "Pune zones in the data", "the ticket")
    f(S, "items", case["items"], "59", "distinct items in cart_items (the case file says about 60)", "notebook 02, notes")
    f(S, "cart_window", "1 to 28 September 2026", "1 to 28 September", "the carts' window, four weeks", "the ticket")
    f(S, "heavy_tenth_share", round(case["heavy_share"], 4), "38 percent", "carts placed by the 1,200 customers with the most carts, over 40,000", "ticket caveat, notebook 03, deck")
    f(S, "heavy_customers", 1200, "1,200", "the top tenth of 12,000 customers", "notebook 03, notes")
    f(S, "heavy_carts_min", case["heavy_min"], str(case["heavy_min"]), "fewest carts held by any top-tenth customer", "notebook 03")
    f(S, "light_carts_max", case["light_max"], str(case["light_max"]), "most carts held by anyone outside the top tenth", "notebook 03")
    S = "strip"
    f(S, "milk_slot_ctr_after", 0.012, "1.2 percent", "clicks over impressions on slots suggesting toned milk, after", "chapter 2, notebook 02")
    f(S, "other_slot_ctr_after", 0.064, "6.4 percent", "the same for every other suggestion, after", "chapter 2, notebook 02")
    f(S, "other_slot_ctr_before", 0.062, "6.2 percent", "every suggestion other than milk, before", "chapter 2, notebook 02")
    f(S, "milk_share_after", round(share_after, 4), "50 percent", "milk's share of slot impressions, after (case file 44, corrected)", "chapter 2, notebook 02")
    f(S, "milk_share_before", round(strip[("before", "milk_share")], 4), "2 percent", "milk's share of slot impressions under the curated list", "chapter 2, notebook 02")
    for w in ("before", "after"):
        for g in ("milk", "other"):
            s = strip[(w, g, "slot")]
            for k, v in s.items():
                f(S, f"ctr_{w}_{g}_slot{k}", round(v, 4), f"{v * 100:.1f} percent", f"click-through on slot {k}, {g}, {w}", "the slot picture, notebook 02")
    for k, v in strip[("after", "milk_by_slot")].items():
        f(S, f"milk_share_after_slot{k}", round(v, 4), f"{v * 100:.0f} percent", f"milk's share of slot {k}'s impressions after the change", "notebook 02, the slot picture")
    va, vb = strip[("after", "views")], strip[("before", "views")]
    f(S, "views_a_day_after", 60_000, "60,000", "slot-1 impressions a day, the mean of 7 to 27 September; every view shows all three slots", "chapter 3 cascade, notebook 03")
    f(S, "views_a_day_before", round(vb.mean()), f"{round(vb.mean()):,}", "the same for 17 August to 6 September", "notebook 02")
    f(S, "views_day_low", int(va.min()), f"{int(va.min()):,}", "the quietest day after the change", "notebook 02")
    f(S, "views_day_high", int(va.max()), f"{int(va.max()):,}", "the busiest day after the change", "notebook 02")
    d = strip[("after", "daily_ctr")]
    f(S, "daily_ctr_after_low", round(d.min(), 4), f"{d.min() * 100:.1f} percent", "lowest daily strip click-through after the change", "notebook 02")
    f(S, "daily_ctr_after_high", round(d.max(), 4), f"{d.max() * 100:.1f} percent", "highest daily strip click-through after the change", "notebook 02")
    d = strip[("before", "daily_ctr")]
    f(S, "daily_ctr_before_low", round(d.min(), 4), f"{d.min() * 100:.1f} percent", "lowest daily strip click-through before the change", "notebook 02")
    f(S, "daily_ctr_before_high", round(d.max(), 4), f"{d.max() * 100:.1f} percent", "highest daily strip click-through before the change", "notebook 02")
    f(S, "add_rate_observed", round(strip[("after", "other", "add")], 4), "0.5", "adds over clicks after the change, strip_log", "chapter 3, notebook 03")
    f(S, "margin_per_line_observed", round(case["margin_line"], 2), f"Rs {case['margin_line']:.1f}", "mean margin_rs of a cart_items line, milk aside", "chapter 3, notebook 03")
    f(S, "milk_margin", MARGIN["toned milk"], f"Rs {MARGIN['toned milk']:.0f}", "margin_rs on a pouch of toned milk", "notebook 03, transcript")
    f(S, "price_per_add_observed", round(strip["price_per_add"], 2), f"Rs {strip['price_per_add']:.0f}", "unit price of the same items, weighted by adds", "notebook 03, the gross-sales trap")
    f(S, "strip_rows", strip["rows"], f"{strip['rows']:,}", "rows in strip_log", "notebook 02")
    S = "full_data"
    for name in ("toned milk", "bread", "eggs", "curd", "bananas", "onions", "tomatoes", "potatoes",
                 "coriander", "chips", "cold drink", "green chillies", "paneer", "butter",
                 "ice cream", "chocolate sauce"):
        fid = name.replace(" ", "_") + "_share"
        v = sh[name]
        shown = f"{v * 100:.2f} percent" if v < 0.02 else f"{v * 100:.1f} percent".replace(".0 percent", " percent")
        f(S, fid, round(v, 4), shown, f"share of the 40,000 carts holding {name}", "chapter 2, notebook 02")
        f(S, fid.replace("_share", "_carts"), case["count"][name], f"{case['count'][name]:,}", f"carts holding {name}", "notebook 02")
    for key, fid in ((("bread", "toned milk"), "bread_milk"), (("eggs", "toned milk"), "eggs_milk"),
                     (("chips", "cold drink"), "chips_cold"), (("ice cream", "chocolate sauce"), "ice_choc"),
                     (("coriander", "green chillies"), "coriander_chillies"), (("bread", "butter"), "bread_butter"),
                     (("onions", "tomatoes"), "onions_tomatoes"), (("curd", "toned milk"), "curd_milk"),
                     (("bananas", "toned milk"), "bananas_milk")):
        x = m[key]
        f(S, f"{fid}_carts", x["nab"], f"{x['nab']:,}", f"carts holding both {key[0]} and {key[1]}", "chapter 2 and 3")
        sup = x["support"]
        f(S, f"{fid}_support", round(sup, 4), f"{sup * 100:.2f} percent" if sup < 0.01 else f"{sup * 100:.1f} percent", f"both over 40,000", "chapter 2 and 3")
        f(S, f"{fid}_conf_ab", round(x["conf_ab"], 4), f"{x['conf_ab']:.2f}", f"confidence {key[0]} to {key[1]}", "chapter 2 and 3")
        f(S, f"{fid}_conf_ba", round(x["conf_ba"], 4), f"{x['conf_ba']:.2f}", f"confidence {key[1]} to {key[0]}", "chapter 2 and 3")
        f(S, f"{fid}_lift", round(x["lift"], 4), f"{x['lift']:.2f}", f"lift of {key[0]} and {key[1]}", "chapter 2 and 3")
        f(S, f"{fid}_expected", round(x["na"] * x["nb"] / N_CARTS), f"{round(x['na'] * x['nb'] / N_CARTS):,}", f"carts expected to hold both if independent", "chapter 2, notebook 02")
    n2, lo_c, hi_c, lo_l, hi_l = case["common"]
    f(S, "common_items", n2, str(n2), "items other than milk in at least 2 percent of carts", "chapter 2, notebook 02")
    f(S, "common_conf_low", round(lo_c, 4), f"{lo_c:.2f}", "lowest confidence to milk among them", "chapter 2, notebook 02")
    f(S, "common_conf_high", round(hi_c, 4), f"{hi_c:.2f}", "highest confidence to milk among them", "chapter 2, notebook 02")
    f(S, "common_lift_low", round(lo_l, 4), f"{lo_l:.2f}", "lowest lift with milk among them", "chapter 2, notebook 02")
    f(S, "common_lift_high", round(hi_l, 4), f"{hi_l:.2f}", "highest lift with milk among them", "chapter 2, notebook 02")
    f(S, "pairs_seen", case["pairs_seen"], f"{case['pairs_seen']:,}", "distinct pairs found in at least one cart", "notebook 02")
    f(S, "lines", case["lines"], f"{case['lines']:,}", "rows in cart_items", "notebook 02")
    f(S, "double_loop_checks", case["pairs_seen"] * N_CARTS, "about 68 million", "1,711 possible pairs tested against each of 40,000 carts", "notes, chapter 2 sizing")
    check("the double loop's size prints as about 68 million", 67_500_000 <= case["pairs_seen"] * N_CARTS < 68_500_000)
    f(S, "pair_increments", case["pair_increments"], f"about {round(case['pair_increments'], -3):,}", "pairs added by Counter: each cart adds one per pair it holds", "notes, chapter 2 sizing")
    f(S, "items_per_cart", round(case["items_per_cart"], 2), f"{case['items_per_cart']:.1f}", "mean distinct items in a cart", "notes, chapter 2 sizing")
    f(S, "bread_milk_excess", 0.0423, "4 percent", "lift 1.0423 less one: bread buyers take milk 4 percent more often than all shoppers", "interview transcript")
    f(S, "pairs_per_cart", round(case["pair_increments"] / N_CARTS, 2), f"{case['pair_increments'] / N_CARTS:.1f}", "pairs Counter adds for an average cart", "notes, chapter 2 sizing")
    f(S, "bread_price", 45, "Rs 45", "bread's price in cart_items", "chapter 3, the margin definition")
    f(S, "bread_margin", 6.7, "Rs 6.70", "bread's margin in cart_items", "chapter 3, the margin definition")
    f(S, "cart_value_median", case["value_median"], f"Rs {case['value_median']:.0f}", "median cart value", "notebook 02")
    S = "floor"
    f(S, "support_floor", 0.01, "1 percent", "the support floor the room sets", "chapter 3")
    f(S, "plot_floor", 0.001, "0.1 percent", "the least support a pair needs to be drawn on the action map", "chapter 3 picture")
    f(S, "plot_floor_carts", 40, "40", "0.1 percent of 40,000 carts", "drill 2")
    f(S, "pairs_plotted", case["pairs_plotted"], f"{case['pairs_plotted']:,}", "pairs with support of at least 0.1 percent", "chapter 3 picture, drill 2")
    f(S, "watch_band_low", 0.002, "0.2 percent", "the low end of the band searched for a strong thin pair", "chapter 3, notebook 03")
    f(S, "watch_band_low_carts", 80, "80", "0.2 percent of 40,000 carts", "chapter 3, notebook 03")
    f(S, "common_floor", 0.02, "2 percent", "an item counts as common at this share of carts (the case file)", "chapter 2")
    f(S, "kalpa_floor", 0.05, "5 percent", "the lab's support floor (the case file)", "notebook 04, lab note")
    f(S, "support_floor_carts", 400, "400", "1 percent of 40,000 carts", "chapter 3")
    f(S, "floor_pairs", case["floor_pairs"], str(case["floor_pairs"]), "pairs at or above the floor", "chapter 3, notebook 03")
    f(S, "floor_pairs_lift_1_5", case["floor_above_1_5"], str(case["floor_above_1_5"]), "of those, pairs at lift 1.5 or more", "chapter 3, notebook 03")
    a, b2, l = case["next_after_four"]
    f(S, "fifth_pair_lift", round(l, 4), f"{l:.2f}", f"the fifth pair above the floor, {a} and {b2}", "notebook 03")
    f(S, "watch_band_pairs", case["watch_band_pairs"], str(case["watch_band_pairs"]), "pairs between 0.2 and 1 percent support", "notebook 03")
    tn, tl = case["tiny"]
    f(S, "tiny_pairs", tn, f"{tn:,}", "pairs below 0.2 percent support", "notebook 03")
    f(S, "tiny_lift_max", round(tl, 4), f"{tl:.1f}", "highest lift among them", "notebook 03")
    S = "caveats"
    f(S, "chips_cold_lift_per_customer", round(case["cc_cust"], 4), f"{case['cc_cust']:.2f}", "lift with every customer counted once (each cart weighs one over its customer's carts)", "chapter 3, notebook 03")
    f(S, "bread_milk_lift_per_customer", round(case["bm_cust"], 4), f"{case['bm_cust']:.2f}", "the same for bread and milk", "chapter 3, notebook 03")
    for (a, b2), fid in ((("chips", "cold drink"), "chips_cold"), (("coriander", "green chillies"), "coriander_chillies"),
                         (("bread", "butter"), "bread_butter"), (("onions", "tomatoes"), "onions_tomatoes")):
        v = case["size_lift"][(a, b2)]
        f(S, f"{fid}_lift_size", round(v, 4), f"{v:.2f}", f"{a} and {b2}, lift with chance counted within each cart size", "interview room, half2")
    for (a, b2), fid in ((("chips", "cold drink"), "chips_cold"), (("onions", "tomatoes"), "onions_tomatoes")):
        v = case["both_lift"][(a, b2)]
        f(S, f"{fid}_lift_both", round(v, 4), f"{v:.2f}", f"{a} and {b2}, each customer once and chance counted within each cart size", "interview room, half2")
    f(S, "chips_cold_heavy_share", round(case["cc_heavy_share"], 4), f"{case['cc_heavy_share'] * 100:.0f} percent", "share of chips-and-cold-drink carts placed by the top tenth", "chapter 3, notebook 03")
    for bnd, v in case["milk_by_band"].items():
        f(S, f"milk_share_{bnd}", round(v, 4), f"{v * 100:.0f} percent", f"share of {bnd} carts holding milk", "chapter 3, notebook 03")
    for bnd, v in case["bm_by_band"].items():
        f(S, f"bread_milk_lift_{bnd}", round(v, 4), f"{v:.2f}", f"bread and milk lift among {bnd} carts", "notebook 03")
    f(S, "stockout_zones", "Hadapsar and Viman Nagar", "Hadapsar and Viman Nagar", "the two zones", "ticket caveat, chapter 3")
    f(S, "stockout_week", "15 to 21 September 2026", "15 to 21 September", "week three", "chapter 3")
    f(S, "stockout_carts", case["stock_carts"], f"{case['stock_carts']:,}", "carts in the two zones in week three", "notebook 03")
    f(S, "stockout_curd_carts", case["stock_curd"], str(case["stock_curd"]), "of those, carts with curd", "notebook 03")
    f(S, "curd_share_stockout", round(case["curd_in_stock"], 4), f"{case['curd_in_stock'] * 100:.1f} percent", "curd's share in the two zones in week three", "chapter 3, notebook 03")
    f(S, "curd_share_elsewhere", round(case["curd_elsewhere"], 4), f"{case['curd_elsewhere'] * 100:.1f} percent", "curd's share everywhere else", "chapter 3, notebook 03")
    f(S, "curd_cell_low", round(case["curd_cell_min"], 4), f"{case['curd_cell_min'] * 100:.0f} percent", "lowest curd share in any other zone-week", "notebook 03")
    f(S, "curd_cell_high", round(case["curd_cell_max"], 4), f"{case['curd_cell_max'] * 100:.0f} percent", "highest curd share in any other zone-week", "notebook 03")
    ca, ck = case["curd_all"], case["curd_kept"]
    f(S, "curd_share_all", round(ca["na"] / ca["n"], 4), f"{ca['na'] / ca['n'] * 100:.1f} percent", "curd's share of all 40,000 carts", "notebook 03")
    f(S, "curd_share_kept", round(ck["na"] / ck["n"], 4), f"{ck['na'] / ck['n'] * 100:.1f} percent", "curd's share with the two zone-weeks set aside", "chapter 3, notebook 03")
    f(S, "curd_milk_lift_all", round(ca["lift"], 4), f"{ca['lift']:.2f}", "curd and milk lift, all carts", "chapter 3, notebook 03")
    f(S, "curd_milk_lift_kept", round(ck["lift"], 4), f"{ck['lift']:.2f}", "curd and milk lift, the two zone-weeks set aside", "chapter 3, notebook 03")
    f(S, "curd_milk_support_all", round(ca["nab"] / ca["n"], 4), f"{ca['nab'] / ca['n'] * 100:.1f} percent", "curd with milk over all carts", "notebook 03")
    f(S, "curd_milk_support_kept", round(ck["nab"] / ck["n"], 4), f"{ck['nab'] / ck['n'] * 100:.1f} percent", "curd with milk, the two zone-weeks set aside", "notebook 03")
    S = "slot_value"
    f(S, "views_assumed", views, "60,000", "cart-page views a day, the after-change mean in strip_log", "chapter 3, notebook 03")
    f(S, "add_rate_assumed", add, "0.5", "assumption, range 0.4 to 0.6 (strip_log reads 0.50)", "chapter 3, notebook 03")
    f(S, "add_rate_low", 0.4, "0.4", "the range's low end", "chapter 3, notebook 03")
    f(S, "add_rate_high", 0.6, "0.6", "the range's high end", "chapter 3, notebook 03")
    f(S, "margin_assumed", margin, "Rs 9", "assumption, range Rs 7 to Rs 11", "chapter 3, notebook 03")
    f(S, "margin_low", 7, "Rs 7", "the range's low end", "chapter 3, notebook 03")
    f(S, "margin_high", 11, "Rs 11", "the range's high end", "chapter 3, notebook 03")
    f(S, "impressions_a_day", 3 * views, f"{3 * views:,}", "60,000 views a day, each showing three slots", "chapter 3, notebook 03")
    f(S, "value_per_click_mid", 4.5, "Rs 4.50", "0.5 adds a click x Rs 9", "chapter 3, notebook 03")
    f(S, "value_per_click_low", 2.8, "Rs 2.80", "0.4 x Rs 7, the low end", "chapter 3, notebook 03")
    f(S, "value_per_click_high", 6.6, "Rs 6.60", "0.6 x Rs 11, the high end", "chapter 3, notebook 03")
    f(S, "slot_value_other_day", round(other_day), "Rs 17,280", "60,000 x 0.064 x 0.5 x 9", "chapter 3, cheat sheet")
    f(S, "slot_value_milk_day", round(milk_day), "Rs 3,240", "60,000 x 0.012 x 0.5 x 9", "chapter 3, cheat sheet")
    f(S, "slot_gap_day", round(gap_day), "Rs 14,040", "17,280 less 3,240, a slot a day", "chapter 3")
    f(S, "slot_gap_month", round(gap_month), lakh(gap_month), "14,040 x 30, a slot a month (the case file's Rs 4.2 lakh)", "chapter 3")
    f(S, "slot_value_other_month", round(other_day * 30), lakh(other_day * 30), "17,280 x 30", "notebook 03")
    f(S, "slot_value_milk_month", round(milk_day * 30), lakh(milk_day * 30), "3,240 x 30", "notebook 03")
    f(S, "milk_slots_worth", 1.5, "1.5", "three slots times milk's half of the impressions", "chapter 3")
    f(S, "recoverable_month", round(recover), lakh(recover), "14,040 x 3 x 0.50 x 30: what re-ranking recovers on milk's half", "chapter 3, half2, notes")
    f(S, "ceiling_month", round(ceiling), lakh(ceiling), "14,040 x 3 x 30: only if every slot showed milk (the case file's Rs 12.6 lakh)", "notebook 03")
    lo = views * (0.064 - 0.012) * 0.4 * 7 * 3 * 0.5 * 30
    hi = views * (0.064 - 0.012) * 0.6 * 11 * 3 * 0.5 * 30
    f(S, "recoverable_low", round(lo), lakh(lo), "add rate 0.4 and margin Rs 7", "chapter 3, notebook 03")
    f(S, "recoverable_high", round(hi), lakh(hi), "add rate 0.6 and margin Rs 11", "chapter 3, notebook 03")
    f(S, "clicks_a_day", round(60_000 * 0.064), f"{round(60_000 * 0.064):,}", "60,000 x 0.064", "board work, the cascade")
    f(S, "adds_a_day", round(adds_day), f"{round(adds_day):,}", "60,000 x 0.064 x 0.5", "notebook 03, the trap")
    f(S, "gross_sales_day", round(gross_day), f"Rs {indian(gross_day)}", "1,920 adds x the average price of an added item", "notebook 03, the trap")
    thin_views = views * 0.04
    m_sauce, m_milk = MARGIN["chocolate sauce"], MARGIN["toned milk"]
    thin_month = thin_views * 30 * (0.064 * add * m_sauce - 0.012 * add * m_milk)
    f(S, "ice_cream_views_day", round(thin_views), f"{round(thin_views):,}", "60,000 views x ice cream's 4 percent of carts, if views follow carts", "interview room, half1, half2, notes")
    f(S, "sauce_margin", m_sauce, f"Rs {m_sauce:.2f}", "margin_rs on a bottle of chocolate sauce", "interview room, half1, notes")
    f(S, "thin_rule_month", round(thin_month), "about Rs 85,000", "2,400 x 30 x (0.064 x 0.5 x Rs 37.40 - 0.012 x 0.5 x Rs 2): sauce in place of milk beside ice cream, each add at its own margin, sauce clicking like the rest", "interview room, half1, half2, notes")
    n_same, r_lo, r_hi = strip["same_cells"]
    f(S, "same_cells", n_same, "four", "anchor, suggestion and slot cells other than milk shown in both windows", "the [D] transcript")
    f(S, "same_cells_rise_low", round(r_lo, 4), f"{r_lo * 100:.0f} percent", "the smallest rise in click-through among them", "the [D] transcript")
    f(S, "same_cells_rise_high", round(r_hi, 4), f"{r_hi * 100:.0f} percent", "the largest rise in click-through among them", "the [D] transcript")
    milk_at_own = views * 30 * 3 * 0.5 * (0.064 * add * margin - 0.012 * add * m_milk)
    f(S, "recoverable_month_milk_own", round(milk_at_own), lakh(milk_at_own), "60,000 x 30 x 1.5 x (0.064 x 0.5 x Rs 9 - 0.012 x 0.5 x Rs 2): milk priced at its own margin", "interview room")
    p0 = case["m"][("ice cream", "chocolate sauce")]["conf_ab"]
    lift_pts = 0.064 * add
    n_arm = [(1.96 + 0.8416) ** 2 * (p0 * (1 - p0) + (p0 + e) * (1 - p0 - e)) / e ** 2 for e in (lift_pts, lift_pts / 2)]
    f(S, "trial_lift_points", lift_pts, "3.2 points", "0.064 x 0.5: the share of ice-cream carts the strip's sauce adds would reach, if every add were new", "interview room, trainer")
    f(S, "trial_n_full", round(n_arm[0]), "about 1,100", "ice-cream carts an arm to detect 6.25 to 9.45 percent buying sauce, 5 percent two-sided, 80 percent power", "interview room, trainer")
    f(S, "trial_n_half", round(n_arm[1]), "about 4,000", "the same for half that effect, if half the adds would have come anyway", "interview room, trainer")
    f(S, "ice_cream_cart_margin_sd", round(case["ic_margin_sd"], 2), f"Rs {case['ic_margin_sd']:.0f}", "standard deviation of a whole ice-cream cart's margin", "interview room, trainer")
    f(S, "serving_cost_10p_month", round(views * 0.10 * 30), lakh(views * 0.10 * 30), "60,000 views x Rs 0.10 x 30: ten paise of serving cost a view, a month", "interview room, AI variant")
    f(S, "serving_breakeven_paise", round(recover / (views * 30) * 100, 1), "35 paise", "Rs 6.3 lakh / (60,000 x 30): the serving cost a view that uses up the re-rank's recovery", "interview room, AI variant")
    S = "twelve_rows"
    f(S, "twelve_milk", 8, "8", "carts of the twelve holding milk", "chapter 1, notebook 01, cheat sheet")
    f(S, "twelve_bread", 4, "4", "carts holding bread", "chapter 1, notebook 01")
    f(S, "twelve_bread_milk", 4, "4", "carts holding bread and milk", "chapter 1")
    f(S, "twelve_bread_support", 0.3333, "0.33", "4 of 12", "chapter 1")
    f(S, "twelve_bread_milk_conf", 1.0, "1.00", "4 of 4", "chapter 1, cheat sheet")
    f(S, "twelve_milk_to_bread_conf", 0.5, "0.50", "4 of 8", "chapter 1, notebook 01")
    f(S, "twelve_bread_milk_expected", 2.6667, "2.67", "(4/12) x (8/12) x 12", "chapter 1")
    f(S, "twelve_bread_milk_lift", 1.5, "1.50", "4 over 2.67", "chapter 1, cheat sheet")
    f(S, "twelve_chips", 3, "3", "carts holding chips", "chapter 1")
    f(S, "twelve_cold", 3, "3", "carts holding a cold drink", "chapter 1")
    f(S, "twelve_chips_cold", 2, "2", "carts holding both", "chapter 1")
    f(S, "twelve_chips_cold_support", 0.1667, "0.17", "2 of 12", "chapter 1")
    f(S, "twelve_chips_cold_conf", 0.6667, "0.67", "2 of 3", "chapter 1")
    f(S, "twelve_chips_cold_expected", 0.75, "0.75", "(3/12) x (3/12) x 12", "chapter 1")
    f(S, "twelve_chips_cold_lift", 2.6667, "2.67", "2 over 0.75", "chapter 1, cheat sheet")
    f(S, "twelve_ice_choc", 1, "1", "the one cart with both", "chapter 1")
    f(S, "twelve_ice_choc_lift", 12.0, "12", "1 over (1/12)", "chapter 1")
    S = "toy"
    f(S, "weight_example_carts", 4, "4", "invented: a shopper with four carts", "chapter 3, counting each customer once")
    f(S, "weight_example", 0.25, "0.25", "one over four: each of that shopper's carts weighs 0.25", "chapter 3, counting each customer once")
    toy_facts(f, *toys)
    S = "public"
    f(S, "instamart_orders_per_store", 1089, "1,089", "Swiggy Instamart orders per dark store per day, quarter to June 2026 (T3, checked 12 October 2026)", "guesstimate")
    f(S, "instamart_stores", 1171, "1,171", "Swiggy Instamart dark stores, same source (T3)", "guesstimate")
    f(S, "instamart_cities", 131, "131", "cities those 1,171 dark stores span, same source (T3, checked 12 October 2026)", "guesstimate")
    f(S, "maxxsaver_mtu_share", 0.28, "over 28 percent", "Maxxsaver users among MTUs (W4)", "chapter 3, notes")
    f(S, "maxxsaver_aov", 612, "Rs 612", "Maxxsaver AOV, up 16 percent (W4)", "chapter 3, notes")
    f(S, "osco_transactions", 1_200_000, "about 1.2 million", "Osco Drug transactions, 1992 (W2)", "chapter 2, notes")
    f(S, "uber_cross_use", 3, "over three times", "bookings of consumers who use rides and delivery (W4)", "chapter 3, notes")
    f(S, "walmart_poptarts", 7, "about seven times", "strawberry Pop-Tarts before Charley (W3)", "fallback")
    f(S, "maxxsaver_aov_growth", 0.16, "16 percent", "Instamart AOV growth quarter on quarter, Q1 FY26 letter (W4, checked 12 October 2026)", "chapter 3, notes")
    f(S, "uber_both_share", 0.2, "about one in five", "eligible consumers active monthly in both rides and delivery, Uber 10-K for 2025 (W4)", "notes")
    S = "guesstimate"
    g_hh, g_hl, g_hh_hi = 40_000, 30_000, 50_000
    g_ad, g_ad_lo, g_ad_hi = 0.30, 0.20, 0.40       # households using quick commerce in a week
    g_sc, g_sc_lo, g_sc_hi = 0.50, 0.35, 0.65       # Instamart's slice of them
    g_sh, g_sl, g_s_hi = round(g_ad * g_sc, 2), round(g_ad_lo * g_sc_lo, 2), round(g_ad_hi * g_sc_hi, 2)
    g_ow, g_ol, g_o_hi = 1.5, 1.0, 2.0
    g_mid, g_low, g_high = g_hh * g_sh * g_ow / 7, g_hl * g_sl * g_ol / 7, g_hh_hi * g_s_hi * g_o_hi / 7
    for fid, val, shown, how in (
            ("gs_radius", 2.5, "2.5 km", "assumption: a dark store's delivery radius"),
            ("gs_area", 19.6, "about 20 square km", "3.14 x 2.5 x 2.5"),
            ("gs_density", 2000, "about 2,000", "assumption: households a square km in a large city's residential belt"),
            ("gs_households", g_hh, "40,000", "assumption: households a dark store's catchment holds, about 20 x 2,000"),
            ("gs_households_low", g_hl, "30,000", "assumption's low end"),
            ("gs_households_high", g_hh_hi, "50,000", "assumption's high end"),
            ("gs_adoption", g_ad, "30 percent", "assumption: households using quick commerce in a given week"),
            ("gs_adoption_low", g_ad_lo, "20", "assumption's low end, in percent"),
            ("gs_adoption_high", g_ad_hi, "40 percent", "assumption's high end"),
            ("gs_slice", g_sc, "half", "assumption: Instamart's slice of those households"),
            ("gs_slice_low", g_sc_lo, "35", "assumption's low end, in percent"),
            ("gs_slice_high", g_sc_hi, "65 percent", "assumption's high end"),
            ("gs_share_week", g_sh, "15 percent", "30 percent x half: share of the catchment ordering from Instamart in a given week"),
            ("gs_share_low", g_sl, "7", "20 percent x 35 percent, in percent"),
            ("gs_share_high", g_s_hi, "26", "40 percent x 65 percent, in percent"),
            ("gs_orders_week", g_ow, "1.5", "assumption: orders a week from each ordering household"),
            ("gs_orders_low", g_ol, "1", "assumption's low end"),
            ("gs_orders_high", g_o_hi, "2", "assumption's high end"),
            ("gs_orders_day", round(g_mid, 1), "about 1,290", "40,000 x 0.15 x 1.5 / 7"),
            ("gs_orders_day_low", round(g_low, 1), "about 300", "30,000 x 0.07 x 1 / 7"),
            ("gs_orders_day_high", round(g_high, 1), "about 3,710", "50,000 x 0.26 x 2 / 7"),
            ("gs_gap", round(g_mid / 1089 - 1, 4), "18 percent", "the estimate above Swiggy's 1,089"),
            ("gs_share_needed", round(1089 * 7 / (g_hh * g_ow), 4), "about 13 percent", "the weekly share that lands on 1,089: 1,089 x 7 / (40,000 x 1.5)"),
            ("gs_share_low_day", round(g_hh * g_sl * g_ow / 7, 1), "about 600", "40,000 x 0.07 x 1.5 / 7: the share alone at its low end"),
            ("gs_share_high_day", round(g_hh * g_s_hi * g_ow / 7, 1), "about 2,230", "40,000 x 0.26 x 1.5 / 7: the share alone at its high end"),
            ("gs_orders_only_low_day", round(g_hh * g_sh * g_ol / 7, 1), "about 860", "40,000 x 0.15 x 1 / 7: orders a week alone at its low end"),
            ("gs_orders_only_high_day", round(g_hh * g_sh * g_o_hi / 7, 1), "about 1,710", "40,000 x 0.15 x 2 / 7: orders a week alone at its high end")):
        f(S, fid, val, shown, how, "guesstimate: notes and the trainer sheet")
    S = "pairs_detail"
    for name in sorted(sh):
        if name in ("toned milk", "bread", "eggs", "curd", "bananas", "onions", "tomatoes", "potatoes",
                    "coriander", "chips", "cold drink", "green chillies", "paneer", "butter",
                    "ice cream", "chocolate sauce"):
            continue
        f(S, name.replace(" ", "_") + "_share", round(sh[name], 4), f"{sh[name]:.3f}", f"share of carts holding {name}", "notebook 02 output")
    for a, b2, k in case["top_by_count"]:
        f(S, f"by_count_{a}_{b2}".replace(" ", "_"), k, f"{k:,}", f"carts holding {a} and {b2}, ranked by count", "chapter 2, notebook 02")
    for a, b2, k, sup, l in case["floor_rows"] + case["band_rows"]:
        key = f"pair_{a}_{b2}".replace(" ", "_")
        if f"{key}_carts" in {x[1] for x in F}:
            continue
        f(S, f"{key}_carts", k, f"{k:,}", f"carts holding {a} and {b2}", "notebook 03 output")
        f(S, f"{key}_support", round(sup, 4), f"{sup:.4f}", f"their support", "notebook 03 output")
        f(S, f"{key}_lift", round(l, 4), f"{l:.4f}", f"their lift", "notebook 03 output")
    for (zone, week), val in sorted(case["curd_grid"].items()):
        f(S, f"curd_{zone}_w{week}".replace(" ", "_").lower(), round(val, 4), f"{val * 100:.0f} percent", f"curd's share in {zone}, week {week}", "chapter 3 picture, notebook 03")
    f(S, "bread_milk_expected_share", round(sh["bread"] * sh["toned milk"], 4), f"{sh['bread'] * sh['toned milk']:.3f}", "bread's share times milk's share", "chapter 2, notebook 02")
    f(S, "after_strip_ctr_exact", round(strip["after_ctr_exact"], 4), f"{strip['after_ctr_exact']:.4f}", "the after rate before rounding to 3.8 percent", "notebook 02 output")
    f(S, "milk_impressions_a_day", round(strip["milk_imp_day"]), f"{round(strip['milk_imp_day']):,}", "milk impressions a day after the change, all three slots", "notebook 03, the second route")
    f(S, "milk_lift_band_low", 0.96, "0.96", "the case file's band for lift with milk, low end", "notebook 02 check")
    f(S, "milk_lift_band_high", 1.08, "1.08", "the case file's band for lift with milk, high end", "notebook 02 check")
    S = "predict_options"
    f(S, "option_rs_50000", 50_000, "Rs 50,000", "invented distractor on the month-recovered predict slide", "chapter 3 predict")
    f(S, "option_rs_2_lakh", 200_000, "Rs 2 lakh", "invented distractor", "chapter 3 predict")
    f(S, "option_rs_6_lakh", 600_000, "Rs 6 lakh", "the rounded key", "chapter 3 predict")
    f(S, "option_rs_50_lakh", 5_000_000, "Rs 50 lakh", "invented distractor", "chapter 3 predict")
    S = "exercise_numbers"
    f(S, "slot_value_no_add_rate", round(views * 0.064 * margin), "Rs 34,560", "60,000 x 0.064 x Rs 9, the add rate left out (a distractor)", "unguided strip exercise")
    f(S, "conf_ratio_distractor", 1.88, "1.88", "0.45 / 0.24, a ratio of two confidences (a distractor)", "drill 1")
    f(S, "inverse_conf_distractor", 2.22, "2.22", "3,200 / 1,440 (a distractor)", "drill 1")
    f(S, "lift_rule_floor", 1.5, "1.5", "the drill's rule: lift at least 1.5 above the support floor", "drill 2")
    f(S, "kalpa_charger_cost", 120, "Rs 120", "unit cost of the charger, products table", "Kalpa exercise")
    f(S, "kalpa_bundle_discount", 20, "Rs 20", "assumption: merchandising's discount on a bundled charger", "Kalpa exercise")
    f(S, "kalpa_margin_at_list", 79, "Rs 79", "199 less 120", "Kalpa exercise")
    f(S, "kalpa_margin_bundled", 59, "Rs 59", "199 less 20 less 120", "Kalpa exercise")
    f(S, "kalpa_price_bundled", 179, "Rs 179", "199 less 20 (a distractor)", "Kalpa exercise")
    f(S, "kalpa_margin_distractor", 99, "Rs 99", "79 plus 20 (a distractor)", "Kalpa exercise")
    S = "practice_toy"
    for fid, val, shown, how in (
            ("hardware_bills", 200, "200", "invented: a Nagpur hardware shop's bills in a week"),
            ("hardware_paint", 90, "90", "invented: bills with paint"),
            ("hardware_brushes", 50, "50", "invented: bills with brushes"),
            ("hardware_both", 28, "28", "invented: bills with paint and brushes"),
            ("hardware_support", 0.14, "0.14", "28 of 200"),
            ("hardware_brushes_conf", 0.56, "0.56", "28 of 50, from brushes to paint"),
            ("hardware_paint_conf", 0.3111, "0.31", "28 of 90, from paint to brushes"),
            ("hardware_expected", 22.5, "22.5", "200 x 90/200 x 50/200"),
            ("hardware_lift", 1.2444, "1.24", "28 over 22.5"),
            ("hardware_sandpaper", 80, "80", "invented: bills with sandpaper"),
            ("hardware_sandpaper_paint", 36, "36", "invented: bills with sandpaper and paint"),
            ("hardware_sandpaper_conf", 0.45, "0.45", "36 of 80"),
            ("hardware_sandpaper_expected", 36, "36", "200 x 80/200 x 90/200"),
            ("hardware_sandpaper_lift", 1.0, "1.00", "36 over 36"),
            ("hardware_paint_share", 0.45, "45 percent", "90 of 200"),
            ("hardware_sandpaper_no_paint", 44, "44", "80 less 36"),
            ("practice_clicks", 1_500, "1,500", "30,000 x 0.05"),
            ("practice_views", 30_000, "30,000", "invented: cart-page views a day"),
            ("practice_ctr", 0.05, "5 percent", "invented: click-through"),
            ("practice_margin", 10, "Rs 10", "invented: margin an add"),
            ("practice_discount", 3, "Rs 3", "invented: bundle discount an add"),
            ("practice_adds", 750, "750", "30,000 x 0.05 x 0.5"),
            ("practice_gross_margin", 7_500, "Rs 7,500", "750 x Rs 10"),
            ("practice_returned", 2_250, "Rs 2,250", "750 x Rs 3"),
            ("practice_net", 5_250, "Rs 5,250", "7,500 less 2,250"),
            ("practice_no_add_rate", 15_000, "Rs 15,000", "a distractor: the add rate left out"),
            ("practice_sales_distractor", 22_500, "Rs 22,500", "a distractor: 750 adds x Rs 30 price"),
            ("practice_price", 30, "Rs 30", "invented: price of the added item"),
            ("pair_a_support", 0.12, "12 percent", "invented pair A"), ("pair_a_lift", 1.05, "1.05", "invented pair A"),
            ("pair_b_support", 0.04, "4 percent", "invented pair B"), ("pair_b_lift", 2.6, "2.6", "invented pair B"),
            ("pair_c_support", 0.004, "0.4 percent", "invented pair C"), ("pair_c_lift", 6.0, "6.0", "invented pair C"),
            ("pair_d_support", 0.02, "2 percent", "invented pair D"), ("pair_d_lift", 1.8, "1.8", "invented pair D"),
            ("bundle_x_lift", 1.02, "1.02", "invented bundle X"), ("bundle_x_support", 0.3, "30 percent", "invented bundle X"),
            ("bundle_y_lift", 2.4, "2.4", "invented bundle Y"), ("bundle_y_support", 0.03, "3 percent", "invented bundle Y"),
            ("bundle_y_margin", 12, "Rs 12", "invented bundle Y margin an add"),
            ("bundle_z_lift", 5.0, "5.0", "invented bundle Z"), ("bundle_z_support", 0.002, "0.2 percent", "invented bundle Z")):
        f(S, fid, val, shown, how, "practice lab set")
    S = "kahoot_toy"
    for fid, val, shown, how in (
            ("kahoot_popular_share", 0.75, "75 percent", "invented: the popular item's share of carts"),
            ("kahoot_partner_conf", 0.76, "0.76", "invented: the partner's confidence toward it"),
            ("kahoot_partner_lift", 1.01, "1.01", "0.76 over 0.75"),
            ("kahoot_blend_sum", 0.076, "7.6 percent", "a distractor: 1.2 plus 6.4"),
            ("kahoot_blend_gap", 0.026, "2.6 percent", "a distractor: 6.4 less 3.8"),
            ("kahoot_cart_pairs", 3, "3", "C033861 holds three items, so it adds three pairs, 3 x 2 / 2"),
            ("kahoot_cart_ordered", 6, "6", "a distractor: each pair counted once in each order"),
            ("kahoot_cart_square", 9, "9", "a distractor: every item paired with every item, itself included")):
        f(S, fid, val, shown, how, "Kahoot")
    S = "fallback"
    for name, (k, rows) in case["slices"].items():
        fid = "slice_" + name.replace(", ", "_").replace(" ", "_").lower()
        f(S, fid + "_carts", k, f"{k:,}", f"carts in {name}", "fallback S6 and S7, the rerun")
    for name in ("Kothrud, evening", "Baner, morning", "Hinjewadi, night", "Viman Nagar, week three"):
        k, rows = case["slices"][name]
        base = "slice_" + name.replace(", ", "_").replace(" ", "_").lower()
        for a, b2, l, both in rows[:4]:
            key = f"{base}_{a}_{b2}".replace(" ", "_")
            f(S, key + "_lift", round(l, 4), f"{l:.2f}", f"lift of {a} and {b2} in {name}", "take-home self-check")
            f(S, key + "_carts", both, f"{both:,}", f"carts holding {a} and {b2} in {name}", "take-home self-check")
    slips = case["thin_slips"]
    f(S, "slice_thin_slips", len(slips), str(len(slips)), "pairs above the floor that outrank bread and butter in Hinjewadi at night", "fallback S7")
    f(S, "slice_thin_carts_max", max(r[3] for r in slips), str(max(r[3] for r in slips)), "most carts behind any of those pairs", "fallback S7")
    f(S, "slice_thin_carts_min", min(r[3] for r in slips), str(min(r[3] for r in slips)), "fewest carts behind any of them", "fallback S7")
    w3, w4 = case["curd_hadapsar"]
    f(S, "curd_hadapsar_week3", round(w3, 4), f"{w3 * 100:.1f} percent", "curd's share in Hadapsar, week three", "fallback S6")
    f(S, "curd_hadapsar_week4", round(w4, 4), f"{w4 * 100:.0f} percent", "curd's share in Hadapsar, week four", "fallback S6")
    for name in ("Kothrud, evening", "Baner, morning", "Hinjewadi, night", "Viman Nagar, week three"):
        k = case["slices"][name][0]
        base = "slice_" + name.replace(", ", "_").replace(" ", "_").lower()
        f(S, base + "_floor", round(k / 100, 2), f"{k / 100:.2f}", f"1 percent of the carts in {name}", "take-home brief and self-check")
        f(S, base + "_floor_min", math.ceil(k / 100), str(math.ceil(k / 100)), f"fewest carts a pair needs to clear the floor in {name}", "take-home self-check")
    S = "preread"
    f(S, "thursday_blended_retention", 0.38, "38 percent", "Thursday's ticket: blended month-two retention, June to September (case file target)", "pre-read")
    f(S, "thursday_jan_month_one", 0.58, "58 percent", "Thursday's ticket: January cohort's month-one rate (case file target)", "pre-read")
    f(S, "thursday_jul_month_one", 0.49, "49 percent", "Thursday's ticket: July cohort (case file target)", "pre-read")
    f(S, "thursday_aug_month_one", 0.31, "31 percent", "Thursday's ticket: August sale cohort (case file target)", "pre-read")
    f(S, "thursday_aug_size", 2.6, "2.6 times", "Thursday's ticket: the August cohort against a normal month (case file target)", "pre-read")
    f(S, "thursday_android_before", 0.58, "58 percent", "Thursday's ticket: members' add-to-cart to order on Android before 14 September (case file target)", "pre-read")
    f(S, "thursday_android_after", 0.44, "44 percent", "Thursday's ticket: the same after (case file target)", "pre-read")
    f(S, "thursday_members", 53_089, "53,089", "Thursday's ticket: members signed up January to September 2026 (the spine's Thursday ticket and the case file)", "pre-read")
    f(S, "thursday_aug_members", 13_000, "13,000", "Thursday's ticket: the August cohort, 2.6 times the 5,000 a month of January to July (case file)", "pre-read")
    f(S, "thursday_normal_month", 5_000, "5,000", "Thursday's ticket: members a month, January to July (case file)", "pre-read")
    S = "week_map"
    f(S, "monday_trips_per_hour_before", 1.9, "1.9", "Monday's target in the W04 spine, section 5", "slide two's week map")
    f(S, "monday_trips_per_hour_after", 1.6, "1.6", "Monday's target in the W04 spine, section 5", "slide two's week map")
    f(S, "tuesday_bookings_per_hour_before", 314, "Rs 314", "Tuesday's target in the W04 spine, section 6", "slide two's week map")
    f(S, "tuesday_bookings_per_hour_after", 260, "Rs 260", "Tuesday's target in the W04 spine, section 6", "slide two's week map")
    S = "kalpa_lab"
    f(S, "kalpa_charger_list_price", 199, "Rs 199", "list price of the phone charger, products table (the row)", "every Kalpa mention")
    f(S, "kalpa_claim_share", 0.8, "80 percent", "merchandising's claim in the row: the charger is in 80 percent of baskets", "lab ticket")
    t_share, tc, te = kalpa["twelve_m"]
    f(S, "kalpa_orders", 1000, "1,000", "v4 orders, every one with lines", "notebook 04, lab note")
    f(S, "kalpa_baskets", kalpa["baskets"], str(kalpa["baskets"]), "consumer orders, the basket base", "notebook 04, lab note")
    f(S, "kalpa_business", kalpa["business"], str(kalpa["business"]), "Business orders, one product in bulk", "notebook 04")
    f(S, "kalpa_lines_max", kalpa["lines_max"], str(kalpa["lines_max"]), "most lines in a consumer basket", "notebook 04")
    f(S, "kalpa_charger_all_orders", round(kalpa["charger_all"], 4), f"{kalpa['charger_all'] * 100:.1f} percent", "TRAP: the charger's share if the Business orders stay in the base", "lab note")
    f(S, "kalpa_charger_share", round(kalpa["charger"], 4), f"{kalpa['charger'] * 100:.1f} percent", "PLANT: baskets with the charger", "TRAINER until the lab")
    sc = kalpa["screen"]
    f(S, "kalpa_screen_charger_conf", round(sc["conf_ab"], 4), f"{sc['conf_ab']:.2f}", "PLANT: screen protector to charger", "TRAINER until the lab")
    f(S, "kalpa_screen_charger_lift", round(sc["lift"], 4), f"{sc['lift']:.2f}", "PLANT: their lift", "TRAINER until the lab")
    lc, hc, ll, hl = kalpa["charger_band"]
    f(S, "kalpa_charger_conf_band", f"{lc:.2f} to {hc:.2f}", f"{lc:.2f} to {hc:.2f}", "PLANT: confidence to the charger, every product at 2 percent or more", "TRAINER until the lab")
    f(S, "kalpa_charger_lift_band", f"{ll:.2f} to {hl:.2f}", f"{ll:.2f} to {hl:.2f}", "PLANT: lift with the charger, the same products", "TRAINER until the lab")
    ep = kalpa["pair"]
    f(S, "kalpa_pair_lift", round(ep["lift"], 4), f"{ep['lift']:.1f}", "PLANT: wireless earphones and earphone case", "TRAINER until the lab")
    f(S, "kalpa_pair_support", round(ep["support"], 4), f"{ep['support'] * 100:.0f} percent", "PLANT: their support", "TRAINER until the lab")
    f(S, "kalpa_pair_baskets", ep["nab"], str(ep["nab"]), "PLANT: baskets with both", "TRAINER until the lab")
    f(S, "kalpa_pair_retail_plus", round(kalpa["pair_plus"], 4), f"{kalpa['pair_plus'] * 100:.0f} percent", "PLANT: share of those baskets from Retail-Plus", "TRAINER until the lab")
    th = kalpa["thin"]
    f(S, "kalpa_thin_lift", round(th["lift"], 4), f"{th['lift']:.1f}", "PLANT: car phone mount and car charger", "TRAINER until the lab")
    f(S, "kalpa_thin_support", round(th["support"], 4), f"{th['support'] * 100:.2f} percent", "PLANT: their support", "TRAINER until the lab")
    f(S, "kalpa_thin_baskets", th["nab"], str(th["nab"]), "PLANT: baskets with both", "TRAINER until the lab")
    f(S, "kalpa_floor_pairs", kalpa["floor_pairs"], str(kalpa["floor_pairs"]), "pairs at or above the 5 percent floor", "lab note")
    f(S, "kalpa_one_pct_baskets", round(kalpa["baskets"] / 100, 2), f"about {round(kalpa['baskets'] / 100)}", "1 percent of the consumer baskets", "notebook 04")
    f(S, "kalpa_floor_baskets", round(kalpa["baskets"] * 0.05, 2), f"about {round(kalpa['baskets'] * 0.05)}", "5 percent of the consumer baskets", "notebook 04")
    f(S, "kalpa_twelve_ids", ", ".join(kalpa["twelve"]), "", "the lab's twelve baskets", "lab note")
    f(S, "kalpa_twelve_charger", 9, "9", "of the twelve, baskets with the charger (0.75)", "lab note, notebook 04")
    f(S, "kalpa_twelve_screen_conf", round(tc["conf_ab"], 4), f"{tc['conf_ab']:.2f}", "screen protector to charger on the twelve", "lab note, notebook 04")
    f(S, "kalpa_twelve_screen_lift", round(tc["lift"], 4), f"{tc['lift']:.2f}", "their lift on the twelve", "lab note, notebook 04")
    f(S, "kalpa_twelve_pair_lift", round(te["lift"], 4), f"{te['lift']:.2f}", "earphones and case on the twelve", "lab note, notebook 04")

    head = ("# content/W04/D3/internal/C2_W04_D03_facts_INTERNAL.yaml, written by the generator.\n"
            "# Every number a Wednesday learner sees, with how it was computed, the form it is printed\n"
            "# in and where it is used. Public facts carry their R2 id; toys are labelled invented.\n"
            "#\n"
            "# Corrections to the case file:\n"
            "#   milk_share_after is 50 percent, since 44 percent beside the 1.2 and 6.4 percent slot\n"
            "#     rates blends to 4.1 percent and the ticket's after rate is 3.8.\n"
            "#   twelve_bread_milk_conf is 1.00 and the lift 1.50, since the case file's 0.75 sits 0.01\n"
            "#     from the full-data 0.74 and the spine asks for five points between them.\n"
            "#   recoverable_month replaces the case file's Rs 12.6 lakh over three slots, which held\n"
            "#     only if every slot showed milk; strip_log shows milk on half the slot impressions.\n"
            "#   the twelve rows are real carts of the 40,000 and the Kalpa lines sit on v4's own 1,000\n"
            "#     orders, as the spine and the case file ask.\n\n")
    out = [head]
    section = None
    for sec, fid, value, shown, how, used in F:
        if sec != section:
            out.append(f"\n{sec}:\n")
            section = sec
        v = value if isinstance(value, (int, float)) else f'"{value}"'
        where = "used_by" if fid.startswith("toy_") else "used_in"
        out.append(f"  - id: {fid}\n    value: {v}\n    shown: \"{shown}\"\n"
                   f"    how: \"{how}\"\n    {where}: \"{used}\"\n")
    FACTS.write_text("".join(out), encoding="utf-8")
    ids = [x[1] for x in F]
    check("every fact id is unique", len(ids) == len(set(ids)))
    return F


def main():
    rng = random.Random(SEED)
    DATA.mkdir(parents=True, exist_ok=True)
    print("The case: carts, items and the twelve rows")
    cart_df, item_df, twelve_df = write_case(rng)
    case = verify_case(cart_df, item_df, twelve_df)
    print("\nThe strip log")
    log = write_strip_log(random.Random(SEED + 1))
    strip = verify_strip(log)
    print("\nThe Kalpa transfer on v4's orders")
    products, orders, items = write_kalpa(random.Random(SEED + 2))
    kalpa = verify_kalpa(products, orders, items)
    print("\nThe concept chapters' invented examples")
    toys = verify_toys(*write_toys())
    write_facts(case, strip, kalpa, toys)
    print(f"\nWrote {len(cart_df):,} carts, {len(item_df):,} cart lines, {len(log):,} strip_log rows, "
          f"{len(items):,} Kalpa lines and the facts file.")


if __name__ == "__main__":
    main()

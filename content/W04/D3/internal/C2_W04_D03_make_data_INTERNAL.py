"""Generate the Wednesday case data: Swiggy Instamart Pune carts and strip_log, plus the small
Kalpa Retail transfer tables for the TA lab. One seeded, deterministic generator; pandas and the
standard library only; the smallest code that fully works.

Writes seven CSVs to content/W04/D3/data/:
    C2_W04_D03_carts_STUDENT.csv            40,000 Pune carts, 1-28 September 2026
    C2_W04_D03_cart_items_STUDENT.csv       items in each cart with price and margin
    C2_W04_D03_strip_log_STUDENT.csv        daily slot impressions, clicks, adds, 17 Aug-27 Sep
    C2_W04_D03_twelve_rows_STUDENT.csv      the twelve printed carts for the L1 hand count
    C2_W04_D03_kalpa_products_STUDENT.csv   Kalpa Retail product catalogue including the Rs 199 charger
    C2_W04_D03_kalpa_order_items_STUDENT.csv  Kalpa order lines for the lab, with the plants hidden
    C2_W04_D03_kalpa_orders_STUDENT.csv     Kalpa order headers (one row per order), with amount

Prints a PASS line for every asserted target and raises AssertionError on any miss. Also writes the
day's facts file at ../internal/C2_W04_D03_facts_INTERNAL.yaml, listing every number a learner will
see with its id, how it was computed in one line and where it is used. No number appears in a
STUDENT file that is not in that facts file.

Corrections recorded in the facts file and in the drafting report:
    the 44 percent milk-impression share after the change cannot sit beside the 1.2 and 6.4
    percent slot click-throughs and the 3.8 percent blend, since 0.44*1.2 + 0.56*6.4 is 4.11 and
    not 3.8; the share that reproduces 3.8 from the two is 50 percent, and the strip_log is
    generated to that share.

    the twelve-row bread to milk confidence that the case file prints as 0.75 sits 0.01 from the
    full-data 0.74, which the spine's distance rule forbids; the twelve rows are reshaped so
    bread is in 4 carts and all 4 of them hold milk, which gives confidence 1.00 and lift 1.50
    cleanly separated from the full-data values.
"""
import csv
import random
import textwrap
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
DATA.mkdir(parents=True, exist_ok=True)
FACTS = HERE / "C2_W04_D03_facts_INTERNAL.yaml"

SEED = 20261028
N_CARTS = 40_000
PUNE_ZONES = ["Kothrud", "Baner", "Viman Nagar", "Kalyani Nagar",
              "Aundh", "Hadapsar", "Hinjewadi", "Camp"]
TIME_BANDS = ["morning", "afternoon", "evening", "night"]
START_DATE = date(2026, 9, 1)

# Base prices in Rs and the 18 percent margin we take on each item sold.
PRICES = {
    "toned milk": 32, "bread": 45, "eggs": 72, "curd": 55, "bananas": 48,
    "chips": 20, "cold drink": 40, "ice cream": 150, "chocolate sauce": 180,
    "paneer": 95, "coriander": 10, "onions": 35, "potatoes": 30, "tomatoes": 40,
}
MARGINS = {name: round(price * 0.18, 2) for name, price in PRICES.items()}

# Target probabilities and conditional rates calibrated to hit the case file's confidence targets.
# Independent sampling in each cart, conditional on milk status for the milk-paired items.
P_MILK = 0.71
# Pair (P(item | milk), P(item | not milk)) chosen so marginal matches and confidence to milk
# matches the case file's targets. Working for bread, which anchors the row's lift arithmetic:
#   P(bread, milk) = conf(bread -> milk) * P(bread) = 0.74 * 0.34 = 0.2516
#   P(bread | milk) = 0.2516 / 0.71 = 0.3544
#   P(bread | not milk) = (0.34 - 0.2516) / 0.29 = 0.3048
MILK_PAIRED = {
    "bread":     (0.3544, 0.3048),  # marginal 0.34, conf->milk 0.74, lift 1.04
    "eggs":      (0.2982, 0.2700),  # marginal 0.29, conf->milk 0.73, lift 1.03
    "curd":      (0.2637, 0.2510),  # marginal 0.26, conf->milk 0.72, lift 1.014
    "bananas":   (0.2332, 0.2221),  # marginal 0.23, conf->milk 0.72, lift 1.014
    "ice cream": (0.0406, 0.0387),  # marginal 0.04,  conf->milk 0.72, lift 1.014
}
# Independent sampling (no coupling with milk) for items the spine does not pin to milk.
INDEP = {
    "paneer":    0.08,
    "coriander": 0.15,
    "onions":    0.22,
    "potatoes":  0.18,
    "tomatoes":  0.20,
}

# The chips and cold drink joint: four outcomes, independent of milk, so the chips->milk and
# cold->milk confidences land at 0.71 and sit cleanly inside the spine's [0.68, 0.78] band.
#   P(chips=1, cold=1) = 0.050     support 5.0 percent
#   P(chips=1, cold=0) = 0.070     chips marginal 0.120
#   P(chips=0, cold=1) = 0.073     cold marginal 0.123
#   P(chips=0, cold=0) = 0.807
CC_CUT = [0.050, 0.120, 0.193]  # cumulative

# Ice cream and chocolate sauce joint; chocolate sauce only appears paired with ice cream or alone,
# and the pair sits at 100 of 40,000, so the full-data lift at 0.0025 / (0.04 * 0.0136) is 4.60.
# Ice cream itself follows MILK_PAIRED above, so this draw places chocolate sauce conditional on
# whether this cart already had ice cream from the MILK_PAIRED draw.
P_CHOC_GIVEN_ICE = 0.0025 / 0.04        # 0.0625
P_CHOC_GIVEN_NOT_ICE = (0.0136 - 0.0025) / 0.96  # 0.01156


def sample_cart(rng):
    """One cart's items as a set, sampled with the calibrated distributions above."""
    items = set()
    has_milk = rng.random() < P_MILK
    if has_milk:
        items.add("toned milk")
    for name, (p_milk, p_notmilk) in MILK_PAIRED.items():
        if rng.random() < (p_milk if has_milk else p_notmilk):
            items.add(name)
    r = rng.random()
    if r < CC_CUT[0]:
        items.add("chips"); items.add("cold drink")
    elif r < CC_CUT[1]:
        items.add("chips")
    elif r < CC_CUT[2]:
        items.add("cold drink")
    p_choc = P_CHOC_GIVEN_ICE if "ice cream" in items else P_CHOC_GIVEN_NOT_ICE
    if rng.random() < p_choc:
        items.add("chocolate sauce")
    for name, p in INDEP.items():
        if rng.random() < p:
            items.add(name)
    if not items:
        items.add("coriander")  # the one hedge; a cart with no items would break the join
    return items


def write_carts():
    """40,000 Pune carts and their items, written as two CSVs."""
    rng = random.Random(SEED)
    carts_rows = []
    items_rows = []
    # The top tenth of customers place 38 percent of the carts. 1,000 top customers against
    # 9,000 ordinary customers places 15,200 of the 40,000 carts in the heavy tenth.
    for i in range(N_CARTS):
        cart_id = f"C{i:06d}"
        day_offset = rng.randint(0, 27)
        placed = START_DATE + timedelta(days=day_offset)
        zone = rng.choice(PUNE_ZONES)
        band = rng.choices(TIME_BANDS, weights=[2, 2, 3, 1])[0]
        if rng.random() < 0.38:
            customer_id = f"K{rng.randint(1, 1000):05d}"
        else:
            customer_id = f"K{rng.randint(1001, 10000):05d}"
        items = sample_cart(rng)
        cart_value = sum(PRICES[name] for name in items)
        carts_rows.append({
            "cart_id": cart_id, "customer_id": customer_id,
            "placed_date": placed.isoformat(), "zone": zone,
            "time_band": band, "cart_value_rs": cart_value,
        })
        for name in sorted(items):
            items_rows.append({
                "cart_id": cart_id, "item": name, "quantity": 1,
                "price_rs": PRICES[name], "margin_rs": MARGINS[name],
            })
    carts = pd.DataFrame(carts_rows)
    cart_items = pd.DataFrame(items_rows)
    carts.to_csv(DATA / "C2_W04_D03_carts_STUDENT.csv", index=False)
    cart_items.to_csv(DATA / "C2_W04_D03_cart_items_STUDENT.csv", index=False)
    return carts, cart_items


def write_strip_log():
    """Daily strip impressions, clicks and adds for 17 August to 27 September 2026.

    The strip has three slots; the before-change window runs 17 August to 6 September and the
    after-change window 7 September to 27 September. Before the change the slots were curated so
    no slot is called a milk slot in the log; after the change milk fills half the slot
    impressions, which is the share that reproduces the headline 3.8 percent blended click-through
    from the 1.2 percent on milk slots and the 6.4 percent on every other slot.
    """
    rng = random.Random(SEED + 1)
    rows = []
    total_views_per_day = 60_000  # Pune cart-page views
    daily_slot_impressions = total_views_per_day // 3  # 20,000 per slot per day
    before_start = date(2026, 8, 17)
    change_day = date(2026, 9, 7)
    end = date(2026, 9, 27)
    anchor_items = ["bread", "eggs", "curd", "bananas"]
    other_items = ["cold drink", "chips", "ice cream", "paneer", "coriander", "onions"]
    d = before_start
    while d <= end:
        after = d >= change_day
        for slot in [1, 2, 3]:
            if after:
                # Milk gets half the slot impressions, click-through 1.2 percent.
                milk_imp = daily_slot_impressions // 2
                other_imp = daily_slot_impressions - milk_imp
                milk_clicks = round(milk_imp * 0.012)
                other_clicks = round(other_imp * 0.064)
                milk_adds = round(milk_clicks * 0.5)
                other_adds = round(other_clicks * 0.5)
                rows.append({
                    "date": d.isoformat(), "slot": slot,
                    "anchor_item": rng.choice(anchor_items), "suggested_item": "toned milk",
                    "impressions": milk_imp, "clicks": milk_clicks, "adds": milk_adds,
                })
                rows.append({
                    "date": d.isoformat(), "slot": slot,
                    "anchor_item": rng.choice(anchor_items),
                    "suggested_item": rng.choice(other_items),
                    "impressions": other_imp, "clicks": other_clicks, "adds": other_adds,
                })
            else:
                # Curated: no milk slot, click-through 6.1 percent averaged across the strip.
                imp = daily_slot_impressions
                clicks = round(imp * 0.061)
                adds = round(clicks * 0.5)
                rows.append({
                    "date": d.isoformat(), "slot": slot,
                    "anchor_item": rng.choice(anchor_items),
                    "suggested_item": rng.choice(other_items),
                    "impressions": imp, "clicks": clicks, "adds": adds,
                })
        d += timedelta(days=1)
    df = pd.DataFrame(rows)
    df.to_csv(DATA / "C2_W04_D03_strip_log_STUDENT.csv", index=False)
    return df


# ---- the twelve printed rows ---------------------------------------------------------------------
# A fixed hand-crafted table. Milk sits in 8 of 12 carts; bread in 4, all 4 with milk, so bread to
# milk confidence lands at 1.00 and lift at 1.50 on the twelve rows, each at least 0.05 from the
# full-data 0.74 and 1.04. Chips and cold drink sit in 3 carts each with 2 shared, so support is
# 2 over 12 and lift is 2.67, each separated from the full-data 0.05 / 0.42 / 3.40. Ice cream and
# chocolate sauce ride in one cart together, support 1 over 12 and lift 12. Every value also sits
# at least 0.05 from the Kalpa plants 0.82 confidence, 0.97 lift, 3.1 lift and 4.0 lift.
TWELVE_ROWS = [
    ("TR01", ["toned milk", "bread", "eggs", "bananas", "coriander", "onions", "potatoes"]),
    ("TR02", ["toned milk", "bread", "eggs", "curd", "bananas"]),
    ("TR03", ["toned milk", "bread", "curd", "paneer", "onions"]),
    ("TR04", ["toned milk", "bread", "eggs", "tomatoes"]),
    ("TR05", ["toned milk", "eggs", "chips", "cold drink", "onions"]),
    ("TR06", ["toned milk", "chips", "cold drink", "coriander"]),
    ("TR07", ["toned milk", "bananas", "onions", "potatoes"]),
    ("TR08", ["toned milk", "paneer", "coriander", "tomatoes"]),
    ("TR09", ["chips", "coriander", "onions", "potatoes"]),
    ("TR10", ["cold drink", "curd", "bananas", "tomatoes"]),
    ("TR11", ["eggs", "ice cream", "chocolate sauce"]),
    ("TR12", ["curd", "onions"]),
]


def write_twelve_rows():
    rows = []
    all_items = sorted({item for _, items in TWELVE_ROWS for item in items})
    for cart_id, items in TWELVE_ROWS:
        row = {"cart_id": cart_id}
        for name in all_items:
            row[name] = 1 if name in items else 0
        rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(DATA / "C2_W04_D03_twelve_rows_STUDENT.csv", index=False)
    return df


# ---- Kalpa Retail transfer -----------------------------------------------------------------------
# A smaller Kalpa dataset for the lab: 600 Kalpa Retail orders of which 500 are consumer baskets
# and 100 are Business bulk-orders. The plants are the ones the row names: the Rs 199 phone charger
# in a dominant share of consumer baskets; a partner item whose confidence to the charger prints
# 0.82 and whose lift prints 0.97; a stronger pair above a 5 percent support floor at lift 3.1;
# and one thin pair at lift 4.0 with support between 0.2 and 0.4 percent.
KALPA_PRODUCTS = [
    # (product_id, name, category, list_price, unit_cost)
    ("P001", "phone charger 20W",     "Electronics", 199,  120),
    ("P002", "screen protector",      "Electronics", 149,   85),
    ("P003", "earphone jack adapter", "Electronics",  89,   50),
    ("P004", "wireless earphones",    "Electronics", 1499, 950),
    ("P005", "earphone case",         "Electronics", 299,  170),
    ("P006", "USB-C cable",           "Electronics", 249,  140),
    ("P007", "car charger",           "Electronics", 349,  200),
    ("P008", "power bank 10000mAh",   "Electronics", 1199, 780),
    ("P009", "phone grip",            "Accessories",  99,   55),
    ("P010", "cable organiser",       "Accessories", 149,   80),
    ("P011", "notebook A5",           "Stationery",   79,   40),
    ("P012", "pen set",               "Stationery",   99,   50),
    ("P013", "LED desk lamp",         "Lighting",     699,  420),
    ("P014", "extension cord",        "Electronics",  499,  290),
    ("P015", "wall adapter",          "Electronics",  299,  170),
]

# Plant arithmetic, with marginals and overlaps carefully set to hit the case file's shape.
#   N_CONSUMER = 500 consumer baskets.
#   charger (P001):      425 baskets (85 percent).
#   screen (P002):        60 baskets, 49 of them with charger, confidence 49/60 = 0.817 ~ 0.82,
#                         lift 0.098 / (0.12 * 0.85) = 0.961 ~ 0.97.
#   earphones (P004):     75 baskets.
#   case (P005):          65 baskets, together with earphones in 30, support 0.060, lift
#                         0.060 / (0.15 * 0.13) = 3.08 ~ 3.1.
#   usb (P006):           10 baskets.
#   car charger (P007):   25 baskets, together with usb in 2, support 0.004, lift
#                         0.004 / (0.02 * 0.05) = 4.00.
N_CONSUMER = 500
N_BUSINESS = 100

PLANTS = {
    "charger_count": 425,
    "screen_count": 60,
    "screen_with_charger": 49,
    "earphones_count": 75,
    "case_count": 65,
    "earphones_case_together": 30,
    "earphones_retail_plus_share": 0.72,  # above the row's 70 percent floor
    "usb_count": 10,
    "car_charger_count": 25,
    "usb_car_together": 2,
}


def write_kalpa():
    """500 consumer baskets and 100 Business bulk-orders for Kalpa Retail.

    A consumer basket runs one to about eight product lines; a Business order is one product line
    at a large quantity. Every order's lines sum to its `amount` by construction, which is what the
    lab notebook will check. The plants above are placed in the first N_CONSUMER baskets.
    """
    rng = random.Random(SEED + 2)
    product_df = pd.DataFrame(KALPA_PRODUCTS,
                              columns=["product_id", "name", "category",
                                       "list_price", "unit_cost"])
    product_df.to_csv(DATA / "C2_W04_D03_kalpa_products_STUDENT.csv", index=False)
    name_to_id = dict(zip(product_df.name, product_df.product_id))
    price_of = dict(zip(product_df.name, product_df.list_price))

    # Decide, for each consumer basket, which of the planted items it holds.
    baskets = [[] for _ in range(N_CONSUMER)]
    tiers = []
    # First: assign the charger to 425 baskets, chosen as the first 425 for determinism.
    for i in range(PLANTS["charger_count"]):
        baskets[i].append("phone charger 20W")
    # Screen protector: 60 baskets, 49 of them in [0..424] (charger-holders).
    screen_with = list(range(PLANTS["screen_with_charger"]))
    screen_without = list(range(PLANTS["charger_count"],
                                PLANTS["charger_count"]
                                + (PLANTS["screen_count"] - PLANTS["screen_with_charger"])))
    for i in screen_with + screen_without:
        baskets[i].append("screen protector")
    # Earphones and case: a correlated pair, lift 3.1. Place 30 baskets with both, 45 with
    # earphones only, 35 with case only.
    rng_order = list(range(N_CONSUMER))
    rng.shuffle(rng_order)
    both = rng_order[:30]
    e_only = rng_order[30:30 + 45]
    c_only = rng_order[30 + 45:30 + 45 + 35]
    for i in both:
        baskets[i].append("wireless earphones"); baskets[i].append("earphone case")
    for i in e_only:
        baskets[i].append("wireless earphones")
    for i in c_only:
        baskets[i].append("earphone case")
    # Retail-Plus marker: 72 percent of the 30 both-baskets are Retail-Plus, so 22 of them get the
    # tier marker. The rest of the baskets each get a tier independently.
    tier_plus = set(both[:int(round(0.72 * 30))])
    # USB-C cable and car charger: 2 baskets with both, 8 with usb only, 23 with car charger only.
    rng.shuffle(rng_order)
    uc_both = rng_order[:2]
    u_only = rng_order[2:10]
    c_car_only = rng_order[10:33]
    for i in uc_both:
        baskets[i].append("USB-C cable"); baskets[i].append("car charger")
    for i in u_only:
        baskets[i].append("USB-C cable")
    for i in c_car_only:
        baskets[i].append("car charger")
    # The thinner filler: each basket gets 0 to 4 other products drawn from the catalogue.
    filler_pool = [p[1] for p in KALPA_PRODUCTS
                   if p[1] not in {"phone charger 20W", "screen protector",
                                   "wireless earphones", "earphone case",
                                   "USB-C cable", "car charger"}]
    for i, basket in enumerate(baskets):
        n_filler = rng.choice([0, 0, 1, 1, 2, 3, 4])
        for _ in range(n_filler):
            item = rng.choice(filler_pool)
            if item not in basket:
                basket.append(item)
        # Guarantee each basket has at least one line.
        if not basket:
            basket.append(rng.choice(filler_pool))

    # Write consumer orders and their lines.
    orders_rows = []
    items_rows = []
    for i, basket in enumerate(baskets):
        order_id = f"KO{i+1:05d}"
        customer_tier = "Retail-Plus" if i in tier_plus else rng.choice(
            ["Retail-Core", "Retail-Plus", "Retail-Core", "Retail-Core"])
        customer_id = f"RC{i+1:05d}" if customer_tier == "Retail-Core" else f"RP{i+1:05d}"
        amount = 0
        for product_name in basket:
            qty = 1
            unit_price = price_of[product_name]
            items_rows.append({
                "order_id": order_id, "product_id": name_to_id[product_name],
                "product_name": product_name, "quantity": qty, "unit_price": unit_price,
                "line_total": qty * unit_price,
            })
            amount += qty * unit_price
        orders_rows.append({
            "order_id": order_id, "customer_id": customer_id,
            "customer_tier": customer_tier, "channel": "consumer",
            "placed_date": (date(2026, 7, 1) + timedelta(days=rng.randint(0, 90))).isoformat(),
            "amount": amount, "line_count": len(basket),
        })

    # Business orders: one product per order at a large quantity.
    for b in range(N_BUSINESS):
        order_id = f"KO{N_CONSUMER + b + 1:05d}"
        product_name = rng.choice([p[1] for p in KALPA_PRODUCTS])
        qty = rng.choice([50, 100, 200, 500])
        unit_price = price_of[product_name]
        items_rows.append({
            "order_id": order_id, "product_id": name_to_id[product_name],
            "product_name": product_name, "quantity": qty, "unit_price": unit_price,
            "line_total": qty * unit_price,
        })
        orders_rows.append({
            "order_id": order_id, "customer_id": f"KB{b+1:05d}",
            "customer_tier": "Business", "channel": "business",
            "placed_date": (date(2026, 7, 1) + timedelta(days=rng.randint(0, 90))).isoformat(),
            "amount": qty * unit_price, "line_count": 1,
        })

    orders = pd.DataFrame(orders_rows)
    items = pd.DataFrame(items_rows)
    orders.to_csv(DATA / "C2_W04_D03_kalpa_orders_STUDENT.csv", index=False)
    items.to_csv(DATA / "C2_W04_D03_kalpa_order_items_STUDENT.csv", index=False)
    return orders, items


# ---- assertions ----------------------------------------------------------------------------------
def assert_within(label, actual, target, tol):
    direction = "<=" if abs(actual - target) <= tol else "GT"
    if abs(actual - target) > tol:
        raise AssertionError(f"FAIL {label}: {actual:.4f} is {abs(actual - target):.4f} "
                             f"from target {target:.4f} (tol {tol})")
    print(f"PASS {label}: {actual:.4f} within {tol} of {target}")


def verify_case(carts, cart_items):
    """Check marginals, pair supports, confidences and lifts against the case file's targets."""
    n = len(carts)
    item_sets = cart_items.groupby("cart_id")["item"].apply(set)
    def rate(name):
        return int(sum(1 for s in item_sets if name in s)) / n
    def pair(a, b):
        return int(sum(1 for s in item_sets if a in s and b in s)) / n
    p_milk = rate("toned milk")
    assert_within("milk marginal", p_milk, 0.71, 0.012)
    p_bread = rate("bread");          assert_within("bread marginal",      p_bread, 0.34, 0.010)
    p_eggs = rate("eggs");            assert_within("eggs marginal",       p_eggs,  0.29, 0.010)
    p_curd = rate("curd");            assert_within("curd marginal",       p_curd,  0.26, 0.010)
    p_ban = rate("bananas");          assert_within("bananas marginal",    p_ban,   0.23, 0.010)
    p_chips = rate("chips");          assert_within("chips marginal",      p_chips, 0.12, 0.010)
    p_cold = rate("cold drink");      assert_within("cold drink marginal", p_cold,  0.123, 0.010)
    p_ice = rate("ice cream");        assert_within("ice cream marginal",  p_ice,   0.04, 0.006)
    p_choc = rate("chocolate sauce"); assert_within("choc sauce marginal", p_choc,  0.0136, 0.004)
    # Pair-level targets.
    p_bm = pair("bread", "toned milk")
    conf_bm = p_bm / p_bread
    lift_bm = p_bm / (p_bread * p_milk)
    assert_within("bread -> milk conf", conf_bm, 0.74, 0.02)
    assert_within("bread, milk lift",    lift_bm, 1.04, 0.03)
    p_em = pair("eggs", "toned milk"); conf_em = p_em / p_eggs
    lift_em = p_em / (p_eggs * p_milk)
    assert_within("eggs -> milk conf",   conf_em, 0.73, 0.02)
    assert_within("eggs, milk lift",     lift_em, 1.03, 0.03)
    p_cc = pair("chips", "cold drink")
    conf_cc = p_cc / p_chips
    conf_ccc = p_cc / p_cold
    lift_cc = p_cc / (p_chips * p_cold)
    assert_within("chips, cold support", p_cc,     0.050, 0.004)
    assert_within("chips -> cold conf",  conf_cc,  0.42,  0.03)
    assert_within("cold -> chips conf",  conf_ccc, 0.41,  0.03)
    assert_within("chips, cold lift",    lift_cc,  3.4,   0.25)
    p_ic = pair("ice cream", "chocolate sauce")
    lift_ic = p_ic / (p_ice * p_choc)
    assert_within("ice, choc support",   p_ic,    0.0025, 0.0015)
    assert_within("ice, choc lift",      lift_ic, 4.6,    1.5)
    # Confidence to milk for items with support >= 2 percent sits in [0.68, 0.78], lift in [0.96, 1.08].
    for name in ["bread", "eggs", "curd", "bananas", "chips", "cold drink", "ice cream"]:
        p_x = rate(name)
        p_xm = pair(name, "toned milk")
        conf_xm = p_xm / p_x
        lift_xm = p_xm / (p_x * p_milk)
        if 0.68 <= conf_xm <= 0.78:
            print(f"PASS conf({name} -> milk) in [0.68, 0.78]: {conf_xm:.3f}")
        else:
            raise AssertionError(f"FAIL conf({name} -> milk)={conf_xm:.3f} outside [0.68, 0.78]")
        if 0.96 <= lift_xm <= 1.08:
            print(f"PASS lift({name}, milk) in [0.96, 1.08]: {lift_xm:.3f}")
        else:
            raise AssertionError(f"FAIL lift({name}, milk)={lift_xm:.3f} outside [0.96, 1.08]")
    # Heavy-tenth check: top ten percent of customers place about 38 percent of carts.
    cust_counts = carts["customer_id"].value_counts()
    top_n = max(1, int(round(0.10 * len(cust_counts))))
    heavy_share = cust_counts.iloc[:top_n].sum() / len(carts)
    assert_within("top 10 percent of customers place share", heavy_share, 0.38, 0.03)
    return {
        "milk_marginal": p_milk, "bread_marginal": p_bread, "eggs_marginal": p_eggs,
        "curd_marginal": p_curd, "bananas_marginal": p_ban, "chips_marginal": p_chips,
        "cold_marginal": p_cold, "icecream_marginal": p_ice, "chocsauce_marginal": p_choc,
        "bread_milk_support": p_bm, "bread_milk_conf": conf_bm, "bread_milk_lift": lift_bm,
        "eggs_milk_conf": conf_em, "eggs_milk_lift": lift_em,
        "chips_cold_support": p_cc, "chips_cold_conf_c": conf_cc, "chips_cold_conf_d": conf_ccc,
        "chips_cold_lift": lift_cc,
        "ice_choc_support": p_ic, "ice_choc_lift": lift_ic,
        "heavy_tenth_share": heavy_share,
    }


def verify_strip(strip):
    """Check the before and after click-throughs reproduce the headline rates."""
    before = strip[strip.date < "2026-09-07"]
    after = strip[strip.date >= "2026-09-07"]
    before_ctr = before.clicks.sum() / before.impressions.sum()
    after_ctr = after.clicks.sum() / after.impressions.sum()
    assert_within("before-change blended CTR", before_ctr, 0.061, 0.001)
    assert_within("after-change blended CTR",  after_ctr,  0.038, 0.001)
    milk_after = after[after.suggested_item == "toned milk"]
    other_after = after[after.suggested_item != "toned milk"]
    milk_ctr = milk_after.clicks.sum() / milk_after.impressions.sum()
    other_ctr = other_after.clicks.sum() / other_after.impressions.sum()
    assert_within("milk-slot CTR after",  milk_ctr,  0.012, 0.001)
    assert_within("other-slot CTR after", other_ctr, 0.064, 0.001)
    milk_share = milk_after.impressions.sum() / after.impressions.sum()
    # The milk impression share after the change sits at the 50 percent that reproduces the 3.8
    # blend from the 1.2 and 6.4 slot rates, which is the correction recorded in the facts file.
    assert_within("milk-slot impression share after", milk_share, 0.50, 0.01)
    return {"before_ctr": before_ctr, "after_ctr": after_ctr,
            "milk_slot_ctr": milk_ctr, "other_slot_ctr": other_ctr,
            "milk_slot_share_after": milk_share}


def verify_twelve_rows(df):
    """The twelve rows hand count: assert the ratios the deck and the cheat sheet will print."""
    def cnt(col): return int(df[col].sum())
    def tog(a, b): return int(((df[a] == 1) & (df[b] == 1)).sum())
    milk = cnt("toned milk"); bread = cnt("bread"); eggs = cnt("eggs")
    chips = cnt("chips"); cold = cnt("cold drink")
    ice = cnt("ice cream"); choc = cnt("chocolate sauce")
    bm = tog("bread", "toned milk"); cc = tog("chips", "cold drink")
    ic = tog("ice cream", "chocolate sauce")
    # Hand counts.
    assert milk == 8, f"milk 8 expected, got {milk}"; print(f"PASS twelve rows milk count: 8")
    assert bread == 4, f"bread 4 expected, got {bread}"; print(f"PASS twelve rows bread count: 4")
    assert bm == 4, f"bread with milk 4 expected, got {bm}"
    print(f"PASS twelve rows bread with milk count: 4 (bread -> milk conf 1.00, lift 1.50)")
    assert chips == 3 and cold == 3 and cc == 2
    print(f"PASS twelve rows chips 3, cold 3, together 2 (support 0.167, conf 0.667, lift 2.667)")
    assert ice == 1 and choc == 1 and ic == 1
    print(f"PASS twelve rows ice-choc 1 together (support 0.083, lift 12)")
    return {
        "milk_n": milk, "bread_n": bread, "bread_milk_n": bm,
        "chips_n": chips, "cold_n": cold, "chips_cold_n": cc,
        "ice_n": ice, "choc_n": choc, "ice_choc_n": ic,
        "milk_marginal_12": milk / 12, "bread_marginal_12": bread / 12,
        "bread_milk_conf_12": bm / bread,
        "bread_milk_lift_12": (bm / 12) / ((bread / 12) * (milk / 12)),
        "chips_cold_support_12": cc / 12,
        "chips_cold_conf_12": cc / chips,
        "chips_cold_lift_12": (cc / 12) / ((chips / 12) * (cold / 12)),
        "ice_choc_support_12": ic / 12,
        "ice_choc_lift_12": (ic / 12) / ((ice / 12) * (choc / 12)),
    }


def verify_kalpa(orders, items):
    """The Kalpa transfer plants: charger share, screen partner confidence and lift, strongest and
    thinnest pairs, and the Business order shape."""
    consumer = orders[orders.channel == "consumer"]
    basket_items = items[items.order_id.isin(consumer.order_id)].groupby("order_id")["product_name"].apply(set)
    n = len(basket_items)
    def rate(name): return int(sum(1 for s in basket_items if name in s)) / n
    def pair_rate(a, b):
        return int(sum(1 for s in basket_items if a in s and b in s)) / n
    p_charger = rate("phone charger 20W")
    p_screen = rate("screen protector")
    pair_sc = pair_rate("screen protector", "phone charger 20W")
    conf_sc = pair_sc / p_screen
    lift_sc = pair_sc / (p_screen * p_charger)
    assert 0.84 <= p_charger <= 0.86, f"charger share {p_charger:.3f} outside [0.84, 0.86]"
    print(f"PASS Kalpa charger share: {p_charger:.3f}")
    assert_within("Kalpa screen -> charger conf", conf_sc, 0.82, 0.02)
    assert_within("Kalpa screen, charger lift",    lift_sc, 0.97, 0.03)
    p_ear = rate("wireless earphones"); p_case = rate("earphone case")
    pair_ec = pair_rate("wireless earphones", "earphone case")
    lift_ec = pair_ec / (p_ear * p_case)
    assert pair_ec >= 0.05, f"strongest pair support {pair_ec:.3f} below 0.05"
    assert_within("Kalpa strongest pair lift", lift_ec, 3.1, 0.3)
    p_usb = rate("USB-C cable"); p_cc = rate("car charger")
    pair_uc = pair_rate("USB-C cable", "car charger")
    lift_uc = pair_uc / (p_usb * p_cc)
    assert 0.002 <= pair_uc <= 0.004, f"thin pair support {pair_uc:.4f} outside [0.002, 0.004]"
    assert_within("Kalpa thin pair lift", lift_uc, 4.0, 0.4)
    # Every order's lines must sum to orders.amount.
    line_sums = items.groupby("order_id")["line_total"].sum()
    merged = orders.set_index("order_id")["amount"]
    joined = line_sums.to_frame("sum").join(merged.to_frame("amount"))
    if not (joined["sum"] == joined["amount"]).all():
        raise AssertionError("order lines do not sum to order amount for every order")
    print(f"PASS Kalpa order lines sum to amount for every one of {len(orders)} orders")
    return {
        "charger_share": p_charger, "screen_conf_to_charger": conf_sc,
        "screen_charger_lift": lift_sc, "strongest_pair_lift": lift_ec,
        "strongest_pair_support": pair_ec, "thin_pair_lift": lift_uc,
        "thin_pair_support": pair_uc, "consumer_count": n,
        "business_count": int((orders.channel == "business").sum()),
    }


# ---- facts file ----------------------------------------------------------------------------------
def write_facts(case, strip, twelve, kalpa):
    """Write every learner-visible number with its id, how-computed line, and where it is used."""
    text = textwrap.dedent(f"""
    # content/W04/D3/internal/C2_W04_D03_facts_INTERNAL.yaml
    # Every number a Wednesday pack learner will see, with its id, how it was computed and where
    # it is used. The generator writes this file alongside the CSVs; a figure script, a deck or a
    # notebook that prints a number not listed here fails the pack's own self-check.
    #
    # Corrections. Two figures the case file lists cannot stand together, so they were adjusted:
    #   milk_slot_share_after was set to 0.50 because 44 percent beside 1.2 and 6.4 percent slot
    #     click-throughs produces a 4.11 percent blend and not the 3.8 percent the headline fall
    #     calls for. 0.50 is the share that reproduces 3.8 from the two slot rates.
    #   twelve_bread_milk_conf was moved from 0.75 to 1.00 (every bread cart also holds milk) so
    #     the hand count sits at least 0.05 from the full-data 0.74, which the spine's distance
    #     rule requires.

    day:
      week: W04
      day: D3
      date: 2026-10-28
      case: Swiggy Instamart, Pune, the frequently bought together strip
      kalpa_transfer: Rs 199 phone charger across Kalpa Retail consumer baskets

    # ----------------------------------------------------------------- the case ticket
    ticket:
      - id: before_strip_ctr
        value: 0.061
        how: "clicks over impressions for the three slots, 17 August to 6 September 2026"
        used_in: deck half1 cover, notebook 01 cell 1, cheat sheet panel 1
      - id: after_strip_ctr
        value: 0.038
        how: "clicks over impressions for the three slots, 7 to 27 September 2026"
        used_in: deck half1 cover, notebook 01 cell 1, cheat sheet panel 1
      - id: milk_slot_ctr_after
        value: {strip['milk_slot_ctr']:.4f}
        how: "clicks over impressions on the slots suggesting toned milk, 7 to 27 September 2026"
        used_in: deck half1 chapter 2, notebook 02 your-turn
      - id: other_slot_ctr_after
        value: {strip['other_slot_ctr']:.4f}
        how: "clicks over impressions on the slots suggesting any item other than toned milk"
        used_in: deck half1 chapter 2, notebook 02 your-turn
      - id: milk_slot_share_after
        value: {strip['milk_slot_share_after']:.4f}
        how: "milk-slot impressions over total slot impressions, 7 to 27 September 2026"
        used_in: deck half1 chapter 3, notebook 03
      - id: total_carts
        value: 40000
        how: "fixed by the generator"
        used_in: ticket, notebook 02 cell 1
      - id: cart_window_days
        value: 28
        how: "1 to 28 September 2026 inclusive"
        used_in: ticket
      - id: pune_zones
        value: 8
        how: "fixed city map used by the Pune Instamart surface"
        used_in: ticket

    # ----------------------------------------------------------------- the full-data pairs table
    full_data:
      - id: milk_marginal
        value: {case['milk_marginal']:.4f}
        how: "share of the 40,000 carts that hold toned milk"
        used_in: deck half1 chapter 2, notebook 02, cheat sheet panel 1
      - id: bread_marginal
        value: {case['bread_marginal']:.4f}
        how: "share of the 40,000 carts that hold bread"
        used_in: deck half1 chapter 2, notebook 02
      - id: eggs_marginal
        value: {case['eggs_marginal']:.4f}
        how: "share of the 40,000 carts that hold eggs"
        used_in: deck half1 chapter 2
      - id: curd_marginal
        value: {case['curd_marginal']:.4f}
        how: "share of the 40,000 carts that hold curd"
        used_in: deck half1 chapter 2
      - id: bananas_marginal
        value: {case['bananas_marginal']:.4f}
        how: "share of the 40,000 carts that hold bananas"
        used_in: deck half1 chapter 2
      - id: chips_marginal
        value: {case['chips_marginal']:.4f}
        how: "share of the 40,000 carts that hold chips"
        used_in: deck half1 chapter 2, cheat sheet panel 1
      - id: cold_marginal
        value: {case['cold_marginal']:.4f}
        how: "share of the 40,000 carts that hold a cold drink"
        used_in: deck half1 chapter 2, cheat sheet panel 1
      - id: icecream_marginal
        value: {case['icecream_marginal']:.4f}
        how: "share of the 40,000 carts that hold ice cream"
        used_in: deck half1 chapter 2
      - id: chocsauce_marginal
        value: {case['chocsauce_marginal']:.4f}
        how: "share of the 40,000 carts that hold chocolate sauce"
        used_in: deck half1 chapter 2
      - id: bread_milk_support
        value: {case['bread_milk_support']:.4f}
        how: "share of the 40,000 carts that hold both bread and toned milk"
        used_in: notebook 02 cell 7
      - id: bread_milk_conf
        value: {case['bread_milk_conf']:.4f}
        how: "P(milk | bread), computed as bread_milk_support divided by bread_marginal"
        used_in: deck half1 chapter 2 trap slide, notebook 02 cell 8, cheat sheet panel 1
      - id: bread_milk_lift
        value: {case['bread_milk_lift']:.4f}
        how: "bread_milk_support divided by (bread_marginal times milk_marginal)"
        used_in: deck half1 chapter 2 reveal slide, notebook 02 cell 9, cheat sheet panel 1
      - id: eggs_milk_conf
        value: {case['eggs_milk_conf']:.4f}
        how: "P(milk | eggs), the same shape as bread -> milk"
        used_in: notebook 02 cell 10
      - id: eggs_milk_lift
        value: {case['eggs_milk_lift']:.4f}
        how: "symmetric lift between eggs and toned milk"
        used_in: notebook 02 cell 10
      - id: chips_cold_support
        value: {case['chips_cold_support']:.4f}
        how: "share of the 40,000 carts that hold both chips and a cold drink"
        used_in: deck half1 chapter 2 reveal slide, notebook 02 cell 12
      - id: chips_cold_conf
        value: {case['chips_cold_conf_c']:.4f}
        how: "P(cold | chips), chips_cold_support divided by chips_marginal"
        used_in: notebook 02 cell 12
      - id: cold_chips_conf
        value: {case['chips_cold_conf_d']:.4f}
        how: "P(chips | cold), chips_cold_support divided by cold_marginal"
        used_in: notebook 02 cell 12
      - id: chips_cold_lift
        value: {case['chips_cold_lift']:.4f}
        how: "chips_cold_support divided by (chips_marginal times cold_marginal)"
        used_in: deck half1 chapter 2, notebook 02 cell 13, cheat sheet panel 1
      - id: ice_choc_support
        value: {case['ice_choc_support']:.6f}
        how: "share of the 40,000 carts that hold both ice cream and chocolate sauce"
        used_in: deck half1 chapter 2, notebook 02 cell 14
      - id: ice_choc_lift
        value: {case['ice_choc_lift']:.4f}
        how: "ice_choc_support divided by (icecream_marginal times chocsauce_marginal)"
        used_in: deck half1 chapter 2 thin-pair slide, notebook 02 cell 14
      - id: heavy_tenth_share
        value: {case['heavy_tenth_share']:.4f}
        how: "carts placed by the top ten percent of customers, divided by total carts"
        used_in: deck half1 chapter 3 caveat slide, notebook 03

    # ----------------------------------------------------------------- the twelve printed rows
    twelve_rows:
      - id: twelve_milk
        value: {twelve['milk_n']}
        how: "the number of the twelve printed carts that hold toned milk"
        used_in: deck half1 chapter 1, notebook 01 cell 4, cheat sheet panel 2
      - id: twelve_bread
        value: {twelve['bread_n']}
        how: "the number of the twelve printed carts that hold bread"
        used_in: deck half1 chapter 1, notebook 01 cell 4
      - id: twelve_bread_milk
        value: {twelve['bread_milk_n']}
        how: "the number of the twelve printed carts that hold both bread and toned milk"
        used_in: deck half1 chapter 1, notebook 01 cell 5
      - id: twelve_bread_milk_conf
        value: {twelve['bread_milk_conf_12']:.4f}
        how: "twelve_bread_milk divided by twelve_bread; the hand count's confidence"
        used_in: deck half1 chapter 1 reveal slide, notebook 01 cell 5, cheat sheet panel 2
      - id: twelve_bread_milk_lift
        value: {twelve['bread_milk_lift_12']:.4f}
        how: "the hand count's lift from the twelve rows"
        used_in: deck half1 chapter 1 reveal slide, notebook 01 cell 6, cheat sheet panel 2
      - id: twelve_chips
        value: {twelve['chips_n']}
        how: "the number of the twelve printed carts that hold chips"
        used_in: deck half1 chapter 1, notebook 01 cell 7
      - id: twelve_cold
        value: {twelve['cold_n']}
        how: "the number of the twelve printed carts that hold a cold drink"
        used_in: deck half1 chapter 1, notebook 01 cell 7
      - id: twelve_chips_cold
        value: {twelve['chips_cold_n']}
        how: "the number of the twelve printed carts that hold both chips and a cold drink"
        used_in: deck half1 chapter 1, notebook 01 cell 7
      - id: twelve_chips_cold_support
        value: {twelve['chips_cold_support_12']:.4f}
        how: "twelve_chips_cold divided by 12"
        used_in: notebook 01 cell 8, cheat sheet panel 2
      - id: twelve_chips_cold_conf
        value: {twelve['chips_cold_conf_12']:.4f}
        how: "twelve_chips_cold divided by twelve_chips"
        used_in: notebook 01 cell 8
      - id: twelve_chips_cold_lift
        value: {twelve['chips_cold_lift_12']:.4f}
        how: "the hand count's lift for the chips and cold-drink pair"
        used_in: notebook 01 cell 8, cheat sheet panel 2
      - id: twelve_ice_choc
        value: {twelve['ice_choc_n']}
        how: "the number of the twelve printed carts that hold both ice cream and chocolate sauce"
        used_in: deck half1 chapter 1 rare-pair slide, notebook 01 cell 9
      - id: twelve_ice_choc_lift
        value: {twelve['ice_choc_lift_12']:.4f}
        how: "the hand count's lift for the ice cream and chocolate sauce pair"
        used_in: notebook 01 cell 9

    # ----------------------------------------------------------------- the Rs 9 slot value
    slot_value:
      - id: pune_cart_views_a_day
        value: 60000
        how: "assumption with a range of 50,000 to 70,000; labelled on every slide and sheet"
        used_in: deck half1 chapter 3, notebook 03
      - id: strip_add_rate
        value: 0.50
        how: "assumption with a range of 0.4 to 0.6; labelled on every slide and sheet"
        used_in: deck half1 chapter 3, notebook 03
      - id: margin_per_add_rs
        value: 9
        how: "assumption with a range of Rs 7 to Rs 11; labelled on every slide and sheet"
        used_in: deck half1 chapter 3, notebook 03
      - id: slot_value_at_other_rs_day
        value: 17280
        how: "60,000 x 0.064 x 0.5 x 9, in Rs per day"
        used_in: deck half1 chapter 3 waterfall slide, notebook 03, cheat sheet panel 2
      - id: slot_value_at_milk_rs_day
        value: 3240
        how: "60,000 x 0.012 x 0.5 x 9, in Rs per day"
        used_in: deck half1 chapter 3 waterfall slide, notebook 03, cheat sheet panel 2
      - id: slot_value_gap_rs_month
        value: 421200
        how: "(17280 - 3240) x 30, in Rs per month per slot"
        used_in: deck half1 chapter 3, notebook 03
      - id: slot_value_three_slots_rs_month
        value: 1263600
        how: "3 x slot_value_gap_rs_month, in Rs per month"
        used_in: deck half1 chapter 3 close, notebook 03
      - id: support_floor_percent
        value: 1.0
        how: "the floor the room sets to count the pairs that qualify; 1 percent of 40,000 is 400"
        used_in: deck half1 chapter 3, notebook 03

    # ----------------------------------------------------------------- the Kalpa transfer, lab only
    # These numbers sit in TRAINER files and in notebook 04's your-turn cell outputs. No STUDENT
    # file names them before the lab, per decision w4-finding-once-found.
    kalpa_lab:
      - id: kalpa_consumer_baskets
        value: {kalpa['consumer_count']}
        how: "consumer baskets in the Kalpa transfer dataset"
        used_in: notebook 04 cell 1, trainer lab note
      - id: kalpa_business_orders
        value: {kalpa['business_count']}
        how: "Business orders in the Kalpa transfer dataset"
        used_in: notebook 04 cell 1
      - id: kalpa_charger_share
        value: {kalpa['charger_share']:.4f}
        how: "share of Kalpa consumer baskets that hold the Rs 199 phone charger"
        used_in: notebook 04 your-turn output, trainer lab note (TRAINER until the lab)
      - id: kalpa_screen_charger_conf
        value: {kalpa['screen_conf_to_charger']:.4f}
        how: "P(charger | screen protector), the plant the row names"
        used_in: notebook 04 cell 7 output (TRAINER until the lab)
      - id: kalpa_screen_charger_lift
        value: {kalpa['screen_charger_lift']:.4f}
        how: "symmetric lift between screen protector and the charger"
        used_in: notebook 04 cell 7 output (TRAINER until the lab)
      - id: kalpa_strongest_pair_lift
        value: {kalpa['strongest_pair_lift']:.4f}
        how: "lift of the strongest pair above a 5 percent support floor, wireless earphones and earphone case"
        used_in: notebook 04 cell 8 output (TRAINER until the lab)
      - id: kalpa_strongest_pair_support
        value: {kalpa['strongest_pair_support']:.4f}
        how: "support of wireless earphones and earphone case"
        used_in: notebook 04 cell 8 output (TRAINER until the lab)
      - id: kalpa_thin_pair_lift
        value: {kalpa['thin_pair_lift']:.4f}
        how: "lift of the one pair with support between 0.2 and 0.4 percent, USB-C cable and car charger"
        used_in: notebook 04 cell 9 output (TRAINER until the lab)
      - id: kalpa_thin_pair_support
        value: {kalpa['thin_pair_support']:.4f}
        how: "support of USB-C cable and car charger"
        used_in: notebook 04 cell 9 output (TRAINER until the lab)
    """).lstrip("\n")
    FACTS.write_text(text, encoding="utf-8")
    print(f"\nFacts file written: {FACTS.relative_to(HERE.parent.parent.parent.parent)}")


# ---- main ---------------------------------------------------------------------------------------
def main():
    print("Building the Wednesday case data...")
    carts, cart_items = write_carts()
    print(f"  wrote {len(carts):,} carts and {len(cart_items):,} cart item lines")
    strip = write_strip_log()
    print(f"  wrote {len(strip):,} strip_log rows")
    twelve = write_twelve_rows()
    print(f"  wrote the twelve printed carts")
    kalpa_orders, kalpa_items = write_kalpa()
    print(f"  wrote {len(kalpa_orders):,} Kalpa orders and {len(kalpa_items):,} order lines")
    print("\nVerifying the case targets...")
    case_results = verify_case(carts, cart_items)
    print("\nVerifying the strip_log click-throughs...")
    strip_results = verify_strip(strip)
    print("\nVerifying the twelve-row hand counts...")
    twelve_results = verify_twelve_rows(twelve)
    print("\nVerifying the Kalpa transfer plants...")
    kalpa_results = verify_kalpa(kalpa_orders, kalpa_items)
    write_facts(case_results, strip_results, twelve_results, kalpa_results)
    print("\nAll assertions passed.")


if __name__ == "__main__":
    main()

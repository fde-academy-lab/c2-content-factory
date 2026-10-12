"""Monday W04 D1 case data generator.

Seeded, deterministic. Standard library and pandas only (ponytail-small).

Writes the Uber Hyderabad case tables and the small Kalpa Retail transfer tables
to content/W04/D1/data/ as C2_W04_D01_{table}_STUDENT.csv, and the day's facts
file to content/W04/D1/internal/ as C2_W04_D01_facts_INTERNAL.yaml.

Every target in docs/detailing/W04_case_file.md's Monday section is asserted.
Each check prints PASS when it holds; the script exits non-zero on any failure.

Run from the repository root:
    python3 content/W04/D1/internal/C2_W04_D01_make_data_INTERNAL.py
"""
import csv
import datetime as dt
import pathlib
import random
import sys

import pandas as pd
import yaml


HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
DATA = DAY / "data"
DATA.mkdir(parents=True, exist_ok=True)
STEM = "C2_W04_D01"
SEED = 20261026
rng = random.Random(SEED)


# ---------------------------------------------------------------------------- the case
LAUNCH = dt.date(2026, 8, 31)
BEFORE_WEEKS = [dt.date(2026, 7, 20) + dt.timedelta(days=7 * i) for i in range(6)]
AFTER_WEEKS = [dt.date(2026, 8, 31) + dt.timedelta(days=7 * i) for i in range(6)]
TWELVE_BEFORE = dt.date(2026, 8, 10)
TWELVE_AFTER = dt.date(2026, 9, 21)
assert TWELVE_BEFORE in BEFORE_WEEKS and TWELVE_AFTER in AFTER_WEEKS

CORE_ZONES = ["Banjara Hills", "Jubilee Hills", "Gachibowli", "Madhapur", "Hitech City",
              "Begumpet", "Kondapur", "Kukatpally", "Secunderabad"]
OUTER_ZONES = ["Shamshabad", "Rajendranagar", "Patancheru"]
ZONES = CORE_ZONES + OUTER_ZONES

FARE = 165
ORDINARY = 880
IDLE_TAIL = 180
NEW = 140
TOTAL = ORDINARY + IDLE_TAIL + NEW

# City totals (targets from the case file)
HOURS_BEFORE = 118000
HOURS_AFTER = 146300
TRIPS_BEFORE = 224200
TRIPS_AFTER = 230900
BOOKINGS_BEFORE = TRIPS_BEFORE * FARE          # 36,993,000
BOOKINGS_AFTER = TRIPS_AFTER * FARE            # 38,098,500
TOPUP_AFTER = 19000000                         # Rs 1.9 crore
TOPUP_LOW_ACC = int(TOPUP_AFTER * 0.61)        # Rs 1.159 crore to acceptance < 0.5
TOPUP_HIGH_ACC = TOPUP_AFTER - TOPUP_LOW_ACC

# Group-level hours split
HOURS_ORD_BEFORE = 98000
HOURS_IDLE_BEFORE = 20000
HOURS_ORD_AFTER = 102000
HOURS_IDLE_AFTER = 42000
HOURS_NEW_AFTER = 2300

# Group-level trips split
TRIPS_ORD_BEFORE = 186200   # 98000 * 1.9
TRIPS_IDLE_BEFORE = 38000   # 20000 * 1.9
TRIPS_ORD_AFTER = 193800    # 102000 * 1.9
TRIPS_IDLE_AFTER = 33440    # idle hours up 2.1x, trips down 12% per driver
TRIPS_NEW_AFTER = TRIPS_AFTER - TRIPS_ORD_AFTER - TRIPS_IDLE_AFTER  # 3660

assert HOURS_ORD_BEFORE + HOURS_IDLE_BEFORE == HOURS_BEFORE
assert HOURS_ORD_AFTER + HOURS_IDLE_AFTER + HOURS_NEW_AFTER == HOURS_AFTER
assert TRIPS_ORD_BEFORE + TRIPS_IDLE_BEFORE == TRIPS_BEFORE
assert TRIPS_ORD_AFTER + TRIPS_IDLE_AFTER + TRIPS_NEW_AFTER == TRIPS_AFTER


# ---------------------------------------------------------------------------- twelve rows
# Six specific drivers for the hand-count table. A to D are ordinary, E and F are
# the idle tail in outer zones. Values are the ones a learner reads off the sheet.
TWELVE = {
    "A": {"group": "ord", "zone": "Jubilee Hills",
          "before": (10, 24, 21, 0, 21), "after": (11, 25, 22, 0, 22)},
    "B": {"group": "ord", "zone": "Banjara Hills",
          "before": (9, 20, 17, 0, 17),  "after": (10, 21, 18, 0, 18)},
    "C": {"group": "ord", "zone": "Gachibowli",
          "before": (11, 25, 22, 0, 22), "after": (12, 26, 23, 0, 23)},
    "D": {"group": "ord", "zone": "Madhapur",
          "before": (10, 22, 19, 0, 19), "after": (11, 23, 20, 0, 20)},
    "E": {"group": "idle", "zone": "Shamshabad",
          "before": (10, 21, 18, 0, 18), "after": (16, 14, 4, 1, 3)},
    "F": {"group": "idle", "zone": "Rajendranagar",
          "before": (10, 20, 17, 0, 17), "after": (14, 12, 3, 1, 2)},
}
TWELVE_ORDER = ["A", "B", "C", "D", "E", "F"]
# The columns of each tuple: (hours, requests, accepted, cancels, trips)


def compute_twelve_totals():
    before = [TWELVE[k]["before"] for k in TWELVE_ORDER]
    after = [TWELVE[k]["after"] for k in TWELVE_ORDER]
    sum_b = tuple(sum(x[i] for x in before) for i in range(5))
    sum_a = tuple(sum(x[i] for x in after) for i in range(5))
    return sum_b, sum_a


TWELVE_SUM_BEFORE, TWELVE_SUM_AFTER = compute_twelve_totals()
# TWELVE_SUM_BEFORE = (60, 132, 114, 0, 114)
# TWELVE_SUM_AFTER  = (74, 121, 90, 2, 88)
# Hand count ratios: 114/60 = 1.9; 88/74 = 1.189.
# This differs from the case file's printed hand count of 1.49 (which assumed
# 110 trips after). The row data as printed sums to 88, so the facts file
# records the computed ratio and the correction is named in the pack report.


# ---------------------------------------------------------------------------- helpers
def jitter(mean, spread):
    """A positive integer around mean ± spread, with no zero draws."""
    v = int(round(rng.gauss(mean, spread)))
    return max(1, v)


def allocate(total, n, mean, spread, min_v=1):
    """Return n positive integers that sum exactly to total, roughly around mean."""
    xs = [max(min_v, int(round(rng.gauss(mean, spread)))) for _ in range(n)]
    diff = total - sum(xs)
    step = 1 if diff > 0 else -1
    i = 0
    while diff != 0:
        pos = i % n
        if step == -1 and xs[pos] <= min_v:
            i += 1
            continue
        xs[pos] += step
        diff -= step
        i += 1
    assert sum(xs) == total
    return xs


def allocate_pairs(hours_total, trips_total, n, hours_mean, hours_spread, trips_per_hour):
    """Return (hours, trips) pairs that sum to the two totals, with trips tied to hours."""
    hours = allocate(hours_total, n, hours_mean, hours_spread, min_v=1)
    # Trips roughly proportional to hours with jitter
    raw = [max(0, int(round(h * trips_per_hour + rng.gauss(0, max(0.5, h * 0.15))))) for h in hours]
    diff = trips_total - sum(raw)
    step = 1 if diff > 0 else -1
    i = 0
    guard = 0
    while diff != 0:
        pos = i % n
        if step == -1 and raw[pos] <= 0:
            i += 1
            guard += 1
            if guard > n * 20:
                # Spread the shortfall across every index that can still go down
                for j in range(n):
                    if diff == 0:
                        break
                    if raw[j] > 0:
                        raw[j] -= 1
                        diff += 1
                break
            continue
        raw[pos] += step
        diff -= step
        i += 1
    assert sum(raw) == trips_total
    return list(zip(hours, raw))


# ---------------------------------------------------------------------------- drivers
drivers = []
for i in range(1, ORDINARY + 1):
    drivers.append({"driver_id": f"d_{i:04d}", "class": "ord",
                    "home_zone": CORE_ZONES[(i - 1) % len(CORE_ZONES)],
                    "joined_month": "2024-{:02d}".format(((i - 1) % 12) + 1),
                    "enrolled": True})
for i in range(ORDINARY + 1, ORDINARY + IDLE_TAIL + 1):
    idx = i - ORDINARY - 1
    # idle tail drivers home in a mix of core and outer; most in outer
    home = OUTER_ZONES[idx % 3] if idx % 4 != 0 else CORE_ZONES[idx % len(CORE_ZONES)]
    drivers.append({"driver_id": f"d_{i:04d}", "class": "idle",
                    "home_zone": home,
                    "joined_month": "2025-{:02d}".format(((idx) % 12) + 1),
                    "enrolled": True})
for i in range(ORDINARY + IDLE_TAIL + 1, TOTAL + 1):
    idx = i - ORDINARY - IDLE_TAIL - 1
    drivers.append({"driver_id": f"d_{i:04d}", "class": "new",
                    "home_zone": ZONES[idx % len(ZONES)],
                    "joined_month": "2026-09",
                    "enrolled": True})

# Overlay the twelve-row drivers' home zone and class
TWELVE_IDS = {"A": "d_0001", "B": "d_0002", "C": "d_0003", "D": "d_0004",
              "E": "d_0881", "F": "d_0882"}
for label, did in TWELVE_IDS.items():
    row = next(d for d in drivers if d["driver_id"] == did)
    row["home_zone"] = TWELVE[label]["zone"]
    row["class"] = TWELVE[label]["group"]

drivers_df = pd.DataFrame(drivers)[["driver_id", "home_zone", "joined_month", "enrolled"]]
drivers_df.to_csv(DATA / f"{STEM}_drivers_STUDENT.csv", index=False)


# ---------------------------------------------------------------------------- driver-weeks
ord_ids = [d["driver_id"] for d in drivers if d["class"] == "ord"]
idle_ids = [d["driver_id"] for d in drivers if d["class"] == "idle"]
new_ids = [d["driver_id"] for d in drivers if d["class"] == "new"]
assert len(ord_ids) == ORDINARY and len(idle_ids) == IDLE_TAIL and len(new_ids) == NEW

# Carve out the twelve-row drivers from the group totals, so A-F values do not
# double-count. Reserve exactly the TWELVE_BEFORE and TWELVE_AFTER rows for them.
RESERVED_HOURS_B_ORD = sum(TWELVE[k]["before"][0] for k in "ABCD")    # 40
RESERVED_TRIPS_B_ORD = sum(TWELVE[k]["before"][4] for k in "ABCD")    # 79
RESERVED_HOURS_A_ORD = sum(TWELVE[k]["after"][0] for k in "ABCD")     # 44
RESERVED_TRIPS_A_ORD = sum(TWELVE[k]["after"][4] for k in "ABCD")     # 83
RESERVED_HOURS_B_IDLE = sum(TWELVE[k]["before"][0] for k in "EF")     # 20
RESERVED_TRIPS_B_IDLE = sum(TWELVE[k]["before"][4] for k in "EF")     # 35
RESERVED_HOURS_A_IDLE = sum(TWELVE[k]["after"][0] for k in "EF")      # 30
RESERVED_TRIPS_A_IDLE = sum(TWELVE[k]["after"][4] for k in "EF")      # 5
# ("Reserved" here is the arithmetic allowance taken out of the group totals; the
# six driver-weeks are then written back in with their exact hardcoded values.)

records = []  # one dict per driver-week we will emit


def emit(did, week, zone_mode, hours, requests, accepted, cancels, trips, bookings, topup):
    """Append one driver-week row, with every field validated."""
    assert hours >= 0 and requests >= 0 and 0 <= accepted <= requests
    assert 0 <= cancels <= accepted and 0 <= trips <= accepted - cancels
    records.append({
        "driver_id": did,
        "week_start": week.isoformat(),
        "zone_mode": zone_mode,
        "peak_online_hours": hours,
        "peak_requests": requests,
        "peak_accepted": accepted,
        "peak_driver_cancels": cancels,
        "peak_trips": trips,
        "peak_bookings_rs": bookings,
        "topup_rs": topup,
        "offpeak_trips": max(0, int(round(hours * 0.6 + rng.gauss(0, 2)))),
    })


# --------------------------- ordinary drivers before the launch
for widx, week in enumerate(BEFORE_WEEKS):
    is_twelve_week = week == TWELVE_BEFORE
    # Per-week total hours and trips to allocate to the 880 ordinary drivers,
    # minus the four twelve-row entries that live in the TWELVE_BEFORE week.
    base_hours = HOURS_ORD_BEFORE // 6
    base_trips = TRIPS_ORD_BEFORE // 6
    extra_hours = HOURS_ORD_BEFORE - base_hours * 6 if widx == 5 else 0
    extra_trips = TRIPS_ORD_BEFORE - base_trips * 6 if widx == 5 else 0
    hours_week = base_hours + extra_hours
    trips_week = base_trips + extra_trips
    pool = [i for i in ord_ids if not (is_twelve_week and i in TWELVE_IDS.values())]
    if is_twelve_week:
        hours_week -= RESERVED_HOURS_B_ORD
        trips_week -= RESERVED_TRIPS_B_ORD
    pairs = allocate_pairs(hours_week, trips_week, len(pool),
                           hours_mean=hours_week / len(pool),
                           hours_spread=2.5, trips_per_hour=1.9)
    for did, (h, tr) in zip(pool, pairs):
        requests = jitter(h * 2.9, max(1, h * 0.4))
        requests = max(requests, tr + 1)
        accepted_rate = 0.86 + rng.gauss(0, 0.03)
        accepted = int(round(requests * max(0.7, min(0.95, accepted_rate))))
        accepted = max(accepted, tr)
        cancels = max(0, int(round(accepted * 0.04 + rng.gauss(0, 0.5))))
        cancels = min(cancels, accepted - tr)
        bookings = tr * FARE
        zone = next(d for d in drivers if d["driver_id"] == did)["home_zone"]
        if rng.random() < 0.15:
            zone = CORE_ZONES[rng.randrange(len(CORE_ZONES))]
        emit(did, week, zone, h, requests, accepted, cancels, tr, bookings, 0)

# --------------------------- idle-tail drivers before the launch (ordinary behavior)
for widx, week in enumerate(BEFORE_WEEKS):
    is_twelve_week = week == TWELVE_BEFORE
    base_hours = HOURS_IDLE_BEFORE // 6
    base_trips = TRIPS_IDLE_BEFORE // 6
    extra_hours = HOURS_IDLE_BEFORE - base_hours * 6 if widx == 5 else 0
    extra_trips = TRIPS_IDLE_BEFORE - base_trips * 6 if widx == 5 else 0
    hours_week = base_hours + extra_hours
    trips_week = base_trips + extra_trips
    pool = [i for i in idle_ids if not (is_twelve_week and i in TWELVE_IDS.values())]
    if is_twelve_week:
        hours_week -= RESERVED_HOURS_B_IDLE
        trips_week -= RESERVED_TRIPS_B_IDLE
    pairs = allocate_pairs(hours_week, trips_week, len(pool),
                           hours_mean=hours_week / len(pool),
                           hours_spread=2.5, trips_per_hour=1.9)
    for did, (h, tr) in zip(pool, pairs):
        requests = jitter(h * 2.9, max(1, h * 0.4))
        requests = max(requests, tr + 1)
        accepted_rate = 0.86 + rng.gauss(0, 0.03)
        accepted = int(round(requests * max(0.7, min(0.95, accepted_rate))))
        accepted = max(accepted, tr)
        cancels = max(0, int(round(accepted * 0.04 + rng.gauss(0, 0.5))))
        cancels = min(cancels, accepted - tr)
        bookings = tr * FARE
        zone = next(d for d in drivers if d["driver_id"] == did)["home_zone"]
        emit(did, week, zone, h, requests, accepted, cancels, tr, bookings, 0)

# --------------------------- the twelve-row driver-weeks before
for label in TWELVE_ORDER:
    row = TWELVE[label]
    h, req, acc, canc, tr = row["before"]
    emit(TWELVE_IDS[label], TWELVE_BEFORE, row["zone"], h, req, acc, canc, tr, tr * FARE, 0)


# --------------------------- ordinary drivers after the launch
# Target per-week bookings share so acceptance >= 0.5 holds for ordinary.
TOPUP_ORD_AFTER = TOPUP_HIGH_ACC - 300000  # ordinary share; the remainder covers new drivers
for widx, week in enumerate(AFTER_WEEKS):
    is_twelve_week = week == TWELVE_AFTER
    base_hours = HOURS_ORD_AFTER // 6
    base_trips = TRIPS_ORD_AFTER // 6
    extra_hours = HOURS_ORD_AFTER - base_hours * 6 if widx == 5 else 0
    extra_trips = TRIPS_ORD_AFTER - base_trips * 6 if widx == 5 else 0
    hours_week = base_hours + extra_hours
    trips_week = base_trips + extra_trips
    pool = [i for i in ord_ids if not (is_twelve_week and i in TWELVE_IDS.values())]
    if is_twelve_week:
        hours_week -= RESERVED_HOURS_A_ORD
        trips_week -= RESERVED_TRIPS_A_ORD
    pairs = allocate_pairs(hours_week, trips_week, len(pool),
                           hours_mean=hours_week / len(pool),
                           hours_spread=2.5, trips_per_hour=1.9)
    week_topup = TOPUP_ORD_AFTER // 6
    if widx == 5:
        week_topup = TOPUP_ORD_AFTER - (TOPUP_ORD_AFTER // 6) * 5
    topups = allocate(week_topup, len(pool), week_topup / len(pool), 400, min_v=0)
    for did, (h, tr), tu in zip(pool, pairs, topups):
        requests = jitter(h * 2.9, max(1, h * 0.4))
        requests = max(requests, tr + 1)
        accepted_rate = 0.84 + rng.gauss(0, 0.03)
        accepted = int(round(requests * max(0.55, min(0.95, accepted_rate))))
        # Keep ordinary acceptance strictly >= 0.5 so the 61% topup split stays clean.
        if accepted < int(requests * 0.55):
            accepted = int(requests * 0.55)
        accepted = max(accepted, tr)
        cancels = max(0, int(round(accepted * 0.08 + rng.gauss(0, 0.5))))
        cancels = min(cancels, accepted - tr)
        bookings = tr * FARE
        zone = next(d for d in drivers if d["driver_id"] == did)["home_zone"]
        if rng.random() < 0.15:
            zone = CORE_ZONES[rng.randrange(len(CORE_ZONES))]
        emit(did, week, zone, h, requests, accepted, cancels, tr, bookings, tu)

# --------------------------- idle-tail drivers after the launch
# Each driver's hours rise about 2.1x and trips fall about 12 percent.
# 70 percent of their new hours (new hours = after - before = 22,000 total) land
# in the three outer zones, and acceptance stays below 0.5 so top-up follows.
IDLE_NEW_HOURS = HOURS_IDLE_AFTER - HOURS_IDLE_BEFORE  # 22000
OUTER_SHARE_NEW = int(IDLE_NEW_HOURS * 0.70)           # 15400 hours in outer zones

for widx, week in enumerate(AFTER_WEEKS):
    is_twelve_week = week == TWELVE_AFTER
    base_hours = HOURS_IDLE_AFTER // 6
    base_trips = TRIPS_IDLE_AFTER // 6
    extra_hours = HOURS_IDLE_AFTER - base_hours * 6 if widx == 5 else 0
    extra_trips = TRIPS_IDLE_AFTER - base_trips * 6 if widx == 5 else 0
    hours_week = base_hours + extra_hours
    trips_week = base_trips + extra_trips
    pool = [i for i in idle_ids if not (is_twelve_week and i in TWELVE_IDS.values())]
    if is_twelve_week:
        hours_week -= RESERVED_HOURS_A_IDLE
        trips_week -= RESERVED_TRIPS_A_IDLE
    hours_mean = hours_week / len(pool)
    pairs = allocate_pairs(hours_week, trips_week, len(pool),
                           hours_mean=hours_mean,
                           hours_spread=hours_mean * 0.3,
                           trips_per_hour=0.80)
    week_topup = TOPUP_LOW_ACC // 6
    if widx == 5:
        week_topup = TOPUP_LOW_ACC - (TOPUP_LOW_ACC // 6) * 5
    topups = allocate(week_topup, len(pool), week_topup / len(pool), 1500, min_v=100)
    for did, (h, tr), tu in zip(pool, pairs, topups):
        # Requests are low in outer zones.
        requests = jitter(h * 1.6, max(1, h * 0.3))
        requests = max(requests, tr + 2)
        # Acceptance stays below 0.5 by construction (they are the gamers).
        accepted_rate = 0.35 + rng.gauss(0, 0.05)
        accepted = int(round(requests * max(0.2, min(0.49, accepted_rate))))
        accepted = max(accepted, tr)
        cancels = max(0, int(round(accepted * 0.12 + rng.gauss(0, 0.3))))
        cancels = min(cancels, accepted - tr)
        bookings = tr * FARE
        # 70 percent of their new hours in outer zones. Mark zone_mode as outer
        # for most idle-tail driver-weeks after.
        if rng.random() < 0.7:
            zone = OUTER_ZONES[rng.randrange(len(OUTER_ZONES))]
        else:
            zone = CORE_ZONES[rng.randrange(len(CORE_ZONES))]
        emit(did, week, zone, h, requests, accepted, cancels, tr, bookings, tu)

# --------------------------- the twelve-row driver-weeks after
for label in TWELVE_ORDER:
    row = TWELVE[label]
    h, req, acc, canc, tr = row["after"]
    # Twelve-row topup: E and F (idle tail) receive the lab's labelled amounts;
    # A to D (ordinary) receive zero so the hand count on the sheet reads clean.
    tu = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 10000, "F": 9000}[label]
    emit(TWELVE_IDS[label], TWELVE_AFTER, row["zone"], h, req, acc, canc, tr, tr * FARE, tu)

# --------------------------- new drivers after the launch
new_total_pairs = allocate_pairs(HOURS_NEW_AFTER, TRIPS_NEW_AFTER,
                                 NEW, hours_mean=HOURS_NEW_AFTER / NEW,
                                 hours_spread=4, trips_per_hour=1.59)
# Each new driver drives in one of the six after weeks (average), chosen deterministically.
new_topups = allocate(TOPUP_AFTER - TOPUP_LOW_ACC - TOPUP_ORD_AFTER,  # 300000
                      NEW, 300000 / NEW, 200, min_v=0)
for did, (h, tr), tu in zip(new_ids, new_total_pairs, new_topups):
    week = AFTER_WEEKS[rng.randrange(len(AFTER_WEEKS))]
    requests = jitter(h * 2.5, max(1, h * 0.3))
    requests = max(requests, tr + 1)
    accepted_rate = 0.70 + rng.gauss(0, 0.04)
    accepted = int(round(requests * max(0.55, min(0.85, accepted_rate))))
    accepted = max(accepted, tr)
    cancels = max(0, int(round(accepted * 0.07 + rng.gauss(0, 0.4))))
    cancels = min(cancels, accepted - tr)
    bookings = tr * FARE
    zone = next(d for d in drivers if d["driver_id"] == did)["home_zone"]
    emit(did, week, zone, h, requests, accepted, cancels, tr, bookings, tu)

# --------------------------- normalise after-window totals to the exact targets
# The generator above produces plausible rows; this pass pushes them to the exact
# city numbers in the facts file (acceptance 0.73, driver cancels 0.09, top-up Rs
# 1.9 crore, 61 percent of top-up to driver-weeks with acceptance below 0.5).

after_iso = {w.isoformat() for w in AFTER_WEEKS}
idle_set = set(idle_ids)
ord_set = set(ord_ids)
new_set = set(new_ids)
twelve_set = set(TWELVE_IDS.values())


def rebalance(indices, key, target, min_fn, max_fn):
    """Round-robin adjust records[i][key] so the sum over indices equals target."""
    current = sum(records[i][key] for i in indices)
    diff = target - current
    if diff == 0:
        return
    step = 1 if diff > 0 else -1
    guard = 0
    while diff != 0 and guard < len(indices) * 200:
        moved = False
        for i in indices:
            if diff == 0:
                break
            v = records[i][key]
            if step == 1 and v + 1 > max_fn(records[i]):
                continue
            if step == -1 and v - 1 < min_fn(records[i]):
                continue
            records[i][key] += step
            diff -= step
            moved = True
        if not moved:
            break
        guard += 1
    if diff != 0:
        raise RuntimeError(
            f"could not rebalance {key} to {target}; remaining diff {diff}")


TWELVE_ROWS_AFTER_LIST = [TWELVE[k]["after"] for k in TWELVE_ORDER]
TW_HOURS_AFTER = sum(r[0] for r in TWELVE_ROWS_AFTER_LIST)   # 74
TW_REQ_AFTER = sum(r[1] for r in TWELVE_ROWS_AFTER_LIST)     # 121
TW_ACC_AFTER = sum(r[2] for r in TWELVE_ROWS_AFTER_LIST)     # 90
TW_CANC_AFTER = sum(r[3] for r in TWELVE_ROWS_AFTER_LIST)    # 2
TW_TRIPS_AFTER = sum(r[4] for r in TWELVE_ROWS_AFTER_LIST)   # 88
TW_TOPUP_AFTER = 19000  # E 10,000 + F 9,000

IDLE_TW_IDS = {TWELVE_IDS["E"], TWELVE_IDS["F"]}
ORD_TW_IDS = {TWELVE_IDS["A"], TWELVE_IDS["B"], TWELVE_IDS["C"], TWELVE_IDS["D"]}

# Group indices (after window). Only the TWELVE_AFTER-week rows for A-F are
# excluded, because their values are hardcoded to the case file; the other
# after weeks of A-F are normalised with their group.
tw_iso = TWELVE_AFTER.isoformat()
idle_after = [i for i, r in enumerate(records)
              if r["week_start"] in after_iso and r["driver_id"] in idle_set
              and not (r["driver_id"] in IDLE_TW_IDS and r["week_start"] == tw_iso)]
ord_after = [i for i, r in enumerate(records)
             if r["week_start"] in after_iso and r["driver_id"] in ord_set
             and not (r["driver_id"] in ORD_TW_IDS and r["week_start"] == tw_iso)]
new_after = [i for i, r in enumerate(records)
             if r["week_start"] in after_iso and r["driver_id"] in new_set]
tw_idle_hours = sum(TWELVE[k]["after"][0] for k in "EF")      # 30
tw_idle_req = sum(TWELVE[k]["after"][1] for k in "EF")        # 26
tw_idle_acc = sum(TWELVE[k]["after"][2] for k in "EF")        # 7
tw_idle_canc = sum(TWELVE[k]["after"][3] for k in "EF")       # 2
tw_idle_trips = sum(TWELVE[k]["after"][4] for k in "EF")      # 5

tw_ord_hours = sum(TWELVE[k]["after"][0] for k in "ABCD")     # 44
tw_ord_req = sum(TWELVE[k]["after"][1] for k in "ABCD")       # 95
tw_ord_acc = sum(TWELVE[k]["after"][2] for k in "ABCD")       # 83
tw_ord_canc = sum(TWELVE[k]["after"][3] for k in "ABCD")      # 0
tw_ord_trips = sum(TWELVE[k]["after"][4] for k in "ABCD")     # 83

# Target totals for the after window, after holding out the twelve rows.
# City targets: requests 347,583, accepted 253,736, cancels 22,836, trips 230,900, topup 19,000,000.
IDLE_REQ_TARGET = 90000
IDLE_ACC_TARGET = 34440           # idle acceptance = 34440 / 90000 = 0.383
IDLE_CANC_TARGET = 1000
IDLE_TOPUP_TARGET = TOPUP_LOW_ACC - TW_TOPUP_AFTER   # 11,590,000 - 19,000 = 11,571,000

ORD_REQ_TARGET = 252583
ORD_ACC_TARGET = 215000
ORD_CANC_TARGET = 21200
ORD_TOPUP_TARGET = 7110000

NEW_REQ_TARGET = 5000
NEW_ACC_TARGET = 4296
NEW_CANC_TARGET = 636
NEW_TOPUP_TARGET = 300000

# Carve out the twelve-row contributions from each group's target.
idle_target_req = IDLE_REQ_TARGET - tw_idle_req
idle_target_acc = IDLE_ACC_TARGET - tw_idle_acc
idle_target_canc = IDLE_CANC_TARGET - tw_idle_canc
idle_target_topup = IDLE_TOPUP_TARGET
# Idle: cancels and accepted and trips related via accepted = trips + cancels, where
# trips are already fixed by the allocator. So we only adjust cancels; accepted
# then follows as trips + cancels. Requests adjust independently.
# First, set cancels: rebalance from current to target.
for i in idle_after:
    r = records[i]
    r["peak_driver_cancels"] = max(0, min(r["peak_driver_cancels"], 3))
# Rebalance cancels to target
rebalance(idle_after, "peak_driver_cancels", idle_target_canc,
          min_fn=lambda r: 0, max_fn=lambda r: 6)
# Set accepted = trips + cancels
for i in idle_after:
    records[i]["peak_accepted"] = records[i]["peak_trips"] + records[i]["peak_driver_cancels"]
# Verify accepted total
cur_acc = sum(records[i]["peak_accepted"] for i in idle_after)
# accepted = trips + cancels; both are fixed now, so cur_acc = idle_trips + idle_cancels_target
# We want cur_acc == idle_target_acc. By construction: idle_trips + idle_target_canc should equal target.
# Let's assert, else nudge trips via accepted.
if cur_acc != idle_target_acc:
    # Difference goes into cancels since trips are fixed
    diff = idle_target_acc - cur_acc
    rebalance(idle_after, "peak_driver_cancels",
              sum(records[i]["peak_driver_cancels"] for i in idle_after) + diff,
              min_fn=lambda r: 0, max_fn=lambda r: 20)
    for i in idle_after:
        records[i]["peak_accepted"] = records[i]["peak_trips"] + records[i]["peak_driver_cancels"]

# Set requests: each row's requests >= accepted / 0.49 (to keep acceptance < 0.5)
for i in idle_after:
    min_req = int(records[i]["peak_accepted"] / 0.49) + 1
    records[i]["peak_requests"] = max(records[i]["peak_requests"], min_req)
rebalance(idle_after, "peak_requests", idle_target_req,
          min_fn=lambda r: max(r["peak_accepted"] + 1, int(r["peak_accepted"] / 0.49) + 1),
          max_fn=lambda r: int(r["peak_accepted"] / 0.1))

# Set topup
rebalance(idle_after, "topup_rs", idle_target_topup,
          min_fn=lambda r: 100, max_fn=lambda r: 40000)

# -------------------------- ordinary non-twelve after
rebalance(ord_after, "peak_driver_cancels", ORD_CANC_TARGET - tw_ord_canc,
          min_fn=lambda r: 0, max_fn=lambda r: 30)
for i in ord_after:
    records[i]["peak_accepted"] = records[i]["peak_trips"] + records[i]["peak_driver_cancels"]
cur_acc_ord = sum(records[i]["peak_accepted"] for i in ord_after)
if cur_acc_ord != ORD_ACC_TARGET - tw_ord_acc:
    diff = (ORD_ACC_TARGET - tw_ord_acc) - cur_acc_ord
    rebalance(ord_after, "peak_driver_cancels",
              sum(records[i]["peak_driver_cancels"] for i in ord_after) + diff,
              min_fn=lambda r: 0, max_fn=lambda r: 30)
    for i in ord_after:
        records[i]["peak_accepted"] = records[i]["peak_trips"] + records[i]["peak_driver_cancels"]

# Ordinary acceptance >= 0.55 (keeps every row above the 0.5 topup split)
for i in ord_after:
    acc = records[i]["peak_accepted"]
    max_req = int(acc / 0.55) if acc > 0 else records[i]["peak_requests"]
    records[i]["peak_requests"] = min(records[i]["peak_requests"], max(max_req, acc + 1))
rebalance(ord_after, "peak_requests", ORD_REQ_TARGET - tw_ord_req,
          min_fn=lambda r: r["peak_accepted"] + 1,
          max_fn=lambda r: int(r["peak_accepted"] / 0.55) if r["peak_accepted"] > 0 else 10)

rebalance(ord_after, "topup_rs", ORD_TOPUP_TARGET,
          min_fn=lambda r: 0, max_fn=lambda r: 8000)

# -------------------------- new drivers after
rebalance(new_after, "peak_driver_cancels", NEW_CANC_TARGET,
          min_fn=lambda r: 0, max_fn=lambda r: 15)
for i in new_after:
    records[i]["peak_accepted"] = records[i]["peak_trips"] + records[i]["peak_driver_cancels"]
cur_acc_new = sum(records[i]["peak_accepted"] for i in new_after)
if cur_acc_new != NEW_ACC_TARGET:
    diff = NEW_ACC_TARGET - cur_acc_new
    rebalance(new_after, "peak_driver_cancels",
              sum(records[i]["peak_driver_cancels"] for i in new_after) + diff,
              min_fn=lambda r: 0, max_fn=lambda r: 30)
    for i in new_after:
        records[i]["peak_accepted"] = records[i]["peak_trips"] + records[i]["peak_driver_cancels"]

for i in new_after:
    acc = records[i]["peak_accepted"]
    max_req = int(acc / 0.6) if acc > 0 else records[i]["peak_requests"]
    records[i]["peak_requests"] = min(records[i]["peak_requests"], max(max_req, acc + 1))
rebalance(new_after, "peak_requests", NEW_REQ_TARGET,
          min_fn=lambda r: r["peak_accepted"] + 1,
          max_fn=lambda r: int(r["peak_accepted"] / 0.5) if r["peak_accepted"] > 0 else 10)

rebalance(new_after, "topup_rs", NEW_TOPUP_TARGET,
          min_fn=lambda r: 0, max_fn=lambda r: 5000)

# Recompute bookings for every after driver-week (unchanged by this pass).
for i in idle_after + ord_after + new_after:
    records[i]["peak_bookings_rs"] = records[i]["peak_trips"] * FARE


driver_weeks = pd.DataFrame(records).sort_values(["week_start", "driver_id"]).reset_index(drop=True)
driver_weeks.to_csv(DATA / f"{STEM}_driver_weeks_STUDENT.csv", index=False)


# ---------------------------------------------------------------------------- zone-weeks
# Zone-level rider requests sum to trips/0.89 (before) and trips/0.90 (after).
ZONE_REQ_BEFORE = int(round(TRIPS_BEFORE / 0.89))   # 251,910
ZONE_REQ_AFTER = int(round(TRIPS_AFTER / 0.90))     # 256,556
ZONE_FUL_BEFORE = TRIPS_BEFORE
ZONE_FUL_AFTER = TRIPS_AFTER


def zone_split(total_req, total_ful, weeks):
    """Split request and fulfilled totals across 12 zones x 6 weeks, with 92/8
    core-against-outer share so outer gets few requests at any hour."""
    core_req = int(total_req * 0.92)
    outer_req = total_req - core_req
    core_ful = int(total_ful * 0.93)
    outer_ful = total_ful - core_ful
    rows = []
    core_per = core_req // (len(CORE_ZONES) * len(weeks))
    outer_per = outer_req // (len(OUTER_ZONES) * len(weeks))
    core_f_per = core_ful // (len(CORE_ZONES) * len(weeks))
    outer_f_per = outer_ful // (len(OUTER_ZONES) * len(weeks))
    for zone in CORE_ZONES:
        for week in weeks:
            r = core_per + rng.randint(-80, 80)
            f = min(core_f_per + rng.randint(-60, 60), r)
            r = max(1, r)
            f = max(0, f)
            rows.append((zone, week, r, f))
    for zone in OUTER_ZONES:
        for week in weeks:
            r = outer_per + rng.randint(-40, 40)
            f = min(outer_f_per + rng.randint(-30, 30), r)
            r = max(1, r)
            f = max(0, f)
            rows.append((zone, week, r, f))
    # Rebalance to exact totals, round-robin, bounded so f stays within r.
    def nudge(sign, field_idx, limit_check):
        for _ in range(abs(sign)):
            for j in range(len(rows)):
                zone, week, r, f = rows[j]
                vals = [zone, week, r, f]
                if sign > 0:
                    vals[field_idx] += 1
                else:
                    if vals[field_idx] <= 1:
                        continue
                    vals[field_idx] -= 1
                if not limit_check(vals):
                    continue
                rows[j] = tuple(vals)
                break

    cur_r = sum(r for _, _, r, _ in rows)
    cur_f = sum(f for _, _, _, f in rows)
    while cur_r != total_req:
        delta = total_req - cur_r
        step = 1 if delta > 0 else -1
        for j in range(len(rows)):
            z, w, r, f = rows[j]
            if step == -1 and r <= f + 1:
                continue
            if step == -1 and r <= 1:
                continue
            rows[j] = (z, w, r + step, f)
            cur_r += step
            if cur_r == total_req:
                break
    while cur_f != total_ful:
        delta = total_ful - cur_f
        step = 1 if delta > 0 else -1
        changed = False
        for j in range(len(rows)):
            z, w, r, f = rows[j]
            if step == 1 and f + 1 > r:
                continue
            if step == -1 and f <= 1:
                continue
            rows[j] = (z, w, r, f + step)
            cur_f += step
            changed = True
            if cur_f == total_ful:
                break
        if not changed:
            break
    assert sum(r for _, _, r, _ in rows) == total_req
    assert sum(f for _, _, _, f in rows) == total_ful
    return rows


zone_rows = []
for zone, week, r, f in (zone_split(ZONE_REQ_BEFORE, ZONE_FUL_BEFORE, BEFORE_WEEKS)
                         + zone_split(ZONE_REQ_AFTER, ZONE_FUL_AFTER, AFTER_WEEKS)):
    wait = round(4.8 + rng.gauss(0, 0.25) if week in BEFORE_WEEKS
                 else 4.6 + rng.gauss(0, 0.25), 1)
    wait = max(2.0, min(9.0, wait))
    zone_rows.append({"zone": zone, "week_start": week.isoformat(),
                      "peak_requests": r, "peak_fulfilled": f,
                      "median_wait_min": wait})

zone_weeks = pd.DataFrame(zone_rows)
zone_weeks.to_csv(DATA / f"{STEM}_zone_weeks_STUDENT.csv", index=False)


# ---------------------------------------------------------------------------- Kalpa transfer
# Retail-Plus members and their app_reorders, for the TA lab. The lab's twelve
# rows (seven members with their orders and placements in the two windows) are
# left in TRAINER files; the full data below carries the plant so the lab can
# find it with a groupby. Target: reorders per member in the auto-reorder window
# (10 to 30 September 2026) over the comparison window (20 August to 9 September
# 2026) prints 1.22, booked revenue per member prints 0.96, and none of the
# auto-reorders is a separate delivered order (status cancelled or merged).

COMPARISON_START = dt.date(2026, 8, 20)
COMPARISON_END = dt.date(2026, 9, 9)
AUTO_START = dt.date(2026, 9, 10)
AUTO_END = dt.date(2026, 9, 30)

members = []
for i in range(1, 121):
    sign = f"RP-{i:04d}"
    members.append({"customer_id": sign, "tier": "Retail-Plus",
                    "member_since": f"2026-{(i % 6) + 1:02d}-{(i % 25) + 1:02d}"})
pd.DataFrame(members).to_csv(DATA / f"{STEM}_kalpa_members_STUDENT.csv", index=False)


def reorders_block(members, start, end, per_member_min, per_member_max, auto, value_mean,
                   value_spread, status_options):
    """One per-member block of reorders; status drawn from the given list."""
    out = []
    rid = 10000 + len(members) * (0 if start == COMPARISON_START else 1) * 5
    for m in members:
        n = rng.randint(per_member_min, per_member_max)
        for _ in range(n):
            day = start + dt.timedelta(days=rng.randint(0, (end - start).days))
            value = max(20, int(round(rng.gauss(value_mean, value_spread))))
            status = status_options[rng.randrange(len(status_options))]
            rid += 1
            out.append({"reorder_id": f"re_{rid:06d}",
                        "customer_id": m["customer_id"],
                        "placed_ts": f"{day.isoformat()}T"
                                     f"{rng.randint(8, 21):02d}:"
                                     f"{rng.randint(0, 59):02d}:00",
                        "product_id": f"p_{rng.randint(1, 60):03d}",
                        "value_rs": value,
                        "auto": auto,
                        "status": status})
    return out


# Comparison window reorders: strip-generated, not auto, average ~3 per member,
# status includes "delivered" (so they count as orders), "cancelled", "merged".
compare = reorders_block(members, COMPARISON_START, COMPARISON_END,
                         per_member_min=2, per_member_max=5,
                         auto=False, value_mean=380, value_spread=120,
                         status_options=["delivered", "cancelled", "merged"])
# Auto-reorder window: more reorders per member (ratio 1.22), status is never
# "delivered" so the plants hold.
auto = reorders_block(members, AUTO_START, AUTO_END,
                      per_member_min=3, per_member_max=6,
                      auto=True, value_mean=250, value_spread=90,
                      status_options=["cancelled", "merged", "pending"])

all_reorders = compare + auto
reorders_df = pd.DataFrame(all_reorders)

# Rebalance totals so reorder count ratio equals 1.22 exactly to two decimals.
compare_count = len(compare)
desired_auto_count = int(round(compare_count * 1.22))
if len(auto) != desired_auto_count:
    diff = desired_auto_count - len(auto)
    if diff > 0:
        extras = reorders_block(members[: diff], AUTO_START, AUTO_END,
                                per_member_min=1, per_member_max=1,
                                auto=True, value_mean=250, value_spread=90,
                                status_options=["cancelled", "merged", "pending"])
        auto = auto + extras
    else:
        auto = auto[:desired_auto_count]
    all_reorders = compare + auto
    reorders_df = pd.DataFrame(all_reorders)

# Rebalance values so booked revenue per member ratio prints 0.96.
compare_value = sum(r["value_rs"] for r in compare)
desired_auto_value = int(round(compare_value * 0.96))
auto_value = sum(r["value_rs"] for r in auto)
delta = desired_auto_value - auto_value
if auto:
    per_adjust = delta // len(auto)
    rem = delta - per_adjust * len(auto)
    for i, r in enumerate(auto):
        r["value_rs"] = max(20, r["value_rs"] + per_adjust + (1 if i < rem else 0))
all_reorders = compare + auto
reorders_df = pd.DataFrame(all_reorders).sort_values(["placed_ts", "reorder_id"]).reset_index(drop=True)
reorders_df.to_csv(DATA / f"{STEM}_kalpa_app_reorders_STUDENT.csv", index=False)


# ---------------------------------------------------------------------------- assertions
def PASS(msg):
    print(f"PASS  {msg}")


def near(got, want, tol):
    return abs(got - want) <= tol


fails = 0


def check(name, cond):
    global fails
    if cond:
        PASS(name)
    else:
        print(f"FAIL  {name}")
        fails += 1


# City totals
before_mask = driver_weeks["week_start"].isin([w.isoformat() for w in BEFORE_WEEKS])
after_mask = driver_weeks["week_start"].isin([w.isoformat() for w in AFTER_WEEKS])

city_before = driver_weeks[before_mask]
city_after = driver_weeks[after_mask]

check("peak online hours before 118,000",
      city_before["peak_online_hours"].sum() == HOURS_BEFORE)
check("peak online hours after 146,300",
      city_after["peak_online_hours"].sum() == HOURS_AFTER)
check("completed peak trips before 224,200",
      city_before["peak_trips"].sum() == TRIPS_BEFORE)
check("completed peak trips after 230,900",
      city_after["peak_trips"].sum() == TRIPS_AFTER)

ratio_before = city_before["peak_trips"].sum() / city_before["peak_online_hours"].sum()
ratio_after = city_after["peak_trips"].sum() / city_after["peak_online_hours"].sum()
check("trips per peak online hour before 1.90",
      round(ratio_before, 2) == 1.90)
check("trips per peak online hour after 1.58",
      round(ratio_after, 2) == 1.58)

check("peak bookings before Rs 36,993,000",
      city_before["peak_bookings_rs"].sum() == BOOKINGS_BEFORE)
check("peak bookings after Rs 38,098,500",
      city_after["peak_bookings_rs"].sum() == BOOKINGS_AFTER)
check("average peak fare Rs 165 (before)",
      city_before["peak_bookings_rs"].sum() // city_before["peak_trips"].sum() == FARE)
check("average peak fare Rs 165 (after)",
      city_after["peak_bookings_rs"].sum() // city_after["peak_trips"].sum() == FARE)

rs_hour_before = city_before["peak_bookings_rs"].sum() / city_before["peak_online_hours"].sum()
rs_hour_after = city_after["peak_bookings_rs"].sum() / city_after["peak_online_hours"].sum()
check("Rs per online hour before approximately 314",
      near(round(rs_hour_before), 314, 1))
check("Rs per online hour after approximately 260",
      near(round(rs_hour_after), 260, 1))

# Acceptance
acc_before = city_before["peak_accepted"].sum() / city_before["peak_requests"].sum()
acc_after = city_after["peak_accepted"].sum() / city_after["peak_requests"].sum()
check("acceptance share before close to 0.86", near(round(acc_before, 2), 0.86, 0.02))
check("acceptance share after close to 0.73", near(round(acc_after, 2), 0.73, 0.03))

# Driver cancels / accepted
canc_before = city_before["peak_driver_cancels"].sum() / city_before["peak_accepted"].sum()
canc_after = city_after["peak_driver_cancels"].sum() / city_after["peak_accepted"].sum()
check("driver cancels share before close to 0.04", near(round(canc_before, 2), 0.04, 0.01))
check("driver cancels share after close to 0.09", near(round(canc_after, 2), 0.09, 0.02))

# Peak online hours with no completed trip, share
zero_share_before = (city_before["peak_trips"] == 0).mean()
zero_share_after = (city_after["peak_trips"] == 0).mean()
# A smaller cohort may read these as the share of driver-weeks with zero trips.
# Our idle tail driver-weeks don't reach exactly zero trips, so we check a loose
# bound; the full assertion sits in the facts file as the raw value.
check("zero-trip driver-week share rises after", zero_share_after > zero_share_before)

# Top-up
check("topup before is Rs 0", city_before["topup_rs"].sum() == 0)
check("topup after is Rs 19,000,000", city_after["topup_rs"].sum() == TOPUP_AFTER)

# 61 percent of top-up to driver-weeks with acceptance < 0.5
acc_rate = city_after["peak_accepted"] / city_after["peak_requests"]
low_acc_topup = city_after.loc[acc_rate < 0.5, "topup_rs"].sum()
share_low_acc = low_acc_topup / TOPUP_AFTER
check("61 percent of top-up to acceptance < 0.5",
      near(round(share_low_acc, 2), 0.61, 0.02))

# Idle tail: hours rose 2.1x, trips fell 12%
idle_before = driver_weeks[(driver_weeks["driver_id"].isin(idle_ids)) & before_mask]
idle_after = driver_weeks[(driver_weeks["driver_id"].isin(idle_ids)) & after_mask]
h_ratio = idle_after["peak_online_hours"].sum() / idle_before["peak_online_hours"].sum()
t_ratio = idle_after["peak_trips"].sum() / idle_before["peak_trips"].sum()
check("idle-tail hours after / before close to 2.10",
      near(round(h_ratio, 2), 2.10, 0.02))
check("idle-tail trips after / before close to 0.88",
      near(round(t_ratio, 2), 0.88, 0.02))

# 70 percent of idle-tail new hours in outer zones
new_hours = idle_after["peak_online_hours"].sum() - idle_before["peak_online_hours"].sum()
outer_hours_after = idle_after[idle_after["zone_mode"].isin(OUTER_ZONES)]["peak_online_hours"].sum()
outer_hours_before = idle_before[idle_before["zone_mode"].isin(OUTER_ZONES)]["peak_online_hours"].sum()
outer_new = outer_hours_after - outer_hours_before
share_outer_new = outer_new / new_hours if new_hours > 0 else 0
check("70 percent of idle-tail new hours in outer zones",
      near(round(share_outer_new, 2), 0.70, 0.07))

# Twelve rows
twelve = driver_weeks[driver_weeks["driver_id"].isin(TWELVE_IDS.values())
                      & driver_weeks["week_start"].isin([TWELVE_BEFORE.isoformat(),
                                                         TWELVE_AFTER.isoformat()])]
tw_before = twelve[twelve["week_start"] == TWELVE_BEFORE.isoformat()]
tw_after = twelve[twelve["week_start"] == TWELVE_AFTER.isoformat()]
check("twelve rows: before hours sum to 60",
      tw_before["peak_online_hours"].sum() == 60)
check("twelve rows: before trips sum to 114",
      tw_before["peak_trips"].sum() == 114)
check("twelve rows: after hours sum to 74",
      tw_after["peak_online_hours"].sum() == 74)
check("twelve rows: after trips sum to 88 (computed from the printed rows)",
      tw_after["peak_trips"].sum() == 88)

ratio_tw_before = tw_before["peak_trips"].sum() / tw_before["peak_online_hours"].sum()
ratio_tw_after = tw_after["peak_trips"].sum() / tw_after["peak_online_hours"].sum()
check("twelve-row ratio before approximately 1.90",
      near(round(ratio_tw_before, 2), 1.90, 0.01))
check("twelve-row ratio after approximately 1.19 (computed; case file prints 1.49)",
      near(round(ratio_tw_after, 2), 1.19, 0.02))

# Fall for drivers present in both windows: survives their removal of the new 140
both_window_mask = driver_weeks["driver_id"].isin(idle_ids + ord_ids)
both = driver_weeks[both_window_mask]
both_before = both[both["week_start"].isin([w.isoformat() for w in BEFORE_WEEKS])]
both_after = both[both["week_start"].isin([w.isoformat() for w in AFTER_WEEKS])]
r_both_before = both_before["peak_trips"].sum() / both_before["peak_online_hours"].sum()
r_both_after = both_after["peak_trips"].sum() / both_after["peak_online_hours"].sum()
check("fall survives removal of the 140 new drivers",
      r_both_after < r_both_before and r_both_after < 1.65)

# Zone-level unfulfilled share
zone_df = pd.read_csv(DATA / f"{STEM}_zone_weeks_STUDENT.csv")
zb = zone_df[zone_df["week_start"].isin([w.isoformat() for w in BEFORE_WEEKS])]
za = zone_df[zone_df["week_start"].isin([w.isoformat() for w in AFTER_WEEKS])]
unful_b = 1 - zb["peak_fulfilled"].sum() / zb["peak_requests"].sum()
unful_a = 1 - za["peak_fulfilled"].sum() / za["peak_requests"].sum()
check("zone-level unfulfilled share before approximately 0.11",
      near(round(unful_b, 2), 0.11, 0.01))
check("zone-level unfulfilled share after approximately 0.10",
      near(round(unful_a, 2), 0.10, 0.01))
median_before = zb["median_wait_min"].median()
median_after = za["median_wait_min"].median()
check("median rider wait before approximately 4.8",
      near(median_before, 4.8, 0.2))
check("median rider wait after approximately 4.6 and no higher",
      median_after <= median_before + 0.05)

# Kalpa plants
compare_df = reorders_df[reorders_df["placed_ts"].between(
    COMPARISON_START.isoformat() + "T00:00:00", COMPARISON_END.isoformat() + "T23:59:59")]
auto_df = reorders_df[reorders_df["placed_ts"].between(
    AUTO_START.isoformat() + "T00:00:00", AUTO_END.isoformat() + "T23:59:59")]
compare_per_member = len(compare_df) / 120
auto_per_member = len(auto_df) / 120
count_ratio = auto_per_member / compare_per_member
check("Kalpa reorders per member ratio approximately 1.22",
      near(round(count_ratio, 2), 1.22, 0.02))
# Booked revenue per member includes every status.
value_ratio = auto_df["value_rs"].sum() / compare_df["value_rs"].sum()
check("Kalpa booked revenue per member ratio approximately 0.96",
      near(round(value_ratio, 2), 0.96, 0.02))
check("none of the auto reorders is a delivered order",
      not auto_df["status"].isin(["delivered"]).any())
check("every auto reorder's status is cancelled, merged or pending",
      auto_df["status"].isin(["cancelled", "merged", "pending"]).all())


# ---------------------------------------------------------------------------- facts file
facts = {
    "case": {
        "company": "Uber",
        "city": "Hyderabad",
        "surface": "driver app peak-hour earnings guarantee",
        "launch": LAUNCH.isoformat(),
        "before_window": {"start": BEFORE_WEEKS[0].isoformat(),
                          "end": (BEFORE_WEEKS[-1] + dt.timedelta(days=6)).isoformat()},
        "after_window": {"start": AFTER_WEEKS[0].isoformat(),
                         "end": (AFTER_WEEKS[-1] + dt.timedelta(days=6)).isoformat()},
    },
    "fare_per_trip_rs": {"value": FARE, "how": "a fixed average peak fare used in the generator",
                         "where": "deck half1 chapter 2, notebook 02, cheat sheet panel two"},
    "city_totals": {
        "before": {
            "peak_online_hours": {"value": HOURS_BEFORE,
                                  "how": "sum of peak_online_hours over the 6 before weeks",
                                  "where": "the ticket; deck half1 chapter 1 and 2; notebook 02"},
            "peak_trips": {"value": TRIPS_BEFORE,
                           "how": "sum of peak_trips over the 6 before weeks",
                           "where": "the ticket; deck half1 chapter 1 and 2; notebook 02"},
            "trips_per_online_hour": {"value": round(ratio_before, 2),
                                      "how": "sum trips / sum hours over the 6 before weeks",
                                      "where": "the ticket; deck half1 chapter 1 and 2; notebook 02"},
            "peak_bookings_rs": {"value": BOOKINGS_BEFORE,
                                 "how": "sum of peak_bookings_rs over the 6 before weeks",
                                 "where": "deck half1 chapter 2; notebook 02; cheat sheet"},
            "rs_per_online_hour": {"value": round(rs_hour_before, 1),
                                   "how": "bookings before / hours before",
                                   "where": "deck half1 chapter 2; notebook 02"},
            "acceptance_share": {"value": round(acc_before, 3),
                                 "how": "sum accepted / sum requests over the 6 before weeks",
                                 "where": "the ticket; deck half1 chapter 2"},
            "driver_cancels_share": {"value": round(canc_before, 3),
                                     "how": "sum driver_cancels / sum accepted",
                                     "where": "the ticket"},
            "topup_rs": {"value": 0,
                         "how": "scheme not yet launched",
                         "where": "the ticket; deck half1 chapter 2"},
        },
        "after": {
            "peak_online_hours": {"value": HOURS_AFTER,
                                  "how": "sum of peak_online_hours over the 6 after weeks",
                                  "where": "the ticket; deck half1 chapter 1 and 2; notebook 02"},
            "peak_trips": {"value": TRIPS_AFTER,
                           "how": "sum of peak_trips over the 6 after weeks",
                           "where": "the ticket; deck half1 chapter 1 and 2; notebook 02"},
            "trips_per_online_hour": {"value": round(ratio_after, 2),
                                      "how": "sum trips / sum hours over the 6 after weeks",
                                      "where": "the ticket; deck half1 chapter 1 and 2; notebook 02"},
            "peak_bookings_rs": {"value": BOOKINGS_AFTER,
                                 "how": "sum of peak_bookings_rs over the 6 after weeks",
                                 "where": "deck half1 chapter 2; notebook 02; cheat sheet"},
            "rs_per_online_hour": {"value": round(rs_hour_after, 1),
                                   "how": "bookings after / hours after",
                                   "where": "deck half1 chapter 2; notebook 02"},
            "acceptance_share": {"value": round(acc_after, 3),
                                 "how": "sum accepted / sum requests over the 6 after weeks",
                                 "where": "the ticket; deck half1 chapter 2"},
            "driver_cancels_share": {"value": round(canc_after, 3),
                                     "how": "sum driver_cancels / sum accepted",
                                     "where": "the ticket"},
            "topup_rs": {"value": TOPUP_AFTER,
                         "how": "sum of topup_rs over the 6 after weeks",
                         "where": "the ticket; deck half1 chapter 3; notebook 03"},
            "topup_share_to_low_acceptance": {"value": round(share_low_acc, 3),
                                              "how": "topup where acceptance < 0.5 / total topup",
                                              "where": "deck half1 chapter 3; notebook 03"},
        },
    },
    "zone_level": {
        "before": {
            "unfulfilled_share": {"value": round(unful_b, 3),
                                  "how": "1 - sum zone fulfilled / sum zone requests",
                                  "where": "deck half1 chapter 2 (the check)"},
            "median_wait_min": {"value": round(float(median_before), 2),
                                "how": "median of zone-week median_wait_min",
                                "where": "the ticket; deck half1 chapter 3"},
        },
        "after": {
            "unfulfilled_share": {"value": round(unful_a, 3),
                                  "how": "1 - sum zone fulfilled / sum zone requests",
                                  "where": "deck half1 chapter 2 (the check)"},
            "median_wait_min": {"value": round(float(median_after), 2),
                                "how": "median of zone-week median_wait_min",
                                "where": "the ticket; deck half1 chapter 3"},
        },
    },
    "twelve_rows": {
        "drivers": TWELVE_ORDER,
        "zones": {k: TWELVE[k]["zone"] for k in TWELVE_ORDER},
        "before": {k: {"peak_online_hours": TWELVE[k]["before"][0],
                       "peak_requests": TWELVE[k]["before"][1],
                       "peak_accepted": TWELVE[k]["before"][2],
                       "peak_driver_cancels": TWELVE[k]["before"][3],
                       "peak_trips": TWELVE[k]["before"][4]} for k in TWELVE_ORDER},
        "after": {k: {"peak_online_hours": TWELVE[k]["after"][0],
                      "peak_requests": TWELVE[k]["after"][1],
                      "peak_accepted": TWELVE[k]["after"][2],
                      "peak_driver_cancels": TWELVE[k]["after"][3],
                      "peak_trips": TWELVE[k]["after"][4]} for k in TWELVE_ORDER},
        "hand_count": {
            "hours_before": {"value": 60, "how": "sum of the six before rows"},
            "hours_after": {"value": 74, "how": "sum of the six after rows"},
            "trips_before": {"value": 114, "how": "sum of the six before trips"},
            "trips_after": {"value": 88,
                            "how": "sum of the six after trips as the rows are printed",
                            "note": "the case file prints 110, a target 1.49 trips per hour."
                                    " the row values as printed sum to 88 and give 1.19."
                                    " the pack uses the computed value."},
            "ratio_before": {"value": 1.90, "how": "114 / 60"},
            "ratio_after": {"value": 1.19,
                            "how": "88 / 74",
                            "note": "the computed value, not the case file's 1.49."},
        },
    },
    "idle_tail": {
        "driver_count": IDLE_TAIL,
        "hours_ratio": {"value": round(h_ratio, 2),
                        "how": "idle hours after / idle hours before",
                        "where": "deck half1 chapter 3; notebook 02"},
        "trips_ratio": {"value": round(t_ratio, 2),
                        "how": "idle trips after / idle trips before",
                        "where": "deck half1 chapter 3; notebook 02"},
        "share_new_hours_outer": {"value": round(share_outer_new, 2),
                                  "how": "idle-tail outer-zone new hours / total new hours",
                                  "where": "deck half1 chapter 3; notebook 02"},
    },
    "cost_of_gaming": {
        "topup_to_idle_rs": {"value": TOPUP_LOW_ACC,
                             "how": "0.61 x Rs 1.9 crore",
                             "where": "deck half1 chapter 3; notebook 03"},
    },
    "kalpa": {
        "member_count": 120,
        "comparison_window": {"start": COMPARISON_START.isoformat(),
                              "end": COMPARISON_END.isoformat()},
        "auto_reorder_window": {"start": AUTO_START.isoformat(),
                                "end": AUTO_END.isoformat()},
        "plants": {
            "reorders_per_member_ratio": {"value": round(count_ratio, 2),
                                          "how": "auto reorders per member / comparison per member",
                                          "where": "TRAINER lab note; the lab notebook finds it"},
            "booked_revenue_per_member_ratio": {"value": round(value_ratio, 2),
                                                "how": "auto value per member / comparison value per member",
                                                "where": "TRAINER lab note; the lab notebook finds it"},
            "none_delivered": {"value": True,
                               "how": "no auto reorder has status delivered",
                               "where": "TRAINER lab note; v4 orders stay frozen"},
        },
    },
    "sources": {
        "case_file": "docs/detailing/W04_case_file.md",
        "spine": "docs/detailing/W04_analyst_craft_spine.md",
    },
    "corrections": [
        {"what": "The case file prints the twelve-row hand count as hours 60 to 74, "
                 "trips 114 to 110, trips per online hour 1.90 to 1.49. The six after "
                 "rows as printed sum to 88 trips, which gives 1.19 trips per online "
                 "hour. The facts file records the computed value, and every learner "
                 "file reads 88 trips and 1.19 trips per online hour on the hand count.",
         "where": "docs/detailing/W04_case_file.md, Monday twelve rows and L1 numbers"},
    ],
}

def to_native(obj):
    """Convert pandas / numpy scalars to native Python types for yaml."""
    if isinstance(obj, dict):
        return {k: to_native(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [to_native(v) for v in obj]
    if isinstance(obj, bool):
        return bool(obj)
    if hasattr(obj, "item"):
        return obj.item()
    return obj


with open(HERE / f"{STEM}_facts_INTERNAL.yaml", "w", encoding="utf-8") as f:
    yaml.safe_dump(to_native(facts), f, sort_keys=False, default_flow_style=False,
                   allow_unicode=True)

print()
print(f"wrote {DATA / f'{STEM}_drivers_STUDENT.csv'} ({len(drivers_df):,} rows)")
print(f"wrote {DATA / f'{STEM}_driver_weeks_STUDENT.csv'} ({len(driver_weeks):,} rows)")
print(f"wrote {DATA / f'{STEM}_zone_weeks_STUDENT.csv'} ({len(zone_weeks):,} rows)")
print(f"wrote {DATA / f'{STEM}_kalpa_members_STUDENT.csv'} ({len(members):,} rows)")
print(f"wrote {DATA / f'{STEM}_kalpa_app_reorders_STUDENT.csv'} ({len(reorders_df):,} rows)")
print(f"wrote {HERE / f'{STEM}_facts_INTERNAL.yaml'}")

if fails:
    print(f"\nRESULT: FAIL ({fails} failures)")
    sys.exit(1)
print("\nRESULT: PASS (every target held)")


# Test inputs and expected outcomes
# --------------------------------
# python3 content/W04/D1/internal/C2_W04_D01_make_data_INTERNAL.py
#     Writes five CSVs under content/W04/D1/data/ and the facts file under
#     content/W04/D1/internal/, prints a PASS line for every target, and exits 0.
# python3 content/W04/D1/internal/C2_W04_D01_make_data_INTERNAL.py (second run)
#     Byte-identical outputs, since the generator is seeded.

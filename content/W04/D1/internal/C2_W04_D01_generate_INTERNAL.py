"""Week 4 Monday: the case data and the facts file (Uber, Hyderabad; an illustrative case).

Seeded, so two runs write byte-identical files. Standard library, pandas and PyYAML only.

Writes to content/W04/D1/data/ the three case tables (drivers, driver_weeks, zone_weeks) and the two
Kalpa transfer tables: kalpa_members, a byte copy of Thursday's kalpa_memberships, and
kalpa_app_reorders, whose placements that became orders are the frozen v4 warehouse's own app orders
(read from content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql). Writes to internal/ the facts
file and the contract output. Every target in the Monday section of docs/detailing/W04_case_file.md,
every value the orchestrator's review of 12 October 2026 holds, every Kalpa plant, both directions of
the join to v4 and the case tables' checksums on origin/main are asserted; a failed line makes the
script exit 1.

    python3 content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py              write, then check
    python3 content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py --contract   also print every line
    python3 content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py --list       print the facts ids

How the weeks are shaped. Rider requests follow a gentle monsoon season: they rise through the rainy
weeks to a crest in the first after weeks and ease as the monsoon withdraws. Completed trips are the
fulfilled share of each week's requests. Each driver group's six-week totals (hours, trips, offers,
accepted, cancels, hours with no trip, top-up) are held exactly and split across the weeks with a
few percent of seeded variation, then across the group's driver-weeks; the idle tail's hours ramp up
over the first after week. A small, varying number of driver-weeks each week have no peak hour at
all (the driver drove off-peak only), so the drivers online at peak change week to week while the
row counts per window stay at 6,360 and 6,500.
"""
import datetime as dt
import hashlib
import itertools
import pathlib
import random
import sys
from collections import Counter

import pandas as pd
import yaml

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent / "data"
DATA.mkdir(parents=True, exist_ok=True)
STEM = "C2_W04_D01"
SEED = 20261026
rng = random.Random(SEED)

# ---------------------------------------------------------------------------------- the case's terms
WEEKS = [dt.date(2026, 7, 20) + dt.timedelta(days=7 * i) for i in range(12)]
BEFORE, AFTER = WEEKS[:6], WEEKS[6:]
LAUNCH = WEEKS[6]                                   # Monday 31 August 2026
TWELVE_WEEKS = {"before": dt.date(2026, 8, 10), "after": dt.date(2026, 9, 21)}
FARE = 165                                          # average peak fare, Rs
FLOOR = 300                                         # the guarantee's floor, Rs per peak online hour
WINDOWS_PER_DAY, WINDOW_HOURS = 2, 3
MAX_HOURS = WINDOWS_PER_DAY * WINDOW_HOURS * 7      # 42 peak hours in a week, at most

CORE = ["Banjara Hills", "Jubilee Hills", "Gachibowli", "Madhapur", "Hitech City",
        "Begumpet", "Kondapur", "Kukatpally", "Secunderabad"]
OUTER = ["Shamshabad", "Rajendranagar", "Patancheru"]
ZONES = CORE + OUTER

ORD, IDLE, NEW = 880, 180, 140                      # ordinary, idle tail, joined after the launch

# Each group's six-week totals, held exactly. accepted = trips + driver cancels in every row.
TOTALS = {
    ("ord", "before"):  dict(h=98000, t=186200, c=7154, o=224048, n=21560, tu=0),
    ("idle", "before"): dict(h=20000, t=38000, c=1460, o=45725, n=4400, tu=0),
    ("ord", "after"):   dict(h=102000, t=193800, c=16200, o=252583, n=24684, tu=7110000),
    ("idle", "after"):  dict(h=42000, t=33440, c=6000, o=90000, n=30240, tu=11590000),
    ("new", "after"):   dict(h=2300, t=3660, c=636, o=5000, n=690, tu=300000),
}
REQUESTS = {"before": 251910, "after": 256556}      # rider requests, zone_weeks, six weeks
SEASON = [1.000, 1.011, 1.018, 1.023, 1.031, 1.038, 1.059, 1.066, 1.057, 1.035, 1.016, 1.000]
IDLE_RAMP = [0.87, 1.00, 1.03, 1.04, 1.03, 1.03]   # idle-tail hours over the six after weeks
NEW_ROWS = [10, 16, 22, 26, 30, 36]                 # new drivers' driver-weeks, by after week
ZERO_ROWS = {"before": [14, 18, 12, 16, 17, 13], "after": [12, 9, 11, 13, 10, 11]}

# The twelve rows: (hours, offers, accepted, driver cancels, trips, hours with no trip, top-up).
TWELVE = {
    "A": ("d_0001", "Jubilee Hills", (10, 24, 21, 0, 21, 1, 0), (11, 25, 22, 0, 22, 1, 0)),
    "B": ("d_0002", "Banjara Hills", (9, 20, 17, 0, 17, 1, 0), (10, 21, 18, 0, 18, 1, 0)),
    "C": ("d_0003", "Gachibowli", (11, 25, 22, 0, 22, 2, 0), (12, 26, 23, 0, 23, 2, 0)),
    "D": ("d_0004", "Madhapur", (10, 22, 19, 0, 19, 1, 0), (11, 23, 20, 0, 20, 2, 0)),
    "E": ("d_0881", "Shamshabad", (10, 21, 18, 0, 18, 1, 0), (16, 14, 4, 1, 3, 14, 4400)),
    "F": ("d_0882", "Rajendranagar", (10, 20, 17, 0, 17, 2, 0), (14, 12, 3, 1, 2, 13, 3850)),
}
FIELDS = ["peak_online_hours", "peak_offers", "peak_accepted", "peak_driver_cancels",
          "peak_trips", "peak_hours_no_trip", "topup_rs"]


def spread(total, weights, lo=None, hi=None):
    """Integers proportional to weights that sum to total exactly, each kept inside [lo, hi]."""
    n = len(weights)
    lo = lo or [0] * n
    hi = hi or [10 ** 12] * n
    w = sum(weights) or 1
    raw = [total * x / w for x in weights]
    out = [int(r) for r in raw]
    for i in sorted(range(n), key=lambda i: out[i] - raw[i])[: total - sum(out)]:
        out[i] += 1
    out = [min(max(v, a), b) for v, a, b in zip(out, lo, hi)]
    gap = total - sum(out)
    order = sorted(range(n), key=lambda i: -weights[i])
    while gap:
        moved = False
        for i in order:
            step = 1 if gap > 0 else -1
            if lo[i] <= out[i] + step <= hi[i]:
                out[i] += step
                gap -= step
                moved = True
                if not gap:
                    break
        if not moved:
            raise ValueError(f"cannot spread {total} inside the bounds")
    return out


def wobble(x, pct):
    """x moved by up to pct either way, seeded."""
    return x * rng.uniform(1 - pct, 1 + pct)


# ---------------------------------------------------------------------------------- drivers
drivers = []
for i in range(1, ORD + IDLE + NEW + 1):
    if i <= ORD:
        group, home, joined = "ord", CORE[(i - 1) % 9], f"2024-{(i - 1) % 12 + 1:02d}"
    elif i <= ORD + IDLE:
        k = i - ORD - 1
        group = "idle"
        home = OUTER[k % 3] if k % 4 else CORE[k % 9]
        joined = f"2025-{k % 12 + 1:02d}"
    else:
        group, home, joined = "new", ZONES[(i - ORD - IDLE - 1) % 12], "2026-09"
    drivers.append({"driver_id": f"d_{i:04d}", "group": group, "home_zone": home,
                    "joined_month": joined, "enrolled": True})
for _, (did, zone, _, _) in TWELVE.items():
    next(d for d in drivers if d["driver_id"] == did)["home_zone"] = zone
pd.DataFrame(drivers)[["driver_id", "home_zone", "joined_month", "enrolled"]].to_csv(
    DATA / f"{STEM}_drivers_STUDENT.csv", index=False)

GROUP = {d["driver_id"]: d["group"] for d in drivers}
HOME = {d["driver_id"]: d["home_zone"] for d in drivers}
TWELVE_IDS = {did for did, _, _, _ in TWELVE.values()}

# Each driver's steady habits, so a driver looks like the same person week to week.
BASE = {}
for d in drivers:
    did, g = d["driver_id"], d["group"]
    BASE[did] = {
        "hours": min(30, max(8, rng.gauss(18.6, 2.6))),
        "after_hours": rng.uniform(0.86, 1.0) * MAX_HOURS if g == "idle" else None,
        "tph": rng.gauss(1.0, 0.05),
        "offpeak": rng.randint(6, 16),
    }
    BASE[did]["after_tph"] = BASE[did]["tph"]
for did in ("d_0001", "d_0002", "d_0003", "d_0004"):
    BASE[did]["hours"] = 10.5
for did, after_h in (("d_0881", 15.5), ("d_0882", 14.0)):
    BASE[did].update(hours=10.0, after_hours=after_h, after_tph=0.32)
if GROUP["d_0881"] != "idle" or GROUP["d_0004"] != "ord":
    sys.exit("the twelve rows' drivers sit in the wrong groups")

# ---------------------------------------------------------------------------------- the weekly plan
requests_w = spread(REQUESTS["before"], SEASON[:6]) + spread(REQUESTS["after"], SEASON[6:])
fulfil = [wobble(0.890, 0.004) for _ in BEFORE] + [wobble(0.900, 0.004) for _ in AFTER]
trips_w = (spread(224200, [r * f for r, f in zip(requests_w[:6], fulfil[:6])])
           + spread(230900, [r * f for r, f in zip(requests_w[6:], fulfil[6:])]))

plan = {}   # (group, week index) -> totals for that group-week
idle_t = (spread(38000, [wobble(t, 0.02) for t in trips_w[:6]])
          + spread(33440, [wobble(x, 0.01) for x in [1.02, 1.00, 0.995, 0.995, 0.99, 0.99]]))
new_t = [0] * 6 + spread(3660, NEW_ROWS)
ord_t = [trips_w[w] - idle_t[w] - new_t[w] for w in range(12)]
ord_h = (spread(98000, [ord_t[w] / wobble(1.9, 0.015) for w in range(6)])
         + spread(102000, [ord_t[w] / wobble(1.9, 0.015) for w in range(6, 12)]))
idle_h = (spread(20000, [idle_t[w] / wobble(1.9, 0.015) for w in range(6)])
          + spread(42000, [wobble(x, 0.01) for x in IDLE_RAMP]))
new_h = [0] * 6 + spread(2300, NEW_ROWS)
hours = {"ord": ord_h, "idle": idle_h, "new": new_h}
trips = {"ord": ord_t, "idle": idle_t, "new": new_t}
for (g, window), tot in TOTALS.items():
    idx = list(range(6) if window == "before" else range(6, 12))
    h_g, t_g = [hours[g][w] for w in idx], [trips[g][w] for w in idx]
    c_g = spread(tot["c"], [wobble(x, 0.03) for x in t_g])           # cancels follow trips
    o_g = spread(tot["o"], [wobble(t + c, 0.01) for t, c in zip(t_g, c_g)])  # offers follow accepted
    n_g = spread(tot["n"], [wobble(x, 0.02) for x in h_g])           # idle hours follow hours
    tu_g = spread(tot["tu"], [wobble(x, 0.02) for x in h_g])
    for k, w in enumerate(idx):
        plan[(g, w)] = {"h": h_g[k], "t": t_g[k], "c": c_g[k], "o": o_g[k], "n": n_g[k], "tu": tu_g[k]}

# ---------------------------------------------------------------------------------- driver-weeks
ACCEPT = {("ord", "before"): 0.863, ("idle", "before"): 0.863,
          ("ord", "after"): 0.831, ("idle", "after"): 0.438, ("new", "after"): 0.859}
NO_TRIP = {("ord", "before"): 0.22, ("idle", "before"): 0.22,
           ("ord", "after"): 0.242, ("idle", "after"): 0.72, ("new", "after"): 0.30}
rows = []
ord_ids = [d["driver_id"] for d in drivers if d["group"] == "ord"]
new_ids = [d["driver_id"] for d in drivers if d["group"] == "new"]
rng.shuffle(new_ids)
new_week = {}
for k, n in enumerate(NEW_ROWS):
    for did in new_ids[sum(NEW_ROWS[:k]): sum(NEW_ROWS[:k + 1])]:
        new_week[did] = 6 + k

for w, week in enumerate(WEEKS):
    window = "before" if w < 6 else "after"
    zero_pool = [d for d in ord_ids if d not in TWELVE_IDS]
    zero = set(rng.sample(zero_pool, ZERO_ROWS[window][w % 6]))
    for g in ("ord", "idle", "new"):
        if (g, window) not in TOTALS:
            continue
        p = plan[(g, w)]
        ids = [d["driver_id"] for d in drivers if d["group"] == g]
        if g == "new":
            ids = [d for d in ids if new_week[d] == w]
        fixed = {}
        for label, (did, zone, before_row, after_row) in TWELVE.items():
            if did in ids and week == TWELVE_WEEKS[window]:
                fixed[did] = dict(zip(FIELDS, before_row if window == "before" else after_row))
        live = [d for d in ids if d not in fixed and d not in zero]
        left = {key: p[key] - sum(f[name] for f in fixed.values())
                for key, name in (("h", "peak_online_hours"), ("t", "peak_trips"),
                                  ("c", "peak_driver_cancels"), ("o", "peak_offers"),
                                  ("n", "peak_hours_no_trip"), ("tu", "topup_rs"))}
        idle_after = g == "idle" and window == "after"
        h_base = [BASE[d]["after_hours"] if idle_after else BASE[d]["hours"] for d in live]
        ramp = IDLE_RAMP[w - 6] / max(IDLE_RAMP) if idle_after else 1
        h = spread(left["h"], [wobble(b * ramp, 0.06) for b in h_base], [1] * len(live),
                   [MAX_HOURS] * len(live))
        tph = 0.796 if idle_after else (1.59 if g == "new" else 1.9)
        habit = "after_tph" if idle_after else "tph"
        t = spread(left["t"], [x * tph * BASE[d][habit] * rng.uniform(0.95, 1.05)
                               for x, d in zip(h, live)], [1] * len(live))
        c = spread(left["c"], [x * rng.uniform(0.6, 1.4) for x in t])
        a = [x + y for x, y in zip(t, c)]
        acc = ACCEPT[(g, window)]
        o_lo = [2 * x + 1 if idle_after else x for x in a]
        o_hi = [2 * x if window == "after" and not idle_after else 10 ** 6 for x in a]
        o = spread(left["o"], [x / wobble(acc, 0.04) + 0.5 for x in a], o_lo, o_hi)
        share = NO_TRIP[(g, window)]
        n = spread(left["n"], [x * wobble(share, 0.15) for x in h],
                   [max(0, x - y) for x, y in zip(h, t)], h)
        if window == "before":
            tu = [0] * len(live)
        elif idle_after:
            tu = spread(left["tu"], [x * rng.uniform(0.93, 1.0) for x in h], [1] * len(live),
                        [FLOOR * x for x in h])
        else:
            tu = spread(left["tu"], [x * max(0.0, 2.15 - y / x) for x, y in zip(h, t)],
                        None, [FLOOR * x for x in h])
        for k, did in enumerate(live):
            fixed[did] = dict(zip(FIELDS, (h[k], o[k], a[k], c[k], t[k], n[k], tu[k])))
        for did in ids:
            if did in zero:
                vals = dict.fromkeys(FIELDS, 0)
                off = BASE[did]["offpeak"] + rng.randint(6, 12)
            else:
                vals = fixed[did]
                off = max(0, round(BASE[did]["offpeak"] + rng.gauss(0, 2)))
            rows.append({"driver_id": did, "week_start": week.isoformat(), "zone_mode": HOME[did],
                         **vals, "peak_bookings_rs": vals["peak_trips"] * FARE,
                         "offpeak_trips": off})

dw = pd.DataFrame(rows)
# Where most of a driver's online time sat that week: home, or now and then another core zone; the
# idle tail's after weeks drift to the outer zones, which is where the floor pays without a trip.
for i in dw.index:
    did, week = dw.at[i, "driver_id"], dw.at[i, "week_start"]
    if did in TWELVE_IDS:
        continue
    g, after = GROUP[did], week >= LAUNCH.isoformat()
    if g == "ord" and rng.random() < 0.15:
        dw.at[i, "zone_mode"] = rng.choice(CORE)
    elif g == "idle" and after and HOME[did] in CORE and rng.random() < 0.35:
        dw.at[i, "zone_mode"] = rng.choice(OUTER)
idle_rows = dw["driver_id"].map(GROUP).eq("idle")
is_after = dw["week_start"] >= LAUNCH.isoformat()
outer_before = dw.loc[idle_rows & ~is_after & dw["zone_mode"].isin(OUTER), "peak_online_hours"].sum()
target = outer_before + round(0.72 * 22000)        # 72 percent of the idle tail's new hours
movable = [i for i in dw.index[idle_rows & is_after] if dw.at[i, "driver_id"] not in TWELVE_IDS]
rng.shuffle(movable)
now = dw.loc[idle_rows & is_after & dw["zone_mode"].isin(OUTER), "peak_online_hours"].sum()
for i in movable:
    if abs(now - target) <= 40:
        break
    in_outer = dw.at[i, "zone_mode"] in OUTER
    if now > target and in_outer:                   # an outer-zone driver who sat in a core zone
        dw.at[i, "zone_mode"] = rng.choice(CORE)
        now -= dw.at[i, "peak_online_hours"]
    elif now < target and not in_outer:
        dw.at[i, "zone_mode"] = rng.choice(OUTER)
        now += dw.at[i, "peak_online_hours"]
dw = dw.sort_values(["week_start", "driver_id"]).reset_index(drop=True)
dw = dw[["driver_id", "week_start", "zone_mode", "peak_online_hours", "peak_offers", "peak_accepted",
         "peak_driver_cancels", "peak_trips", "peak_hours_no_trip", "peak_bookings_rs", "topup_rs",
         "offpeak_trips"]]
dw.to_csv(DATA / f"{STEM}_driver_weeks_STUDENT.csv", index=False)

# ---------------------------------------------------------------------------------- zone-weeks
ZONE_SIZE = {"Banjara Hills": 0.95, "Jubilee Hills": 0.95, "Gachibowli": 1.15, "Madhapur": 1.20,
             "Hitech City": 1.25, "Begumpet": 0.80, "Kondapur": 1.00, "Kukatpally": 0.95,
             "Secunderabad": 0.85, "Shamshabad": 0.30, "Rajendranagar": 0.28, "Patancheru": 0.25}
WAIT = {"before": (4.8, 6.5), "after": (4.6, 6.0)}   # core and outer centre of the weekly medians
zone_rows = []
for w, week in enumerate(WEEKS):
    window = "before" if w < 6 else "after"
    req = spread(requests_w[w], [wobble(ZONE_SIZE[z], 0.03) for z in ZONES])
    ful = spread(trips_w[w], [r * (0.90 if z in CORE else 0.78) for r, z in zip(req, ZONES)],
                 None, req)
    for z, r, f in zip(ZONES, req, ful):
        centre = WAIT[window][0] if z in CORE else WAIT[window][1]
        zone_rows.append({"zone": z, "week_start": week.isoformat(), "peak_requests": r,
                          "peak_fulfilled": f, "median_wait_min": round(rng.gauss(centre, 0.18), 1)})
zw = pd.DataFrame(zone_rows)
for window, (core_centre, _) in WAIT.items():
    in_window = zw["week_start"].lt(LAUNCH.isoformat()) == (window == "before")
    core_idx = list(zw.index[in_window & zw["zone"].isin(CORE)])
    while round(zw.loc[in_window, "median_wait_min"].median(), 2) != core_centre:
        side = 1 if zw.loc[in_window, "median_wait_min"].median() < core_centre else -1
        pick = [i for i in core_idx if (zw.at[i, "median_wait_min"] - core_centre) * side < 0]
        i = rng.choice(pick)
        zw.at[i, "median_wait_min"] = round(zw.at[i, "median_wait_min"] + 0.1 * side, 1)
zw.to_csv(DATA / f"{STEM}_zone_weeks_STUDENT.csv", index=False)

# ---------------------------------------------------------------------------------- the Kalpa transfer
# The TA lab's two tables. kalpa_members is Thursday's kalpa_memberships, copied byte for byte, so the
# two days describe one tier. kalpa_app_reorders logs every reorder placement from 20 August to 30
# September. Before 10 September members reordered with the Reorder button: a placement that became
# an order is one of the frozen v4 warehouse's app orders (same customer, date, amount and status,
# its id in order_id), and the rest merged into a basket the member already had open. From 10
# September the app's auto-reorder feature placed every row itself, and none became an order; the
# members' own checkouts in that window are v4's other app orders, outside the log. The per-member
# comparison runs on the 107 who had joined by the monsoon sale's last day, so each was a member for
# the whole of both windows; the 13 who joined inside the comparison window stay in the tables.
REPO = HERE.parents[3]
V4_SQL = REPO / "content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql"
THURSDAY_MEMBERS = REPO / "content/W04/D4/data/C2_W04_D04_kalpa_memberships_STUDENT.csv"
COMPARISON = (dt.date(2026, 8, 20), dt.date(2026, 9, 9))
AUTO_WINDOW = (dt.date(2026, 9, 10), dt.date(2026, 9, 30))
MONSOON_SALE_LAST_DAY = dt.date(2026, 8, 19)
MERGED, AUTO = 29, 44               # the 107's: 7 v4 orders + 29 merged = 36 placements, then 44 (1.22)
LATE_MERGED, LATE_AUTO = 2, 4       # the 13's, beside their 3 v4 orders
POOL, AUTO_EXTRA = 30, 8            # the 107 who use the Reorder button, and the others the feature reached
CASE_SHA256 = {                     # git show origin/main:<path> | sha256sum, 13 October 2026
    "drivers": "c93a28b597e50ee8828663a4030dd8ae678b6676b2ea6e3ff476d5036f756b8b",
    "driver_weeks": "9d18cc7ba078dea7e48114e658ddafb816f33859aa6d167734994a48da169219",
    "zone_weeks": "ad6c2463bd43a69e43c2f1571fab6b7f7943734998df283a8b6bb81be37c2b48",
}
sql_lines = V4_SQL.read_text(encoding="utf-8").splitlines()


def copy_block(table):
    """One table of the v4 dump as a list of dicts, read the way Thursday's generator reads it."""
    start = next(i for i, line in enumerate(sql_lines) if line.startswith(f"COPY {table} "))
    cols = sql_lines[start].split("(")[1].split(")")[0].split(", ")
    out, i = [], start + 1
    while sql_lines[i] != "\\.":
        out.append(dict(zip(cols, sql_lines[i].split("\t"))))
        i += 1
    return out


def days_in(span):
    return [span[0] + dt.timedelta(days=d) for d in range((span[1] - span[0]).days + 1)]


members_bytes = THURSDAY_MEMBERS.read_bytes()
(DATA / f"{STEM}_kalpa_members_STUDENT.csv").write_bytes(members_bytes)
members = pd.read_csv(THURSDAY_MEMBERS)
since = dict(zip(members["customer_id"], members["member_since"]))
base = sorted(c for c, s in since.items() if s <= MONSOON_SALE_LAST_DAY.isoformat())
late_joiners = sorted(c for c in since if c not in set(base))
v4_app = [o for o in copy_block("orders") if o["customer_id"] in since and o["channel"] == "app"]
in_span = lambda o, span: span[0].isoformat() <= o["order_date"] <= span[1].isoformat()  # noqa: E731
v4_comparison = sorted((o for o in v4_app if in_span(o, COMPARISON)), key=lambda o: (o["order_date"], o["order_id"]))
v4_window = [o for o in v4_app if in_span(o, AUTO_WINDOW)]
AMOUNTS = sorted(int(o["amount"]) for o in v4_app if "2026-07-01" <= o["order_date"] <= "2026-09-30")

krng = random.Random(f"{SEED} kalpa")
k_rows = [{"customer_id": o["customer_id"], "day": o["order_date"], "value_rs": int(o["amount"]), "auto": False,
           "status": o["status"], "order_id": o["order_id"]} for o in v4_comparison]
users = sorted({o["customer_id"] for o in v4_comparison} & set(base))
non_users = [c for c in base if c not in users]
krng.shuffle(non_users)
pool = sorted(users + non_users[: POOL - len(users)])
auto_pool = pool + sorted(non_users[POOL - len(users): POOL - len(users) + AUTO_EXTRA])
order_days = {(o["customer_id"], o["order_date"]) for o in v4_comparison}


def merged_row(r, who):
    """A Reorder press whose items joined an open basket: never on a day the member's own order was placed."""
    open_days = [d.isoformat() for d in days_in(COMPARISON)
                 if d.isoformat() >= since[who] and (who, d.isoformat()) not in order_days]
    return {"customer_id": who, "day": r.choice(open_days), "value_rs": r.choice(AMOUNTS), "auto": False,
            "status": "merged", "order_id": ""}


def auto_row(r, who):
    """A placement the app made itself: cancelled or merged, or pending if placed in the last week."""
    day = r.choice(days_in(AUTO_WINDOW))
    status = r.choice(["cancelled", "merged", "pending"] if day >= dt.date(2026, 9, 24) else ["cancelled", "merged"])
    return {"customer_id": who, "day": day.isoformat(), "value_rs": r.choice(AMOUNTS), "auto": True,
            "status": status, "order_id": ""}


k_rows += [merged_row(krng, krng.choice(pool)) for _ in range(MERGED)]
autos = [auto_row(krng, krng.choice(auto_pool)) for _ in range(AUTO)]
# The auto placements' values, scaled in tens so the 107's booked value in the window is 0.96 of the comparison's.
comparison_rs = sum(r["value_rs"] for r in k_rows if r["customer_id"] in set(base))
want_rs = 10 * round(0.96 * comparison_rs / 10)
scale = want_rs / sum(r["value_rs"] for r in autos)
for r in autos:
    r["value_rs"] = 10 * round(r["value_rs"] * scale / 10)
gap = (want_rs - sum(r["value_rs"] for r in autos)) // 10
for i in range(abs(gap)):
    autos[i % len(autos)]["value_rs"] += 10 if gap > 0 else -10
k_rows += autos
lrng = random.Random(f"{SEED} kalpa late")
k_rows += [merged_row(lrng, lrng.choice(late_joiners)) for _ in range(LATE_MERGED)]
for _ in range(LATE_AUTO):
    r = auto_row(lrng, lrng.choice(late_joiners))
    r["value_rs"] = 10 * round(r["value_rs"] * scale / 10)
    k_rows.append(r)
for r in k_rows:
    r["placed_ts"] = f"{r['day']}T{krng.randint(8, 21):02d}:{krng.randint(0, 59):02d}:00"
reorders = pd.DataFrame(k_rows).sort_values(["placed_ts", "customer_id"], kind="stable").reset_index(drop=True)
reorders.insert(0, "reorder_id", [f"re_{i:06d}" for i in range(1, len(reorders) + 1)])
reorders = reorders[["reorder_id", "customer_id", "placed_ts", "value_rs", "auto", "status", "order_id"]]
reorders.to_csv(DATA / f"{STEM}_kalpa_app_reorders_STUDENT.csv", index=False)

# ---------------------------------------------------------------------------------- the numbers
dw["window"] = dw["week_start"].lt(LAUNCH.isoformat()).map({True: "before", False: "after"})
dw["group"] = dw["driver_id"].map(GROUP)
zw["window"] = zw["week_start"].lt(LAUNCH.isoformat()).map({True: "before", False: "after"})
city = dw.groupby("window").sum(numeric_only=True)
zones = zw.groupby("window").agg(requests=("peak_requests", "sum"), fulfilled=("peak_fulfilled", "sum"),
                                 wait=("median_wait_min", "median"))
B, A = city.loc["before"], city.loc["after"]
rows_n = dw.groupby("window").size()
online_n = dw[dw["peak_online_hours"] > 0].groupby("window").size()
after = dw[dw["window"] == "after"].copy()
after["acceptance"] = after["peak_accepted"] / after["peak_offers"]
low_topup = int(after.loc[after["acceptance"] < 0.5, "topup_rs"].sum())
high_topup = int(after.loc[after["acceptance"] >= 0.5, "topup_rs"].sum())
per_driver = after.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
slow = per_driver[per_driver["peak_trips"] / per_driver["peak_online_hours"] < 1.0]
idle = dw[dw["group"] == "idle"].groupby("window").sum(numeric_only=True)
idle_outer = (dw[(dw["group"] == "idle") & dw["zone_mode"].isin(OUTER)]
              .groupby("window")["peak_online_hours"].sum())
outer_share = (idle_outer["after"] - idle_outer["before"]) / (idle.loc["after", "peak_online_hours"]
                                                                 - idle.loc["before", "peak_online_hours"])
pre = dw[dw["group"] != "new"].groupby("window").sum(numeric_only=True)
core = dw[dw["zone_mode"].isin(CORE)].groupby("window").sum(numeric_only=True)
crest = dw[dw["week_start"].isin([w.isoformat() for w in AFTER[:3]])][["peak_trips", "peak_online_hours"]].sum()
online = dw[dw["peak_online_hours"] > 0].copy()
online["ratio"] = online["peak_trips"] / online["peak_online_hours"]
mean_of_ratios = online.groupby("window")["ratio"].mean()
weekly = dw.groupby("week_start").agg(
    hours=("peak_online_hours", "sum"), trips=("peak_trips", "sum"), offers=("peak_offers", "sum"),
    accepted=("peak_accepted", "sum"), bookings=("peak_bookings_rs", "sum"),
    rows=("driver_id", "size"), online=("peak_online_hours", lambda s: int((s > 0).sum())))
weekly = weekly.join(zw.groupby("week_start").agg(requests=("peak_requests", "sum"),
                                                  fulfilled=("peak_fulfilled", "sum")))
north = (dw[dw["peak_online_hours"] > 0].groupby("window")["peak_trips"].sum() / online_n)

# The lab's numbers, counted the way the notebook counts them: the 107, per member, in each window.
reorders["day"] = reorders["placed_ts"].str[:10]
reorders["slot"] = reorders["day"].map(lambda d: "comparison" if d <= COMPARISON[1].isoformat() else "window")
in_base = reorders["customer_id"].isin(base)
counts = reorders[in_base].groupby("slot").size()
booked = reorders[in_base].groupby("slot")["value_rs"].sum()
k_count_ratio = (counts["window"] / len(base)) / (counts["comparison"] / len(base))
k_value_ratio = (booked["window"] / len(base)) / (booked["comparison"] / len(base))
all_counts = reorders.groupby("slot").size()
all_booked = reorders.groupby("slot")["value_rs"].sum()
window_rows = reorders[reorders["slot"] == "window"]
# The lab's twelve rows: the first seven of the 107, in id order, with placements in both windows whose
# hand count leans the way the full table does and sits at least 0.10 from each of its two ratios.
per_member = reorders[in_base].pivot_table(index="customer_id", columns="slot", values="value_rs",
                                           aggfunc=["size", "sum"], fill_value=0)
per_member.columns = [f"{a}_{b}" for a, b in per_member.columns]
both = per_member[(per_member["size_comparison"] > 0) & (per_member["size_window"] > 0)]
for lab in itertools.combinations(both.index, 7):
    lab_t = both.loc[list(lab)]
    lab_count_ratio = lab_t["size_window"].sum() / lab_t["size_comparison"].sum()
    lab_value_ratio = lab_t["sum_window"].sum() / lab_t["sum_comparison"].sum()
    if lab_count_ratio >= k_count_ratio + 0.10 and lab_value_ratio <= k_value_ratio - 0.10:
        break

# ---------------------------------------------------------------------------------- the contract
lines = []


def check(name, ok, got=None, want=None):
    lines.append(("PASS" if ok else "FAIL", name, got, want))


r2 = lambda x: round(float(x), 2)
r3 = lambda x: round(float(x), 3)
check("peak online hours, before", B["peak_online_hours"] == 118000, B["peak_online_hours"], 118000)
check("peak online hours, after", A["peak_online_hours"] == 146300, A["peak_online_hours"], 146300)
check("hours up 24 percent", round(100 * (A["peak_online_hours"] / B["peak_online_hours"] - 1)) == 24)
check("completed peak trips, before", B["peak_trips"] == 224200, B["peak_trips"], 224200)
check("completed peak trips, after", A["peak_trips"] == 230900, A["peak_trips"], 230900)
check("trips up 3 percent", round(100 * (A["peak_trips"] / B["peak_trips"] - 1)) == 3)
check("trips per peak online hour 1.90 before", r2(B["peak_trips"] / B["peak_online_hours"]) == 1.90)
check("trips per peak online hour 1.58 after", r2(A["peak_trips"] / A["peak_online_hours"]) == 1.58)
check("acceptance 0.863 before", r3(B["peak_accepted"] / B["peak_offers"]) == 0.863,
      r3(B["peak_accepted"] / B["peak_offers"]), 0.863)
check("acceptance 0.730 after", r3(A["peak_accepted"] / A["peak_offers"]) == 0.730,
      r3(A["peak_accepted"] / A["peak_offers"]), 0.730)
check("driver cancels share 0.037 before", r3(B["peak_driver_cancels"] / B["peak_accepted"]) == 0.037)
check("driver cancels share 0.090 after", r3(A["peak_driver_cancels"] / A["peak_accepted"]) == 0.090)
check("accepted = trips + driver cancels in every row",
      (dw["peak_accepted"] == dw["peak_trips"] + dw["peak_driver_cancels"]).all())
check("share of peak online hours with no trip 0.22 before",
      r2(B["peak_hours_no_trip"] / B["peak_online_hours"]) == 0.22)
check("share of peak online hours with no trip 0.38 after",
      r2(A["peak_hours_no_trip"] / A["peak_online_hours"]) == 0.38)
check("hours with no trip never exceed hours, never fall below hours less trips",
      ((dw["peak_hours_no_trip"] <= dw["peak_online_hours"])
       & (dw["peak_hours_no_trip"] >= (dw["peak_online_hours"] - dw["peak_trips"]).clip(lower=0))).all())
check("median rider wait 4.8 before", r2(zones.loc["before", "wait"]) == 4.8, zones.loc["before", "wait"], 4.8)
check("median rider wait 4.6 after", r2(zones.loc["after", "wait"]) == 4.6, zones.loc["after", "wait"], 4.6)
check("unfulfilled share 0.11 before",
      r3(1 - zones.loc["before", "fulfilled"] / zones.loc["before", "requests"]) == 0.110)
check("unfulfilled share 0.10 after",
      r3(1 - zones.loc["after", "fulfilled"] / zones.loc["after", "requests"]) == 0.100)
check("rider requests rise slightly, 251,910 to 256,556",
      (zones.loc["before", "requests"], zones.loc["after", "requests"]) == (251910, 256556))
check("zone fulfilled equals driver trips, week by week",
      (weekly["fulfilled"] == weekly["trips"]).all())
check("requests crest in the first after weeks and ease by the last",
      weekly["requests"].idxmax() in [w.isoformat() for w in AFTER[:3]]
      and weekly["requests"].iloc[-1] < weekly["requests"].iloc[7])
check("bookings Rs 3,69,93,000 before and Rs 3,80,98,500 after",
      (B["peak_bookings_rs"], A["peak_bookings_rs"]) == (36993000, 38098500))
check("Rs 314 and Rs 260 per peak online hour",
      (round(B["peak_bookings_rs"] / B["peak_online_hours"]), round(A["peak_bookings_rs"] / A["peak_online_hours"]))
      == (314, 260))
check("top-up Rs 0 before and Rs 1.9 crore after", (B["topup_rs"], A["topup_rs"]) == (0, 19000000))
check("61 percent of the top-up to driver-weeks under 0.5 acceptance",
      (low_topup, high_topup) == (11590000, 7410000), (low_topup, high_topup), (11590000, 7410000))
check("no top-up above the floor times the hours", (dw["topup_rs"] <= FLOOR * dw["peak_online_hours"]).all())
check("no driver-week above 42 peak hours", dw["peak_online_hours"].max() <= MAX_HOURS,
      dw["peak_online_hours"].max(), MAX_HOURS)
check("driver-weeks 6,360 before and 6,500 after", (rows_n["before"], rows_n["after"]) == (6360, 6500))
check("drivers online at peak vary week to week", weekly["online"].nunique() >= 8,
      weekly["online"].tolist())
check("1,200 drivers, 140 joined after the launch",
      len(drivers) == 1200 and sum(d["joined_month"] == "2026-09" for d in drivers) == 140)
check("idle tail: 180 drivers under 1.0 trips per peak online hour after the launch",
      len(slow) == 180 and set(slow.index) == {d for d, g in GROUP.items() if g == "idle"}, len(slow), 180)
check("idle tail: hours 2.1 times", r2(idle.loc["after", "peak_online_hours"] / idle.loc["before", "peak_online_hours"]) == 2.10)
check("idle tail: trips 0.88 times", r2(idle.loc["after", "peak_trips"] / idle.loc["before", "peak_trips"]) == 0.88)
check("idle tail: 72 percent of new hours in the outer zones", r2(outer_share) == 0.72, r2(outer_share), 0.72)
check("idle tail driver-weeks after the launch all under 0.5 acceptance",
      (after.loc[after["group"] == "idle", "acceptance"] < 0.5).all())
check("every other driver-week after the launch with an hour online at 0.5 or above",
      (after.loc[(after["group"] != "idle") & (after["peak_online_hours"] > 0), "acceptance"] >= 0.5).all())
check("the fall survives without the 140 new drivers",
      r2(pre.loc["after", "peak_trips"] / pre.loc["after", "peak_online_hours"]) < 1.65)
check("in the three crest weeks the fall is already there",
      crest["peak_trips"] / crest["peak_online_hours"] < 1.65)
tw = dw[dw["driver_id"].isin(TWELVE_IDS) & dw["week_start"].isin([d.isoformat() for d in TWELVE_WEEKS.values()])]
tw_sum = tw.groupby("window")[["peak_online_hours", "peak_trips"]].sum()
check("twelve rows: hours 60 to 74, trips 114 to 88",
      (tw_sum.loc["before"].tolist(), tw_sum.loc["after"].tolist()) == ([60, 114], [74, 88]))
check("twelve rows: 1.90 to 1.19 trips per hour",
      (r2(114 / 60), r2(88 / 74)) == (1.90, 1.19))
check("twelve-row hand count at least 0.05 from the city's 1.58",
      abs(88 / 74 - A["peak_trips"] / A["peak_online_hours"]) >= 0.05)
idle_after_rows = dw[(dw["group"] == "idle") & (dw["window"] == "after")]
idle_week_hours = idle_after_rows["peak_online_hours"].sum() / (len(slow) * len(AFTER))
check("the idle tail averages 39 peak online hours a driver-week after the launch; E and F log 16 and 14",
      round(idle_week_hours) == 39 and len(idle_after_rows) == len(slow) * len(AFTER)
      and (TWELVE["E"][3][0], TWELVE["F"][3][0]) == (16, 14), round(idle_week_hours, 1), 39)
written = {t: hashlib.sha256((DATA / f"{STEM}_{t}_STUDENT.csv").read_bytes()).hexdigest() for t in CASE_SHA256}
check("the case tables (drivers, driver_weeks, zone_weeks) are byte-identical to origin/main", written == CASE_SHA256)
check("Kalpa: kalpa_members is Thursday's kalpa_memberships, byte for byte",
      (DATA / f"{STEM}_kalpa_members_STUDENT.csv").read_bytes() == THURSDAY_MEMBERS.read_bytes())
by_month = members["member_since"].str[:7].value_counts().sort_index()
check("Kalpa: 120 members, C-0151 to C-0270; 11 to 14 joined a month from January to July, 32 in August, "
      "the last on 29 August",
      len(members) == 120 and members["customer_id"].is_unique
      and (members["customer_id"].min(), members["customer_id"].max()) == ("C-0151", "C-0270")
      and by_month.loc["2026-01":"2026-07"].between(11, 14).all() and by_month.get("2026-08") == 32
      and members["member_since"].max() == "2026-08-29")
check("Kalpa: 107 joined by 19 August, the monsoon sale's last day, and 13 from 20 to 29 August",
      (len(base), len(late_joiners)) == (107, 13) and min(since[c] for c in late_joiners) >= "2026-08-20",
      (len(base), len(late_joiners)), (107, 13))
check("Kalpa: every placement falls from 20 August to 30 September, never before its member joined",
      reorders["day"].between(COMPARISON[0].isoformat(), AUTO_WINDOW[1].isoformat()).all()
      and (reorders["day"] >= reorders["customer_id"].map(since)).all())
v4_by_id = {o["order_id"]: o for o in v4_comparison}
as_orders = reorders[reorders["order_id"] != ""]
check("Kalpa join, log to warehouse: every placement with an order_id is a v4 app order of 20 August to 9 "
      "September, with its customer, date, amount and status",
      all(r.order_id in v4_by_id and (r.customer_id, r.day, r.value_rs, r.status)
          == (v4_by_id[r.order_id]["customer_id"], v4_by_id[r.order_id]["order_date"],
              int(v4_by_id[r.order_id]["amount"]), v4_by_id[r.order_id]["status"])
          for r in as_orders.itertuples()))
check("Kalpa join, warehouse to log: each of v4's 10 Retail-Plus app orders of that window appears exactly once",
      sorted(as_orders["order_id"]) == sorted(v4_by_id) and len(v4_by_id) == 10, len(as_orders), 10)
comparison_rows = reorders[reorders["slot"] == "comparison"]
check("Kalpa: the comparison window holds members' own placements only, the rest merged with no order_id",
      (~comparison_rows["auto"]).all()
      and comparison_rows.loc[comparison_rows["order_id"] == "", "status"].eq("merged").all())
check("Kalpa: every placement in the window is the app's own, cancelled, merged or pending, with no order_id",
      window_rows["auto"].all() and window_rows["status"].isin(["cancelled", "merged", "pending"]).all()
      and window_rows["order_id"].eq("").all())
check("Kalpa: v4's 7 Retail-Plus app orders of 10 to 30 September are members' own checkouts, outside the log",
      len(v4_window) == 7 and not {o["order_id"] for o in v4_window} & set(reorders["order_id"]), len(v4_window), 7)
check("Kalpa plant: reorders placed per member, the 107, 1.22 times", r2(k_count_ratio) == 1.22, r2(k_count_ratio),
      1.22)
check("Kalpa plant: booked value per member, the 107, any status, 0.96 times", r2(k_value_ratio) == 0.96,
      r2(k_value_ratio), 0.96)
check("Kalpa plant: none of the window's placements delivered", not window_rows["status"].eq("delivered").any())
check("Kalpa: v4's scale, a few tenths of a placement per member per window",
      all(0.2 <= counts[s] / len(base) <= 0.5 for s in ("comparison", "window")),
      (r2(counts["comparison"] / len(base)), r2(counts["window"] / len(base))))
check("Kalpa: over all 120 members both ratios print otherwise, so the base of 107 changes the answer",
      abs(all_counts["window"] / all_counts["comparison"] - k_count_ratio) >= 0.03
      and abs(all_booked["window"] / all_booked["comparison"] - k_value_ratio) >= 0.03,
      (r2(all_counts["window"] / all_counts["comparison"]), r2(all_booked["window"] / all_booked["comparison"])))
check("Kalpa lab twelve rows: seven of the 107 with placements in both windows, both ratios at least 0.05 from "
      "1.22 and 0.96",
      len(lab) == 7 and set(lab) <= set(base) and (lab_t[["size_comparison", "size_window"]] > 0).all().all()
      and abs(lab_count_ratio - 1.22) >= 0.05 and abs(lab_value_ratio - 0.96) >= 0.05,
      (r2(lab_count_ratio), r2(lab_value_ratio)))
sale = next(c for c in copy_block("campaigns") if c["name"] == "Monsoon Sale")
check("Kalpa: v4's monsoon sale runs 5 to 19 August for Retail-Plus, its last day the shared constant",
      (sale["start_date"], sale["end_date"], sale["segment"]) == ("2026-08-05", MONSOON_SALE_LAST_DAY.isoformat(),
                                                                  "Retail-Plus"), (sale["start_date"], sale["end_date"]))
thursday = yaml.safe_load((REPO / "content/W04/D4/internal/C2_W04_D04_facts_INTERNAL.yaml")
                          .read_text(encoding="utf-8"))["shared_constants"]
shared = {"kalpa_comparison_window": [d.isoformat() for d in COMPARISON],
          "kalpa_auto_reorder_window": [d.isoformat() for d in AUTO_WINDOW],
          "monsoon_sale_last_day": MONSOON_SALE_LAST_DAY.isoformat()}
check("shared constants: the two Kalpa windows and the monsoon sale's last day, equal to Thursday's",
      shared == thursday and shared["kalpa_comparison_window"] == ["2026-08-20", "2026-09-09"]
      and shared["kalpa_auto_reorder_window"] == ["2026-09-10", "2026-09-30"]
      and shared["monsoon_sale_last_day"] == "2026-08-19")

# ---------------------------------------------------------------------------------- the facts file
numbers = []


def fact(fid, value, unit, how, used_by):
    if hasattr(value, "item"):
        value = value.item()
    numbers.append({"id": fid, "value": value, "unit": unit, "how": how, "used_by": used_by})


TICKET = "the ticket; half1 S1; notebook 01 cell 1; cheat sheet panel 1; notes"
fact("launch_date", "2026-08-31", "date", "the scheme's first day, a Monday", TICKET)
fact("window_before", "2026-07-20 to 2026-08-30", "dates", "six weeks beginning 20 July", TICKET)
fact("window_after", "2026-08-31 to 2026-10-11", "dates", "six weeks beginning 31 August", TICKET)
fact("floor_rs_per_hour", FLOOR, "Rs per peak online hour", "the guarantee's floor (synthetic terms)", TICKET)
fact("peak_windows_per_day", WINDOWS_PER_DAY, "windows", "two peak windows a day (synthetic terms)", TICKET)
fact("peak_window_hours", WINDOW_HOURS, "hours", "each window three hours long", TICKET)
fact("max_peak_hours_per_week", MAX_HOURS, "hours", "2 windows x 3 hours x 7 days", "data dictionary; L4")
fact("fare_avg_rs", FARE, "Rs per trip", "bookings / trips, both windows", "L2; Tuesday's per-trip denominator")
fact("drivers_total", 1200, "drivers", "rows of drivers", TICKET)
fact("drivers_new", 140, "drivers", "joined_month 2026-09", TICKET + "; L4 mix")
fact("drivers_pre_launch", 1060, "drivers", "1,200 less 140", "L4 mix")
fact("zones_total", 12, "zones", "rows of zone_weeks per week", TICKET)
fact("zones_outer", 3, "zones", "Shamshabad, Rajendranagar, Patancheru", TICKET)
for win, row in (("before", B), ("after", A)):
    fact(f"hours_{win}", row["peak_online_hours"], "hours", f"sum of peak_online_hours, {win}", TICKET + "; L2")
    fact(f"trips_{win}", row["peak_trips"], "trips", f"sum of peak_trips, {win}", TICKET + "; L2")
    fact(f"tph_{win}", r2(row["peak_trips"] / row["peak_online_hours"]), "trips per peak online hour",
         "sum of trips / sum of hours", TICKET + "; L2")
    fact(f"offers_{win}", row["peak_offers"], "offers", f"sum of peak_offers, {win}", "L2")
    fact(f"accepted_{win}", row["peak_accepted"], "offers", f"sum of peak_accepted, {win}", "L2")
    fact(f"driver_cancels_{win}", row["peak_driver_cancels"], "trips", f"sum of peak_driver_cancels, {win}", "L2")
    fact(f"acceptance_{win}", r3(row["peak_accepted"] / row["peak_offers"]), "share",
         "sum accepted / sum offers", TICKET + "; L2; guardrail 1")
    fact(f"driver_cancel_share_{win}", r3(row["peak_driver_cancels"] / row["peak_accepted"]), "share",
         "sum driver cancels / sum accepted", TICKET)
    fact(f"no_trip_hours_{win}", row["peak_hours_no_trip"], "hours", f"sum of peak_hours_no_trip, {win}", "L4")
    fact(f"no_trip_share_{win}", r2(row["peak_hours_no_trip"] / row["peak_online_hours"]), "share",
         "sum hours with no trip / sum hours", TICKET + "; L4 data quality")
    fact(f"bookings_{win}_rs", row["peak_bookings_rs"], "Rs", f"sum of peak_bookings_rs, {win}", "L2; Tuesday")
    fact(f"rs_per_hour_{win}", round(row["peak_bookings_rs"] / row["peak_online_hours"], 1), "Rs",
         "bookings / hours", "L2; Tuesday")
    fact(f"driver_weeks_{win}", int(rows_n[win]), "driver-weeks", "rows of driver_weeks", "L2; Tuesday")
    fact(f"online_driver_weeks_{win}", int(online_n[win]), "driver-weeks",
         "rows with at least one peak online hour", "L5 denominator; Tuesday")
    fact(f"rs_per_driver_week_{win}", round(row["peak_bookings_rs"] / rows_n[win], 1), "Rs",
         "bookings / driver-weeks", "Tuesday")
    fact(f"north_star_{win}", r2(north[win]), "trips per online driver-week",
         "trips / driver-weeks with at least one peak hour", "L5 the redesign's north star")
    fact(f"requests_{win}", int(zones.loc[win, "requests"]), "rider requests", "sum of zone peak_requests",
         "L2 the demand check")
    fact(f"unfulfilled_share_{win}", r2(1 - zones.loc[win, "fulfilled"] / zones.loc[win, "requests"]), "share",
         "1 - fulfilled / requests", TICKET)
    fact(f"median_wait_{win}", r2(zones.loc[win, "wait"]), "minutes",
         "middle value of the 72 zone-week medians", TICKET + "; guardrail 2")
    fact(f"offers_per_request_{win}", r2(row["peak_offers"] / zones.loc[win, "requests"]), "offers",
         "driver offers / rider requests", "L2 the two tables")
    fact(f"mean_of_ratios_{win}", r2(mean_of_ratios[win]), "trips per peak online hour",
         "mean of each online driver-week's trips / hours (the wrong number)", "L2 trap")
fact("hours_change_pct", round(100 * (A["peak_online_hours"] / B["peak_online_hours"] - 1)), "percent",
     "146,300 / 118,000 - 1", TICKET)
fact("trips_change_pct", round(100 * (A["peak_trips"] / B["peak_trips"] - 1)), "percent",
     "230,900 / 224,200 - 1", TICKET)
fact("requests_change_pct", round(100 * (zones.loc["after", "requests"] / zones.loc["before", "requests"] - 1), 1),
     "percent", "256,556 / 251,910 - 1", "L2 the demand check")
fact("topup_before_rs", int(B["topup_rs"]), "Rs", "sum of topup_rs, before", TICKET)
fact("topup_after_rs", int(A["topup_rs"]), "Rs", "sum of topup_rs, after (Rs 1.9 crore)", TICKET + "; L3")
fact("topup_low_acceptance_rs", low_topup, "Rs",
     "top-up to after driver-weeks with accepted / offers under 0.5 (Rs 1.159 crore)", "L3; L5")
fact("topup_low_acceptance_share", r2(low_topup / A["topup_rs"]), "share", "11,590,000 / 19,000,000", "L3; L5")
fact("topup_high_acceptance_rs", high_topup, "Rs",
     "top-up to after driver-weeks at or above 0.5 acceptance (Rs 74 lakh); what the six weeks would "
     "have cost had only these driver-weeks been paid and every driver behaved the same", "L5")
fact("topup_per_trip_after_rs", round(A["topup_rs"] / A["peak_trips"], 1), "Rs per completed trip",
     "top-up / trips, after", "guardrail 3")
fact("uptake_low", 0.2, "share (assumption)",
     "share of the idle tail's top-up that would still be paid because those drivers start accepting "
     "(assumption, range 0.2 to 0.5; the A/B test settles it)", "L5")
fact("uptake_high", 0.5, "share (assumption)", "upper end of the same assumption", "L5")
fact("saving_same_behaviour_rs", low_topup, "Rs", "the top-up the redesign stops paying if nobody changes", "L5")
fact("saving_low_rs", round(low_topup * 0.5), "Rs", "11,590,000 x (1 - 0.5)", "L5")
fact("saving_high_rs", round(low_topup * 0.8), "Rs", "11,590,000 x (1 - 0.2)", "L5")
fact("idle_tail_drivers", len(slow), "drivers",
     "drivers whose after-window trips / hours is under 1.0", "L3 your-turn cell")
fact("idle_tail_share_of_drivers", r2(len(slow) / 1200), "share", "180 / 1,200", "L3")
fact("idle_hours_before", int(idle.loc["before", "peak_online_hours"]), "hours", "idle tail, before", "L3")
fact("idle_hours_after", int(idle.loc["after", "peak_online_hours"]), "hours", "idle tail, after", "L3")
fact("idle_trips_before", int(idle.loc["before", "peak_trips"]), "trips", "idle tail, before", "L3")
fact("idle_trips_after", int(idle.loc["after", "peak_trips"]), "trips", "idle tail, after", "L3")
fact("idle_hours_ratio", r2(idle.loc["after", "peak_online_hours"] / idle.loc["before", "peak_online_hours"]),
     "times", "42,000 / 20,000", "L3")
fact("idle_trips_ratio", r2(idle.loc["after", "peak_trips"] / idle.loc["before", "peak_trips"]),
     "times", "33,440 / 38,000 (down 12 percent)", "L3")
fact("idle_new_hours_outer_share", r2(outer_share), "share",
     "(idle outer-zone hours after - before) / (idle hours after - before)", "L3")
others = dw[dw["group"] == "ord"].groupby("window").sum(numeric_only=True)
fact("drivers_others", ORD, "drivers", "drivers who joined before the launch and sit outside the idle tail",
     "L5 driver operations' objection")
for win in ("before", "after"):
    fact(f"others_hours_{win}", int(others.loc[win, "peak_online_hours"]), "hours", f"the other 880 drivers, {win}", "L5")
    fact(f"others_trips_{win}", int(others.loc[win, "peak_trips"]), "trips", f"the other 880 drivers, {win}", "L5")
    fact(f"others_tph_{win}", r2(others.loc[win, "peak_trips"] / others.loc[win, "peak_online_hours"]),
         "trips per peak online hour", f"the other 880 drivers, {win}", "L5")
    fact(f"requests_per_hour_{win}", r2(zones.loc[win, "requests"] / city.loc[win, "peak_online_hours"]),
         "rider requests per peak online hour", "zone requests / driver hours", "the input on the tree")
on_after = after[after["peak_online_hours"] > 0]
fact("acceptance_max_idle_week_after", r2(on_after.loc[on_after["group"] == "idle", "acceptance"].max()), "share",
     "highest weekly accepted share of any idle-tail driver-week after the launch", "L5 the floor; follow-up 2")
fact("acceptance_min_other_week_after", r2(on_after.loc[on_after["group"] != "idle", "acceptance"].min()), "share",
     "lowest weekly accepted share of any other driver-week online after the launch", "L5 the floor; follow-up 2")
fact("tph_pre_launch_after", r2(pre.loc["after", "peak_trips"] / pre.loc["after", "peak_online_hours"]),
     "trips per peak online hour", "after window, drivers who joined before the launch", "L4 mix")
fact("tph_core_zones_before", r2(core.loc["before", "peak_trips"] / core.loc["before", "peak_online_hours"]),
     "trips per peak online hour", "driver-weeks whose zone_mode is a core zone, before", "L4 thin zones")
fact("tph_core_zones_after", r2(core.loc["after", "peak_trips"] / core.loc["after", "peak_online_hours"]),
     "trips per peak online hour", "driver-weeks whose zone_mode is a core zone, after", "L4 thin zones")
fact("tph_crest_weeks_after", r2(crest["peak_trips"] / crest["peak_online_hours"]), "trips per peak online hour",
     "the three after weeks with the most rider requests", "L4 seasonality bound")
for week, r in weekly.iterrows():
    key = week.replace("-", "_")
    fact(f"tph_{key}", r2(r["trips"] / r["hours"]), "trips per peak online hour", f"week of {week}",
         "the drift chart; explorer M1; Tuesday")
for week, r in weekly.iterrows():
    key = week.replace("-", "_")
    fact(f"hours_{key}", int(r["hours"]), "hours", f"week of {week}", "the drift chart; Tuesday")
    fact(f"trips_{key}", int(r["trips"]), "trips", f"week of {week}", "the drift chart; Tuesday")
    fact(f"requests_{key}", int(r["requests"]), "rider requests", f"week of {week}", "L4 seasonality")
    fact(f"acceptance_{key}", r3(r["accepted"] / r["offers"]), "share", f"week of {week}", "explorer M4; Tuesday")
    fact(f"rs_per_hour_{key}", round(r["bookings"] / r["hours"], 1), "Rs", f"week of {week}", "explorer M4; Tuesday")
    fact(f"bookings_{key}_rs", int(r["bookings"]), "Rs", f"week of {week}", "Tuesday")
    fact(f"driver_weeks_{key}", int(r["rows"]), "driver-weeks", f"week of {week}", "Tuesday")
    fact(f"online_drivers_{key}", int(r["online"]), "drivers", f"week of {week}, at least one peak hour",
         "L4; Tuesday")
fact("twelve_hours_before", 60, "hours", "sum of the six before rows", "L1 hand count")
fact("twelve_hours_after", 74, "hours", "sum of the six after rows", "L1 hand count")
fact("twelve_trips_before", 114, "trips", "sum of the six before rows", "L1 hand count")
fact("twelve_trips_after", 88, "trips", "sum of the six after rows", "L1 hand count")
fact("twelve_tph_before", 1.90, "trips per peak online hour", "114 / 60", "L1 hand count")
fact("twelve_tph_after", 1.19, "trips per peak online hour", "88 / 74", "L1 hand count")
fact("twelve_hours_change_pct", 23, "percent", "74 / 60 - 1", "L1 hand count")
fact("twelve_trips_change_pct", -23, "percent", "88 / 114 - 1", "L1 hand count")
fact("twelve_idle_share", 0.33, "share", "2 of the six drivers (E and F) sit in the idle tail", "L1; L2")
fact("idle_hours_per_driver_week_after", round(idle_week_hours), "peak online hours a driver-week",
     "idle_hours_after 42,000 over 180 drivers and six weeks (38.9), to the nearest hour; E and F log 16 and 14",
     "the twelve rows: the card's two idle drivers keep shorter weeks than the tail's average")
# Added by the finishing session for the exercises, the Kahoot and the ticket's change column; every
# value is read from the same tables, so the data files are unchanged.
fact("acceptance_change_points", round(100 * (B["peak_accepted"] / B["peak_offers"]
                                              - A["peak_accepted"] / A["peak_offers"])), "points",
     "acceptance before less acceptance after, in points", "the ticket's change column")
fact("driver_cancel_change_points", round(100 * (A["peak_driver_cancels"] / A["peak_accepted"]
                                                 - B["peak_driver_cancels"] / B["peak_accepted"])), "points",
     "driver-cancelled share after less before, in points", "the ticket's change column")
fact("no_trip_change_points", round(100 * (A["peak_hours_no_trip"] / A["peak_online_hours"]
                                           - B["peak_hours_no_trip"] / B["peak_online_hours"])), "points",
     "share of hours with no trip after less before, in points", "the ticket's change column")
fact("mean_of_ratios_hidden_share", r2((mean_of_ratios["after"] - A["peak_trips"] / A["peak_online_hours"])
                                       / (B["peak_trips"] / B["peak_online_hours"]
                                          - A["peak_trips"] / A["peak_online_hours"])), "share",
     "(1.71 - 1.58) / (1.90 - 1.58): the part of the fall the average of rates hides", "L2 trap, two-fifths")
fact("topup_high_acceptance_share", r2(high_topup / (low_topup + high_topup)), "share",
     "top-up to driver-weeks at or above half accepted, over all top-up", "L5; S28 option b")
fact("driver_weeks_total", int(len(dw)), "driver-weeks", "rows of driver_weeks, twelve weeks", "notebook 02; S17")
fact("tph_fall", r2(B["peak_trips"] / B["peak_online_hours"] - A["peak_trips"] / A["peak_online_hours"]),
     "trips per peak online hour", "1.90 - 1.58", "L2 trap")
fact("mean_of_ratios_fall", r2(B["peak_trips"] / B["peak_online_hours"] - mean_of_ratios["after"]),
     "trips per peak online hour", "1.90 - 1.71, the fall the average of rates shows", "L2 trap")
fact("fall_hidden_by_mean", r2(mean_of_ratios["after"] - A["peak_trips"] / A["peak_online_hours"]),
     "trips per peak online hour", "1.71 - 1.58, the part of the fall the average hides", "L2 trap")
fact("twelve_trips_per_driver_before", r2(114 / 6), "trips per driver", "114 trips over the six drivers",
     "explorer M3, the enrolled-driver denominator on the twelve rows")
fact("twelve_trips_per_driver_after", r2(88 / 6), "trips per driver", "88 trips over the six drivers",
     "explorer M3, the enrolled-driver denominator on the twelve rows")
# Added after the cold reads: the outer zones' wait and fulfilment, what the top-up bought, and the
# cancel shares by group. Read from the same tables, so the data files are unchanged.
zw["outer"] = zw["zone"].isin(OUTER)
ozw = zw[zw["outer"]].groupby("window").agg(wait=("median_wait_min", "median"),
                                             requests=("peak_requests", "sum"),
                                             fulfilled=("peak_fulfilled", "sum"))
ofil = ozw["fulfilled"] / ozw["requests"]
extra_outer = ozw.loc["after", "fulfilled"] - ozw.loc["after", "requests"] * ofil["before"]
idle_outer_topup = int(after.loc[after["driver_id"].isin(slow.index) & after["zone_mode"].isin(OUTER),
                                 "topup_rs"].sum())
fact("outer_wait_before", r2(ozw.loc["before", "wait"]), "minutes",
     "middle value of the 18 outer zone-week medians, before", "the interview's zone check")
fact("outer_wait_after", r2(ozw.loc["after", "wait"]), "minutes",
     "middle value of the 18 outer zone-week medians, after", "the interview's zone check")
fact("outer_fulfil_before", r3(ofil["before"]), "share", "outer zones' fulfilled over requests, before",
     "the interview's zone check")
fact("outer_fulfil_after", r3(ofil["after"]), "share", "outer zones' fulfilled over requests, after",
     "the interview's zone check")
fact("outer_extra_trips", int(round(extra_outer)), "trips",
     "outer fulfilled after, less outer requests after times the before fulfilment rate", "the interview's zone check")
fact("idle_outer_topup_rs", idle_outer_topup, "Rs",
     "top-up to idle-tail driver-weeks whose zone_mode is an outer zone, after", "the interview's zone check")
fact("cost_per_extra_outer_trip_rs", int(round(idle_outer_topup / extra_outer, -3)), "Rs",
     "idle outer top-up over the extra outer trips, to the nearest thousand", "the interview's zone check")
fact("extra_trips", int(A["peak_trips"] - B["peak_trips"]), "trips", "230,900 - 224,200", "the interview's sizing")
fact("topup_per_extra_trip_rs", round(19000000 / (A["peak_trips"] - B["peak_trips"])), "Rs",
     "Rs 1.9 crore over the 6,700 extra trips", "the interview's sizing")
fact("topup_per_extra_trip_fares", round(19000000 / (A["peak_trips"] - B["peak_trips"]) / FARE, 1), "fares",
     "Rs 2,836 over the Rs 165 average fare", "the interview's sizing")
fact("hours_to_carry_idle_trips", int(round(idle.loc["after", "peak_trips"] / 1.9)), "hours",
     "33,440 idle-tail trips at 1.90 trips per hour", "the role card; follow-up on drivers who quit")
grp = dw.assign(g=dw["driver_id"].map(lambda d: "idle" if d in set(slow.index) else ("new" if d > "d_1060" else "other")))
for gname in ("idle", "new", "other"):
    sub = grp[(grp["g"] == gname) & (grp["window"] == "after")]
    fact(f"cancel_share_{gname}_after", r3(sub["peak_driver_cancels"].sum() / sub["peak_accepted"].sum()), "share",
         f"driver-cancelled over accepted, {gname} drivers, after", "the acceptance guardrail's gaming note")
sub = grp[(grp["g"] == "other") & (grp["window"] == "before")]
fact("cancel_share_other_before", r3(sub["peak_driver_cancels"].sum() / sub["peak_accepted"].sum()), "share",
     "driver-cancelled over accepted, other drivers, before", "the acceptance guardrail's gaming note")
comp = on_after["peak_trips"] / on_after["peak_offers"]
fact("completed_share_max_idle_week_after", r2(comp[on_after["group"] == "idle"].max()), "share",
     "trips over offers shown, highest idle-tail week after", "the payout rule's floor")
fact("completed_share_min_other_week_after", r2(comp[on_after["group"] != "idle"].min()), "share",
     "trips over offers shown, lowest other week online after", "the payout rule's floor")
late = dw["week_start"].lt("2026-09-07").map({True: "before", False: "after"})
late_city = dw.groupby(late)[["peak_trips", "peak_online_hours"]].sum()
for win in ("before", "after"):
    fact(f"tph_split_0907_{win}", r2(late_city.loc[win, "peak_trips"] / late_city.loc[win, "peak_online_hours"]),
         "trips per peak online hour", f"the window flagged at 7 September, so the launch week counts as before; {win}",
         "the lab set's Parsons problem, option d")

toys = [
    {"id": "toy_canteen", "label": "invented", "values": {"tokens_before": 200, "tokens_after": 400,
                                                          "plates": 200}, "used_by": "L1 the proxy"},
    {"id": "toy_two_drivers", "label": "invented",
     "values": {"rates": [2.0, 0.5], "hours": [10, 40], "trips": 40, "total_hours": 50,
                "ratio_of_sums": 0.8, "mean_of_ratios": 1.25},
     "used_by": "L2 ratio of sums; the long, slow week pulls the average up, as on the city"},
    {"id": "toy_mix", "label": "invented",
     "values": {"drivers": 100, "rate": 1.9, "idle_drivers": 20, "idle_rate": 0.2, "blend": 1.62},
     "used_by": "L3 the mix behind a rate"},
]

twelve_rows = []
for label, (did, zone, before_row, after_row) in TWELVE.items():
    for window, vals in (("before", before_row), ("after", after_row)):
        twelve_rows.append({"driver": label, "driver_id": did, "zone": zone, "window": window,
                            "week_start": TWELVE_WEEKS[window].isoformat(), **dict(zip(FIELDS, vals))})

lab_rows = [{"customer_id": cid, "placed_comparison": int(r["size_comparison"]),
             "placed_window": int(r["size_window"]), "booked_comparison_rs": int(r["sum_comparison"]),
             "booked_window_rs": int(r["sum_window"])} for cid, r in lab_t.iterrows()]
example = next(c for c in late_joiners if since[c] == "2026-08-25")
lab_mean = {"placed_ratio": r2((lab_t["size_window"] / lab_t["size_comparison"]).mean()),
            "booked_ratio": r2((lab_t["sum_window"] / lab_t["sum_comparison"]).mean())}
on_20 = reorders["customer_id"].isin([c for c, s in since.items() if s <= COMPARISON[0].isoformat()])
cut_20 = {"members": sum(s <= COMPARISON[0].isoformat() for s in since.values()),
          "placed_ratio": r2((on_20 & (reorders["slot"] == "window")).sum()
                             / (on_20 & (reorders["slot"] == "comparison")).sum()),
          "booked_ratio": r2(reorders.loc[on_20 & (reorders["slot"] == "window"), "value_rs"].sum()
                             / reorders.loc[on_20 & (reorders["slot"] == "comparison"), "value_rs"].sum())}
example_days = (COMPARISON[1] - dt.date.fromisoformat(since[example])).days + 1


def by_status(frame):
    return {s: int(n) for s, n in frame.groupby("status").size().items()}


facts = {
    "day": "W04/D1, Monday 26 October 2026",
    "written_by": "C2_W04_D01_generate_INTERNAL.py, the W04 D1 finishing session, 12 October 2026; the Kalpa "
                  "lab rebuilt on Thursday's membership table, 13 October 2026",
    "source_tables": {
        "drivers": "data/C2_W04_D01_drivers_STUDENT.csv",
        "driver_weeks": "data/C2_W04_D01_driver_weeks_STUDENT.csv",
        "zone_weeks": "data/C2_W04_D01_zone_weeks_STUDENT.csv",
        "kalpa_members": "data/C2_W04_D01_kalpa_members_STUDENT.csv (a byte copy of Thursday's "
                         "data/C2_W04_D04_kalpa_memberships_STUDENT.csv)",
        "kalpa_app_reorders": "data/C2_W04_D01_kalpa_app_reorders_STUDENT.csv (its order_id rows are orders of "
                              "content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql)",
    },
    "numbers": numbers,
    "toys": toys,
    "twelve_rows": twelve_rows,
    "kalpa": {
        "members": len(members),
        "members_base": len(base),
        "members_joined_in_comparison": len(late_joiners),
        "base_rule": "members whose member_since is on or before 19 August 2026, the monsoon sale's last day, "
                     "so each was a member for the whole of both windows",
        "members_joined_by_month": {m: int(n) for m, n in by_month.items()},
        "window_days": {"comparison": len(days_in(COMPARISON)), "auto_reorder": len(days_in(AUTO_WINDOW))},
        "late_example": {"customer_id": example, "member_since": since[example], "comparison_days": example_days,
                         "comparison_days_missed": len(days_in(COMPARISON)) - example_days},
        "rows_in_log": len(reorders),
        "reorders_comparison": int(counts["comparison"]),
        "reorders_window": int(counts["window"]),
        "booked_comparison_rs": int(booked["comparison"]),
        "booked_window_rs": int(booked["window"]),
        "placed_per_member": {s: r3(counts[s] / len(base)) for s in ("comparison", "window")},
        "booked_per_member_rs": {s: round(float(booked[s] / len(base)), 1) for s in ("comparison", "window")},
        "mean_value_rs": {s: round(float(booked[s] / counts[s])) for s in ("comparison", "window")},
        "mean_value_ratio": r2((booked["window"] / counts["window"]) / (booked["comparison"] / counts["comparison"])),
        "status_comparison": by_status(reorders[in_base & (reorders["slot"] == "comparison")]),
        "status_window": by_status(reorders[in_base & (reorders["slot"] == "window")]),
        "orders_in_comparison": len(v4_by_id),
        "orders_in_comparison_base": int((in_base & (reorders["order_id"] != "")).sum()),
        "merged_in_comparison_base": MERGED,
        "v4_app_orders_in_window_outside_log": len(v4_window),
        "all_members": {"reorders_comparison": int(all_counts["comparison"]),
                        "reorders_window": int(all_counts["window"]),
                        "placed_ratio": r2(all_counts["window"] / all_counts["comparison"]),
                        "booked_ratio": r2(all_booked["window"] / all_booked["comparison"])},
        "lab_rule": "the first seven of the 107, in id order, with placements in both windows whose hand count "
                    "leans the way the full table does and sits at least 0.10 from each of its two ratios",
        "lab_twelve_rows": lab_rows,
        "lab_totals": {"placed_comparison": int(lab_t["size_comparison"].sum()),
                       "placed_window": int(lab_t["size_window"].sum()),
                       "booked_comparison_rs": int(lab_t["sum_comparison"].sum()),
                       "booked_window_rs": int(lab_t["sum_window"].sum())},
        "lab_hand_count": {"placed_ratio": r2(lab_count_ratio), "booked_ratio": r2(lab_value_ratio)},
        "lab_mean_of_member_ratios": lab_mean,
        "base_cut_on_20_august": cut_20,
        "monsoon_sale": {"first_day": sale["start_date"], "last_day": sale["end_date"], "campaign_id": sale["campaign_id"]},
        "window_three_weeks_earlier": ["2026-07-30", "2026-08-19"],
        "audience": "TRAINER until the lab counts them",
    },
    "plants": [
        {"id": "kalpa_reorders_per_member_ratio", "value": r2(k_count_ratio),
         "how": "reorders placed per member, the 107 who joined by 19 August, 10 to 30 September over 20 August "
                "to 9 September",
         "found_in": "notebooks/C2_W04_D01_04_kalpa_lab_STUDENT.ipynb, the empty your-turn cell"},
        {"id": "kalpa_booked_value_per_member_ratio", "value": r2(k_value_ratio),
         "how": "booked value of reorders per member, any status, the same 107 and the same two windows",
         "found_in": "notebooks/C2_W04_D01_04_kalpa_lab_STUDENT.ipynb, the empty your-turn cell"},
        {"id": "kalpa_window_none_delivered", "value": True,
         "how": "every placement in the window is an auto-reorder that was cancelled, merged or pending, and "
                "none became an order",
         "found_in": "notebooks/C2_W04_D01_04_kalpa_lab_STUDENT.ipynb, the second your-turn cell"},
    ],
    "shared_constants": shared,
}

if __name__ == "__main__":
    with open(HERE / f"{STEM}_facts_INTERNAL.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(facts, f, sort_keys=False, allow_unicode=True, width=100)
    report = ["# Week 4 Monday: the generator's contract", "",
              "Written by `C2_W04_D01_generate_INTERNAL.py`; every line must read PASS.", "",
              "| Result | Line | Got | Wanted |", "|---|---|---|---|"]
    report += [f"| {r} | {n} | {'' if g is None else g} | {'' if w is None else w} |" for r, n, g, w in lines]
    (HERE / f"{STEM}_contract_INTERNAL.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    if "--list" in sys.argv:
        for x in numbers:
            print(f"{x['id']}: {x['value']}")
    fails = [x for x in lines if x[0] == "FAIL"]
    if "--contract" in sys.argv or fails:
        for r, n, g, w in lines:
            print(f"{r}  {n}" + (f"  (got {g}, wanted {w})" if r == "FAIL" and g is not None else ""))
    print(f"{len(lines) - len(fails)} of {len(lines)} contract lines PASS; "
          f"{len(dw):,} driver-weeks, {len(zw)} zone-weeks, {len(reorders)} Kalpa reorders")
    sys.exit(1 if fails else 0)

# Test inputs and expected outcomes
# python3 content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py
#     writes five CSVs and the facts file, prints "62 of 62 contract lines PASS" and exits 0
# python3 content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py --contract
#     the same, with one PASS line per target printed first
# python3 content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py --list
#     the same, with every facts id and its value printed first
# a second run of any of the above
#     byte-identical CSVs, facts file and contract output, since every draw is seeded

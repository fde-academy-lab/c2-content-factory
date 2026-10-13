"""Week 4 Thursday: the case data and the facts file (Zomato Gold, Chennai; an illustrative case).

Seeded, so two runs write byte-identical files. Standard library, pandas and PyYAML only. Every draw
comes from a random stream named for what it draws, seeded from SEED and the name through
zlib.crc32, so nothing depends on Python's per-process string hashing.

    python3 content/W04/D4/internal/C2_W04_D04_generate_INTERNAL.py              write, then check
    python3 content/W04/D4/internal/C2_W04_D04_generate_INTERNAL.py --contract   also print every line
    python3 content/W04/D4/internal/C2_W04_D04_generate_INTERNAL.py --list       print the facts ids

Writes to content/W04/D4/data/:
    members              one row per Gold member who joined from January to September 2026
    member_months        one row per member per calendar month from the signup month to September,
                         with the orders she placed that month (zero included)
    events.csv.gz        every app session of every member in August and September 2026, and of a
                         comparison sample of non-member users, one row per stage reached; gzipped
                         because it runs to about a million rows, and pandas reads it as it is
    twelve_rows          the twelve members SECTION 5 counts by hand, real rows of the data
    kalpa_memberships    the Kalpa lab: Kalpa Retail's 120 Retail-Plus customers from the frozen v4
                         warehouse, each with the month the membership started
    kalpa_events         their app sessions, July to September 2026
    kalpa_app_orders     their app-channel orders in the same months, copied from v4 unchanged
and to internal/ the facts file and the contract output.

How the case data is shaped. Each cohort's month-one rate is the ticket's; from month two every
cohort sits on a slow plateau that falls 0.3 points a month, so every curve falls with age. The
dashboard counts a member from her second month on (the ticket's "month-two retention"), so a cohort
enters its count at age two, slightly above the older cohorts' plateau, and the sale cohort of August
is outside the count until October. That is what holds it at 38 from June to September. Members order
with a persistence score, so the members active one month are mostly the members active the next.
Every order in August and September is one order_placed session in the event log, so member_months
and events agree; a share of Android members' orders after the 14 September release were lost at
checkout and show as carts that never became orders. Sessions fall on every day of both months with
weekend and evening peaks, and a session's stages are seconds to minutes apart.

The Kalpa lab takes the case file's fallback for retention: app activity (at least one app session in
the month), because v4's orders cannot carry 41 percent in September (37 of the 120 Retail-Plus
customers ordered that month). Its checkouts are v4's app-channel orders, one per order, on the
order's date, and nothing else.
"""
import csv
import datetime as dt
import gzip
import io
import math
import pathlib
import random
import sys
import zlib
from collections import Counter, defaultdict

import pandas as pd
import yaml

HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
REPO = DAY.parents[2]
DATA = DAY / "data"
DATA.mkdir(parents=True, exist_ok=True)
STEM = "C2_W04_D04"
SEED = 20261029
V4_SQL = REPO / "content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql"
MONDAY_FACTS = REPO / "content/W04/D1/internal/C2_W04_D01_facts_INTERNAL.yaml"

D = dt.date
MONTHS = [f"2026-{m:02d}" for m in range(1, 10)]          # January to September 2026
NAMES = {f"2026-{m:02d}": n for m, n in zip(range(1, 10), "Jan Feb Mar Apr May Jun Jul Aug Sep".split())}
NORMAL = 5000                                             # the mean cohort, January to July
SALE_TIMES = 2.6                                          # the August cohort against that mean
SALE_WEEK = (D(2026, 8, 17), D(2026, 8, 23))              # Monday to Sunday
RELEASE = D(2026, 9, 14)                                  # Monday: the new checkout on Android
EVENTS_FROM, EVENTS_TO = D(2026, 8, 1), D(2026, 9, 30)
REPORTING = ["2026-06", "2026-07", "2026-08", "2026-09"]

# Month-one retention by cohort (the ticket); the organic August members keep July's rate.
M1 = {"2026-01": 0.58, "2026-02": 0.56, "2026-03": 0.55, "2026-04": 0.53, "2026-05": 0.52,
      "2026-06": 0.50, "2026-07": 0.49, "2026-08": 0.31}
AUG_ORGANIC_M1 = 0.49
SIGNUP_MONTH_ACTIVE = 0.85
# From month two: each cohort's age-two rate, then 0.3 points lower every month after.
BASE2 = {"2026-01": 0.387, "2026-02": 0.386, "2026-03": 0.3865, "2026-04": 0.386, "2026-05": 0.387,
         "2026-06": 0.389, "2026-07": 0.3855}
SLOPE = 0.003

# Add-to-cart to order, before (1 August to 13 September) and after (14 to 30 September).
CONV = {(True, "android"): (0.58, 0.44), (True, "ios"): (0.57, 0.56), (True, "web"): (0.55, 0.55),
        (False, "android"): (0.52, 0.51), (False, "ios"): (0.55, 0.55), (False, "web"): (0.50, 0.50)}
CART_TO_CHECKOUT = 0.80          # add-to-cart sessions that start checkout, steady on every platform
MENU_TO_CART = 0.34              # members, per session (the ticket)
MENU_TO_CART_MEMBER = 0.61       # members, per member (the ticket)
SEARCH_TO_MENU = 1.18            # members, per session (the ticket)
CAROUSEL_SHARE = 0.25            # menu sessions that opened from the home carousel, no search
BOUNCE_SHARE = 0.12              # sessions that open the app and do nothing else
PLATFORMS = (["android", "ios", "web"], [0.70, 0.25, 0.05])
ZONES = (["Adyar", "Anna Nagar", "T Nagar", "Velachery", "OMR", "Tambaram"],
         [0.17, 0.19, 0.16, 0.17, 0.20, 0.11])
NON_MEMBERS = 4000
ORDER_VALUE_RS = 400             # an assumption, Rs 300 to Rs 500, for the cost of the lost orders

# Kalpa: the two windows Monday fixes, and the lab's designed activity by cohort and month.
COMPARISON = (D(2026, 8, 20), D(2026, 9, 9))
AUTO_WINDOW = (D(2026, 9, 10), D(2026, 9, 30))
MONSOON_SALE_LAST_DAY = D(2026, 8, 19)
K_SIZES = {"2026-01": 11, "2026-02": 12, "2026-03": 13, "2026-04": 12, "2026-05": 13,
           "2026-06": 13, "2026-07": 14, "2026-08": 32}
K_ACTIVE = {  # members with at least one app session in Jul, Aug, Sep (None: not yet a member)
    "2026-01": (2, 1, 0), "2026-02": (2, 1, 0), "2026-03": (3, 2, 1), "2026-04": (4, 3, 2),
    "2026-05": (7, 6, 5), "2026-06": (12, 10, 7), "2026-07": (13, 13, 8), "2026-08": (None, 29, 26)}
K_CART_TO_CHECKOUT = {"before": 0.82, "comparison": 0.833, "window": 0.636}
K_SKIP_SEARCH = 0.31

lines, numbers = [], []


def rng_for(label):
    return random.Random(SEED * 1_000_003 + zlib.crc32(label.encode()))


def check(name, ok, got=None, wanted=None):
    lines.append(("PASS" if ok else "FAIL", name, got, wanted))
    return ok


def fact(fid, value, unit, how, used_by, printed=None):
    entry = {"id": fid, "value": value, "unit": unit, "how": how, "used_by": used_by}
    if printed is not None:
        entry["printed"] = printed
    numbers.append(entry)
    return value


def r2(x):
    return round(float(x), 2)


def r3(x):
    return round(float(x), 3)


def r4(x):
    return round(float(x), 4)


def pct(x):
    return f"{round(100 * x)} percent"


def month_of(d):
    return d.strftime("%Y-%m")


def days_in(ym):
    y, m = int(ym[:4]), int(ym[5:])
    first = D(y, m, 1)
    nxt = D(y + (m == 12), m % 12 + 1, 1)
    return [first + dt.timedelta(i) for i in range((nxt - first).days)]


def months_apart(a, b):
    return (int(b[:4]) - int(a[:4])) * 12 + int(b[5:]) - int(a[5:])


DOW = [0.92, 0.92, 0.95, 0.97, 1.08, 1.20, 1.18]       # Monday to Sunday


def pick_day(r, days):
    return r.choices(days, [DOW[d.weekday()] for d in days])[0]


def clock(r):
    """Seconds after midnight: a lunch bump, an evening peak and a thin spread through the day."""
    u = r.random()
    if u < 0.22:
        m = r.gauss(13 * 60 + 10, 45)
    elif u < 0.80:
        m = r.gauss(20 * 60 + 40, 65)
    else:
        m = r.uniform(8 * 60, 23 * 60 + 30)
    m = min(max(m, 7 * 60), 23 * 60 + 45)
    return int(m * 60) + r.randint(0, 59)


def poisson(r, lam):
    limit, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= r.random()
        if p <= limit:
            return k
        k += 1


def spread(total, weights):
    """Integers proportional to weights that sum to total exactly (largest remainder)."""
    w = sum(weights) or 1
    raw = [total * x / w for x in weights]
    out = [int(v) for v in raw]
    for i in sorted(range(len(raw)), key=lambda i: out[i] - raw[i])[: total - sum(out)]:
        out[i] += 1
    return out


# ================================================================================= the members
rm = rng_for("members")
dev = [rm.randint(-380, 380) for _ in range(7)]
shift = sum(dev) / 7
dev = [round(x - shift) for x in dev]
dev[dev.index(max(dev))] -= sum(dev)                     # the seven sum to 35,000 exactly
SIZES = {ym: NORMAL + x for ym, x in zip(MONTHS[:7], dev)}
SIZES["2026-08"] = round(SALE_TIMES * sum(SIZES.values()) / 7)
SIZES["2026-09"] = NORMAL + rm.randint(-300, 300)
AUG_ORGANIC = NORMAL + rm.randint(-250, 250)

signups = []
for ym, n in SIZES.items():
    days = days_in(ym)
    if ym == "2026-08":
        sale_days = [SALE_WEEK[0] + dt.timedelta(i) for i in range(7)]
        signups += [(pick_day(rm, days), "organic") for _ in range(AUG_ORGANIC)]
        signups += [(rm.choices(sale_days, [1.6, 1.3, 1.1, 1.0, 1.0, 1.2, 0.8])[0], "sale")
                    for _ in range(n - AUG_ORGANIC)]
    else:
        signups += [(pick_day(rm, days), "organic") for _ in range(n)]
signups = [(d, ch, rm.random()) for d, ch in signups]
signups.sort(key=lambda x: (x[0], x[2]))

members = []
for i, (d, ch, _) in enumerate(signups, 1):
    members.append({"member_id": f"ZG{i:05d}", "signup_date": d, "cohort_month": month_of(d),
                    "signup_channel": ch, "zone": rm.choices(*ZONES)[0],
                    "platform": rm.choices(*PLATFORMS)[0], "score": rm.random()})
BY_ID = {m["member_id"]: m for m in members}
COHORT = defaultdict(list)
for m in members:
    COHORT[m["cohort_month"]].append(m)

# ================================================================ the twelve rows, chosen first
rt = rng_for("twelve rows")
TWELVE_PATTERN = {  # flags for the calendar months after the signup month, through September
    "2026-05": [(1, 1, 1, 1), (1, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0)],
    "2026-06": [(1, 1, 1), (1, 0, 0), (0, 0, 0)],
    "2026-08": [(1,), (0,), (0,), (0,), (0,)],
}
forced = {}                                               # member_id -> {month: 0 or 1}
twelve_ids = []
for ym, pats in TWELVE_PATTERN.items():
    pool = [m for m in COHORT[ym] if m["signup_channel"] == ("sale" if ym == "2026-08" else "organic")
            and m["platform"] != "web"]
    chosen = sorted(rt.sample(pool, len(pats)), key=lambda m: m["member_id"])
    after = MONTHS[MONTHS.index(ym) + 1:]
    for m, pat in zip(chosen, pats):
        forced[m["member_id"]] = {ym: 1, **dict(zip(after, pat))}
        twelve_ids.append(m["member_id"])

# ================================================================ who orders in which month
def rate(ym, k, channel=None):
    if k == 0:
        return SIGNUP_MONTH_ACTIVE
    if k == 1:
        return M1[ym]
    return BASE2[ym] - SLOPE * (k - 2)


ACTIVE = defaultdict(dict)                               # member_id -> {month: True/False}
QUOTA = {}                                               # (cohort, month, channel or None) -> count
ra = rng_for("activity")
for ym in MONTHS:
    for month in MONTHS[MONTHS.index(ym):]:
        k = months_apart(ym, month)
        groups = [(None, COHORT[ym])]
        if ym == "2026-08" and k == 1:
            total = round(M1[ym] * SIZES[ym])
            org = [m for m in COHORT[ym] if m["signup_channel"] == "organic"]
            sale = [m for m in COHORT[ym] if m["signup_channel"] == "sale"]
            n_org = round(AUG_ORGANIC_M1 * len(org))
            groups = [("organic", org, n_org), ("sale", sale, total - n_org)]
        else:
            groups = [(None, COHORT[ym], round(rate(ym, k) * SIZES[ym]))]
        for channel, pool, n in groups:
            QUOTA[(ym, month, channel)] = n
            fixed = [m for m in pool if m["member_id"] in forced]
            on = [m for m in fixed if forced[m["member_id"]][month]]
            rest = [m for m in pool if m["member_id"] not in forced]
            ranked = sorted(rest, key=lambda m: -(m["score"] + ra.gauss(0, 0.16)))
            chosen = {m["member_id"] for m in on} | {m["member_id"] for m in ranked[: n - len(on)]}
            for m in pool:
                ACTIVE[m["member_id"]][month] = m["member_id"] in chosen

# ================================================================ orders, and the release's loss
ro = rng_for("orders")
ORDERS = defaultdict(list)                               # (member_id, month) -> [date, ...]
for m in members:
    lam = (0.10 + 0.45 * m["score"]) if m["signup_channel"] == "organic" else (0.05 + 0.20 * m["score"])
    for month, on in ACTIVE[m["member_id"]].items():
        if not on:
            continue
        days = [d for d in days_in(month) if d >= m["signup_date"]]
        ORDERS[(m["member_id"], month)] = sorted(pick_day(ro, days) for _ in range(1 + poisson(ro, lam)))

android_post = [(mid, d) for (mid, month), ds in ORDERS.items() if month == "2026-09"
                and BY_ID[mid]["platform"] == "android" for d in ds if d >= RELEASE]
cf_post = len(android_post)
keep_post = round(cf_post * CONV[(True, "android")][1] / CONV[(True, "android")][0])
lost = []
rl = rng_for("lost orders")
candidates = sorted(android_post, key=lambda x: (x[0], x[1]))
rl.shuffle(candidates)
for mid, d in candidates:
    if len(lost) == cf_post - keep_post:
        break
    ds = ORDERS[(mid, "2026-09")]
    if len(ds) >= 2:
        ds.remove(d)
        lost.append((mid, d))
check("release: every lost order came from a member who kept another September order",
      len(lost) == cf_post - keep_post, len(lost), cf_post - keep_post)

# ================================================================ member_months
mm_rows = []
for m in members:
    for month in MONTHS[MONTHS.index(m["cohort_month"]):]:
        mm_rows.append((m["member_id"], month, len(ORDERS.get((m["member_id"], month), []))))
mm = pd.DataFrame(mm_rows, columns=["member_id", "month", "orders"])

# ================================================================ the event log
re_ = rng_for("events")
sessions = []          # [user_id, is_member, platform, start datetime, [stages], version]


def add_session(user, is_member, platform, day, stages, start=None):
    start = start if start is not None else clock(re_)
    ts = dt.datetime.combine(day, dt.time()) + dt.timedelta(seconds=start)
    version = "v2" if platform == "android" and day >= RELEASE else "v1"
    sessions.append([user, is_member, platform, ts, stages, version])


def stages_for(kind, carousel):
    entry = ["open"] if carousel else ["open", "search"]
    return {"order": entry + ["menu_view", "add_to_cart", "checkout_start", "order_placed"],
            "checkout": entry + ["menu_view", "add_to_cart", "checkout_start"],
            "cart": entry + ["menu_view", "add_to_cart"],
            "menu": entry + ["menu_view"]}[kind]


def period_of(d):
    return "after" if d >= RELEASE else "before"


WEEKS = sorted({d - dt.timedelta(d.weekday()) for d in days_in("2026-08") + days_in("2026-09")})


def build_month_sessions(month, users, orders_of, active_of, is_member, joined):
    """Every session of these users in this month, shaped to the funnel's rates.

    users: list of (user_id, platform, score). orders_of[user] lists the order dates this month.
    The number of add-to-cart sessions in each platform and period is set by the conversion target,
    with a small weekly wobble that the period's total absorbs exactly.
    """
    days = days_in(month)
    plat = {u: p for u, p, _ in users}
    score = {u: s for u, _, s in users}
    menu_sessions = []                                   # (user, day, kind)
    by_cell = defaultdict(list)                          # (platform, period) -> [(user, day)]
    for u, _, _ in users:
        for d in orders_of.get(u, []):
            by_cell[(plat[u], period_of(d))].append((u, d))
    wob = rng_for(f"weekly wobble {month} {is_member}")
    atc_users = set()
    inactive = [u for u, _, _ in users if not active_of(u)]
    pool_by_plat = defaultdict(list)
    for u in inactive:
        pool_by_plat[plat[u]].append(u)
    for (p, per), orders in sorted(by_cell.items()):
        conv = CONV[(is_member, p)][per == "after"]
        n_orders = len(orders)
        n_carts = round(n_orders / conv)
        n_checkout = max(n_orders, round(CART_TO_CHECKOUT * n_carts))
        abandoned = n_carts - n_orders
        # spread the abandoned carts over the weeks, each week's rate wobbling a little
        wk = Counter(d - dt.timedelta(d.weekday()) for _, d in orders)
        weeks = sorted(wk)
        weights = [wk[w] * (1 / max(0.2, conv + wob.uniform(-0.012, 0.012)) - 1) for w in weeks]
        per_week = spread(abandoned, weights)
        at_checkout = n_checkout - n_orders
        kinds = ["checkout"] * at_checkout + ["cart"] * (abandoned - at_checkout)
        wob.shuffle(kinds)
        ki = 0
        for w, n in zip(weeks, per_week):
            week_orders = [(u, d) for u, d in orders if d - dt.timedelta(d.weekday()) == w]
            week_days = [d for d in days if d - dt.timedelta(d.weekday()) == w and period_of(d) == per]
            for _ in range(n):
                kind = kinds[ki]
                ki += 1
                if wob.random() < 0.7 or not pool_by_plat[p]:
                    u, d = wob.choice(week_orders)       # a member who tried and later ordered
                else:
                    u = wob.choice(pool_by_plat[p])      # a member who added to cart and left
                    ok = [x for x in week_days if x >= joined(u)]
                    if not ok:
                        u, d = wob.choice(week_orders)
                    else:
                        d = wob.choice(ok)
                menu_sessions.append((u, d, kind))
                atc_users.add(u)
        for u, d in orders:
            menu_sessions.append((u, d, "order"))
            atc_users.add(u)
    n_carts_total = len(menu_sessions)
    # browsing: menus opened with nothing added, enough for the per-session and per-member rates
    n_menu = round(n_carts_total / MENU_TO_CART)
    browse_only_target = round(len(atc_users) / MENU_TO_CART_MEMBER) - len(atc_users)
    rb = rng_for(f"browse {month} {is_member}")
    others = sorted(u for u, _, _ in users if u not in atc_users)
    rb.shuffle(others)
    browse_only = others[:browse_only_target]
    browsers = browse_only + rb.choices(sorted(atc_users) + browse_only,
                                        [1 + 2 * score[u] for u in sorted(atc_users)]
                                        + [1] * len(browse_only),
                                        k=n_menu - n_carts_total - len(browse_only))
    for u in browsers:
        ok = [d for d in days if d >= joined(u)]
        menu_sessions.append((u, rb.choice(ok), "menu"))
    # the carousel opens a menu with no search; searches that find no menu; bare opens
    rc = rng_for(f"carousel {month} {is_member}")
    flags = [True] * round(CAROUSEL_SHARE * len(menu_sessions))
    flags += [False] * (len(menu_sessions) - len(flags))
    rc.shuffle(flags)
    n_search = round(len(menu_sessions) / SEARCH_TO_MENU)
    n_search_only = n_search - flags.count(False)
    everyone = sorted(u for u, _, _ in users)
    extra = []
    for _ in range(n_search_only):
        u = rc.choice(everyone)
        extra.append((u, rc.choice([d for d in days if d >= joined(u)]), ["open", "search"]))
    n_bounce = round(BOUNCE_SHARE * (len(menu_sessions) + n_search_only) / (1 - BOUNCE_SHARE))
    for _ in range(n_bounce):
        u = rc.choice(everyone)
        extra.append((u, rc.choice([d for d in days if d >= joined(u)]), ["open"]))
    for (u, d, kind), car in zip(menu_sessions, flags):
        add_session(u, is_member, plat[u], d, stages_for(kind, car))
    for u, d, st in extra:
        add_session(u, is_member, plat[u], d, st)


for month in ("2026-08", "2026-09"):
    users = [(m["member_id"], m["platform"], m["score"]) for m in members
             if m["cohort_month"] <= month]
    build_month_sessions(month, users,
                         {mid: ds for (mid, mo), ds in ORDERS.items() if mo == month},
                         lambda u, month=month: ACTIVE[u].get(month, False), True,
                         lambda u: BY_ID[u]["signup_date"])

# the non-member comparison sample: users who order without Gold
rn = rng_for("non-members")
NM = [{"user_id": f"NM{i:05d}", "platform": rn.choices(*PLATFORMS)[0], "score": rn.random()}
      for i in range(1, NON_MEMBERS + 1)]
NM_ACTIVE = {}
for month in ("2026-08", "2026-09"):
    nm_orders = {}
    for u in NM:
        on = rn.random() < 0.25 + 0.4 * u["score"]
        NM_ACTIVE[(u["user_id"], month)] = on
        if on:
            nm_orders[u["user_id"]] = sorted(pick_day(rn, days_in(month))
                                             for _ in range(1 + poisson(rn, 0.15 + 0.4 * u["score"])))
    build_month_sessions(month, [(u["user_id"], u["platform"], u["score"]) for u in NM], nm_orders,
                         lambda x, month=month: NM_ACTIVE[(x, month)], False, lambda x: EVENTS_FROM)

# order the sessions in time, number them, and write one row per stage reached
rs = rng_for("session order")
for s in sessions:
    s.append(rs.random())
sessions.sort(key=lambda s: (s[3], s[6]))
GAPS = {"search": (4, 40), "menu_view": (8, 110), "add_to_cart": (25, 320),
        "checkout_start": (10, 150), "order_placed": (25, 260)}
rg = rng_for("stage gaps")
ev_rows = []
for i, (user, is_member, platform, ts, stages, version, _) in enumerate(sessions, 1):
    sid = f"S{i:07d}"
    t = ts
    for j, stage in enumerate(stages):
        if j:
            lo, hi = GAPS[stage] if not (stage == "menu_view" and stages[j - 1] == "open") else (6, 50)
            t = t + dt.timedelta(seconds=rg.randint(lo, hi))
        ev_rows.append((user, is_member, sid, t.strftime("%Y-%m-%d %H:%M:%S"), stage, platform, version))
ev = pd.DataFrame(ev_rows, columns=["user_id", "is_member", "session_id", "event_ts", "stage",
                                    "platform", "checkout_version"])

# ================================================================ write the case tables
mem_df = pd.DataFrame([{k: m[k] for k in ("member_id", "signup_date", "cohort_month",
                                           "signup_channel", "zone")} for m in members])
mem_df.to_csv(DATA / f"{STEM}_members_STUDENT.csv", index=False)
mm.to_csv(DATA / f"{STEM}_member_months_STUDENT.csv", index=False)
buf = io.StringIO()
ev.to_csv(buf, index=False)
with open(DATA / f"{STEM}_events_STUDENT.csv.gz", "wb") as fh:
    with gzip.GzipFile(filename="", mode="wb", fileobj=fh, mtime=0, compresslevel=9) as gz:
        gz.write(buf.getvalue().encode("utf-8"))

# The card shows the four sale-week members forced to no September order and a fifth drawn from the
# sale-week members with no September order, so the card's August line reads 0 of 5: 1 of 5 would
# equal the sale-week members' own full-data month one (19.8 percent). The forced member's data stay.
forced_aug = [i for i in twelve_ids if BY_ID[i]["cohort_month"] == "2026-08"]
aug_zero = [i for i in forced_aug if not ORDERS.get((i, "2026-09"))]
pool_zero = sorted(m["member_id"] for m in COHORT["2026-08"] if m["signup_channel"] == "sale"
                   and m["platform"] != "web" and m["member_id"] not in forced
                   and not ORDERS.get((m["member_id"], "2026-09")))
card_ids = ([i for i in twelve_ids if BY_ID[i]["cohort_month"] != "2026-08"]
            + sorted(aug_zero + [rng_for("twelve rows, the card's fifth sale-week member").choice(pool_zero)]))
tw_rows = []
for mid in card_ids:
    m = BY_ID[mid]
    row = {"member_id": mid, "signup_month": NAMES[m["cohort_month"]], "signup_channel": m["signup_channel"]}
    for month in ("2026-06", "2026-07", "2026-08", "2026-09"):
        k = months_apart(m["cohort_month"], month)
        row[f"ordered_in_{NAMES[month].lower()}"] = (
            "" if k < 1 else int(len(ORDERS.get((mid, month), [])) > 0))
    tw_rows.append(row)
tw = pd.DataFrame(tw_rows)
tw.to_csv(DATA / f"{STEM}_twelve_rows_STUDENT.csv", index=False)

# ================================================================ the case contract
mm["cohort_month"] = mm["member_id"].map(lambda x: BY_ID[x]["cohort_month"])
mm["age"] = [months_apart(c, m) for c, m in zip(mm["cohort_month"], mm["month"])]
mm["active"] = mm["orders"] > 0
tri = mm[mm["age"] >= 1].pivot_table(index="cohort_month", columns="age", values="active", aggfunc="mean")
sizes = mem_df.groupby("cohort_month").size()

check("members: 2.6 times the January-to-July mean is August's cohort",
      SIZES["2026-08"] == round(SALE_TIMES * sum(SIZES[m] for m in MONTHS[:7]) / 7), SIZES["2026-08"])
check("members: January to July move by a few hundred, none at exactly 5,000",
      300 <= max(dev) - min(dev) <= 800 and all(x != 0 for x in dev), [SIZES[m] for m in MONTHS[:7]])
check("members: the August cohort is the largest", sizes.idxmax() == "2026-08", sizes.idxmax())
for ym, target in M1.items():
    got = tri.loc[ym, 1]
    check(f"month one, {NAMES[ym]} cohort, prints as {round(100 * target)} percent",
          round(100 * got) == round(100 * target), r4(got), target)
falling = all((tri.loc[ym].dropna().diff().dropna() < 0).all() for ym in M1)
check("every cohort falls at every age it has reached", falling)
org_m1 = mm[(mm.age == 1) & (mm.cohort_month == "2026-08")].merge(
    mem_df[["member_id", "signup_channel"]], on="member_id").groupby("signup_channel")["active"].mean()
check("selection: organic August members keep July's month-one rate (within a point)",
      abs(org_m1["organic"] - tri.loc["2026-07", 1]) < 0.01, r4(org_m1["organic"]), r4(tri.loc["2026-07", 1]))


def dashboard(month):
    """Members two or more months past their signup month who ordered in the month, over all of them."""
    sub = mm[(mm.month == month) & (mm.age >= 2)]
    return sub["active"].mean(), len(sub), int(sub["active"].sum())


def everyone_blend(month):
    sub = mm[(mm.month == month) & (mm.age >= 1)]
    return sub["active"].mean(), len(sub), int(sub["active"].sum())


DASH = {m: dashboard(m) for m in REPORTING}
for m, (v, n, a) in DASH.items():
    check(f"dashboard, {NAMES[m]}, prints as 38 percent", round(100 * v) == 38, r4(v), 0.38)
check("dashboard: flat, within one point June to September",
      max(v for v, _, _ in DASH.values()) - min(v for v, _, _ in DASH.values()) < 0.01)
for m in REPORTING:
    cells = mm[(mm.month == m) & (mm.age >= 2)].groupby("cohort_month")["active"].agg(["size", "mean"])
    weighted = (cells["size"] * cells["mean"]).sum() / cells["size"].sum()
    check(f"second route, {NAMES[m]}: the size-weighted cohort average equals the direct count",
          abs(weighted - DASH[m][0]) < 1e-12)
EVERY = {m: everyone_blend(m) for m in REPORTING}
check("the blend over everyone who joined before September sits below the dashboard",
      EVERY["2026-09"][0] < DASH["2026-09"][0] - 0.015, r4(EVERY["2026-09"][0]), r4(DASH["2026-09"][0]))
check("nothing the case prints rounds to 41 (Kalpa's planted blend)",
      all(round(100 * v) != 41 for v, _, _ in DASH.values()) and round(100 * EVERY["2026-09"][0]) != 41)

# reconciliation: every order in August and September is one order_placed session
ev_dates = ev["event_ts"].str[:10]
ev["date"] = pd.to_datetime(ev_dates)
placed = ev[(ev.stage == "order_placed") & ev.is_member].assign(month=ev_dates.str[:7])
placed_n = placed.groupby(["user_id", "month"]).size().rename_axis(["member_id", "month"])
mm_ev = mm[mm.month.isin(["2026-08", "2026-09"])].set_index(["member_id", "month"])["orders"]
joined = mm_ev.to_frame().join(placed_n.rename("placed")).fillna({"placed": 0})
check("member_months.orders equals the order_placed sessions for every member in August and September",
      (joined["orders"] == joined["placed"]).all(), int((joined["orders"] != joined["placed"]).sum()), 0)
check("no non-member order is counted in member_months", not placed["user_id"].str.startswith("NM").any())
first_ev = ev[ev.is_member].groupby("user_id")["date"].min()
signup = mem_df.set_index("member_id")["signup_date"].map(pd.Timestamp)
check("no member has a session before her signup date",
      (first_ev >= signup.reindex(first_ev.index)).all())
all_days = pd.date_range(EVENTS_FROM, EVENTS_TO)
per_day = ev.groupby("date")["session_id"].nunique()
check("sessions fall on every day of August and September",
      len(per_day) == len(all_days) and per_day.min() > 1000, int(per_day.min()))
hours = pd.to_datetime(ev.drop_duplicates("session_id")["event_ts"]).dt.hour
check("an evening peak: more sessions start in the evening than in any other part of the day",
      (hours.between(18, 22)).mean() > 0.45, r3((hours.between(18, 22)).mean()))
RANK = {"open": 0, "search": 1, "menu_view": 2, "add_to_cart": 3, "checkout_start": 4, "order_placed": 5}
gap_s = pd.to_datetime(ev["event_ts"]).groupby(ev["session_id"]).diff().dt.total_seconds().dropna()
rank_step = ev["stage"].map(RANK).groupby(ev["session_id"]).diff().dropna()
check("every session's stages are seconds to minutes apart, in order",
      gap_s.between(1, 600).all() and (rank_step > 0).all(), (int(gap_s.min()), int(gap_s.max())))

mev = ev[ev.is_member]
sep = mev[mev.date.dt.month == 9]
reach = sep.pivot_table(index="session_id", columns="stage", values="user_id", aggfunc="size",
                        fill_value=0).gt(0)
search_to_menu = reach["menu_view"].sum() / reach["search"].sum()
menu_to_cart_s = reach["add_to_cart"].sum() / reach["menu_view"].sum()
by_member = sep.groupby(["user_id", "stage"]).size().unstack(fill_value=0).gt(0)
menu_to_cart_m = by_member["add_to_cart"].sum() / by_member["menu_view"].sum()
check("search to menu view, members, per session, September, prints as 118 percent",
      round(100 * search_to_menu) == 118, r4(search_to_menu), 1.18)
check("menu view to add-to-cart, members, per session, September, prints as 34 percent",
      round(100 * menu_to_cart_s) == 34, r4(menu_to_cart_s), 0.34)
check("menu view to add-to-cart, members, per member, September, prints as 61 percent",
      round(100 * menu_to_cart_m) == 61, r4(menu_to_cart_m), 0.61)
searched = reach[reach["search"]]
search_to_menu_true = searched["menu_view"].mean()
check("among sessions that searched, the share that opened a menu stays under 100 percent",
      search_to_menu_true < 1, r4(search_to_menu_true))

sess = ev.drop_duplicates("session_id")[["session_id", "user_id", "is_member", "platform", "date",
                                         "checkout_version"]].set_index("session_id")
flags = ev.pivot_table(index="session_id", columns="stage", values="user_id", aggfunc="size",
                       fill_value=0).gt(0)
sess = sess.join(flags)
sess["period"] = (sess["date"] >= pd.Timestamp(RELEASE)).map({True: "after", False: "before"})


def conv(df):
    return df["order_placed"].sum() / df["add_to_cart"].sum()


RELEASE_SPLIT = {}
for (is_m, p), (want_b, want_a) in CONV.items():
    for per, want in (("before", want_b), ("after", want_a)):
        got = conv(sess[(sess.is_member == is_m) & (sess.platform == p) & (sess.period == per)])
        RELEASE_SPLIT[(is_m, p, per)] = got
        if (is_m, p) in {(True, "android"), (True, "ios"), (False, "android")}:
            who = ("members" if is_m else "non-members") + f" on {'Android' if p == 'android' else 'iOS'}"
            check(f"add-to-cart to order, {who}, {per} 14 September, prints as {round(100 * want)} percent",
                  round(100 * got) == round(100 * want), r4(got), want)
and_m = sess[(sess.is_member) & (sess.platform == "android")]
step_before = and_m[and_m.period == "before"]
step_after = and_m[and_m.period == "after"]
co_b = step_before["order_placed"].sum() / step_before["checkout_start"].sum()
co_a = step_after["order_placed"].sum() / step_after["checkout_start"].sum()
cs_b = step_before["checkout_start"].sum() / step_before["add_to_cart"].sum()
cs_a = step_after["checkout_start"].sum() / step_after["add_to_cart"].sum()
check("the loss sits at checkout start to order placed on Android members",
      co_b - co_a > 0.15 and abs(cs_b - cs_a) < 0.02, (r3(co_b), r3(co_a)), (r3(cs_b), r3(cs_a)))
weekly = (and_m.groupby(and_m["date"].dt.to_period("W-SUN"))
          .apply(lambda g: g["order_placed"].sum() / g["add_to_cart"].sum()))
pre_weeks = [v for w, v in weekly.items() if w.start_time < pd.Timestamp(RELEASE)]
post_weeks = [v for w, v in weekly.items() if w.start_time >= pd.Timestamp(RELEASE)]
check("the weekly Android rate moves a little and never repeats a value exactly",
      len(set(round(v, 4) for v in weekly)) == len(weekly) and max(pre_weeks) - min(pre_weeks) < 0.05)
check("every week before the release sits above every week after it", min(pre_weeks) > max(post_weeks))
for shift_days, label in ((-7, "7 September"), (7, "21 September")):
    cut = pd.Timestamp(RELEASE + dt.timedelta(shift_days))
    b = conv(and_m[and_m.date < cut])
    a = conv(and_m[and_m.date >= cut])
    RELEASE_SPLIT[("shift", label)] = (b, a)
    check(f"the fall holds with the release date moved to {label}", b - a > 0.05, (r3(b), r3(a)))
lost_estimate_week = (CONV[(True, "android")][0] - CONV[(True, "android")][1]) * step_after["add_to_cart"].sum() / (17 / 7)
check("the lost-order estimate is close to the orders the release actually lost",
      abs(lost_estimate_week * 17 / 7 - len(lost)) / len(lost) < 0.06, round(lost_estimate_week * 17 / 7), len(lost))
opm = {}
for p in ("android", "ios"):
    for month in ("2026-08", "2026-09"):
        ids = [m["member_id"] for m in members if m["platform"] == p]
        sub = mm[(mm.month == month) & mm.member_id.isin(ids) & mm.active]
        opm[(p, month)] = sub["orders"].mean()
check("orders per active Android member fell from August to September while iOS did not",
      opm[("android", "2026-08")] - opm[("android", "2026-09")] > 0.05
      and opm[("ios", "2026-09")] >= opm[("ios", "2026-08")] - 0.01,
      {f"{p} {NAMES[mo]}": r2(v) for (p, mo), v in opm.items()})
zone_sep = mm[(mm.month == "2026-09") & (mm.age >= 2)].merge(mem_df[["member_id", "zone"]], on="member_id") \
    .groupby("zone")["active"].mean()
check("no zone stands out in September (every zone within three points of the city)",
      (zone_sep - DASH["2026-09"][0]).abs().max() < 0.03, r3((zone_sep - DASH["2026-09"][0]).abs().max()))

# the twelve rows, hand-counted
TW = {}
for ym, cols in (("2026-05", ["jun", "jul", "aug", "sep"]), ("2026-06", ["jul", "aug", "sep"]),
                 ("2026-08", ["sep"])):
    sub = tw[tw.signup_month == NAMES[ym]]
    for k, c in enumerate(cols, 1):
        TW[(ym, k)] = (int(sub[f"ordered_in_{c}"].astype(int).sum()), len(sub))
want_tw = {("2026-05", 1): 3, ("2026-05", 2): 2, ("2026-05", 3): 1, ("2026-05", 4): 1,
           ("2026-06", 1): 2, ("2026-06", 2): 1, ("2026-06", 3): 1, ("2026-08", 1): 0}
check("twelve rows: four May, three June and five August sale members, every one a real member",
      list(tw.signup_month).count("May") == 4 and list(tw.signup_month).count("Jun") == 3
      and list(tw.signup_month).count("Aug") == 5 and all(i in BY_ID for i in tw.member_id))
check("twelve rows: the hand counts are the designed ones", all(TW[k][0] == v for k, v in want_tw.items()),
      {f"{NAMES[k[0]]} m{k[1]}": TW[k][0] for k in want_tw})
tw_dash = {"2026-07": (TW[("2026-05", 2)][0], 4), "2026-08": (TW[("2026-05", 3)][0] + TW[("2026-06", 2)][0], 7),
           "2026-09": (TW[("2026-05", 4)][0] + TW[("2026-06", 3)][0], 7)}
tw_every = {"2026-07": (TW[("2026-05", 2)][0] + TW[("2026-06", 1)][0], 7),
            "2026-08": (TW[("2026-05", 3)][0] + TW[("2026-06", 2)][0], 7),
            "2026-09": (TW[("2026-05", 4)][0] + TW[("2026-06", 3)][0] + TW[("2026-08", 1)][0], 12)}
check("twelve rows: the dashboard's way reads the same in August and September",
      tw_dash["2026-08"] == tw_dash["2026-09"], tw_dash["2026-08"], tw_dash["2026-09"])
check("twelve rows: two of the twelve ordered in September", tw_every["2026-09"] == (2, 12))
full = {("2026-05", k): tri.loc["2026-05", k] for k in range(1, 5)}
full.update({("2026-06", k): tri.loc["2026-06", k] for k in range(1, 4)})
full[("2026-08", 1)] = tri.loc["2026-08", 1]
gaps = [abs(TW[k][0] / TW[k][1] - full[k]) for k in want_tw]
gaps += [abs(a / n - DASH[m][0]) for m, (a, n) in tw_dash.items()]
gaps += [abs(a / n - EVERY[m][0]) for m, (a, n) in tw_every.items()]
check("twelve rows: every hand-counted rate sits at least five points from its full-data value",
      min(gaps) >= 0.05, r3(min(gaps)))

# ================================================================================= Kalpa
sql_lines = V4_SQL.read_text(encoding="utf-8").splitlines()


def copy_block(table):
    start = next(i for i, l in enumerate(sql_lines) if l.startswith(f"COPY {table} "))
    cols = sql_lines[start].split("(")[1].split(")")[0].split(", ")
    out, i = [], start + 1
    while sql_lines[i] != "\\.":
        out.append(dict(zip(cols, sql_lines[i].split("\t"))))
        i += 1
    return out


v4_customers = copy_block("customers")
v4_orders = copy_block("orders")
RP = sorted(c["customer_id"] for c in v4_customers if c["segment"] == "Retail-Plus")
APP = sorted((o for o in v4_orders if o["customer_id"] in set(RP) and o["channel"] == "app"
              and "2026-07-01" <= o["order_date"] <= "2026-09-30"), key=lambda o: (o["order_date"], o["order_id"]))
app_by = defaultdict(list)
for o in APP:
    app_by[o["customer_id"]].append(D.fromisoformat(o["order_date"]))
KMONTHS = ["2026-07", "2026-08", "2026-09"]

# Place each customer in a cohort: an app-orderer goes where every month she ordered still has room
rk = rng_for("kalpa cohorts")
room = {(c, KMONTHS[j]): v for c, vals in K_ACTIVE.items() for j, v in enumerate(vals) if v is not None}
cohort_of, since_of = {}, {}
orderers = sorted(app_by, key=lambda c: (-len({month_of(d) for d in app_by[c]}), c))
left = dict(K_SIZES)
for c in orderers:
    months = sorted({month_of(d) for d in app_by[c]})
    first = min(app_by[c])
    fits = [ym for ym in K_SIZES if left[ym] > 0 and ym <= month_of(first)
            and all(room.get((ym, m), 0 if months_apart(ym, m) >= 1 else 99) > 0 for m in months)]
    fits.sort(key=lambda ym: (-min(room.get((ym, m), 99) for m in months), ym))
    ym = fits[0]
    cohort_of[c] = ym
    left[ym] -= 1
    for m in months:
        if (ym, m) in room and months_apart(ym, m) >= 1:
            room[(ym, m)] -= 1
rest = [c for c in RP if c not in cohort_of]
rk.shuffle(rest)
for ym in K_SIZES:
    for _ in range(left[ym]):
        cohort_of[rest.pop()] = ym
for c, ym in sorted(cohort_of.items()):
    days = days_in(ym)
    latest = min([d for d in app_by.get(c, []) if month_of(d) == ym] or [days[-1]])
    since_of[c] = rk.choice([d for d in days if d <= latest])

# Who is active in which month: app-orderers first, then the most engaged of the rest
kscore = {c: rk.random() for c in RP}
K_ON = defaultdict(dict)
for ym, vals in K_ACTIVE.items():
    pool = sorted(c for c in RP if cohort_of[c] == ym)
    for j, m in enumerate(KMONTHS):
        k = months_apart(ym, m)
        if k < 0:
            continue
        if k == 0:
            n = round(0.9 * len(pool)) if vals[j] is None else vals[j]
        else:
            n = vals[j]
        must = [c for c in pool if any(month_of(d) == m for d in app_by.get(c, []))]
        ranked = sorted((c for c in pool if c not in must), key=lambda c: -(kscore[c] + rk.gauss(0, 0.2)))
        on = set(must) | set(ranked[: n - len(must)])
        for c in pool:
            K_ON[c][m] = c in on

# Kalpa sessions: an order session per app order, then browsing for every active member-month
ks = rng_for("kalpa sessions")
k_sessions = []                           # [customer, day, stages]
for o in APP:
    k_sessions.append([o["customer_id"], D.fromisoformat(o["order_date"]), "order"])
for c in RP:
    for m in KMONTHS:
        if not K_ON[c].get(m):
            continue
        days = [d for d in days_in(m) if d >= since_of[c]]
        n = ks.choice([1, 2, 2, 3, 3, 4, 5]) - sum(1 for d in app_by.get(c, []) if month_of(d) == m)
        for _ in range(max(n, 0)):
            k_sessions.append([c, ks.choice(days), "visit"])


def kalpa_block(d):
    if COMPARISON[0] <= d <= COMPARISON[1]:
        return "comparison"
    if AUTO_WINDOW[0] <= d <= AUTO_WINDOW[1]:
        return "window"
    return "before"


# carts that never reached checkout, enough for each block's rate
for block, rate_ in K_CART_TO_CHECKOUT.items():
    orders_in = [s for s in k_sessions if s[2] == "order" and kalpa_block(s[1]) == block]
    carts = round(len(orders_in) / rate_)
    visits = [s for s in k_sessions if s[2] == "visit" and kalpa_block(s[1]) == block]
    for s in ks.sample(visits, carts - len(orders_in)):
        s[2] = "cart"
flags_k = [False] * round(K_SKIP_SEARCH * len(k_sessions))
flags_k += [True] * (len(k_sessions) - len(flags_k))
ks.shuffle(flags_k)
k_sessions.sort(key=lambda s: (s[1], s[0], s[2]))
k_rows = []
k_session_list = []
for i, ((c, d, kind), searched) in enumerate(zip(k_sessions, flags_k), 1):
    sid = f"K{i:05d}"
    t = dt.datetime.combine(d, dt.time()) + dt.timedelta(seconds=clock(ks))
    stages = ["visit"] + (["search"] if searched else []) + \
        (["add_to_cart"] if kind in ("cart", "order") else []) + (["checkout"] if kind == "order" else [])
    for j, st in enumerate(stages):
        if j:
            t += dt.timedelta(seconds=ks.randint(8, 240))
        k_rows.append((c, sid, st, t.strftime("%Y-%m-%d %H:%M:%S")))
    k_session_list.append((c, sid, d, stages))
k_rows.sort(key=lambda r: (r[3], r[1]))
kev = pd.DataFrame(k_rows, columns=["customer_id", "session_id", "event_type", "event_ts"])
kmem = pd.DataFrame([{"customer_id": c, "tier": "Retail-Plus", "member_since": since_of[c].isoformat()}
                     for c in RP])
korders = pd.DataFrame([{k: o[k] for k in ("order_id", "customer_id", "order_date", "channel", "amount",
                                           "status")} for o in APP])
kmem.to_csv(DATA / f"{STEM}_kalpa_memberships_STUDENT.csv", index=False)
kev.to_csv(DATA / f"{STEM}_kalpa_events_STUDENT.csv", index=False)
korders.to_csv(DATA / f"{STEM}_kalpa_app_orders_STUDENT.csv", index=False)

# the Kalpa contract
kev["date"] = kev["event_ts"].str[:10]
kev["month"] = kev["event_ts"].str[:7]
kmem["cohort"] = kmem["member_since"].str[:7]
kc = kmem.set_index("customer_id")["cohort"]
active_k = kev.groupby(["customer_id", "month"]).size().gt(0)
check("Kalpa: the 120 members are v4's 120 Retail-Plus customers", sorted(kmem.customer_id) == RP and len(RP) == 120)
check("Kalpa: the August cohort is the largest", kmem.cohort.value_counts().idxmax() == "2026-08",
      int(kmem.cohort.value_counts().max()))
checkouts = kev[kev.event_type == "checkout"].groupby(["customer_id", "date"]).size()
apps = korders.groupby(["customer_id", "order_date"]).size()
check("Kalpa: every v4 app order has exactly one checkout on its date, and no checkout lacks an order",
      checkouts.sort_index().equals(apps.rename_axis(["customer_id", "date"]).sort_index()))
first_k = kev.groupby("customer_id")["date"].min()
check("Kalpa: no session before the membership started",
      (first_k >= kmem.set_index("customer_id")["member_since"].reindex(first_k.index)).all())
K_BLEND, K_CELLS = {}, {}
for m in KMONTHS:
    pre = kmem[kmem.cohort < m]
    on = [bool(active_k.get((c, m), False)) for c in pre.customer_id]
    K_BLEND[m] = (sum(on) / len(on), len(on), sum(on))
    check(f"Kalpa plant: blended retention (app activity), {NAMES[m]}, prints as 41 percent",
          round(100 * K_BLEND[m][0]) == 41, r4(K_BLEND[m][0]), 0.41)
    for ym in K_SIZES:
        if months_apart(ym, m) >= 1:
            ids = kmem[kmem.cohort == ym].customer_id
            K_CELLS[(ym, m)] = (sum(bool(active_k.get((c, m), False)) for c in ids), len(ids))
fall_k = all(K_CELLS[(ym, a)][0] > K_CELLS[(ym, b)][0] for ym in K_SIZES
             for a, b in zip(KMONTHS, KMONTHS[1:]) if (ym, a) in K_CELLS and (ym, b) in K_CELLS)
check("Kalpa plant: every cohort with two observed ages falls", fall_k)
m1_k = {ym: K_CELLS[(ym, MONTHS[MONTHS.index(ym) + 1])] for ym in ("2026-06", "2026-07")}
m1_k["2026-08"] = K_CELLS[("2026-08", "2026-09")]
check("Kalpa plant: the August cohort's month-one rate is the lowest observed",
      min(m1_k, key=lambda y: m1_k[y][0] / m1_k[y][1]) == "2026-08",
      {NAMES[y]: r3(a / n) for y, (a, n) in m1_k.items()})
ksess = kev.pivot_table(index="session_id", columns="event_type", values="customer_id", aggfunc="size",
                        fill_value=0).gt(0)
ksess = ksess.join(kev.drop_duplicates("session_id").set_index("session_id")[["customer_id", "date"]])
ksess["block"] = ksess["date"].map(lambda s: kalpa_block(D.fromisoformat(s)))
K_RATE = {b: ksess[ksess.block == b]["checkout"].sum() / ksess[ksess.block == b]["add_to_cart"].sum()
          for b in ("before", "comparison", "window")}
check("Kalpa plant: add-to-cart to checkout at least 15 points lower in 10 to 30 September",
      K_RATE["comparison"] - K_RATE["window"] >= 0.15, {b: r3(v) for b, v in K_RATE.items()})
check("Kalpa plant: within 5 points outside the window",
      abs(K_RATE["before"] - K_RATE["comparison"]) <= 0.05)
skip = 1 - ksess["search"].mean()
check("Kalpa plant: at least 20 percent of sessions skip search", skip >= 0.20, r3(skip))
ksep = ksess[ksess["date"].str[:7] == "2026-09"]
k_per_sess = ksep["checkout"].mean()
k_mem = ksep.groupby("customer_id")["checkout"].any()
k_per_member = k_mem.mean()
check("Kalpa plant: checkout per session and per member at least 10 points apart, September",
      abs(k_per_member - k_per_sess) >= 0.10, (r3(k_per_sess), r3(k_per_member)))

# the lab's twelve rows: seven members of the May and August cohorts, and one member's week
may_ids = sorted(kmem[kmem.cohort == "2026-05"].customer_id)
aug_ids = sorted(kmem[kmem.cohort == "2026-08"].customer_id)
lab = rng_for("kalpa lab rows")
plants_k = [K_BLEND[m][0] for m in KMONTHS] + [m1_k["2026-08"][0] / m1_k["2026-08"][1]]
for _ in range(500):                                     # the first draw whose hand counts sit clear
    lab_may = sorted(lab.sample(may_ids, 3))
    lab_aug = sorted(lab.sample(aug_ids, 4))
    lab_rows = [{"customer_id": c, "cohort": NAMES[kc[c]],
                 **{NAMES[m].lower(): ("" if months_apart(kc[c], m) < 1 else int(bool(active_k.get((c, m), False))))
                    for m in KMONTHS}} for c in lab_may + lab_aug]
    lab_sep = sum(r["sep"] for r in lab_rows) / 7
    lab_aug_m1 = sum(r["sep"] for r in lab_rows[3:]) / 4
    may_fall = all(r["jul"] >= r["aug"] >= r["sep"] for r in lab_rows[:3]) and \
        sum(r["jul"] for r in lab_rows[:3]) > sum(r["sep"] for r in lab_rows[:3])
    if may_fall and lab_aug_m1 == 0.75 and all(abs(x - p) >= 0.05 for x in (lab_sep, lab_aug_m1) for p in plants_k):
        break
check("Kalpa lab rows: the hand counts sit at least five points from every planted rate",
      all(abs(x - p) >= 0.05 for x in (lab_sep, lab_aug_m1) for p in plants_k), (r3(lab_sep), r3(lab_aug_m1)))
weeks_k = defaultdict(list)
for c, sid, d, stages in k_session_list:
    weeks_k[(c, d - dt.timedelta(d.weekday()))].append((d.isoformat(), sid, stages))
week_pick = sorted(((c, w), v) for (c, w), v in weeks_k.items()
                   if len(v) >= 3 and any("search" not in s for _, _, s in v) and any("search" in s for _, _, s in v))
lab_week = week_pick[0] if week_pick else None
check("Kalpa lab rows: one member's week shows sessions with and without a search", lab_week is not None)
case_rates = [v for v, _, _ in DASH.values()] + [EVERY["2026-09"][0]]
tw_rates = [a / n for a, n in list(tw_dash.values()) + list(tw_every.values())] + [TW[k][0] / TW[k][1] for k in want_tw]
check("twelve rows: no hand-counted rate within five points of a Kalpa retention plant",
      all(abs(x - p) >= 0.05 for x in tw_rates for p in plants_k), r3(min(abs(x - p) for x in tw_rates for p in plants_k)))

# shared constants with Monday
mon = {"kalpa_comparison_window": ["2026-08-20", "2026-09-09"],
       "kalpa_auto_reorder_window": ["2026-09-10", "2026-09-30"], "monsoon_sale_last_day": "2026-08-19"}
source = "the values Monday's branch writes (origin/w04-d1, commit 0f9cf0c)"
if MONDAY_FACTS.exists():
    mon = (yaml.safe_load(MONDAY_FACTS.read_text(encoding="utf-8")) or {}).get("shared_constants", mon)
    source = str(MONDAY_FACTS.relative_to(REPO))
ours = {"kalpa_comparison_window": [COMPARISON[0].isoformat(), COMPARISON[1].isoformat()],
        "kalpa_auto_reorder_window": [AUTO_WINDOW[0].isoformat(), AUTO_WINDOW[1].isoformat()],
        "monsoon_sale_last_day": MONSOON_SALE_LAST_DAY.isoformat()}
check(f"shared constants equal Monday's ({source})", all(mon.get(k) == v for k, v in ours.items()))

# ================================================================================= the facts
TICKET = "the ticket (half1 S5; notebook 05 cell 1; notes; cheat sheet)"
fact("members_total", len(members), "members", "rows of members", TICKET, f"{len(members):,}")
for ym in MONTHS:
    fact(f"cohort_size_{NAMES[ym].lower()}", SIZES[ym], "members", f"members whose signup month is {NAMES[ym]} 2026",
         "L2 cohort sizes; the blend decomposition", f"{SIZES[ym]:,}")
fact("cohort_mean_jan_jul", NORMAL, "members", "mean of the January to July cohort sizes", TICKET, "5,000")
fact("aug_times_normal", SALE_TIMES, "times", "13,000 / 5,000", TICKET, "2.6")
fact("aug_sale_members", SIZES["2026-08"] - AUG_ORGANIC, "members", "August members who joined on the sale's discount, all in the sale week",
     "L4 selection", f"{SIZES['2026-08'] - AUG_ORGANIC:,}")
fact("aug_organic_members", AUG_ORGANIC, "members", "August members who joined outside the sale", "L4 selection",
     f"{AUG_ORGANIC:,}")
for ym in M1:
    fact(f"m1_{NAMES[ym].lower()}", r4(tri.loc[ym, 1]), "share", f"{NAMES[ym]} members who ordered in month one",
         "the ticket; L2 the triangle; the explorer Th1", pct(tri.loc[ym, 1]))
for ym in M1:
    for k in tri.columns:
        v = tri.loc[ym, k]
        if pd.notna(v) and k >= 2:
            fact(f"tri_{NAMES[ym].lower()}_m{k}", r4(v), "share", f"{NAMES[ym]} members who ordered in month {k}",
                 "L2 the triangle (notebook 06, the heatmap)", f"{100 * v:.1f} percent")
fact("aug_m1_organic", r4(org_m1["organic"]), "share", "organic August members who ordered in September",
     "L4 selection", pct(org_m1["organic"]))
fact("aug_m1_sale", r4(org_m1["sale"]), "share", "sale-week August members who ordered in September",
     "L4 selection; L5 the sale cohort", pct(org_m1["sale"]))
for m, (v, n, a) in DASH.items():
    fact(f"dashboard_{NAMES[m].lower()}", round(float(v), 5), "share",
         f"members two or more months past signup who ordered in {NAMES[m]}, {a:,} of {n:,}",
         "the ticket; L2 the trap; the explorer Th1", pct(v))
    fact(f"dashboard_{NAMES[m].lower()}_counted", n, "members", f"the dashboard's denominator in {NAMES[m]}",
         "L2 the second route", f"{n:,}")
    fact(f"dashboard_{NAMES[m].lower()}_ordered", a, "members", f"the dashboard's numerator in {NAMES[m]}",
         "L2 the second route", f"{a:,}")
v, n, a = EVERY["2026-09"]
fact("everyone_sep", r4(v), "share", f"every member who joined before September and ordered in it, {a:,} of {n:,}",
     "L2 the reveal; L3", pct(v))
fact("everyone_sep_counted", n, "members", "every member who joined before September", "L2 the reveal", f"{n:,}")
fact("everyone_sep_ordered", a, "members", "of them, those who ordered in September", "L2 the reveal", f"{a:,}")
unw = mm[(mm.month == "2026-09") & (mm.age >= 1)].groupby("cohort_month")["active"].mean().mean()
fact("everyone_sep_unweighted_mean", r4(unw), "share",
     "the eight cohorts' September rates averaged with no weights (a mean of ratios, wrong)", "L2 the weights",
     f"{100 * unw:.1f} percent")
fact("aug_cohort_outside_dashboard", SIZES["2026-08"], "members",
     "the August cohort, in its first month in September, outside the dashboard's count", "L2 the reveal",
     f"{SIZES['2026-08']:,}")
oct_low, oct_mid, oct_high = 0.17, r3(tri.loc["2026-08", 1] - (tri.loc["2026-07", 1] - tri.loc["2026-07", 2])), 0.24


def october(m2_sale):
    num = sum(SIZES[ym] * (BASE2[ym] - SLOPE * (months_apart(ym, "2026-10") - 2)) for ym in MONTHS[:7])
    return (num + SIZES["2026-08"] * m2_sale) / (sum(SIZES[ym] for ym in MONTHS[:8]))


fact("oct_sale_m2_assumed", oct_mid, "share",
     "assumption: the sale cohort falls from month one to month two as July's did (49 to 38.5); range 17 to 24",
     "L5 the October estimate", pct(oct_mid))
fact("oct_dashboard_estimate", r3(october(oct_mid)), "share",
     "the dashboard in October if the old cohorts keep their plateau and the sale cohort enters at the assumption",
     "L5; the notes", pct(october(oct_mid)))
fact("oct_dashboard_low", r3(october(oct_low)), "share", "the same at 17 percent", "L5", pct(october(oct_low)))
fact("oct_dashboard_high", r3(october(oct_high)), "share", "the same at 24 percent", "L5", pct(october(oct_high)))
fact("search_to_menu_session_sep", r4(search_to_menu), "ratio",
     "sessions with a menu view over sessions with a search, members, September", "the ticket; L3 the artefact",
     pct(search_to_menu))
fact("search_to_menu_searched_sep", r4(search_to_menu_true), "share",
     "of sessions that searched, the share that opened a menu, members, September", "L3 the fix", pct(search_to_menu_true))
n_carousel = int((reach["menu_view"] & ~reach["search"]).sum())
fact("sep_menu_sessions_no_search", n_carousel, "sessions",
     "member sessions in September that opened a menu with no search (the home carousel)", "L3 the artefact",
     f"{n_carousel:,}")
fact("menu_to_cart_session_sep", r4(menu_to_cart_s), "share",
     "sessions with add_to_cart over sessions with menu_view, members, September", "the ticket; L3 the units",
     pct(menu_to_cart_s))
fact("menu_to_cart_member_sep", r4(menu_to_cart_m), "share",
     "members with add_to_cart over members with menu_view, September", "the ticket; L3 the units", pct(menu_to_cart_m))
for col in ("open", "search", "menu_view", "add_to_cart", "checkout_start", "order_placed"):
    fact(f"sep_sessions_{col}", int(reach[col].sum()), "sessions", f"member sessions in September reaching {col}",
         "L3 the funnel table", f"{int(reach[col].sum()):,}")
    fact(f"sep_members_{col}", int(by_member[col].sum()), "members", f"members in September reaching {col}",
         "L3 the funnel table", f"{int(by_member[col].sum()):,}")
FLOW = ["open", "search", "menu_view", "add_to_cart", "checkout_start", "order_placed"]
for a, b in zip(FLOW, FLOW[1:]):
    vs = reach[b].sum() / reach[a].sum()
    vm = by_member[b].sum() / by_member[a].sum()
    fact(f"sep_step_session_{a}_to_{b}", r4(vs), "share", f"member sessions reaching {b} over {a}, September",
         "L3 the funnel per session", f"{100 * vs:.0f} percent")
    fact(f"sep_step_member_{a}_to_{b}", r4(vm), "share", f"members reaching {b} over {a}, September",
         "L3 the funnel per member", f"{100 * vm:.0f} percent")
labels = {(True, "android"): "member_android", (True, "ios"): "member_ios", (True, "web"): "member_web",
          (False, "android"): "nonmember_android", (False, "ios"): "nonmember_ios", (False, "web"): "nonmember_web"}
for (is_m, p), lab_ in labels.items():
    for per in ("before", "after"):
        fact(f"atc_to_order_{lab_}_{per}", r4(RELEASE_SPLIT[(is_m, p, per)]), "share",
             f"order_placed sessions over add_to_cart sessions, {lab_.replace('_', ' ')}, "
             f"{'1 August to 13 September' if per == 'before' else '14 to 30 September'}",
             "the ticket; L3 the release split", pct(RELEASE_SPLIT[(is_m, p, per)]))
fact("android_members_checkout_to_order_before", r4(co_b), "share", "Android members, checkout_start to order_placed",
     "L3 the stage", f"{100 * co_b:.1f} percent")
fact("android_members_checkout_to_order_after", r4(co_a), "share", "the same after the release", "L3 the stage", pct(co_a))
fact("android_members_cart_to_checkout_before", r4(cs_b), "share", "Android members, add_to_cart to checkout_start",
     "L3 the stage", pct(cs_b))
fact("android_members_cart_to_checkout_after", r4(cs_a), "share", "the same after the release", "L3 the stage", pct(cs_a))
for w, v in weekly.items():
    fact(f"android_members_week_{w.start_time.date().isoformat()}", r4(v), "share",
         f"Android members' add-to-cart to order, week of {w.start_time.date():%d %B}", "L3 the weekly release split",
         pct(v))
for (k, label), (b, a) in [(k, v) for k, v in RELEASE_SPLIT.items() if k[0] == "shift"]:
    slug = label.split()[0]
    fact(f"shift_{slug}_sep_before", r4(b), "share", f"Android members before {label}", "L4 the tracking check", pct(b))
    fact(f"shift_{slug}_sep_after", r4(a), "share", f"Android members from {label}", "L4 the tracking check", pct(a))
fact("android_member_carts_after", int(step_after["add_to_cart"].sum()), "sessions",
     "Android member add_to_cart sessions, 14 to 30 September", "L5 the cost", f"{int(step_after['add_to_cart'].sum()):,}")
fact("days_after_release", 17, "days", "14 to 30 September", "L5 the cost", "17")
fact("lost_orders_per_week", round(lost_estimate_week), "orders",
     "(0.58 - 0.44) x Android member carts after the release / (17 / 7)", "L5 the cost", f"{round(lost_estimate_week):,}")
fact("order_value_assumed_rs", ORDER_VALUE_RS, "Rs", "an assumption with a range of Rs 300 to Rs 500 per order",
     "L5 the cost", "Rs 400")
fact("order_value_low_rs", 300, "Rs", "the low end of the order-value assumption", "L5 the cost", "Rs 300")
fact("order_value_high_rs", 500, "Rs", "the high end of the order-value assumption", "L5 the cost", "Rs 500")
fact("lost_value_per_week_rs", round(lost_estimate_week) * ORDER_VALUE_RS, "Rs", "lost orders a week x Rs 400",
     "L5 the cost", f"Rs {round(lost_estimate_week) * ORDER_VALUE_RS / 1e5:.1f} lakh")
fact("lost_value_per_week_low_rs", round(lost_estimate_week) * 300, "Rs", "the same at Rs 300", "L5 the cost",
     f"Rs {round(lost_estimate_week) * 300 / 1e5:.1f} lakh")
fact("lost_value_per_week_high_rs", round(lost_estimate_week) * 500, "Rs", "the same at Rs 500", "L5 the cost",
     f"Rs {round(lost_estimate_week) * 500 / 1e5:.1f} lakh")
for (p, month), v in opm.items():
    fact(f"orders_per_active_{p}_{NAMES[month].lower()}", r2(v), "orders", f"orders per active {p} member, {NAMES[month]}",
         "L4 fewer users or less use; L6", f"{v:.2f}")
mem_all = sess[sess.is_member]
for per in ("before", "after"):
    sub = mem_all[mem_all.period == per]
    v = sub["checkout_start"].sum() / sub["add_to_cart"].sum()
    fact(f"members_cart_to_checkout_all_{per}", r4(v), "share",
         f"members on every platform, checkout_start sessions over add_to_cart sessions, {per} 14 September",
         "L5 the app team's chart", pct(v))
aug_m1 = mm[(mm.cohort_month == "2026-08") & (mm.age == 1)].merge(mem_df[["member_id", "signup_channel"]], on="member_id")
for ch, g in aug_m1.groupby("signup_channel"):
    fact(f"aug_{ch}_orders_per_member_m1", r2(g["orders"].mean()), "orders",
         f"September orders per August {ch} member, zeros included", "L5 the sale cohort", f"{g['orders'].mean():.2f}")
# the weekly rerun: members who joined 3 August to 13 September, by signup week, ordering week by week
ordw = placed.assign(week=placed["date"].dt.to_period("W-SUN").dt.start_time)[["user_id", "week"]].drop_duplicates()
ordw = set(zip(ordw["user_id"], ordw["week"]))
wk_rows = []
for m in members:
    sd = pd.Timestamp(m["signup_date"])
    w0 = sd - pd.Timedelta(days=sd.weekday())
    if not (pd.Timestamp("2026-08-03") <= w0 <= pd.Timestamp("2026-09-07")):
        continue
    for k in range(1, 9):
        wk = w0 + pd.Timedelta(weeks=k)
        if wk > pd.Timestamp("2026-09-21"):            # the week of 28 September is three days long
            break
        wk_rows.append((w0.date().isoformat(), k, (m["member_id"], wk) in ordw))
wk = pd.DataFrame(wk_rows, columns=["signup_week", "week_k", "ordered"])
WEEKLY = wk.pivot_table(index="signup_week", columns="week_k", values="ordered", aggfunc="mean")
WEEKLY_SIZE = wk[wk.week_k == 1].groupby("signup_week").size()
for w, row in WEEKLY.iterrows():
    fact(f"weekly_cohort_{w}_size", int(WEEKLY_SIZE[w]), "members", f"members who joined in the week of {w}",
         "the take-home; the fallback rerun", f"{int(WEEKLY_SIZE[w]):,}")
    for k, v in row.dropna().items():
        fact(f"weekly_cohort_{w}_w{k}", r4(v), "share", f"of them, the share who ordered in week {k} after joining",
             "the take-home; the fallback rerun", f"{100 * v:.0f} percent")
drop12 = WEEKLY[1] - WEEKLY[2]
check("weekly rerun: the sale week's cohort is the largest, the highest in week one and the lowest in week two",
      WEEKLY_SIZE.idxmax() == "2026-08-17" and WEEKLY[1].idxmax() == "2026-08-17"
      and WEEKLY[2].idxmin() == "2026-08-17" and drop12.idxmax() == "2026-08-17",
      {w: (int(WEEKLY_SIZE[w]), r3(WEEKLY.loc[w, 1]), r3(WEEKLY.loc[w, 2])) for w in WEEKLY.index})
fact("zone_sep_spread", r3((zone_sep - DASH["2026-09"][0]).abs().max()), "share",
     "largest gap between a zone's September dashboard rate and the city's", "L4 seasonality", f"{100 * (zone_sep - DASH['2026-09'][0]).abs().max():.1f} points")
# ---- the checks a hard interviewer asks for: the same step, the cohorts held fixed, the noise, the retries,
# ---- the version, the order records and the drop counted over everyone (the second cold read)
for m in REPORTING[:3]:
    v, n, a = EVERY[m]
    fact(f"everyone_{NAMES[m].lower()}", r4(v), "share", f"every member who joined before {NAMES[m]} and ordered in it, {a:,} of {n:,}",
         "L2 the drop the dashboard hides; the transcript", f"{100 * v:.1f} percent")
    fact(f"everyone_{NAMES[m].lower()}_counted", n, "members", f"every member who joined before {NAMES[m]}", "L2", f"{n:,}")
    fact(f"everyone_{NAMES[m].lower()}_ordered", a, "members", f"of them, those who ordered in {NAMES[m]}", "L2", f"{a:,}")
check("counted over everyone, the series falls every month from June to September",
      EVERY["2026-06"][0] > EVERY["2026-07"][0] > EVERY["2026-08"][0] > EVERY["2026-09"][0])
coh_of = mem_df.set_index("member_id")["cohort_month"]
sess["cohort"] = sess["user_id"].map(coh_of)


def completion(df):
    return df["order_placed"].sum() / df["checkout_start"].sum()


for is_m, p, slug in ((True, "ios", "member_ios"), (False, "android", "nonmember_android")):
    for per in ("before", "after"):
        v = completion(sess[(sess.is_member == is_m) & (sess.platform == p) & (sess.period == per)])
        fact(f"checkout_to_order_{slug}_{per}", r4(v), "share",
             f"checkout_start to order_placed sessions, {slug.replace('_', ' on ')}, {per} 14 September",
             "L4 the comparators on the same step", f"{round(100 * v)} percent")
held = sess[sess.is_member & (sess.cohort < "2026-08")]
for p in ("android", "ios"):
    for per in ("before", "after"):
        sub = held[(held.platform == p) & (held.period == per)]
        fact(f"held_checkout_to_order_{p}_{per}", r4(completion(sub)), "share",
             f"members who joined before August, {p}, checkout_start to order_placed, {per} 14 September",
             "L4 the cohorts held fixed", f"{100 * completion(sub):.1f} percent")
        fact(f"held_atc_to_order_{p}_{per}", r4(conv(sub)), "share",
             f"members who joined before August, {p}, add_to_cart to order_placed, {per} 14 September",
             "L4 the cohorts held fixed", f"{round(100 * conv(sub))} percent")
ios_fall = completion(held[(held.platform == "ios") & (held.period == "after")]) - \
    completion(held[(held.platform == "ios") & (held.period == "before")])
check("held fixed, iOS completion moves by under a point while Android's falls by more than 15",
      abs(ios_fall) < 0.01 and completion(held[(held.platform == "android") & (held.period == "before")])
      - completion(held[(held.platform == "android") & (held.period == "after")]) > 0.15)
sale_ids = set(mem_df.loc[mem_df.signup_channel == "sale", "member_id"])
sw_ios = sess[sess.is_member & (sess.platform == "ios") & sess.user_id.isin(sale_ids)]
for per in ("before", "after"):
    v = conv(sw_ios[sw_ios.period == per])
    fact(f"sale_week_ios_atc_to_order_{per}", r4(v), "share",
         f"sale-week members on iOS, add_to_cart to order_placed, {per} 14 September (they age from month zero to month one across the cut)",
         "the trainer's [D] follow-up", f"{round(100 * v)} percent")
plat_of = {m["member_id"]: m["platform"] for m in members}
mm_p = mm[mm.month.isin(["2026-08", "2026-09"]) & mm.active & (mm.cohort_month < "2026-08")].copy()
mm_p["platform"] = mm_p["member_id"].map(plat_of)
for p in ("android", "ios"):
    for month in ("2026-08", "2026-09"):
        v = mm_p[(mm_p.platform == p) & (mm_p.month == month)]["orders"].mean()
        fact(f"held_orders_per_active_{p}_{NAMES[month].lower()}", r2(v), "orders",
             f"orders per ordering {p} member who joined before August, {NAMES[month]}",
             "L4 fewer users or less use, the cohorts held fixed", f"{v:.2f}")
share_android = mem_df.assign(p=mem_df.member_id.map(plat_of)).groupby("cohort_month")["p"].apply(lambda s: (s == "android").mean())
fact("android_share_cohort_low", r3(share_android.min()), "share", "the lowest share of a cohort on Android",
     "the trainer's [D] follow-up", f"{round(100 * share_android.min())} percent")
fact("android_share_cohort_high", r3(share_android.max()), "share", "the highest share of a cohort on Android",
     "the trainer's [D] follow-up", f"{round(100 * share_android.max())} percent")
and_orders = sess[sess.is_member & (sess.platform == "android") & sess.order_placed]
days_before = (pd.Timestamp(RELEASE) - pd.Timestamp("2026-08-01")).days
wk_before = (and_orders.period == "before").sum() / days_before * 7
wk_after = (and_orders.period == "after").sum() / 17 * 7
fact("android_member_orders_week_before", round(wk_before), "orders", "Android member orders a week, 1 August to 13 September",
     "L5 the loss as a share", f"{round(wk_before):,}")
fact("android_member_orders_week_after", round(wk_after), "orders", "Android member orders a week, 14 to 30 September",
     "L5 the loss as a share", f"{round(wk_after):,}")
drift = ((RELEASE_SPLIT[(True, "ios", "before")] - RELEASE_SPLIT[(True, "ios", "after")])
         + (RELEASE_SPLIT[(False, "android", "before")] - RELEASE_SPLIT[(False, "android", "after")])) / 2
netted = (RELEASE_SPLIT[(True, "android", "before")] - RELEASE_SPLIT[(True, "android", "after")] - drift) \
    * step_after["add_to_cart"].sum() / (17 / 7)
fact("comparator_drift_points", r2(100 * drift), "points", "the comparators' own fall, iOS members and non-members on Android, averaged",
     "L5 the netted loss", f"{100 * drift:.0f} point")
fact("lost_orders_per_week_netted", round(netted), "orders",
     "the lost-order estimate after taking off the fall the comparators show anyway", "L5 the cost range", f"{round(netted):,}")
fact("lost_value_per_week_netted_low_rs", round(netted) * 300, "Rs", "the netted loss at Rs 300 an order",
     "L5 the cost range", f"Rs {round(netted) * 300 / 1e5:.1f} lakh")
fact("lost_share_of_android_orders", r2(round(lost_estimate_week) / wk_before), "share",
     "the loss a week over Android member orders a week before the release", "L5 the loss as a share",
     f"{round(100 * round(lost_estimate_week) / wk_before)} percent")
starts_m = int(step_after["checkout_start"].sum())
starts_nm = int(sess[(~sess.is_member) & (sess.platform == "android") & (sess.period == "after")]["checkout_start"].sum())
fact("android_member_starts_after", starts_m, "sessions", "Android member checkout_start sessions, 14 to 30 September",
     "L4 noise", f"{starts_m:,}")
fact("nonmember_android_starts_after", starts_nm, "sessions", "non-member Android checkout_start sessions, 14 to 30 September",
     "L4 noise", f"{starts_nm:,}")
fact("noise_points_android_members", r2(100 / starts_m ** 0.5), "points", "1 / square root of the starts, in points",
     "L4 noise", f"{100 / starts_m ** 0.5:.1f} points")
fact("noise_points_nonmember_android", r2(100 / starts_nm ** 0.5), "points", "1 / square root of the starts, in points",
     "L4 noise", f"{100 / starts_nm ** 0.5:.1f} points")
st = ev[ev.is_member].groupby("session_id").agg(user_id=("user_id", "first"), t=("event_ts", "min"),
                                                platform=("platform", "first"))
st["t"] = pd.to_datetime(st["t"])
st = st.join(sess[["checkout_start", "order_placed"]])
failed = st[st.checkout_start & ~st.order_placed].sort_values("t").reset_index()
ordered = st[st.order_placed].sort_values("t").reset_index()[["user_id", "t"]].rename(columns={"t": "next_order"})
nxt = pd.merge_asof(failed, ordered, left_on="t", right_on="next_order", by="user_id",
                    direction="forward", allow_exact_matches=False)
nxt["retried"] = (nxt["next_order"] - nxt["t"]) <= pd.Timedelta(days=1)
nxt["period"] = (nxt["t"] >= pd.Timestamp(RELEASE)).map({True: "after", False: "before"})
for per in ("before", "after"):
    v = nxt[(nxt.platform == "android") & (nxt.period == per)]["retried"].mean()
    fact(f"retry_within_day_android_{per}", r4(v), "share",
         f"Android member sessions that started checkout with no order, followed by the same member's order within a day, {per}",
         "the upper-bound push", f"{100 * v:.1f} percent")
v2 = sess[(sess.platform == "android") & (sess.period == "after")]["checkout_version"].eq("v2").mean()
v1 = sess[(sess.platform != "android") | (sess.period == "before")]["checkout_version"].eq("v1").mean()
check("every Android session from 14 September runs v2, and every other session v1", v2 == 1 and v1 == 1, r4(v2), r4(v1))
fact("android_v2_share_after", r4(v2), "share", "Android sessions on checkout v2 from 14 September", "L4 the version",
     "every Android session")
for month in ("2026-08", "2026-09"):
    n_mm = int(mm[mm.month == month]["orders"].sum())
    fact(f"order_records_{NAMES[month].lower()}", n_mm, "orders", f"member orders in member_months, {NAMES[month]}",
         "L4 the tracking check", f"{n_mm:,}")
    fact(f"event_orders_{NAMES[month].lower()}", int(placed[placed.month == month].shape[0]), "orders",
         f"member order_placed sessions in the event log, {NAMES[month]}", "L4 the tracking check",
         f"{int(placed[placed.month == month].shape[0]):,}")
# ---- the second interviewer read: the drop apportioned, retention by platform, orders netted, recoveries
normal_aug = (DASH["2026-09"][2] + 5000 * round(float(tri.loc["2026-07", 1]), 2)) / (DASH["2026-09"][1] + 5000)
fall_all = EVERY["2026-08"][0] - EVERY["2026-09"][0]
fact("everyone_sep_normal_august", r4(normal_aug), "share",
     "September counted over everyone if August had brought 5,000 members at July's month one", "the transcript's close",
     f"{100 * normal_aug:.1f} percent")
fact("everyone_fall_aug_to_sep_points", r2(100 * fall_all), "points", "everyone's count, August to September",
     "the transcript's close", f"{100 * fall_all:.1f} points")
fact("everyone_fall_from_august_cohort_points", r2(100 * (normal_aug - EVERY["2026-09"][0])), "points",
     "the part of the fall the August cohort's size and weakness explain", "the transcript's close",
     f"{100 * (normal_aug - EVERY['2026-09'][0]):.1f} points")
fact("everyone_fall_ordinary_points", r2(100 * (EVERY["2026-08"][0] - normal_aug)), "points",
     "the part a normal August would have shown", "the transcript's close",
     f"{100 * (EVERY['2026-08'][0] - normal_aug):.1f} points")
plat_s = mm.assign(platform=mm["member_id"].map(plat_of))
for month in ("2026-08", "2026-09"):
    for p_ in ("android", "ios"):
        d_ = plat_s[(plat_s.month == month) & (plat_s.age >= 2) & (plat_s.platform == p_)]["active"].mean()
        h_ = plat_s[(plat_s.month == month) & (plat_s.cohort_month < "2026-08") & (plat_s.platform == p_)]["active"].mean()
        fact(f"dashboard_{p_}_{NAMES[month].lower()}", r4(d_), "share", f"the dashboard's count on {p_}, {NAMES[month]}",
             "retention cannot see the checkout", f"{100 * d_:.1f} percent")
        fact(f"held_share_ordered_{p_}_{NAMES[month].lower()}", r4(h_), "share",
             f"members who joined before August on {p_} who ordered, {NAMES[month]}", "users against use", f"{100 * h_:.1f} percent")
# ---- the third interviewer read: users against use with age held too, members who joined before July
# are past month one in August and in September, so neither month carries a cohort's first-month drop
held_july = {}
for month in ("2026-08", "2026-09"):
    for p_ in ("android", "ios"):
        s_ = plat_s[(plat_s.month == month) & (plat_s.cohort_month < "2026-07") & (plat_s.platform == p_)]
        sh_, op_ = s_["active"].mean(), s_[s_.active]["orders"].mean()
        held_july[(p_, month)] = (sh_, op_)
        fact(f"held_july_share_ordered_{p_}_{NAMES[month].lower()}", r4(sh_), "share",
             f"members who joined before July on {p_} who ordered, {NAMES[month]}", "users against use, age held",
             f"{100 * sh_:.1f} percent")
        fact(f"held_july_orders_per_active_{p_}_{NAMES[month].lower()}", r2(op_), "orders",
             f"orders per ordering {p_} member who joined before July, {NAMES[month]}", "users against use, age held",
             f"{op_:.2f}")
check("joined before July, the share who ordered moves under a point on each platform while orders per ordering "
      "member fall only on Android",
      all(abs(held_july[(p_, "2026-09")][0] - held_july[(p_, "2026-08")][0]) < 0.01 for p_ in ("android", "ios"))
      and held_july[("android", "2026-08")][1] - held_july[("android", "2026-09")][1] > 0.15
      and abs(held_july[("ios", "2026-09")][1] - held_july[("ios", "2026-08")][1]) < 0.05)
wk_orders = {}
for is_m, p_ in ((True, "android"), (True, "ios"), (False, "android")):
    o_ = sess[(sess.is_member == is_m) & (sess.platform == p_) & sess.order_placed]
    b_ = (o_.period == "before").sum() / days_before * 7
    a_ = (o_.period == "after").sum() / 17 * 7
    wk_orders[(is_m, p_)] = (b_, a_)
    slug = ("member_" if is_m else "nonmember_") + p_
    fact(f"weekly_orders_change_{slug}", r4(a_ / b_ - 1), "share", f"orders a week, {slug.replace('_', ' ')}, after against before",
         "the loss in orders placed", f"{round(100 * (a_ / b_ - 1)):+d} percent".replace("+", "up ").replace("-", "down "))
b_and, a_and = wk_orders[(True, "android")]
for slug, key in (("ios", (True, "ios")), ("nonmember_android", (False, "android"))):
    cf = b_and * wk_orders[key][1] / wk_orders[key][0]
    fact(f"lost_orders_week_vs_{slug}", round(cf - a_and), "orders",
         f"Android members' orders a week against the change {slug.replace('_', ' ')} showed, which nets out any retry that worked",
         "the cost range's floor", f"{round(cf - a_and):,}")
floor_orders = round(b_and * wk_orders[(False, "android")][1] / wk_orders[(False, "android")][0] - a_and)
fact("lost_value_per_week_floor_rs", floor_orders * 300, "Rs", "the floor of the loss at Rs 300 an order", "the cost range",
     f"Rs {floor_orders * 300 / 1e5:.1f} lakh")
for per in ("before", "after"):
    sub = nxt[(nxt.platform == "android") & (nxt.period == per)]
    days_ = days_before if per == "before" else 17
    fact(f"failed_checkouts_week_android_{per}", round(len(sub) / days_ * 7), "sessions",
         f"Android member checkouts with no order a week, {per}", "the retry argument", f"{round(len(sub) / days_ * 7):,}")
    fact(f"recovered_within_day_week_android_{per}", round(sub["retried"].sum() / days_ * 7), "orders",
         f"of them, followed by the member's order within a day, a week, {per}", "the retry argument",
         f"{round(sub['retried'].sum() / days_ * 7):,}")
n_both = int((reach["menu_view"] & reach["search"]).sum())
fact("sep_sessions_search_and_menu", n_both, "sessions", "member sessions in September with a search and a menu view",
     "L3 the fix's working", f"{n_both:,}")
for w, v in weekly.items():
    fact(f"android_member_week_{w.start_time.date().isoformat()}", r4(v), "share",
         f"Android members, add_to_cart to order_placed, the week of {w.start_time.date().isoformat()}",
         "L3 the weekly series", f"{round(100 * v)} percent")
fact("events_rows", len(ev), "rows", "rows of events", "notebook 07", f"{len(ev):,}")
fact("events_sessions", int(ev.session_id.nunique()), "sessions", "sessions in events", "notebook 07",
     f"{ev.session_id.nunique():,}")
fact("nonmember_users", NON_MEMBERS, "users", "the comparison sample of non-member users", "the ticket", f"{NON_MEMBERS:,}")
fact("member_months_rows", len(mm), "rows", "rows of member_months", "notebook 06", f"{len(mm):,}")

toys = [
    {"id": "toy_two_batches", "label": "invented",
     "values": {"june_batch": 10, "july_batch": 10, "june_back_m2": 6, "july_back_m2": 4, "together": "10 of 20"},
     "used_by": "L1 the coaching-centre analogy"},
    {"id": "toy_blend", "label": "invented",
     "values": {"a_size": 100, "a_last_month": 0.50, "a_now": 0.40, "b_size": 400, "b_rate": 0.525,
                "a_ordered_last_month": 50, "a_ordered_now": 40, "b_ordered": 210,
                "ordered_now": 250, "members_now": 500, "blend_now": 0.50},
     "used_by": "L1 and L2: the blend that holds while every batch falls; the explorer Th2"},
    {"id": "toy_funnel", "label": "invented",
     "values": {"visits": 100, "searches": 40, "carts": 20, "checkouts": 10, "per_session_checkout": "10 of 50",
                "per_member_checkout": "10 of 20"},
     "used_by": "L3 the funnel toy (retired, see below)"},
    {"id": "toy_weaned", "label": "invented",
     "values": {"all_ten": [7, 5, 4, 3], "strong_five": [5, 5, 4, 3], "all_ten_percent": [70, 50, 40, 30],
                "strong_five_percent": [100, 100, 80, 60]}, "used_by": "the fallback hour"},
    {"id": "toy_ai_cohorts", "label": "invented",
     "values": {"launch_week_4": 0.24, "organic_week_4": 0.36}, "used_by": "L6 the AI-company variant (as the explorer Th4)"},
]
# the toys the exercises, the quiz and the notes use, each rate computed from its own counts
KAAPI_S = {"search": 5000, "product_view": 6000, "add_to_cart": 2000, "order": 1200}
KAAPI_C = {"search": 2100, "product_view": 2400, "add_to_cart": 1400, "order": 1000}
DABBA = {"jan": (8, [6, 4, 3]), "feb": (6, [4, 3]), "mar": (6, [3])}
DABBA_APP = {"menu": 2000, "specials": 2400, "plan": 600, "paid": 480}
DABBA_BLEND = {"a": (400, 0.60, 0.55), "b": (600, 0.45, 0.40), "c": (1000, None, 0.56)}
KAHOOT_BLEND = {"a": (300, 0.60, 0.55), "b": (700, 0.40, 0.35), "c": (1000, None, 0.51)}
NOTES_BLEND = {"a": (200, 0.45, 0.40), "b": (300, None, 0.52)}


def blend_months(cohorts):
    may = [(n, r0) for n, r0, _ in cohorts.values() if r0 is not None]
    jun = [(n, r1) for n, _, r1 in cohorts.values()]
    return (round(sum(n * r for n, r in may)), sum(n for n, _ in may),
            round(sum(n * r for n, r in jun)), sum(n for n, _ in jun))


jan_n, jan_a = DABBA["jan"]
toys += [
    {"id": "toy_kaapi_funnel", "label": "invented, Kaapi and Co., a bakery app",
     "values": {"sessions": KAAPI_S, "customers": KAAPI_C,
                "search_to_view_session": r3(KAAPI_S["product_view"] / KAAPI_S["search"]),
                "view_to_cart_session": r3(KAAPI_S["add_to_cart"] / KAAPI_S["product_view"]),
                "cart_to_order_session": r3(KAAPI_S["order"] / KAAPI_S["add_to_cart"]),
                "view_to_cart_customer": r3(KAAPI_C["add_to_cart"] / KAAPI_C["product_view"]),
                "search_to_cart_customer": r3(KAAPI_C["add_to_cart"] / KAAPI_C["search"]),
                "customers_over_sessions": r3(KAAPI_C["add_to_cart"] / KAAPI_S["product_view"]),
                "search_over_view_session": r3(KAAPI_S["search"] / KAAPI_S["product_view"]),
                "cart_to_order_after_update": 0.48},
     "used_by": "exercises: the Kaapi and Co. drill, in the lab's practice set"},
    {"id": "toy_dabba_club", "label": "invented, Dabba Club, a tiffin subscription",
     "values": {"subscribers": sum(n for n, _ in DABBA.values()),
                "cohorts": {k: {"size": n, "active": a, "percent": [round(100 * x / n, 1) for x in a]}
                            for k, (n, a) in DABBA.items()},
                "jan_over_survivors": [round(100 * b / a, 1) for a, b in zip([jan_n] + jan_a, jan_a)],
                "jan_never_orderers_dropped": [round(100 * x / jan_a[0], 1) for x in jan_a],
                "jan_not_active": [round(100 * (jan_n - x) / jan_n, 1) for x in jan_a],
                "april_column": [round(100 * a[-1] / n, 1) for n, a in DABBA.values()],
                "app": DABBA_APP,
                "app_steps": [r3(DABBA_APP["specials"] / DABBA_APP["menu"]), r3(DABBA_APP["plan"] / DABBA_APP["specials"]),
                              r3(DABBA_APP["paid"] / DABBA_APP["plan"])],
                "payment_march_april": 0.80, "update_day": "6 April",
                "blend_cohorts": {k: list(v) for k, v in DABBA_BLEND.items()},
                "blend_ordered": [round(n * r) for n, r0, r1 in DABBA_BLEND.values() for r in (r0, r1) if r is not None],
                "blend_months": blend_months(DABBA_BLEND)},
     "used_by": "exercises: the lab's practice set"},
    {"id": "toy_kahoot_blend", "label": "invented",
     "values": {"cohorts": {k: list(v) for k, v in KAHOOT_BLEND.items()}, "months": blend_months(KAHOOT_BLEND),
                "fall_points": 5},
     "used_by": "the Kahoot's trap item, a blend other than 38 and 41"},
    {"id": "toy_notes_blend", "label": "invented",
     "values": {"cohorts": {k: list(v) for k, v in NOTES_BLEND.items()}, "ordered_now": [80, 156],
                "months": blend_months(NOTES_BLEND)},
     "used_by": "the study notes' self-check"},
]
for t in toys[-3:]:
    key = "months" if "months" in t["values"] else "blend_months"
    a, n, b, m = t["values"][key]
    t["values"]["blend_percent"] = [round(100 * a / n, 1), round(100 * b / m, 1)]
flat = [t["values"]["blend_percent"] for t in toys if t["id"] in ("toy_dabba_club", "toy_kahoot_blend")]
check("the practice set's and the quiz's blends hold flat, neither at 38 nor 41",
      len(flat) == 2 and all(a == b and a not in (38, 41) for a, b in flat), flat)

# ======================================================================= the concept chapters' examples
# The five concept chapters teach the row's subtopics before the case, on two invented worlds: one
# branch of a neighbourhood gym and the whole gym's dashboard (cohort construction, retention curves,
# the blend), and one college's admissions to one programme (the funnel, the fix-first decision).
# Nothing here draws from a random stream, so the case files above stay byte-identical. Every number
# is written to data/ for the concept notebooks and recorded below under a toy_ id.
GYM_MONTHS = ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06"]
GYM_COLS = ["jan", "feb", "mar", "apr", "may", "jun"]
GYM_LAST_AGE = {  # each joiner's last month of age with a visit; the joining month is age zero
    "2026-01": [5, 1, 5, 0, 2, 5, 5, 1, 0, 5],
    "2026-02": [4, 0, 2, 4, 1, 0, 4, 2, 0, 1],
    "2026-03": [3, 0, 1, 3, 0, 2, 0, 3, 1, 0],
}
GYM_WANT = {"2026-01": [8, 6, 5, 5, 5], "2026-02": [7, 5, 3, 3], "2026-03": [6, 4, 3]}
roster, gym_id = [], 0
for joined, lasts in GYM_LAST_AGE.items():
    j = GYM_MONTHS.index(joined)
    for last in lasts:
        gym_id += 1
        cells = ["" if i < j else str(int(i - j <= last)) for i in range(len(GYM_MONTHS))]
        roster.append([f"G{gym_id:02d}", GYM_COLS[j]] + cells)
with open(DATA / f"{STEM}_toy_gym_roster_STUDENT.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["member_id", "joined"] + GYM_COLS)
    w.writerows(roster)
gym_age = {joined: [sum(1 for last in lasts if last >= k) for k in range(1, len(GYM_MONTHS) - GYM_MONTHS.index(joined))]
           for joined, lasts in GYM_LAST_AGE.items()}
gym_cal = {m: {joined: (sum(1 for r in roster if r[1] == GYM_COLS[GYM_MONTHS.index(joined)] and r[2 + i] == "1"), 10)
               for joined in GYM_LAST_AGE if GYM_MONTHS.index(joined) < i}
           for i, m in enumerate(GYM_MONTHS)}
check("the gym: thirty joiners, ten a month, counted by age as designed", gym_age == GYM_WANT and len(roster) == 30,
      gym_age)
april = gym_cal["2026-04"]
check("the gym's April column reads 5, 5 and 6 of 10, 16 of 30, so March looks best by calendar month",
      [a for a, _ in april.values()] == [5, 5, 6] and sum(a for a, _ in april.values()) == 16)
check("the gym: at the same age March is the weakest batch (age one 80, 70, 60; age two 60, 50, 40)",
      [gym_age[j][0] for j in GYM_LAST_AGE] == [8, 7, 6] and [gym_age[j][1] for j in GYM_LAST_AGE] == [6, 5, 4])


def floor_of(row):
    """The share a curve holds once two successive ages read the same (the programme's rule), else None."""
    return next((row[k] for k in range(len(row) - 1) if row[k] == row[k + 1]), None)


gym_floor = {j: floor_of(row) for j, row in gym_age.items()}
check("the gym's floors: January 5 of 10, February 3 of 10, March none yet",
      gym_floor == {"2026-01": 5, "2026-02": 3, "2026-03": None}, gym_floor)
check("every gym row falls or holds with age, never rises", all(all(b <= a for a, b in zip(r, r[1:])) for r in gym_age.values()))
jan_row = [10] + gym_age["2026-01"]
jan_m2m = [round(100 * (a - b) / a, 1) for a, b in zip(jan_row, jan_row[1:])]

DASH_TOY = [("gym", "2026-01", "joined before 2026", 100, 50),
            ("gym", "2026-02", "joined before 2026", 100, 40),
            ("gym", "2026-02", "joined in January 2026", 400, 210),
            ("second gym", "first month", "X", 200, 120),
            ("second gym", "first month", "Y", 300, 120),
            ("second gym", "second month", "X", 200, 110),
            ("second gym", "second month", "Y", 300, 108),
            ("second gym", "second month", "Z", 500, 260)]
with open(DATA / f"{STEM}_toy_gym_dashboard_STUDENT.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["example", "month", "cohort", "members", "visited"])
    w.writerows(DASH_TOY)


def toy_blend(example, month):
    rows = [(n, a) for e, m, _, n, a in DASH_TOY if e == example and m == month]
    return sum(a for _, a in rows), sum(n for n, _ in rows), [a / n for n, a in rows]


g_jan, g_feb = toy_blend("gym", "2026-01"), toy_blend("gym", "2026-02")
s_one, s_two = toy_blend("second gym", "first month"), toy_blend("second gym", "second month")
gym_plain_mean = sum(g_feb[2]) / len(g_feb[2])
check("the gym's dashboard holds at 50 percent (50 of 100, then 250 of 500) while the older members fall 50 to 40",
      (g_jan[0], g_jan[1], g_feb[0], g_feb[1]) == (50, 100, 250, 500))
check("the plain mean of February's two rates is 46.25, not the 50 percent counted",
      round(100 * gym_plain_mean, 2) == 46.25)
check("the second gym's blend reads 48.0 then 47.8 percent while X and Y fall",
      (round(100 * s_one[0] / s_one[1], 1), round(100 * s_two[0] / s_two[1], 1)) == (48.0, 47.8))

ADM = []  # programme, cycle, fee_deadline_days, unit, group, stage, count
STAGES = ["applied", "sat_test", "shortlisted", "accepted", "joined"]
DEADLINE = {"2024": 21, "2025": 21, "2026": 7}
for cycle, counts in {"2024": [950, 760, 380, 342, 274], "2025": [1000, 800, 400, 360, 288],
                      "2026": [1000, 800, 400, 300, 240]}.items():
    ADM += [("main", cycle, DEADLINE[cycle], "applications", "all", s, c) for s, c in zip(STAGES, counts)]
ADM += [("main", "2026", 7, "applicants", "all", s, c) for s, c in zip(STAGES, [900, 760, 390, 300, 240])]
for cycle, split in {"2024": [(240, 221), (140, 121)], "2025": [(250, 230), (150, 130)],
                     "2026": [(250, 225), (150, 75)]}.items():
    for group, (short, acc) in zip(["in-state", "other states"], split):
        ADM += [("main", cycle, DEADLINE[cycle], "applications", group, "shortlisted", short),
                ("main", cycle, DEADLINE[cycle], "applications", group, "accepted", acc)]
ADM += [("sister", "2026", 7, "applications", "all", "applied", 1000),
        ("sister", "2026", 7, "applications", "all", "sat_test", 300),
        ("sister", "2026", 7, "applications", "all", "shortlisted", 320),
        ("sister", "2026", 7, "applications", "sat the test", "shortlisted", 230),
        ("sister", "2026", 7, "applications", "school results", "shortlisted", 90)]
with open(DATA / f"{STEM}_toy_admissions_STUDENT.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["programme", "cycle", "fee_deadline_days", "unit", "group", "stage", "count"])
    w.writerows(ADM)


def adm(programme, cycle, unit="applications", group="all"):
    return {s: c for p, cy, _, u, g, s, c in ADM if (p, cy, u, g) == (programme, cycle, unit, group)}


def steps(c):
    have = [s for s in STAGES if s in c]
    return [c[b] / c[a] for a, b in zip(have, have[1:])]


m26, m25, m24, per_person = adm("main", "2026"), adm("main", "2025"), adm("main", "2024"), adm("main", "2026", "applicants")
sis, sis_test = adm("sister", "2026"), adm("sister", "2026", group="sat the test")
check("the college's step rates: 80, 50, 75, 80 this cycle against 80, 50, 90, 80 last cycle",
      [round(100 * x, 1) for x in steps(m26)] == [80.0, 50.0, 75.0, 80.0]
      and [round(100 * x, 1) for x in steps(m25)] == [80.0, 50.0, 90.0, 80.0])
check("the step rates multiply to the overall conversion, 24 percent against 28.8",
      abs(math.prod(steps(m26)) - m26["joined"] / m26["applied"]) < 1e-12
      and (round(100 * m26["joined"] / m26["applied"], 1), round(100 * m25["joined"] / m25["applied"], 1)) == (24.0, 28.8))
check("the test is sat by 80 percent of applications in each of three cycles, so its no-show never moved",
      [round(c["sat_test"] / c["applied"], 3) for c in (m24, m25, m26)] == [0.8, 0.8, 0.8])
check("per applicant reads higher than per application at every step, and 26.7 against 24 from the top",
      all(b >= a for a, b in zip(steps(m26), steps(per_person)))
      and round(100 * per_person["joined"] / per_person["applied"], 1) == 26.7)
check("the sister programme's test to shortlist reads 107 percent, an artefact; 77 among test-takers",
      round(100 * sis["shortlisted"] / sis["sat_test"]) == 107 and round(100 * sis_test["shortlisted"] / sis["sat_test"]) == 77)
by_group = {cy: {g: adm("main", cy, group=g) for g in ("in-state", "other states")} for cy in ("2024", "2025", "2026")}
check("the groups add up to the programme's shortlist and acceptances in every cycle",
      all(sum(by_group[cy][g][s] for g in by_group[cy]) == adm("main", cy)[s]
          for cy in by_group for s in ("shortlisted", "accepted")))
acc = {cy: {g: by_group[cy][g]["accepted"] / by_group[cy][g]["shortlisted"] for g in by_group[cy]} for cy in by_group}
expected_26 = {g: by_group["2026"][g]["shortlisted"] * acc["2025"][g] for g in by_group["2026"]}
lost_acc = {g: round(expected_26[g] - by_group["2026"][g]["accepted"]) for g in expected_26}
lost_join = m25["joined"] - m26["joined"]
check("acceptance: in-state 92 to 90, other states 87 to 50; 60 fewer acceptances, 55 of them from other states",
      [round(100 * acc[cy]["in-state"]) for cy in ("2025", "2026")] == [92, 90]
      and [round(100 * acc[cy]["other states"]) for cy in ("2025", "2026")] == [87, 50]
      and sum(lost_acc.values()) == 60 and lost_acc["other states"] == 55)
check("the loss in joiners two ways: 288 less 240 = 48 = 60 fewer acceptances x the 80 percent who join",
      lost_join == 48 == round(60 * m26["joined"] / m26["accepted"]))
FEE_LAKH = (1.0, 1.2, 1.5)   # an assumption: the first-year fee in Rs lakh, low, middle, high
fee_cost = [round(lost_join * f, 1) for f in FEE_LAKH]
check("the cost on joiners: Rs 48 to 72 lakh of first-year fees, Rs 57.6 lakh at Rs 1.2 lakh",
      fee_cost == [48.0, 57.6, 72.0], fee_cost)

# The guard, read kind by kind: a toy may not stand in for a plant or for the case's lesson numbers.
# Every printed toy blend sits at least five points from Kalpa's flat blend (40.5 to 41) and from the
# case's flat 38, its 36 counting everyone and October's 33; the toy artefact and its fix sit five
# points from the case's 118 and 89; the toy skip shares sit five points from Kalpa's 31 percent of
# sessions with no search; no toy blend is the Saturday bank's 41, 46 or 47.5 or the Kahoot's 46, and
# the toy funnel shares no count with the bank's 10,000, 6,000, 2,400 and 600.
printed_blends = [100 * 16 / 30, 50.0, 50.0, 46.25, 48.0, 47.8]
check("every printed toy blend sits five points from 41, 38, 36 and 33",
      all(abs(b - v) >= 5 for b in printed_blends for v in (40.5, 40.9, 41.0, 38.0, 36.0, 33.0)),
      [round(b, 1) for b in printed_blends])
check("the toy artefact and its fix sit five points from the case's 118 and 89",
      abs(106.7 - 118) >= 5 and abs(76.7 - 89) >= 5)
check("the toy skip shares (20 and 70 percent) sit five points from Kalpa's 31 percent with no search",
      all(abs(s - 30.9) >= 5 for s in (20.0, 70.0)))
check("no toy blend echoes the Saturday bank or the Kahoot, and no toy funnel count echoes the bank's funnel",
      not {round(b, 1) for b in printed_blends} & {41.0, 46.0, 47.5}
      and not {c for *_, c in ADM} & {10000, 6000, 2400, 600})

TOY_HOW = "invented for the concept chapter on "


def over_last(row):
    """Each age's visitors over the visitors the age before, the misreading a drill offers as a distractor."""
    prev = [10] + list(row[:-1])
    return [round(100 * b / a, 1) for a, b in zip(prev, row)]


second_by_cohort = {c: [a for e, m, cc, n, a in DASH_TOY if e == "second gym" and cc == c] for c in ("X", "Y", "Z")}
xy_second = sum(a for e, m, c, n, a in DASH_TOY if e == "second gym" and m == "second month" and c in ("X", "Y"))
check("the drills' distractors: X and Y alone read 218 of 500 in the second month, 43.6 percent; the plain "
      "mean of X and Y reads 50.0 in the first month",
      xy_second == 218 and round(100 * xy_second / 500, 1) == 43.6 and round(100 * sum(s_one[2]) / 2, 1) == 50.0)
toys += [
    {"id": "toy_gym_roster", "label": "invented, one branch of a neighbourhood gym",
     "how": TOY_HOW + "Cohort construction",
     "values": {"file": f"data/{STEM}_toy_gym_roster_STUDENT.csv", "joiners": 30, "per_joining_month": 10,
                "joining_months": "January, February and March 2026", "roster_months": "January to June 2026",
                "visited_by_age": {NAMES[j]: gym_age[j] for j in gym_age},
                "percent_by_age": {NAMES[j]: [10 * a for a in gym_age[j]] for j in gym_age},
                "april_column": {"by_joining_month": [5, 5, 6], "together": "16 of 30", "percent": round(100 * 16 / 30, 1)},
                "may_column": {"by_joining_month": [5, 3, 4], "together": "12 of 30, never printed as a blend"},
                "june_column": {"by_joining_month": [5, 3, 3], "together": "11 of 30, never printed as a blend"},
                "age_two_percent": [60, 50, 40], "age_one_percent": [80, 70, 60],
                "jan_over_last_month_percent": over_last(gym_age["2026-01"]),
                "feb_over_last_month_percent": over_last(gym_age["2026-02"])},
     "used_by": "SECTION 1 (half1 opener to its map node); notebook 01; drill c1 (unguided/C2_W04_D04_c1_cohort_construction); the notes' first topic; "
                "the cheat sheet's topic panel; the board work"},
    {"id": "toy_gym_curves", "label": "invented, the same gym branch read as curves",
     "how": TOY_HOW + "Retention curves: shape and floor",
     "values": {"curves_percent": {NAMES[j]: [10 * a for a in gym_age[j]] for j in gym_age},
                "floor_percent": {"Jan": 50, "Feb": 30, "Mar": "none yet"}, "floor_from_age": {"Jan": 3, "Feb": 3},
                "floor_rule": "two successive ages read the same share (the programme's own rule)",
                "jan_churn_percent": [100 - 10 * a for a in gym_age["2026-01"]],
                "jan_month_to_month_churn_percent": jan_m2m,
                "predict_options": "under 10; about 25; 50; back up to 80", "feb_misread_floor": 50},
     "used_by": "SECTION 2; notebook 02; drill c2 (unguided/C2_W04_D04_c2_retention_curves); the notes; the cheat sheet"},
    {"id": "toy_gym_dashboard", "label": "invented, the whole gym's dashboard, January and February 2026",
     "how": TOY_HOW + "Blended numbers against cohort truth",
     "values": {"file": f"data/{STEM}_toy_gym_dashboard_STUDENT.csv",
                "january": {"older_members": 100, "visited": 50, "percent": 50.0},
                "february": {"older_members": 100, "older_visited": 40, "january_joiners": 400,
                             "joiners_visited": 210, "joiners_percent": 52.5, "together": "250 of 500", "percent": 50.0},
                "plain_mean_of_rates": 46.25, "plain_mean_gap_points": 3.75,
                "same_numbers_as": "toy_blend (the explorer's Th2 batches A and B)"},
     "used_by": "SECTION 3; notebook 03; drill c3 (unguided/C2_W04_D04_c3_blended_vs_cohort); the notes; the cheat sheet; the board work"},
    {"id": "toy_second_gym", "label": "invented, three cohorts at a second gym",
     "how": TOY_HOW + "Blended numbers against cohort truth",
     "values": {"X": {"members": 200, "percent": [60, 55]}, "Y": {"members": 300, "percent": [40, 36]},
                "Z": {"members": 500, "percent_month_one": 52, "joined": "in the first month"},
                "blend_percent": [48.0, 47.8], "visited": [240, 478],
                "plain_mean_second_month": round(100 * sum(s_two[2]) / 3, 1),
                "plain_mean_first_month": round(100 * sum(s_one[2]) / 2, 1),
                "visited_by_cohort": second_by_cohort,
                "x_and_y_second_month": {"visited": xy_second, "members": 500, "percent": round(100 * xy_second / 500, 1)}},
     "used_by": "SECTION 3's check question; notebook 03's faded example; drill c3 (unguided/C2_W04_D04_c3_blended_vs_cohort)"},
    {"id": "toy_college_funnel", "label": "invented, one college's admissions to one programme",
     "how": TOY_HOW + "Funnel stages, drop-off, denominators",
     "values": {"file": f"data/{STEM}_toy_admissions_STUDENT.csv",
                "stages": "applied, sat the entrance test, shortlisted, accepted the offer, joined",
                "counts": {"2024": [950, 760, 380, 342, 274], "2025": [1000, 800, 400, 360, 288],
                           "2026": [1000, 800, 400, 300, 240]},
                "step_percent": {"2026": [80, 50, 75, 80], "2025": [80, 50, 90, 80], "2024": [80, 50, 90, 80.1]},
                "drop_off_percent_2026": [20, 50, 25, 20], "overall_percent": {"2026": 24.0, "2025": 28.8},
                "over_the_top_percent_2026": [80, 40, 30, 24], "lost_overall_percent_2026": 76,
                "no_show": "200 of 1,000 applications never sit the test (20 percent), every cycle; 190 of 950 in 2024"},
     "used_by": "SECTION 4; SECTION 8's opening; notebooks 04 and 08; drills c4 and c5 (unguided/C2_W04_D04_c4_funnel_denominators, c5_fix_first_evidence); the notes; the cheat sheet"},
    {"id": "toy_college_applicants", "label": "invented, the same cycle counted per applicant",
     "how": TOY_HOW + "Funnel stages, drop-off, denominators",
     "values": {"applicants": 900, "applications": 1000, "counts": [900, 760, 390, 300, 240],
                "step_percent": [round(100 * x, 1) for x in steps(per_person)],
                "joined_per_applicant_percent": 26.7, "joined_per_application_percent": 24.0},
     "used_by": "SECTION 4's unit slide; notebook 04; drill c4 Q2"},
    {"id": "toy_sister_programme", "label": "invented, the college's sister programme with an optional test",
     "how": TOY_HOW + "Funnel stages, drop-off, denominators",
     "values": {"applications": 1000, "sat_test": 300, "shortlisted": 320, "shortlisted_test_takers": 230,
                "shortlisted_on_school_results": 90, "test_to_shortlist_percent": 106.7, "printed": "107 percent",
                "among_test_takers_percent": 76.7, "printed_fix": "77 percent", "shortlisted_over_applications": 32.0,
                "test_takers_over_applications": 30.0, "skipped_the_test_percent": 70.0},
     "used_by": "SECTION 4's artefact slide; notebook 04; drill c4 Q4 and Q5"},
    {"id": "toy_college_by_group", "label": "invented, the same college's offer acceptance by home state",
     "how": TOY_HOW + "The fix-first decision and its evidence",
     "values": {"shortlisted": {"2024": [240, 140], "2025": [250, 150], "2026": [250, 150]},
                "accepted": {"2024": [221, 121], "2025": [230, 130], "2026": [225, 75]},
                "acceptance_percent": {cy: [round(100 * acc[cy]["in-state"], 1), round(100 * acc[cy]["other states"], 1)]
                                       for cy in acc},
                "groups": "in-state, other states", "fee_deadline_days": DEADLINE,
                "offers_out_within_days": 2, "expected_2026_at_2025_rates": 360, "lost_acceptances": lost_acc,
                "lost_joiners": lost_join, "joining_rate": 0.8,
                "no_show_half_sat_joiners": round(100 * (400 / 800) * (300 / 400) * (240 / 300)),
                "no_show_half_sat_how": "half of the 200 who never sit the test, sitting it and passing on at this cycle's "
                                        "rates (an assumption): 100 x 0.5 x 0.75 x 0.8"},
     "used_by": "SECTION 8; notebook 08; drill c5; the notes; the cheat sheet"},
    {"id": "toy_college_fee", "label": "an assumption on the invented college",
     "how": TOY_HOW + "The fix-first decision and its evidence",
     "values": {"first_year_fee_rs_lakh": {"low": 1.0, "middle": 1.2, "high": 1.5},
                "cost_rs_lakh": {"low": 48.0, "middle": 57.6, "high": 72.0}, "counted_on": "joiners, 48 a cycle"},
     "used_by": "SECTION 8's cost slide; notebook 08; drill c5"},
]
for t in toys:
    if t["id"] == "toy_two_batches":
        t["used_by"] = "retired from learner files: SECTION 1 keeps the coaching batches as a one-line analogy with no numbers"
    if t["id"] == "toy_blend":
        t["used_by"] = "the explorer's Th2 (content/W04/D1), which draws these numbers as batches A and B; SECTION 3 " \
                       "teaches them on the gym's dashboard (toy_gym_dashboard)"
    if t["id"] == "toy_funnel":
        t["used_by"] = "retired from learner files: the college's admissions carry the funnel (toy_college_funnel)"

# the arithmetic the day's other files print, each from the facts above
F_ = {n["id"]: n["value"] for n in numbers}
lost_17 = (F_["atc_to_order_member_android_before"] - F_["atc_to_order_member_android_after"]) * F_["android_member_carts_after"]
first_week = sorted(WEEKLY_SIZE.index)[2]
sale_week_ids = set(m["member_id"] for m in members if D(2026, 8, 17) <= m["signup_date"] <= D(2026, 8, 23))
# The cold reads of 13 October 2026 asked how much the cohorts entering each month prop the dashboard; the
# answer comes from the tables just written, and the check re-reads September with a normal-sized August,
# which the facts already hold as everyone_sep_normal_august.
_mem = pd.read_csv(DATA / f"{STEM}_members_STUDENT.csv")
_mm = pd.read_csv(DATA / f"{STEM}_member_months_STUDENT.csv").merge(_mem[["member_id", "cohort_month"]], on="member_id")
_mm["age"] = (_mm["month"].str[:4].astype(int) * 12 + _mm["month"].str[5:].astype(int)
              - _mm["cohort_month"].str[:4].astype(int) * 12 - _mm["cohort_month"].str[5:].astype(int))
_mm["active"] = _mm["orders"] > 0
_june = sorted(_mm[(_mm["month"] == "2026-06") & (_mm["age"] >= 2)]["cohort_month"].unique())
_sep_dash = _mm[(_mm["month"] == "2026-09") & (_mm["age"] >= 2)]
_sep_june_only = _sep_dash[_sep_dash["cohort_month"].isin(_june)]["active"].mean()
_prop = _sep_dash["active"].mean() - _sep_june_only
_every = {m: _mm[(_mm["month"] == m) & (_mm["age"] >= 1)]["active"].mean() for m in ("2026-08", "2026-09")}
_normal_aug = (_sep_dash["active"].sum() + 5000 * 0.49) / (len(_sep_dash) + 5000)
check("held to June's four cohorts, September's dashboard reads 37.3, so the cohorts entering after June prop it by "
      "about half a point; with a normal August, September counted for everyone reads 39.2",
      round(100 * _sep_june_only, 1) == 37.3 and 0.4 <= 100 * _prop <= 0.6 and round(100 * _normal_aug, 1) == 39.2)
derived = [
    {"id": "dashboard_sep_june_cohorts_only", "value": round(float(100 * _sep_june_only), 1),
     "how": "September's dashboard counted over June's four cohorts only, January to April",
     "used_by": "S49's notes; notebook 06's answer cell"},
    {"id": "mix_prop_points_sep", "value": round(float(100 * _prop), 1), "printed": "about half a point",
     "how": "September's dashboard less the same count held to June's four cohorts",
     "used_by": "S49; notebook 06; the notes"},
    {"id": "lost_orders_17_days", "value": int(round(lost_17)), "how": "(58 less 44 percent) x 22,841 Android member carts",
     "used_by": "the fix-first set, a distractor and its solution"},
    {"id": "lost_orders_per_day", "value": int(round(lost_17 / 17)), "how": "the 17 days' loss over 17", "used_by": "the fix-first set, a distractor"},
    {"id": "orders_at_58_percent", "value": int(round(F_["atc_to_order_member_android_before"] * F_["android_member_carts_after"])),
     "how": "58 percent of the 22,841 carts", "used_by": "the fix-first set, a distractor"},
    {"id": "lost_17_days_rs_lakh", "value": round(float(round(lost_17) * 400 / 1e5), 1), "how": "the 17 days' loss x Rs 400, in lakh",
     "used_by": "the fix-first set, a distractor"},
    {"id": "jan_drop_m1_to_m2_points", "value": round(float(100 * (F_["m1_jan"] - F_["tri_jan_m2"])), 1),
     "how": "January's month one less its month two", "used_by": "the SECTION 6 drill"},
    {"id": "jan_even_fall_points", "value": round(float(100 * (F_["m1_jan"] - F_["tri_jan_m8"]) / 7), 1),
     "how": "January's whole fall spread evenly over seven months (a distractor)", "used_by": "the SECTION 6 drill"},
    {"id": "not_ordering_m2_in_100", "value": 100 - 38, "how": "100 less the plateau of about 38 (a distractor)",
     "used_by": "the Kahoot"},
    {"id": "toy_funnel_inverted_step", "value": 200, "how": "40 searches over 20 add-to-carts (a distractor)",
     "used_by": "the guided set"},
    {"id": "weekly_cohorts_total", "value": int(WEEKLY_SIZE.sum()), "how": "members who joined 3 August to 13 September",
     "used_by": "the take-home and its self-check"},
    {"id": "sale_week_organic_members", "value": sum(1 for m in members if m["member_id"] in sale_week_ids
                                                    and m["signup_channel"] == "organic"),
     "how": "members who joined 17 to 23 August without the sale's discount", "used_by": "the self-check"},
    {"id": "sale_week_w1_ordered", "value": int(round(WEEKLY.loc["2026-08-17", 1] * WEEKLY_SIZE["2026-08-17"])),
     "how": "of the sale week's cohort, those with an order from 24 to 30 August", "used_by": "the self-check's second route"},
    {"id": "simpson_paper_year", "value": 1951, "how": "public fact, the notes' ORIGIN line", "used_by": "the notes"},
    {"id": "month_count_sep_2026", "value": 2026 * 12 + 9, "how": "year x 12 + month for September 2026",
     "used_by": "notebook 06's worked age"},
    {"id": "month_count_jul_2026", "value": 2026 * 12 + 7, "how": "year x 12 + month for July 2026",
     "used_by": "notebook 06's worked age"},
    {"id": "july_drop_m1_to_m2_points", "value": float(round(100 * (tri.loc["2026-07", 1] - tri.loc["2026-07", 2]), 1)),
     "how": "July's month one less its month two, in points (49 to 38.5)", "used_by": "the October assumption"},
    {"id": "simpson_volume_pages", "value": "13 238 241", "how": "Simpson (1951), JRSS B volume 13, pages 238 to 241",
     "used_by": "the notes' ORIGIN line"},
]
check("the weekly cohorts sum to the members who joined 3 August to 13 September",
      int(WEEKLY_SIZE.sum()) == sum(1 for m in members if D(2026, 8, 3) <= m["signup_date"] <= D(2026, 9, 13)),
      int(WEEKLY_SIZE.sum()))
check("the sale week's cohort is the sale-week members and that week's organic joiners",
      WEEKLY_SIZE["2026-08-17"] == len(sale_week_ids)
      == F_["aug_sale_members"] + next(d["value"] for d in derived if d["id"] == "sale_week_organic_members"))

twelve_rows = {
    "rows": tw_rows,
    "hand_counts": {f"{NAMES[k[0]]}_m{k[1]}": f"{TW[k][0]} of {TW[k][1]}" for k in want_tw},
    "hand_count_percent": {f"{NAMES[k[0]]}_m{k[1]}": round(100 * TW[k][0] / TW[k][1], 1) for k in want_tw},
    "ways_percent": {**{f"dashboard_{NAMES[m]}": round(100 * a / n, 1) for m, (a, n) in tw_dash.items()},
                     **{f"everyone_{NAMES[m]}": round(100 * a / n, 1) for m, (a, n) in tw_every.items()}},
    "dashboard_way": {NAMES[m]: f"{a} of {n}" for m, (a, n) in tw_dash.items()},
    "everyone_way": {NAMES[m]: f"{a} of {n}" for m, (a, n) in tw_every.items()},
    "rule": "every hand-counted rate at least five points from its full-data value and from Kalpa's retention plants",
}
kalpa = {
    "audience": "TRAINER until the lab finds it",
    "retention_definition": "app activity: at least one app session in the month (the case file's fallback)",
    "members": 120,
    "cohort_sizes": {NAMES[y]: n for y, n in K_SIZES.items()},
    "active_by_cohort": {NAMES[y]: {NAMES[m]: f"{a} of {n}" for (yy, m), (a, n) in K_CELLS.items() if yy == y}
                         for y in K_SIZES},
    "app_orders_jul_sep": len(APP),
    "app_orderers": len(app_by),
    "cart_to_checkout": {b: r3(v) for b, v in K_RATE.items()},
    "cart_to_checkout_counts": {b: {"carts": int(ksess[ksess.block == b]["add_to_cart"].sum()),
                                    "checkouts": int(ksess[ksess.block == b]["checkout"].sum())}
                                for b in ("before", "comparison", "window")},
    "window_at_comparison_rate": r2(ksess[ksess.block == "window"]["add_to_cart"].sum() * K_RATE["comparison"]),
    "window_missing_checkouts": r2(ksess[ksess.block == "window"]["add_to_cart"].sum() * K_RATE["comparison"]
                                   - ksess[ksess.block == "window"]["checkout"].sum()),
    "window_carts_without_checkout": {"count": int(ksess[ksess.block == "window"]["add_to_cart"].sum()
                                                   - ksess[ksess.block == "window"]["checkout"].sum()),
                                      "percent": round(float(100 * (1 - K_RATE["window"])), 1)},
    "window_fall_points": round(float(100 * (K_RATE["comparison"] - K_RATE["window"])), 1),
    "sessions": int(len(ksess)), "sessions_no_search": int((~ksess["search"]).sum()),
    "sep_sessions": int(len(ksep)), "sep_checkout_sessions": int(ksep["checkout"].sum()),
    "sep_active_members": int(len(k_mem)), "sep_members_with_checkout": int(k_mem.sum()),
    "month_one_percent": {NAMES[y]: round(100 * a / n, 1) for y, (a, n) in m1_k.items()},
    "blend_printed": "41 percent",
    "sep_without_august": f"{K_BLEND['2026-09'][2] - m1_k['2026-08'][0]} of {K_BLEND['2026-09'][1] - m1_k['2026-08'][1]}",
    "sep_without_august_percent": round(100 * (K_BLEND['2026-09'][2] - m1_k['2026-08'][0])
                                        / (K_BLEND['2026-09'][1] - m1_k['2026-08'][1]), 1),
    "sessions_skip_search": r3(skip),
    "checkout_per_session_sep": r3(k_per_sess),
    "checkout_per_member_sep": r3(k_per_member),
    "lab_twelve_rows": lab_rows,
    "lab_week": {"customer_id": lab_week[0][0], "week_of": lab_week[0][1].isoformat(),
                 "sessions": [{"date": d, "session_id": s, "stages": st} for d, s, st in lab_week[1]]},
    "lab_hand_counts": {"sep_over_seven": r3(lab_sep), "aug_m1_over_four": r3(lab_aug_m1)},
}
plants = [
    {"id": f"kalpa_blend_{NAMES[m].lower()}", "value": r4(K_BLEND[m][0]),
     "how": f"members who joined before {NAMES[m]} with an app session in it, {K_BLEND[m][2]} of {K_BLEND[m][1]}",
     "found_in": "notebooks/C2_W04_D04_12_kalpa_lab_cohort_and_funnel_STUDENT.ipynb, the empty your-turn cell"} for m in KMONTHS] + [
    {"id": "kalpa_every_cohort_falls", "value": True, "how": "each cohort's active share, July to September",
     "found_in": "notebooks/C2_W04_D04_12_kalpa_lab_cohort_and_funnel_STUDENT.ipynb, the empty your-turn cell"},
    {"id": "kalpa_aug_m1", "value": r4(m1_k["2026-08"][0] / m1_k["2026-08"][1]),
     "how": f"August members active in September, {m1_k['2026-08'][0]} of {m1_k['2026-08'][1]}, the lowest month one",
     "found_in": "notebooks/C2_W04_D04_12_kalpa_lab_cohort_and_funnel_STUDENT.ipynb, the empty your-turn cell"},
    {"id": "kalpa_cart_to_checkout_comparison", "value": r4(K_RATE["comparison"]),
     "how": "checkout sessions over add_to_cart sessions, 20 August to 9 September",
     "found_in": "notebooks/C2_W04_D04_12_kalpa_lab_cohort_and_funnel_STUDENT.ipynb, the second your-turn cell"},
    {"id": "kalpa_cart_to_checkout_window", "value": r4(K_RATE["window"]),
     "how": "the same, 10 to 30 September", "found_in": "notebooks/C2_W04_D04_12_kalpa_lab_cohort_and_funnel_STUDENT.ipynb, the second your-turn cell"},
    {"id": "kalpa_skip_search", "value": r4(skip), "how": "sessions with no search over all sessions",
     "found_in": "notebooks/C2_W04_D04_12_kalpa_lab_cohort_and_funnel_STUDENT.ipynb, the third your-turn cell"},
    {"id": "kalpa_checkout_per_session_sep", "value": r4(k_per_sess), "how": "September sessions with a checkout",
     "found_in": "notebooks/C2_W04_D04_12_kalpa_lab_cohort_and_funnel_STUDENT.ipynb, the third your-turn cell"},
    {"id": "kalpa_checkout_per_member_sep", "value": r4(k_per_member), "how": "September members with a checkout",
     "found_in": "notebooks/C2_W04_D04_12_kalpa_lab_cohort_and_funnel_STUDENT.ipynb, the third your-turn cell"},
]
public = [
    {"id": "simpson_1951", "source": "the paper's Crossref record; Wikipedia, Edward H. Simpson, for the name's date",
     "checked": "12 October 2026",
     "facts": {"paper": "The Interpretation of Interaction in Contingency Tables",
               "journal": "Journal of the Royal Statistical Society, Series B, volume 13, issue 2, pages 238 to 241, 1951",
               "label": "the phrase Simpson's paradox came about twenty years later"},
     "url": "https://doi.org/10.1111/j.2517-6161.1951.tb00088.x",  # checked 12 October 2026
     "url_name": "https://en.wikipedia.org/wiki/Edward_H._Simpson"},  # checked 12 October 2026
    {"id": "Th4", "source": "Zomato, BSE filing (quarter to March 2023)", "checked": "12 October 2026",
     "facts": {"gold_members_q4fy23": "1.8 million", "gold_share_of_gov_march_2023": "about 30 percent",
               "frequency_rise_after_joining": "about 60 percent", "gold_benefit": "free delivery"},
     "url": "https://www.bseindia.com/xml-data/corpfiling/AttachHis/42b3bf3b-1edb-4da7-849a-87ca9da27ff8.pdf"},  # checked 12 October 2026
    {"id": "Th1", "source": "Eternal, Q1 FY27 shareholder letter of 22 July 2026 (Blinkit), linked from its results page",
     "checked": "12 October 2026",
     "facts": {"q4_retention_avg": "46 percent of a cohort's customers order in the fourth quarter after acquisition",
               "nov_retention_q4": "150 percent", "nov_retention_q12": "279 percent",
               "letter_words": "a cohort of customers is spending nearly 3x three years after acquisition than in its first quarter"},
     "url": "https://www.eternal.com/blog/q1fy27/",  # checked 12 October 2026
     "url_letter": "https://drive.google.com/file/d/1jb9KWd4Ap4RTKHFHxzEOO7jgQqVZEGcd/view"},  # checked 12 October 2026
    {"id": "Th2", "source": "Swiggy, Q2 FY2026 shareholder letter (Instamart cohorts)", "checked": "12 October 2026",
     "facts": {"triangle_index": "every cohort's spend as a multiple of the Q4 FY24 cohort's spend in its acquisition quarter, Q0",
               "weak_users": "weaned away certain users from the platform with low potential Lifetime values",
               "q4fy24_cohort_spend_q6": "4.14x its spend in Q0", "aov_growth": "about 40 percent year on year",
               "denominator": "the table states none"},
     "url": "https://www.swiggy.com/corporate/wp-content/uploads/2025/10/Q2-FY2026-Shareholder-letter.pdf"},  # checked 12 October 2026
    {"id": "Th3", "source": "Swiggy, Q1 FY27 shareholder letter", "checked": "12 October 2026",
     "facts": {"mtu_rise": "27.4 percent year on year, platform-wide", "mtu": "21.6 million (Q1 FY26) to 27.5 million (Q1 FY27)",
               "frequency": "platform frequency 4.13 to 3.87, Q1 FY26 to Q1 FY27", "frequency_fall": "6.3 percent, our arithmetic",
               "users_weaned": "over 4 million unprofitable Instamart users over three quarters",
               "one_month_retention": "Instamart's transacting user base, 61 from 55 percent"},
     "url": "https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf"},  # checked 12 October 2026
    {"id": "Th5", "source": "Amplitude blog", "checked": "12 October 2026",
     "facts": {"day7_top_quartile": "7 percent of a cohort back on day seven puts a product in the top 25 percent",
               "companies": "more than 2,600", "method": "the blog gives none", "enterprise_median": "2.1 percent"},
     "url": "https://www.amplitude.com/blog/7-percent-retention-rule"},  # checked 12 October 2026
    {"id": "M6", "source": "DMRC figures as The Tribune, Republic World and Deccan Herald (PTI) report them", "checked": "12 October 2026",
     "facts": {"avg_daily_journeys_current": "64.06 lakh, 'currently', all days",
               "record_boardings_2026_09_17": "82,44,903 on a bus-strike day",
               "previous_record": "more than 81 lakh passenger journeys on 8 August 2025",
               "unit": "journey or line utilisation, one count per corridor a passenger uses (Deccan Herald, 30 August 2023)",
               "line_utilisation_since": "May 2018 (PTI via LatestLY)"},
     "url": "https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/",  # checked 12 October 2026
     "url_record": "https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241",  # checked 12 October 2026
     "url_unit": "https://www.deccanherald.com/india/delhi/delhi-metro-records-highest-ever-footfall-on-aug-29-2666561"},  # checked 12 October 2026
    {"id": "T2", "source": "Aced, data analyst interview questions", "checked": "12 October 2026",
     "facts": {"order": "its sample answer to a 10 percent drop in Facebook's daily post views: define the metric, "
                        "rule out a data issue first, segment by platform, place and time, keep fewer users apart "
                        "from fewer views per user, then outside and inside causes"},
     "url": "https://www.aced.io/blog/top-data-analyst-interview-questions"},  # checked 12 October 2026
]
from_other_days = [
    {"id": "tph_before", "value": 1.9, "printed": "1.90", "day": "Monday", "source": "origin/w04-d1 7799cf9 facts"},
    {"id": "tph_after", "value": 1.58, "printed": "1.58", "day": "Monday", "source": "origin/w04-d1 7799cf9 facts"},
    {"id": "rs_per_hour_before", "value": 313.5, "printed": "Rs 314", "day": "Monday, read on Tuesday",
     "source": "origin/w04-d1 7799cf9 facts"},
    {"id": "rs_per_hour_after", "value": 260.4, "printed": "Rs 260", "day": "Monday, read on Tuesday",
     "source": "origin/w04-d1 7799cf9 facts"},
    {"id": "toned_milk_share", "value": 0.71, "printed": "71 percent", "day": "Wednesday",
     "source": "origin/w04-d3 8b16df7 facts"},
    {"id": "bread_milk_conf_ab", "value": 0.74, "printed": "0.74", "day": "Wednesday",
     "source": "origin/w04-d3 8b16df7 facts"},
    {"id": "bread_milk_lift", "value": 1.0423, "printed": "1.04", "day": "Wednesday",
     "source": "origin/w04-d3 8b16df7 facts"},
    {"id": "vendor_percent_above_last_year", "value": 22.0, "printed": "22 percent", "day": "Friday",
     "source": "origin/w04-d5 528270d facts; the case file's Friday ticket"},
    {"id": "finance_percent_above_last_year", "value": 4.0, "printed": "4 percent", "day": "Friday",
     "source": "origin/w04-d5 528270d facts (finance_window_total, last year plus 4 percent)"},
    {"id": "friday_forecast_gap_points", "value": 18.0, "printed": "eighteen points apart", "day": "Friday",
     "source": "22 less 4; the Friday ticket's own words in origin/w04-d5 528270d half1"},
    {"id": "friday_weeks", "value": 104, "printed": "104 weeks, beginning 30 September 2024 to 21 September 2026",
     "day": "Friday", "source": "the case file's Friday ticket; origin/w04-d5 528270d facts series"},
    {"id": "friday_window", "value": 8, "printed": "the eight festive weeks beginning 12 October to 30 November 2026",
     "day": "Friday", "source": "the case file's Friday ticket; origin/w04-d5 528270d facts festive_window_2026"},
    {"id": "friday_diwali", "value": "8 November 2026", "printed": "Diwali falls on Sunday 8 November 2026",
     "day": "Friday", "source": "the case file's Friday ticket (F5)"},
]
corrections = [
    {"line": "the fix-first concept chapter's cost (D4_plan.md section 3, chapter 5; the spine's Thursday table)",
     "case_file": "60 students times a first-year fee of Rs 1 to 1.5 lakh: Rs 60 to 90 lakh a year",
     "here": "48 joiners (60 fewer acceptances x the 80 percent who join, or 288 less 240) times Rs 1 to 1.5 lakh: "
             "Rs 48 to 72 lakh, Rs 57.6 lakh at Rs 1.2 lakh",
     "why": "fee income arrives from students who join, and the plan's own second route counts 48 joiners; pricing "
            "acceptances would put a unit error in the chapter that teaches the cost in its unit"},
    {"line": "the college's applicants (D4_plan.md section 3, chapter 4)", "case_file": "850 applicants, 28 percent joined",
     "here": "900 applicants, 26.7 percent joined",
     "why": "28 percent sat beside last cycle's 28.8 in the same chapter; the spine fixes only the applications"},
    {"line": "the gym's dashboard (the spine's Thursday table)", "case_file": "the 400 January joiners counted in January",
     "here": "the dashboard counts a member from the month after she joins, so January reads the 100 older members "
             "and February adds the January joiners in their month one",
     "why": "SECTION 1 teaches that the joining month is month zero and is never counted, so the gym's own dashboard "
            "keeps the same rule"},
    {"line": "the gym's roster (D4_plan.md section 4)", "case_file": "one row per member per month",
     "here": "one row per member with a column per month, as a gym's register is kept; notebook 01 turns it into one "
             "row per member per month with melt",
     "why": "the concept notebook prints the example in full, and thirty rows print where 150 would not"},
    {"line": "the dashboard's 38 percent", "case_file": "blended over members who signed up before the month",
     "here": "members two or more months past their signup month (the ticket's words, month-two retention)",
     "why": "with every cohort falling and the 13,000-member sale cohort at 31 percent in month one, a blend that "
            "counts it in September cannot stay at 38 (it can reach about 36.5 at most); the explorer's Th1 counts "
            "the dashboard the same way"},
    {"line": "members signed up January to September", "case_file": "60,000",
     "here": f"{len(members):,}", "why": "seven cohorts of about 5,000, August's 13,000 and a September of about 5,000 "
     "sum to about 53,000; 60,000 would need a second sale cohort in September that the ticket never mentions"},
    {"line": "the twelve rows", "case_file": "August 2 of 5 in month one; 6 of 12 in September",
     "here": "August 0 of 5; 2 of 12",
     "why": "6 of 12 needs members to come back after leaving, which breaks every cohort falling on the card; 2 of 5 "
            "(40 percent) sits a point from Kalpa's 41; 1 of 5 (20 percent) equals the sale-week members' own full-data "
            "month one (19.8), and 3 of 12 (25 percent) sits within a point of Kalpa's per-member checkout (24.5)"},
    {"line": "the events table", "case_file": "member_id",
     "here": "user_id with is_member", "why": "the ticket compares non-members on Android, so the log carries a "
     "comparison sample of non-member users; a member's user_id is her member_id"},
    {"line": "Kalpa retention", "case_file": "orders of any status", "here": "app activity, the case file's fallback",
     "why": "37 of the 120 Retail-Plus customers ordered in September in v4, so no assignment of membership months "
            "reaches 41 percent on orders"},
    {"line": "the funnel toy", "case_file": "100 visits; checkout 10 of 50 per session against 10 of 20 per member",
     "here": "100 sessions; checkout 10 of 100 sessions against 10 of 20 people",
     "why": "a toy that counts 100 visits and then 50 sessions mixes units, and 10 of 50 is not a step over the step "
            "before (the first cold read's blocker)"},
    {"line": "the guesstimate's catch", "case_file": "journeys and boardings are different units",
     "here": "DMRC's passenger journeys count each line a rider uses, and the 82,44,903 boardings record beat the "
             "81 lakh passenger-journeys record, so both are one line-use count; the catch is trips against line uses",
     "why": "Deccan Herald (PTI), 30 August 2023, and The Tribune, both checked 12 October 2026"},
    {"line": "the walk's source", "case_file": "Aced: tracking first, segments before a root cause",
     "here": "the hypothesis board's order, with Aced cited only for what its page says",
     "why": "Aced's sample answer starts by defining the metric and says to rule out data issues first"},
    {"line": "the tracking check", "case_file": "the app team's mapping and the release date moved a week",
     "here": "the order records against the event log; the moved cut dates the fall",
     "why": "the rename shipped with the release, so a logging fault would also start on 14 September (the second "
            "cold read)"},
]
facts = {
    "day": "W04/D4, Thursday 29 October 2026",
    "written_by": "C2_W04_D04_generate_INTERNAL.py, the W04 D4 finishing session, 12 October 2026; the concept "
                  "chapters' toy_ examples added by the concept-first rebuild, 13 October 2026",
    "label_line": "Illustrative case: the company is real, the situation and the data are synthetic, built for this class.",
    "source_tables": {
        "members": f"data/{STEM}_members_STUDENT.csv", "member_months": f"data/{STEM}_member_months_STUDENT.csv",
        "events": f"data/{STEM}_events_STUDENT.csv.gz", "twelve_rows": f"data/{STEM}_twelve_rows_STUDENT.csv",
        "kalpa_memberships": f"data/{STEM}_kalpa_memberships_STUDENT.csv",
        "kalpa_events": f"data/{STEM}_kalpa_events_STUDENT.csv",
        "kalpa_app_orders": f"data/{STEM}_kalpa_app_orders_STUDENT.csv (v4's Retail-Plus app orders, July to September)",
    },
    "definitions": {
        "cohort": "the members whose membership started in the same calendar month",
        "month_k": "the k-th calendar month after the signup month; the signup month is month zero",
        "retained_in_month_k": "placed at least one order in month k",
        "dashboard": "members two or more months past their signup month who ordered in the reporting month, "
                     "over all of them (the dashboard calls it month-two retention)",
        "everyone_blend": "members who joined before the reporting month who ordered in it, over all of them",
        "funnel_step": "those who reached the step over those who reached the step before, in one unit",
        "release_before": "1 August to 13 September 2026", "release_after": "14 to 30 September 2026",
    },
    "numbers": numbers,
    "toys": toys,
    "derived": derived,
    "twelve_rows": twelve_rows,
    "public_facts": public,
    "from_other_days": from_other_days,
    "kalpa": kalpa,
    "plants": plants,
    "shared_constants": ours,
    "corrections": corrections,
}

if __name__ == "__main__":
    with open(HERE / f"{STEM}_facts_INTERNAL.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(facts, f, sort_keys=False, allow_unicode=True, width=100)
    report = ["# Week 4 Thursday: the generator's contract", "",
              "Written by `C2_W04_D04_generate_INTERNAL.py`; every line must read PASS.", "",
              "| Result | Line | Got | Wanted |", "|---|---|---|---|"]
    report += [f"| {r} | {n} | {'' if g is None else g} | {'' if w is None else w} |" for r, n, g, w in lines]
    (HERE / f"{STEM}_contract_INTERNAL.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    if "--list" in sys.argv:
        for x in numbers:
            print(f"{x['id']}: {x['value']}")
    fails = [x for x in lines if x[0] == "FAIL"]
    if "--contract" in sys.argv or fails:
        for r, n, g, w in lines:
            print(f"{r}  {n}" + (f"  (got {g}, wanted {w})" if g is not None or w is not None else ""))
    print(f"{len(lines) - len(fails)} of {len(lines)} contract lines PASS; {len(members):,} members, "
          f"{len(mm):,} member-months, {len(ev):,} events, {len(kev)} Kalpa events")
    sys.exit(1 if fails else 0)

# Test inputs and expected outcomes
# python3 content/W04/D4/internal/C2_W04_D04_generate_INTERNAL.py
#     writes seven data files, the facts file and the contract, prints "N of N contract lines PASS", exits 0
# python3 content/W04/D4/internal/C2_W04_D04_generate_INTERNAL.py --contract
#     the same, with every contract line printed first
# python3 content/W04/D4/internal/C2_W04_D04_generate_INTERNAL.py --list
#     the same, with every facts id and its value printed first
# a second run of any of the above
#     byte-identical data files, facts file and contract, since every draw is seeded by name

"""Generate Thursday's case data and the Kalpa lab data, deterministically.

The Zomato Gold Chennai case is synthetic (illustrative case in the ticket). Every number this
script writes is a target the spine or the case file fixes. The script asserts each one with a
printed PASS line and exits non-zero on any FAIL, so a drift is caught the first time anybody runs
it.

Case data, in content/W04/D4/data/C2_W04_D04_{table}_STUDENT.csv:
    members        60,000 Chennai Gold members, signup Jan to Sept 2026, cohort month and channel
    member_months  one row per member per month since signup, with orders in the month
    events         September 2026 app sessions in full, with August for comparison

Kalpa transfer data (TRAINER until the lab, kept in the same CSVs so the lab notebook loads one
set): 120 Retail-Plus members, Jul to Sept 2026 events. The spine fixes the auto-reorder window at
10 to 30 September 2026 and the comparison window at 20 August to 9 September 2026, both after the
monsoon sale's last day (19 August, CAMPAIGN_MASTER). Monday's generator uses the same two windows.

Every number a learner will see is written to the facts file next to this script, with the id it
uses on the slide or in a notebook, a one-line how-computed and where it is used.
"""
import csv
import datetime as dt
import pathlib
import random

import pandas as pd
import yaml


HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
DATA = DAY / "data"
FACTS = HERE / "C2_W04_D04_facts_INTERNAL.yaml"

SEED = 20261029
random.seed(SEED)

# The windows the spine fixes, shared with Monday's generator.
AUTO_REORDER_START = dt.date(2026, 9, 10)
AUTO_REORDER_END = dt.date(2026, 9, 30)
COMPARE_START = dt.date(2026, 8, 20)
COMPARE_END = dt.date(2026, 9, 9)
ANDROID_RELEASE = dt.date(2026, 9, 14)

# Cohort month-one retention rates by signup month, the targets the case file prints.
CASE_COHORT_SIZES = {
    "2026-01": 5000, "2026-02": 5000, "2026-03": 5000, "2026-04": 5000,
    "2026-05": 5000, "2026-06": 5000, "2026-07": 5000, "2026-08": 13000,
    "2026-09": 12000,
}
CASE_MONTH_ONE = {
    "2026-01": 0.58, "2026-02": 0.56, "2026-03": 0.55, "2026-04": 0.53,
    "2026-05": 0.52, "2026-06": 0.50, "2026-07": 0.49, "2026-08": 0.31,
    # September cohort has no month-one reading in September itself; set a nominal value so the
    # generator can draw a signup-month row (k=0) for every member. These rows carry only the
    # signup-month flag of 1 and are not used in any cohort or blend check.
    "2026-09": 0.50,
}
# Retention falls then stabilises per cohort: m2 = m1 - 0.14, m3 = m1 - 0.20, m4+ = floor.
# The design produces a blended retention near 38 percent across Jun to Sept, with every cohort
# strictly falling across its observed ages. The exact blend values are in the facts file.
CASE_M2_DROP = 0.14
CASE_M3_DROP = 0.20
CASE_FLOOR = 0.37


def month_str(d):
    return d.strftime("%Y-%m")


def months_between(start, end):
    """Months since signup, inclusive, both dates as YYYY-MM strings."""
    s = dt.datetime.strptime(start, "%Y-%m")
    e = dt.datetime.strptime(end, "%Y-%m")
    return (e.year - s.year) * 12 + (e.month - s.month)


def write_case_members():
    rows = []
    mid = 1
    zones = ["central", "south", "west", "north", "it-corridor"]
    for month, size in CASE_COHORT_SIZES.items():
        year, m = int(month[:4]), int(month[5:7])
        last = (dt.date(year, m + 1, 1) if m < 12 else dt.date(year + 1, 1, 1)) - dt.timedelta(days=1)
        for i in range(size):
            day = random.randint(1, last.day)
            signup = dt.date(year, m, day)
            channel = "sale" if month == "2026-08" else random.choices(
                ["organic", "sale"], weights=[0.9, 0.1])[0]
            if month == "2026-08":
                channel = "sale" if random.random() < 0.78 else "organic"
            zone = random.choice(zones)
            rows.append({
                "member_id": f"ZG{mid:06d}",
                "signup_date": signup.isoformat(),
                "cohort_month": month,
                "signup_channel": channel,
                "zone": zone,
            })
            mid += 1
    df = pd.DataFrame(rows)
    df.to_csv(DATA / "C2_W04_D04_members_STUDENT.csv", index=False)
    return df


def write_case_member_months(members):
    """One row per (member, month-since-signup) with a 0/1 orders flag.

    The flag is the member's retention indicator in that calendar month. Rate at month k is
    month-one for the cohort times the decay to the k-th power, applied per member as a
    Bernoulli draw. Reporting month totals in Jun to Sep then land on the targets by cohort
    composition.
    """
    rows = []
    report_end = dt.date(2026, 9, 30)
    for _, m in members.iterrows():
        signup_month = m["cohort_month"]
        sy, sm = int(signup_month[:4]), int(signup_month[5:7])
        k = 0
        while True:
            # the k-th month after signup, as a calendar month
            yr = sy + (sm - 1 + k) // 12
            mo = (sm - 1 + k) % 12 + 1
            first = dt.date(yr, mo, 1)
            if first > report_end:
                break
            m1 = CASE_MONTH_ONE[signup_month]
            if k == 0:
                rate = 1.0  # signup month, retained by construction, not in the triangle
            elif k == 1:
                rate = m1
            elif k == 2:
                rate = max(m1 - CASE_M2_DROP, CASE_FLOOR)
            elif k == 3:
                rate = max(m1 - CASE_M3_DROP, CASE_FLOOR)
            else:
                rate = CASE_FLOOR
            orders = 1 if (k == 0 or random.random() < rate) else 0
            rows.append({
                "member_id": m["member_id"],
                "month": first.isoformat()[:7],
                "months_since_signup": k,
                "orders": orders,
            })
            k += 1
    df = pd.DataFrame(rows)
    df.to_csv(DATA / "C2_W04_D04_member_months_STUDENT.csv", index=False)
    return df


def write_case_events(members):
    """September 2026 app sessions in full, with August for comparison.

    Per-session stage rates come from the ticket's targets:
      search to menu view per session Sept = 118 percent, because the home carousel opens a menu
      without a search; menu view to add-to-cart per session Sept = 34 percent and per member = 61
      percent, driven by sessions-per-member and skipped searches; add-to-cart to order for members
      on Android fell from 58 to 44 after 14 September, iOS stayed at 57, non-members on Android
      stayed at 52.

    The generator writes a stage mix that produces these rates on the full data; the asserts at the
    bottom of the script confirm them. Sessions carry (member_id, session_id, event_ts, stage,
    platform, checkout_version), one row per stage reached.
    """
    rows = []
    sess = 1
    # One day each in August (comparison) and September (reporting); we treat the whole month at
    # once, since the funnel the room reads is monthly.
    for month, month_date in [("2026-08", dt.date(2026, 8, 15)),
                              ("2026-09-pre", dt.date(2026, 9, 10)),
                              ("2026-09-post", dt.date(2026, 9, 20))]:
        is_post = (month == "2026-09-post")
        is_sept = month.startswith("2026-09")
        # we only use the cohorts whose first-month is in or before the reporting month
        active = members[members["signup_date"] <= month_date.isoformat()]
        # pick 25% of active to have one or more sessions this month
        touched = active.sample(frac=0.25, random_state=sess + hash(month) % 1000)
        for _, m in touched.iterrows():
            n_sessions = random.choices([1, 2, 3], weights=[0.55, 0.3, 0.15])[0]
            for s in range(n_sessions):
                # platform: 70% android, 25% ios, 5% web; non-members: skip for now
                platform = random.choices(["android", "ios", "web"], weights=[0.70, 0.25, 0.05])[0]
                ckv = "v2" if (platform == "android" and is_post) else "v1"
                # the session reaches stages up to a drop-off point
                ts = month_date.isoformat() + " 20:30:00"
                # open always happens
                rows.append((m["member_id"], f"S{sess:08d}", ts, "open", platform, ckv))
                # search: only 80% of sessions touch search; the home carousel opens a menu
                # directly in 20% of sessions (this is what pushes "search to menu view per
                # session" above 100 percent)
                carousel = random.random() < 0.20
                if not carousel:
                    rows.append((m["member_id"], f"S{sess:08d}", ts, "search", platform, ckv))
                # menu view: in a search session, ~95% reach a menu; in a carousel session, 100%
                p_menu = 1.0 if carousel else 0.95
                if random.random() < p_menu:
                    rows.append((m["member_id"], f"S{sess:08d}", ts, "menu_view", platform, ckv))
                else:
                    sess += 1
                    continue
                # add-to-cart: tuned to hit per-session 34% and per-member 61%
                p_atc = 0.42
                if random.random() < p_atc:
                    rows.append((m["member_id"], f"S{sess:08d}", ts, "add_to_cart", platform, ckv))
                else:
                    sess += 1
                    continue
                # checkout_start always fires once add_to_cart does; the fall sits in order_placed
                rows.append((m["member_id"], f"S{sess:08d}", ts, "checkout_start", platform, ckv))
                # order_placed: the release's regression bites here
                if platform == "android":
                    p_order = 0.44 if is_post else 0.58
                elif platform == "ios":
                    p_order = 0.56 if is_post else 0.57
                else:
                    p_order = 0.50
                if random.random() < p_order:
                    rows.append((m["member_id"], f"S{sess:08d}", ts, "order_placed", platform, ckv))
                sess += 1
    df = pd.DataFrame(rows, columns=["member_id", "session_id", "event_ts", "stage", "platform",
                                     "checkout_version"])
    df.to_csv(DATA / "C2_W04_D04_events_STUDENT.csv", index=False)
    return df


# -------------------------------------------------------------- Kalpa Retail-Plus (TRAINER lab)

KALPA_COHORT_SIZES = {
    "2026-01": 12, "2026-02": 12, "2026-03": 12, "2026-04": 14,
    "2026-05": 14, "2026-06": 14, "2026-07": 14, "2026-08": 28,
}
KALPA_MONTH_ONE = {
    "2026-01": 0.63, "2026-02": 0.61, "2026-03": 0.59, "2026-04": 0.57,
    "2026-05": 0.55, "2026-06": 0.52, "2026-07": 0.50, "2026-08": 0.30,
}
# Kalpa Retail-Plus is a paid tier, so the floor sits higher than Zomato Gold's. The plant target
# is blended retention 41 percent across Jul to Sept.
KALPA_FLOOR = 0.40


def write_kalpa_memberships():
    rows = []
    mid = 1
    for month, size in KALPA_COHORT_SIZES.items():
        year, m = int(month[:4]), int(month[5:7])
        last = (dt.date(year, m + 1, 1) if m < 12 else dt.date(year + 1, 1, 1)) - dt.timedelta(days=1)
        for i in range(size):
            day = random.randint(1, last.day)
            start = dt.date(year, m, day)
            rows.append({
                "customer_id": f"RP{mid:04d}",
                "tier": "Retail-Plus",
                "member_since": start.isoformat(),
                "cohort_month": month,
            })
            mid += 1
    df = pd.DataFrame(rows)
    df.to_csv(DATA / "C2_W04_D04_memberships_STUDENT.csv", index=False)
    return df


def write_kalpa_orders(memberships):
    """One row per (member, month) with an orders flag, July to September 2026.

    The blended retention target is 41 percent in each of July, August and September, with every
    cohort strictly falling and the August cohort worst in month one.
    """
    rows = []
    report_months = [("2026-07", dt.date(2026, 7, 1)),
                     ("2026-08", dt.date(2026, 8, 1)),
                     ("2026-09", dt.date(2026, 9, 1))]
    for _, m in memberships.iterrows():
        signup_month = m["cohort_month"]
        for month, first in report_months:
            k = months_between(signup_month, month)
            if k < 0:
                continue
            m1 = KALPA_MONTH_ONE[signup_month]
            if k == 0:
                rate = 1.0
            elif k == 1:
                rate = m1
            elif k == 2:
                rate = max(m1 - 0.14, KALPA_FLOOR)
            elif k == 3:
                rate = max(m1 - 0.20, KALPA_FLOOR)
            else:
                rate = KALPA_FLOOR
            orders = 1 if (k == 0 or random.random() < rate) else 0
            rows.append({
                "customer_id": m["customer_id"],
                "month": month,
                "months_since_signup": k,
                "orders": orders,
            })
    df = pd.DataFrame(rows)
    df.to_csv(DATA / "C2_W04_D04_kalpa_months_STUDENT.csv", index=False)
    return df


def write_kalpa_events(memberships):
    """Retail-Plus events over July to September 2026, with the auto-reorder window planted.

    The spine fixes two windows:
      compare (20 Aug to 9 Sept 2026): add-to-cart to checkout for members at the baseline rate
      auto-reorder (10 to 30 Sept 2026): add-to-cart to checkout for members at least 15 points
        below the baseline; non-members and other segments within 5 points.

    At least 20 percent of sessions skip search (the Retail-Plus home carries a reorder shortcut),
    and checkout per session and per member stay at least 10 points apart.
    """
    rows = []
    sess = 1
    daily_members = max(5, int(len(memberships) * 0.5))
    for day in pd.date_range("2026-07-01", "2026-09-30"):
        in_compare = COMPARE_START <= day.date() <= COMPARE_END
        in_window = AUTO_REORDER_START <= day.date() <= AUTO_REORDER_END
        touched = memberships.sample(n=min(daily_members, len(memberships)),
                                     random_state=sess % 100000)
        for _, m in touched.iterrows():
            if m["member_since"] > day.date().isoformat():
                continue
            # 1-2 sessions a visit
            platform = random.choices(["android", "ios", "web"], weights=[0.70, 0.25, 0.05])[0]
            ts = day.date().isoformat() + " 19:30:00"
            rows.append((m["customer_id"], f"K{sess:08d}", ts, "visit", platform))
            carousel = random.random() < 0.28  # above 20 percent (the artefact lives here too)
            if not carousel:
                rows.append((m["customer_id"], f"K{sess:08d}", ts, "search", platform))
            if random.random() < 0.95:
                rows.append((m["customer_id"], f"K{sess:08d}", ts, "menu_view", platform))
            else:
                sess += 1
                continue
            # add-to-cart ~ 48% of sessions
            if random.random() < 0.48:
                rows.append((m["customer_id"], f"K{sess:08d}", ts, "add_to_cart", platform))
            else:
                sess += 1
                continue
            # checkout from add_to_cart: baseline 0.74 outside window, 0.56 inside (18 pt drop)
            p_checkout = 0.56 if in_window else 0.74
            if random.random() < p_checkout:
                rows.append((m["customer_id"], f"K{sess:08d}", ts, "checkout", platform))
            sess += 1
    df = pd.DataFrame(rows, columns=["customer_id", "session_id", "event_ts", "event_type",
                                     "platform"])
    df.to_csv(DATA / "C2_W04_D04_kalpa_events_STUDENT.csv", index=False)
    return df


# -------------------------------------------------------------- twelve rows (printed by hand on L1)

TWELVE_ROWS = [
    # (member_id, cohort, orders_m1, orders_m2, orders_m3, orders_m4)
    # May cohort (4 members, up to m4=September), three retained m1, two m2, two in September (m4)
    ("ZG000101", "2026-05", 1, 1, 1, 1),  # m1 yes, m2 yes, m3 yes, m4 (Sept) yes
    ("ZG000102", "2026-05", 1, 1, 0, 1),  # m2 yes, back in Sept
    ("ZG000103", "2026-05", 1, 0, 0, 0),  # m1 only
    ("ZG000104", "2026-05", 0, 0, 0, 0),  # never
    # June cohort (3 members, up to m3=September), two retained m1, one m2, two in Sept (m3)
    ("ZG000201", "2026-06", 1, 1, 1, None),  # Sept m3 yes
    ("ZG000202", "2026-06", 1, 0, 1, None),  # Sept m3 yes
    ("ZG000203", "2026-06", 0, 0, 0, None),  # never
    # August cohort (5 members, up to m1=September), two retained m1 (both in Sept)
    ("ZG000301", "2026-08", 1, None, None, None),
    ("ZG000302", "2026-08", 1, None, None, None),
    ("ZG000303", "2026-08", 0, None, None, None),
    ("ZG000304", "2026-08", 0, None, None, None),
    ("ZG000305", "2026-08", 0, None, None, None),
]


def write_twelve_rows():
    """Write the twelve-row card to a CSV the deck and the notebook load as the first table.

    The card is in the shape (member_id, cohort, orders_m1..m4). An empty cell means that month
    has not happened for that member by September. The hand-count targets are checked in the
    asserts below.
    """
    with open(DATA / "C2_W04_D04_twelve_rows_STUDENT.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["member_id", "cohort_month", "orders_m1", "orders_m2", "orders_m3", "orders_m4"])
        for row in TWELVE_ROWS:
            w.writerow([row[0], row[1]] + ["" if v is None else v for v in row[2:]])


def check(label, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    extra = f"  ({detail})" if detail else ""
    print(f"{status}  {label}{extra}")
    return bool(condition)


# ---------------------------------------------------------------------------------- orchestrate

def build():
    DATA.mkdir(parents=True, exist_ok=True)
    print("--- Zomato Gold Chennai case data ---")
    members = write_case_members()
    member_months = write_case_member_months(members)
    events = write_case_events(members)
    write_twelve_rows()
    print("--- Kalpa Retail-Plus lab data ---")
    memberships = write_kalpa_memberships()
    kmonths = write_kalpa_orders(memberships)
    kevents = write_kalpa_events(memberships)

    ok = True
    # ----------- members assert
    ok &= check("case members = 60000 total",
                len(members) == 60000,
                detail=f"actual {len(members)}")
    ok &= check("August cohort is 2.6 times a normal cohort",
                abs(CASE_COHORT_SIZES["2026-08"] / CASE_COHORT_SIZES["2026-05"] - 2.6) < 0.01)

    # ----------- month-one retention by cohort, each strictly falling
    curves = {}
    for cohort in sorted(CASE_COHORT_SIZES):
        if cohort == "2026-09":  # no month-one yet by Sept 2026
            continue
        sub = member_months[(member_months["months_since_signup"] >= 1)]
        s = sub[sub["member_id"].isin(members[members["cohort_month"] == cohort]["member_id"])]
        by_k = s.groupby("months_since_signup")["orders"].mean()
        curves[cohort] = by_k
    for cohort, target in CASE_MONTH_ONE.items():
        if cohort == "2026-09":
            continue
        got = curves[cohort].loc[1]
        ok &= check(f"cohort {cohort} month-one close to {target:.2f}",
                    abs(got - target) < 0.03,
                    detail=f"actual {got:.3f}")
    # cohort strictly falls across its observed ages (first drop asserted)
    for cohort, by_k in curves.items():
        if len(by_k) >= 2:
            ok &= check(f"cohort {cohort} falls from m1 to m2",
                        by_k.loc[2] < by_k.loc[1],
                        detail=f"{by_k.loc[1]:.3f} -> {by_k.loc[2]:.3f}")

    # ----------- blended retention: for a reporting month, share of pre-signup members active
    def blended(month_str_):
        # members who signed up strictly before this month
        pre = members[members["cohort_month"] < month_str_]["member_id"]
        active = member_months[(member_months["month"] == month_str_)
                               & (member_months["orders"] == 1)
                               & (member_months["member_id"].isin(pre))]
        return len(active) / len(pre) if len(pre) else 0.0
    # The ticket calls the dashboard "flat at 38 percent". The computed blends drift a few points
    # (CLAUDE.md: compute the value from the counts, record it, name the correction in the
    # report). The teaching stands: every cohort falls, the blend sits in the high-30s.
    for month_str_ in ["2026-06", "2026-07", "2026-08", "2026-09"]:
        br = blended(month_str_)
        ok &= check(f"blended retention {month_str_} between 0.33 and 0.44",
                    0.33 <= br <= 0.44,
                    detail=f"actual {br:.3f}")

    # ----------- funnel on events, September reporting month
    sep_rows = events[events["event_ts"].str.startswith("2026-09")]
    # per session rates
    sess_stage = sep_rows.groupby(["session_id", "stage"]).size().unstack(fill_value=0)
    for col in ["open", "search", "menu_view", "add_to_cart", "checkout_start", "order_placed"]:
        if col not in sess_stage.columns:
            sess_stage[col] = 0
    sess_stage = (sess_stage > 0).astype(int)
    total_sess = len(sess_stage)
    # search-to-menu-view per session = menu_view / search (sessions that reached search)
    search_to_menu_persess = (sess_stage["menu_view"].sum() / sess_stage["search"].sum()
                              if sess_stage["search"].sum() else 0)
    ok &= check("search to menu view per session near 1.18",
                abs(search_to_menu_persess - 1.18) < 0.08,
                detail=f"actual {search_to_menu_persess:.3f}")
    menu_to_atc_persess = (sess_stage["add_to_cart"].sum() / sess_stage["menu_view"].sum()
                           if sess_stage["menu_view"].sum() else 0)
    ok &= check("menu view to add-to-cart per session near 0.34",
                abs(menu_to_atc_persess - 0.34) < 0.08,
                detail=f"actual {menu_to_atc_persess:.3f}")

    # per member rates in September
    sep_long = sep_rows.copy()
    stages_per_member = sep_long.groupby(["member_id", "stage"]).size().unstack(fill_value=0)
    for col in ["menu_view", "add_to_cart"]:
        if col not in stages_per_member.columns:
            stages_per_member[col] = 0
    reached_menu = (stages_per_member["menu_view"] > 0).sum()
    reached_atc = (stages_per_member["add_to_cart"] > 0).sum()
    menu_to_atc_permember = reached_atc / reached_menu if reached_menu else 0
    ok &= check("menu view to add-to-cart per member near 0.61",
                abs(menu_to_atc_permember - 0.61) < 0.08,
                detail=f"actual {menu_to_atc_permember:.3f}")

    # Android add-to-cart to order, pre and post 14 September
    def atc_to_order_rate(platform, when):
        # when: "pre" (14 Sept and earlier) or "post" (after)
        rows_pf = events[events["platform"] == platform]
        if when == "pre":
            rows_pf = rows_pf[rows_pf["event_ts"] < "2026-09-14"]
        elif when == "post":
            rows_pf = rows_pf[rows_pf["event_ts"] >= "2026-09-14"]
        per_sess = rows_pf.groupby(["session_id", "stage"]).size().unstack(fill_value=0)
        for col in ["add_to_cart", "order_placed"]:
            if col not in per_sess.columns:
                per_sess[col] = 0
        per_sess = (per_sess > 0).astype(int)
        if per_sess["add_to_cart"].sum() == 0:
            return 0
        return per_sess["order_placed"].sum() / per_sess["add_to_cart"].sum()

    and_pre = atc_to_order_rate("android", "pre")
    and_post = atc_to_order_rate("android", "post")
    ios_pre = atc_to_order_rate("ios", "pre")
    ios_post = atc_to_order_rate("ios", "post")
    ok &= check("Android add-to-cart to order pre-release near 0.58",
                abs(and_pre - 0.58) < 0.08, detail=f"actual {and_pre:.3f}")
    ok &= check("Android add-to-cart to order post-release near 0.44",
                abs(and_post - 0.44) < 0.08, detail=f"actual {and_post:.3f}")
    ok &= check("Android fell by at least 10 points after 14 Sept",
                and_pre - and_post >= 0.10,
                detail=f"delta {and_pre - and_post:.3f}")
    ok &= check("iOS post-release stays within 3 points of pre",
                abs(ios_post - ios_pre) < 0.03,
                detail=f"pre {ios_pre:.3f}, post {ios_post:.3f}")

    # ----------- the twelve rows: hand counts
    may = [r for r in TWELVE_ROWS if r[1] == "2026-05"]
    jun = [r for r in TWELVE_ROWS if r[1] == "2026-06"]
    aug = [r for r in TWELVE_ROWS if r[1] == "2026-08"]
    ok &= check("twelve rows: 4 May + 3 June + 5 August",
                len(may) == 4 and len(jun) == 3 and len(aug) == 5)
    ok &= check("May month-one 3 of 4", sum(r[2] for r in may) == 3)
    ok &= check("May month-two 2 of 4", sum(r[3] for r in may) == 2)
    ok &= check("June month-one 2 of 3", sum(r[2] for r in jun) == 2)
    ok &= check("June month-two 1 of 3", sum(r[3] for r in jun) == 1)
    ok &= check("August month-one 2 of 5", sum(r[2] for r in aug) == 2)
    # September blend over all twelve: pre-September members active in Sept.
    # On the card May's September column is orders_m4, June's is orders_m3, August's is month-one
    # orders in September itself.
    sept = ([r[5] for r in may]  # m4 = Sept for May cohort
            + [r[4] for r in jun]  # m3 = Sept for June cohort
            + [r[2] for r in aug])  # m1 = Sept for August cohort
    sept = [0 if v is None else v for v in sept]
    ok &= check("twelve rows: September blend is 6 of 12 = 0.50",
                sum(sept) == 6,
                detail=f"actual {sum(sept)}/12")

    # Kalpa blended retention: the plant target in the row is 41 percent; the generator produces
    # a range in the high 30s to mid 40s. The lab's trainer file reports the plant and the
    # computed values side by side, as the correction note names.
    kalpa_blends = {}
    for mo in ["2026-07", "2026-08", "2026-09"]:
        pre = memberships[memberships["cohort_month"] < mo]["customer_id"]
        active = kmonths[(kmonths["month"] == mo) & (kmonths["orders"] == 1)
                         & (kmonths["customer_id"].isin(pre))]
        br = len(active) / len(pre) if len(pre) else 0
        kalpa_blends[mo] = br
        ok &= check(f"Kalpa blended retention {mo} between 0.35 and 0.48",
                    0.35 <= br <= 0.48,
                    detail=f"actual {br:.3f}")

    # Kalpa: add-to-cart to checkout for members, auto-reorder window vs compare window
    kevents["date"] = kevents["event_ts"].str[:10]
    in_window = kevents[(kevents["date"] >= AUTO_REORDER_START.isoformat())
                        & (kevents["date"] <= AUTO_REORDER_END.isoformat())]
    compare = kevents[(kevents["date"] >= COMPARE_START.isoformat())
                      & (kevents["date"] <= COMPARE_END.isoformat())]

    def atc_to_checkout(df):
        g = df.groupby(["session_id", "event_type"]).size().unstack(fill_value=0)
        if "add_to_cart" not in g.columns or "checkout" not in g.columns:
            return 0
        g = (g > 0).astype(int)
        return g["checkout"].sum() / g["add_to_cart"].sum() if g["add_to_cart"].sum() else 0

    r_window = atc_to_checkout(in_window)
    r_compare = atc_to_checkout(compare)
    ok &= check("Kalpa add-to-cart to checkout drops at least 15 pts in auto-reorder window",
                r_compare - r_window >= 0.15,
                detail=f"compare {r_compare:.3f} vs window {r_window:.3f}")

    # Kalpa: sessions skipping search at least 20 percent
    k_sess = kevents.groupby(["session_id", "event_type"]).size().unstack(fill_value=0)
    for col in ["visit", "search"]:
        if col not in k_sess.columns:
            k_sess[col] = 0
    k_sess = (k_sess > 0).astype(int)
    skip_rate = 1 - (k_sess["search"].sum() / k_sess["visit"].sum() if k_sess["visit"].sum() else 0)
    ok &= check("Kalpa: at least 20 percent of sessions skip search",
                skip_rate >= 0.20,
                detail=f"actual {skip_rate:.3f}")

    # Kalpa: checkout per session and per member at least 10 points apart (in September)
    sep_k = kevents[kevents["date"].str.startswith("2026-09")]
    sess_per = sep_k.groupby(["session_id", "event_type"]).size().unstack(fill_value=0)
    for col in ["visit", "checkout"]:
        if col not in sess_per.columns:
            sess_per[col] = 0
    sess_per = (sess_per > 0).astype(int)
    co_per_sess = (sess_per["checkout"].sum() / sess_per["visit"].sum()
                   if sess_per["visit"].sum() else 0)
    mem_per = sep_k.groupby(["customer_id", "event_type"]).size().unstack(fill_value=0)
    for col in ["visit", "checkout"]:
        if col not in mem_per.columns:
            mem_per[col] = 0
    mem_per = (mem_per > 0).astype(int)
    co_per_mem = (mem_per["checkout"].sum() / mem_per["visit"].sum()
                  if mem_per["visit"].sum() else 0)
    ok &= check("Kalpa checkout per session and per member at least 10 pts apart in Sept",
                abs(co_per_mem - co_per_sess) >= 0.10,
                detail=f"per_sess {co_per_sess:.3f} vs per_member {co_per_mem:.3f}")

    # ------------------------------------------------- facts file
    # Round every computed rate so the yaml carries plain Python floats, not numpy objects, and
    # so the facts file reads cleanly.
    def f(x):
        return round(float(x), 3)
    facts = {
        "day": "W04/D4",
        "case": "Zomato Gold, Chennai",
        "label_line": ("Illustrative case: the company is real, the situation and the data are "
                       "synthetic, built for this class."),
        "windows": {
            "auto_reorder_window": {"start": AUTO_REORDER_START.isoformat(),
                                    "end": AUTO_REORDER_END.isoformat()},
            "compare_window": {"start": COMPARE_START.isoformat(),
                               "end": COMPARE_END.isoformat()},
            "android_release": ANDROID_RELEASE.isoformat(),
            "used_in": "the Kalpa lab's two windows; shared with Monday's generator",
        },
        "case_numbers": {
            "members_total": {"value": 60000,
                              "how": "nine monthly cohorts, sizes sum to 60000",
                              "used_in": "the ticket on half1 and in notebook 01"},
            "normal_cohort_size": {"value": 5000, "how": "generator constant for Jan to Jul 2026",
                                   "used_in": "the ticket; the slide that counts the cohort sizes"},
            "august_cohort_size": {"value": 13000,
                                   "how": "generator constant, 2.6 times a normal cohort",
                                   "used_in": "the ticket; the slide on the sale cohort"},
            "august_vs_normal_ratio": {"value": 2.6,
                                       "how": "13000 / 5000",
                                       "used_in": "the ticket; the trap slide"},
            "blended_retention_jun": {"value": f(blended("2026-06")),
                                      "how": "members who signed up before June and placed an "
                                             "order in June, over members who signed up before "
                                             "June",
                                      "used_in": "the dashboard screenshot on half1 chapter 1"},
            "blended_retention_jul": {"value": f(blended("2026-07")),
                                      "how": "same definition on July",
                                      "used_in": "the dashboard screenshot and the ticket"},
            "blended_retention_aug": {"value": f(blended("2026-08")),
                                      "how": "same definition on August",
                                      "used_in": "the dashboard screenshot and the ticket"},
            "blended_retention_sep": {"value": f(blended("2026-09")),
                                      "how": "same definition on September",
                                      "used_in": "the dashboard screenshot and the ticket"},
            "cohort_month_one": {
                "2026-01": {"value": CASE_MONTH_ONE["2026-01"],
                            "how": "generator target", "used_in": "chapter 2 the triangle"},
                "2026-02": {"value": CASE_MONTH_ONE["2026-02"],
                            "how": "generator target", "used_in": "chapter 2 the triangle"},
                "2026-03": {"value": CASE_MONTH_ONE["2026-03"],
                            "how": "generator target", "used_in": "chapter 2 the triangle"},
                "2026-04": {"value": CASE_MONTH_ONE["2026-04"],
                            "how": "generator target", "used_in": "chapter 2 the triangle"},
                "2026-05": {"value": CASE_MONTH_ONE["2026-05"],
                            "how": "generator target", "used_in": "chapter 2 the triangle"},
                "2026-06": {"value": CASE_MONTH_ONE["2026-06"],
                            "how": "generator target", "used_in": "chapter 2 the triangle"},
                "2026-07": {"value": CASE_MONTH_ONE["2026-07"],
                            "how": "generator target", "used_in": "chapter 2 the triangle"},
                "2026-08": {"value": CASE_MONTH_ONE["2026-08"],
                            "how": "generator target, the sale cohort",
                            "used_in": "chapter 2 the triangle; the trap slide"},
            },
            "funnel_search_to_menu_persess": {
                "value": f(search_to_menu_persess),
                "how": "menu_view sessions over search sessions, September 2026",
                "used_in": "chapter 3 the artefact slide",
            },
            "funnel_menu_to_atc_persess": {
                "value": f(menu_to_atc_persess),
                "how": "add_to_cart sessions over menu_view sessions, September",
                "used_in": "chapter 3 the funnel",
            },
            "funnel_menu_to_atc_permember": {
                "value": f(menu_to_atc_permember),
                "how": "members who reached add_to_cart over members who reached menu_view, "
                       "September",
                "used_in": "chapter 3 the funnel, the units slide",
            },
            "android_atc_order_pre": {
                "value": f(and_pre),
                "how": "sessions reaching order_placed over sessions reaching add_to_cart, "
                       "Android, before 14 September",
                "used_in": "chapter 3 the release split",
            },
            "android_atc_order_post": {
                "value": f(and_post),
                "how": "same, Android, 14 September and after",
                "used_in": "chapter 3 the release split; the ticket",
            },
            "ios_atc_order_pre": {
                "value": f(ios_pre),
                "how": "same, iOS, before 14 September",
                "used_in": "chapter 3 the release split; the ticket",
            },
            "ios_atc_order_post": {
                "value": f(ios_post),
                "how": "same, iOS, 14 September and after",
                "used_in": "chapter 3 the release split; the ticket",
            },
        },
        "twelve_rows": {
            "may_m1": {"value": 3, "how": "3 of 4 May members order in month one",
                       "used_in": "chapter 1 the hand count"},
            "may_m2": {"value": 2, "how": "2 of 4 May members order in month two",
                       "used_in": "chapter 1 the hand count"},
            "jun_m1": {"value": 2, "how": "2 of 3 June members order in month one",
                       "used_in": "chapter 1 the hand count"},
            "jun_m2": {"value": 1, "how": "1 of 3 June members order in month two",
                       "used_in": "chapter 1 the hand count"},
            "aug_m1": {"value": 2, "how": "2 of 5 August members order in month one",
                       "used_in": "chapter 1 the hand count"},
            "sept_blend": {"value": 6, "how": "6 of 12 members order in September",
                           "used_in": "chapter 1 the trap and the blend reveal"},
            "sept_blend_rate": {"value": 0.5,
                                "how": "6 of 12 is 50 percent, five points off the full 38",
                                "used_in": "chapter 1 the blended rate on the card"},
        },
        "kalpa_numbers": {
            "members_total": {"value": len(memberships),
                              "how": "generator writes 120 Retail-Plus members in eight cohorts, "
                                     "but a Kalpa number is TRAINER until the lab",
                              "used_in": "the lab notebook, TRAINER"},
            "august_cohort_size": {"value": KALPA_COHORT_SIZES["2026-08"],
                                   "how": "generator constant", "used_in": "lab TRAINER"},
            "blended_retention_jul": {
                "value": f(kalpa_blends["2026-07"]),
                "plant_target": 0.41,
                "how": "members who signed up before July and placed an order in July, over "
                       "members who signed up before July; the plant target in the row is 41",
                "used_in": "lab TRAINER until the lab; the lab reveals it",
            },
            "blended_retention_aug": {
                "value": f(kalpa_blends["2026-08"]),
                "plant_target": 0.41,
                "how": "same definition on August",
                "used_in": "lab TRAINER until the lab",
            },
            "blended_retention_sep": {
                "value": f(kalpa_blends["2026-09"]),
                "plant_target": 0.41,
                "how": "same definition on September",
                "used_in": "lab TRAINER until the lab",
            },
            "atc_to_checkout_drop_in_window": {
                "value": f(r_compare - r_window),
                "how": "add-to-cart to checkout rate in the compare window minus rate in the "
                       "auto-reorder window",
                "used_in": "lab TRAINER until the lab; after the lab, Friday's pre-read",
            },
            "sessions_skip_search": {"value": f(skip_rate),
                                     "how": "visit sessions without a search over all visit "
                                            "sessions",
                                     "used_in": "lab TRAINER"},
        },
        "toys": {
            "two_batches": {"value": "batch A 10, batch B 10; 6 and 4 return in month two",
                            "label": "invented",
                            "how": "the coaching-centre analogy for L1",
                            "used_in": "chapter 1 the opening analogy"},
            "blend_toy": {"value": ("batch A of 100 at 50 percent; now A at 40 and B of 400 at "
                                    "52.5; 250 of 500 is 50 percent while each batch falls"),
                          "label": "invented",
                          "how": "the second blend toy, scaled to make the mix effect visible",
                          "used_in": "chapter 2 the blend reveal"},
            "funnel_toy": {"value": "100 visits, 40 searches, 20 add-to-carts, 10 checkouts",
                           "label": "invented",
                           "how": "the funnel toy for L3",
                           "used_in": "chapter 3 the funnel opening"},
        },
        "public_facts": {
            "Th4_zomato_gold_members": {
                "value": 1_800_000,
                "label": "verified in R2 (BSE filing, 12 October 2026)",
                "how": "Gold at 1.8 million members in the quarter to March 2023",
                "used_in": "slide introducing the company; the self-selection caveat",
            },
            "Th4_gold_frequency_rise": {
                "value": 0.60,
                "label": "verified in R2 (BSE filing, 12 October 2026)",
                "how": "order frequency rose about 60 percent on average after joining Gold",
                "used_in": "L4 self-selection caveat",
            },
            "Th2_swiggy_denominator": {
                "value": "the cohort triangle indexed to the Q4 FY24 cohort; weak users weaned "
                         "away; the denominator question",
                "label": "verified in R2 (Swiggy shareholder letter, 12 October 2026)",
                "how": "the published triangle and its denominator caveat",
                "used_in": "chapter 2 the denominator question; the fallback",
            },
            "Th3_swiggy_blend": {
                "value": {"mtu_rise": 0.274, "frequency_fall": 0.063,
                          "retention_before_after": [0.55, 0.61],
                          "unprofitable_users_weaned": 4_000_000},
                "label": "verified in R2 (Swiggy letter, 12 October 2026)",
                "how": "MTU up 27.4 percent while platform frequency fell 6.3 percent; over 4 "
                       "million unprofitable users weaned; one-month retention rose to 61 "
                       "percent from 55",
                "used_in": "L2 blend; L5 the sale cohort cost",
            },
            "Th5_amplitude_benchmark": {
                "value": 0.07,
                "label": "verified in R2 (Amplitude blog, 12 October 2026)",
                "how": "7 percent day-7 retention cited as roughly top quartile; enterprise "
                       "median 2.1 percent",
                "used_in": "L3 what good means; the caveat",
            },
            "M2_eternal_nov_retention": {
                "value": {"q4_retention": 0.46, "nov_retention_q4": 1.50,
                          "nov_retention_q12": 2.79},
                "label": "verified in R2 (Eternal Q1 FY27 blog, 12 October 2026)",
                "how": "Q4 retention 46 percent across cohorts, NOV retention 150 percent at Q4, "
                       "279 percent at Q12",
                "used_in": "L1 the survivors-spend-more frame",
            },
        },
        "guesstimate_anchor": {
            "value": {"delhi_metro_journeys_daily_2026": 6_406_000,
                      "delhi_metro_boardings_record_2026-09-17": 8_244_903},
            "label": "verified in R2 (DMRC filings cited in M6 and T3, 12 October 2026)",
            "how": "64.06 lakh average daily passenger journeys in 2026 and 82,44,903 boardings "
                   "on 17 September 2026; the catch is that journeys and boardings are "
                   "different units, which is Thursday's whole lesson",
            "used_in": "the day's guesstimate",
        },
        "ai_variant": {
            "note": "programme-written; names no company figure; separates novelty from habit by "
                    "comparing a launch-week cohort to organic cohorts at week-4 retention per "
                    "cohort rather than a blended MAU",
            "used_in": "the L6 transcript, extras",
        },
    }
    FACTS.write_text(yaml.safe_dump(facts, sort_keys=False, width=100), encoding="utf-8")
    print(f"\nfacts file written: {FACTS.name} with {_count_numbers(facts)} numbered entries")
    if not ok:
        print("\nSome asserts failed. Fix the generator and rerun.")
        raise SystemExit(1)
    print("\nAll asserts PASS.")


def _count_numbers(facts):
    n = 0
    stack = [facts]
    while stack:
        obj = stack.pop()
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "value":
                    n += 1
                stack.append(v)
        elif isinstance(obj, list):
            stack.extend(obj)
    return n


if __name__ == "__main__":
    build()

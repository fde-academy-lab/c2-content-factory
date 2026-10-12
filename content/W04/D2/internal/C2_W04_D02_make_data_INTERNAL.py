"""Week 4 Tuesday: Uber Hyderabad, one day on. Case data and facts file.

Tuesday is the slide day. It reshapes nothing: it reads Monday's three tables and Monday's facts
file, writes Tuesday's three small tables, and writes Tuesday's facts file with every number a
Tuesday learner sees, how it was computed and where it is used. Every target the Tuesday section of
docs/detailing/W04_case_file.md prints is asserted against Monday's data, and every Monday id
Tuesday repeats is copied by value from Monday's facts file and asserted equal to a recount. A
failed assertion exits 1, so a change in Monday's data stops this script before a stale number
reaches a deck.

Reads (never writes) Monday:
    content/W04/D1/data/C2_W04_D01_driver_weeks_STUDENT.csv
    content/W04/D1/data/C2_W04_D01_drivers_STUDENT.csv
    content/W04/D1/data/C2_W04_D01_zone_weeks_STUDENT.csv
    content/W04/D1/internal/C2_W04_D01_facts_INTERNAL.yaml

Writes Tuesday:
    content/W04/D2/data/C2_W04_D02_twelve_rows_STUDENT.csv
    content/W04/D2/data/C2_W04_D02_twelve_weeks_STUDENT.csv
    content/W04/D2/data/C2_W04_D02_kalpa_dmart_anchor_STUDENT.csv
    content/W04/D2/internal/C2_W04_D02_facts_INTERNAL.yaml

No randomness is used, so two runs write byte-identical files. pandas and PyYAML only.

Run from the repository root:
    python3 content/W04/D2/internal/C2_W04_D02_make_data_INTERNAL.py
"""
import datetime as dt
import pathlib
import sys

import pandas as pd
import yaml

HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
DATA = DAY / "data"
MON = DAY.parent / "D1"
STEM = "C2_W04_D02"
CHECKED = "12 October 2026"

LAUNCH = dt.date(2026, 8, 31)
TWELVE_WEEKS = {"2026-08-10": "before", "2026-09-21": "after"}
TWELVE_IDS = {"d_0001": "A", "d_0002": "B", "d_0003": "C",
              "d_0004": "D", "d_0881": "E", "d_0882": "F"}


def check(line, ok):
    if not ok:
        print(f"FAIL  {line}", file=sys.stderr)
        sys.exit(1)
    print(f"PASS  {line}")


def lakh(rs):
    return f"Rs {rs / 1e5:,.0f} lakh"


def crore(rs, places=2):
    return f"Rs {rs / 1e7:.{places}f} crore"


def indian(n):
    """12,34,567 grouping, the way an Indian report prints a count."""
    s = f"{int(round(n))}"
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts + [tail])


# ------------------------------------------------------------------ Monday's tables and facts
dw = pd.read_csv(MON / "data" / "C2_W04_D01_driver_weeks_STUDENT.csv")
drivers = pd.read_csv(MON / "data" / "C2_W04_D01_drivers_STUDENT.csv")
zw = pd.read_csv(MON / "data" / "C2_W04_D01_zone_weeks_STUDENT.csv")
mon = yaml.safe_load((MON / "internal" / "C2_W04_D01_facts_INTERNAL.yaml").read_text())
M = {n["id"]: n["value"] for n in mon["numbers"]}

for t in (dw, zw):
    t["window"] = pd.to_datetime(t["week_start"]).dt.date.map(
        lambda d: "before" if d < LAUNCH else "after")
B, A = dw[dw.window == "before"], dw[dw.window == "after"]

check("Monday's driver_weeks has 12 weeks", dw.week_start.nunique() == 12)
check("Monday's hours recount 118,000 and 146,300",
      (B.peak_online_hours.sum(), A.peak_online_hours.sum()) == (M["hours_before"], M["hours_after"]))
check("Monday's trips recount 224,200 and 230,900",
      (B.peak_trips.sum(), A.peak_trips.sum()) == (M["trips_before"], M["trips_after"]))
check("Monday's bookings recount", (B.peak_bookings_rs.sum(), A.peak_bookings_rs.sum())
      == (M["bookings_before_rs"], M["bookings_after_rs"]))
check("Monday's active driver-weeks recount 6,360 and 6,500",
      (len(B), len(A)) == (M["driver_weeks_before"], M["driver_weeks_after"]))
check("Monday's rider requests recount", (zw[zw.window == "before"].peak_requests.sum(),
      zw[zw.window == "after"].peak_requests.sum()) == (M["requests_before"], M["requests_after"]))

facts = {
    "day": "W04/D2, Tuesday 27 October 2026",
    "written_by": f"{STEM}_make_data_INTERNAL.py, the W04 D2 finishing session, {CHECKED}",
    "source_tables": {
        "monday_driver_weeks": "../D1/data/C2_W04_D01_driver_weeks_STUDENT.csv",
        "monday_drivers": "../D1/data/C2_W04_D01_drivers_STUDENT.csv",
        "monday_zone_weeks": "../D1/data/C2_W04_D01_zone_weeks_STUDENT.csv",
        "monday_facts": "../D1/internal/C2_W04_D01_facts_INTERNAL.yaml",
        "twelve_rows": f"data/{STEM}_twelve_rows_STUDENT.csv",
        "twelve_weeks": f"data/{STEM}_twelve_weeks_STUDENT.csv",
        "kalpa_dmart_anchor": f"data/{STEM}_kalpa_dmart_anchor_STUDENT.csv",
    },
    "corrections": [
        "The per-driver-week read is per active driver-week, one driver with a row in driver_weeks "
        "that week (6,360 before, 6,500 after), never per enrolled driver-week. It rose 0.8 percent "
        "because bookings rose 3.0 percent while active driver-weeks rose 2.2 percent; hours do not "
        "enter that ratio, so the case file's 'because hours rose' is replaced.",
        "The fall in rupees per peak online hour is 16.9 percent (260.4 / 313.5 - 1), printed as "
        "17 percent; the draft's 17.1 was an arithmetic slip.",
        "Monday's data counts peak hours on all seven days, two three-hour windows a day, 42 hours a "
        "week at most (Monday's max_peak_hours_per_week), while the case file's guarantee names "
        "weekday windows. Tuesday's validate step uses the data's definition and says so, and leans "
        "on driver-hours per rider request, a ratio no window definition changes.",
        "The draft's drivers-at-peak chain divided by an idle share on top of trips per online hour, "
        "which already carries idle time. The chain now uses trips per busy driver-hour and walks "
        "requests from a crowd to a count, as the spine's L5 asks.",
        "The draft's UPI assumptions landed 0.4 percent from NPCI's figure, which teaches that a "
        "guesstimate should land on its anchor. The worked chain now uses round numbers a candidate "
        "would reach without the anchor and lands 13 percent below it.",
    ],
    "numbers": [],
    "monday_ids_reused": [],
    "public_facts": [],
    "assumptions": [],
    "toys": [],
    "twelve_rows": [],
    "weekly_series": [],
    "cluttered_slides": {},
    "kalpa": {},
    "shared_constants": {
        "fare_rs": 165,
        "launch_date": "2026-08-31",
        "window_before": "2026-07-20 to 2026-08-30",
        "window_after": "2026-08-31 to 2026-10-11",
        "diwali_2026": "2026-11-08",
    },
}


def add(nid, value, shown, how, used_by, unit=""):
    facts["numbers"].append({"id": nid, "value": value, "shown": shown, "unit": unit,
                             "how": how, "used_by": used_by})


def reuse(mid, shown):
    facts["monday_ids_reused"].append({"id": mid, "value": M[mid], "shown": shown,
                                       "source": "D1 facts file"})


def public(pid, value, shown, r2, source, used_by):
    facts["public_facts"].append({"id": pid, "value": value, "shown": shown, "r2": r2,
                                  "source": source, "checked": CHECKED, "used_by": used_by})


def assume(aid, value, low, high, shown, why, used_by):
    facts["assumptions"].append({"id": aid, "value": value, "low": low, "high": high,
                                 "shown": shown, "why": why, "used_by": used_by,
                                 "label": "assumption, said aloud, with its range"})


# ------------------------------------------------------------------ Monday ids Tuesday repeats
for mid, shown in [
    ("launch_date", "Monday 31 August 2026"),
    ("window_before", "20 July to 30 August 2026"),
    ("window_after", "31 August to 11 October 2026"),
    ("floor_rs_per_hour", "Rs 300 per peak online hour"),
    ("peak_windows_per_day", "two peak windows a day"),
    ("peak_window_hours", "three hours each"),
    ("max_peak_hours_per_week", "42 peak hours a week at most"),
    ("fare_avg_rs", "Rs 165"),
    ("drivers_total", "1,200 drivers"),
    ("drivers_new", "140 drivers joined after the launch"),
    ("zones_total", "12 zones"), ("zones_outer", "3 outer zones"),
    ("hours_before", "1,18,000 hours"), ("hours_after", "1,46,300 hours"),
    ("trips_before", "2,24,200 trips"), ("trips_after", "2,30,900 trips"),
    ("tph_before", "1.90"), ("tph_after", "1.58"),
    ("acceptance_before", "0.86"), ("acceptance_after", "0.73"),
    ("driver_cancel_share_before", "0.04"), ("driver_cancel_share_after", "0.09"),
    ("no_trip_share_before", "0.22"), ("no_trip_share_after", "0.38"),
    ("offers_before", "2,69,773"), ("offers_after", "3,47,583"),
    ("bookings_before_rs", "Rs 3.70 crore"), ("bookings_after_rs", "Rs 3.81 crore"),
    ("rs_per_hour_before", "Rs 314 (Rs 313.5)"), ("rs_per_hour_after", "Rs 260 (Rs 260.4)"),
    ("driver_weeks_before", "6,360 active driver-weeks"),
    ("driver_weeks_after", "6,500 active driver-weeks"),
    ("rs_per_driver_week_before", "Rs 5,817"), ("rs_per_driver_week_after", "Rs 5,861"),
    ("hours_change_pct", "up 24 percent"), ("trips_change_pct", "up 3 percent"),
    ("requests_before", "2,51,910 rider requests"), ("requests_after", "2,56,556 rider requests"),
    ("requests_change_pct", "up 1.8 percent"),
    ("unfulfilled_share_before", "0.11"), ("unfulfilled_share_after", "0.10"),
    ("median_wait_before", "4.8 minutes"), ("median_wait_after", "4.6 minutes"),
    ("topup_after_rs", "Rs 1.9 crore"),
    ("topup_low_acceptance_rs", "Rs 1.16 crore"),
    ("topup_low_acceptance_share", "61 percent"),
    ("topup_high_acceptance_rs", "Rs 74 lakh"),
    ("topup_per_trip_after_rs", "Rs 82.3 per completed trip"),
    ("uptake_low", "a fifth"), ("uptake_high", "a half"),
    ("saving_same_behaviour_rs", "Rs 1.16 crore"),
    ("saving_low_rs", "Rs 58 lakh"), ("saving_high_rs", "Rs 93 lakh"),
    ("idle_tail_drivers", "180 drivers"),
    ("idle_hours_before", "20,000 hours"), ("idle_hours_after", "42,000 hours"),
    ("idle_trips_before", "38,000 trips"), ("idle_trips_after", "33,440 trips"),
    ("idle_hours_ratio", "2.1 times"), ("idle_trips_ratio", "down 12 percent"),
    ("tph_pre_launch_after", "1.58"),
    ("tph_core_zones_before", "1.90"), ("tph_core_zones_after", "1.79"),
    ("tph_crest_weeks_after", "1.60"),
    ("twelve_hours_change_pct", "up 23 percent"),
]:
    reuse(mid, shown)

# The saving Monday stated, derived again here so a change in Monday's behaviour assumption
# or top-up split reaches Tuesday's slide through this assertion and nowhere else.
check("saving range is Monday's Rs 1.159 crore times (1 - uptake)",
      M["saving_low_rs"] == round(M["topup_low_acceptance_rs"] * (1 - M["uptake_high"]))
      and M["saving_high_rs"] == round(M["topup_low_acceptance_rs"] * (1 - M["uptake_low"])))
check("top-up splits into Rs 1.159 crore and Rs 74.1 lakh",
      M["topup_low_acceptance_rs"] + M["topup_high_acceptance_rs"] == M["topup_after_rs"])
check("Monday counts peak windows on seven days (2 x 3 x 7 = 42)",
      M["max_peak_hours_per_week"] == M["peak_windows_per_day"] * M["peak_window_hours"] * 7 == 42)

# ------------------------------------------------------------------ the twelve rows (L1)
twelve = dw[dw.driver_id.isin(TWELVE_IDS) & dw.week_start.isin(TWELVE_WEEKS)].copy()
twelve["driver"] = twelve.driver_id.map(TWELVE_IDS)
twelve["window"] = twelve.week_start.map(TWELVE_WEEKS)
twelve = twelve.sort_values(["driver", "week_start"]).reset_index(drop=True)
twelve = twelve[["driver", "driver_id", "zone_mode", "window", "week_start", "peak_online_hours",
                 "peak_offers", "peak_accepted", "peak_driver_cancels", "peak_trips",
                 "peak_hours_no_trip", "peak_bookings_rs", "topup_rs"]].rename(
    columns={"zone_mode": "zone"})
twelve.to_csv(DATA / f"{STEM}_twelve_rows_STUDENT.csv", index=False)
check("twelve rows written", len(twelve) == 12)


def three(sub):
    h, t, b, n = (int(sub.peak_online_hours.sum()), int(sub.peak_trips.sum()),
                  int(sub.peak_bookings_rs.sum()), len(sub))
    return dict(hours=h, trips=t, bookings=b, rows=n, per_hour=b / h, per_dw=b / n, per_trip=b / t)


tb, ta = three(twelve[twelve.window == "before"]), three(twelve[twelve.window == "after"])
check("twelve rows: 60 and 74 hours, 114 and 88 trips",
      (tb["hours"], ta["hours"], tb["trips"], ta["trips"]) == (60, 74, 114, 88))
check("twelve rows: Rs 18,810 and Rs 14,520", (tb["bookings"], ta["bookings"]) == (18810, 14520))
check("twelve rows: Rs 313.5 and Rs 196.2 per hour",
      (round(tb["per_hour"], 1), round(ta["per_hour"], 1)) == (313.5, 196.2))
check("twelve rows: Rs 3,135 and Rs 2,420 per driver-week",
      (tb["per_dw"], ta["per_dw"]) == (3135, 2420))
check("twelve rows: Rs 165 per trip on both sides", tb["per_trip"] == ta["per_trip"] == 165)
for col in ("peak_online_hours", "peak_trips", "peak_bookings_rs"):
    check(f"twelve rows: totals equal the sum of the printed rows ({col})",
          twelve.groupby("window")[col].sum().to_dict()
          == {"before": tb[{"peak_online_hours": "hours", "peak_trips": "trips",
                            "peak_bookings_rs": "bookings"}[col]],
              "after": ta[{"peak_online_hours": "hours", "peak_trips": "trips",
                           "peak_bookings_rs": "bookings"}[col]]})

tw_hour_pct = round((ta["per_hour"] / tb["per_hour"] - 1) * 100, 1)
tw_dw_pct = round((ta["per_dw"] / tb["per_dw"] - 1) * 100, 1)
add("twelve_hours_before", 60, "60", "sum of the six before rows", "half1 S11; notebook cell 4; sheet panel 2")
add("twelve_hours_after", 74, "74", "sum of the six after rows", "half1 S11; notebook cell 4; sheet panel 2")
add("twelve_trips_before", 114, "114", "sum of the six before rows", "half1 S11; sheet panel 2")
add("twelve_trips_after", 88, "88", "sum of the six after rows", "half1 S11; sheet panel 2")
add("twelve_bookings_before_rs", 18810, "Rs 18,810", "sum of peak_bookings_rs, six before rows",
    "half1 S11; notebook; sheet panel 2")
add("twelve_bookings_after_rs", 14520, "Rs 14,520", "sum of peak_bookings_rs, six after rows",
    "half1 S11; notebook; sheet panel 2")
add("twelve_driver_weeks", 6, "6", "rows in each window of the twelve", "half1 S11")
add("twelve_rs_per_hour_before", 313.5, "Rs 313.5", "18,810 / 60", "half1 S11, S12; notebook; sheet")
add("twelve_rs_per_hour_after", 196.2, "Rs 196.2", "14,520 / 74", "half1 S11, S12; notebook; sheet")
add("twelve_rs_per_driver_week_before", 3135, "Rs 3,135", "18,810 / 6", "half1 S11; notebook; sheet")
add("twelve_rs_per_driver_week_after", 2420, "Rs 2,420", "14,520 / 6", "half1 S11; notebook; sheet")
add("twelve_rs_per_trip", 165, "Rs 165", "18,810 / 114 and 14,520 / 88", "half1 S11; notebook; sheet")
add("twelve_rs_per_hour_change_pct", tw_hour_pct, "down 37 percent", "196.2 / 313.5 - 1",
    "half1 S11, S12; notebook; sheet")
add("twelve_rs_per_driver_week_change_pct", tw_dw_pct, "down 23 percent", "2,420 / 3,135 - 1",
    "half1 S11, S12; notebook; sheet")
check("twelve rows change: -37.4 and -22.8 percent", (tw_hour_pct, tw_dw_pct) == (-37.4, -22.8))

# ------------------------------------------------------------------ the full data, three reads (L2)
fb, fa = three(B), three(A)
hour_pct = round((fa["per_hour"] / fb["per_hour"] - 1) * 100, 1)
dw_pct = round((fa["per_dw"] / fb["per_dw"] - 1) * 100, 1)
book_pct = round((fa["bookings"] / fb["bookings"] - 1) * 100, 1)
rows_pct = round((fa["rows"] / fb["rows"] - 1) * 100, 1)
check("full data: Rs 313.5 to Rs 260.4 per hour",
      (round(fb["per_hour"], 1), round(fa["per_hour"], 1)) == (313.5, 260.4))
check("full data: Rs 5,816.5 to Rs 5,861.3 per active driver-week",
      (round(fb["per_dw"], 1), round(fa["per_dw"], 1)) == (5816.5, 5861.3))
check("full data: Rs 165 per trip on both sides", fb["per_trip"] == fa["per_trip"] == 165)
check("per hour fell 16.9 percent", hour_pct == -16.9)
check("bookings +3.0, active driver-weeks +2.2, so per driver-week +0.8 percent",
      (book_pct, rows_pct, dw_pct) == (3.0, 2.2, 0.8))
check("the hand count sits at least 0.05 from the full-data ratio after (196.2 against 260.4)",
      abs(ta["per_hour"] - fa["per_hour"]) >= 0.05)
add("full_rs_per_hour_change_pct", hour_pct, "down 17 percent", "260.4 / 313.5 - 1",
    "ticket; half1 S1, S14, S15; notebook cell 6; notes; sheet")
add("full_rs_per_driver_week_change_pct", dw_pct, "up 0.8 percent", "5,861.3 / 5,816.5 - 1",
    "half1 S1, S14, S16; notebook cells 6 to 8; notes; sheet; exercises")
add("full_bookings_change_pct", book_pct, "up 3.0 percent", "3,80,98,500 / 3,69,93,000 - 1",
    "half1 S16; notebook cell 8; notes")
add("full_driver_weeks_change_pct", rows_pct, "up 2.2 percent", "6,500 / 6,360 - 1",
    "half1 S16; notebook cell 8; notes")
add("rs_per_hour_per_ten", round(fa["per_hour"] / fb["per_hour"] * 10, 1), "about Rs 8.30 of every Rs 10",
    "260.4 / 313.5 x 10", "half2 transcript 1; extras transcript 1")
joiner_rows = int(A[A.driver_id.isin(drivers[drivers.joined_month == "2026-09"].driver_id)].shape[0])
check("the 140 joiners account for the 140 extra active driver-weeks",
      joiner_rows == M["driver_weeks_after"] - M["driver_weeks_before"] == 140)
add("joiner_driver_weeks_after", joiner_rows, "140 active driver-weeks",
    "rows of driver_weeks in the after window for drivers with joined_month 2026-09",
    "half1 S16; notebook cell 7; notes")
hpw_b, hpw_a = fb["hours"] / fb["rows"], fa["hours"] / fa["rows"]
add("hours_per_driver_week_before", round(hpw_b, 1), "18.6 hours", "1,18,000 / 6,360", "notebook depth line")
add("hours_per_driver_week_after", round(hpw_a, 1), "22.5 hours", "1,46,300 / 6,500", "notebook depth line")
check("second route: fare x trips per hour = rupees per hour, both windows",
      abs(165 * fb["trips"] / fb["hours"] - fb["per_hour"]) < 1e-9
      and abs(165 * fa["trips"] / fa["hours"] - fa["per_hour"]) < 1e-9)

# The 1,020 drivers outside Monday's idle tail: driver operations' "drivers will log off" is false
# for them, and this is the evidence line that says so.
after_rate = A.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
idle_ids = set(after_rate[after_rate.peak_trips / after_rate.peak_online_hours < 1.0].index)
check("Monday's idle tail recounts to 180 drivers", len(idle_ids) == M["idle_tail_drivers"])
joiners = set(drivers[drivers.joined_month == "2026-09"].driver_id)
check("none of the 140 joiners sits in the idle tail", len(idle_ids & joiners) == 0)
rest = dw[~dw.driver_id.isin(idle_ids)]
rb, ra = three(rest[rest.window == "before"]), three(rest[rest.window == "after"])
rest_topup = int(rest[rest.window == "after"].topup_rs.sum())
check("the rest were paid Monday's Rs 74.1 lakh of top-up", rest_topup == M["topup_high_acceptance_rs"])
add("rest_drivers", rest.driver_id.nunique(), "1,020 drivers", "1,200 less the 180 in the idle tail",
    "half1 S20, S21; role cards; notes")
add("rest_hours_before", rb["hours"], "98,000 hours", "peak hours, drivers outside the idle tail, before", "role cards")
add("rest_hours_after", ra["hours"], "1,04,300 hours", "the same, after", "role cards")
add("rest_trips_before", rb["trips"], "1,86,200 trips", "peak trips, drivers outside the idle tail, before", "role cards")
add("rest_trips_after", ra["trips"], "1,97,460 trips", "the same, after", "role cards")
add("rest_tph_before", round(rb["trips"] / rb["hours"], 2), "1.90", "1,86,200 / 98,000",
    "half1 S20, S21; role cards; notes; exercises")
add("rest_tph_after", round(ra["trips"] / ra["hours"], 2), "1.89", "1,97,460 / 1,04,300",
    "half1 S20, S21; role cards; notes; exercises")
add("rest_trips_change_pct", round((ra["trips"] / rb["trips"] - 1) * 100, 1), "up 6 percent",
    "1,97,460 / 1,86,200 - 1", "role cards; notes")
add("idle_tail_joiners", 0, "none of the 140", "joiners among the 180 idle-tail drivers",
    "half1 S20; role cards; exercises")

# ------------------------------------------------------------------ the twelve weeks (makeover)
weekly = dw.groupby("week_start").agg(
    peak_online_hours=("peak_online_hours", "sum"), peak_trips=("peak_trips", "sum"),
    peak_bookings_rs=("peak_bookings_rs", "sum"), active_driver_weeks=("driver_id", "count"),
).reset_index()
weekly = weekly.merge(zw.groupby("week_start").peak_requests.sum().rename("rider_requests"),
                      on="week_start")
weekly["window"] = weekly.week_start.map(
    lambda s: "before" if dt.date.fromisoformat(s) < LAUNCH else "after")
weekly["rs_per_hour"] = (weekly.peak_bookings_rs / weekly.peak_online_hours).round(2)
weekly["rs_per_driver_week"] = (weekly.peak_bookings_rs / weekly.active_driver_weeks).round(2)
weekly["rs_per_trip"] = (weekly.peak_bookings_rs / weekly.peak_trips).round(2)
weekly = weekly[["week_start", "window", "peak_online_hours", "peak_trips", "peak_bookings_rs",
                 "active_driver_weeks", "rider_requests", "rs_per_hour", "rs_per_driver_week",
                 "rs_per_trip"]]
weekly.to_csv(DATA / f"{STEM}_twelve_weeks_STUDENT.csv", index=False)
check("twelve weeks written", len(weekly) == 12)
check("weekly hours sum to the window totals", weekly.groupby("window").peak_online_hours.sum().to_dict()
      == {"before": M["hours_before"], "after": M["hours_after"]})
check("no two weeks carry the same hours (the series moves)", weekly.peak_online_hours.nunique() == 12)
check("every after week sits below every before week in rupees per hour (a step at the launch)",
      weekly[weekly.window == "after"].rs_per_hour.max() < weekly[weekly.window == "before"].rs_per_hour.min())
for _, r in weekly.iterrows():
    facts["weekly_series"].append({k: (float(v) if isinstance(v, float) else
                                       (int(v) if not isinstance(v, str) else v))
                                   for k, v in r.items()})
wk_after = weekly[weekly.window == "after"]
add("weekly_rs_per_hour_after_max", float(wk_after.rs_per_hour.max()), "Rs 271",
    "the highest after week, the launch week", "half1 S17; notebook cell 10")
add("weekly_rs_per_hour_before_min", float(weekly[weekly.window == "before"].rs_per_hour.min()), "Rs 310",
    "the lowest before week", "half1 S17; notebook cell 10")
add("weekly_rs_per_dw_after_first", float(wk_after.rs_per_driver_week.iloc[0]), "Rs 6,033",
    "the first after week, per active driver-week", "notes (the window total hides a slide)")
add("weekly_rs_per_dw_after_last", float(wk_after.rs_per_driver_week.iloc[-1]), "Rs 5,587",
    "the last after week, per active driver-week", "notes (the window total hides a slide)")

# ------------------------------------------------------------------ the validate step (L5)
peak_hours_window = M["max_peak_hours_per_week"] * 6
dh_req_b = M["hours_before"] / M["requests_before"]
dh_req_a = M["hours_after"] / M["requests_after"]
add("peak_hours_in_window", peak_hours_window, "252 peak hours",
    "42 peak hours a week x 6 weeks, Monday's definition (two three-hour windows on all seven days)",
    "half2 S10; notebook cell 14; guesstimate note")
add("requests_per_peak_hour_after", round(M["requests_after"] / peak_hours_window),
    "about 1,018 an hour", "2,56,556 / 252", "half2 S10; notebook cell 14; guesstimate note")
add("drivers_online_per_peak_hour_after", round(M["hours_after"] / peak_hours_window),
    "about 581 drivers", "1,46,300 / 252", "guesstimate note")
add("driver_hours_per_request_before", round(dh_req_b, 2), "0.47", "1,18,000 / 2,51,910",
    "half2 S10; notebook cell 14; notes; exercises")
add("driver_hours_per_request_after", round(dh_req_a, 2), "0.57", "1,46,300 / 2,56,556",
    "half2 S10; notebook cell 14; notes")
check("driver-hours per request 0.47 before and 0.57 after",
      (round(dh_req_b, 2), round(dh_req_a, 2)) == (0.47, 0.57))

# ------------------------------------------------------------------ drivers at the evening peak
assume("hyd_people", 1e7, 9e6, 1.1e7, "about 1 crore people",
       "a round number for the Hyderabad metro area, said aloud and to be checked", "half2 S8; notebook; note")
assume("weekday_ride_share", 0.01, 0.005, 0.015, "1 percent",
       "share of people who take one Uber trip on a weekday", "half2 S8; notebook; note")
assume("evening_share", 0.25, 0.20, 0.30, "a quarter",
       "share of the day's trips that fall in the three evening peak hours", "half2 S8; notebook; note")
assume("trips_per_busy_hour", 2.4, 2.0, 3.0, "2.4 trips",
       "a peak trip takes about 25 minutes from accepting to dropping, so a busy driver fits 2.4 an hour",
       "half2 S8; notebook; note")
assume("idle_share", 0.30, 0.22, 0.38, "0.30",
       "share of online drivers with no rider at a given moment; the range is the case's own share of "
       "online hours with no completed trip, 0.22 before and 0.38 after", "half2 S8; notebook; note")
assume("buffer", 1.15, 1.10, 1.25, "1.15",
       "the busiest half hour carries more than the window's average hour", "half2 S8; notebook; note")
AS = {a["id"]: a for a in facts["assumptions"]}


def drivers_needed(people, share, evening, busy, idle, buffer):
    per_hour = people * share * evening / M["peak_window_hours"]
    return per_hour / (busy * (1 - idle)) * buffer


base = {k: AS[k]["value"] for k in ("hyd_people", "weekday_ride_share", "evening_share",
                                    "trips_per_busy_hour", "idle_share", "buffer")}
order = ["hyd_people", "weekday_ride_share", "evening_share", "trips_per_busy_hour", "idle_share", "buffer"]
central = drivers_needed(*[base[k] for k in order])
req_hour = base["hyd_people"] * base["weekday_ride_share"] * base["evening_share"] / M["peak_window_hours"]
swing = {}
for k in order:
    lo = drivers_needed(*[AS[k]["low"] if j == k else base[j] for j in order])
    hi = drivers_needed(*[AS[k]["high"] if j == k else base[j] for j in order])
    swing[k] = (round(min(lo, hi)), round(max(lo, hi)))
biggest = max(swing, key=lambda k: swing[k][1] - swing[k][0])
check("drivers at peak: about 5,700 at the central values", round(central, -2) == 5700)
check("the share of people who ride moves the answer most", biggest == "weekday_ride_share")
check("the idle share moves it less than the ride share, more than the buffer",
      (swing["weekday_ride_share"][1] - swing["weekday_ride_share"][0])
      > (swing["idle_share"][1] - swing["idle_share"][0])
      > (swing["buffer"][1] - swing["buffer"][0]))
add("requests_per_evening_hour", round(req_hour), "about 8,300 an hour",
    "1 crore x 1 percent x a quarter / 3 hours", "half2 S8, S9; notebook cell 12; note; exercises")
add("trips_per_online_hour_chain", round(base["trips_per_busy_hour"] * (1 - base["idle_share"]), 2),
    "1.68", "2.4 x (1 - 0.30)", "half2 S9, S10; notebook cell 12; note")
add("drivers_at_peak_central", round(central), "about 5,700 drivers",
    "8,333 / 1.68 x 1.15", "half2 S9; notebook cell 12; notes; sheet; exercises")
for k in order:
    add(f"swing_{k}_low", swing[k][0], f"{round(swing[k][0], -2):,.0f}", f"{k} at its low or high end",
        "notebook cell 12 (the swing chart)")
    add(f"swing_{k}_high", swing[k][1], f"{round(swing[k][1], -2):,.0f}", f"{k} at its other end",
        "notebook cell 12 (the swing chart)")
add("drivers_at_peak_range_low", round(swing["weekday_ride_share"][0], -2), "about 2,900",
    "the ride share at 0.5 percent, every other factor central", "half2 S9; notes; sheet")
add("drivers_at_peak_range_high", round(swing["weekday_ride_share"][1], -2), "about 8,600",
    "the ride share at 1.5 percent, every other factor central", "half2 S9; notes; sheet")
chain_dh = 1 / (base["trips_per_busy_hour"] * (1 - base["idle_share"]))
add("driver_hours_per_request_chain", round(chain_dh, 2), "0.60",
    "1 / 1.68, before the buffer", "half2 S10; notebook cell 14; notes")
add("chain_over_case_before", round(chain_dh / dh_req_b, 2), "about a quarter more",
    "0.595 / 0.468", "half2 S10; notebook cell 14")
day_trips = base["hyd_people"] * base["weekday_ride_share"]
wrong = day_trips / base["trips_per_busy_hour"]
add("weekday_trips_city", round(day_trips), "1 lakh trips a day", "1 crore x 1 percent",
    "half2 S11 (the trap)")
add("wrong_unit_drivers", round(wrong, -2), "about 41,700 drivers",
    "a day's 1 lakh trips divided by an hour's 2.4 trips per driver: a day treated as an hour",
    "half2 S11; exercises; Kahoot")
check("the wrong-unit answer is about seven times the honest one", 7 <= wrong / central < 7.5)
add("wrong_unit_ratio", round(wrong / central, 1), "about seven times", "41,667 / 5,704", "half2 S11")
add("hyd_published_drivers_online_peak", None, "to be found",
    "R2 holds no figure; a search on 12 October 2026 found only undated or decade-old counts of "
    "drivers signed up, which is a different unit, so the slot stays to be found",
    "half2 S10; notes; guesstimate note")

# ------------------------------------------------------------------ UPI, in pairs
assume("india_people", 1.4e9, 1.4e9, 1.45e9, "about 140 crore people",
       "a round number said aloud", "half2 S12; notebook cell 14; note")
assume("upi_active_users", 3.5e8, 2.5e8, 4.5e8, "about 35 crore",
       "about one in four of India's people pays by UPI in a month", "half2 S12; notebook; note")
assume("upi_payments_per_day", 2, 1, 3, "about 2",
       "a tea, a recharge or a transfer on an ordinary day", "half2 S12; notebook; note")
upi = AS_u = {a["id"]: a for a in facts["assumptions"]}
upi_est = upi["upi_active_users"]["value"] * upi["upi_payments_per_day"]["value"]
public("upi_per_day", 802_000_000, "802 million a day", "T3",
       "Outlook Money, 2 October 2026, citing NPCI's data on X: an average of 802 million UPI "
       "transactions a day in September 2026; https://www.outlookmoney.com/banking/"
       "upi-processes-2407-billion-transactions-worth-rs-2937-lakh-crore-in-september",
       "half2 S12, S13; notebook cell 14; notes; Kahoot; exercises")
public("upi_month_total", 24_070_000_000, "24.07 billion in the month", "T3",
       "the same report: 24.07 billion transactions worth Rs 29.37 lakh crore in September 2026",
       "half2 S13; Kahoot; exercises")
add("upi_estimate_per_day", int(upi_est), "70 crore a day (700 million)", "35 crore x 2",
    "half2 S12, S13; notebook cell 14; notes")
add("upi_estimate_gap_pct", round((upi_est / 802_000_000 - 1) * 100, 1), "about 13 percent below",
    "700 million / 802 million - 1", "half2 S13; notebook cell 14; notes")
add("upi_month_over_30", round(24_070_000_000 / 30 / 1e6), "802 million", "24.07 billion / 30 days",
    "half2 S13; Kahoot; exercises")
add("upi_month_over_31", round(24_070_000_000 / 31 / 1e6), "776 million", "24.07 billion / 31 days",
    "half2 S13; Kahoot; exercises")
add("upi_31_day_gap_pct", round((24_070_000_000 / 31) / (24_070_000_000 / 30) * 100 - 100, 1),
    "about 3 percent low", "30 / 31 - 1", "half2 S13; Kahoot")
add("upi_users_swing_low", int(2.5e8 * 2), "50 crore", "25 crore x 2", "notebook cell 14")
add("upi_users_swing_high", int(4.5e8 * 2), "90 crore", "45 crore x 2", "notebook cell 14")
add("upi_payments_swing_low", int(3.5e8 * 1), "35 crore", "35 crore x 1", "notebook cell 14")
add("upi_payments_swing_high", int(3.5e8 * 3), "105 crore", "35 crore x 3", "notebook cell 14")
check("UPI: 70 crore a day, 13 percent below 802 million",
      upi_est == 7e8 and round((upi_est / 802e6 - 1) * 100) == -13)

# ------------------------------------------------------------------ other public facts used
public("flipkart_concurrent_users", 6_300_000, "6.3 million concurrent users in a minute", "T3",
       "Flipkart Stories, 9 October 2026: 'Flipkart recorded 6.3 million concurrent users in a "
       "minute' in the opening hour of The Big Billion Days; the URL slug reads 63 million; "
       "https://stories.flipkart.com/announcement/india-logs-on-for-the-big-billion-days-flipkart-"
       "records-63-million-concurrent-users-as-the-festive-season-opens",
       "half2 S14; Kahoot; notes; exercises")
public("flipkart_url_reading", 63_000_000, "63 million (the URL slug)", "T3", "the same page's URL",
       "half2 S14; Kahoot; notes")
public("dmrc_journeys_2026", 6_406_000, "64.06 lakh journeys a day", "M6",
       "The Tribune, updated 9 August 2026, citing DMRC: average daily ridership of 64.06 lakh "
       "journeys; https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-"
       "punctuality-in-2026-dmrc/", "half2 S14; exercises; notes")
public("dmrc_boardings_record", 8_244_903, "82,44,903 boardings", "M6",
       "Republic World, 18 September 2026, quoting DMRC: highest-ever passenger boardings of "
       "82,44,903 on 17 September 2026; https://www.republicworld.com/india/delhi-metro-breaks-"
       "all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241",
       "half2 S14; exercises; notes")
public("dmrc_line_utilisation_2018", 4_535_932, "45,35,932 line uses", "M6",
       "PTI via LatestLY, 30 May 2018: line utilisation on 29 May 2018 was 45,35,932, against gate "
       "ridership near 27 lakh a day in February 2018; https://www.latestly.com/agency-news/dmrc-"
       "uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp",
       "notes (the unit trap)")
public("dmrc_ridership_2018", 2_700_000, "27 lakh a day", "M6", "the same report", "notes (the unit trap)")
public("amazon_memo_pages", 6, "six-page memo", "T1",
       "Amazon's 2017 letter to shareholders, filed 18 April 2018: 'We don't do PowerPoint (or any "
       "other slide-oriented) presentations'; memos are read silently at the start of each meeting; "
       "'a great memo probably should take a week or more'; https://www.sec.gov/Archives/edgar/data/"
       "1018724/000119312518121161/d456916dex991.htm", "half1 S27; notes; Kahoot; exercises")
public("dmart_revenue_fy26_crore", 66968, "Rs 66,968 crore", "T3",
       "Avenue Supermarts press release, 2 May 2026: standalone total revenue for FY26 Rs 66,968 "
       "crore; 85 stores added in FY26; 500 stores at 31 March 2026; two-year-old stores grew 10.8 "
       "percent in Q4 FY26; https://nsearchives.nseindia.com/corporate/DMART_02052026173007_"
       "ASLPressRelease02052026.pdf", "lab; Kalpa exercise; lab set; guesstimate note")
public("dmart_stores_fy26_end", 500, "500 stores", "T3", "the same release", "lab; Kalpa exercise")
public("dmart_stores_added_fy26", 85, "85 stores added", "T3", "the same release", "lab; Kalpa exercise")
public("dmart_two_year_store_growth_pct", 10.8, "10.8 percent", "T3",
       "the same release: two years and older DMart stores grew 10.8 percent in Q4 FY26",
       "lab note; Kalpa exercise solution")
per_store_end = round(66968 / 500, 1)
per_store_avg = round(66968 / ((500 + 415) / 2), 1)
add("dmart_stores_fy25_end", 415, "415 stores", "500 less the 85 added in FY26", "lab; Kalpa exercise")
add("dmart_revenue_per_store_year_end", per_store_end, "about Rs 134 crore", "66,968 / 500 (our arithmetic)",
    "lab; Kalpa exercise; lab set; sheet")
add("dmart_revenue_per_store_average", per_store_avg, "about Rs 146 crore",
    "66,968 / ((500 + 415) / 2) (our arithmetic)", "lab; Kalpa exercise; lab set")
add("dmart_denominator_gap_pct", round((per_store_avg / per_store_end - 1) * 100), "about 9 percent",
    "146.4 / 133.9 - 1", "lab; Kalpa exercise")
add("dmart_revenue_over_fy25_end", round(66968 / 415, 1), "about Rs 161 crore",
    "66,968 / 415, the wrong denominator a hurried analyst uses", "Kalpa exercise (distractor)")
check("DMart per store: 133.9 and 146.4", (per_store_end, per_store_avg) == (133.9, 146.4))
public("swiggy_instamart_ctr_before", 0.061, "6.1 percent", "case file, Wednesday ticket",
       "Wednesday's target, asserted by Wednesday's generator: strip click-through in the three "
       "weeks before 7 September 2026", "preread")
public("swiggy_instamart_ctr_after", 0.038, "3.8 percent", "case file, Wednesday ticket",
       "Wednesday's target: strip click-through in the three weeks after", "preread")

# ------------------------------------------------------------------ toys, labelled invented
facts["toys"] += [
    {"id": "toy_notice_board", "label": "invented",
     "values": {"topic_title": "Breakfast survey results",
                "claim_title": "Rotis replace rice at Monday breakfast, so the kitchen moves two "
                               "staff from the rice counter to the roti line", "staff_moved": 2},
     "used_by": "half1 S6; notes; sheet"},
    {"id": "toy_canteen_tea", "label": "invented",
     "values": {"students": 2000, "share_who_buy_tea": 0.6, "cups_each": 2, "cups_a_day": 2400},
     "used_by": "half2 S6; guided exercise; notes"},
    {"id": "toy_two_million_city", "label": "invented",
     "values": {"people": 2_000_000, "wrong_households": 9_000_000, "people_per_household": 4,
                "right_households": 500_000},
     "used_by": "half2 S14; Kahoot"},
    {"id": "toy_ai_acceptance_rate", "label": "invented",
     "values": {"acceptance_rate_pct": 32},
     "used_by": "half2 S21; extras AI variant; notes"},
]

# ------------------------------------------------------------------ twelve rows into the facts
for _, r in twelve.iterrows():
    facts["twelve_rows"].append({k: (int(v) if isinstance(v, (int,)) or str(v).isdigit() else v)
                                 for k, v in r.items()})

# ------------------------------------------------------------------ the three cluttered slides
def ids(*pairs):
    return [{"label": a, "shows": b, "facts_ids": c} for a, b, c in pairs]


facts["cluttered_slides"] = {
    "A_dashboard": ids(
        ("Peak online hours", "+24 percent", "hours_change_pct"),
        ("Completed peak trips", "+3 percent", "trips_change_pct"),
        ("Trips per peak online hour", "1.90 to 1.58", "tph_before, tph_after"),
        ("Acceptance share", "0.86 to 0.73", "acceptance_before, acceptance_after"),
        ("Online hours with no trip", "0.22 to 0.38", "no_trip_share_before, no_trip_share_after"),
        ("Median rider wait", "4.8 to 4.6 min", "median_wait_before, median_wait_after"),
        ("Top-up paid", "Rs 1.9 crore", "topup_after_rs"),
        ("New drivers since launch", "140", "drivers_new"),
        ("Top-up to low acceptance", "61 percent", "topup_low_acceptance_share")),
    "B_finance": ids(
        ("Gross peak bookings", "Rs 3.70 cr to Rs 3.81 cr", "bookings_before_rs, bookings_after_rs"),
        ("Bookings per online hour", "Rs 314 to Rs 260", "rs_per_hour_before, rs_per_hour_after"),
        ("Bookings per active driver-week", "Rs 5,817 to Rs 5,861",
         "rs_per_driver_week_before, rs_per_driver_week_after"),
        ("Bookings per trip", "Rs 165 to Rs 165", "fare_avg_rs"),
        ("Top-up paid", "Rs 1.9 crore", "topup_after_rs"),
        ("Top-up per completed trip", "Rs 82.3", "topup_per_trip_after_rs"),
        ("Top-up, under-half acceptance", "Rs 1.16 crore", "topup_low_acceptance_rs"),
        ("Top-up, everyone else", "Rs 74 lakh", "topup_high_acceptance_rs"),
        ("Rider requests", "2,51,910 to 2,56,556", "requests_before, requests_after")),
    "C_driver_ops": ids(
        ("Drivers", "1,200 (140 new)", "drivers_total, drivers_new"),
        ("Active driver-weeks", "6,360 to 6,500", "driver_weeks_before, driver_weeks_after"),
        ("Offers shown to drivers", "2,69,773 to 3,47,583", "offers_before, offers_after"),
        ("Acceptance share", "0.86 to 0.73", "acceptance_before, acceptance_after"),
        ("Driver cancels after accepting", "0.04 to 0.09",
         "driver_cancel_share_before, driver_cancel_share_after"),
        ("Drivers in the idle tail", "180", "idle_tail_drivers"),
        ("Idle-tail online hours", "20,000 to 42,000", "idle_hours_before, idle_hours_after"),
        ("Idle-tail trips", "38,000 to 33,440", "idle_trips_before, idle_trips_after"),
        ("Unfulfilled requests", "0.11 to 0.10", "unfulfilled_share_before, unfulfilled_share_after")),
}
known = {n["id"] for n in facts["monday_ids_reused"]}
for name, rows in facts["cluttered_slides"].items():
    check(f"cluttered slide {name} carries nine numbers, every one a Monday id",
          len(rows) == 9 and all(i.strip() in known for r in rows for i in r["facts_ids"].split(",")))

# ------------------------------------------------------------------ Kalpa, for the lab
dm = pd.DataFrame([
    {"item": "FY26 standalone total revenue, Rs crore", "value": 66968,
     "note": "Avenue Supermarts press release, 2 May 2026 (checked 12 October 2026)"},
    {"item": "Stores at 31 March 2026", "value": 500, "note": "the same release"},
    {"item": "Stores added in FY26", "value": 85, "note": "the same release"},
    {"item": "Stores at 31 March 2025", "value": 415, "note": "500 less the 85 added"},
    {"item": "Revenue per store, Rs crore, year-end count", "value": per_store_end,
     "note": "66,968 / 500, our arithmetic"},
    {"item": "Revenue per store, Rs crore, average count", "value": per_store_avg,
     "note": "66,968 / 457.5, our arithmetic"},
])
dm.to_csv(DATA / f"{STEM}_kalpa_dmart_anchor_STUDENT.csv", index=False)
check("DMart anchor written", len(dm) == 6)

facts["kalpa"] = {
    "no_plant_today": True,
    "status": "the three Kalpa role cards and Anand's store question are proposed for client zero "
              "v2.3 (the row's client-zero column, 21 September 2026, not yet locked)",
    "v4": {"orders": 1000, "customers": 340, "q1_rs": 100_000_000, "q2_rs": 98_400_000,
           "shown": "1,000 orders from 340 customers; Rs 10.00 crore in April to June and "
                    "Rs 9.84 crore in July to September 2026",
           "source": "data/generate_client_zero.py (V4_Q1_TOTAL, V4_Q2_TOTAL, V4_CUSTOMERS) and "
                     "the spine's section 14"},
    "north_star": "delivered orders per active customer per month",
    "guardrails": ["revenue per active customer", "discount share of booked revenue", "the return rate"],
    "leading_inputs": ["add-to-cart events per active app member", "new Retail-Plus sign-ups"],
    "heads": ["the marketing lead", "Operations", "the head of Retail-Plus"],
    "store_worked_example": {
        "label": "the TA's worked answer; every value an assumption with its range",
        "catchment_households": {"value": 50000, "low": 30000, "high": 80000},
        "share_who_shop_year_one": {"value": 0.4, "low": 0.25, "high": 0.5},
        "shoppers_year_one": 20000,
        "sign_up_share": {"value": 0.05, "low": 0.02, "high": 0.08},
        "sign_ups_year_one": 1000,
        "visits_per_month": {"value": 2, "low": 1, "high": 4},
        "spend_per_visit_rs": {"value": 1500, "low": 1000, "high": 2000},
        "first_year_sales_rs": 20000 * 2 * 12 * 1500,
        "share_of_dmart_store": round(20000 * 2 * 12 * 1500 / (per_store_end * 1e7), 2),
    },
}
ex = facts["kalpa"]["store_worked_example"]
check("Kalpa worked store: 1,000 sign-ups, Rs 72 crore, about half a mature DMart store",
      ex["sign_ups_year_one"] == 50000 * 0.4 * 0.05 and ex["first_year_sales_rs"] == 720_000_000
      and ex["share_of_dmart_store"] == 0.54)
check("Kalpa v4 totals match the client-zero generator's constants",
      facts["kalpa"]["v4"]["q1_rs"] == 100_000_000 and facts["kalpa"]["v4"]["customers"] == 340)

# ------------------------------------------------------------------ write and re-read
out = HERE / f"{STEM}_facts_INTERNAL.yaml"
out.write_text(yaml.safe_dump(facts, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")
back = yaml.safe_load(out.read_text(encoding="utf-8"))
check("facts file re-reads with every block", all(k in back for k in (
    "numbers", "monday_ids_reused", "public_facts", "assumptions", "toys", "twelve_rows",
    "weekly_series", "cluttered_slides", "kalpa")))
check("every Tuesday id is unique", len({n["id"] for n in back["numbers"]}) == len(back["numbers"]))
print(f"\nwrote {out.relative_to(DAY.parent.parent.parent)}: {len(back['numbers'])} numbers, "
      f"{len(back['monday_ids_reused'])} Monday ids, {len(back['public_facts'])} public facts, "
      f"{len(back['assumptions'])} assumptions")

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

Writes Tuesday's case tables, which match the merged pack's byte for byte (asserted against
origin/main), the concept chapters' invented examples and the facts file:
    content/W04/D2/data/C2_W04_D02_twelve_rows_STUDENT.csv
    content/W04/D2/data/C2_W04_D02_twelve_weeks_STUDENT.csv
    content/W04/D2/data/C2_W04_D02_kalpa_dmart_anchor_STUDENT.csv
    content/W04/D2/data/C2_W04_D02_driver_groups_STUDENT.csv
    content/W04/D2/data/C2_W04_D02_driver_segments_STUDENT.csv       (case, for notebook 05)
    content/W04/D2/data/C2_W04_D02_kirana_days_STUDENT.csv           (invented, chapters 1 and 2)
    content/W04/D2/data/C2_W04_D02_kirana_slide_elements_STUDENT.csv (invented, chapter 2)
    content/W04/D2/data/C2_W04_D02_school_attendance_STUDENT.csv     (invented, chapter 3)
    content/W04/D2/data/C2_W04_D02_canteen_ledger_STUDENT.csv        (invented, chapter 6)
    content/W04/D2/data/C2_W04_D02_canteen_till_STUDENT.csv          (invented, chapter 6)
    content/W04/D2/data/C2_W04_D02_sanity_tests_STUDENT.csv          (invented, chapter 6)
    content/W04/D2/data/C2_W04_D02_kirana_page_STUDENT.txt           (invented, chapter 7)
    content/W04/D2/internal/C2_W04_D02_facts_INTERNAL.yaml

No randomness is used, so two runs write byte-identical files. pandas and PyYAML only.

Run from the repository root:
    python3 content/W04/D2/internal/C2_W04_D02_make_data_INTERNAL.py
"""
import datetime as dt
import pathlib
import re
import subprocess
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
        "driver_groups": f"data/{STEM}_driver_groups_STUDENT.csv",
    },
    "corrections": [
        "The per-driver-week read is per active driver-week, one driver with a row in driver_weeks "
        "that week (6,360 before, 6,500 after), never per enrolled driver-week. It rose 0.8 percent: "
        "bookings rose 3.0 percent while active driver-weeks rose 2.2 percent. The ratio's formula has "
        "no hours in it, yet it splits into rupees per hour times hours per driver-week (Rs 313.5 x "
        "18.55 before, Rs 260.4 x 22.51 after), so it rose because each driver-week carried about four "
        "more online hours while each hour brought in 17 percent less. The 140 joiners pulled it down "
        "(Rs 4,314 a driver-week); the drivers there before the launch rose 1.4 percent.",
        "The validate step compares like with like: driver-hours per completed trip, 0.53 before the "
        "launch, against the chain's 0.60, so the chain runs about an eighth high and the checked "
        "answer is about 5,000 to 5,700. The draft compared per request with per trip.",
        "A four-hour window does not shrink the busiest moment: the buffer rises to about 1.53 and the "
        "answer stays about 5,700. The draft's 4,300 is now the weak answer in the scorecard.",
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


def plain(v):
    """A numpy number as the Python number YAML can write."""
    return v.item() if hasattr(v, "item") else v


def add(nid, value, shown, how, used_by, unit=""):
    value = plain(value)
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
    ("hours_before", "118,000 hours"), ("hours_after", "146,300 hours"),
    ("trips_before", "224,200 trips"), ("trips_after", "230,900 trips"),
    ("tph_before", "1.90"), ("tph_after", "1.58"),
    ("acceptance_before", "0.86"), ("acceptance_after", "0.73"),
    ("driver_cancel_share_before", "0.04"), ("driver_cancel_share_after", "0.09"),
    ("no_trip_share_before", "0.22"), ("no_trip_share_after", "0.38"),
    ("offers_before", "269,773"), ("offers_after", "347,583"),
    ("bookings_before_rs", "Rs 3.70 crore"), ("bookings_after_rs", "Rs 3.81 crore"),
    ("rs_per_hour_before", "Rs 314 (Rs 313.5)"), ("rs_per_hour_after", "Rs 260 (Rs 260.4)"),
    ("driver_weeks_before", "6,360 active driver-weeks"),
    ("driver_weeks_after", "6,500 active driver-weeks"),
    ("rs_per_driver_week_before", "Rs 5,817"), ("rs_per_driver_week_after", "Rs 5,861"),
    ("hours_change_pct", "up 24 percent"), ("trips_change_pct", "up 3 percent"),
    ("requests_before", "251,910 rider requests"), ("requests_after", "256,556 rider requests"),
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
    ("saving_low_rs", "Rs 58 lakh"), ("saving_high_rs", "Rs 92.7 lakh"),
    ("idle_tail_drivers", "180 drivers"),
    ("idle_hours_before", "20,000 hours"), ("idle_hours_after", "42,000 hours"),
    ("idle_trips_before", "38,000 trips"), ("idle_trips_after", "33,440 trips"),
    ("idle_hours_ratio", "2.1 times"), ("idle_trips_ratio", "down 12 percent"),
    ("tph_pre_launch_after", "1.58"),
    ("tph_core_zones_before", "1.90"), ("tph_core_zones_after", "1.79"),
    ("tph_crest_weeks_after", "1.60"),
    ("twelve_hours_change_pct", "up 23 percent"),
    ("drivers_pre_launch", "1,060 drivers before the launch"),
    ("acceptance_max_idle_week_after", "at most 46 percent"),
    ("acceptance_min_other_week_after", "at least 78 percent"),
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

check("the 1,060 drivers before the launch and the 140 joiners make Monday's 1,200",
      M["drivers_pre_launch"] + M["drivers_new"] == M["drivers_total"] == 1200)
check("Monday's low-acceptance weeks are the idle tail's weeks: every idle week after accepted at most "
      "0.46, every other week at least 0.78", M["acceptance_max_idle_week_after"] < 0.5
      <= M["acceptance_min_other_week_after"])
add("tph_after_exact", round(M["trips_after"] / M["hours_after"], 3), "1.578",
    "230,900 / 146,300, the 1.58 before rounding", "half1 S17; notebook cells 7 and 8; notes")
check("Rs 165 x 1.578 = Rs 260.4, so the second route lands on the first",
      round(165 * round(M["trips_after"] / M["hours_after"], 3), 1) == 260.4)
add("saving_low_lakh", round(M["topup_low_acceptance_rs"] / 2 / 1e5, 1), "Rs 58 lakh (57.95)",
    "1.159 crore x 1/2 in lakh: 115.9 / 2", "half1 S4; written case brief")
add("saving_high_lakh", round(M["topup_low_acceptance_rs"] * 0.8 / 1e5, 1), "Rs 92.7 lakh",
    "1.159 crore x 4/5 in lakh: 115.9 x 0.8", "half1 S4; written case brief")
add("topup_low_acceptance_lakh", round(M["topup_low_acceptance_rs"] / 1e5, 1), "115.9 lakh",
    "Rs 1.159 crore in lakh (1 crore = 100 lakh)", "half1 S4; written case brief")

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
add("full_bookings_change_pct", book_pct, "up 3.0 percent", "38,098,500 / 36,993,000 - 1",
    "half1 S16; notebook cell 8; notes")
add("full_driver_weeks_change_pct", rows_pct, "up 2.2 percent", "6,500 / 6,360 - 1",
    "half1 S16; notebook cell 8; notes")
add("bookings_ratio", round(fa["bookings"] / fb["bookings"], 3), "1.030", "38,098,500 / 36,993,000",
    "half1 S16")
add("driver_weeks_ratio", round(fa["rows"] / fb["rows"], 3), "1.022", "6,500 / 6,360", "half1 S16")
add("rs_per_dw_ratio", round(fa["per_dw"] / fb["per_dw"], 3), "1.008", "1.030 / 1.022", "half1 S16")
add("rs_per_hour_per_ten", round(fa["per_hour"] / fb["per_hour"] * 10, 1), "about Rs 8.30 of every Rs 10",
    "260.4 / 313.5 x 10", "half2 transcript 1; extras transcript 1")
joiner_rows = int(A[A.driver_id.isin(drivers[drivers.joined_month == "2026-09"].driver_id)].shape[0])
check("the 140 joiners account for the 140 extra active driver-weeks",
      joiner_rows == M["driver_weeks_after"] - M["driver_weeks_before"] == 140)
add("joiner_driver_weeks_after", joiner_rows, "140 active driver-weeks",
    "rows of driver_weeks in the after window for drivers with joined_month 2026-09",
    "half1 S16; notebook cell 7; notes")
hpw_b, hpw_a = fb["hours"] / fb["rows"], fa["hours"] / fa["rows"]
add("hours_per_driver_week_before", round(hpw_b, 1), "18.6 hours", "118,000 / 6,360", "notebook depth line")
add("hours_per_driver_week_after", round(hpw_a, 1), "22.5 hours", "146,300 / 6,500", "notebook depth line")
check("rupees per driver-week = rupees per hour x hours per driver-week, both windows",
      abs(fb["per_hour"] * hpw_b - fb["per_dw"]) < 1e-6 and abs(fa["per_hour"] * hpw_a - fa["per_dw"]) < 1e-6)
add("hours_per_driver_week_change_pct", round((hpw_a / hpw_b - 1) * 100, 1), "up 21 percent",
    "22.51 / 18.55 - 1", "half1 S16; notebook cell 8; notes; extras transcript 1")
add("hours_per_driver_week_extra", round(hpw_a - hpw_b), "about four more hours",
    "22.51 - 18.55", "half1 S16; notes; extras transcript 1")
joiner_ids = set(drivers[drivers.joined_month == "2026-09"].driver_id)
pre_a, join_a = three(A[~A.driver_id.isin(joiner_ids)]), three(A[A.driver_id.isin(joiner_ids)])
check("the drivers who were there before the launch kept their 6,360 driver-weeks",
      pre_a["rows"] == fb["rows"] == 6360)
add("pre_launch_rs_per_dw_after", round(pre_a["per_dw"], 1), "Rs 5,895 (5,895.4)",
    "the 1,060 pre-launch drivers' bookings after / their 6,360 driver-weeks", "half1 S16; notes; extras")
add("pre_launch_rs_per_dw_change_pct", round((pre_a["per_dw"] / fb["per_dw"] - 1) * 100, 1), "up 1.4 percent",
    "5,895.4 / 5,816.5 - 1", "half1 S16; notebook cell 8; notes; extras transcript 1")
add("pre_launch_hours_per_dw_after", round(pre_a["hours"] / pre_a["rows"], 1), "22.6 hours",
    "144,000 / 6,360", "notes; extras transcript 1")
add("joiner_rs_per_dw", round(join_a["per_dw"]), "Rs 4,314",
    "the 140 joiners' bookings after / their 140 driver-weeks", "half1 S16; notebook cell 8; notes; extras")
add("joiner_hours_per_dw", round(join_a["hours"] / join_a["rows"], 1), "16.4 hours",
    "2,300 / 140", "notes")
check("the joiners pulled the read down: below the average, and the pre-launch drivers rose more",
      join_a["per_dw"] < fa["per_dw"] < pre_a["per_dw"])
groups = pd.DataFrame([
    {"window": "before", "group": "drivers there before the launch", "driver_weeks": fb["rows"],
     "peak_online_hours": fb["hours"], "peak_trips": fb["trips"], "peak_bookings_rs": fb["bookings"]},
    {"window": "after", "group": "drivers there before the launch", "driver_weeks": pre_a["rows"],
     "peak_online_hours": pre_a["hours"], "peak_trips": pre_a["trips"], "peak_bookings_rs": pre_a["bookings"]},
    {"window": "after", "group": "the 140 joiners", "driver_weeks": join_a["rows"],
     "peak_online_hours": join_a["hours"], "peak_trips": join_a["trips"], "peak_bookings_rs": join_a["bookings"]},
])
groups.to_csv(DATA / f"{STEM}_driver_groups_STUDENT.csv", index=False)
check("the driver groups add up to the city's after window",
      groups[groups.window == "after"][["driver_weeks", "peak_online_hours", "peak_trips", "peak_bookings_rs"]]
      .sum().tolist() == [fa["rows"], fa["hours"], fa["trips"], fa["bookings"]])
for nid, val, shown in [("pre_launch_hours_after", pre_a["hours"], "144,000 hours"),
                        ("pre_launch_trips_after", pre_a["trips"], "227,240 trips"),
                        ("pre_launch_bookings_after_rs", pre_a["bookings"], "Rs 37,494,600"),
                        ("joiner_hours_after", join_a["hours"], "2,300 hours"),
                        ("joiner_trips_after", join_a["trips"], "3,660 trips"),
                        ("joiner_bookings_after_rs", join_a["bookings"], "Rs 603,900")]:
    add(nid, val, shown, "Monday's driver_weeks split by joined_month, after the launch",
        "data/C2_W04_D02_driver_groups_STUDENT.csv; notebook cell 8")
check("second route: fare x trips per hour = rupees per hour, both windows",
      abs(165 * fb["trips"] / fb["hours"] - fb["per_hour"]) < 1e-9
      and abs(165 * fa["trips"] / fa["hours"] - fa["per_hour"]) < 1e-9)

# Driver operations' "drivers will log off" is false for the drivers outside Monday's idle tail.
# Monday's settled answer counts the 880 drivers who were there before the launch and sit outside
# the tail (Monday's drivers_others), so Tuesday copies those ids and recounts them here; the 140
# joiners are a separate group, and none of them is in the tail.
after_rate = A.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
idle_ids = set(after_rate[after_rate.peak_trips / after_rate.peak_online_hours < 1.0].index)
check("Monday's idle tail recounts to 180 drivers", len(idle_ids) == M["idle_tail_drivers"])
joiners = set(drivers[drivers.joined_month == "2026-09"].driver_id)
check("none of the 140 joiners sits in the idle tail", len(idle_ids & joiners) == 0)
others = dw[~dw.driver_id.isin(idle_ids | joiners)]
ob, oa = three(others[others.window == "before"]), three(others[others.window == "after"])
check("the other drivers recount to Monday's 880", others.driver_id.nunique() == M["drivers_others"])
check("their hours and trips recount to Monday's ids, both windows",
      (ob["hours"], oa["hours"], ob["trips"], oa["trips"])
      == (M["others_hours_before"], M["others_hours_after"],
          M["others_trips_before"], M["others_trips_after"]))
check("their trips per online hour are Monday's 1.90 in both windows",
      round(ob["trips"] / ob["hours"], 2) == M["others_tph_before"] == 1.9
      and round(oa["trips"] / oa["hours"], 2) == M["others_tph_after"] == 1.9)
rest_topup = int(dw[(dw.window == "after") & ~dw.driver_id.isin(idle_ids)].topup_rs.sum())
check("the drivers outside the tail were paid Monday's Rs 74.1 lakh of top-up",
      rest_topup == M["topup_high_acceptance_rs"])
for mid, shown in [("drivers_others", "880 drivers"), ("others_hours_before", "98,000 hours"),
                   ("others_hours_after", "102,000 hours"), ("others_trips_before", "186,200 trips"),
                   ("others_trips_after", "193,800 trips"), ("others_tph_before", "1.90"),
                   ("others_tph_after", "1.90")]:
    reuse(mid, shown)
add("others_trips_change_pct", round((oa["trips"] / ob["trips"] - 1) * 100, 1), "up 4 percent",
    "193,800 / 186,200 - 1, the other 880 drivers", "role cards; studio solution")
add("idle_tph_after", round(M["idle_trips_after"] / M["idle_hours_after"], 1), "0.8 trips an hour",
    "33,440 / 42,000, the idle tail after the launch", "studio solution; notes")
add("idle_tail_joiners", 0, "none of the 140", "joiners among the 180 idle-tail drivers",
    "half1 S20; role cards; exercises")
# Transcript 1's per-driver-week line, by group: the hours rise sits in the idle tail.
weeks_in_window = 6
idle_wk_b = M["idle_hours_before"] / (M["idle_tail_drivers"] * weeks_in_window)
others_wk_b = ob["hours"] / (M["drivers_others"] * weeks_in_window)
others_wk_a = oa["hours"] / (M["drivers_others"] * weeks_in_window)
add("idle_hours_per_week_before", round(idle_wk_b, 1), "about 18.5 hours a week",
    "20,000 / (180 x 6), the idle tail before the launch", "extras transcript 1; notebook 10; scorecards")
reuse("idle_hours_per_driver_week_after", "about 39 hours a week")
add("idle_hours_per_week_after", round(M["idle_hours_after"] / (M["idle_tail_drivers"] * weeks_in_window), 1),
    "38.9 hours a week", "42,000 / (180 x 6), the idle tail after the launch, as notebook 10 prints it",
    "notebook 10")
add("idle_trips_fall_pct", round((1 - M["idle_trips_after"] / M["idle_trips_before"]) * 100),
    "12 percent fewer trips", "1 - 33,440 / 38,000, the idle tail", "extras transcript 1; notebook 10; scorecards")
add("others_hours_per_week_rise", round(others_wk_a - others_wk_b, 2), "under one more hour a week",
    "102,000 / 5,280 - 98,000 / 5,280, the other 880 drivers", "extras transcript 1; notebook 10")
check("the idle tail doubled its weekly hours while the other 880 added under one",
      round(M["idle_hours_after"] / M["idle_hours_before"], 1) == 2.1 and others_wk_a - others_wk_b < 1)

# Where the idle money went and what riders got, for the defence and transcript 1
zr = zw.groupby("zone").peak_requests.sum().sort_values()
outer = set(zr.index[:M["zones_outer"]])
A2 = A.assign(acc=A.peak_accepted / A.peak_offers)
low = A2[A2.acc < 0.5]
check("the low-acceptance driver-weeks carry Monday's Rs 1.159 crore", int(low.topup_rs.sum()) == M["topup_low_acceptance_rs"])
add("idle_topup_outer_share", round(low[low.zone_mode.isin(outer)].topup_rs.sum() / low.topup_rs.sum(), 2),
    "74 percent", "top-up to low-acceptance driver-weeks whose zone_mode is one of the three outer zones",
    "half1 S4, S20; notes; extras transcript 1")
add("low_acceptance_no_trip_share", round(low.peak_hours_no_trip.sum() / low.peak_online_hours.sum(), 2),
    "72 percent", "hours with no trip over online hours, low-acceptance driver-weeks after the launch",
    "extras transcript 1")
zw_w = zw.assign(outer=zw.zone.isin(outer))
check("Monday's outer-zone waits recount: the middle of the outer zone-week medians, 6.6 and 5.95",
      (zw_w[(zw_w.window == "before") & zw_w.outer].median_wait_min.median(),
       zw_w[(zw_w.window == "after") & zw_w.outer].median_wait_min.median())
      == (M["outer_wait_before"], M["outer_wait_after"]))
reuse("outer_wait_before", "6.6 minutes")
reuse("outer_wait_after", "about 6 minutes (5.95)")
wk = dw.groupby("week_start")[["peak_trips", "peak_online_hours"]].sum()
last3 = ["2026-09-21", "2026-09-28", "2026-10-05"]
add("tph_last_three_after", round(wk.loc[last3].peak_trips.sum() / wk.loc[last3].peak_online_hours.sum(), 2),
    "1.56", "trips over hours in the weeks of 21 September to 5 October",
    "half1 S20, S23; notes; extras transcript 1; studio solution")
wr = zw.groupby("week_start").peak_requests.sum()
add("requests_last_three_low", int(wr.loc[last3].min()), "41,161", "fewest weekly requests, last three weeks",
    "half1 S23 notes; extras transcript 1")
add("requests_last_three_high", int(wr.loc[last3].max()), "42,602", "most weekly requests, last three weeks",
    "half1 S23 notes; extras transcript 1")
before_weeks = sorted(w for w in wr.index if dt.date.fromisoformat(w) < LAUNCH)
add("requests_before_week_low", int(wr.loc[before_weeks].min()), "41,155", "fewest weekly requests, before",
    "half1 S23 notes; extras transcript 1")
add("requests_before_week_high", int(wr.loc[before_weeks].max()), "42,719", "most weekly requests, before",
    "half1 S23 notes; extras transcript 1")
check("the last three weeks' requests sit inside the before window's weekly range",
      wr.loc[before_weeks].min() <= wr.loc[last3].min() and wr.loc[last3].max() <= wr.loc[before_weeks].max())
add("idle_tail_tph_before", round(M["idle_trips_before"] / M["idle_hours_before"], 2), "1.90",
    "38,000 / 20,000: the idle tail before the launch", "half1 S20 notes; role cards; extras")

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
    "about 1,018 an hour", "256,556 / 252", "half2 S10; notebook cell 14; guesstimate note")
add("drivers_online_per_peak_hour_after", round(M["hours_after"] / peak_hours_window),
    "about 581 drivers", "146,300 / 252", "guesstimate note")
add("driver_hours_per_request_before", round(dh_req_b, 2), "0.47", "118,000 / 251,910",
    "half2 S10; notebook cell 14; notes; exercises")
add("driver_hours_per_request_after", round(dh_req_a, 2), "0.57", "146,300 / 256,556",
    "half2 S10; notebook cell 14; notes")
check("driver-hours per request 0.47 before and 0.57 after",
      (round(dh_req_b, 2), round(dh_req_a, 2)) == (0.47, 0.57))
dh_trip_b = M["hours_before"] / M["trips_before"]
dh_trip_a = M["hours_after"] / M["trips_after"]
add("driver_hours_per_trip_before", round(dh_trip_b, 2), "0.53", "118,000 / 224,200, per completed trip",
    "half2 S41; notebook cell 13; notes; guesstimate note; extras transcript 2")
add("driver_hours_per_trip_after", round(dh_trip_a, 2), "0.63", "146,300 / 230,900, per completed trip",
    "half2 S41; notebook cell 13")
add("served_share_before", round(M["trips_before"] / M["requests_before"], 2), "0.89",
    "224,200 / 251,910", "half1 S4; extras transcript 1")
add("served_share_after", round(M["trips_after"] / M["requests_after"], 2), "0.90",
    "230,900 / 256,556", "half1 S4; extras transcript 1")
extra_served = M["trips_after"] - M["requests_after"] * M["trips_before"] / M["requests_before"]
add("extra_requests_served", round(extra_served, -2), "about 2,600 more requests served",
    "230,900 - 256,556 x 0.890, against the before window's served share", "half1 S4; extras transcript 1")
add("topup_per_extra_trip_rs", round(M["topup_after_rs"] / (M["trips_after"] - M["trips_before"])),
    "at least Rs 2,836 for each extra trip", "19,000,000 / (230,900 - 224,200)", "half1 S4; extras transcript 1")
check("about 2,600 more requests served, at Rs 2,836 of top-up for each extra trip",
      round(extra_served, -2) == 2600 and round(19_000_000 / 6_700) == 2836)

# ------------------------------------------------------------------ drivers at the evening peak
assume("hyd_people", 1e7, 9e6, 1.1e7, "about 1 crore people",
       "a round number for the Hyderabad metro area, said aloud and to be checked", "half2 S8; notebook; note")
assume("weekday_ride_share", 0.01, 0.005, 0.015, "1 trip for every 100 people",
       "weekday Uber trips per person, counted in trips, so a commuter who rides both ways counts twice",
       "half2 S38; notebook; note")
assume("evening_share", 0.25, 0.20, 0.30, "a quarter",
       "share of the day's trips that fall in the three evening peak hours", "half2 S8; notebook; note")
assume("trips_per_busy_hour", 2.4, 2.0, 3.0, "2.4 trips",
       "a peak trip takes about 25 minutes from accepting to dropping, so a busy driver fits 2.4 an hour",
       "half2 S8; notebook; note")
assume("idle_share", 0.30, 0.22, 0.38, "0.30",
       "share of online drivers with no rider at a given moment, a guess said aloud from a busy evening "
       "to a slack one; the validate step checks it like for like", "half2 S38; notebook; note")
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
add("requests_per_evening_hour", round(req_hour), "about 8,330 an hour",
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
evening_trips = base["hyd_people"] * base["weekday_ride_share"] * base["evening_share"]
before_buffer = req_hour / (base["trips_per_busy_hour"] * (1 - base["idle_share"]))
four_hour_req = evening_trips / 4
four_hour_drivers = four_hour_req / (base["trips_per_busy_hour"] * (1 - base["idle_share"])) * base["buffer"]
add("evening_window_trips", round(evening_trips), "25,000 trips in the window", "1 lakh x a quarter",
    "half2 S39, S49; notebook; note")
add("drivers_before_buffer", round(before_buffer, -1), "about 4,960 drivers", "8,333 / 1.68",
    "half2 S39; note")
add("four_hour_requests_per_hour", round(four_hour_req), "about 6,250 an hour",
    "25,000 / 4 hours, if a fourth hour adds no trips", "half2 S49; extras transcript 2; scorecards")
add("four_hour_drivers_wrong", round(four_hour_drivers, -2), "about 4,300 drivers",
    "6,250 / 1.68 x 1.15: the weak answer, which lets a longer window shrink the busiest moment",
    "scorecards (the weak answer)")
peak_rate = req_hour * base["buffer"]
add("four_hour_buffer", round(peak_rate / four_hour_req, 2), "about 1.53",
    "8,333 x 1.15 / 6,250: the busiest half hour over a four-hour window's average hour",
    "half2 S50 notes; extras transcript 2; scorecards")
check("a four-hour window keeps the busiest half hour: buffer 1.53, about 5,700 drivers",
      round(peak_rate / four_hour_req, 2) == 1.53
      and round(four_hour_req / (base["trips_per_busy_hour"] * (1 - base["idle_share"]))
                * peak_rate / four_hour_req, -2) == 5700)
add("busy_share", round(1 - base["idle_share"], 2), "0.70 (70 percent)", "1 - the idle share of 0.30",
    "half2 S39; notebook; guided exercise; notes")
add("buffer_pct", round((base["buffer"] - 1) * 100), "15 percent", "a buffer of 1.15", "extras transcript 2; notes")
add("distractor_divided_by_busy", round(base["trips_per_busy_hour"] / (1 - base["idle_share"]), 2), "3.43",
    "2.4 / 0.70, the division done the wrong way", "guided exercise Q3 (distractor)")
add("distractor_times_idle", round(base["trips_per_busy_hour"] * base["idle_share"], 2), "0.72",
    "2.4 x 0.30, the idle drivers' share", "guided exercise Q3 (distractor)")
# The guided set's third item: the same two factors at Monday's after-launch idle share, 0.38
hi_idle = M["no_trip_share_after"]
add("busy_share_at_idle_038", round(1 - hi_idle, 2), "0.62 (62 percent)", "1 - 0.38",
    "guided exercise Q3 and its solution")
add("tph_online_at_idle_038", round(base["trips_per_busy_hour"] * (1 - hi_idle), 2), "about 1.49",
    "2.4 x (1 - 0.38)", "guided exercise Q3 (key)")
add("distractor_times_idle_038", round(base["trips_per_busy_hour"] * hi_idle, 2), "0.91",
    "2.4 x 0.38, the idle drivers' share", "guided exercise Q3 (distractor)")
add("distractor_divided_by_busy_038", round(base["trips_per_busy_hour"] / (1 - hi_idle), 2), "3.87",
    "2.4 / 0.62, the division done the wrong way", "guided exercise Q3 (distractor)")
add("distractor_minus_idle_038", round(base["trips_per_busy_hour"] - hi_idle, 2), "2.02",
    "2.4 - 0.38, a share subtracted from a rate", "guided exercise Q3 (distractor)")
check("guided Q3: 2.4 x 0.62 = 1.49, and its three wrong ways are 0.91, 3.87 and 2.02",
      (round(2.4 * 0.62, 2), round(2.4 * 0.38, 2), round(2.4 / 0.62, 2), round(2.4 - 0.38, 2))
      == (1.49, 0.91, 3.87, 2.02))
chain_dh = 1 / (base["trips_per_busy_hour"] * (1 - base["idle_share"]))
add("driver_hours_per_request_chain", round(chain_dh, 2), "0.60",
    "1 / 1.68, before the buffer", "half2 S10; notebook cell 14; notes")
add("chain_over_case_before", round(chain_dh / dh_req_b, 2), "about a quarter more",
    "0.595 / 0.468", "half2 S10; notebook cell 14")
chain_trip = chain_dh / dh_trip_b
add("chain_over_case_per_trip", round(chain_trip, 2), "about an eighth more (13 percent)",
    "0.595 / 0.526: the chain's driver-hours per trip over the case's, before the launch",
    "half2 S41; notebook cell 13; notes; guesstimate note; extras transcript 2")
case_tph_b = M["trips_before"] / M["hours_before"]
validated = req_hour / case_tph_b * base["buffer"]
add("drivers_at_case_tph", round(validated, -2), "about 5,000 drivers",
    "8,333 / 1.90 x 1.15: the chain re-run at the case's own trips per online hour before the launch",
    "half2 S41, S46, S56; notebook cell 13; notes; sheet; guesstimate note; extras transcript 2")
trip_min = 60 / base["trips_per_busy_hour"]
add("idle_like_before", round(1 - case_tph_b * trip_min / 60, 2), "about 0.21",
    "1 - 1.90 trips x 25 minutes / 60: idle at a moment, like for like, before the launch",
    "half2 S41 notes; extras transcript 2; guesstimate note")
add("idle_like_after", round(1 - M["trips_after"] / M["hours_after"] * trip_min / 60, 2), "about 0.34",
    "1 - 1.578 trips x 25 minutes / 60, after the launch", "extras transcript 2; guesstimate note")
two_per_100 = drivers_needed(base["hyd_people"], 2 * base["weekday_ride_share"], base["evening_share"],
                             base["trips_per_busy_hour"], base["idle_share"], base["buffer"])
add("drivers_at_two_per_100", round(two_per_100), "about 11,400 drivers",
    "the chain with 2 weekday trips per 100 people: the answer doubles, since the chain is a product",
    "notebook cells 11 and 12")
check("Monday's extra_trips is the after window's trips less the before window's",
      M["extra_trips"] == M["trips_after"] - M["trips_before"] == 6700)
reuse("extra_trips", "6,700 extra trips")
check("validate: the chain runs 13 percent high per trip, and the case's 1.90 trips an hour gives about 5,000",
      round(chain_trip, 2) == 1.13 and round(validated, -2) == 5000)
add("floor_cost_thousand_drivers_evening_rs", 1000 * M["peak_window_hours"] * 300, "up to Rs 9 lakh an evening",
    "1,000 drivers x 3 hours x the Rs 300 floor, if they carry no trips", "extras transcript 2; scorecards")
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
       "transactions a day in September 2026; checked 12 October 2026 at https://www.outlookmoney.com/banking/"
       "upi-processes-2407-billion-transactions-worth-rs-2937-lakh-crore-in-september",
       "half2 S12, S13; notebook cell 14; notes; Kahoot; exercises")
public("upi_month_total", 24_070_000_000, "24.07 billion in the month", "T3",
       "the same report: 24.07 billion transactions worth Rs 29.37 lakh crore in September 2026",
       "half2 S13; Kahoot; exercises")
add("upi_estimate_per_day", int(upi_est), "70 crore a day (700 million)", "35 crore x 2",
    "half2 S12, S13; notebook cell 14; notes")
add("upi_estimate_gap_pct", round((upi_est / 802_000_000 - 1) * 100, 1), "about 13 percent below",
    "700 million / 802 million - 1", "half2 S13; notebook cell 14; notes")
add("upi_value_per_payment_rs", round(29.37e12 / 24.07e9), "about Rs 1,220 a payment",
    "Rs 29.37 lakh crore / 24.07 billion: far above a tea, so the count holds large transfers between people",
    "half2 S44; notes; guesstimate note; paired solution")
add("upi_daily_times_31_billion", round(802e6 * 31 / 1e9, 2), "24.86 billion",
    "802 million x 31, a month total built on the wrong number of days", "mid-session drill 2 Q1 (distractor)")
add("upi_month_over_30", round(24_070_000_000 / 30 / 1e6), "802 million", "24.07 billion / 30 days",
    "half2 S13; Kahoot; exercises")
add("upi_month_over_31", round(24_070_000_000 / 31 / 1e6), "776 million", "24.07 billion / 31 days",
    "half2 S13; Kahoot; exercises")
add("upi_31_day_gap_pct", round((24_070_000_000 / 31) / (24_070_000_000 / 30) * 100 - 100, 1),
    "about 3 percent low", "30 / 31 - 1", "half2 S13; Kahoot")
add("upi_estimate_millions", 700, "700 million", "35 crore x 2, in millions", "half2 S44; notebook; notes")
add("september_days", 30, "30 days", "the days in September 2026", "half2 S44; notebook; Kahoot; exercises")
add("a_31_day_month", 31, "31 days", "the wrong divisor for September", "half2 S44; notebook; Kahoot; exercises")
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
       "checked 12 October 2026 at https://stories.flipkart.com/announcement/india-logs-on-for-the-big-billion-days-flipkart-"
       "records-63-million-concurrent-users-as-the-festive-season-opens",
       "half2 S14; Kahoot; notes; exercises")
add("flipkart_url_number", 63, "63", "the number in the URL slug, in millions", "half2 S45, S53; notes; sheet")
public("flipkart_url_reading", 63_000_000, "63 million (the URL slug)", "T3", "the same page's URL",
       "half2 S14; Kahoot; notes")
public("dmrc_journeys_2026", 6_406_000, "64.06 lakh journeys a day", "M6",
       "The Tribune, updated 9 August 2026, citing DMRC: average daily ridership of 64.06 lakh "
       "journeys; checked 12 October 2026 at https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-"
       "punctuality-in-2026-dmrc/", "half2 S14; exercises; notes")
public("dmrc_boardings_record", 8_244_903, "82,44,903 boardings", "M6",
       "Republic World, 18 September 2026, quoting DMRC: highest-ever passenger boardings of "
       "82,44,903 on 17 September 2026; checked 12 October 2026 at https://www.republicworld.com/india/delhi-metro-breaks-"
       "all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241",
       "half2 S14; exercises; notes")
public("dmrc_line_utilisation_2018", 4_535_932, "45,35,932 line uses", "M6",
       "PTI via LatestLY, 30 May 2018: line utilisation on 29 May 2018 was 45,35,932, against gate "
       "ridership near 27 lakh a day in February 2018; checked 12 October 2026 at https://www.latestly.com/agency-news/dmrc-"
       "uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp",
       "notes (the unit trap)")
public("dmrc_ridership_2018", 2_700_000, "27 lakh a day", "M6", "the same report", "notes (the unit trap)")
public("amazon_memo_pages", 6, "six-page memo", "T1",
       "Amazon's 2017 letter to shareholders, filed 18 April 2018: 'We don't do PowerPoint (or any "
       "other slide-oriented) presentations'; memos are read silently at the start of each meeting; "
       "'a great memo probably should take a week or more'; checked 12 October 2026 at https://www.sec.gov/Archives/edgar/data/"
       "1018724/000119312518121161/d456916dex991.htm", "half1 S27; notes; Kahoot; exercises")
public("dmart_revenue_fy26_crore", 66968, "Rs 66,968 crore", "T3",
       "Avenue Supermarts press release, 2 May 2026: standalone total revenue for FY26 Rs 66,968 "
       "crore; 85 stores added in FY26; 500 stores at 31 March 2026; two-year-old stores grew 10.8 "
       "percent in Q4 FY26; checked 12 October 2026 at https://nsearchives.nseindia.com/corporate/DMART_02052026173007_"
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
add("dmart_average_store_count", 457.5, "457.5 stores", "(415 + 500) / 2", "Kalpa exercise solution")
add("dmart_revenue_over_added", round(66968 / 85, 1), "about Rs 788 crore",
    "66,968 / 85, dividing by the stores added: a wrong denominator", "Kalpa exercise (distractor)")
public("upi_month_value_lakh_crore", 29.37, "Rs 29.37 lakh crore", "T3",
       "the same Outlook Money report: the September 2026 transactions were worth Rs 29.37 lakh crore",
       "mid-session drill 2 (distractor); its solution")

public("ziegler_2022", 2022, "Ziegler and colleagues, 2022", "fresh check",
       "Productivity Assessment of Neural Code Completion, arXiv 2205.06537, submitted 13 May 2022, a study "
       "of GitHub Copilot's users: the rate at which shown suggestions are accepted, rather than the "
       "persistence of completions in the code, drives developers' perception of productivity",
       "half2 S51; extras AI variant; notes")
public("metr_2025_slower_pct", 19, "19 percent longer", "fresh check",
       "METR, 10 July 2025: 16 experienced open-source developers, 246 issues; with AI tools allowed they "
       "took 19 percent longer, expected a 24 percent speed-up and afterwards believed 20 percent; the "
       "page now says the results are out of date", "extras AI variant; scorecards")
public("metr_2025_believed_pct", 20, "20 percent faster", "fresh check", "the same METR page", "extras AI variant")
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
     "used_by": "half1 SECTION 1 (the first prediction); notes"},
    {"id": "toy_canteen_tea", "label": "invented",
     "values": {"students": 3000, "share_who_buy_tea": 0.45, "tea_buyers": 1350, "cups_each": 2,
                "cups_a_day": 2700},
     "used_by": "half2 SECTION 6; guided exercise Q3's worked example; notes; every value also under "
                "its own toy_canteen_ id in toy_numbers"},
    {"id": "toy_two_million_city", "label": "invented",
     "values": {"people": 2_000_000, "wrong_households": 8_000_000, "people_per_household": 4,
                "right_households": 500_000},
     "used_by": "half2, SECTION 8's three published traps; Kahoot Q5"},
    {"id": "toy_kahoot_q6", "label": "invented",
     "values": {"trips_a_day": 100000, "trips_per_busy_hour": 2.5, "wrong_drivers": 40000},
     "used_by": "Kahoot Q6"},
    {"id": "toy_kahoot_q8", "label": "invented",
     "values": {"month_total_billion": 31, "days": 31, "per_day_billion": 1, "over_30_days_billion": 1.03},
     "used_by": "exercises ch6 Q6 (moved from the Kahoot, whose Q8 now tests the written case)"},
    {"id": "toy_auto_driver", "label": "invented",
     "values": {"day_rs": 1800, "monday_rides": 20, "monday_hours": 9, "tuesday_rides": 18,
                "tuesday_hours": 12, "monday_per_ride_rs": 90, "tuesday_per_ride_rs": 100,
                "monday_per_hour_rs": 200, "tuesday_per_hour_rs": 150},
     "used_by": "notebook 01's your-turn cell, the faded second example; notes, chapter 1's second example"},
    {"id": "toy_payments_month", "label": "invented",
     "values": {"month_total_billion": 9, "days_in_month": 30, "per_day_million": 300,
                "over_31_days_million": 290, "gap_pct": -3.2},
     "used_by": "notebook 08, the per-day check on an invented network"},
    {"id": "toy_food_stall", "label": "invented",
     "values": {"sales_rs": 12000, "orders": 240, "staff_hours": 40, "staff_days": 5,
                "per_order_rs": 50, "per_staff_hour_rs": 300, "per_staff_day_rs": 2400},
     "used_by": "lab set P2 and its solution"},
    {"id": "toy_kalpa_store_overshoot", "label": "invented",
     "values": {"first_year_sales_crore": 150},
     "used_by": "Kalpa exercise Q2 and its solution"},
    {"id": "toy_ai_acceptance_rate", "label": "invented",
     "values": {"acceptance_rate_pct": 32, "retained_share_of_accepted": 0.8, "retained_pct_of_shown": 26,
                "retained_after_days": 7},
     "used_by": "half2 S21; extras AI variant; notes"},
]

check("the auto driver's three reads: per day flat, per ride up, per hour down",
      (1800 / 20, 1800 / 18, 1800 / 9, 1800 / 12) == (90, 100, 200, 150))

# ------------------------------------------------------------------ the concept chapters' examples
# The five concept chapters teach the row's subtopics on invented everyday examples before Uber
# applies them. Each example is written to data/ here, and every number a learner sees on it is
# recorded under a toy_ id, with the chapter it was invented for and the files that use it. No
# randomness: the tables are typed below and every total is asserted.
S1 = "The one-slide answer: claim, evidence, caveat, action"
S2 = "What to leave out, and the appendix"
S3 = "Defending under challenge: restate, answer, concede, what would change your mind"
S4 = "The guesstimate: clarify, map, calculate, validate"
S5 = "The AI-free written business case"
facts["toy_numbers"] = []


def toy(tid, value, shown, subtopic, how, used_by, unit=""):
    facts["toy_numbers"].append({"id": tid, "value": plain(value), "shown": shown, "unit": unit,
                                 "how": f"invented for the concept chapter on {subtopic}: {how}",
                                 "used_by": used_by})


# Ramesh's kirana shop opens two more hours a day in October. Four weeks either side, 56 days.
SEPT_CUSTOMERS = [117, 118, 121, 118, 120, 121, 123, 117, 105, 119, 118, 120, 122, 122,
                  118, 119, 120, 119, 121, 104, 124, 118, 119, 120, 121, 121, 122, 125]
OCT_CUSTOMERS = [120, 121, 122, 110, 124, 125, 127, 128, 129, 130, 129, 131, 132, 134,
                 128, 129, 130, 129, 131, 132, 134, 121, 122, 123, 111, 124, 125, 127]
# Two rain days in each month, so the weather drags both months alike and explains none of the
# change; the festival fortnight is the one difference the slide has to carry as its caveat.
SEPT_RAIN, OCT_RAIN, FESTIVAL = {9, 20}, {4, 25}, set(range(8, 22))
SPREAD = [120, -80, 40, -160, 60, 0, 20]      # a week's spread around Rs 100 a customer; sums to 0
rows = []
for month, hours, customers, rain in (("September", 10, SEPT_CUSTOMERS, SEPT_RAIN),
                                      ("October", 12, OCT_CUSTOMERS, OCT_RAIN)):
    for day, c in enumerate(customers, start=1):
        rows.append({"month": month, "day": day, "hours_open": hours, "customers": c,
                     "sales_rs": 100 * c + SPREAD[(day - 1) % 7],
                     "rain_day": "yes" if day in rain else "no",
                     "festival_day": "yes" if month == "October" and day in FESTIVAL else "no"})
kirana = pd.DataFrame(rows)
kirana.to_csv(DATA / f"{STEM}_kirana_days_STUDENT.csv", index=False)
km = kirana.groupby("month", sort=False).agg(days=("day", "count"), hours=("hours_open", "mean"),
                                             customers=("customers", "sum"), sales=("sales_rs", "sum"))
sep, octo = km.loc["September"], km.loc["October"]
per_day = (sep.sales / sep.days, octo.sales / octo.days)
per_hour = (per_day[0] / sep.hours, per_day[1] / octo.hours)
per_cust = (sep.sales / sep.customers, octo.sales / octo.customers)
check("kirana: 28 days a month, 10 hours open in September and 12 in October",
      (sep.days, octo.days, sep.hours, octo.hours) == (28, 28, 10, 12))
check("kirana: 119 and 126 customers a day", (sep.customers / 28, octo.customers / 28) == (119, 126))
check("kirana: Rs 11,900 and Rs 12,600 a day", per_day == (11900, 12600))
check("kirana: Rs 1,190 and Rs 1,050 an hour", per_hour == (1190, 1050))
check("kirana: Rs 100 a customer in both months", per_cust == (100, 100))
check("kirana: per day up 5.9 percent, per hour down 11.8 percent",
      (round((per_day[1] / per_day[0] - 1) * 100, 1), round((per_hour[1] / per_hour[0] - 1) * 100, 1))
      == (5.9, -11.8))
check("kirana: 2 rain days in each month, 14 festival days",
      (len(SEPT_RAIN), len(OCT_RAIN), len(FESTIVAL)) == (2, 2, 14))
check("kirana: every October day sells less an hour than every dry September day",
      kirana[kirana.month == "October"].eval("sales_rs / hours_open").max()
      < kirana[(kirana.month == "September") & (kirana.rain_day == "no")].eval("sales_rs / hours_open").min())
check("kirana: no number echoes the case (not 17 percent, 0.8 percent, Rs 165 or 5,700)",
      not {5.9, 11.8, 119, 126, 11900, 12600, 1190, 1050} & {17, 0.8, 165, 5700})
for tid, v, shown, how, used in [
    ("toy_kirana_days_each_month", 28, "four weeks (28 days)", "days counted on each side of the change",
     "data/C2_W04_D02_kirana_days_STUDENT.csv; half1 SECTION 1; notebooks 01, 02; notes"),
    ("toy_kirana_days", 56, "56 days", "the four weeks either side, the table's rows", "notebook 01"),
    ("toy_kirana_hours_sep", 10, "10 hours a day", "hours open each day in September",
     "half1 SECTION 1; notebooks 01, 07; exercises ch1; notes"),
    ("toy_kirana_hours_oct", 12, "12 hours a day", "hours open each day in October, two more",
     "half1 SECTION 1; notebooks 01, 07; exercises ch1; notes"),
    ("toy_kirana_extra_hours", 2, "two more hours", "the change: 12 hours less 10", "half1 SECTION 1; notes"),
    ("toy_kirana_customers_sep", 119, "119 customers a day", "3,332 customers over 28 September days",
     "half1 SECTIONs 1, 2; notebooks 01, 02, 07; exercises ch1, ch2; notes"),
    ("toy_kirana_customers_oct", 126, "126 customers a day", "3,528 customers over 28 October days",
     "half1 SECTIONs 1, 2; notebooks 01, 02, 07; exercises ch1, ch2; notes"),
    ("toy_kirana_customers_sep_total", 3332, "3,332", "the September column's sum", "notebook 01"),
    ("toy_kirana_customers_oct_total", 3528, "3,528", "the October column's sum", "notebook 01"),
    ("toy_kirana_sales_day_sep", 11900, "Rs 11,900 a day", "Rs 3,33,200 over 28 September days",
     "half1 SECTIONs 1, 2; notebooks 01, 07; exercises ch1, ch7; Kahoot Q8; notes; sheet"),
    ("toy_kirana_sales_day_oct", 12600, "Rs 12,600 a day", "Rs 3,52,800 over 28 October days",
     "half1 SECTIONs 1, 2; notebooks 01, 07; exercises ch1, ch7; Kahoot Q8; notes; sheet"),
    ("toy_kirana_sales_sep_total", 333200, "Rs 3.33 lakh", "four weeks of September sales, Rs 3,33,200",
     "half1 SECTION 2; notebook 02; notes", ),
    ("toy_kirana_sales_oct_total", 352800, "Rs 3.53 lakh", "four weeks of October sales, Rs 3,52,800",
     "half1 SECTION 2; notebook 02; notes"),
    ("toy_kirana_rise_day", 700, "Rs 700 a day", "12,600 less 11,900, the son's number",
     "half1 SECTIONs 1, 7; notebooks 01, 07; exercises ch1, ch7; Kahoot Q8; notes; sheet"),
    ("toy_kirana_rise_day_pct", 5.9, "up 5.9 percent", "12,600 / 11,900 - 1",
     "half1 SECTION 1; notebook 01; notes; sheet"),
    ("toy_kirana_per_hour_sep", 1190, "Rs 1,190 an hour", "11,900 / 10",
     "half1 SECTIONs 1, 2, 7; notebooks 01, 02, 07; exercises ch1, ch7; Kahoot Q8; notes; sheet"),
    ("toy_kirana_per_hour_oct", 1050, "Rs 1,050 an hour", "12,600 / 12",
     "half1 SECTIONs 1, 2, 7; notebooks 01, 02, 07; exercises ch1, ch7; Kahoot Q8; notes; sheet"),
    ("toy_kirana_per_hour_pct", -11.8, "down 11.8 percent", "1,050 / 1,190 - 1",
     "half1 SECTION 1; notebook 01; exercises ch1; notes; sheet"),
    ("toy_kirana_per_customer", 100, "Rs 100 a customer", "11,900 / 119 and 12,600 / 126",
     "half1 SECTIONs 1, 2, 7; notebooks 01, 02, 07; exercises ch1; notes; sheet"),
    ("toy_kirana_rain_sep", 2, "2 rain days", "September's days marked rain, as many as October's",
     "half1 SECTION 2; notebook 02; exercises ch2; notes"),
    ("toy_kirana_rain_oct", 2, "2 rain days", "October's days marked rain, as many as September's",
     "half1 SECTION 2; notebook 02; exercises ch2; notes"),
    ("toy_kirana_festival_days", 14, "14 of October's 28 days", "the festival fortnight, October's days 8 to 21",
     "half1 SECTIONs 1, 2, 7; notebooks 01, 02, 07; exercises ch2; notes"),
]:
    toy(tid, v, shown, S1, how, used)
toy("toy_kirana_extra_hour_rs", 350, "Rs 350 an hour", S1, "the most each of the two added hours can have "
    "sold: the Rs 700 rise over the 2 extra hours, if the old ten hours sold as they did in September",
    "half1 SECTION 1; notebooks 01, 02; exercises ch1; notes; sheet; board work; day sheet")
check("the two added hours sold at most Rs 350 each", (12600 - 11900) / (12 - 10) == 350)
toy("toy_kirana_helper_rate", 85, "Rs 85 an hour", S1, "the helper's wage for each extra hour",
    "half1 SECTIONs 1, 2; notebook 02; exercises ch1, ch2; notes")
toy("toy_kirana_helper_cost", 170, "Rs 170 a day", S1, "the helper's two extra hours, 2 x Rs 85",
    "half1 SECTIONs 1, 7; notebooks 01, 07; exercises ch1, ch7; notes; sheet")
toy("toy_kirana_son_hours_sep", 4, "4 hours a day", S2, "the son's hours at the counter in September",
    "half1 SECTION 2; notebook 02; exercises ch2")
toy("toy_kirana_son_hours_oct", 6, "6 hours a day", S2, "the son's hours at the counter in October, "
    "the two extra evening hours added", "half1 SECTION 2; notebook 02; exercises ch2")
toy("toy_kirana_hour_index_oct", 88, "index 88", S5, "October's sales per hour over September's, x 100 "
    "(1,050 / 1,190 x 100 = 88.2), the draft page's method word", "notebook 07; exercises ch7")
toy("toy_kirana_days_to_decide", 30, "thirty days", S1, "the month the action keeps the hours for",
    "half1 SECTIONs 1, 7; notebooks 01, 07; notes")
check("the helper's two hours cost Rs 170", 2 * 85 == 170)
check("October's per-hour index is 88", round(1050 / 1190 * 100) == 88)

# The kirana draft slide's eight elements, routed by chapter 2's sort.
elements = pd.DataFrame([
    ("Chart: sales per hour, by day", "Rs 1,190 an hour in September, Rs 1,050 in October", "yes", "", "no"),
    ("Total sales, four weeks", "Rs 3.33 lakh in September, Rs 3.53 lakh in October", "no", "the accountant", "no"),
    ("Customers a day", "119 in September, 126 in October", "no", "the son", "no"),
    ("Rain days", "2 in September, 2 in October", "no", "", "no"),
    ("The son's hours at the counter", "4 a day in September, 6 in October", "no", "the son", "no"),
    ("The helper's wage", "Rs 85 an hour; the two extra hours cost Rs 170 a day", "no", "the accountant", "no"),
    ("The festival fortnight", "14 of October's 28 days", "no", "", "yes"),
    ("Sales per customer", "Rs 100 in both months", "yes", "", "no"),
], columns=["element", "what_it_shows", "supports_claim", "whose_question", "is_caveat"])
elements.to_csv(DATA / f"{STEM}_kirana_slide_elements_STUDENT.csv", index=False)
stay = elements[(elements.supports_claim == "yes") | (elements.is_caveat == "yes")]
check("the draft's eight elements: three stay, two go to each page, one is cut",
      (len(elements), len(stay), (elements.whose_question == "the son").sum(),
       (elements.whose_question == "the accountant").sum()) == (8, 3, 2, 2))
for tid, v, shown, how in [
        ("toy_draft_elements", 8, "eight elements", "elements on Ramesh's first draft of the slide"),
        ("toy_draft_stay", 3, "three stay", "the two that carry the claim and the caveat"),
        ("toy_draft_carry_claim", 2, "two carry the claim", "the per-hour chart and the per-customer line"),
        ("toy_draft_son_page", 2, "two go to the son's page", "customers a day and the son's hours"),
        ("toy_draft_accounts_page", 2, "two go to the accounts page", "four weeks' sales and the helper's wage"),
        ("toy_draft_cut", 1, "one is cut", "rain days, two in each month, which explain none of the change "
         "and nobody will ask about"),
        ("toy_clutter_series", 6, "six series", "lines on the cluttered chart of the 56 days"),
        ("toy_clear_series", 1, "one line", "lines on the clear chart")]:
    toy(tid, v, shown, S2, how, "half1 SECTION 2; notebook 02; exercises ch2; notes")

# A secondary school's attendance, this year and last, eight weeks each.
ATT_LAST = [76, 77, 76, 77, 77, 85, 85, 85]
ATT_THIS = [77, 76, 81, 82, 81, 89, 90, 89]
school = pd.DataFrame([{"year": y, "week": w, "attendance_pct": v, "exam_week": "yes" if w >= 6 else "no",
                        "timetable_changed": "yes" if y == "this year" and w >= 3 else "no"}
                       for y, vals in (("last year", ATT_LAST), ("this year", ATT_THIS))
                       for w, v in enumerate(vals, start=1)])
school.to_csv(DATA / f"{STEM}_school_attendance_STUDENT.csv", index=False)


def mean(xs):
    return sum(xs) / len(xs)


lift_last = mean(ATT_LAST[5:]) - mean(ATT_LAST[2:5])
lift_this = mean(ATT_THIS[5:]) - mean(ATT_THIS[2:5])
pre_rise = mean(ATT_THIS[2:5]) - mean(ATT_LAST[2:5])
whole_rise = mean(ATT_THIS[5:]) - mean(ATT_THIS[:2])
check("school: weeks 1 and 2 match in both years (76.5)", mean(ATT_LAST[:2]) == mean(ATT_THIS[:2]) == 76.5)
check("school: the exam weeks lift about 8 points in both years (8.3 and 8.0)",
      (round(lift_last, 1), round(lift_this, 1)) == (8.3, 8.0))
check("school: weeks 3 to 5 sit 4 to 5 points above last year's (4.7 on average)",
      round(pre_rise, 1) == 4.7 and [t - l for t, l in zip(ATT_THIS[2:5], ATT_LAST[2:5])] == [5, 5, 4])
check("school: the whole rise is 12.8 points, more than the exams' 8",
      round(whole_rise, 1) == 12.8 and whole_rise > max(lift_last, lift_this))
toy("toy_school_weeks", 8, "eight weeks", S3, "weeks counted in each year",
    "half1 SECTION 3; notebook 03; exercises ch3; notes")
toy("toy_school_change_week", 3, "from week 3", S3, "the week the new timetable began this year",
    "half1 SECTION 3; notebook 03; exercises ch3; notes")
for i, v in enumerate(ATT_LAST, start=1):
    toy(f"toy_school_last_w{i}", v, f"{v} percent", S3, f"last year's attendance, week {i}",
        "data/C2_W04_D02_school_attendance_STUDENT.csv; half1 SECTION 3; notebook 03; exercises ch3")
for i, v in enumerate(ATT_THIS, start=1):
    toy(f"toy_school_this_w{i}", v, f"{v} percent", S3, f"this year's attendance, week {i}",
        "data/C2_W04_D02_school_attendance_STUDENT.csv; half1 SECTION 3; notebook 03; exercises ch3")
for tid, v, shown, how in [
        ("toy_school_start_mean", 76.5, "76.5 percent", "weeks 1 and 2, the same in both years"),
        ("toy_school_lift_last", round(lift_last, 1), "8.3 points", "last year's weeks 6 to 8 over weeks 3 to 5"),
        ("toy_school_lift_this", round(lift_this, 1), "8.0 points", "this year's weeks 6 to 8 over weeks 3 to 5"),
        ("toy_school_pre_rise", round(pre_rise, 1), "4.7 points", "weeks 3 to 5, this year over last year"),
        ("toy_school_whole_rise", round(whole_rise, 1), "12.8 points", "this year's weeks 6 to 8 over weeks 1 and 2"),
        ("toy_school_w35_last", round(mean(ATT_LAST[2:5]), 1), "76.7 percent", "last year's weeks 3 to 5"),
        ("toy_school_w35_this", round(mean(ATT_THIS[2:5]), 1), "81.3 percent", "this year's weeks 3 to 5"),
        ("toy_school_exam_last", round(mean(ATT_LAST[5:]), 1), "85.0 percent", "last year's exam weeks"),
        ("toy_school_exam_this", round(mean(ATT_THIS[5:]), 1), "89.3 percent", "this year's exam weeks")]:
    toy(tid, v, shown, S3, how, "half1 SECTION 3; notebook 03; exercises ch3; notes; sheet")

# The campus canteen's tea, sized from nothing, then checked against five weekdays of its till.
ledger = pd.DataFrame([
    ("students on campus", 3000, 2700, 3300, "students", "the campus head count, rounded"),
    ("share who buy tea on a weekday", 0.45, 0.25, 0.65, "share of students", "a guess from the queue at the counter"),
    ("cups each buyer drinks", 2, 1.5, 2.5, "cups a buyer", "one in the morning, one after lunch"),
], columns=["factor", "central", "low", "high", "unit", "why"])
ledger.to_csv(DATA / f"{STEM}_canteen_ledger_STUDENT.csv", index=False)
TILL = [("Monday", 2295), ("Tuesday", 2380), ("Wednesday", 2310), ("Thursday", 2375), ("Friday", 2340)]
pd.DataFrame(TILL, columns=["weekday", "cups_sold"]).to_csv(DATA / f"{STEM}_canteen_till_STUDENT.csv", index=False)
cups = 3000 * 0.45 * 2
till_mean = mean([c for _, c in TILL])
implied_share = till_mean / (3000 * 2)
swing_canteen = {"students on campus": (2700 * 0.45 * 2, 3300 * 0.45 * 2),
                 "share who buy tea on a weekday": (3000 * 0.25 * 2, 3000 * 0.65 * 2),
                 "cups each buyer drinks": (3000 * 0.45 * 1.5, 3000 * 0.45 * 2.5)}
check("canteen: 3,000 x 0.45 x 2 = 2,700 cups, from 1,350 buyers", (cups, 3000 * 0.45) == (2700, 1350))
check("canteen: the till averages 2,340 cups over five weekdays", till_mean == 2340)
check("canteen: the chain runs 15.4 percent high, and a share of 0.39 lands on the till",
      round((cups / till_mean - 1) * 100, 1) == 15.4 and round(implied_share, 2) == 0.39
      and 3000 * 0.39 * 2 == till_mean)
check("canteen: the share who buy sets the range (1,500 to 3,900, wider than the others)",
      max(swing_canteen, key=lambda k: swing_canteen[k][1] - swing_canteen[k][0])
      == "share who buy tea on a weekday" and swing_canteen["share who buy tea on a weekday"] == (1500, 3900))
for tid, v, shown, how in [
        ("toy_canteen_students", 3000, "3,000 students", "students on campus, the central guess"),
        ("toy_canteen_students_low", 2700, "2,700", "students, the low end"),
        ("toy_canteen_students_high", 3300, "3,300", "students, the high end"),
        ("toy_canteen_share", 0.45, "0.45 (45 percent)", "share who buy tea on a weekday, the central guess"),
        ("toy_canteen_share_low", 0.25, "0.25", "the share, the low end"),
        ("toy_canteen_share_high", 0.65, "0.65", "the share, the high end"),
        ("toy_canteen_cups_each", 2, "2 cups", "cups each buyer drinks, the central guess"),
        ("toy_canteen_cups_each_low", 1.5, "1.5", "cups each, the low end"),
        ("toy_canteen_cups_each_high", 2.5, "2.5", "cups each, the high end"),
        ("toy_canteen_buyers", 1350, "1,350 buyers", "3,000 x 0.45"),
        ("toy_canteen_cups", 2700, "2,700 cups", "3,000 x 0.45 x 2"),
        ("toy_canteen_till_mean", 2340, "2,340 cups", "the till's five weekdays, averaged"),
        ("toy_canteen_gap_pct", 15.4, "15.4 percent high", "2,700 / 2,340 - 1"),
        ("toy_canteen_implied_share", 0.39, "0.39", "the share that lands on the till: 2,340 / (3,000 x 2)"),
        ("toy_canteen_swing_students_low", 2430, "2,430", "2,700 x 0.45 x 2"),
        ("toy_canteen_swing_students_high", 2970, "2,970", "3,300 x 0.45 x 2"),
        ("toy_canteen_swing_share_low", 1500, "1,500", "3,000 x 0.25 x 2"),
        ("toy_canteen_swing_share_high", 3900, "3,900", "3,000 x 0.65 x 2"),
        ("toy_canteen_swing_cups_low", 2025, "2,025", "3,000 x 0.45 x 1.5"),
        ("toy_canteen_swing_cups_high", 3375, "3,375", "3,000 x 0.45 x 2.5"),
        ("toy_canteen_candidate_b", 2350, "2,350", "the near guess with no chain, in the prediction")]:
    toy(tid, v, shown, S4, how, "half2 SECTION 6; notebook 06; exercises ch6; notes; sheet")
for day, c in TILL:
    toy(f"toy_canteen_till_{day.lower()}", c, f"{c:,}", S4, f"cups the till counted on {day}",
        "data/C2_W04_D02_canteen_till_STUDENT.csv; notebook 06")

# The three sanity tests, each on its own small example.
sanity = pd.DataFrame([
    ("unit", "a town", "people", 24000, "people"),
    ("unit", "a town", "people to a household", 4, "people"),
    ("period", "a phone pack", "data a day", 1.5, "GB"),
    ("period", "a phone pack", "days in the pack", 28, "days"),
    ("period", "a phone pack", "days in a month", 30, "days"),
    ("definition", "Gulmohar Secondary School's board exam", "students enrolled", 150, "students"),
    ("definition", "Gulmohar Secondary School's board exam", "students who sat", 135, "students"),
    ("definition", "Gulmohar Secondary School's board exam", "students who passed", 113, "students"),
], columns=["test", "example", "quantity", "value", "unit"])
sanity.to_csv(DATA / f"{STEM}_sanity_tests_STUDENT.csv", index=False)
check("unit: 24,000 people make about 6,000 households; multiplying gives 96,000, 16 times too many",
      (24000 / 4, 24000 * 4, 24000 * 4 / (24000 / 4)) == (6000, 96000, 16))
check("period: 1.5 GB a day is 42 GB a pack and 45 GB a month, 1.5 a day either way",
      (1.5 * 28, 1.5 * 30) == (42, 45))
check("definition: 113 passes are 83.7 percent of 135 who sat and 75.3 percent of 150 enrolled",
      (round(113 / 135 * 100, 1), round(113 / 150 * 100, 1)) == (83.7, 75.3))
for tid, v, shown, how in [
        ("toy_town_people", 24000, "24,000 people", "a town's people"),
        ("toy_town_per_household", 4, "about 4 to a household", "people to a household, a round guess"),
        ("toy_town_households", 6000, "about 6,000 households", "24,000 / 4"),
        ("toy_town_wrong_households", 96000, "96,000 households", "24,000 x 4, the slip"),
        ("toy_town_wrong_ratio", 16, "16 times too many", "96,000 / 6,000"),
        ("toy_pack_gb_day", 1.5, "1.5 GB a day", "a phone pack's daily data"),
        ("toy_pack_days", 28, "28 days", "the pack's length"),
        ("toy_pack_gb_total", 42, "42 GB", "1.5 x 28"),
        ("toy_month_days", 30, "30 days", "a month as the bill counts it"),
        ("toy_month_gb_total", 45, "45 GB", "1.5 x 30"),
        ("toy_exam_enrolled", 150, "150 enrolled", "Gulmohar's class 10 students enrolled"),
        ("toy_exam_sat", 135, "135 sat", "the students who sat the board exam"),
        ("toy_exam_passed", 113, "113 passed", "the students who passed"),
        ("toy_exam_pass_sat_pct", 83.7, "83.7 percent", "113 / 135"),
        ("toy_exam_pass_enrolled_pct", 75.3, "75.3 percent", "113 / 150")]:
    toy(tid, v, shown, S4, how, "half2 SECTION 6; notebook 06; exercises ch6; notes; sheet")

# Ramesh's page, twice: the draft of number lines and the four sentences.
PAGE_A = [
    "- North star (sales a day): Rs 11,900 to Rs 12,600",
    "- Denominator: hours open, 10 to 12",
    "- Sales per hour index: 100 to 88",
    "- Customers a day: 119 to 126",
    "- Sales per customer: Rs 100 in both months",
    "- Rain days: 2 and 2",
    "- Festival days: none and 14",
    "- Helper's extra cost: Rs 170 a day",
    "- Guardrail: sales per customer held",
]
PAGE_B = [
    "Keep the longer hours for one more month and count the evening's own sales, because the two extra "
    "hours have brought Rs 700 a day while each hour of the day now earns less.",
    "Sales per hour fell from Rs 1,190 in September to Rs 1,050 in October, and sales per customer held "
    "at Rs 100.",
    "A festival fortnight fell inside October, so part of the extra Rs 700 a day may be the season.",
    "Keep the hours through November, write the evening's sales in a separate column each day, and decide "
    "after thirty days; the helper's two extra hours cost Rs 170 a day, and Ramesh signs.",
]
(DATA / f"{STEM}_kirana_page_STUDENT.txt").write_text(
    "VERSION A: THE DRAFT\n" + "\n".join(PAGE_A) + "\n=====\nVERSION B: THE PAGE\n" + "\n".join(PAGE_B) + "\n",
    encoding="utf-8")
METHOD_WORDS = ["denominator", "numerator", "index", "guardrail", "north star"]
words_b = sum(len(s.split()) for s in PAGE_B)
check("the page: four sentences, no method word, under the pack's 250-word ceiling",
      len(PAGE_B) == 4 and words_b <= 250
      and not any(w in " ".join(PAGE_B).lower() for w in METHOD_WORDS))
check("the draft prints 13 numbers and the page 6", (len(re.findall(r"\d[\d,.]*", "\n".join(PAGE_A))),
      len(re.findall(r"\d[\d,.]*", "\n".join(PAGE_B)))) == (13, 6))
check("the draft: nine lines and four method words",
      len(PAGE_A) == 9 and sum(w in " ".join(PAGE_A).lower() for w in METHOD_WORDS) == 4)
for tid, v, shown, how in [
        ("toy_page_sentences", 4, "four sentences", "the page's sentences: claim, evidence, caveat, action"),
        ("toy_page_draft_lines", 9, "nine lines", "the draft's lines of numbers"),
        ("toy_page_draft_method_words", 4, "four method words", "north star, denominator, index, guardrail"),
        ("toy_page_words", words_b, f"{words_b} words", "words on the four-sentence page"),
        ("toy_page_draft_numbers", 13, "13 numbers", "numbers printed on the draft's nine lines"),
        ("toy_page_numbers", 6, "6 numbers", "numbers printed on the page's four sentences"),
        ("toy_page_ceiling", 250, "250 words", "the pack's own ceiling for Ramesh's page, asserted by this "
         "script; since the 13 October fix pass no learner file states it, and the page's five rules carry no word "
         "count")]:
    toy(tid, v, shown, S5, how, "half2 SECTION 7; notebook 07; exercises ch7; notes")

# For notebook 05 (a case notebook): the drivers by segment, each a Monday id already in this file.
segments = pd.DataFrame([
    ("the idle tail", "before", 180, M["idle_hours_before"], M["idle_trips_before"]),
    ("the idle tail", "after", 180, M["idle_hours_after"], M["idle_trips_after"]),
    ("the other drivers there before the launch", "before", 880, M["others_hours_before"], M["others_trips_before"]),
    ("the other drivers there before the launch", "after", 880, M["others_hours_after"], M["others_trips_after"]),
    ("the 140 joiners", "after", 140, join_a["hours"], join_a["trips"]),
], columns=["segment", "window", "drivers", "peak_online_hours", "peak_trips"])
segments.to_csv(DATA / f"{STEM}_driver_segments_STUDENT.csv", index=False)
seg_tot = segments.groupby("window")[["peak_online_hours", "peak_trips"]].sum()
check("the segments add up to the city: 118,000 and 146,300 hours, 224,200 and 230,900 trips",
      (seg_tot.loc["before"].tolist(), seg_tot.loc["after"].tolist())
      == ([M["hours_before"], M["trips_before"]], [M["hours_after"], M["trips_after"]]))
check("the segments' drivers add up to 1,060 before and 1,200 after",
      segments[segments.window == "before"].drivers.sum() == M["drivers_pre_launch"]
      and segments[segments.window == "after"].drivers.sum() == M["drivers_total"])
add("joiner_tph_after", round(join_a["trips"] / join_a["hours"], 2), "1.59",
    "3,660 / 2,300: the 140 joiners' trips per online hour after the launch", "notebook 05; notes")
add("idle_tail_hours_share_after", round(M["idle_hours_after"] / M["hours_after"] * 100), "29 percent",
    "42,000 / 146,300: the idle tail's share of the city's peak online hours after the launch", "notebook 05")

# ------------------------------------------------------------------ twelve rows into the facts
for _, r in twelve.iterrows():
    rec = {k: (int(v) if isinstance(v, (int,)) or str(v).isdigit() else v) for k, v in r.items()}
    rec["rs_per_hour"] = round(int(r["peak_bookings_rs"]) / int(r["peak_online_hours"]), 1)
    facts["twelve_rows"].append(rec)
check("E and F, the idle-tail pair, have the two lowest after-week rupees per hour on the twelve rows",
      sorted(r["driver"] for r in facts["twelve_rows"] if r["window"] == "after"
             and r["rs_per_hour"] < 100) == ["E", "F"])

# ------------------------------------------------------------------ the room, for the studio
facts["programme"] = {"cohort_students": 35, "threes": 11, "pairs": 1,
                      "source": "data/programme/facts.yaml, cohort.students; 35 = 11 threes and one pair"}
check("35 learners make eleven threes and one pair", 11 * 3 + 2 == 35)

# ------------------------------------------------------------------ the three cluttered slides
def ids(*pairs):
    return [{"label": a, "shows": b, "facts_ids": c} for a, b, c in pairs]


facts["cluttered_slides"] = {
    "A_dashboard": ids(
        ("Peak online hours", "+24 percent", "hours_change_pct"),
        ("Completed peak trips", "+3 percent", "trips_change_pct"),
        ("Trips per peak online hour", "1.90 to 1.58", "tph_before, tph_after"),
        ("Acceptance share", "86% to 73%", "acceptance_before, acceptance_after"),
        ("Online hours with no trip", "22% to 38%", "no_trip_share_before, no_trip_share_after"),
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
        ("Rider requests", "251,910 to 256,556", "requests_before, requests_after")),
    "C_driver_ops": ids(
        ("Drivers", "1,060 to 1,200 (140 new)", "drivers_pre_launch, drivers_total, drivers_new"),
        ("Active driver-weeks", "6,360 to 6,500", "driver_weeks_before, driver_weeks_after"),
        ("Offers shown to drivers", "269,773 to 347,583", "offers_before, offers_after"),
        ("Acceptance share", "86% to 73%", "acceptance_before, acceptance_after"),
        ("Driver cancels after accepting", "4% to 9%",
         "driver_cancel_share_before, driver_cancel_share_after"),
        ("Drivers in the idle tail", "180", "idle_tail_drivers"),
        ("Idle-tail online hours", "20,000 to 42,000", "idle_hours_before, idle_hours_after"),
        ("Idle-tail trips", "38,000 to 33,440", "idle_trips_before, idle_trips_after"),
        ("Unfulfilled requests", "11% to 10%", "unfulfilled_share_before, unfulfilled_share_after")),
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
        "share_of_dmart_store": round(20000 * 2 * 12 * 1500 / (per_store_avg * 1e7), 2),
        "check_against": "DMart's revenue per store on the average of the opening and closing counts, "
                         "about Rs 146 crore, the count that was open across the year",
    },
}
ex = facts["kalpa"]["store_worked_example"]
ex["sign_ups_range_by_factor"] = {
    "households": [round(30000 * 0.4 * 0.05), round(80000 * 0.4 * 0.05)],
    "share_who_shop": [round(50000 * 0.25 * 0.05), round(50000 * 0.5 * 0.05)],
    "sign_up_share": [round(50000 * 0.4 * 0.02), round(50000 * 0.4 * 0.08)],
}
check("the sign-up share sets the Kalpa range: 400 to 1,600, wider than 600 to 1,600 and 625 to 1,250",
      ex["sign_ups_range_by_factor"] == {"households": [600, 1600], "share_who_shop": [625, 1250],
                                         "sign_up_share": [400, 1600]})
check("Kalpa worked store: 1,000 sign-ups, Rs 72 crore, about half a mature DMart store",
      ex["sign_ups_year_one"] == 50000 * 0.4 * 0.05 and ex["first_year_sales_rs"] == 720_000_000
      and ex["share_of_dmart_store"] == 0.49)
check("Kalpa v4 totals match the client-zero generator's constants",
      facts["kalpa"]["v4"]["q1_rs"] == 100_000_000 and facts["kalpa"]["v4"]["customers"] == 340)

# ------------------------------------------------------------------ the case tables, unchanged
# The concept-first rebuild of 13 October 2026 added the concept chapters' examples and moved no
# case number, so every case table written above must match the merged pack's byte for byte.
for name in ("twelve_rows", "twelve_weeks", "kalpa_dmart_anchor", "driver_groups"):
    rel_path = f"content/W04/D2/data/{STEM}_{name}_STUDENT.csv"
    try:
        merged = subprocess.run(["git", "show", f"origin/main:{rel_path}"], capture_output=True,
                                check=True, cwd=DAY.parent.parent.parent).stdout
    except (OSError, subprocess.CalledProcessError):
        print(f"SKIP  {rel_path}: origin/main cannot be read here, so the byte check did not run")
        continue
    check(f"{name} is byte-identical to origin/main's copy",
          (DATA / f"{STEM}_{name}_STUDENT.csv").read_bytes() == merged)

# ------------------------------------------------------------------ write and re-read
out = HERE / f"{STEM}_facts_INTERNAL.yaml"
out.write_text(yaml.safe_dump(facts, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")
back = yaml.safe_load(out.read_text(encoding="utf-8"))
check("facts file re-reads with every block", all(k in back for k in (
    "numbers", "monday_ids_reused", "public_facts", "assumptions", "toys", "toy_numbers", "twelve_rows",
    "weekly_series", "cluttered_slides", "kalpa")))
check("every Tuesday id is unique", len({n["id"] for n in back["numbers"]}) == len(back["numbers"]))
check("every toy id is unique and starts toy_", len({n["id"] for n in back["toy_numbers"]})
      == len(back["toy_numbers"]) and all(n["id"].startswith("toy_") for n in back["toy_numbers"]))
check("every toy number says which concept chapter it was invented for", all(
    n["how"].startswith("invented for the concept chapter on ") and n["used_by"] for n in back["toy_numbers"]))
print(f"\nwrote {out.relative_to(DAY.parent.parent.parent)}: {len(back['numbers'])} numbers, "
      f"{len(back['monday_ids_reused'])} Monday ids, {len(back['public_facts'])} public facts, "
      f"{len(back['assumptions'])} assumptions, {len(back['toy_numbers'])} toy numbers")

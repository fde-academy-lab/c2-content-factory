"""Week 4 Tuesday: Uber Hyderabad, one day on. Case data generator and facts file.

Tuesday is the slide day: the same six-week case as Monday, now read as rupees per online
hour, per driver-week and per trip. The generator does not re-shape the case data. It
reads Monday's three tables from ``content/W04/D1/data/``, builds Tuesday's two small
tables (the twelve rows the room will read three ways, and the twelve-week series with
the three denominators), writes Tuesday's facts file with every number a learner will see
in a STUDENT file, and asserts every target the Tuesday section of
``docs/detailing/W04_case_file.md`` prints. A failed assertion exits 1.

Reads from Monday:
    content/W04/D1/data/C2_W04_D01_driver_weeks_STUDENT.csv
    content/W04/D1/data/C2_W04_D01_drivers_STUDENT.csv

Writes to Tuesday:
    content/W04/D2/data/C2_W04_D02_twelve_rows_STUDENT.csv
    content/W04/D2/data/C2_W04_D02_three_denominators_STUDENT.csv
    content/W04/D2/data/C2_W04_D02_kalpa_dmart_anchor_STUDENT.csv
    content/W04/D2/internal/C2_W04_D02_facts_INTERNAL.yaml

Standard library and pandas only. Seeded, so two runs write byte-identical files.

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
DATA.mkdir(parents=True, exist_ok=True)
MON_DATA = DAY.parent / "D1" / "data"
MON_INTERNAL = DAY.parent / "D1" / "internal"
STEM = "C2_W04_D02"

LAUNCH = dt.date(2026, 8, 31)
TWELVE_BEFORE = dt.date(2026, 8, 10)
TWELVE_AFTER = dt.date(2026, 9, 21)
FARE_RS = 165


def passed(line):
    print(f"PASS  {line}")


def check(line, ok):
    if not ok:
        print(f"FAIL  {line}", file=sys.stderr)
        sys.exit(1)
    passed(line)


# -------------------------------------------------------------------- read Monday's tables
dw = pd.read_csv(MON_DATA / "C2_W04_D01_driver_weeks_STUDENT.csv")
drivers = pd.read_csv(MON_DATA / "C2_W04_D01_drivers_STUDENT.csv")
mon_facts = yaml.safe_load((MON_INTERNAL / "C2_W04_D01_facts_INTERNAL.yaml").read_text())
mon_by_id = {n["id"]: n["value"] for n in mon_facts["numbers"]}

dw["week"] = pd.to_datetime(dw["week_start"]).dt.date
dw["window"] = dw["week"].apply(lambda d: "before" if d < LAUNCH else "after")

check("Monday has 12 weeks",   dw["week"].nunique() == 12)
check("Monday has 12,860 driver-week rows",   len(dw) == 12860)
check("Monday hours before == 118,000",  int(dw[dw.window == "before"]["peak_online_hours"].sum()) == 118000)
check("Monday hours after == 146,300",   int(dw[dw.window == "after"]["peak_online_hours"].sum()) == 146300)

# ---------------------------------------------------------------- the twelve case rows
TWELVE = [("d_0001", "A"), ("d_0002", "B"), ("d_0003", "C"),
          ("d_0004", "D"), ("d_0881", "E"), ("d_0882", "F")]
TWELVE_IDS = [d for d, _ in TWELVE]
LETTER = dict(TWELVE)
WEEKS = {str(TWELVE_BEFORE): "before", str(TWELVE_AFTER): "after"}

twelve = dw[dw.driver_id.isin(TWELVE_IDS) & dw.week_start.isin(WEEKS)].copy()
twelve["driver"] = twelve.driver_id.map(LETTER)
twelve["window"] = twelve.week_start.map(WEEKS)
twelve = twelve.sort_values(["driver", "window"], ascending=[True, False]).reset_index(drop=True)

twelve_out = twelve[["driver", "driver_id", "zone_mode", "window", "week_start",
                     "peak_online_hours", "peak_offers", "peak_accepted",
                     "peak_driver_cancels", "peak_trips", "peak_hours_no_trip",
                     "peak_bookings_rs", "topup_rs"]].rename(columns={"zone_mode": "zone"})
twelve_out.to_csv(DATA / f"{STEM}_twelve_rows_STUDENT.csv", index=False)
check(f"wrote twelve rows: {len(twelve_out)} == 12", len(twelve_out) == 12)

# ---------- three denominators on the twelve rows (per online hour, per driver-week, per trip)
def three_den(subset):
    hours = int(subset.peak_online_hours.sum())
    trips = int(subset.peak_trips.sum())
    booking = int(subset.peak_bookings_rs.sum())
    rows = len(subset)
    return {
        "hours": hours,
        "trips": trips,
        "driver_weeks": rows,
        "bookings_rs": booking,
        "rs_per_hour": round(booking / hours, 2),
        "rs_per_driver_week": round(booking / rows, 2),
        "rs_per_trip": round(booking / trips, 2),
    }


twelve_before = three_den(twelve_out[twelve_out.window == "before"])
twelve_after = three_den(twelve_out[twelve_out.window == "after"])

check("twelve rows hours before 60",     twelve_before["hours"] == 60)
check("twelve rows trips before 114",    twelve_before["trips"] == 114)
check("twelve rows bookings before 18,810", twelve_before["bookings_rs"] == 18810)
check("twelve rows Rs/hour before 313.50",  twelve_before["rs_per_hour"] == 313.50)
check("twelve rows Rs/driver-week before 3,135", twelve_before["rs_per_driver_week"] == 3135.00)
check("twelve rows Rs/trip before 165",     twelve_before["rs_per_trip"] == 165.00)

check("twelve rows hours after 74",      twelve_after["hours"] == 74)
check("twelve rows trips after 88",      twelve_after["trips"] == 88)
check("twelve rows bookings after 14,520",   twelve_after["bookings_rs"] == 14520)
check("twelve rows Rs/hour after 196.22",    twelve_after["rs_per_hour"] == 196.22)
check("twelve rows Rs/driver-week after 2,420", twelve_after["rs_per_driver_week"] == 2420.00)
check("twelve rows Rs/trip after 165",       twelve_after["rs_per_trip"] == 165.00)

# ------------------------- the three denominators on the full data (per window)
full_before = three_den(dw[dw.window == "before"])
full_after = three_den(dw[dw.window == "after"])

check("full before Rs/hour 313.50 (Monday's)", abs(full_before["rs_per_hour"] - 313.50) < 0.02)
check("full after Rs/hour 260.4 (Monday's)",   abs(full_after["rs_per_hour"] - 260.4) < 0.1)
check("full before Rs/driver-week 5,816.5",     abs(full_before["rs_per_driver_week"] - 5816.5) < 1)
check("full after Rs/driver-week 5,861.3",      abs(full_after["rs_per_driver_week"] - 5861.3) < 1)
check("full Rs/trip before 165",                full_before["rs_per_trip"] == 165.00)
check("full Rs/trip after 165",                 full_after["rs_per_trip"] == 165.00)

# ----------------------------------------- the twelve-week series with three denominators
weekly = dw.groupby("week_start").agg(
    hours=("peak_online_hours", "sum"),
    trips=("peak_trips", "sum"),
    bookings_rs=("peak_bookings_rs", "sum"),
    driver_weeks=("peak_online_hours", "count"),
).reset_index().sort_values("week_start")
weekly["rs_per_hour"] = (weekly.bookings_rs / weekly.hours).round(2)
weekly["rs_per_driver_week"] = (weekly.bookings_rs / weekly.driver_weeks).round(2)
weekly["rs_per_trip"] = (weekly.bookings_rs / weekly.trips).round(2)
weekly["window"] = weekly.week_start.apply(
    lambda s: "before" if dt.date.fromisoformat(s) < LAUNCH else "after")
weekly.to_csv(DATA / f"{STEM}_three_denominators_STUDENT.csv", index=False)
check(f"wrote twelve-week series: {len(weekly)} == 12", len(weekly) == 12)

# ---------------------------------- the Kalpa DMart anchor (one tiny table for the lab)
DMART = pd.DataFrame([
    {"item": "FY26 standalone revenue, Rs crore", "value": 66968,
     "note": "D-Mart Supermarts, FY 2025-26 standalone, press release 2 May 2026"},
    {"item": "Stores at FY26 end",            "value": 500,
     "note": "500 stores at FY26 end, 85 added during the year"},
    {"item": "Stores at FY25 end",            "value": 415,
     "note": "500 less the 85 added"},
    {"item": "Rs per store, year-end count",  "value": round(66968 / 500, 1),
     "note": "66,968 crore divided by 500"},
    {"item": "Rs per store, average count",   "value": round(66968 / ((500 + 415) / 2), 1),
     "note": "66,968 crore divided by the average of 500 and 415"},
])
DMART.to_csv(DATA / f"{STEM}_kalpa_dmart_anchor_STUDENT.csv", index=False)
check("wrote DMart anchor: 5 rows", len(DMART) == 5)
check("DMart revenue per store, year-end, Rs 133.9 crore",
      abs(DMART.loc[DMART["item"] == "Rs per store, year-end count", "value"].iloc[0] - 133.9) < 0.5)

# ------------------------------------------------------------------ Tuesday's facts file
# Keep every number Tuesday prints under an id. Monday's values enter under Monday's ids so
# the Tuesday generator never recomputes them another way.
facts = {
    "day": "W04/D2, Tuesday 27 October 2026",
    "written_by": f"{STEM}_make_data_INTERNAL.py; the W04 D2 drafting session, 12 October 2026",
    "source_tables": {
        "monday_driver_weeks": "../D1/data/C2_W04_D01_driver_weeks_STUDENT.csv",
        "monday_drivers": "../D1/data/C2_W04_D01_drivers_STUDENT.csv",
        "monday_facts": "../D1/internal/C2_W04_D01_facts_INTERNAL.yaml",
        "twelve_rows": f"data/{STEM}_twelve_rows_STUDENT.csv",
        "three_denominators": f"data/{STEM}_three_denominators_STUDENT.csv",
        "kalpa_dmart_anchor": f"data/{STEM}_kalpa_dmart_anchor_STUDENT.csv",
    },
    "numbers": [],
    "monday_ids_reused": [],
    "toys": [],
    "twelve_rows": [],
    "weekly_series": [],
    "kalpa": {},
    "shared_constants": {
        "fare_rs": 165,
        "launch_date": "2026-08-31",
        "window_before": "2026-07-20 to 2026-08-30",
        "window_after": "2026-08-31 to 2026-10-11",
        "diwali_2026": "2026-11-08",
    },
}


def add(nid, value, unit, how, used_by):
    facts["numbers"].append({"id": nid, "value": value, "unit": unit, "how": how,
                             "used_by": used_by})


# ----- Monday ids reused on Tuesday (every one copied by value from Monday's facts file)
MONDAY_REUSED = [
    "launch_date", "window_before", "window_after", "floor_rs_per_hour",
    "fare_avg_rs", "drivers_total", "drivers_new",
    "hours_before", "trips_before", "tph_before", "acceptance_before",
    "no_trip_share_before", "bookings_before_rs", "rs_per_hour_before",
    "driver_weeks_before", "online_driver_weeks_before", "rs_per_driver_week_before",
    "hours_after", "trips_after", "tph_after", "acceptance_after",
    "no_trip_share_after", "bookings_after_rs", "rs_per_hour_after",
    "driver_weeks_after", "online_driver_weeks_after", "rs_per_driver_week_after",
    "hours_change_pct", "trips_change_pct", "topup_after_rs",
    "topup_low_acceptance_rs", "topup_low_acceptance_share",
    "idle_tail_drivers", "idle_hours_before", "idle_hours_after",
    "idle_trips_before", "idle_trips_after",
    "median_wait_before", "median_wait_after",
    "requests_before", "requests_after",
]
for mid in MONDAY_REUSED:
    v = mon_by_id[mid]
    facts["monday_ids_reused"].append({"id": mid, "value": v,
                                       "source": "D1 facts file"})
# Sanity: Monday ids remain unchanged on this run
check("Monday Rs/hour before 313.5 unchanged", mon_by_id["rs_per_hour_before"] == 313.5)
check("Monday Rs/hour after 260.4 unchanged",  mon_by_id["rs_per_hour_after"] == 260.4)
check("Monday Rs/driver-week before 5,816.5 unchanged", mon_by_id["rs_per_driver_week_before"] == 5816.5)
check("Monday Rs/driver-week after 5,861.3 unchanged", mon_by_id["rs_per_driver_week_after"] == 5861.3)

# ----- Tuesday's own ids (the twelve rows read three ways; derivations the slide names)
add("twelve_hours_before", 60, "hours",
    "sum of the six before rows", "L1 hand count; cheat sheet panel 2")
add("twelve_hours_after", 74, "hours",
    "sum of the six after rows", "L1 hand count; cheat sheet panel 2")
add("twelve_trips_before", 114, "trips",
    "sum of the six before rows", "L1 hand count")
add("twelve_trips_after", 88, "trips",
    "sum of the six after rows", "L1 hand count")
add("twelve_bookings_before_rs", 18810, "Rs",
    "sum of peak_bookings_rs for the six before rows (165 Rs/trip x 114 trips)",
    "L1, L2 hand count")
add("twelve_bookings_after_rs", 14520, "Rs",
    "sum of peak_bookings_rs for the six after rows (165 Rs/trip x 88 trips)",
    "L1, L2 hand count")
add("twelve_rs_per_hour_before", 313.5, "Rs per peak online hour",
    "18,810 / 60", "L1 three denominators; half1 chapter 1; notebook 01")
add("twelve_rs_per_hour_after", 196.2, "Rs per peak online hour",
    "14,520 / 74", "L1 three denominators; half1 chapter 1; notebook 01")
add("twelve_rs_per_driver_week_before", 3135, "Rs per driver-week",
    "18,810 / 6", "L1 three denominators; half1 chapter 1; notebook 01")
add("twelve_rs_per_driver_week_after", 2420, "Rs per driver-week",
    "14,520 / 6", "L1 three denominators; half1 chapter 1; notebook 01")
add("twelve_rs_per_trip_before", 165, "Rs per trip",
    "18,810 / 114", "L1 three denominators; half1 chapter 1; notebook 01")
add("twelve_rs_per_trip_after", 165, "Rs per trip",
    "14,520 / 88", "L1 three denominators; half1 chapter 1; notebook 01")
add("twelve_rs_per_hour_change_pct", -37.4, "percent",
    "196.2 / 313.5 - 1", "L1, half1 chapter 1")
add("twelve_rs_per_driver_week_change_pct", -22.8, "percent",
    "2420 / 3135 - 1", "L1, half1 chapter 1")
add("twelve_rs_per_trip_change_pct", 0, "percent",
    "165 / 165 - 1", "L1, half1 chapter 1")

# ----- the full-data three denominators (Tuesday computes each from Monday's tables)
add("full_rs_per_hour_before", round(full_before["rs_per_hour"], 1), "Rs per peak online hour",
    "sum of peak_bookings_rs / sum of peak_online_hours over all before rows",
    "L2 three denominators; half1 chapter 2; notebook 01")
add("full_rs_per_hour_after",  round(full_after["rs_per_hour"], 1), "Rs per peak online hour",
    "sum of peak_bookings_rs / sum of peak_online_hours over all after rows",
    "L2 three denominators; half1 chapter 2; notebook 01")
add("full_rs_per_driver_week_before", round(full_before["rs_per_driver_week"], 0),
    "Rs per driver-week",
    "sum of peak_bookings_rs / count of driver-weeks over all before rows",
    "L2 three denominators; half1 chapter 2; notebook 01")
add("full_rs_per_driver_week_after", round(full_after["rs_per_driver_week"], 0),
    "Rs per driver-week",
    "sum of peak_bookings_rs / count of driver-weeks over all after rows",
    "L2 three denominators; half1 chapter 2; notebook 01")
add("full_rs_per_trip_before", 165, "Rs per trip",
    "sum of peak_bookings_rs / sum of peak_trips over all before rows",
    "L2 three denominators; half1 chapter 2; notebook 01")
add("full_rs_per_trip_after", 165, "Rs per trip",
    "sum of peak_bookings_rs / sum of peak_trips over all after rows",
    "L2 three denominators; half1 chapter 2; notebook 01")
add("full_rs_per_hour_change_pct", -17.1, "percent",
    "260.4 / 313.5 - 1", "L2; half1 chapter 2")
add("full_rs_per_driver_week_change_pct", 0.8, "percent",
    "5861.3 / 5816.5 - 1", "L2; half1 chapter 2")

# ----- the drivers-at-peak guesstimate factors (worked together; labelled assumptions)
# Hyderabad has about 50 to 70 lakh adults; the city head's own evening peak draws many thousands
# of ride requests an hour, with every assumption said aloud so a learner can challenge it.
add("peak_window_minutes", 180, "minutes",
    "three hours of evening peak", "L5 guesstimate map; dojo")
add("hyd_peak_requests_per_hour_low",  8000,  "requests per hour (assumption, range 7,000 to 12,000)",
    "clarifying assumption said aloud, lower bound",
    "L5 guesstimate map; dojo")
add("hyd_peak_requests_per_hour_mid",  10000, "requests per hour (assumption)",
    "clarifying assumption said aloud, central value",
    "L5 guesstimate map; dojo")
add("trips_per_driver_per_peak_hour",  2,     "trips per hour (assumption)",
    "a driver completes about two peak trips an hour, from the case's 1.6 to 1.9",
    "L5 guesstimate map; dojo")
add("idle_share_assumption", 0.30, "share (assumption, range 0.20 to 0.40)",
    "share of online drivers idle at any moment of peak; the number that moves the answer most",
    "L5 guesstimate map; dojo")
add("buffer_for_wait", 1.15, "multiplier (assumption)",
    "15 percent buffer above drivers needed, so median wait sits under five minutes",
    "L5 guesstimate map; dojo")
# Product, said aloud: 10,000 requests/hour / 2 trips/driver/hour = 5,000 driver-hours of demand;
# with 30 percent idle, divide by 0.70 and multiply by 1.15 for the wait buffer.
# 5,000 / 0.70 x 1.15 ~= 8,214 drivers at any moment of peak.
add("guesstimate_drivers_online_peak", 8200, "drivers (central value)",
    "10,000 requests/hour divided by 2 trips/driver/hour, divided by 0.70, times 1.15; "
    "rounded to two significant figures",
    "L5 guesstimate; dojo; cheat sheet panel 2")
add("guesstimate_drivers_online_peak_range_low",  5000, "drivers (range low)",
    "7,000 requests/hour, 20 percent idle, same buffer",
    "L5 guesstimate; dojo")
add("guesstimate_drivers_online_peak_range_high", 11500, "drivers (range high)",
    "12,000 requests/hour, 40 percent idle, same buffer",
    "L5 guesstimate; dojo")
add("hyd_published_drivers_online_peak", None, "drivers (not verified)",
    "no published figure in the research ledger; the finishing session may fetch and date a "
    "primary source",
    "L5 validate; dojo (slot reads 'to be found')")

# ----- the paired guesstimate: UPI transactions a day, validated against NPCI
add("upi_active_users_assumption", 350000000, "users (assumption)",
    "about 35 crore active UPI users, said aloud",
    "L5 paired guesstimate; dojo")
add("upi_payments_per_user_per_day", 2.3, "payments per day (assumption)",
    "about 2 to 3 payments a day per active user, said aloud",
    "L5 paired guesstimate; dojo")
add("upi_guesstimate_per_day", 805000000, "transactions per day",
    "35 crore users x 2.3 payments; rounded to the nearest 5 million",
    "L5 paired guesstimate; dojo")
add("upi_published_per_day", 802000000, "transactions per day",
    "NPCI through Outlook Money, September 2026 average (R2 T3)",
    "L5 paired guesstimate; dojo")
add("upi_published_month_total", 24070000000, "transactions in September 2026",
    "NPCI through Outlook Money, September 2026 total (R2 T3)",
    "L5 paired guesstimate; dojo")
add("thirty_vs_thirty_one_days", 30, "days",
    "a 30-day month against a 31-day month moves the monthly total",
    "L5 paired guesstimate catch")

# ----- the slide trap: nine Monday numbers rebuilt to one claim
add("slide_elements_cluttered", 9, "elements",
    "a cluttered slide of nine Monday numbers rebuilt live",
    "L1, L4 declutter")
add("slide_elements_cut_to", 2, "elements",
    "nine numbers cut to two: the claim's own evidence and its denominator",
    "L1, L4 declutter")

# ----- the memo-against-slide (Amazon's 2017 letter)
add("amazon_memo_pages", 6, "pages",
    "Amazon's six-page memo read in silence (letter to shareholders 2017, R2 T1)",
    "L3 the defence shape")

# ----- the Kalpa DMart anchor numbers used in the lab
add("dmart_fy26_revenue_rs_crore", 66968, "Rs crore",
    "D-Mart Supermarts FY 2025-26 standalone revenue (press release 2 May 2026, R2 T3)",
    "lab Kalpa guesstimate anchor")
add("dmart_stores_fy26_end", 500, "stores",
    "500 stores at FY26 end, 85 added during the year (R2 T3)",
    "lab Kalpa guesstimate anchor")
add("dmart_stores_fy25_end", 415, "stores",
    "500 at FY26 end less the 85 added during FY26",
    "lab Kalpa guesstimate anchor")
add("dmart_revenue_per_store_year_end", 133.9, "Rs crore",
    "66,968 / 500; our arithmetic",
    "lab Kalpa guesstimate anchor; cheat sheet panel 2")
add("dmart_revenue_per_store_average", 146.4, "Rs crore",
    "66,968 / ((500 + 415) / 2); our arithmetic",
    "lab Kalpa guesstimate anchor")

# ----- the toy: a hostel notice board, a canteen's cups of tea
facts["toys"].append({
    "id": "toy_notice_board",
    "label": "invented",
    "values": {"headline_topic": "Breakfast survey results",
               "headline_claim": "Rotis replace rice at Monday breakfast; the kitchen moves "
                                 "two staff from the rice counter to the roti line"},
    "used_by": "L1 the title is the claim",
})
facts["toys"].append({
    "id": "toy_canteen_tea",
    "label": "invented",
    "values": {"students": 2000, "share_who_buy_tea": 0.6,
               "cups_per_person_per_day": 2.0, "cups_per_day": 2400},
    "used_by": "L5 the dojo's warm-up",
})
facts["toys"].append({
    "id": "toy_hyd_crowd",
    "label": "invented",
    "values": {"wrong_households": 9000000, "right_households": 500000,
               "note": "a city of two million people cannot have nine million households"},
    "used_by": "L5 the Kahoot trap",
})

# ----- the twelve rows in the facts file (the room reads these three ways)
for _, row in twelve_out.iterrows():
    facts["twelve_rows"].append({
        "driver": row["driver"], "driver_id": row["driver_id"],
        "zone": row["zone"], "window": row["window"], "week_start": row["week_start"],
        "peak_online_hours": int(row["peak_online_hours"]),
        "peak_offers": int(row["peak_offers"]),
        "peak_accepted": int(row["peak_accepted"]),
        "peak_driver_cancels": int(row["peak_driver_cancels"]),
        "peak_trips": int(row["peak_trips"]),
        "peak_hours_no_trip": int(row["peak_hours_no_trip"]),
        "peak_bookings_rs": int(row["peak_bookings_rs"]),
        "topup_rs": int(row["topup_rs"]),
    })

# ----- the twelve-week series Tuesday draws three times
for _, row in weekly.iterrows():
    facts["weekly_series"].append({
        "week_start": row["week_start"],
        "window": row["window"],
        "hours": int(row["hours"]),
        "trips": int(row["trips"]),
        "driver_weeks": int(row["driver_weeks"]),
        "bookings_rs": int(row["bookings_rs"]),
        "rs_per_hour": float(row["rs_per_hour"]),
        "rs_per_driver_week": float(row["rs_per_driver_week"]),
        "rs_per_trip": float(row["rs_per_trip"]),
    })

# ----- Kalpa for the lab: only what the lab reuses (Monday's north-star slide practice,
#       plus the DMart anchor the second ask reads against). The row says 'no plant today'.
facts["kalpa"] = {
    "lab_shape": "every learner presents Monday's Kalpa north star (delivered orders per "
                 "active customer per month) on one slide to a TA, three minutes, scored on "
                 "the four moves; then Anand's new-store question, mapped and validated "
                 "against DMart (R2 T3), with the catch that a first-year store sells less",
    "no_plant_today": True,
    "dmart_anchor_file": f"data/{STEM}_kalpa_dmart_anchor_STUDENT.csv",
}

# ------------------------------------------------------------------- write facts, assert
facts_path = HERE / f"{STEM}_facts_INTERNAL.yaml"
facts_path.write_text(yaml.safe_dump(facts, sort_keys=False, allow_unicode=True, width=100),
                      encoding="utf-8")
check(f"wrote facts: {facts_path.name}", facts_path.exists())
check("facts has >= 40 numbers", len(facts["numbers"]) >= 40)
check("twelve rows in facts == 12", len(facts["twelve_rows"]) == 12)
check("weekly series in facts == 12", len(facts["weekly_series"]) == 12)
check("Monday ids reused >= 30", len(facts["monday_ids_reused"]) >= 30)

# ----- one last cross-check: the facts file's twelve-row totals match the CSV it wrote
tw = pd.read_csv(DATA / f"{STEM}_twelve_rows_STUDENT.csv")
check("twelve rows CSV before hours 60",
      int(tw[tw.window == "before"]["peak_online_hours"].sum()) == 60)
check("twelve rows CSV after hours 74",
      int(tw[tw.window == "after"]["peak_online_hours"].sum()) == 74)
check("twelve rows CSV before trips 114",
      int(tw[tw.window == "before"]["peak_trips"].sum()) == 114)
check("twelve rows CSV after trips 88",
      int(tw[tw.window == "after"]["peak_trips"].sum()) == 88)

print()
print(f"wrote: {DATA / f'{STEM}_twelve_rows_STUDENT.csv'}")
print(f"wrote: {DATA / f'{STEM}_three_denominators_STUDENT.csv'}")
print(f"wrote: {DATA / f'{STEM}_kalpa_dmart_anchor_STUDENT.csv'}")
print(f"wrote: {facts_path}")
print(f"facts numbers: {len(facts['numbers'])}")

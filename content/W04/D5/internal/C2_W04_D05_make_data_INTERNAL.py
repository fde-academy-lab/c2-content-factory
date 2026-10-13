"""Build the Friday case data for Week 4 Day 5: Flipkart's Lucknow fulfilment centre, and Kalpa.

Writes the case tables and the Kalpa transfer tables to content/W04/D5/data/, writes
content/W04/D5/internal/C2_W04_D05_facts_INTERNAL.yaml with every number a learner sees, and
asserts the case file's targets the data can honestly hold. Deterministic: fixed seeds, no clock,
so two runs write byte-identical files.

    python3 content/W04/D5/internal/C2_W04_D05_make_data_INTERNAL.py

How every forecast is made, so no number a method is scored on was ever seen by that method:

  The hold-out is the last thirteen weeks, 29 June to 21 September 2026, forecast from one origin,
  the week of 22 June 2026, the way a planner would have made them that week. Naive repeats the
  origin week; drift draws the line from the first week through the origin week; the house bot
  (same week last year) copies the week 52 weeks back; finance's rule is the bot plus 4 percent;
  the festival-aligned baseline copies the week at the same distance from last year's Diwali for
  the weeks from five before Diwali to four after, the same calendar week otherwise, plus the
  4 percent a year the history grew. The vendor's hold-out rows are its forecast from the same
  origin, so the hold-out scores a forecast and never a fit.

  The 2025 festive back-test forecasts 29 September to 17 November 2025 from the week of
  22 September 2025 by the same three rules, the only festival the data can test them on.

  The 2026 festive window, 12 October to 30 November 2026, is forecast from all 104 weeks and
  set against both 2025 windows: the same calendar weeks (13 October to 1 December 2025) and the
  same weeks counted from Diwali (29 September to 17 November 2025).

Kalpa: monthly revenue October 2024 to September 2026, with April to September 2026 equal to the
monthly sums of v4's orders.amount (data/generate_client_zero.py), the vendor's curve fitted to
October 2024 to March 2026 and forecast from there to March 2027, and the plan line.

The concept chapters' example, invented and labelled invented wherever it appears: a chai stall at
a hostel gate, 730 days of cups from Monday 30 September 2024, about 100 on a weekday and 60 on a
Sunday, about 1.4 times an ordinary day in the exam fortnight that closes each semester and 0.4 in
Diwali week, when the hostel empties, the level growing about 10 percent a year under a wobble of
a few cups. Its Diwalis fall on the real dates (31 October 2024 and 20 October 2025). The days each
chapter counts by hand are pinned to round numbers and written as the chapter's own small table.
The hostel mess's rice, the exercises' cameo, is invented the same way. Every one of these numbers
is recorded under a toy_ id. Run with --against-main to assert that every case table is byte for
byte the one origin/main holds.
"""
from __future__ import annotations

import math
import pathlib
import random
import sys
from datetime import date, timedelta

import pandas as pd
import yaml

HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
ROOT = DAY.parents[2]
DATA = DAY / "data"
FACTS = HERE / "C2_W04_D05_facts_INTERNAL.yaml"
sys.path.insert(0, str(ROOT / "data"))
import generate_client_zero as gcz  # noqa: E402

SEED = 20261030
START = date(2024, 9, 30)          # Monday, the first week of the history
N_HIST = 104                       # 30 Sep 2024 to 21 Sep 2026
N_ALL = 114                        # to the week of 30 Nov 2026
ORDINARY = 210_000                 # an ordinary week in late 2024, before season and noise
GROWTH = 1.034                     # the level's yearly growth; the measured year on year is about 4
DRIFT = 1.04                       # the 4 percent a year the history grew
FINANCE = 1.04                     # finance's rule: last year's weeks plus 4 percent
DIWALI = {2024: 4, 2025: 55, 2026: 109}   # week index of the Monday of each Diwali week
FESTIVE = {-3: 1.5, -2: 1.9, -1: 1.7, 0: 1.4, 1: 0.88}   # weeks from Diwali, times the ordinary week
SALE_OFFSETS = (-3, -2)            # the festive sale runs three and two weeks before Diwali
ALIGN = range(-5, 5)               # weeks the festival-aligned copy matches by distance from Diwali
MONTH = {1: 0.95, 2: 0.94, 3: 0.98, 4: 0.97, 5: 0.99, 6: 1.01,
         7: 0.90, 8: 0.92, 9: 1.03, 10: 1.0, 11: 1.01, 12: 1.04}
PAYDAY = 1.035                     # the week that holds the 1st of a month
AUG_SALE = 1.22                    # the week that holds 15 August
NOISE = 0.02
ORIGIN = 90                        # the week of 22 June 2026, the hold-out's origin
HOLDOUT = range(91, 104)           # 29 June to 21 September 2026
BACK_ORIGIN = 51                   # the week of 22 September 2025
BACK = range(52, 60)               # 29 September to 17 November 2025
HORIZON = range(104, 114)          # 28 September to 30 November 2026
WINDOW = range(106, 114)           # 12 October to 30 November 2026
PER_SHIFT = 120
IDLE_SHIFT_RS, IDLE_LOW, IDLE_HIGH = 650, 500, 800
LATE_RS, LATE_LOW, LATE_HIGH = 25, 15, 40
OVER_RS = IDLE_SHIFT_RS / PER_SHIFT          # Rs 5.42 per shipment planned and never shipped
QUANTILE = LATE_RS / (LATE_RS + OVER_RS)     # 0.82
VENDOR_PROMISE = 1.22
VENDOR_HOLD = (0.025, 0.007)       # the vendor's hold-out lift: a level, and a rise per week ahead
VENDOR_RISE = 0.006                # its festive forecast rises with the weeks ahead too


def week(i):
    return START + timedelta(weeks=i)


def dmy(i):
    """The Monday of week i, as a slide prints it: 12 Oct 2026."""
    d = week(i)
    return f"{d.day} {d:%b %Y}"


def offset(i):
    """Weeks from the nearest Diwali week inside the alignment band, or None."""
    for d in DIWALI.values():
        if i - d in ALIGN:
            return i - d
    return None


def holds_day(i, month, day):
    return any((week(i) + timedelta(days=k)).month == month and (week(i) + timedelta(days=k)).day == day
               for k in range(7))


def payday(i):
    return any((week(i) + timedelta(days=k)).day == 1 for k in range(7))


def build_series():
    """104 weeks of outbound shipments, rounded to the hundred, plus the calendar to week 114."""
    rng = random.Random(SEED)
    rows = []
    for i in range(N_HIST):
        o = offset(i)
        level = ORDINARY * GROWTH ** (i / 52)
        if o in FESTIVE:
            factor = FESTIVE[o]
        else:
            factor = MONTH[(week(i) + timedelta(days=3)).month]
            factor *= PAYDAY if payday(i) else 1.0
            factor *= AUG_SALE if holds_day(i, 8, 15) else 1.0
        noise = max(-0.045, min(0.045, rng.gauss(0, NOISE)))
        shipments = int(round(level * factor * (1 + noise) / 100) * 100)
        roster = int(round(level / PER_SHIFT * 1.02))           # the standing roster for an ordinary week
        worked = math.ceil(shipments / PER_SHIFT)
        rows.append({"week_start": week(i).isoformat(), "shipments": shipments,
                     "packer_shifts_worked": worked, "overtime_shifts": max(0, worked - roster)})
    cal = []
    for i in range(N_ALL):
        o = offset(i)
        sale = (o in SALE_OFFSETS) or holds_day(i, 8, 15)
        cal.append({"week_start": week(i).isoformat(), "diwali_week": int(o == 0), "sale_week": int(sale)})
    return pd.DataFrame(rows), pd.DataFrame(cal)


def aligned_source(i):
    """The week the festival-aligned copy reads for target week i."""
    o = offset(i)
    if o is None:
        return i - 52
    previous = max(d for d in DIWALI.values() if d < i - 26)
    return previous + o


def forecasts(y, targets, origin):
    """Every rule's forecast for the target weeks, made from the weeks up to origin."""
    slope = (y[origin] - y[0]) / origin
    return {
        "naive": {i: y[origin] for i in targets},
        "drift": {i: round(y[origin] + (i - origin) * slope) for i in targets},
        "bot": {i: y[i - 52] for i in targets},
        "finance": {i: round(y[i - 52] * FINANCE) for i in targets},
        "aligned": {i: round(y[aligned_source(i)] * DRIFT) for i in targets},
    }


def vendor_rows(y):
    """The vendor's file: a fit to the 91 training weeks, a forecast for the hold-out from the
    week of 22 June 2026, and a forecast for 28 September to 30 November 2026 from all 104 weeks.
    Its season copies the calendar weeks; its level reads the 2025 festive spike as growth, so it
    runs high and climbs with the weeks ahead."""
    rng = random.Random(SEED + 7)
    rows = []
    for i in range(ORIGIN + 1):
        e = max(-0.018, min(0.018, rng.gauss(0, 0.008)))
        rows.append((i, int(round(y[i] * (1 + e) / 100) * 100), "fitted"))
    a, b = VENDOR_HOLD
    for i in HOLDOUT:
        e = rng.gauss(0, 0.006)
        rows.append((i, int(round(y[i - 52] * DRIFT * (1 + a + b * (i - ORIGIN) + e) / 100) * 100), "holdout"))
    shape = {i: y[i - 52] * (1 + VENDOR_RISE * (i - (N_HIST - 1))) for i in HORIZON}
    scale = VENDOR_PROMISE * sum(y[i - 52] for i in WINDOW) / sum(shape[i] for i in WINDOW)
    for i in HORIZON:
        rows.append((i, int(round(shape[i] * scale / 100) * 100), "forecast"))
    return rows


def score(f, y, weeks):
    over = sum(max(0, f[i] - y[i]) for i in weeks)
    under = sum(max(0, y[i] - f[i]) for i in weeks)
    return {
        "mae": sum(abs(f[i] - y[i]) for i in weeks) / len(weeks),
        "high_weeks": sum(f[i] > y[i] for i in weeks),
        "over": over, "under": under,
        "idle_rs": over * OVER_RS, "late_rs": under * LATE_RS,
        "cost_rs": over * OVER_RS + under * LATE_RS,
    }


def quantile(values, p):
    """The p quantile with linear interpolation, as pandas computes it."""
    return float(pd.Series(values).quantile(p))


# ------------------------------------------------------------------------------------- Kalpa

def kalpa_months():
    return [f"{y}-{m:02d}" for y, m in
            [(2024 + (9 + k) // 12, (9 + k) % 12 + 1) for k in range(24)]]


def build_kalpa():
    """Kalpa Retail's 24 months, the vendor's file and the plan line.

    April to September 2026 are v4's monthly order sums. The year before mirrors their shape at a
    level about 4 percent lower, so a copy of last year's month is hard to beat; the two Octobers
    carry Diwali; October 2026 to March 2027 is the window the board number covers.
    """
    v4 = gcz.build_v4()
    sums = {}
    for o in v4["orders"]:
        sums[o["order_date"][:7]] = sums.get(o["order_date"][:7], 0) + o["amount"]
    rng = random.Random(SEED + 100)
    rev = {m: sums[m] for m in ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]}
    for m in ["2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09"]:
        rev[m] = int(round(rev[f"2026-{m[5:]}"] * 0.962 * (1 + rng.uniform(-0.015, 0.015)) / 1000) * 1000)
    ordinary = {"2025-11": 29_600_000, "2025-12": 30_900_000, "2026-01": 28_300_000,
                "2026-02": 27_400_000, "2026-03": 29_900_000}
    for m, v in ordinary.items():
        rev[m] = int(round(v * (1 + rng.uniform(-0.01, 0.01)) / 1000) * 1000)
    rev["2025-10"] = int(round(1.56 * (rev["2025-09"] + rev["2025-11"]) / 2 / 1000) * 1000)
    for m in ["2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03"]:
        later = f"{int(m[:4]) + 1}-{m[5:]}"
        rev[m] = int(round(rev[later] * 0.962 * (1 + rng.uniform(-0.012, 0.012)) / 1000) * 1000)
    months = kalpa_months()
    monthly = pd.DataFrame({"month": months, "revenue_rs": [rev[m] for m in months]})

    vrng = random.Random(SEED + 11)
    vend = []
    for m in months[:18]:
        e = max(-0.018, min(0.018, vrng.gauss(0, 0.009)))
        vend.append((m, int(round(rev[m] * (1 + e) / 1000) * 1000), "fitted"))
    ahead = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09",
             "2026-10", "2026-11", "2026-12", "2027-01", "2027-02", "2027-03"]
    lift = {m: 1.13 + 0.012 * k for k, m in enumerate(ahead[:6])}
    later = ahead[6:]
    base = {m: rev[f"{int(m[:4]) - 1}-{m[5:]}"] for m in later}
    shape = {m: base[m] * (1 + 0.01 * k) for k, m in enumerate(later)}
    scale = VENDOR_PROMISE * sum(base.values()) / sum(shape.values())
    for m in ahead[:6]:
        vend.append((m, int(round(rev[f"{int(m[:4]) - 1}-{m[5:]}"] * lift[m] / 1000) * 1000), "holdout"))
    for m in later:
        vend.append((m, int(round(shape[m] * scale / 1000) * 1000), "forecast"))
    vendor = pd.DataFrame(vend, columns=["month", "vendor_rs", "kind"])
    plan = pd.DataFrame({"month": later,
                         "plan_rs": [int(round(base[m] * 1.15 / 1000) * 1000) for m in later]})
    return monthly, vendor, plan, sums


# ------------------------------------------------------------------------------------- the stall
# The gate chai stall, invented for the concept chapters. Its own random stream, so the case
# tables above draw exactly the numbers they always drew.

STALL_SEED = SEED + 900
STALL_START = date(2024, 9, 30)            # a Monday; 730 days run to Tuesday 29 September 2026
STALL_DAYS = 730
STALL_LEVEL = 100                          # cups on an ordinary weekday at the start
STALL_GROWTH = 1.10                        # the level's growth a year, as the hostel fills
STALL_SUNDAY = 0.6                         # a Sunday's cups over an ordinary weekday's
STALL_EXAM = 1.4                           # a day of the exam fortnight over an ordinary day
STALL_DIWALI = 0.4                         # a day of Diwali week, the hostel empty, over an ordinary day
STALL_NOISE, STALL_CLIP = 0.03, 0.10
STALL_EXAMS = [date(2024, 11, 27), date(2025, 4, 23), date(2025, 11, 26), date(2026, 4, 22)]   # 14 days each
STALL_DIWALI_WEEKS = [date(2024, 10, 28), date(2025, 10, 20)]   # the Mondays of the weeks holding Diwali
STALL_ALIGN_DAYS = 14                      # the festival-aligned copy's stretch either side of Diwali's week
STALL_PINS = {
    # chapter 1: two Mondays a week apart, the Sunday between, and the same days 52 weeks later
    date(2024, 9, 30): 100, date(2024, 10, 6): 60, date(2024, 10, 7): 100, date(2025, 10, 5): 66, date(2025, 10, 6): 110,
    # chapter 2: last Sunday, the last four days, and next Sunday
    date(2025, 1, 12): 61, date(2025, 1, 15): 98, date(2025, 1, 16): 104, date(2025, 1, 17): 101,
    date(2025, 1, 18): 103, date(2025, 1, 19): 60,
    # chapter 2: the first day of the exam fortnight in both years, and the day before it
    date(2024, 11, 27): 140, date(2025, 11, 25): 110, date(2025, 11, 26): 154,
    # chapter 2: Diwali moved eleven days earlier in 2025
    date(2024, 10, 21): 100, date(2024, 10, 31): 40, date(2025, 10, 20): 44, date(2025, 10, 30): 110,
    # chapter 3: the origin and the three hidden days
    date(2025, 2, 11): 100, date(2025, 2, 12): 110, date(2025, 2, 13): 95, date(2025, 2, 14): 100,
    # chapter 4: the nephew's four days and day 5
    date(2025, 3, 3): 100, date(2025, 3, 4): 104, date(2025, 3, 5): 98, date(2025, 3, 6): 110,
    date(2025, 3, 7): 102,
}
CAN = 40                                   # cups of tea one milk can makes
UNSOLD_RS, SHORT_RS = 6, 12                # a cup's milk wasted, and a cup's margin lost
DRIFT_WEEKS = (date(2024, 12, 30), 12)     # the plain climb: twelve weeks of weekly totals from here


def in_exams(d):
    return any(s <= d < s + timedelta(days=14) for s in STALL_EXAMS)


def in_diwali(d):
    return any(m <= d < m + timedelta(days=7) for m in STALL_DIWALI_WEEKS)


def stall_aligned_source(d):
    """The day the festival-aligned copy reads: 51 weeks back near Diwali's week, 52 elsewhere."""
    for m in STALL_DIWALI_WEEKS[1:]:
        if m - timedelta(days=STALL_ALIGN_DAYS) <= d < m + timedelta(days=7 + STALL_ALIGN_DAYS):
            return d - timedelta(weeks=51)
    return d - timedelta(weeks=52)


def build_stall():
    """730 days of the stall's cups, with the pinned days in place."""
    rng = random.Random(STALL_SEED)
    rows = []
    for k in range(STALL_DAYS):
        d = STALL_START + timedelta(days=k)
        level = STALL_LEVEL * STALL_GROWTH ** (k / 365)
        if in_diwali(d):
            factor = STALL_DIWALI
        else:
            factor = (STALL_SUNDAY if d.weekday() == 6 else 1.0) * (STALL_EXAM if in_exams(d) else 1.0)
        noise = max(-STALL_CLIP, min(STALL_CLIP, rng.gauss(0, STALL_NOISE)))
        cups = STALL_PINS.get(d, int(round(level * factor * (1 + noise))))
        rows.append({"date": d.isoformat(), "weekday": d.strftime("%a"), "cups": cups,
                     "exam_fortnight": int(in_exams(d)), "diwali_week": int(in_diwali(d))})
    return pd.DataFrame(rows)


def stall_tables(stall):
    """The small tables the four concept notebooks print in full, each a slice of the stall's days."""
    s = stall.set_index("date")
    day = lambda d: s.loc[d.isoformat()]
    first = [STALL_START + timedelta(days=k) for k in range(14)]
    fortnights = pd.DataFrame({
        "day": range(1, 15), "weekday": [d.strftime("%a") for d in first],
        "date_2024": [d.isoformat() for d in first], "cups_2024": [day(d).cups for d in first],
        "date_2025": [(d + timedelta(weeks=52)).isoformat() for d in first],
        "cups_2025": [day(d + timedelta(weeks=52)).cups for d in first]})
    w = [date(2025, 1, 12) + timedelta(days=k) for k in range(8)]
    week = pd.DataFrame({"date": [d.isoformat() for d in w], "weekday": [d.strftime("%a") for d in w],
                         "cups": [day(d).cups for d in w]})
    h = [date(2025, 2, 1) + timedelta(days=k) for k in range(14)]
    hidden = pd.DataFrame({"day": range(1, 15), "date": [d.isoformat() for d in h],
                           "weekday": [d.strftime("%a") for d in h], "cups": [day(d).cups for d in h],
                           "hidden": [int(k >= 11) for k in range(14)]})
    n = [date(2025, 3, 3) + timedelta(days=k) for k in range(14)]
    nephew = pd.DataFrame({"date": [d.isoformat() for d in n], "weekday": [d.strftime("%a") for d in n],
                           "cups": [day(d).cups for d in n], "hidden": [int(k >= 7) for k in range(14)]})
    what_ifs = pd.DataFrame([
        {"example": "mape", "day": "an ordinary day", "forecast": 100, "sold": 85},
        {"example": "mape", "day": "a rain day, the stall shut after an hour", "forecast": 20, "sold": 5},
        {"example": "rule P", "day": "day 1", "forecast": 110, "sold": 100},
        {"example": "rule P", "day": "day 2", "forecast": 110, "sold": 100},
        {"example": "rule Q", "day": "day 1", "forecast": 110, "sold": 100},
        {"example": "rule Q", "day": "day 2", "forecast": 90, "sold": 100},
    ])
    return fortnights, week, hidden, nephew, what_ifs


# ------------------------------------------------------------------------------------- facts

def plain(value):
    """A number pandas handed back, as the plain int or float the YAML writer understands."""
    if isinstance(value, (list, tuple)):
        return [plain(v) for v in value]
    if hasattr(value, "item"):
        value = value.item()
    return round(value, 6) if isinstance(value, float) else value


class Facts:
    """Every number a learner sees, as rows of id, value, the form it prints in, how and where."""

    def __init__(self):
        self.sections = {}

    def add(self, section, fid, value, shown, how, used):
        if isinstance(value, float):
            value = round(value, 6)
        self.sections.setdefault(section, []).append(
            {"id": fid, "value": value, "shown": shown, "how": how, "used_in": used})
        return value

    def toy(self, fid, value, shown, how, used):
        """An invented number, under a toy_ id, with how it was invented and who uses it."""
        value = plain(value)
        self.sections.setdefault("toy", []).append(
            {"id": f"toy_{fid}", "value": value, "shown": shown, "how": how, "used_by": used})
        return value

    def write(self, header):
        body = yaml.safe_dump(self.sections, sort_keys=False, allow_unicode=False, width=100)
        FACTS.write_text(header + "\n\n" + body, encoding="utf-8")
        return sum(len(rows) for rows in self.sections.values())


def n(x):
    """A count of shipments as the case prints it, with thousands commas: 2,385,240.

    Standard formatting, so a number in a learner file matches what the learner's notebook prints.
    """
    return f"{int(round(x)):,}"


def lakh(rs, places=1):
    return f"Rs {rs / 1e5:.{places}f} lakh"


def pct(x, places=1):
    return f"{x * 100:.{places}f} percent"


SUB = {1: "Trend and seasonality, read before modelling",
       2: "Naive, seasonal naive and drift baselines",
       3: "Holding out; MAE and MAPE in the business's units",
       4: "Beating the baseline; the vendor curve tested",
       5: "The good-enough call and the forecast note"}


def concept(k, detail):
    return f"invented for the concept chapter on {SUB[k]}: {detail}"


def exercise(k, detail):
    return f"invented for the exercise set on {SUB[k]}: {detail}"


def stall_facts(F, stall, tables, y, ahead, S):
    """Every number the concept chapters, their notebooks and the hostel-mess items print."""
    fortnights, week, hidden, nephew, what_ifs = tables
    s = stall.set_index("date").cups
    c = lambda d: int(s[d.isoformat()])
    out = {}

    # ---- the stall itself
    F.toy("stall_days", STALL_DAYS, "730 days", concept(1, "the stall's record, 30 Sep 2024 to 29 Sep 2026"),
          ["notebooks 01 to 04", "half1 SECTIONs 1 to 4"])
    F.toy("stall_level", STALL_LEVEL, "about 100 cups", concept(1, "an ordinary weekday at the start"),
          ["half1 SECTION 1", "notebook 01", "notes"])
    F.toy("stall_growth", STALL_GROWTH - 1, "about 10 percent a year", concept(1, "the level's growth as the hostel fills"),
          ["half1 SECTION 1", "notebook 01", "notes"])
    F.toy("stall_sunday_share", STALL_SUNDAY, "0.6", concept(1, "a Sunday's cups over an ordinary weekday's"),
          ["half1 SECTION 1", "notebook 01"])
    F.toy("stall_exam_factor", STALL_EXAM, "1.4", concept(1, "a day of the exam fortnight over an ordinary day"),
          ["half1 SECTION 1", "notebook 01"])
    F.toy("stall_diwali_factor", STALL_DIWALI, "0.4", concept(1, "a day of Diwali week over an ordinary day"),
          ["half1 SECTION 1", "notebook 01"])
    F.toy("stall_exam_days", 14, "a fortnight", concept(1, "the exam fortnight that closes each semester, two a year"),
          ["half1 SECTION 1"])
    F.toy("stall_week", 7, "7 days", concept(1, "the season's length of the weekly beat"),
          ["half1 SECTIONs 1 and 2", "notebooks 01 and 02"])
    F.toy("stall_year_lag", 364, "364 days", concept(2, "52 weeks back, so a copy lands on the same weekday"),
          ["half1 SECTION 2", "notebook 02"])
    F.toy("stall_aligned_lag", 357, "357 days", concept(2, "51 weeks back, the festival-aligned copy near Diwali's week"),
          ["half1 SECTION 2", "notebook 02"])
    F.toy("stall_diwali_shift", 11, "eleven days", concept(2, "Diwali on 20 Oct 2025 came eleven days earlier in the calendar than 31 Oct 2024"),
          ["half1 SECTION 2", "notebook 02", "notes"])

    # ---- chapter 1: the weekly beat, growth read a season apart, the yearly beat
    F.toy("ch1_cups_2024", fortnights.cups_2024.tolist(), ", ".join(map(str, fortnights.cups_2024)),
          concept(1, "the stall's first fourteen days, 30 Sep to 13 Oct 2024"), ["notebook 01", "half1 SECTION 1"])
    F.toy("ch1_cups_2025", fortnights.cups_2025.tolist(), ", ".join(map(str, fortnights.cups_2025)),
          concept(1, "the same fourteen days 52 weeks later, 29 Sep to 12 Oct 2025"), ["notebook 01", "half1 SECTION 1"])
    for name, d in (("sunday", date(2024, 10, 6)), ("monday", date(2024, 10, 7)),
                    ("sunday_next", date(2025, 10, 5)), ("monday_next", date(2025, 10, 6))):
        F.toy(f"ch1_{name}", c(d), str(c(d)), concept(1, f"cups on {d:%a %d %b %Y}"), ["half1 SECTION 1", "notebook 01", "notes"])
    wrong = c(date(2024, 10, 7)) / c(date(2024, 10, 6)) - 1
    F.toy("ch1_wrong_growth", wrong, "67 percent", concept(1, "Monday over Sunday, minus one: the weekly beat read as growth"),
          ["half1 SECTION 1", "notebook 01", "Kahoot Q8", "notes"])
    F.toy("ch1_share", c(date(2024, 10, 6)) / c(date(2024, 10, 7)), "0.6", concept(1, "Sunday's 60 over Monday's 100"),
          ["half1 SECTION 1", "notebook 01"])
    g = c(date(2025, 10, 6)) / c(date(2024, 10, 7)) - 1
    F.toy("ch1_growth", g, "10 percent", concept(1, "this Monday over the same Monday 52 weeks back, minus one"),
          ["half1 SECTION 1", "notebook 01", "notes"])
    ratio = fortnights.cups_2025.sum() / fortnights.cups_2024.sum() - 1
    F.toy("ch1_fortnight_growth", ratio, pct(ratio), concept(1, "the fourteen days of 2025 over the same days of 2024, minus one"),
          ["notebook 01"])
    F.toy("ch1_fortnight_totals", [int(fortnights.cups_2024.sum()), int(fortnights.cups_2025.sum())],
          f"{fortnights.cups_2024.sum():,} and {fortnights.cups_2025.sum():,}", concept(1, "the two fortnights' totals"), ["notebook 01"])
    st = stall.assign(d=pd.to_datetime(stall.date))
    weekday = st.d.dt.weekday < 6

    def season_ratio(start, days, before=14):
        inside = st[(st.d >= pd.Timestamp(start)) & (st.d < pd.Timestamp(start) + pd.Timedelta(days=days)) & weekday]
        prior = st[(st.d >= pd.Timestamp(start) - pd.Timedelta(days=before)) & (st.d < pd.Timestamp(start)) & weekday]
        return inside.cups.mean() / prior.cups.mean()
    exam = [season_ratio(STALL_EXAMS[0], 14), season_ratio(STALL_EXAMS[2], 14)]
    diwali = [season_ratio(STALL_DIWALI_WEEKS[0], 7), season_ratio(STALL_DIWALI_WEEKS[1], 7)]
    F.toy("ch1_exam_ratio", [round(x, 2) for x in exam], f"{exam[0]:.2f} and {exam[1]:.2f}",
          concept(1, "the first exam fortnight's weekdays over the fortnight before it, 2024 and 2025"), ["notebook 01", "half1 SECTION 1"])
    F.toy("ch1_diwali_ratio", [round(x, 2) for x in diwali], f"{diwali[0]:.2f} and {diwali[1]:.2f}",
          concept(1, "Diwali week's weekdays over the fortnight before it, 2024 and 2025"), ["notebook 01", "half1 SECTION 1"])
    yr2 = st[st.d >= pd.Timestamp(STALL_START) + pd.Timedelta(weeks=52)].copy()
    yr2["last_year"] = [c(d.date() - timedelta(weeks=52)) for d in yr2.d]
    yr2["left"] = yr2.cups - yr2.last_year * STALL_GROWTH
    moved = yr2.d.apply(lambda d: STALL_DIWALI_WEEKS[1] <= d.date() < STALL_DIWALI_WEEKS[1] + timedelta(days=14))
    rest = yr2[~moved].left
    F.toy("ch1_left_mean", rest.mean(), f"{rest.mean():.1f}", concept(1, "what is left after the growth and the beats are copied out, its mean, Diwali's fortnight aside"),
          ["notebook 01"])
    F.toy("ch1_left_spread", rest.std(), f"{rest.std():.1f}", concept(1, "the same, its standard deviation in cups"), ["notebook 01", "notes"])
    F.toy("ch1_left_worst", yr2[moved].left.abs().max(), f"{yr2[moved].left.abs().max():.0f}",
          concept(1, "the largest left-over in the fortnight Diwali moved into, cups"), ["notebook 01"])
    F.toy("ch1_left_days", int(len(rest)), f"{len(rest)}", concept(1, "the year-two days outside that fortnight"), ["notebook 01"])
    out.update(exam_ratio=exam, diwali=diwali, ratio=ratio, left_mean=rest.mean(), left_spread=rest.std())

    # ---- chapter 2: three copy rules, the yearly copy and its growth, the moving festival, drift
    F.toy("ch2_week", week.cups.tolist(), ", ".join(map(str, week.cups)),
          concept(2, "Sun 12 Jan to Sun 19 Jan 2025"), ["notebook 02", "half1 SECTION 2"])
    four = [c(date(2025, 1, 15) + timedelta(days=k)) for k in range(4)]
    naive, sunday, actual = four[-1], c(date(2025, 1, 12)), c(date(2025, 1, 19))
    step = (four[-1] - four[0]) / 3
    drift = four[-1] + step
    F.toy("ch2_four", four, ", ".join(map(str, four)), concept(2, "the four days before next Sunday, Wed 15 to Sat 18 Jan 2025"),
          ["half1 SECTION 2", "notebook 02", "notes", "c2 set"])
    F.toy("ch2_last_sunday", sunday, str(sunday), concept(2, "Sun 12 Jan 2025"), ["half1 SECTION 2", "notebook 02", "notes"])
    F.toy("ch2_next_sunday", actual, str(actual), concept(2, "Sun 19 Jan 2025, what the forecasts are scored on"), ["half1 SECTION 2", "notebook 02"])
    F.toy("ch2_naive", naive, str(naive), concept(2, "the naive: Saturday's 103 repeated"), ["half1 SECTION 2", "notebook 02", "notes"])
    F.toy("ch2_drift_step", step, f"{step:.2f}", concept(2, "drift's step: (103 - 98) / 3"), ["half1 SECTION 2", "notebook 02"])
    F.toy("ch2_drift", drift, f"{drift:.1f}", concept(2, "drift: 103 plus the step, about 105"), ["half1 SECTION 2", "notebook 02", "notes"])
    F.toy("ch2_drift_round", round(drift), str(round(drift)), concept(2, "drift rounded to a cup"), ["half1 SECTION 2", "notes"])
    for name, f in (("naive", naive), ("drift", drift), ("snaive", sunday)):
        F.toy(f"ch2_miss_{name}", f - actual, f"{f - actual:+.0f}" if name != "drift" else f"{f - actual:+.1f}",
              concept(2, f"{name} minus next Sunday's 60"), ["half1 SECTION 2", "notebook 02"])
    e1, e0, e2 = c(STALL_EXAMS[0]), c(STALL_EXAMS[2] - timedelta(days=1)), c(STALL_EXAMS[2])
    F.toy("ch2_exam_2024", e1, str(e1), concept(2, "the first day of the November exam fortnight, Wed 27 Nov 2024"), ["half1 SECTION 2", "notebook 02"])
    F.toy("ch2_exam_eve", e0, str(e0), concept(2, "the day before it a year later, Tue 25 Nov 2025"), ["half1 SECTION 2", "notebook 02"])
    F.toy("ch2_exam_2025", e2, str(e2), concept(2, "the first exam day of 2025, Wed 26 Nov 2025"), ["half1 SECTION 2", "notebook 02", "notes"])
    F.toy("ch2_exam_miss_naive", e0 - e2, f"{e0 - e2:+d}", concept(2, "the naive's miss on the first exam day"), ["half1 SECTION 2", "notebook 02"])
    F.toy("ch2_exam_miss_copy", e1 - e2, f"{e1 - e2:+d}", concept(2, "the yearly copy's miss: the growth"), ["half1 SECTION 2", "notebook 02"])
    grown = round(e1 * STALL_GROWTH)
    F.toy("ch2_exam_grown", grown, str(grown), concept(2, "the yearly copy times 1.10"), ["half1 SECTION 2", "notebook 02"])
    F.toy("ch2_growth_factor", STALL_GROWTH, "1.10", concept(2, "the growth chapter 1 read, as a multiplier"), ["half1 SECTION 2", "notebook 02"])
    exam_days = [date(2025, 11, 12) + timedelta(days=k) for k in range(28)]
    for name, rule, detail in (("naive", lambda d: c(d - timedelta(days=1)), "yesterday's cups"),
                               ("copy", lambda d: c(d - timedelta(weeks=52)), "the day 364 back"),
                               ("grown", lambda d: round(c(d - timedelta(weeks=52)) * STALL_GROWTH), "the day 364 back times 1.10")):
        m = sum(abs(rule(d) - c(d)) for d in exam_days) / len(exam_days)
        F.toy(f"ch2_exam_window_mae_{name}", m, f"{m:.1f}",
              concept(2, f"the average miss of {detail} on the 28 days from 12 Nov 2025, the fortnight before the exams and the exam fortnight"),
              ["half1 SECTION 2 picture", "notebook 02"])
    d24, d25 = date(2024, 10, 31), date(2025, 10, 20)
    pairs = {"diwali_2025": (d25, d25 - timedelta(weeks=52)), "after_2025": (date(2025, 10, 30), date(2025, 10, 30) - timedelta(weeks=52))}
    for name, (t, src) in pairs.items():
        F.toy(f"ch2_{name}", c(t), str(c(t)), concept(2, f"cups on {t:%a %d %b %Y}"), ["half1 SECTION 2", "notebook 02", "notes"])
        F.toy(f"ch2_{name}_copy", c(src), str(c(src)), concept(2, f"the calendar copy's source, {src:%a %d %b %Y}"), ["half1 SECTION 2", "notebook 02"])
        F.toy(f"ch2_{name}_miss", c(src) - c(t), f"{c(src) - c(t):+d}", concept(2, "the calendar copy minus what sold"), ["half1 SECTION 2", "notebook 02", "notes"])
    win = [STALL_DIWALI_WEEKS[1] - timedelta(days=7) + timedelta(days=k) for k in range(21)]
    cal_miss = [c(d - timedelta(weeks=52)) - c(d) for d in win]
    ali_miss = [c(stall_aligned_source(d)) - c(d) for d in win]
    F.toy("ch2_window_cal_worst", max(map(abs, cal_miss)), str(max(map(abs, cal_miss))),
          concept(2, "the calendar copy's worst miss, 13 Oct to 2 Nov 2025"), ["notebook 02", "half1 SECTION 2"])
    F.toy("ch2_window_aligned_worst", max(map(abs, ali_miss)), str(max(map(abs, ali_miss))),
          concept(2, "the festival-aligned copy's worst miss on the same days"), ["notebook 02", "half1 SECTION 2"])
    F.toy("ch2_window_cal_mae", sum(map(abs, cal_miss)) / len(win), f"{sum(map(abs, cal_miss)) / len(win):.1f}",
          concept(2, "the calendar copy's average miss on those 21 days"), ["notebook 02"])
    F.toy("ch2_window_aligned_mae", sum(map(abs, ali_miss)) / len(win), f"{sum(map(abs, ali_miss)) / len(win):.1f}",
          concept(2, "the festival-aligned copy's average miss on those 21 days"), ["notebook 02"])
    F.toy("ch2_window_days", len(win), "21 days", concept(2, "the three weeks around Diwali's week of 2025"), ["notebook 02"])
    start, nweeks = DRIFT_WEEKS
    totals = [int(sum(c(start + timedelta(weeks=w, days=k)) for k in range(7))) for w in range(nweeks + 1)]
    dstep = (totals[nweeks - 1] - totals[0]) / (nweeks - 1)
    dfore = totals[nweeks - 1] + dstep
    F.toy("ch2_weekly_totals", totals[:nweeks], ", ".join(f"{t:,}" for t in totals[:nweeks]),
          concept(2, "the stall's weekly totals, the twelve weeks from Mon 30 Dec 2024"), ["notebook 02"])
    F.toy("ch2_weekly_step", dstep, f"{dstep:.1f}", concept(2, "drift's step on the weekly totals: (week 12 - week 1) / 11"), ["notebook 02"])
    F.toy("ch2_weekly_forecast", dfore, f"{dfore:,.0f}", concept(2, "drift's forecast for week 13"), ["notebook 02"])
    F.toy("ch2_weekly_actual", totals[nweeks], f"{totals[nweeks]:,}", concept(2, "what week 13 sold"), ["notebook 02"])
    F.toy("ch2_weekly_miss", dfore - totals[nweeks], f"{dfore - totals[nweeks]:+.0f}", concept(2, "drift's miss on week 13"), ["notebook 02"])
    mon, sun_before, mon_before = c(date(2025, 1, 20)), c(date(2025, 1, 19)), c(date(2025, 1, 13))
    F.toy("ch2_turn_monday", mon, str(mon), concept(2, "the your-turn: cups on Mon 20 Jan 2025, the day after next Sunday"),
          ["notebook 02"])
    F.toy("ch2_turn_naive_miss", sun_before - mon, f"{sun_before - mon:+d}", concept(2, "the naive copies Sunday's 60 into Monday: its miss"),
          ["notebook 02"])
    F.toy("ch2_turn_snaive", mon_before, str(mon_before), concept(2, "the seasonal naive copies last Monday, 13 Jan 2025"), ["notebook 02"])
    F.toy("ch2_turn_snaive_miss", mon_before - mon, f"{mon_before - mon:+d}", concept(2, "the seasonal naive's miss on that Monday"),
          ["notebook 02"])
    out.update(four=four, drift=drift, exam_days=(e0, e1, e2), cal_worst=max(map(abs, cal_miss)),
               ali_worst=max(map(abs, ali_miss)), weekly=(totals, dstep, dfore))

    # ---- chapter 3: hide the latest days, score them, price them
    F.toy("ch3_cups", hidden.cups.tolist(), ", ".join(map(str, hidden.cups)), concept(3, "fourteen days, Sat 1 to Fri 14 Feb 2025"),
          ["notebook 03", "half1 SECTION 3"])
    origin = int(hidden.cups.iloc[10])
    acts = hidden.cups.iloc[11:].tolist()
    miss = [origin - a for a in acts]
    mae = sum(map(abs, miss)) / 3
    mape = sum(abs(m) / a for m, a in zip(miss, acts)) / 3
    lean = sum(miss) / 3
    short = sum(-m for m in miss if m < 0)
    unsold = sum(m for m in miss if m > 0)
    F.toy("ch3_origin", origin, str(origin), concept(3, "day 11, Tue 11 Feb 2025, the last day the rule may see"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_hidden", acts, ", ".join(map(str, acts)), concept(3, "days 12 to 14, what sold"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_misses", miss, ", ".join(f"{m:+d}" if m else "0" for m in miss), concept(3, "the naive's 100 minus what sold, each day"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_abs_sum", sum(map(abs, miss)), str(sum(map(abs, miss))), concept(3, "the misses' sizes added: 10 + 5 + 0"), ["half1 SECTION 3", "notebook 03"])
    F.toy("ch3_mae", mae, f"{mae:.1f}", concept(3, "MAE: 15 cups over 3 days"), ["half1 SECTION 3", "notebook 03", "notes", "Kahoot"])
    F.toy("ch3_mape", mape, pct(mape), concept(3, "MAPE: (10/110 + 5/95 + 0/100) / 3"), ["half1 SECTION 3", "notebook 03", "notes"])
    for name, a in zip(("day12", "day13"), acts[:2]):
        F.toy(f"ch3_pct_{name}", abs(origin - a) / a, pct(abs(origin - a) / a), concept(3, f"the miss over what sold, {name}"), ["notebook 03"])
    F.toy("ch3_lean", lean, f"{lean:+.1f}", concept(3, "the signed misses averaged: the rule runs 1.7 cups low"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_unsold_rs", UNSOLD_RS, "Rs 6", concept(3, "a cup's milk wasted when it does not sell"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_short_rs", SHORT_RS, "Rs 12", concept(3, "a cup's margin lost when the milk runs out"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_short_cups", short, str(short), concept(3, "cups short across the hidden days"), ["half1 SECTION 3", "notebook 03"])
    F.toy("ch3_unsold_cups", unsold, str(unsold), concept(3, "cups unsold across the hidden days"), ["half1 SECTION 3", "notebook 03"])
    F.toy("ch3_short_cost", short * SHORT_RS, f"Rs {short * SHORT_RS}", concept(3, "10 short x Rs 12"), ["half1 SECTION 3", "notebook 03"])
    F.toy("ch3_unsold_cost", unsold * UNSOLD_RS, f"Rs {unsold * UNSOLD_RS}", concept(3, "5 unsold x Rs 6"), ["half1 SECTION 3", "notebook 03"])
    F.toy("ch3_cost", short * SHORT_RS + unsold * UNSOLD_RS, f"Rs {short * SHORT_RS + unsold * UNSOLD_RS}",
          concept(3, "the three days' misses in rupees"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_horizon", 3, "three days", concept(3, "the milk order reaches three days ahead, so three days are hidden"), ["half1 SECTION 3", "notebook 03"])
    F.toy("ch3_train_days", 11, "11 days", concept(3, "days 1 to 11, the training days"), ["half1 SECTION 3", "notebook 03"])
    mp = what_ifs[what_ifs.example == "mape"]
    mp_miss = (mp.forecast - mp.sold).abs().tolist()
    mp_pct = [m / a for m, a in zip(mp_miss, mp.sold)]
    F.toy("ch3_mape_days", mp.forecast.tolist() + mp.sold.tolist(), "100 and 85; 20 and 5",
          concept(3, "two days apart from the stall's record: forecast and sold on an ordinary day and a rain day"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_mape_miss", mp_miss[0], str(mp_miss[0]), concept(3, "both days miss by 15 cups"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_mape_pcts", [round(p, 4) for p in mp_pct], f"{mp_pct[0] * 100:.1f} and {mp_pct[1] * 100:.0f} percent",
          concept(3, "15 over 85, and 15 over 5"), ["half1 SECTION 3", "notebook 03", "notes"])
    F.toy("ch3_mape_mean", sum(mp_pct) / 2, pct(sum(mp_pct) / 2), concept(3, "the two days' MAPE"), ["half1 SECTION 3", "notebook 03"])
    rules = {}
    for r in ("rule P", "rule Q"):
        sub = what_ifs[what_ifs.example == r]
        m = (sub.forecast - sub.sold).tolist()
        cost = sum(x * UNSOLD_RS if x > 0 else -x * SHORT_RS for x in m)
        rules[r] = (m, sum(map(abs, m)) / 2, sum(m) / 2, cost)
        key = r.replace(" ", "_").lower()
        F.toy(f"ch3_{key}_misses", m, ", ".join(f"{x:+d}" for x in m), concept(3, f"{r}'s two misses"), ["half1 SECTION 3", "notebook 03"])
        F.toy(f"ch3_{key}_mae", sum(map(abs, m)) / 2, f"{sum(map(abs, m)) / 2:.0f}", concept(3, f"{r}'s MAE"), ["half1 SECTION 3", "notebook 03"])
        F.toy(f"ch3_{key}_lean", sum(m) / 2, f"{sum(m) / 2:+.0f}", concept(3, f"{r}'s lean"), ["notebook 03"])
        F.toy(f"ch3_{key}_cost", cost, f"Rs {cost}", concept(3, f"{r}'s misses at Rs 6 unsold and Rs 12 short"), ["half1 SECTION 3", "notebook 03", "notes"])
    week_back = hidden.cups.iloc[4:7].tolist()                 # days 5 to 7, the same weekdays a week before days 12 to 14
    t_miss = [f - a for f, a in zip(week_back, acts)]
    t_short, t_unsold = sum(-m for m in t_miss if m < 0), sum(m for m in t_miss if m > 0)
    F.toy("ch3_turn_forecasts", week_back, ", ".join(map(str, week_back)), concept(3, "the your-turn: the seasonal naive copies days 5 to 7 into days 12 to 14"),
          ["notebook 03"])
    F.toy("ch3_turn_misses", t_miss, ", ".join(f"{m:+d}" for m in t_miss), concept(3, "its misses, forecast minus sold"), ["notebook 03"])
    F.toy("ch3_turn_mae", sum(map(abs, t_miss)) / 3, f"{sum(map(abs, t_miss)) / 3:.1f}", concept(3, "its MAE on the three hidden days"), ["notebook 03"])
    F.toy("ch3_turn_lean", sum(t_miss) / 3, f"{sum(t_miss) / 3:+.1f}", concept(3, "its lean"), ["notebook 03"])
    F.toy("ch3_turn_short_cups", t_short, str(t_short), concept(3, "cups short across the three days"), ["notebook 03"])
    F.toy("ch3_turn_unsold_cups", t_unsold, str(t_unsold), concept(3, "cups unsold across the three days"), ["notebook 03"])
    F.toy("ch3_turn_cost", t_short * SHORT_RS + t_unsold * UNSOLD_RS, f"Rs {t_short * SHORT_RS + t_unsold * UNSOLD_RS}",
          concept(3, "its misses in rupees: short at Rs 12, unsold at Rs 6"), ["notebook 03"])
    F.toy("ch3_cover_share", SHORT_RS / (SHORT_RS + UNSOLD_RS), "two days in three",
          concept(5, "the stall's plan share, Rs 12 over Rs 12 plus Rs 6, which opens notebook 07's depth section"), ["notebook 07"])
    out.update(mae=mae, mape=mape, lean=lean, cost=short * SHORT_RS + unsold * UNSOLD_RS, rules=rules, mape_days=mp_pct)

    # ---- chapter 4: fit against forecast, the baseline race, the cans, the note
    days5 = nephew.cups.iloc[:5].tolist()
    F.toy("ch4_four", days5[:4], ", ".join(map(str, days5[:4])), concept(4, "the nephew's four days, Mon 3 to Thu 6 Mar 2025"),
          ["half1 SECTION 4", "notebook 04", "notes", "c4 set"])
    F.toy("ch4_day5", days5[4], str(days5[4]), concept(4, "day 5, Fri 7 Mar 2025, what sold"), ["half1 SECTION 4", "notebook 04", "notes"])
    xs = [1, 2, 3, 4]
    xm, ym = sum(xs) / 4, sum(days5[:4]) / 4
    slope = sum((x - xm) * (v - ym) for x, v in zip(xs, days5[:4])) / sum((x - xm) ** 2 for x in xs)
    inter = ym - slope * xm
    line5 = inter + slope * 5
    fit_err = [abs(inter + slope * x - v) for x, v in zip(xs, days5[:4])]
    d1 = [b - a for a, b in zip(days5[:4], days5[1:4])]
    d2 = [b - a for a, b in zip(d1, d1[1:])]
    d3 = d2[1] - d2[0]
    cubic5 = days5[3] + (d1[-1] + (d2[-1] + d3))
    F.toy("ch4_line_slope", slope, f"{slope:.1f}", concept(4, "the straight line's slope through the four days"), ["notebook 04"])
    F.toy("ch4_line_start", inter, f"{inter:.0f}", concept(4, "the line's value at day 0"), ["notebook 04"])
    F.toy("ch4_line", line5, f"{line5:.0f}", concept(4, "the line's forecast for day 5"), ["half1 SECTION 4", "notebook 04", "notes", "c4 set"])
    F.toy("ch4_line_fit_mae", sum(fit_err) / 4, f"{sum(fit_err) / 4:.1f}", concept(4, "the line's average distance from the four days it was drawn through"),
          ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_differences", d1 + d2 + [d3], "4, -6, 12; -10, 18; 28", concept(4, "the four days' differences, three rounds deep"), ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_curve", cubic5, str(cubic5), concept(4, "the curve through all four days, extended to day 5"), ["half1 SECTION 4", "notebook 04", "notes", "c4 set"])
    F.toy("ch4_curve_next_d2", d2[-1] + d3, str(d2[-1] + d3), concept(4, "the next second difference: 18 + 28"), ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_curve_next_d1", d1[-1] + d2[-1] + d3, str(d1[-1] + d2[-1] + d3), concept(4, "the next first difference: 12 + 46"),
          ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_curve_mean", (cubic5 + line5) / 2, f"{(cubic5 + line5) / 2:.1f}", concept(4, "the average of the curve and the line, a wrong option"), ["c4 set"])
    for name, f in (("line", line5), ("curve", cubic5), ("naive", days5[3])):
        F.toy(f"ch4_miss_{name}", abs(f - days5[4]), f"{abs(f - days5[4]):.0f}", concept(4, f"the {name}'s miss on day 5"),
              ["half1 SECTION 4", "notebook 04", "notes"])
    F.toy("ch4_cups", nephew.cups.tolist(), ", ".join(map(str, nephew.cups)), concept(4, "Mon 3 to Sun 16 Mar 2025; the last seven are hidden"),
          ["notebook 04"])
    seen, hid = nephew.cups.iloc[:7].tolist(), nephew.cups.iloc[7:].tolist()
    mean7 = sum(seen) / 7
    sn_miss = [a - b for a, b in zip(seen, hid)]
    mn_miss = [mean7 - b for b in hid]
    sn_mae, mn_mae = sum(map(abs, sn_miss)) / 7, sum(map(abs, mn_miss)) / 7
    F.toy("ch4_mean7", mean7, f"{mean7:.1f}", concept(4, "the nephew's rule: the mean of the last seven days"), ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_snaive_mae", sn_mae, f"{sn_mae:.1f}", concept(4, "the seasonal naive (same day last week) on the seven hidden days"),
          ["half1 SECTION 4", "notebook 04", "notes"])
    F.toy("ch4_mean7_mae", mn_mae, f"{mn_mae:.1f}", concept(4, "the nephew's mean on the same days"), ["half1 SECTION 4", "notebook 04", "notes"])
    F.toy("ch4_snaive_lean", sum(sn_miss) / 7, f"{sum(sn_miss) / 7:+.1f}", concept(4, "the seasonal naive's lean"), ["notebook 04"])
    F.toy("ch4_mean7_lean", sum(mn_miss) / 7, f"{sum(mn_miss) / 7:+.1f}", concept(4, "the mean's lean"), ["notebook 04"])
    F.toy("ch4_mean7_sunday_miss", mn_miss[-1], f"{mn_miss[-1]:+.1f}", concept(4, "the mean's miss on the hidden Sunday"), ["notebook 04"])
    cans = lambda v: math.ceil(v / CAN)
    sn_cans, mn_cans, true_cans = [cans(v) for v in seen], [cans(mean7)] * 7, [cans(v) for v in hid]
    F.toy("ch4_can", CAN, "40 cups", concept(5, "cups of tea one milk can makes"), ["half1 SECTION 4", "notebook 04", "notes", "c4 set"])
    F.toy("ch4_cans_snaive", sn_cans, ", ".join(map(str, sn_cans)), concept(5, "cans the seasonal naive orders, Mon to Sun"), ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_cans_perfect", true_cans, ", ".join(map(str, true_cans)), concept(5, "cans a forecast that knew the future would order"), ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_cans_mean7", mn_cans, ", ".join(map(str, mn_cans)), concept(5, "cans the nephew's mean orders"), ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_cans_differ_snaive", sum(a != b for a, b in zip(sn_cans, true_cans)), "0",
          concept(5, "days on which the seasonal naive's cans differ from a perfect forecast's"), ["half1 SECTION 4", "notebook 04", "notes"])
    F.toy("ch4_cans_differ_mean7", sum(a != b for a, b in zip(mn_cans, true_cans)), str(sum(a != b for a, b in zip(mn_cans, true_cans))),
          concept(5, "days on which the nephew's cans differ: the Sunday"), ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_spare_can_rs", CAN * UNSOLD_RS, f"Rs {CAN * UNSOLD_RS}", concept(5, "a whole can of milk wasted: 40 cups x Rs 6"), ["half1 SECTION 4", "notebook 04"])
    F.toy("ch4_bar_high_rs", sn_mae * UNSOLD_RS, f"Rs {sn_mae * UNSOLD_RS:.0f}", concept(5, "the seasonal naive's MAE priced if it runs high"), ["half1 SECTION 4", "notebook 04", "notes"])
    F.toy("ch4_bar_low_rs", sn_mae * SHORT_RS, f"Rs {sn_mae * SHORT_RS:.0f}", concept(5, "the same MAE priced if it runs short"), ["half1 SECTION 4", "notebook 04", "notes"])
    F.toy("ch4_weekday_cans", 3, "3 cans", concept(5, "the note: 3 cans a day Monday to Saturday"), ["half1 SECTION 4", "notebook 04", "notes", "c4 set"])
    F.toy("ch4_sunday_cans", 2, "2 cans", concept(5, "the note: 2 cans on Sunday"), ["half1 SECTION 4", "notebook 04", "notes", "c4 set"])
    F.toy("ch4_note_lines", 4, "four lines", concept(5, "the forecast note: number, method, error bar, what would make it wrong"),
          ["half1 SECTION 4", "notebook 04", "notes"])
    out.update(line5=line5, cubic5=cubic5, sn_mae=sn_mae, mn_mae=mn_mae, cans=(sn_cans, mn_cans, true_cans))

    # ---- the case's numbers the concept glimpses and the staffing chapter print
    vendor_gap = S["vendor"]["mae"] - S["aligned"]["mae"]
    bot_gap = S["bot"]["mae"] - S["aligned"]["mae"]
    F.add("good_enough", "bot_gap_shifts", bot_gap / PER_SHIFT, f"{bot_gap / PER_SHIFT:.0f}",
          "the bot's MAE minus festival-aligned's, over 120 shipments a shift", "half2 SECTION 7, notebook 07")
    F.add("good_enough", "vendor_gap", vendor_gap, n(vendor_gap), "the vendor's MAE minus festival-aligned's", "half2 SECTION 7, notebook 07")
    F.add("good_enough", "vendor_gap_shifts", vendor_gap / PER_SHIFT, f"{vendor_gap / PER_SHIFT:.0f}",
          "that gap over 120 shipments a shift", "half2 SECTION 7, notebook 07")
    F.add("good_enough", "error_bar_shifts", S["aligned"]["mae"] / PER_SHIFT, f"about {S['aligned']['mae'] / PER_SHIFT:.0f}",
          "festival-aligned's MAE, 6,615, over 120: shifts a week", "half2 SECTION 7, notes, cheat sheet")
    better = 100
    moved_w = [math.ceil(ahead["aligned"][i] / PER_SHIFT) - math.ceil((ahead["aligned"][i] - better) / PER_SHIFT) for i in WINDOW]
    F.add("good_enough", "better_by", better, "100 shipments", "a rule that beat festival-aligned by this much a week", "half2 SECTION 7, notebook 04, notebook 07")
    F.add("good_enough", "better_saves_rs", better * LATE_RS, f"Rs {better * LATE_RS:,}",
          "the most an MAE 100 lower saves a week: 100 late shipments at Rs 25", "half2 SECTION 7, notebook 07, notes")
    F.add("good_enough", "better_saves_low_rs", better * OVER_RS, f"Rs {better * OVER_RS:,.0f}",
          "the least it saves a week: 100 spare shipments at Rs 5.42", "half2 SECTION 7, notebook 07, notes")
    F.add("good_enough", "better_window_low_rs", 8 * better * OVER_RS, f"Rs {round(8 * better * OVER_RS, -2):,.0f}",
          "the same over the eight window weeks, low end", "half2 SECTION 7, notebook 07")
    F.add("good_enough", "better_window_high_rs", 8 * better * LATE_RS, f"Rs {8 * better * LATE_RS:,}",
          "the same over the eight window weeks, high end", "half2 SECTION 7, notebook 07")
    for late in (LATE_LOW, LATE_RS, LATE_HIGH):       # does the priced ranking survive the ticket's cost ranges?
        for idle in (IDLE_LOW, IDLE_SHIFT_RS, IDLE_HIGH):
            for m in ("aligned", "vendor"):
                c = S[m]["under"] * late + S[m]["over"] * idle / PER_SHIFT
                F.add("sensitivity", f"{m}_late{late}_idle{idle}_rs", c, lakh(c), f"{m}'s hidden-week misses at Rs {late} late and Rs {idle} an idle shift", "half1 S56, transcripts")
    wins = sum(S["vendor"]["under"] * late + S["vendor"]["over"] * idle / PER_SHIFT < S["aligned"]["under"] * late + S["aligned"]["over"] * idle / PER_SHIFT
               for late in (LATE_LOW, LATE_RS, LATE_HIGH) for idle in (IDLE_LOW, IDLE_SHIFT_RS, IDLE_HIGH))
    F.add("sensitivity", "vendor_cheaper_corners", wins, f"{wins} of 9", "cost pairs from the ticket's ranges at which the vendor's misses cost less", "half1 S56, transcripts")
    F.add("good_enough", "better_shifts_moved", moved_w, ", ".join(map(str, moved_w)),
          "shifts such a rule would book differently in each window week, 12 Oct to 30 Nov 2026", "half2 SECTION 7, notebook 07")
    F.add("good_enough", "better_weeks_moved", sum(1 for m in moved_w if m), f"{sum(1 for m in moved_w if m)} of 8",
          "window weeks in which it moves a shift at all", "half2 SECTION 7, notebook 07")
    F.add("good_enough", "peak_raw_shifts", ahead["aligned"][107] / PER_SHIFT, f"{ahead['aligned'][107] / PER_SHIFT:,.1f}",
          "434,928 / 120 before rounding up", "staffing set")
    F.add("good_enough", "peak_round_down", math.floor(ahead["aligned"][107] / PER_SHIFT), f"{math.floor(ahead['aligned'][107] / PER_SHIFT):,}",
          "rounded down, a wrong option that leaves shipments unpacked", "staffing set")
    F.add("good_enough", "fitted_rows", ORIGIN + 1, "91", "the vendor file's fitted rows", "notebook 04")
    F.add("good_enough", "holdout_rows", len(HOLDOUT), "13", "its holdout rows", "notebook 04")
    F.add("good_enough", "forecast_rows", len(HORIZON), "10", "its forecast rows", "notebook 04")
    out.update(moved=moved_w)

    # ---- the hostel mess, the exercises' cameo
    F.toy("mess_weekday_kg", 25, "25 kg", exercise(1, "rice a weekday at the hostel mess"), ["c1 set", "c2 set", "c3 set"])
    F.toy("mess_sunday_kg", 40, "40 kg", exercise(1, "rice on a Sunday, biryani day"), ["c1 set", "c2 set"])
    guest = [v + 2 * k for k in range(4) for v in (190, 186, 194, 238)]
    F.toy("mess_sixteen_weeks", guest, ", ".join(map(str, guest)), exercise(1, "sixteen weeks of rice, a guest dinner every fourth week, 2 kg more each cycle"),
          ["c1 set"])
    F.toy("mess_guest_extra", 238 - 190, "48 kg", exercise(1, "the guest week over an ordinary week"), ["c1 set"])
    F.toy("mess_cycle_climb", 2, "2 kg", exercise(1, "the climb from one cycle to the next"), ["c1 set"])
    F.toy("mess_four_days", [25, 26, 25, 27], "25, 26, 25 and 27 kg", exercise(2, "the last four days at the mess"), ["c2 set"])
    F.toy("mess_last_sunday", 42, "42 kg", exercise(2, "last Sunday at the mess"), ["c2 set"])
    F.toy("mess_drift", 27 + (27 - 25) / 3, "27.7", exercise(2, "drift: 27 plus (27 - 25) / 3"), ["c2 set"])
    F.toy("mess_mean_four", (25 + 26 + 25 + 27) / 4, "25.75", exercise(2, "the four days' mean, a wrong option"), ["c2 set"])
    F.toy("mess_misses", [12, -8, 5, -15, 6], "12, -8, 5, -15 and 6", exercise(3, "five hidden days' misses, kg"), ["c3 set"])
    F.toy("mess_miss_sum", 46, "46", exercise(3, "their sizes added"), ["c3 set"])
    F.toy("mess_mae", 9.2, "9.2", exercise(3, "46 / 5"), ["c3 set"])
    F.toy("mess_rule_misses", [10, 10, 10, -10], "+10, +10 against +10, -10", exercise(3, "two rules' misses for the lean item, cups"), ["c3 set"])
    F.toy("lab_series_x", [50 + 3 * k for k in range(8)], "50, 53, 56", exercise(1, "practice set: a climb"), ["lab set"])
    F.toy("lab_series_y", [50, 50, 70, 50] * 2, "50, 50, 70, 50", exercise(1, "practice set: a repeat of four"), ["lab set"])
    F.toy("lab_series_z", [50, 54, 47, 52, 49, 53, 48, 51], "50, 54, 47, 52", exercise(1, "practice set: a wobble"), ["lab set"])
    F.toy("lab_misses", [9, -6, 14, -3, -4], "9, -6, 14, -3 and -4", exercise(3, "practice set: five misses"), ["lab set"])
    F.toy("lab_miss_sum", 36, "36", exercise(3, "their sizes added"), ["lab set"])
    F.toy("lab_mae", 7.2, "7.2", exercise(3, "36 / 5"), ["lab set"])
    F.toy("lab_signed_mean", 2, "2.0", exercise(3, "the signed misses averaged, a wrong option"), ["lab set"])
    F.toy("lab_rule_miss", 1_000, "1,000", exercise(3, "practice set: two rules each miss by this many shipments a week"), ["lab set"])
    F.toy("lab_rule_high_rs", 1_000 * 5, "Rs 5,000", exercise(3, "always high: 1,000 x Rs 5"), ["lab set"])
    F.toy("lab_rule_low_rs", 1_000 * 30, "Rs 30,000", exercise(3, "always low: 1,000 x Rs 30"), ["lab set"])
    return out


def main():
    DATA.mkdir(parents=True, exist_ok=True)
    weekly, calendar = build_series()
    y = weekly["shipments"].tolist()
    vendor = vendor_rows(y)
    vend = {i: v for i, v, _ in vendor}
    hold = forecasts(y, HOLDOUT, ORIGIN)
    hold["vendor"] = {i: vend[i] for i in HOLDOUT}
    back = forecasts(y, BACK, BACK_ORIGIN)
    ahead = forecasts(y, HORIZON, N_HIST - 1)
    ahead["vendor"] = {i: vend[i] for i in HORIZON}

    weekly.to_csv(DATA / "C2_W04_D05_weekly_shipments_STUDENT.csv", index=False)
    calendar.to_csv(DATA / "C2_W04_D05_calendar_STUDENT.csv", index=False)
    pd.DataFrame([{"week_start": week(i).isoformat(), "vendor_shipments": v, "kind": k}
                  for i, v, k in vendor]).to_csv(DATA / "C2_W04_D05_vendor_forecast_STUDENT.csv", index=False)
    pd.DataFrame([{"item": "idle_packer_shift", "rs": IDLE_SHIFT_RS, "low": IDLE_LOW, "high": IDLE_HIGH},
                  {"item": "late_shipment", "rs": LATE_RS, "low": LATE_LOW, "high": LATE_HIGH}]
                 ).to_csv(DATA / "C2_W04_D05_costs_STUDENT.csv", index=False)
    twelve = [1, 2, 3, 4, 5, 6, 52, 53, 54, 55, 56, 57]
    weekly.iloc[twelve][["week_start", "shipments"]].to_csv(
        DATA / "C2_W04_D05_twelve_rows_STUDENT.csv", index=False)
    monthly, kvendor, kplan, v4sums = build_kalpa()
    monthly.to_csv(DATA / "C2_W04_D05_kalpa_monthly_revenue_STUDENT.csv", index=False)
    kvendor.to_csv(DATA / "C2_W04_D05_kalpa_vendor_forecast_STUDENT.csv", index=False)
    kplan.to_csv(DATA / "C2_W04_D05_kalpa_plan_line_STUDENT.csv", index=False)
    for stale in ("C2_W04_D05_kalpa_twelve_rows_STUDENT.csv",):
        (DATA / stale).unlink(missing_ok=True)
    stall = build_stall()
    stall.to_csv(DATA / "C2_W04_D05_chai_stall_daily_STUDENT.csv", index=False)
    tables = stall_tables(stall)
    for name, t in zip(("fortnights", "week", "hidden_days", "nephew", "what_ifs"), tables):
        t.to_csv(DATA / f"C2_W04_D05_chai_stall_{name}_STUDENT.csv", index=False)

    F = Facts()
    S = {m: score(f, y, HOLDOUT) for m, f in hold.items()}
    B = {m: score(back[m], y, BACK) for m in ("bot", "finance", "aligned")}

    # ---- the ticket
    F.add("ticket", "history_weeks", N_HIST, "104", "rows in weekly_shipments", "every ticket")
    F.add("ticket", "first_week", week(0).isoformat(), "30 Sep 2024", "the first week_start", "ticket")
    F.add("ticket", "last_week", week(N_HIST - 1).isoformat(), "21 Sep 2026", "the last week_start", "ticket")
    lo, hi = min(y[6:13]), max(y[6:13])
    F.add("ticket", "ordinary_week", ORDINARY, "about 210,000",
          f"the level of an ordinary week in late 2024 before season and noise; the weeks of 11 Nov to 23 Dec 2024 run {n(lo)} to {n(hi)}",
          "ticket")
    for o, r in FESTIVE.items():
        F.add("ticket", f"festive_ratio_{o:+d}".replace("+", "p").replace("-", "m"), r, f"{r}",
              f"shipments {abs(o)} week(s) {'before' if o < 0 else 'after'} Diwali's week over the ordinary week"
              if o else "shipments in Diwali's week over the ordinary week", "ticket, chapter 1")
    F.add("ticket", "per_shift", PER_SHIFT, "120", "shipments a packer packs in a shift (target)", "ticket, chapter 3")
    F.add("ticket", "window_weeks", len(WINDOW), "eight", "12 Oct to 30 Nov 2026", "ticket")
    F.add("ticket", "horizon_weeks", len(HORIZON), "ten", "28 Sep to 30 Nov 2026, from the origin of 21 Sep 2026", "chapter 3")
    F.add("ticket", "holdout_weeks", len(HOLDOUT), "thirteen", "29 Jun to 21 Sep 2026", "chapter 2")
    F.add("ticket", "training_weeks", ORIGIN + 1, "91", "30 Sep 2024 to 22 Jun 2026", "chapter 2")
    F.add("ticket", "vendor_promise_pct", 22, "22 percent", "the vendor's 2026 window over the same calendar weeks of 2025", "ticket")
    F.add("ticket", "finance_rule_pct", 4, "4 percent", "finance's rule: last year's same calendar weeks plus 4 percent", "ticket")
    F.add("ticket", "points_apart", 18, "eighteen points", "22 minus 4", "ticket")
    F.add("ticket", "idle_shift_rs", IDLE_SHIFT_RS, "Rs 650", "an idle packer-shift, assumption", "ticket, chapter 3")
    F.add("ticket", "idle_shift_low", IDLE_LOW, "Rs 500", "its range, low", "ticket")
    F.add("ticket", "idle_shift_high", IDLE_HIGH, "Rs 800", "its range, high", "ticket")
    F.add("ticket", "late_rs", LATE_RS, "Rs 25", "a late shipment, assumption", "ticket, chapter 3")
    F.add("ticket", "late_low", LATE_LOW, "Rs 15", "its range, low", "ticket")
    F.add("ticket", "late_high", LATE_HIGH, "Rs 40", "its range, high", "ticket")
    F.add("ticket", "over_rs", OVER_RS, "Rs 5.42", "650 / 120, the cost of one shipment planned and not shipped", "chapter 3")
    F.add("ticket", "cost_ratio", LATE_RS / OVER_RS, "4.6", "25 / 5.42", "chapter 3")
    F.add("ticket", "plan_quantile", QUANTILE, "0.82", "25 / (25 + 5.42)", "chapter 3")
    F.add("ticket", "quantile_scale_rs", LATE_RS + OVER_RS, f"Rs {LATE_RS + OVER_RS:.2f}",
          "the two costs added: the priced miss is this times the pinball loss at 0.82", "transcripts")
    F.add("ticket", "cost_sum", LATE_RS + OVER_RS, "30.42", "25 + 5.42", "chapter 3")
    F.add("ticket", "diwali_2024", "2024-10-31", "Thursday 31 October 2024", "F5; the week of 28 Oct 2024", "ticket")
    F.add("ticket", "diwali_2025", "2025-10-20", "Monday 20 October 2025", "F5; the week of 20 Oct 2025", "ticket")
    F.add("ticket", "diwali_2026", "2026-11-08", "Sunday 8 November 2026", "F5 and facts.yaml; the week of 2 Nov 2026", "ticket")
    F.add("ticket", "diwali_move_weeks", 2, "two weeks", "the week of 2 Nov 2026 is 54 weeks after the week of 20 Oct 2025", "chapter 1, 3")
    F.add("ticket", "diwali_move_2025_weeks", 1, "one week", "the week of 20 Oct 2025 is 51 weeks after the week of 28 Oct 2024", "chapter 1")

    # ---- the twelve rows and the hand count
    for i in twelve:
        F.add("twelve_rows", f"row_{week(i):%Y_%m_%d}", y[i], n(y[i]), f"shipments, week of {dmy(i)}", "chapter 1, sheet panel 2")
    F.add("hand_count", "diwali25_actual", y[55], n(y[55]), "shipments, week of 20 Oct 2025", "chapter 1")
    F.add("hand_count", "naive", y[54], n(y[54]), "the week before, 13 Oct 2025", "chapter 1")
    F.add("hand_count", "bot", y[3], n(y[3]), "52 weeks back, 21 Oct 2024, one week before Diwali 2024", "chapter 1")
    fa55 = round(y[4] * DRIFT)
    F.add("hand_count", "aligned_source", y[4], n(y[4]), "Diwali 2024's own week, 28 Oct 2024", "chapter 1")
    F.add("hand_count", "aligned", fa55, n(fa55), "28 Oct 2024 times 1.04", "chapter 1")
    F.add("hand_count", "naive_miss", y[54] - y[55], n(y[54] - y[55]), "naive minus actual", "chapter 1")
    F.add("hand_count", "bot_miss", y[3] - y[55], n(y[3] - y[55]), "bot minus actual", "chapter 1")
    F.add("hand_count", "aligned_miss", fa55 - y[55], n(fa55 - y[55]), "aligned minus actual", "chapter 1")
    F.add("hand_count", "aligned_nogrowth_miss", y[4] - y[55], n(y[4] - y[55]),
          "festival-aligned with no growth, as October 2025 could run it: 28 Oct 2024 minus the actual", "half1 S44, notebook 05, notes")
    F.add("hand_count", "peak_2024", y[2], n(y[2]), "the 2024 peak, week of 14 Oct 2024, two weeks before Diwali", "chapter 1")
    F.add("hand_count", "peak_2025", y[53], n(y[53]), "the 2025 peak, week of 6 Oct 2025, two weeks before Diwali", "chapter 1")
    F.add("hand_count", "bot_peak_2025", y[2], n(y[2]), "the bot's biggest 2025 week is 13 Oct 2025, a copy of 14 Oct 2024", "chapter 1")
    F.add("hand_count", "bot_2026_source", y[55], n(y[55]), "the week of 20 Oct 2025 copied 52 weeks on lands on 19 Oct 2026", "chapter 1")
    F.add("hand_count", "bot_2026_peak", y[53], n(y[53]), "the 2025 peak copied 52 weeks on lands on 5 Oct 2026", "chapter 3")

    # ---- the series
    growth = sum(y[52:104]) / sum(y[0:52]) - 1
    growth_train = sum(y[52:91]) / sum(y[0:39]) - 1
    F.add("series", "growth_measured", growth, pct(growth), "the second year's shipments over the first year's, minus one", "chapter 2, 3")
    F.add("series", "growth_train", growth_train, pct(growth_train),
          "the 39 training weeks with a year behind them over the same weeks a year earlier", "notebook 02")
    F.add("series", "year1_total", sum(y[0:52]), n(sum(y[0:52])), "shipments, 30 Sep 2024 to 22 Sep 2025", "notebook 02")
    F.add("series", "year2_total", sum(y[52:104]), n(sum(y[52:104])), "shipments, 29 Sep 2025 to 21 Sep 2026", "notebook 02")
    F.add("series", "origin_week", y[ORIGIN], n(y[ORIGIN]), "shipments, week of 22 Jun 2026, the hold-out's origin", "chapter 2")
    F.add("series", "first_week", y[0], n(y[0]), "shipments, week of 30 Sep 2024", "chapter 2")
    slope = (y[ORIGIN] - y[0]) / ORIGIN
    F.add("series", "drift_slope", slope, f"{slope:.0f}", "(22 Jun 2026 minus 30 Sep 2024) / 90, shipments a week", "chapter 2")
    F.add("series", "aug_sale_2026", y[97], n(y[97]), "shipments, week of 10 Aug 2026, the August sale", "chapter 2")
    F.add("series", "aug_sale_2025", y[45], n(y[45]), "shipments, week of 11 Aug 2025", "chapter 2")
    F.add("series", "peak_overtime_2025", int(weekly.loc[53, "overtime_shifts"]), n(weekly.loc[53, "overtime_shifts"]),
          "overtime shifts in the week of 6 Oct 2025", "chapter 3 caveats")
    F.add("series", "ordinary_overtime", int(weekly.loc[60, "overtime_shifts"]), n(weekly.loc[60, "overtime_shifts"]),
          "overtime shifts in the week of 24 Nov 2025", "chapter 3 caveats")
    hold_mean = sum(y[i] for i in HOLDOUT) / len(HOLDOUT)
    F.add("series", "holdout_mean", hold_mean, n(hold_mean), "mean weekly shipments on the hold-out", "chapter 2")

    # ---- the hold-out
    names = {"naive": "naive", "drift": "drift", "bot": "the house bot (same week last year)",
             "finance": "finance's rule", "aligned": "the festival-aligned baseline", "vendor": "the vendor"}
    for m, s in S.items():
        F.add("holdout", f"{m}_mae", s["mae"], n(s["mae"]), f"mean absolute error of {names[m]} on the 13 hold-out weeks", "chapter 2")
        F.add("holdout", f"{m}_high_weeks", s["high_weeks"], f"{s['high_weeks']} of 13", f"weeks {names[m]} forecast above the actual", "chapter 2")
        F.add("holdout", f"{m}_over", s["over"], n(s["over"]), f"shipments {names[m]} forecast above the actual, summed", "chapter 2")
        F.add("holdout", f"{m}_under", s["under"], n(s["under"]), f"shipments {names[m]} forecast below the actual, summed", "chapter 2")
        F.add("holdout", f"{m}_idle_rs", s["idle_rs"], lakh(s["idle_rs"]), "the over-forecast times Rs 5.42", "chapter 2")
        F.add("holdout", f"{m}_late_rs", s["late_rs"], lakh(s["late_rs"]), "the under-forecast times Rs 25", "chapter 2")
        F.add("holdout", f"{m}_cost_rs", s["cost_rs"], lakh(s["cost_rs"]), "idle plus late, in rupees", "chapter 2")
    F.add("holdout", "vendor_over_aligned_pct", S["vendor"]["mae"] / S["aligned"]["mae"] - 1,
          pct(S["vendor"]["mae"] / S["aligned"]["mae"] - 1, 0), "vendor MAE over the aligned MAE, minus one", "chapter 2")
    F.add("holdout", "vendor_over_bot_pct", S["vendor"]["mae"] / S["bot"]["mae"] - 1,
          pct(S["vendor"]["mae"] / S["bot"]["mae"] - 1, 0), "vendor MAE over the bot's, minus one", "chapter 2")
    F.add("holdout", "bot_over_aligned", S["bot"]["mae"] - S["aligned"]["mae"], n(S["bot"]["mae"] - S["aligned"]["mae"]),
          "the bot's MAE minus the aligned MAE", "chapter 2")
    vpct = [(hold["vendor"][i] - y[i]) / y[i] for i in HOLDOUT]
    early, late = sum(vpct[:6]) / 6, sum(vpct[7:]) / 6
    F.add("holdout", "vendor_miss_week1", hold["vendor"][HOLDOUT[0]] - y[HOLDOUT[0]], n(hold["vendor"][HOLDOUT[0]] - y[HOLDOUT[0]]),
          "the vendor's miss in hidden week 1, 29 Jun 2026, too high", "notes, the reveal GIF")
    F.add("holdout", "bot_miss_week1", y[HOLDOUT[0]] - hold["bot"][HOLDOUT[0]], n(y[HOLDOUT[0]] - hold["bot"][HOLDOUT[0]]),
          "the house bot's miss in hidden week 1, too low", "notes, the reveal GIF")
    F.add("holdout", "vendor_mean_high_pct", sum(vpct) / 13, pct(sum(vpct) / 13), "the vendor's mean error over the actual, in percent", "chapter 2")
    F.add("holdout", "vendor_first6_pct", early, pct(early), "its mean error in hidden weeks 1 to 6, 29 Jun to 3 Aug 2026", "chapter 2")
    F.add("holdout", "vendor_last6_pct", late, pct(late), "its mean error in hidden weeks 8 to 13, 17 Aug to 21 Sep 2026", "chapter 2")
    errs = [(y[i] - hold["aligned"][i]) / hold["aligned"][i] for i in HOLDOUT]
    cushion = round(quantile(errs, QUANTILE), 3)       # the planner rounds it to a tenth of a percent
    F.add("holdout", "aligned_low_weeks", 13 - S["aligned"]["high_weeks"], f"{13 - S['aligned']['high_weeks']}", "weeks the aligned baseline sat below the actual", "chapter 2 second route")
    for m in ("aligned", "finance", "bot", "drift", "naive", "vendor"):
        mp = sum(abs(hold[m][i] - y[i]) / y[i] for i in HOLDOUT) / len(HOLDOUT)
        F.add("holdout", f"{m}_mape", mp, pct(mp, 2), f"{m}'s MAPE on the 13 hidden weeks", "notebook 06, half2 D2")
    F.add("holdout", "aligned_err_min_pct", min(errs), pct(min(errs)), "the aligned baseline's lowest error, actual minus forecast over forecast", "chapter 3")
    F.add("holdout", "aligned_err_max_pct", max(errs), pct(max(errs)), "its highest error", "chapter 3")
    F.add("holdout", "cushion_pct", cushion, pct(cushion), "the 0.82 quantile of those 13 errors, rounded to a tenth of a percent", "chapter 3")
    F.add("holdout", "cushion_factor", 1 + cushion, f"{1 + cushion:.3f}", "the plan's multiplier", "chapter 3")
    raised = {i: round(hold["aligned"][i] * (1 + cushion)) for i in HOLDOUT}
    R = score(raised, y, HOLDOUT)
    F.add("holdout", "raised_mae", R["mae"], n(R["mae"]), "the aligned baseline raised by the cushion, on the same weeks", "chapter 3")
    F.add("holdout", "raised_cost_rs", R["cost_rs"], lakh(R["cost_rs"]), "its errors priced, on the weeks the cushion was read from", "chapter 3")
    F.add("holdout", "raised_high_weeks", R["high_weeks"], f"{R['high_weeks']} of 13", "weeks the raised baseline sits above the actual", "chapter 3")
    F.add("holdout", "aligned_abs_total", S["aligned"]["over"] + S["aligned"]["under"],
          n(S["aligned"]["over"] + S["aligned"]["under"]), "the aligned baseline's 13 misses, signs dropped, summed", "chapter 2 second route")
    F.add("holdout", "share_short_pct", 1 - QUANTILE, pct(1 - QUANTILE, 0), "one minus the plan share", "chapter 3")
    srt = sorted(errs)
    F.add("holdout", "above_sorted_pct", [round(e * 100, 1) for e in srt],
          ", ".join(f"{e * 100:.1f}" for e in srt), "demand above festival-aligned on the 13 hidden weeks, percent, smallest first", "chapter 3 cushion")
    F.add("holdout", "above_10th_pct", srt[9], pct(srt[9]), "the 10th smallest of the 13", "chapter 3 cushion")
    F.add("holdout", "above_11th_pct", srt[10], pct(srt[10]), "the 11th smallest of the 13", "chapter 3 cushion")
    F.add("holdout", "weeks_covered", sum(e <= cushion for e in errs), f"{sum(e <= cushion for e in errs)} of 13",
          "hidden weeks whose demand the raised forecast covers", "chapter 3 cushion")
    F.add("holdout", "toy_late_side", 18 * LATE_RS, f"Rs {18 * LATE_RS}", "18 short weeks in 100 x Rs 25: one more shipment of plan saves this", "chapter 3 derivation")
    F.add("holdout", "toy_idle_side", 82 * OVER_RS, f"Rs {82 * OVER_RS:.0f}", "82 covered weeks in 100 x Rs 5.42: one more shipment of plan wastes this", "chapter 3 derivation")
    F.add("holdout", "toy_weeks", [18, 82, 100], "18, 82 and 100", "the derivation's weeks: short, covered and all", "chapter 3 derivation")
    F.add("holdout", "bot_low_weeks", 13 - S["bot"]["high_weeks"], f"{13 - S['bot']['high_weeks']} of 13", "weeks the bot sat below the actual", "chapter 2")
    vfit = max(abs(vend[i] - y[i]) / y[i] for i in range(ORIGIN + 1))
    F.add("holdout", "vendor_fit_max_pct", vfit, pct(vfit), "the vendor's largest miss on its 91 fitted weeks", "chapter 2")
    for i in HOLDOUT:
        F.add("holdout_weeks", f"actual_{week(i):%m_%d}", y[i], n(y[i]), f"shipments, week of {dmy(i)}", "chapter 2 error table")
        for m in ("drift", "bot", "aligned", "vendor"):
            F.add("holdout_weeks", f"{m}_{week(i):%m_%d}", hold[m][i], n(hold[m][i]), f"{names[m]}, week of {dmy(i)}", "chapter 2 error table")
        F.add("holdout_weeks", f"aligned_miss_{week(i):%m_%d}", hold["aligned"][i] - y[i], n(hold["aligned"][i] - y[i]),
              f"aligned minus actual, week of {dmy(i)}", "chapter 2 second route")

    # ---- the four-week hold-out (fallback part 1, take-home): the origin moves to 24 Aug 2026
    last4 = range(100, 104)
    s4 = forecasts(y, last4, 99)
    s4["vendor"] = {i: vend[i] for i in last4}
    S4 = {m: score(f, y, last4) for m, f in s4.items()}
    F.add("holdout_4", "origin_week", y[99], n(y[99]), "shipments, week of 24 Aug 2026, the four-week test's origin", "fallback, take-home")
    for m, sc in S4.items():
        F.add("holdout_4", f"{m}_mae", sc["mae"], n(sc["mae"]), f"{names[m]} on 31 Aug to 21 Sep 2026", "fallback, take-home")
        F.add("holdout_4", f"{m}_cost_rs", sc["cost_rs"], lakh(sc["cost_rs"], 2),
              "its four misses priced, to two places so an exact half reads the same by hand and in code", "fallback, take-home")
        F.add("holdout_4", f"{m}_high_weeks", sc["high_weeks"], f"{sc['high_weeks']} of 4", "weeks too high", "take-home")
    F.add("holdout_4", "vendor_over_aligned_pct", S4["vendor"]["mae"] / S4["aligned"]["mae"] - 1,
          pct(S4["vendor"]["mae"] / S4["aligned"]["mae"] - 1, 0), "vendor over aligned on four weeks", "take-home")
    for i in last4:
        F.add("holdout_4_weeks", f"naive_miss_{week(i):%m_%d}", s4["naive"][i] - y[i], n(s4["naive"][i] - y[i]),
              f"naive minus actual from 24 Aug, week of {dmy(i)}", "take-home self-check")
    F.add("holdout_4", "origin_position", 99, "99", "the origin's position in the 104 rows, counting from 0; drift's step divides by it", "take-home")
    F.add("holdout_4", "hold_mean", sum(y[i] for i in last4) / 4, n(sum(y[i] for i in last4) / 4),
          "the four hidden weeks' average shipments", "take-home self-check")
    F.add("holdout_4", "bot_move", S["bot"]["mae"] - S4["bot"]["mae"], n(S["bot"]["mae"] - S4["bot"]["mae"]),
          "the house bot's MAE on thirteen weeks minus on four", "take-home self-check")
    F.add("holdout_4", "aligned_move", S4["aligned"]["mae"] - S["aligned"]["mae"], n(S4["aligned"]["mae"] - S["aligned"]["mae"]),
          "festival-aligned's MAE on four weeks minus on thirteen", "take-home self-check")
    F.add("holdout_4", "vendor_steps", [10, 13], "10 to 13", "weeks ahead of 22 Jun 2026 that the vendor's four rows forecast", "take-home self-check")
    F.add("saturday", "minutes", [120, 20, 20, 60, 30, 30, 20], "120, 20, 20, 60, 30, 30 and 20",
          "Saturday's parts in minutes: paper, break, marking, discussion, transfer drill, mock interviews, bridge (spine section 10; facts.yaml saturday-w4-shape)", "Saturday preview")

    # ---- the rolling origin by hand on the twelve rows (fallback part 2)
    for i in range(53, 58):
        F.add("rolling_origin", f"naive_{week(i):%m_%d}", y[i - 1], n(y[i - 1]), f"one week ahead from {dmy(i - 1)}", "fallback part 2")
        F.add("rolling_origin", f"naive_miss_{week(i):%m_%d}", y[i - 1] - y[i], n(y[i - 1] - y[i]), "naive minus actual", "fallback part 2")
        fa = round(y[i - 51] * DRIFT)
        F.add("rolling_origin", f"aligned_{week(i):%m_%d}", fa, n(fa), f"festival-aligned for {dmy(i)}", "fallback part 2")
        F.add("rolling_origin", f"aligned_miss_{week(i):%m_%d}", fa - y[i], n(fa - y[i]), "aligned minus actual", "fallback part 2")
    rn = sum(abs(y[i - 1] - y[i]) for i in range(53, 58)) / 5
    ra = sum(abs(round(y[i - 51] * DRIFT) - y[i]) for i in range(53, 58)) / 5
    F.add("rolling_origin", "naive_mae", rn, n(rn), "naive's five one-week-ahead misses, averaged", "fallback part 2")
    F.add("rolling_origin", "aligned_mae", ra, n(ra), "festival-aligned's five misses, averaged", "fallback part 2")
    F.add("rolling_origin", "ratio", rn / ra, f"about {rn / ra:.0f}", "naive's average miss over festival-aligned's", "fallback part 2")
    for i in range(53, 58):                           # the same five steps with no growth, which October 2025 could not measure
        F.add("rolling_origin", f"aligned_nogrowth_{week(i):%m_%d}", y[i - 51], n(y[i - 51]), f"festival-aligned with no growth for {dmy(i)}", "fallback part 2")
        F.add("rolling_origin", f"aligned_nogrowth_miss_{week(i):%m_%d}", y[i - 51] - y[i], n(y[i - 51] - y[i]), "that minus actual", "fallback part 2")
    ra0 = sum(abs(y[i - 51] - y[i]) for i in range(53, 58)) / 5
    F.add("rolling_origin", "aligned_nogrowth_mae", ra0, n(ra0), "festival-aligned's five misses with no growth, averaged", "fallback part 2")
    F.add("rolling_origin", "ratio_nogrowth", rn / ra0, f"about {rn / ra0:.1f}", "naive's average miss over that", "fallback part 2")

    # ---- the 2025 festive back-test
    for m, s in B.items():
        F.add("backtest_2025", f"{m}_mae", s["mae"], n(s["mae"]), f"{names[m]} on 29 Sep to 17 Nov 2025, forecast from 22 Sep 2025", "chapter 3")
        F.add("backtest_2025", f"{m}_over", s["over"], n(s["over"]), "shipments forecast above the actual", "chapter 3")
        F.add("backtest_2025", f"{m}_under", s["under"], n(s["under"]), "shipments forecast below the actual", "chapter 3")
        F.add("backtest_2025", f"{m}_idle_rs", s["idle_rs"], lakh(s["idle_rs"]), "over times Rs 5.42", "chapter 3")
        F.add("backtest_2025", f"{m}_late_rs", s["late_rs"], lakh(s["late_rs"]), "under times Rs 25", "chapter 3")
        F.add("backtest_2025", f"{m}_cost_rs", s["cost_rs"], lakh(s["cost_rs"]), "idle plus late", "chapter 3")
    flat = sum(abs(y[aligned_source(i)] - y[i]) for i in BACK) / len(BACK)
    flat_late = sum(max(0, y[i] - y[aligned_source(i)]) for i in BACK) * LATE_RS
    flat_idle = sum(max(0, y[aligned_source(i)] - y[i]) for i in BACK) * OVER_RS
    F.add("backtest_2025", "aligned_nogrowth_cost_rs", flat_late + flat_idle, lakh(flat_late + flat_idle),
          "festival-aligned with no growth on 2025's festival, priced", "chapter 3 notebook")
    F.add("backtest_2025", "aligned_nogrowth_mae", flat, n(flat),
          "festival-aligned on 2025's festival with no growth added, as a planner in September 2025 could run it", "chapter 3")
    for i in BACK:
        F.add("backtest_weeks", f"actual_{week(i):%m_%d}", y[i], n(y[i]), f"shipments, week of {dmy(i)}", "chapter 3")
        for m in ("bot", "aligned"):
            F.add("backtest_weeks", f"{m}_{week(i):%m_%d}", back[m][i], n(back[m][i]), f"{names[m]}, week of {dmy(i)}", "chapter 3")

    # ---- the 2026 festive window against both 2025 windows
    cal = sum(y[i - 52] for i in WINDOW)
    fest = sum(y[aligned_source(i)] for i in WINDOW)
    F.add("window_2026", "calendar_2025_total", cal, n(cal), "shipments, 13 Oct to 1 Dec 2025, the same calendar weeks", "chapter 3")
    F.add("window_2026", "festival_2025_total", fest, n(fest), "shipments, 29 Sep to 17 Nov 2025, the same weeks counted from Diwali", "chapter 3")
    F.add("window_2026", "festival_over_calendar_pct", fest / cal - 1, pct(fest / cal - 1), "the two 2025 windows apart", "chapter 3")
    totals = {}
    for m in ("bot", "finance", "vendor", "aligned"):
        t = sum(ahead[m][i] for i in WINDOW)
        totals[m] = t
        F.add("window_2026", f"{m}_total", t, n(t), f"{names[m]}, 12 Oct to 30 Nov 2026", "chapter 3")
        F.add("window_2026", f"{m}_vs_calendar_pct", t / cal - 1, pct(t / cal - 1), "over the calendar window", "chapter 3")
        F.add("window_2026", f"{m}_vs_festival_pct", t / fest - 1, pct(t / fest - 1), "over the festival-aligned window", "chapter 3")
    F.add("window_2026", "vendor_over_aligned_pct", totals["vendor"] / totals["aligned"] - 1,
          pct(totals["vendor"] / totals["aligned"] - 1), "the vendor's window total over the aligned total", "chapter 3")
    F.add("window_2026", "finance_under_aligned", totals["aligned"] - totals["finance"],
          n(totals["aligned"] - totals["finance"]), "aligned total minus finance's", "chapter 3")
    F.add("window_2026", "finance_under_aligned_pct", totals["finance"] / totals["aligned"] - 1,
          pct(totals["finance"] / totals["aligned"] - 1), "finance's total over the aligned total", "chapter 3")
    for i in HORIZON:
        for m in ("bot", "finance", "vendor", "aligned"):
            F.add("window_weeks", f"{m}_{week(i):%m_%d}", ahead[m][i], n(ahead[m][i]), f"{names[m]}, week of {dmy(i)}", "chapter 3")
    plan = {i: round(ahead["aligned"][i] * (1 + cushion)) for i in WINDOW}
    shifts = {i: math.ceil(plan[i] / PER_SHIFT) for i in WINDOW}
    base_shifts = {i: math.ceil(ahead["aligned"][i] / PER_SHIFT) for i in WINDOW}
    for i in WINDOW:
        F.add("plan_weeks", f"plan_{week(i):%m_%d}", plan[i], n(plan[i]), f"the aligned forecast raised by the cushion, week of {dmy(i)}", "chapter 3, half2")
        F.add("plan_weeks", f"shifts_{week(i):%m_%d}", shifts[i], n(shifts[i]), "plan / 120, rounded up", "chapter 3, half2")
        F.add("plan_weeks", f"base_shifts_{week(i):%m_%d}", base_shifts[i], n(base_shifts[i]), "aligned forecast / 120, rounded up", "chapter 3")
    F.add("plan", "plan_total", sum(plan.values()), n(sum(plan.values())), "the plan's eight weeks", "chapter 3")
    F.add("plan", "shifts_total", sum(shifts.values()), n(sum(shifts.values())), "packer shifts over the eight weeks", "chapter 3, half2")
    F.add("plan", "base_shifts_total", sum(base_shifts.values()), n(sum(base_shifts.values())), "shifts at the unraised forecast", "chapter 3")
    F.add("plan", "extra_shifts", sum(shifts.values()) - sum(base_shifts.values()),
          n(sum(shifts.values()) - sum(base_shifts.values())), "the cushion's shifts", "chapter 3")
    F.add("plan", "extra_shifts_rs", (sum(shifts.values()) - sum(base_shifts.values())) * IDLE_SHIFT_RS,
          lakh((sum(shifts.values()) - sum(base_shifts.values())) * IDLE_SHIFT_RS), "the cushion's shifts at Rs 650, if all sat idle", "chapter 3")
    peak = max(WINDOW, key=lambda i: plan[i])
    F.add("plan", "peak_week_shifts", shifts[peak], n(shifts[peak]), f"shifts in the plan's biggest week, {dmy(peak)}", "chapter 3")
    mae_a = S["aligned"]["mae"]
    F.add("error_bar", "week_shipments", mae_a, n(mae_a), "the aligned baseline's hold-out MAE, a week", "chapter 3")
    F.add("error_bar", "week_idle_rs", mae_a * OVER_RS, f"about Rs {round(mae_a * OVER_RS / 100) * 100:,}",
          "a week's MAE too high, priced: 6,615 x Rs 650 / 120, to the nearest hundred", "chapter 3")
    F.add("error_bar", "week_late_rs", mae_a * LATE_RS, lakh(mae_a * LATE_RS, 2), "a week's MAE too low, priced: 6,615 x Rs 25", "chapter 3")
    F.add("error_bar", "window_shipments", mae_a * 8, n(mae_a * 8), "eight weeks of MAE", "chapter 3")
    F.add("error_bar", "window_idle_rs", mae_a * 8 * OVER_RS, lakh(mae_a * 8 * OVER_RS), "eight weeks too high, priced", "chapter 3")
    F.add("error_bar", "window_late_rs", mae_a * 8 * LATE_RS, lakh(mae_a * 8 * LATE_RS), "eight weeks too low, priced", "chapter 3")
    F.add("error_bar", "festive_mae_2025", B["aligned"]["mae"], n(B["aligned"]["mae"]), "the aligned baseline's MAE on the 2025 festival", "chapter 3")
    ahead["plan"] = plan
    names["plan"] = "the plan"
    for m in ("bot", "finance", "vendor", "plan"):
        over = sum(max(0, ahead[m][i] - ahead["aligned"][i]) for i in WINDOW)
        under = sum(max(0, ahead["aligned"][i] - ahead[m][i]) for i in WINDOW)
        F.add("scenario_2026", f"{m}_over", over, n(over), f"{names[m]} above the aligned forecast, eight weeks", "chapter 3")
        F.add("scenario_2026", f"{m}_under", under, n(under), f"{names[m]} below the aligned forecast, eight weeks", "chapter 3")
        F.add("scenario_2026", f"{m}_cost_rs", over * OVER_RS + under * LATE_RS, lakh(over * OVER_RS + under * LATE_RS),
              "if demand follows the festival-aligned forecast: idle at Rs 5.42, late at Rs 25", "chapter 3")

    # ---- the interview room: the lines a hire-grade answer needs after the interviewer's cold read
    for m in ("aligned", "finance", "bot", "vendor", "naive", "drift"):
        own = [(y[i] - hold[m][i]) / hold[m][i] for i in HOLDOUT]
        c = round(quantile(own, QUANTILE), 3)
        rc = score({i: round(hold[m][i] * (1 + c)) for i in HOLDOUT}, y, HOLDOUT)
        F.add("interview", f"own_cushion_{m}_pct", c, pct(c), f"{names[m]}'s own 0.82 point on the 13 hidden weeks", "transcripts")
        F.add("interview", f"own_raised_cost_{m}_rs", rc["cost_rs"], lakh(rc["cost_rs"]),
              f"{names[m]} moved to its own 0.82 point, its 13 misses priced on the same weeks", "transcripts")
    bias = sum(hold["vendor"][i] - y[i] for i in HOLDOUT) / len(HOLDOUT)
    F.add("interview", "vendor_bias", bias, n(bias), "the vendor's mean signed miss on the hidden weeks, too high", "transcripts")
    fin_shifts = sum(math.ceil(ahead["finance"][i] / PER_SHIFT) for i in WINDOW)
    F.add("interview", "finance_shifts_total", fin_shifts, n(fin_shifts), "finance's rule / 120, rounded up, over the eight weeks", "transcripts")
    F.add("interview", "plan_over_finance_shifts", sum(shifts.values()) - fin_shifts, n(sum(shifts.values()) - fin_shifts),
          "the plan's shifts minus finance's", "transcripts")
    F.add("interview", "plan_over_finance_rs", (sum(shifts.values()) - fin_shifts) * IDLE_SHIFT_RS,
          lakh((sum(shifts.values()) - fin_shifts) * IDLE_SHIFT_RS), "those shifts at Rs 650", "transcripts")
    pk = 107                                            # the week of 19 Oct 2026, the plan's busiest
    lo_d, hi_d = ahead["aligned"][pk] * (1 + min(errs)), ahead["aligned"][pk] * (1 + max(errs))
    F.add("interview", "peak_demand_low", lo_d, n(lo_d), "19 Oct 2026 if demand lands as far below the forecast as the lowest hidden week", "transcripts")
    F.add("interview", "peak_demand_high", hi_d, n(hi_d), "19 Oct 2026 if demand lands as far above as the highest hidden week", "transcripts")
    F.add("interview", "peak_low_spare_rs", (plan[pk] - lo_d) * OVER_RS, lakh((plan[pk] - lo_d) * OVER_RS),
          "the plan's spare shipments at the low end, at Rs 5.42", "transcripts")
    F.add("interview", "peak_high_late_rs", (hi_d - plan[pk]) * LATE_RS, lakh((hi_d - plan[pk]) * LATE_RS),
          "the plan's late shipments at the high end, at Rs 25", "transcripts")
    F.add("interview", "peak_low_shifts", math.ceil(lo_d / PER_SHIFT), n(math.ceil(lo_d / PER_SHIFT)), "shifts the low end needs", "transcripts")
    F.add("error_range", "peak_low_spare_rs", (ahead["aligned"][pk] - lo_d) * OVER_RS, lakh((ahead["aligned"][pk] - lo_d) * OVER_RS),
          "booked at the forecast, the week of 19 Oct 2026's spare shipments at the range's low end, at Rs 5.42", "half2 S7, notes, staffing note")
    F.add("error_range", "peak_high_late_rs", (hi_d - ahead["aligned"][pk]) * LATE_RS, lakh((hi_d - ahead["aligned"][pk]) * LATE_RS),
          "booked at the forecast, its late shipments at the range's high end, at Rs 25", "half2 S7, notes, staffing note")
    F.add("error_range", "mae_share_of_level", S["aligned"]["mae"] / (sum(y[i] for i in HOLDOUT) / len(HOLDOUT)),
          pct(S["aligned"]["mae"] / (sum(y[i] for i in HOLDOUT) / len(HOLDOUT))), "festival-aligned's MAE over the hidden weeks' average week", "half2 S7, notes")
    F.add("interview", "peak_high_shifts", math.ceil(hi_d / PER_SHIFT), n(math.ceil(hi_d / PER_SHIFT)), "shifts the high end needs", "transcripts")
    srt_e = sorted(errs)
    pos = QUANTILE * (len(errs) + 1)
    weibull = srt_e[int(pos) - 1] + (pos - int(pos)) * (srt_e[int(pos)] - srt_e[int(pos) - 1])
    def peak_cost(c):
        p_ = ahead["aligned"][pk] * (1 + c)
        tot = 0
        for e in errs:
            d = ahead["aligned"][pk] * (1 + e)
            tot += max(0, p_ - d) * OVER_RS + max(0, d - p_) * LATE_RS
        return tot / len(errs)
    F.add("interview", "peak_cost_at_cushion_rs", peak_cost(cushion), lakh(peak_cost(cushion)),
          "the week of 19 Oct 2026 at the 2.6 percent cushion, averaged over the 13 misses as demands", "notebook 03, slides")
    F.add("interview", "peak_cost_at_zero_rs", peak_cost(0), lakh(peak_cost(0)),
          "the same week booked at the forecast itself", "notebook 03, slides")
    F.add("interview", "peak_cost_at_weibull_rs", peak_cost(round(weibull, 3)), lakh(peak_cost(round(weibull, 3))),
          "the same week at the 4.1 percent reading", "notebook 03, slides")
    grid = [i / 1000 for i in range(-80, 101, 2)]
    lowest = min(grid, key=peak_cost)
    F.add("interview", "curve_min_pct", lowest, pct(lowest), "the lowest point of the week's cost curve, on notebook 03's grid of 0.2 percent steps", "notebook 03, slides")
    vend_total = sum(ahead["vendor"][i] for i in WINDOW)
    F.add("interview", "plan_minus_vendor_total", sum(plan.values()) - vend_total, n(sum(plan.values()) - vend_total),
          "the plan's eight weeks minus the vendor's", "transcript 2")
    F.add("interview", "plan_vendor_pct", sum(plan.values()) / vend_total - 1, pct(sum(plan.values()) / vend_total - 1),
          "the plan's eight weeks over the vendor's", "transcript 2")
    F.add("interview", "vendor_shifts_total", sum(math.ceil(ahead["vendor"][i] / PER_SHIFT) for i in WINDOW),
          n(sum(math.ceil(ahead["vendor"][i] / PER_SHIFT) for i in WINDOW)), "the vendor's curve / 120, rounded up, eight weeks", "transcript 2")
    rush = sum(plan[i] - ahead["vendor"][i] for i in (107, 108, 109))
    F.add("interview", "plan_over_vendor_rush", rush, n(rush), "the plan minus the vendor's curve, 19 Oct to 2 Nov 2026", "transcript 2")
    over_mae = sum(abs(hold["aligned"][i] - y[i]) > S["aligned"]["mae"] for i in HOLDOUT)
    F.add("interview", "weeks_over_mae", over_mae, f"{over_mae} of 13", "hidden weeks festival-aligned missed by more than its MAE", "notes, transcripts")
    F.add("interview", "cushion_weibull_pct", weibull, pct(weibull),
          "the 0.82 point read at position 0.82 x 14 of the sorted thirteen, another common convention", "scorecard")
    cov_g = sum(back["aligned"][i] * (1 + cushion) >= y[i] for i in BACK)
    cov_n = sum(y[aligned_source(i)] * (1 + cushion) >= y[i] for i in BACK)
    F.add("interview", "backtest_covered_growth", cov_g, f"{cov_g} of 8", "2025's festive weeks the raised festival-aligned copy covered, with the 4 percent", "transcripts")
    F.add("interview", "backtest_covered_nogrowth", cov_n, f"{cov_n} of 8", "the same, with no growth added", "transcripts")
    fest_mean = sum(y[i] for i in BACK) / len(BACK)
    F.add("interview", "festive_mae_pct", B["aligned"]["mae"] / fest_mean, pct(B["aligned"]["mae"] / fest_mean),
          "festival-aligned's 2025 festive miss over the festive weeks' mean", "scorecard")
    F.add("interview", "holdout_abs_pct", sum(abs(e) for e in errs) / len(errs), pct(sum(abs(e) for e in errs) / len(errs)),
          "festival-aligned's mean miss on the hidden weeks, as a percent of the forecast", "scorecard")
    F.add("interview", "peak_shifts_worked_2025", int(weekly.loc[53, "packer_shifts_worked"]), n(weekly.loc[53, "packer_shifts_worked"]),
          "shifts worked in the week of 6 Oct 2025, overtime included", "transcripts")
    for k in (1.5, 2.0):
        cu = (k - 1) * OVER_RS
        F.add("interview", f"overtime_share_{int(k * 100)}", cu / (cu + OVER_RS), f"{cu / (cu + OVER_RS):.2f}",
              f"the share to cover if a short shipment is packed on overtime at {k:g} times a shift's cost (assumed)", "transcripts")
    F.add("interview", "overtime_rates", [1.5, 2], "one and a half and two times", "overtime at these multiples of a shift's cost (assumed)", "transcripts")
    F.add("toys", "ai_users", 200_000, "2 lakh", "users of the assistant at launch (invented)", "AI variant")
    F.add("toys", "ai_peak_share", 0.01, "1 percent", "users who send a request in the peak minute (invented)", "AI variant")
    F.add("toys", "ai_requests_minute", 2_000, "2,000", "2 lakh x 1 percent, requests in the peak minute", "AI variant")
    F.add("toys", "ai_requests_second", 2_000 / 60, "about 33", "2,000 over 60 seconds", "AI variant")
    F.add("toys", "ai_prompt_tokens", 1_000, "1,000", "prompt tokens a request (invented)", "AI variant")
    F.add("toys", "ai_answer_tokens", 500, "500", "answer tokens a request (invented)", "AI variant")
    F.add("toys", "ai_stream_seconds", 10, "10 seconds", "time to stream one answer (invented)", "AI variant")
    F.add("toys", "ai_open_requests", 2_000 / 60 * 10, "about 330", "33 a second x 10 seconds, requests open at once", "AI variant")
    F.add("toys", "ai_peak_ratio", 5, "five times", "the peak minute over the average minute (invented)", "AI variant")
    F.add("toys", "ai_prompt_tokens_minute", 2_000 * 1_000, "20 lakh", "2,000 requests x 1,000 prompt tokens, a minute", "AI variant")
    F.add("toys", "ai_answer_tokens_minute", 2_000 * 500, "10 lakh", "2,000 requests x 500 answer tokens, a minute", "AI variant")
    F.add("toys", "ai_gpu_holds", 20, "20", "open requests of this mix one GPU holds inside the latency target, from a load test (invented)", "AI variant")
    F.add("toys", "ai_gpus", math.ceil(2_000 / 60 * 10 / 20), "about 17", "330 open requests over 20 a GPU, before headroom", "AI variant")
    F.add("toys", "ai_requests_user_day", 2_000 / 5 * 1_440 / 200_000, "about 3", "2,000 / 5 a minute x 1,440 minutes / 2 lakh users", "AI variant")

    # ---- the week map's earlier nodes, as each day's ticket prints them (docs/detailing/W04_case_file.md)
    F.add("week_map", "mon_before", 1.9, "1.9", "Monday's ticket: trips per peak online hour before the scheme", "slide 2")
    F.add("week_map", "mon_after", 1.6, "1.6", "Monday's ticket: after", "slide 2")
    F.add("week_map", "tue_before", 314, "Rs 314", "Tuesday's ticket: gross bookings per peak online hour before", "slide 2")
    F.add("week_map", "tue_after", 260, "Rs 260", "Tuesday's ticket: after", "slide 2")
    F.add("week_map", "wed_before", 0.061, "6.1 percent", "Wednesday's ticket: strip click-through before", "slide 2")
    F.add("week_map", "wed_after", 0.038, "3.8 percent", "Wednesday's ticket: after", "slide 2")
    F.add("week_map", "thu_before", 0.58, "58 percent", "Thursday's ticket: Android add-to-cart to order, members, before", "slide 2")
    F.add("week_map", "thu_after", 0.44, "44 percent", "Thursday's ticket: after", "slide 2")
    F.add("week_map", "thu_flat", 0.38, "38 percent", "Thursday's ticket: the flat month-two retention", "Kahoot return question")

    # ---- rule constants and the wrong options a quiz or a slide offers, so every printed number has a home
    F.add("rules", "lag_weeks", 52, "52 weeks", "the house bot's copy: the same week a year back", "every file")
    F.add("rules", "lag_2025", 51, "51 weeks", "Diwali 2025's week is 51 weeks after Diwali 2024's", "notebook 01")
    F.add("rules", "lag_2026", 54, "54 weeks", "Diwali 2026's week is 54 weeks after Diwali 2025's", "chapter 3")
    F.add("rules", "align_before", 5, "five weeks", "the festival-aligned copy matches by distance from five weeks before Diwali", "chapter 2, 3")
    F.add("rules", "align_after", 4, "four after", "to four weeks after", "chapter 2, 3")
    F.add("rules", "fit_band_pct", 2, "2 percent", "the vendor's claim: within 2 percent of every past week", "chapter 2")
    F.add("rules", "vendor_floor_ratio", 1.3, "30 percent", "the case file's floor: the vendor at least 30 percent above festival-aligned", "notebook 02 check")
    F.add("rules", "growth_factor", DRIFT, "1.04", "the 4 percent a year, as a multiplier", "every file")
    F.add("rules", "nearest_holdout_gap", 6, "6 weeks", "the hidden week nearest Diwali 2026 sits six weeks before it", "notebook 02")
    F.add("distractors", "within_10000", 10_000, "10,000", "a wrong option: all three rules within 10,000", "chapter 1 vote")
    F.add("kalpa_rules", "drift_steps", 17, "17", "months from Oct 2024 to Mar 2026, the drift line's run", "lab")
    F.add("kalpa_rules", "plan_factor", 1.15, "15 percent", "the plan line: the same month a year earlier plus 15 percent", "lab")
    F.add("kalpa_rules", "hold_months", 6, "six", "April to September 2026", "lab")
    F.add("kalpa_rules", "months", 24, "24", "October 2024 to September 2026", "lab")
    F.add("kalpa_rules", "v4_orders", gcz.V4_ORDERS, "1,000", "the orders in the Week 2 warehouse (v4)", "lab")
    F.add("kalpa_rules", "naive_check_floor", 5_000_000, "Rs 50 lakh", "the lab's check: naive misses by more than this a month", "lab")

    # ---- the exercises' worked numbers
    gw = [54, 55, 56]                                  # 13, 20 and 27 Oct 2025, scored by the bot by hand
    gm = [y[i - 52] - y[i] for i in gw]
    F.add("exercises", "guided_misses", gm, ", ".join(n(m) for m in gm), "bot minus actual, 13, 20 and 27 Oct 2025", "guided set")
    F.add("exercises", "guided_sum", sum(abs(m) for m in gm), n(sum(abs(m) for m in gm)), "the three misses, summed", "guided set")
    F.add("exercises", "guided_mae", sum(abs(m) for m in gm) / 3, n(sum(abs(m) for m in gm) / 3), "the three misses over three", "guided set")
    F.add("exercises", "guided_over12", sum(abs(m) for m in gm) / 12, n(sum(abs(m) for m in gm) / 12), "the sum over twelve rows, a wrong option", "guided set")
    F.add("exercises", "guided_first_copy_plus", round(y[2] * FINANCE), n(round(y[2] * FINANCE)), "14 Oct 2024 times 1.04, a wrong option", "guided set")
    leaky = sum(abs(y[i - 1] - y[i]) for i in HOLDOUT) / 13
    F.add("exercises", "leaky_naive_mae", leaky, n(leaky), "naive scored one week at a time with each hidden week's own predecessor: a leak", "chapter 2 set")
    F.add("exercises", "shifts_no_cushion_10_19", math.ceil(ahead["aligned"][107] / PER_SHIFT), n(math.ceil(ahead["aligned"][107] / PER_SHIFT)),
          "434,928 / 120 rounded up, a wrong option", "staffing set")
    F.add("exercises", "shifts_vendor_10_05", math.ceil(vend[105] / PER_SHIFT), n(math.ceil(vend[105] / PER_SHIFT)),
          "the vendor's 5 Oct 2026 / 120, a wrong option", "staffing set")
    F.add("exercises", "shifts_bot_10_19", math.ceil(ahead["bot"][107] / PER_SHIFT), n(math.ceil(ahead["bot"][107] / PER_SHIFT)),
          "the bot's 19 Oct 2026 / 120, a wrong option", "staffing set")
    F.add("exercises", "plan_10_19_raw", ahead["aligned"][107] * (1 + cushion) / PER_SHIFT,
          f"{ahead['aligned'][107] * (1 + cushion) / PER_SHIFT:,.1f}", "446,236 / 120 before rounding up", "staffing set")
    F.add("exercises", "pairs", [9_800, 6_000, 6_200], "9,800, 6,000 and 6,200", "three invented model MAEs for the good-enough drill", "chapter 2 set")
    F.add("exercises", "pair3_high", 7, "7 of 13", "invented: the third model's weeks too high", "chapter 2 set")
    F.add("exercises", "pair1_gap_pct", 1 - 9_800 / S["bot"]["mae"], pct(1 - 9_800 / S["bot"]["mae"]), "how far 9,800 sits under the bot's MAE", "chapter 2 set")
    F.add("exercises", "pair1_gap", S["bot"]["mae"] - 9_800, n(S["bot"]["mae"] - 9_800), "the bot's MAE minus team A's", "chapter 2 set")
    F.add("exercises", "pair1_gap_shifts", (S["bot"]["mae"] - 9_800) / PER_SHIFT, f"{(S['bot']['mae'] - 9_800) / PER_SHIFT:.1f}",
          "31 shipments a week over 120 a shift", "chapter 2 set")
    F.add("exercises", "pair1_vs_aligned", 9_800 - S["aligned"]["mae"], n(9_800 - S["aligned"]["mae"]), "team A's MAE above festival-aligned's", "chapter 4 set")
    F.add("exercises", "pair3_lead", S["aligned"]["mae"] - 6_200, n(S["aligned"]["mae"] - 6_200), "team C's lead over festival-aligned, shipments a week", "chapter 4 set")
    F.add("exercises", "pair3_lead_rs", (S["aligned"]["mae"] - 6_200) * LATE_RS, f"about Rs {round((S['aligned']['mae'] - 6_200) * LATE_RS, -2):,.0f}",
          "the most that lead saves a week: each shipment a late one at Rs 25", "chapter 4 set")
    F.add("exercises", "ch1_series_a", [100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144], "100, 104, 108", "invented: a climb", "chapter 1 set")
    F.add("exercises", "ch1_series_b", [100, 130, 100, 70] * 3, "100, 130, 100, 70", "invented: a repeat of four", "chapter 1 set")
    F.add("exercises", "ch1_series_c", [100, 132, 104, 76, 108, 140, 112, 84, 116, 148, 120, 92], "100, 132, 104, 76", "invented: both", "chapter 1 set")
    F.add("exercises", "ch1_b_mean", 100, "100", "series B's mean, a wrong option", "chapter 1 set")
    F.add("exercises", "ch1_c_rise", 8, "8", "series C rises 8 a cycle of four", "chapter 1 set")
    F.add("exercises", "ch1_c_two_cycles", 16, "16", "two cycles of C's climb, the miss of a copy from eight back", "chapter 1 set")
    F.add("practice", "series_x", [20, 22, 24, 26, 28, 30, 32, 34], "20, 22, 24", "invented: a climb", "lab set")
    F.add("practice", "series_y", [20, 35, 20, 20, 20, 35, 20, 20], "20, 35, 20, 20", "invented: a repeat of four", "lab set")
    F.add("practice", "series_z", [20, 23, 18, 21, 22, 19, 21, 20], "20, 23, 18, 21", "invented: wobble", "lab set")
    F.add("practice", "shop_last", [40, 55, 70, 50, 35, 41], "40, 55, 70, 50, 35, 41", "invented: last year's six weeks, festival in week 3", "lab set")
    F.add("practice", "shop_this", [42, 44, 58, 73], "42, 44, 58, 73", "invented: this year's first four, festival in week 4", "lab set")
    F.add("practice", "errors", [12, -8, 5, -15, 6], "12, -8, 5, -15 and 6", "invented: five misses", "lab set")
    F.add("practice", "errors_sum", 46, "46", "their sizes, summed", "lab set")
    F.add("practice", "errors_mae", 9.2, "9.2", "46 / 5", "lab set")
    F.add("practice", "errors_signed_mean", 0, "0", "the signed misses cancel, a wrong option", "lab set")
    F.add("practice", "idle_rs", 600, "Rs 600", "invented idle shift", "lab set")
    F.add("practice", "late_rs", 30, "Rs 30", "invented late shipment", "lab set")
    F.add("practice", "over_rs", 5, "Rs 5", "600 / 120", "lab set")
    F.add("practice", "share", 30 / 35, "0.86", "30 / (30 + 5)", "lab set")
    F.add("practice", "share_wrong", 5 / 35, "0.14", "5 / 35, the share upside down", "lab set")
    F.add("practice", "share_other", [0.5, 0.95], "0.50 and 0.95", "wrong options", "lab set")

    # ---- Kalpa, TRAINER until the lab
    rev = dict(zip(monthly.month, monthly.revenue_rs))
    kv = dict(zip(kvendor.month, kvendor.vendor_rs))
    hold_m = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]
    months = kalpa_months()
    ksn = {m: rev[f"{int(m[:4]) - 1}-{m[5:]}"] for m in hold_m}
    knaive = {m: rev["2026-03"] for m in hold_m}
    kslope = (rev["2026-03"] - rev["2024-10"]) / 17
    kdrift = {m: rev["2026-03"] + (k + 1) * kslope for k, m in enumerate(hold_m)}
    kven = {m: kv[m] for m in hold_m}
    kmae = {name: sum(abs(f[m] - rev[m]) for m in hold_m) / 6
            for name, f in (("seasonal_naive", ksn), ("naive", knaive), ("drift", kdrift), ("vendor", kven))}
    for name, v in kmae.items():
        F.add("kalpa", f"{name}_mae_rs", v, lakh(v), f"Kalpa {name} MAE on Apr to Sep 2026, forecast from Mar 2026", "lab")
    kal_hold = {m: round(ksn[m] * FINANCE) for m in hold_m}
    kal_mae = sum(abs(kal_hold[m] - rev[m]) for m in hold_m) / 6
    for m in hold_m:
        F.add("kalpa_months", f"aligned_{m.replace('-', '_')}", kal_hold[m], lakh(kal_hold[m]),
              f"festival-aligned for {m}: the same month of 2025 plus 4 percent", "Kalpa set")
    F.add("kalpa", "aligned_mae_rs", kal_mae, lakh(kal_mae),
          "festival-aligned (the seasonal copy plus 4 percent) on Apr to Sep 2026, which holds no Diwali month", "lab, Kalpa set")
    F.add("kalpa", "vendor_over_sn_pct", kmae["vendor"] / kmae["seasonal_naive"] - 1,
          pct(kmae["vendor"] / kmae["seasonal_naive"] - 1, 0), "vendor MAE over the seasonal naive's, minus one", "lab")
    for m in months:
        F.add("kalpa_months", f"rev_{m.replace('-', '_')}", rev[m], lakh(rev[m]), f"Kalpa revenue, {m}", "lab")
    F.add("kalpa_months", "nov_mar_two_places", [round(rev["2025-11"] / 1e5, 2), round(rev["2026-03"] / 1e5, 2)],
          f"{rev['2025-11'] / 1e5:.2f} and {rev['2026-03'] / 1e5:.2f}", "Nov 2025 and Mar 2026 in Rs lakh to two places, which one place prints alike", "Kalpa board set")
    for m in hold_m:
        F.add("kalpa_months", f"v4_{m.replace('-', '_')}", v4sums[m], lakh(v4sums[m]), f"sum of v4 orders.amount, {m}", "lab")
        F.add("kalpa_months", f"vendor_{m.replace('-', '_')}", kv[m], lakh(kv[m]), f"the vendor's forecast from Mar 2026, {m}", "lab, Kalpa set")
    later = ["2026-10", "2026-11", "2026-12", "2027-01", "2027-02", "2027-03"]
    last = {m: rev[f"{int(m[:4]) - 1}-{m[5:]}"] for m in later}
    swap = {"2026-10": "2025-11", "2026-11": "2025-10"}
    aligned_k = {m: round(rev[swap.get(m, f"{int(m[:4]) - 1}-{m[5:]}")] * DRIFT) for m in later}
    finance_k = {m: round(last[m] * DRIFT) for m in later}
    plan_k = dict(zip(kplan.month, kplan.plan_rs))
    for m in later:
        for name, f in (("seasonal_naive", last), ("finance", finance_k), ("aligned", aligned_k),
                        ("vendor", {x: kv[x] for x in later}), ("plan", plan_k)):
            F.add("kalpa_window", f"{name}_{m.replace('-', '_')}", f[m], lakh(f[m]), f"Kalpa {name}, {m}", "lab, unguided exercise")
    for name, f in (("seasonal_naive", last), ("finance", finance_k), ("aligned", aligned_k),
                    ("vendor", {x: kv[x] for x in later}), ("plan", plan_k)):
        t = sum(f.values())
        F.add("kalpa_window", f"{name}_total", t, f"Rs {t / 1e7:.2f} crore", f"Kalpa {name}, Oct 2026 to Mar 2027", "lab, unguided exercise")
        F.add("kalpa_window", f"{name}_vs_last_pct", t / sum(last.values()) - 1, pct(t / sum(last.values()) - 1),
              "over the same six months a year earlier", "lab, unguided exercise")
    y1 = sum(rev[m] for m in months[:12]); y2 = sum(rev[m] for m in months[12:])
    F.add("kalpa", "year_to_sep25_rs", y1, f"Rs {y1 / 1e7:.2f} crore", "Oct 2024 to Sep 2025", "lab")
    F.add("kalpa", "year_to_sep26_rs", y2, f"Rs {y2 / 1e7:.2f} crore", "Oct 2025 to Sep 2026", "lab")
    F.add("kalpa", "year_gap_pct", 1 - y1 / y2, pct(1 - y1 / y2), "how far the first year sits below the second", "lab")
    F.add("kalpa", "growth_pct", y2 / y1 - 1, pct(y2 / y1 - 1), "the second year over the first, minus one", "lab")
    F.add("kalpa", "q1_total_rs", sum(rev[m] for m in hold_m[:3]), "Rs 10.00 crore", "Apr to Jun 2026, V4_Q1_TOTAL", "lab")
    F.add("kalpa", "q2_total_rs", sum(rev[m] for m in hold_m[3:]), "Rs 9.84 crore", "Jul to Sep 2026, V4_Q2_TOTAL", "lab")
    oct24 = rev["2024-10"] / rev["2024-11"]
    oct25 = rev["2025-10"] / ((rev["2025-09"] + rev["2025-11"]) / 2)
    F.add("kalpa", "oct24_ratio", oct24, f"{oct24:.2f}", "Oct 2024 over Nov 2024, its one neighbour in the data", "lab")
    F.add("kalpa", "oct25_ratio", oct25, f"{oct25:.2f}", "Oct 2025 over the mean of Sep and Nov 2025", "lab")
    kfit = max(abs(kv[m] - rev[m]) / rev[m] for m in months[:18])
    F.add("kalpa", "vendor_fit_max_pct", kfit, pct(kfit), "the vendor's largest miss on its 18 fitted months", "lab")
    kcushion_errs = [(rev[m] - ksn[m]) / ksn[m] for m in hold_m]
    F.add("kalpa", "sn_err_mean_pct", sum(kcushion_errs) / 6, pct(sum(kcushion_errs) / 6), "the seasonal naive's mean error on the hold-out", "unguided exercise")

    # ---- the guesstimate and the public facts used on Friday
    F.add("public", "siam_two_wheelers", 21_700_000, "2.17 crore", "SIAM, FY 2025-26 domestic two-wheeler sales (T3, checked 12 Oct 2026)", "guesstimate")
    F.add("public", "fada_oct25", 3_149_846, "31,49,846", "FADA, October 2025 two-wheeler retail (F5, checked 12 Oct 2026)", "chapter 3 caveats, guesstimate")
    F.add("public", "fada_sep25", 1_287_735, "12,87,735", "FADA, September 2025 two-wheeler retail (F5)", "chapter 3 caveats")
    F.add("public", "fada_oct25_lakh", 31.5, "31.5 lakh", "31,49,846 in lakh", "guesstimate")
    F.add("public", "fada_window_days", 42, "42-day", "FADA's festive window (F5)", "chapter 3 caveats")
    F.add("public", "fada_sep25_lakh", 12.9, "12.9 lakh", "12,87,735 in lakh", "chapter 3 caveats")
    F.add("public", "m5_products", 3049, "3,049", "products in M5, Walmart's daily unit sales (F2)", "chapter 1")
    F.add("public", "zillow_band_pct", 2, "2 percent", "200 basis points as a percent", "half2, transcript, notes")
    F.add("public", "zillow_swing_points", 12, "about 12 percentage points", "1,200 basis points as percentage points", "half2, transcript, notes")
    F.add("public", "flipkart_space", 14, "14 million cubic feet", "Flipkart, warehouse space for TBBD 2026 (F6)", "chapter 1 close")
    F.add("public", "flipkart_jobs", 250_000, "more than 2.5 lakh", "Flipkart, direct and indirect festive employment opportunities (F6)", "chapter 1 close")
    F.add("public", "m5_seasonal_naive", 0.847, "0.847", "M5 score of the seasonal naive (F2)", "chapter 1, notes")
    F.add("public", "m5_naive", 1.752, "1.752", "M5 score of the naive (F2)", "chapter 1, notes")
    F.add("public", "m5_winner", 0.520, "0.520", "M5 winner's score (F2)", "notes")
    F.add("public", "m5_mlp", 0.977, "0.977", "M5 perceptron benchmark (F2)", "notes")
    F.add("public", "m5_rf", 1.010, "1.010", "M5 random forest benchmark (F2)", "notes")
    F.add("public", "plos_series", 1045, "1,045", "PLOS ONE 2018 series count (F1)", "notes")
    F.add("public", "zillow_band", 200, "200 basis points", "Zillow's public guardrail, plus or minus (F3)", "fallback, transcript")
    F.add("public", "zillow_swing", 1200, "about 1,200 basis points", "the swing Zillow reported (F3)", "fallback, transcript")
    F.add("public", "zillow_writedown", 304, "about USD 304 million", "Zillow's inventory write-down (F3)", "fallback, transcript")
    F.add("public", "zillow_workforce", 0.25, "about 25 percent", "Zillow's workforce cut (F3)", "fallback")
    F.add("public", "zillow_q4_low", -500, "minus 500", "Zillow's expected Q4 2021 unit economics, basis points, one end (F3)", "fallback")
    F.add("public", "zillow_q4_high", -700, "minus 700", "the other end (F3)", "fallback")
    F.add("public", "zillow_q4_pct", [5, 7], "5 to 7 percent", "minus 500 to minus 700 basis points as a percent loss", "transcript")
    F.add("public", "zillow_months", [3, 6], "three to six months", "how far ahead Zillow forecast prices (F3)", "fallback")
    F.add("public", "target_stores", 133, "133", "Target Canada stores closed, release of 15 Jan 2015 (F4)", "fallback")
    F.add("public", "target_staff", 17_600, "about 17,600", "Target Canada employees (F4)", "fallback")
    F.add("public", "flipkart_sale_open", "2026-10-09", "9 October 2026", "The Big Billion Days 2026 main sale (F6)", "chapter 1 close")
    F.add("public", "flipkart_release", "2026-10-06", "6 October 2026", "Flipkart's announcement date (F6)", "chapter 1 close")
    F.add("public", "split_difference", 13, "13 percent", "the midpoint of 4 and 22, the weak answer", "fallback, transcript")
    F.add("public", "m5_top_ml", 50, "50", "M5: all 50 top-performing methods were machine learning (the M5 accuracy paper, checked 12 Oct 2026)", "transcript, notes")
    F.add("public", "m5_beat_snaive_pct", 0.358, "35.8 percent", "M5: 1,972 of the 5,507 teams, 35.8 percent, beat the seasonal naive (the accuracy paper, checked 12 Oct 2026)", "half1 S14, notes")
    F.add("public", "m5_snaive_period", 7, "7", "M5's seasonal naive copies the value 7 days back, since the series are daily", "half1 S14, notes")
    F.add("public", "plos_methods", 8, "eight", "PLOS ONE 2018: eight machine-learning and eight statistical methods", "transcript, notes")
    F.add("public", "target_data_accuracy", 0.30, "about 30 percent", "Canadian Business: item data in Target Canada's system was accurate about 30 percent of the time", "transcript, notes")
    F.add("public", "amazon_test_weeks", 2, "two weeks", "Amazon Science: the retrained recommender was tested on the two weeks after its cutoff", "transcript, notes")
    F.add("public", "fada_quiet_days", 21, "21 days", "FADA: September 2025's first 21 days were almost quiet ahead of GST 2.0 (F5)", "guesstimate card")

    F.add("kalpa_exercise", "bar_six", kal_mae * 6, f"about Rs {kal_mae * 6 / 1e5:.0f} lakh",
          "six months of festival-aligned's hidden-month MAE, all one way", "Kalpa set")
    F.add("kalpa_exercise", "sn_bar_six", kmae["seasonal_naive"] * 6, f"about Rs {kmae['seasonal_naive'] * 6 / 1e5:.0f} lakh",
          "six months of the seasonal copy's MAE, all one way, a wrong option", "Kalpa set")
    F.add("kalpa_exercise", "vendor_minus_sn", kmae["vendor"] - kmae["seasonal_naive"], lakh(kmae["vendor"] - kmae["seasonal_naive"]),
          "the vendor's MAE minus the seasonal copy's, a month", "Kalpa set")
    F.add("kalpa_exercise", "gap_to_plan", sum(plan_k.values()) - sum(aligned_k.values()),
          f"Rs {(sum(plan_k.values()) - sum(aligned_k.values())) / 1e7:.2f} crore", "plan line minus festival-aligned, six months", "Kalpa set")
    F.add("kalpa_exercise", "gap_to_plan_pct", sum(plan_k.values()) / sum(aligned_k.values()) - 1,
          pct(sum(plan_k.values()) / sum(aligned_k.values()) - 1), "the plan line over festival-aligned", "Kalpa set")

    # ---- the guesstimate: two-wheelers sold in India in a year (assumptions labelled, the anchor public)
    hh, own, years, first = 300_000_000, 0.50, 8, 0.15
    repl = hh * own / years
    est = repl * (1 + first)
    F.add("guesstimate", "households", hh, "30 crore", "Indian households, assumption, range 28 to 32 crore", "half2, transcript")
    F.add("guesstimate", "own_share", own, "half", "share of households with a two-wheeler, assumption, range 40 to 60 percent", "half2, transcript")
    F.add("guesstimate", "replace_years", years, "8 years", "years before a household replaces it, assumption, range 6 to 10", "half2, transcript")
    F.add("guesstimate", "replace_years_range", [6, 10], "6 to 10 years", "the replacement years' assumed range", "half2 D4, transcript")
    F.add("guesstimate", "replacement", repl, f"about {repl / 1e7:.1f} crore", "30 crore x 0.5 / 8", "half2, transcript")
    F.add("guesstimate", "first_time", first, "15 percent", "first-time buyers on top, assumption, range 10 to 20 percent", "half2, transcript")
    F.add("guesstimate", "estimate", est, f"about {est / 1e7:.1f} crore", "replacement x 1.15, 2.16 unrounded", "half2, transcript")
    for name_, lo_, hi_ in (("years", hh * own / 10 * (1 + first), hh * own / 6 * (1 + first)),
                            ("own", hh * 0.4 / years * (1 + first), hh * 0.6 / years * (1 + first)),
                            ("households", 280_000_000 * own / years * (1 + first), 320_000_000 * own / years * (1 + first)),
                            ("first", repl * 1.10, repl * 1.20)):
        F.add("guesstimate", f"swing_{name_}_low_pct", lo_ / est - 1, pct(lo_ / est - 1, 0), f"{name_} at its low end, the rest held", "guesstimate card")
        F.add("guesstimate", f"swing_{name_}_high_pct", hi_ / est - 1, pct(hi_ / est - 1, 0), f"{name_} at its high end, the rest held", "guesstimate card")
    F.add("guesstimate", "vehicles_per_home", [1, 1.25], "1, from 1 to 1.25", "vehicles per owning household, assumption", "guesstimate card")
    F.add("guesstimate", "swing_vehicles_pct", 0.25, "25 percent", "a second vehicle in one owning home in four, the rest held", "guesstimate card")
    F.add("guesstimate", "range_one_low", hh * own / 10 * (1 + first), f"about {hh * own / 10 * (1 + first) / 1e7:.1f} crore",
          "replacement years at 10, the rest held", "half2 S9, notes")
    F.add("guesstimate", "range_one_high", hh * own / 6 * (1 + first), f"about {hh * own / 6 * (1 + first) / 1e7:.1f} crore",
          "replacement years at 6, the rest held", "half2 S9, notes")
    F.add("guesstimate", "anchor", 21_705_974, "2,17,05,974", "SIAM, FY 2025-26 domestic two-wheeler sales (T3, checked 12 Oct 2026)", "half2, transcript")
    F.add("guesstimate", "estimate_vs_anchor_pct", est / 21_705_974 - 1, pct(est / 21_705_974 - 1), "estimate over anchor, minus one", "transcript")
    F.add("guesstimate", "annualised_october", 3_149_846 * 12, f"about {3_149_846 * 12 / 1e7:.2f} crore", "October 2025 retail times 12", "half2, transcript")
    F.add("guesstimate", "annualised_over_pct", 3_149_846 * 12 / 21_705_974 - 1, pct(3_149_846 * 12 / 21_705_974 - 1, 0),
          "the annualised festive month over the anchor", "half2, transcript")
    low = 280_000_000 * 0.40 / 10 * 1.10
    high = 320_000_000 * 0.60 / 6 * 1.20
    F.add("guesstimate", "range_low", low, f"about {low / 1e7:.1f} crore", "every input at its low end: 28 crore x 0.4 / 10 x 1.1", "guesstimate card")
    F.add("guesstimate", "range_high", high, f"about {high / 1e7:.1f} crore", "every input at its high end: 32 crore x 0.6 / 6 x 1.2", "guesstimate card")
    F.add("guesstimate", "anchor_growth_pct", 10.7, "10.7 percent", "SIAM's FY 2025-26 two-wheeler growth on the year before (T3)", "guesstimate card")

    # ---- the chai stall and the hostel mess, invented for the concept chapters and their sets
    toy = stall_facts(F, stall, tables, y, ahead, S)

    # ---- what the case file targeted and the data hold
    corrections = [
        "Hold-out MAEs are forecasts from one origin (22 Jun 2026), so no rule sees a week it is scored on. "
        f"The case file's naive 21,000, drift 11,500, same-week-last-year 9,200, festival-aligned 8,900, finance 9,600 and vendor 14,800 "
        f"become {n(S['naive']['mae'])}, {n(S['drift']['mae'])}, {n(S['bot']['mae'])}, {n(S['aligned']['mae'])}, "
        f"{n(S['finance']['mae'])} and {n(S['vendor']['mae'])}.",
        "Festival-aligned and finance's rule tie on the hold-out: no hold-out week lies within five weeks of a Diwali, "
        "so both copy the same calendar week a year back and add the same 4 percent; they part only in the festive weeks.",
        "Drift sits beside naive: the line from 30 Sep 2024 to 22 Jun 2026 rises "
        f"{slope:.0f} shipments a week, so the case file's 11,500 has nothing to stand on.",
        "The vendor's hold-out misses are all above the actual and grow with the weeks ahead "
        f"({pct(early)} in the first six weeks, {pct(late)} in the last six); the case file's 'two weeks after the 2025 festival' "
        "lie in its fitted history, where it sits within 2 percent.",
        f"The 2026 window: the festival-aligned baseline is {pct(totals['aligned'] / cal - 1)} above the same calendar weeks of 2025 "
        f"and {pct(totals['aligned'] / fest - 1)} above the same weeks counted from Diwali; the case file's 'about 6 percent' "
        "becomes those two numbers. Finance is 4.0 percent above the calendar window and "
        f"{pct(totals['finance'] / fest - 1)} against the festival-aligned one; the vendor is 22.0 percent above the calendar window "
        f"and {pct(totals['vendor'] / totals['aligned'] - 1)} above the aligned total.",
        "The hold-out is 29 Jun to 21 Sep 2026: thirteen Mondays end on 21 Sep (the case file's correction of 12 Oct 2026).",
        f"The ordinary week is about 210,000 at the level; the ordinary weeks of 11 Nov to 23 Dec 2024 run {n(min(y[6:13]))} to {n(max(y[6:13]))} with season, payday and noise.",
        "Kalpa's April to September 2026 are v4's monthly order sums, lumpy because two large Business orders (Rs 1.23 crore on "
        "28 Apr and Rs 1.99 crore on 13 Jul 2026) sit in them; the year before mirrors that shape about 4 percent lower.",
        "Kalpa's vendor rows for April 2026 onward are its forecast from March 2026, labelled forecast, never fitted.",
    ]
    header = "\n".join([
        "# content/W04/D5/internal/C2_W04_D05_facts_INTERNAL.yaml, written by C2_W04_D05_make_data_INTERNAL.py.",
        "# Every number a Friday learner sees, with the form it prints in, how it was computed and where",
        "# it is used. Public facts carry their R2 id; toys are labelled invented where they appear; the",
        "# kalpa sections are TRAINER until the lab finds them. The toy section holds the chai stall and",
        "# the hostel mess, invented for the concept chapters, each row under a toy_ id with how it was",
        "# invented and the files that use it (used_by). In the case sections, used_in names the case's",
        "# chapters as built before 13 October 2026: its chapters 1 to 3 are now SECTIONs 5 to 7, and",
        "# notebooks 01 to 04 are now 05 to 08.",
        "#",
        "# Corrections to the case file (docs/detailing/W04_case_file.md, Friday):",
    ] + [f"#   {k + 1}. " + "\n#      ".join(_wrap(c, 92)) for k, c in enumerate(corrections)])
    count = F.write(header)

    # ---- the targets, asserted
    def want(label, ok, got):
        print(f"{'PASS' if ok else 'FAIL'}  {label}: {got}")
        if not ok:
            raise SystemExit(f"target missed: {label}")

    want("104 weeks of history", len(y) == 104, len(y))
    want("calendar runs 114 weeks", len(calendar) == 114, len(calendar))
    want("ordinary weeks of late 2024 sit near 210,000", all(200_000 <= y[i] <= 230_000 for i in range(6, 13)), y[6:13])
    for o, r in FESTIVE.items():
        for d in (DIWALI[2024], DIWALI[2025]):
            level = ORDINARY * GROWTH ** ((d + o) / 52)
            want(f"festive ratio at {o:+d}, week {d + o}", abs(y[d + o] / level - r) <= 0.07, round(y[d + o] / level, 3))
    want("measured growth rounds to about 4 percent", 0.036 <= growth <= 0.044, round(growth, 4))
    want("vendor fits the 91 training weeks within 2 percent", vfit <= 0.02, round(vfit, 4))
    want("vendor's hold-out MAE at least 30 percent above the aligned baseline's",
         S["vendor"]["mae"] >= 1.3 * S["aligned"]["mae"], (round(S["vendor"]["mae"]), round(S["aligned"]["mae"])))
    want("vendor loses to the house bot", S["vendor"]["mae"] > S["bot"]["mae"], (round(S["vendor"]["mae"]), round(S["bot"]["mae"])))
    want("the bot beats naive and drift", S["bot"]["mae"] < min(S["naive"]["mae"], S["drift"]["mae"]),
         (round(S["bot"]["mae"]), round(S["naive"]["mae"]), round(S["drift"]["mae"])))
    want("aligned and finance tie on the hold-out", hold["aligned"] == hold["finance"], "identical forecasts")
    want("aligned beats the bot", S["aligned"]["mae"] < S["bot"]["mae"], (round(S["aligned"]["mae"]), round(S["bot"]["mae"])))
    want("the vendor errs high on most hold-out weeks", S["vendor"]["high_weeks"] >= 11, S["vendor"]["high_weeks"])
    want("the vendor's misses grow with the weeks ahead", late > early, (round(early, 4), round(late, 4)))
    want("priced, the vendor costs less than the aligned baseline at the median",
         S["vendor"]["cost_rs"] < S["aligned"]["cost_rs"], (round(S["vendor"]["cost_rs"]), round(S["aligned"]["cost_rs"])))
    want("the bot lands the 2025 peak a week late", max(BACK, key=lambda i: back["bot"][i]) == 54, dmy(max(BACK, key=lambda i: back["bot"][i])))
    want("the aligned copy lands the 2025 peak on the week of 6 Oct 2025", max(BACK, key=lambda i: back["aligned"][i]) == 53, "6 Oct 2025")
    want("the 2025 back-test prices the bot far above the aligned baseline", B["bot"]["cost_rs"] > 5 * B["aligned"]["cost_rs"],
         (round(B["bot"]["cost_rs"]), round(B["aligned"]["cost_rs"])))
    want("the bot's 2026 peak lands on 5 Oct 2026, two weeks early", max(HORIZON, key=lambda i: ahead["bot"][i]) == 105, "5 Oct 2026")
    want("the aligned 2026 peak lands on 19 Oct 2026", max(HORIZON, key=lambda i: ahead["aligned"][i]) == 107, "19 Oct 2026")
    want("vendor 22.0 percent above the calendar window", abs(totals["vendor"] / cal - 1.22) < 0.0005, round(totals["vendor"] / cal - 1, 4))
    want("finance 4.0 percent above the calendar window", abs(totals["finance"] / cal - 1.04) < 0.0005, round(totals["finance"] / cal - 1, 4))
    want("aligned 4.0 percent above the festival window", abs(totals["aligned"] / fest - 1.04) < 0.0005, round(totals["aligned"] / fest - 1, 4))
    want("finance sits below the aligned total", totals["finance"] < totals["aligned"], (totals["finance"], totals["aligned"]))
    want("plan quantile about 0.82", abs(QUANTILE - 0.82) < 0.005, round(QUANTILE, 4))
    want("twelve rows: six around each Diwali", [week(i).isoformat() for i in twelve][::6] == ["2024-10-07", "2025-09-29"], "ok")
    want("Kalpa Apr to Jun 2026 sum to Rs 10.00 crore", sum(rev[m] for m in hold_m[:3]) == gcz.V4_Q1_TOTAL, sum(rev[m] for m in hold_m[:3]))
    want("Kalpa Jul to Sep 2026 sum to Rs 9.84 crore", sum(rev[m] for m in hold_m[3:]) == gcz.V4_Q2_TOTAL, sum(rev[m] for m in hold_m[3:]))
    want("Kalpa Apr to Sep 2026 equal v4's monthly sums", all(rev[m] == v4sums[m] for m in hold_m), "equal")
    want("Kalpa Octobers 1.4 to 1.7 times their neighbours", 1.4 <= oct24 <= 1.7 and 1.4 <= oct25 <= 1.7, (round(oct24, 2), round(oct25, 2)))
    want("Kalpa first year 3 to 5 percent below the second", 0.03 <= 1 - y1 / y2 <= 0.05, round(1 - y1 / y2, 4))
    want("Kalpa vendor fits within 2 percent", kfit <= 0.02, round(kfit, 4))
    want("Kalpa vendor MAE at least 30 percent above the seasonal naive's", kmae["vendor"] >= 1.3 * kmae["seasonal_naive"],
         (round(kmae["vendor"]), round(kmae["seasonal_naive"])))
    want("Kalpa seasonal naive beats naive and drift", kmae["seasonal_naive"] < min(kmae["naive"], kmae["drift"]),
         {k: round(v / 1e5, 1) for k, v in kmae.items()})
    kvt = sum(kv[m] for m in later)
    want("Kalpa vendor 22 percent above the year before", abs(kvt / sum(last.values()) - 1.22) < 0.001, round(kvt / sum(last.values()) - 1, 4))
    want("Kalpa month-aligned copy puts the spike in October 2026", max(later, key=lambda m: last[m]) == "2026-10", "Oct 2026")
    want("Kalpa festival-aligned copy puts it in November 2026", max(later, key=lambda m: aligned_k[m]) == "2026-11", "Nov 2026")
    # ---- the stall's targets (concept chapters)
    want("the stall holds 730 days from Mon 30 Sep 2024", len(stall) == 730 and stall.date.iloc[0] == "2024-09-30", stall.date.iloc[-1])
    want("growth read a season apart on the fortnights is 8 to 12 percent", 0.08 <= toy["ratio"] <= 0.12, round(toy["ratio"], 4))
    want("the exam fortnight is about 1.4 times an ordinary fortnight both years", all(1.33 <= r <= 1.47 for r in toy["exam_ratio"]), [round(r, 2) for r in toy["exam_ratio"]])
    want("Diwali week is about 0.4 times an ordinary fortnight both years", all(0.36 <= r <= 0.44 for r in toy["diwali"]), [round(r, 2) for r in toy["diwali"]])
    want("what is left has a mean near 0 and a spread of a few cups", abs(toy["left_mean"]) < 1.5 and toy["left_spread"] < 6,
         (round(toy["left_mean"], 2), round(toy["left_spread"], 2)))
    want("next Sunday: the seasonal naive within 2 cups, naive and drift over 40 out", abs(61 - 60) <= 2 and toy["drift"] - 60 > 40, round(toy["drift"], 2))
    e0, e1, e2 = toy["exam_days"]
    want("the naive misses the first exam day by more than 30, the yearly copy by about the growth", e2 - e0 > 30 and abs(round(e1 * 1.1) - e2) <= 2, (e2 - e0, e2 - e1))
    want("the calendar copy misses the moved Diwali by over 50 cups; the aligned copy by under 20", toy["cal_worst"] > 50 and toy["ali_worst"] < 20,
         (toy["cal_worst"], toy["ali_worst"]))
    want("chapter 3: MAE 5.0, MAPE about 4.8 percent, a lean of -1.7 cups, Rs 150", round(toy["mae"], 1) == 5.0 and round(toy["mape"] * 100, 1) == 4.8
         and round(toy["lean"], 1) == -1.7 and toy["cost"] == 150, (toy["mae"], round(toy["mape"], 4), round(toy["lean"], 2), toy["cost"]))
    want("same MAE, different rupees: Rs 120 against Rs 180", toy["rules"]["rule P"][3] == 120 and toy["rules"]["rule Q"][3] == 180
         and toy["rules"]["rule P"][1] == toy["rules"]["rule Q"][1], (toy["rules"]["rule P"][3], toy["rules"]["rule Q"][3]))
    want("the MAPE what-if: 15 cups is 17.6 and 300 percent", [round(p * 100, 1) for p in toy["mape_days"]] == [17.6, 300.0], toy["mape_days"])
    want("chapter 4: the line says 109, the curve 168", round(toy["line5"]) == 109 and toy["cubic5"] == 168, (toy["line5"], toy["cubic5"]))
    want("chapter 4: the seasonal naive beats the nephew's mean on seven hidden days by at least half", toy["sn_mae"] * 2 <= toy["mn_mae"],
         (round(toy["sn_mae"], 2), round(toy["mn_mae"], 2)))
    sn_c, mn_c, tr_c = toy["cans"]
    want("chapter 4: the seasonal naive orders the cans a perfect forecast would, all seven days", sn_c == tr_c, (sn_c, tr_c))
    want("chapter 4: the nephew's mean orders a wrong can on the Sunday only", [a != b for a, b in zip(mn_c, tr_c)] == [False] * 6 + [True], mn_c)
    want("a rule 100 shipments a week better moves at most one shift in any window week", max(toy["moved"]) <= 1, toy["moved"])
    print(f"\nWrote {count} facts to {FACTS.relative_to(ROOT)} and {len(list(DATA.glob('*.csv')))} tables to {DATA.relative_to(ROOT)}")


def _wrap(text, width):
    words, lines, line = text.split(), [], ""
    for w in words:
        if len(line) + len(w) + 1 > width:
            lines.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    return lines + [line]


CASE_TABLES = ("weekly_shipments", "calendar", "vendor_forecast", "costs", "twelve_rows",
               "kalpa_monthly_revenue", "kalpa_vendor_forecast", "kalpa_plan_line")


def against_main():
    """Assert every case table is byte for byte the one origin/main holds."""
    import subprocess
    bad = 0
    for name in CASE_TABLES:
        rel = (DATA / f"C2_W04_D05_{name}_STUDENT.csv").relative_to(ROOT).as_posix()
        main_bytes = subprocess.run(["git", "show", f"origin/main:{rel}"], cwd=ROOT, capture_output=True, check=True).stdout
        same = (ROOT / rel).read_bytes() == main_bytes
        bad += not same
        print(f"{'PASS' if same else 'FAIL'}  {rel} is byte-identical to origin/main ({len(main_bytes)} bytes)")
    if bad:
        raise SystemExit(f"{bad} case table(s) differ from origin/main")


if __name__ == "__main__":
    main()
    if "--against-main" in sys.argv:
        against_main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W04/D5/internal/C2_W04_D05_make_data_INTERNAL.py
#     Every target line prints PASS, then the facts and table counts; the run exits 0.
# Running it twice in a row
#     Both runs write byte-identical CSVs and facts file (git diff --stat shows nothing).
# DRIFT changed to 1.05
#     "aligned and finance tie on the hold-out" fails, since finance keeps 4 percent.
# VENDOR_HOLD set to (0.0, 0.0)
#     "vendor's hold-out MAE at least 30 percent above the aligned baseline's" fails.

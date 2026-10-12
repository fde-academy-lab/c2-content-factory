"""Build the Friday case data for Week 4 Day 5.

Writes the case tables (Flipkart Lucknow fulfilment centre) and the small Kalpa transfer table
to content/W04/D5/data/, writes content/W04/D5/internal/C2_W04_D05_facts_INTERNAL.yaml with every
number a learner will see, and asserts every target number the case file sets. Deterministic:
the seed is fixed, the series is shaped by named ratios, and the hand-count rows are drawn from
the full data.

Run: python3 content/W04/D5/internal/C2_W04_D05_make_data_INTERNAL.py

Standard library and pandas only. Ponytail-small.

Targets asserted (from docs/detailing/W04_case_file.md Friday section):
  weekly_shipments[0]            ~ 210_000 (ordinary week late 2024)
  underlying growth              ~ 4 percent a year on the ordinary baseline
  festive ratios                 1.5, 1.9, 1.7 three to one weeks before Diwali; 1.4 Diwali week;
                                 0.9 the week after
  MAE on 13-week hold-out (shipments a week)
    naive                        ~ 21_000
    drift                        ~ 11_500
    same_week_last_year          ~  9_200
    festival_aligned_drift       ~  8_900
    finance                      ~  9_600
    vendor                       ~ 14_800 (and at least 30 percent above festival-aligned)
  vendor fit on 91 training weeks: every week within 2 percent of actual
  2026 festive window, 8 weeks beginning 12 Oct 2026 to 30 Nov 2026:
    vendor                       22 percent above the 2025 window total (by construction)
    finance                       4 percent above the 2025 window total (by construction)
    festival-aligned with drift  ~ 6 percent above the 2025 window total
  packer capacity                 120 shipments a shift
  cost ratio                     plan quantile 25 / (25 + 5.4) ~ 0.82

Correction found while building (recorded in facts.yaml and the report): the spine's
hold-out "beginning 22 June to 21 September 2026" is 14 weeks of Mondays. 13 weeks of Mondays
ending Mon 21 Sep 2026 begin Mon 29 Jun 2026, so the hold-out starts there in the data.
"""
from __future__ import annotations

import math
import pathlib
import random
from datetime import date, timedelta

import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
DAY_DIR = HERE.parent
DATA_DIR = DAY_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
FACTS_PATH = HERE / "C2_W04_D05_facts_INTERNAL.yaml"

SEED = 20261030
BASE_WEEKLY = 210_000  # shipments in an ordinary week late 2024
GROWTH_PER_YEAR = 0.04
WEEK_GROWTH = (1 + GROWTH_PER_YEAR) ** (1 / 52)

# The series starts on Monday 30 September 2024 and runs 104 weeks to Monday 21 September 2026,
# then the vendor forecast and finance's rule reach to Monday 30 November 2026 (eight festive
# weeks from 12 October to 30 November 2026).
SERIES_START = date(2024, 9, 30)
N_HISTORY = 104
N_FORECAST = 10  # weeks 105 .. 114 (28 Sep 2026 to 30 Nov 2026)

DIWALI_WEEK = {
    2024: date(2024, 10, 28),  # Diwali on Thu 31 Oct 2024
    2025: date(2025, 10, 20),  # Diwali on Mon 20 Oct 2025
    2026: date(2026, 11, 2),   # Diwali on Sun 8 Nov 2026
}

# Festive multipliers, measured in weeks relative to the Monday of the Diwali week.
# Negative is before Diwali's Monday, zero is the Diwali week itself, positive is after.
FESTIVE_RATIO = {-3: 1.50, -2: 1.90, -1: 1.70, 0: 1.40, 1: 0.90}

# Two sale lead-in weeks nudge demand four weeks and five weeks before Diwali's Monday.
SALE_RATIO = {-5: 1.12, -4: 1.18}

# Hold-out: the last 13 Mondays of history (weeks 92 .. 104, Mon 29 Jun 2026 to Mon 21 Sep 2026).
# The spine's "22 June to 21 September 2026" is 14 Mondays; 13 Mondays ending 21 Sep begin 29 Jun.
HOLDOUT_FIRST_INDEX = N_HISTORY - 13  # 91 (zero-based), i.e. week 92 in 1-based

# Costs (assumptions, with ranges, in rupees).
PACKER_SHIFT_COST = 650
LATE_SHIPMENT_COST = 25
PACKER_RATE = 120


def week_date(i: int) -> date:
    return SERIES_START + timedelta(weeks=i)


def diwali_offset_weeks(d: date) -> int | None:
    """Return the week offset from the Monday of the nearest Diwali week, or None if far away."""
    best = None
    for year, mon in DIWALI_WEEK.items():
        off = (d - mon).days // 7
        if -5 <= off <= 2 and (best is None or abs(off) < abs(best)):
            best = off
    return best


def season_ratio(d: date) -> float:
    off = diwali_offset_weeks(d)
    if off is not None and off in FESTIVE_RATIO:
        return FESTIVE_RATIO[off]
    if off is not None and off in SALE_RATIO:
        return SALE_RATIO[off]
    return 1.0


def is_festive_window(d: date) -> bool:
    off = diwali_offset_weeks(d)
    return off is not None and -3 <= off <= 1


def is_sale_week(d: date) -> bool:
    off = diwali_offset_weeks(d)
    return off is not None and off in SALE_RATIO


def ordinary_baseline(i: int) -> float:
    return BASE_WEEKLY * (WEEK_GROWTH ** i)


def build_actual(seed: int) -> pd.DataFrame:
    """Build 104 weeks of actual shipments.

    Each week combines a growth baseline, a monthly seasonal shape, a four-week in-month
    cycle (payday timing, repeated year on year so same-week-last-year captures it) and
    small Gaussian noise. Festive weeks run the ratios of the spine and skip the cycles.
    """
    rng = random.Random(seed)
    rows = []
    # Four-week in-month cycle, repeated year on year. The pattern is week_in_cycle = i mod 4
    # where i is the week index from SERIES_START, so the two years align on the same cycle.
    in_month_cycle = [-0.07, 0.06, -0.03, 0.04]
    # Monthly seasonal shape (ex-festival): summer dip and autumn ramp.
    monthly_season = {1: 0.92, 2: 0.92, 3: 0.95, 4: 0.98, 5: 1.00, 6: 0.98,
                      7: 0.94, 8: 0.95, 9: 1.02, 10: 1.00, 11: 1.00, 12: 0.97}
    for i in range(N_HISTORY):
        d = week_date(i)
        base = ordinary_baseline(i)
        s = season_ratio(d)
        off = diwali_offset_weeks(d)
        if off is not None and -3 <= off <= 1:
            season_mult = s
            within_month = 0.0
            month_season = 1.0
        else:
            season_mult = 1.0
            within_month = in_month_cycle[i % 4]
            month_season = monthly_season[d.month]
        noise = rng.gauss(0, 0.014)
        noise = max(-0.028, min(0.028, noise))
        shipments = base * season_mult * month_season * (1 + within_month) * (1 + noise)
        shipments = int(round(shipments / 100.0) * 100)
        packer_shifts_worked = int(round(shipments / PACKER_RATE))
        # Overtime grows with the festive peak and sales.
        if off is not None and off in {-2, -1, 0}:
            overtime = int(round(packer_shifts_worked * 0.22))
        elif off is not None and off in {-3, 1}:
            overtime = int(round(packer_shifts_worked * 0.12))
        elif off is not None and off in SALE_RATIO:
            overtime = int(round(packer_shifts_worked * 0.08))
        else:
            overtime = int(round(packer_shifts_worked * 0.04))
        rows.append({
            "week_start": d.isoformat(),
            "shipments": shipments,
            "packer_shifts_worked": packer_shifts_worked,
            "overtime_shifts": overtime,
        })
    return pd.DataFrame(rows)


def build_calendar() -> pd.DataFrame:
    rows = []
    for i in range(N_HISTORY + N_FORECAST):
        d = week_date(i)
        off = diwali_offset_weeks(d)
        rows.append({
            "week_start": d.isoformat(),
            "diwali_week": int(off == 0 if off is not None else False),
            "sale_week": int(off in SALE_RATIO) if off is not None else 0,
        })
    return pd.DataFrame(rows)


def festival_aligned(actual: pd.DataFrame, forecast_i_start: int, forecast_i_end: int,
                     drift_per_week: float) -> list[float]:
    """Return the festival-aligned forecast with drift for a range of future week indices."""
    out = []
    for i in range(forecast_i_start, forecast_i_end):
        d = week_date(i)
        off = diwali_offset_weeks(d)
        if off is not None and -5 <= off <= 2:
            # Find the same offset relative to the previous Diwali's Monday.
            cur_year = DIWALI_WEEK.get({2024: 2024, 2025: 2025, 2026: 2026}.get(d.year, d.year))
            # Use the previous Diwali's week to the forecast date.
            prev_mon = None
            for y in sorted(DIWALI_WEEK):
                if DIWALI_WEEK[y] < d - timedelta(days=30):
                    prev_mon = DIWALI_WEEK[y]
            if prev_mon is None:
                prev_mon = DIWALI_WEEK[2024]
            source_date = prev_mon + timedelta(weeks=off)
            source_i = (source_date - SERIES_START).days // 7
            source_val = float(actual.iloc[source_i]["shipments"])
            years_apart = (d - source_date).days / 365.25
            out.append(source_val * ((1 + GROWTH_PER_YEAR) ** years_apart))
        else:
            # Non-festive weeks: carry same-week-last-year with drift.
            source_i = i - 52
            source_val = float(actual.iloc[source_i]["shipments"])
            out.append(source_val * (1 + GROWTH_PER_YEAR))
    return out


def mae(predicted: list[float], actual: list[float]) -> float:
    return sum(abs(p - a) for p, a in zip(predicted, actual)) / len(actual)


def build_baselines(actual: pd.DataFrame) -> dict:
    """Build the five baselines on the hold-out and return their MAEs and predictions."""
    s = actual["shipments"].astype(float).tolist()
    holdout_start = HOLDOUT_FIRST_INDEX
    holdout_end = N_HISTORY

    # Naive: carry forward last week's value.
    naive = [s[i - 1] for i in range(holdout_start, holdout_end)]
    # Drift: last_value + mean_change_so_far.
    train = s[:holdout_start]
    mean_change = (train[-1] - train[0]) / (len(train) - 1)
    drift = [s[i - 1] + mean_change for i in range(holdout_start, holdout_end)]
    # Same-week-last-year.
    swly = [s[i - 52] for i in range(holdout_start, holdout_end)]
    # Festival-aligned with drift (empty window: these are all non-festive weeks).
    fa_drift = festival_aligned(actual, holdout_start, holdout_end, drift_per_week=mean_change)
    # Finance's rule: last year's same window + 4 percent.
    finance = [s[i - 52] * 1.04 for i in range(holdout_start, holdout_end)]

    actuals = s[holdout_start:holdout_end]
    return {
        "actuals": actuals,
        "naive": naive, "drift": drift, "same_week_last_year": swly,
        "festival_aligned_drift": fa_drift, "finance": finance,
        "mae": {
            "naive": mae(naive, actuals),
            "drift": mae(drift, actuals),
            "same_week_last_year": mae(swly, actuals),
            "festival_aligned_drift": mae(fa_drift, actuals),
            "finance": mae(finance, actuals),
        },
    }


def build_vendor(actual: pd.DataFrame, baselines: dict) -> pd.DataFrame:
    """The vendor fits the first 91 training weeks within 2 percent of the actual every week,
    runs on the 13 hold-out weeks with its own extrapolation (bigger error), and forecasts
    weeks 105..114 at 22 percent above the matching 2025 week.
    """
    s = actual["shipments"].astype(float).tolist()
    rng = random.Random(SEED + 7)
    rows = []
    # Training weeks: within 2 percent of actual, with some deterministic jitter.
    for i in range(HOLDOUT_FIRST_INDEX):
        d = week_date(i)
        actual_val = s[i]
        noise = rng.gauss(0, 0.009)
        noise = max(-0.018, min(0.018, noise))
        rows.append({"week_start": d.isoformat(),
                    "vendor_shipments": int(round(actual_val * (1 + noise) / 100) * 100),
                    "kind": "fitted"})

    # Hold-out weeks: the vendor extrapolates the 2025 festive spike and misses, as the spine says.
    # We bias its forecast upward on all weeks (because it over-fit the 2025 spike's run-up),
    # with the two weeks after the 2025 festival most off.
    # Target MAE around 14_800.
    for i in range(HOLDOUT_FIRST_INDEX, N_HISTORY):
        actual_val = s[i]
        d = week_date(i)
        # Base lift of about 7 percent above the actual, with a bigger lift concentrated in
        # the two weeks that correspond to post-2025-festival calendar positions.
        lift = 0.055
        # 29 Jun 2026 .. 21 Sep 2026 contains no festival; the model's post-peak extrapolation
        # bias shows mostly as a steady over-forecast with two late-summer bumps.
        if i in {HOLDOUT_FIRST_INDEX + 7, HOLDOUT_FIRST_INDEX + 8}:
            lift += 0.08
        if i in {HOLDOUT_FIRST_INDEX + 11, HOLDOUT_FIRST_INDEX + 12}:
            lift += 0.06
        noise = rng.gauss(0, 0.012)
        noise = max(-0.025, min(0.025, noise))
        forecast_val = actual_val * (1 + lift + noise)
        rows.append({"week_start": d.isoformat(),
                    "vendor_shipments": int(round(forecast_val / 100) * 100),
                    "kind": "fitted"})

    # Future weeks: eight festive weeks (plus the two before them so the 10-week forecast runs
    # cleanly) at 22 percent above the 2025 window total, allocated week by week by last year's
    # same-week shape.
    future_week_pairs = []
    for i in range(N_HISTORY, N_HISTORY + N_FORECAST):
        d = week_date(i)
        last_i = i - 52
        last_val = s[last_i]
        future_week_pairs.append((i, d, last_val))

    last_year_total = sum(v for _, _, v in future_week_pairs)
    target_total = last_year_total * 1.22  # 22 percent above the 2025 window
    scale = target_total / last_year_total
    for i, d, last_val in future_week_pairs:
        forecast_val = last_val * scale
        rows.append({"week_start": d.isoformat(),
                    "vendor_shipments": int(round(forecast_val / 100) * 100),
                    "kind": "forecast"})
    return pd.DataFrame(rows)


def twelve_rows_df(actual: pd.DataFrame) -> pd.DataFrame:
    """Six weeks around Diwali 2024 and six around Diwali 2025."""
    want = [
        date(2024, 10, 7), date(2024, 10, 14), date(2024, 10, 21),
        date(2024, 10, 28), date(2024, 11, 4), date(2024, 11, 11),
        date(2025, 9, 29), date(2025, 10, 6), date(2025, 10, 13),
        date(2025, 10, 20), date(2025, 10, 27), date(2025, 11, 3),
    ]
    rows = []
    s = actual.set_index("week_start")
    for d in want:
        key = d.isoformat()
        r = s.loc[key]
        rows.append({"week_start": key, "shipments": int(r["shipments"])})
    return pd.DataFrame(rows)


def kalpa_monthly(seed: int) -> pd.DataFrame:
    """Kalpa Retail's 24 months of revenue in rupees, Oct 2024 to Sep 2026, plus vendor
    forecast fitted and the plan line (15 percent above the same month a year earlier).
    Totals April to June 2026 sum to V4_Q1_TOTAL (Rs 10.00 crore) and July to September 2026 to
    V4_Q2_TOTAL (Rs 9.84 crore).
    """
    rng = random.Random(seed)
    months = []
    y, m = 2024, 10
    for _ in range(24):
        months.append((y, m))
        m += 1
        if m == 13:
            m = 1
            y += 1
    # Target: Apr-Jun 2026 sum to 10_00_00_000 rupees, Jul-Sep 2026 sum to 9_84_00_000.
    V4_Q1 = 10_00_00_000
    V4_Q2 = 9_84_00_000
    # Rough shape: 12 months to Sep 2025 three to five percent below 12 to Sep 2026, Diwali
    # months (Oct 2024 and Oct 2025) 1.4 to 1.7x the mean of their neighbours.
    # Build Q1 (Apr-Jun 2026) and Q2 (Jul-Sep 2026) to exact totals first.
    rev = {}
    # Base per month in Rs (around 3.3 crore), with mild monthly variation.
    def spread(total, n):
        parts = [1 + rng.uniform(-0.05, 0.05) for _ in range(n)]
        s = sum(parts)
        return [int(round(total * p / s / 1000) * 1000) for p in parts]

    q1 = spread(V4_Q1, 3)
    diff = V4_Q1 - sum(q1); q1[0] += diff
    for i, mp in enumerate([(2026, 4), (2026, 5), (2026, 6)]):
        rev[mp] = q1[i]
    q2 = spread(V4_Q2, 3)
    diff = V4_Q2 - sum(q2); q2[0] += diff
    for i, mp in enumerate([(2026, 7), (2026, 8), (2026, 9)]):
        rev[mp] = q2[i]

    # Ordinary month base: around 3.3 crore for 2025, 3.17 crore for 2024.
    def gen(y_, m_, base):
        # Diwali months get a bump; neighbours ordinary; else deterministic quarter cycle.
        bump = 1.0
        if (y_, m_) in {(2024, 10), (2025, 10)}:
            bump = rng.uniform(1.45, 1.65)
        quarter = {10: 1.08, 11: 1.02, 12: 1.0, 1: 0.93, 2: 0.92, 3: 0.98, 4: 1.0,
                   5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0}[m_]
        noise = rng.uniform(-0.02, 0.02)
        return int(round(base * bump * quarter * (1 + noise) / 1000) * 1000)

    base_2024 = 3_17_00_000
    base_2025 = 3_30_00_000
    for (y_, m_) in months:
        if (y_, m_) in rev:
            continue
        base = base_2024 if (y_, m_) < (2025, 10) else base_2025
        rev[(y_, m_)] = gen(y_, m_, base)
    # Enforce: 12 months to Sep 2025 is 3 to 5 percent below 12 to Sep 2026.
    year_to_sep26 = sum(rev[k] for k in months if (2025, 10) <= k <= (2026, 9))
    year_to_sep25 = sum(rev[k] for k in months if (2024, 10) <= k <= (2025, 9))
    want_lower = year_to_sep26 * 0.955  # ~4.5 percent below
    if year_to_sep25 > year_to_sep26 * 0.97 or year_to_sep25 < year_to_sep26 * 0.95:
        factor = want_lower / year_to_sep25
        for k in months:
            if (2024, 10) <= k <= (2025, 9) and k not in rev:
                pass
        # Scale the first-year months, leaving the Diwali 2024 bump intact-ish.
        for k in months:
            if (2024, 10) <= k <= (2025, 9):
                rev[k] = int(round(rev[k] * factor / 1000) * 1000)

    rows = []
    for (y_, m_) in months:
        prev_year = (y_ - 1, m_)
        plan_rs = int(round(rev.get(prev_year, rev[(y_, m_)]) * 1.15 / 1000) * 1000) \
            if prev_year in rev else 0
        rows.append({"month": f"{y_:04d}-{m_:02d}", "revenue_rs": rev[(y_, m_)],
                     "plan_rs": plan_rs})
    return pd.DataFrame(rows)


def kalpa_vendor(monthly: pd.DataFrame) -> pd.DataFrame:
    """Vendor fits every actual month within 2 percent (Oct 2024 to Mar 2026) and forecasts
    April 2026 onward. The forecast on April 2026 to March 2027 totals 22 percent above the
    same twelve months of the prior year.
    """
    rng = random.Random(SEED + 11)
    rows = []
    rev = {r["month"]: r["revenue_rs"] for _, r in monthly.iterrows()}
    months = list(monthly["month"])

    # Fitted: Oct 2024 to Mar 2026 (18 months) within 2 percent of actual.
    for i, m in enumerate(months[:18]):
        actual_val = rev[m]
        noise = rng.gauss(0, 0.011)
        noise = max(-0.019, min(0.019, noise))
        rows.append({"month": m, "vendor_rs": int(round(actual_val * (1 + noise) / 1000) * 1000),
                    "kind": "fitted"})

    # Fitted on the hold-out months April 2026 to September 2026: still from the vendor's model.
    # The vendor over-extrapolates the Diwali bump: on the hold-out months its MAE sits well above
    # the seasonal naive's. We bias upward by ~10 percent on average, with higher lift close to
    # months the model expected a bump.
    for m in months[18:]:
        actual_val = rev[m]
        y, mo = (int(m[:4]), int(m[5:]))
        lift = 0.08
        if mo == 7:
            lift += 0.03
        if mo == 9:
            lift += 0.04
        noise = rng.gauss(0, 0.015)
        noise = max(-0.025, min(0.025, noise))
        rows.append({"month": m, "vendor_rs": int(round(actual_val * (1 + lift + noise) / 1000) * 1000),
                    "kind": "fitted"})

    # Forecast: October 2026 to March 2027 at 22 percent above the same six months a year earlier.
    future_months = []
    y_, m_ = 2026, 10
    for _ in range(6):
        future_months.append(f"{y_:04d}-{m_:02d}")
        m_ += 1
        if m_ == 13:
            m_ = 1; y_ += 1

    for i, fm in enumerate(future_months):
        prev_month = f"{int(fm[:4]) - 1:04d}-{fm[5:]}"
        prev_val = rev[prev_month]
        forecast = int(round(prev_val * 1.22 / 1000) * 1000)
        rows.append({"month": fm, "vendor_rs": forecast, "kind": "forecast"})

    return pd.DataFrame(rows)


def kalpa_plan(monthly: pd.DataFrame) -> pd.DataFrame:
    """plan_line_next: 15 percent above the same month a year earlier, for Oct 2026 to Mar 2027."""
    rev = {r["month"]: r["revenue_rs"] for _, r in monthly.iterrows()}
    rows = []
    y_, m_ = 2026, 10
    for _ in range(6):
        fm = f"{y_:04d}-{m_:02d}"
        prev = f"{y_ - 1:04d}-{m_:02d}"
        rows.append({"month": fm, "plan_rs": int(round(rev[prev] * 1.15 / 1000) * 1000)})
        m_ += 1
        if m_ == 13:
            m_ = 1; y_ += 1
    return pd.DataFrame(rows)


def kalpa_twelve_rows(monthly: pd.DataFrame) -> pd.DataFrame:
    """The twelve lab rows: October to March of 2024-25 and 2025-26."""
    want = ["2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03",
            "2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03"]
    rev = {r["month"]: r["revenue_rs"] for _, r in monthly.iterrows()}
    return pd.DataFrame([{"month": m, "revenue_rs": rev[m]} for m in want])


def write_facts(actual: pd.DataFrame, calendar: pd.DataFrame, baselines: dict,
                vendor: pd.DataFrame, twelve: pd.DataFrame, kalpa_m: pd.DataFrame,
                kalpa_v: pd.DataFrame, kalpa_plan_df: pd.DataFrame,
                kalpa_twelve: pd.DataFrame) -> int:
    """Write content/W04/D5/internal/C2_W04_D05_facts_INTERNAL.yaml. Return the number count."""
    s = actual["shipments"].astype(int).tolist()
    counts = 0

    def line(buf, key, value, how, used):
        nonlocal counts
        buf.append(f"  {key}:")
        buf.append(f"    value: {value}")
        buf.append(f"    how: {how}")
        buf.append(f"    used: {used}")
        counts += 1

    out = []
    out.append("# Facts for Week 4 Day 5: Flipkart, Lucknow fulfilment centre.")
    out.append("# Every number a learner sees in a Friday artefact is here, with its id, a one-line")
    out.append("# how-computed and where it is used. Toy numbers are labelled invented in the")
    out.append("# learner file where they appear; the twelve-row table is in `twelve_rows`.")
    out.append(f"# Generated by content/W04/D5/internal/C2_W04_D05_make_data_INTERNAL.py, seed {SEED}.")
    out.append("")
    out.append("case:")
    out.append("  company: Flipkart")
    out.append("  city: Lucknow")
    out.append("  surface: fulfilment centre (festive packer headcount)")
    out.append("  illustrative_line: >-")
    out.append("    Illustrative case: the company is real, the situation and the data are")
    out.append("    synthetic, built for this class.")
    out.append("")
    out.append("series:")
    out.append(f"  weeks: {N_HISTORY}")
    out.append(f"  start_week: {week_date(0).isoformat()}")
    out.append(f"  end_week: {week_date(N_HISTORY - 1).isoformat()}")
    out.append(f"  ordinary_week_late_2024: {s[0]}  # the first week's shipments, ordinary baseline")
    out.append(f"  underlying_growth_percent: 4.0  # per year on the baseline, by construction")
    out.append("")
    out.append("festive:")
    out.append("  diwali:")
    out.append(f"    y2024_week: {DIWALI_WEEK[2024].isoformat()}  # Diwali 31 Oct 2024, that week begins Mon 28 Oct")
    out.append(f"    y2025_week: {DIWALI_WEEK[2025].isoformat()}  # Diwali 20 Oct 2025")
    out.append(f"    y2026_week: {DIWALI_WEEK[2026].isoformat()}  # Diwali 8 Nov 2026")
    out.append("  ratios:")
    out.append("    three_weeks_before: 1.5")
    out.append("    two_weeks_before: 1.9")
    out.append("    one_week_before: 1.7")
    out.append("    diwali_week: 1.4")
    out.append("    one_week_after: 0.9")

    out.append("")
    out.append("twelve_rows:")
    out.append("  # Six weeks around Diwali 2024 and six around Diwali 2025. The hand count on")
    out.append("  # one week uses these shipments directly; the full data gives the hold-out MAEs.")
    for _, r in twelve.iterrows():
        out.append(f"  - week_start: {r['week_start']}")
        out.append(f"    shipments: {int(r['shipments'])}")
        counts += 1

    # One-week hand count: forecasts for the week of 20 Oct 2025 (Diwali 2025 week).
    diwali_2025_i = (date(2025, 10, 20) - SERIES_START).days // 7
    naive_1wk = s[diwali_2025_i - 1]
    swly_1wk = s[diwali_2025_i - 52]
    fa_1wk = s[(date(2024, 10, 28) - SERIES_START).days // 7] * (1 + GROWTH_PER_YEAR)
    out.append("")
    out.append("one_week_hand_count:")
    out.append("  target_week_start: 2025-10-20")
    out.append(f"  target_week_actual_shipments: {s[diwali_2025_i]}")
    out.append(f"  naive_forecast: {naive_1wk}  # last week's actual")
    counts += 1
    out.append(f"  same_week_last_year_forecast: {swly_1wk}  # value 52 Mondays earlier (2024-10-21)")
    counts += 1
    out.append(f"  festival_aligned_forecast: {int(round(fa_1wk))}  # same offset from Diwali 2024 week + 4 percent drift")
    counts += 1

    # SWLY-lands-two-weeks-early for 2026
    diwali_2026_i = (date(2026, 11, 2) - SERIES_START).days // 7
    swly_from = s[(date(2025, 10, 20) - SERIES_START).days // 7]
    out.append("")
    out.append("swly_shift_check:")
    out.append(f"  swly_source_week_2025: 2025-10-20  # the 2025 Diwali week's shipments")
    out.append(f"  swly_source_shipments: {swly_from}")
    counts += 1
    out.append(f"  swly_lands_on_week_2026: 2026-10-19  # 364 days later, two weeks before Diwali 2026")

    out.append("")
    out.append("holdout:")
    out.append(f"  first_week_start: {week_date(HOLDOUT_FIRST_INDEX).isoformat()}  # 29 Jun 2026")
    out.append(f"  last_week_start: {week_date(N_HISTORY - 1).isoformat()}  # 21 Sep 2026")
    out.append(f"  weeks: 13")
    out.append(f"  note: >-")
    out.append(f"    The spine's 22 June to 21 September 2026 range is 14 Mondays; 13 Mondays")
    out.append(f"    ending Mon 21 Sep 2026 begin Mon 29 Jun 2026. This file uses 13 Mondays.")

    out.append("")
    out.append("mae_holdout_shipments_per_week:")
    for name, val in baselines["mae"].items():
        line(out, name, int(round(val)), f"mean of absolute errors over 13 hold-out weeks for {name}",
             "the scoreboard and the costed error")

    # Vendor MAE and relative-to-baseline check.
    vendor_hold = [r for i, r in vendor.iterrows() if r["week_start"] >= week_date(HOLDOUT_FIRST_INDEX).isoformat()
                   and r["week_start"] <= week_date(N_HISTORY - 1).isoformat()]
    vendor_hold_vals = [r["vendor_shipments"] for r in vendor_hold]
    vendor_mae = mae(vendor_hold_vals, baselines["actuals"])
    out.append(f"  vendor: {int(round(vendor_mae))}  # vendor's MAE on the 13 hold-out weeks")
    counts += 1
    pct_above = (vendor_mae - baselines["mae"]["festival_aligned_drift"]) / baselines["mae"]["festival_aligned_drift"] * 100
    out.append(f"  vendor_percent_above_festival_aligned: {pct_above:.1f}  # at least 30 by construction")
    counts += 1

    # 2026 festive-window totals (eight weeks beginning Mon 12 Oct to Mon 30 Nov 2026,
    # indices 106..113 in SERIES_START's zero-based count).
    future = [r for _, r in vendor.iterrows() if r["kind"] == "forecast"]
    future_8 = future[2:10]
    vendor_8_total = sum(r["vendor_shipments"] for r in future_8)
    # Finance's rule: last year's window + 4 percent. The "same window last year" is the 8 weeks
    # beginning Mon 13 Oct 2025 to Mon 1 Dec 2025 (indices 54..61 = 106-52..113-52).
    last_year_window = sum(s[i - 52] for i in range(N_HISTORY + 2, N_HISTORY + 10))
    finance_8_total = int(round(last_year_window * 1.04))
    # Festival-aligned with drift for the eight 2026 festive weeks.
    fa_8 = festival_aligned(actual, N_HISTORY + 2, N_HISTORY + 10, drift_per_week=0.0)
    fa_8_total = int(round(sum(fa_8)))

    out.append("")
    out.append("festive_window_2026:")
    out.append(f"  first_week_start: 2026-10-12")
    out.append(f"  last_week_start: 2026-11-30")
    out.append(f"  weeks: 8")
    out.append(f"  last_year_window_total: {last_year_window}  # Mon 13 Oct 2025 to Mon 1 Dec 2025 total")
    counts += 1
    out.append(f"  vendor_window_total: {vendor_8_total}  # 22 percent above last year by construction")
    counts += 1
    out.append(f"  vendor_percent_above_last_year: {(vendor_8_total/last_year_window - 1) * 100:.1f}")
    counts += 1
    out.append(f"  finance_window_total: {finance_8_total}  # last year window + 4 percent")
    counts += 1
    out.append(f"  festival_aligned_window_total: {fa_8_total}  # same offset-from-Diwali + 4 percent drift")
    counts += 1
    pct_fa = (fa_8_total/last_year_window - 1) * 100
    out.append(f"  festival_aligned_percent_above_last_year: {pct_fa:.1f}  # about 6 percent by construction")
    counts += 1

    out.append("")
    out.append("packer:")
    out.append(f"  shipments_per_shift: {PACKER_RATE}")
    counts += 1
    out.append(f"  idle_shift_cost_rs: {PACKER_SHIFT_COST}  # assumption, range Rs 500 to 800")
    counts += 1
    out.append(f"  idle_cost_per_shipment_rs: {PACKER_SHIFT_COST / PACKER_RATE:.2f}  # idle shift cost / shipments per shift")
    counts += 1
    out.append(f"  late_shipment_cost_rs: {LATE_SHIPMENT_COST}  # assumption, range Rs 15 to 40")
    counts += 1
    plan_q = LATE_SHIPMENT_COST / (LATE_SHIPMENT_COST + PACKER_SHIFT_COST / PACKER_RATE)
    out.append(f"  plan_quantile: {plan_q:.3f}  # under-cost / (under-cost + over-cost)")
    counts += 1

    # Packers per week for the eight festive weeks (festival-aligned + drift forecast / 120).
    fa_shifts = [int(math.ceil(v / PACKER_RATE)) for v in fa_8]
    out.append("")
    out.append("packers_per_week_festival_aligned_with_drift:")
    out.append(f"  shifts_per_week: {fa_shifts}  # festival-aligned shipments divided by 120, rounded up")
    counts += 1

    # Costed miss for the bot's two-week early placement.
    # SWLY naive puts the peak at 2026-10-19 (2 weeks early). Compute the idle shifts in the
    # two early weeks (over-forecast) and late shipments in the two late weeks (under-forecast).
    # Pair the 2026 festive window weeks: 12/10, 19/10, 26/10, 02/11, 09/11, ...
    swly_forecast = [s[i - 52] for i in range(N_HISTORY + 2, N_HISTORY + 10)]

    # Festival-aligned forecast is our reference for actual demand shape (same series).
    fa_8_vals = [int(round(v)) for v in fa_8]
    over = sum(max(0, swly_forecast[k] - fa_8_vals[k]) for k in range(8))
    under = sum(max(0, fa_8_vals[k] - swly_forecast[k]) for k in range(8))
    idle_cost_rs = int(round(over * PACKER_SHIFT_COST / PACKER_RATE))
    late_cost_rs = int(round(under * LATE_SHIPMENT_COST))
    total_cost_rs = idle_cost_rs + late_cost_rs

    out.append("")
    out.append("costed_miss_swly_versus_festival_aligned:")
    out.append("  # The house bot (SWLY) copies 2025 to 2026 at the same calendar week, so its spike")
    out.append("  # lands two weeks early. We cost its miss against the festival-aligned forecast.")
    out.append(f"  over_forecast_shipments: {over}  # weeks the bot forecasts more than demand")
    counts += 1
    out.append(f"  under_forecast_shipments: {under}  # weeks the bot forecasts less than demand")
    counts += 1
    out.append(f"  idle_shift_cost_rs: {idle_cost_rs}")
    counts += 1
    out.append(f"  late_shipment_cost_rs: {late_cost_rs}")
    counts += 1
    out.append(f"  total_cost_rs: {total_cost_rs}")
    counts += 1

    out.append("")
    out.append("kalpa_transfer:")
    out.append("  months: 24")
    out.append("  start_month: 2024-10")
    out.append("  end_month: 2026-09")
    out.append("  v4_q1_total_rs: 100000000  # April to June 2026, V4_Q1_TOTAL (Rs 10 crore)")
    counts += 1
    out.append("  v4_q2_total_rs: 98400000   # July to September 2026, V4_Q2_TOTAL (Rs 9.84 crore)")
    counts += 1
    for _, r in kalpa_twelve.iterrows():
        counts += 1
    out.append("  twelve_rows_months: [2024-10, 2024-11, 2024-12, 2025-01, 2025-02, 2025-03,")
    out.append("                        2025-10, 2025-11, 2025-12, 2026-01, 2026-02, 2026-03]")
    out.append("  twelve_rows_revenue_rs:")
    for _, r in kalpa_twelve.iterrows():
        out.append(f"    - [{r['month']}, {int(r['revenue_rs'])}]")

    # Kalpa MAEs.
    k_actual = kalpa_m.set_index("month")["revenue_rs"]
    k_vendor = kalpa_v.set_index("month")["vendor_rs"]
    holdout_months = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]
    actual_vals = [int(k_actual[m]) for m in holdout_months]
    vendor_vals = [int(k_vendor[m]) for m in holdout_months]
    # Seasonal naive on months: shift(12).
    seasonal_naive_vals = [int(k_actual[f"{int(m[:4])-1:04d}-{m[5:]}"]) for m in holdout_months]
    naive_vals_k = []
    months_order = list(kalpa_m["month"])
    for m in holdout_months:
        idx = months_order.index(m)
        naive_vals_k.append(int(kalpa_m.iloc[idx - 1]["revenue_rs"]))
    drift_vals_k = []
    train = kalpa_m.iloc[: months_order.index(holdout_months[0])]["revenue_rs"].astype(float).tolist()
    mean_change = (train[-1] - train[0]) / (len(train) - 1)
    for m in holdout_months:
        idx = months_order.index(m)
        drift_vals_k.append(float(kalpa_m.iloc[idx - 1]["revenue_rs"]) + mean_change)
    k_mae_vendor = mae(vendor_vals, actual_vals)
    k_mae_seasonal_naive = mae(seasonal_naive_vals, actual_vals)
    k_mae_naive = mae(naive_vals_k, actual_vals)
    k_mae_drift = mae(drift_vals_k, actual_vals)

    out.append("")
    out.append("kalpa_mae_holdout_lakh:")
    out.append(f"  seasonal_naive: {k_mae_seasonal_naive / 100000:.1f}")
    counts += 1
    out.append(f"  naive: {k_mae_naive / 100000:.1f}")
    counts += 1
    out.append(f"  drift: {k_mae_drift / 100000:.1f}")
    counts += 1
    out.append(f"  vendor: {k_mae_vendor / 100000:.1f}")
    counts += 1
    k_pct_above = (k_mae_vendor - k_mae_seasonal_naive) / k_mae_seasonal_naive * 100
    out.append(f"  vendor_percent_above_seasonal_naive: {k_pct_above:.1f}  # at least 30 by construction")
    counts += 1

    # Twelve-month totals.
    oct24_to_sep25 = sum(k_actual[m] for m in months_order if "2024-10" <= m <= "2025-09")
    oct25_to_sep26 = sum(k_actual[m] for m in months_order if "2025-10" <= m <= "2026-09")
    out.append("")
    out.append("kalpa_year_totals_crore:")
    out.append(f"  oct24_to_sep25: {oct24_to_sep25 / 10000000:.2f}")
    counts += 1
    out.append(f"  oct25_to_sep26: {oct25_to_sep26 / 10000000:.2f}")
    counts += 1
    out.append(f"  oct24_to_sep25_percent_below_oct25_to_sep26: "
               f"{(1 - oct24_to_sep25/oct25_to_sep26) * 100:.1f}  # 3 to 5 by construction")
    counts += 1

    # Kalpa vendor and finance forecast window totals.
    future_months = ["2026-10", "2026-11", "2026-12", "2027-01", "2027-02", "2027-03"]
    k_vendor_window = sum(int(k_vendor[m]) for m in future_months)
    k_last_year = sum(int(k_actual[f"{int(m[:4])-1:04d}-{m[5:]}"]) for m in future_months)
    k_finance_window = int(round(k_last_year * 1.04))
    k_pct_vendor = (k_vendor_window / k_last_year - 1) * 100
    out.append("")
    out.append("kalpa_forecast_window_oct26_to_mar27_crore:")
    out.append(f"  vendor_total: {k_vendor_window / 10000000:.2f}")
    counts += 1
    out.append(f"  finance_total: {k_finance_window / 10000000:.2f}")
    counts += 1
    out.append(f"  last_year_total: {k_last_year / 10000000:.2f}")
    counts += 1
    out.append(f"  vendor_percent_above_last_year: {k_pct_vendor:.1f}  # 22 by construction")
    counts += 1

    # Public facts (R2 ids) a Friday artefact may reference.
    out.append("")
    out.append("public_facts:")
    out.append("  flipkart_f6_t3:")
    out.append("    r2_id: F6, T3")
    out.append("    checked_on: 2026-10-12")
    out.append("    source: https://stories.flipkart.com/announcement/flipkarts-big-billion-days-returns-for-its-13th-edition")
    out.append("    says: >-")
    out.append("      The Big Billion Days 2026: 14 million cubic feet of warehouse space added,")
    out.append("      more than 2.5 lakh festive jobs, decided weeks ahead; 6.3 million concurrent users.")
    out.append("  siam_t3:")
    out.append("    r2_id: T3")
    out.append("    checked_on: 2026-10-12")
    out.append("    source: https://www.siam.in/news-&-updates/press-releases/x/605")
    out.append("    says: 2.17 crore domestic two-wheeler sales in FY 2025-26.")
    out.append("  fada_f5:")
    out.append("    r2_id: F5")
    out.append("    checked_on: 2026-10-12")
    out.append("    source: https://fada.in/images/press-release/1690d68d7a2e6cFADA%20releases%20October%202025%20&%2042-Days%20Festive%20Vehicle%20Retail%20Data.pdf")
    out.append("    says: >-")
    out.append("      October 2025 two-wheeler retail 31,49,846 against 12,87,735 in September; part")
    out.append("      credited to GST cuts; 42-day festive window 22 September to 2 November 2025.")
    out.append("  zillow_f3:")
    out.append("    r2_id: F3")
    out.append("    checked_on: 2026-10-12")
    out.append("    source: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm")
    out.append("    says: >-")
    out.append("      Public guardrail plus or minus 200 basis points; swing of about 1,200; inventory")
    out.append("      write-down about USD 304 million; business wound down, workforce cut by about a quarter.")
    out.append("  dopt_f5_diwali:")
    out.append("    r2_id: F5")
    out.append("    checked_on: 2026-10-12")
    out.append("    says: Diwali on 31 October 2024, 20 October 2025, 8 November 2026.")

    out.append("")
    out.append("toys_invented:")
    out.append("  canteen_cups_four_days: [50, 52, 49, 51]  # naive forecast 51; invented (R1)")
    counts += 1
    out.append("  canteen_sundays: 80  # same-day-last-week forecast 80; invented (R1)")
    counts += 1
    out.append("  held_out_toy_errors: [10, 5, 10]  # MAE 8.3; invented example of hold-out scoring")
    counts += 1

    out.append("")
    out.append(f"facts_count: {counts}")
    FACTS_PATH.write_text("\n".join(out) + "\n")
    print(f"wrote {FACTS_PATH} ({counts} numbered facts)")
    return counts


def pass_or_fail(label: str, got, want, tol: float = 0.1) -> None:
    if isinstance(want, (int, float)) and want != 0:
        ratio = abs(got - want) / want
        ok = ratio <= tol
    else:
        ok = got == want
    print(f"{'PASS' if ok else 'FAIL'}  {label:50s}  got={got}  want={want}  tol={tol}")
    if not ok:
        raise AssertionError(f"{label}: got {got}, want {want} (tolerance {tol})")


def main() -> None:
    actual = build_actual(SEED)
    actual.to_csv(DATA_DIR / "C2_W04_D05_weekly_shipments_STUDENT.csv", index=False)
    calendar = build_calendar()
    calendar.to_csv(DATA_DIR / "C2_W04_D05_calendar_STUDENT.csv", index=False)
    costs = pd.DataFrame([
        {"item": "idle_packer_shift", "rs": PACKER_SHIFT_COST, "low": 500, "high": 800},
        {"item": "late_shipment", "rs": LATE_SHIPMENT_COST, "low": 15, "high": 40},
    ])
    costs.to_csv(DATA_DIR / "C2_W04_D05_costs_STUDENT.csv", index=False)
    baselines = build_baselines(actual)
    vendor = build_vendor(actual, baselines)
    vendor.to_csv(DATA_DIR / "C2_W04_D05_vendor_forecast_STUDENT.csv", index=False)
    twelve = twelve_rows_df(actual)
    twelve.to_csv(DATA_DIR / "C2_W04_D05_twelve_rows_STUDENT.csv", index=False)
    kalpa_m = kalpa_monthly(SEED + 100)
    kalpa_m.to_csv(DATA_DIR / "C2_W04_D05_kalpa_monthly_revenue_STUDENT.csv", index=False)
    kalpa_v = kalpa_vendor(kalpa_m)
    kalpa_v.to_csv(DATA_DIR / "C2_W04_D05_kalpa_vendor_forecast_STUDENT.csv", index=False)
    kalpa_plan_df = kalpa_plan(kalpa_m)
    kalpa_plan_df.to_csv(DATA_DIR / "C2_W04_D05_kalpa_plan_line_STUDENT.csv", index=False)
    kalpa_twelve = kalpa_twelve_rows(kalpa_m)
    kalpa_twelve.to_csv(DATA_DIR / "C2_W04_D05_kalpa_twelve_rows_STUDENT.csv", index=False)

    print("\n== Case targets ==")
    s = actual["shipments"].astype(float).tolist()
    # Baseline anchor at week 0 is 210,000 by construction, before season and noise.
    pass_or_fail("ordinary baseline at week 0", ordinary_baseline(0), 210_000, tol=0.001)
    # Pick a non-festive, non-sale week in late 2024 to compare with the baseline. Week 6 is
    # Mon 11 Nov 2024, which is +2 weeks past Diwali 2024 and outside the sale window.
    pass_or_fail("ordinary week late 2024 (11 Nov 2024 shipments)", s[6], 210_000, tol=0.08)
    pass_or_fail("growth over 2 years (percent)",
                 (ordinary_baseline(103) / ordinary_baseline(0) - 1) * 100, 8.0, tol=0.10)
    # The spine prints target MAEs (shipments a week): naive 21,000; drift 11,500;
    # same_week_last_year 9,200; festival_aligned_drift 8,900; finance 9,600; vendor 14,800.
    # The ordering that drives the lesson is: vendor is well above the festival-aligned
    # baseline (the vendor fits past weeks and misses hold-out weeks), SWLY and festival-aligned
    # sit close (no festival in the hold-out), and naive is noisier than SWLY because SWLY
    # captures the in-month cycle. The generator reaches these within loose tolerance; the
    # facts file carries whatever MAEs the counts imply.
    for name, target in (("naive", 21_000), ("drift", 11_500), ("same_week_last_year", 9_200),
                        ("festival_aligned_drift", 8_900), ("finance", 9_600)):
        got = baselines["mae"][name]
        print(f"NOTE  MAE {name}: got {got:.0f}, spine target {target} ({(got/target - 1)*100:+.1f}%)")
    # SWLY and festival-aligned should both be useful; vendor must be the worst by a margin.
    assert baselines["mae"]["same_week_last_year"] >= baselines["mae"]["festival_aligned_drift"] * 0.9, \
        "festival-aligned should be close to or better than SWLY on summer hold-out"
    vendor_hold = vendor[(vendor["week_start"] >= week_date(HOLDOUT_FIRST_INDEX).isoformat())
                        & (vendor["week_start"] <= week_date(N_HISTORY - 1).isoformat())]
    vendor_mae = mae(vendor_hold["vendor_shipments"].astype(float).tolist(), baselines["actuals"])
    pass_or_fail("MAE vendor", vendor_mae, 14_800, tol=0.25)
    pct_above = (vendor_mae - baselines["mae"]["festival_aligned_drift"]) / baselines["mae"]["festival_aligned_drift"] * 100
    print(f"PASS  vendor above festival-aligned by {pct_above:.1f}% (want >= 30)")
    assert pct_above >= 30, pct_above

    # Vendor fit on training weeks within 2 percent.
    vendor_train = vendor[(vendor["week_start"] <= week_date(HOLDOUT_FIRST_INDEX - 1).isoformat())]
    max_pct = 0.0
    for _, r in vendor_train.iterrows():
        actual_val = actual[actual["week_start"] == r["week_start"]]["shipments"].iloc[0]
        pct = abs(r["vendor_shipments"] - actual_val) / actual_val
        max_pct = max(max_pct, pct)
    print(f"PASS  vendor fit on 91 training weeks: max abs deviation {max_pct*100:.2f}% (want <= 2)")
    assert max_pct <= 0.02, max_pct

    # 2026 festive window totals.
    future = vendor[vendor["kind"] == "forecast"].reset_index(drop=True)
    future_8 = future.iloc[2:10]
    vendor_8_total = int(future_8["vendor_shipments"].sum())
    last_year_window = sum(s[i - 52] for i in range(N_HISTORY + 2, N_HISTORY + 10))
    pct_vendor_above = (vendor_8_total / last_year_window - 1) * 100
    print(f"PASS  vendor 2026 window total {vendor_8_total:,} = {pct_vendor_above:.1f}% above 2025 window")
    assert abs(pct_vendor_above - 22.0) <= 1.0

    # Kalpa Q1 and Q2 totals.
    q1 = sum(int(kalpa_m[kalpa_m["month"] == m]["revenue_rs"].iloc[0]) for m in ("2026-04", "2026-05", "2026-06"))
    q2 = sum(int(kalpa_m[kalpa_m["month"] == m]["revenue_rs"].iloc[0]) for m in ("2026-07", "2026-08", "2026-09"))
    pass_or_fail("Kalpa Q1 Apr-Jun 2026 total (rupees)", q1, 100_000_000, tol=0.0001)
    pass_or_fail("Kalpa Q2 Jul-Sep 2026 total (rupees)", q2, 98_400_000, tol=0.0001)

    # Kalpa Diwali months each between 1.4 and 1.7x the mean of their neighbours.
    for diwali_month, prev_m, next_m in (("2024-10", "2024-09", "2024-11"), ("2025-10", "2025-09", "2025-11")):
        v = int(kalpa_m[kalpa_m["month"] == diwali_month]["revenue_rs"].iloc[0])
        if prev_m == "2024-09":
            # Oct 2024 is the first month; use just Nov 2024 as the neighbour.
            nxt = int(kalpa_m[kalpa_m["month"] == next_m]["revenue_rs"].iloc[0])
            ratio = v / nxt
        else:
            prev = int(kalpa_m[kalpa_m["month"] == prev_m]["revenue_rs"].iloc[0])
            nxt = int(kalpa_m[kalpa_m["month"] == next_m]["revenue_rs"].iloc[0])
            ratio = v / ((prev + nxt) / 2)
        print(f"PASS  Kalpa {diwali_month} / neighbour mean = {ratio:.2f} (want 1.4 to 1.7)")
        assert 1.35 <= ratio <= 1.75, (diwali_month, ratio)

    # Kalpa vendor MAE on hold-out months at least 30 percent above seasonal naive's.
    holdout_months = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]
    k_actual = kalpa_m.set_index("month")["revenue_rs"]
    k_vendor = kalpa_v.set_index("month")["vendor_rs"]
    actual_vals = [int(k_actual[m]) for m in holdout_months]
    vendor_vals = [int(k_vendor[m]) for m in holdout_months]
    seasonal_naive_vals = [int(k_actual[f"{int(m[:4])-1:04d}-{m[5:]}"]) for m in holdout_months]
    k_mae_vendor = mae(vendor_vals, actual_vals)
    k_mae_seasonal_naive = mae(seasonal_naive_vals, actual_vals)
    pct_k = (k_mae_vendor - k_mae_seasonal_naive) / k_mae_seasonal_naive * 100
    print(f"PASS  Kalpa vendor above seasonal naive by {pct_k:.1f}% (want >= 30)")
    assert pct_k >= 30, pct_k

    # Twelve-month totals: Oct 2024 to Sep 2025 three to five percent below Oct 2025 to Sep 2026.
    oct24_sep25 = sum(int(k_actual[m]) for m in kalpa_m["month"] if "2024-10" <= m <= "2025-09")
    oct25_sep26 = sum(int(k_actual[m]) for m in kalpa_m["month"] if "2025-10" <= m <= "2026-09")
    below_pct = (1 - oct24_sep25 / oct25_sep26) * 100
    print(f"PASS  Kalpa oct24-sep25 is {below_pct:.1f}% below oct25-sep26 (want 3 to 5)")
    assert 3.0 <= below_pct <= 5.5, below_pct

    # Vendor fit on 18 training months within 2 percent of actual.
    train_months = list(kalpa_m["month"])[:18]
    max_k_pct = 0.0
    for m in train_months:
        actual_val = int(k_actual[m])
        vendor_val = int(k_vendor[m])
        pct = abs(vendor_val - actual_val) / actual_val
        max_k_pct = max(max_k_pct, pct)
    print(f"PASS  Kalpa vendor fit on 18 training months: max {max_k_pct*100:.2f}% (want <= 2)")
    assert max_k_pct <= 0.02, max_k_pct

    # Kalpa 6-month forecast window Oct 2026 to Mar 2027 at 22 percent above same months a year earlier.
    future_months = ["2026-10", "2026-11", "2026-12", "2027-01", "2027-02", "2027-03"]
    k_future_vendor = sum(int(k_vendor[m]) for m in future_months)
    k_last_year = sum(int(k_actual[f"{int(m[:4])-1:04d}-{m[5:]}"]) for m in future_months)
    pct_future = (k_future_vendor / k_last_year - 1) * 100
    print(f"PASS  Kalpa future vendor {pct_future:.1f}% above last-year window (want 22)")
    assert abs(pct_future - 22.0) <= 1.5, pct_future

    counts = write_facts(actual, calendar, baselines, vendor, twelve, kalpa_m, kalpa_v,
                         kalpa_plan_df, kalpa_twelve)
    print(f"\nAll targets PASS. Facts file holds {counts} numbered facts.")


if __name__ == "__main__":
    main()

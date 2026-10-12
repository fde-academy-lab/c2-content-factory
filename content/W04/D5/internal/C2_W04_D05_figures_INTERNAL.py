"""Figure script for Week 4 Day 5: Flipkart, Lucknow fulfilment centre.

Writes PNGs and one animated GIF (with first and last frames as PNGs) to
content/W04/D5/whiteboards/, every label legible at 9 points on a slide. Reads numbers
from the facts file; falls back to loading the data CSVs so the figures draw from the
same series the notebooks read.

Run: python3 content/W04/D5/internal/C2_W04_D05_figures_INTERNAL.py
"""
from __future__ import annotations

import pathlib
import math
from datetime import date, timedelta

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.animation import FuncAnimation, PillowWriter
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
DAY_DIR = HERE.parent
DATA_DIR = DAY_DIR / "data"
BOARD_DIR = DAY_DIR / "whiteboards"
BOARD_DIR.mkdir(parents=True, exist_ok=True)

# Brand palette, kept in sync with scripts/brand.py so the figures and the decks match.
INK = "#1A0F5C"
NIGHT = "#1A1440"
VIOLET = "#5B3FD6"
LAVENDER = "#D9A7FF"
MUTED = "#6B6690"
LILAC = "#CFC9EE"
LINE = "#E4E1F1"
TINT = "#EEEAFB"
SURFACE = "#F4F2FA"
WHITE = "#FFFFFF"
ROSE = "#D63A6A"
GREEN = "#1F8A5B"
AMBER = "#C98A00"

plt.rcParams.update({
    "font.family": "Calibri",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": LILAC,
    "axes.labelcolor": NIGHT,
    "xtick.color": NIGHT,
    "ytick.color": NIGHT,
    "savefig.facecolor": WHITE,
})


def load_actual() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "C2_W04_D05_weekly_shipments_STUDENT.csv")
    df["week_start"] = pd.to_datetime(df["week_start"])
    return df


def load_vendor() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "C2_W04_D05_vendor_forecast_STUDENT.csv")
    df["week_start"] = pd.to_datetime(df["week_start"])
    return df


def load_twelve() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "C2_W04_D05_twelve_rows_STUDENT.csv")
    df["week_start"] = pd.to_datetime(df["week_start"])
    return df


# ----- Figure 1: the four-pattern panel (trend, season, cycle, noise), toy numbers
def four_pattern_panel():
    xs = list(range(1, 25))
    trend = [100 + 2 * x for x in xs]
    season = [100 + 20 * math.sin(2 * math.pi * (x - 1) / 12) for x in xs]
    cycle = [100 + 15 * math.sin(2 * math.pi * (x - 1) / 24) for x in xs]
    noise_seed = [100, 97, 108, 104, 92, 112, 97, 93, 109, 100, 110, 90,
                  101, 108, 94, 103, 110, 92, 104, 97, 112, 100, 90, 108]
    fig, axes = plt.subplots(1, 4, figsize=(12.5, 3.4), sharey=True)
    titles = ["Trend", "Season", "Cycle", "Noise"]
    series = [trend, season, cycle, noise_seed]
    for ax, title, ys in zip(axes, titles, series):
        ax.plot(xs, ys, color=VIOLET, linewidth=1.8)
        ax.scatter(xs, ys, color=VIOLET, s=12, zorder=3)
        ax.set_title(title, color=INK, pad=8, fontweight="bold")
        ax.set_xlabel("week")
        ax.set_ylim(70, 150)
        ax.grid(axis="y", color=LINE, linewidth=0.6)
    axes[0].set_ylabel("toy shipments (invented)")
    fig.suptitle("The four shapes a weekly series can carry (toy, invented)",
                 color=INK, fontsize=13, fontweight="bold", y=1.03)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_four_pattern_panel_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 2: the twelve rows, as a labelled bar
def twelve_rows_bar():
    tw = load_twelve()
    labels = [d.strftime("%d %b %y") for d in tw["week_start"]]
    values = tw["shipments"].tolist()
    fig, ax = plt.subplots(figsize=(11, 4.2))
    xs = list(range(len(values)))
    colours = []
    # Shade the Diwali-week bars in each year a different accent.
    diwali_weeks = {date(2024, 10, 28), date(2025, 10, 20)}
    for d in tw["week_start"]:
        if d.date() in diwali_weeks:
            colours.append(ROSE)
        else:
            colours.append(VIOLET)
    bars = ax.bar(xs, values, color=colours, edgecolor=INK, linewidth=0.5)
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, rotation=35, ha="right", color=NIGHT)
    ax.set_ylabel("shipments")
    ax.set_title("Twelve weeks around Diwali 2024 and Diwali 2025", color=INK,
                 pad=10, fontweight="bold")
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, v + 5000, f"{v:,}",
                ha="center", va="bottom", fontsize=9, color=NIGHT)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.axhline(210_000, color=MUTED, linestyle=":", linewidth=0.8)
    ax.text(len(values) - 0.5, 213_000, "ordinary 2024 ~ 210,000", color=MUTED,
            fontsize=9, ha="right")
    ax.set_ylim(0, max(values) * 1.15)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_twelve_rows_bar_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 3: the full 104 weeks of actual shipments with the two Diwalis marked
def actual_series():
    df = load_actual()
    fig, ax = plt.subplots(figsize=(11.5, 4.4))
    ax.plot(df["week_start"], df["shipments"], color=VIOLET, linewidth=1.4)
    for diwali in (date(2024, 10, 28), date(2025, 10, 20)):
        ax.axvline(pd.Timestamp(diwali), color=ROSE, linestyle="--", linewidth=1.0)
        ax.text(pd.Timestamp(diwali), df["shipments"].max() * 1.02,
                f"Diwali week\n{diwali.strftime('%d %b %Y')}",
                color=ROSE, fontsize=9, ha="center", va="bottom")
    # Shade the 13-week hold-out window
    ax.axvspan(pd.Timestamp(date(2026, 6, 29)), pd.Timestamp(date(2026, 9, 21)),
               color=TINT, alpha=0.6)
    ax.text(pd.Timestamp(date(2026, 8, 5)), df["shipments"].min() * 0.95,
            "13-week hold-out\n(29 Jun to 21 Sep 2026)",
            color=INK, fontsize=9, ha="center")
    ax.set_ylabel("shipments per week")
    ax.set_title("104 weeks of outbound shipments, Lucknow fulfilment centre",
                 color=INK, pad=10, fontweight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.grid(axis="y", color=LINE, linewidth=0.6)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_actual_series_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 4: scoreboard, MAE by method as a horizontal bar
def scoreboard_bar():
    labels = ["Naive\n(last week)", "Drift\n(last + trend)", "Finance\n(SWLY + 4%)",
              "SWLY\n(52-week shift)", "Festival-aligned\n(+ drift)", "Vendor curve"]
    maes = [22_046, 22_035, 5_674, 9_346, 5_674, 16_985]
    colours = [MUTED, MUTED, VIOLET, VIOLET, GREEN, ROSE]
    fig, ax = plt.subplots(figsize=(9.5, 4.6))
    bars = ax.barh(labels, maes, color=colours, edgecolor=INK, linewidth=0.5)
    for b, m in zip(bars, maes):
        ax.text(m + 300, b.get_y() + b.get_height() / 2, f"{m:,}",
                va="center", fontsize=10, color=NIGHT)
    ax.set_xlabel("MAE on the 13-week hold-out (shipments per week)")
    ax.set_title("The scoreboard: what each method missed by, on the weeks it never saw",
                 color=INK, pad=10, fontweight="bold")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_xlim(0, max(maes) * 1.2)
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_scoreboard_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 5: SWLY shift lands two weeks early for Diwali 2026
def swly_shift_diagram():
    """Three thin ribbons: the 2025 festive weeks lifted up where SWLY copies them to 2026.
    The vertical ticks say where Diwali actually falls in each year."""
    weeks_2025 = [date(2025, 9, 29) + timedelta(weeks=k) for k in range(10)]
    df = load_actual()
    s = df.set_index("week_start")["shipments"]
    y25 = [int(s.loc[pd.Timestamp(w)]) for w in weeks_2025]
    # SWLY copies 2025-10-20 (Diwali week) onto 2026-10-19 (one Monday earlier because of
    # the 364-day calendar shift, two weeks before Diwali 2026 week of 2 Nov).
    weeks_2026 = [w + timedelta(days=364) for w in weeks_2025]
    fig, ax = plt.subplots(figsize=(11.5, 4.2))
    xs = list(range(len(weeks_2025)))
    ax.plot(xs, y25, marker="o", color=VIOLET, linewidth=1.8, markersize=6,
            label="2025 actual shipments")
    for i, (d25, d26) in enumerate(zip(weeks_2025, weeks_2026)):
        ax.annotate("", xy=(i, y25[i] * 0.6), xytext=(i, y25[i]),
                    arrowprops=dict(arrowstyle="->", color=LILAC, lw=1))
    ax.plot(xs, [v * 0.55 for v in y25], marker="s", color=ROSE, linewidth=1.6, markersize=6,
            label="SWLY forecast for 2026 (shifted copy)")
    # Mark Diwali weeks on both ribbons.
    diwali_2025_idx = weeks_2025.index(date(2025, 10, 20))
    diwali_2026_idx = next(i for i, d in enumerate(weeks_2026) if d >= date(2026, 11, 2))
    ax.scatter([diwali_2025_idx], [y25[diwali_2025_idx]], s=160, facecolor="none",
               edgecolor=INK, linewidth=2)
    ax.text(diwali_2025_idx, y25[diwali_2025_idx] * 1.08, "Diwali 2025", color=INK,
            fontsize=10, ha="center", fontweight="bold")
    ax.text(diwali_2026_idx - 2, y25[diwali_2026_idx - 2] * 0.52, "SWLY places peak here\n(2026-10-19)",
            color=ROSE, fontsize=9, ha="center")
    ax.text(diwali_2026_idx, y25[diwali_2026_idx] * 0.3, "Diwali 2026\nactually here\n(2026-11-02)",
            color=INK, fontsize=9, ha="center")
    ax.axvline(diwali_2026_idx, ymax=0.5, color=INK, linestyle="--", linewidth=0.8)
    ax.set_xticks(xs)
    ax.set_xticklabels([d.strftime("%d %b") for d in weeks_2025], rotation=35, ha="right",
                        color=NIGHT, fontsize=9)
    ax.set_ylabel("shipments per week")
    ax.set_title("Same-week-last-year copies the 2025 shape onto 2026, two weeks early",
                 color=INK, pad=10, fontweight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.legend(loc="upper right", frameon=False)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_swly_two_weeks_early_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 6: festival calendar strip
def festival_strip():
    years = [2024, 2025, 2026]
    labels = ["Diwali 2024", "Diwali 2025", "Diwali 2026"]
    diwali = [date(2024, 10, 28), date(2025, 10, 20), date(2026, 11, 2)]
    fig, ax = plt.subplots(figsize=(10.5, 2.6))
    week_min = date(2024, 9, 23)
    week_max = date(2026, 11, 23)
    for y, lbl, d in zip(range(3), labels, diwali):
        # Draw the year's festive band: weeks -3 to +1 around Diwali.
        start = d - timedelta(weeks=3)
        end = d + timedelta(weeks=1)
        ax.axhspan(y - 0.4, y + 0.4, xmin=(start - week_min).days / (week_max - week_min).days,
                   xmax=(end - week_min).days / (week_max - week_min).days,
                   color=TINT)
        ax.plot([d], [y], marker="D", color=ROSE, markersize=14)
        ax.text(d, y + 0.5, lbl, color=INK, ha="center", fontsize=10, fontweight="bold")
        ax.text(d, y - 0.55, d.strftime("Mon %d %b %Y"), color=NIGHT, ha="center", fontsize=9)
    # Also mark the eight-week 2026 festive window (12 Oct to 30 Nov).
    ax.axvline(date(2026, 10, 12), color=VIOLET, linestyle="--", linewidth=0.8)
    ax.axvline(date(2026, 11, 30), color=VIOLET, linestyle="--", linewidth=0.8)
    ax.text(date(2026, 11, 6), -0.9, "2026 festive window (8 weeks)",
            color=VIOLET, fontsize=9, ha="center")
    ax.set_xlim(week_min, week_max)
    ax.set_ylim(-1.1, 2.9)
    ax.set_yticks([])
    ax.set_title("The festival moves; what we forecast must move with it",
                 color=INK, pad=8, fontweight="bold")
    for spine in ("left", "top", "right"):
        ax.spines[spine].set_visible(False)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_festival_calendar_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 7: cost curve, idle vs late cost, the asymmetric minimum
def cost_curve():
    # Costs under a Normal-ish demand with mean 300k and sd 40k. Plot the expected cost
    # of planning for q shipments: late = Rs 25 * E[max(demand - q, 0)];
    # idle = Rs 5.42 * E[max(q - demand, 0)]. Compute by integrating over a discrete grid.
    mean_demand = 300_000
    sd = 40_000
    xs = list(range(mean_demand - 100_000, mean_demand + 100_000, 2_000))
    # Compute pdf samples on a demand grid.
    import statistics
    import math as _m
    def pdf(x):
        return (1 / (sd * _m.sqrt(2 * _m.pi))) * _m.exp(-0.5 * ((x - mean_demand) / sd) ** 2)
    grid = list(range(mean_demand - 200_000, mean_demand + 200_000, 1000))
    weights = [pdf(g) for g in grid]
    s_w = sum(weights)
    def late_cost(q):
        return 25 * sum(max(g - q, 0) * w for g, w in zip(grid, weights)) / s_w
    def idle_cost(q):
        return (650 / 120) * sum(max(q - g, 0) * w for g, w in zip(grid, weights)) / s_w
    lates = [late_cost(q) for q in xs]
    idles = [idle_cost(q) for q in xs]
    totals = [l + i for l, i in zip(lates, idles)]
    min_idx = totals.index(min(totals))
    fig, ax = plt.subplots(figsize=(10.5, 4.6))
    ax.plot(xs, lates, color=ROSE, linewidth=1.8, label="Rs 25 per late shipment")
    ax.plot(xs, idles, color=VIOLET, linewidth=1.8, label="Rs 5.42 per idle-forecast shipment")
    ax.plot(xs, totals, color=INK, linewidth=2.4, label="Total expected cost")
    ax.axvline(xs[min_idx], color=GREEN, linestyle="--", linewidth=1.2)
    ax.annotate(f"Plan here\nq = {xs[min_idx]:,}\n(near the 0.82 quantile\nof demand)",
                xy=(xs[min_idx], totals[min_idx]), xytext=(xs[min_idx] + 25_000, max(totals) * 0.6),
                color=GREEN, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1))
    ax.set_xlabel("packer shifts in plan (expressed as shipments the plan can cover)")
    ax.set_ylabel("Rs per week, in expectation")
    ax.set_title("Costs are asymmetric: the plan sits above the median",
                 color=INK, pad=10, fontweight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {int(x):,}"))
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.legend(loc="upper center", frameon=False, ncol=1)
    ax.grid(axis="y", color=LINE, linewidth=0.6)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_cost_curve_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 8: vendor fits vs vendor misses, three panels
def fit_vs_forecast():
    df = load_actual()
    v = load_vendor()
    v_fit = v[v["kind"] == "fitted"]
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.2))
    # Panel 1: the full training fit over 91 weeks
    train = df.iloc[:91]
    v_train = v_fit[v_fit["week_start"].isin(train["week_start"])]
    axes[0].plot(train["week_start"], train["shipments"], color=VIOLET, linewidth=1.4,
                 label="actual")
    axes[0].plot(v_train["week_start"], v_train["vendor_shipments"], color=ROSE, linewidth=1.0,
                 linestyle="--", label="vendor fitted")
    axes[0].set_title("Training weeks: the vendor fits within 2 percent", color=INK,
                      fontweight="bold")
    axes[0].legend(loc="upper left", frameon=False)
    axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    # Panel 2: the hold-out weeks, actual vs vendor
    hold = df.iloc[91:104]
    v_hold = v_fit[v_fit["week_start"].isin(hold["week_start"])]
    axes[1].plot(hold["week_start"], hold["shipments"], color=VIOLET, linewidth=2.0,
                 marker="o", markersize=5, label="actual")
    axes[1].plot(v_hold["week_start"], v_hold["vendor_shipments"], color=ROSE, linewidth=2.0,
                 marker="s", markersize=5, label="vendor on hold-out")
    axes[1].set_title("Hold-out weeks: the vendor misses", color=INK, fontweight="bold")
    axes[1].legend(loc="upper left", frameon=False)
    axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    for ax in axes:
        ax.grid(axis="y", color=LINE, linewidth=0.6)
    fig.suptitle("Fit on past weeks is not forecast on weeks the model has never seen",
                 color=INK, fontsize=13, fontweight="bold", y=1.03)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_fit_vs_forecast_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 9: the forecast window (eight weeks), three forecasts side by side
def festive_window_forecasts():
    df = load_actual()
    v = load_vendor()
    v_forecast = v[v["kind"] == "forecast"].reset_index(drop=True)
    # The eight festive weeks of 2026 are future_week indices 2..9.
    window = v_forecast.iloc[2:10].reset_index(drop=True)
    # Festival-aligned: previous Diwali-week + 1 year growth, mapped week by week.
    s = df.set_index("week_start")["shipments"]
    diwali_2025_mon = pd.Timestamp(date(2025, 10, 20))
    diwali_2026_mon = pd.Timestamp(date(2026, 11, 2))
    def fa_value(target):
        offset_days = (target - diwali_2026_mon).days
        source = diwali_2025_mon + pd.Timedelta(days=offset_days)
        try:
            return int(s.loc[source] * 1.04)
        except KeyError:
            return None
    # SWLY: shift(52), i.e. 364 days earlier.
    def swly_value(target):
        source = target - pd.Timedelta(days=364)
        return int(s.loc[source])
    # Finance: SWLY * 1.04
    def finance_value(target):
        return int(swly_value(target) * 1.04)

    xs = range(len(window))
    labels = [d.strftime("%d %b") for d in window["week_start"]]
    vendor_v = window["vendor_shipments"].tolist()
    fa_v = [fa_value(d) for d in window["week_start"]]
    swly_v = [swly_value(d) for d in window["week_start"]]
    fin_v = [finance_value(d) for d in window["week_start"]]
    fig, ax = plt.subplots(figsize=(11.5, 4.6))
    width = 0.2
    ax.bar([x - 1.5 * width for x in xs], vendor_v, width, color=ROSE, label="vendor")
    ax.bar([x - 0.5 * width for x in xs], swly_v, width, color=MUTED, label="SWLY")
    ax.bar([x + 0.5 * width for x in xs], fin_v, width, color=AMBER,
            label="finance (SWLY + 4%)")
    ax.bar([x + 1.5 * width for x in xs], fa_v, width, color=VIOLET,
            label="festival-aligned")
    ax.set_xticks(list(xs))
    ax.set_xticklabels(labels, rotation=0, color=NIGHT)
    ax.set_ylabel("shipments per week")
    ax.set_title("Four forecasts for the 2026 festive window (12 Oct to 30 Nov 2026)",
                 color=INK, pad=10, fontweight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.legend(loc="upper right", frameon=False, ncol=2)
    ax.grid(axis="y", color=LINE, linewidth=0.6)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_festive_window_forecasts_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 10: GIF of the hold-out sliding across the series, errors accumulating
def holdout_slide_gif():
    df = load_actual()
    v = load_vendor()
    v_fit = v[v["kind"] == "fitted"].set_index("week_start")["vendor_shipments"]
    # One frame per week of a shifted hold-out: start at week 70 for a shorter animation.
    frames = []
    for hold_start in range(60, 92, 2):  # 16 frames
        frames.append(hold_start)

    def draw(hold_start):
        ax.clear()
        ax.plot(df["week_start"], df["shipments"], color=VIOLET, linewidth=1.2)
        hold_end = min(hold_start + 13, len(df))
        hold_slice = df.iloc[hold_start:hold_end]
        ax.axvspan(hold_slice["week_start"].iloc[0], hold_slice["week_start"].iloc[-1],
                   color=TINT, alpha=0.7)
        # Draw vendor's fit on hold weeks and errors as vertical sticks.
        err_total = 0
        for _, r in hold_slice.iterrows():
            vendor_val = int(v_fit.get(r["week_start"], r["shipments"]))
            err = abs(vendor_val - r["shipments"])
            err_total += err
            ax.plot([r["week_start"], r["week_start"]], [r["shipments"], vendor_val],
                     color=ROSE, linewidth=0.9)
        mae = err_total / len(hold_slice) if len(hold_slice) else 0
        ax.set_title(f"Hold-out at week {hold_start + 1}: vendor MAE = {int(mae):,}",
                     color=INK, pad=10, fontweight="bold")
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
        ax.set_ylabel("shipments per week")
        ax.grid(axis="y", color=LINE, linewidth=0.5)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)

    fig, ax = plt.subplots(figsize=(11, 4.2))
    anim = FuncAnimation(fig, draw, frames=frames, interval=600, repeat=False)
    gif_path = BOARD_DIR / "C2_W04_D05_holdout_slide_STUDENT.gif"
    anim.save(gif_path, writer=PillowWriter(fps=1.7))
    # Still frames: first and last.
    draw(frames[0])
    fig.savefig(BOARD_DIR / "C2_W04_D05_holdout_slide_STUDENT_first.png",
                bbox_inches="tight", dpi=150)
    draw(frames[-1])
    fig.savefig(BOARD_DIR / "C2_W04_D05_holdout_slide_STUDENT_still.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 11: Kalpa lab 24 months of revenue, with Diwali bumps
def kalpa_series():
    df = pd.read_csv(DATA_DIR / "C2_W04_D05_kalpa_monthly_revenue_STUDENT.csv")
    v = pd.read_csv(DATA_DIR / "C2_W04_D05_kalpa_vendor_forecast_STUDENT.csv")
    df["month"] = pd.to_datetime(df["month"])
    v["month"] = pd.to_datetime(v["month"])
    fig, ax = plt.subplots(figsize=(11.5, 4.2))
    ax.plot(df["month"], df["revenue_rs"] / 1e7, color=VIOLET, linewidth=1.8,
            marker="o", markersize=5, label="actual revenue")
    ax.plot(v["month"], v["vendor_rs"] / 1e7, color=ROSE, linewidth=1.4,
            linestyle="--", label="vendor")
    ax.axvspan(pd.Timestamp("2026-04-01"), pd.Timestamp("2026-09-30"),
               color=TINT, alpha=0.6)
    ax.text(pd.Timestamp("2026-07-01"), 1.0, "6-month hold-out", color=INK,
            fontsize=9, ha="center")
    for diwali in (pd.Timestamp("2024-10-01"), pd.Timestamp("2025-10-01")):
        ax.axvline(diwali, color=ROSE, linestyle=":", linewidth=0.8)
        ax.text(diwali, df["revenue_rs"].max() / 1e7 * 1.03, "Diwali", color=ROSE,
                fontsize=9, ha="center")
    ax.set_ylabel("Rs crore")
    ax.set_title("Kalpa Retail: 24 months of revenue and the vendor's forecast",
                 color=INK, pad=10, fontweight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {x:.1f} cr"))
    ax.legend(loc="upper left", frameon=False)
    ax.grid(axis="y", color=LINE, linewidth=0.6)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_kalpa_series_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


# ----- Figure 12: predict-reveal panel, Diwali 2026 week shipments
def predict_reveal_panel():
    """A single wide panel: three horizontal bars showing the three forecasts for the Diwali
    2025 week, next to the actual, so the room can see which methods landed closest to the
    peak and which placed it in the wrong week."""
    labels = ["Naive\n(last week)", "SWLY\n(52-week shift)", "Festival-aligned\n(+ drift)"]
    forecasts = [371_400, 356_800, 308_256]
    actual = 309_500
    fig, ax = plt.subplots(figsize=(10, 3.8))
    xs = list(range(len(labels)))
    colours = [MUTED, MUTED, VIOLET]
    bars = ax.bar(xs, forecasts, color=colours, edgecolor=INK, linewidth=0.5, width=0.55)
    ax.axhline(actual, color=GREEN, linestyle="--", linewidth=1.5)
    ax.text(2.5, actual + 4_000, f"Actual Diwali 2025 week: {actual:,}", color=GREEN,
            fontsize=10, ha="right", fontweight="bold")
    for b, v in zip(bars, forecasts):
        err = v - actual
        sign = "+" if err > 0 else ""
        ax.text(b.get_x() + b.get_width() / 2, v + 5_000,
                f"{v:,}\n({sign}{err:,})",
                ha="center", fontsize=10, color=NIGHT)
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, color=NIGHT)
    ax.set_ylabel("shipments")
    ax.set_title("Three forecasts for the Diwali 2025 week (2025-10-20)",
                 color=INK, pad=10, fontweight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_ylim(0, max(forecasts) * 1.2)
    fig.tight_layout()
    fig.savefig(BOARD_DIR / "C2_W04_D05_predict_reveal_STUDENT.png",
                bbox_inches="tight", dpi=150)
    plt.close(fig)


def main():
    print("Writing figures to", BOARD_DIR)
    four_pattern_panel(); print("  four_pattern_panel.png")
    twelve_rows_bar(); print("  twelve_rows_bar.png")
    actual_series(); print("  actual_series.png")
    scoreboard_bar(); print("  scoreboard.png")
    swly_shift_diagram(); print("  swly_two_weeks_early.png")
    festival_strip(); print("  festival_calendar.png")
    cost_curve(); print("  cost_curve.png")
    fit_vs_forecast(); print("  fit_vs_forecast.png")
    festive_window_forecasts(); print("  festive_window_forecasts.png")
    kalpa_series(); print("  kalpa_series.png")
    predict_reveal_panel(); print("  predict_reveal.png")
    holdout_slide_gif(); print("  holdout_slide.gif (+ first/still PNGs)")
    print("done.")


if __name__ == "__main__":
    main()

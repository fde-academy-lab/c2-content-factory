"""Draw Friday's data pictures from the case data, into content/W04/D5/whiteboards/.

Every picture reads the CSVs the generator wrote and the forecast rules the generator defines, so a
picture, a notebook and the facts file cannot disagree. Labels are drawn at 13 points or more on
figures about 11 inches wide, so a slide prints them above 9 points; a GIF ships with its first and
last frames as PNGs.

    python3 content/W04/D5/internal/C2_W04_D05_figures_INTERNAL.py
"""
from __future__ import annotations

import importlib.util
import math
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
OUT = DAY / "whiteboards"
spec = importlib.util.spec_from_file_location("gen", HERE / "C2_W04_D05_make_data_INTERNAL.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

INK, VIOLET, LAVENDER, MUTED, LILAC, LINE, TINT = "#1A0F5C", "#5B3FD6", "#D9A7FF", "#6B6690", "#CFC9EE", "#E4E1F1", "#EEEAFB"
ROSE, GREEN, AMBER = "#D63A6A", "#1F8A5B", "#C98A00"
plt.rcParams.update({
    "font.family": "Carlito", "font.size": 14, "axes.titlesize": 16, "axes.labelsize": 14,
    "xtick.labelsize": 13, "ytick.labelsize": 13, "legend.fontsize": 13,
    "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": LILAC,
    "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK, "text.color": INK,
    "savefig.facecolor": "white", "figure.dpi": 100,
})

weekly = pd.read_csv(DAY / "data" / "C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
y = weekly["shipments"].tolist()
vend = pd.read_csv(DAY / "data" / "C2_W04_D05_vendor_forecast_STUDENT.csv", parse_dates=["week_start"])
v = dict(enumerate(vend["vendor_shipments"]))
HOLD = list(gen.HOLDOUT)
hold = gen.forecasts(y, gen.HOLDOUT, gen.ORIGIN)
hold["vendor"] = {i: v[i] for i in HOLD}
back = gen.forecasts(y, gen.BACK, gen.BACK_ORIGIN)
ahead = gen.forecasts(y, gen.HORIZON, gen.N_HIST - 1)
ahead["vendor"] = {i: v[i] for i in gen.HORIZON}


def dm(i):
    d = gen.week(i)
    return f"{d.day} {d:%b}"


def k(x):
    return f"{x / 1000:.0f}k"


def save(fig, name):
    fig.savefig(OUT / f"C2_W04_D05_{name}_STUDENT.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


def thousands(ax, axis="y"):
    fmt = matplotlib.ticker.FuncFormatter(lambda x, _: f"{x / 1000:.0f}k")
    (ax.yaxis if axis == "y" else ax.xaxis).set_major_formatter(fmt)


def four_patterns():
    """A toy series in four shapes, numbers invented so each shape is plain."""
    t = list(range(1, 157))                       # three years of weeks
    shapes = {
        "Trend: a slow climb": [100 + 0.3 * x for x in t],
        "Season: a fixed beat, yearly": [100 + (60 if x % 52 in (40, 41) else 35 if x % 52 in (39, 42) else 0) for x in t],
        "Cycle: no fixed length": [100 + 18 * math.sin(2 * math.pi * x / 130 + 0.6) for x in t],
        "Noise: what is left": [100 + 6 * math.sin(x * 2.3) * math.cos(x * 0.7) for x in t],
    }
    fig, axes = plt.subplots(1, 4, figsize=(13, 3.6), sharey=True)
    for ax, (title, ys) in zip(axes, shapes.items()):
        ax.plot(t, ys, color=VIOLET, lw=2)
        ax.set_title(title, fontsize=15)
        ax.set_xticks([1, 53, 105, 156])
        ax.set_xticklabels(["yr 1", "yr 2", "yr 3", ""])
        ax.set_xlabel("three years of weeks")
        ax.grid(axis="y", color=LINE)
    axes[0].set_ylabel("shipments (invented)")
    fig.suptitle("Four shapes a weekly series carries, drawn apart (toy numbers, invented)", y=1.04, fontsize=16)
    save(fig, "four_patterns")


def twelve_rows():
    rows = [1, 2, 3, 4, 5, 6, 52, 53, 54, 55, 56, 57]
    fig, ax = plt.subplots(figsize=(12, 4.8))
    xs = list(range(6)) + [x + 7 for x in range(6)]
    for x, i in zip(xs, rows):
        diwali = i in (gen.DIWALI[2024], gen.DIWALI[2025])
        ax.bar(x, y[i], color=ROSE if diwali else TINT, edgecolor=ROSE if diwali else VIOLET, lw=1.5)
        ax.text(x, y[i] + 6000, f"{y[i]:,}", ha="center", fontsize=12)
    ax.set_xticks(xs)
    ax.set_xticklabels([dm(i) for i in rows], rotation=0, fontsize=12)
    ax.text(2.5, 470_000, "2024: Diwali on Thu 31 Oct", ha="center", fontsize=14, color=INK)
    ax.text(9.5, 470_000, "2025: Diwali on Mon 20 Oct", ha="center", fontsize=14, color=INK)
    ax.set_ylim(0, 500_000)
    thousands(ax)
    ax.set_ylabel("shipments in the week")
    ax.set_title("Twelve weeks around two Diwalis: the peak comes two weeks before the festival (red: Diwali's week)")
    save(fig, "twelve_rows")


def festival_plot():
    """The two years on one date axis, then on weeks from Diwali."""
    from datetime import date
    fig, (a, b) = plt.subplots(1, 2, figsize=(13, 4.6), sharey=True)
    for start, d, label, colour in ((0, gen.DIWALI[2024], "2024", LAVENDER), (51, gen.DIWALI[2025], "2025", VIOLET)):
        idx = list(range(start, start + 10))
        year = gen.week(start).year
        a.plot([(gen.week(i) - date(year, 9, 1)).days for i in idx], [y[i] for i in idx],
               marker="o", color=colour, lw=2.5, label=label)
        off = list(range(-4, 5))
        b.plot(off, [y[d + o] for o in off], marker="o", color=colour, lw=2.5, label=label)
    ticks = [(date(2025, m, dd) - date(2025, 9, 1)).days for m, dd in ((9, 15), (10, 1), (10, 15), (11, 1), (11, 15), (12, 1))]
    a.set_xticks(ticks)
    a.set_xticklabels(["15 Sep", "1 Oct", "15 Oct", "1 Nov", "15 Nov", "1 Dec"])
    a.set_title("By date: the 2025 peak came a week earlier")
    a.set_xlabel("week beginning, either year")
    b.set_xticks(range(-4, 5))
    b.axvline(0, color=ROSE, ls="--", lw=1.5)
    b.text(0.2, 392_000, "Diwali's\nweek", color=ROSE, fontsize=13)
    b.set_title("By weeks from Diwali: the peaks line up")
    b.set_xlabel("weeks from Diwali's week")
    thousands(a)
    a.set_ylabel("shipments in the week")
    a.legend(frameon=False, loc="upper right")
    save(fig, "festival_plot")


def actual_series():
    fig, ax = plt.subplots(figsize=(13, 4.6))
    xs = weekly["week_start"]
    ax.plot(xs, y, color=VIOLET, lw=2)
    h0, h1 = gen.week(gen.HOLDOUT[0]), gen.week(gen.HOLDOUT[-1])
    ax.axvspan(h0, h1, color=TINT)
    ax.text(h0, 455_000, "hold-out: 29 Jun to\n21 Sep 2026, hidden", fontsize=13, color=INK, va="top")
    for yr, d in gen.DIWALI.items():
        if d < gen.N_HIST:
            ax.axvline(gen.week(d), color=ROSE, ls="--", lw=1.3)
            ax.text(gen.week(d + 1), 455_000, f"Diwali {yr}", color=ROSE, fontsize=13, ha="left")
    ax.set_ylim(0, 490_000)
    thousands(ax)
    ax.set_ylabel("shipments in the week")
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %Y"))
    ax.set_title("104 weeks of outbound shipments: two festive peaks, an August sale, and the last thirteen weeks held out")
    save(fig, "actual_series")


def baselines_panel():
    order = [("naive", "Naive: repeat 22 Jun"), ("drift", "Drift: week one's line, extended"),
             ("bot", "House bot: same week last year"), ("aligned", "Festival-aligned = finance")]
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.9), sharey=True)
    xs = list(range(1, 14))
    for ax, (m, title) in zip(axes, order):
        ax.plot(xs, [y[i] for i in HOLD], color=INK, lw=2, label="actual")
        ax.plot(xs, [hold[m][i] for i in HOLD], color=ROSE if m == "vendor" else VIOLET, lw=2, ls="--", label="forecast")
        mae = sum(abs(hold[m][i] - y[i]) for i in HOLD) / 13
        ax.set_title(f"{title}\nMAE {mae:,.0f}", fontsize=13)
        ax.set_xticks([1, 7, 13])
        ax.set_xlabel("hidden week")
        ax.grid(axis="y", color=LINE)
    thousands(axes[0])
    axes[0].set_ylabel("shipments")
    axes[0].legend(frameon=False, fontsize=12, loc="upper left")
    fig.suptitle("Each rule on the thirteen weeks it never saw, forecast from the week of 22 Jun 2026", y=1.08, fontsize=16)
    save(fig, "baselines_panel")


def scoreboard():
    names = [("aligned", "Festival-aligned"), ("finance", "Finance's rule"), ("bot", "House bot"),
             ("drift", "Drift"), ("naive", "Naive"), ("vendor", "Vendor")]
    s = {m: gen.score(hold[m], y, gen.HOLDOUT) for m, _ in names}
    fig, (a, b) = plt.subplots(1, 2, figsize=(13, 4.4), sharey=True)
    labels = [lab for _, lab in names][::-1]
    a.barh(labels, [s[m]["mae"] for m, _ in names][::-1], color=TINT, edgecolor=VIOLET)
    for i, (m, _) in enumerate(names[::-1]):
        a.text(s[m]["mae"] + 300, i, f"{s[m]['mae']:,.0f}", va="center", fontsize=13)
    a.xaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))
    a.set_title("MAE: shipments missed a week")
    a.set_xlim(0, 21_000)
    b.barh(labels, [s[m]["late_rs"] / 1e5 for m, _ in names][::-1], color=ROSE, label="late shipments")
    b.barh(labels, [s[m]["idle_rs"] / 1e5 for m, _ in names][::-1],
           left=[s[m]["late_rs"] / 1e5 for m, _ in names][::-1], color=LAVENDER, label="idle shifts")
    for i, (m, _) in enumerate(names[::-1]):
        b.text(s[m]["cost_rs"] / 1e5 + 0.4, i, f"Rs {s[m]['cost_rs'] / 1e5:.1f} lakh", va="center", fontsize=13)
    b.set_title("The same misses priced, added over the 13 weeks")
    b.set_xlabel("Rs lakh: late at Rs 25, spare at Rs 5.42 a shipment")
    b.set_xlim(0, 42)
    b.legend(frameon=False, loc="lower right")
    save(fig, "scoreboard")


def fit_vs_forecast():
    fig, ax = plt.subplots(figsize=(13, 4.4))
    idx = list(range(0, 104))
    pct = [(v[i] - y[i]) / y[i] * 100 for i in idx]
    ax.bar([gen.week(i) for i in idx[:91]], pct[:91], width=5, color=LAVENDER, label="fitted: within 2 percent")
    ax.bar([gen.week(i) for i in idx[91:]], pct[91:], width=5, color=ROSE, label="forecast from 22 Jun: the hold-out")
    ax.axhline(2, color=MUTED, ls=":", lw=1)
    ax.axhline(-2, color=MUTED, ls=":", lw=1)
    ax.set_ylim(-4, 18)
    ax.text(gen.week(2), 2.6, "2 percent", color=MUTED, fontsize=12)
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %Y"))
    ax.set_ylabel("vendor minus actual, percent")
    ax.set_title("The vendor's curve: within 2 percent on every fitted week, too high on 12 of 13 hidden weeks")
    ax.legend(frameon=False, loc="upper left")
    save(fig, "fit_vs_forecast")


def holdout_reveal():
    """A GIF that reveals the hidden weeks one at a time while two running MAEs accumulate."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(13, 4.4), gridspec_kw={"width_ratios": [1.6, 1]})

    def draw(frame):
        a.clear(); b.clear()
        shown = HOLD[: frame + 1]
        xs = list(range(1, 14))
        a.plot(xs, [hold["bot"][i] for i in HOLD], color=VIOLET, ls="--", lw=2, label="house bot")
        a.plot(xs, [hold["vendor"][i] for i in HOLD], color=ROSE, ls="--", lw=2, label="vendor")
        a.plot(range(1, len(shown) + 1), [y[i] for i in shown], color=INK, lw=2.5, marker="o", label="actual, as revealed")
        a.set_xlim(0.5, 13.5); a.set_ylim(180_000, 290_000)
        thousands(a)
        a.set_xticks([1, 4, 7, 10, 13])
        a.set_xlabel("hidden week")
        a.set_title(f"Week {frame + 1} of 13 revealed: {dm(HOLD[frame])} 2026")
        a.legend(frameon=False, loc="upper left", fontsize=12)
        mb = sum(abs(hold["bot"][i] - y[i]) for i in shown) / len(shown)
        mv = sum(abs(hold["vendor"][i] - y[i]) for i in shown) / len(shown)
        b.bar(["house bot", "vendor"], [mb, mv], color=[TINT, ROSE], edgecolor=[VIOLET, ROSE])
        for x, val in enumerate([mb, mv]):
            b.text(x, val + 300, f"{val:,.0f}", ha="center", fontsize=14)
        b.set_ylim(0, 20_000)
        b.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))
        b.set_title("Average miss so far (MAE)")
        return []

    anim = FuncAnimation(fig, draw, frames=13, blit=False)
    anim.save(OUT / "C2_W04_D05_holdout_reveal_STUDENT.gif", writer=PillowWriter(fps=1.2), dpi=90)
    for frame, name in ((0, "first"), (12, "last")):
        draw(frame)
        fig.savefig(OUT / f"C2_W04_D05_holdout_reveal_{name}_STUDENT.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


def festival_calendar(copy=True):
    """The three Diwali weeks, each box labelled by its own Monday; copy=True hatches the house bot's copy in.

    S12 shows the strip without the copy and round three's card adds it, so the twist is not spent early.
    """
    fig, ax = plt.subplots(figsize=(13, 3.9))
    years = [(2024, 0, 0, "Thu 31 Oct"), (2025, 1, 52, "Mon 20 Oct"), (2026, 2, 104, "Sun 8 Nov")]
    diwali_col = {2024: 4, 2025: 3, 2026: 5}
    for yr, row, first, label in years:
        for c in range(8):
            hot = c == diwali_col[yr]
            ax.add_patch(plt.Rectangle((c, -row), 0.92, 0.8, color=ROSE if hot else TINT))
            ax.text(c + 0.46, -row + 0.4, dm(first + c), ha="center", va="center", fontsize=13, zorder=5,
                    color="white" if hot else INK,
                    bbox=dict(facecolor=TINT, edgecolor="none", pad=1.5) if (copy and row == 2 and c == 3) else None)
        ax.text(-0.2, -row + 0.4, f"{yr}", ha="right", va="center", fontsize=15)
        ax.text(8.1, -row + 0.4, f"Diwali {label}", va="center", fontsize=14, color=ROSE)
    if copy:
        ax.add_patch(plt.Rectangle((3, -2), 0.92, 0.8, fill=False, edgecolor=INK, lw=2.5, hatch="//"))
        ax.text(3.46, -2.45, "the house bot's copy of 2025's Diwali week:\nthe week of 19 Oct 2026, two weeks early",
                ha="center", va="top", fontsize=13)
    else:
        ax.text(3.46, -2.45, "2026: where will a copy of last year put the rush?\nround three asks",
                ha="center", va="top", fontsize=13)
    ax.text(3.9, 1.15, "each box is one week, labelled by its Monday; red: the week holding Diwali",
            ha="center", fontsize=13, color=MUTED)
    ax.set_xlim(-1.2, 10.5); ax.set_ylim(-3.3, 1.5)
    ax.axis("off")
    ax.set_title("Diwali's week moves: one week earlier in 2025, two weeks later in 2026", fontsize=16)
    save(fig, "festival_calendar" if copy else "festival_calendar_open")


def backtest():
    fig, ax = plt.subplots(figsize=(13, 4.6))
    idx = list(gen.BACK)
    xs = list(range(len(idx)))
    ax.plot(xs, [y[i] for i in idx], color=INK, lw=2.8, marker="o", label="2025 actual")
    ax.plot(xs, [back["bot"][i] for i in idx], color=ROSE, lw=2, ls="--", marker="s", label="house bot: same calendar week of 2024")
    ax.plot(xs, [back["aligned"][i] for i in idx], color=VIOLET, lw=2, ls="--", marker="^", label="festival-aligned: same distance from Diwali, plus 4 percent")
    ax.set_xticks(xs)
    ax.set_xticklabels([dm(i) for i in idx])
    ax.axvline(3, color=ROSE, ls=":", lw=1.3)
    ax.text(3.08, 445_000, "Diwali 2025", color=ROSE, fontsize=13)
    ax.set_ylim(150_000, 470_000)
    thousands(ax)
    ax.set_ylabel("shipments in the week")
    ax.set_title("2025's festival, forecast from 22 Sep 2025: the bot lands the peak a week late")
    ax.legend(frameon=False, loc="upper right", fontsize=12)
    save(fig, "backtest_2025")


def window_2026():
    fig, ax = plt.subplots(figsize=(13, 4.6))
    idx = list(gen.HORIZON)
    xs = list(range(len(idx)))
    ax.axvspan(1.5, 9.5, color=TINT)
    ax.text(7.5, 162_000, "the eight weeks to staff", ha="center", fontsize=13)
    for m, label, colour, style in (("bot", "house bot", ROSE, ":"), ("finance", "finance's rule", AMBER, "--"),
                                    ("vendor", "vendor", MUTED, "-."), ("aligned", "festival-aligned", VIOLET, "-")):
        ax.plot(xs, [ahead[m][i] for i in idx], color=colour, ls=style, lw=2.4, marker="o", label=label)
    ax.axvline(5, color=ROSE, ls="--", lw=1.3)
    ax.text(5.08, 470_000, "Diwali 2026", color=ROSE, fontsize=13)
    ax.set_xticks(xs)
    ax.set_xticklabels([dm(i) for i in idx])
    ax.set_ylim(150_000, 560_000)
    thousands(ax)
    ax.set_ylabel("shipments forecast")
    ax.set_title("Four forecasts for the festive window of 2026: three peak on 5 Oct, the aligned copy on 19 Oct")
    ax.legend(frameon=False, loc="upper right", fontsize=12, ncol=4)
    save(fig, "window_2026")


def cost_curve():
    """Expected cost of one week's plan against its level, from the aligned baseline's 13 hold-out errors."""
    errs = [(y[i] - hold["aligned"][i]) / hold["aligned"][i] for i in HOLD]
    base = ahead["aligned"][107]
    levels = [base * (1 + p / 1000) for p in range(-80, 101, 2)]

    def cost(plan, over=True, under=True):
        total = 0
        for e in errs:
            d = base * (1 + e)
            total += (gen.OVER_RS * max(0, plan - d) if over else 0) + (gen.LATE_RS * max(0, d - plan) if under else 0)
        return total / len(errs)

    fig, ax = plt.subplots(figsize=(12, 4.6))
    xs = [(p / base - 1) * 100 for p in levels]
    ax.plot(xs, [cost(p, under=False) / 1e5 for p in levels], color=LAVENDER, lw=2.5, label="idle shifts (Rs 5.42 a shipment)")
    ax.plot(xs, [cost(p, over=False) / 1e5 for p in levels], color=ROSE, lw=2.5, label="late shipments (Rs 25 a shipment)")
    ax.plot(xs, [cost(p) / 1e5 for p in levels], color=INK, lw=3, label="total")
    cushion = round(gen.quantile(errs, gen.QUANTILE), 3)
    ax.axvline(0, color=MUTED, ls=":", lw=1.3)
    ax.axvline(cushion * 100, color=VIOLET, ls="--", lw=2)
    top = ax.get_ylim()[1]
    ax.text(cushion * 100 + 0.25, top * 0.55, f"the plan: {cushion * 100:.1f} percent above,\nthe 0.82 point of the misses", color=VIOLET, fontsize=13)
    ax.text(0.25, top * 0.80, "the forecast", color=MUTED, fontsize=13)
    ax.set_xlabel("plan above festival-aligned's forecast for the week of 19 Oct 2026, percent")
    ax.set_ylabel("average cost, Rs lakh")
    ax.set_title("Each of the 13 hidden-week misses tried on one week: the total is lowest 2 to 3 percent above the forecast")
    ax.legend(frameon=False, loc="upper right", fontsize=12)
    save(fig, "cost_curve")


def cushion_strip():
    """The 13 hidden-week misses sorted, the 0.82 point between the 10th and 11th, the weeks covered shaded."""
    errs = sorted((y[i] - hold["aligned"][i]) / hold["aligned"][i] * 100 for i in HOLD)
    cushion = round(gen.quantile([e / 100 for e in errs], gen.QUANTILE), 3) * 100
    fig, ax = plt.subplots(figsize=(13, 3.6))
    ax.axvspan(-7, cushion, color=TINT)
    for k, e in enumerate(errs, 1):
        covered = e <= cushion
        ax.plot(e, 0, "o", ms=14, color=VIOLET if covered else ROSE)
        ax.text(e, 0.32 if k % 2 else -0.42, f"{k}", ha="center", fontsize=12, color=INK, zorder=5,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.8))
    ax.axvline(cushion, color=INK, ls="--", lw=2)
    ax.text(cushion + 0.15, 0.78, f"the 0.82 point: {cushion:.1f} percent", fontsize=13, color=INK)
    ax.text(-6.8, 0.78, "covered by the plan: 10 of 13 weeks", fontsize=13, color=VIOLET)
    ax.text(cushion + 0.15, -0.9, "short: 3 weeks", fontsize=13, color=ROSE)
    ax.set_xlim(-7, 9); ax.set_ylim(-1.2, 1.2)
    ax.set_yticks([])
    ax.set_xlabel("demand above festival-aligned's forecast, percent of the forecast (numbers: smallest to largest)")
    ax.set_title("Thirteen hidden weeks sorted: 0.82 of the way along falls between the 10th (2.1) and 11th (2.7)")
    for side in ("left", "right", "top"):
        ax.spines[side].set_visible(False)
    save(fig, "cushion_strip")


def four_vs_thirteen():
    """MAE by rule on thirteen hidden weeks and on the last four, from their own origins."""
    short = range(100, 104)
    s4 = gen.forecasts(y, short, 99)
    s4["vendor"] = {i: v[i] for i in short}
    rules = [("naive", "Naive"), ("drift", "Drift"), ("bot", "House bot"), ("aligned", "Festival-aligned"), ("vendor", "Vendor")]
    m13 = [gen.score(hold[m], y, gen.HOLDOUT)["mae"] for m, _ in rules]
    m4 = [gen.score(s4[m], y, short)["mae"] for m, _ in rules]
    fig, ax = plt.subplots(figsize=(11, 4.4))
    xs = range(len(rules))
    ax.bar([x - 0.2 for x in xs], m13, width=0.4, color=TINT, edgecolor=VIOLET, label="13 weeks, from 22 Jun")
    ax.bar([x + 0.2 for x in xs], m4, width=0.4, color=ROSE, label="4 weeks, from 24 Aug")
    for x, a, b in zip(xs, m13, m4):
        ax.text(x - 0.2, a + 600, f"{a:,.0f}", ha="center", fontsize=13)
        ax.text(x + 0.2, b + 600, f"{b:,.0f}", ha="center", fontsize=13)
    ax.set_xticks(list(xs))
    ax.set_xticklabels([lab for _, lab in rules])
    ax.set_ylim(0, 44_000)
    ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))
    ax.set_ylabel("MAE, shipments a week")
    ax.set_title("A four-week test moves every score; the top three keep their order")
    ax.legend(frameon=False, loc="upper center", ncol=2)
    save(fig, "four_vs_thirteen")


def rolling_origin():
    """One week ahead from five origins through 2025's festival: naive lags by a week."""
    idx = list(range(53, 58))
    fig, ax = plt.subplots(figsize=(11, 4.4))
    xs = list(range(len(idx)))
    ax.plot(xs, [y[i] for i in idx], color=INK, lw=2.8, marker="o", label="actual")
    ax.plot(xs, [y[i - 1] for i in idx], color=ROSE, lw=2, ls="--", marker="s", label="naive: the week before")
    ax.plot(xs, [round(y[i - 51] * gen.DRIFT) for i in idx], color=VIOLET, lw=2, ls="--", marker="^",
            label="festival-aligned: 2024 at the same distance, plus 4 percent")
    ax.set_xticks(xs)
    ax.set_xticklabels([dm(i) + " 2025" for i in idx])
    ax.set_ylim(150_000, 470_000)
    thousands(ax)
    ax.set_ylabel("shipments in the week")
    ax.set_title("Forecast one week ahead, five times: naive arrives a week late every time")
    ax.legend(frameon=False, loc="upper right", fontsize=12)
    save(fig, "rolling_origin")


def main():
    for old in OUT.glob("C2_W04_D05_*"):
        old.unlink()
    four_patterns(); twelve_rows(); festival_plot(); actual_series(); baselines_panel(); scoreboard()
    fit_vs_forecast(); holdout_reveal(); festival_calendar(); festival_calendar(copy=False); backtest(); cushion_strip(); window_2026(); cost_curve()
    four_vs_thirteen(); rolling_origin()
    print("\n".join(sorted(p.name for p in OUT.iterdir())))


if __name__ == "__main__":
    main()

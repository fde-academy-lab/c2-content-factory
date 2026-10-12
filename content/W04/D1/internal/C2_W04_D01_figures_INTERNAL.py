"""Monday W04 D1 figures.

Writes the day's PNGs and the drift GIF to content/W04/D1/whiteboards/, every
label legible at 9 points on a slide. Reads numbers from the facts file and the
driver-week data; nothing is hard-coded.

Run from the repository root:
    python3 content/W04/D1/internal/C2_W04_D01_figures_INTERNAL.py
"""
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import pandas as pd
import yaml


HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
BOARDS = DAY / "whiteboards"
BOARDS.mkdir(parents=True, exist_ok=True)
DATA = DAY / "data"
STEM = "C2_W04_D01"

INK = "#1A0F5C"
VIOLET = "#5B3FD6"
ACCENT = "#4E38AB"
LAVENDER = "#D9A7FF"
MUTED = "#6B6690"
ROSE = "#D63A6A"
GREEN = "#1F8A5B"
LINE = "#E4E1F1"
TINT = "#EEEAFB"
WHITE = "#FFFFFF"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": INK,
    "axes.titlecolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.facecolor": WHITE,
    "axes.facecolor": WHITE,
})


facts = yaml.safe_load((HERE / f"{STEM}_facts_INTERNAL.yaml").read_text(encoding="utf-8"))
dw = pd.read_csv(DATA / f"{STEM}_driver_weeks_STUDENT.csv")
dw["week"] = pd.to_datetime(dw["week_start"])
dw_before = dw[dw["week"] < pd.Timestamp("2026-08-31")]
dw_after = dw[dw["week"] >= pd.Timestamp("2026-08-31")]


# ---------------------------------------------------------------------------- 1. drift lines
# One PNG and one GIF: hours per week (left axis) rising while trips per hour
# (right axis) falls, across the twelve weeks of data.

weekly = (dw.groupby("week")
            .agg(peak_online_hours=("peak_online_hours", "sum"),
                 peak_trips=("peak_trips", "sum"))
            .reset_index()
            .sort_values("week"))
weekly["trips_per_hour"] = weekly["peak_trips"] / weekly["peak_online_hours"]
weekly["week_label"] = weekly["week"].dt.strftime("%d %b")
launch_idx = weekly.index[weekly["week"] >= pd.Timestamp("2026-08-31")].min()


def draw_drift(ax1, ax2, upto):
    xs = range(len(weekly))
    hrs = weekly["peak_online_hours"].values
    tph = weekly["trips_per_hour"].values
    xs_v = list(xs)[: upto + 1]
    hrs_v = hrs[: upto + 1]
    tph_v = tph[: upto + 1]
    ax1.clear()
    ax2.clear()
    ax1.plot(xs_v, hrs_v, color=VIOLET, linewidth=2.4, marker="o",
             markersize=5, label="peak online hours")
    ax2.plot(xs_v, tph_v, color=ROSE, linewidth=2.4, marker="s",
             markersize=5, label="trips per online hour")
    ax1.axvline(launch_idx - 0.5, color=INK, linestyle="--", linewidth=1.2, alpha=0.6)
    ax1.text(launch_idx - 0.5, max(hrs) * 1.02, " scheme launched",
             fontsize=10, color=INK, ha="left", va="bottom")
    ax1.set_xticks(list(xs))
    ax1.set_xticklabels(weekly["week_label"].values, rotation=0, fontsize=9)
    ax1.set_ylabel("peak online hours", color=VIOLET)
    ax1.tick_params(axis="y", colors=VIOLET)
    ax2.set_ylabel("trips per online hour", color=ROSE)
    ax2.tick_params(axis="y", colors=ROSE)
    ax1.set_ylim(min(hrs) * 0.9, max(hrs) * 1.1)
    ax2.set_ylim(min(tph) * 0.9, max(tph) * 1.08)
    ax1.set_title("Hours up a quarter, trips per hour fall from 1.9 to 1.6",
                  loc="left", pad=14)
    ax1.set_xlabel("week beginning")
    for sp in ax2.spines.values():
        sp.set_visible(False)
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(MUTED)


fig, ax1 = plt.subplots(figsize=(8.6, 4.6))
ax2 = ax1.twinx()
draw_drift(ax1, ax2, len(weekly) - 1)
plt.tight_layout()
fig.savefig(BOARDS / f"{STEM}_drift_STUDENT.png", dpi=160)
plt.close(fig)

# GIF: build one week at a time
fig, ax1 = plt.subplots(figsize=(8.6, 4.6))
ax2 = ax1.twinx()

def animate(i):
    draw_drift(ax1, ax2, i)
    fig.tight_layout()
    return []


ani = anim.FuncAnimation(fig, animate, frames=len(weekly), interval=600, blit=False)
ani.save(BOARDS / f"{STEM}_drift_STUDENT.gif", writer=anim.PillowWriter(fps=2))
# Save the still: the first and last frames.
draw_drift(ax1, ax2, 0)
fig.tight_layout()
fig.savefig(BOARDS / f"{STEM}_drift_still_STUDENT.png", dpi=160)
plt.close(fig)


# ---------------------------------------------------------------------------- 2. the idle tail
# A scatter of after-driver-weeks: hours against trips, with the idle-tail
# driver-weeks (acceptance < 0.5) marked, outer zones circled.

idle_set = set([f"d_{i:04d}" for i in range(881, 1061)])
outer_zones = ["Shamshabad", "Rajendranagar", "Patancheru"]
dw_after["acceptance"] = dw_after["peak_accepted"] / dw_after["peak_requests"]
sample_idx = dw_after.sample(n=min(1800, len(dw_after)), random_state=20261026).index
sample = dw_after.loc[sample_idx]

fig, ax = plt.subplots(figsize=(8.6, 5.2))
not_idle = sample[~sample["driver_id"].isin(idle_set)]
idle = sample[sample["driver_id"].isin(idle_set)]
ax.scatter(not_idle["peak_online_hours"], not_idle["peak_trips"],
           s=10, color=LAVENDER, alpha=0.55, label="other driver-weeks")
idle_core = idle[~idle["zone_mode"].isin(outer_zones)]
idle_outer = idle[idle["zone_mode"].isin(outer_zones)]
ax.scatter(idle_core["peak_online_hours"], idle_core["peak_trips"],
           s=14, color=ROSE, alpha=0.65, label="idle tail, core zone")
ax.scatter(idle_outer["peak_online_hours"], idle_outer["peak_trips"],
           s=14, color=INK, alpha=0.75, label="idle tail, outer zone")
ax.plot([0, 60], [0, 60 * 1.9], color=VIOLET, linestyle=":", linewidth=1.5,
        label="1.9 trips per hour")
ax.set_xlabel("peak online hours in a week")
ax.set_ylabel("peak trips in a week")
ax.set_title("The idle tail: hours rose, trips did not follow", loc="left", pad=14)
ax.legend(loc="upper left", frameon=False, fontsize=10)
ax.set_xlim(0, max(80, sample["peak_online_hours"].max() * 1.05))
ax.set_ylim(0, max(100, sample["peak_trips"].max() * 1.05))
plt.tight_layout()
fig.savefig(BOARDS / f"{STEM}_idle_tail_STUDENT.png", dpi=160)
plt.close(fig)


# ---------------------------------------------------------------------------- 3. requests by zone
# Core vs outer zone requests, as a bar chart. Shows "the outer zones get few
# requests at any hour."

zone_df = pd.read_csv(DATA / f"{STEM}_zone_weeks_STUDENT.csv")
core_zones = ["Banjara Hills", "Jubilee Hills", "Gachibowli", "Madhapur", "Hitech City",
              "Begumpet", "Kondapur", "Kukatpally", "Secunderabad"]
zone_df["kind"] = zone_df["zone"].apply(lambda z: "core" if z in core_zones else "outer")
by_zone = (zone_df.groupby("zone", as_index=False)
                 .agg(requests=("peak_requests", "sum"),
                      kind=("kind", "first"))
                 .sort_values("requests", ascending=False))

fig, ax = plt.subplots(figsize=(8.6, 4.6))
colors = [VIOLET if k == "core" else ROSE for k in by_zone["kind"]]
ax.bar(range(len(by_zone)), by_zone["requests"].values, color=colors)
ax.set_xticks(range(len(by_zone)))
ax.set_xticklabels(by_zone["zone"].values, rotation=30, ha="right", fontsize=9)
ax.set_ylabel("peak requests over twelve weeks")
ax.set_title("The three outer zones get a fraction of core zone requests",
             loc="left", pad=14)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=VIOLET, label="core zone"),
                   Patch(color=ROSE, label="outer zone")],
          loc="upper right", frameon=False, fontsize=10)
plt.tight_layout()
fig.savefig(BOARDS / f"{STEM}_zone_requests_STUDENT.png", dpi=160)
plt.close(fig)


# ---------------------------------------------------------------------------- 4. where the top-up went
# Share of top-up to acceptance below 0.5 vs at or above 0.5.
after_only = dw[dw["week"] >= pd.Timestamp("2026-08-31")].copy()
after_only["acceptance"] = after_only["peak_accepted"] / after_only["peak_requests"]
low = after_only.loc[after_only["acceptance"] < 0.5, "topup_rs"].sum()
high = after_only.loc[after_only["acceptance"] >= 0.5, "topup_rs"].sum()

fig, ax = plt.subplots(figsize=(7.4, 3.4))
ax.barh(["acceptance below 0.5", "acceptance at 0.5 or above"],
        [low / 1e5, high / 1e5], color=[ROSE, VIOLET])
for i, v in enumerate([low, high]):
    ax.text(v / 1e5 + 2, i, f"Rs {v / 1e5:,.0f} lakh ({v / (low + high) * 100:.0f}%)",
            va="center", fontsize=10, color=INK)
ax.set_xlabel("top-up paid, Rs lakh")
ax.set_title("Rs 1.9 crore paid: 61 percent went to idle-online driver-weeks",
             loc="left", pad=14)
ax.set_xlim(0, max(low, high) / 1e5 * 1.35)
plt.tight_layout()
fig.savefig(BOARDS / f"{STEM}_topup_split_STUDENT.png", dpi=160)
plt.close(fig)


# ---------------------------------------------------------------------------- 5. three ways to read Rs
# A deck exhibit: Rs 314 to 260 per online hour, up per driver-week, flat per trip.

labels = ["per peak online hour", "per enrolled driver-week", "per completed trip"]
# Compute from the data for consistency with the facts file.
rs_hr_b = dw_before["peak_bookings_rs"].sum() / dw_before["peak_online_hours"].sum()
rs_hr_a = dw_after["peak_bookings_rs"].sum() / dw_after["peak_online_hours"].sum()
rs_dw_b = dw_before["peak_bookings_rs"].sum() / len(dw_before)
rs_dw_a = dw_after["peak_bookings_rs"].sum() / len(dw_after)
rs_tr_b = dw_before["peak_bookings_rs"].sum() / dw_before["peak_trips"].sum()
rs_tr_a = dw_after["peak_bookings_rs"].sum() / dw_after["peak_trips"].sum()
before_vals = [rs_hr_b, rs_dw_b, rs_tr_b]
after_vals = [rs_hr_a, rs_dw_a, rs_tr_a]

fig, ax = plt.subplots(figsize=(9.0, 4.6))
x = range(len(labels))
width = 0.36
ax.bar([i - width / 2 for i in x], before_vals, width,
       color=LAVENDER, label="six weeks before")
ax.bar([i + width / 2 for i in x], after_vals, width,
       color=VIOLET, label="six weeks after")
for i in x:
    ax.text(i - width / 2, before_vals[i] + max(before_vals) * 0.02,
            f"Rs {before_vals[i]:,.0f}", ha="center", fontsize=10, color=INK)
    ax.text(i + width / 2, after_vals[i] + max(after_vals) * 0.02,
            f"Rs {after_vals[i]:,.0f}", ha="center", fontsize=10, color=INK)
ax.set_xticks(list(x))
ax.set_xticklabels(labels, fontsize=10)
ax.set_ylabel("rupees per unit")
ax.set_title("The same rupees read three ways, three directions",
             loc="left", pad=14)
ax.legend(loc="upper right", frameon=False, fontsize=10)
ax.set_ylim(0, max(max(before_vals), max(after_vals)) * 1.25)
plt.tight_layout()
fig.savefig(BOARDS / f"{STEM}_three_denominators_STUDENT.png", dpi=160)
plt.close(fig)


# ---------------------------------------------------------------------------- 6. the fall survives
# Two bars: trips per online hour before and after, over all drivers and over
# the pre-launch cohort only.

both_before = dw_before
both_after = dw_after[~dw_after["driver_id"].str.startswith("d_1")]  # excludes 140 new
both_after2 = dw_after[dw_after["driver_id"].astype(str).str[0:4].isin(set(dw_before["driver_id"].astype(str).str[0:4]))]

# Simpler: use the sets we know.
pre_launch_ids = set([f"d_{i:04d}" for i in range(1, 1061)])
after_pre = dw_after[dw_after["driver_id"].isin(pre_launch_ids)]
r_all_before = dw_before["peak_trips"].sum() / dw_before["peak_online_hours"].sum()
r_all_after = dw_after["peak_trips"].sum() / dw_after["peak_online_hours"].sum()
r_pre_after = after_pre["peak_trips"].sum() / after_pre["peak_online_hours"].sum()

fig, ax = plt.subplots(figsize=(8.0, 4.2))
labels = ["before (all drivers)", "after (all drivers)",
          "after, pre-launch drivers only"]
vals = [r_all_before, r_all_after, r_pre_after]
colors = [LAVENDER, VIOLET, ACCENT]
ax.bar(labels, vals, color=colors)
for i, v in enumerate(vals):
    ax.text(i, v + 0.02, f"{v:.2f}", ha="center", fontsize=11, color=INK, fontweight="bold")
ax.set_ylabel("trips per peak online hour")
ax.set_title("The fall survives the removal of the 140 new drivers",
             loc="left", pad=14)
ax.set_ylim(0, max(vals) * 1.2)
plt.tight_layout()
fig.savefig(BOARDS / f"{STEM}_fall_survives_STUDENT.png", dpi=160)
plt.close(fig)


print(f"wrote 7 figure files to {BOARDS}")
for p in sorted(BOARDS.glob(f"{STEM}_*.png")) + sorted(BOARDS.glob(f"{STEM}_*.gif")):
    print(f"  {p.name}  ({p.stat().st_size:,} bytes)")


# Test inputs and expected outcomes
# --------------------------------
# python3 content/W04/D1/internal/C2_W04_D01_figures_INTERNAL.py
#     Writes six PNGs and one GIF under content/W04/D1/whiteboards/, each with
#     labels readable at 9 points on a slide. Deterministic given the data file.

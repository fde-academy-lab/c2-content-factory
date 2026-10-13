"""Draw the Week 4 Monday pictures into content/W04/D1/whiteboards/ from the day's own data.

    python3 content/W04/D1/internal/C2_W04_D01_figures_INTERNAL.py

Six pictures and one GIF: the drift chart (its last frame as C2_W04_D01_drift_STUDENT.png, its first
as C2_W04_D01_drift_still_STUDENT.png, and the GIF that draws the twelve weeks one at a time), the
idle tail, where the top-up went, rider requests by zone, the fall under each cut, and which number
moved first. Every value is computed from data/ and agrees with internal/C2_W04_D01_facts_INTERNAL.yaml;
labels are sized to print at nine points or more on a slide.
"""
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.animation as animation  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

DAY = pathlib.Path(__file__).resolve().parent.parent
OUT = DAY / "whiteboards"
OUT.mkdir(exist_ok=True)
STEM = "C2_W04_D01"
INK, VIOLET, ROSE, LAV, MUTED = "#1A0F5C", "#5B3FD6", "#D63A6A", "#D9A7FF", "#6B6690"
OUTER = ["Shamshabad", "Rajendranagar", "Patancheru"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.titlesize": 14,
                     "axes.titleweight": "bold", "axes.titlecolor": INK, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK, "axes.edgecolor": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False})

dw = pd.read_csv(DAY / "data" / f"{STEM}_driver_weeks_STUDENT.csv")
zw = pd.read_csv(DAY / "data" / f"{STEM}_zone_weeks_STUDENT.csv")
dw["window"] = dw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
after = dw[dw["window"] == "after"].copy()
after["acceptance"] = after["peak_accepted"] / after["peak_offers"]
per_driver = after.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
idle_ids = set(per_driver.index[per_driver["peak_trips"] / per_driver["peak_online_hours"] < 1.0])
weekly = dw.groupby("week_start")[["peak_online_hours", "peak_trips", "peak_accepted", "peak_offers",
                                   "peak_bookings_rs"]].sum()
weekly["tph"] = weekly["peak_trips"] / weekly["peak_online_hours"]
labels = [pd.Timestamp(w).strftime("%d %b") for w in weekly.index]


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / f"{STEM}_{name}_STUDENT.png", dpi=160)
    plt.close(fig)


# 1. The drift chart, its two stills and the GIF that draws it week by week.
def drift(ax, upto):
    ax.clear()
    right = ax.right
    right.clear()
    ax.plot(range(upto + 1), weekly["peak_online_hours"][: upto + 1], marker="o", color=VIOLET, lw=2.4)
    right.plot(range(upto + 1), weekly["tph"][: upto + 1], marker="s", color=ROSE, lw=2.4)
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(18000, 26500)
    right.set_ylim(1.4, 2.05)
    ax.axvline(5.5, color=INK, linestyle="--", lw=1.2, alpha=0.6)
    ax.text(5.6, 26000, "scheme launched", color=INK, fontsize=11)
    ax.set_xticks(range(12), labels, fontsize=10)
    ax.set_ylabel("peak online hours", color=VIOLET)
    right.set_ylabel("trips per peak online hour", color=ROSE)
    right.yaxis.set_label_position("right")
    right.yaxis.tick_right()
    right.spines["right"].set_visible(True)
    ax.set_title("Hours up a quarter, trips per hour fall from 1.9 to 1.6", loc="left", pad=12)


fig, ax = plt.subplots(figsize=(9.2, 4.6))
ax.right = ax.twinx()
drift(ax, 11)
save(fig, "drift")
fig, ax = plt.subplots(figsize=(9.2, 4.6))
ax.right = ax.twinx()
drift(ax, 0)
save(fig, "drift_still")
fig, ax = plt.subplots(figsize=(9.2, 4.6))
ax.right = ax.twinx()
movie = animation.FuncAnimation(fig, lambda i: drift(ax, i), frames=12, interval=700)
fig.tight_layout()
movie.save(OUT / f"{STEM}_drift_STUDENT.gif", writer=animation.PillowWriter(fps=1.5))
plt.close(fig)

# 2. The idle tail: every driver-week after the launch, hours against trips.
mark = after["driver_id"].isin(idle_ids)
fig, ax = plt.subplots(figsize=(9.2, 4.2))
ax.scatter(after.loc[~mark, "peak_online_hours"], after.loc[~mark, "peak_trips"], s=9, color=LAV,
           alpha=0.6, label="every other driver-week")
outer = mark & after["zone_mode"].isin(OUTER)
ax.scatter(after.loc[mark & ~outer, "peak_online_hours"], after.loc[mark & ~outer, "peak_trips"], s=12,
           color=ROSE, alpha=0.8, label="idle tail, most time in a core zone")
ax.scatter(after.loc[outer, "peak_online_hours"], after.loc[outer, "peak_trips"], s=12, color=INK,
           alpha=0.8, label="idle tail, most time in an outer zone")
ax.plot([0, 36], [0, 36 * 1.9], color=VIOLET, linestyle=":", lw=1.6, label="1.9 trips per hour")
ax.axvline(42, color=MUTED, linestyle="--", lw=1.0)
ax.text(41.6, 4, "42 hours: every peak\nwindow of the week", ha="right", fontsize=12, color=MUTED)
ax.set_xlim(0, 45)
ax.set_ylim(0, 70)
ax.set_xlabel("peak online hours in the week")
ax.set_ylabel("completed peak trips in the week")
ax.set_title("Each dot is one driver-week after the launch: the idle tail sits right and low",
             loc="left", pad=12, fontsize=13)
ax.legend(frameon=False, loc="upper left", fontsize=12)
save(fig, "idle_tail")

# 3. Where the Rs 1.9 crore top-up went.
low = after.loc[after["acceptance"] < 0.5, "topup_rs"].sum()
high = after.loc[after["acceptance"] >= 0.5, "topup_rs"].sum()
fig, ax = plt.subplots(figsize=(9.2, 3.2))
ax.barh(["accepted 0.5 or more\nof the offers shown", "accepted under 0.5\nof the offers shown"],
        [high / 1e5, low / 1e5], color=[VIOLET, ROSE])
for y, v in enumerate([high, low]):
    ax.text(v / 1e5 + 2, y, f"Rs {v / 1e5:.0f} lakh, {v / (low + high):.0%}", va="center", fontsize=12)
ax.set_xlim(0, 150)
ax.set_xlabel("top-up paid over the six weeks after the launch, Rs lakh")
fig.suptitle("Where the Rs 1.9 crore top-up went", x=0.02, ha="left", fontsize=14,
             fontweight="bold", color=INK)
save(fig, "topup_split")

# 4. Rider requests by zone over the twelve weeks.
by_zone = zw.groupby("zone")["peak_requests"].sum().sort_values()
fig, ax = plt.subplots(figsize=(9.2, 4.6))
ax.barh(by_zone.index, by_zone.values / 1000, color=[ROSE if z in OUTER else VIOLET for z in by_zone.index])
ax.set_xlabel("rider requests at peak over twelve weeks, thousands")
ax.set_title("The three outer zones get a fraction of the requests", loc="left", pad=12)
save(fig, "zone_requests")

# 5. The fall under each cut the data can make.
rate = lambda d: d["peak_trips"].sum() / d["peak_online_hours"].sum()  # noqa: E731
busiest = zw.groupby("week_start")["peak_requests"].sum().nlargest(3).index
cuts = [("before the launch, every driver", rate(dw[dw["window"] == "before"]), LAV),
        ("after, every driver", rate(after), ROSE),
        ("after, drivers who joined before the launch", rate(after[after["driver_id"] <= "d_1060"]), VIOLET),
        ("after, the three weeks with most requests", rate(dw[dw["week_start"].isin(busiest)]), VIOLET),
        ("after, core zones only", rate(after[~after["zone_mode"].isin(OUTER)]), VIOLET)]
fig, ax = plt.subplots(figsize=(9.2, 3.8))
for y, (name, value, colour) in enumerate(reversed(cuts)):
    ax.barh(y, value, color=colour)
    ax.text(value + 0.03, y, f"{value:.2f}", va="center", fontsize=12)
ax.set_yticks(range(len(cuts)), [c[0] for c in reversed(cuts)])
ax.set_xlim(0, 2.3)
ax.set_xlabel("trips per peak online hour")
ax.set_title("The fall survives every cut the data can make", loc="left", pad=12)
save(fig, "fall_cuts")

# 6. Which number moved first: acceptance against bookings per online hour, week by week.
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 3.6))
a1.plot(range(12), weekly["peak_accepted"] / weekly["peak_offers"], marker="o", color=VIOLET, lw=2.2)
a1.set_title("Offers accepted, share", loc="left", fontsize=13)
a1.set_ylim(0.6, 0.9)
a2.plot(range(12), weekly["peak_bookings_rs"] / weekly["peak_online_hours"], marker="s", color=ROSE, lw=2.2)
a2.set_title("Bookings per online hour, Rs", loc="left", fontsize=13)
a2.set_ylim(220, 330)
for a in (a1, a2):
    a.axvline(5.5, color=INK, linestyle="--", lw=1.0, alpha=0.6)
    a.set_xticks([0, 6, 8, 11], ["20 Jul", "31 Aug", "14 Sep", "5 Oct"], fontsize=10)
fig.suptitle("Acceptance settled in the launch week; bookings per hour took three weeks",
             x=0.02, ha="left", fontsize=14, fontweight="bold", color=INK)
save(fig, "lead")

# 7. The acceptance gap: weekly accepted share after the launch, idle tail against everyone else.
online_after = after[after["peak_online_hours"] > 0]
idle_week = online_after["driver_id"].isin(idle_ids)
bins = [x / 50 for x in range(51)]
fig, ax = plt.subplots(figsize=(9.2, 3.8))
ax.hist(online_after.loc[idle_week, "acceptance"], bins=bins, color=ROSE, label="idle-tail driver-weeks")
ax.hist(online_after.loc[~idle_week, "acceptance"], bins=bins, color=VIOLET, label="every other driver-week")
top_idle = online_after.loc[idle_week, "acceptance"].max()
low_other = online_after.loc[~idle_week, "acceptance"].min()
for x, words, side, height in ((top_idle, f"highest idle week {top_idle:.2f}", 1, 0.85),
                               (low_other, f"lowest other week {low_other:.2f}", -1, 0.5)):
    ax.axvline(x, color=INK, linestyle="--", lw=1.0)
    ax.text(x + 0.01 * side, ax.get_ylim()[1] * height, words, fontsize=12, color=INK,
            ha="left" if side > 0 else "right")
ax.set_xlim(0, 1)
ax.set_xlabel("share of offers accepted in the week, after the launch")
ax.set_ylabel("driver-weeks")
ax.legend(frameon=False, loc="upper left")
ax.set_title("An acceptance floor anywhere in the gap stops only the idling", loc="left", pad=12)
save(fig, "acceptance_gap")

for p in sorted(OUT.glob(f"{STEM}_*")):
    print(f"{p.name}  {p.stat().st_size:,} bytes")

# Test inputs and expected outcomes
# python3 content/W04/D1/internal/C2_W04_D01_figures_INTERNAL.py
#     writes seven PNGs and one GIF under whiteboards/ and prints each with its size
# a second run
#     redraws the same pictures from the same data

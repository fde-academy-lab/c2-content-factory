"""Week 4 Tuesday figures, every number read from Tuesday's facts file.

Writes the day's data pictures to content/W04/D2/whiteboards/. Mechanisms (the four moves, the
slide anatomy, the guesstimate tree, the week map) are mermaid fences in the decks and the sheet,
so this script draws only pictures of data, and of the one slide the room rebuilds.

    C2_W04_D02_cluttered_slide_STUDENT.png   slide A as it arrived: nine Monday numbers, a topic title
    C2_W04_D02_cleared_slide_STUDENT.png     slide A rebuilt: claim, evidence, caveat, action, numbered
    C2_W04_D02_cluttered_chart_STUDENT.png   the twelve weeks in three units on one axis
    C2_W04_D02_three_denominators_STUDENT.png the twelve rows read in rupees three ways
    C2_W04_D02_three_reads_STUDENT.png       the twelve weeks, each read indexed to its before window
    C2_W04_D02_guesstimate_swing_STUDENT.png how far each assumption moves the drivers-at-peak answer

Every label is set at 12 points or more on a figure no wider than 10 inches, so it prints above
9 points on a slide and above 5 on the sheet.

Run from the repository root, after the generator:
    python3 content/W04/D2/internal/C2_W04_D02_figures_INTERNAL.py
"""
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import matplotlib.ticker
import yaml

HERE = pathlib.Path(__file__).resolve().parent
BOARDS = HERE.parent / "whiteboards"
STEM = "C2_W04_D02"

INK, VIOLET, MUTED, ROSE = "#1A0F5C", "#5B3FD6", "#6B6690", "#D63A6A"
GREEN, AMBER, AMBER_TINT, TINT, LINE = "#1F8A5B", "#C98A00", "#FFF7E6", "#EEEAFB", "#E4E1F1"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13, "axes.titlesize": 15, "axes.titleweight": "bold",
    "axes.labelsize": 13, "xtick.labelsize": 12, "ytick.labelsize": 12, "axes.edgecolor": MUTED,
    "axes.labelcolor": INK, "axes.titlecolor": INK, "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white",
})

facts = yaml.safe_load((HERE / f"{STEM}_facts_INTERNAL.yaml").read_text(encoding="utf-8"))
N = {n["id"]: n for n in facts["numbers"]}
MON = {n["id"]: n for n in facts["monday_ids_reused"]}
AS = {a["id"]: a for a in facts["assumptions"]}
WEEKS = facts["weekly_series"]
LABELS = [str(int(w["week_start"][8:])) + " " + {"07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct"}[w["week_start"][5:7]]
          for w in WEEKS]


def save(fig, name):
    out = BOARDS / f"{STEM}_{name}_STUDENT.png"
    fig.savefig(out, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.name}")


def box(ax, x, y, w, h, edge, fill):
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                        linewidth=1.4, edgecolor=edge, facecolor=fill))


def cluttered_slide():
    """Slide A as the operations analyst sent it: a topic title and nine numbers of equal weight."""
    rows = facts["cluttered_slides"]["A_dashboard"]
    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.set_xlim(0, 10), ax.set_ylim(0, 5.6), ax.axis("off")
    ax.text(5, 5.25, "Peak guarantee: six-week review", ha="center", fontsize=19, weight="bold", color=INK)
    for i, r in enumerate(rows):
        col, row = i % 3, i // 3
        x, y = 0.25 + col * 3.25, 3.55 - row * 1.55
        box(ax, x, y, 3.0, 1.3, LINE, TINT)
        ax.text(x + 1.5, y + 0.92, r["label"], ha="center", fontsize=12, color=MUTED)
        ax.text(x + 1.5, y + 0.38, r["shows"], ha="center", fontsize=16, weight="bold", color=INK)
    return fig


def week_chart(ax, emphasis=True):
    """Rupees per peak online hour over the twelve weeks, the slide's one piece of evidence."""
    xs = range(len(WEEKS))
    ys = [w["rs_per_hour"] for w in WEEKS]
    ax.plot(xs, ys, color=VIOLET, lw=3, marker="o", ms=6)
    before = MON["rs_per_hour_before"]["value"]
    after = MON["rs_per_hour_after"]["value"]
    ax.hlines(before, -0.3, 5.3, color=MUTED, ls=":", lw=1.6)
    ax.hlines(after, 5.7, 11.3, color=MUTED, ls=":", lw=1.6)
    ax.text(2.5, before + 6, f"six weeks before: Rs {before:.0f}", ha="center", fontsize=13, color=INK)
    ax.text(8.5, after - 13, f"six weeks after: Rs {after:.0f}", ha="center", fontsize=13, color=INK)
    ax.axvline(5.5, color=ROSE, lw=1.4, ls="--")
    ax.text(5.6, 334, "launch,\n31 Aug", fontsize=12, color=ROSE, va="top")
    ax.set_ylim(220, 340)
    ax.set_xticks(list(xs)[::2], LABELS[::2])
    ax.set_ylabel("Rs per peak online hour")


def cleared_slide():
    """Slide A rebuilt: the four parts, numbered where they sit on the page."""
    fig = plt.figure(figsize=(10, 5.6))
    top = fig.add_axes([0, 0, 1, 1]); top.set_xlim(0, 10); top.set_ylim(0, 5.6); top.axis("off")
    top.text(0.25, 5.2, "1  The scheme is paying for online hours that carry no trips",
             fontsize=17, weight="bold", color=INK)
    top.text(0.55, 4.82, "pay per completed peak trip, with an acceptance floor", fontsize=13,
             color=MUTED, style="italic")
    chart = fig.add_axes([0.07, 0.12, 0.55, 0.62])
    week_chart(chart)
    chart.set_title("2  Gross bookings per peak online hour", fontsize=14, loc="left", color=INK)
    box(top, 6.55, 2.75, 3.25, 1.75, AMBER, AMBER_TINT)
    top.text(6.7, 4.2, "3  Caveat", fontsize=13, weight="bold", color=AMBER)
    top.text(6.7, 3.95, "The monsoon ended inside the\nwindow, and last year's weeks\n"
             "are not in the data, so part\nof the fall may be the season.", fontsize=12, color=INK,
             va="top")
    box(top, 6.55, 0.55, 3.25, 1.95, GREEN, "white")
    lo, hi = MON["saving_low_rs"]["shown"], MON["saving_high_rs"]["shown"]
    top.text(6.7, 2.2, "4  Action, for the city head", fontsize=13, weight="bold", color=GREEN)
    top.text(6.7, 1.95, f"Pay per completed peak trip\nwith an acceptance floor:\n{lo} to {hi} back over\n"
             "six weeks if a fifth to a half\nof idle drivers start accepting.", fontsize=12, color=INK,
             va="top")
    return fig


def cluttered_chart():
    """The twelve weeks as the dashboard drew them: three units on one axis, a legend, a grid."""
    fig, ax = plt.subplots(figsize=(10, 5.2))
    xs = range(len(WEEKS))
    ax.plot(xs, [w["rs_per_hour"] for w in WEEKS], marker="o", label="Rs per online hour")
    ax.plot(xs, [w["rs_per_driver_week"] / 20 for w in WEEKS], marker="s", label="Rs per driver-week / 20")
    ax.plot(xs, [w["rs_per_trip"] for w in WEEKS], marker="^", label="Rs per trip")
    ax.plot(xs, [w["peak_online_hours"] / 100 for w in WEEKS], marker="x", label="online hours / 100")
    ax.grid(True, color="#BBBBBB")
    ax.set_xticks(list(xs), LABELS, rotation=45)
    ax.set_title("Peak metrics, weeks of 20 Jul to 5 Oct")
    ax.set_ylabel("value (mixed units)")
    ax.legend(loc="lower left", fontsize=12, ncol=2)
    return fig


def three_denominators():
    """The twelve rows' rupees read per online hour, per driver-week and per trip."""
    panels = [("Per peak online hour", "twelve_rs_per_hour_before", "twelve_rs_per_hour_after",
               "twelve_rs_per_hour_change_pct"),
              ("Per driver-week", "twelve_rs_per_driver_week_before", "twelve_rs_per_driver_week_after",
               "twelve_rs_per_driver_week_change_pct"),
              ("Per trip", "twelve_rs_per_trip", "twelve_rs_per_trip", None)]
    fig, axes = plt.subplots(1, 3, figsize=(10, 4.8))
    for ax, (title, b, a, pct) in zip(axes, panels):
        vals = [N[b]["value"], N[a]["value"]]
        ax.bar(["before", "after"], vals, color=[VIOLET, ROSE if pct else GREEN], width=0.6)
        for i, v in enumerate(vals):
            ax.text(i, v * 1.02, f"Rs {v:,.0f}" if v >= 1000 else f"Rs {v:g}", ha="center",
                    fontsize=13, weight="bold", color=INK)
        ax.set_ylim(0, max(vals) * 1.25), ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_title(title, fontsize=14)
        ax.text(0.5, -0.17, N[pct]["shown"] if pct else "flat", transform=ax.transAxes,
                ha="center", fontsize=13, color=MUTED, style="italic")
    fig.suptitle("Six drivers, two weeks, the same rupees three ways", fontsize=15, weight="bold", color=INK)
    fig.tight_layout()
    return fig


def three_reads():
    """Each read divided by its own before-window value, so the three share one axis at 100."""
    reads = [("per online hour", "rs_per_hour", MON["rs_per_hour_before"]["value"], VIOLET),
             ("per active driver-week", "rs_per_driver_week", MON["rs_per_driver_week_before"]["value"], AMBER),
             ("per trip", "rs_per_trip", MON["fare_avg_rs"]["value"], GREEN)]
    fig, ax = plt.subplots(figsize=(10, 5.2))
    xs = range(len(WEEKS))
    for label, key, base, colour in reads:
        ys = [100 * w[key] / base for w in WEEKS]
        ax.plot(xs, ys, color=colour, lw=2.8, marker="o", ms=5)
        ax.text(11.3, ys[-1], label, color=colour, fontsize=13, va="center")
    ax.axhline(100, color=MUTED, lw=1, ls=":")
    ax.axvline(5.5, color=ROSE, lw=1.4, ls="--")
    ax.text(5.6, 107.5, "launch", color=ROSE, fontsize=12)
    ax.set_xlim(-0.4, 14.6), ax.set_ylim(78, 109)
    ax.set_xticks(list(xs)[::2], LABELS[::2])
    ax.set_ylabel("index, before window = 100")
    ax.set_title("The same rupees, three denominators, three directions", loc="left")
    return fig


def guesstimate_swing():
    """One assumption at a time at its low and high end, every other factor at its central value."""
    names = {"weekday_ride_share": "people who ride on a weekday", "evening_share": "share in the evening",
             "trips_per_busy_hour": "trips a busy driver fits in", "idle_share": "idle share",
             "hyd_people": "people in the city", "buffer": "buffer for the busiest half hour"}
    order = sorted(names, key=lambda k: N[f"swing_{k}_high"]["value"] - N[f"swing_{k}_low"]["value"])
    central = N["drivers_at_peak_central"]["value"]
    fig, ax = plt.subplots(figsize=(10, 5.0))
    for i, k in enumerate(order):
        lo, hi = N[f"swing_{k}_low"]["value"], N[f"swing_{k}_high"]["value"]
        ax.barh(i, hi - lo, left=lo, color=VIOLET if k == order[-1] else "#B9AEF0", height=0.55)
        ax.text(lo - 120, i, f"{round(lo, -2):,.0f}", ha="right", va="center", fontsize=12, color=INK)
        ax.text(hi + 120, i, f"{round(hi, -2):,.0f}", ha="left", va="center", fontsize=12, color=INK)
    ax.axvline(central, color=ROSE, lw=1.6)
    ax.text(central + 80, -0.75, f"central: about {round(central, -2):,.0f}", ha="left",
            fontsize=12, color=ROSE)
    ax.set_ylim(-1.0, len(order) - 0.4)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.set_yticks(range(len(order)), [names[k] for k in order])
    ax.set_xlim(1500, 10500)
    ax.set_xlabel("drivers online at the weekday evening peak")
    ax.set_title("Which assumption moves the answer most?", loc="left")
    return fig


for name, draw in [("cluttered_slide", cluttered_slide), ("cleared_slide", cleared_slide),
                   ("cluttered_chart", cluttered_chart), ("three_denominators", three_denominators),
                   ("three_reads", three_reads), ("guesstimate_swing", guesstimate_swing)]:
    save(draw(), name)

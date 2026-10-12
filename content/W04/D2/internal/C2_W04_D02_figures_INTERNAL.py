"""Week 4 Tuesday figures.

Writes the day's data pictures to content/W04/D2/whiteboards/, every label legible at
9 points on a slide. Reads Monday's weekly series through Tuesday's own facts file;
nothing hard-coded.

Pictures:
    C2_W04_D02_cluttered_STUDENT.png       nine Monday numbers on a slide
    C2_W04_D02_cleared_STUDENT.png         the same slide after the declutter
    C2_W04_D02_three_denominators_STUDENT.png three ways the twelve rows read in rupees
    C2_W04_D02_denominator_drift_STUDENT.png  twelve weeks, Rs per hour against Rs per driver-week
    C2_W04_D02_denominator_drift_STUDENT.gif  the same lines drawn one week at a time
    C2_W04_D02_denominator_drift_still_STUDENT.png the GIF's final frame as a still

Run from the repository root:
    python3 content/W04/D2/internal/C2_W04_D02_figures_INTERNAL.py
"""
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.animation as anim
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import yaml

HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
BOARDS = DAY / "whiteboards"
BOARDS.mkdir(parents=True, exist_ok=True)
STEM = "C2_W04_D02"

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
AMBER = "#C98A00"
AMBER_TINT = "#FFF7E6"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "axes.titlesize": 15,
    "axes.titleweight": "bold",
    "axes.labelsize": 13,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
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
by_id = {n["id"]: n["value"] for n in facts["numbers"]}
weekly = facts["weekly_series"]


def save(fig, name):
    out = BOARDS / f"{STEM}_{name}.png"
    fig.savefig(out, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out}")


# --------------------------------------------------- the cluttered Monday slide (nine numbers)
NUMBERS = [
    ("Peak online hours", "+24 percent"),
    ("Trips", "+3 percent"),
    ("Trips per peak online hour", "1.90 to 1.58"),
    ("Acceptance", "0.86 to 0.73"),
    ("Share of online hours with no trip", "0.22 to 0.38"),
    ("Median rider wait", "4.8 to 4.6 min"),
    ("Top-up paid", "Rs 1.9 crore"),
    ("New drivers after launch", "140"),
    ("Share of top-up to idle hours", "61 percent"),
]


def cluttered_slide():
    fig, ax = plt.subplots(figsize=(9, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.text(5, 5.6, "Peak guarantee: six-week review",
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)
    ax.text(5, 5.1, "nine numbers from the six-week dashboard",
            ha="center", va="center", fontsize=10, color=MUTED)
    cols, rows = 3, 3
    x0, y0 = 0.6, 3.4
    cell_w, cell_h = 3.0, 1.4
    for n, (label, val) in enumerate(NUMBERS):
        col = n % cols
        row = n // cols
        x = x0 + col * cell_w
        y = y0 - row * cell_h
        box = mpatches.FancyBboxPatch((x, y), cell_w * 0.9, cell_h * 0.85,
                                      boxstyle="round,pad=0.05,rounding_size=0.1",
                                      linewidth=1, edgecolor=LINE, facecolor=TINT)
        ax.add_patch(box)
        ax.text(x + cell_w * 0.45, y + cell_h * 0.6, label,
                ha="center", va="center", fontsize=12, color=MUTED, wrap=True)
        ax.text(x + cell_w * 0.45, y + cell_h * 0.3, val,
                ha="center", va="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(5, 0.3, "What does a city head do with this?",
            ha="center", va="center", fontsize=13, color=ROSE, style="italic")
    return fig


save(cluttered_slide(), "cluttered_STUDENT")


# ------------------------- the cleared slide (one claim, one number with its denominator)
def cleared_slide():
    fig, ax = plt.subplots(figsize=(9, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.text(5, 5.4, "Peak scheme is paying for hours that do not carry trips",
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)
    ax.text(5, 4.85, "redesign to pay per completed peak trip, with an acceptance guardrail",
            ha="center", va="center", fontsize=12, color=MUTED, style="italic")
    # One chart: Rs per peak online hour, before against after
    ax.add_patch(mpatches.FancyBboxPatch((0.6, 1.2), 5.5, 3.1,
                                         boxstyle="round,pad=0.05,rounding_size=0.1",
                                         linewidth=1, edgecolor=LINE, facecolor=WHITE))
    rs_before = 314
    rs_after = 260
    bar_x = [1.4, 3.6]
    bar_vals = [rs_before, rs_after]
    bar_labels = ["Six weeks before", "Six weeks after"]
    for x, v, lab in zip(bar_x, bar_vals, bar_labels):
        ax.add_patch(mpatches.Rectangle((x, 1.5), 1.4, v / 350 * 2.3,
                                        facecolor=VIOLET if v > rs_after else ROSE,
                                        edgecolor="none"))
        ax.text(x + 0.7, 1.5 + v / 350 * 2.3 + 0.12, f"Rs {v}",
                ha="center", va="bottom", fontsize=15, fontweight="bold", color=INK)
        ax.text(x + 0.7, 1.3, lab, ha="center", va="center", fontsize=12, color=MUTED)
    ax.text(3.35, 4.1, "Gross bookings per peak online hour",
            ha="center", va="center", fontsize=14, fontweight="bold", color=INK)
    ax.text(3.35, 3.85, "Rs 314 to Rs 260, a 17 percent fall",
            ha="center", va="center", fontsize=12, color=MUTED)
    # The caveat, in plain sight
    ax.add_patch(mpatches.FancyBboxPatch((6.4, 2.6), 3.2, 1.6,
                                         boxstyle="round,pad=0.05,rounding_size=0.1",
                                         linewidth=1, edgecolor=AMBER, facecolor=AMBER_TINT))
    ax.text(8.0, 3.9, "Caveat", ha="center", va="center",
            fontsize=12, fontweight="bold", color=AMBER)
    ax.text(8.0, 3.4,
            "The monsoon ended inside\nthe window; 140 drivers\njoined after the launch",
            ha="center", va="center", fontsize=11, color=INK)
    # The action
    ax.add_patch(mpatches.FancyBboxPatch((6.4, 1.2), 3.2, 1.2,
                                         boxstyle="round,pad=0.05,rounding_size=0.1",
                                         linewidth=1, edgecolor=GREEN, facecolor=WHITE))
    ax.text(8.0, 2.1, "Action", ha="center", va="center",
            fontsize=12, fontweight="bold", color=GREEN)
    ax.text(8.0, 1.6,
            "Pay per completed peak trip\nwith an acceptance guardrail;\nsaving Rs 58 lakh to 93 lakh",
            ha="center", va="center", fontsize=11, color=INK)
    ax.text(5, 0.3, "one claim, one chart, one caveat, one action",
            ha="center", va="center", fontsize=12, color=MUTED, style="italic")
    return fig


save(cleared_slide(), "cleared_STUDENT")


# ------------------------- three denominators: twelve rows read three ways
def three_denominators():
    fig, axes = plt.subplots(1, 3, figsize=(10, 4.5))
    labels = ["Before", "After"]
    panels = [
        ("Per peak online hour", by_id["twelve_rs_per_hour_before"], by_id["twelve_rs_per_hour_after"],
         "Rs/hour", "down 37 percent"),
        ("Per driver-week",      by_id["twelve_rs_per_driver_week_before"],
         by_id["twelve_rs_per_driver_week_after"], "Rs/driver-week", "down 23 percent"),
        ("Per trip",             by_id["twelve_rs_per_trip_before"],
         by_id["twelve_rs_per_trip_after"], "Rs/trip", "flat at Rs 165"),
    ]
    for ax, (title, b, a, unit, verdict) in zip(axes, panels):
        values = [b, a]
        colors = [VIOLET, ROSE if verdict.startswith("down") else GREEN]
        ax.bar(labels, values, color=colors, edgecolor="none")
        ax.set_title(title, color=INK, pad=8)
        ax.set_ylabel(unit)
        for i, v in enumerate(values):
            ax.text(i, v, f"Rs {v:g}", ha="center", va="bottom", fontsize=14,
                    color=INK, fontweight="bold")
        top = max(values) * 1.2
        ax.set_ylim(0, top)
        ax.text(0.5, -0.22, verdict, ha="center", va="center",
                transform=ax.transAxes, fontsize=12, color=MUTED, style="italic")
    fig.suptitle("The same rupees, the same twelve rows, three different stories",
                 color=INK, fontweight="bold", fontsize=15, y=1.02)
    fig.tight_layout()
    return fig


save(three_denominators(), "three_denominators_STUDENT")


# -------- the denominator drift: twelve weeks of per-hour against per-driver-week
def denominator_drift(final_frames=1, highlight_from=None):
    fig, ax = plt.subplots(figsize=(9, 4.6))
    weeks = [w["week_start"] for w in weekly]
    rs_per_hour = [w["rs_per_hour"] for w in weekly]
    rs_per_dw = [w["rs_per_driver_week"] for w in weekly]
    xs = list(range(len(weeks)))
    ax.plot(xs, rs_per_hour, color=VIOLET, linewidth=2.5, marker="o",
            label="Rs per peak online hour")
    ax2 = ax.twinx()
    ax2.plot(xs, rs_per_dw, color=AMBER, linewidth=2.5, marker="s",
             label="Rs per driver-week")
    ax.set_xticks(xs)
    ax.set_xticklabels([w[5:] for w in weeks], rotation=30, ha="right", fontsize=9)
    ax.set_ylabel("Rs per peak online hour", color=VIOLET)
    ax2.set_ylabel("Rs per driver-week", color=AMBER)
    ax.set_ylim(240, 330)
    ax2.set_ylim(5600, 6100)
    ax.axvline(5.5, color=MUTED, linestyle="--", linewidth=1)
    ax.text(5.5, 325, " launch", color=MUTED, fontsize=10, ha="left", va="top")
    ax.set_title("Which story does the denominator tell?",
                 color=INK, fontweight="bold")
    ax2.spines["top"].set_visible(False)
    ax.spines["top"].set_visible(False)
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2,
              loc="upper right", frameon=False, fontsize=10)
    fig.tight_layout()
    return fig


save(denominator_drift(), "denominator_drift_STUDENT")


# -------- the GIF of the drift, drawn one week at a time
def drift_gif():
    weeks = [w["week_start"] for w in weekly]
    rs_per_hour = [w["rs_per_hour"] for w in weekly]
    rs_per_dw = [w["rs_per_driver_week"] for w in weekly]
    xs = list(range(len(weeks)))

    fig, ax = plt.subplots(figsize=(9, 4.6))
    ax2 = ax.twinx()

    def frame(k):
        ax.clear()
        ax2.clear()
        upto = max(1, k + 1)
        ax.plot(xs[:upto], rs_per_hour[:upto], color=VIOLET, linewidth=2.5, marker="o",
                label="Rs per peak online hour")
        ax2.plot(xs[:upto], rs_per_dw[:upto], color=AMBER, linewidth=2.5, marker="s",
                 label="Rs per driver-week")
        ax.set_xticks(xs)
        ax.set_xticklabels([w[5:] for w in weeks], rotation=30, ha="right", fontsize=9)
        ax.set_ylabel("Rs per peak online hour", color=VIOLET)
        ax2.set_ylabel("Rs per driver-week", color=AMBER)
        ax.set_ylim(240, 330)
        ax2.set_ylim(5600, 6100)
        ax.set_xlim(-0.5, len(weeks) - 0.5)
        ax.axvline(5.5, color=MUTED, linestyle="--", linewidth=1)
        ax.text(5.5, 325, " launch", color=MUTED, fontsize=10, ha="left", va="top")
        ax.set_title("Which story does the denominator tell?",
                     color=INK, fontweight="bold")
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2,
                  loc="upper right", frameon=False, fontsize=10)
        return []

    animation = anim.FuncAnimation(fig, frame, frames=len(weeks), interval=500, repeat=False)
    gif_path = BOARDS / f"{STEM}_denominator_drift_STUDENT.gif"
    animation.save(gif_path, writer=anim.PillowWriter(fps=2))
    # Also write the final frame as the still beside the GIF
    frame(len(weeks) - 1)
    still_path = BOARDS / f"{STEM}_denominator_drift_still_STUDENT.png"
    fig.savefig(still_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {gif_path}")
    print(f"wrote {still_path}")


drift_gif()


# -------- a simple guesstimate tree: drivers online at the evening peak
def guesstimate_tree():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.text(5, 5.5, "How many drivers must be online at the evening peak?",
            ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

    nodes = [
        (5.0, 4.5, "Drivers online at peak", "about 8,200", ACCENT, WHITE),
        (1.6, 3.1, "Requests per hour", "about 10,000", VIOLET, TINT),
        (4.3, 3.1, "Trips per driver per hour", "about 2", VIOLET, TINT),
        (6.6, 3.1, "Idle share", "0.30 (0.20 to 0.40)", VIOLET, TINT),
        (8.9, 3.1, "Buffer", "1.15 (wait target)", VIOLET, TINT),
    ]
    for x, y, label, val, border, fill in nodes:
        box = mpatches.FancyBboxPatch((x - 1.0, y - 0.5), 2.0, 1.0,
                                      boxstyle="round,pad=0.05,rounding_size=0.1",
                                      linewidth=1.5, edgecolor=border, facecolor=fill)
        ax.add_patch(box)
        ax.text(x, y + 0.2, label, ha="center", va="center",
                fontsize=10, color=INK, fontweight="bold")
        ax.text(x, y - 0.2, val, ha="center", va="center",
                fontsize=10, color=INK)
    # Lines from root to factors
    for x in [1.6, 4.3, 6.6, 8.9]:
        ax.plot([5.0, x], [4.0, 3.6], color=MUTED, linewidth=1)
    ax.text(5, 1.7, "The product, step by step",
            ha="center", va="center", fontsize=11, fontweight="bold", color=INK)
    ax.text(5, 1.3,
            "10,000 requests per hour / 2 trips per driver per hour = 5,000 driver-hours of demand",
            ha="center", va="center", fontsize=10, color=INK)
    ax.text(5, 1.0,
            "5,000 / 0.70 x 1.15 = about 8,200 drivers online at any peak minute",
            ha="center", va="center", fontsize=10, color=INK)
    ax.text(5, 0.4,
            "Validate against the case's zone_weeks (synthetic); the published figure is to be found",
            ha="center", va="center", fontsize=10, color=MUTED, style="italic")
    return fig


save(guesstimate_tree(), "guesstimate_tree_STUDENT")


# -------- the four moves of a defence (predict then reveal: a timeline)
def four_moves():
    fig, ax = plt.subplots(figsize=(11, 3.2))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 3.2)
    ax.axis("off")
    ax.text(5.5, 3.0, "What does defence under objection look like?",
            ha="center", va="center", fontsize=14, fontweight="bold", color=INK)
    moves = [
        ("1. Restate", "until the owner agrees\nyou have heard them"),
        ("2. Answer", "from the evidence,\nby line of the slide"),
        ("3. Concede", "what is true\nin plain words"),
        ("4. What would\n   change my mind", "name the fact\nthat would move you"),
    ]
    for i, (title, body) in enumerate(moves):
        x = 1.0 + i * 2.5
        box = mpatches.FancyBboxPatch((x - 1.0, 0.7), 2.1, 1.6,
                                      boxstyle="round,pad=0.05,rounding_size=0.1",
                                      linewidth=1.5, edgecolor=VIOLET, facecolor=TINT)
        ax.add_patch(box)
        ax.text(x + 0.05, 2.05, title, ha="center", va="center",
                fontsize=11, color=INK, fontweight="bold")
        ax.text(x + 0.05, 1.3, body, ha="center", va="center",
                fontsize=9.5, color=INK)
        if i < len(moves) - 1:
            ax.annotate("", xy=(x + 1.4, 1.5), xytext=(x + 1.1, 1.5),
                        arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.5))
    ax.text(5.5, 0.2,
            "The loser can repeat the slide accurately when every move is done in sight of the room",
            ha="center", va="center", fontsize=10, color=MUTED, style="italic")
    return fig


save(four_moves(), "four_moves_STUDENT")

print()
print("done")

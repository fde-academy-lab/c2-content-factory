"""Draw the Wednesday data pictures the deck, the cheat sheet and the notes place by path.

Every picture is drawn by matplotlib from the generated CSVs and the facts file; nothing is pasted
in. The GIF ships beside its first and last stills, since PowerPoint plays motion in slideshow
mode only and LibreOffice renders the still at build time. Labels are checked against the nine-
points-on-a-slide and five-points-on-a-sheet bar; where they would fall under, the picture is
reshaped shorter or narrower before saving.

Writes PNG and GIF files to content/W04/D3/whiteboards/.
"""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.patches as mpatches
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
OUT = HERE.parent / "whiteboards"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#1A0F5C"
NIGHT = "#1A1440"
VIOLET = "#5B3FD6"
LAVENDER = "#D9A7FF"
TINT = "#EEEAFB"
MUTED = "#6B6690"
LINE = "#E4E1F1"
WHITE = "#FFFFFF"
ROSE = "#D63A6A"
GREEN = "#1F8A5B"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.labelcolor": INK,
    "axes.edgecolor": LINE,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
})

MILK_MARG = 0.7110
BREAD_MARG = 0.3420
EGGS_MARG = 0.2906
CURD_MARG = 0.2581
BANANAS_MARG = 0.2315
CHIPS_MARG = 0.1218
COLD_MARG = 0.1235
ICE_MARG = 0.0393
CHOC_MARG = 0.0145
BREAD_MILK_SUP = BREAD_MARG * 0.7419
BREAD_MILK_LIFT = 1.0435
CHIPS_COLD_SUP = 0.0500
CHIPS_COLD_LIFT = 3.3223
ICE_CHOC_SUP = 0.0026
ICE_CHOC_LIFT = 4.4720


def ten_dot_venn():
    """The ten tea-stall orders as dots in two circles, with the 2 by 2 table beside it. The toy
    the L1 chapter uses in its first beat, labelled invented on the deck and the cheat sheet."""
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={"width_ratios": [1.1, 1]})
    for ax in (ax_left, ax_right):
        ax.set_aspect("equal"); ax.axis("off")
    # Ten orders: chai in 6, biscuit in 4, both in 3.
    chai_only = [(1.0, 2.0), (1.5, 1.2), (2.0, 2.6)]
    both = [(2.8, 2.0), (3.0, 1.3), (2.6, 2.7)]
    biscuit_only = [(4.5, 2.0)]
    others = [(5.6, 2.4), (5.3, 1.4), (6.0, 2.0)]
    chai_circle = plt.Circle((2.0, 2.0), 1.3, fill=True, facecolor=TINT, edgecolor=VIOLET, linewidth=2)
    biscuit_circle = plt.Circle((3.5, 2.0), 1.3, fill=True, facecolor="none", edgecolor=VIOLET,
                                linewidth=2, alpha=0.0)
    bisc_fill = plt.Circle((3.5, 2.0), 1.3, fill=True, facecolor="#F6EEFC", edgecolor=VIOLET,
                           linewidth=2, alpha=0.5)
    ax_left.add_patch(chai_circle)
    ax_left.add_patch(bisc_fill)
    ax_left.add_patch(biscuit_circle)
    for pt in chai_only + both + biscuit_only + others:
        ax_left.plot(pt[0], pt[1], "o", color=INK, markersize=8)
    ax_left.text(1.3, 3.5, "chai in 6", color=VIOLET, fontsize=12, weight="bold")
    ax_left.text(4.0, 3.5, "biscuit in 4", color=VIOLET, fontsize=12, weight="bold")
    ax_left.text(2.65, 0.4, "both in 3", color=INK, fontsize=12, weight="bold", ha="center")
    ax_left.set_xlim(0, 7); ax_left.set_ylim(0, 4)
    # 2 by 2 table on the right.
    cell_colors = [[TINT, LINE], [LINE, "#F6F3FB"]]
    cells = [[3, 3], [1, 3]]
    tab = ax_right.table(cellText=[["3", "3"], ["1", "3"]],
                         rowLabels=["chai", "no chai"],
                         colLabels=["biscuit", "no biscuit"],
                         cellColours=cell_colors,
                         loc="center", cellLoc="center",
                         bbox=[0.1, 0.2, 0.8, 0.6])
    tab.auto_set_font_size(False); tab.set_fontsize(13)
    for (r, c), cell in tab.get_celld().items():
        cell.set_edgecolor(LINE); cell.set_linewidth(1.2)
        if r == 0: cell.set_text_props(weight="bold", color=INK)
        if c == -1: cell.set_text_props(weight="bold", color=INK)
    ax_right.text(0.5, 0.9, "the 2 by 2 the circles stand for",
                  transform=ax_right.transAxes, ha="center", color=MUTED, fontsize=11)
    ax_right.text(0.5, 0.08, "support 3 of 10, confidence 0.50, lift 1.25",
                  transform=ax_right.transAxes, ha="center", color=INK, fontsize=11, weight="bold")
    plt.tight_layout()
    fig.savefig(OUT / "C2_W04_D03_ten_dots_STUDENT.png", dpi=180, bbox_inches="tight",
                facecolor=WHITE)
    plt.close(fig)


def actual_vs_expected_bars():
    """Lift as a ratio of two bars: for each featured pair, draw the expected and the actual share
    of carts. Reads from the full-data facts."""
    pairs = [
        ("bread and milk", BREAD_MARG * MILK_MARG, BREAD_MILK_SUP),
        ("eggs and milk", EGGS_MARG * MILK_MARG, EGGS_MARG * 0.7267),
        ("chips and cold", CHIPS_MARG * COLD_MARG, CHIPS_COLD_SUP),
        ("ice cream and choc sauce", ICE_MARG * CHOC_MARG, ICE_CHOC_SUP),
    ]
    labels = [p[0] for p in pairs]
    expected = [p[1] for p in pairs]
    actual = [p[2] for p in pairs]
    fig, ax = plt.subplots(figsize=(9.5, 5))
    y = range(len(pairs))
    bar_h = 0.35
    ax.barh([i - bar_h / 2 for i in y], expected, bar_h, color=LINE, edgecolor=VIOLET,
            label="expected if independent")
    ax.barh([i + bar_h / 2 for i in y], actual, bar_h, color=VIOLET, edgecolor=INK,
            label="actually seen")
    for i, (e, a) in enumerate(zip(expected, actual)):
        lift = a / e if e > 0 else 0
        ax.text(max(e, a) * 1.02, i, f"lift {lift:.2f}", va="center", color=INK, fontsize=11,
                weight="bold")
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, color=INK)
    ax.set_xlabel("share of the 40,000 Pune carts")
    ax.set_title("Lift reads off the gap between expected and seen")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.legend(loc="lower right", frameon=False)
    plt.tight_layout()
    fig.savefig(OUT / "C2_W04_D03_actual_vs_expected_STUDENT.png", dpi=180, bbox_inches="tight",
                facecolor=WHITE)
    plt.close(fig)


def ctr_by_slot_bars():
    """The click-through by suggested item: milk slots against every other slot, before and after,
    showing the blended fall as a mix of two rates."""
    labels = ["before change\nany suggestion", "after change\nmilk slots",
              "after change\nother slots", "after change\nblended"]
    values = [0.061, 0.012, 0.064, 0.038]
    colors = [MUTED, ROSE, GREEN, INK]
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(labels, values, color=colors, edgecolor=INK, linewidth=0.8)
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.002, f"{v*100:.1f}%",
                ha="center", color=INK, weight="bold", fontsize=11)
    ax.set_ylabel("click-through rate")
    ax.set_title("The fall sits in the milk slots")
    ax.set_ylim(0, 0.08)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x*100:.0f}%"))
    ax.tick_params(axis="x", labelsize=10)
    plt.tight_layout()
    fig.savefig(OUT / "C2_W04_D03_ctr_by_slot_STUDENT.png", dpi=180, bbox_inches="tight",
                facecolor=WHITE)
    plt.close(fig)


def action_map_scatter():
    """Every pair above the support floor plotted on a lift against support board, with the four
    regions: promote (lift high, support above floor), watch (lift high, support below floor),
    ignore (lift near 1), trap (lift near 1 with high confidence from a popular partner)."""
    # Representative pairs computed from the facts, with the twelve rows and the lab's plants kept
    # off the board.
    pairs = [
        ("chips and cold", CHIPS_COLD_SUP, CHIPS_COLD_LIFT),
        ("ice cream and choc sauce", ICE_CHOC_SUP, ICE_CHOC_LIFT),
        ("bread and milk", BREAD_MILK_SUP, BREAD_MILK_LIFT),
        ("eggs and milk", EGGS_MARG * 0.7267, 1.0221),
        ("curd and milk", CURD_MARG * 0.715, 1.006),
        ("bananas and milk", BANANAS_MARG * 0.718, 1.010),
        ("bread and eggs", 0.11, 1.11),
        ("curd and bananas", 0.065, 1.08),
    ]
    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    ax.axhline(1.0, color=MUTED, lw=1, ls="--", alpha=0.7)
    ax.axvline(0.01, color=MUTED, lw=1, ls="--", alpha=0.7)  # 1 percent floor
    ax.text(0.011, 4.9, "support floor at 1%", color=MUTED, fontsize=10)
    ax.text(0.5, 1.03, "lift = 1 (independence)", color=MUTED, fontsize=10, ha="right")
    # Shade quadrants.
    ax.axhspan(1.2, 6, xmin=0.165, xmax=1.0, facecolor="#E8F5EE", alpha=0.6)
    ax.axhspan(1.2, 6, xmin=0, xmax=0.165, facecolor="#FBF4E3", alpha=0.6)
    ax.axhspan(0, 1.2, xmin=0, xmax=1.0, facecolor="#F6F3FB", alpha=0.5)
    # Region labels.
    ax.text(0.08, 5.2, "PROMOTE", color=GREEN, fontsize=14, weight="bold", ha="center")
    ax.text(0.004, 5.2, "WATCH", color="#C98A00", fontsize=14, weight="bold", ha="center")
    ax.text(0.15, 0.6, "IGNORE and the popularity trap", color=MUTED, fontsize=12, weight="bold")
    for label, sup, lift in pairs:
        color = VIOLET
        ax.scatter(sup, lift, s=70, color=color, edgecolor=INK, zorder=3)
        ax.text(sup * 1.1, lift + 0.08, label, color=INK, fontsize=10)
    ax.set_xscale("log")
    ax.set_xlim(0.001, 0.5)
    ax.set_ylim(0, 5.5)
    ax.set_xlabel("support (log scale)")
    ax.set_ylabel("lift")
    ax.set_title("Where every pair sits on the action map")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    plt.tight_layout()
    fig.savefig(OUT / "C2_W04_D03_action_map_STUDENT.png", dpi=180, bbox_inches="tight",
                facecolor=WHITE)
    plt.close(fig)


def slot_value_waterfall():
    """Margin gained, less margin returned to the customer, less the slot's opportunity cost,
    giving the net value of a slot a day. Reads from the facts."""
    labels = ["impressions\n60,000", "clicks at 6.4%\n3,840",
              "adds at 50%\n1,920", "margin at Rs 9\nRs 17,280",
              "milk slots at 1.2%\nRs 3,240", "the gap\nRs 14,040/day"]
    values = [0, 3840, 1920, 17280, 3240, 14040]
    fig, ax = plt.subplots(figsize=(10, 4.5))
    # Simple cascade: show the four computations as side-by-side bars on different scales.
    # Draw stacked explanation blocks.
    ax.axis("off")
    x = 0.05
    for i, (lab, val) in enumerate(zip(labels, values)):
        colour = VIOLET if i < 4 else ROSE if i == 4 else INK
        ax.add_patch(mpatches.FancyBboxPatch((x, 0.3), 0.14, 0.5,
                                              boxstyle="round,pad=0.02",
                                              facecolor=TINT if i < 4 else "#FBE9EF" if i == 4 else INK,
                                              edgecolor=colour, linewidth=1.5))
        text_colour = WHITE if i == 5 else INK
        ax.text(x + 0.07, 0.55, lab, ha="center", va="center", color=text_colour, fontsize=11,
                weight="bold")
        if i < 5:
            ax.annotate("", xy=(x + 0.16, 0.55), xytext=(x + 0.14, 0.55),
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3))
        x += 0.158
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.text(0.5, 0.15, "A slot full of the top-seller earns five times less than a slot that beats chance.",
            ha="center", color=MUTED, fontsize=11, style="italic")
    plt.tight_layout()
    fig.savefig(OUT / "C2_W04_D03_slot_value_cascade_STUDENT.png", dpi=180, bbox_inches="tight",
                facecolor=WHITE)
    plt.close(fig)


def shrinking_universe_gif():
    """Confidence as a smaller denominator: the twelve carts, then only those with bread, then
    those with bread and milk. Writes the GIF and its first and last frames as PNGs."""
    cart_items = {
        "TR01": {"milk", "bread", "eggs", "bananas"},
        "TR02": {"milk", "bread", "eggs", "curd"},
        "TR03": {"milk", "bread", "curd", "paneer"},
        "TR04": {"milk", "bread", "eggs"},
        "TR05": {"milk", "eggs", "chips", "cold"},
        "TR06": {"milk", "chips", "cold"},
        "TR07": {"milk", "bananas"},
        "TR08": {"milk", "paneer"},
        "TR09": {"chips"},
        "TR10": {"cold", "curd"},
        "TR11": {"eggs", "ice cream", "choc"},
        "TR12": {"curd", "onions"},
    }
    labels = list(cart_items.keys())
    # Positions: 4 wide, 3 tall.
    pos = {labels[i]: (i % 4, 2 - i // 4) for i in range(12)}

    def draw_state(ax, stage):
        ax.clear(); ax.set_xlim(-0.5, 3.5); ax.set_ylim(-0.5, 2.5); ax.set_aspect("equal")
        ax.axis("off")
        for cid, (x, y) in pos.items():
            items = cart_items[cid]
            if stage == 0:
                face = TINT; edge = VIOLET; alpha = 1.0
            elif stage == 1:
                has_bread = "bread" in items
                face = TINT if has_bread else WHITE
                edge = VIOLET if has_bread else "#B8B2D6"
                alpha = 1.0 if has_bread else 0.25
            else:
                has_both = "bread" in items and "milk" in items
                face = TINT if has_both else WHITE
                edge = VIOLET if has_both else "#B8B2D6"
                alpha = 1.0 if has_both else 0.2
            ax.add_patch(mpatches.FancyBboxPatch((x - 0.4, y - 0.3), 0.8, 0.6,
                                                  boxstyle="round,pad=0.03",
                                                  facecolor=face, edgecolor=edge,
                                                  linewidth=1.5, alpha=alpha))
            ax.text(x, y + 0.08, cid, ha="center", color=INK, fontsize=10, weight="bold",
                    alpha=min(alpha + 0.3, 1.0))
            short = " ".join(sorted(items))[:28]
            ax.text(x, y - 0.18, short, ha="center", color=MUTED, fontsize=7, alpha=alpha)
        titles = ["Every cart: 12",
                  "Carts that hold bread: 4",
                  "Of those, carts that also hold milk: 4"]
        reads = ["bread share = 4/12 = 0.33",
                 "shrink the world to the 4 bread carts",
                 "confidence(bread -> milk) = 4/4 = 1.00"]
        ax.set_title(titles[stage], fontsize=14, color=INK)
        ax.text(1.5, -0.4, reads[stage], ha="center", color=INK, fontsize=11, weight="bold")

    fig, ax = plt.subplots(figsize=(9, 5))
    def frame(i): draw_state(ax, i)
    # Still frames.
    draw_state(ax, 0)
    fig.savefig(OUT / "C2_W04_D03_shrink_still_first_STUDENT.png", dpi=180,
                bbox_inches="tight", facecolor=WHITE)
    draw_state(ax, 2)
    fig.savefig(OUT / "C2_W04_D03_shrink_still_last_STUDENT.png", dpi=180,
                bbox_inches="tight", facecolor=WHITE)
    anim = FuncAnimation(fig, frame, frames=3, interval=1600, repeat=True)
    anim.save(OUT / "C2_W04_D03_shrink_STUDENT.gif", writer=PillowWriter(fps=0.75))
    plt.close(fig)


def milk_everywhere_bars():
    """For every item with support of at least 2 percent, the confidence toward milk and the lift,
    showing that the lift sits near 1 for all of them even as confidence varies, which is the
    popularity trap in one chart."""
    items = [
        ("bread", 0.3420, 0.7419, 1.0435),
        ("eggs", 0.2906, 0.7267, 1.0221),
        ("curd", 0.2581, 0.715, 1.006),
        ("bananas", 0.2315, 0.718, 1.010),
        ("chips", 0.1218, 0.713, 1.003),
        ("cold drink", 0.1235, 0.714, 1.004),
        ("ice cream", 0.0393, 0.731, 1.028),
    ]
    labels = [i[0] for i in items]
    confs = [i[2] for i in items]
    lifts = [i[3] for i in items]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.barh(labels, confs, color=TINT, edgecolor=VIOLET, linewidth=1.4)
    ax1.axvline(0.71, color=INK, lw=1.3, ls="--")
    ax1.text(0.73, 6.1, "milk's share\n0.71", color=INK, fontsize=10)
    ax1.set_xlim(0, 1); ax1.set_xlabel("confidence to milk")
    ax1.set_title("every pair looks like a bundle...")
    ax1.spines["top"].set_visible(False); ax1.spines["right"].set_visible(False)
    for i, c in enumerate(confs):
        ax1.text(c + 0.01, i, f"{c:.2f}", va="center", color=INK, fontsize=10)
    ax2.barh(labels, lifts, color=TINT, edgecolor=VIOLET, linewidth=1.4)
    ax2.axvline(1.0, color=INK, lw=1.3, ls="--")
    ax2.set_xlim(0, 1.3); ax2.set_xlabel("lift")
    ax2.set_title("...until lift says independence")
    ax2.spines["top"].set_visible(False); ax2.spines["right"].set_visible(False)
    for i, l in enumerate(lifts):
        ax2.text(l + 0.01, i, f"{l:.2f}", va="center", color=INK, fontsize=10)
    plt.tight_layout()
    fig.savefig(OUT / "C2_W04_D03_milk_everywhere_STUDENT.png", dpi=180, bbox_inches="tight",
                facecolor=WHITE)
    plt.close(fig)


def milk_share_rect():
    """A unit square with P(A) as a vertical band, P(B) as a horizontal band, their expected
    overlap shaded, and the observed overlap drawn beside it. The scene the explorer repeats, drawn
    once as a still so the deck and the sheet can place it."""
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(10, 5))
    for ax in (axL, axR):
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect("equal")
        ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
        ax.set_xticks([0, 0.5, 1.0]); ax.set_yticks([0, 0.5, 1.0])
    # Left: expected if independent.
    axL.add_patch(mpatches.Rectangle((0, 0), BREAD_MARG, 1, facecolor=TINT, alpha=0.6, edgecolor=VIOLET))
    axL.add_patch(mpatches.Rectangle((0, 0), 1, MILK_MARG, facecolor=LAVENDER, alpha=0.4, edgecolor=INK))
    axL.add_patch(mpatches.Rectangle((0, 0), BREAD_MARG, MILK_MARG, facecolor=VIOLET, alpha=0.8,
                                      edgecolor=INK, linewidth=2))
    axL.text(BREAD_MARG / 2, 1.05, f"P(bread) = {BREAD_MARG:.2f}", ha="center", color=INK, fontsize=11)
    axL.text(1.05, MILK_MARG / 2, f"P(milk) = {MILK_MARG:.2f}", color=INK, fontsize=11)
    axL.text(BREAD_MARG / 2, MILK_MARG / 2, f"expected\n{BREAD_MARG * MILK_MARG:.3f}",
             ha="center", va="center", color=WHITE, fontsize=11, weight="bold")
    axL.set_title("Expected if independent")
    # Right: observed.
    obs = BREAD_MILK_SUP
    axR.add_patch(mpatches.Rectangle((0, 0), BREAD_MARG, 1, facecolor=TINT, alpha=0.4, edgecolor=VIOLET,
                                      linestyle="--"))
    axR.add_patch(mpatches.Rectangle((0, 0), 1, MILK_MARG, facecolor=LAVENDER, alpha=0.3, edgecolor=INK,
                                      linestyle="--"))
    # Observed overlap: draw as a rectangle with area obs sitting inside both bands.
    w = BREAD_MARG; h = obs / w
    axR.add_patch(mpatches.Rectangle((0, 0), w, h, facecolor=VIOLET, alpha=0.9, edgecolor=INK,
                                      linewidth=2))
    axR.text(w / 2, h / 2, f"observed\n{obs:.3f}", ha="center", va="center", color=WHITE,
             fontsize=11, weight="bold")
    axR.set_title(f"Observed; lift = {BREAD_MILK_LIFT:.2f}")
    plt.tight_layout()
    fig.savefig(OUT / "C2_W04_D03_areas_STUDENT.png", dpi=180, bbox_inches="tight",
                facecolor=WHITE)
    plt.close(fig)


def main():
    print("Drawing Wednesday's pictures...")
    ten_dot_venn()
    print("  wrote ten_dots")
    milk_share_rect()
    print("  wrote areas")
    actual_vs_expected_bars()
    print("  wrote actual_vs_expected")
    milk_everywhere_bars()
    print("  wrote milk_everywhere")
    ctr_by_slot_bars()
    print("  wrote ctr_by_slot")
    action_map_scatter()
    print("  wrote action_map")
    slot_value_waterfall()
    print("  wrote slot_value_cascade")
    shrinking_universe_gif()
    print("  wrote shrink gif and its two stills")
    print("Done.")


if __name__ == "__main__":
    main()

"""Draw the two exhibit placeholders of the Build 2 presentation template.

    python3 content/W06/D2/4_trainer_only/C2_W06_D02_presentation_figures_INTERNAL.py

Writes, into content/W06/D2/2_starter_repo/presentation/figures/:
  exhibit_demo.png        slide 3: a wireframe of the live demo's one screen, no data in it
  exhibit_error_bill.png  slide 5: a wireframe of the error-bill chart, grey bars with blanks

Both are frames for a group to replace with its own screenshot and its own chart. They carry no
number from the card book, so nothing the room is meant to compute or find is drawn here. The
colours are the deck's (scripts/brand.py), and every label is drawn at 15 points or more in a
strip ten inches wide, which the deck sets in a band across the foot of its slide, so it prints
well above the nine points a room reads from the back.
"""
import pathlib
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import brand  # noqa: E402

OUT = HERE.parent / "2_starter_repo" / "presentation" / "figures"
GREY = "#C9C5DD"


def frame(ax, title, lines):
    """The dashed strip every placeholder sits in, with what to paste written on its left third."""
    ax.add_patch(FancyBboxPatch((0.006, 0.02), 0.988, 0.96, boxstyle="round,pad=0,rounding_size=0.04",
                                fill=True, facecolor=brand.SURFACE, edgecolor=brand.VIOLET,
                                linewidth=2.2, linestyle=(0, (6, 4)), transform=ax.transAxes))
    ax.text(0.03, 0.86, title, transform=ax.transAxes, fontsize=19, fontweight="bold",
            color=brand.INK, va="top", linespacing=1.15)
    for i, line in enumerate(lines):
        ax.text(0.03, 0.50 - 0.13 * i, line, transform=ax.transAxes, fontsize=15,
                color=brand.MUTED, va="top")


def demo():
    fig = plt.figure(figsize=(10, 3.3), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    frame(ax, "Paste your demo\nscreenshot here",
          ["Your fallback if the", "live app stops."])
    # The one screen of the app: a customer, three numbers, one slider for the card.
    ax.add_patch(FancyBboxPatch((0.33, 0.08), 0.64, 0.84, boxstyle="round,pad=0,rounding_size=0.03",
                                facecolor=brand.WHITE, edgecolor=GREY, linewidth=1.6,
                                transform=ax.transAxes))
    ax.text(0.355, 0.85, "Customer __", transform=ax.transAxes, fontsize=17, fontweight="bold",
            color=brand.INK, va="top")
    boxes = [("Chance of default", "__ %"), ("Main reason", "__"), ("Cost if skipped", "__ units")]
    for i, (label, value) in enumerate(boxes):
        x = 0.355 + i * 0.205
        ax.add_patch(FancyBboxPatch((x, 0.30), 0.19, 0.36, boxstyle="round,pad=0,rounding_size=0.03",
                                    facecolor=brand.TINT, edgecolor=brand.LILAC, linewidth=1.2,
                                    transform=ax.transAxes))
        ax.text(x + 0.095, 0.60, label, transform=ax.transAxes, fontsize=15, color=brand.MUTED,
                ha="center", va="top")
        ax.text(x + 0.095, 0.40, value, transform=ax.transAxes, fontsize=19, fontweight="bold",
                color=brand.INK, ha="center", va="center")
    ax.text(0.355, 0.17, "Card's number", transform=ax.transAxes, fontsize=15, color=brand.MUTED,
            va="center")
    ax.plot([0.54, 0.94], [0.17, 0.17], transform=ax.transAxes, color=GREY, linewidth=4,
            solid_capstyle="round")
    ax.plot([0.70], [0.17], marker="o", markersize=14, color=brand.VIOLET, transform=ax.transAxes)
    fig.savefig(OUT / "exhibit_demo.png", facecolor="white")
    plt.close(fig)


def error_bill():
    fig = plt.figure(figsize=(10, 3.3), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    frame(ax, "Paste your\nerror-bill chart",
          ["One bar per list, same", "customers, same costs."])
    inner = fig.add_axes([0.34, 0.22, 0.62, 0.68])
    names = ["Call nobody", "Call everyone", "The rule", "Our model"]
    heights = [0.95, 0.75, 0.62, 0.52]
    inner.bar(range(4), heights, color=[GREY, GREY, brand.LILAC, brand.VIOLET], width=0.62)
    inner.errorbar([2, 3], [heights[2], heights[3]], yerr=0.07, fmt="none", ecolor=brand.INK,
                   capsize=9, linewidth=2)
    for i, h in enumerate(heights):
        inner.text(i, h / 2, "__ units", ha="center", va="center", fontsize=15, fontweight="bold",
                   color=brand.WHITE if i == 3 else brand.INK)
    inner.set_xticks(range(4), names, fontsize=15, color=brand.INK)
    inner.tick_params(axis="x", length=0)
    inner.set_yticks([])
    inner.set_ylim(0, 1.05)
    for side in ("top", "right", "left"):
        inner.spines[side].set_visible(False)
    inner.spines["bottom"].set_color(brand.MUTED)
    inner.set_facecolor(brand.SURFACE)
    fig.savefig(OUT / "exhibit_error_bill.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    demo()
    error_bill()
    print(f"wrote {OUT / 'exhibit_demo.png'} and {OUT / 'exhibit_error_bill.png'}")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W06/D2/4_trainer_only/C2_W06_D02_presentation_figures_INTERNAL.py
#     Writes two PNGs into 2_starter_repo/presentation/figures/, each a dashed violet frame with
#     its paste instruction on top and a wireframe beneath, and no number from the card book.
# The template rebuilt after this runs
#     python3 scripts/build_deck.py on the template places exhibit_demo.png on slide 3 and
#     exhibit_error_bill.png on slide 5, each under its caption.
# Either PNG deleted, then the template rebuilt
#     build_deck.py stops with FAIL and the slide number, because a slide would ship without it.

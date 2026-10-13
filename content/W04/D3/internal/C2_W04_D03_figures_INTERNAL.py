"""Draw the Wednesday pictures the decks, the cheat sheet and the notes place by path.

Run from the repository root, after the generator:
    python3 content/W04/D3/internal/C2_W04_D03_figures_INTERNAL.py

Every picture is drawn by matplotlib from the generated CSVs and the facts file, so a number on a
picture is a number in the facts file. The GIF ships beside its first and last stills. Labels are
set at 12 points or more on pictures a slide shows at about full width, so they print above nine
points on a slide; the cheat sheet's anchor is drawn at the sheet's own width.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import pandas as pd
import yaml

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
OUT = HERE.parent / "whiteboards"
OUT.mkdir(parents=True, exist_ok=True)
FACTS = {r["id"]: r for rows in yaml.safe_load((HERE / "C2_W04_D03_facts_INTERNAL.yaml")
                                                .read_text(encoding="utf-8")).values()
         for r in rows}


def v(fid):
    return FACTS[fid]["value"]


def s(fid):
    return FACTS[fid]["shown"]


INK, VIOLET, TINT, MUTED, LINE = "#1A0F5C", "#5B3FD6", "#EEEAFB", "#6B6690", "#E4E1F1"
ROSE, GREEN, AMBER, WHITE, LAV = "#D63A6A", "#1F8A5B", "#C98A00", "#FFFFFF", "#D9A7FF"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13, "axes.titlesize": 15, "axes.labelsize": 13,
    "xtick.labelsize": 12, "ytick.labelsize": 12, "legend.fontsize": 12,
    "axes.labelcolor": INK, "axes.edgecolor": "#B8B2D6", "axes.titleweight": "bold",
    "axes.titlecolor": INK, "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
})


def save(fig, name):
    fig.savefig(OUT / name, dpi=170, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print("  wrote", name)


def baskets():
    items = pd.read_csv(DATA / "C2_W04_D03_cart_items_STUDENT.csv")
    return items, items.groupby("cart_id").item.apply(set)


# =========================================================================== SECTIONs 1 to 6 and 9
# The concept chapters' pictures, drawn from the invented tables the generator writes: the hostel
# canteen's twelve lunch orders, its 600-order month and Sharma Kirana's month. Every picture says
# "invented" in its title or its foot, as every slide and cell that places it does.
def canteen():
    lines = pd.read_csv(DATA / "C2_W04_D03_canteen_order_lines_STUDENT.csv")
    return [(oid, set(g)) for oid, g in lines.groupby("order_id").item]


def measures(orders, a, b):
    n = len(orders)
    na = sum(a in x for _, x in orders)
    nb = sum(b in x for _, x in orders)
    nab = sum(a in x and b in x for _, x in orders)
    exp = na * nb / n
    return {"na": na, "nb": nb, "nab": nab, "exp": exp, "lift": nab / exp,
            "ab": nab / na, "ba": nab / nb}


def all_pairs(orders):
    n = len(orders)
    single = Counter(x for _, b in orders for x in b)
    double = Counter(p for _, b in orders for p in combinations(sorted(b), 2))
    return pd.DataFrame([{"a": a, "b": c, "both": k, "support": k / n,
                          "ab": k / single[a], "ba": k / single[c],
                          "lift": k * n / (single[a] * single[c])} for (a, c), k in double.items()])


def canteen_dots(name, reads):
    """The twelve orders as dots in two circles, roti and sabzi, beside the 2 by 2 table of counts."""
    orders = canteen()
    fig, (ax, at) = plt.subplots(1, 2, figsize=(12.5, 4.8), gridspec_kw={"width_ratios": [1.25, 1]})
    for a in (ax, at):
        a.axis("off")
    ax.set_aspect("equal")
    ax.add_patch(plt.Circle((2.3, 2.1), 1.55, facecolor=TINT, edgecolor=VIOLET, lw=2.2))
    ax.add_patch(plt.Circle((4.1, 2.1), 1.55, facecolor="#F6EEFC", edgecolor=VIOLET, lw=2.2, alpha=0.75))
    spots = {"roti": [(1.45, 2.1)], "both": [(3.2, 2.85), (3.2, 2.1), (3.2, 1.35)],
             "sabzi": [(4.95, 2.1)],
             "neither": [(6.6, 3.4), (7.4, 3.4), (6.6, 2.6), (7.4, 2.6), (6.6, 1.8), (7.4, 1.8), (7.0, 1.0)]}
    used = {k: 0 for k in spots}
    for oid, b in orders:
        k = ("both" if {"roti", "sabzi"} <= b else "roti" if "roti" in b else
             "sabzi" if "sabzi" in b else "neither")
        x, y = spots[k][used[k]]
        used[k] += 1
        ax.plot(x, y, "o", color=INK, ms=13)
        ax.text(x, y - 0.38, oid, ha="center", fontsize=12, color=INK)
    ax.text(1.0, 3.95, f"roti: {v('toy_canteen_roti_orders')}", color=VIOLET, fontsize=15, weight="bold")
    ax.text(4.0, 3.95, f"sabzi: {v('toy_canteen_sabzi_orders')}", color=VIOLET, fontsize=15, weight="bold")
    ax.text(3.2, 0.15, f"both: {v('toy_canteen_roti_sabzi_both')}", color=INK, fontsize=15, weight="bold", ha="center")
    ax.text(7.0, 0.15, f"neither: {v('toy_canteen_neither')}", color=MUTED, fontsize=14, ha="center")
    ax.set_xlim(0.5, 7.9)
    ax.set_ylim(-0.1, 4.4)
    both, ro, so, ne = (v("toy_canteen_roti_sabzi_both"), v("toy_canteen_roti_only"),
                        v("toy_canteen_sabzi_only"), v("toy_canteen_neither"))
    tab = at.table(cellText=[[both, ro, both + ro], [so, ne, so + ne], [both + so, ro + ne, 12]],
                   rowLabels=["roti", "no roti", "all"], colLabels=["sabzi", "no sabzi", "all"],
                   cellColours=[[TINT, WHITE, "#F7F5FD"], [WHITE, WHITE, "#F7F5FD"],
                                ["#F7F5FD", "#F7F5FD", "#F7F5FD"]],
                   loc="center", cellLoc="center", bbox=[0.2, 0.28, 0.76, 0.58])
    tab.auto_set_font_size(False)
    tab.set_fontsize(15)
    for (r, c), cell in tab.get_celld().items():
        cell.set_edgecolor("#B8B2D6")
        if r == 0 or c == -1:
            cell.set_text_props(weight="bold", color=INK)
    at.text(0.58, 0.94, "twelve lunch orders, invented", transform=at.transAxes, ha="center",
            color=MUTED, fontsize=14)
    at.text(0.58, 0.1, reads, transform=at.transAxes, ha="center", color=INK, fontsize=15, weight="bold")
    fig.tight_layout()
    save(fig, name)


def canteen_pair_counts():
    """The six most common pairs by the orders they share, the pairs holding chaas edged red."""
    p = all_pairs(canteen()).sort_values(["both", "a"], ascending=[False, True]).head(6)
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    y = range(len(p))
    colors = [ROSE if "chaas" in (r.a, r.b) else VIOLET for r in p.itertuples()]
    ax.barh(list(y), p.both, color=[TINT if c == VIOLET else "#FBE3EA" for c in colors],
            edgecolor=colors, lw=2)
    for i, r in zip(y, p.itertuples()):
        ax.text(r.both + 0.1, i, f"{r.both} of 12 = {r.support:.2f}", va="center", fontsize=13,
                color=INK, weight="bold")
    ax.set_yticks(list(y), [f"{r.a} + {r.b}" for r in p.itertuples()])
    ax.invert_yaxis()
    ax.set_xlim(0, 9.4)
    ax.set_xticks([0, 2, 4, 6])
    ax.set_xlabel("orders holding both, of 12")
    ax.set_title("Six most common pairs;\nred edge: holds chaas", fontsize=13)
    fig.text(0.99, 0.01, "twelve lunch orders, invented", ha="right", fontsize=12, color=MUTED)
    fig.tight_layout()
    save(fig, "C2_W04_D03_canteen_pair_counts_STUDENT.png")

def card_grid(ax, orders, lit, dark, title, read):
    """Twelve order cards in three rows: `lit` orders outlined, `dark` orders filled."""
    ax.set_xlim(-0.55, 3.55)
    ax.set_ylim(-0.95, 2.6)
    ax.axis("off")
    for i, (oid, b) in enumerate(orders):
        x, y = i % 4, 2 - i // 4
        on, full = oid in lit, oid in dark
        ax.add_patch(mpatches.FancyBboxPatch((x - 0.44, y - 0.34), 0.88, 0.68, boxstyle="round,pad=0.02",
                                             lw=2 if on else 1.2,
                                             facecolor=VIOLET if full else (TINT if on else WHITE),
                                             edgecolor=VIOLET if on else "#D5D1E8"))
        ax.text(x, y, oid, ha="center", va="center", fontsize=15, weight="bold",
                color=WHITE if full else (INK if on else "#B8B2D6"))
    ax.set_title(title, fontsize=15)
    ax.text(1.5, -0.78, read, ha="center", fontsize=15, weight="bold", color=INK)


def canteen_two_ways():
    """Confidence from each side of dal rice and papad: the same three orders over 6 and over 5."""
    orders = canteen()
    dal = {o for o, b in orders if "dal rice" in b}
    pap = {o for o, b in orders if "papad" in b}
    both = dal & pap
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.8))
    card_grid(a1, orders, dal, both, f"From dal rice: its {len(dal)} orders",
              f"{len(both)} of {len(dal)} hold papad: {s('toy_canteen_dal_papad_conf_ab')}")
    card_grid(a2, orders, pap, both, f"From papad: its {len(pap)} orders",
              f"{len(both)} of {len(pap)} hold dal rice: {s('toy_canteen_dal_papad_conf_ba')}")
    fig.suptitle("The same three orders, two denominators (invented orders; filled: holds both)",
                 fontsize=15, weight="bold", color=INK)
    fig.tight_layout()
    save(fig, "C2_W04_D03_canteen_two_ways_STUDENT.png")


def canteen_shrink():
    """Confidence as a smaller world: twelve orders, then dal rice's six, then the three with papad."""
    orders = canteen()
    dal = {o for o, b in orders if "dal rice" in b}
    both = {o for o, b in orders if {"dal rice", "papad"} <= b}
    everyone = {o for o, _ in orders}
    stages = [(everyone, set(), "All twelve orders (invented)", "dal rice is in 6 of 12"),
              (dal, set(), "Keep only the orders with dal rice: 6", "confidence asks only about these 6"),
              (dal, both, "Of the 6, those that also hold papad: 3",
               f"confidence from dal rice to papad = 3 / 6 = {s('toy_canteen_dal_papad_conf_ab')}")]
    fig, ax = plt.subplots(figsize=(12.5, 5.0))

    def draw(i):
        ax.clear()
        lit, dark, title, read = stages[i]
        card_grid(ax, orders, lit, dark, title, read)

    draw(0)
    fig.savefig(OUT / "C2_W04_D03_canteen_shrink_still_first_STUDENT.png", dpi=170, bbox_inches="tight",
                facecolor=WHITE)
    draw(2)
    fig.savefig(OUT / "C2_W04_D03_canteen_shrink_still_last_STUDENT.png", dpi=170, bbox_inches="tight",
                facecolor=WHITE)
    anim = FuncAnimation(fig, draw, frames=3, interval=1800)
    anim.save(OUT / "C2_W04_D03_canteen_shrink_STUDENT.gif", writer=PillowWriter(fps=0.6))
    plt.close(fig)
    print("  wrote the canteen shrink GIF and its two stills")


def canteen_direction():
    """Confidence one way against the other for every pair of the twelve orders, with the diagonal."""
    p = all_pairs(canteen())
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.plot([0, 1.05], [0, 1.05], color=MUTED, ls="--", lw=1.2)
    ax.text(0.12, 0.2, "both ways equal", color=MUTED, fontsize=12, rotation=28)
    ax.scatter(p.ab, p.ba, s=80, color=VIOLET, edgecolor=INK, zorder=3)
    marks = {("curd", "gulab jamun"): ("curd to gulab\njamun 0.50,\nback 1.00", (1.08, 1.08)),
             ("roti", "sabzi"): ("roti and sabzi:\n0.75 both ways", (1.08, 0.62)),
             ("dal rice", "papad"): ("dal rice to\npapad 0.50,\nback 0.60", (1.08, 0.24))}
    for (a, b), (label, at) in marks.items():
        r = p[(p.a == a) & (p.b == b)].iloc[0]
        ax.annotate(label, (r.ab, r.ba), xytext=at, textcoords="data", fontsize=12, color=INK,
                    weight="bold", va="center",
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=1, shrinkA=2, shrinkB=6))
    ax.set_xlim(0, 1.75)
    ax.set_ylim(0, 1.25)
    ax.set_xticks([0, 0.5, 1])
    ax.set_xlabel("confidence one way")
    ax.set_ylabel("confidence back")
    ax.set_title("The 13 pairs, both directions", fontsize=14)
    fig.text(0.99, 0.01, "twelve lunch orders, invented", ha="right", fontsize=12, color=MUTED)
    fig.tight_layout()
    save(fig, "C2_W04_D03_canteen_direction_STUDENT.png")

def canteen_seen_expected():
    """Seen against expected for four pairs of the twelve orders: lift is the ratio of the two bars."""
    orders = canteen()
    pairs = [("roti", "sabzi"), ("dal rice", "papad"), ("roti", "chaas"), ("papad", "chaas")]
    fig, axes = plt.subplots(1, 4, figsize=(12.5, 4.6))
    for a, (x, y) in zip(axes, pairs):
        m = measures(orders, x, y)
        a.bar([0, 1], [m["exp"], m["nab"]], color=[LINE, VIOLET], edgecolor=INK, width=0.6)
        for xx, val in ((0, m["exp"]), (1, m["nab"])):
            a.text(xx, val + 0.08, f"{val:.2f}".rstrip("0").rstrip("."), ha="center", fontsize=14, color=INK)
        a.set_xticks([0, 1], ["chance", "seen"])
        a.set_yticks([])
        a.spines["left"].set_visible(False)
        a.set_ylim(0, 4.6)
        a.set_title(f"{x} + {y}\nlift {m['lift']:.2f}", fontsize=14)
    fig.suptitle("Orders holding both: what chance alone gives, against what the twelve show (invented)",
                 fontsize=15, weight="bold", color=INK)
    fig.tight_layout()
    save(fig, "C2_W04_D03_canteen_seen_expected_STUDENT.png")


def canteen_areas():
    """Lift as a ratio of two areas on the unit square, roti and sabzi."""
    pr, seen = 4 / 12, v("toy_canteen_roti_sabzi_support")
    fig, (al, ar) = plt.subplots(1, 2, figsize=(6.4, 4.4))
    for a in (al, ar):
        a.set_xlim(0, 1)
        a.set_ylim(0, 1)
        a.set_aspect("equal")
        a.set_xticks([0, 1 / 3, 1], ["0", "1/3", "1"])
        a.set_yticks([0, 1 / 3, 0.75, 1], ["0", "1/3", "0.75", "1"])
    al.add_patch(mpatches.Rectangle((0, 0), pr, 1, facecolor=TINT, edgecolor=VIOLET))
    al.add_patch(mpatches.Rectangle((0, 0), 1, pr, facecolor=LAV, alpha=0.35, edgecolor=INK))
    al.add_patch(mpatches.Rectangle((0, 0), pr, pr, facecolor=VIOLET, edgecolor=INK, lw=2))
    al.text(0.67, 0.7, "chance\n0.11 x 12\n= 1.33", ha="center", va="center", color=INK, fontsize=13,
            weight="bold")
    al.set_xlabel("roti: 4 of 12")
    al.set_ylabel("sabzi: 4 of 12")
    al.set_title("Ignoring\neach other", fontsize=12)
    ar.add_patch(mpatches.Rectangle((0, 0), pr, 1, facecolor=TINT, edgecolor=VIOLET, ls="--"))
    ar.add_patch(mpatches.Rectangle((0, 0), pr, seen / pr, facecolor=VIOLET, edgecolor=INK, lw=2))
    ar.add_patch(mpatches.Rectangle((0, 0), pr, pr, fill=False, edgecolor=ROSE, lw=2.4, ls="--"))
    ar.text(0.67, 0.7, "seen\n0.25 x 12\n= 3", ha="center", va="center", color=INK, fontsize=13,
            weight="bold")
    ar.set_xlabel("roti: 4 of 12")
    ar.set_ylabel("roti orders with sabzi")
    ar.set_title(f"Lift 3 / 1.33\n= {s('toy_canteen_roti_sabzi_lift')}", fontsize=12)
    fig.text(0.99, 0.01, "red dashes: chance; invented", ha="right", fontsize=12, color=MUTED)
    fig.tight_layout()
    save(fig, "C2_W04_D03_canteen_areas_STUDENT.png")

def chaas_partner():
    """Chaas in 9 of 12: confidence toward it reads like a bundle, lift with it sits near one."""
    orders = canteen()
    items = ["dal rice", "sabzi", "roti", "papad"]
    ms = [measures(orders, x, "chaas") for x in items]
    share = v("toy_canteen_chaas_share")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 4.4), sharey=True)
    y = range(len(items))
    a1.barh(list(y), [m["ab"] for m in ms], color=TINT, edgecolor=VIOLET, lw=2)
    a1.axvline(share, color=ROSE, ls="--", lw=2)
    a1.text(share + 0.01, 3.55, f"chaas in {share:.2f} of all orders", color=ROSE, fontsize=13)
    for i, m in zip(y, ms):
        a1.text(0.03, i, f"{m['ab']:.2f}", va="center", fontsize=14, color=INK, weight="bold")
    a1.set_yticks(list(y), items)
    a1.invert_yaxis()
    a1.set_xlim(0, 1.15)
    a1.set_xlabel("confidence toward chaas")
    a1.set_title("Every item looks bundled with chaas")
    a2.barh(list(y), [m["lift"] for m in ms], color=TINT, edgecolor=VIOLET, lw=2)
    a2.axvline(1, color=INK, ls="--", lw=1.6)
    for i, m in zip(y, ms):
        a2.text(0.03, i, f"{m['lift']:.2f}", va="center", fontsize=14, color=INK, weight="bold")
    a2.set_xlim(0, 1.6)
    a2.set_xlabel("lift with chaas (dashes: one, chance)")
    a2.set_title("Lift: about as often as chance")
    fig.suptitle("The four items in four or more of the twelve orders, invented", fontsize=13, color=MUTED)
    fig.tight_layout()
    save(fig, "C2_W04_D03_chaas_partner_STUDENT.png")


def popular_sweep():
    """An item that ignores its partner: the partner's confidence rises with its share, lift stays one."""
    shares = [x / 100 for x in range(20, 91, 10)]
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.plot([x * 100 for x in shares], shares, color=VIOLET, lw=3, marker="o", ms=7,
            label="confidence toward it")
    ax.plot([x * 100 for x in shares], [1] * len(shares), color=ROSE, lw=3, ls="--", marker="s", ms=7,
            label="lift with it")
    ax.set_xlabel("percent of baskets with the popular item")
    ax.set_ylabel("confidence, or lift")
    ax.set_ylim(0, 1.25)
    ax.legend(frameon=False, loc="lower right", fontsize=12)
    ax.set_title("A partner that ignores\nthe popular item", fontsize=13)
    fig.text(0.99, 0.01, "invented", ha="right", fontsize=12, color=MUTED)
    fig.tight_layout()
    save(fig, "C2_W04_D03_popular_sweep_STUDENT.png")

def canteen_rankings():
    """The canteen's pairs ranked by count and by lift: two different tops."""
    p = all_pairs(canteen())
    by_count = p.sort_values(["both", "lift"], ascending=[False, False]).head(4)
    by_lift = p.sort_values(["lift", "both"], ascending=[False, False]).head(4)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.6))
    for a, frame, col, title in ((a1, by_count, "both", "By count: orders holding both"),
                                 (a2, by_lift, "lift", "By lift: seen over chance")):
        y = range(len(frame))
        a.barh(list(y), frame[col], color=TINT, edgecolor=VIOLET, lw=2)
        for i, r in zip(y, frame.itertuples()):
            if col == "lift":
                note = f"{r.lift:.2f} on {r.both} order{'s' if r.both > 1 else ''}"
            else:
                note = f"{r.both} orders, lift {r.lift:.2f}"
            a.text(getattr(r, col) + frame[col].max() * 0.03, i, note, va="center", fontsize=12, color=INK)
        a.set_yticks(list(y), [f"{r.a} + {r.b}" for r in frame.itertuples()])
        a.invert_yaxis()
        a.set_xticks([])
        a.spines["bottom"].set_visible(False)
        a.set_xlim(0, frame[col].max() * 1.9)
        a.set_title(title, fontsize=13)
    fig.text(0.99, 0.01, "twelve lunch orders, invented", ha="right", fontsize=12, color=MUTED)
    fig.tight_layout()
    save(fig, "C2_W04_D03_canteen_rankings_STUDENT.png")

def month_luck():
    """600 invented orders in which no item depends on another: lift on few orders swings by luck."""
    m = pd.read_csv(DATA / "C2_W04_D03_canteen_month_STUDENT.csv")
    orders = [(o, set(g)) for o, g in m.groupby("order_id").item]
    p = all_pairs(orders)
    fig, ax = plt.subplots(figsize=(12.5, 4.8))
    thin, thick = p[p.both <= 2], p[p.both >= 30]
    mid = p[(p.both > 2) & (p.both < 30)]
    ax.scatter(mid.both, mid.lift, s=40, color=MUTED, alpha=0.6, label="3 to 29 orders")
    ax.scatter(thin.both, thin.lift, s=70, color=ROSE, edgecolor=INK, label="one or two orders")
    ax.scatter(thick.both, thick.lift, s=70, color=GREEN, edgecolor=INK, label="30 or more orders")
    ax.axhline(1, color=INK, ls="--", lw=1.4)
    ax.axvline(30, color=MUTED, ls=":", lw=1.4)
    top = thin.sort_values("lift").iloc[-1]
    ax.annotate(f"{top.a} + {top.b}: {top.lift:.2f} on {top.both} orders", (top.both, top.lift),
                textcoords="offset points", xytext=(12, -4), fontsize=13, weight="bold", color=INK)
    ax.text(40, 1.6, f"30 or more orders: lift {thick.lift.min():.2f} to {thick.lift.max():.2f}",
            fontsize=13, weight="bold", color=GREEN)
    ax.set_xscale("log")
    ax.set_xticks([1, 3, 10, 30, 100, 300], ["1", "3", "10", "30", "100", "300"])
    ax.set_xlabel("orders holding both (each step right is about three times more)")
    ax.set_ylabel("lift")
    ax.set_ylim(0, max(10, top.lift + 1))
    ax.legend(frameon=False, loc="upper right", fontsize=12)
    ax.set_title("600 invented orders, no item depending on another: every pair should read one")
    fig.tight_layout()
    save(fig, "C2_W04_D03_month_luck_STUDENT.png")


def canteen_action_map():
    """The canteen's pairs placed: a floor of three orders, a bar of 1.5, four regions."""
    p = all_pairs(canteen())
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.axvspan(2.5, 6.6, ymin=1.5 / 6.8, ymax=1, color="#E8F5EE", alpha=0.8)
    ax.axvspan(0.4, 2.5, ymin=1.5 / 6.8, ymax=1, color="#FBF4E3", alpha=0.9)
    ax.axvline(2.5, color=MUTED, ls="--", lw=1.3)
    ax.axhline(1.5, color=GREEN, ls=":", lw=1.6)
    ax.axhline(1, color=INK, ls="--", lw=1.2)
    ax.scatter(p.both, p.lift, s=70, color=VIOLET, edgecolor=INK, zorder=3)
    ax.text(2.6, 6.25, "floor: 3", color=MUTED, fontsize=12)
    ax.text(4.4, 4.9, "PROMOTE", color=GREEN, fontsize=13, weight="bold")
    ax.text(1.0, 4.4, "WATCH", color=AMBER, fontsize=13, weight="bold")
    ax.text(1.2, 0.2, "IGNORE", color=MUTED, fontsize=12, weight="bold")
    ax.text(3.2, 0.2, "TRAP: near one", color=ROSE, fontsize=12, weight="bold")
    marks = {("roti", "sabzi"): ("roti + sabzi 2.25", (8, 6)), ("papad", "pickle"): ("papad +\npickle 2.40", (-8, 10)),
             ("curd", "gulab jamun"): ("gulab jamun\n+ curd 6.00", (10, -12)),
             ("chaas", "dal rice"): ("dal rice + chaas 1.33", None)}
    for (a, b), (label, off) in marks.items():
        r = p[(p.a == a) & (p.b == b)].iloc[0]
        if off is None:
            ax.annotate(label, (r.both, r.lift), xytext=(3.9, 3.3), textcoords="data", fontsize=12,
                        weight="bold", color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1))
            continue
        ax.annotate(label, (r.both, r.lift), textcoords="offset points", xytext=off,
                    fontsize=12, weight="bold", color=INK, ha="right" if off[0] < 0 else "left")
    ax.set_xlim(0.4, 6.6)
    ax.set_ylim(0, 6.8)
    ax.set_xticks(range(1, 7))
    ax.set_xlabel("orders holding both, of 12")
    ax.set_ylabel("lift")
    ax.set_title("The canteen's 13 pairs, placed", fontsize=14)
    fig.text(0.99, 0.01, "invented orders", ha="right", fontsize=12, color=MUTED)
    fig.tight_layout()
    save(fig, "C2_W04_D03_canteen_action_map_STUDENT.png")

def kirana_bridge():
    """Sharma Kirana's combo card, from 18 new packs to Rs 28 a month."""
    steps = [("18 new packs\nx Rs 12 margin", int(v("toy_kirana_incremental_margin"))),
             ("Rs 1 back on\n168 combo bills", -int(v("toy_kirana_discount_back"))),
             ("printing\nthe cards", -int(v("toy_kirana_printing")))]
    fig, ax = plt.subplots(figsize=(12.5, 4.6))
    run = 0
    for i, (label, val) in enumerate(steps):
        bottom = run if val > 0 else run + val
        ax.bar(i, abs(val), bottom=bottom, color=GREEN if val > 0 else ROSE, edgecolor=INK, width=0.6)
        ax.text(i, run + val + (8 if val > 0 else -22), f"{'+' if val > 0 else '-'}Rs {abs(val)}",
                ha="center", fontsize=15, weight="bold", color=INK)
        run += val
    ax.bar(3, run, color=VIOLET, edgecolor=INK, width=0.6)
    ax.text(3, run + 8, f"Rs {run} a month", ha="center", fontsize=15, weight="bold", color=INK)
    ax.set_xticks(range(4), [x[0] for x in steps] + ["expected value"])
    ax.set_ylim(0, 260)
    ax.set_ylabel("Rs a month")
    ax.set_title("Sharma Kirana's tea-and-rusk card, one invented month: Rs 216 - Rs 168 - Rs 20 = Rs 28")
    fig.tight_layout()
    save(fig, "C2_W04_D03_kirana_bridge_STUDENT.png")


def kirana_discount():
    """Expected value against the discount, and against the response the card assumes."""
    tea_only, both, margin, printing = 450, 150, 12, 20
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.6), gridspec_kw={"width_ratios": [1.4, 1]})
    ds = [x / 10 for x in range(0, 51)]
    packs = round(tea_only * 0.04)
    ev = [packs * margin - (both + packs) * d - printing for d in ds]
    a1.plot(ds, ev, color=VIOLET, lw=3)
    a1.axhline(0, color=INK, lw=1.2)
    a1.scatter([1, 2], [packs * margin - (both + packs) - printing, packs * margin - (both + packs) * 2 - printing],
               s=90, color=[GREEN, ROSE], edgecolor=INK, zorder=3)
    a1.text(1.12, 40, "Rs 1 off: Rs 28", fontsize=14, weight="bold", color=GREEN)
    a1.text(2.12, -150, "Rs 2 off: Rs -140", fontsize=14, weight="bold", color=ROSE)
    a1.set_xlabel("discount on a combo bill, Rs (response held at 4 percent)")
    a1.set_ylabel("expected value, Rs a month")
    a1.set_title("It crosses zero just past Rs 1", fontsize=15)
    rs = [0.02, 0.04, 0.06]
    vals = [round(tea_only * r) * margin - (both + round(tea_only * r)) - printing for r in rs]
    a2.bar(range(3), vals, color=[ROSE if x < 0 else GREEN for x in vals], edgecolor=INK, width=0.6)
    for i, val in enumerate(vals):
        a2.text(i, val + (6 if val >= 0 else -18), f"Rs {val}", ha="center", fontsize=14, weight="bold", color=INK)
    a2.axhline(0, color=INK, lw=1.2)
    a2.set_xticks(range(3), ["2 percent", "4 percent", "6 percent"])
    a2.set_xlabel("share of the 450 that add a pack")
    a2.set_ylim(-110, 160)
    a2.set_title("The assumed response decides the sign", fontsize=15)
    fig.suptitle("Sharma Kirana's combo card, invented", fontsize=13, color=MUTED)
    fig.tight_layout()
    save(fig, "C2_W04_D03_kirana_discount_STUDENT.png")


def concept_pictures():
    canteen_dots("C2_W04_D03_canteen_dots_STUDENT.png",
                 f"support = 3 / 12 = {s('toy_canteen_roti_sabzi_support')}")
    canteen_dots("C2_W04_D03_canteen_two_by_two_STUDENT.png",
                 f"support {s('toy_canteen_roti_sabzi_support')}   confidence "
                 f"{s('toy_canteen_roti_sabzi_conf_ab')}   lift {s('toy_canteen_roti_sabzi_lift')}")
    canteen_pair_counts()
    canteen_two_ways()
    canteen_shrink()
    canteen_direction()
    canteen_seen_expected()
    canteen_areas()
    chaas_partner()
    popular_sweep()
    canteen_rankings()
    month_luck()
    canteen_action_map()
    kirana_bridge()
    kirana_discount()


# =========================================================================== SECTION 7, the twelve carts
def twelve():
    t = pd.read_csv(DATA / "C2_W04_D03_twelve_rows_STUDENT.csv")
    return t, [(r.cart_id, {c for c in t.columns[1:] if getattr(r, c.replace(" ", "_"), 0) == 1})
               for r in t.rename(columns=lambda c: c.replace(" ", "_")).itertuples()]


def shrinking_universe():
    """Confidence as a smaller denominator: twelve carts, then the bread carts, then bread with milk."""
    t = pd.read_csv(DATA / "C2_W04_D03_twelve_rows_STUDENT.csv")
    carts = [(row["cart_id"], {c for c in t.columns[1:] if row[c] == 1}) for _, row in t.iterrows()]
    short = {"toned milk": "milk", "chocolate sauce": "choc sauce", "cold drink": "cold drink"}
    pos = [(i % 4, 2 - i // 4) for i in range(12)]
    titles = [f"All twelve carts: milk in {v('twelve_milk')}",
              f"Keep only the carts with bread: {v('twelve_bread')}",
              f"Of the {v('twelve_bread')} bread carts, {v('twelve_bread_milk')} also hold milk"]
    reads = ["bread is in 4 of 12 carts",
             "confidence asks only about these 4 carts",
             f"confidence = 4 / 4 = {s('twelve_bread_milk_conf')}; milk was in 8 of 12 anyway"]

    def draw(ax, stage):
        ax.clear()
        ax.set_xlim(-0.55, 3.55)
        ax.set_ylim(-0.75, 2.5)
        ax.axis("off")
        for (cid, held), (x, y) in zip(carts, pos):
            on = stage == 0 or ("bread" in held and (stage == 1 or "toned milk" in held))
            ax.add_patch(mpatches.FancyBboxPatch((x - 0.46, y - 0.36), 0.92, 0.72,
                                                 boxstyle="round,pad=0.02", lw=1.6,
                                                 facecolor=TINT if on else WHITE,
                                                 edgecolor=VIOLET if on else "#D5D1E8",
                                                 alpha=1 if on else 0.6))
            ax.text(x, y + 0.17, cid, ha="center", fontsize=12, weight="bold",
                    color=INK if on else "#B8B2D6")
            label = "milk" if "toned milk" in held else "no milk"
            label += ", bread" if "bread" in held else ""
            ax.text(x, y - 0.13, label, ha="center", fontsize=11, color=INK if on else "#C9C5DD")
        ax.set_title(titles[stage], fontsize=16)
        ax.text(1.5, -0.62, reads[stage], ha="center", fontsize=14, weight="bold", color=INK)

    fig, ax = plt.subplots(figsize=(12.5, 5.0))
    draw(ax, 0)
    fig.savefig(OUT / "C2_W04_D03_shrink_still_first_STUDENT.png", dpi=170, bbox_inches="tight",
                facecolor=WHITE)
    draw(ax, 2)
    fig.savefig(OUT / "C2_W04_D03_shrink_still_last_STUDENT.png", dpi=170, bbox_inches="tight",
                facecolor=WHITE)
    anim = FuncAnimation(fig, lambda i: draw(ax, i), frames=3, interval=1800)
    anim.save(OUT / "C2_W04_D03_shrink_STUDENT.gif", writer=PillowWriter(fps=0.6))
    plt.close(fig)
    print("  wrote the shrink GIF and its two stills")


# =========================================================================== SECTION 8, every cart
def areas():
    """Lift as a ratio of two areas: bread's band times milk's band against the observed overlap."""
    pb, pm, obs = v("bread_share"), v("toned_milk_share"), v("bread_milk_support")
    fig, (al, ar) = plt.subplots(1, 2, figsize=(12.5, 5.0))
    for a in (al, ar):
        a.set_xlim(0, 1)
        a.set_ylim(0, 1)
        a.set_aspect("equal")
        a.set_xticks([0, 0.5, 1])
        a.set_yticks([0, 0.5, 1])
    al.add_patch(mpatches.Rectangle((0, 0), pb, 1, facecolor=TINT, edgecolor=VIOLET))
    al.add_patch(mpatches.Rectangle((0, 0), 1, pm, facecolor=LAV, alpha=0.35, edgecolor=INK))
    al.add_patch(mpatches.Rectangle((0, 0), pb, pm, facecolor=VIOLET, edgecolor=INK, lw=2))
    al.text(pb / 2, pm / 2, f"expected\n{pb:.2f} x {pm:.2f}\n= {pb * pm:.3f}", ha="center",
            va="center", color=WHITE, fontsize=13, weight="bold")
    al.set_xlabel(f"share of carts with bread: {pb:.2f}")
    al.set_ylabel(f"share of carts with milk: {pm:.2f}")
    al.set_title("If bread and milk ignored each other", fontsize=14)
    ar.add_patch(mpatches.Rectangle((0, 0), pb, 1, facecolor=TINT, edgecolor=VIOLET, ls="--"))
    ar.add_patch(mpatches.Rectangle((0, 0), pb, obs / pb, facecolor=VIOLET, edgecolor=INK, lw=2))
    ar.add_patch(mpatches.Rectangle((0, 0), pb, pm, fill=False, edgecolor=ROSE, lw=2, ls="--"))
    ar.text(pb / 2, obs / pb / 2, f"seen\n{obs:.3f}", ha="center", va="center", color=WHITE,
            fontsize=13, weight="bold")
    ar.text(pb + 0.04, (obs / pb) + 0.01, f"height {s('bread_milk_conf_ab')}: milk inside the bread carts",
            fontsize=12, color=INK, va="bottom")
    ar.text(pb + 0.04, pm - 0.03, f"red dashes, height {pm:.2f}: milk in all carts", fontsize=12,
            color=ROSE, va="top")
    ar.text(pb + 0.04, 0.22, "area = width x height\n= share of carts holding both", fontsize=12,
            color=MUTED)
    ar.set_xlabel(f"share of carts with bread: {pb:.2f}")
    ar.set_ylabel("share of the bread carts with milk")
    ar.set_title(f"Seen {s('bread_milk_carts')} carts, expected {s('bread_milk_expected')}: "
                 f"lift {s('bread_milk_lift')}", fontsize=14)
    fig.tight_layout()
    save(fig, "C2_W04_D03_areas_STUDENT.png")


def milk_everywhere():
    """Confidence toward milk and lift with milk for the nine most common items."""
    items, b = baskets()
    n = len(b)
    milk = b.apply(lambda x: "toned milk" in x)
    share = items.groupby("item").cart_id.nunique().drop("toned milk").sort_values(ascending=False)
    top = list(share.index[:9])
    conf = [(b.apply(lambda x: t in x) & milk).sum() / b.apply(lambda x: t in x).sum() for t in top]
    lift = [c / v("toned_milk_share") for c in conf]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 4.6), sharey=True)
    y = range(len(top))
    a1.barh(y, conf, color=TINT, edgecolor=VIOLET)
    a1.axvline(v("toned_milk_share"), color=INK, ls="--", lw=1.4)
    for i, c in zip(y, conf):
        a1.text(0.03, i, f"{c:.2f}", va="center", ha="left", fontsize=12, color=INK)
    a1.set_yticks(list(y), top)
    a1.invert_yaxis()
    a1.set_xlim(0, 1)
    a1.set_xlabel(f"confidence toward milk (dashes: milk's own share, {s('toned_milk_share')})")
    a1.set_title("Every item looks bundled with milk")
    a2.barh(y, lift, color=TINT, edgecolor=VIOLET)
    a2.axvline(1, color=INK, ls="--", lw=1.4)
    for i, l in zip(y, lift):
        a2.text(0.03, i, f"{l:.2f}", va="center", ha="left", fontsize=12, color=INK)
    a2.set_xlim(0, 1.25)
    a2.set_xlabel("lift with milk (dashes: one, chance)")
    a2.set_title("Lift says: about as often as chance")
    fig.tight_layout()
    save(fig, "C2_W04_D03_milk_everywhere_STUDENT.png")


def actual_vs_expected():
    """For four pairs, the carts expected to hold both if independent against the carts that do."""
    pairs = [("bread and milk", "bread_milk"), ("eggs and milk", "eggs_milk"),
             ("chips and cold drink", "chips_cold"), ("ice cream and choc sauce", "ice_choc")]
    fig, axes = plt.subplots(1, 4, figsize=(12.5, 4.6))
    for a, (label, key) in zip(axes, pairs):
        e, o = v(f"{key}_expected"), v(f"{key}_carts")
        a.bar([0, 1], [e, o], color=[LINE, VIOLET], edgecolor=INK, width=0.6)
        for x, val in ((0, e), (1, o)):
            a.text(x, val * 1.02, f"{val:,}", ha="center", va="bottom", fontsize=12, color=INK)
        a.set_xticks([0, 1], ["expected", "seen"])
        a.set_yticks([])
        a.spines["left"].set_visible(False)
        a.set_ylim(0, max(e, o) * 1.25)
        a.set_title(f"{label}\nlift {s(key + '_lift')}", fontsize=13)
    fig.suptitle("Carts holding both: expected if independent, against what 40,000 carts show",
                 fontsize=15, weight="bold", color=INK)
    fig.tight_layout()
    save(fig, "C2_W04_D03_actual_vs_expected_STUDENT.png")


def strip_daily():
    """Daily strip click-through and milk's share of slot impressions, 17 August to 27 September."""
    log = pd.read_csv(DATA / "C2_W04_D03_strip_log_STUDENT.csv", parse_dates=["date"])
    day = log.groupby("date")[["impressions", "clicks"]].sum()
    day["ctr"] = day.clicks / day.impressions
    milk = log[log.suggested_item == "toned milk"].groupby("date").impressions.sum()
    day["milk"] = (milk / day.impressions).fillna(0)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(12.5, 4.6), sharex=True,
                                 gridspec_kw={"height_ratios": [1.5, 1]})
    a1.plot(day.index, day.ctr * 100, color=VIOLET, lw=2.4, marker="o", ms=4)
    a1.axvline(pd.Timestamp("2026-09-07"), color=ROSE, ls="--", lw=1.6)
    a1.text(pd.Timestamp("2026-09-07"), 6.6, "  7 Sep: ranked by count", color=ROSE, fontsize=13)
    a1.set_ylabel("click-through, %")
    a1.set_ylim(3, 7)
    a1.set_title(f"Strip click-through by day: about {s('before_strip_ctr')} before, "
                 f"{s('after_strip_ctr')} after")
    a2.bar(day.index, day.milk * 100, color=[ROSE if d >= pd.Timestamp("2026-09-07") else LINE
                                             for d in day.index], edgecolor=INK, lw=0.4)
    a2.set_ylabel("milk's share\nof slots, %")
    a2.set_ylim(0, 60)
    a2.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    a2.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    fig.tight_layout()
    save(fig, "C2_W04_D03_strip_daily_STUDENT.png")


def ctr_by_slot():
    """Click-through by slot position: before, milk after, everything else after."""
    groups = [("before, everything else", "before", "other", MUTED),
              ("after, milk", "after", "milk", ROSE),
              ("after, everything else", "after", "other", GREEN)]
    fig, ax = plt.subplots(figsize=(12.5, 4.4))
    width = 0.26
    for k, (label, w, g, color) in enumerate(groups):
        vals = [v(f"ctr_{w}_{g}_slot{slot}") for slot in (1, 2, 3)]
        xs = [slot + (k - 1) * width for slot in (1, 2, 3)]
        ax.bar(xs, [x * 100 for x in vals], width, color=color, edgecolor=INK, label=label)
        shown = [s(f"ctr_{w}_{g}_slot{slot}").split()[0] for slot in (1, 2, 3)]
        for x, val, txt in zip(xs, vals, shown):
            ax.text(x, val * 100 + 0.12, txt, ha="center", fontsize=12, color=INK)
    ax.set_xticks([1, 2, 3], ["slot 1", "slot 2", "slot 3"])
    ax.set_ylabel("click-through, %")
    ax.set_ylim(0, 10)
    ax.legend(frameon=False, loc="upper right")
    ax.set_title("Among suggestions other than milk, slot 1 draws the most clicks; milk is low in every slot")
    fig.tight_layout()
    save(fig, "C2_W04_D03_ctr_by_slot_STUDENT.png")


# =========================================================================== SECTION 10, the strip
def pairs_frame(b):
    n = len(b)
    single = Counter(x for st in b for x in st)
    double = Counter(p for st in b for p in combinations(sorted(st), 2))
    return pd.DataFrame([{"a": a, "b": c, "support": k / n, "lift": k * n / (single[a] * single[c])}
                         for (a, c), k in double.items()])


def action_map():
    """Every pair with support of at least 0.1 percent, lift against support, with the floor."""
    _, b = baskets()
    p = pairs_frame(list(b))
    p = p[p.support >= 0.001]
    fig, ax = plt.subplots(figsize=(12.5, 5.0))
    ax.axvspan(0.01, 0.6, ymin=1.5 / 5.2, ymax=1, color="#E8F5EE", alpha=0.7)
    ax.axvspan(0.001, 0.01, ymin=1.5 / 5.2, ymax=1, color="#FBF4E3", alpha=0.8)
    ax.scatter(p.support, p.lift, s=16, color=VIOLET, alpha=0.45, edgecolor="none")
    ax.axhline(1, color=MUTED, ls="--", lw=1.2)
    ax.axhline(1.5, color=GREEN, ls=":", lw=1.4)
    ax.axvline(0.01, color=MUTED, ls="--", lw=1.2)
    ax.text(0.0105, 4.95, "floor: 1 percent of carts", color=MUTED, fontsize=12)
    ax.text(0.0013, 1.58, "lift 1.5", color=GREEN, fontsize=12)
    ax.text(0.15, 4.6, "PROMOTE", color=GREEN, fontsize=15, weight="bold")
    ax.text(0.0013, 4.6, "WATCH", color=AMBER, fontsize=15, weight="bold")
    ax.text(0.0013, 0.4, "IGNORE", color=MUTED, fontsize=13, weight="bold")
    ax.text(0.02, 0.4, "TRAP: near one, on many carts", color=ROSE, fontsize=13, weight="bold")
    labels = [("chips", "cold drink", "chips + cold drink", (8, 6)),
              ("coriander", "green chillies", "coriander + chillies", (8, -16)),
              ("bread", "butter", "bread + butter", (8, 4)),
              ("onions", "tomatoes", "onions + tomatoes", (8, 6)),
              ("chocolate sauce", "ice cream", "ice cream + choc sauce", (8, 4)),
              ("bread", "toned milk", "bread + milk", (-10, 10))]
    for a, c, label, off in labels:
        row = p[(p.a == a) & (p.b == c)]
        x, y = row.support.iloc[0], row.lift.iloc[0]
        ax.scatter([x], [y], s=70, color=INK, zorder=3)
        ax.annotate(f"{label}  {y:.2f}", (x, y), textcoords="offset points", xytext=off,
                    fontsize=12, color=INK, weight="bold",
                    ha="right" if off[0] < 0 else "left")
    ax.set_xscale("log")
    ax.set_xlim(0.001, 0.6)
    ax.set_ylim(0, 5.2)
    ax.set_xticks([0.001, 0.01, 0.1, 0.5], ["0.1%", "1%", "10%", "50%"])
    ax.set_xlabel("support: share of the 40,000 carts holding both (each step right is ten times more carts)")
    ax.set_ylabel("lift")
    ax.set_title(f"{len(p):,} pairs with support of at least 0.1 percent; four beat chance above the floor")
    fig.tight_layout()
    save(fig, "C2_W04_D03_action_map_STUDENT.png")


def heavy_tenth():
    """Per cart against per customer: the party pair shrinks, milk's pair does not move."""
    rows = [("chips + cold drink", v("chips_cold_lift"), v("chips_cold_lift_per_customer")),
            ("bread + milk", v("bread_milk_lift"), v("bread_milk_lift_per_customer"))]
    fig, ax = plt.subplots(figsize=(12.5, 3.8))
    for i, (label, per_cart, per_cust) in enumerate(rows):
        ax.barh(i - 0.18, per_cart, 0.34, color=VIOLET, edgecolor=INK,
                label="every cart counted" if i == 0 else None)
        ax.barh(i + 0.18, per_cust, 0.34, color=LAV, edgecolor=INK,
                label="every customer counted once" if i == 0 else None)
        ax.text(per_cart + 0.04, i - 0.18, f"{per_cart:.2f}", va="center", fontsize=13, color=INK)
        ax.text(per_cust + 0.04, i + 0.18, f"{per_cust:.2f}", va="center", fontsize=13, color=INK)
    ax.set_yticks([0, 1], [r[0] for r in rows])
    ax.invert_yaxis()
    ax.axvline(1, color=MUTED, ls="--", lw=1.2)
    ax.set_xlim(0, 4)
    ax.set_xlabel("lift")
    ax.legend(frameon=False, loc="lower right")
    ax.set_title(f"The top tenth place {s('heavy_tenth_share')} of carts and "
                 f"{s('chips_cold_heavy_share')} of the chips + cold drink carts")
    fig.tight_layout()
    save(fig, "C2_W04_D03_heavy_tenth_STUDENT.png")


def stockout():
    """Curd's share of carts by zone and week, the two stock-out cells near zero."""
    carts = pd.read_csv(DATA / "C2_W04_D03_carts_STUDENT.csv", parse_dates=["placed_date"])
    items = pd.read_csv(DATA / "C2_W04_D03_cart_items_STUDENT.csv")
    curd = set(items.loc[items.item == "curd", "cart_id"])
    carts["curd"] = carts.cart_id.isin(curd)
    carts["week"] = (carts.placed_date.dt.day - 1) // 7 + 1
    grid = carts.pivot_table(index="zone", columns="week", values="curd", aggfunc="mean")
    grid = grid.loc[grid.mean(axis=1).sort_values(ascending=False).index]
    fig, ax = plt.subplots(figsize=(12.5, 4.6))
    im = ax.imshow(grid.values, cmap="Purples", vmin=0, vmax=0.35, aspect="auto")
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            val = grid.values[i, j]
            ax.text(j, i, f"{val * 100:.0f}%", ha="center", va="center", fontsize=13,
                    color=WHITE if val > 0.2 else ROSE, weight="bold")
    ax.set_xticks(range(4), ["week 1\n1-7 Sep", "week 2\n8-14 Sep", "week 3\n15-21 Sep",
                             "week 4\n22-28 Sep"])
    ax.set_yticks(range(len(grid)), grid.index)
    ax.spines[:].set_visible(False)
    ax.set_title("Share of carts holding curd, by zone and week")
    fig.tight_layout()
    save(fig, "C2_W04_D03_stockout_STUDENT.png")


def slot_value():
    """The rupee value of one slot a day, and what re-ranking recovers in a month."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.3), gridspec_kw={"width_ratios": [1.1, 1]})
    vals = [v("slot_value_other_day"), v("slot_value_milk_day")]
    a1.bar([0, 1], vals, color=[GREEN, ROSE], edgecolor=INK, width=0.6)
    for x, val in zip([0, 1], vals):
        a1.text(x, val + 300, f"Rs {val:,}", ha="center", fontsize=14, weight="bold", color=INK)
    a1.annotate("", xy=(0.5, vals[1]), xytext=(0.5, vals[0]),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.6))
    a1.text(0.55, (vals[0] + vals[1]) / 2, f"gap\n{s('slot_gap_day')}", fontsize=13, color=INK)
    a1.set_xticks([0, 1], ["a slot showing a pair\nthat beats chance (6.4%)",
                           "a slot showing\nmilk (1.2%)"])
    a1.set_yticks([])
    a1.spines["left"].set_visible(False)
    a1.set_ylim(0, 20500)
    a1.set_title("One slot, one day: 60,000 views x CTR x 0.5 x Rs 9", fontsize=14)
    steps = [("gap a slot a day", v("slot_gap_day")), ("x 30 days", v("slot_gap_month")),
             ("x 1.5 slots' worth\nof milk impressions", v("recoverable_month"))]
    a2.barh([2, 1, 0], [x[1] for x in steps], color=[LINE, TINT, VIOLET], edgecolor=INK)
    shown = [s("slot_gap_day"), s("slot_gap_month"), s("recoverable_month")]
    for y, (label, val), txt in zip([2, 1, 0], steps, shown):
        a2.text(val + 12000, y, txt, va="center", fontsize=14, weight="bold", color=INK)
    a2.set_yticks([2, 1, 0], [x[0] for x in steps])
    a2.set_xticks([])
    a2.spines["bottom"].set_visible(False)
    a2.set_xlim(0, 900_000)
    a2.set_title("What re-ranking recovers in a month", fontsize=14)
    fig.tight_layout()
    save(fig, "C2_W04_D03_slot_value_STUDENT.png")


def main():
    print("Drawing Wednesday's pictures from the data and the facts file")
    concept_pictures()
    shrinking_universe()
    areas()
    milk_everywhere()
    actual_vs_expected()
    strip_daily()
    ctr_by_slot()
    action_map()
    heavy_tenth()
    stockout()
    slot_value()


if __name__ == "__main__":
    main()

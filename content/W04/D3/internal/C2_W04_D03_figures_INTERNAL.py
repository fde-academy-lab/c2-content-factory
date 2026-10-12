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


# =========================================================================== chapter 1
def ten_dots(name="C2_W04_D03_ten_dots_STUDENT.png", width=11.5):
    """The tea stall's ten invented orders as dots in two circles, beside the 2 by 2 table."""
    fig, (ax, at) = plt.subplots(1, 2, figsize=(width, 4.6), gridspec_kw={"width_ratios": [1.15, 1]})
    for a in (ax, at):
        a.axis("off")
    ax.set_aspect("equal")
    ax.add_patch(plt.Circle((2.2, 2.0), 1.45, facecolor=TINT, edgecolor=VIOLET, lw=2.2))
    ax.add_patch(plt.Circle((3.9, 2.0), 1.45, facecolor="#F6EEFC", edgecolor=VIOLET, lw=2.2, alpha=0.75))
    chai_only = [(1.3, 2.4), (1.6, 1.4), (2.0, 2.9)]
    both = [(3.0, 2.5), (3.1, 1.6), (2.75, 2.05)]
    biscuit_only = [(4.6, 2.0)]
    neither = [(6.3, 3.0), (6.6, 2.0), (6.3, 1.0)]
    for x, y in chai_only + both + biscuit_only + neither:
        ax.plot(x, y, "o", color=INK, ms=11)
    ax.text(1.4, 3.75, "chai: 6", color=VIOLET, fontsize=14, weight="bold")
    ax.text(3.9, 3.75, "biscuit: 4", color=VIOLET, fontsize=14, weight="bold")
    ax.text(2.95, 0.2, "both: 3", color=INK, fontsize=14, weight="bold", ha="center")
    ax.text(6.45, 0.2, "neither: 3", color=MUTED, fontsize=13, ha="center")
    ax.set_xlim(0.5, 7.3)
    ax.set_ylim(-0.1, 4.2)
    tab = at.table(cellText=[["3", "3", "6"], ["1", "3", "4"], ["4", "6", "10"]],
                   rowLabels=["chai", "no chai", "all"], colLabels=["biscuit", "no biscuit", "all"],
                   cellColours=[[TINT, WHITE, "#F7F5FD"], [WHITE, WHITE, "#F7F5FD"],
                                ["#F7F5FD", "#F7F5FD", "#F7F5FD"]],
                   loc="center", cellLoc="center", bbox=[0.18, 0.25, 0.78, 0.6])
    tab.auto_set_font_size(False)
    tab.set_fontsize(14)
    for (r, c), cell in tab.get_celld().items():
        cell.set_edgecolor("#B8B2D6")
        if r == 0 or c == -1:
            cell.set_text_props(weight="bold", color=INK)
    at.text(0.57, 0.93, "ten orders, invented", transform=at.transAxes, ha="center", color=MUTED, fontsize=13)
    at.text(0.57, 0.1, f"support {s('tea_support')}   confidence {s('tea_conf')}   lift {s('tea_lift')}",
            transform=at.transAxes, ha="center", color=INK, fontsize=14, weight="bold")
    fig.tight_layout()
    save(fig, name)


def carry_bag():
    """The popular partner in miniature: biscuit to carry bag reads 0.75, under the bag's own 0.9."""
    fig, ax = plt.subplots(figsize=(10.5, 3.8))
    rows = [("confidence, biscuit to bag", v("tea_bag_conf"), VIOLET),
            ("share of all ten orders with a bag", 0.9, MUTED)]
    for i, (label, val, color) in enumerate(rows):
        ax.barh(i, val, color=color if i == 0 else LINE, edgecolor=INK, height=0.55)
        ax.text(val + 0.015, i, f"{val:.2f}", va="center", fontsize=15, weight="bold", color=INK)
    ax.set_yticks([0, 1], [r[0] for r in rows])
    ax.set_xlim(0, 1.12)
    ax.invert_yaxis()
    ax.set_xlabel("share of orders")
    ax.set_title(f"Bag in 9 of 10 orders: lift = 0.75 / 0.90 = {s('tea_bag_lift')}, below one (invented)")
    fig.tight_layout()
    save(fig, "C2_W04_D03_carry_bag_STUDENT.png")


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
              f"Of those, carts that also hold milk: {v('twelve_bread_milk')}"]
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


# =========================================================================== chapter 2
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
    al.set_ylabel(f"share with milk: {pm:.2f}")
    al.set_title("If bread and milk ignored each other")
    ar.add_patch(mpatches.Rectangle((0, 0), pb, 1, facecolor=TINT, edgecolor=VIOLET, ls="--"))
    ar.add_patch(mpatches.Rectangle((0, 0), pb, obs / pb, facecolor=VIOLET, edgecolor=INK, lw=2))
    ar.add_patch(mpatches.Rectangle((0, 0), pb, pm, fill=False, edgecolor=ROSE, lw=2, ls="--"))
    ar.text(pb / 2, obs / pb / 2, f"seen\n{obs:.3f}", ha="center", va="center", color=WHITE,
            fontsize=13, weight="bold")
    ar.text(pb + 0.04, (obs / pb) - 0.02, f"milk inside the bread carts: {s('bread_milk_conf_ab')}",
            fontsize=12, color=INK, va="top")
    ar.text(pb + 0.04, pm - 0.1, f"red dashes: the expected {pb * pm:.3f}", fontsize=12, color=ROSE)
    ar.set_xlabel(f"share of carts with bread: {pb:.2f}")
    ar.set_title(f"What 40,000 carts show: lift {obs:.3f} / {pb * pm:.3f} = {s('bread_milk_lift')}")
    fig.tight_layout()
    save(fig, "C2_W04_D03_areas_STUDENT.png")


def milk_everywhere():
    """Confidence toward milk and lift with milk for the twelve most common items."""
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
    a1.text(v("toned_milk_share") + 0.02, -0.9, f"milk's own share {s('toned_milk_share')}",
            fontsize=12, color=INK)
    for i, c in zip(y, conf):
        a1.text(c - 0.02, i, f"{c:.2f}", va="center", ha="right", fontsize=12, color=INK)
    a1.set_yticks(list(y), top)
    a1.invert_yaxis()
    a1.set_xlim(0, 1)
    a1.set_xlabel("confidence toward milk")
    a1.set_title("Every item looks bundled with milk")
    a2.barh(y, lift, color=TINT, edgecolor=VIOLET)
    a2.axvline(1, color=INK, ls="--", lw=1.4)
    for i, l in zip(y, lift):
        a2.text(l - 0.02, i, f"{l:.2f}", va="center", ha="right", fontsize=12, color=INK)
    a2.set_xlim(0, 1.25)
    a2.set_xlabel("lift with milk")
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
    groups = [("before, every suggestion", "before", "other", MUTED),
              ("after, milk", "after", "milk", ROSE),
              ("after, everything else", "after", "other", GREEN)]
    fig, ax = plt.subplots(figsize=(12.5, 4.4))
    width = 0.26
    for k, (label, w, g, color) in enumerate(groups):
        vals = [v(f"ctr_{w}_{g}_slot{slot}") for slot in (1, 2, 3)]
        xs = [slot + (k - 1) * width for slot in (1, 2, 3)]
        ax.bar(xs, [x * 100 for x in vals], width, color=color, edgecolor=INK, label=label)
        for x, val in zip(xs, vals):
            ax.text(x, val * 100 + 0.12, f"{val * 100:.1f}", ha="center", fontsize=12, color=INK)
    ax.set_xticks([1, 2, 3], ["slot 1", "slot 2", "slot 3"])
    ax.set_ylabel("click-through, %")
    ax.set_ylim(0, 10)
    ax.legend(frameon=False, loc="upper right")
    ax.set_title("Slot 1 draws the most clicks; milk clicks low in every slot")
    fig.tight_layout()
    save(fig, "C2_W04_D03_ctr_by_slot_STUDENT.png")


# =========================================================================== chapter 3
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
    ax.axvline(0.01, color=MUTED, ls="--", lw=1.2)
    ax.text(0.0105, 4.95, "floor: 1 percent of carts", color=MUTED, fontsize=12)
    ax.text(0.15, 4.6, "PROMOTE", color=GREEN, fontsize=15, weight="bold")
    ax.text(0.0013, 4.6, "WATCH", color=AMBER, fontsize=15, weight="bold")
    ax.text(0.03, 0.55, "IGNORE: lift near one, where milk's pairs sit", color=MUTED, fontsize=13,
            weight="bold")
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
    ax.set_xlabel("support: share of the 40,000 carts holding both (log scale)")
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
    ten_dots()
    carry_bag()
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

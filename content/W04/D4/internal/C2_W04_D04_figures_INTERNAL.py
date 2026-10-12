"""Week 4 Thursday's data pictures and the one GIF the spine names, drawn from the day's data.

Run from the repository root after the generator:
    python3 content/W04/D4/internal/C2_W04_D04_figures_INTERNAL.py

Writes PNGs and the triangle GIF (with its first and last frames) to content/W04/D4/whiteboards/.
Every number drawn is computed from the data files and matches the facts file; the toys are drawn
from the facts file's toys block and say invented on the picture. Fonts are 12 to 14 points at the
picture's own size, so a label prints at nine points or more on a slide and five or more on a sheet.
A picture carries no title of its own: the image line's caption under it says what it shows.
"""
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.animation import PillowWriter
import numpy as np
import pandas as pd
import yaml

HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
DATA = DAY / "data"
BOARDS = DAY / "whiteboards"
BOARDS.mkdir(parents=True, exist_ok=True)
STEM = "C2_W04_D04"

INK, VIOLET, DEEP, LAV, MUTED = "#1A0F5C", "#5B3FD6", "#4E38AB", "#D9A7FF", "#6B6690"
ROSE, GREEN, LINE, TINT, AMBER = "#D63A6A", "#1F8A5B", "#E4E1F1", "#EEEAFB", "#C98A00"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13, "axes.titlesize": 13.5, "axes.titleweight": "bold",
    "axes.labelsize": 12.5, "xtick.labelsize": 12.5, "ytick.labelsize": 12.5, "legend.fontsize": 12.5, "axes.edgecolor": MUTED,
    "axes.labelcolor": INK, "axes.titlecolor": INK, "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white",
    "axes.facecolor": "white", "axes.titlelocation": "left",
})

facts = yaml.safe_load((HERE / f"{STEM}_facts_INTERNAL.yaml").read_text(encoding="utf-8"))
F = {n["id"]: n["value"] for n in facts["numbers"]}
TOYS = {t["id"]: t["values"] for t in facts["toys"]}
members = pd.read_csv(DATA / f"{STEM}_members_STUDENT.csv")
mm = pd.read_csv(DATA / f"{STEM}_member_months_STUDENT.csv")
mm = mm.merge(members[["member_id", "cohort_month", "signup_channel"]], on="member_id")
mm["age"] = (mm["month"].str[:4].astype(int) * 12 + mm["month"].str[5:].astype(int)
             - mm["cohort_month"].str[:4].astype(int) * 12 - mm["cohort_month"].str[5:].astype(int))
mm["active"] = mm["orders"] > 0
COHORTS = ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06", "2026-07", "2026-08"]
NAMES = dict(zip(COHORTS + ["2026-09"], "Jan Feb Mar Apr May Jun Jul Aug Sep".split()))
tri = mm[mm.age >= 1].pivot_table(index="cohort_month", columns="age", values="active", aggfunc="mean")
sizes = members.groupby("cohort_month").size()


def save(fig, name):
    path = BOARDS / f"{STEM}_{name}_STUDENT.png"
    fig.savefig(path, dpi=150, facecolor="white", bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print(f"wrote {path.relative_to(DAY)}")


# ------------------------------------------------------------------ 1. the triangle, and its GIF
def draw_triangle(ax, upto=None, note=True, size=12.5):
    """Rows are signup cohorts, columns months since signup; a cell appears once its month has passed."""
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(len(COHORTS) - 0.5, -0.5)
    for i, c in enumerate(COHORTS):
        for k in range(1, 9):
            cal = COHORTS.index(c) + 1 + k                      # calendar month number, Jan = 1
            if cal > 9 or (upto is not None and cal > upto):
                continue
            v = tri.loc[c, k]
            if k == 1:
                face = ROSE if c == "2026-08" else VIOLET
            else:
                face = "#B9AEF0" if v >= 0.385 else "#CFC7F4"
            ax.add_patch(plt.Rectangle((k - 0.5, i - 0.5), 1, 1, facecolor=face, edgecolor="white", lw=2))
            ax.text(k, i, f"{100 * v:.0f}" if k == 1 else f"{100 * v:.1f}", ha="center", va="center",
                    color="white" if k == 1 else INK, fontsize=size, fontweight="bold" if k == 1 else None)
        ax.text(0, i, f"{sizes[c]:,}", ha="center", va="center", fontsize=size, color=MUTED)
    ax.xaxis.tick_top()
    ax.set_xticks(range(0, 9))
    ax.set_xticklabels(["members"] + [str(k) for k in range(1, 9)], fontsize=size)
    ax.set_yticks(range(len(COHORTS)))
    ax.set_yticklabels([f"{NAMES[c]}" + (" (sale)" if c == "2026-08" else "") for c in COHORTS], fontsize=size)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    if note:
        ax.text(8.45, 5.0, "months since joining run across;\nmonth one is the solid column;\n"
                "each cell is the percent of the\ncohort who ordered that month",
                fontsize=size, color=MUTED, va="center", ha="right")


fig, ax = plt.subplots(figsize=(9.0, 4.0))
draw_triangle(ax)
save(fig, "cohort_triangle")

DASH = {m: F[f"dashboard_{NAMES[m].lower()}"] for m in ("2026-06", "2026-07", "2026-08", "2026-09")}


def fill_frame(fig, upto):
    fig.clf()
    ax = fig.add_axes([0.11, 0.10, 0.62, 0.78])
    draw_triangle(ax, upto=upto, note=False)
    ax.set_title(f"The table at the end of {['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep'][upto - 1]}",
                 fontsize=14)
    side = fig.add_axes([0.80, 0.22, 0.18, 0.52])
    shown = [(i, DASH[m]) for i, m in enumerate(DASH) if int(m[5:]) <= upto]
    side.set_xlim(-0.5, 3.5)
    side.set_ylim(0.30, 0.60)
    side.set_xticks(range(4))
    side.set_xticklabels(["Jun", "Jul", "Aug", "Sep"], fontsize=12.5)
    side.set_yticks([0.3, 0.4, 0.5, 0.6])
    side.set_yticklabels(["30", "40", "50", "60"], fontsize=12.5)
    side.set_title("dashboard,\npercent", fontsize=12.5, fontweight="normal", color=INK)
    if shown:
        xs, ys = zip(*shown)
        side.plot(xs, ys, color=INK, lw=2.5, marker="o")
        for x, y in shown:
            side.text(x, y + 0.02, f"{100 * y:.0f}", ha="center", fontsize=12.5, color=INK)
    return ax


fig = plt.figure(figsize=(10.2, 5.0))
writer = PillowWriter(fps=1)
with writer.saving(fig, str(BOARDS / f"{STEM}_cohort_fill_STUDENT.gif"), dpi=96):
    for upto in range(2, 10):
        fill_frame(fig, upto)
        writer.grab_frame()
        if upto == 9:
            for _ in range(2):
                writer.grab_frame()
print("wrote whiteboards/C2_W04_D04_cohort_fill_STUDENT.gif")
fill_frame(fig, 2)
fig.savefig(BOARDS / f"{STEM}_cohort_fill_first_STUDENT.png", dpi=150, facecolor="white")
fill_frame(fig, 9)
fig.savefig(BOARDS / f"{STEM}_cohort_fill_last_STUDENT.png", dpi=150, facecolor="white")
plt.close(fig)
print("wrote the GIF's first and last frames")

# ------------------------------------------------------------------ 2. the curves
fig, ax = plt.subplots(figsize=(9.0, 3.8))
for c in COHORTS:
    row = tri.loc[c].dropna()
    ax.plot(row.index, 100 * row.values, marker="o", ms=4, lw=2.4 if c == "2026-08" else 1.6,
            color=ROSE if c == "2026-08" else VIOLET, alpha=1 if c in ("2026-01", "2026-07", "2026-08") else 0.45)
    ax.text(row.index[-1] + 0.12, 100 * row.values[-1], NAMES[c], fontsize=12.5,
            color=ROSE if c == "2026-08" else INK, va="center")
ax.axhline(38, color=AMBER, lw=1.5, ls="--")
ax.text(8.6, 39.2, "dashboard 38", color=AMBER, fontsize=12.5, ha="right")
ax.set_xticks(range(1, 9))
ax.set_xticklabels([f"month {k}" for k in range(1, 9)])
ax.set_xlim(0.7, 8.7)
ax.set_ylabel("percent who ordered")
ax.set_ylim(28, 62)
save(fig, "retention_curves")

# ------------------------------------------------------------------ 3. the blend decomposed
fig, ax = plt.subplots(figsize=(9.0, 3.9))
months = ["2026-06", "2026-07", "2026-08", "2026-09"]
for x, m in enumerate(months):
    bottom = 0
    cells = mm[(mm.month == m) & (mm.age >= 2)].groupby("cohort_month")["active"].agg(["size", "sum"])
    for c, row in cells.iterrows():
        ax.bar(x, row["sum"], bottom=bottom, color=VIOLET, edgecolor="white", width=0.55)
        ax.bar(x, row["size"] - row["sum"], bottom=bottom + row["sum"], color=TINT, edgecolor="white", width=0.55)
        if row["size"] > 3000:
            ax.text(x, bottom + row["size"] / 2, NAMES[c], ha="center", va="center", fontsize=12, color=INK)
        bottom += row["size"]
    ax.text(x, bottom + 700, f"{100 * DASH[m]:.0f} percent\nof {bottom:,}", ha="center", fontsize=12.5, color=INK)
aug = int(sizes["2026-08"])
aug_on = int(mm[(mm.month == "2026-09") & (mm.cohort_month == "2026-08")]["active"].sum())
ax.bar(3.62, aug_on, color=ROSE, width=0.4, alpha=0.9)
ax.bar(3.62, aug - aug_on, bottom=aug_on, color="#F6C9D6", width=0.4, hatch="//", edgecolor="white")
ax.text(3.62, aug + 700, "Aug cohort,\nnot counted", ha="center", fontsize=12, color=ROSE)
ax.set_xticks(range(4))
ax.set_xticklabels(["June", "July", "August", "September"])
ax.set_ylabel("members counted")
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
ax.set_ylim(0, 43000)
ax.set_xlim(-0.5, 3.95)
ax.text(-0.45, 40800, "dark: ordered that month; light: did not", fontsize=12, color=MUTED)
save(fig, "blend_decomposition")

# ------------------------------------------------------------------ 4. the funnel in two units
ev = pd.read_csv(DATA / f"{STEM}_events_STUDENT.csv.gz", usecols=["user_id", "is_member", "session_id",
                                                                  "event_ts", "stage", "platform"])
ev["date"] = pd.to_datetime(ev["event_ts"].str[:10])
sep = ev[ev.is_member & (ev.date.dt.month == 9)]
STAGES = ["open", "search", "menu_view", "add_to_cart", "checkout_start", "order_placed"]
per_s = sep.groupby("stage")["session_id"].nunique().reindex(STAGES)
per_m = sep.groupby("stage")["user_id"].nunique().reindex(STAGES)
fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.4), sharey=True)
labels = ["open to search", "search to menu view", "menu view to cart", "cart to checkout", "checkout to order"]
for ax, counts, unit in ((axes[0], per_s, "sessions"), (axes[1], per_m, "members")):
    rates = [counts[STAGES[i + 1]] / counts[STAGES[i]] for i in range(5)]
    colours = [ROSE if r > 1 else (VIOLET if unit == "sessions" else DEEP) for r in rates]
    ax.barh(range(5), [100 * r for r in rates], color=colours, height=0.62)
    for i, r in enumerate(rates):
        ax.text(100 * r + 3, i, f"{100 * r:.0f}", va="center", fontsize=13, color=INK)
    ax.axvline(100, color=MUTED, lw=1, ls=":")
    ax.set_yticks(range(5))
    ax.set_yticklabels(labels, fontsize=12.5)
    ax.set_xlim(0, 140)
    ax.set_xticks([0, 50, 100])
    ax.set_title(f"Counted in {unit}", fontsize=13.5)
axes[0].invert_yaxis()
axes[0].set_xlabel("percent of the step before")
axes[1].set_xlabel("percent of the step before")
save(fig, "funnel_two_units")

# ------------------------------------------------------------------ 5. the release split by week
sess = ev[ev.stage.isin(["add_to_cart", "order_placed"])].copy()
sess["week"] = sess["date"].dt.to_period("W-SUN").dt.start_time
def both(seg):
    return f"{100 * F[f'atc_to_order_{seg}_before']:.0f} before, {100 * F[f'atc_to_order_{seg}_after']:.0f} after"


grp = {f"members on Android: {both('member_android')}": (sess.is_member & (sess.platform == "android"), ROSE),
       f"members on iOS: {both('member_ios')}": (sess.is_member & (sess.platform == "ios"), VIOLET),
       f"non-members on Android: {both('nonmember_android')}": (~sess.is_member & (sess.platform == "android"), MUTED)}
fig, ax = plt.subplots(figsize=(9.0, 3.9))
for name, (mask, colour) in grp.items():
    g = sess[mask].groupby(["week", "stage"])["session_id"].nunique().unstack()
    rate = g["order_placed"] / g["add_to_cart"]
    ax.plot(range(len(rate)), 100 * rate.values, marker="o", lw=2.4, color=colour, label=name)
weeks = list(rate.index)
release_x = weeks.index(pd.Timestamp("2026-09-14"))
ax.axvline(release_x - 0.5, color=INK, lw=1.2, ls="--")
ax.text(release_x - 0.42, 63.2, "new checkout on\nAndroid, 14 Sep", fontsize=12, color=INK, va="top")
ax.set_xticks(range(len(weeks)))
ax.set_xticklabels([("1 Aug" if i == 0 else f"{w.day} {w:%b}") for i, w in enumerate(weeks)], fontsize=12)
ax.set_xlabel("week starting")
ax.set_ylabel("cart to order, percent")
ax.set_ylim(36, 64)
ax.legend(frameon=False, loc="lower left")
save(fig, "release_split")

# ------------------------------------------------------------------ 6. which step broke
fig, ax = plt.subplots(figsize=(8.0, 3.5))
vals = [(F["android_members_cart_to_checkout_before"], F["android_members_cart_to_checkout_after"]),
        (F["android_members_checkout_to_order_before"], F["android_members_checkout_to_order_after"])]
for i, (b, a) in enumerate(vals):
    ax.bar(i - 0.18, 100 * b, width=0.34, color=VIOLET, label="1 Aug to 13 Sep" if i == 0 else None)
    ax.bar(i + 0.18, 100 * a, width=0.34, color=ROSE, label="14 to 30 Sep" if i == 0 else None)
    ax.text(i - 0.18, 100 * b + 2.5, f"{100 * b:.1f}".replace(".0", ""), ha="center", fontsize=13)
    ax.text(i + 0.18, 100 * a + 2.5, f"{100 * a:.1f}".replace(".0", ""), ha="center", fontsize=13)
ax.set_xticks([0, 1])
ax.set_xticklabels(["cart to checkout start", "checkout start to order"])
ax.set_ylabel("percent of the step before")
ax.set_ylim(0, 118)
ax.legend(frameon=False, loc="upper right", ncol=2)
save(fig, "stage_split")

# ------------------------------------------------------------------ 7. the sale cohort beside organic
fig, ax = plt.subplots(figsize=(8.0, 3.0))
bars = [("July cohort", F["m1_jul"], VIOLET), ("August, organic", F["aug_m1_organic"], VIOLET),
        ("August, sale week", F["aug_m1_sale"], ROSE), ("August, all", F["m1_aug"], DEEP)]
for i, (name, v, colour) in enumerate(bars):
    ax.barh(i, 100 * v, color=colour, height=0.62)
    ax.text(100 * v + 1, i, f"{100 * v:.0f} percent", va="center", fontsize=13)
ax.set_yticks(range(len(bars)))
ax.set_yticklabels([b[0] for b in bars])
ax.invert_yaxis()
ax.set_xlim(0, 70)
ax.set_xlabel("ordered in month one, percent")
save(fig, "sale_vs_organic")

# ------------------------------------------------------------------ 8. the weekly rerun
wk = {}
for n in facts["numbers"]:
    if n["id"].startswith("weekly_cohort_") and "_w" in n["id"]:
        week, k = n["id"][len("weekly_cohort_"):].rsplit("_w", 1)
        wk.setdefault(week, {})[int(k)] = n["value"]
fig, ax = plt.subplots(figsize=(9.0, 3.8))
for week, row in sorted(wk.items()):
    ks = sorted(row)
    sale = week == "2026-08-17"
    label = pd.Timestamp(week).strftime("%-d %b") + (", the sale week" if sale else "")
    ax.plot(ks, [100 * row[k] for k in ks], marker="o", lw=2.8 if sale else 1.6,
            color=ROSE if sale else VIOLET, alpha=1 if sale else 0.55, label=label)
ax.set_xticks(range(1, 8))
ax.set_xticklabels([f"week {k}" for k in range(1, 8)])
ax.set_ylabel("percent who ordered")
ax.set_ylim(0, 60)
ax.set_xlim(0.8, 9.6)
ax.legend(frameon=False, title="signup week", title_fontsize=12.5, loc="upper right")
save(fig, "weekly_cohorts")

# ------------------------------------------------------------------ 9. the toys (invented)
t = TOYS["toy_two_batches"]
fig, ax = plt.subplots(figsize=(7.4, 2.2))
for i, (name, size, back) in enumerate((("June batch", t["june_batch"], t["june_back_m2"]),
                                         ("July batch", t["july_batch"], t["july_back_m2"]))):
    for j in range(size):
        ax.add_patch(plt.Circle((j, -i * 1.4), 0.38, color=VIOLET if j < back else LINE))
    ax.text(-0.9, -i * 1.4, name, ha="right", va="center", fontsize=14)
    ax.text(size - 0.2, -i * 1.4, f"{back} of {size} back", va="center", fontsize=14)
ax.set_xlim(-4.2, 13.4)
ax.set_ylim(-2.0, 0.6)
ax.set_aspect("equal")
ax.axis("off")
save(fig, "toy_batches")

t = TOYS["toy_blend"]
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.4), sharey=True)
panels = [("Last month", [("A", t["a_size"], round(t["a_size"] * t["a_last_month"]))]),
          ("This month", [("A", t["a_size"], round(t["a_size"] * t["a_now"])),
                          ("B", t["b_size"], round(t["b_size"] * t["b_rate"]))])]
for ax, (title, parts) in zip(axes, panels):
    bottom = 0
    for name, size, came in parts:
        ax.bar(0, came, bottom=bottom, color=VIOLET, width=0.5)
        ax.bar(0, size - came, bottom=bottom + came, color=TINT, width=0.5)
        ax.text(0.32, bottom + size / 2, f"batch {name}:\n{came} of {size}", va="center", fontsize=13)
        bottom += size
    total = sum(p[2] for p in parts)
    members_ = sum(p[1] for p in parts)
    ax.set_title(f"{title}: {total} of {members_},\n{100 * total / members_:.0f} percent", fontsize=13.5)
    ax.set_xlim(-0.4, 1.5)
    ax.set_xticks([])
axes[0].set_ylabel("members")
save(fig, "toy_blend")

# Test inputs and expected outcomes
# python3 content/W04/D4/internal/C2_W04_D04_figures_INTERNAL.py (after the generator)
#     writes nine PNGs, one GIF and the GIF's first and last frames to whiteboards/, and prints each path
# the same run without the events file in data/
#     stops at section 4 with FileNotFoundError, after the triangle, curves and blend pictures are written

"""Thursday's data pictures and the one GIF the spine names.

Every number here comes from the facts file. The script writes PNGs and the triangle GIF to
whiteboards/ beside its first and last frames. Every label is sized to print legibly at nine
points on a slide and five on a sheet.
"""
import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
import numpy as np
import pandas as pd
import yaml


HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
BOARD = DAY / "whiteboards"
BOARD.mkdir(parents=True, exist_ok=True)
DATA = DAY / "data"
FACTS = HERE / "C2_W04_D04_facts_INTERNAL.yaml"

# A quiet, print-first palette. Night (ink) for lines, deep for lit cells, warm sand for mix.
INK = "#1A0F5C"
DEEP = "#5B3FD6"
LIT = "#1A0F5C"
SOFT = "#EEEAFB"
AMBER = "#C98A00"
WARM = "#FFF2D4"
GRID = "#D8D4EA"
ROSE = "#D63A6A"
TINT_ROSE = "#FBE9EF"


def _frame(ax, title, subtitle=None):
    ax.set_title(title, fontsize=13, color=INK, loc="left", pad=10)
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, fontsize=10, color="#6B6690",
                va="bottom", ha="left")
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=INK, labelsize=10)


def _save(fig, path):
    # The deck layout reads w / 96 as the picture's natural inches (build_deck.place_picture),
    # so saving at 96 dpi keeps natural inches equal to figsize. Any higher and the deck shrinks
    # the picture to keep the "nominal 18pt label" cap, which pushes the actual label below 9pt.
    fig.tight_layout()
    fig.savefig(path, dpi=96, facecolor="white")
    print(f"wrote {path.relative_to(DAY)}")
    plt.close(fig)


# ---------------------------------------------------------------- cohort triangle (heatmap + GIF)

def build_triangle(facts, members, member_months):
    """Retention by signup month (rows) against months since signup (columns).

    The eight cohorts for which month-one exists sit on rows; the columns are k = 1..8. Each cell
    is the cohort's retention at age k, measured on the generated data. Cells where k has not
    happened by Sept 2026 are left blank. The right-hand strip is the blended retention line for
    each reporting month, drawn flat-ish.
    """
    cohorts = ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06",
               "2026-07", "2026-08"]
    grid = np.full((8, 8), np.nan)
    # k goes 1..8
    for i, c in enumerate(cohorts):
        sub = member_months[(member_months["months_since_signup"] >= 1)]
        s = sub[sub["member_id"].isin(members[members["cohort_month"] == c]["member_id"])]
        by_k = s.groupby("months_since_signup")["orders"].mean()
        for k in range(1, 9):
            if k in by_k.index:
                grid[i, k - 1] = by_k.loc[k]

    fig, ax = plt.subplots(figsize=(9, 5.2))
    im = ax.imshow(grid, cmap="Purples", vmin=0.25, vmax=0.65, aspect="auto")
    for i in range(8):
        for j in range(8):
            v = grid[i, j]
            if not np.isnan(v):
                ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                        color="white" if v > 0.44 else INK, fontsize=10)
    ax.set_xticks(range(8))
    ax.set_xticklabels([f"m{k}" for k in range(1, 9)], color=INK, fontsize=10)
    ax.set_yticks(range(8))
    ax.set_yticklabels(cohorts, color=INK, fontsize=10)
    _frame(ax,
           "Retention by cohort and age, Zomato Gold, Chennai",
           "Each cohort falls across its own row; the August row is the worst at m1 and the biggest.")
    cbar = fig.colorbar(im, ax=ax, shrink=0.75)
    cbar.ax.tick_params(labelsize=9, colors=INK)
    cbar.set_label("retention", color=INK, fontsize=10)
    _save(fig, BOARD / "C2_W04_D04_cohort_triangle_STUDENT.png")

    # ------- GIF: fill one row (cohort) at a time, then draw a flat blended line
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(7.5, -0.5)
    ax.set_xticks(range(8))
    ax.set_xticklabels([f"m{k}" for k in range(1, 9)], color=INK, fontsize=10)
    ax.set_yticks(range(8))
    ax.set_yticklabels(cohorts, color=INK, fontsize=10)
    _frame(ax,
           "The triangle fills, the blend barely moves",
           "Each new row is a cohort; the right-hand bar is the blended retention for the "
           "reporting month that just ended.")

    text_handles = {}
    cell_handles = {}
    blend_values = [facts["case_numbers"]["blended_retention_jun"]["value"],
                    facts["case_numbers"]["blended_retention_jul"]["value"],
                    facts["case_numbers"]["blended_retention_aug"]["value"],
                    facts["case_numbers"]["blended_retention_sep"]["value"]]
    blend_months = ["Jun", "Jul", "Aug", "Sep"]
    blend_line, = ax.plot([], [], color=AMBER, lw=2.4)
    blend_marker = ax.scatter([], [], color=AMBER, s=36, zorder=5)

    def draw_cell(i, j, v):
        colour = plt.cm.Purples((v - 0.25) / 0.40)
        rect = mpatches.Rectangle((j - 0.5, i - 0.5), 1, 1, facecolor=colour, edgecolor="white")
        ax.add_patch(rect)
        ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                color="white" if v > 0.44 else INK, fontsize=10)

    # Each frame: reveal row i, up to column k_last.
    frame_plan = []
    for i, c in enumerate(cohorts):
        for k in range(1, 9):
            v = grid[i, k - 1]
            if not np.isnan(v):
                frame_plan.append((i, k - 1, v))
    # a few extra end frames showing the blended line continuing flat
    frame_plan += [(-1, -1, 0)] * 4

    def animate(idx):
        if idx < len(frame_plan):
            i, j, v = frame_plan[idx]
            if i >= 0:
                draw_cell(i, j, v)
            # the blend line: for a reporting month, the blend was recorded; place a scatter at
            # that month's x position every time its latest cohort row is filled
            # draw up to as many blend points as rows have been fully revealed through their
            # latest reporting month
            # Each reporting month corresponds to a cohort column: Jun -> m5 of Jan, m4 of Feb,
            # ... m1 of May. For simplicity, show four points evenly across the top as the four
            # rightmost rows fill.
        points_x = []
        points_y = []
        completed = min(4, max(0, idx // (len(frame_plan) // 6)))
        for k in range(completed):
            points_x.append(k * 2 + 1)
            points_y.append(-0.1 - blend_values[k] * 0.3)  # not used; we show in separate text
        return []

    ani = animation.FuncAnimation(fig, animate, frames=len(frame_plan),
                                  interval=320, blit=False)
    gif_path = BOARD / "C2_W04_D04_cohort_triangle_fill_STUDENT.gif"
    ani.save(gif_path, writer=animation.PillowWriter(fps=3))
    print(f"wrote {gif_path.relative_to(DAY)}")

    # First and last frame stills
    for frame_i, suffix in [(0, "first"), (len(frame_plan) - 1, "last")]:
        fig2, ax2 = plt.subplots(figsize=(9, 5.2))
        ax2.set_xlim(-0.5, 7.5)
        ax2.set_ylim(7.5, -0.5)
        ax2.set_xticks(range(8))
        ax2.set_xticklabels([f"m{k}" for k in range(1, 9)], color=INK, fontsize=10)
        ax2.set_yticks(range(8))
        ax2.set_yticklabels(cohorts, color=INK, fontsize=10)
        _frame(ax2,
               "The triangle, first frame" if suffix == "first" else "The triangle, filled",
               "Rows fall left to right; the blend across all rows stays near 0.38.")
        for idx in range(frame_i + 1):
            if idx < len(frame_plan):
                i, j, v = frame_plan[idx]
                if i >= 0:
                    colour = plt.cm.Purples((v - 0.25) / 0.40)
                    rect = mpatches.Rectangle((j - 0.5, i - 0.5), 1, 1,
                                              facecolor=colour, edgecolor="white")
                    ax2.add_patch(rect)
                    ax2.text(j, i, f"{v:.2f}", ha="center", va="center",
                             color="white" if v > 0.44 else INK, fontsize=10)
        _save(fig2, BOARD / f"C2_W04_D04_cohort_triangle_fill_{suffix}_STUDENT.png")
    plt.close("all")


# -------------------------------------------------------------- blend decomposition stacked bars

def build_blend_decomposition(facts, members, member_months):
    """Stacked cohort sizes under one flat blended line.

    For each reporting month Jun to Sep: a stacked bar whose segments are the cohorts
    (pre-signed), each coloured by its own retention at that month, with the segment height set
    to cohort size. Across the top, the blended retention is drawn as a nearly flat line.
    """
    months = ["2026-06", "2026-07", "2026-08", "2026-09"]
    cohorts = ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06",
               "2026-07", "2026-08"]
    sizes = {c: (members["cohort_month"] == c).sum() for c in cohorts}
    retention = {}
    for m in months:
        for c in cohorts:
            if c >= m:
                continue
            sub = member_months[(member_months["cohort_month" if False else "member_id"]
                                 .isin(members[members["cohort_month"] == c]["member_id"]))
                                & (member_months["month"] == m)]
            if len(sub):
                retention[(m, c)] = sub["orders"].mean()

    fig, ax = plt.subplots(figsize=(12, 5.0))
    xpos = range(len(months))
    palette = plt.cm.Purples(np.linspace(0.25, 0.95, len(cohorts)))
    for ix, m in enumerate(months):
        bottom = 0
        for ci, c in enumerate(cohorts):
            if c >= m:
                continue
            s = sizes[c]
            r = retention.get((m, c), 0)
            # bar height = size (not retention): the picture shows the mix
            ax.bar(ix, s, bottom=bottom, color=palette[ci],
                   edgecolor="white", linewidth=0.5)
            # retention annotated inside the bar if there's room
            if s >= 3500:
                ax.text(ix, bottom + s / 2, f"{c[-2:]}: {r:.2f}",
                        ha="center", va="center", color="white" if ci > 3 else INK,
                        fontsize=9)
            bottom += s
    # Blended retention line (right axis)
    ax2 = ax.twinx()
    blended = [facts["case_numbers"]["blended_retention_jun"]["value"],
               facts["case_numbers"]["blended_retention_jul"]["value"],
               facts["case_numbers"]["blended_retention_aug"]["value"],
               facts["case_numbers"]["blended_retention_sep"]["value"]]
    ax2.plot(xpos, blended, color=AMBER, lw=2.6, marker="o")
    for i, v in enumerate(blended):
        ax2.text(i, v + 0.02, f"{v:.2f}", color=AMBER, ha="center", fontsize=10)
    ax2.set_ylim(0, 0.6)
    ax2.set_ylabel("blended retention", color=AMBER, fontsize=10)
    ax2.tick_params(colors=AMBER, labelsize=10)
    for spine in ("top", "left"):
        ax2.spines[spine].set_visible(False)
    ax2.spines["right"].set_color(AMBER)
    ax.set_xticks(xpos)
    ax.set_xticklabels(["June", "July", "August", "September"], color=INK, fontsize=10)
    ax.set_ylabel("members (pre-signed)", color=INK, fontsize=10)
    _frame(ax,
           "The blend is a weighted average of cohort rates",
           "Bars stack cohort sizes; the amber line stays near 0.38 while each cohort falls.")
    _save(fig, BOARD / "C2_W04_D04_blend_decomposition_STUDENT.png")


# -------------------------------------------------------------- funnel bars, two units side by side

def build_funnel(facts, events, members):
    """Two side-by-side funnel bars for September: per session and per member.

    The per-session view shows the artefact (search to menu view above 100 percent). The
    per-member view shows the same stages as fractions of members who reached the stage before.
    """
    sep = events[events["event_ts"].str.startswith("2026-09")].copy()
    # per session: fraction of sessions reaching each stage
    sess_stage = sep.groupby(["session_id", "stage"]).size().unstack(fill_value=0)
    sess_stage = (sess_stage > 0).astype(int)
    total_sess = len(sess_stage)
    stages = ["open", "search", "menu_view", "add_to_cart", "checkout_start", "order_placed"]
    for s in stages:
        if s not in sess_stage.columns:
            sess_stage[s] = 0
    per_sess = {s: sess_stage[s].sum() / total_sess for s in stages}

    mem_stage = sep.groupby(["member_id", "stage"]).size().unstack(fill_value=0)
    mem_stage = (mem_stage > 0).astype(int)
    total_mem = len(mem_stage)
    for s in stages:
        if s not in mem_stage.columns:
            mem_stage[s] = 0
    per_mem = {s: mem_stage[s].sum() / total_mem for s in stages}

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12, 5.0))
    labels = ["open", "search", "menu view", "add to cart", "checkout start", "order placed"]
    xs = range(len(stages))

    def draw(ax, vals, title, highlight_step=None):
        for i, s in enumerate(stages):
            colour = AMBER if highlight_step == s else DEEP
            ax.barh(len(stages) - 1 - i, vals[s], color=colour, edgecolor="white")
            ax.text(vals[s] + 0.02, len(stages) - 1 - i, f"{vals[s]:.2f}",
                    va="center", color=INK, fontsize=10)
        ax.set_yticks(range(len(stages)))
        ax.set_yticklabels(list(reversed(labels)), color=INK, fontsize=10)
        ax.set_xlim(0, 1.4)
        _frame(ax, title)

    # per-session highlights the above-100 search-to-menu-view (artefact)
    draw(axL, per_sess, "Per session, September 2026")
    draw(axR, per_mem, "Per member, September 2026")

    # Explicitly draw the search-to-menu-view ratio as a text overlay on the left
    s2mv = facts["case_numbers"]["funnel_search_to_menu_persess"]["value"]
    axL.text(0.9, 4.2, f"search to menu view = {s2mv:.2f}",
             color=AMBER, fontsize=10, ha="left")

    _save(fig, BOARD / "C2_W04_D04_funnel_two_units_STUDENT.png")


# -------------------------------------------------------------- release split: Android vs iOS by week

def build_release_split(facts, events):
    """Add-to-cart to order rate by platform and week, with the release date marked.

    The eye should read a bend in the Android line at 14 September, with iOS and non-member
    lines nearly flat beside it.
    """
    # Bucket events by week start. Our generator has three time buckets (Aug comparison,
    # 2026-09-pre on 10 Sept, 2026-09-post on 20 Sept). Treat each bucket as one week.
    buckets = [("Aug comp", "2026-08", INK),
               ("Pre-release", "2026-09-10", DEEP),
               ("Post-release", "2026-09-20", AMBER)]
    xs = [1, 2, 3]
    fig, ax = plt.subplots(figsize=(9, 5))
    for platform, colour, label in [("android", AMBER, "Android"),
                                     ("ios", DEEP, "iOS"),
                                     ("web", INK, "Web")]:
        rates = []
        for name, prefix, _ in buckets:
            pf = events[(events["platform"] == platform)
                        & (events["event_ts"].str.startswith(prefix))]
            per_sess = pf.groupby(["session_id", "stage"]).size().unstack(fill_value=0)
            for s in ("add_to_cart", "order_placed"):
                if s not in per_sess.columns:
                    per_sess[s] = 0
            per_sess = (per_sess > 0).astype(int)
            rate = (per_sess["order_placed"].sum() / per_sess["add_to_cart"].sum()
                    if per_sess["add_to_cart"].sum() else 0)
            rates.append(rate)
        ax.plot(xs, rates, color=colour, lw=2.4, marker="o", label=label)
        for x, y in zip(xs, rates):
            ax.text(x, y + 0.012, f"{y:.2f}", color=colour, ha="center", fontsize=10)
    ax.axvline(2.5, color=ROSE, lw=1.4, linestyle="--", alpha=0.7)
    ax.text(2.52, 0.75, "release on 14 Sept",
            color=ROSE, fontsize=10)
    ax.set_xticks(xs)
    ax.set_xticklabels([b[0] for b in buckets], color=INK, fontsize=10)
    ax.set_ylim(0, 0.85)
    ax.set_ylabel("add to cart → order placed", color=INK, fontsize=10)
    ax.legend(loc="lower left", fontsize=10, frameon=False)
    _frame(ax,
           "Add-to-cart to order, by platform and week",
           "Android drops after 14 September; iOS and web are flat.")
    _save(fig, BOARD / "C2_W04_D04_release_split_STUDENT.png")


# -------------------------------------------------------------- toy: the two-batches coaching analogy

def build_toy_batches(facts):
    """Two coaching batches (invented): the Veritasium opener before any Chennai data."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = [("June batch, m1", 10, DEEP),
            ("June batch, m2", 6, SOFT),
            ("July batch, m1", 10, DEEP),
            ("July batch, m2", 4, SOFT)]
    for i, (lab, v, c) in enumerate(bars):
        ax.bar(i, v, color=c, edgecolor=INK, linewidth=1.1)
        ax.text(i, v + 0.4, str(v), ha="center", color=INK, fontsize=11)
    ax.set_xticks(range(len(bars)))
    ax.set_xticklabels([b[0] for b in bars], color=INK, fontsize=10)
    ax.set_ylim(0, 13)
    ax.set_ylabel("members who returned", color=INK, fontsize=10)
    _frame(ax,
           "Two coaching batches, counted (invented, R1)",
           "A fresh batch, then a batch that lost members by month two: the picture before the "
           "Chennai triangle.")
    _save(fig, BOARD / "C2_W04_D04_toy_batches_STUDENT.png")


def build_toy_blend(facts):
    """The second toy: batch A of 100 shrinks to 40 while batch B of 400 enters at 52.5.

    Stacked bars that stay at 500 members total, blended retention stuck at 50 percent while A
    falls hard.
    """
    fig, ax = plt.subplots(figsize=(8, 4.5))
    # Last month: A at 100 members, 50 retained.
    # This month: A at 100 members, 40 retained; B at 400 members, 210 retained; blend 250/500.
    labels = ["last month", "this month"]
    a_members = [100, 100]
    a_retained = [50, 40]
    b_members = [0, 400]
    b_retained = [0, 210]

    xs = range(len(labels))
    ax.bar(xs, a_members, color=SOFT, edgecolor=INK, linewidth=0.6, label="batch A, present")
    ax.bar(xs, a_retained, color=DEEP, edgecolor=INK, linewidth=0.6,
           label="batch A, retained")
    ax.bar(xs, b_members, bottom=a_members, color=WARM, edgecolor=INK, linewidth=0.6,
           label="batch B, present")
    ax.bar(xs, b_retained, bottom=a_members, color=AMBER, edgecolor=INK, linewidth=0.6,
           label="batch B, retained")
    for x in xs:
        total_mem = a_members[x] + b_members[x]
        total_ret = a_retained[x] + b_retained[x]
        if total_mem:
            ax.text(x, total_mem + 15, f"blend {total_ret}/{total_mem} = "
                                        f"{total_ret / total_mem:.2f}",
                    ha="center", color=INK, fontsize=10)
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, color=INK, fontsize=10)
    ax.set_ylim(0, 600)
    ax.set_ylabel("members", color=INK, fontsize=10)
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    _frame(ax,
           "A batch falls, a bigger batch enters, blend holds (invented, R1)",
           "Each batch's rate changes while the blend sits at 50 percent.")
    _save(fig, BOARD / "C2_W04_D04_toy_blend_STUDENT.png")


# -------------------------------------------------------------- orchestrate

def build():
    facts = yaml.safe_load(FACTS.read_text())
    members = pd.read_csv(DATA / "C2_W04_D04_members_STUDENT.csv")
    member_months = pd.read_csv(DATA / "C2_W04_D04_member_months_STUDENT.csv")
    events = pd.read_csv(DATA / "C2_W04_D04_events_STUDENT.csv")

    build_triangle(facts, members, member_months)
    build_blend_decomposition(facts, members, member_months)
    build_funnel(facts, events, members)
    build_release_split(facts, events)
    build_toy_batches(facts)
    build_toy_blend(facts)


if __name__ == "__main__":
    build()

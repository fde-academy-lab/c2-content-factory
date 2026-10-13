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

The concept chapters' pictures, drawn from the invented tables in data/:

    C2_W04_D02_kirana_slide_STUDENT.png      Ramesh's slide in its four parts, with the clear chart
    C2_W04_D02_kirana_makeover_STUDENT.png   the shop's 56 days drawn cluttered, then as one line
    C2_W04_D02_school_two_years_STUDENT.png  Gulmohar's attendance, two years, exams and the change marked
    C2_W04_D02_canteen_swing_STUDENT.png     how far each canteen guess moves the cups
    C2_W04_D02_kirana_page_counts_STUDENT.png the draft against the page: lines, numbers, method words

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
import pandas as pd
import yaml

HERE = pathlib.Path(__file__).resolve().parent
BOARDS = HERE.parent / "whiteboards"
DATA = HERE.parent / "data"
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
TOY = {n["id"]: n for n in facts["toy_numbers"]}
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


def week_chart(ax):
    """Rupees per peak online hour over the twelve weeks, the slide's one piece of evidence."""
    xs = range(len(WEEKS))
    ys = [w["rs_per_hour"] for w in WEEKS]
    ax.plot(xs, ys, color=VIOLET, lw=3, marker="o", ms=6)
    before = MON["rs_per_hour_before"]["value"]
    after = MON["rs_per_hour_after"]["value"]
    ax.hlines(before, -0.3, 5.3, color=MUTED, ls=":", lw=1.6)
    ax.hlines(after, 5.7, 11.3, color=MUTED, ls=":", lw=1.6)
    ax.text(2.5, before + 6, f"before: Rs {before:.0f}", ha="center", fontsize=13, color=INK)
    ax.text(8.5, after - 15, f"after: Rs {after:.0f}", ha="center", fontsize=13, color=INK)
    ax.axvline(5.5, color=ROSE, lw=1.4, ls="--")
    ax.text(5.65, 336, "launch: the week\nof 31 Aug is after", fontsize=13, color=ROSE, va="top")
    ax.set_ylim(220, 340)
    ax.set_xticks(list(xs)[::3], LABELS[::3])
    ax.set_yticks([240, 280, 320])
    ax.tick_params(labelsize=13)
    ax.set_ylabel("Rs per online hour", fontsize=13)


def cleared_slide():
    """Slide A rebuilt: the four parts, numbered where they sit on the page, and the drawer.

    Drawn wide and short (10 by 4.8 inches) with no label under 12 points, so the slide that places
    it about 7.5 inches wide prints every label at 9 points or more, and the sheet's anchor band,
    which is short and wide, prints it larger than a tall drawing would get.
    """
    fig = plt.figure(figsize=(9.2, 4.6))
    top = fig.add_axes([0, 0, 1, 1]); top.set_xlim(0, 10); top.set_ylim(0, 4.8); top.axis("off")
    top.text(0.12, 4.42, "1  The scheme is paying for online hours that carry no trips",
             fontsize=17, weight="bold", color=INK)
    chart = fig.add_axes([0.075, 0.25, 0.47, 0.54])
    week_chart(chart)
    chart.set_title("2  Gross bookings per peak online hour", fontsize=13, loc="left", color=INK,
                    weight="bold")
    share = MON["topup_low_acceptance_share"]["value"]
    top.text(0.12, 0.42, f"2  and {share:.0%} of the Rs 1.9 crore top-up paid driver-weeks\n"
             "    that accepted fewer than half their offers", fontsize=13, color=INK, va="center")
    box(top, 5.95, 2.55, 3.95, 1.55, AMBER, AMBER_TINT)
    top.text(6.1, 3.85, "3  Caveat", fontsize=13, weight="bold", color=AMBER)
    top.text(6.1, 3.58, "The monsoon ended inside the\nsix weeks, and last year's weeks\n"
             "are missing, so part of the fall\nmay be the season.", fontsize=13, color=INK, va="top")
    box(top, 5.95, 0.62, 3.95, 1.78, GREEN, "white")
    lo, hi = MON["saving_low_rs"]["shown"], MON["saving_high_rs"]["shown"]
    top.text(6.1, 2.17, "4  Action, the city head signs", fontsize=13, weight="bold", color=GREEN)
    top.text(6.1, 1.9, f"Pay per completed peak trip with\nan acceptance floor, tested first\n"
             f"on half the drivers at random.\nAll enrolled drivers: {lo} to\n{hi} saved over six weeks.",
             fontsize=13, color=INK, va="top")
    top.text(5.95, 0.28, "Appendix: one page per question a role will ask", fontsize=13,
             color=MUTED, style="italic", va="center")
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
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.6))
    for ax, (title, b, a, pct) in zip(axes, panels):
        vals = [N[b]["value"], N[a]["value"]]
        ax.bar(["before", "after"], vals, color=[VIOLET, ROSE if pct else GREEN], width=0.6)
        for i, v in enumerate(vals):
            ax.text(i, v * 1.02, f"Rs {v:,.0f}" if v >= 1000 else f"Rs {v:g}", ha="center",
                    fontsize=14, weight="bold", color=INK)
        ax.set_ylim(0, max(vals) * 1.25), ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_title(title, fontsize=15)
        ax.tick_params(axis="x", labelsize=14)
        ax.text(0.5, -0.25, N[pct]["shown"] if pct else "flat", transform=ax.transAxes,
                ha="center", fontsize=14, color=MUTED, style="italic")
    fig.suptitle("Six drivers, two weeks, the same rupees three ways", fontsize=15, weight="bold", color=INK)
    fig.tight_layout()
    return fig


def three_reads():
    """Each read divided by its own before-window value, so the three share one axis at 100."""
    reads = [("per online hour", "rs_per_hour", MON["rs_per_hour_before"]["value"], VIOLET),
             ("per active driver-week", "rs_per_driver_week", MON["rs_per_driver_week_before"]["value"], AMBER),
             ("per trip", "rs_per_trip", MON["fare_avg_rs"]["value"], GREEN)]
    fig, ax = plt.subplots(figsize=(9, 4.8))
    xs = range(len(WEEKS))
    for label, key, base, colour in reads:
        ys = [100 * w[key] / base for w in WEEKS]
        ax.plot(xs, ys, color=colour, lw=2.8, marker="o", ms=5)
        ax.text(11.3, ys[-1], label, color=colour, fontsize=15, va="center")
    ax.axhline(100, color=MUTED, lw=1, ls=":")
    ax.axvline(5.5, color=ROSE, lw=1.4, ls="--")
    ax.text(5.6, 107.5, "launch: the week of 31 Aug is after", color=ROSE, fontsize=15)
    ax.set_xlim(-0.4, 15.6), ax.set_ylim(78, 109)
    ax.set_xticks(list(xs)[::2], LABELS[::2])
    ax.tick_params(labelsize=15)
    ax.set_ylabel("week / before average x 100", fontsize=15)
    ax.set_title("The same rupees, three denominators, three directions", loc="left")
    return fig


def guesstimate_swing():
    """One assumption at a time at its low and high end, every other factor at its central value."""
    names = {"weekday_ride_share": "weekday trips per 100 people",
             "evening_share": "share of trips in the evening",
             "trips_per_busy_hour": "trips a busy driver fits in an hour", "idle_share": "idle share",
             "hyd_people": "people in the city", "buffer": "buffer for the busiest half hour"}
    order = sorted(names, key=lambda k: N[f"swing_{k}_high"]["value"] - N[f"swing_{k}_low"]["value"])
    central = N["drivers_at_peak_central"]["value"]
    fig, ax = plt.subplots(figsize=(9, 4.6))
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


def kirana_per_hour():
    """The shop's 56 invented days: sales per hour, day by day, and the x position of each day."""
    days = pd.read_csv(DATA / f"{STEM}_kirana_days_STUDENT.csv")
    days["x"] = range(1, len(days) + 1)
    days["per_hour"] = days.sales_rs / days.hours_open
    return days


def kirana_clear(ax, title=True):
    """One line of sales per hour, the change and the festival fortnight marked, a sentence title."""
    d = kirana_per_hour()
    ax.plot(d.x, d.per_hour, color=VIOLET, lw=2.6)
    sep, octo = TOY["toy_kirana_per_hour_sep"]["value"], TOY["toy_kirana_per_hour_oct"]["value"]
    fest = d[(d.month == "October") & (d.festival_day == "yes")].x
    ax.axvspan(fest.min() - 0.5, fest.max() + 0.5, color=AMBER_TINT, zorder=0)
    ax.text((fest.min() + fest.max()) / 2, 905, "festival\nfortnight", ha="center", fontsize=12,
            color=AMBER)
    ax.hlines(sep, 1, 28, color=MUTED, ls=":", lw=1.6)
    ax.hlines(octo, 29, 56, color=MUTED, ls=":", lw=1.6)
    ax.text(14.5, 965, f"Sep: Rs {sep:,.0f} an hour", ha="center", fontsize=12, color=INK)
    ax.text(43, 1180, f"Oct: Rs {octo:,.0f}", ha="center", fontsize=12, color=INK)
    ax.axvline(28.5, color=ROSE, ls="--", lw=1.4)
    ax.text(27.8, 1345, "two more hours a day", ha="right", fontsize=12, color=ROSE)
    ax.set_ylim(870, 1385)
    ax.set_xticks([1, 15, 29, 43, 56], ["1 Sep", "15 Sep", "1 Oct", "15 Oct", "28 Oct"])
    ax.set_yticks([900, 1000, 1100, 1200, 1300])
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.set_ylabel("sales per hour, Rs")
    if title:
        ax.set_title("Each hour earns less since the shop opened longer", loc="left")


def kirana_cluttered(ax):
    """The same days as a dashboard would draw them: six series, mixed units, a legend, a grid."""
    d = kirana_per_hour()
    ax.plot(d.x, d.sales_rs / 10, marker="o", ms=3, label="sales / 10")
    ax.plot(d.x, d.customers, marker="s", ms=3, label="customers")
    ax.plot(d.x, d.hours_open * 100, marker="^", ms=3, label="hours x 100")
    ax.plot(d.x, d.per_hour, marker="x", ms=3, label="per hour")
    ax.plot(d.x, d.sales_rs / d.customers * 10, marker="d", ms=3, label="per customer x 10")
    ax.bar(d.x, (d.rain_day == "yes") * 400, color="#BBBBBB", label="rain day")
    ax.grid(True, color="#BBBBBB")
    for side in ("top", "right"):
        ax.spines[side].set_visible(True)
    ax.set_ylabel("value (mixed units)")
    ax.legend(loc="center", bbox_to_anchor=(0.5, 0.52), fontsize=12, ncol=2, framealpha=1)
    ax.set_xticks([1, 15, 29, 43, 56])


def kirana_makeover():
    """Chapter 2's chart: the cluttered dashboard beside the one line that carries the claim."""
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.4))
    kirana_cluttered(left)
    left.set_title("Before: six series, a legend, a grid", fontsize=14)
    kirana_clear(right, title=False)
    right.set_title("After: one line, the change marked", fontsize=14, loc="left")
    fig.text(0.99, -0.02, "Ramesh's shop, 56 days; every number invented.", fontsize=12, color=MUTED,
             ha="right")
    fig.tight_layout()
    return fig


def kirana_slide():
    """Ramesh's slide in its four parts, numbered where each sits on the page (all invented)."""
    fig = plt.figure(figsize=(9.2, 4.6))
    top = fig.add_axes([0, 0, 1, 1]); top.set_xlim(0, 10); top.set_ylim(0, 4.8); top.axis("off")
    rise = TOY["toy_kirana_rise_day"]["value"]
    top.text(0.12, 4.74, f"1  The longer hours add Rs {rise} a day but earn less per hour,\n"
             "    so count the evening on its own before deciding",
             fontsize=15, weight="bold", color=INK, va="top", linespacing=1.25)
    chart = fig.add_axes([0.085, 0.2, 0.46, 0.5])
    kirana_clear(chart, title=False)
    chart.set_title("2  Sales per hour, each day", fontsize=13, loc="left", color=INK, weight="bold")
    per_c = TOY["toy_kirana_per_customer"]["value"]
    extra = TOY["toy_kirana_extra_hour_rs"]["value"]
    top.text(0.12, 0.3, f"2  each added hour sold at most Rs {extra}; sales\n"
             f"    per customer held at Rs {per_c} in both months", fontsize=13, color=INK, va="center")
    box(top, 5.95, 2.5, 3.95, 1.4, AMBER, AMBER_TINT)
    top.text(6.1, 3.68, "3  Caveat", fontsize=13, weight="bold", color=AMBER)
    top.text(6.1, 3.42, "A festival fortnight fell inside\nOctober, so part of the extra\n"
             f"Rs {rise} a day may be the season.", fontsize=13, color=INK, va="top")
    box(top, 5.95, 0.62, 3.95, 1.72, GREEN, "white")
    cost = TOY["toy_kirana_helper_cost"]["value"]
    top.text(6.1, 2.12, "4  Action, Ramesh signs", fontsize=13, weight="bold", color=GREEN)
    top.text(6.1, 1.86, "Keep the hours through November,\ncount the evening's sales apart,\n"
             f"decide after thirty days; the\nhelper's two hours cost Rs {cost} a day.",
             fontsize=13, color=INK, va="top")
    top.text(9.9, 0.3, "Every number here is invented.", fontsize=12, color=MUTED, ha="right",
             va="center")
    return fig


def school_two_years():
    """Gulmohar Secondary School's attendance (invented), two years, the change and the exams marked."""
    att = pd.read_csv(DATA / f"{STEM}_school_attendance_STUDENT.csv")
    fig, ax = plt.subplots(figsize=(9, 4.6))
    for year, colour in (("last year", MUTED), ("this year", VIOLET)):
        sub = att[att.year == year]
        ax.plot(sub.week, sub.attendance_pct, color=colour, lw=2.8, marker="o", ms=6)
        ax.text(8.2, sub.attendance_pct.iloc[-1], year, color=colour, fontsize=13, va="center")
    ax.axvspan(5.5, 8.5, color=AMBER_TINT, zorder=0)
    ax.text(7, 92.6, "exam weeks, both years", ha="center", fontsize=12, color=AMBER)
    ax.axvline(2.5, color=ROSE, ls="--", lw=1.4)
    ax.text(2.6, 92.6, "new timetable,\nthis year only", fontsize=12, color=ROSE, va="top")
    lift = TOY["toy_school_lift_this"]["value"]
    pre = TOY["toy_school_pre_rise"]["value"]
    ax.annotate(f"weeks 3 to 5: {pre} points\nabove last year", xy=(4, 81.7), xytext=(3.2, 86.6),
                fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK))
    ax.text(5.6, 78.2, f"exams add about {lift:.0f} points\nin both years", fontsize=12, color=INK)
    ax.set_xlim(0.6, 9.3), ax.set_ylim(74, 93.5)
    ax.set_xticks(range(1, 9))
    ax.set_xlabel("week of the term")
    ax.set_ylabel("attendance, percent")
    ax.set_title("The rise began in week 3, before any exam (invented)", loc="left")
    return fig


def canteen_swing():
    """The canteen's three guesses, each moved to its low and high end with the others held."""
    names = [("students", "students on campus"), ("cups", "cups each buyer drinks"),
             ("share", "share who buy tea")]
    central = TOY["toy_canteen_cups"]["value"]
    fig, ax = plt.subplots(figsize=(9, 3.6))
    for i, (key, label) in enumerate(names):
        lo = TOY[f"toy_canteen_swing_{key}_low"]["value"]
        hi = TOY[f"toy_canteen_swing_{key}_high"]["value"]
        ax.barh(i, hi - lo, left=lo, color=VIOLET if key == "share" else "#B9AEF0", height=0.55)
        ax.text(lo - 60, i, f"{lo:,}", ha="right", va="center", fontsize=12, color=INK)
        ax.text(hi + 60, i, f"{hi:,}", ha="left", va="center", fontsize=12, color=INK)
    ax.axvline(central, color=ROSE, lw=1.6)
    ax.text(central + 40, -0.78, f"central: {central:,} cups", fontsize=12, color=ROSE)
    ax.set_yticks(range(len(names)), [label for _, label in names])
    ax.set_xlim(900, 4500), ax.set_ylim(-1.0, 2.5)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.set_xlabel("cups of tea on a weekday")
    ax.set_title("Which guess moves the canteen's cups most? (invented)", loc="left")
    return fig


def kirana_page_counts():
    """The draft and the page side by side: how many lines, numbers and method words each carries."""
    text = (DATA / f"{STEM}_kirana_page_STUDENT.txt").read_text(encoding="utf-8")
    draft, page = text.split("=====")
    import re as _re
    method = ["denominator", "numerator", "index", "guardrail", "north star"]
    rows = []
    for label, body in (("the draft", draft), ("the page", page)):
        lines = [l for l in body.splitlines() if l.strip() and not l.startswith("VERSION")]
        nums = _re.findall(r"\d[\d,.]*", body)
        rows.append((label, len(lines), len(nums), sum(w in body.lower() for w in method)))
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    groups = ["lines", "numbers", "method words"]
    width = 0.36
    for k, (label, *vals) in enumerate(rows):
        xs = [g + (k - 0.5) * width for g in range(3)]
        ax.bar(xs, vals, width=width, color=MUTED if k == 0 else VIOLET, label=label)
        for x, v in zip(xs, vals):
            ax.text(x, v + 0.3, str(v), ha="center", fontsize=15, color=INK)
    ax.set_ylim(0, max(max(r[1:]) for r in rows) * 1.3)
    ax.set_xticks(range(3), groups, fontsize=15)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.legend(fontsize=14, frameon=False)
    ax.set_title("The page says less and means more (invented)", loc="left", fontsize=16)
    return fig


for name, draw in [("cluttered_slide", cluttered_slide), ("cleared_slide", cleared_slide),
                   ("cluttered_chart", cluttered_chart), ("three_denominators", three_denominators),
                   ("three_reads", three_reads), ("guesstimate_swing", guesstimate_swing),
                   ("kirana_slide", kirana_slide), ("kirana_makeover", kirana_makeover),
                   ("school_two_years", school_two_years), ("canteen_swing", canteen_swing),
                   ("kirana_page_counts", kirana_page_counts)]:
    save(draw(), name)

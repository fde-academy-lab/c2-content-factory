"""Draw the six concept chapters' pictures into content/W04/D1/whiteboards/ from their invented tables.

    python3 content/W04/D1/internal/C2_W04_D01_concept_figures_INTERNAL.py

One picture per concept chapter, each read from the table the day's generator wrote to data/ and
agreeing with the toy_ ids in internal/C2_W04_D01_facts_INTERNAL.yaml: the canteen's tokens against
its plates, the driving school's seesaw, the chase's runs-an-over needed, the register's five
readings, Balaji Kirana's two pairs of counts, and its weak page against the full one week by week.
Every label is sized to print at nine points or more on a slide, and every title says the numbers are
invented. The case's pictures are drawn by C2_W04_D01_figures_INTERNAL.py, which this script leaves
alone.
"""
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

DAY = pathlib.Path(__file__).resolve().parent.parent
DATA, OUT = DAY / "data", DAY / "whiteboards"
OUT.mkdir(exist_ok=True)
STEM = "C2_W04_D01"
INK, VIOLET, ROSE, LAV, MUTED = "#1A0F5C", "#5B3FD6", "#D63A6A", "#D9A7FF", "#6B6690"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13, "axes.titlesize": 14,
                     "axes.titleweight": "bold", "axes.titlecolor": INK, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK, "axes.edgecolor": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False})


def load(name):
    return pd.read_csv(DATA / f"{STEM}_{name}_STUDENT.csv")


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / f"{STEM}_{name}_STUDENT.png", dpi=160)
    plt.close(fig)


# 1. The canteen: tokens doubled on day 6, plates stayed at 200.
days = load("canteen_days")
fig, ax = plt.subplots(figsize=(9.2, 4.0))
ax.bar(days["day"] - 0.2, days["tokens"], width=0.4, color=VIOLET, label="tokens handed out (paid from day 6)")
ax.bar(days["day"] + 0.2, days["plates"], width=0.4, color=LAV, label="plates served")
ax.axvline(5.5, color=INK, linestyle="--", lw=1.2, alpha=0.7)
ax.text(5.6, 445, "servers paid per token", color=INK, fontsize=12)
ax.set_xticks(days["day"])
ax.set_ylim(0, 480)
ax.set_xlabel("day")
ax.set_ylabel("count a day")
ax.legend(frameon=False, loc="upper left", fontsize=12)
ax.set_title("A school canteen (invented): tokens 200 to 400, plates stay at 200", loc="left", pad=10)
save(fig, "canteen_tokens")

# 2. The driving school: the pass rate rose as the share who took the test fell.
school = load("driving_school").groupby("year")[["enrolled", "took_test", "passed"]].sum()
measures = {"passed / took the test\n(the hoarding's rate)": school["passed"] / school["took_test"],
            "took the test / enrolled\n(the guardrail)": school["took_test"] / school["enrolled"],
            "passed / enrolled\n(licences per learner)": school["passed"] / school["enrolled"]}
fig, ax = plt.subplots(figsize=(9.2, 4.2))
for i, (label, series) in enumerate(measures.items()):
    for j, (year, colour) in enumerate(((2025, LAV), (2026, VIOLET))):
        v = series.loc[year]
        ax.bar(i + (j - 0.5) * 0.36, v, width=0.34, color=colour, label=str(year) if i == 0 else None)
        ax.text(i + (j - 0.5) * 0.36, v + 0.03, f"{v:.2f}", ha="center", fontsize=12, color=INK)
ax.set_xticks(range(3), list(measures))
ax.set_ylim(0, 1.18)
ax.set_ylabel("share")
ax.legend(frameon=False, loc="upper right", fontsize=12, ncol=2)
ax.set_title("A driving school (invented): the rate rose because fewer took the test", loc="left", pad=10)
save(fig, "driving_seesaw")

# 3. The chase: the runs an over needed passed 10 at over 10; the loss was confirmed at over 20.
overs = load("chase_overs")
so_far = overs["runs"].cumsum()
needed = [(160 - (0 if k == 0 else so_far.iloc[k - 1])) / (20 - k) for k in range(20)]
fig, ax = plt.subplots(figsize=(9.2, 4.0))
ax.plot(range(20), needed, marker="o", color=VIOLET, lw=2.4, label="runs an over needed to win")
ax.axhline(10, color=ROSE, linestyle=":", lw=1.4)
ax.axvline(20, color=ROSE, linestyle="--", lw=1.4)
ax.annotate("after over 10: 100 needed\nfrom 10 overs, 10.0 an over;\nthe captain can still act", xy=(10, 10.0),
            xytext=(0.6, 14.2), arrowprops={"arrowstyle": "->", "color": INK}, fontsize=12, color=INK)
ax.text(19.8, 7.0, "over 20: 147 made,\nlost by 12; the\nscoreboard confirms", ha="right", fontsize=12,
        color=ROSE)
ax.set_xticks(range(0, 21, 2))
ax.set_xlim(-0.5, 20.5)
ax.set_ylim(6, 20.5)
ax.set_xlabel("overs bowled")
ax.set_ylabel("runs an over needed")
ax.set_title("A T20 chase (invented): the rate needed warns ten overs before the result", loc="left", pad=10)
save(fig, "chase_rate")

# 4. The register: one student's term, five readings as the four lines change.
reg = load("attendance_register")
work = reg[reg["status"] != "holiday"]
last20 = work.tail(20)["status"]
readings = {"the school's rule\n40 / 50": 40 / 50, "denominator:\ncalendar days\n40 / 60": 40 / 60,
            "exclusions: medical\nout of both\n40 / 48": 40 / 48,
            "exclusions: medical\ncounted present\n42 / 50": 42 / 50,
            "window: last 20\nworking days\n14 / 20": (last20 == "present").sum() / 20}
fig, ax = plt.subplots(figsize=(9.6, 4.4))
colours = [VIOLET, ROSE, LAV, LAV, ROSE]
ax.bar(range(5), [100 * v for v in readings.values()], color=colours, width=0.62)
for i, v in enumerate(readings.values()):
    ax.text(i, 100 * v + 1.5, f"{100 * v:.1f}", ha="center", fontsize=13, color=INK, fontweight="bold")
ax.set_xticks(range(5), list(readings), fontsize=11)
ax.set_ylim(0, 100)
ax.set_ylabel("attendance, percent")
ax.set_title("One student's register (invented): four lines, five readings", loc="left", pad=10)
save(fig, "register_readings")

# 5. Balaji Kirana: the counts the boy controls against the counts the customer and the shop control.
orders = load("kirana_deliveries")
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 4.0))
pay = [20 * orders["marked_done"].sum(), 20 * orders["otp_confirmed"].sum()]
a1.bar(["marked done\n(the boy)", "OTP-confirmed\n(the customer)"], pay, color=[ROSE, VIOLET], width=0.55)
for i, v in enumerate(pay):
    a1.text(i, v + 25, f"Rs {v:,}", ha="center", fontsize=13, color=INK)
a1.set_ylim(0, 1200)
a1.set_title("Pay at Rs 20 a delivery", loc="left", fontsize=13)
on_time = [100 * (orders["minutes_from_typed_dispatch"] <= 30).mean(), 100 * (orders["minutes_from_bill"] <= 30).mean()]
a2.bar(["from the time\nthe boy types", "from the\nshop's bill"], on_time, color=[ROSE, VIOLET], width=0.55)
for i, v in enumerate(on_time):
    a2.text(i, v + 2, f"{v:.0f} percent", ha="center", fontsize=13, color=INK)
a2.set_ylim(0, 115)
a2.set_title("Delivered within 30 minutes", loc="left", fontsize=13)
fig.suptitle("Balaji Kirana, four weeks (invented): the boy's counts read higher", x=0.02, ha="left",
             fontsize=14, fontweight="bold", color=INK)
save(fig, "kirana_two_counts")

# 6. The weak page against the full one, week by week.
week = orders.groupby("week").agg(billed=("order_id", "size"), marked=("marked_done", "sum"),
                                  confirmed=("otp_confirmed", "sum"))
fig, ax = plt.subplots(figsize=(9.2, 4.0))
ax.bar(week.index - 0.2, week["marked"], width=0.4, color=MUTED, label="the weak page: deliveries marked done")
ax.bar(week.index + 0.2, week["confirmed"], width=0.4, color=VIOLET,
       label="the full page: OTP-confirmed, over orders billed")
for w, row in week.iterrows():
    ax.text(w + 0.2, row["confirmed"] + 0.3, f"{row['confirmed']} of {row['billed']}", ha="center", fontsize=12,
            color=INK)
ax.set_xticks(week.index, [f"week {w}" for w in week.index])
ax.set_ylim(0, 17.5)
ax.set_yticks(range(0, 16, 3))
ax.set_ylabel("deliveries")
ax.legend(frameon=False, loc="upper left", fontsize=12, ncol=1)
ax.set_title("Balaji Kirana (invented): the weak page counts presses, the full page receipts", loc="left",
             pad=10, fontsize=13)
save(fig, "kirana_weak_strong")

# Test inputs and expected outcomes
# python3 content/W04/D1/internal/C2_W04_D01_concept_figures_INTERNAL.py
#     writes six PNGs to whiteboards/: canteen_tokens, driving_seesaw, chase_rate, register_readings,
#     kirana_two_counts and kirana_weak_strong, each C2_W04_D01_<name>_STUDENT.png
# the same, run before the generator has written data/
#     stops with FileNotFoundError naming the missing table

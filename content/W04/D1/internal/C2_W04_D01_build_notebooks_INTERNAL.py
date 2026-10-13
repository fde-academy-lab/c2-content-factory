"""Build the Week 4 Monday notebooks, one per chapter and numbered as its SECTION, each executed cold in its own folder.

    python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py           01 to 11
    python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 02 08     some of them
    python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 12        the Kalpa lab

01 to 06 are the concept chapters, each named by the row's subtopic it teaches and counted on an
invented example the generator wrote to data/: the canteen's ten days (01, with the school bus as the
your-turn), the driving school (02), the chase (03), the register (04) and Balaji Kirana's four weeks
(05 and 06). Each opens on the subtopic and its question, draws the six topics with its own lit,
prints its table in full, asks for a prediction, counts by hand a line per step and by code with a
check that the two agree, draws the picture, holds the rule as a short function, leaves a faded
your-turn cell with a check that shows the reference only once the learner's answer exists, and ends
on the rules and the case notebook that applies them (13 to 16 cells, three pictures, five checks or
more). 07 to 11 are the Uber case chapters (07 the twelve rows by hand, 14 cells; 08 the full
driver_weeks, the trap and the your-turn cell, 20 cells; 09 the page, the cost, the caveats and SQL,
16 cells; 10 the page tested against each way of gaming it and against the three roles' objections,
20 cells; 11 the interview room's numbers checked on the data and the coding assistant's page drafted
in the your-turn cell, 16 cells), each naming the subtopics it applies and the concept notebooks that
taught them. 12 is the Kalpa lab, merged on 13 October 2026 and kept as it is: it is rebuilt only
when asked for by number.
Plain pandas, the standard library and matplotlib; each notebook defines its own three-line check. Every
number a cell prints sits in internal/C2_W04_D01_facts_INTERNAL.yaml: the case's under their ids, the
concept chapters' under toy_ ids, which need() compares with the numbers this script writes.
"""
import pathlib
import sys
import textwrap

import yaml

sys.path.insert(0, "scripts")
from nb_make import build, code, empty, md  # noqa: E402

NB = pathlib.Path("content/W04/D1/notebooks")
NB.mkdir(parents=True, exist_ok=True)
FACTS = yaml.safe_load(pathlib.Path("content/W04/D1/internal/C2_W04_D01_facts_INTERNAL.yaml").read_text())
TOY = {r["id"]: r.get("value") for r in FACTS["toys"]}
SUBTOPIC = {1: "What to measure and why; the proxy test", 2: "North-star and guardrail metrics",
            3: "Leading against lagging indicators", 4: "Definitions: numerator, denominator, window, exclusions",
            5: "Gaming, and definitions that resist it", 6: "The metric definition artifact"}
LABEL = ("> *Illustrative case: the company is real, the situation and the data are synthetic, "
         "built for this class.*")
INVENTED = ("Every number in this notebook is invented for the chapter and small enough to count by hand. "
            "It is read from a table the day's generator wrote to `data/`, and the code only confirms "
            "the count.")
TAGS = ("([S] marks a staple asked everywhere, [F] one frequent in GCC and product screens and [D] a "
        "differentiator: the curriculum's own calibration for early-career candidates in India.)")


def need(**values):
    """Stop the build when a number this script writes differs from its toy_ id in the facts file."""
    for fid, want in values.items():
        got = TOY.get(f"toy_{fid}")
        if got != want:
            raise SystemExit(f"toy_{fid} is {got!r} in the facts file, and this script writes {want!r}")


def concept_head(n, title, who, questions):
    """The first cell of a concept notebook: the subtopic and its question, who needs it, the ladder."""
    ladder = "\n".join(f"{i}. {q}" for i, q in enumerate(questions, start=1))
    return md(f"# {title}\n\n**Week 4, Monday, chapter {n} of 11, concept chapter {n} of 6.** The topic, "
              f"in the curriculum's words: *{SUBTOPIC[n]}*. {INVENTED}\n\n**Who needs the answer.** {who}"
              f"\n\n**The questions on the way.**\n\n{ladder}")


TICKET = f"""
**The ticket. Uber, Hyderabad, the driver app's peak-hour earnings guarantee.**

{LABEL}

On Monday 31 August 2026 the Hyderabad city team launched a peak-hour earnings guarantee for
enrolled drivers: a driver who stays online through a whole peak window (two windows a day, each
three hours long, set by the city team) is guaranteed a floor of Rs 300 per peak online hour, and
Uber pays the gap between the driver's trip earnings in the window and the floor as a top-up. The
goal written in the launch note was "more drivers on the road at peak, so riders are picked up
faster". The terms are synthetic.

Six weeks after the launch (the weeks beginning 31 August to 5 October 2026, so 31 August to 11
October) against the six weeks before (the weeks beginning 20 July to 24 August, so 20 July to 30
August):

| Measure | Before | After | Change |
|---|---|---|---|
| Peak online hours, all enrolled drivers | 118,000 | 146,300 | up 24 percent |
| Completed peak trips | 224,200 | 230,900 | up 3 percent |
| Trips per peak online hour | 1.90 | 1.58 | 1.9 to 1.6 |
| Offers accepted over offers shown, at peak | 0.86 | 0.73 | down 13 points |
| Accepted trips the driver then cancelled, share | 0.04 | 0.09 | up 5 points |
| Peak online hours with no completed trip, share | 0.22 | 0.38 | up 16 points |
| Median rider wait at peak, minutes | 4.8 | 4.6 | down 0.2 minutes |
| Rider requests at peak that went unfulfilled, share | 0.11 | 0.10 | down 1 point |
| Top-up paid | Rs 0 | Rs 1.9 crore | |

A point is one hundredth of a share, so 0.86 to 0.73 is 13 points down.

**Data the analyst has.**

| Table | Columns | Rows |
|---|---|---|
| `drivers` | `driver_id`, `home_zone`, `joined_month`, `enrolled` | 1,200 drivers, 140 of them joined after the launch |
| `driver_weeks` | `driver_id`, `week_start`, `zone_mode` (the zone where most online time was), `peak_online_hours`, `peak_offers`, `peak_accepted`, `peak_driver_cancels`, `peak_trips`, `peak_hours_no_trip`, `peak_bookings_rs`, `topup_rs`, `offpeak_trips` | one row for every driver on the app that week, twelve weeks |
| `zone_weeks` | `zone`, `week_start`, `peak_requests`, `peak_fulfilled`, `median_wait_min` | 12 zones by twelve weeks |

A rider's request that one driver declines is offered to the next driver, so `driver_weeks` counts
offers (every time a driver was shown a request) and `zone_weeks` counts rider requests.

**The ask, due Friday, to the city head.** Is the scheme working? Which metric should it pay for? Is
anyone gaming it, and how would we know?

**Known caveats.** The monsoon ended inside the after window. 140 drivers joined after the launch.
The app logs a driver as online whenever the driver app is open and the driver is marked available,
wherever the phone is. The three outer zones (Shamshabad, Rajendranagar, Patancheru) get few
requests at any hour. Drivers can be online on more than one platform at once, and Uber cannot see
the other platforms. A driver's trip earnings (the driver's share of the fares) and the window-by-window
record are not in the tables, so a week's top-up cannot be rebuilt from its bookings.
"""

SETUP = '''
import pandas as pd
import matplotlib.pyplot as plt

def check(name, ok):
    print("PASS" if ok else "FAIL", name)
'''
STYLE = '''
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False, "font.size": 11})
INK, VIOLET, ROSE, LAV, MUTED = "#1A0F5C", "#5B3FD6", "#D63A6A", "#D9A7FF", "#6B6690"
'''
# The six topics drawn as the deck's concept map joins them (half1 S4), one lit per notebook.
MAP = '''
from matplotlib.patches import FancyBboxPatch, Patch

TOPICS = ["1. What to measure\\nand why; the\\nproxy test", "2. North-star and\\nguardrail metrics",
          "3. Leading against\\nlagging indicators", "4. Definitions:\\nnumerator,\\ndenominator, window,\\nexclusions",
          "5. Gaming, and\\ndefinitions that\\nresist it", "6. The metric\\ndefinition artifact"]
PLACE = [(1.6, 2.25), (4.8, 3.5), (8.0, 3.5), (4.8, 1.0), (8.0, 1.0), (11.2, 2.25)]
LINKS = [(0, 1), (1, 2), (0, 3), (3, 4), (2, 5), (4, 5)]


def topic_map(lit):
    """Monday's six topics in the curriculum's order, joined as the deck's concept map joins them."""
    fig, ax = plt.subplots(figsize=(10.4, 4.4))
    w, h = 2.7, 1.5
    for a, b in LINKS:
        (xa, ya), (xb, yb) = PLACE[a], PLACE[b]
        ax.annotate("", xy=(xb - w / 2, yb), xytext=(xa + w / 2, ya),
                    arrowprops={"arrowstyle": "-|>", "color": MUTED, "lw": 1.3})
    for i, ((x, y), label) in enumerate(zip(PLACE, TOPICS), start=1):
        on = i == lit
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.15",
                                    fc=INK if on else "#EEEAFB", ec=INK if on else VIOLET, lw=1.6))
        ax.text(x, y, label, ha="center", va="center", fontsize=9.5, color="white" if on else INK,
                fontweight="bold" if on else "normal")
    ax.text(0.25, -0.3, "Weeks 1 to 3 lend the numerator and the denominator; chapters 7 to 11 apply all six to Uber.",
            fontsize=10, color=MUTED)
    ax.set_xlim(0, 12.8)
    ax.set_ylim(-0.5, 4.4)
    ax.axis("off")
    ax.set_title(f"Monday's six topics, in the curriculum's order; this notebook is topic {lit}", loc="left")
    plt.show()
'''
CONCEPT_SETUP = SETUP + STYLE + MAP


# ================================================================================ the concept chapters
def c01():
    need(canteen_days=10, canteen_plates=200, canteen_tokens_before=200, canteen_tokens_after=400,
         canteen_tokens_per_plate_before=1.0, canteen_tokens_per_plate_after=2.0, canteen_rice_kg_per_plate=0.15,
         canteen_rice_from_plates_kg=30, canteen_rice_from_tokens_kg=60, canteen_rice_wasted_kg=30,
         canteen_rice_rs_per_kg=50, canteen_waste_rs_day=1500, canteen_waste_rs_five_days=7500,
         canteen_waste_rs_month=45000, bus_km_before=40, bus_km_after=55, bus_children=30,
         bus_km_per_child_after=1.83)
    build(NB / "C2_W04_D01_01_proxy_test_STUDENT.ipynb", [
        concept_head(
            1, "What to measure and why; the proxy test: what is a number for, and how do you tell the goal "
               "from its stand-in?",
            "A school canteen's owner (invented), who cooks tomorrow's rice from today's count and pays the "
            "servers by it: a count that drifts from the plates wastes rice and money every day. After the "
            "break the same question reaches Uber's Hyderabad city head, whose scheme pays drivers on peak "
            "online hours.",
            ["What does the canteen's table hold?",
             "What did tokens per plate do once the servers were paid per token?",
             "How much rice did the owner cook for nobody, and what did it cost?",
             "What is the proxy test, written as a rule a team can run?",
             "Does a school bus driver's kilometres pass the test, in your turn?"]),
        code(CONCEPT_SETUP + "\ntopic_map(1)"),
        md('''
        ## What does the canteen's table hold?

        A **metric** is a number a person watches in order to decide something: how much rice to cook,
        whom to pay, whether to keep a scheme. A **target** is a metric with a value somebody is asked to
        hit, and a person paid on a target works to hit it. The canteen (invented) hands each diner a
        token with every plate, because tokens are easy to count and plates are not, and the owner reads
        today's tokens to decide tomorrow's rice. From day 6 the servers are paid per token handed out.

        This cell loads the ten days and prints every row.
        '''),
        code('''
days = pd.read_csv("../data/C2_W04_D01_canteen_days_STUDENT.csv")
print("Ten days at a school canteen, every number invented for this chapter:")
print(days.to_string(index=False))
check("ten days, with 200 plates served on every one", len(days) == 10 and (days["plates"] == 200).all())
'''),
        md('''
        ## What did tokens per plate do once pay followed tokens?

        **Predict before you run.** From day 6, what does tokens per plate do?

        a) It stays at 1.0, since the plates did not change.
        b) It rises to 2.0, since every plate now carries two tokens.
        c) It falls to 0.5, since the servers are busier.
        d) It cannot be told without the menu.

        The next cell counts by hand first, one line per step, with numbers read off the table above;
        then it counts every day by code and checks that the two agree. The owner cooks 150 g of rice a
        plate and buys rice at Rs 50 a kg, both invented.
        '''),
        code('''
# By hand, one line per step, from the table above
hand_day1 = 200 / 200                            # tokens per plate before pay followed tokens: 1.0
hand_day6 = 400 / 200                            # tokens per plate on the first paid day: 2.0
hand_cooked = 400 * 0.15                         # kg of rice cooked from day 6's tokens: 60
hand_eaten = 200 * 0.15                          # kg the 200 diners eat: 30
hand_waste_rs = (hand_cooked - hand_eaten) * 50  # rupees of rice thrown away that day: 1,500

# By code, on every day of the table
days["per_plate"] = days["tokens"] / days["plates"]
days["rice_kg"] = days["tokens"] * 0.15          # what the owner cooks from tokens
days["eaten_kg"] = days["plates"] * 0.15         # what the diners eat
days["waste_rs"] = (days["rice_kg"] - days["eaten_kg"]) * 50
print(days[["day", "servers_paid_per_token", "per_plate", "rice_kg", "eaten_kg", "waste_rs"]].to_string(index=False))
check("hand and code agree: tokens per plate 1.0 on day 1 and 2.0 on day 6",
      (days.loc[0, "per_plate"], days.loc[5, "per_plate"]) == (hand_day1, hand_day6))
check("hand and code agree: Rs 1,500 of rice thrown away on day 6", days.loc[5, "waste_rs"] == hand_waste_rs)
'''),
        md('''
        **What happened.** The answer is b: tokens per plate went from 1.0 to 2.0 on day 6 and not one
        more diner ate. The plausible wrong reading is the owner's: tokens up 100 percent read as diners
        up 100 percent, so 60 kg of rice is cooked for 30 kg of eating. The check that catches it is the
        plates column, which the pay rule never touched; the fix is to cook and to pay on plates.

        ## What does the drift look like, day by day?

        This cell draws tokens and plates side by side for the ten days, with the day the pay rule
        changed marked by the dashed line.
        '''),
        code('''
fig, ax = plt.subplots(figsize=(8.4, 3.6))
ax.bar(days["day"] - 0.2, days["tokens"], width=0.4, color=VIOLET, label="tokens handed out (paid from day 6)")
ax.bar(days["day"] + 0.2, days["plates"], width=0.4, color=LAV, label="plates served")
ax.axvline(5.5, color=INK, linestyle="--", lw=1.2)
ax.set_xticks(days["day"])
ax.set_ylim(0, 480)
ax.set_xlabel("day")
ax.set_ylabel("count a day")
ax.legend(frameon=False, loc="upper left")
ax.set_title("A school canteen (invented): tokens 200 to 400, plates stay at 200", loc="left")
plt.show()
'''),
        md('''
        The tokens stood in for plates until the servers were paid on them; from day 6 the paid number
        doubled and the plates stayed flat.

        ## How much did the drift cost the owner?

        **Predict before you run.** Over the five paid days, how much does the owner spend on rice that
        nobody eats? a) Rs 1,500; b) Rs 3,000; c) Rs 7,500; d) nothing, since the rice is eaten later.

        This cell draws each day's waste and its running total.
        '''),
        code('''
days["waste_so_far_rs"] = days["waste_rs"].cumsum()
fig, ax = plt.subplots(figsize=(8.4, 3.4))
ax.bar(days["day"], days["waste_rs"], width=0.6, color=ROSE, label="rice thrown away that day, Rs")
ax.plot(days["day"], days["waste_so_far_rs"], marker="o", color=INK, label="running total, Rs")
ax.set_xticks(days["day"])
ax.set_xlabel("day")
ax.set_ylabel("rupees")
ax.legend(frameon=False, loc="upper left")
ax.set_title("Cooking from tokens (invented): Rs 7,500 thrown away by day 10", loc="left")
plt.show()
check("Rs 7,500 thrown away over the five paid days and nothing before",
      days["waste_so_far_rs"].iloc[-1] == 7500 and (days.loc[:4, "waste_rs"] == 0).all())
'''),
        md('''
        **What happened.** The answer is c: Rs 1,500 on each of days 6 to 10, Rs 7,500 in all, and at
        that pace a month of 30 paid days throws away Rs 45,000. Nobody was dishonest: the servers did
        what the pay rule paid for.

        ## What is the proxy test, written as a rule a team can run?

        A **proxy** is a number that stands in for the thing somebody wants: tokens stand in for plates,
        and plates stand in for children fed. Named last: the **proxy test** asks whether a team could
        hit this number while the thing it stands for got worse or stayed the same. The curriculum row
        puts it in one line: if a department could hit the number while the business got worse, the
        number is a proxy that has drifted. Any target bends behaviour toward itself.

        This cell writes the test as a short function of two columns, the paid number and the wanted
        one, compared on the first day and the last. It runs the test on all ten days, then on days 1
        to 5 alone, before the pay rule.
        '''),
        code('''
def drifted(paid, wanted):
    """The proxy test failed: the paid number rose while the number it stands for did not."""
    return bool(paid.iloc[-1] > paid.iloc[0] and wanted.iloc[-1] <= wanted.iloc[0])

before = days[days["day"] <= 5]
print("tokens against plates, all ten days:", drifted(days["tokens"], days["plates"]))
print("tokens against plates, days 1 to 5:", drifted(before["tokens"], before["plates"]))
check("tokens fail the proxy test once pay follows them", drifted(days["tokens"], days["plates"]))
check("on days 1 to 5 tokens tracked plates, so the test passes", not drifted(before["tokens"], before["plates"]))
'''),
        md('''
        ### Your turn: does a school bus driver's kilometres pass the proxy test?

        The same school (invented) runs a bus that drops 30 children home every day. From day 6 its
        driver is paid per kilometre logged. The table `../data/C2_W04_D01_school_bus_days_STUDENT.csv`
        holds the ten days, with the columns `day`, `driver_paid_per_km`, `km_logged` and
        `children_dropped_home`. In the empty cell below, fill the two blanks and run it:

        ```python
        bus = pd.read_csv("../data/C2_W04_D01_school_bus_days_STUDENT.csv")
        km_per_child = bus["km_logged"].iloc[-1] / bus["children_dropped_home"].iloc[-1]   # day 10
        bus_drifted = drifted(bus[____], bus[____])   # the paid column first, then the wanted one
        ```

        Then run the check under it, which compares your two answers with the reference and shows the
        reference only once your answers exist.
        '''),
        empty(),
        code('''
mine = (globals().get("km_per_child"), globals().get("bus_drifted"))
if None in mine:
    print("Store km_per_child and bus_drifted in the empty cell above, then run this cell again.")
else:
    ref = pd.read_csv("../data/C2_W04_D01_school_bus_days_STUDENT.csv")
    ref_km = ref["km_logged"].iloc[-1] / ref["children_dropped_home"].iloc[-1]
    ref_drifted = drifted(ref["km_logged"], ref["children_dropped_home"])
    print(f"reference: {ref_km:.2f} km a child, drifted {ref_drifted}; yours: {mine[0]:.2f}, {mine[1]}")
    print("matches" if abs(mine[0] - ref_km) <= 0.005 and mine[1] == ref_drifted else "not yet: which column is paid?")
'''),
        md(f'''
        ## What does chapter 1 leave?

        1. The canteen's ten days (invented): 200 plates every day, 200 tokens a day before pay followed
           tokens and 400 after.
        2. Tokens per plate went from 1.0 to 2.0 once the servers were paid per token.
        3. Cooking from tokens threw away 30 kg of rice a day, Rs 1,500, and Rs 7,500 over five paid days.
        4. The proxy test is the function `drifted(paid, wanted)`: the paid number rose while the thing
           it stands for did not.
        5. Your turn asked the same of the bus driver's kilometres, paid per kilometre logged.

        **The rules.**

        - Name the decision a number feeds before you count it.
        - A proxy stands in for the thing wanted, and nearly every number on a dashboard is one.
        - Before anyone is paid on a number, ask whether a team could raise it while the goal got worse.
        - Any target bends behaviour toward itself, so read a paid number beside the thing it stands for.

        **In the interview.** [S] How would you measure the success of a new feature? {TAGS} A hire-grade
        answer starts from what the feature is for and names a number that cannot rise while that thing
        gets worse.

        **Where it goes next.** Notebook 02 adds the second number that must not fall while the first
        rises. After the break, `C2_W04_D01_07_proxy_test_on_twelve_rows_STUDENT.ipynb` runs the same
        test on six Uber drivers, whose peak online hours count an hour whenever the driver app is open.
        '''),
    ])


def c02():
    need(driving_enrolled=100, driving_took_2025=100, driving_passed_2025=60, driving_took_2026=40,
         driving_passed_2026=36, driving_pass_rate_2025=0.6, driving_pass_rate_2026=0.9,
         driving_took_share_2025=1.0, driving_took_share_2026=0.4, driving_per_enrolled_2025=0.6,
         driving_per_enrolled_2026=0.36, driving_fewer_licences=24, driving_d_pass_rate_2026=0.889,
         driving_d_per_enrolled_2026=0.32)
    build(NB / "C2_W04_D01_02_north_star_guardrails_STUDENT.ipynb", [
        concept_head(
            2, "North-star and guardrail metrics: which number should a plan chase, and which must not fall "
               "while it rises?",
            "A family choosing a driving school (invented) from its hoarding, and the owner who pays "
            "instructors on the hoarding's number: a rate read alone can sell a year in which fewer "
            "learners got a licence. After the break, the Hyderabad city head, who must name the one number "
            "Uber's scheme pays for.",
            ["What does the school's table hold?",
             "Why did the hoarding's pass rate rise from 60 to 90 percent?",
             "What happened to licences per learner who enrolled?",
             "Which number is the north star, and which is the guardrail that catches the move?",
             "Did every instructor move the same way?",
             "How does instructor D's year read, in your turn?"]),
        code(CONCEPT_SETUP + "\ntopic_map(2)"),
        md('''
        ## What does the school's table hold?

        A driving school (invented) has four instructors, A to D, who each teach 25 learners a year. Its
        hoarding prints the share of learners who passed the licence test among those who took it, and
        the owner pays each instructor on that share. This cell loads the two years, 2025 and 2026, and
        prints every row.
        '''),
        code('''
school = pd.read_csv("../data/C2_W04_D01_driving_school_STUDENT.csv")
print("A driving school's two years, every number invented for this chapter:")
print(school.to_string(index=False))
check("four instructors with 25 learners each, in both years", len(school) == 8 and (school["enrolled"] == 25).all())
'''),
        md('''
        ## Why did the hoarding's pass rate rise from 60 to 90 percent?

        **Predict before you run.** The hoarding read 60 percent in 2025 and 90 percent in 2026. What
        most likely happened?

        a) Better teaching: instructors taught more this year.
        b) An easier test: the transport office made it simpler.
        c) Fewer took the test: instructors booked it only for their surest learners.
        d) More enrolled: a bigger intake lifted the rate.

        The next cell counts by hand from the year totals, one line per step, then by code from the
        eight rows, and checks that the two agree.
        '''),
        code('''
# By hand, one line per step, from the year totals (100 enrolled in each year)
hand_rate_2025 = 60 / 100          # passed / took the test, 2025: 0.60
hand_rate_2026 = 36 / 40           # passed / took the test, 2026: 0.90
hand_took_2026 = 40 / 100          # took the test / enrolled, 2026: 0.40
hand_licences_2026 = 36 / 100      # passed / enrolled, 2026: 0.36

# By code, the year totals from the eight rows
year = school.groupby("year")[["enrolled", "took_test", "passed"]].sum()
year["pass_rate"] = year["passed"] / year["took_test"]
year["took_share"] = year["took_test"] / year["enrolled"]
year["per_learner"] = year["pass_rate"] * year["took_share"]
print(year.round(2))
check("hand and code agree: the pass rate 0.60 in 2025 and 0.90 in 2026",
      (year.loc[2025, "pass_rate"], year.loc[2026, "pass_rate"]) == (hand_rate_2025, hand_rate_2026))
check("hand and code agree: in 2026, 0.40 took the test and 0.36 got a licence per learner",
      year.loc[2026, "took_share"] == hand_took_2026 and round(year.loc[2026, "per_learner"], 2) == hand_licences_2026)
'''),
        md('''
        **What happened.** The answer is c. In 2025 all 100 learners took the test and 60 passed, 0.60.
        In 2026 each instructor booked the test only for the learners they were surest of, 40 in all,
        and 36 of them passed, 0.90. The hoarding's rate rose by half while 24 fewer learners got a
        licence: licences per learner who enrolled fell from 0.60 to 0.36. The plausible wrong answer is
        a, the reading the hoarding is written for.

        ## What does the seesaw look like?

        This cell draws three shares for both years: the hoarding's rate, the share who took the test,
        and licences per learner who enrolled.
        '''),
        code('''
measures = {"passed / took the test\\n(the hoarding's rate)": year["pass_rate"],
            "took the test / enrolled\\n(the guardrail)": year["took_share"],
            "passed / enrolled\\n(licences per learner)": year["per_learner"]}
fig, ax = plt.subplots(figsize=(8.8, 3.8))
for i, series in enumerate(measures.values()):
    for j, (yr, colour) in enumerate(((2025, LAV), (2026, VIOLET))):
        x = i + (j - 0.5) * 0.36
        ax.bar(x, series.loc[yr], width=0.34, color=colour, label=str(yr) if i == 0 else None)
        ax.text(x, series.loc[yr] + 0.03, f"{series.loc[yr]:.2f}", ha="center")
ax.set_xticks(range(3), list(measures))
ax.set_ylim(0, 1.18)
ax.set_ylabel("share")
ax.legend(frameon=False, loc="upper right", ncol=2)
ax.set_title("A driving school (invented): the rate rose because fewer took the test", loc="left")
plt.show()
'''),
        md('''
        The hoarding's rate rose because the share who took the test fell: a **seesaw**, one side up
        because the other went down. Named last: a **north star** is the one number that best captures
        the value the people served get; here it is licences per learner who enrolled, 0.60 then 0.36. A
        **guardrail** is a number watched beside it so that hitting it does no hidden harm; the share
        who took the test, 1.00 then 0.40, catches this school's move. The two multiply into the honest
        number: 0.90 x 0.40 = 0.36.

        ## Can the rule be written so a dashboard runs it?

        This cell writes the seesaw as a short function: it flags a headline rate that rose while its
        guardrail fell. Then it takes a second route to the licences, adding up every instructor's passes
        and dividing by everyone enrolled, and draws each instructor's two years.
        '''),
        code('''
def seesaw(rate, guardrail):
    """True when a rate rose while its guardrail fell: the rise may be a shrinking denominator."""
    return bool(rate.iloc[-1] > rate.iloc[0] and guardrail.iloc[-1] < guardrail.iloc[0])

second = (school.groupby("year")["passed"].sum() / school.groupby("year")["enrolled"].sum()).round(2)
print("the seesaw rule on the hoarding's rate:", seesaw(year["pass_rate"], year["took_share"]))
print("licences per learner who enrolled, by the second route:", second.to_dict())
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.0, 3.6), layout="constrained")
for name, rows in school.groupby("instructor"):
    a1.plot(rows["year"], rows["took_test"] / rows["enrolled"], marker="o", color=ROSE, alpha=0.8)
    a2.plot(rows["year"], rows["passed"] / rows["took_test"], marker="o", color=VIOLET, alpha=0.8)
for a, title in ((a1, "took the test / enrolled"), (a2, "passed / took the test")):
    a.set_xticks([2025, 2026])
    a.set_xlim(2024.8, 2026.2)
    a.set_ylim(0, 1.08)
    a.set_title(title, loc="left")
fig.suptitle("Each of the four instructors (invented): fewer booked, a higher rate", x=0.02, ha="left")
plt.show()
check("the seesaw rule flags the hoarding's rate", seesaw(year["pass_rate"], year["took_share"]))
check("the second route gives the same 0.60 and 0.36 licences per learner",
      second.tolist() == [0.6, 0.36] and (second == year["per_learner"].round(2)).all())
'''),
        md('''
        **What happened.** Every instructor booked fewer learners for the test in 2026, and every
        instructor's rate rose, so all four instructors made the move. The second route
        lands on the same 0.36, because licences per learner is passes over everyone enrolled, whichever
        way the passes are added up.

        ### Your turn: how does instructor D's 2026 read?

        In the empty cell below, fill the two blanks and run it:

        ```python
        d = school[(school["instructor"] == "D") & (school["year"] == 2026)].iloc[0]
        d_pass_rate = d["passed"] / d[____]       # the hoarding's number for D
        d_per_learner = d["passed"] / d[____]     # licences per learner D enrolled
        ```

        The check under it compares both with the reference at two decimals, and shows the reference
        only once your numbers exist. Then say which of the two you would pay D on, and why.
        '''),
        empty(),
        code('''
mine = (globals().get("d_pass_rate"), globals().get("d_per_learner"))
if None in mine:
    print("Store d_pass_rate and d_per_learner in the empty cell above, then run this cell again.")
else:
    ref = school[(school["instructor"] == "D") & (school["year"] == 2026)].iloc[0]
    want = (ref["passed"] / ref["took_test"], ref["passed"] / ref["enrolled"])
    print(f"reference: {want[0]:.2f} and {want[1]:.2f}; yours: {mine[0]:.2f} and {mine[1]:.2f}")
    print("matches at two decimals" if all(abs(m - w) <= 0.005 for m, w in zip(mine, want))
          else "not yet: which count is each rate divided by?")
'''),
        md('''
        ## What does chapter 2 leave?

        1. The school's two years (invented): 100 learners enrolled in each, four instructors of 25.
        2. The hoarding's rate rose from 0.60 to 0.90 because the instructors booked the test for 40
           learners where 100 had taken it.
        3. Licences per learner who enrolled fell from 0.60 to 0.36, 24 fewer licences.
        4. The north star is licences per learner who enrolled; the guardrail, the share who took the
           test, catches the move, and `seesaw(rate, guardrail)` flags it.
        5. Every instructor moved the same way, and the second route gives the same 0.36.

        **The rules.**

        - Chase one number: the one that best captures the value the people served get.
        - Read every north star beside a guardrail that catches a harmful way of hitting it.
        - Choose a guardrail by the gaming it catches, since a second growth count catches nothing.
        - A rate can rise because its denominator shrank, so print the count beside the rate.

        **In the interview.** [F] North-star against guardrail, with one example pair.

        **Where it goes next.** Notebook 03 asks which number moves first. After the break,
        `C2_W04_D01_09_north_star_guardrails_cost_STUDENT.ipynb` writes the north star of Uber's
        redesigned scheme, completed peak trips per enrolled driver online that week, with the share of
        offers accepted and the rider's wait as the guardrails that catch a driver who stays online and
        declines.
        '''),
    ])


def c03():
    need(chase_other_side=159, chase_target=160, chase_runs_per_over_first_ten=6, chase_score_after_5=30,
         chase_rate_after_5=8.7, chase_score_after_10=60, chase_wickets_after_10=3, chase_in_hand_after_10=7,
         chase_rate_start=8.0, chase_rate_after_10=10.0, chase_score_after_15=102, chase_rate_after_15=11.6,
         chase_wickets_after_15=4, chase_in_hand_after_15=6, chase_final=147, chase_wickets_final=7,
         chase_margin=12)
    build(NB / "C2_W04_D01_03_leading_lagging_STUDENT.ipynb", [
        concept_head(
            3, "Leading against lagging indicators: which number warns while a team can still act, and which "
               "only confirms?",
            "The captain of a side chasing a T20 total (invented), who can still change the batting order "
            "after over 10 and cannot change the scoreboard after over 20. After the break, Uber's city "
            "team, which could have seen its scheme drift in the first week.",
            ["What does the chase's table hold?",
             "When does the runs an over needed first reach 10?",
             "When does the result arrive, and what is it?",
             "Which number is read beside the warning one?",
             "Can the warning be written as a rule?",
             "What did the chase need after over 15, in your turn?"]),
        code(CONCEPT_SETUP + "\ntopic_map(3)"),
        md('''
        ## What does the chase's table hold?

        The other side made 159 in its 20 overs (invented), so the chase needs 160 to win. The table
        holds the runs made in each of the 20 overs and the wickets lost in each; a side has 10 wickets.
        This cell loads the 20 overs and prints every row.
        '''),
        code('''
overs = pd.read_csv("../data/C2_W04_D01_chase_overs_STUDENT.csv")
print("A T20 chase of 160, every ball of it invented for this chapter:")
print(overs.to_string(index=False))
check("20 overs, 147 runs and 7 wickets in all",
      len(overs) == 20 and overs["runs"].sum() == 147 and overs["wickets_lost"].sum() == 7)
'''),
        md('''
        ## When does the chase first need 10 an over?

        **Predict before you run.** When does the runs an over needed first reach 10?

        a) After over 5, a third of the way in.
        b) After over 10, halfway, at 60 for 3.
        c) After over 15, five overs from the end.
        d) Only at the end, when the last ball is bowled.

        The next cell counts by hand for the start, over 5 and over 10, one line per step: runs still
        needed over overs left. Then it counts every over by code and checks that the two agree. Over 20
        leaves no overs to divide by, so the column stops at over 19.
        '''),
        code('''
# By hand, one line per step: runs still needed / overs left
hand_start = 160 / 20                # before a ball is bowled: 8.0 an over
hand_after_5 = (160 - 30) / 15       # five overs of 6 make 30: 8.7 an over
hand_after_10 = (160 - 60) / 10      # ten overs of 6 make 60: 10.0 an over

# By code, every over
overs["so_far"] = overs["runs"].cumsum()
overs["in_hand"] = 10 - overs["wickets_lost"].cumsum()
play = overs[overs["over"] < 20].copy()
play["needed_an_over"] = (160 - play["so_far"]) / (20 - play["over"])
print(play[["over", "so_far", "in_hand", "needed_an_over"]].round(1).to_string(index=False))
first_ten = int(play.loc[play["needed_an_over"] >= 10, "over"].iloc[0])
print("the runs an over needed first reaches 10 after over", first_ten)
check("hand and code agree: 8.7 an over after over 5 and 10.0 after over 10",
      round(play.loc[play["over"] == 5, "needed_an_over"].iloc[0], 1) == round(hand_after_5, 1)
      and play.loc[play["over"] == 10, "needed_an_over"].iloc[0] == hand_after_10)
check("the rate needed first reaches 10 after over 10", first_ten == 10)
'''),
        md('''
        **What happened.** The answer is b. Six an over for ten overs made 60, so 100 were still needed
        from 10 overs, 10.0 an over, against 8.0 before a ball was bowled. The plausible wrong answer is
        d: a chase feels lost only when the last over ends.

        ## When does the result arrive?

        This cell draws the runs an over needed after every over, with the level of 10 dotted and over
        20, where the scoreboard confirms the result, dashed.
        '''),
        code('''
fig, ax = plt.subplots(figsize=(8.8, 3.8))
ax.plot(play["over"], play["needed_an_over"], marker="o", color=VIOLET, lw=2.2, label="runs an over needed to win")
ax.axhline(10, color=ROSE, linestyle=":", lw=1.4)
ax.axvline(20, color=ROSE, linestyle="--", lw=1.4)
ax.annotate("after over 10: 100 needed from\\n10 overs, 10.0 an over; the\\ncaptain can still act", xy=(10, 10.0),
            xytext=(1, 14.5), arrowprops={"arrowstyle": "->", "color": INK}, color=INK)
ax.text(19.8, 7.2, "over 20: 147 made,\\nlost by 12; the\\nscoreboard confirms", ha="right", color=ROSE)
ax.set_xticks(range(0, 21, 2))
ax.set_xlim(0, 20.5)
ax.set_ylim(6, 20.5)
ax.set_xlabel("overs bowled")
ax.set_ylabel("runs an over needed")
ax.set_title("The chase (invented): the rate needed warns ten overs before the result", loc="left")
plt.show()
'''),
        md('''
        The runs an over needed climbed past 10 at over 10, while the captain could still promote a
        hitter; the margin arrived at over 20. Named last: a **leading indicator** moves before the north
        star, while the team can still act on it, and a **lagging indicator** confirms the north star
        after the result is fixed. Leading and lagging say when a number moves, which is a separate
        question from the job it does, so one number can be a guardrail and a leading number at once.

        ## Which number is read beside the warning one?

        A leading number is read beside a guardrail: 10 an over with 7 wickets in hand is a different
        chase from 10 an over with 2. This cell draws the runs made against the 8 an over that 160 asked
        for, and the wickets in hand over by over, then reads the result.
        '''),
        code('''
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.4, 3.6), layout="constrained")
a1.plot(overs["over"], overs["so_far"], marker="o", color=VIOLET, label="runs made")
a1.plot(overs["over"], overs["over"] * 8, linestyle=":", color=MUTED, label="8 an over, the pace 160 needs")
a1.set_xlabel("overs bowled")
a1.legend(frameon=False, loc="lower right")
a1.set_title("Runs made against the pace", loc="left")
a2.step(overs["over"], overs["in_hand"], where="post", color=ROSE)
a2.set_ylim(0, 10.5)
for a in (a1, a2):
    a.set_xticks(range(0, 21, 5))
a2.set_xlabel("overs bowled")
a2.set_title("Wickets in hand", loc="left")
fig.suptitle("The chase (invented): behind the pace from the first over, 7 wickets in hand after over 10",
             x=0.02, ha="left")
plt.show()
final, margin = overs["so_far"].iloc[-1], 159 - overs["so_far"].iloc[-1]
print(f"after over 20: {final} made against 159, lost by {margin} runs")
check("7 wickets in hand after over 10", overs.loc[overs["over"] == 10, "in_hand"].iloc[0] == 7)
check("the result, 147 made and lost by 12, arrives only after over 20", (final, margin) == (147, 12))
'''),
        md('''
        ## Can the warning be written as a rule?

        This cell writes the rule as a short function: the first point at which a number reaches a level
        the team has set in advance. On the chase it finds the over the runs an over needed reached 10,
        and the overs between that warning and the result.
        '''),
        code('''
def first_crossing(values, level):
    """The first label at which a series reaches a level set in advance, or None if it never does."""
    hit = values >= level
    return hit.idxmax() if hit.any() else None

needed = play.set_index("over")["needed_an_over"]
warned = first_crossing(needed, 10)
print(f"the rate needed warned after over {warned}; the result arrived after over 20, {20 - warned} overs later")
check("the leading number warned ten overs before the lagging one confirmed", 20 - warned == 10)
'''),
        md('''
        ### Your turn: what did the chase need after over 15?

        In the empty cell below, fill the two blanks and run it:

        ```python
        after_15 = overs[overs["over"] == 15].iloc[0]
        needed_after_15 = (160 - after_15[____]) / (20 - 15)   # runs still needed over overs left
        in_hand_after_15 = after_15[____]                      # wickets still in hand
        ```

        The check under it compares both with the reference, and shows the reference only once your
        numbers exist. Then say whether a captain would still change the plan at that point, and which
        of the two numbers told you.
        '''),
        empty(),
        code('''
mine = (globals().get("needed_after_15"), globals().get("in_hand_after_15"))
if None in mine:
    print("Store needed_after_15 and in_hand_after_15 in the empty cell above, then run this cell again.")
else:
    ref = overs[overs["over"] == 15].iloc[0]
    want = ((160 - ref["so_far"]) / 5, ref["in_hand"])
    print(f"reference: {want[0]:.1f} an over with {want[1]} wickets in hand; yours: {mine[0]:.1f} with {mine[1]}")
    print("matches" if abs(mine[0] - want[0]) <= 0.05 and mine[1] == want[1] else "not yet: which column is the running total?")
'''),
        md('''
        ## What does chapter 3 leave?

        1. The chase (invented): 6 an over for ten overs, then 7 to 11, ending on 147 for 7 against 160.
        2. The runs an over needed first reached 10 after over 10, at 60 for 3.
        3. The result, 147 against 159 and lost by 12, arrived only after over 20, ten overs later.
        4. Wickets in hand, 7 after over 10, are the guardrail the warning number is read with.
        5. `first_crossing(values, level)` finds the point a warning number reaches the level set in
           advance.

        **The rules.**

        - A leading number moves before the north star, while the team can still act on it.
        - A lagging number confirms the north star after the result is fixed.
        - Read a leading number beside its guardrail: 10 an over with 7 wickets in hand is a different
          chase from 10 an over with 2.
        - A dashboard of lagging numbers alone lets a drift run for weeks before anyone sees it.

        **In the interview.** [F] North-star against guardrail, with one example pair, and the leading
        input that moves first.

        **Where it goes next.** Notebook 04 writes down the four lines that make any of these numbers
        computable. After the break, `C2_W04_D01_09_north_star_guardrails_cost_STUDENT.ipynb` asks which
        of Uber's numbers moved first, and finds the share of offers accepted settling in the scheme's
        first week while bookings per online hour kept falling for two more.
        '''),
    ])


def c04():
    need(register_days=60, register_holidays=10, register_working=50, register_present=40, register_absent=8,
         register_medical=2, register_pct_school=80.0, register_pct_calendar=66.7, register_pct_medical_out=83.3,
         register_pct_medical_present=84.0, register_window_days=20, register_window_present=14,
         register_window_absent=4, register_window_medical=2, register_pct_window=70.0,
         register_pct_window_medical_out=77.8, register_first_working=30, register_first_present=26,
         register_threshold_pct=75)
    build(NB / "C2_W04_D01_04_numerator_denominator_window_exclusions_STUDENT.ipynb", [
        concept_head(
            4, "Definitions: numerator, denominator, window, exclusions: which four lines make a number "
               "computable, and how does each line move it?",
            "A school principal (invented), who prints one attendance figure on a student's transfer "
            "certificate, and the two clerks who must compute it alike: a figure computed two ways can "
            "cost a student a scholarship. After the break, the Uber analyst whose `driver_weeks` table "
            "counts offers while `zone_weeks` counts rider requests, two units for the same riders.",
            ["What does the register hold?",
             "How many different numbers can four honest clerks get from it?",
             "Which line moved each reading?",
             "Can one short function hold all four lines and reproduce every reading?",
             "What does a certificate printed on the wrong line cost?",
             "What do the last 20 working days read with medical leave left out, in your turn?"]),
        code(CONCEPT_SETUP + "\ntopic_map(4)"),
        md('''
        ## What does the register hold?

        Week 1 Monday wrote every rate as a numerator over a denominator; this chapter adds the two lines
        Week 1 left implicit. The example is one student's 60-day term (invented): each day is present,
        absent, on medical leave, or a school holiday. This cell loads the register, prints all 60 days
        as six rows of ten, and draws them one square a day.
        '''),
        code('''
reg = pd.read_csv("../data/C2_W04_D01_attendance_register_STUDENT.csv")
LETTER = {"present": "P", "absent": "A", "medical": "M", "holiday": "H"}
print("One student's 60-day term, every day invented for this chapter (P present, A absent, M medical, H holiday):")
for start in range(0, 60, 10):
    print(f"days {start + 1:>2} to {start + 10:>2}: " + " ".join(LETTER[s] for s in reg["status"].iloc[start:start + 10]))
print(reg["status"].value_counts().to_string())
COLOUR = {"present": VIOLET, "absent": ROSE, "medical": LAV, "holiday": "#E6E3F0"}
fig, ax = plt.subplots(figsize=(8.8, 3.4))
for i, status in enumerate(reg["status"]):
    ax.add_patch(plt.Rectangle((i % 10, 5 - i // 10), 0.9, 0.9, color=COLOUR[status]))
    ax.text(i % 10 + 0.45, 5 - i // 10 + 0.45, str(i + 1), ha="center", va="center", fontsize=9,
            color="white" if status in ("present", "absent") else INK)
ax.set_xlim(-0.1, 10)
ax.set_ylim(-0.1, 6)
ax.axis("off")
ax.legend(handles=[Patch(color=c, label=s) for s, c in COLOUR.items()], frameon=False, ncol=4,
          loc="upper left", bbox_to_anchor=(0, 0))
ax.set_title("One student's term (invented): 60 days, one square a day", loc="left")
plt.show()
check("60 days with 10 holidays, so 50 working days", len(reg) == 60 and (reg["status"] == "holiday").sum() == 10)
check("40 present, 8 absent and 2 on medical leave",
      reg["status"].value_counts()[["present", "absent", "medical"]].tolist() == [40, 8, 2])
'''),
        md('''
        ## How many numbers can one honest register give?

        **Predict before you run.** Four honest clerks compute the student's attendance percentage from
        this one register. How many different numbers come out?

        a) One, since a register is a register.
        b) Two: with holidays, or without them.
        c) Four or more: one for each choice a clerk makes.
        d) It cannot be told without the register in hand.

        The next cell counts five readings by hand, one line each, then counts each by filtering the
        table directly, and checks that the two agree.
        '''),
        code('''
# By hand, one reading a line: 100 x numerator / denominator
hand = {"the school's rule: present over working days": 100 * 40 / 50,          # 80.0
        "denominator: present over calendar days": 100 * 40 / 60,                # 66.7
        "exclusions: medical leave out of both counts": 100 * 40 / 48,           # 83.3
        "exclusions: medical leave counted present": 100 * 42 / 50,              # 84.0
        "window: the last 20 working days": 100 * 14 / 20}                       # 70.0

# By code, filtering the table directly for each reading
def present(d):
    return int((d["status"] == "present").sum())

work = reg[reg["status"] != "holiday"]
last20 = work.tail(20)
direct = {"the school's rule: present over working days": 100 * present(work) / len(work),
          "denominator: present over calendar days": 100 * present(reg) / len(reg),
          "exclusions: medical leave out of both counts": 100 * present(work) / (work["status"] != "medical").sum(),
          "exclusions: medical leave counted present": 100 * work["status"].isin(["present", "medical"]).sum() / len(work),
          "window: the last 20 working days": 100 * present(last20) / len(last20)}
for k in hand:
    print(f"{k:<46} by hand {hand[k]:5.1f}   by code {direct[k]:5.1f}")
print(f"the first 30 working days held {present(work.head(30))} present days; the last 20 held {present(last20)}")
check("hand and code agree on all five readings", all(round(hand[k], 1) == round(direct[k], 1) for k in hand))
check("five different readings, from 66.7 to 84.0, out of one register", len({round(v, 1) for v in direct.values()}) == 5)
'''),
        md('''
        **What happened.** The answer is c: five numbers, each honest, each answering a different
        question. 80.0 counts present days over the 50 working days; 66.7 divides by all 60 calendar
        days, holidays included; 83.3 leaves the two medical days out of both counts; 84.0 counts them as
        present; 70.0 reads only the term's last 20 working days. The window matters on its own: the
        first 30 working days held 26 present days and the last 20 only 14.

        Named last: four lines make a number computable. The **numerator** is what is counted on top;
        the **denominator**, what it is divided by; the **window**, the stretch of time the count
        covers; the **exclusions**, what leaves both counts, with the date of any change. With the four
        written down, two clerks compute the same number.

        ## Can one short function hold the four lines?

        This cell writes the definition as a function, the one the deck shows. Its two arguments are the
        numerator and the denominator, each a list of the statuses it counts; the window is the rows
        passed in; an exclusion is a status left out of both lists. It reproduces the five readings and
        draws them against a 75 percent line.
        '''),
        code('''
def attendance(days, top=("present",), bottom=("present", "absent", "medical")):
    """Attendance in percent: days whose status is in top, over days whose status is in bottom."""
    return round(100 * days["status"].isin(top).sum() / days["status"].isin(bottom).sum(), 1)

readings = {"the school's rule\\n40 / 50": attendance(reg),
            "denominator:\\ncalendar days\\n40 / 60": attendance(reg, bottom=("present", "absent", "medical", "holiday")),
            "exclusions: medical\\nout of both\\n40 / 48": attendance(reg, bottom=("present", "absent")),
            "exclusions: medical\\ncounted present\\n42 / 50": attendance(reg, top=("present", "medical")),
            "window: last 20\\nworking days\\n14 / 20": attendance(work.tail(20))}
fig, ax = plt.subplots(figsize=(9.4, 4.2))
ax.bar(range(5), list(readings.values()), color=[VIOLET, ROSE, LAV, LAV, ROSE], width=0.62)
for i, v in enumerate(readings.values()):
    ax.text(i, v + 1.5, f"{v:.1f}", ha="center", fontweight="bold", color=INK)
ax.axhline(75, color=INK, linestyle="--", lw=1.2)
ax.text(4.42, 75, "75\\npercent", va="center", color=INK)
ax.set_xlim(-0.5, 5.0)
ax.set_xticks(range(5), list(readings), fontsize=10)
ax.set_ylim(0, 100)
ax.set_ylabel("attendance, percent")
ax.set_title("One student's register (invented): four lines, five readings", loc="left")
plt.show()
check("the function reproduces the five readings counted directly",
      list(readings.values()) == [round(v, 1) for v in direct.values()])
check("two of the five readings fall below a 75 percent line", sum(v < 75 for v in readings.values()) == 2)
'''),
        md('''
        ## What does a certificate printed on the wrong line cost?

        Suppose a scholarship (invented) asks for attendance of 75 percent or more. The clerk who divides
        by calendar days prints 66.7 and the student loses it; the clerk who follows the school's rule
        prints 80.0 and the student keeps it; a clerk who reads only the last 20 working days prints
        70.0. The check that catches the wrong number is the denominator and the window lines. The fix
        is to print the definition beside the number wherever it travels: present days over working
        days, the whole term, medical days kept in the denominator and out of the numerator.

        ### Your turn: what do the last 20 working days read with medical leave left out?

        In the term's last 20 working days the student was present on 14, absent on 4 and on medical
        leave for 2. A clerk leaves the medical days out of both counts. In the empty cell below, fill
        the two blanks and run it:

        ```python
        last_20 = reg[reg["status"] != "holiday"].tail(____)
        window_medical_out = attendance(last_20, bottom=(____))
        ```

        The check under it compares your number with the reference at one decimal, and shows the
        reference only once your number exists.
        '''),
        empty(),
        code('''
mine = globals().get("window_medical_out")
if mine is None:
    print("Store window_medical_out in the empty cell above, then run this cell again.")
else:
    ref = attendance(reg[reg["status"] != "holiday"].tail(20), bottom=("present", "absent"))
    print(f"reference: {ref:.1f}; yours: {mine:.1f}")
    print("matches at one decimal" if abs(mine - ref) <= 0.05 else "not yet: which statuses stay in the denominator?")
'''),
        md('''
        ## What does chapter 4 leave?

        1. The register (invented) holds 60 days: 10 holidays, 40 present, 8 absent and 2 on medical leave.
        2. Four honest clerks can print five numbers from it, from 66.7 to 84.0 percent.
        3. The denominator moved it to 66.7, the exclusions to 83.3 and 84.0, and the window to 70.0.
        4. One function, `attendance(days, top, bottom)`, holds the four lines and reproduces all five.
        5. Printed on the wrong line, the same student loses a scholarship set at 75 percent.

        **The rules.**

        - Write the numerator and the denominator as counts of named things.
        - Write the window as dates or periods: the same register reads 80.0 over the term and 70.0 over
          its last 20 working days.
        - List every exclusion, and date any change to the list.
        - Print the definition beside the number wherever the number travels.

        **In the interview.** [F] What makes a metric gameable, and how do you write one that is not?

        **The published form.** Swiggy's shareholder letters define a monthly transacting user as a
        unique user with at least one completed order in the month, averaged over the period, so a
        reader cannot mistake it for registered users. In 2018 Delhi Metro counted about 27 lakh riders
        a day while its new "line utilisation" count read 45,35,932 on 29 May 2018, because a rider who
        changes across three lines counts three times: one crowd, two units.

        **Where it goes next.** Notebook 05 asks what the four lines must resist. After the break,
        `C2_W04_D01_08_denominators_on_full_data_STUDENT.ipynb` writes the four lines for all 12,860
        Uber driver-weeks, where offers and rider requests count the same riders in two units.
        '''),
    ])


def c05():
    need(kirana_orders=50, kirana_marked=50, kirana_confirmed=40, kirana_unconfirmed=10, kirana_complaints=6,
         kirana_pay_rs=20, kirana_pay_marked_rs=1000, kirana_pay_confirmed_rs=800, kirana_pay_gap_rs=200,
         kirana_pay_raised_rs=25, kirana_pay_raised_marked_rs=1250, kirana_ontime_typed=1.0,
         kirana_ontime_bill=0.7, kirana_ontime_bill_count=35, kirana_confirmed_ontime=30,
         kirana_pay_confirmed_ontime_rs=600)
    build(NB / "C2_W04_D01_05_gaming_resistant_definitions_STUDENT.ipynb", [
        concept_head(
            5, "Gaming, and definitions that resist it: how is a paid number gamed, and which line of a "
               "definition stops each way?",
            "The owner of Balaji Kirana (invented), who pays the delivery boy Rs 20 for each delivery marked "
            "done in the shop's app and promises customers delivery within 30 minutes: a count the boy "
            "controls pays him for parcels nobody received. After the break, Uber's city head and finance "
            "partner, whose scheme pays a top-up on hours the driver controls.",
            ["What do the shop's four weeks of orders hold?",
             "How many deliveries did the boy mark done, and how many did customers confirm?",
             "What does each count pay, and what does on time read on each clock?",
             "Where do the month's complaints sit, found a second way?",
             "Which line of a definition stops each way of gaming?",
             "What does a resistant pay rule pay, in your turn?"]),
        code(CONCEPT_SETUP + "\ntopic_map(5)"),
        md('''
        ## What do the shop's four weeks of orders hold?

        **Gaming** is raising a number without doing what it stands for. It needs no dishonesty: a paid
        number pulls behaviour toward it, and people move with the pull. Balaji Kirana (invented), a
        corner shop in Hyderabad, delivers the orders it bills. For each order the table records whether
        the boy marked it done in the shop's app, whether the customer confirmed it with the OTP, the
        one-time code read out at the door, the minutes from the dispatch time the boy types to the done
        press, the minutes from the shop's bill to the done press, and whether the customer complained.
        This cell loads the 50 orders and prints every row.
        '''),
        code('''
orders = pd.read_csv("../data/C2_W04_D01_kirana_deliveries_STUDENT.csv")
print("Balaji Kirana's four weeks of home deliveries, every order invented for this chapter:")
print(orders.to_string(index=False))
check("50 orders over four weeks", len(orders) == 50 and orders["week"].nunique() == 4)
check("the boy marked every order done", orders["marked_done"].all())
'''),
        md('''
        ## What can rise with no parcel changing hands?

        **Predict before you run.** The boy marked all 50 orders done, so he is paid Rs 1,000. Against
        the deliveries customers confirmed with their OTP, what does the shop find?

        a) The same 50: a delivery marked is a delivery made.
        b) Fewer than 50: some were marked at the gate and never handed over.
        c) More than 50: customers confirm orders he forgot to mark.
        d) It cannot be told: the app keeps no second record.

        The next cell counts by hand from the table's columns, one line per step: the True values in
        `marked_done` and in `otp_confirmed`, and the minutes of 30 or under in each clock column. Then
        it counts by code and checks that the two agree.
        '''),
        code('''
# By hand, one line per step, from the columns of the table above
hand_marked = 50                 # True in marked_done: every order
hand_confirmed = 40              # True in otp_confirmed
hand_pay_marked = 50 * 20        # Rs 1,000 paid on the boy's count
hand_pay_confirmed = 40 * 20     # Rs 800 on the customer's count
hand_ontime_typed = 50 / 50      # 30 minutes or under from the time the boy types: every order
hand_ontime_bill = 35 / 50       # 30 minutes or under from the shop's bill: 35 orders

# By code, from every row
counted = {"marked": int(orders["marked_done"].sum()), "confirmed": int(orders["otp_confirmed"].sum())}
pay = {who: 20 * n for who, n in counted.items()}
ontime = {"typed": (orders["minutes_from_typed_dispatch"] <= 30).mean(),
          "bill": (orders["minutes_from_bill"] <= 30).mean()}
print("deliveries:", counted, " pay, Rs:", pay, " on time:", ontime)
check("hand and code agree: 50 marked done and 40 confirmed, Rs 1,000 against Rs 800",
      (counted["marked"], counted["confirmed"], pay["marked"], pay["confirmed"])
      == (hand_marked, hand_confirmed, hand_pay_marked, hand_pay_confirmed))
check("hand and code agree: on time 1.00 on the boy's clock and 0.70 on the shop's",
      (ontime["typed"], ontime["bill"]) == (hand_ontime_typed, hand_ontime_bill))
'''),
        md('''
        **What happened.** The answer is b: the boy marked 50 done and customers confirmed 40, so pay on
        his count is Rs 1,000 and on theirs Rs 800. The Rs 200 gap is the gaming: 10 orders were marked
        done at the gate and never handed over. His clock reads every order on time because he types the
        dispatch time himself; the shop's bill clock reads 35 of 50, 0.70. The plausible wrong belief is
        a: if we pay per delivery, we get more deliveries.

        ## Whose counts read higher?

        This cell draws the two pairs of counts: pay on the boy's count against the customer's, and on
        time by the boy's clock against the shop's.
        '''),
        code('''
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.4, 4.0), layout="constrained")
a1.bar(["marked done\\n(the boy)", "OTP-confirmed\\n(the customer)"], [pay["marked"], pay["confirmed"]],
       color=[ROSE, VIOLET], width=0.55)
for i, v in enumerate([pay["marked"], pay["confirmed"]]):
    a1.text(i, v + 25, f"Rs {v:,}", ha="center")
a1.set_ylim(0, 1200)
a1.set_title("Pay at Rs 20 a delivery", loc="left")
a2.bar(["from the time\\nthe boy types", "from the\\nshop's bill"], [100 * ontime["typed"], 100 * ontime["bill"]],
       color=[ROSE, VIOLET], width=0.55)
for i, v in enumerate([100 * ontime["typed"], 100 * ontime["bill"]]):
    a2.text(i, v + 2, f"{v:.0f} percent", ha="center")
a2.set_ylim(0, 115)
a2.set_title("Delivered within 30 minutes", loc="left")
fig.suptitle("Balaji Kirana, four weeks (invented): the boy's counts read higher", x=0.02, ha="left")
plt.show()
'''),
        md('''
        Both of the boy's counts read better than the counts the customer and the shop keep.

        ## Where do the complaints sit, found a second way?

        The first route found the gap by counting OTPs. The second starts from the customers: this cell
        matches the month's 6 complaints to the orders, then writes the resisting rule as a short
        function. A delivery counts for pay only with a receipt, the customer's OTP, and only when it is
        on time by a clock the system starts, the shop's bill.
        '''),
        code('''
by_receipt = orders.groupby("otp_confirmed")["complaint"].agg(orders="size", complaints="sum")
by_receipt.index = ["no OTP", "OTP-confirmed"]
print(by_receipt)

def paid_deliveries(orders, receipt=True, clock="minutes_from_bill", limit=30):
    """Deliveries that count for pay: OTP-confirmed when receipt is True, and done within the limit on the clock."""
    done = orders["otp_confirmed"] if receipt else orders["marked_done"]
    return int((done & (orders[clock] <= limit)).sum())

gamed = paid_deliveries(orders, receipt=False, clock="minutes_from_typed_dispatch")
resistant = paid_deliveries(orders)
print(f"on the boy's count and clock: {gamed} deliveries; with a receipt and the shop's clock: {resistant}")
fig, ax = plt.subplots(figsize=(7.4, 3.4))
ax.bar([-0.2, 0.8], by_receipt["orders"], width=0.4, color=LAV, label="orders")
ax.bar([0.2, 1.2], by_receipt["complaints"], width=0.4, color=ROSE, label="complaints")
for x, v in zip([-0.2, 0.8, 0.2, 1.2], list(by_receipt["orders"]) + list(by_receipt["complaints"])):
    ax.text(x, v + 0.8, str(v), ha="center")
ax.set_xticks([0, 1], by_receipt.index)
ax.set_ylim(0, 46)
ax.legend(frameon=False, loc="upper left")
ax.set_title("All 6 complaints sit on the 10 orders with no OTP", loc="left")
plt.show()
check("all 6 complaints sit on the 10 orders with no OTP",
      by_receipt.loc["no OTP"].tolist() == [10, 6] and by_receipt.loc["OTP-confirmed", "complaints"] == 0)
check("the resistant rule counts 30 deliveries where the gamed one counts 50", (gamed, resistant) == (50, 30))
'''),
        md('''
        **What happened.** All 6 complaints sit on the 10 orders with no OTP and none on the 40 the
        customers confirmed, so the second route finds the same 10 orders. The function shows two lines
        doing the work: the receipt condition cuts the count from 50 to 40, and the shop's clock cuts it
        to the 30 confirmed deliveries made within 30 minutes of the bill.

        **The trap.** The owner raises the rate to Rs 25 for each delivery marked done, to motivate the
        boy: four weeks then cost 50 x Rs 25 = Rs 1,250 while 40 parcels still reach customers. The check
        that catches it is the OTP column; the fix is a receipt condition in the numerator, a count the
        person served confirms.

        ## Which line of a definition stops each way of gaming?

        Named last: a definition **resists gaming** when its numerator needs a receipt, its denominator
        is set by someone other than the people paid, its clock starts at a time the system records, its
        exclusions are dated, and it says what it does not reward. The four ways the shop shows, each
        with the public record where it happened and the line that stops it:

        | How it is gamed | At Balaji Kirana (invented) | In public | The line that stops it |
        |---|---|---|---|
        | The paid person controls the count | The boy presses done | Uber's case: an open app counts as online (chapter 7) | A count the person served confirms |
        | No receipt or use is needed | Done with no OTP | Wells Fargo counted accounts nobody used | A receipt condition in the numerator |
        | The person timed sets the clock's start | The boy types the dispatch time | US Veterans Affairs schedulers typed a "desired date" | A window that starts at the system's time |
        | A quiet change of definition | The shop starts counting attempts | Wells Fargo added remittance accounts to its count in 2013 without telling investors | Exclusions and changes dated on the page |

        ### Your turn: what does the resistant rule pay?

        At Rs 20 a delivery, what does the boy earn for the four weeks when only OTP-confirmed deliveries
        made within 30 minutes of the shop's bill count? In the empty cell below, fill the two blanks and
        run it:

        ```python
        resistant_pay_rs = 20 * paid_deliveries(orders, receipt=____, clock="____")
        ```

        The check under it compares your number with the reference, and shows the reference only once
        your number exists. Then say in one sentence what the rule does not reward.
        '''),
        empty(),
        code('''
mine = globals().get("resistant_pay_rs")
if mine is None:
    print("Store resistant_pay_rs in the empty cell above, then run this cell again.")
else:
    ref = 20 * paid_deliveries(orders)
    print(f"reference: Rs {ref:,}; yours: Rs {mine:,}")
    print("matches" if mine == ref else "not yet: which column is the receipt, and which clock does the shop start?")
'''),
        md('''
        ## What does chapter 5 leave?

        1. The shop's four weeks (invented) hold 50 orders, all marked done by the boy and 40 confirmed
           by the customer's OTP.
        2. Pay reads Rs 1,000 on the boy's count and Rs 800 on the customer's; on time reads 1.00 on his
           clock and 0.70 on the shop's.
        3. All 6 complaints sit on the 10 orders with no OTP, so a second route finds the same gaming.
        4. `paid_deliveries(orders)` counts with a receipt and a system clock, and counts 30 where the
           boy's own count and clock read 50.
        5. Each way of gaming has a line that stops it: a receipt, a denominator the paid person does not
           set, a system clock, dated exclusions, and a line on what the number does not reward.

        **The rules.**

        - Let the person served confirm the count, as an OTP does.
        - Start the clock at a time the system records, never at one the person timed types in.
        - Date every change to what is counted, and print the change beside the number.
        - Say in one line what the number deliberately does not reward.

        **In the interview.** [F] What makes a metric gameable, and how do you write one that is not?

        **Where it goes next.** Notebook 06 puts the lines on one page. After the break,
        `C2_W04_D01_08_denominators_on_full_data_STUDENT.ipynb` finds Uber drivers logging hours with no
        trip, a count the driver controls, and `C2_W04_D01_09_north_star_guardrails_cost_STUDENT.ipynb`
        prices what paying for it cost.
        '''),
    ])


def c06():
    need(artifact_lines=7, artifact_weak_lines=2, artifact_weak_missing=5, artifact_target_pct=20,
         kirana_week_orders=[12, 13, 12, 13], kirana_week_confirmed=[10, 10, 10, 10], kirana_confirmed_share=0.8,
         kirana_complaints_per_100=12, kirana_confirmed_ontime=30, kirana_confirmed_ontime_share=0.75)
    build(NB / "C2_W04_D01_06_metric_definition_artifact_STUDENT.ipynb", [
        concept_head(
            6, "The metric definition artifact: what does the one page a company adopts hold, line by line?",
            "The owner of Balaji Kirana (invented), whose son wants \"deliveries up 20 percent\" as the "
            "shop's growth target, and who must write down what that number means before anyone is paid on "
            "it. After the break, the Hyderabad city head, who signs Uber's page.",
            ["What are the seven lines of the page?",
             "How many of them does the weak page, \"Deliveries, monthly, plus 20 percent\", hold?",
             "What does the full page say for the shop, and what does each page read week by week?",
             "Can a check find a blank line, or a guardrail that catches nothing?",
             "Does your page for chapter 2's driving school pass the check, in your turn?"]),
        code(CONCEPT_SETUP + "\ntopic_map(6)"),
        md('''
        ## What does the shop's table hold?

        The **metric definition artifact** is one page a company adopts, so teams argue about one written
        thing instead of three remembered ones. This notebook writes the page for Balaji Kirana (invented)
        on the same 50 orders as notebook 05, loaded again so this notebook stands alone. This cell loads
        the orders and prints every row.
        '''),
        code('''
orders = pd.read_csv("../data/C2_W04_D01_kirana_deliveries_STUDENT.csv")
print("Balaji Kirana's four weeks of home deliveries, every order invented for this chapter:")
print(orders.to_string(index=False))
check("50 orders, billed 12, 13, 12 and 13 a week", orders.groupby("week").size().tolist() == [12, 13, 12, 13])
'''),
        md('''
        ## How many of the seven lines does the weak page hold?

        The page has seven lines, in this order: the **numerator** (what is counted, with its receipt);
        the **denominator** (divided by what, with its count printed); the **window** (over which
        period); the **exclusions** (what leaves both counts, each change dated); what it **does not
        reward** (behaviour the number refuses to pay for); the **guardrails** (two or three numbers that
        must not fall); and the **gaming note** (the way of gaming each guardrail catches).

        **Predict before you run.** The son's growth plan reads "Deliveries, monthly, plus 20 percent".
        How many of the seven lines does it hold?

        a) One: only what is counted.
        b) Two: what is counted, and over when.
        c) Four: the lines that make it computable.
        d) All seven: a name, a window and a target.

        The next cell reads the weak page by hand, one line at a time, then by code, and checks that the
        two agree.
        '''),
        code('''
LINES = ["numerator", "denominator", "window", "exclusions", "does_not_reward", "guardrails", "gaming_note"]
weak = {"numerator": "deliveries", "window": "monthly"}     # "Deliveries, monthly, plus 20 percent"

# By hand, one line per step: which of the seven does the weak page write?
hand_held = ["numerator", "window"]    # "deliveries" is line 1, with no receipt; "monthly" is line 3
hand_blank = 7 - len(hand_held)        # five lines left blank; "plus 20 percent" is a target, no line at all

# By code
blank = [line for line in LINES if not weak.get(line)]
print("written on the weak page:", [line for line in LINES if weak.get(line)])
print("blank on the weak page:", blank)
check("hand and code agree: the weak page writes 2 of the 7 lines and leaves 5 blank",
      len(blank) == hand_blank and [line for line in LINES if line not in blank] == hand_held)
'''),
        md('''
        **What happened.** The answer is b: "deliveries" is line 1 with no receipt and "monthly" is line
        3; "plus 20 percent" is a target, which says how much and never what. The misconception under d
        is that a metric is defined once it has a name and a target.

        ## What does the full page say, and what does each page read?

        This cell writes the full page for the shop as a seven-key dictionary and draws the two pages
        side by side, line by line.
        '''),
        code('''
full = {"numerator": "deliveries confirmed with the customer's OTP",
        "denominator": "orders billed that week, the count printed beside the rate",
        "window": "the calendar week",
        "exclusions": "orders the customer cancelled before dispatch, each change dated; none in these four weeks",
        "does_not_reward": "a done press with no OTP, a dispatch time typed by hand, a shrinking order count",
        "guardrails": ["complaints per 100 orders billed", "confirmed deliveries within 30 minutes of the bill"],
        "gaming_note": {"complaints per 100 orders billed": "catches gate-marking",
                        "confirmed deliveries within 30 minutes of the bill": "catches a dispatch time typed late"}}
SHORT = {"numerator": "OTP-confirmed deliveries", "denominator": "orders billed, count printed",
         "window": "the calendar week", "exclusions": "cancelled before dispatch",
         "does_not_reward": "presses, typed clocks", "guardrails": "complaints; the bill clock",
         "gaming_note": "what each one catches"}
fig, ax = plt.subplots(figsize=(9.6, 4.4))
for r, line in enumerate(LINES):
    y = len(LINES) - 1 - r
    ax.text(-0.15, y, line.replace("_", " "), ha="right", va="center", color=INK)
    for c, (page, text) in enumerate(((weak, weak.get(line) or "blank"), (full, SHORT[line]))):
        filled = bool(page.get(line))
        ax.add_patch(plt.Rectangle((c * 2.6, y - 0.4), 2.5, 0.8, fc=VIOLET if filled else "white",
                                   ec=VIOLET if filled else ROSE, lw=1.4))
        ax.text(c * 2.6 + 1.25, y, text, ha="center", va="center", color="white" if filled else ROSE)
ax.text(1.25, 7.0, "the weak page", ha="center", fontweight="bold", color=INK)
ax.text(3.85, 7.0, "the full page", ha="center", fontweight="bold", color=INK)
ax.set_xlim(-2.6, 5.2)
ax.set_ylim(-0.6, 7.5)
ax.axis("off")
ax.set_title("Balaji Kirana's two pages (invented): 2 of 7 lines against 7 of 7", loc="left")
plt.show()
'''),
        md('''
        The weak page writes two lines and the full page all seven. The next cell reads both pages on
        the four weeks: the weak page counts every done press, and the full page counts OTP-confirmed
        deliveries over the orders billed, with its two guardrails beside it.
        '''),
        code('''
week = orders.groupby("week").agg(billed=("order_id", "size"), marked=("marked_done", "sum"),
                                  confirmed=("otp_confirmed", "sum"))
print(week)
confirmed = orders[orders["otp_confirmed"]]
reading = {"full page, the four weeks": round(orders["otp_confirmed"].sum() / len(orders), 2),
           "complaints per 100 orders billed": round(100 * orders["complaint"].sum() / len(orders)),
           "confirmed deliveries within 30 minutes of the bill": round((confirmed["minutes_from_bill"] <= 30).mean(), 2)}
print(reading)
fig, ax = plt.subplots(figsize=(8.8, 3.8))
ax.bar(week.index - 0.2, week["marked"], width=0.4, color=MUTED, label="the weak page: deliveries marked done")
ax.bar(week.index + 0.2, week["confirmed"], width=0.4, color=VIOLET, label="the full page: OTP-confirmed, of orders billed")
for w, row in week.iterrows():
    ax.text(w + 0.2, row["confirmed"] + 0.3, f"{row['confirmed']} of {row['billed']}", ha="center", color=INK)
ax.set_xticks(week.index, [f"week {w}" for w in week.index])
ax.set_ylim(0, 17.5)
ax.set_ylabel("deliveries")
ax.legend(frameon=False, loc="upper left")
ax.set_title("Balaji Kirana (invented): the weak page counts presses, the full page receipts", loc="left")
plt.show()
check("the weak page reads 12 or 13 a week, the full page 10 confirmed every week",
      week["marked"].tolist() == [12, 13, 12, 13] and week["confirmed"].tolist() == [10, 10, 10, 10])
check("the full page reads 0.80 over the four weeks, its guardrails 12 per 100 and 0.75",
      list(reading.values()) == [0.8, 12, 0.75])
'''),
        md('''
        **What happened.** Week by week the weak page reads 12 or 13 deliveries, every press counted; the
        full page reads 10 confirmed in each week out of 12 or 13 orders billed, 40 of 50 over the four
        weeks, 0.80. Its guardrails read 12 complaints per 100 orders billed, and 30 of the 40 confirmed
        deliveries within 30 minutes of the bill, 0.75.

        Named last: the **metric definition artifact** is the seven-line page a company adopts, four
        lines that make the number computable and three that make it safe to pay for. The curriculum row
        sets the bar: a definition is complete only when it names its numerator, its denominator, its
        window, and what it deliberately does not reward.

        ## Can a check find a blank line, or a guardrail that catches nothing?

        This cell writes the check as a short function. It lists every line left blank, and every
        guardrail the gaming note does not say it catches, since a guardrail earns its place by the
        gaming it catches (chapter 2's third rule). **The trap:** the son adds "orders billed up" as a
        third guardrail. It is a second growth count, it catches no way of gaming the first, and the
        check flags it; the fix is to drop it or to name the gaming it catches.
        '''),
        code('''
def written(value):
    """A line counts as written when it holds something other than the ____ placeholder."""
    return bool(value) and "____" not in str(value)

def missing_lines(page):
    """The page's blank lines, then every guardrail its gaming note does not say it catches."""
    blank_lines = [line for line in LINES if not written(page.get(line))]
    note = page.get("gaming_note") or {}
    unnamed = [g for g in page.get("guardrails") or [] if not written(note.get(g))]
    return blank_lines + [f"a guardrail that catches nothing named: {g}" for g in unnamed]

trap = {**full, "guardrails": full["guardrails"] + ["orders billed up"]}
for name, page in (("the weak page", weak), ("the full page", full), ("the full page plus a growth count", trap)):
    print(f"{name}: {missing_lines(page) or 'nothing missing'}")
check("the check finds the weak page's five blank lines", missing_lines(weak) == blank)
check("the full page passes the check", missing_lines(full) == [])
check("a growth count added as a guardrail is flagged",
      missing_lines(trap) == ["a guardrail that catches nothing named: orders billed up"])
'''),
        md('''
        ### Your turn: does your page for the driving school pass the check?

        Write chapter 2's driving school (invented) as a seven-line page whose north star is licences per
        learner who enrolled. Two lines are filled for you; fill the other five, naming in the gaming
        note each guardrail you list and what it catches. In the empty cell below, edit and run:

        ```python
        school_page = {"numerator": "learners who passed the licence test",
                       "denominator": "____",
                       "window": "the calendar year",
                       "exclusions": "____",
                       "does_not_reward": "____",
                       "guardrails": ["____"],
                       "gaming_note": {"____": "____"}}
        ```

        The check under it runs `missing_lines` on your page and passes when nothing is missing.
        '''),
        empty(),
        code('''
mine = globals().get("school_page")
if mine is None:
    print("Store school_page in the empty cell above, then run this cell again.")
else:
    gaps = missing_lines(mine)
    print("nothing missing: the page holds all seven lines" if not gaps else f"not yet, still missing: {gaps}")
'''),
        md('''
        ## What does chapter 6 leave?

        1. The page has seven lines: numerator, denominator, window, exclusions, what it does not reward,
           guardrails and the gaming note.
        2. The weak page writes two of them; "plus 20 percent" is a target, and no line at all.
        3. The full page counts OTP-confirmed deliveries over orders billed, by calendar week, and reads
           0.80 over the four weeks (invented), with its guardrails at 12 complaints per 100 orders billed
           and 0.75 within 30 minutes of the bill.
        4. `missing_lines(page)` finds a blank line, and a guardrail the gaming note does not say it
           catches.

        **The rules.**

        - Write all seven lines before anyone is paid on the number.
        - The first four lines make it computable; the last three make it safe to pay for.
        - A target is no line of a definition: "plus 20 percent" says how much and never what.
        - When teams disagree, change a line on the page and date it.

        **In the interview.** [D] Three departments each want their own target; how do you get to one,
        and what do you say to the two who lose?

        **Where it goes next.** After the break, `C2_W04_D01_07_proxy_test_on_twelve_rows_STUDENT.ipynb`
        opens the Uber case on six drivers counted by hand, and
        `C2_W04_D01_09_north_star_guardrails_cost_STUDENT.ipynb` fills the same seven lines for Uber's
        scheme with the room; the Kalpa lab fills them for Kalpa's growth plan.
        '''),
    ])


# ================================================================================ the case chapters
def case07():
    build(NB / "C2_W04_D01_07_proxy_test_on_twelve_rows_STUDENT.ipynb", [
        md(textwrap.dedent('''
        # Twelve driver-weeks by hand, with the proxy test and the four definition lines: what does an hour count?

        **Week 4, Monday, chapter 7 of 11, the first case chapter.** It applies two of the morning's
        topics: *What to measure and why; the proxy test*, taught in
        `C2_W04_D01_01_proxy_test_STUDENT.ipynb`, and *Definitions: numerator, denominator, window,
        exclusions*, taught in `C2_W04_D01_04_numerator_denominator_window_exclusions_STUDENT.ipynb`.
        Level 1 of the case's six, which climb from a hand count (L1) to interview depth (L6): read the
        ticket, say what the number stands for, and count it by hand on twelve rows of the case's own
        data.
        ''') + TICKET + textwrap.dedent('''
        **Who needs the answer.** The Hyderabad city head decides on Friday whether the scheme is
        working and whether to extend it. If "hours up 24 percent" is read as "more riders served"
        and it is not, the same top-up goes to two more cities.

        **The questions on the way.**

        1. What does chapter 1's proxy test ask of peak online hours?
        2. What did six drivers' hours and trips do between one week before and one week after?
        3. What is trips per peak online hour on those twelve rows, before and after?
        4. Which drivers moved it, and why do the six fall further than the city?
        5. How many of the offers shown did each driver accept?
        ''')),
        md('''
        ## What does chapter 1's proxy test ask of peak online hours?

        Chapter 1's canteen (invented) paid its servers per token and watched tokens double while plates
        stayed at 200: the paid number drifted from the thing it stood for. The proxy test asks whether
        a team could hit a number while the thing it stands for got worse or stayed the same. The
        ticket's "peak online hours" counts an hour whenever the driver app is open and the driver is
        marked available, wherever the phone is, so a driver can raise it with no rider served.

        ## What did six drivers' hours and trips do between one week before and one week after?

        The twelve rows are six drivers, A to F, each in two weeks: the week beginning 10 August 2026
        (before the launch) and the week beginning 21 September 2026 (after). This cell sets up the
        notebook and picks those twelve driver-weeks out of `driver_weeks`. New in it: `.isin(...)`
        keeps the rows whose value is in a list, `.map(...)` swaps each value for the one a dictionary
        gives it, and `sort_values` puts the rows in order.
        '''),
        code(SETUP + STYLE + '''
dw = pd.read_csv("../data/C2_W04_D01_driver_weeks_STUDENT.csv")
names = {"d_0001": "A", "d_0002": "B", "d_0003": "C", "d_0004": "D", "d_0881": "E", "d_0882": "F"}
twelve = dw[dw["driver_id"].isin(names) & dw["week_start"].isin(["2026-08-10", "2026-09-21"])].copy()
twelve["driver"] = twelve["driver_id"].map(names)
twelve["week"] = twelve["week_start"].map({"2026-08-10": "before", "2026-09-21": "after"})
twelve = twelve.sort_values(["driver", "week"], ascending=[True, False])
twelve[["driver", "week", "zone_mode", "peak_online_hours", "peak_offers", "peak_accepted", "peak_trips"]]
'''),
        md('''
        **The rate's four lines, as chapter 4 writes them.** Numerator: completed peak trips. Denominator:
        peak online hours. Window: the week before the launch against the week after. Exclusions: none
        on these twelve rows.

        **Predict before you run.** On these six drivers, what happens to trips per peak online hour
        between the two weeks? a) holds near 1.9; b) falls to about 1.6, as the city's did; c) falls
        to about 1.2; d) rises above 2.0.

        This cell adds up the hours and the trips in each week, then divides the two sums.
        '''),
        code('''
totals = twelve.groupby("week")[["peak_online_hours", "peak_trips"]].sum().loc[["before", "after"]]
totals["trips_per_hour"] = (totals["peak_trips"] / totals["peak_online_hours"]).round(2)
totals
'''),
        md('''
        **What happened.** The answer is c. The six drivers logged 60 hours and 114 trips before,
        74 hours and 88 trips after: hours up 23 percent, trips down 23 percent, and trips per peak
        online hour from 1.90 to 1.19. The city fell to 1.58, and the six fall further because they
        were chosen to show the mechanism: two of them, E and F, logged hours with almost no trips,
        a third of this sample. How common such drivers are in the city is chapter 8's question.
        E and F also keep shorter weeks than most drivers who idle like them, which chapter 8's
        full data shows.

        ## Which drivers moved the ratio, and in which direction?

        This cell takes each driver's own trips per hour in both weeks and draws one line per driver.
        New in it: `.pivot` turns the two weeks into two columns with one row per driver, and
        `.iterrows()` walks those rows one at a time to draw each line.
        '''),
        code('''
wide = twelve.pivot(index="driver", columns="week", values=["peak_online_hours", "peak_trips"])
rate = (wide["peak_trips"] / wide["peak_online_hours"]).round(2)[["before", "after"]]
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for driver, row in rate.iterrows():
    colour = ROSE if driver in "EF" else VIOLET
    ax.plot([0, 1], [row["before"], row["after"]], marker="o", color=colour)
    ax.text(1.04, row["after"], driver, color=colour, va="center")
ax.set_xticks([0, 1], ["week of 10 Aug", "week of 21 Sep"])
ax.set_ylim(0, 2.4)
ax.set_ylabel("trips per peak online hour")
ax.set_title("Four drivers held near 2; E and F fell close to zero", loc="left")
plt.show()
rate
'''),
        md('''
        **What happened.** A to D held between 1.80 and 2.10 trips an hour. E went from 10 hours and
        18 trips to 16 hours and 3 trips; F went from 10 hours and 17 trips to 14 hours and 2 trips.
        Both sit in outer zones (Shamshabad and Rajendranagar), where riders ask for few trips at any
        hour. Their hours went up and their trips nearly vanished: the proxy rose while the thing it
        stands for fell.

        This cell draws the six drivers' hours and trips as two pairs of bars, the picture the
        hand count makes.
        '''),
        code('''
fig, ax = plt.subplots(figsize=(6.4, 3.4))
ax.bar([0, 1], totals["peak_online_hours"], width=0.35, color=VIOLET, label="peak online hours")
ax.bar([0.38, 1.38], totals["peak_trips"], width=0.35, color=LAV, label="completed peak trips")
for x, v in zip([0, 1, 0.38, 1.38], list(totals["peak_online_hours"]) + list(totals["peak_trips"])):
    ax.text(x, v + 2, str(v), ha="center")
ax.set_xticks([0.19, 1.19], ["before", "after"])
ax.set_ylim(0, 132)
ax.set_title("Six drivers: hours up 23 percent, trips down 23 percent", loc="left")
ax.legend(frameon=False, loc="upper right")
plt.show()
'''),
        md('''
        ## How many of the offers shown did each driver accept?

        A driver who stays online without driving shows first in what that driver does with the offers
        the app shows. This cell draws each driver's offers shown and offers accepted in the week after
        the launch.
        '''),
        code('''
after_rows = twelve[twelve["week"] == "after"].set_index("driver")
fig, ax = plt.subplots(figsize=(6.4, 3.4))
ax.bar([i - 0.2 for i in range(6)], after_rows["peak_offers"], width=0.4, color=LAV, label="offers shown")
ax.bar([i + 0.2 for i in range(6)], after_rows["peak_accepted"], width=0.4, color=VIOLET, label="offers accepted")
ax.set_xticks(range(6), after_rows.index)
ax.set_ylabel("offers in the week of 21 Sep")
ax.set_title("The week after: A to D accepted most offers; E and F, a few", loc="left")
ax.legend(frameon=False, loc="upper right")
plt.show()
after_rows[["peak_offers", "peak_accepted"]]
'''),
        md('''
        **What happened.** A to D accepted most of what they were shown. E accepted 4 of the 14 offers
        it was shown and F 3 of 12: both stayed online and declined.

        This cell checks the claims the chapter makes about its own numbers.
        '''),
        code('''
check("the twelve rows are six drivers in two weeks", len(twelve) == 12 and twelve["driver"].nunique() == 6)
check("hours 60 before and 74 after", list(totals["peak_online_hours"]) == [60, 74])
check("trips 114 before and 88 after", list(totals["peak_trips"]) == [114, 88])
check("trips per peak online hour 1.90 before and 1.19 after", list(totals["trips_per_hour"]) == [1.90, 1.19])
check("E and F fell below 0.25 trips an hour after the launch", (rate.loc[["E", "F"], "after"] < 0.25).all())
check("E accepted 4 of 14 offers and F 3 of 12 after the launch",
      after_rows.loc[["E", "F"], ["peak_accepted", "peak_offers"]].values.tolist() == [[4, 14], [3, 12]])
'''),
        md(f'''
        ## What does chapter 7 answer?

        1. Peak online hours count an hour whenever the driver app is open, so they fail chapter 1's
           proxy test: a driver can raise them with no rider served.
        2. The six drivers' hours rose from 60 to 74 while their trips fell from 114 to 88.
        3. Trips per peak online hour on the twelve rows, completed peak trips over peak online hours
           in the week before against the week after, fell from 1.90 to 1.19.
        4. E and F moved it: their hours rose while their trips fell to 3 and 2. The six fall further
           than the city's 1.58 because they were chosen to show the mechanism.
        5. E accepted 4 of 14 offers and F 3 of 12, while A to D accepted most of theirs.

        **The check a senior analyst runs before trusting a rate.** Read its baseline (1.90 before),
        its denominator (hours the app was open, which a driver controls) and the evidence that the
        thing it stands for moved (trips rose only 3 percent across the city).

        **In the interview.** [S] How would you measure the success of a new feature? {TAGS} A
        hire-grade answer starts from what the feature is for and names a number that cannot rise while
        that thing gets worse. Notebook 08 runs the same count on all 12,860 driver-weeks.
        '''),
    ])


def case08():
    build(NB / "C2_W04_D01_08_denominators_on_full_data_STUDENT.ipynb", [
        md(f'''
        # All 12,860 driver-weeks, with the definition lines and gaming: what do the city totals say, and which drivers and zones drive the fall?

        **Week 4, Monday, chapter 8 of 11, the second case chapter.** It applies two of the morning's
        topics: *Definitions: numerator, denominator, window, exclusions*, taught in
        `C2_W04_D01_04_numerator_denominator_window_exclusions_STUDENT.ipynb`, and *Gaming, and
        definitions that resist it*, taught in `C2_W04_D01_05_gaming_resistant_definitions_STUDENT.ipynb`.
        Levels 2 and 3 of the case's six: the same count on the full data in the smallest code, then the
        trap, the denominator and the segment that drives the number. New in the setup cell:
        `.lt("2026-08-31")` asks whether each week starts before the launch, and `.map` turns True and
        False into before and after.

        **The case.** Uber's Hyderabad city team launched a peak-hour earnings guarantee on Monday
        31 August 2026, a floor of Rs 300 per peak online hour with Uber paying the gap as a top-up.
        Peak online hours rose 24 percent over the six weeks after the launch, completed peak trips 3
        percent, and the city head asks whether the scheme is working, what it should pay for and
        whether anyone is gaming it.

        {LABEL}

        Notebook 07 counted six drivers by hand: their hours rose from 60 to 74, their trips fell from
        114 to 88, and trips per peak online hour fell from 1.90 to 1.19, pulled down by two drivers in
        outer zones. This notebook runs the count on every driver-week.

        **Who needs the answer.** The city head, before a proposal to extend the scheme to two more
        cities goes out. A fall read as weak demand, or measured with the wrong denominator, sends the
        same top-up further.

        **The questions on the way.**

        1. What are the city's totals before and after the launch?
        2. Did rider demand fall?
        3. What does a quick average of each driver-week's rate say, and why is it wrong?
        4. Which drivers sit under 1.0 trip per peak online hour after the launch?
        5. Where did their new hours go, and does a second route find the same drivers?
        '''),
        code(SETUP + STYLE + '''
dw = pd.read_csv("../data/C2_W04_D01_driver_weeks_STUDENT.csv")
zw = pd.read_csv("../data/C2_W04_D01_zone_weeks_STUDENT.csv")
dw["window"] = dw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
zw["window"] = zw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
print(f"{len(dw):,} driver-weeks and {len(zw)} zone-weeks, twelve weeks from {dw.week_start.min()}")
'''),
        md('''
        ## What are the city's totals before and after the launch?

        A rate is a ratio of two sums: add up every trip, add up every hour, then divide. Its four lines,
        as chapter 4 writes them: numerator, completed peak trips; denominator, peak online hours;
        window, the six weeks on each side of the launch; exclusions, none. This cell sums the six weeks
        on each side of the launch and takes each rate that way.
        '''),
        code('''
city = dw.groupby("window")[["peak_online_hours", "peak_trips", "peak_offers", "peak_accepted",
                             "peak_driver_cancels", "peak_hours_no_trip"]].sum().loc[["before", "after"]]
city["trips_per_hour"] = (city["peak_trips"] / city["peak_online_hours"]).round(2)
city["acceptance"] = (city["peak_accepted"] / city["peak_offers"]).round(3)
city["driver_cancel_share"] = (city["peak_driver_cancels"] / city["peak_accepted"]).round(3)
city["no_trip_share"] = (city["peak_hours_no_trip"] / city["peak_online_hours"]).round(2)
city.T
'''),
        md('''
        **What happened.** Peak online hours rose from 118,000 to 146,300 and completed peak trips from
        224,200 to 230,900, so trips per peak online hour fell from 1.90 to 1.58. The share of offers
        accepted fell from 0.863 to 0.730, the share of accepted trips the driver then cancelled rose
        from 0.037 to 0.090, and the share of online hours with no completed trip rose from 0.22 to
        0.38.

        ## Did rider demand fall?

        If riders asked for fewer trips, trips per online hour would fall with nobody gaming
        anything. Demand lives in `zone_weeks`, which counts rider requests.

        **Predict before you run.** From the six weeks before to the six weeks after, rider requests
        a) fell by about a tenth; b) held about level; c) rose a little; d) rose by a quarter, as
        hours did.

        This cell sums requests and fulfilled requests by window, takes the city's wait as the median
        of the 72 zone-week median waits in each window (12 zones for six weeks), and sets offers
        beside requests. New in it: `.agg(name=(column, "sum"))` makes several named totals in one
        step.
        '''),
        code('''
demand = zw.groupby("window").agg(requests=("peak_requests", "sum"), fulfilled=("peak_fulfilled", "sum"),
                                  median_wait=("median_wait_min", "median")).loc[["before", "after"]]
demand["unfulfilled_share"] = (1 - demand["fulfilled"] / demand["requests"]).round(2)
demand["offers_per_request"] = (city["peak_offers"] / demand["requests"]).round(2)
demand
'''),
        md('''
        **What happened.** The answer is c: rider requests rose from 251,910 to 256,556, up 1.8
        percent, and the share left unfulfilled went from 0.11 to 0.10, while the median wait moved
        from 4.8 to 4.6 minutes. The fall is not demand. Offers per request rose from 1.07 to 1.35,
        because a request that one driver declines is offered to the next and counted again in
        `driver_weeks`: more declining shows up as more offers for the same riders. Offers and requests
        are two units for one crowd, as chapter 4's Delhi Metro counted riders once and line uses
        again.

        This cell draws the twelve weeks, hours on the left axis and trips per hour on the right
        (`ax.twinx()` adds the second axis), to
        see whether the after window is two odd weeks or a level that held.
        '''),
        code('''
weekly = dw.groupby("week_start")[["peak_online_hours", "peak_trips"]].sum()
weekly["trips_per_hour"] = weekly["peak_trips"] / weekly["peak_online_hours"]
fig, ax = plt.subplots(figsize=(8.0, 3.8))
ax.plot(range(12), weekly["peak_online_hours"], marker="o", color=VIOLET)
ax.set_ylabel("peak online hours", color=VIOLET)
right = ax.twinx()
right.plot(range(12), weekly["trips_per_hour"], marker="s", color=ROSE)
right.set_ylabel("trips per peak online hour", color=ROSE)
right.spines["right"].set_visible(True)
ax.axvline(5.5, color=MUTED, linestyle="--")
ax.set_xticks(range(12), [w[5:] for w in weekly.index], rotation=45)
ax.set_title("Hours jumped at the launch; trips per hour fell and stayed down", loc="left")
plt.show()
weekly["trips_per_hour"].round(2).to_frame().T
'''),
        md('''
        **What happened.** Before the launch, trips per hour wandered between 1.88 and 1.93. In the
        launch week it read 1.64, and from then on it stayed between 1.55 and 1.59. Hours rose from
        about 20,000 a week to about 24,000. The fall held for six weeks.

        ## What does a quick average of each driver-week's rate say?

        **The plausible wrong answer.** A colleague in a hurry works out trips per hour for each
        driver-week, then takes the plain average of those rates for each window.

        **Predict before you run.** What does that average print for the after window? a) 1.58;
        b) 1.71; c) 1.19; d) 1.90.

        This cell computes the colleague's number beside the ratio of the sums.
        '''),
        code('''
online = dw[dw["peak_online_hours"] > 0].copy()
online["rate"] = online["peak_trips"] / online["peak_online_hours"]
compare = pd.DataFrame({"mean_of_rates": online.groupby("window")["rate"].mean().round(2),
                        "ratio_of_sums": city["trips_per_hour"]}).loc[["before", "after"]]
compare
'''),
        md('''
        **Why it is wrong.** The answer is b: the average of rates prints 1.71, against 1.58 from the
        sums. The true fall is 0.32, from 1.90 to 1.58; the average shows 0.19 of it and hides 0.13,
        about two-fifths. An average of rates gives a 42-hour driver-week the same weight as a 10-hour
        one, so the long, slow weeks of the drivers online longest count no more than anyone's short,
        busy ones. With **invented numbers**: a driver at 2.0 trips an hour for 10 hours (20 trips)
        and a driver at 0.5 for 40 hours (20 trips) made 40 trips in 50 hours, which is 0.80 an hour,
        while the average of their two rates is 1.25: too high, in the same direction as the city's
        1.71. The fix is the ratio of the sums, with its denominator named: trips per peak online
        hour, all hours in the window.

        ## Which drivers sit under 1.0 trip per peak online hour after the launch?

        **Predict before you run.** Of the 1,200 drivers, how many made fewer than one trip per peak
        online hour across the six weeks after the launch? a) about 30; b) about 100; c) about 180;
        d) about 400.

        **Your turn.** Type these lines into the empty cell below and run it:

        ```python
        after = dw[dw["window"] == "after"]
        per_driver = after.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
        per_driver["rate"] = per_driver["peak_trips"] / per_driver["peak_online_hours"]
        (per_driver["rate"] < 1.0).sum()
        ```
        '''),
        empty(),
        md('''
        Your cell prints a count of drivers. The next cell builds the same group so the rest of the
        notebook can use it, and sets their hours and trips before and after; `:.0%` prints a share as
        a whole percent.
        '''),
        code('''
after = dw[dw["window"] == "after"]
per_driver = after.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
slow = set(per_driver.index[per_driver["peak_trips"] / per_driver["peak_online_hours"] < 1.0])
tail = dw[dw["driver_id"].isin(slow)].groupby("window")[["peak_online_hours", "peak_trips"]].sum()
tail = tail.loc[["before", "after"]]
print(f"{len(slow)} drivers, {len(slow) / 1200:.0%} of the 1,200")
print("hours, after over before:", round(tail.loc["after", "peak_online_hours"] / tail.loc["before", "peak_online_hours"], 2))
print("trips, after over before:", round(tail.loc["after", "peak_trips"] / tail.loc["before", "peak_trips"], 2))
'''),
        md('''
        **What happened.** The answer is c: 180 drivers, 15 percent of the 1,200. Their peak online
        hours after the launch were 2.1 times their hours before, while their trips were 0.88 times,
        down 12 percent. Call them the **idle tail**: drivers who stayed online without driving. It is
        chapter 5's first way of gaming, the paid person controlling the count, since a driver decides
        when the app is open. The six of chapter 7 held two such drivers, a third of the sample against
        15 percent city-wide, which is why the six fell to 1.19 while the city fell to 1.58.

        ## Where did the idle tail's new hours go?

        This cell compares the idle tail's hours in the three outer zones before and after, then
        draws every driver-week after the launch, hours against trips.
        '''),
        code('''
OUTER = ["Shamshabad", "Rajendranagar", "Patancheru"]
idle = dw[dw["driver_id"].isin(slow)]
outer_hours = idle[idle["zone_mode"].isin(OUTER)].groupby("window")["peak_online_hours"].sum()
new_hours = tail.loc["after", "peak_online_hours"] - tail.loc["before", "peak_online_hours"]
outer_share = (outer_hours["after"] - outer_hours["before"]) / new_hours
print(f"new hours {new_hours:,}; share logged in the outer zones {outer_share:.2f}")
mark = after["driver_id"].isin(slow)
fig, ax = plt.subplots(figsize=(7.4, 4.2))
ax.scatter(after.loc[~mark, "peak_online_hours"], after.loc[~mark, "peak_trips"], s=6, color=LAV,
           label="every other driver-week")
ax.scatter(after.loc[mark, "peak_online_hours"], after.loc[mark, "peak_trips"], s=8, color=ROSE,
           label="the idle tail's driver-weeks")
ax.plot([0, 36], [0, 36 * 1.9], linestyle=":", color=VIOLET, label="1.9 trips per hour")
ax.set_xlim(0, 45)
ax.set_xlabel("peak online hours in the week")
ax.set_ylabel("completed peak trips")
ax.set_title("After the launch: the idle tail sits far right and low", loc="left")
ax.legend(frameon=False)
plt.show()
'''),
        md('''
        **What happened.** The idle tail logged 22,000 new hours, and 72 percent of them sat in the
        three outer zones, where requests are thin at any hour: a driver parked there stays online,
        is shown few requests, and is paid the floor. A week holds at most 42 peak hours (two
        three-hour windows a day, seven days), and many idle-tail weeks sit near that edge.

        ## Does a second route find the same drivers?

        The first route sorted drivers by trips per hour. The second ignores trips and asks only how
        often each driver accepted what the app offered: this cell keeps every driver whose accepted
        share stayed under 0.5 in every week they worked after the launch, then draws requests by
        zone to show how thin the outer zones are.
        '''),
        code('''
weeks_after = after[after["peak_offers"] > 0]
low_every_week = (weeks_after["peak_accepted"] / weeks_after["peak_offers"] < 0.5).groupby(weeks_after["driver_id"]).all()
second = set(low_every_week.index[low_every_week])
print(f"{len(second)} drivers by acceptance; the same drivers as the first route: {second == slow}")
by_zone = zw.groupby("zone")["peak_requests"].sum().sort_values()
fig, ax = plt.subplots(figsize=(7.4, 3.8))
ax.barh(by_zone.index, by_zone.values, color=[ROSE if z in OUTER else VIOLET for z in by_zone.index])
ax.set_xlabel("rider requests at peak, twelve weeks")
ax.set_title("The three outer zones get a fraction of the requests", loc="left")
plt.show()
'''),
        code('''
check("hours 118,000 before and 146,300 after", list(city["peak_online_hours"]) == [118000, 146300])
check("trips per peak online hour 1.90 before and 1.58 after", list(city["trips_per_hour"]) == [1.90, 1.58])
check("rider requests rose, 251,910 to 256,556", list(demand["requests"]) == [251910, 256556])
check("the average of rates prints 1.71 after, above the true 1.58", compare.loc["after", "mean_of_rates"] == 1.71)
check("180 drivers under 1.0 trip per hour after the launch", len(slow) == 180)
check("the idle tail's hours 2.1 times, trips 0.88 times",
      round(tail.loc["after", "peak_online_hours"] / tail.loc["before", "peak_online_hours"], 2) == 2.1
      and round(tail.loc["after", "peak_trips"] / tail.loc["before", "peak_trips"], 2) == 0.88)
check("72 percent of the new hours in the outer zones", round(outer_share, 2) == 0.72)
check("the acceptance route finds the same 180 drivers", second == slow)
'''),
        md('''
        ## What does chapter 8 answer?

        1. Hours rose from 118,000 to 146,300 and trips from 224,200 to 230,900: 1.90 to 1.58 trips an hour.
        2. Demand did not fall: rider requests rose 1.8 percent, and waits moved from 4.8 to 4.6 minutes.
        3. An average of each week's rate prints 1.71 and hides two-fifths of the fall; the ratio of
           the sums, 1.58, is the number.
        4. 180 drivers, 15 percent, sit under 1.0 trip an hour after the launch, with hours 2.1 times
           and trips 0.88 times their level before.
        5. 72 percent of their new hours sat in the three thin outer zones, and the acceptance route
           finds the same 180 drivers.

        **The check a senior analyst runs.** Before celebrating hours, set the baseline (1.90) beside
        the new rate (1.58), name the denominator (hours the app was open), look for the evidence in
        a second table (rider requests rose), and reach the segment a second way (acceptance finds
        the same 180).

        **In the interview.** [F] What makes a metric gameable? The measured person controls the
        count: here a driver decides when the app is open. Notebook 09 prices what that cost and
        writes the number the scheme should pay for.
        '''),
    ])


def case09():
    build(NB / "C2_W04_D01_09_north_star_guardrails_cost_STUDENT.ipynb", [
        md(f'''
        # The redesign's north star, guardrails, leading inputs and seven-line page: what should the scheme pay for, and what did paying for hours cost?

        **Week 4, Monday, chapter 9 of 11, the third case chapter.** It applies four of the morning's
        topics: *North-star and guardrail metrics*, taught in `C2_W04_D01_02_north_star_guardrails_STUDENT.ipynb`;
        *Leading against lagging indicators*, taught in `C2_W04_D01_03_leading_lagging_STUDENT.ipynb`;
        *Gaming, and definitions that resist it*, taught in
        `C2_W04_D01_05_gaming_resistant_definitions_STUDENT.ipynb`; and *The metric definition
        artifact*, taught in `C2_W04_D01_06_metric_definition_artifact_STUDENT.ipynb`. Levels 3 to 5 of
        the case's six: the trap priced in rupees, the definition that resists it, the caveats an
        engineer names aloud, and a second route in SQL.

        **The case.** Uber's Hyderabad city team launched a peak-hour earnings guarantee on Monday
        31 August 2026: a floor of Rs 300 per peak online hour, with Uber paying the gap between a
        driver's trip earnings and the floor as a top-up. Six weeks on, peak online hours are up 24
        percent, completed peak trips up 3 percent, and the top-up has cost Rs 1.9 crore.

        {LABEL}

        Notebook 08 found the fall in the full data: trips per peak online hour fell from 1.90 to 1.58
        while rider requests rose, and 180 drivers (15 percent) logged 2.1 times their hours with 12
        percent fewer trips, 72 percent of their new hours in the three thin outer zones.

        **Who needs the answer.** The city head, who must say by Friday what the scheme pays for, and
        the finance partner, who holds the top-up budget. A scheme that keeps paying for hours keeps
        paying drivers to sit online in zones with no riders.

        **The questions on the way.**

        1. How much of the Rs 1.9 crore went to driver-weeks that accepted fewer than half their offers?
        2. What would the redesign save, under a stated assumption about how drivers respond?
        3. What do the north star and its three guardrails read, before and after?
        4. Which number moved first?
        5. Which doubts does the fall survive, and which stay open?
        6. Does SQL reach the same totals as pandas?
        '''),
        code(SETUP + STYLE + '''
dw = pd.read_csv("../data/C2_W04_D01_driver_weeks_STUDENT.csv")
zw = pd.read_csv("../data/C2_W04_D01_zone_weeks_STUDENT.csv")
dw["window"] = dw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
zw["window"] = zw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
after = dw[dw["window"] == "after"].copy()
after["acceptance"] = after["peak_accepted"] / after["peak_offers"]
print(f"{len(after):,} driver-weeks after the launch; top-up paid Rs {after['topup_rs'].sum() / 1e7:.2f} crore")
'''),
        md('''
        ## How much of the Rs 1.9 crore went to driver-weeks that accepted fewer than half their offers?

        **Predict before you run.** What share of the top-up went to driver-weeks whose accepted share
        was under 0.5? a) 15 percent; b) 39 percent; c) 61 percent; d) 88 percent.

        This cell splits the top-up at an accepted share of 0.5 and draws the two parts.
        '''),
        code('''
low = after.loc[after["acceptance"] < 0.5, "topup_rs"].sum()
high = after.loc[after["acceptance"] >= 0.5, "topup_rs"].sum()
fig, ax = plt.subplots(figsize=(7.0, 2.6))
ax.barh(["accepted under 0.5", "accepted 0.5 or more"], [low / 1e5, high / 1e5], color=[ROSE, VIOLET])
for y, v in enumerate([low, high]):
    ax.text(v / 1e5 + 2, y, f"Rs {v / 1e5:.0f} lakh", va="center")
ax.set_xlabel("top-up paid over six weeks, Rs lakh")
ax.set_title("Where the Rs 1.9 crore top-up went", loc="left")
plt.show()
print(f"share to driver-weeks under 0.5: {low / (low + high):.2f}")
'''),
        md('''
        **What happened.** The answer is c: Rs 1.159 crore, 61 percent of the Rs 1.9 crore, went to
        driver-weeks that accepted fewer than half the offers they were shown, and Rs 74 lakh went to
        the rest. Had only the driver-weeks at or above 0.5 been paid, and had every driver behaved the
        same, the six weeks would have cost Rs 74 lakh. A new rule changes behaviour, so Rs 74 lakh is
        the least the six weeks would have cost under it.

        ## What would the redesign save, under a stated assumption about how drivers respond?

        The driver-weeks under 0.5 are the idle tail's: its highest week after the launch accepted
        0.46 of its offers and every other driver's lowest accepted 0.78, so the Rs 1.159 crore is the
        idle tail's top-up. Some idle-tail drivers would start accepting enough to qualify under a rule
        that pays for trips. The share of the idle tail's top-up that would still be paid is an **assumption**:
        0.2 at the low end, 0.5 at the high end. A test of the redesign, which this afternoon's
        tentative faculty block designs, is what settles it. This cell prices both ends.
        '''),
        code('''
saving = pd.DataFrame({"still_paid_share": [0.2, 0.5]})
saving["saving_rs"] = (low * (1 - saving["still_paid_share"])).round()
saving["saving_lakh"] = (saving["saving_rs"] / 1e5).round(1)
saving
'''),
        md('''
        **What happened.** If a fifth of the idle tail's top-up were still paid, the redesign saves
        Rs 92.7 lakh over six weeks; if half were, Rs 58.0 lakh. The range is the honest answer to
        finance until the test reports.

        ## What do the north star and its three guardrails read, before and after?

        The redesign's page, the seven lines of chapter 6, line by line:

        | Line | What it says |
        |---|---|
        | Numerator | Trips completed inside the peak windows, one per paying rider: Uber's annual report counts an UberX Share ride with three paying riders as three trips |
        | Denominator | Enrolled drivers online at least one peak hour that week, with the count printed beside the rate |
        | Window | The calendar week |
        | Exclusions | Trips cancelled by either side, test accounts, trips outside the windows |
        | What it does not reward | Hours online; offers declined; a shrinking enrolled base, since fewer drivers in the count would raise the rate with no extra trip |
        | Guardrails | For riders: offers accepted over offers shown, at or above a floor the city sets, and the median rider wait at peak. For the budget: top-up per completed trip |
        | Gaming note | Guardrail 1 catches declining and cherry-picking; guardrail 2, supply that stops serving riders; guardrail 3, a top-up that runs away from the trips it pays for |

        This cell computes the north star and the three guardrails for each window.
        '''),
        code('''
online = dw[dw["peak_online_hours"] > 0]
board = pd.DataFrame({
    "north_star_trips_per_online_driver_week": (online.groupby("window")["peak_trips"].sum()
                                                / online.groupby("window").size()).round(2),
    "online_driver_weeks": online.groupby("window").size(),
    "acceptance": (dw.groupby("window")["peak_accepted"].sum() / dw.groupby("window")["peak_offers"].sum()).round(3),
    "median_wait": zw.groupby("window")["median_wait_min"].median(),
    "topup_per_trip_rs": (dw.groupby("window")["topup_rs"].sum() / dw.groupby("window")["peak_trips"].sum()).round(1),
}).loc[["before", "after"]]
board.T
'''),
        md('''
        **What happened.** The north star read 35.76 trips per online driver-week before and 35.89
        after: hours rose 24 percent and the number the scheme exists for barely moved. Acceptance
        fell from 0.863 to 0.730, the median wait went from 4.8 to 4.6 minutes, and the top-up cost
        Rs 82.3 per completed trip after the launch, against nothing before.

        ## Which number moved first?

        Chapter 3's chase named the two kinds: a **leading** input moves before the number the plan is
        judged on, while the team can still act; a **lagging** one confirms it later. This cell draws
        the weekly share of offers accepted beside bookings per online hour.
        '''),
        code('''
wk = dw.groupby("week_start")[["peak_accepted", "peak_offers", "peak_bookings_rs", "peak_online_hours"]].sum()
wk["acceptance"] = wk["peak_accepted"] / wk["peak_offers"]
wk["rs_per_hour"] = wk["peak_bookings_rs"] / wk["peak_online_hours"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.0, 3.2))
a1.plot(range(12), wk["acceptance"], marker="o", color=VIOLET)
a1.set_title("Offers accepted, share", loc="left")
a2.plot(range(12), wk["rs_per_hour"], marker="s", color=ROSE)
a2.set_title("Bookings per online hour, Rs", loc="left")
for a in (a1, a2):
    a.axvline(5.5, color=MUTED, linestyle="--")
    a.set_xticks([0, 6, 11], ["20 Jul", "31 Aug", "5 Oct"])
plt.show()
wk.loc[["2026-08-31", "2026-09-07", "2026-09-14"], ["acceptance", "rs_per_hour"]].round(3)
'''),
        md('''
        **What happened.** Acceptance dropped to its new level in the launch week (0.729) and stayed
        there; bookings per online hour fell to Rs 271 in the launch week and kept falling to Rs 262
        and Rs 259 over the next two. Acceptance settled two weeks before bookings per hour did, which
        is what a leading input is for: a city team watching it would have seen the gaming in week one.

        ## Which doubts does the fall survive, and which stay open?

        **Predict before you run.** Take out the 140 drivers who joined after the launch. What does
        trips per peak online hour read for the six weeks after? a) 1.90; b) 1.79; c) 1.58; d) 1.19.

        This cell restates the after-window rate under each cut the data can make. New in it: a
        dictionary holds each slice of the table under its name, and
        `{name: ... for name, d in slices.items()}` runs the same division, trips over hours, on every
        slice; `.nlargest(3)` picks the three weeks with the most requests, and the drivers who joined
        before the launch are the ids up to `d_1060`.
        '''),
        code('''
OUTER = ["Shamshabad", "Rajendranagar", "Patancheru"]
busiest = zw.groupby("week_start")["peak_requests"].sum().nlargest(3).index
slices = {
    "before, every driver": dw[dw["window"] == "before"],
    "after, every driver": after,
    "after, drivers who joined before the launch": after[after["driver_id"] <= "d_1060"],
    "after, the three weeks with most requests": dw[dw["week_start"].isin(busiest)],
    "after, core zones only": after[~after["zone_mode"].isin(OUTER)],
}
cuts = pd.Series({name: round(d["peak_trips"].sum() / d["peak_online_hours"].sum(), 2)
                  for name, d in slices.items()})
fig, ax = plt.subplots(figsize=(7.4, 3.2))
ax.barh(cuts.index[::-1], cuts.values[::-1], color=[VIOLET, VIOLET, VIOLET, ROSE, LAV])
ax.set_xlim(0, 2.2)
ax.set_xlabel("trips per peak online hour")
ax.set_title("The fall under each cut the data can make", loc="left")
plt.show()
cuts
'''),
        md('''
        **What happened.** The answer is c: without the 140 new drivers the rate after the launch is
        still 1.58, so the new drivers do not explain the fall. In the three weeks with the most rider
        requests of all twelve (the first three after the launch, still in the rains) the rate was
        already 1.60, so the monsoon's end cannot explain the fall: demand was at its highest and the
        fall was there. In the nine core zones the rate fell from 1.90 to 1.79, so most of the fall
        sits in the three outer zones. Three doubts stay open: drivers on two apps (the data holds
        weekly totals, so it cannot show a decline made because another app's trip was under way),
        who chose to enrol (every driver here enrolled, so no group stayed out to compare with), and
        cause (only a test of the redesign settles whether the scheme or the season moved the
        number).

        ## Does SQL reach the same totals as pandas?

        This cell loads `driver_weeks` into an in-memory SQLite database (a small database that lives
        inside Python) and sums the same columns with one `GROUP BY`, then compares the two routes;
        `1.0 *` makes SQL divide with decimals.
        '''),
        code('''
import sqlite3
con = sqlite3.connect(":memory:")
dw.to_sql("driver_weeks", con, index=False)
sql = pd.read_sql("""
    SELECT window, SUM(peak_online_hours) AS hours, SUM(peak_trips) AS trips,
           ROUND(1.0 * SUM(peak_trips) / SUM(peak_online_hours), 2) AS trips_per_hour
    FROM driver_weeks GROUP BY window ORDER BY window DESC""", con).set_index("window")
sql
'''),
        code('''
check("61 percent of the top-up went to driver-weeks under 0.5", round(low / (low + high), 2) == 0.61)
check("Rs 1.159 crore and Rs 74 lakh", (low, high) == (11590000, 7410000))
check("the north star reads 35.76 before and 35.89 after", list(board.iloc[:, 0]) == [35.76, 35.89])
check("acceptance settled in the launch week at 0.729", round(wk.loc["2026-08-31", "acceptance"], 3) == 0.729)
check("the fall survives without the 140 new drivers", cuts["after, drivers who joined before the launch"] == 1.58)
check("the three weeks with most requests already read 1.60", cuts["after, the three weeks with most requests"] == 1.60)
check("SQL and pandas agree on hours and trips", list(sql["hours"]) == [118000, 146300] and list(sql["trips"]) == [224200, 230900])
'''),
        md('''
        ## What does chapter 9 answer?

        1. Rs 1.159 crore, 61 percent of the top-up, went to driver-weeks that accepted fewer than
           half their offers; Rs 74 lakh went to the rest.
        2. Under a stated assumption about how idle drivers respond, the redesign saves Rs 92.7 lakh
           over six weeks if a fifth of the idle tail's top-up is still paid and Rs 58 lakh if half
           is; the test settles where.
        3. The north star barely moved (35.76 to 35.89 trips per online driver-week); acceptance fell
           from 0.863 to 0.730, waits went from 4.8 to 4.6 minutes, and the top-up cost Rs 82.3 a trip.
        4. Acceptance settled in the launch week, two weeks before bookings per hour did.
        5. The fall survives the new drivers (1.58) and the three weeks with most requests (1.60);
           drivers on two apps, who chose to enrol and cause stay open.
        6. SQL's `GROUP BY` returns the same hours and trips as pandas.

        **The check a senior analyst runs.** Price the trap in rupees, write every line of the
        definition, name what the data cannot show and the fact that would settle it, and reach the
        totals a second way before anything leaves the team.

        **In the interview.** [F] North star against guardrail, with one example pair: completed
        peak trips per enrolled driver per week, guarded by the share of offers accepted, which
        catches a driver who stays online and declines. The tentative faculty block this afternoon
        designs the test that would settle cause.
        '''),
    ])


# The page of seven lines and the check from notebook 06, shared by notebooks 10 and 11.
PAGE_CHECK = '''
LINES = ["numerator", "denominator", "window", "exclusions", "does_not_reward", "guardrails", "gaming_note"]

def written(value):
    """A line counts as written when it holds something other than the ____ placeholder."""
    return bool(value) and "____" not in str(value)

def missing_lines(page):
    """The page's blank lines, then every guardrail its gaming note does not say it catches."""
    blank_lines = [line for line in LINES if not written(page.get(line))]
    note = page.get("gaming_note") or {}
    unnamed = [g for g in page.get("guardrails") or [] if not written(note.get(g))]
    return blank_lines + [f"a guardrail that catches nothing named: {g}" for g in unnamed]

uber = {"numerator": "trips completed inside the peak windows, one per paying rider",
        "denominator": "enrolled drivers online at least one peak hour that week, the count printed beside the rate",
        "window": "the calendar week",
        "exclusions": "trips cancelled by either side, test accounts, trips outside the windows",
        "does_not_reward": "hours online, offers declined, a shrinking enrolled base",
        "guardrails": ["offers accepted over offers shown, at or above a floor",
                       "median rider wait at peak, by zone", "top-up per completed trip"],
        "gaming_note": {"offers accepted over offers shown, at or above a floor": "catches declining and cherry-picking",
                        "median rider wait at peak, by zone": "catches supply that stops serving riders",
                        "top-up per completed trip": "catches a top-up that runs away from the trips it pays for"}}
'''


def case10():
    build(NB / "C2_W04_D01_10_gaming_page_three_roles_STUDENT.ipynb", [
        md(f'''
        # The page under attack from three roles, with gaming and the seven lines: does each line resist the gaming it must, and does the page answer all three roles?

        **Week 4, Monday, chapter 10 of 11, the fourth case chapter.** It applies two of the morning's
        topics: *Gaming, and definitions that resist it*, taught in
        `C2_W04_D01_05_gaming_resistant_definitions_STUDENT.ipynb`, and *The metric definition
        artifact*, taught in `C2_W04_D01_06_metric_definition_artifact_STUDENT.ipynb`. Level 5 of the
        case's six: decide, cost the decision and defend it against the people it costs. Round 3 of
        the war game runs beside it.

        **The case.** Uber's Hyderabad city team launched a peak-hour earnings guarantee on Monday
        31 August 2026: a floor of Rs 300 per peak online hour, with Uber paying the gap between a
        driver's trip earnings and the floor as a top-up. Six weeks on, peak online hours are up 24
        percent and completed peak trips 3 percent.

        {LABEL}

        Notebook 09 wrote the redesign's seven-line page, found Rs 1.159 crore of the top-up paid to
        driver-weeks that accepted fewer than half their offers, and put the redesign's saving at
        Rs 58 to 92.7 lakh under a stated assumption. This notebook puts the page under attack: first
        from each way of gaming the scheme, then from the three people in the room who each lose
        something under it.

        **Who needs the answer.** The city head, who signs the page on Friday, and the three people
        who each lose something under it: the driver-operations lead, the marketing lead and the
        finance partner. A page that cannot answer them is dropped, and the city keeps paying for
        hours.

        **The questions on the way.**

        1. Does the redesign's page hold all seven lines?
        2. Does each line resist the gaming it must?
        3. Driver operations: if drivers log off, what would riders lose, and which line shows it?
        4. Marketing: does the floor stay for every driver who serves riders?
        5. Finance: is the fall the monsoon's end?
        6. Where does the floor sit if an accepted trip later cancelled counts as declined?
        '''),
        code(SETUP + STYLE + '''
dw = pd.read_csv("../data/C2_W04_D01_driver_weeks_STUDENT.csv")
zw = pd.read_csv("../data/C2_W04_D01_zone_weeks_STUDENT.csv")
dw["window"] = dw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
after = dw[dw["window"] == "after"]
per_driver = after.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
idle = set(per_driver.index[per_driver["peak_trips"] / per_driver["peak_online_hours"] < 1.0])

def group(driver_id):
    """The idle tail, the 140 who joined after the launch (ids above d_1060), or the other 880."""
    if driver_id in idle:
        return "idle tail"
    return "joined after the launch" if driver_id > "d_1060" else "the other 880"

dw["group"] = dw["driver_id"].map(group)
on_after = dw[(dw["window"] == "after") & (dw["peak_online_hours"] > 0)]
print(f"{len(idle)} drivers in the idle tail, found as notebook 08 found them; "
      f"{len(on_after):,} driver-weeks online after the launch")
'''),
        md('''
        ## Does the redesign's page hold all seven lines?

        This cell writes notebook 09's page as a seven-key dictionary, the shape chapter 6 used for
        Balaji Kirana (invented), and runs chapter 6's check, `missing_lines(page)`, copied here from
        notebook 06 so this notebook stands alone. The check lists every blank line and every
        guardrail the gaming note does not say it catches.
        '''),
        code(PAGE_CHECK + '''
for line in LINES:
    value = uber[line]
    if isinstance(value, dict):
        value = "; ".join(f"{g} {what}" for g, what in value.items())
    elif isinstance(value, list):
        value = "; ".join(value)
    print(f"{line.replace('_', ' ')}: {value}")
print("missing:", missing_lines(uber) or "nothing")
'''),
        md('''
        ## Does each line resist the gaming it must?

        Chapter 5 named the ways a number is gamed, and chapter 6 said a guardrail earns its place by
        the gaming it catches. The page survives only if each way of gaming the scheme meets a line
        that stops it. The redesign's north star is completed peak trips per enrolled driver online at
        peak, per week: trips over the driver-weeks with at least one peak online hour.

        **Predict before you run.** Suppose every idle-tail driver doubled the peak online hours of
        every week after the launch, with the same trips. What would the north star read after the
        launch?

        a) 35.89, as it reads now.
        b) Higher, about 41.
        c) Lower, about 30.
        d) Doubled, about 72.

        This cell writes the north star as a function and reads it on the six weeks after the launch
        three times: as the data stands, with the idle tail's hours doubled, and with the idle tail
        logged off, its driver-weeks taken out.
        '''),
        code('''
def north_star(d):
    """Completed peak trips per driver-week with at least one peak online hour, and that count."""
    online = d[d["peak_online_hours"] > 0]
    return round(online["peak_trips"].sum() / len(online), 2), len(online)

in_idle = after["driver_id"].isin(idle)
doubled = after.assign(peak_online_hours=after["peak_online_hours"].where(~in_idle, 2 * after["peak_online_hours"]))
moves = pd.DataFrame([("as the data stands", *north_star(after)),
                      ("the idle tail doubles its hours", *north_star(doubled)),
                      ("the idle tail logs off", *north_star(after[~in_idle]))],
                     columns=["after the launch", "north_star", "online_driver_weeks"]).set_index("after the launch")
moves
'''),
        md('''
        **What happened.** The answer is a. Doubling the idle tail's hours leaves the north star at
        35.89, because hours sit in neither its numerator (trips) nor its denominator (drivers online
        at least one peak hour): logging in for longer cannot raise it. Logging off can. With the idle
        tail's 1,080 driver-weeks taken out, the north star rises to 36.88, although the 33,440 trips
        those drivers made are gone unless other drivers carry them. That is why the page prints the
        count beside the rate (6,434 driver-weeks against 5,354), says it does not reward a shrinking
        base, and guards the riders' side with the wait.

        This cell draws each way of gaming the scheme against the lines of the page, with a filled
        square where a line stops the move. The last move is one the redesign itself invites: a driver
        parked in a thin zone who accepts the few offers shown there passes the acceptance floor, and
        only top-up per completed trip shows what that week cost. The redesign has not run, so the data
        cannot show that move yet.
        '''),
        code('''
MOVES = ["log in\\nfor longer", "stay online\\nand decline", "accept,\\nthen cancel", "log off",
         "accept a thin\\nzone's few offers"]
ROWS = ["numerator", "denominator", "window", "exclusions", "does not reward", "guardrail 1: accepted share",
        "guardrail 2: wait by zone", "guardrail 3: top-up per trip", "gaming note"]
STOPS = {"numerator": [0], "denominator": [0, 3], "exclusions": [2], "does not reward": [0, 1, 3],
         "guardrail 1: accepted share": [1, 2], "guardrail 2: wait by zone": [3],
         "guardrail 3: top-up per trip": [4]}
fig, ax = plt.subplots(figsize=(9.6, 4.8))
for r, line in enumerate(ROWS):
    y = len(ROWS) - 1 - r
    ax.text(-0.6, y, line, ha="right", va="center", color=INK)
    for c in range(len(MOVES)):
        hit = c in STOPS.get(line, [])
        ax.add_patch(plt.Rectangle((c - 0.4, y - 0.4), 0.8, 0.8, fc=VIOLET if hit else "white",
                                   ec=VIOLET if hit else "#D8D4EA", lw=1.2))
for c, move in enumerate(MOVES):
    ax.text(c, len(ROWS) - 0.45, move, ha="center", va="bottom", color=INK, fontsize=9.5)
ax.set_xlim(-3.9, len(MOVES) - 0.2)
ax.set_ylim(-0.6, len(ROWS) + 0.8)
ax.axis("off")
ax.set_title("Each way of gaming the scheme, and the lines of the page that stop it", loc="left")
plt.show()
for c, move in enumerate(MOVES):
    print(move.replace("\\n", " "), "is stopped by:", ", ".join(line for line, cols in STOPS.items() if c in cols))
'''),
        md('''
        **What happened.** Every move meets at least one line. The window and the gaming note stop no
        move of their own: the window makes the number computable, and the gaming note records which
        move each guardrail catches. Logging off is the one move the north star itself rewards, so the
        page meets it three times: the count printed beside the rate, the line on what it does not
        reward, and the wait.

        ## Driver operations: if drivers log off, what would riders lose, and which line shows it?

        The driver-operations lead says drivers will log off once the floor asks that half their offers
        be accepted. Part of that is true: the 180 drivers of the idle tail may well log off. The rest
        is a question the data can answer: did the drivers who serve riders change how they drove?

        This cell sums hours and trips by window for the idle tail and for the other 880 who joined
        before the launch, leaving out the 140 who joined after it, and draws each group's weekly
        trips per peak online hour.
        '''),
        code('''
both = dw[dw["group"] != "joined after the launch"]
groups = both.groupby(["group", "window"])[["peak_online_hours", "peak_trips"]].sum()
groups["trips_per_hour"] = (groups["peak_trips"] / groups["peak_online_hours"]).round(2)
groups = groups.loc[[("the other 880", "before"), ("the other 880", "after"), ("idle tail", "before"), ("idle tail", "after")]]
weekly = both.groupby(["week_start", "group"])[["peak_trips", "peak_online_hours"]].sum()
rate = (weekly["peak_trips"] / weekly["peak_online_hours"]).unstack()
fig, ax = plt.subplots(figsize=(8.0, 3.6))
ax.plot(range(12), rate["the other 880"], marker="o", color=VIOLET, label="the other 880")
ax.plot(range(12), rate["idle tail"], marker="s", color=ROSE, label="the idle tail, 180 drivers")
ax.axvline(5.5, color=MUTED, linestyle="--")
ax.set_xticks(range(12), [w[5:] for w in rate.index], rotation=45)
ax.set_ylim(0, 2.3)
ax.set_ylabel("trips per peak online hour")
ax.legend(frameon=False, loc="lower left")
ax.set_title("The other 880 held their rate; the idle tail's fell at the launch", loc="left")
plt.show()
idle_trips = groups.loc[("idle tail", "after"), "peak_trips"]
carry = int(round(idle_trips / 1.9))
print(groups)
print(f"if the idle tail logged off, its {idle_trips:,} trips would need about {carry:,} more peak online hours at 1.90 trips an hour")
'''),
        md('''
        **What happened.** The other 880 made 1.90 trips per peak online hour before the launch and
        1.90 after: the drivers who serve riders did not change. The idle tail fell from 1.90 to 0.80.
        If the idle tail logged off, its 33,440 trips would need about 17,600 more peak online hours
        from the others at 1.90 trips an hour. Whether riders would then wait longer is what guardrail
        2 answers: the median rider wait at peak, read zone by zone, moves for riders when supply that
        served them leaves, while the north star, as the cell above showed, would rise. The line that
        answers driver operations is guardrail 2, and the count printed beside the rate shows who left.

        ## Marketing: does the floor stay for every driver who serves riders?

        The marketing lead says changing the terms looks like bait, since the floor was the promise.
        The redesign keeps the Rs 300 floor for every driver-week that accepts at least half its
        offers, so the question for the data is how many driver-weeks outside the idle tail would lose
        it.

        **Predict before you run.** Of the driver-weeks online after the launch outside the idle tail,
        how many accepted fewer than half their offers? a) none; b) about 100; c) about 1,000; d) about
        2,000.

        This cell draws each driver-week's accepted share after the launch, the idle tail against every
        other driver-week, with the floor at 0.5.
        '''),
        code('''
share = on_after["peak_accepted"] / on_after["peak_offers"]
in_tail = on_after["driver_id"].isin(idle)
bins = [i / 40 for i in range(41)]
fig, ax = plt.subplots(figsize=(8.0, 3.6))
ax.hist(share[in_tail], bins=bins, color=ROSE, label="idle-tail driver-weeks")
ax.hist(share[~in_tail], bins=bins, color=VIOLET, alpha=0.85, label="every other driver-week")
ax.axvline(0.5, color=INK, linestyle="--")
ax.text(0.51, 0.93, "the floor, 0.5", color=INK, transform=ax.get_xaxis_transform())
ax.set_xlabel("offers accepted over offers shown, one driver-week after the launch")
ax.set_ylabel("driver-weeks")
ax.legend(frameon=False, loc="upper left")
ax.set_title("No week outside the idle tail falls under the floor", loc="left")
plt.show()
edges = (round(share[in_tail].max(), 2), round(share[~in_tail].min(), 2))
under = int((share[~in_tail] < 0.5).sum())
print(f"the idle tail's highest week accepted {edges[0]}; every other week at least {edges[1]}; "
      f"driver-weeks outside the idle tail under 0.5: {under}")
'''),
        md('''
        **What happened.** The answer is a: no driver-week outside the idle tail accepted fewer than
        half its offers. The idle tail's highest week accepted 0.46 and every other week at least 0.78,
        so a floor at 0.5 takes the top-up from idle-tail weeks only, and every driver who serves
        riders keeps the promise. The gap is this clean because the data is synthetic; on a real city
        the two groups overlap, and where the floor sits becomes a trade-off the test measures. The
        line that answers marketing is guardrail 1's floor, written into the payout rule.

        ## Finance: is the fall the monsoon's end?

        The finance partner says the fall in trips per hour is the season, since the monsoon ended
        inside the after window. Part of that is true: the season moves rider requests. The question is
        whether the rate moved with requests or with the launch.

        This cell draws the city's weekly rider requests beside its weekly trips per peak online hour.
        '''),
        code('''
weeks = dw.groupby("week_start")[["peak_trips", "peak_online_hours"]].sum()
weeks["trips_per_hour"] = (weeks["peak_trips"] / weeks["peak_online_hours"]).round(2)
weeks["requests"] = zw.groupby("week_start")["peak_requests"].sum()
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.4))
a1.bar(range(12), weeks["requests"] / 1000, color=LAV)
a1.set_ylim(0, 50)
a1.set_title("Rider requests at peak, thousands", loc="left")
a2.plot(range(12), weeks["trips_per_hour"], marker="o", color=ROSE)
a2.set_ylim(0, 2.3)
a2.set_title("Trips per peak online hour", loc="left")
for a in (a1, a2):
    a.axvline(5.5, color=MUTED, linestyle="--")
    a.set_xticks([0, 6, 11], ["20 Jul", "31 Aug", "5 Oct"])
plt.show()
busiest = weeks["requests"].nlargest(3).index
crest = round(weeks.loc[busiest, "peak_trips"].sum() / weeks.loc[busiest, "peak_online_hours"].sum(), 2)
step = (weeks.loc["2026-08-24", "trips_per_hour"], weeks.loc["2026-08-31", "trips_per_hour"])
print(f"weekly requests from {weeks['requests'].min():,} to {weeks['requests'].max():,}")
print(f"trips per peak online hour, the week before the launch {step[0]:.2f}, the launch week {step[1]:.2f}")
print(f"the three weeks with most requests ({', '.join(busiest)}) read {crest:.2f}")
'''),
        md('''
        **What happened.** Weekly requests stayed between 41,155 and 43,878 across all twelve weeks,
        while the rate stepped from 1.88 in the week before the launch to 1.64 in the launch week, and
        the three weeks with the most requests, the first three after the launch and still in the
        rains, read 1.60. The season moved requests within a narrow band; the rate fell in the week the
        scheme began. The line that answers finance is the window: a calendar week shows the step that
        six-week totals blur. The top-up budget is finance's own number, so finance watches guardrail 3,
        top-up per completed trip, and decides what the floor may cost.

        ### Your turn: where does the floor sit if an accepted trip later cancelled counts as declined?

        The payout rule counts an accepted trip that the driver later cancelled as declined, so a
        driver cannot pass the floor by accepting and cancelling. In this data every accepted trip
        either became a completed trip or was cancelled by the driver, so the rule's share is trips
        completed over offers shown. Fill the two blanks, then type and run the lines in the empty
        cell below:

        ```python
        done = on_after["peak_trips"] / on_after["____"]
        in_tail = on_after["driver_id"].isin(idle)
        idle_edge = round(done[in_tail].max(), 2)
        other_edge = round(done[~in_tail].____(), 2)
        print(idle_edge, other_edge)
        ```

        The check under it compares your two edges with the reference and asks whether 0.5 still sits
        between them.
        '''),
        empty(),
        code('''
mine = (globals().get("idle_edge"), globals().get("other_edge"))
if None in mine:
    print("Store idle_edge and other_edge in the empty cell above, then run this cell again.")
else:
    done = on_after["peak_trips"] / on_after["peak_offers"]
    tail = on_after["driver_id"].isin(idle)
    reference = (round(done[tail].max(), 2), round(done[~tail].min(), 2))
    print("the reference edges:", reference)
    check("your edges match the reference, and 0.5 still sits between them",
          tuple(mine) == reference and reference[0] < 0.5 < reference[1])
'''),
        md('''
        This cell checks the claims the chapter makes about its own numbers.
        '''),
        code('''
check("the redesign's page holds all seven lines", missing_lines(uber) == [])
check("doubling the idle tail's hours leaves the north star at 35.89",
      moves["north_star"].tolist()[:2] == [35.89, 35.89])
check("the idle tail logging off raises the north star to 36.88, on 5,354 driver-weeks against 6,434",
      moves.loc["the idle tail logs off"].tolist() == [36.88, 5354]
      and moves.loc["as the data stands", "online_driver_weeks"] == 6434)
check("every way of gaming the scheme meets a line that stops it",
      all(any(c in cols for cols in STOPS.values()) for c in range(len(MOVES))))
check("the other 880 held 1.90 trips an hour in both windows; the idle tail fell from 1.90 to 0.80",
      groups["trips_per_hour"].tolist() == [1.9, 1.9, 1.9, 0.8])
check("the idle tail's 33,440 trips would need about 17,600 hours at 1.90", (idle_trips, carry) == (33440, 17600))
check("idle-tail weeks accept at most 0.46, every other week at least 0.78, none of them under 0.5",
      edges == (0.46, 0.78) and under == 0)
check("the rate stepped from 1.88 to 1.64 in the launch week", step == (1.88, 1.64))
check("weekly requests stayed between 41,155 and 43,878; the three busiest weeks read 1.60",
      (weeks["requests"].min(), weeks["requests"].max()) == (41155, 43878) and crest == 1.6)
'''),
        md('''
        ## What does chapter 10 answer?

        1. The redesign's page holds all seven lines, and its gaming note says what each guardrail
           catches.
        2. Each way of gaming the scheme meets a line that stops it. Logging in for longer moves
           neither the numerator nor the denominator, so the north star stays at 35.89. Logging off
           raises it to 36.88, and the count beside the rate and the wait catch it. Declining and
           accepting then cancelling meet the floor; a thin zone's few accepted offers meet top-up per
           completed trip.
        3. Driver operations is answered by guardrail 2: the other 880 held 1.90 trips an hour, and if
           the idle tail logged off, its 33,440 trips would need about 17,600 hours from them.
        4. Marketing is answered by the floor: no driver-week outside the idle tail accepted under half
           its offers, so every driver who serves riders keeps the promise.
        5. Finance is answered by the window: requests stayed between 41,155 and 43,878 a week while
           the rate stepped from 1.88 to 1.64 in the launch week.
        6. Your turn found where the floor's edges sit when an accepted trip later cancelled counts as
           declined.

        **The rules.**

        - Test every line against the move it must resist, on the data, before anyone signs the page.
        - Each role's objection is partly right: name the true part, then the line that answers the
          rest.
        - A number that rises when people leave needs its count printed beside it and a guardrail on
          the people it serves.

        **In the interview.** [D] Three departments each want their own target; how do you get to one,
        and what do you say to the two who lose? One page, with each department's worry written as a
        guardrail or a line, and each answer backed by its number. Notebook 11 takes the whole day into
        the interview room.
        '''),
    ])


def case11():
    build(NB / "C2_W04_D01_11_new_feature_definition_page_STUDENT.ipynb", [
        md(f'''
        # The interview question on a new feature, with all six topics: what wins the interview, and does the same page hold for an AI coding assistant?

        **Week 4, Monday, chapter 11 of 11, the last case chapter.** It applies all six of the
        morning's topics, each taught in its own notebook: *What to measure and why; the proxy test*
        (01), *North-star and guardrail metrics* (02), *Leading against lagging indicators* (03),
        *Definitions: numerator, denominator, window, exclusions* (04), *Gaming, and definitions that
        resist it* (05) and *The metric definition artifact* (06). Level 6 of the case's six: the
        interview room, where the same case is asked cold.

        **The case.** Uber's Hyderabad city team launched a peak-hour earnings guarantee on Monday
        31 August 2026: a floor of Rs 300 per peak online hour, with Uber paying the gap between a
        driver's trip earnings and the floor as a top-up.

        {LABEL}

        **Who needs the answer.** You, in a product or analytics screen, where the question below is
        asked cold and a candidate who names one number and stops is screened out.

        **The questions on the way.**

        1. What does the interviewer ask, and what should a candidate clarify first?
        2. Which numbers does a hire-grade answer carry, and does the data hold each one?
        3. Where do the zones and the money take the answer?
        4. Which line answers each follow-up?
        5. Does the same page hold for an AI coding assistant, in your turn?
        '''),
        code(SETUP + STYLE + '''
dw = pd.read_csv("../data/C2_W04_D01_driver_weeks_STUDENT.csv")
zw = pd.read_csv("../data/C2_W04_D01_zone_weeks_STUDENT.csv")
dw["window"] = dw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
zw["window"] = zw["week_start"].lt("2026-08-31").map({True: "before", False: "after"})
print(f"{len(dw):,} driver-weeks and {len(zw)} zone-weeks, the tables notebooks 07 to 10 read")
'''),
        md('''
        ## What does the interviewer ask, and what should a candidate clarify first?

        > "Uber launched a peak-hour earnings guarantee for drivers in one city six weeks ago. How would
        > you measure whether it is a success?"

        A strong candidate asks before naming any number. What was the scheme meant to change: more
        drivers online, or riders picked up faster? Who is in it, and who pays? What would count as
        harm? Which decision rides on the answer, and against which baseline?

        **The trap the interviewer sets.** Peak online hours rose 24 percent. A candidate who names
        that number and stops has measured the scheme by what it paid for, chapter 1's proxy test
        failed in the first sentence.

        A hire-grade answer runs five steps: the goal, one north star with its lines, the guardrails, a
        leading input, and the test that would settle cause. This cell computes the number that fills
        each step and draws the five steps with their numbers.
        '''),
        code('''
online = dw[dw["peak_online_hours"] > 0]
sums = dw.groupby("window")[["peak_trips", "peak_accepted", "peak_offers", "topup_rs"]].sum()
board = pd.DataFrame({
    "north_star": (online.groupby("window")["peak_trips"].sum() / online.groupby("window").size()).round(2),
    "acceptance": (sums["peak_accepted"] / sums["peak_offers"]).round(3),
    "median_wait": zw.groupby("window")["median_wait_min"].median().round(2),
    "topup_per_trip_rs": (sums["topup_rs"] / sums["peak_trips"]).round(1),
}).loc[["before", "after"]]
wk = dw.groupby("week_start")[["peak_accepted", "peak_offers"]].sum()
launch_acceptance = round(wk.loc["2026-08-31", "peak_accepted"] / wk.loc["2026-08-31", "peak_offers"], 3)
b, a = board.loc["before"], board.loc["after"]
STEPS = [("1. The goal", "riders picked up\\nfaster at peak"),
         ("2. The north star", f"trips per online\\ndriver-week,\\n{b.north_star:.2f} to {a.north_star:.2f}"),
         ("3. The guardrails", f"accepted {b.acceptance:.3f}\\nto {a.acceptance:.3f}; wait {b.median_wait}\\n"
                               f"to {a.median_wait} minutes;\\ntop-up Rs {a.topup_per_trip_rs} a trip"),
         ("4. The leading input", f"acceptance settled\\nin the launch week,\\nat {launch_acceptance:.3f}"),
         ("5. The test", "zones as the unit,\\nold rule\\nagainst new")]
fig, ax = plt.subplots(figsize=(11.6, 3.2))
for i, (title, body) in enumerate(STEPS):
    x = i * 2.3
    lit = i == 0
    ax.add_patch(plt.Rectangle((x, 0), 2.0, 2.0, fc=INK if lit else "#EEEAFB", ec=INK if lit else VIOLET, lw=1.5))
    ax.text(x + 1.0, 1.72, title, ha="center", va="center", fontsize=10, fontweight="bold", color="white" if lit else INK)
    ax.text(x + 1.0, 0.8, body, ha="center", va="center", fontsize=9.5, color="white" if lit else INK)
    if i:
        ax.annotate("", xy=(x, 1.0), xytext=(x - 0.3, 1.0), arrowprops={"arrowstyle": "-|>", "color": MUTED})
ax.set_xlim(-0.1, 11.4)
ax.set_ylim(-0.1, 2.15)
ax.axis("off")
ax.set_title("A hire-grade answer in five steps, each filled from the data", loc="left")
plt.show()
board.T
'''),
        md('''
        **What happened.** The north star read 35.76 trips per online driver-week before and 35.89
        after. Acceptance fell from 0.863 to 0.730 and settled at 0.729 in the launch week itself, the
        median wait moved from 4.8 to 4.6 minutes, and the top-up cost Rs 82.3 per completed trip after
        the launch, against nothing before.

        ## Which numbers does a hire-grade answer carry, and does the data hold each one?

        **Predict before you run.** Peak online hours rose 24 percent. What did the north star do
        across the same two windows?

        a) It rose with the hours, by about a quarter.
        b) It rose with the trips, by about 3 percent.
        c) It barely moved.
        d) It fell with trips per hour, by about a sixth.

        This cell sets the four numbers a weak answer and a hire-grade answer would read side by side,
        each as after over before, with its two values written on its bar.
        '''),
        code('''
hours = dw.groupby("window")["peak_online_hours"].sum()
trips = dw.groupby("window")["peak_trips"].sum()
tph = (trips / hours).round(2)
reads = pd.DataFrame({
    "peak online hours": [hours["before"], hours["after"], f"{hours['before']:,} to {hours['after']:,}"],
    "completed peak trips": [trips["before"], trips["after"], f"{trips['before']:,} to {trips['after']:,}"],
    "the north star": [b.north_star, a.north_star, f"{b.north_star:.2f} to {a.north_star:.2f}"],
    "trips per peak online hour": [tph["before"], tph["after"], f"{tph['before']:.2f} to {tph['after']:.2f}"],
}, index=["before", "after", "label"]).T
ratio = (reads["after"].astype(float) / reads["before"].astype(float)).tolist()
fig, ax = plt.subplots(figsize=(8.4, 3.4))
y = list(range(len(reads)))[::-1]
ax.barh(y, ratio, color=[MUTED, VIOLET, INK, ROSE])
ax.axvline(1.0, color=INK, lw=1)
for yy, r, label in zip(y, ratio, reads["label"]):
    ax.text(max(r, 1.0) + 0.02, yy, label, va="center", color=INK)
ax.set_yticks(y, reads.index)
ax.set_xlim(0, 1.75)
ax.set_xlabel("after the launch over before")
ax.set_title("The weak answer reads the top bar; the hire-grade answer reads all four", loc="left")
plt.show()
reads[["before", "after"]]
'''),
        md('''
        **What happened.** The answer is c: the north star moved from 35.76 to 35.89 while hours rose
        from 118,000 to 146,300 and trips per peak online hour fell from 1.90 to 1.58. The weak answer
        reads the top bar and says the scheme works; the hire-grade answer reads all four and says the
        scheme bought hours while the number it exists for barely moved.

        ## Where do the zones and the money take the answer?

        A hire-grade answer then names who moved the number, where, and what each extra trip cost. This
        cell finds the idle tail as notebook 08 did, reads the outer zones' wait in each window as the
        middle of their 18 zone-week medians, and divides the top-up by the trips it bought: the idle
        tail's outer-zone top-up over the extra trips the outer zones fulfilled, and the whole top-up
        over the city's extra trips.
        '''),
        code('''
OUTER = ["Shamshabad", "Rajendranagar", "Patancheru"]
after = dw[dw["window"] == "after"]
per_driver = after.groupby("driver_id")[["peak_trips", "peak_online_hours"]].sum()
idle = set(per_driver.index[per_driver["peak_trips"] / per_driver["peak_online_hours"] < 1.0])
outer = zw[zw["zone"].isin(OUTER)]
outer_wait = outer.groupby("window")["median_wait_min"].median().round(2).loc[["before", "after"]]
o = outer.groupby("window")[["peak_requests", "peak_fulfilled"]].sum()
extra_outer = o.loc["after", "peak_fulfilled"] - o.loc["after", "peak_requests"] * o.loc["before", "peak_fulfilled"] / o.loc["before", "peak_requests"]
idle_outer_topup = after.loc[after["driver_id"].isin(idle) & after["zone_mode"].isin(OUTER), "topup_rs"].sum()
per_extra_outer = int(round(idle_outer_topup / extra_outer, -3))
per_extra_trip = int(round(after["topup_rs"].sum() / (trips["after"] - trips["before"])))
fig, ax = plt.subplots(figsize=(8.0, 3.6))
for zone, colour in zip(OUTER, [VIOLET, ROSE, LAV]):
    z = outer[outer["zone"] == zone].sort_values("week_start")
    ax.plot(range(12), z["median_wait_min"], marker="o", color=colour, label=zone)
for win, (x0, x1) in {"before": (0, 5), "after": (6, 11)}.items():
    ax.hlines(outer_wait[win], x0 - 0.2, x1 + 0.2, color=INK, linestyle=":",
              label="the middle of each\\nwindow's 18 waits" if win == "before" else None)
ax.axvline(5.5, color=MUTED, linestyle="--")
ax.set_xticks([0, 6, 11], ["20 Jul", "31 Aug", "5 Oct"])
ax.set_ylim(5.2, 7.0)
ax.set_ylabel("median rider wait at peak, minutes")
ax.legend(frameon=False, loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=9.5)
ax.set_title("The outer zones' wait fell a little after the launch", loc="left")
plt.show()
print(f"{len(idle)} drivers in the idle tail; the outer zones' wait {outer_wait['before']} to {outer_wait['after']} minutes")
print(f"the idle tail's outer-zone top-up per extra outer trip: about Rs {per_extra_outer:,}")
print(f"the whole top-up per extra trip across the city: Rs {per_extra_trip:,}, over {trips['after'] - trips['before']:,} extra trips")
'''),
        md('''
        **What happened.** The 180 drivers of the idle tail added hours on fewer trips, most of the new
        hours in the three outer zones. There the middle wait fell from 6.6 to 5.95 minutes, so riders
        in the thin zones gained a little, and the idle tail's top-up in those zones came to about
        Rs 46,000 for each extra trip they fulfilled. Across the city the Rs 1.9 crore came to Rs 2,836
        for each of the 6,700 extra trips. That is the decision line: hold the scheme, keep the floor
        only for weeks that accept at least half their offers, and test the redesign with zones as the
        unit.

        ## Which line answers each follow-up?

        | The interviewer pushes | The hire-grade line, from the numbers above |
        |---|---|
        | "Online hours rose 24 percent; what do you check before you celebrate?" | Trips per online hour and the rider's wait: hours rose 24 percent and trips 3, so the rate fell from 1.90 to 1.58 and waits barely moved |
        | "Which guardrail would driver operations fight, and why are they partly right?" | The acceptance floor: some declines are fair, so set it in the gap the data shows, above 0.46 and below 0.78, and test two levels, since on a real city the groups overlap |
        | "The drivers control when they log in; what happens to your number?" | Logging in cannot raise it, since each trip needs a rider's request; logging off can, so print the driver count beside the rate |

        Notebook 10 ran the third line on the data: doubling the idle tail's hours left the north star
        at 35.89, and taking the idle tail's driver-weeks out raised it to 36.88.

        ## Does the same page hold for an AI coding assistant?

        The interviewer's last push moves the question to an AI company: how would you measure an AI
        coding assistant without rewarding suggestions that were accepted and then deleted? The gamed
        proxy there is suggestions accepted, the way peak online hours were Uber's: a developer can
        accept a suggestion and delete it in the next edit. The answer runs on the same seven lines, so
        the check is chapter 6's `missing_lines(page)`, copied here from notebook 06 so this notebook
        stands alone. The variant is written for this programme and names no company and no figure.

        This cell writes the weak answer and Uber's page as pages and draws both, line by line.
        '''),
        code(PAGE_CHECK + '''
weak = {"numerator": "peak online hours", "window": "six weeks"}    # "hours are up 24 percent, so it works"
SHORT = {"numerator": "trips completed", "denominator": "drivers online, count printed",
         "window": "the calendar week", "exclusions": "cancelled, test, off-window",
         "does_not_reward": "hours, declines, a smaller base", "guardrails": "acceptance; wait; top-up a trip",
         "gaming_note": "what each one catches"}
fig, ax = plt.subplots(figsize=(9.6, 4.4))
for r, line in enumerate(LINES):
    y = len(LINES) - 1 - r
    ax.text(-0.15, y, line.replace("_", " "), ha="right", va="center", color=INK)
    for c, (page, text) in enumerate(((weak, weak.get(line) or "blank"), (uber, SHORT[line]))):
        filled = bool(page.get(line))
        ax.add_patch(plt.Rectangle((c * 2.6, y - 0.4), 2.5, 0.8, fc=VIOLET if filled else "white",
                                   ec=VIOLET if filled else ROSE, lw=1.4))
        ax.text(c * 2.6 + 1.25, y, text, ha="center", va="center", color="white" if filled else ROSE)
ax.text(1.25, 7.0, "the weak answer", ha="center", fontweight="bold", color=INK)
ax.text(3.85, 7.0, "the hire-grade page", ha="center", fontweight="bold", color=INK)
ax.set_xlim(-2.6, 5.2)
ax.set_ylim(-0.6, 7.5)
ax.axis("off")
ax.set_title("The weak answer writes 2 of the 7 lines; the hire-grade page writes all 7", loc="left")
plt.show()
for name, page in (("the weak answer", weak), ("the hire-grade page", uber)):
    print(f"{name}: {missing_lines(page) or 'nothing missing'}")
'''),
        md('''
        ### Your turn: does your page for the AI coding assistant pass the check?

        Write the coding assistant's page as seven lines. Its north star is the suggested code still
        present at the next commit, per developer with a seat, per week; a commit is a saved change to
        the code. Two lines are filled for you. Fill the other five, naming in the gaming note each
        guardrail you list and the gaming it catches. In the empty cell below, edit and run:

        ```python
        ai_page = {"numerator": "suggested lines still present at the next commit",
                   "denominator": "____",
                   "window": "the calendar week",
                   "exclusions": "____",
                   "does_not_reward": "____",
                   "guardrails": ["____"],
                   "gaming_note": {"____": "____"}}
        ```

        The check under it runs `missing_lines` on your page and passes when nothing is missing. Then
        say which of your lines catches a developer who accepts every suggestion and deletes it in the
        next edit.
        '''),
        empty(),
        code('''
mine = globals().get("ai_page")
if mine is None:
    print("Store ai_page in the empty cell above, then run this cell again.")
else:
    gaps = missing_lines(mine)
    print("nothing missing: the page holds all seven lines" if not gaps else f"not yet, still missing: {gaps}")
'''),
        md('''
        This cell checks the claims the chapter makes about its own numbers.
        '''),
        code('''
check("hours 118,000 to 146,300, trips 224,200 to 230,900, trips per hour 1.90 to 1.58",
      (hours.tolist(), trips.tolist(), tph.tolist()) == ([146300, 118000], [230900, 224200], [1.58, 1.9]))
check("the north star 35.76 to 35.89; acceptance 0.863 to 0.730; the wait 4.8 to 4.6 minutes",
      board["north_star"].tolist() == [35.76, 35.89] and board["acceptance"].tolist() == [0.863, 0.73]
      and board["median_wait"].tolist() == [4.8, 4.6])
check("acceptance settled at 0.729 in the launch week; the top-up cost Rs 82.3 a trip after it",
      launch_acceptance == 0.729 and a.topup_per_trip_rs == 82.3)
check("180 drivers in the idle tail; the outer zones' wait 6.6 to 5.95 minutes",
      len(idle) == 180 and outer_wait.tolist() == [6.6, 5.95])
check("about Rs 46,000 per extra outer trip, and Rs 2,836 per extra trip across the city",
      (per_extra_outer, per_extra_trip) == (46000, 2836))
check("the weak answer writes 2 of the 7 lines, and the hire-grade page all seven",
      len(missing_lines(weak)) == 5 and missing_lines(uber) == [])
'''),
        md(f'''
        ## What does chapter 11 answer?

        1. Clarify first: what the scheme is for, who is in it and who pays, what counts as harm, and
           which decision rides on the answer against which baseline.
        2. The hire-grade answer runs five steps, each filled from the data: riders picked up faster;
           the north star at 35.76 then 35.89; acceptance 0.863 to 0.730, the wait 4.8 to 4.6 minutes
           and Rs 82.3 of top-up a trip; acceptance settled in the launch week; a test by zone.
        3. It reads all four bars: hours rose from 118,000 to 146,300 while trips per hour fell from
           1.90 to 1.58 and the north star barely moved.
        4. It names the segment and the money: 180 drivers, the outer zones' wait 6.6 to 5.95 minutes
           at about Rs 46,000 per extra outer trip, and Rs 2,836 per extra trip across the city.
        5. Each follow-up has a line from the data, and the coding assistant's page runs on the same
           seven lines and the same check.

        **The rules.**

        - Clarify the goal before naming a number, then name the number the goal needs.
        - Read the paid number beside the number it stands for, never alone.
        - Close on a decision with its cost, and on the test that would settle cause.

        **In the interview.** [S] How would you measure the success of a new feature? {TAGS} The six
        topics are the skeleton of the answer: the proxy test on the obvious number, a north star with
        its guardrails, the leading input, the four lines, the gaming each line resists, and the page
        that holds them. The Kahoot follows, and the practice lab's notebook,
        `C2_W04_D01_12_kalpa_lab_STUDENT.ipynb`, runs the same method on Kalpa Retail.
        '''),
    ])


# ================================================================================ the Kalpa lab
def lab12():
    """The lab as merged on 13 October 2026 (pull request 246), under its new number; rebuilt only on request."""
    build(NB / "C2_W04_D01_12_kalpa_lab_STUDENT.ipynb", [
        md('''
        # Does "reorders per member" reward what the head of Retail-Plus needs from the tier?

        Week 4, Monday, the TA-led practice lab. The method of the morning, moved to Kalpa Retail,
        the programme's fictional client: Kalpa and its people are invented, and the data are
        synthetic.

        **The situation.** The head of Retail-Plus, who owns Kalpa's paid membership tier, wants a
        growth number for the tier: reorders placed per member. A member places a reorder by tapping
        the app's Reorder button, and the app can also place one on its own, an auto-reorder; its
        auto-reorder feature ran from 10 to 30 September 2026. The comparison is the three weeks
        before that, 20 August to 9 September 2026, and both windows sit after the monsoon sale's
        last day, 19 August.

        **The data.**

        | Table | Columns | Rows |
        |---|---|---|
        | `kalpa_members` | `customer_id`, `tier`, `member_since` (the day the membership started; the table records no end date) | the tier's 120 members, the same table this week's Thursday lab reads |
        | `kalpa_app_reorders` | `reorder_id`, `customer_id`, `placed_ts`, `value_rs` (the placement's booked value, whatever happened to it), `auto` (True when the app placed it on its own), `status`, `order_id` (the order in Kalpa's warehouse that the placement became, blank if none) | one row per reorder placement, 20 August to 30 September 2026 |

        A placement's `status` is delivered or returned (it became an order, which was delivered, or
        delivered and sent back), cancelled (the order it became was cancelled, or the placement was
        cancelled before it became one; `order_id` tells the two apart), merged (its items joined a
        basket the member already had open, so it never became an order of its own, and they reach
        the member only if the member checks that basket out) or pending (still waiting). Orders
        members place themselves through the normal checkout are not in `kalpa_app_reorders`, which
        logs reorder placements only.

        **Who needs the answer.** The head of Retail-Plus, who is about to take "reorders per
        member" to the growth review, the meeting where each team's numbers are judged, as the
        tier's number. If the number does not track what members receive, the review judges the tier
        on the wrong thing.

        **The questions on the way.**

        1. What does the table hold, before anything is counted?
        2. What do seven members' rows say, counted by hand?
        3. What do reorders placed per member and booked value per member do across the two windows?
        4. Which reorders are these, and what happened to them?
        '''),
        code(SETUP + STYLE + '''
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

members = pd.read_csv("../data/C2_W04_D01_kalpa_members_STUDENT.csv")
reorders = pd.read_csv("../data/C2_W04_D01_kalpa_app_reorders_STUDENT.csv")
reorders["day"] = reorders["placed_ts"].str[:10]
print(f"{len(members)} Retail-Plus members; {len(reorders)} reorder placements from {reorders.day.min()} to {reorders.day.max()}")
'''),
        md('''
        ## What does the table hold, before anything is counted?

        This cell draws three plain views of the whole table, both windows together: what a
        placement is worth, how many placements each member made, and how many members the tier
        held on each day of the two windows. It also keeps the members who had joined by 19 August
        as `base`, the members the per-member comparison counts.
        '''),
        code('''
fig, ax = plt.subplots(figsize=(6.4, 2.8))
ax.hist(reorders["value_rs"], bins=range(0, 5001, 250), color=VIOLET, edgecolor="white")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel("booked value of one placement, Rs")
ax.set_title("What a placement is worth, both windows together", loc="left")
plt.show()
fig, ax = plt.subplots(figsize=(6.4, 2.8))
ax.hist(reorders.groupby("customer_id").size(), bins=range(1, 7), color=LAV, edgecolor="white", align="left")
ax.set_xlabel("placements per member, both windows together (members with at least one)")
ax.set_title("How many placements each member made", loc="left")
plt.show()
days = pd.date_range("2026-08-19", "2026-09-30")
joined = [(members["member_since"] <= d.strftime("%Y-%m-%d")).sum() for d in days]
fig, ax = plt.subplots(figsize=(6.4, 2.8))
ax.axvspan(pd.Timestamp("2026-08-20"), pd.Timestamp("2026-09-10"), color=LAV, alpha=0.25, lw=0)
ax.axvspan(pd.Timestamp("2026-09-10"), pd.Timestamp("2026-10-01"), color=MUTED, alpha=0.10, lw=0)
ax.step(days, joined, where="post", color=VIOLET, lw=2)
ax.text(pd.Timestamp("2026-08-21"), 124, "comparison, 20 Aug to 9 Sep", color=INK, fontsize=9)
ax.text(pd.Timestamp("2026-09-11"), 124, "auto-reorder window, 10 to 30 Sep", color=INK, fontsize=9)
ax.text(pd.Timestamp("2026-08-19"), joined[0] - 4, f"{joined[0]} by 19 Aug", color=INK, fontsize=9)
ax.text(pd.Timestamp("2026-09-29"), joined[-1] - 4, f"{joined[-1]} from 29 Aug", color=INK, fontsize=9, ha="right")
ax.set_ylim(95, 128)
ax.set_ylabel("members who had joined")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
ax.set_title("How many members the tier held on each day of the two windows", loc="left")
plt.show()
base = members.loc[members["member_since"] <= "2026-08-19", "customer_id"]
print(len(base), "members had joined by 19 August")
'''),
        md('''
        ## What do seven members' rows say, counted by hand?

        Your TA hands out a sheet with seven members' placements and booked values in the two
        windows: C-0152, C-0184, C-0211, C-0215, C-0224, C-0240 and C-0264, all seven in the tier
        for the whole of both windows. Before the ratio code runs, add up each window's placements
        and booked value for the seven, divide by seven, and write the two ratios (window over
        comparison) on the TA's sheet. The seven cancels out of each ratio, so the per-member form
        gives the same answer as the totals; it is the form the head of Retail-Plus reports. Working
        without the sheet, type these two lines into the empty cell below and run them, where False
        is the comparison window and True the auto-reorder window:

        ```python
        seven = ["C-0152", "C-0184", "C-0211", "C-0215", "C-0224", "C-0240", "C-0264"]
        print(reorders[reorders["customer_id"].isin(seven)].groupby(["customer_id", reorders["day"] >= "2026-09-10"])["value_rs"].agg(["size", "sum"]))
        ```
        '''),
        empty(),
        md('''
        ## What do reorders placed per member and booked value per member do across the two windows?

        The per-member figures divide both windows by the same 107 members in `base`, the ones
        already in the tier when the comparison window opened on 20 August, because a member who
        joined later had fewer of its days to reorder in: one who joined on 25 August had 16 of its 21.

        **Predict before you run.** From the comparison window to the auto-reorder window, reorders
        placed per member a) fell; b) stayed exactly level; c) rose, by a third or less; d) rose by
        more than a third. And booked value per member a) fell; b) stayed exactly level; c) rose, by
        a third or less; d) rose by more than a third.

        **Your turn.** Type these lines into the empty cell below and run it:

        ```python
        comparison = reorders[reorders["day"].between("2026-08-20", "2026-09-09") & reorders["customer_id"].isin(base)]
        window = reorders[reorders["day"].between("2026-09-10", "2026-09-30") & reorders["customer_id"].isin(base)]
        placed = (len(window) / len(base)) / (len(comparison) / len(base))
        booked = (window["value_rs"].sum() / len(base)) / (comparison["value_rs"].sum() / len(base))
        print(round(placed, 2), round(booked, 2))
        ```

        `.between(start, end)` keeps the days from the first date to the second, both included, and
        `.isin(base)` keeps the 107 members' rows.
        '''),
        empty(),
        md('''
        ## Which reorders are these, and what happened to them?

        **Your turn.** Type these lines into the empty cell below and run it, then say in one
        sentence to your neighbour what the window's placements were and what became of them. The
        third line counts the placements in each window that became an order in the warehouse:

        ```python
        print(window.groupby(["auto", "status"]).size())
        print(comparison.groupby(["auto", "status"]).size())
        print(window["order_id"].notna().sum(), comparison["order_id"].notna().sum())
        print(round(window["value_rs"].mean()), round(comparison["value_rs"].mean()))
        ```
        '''),
        empty(),
        md('''
        This cell checks the table itself, so a wrong count in your cells cannot come from a broken file.
        '''),
        code('''
since = reorders["customer_id"].map(members.set_index("customer_id")["member_since"])
check("120 Retail-Plus members, one row each", len(members) == 120 and members["customer_id"].is_unique)
check("every placement has a unique id", reorders["reorder_id"].is_unique)
check("every placement falls between 20 August and 30 September", reorders["day"].between("2026-08-20", "2026-09-30").all())
check("every status is delivered, returned, cancelled, merged or pending",
      reorders["status"].isin(["delivered", "returned", "cancelled", "merged", "pending"]).all())
check("every booked value is positive", (reorders["value_rs"] > 0).all())
check("every placement belongs to a member and falls on or after the day the member joined",
      since.notna().all() and (reorders["day"] >= since).all())
check("no warehouse order appears twice", reorders["order_id"].dropna().is_unique)
'''),
        md('''
        ## What does the lab hand on?

        Write on the TA's sheet: your two ratios from the hand count and from the full table, the one
        sentence on what the window's placements were and what became of them, and which line of a
        complete definition would have stopped "reorders per member" rising for that.

        **The check a senior analyst runs.** The baseline (the comparison window), the denominator
        (the same 107 members in both windows), the evidence that the thing the number stands for
        moved (booked value and what became an order), and a second way to the same answer: the
        ratio of the two windows' totals equals the ratio of the per-member figures, because both
        windows divide by the same 107. The seven's hand count leans the same way and lands
        elsewhere, because seven members are a sample of the tier.

        The unguided exercise that follows writes the growth plan's own north star, delivered orders
        per active customer per month, on the same seven-line template as the morning's.
        '''),
    ])


BUILDERS = {"01": c01, "02": c02, "03": c03, "04": c04, "05": c05, "06": c06,
            "07": case07, "08": case08, "09": case09, "10": case10, "11": case11, "12": lab12}
DEFAULT = [k for k in BUILDERS if k != "12"]   # the lab ships as merged unless asked for by number

if __name__ == "__main__":
    for key in sys.argv[1:] or DEFAULT:
        BUILDERS[key]()
        print("built", key)

# Test inputs and expected outcomes
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py
#     builds and executes notebooks 01 to 11, printing "built 01" to "built 11"; every check PASS,
#     and the lab notebook 12 is left as merged
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 04
#     rebuilds notebook 04 alone
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 12
#     rebuilds the Kalpa lab from its cells as merged, under its new number
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 10 11
#     rebuilds the two afternoon notebooks; notebook 10's checks include the north star at 35.89 with the
#     idle tail's hours doubled and 36.88 with the idle tail logged off
# python3 content/W04/D1/internal/C2_W04_D01_build_notebooks_INTERNAL.py 13
#     stops with a KeyError, since the day has no chapter 13
# the same run after a toy number in the generator changes (say tokens after the pay rule become 450)
#     stops before building, naming the toy_ id whose value differs from the number this script writes

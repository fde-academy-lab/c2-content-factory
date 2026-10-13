"""Write Tuesday's nine notebooks and execute each cold in its own folder.

Notebooks 01, 02, 03, 06 and 07 teach the row's five subtopics on invented examples (Ramesh's kirana
shop, Gulmohar Secondary School, a campus canteen's tea, Ramesh's page); 04, 05 and 08 apply them to
the Uber case, one per case chapter with a notebook; 11 runs the guesstimate on Kalpa in the lab.
Chapters 9 and 10 have no notebook: the page is written by hand and the interview room is spoken.
A notebook's number is its chapter's SECTION number, and the lab takes the number after SECTION 10.

    python3 content/W04/D2/internal/C2_W04_D02_build_notebooks_INTERNAL.py          # all nine
    python3 content/W04/D2/internal/C2_W04_D02_build_notebooks_INTERNAL.py 01 06    # just these

The markdown here is the notebooks' prose, so the humanizer's file-mode read runs on this script.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import md, code, empty, build  # noqa: E402

NB = ROOT / "content" / "W04" / "D2" / "notebooks"
LABEL = ("> *Illustrative case: the company is real, the situation and the data are synthetic, built "
         "for this class.*")

SETUP = '''import textwrap
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.width", 140)
plt.rcParams.update({"figure.figsize": (9, 3.8), "font.size": 11,
                     "axes.spines.top": False, "axes.spines.right": False})
INK, VIOLET, LILAC, PALE, ROSE, AMBER = "#1A0F5C", "#5B3FD6", "#B9AEF0", "#EEEAFB", "#D63A6A", "#C98A00"

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
'''

SHOP = ("Ramesh's kirana shop is invented: it opened two more hours a day from October, and every day "
        "and every rupee in this notebook is an invented number written by the day's seeded generator.")


# ------------------------------------------------------------------ concept notebook 01
def nb01():
    return [
        md(f"""
        # The one-slide answer: claim, evidence, caveat, action: what does a slide carry?

        **Week 4, Tuesday, concept notebook 1 of 5, beside chapter 1 of the deck.** {SHOP}

        **Who needs the answer.** Ramesh (invented), who must decide whether the longer hours
        stay, and his son, who argued for them and loses if they go. A slide that quotes the wrong
        denominator lets each of them read a different verdict from the same rupees, and the helper
        is paid for two hours nobody has priced.

        **The questions on the way.** What do the 56 days say per day, per hour and per customer?
        Which denominator prices Ramesh's decision? Does the fall per hour hold on every day? What
        does the slide say in its four parts? What does the trap sentence get wrong?
        """),
        code(SETUP + '''
# Ramesh's 56 days: four weeks in September at 10 hours a day, four in October at 12; all invented
days = pd.read_csv("../data/C2_W04_D02_kirana_days_STUDENT.csv")
check("56 days, 28 in each month", len(days) == 56 and (days.month.value_counts() == 28).all())
check("10 hours a day in September and 12 in October",
      set(days[days.month == "September"].hours_open) == {10} and set(days[days.month == "October"].hours_open) == {12})
print(days.to_string(index=False))           # the whole table, one row per day, every number invented
'''),
        md("""
        ## What do the 56 days say per day, per hour and per customer?

        A **rate** is one number divided by another, and the number below the line is its
        **denominator**: sales per day divide by days, sales per hour by hours open, sales per
        customer by customers. Since Week 1 a rate that does not name its denominator has been a
        rumour.

        Count by hand first, on each month's totals. September sold Rs 3.33 lakh over 28 days, Rs
        11,900 a day, and at 10 hours a day that is Rs 1,190 an hour. October sold Rs 3.53 lakh
        over 28 days, Rs 12,600 a day, and at 12 hours a day Rs 1,050 an hour. Each month's
        customers spent Rs 100 each: 3,332 customers in September and 3,528 in October.

        **Predict before you run.** The son says the shop earns more; the father says each hour
        earns less. Who is right?

        a) The son, since sales a day rose
        b) The father, since sales an hour fell
        c) Both, each on a different denominator
        d) Neither, since sales per customer did not move
        """),
        code('''
# Add up each month, then divide the same rupees by days, by hours open and by customers
m = days.groupby("month").agg(sales=("sales_rs", "sum"), days=("day", "count"),
                              hours=("hours_open", "mean"), customers=("customers", "sum"))
m = m.loc[["September", "October"]]
m["per_day"] = m.sales / m.days                  # Rs a day
m["per_hour"] = m.per_day / m.hours              # Rs an hour open
m["per_customer"] = m.sales / m.customers        # Rs a customer
print(m.round(1).to_string())
chg = (m.loc["October"] / m.loc["September"] - 1) * 100
print(f"October on September: per day {chg.per_day:+.1f} percent, per hour {chg.per_hour:+.1f} percent, per customer flat")
check("by hand and by code: Rs 11,900 and Rs 12,600 a day", list(m.per_day) == [11900, 12600])
check("by hand and by code: Rs 1,190 and Rs 1,050 an hour", list(m.per_hour) == [1190, 1050])
check("by hand and by code: Rs 100 a customer in both months", list(m.per_customer) == [100, 100])

reads = ["per_day", "per_hour", "per_customer"]
index = m.loc["October", reads] / m.loc["September", reads] * 100     # September = 100
fig, ax = plt.subplots(figsize=(8, 3.6))
bars = ax.bar(["per day", "per hour", "per customer"], index, color=[LILAC, VIOLET, PALE], edgecolor=VIOLET)
ax.bar_label(bars, fmt="%.1f")
ax.axhline(100, color="gray", ls=":")
ax.set_ylim(80, 110)
ax.set_ylabel("October, with September = 100")
ax.set_title("The same rupees on three denominators: up, down and flat (invented)", loc="left")
plt.show()
'''),
        md("""
        **What happened.** The answer is c. Per day the shop is up Rs 700, 5.9 percent, which is
        the son's sentence; per hour it is down 11.8 percent, which is the father's; per customer
        it is flat at Rs 100. Three honest divisions of the same rupees gave three verdicts, so the
        denominator decides which sentence the slide carries.

        ## Which denominator prices Ramesh's decision?

        The decision on the table is whether the two extra hours pay, and a decision about hours is
        priced per hour. The cell writes that choice as a function: name the unit the decision buys
        or loses, then read the rate in that unit.

        **Predict before you run.** Ramesh's accountant asks a different question: did each
        customer spend less after the change? Which rate answers her?

        a) Sales per day
        b) Sales per hour
        c) Sales per customer
        d) Total sales over the four weeks
        """),
        code('''
def evidence_for(unit, table):
    """The rate a decision is priced in: its denominator is the unit the decision buys or loses."""
    before, after = table[f"per_{unit}"]
    return f"sales per {unit}: Rs {before:,.0f} in September, Rs {after:,.0f} in October"

print("Ramesh, do the two extra hours pay?        ", evidence_for("hour", m))
print("The accountant, does each customer spend less?", evidence_for("customer", m))
check("the hours decision reads per hour", evidence_for("hour", m).startswith("sales per hour"))
check("per customer did not move between the months", m.per_customer.nunique() == 1)
'''),
        md("""
        **What happened.** The answer is c: her question is about customers, so it is read per
        customer, and it says nobody spent less. Ramesh's question is about hours, so his slide is
        priced per hour, with sales per customer beside it.

        ## Does the fall per hour hold on every day, or only on a few?

        A monthly average can hide a handful of bad days. The chart draws sales per hour for each of
        the 56 days, with the rain days as dots and October's festival fortnight shaded, and it
        carries the claim as its title.

        **Predict before you run.** How many October days earned more per hour than the weakest dry
        September day?

        a) None
        b) About a quarter of them
        c) About half
        d) Only the festival days
        """),
        code('''
days["per_hour"] = days.sales_rs / days.hours_open
days["x"] = range(1, len(days) + 1)
fest = days[days.festival_day == "yes"].x
rain = days[days.rain_day == "yes"]
fig, ax = plt.subplots(figsize=(10, 4))
ax.axvspan(fest.min() - 0.5, fest.max() + 0.5, color="#FFF7E6", label="festival fortnight")
ax.plot(days.x, days.per_hour, color=VIOLET, lw=2.5)
ax.scatter(rain.x, rain.per_hour, color=ROSE, zorder=3, label="rain day")
ax.axvline(28.5, color="gray", ls="--")
ax.text(29, 1285, "two more hours a day from October", color="gray")
ax.set_xticks([1, 15, 29, 43, 56], ["1 Sep", "15 Sep", "1 Oct", "15 Oct", "28 Oct"])
ax.set_ylim(880, 1300)
ax.set_ylabel("sales per hour open, Rs")
ax.set_title("The longer hours add sales a day and earn less in every hour (invented)", loc="left")
ax.legend(loc="lower left")
plt.show()

sep, octo = days[days.month == "September"], days[days.month == "October"]
weakest_dry = sep[sep.rain_day == "no"].per_hour.min()
above = int((octo.per_hour > weakest_dry).sum())
print("October days above the weakest dry September day, per hour:", "none" if above == 0 else above)
check("every October day earns less per hour than every dry September day", above == 0)
check("the festival days sell more a day than October's other days",
      octo[octo.festival_day == "yes"].sales_rs.mean() > octo[octo.festival_day == "no"].sales_rs.mean())
'''),
        md("""
        **What happened.** The answer is a. Every October day, the festival days included, earned
        less per hour than every dry September day, so the fall is no handful of bad days. The
        festival days do sell more a day than October's other days, and that is the caveat: part of
        the extra Rs 700 a day may be the season, which this data cannot separate yet.

        ## What does the slide say in its four parts?

        Named last, the rule the chapter builds: a slide that carries a decision has four parts, in
        the order a reader needs them. The **claim** is the title, a sentence with a verb saying
        what is true and what to do. The **evidence** is one number with its denominator, or one
        chart. The **caveat** is what the evidence cannot show yet, beside it. The **action** says
        what to do, its cost in rupees and weeks, and who signs. Together they are the one-slide
        answer: claim, evidence, caveat, action. The function below assembles them and the picture
        draws them where a reader meets them.
        """),
        code('''
def one_slide(claim, evidence, caveat, action):
    """The one-slide answer: four parts, in the order a reader needs them."""
    slide = {"claim": claim, "evidence": evidence, "caveat": caveat, "action": action}
    for part, text in slide.items():
        print(f"{part:>8}: {text}")
    return slide

slide = one_slide(
    claim="The longer hours add Rs 700 a day but earn less per hour, so count the evening on its own before deciding",
    evidence=evidence_for("hour", m) + "; sales per customer held at Rs 100",
    caveat="A festival fortnight fell inside October, so part of the extra Rs 700 a day may be the season",
    action="Keep the hours through November, count the evening's sales apart and decide after thirty days; "
           "the helper's two extra hours cost Rs 170 a day, and Ramesh signs")

fig = plt.figure(figsize=(10, 5.2))
fig.text(0.02, 0.97, "1  " + textwrap.fill(slide["claim"], 80), fontsize=13, weight="bold", color=INK, va="top")
ev = fig.add_axes([0.07, 0.08, 0.52, 0.66])
ev.plot(days.x, days.per_hour, color=VIOLET, lw=2)
ev.axvline(28.5, color="gray", ls="--")
ev.set_xticks([1, 29, 56], ["1 Sep", "1 Oct", "28 Oct"])
ev.set_title("2  Sales per hour open, each day, Rs", loc="left", fontsize=11)
fig.text(0.64, 0.70, "3  Caveat\\n" + textwrap.fill(slide["caveat"], 34), fontsize=10.5, va="top",
         bbox=dict(boxstyle="round", fc="#FFF7E6", ec=AMBER))
fig.text(0.64, 0.36, "4  Action\\n" + textwrap.fill(slide["action"], 34), fontsize=10.5, va="top",
         bbox=dict(boxstyle="round", fc="white", ec=VIOLET))
plt.show()
check("the evidence names its denominator", " per " in slide["evidence"])
check("the action carries a cost in rupees and who signs", "Rs" in slide["action"] and "signs" in slide["action"])
check("the son can repeat the title, since it carries his Rs 700", "Rs 700" in slide["claim"])
'''),
        md("""
        ## What does the trap sentence get wrong?

        **The plausible wrong answer.** "Sales a day rose from Rs 11,900 to Rs 12,600, so the longer
        hours work; keep them." Every rupee in it is right, and a hurried read reaches it in one
        line.

        **Predict before you run.** What bought the extra Rs 700 a day?

        a) More customers, each spending more
        b) Two more hours a day, each hour earning less
        c) Higher prices on the same goods
        d) The festival fortnight alone
        """),
        code('''
hurried = m.per_day.diff().iloc[-1]                  # sales a day, October less September
extra_hours = m.hours.diff().iloc[-1]
print(f"the hurried read: Rs {hurried:,.0f} more a day, so keep the hours")
print(f"what bought the rise: {extra_hours:.0f} more hours a day, each earning {abs(chg.per_hour):.1f} percent less")
check("the hurried read is true to the rupee", hurried == 700)
check("and it was bought with two more hours a day", extra_hours == 2)
'''),
        md("""
        **Why it is wrong.** The answer is b: the rise was bought with two more hours a day, and the
        decision is about those hours: per hour the shop earns 11.8 percent less. The sentence would keep
        paying the helper Rs 170 a day without asking whether the evening earns it. **The check:**
        name the unit the decision is priced in, here the hour, before reading any number. **The
        fix:** the evidence is sales per hour, Rs 1,190 to Rs 1,050, with sales per customer beside
        it.

        **Your turn.** A second example of the same shape, also invented: an auto driver earned Rs
        1,800 on Monday from 20 rides in 9 hours, and Rs 1,800 on Tuesday from 18 rides in 12
        hours. Read his two days per day, per ride and per hour, then say which denominator prices
        his question, "should I drive the longer day again?". Fill the blanks, type the lines into
        the empty cell below and run them; the checks print PASS when the reads are right.

        ```python
        auto = pd.DataFrame({"rs": [1800, 1800], "rides": [20, 18], "hours": [9, 12]},
                            index=["Monday", "Tuesday"])
        auto["per_ride"] = auto.rs / auto.___
        auto["per_hour"] = auto.rs / auto.___
        print(auto)
        check("per day is flat", auto.rs.nunique() == 1)
        check("per ride rose while per hour fell",
              auto.per_ride.is_monotonic_increasing and auto.per_hour.is_monotonic_decreasing)
        ```
        """),
        empty(),
        md("""
        ## Which rules does the chapter leave?

        1. The title is the claim: a sentence with a verb that says what is true and what to do.
        2. The evidence is one number with its denominator and window, or one chart, chosen by the
           decision it prices.
        3. The caveat sits beside the evidence, in plain sight.
        4. The action names what to do, its cost in rupees and weeks, and who signs.

        A slide has worked when the person who loses under it can repeat it accurately while
        disagreeing with it.

        **In the interview.** [S] Present a recommendation to a non-technical stakeholder in two
        minutes: open on the claim, then one number with its denominator.

        **Where it is used next.** Notebook 02 sorts what leaves Ramesh's slide. Chapter 4's
        notebook, `C2_W04_D02_04_case_one_slide_answer_three_denominators_STUDENT.ipynb`, runs the
        same three divisions on Uber's twelve driver-weeks and rebuilds the city head's slide in
        these four parts.
        """),
    ]


# ------------------------------------------------------------------ concept notebook 02
def nb02():
    return [
        md("""
        # What to leave out, and the appendix: where does the rest go?

        **Week 4, Tuesday, concept notebook 2 of 5, beside chapter 2 of the deck.** Ramesh's kirana
        shop returns from notebook 01 with the same invented numbers; only the question changes.
        Notebook 01 found that his decision is priced per hour: Rs 1,190 an hour in September and
        Rs 1,050 in October.

        **Who needs the answer.** Ramesh (invented), who reads the slide in five minutes, and two
        readers who each look for their own question behind it: his son and the shop's accountant.
        A slide that keeps everything buries the claim, and a slide that drops the caveat is called
        dishonest by the first reader who finds it missing.

        **The questions on the way.** How many of the draft's eight elements stay? Where does each
        of the rest go? Can the caveat leave when the slide is crowded? Does a chart obey the same
        rule?
        """),
        code(SETUP + '''
# Ramesh's first draft: eight elements, what each shows, and who would ask about it; all invented
elements = pd.read_csv("../data/C2_W04_D02_kirana_slide_elements_STUDENT.csv").fillna("")
check("eight elements on the first draft", len(elements) == 8)
check("exactly one element is the caveat", (elements.is_caveat == "yes").sum() == 1)
print(elements.to_string(index=False))
'''),
        md("""
        ## How many of the draft's eight elements stay?

        An **element** is anything on a slide a reader's eye can land on: a number, a chart, a line
        of text. The **appendix** is the set of pages behind the slide, shown only when someone
        asks. Sort by hand first, asking three questions of each element in turn: does the claim
        need it; if not, will a named person ask about it; and is it the caveat, which stays
        whatever else happens.

        **Predict before you run.** How many of the eight belong on the slide itself?

        a) 2, the two that carry the claim
        b) 3
        c) 5
        d) All 8
        """),
        code('''
def route(e):
    """The sort: the caveat and what the claim needs stay; a named reader's question gets a page; the rest leaves."""
    if e.is_caveat == "yes" or e.supports_claim == "yes":
        return "the slide"
    return f"{e.whose_question}'s page" if e.whose_question else "leaves"

elements["goes_to"] = elements.apply(route, axis=1)
print(elements[["element", "goes_to"]].to_string(index=False))
where = elements.goes_to.value_counts()
check("three stay on the slide", where["the slide"] == 3)
check("two go to the son's page and two to the accountant's page",
      where["the son's page"] == 2 and where["the accountant's page"] == 2)
check("one leaves", where["leaves"] == 1)

fig, ax = plt.subplots(figsize=(10, 3.0))
columns = ["the slide", "the son's page", "the accountant's page", "leaves"]
for i, col in enumerate(columns):
    ax.text(i, 0.97, col, ha="center", va="top", weight="bold", color="white",
            bbox=dict(boxstyle="round", fc=[INK, VIOLET, VIOLET, ROSE][i], ec="none"))
    for j, name in enumerate(elements[elements.goes_to == col].element):
        ax.text(i, 0.76 - j * 0.24, textwrap.fill(name, 22), ha="center", va="top", fontsize=9.5,
                bbox=dict(boxstyle="round", fc=PALE, ec=VIOLET))
ax.set_xlim(-0.6, 3.6)
ax.set_ylim(0.15, 1)
ax.axis("off")
ax.set_title("Where Ramesh's eight elements go (invented)", loc="left")
plt.show()
'''),
        md("""
        **What happened.** The answer is b. Two elements carry the claim, the per-hour chart and
        sales per customer, and the festival fortnight stays as the caveat. The son's page takes
        customers a day and his hours at the counter; the accountant's page takes the four weeks'
        totals and the helper's wage; rain days leave, because nobody will ask. Option a is the
        trap: the two that carry the claim are right, and the caveat is forgotten.

        ## Where does each of the rest go?

        Each appendix page is headed by its owner's question, so Ramesh can turn to it the moment
        the question comes, and every number on it answers that question and nothing else.
        """),
        code('''
questions = {"the son": "Did my extra hours at the counter bring customers?",
             "the accountant": "What did the longer hours cost, and what did they bring?"}
for owner, question in questions.items():
    print(f"Appendix page for {owner}: {question}")
    for _, e in elements[elements.whose_question == owner].iterrows():
        print(f"    {e.element}: {e.what_it_shows}")
off = elements[elements.goes_to != "the slide"]
check("an element off the slide leaves exactly when nobody will ask about it",
      ((off.goes_to == "leaves") == (off.whose_question == "")).all())
check("every page is headed by a question", all(q.endswith("?") for q in questions.values()))
'''),
        md("""
        ## Can the caveat leave when the slide is crowded?

        **The plausible wrong answer.** "The slide is crowded, so the festival fortnight goes to the
        appendix with the rain days; it is only a detail." A hurried sort that asks only the first
        two questions puts it there.

        **Predict before you run.** Where does the hurried sort send the festival fortnight?

        a) The slide
        b) The son's page
        c) The accountant's page
        d) Off the slide and out of every page
        """),
        code('''
def hurried_route(e):
    """The same sort with the caveat question skipped."""
    if e.supports_claim == "yes":
        return "the slide"
    return f"{e.whose_question}'s page" if e.whose_question else "leaves"

festival = elements[elements.element == "The festival fortnight"].iloc[0]
print("the hurried sort sends the festival fortnight to:", hurried_route(festival))
print("the rule keeps it on:", route(festival))
check("the hurried sort drops the caveat", hurried_route(festival) == "leaves")
check("the rule keeps the caveat on the slide", route(festival) == "the slide")
'''),
        md("""
        **Why it is wrong.** The answer is d, and the son will raise the festival first: when he
        finds it missing he calls the slide dishonest, after which Ramesh trusts nothing on it. **The check:** is the
        caveat on the slide itself? **The fix:** ask the caveat question first; when the slide is
        crowded, something else leaves instead.

        ## Does a chart obey the same rule?

        The same 56 days, drawn the way a dashboard sends them: six series in mixed units, a legend,
        a grid and a border. Then the makeover keeps only what the claim needs.

        **Predict before you run.** How many of the cluttered chart's six series carry the claim
        that each hour earns less?

        a) One
        b) Two
        c) Three
        d) All six
        """),
        code('''
days = pd.read_csv("../data/C2_W04_D02_kirana_days_STUDENT.csv")
days["x"] = range(1, len(days) + 1)
days["per_hour"] = days.sales_rs / days.hours_open
series = {"sales / 10": days.sales_rs / 10, "customers": days.customers, "hours x 100": days.hours_open * 100,
          "per hour": days.per_hour, "per customer x 10": days.sales_rs / days.customers * 10}
fig, ax = plt.subplots(figsize=(9, 4))
for label, values in series.items():
    ax.plot(days.x, values, marker="o", ms=3, label=label)
ax.bar(days.x, (days.rain_day == "yes") * 400, color="#BBBBBB", label="rain day")
ax.grid(True)
ax.spines[["top", "right"]].set_visible(True)
ax.legend(ncol=3, fontsize=9)
ax.set_title("Shop dashboard, September and October")
plt.show()

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(days.x, days.per_hour, color=VIOLET, lw=2.6)
ax.hlines(1190, 1, 28, color="gray", ls=":")
ax.hlines(1050, 29, 56, color="gray", ls=":")
ax.text(14.5, 1285, "September: Rs 1,190 an hour", ha="center")
ax.text(42.5, 1150, "October: Rs 1,050", ha="center")
ax.set_ylim(880, 1310)
ax.axvline(28.5, color=ROSE, ls="--")
ax.set_xticks([1, 15, 29, 43, 56], ["1 Sep", "15 Sep", "1 Oct", "15 Oct", "28 Oct"])
ax.set_ylabel("sales per hour, Rs")
ax.set_title("Each hour earns less since the shop opened longer (invented)", loc="left")
plt.show()
kept = ["per hour"]
check("one series of the six carries the claim", len(series) + 1 == 6 and len(kept) == 1)
'''),
        md("""
        **What happened.** The answer is a. Five of the six series leave, with the legend, the grid
        and the border; one line and two labels stay, and the title says the claim. The test is the
        one the elements met: does the claim need this ink? Storytelling with Data puts it as a
        question to ask of every element, "Is it adding any informative value?", and takes out
        whatever is not.

        **Your turn.** Ramesh's accountant presents the same eight elements to the bank, and her
        claim is different: the helper's two extra hours cost less than they bring. Mark which
        elements her claim needs, run the same sort, and check that the caveat still stays. Fill
        the blank, type the lines into the empty cell below and run them:

        ```python
        bank = elements.copy()
        bank["supports_claim"] = "no"
        needs = ["The helper's wage", ___]               # the element that shows what the hours brought
        bank.loc[bank.element.isin(needs), "supports_claim"] = "yes"
        bank["goes_to"] = bank.apply(route, axis=1)
        print(bank[["element", "goes_to"]].to_string(index=False))
        check("the festival fortnight stays on the slide whatever the claim",
              bank.set_index("element").goes_to["The festival fortnight"] == "the slide")
        check("the bank's slide keeps three elements", (bank.goes_to == "the slide").sum() == 3)
        ```
        """),
        empty(),
        md("""
        ## Which rules does the chapter leave?

        1. An element stays only if the claim cannot stand without it.
        2. An element a named person will ask about goes to that person's page, headed by their
           question.
        3. An element nobody will ask about leaves.
        4. The caveat stays on the slide, even when the slide is crowded.

        Named last: this is what to leave out, and the appendix. A chart obeys the same rule, one
        series at a time.

        **In the interview.** [F] What do you leave off the slide, and where does it go? Answer with
        the drawer: one page per question a named role will ask, the caveat kept in sight.

        **Where it is used next.** Chapter 4's notebook,
        `C2_W04_D02_04_case_one_slide_answer_three_denominators_STUDENT.ipynb`, cuts Uber's
        nine-number slide to its claim; chapter 5's notebook,
        `C2_W04_D02_05_case_defending_under_challenge_evidence_STUDENT.ipynb`, builds one appendix
        page for each of the three roles' questions.
        """),
    ]


# ------------------------------------------------------------------ concept notebook 03
def nb03():
    return [
        md("""
        # Defending under challenge: restate, answer, concede, what would change your mind: how do you hold a claim?

        **Week 4, Tuesday, concept notebook 3 of 5, beside chapter 3 of the deck.** Gulmohar
        Secondary School is invented, and so is every week of its attendance in this notebook,
        written by the day's seeded generator.

        **Who needs the answer.** A teacher at Gulmohar (invented) who claims at a staff meeting
        that the new timetable, from week 3, raised attendance, and the headmaster, who decides
        whether the timetable stays. The sports teacher objects: "Attendance rose because the exams
        began." A defence that concedes nothing loses the room, and one that concedes everything
        loses a term.

        **The questions on the way.** Which part of the objection is true? Which evidence answers
        the rest? What does the teacher's own overclaim get wrong? What does a full defence sound
        like?
        """),
        code(SETUP + '''
# Gulmohar's attendance, eight weeks of last year and eight of this year; every number invented
att = pd.read_csv("../data/C2_W04_D02_school_attendance_STUDENT.csv")
check("eight weeks in each year", (att.year.value_counts() == 8).all())
check("exams in weeks 6 to 8 of both years", set(att[att.exam_week == "yes"].week) == {6, 7, 8})
check("the new timetable runs from week 3, this year only",
      set(att[att.timetable_changed == "yes"].week) == set(range(3, 9))
      and set(att[att.timetable_changed == "yes"].year) == {"this year"})
print(att.to_string(index=False))
'''),
        md("""
        ## Which part of the objection is true?

        An **objection** is the reason a listener gives for not accepting a claim, usually built
        on a number the objector can see. To **concede** is to say its true part out loud. Count by
        hand first. Last year the exam weeks ran 85, 85 and 85, an average of 85.0, against 76, 77
        and 77 in weeks 3 to 5, an average of 76.7. This year they ran 89, 90 and 89, an average of
        89.3, against 81, 82 and 81, an average of 81.3.

        **Predict before you run.** In each year, how far do the exam weeks sit above the three
        weeks before them?

        a) About 2 points
        b) About 8 points
        c) About 13 points
        d) Only this year's exams lift attendance
        """),
        code('''
w = att.pivot(index="week", columns="year", values="attendance_pct")[["last year", "this year"]]
exam_lift = (w.loc[6:8].mean() - w.loc[3:5].mean()).round(1)      # each year's exams over weeks 3 to 5
print(exam_lift.rename("exam weeks over weeks 3 to 5, points").to_string())
check("by hand and by code: 8.3 points last year and 8.0 this year", list(exam_lift) == [8.3, 8.0])

fig, ax = plt.subplots(figsize=(9, 4.2))
for year, colour in (("last year", "gray"), ("this year", VIOLET)):
    ax.plot(w.index, w[year], color=colour, lw=2.6, marker="o", label=year)
ax.axvspan(5.5, 8.5, color="#FFF7E6", label="exam weeks, both years")
ax.axvline(2.5, color=ROSE, ls="--", label="new timetable, this year only")
ax.set_xlabel("week of the term")
ax.set_ylabel("attendance, percent")
ax.set_title("The rise began in week 3, before any exam (invented)", loc="left")
ax.legend(loc="lower right", fontsize=9)
plt.show()
'''),
        md("""
        **What happened.** The answer is b: 8.3 points last year and 8.0 this year. That is the true
        part of the objection, and it holds in both years: exam weeks run about 8 points above the
        weeks before them with or without the new timetable. The picture shows where the objection
        stops being true: the two lines agree in weeks 1 and 2 and part from week 3, before any
        exam.

        ## Which evidence answers the rest?

        Compare like with like: the same weeks of the term, this year against last year, so the
        exams and the season cancel out.

        **Predict before you run.** How far do weeks 3 to 5 this year sit above the same weeks last
        year?

        a) About the same
        b) About 4.7 points higher
        c) About 12.8 points higher
        d) Lower
        """),
        code('''
early = w.loc[3:5].mean()
rise = round(early["this year"] - early["last year"], 1)            # the timetable's weeks, before any exam
start = w.loc[1:2].mean()
gap = w["this year"] - w["last year"]                               # this year less last year, week by week
print(f"weeks 3 to 5: {early['this year']:.1f} this year against {early['last year']:.1f} last year, {rise} points apart")
print(f"weeks 1 and 2: {start['this year']:.1f} in both years")
check("weeks 1 and 2 match across the years", start["this year"] == start["last year"] == 76.5)
check("weeks 3 to 5 sit 4.7 points above last year's", rise == 4.7)

fig, ax = plt.subplots(figsize=(9, 3.6))
ax.bar(gap.index, gap, color=[LILAC if wk < 3 else VIOLET for wk in gap.index], edgecolor=VIOLET)
ax.axhline(0, color="gray")
ax.axvline(2.5, color=ROSE, ls="--")
ax.set_xlabel("week of the term")
ax.set_ylabel("this year less last year, points")
ax.set_title("This year runs ahead of last year from week 3 on (invented)", loc="left")
plt.show()
'''),
        md("""
        **What happened.** The answer is b. Weeks 3 to 5 this year average 81.3 against last year's
        76.7, 4.7 points apart, before any exam; weeks 1 and 2 sit at 76.5 in both years. The
        concession carries one number, about 8 points of exam lift in both years, and the answer
        carries another, 4.7 points before the exams.

        ## What does the teacher's own overclaim get wrong?

        **The plausible wrong answer.** "Attendance rose 12.8 points this term, from 76.5 to 89.3,
        so the timetable did it, and the exams are irrelevant." It concedes nothing, and every
        number in it is right.

        **Predict before you run.** Last year, with the old timetable, how far did the exam weeks
        rise above weeks 3 to 5?

        a) Not at all
        b) About 4 points
        c) About 8 points
        d) The full 12.8 points
        """),
        code('''
overclaim = round(w.loc[6:8, "this year"].mean() - start["this year"], 1)
print(f"the overclaim credits the timetable with {overclaim} points")
print(f"last year, with the old timetable, the exam weeks still rose {exam_lift['last year']} points")
check("the overclaim is 12.8 points", overclaim == 12.8)
check("most of it is the exams' lift, which last year shows without the timetable", exam_lift["last year"] > overclaim / 2)

fig, ax = plt.subplots(figsize=(8, 3.4))
labels = ["the overclaim", "the exams' lift,\\nboth years", "weeks 3 to 5 against\\nlast year's"]
bars = ax.bar(labels, [overclaim, exam_lift["this year"], rise], color=[ROSE, LILAC, VIOLET])
ax.bar_label(bars, fmt="%.1f")
ax.set_ylabel("points")
ax.set_title("Concede the exams' 8, keep the 4.7 (invented)", loc="left")
plt.show()
'''),
        md("""
        **Why it is wrong.** The answer is c, 8.3 points: the 12.8 points run from the first weeks to
        the exam weeks, so they carry the exams' lift, which last year shows without any new
        timetable. The sports teacher
        is partly right, and a reply that denies it hands the staff room to her. **The check:** did
        the reply name the true part and the line of evidence, in that order? **The fix:** concede
        the exams' 8 points and claim only what the like-for-like weeks show, 4.7.

        ## What does a full defence sound like?

        Named last, the four moves, in order. **Restate** the objection until its owner agrees with
        your version. **Answer** from a named line of the evidence. **Concede** the true part out
        loud. Say **what would change your mind**, so the claim can be tested. Restating comes
        first because the objector has to accept your version before any answer lands; Rapoport's
        rules, as the philosopher Daniel Dennett set them out, open the same way. The function
        builds the four moves from the two numbers the cells computed.
        """),
        code('''
def defend(restate, answer, concede, change_mind):
    """Defending under challenge: restate, answer, concede, what would change your mind."""
    moves = {"restate": restate, "answer": answer, "concede": concede, "change my mind": change_mind}
    for move, words in moves.items():
        print(f"{move:>15}: {words}")
    return moves

moves = defend(
    restate="You are saying attendance rose because the exams began, so the timetable may have done nothing.",
    answer=f"Weeks 3 to 5 this year sit {rise} points above the same weeks last year, before any exam.",
    concede=f"You are right that exam weeks run about {exam_lift.mean():.0f} points higher; they did in both years.",
    change_mind="If a school with the same exams and the old timetable showed the same rise in weeks 3 to 5, I would drop the claim.")
check("the answer names the line of evidence, 4.7 points", str(rise) in moves["answer"])
check("the concession names the true part, the exams", "exam" in moves["concede"])
'''),
        md("""
        **Your turn.** The headmaster pushes once more: "The rise is a three-week blip; it will
        fade." Find the evidence in the exam weeks: compare this year's exam weeks with last year's,
        then check that the gap holds about the size it had before the exams. Fill the blank, type
        the lines into the empty cell below and run them, then write the four moves for the new
        objection with `defend`:

        ```python
        exam_gap = w.loc[6:8, "this year"].mean() - w.loc[6:8, "last year"].___()
        print(round(exam_gap, 1))
        check("the gap holds through the exam weeks", abs(exam_gap - rise) < 1)
        ```
        """),
        empty(),
        md("""
        ## Which rules does the chapter leave?

        1. Restate the objection until its owner agrees with your version.
        2. Answer from a named line of the evidence, never from the claim repeated.
        3. Concede the true part out loud; the claim survives it.
        4. Say the fact that would change your mind, so the claim can be tested.

        These are the four moves of defending under challenge: restate, answer, concede, what would
        change your mind. A defence fails two ways: overclaiming concedes nothing, and retreating
        concedes everything.

        **In the interview.** [F] A stakeholder's objection is partly right; how do you answer it?

        **Where it is used next.** Chapter 5's notebook,
        `C2_W04_D02_05_case_defending_under_challenge_evidence_STUDENT.ipynb`, finds the true part
        of each of Uber's three objections in the case's own tables and answers the rest with a
        line of evidence.
        """),
    ]


# ------------------------------------------------------------------ case notebook 04
def nb04():
    return [
        md(f"""
        # Uber's slide, rebuilt with the one-slide answer and what to leave out: which number carries it?

        **Week 4, Tuesday, chapter 4, the case's first chapter.** It applies two of the morning's
        topics: the one-slide answer: claim, evidence, caveat, action (concept notebook 01), and
        what to leave out, and the appendix (concept notebook 02). On Ramesh's kirana shop
        (invented) those notebooks found that the same rupees rose 5.9 percent per day and fell
        11.8 percent per hour, that the decision's own unit picks the denominator, and that three of
        the draft's eight elements stay on the slide, the caveat among them. This notebook does the
        same to Uber's numbers.

        **The ticket.** Uber, Hyderabad, the driver app's peak-hour earnings guarantee, one day on.
        The city head takes the redesign to the Thursday city review on one slide, in five minutes,
        with the driver-operations lead, the marketing lead and the finance partner in the room.
        The number the slide must explain first: gross bookings (what riders paid) per peak online
        hour fell from Rs 314 in the six weeks before the launch (31 August 2026) to Rs 260 in the
        six weeks after, while the average peak fare stayed at Rs 165.

        {LABEL}

        **What Monday found.** Peak online hours rose 24 percent while completed peak trips rose 3
        percent, so trips per peak online hour fell from 1.90 to 1.58, and 61 percent of the Rs 1.9
        crore top-up (the gap Uber pays up to the Rs 300 hourly floor) went to driver-weeks that
        accepted fewer than half the requests offered to them.

        **Who needs the answer.** The city head, whose one slide decides whether the scheme is
        kept, ended or changed; a slide that quotes the wrong denominator hands each of the three
        roles a number to argue with, and the city keeps paying for idle hours.

        **The metric at stake.** Gross bookings per peak online hour, Rs 314 to Rs 260.

        **The questions on the way.**

        1. What do the twelve rows say when the same rupees are read three ways?
        2. Which number could carry the slide, and what does each say over all the driver-weeks?
        3. Why does the per-driver-week read rise while the per-hour read falls?
        4. Is the fall in rupees per hour all trips, or some of it fare?
        5. What does the twelve-week chart look like before and after the makeover?
        """),
        code(SETUP + '''
rows = pd.read_csv("../data/C2_W04_D02_twelve_rows_STUDENT.csv")    # six drivers, two weeks
weeks = pd.read_csv("../data/C2_W04_D02_twelve_weeks_STUDENT.csv")  # the city, week by week
print(len(rows), "driver-weeks in the twelve rows;", len(weeks), "weeks in the city table")
check("twelve driver-weeks and twelve city weeks", len(rows) == 12 and len(weeks) == 12)
'''),
        md("""
        ## What do the twelve rows say when the same rupees are read three ways?

        Each row is one driver in one week (the week of 10 August before the launch, the week of 21
        September after it): peak online hours, peak trips and the gross bookings those trips
        brought in. Gross bookings are what riders paid for the trips, before Uber's share and
        before any top-up. The same rupees can be divided by three things: the hours online, the
        driver-weeks, or the trips. The cell sums each column per window and divides three times,
        exactly as the board did, then reads each driver's rupees per hour.

        **Predict before you run.** The board found Rs 313.5 an hour before and Rs 196.2 after.
        Which drivers explain most of that fall?

        a) A and B, the two in the busiest central zones
        b) C and D, the two who drove the most hours before
        c) E and F, Monday's two idle-tail drivers
        d) All six about equally
        """),
        code('''
# Sum the twelve rows by window, then divide the same rupees by hours, driver-weeks and trips.
t = rows.groupby("window")[["peak_online_hours", "peak_trips", "peak_bookings_rs"]].sum()
t["driver_weeks"] = rows.groupby("window").size()
t["rs_per_hour"] = (t.peak_bookings_rs / t.peak_online_hours).round(1)
t["rs_per_driver_week"] = t.peak_bookings_rs / t.driver_weeks
t["rs_per_trip"] = t.peak_bookings_rs / t.peak_trips
t = t.loc[["before", "after"]]
print(t[["peak_online_hours", "peak_trips", "peak_bookings_rs", "rs_per_hour", "rs_per_driver_week", "rs_per_trip"]])
per_driver = (rows.assign(rs_per_hour=(rows.peak_bookings_rs / rows.peak_online_hours).round(1))
              .pivot(index="driver", columns="window", values="rs_per_hour")[["before", "after"]])
print(per_driver)                                            # rupees per peak online hour, driver by driver
check("hand count: Rs 313.5 and Rs 196.2 per hour", list(t.rs_per_hour) == [313.5, 196.2])
check("hand count: Rs 3,135 and Rs 2,420 per driver-week", list(t.rs_per_driver_week) == [3135, 2420])
check("E and F fall furthest", set(per_driver.after.nsmallest(2).index) == {"E", "F"})
'''),
        md("""
        **What happened.** The answer is c. E and F fell from Rs 297.0 and Rs 280.5 an hour to Rs
        30.9 and Rs 23.6, while A to D stayed near Rs 300 to Rs 330. Per peak online hour the six
        drivers fell from Rs 313.5 to Rs 196.2, down 37 percent; per driver-week from Rs 3,135 to
        Rs 2,420, down 23 percent; per trip they held at Rs 165, because each trip pays its fare
        whatever else happens. Ramesh's shop showed the same thing in notebook 01: three honest
        divisions of the same rupees gave three sizes of change, so a slide that says "bookings
        fell" without its denominator has said nothing a role cannot argue with.

        ## Which number could carry the slide, and what does each say over all the driver-weeks?

        The city table holds every week's totals. Four numbers could head the slide, and each role
        has its favourite:

        | Option | What it divides by | Who reaches for it |
        |---|---|---|
        | Gross peak bookings | nothing: the six weeks' sum | marketing, as "bookings are up" |
        | Bookings per peak online hour | the hours the scheme pays for | the analyst |
        | Bookings per active driver-week | one enrolled driver with a row that week | driver operations |
        | Bookings per completed trip | the trips | finance |

        An active driver-week is one enrolled driver with a row in Monday's `driver_weeks` table
        that week; a driver with no row that week is not counted. The cell sizes all four on the
        city's twelve weeks and draws each one's change.

        **Predict before you run.** Rupees per driver-week is rupees per hour times hours per
        driver-week. About how many more peak online hours did an average active driver-week carry
        after the launch?

        a) About 1 more
        b) About 4 more
        c) About 10 more
        d) Fewer than before
        """),
        code('''
# The four candidate numbers on every driver-week in the city, with hours per driver-week beside them.
w = weeks.groupby("window")[["peak_online_hours", "peak_trips", "peak_bookings_rs", "active_driver_weeks"]].sum()
w = w.loc[["before", "after"]]
w["rs_per_hour"] = w.peak_bookings_rs / w.peak_online_hours
w["rs_per_driver_week"] = w.peak_bookings_rs / w.active_driver_weeks
w["rs_per_trip"] = w.peak_bookings_rs / w.peak_trips
w["hours_per_driver_week"] = w.peak_online_hours / w.active_driver_weeks
change = (w.loc["after"] / w.loc["before"] - 1) * 100
print(w[["rs_per_hour", "rs_per_driver_week", "rs_per_trip", "hours_per_driver_week"]].round(1))
print((change[["peak_bookings_rs", "rs_per_hour", "rs_per_driver_week", "hours_per_driver_week"]]).round(1).rename("change, percent"))
check("per hour down 16.9 percent, printed as 17", round(change.rs_per_hour, 1) == -16.9)
check("per active driver-week up 0.8 percent", round(change.rs_per_driver_week, 1) == 0.8)
check("rupees per driver-week is rupees per hour x hours per driver-week",
      ((w.rs_per_hour * w.hours_per_driver_week - w.rs_per_driver_week).abs() < 1e-6).all())

options = {"gross bookings": change.peak_bookings_rs, "per online hour": change.rs_per_hour,
           "per driver-week": change.rs_per_driver_week, "per trip": change.rs_per_trip}
fig, ax = plt.subplots(figsize=(8, 3.6))
bars = ax.bar(list(options), list(options.values()),
              color=[LILAC, ROSE, LILAC, LILAC], edgecolor=VIOLET)
ax.bar_label(bars, fmt="%+.1f")
ax.axhline(0, color="gray")
ax.set_ylim(-21, 6)
ax.set_ylabel("after on before, percent")
ax.set_title("Four candidate numbers, four verdicts on the same six weeks", loc="left")
plt.show()
'''),
        md("""
        **What happened.** The answer is b: 18.6 hours a driver-week before the launch and 22.5
        after, up 21 percent. Per peak online hour the rupees fell from Rs 313.5 to Rs 260.4, down
        17 percent, and per active driver-week they rose from Rs 5,817 to Rs 5,861, up 0.8 percent,
        because each driver-week carried about four more hours at 17 percent less per hour. Gross
        bookings rose 3.0 percent and per trip held at Rs 165.

        **The call.** The slide carries bookings per peak online hour, because the scheme pays by
        the online hour; the other three go behind it, one per role's question, as notebook 02's
        sort sends them. The fact that would change the call: if the scheme paid per completed
        trip, per trip would be the number the decision is priced in.

        **The plausible wrong answer.** "Bookings per driver-week rose from Rs 5,817 to Rs 5,861, so
        the guarantee is working; keep it as it is." That sentence is true to the rupee and would
        keep the city paying for idle hours.

        **Why it is wrong.** The rise was bought with hours, the very thing the scheme pays for.
        Bookings rose 3.0 percent and active driver-weeks 2.2 percent (6,360 to 6,500), so the ratio
        rose 0.8 percent. The next cell splits the drivers into those there before the launch and
        the 140 who joined after it, to see which group moved the read.

        ## Is the fall in rupees per hour all trips, or some of it fare?

        A second route to the same number: rupees per hour is also the average fare times the trips
        each online hour carried. The two routes always agree, since the second splits the first in
        two; what the split shows is which half moved.
        """),
        code('''
# Split the city by when drivers joined, then rebuild rupees per hour as fare x trips per hour.
groups = pd.read_csv("../data/C2_W04_D02_driver_groups_STUDENT.csv")  # Monday's rows, split by joined_month
groups["rs_per_driver_week"] = (groups.peak_bookings_rs / groups.driver_weeks).round(0).astype(int)
groups["hours_per_driver_week"] = (groups.peak_online_hours / groups.driver_weeks).round(1)
print(groups[["window", "group", "driver_weeks", "rs_per_driver_week", "hours_per_driver_week"]])
joiner = groups[groups.group == "the 140 joiners"].iloc[0]
check("the joiners sit below the after average, so they pull the read down",
      joiner.rs_per_driver_week < w.loc["after", "rs_per_driver_week"])
fare = w.peak_bookings_rs / w.peak_trips
trips_per_hour = w.peak_trips / w.peak_online_hours
second_route = fare * trips_per_hour
print(pd.DataFrame({"fare": fare, "trips_per_hour": trips_per_hour.round(3),
                    "fare_x_trips_per_hour": second_route.round(1)}))
check("second route agrees with bookings / hours in both windows",
      ((second_route - w.rs_per_hour).abs() < 1e-9).all())
'''),
        md("""
        **What happened.** The drivers who were there before the launch rose from Rs 5,817 to Rs
        5,895 a driver-week, up 1.4 percent, on 22.6 hours a week against 18.6. The 140 joiners
        drove about one week each at Rs 4,314, below the average, so they pulled the read down to
        0.8 percent. The fare held at Rs 165 in both windows, and trips per hour fell from 1.900 to
        1.578 (printed elsewhere as 1.58): Rs 165 x 1.578 is Rs 260.4, so the whole fall in rupees
        per hour is the fall in trips per hour Monday found. That is the evidence line the slide
        stands on when the finance partner asks whether riders paid less.

        ## What does the twelve-week chart look like before and after the makeover?

        The cluttered version is the one dashboards send: four series in four units on one axis, two
        of them divided by 20 or 100 to fit, a legend away from the lines, gridlines, and a title
        that names a topic. The clear version keeps one series, bookings per peak online hour,
        because the scheme pays by the online hour; it draws the launch, labels the two windows'
        values on the lines, and makes the title a sentence, the claim of notebook 01's first part.
        """),
        code('''
# Draw the series cluttered, then the makeover: one series, the launch, two labels, a sentence title.
x = range(len(weeks))
labels = pd.to_datetime(weeks.week_start).dt.strftime("%d %b")

fig, ax = plt.subplots(figsize=(9, 4.5))                      # before: everything at once
ax.plot(x, weeks.rs_per_hour, marker="o", label="Rs per online hour")
ax.plot(x, weeks.rs_per_driver_week / 20, marker="s", label="Rs per driver-week / 20")
ax.plot(x, weeks.rs_per_trip, marker="^", label="Rs per trip")
ax.plot(x, weeks.peak_online_hours / 100, marker="x", label="online hours / 100")
ax.grid(True); ax.legend(loc="lower left", ncol=2)
ax.set_xticks(list(x), labels, rotation=45); ax.set_title("Peak metrics, weeks of 20 Jul to 5 Oct")
plt.show()

before, after = w.rs_per_hour
fig, ax = plt.subplots(figsize=(9, 4.5))                      # after: one claim, one series
ax.plot(x, weeks.rs_per_hour, color=VIOLET, lw=3, marker="o")
ax.hlines(before, -0.3, 5.3, color="gray", ls=":"); ax.hlines(after, 5.7, 11.3, color="gray", ls=":")
ax.text(2.5, before + 5, f"six weeks before: Rs {before:.0f}", ha="center")
ax.text(8.5, after - 12, f"six weeks after: Rs {after:.0f}", ha="center")
ax.axvline(5.5, color=ROSE, ls="--")
ax.text(5.6, 330, "launch: the week of 31 Aug is after", color=ROSE)
ax.set_ylim(220, 340); ax.set_xticks(list(x)[::2], labels[::2])
ax.set_title("The scheme is paying for online hours that carry no trips", loc="left")
ax.set_ylabel("gross bookings per peak online hour, Rs")
plt.show()
step = weeks[weeks.window == "after"].rs_per_hour.max() < weeks[weeks.window == "before"].rs_per_hour.min()
check("every after week sits below every before week: a step at the launch, not a slow drift", step)
'''),
        md("""
        **What happened.** On the clear chart the eye finds the claim in a second: about Rs 314 an
        hour before, about Rs 260 after, and the drop lands in the launch week, with the highest
        after week (Rs 271) below the lowest before week (Rs 310). A season that ended slowly would
        drift; this steps. That helps with the finance partner's monsoon objection without settling
        it, since last year's weeks are not in the data, and chapter 5's notebook takes the
        objection up.

        **The answers, one line each.**

        1. On the twelve rows the same rupees fell 37 percent per hour, 23 percent per driver-week
           and 0 per trip, and E and F explain most of the fall.
        2. Over all driver-weeks, gross bookings rose 3.0 percent, per hour fell 17 percent, per
           active driver-week rose 0.8 percent and per trip held; the slide carries per hour.
        3. Each driver-week carried about four more hours, and the 140 joiners pulled the read
           down.
        4. The fall is all trips: Rs 165 x 1.90 is Rs 313.5, and Rs 165 x 1.578 is Rs 260.4.
        5. The clear chart carries one series, a launch line and a sentence for a title; the drop
           is a step at the launch.

        ### What will an interviewer ask about this, and what does a strong answer do?

        **[S] Present this recommendation to a non-technical leader in two minutes.** Name the
        decision, open on the claim ("the scheme is paying for online hours that carry no trips"),
        give one number with its denominator (Rs 314 to Rs 260 per peak online hour), say what
        riders got (a median wait of 4.8 to 4.6 minutes), say the caveat (the monsoon ended inside
        the six weeks), and end on the action with its cost and signer (test paying per completed
        peak trip with an acceptance floor; city-wide it saves Rs 58 lakh to Rs 92.7 lakh over six
        weeks if a half to a fifth of the idle drivers' top-up is still paid; the city head signs
        the test).

        **The AI-company variant.** A coding assistant's dashboard reports suggestions accepted per
        developer-week. The same trap waits: accepted text can be deleted soon after. A read that
        matches what the product promises is suggested code still in the file seven days after
        acceptance, per developer who saw a suggestion, with ratio guardrails against padding and
        acceptance kept as a leading input.
        """),
    ]


# ------------------------------------------------------------------ case notebook 05
def nb05():
    return [
        md(f"""
        # Uber's three objections, answered by defending under challenge and the appendix: which objection holds?

        **Week 4, Tuesday, chapter 5, the case's second chapter.** It applies defending under
        challenge: restate, answer, concede, what would change your mind (concept notebook 03), and
        what to leave out, and the appendix (concept notebook 02). At Gulmohar Secondary School
        (invented), notebook 03 conceded the exams' 8 points and answered with the 4.7 points weeks
        3 to 5 gained before any exam. Notebook 04 left the city head's slide on one number: gross
        bookings per peak online hour fell from Rs 314 to Rs 260 because trips per online hour fell
        from 1.90 to 1.58, with the fare flat at Rs 165. This notebook finds the true part of each
        role's objection in the case's own tables and answers the rest.

        **The ticket.** Uber, Hyderabad, the driver app's peak-hour earnings guarantee: an enrolled
        driver online through a peak window is guaranteed Rs 300 per peak online hour, and Uber
        pays the gap as a top-up. Monday's redesign pays per completed peak trip, with a floor kept
        for drivers who accept most offers. Three roles object at Thursday's review. Driver
        operations: "Drivers will log off and supply at peak will fall." Marketing: "The guarantee is
        on every hoarding; changing it six weeks in looks like bait." Finance: "The fall in bookings
        per hour is the monsoon ending."

        {LABEL}

        **Who needs the answer.** The analyst whose slide must survive three roles who each lose
        something under it, and the city head, who sides with nobody until the evidence is on the
        table. A defence that overclaims turns a partly right objector against the test; one that
        retreats keeps paying for idle hours.

        **The metric at stake.** Trips per peak online hour, 1.90 before the launch and 1.58 after,
        the line the slide's evidence stands on.

        **The questions on the way.**

        1. Which drivers' trips per hour fell?
        2. Are the 140 drivers who joined after the hoarding in the idle tail?
        3. Did demand fall away with the monsoon?
        4. What does a full defence of the monsoon objection sound like?
        5. What goes behind the slide, page by page?
        """),
        code(SETUP + '''
segments = pd.read_csv("../data/C2_W04_D02_driver_segments_STUDENT.csv")   # Monday's drivers in three groups
weeks = pd.read_csv("../data/C2_W04_D02_twelve_weeks_STUDENT.csv")         # the city, week by week
print(segments.to_string(index=False))
city = weeks.groupby("window")[["peak_online_hours", "peak_trips"]].sum()
seg = segments.groupby("window")[["peak_online_hours", "peak_trips"]].sum()
check("the three groups add up to the city's hours and trips in both windows", seg.equals(city.loc[seg.index]))
check("1,060 drivers before the launch and 1,200 after",
      segments.groupby("window").drivers.sum().to_dict() == {"after": 1200, "before": 1060})
'''),
        md("""
        ## Which drivers' trips per hour fell?

        Driver operations' objection first. The **idle tail** is Monday's name for the 180 drivers
        whose trips per online hour fell under 1.0 after the launch; the other 880 drivers were
        there before the launch too; the 140 joiners arrived after it.

        **Predict before you run.** Which group's trips per online hour fell?

        a) All three
        b) The idle tail only
        c) The 140 joiners only
        d) The other 880 drivers
        """),
        code('''
segments["trips_per_hour"] = (segments.peak_trips / segments.peak_online_hours).round(2)
tph = segments.pivot(index="segment", columns="window", values="trips_per_hour")[["before", "after"]]
print(tph.to_string())
tail_hours = segments[(segments.segment == "the idle tail") & (segments.window == "after")].peak_online_hours.iloc[0]
tail_share = tail_hours / city.loc["after", "peak_online_hours"]
print(f"the idle tail's share of peak online hours after the launch: {tail_share:.0%}")
check("the idle tail fell from 1.90 to under 1.0", tph.loc["the idle tail"].tolist() == [1.90, 0.80])
check("the other 880 held at 1.90", tph.loc["the other drivers there before the launch"].tolist() == [1.90, 1.90])

fig, ax = plt.subplots(figsize=(9, 3.8))
order = ["the idle tail", "the other drivers there before the launch", "the 140 joiners"]
short = ["the idle tail, 180", "the other 880", "the 140 joiners"]
for k, window in enumerate(["before", "after"]):
    vals = [tph.loc[s, window] for s in order]
    ax.bar([i + (k - 0.5) * 0.38 for i in range(3)], vals, width=0.38,
           color=LILAC if window == "before" else VIOLET, label=window)
ax.axhline(1.0, color=ROSE, ls="--")
ax.text(2.45, 1.04, "the idle tail's line, 1.0", color=ROSE, ha="right")
ax.set_xticks(range(3), short)
ax.set_ylabel("trips per peak online hour")
ax.set_title("Only the idle tail's trips per hour fell", loc="left")
ax.legend()
plt.show()
'''),
        md("""
        **What happened.** The answer is b. The idle tail fell from 1.90 trips per online hour to
        0.80 on 42,000 hours, 29 percent of all peak online hours after the launch, while the other
        880 held at 1.90 and the joiners ran at 1.59. Driver operations' true part: the 180 will
        log off, since their idle hours are exactly what stops being paid. The rest is answered by
        the 880, who kept their trips per hour and keep the floor if they accept.

        ## Are the 140 drivers who joined after the hoarding in the idle tail?

        Marketing's objection: the hoarding promised a floor, and 140 drivers joined after it went
        up. If the joiners were the idle tail, the redesign would punish exactly the drivers the
        hoarding recruited.

        **Predict before you run.** How many of the 140 joiners sit in the idle tail?

        a) All 140
        b) About half
        c) None
        d) The tables cannot say
        """),
        code('''
joiners = segments[segments.segment == "the 140 joiners"].iloc[0]
tail = segments[(segments.segment == "the idle tail") & (segments.window == "before")].iloc[0]
print(f"the joiners ran {joiners.trips_per_hour} trips per online hour, against the idle tail's line of 1.0")
print(f"the idle tail is {tail.drivers} drivers who were there before the launch")
check("the joiners sit above the idle tail's line", joiners.trips_per_hour > 1.0)
check("the idle tail was drawn from the drivers there before the launch",
      tail.drivers + 880 == segments[segments.window == "before"].drivers.sum())
'''),
        md("""
        **What happened.** The answer is c. The idle tail is 180 of the 1,060 drivers who were
        there before the launch, so no joiner is in it, and the joiners ran 1.59 trips per online
        hour, well above the tail's line of 1.0. Marketing's true part stands: the hoarding
        promised a floor, and changing it needs words drivers will accept. The rest is answered:
        the floor stays for drivers who accept, and the joiners are not the drivers it stops
        paying.

        ## Did demand fall away with the monsoon?

        Finance's objection is the hardest, because part of it cannot be answered from these
        tables: the monsoon ended inside the six weeks, and last year's weeks are not in the data.

        **Predict before you run.** Over the six weeks after the launch, rider requests rose 1.8
        percent on the six before. Does that settle finance's objection?

        a) Yes: demand held, so the monsoon explains nothing
        b) No: read the weeks one by one before using a six-week total
        c) Yes: trips rose 3 percent as well
        d) No: requests can never check anything about trips
        """),
        code('''
import matplotlib.dates as mdates
w = weeks.set_index(pd.to_datetime(weeks.week_start))
before, after = w[w.window == "before"], w[w.window == "after"]
rise = after.rider_requests.sum() / before.rider_requests.sum() - 1
falls = (after.rider_requests.diff() < 0).iloc[2:].sum()             # week on week, from 7 September on
last3 = after.iloc[-3:]
last3_tph = last3.peak_trips.sum() / last3.peak_online_hours.sum()
print(f"six weeks on six weeks: requests {rise:+.1%}")
print(f"the last three weeks: requests {last3.rider_requests.min():,} to {last3.rider_requests.max():,}, "
      f"against {before.rider_requests.min():,} to {before.rider_requests.max():,} before the launch")
print(f"the last three weeks: {last3_tph:.2f} trips per online hour, against 1.90 before")
check("requests fell four weeks running from 7 September", falls == 4)
check("the last three weeks' requests sit inside the before window's range",
      last3.rider_requests.between(before.rider_requests.min(), before.rider_requests.max()).all())
check("trips per online hour stayed low in the last three weeks", round(last3_tph, 2) == 1.56)

fig, ax = plt.subplots(figsize=(9, 3.6))
ax.axhspan(before.rider_requests.min(), before.rider_requests.max(), color=PALE, label="the before window's range")
ax.plot(w.index, w.rider_requests, color=VIOLET, marker="o")
ax.axvline(pd.Timestamp("2026-08-28"), color=ROSE, ls="--")
ax.set_ylabel("rider requests in the week")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
ax.set_title("Requests rose, then fell back to the before level", loc="left")
ax.legend(loc="upper left")
plt.show()

fig, ax = plt.subplots(figsize=(9, 3.6))
ax.plot(w.index, w.peak_trips / w.peak_online_hours, color=VIOLET, marker="o")
ax.axvline(pd.Timestamp("2026-08-28"), color=ROSE, ls="--")
ax.axhline(1.90, color="gray", ls=":")
ax.set_ylabel("trips per peak online hour")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
ax.set_title("Trips per online hour stayed low after requests came back", loc="left")
plt.show()
'''),
        md("""
        **What happened.** The answer is b. Requests rose in the launch weeks and then fell four
        weeks running from 7 September, so the six-week rise of 1.8 percent hides a decline. In
        the last three weeks requests were back inside the before window's range, 41,161 to 42,602
        against 41,155 to 42,719, and trips per online hour still ran at 1.56: with demand at its
        old level, each online hour carried fewer trips than before.

        **The plausible wrong answer.** "Requests rose 1.8 percent over the six weeks, so demand
        held and the monsoon explains nothing." **Why it is wrong.** It concedes nothing, and the
        finance partner, who can see the weekly decline, turns the room against the test. **The
        check:** read the weeks one by one before quoting a total. **The fix:** concede the decline
        and the missing year, and answer with the last three weeks.

        ## What does a full defence of the monsoon objection sound like?

        Notebook 03's four moves, restated here so this notebook stands alone: restate, answer,
        concede, what would change your mind. The answer names a line of evidence the cells
        computed.
        """),
        code('''
def defend(restate, answer, concede, change_mind):
    """Defending under challenge: restate, answer, concede, what would change your mind."""
    moves = {"restate": restate, "answer": answer, "concede": concede, "change my mind": change_mind}
    for move, words in moves.items():
        print(f"{move:>15}: {textwrap.fill(words, 110, subsequent_indent=' ' * 17)}")
    return moves

moves = defend(
    restate="You are saying the fall in bookings per hour could be the season ending, so the scheme has not had a fair test.",
    answer=(f"In the last three weeks requests were back at the before window's level and trips per online hour still "
            f"ran at {last3_tph:.2f}; the 880 drivers there before the launch held at 1.90, so the fall sits in the idle tail."),
    concede="You are right that the monsoon ended inside the six weeks, and that last year's weeks are not in the data.",
    change_mind=("Last year's same six weeks showing a fall of this size, or the test of the redesign showing no change "
                 "in trips per online hour."))
check("the answer names a line of evidence", "1.56" in moves["answer"])
check("the concession says the true part", "monsoon" in moves["concede"])
'''),
        md("""
        ## What goes behind the slide, page by page?

        Notebook 02's sort, applied: the slide keeps its claim, its evidence, its caveat and its
        action, and each role's question gets one appendix page headed by that question. The
        monsoon stays on the slide as the caveat; a caveat found in the drawer makes its owner call
        the slide dishonest.
        """),
        code('''
slide_caveat = "The monsoon ended inside the six weeks, so part of the fall may be the season."
drawer = {
    "Driver operations asks: what happens to the drivers who accept?":
        f"The 880 there before the launch ran {tph.loc['the other drivers there before the launch', 'after']:.2f} trips per online hour after it.",
    "Marketing asks: do the 140 new drivers lose out?":
        f"No joiner is in the idle tail; the joiners ran {joiners.trips_per_hour} trips per online hour.",
    "Finance asks: how much of the fall is the season?":
        f"In the last three weeks requests were back at the before level and trips per hour ran at {last3_tph:.2f}.",
}
print("On the slide, the caveat:", slide_caveat)
for heading, line in drawer.items():
    print(f"Appendix page. {heading}\\n    {line}")
check("the caveat sits on the slide, never only in the drawer", "monsoon" in slide_caveat)
check("one page per role, each headed by its question", len(drawer) == 3 and all("?" in h for h in drawer))
'''),
        md("""
        ## Does a second route reach the 880's 1.90?

        The segments table gives the 880's trips per hour directly. The city's totals less the idle
        tail and the joiners give it a second way, which is what a finance partner would do with
        Monday's dashboard alone.
        """),
        code('''
after_city = city.loc["after"]
rest = segments[(segments.window == "after") & (segments.segment != "the other drivers there before the launch")]
hours_880 = after_city.peak_online_hours - rest.peak_online_hours.sum()
trips_880 = after_city.peak_trips - rest.peak_trips.sum()
print(f"city less the tail and the joiners: {trips_880:,} trips over {hours_880:,} hours, {trips_880 / hours_880:.2f} an hour")
check("the second route agrees with the segments table", round(trips_880 / hours_880, 2) == 1.90)
'''),
        md("""
        **The answers, one line each.**

        1. Only the idle tail's trips per hour fell, 1.90 to 0.80; the other 880 held at 1.90.
        2. None of the 140 joiners is in the idle tail; they ran 1.59 trips per online hour.
        3. Requests fell four weeks running from 7 September, then sat at the before level while
           trips per online hour stayed at 1.56; the missing year is conceded.
        4. Restate, answer from the last three weeks and the 880, concede the monsoon and the
           missing year, and name last year's weeks as the fact that would change your mind.
        5. Three appendix pages, each headed by a role's question; the monsoon stays on the slide.

        ### What will an interviewer ask about this, and what does a strong answer do?

        **[F] A stakeholder's objection is partly right; how do you answer it?** Say its true part
        first, out loud, then answer the rest from one named line of evidence, and end on the fact
        that would change your mind, so the room hears a claim that can be tested.

        **[D] What do you do when the person who loses under your claim runs the meeting?** Concede
        the true part before the meeting, keep their visible number on the page, and agree the test
        and the result that decides it in advance.

        **The AI-company variant.** A head of product objects to replacing acceptance rate in the
        sales deck: "acceptance is what customers see." The true part: customers do quote it, and
        it moves first. The answer, on invented numbers: of suggestions shown, 32 percent are
        accepted, and about 26 percent are still in the file seven days later. The defence keeps
        acceptance as a leading input and puts surviving code on the slide, with the fact that
        would change the call: a holdout showing acceptance tracks seat renewals as well as
        surviving code does.
        """),
    ]


# ------------------------------------------------------------------ concept notebook 06
def nb06():
    return [
        md("""
        # The guesstimate: clarify, map, calculate, validate: how big is an unknown?

        **Week 4, Tuesday, concept notebook 4 of 5, beside chapter 6 of the deck.** The campus
        canteen, its till, the town, the phone pack and Gulmohar Secondary School's exam are
        invented, and every number about them in this notebook was written by the day's seeded
        generator.

        **Who needs the answer.** The canteen head (invented), who must order milk for a weekday
        before any till report exists, and any interviewer who asks for a number aloud. A guess
        nobody can check orders too much milk or too little, and an interviewer scores the thinking
        before the number.

        **The questions on the way.** Who scores higher, the chain or the near guess? What exactly
        is counted, and which factors multiply into it? Which guess sets the range? Is the answer
        sane against the till? What does a sanity check catch that careful arithmetic misses?
        """),
        code(SETUP + '''
# The canteen's three guesses, its till for one week, and three checks gone wrong; all invented
ledger = pd.read_csv("../data/C2_W04_D02_canteen_ledger_STUDENT.csv").set_index("factor")
till = pd.read_csv("../data/C2_W04_D02_canteen_till_STUDENT.csv")
tests = pd.read_csv("../data/C2_W04_D02_sanity_tests_STUDENT.csv")
check("three factors in the ledger, each with a low and a high", len(ledger) == 3 and (ledger.low < ledger.high).all())
check("five weekdays on the till", len(till) == 5)
print(ledger.to_string())
print(till.to_string(index=False))
print(tests.to_string(index=False))
'''),
        md("""
        ## Who scores higher, the chain or the near guess?

        A **guesstimate** is a rough count of something nobody has measured; an **assumption** is a
        guess said aloud with its range; the **range** is the lowest and highest answer you would
        still defend. Write your own number for the cups of tea the canteen sells on a weekday
        before you read on. Then two candidates answer.

        **Candidate A:** "Students on campus times the share who buy tea times cups each: 3,000 x
        0.45 x 2 = 2,700 cups. Checked against the till it runs high, so the share is the guess I
        would replace with a count first."

        **Candidate B:** "About 2,350 cups."

        **Predict before you run.** The till's five weekdays average 2,340 cups. Who scores higher?

        a) B, because 2,350 sits ten cups from the till
        b) A, because the chain and the check show how the number was built
        c) They score the same, because both landed near the till
        d) Neither, because a number with no data cannot be marked
        """),
        code('''
# Clarify: one canteen, one weekday, cups of tea. Map: students x share who buy x cups each.
running = ledger.central.cumprod()                      # the running product, said aloud
print(running.round(0).astype(int).to_string())
cups = ledger.central.prod()
by_hand = 3000 * 0.45 * 2
gap_a = cups / till.cups_sold.mean() - 1
print(f"candidate A: {cups:,.0f} cups, {gap_a:.1%} above the till's {till.cups_sold.mean():,.0f}")
check("by hand and by code, the chain gives 2,700 cups", cups == by_hand == 2700)
check("candidate B lands nearer the till than A", abs(2350 - till.cups_sold.mean()) < abs(cups - till.cups_sold.mean()))

fig, ax = plt.subplots(figsize=(8, 3.4))
steps = ["students on campus", "x 0.45 who buy tea", "x 2 cups each"]
bars = ax.bar(steps, running, color=[PALE, LILAC, VIOLET], edgecolor=VIOLET)
ax.bar_label(bars, labels=[f"{v:,.0f}" for v in running])
ax.set_ylim(0, 3500)
ax.set_ylabel("running product")
ax.set_title("The chain, said aloud: 3,000, then 1,350 who buy, then 2,700 cups (invented)", loc="left")
plt.show()
'''),
        md("""
        **What happened.** The answer is b. B lands nearer the till, and still scores lower: its
        2,350 cannot be checked, defended or improved, while A's 2,700 shows which guess to replace.
        Think Insights' guide to guesstimates says the interviewer "is interested in your thought
        process; not the final result", and that the best candidates "validate their results & try
        to spot their own mistake before telling their interviewer they are done".

        Units multiply as well as numbers: students x (buyers per student) x (cups per buyer) =
        cups. Writing the unit beside each factor is how the chain is checked before it is
        calculated.

        ## Which guess sets the range?

        Move one guess at a time to its low end and its high end, holding the other two at their
        central values. The widest bar is the guess to replace with a count first.

        **Predict before you run.** Which guess moves the answer most?

        a) Students on campus
        b) The share who buy tea
        c) Cups each buyer drinks
        d) All three move it equally
        """),
        code('''
def swing(ledger):
    """Each factor moved to its low and its high end, the others held at their central values."""
    out = {}
    for factor in ledger.index:
        ends = []
        for end in ("low", "high"):
            values = ledger.central.copy()
            values[factor] = ledger.loc[factor, end]
            ends.append(values.prod())
        out[factor] = ends
    return pd.DataFrame(out, index=["low", "high"]).T

sw = swing(ledger)
sw["width"] = sw.high - sw.low
sw = sw.sort_values("width")
print(sw[["low", "high"]].round(0).astype(int).to_string())
check("the share who buy sets the range: 1,500 to 3,900", sw.index[-1] == "share who buy tea on a weekday"
      and sw.loc["share who buy tea on a weekday", ["low", "high"]].tolist() == [1500, 3900])

fig, ax = plt.subplots(figsize=(9, 3.4))
ax.barh(sw.index, sw.width, left=sw.low, color=[LILAC, LILAC, VIOLET])
ax.axvline(cups, color=ROSE)
ax.set_ylim(-1.0, 2.6)
ax.text(cups + 40, -0.75, f"central: {cups:,.0f} cups", color=ROSE)
ax.set_xlabel("cups of tea on a weekday")
ax.set_title("Which guess moves the canteen's cups most? (invented)", loc="left")
plt.show()
'''),
        md("""
        **What happened.** The answer is b. With the other two held, students move the answer from
        2,430 to 2,970, cups each from 2,025 to 3,375, and the share who buy from 1,500 to 3,900.
        Say it as: "about 2,700 cups, 1,500 to 3,900 by the share who buy." A range more than twice
        its low end tells the canteen head which number to count before ordering.

        ## Is the answer sane against the till?

        A **check** is a number someone counted, in the same unit, the same period and the same
        definition as the estimate. The till counts cups of tea sold on a weekday, so it passes all
        three tests.

        **Predict before you run.** The chain says 2,700 and the till 2,340. Which guess should
        move?

        a) Students on campus, since the head count may be stale
        b) The share who buy, since it sets the range and the till sits inside it
        c) Cups each, since nobody drinks exactly two
        d) None: the till must be wrong, since the chain was careful
        """),
        code('''
till_mean = till.cups_sold.mean()
implied_share = till_mean / (ledger.loc["students on campus", "central"] * ledger.loc["cups each buyer drinks", "central"])
print(f"the till: {till_mean:,.0f} cups a weekday; the chain runs {gap_a:.1%} high")
print(f"the share that lands on the till: {implied_share:.2f}")
check("the till sits inside the share's range", sw.loc["share who buy tea on a weekday", "low"] <= till_mean
      <= sw.loc["share who buy tea on a weekday", "high"])
check("the share the till implies is 0.39", round(implied_share, 2) == 0.39)

fig, ax = plt.subplots(figsize=(8, 3.4))
ax.axhspan(1500, 3900, color=PALE, label="the range, by the share who buy")
ax.bar(till.weekday, till.cups_sold, color=LILAC, edgecolor=VIOLET, label="the till, each weekday")
ax.axhline(cups, color=ROSE, label="the chain's 2,700")
ax.set_ylim(0, 4200)
ax.set_ylabel("cups of tea")
ax.set_title("The till sits inside the range and below the chain (invented)", loc="left")
ax.legend(loc="upper right", fontsize=9)
plt.show()
'''),
        md("""
        **What happened.** The answer is b. The chain runs 15.4 percent above the till's 2,340, and
        the share that lands on the till is 0.39: 3,000 x 0.39 x 2 = 2,340. The share is the widest
        guess and the one the till contradicts, so it moves; the canteen head now has a number she
        can order milk on and a reason for it.

        ## What does a sanity check catch that careful arithmetic misses?

        **The plausible wrong answer.** "A town of 24,000 people (invented) has 96,000 households."
        Size a household business on it and the market is sixteen times too large. A hurried chain
        multiplies where it should divide, and every step after it is careful.

        **Predict before you run.** With about 4 people to a household, which pair is the hurried
        count and then the right one?

        a) 96,000 hurried, about 6,000 right
        b) 6,000 hurried, about 96,000 right
        c) 24,000 both ways, since the town does not change
        d) 96,000 both ways, since four is the household size
        """),
        code('''
t = tests.set_index(["test", "quantity"]).value
people, per_household = t["unit", "people"], t["unit", "people to a household"]
hurried = people * per_household                      # the unit multiplied where it should be divided
right = people / per_household
print(f"hurried: {hurried:,.0f} households from {people:,.0f} people; right: {right:,.0f}")
check("the hurried count fails the first test: households never exceed people", hurried > people)
check("the fix divides: about 6,000 households", right == 6000)

gb_day, pack_days, month_days = t["period", "data a day"], t["period", "days in the pack"], t["period", "days in a month"]
print(f"period: the pack {gb_day * pack_days:.0f} GB against a month's {gb_day * month_days:.0f} GB, "
      f"and {gb_day} GB a day in both")
enrolled = t["definition", "students enrolled"]
sat, passed = t["definition", "students who sat"], t["definition", "students who passed"]
print(f"definition: {passed:.0f} passes are {passed / sat:.1%} of those who sat and {passed / enrolled:.1%} of those enrolled")
check("per day, the pack and the month agree", gb_day * pack_days / pack_days == gb_day * month_days / month_days)
check("the two pass rates differ by the denominator alone", round(passed / sat * 100, 1) == 83.7 and round(passed / enrolled * 100, 1) == 75.3)

fig, axes = plt.subplots(1, 3, figsize=(10, 3.2))
axes[0].bar(["people", "hurried\\nhouseholds", "households"], [people, hurried, right], color=[LILAC, ROSE, VIOLET])
axes[0].set_title("Unit", loc="left")
axes[1].bar(["28-day pack", "30-day month"], [gb_day * pack_days, gb_day * month_days], color=[LILAC, VIOLET])
axes[1].set_title("Period: GB in total", loc="left")
axes[2].bar(["of those\\nwho sat", "of those\\nenrolled"], [passed / sat * 100, passed / enrolled * 100], color=[LILAC, VIOLET])
axes[2].set_title("Definition: pass rate, %", loc="left")
fig.suptitle("Three ways a check fails: unit, period, definition (invented)", x=0.02, ha="left")
fig.tight_layout()
plt.show()
'''),
        md("""
        **Why it is wrong.** The answer is a. Households are people divided by about four, so the town
        has about 6,000; the chain multiplied the unit, and nothing after it could repair that. **The
        check:** households never exceed people. **The fix:** write the unit beside every factor
        before multiplying. The other two tests fail the same quiet way: a 28-day pack of 1.5 GB a
        day is 42 GB and a 30-day month at the same rate is 45 GB, so compare per day; Gulmohar's
        113 passes are 83.7 percent of the 135 who sat and 75.3 percent of the 150 enrolled, so use
        the denominator the question names.

        Named last, the four steps the canteen ran: **clarify** the unit, the period and what
        counts; **map** the answer as a chain of factors; **calculate** each factor aloud with its
        range; **validate** against a number counted in the same unit, period and definition. That
        is the guesstimate: clarify, map, calculate, validate. The function below is the last
        step, and it refuses a comparison that fails any of the three tests.
        """),
        code('''
def validate(estimate, known, same_unit, same_period, same_definition):
    """The gap between an estimate and a counted number, or no verdict when the comparison is unfair."""
    if not (same_unit and same_period and same_definition):
        return "not a check"
    return f"{estimate / known - 1:+.1%}"

print("the till:", validate(cups, till_mean, True, True, True))
print("the campus head count:", validate(cups, ledger.loc["students on campus", "central"], False, True, True))
check("the till is a check", validate(cups, till_mean, True, True, True) != "not a check")
check("a head count is no check on cups", validate(cups, 3000, False, True, True) == "not a check")
'''),
        md("""
        **Your turn.** Re-run the chain with the share the till implies and show that it lands on
        the till; then say the range it would carry if the share's ends stay where they were. Fill
        the blank, type the lines into the empty cell below and run them:

        ```python
        moved = ledger.copy()
        moved.loc["share who buy tea on a weekday", "central"] = ___
        new_cups = moved.central.prod()
        print(round(new_cups))
        check("the chain with the till's share lands on the till", abs(new_cups - till_mean) < 1)
        ```
        """),
        empty(),
        md("""
        ## Which rules does the chapter leave?

        1. Clarify the unit, the period and what counts before writing any number.
        2. Map the answer as a chain of factors that multiplies out in the unit you clarified.
        3. Say each factor aloud with its range, and name the factor that sets the range.
        4. Validate against a number counted in the same unit, period and definition, and move the
           answer if the check says so.

        **In the interview.** [S] A guesstimate: how many customers could a new store sign up to a
        loyalty tier in its first year? The structure, the stated assumptions and the check carry
        most of the score.

        **Where it is used next.** Chapter 8's notebook,
        `C2_W04_D02_08_case_guesstimate_drivers_at_peak_STUDENT.ipynb`, sizes the drivers Uber
        needs online at the evening peak with the same four steps, and the lab's notebook 11 sizes
        a new Kalpa store's sign-ups.
        """),
    ]


# ------------------------------------------------------------------ concept notebook 07
def nb07():
    return [
        md("""
        # The AI-free written business case: what must a page carry?

        **Week 4, Tuesday, concept notebook 5 of 5, beside chapter 7 of the deck.** Ramesh's shop
        returns from notebook 01 with the same invented numbers. His son wrote two versions of the
        case for keeping the longer hours: a draft of nine lines and a page of four sentences. This
        notebook writes nothing: it counts what the two versions carry, and afterwards it checks
        the page you write by hand in chapter 9.

        **Who needs the answer.** Ramesh (invented), reading his son's page alone in the evening,
        and later today the city head, reading the page each learner writes by hand. A **business
        case** says what to do, why, what it costs, what it returns and what could go wrong. It is
        one page because the reader has two minutes, and it is written without AI because it shows
        your own thinking.

        **The questions on the way.** Which opening does Ramesh act on? What do the draft and the
        page carry, counted? What goes on the page, in what order? Which words stay off it?
        """),
        code(SETUP + '''
import re
text = open("../data/C2_W04_D02_kirana_page_STUDENT.txt", encoding="utf-8").read()
draft_text, page_text = text.split("=====")
draft = [l[2:] for l in draft_text.splitlines() if l.startswith("- ")]
page = [l for l in page_text.splitlines() if l.strip() and not l.startswith("VERSION")]
print(text)                                    # both versions in full; every number is invented
check("the draft has nine lines", len(draft) == 9)
check("the page has four sentences", len(page) == 4)
'''),
        md("""
        ## Which opening does Ramesh act on in two minutes?

        **Opening A** is the draft's first three lines; **opening B** is the page's first sentence.

        **Predict before you run.** Does a business case need a spreadsheet and ten pages? Which
        opening does Ramesh act on?

        a) A, since it carries more numbers
        b) B, since it states the claim in a sentence
        c) Neither, without a chart
        d) Both equally
        """),
        code('''
METHOD = ["denominator", "index", "guardrail", "north star"]

def counts(body):
    """Lines, numbers and method words a reader has to get through."""
    lines = [l for l in body.splitlines() if l.strip() and not l.startswith("VERSION")]
    return {"lines": len(lines), "numbers": len(re.findall(r"\\d[\\d,.]*", body)),
            "method words": sum(word in body.lower() for word in METHOD)}

table = pd.DataFrame({"the draft": counts(draft_text), "the page": counts(page_text)})
print("Opening A:", " / ".join(draft[:3]))
print("Opening B:", page[0])
print(table.to_string())
check("the draft carries 13 numbers and the page 6", table.loc["numbers"].tolist() == [13, 6])
check("the page carries no method word", table.loc["method words", "the page"] == 0)

ax = table.plot.bar(color=["gray", VIOLET], figsize=(8, 3.4), rot=0)
for container in ax.containers:
    ax.bar_label(container)
ax.set_title("The page says less and means more (invented)", loc="left")
plt.show()
'''),
        md("""
        **What happened.** The answer is b. A sentence has to carry its reasoning where a bullet can
        hide it, and opening B says what to do and why before any number. Opening A needs a reader
        who knows what a north star, a denominator and an index are. The draft runs to nine lines,
        13 numbers and four method words; the page to four sentences, 6 numbers and none.

        Amazon's 2017 letter to shareholders, filed 18 April 2018, says: "We don't do PowerPoint
        (or any other slide-oriented) presentations at Amazon." The owner writes a six-page memo
        and the room reads it in silence at the start of the meeting. The afternoon's page is the
        memo form of the morning's slide, cut to one page.

        ## What goes on the page, in what order?

        **Predict before you run.** Where on the page does the caveat sit?

        a) First, so nobody misses it
        b) Before the action, so the reader meets the doubt before the cost
        c) After the action, as a footnote
        d) In an attachment
        """),
        code('''
parts = ["claim", "evidence", "caveat", "action"]
for part, sentence in zip(parts, page):
    print(f"{part:>8}: {sentence}")
check("the claim comes first and gives its reason", "because" in page[0])
check("the evidence carries a number with what it is divided by", "per hour" in page[1])
check("the caveat sits before the action", parts.index("caveat") < parts.index("action"))
check("the action carries its cost and who signs", "Rs" in page[3] and "signs" in page[3])

fig, ax = plt.subplots(figsize=(10, 4.2))
for k, (part, sentence) in enumerate(zip(parts, page)):
    y = 0.9 - k * 0.24
    ax.text(0.0, y, part, weight="bold", color="white", va="top",
            bbox=dict(boxstyle="round", fc=[INK, VIOLET, AMBER, VIOLET][k], ec="none"))
    ax.text(0.13, y, textwrap.fill(sentence, 92), va="top", fontsize=10)
ax.axis("off")
ax.set_title("Ramesh's page in the order he reads it (invented)", loc="left")
plt.show()
'''),
        md("""
        **What happened.** The answer is b. The page runs claim, evidence, caveat, action, one
        sentence each: the reader meets the doubt before the cost, and the action names what to do,
        what it costs (Rs 170 a day) and who signs.

        ## Which words stay off the page?

        A method word is one a reader has to decode before the sentence means anything. Each has
        plain words that replace it:

        | Method word | The plain words that replace it |
        |---|---|
        | Denominator | divided by |
        | Index | compared with the month before |
        | Guardrail | a number that must not get worse |
        | North star | the one number the team is judged on |

        **The plausible wrong answer.** "The draft is the thorough version: it carries every
        number, so it should go to Ramesh." The check below is the rule as a function, run on both
        versions.

        **Predict before you run.** Of the five rules, how many does the draft pass?

        a) All five
        b) Four
        c) One
        d) None
        """),
        code('''
def page_check(text):
    """The AI-free written business case, as checks a reader would make in two minutes."""
    sentences = [s for s in text.splitlines() if s.strip() and not s.startswith("VERSION")]
    words = len(text.split())
    return {"opens on a claim with its reason": "because" in sentences[0] or " so " in sentences[0],
            "no method words": not any(w in text.lower() for w in METHOD),
            "the action names a cost and who signs": "Rs" in sentences[-1] and "signs" in sentences[-1],
            "one page, 250 words or fewer": words <= 250,
            "four to six sentences": 4 <= len(sentences) <= 6}

grid = pd.DataFrame({"the draft": page_check(draft_text), "the page": page_check(page_text)})
print(grid.to_string())
print("words on the page:", sum(len(s.split()) for s in page))
check("the page passes every rule", grid["the page"].all())
check("the draft fails the claim and the method words", not grid.loc["opens on a claim with its reason", "the draft"]
      and not grid.loc["no method words", "the draft"])

fig, ax = plt.subplots(figsize=(8, 3.2))
from matplotlib.colors import ListedColormap
ax.imshow(grid.astype(int).values, cmap=ListedColormap([ROSE, PALE]), vmin=0, vmax=1, aspect="auto")
ax.set_xticks(range(2), grid.columns)
ax.set_yticks(range(len(grid)), grid.index)
for i in range(len(grid)):
    for j in range(2):
        ax.text(j, i, "passes" if grid.iloc[i, j] else "fails", ha="center", va="center",
                color=INK if grid.iloc[i, j] else "white", weight="bold")
ax.set_title("The same rules, run on both versions (invented)", loc="left")
plt.show()
'''),
        md("""
        **Why it is wrong.** The answer is c: the draft passes only the length rule. Thorough is
        measured by what the reader can act on in two minutes. The draft opens on a list of figures
        with no claim, needs four method words decoded, and puts
        no cost or signer in its last line; the page carries 108 words and passes every rule.
        **The check:** read the first sentence alone: does it say what to do and why? **The fix:**
        the four parts as four sentences, in plain words.

        Named last: the AI-free written business case is the slide's four parts as four sentences
        on one page, read in two minutes by someone who was not in the room, written by hand in
        your own words.

        **Your turn, after chapter 9.** Type the page you wrote by hand for the city head into
        `my_page`, one sentence a line, and run the same rules on it. The rules check the shape;
        your trainer reads the argument. Type the lines into the empty cell below and run them:

        ```python
        my_page = \"\"\"
        ___
        \"\"\".strip()
        mine = page_check(my_page)
        print(pd.Series(mine).to_string())
        check("my page opens on its claim", mine["opens on a claim with its reason"])
        check("my page carries no method words", mine["no method words"])
        ```
        """),
        empty(),
        md("""
        ## Which rules does the chapter leave?

        1. The first sentence is the claim, with what to do and why.
        2. The second carries one number, what it is divided by and its window.
        3. The caveat comes before the action, so the reader meets the doubt first.
        4. The action names what to do, its cost in rupees and weeks, and who signs.

        **In the interview.** [S] Present a recommendation to a non-technical stakeholder in two
        minutes: the page, spoken.

        **Where it is used next.** Chapter 9 is the page to the city head, written by hand in 35
        minutes with laptops closed, so it has no notebook; this notebook's `page_check` is the
        check you run on it afterwards.
        """),
    ]


# ------------------------------------------------------------------ case notebook 08
def nb08():
    return [
        md(f"""
        # Drivers at Uber's evening peak, sized by the guesstimate: how many at the peak?

        **Week 4, Tuesday, chapter 8, the case's third chapter.** It applies the guesstimate:
        clarify, map, calculate, validate (concept notebook 06). On the campus canteen (invented),
        notebook 06 built 3,000 x 0.45 x 2 = 2,700 cups, found the share who buy set the range from
        1,500 to 3,900, and checked it against the till's 2,340 in the same unit, period and
        definition. Notebook 05 left the city head's slide defended against three objections; this
        notebook answers the ticket's second question.

        **The ticket.** Uber, Hyderabad. Before Thursday's review the city head asks one more
        thing: roughly how many drivers must be online at the weekday evening peak to keep the
        median rider wait under five minutes, estimated in fifteen minutes and without a dataset.

        {LABEL}

        **Who needs the answer.** The city head, who will ask the finance partner for incentives
        sized on this number; a figure seven times too large pays for drivers the city does not
        need, and one too small leaves riders waiting.

        **The metric at stake.** Drivers online at one moment of the three-hour weekday evening
        peak.

        **The questions on the way.**

        1. Which number would check the estimate?
        2. What does the chain give, and which assumption moves the answer most?
        3. What does the trap of a day's trips divided by an hour's cost?
        4. Is the estimate sane when checked like for like against the case's own data?
        """),
        code(SETUP + '''
weeks = pd.read_csv("../data/C2_W04_D02_twelve_weeks_STUDENT.csv")  # the case's twelve zones, week by week
check("twelve weeks in the case's table", len(weeks) == 12)
print(weeks[["week_start", "window", "peak_online_hours", "peak_trips", "rider_requests"]].to_string(index=False))
'''),
        md("""
        ## Which number would check the estimate?

        Notebook 06's three tests decide it: a check counts the same unit, over the same period,
        under the same definition. Four candidates:

        | Candidate | What it counts |
        |---|---|
        | a) Monday's rider requests, 256,556 over six weeks | requests, summed over six weeks, in the case's twelve zones |
        | b) A published count of Uber drivers signed up in Hyderabad | sign-ups, at any time |
        | c) A published count of Uber drivers online at one weekday evening peak in Hyderabad | drivers online at one moment |
        | d) The online driver-hours behind each completed trip in the case's own data | a ratio inside the chain |

        **Predict before you run.** Which candidate passes all three tests?
        """),
        code('''
def is_check(same_unit, same_period, same_definition):
    """Notebook 06's three tests: a check counts the same unit, period and definition as the estimate."""
    return same_unit and same_period and same_definition

candidates = pd.DataFrame({
    "same unit":       [False, True,  True,  False],
    "same period":     [False, False, True,  True],
    "same definition": [False, False, True,  True],
}, index=["a) requests over six weeks", "b) drivers signed up", "c) drivers online at one peak", "d) driver-hours per trip"])
candidates["a check?"] = [is_check(*r) for r in candidates.values]
print(candidates.to_string())
check("only a published count of drivers online at one peak passes all three", candidates["a check?"].sum() == 1
      and candidates["a check?"].iloc[2])
'''),
        md("""
        **What happened.** The answer is c, and nobody publishes it: no source in the research
        ledger holds a count of Uber drivers online at Hyderabad's evening peak, so that slot stays
        "to be found". a counts rider requests over six weeks in twelve zones: another unit, a longer
        period and a slice of the city. b counts sign-ups, a different definition from drivers
        online at one moment. d is not wrong: it checks one link of the chain, a ratio the case's
        own data holds, and when the direct check does not exist that is the honest fallback the
        afternoon uses.

        ## What does the chain give, and which assumption moves the answer most?

        **Clarify.** One city (the Hyderabad metro area), one platform (Uber) and one product, the
        three-hour weekday evening peak, drivers online at one moment, and a median rider wait
        under five minutes.

        **Map.** Drivers online = (trips to serve in an hour / trips one online driver completes in
        an hour) x a buffer. Trips to serve in an hour = people x weekday Uber trips per person x
        the share of the day's trips in the evening window / 3 hours; counting trips per person,
        never riders, counts a commuter who rides both ways twice. Trips one online driver
        completes in an hour = the trips a busy driver fits in an hour x (1 - the idle share), where
        the idle share is the share of online drivers with no rider at that moment. The buffer
        covers the busiest half hour of the window.

        Every value below is a guess said aloud, with the range it could take and the reason beside
        it.

        **Predict before you run.** If people took 2 weekday Uber trips per 100 instead of 1, what
        would happen to the answer?

        a) It doubles, to about 11,400
        b) It rises by about a quarter
        c) It does not change, since the buffer absorbs it
        d) It halves
        """),
        code('''
# The ledger: every guess with its range, then the chain run on every version of the ledger.
ledger = pd.DataFrame([   # assumption: central, low, high, and why
    ("people in the city",               10_000_000, 9_000_000, 11_000_000, "the metro area, a round number"),
    ("weekday Uber trips per person",    0.01,       0.005,     0.015,      "1 trip for every 100 people"),
    ("share of trips in the evening",    0.25,       0.20,      0.30,       "the evening commute"),
    ("trips a busy driver fits an hour", 2.4,        2.0,       3.0,        "a peak trip takes about 25 minutes"),
    ("idle share",                       0.30,       0.22,      0.38,       "a guess, from a busy evening to a slack one"),
    ("buffer for the busiest half hour", 1.15,       1.10,      1.25,       "the peak inside the peak"),
], columns=["assumption", "central", "low", "high", "why"]).set_index("assumption")

versions = pd.DataFrame([ledger.central.values], index=["central"], columns=ledger.index)
for name in ledger.index:                       # one row per version: one guess moved to an end
    for end in ("low", "high"):
        versions.loc[f"{name}, {end}"] = ledger.central
        versions.loc[f"{name}, {end}", name] = ledger.loc[name, end]
versions.loc["2 trips per 100 people"] = ledger.central
versions.loc["2 trips per 100 people", "weekday Uber trips per person"] = 0.02

v = versions                                    # the chain, run down every row at once
trips_an_hour = v["people in the city"] * v["weekday Uber trips per person"] * v["share of trips in the evening"] / 3
versions["drivers"] = (trips_an_hour / (v["trips a busy driver fits an hour"] * (1 - v["idle share"]))
                       * v["buffer for the busiest half hour"])
central = versions.loc["central", "drivers"]
doubled = versions.loc["2 trips per 100 people", "drivers"]
ends = pd.DataFrame({end: [versions.loc[f"{name}, {end}", "drivers"] for name in ledger.index]
                     for end in ("low", "high")}, index=ledger.index)
swing = pd.DataFrame({"lowest": ends.min(axis=1), "highest": ends.max(axis=1)}).round(-2).astype(int)
swing["width"] = swing.highest - swing.lowest
swing = swing.sort_values("width")
print(ledger[["why"]])
print(f"trips an hour: {10_000_000 * 0.01 * 0.25 / 3:,.0f}; drivers online: {central:,.0f}; "
      f"at 2 trips per 100 people: {doubled:,.0f}")
print(swing[["lowest", "highest"]])

fig, ax = plt.subplots(figsize=(9, 4))
ax.barh(swing.index, swing.width, left=swing.lowest, color=LILAC)
ax.axvline(central, color=ROSE)
ax.set_ylim(-1.0, 5.6)
ax.text(central + 80, -0.75, f"central: about {round(central, -2):,.0f}", color=ROSE)
ax.set_xlabel("drivers online at the weekday evening peak")
ax.set_title("Which assumption moves the answer most?", loc="left")
plt.show()
check("about 5,700 drivers at the central values", round(central, -2) == 5700)
check("doubling trips per person doubles the answer", abs(doubled / central - 2) < 1e-9)
check("trips per person moves the answer most", swing.index[-1] == "weekday Uber trips per person")
'''),
        md("""
        **What happened.** The answer is a: the chain is a product, so doubling one factor doubles
        the answer, to about 11,400. At the central values, about 8,333 trips an hour divided by
        1.68 trips per online driver-hour (2.4 x 0.70), times 1.15, is about 5,700 drivers. Moving
        trips per person from 0.5 to 1.5 per 100 moves the answer from about 2,900 to about 8,600
        with everything else held, wider than any other assumption; the idle share moves it from
        about 5,100 to 6,400.

        ## What does the trap of a day's trips divided by an hour's cost?

        **The plausible wrong answer.** "1 crore people, 1 trip per 100 people, so 1 lakh trips; a
        driver does 2.4 trips an hour; so about 41,700 drivers." A city head who takes that to the
        review asks for incentives for about seven times the drivers the chain says are needed.

        **Predict before you run.** Which step did the hurried chain skip?

        a) The buffer for the busiest half hour
        b) The day's trips were never brought into an hour of the evening window
        c) The people in the city were counted twice
        d) None: it is the chain, rounded differently
        """),
        code('''
day_trips = 10_000_000 * 0.01                          # a day's trips
wrong = day_trips / 2.4                                # divided by an hour's trips per driver
print(f"the hurried chain: {day_trips:,.0f} trips a day / 2.4 an hour = about {round(wrong, -2):,.0f} drivers")
print(f"against the chain's about {round(central, -2):,.0f}: about {wrong / central:.0f} times as many")
check("the hurried answer is about seven times the chain's", 7 < wrong / central < 8)

running = pd.Series({"trips a day": day_trips, "in the evening window": day_trips * 0.25,
                     "an hour of the window": day_trips * 0.25 / 3,
                     "drivers before the buffer": day_trips * 0.25 / 3 / 1.68,
                     "drivers online": day_trips * 0.25 / 3 / (2.4 * 0.7) * 1.15})
fig, ax = plt.subplots(figsize=(9, 3.6))
bars = ax.bar(running.index, running, color=[PALE, PALE, LILAC, LILAC, VIOLET], edgecolor=VIOLET)
ax.bar_label(bars, labels=[f"{x:,.0f}" for x in running], fontsize=9)
ax.set_xticks(range(5), ["trips\\na day", "in the evening\\nwindow", "an hour of\\nthe window",
                         "drivers before\\nthe buffer", "drivers\\nonline"])
ax.set_title("The chain carries each unit to the next: a day, the window, an hour, drivers", loc="left")
plt.show()
check("a second route, step by step, reaches the same drivers", abs(running.iloc[-1] - central) < 1e-6)
'''),
        md("""
        **Why it is wrong.** The answer is b. A day's trips were divided by an hour's trips per
        driver: a period mismatch, and the idle share and the buffer were skipped as well. **The check:**
        write the unit beside every factor. **The fix:** bring the day's trips into the evening
        window's hour before dividing. The step-by-step chain above is a second route to the same
        5,700, and it agrees with the vectorised chain to the driver.

        ## Is the estimate sane when checked like for like against the case's own data?

        **Validate.** Monday's tables are a slice of the city, the twelve zones the enrolled drivers
        work, so their absolute count cannot check a city total. Monday's data counts peak hours on
        all seven days, two three-hour windows a day, 42 hours a week, so its 256,556 after-window
        requests are about 1,018 an hour, far below the city's 8,333 trips. What the slice can
        check is a ratio in the middle of the chain, counted the same way on both sides: online
        driver-hours per completed trip.
        """),
        code('''
# Check the chain like for like against the case's driver-hours per trip, then a month's own days.
case = weeks.groupby("window")[["peak_online_hours", "peak_trips"]].sum().loc[["before", "after"]]
per_trip = case.peak_online_hours / case.peak_trips          # online driver-hours per completed trip
case["driver_hours_per_trip"] = per_trip.round(2)
chain = 1 / (2.4 * (1 - 0.30))
case_tph_before = 1 / per_trip["before"]
checked = 10_000_000 * 0.01 * 0.25 / 3 / case_tph_before * 1.15
print(case)
print(f"the chain: {chain:.2f} driver-hours per trip before its buffer, "
      f"{chain / per_trip['before']:.2f} times the case's before window")
print(f"re-run at the case's {case_tph_before:.2f} trips an hour: about {round(checked, -2):,.0f} drivers")
check("the chain runs high, by about an eighth", 1.1 < chain / per_trip["before"] < 1.15)

fig, ax = plt.subplots(figsize=(8, 3.4))
bars = ax.bar(["the case, before", "the case, after", "the chain, before its buffer"],
              [per_trip["before"], per_trip["after"], chain], color=[LILAC, LILAC, VIOLET])
ax.bar_label(bars, fmt="%.2f")
ax.set_ylabel("online driver-hours per completed trip")
ax.set_title("Like for like, the chain asks for an eighth more driver time per trip", loc="left")
plt.show()

month_total, days = 9e9, 30                 # an invented payments network: 9 billion in a 30-day month
per_day, over_31 = month_total / days, month_total / 31
print(f"per day: {per_day / 1e6:,.0f} million; over 31 days: {over_31 / 1e6:,.0f} million "
      f"({over_31 / per_day - 1:+.1%})")
check("the per-day figure divides by the month's own days", round(per_day / 1e6) == 300)
'''),
        md("""
        **What happened.** Before the launch the case's twelve zones used 0.53 online driver-hours
        per completed trip, with a median wait of 4.8 minutes; after it, 0.63. The chain puts 0.60
        behind each trip before its buffer, about an eighth more than the window whose wait met the
        target, so the chain errs high. Re-run at the case's 1.90 trips an hour it gives about
        5,000 drivers, so the honest answer is about 5,000 to 5,700. The invented network shows the
        per-day check: 9 billion over its 30 days is 300 million a day, and dividing by 31 gives
        290 million, 3.2 percent low for no reason but the calendar. The afternoon's paired drill
        on UPI meets the published figure only after the swap.

        **The answers, one line each.**

        1. Only a published count of drivers online at one peak would check the estimate directly,
           and none has been found; the case's driver-hours per trip checks one link.
        2. About 5,700 drivers before the check, from about 2,900 to 8,600 with everything else
           held, driven by trips per person.
        3. A day's trips over an hour's rate gives about 41,700, about seven times too many.
        4. Like for like, the chain's 0.60 driver-hours per trip runs an eighth above the case's
           0.53, so say about 5,000 to 5,700.

        ### What will an interviewer ask about this, and what does a strong answer do?

        **[S] How many drivers must be online at the evening peak?** Clarify the city, the product,
        the window, the unit (online at one moment) and the wait target; say the formula; say each
        assumption aloud with its range; give the range with everything else held and the factor
        that drives it; check the ratio like for like and move the answer if the check says so; and
        say what the number decides.

        **The AI-company variant.** The same four steps size an AI company's number: how many
        requests a second a chatbot must serve at its evening peak. Clarify one product, one region
        and requests at one moment; map daily users x requests per user x the evening's share,
        divided by the seconds in the window; calculate each factor aloud with its range; and
        validate against a number counted the same way, such as last month's peak second in the
        serving logs.
        """),
    ]


# ------------------------------------------------------------------ lab notebook 11
def nb11():
    return [
        md("""
        # Kalpa's new store, sized by the guesstimate: how many members could it sign up in its first year?

        **Week 4, Tuesday, the TA-led lab, after chapter 10.** **Applies:** the guesstimate:
        clarify, map, calculate, validate (chapter 6, notebook 06), and the one-slide answer: claim,
        evidence, caveat, action (chapter 1, notebook 01), for what you bring back. Notebook 08
        sized Uber's evening-peak drivers at about 5,000 to 5,700 and checked the chain like for
        like against the case's own driver-hours per trip.

        **The question.** Anand Iyer, Kalpa Retail's finance controller, is deciding whether to fund
        a new store, and before the data exists he wants a rough number, sized in fifteen minutes
        from stated assumptions: how many customers it could sign up to Retail-Plus, Kalpa's paid
        membership tier, in its first year. A sign-up is a new paying member whose home store is
        the new one.

        **Who needs the answer.** Anand, who funds or does not fund the store, and who will ask how
        you know your number is not wildly off.

        **The questions on the way.** What exactly is counted? Which chain gives sign-ups, and
        which link can a published number check? Which store count turns DMart's revenue into a
        year per store? Which guess sets your range?

        This notebook sets up the tools and the published anchor; the sizing is yours, in the empty
        cells.
        """),
        code(SETUP + '''
anchor = pd.read_csv("../data/C2_W04_D02_kalpa_dmart_anchor_STUDENT.csv")
print(anchor.iloc[:4].to_string(index=False))          # the published figures, with their source
a = anchor.set_index("item").value
check("the opening count is the closing count less the stores added",
      a["Stores at 31 March 2025"] == a["Stores at 31 March 2026"] - a["Stores added in FY26"])
'''),
        md("""
        ## Which store count turns DMart's revenue into a year per store?

        DMart, a large grocery chain, publishes its revenue and its store counts; nobody publishes
        how many members a new store signs up. A year's revenue was earned by the stores open
        across the year, and DMart opened 85 stores during FY26, so the count at the year's end
        overstates the stores that sold all year. The fair count for a year is the average of the
        opening and closing counts.
        """),
        code('''
opening, closing = a["Stores at 31 March 2025"], a["Stores at 31 March 2026"]
average_count = (opening + closing) / 2
print(f"stores: {opening:.0f} at the start of FY26, {closing:.0f} at its end, {average_count} on average")
check("the average count is 457.5", average_count == 457.5)
check("the year-end count overstates the stores that sold all year", closing > average_count)

fig, ax = plt.subplots(figsize=(8, 3.4))
ax.plot([0, 12], [opening, closing], color=VIOLET, lw=2.5, label="stores open, if added evenly")
ax.axhline(average_count, color=ROSE, ls="--", label="the average count")
ax.axhline(closing, color="gray", ls=":", label="the year-end count")
ax.set_xticks([0, 6, 12], ["1 Apr 2025", "Oct 2025", "31 Mar 2026"])
ax.set_ylabel("DMart stores")
ax.set_title("A year's revenue was earned by the stores open across it", loc="left")
ax.legend(fontsize=9)
plt.show()
'''),
        md("""
        ## Which chain gives sign-ups, and which link can a published number check?

        **Clarify.** One new store, its first year, sign-ups counted as new paying members whose
        home store is the new one. **Map.** Sign-ups = households near the store x the share who
        shop there in year one x the share of those shoppers who sign up. The published anchor
        reaches the first two links only: shoppers x visits a month x spend per visit x 12 is the
        store's first-year sales, which can be laid beside what a mature DMart store sells. The
        sign-up share stays a stated guess.

        The two functions below are notebook 06's, restated so this notebook stands alone. The
        cell proves them on notebook 06's canteen (invented) before you use them.
        """),
        code('''
def chain(ledger):
    """The answer at the central guesses: the factors multiplied."""
    return ledger.central.prod()

def swing(ledger):
    """Each factor moved to its low and its high end, the others held at their central values."""
    out = {}
    for factor in ledger.index:
        ends = []
        for end in ("low", "high"):
            values = ledger.central.copy()
            values[factor] = ledger.loc[factor, end]
            ends.append(values.prod())
        out[factor] = ends
    return pd.DataFrame(out, index=["low", "high"]).T

canteen = pd.read_csv("../data/C2_W04_D02_canteen_ledger_STUDENT.csv").set_index("factor")
sw = swing(canteen)
check("the chain reproduces notebook 06's 2,700 cups", chain(canteen) == 2700)
check("the swing reproduces the share's 1,500 to 3,900", sw.loc["share who buy tea on a weekday"].tolist() == [1500, 3900])
check("every factor's low end gives a smaller answer than its high end", (sw.low <= sw.high).all())

def draw_swing(sw, central, unit):
    sw = sw.assign(width=sw.high - sw.low).sort_values("width")
    fig, ax = plt.subplots(figsize=(9, 3.2))
    ax.barh(sw.index, sw.width, left=sw.low, color=LILAC)
    ax.axvline(central, color=ROSE)
    ax.set_xlabel(unit)
    ax.set_title("Which guess moves the answer most?", loc="left")
    plt.show()

draw_swing(sw, chain(canteen), "cups of tea on a weekday (notebook 06's invented canteen)")

fig, ax = plt.subplots(figsize=(10, 2.6))
boxes = ["households\\nnear the store", "x share who shop\\nthere in year one", "= shoppers",
         "x share who\\nsign up", "= sign-ups"]
for i, label in enumerate(boxes):
    ax.text(i, 0.6, label, ha="center", va="center", fontsize=10,
            bbox=dict(boxstyle="round", fc=VIOLET if i == 4 else PALE, ec=VIOLET),
            color="white" if i == 4 else INK)
ax.text(2, 0.05, "the check: shoppers x visits a month x spend per visit x 12\\nagainst a mature DMart store's year",
        ha="center", va="center", fontsize=9.5, bbox=dict(boxstyle="round", fc="#FFF7E6", ec=AMBER))
ax.set_xlim(-0.6, 4.6)
ax.set_ylim(-0.2, 0.85)
ax.axis("off")
ax.set_title("The map: the anchor checks the shoppers, never the sign-up share", loc="left")
plt.show()
'''),
        md("""
        **Your turn: size Anand's question.** Write your ledger with a central value, a low and a
        high for each of the three factors and one line of why, then run the chain and the swing.
        Type the lines into the empty cell below, with your own numbers in the blanks:

        ```python
        store = pd.DataFrame([
            ("households near the store",        ___, ___, ___, "___"),
            ("share who shop there in year one", ___, ___, ___, "___"),
            ("share of shoppers who sign up",    ___, ___, ___, "___"),
        ], columns=["factor", "central", "low", "high", "why"]).set_index("factor")
        print(f"sign-ups at the central guesses: {chain(store):,.0f}")
        store_swing = swing(store)
        print(store_swing.round(0))
        draw_swing(store_swing, chain(store), "sign-ups in the first year")
        check("every low sits below its central and every high above it",
              ((store.low <= store.central) & (store.central <= store.high)).all())
        ```
        """),
        empty(),
        md("""
        **Your turn: validate against DMart.** Turn your shoppers into a year of sales, then lay
        them beside DMart's revenue per store on the average count. A store in its first year should
        sell less than a mature store; an estimate above it means a guess is too high.

        ```python
        shoppers = store.loc["households near the store", "central"] * store.loc["share who shop there in year one", "central"]
        visits_a_month, spend_per_visit = ___, ___          # your guesses, each said aloud
        first_year_crore = shoppers * visits_a_month * spend_per_visit * 12 / 1e7
        dmart_per_store = a["FY26 standalone total revenue, Rs crore"] / average_count
        print(f"first-year sales: Rs {first_year_crore:,.0f} crore; DMart per store: Rs {dmart_per_store:,.0f} crore")
        check("the new store sells below a mature DMart store", first_year_crore < dmart_per_store)
        ```
        """),
        empty(),
        md("""
        ## What do you bring back to Anand?

        One slide in notebook 01's four parts, said in three minutes to the TA:

        - **The claim:** your sign-ups as a range, and what Anand should do with it.
        - **The evidence:** the chain's central value and the guess that sets the range, from your
          swing.
        - **The caveat:** the DMart check reaches the shoppers and never the sign-up share, and a
          first-year store sells less than a mature one.
        - **The action:** the number to count first, Kalpa's own sign-up rate at its existing
          stores, which would be the like-for-like anchor, and who signs.

        The unguided exercise `exercises/unguided/C2_W04_D02_kalpa_store_STUDENT.md` asks the
        anchor's two decisions in lettered items, and the lab set carries the ladder.
        """),
    ]


NOTEBOOKS = {
    "01": ("C2_W04_D02_01_one_slide_answer_STUDENT.ipynb", nb01),
    "02": ("C2_W04_D02_02_leave_out_and_appendix_STUDENT.ipynb", nb02),
    "03": ("C2_W04_D02_03_defending_under_challenge_STUDENT.ipynb", nb03),
    "04": ("C2_W04_D02_04_case_one_slide_answer_three_denominators_STUDENT.ipynb", nb04),
    "05": ("C2_W04_D02_05_case_defending_under_challenge_evidence_STUDENT.ipynb", nb05),
    "06": ("C2_W04_D02_06_guesstimate_clarify_map_calculate_validate_STUDENT.ipynb", nb06),
    "07": ("C2_W04_D02_07_written_business_case_STUDENT.ipynb", nb07),
    "08": ("C2_W04_D02_08_case_guesstimate_drivers_at_peak_STUDENT.ipynb", nb08),
    "11": ("C2_W04_D02_11_kalpa_store_guesstimate_STUDENT.ipynb", nb11),
}


def main(wanted):
    for key in wanted or NOTEBOOKS:
        name, cells = NOTEBOOKS[key]
        built = build(NB / name, cells())
        print(f"wrote and executed {name}: {len(built.cells)} cells")


if __name__ == "__main__":
    main(sys.argv[1:])

# Test inputs and expected outcomes
# ---------------------------------
# python3 content/W04/D2/internal/C2_W04_D02_build_notebooks_INTERNAL.py
#     writes and executes all nine notebooks, one "wrote and executed" line each; then
#     python3 scripts/nb_check.py content/W04/D2 passes every one.
# python3 content/W04/D2/internal/C2_W04_D02_build_notebooks_INTERNAL.py 06
#     rebuilds notebook 06 alone.
# python3 content/W04/D2/internal/C2_W04_D02_build_notebooks_INTERNAL.py 09
#     KeyError: '09', since chapter 9 has no notebook; nothing is written.

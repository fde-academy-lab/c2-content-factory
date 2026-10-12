"""Write Friday's four notebooks and execute each cold in its own folder.

    python3 content/W04/D5/internal/C2_W04_D05_build_notebooks_INTERNAL.py

The markdown here is the notebooks' prose, so the humanizer's file-mode read runs on this script.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import md, code, empty, build  # noqa: E402

NB = ROOT / "content" / "W04" / "D5" / "notebooks"
LABEL = ("Illustrative case: the company is real, the situation and the data are synthetic, built "
         "for this class.")
TICKET = f"""**The ticket.** Flipkart, the Lucknow fulfilment centre, festive packer headcount. The centre
has 104 weeks of outbound shipments, the weeks beginning Monday 30 September 2024 to Monday 21
September 2026. Diwali fell on Thursday 31 October 2024 and Monday 20 October 2025, and falls on
Sunday 8 November 2026. A packer packs about 120 shipments a shift. The planner must book packer
shifts for the eight festive weeks beginning 12 October to 30 November 2026. A vendor's demand
model promises the festive window 22 percent above last year's; finance's rule is last year's
window plus 4 percent, eighteen points apart. An idle packer-shift costs Rs 650 (assumed, Rs 500 to
800) and a late shipment Rs 25 (assumed, Rs 15 to 40). {LABEL}"""

SETUP = '''import math
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"figure.figsize": (9, 3.8), "font.size": 11,
                     "axes.spines.top": False, "axes.spines.right": False})

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
'''


def nb01():
    return [
        md(f"""
        # What shape do the 104 weeks have, and what would three simple rules say for one week?

        **Week 4, Friday, chapter 1 of 3.** {TICKET}

        **Who needs the answer.** The FC planner, who books packer shifts weeks before the festival
        and cannot add a shift on the day, and the regional operations head, who signs the plan. A
        rule that puts the busiest week in the wrong place books packers for a week that is quiet.

        **The questions on the way.** What does a forecast copy from the past, on a toy you can do
        in your head? Where is each year's peak on twelve real weeks? What do three rules say for
        Diwali 2025's own week? Which week does the copy of last year put the peak in? Does the full
        series show the same shape?
        """),
        code(SETUP + '''
rows = pd.read_csv("../data/C2_W04_D05_twelve_rows_STUDENT.csv", parse_dates=["week_start"])
s = rows.set_index("week_start").shipments
rows
'''),
        md("""
        ## What does a forecast copy from the past, on numbers you can hold in your head?

        A canteen sold 50, 52, 49 and 51 cups of tea on four days (invented). The simplest forecast,
        called **naive**, says tomorrow repeats the last day. If Sundays always sell about 80, the
        forecast for next Sunday copies last Sunday: a **seasonal** copy, the same day a week ago.
        """),
        code('''
cups = [50, 52, 49, 51]                      # four days at a canteen (invented)
print("naive forecast for tomorrow:", cups[-1])
last_sunday = 80                             # last Sunday's cups (invented)
print("seasonal forecast for next Sunday:", last_sunday)
check("naive repeats the last value", cups[-1] == 51)
'''),
        md("""
        ## Where is each year's busiest week on the twelve rows?

        The twelve rows are six weeks around Diwali 2024 and six around Diwali 2025, straight from
        the centre's data.

        **Predict before you run.** In each year, which week ships the most?

        a) Diwali's own week
        b) the week before Diwali's week
        c) two weeks before Diwali's week
        d) the week after Diwali's week
        """),
        code('''
diwali = pd.to_datetime(["2024-10-28", "2025-10-20"])   # the weeks holding Diwali
colours = ["crimson" if d in diwali else "lavender" for d in rows.week_start]
fig, ax = plt.subplots()
ax.bar(rows.week_start.dt.strftime("%d %b %y"), rows.shipments, color=colours, edgecolor="slateblue")
ax.tick_params(axis="x", rotation=60)
ax.set_title("Twelve weeks around two Diwalis (red: the week holding Diwali)")
plt.show()
peaks = rows.loc[rows.groupby(rows.week_start.dt.year).shipments.idxmax()]
print(peaks.to_string(index=False))
check("both peaks sit two weeks before Diwali's week",
      list(peaks.week_start) == list(pd.to_datetime(["2024-10-14", "2025-10-06"])))
'''),
        md("""
        **What happened.** The answer is c. The busiest week is two weeks before Diwali's week in
        both years: 401,000 shipments in the week of 14 October 2024 and 418,200 in the week of 6
        October 2025. Parcels leave the centre before the festival so they arrive in time, which is
        why Diwali's own week ships less (296,900 and 308,900) and the week after falls lowest.

        ## What do three rules forecast for Diwali 2025's own week?

        Stand in the week of 13 October 2025 and forecast the next week, 20 October 2025.
        **Naive** repeats the week before. **Same week last year** copies the week 52 weeks back,
        which is the week of 21 October 2024. **Festival-aligned** copies the week at the same
        distance from last year's Diwali, which is Diwali 2024's own week, 28 October 2024, and adds
        the 4 percent a year the centre grew.

        **Predict before you run.** Which rule lands closest to the 308,900 that shipped?

        a) naive
        b) same week last year
        c) festival-aligned
        d) all three land within 10,000
        """),
        code('''
week = pd.Timestamp
actual = s[week("2025-10-20")]
naive = s[week("2025-10-13")]                       # the week before
same_week = s[week("2024-10-21")]                   # 52 weeks back
aligned = round(s[week("2024-10-28")] * 1.04)       # Diwali 2024's week, plus 4 percent
for name, f in [("naive", naive), ("same week last year", same_week), ("festival-aligned", aligned)]:
    print(f"{name:22s} {f:>9,}   miss {f - actual:>+9,}")
check("festival-aligned lands closest",
      abs(aligned - actual) < min(abs(naive - actual), abs(same_week - actual)))
'''),
        md("""
        **What happened.** The answer is c. Naive misses by 60,100 and same week last year by
        47,300, both too high; festival-aligned misses by 124. The week 52 weeks back looks like
        "the same week", but in 2024 it was the week before Diwali, and the week before Diwali
        ships more than Diwali's own week.

        ## Which week does a copy of last year put the peak in?

        **The plausible wrong answer.** "Same week last year already knows the season, so it is the
        safe rule for a festival." Copy every 2025 week from 52 weeks back and see where its peak
        lands.
        """),
        code('''
y25 = s[s.index.year == 2025]
copy52 = pd.Series({d: s.get(d - pd.Timedelta(weeks=52)) for d in y25.index}).astype("Int64")
copy51 = pd.Series({d: round(s[d - pd.Timedelta(weeks=51)] * 1.04) for d in y25.index})
table = pd.DataFrame({"actual": y25, "same week last year": copy52, "festival-aligned": copy51})
print(table.to_string())
ax = table.astype(float).plot(marker="o", title="2025's festive weeks against two copies of 2024")
ax.set_xlabel("week beginning")
plt.show()
check("the copy of last year peaks on 13 Oct 2025", copy52.idxmax() == week("2025-10-13"))
check("the actual peak is 6 Oct 2025", y25.idxmax() == week("2025-10-06"))
'''),
        md("""
        **Why it is wrong.** Diwali's week came one week earlier in 2025, so the copy of the same
        calendar week put 2024's peak (401,000) on 13 October 2025, a week late, and left the real
        peak week short. The check that catches it is the calendar: line up each year's weeks by
        their distance from Diwali before copying. The week of 29 September 2025 shows a blank in
        the copy, because its source, 30 September 2024, is not one of the twelve rows.

        ## Where does a copy of 2025 put Diwali in 2026?

        Diwali 2026 falls on Sunday 8 November, so its week begins Monday 2 November 2026.
        """),
        code('''
lands = week("2025-10-20") + pd.Timedelta(weeks=52)       # 2025's Diwali week, copied a year on
diwali_2026 = week("2026-11-02")
print("the copy puts Diwali 2025's week on the week of", lands.date())
print("weeks before the real Diwali week:", (diwali_2026 - lands).days // 7)
check("the copy lands two weeks early", (diwali_2026 - lands).days == 14)
'''),
        md("""
        ## Does the full series show the same shape?

        The twelve rows came from 104 weeks. The whole series shows the same two festive peaks, an
        August sale each year and ordinary weeks a little above the ticket's 210,000.
        """),
        code('''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.plot(weekly.week_start, weekly.shipments, color="slateblue")
for d in diwali:
    ax.axvline(d, color="crimson", ls="--")
ax.set_title("104 weeks of outbound shipments; dashed: the weeks holding Diwali")
plt.show()
check("104 weeks", len(weekly) == 104)
check("the twelve rows are rows of the full series",
      rows.merge(weekly, on=["week_start", "shipments"]).shape[0] == 12)
'''),
        md("""
        ## What did chapter 1 answer?

        - **What does a forecast copy?** The last value (naive) or the same point in the last cycle
          (seasonal): tomorrow's tea is 51, next Sunday's is 80, on invented numbers.
        - **Where is the peak?** Two weeks before Diwali's week in both years, 401,000 and 418,200.
        - **What do three rules say for 20 October 2025?** Naive 369,000, same week last year
          356,200, festival-aligned 308,776 against 308,900 shipped.
        - **Where does a copy of last year put the peak?** A week late in 2025, and two weeks early
          in 2026, on the week of 19 October against Diwali's week of 2 November.
        - **Does the full series agree?** Yes: two festive peaks, an August sale, ordinary weeks a
          little above 210,000.

        Chapter 2 asks the question one week cannot settle: how does each rule score on thirteen
        weeks it never saw?
        """),
    ]


def nb02():
    return [
        md(f"""
        # How does each rule score on the thirteen weeks it never saw, and which way is each wrong?

        **Week 4, Friday, chapter 2 of 3.** {TICKET}

        Chapter 1 found the peak two weeks before Diwali's week and showed that a copy of the same
        calendar week lands it a week late in 2025 and two weeks early in 2026. This notebook scores
        every rule, and the vendor's curve, on weeks none of them saw.

        **Who needs the answer.** The FC planner, who may send only a forecast that has beaten the
        house rule on weeks it never saw, and the regional operations head, who must say yes or no
        to the vendor's plus 22 percent before a shift is booked.

        **The questions on the way.** Which weeks do we hide, and from which week do we forecast?
        What does each rule forecast for them? Which rule scores best? What did the vendor score,
        and what does its fit to the past say? Which way is each rule wrong, and what does that
        cost in rupees? Does the score match the printed error table?
        """),
        code(SETUP + '''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
vendor = pd.read_csv("../data/C2_W04_D05_vendor_forecast_STUDENT.csv", parse_dates=["week_start"])
y = weekly.set_index("week_start").shipments
train, hold = y.iloc[:91], y.iloc[91:]
print(f"training weeks: {len(train)}, {train.index[0].date()} to {train.index[-1].date()}")
print(f"hold-out weeks: {len(hold)}, {hold.index[0].date()} to {hold.index[-1].date()}")
print(vendor.kind.value_counts().to_string())
check("91 training weeks and 13 hidden ones", (len(train), len(hold)) == (91, 13))
check("the vendor's hold-out rows are forecasts, never fits",
      set(vendor.set_index("week_start").loc[hold.index, "kind"]) == {"holdout"})
'''),
        md("""
        ## Which weeks do we hide, and how is the score counted?

        The plan covers eight weeks ahead, so the test hides at least as many: the last thirteen
        weeks, 29 June to 21 September 2026. Every rule forecasts all thirteen from one week, the
        week of 22 June 2026, as a planner standing there would have. The score is the **mean
        absolute error** (MAE): each week's miss in shipments, sign dropped, averaged. Three hidden
        weeks with misses of 10, 5 and 10 (invented) score 8.3.
        """),
        code('''
misses = [10, -5, 10]                          # three hidden weeks' misses (invented)
mae_toy = sum(abs(m) for m in misses) / len(misses)
print(f"MAE: {mae_toy:.1f}")
check("the toy MAE is 8.3", round(mae_toy, 1) == 8.3)
'''),
        md("""
        ## What does each rule forecast for the hidden weeks?

        Each rule in one line, all from the week of 22 June 2026. **Naive** repeats that week.
        **Drift** draws the straight line from the first week through that week and extends it.
        **The house bot** copies the week 52 weeks back (same week last year). **Finance's rule**
        is the house bot plus 4 percent. **Festival-aligned** copies the week at the same distance
        from last year's Diwali for the weeks from five before Diwali to four after, the same
        calendar week otherwise, and adds the 4 percent a year the centre grew. No hidden week lies
        within five weeks of a Diwali, so on these weeks festival-aligned and finance's rule are
        one rule.
        """),
        code('''
origin = train.index[-1]
h = pd.Series(range(1, 14), index=hold.index)
slope = (train.iloc[-1] - train.iloc[0]) / (len(train) - 1)
growth = y.iloc[52:91].sum() / y.iloc[0:39].sum() - 1
last_year = y.shift(52).loc[hold.index]
rules = pd.DataFrame({
    "naive": train.iloc[-1],
    "drift": (train.iloc[-1] + h * slope).round(),
    "house bot": last_year,
    "finance": (last_year * 1.04).round(),
    "festival-aligned": (last_year * 1.04).round(),
}).astype(int)
nearest = min(abs((d - pd.Timestamp("2026-11-02")).days) // 7 for d in hold.index)
print(f"origin {origin.date()}, drift {slope:.0f} a week, growth a year {growth:.1%}")
print(f"the hidden week nearest Diwali 2026 is {nearest} weeks before it")
print(rules.head(3).to_string())
check("the growth the training weeks show rounds to 4 percent", round(growth, 2) == 0.04)
check("no hidden week lies within five weeks of a Diwali", nearest > 5)
'''),
        md("""
        **Predict before you run.** Which rule has the lowest MAE on the thirteen hidden weeks?

        a) naive
        b) drift
        c) the house bot
        d) festival-aligned, tied with finance's rule
        """),
        code('''
def mae(f):
    return (f - hold).abs().mean()

fig, axes = plt.subplots(1, 4, figsize=(13, 3.2), sharey=True)
for ax, name in zip(axes, ["naive", "drift", "house bot", "festival-aligned"]):
    ax.plot(range(1, 14), hold.values, color="black", label="actual")
    ax.plot(range(1, 14), rules[name].values, ls="--", color="slateblue", label=name)
    ax.set_title(f"{name}: MAE {mae(rules[name]):,.0f}")
axes[0].legend()
plt.show()
scores = rules.apply(mae).round().astype(int).sort_values()
print(scores.to_string())
check("festival-aligned and finance tie", scores["festival-aligned"] == scores["finance"])
check("the house bot beats naive and drift", scores["house bot"] < min(scores["naive"], scores["drift"]))
'''),
        md("""
        **What happened.** The answer is d. Festival-aligned and finance's rule tie at 6,615
        shipments a week, the house bot scores 9,831, and naive and drift miss by 14,923 and 14,842. The bot
        beats naive because it carries the August sale and the summer dip from last year; it loses
        to the 4 percent rules because a growing series makes last year's week too low. The tie is
        honest: on weeks this far from Diwali the two rules are the same arithmetic.

        **Your turn.** Score the vendor on the same hidden weeks. Type these lines into the empty
        cell below and run it:

        ```python
        v = vendor.set_index("week_start").vendor_shipments
        print(f"vendor MAE: {mae(v.loc[hold.index]):,.0f}")
        ```
        """),
        empty(),
        md("""
        ## What does the vendor's fit to the past say about its forecast?

        **The plausible wrong answer.** "The vendor's curve sits within 2 percent of every week of
        history, so its plus 22 percent can be trusted." A fit is drawn through weeks the model has
        seen; a forecast is made for weeks it has not.
        """),
        code('''
v = vendor.set_index("week_start").vendor_shipments
fit_gap = ((v.loc[train.index] - train) / train).abs().max()
hold_gap = (v.loc[hold.index] - hold) / hold
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.bar(train.index, (v.loc[train.index] - train) / train * 100, width=5, color="plum", label="fitted")
ax.bar(hold.index, hold_gap * 100, width=5, color="crimson", label="hidden weeks")
ax.set_ylabel("vendor minus actual, percent")
ax.legend()
plt.show()
print(f"largest miss on the 91 fitted weeks: {fit_gap:.1%}")
print(f"vendor MAE on the hidden weeks: {mae(v.loc[hold.index]):,.0f}")
check("the fit stays within 2 percent", fit_gap <= 0.02)
check("the vendor's MAE is at least 30 percent above festival-aligned",
      mae(v.loc[hold.index]) >= 1.3 * scores["festival-aligned"])
'''),
        md("""
        **Why it is wrong.** The vendor never misses its fitted weeks by more than 1.4 percent, and
        it misses the hidden weeks by 16,400 a week, 148 percent worse than festival-aligned and 67
        percent worse than the house bot. The check is the one the room fixed before scoring:
        error on the weeks it never saw. The fix is to send nothing to the plan that loses to the
        house bot there.

        ## Which way is each rule wrong, and what does each direction cost?

        **Predict before you run.** Which rule's misses cost the least once a late shipment costs
        Rs 25 and an idle packer-shift Rs 650, about Rs 5.42 a shipment?

        a) festival-aligned, since its MAE is lowest
        b) the vendor
        c) the house bot
        d) naive
        """),
        code('''
rules["vendor"] = v.loc[hold.index]
over = rules.sub(hold, axis=0).clip(lower=0).sum()
under = rules.rsub(hold, axis=0).clip(lower=0).sum()
priced = pd.DataFrame({
    "MAE": rules.apply(mae).round().astype(int),
    "weeks too high": rules.gt(hold, axis=0).sum(),
    "idle Rs lakh": (over * 650 / 120 / 1e5).round(1),
    "late Rs lakh": (under * 25 / 1e5).round(1),
})
priced["cost Rs lakh"] = (over * 650 / 120 / 1e5 + under * 25 / 1e5).round(1)
print(priced.sort_values("cost Rs lakh").to_string())
priced[["late Rs lakh", "idle Rs lakh"]].sort_values("late Rs lakh").plot.barh(stacked=True,
    color=["crimson", "plum"], title="The same misses in rupees")
plt.show()
check("the vendor errs high on 12 of 13 weeks", priced.loc["vendor", "weeks too high"] == 12)
check("priced, the vendor costs less than festival-aligned",
      priced.loc["vendor", "cost Rs lakh"] < priced.loc["festival-aligned", "cost Rs lakh"])
'''),
        md("""
        **What happened.** The answer is b, and it is the uncomfortable result. The vendor's
        misses cost Rs 11.9 lakh, festival-aligned's Rs 13.5 lakh, the house bot's Rs 30.5 lakh.
        The vendor errs high on 12 of 13 weeks, and a shipment of spare capacity costs Rs 5.42
        against Rs 25 for a late one, so its bigger misses are the cheaper kind. The bot's misses
        are the dear kind: 11 of its 13 weeks are too low, which is why it costs more than naive
        while scoring a lower MAE.

        This says that erring high pays at these costs. It does not say the vendor should carry
        the plan: its high bias was never sized, it grows with the weeks ahead (3.6 percent in the
        first six weeks, 11.5 percent in the last six), and no hidden week holds a festival, where
        the vendor copies the wrong weeks. Chapter 3 raises the festival-aligned forecast by a sized
        amount instead.

        ## Does the score match the printed error table?

        A second route to the same number: print festival-aligned's thirteen misses as a table and
        average them by hand.
        """),
        code('''
table = pd.DataFrame({"actual": hold, "festival-aligned": rules["festival-aligned"]})
table["miss"] = table["festival-aligned"] - table["actual"]
print(table.to_string())
by_hand = sum(abs(m) for m in table["miss"]) / 13
print(f"MAE from the printed misses: {by_hand:,.0f}")
check("the printed table gives the same MAE", round(by_hand) == scores["festival-aligned"])
'''),
        md("""
        ## How would you answer "how do you evaluate a forecast?" in an interview?

        Hold out the latest weeks, at least as many as the plan's horizon, and forecast them from
        one origin. Fix the error measure before anyone scores, in the business's unit: shipments,
        then rupees. Compare every candidate with the naive and the seasonal copy, and send nothing
        that loses to them. Report which way the misses run, because a late shipment and an idle
        shift cost different amounts. The trap the interviewer fishes for is judging by the fit.
        """),
        md("""
        ## What did chapter 2 answer?

        - **Which weeks are hidden?** The last thirteen, 29 June to 21 September 2026, forecast
          from the week of 22 June 2026.
        - **Which rule scores best?** Festival-aligned and finance's rule, tied at 6,615 a week;
          the house bot 9,831; naive 14,923; drift 14,842.
        - **What did the vendor score?** 16,400, after fitting history within 1.4 percent: fit is
          not forecast.
        - **Which way is each wrong, and at what cost?** The vendor errs high on 12 of 13 weeks and
          costs Rs 11.9 lakh; festival-aligned Rs 13.5 lakh; the bot errs low and costs Rs 30.5
          lakh.
        - **Does the table agree?** Yes, 6,615 from the printed misses.

        Chapter 3 asks what the hold-out cannot: where the festival falls this year, and how far
        above the forecast the plan should sit.
        """),
    ]


def nb03():
    return [
        md(f"""
        # Which forecast goes to the plan, how many packer shifts a week, and what does a miss cost?

        **Week 4, Friday, chapter 3 of 3.** {TICKET}

        Chapter 2 scored every rule on thirteen hidden summer weeks: festival-aligned and finance's
        rule tied at 6,615 a week, the house bot scored 9,831, the vendor 16,400. None of those
        weeks held a festival, so the hold-out could not test the one thing the plan depends on.

        **Who needs the answer.** The FC planner, who books the shifts, and the regional operations
        head, who answers for late parcels in the festival's busiest weeks. A plan that puts the
        peak in the wrong week pays for idle packers and late shipments in the same month.

        **The questions on the way.** How did each rule do on 2025's festival? Which week does each
        forecast put this year's peak in? How do the four forecasts compare with last year's two
        windows? How far above the forecast should the plan sit? How many shifts a week? What would
        the other plans cost?
        """),
        code(SETUP + '''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
vendor = pd.read_csv("../data/C2_W04_D05_vendor_forecast_STUDENT.csv", parse_dates=["week_start"])
y = weekly.set_index("week_start").shipments
v = vendor.set_index("week_start").vendor_shipments
diwali = {2024: pd.Timestamp("2024-10-28"), 2025: pd.Timestamp("2025-10-20"), 2026: pd.Timestamp("2026-11-02")}

def aligned_source(d):
    """The week festival-aligned copies: the same distance from last year's Diwali near the festival."""
    near = min(diwali.values(), key=lambda w: abs((d - w).days))
    gap = (d - near).days // 7
    if -5 <= gap <= 4 and near.year - 1 in diwali:
        return diwali[near.year - 1] + pd.Timedelta(weeks=gap)
    return d - pd.Timedelta(weeks=52)

print(aligned_source(pd.Timestamp("2026-10-19")).date(), "is the source for the week of 19 Oct 2026")
check("the week of 19 Oct 2026 copies 6 Oct 2025", aligned_source(pd.Timestamp("2026-10-19")) == pd.Timestamp("2025-10-06"))
'''),
        md("""
        ## How did each rule do on 2025's festival?

        The only festival the data can test the rules on is 2025's. Stand in the week of 22
        September 2025 and forecast the eight weeks from 29 September to 17 November 2025.

        **Predict before you run.** By how many weeks does the house bot miss 2025's peak?

        a) none: same week last year knows the season
        b) one week late
        c) one week early
        d) two weeks late
        """),
        code('''
weeks25 = pd.date_range("2025-09-29", periods=8, freq="7D")
back = pd.DataFrame({
    "actual": y.loc[weeks25],
    "house bot": [y[d - pd.Timedelta(weeks=52)] for d in weeks25],
    "festival-aligned": [round(y[aligned_source(d)] * 1.04) for d in weeks25],
}, index=weeks25)
back.plot(marker="o", title="2025's festival, forecast from the week of 22 Sep 2025")
plt.show()
for rule in ["house bot", "festival-aligned"]:
    over = (back[rule] - back.actual).clip(lower=0).sum()
    under = (back.actual - back[rule]).clip(lower=0).sum()
    print(f"{rule:17s} MAE {(back[rule] - back.actual).abs().mean():>7,.0f}   cost Rs {(over * 650 / 120 + under * 25) / 1e5:.1f} lakh")
check("the bot's peak is 13 Oct 2025, a week late", back["house bot"].idxmax() == pd.Timestamp("2025-10-13"))
check("festival-aligned peaks on 6 Oct 2025 with the actual", back["festival-aligned"].idxmax() == back.actual.idxmax())
'''),
        md("""
        **What happened.** The answer is b. The house bot put 2024's peak on 13 October 2025, a
        week late: MAE 58,250 and Rs 79.8 lakh of misses, mostly late shipments in the week the
        real peak came. Festival-aligned missed by 4,034 a week and Rs 4.6 lakh. One festival is a
        thin test, so the plan treats this as evidence about placement, never as a precise error.

        ## Which week does each forecast put this year's peak in?

        Diwali 2026 falls on Sunday 8 November, so its week begins 2 November and the peak should
        come two weeks before, on the week of 19 October.

        **Predict before you run.** Which week does the house bot's copy of 2025 make the busiest
        week of the festive season?

        a) 5 October 2026
        b) 19 October 2026
        c) 26 October 2026
        d) 2 November 2026
        """),
        code('''
weeks26 = pd.date_range("2026-09-28", periods=10, freq="7D")
ahead = pd.DataFrame({
    "house bot": [y[d - pd.Timedelta(weeks=52)] for d in weeks26],
    "finance": [round(y[d - pd.Timedelta(weeks=52)] * 1.04) for d in weeks26],
    "vendor": v.loc[weeks26].values,
    "festival-aligned": [round(y[aligned_source(d)] * 1.04) for d in weeks26],
}, index=weeks26)
ahead.plot(marker="o", title="Four forecasts, 28 Sep to 30 Nov 2026")
plt.show()
print(ahead.idxmax().dt.date.to_string())
check("the bot's busiest week is 5 Oct 2026", ahead["house bot"].idxmax() == pd.Timestamp("2026-10-05"))
check("festival-aligned's busiest week is 19 Oct 2026", ahead["festival-aligned"].idxmax() == pd.Timestamp("2026-10-19"))
'''),
        md("""
        **What happened.** The answer is a. The house bot, finance's rule and the vendor all make 5
        October 2026 the busiest week, because each copies 2025's calendar weeks; festival-aligned
        puts it on 19 October, two weeks before Diwali's week. The vendor's model never knew the
        festival moved.

        ## How do the four forecasts compare with last year's window?

        "Last year's window" has two readings. The same calendar weeks, 13 October to 1 December
        2025, hold only the tail of 2025's festival. The same weeks counted from Diwali, 29
        September to 17 November 2025, hold all of it.
        """),
        code('''
window = weeks26[2:]                                    # 12 Oct to 30 Nov 2026
calendar_2025 = y.loc[window - pd.Timedelta(weeks=52)].sum()
festival_2025 = y.loc[[aligned_source(d) for d in window]].sum()
totals = ahead.loc[window].sum()
compare = pd.DataFrame({"eight weeks": totals.map("{:,}".format),
                        "vs same calendar weeks": (totals / calendar_2025 - 1).map("{:+.1%}".format),
                        "vs same weeks from Diwali": (totals / festival_2025 - 1).map("{:+.1%}".format)})
print(f"2025, same calendar weeks: {calendar_2025:,}   2025, same weeks from Diwali: {festival_2025:,}")
print(compare.to_string())
check("finance is plus 4 percent on the calendar window", round(totals["finance"] / calendar_2025 - 1, 3) == 0.04)
check("the vendor is plus 22 percent on the calendar window", round(totals["vendor"] / calendar_2025 - 1, 3) == 0.22)
check("finance sits below festival-aligned", totals["finance"] < totals["festival-aligned"])
'''),
        md("""
        **What happened.** Against the calendar weeks, festival-aligned reads 19.5 percent above
        last year, close to the vendor's 22.0, because 2026's peak weeks fall inside the window and
        2025's fell before it. Against the weeks counted from Diwali it reads 4.0 percent. Finance's
        plus 4 is plus 4 only on the calendar window: it is 9.5 percent below last year's festival
        weeks and 308,048 shipments below festival-aligned, and short is the costly side. The
        vendor's total sits 2.1 percent above festival-aligned, with its busiest week on 5 October.

        ## How far above the forecast should the plan sit?

        A shipment planned and not shipped costs Rs 650 / 120 = Rs 5.42 of idle shift; a shipment
        short costs Rs 25. The plan should cover demand in the share of weeks that balances the two:
        25 / (25 + 5.42), about 0.82. Read that share off the forecast's own misses on the hidden
        weeks of chapter 2.
        """),
        code('''
hold = y.iloc[91:]
fa_hold = (y.shift(52).loc[hold.index] * 1.04).round()
misses = (hold - fa_hold) / fa_hold                     # positive: demand above the forecast
q = 25 / (25 + 650 / 120)
cushion = round(misses.quantile(q), 3)                  # rounded to a tenth of a percent
print(f"plan share {q:.2f}: demand beat the forecast by more than {cushion:.1%} in {1 - q:.0%} of the hidden weeks")
grid = [i / 1000 for i in range(-80, 101, 2)]
base = ahead.loc["2026-10-19", "festival-aligned"]
cost = [sum(650 / 120 * max(0, base * (1 + g) - base * (1 + m)) + 25 * max(0, base * (1 + m) - base * (1 + g))
            for m in misses) / 13 / 1e5 for g in grid]
plt.plot([g * 100 for g in grid], cost)
plt.axvline(cushion * 100, ls="--", color="slateblue")
plt.xlabel("plan above the forecast, percent (week of 19 Oct 2026)")
plt.ylabel("expected cost, Rs lakh")
plt.show()
check("the plan share is about 0.82", round(q, 2) == 0.82)
check("the cheapest level sits above the forecast", grid[cost.index(min(cost))] > 0)
'''),
        md("""
        ## How many packer shifts does each week need?

        The plan raises each week of the festival-aligned forecast by the 2.6 percent cushion, then
        divides by 120 shipments a shift and rounds up.
        """),
        code('''
plan = (ahead.loc[window, "festival-aligned"] * (1 + cushion)).round()
shifts = (plan / 120).apply(math.ceil)
staffing = pd.DataFrame({"forecast": ahead.loc[window, "festival-aligned"], "plan": plan.astype(int),
                         "packer shifts": shifts})
print(staffing.to_string())
print(f"total: {shifts.sum():,} packer shifts over eight weeks")
staffing["packer shifts"].plot.bar(color="lavender", edgecolor="slateblue", title="Packer shifts a week")
plt.show()
check("the busiest week of the plan is 19 Oct 2026", staffing["packer shifts"].idxmax() == pd.Timestamp("2026-10-19"))
'''),
        md("""
        ## What would the other plans cost if demand follows the festival-aligned forecast?

        A scenario, never a measurement: price each plan against festival-aligned's weeks, Rs 5.42
        for every shipment of spare capacity and Rs 25 for every shipment short.
        """),
        code('''
expected = ahead.loc[window, "festival-aligned"]
plans = ahead.loc[window, ["house bot", "finance", "vendor"]].assign(plan=plan)
over = plans.sub(expected, axis=0).clip(lower=0).sum()
under = plans.rsub(expected, axis=0).clip(lower=0).sum()
print(((over * 650 / 120 + under * 25) / 1e5).round(1).to_string())
check("the plan costs least in this scenario",
      ((over * 650 / 120 + under * 25)).idxmin() == "plan")
'''),
        md("""
        **What happened.** If demand follows festival-aligned, the house bot's weeks cost Rs 111.6
        lakh, finance's Rs 103.6 lakh and the vendor's Rs 82.2 lakh, mostly late shipments in the
        weeks of 19 October to 2 November. The plan's cushion costs Rs 3.3 lakh of spare shifts if
        demand lands exactly on the forecast, which is what the insurance costs.

        ## What can two years of weeks not tell us?

        - **The festival moves, and the sale moves with it.** Checked on one festival only: the 2025
          back-test.
        - **One spike a year is two spikes in two years.** No check inside the data closes it.
        - **The hold-out holds no festive week,** so its 6,615 is an ordinary-week error; the 2025
          festival gave 4,034 on one festival.
        - **Capacity clips the peak.** Overtime shifts reached 1,638 in the week of 6 October 2025
          against 5 in an ordinary November week, so peak demand may have been higher than shipped.
        - **The 4 percent growth** is two years' evidence; a third year could move it.
        - **A vendor model with no Lucknow festival in its forecast record** is an assumption, like
          a forecast with no history behind it.

        ## The same method at an AI company: how much inference capacity does a launch need?

        A product launch is the festival: a known date, a spike, little history. Hide as many days
        as the plan covers, score in requests a minute, compare with last launch's shape, and set
        capacity above the median because a timeout costs more than an idle server.

        ## What did chapter 3 answer?

        - **2025's festival:** the house bot landed the peak a week late (Rs 79.8 lakh of misses);
          festival-aligned missed by Rs 4.6 lakh.
        - **This year's peak:** the house bot, finance and the vendor put it on 5 October 2026;
          festival-aligned on 19 October.
        - **Last year's windows:** festival-aligned is 19.5 percent above the calendar weeks and 4.0
          percent above the weeks from Diwali; finance is 9.5 percent below the festival weeks.
        - **How far above:** the 0.82 share, a 2.6 percent cushion.
        - **Shifts:** 20,275 over eight weeks, 3,719 in the week of 19 October.
        - **The others' cost:** Rs 82.2 to 111.6 lakh if demand follows festival-aligned; the
          cushion Rs 3.3 lakh.
        """),
    ]


def nb04():
    return [
        md("""
        # Which revenue forecast should Anand put in front of Kalpa's board, and how wrong could it be?

        **Week 4, Friday, the TA lab: the same method on Kalpa Retail.** Kalpa Retail's growth plan
        goes to the board and needs a number: revenue for October 2026 to March 2027, against a
        plan line 15 percent above the same months a year earlier, with Diwali inside the window.
        Finance's forecast is last year plus 4 percent; marketing's vendor curve promises 22
        percent. Anand Iyer, the finance controller: "Two forecasts, eighteen points apart. Which
        one do I put in front of the board, and how wrong could it be?" The data hold 24 months of
        revenue, October 2024 to September 2026; April to September 2026 are the monthly sums of
        the 1,000 orders in the Week 2 warehouse. Diwali fell on 31 October 2024 and 20 October
        2025, and falls on 8 November 2026.

        **Who needs the answer.** Anand, who signs the board number, and the head of Retail-Plus,
        whose stock and staff follow it. A number the board holds Kalpa to for two quarters costs
        either a missed promise or idle stock.

        **The questions on the way.** What shape do the two winters have? How do naive and drift
        score on April to September 2026? How do the seasonal copy and the vendor score? Which month
        does each copy put Diwali in this year?
        """),
        code(SETUP + '''
rev = pd.read_csv("../data/C2_W04_D05_kalpa_monthly_revenue_STUDENT.csv").set_index("month").revenue_rs
vendor = pd.read_csv("../data/C2_W04_D05_kalpa_vendor_forecast_STUDENT.csv").set_index("month")
plan = pd.read_csv("../data/C2_W04_D05_kalpa_plan_line_STUDENT.csv").set_index("month").plan_rs
print(f"{len(rev)} months, {rev.index[0]} to {rev.index[-1]}")
print(f"Apr to Jun 2026: Rs {rev['2026-04':'2026-06'].sum() / 1e7:.2f} crore; Jul to Sep: Rs {rev['2026-07':'2026-09'].sum() / 1e7:.2f} crore")
check("24 months", len(rev) == 24)
check("the two quarters match the warehouse", (rev['2026-04':'2026-06'].sum(), rev['2026-07':'2026-09'].sum()) == (100_000_000, 98_400_000))
'''),
        md("""
        ## What shape do the two winters have?

        Twelve rows: October to March of 2024-25 and of 2025-26, in Rs lakh.

        **Predict before you run.** Which month is the biggest of each winter?
        """),
        code('''
winters = pd.DataFrame({"2024-25": rev["2024-10":"2025-03"].values, "2025-26": rev["2025-10":"2026-03"].values},
                       index=["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]) / 1e5
print(winters.round(1).to_string())
(rev / 1e5).plot(marker="o", title="Kalpa Retail revenue, Rs lakh a month", figsize=(10, 3.6))
plt.show()
check("October is each winter's biggest month", list(winters.idxmax()) == ["Oct", "Oct"])
'''),
        md("""
        ## How do naive and drift score on April to September 2026?

        Hide the last six months and forecast them from March 2026. Naive repeats March; drift
        extends the line from October 2024 through March 2026. The score is MAE in Rs lakh.
        """),
        code('''
hold = rev["2026-04":"2026-09"]
months_ahead = pd.Series(range(1, 7), index=hold.index)
naive = pd.Series(rev["2026-03"], index=hold.index)
drift = rev["2026-03"] + months_ahead * (rev["2026-03"] - rev["2024-10"]) / 17

def mae(f):
    return (f - hold).abs().mean() / 1e5

print(f"naive MAE: Rs {mae(naive):.1f} lakh   drift MAE: Rs {mae(drift):.1f} lakh")
pd.DataFrame({"actual": hold, "naive": naive, "drift": drift}).div(1e5).plot(marker="o", title="Six hidden months, Rs lakh")
plt.show()
check("naive misses by more than Rs 50 lakh a month", mae(naive) > 50)
'''),
        md("""
        **Your turn.** Score the seasonal copy (the same month a year earlier) and the vendor's
        forecast on the same six months. Type these lines into the empty cell below and run them:

        ```python
        seasonal = rev.shift(12).loc[hold.index]
        vendor_hold = vendor.loc[hold.index, "vendor_rs"]
        print(vendor.loc[hold.index, "kind"].unique())
        print(f"seasonal MAE: Rs {mae(seasonal):.1f} lakh   vendor MAE: Rs {mae(vendor_hold):.1f} lakh")
        ```
        """),
        empty(),
        md("""
        ## Which month does each copy put Diwali in this year?

        Diwali 2026 falls on 8 November. The month-aligned copy takes each month from the same month
        last year; the festival-aligned copy moves last year's Diwali month to this year's and puts
        last year's November in October's place, then adds 4 percent.

        **Your turn.** Type these lines into the empty cell below:

        ```python
        months = ["2026-10", "2026-11", "2026-12", "2027-01", "2027-02", "2027-03"]
        last = [rev[f"{int(m[:4]) - 1}{m[4:]}"] for m in months]
        aligned = [rev["2025-11"], rev["2025-10"]] + last[2:]
        table = pd.DataFrame({"month-aligned": last, "festival-aligned": [round(a * 1.04) for a in aligned],
                              "vendor": vendor.loc[months, "vendor_rs"].values, "plan line": plan.loc[months].values},
                             index=months) / 1e5
        print(table.round(1).to_string())
        print(table.sum().round(1).to_string())
        ```
        """),
        empty(),
        code('''
growth = rev["2025-10":"2026-09"].sum() / rev["2024-10":"2025-09"].sum() - 1
print(f"the second year grew {growth:.1%} on the first")
print(f"plan line, Oct 2026 to Mar 2027: Rs {plan.sum() / 1e7:.2f} crore")
(plan / 1e5).plot.bar(color="lavender", edgecolor="slateblue", title="The plan line, Rs lakh a month")
plt.show()
check("the plan line is 15 percent above last year's same months",
      abs(plan.sum() / rev["2025-10":"2026-03"].sum() - 1.15) < 0.001)
'''),
        md("""
        ## What do you bring to the TA?

        Anand's board number in one paragraph: the forecast you would send, the months it puts the
        spike in, its error bar in Rs lakh from the six hidden months, and the gap to the plan line.
        The unguided exercise `exercises/unguided/C2_W04_D05_kalpa_board_STUDENT.md` asks the same
        decision in lettered items.

        - **The two winters:** October is the biggest month of each.
        - **Naive and drift:** they miss April to September 2026 by Rs 59.4 and Rs 58.8 lakh a month.
        - **The seasonal copy and the vendor:** your cell.
        - **Diwali this year:** your cell.
        """),
    ]


if __name__ == "__main__":
    for name, cells in [("01_twelve_rows", nb01()), ("02_holdout_scoreboard", nb02()),
                        ("03_festive_plan", nb03()), ("04_kalpa_lab", nb04())]:
        path = NB / f"C2_W04_D05_{name}_STUDENT.ipynb"
        build(path, cells)
        print("built", path.name, len(cells), "cells")

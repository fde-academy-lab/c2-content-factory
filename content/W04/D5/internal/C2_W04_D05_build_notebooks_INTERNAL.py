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
TICKET = f"""**The ticket.** Flipkart, the Lucknow fulfilment centre (FC), the warehouse where orders are packed
and shipped. The centre has 104 weeks of outbound shipments, the weeks beginning Monday 30 September
2024 to Monday 21 September 2026. Diwali fell on Thursday 31 October 2024 and Monday 20 October 2025,
and falls on Sunday 8 November 2026; the festive sale runs in the third and second weeks before
Diwali's week. A packer packs about 120 shipments a shift, and a packer-shift is one packer working
one shift. The planner must book packer shifts for the eight weeks beginning 12 October to 30
November 2026, the festive window. A vendor's demand model promises the window 22 percent above the
same weeks last year; finance's rule is those weeks plus 4 percent: eighteen percentage points apart.
A late shipment costs Rs 25 (assumed, Rs 15 to 40). A spare shipment, planned for and never shipped,
leaves part of a packer-shift idle: Rs 650 a shift (assumed, Rs 500 to 800) over 120 shipments, Rs
5.42 a shipment. {LABEL}"""

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
        Diwali 2025's own week? Which week does the copy of last year put the peak in? How far does
        Diwali's week move into 2026? Does the full series show the same shape?
        """),
        code(SETUP + '''
rows = pd.read_csv("../data/C2_W04_D05_twelve_rows_STUDENT.csv", parse_dates=["week_start"])
s = rows.set_index("week_start").shipments          # shipments, looked up by the week's Monday
rows
'''),
        md("""
        ## What does a forecast copy from the past, on numbers you can hold in your head?

        A canteen sold 50, 52, 49 and 51 cups of tea on four days (invented). The simplest forecast,
        **naive**, says tomorrow repeats the last day: 51. **Drift** draws the line from the first
        day to the last and extends it one step: 51 plus the average daily change, (51 - 50) / 3,
        about 51.3. If Sundays always sell about 80, the forecast for next Sunday copies last
        Sunday: a **seasonal copy**, the same point one season back. For weekly shipments the season
        is a year, so the seasonal copy is **the same week last year**, and the tournament calls it
        **the house bot**: three names for one rule.
        """),
        code('''
cups = [50, 52, 49, 51]                      # four days at a canteen (invented)
print("naive forecast for tomorrow:", cups[-1])
drift = cups[-1] + (cups[-1] - cups[0]) / (len(cups) - 1)    # the last value plus the average step
print(f"drift forecast for tomorrow: {drift:.1f}")
last_sunday = 80                             # last Sunday's cups (invented)
print("seasonal copy for next Sunday:", last_sunday)
check("naive repeats the last value", cups[-1] == 51)
check("drift adds the average step to the last value", round(drift, 1) == 51.3)
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
peaks = []
for year in [2024, 2025]:
    one_year = rows[rows.week_start.dt.year == year]          # that year's six rows
    top = one_year.loc[one_year.shipments.idxmax()]           # the row with the most shipments
    print(year, "busiest week:", top.week_start.date(), f"{top.shipments:,} shipments")
    peaks.append(top.week_start)
check("both peaks sit two weeks before Diwali's week", peaks == list(pd.to_datetime(["2024-10-14", "2025-10-06"])))
'''),
        md("""
        **What happened.** The answer is c. The busiest week is two weeks before Diwali's week in
        both years: 401,000 shipments in the week of 14 October 2024 and 418,200 in the week of 6
        October 2025. Both fall in the festive sale, which runs in the third and second weeks before
        Diwali's week, and parcels leave the centre with the sale so they arrive before the
        festival. Diwali's own week ships less (296,900 and 308,900), and the week after falls
        lowest.

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
actual = s[pd.Timestamp("2025-10-20")]                    # Diwali 2025's own week
naive = s[pd.Timestamp("2025-10-13")]                     # the week before
same_week = s[pd.Timestamp("2024-10-21")]                 # 52 weeks back
aligned = round(s[pd.Timestamp("2024-10-28")] * 1.04)     # Diwali 2024's own week, plus 4 percent
for name, forecast in [("naive", naive), ("same week last year", same_week), ("festival-aligned", aligned)]:
    print(f"{name}: forecast {forecast:,}, miss {forecast - actual:+,}")
check("festival-aligned lands closest",
      abs(aligned - actual) < min(abs(naive - actual), abs(same_week - actual)))
'''),
        md("""
        **What happened.** The answer is c. Naive misses by 60,100 and same week last year by
        47,300, both too high; festival-aligned misses by 124. A miss here is the forecast minus
        what shipped, so a positive miss is too high. The week 52 weeks back looks like "the same
        week", but in 2024 it was the week before Diwali, and the week before Diwali ships more than
        Diwali's own week.

        ## Which week does a copy of last year put the peak in?

        **The plausible wrong answer.** "Same week last year already knows the season, so it is the
        safe rule for a festival." Copy every 2025 week from 52 weeks back and see where its peak
        lands. Beside it, festival-aligned reaches back 51 weeks, because Diwali 2025's week came 51
        weeks after Diwali 2024's.
        """),
        code('''
y25 = s[s.index.year == 2025]                             # the six 2025 rows
copy52, copy51 = {}, {}
for d in y25.index:
    copy52[d] = s.get(d - pd.Timedelta(weeks=52))           # blank when that week is not in the twelve rows
    copy51[d] = round(s[d - pd.Timedelta(weeks=51)] * 1.04)  # the week at the same distance from Diwali
table = pd.DataFrame({"actual": y25, "same week last year": pd.Series(copy52).astype("Int64"),
                      "festival-aligned": pd.Series(copy51)})
print(table.to_string())
ax = table.astype(float).plot(marker="o", title="2025's festive weeks against two copies of 2024")
ax.set_xlabel("week beginning")
plt.show()
check("the copy of last year peaks on 13 Oct 2025", table["same week last year"].idxmax() == pd.Timestamp("2025-10-13"))
check("the actual peak is 6 Oct 2025", y25.idxmax() == pd.Timestamp("2025-10-06"))
'''),
        md("""
        **Why it is wrong.** Diwali's week came one week earlier in 2025, so the copy of the same
        calendar week put 2024's peak (401,000) on 13 October 2025, a week late, and left the real
        peak week short. The check that catches it is the calendar: line up each year's weeks by
        their distance from Diwali before copying. The week of 29 September 2025 shows a blank in
        the copy, because its source, 30 September 2024, is not one of the twelve rows.

        ## How far does Diwali's week move between 2025 and 2026?

        Diwali 2026 falls on Sunday 8 November, so its week begins Monday 2 November 2026. Count the
        weeks from Diwali 2025's week, and set them beside the 52 weeks a copy of last year steps
        back. Where that puts this year's rush is chapter 3's question, so hold your answer.
        """),
        code('''
diwali_2025, diwali_2026 = pd.Timestamp("2025-10-20"), pd.Timestamp("2026-11-02")
gap = (diwali_2026 - diwali_2025).days // 7                # weeks from one Diwali week to the next
print("weeks from Diwali 2025's week to Diwali 2026's:", gap)
print("weeks a copy of last year steps back: 52")
check("Diwali's week moves 54 weeks on, more than a year of weeks", gap == 54)
'''),
        md("""
        ## Does the full series show the same shape?

        The twelve rows came from 104 weeks. The ticket's `calendar` table flags each week that
        holds Diwali and each sale week, so the full series can be read against both.
        """),
        code('''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
calendar = pd.read_csv("../data/C2_W04_D05_calendar_STUDENT.csv", parse_dates=["week_start"])
sale = calendar.loc[calendar.sale_week == 1, "week_start"]          # every sale week the calendar flags
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.plot(weekly.week_start, weekly.shipments, color="slateblue")
for d in diwali:
    ax.axvline(d, color="crimson", ls="--")
for d in sale[sale <= weekly.week_start.max()]:
    ax.axvspan(d, d + pd.Timedelta(days=7), color="gold", alpha=0.4)
ax.set_title("104 weeks of outbound shipments; dashed: Diwali's week; gold: sale weeks")
plt.show()
festive_sale = [d for d in sale if d.month in (9, 10)]               # the festive sale, without August's
expected = []
for w in calendar.loc[calendar.diwali_week == 1, "week_start"]:
    expected += [w - pd.Timedelta(weeks=3), w - pd.Timedelta(weeks=2)]
print("festive sale weeks:", [str(d.date()) for d in festive_sale])
check("104 weeks", len(weekly) == 104)
check("the twelve rows are rows of the full series",
      rows.merge(weekly, on=["week_start", "shipments"]).shape[0] == 12)
check("each festive sale runs three and two weeks before Diwali's week", sorted(expected) == sorted(festive_sale))
'''),
        md("""
        ## What did chapter 1 answer?

        - **What does a forecast copy?** The last value (naive), the line through the values
          (drift) or the same point one season back (the seasonal copy): 51, about 51.3 and 80 on
          invented numbers.
        - **Where is the peak?** Two weeks before Diwali's week in both years, in the sale weeks:
          401,000 and 418,200.
        - **What do three rules say for 20 October 2025?** Naive 369,000, same week last year
          356,200, festival-aligned 308,776 against 308,900 shipped.
        - **Where does a copy of last year put the peak?** A week late in 2025. In 2026 Diwali's
          week comes 54 weeks after 2025's, where a copy steps back 52; chapter 3 asks what that
          does to this year's rush.
        - **Does the full series agree?** Yes: two festive peaks in the sale weeks, an August sale,
          ordinary weeks a little above 210,000.

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
        calendar week lands it a week late in 2025. This notebook scores every rule, and the
        vendor's curve, on weeks none of them saw.

        **Who needs the answer.** The FC planner, who may send only a forecast that has beaten the
        house bot on weeks it never saw, and the regional operations head, who must say yes or no
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
split = 91                                    # the row of the first hidden week, 29 Jun 2026
train, hold = y.iloc[:split], y.iloc[split:]  # the weeks the rules may see, and the weeks they forecast
print(f"training weeks: {len(train)}, {train.index[0].date()} to {train.index[-1].date()}")
print(f"hidden weeks: {len(hold)}, {hold.index[0].date()} to {hold.index[-1].date()}")
print(vendor.kind.value_counts().to_string())
check("the hidden weeks are the latest ones", hold.index[-1] == y.index[-1])
check("no week is lost or counted twice", len(train) + len(hold) == len(y))
check("the vendor's rows for the hidden weeks are forecasts made from 22 June, never fits",
      set(vendor.set_index("week_start").loc[hold.index, "kind"]) == {"holdout"})
'''),
        md("""
        ## Which weeks do we hide, and how is the score counted?

        The plan books eight weeks ahead; that reach is the **horizon**. The test hides at least as
        many weeks at the end of the data: the last thirteen, 29 June to 21 September 2026, the
        **hidden weeks** (also called the hold-out, or the test set). The rules may see only the 91
        **training weeks** before them, and every rule forecasts all thirteen from the last of
        those, the week of 22 June 2026, called the **origin**. The vendor's file labels its rows
        three ways: **fitted** rows are its answers for weeks it was built on, **holdout** rows its
        forecasts for the hidden weeks, made from 22 June, and **forecast** rows the weeks ahead.

        The score is the **mean absolute error** (MAE): each week's miss in shipments, sign dropped,
        averaged. Its cousin, the **mean absolute percentage error** (MAPE), averages each miss as a
        percent of what shipped: it compares centres of different sizes, and it divides by the
        actual, so a week that ships almost nothing makes it explode. Three hidden weeks with misses
        of 10, 5 and 10 (invented) score an MAE of 8.3.
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
        **The house bot** copies the week 52 weeks back. **Finance's rule** is the house bot plus 4
        percent. **Festival-aligned**, from five weeks before Diwali's week to four after, copies
        the week at the same distance from last year's Diwali; on every other week it copies the
        same calendar week; then it adds the 4 percent a year the centre grew. No hidden week falls
        in that stretch around a Diwali, so on these weeks festival-aligned and finance's rule are
        one rule.

        Two pieces of code are new. `y.shift(52)` slides the whole series down 52 rows, so each
        week's row holds the value from 52 weeks earlier. `h` counts the weeks ahead of the origin,
        1 to 13. The growth line compares the latest 39 training weeks, 29 September 2025 to 22
        June 2026, with the same 39 weeks a year earlier.
        """),
        code('''
origin = train.index[-1]                                         # the last week the rules may see
h = pd.Series(range(1, len(hold) + 1), index=hold.index)         # weeks ahead: 1, 2, 3 and so on
slope = (train.iloc[-1] - train.iloc[0]) / (len(train) - 1)       # drift: the average change a week
growth = y.iloc[52:split].sum() / y.iloc[0:split - 52].sum() - 1  # a year's growth on the same weeks
factor = round(1 + growth, 2)                                     # 1.04, the same 4 percent finance uses
last_year = y.shift(52).loc[hold.index]                           # each hidden week's same week last year
rules = pd.DataFrame({
    "naive": train.iloc[-1],
    "drift": (train.iloc[-1] + h * slope).round(),
    "house bot": last_year,
    "finance": (last_year * 1.04).round(),
    "festival-aligned": (last_year * factor).round(),
}).astype(int)
nearest = min(abs((d - pd.Timestamp("2026-11-02")).days) // 7 for d in hold.index)
print(f"origin {origin.date()}, drift {slope:.0f} a week, growth a year {growth:.1%}")
print(f"the hidden week nearest Diwali 2026 is {nearest} weeks before it")
print(rules.head(3).to_string())
check("the growth the training weeks show rounds to 4 percent", factor == 1.04)
check("no hidden week falls in the stretch around a Diwali", nearest > 5)
'''),
        md("""
        **Predict before you run.** Which rule has the lowest MAE on the thirteen hidden weeks?

        a) naive
        b) drift
        c) the house bot
        d) festival-aligned, tied with finance's rule
        """),
        code('''
scores = pd.Series({name: (rules[name] - hold).abs().mean()     # each rule's misses, signs dropped, averaged
                    for name in rules.columns}).round().astype(int).sort_values()
weeks_ahead = range(1, len(hold) + 1)
fig, axes = plt.subplots(1, 4, figsize=(13, 3.2), sharey=True)
for ax, name in zip(axes, ["naive", "drift", "house bot", "festival-aligned"]):
    ax.plot(weeks_ahead, hold.values, color="black", label="actual")
    ax.plot(weeks_ahead, rules[name].values, ls="--", color="slateblue", label=name)
    ax.set_title(f"{name}: MAE {scores[name]:,}")
axes[0].legend()
plt.show()
print(scores.to_string())
check("festival-aligned and finance tie", scores["festival-aligned"] == scores["finance"])
check("the house bot beats naive and drift", scores["house bot"] < min(scores["naive"], scores["drift"]))
'''),
        md("""
        **What happened.** The answer is d. Festival-aligned and finance's rule tie at 6,615
        shipments a week, the house bot scores 9,831, and naive and drift miss by 14,923 and
        14,842. The house bot beats naive because it carries the August sale and the summer dip
        from last year; it loses to the 4 percent rules because a growing series makes last year's
        week too low. The tie is honest: on weeks this far from Diwali the two rules are the same
        arithmetic.

        **Predict before you run.** The vendor's sponsor says the curve sits within 2 percent of
        every past week. On the thirteen hidden weeks, how does it score against the house bot's
        9,831?

        a) far below the bot, since it fits the past best
        b) about the same as the bot
        c) above the bot: it misses by more

        **Your turn.** Score the vendor on the same hidden weeks. Type these lines into the empty
        cell below and run it:

        ```python
        v = vendor.set_index("week_start").vendor_shipments
        print(f"vendor MAE: {(v.loc[hold.index] - hold).abs().mean():,.0f}")
        ```
        """),
        empty(),
        md("""
        ## What does the vendor's fit to the past say about its forecast?

        **The plausible wrong answer.** The vendor's sponsor, the manager who brought the model in,
        says: "The curve sits within 2 percent of every week of history, so its plus 22 percent can
        be trusted." A fit is drawn through weeks the model has seen; a forecast is made for weeks
        it has not. Within 2 percent is the sponsor's claim; the cell below measures the worst
        fitted week.
        """),
        code('''
v = vendor.set_index("week_start").vendor_shipments
fitted = vendor[vendor.kind == "fitted"].set_index("week_start").vendor_shipments
fit_gap = ((fitted - y.loc[fitted.index]) / y.loc[fitted.index]).abs().max()   # the worst fitted week
hold_gap = (v.loc[hold.index] - hold) / hold                                    # each hidden week, as a share
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.bar(fitted.index, (fitted - y.loc[fitted.index]) / y.loc[fitted.index] * 100, width=5, color="plum", label="fitted")
ax.bar(hold.index, hold_gap * 100, width=5, color="crimson", label="hidden weeks")
ax.set_ylabel("vendor minus actual, percent")
ax.legend()
plt.show()
print(f"largest miss on the {len(fitted)} fitted weeks: {fit_gap:.1%}")
vendor_mae = (v.loc[hold.index] - hold).abs().mean()                            # the same measure as the rules
print(f"vendor MAE on the hidden weeks: {vendor_mae:,.0f}")
print(f"too high by {hold_gap.iloc[:6].mean():.1%} on average in hidden weeks 1 to 6, "
      f"{hold_gap.iloc[-6:].mean():.1%} in weeks 8 to 13")
check("the fit stays within 2 percent", fit_gap <= 0.02)
check("the vendor's MAE is at least 30 percent above festival-aligned",
      vendor_mae >= 1.3 * scores["festival-aligned"])
'''),
        md("""
        **Why it is wrong.** The answer is c. The vendor never misses its fitted weeks by more than 1.4 percent, and
        it misses the hidden weeks by 16,400 a week, 148 percent worse than festival-aligned and 67
        percent worse than the house bot. The check is the one the room fixed before scoring: error
        on the weeks it never saw. The fix is to send nothing to the plan that loses to the house
        bot there.

        ## Which way is each rule wrong, and what does each direction cost?

        **Predict before you run.** Which rule's misses cost the least once a late shipment costs
        Rs 25 and a spare shipment Rs 5.42?

        a) festival-aligned, since its MAE is lowest
        b) the vendor
        c) the house bot
        d) naive
        """),
        code('''
rules["vendor"] = v.loc[hold.index]
rows = []
for name in rules.columns:
    miss = rules[name] - hold                                     # forecast minus actual: positive is too high
    spare_rs = miss[miss > 0].sum() * 650 / 120                    # planned and never shipped, Rs 5.42 each
    late_rs = -miss[miss < 0].sum() * 25                           # shipped late, Rs 25 each
    rows.append({"rule": name, "MAE": round(miss.abs().mean()), "weeks too high": int((miss > 0).sum()),
                 "spare Rs lakh": round(spare_rs / 100_000, 1),     # 100,000 rupees make a lakh
                 "late Rs lakh": round(late_rs / 100_000, 1),
                 "cost Rs lakh": round((spare_rs + late_rs) / 100_000, 1)})
priced = pd.DataFrame(rows).set_index("rule").sort_values("cost Rs lakh")
print(priced.to_string())
priced[["late Rs lakh", "spare Rs lakh"]].sort_values("late Rs lakh").plot.barh(stacked=True,
    color=["crimson", "plum"], title="The same misses in rupees, added over the hidden weeks")
plt.show()
check("the vendor errs high on most hidden weeks", priced.loc["vendor", "weeks too high"] > len(hold) / 2)
check("on these hidden weeks, priced, the vendor costs less than festival-aligned",
      priced.loc["vendor", "cost Rs lakh"] < priced.loc["festival-aligned", "cost Rs lakh"])
'''),
        md("""
        **What happened.** The answer is b, and it is the uncomfortable result. The vendor's
        misses cost Rs 11.9 lakh, festival-aligned's Rs 13.5 lakh, the house bot's Rs 30.5 lakh,
        each added over the thirteen weeks. The vendor errs high on 12 of 13 weeks, and a spare
        shipment costs Rs 5.42 against Rs 25 for a late one, so its bigger misses are the cheaper
        kind. The house bot's misses are the dear kind: 11 of its 13 weeks are too low, which is why
        it costs more than naive while scoring a lower MAE.

        This says that erring high pays at these costs. It does not hand the vendor the plan:
        nobody chose how far high it runs, it runs higher the further ahead it looks (3.6 percent
        too high in hidden weeks 1 to 6, 11.5 percent in weeks 8 to 13), and no hidden week holds a
        festival, where the vendor copies the wrong weeks. Chapter 3 raises festival-aligned by an
        amount the two costs choose instead.

        ## Does the score match the printed error table?

        A second route to the same number: print festival-aligned's thirteen misses as a table and
        average them by hand.
        """),
        code('''
table = pd.DataFrame({"actual": hold, "festival-aligned": rules["festival-aligned"]})
table["miss"] = table["festival-aligned"] - table["actual"]        # positive: too high
print(table.to_string())
by_hand = sum(abs(m) for m in table["miss"]) / len(table)
print(f"too high: {table.miss[table.miss > 0].sum():,}; too low: {-table.miss[table.miss < 0].sum():,}")
print(f"MAE from the printed misses: {by_hand:,.0f}")
check("the printed table gives the same MAE", round(by_hand) == scores["festival-aligned"])
'''),
        md("""
        ## How would you answer "how do you evaluate a forecast?" in an interview?

        Hide the latest weeks, at least as many as the plan's horizon, and forecast them from one
        origin. Fix the error measure before anyone scores, in the business's unit: shipments,
        then rupees. Compare every candidate with naive and the house bot, and send nothing that
        loses to them. Report which way the misses run, because a late shipment and a spare one
        cost different amounts. The trap the interviewer fishes for is judging by the fit.
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
          costs Rs 11.9 lakh; festival-aligned Rs 13.5 lakh; the house bot errs low and costs Rs
          30.5 lakh.
        - **Does the table agree?** Yes, 6,615 from the printed misses.
        - **Is festival-aligned good enough?** Good enough is a claim about the decision: a better
          forecast is worth having only if it would book different shifts. Chapter 3 asks where the
          festival falls this year and how far above the forecast the plan should sit, which these
          weeks cannot test.
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
        windows? How far above the forecast should the plan sit, and why? How many shifts a week?
        What would the other plans cost?
        """),
        code(SETUP + '''
weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
vendor = pd.read_csv("../data/C2_W04_D05_vendor_forecast_STUDENT.csv", parse_dates=["week_start"])
costs = pd.read_csv("../data/C2_W04_D05_costs_STUDENT.csv").set_index("item").rs
y = weekly.set_index("week_start").shipments
v = vendor.set_index("week_start").vendor_shipments
spare_rs = costs["idle_packer_shift"] / 120          # an idle shift's Rs 650 over 120 shipments: Rs 5.42
late_rs = costs["late_shipment"]                      # Rs 25 a late shipment
diwali = {2024: pd.Timestamp("2024-10-28"), 2025: pd.Timestamp("2025-10-20"), 2026: pd.Timestamp("2026-11-02")}

source = {}                                           # week -> the week festival-aligned copies for it
for d in pd.date_range(y.index[52], "2026-11-30", freq="7D"):   # every week with a year of weeks behind it
    source[d] = d - pd.Timedelta(weeks=52)            # outside the stretch: the same calendar week
    for year, w in diwali.items():
        gap = (d - w).days // 7                       # weeks from that year's Diwali week; -5 is five before
        if -5 <= gap <= 4 and year - 1 in diwali:
            source[d] = diwali[year - 1] + pd.Timedelta(weeks=gap)   # the same distance from last year's Diwali

print(f"a spare shipment costs Rs {spare_rs:.2f}; a late one Rs {late_rs}")
print(source[pd.Timestamp("2026-10-19")].date(), "is the source for the week of 19 Oct 2026")
check("the week of 19 Oct 2026 copies 6 Oct 2025", source[pd.Timestamp("2026-10-19")] == pd.Timestamp("2025-10-06"))
'''),
        md("""
        ## How did each rule do on 2025's festival?

        The only festival the data can test the rules on is 2025's. A **back-test** stands at an
        earlier date and forecasts what came next as if the later weeks were unknown: stand in the
        week of 22 September 2025 and forecast the eight weeks from 29 September to 17 November
        2025. Festival-aligned copies, from five weeks before Diwali's week to four after, the week
        at the same distance from last year's Diwali. One honest caveat: the 4 percent growth was
        measured later, on weeks up to June 2026, so the cell also runs festival-aligned with no
        growth, as a planner in September 2025 could have.

        **Predict before you run.** By how many weeks does the house bot miss 2025's peak?

        a) none: same week last year knows the season
        b) one week late
        c) one week early
        d) two weeks late
        """),
        code('''
weeks25 = pd.date_range("2025-09-29", periods=8, freq="7D")        # 29 Sep to 17 Nov 2025
back = pd.DataFrame({
    "actual": y.loc[weeks25],
    "house bot": [y[d - pd.Timedelta(weeks=52)] for d in weeks25],
    "finance": [round(y[d - pd.Timedelta(weeks=52)] * 1.04) for d in weeks25],
    "festival-aligned": [round(y[source[d]] * 1.04) for d in weeks25],
    "aligned, no growth": [y[source[d]] for d in weeks25],
}, index=weeks25)
back[["actual", "house bot", "festival-aligned"]].plot(marker="o", title="2025's festival, forecast from 22 Sep 2025")
plt.show()
for rule in ["house bot", "finance", "festival-aligned", "aligned, no growth"]:
    miss = back[rule] - back.actual                                  # positive: too high
    spare = miss[miss > 0].sum() * spare_rs
    late = -miss[miss < 0].sum() * late_rs
    print(f"{rule}: MAE {miss.abs().mean():,.0f}; spare Rs {spare / 100_000:.1f} lakh, "
          f"late Rs {late / 100_000:.1f} lakh, total Rs {(spare + late) / 100_000:.1f} lakh")
overtime = weekly.set_index("week_start").overtime_shifts
print(f"overtime shifts: {overtime['2025-10-06']:,} in the week of 6 Oct 2025, {overtime['2025-11-24']} in the week of 24 Nov 2025")
check("the bot's peak is 13 Oct 2025, a week late", back["house bot"].idxmax() == pd.Timestamp("2025-10-13"))
check("festival-aligned peaks on 6 Oct 2025 with the actual", back["festival-aligned"].idxmax() == back.actual.idxmax())
'''),
        md("""
        **What happened.** The answer is b. The house bot put 2024's peak on 13 October 2025, a
        week late: MAE 58,250 and Rs 79.8 lakh of misses, Rs 69.6 lakh of it late shipments in the
        weeks where 2025's rush came before the copy expected it. Finance's rule, the same copy plus
        4 percent, missed by 60,488 a week. Festival-aligned missed by 4,034 a week and Rs 4.6 lakh,
        and with no growth added it still missed by only 10,575. One festival is a thin test, so the
        plan treats this as evidence about placement, never as a precise error.

        ## Which week does each forecast put this year's peak in?

        Diwali 2026 falls on Sunday 8 November, so its week begins 2 November, and the sale, and
        with it the peak, should come two weeks before, in the week of 19 October.

        **Predict before you run.** Which week does the house bot's copy of 2025 make the busiest
        week of the festive season?

        a) 5 October 2026
        b) 19 October 2026
        c) 26 October 2026
        d) 2 November 2026
        """),
        code('''
weeks26 = pd.date_range("2026-09-28", periods=10, freq="7D")        # 28 Sep to 30 Nov 2026
ahead = pd.DataFrame({
    "house bot": [y[d - pd.Timedelta(weeks=52)] for d in weeks26],
    "finance": [round(y[d - pd.Timedelta(weeks=52)] * 1.04) for d in weeks26],
    "vendor": v.loc[weeks26].values,
    "festival-aligned": [round(y[source[d]] * 1.04) for d in weeks26],
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
        puts it on 19 October, two weeks before Diwali's week. The window the planner books starts
        a week after 5 October, so inside it the calendar copies book the most for 12 October
        (369,000 from the house bot) and far too little for 19 and 26 October (308,900 and 188,600),
        when festival-aligned expects 434,928 and 383,760. The vendor's model never knew the
        festival moved.

        ## How do the four forecasts compare with last year's window?

        "Last year's window" has two readings. The same calendar weeks, 13 October to 1 December
        2025, hold only the tail of 2025's festival. The same weeks counted from Diwali, 29
        September to 17 November 2025, hold all of it.

        **Predict before you run.** Finance's eight weeks sit 4 percent above the same calendar
        weeks of 2025. Where do they sit against 2025's weeks counted from Diwali?

        a) 4 percent above, the same as on the calendar weeks
        b) between 0 and 4 percent above
        c) below them
        """),
        code('''
window = weeks26[2:]                                    # 12 Oct to 30 Nov 2026, the weeks to book
calendar_2025 = y.loc[window - pd.Timedelta(weeks=52)].sum()
festival_2025 = y.loc[[source[d] for d in window]].sum()
totals = ahead.loc[window].sum()
compare = pd.DataFrame({"eight weeks": totals.map("{:,}".format),
                        "vs same calendar weeks": (totals / calendar_2025 - 1).map("{:+.1%}".format),
                        "vs same weeks from Diwali": (totals / festival_2025 - 1).map("{:+.1%}".format)})
print(f"2025, same calendar weeks: {calendar_2025:,}   2025, same weeks from Diwali: {festival_2025:,}")
print(compare.to_string())
print(f"finance below festival-aligned: {totals['festival-aligned'] - totals['finance']:,} shipments")
check("finance is plus 4 percent on the calendar window", round(totals["finance"] / calendar_2025 - 1, 3) == 0.04)
check("the vendor is plus 22 percent on the calendar window", round(totals["vendor"] / calendar_2025 - 1, 3) == 0.22)
check("finance sits below festival-aligned", totals["finance"] < totals["festival-aligned"])
'''),
        md("""
        **What happened.** The answer is c. Against the calendar weeks, festival-aligned reads 19.5 percent above
        last year, close to the vendor's 22.0, because 2026's peak weeks fall inside the window and
        2025's fell before it. Against the weeks counted from Diwali it reads 4.0 percent. Finance's
        plus 4 is plus 4 only on the calendar window: against last year's festival weeks it sits
        9.5 percent below, and against festival-aligned's forecast it is 308,048 shipments short,
        on the costly side. The vendor's total sits 2.1 percent above festival-aligned, with its
        busiest week on 5 October.

        ## How far above the forecast should the plan sit, and why?

        **Predict before you run.** A late shipment costs Rs 25 and a spare one Rs 5.42. Where
        should the plan sit?

        a) at the forecast, covering demand in about half the weeks
        b) above the forecast, covering demand in about four weeks of five
        c) far enough above to cover every week
        d) below the forecast, since spare shipments waste money

        The cell below works out the share of weeks the plan should cover from the two costs, then
        reads that point off festival-aligned's own misses on chapter 2's hidden weeks. Here the
        miss is measured the other way round: how far demand came **above** the forecast, as a
        share of it, so a positive number is a week the forecast was too low.
        """),
        code('''
hold = y.iloc[91:]                                              # chapter 2's thirteen hidden weeks
fa_hold = (y.shift(52).loc[hold.index] * 1.04).round()          # festival-aligned on them
above = (hold - fa_hold) / fa_hold                              # demand above the forecast, as a share
print("demand above the forecast, percent, smallest first:")
print((above * 100).round(1).sort_values().to_list())
q = late_rs / (late_rs + spare_rs)                              # the share of weeks to cover
cushion = round(above.quantile(q), 3)                           # 0.82 of the way along the sorted thirteen
covered = (above <= cushion).sum()
print(f"cover {q:.2f} of weeks: raise the forecast by {cushion:.1%}, which covers {covered} of the 13 weeks")
raised = fa_hold * (1 + cushion)
gap = raised - hold                                             # positive: spare
raised_cost = (gap[gap > 0].sum() * spare_rs - gap[gap < 0].sum() * late_rs) / 100_000
print(f"raised by {cushion:.1%}, these weeks' misses cost Rs {raised_cost:.1f} lakh, read from the same weeks")
check("the plan share is about 0.82", round(q, 2) == 0.82)
check("the cushion sits between the 10th and 11th sorted weeks",
      sorted(above)[9] <= cushion <= sorted(above)[10])
'''),
        md("""
        **What happened.** The answer is b. Raise the plan by one shipment and two things can happen.
        If demand turns out higher, that shipment is no longer late, which saves Rs 25. If demand
        turns out lower, it is a spare shipment, which wastes Rs 5.42. Picture 100 weeks. If demand
        beats the plan in 18 of them, one more shipment of plan saves 18 x Rs 25 = Rs 450 and wastes
        82 x Rs 5.42 = Rs 444: about even, so stop there. That is the rule, called the newsvendor
        rule after a seller deciding how many papers to stock: plan so that demand is covered in
        this share of weeks.

        $$\\text{share covered} = \\frac{\\text{late cost}}{\\text{late cost} + \\text{spare cost}} = \\frac{25}{25 + 5.42} \\approx 0.82$$

        Sorted, the thirteen weeks run from 5.9 percent below the forecast to
        7.8 percent above. The 0.82 point sits between the 10th week, 2.1 percent, and the 11th,
        2.7 percent; `quantile` reads it 0.82 of the way along the list, at 2.6 percent. The raised
        forecast covers 10 of the 13 weeks, and the 11th misses by a hair. With thirteen weeks the
        true point could sit anywhere from about 2 to 3 percent; the curve below shows why that
        stretch costs almost the same.

        ## How does a week's cost change as the plan is raised?

        Try every level of plan on the busiest week, 19 October 2026, and for each level replay
        the thirteen hidden-week misses as thirteen possible demands; average their costs.
        """),
        code('''
base = ahead.loc["2026-10-19", "festival-aligned"]            # the plan's busiest week
levels = [i / 1000 for i in range(-80, 101, 2)]               # 8 percent below to 10 percent above
cost_at = []
for g in levels:                                              # each way the plan could be raised
    plan_level = base * (1 + g)
    total = 0
    for a in above:                                           # each past miss, as a possible demand
        demand = base * (1 + a)
        total += max(0, plan_level - demand) * spare_rs + max(0, demand - plan_level) * late_rs
    cost_at.append(total / len(above) / 100_000)              # the week's average cost, Rs lakh
plt.plot([g * 100 for g in levels], cost_at, color="black")
plt.axvline(cushion * 100, ls="--", color="slateblue")
plt.xlabel("plan above the forecast for the week of 19 Oct 2026, percent")
plt.ylabel("average cost of the week, Rs lakh")
plt.title("Too little plan costs more than too much, so the lowest point sits above the forecast")
plt.show()
lowest = levels[cost_at.index(min(cost_at))]
print(f"the lowest cost sits {lowest:.1%} above the forecast; the plan takes {cushion:.1%}")
check("the cheapest level sits above the forecast", lowest > 0)
'''),
        md("""
        ## How many packer shifts does each week need?

        The plan raises each week of the festival-aligned forecast by the 2.6 percent cushion, then
        divides by 120 shipments a shift and rounds up.
        """),
        code('''
plan = (ahead.loc[window, "festival-aligned"] * (1 + cushion)).round()
shifts = (plan / 120).apply(math.ceil)
plain = (ahead.loc[window, "festival-aligned"] / 120).apply(math.ceil)    # the forecast with no cushion
staffing = pd.DataFrame({"forecast": ahead.loc[window, "festival-aligned"], "plan": plan.astype(int),
                         "packer shifts": shifts})
print(staffing.to_string())
print(f"total: {shifts.sum():,} packer shifts over eight weeks; the forecast alone needs {plain.sum():,}, "
      f"so the cushion adds {shifts.sum() - plain.sum():,}")
staffing["packer shifts"].plot.bar(color="lavender", edgecolor="slateblue", title="Packer shifts a week")
plt.show()
check("the busiest week of the plan is 19 Oct 2026", staffing["packer shifts"].idxmax() == pd.Timestamp("2026-10-19"))
'''),
        md("""
        ## What would the other plans cost if demand follows the festival-aligned forecast?

        A scenario, never a measurement: if festival-aligned is right about where the rush falls,
        what does booking by each other forecast cost? Each plan is priced against festival-aligned's
        weeks, Rs 5.42 for every spare shipment and Rs 25 for every shipment short. The 2025
        back-test is the evidence that festival-aligned places the rush well; this table prices
        being wrong about it.
        """),
        code('''
expected = ahead.loc[window, "festival-aligned"]               # demand, if festival-aligned is right
booked = {"house bot": ahead.loc[window, "house bot"], "finance": ahead.loc[window, "finance"],
          "vendor": ahead.loc[window, "vendor"], "plan": plan}
scenario = {}
for name, b in booked.items():
    gap = b - expected                                         # positive: spare capacity
    scenario[name] = (gap[gap > 0].sum() * spare_rs - gap[gap < 0].sum() * late_rs) / 100_000
    print(f"{name}: Rs {scenario[name]:.1f} lakh")
check("the plan costs least in this scenario", min(scenario, key=scenario.get) == "plan")
'''),
        md("""
        **What happened.** If demand follows festival-aligned, the house bot's weeks cost Rs 111.6
        lakh, finance's Rs 103.6 lakh and the vendor's Rs 82.2 lakh, mostly late shipments in the
        weeks of 19 October to 2 November. The plan's cushion costs Rs 3.3 lakh of spare shifts if
        demand lands exactly on the forecast: the price of the insurance.

        ## What can two years of weeks not tell us?

        - **The festival moves, and the sale moves with it.** Tested on one festival only: the 2025
          back-test.
        - **Two years hold only two festivals,** so the festival's shape rests on two examples; no
          check inside the data closes that.
        - **The hidden weeks hold no festive week,** so their 6,615 is an ordinary-week error; the
          2025 festival gave 4,034 on one festival.
        - **Capacity caps the peak.** Overtime reached 1,638 shifts in the week of 6 October 2025
          against 5 in the week of 24 November 2025, as the back-test cell printed, so peak demand
          may have run above what shipped.
        - **The 4 percent growth** is two years' evidence; a third year could move it.
        - **The vendor's model has never forecast a Lucknow festival it had not seen,** so its
          festive numbers are an untested assumption.

        ## The same method at an AI company: how much inference capacity does a launch need?

        **Inference** is the computing a model does each time it answers a user. A product launch
        is the festival: a known date, a spike, little history. Line the last launch up by days from
        launch day, hide as many days as the plan covers, score in requests a minute, beat the last
        launch's shape, and set capacity above the forecast, because a timeout costs more than an
        idle server.

        ## What did chapter 3 answer?

        - **2025's festival:** the house bot landed the peak a week late (Rs 79.8 lakh of misses);
          festival-aligned missed by Rs 4.6 lakh.
        - **This year's peak:** the house bot, finance and the vendor put it on 5 October 2026;
          festival-aligned on 19 October.
        - **Last year's windows:** festival-aligned is 19.5 percent above the calendar weeks and 4.0
          percent above the weeks from Diwali; finance is 9.5 percent below the festival weeks.
        - **How far above:** cover 0.82 of weeks, a 2.6 percent cushion.
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
        the 1,000 orders in the Week 2 data warehouse, the class's database of Kalpa's orders.
        Diwali fell on 31 October 2024 and 20 October 2025, and falls on 8 November 2026.

        **Who needs the answer.** Anand, who signs the board number, and the head of Retail-Plus,
        whose stock and staff follow it. A number the board holds Kalpa to for two quarters costs
        either a missed promise or idle stock.

        **The questions on the way.** What shape do the two winters have? How do naive and drift
        score on April to September 2026? How do the seasonal copy and the vendor score? Which month
        does each copy put Diwali in this year? What error bar goes beside the board number?
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

        Twelve rows: October to March of 2024-25 and of 2025-26, in Rs lakh (a lakh is 100,000).

        **Predict before you run.** Which month is the biggest of each winter?

        a) October
        b) November
        c) December
        d) March
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

        Hide the last six months and forecast them from March 2026: the board's horizon is six
        months, so the test hides six. Naive repeats March; drift extends the line from October
        2024 through March 2026, 17 months of steps. The score is MAE in Rs lakh. The chart above
        also shows tall Aprils and Julys in both years; they repeat, so a copy of last year carries
        them, and the board's six months, October to March, do not include them.
        """),
        code('''
hold = rev["2026-04":"2026-09"]
months_ahead = pd.Series(range(1, 7), index=hold.index)
naive = pd.Series(rev["2026-03"], index=hold.index)
drift = rev["2026-03"] + months_ahead * (rev["2026-03"] - rev["2024-10"]) / 17   # 17 months, Oct 2024 to Mar 2026

naive_mae = (naive - hold).abs().mean() / 1e5                # misses, signs dropped, averaged: Rs lakh a month
drift_mae = (drift - hold).abs().mean() / 1e5
print(f"naive MAE: Rs {naive_mae:.1f} lakh   drift MAE: Rs {drift_mae:.1f} lakh")
pd.DataFrame({"actual": hold, "naive": naive, "drift": drift}).div(1e5).plot(marker="o", title="Six hidden months, Rs lakh")
plt.show()
check("naive misses by more than Rs 50 lakh a month", naive_mae > 50)
'''),
        md("""
        ## How do the seasonal copy and the vendor score on the same six months?

        **Your turn.** Score the seasonal copy (the same month a year earlier, Kalpa's house bot)
        and the vendor's forecast on the same six months. Type these lines into the empty cell below
        and run them; the vendor's `kind` column says which of its rows are fits and which are
        forecasts for the hidden months:

        ```python
        seasonal = rev.shift(12).loc[hold.index]
        vendor_hold = vendor.loc[hold.index, "vendor_rs"]
        print(vendor.loc[hold.index, "kind"].unique())
        seasonal_mae = (seasonal - hold).abs().mean() / 1e5
        vendor_mae = (vendor_hold - hold).abs().mean() / 1e5
        print(f"seasonal MAE: Rs {seasonal_mae:.1f} lakh   vendor MAE: Rs {vendor_mae:.1f} lakh")
        ```
        """),
        empty(),
        md("""
        ## Which month does each copy put Diwali in this year?

        Diwali 2026 falls on Sunday 8 November. Kalpa's revenue is booked when shoppers buy, in the
        days just before Diwali, so its spike sits in Diwali's own month: October in 2024 and 2025,
        and November in 2026, since the days before 8 November fall in November. Flipkart's
        shipments peaked two weeks earlier because parcels leave the centre in the sale weeks. The
        month-aligned copy takes each month from the same month last year. The festival-aligned copy
        swaps two months: this November gets last year's Diwali month, October 2025, and this
        October gets last year's November; then it adds 4 percent.

        **Your turn.** Type these lines into the empty cell below:

        ```python
        months = ["2026-10", "2026-11", "2026-12", "2027-01", "2027-02", "2027-03"]
        year_before = ["2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03"]
        swapped = ["2025-11", "2025-10", "2025-12", "2026-01", "2026-02", "2026-03"]
        table = pd.DataFrame({"same month last year": [rev[m] for m in year_before],
                              "finance: plus 4 percent": [round(rev[m] * 1.04) for m in year_before],
                              "festival-aligned": [round(rev[m] * 1.04) for m in swapped],
                              "vendor": vendor.loc[months, "vendor_rs"].values,
                              "plan line": plan.loc[months].values}, index=months) / 1e5
        print(table.round(1).to_string())
        print((table.sum() / 100).round(2).to_string())          # six months, Rs crore
        ```
        """),
        empty(),
        code('''
growth = rev["2025-10":"2026-09"].sum() / rev["2024-10":"2025-09"].sum() - 1
print(f"the second year grew {growth:.1%} on the first")
print(f"plan line, Oct 2026 to Mar 2027: Rs {plan.sum() / 1e7:.2f} crore")
copy_plus4 = (rev.shift(12).loc[hold.index] * 1.04).round()        # festival-aligned on the hidden months
aligned_mae = (copy_plus4 - hold).abs().mean() / 1e5
print(f"festival-aligned's own miss on Apr to Sep 2026: Rs {aligned_mae:.1f} lakh a month")
(plan / 1e5).plot.bar(color="lavender", edgecolor="slateblue", title="The plan line, Rs lakh a month")
plt.show()
check("the plan line is 15 percent above last year's same months",
      abs(plan.sum() / rev["2025-10":"2026-03"].sum() - 1.15) < 0.001)
'''),
        md("""
        ## What do you bring to the TA, in rupees?

        Anand's board number in one paragraph: the forecast you would send, the month it puts the
        spike in, its error bar in Rs lakh, and the gap to the plan line. The unguided exercise
        `exercises/unguided/C2_W04_D05_kalpa_board_STUDENT.md` asks the same decision in lettered
        items.

        - **The two winters:** October is the biggest month of each.
        - **Naive and drift:** they miss April to September 2026 by Rs 59.4 and Rs 58.8 lakh a month.
        - **The seasonal copy and the vendor:** your first cell.
        - **Diwali this year, and the six months' totals:** your second cell.
        - **The error bar:** festival-aligned, the seasonal copy plus 4 percent, missed the six
          hidden months by Rs 3.5 lakh a month, about Rs 21 lakh if all six miss the same way. No
          hidden month holds Diwali, so the spike month itself is untested.
        - **Why 4 percent:** finance's rule adds 4; the data's own growth, 3.7 percent, is close, so
          festival-aligned keeps finance's 4 percent and differs from it only in the month that
          carries Diwali.
        """),
    ]


if __name__ == "__main__":
    for name, cells in [("01_twelve_rows", nb01()), ("02_holdout_scoreboard", nb02()),
                        ("03_festive_plan", nb03()), ("04_kalpa_lab", nb04())]:
        path = NB / f"C2_W04_D05_{name}_STUDENT.ipynb"
        build(path, cells)
        print("built", path.name, len(cells), "cells")

# Forecasting basics: how much does the plan deliver, against a baseline that is hard to beat?

Week 4, Friday. About 12 minutes to read, and 10 more for the self-check.

Friday teaches five topics on a chai stall at a hostel gate (invented), small enough to count by
hand; then Flipkart's Lucknow fulfilment centre (FC) uses all five to book packer shifts for eight
festive weeks, between a vendor's plus 22 percent and finance's plus 4. Illustrative case: the company is real, the situation and the data are synthetic, built for this
class.

---

## What can you do after Friday?

- Read a series' trend and seasons before choosing any rule.
- Run naive, seasonal naive and drift by hand, and say when each copy fails.
- Hide the latest periods and score a rule in the business's unit, both ways.
- Say why a close fit proves nothing until a rule beats the baseline.
- Stop improving when a better forecast is worth less than it costs, and write the note.

## Which map holds the day?

```mermaid
flowchart LR
    T1["<b>Chapter 1</b><br/>Trend and<br/>seasonality,<br/>read before<br/>modelling"] --> T2["<b>Chapter 2</b><br/>Naive,<br/>seasonal naive<br/>and drift<br/>baselines"]
    T2 --> T3["<b>Chapter 3</b><br/>Holding out;<br/>MAE and MAPE<br/>in the<br/>business's<br/>units"]
    T3 --> T4["<b>Chapter 4</b><br/>Beating the<br/>baseline; the<br/>vendor curve<br/>tested"]
    T4 --> T5["<b>Chapter 4,</b><br/><b>second half</b><br/>The<br/>good-enough<br/>call and the<br/>forecast note"]
    T5 --> C["<b>The case</b><br/>Flipkart,<br/>Lucknow;<br/>chapters 5,<br/>6 and 7"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class T1,T2,T3,T4,T5 lit
    class C kalpa
```

Each topic needs the one before it: read, copy, score, beat, stop.

---

## Trend and seasonality, read before modelling: what does a series tell you before any rule is chosen?

**Who needs the answer.** The stall's owner (invented), who orders milk for three days at a time,
and the FC planner, who books shifts weeks ahead.

**The questions on the way.** What repeats, and how often? Is the stall (invented) growing? What is left?

A **time series** is one number per equal period, in time order; a **forecast** is a number for a
period nobody has seen. The invented stall sold 60 cups on Sunday 6 October 2024 and 100 on Monday.
Up 67 percent? No: both Sundays of its first fortnight sold about 60 and every other day about 100. A
repeat on a fixed beat is a **season**, and its **length** is the periods before it repeats: 7 days
at the stall, 52 weeks in Flipkart's year.

Read growth at the same point a season apart: a week apart shows a week's change, too small to see,
and a year apart the year's growth. Monday 6 October 2025 sold 110 against 100 a year earlier: up 10
percent. Sunday stays 0.6 of a Monday in both years, so the beat keeps its shape while the level, the **trend**, climbs. Seasons go both ways:
the exam fortnight runs about 1.4 times an ordinary one and Diwali week about 0.4, a dip. What is left
is the **remainder**. Read in cups, a yearly copy's misses hold the remainder of both years, with a
typical size, the standard deviation, of about 4.7 cups, except where Diwali moved: up to 70.

$$y_t = T_t + S_t + R_t \qquad y_t = T_t \times S_t \times R_t$$

Forecasting: Principles and Practice adds the parts when the seasons keep their size and multiplies
them when they grow with the level, as the stall's do (section 3.2, checked 13 October 2026). A **cycle**, a rise and fall with no fixed length, needs more than two years to see.

**At Flipkart.** A level near 210,000 shipments a week, growth of about 4 percent a year, a festive
peak each year.

## Naive, seasonal naive and drift baselines: what does each copy, and when does the copy fail?

**Who needs the answer.** The owner (invented), who needs a rule a person can run on paper, and the
planner, whose house bot, this case's name for the seasonal naive, is one of these rules.

**The questions on the way.** What does each rule copy? Which wins on a beat? Where does it fail?

A **baseline** is the simplest rule that could be right, and its job is to be beaten. Forecast the
invented stall's Sunday 19 January 2025 from the four days before it, 98, 104, 101 and 103, and last
Sunday's 61:

- **Naive** repeats the last value: 103, which misses the 60 sold by 43.
- **Drift** extends the line from the first value to the last, the four days taken as the whole
  history: 103 + (103 - 98) / 3, about 104.7.
- **Seasonal naive** copies one season back, last Sunday: 61, a miss of 1.

With $T$ the last period a rule may see, $h$ the periods ahead and $m$ the season's length
(Forecasting: Principles and Practice, section 5.2, checked 13 October 2026):

$$\hat{y}_{T+h} = y_T \qquad \hat{y}_{T+h} = y_{T+h-m}\ (h \le m) \qquad \hat{y}_{T+h} = y_T + h\,\frac{y_T - y_1}{T - 1}$$

A yearly copy carries last year's level: on the invented stall's first exam day, which sold 154, the
same weekday 364 days back said 140, and times 1.10, 154. A
copy fails when the season moves. Diwali came eleven days earlier in 2025, so the calendar copy put
Diwali's 40 cups on a day that sold 110, a miss of 70, and missed by up to 71 across those three
weeks. Copying the day at the same distance from last year's festival, with no growth so the move
shows alone, misses by at most 13. This programme calls that **festival-aligned**: its own
extension of the seasonal naive.

**At Flipkart.** The seasonal naive with $m = 52$ is "the same week last year", which the afternoon's
tournament calls the house bot; finance's rule is the house bot times 1.04.

## Holding out; MAE and MAPE in the business's units: how is a forecast scored honestly?

**Who needs the answer.** The owner (invented), before trusting a rule, and the regional operations
head, before a vendor's curve books a shift.

**The questions on the way.** Which periods do we hide? How is a miss counted? Which way is it wrong?

Hide the latest periods, at least as many as the forecast must reach ahead. The invented stall's milk
order reaches three days, so days 12 to 14 of a fortnight are **hidden**, day 11 is the **origin**,
the last day a rule may see, and three days is the **horizon**. The test set should "ideally be at
least as large as the maximum forecast horizon required" (Forecasting: Principles and Practice,
section 5.8, checked 13 October 2026).

Naive says 100 for each hidden day; they sold 110, 95 and 100. A **miss** is the forecast minus what
sold: -10, +5 and 0. The book writes sold minus forecast, so its signs run the other way.

$$\text{MAE} = \frac{1}{n}\sum_t \left|\text{miss}_t\right| \qquad \text{MAPE} = \frac{1}{n}\sum_t \frac{\left|\text{miss}_t\right|}{y_t}$$

Here $n$ is the number of hidden periods. The MAE is 5.0 cups and the MAPE about 4.8 percent; the
**lean**, the misses averaged with their signs, is -1.7 cups. Priced at Rs 12 a cup short and Rs 6 a
cup unsold, the three days cost Rs 150. MAPE divides by what sold, so a near-empty day swamps it: a
15-cup miss is 300 percent of a rain day's 5 cups. A miss below what sold cannot pass 100 percent
while one above has no ceiling, so a rule picked by MAPE runs low. Keep MAE for the order and MAPE
for comparing stalls of different sizes.

**WATCH OUT.** Misses of +10, +10 and of +10, -10 share an MAE of 10 and cost Rs 120 and Rs 180.
Report the MAE and the lean together.

**At Flipkart.** Thirteen weeks are hidden, forecast from 22 June 2026, and the plan reaches ten
weeks past the data. A spare shipment costs Rs 650 a shift over 120 shipments, Rs 5.42; a late one Rs 25.

## Beating the baseline; the vendor curve tested: why is a close fit no proof?

**Who needs the answer.** The owner (invented), offered a "model" by a nephew, and the operations head, offered
a vendor's curve that fits history within 2 percent.

**The questions on the way.** What does a perfect fit say about tomorrow? Does the clever rule win?

**Fit** is how close a rule sits to the periods it was built on; **forecast error** is how far it
misses periods it never saw. A curve through the invented stall's four days, 100, 104, 98 and 110,
fits them with an error of 0 and says 168 for day 5, which sold 102: a miss of 66. The straight line,
97 + 2.4 a day, says 109 and misses by 7. By hand: the differences are 4, -6 and 12, theirs -10 and
18, and theirs 28; held level, the next row is 28, 46 and 58, and 110 + 58 = 168. "A model which fits the training data well will not
necessarily forecast well" (Forecasting: Principles and Practice, section 5.8, checked 13 October
2026).

The nephew's second rule (invented), the mean of the last seven days, misses seven hidden days by 12.4 cups; the
seasonal naive by 4.0. Nothing goes to the order unless it beats the seasonal naive on hidden
periods, by the measure fixed before either ran.

**At Flipkart.** The vendor's curve fits its 91 weeks within 1.4 percent and misses the thirteen
hidden weeks by 16,400 a week, 67 percent worse than the house bot's 9,831. In the M5 competition
only 35.8 percent of teams beat the seasonal naive (checked 12 October 2026).

## The good-enough call and the forecast note: when do you stop improving, and what do you send?

**Who needs the answer.** The owner (invented), deciding whether a better rule is worth having, and
the milkman, who reads the order.

**The questions on the way.** Would a better forecast change the order? What goes in the note?

Milk comes in cans of 40 cups (invented). On the seven hidden days the seasonal naive orders 3 cans a
weekday and 2 on Sunday, exactly what a forecast that knew the future would order; the nephew's mean
orders a third can on Sunday, Rs 240 of milk that sours. **Good enough** is a claim about the
decision, never about the model: a better forecast is worth having only when what it changes in the
order is worth more than the work. Here it changes no can.

The **forecast note** to the milkman (invented) carries four lines: the number, 3 cans a day Monday
to Saturday and 2 on Sunday; the method, the same day last week; the error bar, a typical miss of 4.0
cups a day, Rs 24 high or Rs 48 short; and what would make it wrong, exams starting early or the
hostel emptying.

**At Flipkart.** A shift is 120 shipments, small beside the typical miss, so good enough becomes a
question in rupees: a rule whose MAE is 100 lower is worth Rs 542 to Rs 2,500 a week. The staffing
note puts number and method in its title and adds the festival's week and a reply to each objector.

---

## The case: how much is coming to Flipkart's Lucknow centre, and how wrong could the forecast be?

**Who needs the answer.** The FC planner, who books the shifts, and the regional operations head, who
answers for late parcels in the busiest weeks.

**The questions on the way.** Where is the peak? Which rule wins on hidden weeks? How many shifts?

The centre has 104 weeks of outbound shipments. Diwali fell on
Thursday 31 October 2024 and Monday 20 October 2025, and falls on Sunday 8 November 2026 (the holiday lists of DoPT, the
government's personnel department, checked 12 October 2026).

![Two festive seasons on one axis: shipments by weeks from Diwali, 2024 and 2025 overlaid](../whiteboards/C2_W04_D05_festival_plot_STUDENT.png)

**Chapter 5.** Both years peak two weeks before Diwali's week, in the festive sale: 401,000 and
418,200 shipments. For Diwali 2025's week, which shipped 308,900, naive said 369,000 and the seasonal
naive 356,200, both far too high; festival-aligned, with no growth, which October 2025 could not yet
measure, said 296,900, 12,000 low.

**Chapter 6.** On the thirteen hidden weeks festival-aligned and finance's rule tie at 6,615 a week,
since no hidden week sits near Diwali; the house bot scores 9,831, naive 14,923 and the vendor
16,400. Priced, the vendor's misses cost least, Rs 11.9 lakh against Rs 13.5 lakh, only because it
errs high, the cheap side, and only at Rs 25 a late shipment: at Rs 15 festival-aligned costs least.

**Chapter 7.** On 2025's festival the house bot missed by 58,250 a week and festival-aligned, with no
growth, by 10,575, placing the peak right. In 2026 the calendar copies put the busiest week on 5
October and festival-aligned on 19 October. Finance's plus 4 is read against 2025's calendar weeks,
which held only the festival's tail; counted from Diwali it sits 9.5 percent below.
The plan books festival-aligned's forecast over 120 shipments a shift, rounded up: 19,760 shifts.

The **error bar** has two parts: a typical miss of 6,615 shipments a week, about Rs 35,800 of idle
shifts when that far high and Rs 1.65 lakh of late shipments when that far low; and the hidden weeks'
range, 5.9 percent below to 7.8 percent above, which puts the week of 19 October at 3,413 to 3,906
shifts. Two years hold only two festivals, and capacity may cap the peak: overtime hit 1,638 shifts in
the week of 6 October 2025. How far above the forecast to plan, the plan quantile, goes beyond the
five topics.

**Say it to a shift supervisor.** "The computer copied last year's dates, but Diwali falls on a
different date this year, so it books the most packers two weeks before the real rush. We count the
weeks from Diwali instead."

**The answer.** Festival-aligned books 19,760 packer shifts, 3,625 in the week of 19 October, with a
typical miss of 6,615 shipments a week.

---

## Can you answer these without notes?

1. The hostel mess (invented) used 25 kg of rice on Monday and 40 kg on Sunday: which comparison
   reads growth?
2. Diwali's week moves from 20 October to 2 November: which week of last year does the house bot
   copy into 2 November?
3. Naive missed three hidden days by -10, +5 and 0 cups: what are the MAE and the lean?
4. A curve fits every past week within 2 percent: what do you ask before trusting it?
5. What is a forecast whose MAE is 100 shipments a week lower than festival-aligned's worth?
6. From Thursday: why can blended retention stay flat while each signup month's falls?

**Key.** 1: the same day a week back, or the same week a year back. 2: 3 November. 3: 5.0 cups, and
-1.7, running low. 4: its score on periods it never saw, against the seasonal naive. 5: Rs 542 to Rs
2,500 a week, so it earns a place only if it costs less. 6: the blend weights groups by size, so big
young groups at their best months hold it up.

## Which interview questions does Friday prepare you for?

| The question as asked | The hire-grade line |
|---|---|
| [S] How do you evaluate a forecast? | "I hide the latest weeks, as many as the horizon, score the misses in shipments and rupees against the seasonal naive, and back-test the festival the hidden weeks lack." |
| [F] What baseline must any forecast beat, and why? | "Naive with no season, the seasonal naive with one, plus the growth when it trends; a copy costs nothing, so a model that cannot beat it adds cost for no accuracy." |
| [F] A vendor promises 22 percent growth: how do you test it? | "Restate the 22 against the same weeks, score the curve on weeks it never saw, 16,400 a week after a 1.4 percent fit, and ask for its record on a festival it did not see." |
| [D] Finance and Marketing each want their forecast in front of the board; how do you choose, and how do you present the error? | "I score both on weeks neither saw against a copy of last year, send the winner with its typical miss priced each way and its range, and concede what each got right." |

The tags: [S] a staple asked everywhere, [F] frequent in GCC and product screens, [D] a differentiator.

**The AI-company variant**, sizing inference capacity for a launch, is in the transcripts in `extras/`.

## Which words did Friday use?

| Term | Plain meaning | Example |
|---|---|---|
| Festival-aligned | This programme's extension: a copy at the same distance from last year's festival | 19 October 2026 copies 6 October 2025 |
| MAE, MAPE, lean | The average miss's size; as a percent; with signs kept, which an interviewer calls bias | 5.0 cups; 4.8 percent; -1.7 |
| Error bar | The typical miss on unseen periods, priced both ways, and the range of misses | 6,615 shipments a week; 3,413 to 3,906 shifts at the peak |

## Where should you read next, and how long does each take?

| Order | Source | Time |
|---|---|---|
| 1 | Hyndman and Athanasopoulos, Forecasting: Principles and Practice, section 2.3, time series patterns, https://otexts.com/fpp3/graphics.html#sec-tspatterns (checked 13 October 2026) | 10 minutes |
| 2 | The same book, section 5.2, simple forecasting methods, https://otexts.com/fpp3/toolbox.html#sec-simple-methods (checked 13 October 2026) | 20 minutes |
| 3 | The same book, section 5.8, forecast accuracy, https://otexts.com/fpp3/toolbox.html#sec-accuracy (checked 13 October 2026) | 20 minutes |
| 4 | IBM Technology, "What is Time Series Analysis?", a video, https://www.youtube.com/watch?v=GE3JOFwTWVM (checked 13 October 2026) | length not verified |

The week's explorer, `content/W04/D1/demos/C2_W04_D01_week_explorer_STUDENT.html`, replays the day.

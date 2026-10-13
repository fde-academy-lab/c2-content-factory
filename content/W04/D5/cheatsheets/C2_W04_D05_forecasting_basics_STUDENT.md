# Forecasting basics: how much does the plan deliver, and how wrong could it be?

Week 4 Friday. Five topics on a chai stall at a hostel gate (invented), then Flipkart's Lucknow fulfilment centre, where the planner books packer shifts for the eight weeks beginning 12 October to 30 November 2026 between a vendor's plus 22 percent and finance's plus 4. Illustrative case: the company is real, the situation and the data are synthetic, built for this class.

## Panel 1: How do the five topics connect, and where does the case use them?

```mermaid
flowchart LR
    T1["<b>1</b><br/>Trend and<br/>seasonality,<br/>read before<br/>modelling"] --> T2["<b>2</b><br/>Naive,<br/>seasonal naive<br/>and drift<br/>baselines"]
    T2 --> T3["<b>3</b><br/>Holding out;<br/>MAE and MAPE<br/>in the<br/>business's<br/>units"]
    T3 --> T4["<b>4</b><br/>Beating the<br/>baseline; the<br/>vendor curve<br/>tested"]
    T4 --> T5["<b>5</b><br/>The<br/>good-enough<br/>call and the<br/>forecast note"]
    T5 --> C["<b>The case</b><br/>Flipkart,<br/>Lucknow:<br/>19,760 shifts"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class T1,T2,T3,T4,T5 lit
    class C kalpa
```

**Crux:** Read the shape, copy it, score the copy on periods it never saw, keep only what beats the copy, and stop when nothing better would change the order.

## Panel 2: Trend and seasonality, read before modelling: what does a series tell?

- A **season** repeats on a fixed beat, up or down; its **length** is the periods before it repeats: 7 days at the invented stall, 52 weeks at Flipkart.
- Read growth the same point a season apart: Monday 110 against 100 a year earlier is 10 percent; Monday over Sunday, 100 over 60, is the beat.
- The stall's exam fortnight runs about 1.4 times an ordinary one, Diwali week about 0.4; the remainder wobbles about 4.7 cups.
- `y = T + S + R` when the seasons keep their size; a product when they grow with the level.

**Crux:** Name the beat and its length before any rule; at Lucknow, about 4 percent a year and a festive peak.

## Panel 3: Naive, seasonal naive and drift baselines: when does a copy fail?

| Rule | Copies | The invented stall's next Sunday | At Lucknow |
|---|---|---|---|
| Naive | the last value, `y[T]` | 103 | the week of 22 June |
| Seasonal naive | one season back, `y[T+h-m]` | 61, against 60 sold | the house bot, m = 52 |
| Drift | the line extended, `y[T] + h x (y[T] - y[1]) / (T - 1)` | about 104.7 | a step of 70 a week |
| Festival-aligned | the same distance from last year's festival | Diwali's worst miss 13, not 71 | this programme's extension |

**Crux:** On a strong beat the plainest copy that respects it wins; a calendar copy fails when the festival moves.

## Panel 4: Holding out; MAE and MAPE in the business's units: how is a forecast scored?

- Hide the latest periods, at least as many as the horizon: the stall's days 12 to 14 from day 11; Lucknow's 13 weeks from 22 June 2026, horizon ten weeks.
- MAE averages the misses' sizes, in the unit the cost is in: the stall's 5.0 cups; MAPE in percent, 4.8, explodes near zero.
- Keep the **lean**, the signed average: -1.7 cups, running low. Price it: Rs 150 at Rs 12 short and Rs 6 unsold.
- Same MAE, different rupees: +10, +10 costs Rs 120; +10, -10 costs Rs 180.

**Crux:** Fix the measure before scoring, in the business's unit, and report the size and the direction together.

## Panel 5: Beating the baseline and the good-enough call: when does a forecast earn trust?

- Fit is closeness on seen periods: the stall's curve fits four days with an error of 0 and misses day 5 by 66.
- The nephew's mean scores 12.4 cups on hidden days against the seasonal naive's 4.0: it earns no place.
- Good enough is a claim about the decision: the seasonal naive orders the cans a perfect forecast would.
- The note: the number, the method, the error bar in the unit and in rupees, what would make it wrong.

**Crux:** Nothing goes to the order unless it beats the seasonal naive on hidden periods by enough to change a decision.

## Panel 6: The case: where does the peak fall, and how many shifts?

![Two festive seasons by weeks from Diwali: both peak two weeks before Diwali's week](../whiteboards/C2_W04_D05_festival_plot_STUDENT.png)

| On 13 hidden weeks | MAE | Misses priced |
|---|---|---|
| Festival-aligned | 6,615 | Rs 13.5 lakh |
| Seasonal naive, the house bot | 9,831 | Rs 30.5 lakh |
| Vendor's curve, fitted within 1.4 percent | 16,400 | Rs 11.9 lakh |

The plan books festival-aligned's forecast over 120 a shift, rounded up: 19,760 shifts, 3,625 in the week of 19 October. Error bar: 6,615 shipments a week, about Rs 35,800 if high, Rs 1.65 lakh if low. Beyond the row: the plan quantile, 0.82, raises it to 20,275.

**Crux:** Copy by distance from Diwali, score on hidden weeks, price both directions, book in whole shifts.

## Panel 7: What does the interviewer listen for?

[S] "How do you evaluate a forecast?" Hold out the latest weeks, as many as the horizon; score in shipments and rupees against the seasonal naive; back-test a festival, since the hidden weeks hold none. [F] "A vendor promises 22 percent growth; how do you test it?" Score its curve on weeks it never saw, and read the 22 against the right window.

**Crux:** Name the hidden weeks, the unit, the copy to beat and the direction that costs more.

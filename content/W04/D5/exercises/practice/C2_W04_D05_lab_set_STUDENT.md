# Can you run Friday's whole method on shops and series you have never seen?

This set is sat in the TA-led practice lab, after the Kalpa notebook. Every shop, series and cost
below is invented, so the method is all that carries over from the morning: read the shape, apply the
rules, hide weeks and score them, judge a pitch, and price a miss in each direction. The problems
climb from a reading to a decision, one or more for each of the day's five topics.

**Who needs the answer.** You, before Saturday's paper and before an interviewer asks you to forecast
something on a whiteboard.

**The questions on the way.**

- Which shape does each series carry?
- What do three rules forecast for a shop whose festival moved?
- What is the MAE of five misses?
- Which question does a vendor's pitch need first?
- In which order do the lines of the house bot's code run?
- Do two rules with the same miss cost the same?

**What you post,** in this set's thread in the cohort channel: six letters in problem order, with no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

## Can you read a shape and apply a rule?

The first two problems apply chapters 1 and 2, trend and seasonality and the three baselines, on new
numbers.

### Q1. Which line reads the three invented series right?

*Level L1 · asked in analytics screens.* Eight weeks each.

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| X | 50 | 53 | 56 | 59 | 62 | 65 | 68 | 71 |
| Y | 50 | 50 | 70 | 50 | 50 | 50 | 70 | 50 |
| Z | 50 | 54 | 47 | 52 | 49 | 53 | 48 | 51 |

Which line is right?

a) X a season, Y a trend, Z a wobble
b) X a trend, Y a season, Z a wobble
c) X a trend, Y a wobble, Z a season
d) X a wobble, Y a season, Z a trend

### Q2. A gift shop's festival moved a week later this year: what does festival-aligned forecast for this year's week 5?

*Level L1 · asked in retail analytics screens.* Last year's six weeks, festival in week 3: 40, 55, 70,
50, 35, 41. This year's first four weeks, festival in week 4: 42, 44, 58, 73. Treat this year as the
same size as last year. Which value is festival-aligned's?

a) 73, this year's festival week, the week before
b) 35, the same calendar week of last year
c) 50, the week after last year's festival
d) 58, this year's week 3, two weeks back

## Can you score a forecast honestly?

The next two problems apply chapters 3 and 4, holding out and beating the baseline.

### Q3. Five hidden weeks missed by 9, -6, 14, -3 and -4: what is the MAE?

*Level L2 · asked in every analytics screen.*

a) 7.2
b) 2.0
c) 36.0
d) 14.0

### Q4. A vendor says its model fits the last two years within 1 percent and asks to run the plan from next week: which question comes first?

*Level L3 · asked in product-company and GCC screens.*

a) Which algorithm does it use, and how many parameters does it have?
b) How fast does it retrain each week on new data?
c) Can it fit three years of history within 1 percent?
d) On which hidden weeks did it beat a copy of last year?

## Can you put the code in order and price a miss?

The last two problems join the code to the decision.

### Q5. In which order do these lines score the house bot on the hidden weeks?

*Level L2 · asked in data-analyst screens.* The lines arrive scrambled:

```
1  hold = y.iloc[91:]
2  weekly = pd.read_csv("../data/C2_W04_D05_weekly_shipments_STUDENT.csv", parse_dates=["week_start"])
3  print(f"house bot MAE: {mae:,.0f}")
4  y = weekly.set_index("week_start").shipments
5  mae = (y.shift(52).loc[hold.index] - hold).abs().mean()
```

Which order runs?

a) 2, 4, 1, 5, 3
b) 2, 4, 5, 1, 3
c) 4, 2, 1, 5, 3
d) 2, 1, 4, 5, 3

### Q6. Two rules each miss a week by 1,000 shipments, one always high and one always low; a spare shipment costs Rs 5 and a late one Rs 30: which line is right?

*Level L5, a design call · asked in operations analytics screens.* The numbers are invented.

a) They cost the same, since both miss by 1,000 a week
b) The high rule costs more: Rs 30,000 a week against Rs 5,000
c) The low rule costs more: Rs 30,000 a week against Rs 5,000
d) Neither can be priced until both are scored in MAPE

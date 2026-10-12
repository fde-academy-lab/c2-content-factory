# Can you run Friday's whole method on shops and series you have never seen?

The TA-led practice lab, after the Kalpa notebook. Every shop, series and cost below is invented, so
the method is all that carries over from the morning: read the shape, apply the rules, hide weeks and
score them, judge a pitch, and set a plan's level from two costs. The problems climb from a reading
to a plan.

**Who needs the answer.** You, before Saturday's paper and before an interviewer asks you to forecast
something on a whiteboard.

**The questions on the way.**

- Which shape does each series carry?
- What do three rules forecast for a shop whose festival moved?
- What is the MAE of five misses?
- Which question does a vendor's pitch need first?
- In which order do the lines of the house bot's code run?
- What share of weeks should a plan cover, given two costs?

**What you post,** in this set's thread in the cohort channel: six letters in problem order, with no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

## Can you read a shape and apply a rule?

The first two problems are the morning's chapter 1, on new numbers.

### Q1. Which line reads the three invented series right?

*Level L1 · asked in analytics screens.* Eight weeks each.

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| X | 20 | 22 | 24 | 26 | 28 | 30 | 32 | 34 |
| Y | 20 | 35 | 20 | 20 | 20 | 35 | 20 | 20 |
| Z | 20 | 23 | 18 | 21 | 22 | 19 | 21 | 20 |

Which line is right?

a) X a season, Y a trend, Z noise
b) X a trend, Y a season, Z noise
c) X a trend, Y noise, Z a season
d) X noise, Y a season, Z a trend

### Q2. A gift shop's festival moved a week later this year: what does festival-aligned forecast for this year's week 5?

*Level L1 · asked in retail analytics screens.* Last year's six weeks, festival in week 3: 40, 55, 70,
50, 35, 41. This year's first four weeks, festival in week 4: 42, 44, 58, 73. Treat this year as the
same size as last year. Which value is festival-aligned's?

a) 73, this year's festival week, the week before
b) 35, the same calendar week of last year
c) 50, the week after last year's festival
d) 58, this year's week 3, two weeks back

## Can you score a forecast honestly?

The morning's chapter 2, on a printed table.

### Q3. Five hidden weeks missed by 12, -8, 5, -15 and 6: what is the MAE?

*Level L2 · asked in every analytics screen.*

a) 9.2
b) 0.0
c) 46.0
d) 15.0

### Q4. A vendor says its model fits the last two years within 1 percent and asks to run the plan from next week: which question comes first?

*Level L3 · asked in product-company and GCC screens.*

a) Which algorithm does it use, and how many parameters does it have?
b) How fast does it retrain each week on new data?
c) Can it fit three years of history within 1 percent?
d) On which hidden weeks did it beat a copy of last year?

## Can you put the code in order and set a plan's level?

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

### Q6. An idle shift costs Rs 600 and a late shipment Rs 30, and a packer packs 120 a shift: what share of weeks should the plan cover?

*Level L5, a design call · asked in operations analytics screens.* The numbers are invented.

a) 0.50
b) 0.14
c) 0.95
d) 0.86

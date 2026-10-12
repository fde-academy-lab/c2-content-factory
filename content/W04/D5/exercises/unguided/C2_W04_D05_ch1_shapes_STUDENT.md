# What do three series say about trend and season, and which forecast fits each?

Flipkart, the Lucknow fulfilment centre, where the planner reads a series' shape before choosing any
rule for the festive weeks of 2026. Illustrative case: the company is real, the situation and the data
are synthetic, built for this class. The three series below are invented, twelve weeks each, so each
shape stands alone.

**Who needs the answer.** The FC planner, who must name the shape before trusting a rule: a rule that
copies the wrong shape books shifts for weeks that do not need them.

**The questions on the way.**

- Which shape does each series carry?
- What do naive and a seasonal copy forecast for a repeating series?
- What fixes a seasonal copy when the series also climbs?

Four words, defined once. **Trend** is a steady climb or fall. **Season** is a pattern that repeats
on a fixed beat. **Noise** is what is left. **A seasonal copy** forecasts a week by copying the week
one beat back; here the beat is four weeks.

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Series A | 100 | 104 | 108 | 112 | 116 | 120 | 124 | 128 | 132 | 136 | 140 | 144 |
| Series B | 100 | 130 | 100 | 70 | 100 | 130 | 100 | 70 | 100 | 130 | 100 | 70 |
| Series C | 100 | 132 | 104 | 76 | 108 | 140 | 112 | 84 | 116 | 148 | 120 | 92 |

**What you post,** in this set's thread in the cohort channel: three letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxx
```

---

## What does a series' shape say before any rule is chosen?

A forecaster at any product company reads the shape first; every later choice depends on it.

### Q1. Which line reads the three series right?

*Level L1 · asked in analytics screens at e-commerce and logistics companies.*

a) A carries a season only; B a trend only; C both
b) A carries a trend only; B a season only; C both
c) A carries a trend only; B noise only; C a season only
d) A carries both; B a season only; C a trend only

### Q2. What do naive and the seasonal copy forecast for series B's week 13?

*Level L1 · asked in analytics screens at quick-commerce companies.*

a) Naive 70, seasonal copy 100
b) Naive 100, seasonal copy 70
c) Naive 70, seasonal copy 130
d) Naive 100, seasonal copy 100

### Q3. Series C repeats as it climbs, so a copy of four weeks back runs 8 low every time: which forecast fixes it?

*Level L3, a design call · asked in product-company screens.*

a) Naive: the last value, since it already carries the climb
b) The copy from four weeks back, plus the 8 each repeat adds
c) The mean of the last four values, which smooths the repeat
d) The copy from eight weeks back, two repeats earlier

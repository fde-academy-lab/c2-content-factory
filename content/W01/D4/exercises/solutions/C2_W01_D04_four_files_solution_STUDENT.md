# Day 4 solution, M1. Four files, two numbers each

| Dataset | Mean | Median | Reading |
|---|---|---|---|
| P | Rs 42,000 | Rs 39,500 | Mildly right-skewed. Mean is 1.06 times the median, normal for money. |
| Q | Rs 88,000 | Rs 12,000 | Strongly right-skewed. Mean is 7.3 times the median, so something very large is in there. |
| R | Rs 6,400 | Rs 6,350 | Roughly even. The two agree to within one percent. |
| S | Rs 3,100 | Rs 9,800 | Left-skewed. Mean is a third of the median, so something very small pulls down. |

1. **Q.** The mean sits seven times above the median, which one or a few enormous values will do and almost nothing else will.
2. **S**, because a mean *below* the median means the tail is on the low side.
3. **P and R.** In both, mean and median sit close together, so the shape is roughly even and either statistic describes it. Report the count alongside regardless.
4. Realistic causes of a left tail in an order book: refunds and chargebacks recorded as negative amounts, cancelled orders left in at zero, or a partial-payment field where a subset settled at a fraction of the invoice. The general shape is a floor that a subset of orders piles up against or falls below.

**Where your own file sits.** Kalpa's profiled file has a mean of Rs 12,753.30 against a median of Rs 1,910, a ratio of 6.68. It is dataset Q, and more extreme than Q.

**Where this shows up.** Comparing mean to median is the cheapest data-quality check that exists. It is one line, it needs no chart, and it runs on a column you have never seen.

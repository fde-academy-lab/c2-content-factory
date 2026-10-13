# Which scores can the planner trust, and which way does each rule's error run?

This set applies two of the day's topics to chapter 6, the thirteen hidden weeks: holding out, MAE
and MAPE in the business's units, and beating the baseline, with the vendor curve tested. At
Flipkart's Lucknow fulfilment centre, the last thirteen weeks, 29 June to 21 September 2026, were
hidden and every rule forecast them from the week of 22 June 2026. On those weeks the house bot (the
seasonal naive, a copy of the same week last year) missed by 9,831 shipments a week, festival-aligned
and finance's rule by 6,615, naive by 14,923 and the vendor's curve by 16,400. A late shipment costs
Rs 25 and an idle packer-shift Rs 650, which is Rs 5.42 for each shipment of spare capacity.
Illustrative case: the company is real, the situation and the data are synthetic, built for this class.

**Who needs the answer.** The regional operations head, who says yes or no to a model before a shift
is booked: a score read wrongly sends the wrong forecast to the plan.

**The questions on the way.**

- Why does a short piece of code score naive better than the honest test did?
- Which way does each rule's error run?
- What do priced misses say the plan should do?

**What you post,** in this set's thread in the cohort channel: three letters in item order, with no
spaces, in this shape:

```
Post exactly this shape: xxx
```

---

## Can the score itself be trusted?

Every forecasting review at a product company starts by checking how a score was made before
reading it.

### Q1. This code prints 13,654 for naive, where the honest test gave 14,923: what is wrong with it?

*Level L3 · asked in data-science screens at e-commerce and AI companies.*

```python
naive = y.shift(1).loc[hold.index]           # each hidden week's week before
print((naive - hold).abs().mean())           # 13,654
```

`shift(1)` slides the series down one row, so each week's row holds the week before's value. Which
line names the defect?

a) It feeds each hidden week the week before's actual, unknown on 22 June
b) shift(1) should be shift(52), since naive copies the same week last year
c) The score should square each miss first, as RMSE, the root mean squared error, does
d) loc[hold.index] starts the hidden weeks one week late, on 6 July

## Which way does each rule's error run?

The MAE drops the signs; the error table keeps them. Summed over the thirteen hidden weeks:

| Rule | Shipments forecast too high | Weeks too high | Shipments forecast too low | Weeks too low |
|---|---|---|---|---|
| Festival-aligned | 40,748 | 6 | 45,248 | 7 |
| Vendor's curve | 211,300 | 12 | 1,900 | 1 |

### Q2. Which line reads the direction of the two rules' errors right?

*Level L3 · asked in operations-analytics screens.*

a) Both lean high, since both rules carry a positive MAE on the weeks
b) Festival-aligned leans low by 6,615 a week, the vendor high by 16,400
c) The vendor errs about evenly both ways; festival-aligned errs high almost every week
d) Festival-aligned errs about evenly both ways; the vendor errs high almost every week

## What do priced misses say the plan should do?

The same misses cost different amounts in each direction, which every capacity plan has to price.

### Q3. Priced, the vendor's misses cost Rs 11.9 lakh and festival-aligned's Rs 13.5 lakh: which conclusion holds?

*Level L5, a design call · asked in operations-analytics screens.*

a) Send the vendor's curve, since its misses are the cheaper ones
b) Send festival-aligned; erring high is cheaper, so a margin goes above it, sized on purpose
c) Send the average of the vendor's curve and festival-aligned, to split the two errors evenly
d) Keep MAE alone, since pricing the misses adds assumptions about the costs

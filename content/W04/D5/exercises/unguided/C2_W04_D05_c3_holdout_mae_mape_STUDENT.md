# Holding out; MAE and MAPE in the business's units: how does the invented hostel mess score a rule before trusting it?

This set practises chapter 3, holding out, MAE and MAPE in the business's units, at the hostel mess
(invented), where every number is invented. Item 1 is the chapter's live check; the rest are sat in
the lab's opening twenty minutes. Two scores, each defined once: **MAE**, the mean absolute error,
averages the misses' sizes in the unit the mess orders in, kg; **MAPE**, the mean absolute percentage
error, averages each miss as a percent of what was used. A **miss** here is the forecast minus what
was used, so a positive miss is rice cooked and thrown away. At the mess a kilogram short, when students
go without, costs more than a kilogram cooked and thrown away.

**Who needs the answer.** The mess manager (invented), who wants to know how wrong the rice order
could be, and in which direction, before trusting a rule.

**The questions on the way.**

- How far off is the rule, and which way does it lean?
- Which days do you hide to judge a weekly order?
- Which score goes to the manager, and which compares two messes?
- Do two rules with the same MAE cost the same?

**What you post,** in this set's thread in the cohort channel: four letters in item order, with no
spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

## How far off, and which way?

### Q1. Five hidden days missed by 12, -8, 5, -15 and 6 kg: what is the MAE, and which way does the rule lean?

*Level L2 · the chapter's live check.*

a) 9.2 kg, and no lean: the signed misses add to zero
b) 9.2 kg, leaning short: two of the misses are negative
c) 0 kg, since the signed misses cancel each other out
d) 46 kg, the five misses' sizes added together

### Q2. At the mess (invented), rule P missed two days by +10 and +10 kg, rule Q by +10 and -10 kg: which line is right?

*Level L2 · asked in analytics screens.*

a) Q is the better rule, since its two misses cancel to zero
b) P is the better rule, since it never leaves the mess short
c) Their MAEs differ, since P's misses all point one way
d) Same MAE, 10 kg; P leans over, so their costs differ

## Which days, and which score?

### Q3. The mess (invented) orders rice every Monday for the next seven days: to judge a rule on its last 28 days, which days do you hide?

*Level L3, a design call · asked in product-company screens.*

a) Seven days at random, so that every weekday is tested once
b) The seven busiest days, since a miss there costs the mess the most
c) The last seven, all forecast from the day before them, the origin
d) The last three, as many days as the chai stall hid for its milk

### Q4. Which score do you give the mess manager (invented), and which do you use to compare this mess with one twice its size?

*Level L4, a design call · asked in analytics screens at e-commerce companies.*

a) Percent for the manager, since a percent is easy to say aloud; kg for the comparison
b) The MAE in kg for the manager, since kg can be priced; MAPE to compare the messes
c) The MAE in kg for both, since a percent divides by the rice used and can explode
d) MAPE for both, since a percent carries no unit and suits every reader alike

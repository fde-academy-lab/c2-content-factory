# How does the same-week-last-year rule score when you build it by hand and hide three weeks?

At Flipkart's Lucknow fulfilment centre, the planner must book packer shifts for the eight festive
weeks beginning 12 October to 30 November 2026, and the tournament's house bot copies the same week
of last year. Diwali fell on Thursday 31 October 2024 (the week of 28 October) and on Monday 20
October 2025 (the week of 20 October). Illustrative case: the company is real, the situation and the
data are synthetic, built for this class.

The trainer builds this set with the room. The first item is fully worked, the second half worked,
and the third is yours. Each item carries its level, from L1 for a count by hand to L6 for an
interview question, and where such items are asked: a screen is an interview round, and a GCC, a
global capability centre, is a multinational company's own technology centre in India.

**Who needs the answer.** The FC planner, who may send only a rule that has been scored on weeks it
never saw. A rule judged on how it sounds books packers for the wrong weeks.

**The questions on the way.**

- Which week does the rule copy, and what does it forecast?
- What does it score on three hidden weeks?
- Which rule should take over on festive weeks?

The set uses three words, each defined once here. **Same week last year** forecasts a week by copying the week 52 weeks
earlier. **A miss** is the forecast minus what shipped: positive is too high. **MAE**, the mean
absolute error, drops each miss's sign and averages the misses.

These are twelve of the centre's 104 weeks, shipments in each week beginning on the Monday shown.

| Week beginning | Shipments | Week beginning | Shipments |
|---|---|---|---|
| 7 Oct 2024 | 312,900 | 29 Sep 2025 | 331,200 |
| 14 Oct 2024 | 401,000 | 6 Oct 2025 | 418,200 |
| 21 Oct 2024 | 356,200 | 13 Oct 2025 | 369,000 |
| 28 Oct 2024 | 296,900 | 20 Oct 2025 | 308,900 |
| 4 Nov 2024 | 180,600 | 27 Oct 2025 | 188,600 |
| 11 Nov 2024 | 212,700 | 3 Nov 2025 | 227,900 |

**What you post,** in this set's thread in the cohort channel: three letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxx
```

---

## How does a planner build and score a forecasting rule by hand?

This comes up whenever a team proposes a forecast: the first test is a rule anyone can work on paper,
scored on weeks it never saw.

### Q1. Which week does the rule copy for the week of 13 October 2025, and what does it forecast?

*Level L1 · asked in e-commerce and quick-commerce analytics screens.* Worked: count 52 weeks back
from Monday 13 October 2025 and land on Monday 14 October 2024, which shipped 401,000. The rule
forecasts 401,000. Which line matches the working?

a) 21 October 2024, 356,200 shipments
b) 6 October 2025, 418,200 shipments
c) 14 October 2024, 401,000 shipments
d) 14 October 2024, 417,040 shipments

### Q2. Stand in the week of 6 October 2025 and hide the next three weeks: what MAE does the rule score on them?

*Level L2 · asked in every analytics screen.* The hidden weeks are 13, 20 and 27 October 2025. The
copy needs nothing after 6 October, so hiding them only stops you peeking at what they shipped. Half
worked: the rule's copies are 401,000, 356,200 and 296,900, and what shipped was 369,000, 308,900 and
188,600. The first miss is 32,000 too high. Work
the other two misses, drop the signs, and average the three. Which MAE is right?

a) 15,633
b) 62,533
c) 187,600
d) 47,300

### Q3. Every miss runs too high, most of all after Diwali's week: which rule should replace it on festive weeks?

*Level L2, a design call · asked in product-company screens.* Yours to do: read where the misses
came from before choosing.

a) Naive: repeat the week before, whatever it shipped
b) The same calendar copy, raised by 4 percent for growth
c) Festival-aligned: the same distance from Diwali
d) The average of the same calendar week in both years

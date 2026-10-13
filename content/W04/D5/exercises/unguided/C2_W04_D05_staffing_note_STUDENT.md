# Which forecast books the festive shifts, how many a week, and what would make the plan wrong?

This set applies the good-enough call and the forecast note to chapter 7, with two of the morning's
topics beside it: trend and seasonality, for the window a growth figure is read against, and the
baselines, for the calendar copy. At Flipkart's Lucknow fulfilment centre, the planner must book
packer shifts for the eight weeks beginning 12 October to 30 November 2026. Diwali falls on Sunday 8
November 2026, so its week begins 2 November. The festive sale runs in the third and second weeks
before Diwali's week, and the peak comes with it. Illustrative case: the company is real, the
situation and the data are synthetic, built for this class.

What the morning found:

| Forecast | Hidden-week MAE | Its busiest 2026 week | Eight weeks against 13 Oct to 1 Dec 2025 | Against 29 Sep to 17 Nov 2025 |
|---|---|---|---|---|
| Seasonal naive, the house bot: same week last year | 9,831 | 5 October | the same | 13.0 percent below |
| Finance's rule, the bot plus 4 percent | 6,615 | 5 October | 4.0 percent above | 9.5 percent below |
| Vendor's curve | 16,400 | 5 October | 22.0 percent above | 6.1 percent above |
| Festival-aligned, plus 4 percent | 6,615 | 19 October | 19.5 percent above | 4.0 percent above |

The plan covers 12 October to 30 November, so a forecast whose busiest week is 5 October books its
rush before the first week staffed. A packer packs about 120 shipments a shift. A late shipment costs Rs 25 and an idle shift Rs 650,
which is Rs 5.42 a shipment, so the plan prices its error bar in each direction. Festival-aligned
forecasts 434,928 shipments for the week of 19 October 2026.

**Who needs the answer.** The regional operations head, who signs the shift plan and answers for
late parcels in the busiest weeks.

**The questions on the way.**

- Which forecast goes to the plan?
- How many packer shifts does the busiest week need?
- Which change would move the plan's peak?
- Against which window is finance's 4 percent measured?
- What does the note say, line by line?

**What you post,** in this set's thread in the cohort channel: four letters in item order, with no
spaces, in this shape, then the note:

```
Post exactly this shape: xxxx
```

---

## Which forecast, and how many shifts?

This is the call every capacity planner makes before a peak: one forecast, its error bar priced in
each direction, and a count of people.

### Q1. Which forecast goes to the staffing plan?

*Level L5, a design call · asked in operations and supply-chain analytics screens.*

a) The vendor's curve, since its hidden-week misses cost least
b) Finance's rule, since it tied for the lowest hidden-week MAE
c) Festival-aligned, peak on 19 October
d) The midpoint of finance and the vendor, 13 percent up

### Q2. How many packer shifts does the week of 19 October 2026 need under the plan?

*Level L5 · asked in operations analytics screens.*

a) 3,624
b) 4,150
c) 2,575
d) 3,625

## What would make the plan wrong?

A plan names the fact that would move it, so the person who sees that fact knows to call.

### Q3. Suppose, as a hypothetical, this year's sale opens four weeks before Diwali instead of three: what changes in the plan?

*Level L4, a design call · asked in product-company screens.*

a) Nothing: festival-aligned already moves with Diwali
b) Copy by distance from the sale, which the peak follows
c) Add 4 percent more to every week of the window
d) Switch to the vendor's curve, which plans a higher peak

### Q4. Finance's eight weeks sit 4 percent above the same calendar weeks of 2025: where do they sit against the 2025 weeks counted from Diwali?

*Level L3 · asked in analytics screens.*

a) 9.5 percent below, missing the peak weeks
b) 4.0 percent above, the same as the calendar window
c) Equal to them, since both windows are eight weeks
d) 22.0 percent above, as the vendor's curve is

## What does the staffing note say?

Write five lines to the regional operations head, in this order:

| Line | What it says |
|---|---|
| First | The claim as the title: how many shifts, for which weeks, from which forecast |
| Second | Where the peak falls, and why: distance from Diwali, with the week named |
| Third | The error bar: the typical miss in shipments priced in each direction, the peak week's range, and the honest record on 2025's festival, with no growth added |
| Fourth | Three facts that would move the number, each with its check |
| Fifth | One line to finance and one to the vendor's sponsor, each conceding the true part first |

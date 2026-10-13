# Beating the baseline; the vendor curve tested; the good-enough call and the forecast note: which forecast earns trust, and what goes in the note?

This set practises chapter 4, which teaches two of the day's topics: beating the baseline, with the
vendor curve tested, and the good-enough call and the forecast note. Item 1 is the chapter's live
check on the chai stall (invented); item 2 moves to Flipkart's Lucknow fulfilment centre, an
illustrative case (the company is real, the situation and the data are synthetic, built for this
class); item 3 returns to the stall. Items 2 and 3 are sat in the lab's opening twenty minutes.

**Who needs the answer.** The stall's owner (invented), offered a "model" by a nephew, and Flipkart's
regional operations head, offered models by three teams: each must decide what earns a place in the
order before anything is booked.

**The questions on the way.**

- Which forecast for day 5 do you trust, and why?
- Which of three models earns a place over the day's best rule?
- Which first line does the note to the milkman (invented) carry?

**What you post,** in this set's thread in the cohort channel: three letters in item order, with no
spaces, in this shape:

```
Post exactly this shape: xxx
```

---

## Which forecast earns trust?

### Q1. The stall (invented) sold 100, 104, 98 and 110 cups on four days; a curve through all four says 168 for day 5 and the straight line says 109: which do you trust, and why?

*Level L2 · the chapter's live check.*

a) The curve, since it fits all four days with an error of 0 cups
b) Neither yet: order naive's 110 until one wins on unseen days
c) Their average, 138.5 cups, since it splits the difference
d) Neither, since four days are far too few for any forecast at all

### Q2. At Flipkart Lucknow, festival-aligned scores 6,615 shipments a week on the thirteen hidden weeks and the house bot 9,831; three teams bring a model each: which line gives the right call on all three?

*Level L5, a design call · asked in product-company and GCC screens.*

A model earns its place only on weeks it never saw, only by beating the day's best rule, and only by
enough to pay for itself: about 120 shipments make a shift, and a late shipment costs Rs 25.

| Team | Model MAE | Scored on | Also |
|---|---|---|---|
| A | 9,800 | the thirteen hidden weeks | a vendor contract to run it |
| B | 6,000 | the 91 weeks it was fitted to | |
| C | 6,200 | the thirteen hidden weeks, none of them festive | 7 of 13 weeks too high |

Which line is right?

a) Adopt all three: each beats the bot's 9,831
b) Skip A, adopt B, reject C for erring high
c) Skip A, rescore B, retest C on more weeks
d) Adopt A, rescore B, reject C for erring high

## What goes in the note?

### Q3. At the stall (invented), the seasonal naive beat the nephew's mean on seven hidden days, 4.0 cups a day against 12.4, and orders 3 cans a weekday and 2 on Sunday: which first line does the note to the milkman carry?

*Level L4, a design call · asked in analytics screens.*

a) "3 cans a day Monday to Saturday, 2 on Sunday, from last week's same day"
b) "Forecasting analysis for the coming week, with the method and its scores"
c) "The nephew's model fits 100 percent of the history it was built on"
d) "The seasonal naive scored 4.0 cups on seven hidden days, the best rule"

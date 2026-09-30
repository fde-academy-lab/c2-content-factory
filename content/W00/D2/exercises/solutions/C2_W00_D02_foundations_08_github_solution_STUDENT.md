<!-- The finished README for mini project 1, the solution to the Chapter 8 guided exercise. Its Result is what the Chapter 1 guided exercise's notebook prints for its ten practice rows, which the Chapter 7 workbook also holds. -->
# w00-diagnostic-python
Cleans ten Kalpa order rows and totals paid revenue by tier, for Kalpa Retail's Q1 to Q2 revenue question.

## What it shows
Every amount arrives as text, so one function, `to_amount`, converts each amount or raises, and the loop turns a raise into a counted rejection in place of a crash. `'Rs 900'` is rejected with `'n/a'` and the empty amount, because a person reads it easily and `float()` cannot. Revenue is totalled by tier for paid orders only, a zero amount stays in because the test is whether the text converts, and an `assert` proves the tier totals add up to the clean amounts.

## How to run
Open the repository in a Codespace, open `notebook.ipynb`, restart the kernel and run every cell from the top; the three cells need nothing beyond Python.

## Result
Paid revenue by tier from the ten rows, with three rows rejected and one cancelled order left out:

| tier | paid revenue |
|---|---|
| Plus | Rs 3,350 |
| Basic | Rs 2,150 |
| All tiers | Rs 5,500 |

Rejected: K-103, whose amount is `'n/a'`, K-107, whose amount is `''`, and K-109, whose amount is `'Rs 900'`. The cancelled order, K-105 at Rs 800, stays out of every total, and the assert holds: the two totals add up to the Rs 5,500 of clean paid amounts.

## What I would do next
The rows are typed into the first cell, so next month's orders need an edit; reading them from `orders.csv` would let the same notebook run on any month's file, which is where mini project 6 takes it.

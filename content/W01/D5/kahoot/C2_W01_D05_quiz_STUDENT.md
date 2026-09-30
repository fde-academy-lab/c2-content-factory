# Kahoot, Week 1 Friday

Six items, ungraded, scored on correctness and speed together: five on the week's method and the
return question from Thursday.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. A fresh export lands an hour before Meera's call. Which step comes third?
*Tests: the order of the pipeline, and where the reconciliation sits in it.*

- Decompose the change along the revenue tree, segment by segment
- Reconcile counts and rupees against Finance's control totals  <- correct
- Profile each field for present, convertible and distinct counts
- Run the shuffle test on the gap that the note will lead with

---

## Q2. Which check catches rows the migration posted twice?
*Tests: a duplicate is found by the identity rule, not by eye or by a total.*

- Sorting by amount and reading the largest orders at the top
- Comparing the mean order against the median order, per quarter
- Distinct order ids against the number of rows in the file  <- correct
- Checking every field is present on every row of the export

---

## Q3. Your pass reports input 180, clean 171, rejected 9. What still has to reconcile?
*Tests: counts reconcile rows; only rupees prove the values survived the conversion.*

- Each quarter's rupees against the control total  <- correct
- Nothing more, since every row is now accounted for
- The median order, against last week's median order
- The number of segments, against the number of cities

---

## Q4. Anand asks for "a typical order" from a file with a handful of corporate orders in it. Which number?
*Tests: the median for a typical order in a skewed file, the mean for anything that must reconcile.*

- The mean, because it uses every order in the file
- The mean without the corporate orders, which are outliers
- The largest consumer order, as a safe upper figure
- The median, with the corporate orders named beside it  <- correct

---

## Q5. A shuffle test gives p = 0.04. What is 0.04 a share of?
*Tests: the p-value is a share of chance-only worlds, never the chance the finding is wrong.*

- Chance-only worlds with a gap at least as large  <- correct
- Findings like this one that turn out to be wrong later
- Customers whose orders moved between the two quarters
- Orders that the shuffle moved from one segment to the other

---

## Q6. Return from Thursday. Revenue rose after a discount. Which question comes before calling it a success?
*Tests: a fair comparison needs a like-for-like group that did not get the discount.*

- How large was the discount, as a share of the price?
- How much did revenue rise, in rupees rather than percent?
- Compared with whom: a similar group that did not get it?  <- correct
- Did the p-value on the rise come in under 0.05?

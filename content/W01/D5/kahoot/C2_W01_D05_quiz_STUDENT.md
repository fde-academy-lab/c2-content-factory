# Kahoot, Week 1 Friday

Eight items, ungraded, scored on correctness and speed together.

---

## Q1. A fresh export lands an hour before Meera's call. Which step comes third?
*Tests: the order of the pipeline, and where the reconciliation sits in it.*

- Decompose the change along the revenue tree, segment by segment
- Reconcile counts and rupees against Finance's control totals  <- correct
- Profile each field for present, convertible and distinct counts
- Run the shuffle test on the gap that the note will lead with

---

## Q2. The dashboard runs Rs 20 lakh above Finance. Which check do you run first?
*Tests: the design call on a fresh export; the cheapest check that catches the commonest cause goes first.*

- A rupee bridge by month against Finance, about half an hour
- Distinct order ids against the number of rows, one cell  <- correct
- Every order matched to Finance's ledger, most of a day
- A shuffle test on the gap, 2,000 runs, a few minutes

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

## Q6. No control total came with the export. What replaces the rupee check today?
*Tests: the design call when the reference is missing: a check that needs nothing outside the file, and the gap said aloud.*

- Nothing, since without Finance's total no check is possible
- A shuffle test, since it needs no outside number at all
- The median order, compared with last quarter's median
- Every value summed or logged; the note says unreconciled  <- correct

---

## Q7. Four segments moved and you have time for one shuffle test. Which gap do you test?
*Tests: count before rate; one test on the branch that moved on enough orders beats four tests.*

- The segment with the largest percentage move, whatever its count
- The branch that moved on the most orders, customers flat  <- correct
- All four at 0.05, and lead with the smallest p-value
- The corporate segment, since it carries the most rupees

---

## Q8. Return from Thursday. Revenue rose after a discount. Which question comes before calling it a success?
*Tests: a fair comparison needs a like-for-like group that did not get the discount.*

- How large was the discount, as a share of the price?
- How much did revenue rise, in rupees rather than percent?
- Compared with whom: a similar group that did not get it?  <- correct
- Did the p-value on the rise come in under 0.05?

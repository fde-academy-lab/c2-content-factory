# Kahoot, Week 1 Day 2

Six items plus one return question from Monday, one level up. Ungraded, scored on correctness and
speed together.

---

## Q1. What is rung one of the investigation ladder?
*Tests: the order of the rungs, which is the whole case.*

a) Decompose revenue into its factors and see which moved most
b) Confirm the drop is real  <- correct
c) Ask the business what they think caused it before touching data
d) Split the numbers by segment to find where the fall sits

---

## Q2. Revenue per customer fell 8 percent. Which two numbers next?
*Tests: a rate is a ratio, so both halves of it have to be looked at.*

a) Last year's figure and the industry benchmark for the same quarter
b) The forecast and the actual, so the size of the miss is known first
c) Orders per customer and revenue per order  <- correct
d) The largest customer and the smallest, to see the range involved

---

## Q3. Q1 ran 13 weeks and Q2 ran 11. Is the comparison fair?
*Tests: like with like, which is the rung most often skipped.*

a) Yes, because both are complete quarters as the business defines them
b) Yes, if you compare rates rather than the totals themselves
c) Only for revenue, since a rate already divides out the difference
d) No, and per-week figures or matched windows are what fix it  <- correct

---

## Q4. `result = revenue_for(seg)` holds `None`. What went wrong?
*Tests: return against print, and why a function that prints cannot be built on.*

a) The function ends in `print` rather than `return`  <- correct
b) The segment name was misspelled, so no rows matched the filter
c) The function raised an exception that was caught and swallowed
d) `revenue_for` was defined after the line that calls it in the file

---

## Q5. A segment has median Rs 1,200 and a range of Rs 80,000. Say what?
*Tests: a typical value and a spread describe different things.*

a) The median must have been computed on the wrong column entirely
b) Most orders are small and at least one is very much larger  <- correct
c) The segment has too few orders in it to describe at all
d) The mean will be close to Rs 1,200 because the median is close

---

## Q6. Customers flat, orders per customer down in one segment. Say it.
*Tests: a hypothesis is stated as a hypothesis, with its test beside it.*

a) That segment's customers have left and been replaced by new ones
b) Something changed for that segment, and this would settle it  <- correct
c) Acquisition is working and retention is not, across the business
d) The segment definition changed between the quarters being compared

---

## Return question from Monday, one level up

## Q7. The mean doubled and the median did not move. First check?
*Tests: Monday's reveal, now as a diagnostic move rather than a demonstration.*

a) Recompute the mean, because a doubling usually means a code error
b) Compare against the same period last year to see if it is seasonal
c) Sort the amounts and read the top of the list  <- correct
d) Report both numbers and let the stakeholder decide which to use

---

## Trainer note on the set

Q3 is the item the room most often gets wrong at speed, because "compare rates" sounds like the
careful answer and is not: a rate over an 11-week window and a rate over a 13-week window are
still two different things. Q7 is the return question and it is worth ten seconds afterwards,
because the move it asks for is the one Wednesday opens on.

# Wednesday's Kahoot: windows, ranks and the tie

Ungraded. Seven questions.

## Q1. Rs 9,000, Rs 7,500, Rs 7,500, Rs 6,200. What does RANK return?

a) 1, 2, 3, 4
b) 1, 2, 2, 3
c) 1, 2, 2, 4 <- correct
d) 1, 1, 3, 4

## Q2. PARTITION BY resets what?

a) The sort order of the whole result set
b) The numbering, for each group <- correct
c) The rows the query returns at all
d) The aggregate used inside the window

## Q3. `lag(spend)` on a customer's first month returns what?

a) NULL, since there is no previous row <- correct
b) Zero, since nothing was spent before then
c) The customer's own first month value again
d) An error naming the missing partition row

## Q4. Which ORDER BY makes a running total reproducible?

a) Any order, totals do not depend on it
b) One whose values cannot tie <- correct
c) The order the rows were inserted in
d) Descending order, which is deterministic

## Q5. A window function inside WHERE. What happens?

a) It filters once the window has been computed
b) Refused, WHERE runs before the window <- correct
c) It works only when PARTITION BY is present
d) Refused, since windows only work in ORDER BY

## Q6. The business says ties rank the same. Which function?

a) ROW_NUMBER, which gives exactly N rows
b) DENSE_RANK, which never skips a number
c) RANK, which shares and then skips <- correct
d) Any of them, with ORDER BY on the id

## Q7. Return question, one level up

Yesterday your LEFT join grew the row count. Name the cause and the check.

a) Duplicate rows in the left table, checked with DISTINCT
b) A missing WHERE clause, checked by reading the query plan
c) A wrong join type, checked by switching it to an INNER
d) A fan-out on the key, checked by counting rows <- correct

## Trainer note

Q1 is where the room splits. Anybody answering b has `DENSE_RANK` in mind, and the follow-up worth
asking is what position 4 is telling you that position 3 would not: that three members are ahead,
which is true, rather than that two levels are ahead, which is a different question.

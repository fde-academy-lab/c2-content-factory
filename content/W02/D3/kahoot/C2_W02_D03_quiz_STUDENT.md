# Kahoot, Week 2 Wednesday

Eight items, ungraded, scored on correctness and speed together. Q8 returns to Tuesday's join one
level up, on today's question. Every member and amount in Q1 is invented for the quiz.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. Four invented members spent Rs 900, Rs 700, Rs 700 and Rs 500. What do RANK, DENSE_RANK and ROW_NUMBER give?
*Tests: the three tie rules side by side on one small tie.*

- RANK 1,2,2,3; DENSE_RANK 1,2,2,4; ROW_NUMBER 1,2,3,4
- RANK 1,2,2,4; DENSE_RANK 1,2,2,3; ROW_NUMBER 1,2,3,4  <- correct
- RANK 1,2,2,4; DENSE_RANK 1,2,2,3; ROW_NUMBER 1,2,2,4
- RANK 1,2,3,4; DENSE_RANK 1,2,2,3; ROW_NUMBER 1,2,2,3

---

## Q2. A ranking uses PARTITION BY segment. What does the partition reset?
*Tests: the partition sets the group the calculation restarts in.*

- The order in which the query returns its final rows
- The number of rows the query returns at the end
- Nothing, since it only sorts rows inside each segment
- The calculation, which starts again in each segment  <- correct

---

## Q3. LAG(spend) OVER (PARTITION BY customer_id ORDER BY month) on a member's first month returns what?
*Tests: LAG reads the previous row of the partition, and a first row has none.*

- NULL, since the member has no earlier row  <- correct
- Zero, since no spend was recorded before it
- The last month of the member sorted above
- The same month's spend, repeated once more

---

## Q4. Which ORDER BY makes a running total over Q2 orders deterministic, one step per order?
*Tests: a running total needs an order with no ties in it.*

- ORDER BY order_date, since each order has a date
- ORDER BY amount DESC, so the largest orders lead
- ORDER BY order_date, order_id, a unique pair  <- correct
- No ORDER BY, so the rows count once in any order

---

## Q5. A top ten per city uses ROW_NUMBER() OVER (PARTITION BY city ORDER BY revenue DESC). Two Pune members tie at tenth, and Monday's list differs from Tuesday's with no new orders. Why?
*Tests: ROW_NUMBER cuts a tie arbitrarily, so a list without a tiebreaker does not repeat.*

- A late payment changed one member's Q2 revenue overnight
- PARTITION BY restarted the count at a different city
- DESC puts a NULL revenue first on some runs and last on others
- Tied members are cut arbitrarily; add a tiebreaker  <- correct

---

## Q6. The business wants tied members ranked the same and nobody at the line dropped. Which function?
*Tests: the tie rule is a business choice written as a function name.*

- RANK, since ties share a place and the tie ships  <- correct
- DENSE_RANK, since tied members share one number
- ROW_NUMBER, since the list is the size it was asked
- Any of the three, since ties never occur in rupees

---

## Q7. A member bought in July, nothing in August, then in September. What does a partitioned LAG compare September with?
*Tests: LAG reads the previous row, which is not always the previous month.*

- August, read as zero, so September counts as a rise
- Nothing, since LAG returns NULL after any gap
- July, as if it were last month  <- correct
- The September of the member sorted just above him

---

## Q8. Tuesday's LEFT JOIN of orders to payments took 1,000 rows to 1,450. You sum revenue per member on it to rank them. What goes wrong?
*Tests: Tuesday's fan-out, one level up: a joined total that ranks the wrong members.*

- Unpaid orders are dropped, so every rank comes out lower
- Orders with several payments repeat; check counts first  <- correct
- Nothing, since RANK ignores rows repeated by a join
- The ranks shift by one, since the join adds a column

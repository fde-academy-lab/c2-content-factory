# Can you make the day's eight calls about the protect list in twenty seconds each?

Eight items, ungraded, scored on correctness and speed together. Seven are today's, and the last is
the return question from Tuesday, one level up. Each item names what it tests, so an item dropped
for time says what was lost. Every member and amount in items 1, 5 and 7 is invented for the quiz.

Today Kalpa Retail's marketing lead asked for each segment's top fifty members by Q2 revenue and a
flag on anyone whose monthly spend fell two months running, and Meera Raghavan, the CEO, asked to see
Q2 accumulate week by week against the plan line. The head of Retail-Plus, who owns the paid
membership tier, asked that members who spent the same be ranked the same and that every list say how
many made it. Q2 is July to September 2026, and revenue is booked revenue, every order at its amount
whatever its status.

**Who needs the answer.** The trainer, closing the day, and every learner writing tonight's queries.
Each item is one of the day's calls made in seconds, and an item most of the room misses is a call
likely to reach Marketing wrong on Monday, so it is the one to say again before the room leaves.

**The questions on the way.**

- What do RANK, DENSE_RANK and ROW_NUMBER give four members with one tie?
- What does PARTITION BY segment restart?
- What does LAG return on a member's first month?
- Which ORDER BY gives a running total one step per order, the same on every run?
- What does ROW_NUMBER do to a tie at the line of a top-four list?
- Which function ranks members who spent the same the same, with the count said?
- What does LAG call "last month" for a member who skipped August?
- Your LEFT join grew the row count: what is the cause, and what is the check?

---

## Q1. Four invented members spent Rs 900, Rs 700, Rs 700 and Rs 500: what do RANK, DENSE_RANK and ROW_NUMBER give?
*Tests: the three tie rules side by side on one small tie.*

- RANK 1,2,2,3; DENSE_RANK 1,2,2,4; ROW_NUMBER 1,2,3,4
- RANK 1,2,2,4; DENSE_RANK 1,2,2,3; ROW_NUMBER 1,2,3,4  <- correct
- RANK 1,2,2,4; DENSE_RANK 1,2,2,3; ROW_NUMBER 1,2,2,4
- RANK 1,2,3,4; DENSE_RANK 1,2,2,3; ROW_NUMBER 1,2,2,3

---

## Q2. A ranking uses PARTITION BY segment: what does the partition restart?
*Tests: the partition sets the group a window's calculation starts again in.*

- The order in which the query returns its final rows to the screen
- The number of rows the query returns once the window has run
- Nothing at all, since it only sorts the rows inside each segment
- The numbering, which starts again at 1 in each segment  <- correct

---

## Q3. LAG(spend) OVER (PARTITION BY customer_id ORDER BY month) on a member's first month returns what?
*Tests: LAG reads the previous row of the partition, and a first row has none.*

- NULL, since the member has no earlier row  <- correct
- Zero, since no spend was recorded before that month
- The last month of whichever member sorts just above
- The same month's spend, read a second time over

---

## Q4. Which ORDER BY gives a running total over Q2's orders one step per order, the same on every run?
*Tests: a running total is repeatable only when its ORDER BY is unique, since rows sharing a value are summed together.*

- ORDER BY order_date, so the orders run in date order
- ORDER BY amount DESC, so the biggest orders come first
- ORDER BY order_date, order_id  <- correct
- No ORDER BY, since a sum adds up in any order at all

---

## Q5. An invented top four is cut with ROW_NUMBER, and the fourth and fifth members spent the same: what happens to the fifth?
*Tests: ROW_NUMBER always ships the line and breaks a tie by whatever else its ORDER BY names.*

- The fifth joins the list too, since the two spent the same amount
- Left off by the tiebreaker, and the list still says four  <- correct
- Both tied members are left off, and the list ships three
- The query stops with an error until the tie is resolved

---

## Q6. The head of Retail-Plus wants members who spent the same ranked the same, with the count said: which function?
*Tests: the tie rule is a business choice written as a function name.*

- RANK, and say how many made it  <- correct
- DENSE_RANK, since its numbers never skip a place on the list
- ROW_NUMBER, with the customer id as a tiebreaker in the ORDER BY
- LIMIT 50 after an ORDER BY on Q2 revenue, biggest first

---

## Q7. An invented member bought in July and September and not in August: what does LAG, partitioned by member and ordered by month, call "last month" for September?
*Tests: LAG reads the previous row, and a month with no order has no row.*

- August, since August is the calendar month before September
- Nothing, since the August row comes back NULL from the window
- June, since LAG reads two months back by default on a monthly table
- July, the member's previous row  <- correct

---

## Q8. Tuesday, one level up: your LEFT join of orders to payments grew the row count; what is the cause, and what is the check?
*Tests: Tuesday's rule that a join is done only when its row count is explained.*

- A LEFT join always adds the unmatched rows twice, so the check is to use INNER
- The payments table holds NULLs, so the check is COALESCE on every amount
- An order with more than one payment row; count rows before and after  <- correct
- The orders table has duplicate ids, so the check is SELECT DISTINCT on the result

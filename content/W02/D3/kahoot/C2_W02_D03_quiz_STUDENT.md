# Can you make the day's eight calls about the protect list in twenty seconds each?

The quiz has eight items, ungraded and scored on correctness and speed together. Seven are today's, and the last is
the return question from Tuesday, one level up. Each item names what it tests, so an item dropped
for time says what was lost. Every member and amount in items 1, 5 and 7 is invented for the quiz.

Today Kalpa Retail's marketing lead asked for each segment's top fifty members by Q2 revenue and a
flag on anyone whose monthly spend fell two months running, and Meera Raghavan, the CEO, asked to see
Q2 accumulate week by week against the plan line. The head of Retail-Plus, who owns the paid
membership tier, asked that members who spent the same be ranked the same and that every list say how
many made it. Q2 is July to September 2026, and revenue is booked revenue, every order at its amount
whatever its status.

**Who needs the answer.** The trainer needs it to close the day, and every learner needs it before
writing tonight's queries. Each item is one of the day's calls made in seconds, and an item most of the
room misses is a call likely to reach Marketing wrong on Monday, so the trainer says it again before
the room leaves.

**The questions on the way.**

- What do RANK, DENSE_RANK and ROW_NUMBER give four members with one tie?
- What does PARTITION BY segment restart?
- What does LAG return on a member's first month?
- Which ORDER BY gives a running total one step per order, the same on every run?
- What does ROW_NUMBER do when the fourth and fifth members of a top four spent the same?
- Which function ranks members who spent the same the same, running past fifty only for a tie at fiftieth?
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
*Tests: what PARTITION BY does to a ranking.*

- The order in which the query returns its final rows to the screen
- The number of rows the query returns once the window has run
- Nothing at all, since it only sorts the rows inside each segment
- The numbering, which goes back to 1 at the start of each segment  <- correct

---

## Q3. LAG(spend) OVER (PARTITION BY customer_id ORDER BY month) on a member's first month returns what?
*Tests: what LAG returns at the start of a partition.*

- NULL, since nothing comes before the member's first row  <- correct
- Zero, since no spend was recorded before that month
- The last month of whichever member sorts just above
- That month's own spend, since LAG falls back to the current row

---

## Q4. Which ORDER BY gives a running total over Q2's orders one step per order, the same on every run?
*Tests: which order gives a running total a step of its own for every order.*

- ORDER BY order_date, so the orders run in the order they were booked
- ORDER BY amount DESC, so the biggest orders take the first steps
- ORDER BY order_date, order_id, so each order holds its own place  <- correct
- No ORDER BY, since a sum comes out the same in any order at all

---

## Q5. An invented top four is cut with ROW_NUMBER ordered by spend and then customer id, and the fourth and fifth members spent the same: what happens to the fifth?
*Tests: what ROW_NUMBER does when a tie falls across the last place a list keeps.*

- The fifth joins the list too, since the two spent the same amount
- The fifth is left off by the customer id, and the list ships four  <- correct
- Both tied members are left off, and the list ships three
- The list ships four, and which of the two makes it changes each run

---

## Q6. The head of Retail-Plus wants members who spent the same ranked the same, with no list running past fifty unless members tie at fiftieth: which function?
*Tests: matching the head of Retail-Plus's rule to a function.*

- RANK, which shares a place at a tie and skips the place after it  <- correct
- DENSE_RANK, since its numbers never skip a place on the list
- ROW_NUMBER, with the customer id as a tiebreaker in the ORDER BY
- LIMIT 50 after an ORDER BY on Q2 revenue, biggest first

---

## Q7. An invented member bought in July and September and not in August: what does LAG, partitioned by member and ordered by month, call "last month" for September?
*Tests: what LAG reads across a month with no order.*

- August, since August is the calendar month before September
- Nothing, since the August row comes back NULL from the window
- June, since LAG reads two months back by default on a monthly table
- July, since LAG reads the member's previous row and August has none  <- correct

---

## Q8. Tuesday, one level up: your LEFT join of orders to payments grew the row count; what is the cause, and what is the check?
*Tests: Tuesday's rule that a join is done only when its row count is explained.*

- Each unpaid order adds a row of NULLs, so the check is an INNER join
- The payments table holds NULLs, so the check is COALESCE on amounts
- An order with two or more payment rows; count rows before and after  <- correct
- The orders table repeats some ids, so the check is SELECT DISTINCT

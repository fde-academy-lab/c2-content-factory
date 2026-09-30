# Can you make the day's eight calls about the Monday suite in twenty seconds each?

Eight items, ungraded, scored on correctness and speed together. Seven are today's, and the last is
the return question from Week 1 Thursday. Each item names what it tests, so an item dropped for time
says what was lost.

Today Anand Iyer, Kalpa Retail's finance controller, asked for the Monday numbers from the warehouse
itself: Kalpa's Postgres database, where the orders table holds one row per order and the customers
table one row per member, with the member's segment. The team rebuilt Week 1's revenue tree
(customers who bought, times orders per customer, times revenue per order) as queries his analyst
can rerun and audit. Q1 is April to June 2026 and Q2 is July to September 2026.

**Who needs the answer.** The trainer, closing the day, and every learner writing tonight's
queries. Each item is one of the day's calls made in seconds, and an item most of the room misses is
a line likely to reach Anand's analyst wrong next Monday, so it is the one to say again before the
room leaves.

**The questions on the way.**

- Which clause does the database run first, WHERE or SELECT?
- Anand wants only the segment-quarters with at least 30 customers; which clause keeps them?
- How many rows does GROUP BY segment, quarter return on today's book?
- What does LIMIT 5 without ORDER BY hand the analyst?
- In a query with two named steps, what can the second step read?
- How do you count the customers who bought in each quarter, in one line?
- Retail-Plus placed 140 orders from 76 customers; what is its orders per customer?
- Week 1's monsoon sale showed a 6 percent lift that the mix of customers made; what would a fair comparison need?

---

## Q1. Which clause does the database run first, WHERE or SELECT?
*Tests: the logical order a query runs in, written one way and run another.*

- SELECT, since it is written first in the query
- They run together, as one step over each row
- WHERE, since rows are kept before columns are picked  <- correct
- Whichever the planner chooses, so the order cannot be known

---

## Q2. Anand wants only the segment-quarters with at least 30 customers on his sheet; which clause keeps them?
*Tests: WHERE against HAVING, and why WHERE cannot test a count.*

- HAVING count(DISTINCT customer_id) >= 30  <- correct
- WHERE count(DISTINCT customer_id) >= 30
- ORDER BY the count and LIMIT to the groups at the top
- A CASE in SELECT that prints the thin groups' counts as zero

---

## Q3. On today's book, how many rows does GROUP BY c.segment, o.quarter return for orders, customers and rupees?
*Tests: predicting a result's grain before running it: four segments times two quarters.*

- 2, one row for each quarter of the book
- 4, one row for each of the four segments
- 1,000, one row for every order on the book
- 8, one per segment and quarter  <- correct

---

## Q4. The analyst's audit sample is five delivered Q2 app orders, pulled with LIMIT 5 and no ORDER BY; which five does it return?
*Tests: what the database guarantees about row order: nothing without ORDER BY.*

- The five with the smallest order ids, as on the first run
- Whichever five it reaches first; a rerun can differ  <- correct
- The five most recent orders, since new rows come first
- Five chosen at random, so every run draws a new sample

---

## Q5. A query opens WITH q1 AS (Q1's leaves per segment), q2 AS (a step that reads q1); what can the step q2 read?
*Tests: reading named steps from the top down: each step sees the tables and the steps above it.*

- Only the warehouse's tables, never another step
- Only q1, since a step can read nothing else
- The warehouse's tables and q1, the step above it  <- correct
- Every step in the query, including the steps below it

---

## Q6. Last week's Python loop counted the customers present in each quarter; which SQL line does the same?
*Tests: counting customers who bought, each once, against counting order rows.*

- count(DISTINCT customer_id) with GROUP BY quarter  <- correct
- count(*) AS customers with GROUP BY quarter
- count(customer_id), which skips missing ids, per quarter
- count(DISTINCT order_id) with GROUP BY quarter

---

## Q7. Retail-Plus placed 140 orders from 76 customers in Q2; which orders per customer goes on Anand's sheet?
*Tests: integer division, and the check that multiplies a ratio back.*

- 1, as count(*) divided by the distinct count prints it
- 2, the nearest whole number of orders
- 0.54, customers over orders
- 1.84, which multiplies back to the 140 orders  <- correct

---

## Q8. Week 1 Thursday: the monsoon sale's 6 percent lift came from who got it; what would a fair comparison need?
*Tests: the return question from Week 1 Thursday, one level up: a comparison fair on mix.*

- A deeper discount, so that the lift shows more clearly
- Like for like: each segment apart, or a held-back group  <- correct
- The same comparison over a longer window before and after
- The same sale at Diwali, run for a larger share of the base

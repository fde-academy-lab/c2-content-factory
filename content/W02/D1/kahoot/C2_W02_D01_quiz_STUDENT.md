# Can you make the day's eight calls about the Monday suite in twenty seconds each?

Eight items, ungraded, scored on correctness and speed together. Seven are today's, and the last is
the return question from Week 1 Thursday. Each item names what it tests, so an item dropped for time
says what was lost.

Today Anand Iyer, Kalpa Retail's finance controller, asked for the Monday numbers from the warehouse
itself: Kalpa's Postgres database, where the orders table holds one row per order and the customers
table one row per customer, with the customer's segment, one of four: Business, Retail-Core,
Retail-Plus and Student. The team rebuilt Week 1's revenue tree (customers who bought, times orders
per customer, times revenue per order) as queries his analyst can rerun and audit. Q1 is April to June 2026 and Q2 is July to September 2026.

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
- Week 1's monsoon sale showed a 6 percent lift that came from which customers got the discount; what would a fair comparison need?

---

## Q1. Which clause does the database run first, WHERE or SELECT?
*Tests: the logical order a query runs in, written one way and run another.*

- SELECT, since it is written first in the query
- They run together, as one step over each row
- Whichever the planner chooses, so the order cannot be known
- WHERE, since rows are kept before columns are picked  <- correct

---

## Q2. Anand wants only the segment-quarters with at least 30 customers on his sheet; which clause keeps them?
*Tests: WHERE against HAVING, and why WHERE cannot test a count.*

- WHERE count(DISTINCT customer_id) >= 30
- HAVING count(DISTINCT customer_id) >= 30  <- correct
- ORDER BY the count and LIMIT to the groups at the top
- A CASE in SELECT that prints the thin groups' counts as zero

---

## Q3. On today's book, how many rows does GROUP BY c.segment, o.quarter return for orders, customers and rupees?
*Tests: predicting a result's grain before running it: four segments times two quarters.*

- 8, one row for each segment in a quarter  <- correct
- 2, one row for each quarter of the book
- 4, one row for each of the four segments
- 1,000, one row for every order on the book

---

## Q4. The analyst's audit sample is five delivered Q2 app orders, pulled with LIMIT 5 and no ORDER BY; which five does it return?
*Tests: what the database guarantees about row order: nothing without ORDER BY.*

- The five with the smallest order ids, as on the first run
- The five most recent orders, since new rows come first
- Whichever five it reaches first, and a rerun can differ  <- correct
- Five chosen at random, so every run draws a new sample

---

## Q5. A query opens WITH q1 AS (Q1's leaves per segment), q2 AS (a step that reads q1); what can the step q2 read?
*Tests: reading named steps from the top down: each step sees the tables and the steps above it.*

- The warehouse's tables and q1, the step above it  <- correct
- Only the warehouse's tables, never another step
- Only q1, since a step can read nothing else
- Every step in the query, including the steps below it

---

## Q6. Last week's Python loop counted the customers present in each quarter; which SQL line does the same?
*Tests: counting customers who bought, each once, against counting order rows.*

- count(*) AS customers with GROUP BY quarter
- count(DISTINCT customer_id) with GROUP BY quarter  <- correct
- count(customer_id), which skips missing ids, per quarter
- count(DISTINCT order_id) with GROUP BY quarter

---

## Q7. Retail-Plus placed 140 orders from 76 customers in Q2; which orders per customer goes on Anand's sheet?
*Tests: integer division, and dividing by the customers who placed the orders.*

- 1, as count(*) divided by the distinct count prints it
- 2, the nearest whole number of orders
- 1.84, from 140 orders over 76 customers in numeric  <- correct
- 1.17, orders over the tier's 120 members

---

## Q8. Week 1 Thursday: the monsoon sale's 6 percent lift came from which customers got the discount; what would a fair comparison need?
*Tests: the return question from Week 1 Thursday, one level up: a comparison fair on mix.*

- The exposed against everyone else, over a longer window
- Like for like: each segment apart, or a held-back group  <- correct
- The same customers' sale month against the month before
- The lift set against the 17.6 percent it must clear

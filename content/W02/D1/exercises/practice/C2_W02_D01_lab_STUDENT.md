# Can you run the day's checks on a new question in an hour: four row counts, one running order and one short suite?

The TA-led practice lab set, three problems climbing in difficulty, about an hour: problem 1 ten
minutes, problem 2 ten, problem 3 about forty. Work alone for problems 1 and 2 and in pairs for
problem 3. The lab also hosts the escalated case's parts 3 to 5, from
`exercises/unguided/C2_W02_D01_escalated_case_STUDENT.md`, and the interview drill aloud; the TA runs
those around this set.

> "I want these numbers every Monday, for every segment and channel, computed from the warehouse
> itself. No notebooks, no exports, nothing a person can mistype."
>
> Anand Iyer, finance controller, Kalpa Retail

Kalpa Retail's warehouse is a Postgres database. The `orders` table holds 1,000 rows, one per order,
with the columns order_id, customer_id, order_date, quarter, channel, amount and status; the
`customers` table holds 340 rows, one per customer, with customer_id, segment, city, country and
joined_date. Q1 is April to June 2026 and Q2 is July to September 2026. There are three channels (app,
web and store) and three statuses (delivered, returned and cancelled), and every channel has orders of
every status in each quarter. The segment is looked up with `JOIN customers c USING (customer_id)`,
which finds each order's one customer and changes no row count. Customers who bought are counted once
in a group, however many orders they placed. A tie-out adds a set of parts and sets the sum beside the
whole it should make, and a fingerprint is a block of numbers describing the book, printed beside the
results so a reader can tell a changed book from a changed query.

| Segment | Members | Q1 orders | Q1 customers who bought | Q2 orders | Q2 customers who bought |
|---|---|---|---|---|---|
| Business | 40 | 97 | 36 | 91 | 35 |
| Retail-Core | 150 | 199 | 102 | 193 | 96 |
| Retail-Plus | 120 | 215 | 91 | 140 | 76 |
| Student | 30 | 27 | 15 | 38 | 20 |
| The book | 340 | 538 | 244 | 462 | 227 |

**Who needs the answer.** Anand's analyst audits every query the team ships, and the head of customer
service is waiting on a first suite of her own. Both need the same three habits on a question the team
has not run before: say how many rows a query returns before running it, say the order it runs in,
and build a short suite that ties out and draws a sample twice the same way.

**The questions on the way.**

- How many rows does each of four queries return, predicted before you run it?
- In which order does the database work through five clauses, why does one of them sit where it does, and which piece answers each request?
- What does a first returns suite for the head of customer service say, and does it tie out and repeat?

**What you post.** One line of eleven letters in item order, no spaces, then your problem 3 suite
pasted below it:

```
Post exactly this shape: xxxxxxxxxxx
```

---

## Problem 1. How many rows does each of four queries return, predicted before you run it?

Used at work every time a query is written, since a row count you predicted is the cheapest check
there is.

Ten minutes, alone. Write your four predictions down, then run the four queries and compare.

### Q1. How many rows does the Q2 channel and status query return?

```sql
SELECT channel, status, count(*) AS orders
FROM   orders
WHERE  quarter = 'Q2'
GROUP  BY channel, status;
```

How many rows come back?

a) 3
b) 9
c) 6
d) 18

### Q2. How many segment-quarters clear a bar of 90 customers?

```sql
SELECT c.segment, o.quarter, count(DISTINCT o.customer_id) AS customers
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
HAVING count(DISTINCT o.customer_id) >= 90;
```

How many rows come back?

a) 4
b) 2
c) 8
d) 3

### Q3. How many segments placed more than 100 orders in Q2?

```sql
SELECT c.segment, count(*) AS orders
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
GROUP  BY c.segment
HAVING count(*) > 100;
```

How many rows come back?

a) 4
b) 3
c) 2
d) 1

### Q4. How many customers does the half-year list hold?

```sql
SELECT DISTINCT customer_id
FROM   orders
WHERE  quarter IN ('Q1', 'Q2');
```

How many rows come back?

a) 301
b) 471
c) 1,000
d) 340

## Problem 2. In which order does the database work through five clauses, why does one of them sit where it does, and which piece answers each request?

Used at work whenever a query surprises its author and the first question is which clause produced
the surprise.

Ten minutes, alone.

```sql
SELECT   c.segment, count(DISTINCT o.customer_id) AS customers, sum(o.amount) AS revenue
FROM     orders o
JOIN     customers c USING (customer_id)
WHERE    o.channel = 'app'
GROUP BY c.segment
HAVING   count(DISTINCT o.customer_id) >= 30
ORDER BY revenue DESC;
```

### Q5. In which order does the database work through the five clauses after FROM and the lookup?

After FROM and the lookup make the rows, in which order does the database work through the other five
clauses?

a) WHERE, GROUP BY, HAVING, SELECT, ORDER BY
b) SELECT, WHERE, GROUP BY, HAVING, ORDER BY
c) WHERE, GROUP BY, SELECT, HAVING, ORDER BY
d) GROUP BY, WHERE, HAVING, SELECT, ORDER BY

### Q6. Why does WHERE run before GROUP BY while HAVING runs after it?

Kavya Nair, the team's senior analyst, asks you to defend one placement. Why does WHERE run before
GROUP BY while HAVING runs after it?

a) WHERE is written first, and the database runs the clauses in the order they are written
b) HAVING needs the names SELECT gives the columns, so it has to wait for SELECT to finish
c) HAVING and WHERE filter in the same way, and HAVING runs later only to save the database work
d) WHERE judges single rows before groups exist; HAVING judges a group's count once groups form

### Q7. Which piece of a query answers each of the service head's four requests about returns?

The head of customer service sends four requests about returned orders. Match each request to the
piece of a query that answers it.

| Request | Piece of a query |
|---|---|
| 1. Keep only the channels where at least 20 customers returned an order | P. `WHERE status = 'returned'` |
| 2. Keep only the orders that came back | Q. `HAVING count(DISTINCT customer_id) >= 20` |
| 3. How many different customers returned something | R. `count(DISTINCT customer_id)` |
| 4. How many returned orders there were | S. `count(*)` |

Which pairing holds?

a) 1P 2Q 3R 4S
b) 1Q 2P 3R 4S
c) 1Q 2P 3S 4R
d) 1P 2Q 3S 4R

## Problem 3. What does a first returns suite for the head of customer service say, and does it tie out and repeat?

Used at work whenever a new stakeholder asks for a suite of their own and the team has an hour to
build one that an auditor will accept.

About forty minutes, in pairs.

> "How many orders came back, and how many customers sent one back, for each channel in each quarter?
> How many customers sent something back over the half-year? And give my team five returned Q2 orders
> to trace against the ERP."
>
> The head of customer service, Kalpa Retail

A returned order is an order whose status is returned. The ERP is the system Finance books orders in.
Build the suite on the warehouse in three parts, then answer items 8 to 11 from what it prints.

- **The suite, as named steps.** A `WITH` query whose first step, `returned`, keeps the returned
  orders, and whose second step, `per_channel`, counts orders, customers who returned and rupees for
  each channel and quarter. Then the same query with the channel left out of the grouping, whose rows
  are each quarter across all channels, so the channels can be tied out against their quarter.
- **The half-year.** A short query that counts the customers who returned an order in either quarter.
- **The sample and its fingerprint.** A query that returns five returned Q2 orders the analyst's rerun
  will return again, and beside it the returned book's rows, rupees and distinct customers.

### Q8. Which channel's returned orders rose from Q1 to Q2?

Reading your `per_channel` rows, which channel's returned orders rose from Q1 to Q2?

a) app
b) web
c) store
d) none, since every channel's returns fell

### Q9. Which tie-out holds on the returns suite in Q1?

Set your three Q1 channel rows beside the Q1 row of the query without the channel. Which tie-out
holds?

a) The channels' orders and customers both add to the Q1 row, 97 orders and 90 customers
b) The channels' customers add to the Q1 row's 78, and their orders to its 97
c) Neither adds, since each channel's returns are counted in a group of their own
d) The channels' orders add to the Q1 row's 97; their customers add to 90 against its 78

### Q10. Which rebuild from each customer's history confirms the half-year count of customers who returned an order?

Your half-year query counts the customers who returned an order straight from the orders. Three
filters over one row per such customer give their histories: 24 returned an order in both quarters,
54 in Q1 only and 52 in Q2 only. Which rebuild confirms your count, and what does it give?

a) The 184 returned orders, one customer for each, so the half-year holds 184 customers
b) 54 plus 52 is 106, the customers who returned in one quarter only, so 106 in all
c) 24 plus 54 plus 52 is 130, and 24 plus 54 and 24 plus 52 rebuild your quarter rows
d) 24 plus 54 for Q1 and 24 plus 52 for Q2, added together, which gives 154 customers

### Q11. Which ordering and printout make the service team's sample auditable?

Which pair makes the five returned Q2 orders a sample the analyst can audit?

a) `LIMIT 5` alone, with the returned book's rows, rupees and customers printed beside it
b) `ORDER BY order_id LIMIT 5`, with the returned book's rows, rupees and customers printed beside it
c) `ORDER BY order_id LIMIT 5`, with the time the run took printed beside it
d) `ORDER BY channel LIMIT 5`, with the returned book's row count printed beside it, and nothing else

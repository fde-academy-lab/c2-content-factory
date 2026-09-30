# Practice lab: the Monday tree by channel

> "Every segment and channel." Anand Iyer, finance controller, Kalpa Retail

The suite covers segments; Anand asked for channels too. Four problems, about an hour, climbing
from predicting what a query returns to building the channel tree and saying what it means. The
queries are in `sql/C2_W02_D01_05_lab_STUDENT.sql`. Predict before you run, every time: a
prediction written after the result teaches nothing.

Post one line, eleven letters in item order, no spaces, then your channel query from problem 4:

```
Post exactly this shape: xxxxxxxxxxx
```

---

## Problem 1. Predict the row count, about ten minutes

Write your four predictions down, then run blocks `lab_a` to `lab_d` and compare.

### Q1

Anand's analyst asks for orders per quarter with block `lab_a`, which groups by quarter. How many
rows come back?

a) 1
b) 2
c) 3
d) 1,000

### Q2

Block `lab_b` groups by segment and quarter. How many rows does the analyst get?

a) 4
b) 2
c) 1,000
d) 8

### Q3

Block `lab_c` adds `HAVING count(*) < 30` to `lab_b`. How many segment-quarters survive?

a) 1
b) 0
c) 8
d) 3

### Q4

Block `lab_d` groups Q2 orders above Rs 5,000 by channel and status. Every channel has orders of
every status in that range. How many rows come back?

a) 3
b) 6
c) 9
d) 12

## Problem 2. The order the database runs, about ten minutes

### Q5

The thin-cell query holds FROM, WHERE, GROUP BY, HAVING and ORDER BY. In which order does Postgres
apply them?

a) FROM, GROUP BY, WHERE, HAVING, ORDER BY
b) FROM, WHERE, GROUP BY, HAVING, ORDER BY
c) WHERE, FROM, GROUP BY, ORDER BY, HAVING
d) FROM, WHERE, HAVING, GROUP BY, ORDER BY

### Q6

Why does HAVING sit after GROUP BY in that order?

a) Because HAVING is written after GROUP BY in the query text
b) Because HAVING runs faster once rows are sorted
c) Because HAVING can only see columns named in SELECT
d) Because the count it tests exists only once groups do

## Problem 3. A colleague's channel query, about fifteen minutes

Run block `lab_channel_hurried`, a colleague's first attempt at the channel tree. Read every column
before you trust any of them.

### Q7

Which column of the colleague's query is right as it stands?

a) customers
b) orders_per_customer
c) revenue_per_order
d) None of the three

### Q8

The customers column reads 153 for app in Q2. What does 153 count?

a) Customers who bought through the app in Q2, once each
b) App orders placed in Q2, one per row
c) Members whose usual channel is the app
d) Customers who used the app in both quarters

## Problem 4. The channel tree, about twenty-five minutes

Write the channel tree yourself as two CTEs, one per quarter, lined up on channel: revenue in each
quarter, the change in rupees and percent, and orders per customer in each quarter, divided in
numeric. Compare it with block `lab_channel_tree` only after yours runs. Then run
`lab_channel_split`, which splits each channel into Business and consumer orders.

### Q9

Which channel lost the most revenue from Q1 to Q2?

a) App
b) Store
c) Web
d) None, since every channel grew

### Q10

Is web's fall made of consumer orders or of Business orders?

a) Business orders, nearly all of it
b) Consumer orders, which fell in every channel
c) Half each, since both kinds of order fell
d) It cannot be told from the warehouse at all

### Q11

Which sentence about channels goes to Anand?

a) Web is collapsing, so move the web budget into the store.
b) Store grew 61 percent, so the store team earns a bonus.
c) Channels are stable, so the channel split can be dropped.
d) Web's fall and store's rise are Business orders moving.

# How recently, how often and how much has each of Kalpa's 340 customers bought?

Chapter 1 set, five items, after chapter 1: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "One table, one row per customer, refreshed every Monday: how recently each customer bought, how
> often, how much, their segment, whether the monsoon sale reached them, and the flags we act on."
>
> The growth team, Kalpa Retail

Kalpa Retail's growth team decides every Monday who gets an offer: a win-back code for customers who
have gone quiet, a first-order nudge for customers who signed up and never bought. Its table holds
one row per customer and three numbers: recency, the date of the last order; frequency, the count of
orders; and spend, the value of the orders at the prices charged, whatever became of each order
afterwards. Retailers call the three RFM. The warehouse, Kalpa's Postgres database, holds 1,000
orders from April to September 2026, worth Rs 19,84,00,000, and a customer list of 340 customers.

Chapter 1 weighed three ways to compute the numbers: Week 1's loop, which adds each order to its
customer's running total; a SQL `GROUP BY` in the warehouse, which sends back one row per customer
who ordered; and pandas `groupby`, which splits the orders by customer, applies the three
calculations to each group and combines one row per customer. It chose pandas, because the growth
team's analysts work in Python and the day's later steps need the orders in memory. The table it
built from the orders, called `rfm` below, held 301 rows. Once the customer list became the table's
starting point, the 39 customers who never ordered appeared, and a SQL query built from the list
gave the same three numbers for all 340. Kavya Nair, the senior analyst on the team, reviews every
table before it leaves.

**Who needs the answer.** The growth team, which sends Monday's offers from this table. A customer
missing from it gets no offer at all, and a number that a later step reads wrongly sends the wrong
offer.

**The questions on the way.**

- Which way should compute the numbers when the orders run to crores, and what does it move?
- What does the average orders per customer read before anyone fills the gaps?
- What does a teammate's fix print with the order-built table on the left of the merge?
- Which count could the growth team's lead run herself to confirm the 39 before the nudge goes out?
- Which way should build the table once a dashboard on the warehouse is its only reader?

Every number about next year in item 1 is invented.

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

### Q1. Which way should compute the numbers when the orders run to crores, and what does it move?

A year from now, Kalpa Retail's orders table holds 2 crore rows from 9 lakh customers on the list, of
whom 6 lakh have ordered. The growth team still wants the three numbers for every customer each
Monday, merged onto the customer list in pandas. Which way should compute the numbers, and how many
order-side rows does it move out of the warehouse each Monday?

a) pandas `groupby` should compute them, moving 2 crore rows, since the later steps need the orders.
b) SQL `GROUP BY` should compute them, moving 2 crore rows, since the warehouse reads every order.
c) SQL `GROUP BY` should compute them, moving 6 lakh rows, one per customer who ordered.
d) pandas `groupby` should compute them, moving 6 lakh rows, one for each group it returns.

### Q2. What does the average orders per customer read before anyone fills the gaps?

Before the fill, a teammate reads the growth team's average straight off the merged table:

```python
half = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
half["frequency"].mean()
```

`customers` holds all 340 customers, `rfm` the 301 who ordered, and the warehouse holds 1,000
orders. What does the second line print, and over which customers is it an average?

a) It prints 2.94, an average over all 340 customers on the list.
b) It prints 3.32, an average over the 301 who ordered, since `mean` skips the gaps.
c) It prints `nan`, since one missing frequency leaves the whole column's mean missing.
d) It prints 3.32, an average over all 340 customers on the list.

### Q3. What does a teammate's fix print with the order-built table on the left of the merge?

A teammate fixes the first-order nudge list this way:

```python
table = rfm.merge(customers, on="customer_id", how="left", validate="one_to_one")
table = table.assign(frequency=table["frequency"].fillna(0).astype("int64"))
print(len(table), (table["frequency"] == 0).sum())
```

What does the last line print?

a) It prints 340 39, since the merge keeps every customer on either side.
b) It stops with a `MergeError`, since 39 customers find no match on the left.
c) It prints 340 0, since the 39 come back and a missing count is never 0.
d) It prints 301 0, since the left side holds only the customers who ordered.

### Q4. Which count could the growth team's lead run herself to confirm the 39 before the nudge goes out?

From next Monday the growth team's lead signs off the first-order nudge herself. She works in SQL in
the warehouse, never opens a notebook, and wants a count that would disagree with the pandas table's
39 if the table were wrong. Which route qualifies?

a) Group the orders by customer in the warehouse, and count the groups whose `count(*)` is 0.
b) Count, in the warehouse, the listed customers who have no row in `orders`.
c) Left-join the list to the orders, group by customer, and count those whose `count(*)` is 0.
d) Fetch every order's customer id, and check the list against them in a Python loop.

### Q5. Which way should build the table once a dashboard on the warehouse is its only reader?

Next quarter a dashboard that the data platform lead builds on the warehouse becomes the growth
team's only view of the table. It reads every number straight from Postgres whenever someone opens
it, and the sale flag and the months view move into it too. The orders stay at about 500 a quarter,
as they are now. Which way should build the table's three numbers then?

a) pandas `groupby` should stay, since 500 orders a quarter move in a fraction of a second.
b) A SQL `GROUP BY` on the orders should build them, sending one row per customer who ordered.
c) A SQL query from the customer list, with a `LEFT JOIN` to the orders, should build them.
d) pandas `groupby` should stay, with its table written into the warehouse every Monday.

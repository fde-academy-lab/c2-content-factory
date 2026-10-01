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
- Which count could disagree with the pandas table if the table were wrong?
- Which fact, if it became true next quarter, would move the three numbers into the warehouse?

Every number about next year in items 1 and 5 is invented.

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

a) pandas `groupby`: 2 crore rows, since the later steps need the orders
b) Week 1's loop: 9 lakh rows, one for each customer on the list
c) SQL `GROUP BY`: 6 lakh rows, one per customer who ordered
d) pandas `groupby`: 6 lakh rows, one for each group it returns

### Q2. What does the average orders per customer read before anyone fills the gaps?

Before the fill, a teammate reads the growth team's average straight off the merged table:

```python
half = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
half["frequency"].mean()
```

`customers` holds all 340 customers, `rfm` the 301 who ordered, and the warehouse holds 1,000
orders. What does the second line print, and over which customers is it an average?

a) 2.94, over all 340 customers on the list
b) 3.32, over the 301 who ordered, since `mean` skips the gaps
c) `nan`, since one missing frequency leaves the column's mean missing
d) 3.32, over all 340 customers on the list

### Q3. What does a teammate's fix print with the order-built table on the left of the merge?

A teammate fixes the first-order nudge list this way:

```python
table = rfm.merge(customers, on="customer_id", how="left", validate="one_to_one")
table = table.assign(frequency=table["frequency"].fillna(0).astype("int64"))
print(len(table), (table["frequency"] == 0).sum())
```

What does the last line print?

a) 340 39: the merge keeps every customer on either side
b) It stops with a `MergeError`, since 39 customers find no match
c) 340 0: the 39 come back, and a missing count is never 0
d) 301 0: the left side keeps only the customers who ordered

### Q4. Which count could disagree with the pandas table if the table were wrong?

Before the first-order nudge goes to the 39, Kavya wants their count confirmed by a route that shares
no code with the pandas table. Which route qualifies?

a) A SQL count of listed customers with no row at all in `orders`
b) `340 - len(rfm)`, the list less the rows the groupby returned
c) `(table["frequency"] == 0).sum()`, rerun after a restart
d) `(table["spend"] == 0).sum()`, zero spend in place of zero orders

### Q5. Which fact, if it became true next quarter, would move the three numbers into the warehouse?

Chapter 1 chose pandas `groupby` to compute the three numbers. Which of these facts would move that
step to a SQL `GROUP BY` in the warehouse, with pandas merging its answer onto the list?

a) The customer list grows to 4 lakh, and the list is read each Monday
b) The orders table grows to 3 crore rows, too many to move each Monday
c) The growth team asks for a fourth number, the first order's date
d) The monsoon sale's feed has to be merged onto the table every Monday

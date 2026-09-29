# Round 1 set: one row per customer

Fifteen minutes, alone, after round 1's demonstration. Every item is a question the growth team
or Kavya would ask about the Monday table. Run code only where an item says so; the others are
answered from what you know.

Post one line, seven letters in item order, no spaces:

```
Post exactly this shape: xxxxxxx
```

---

### Q1

Marketing wants a Q2-only version of the spend table first. The analyst writes
`orders[orders["quarter"] == "Q2"].groupby("customer_id")["amount"].sum()`. The warehouse holds
340 customers, 301 of whom ordered at some point in the two quarters. How many rows can this
return?

a) 340, one per customer on the list
b) At most 301, and in fact fewer: only customers with a Q2 order
c) Exactly 301, since every buyer on the list bought in both quarters
d) 500, about half the orders

### Q2

The growth team asks: "How many orders does a customer who buys with us place, on average?" An
analyst reports `table["frequency"].mean()` on the 340-row table: 2.94. What is wrong with the
answer?

a) Nothing: 1,000 orders over 340 customers is the definition
b) The mean should be a median, because frequency is skewed by heavy buyers
c) frequency is a float after the merge, so the mean is off by rounding
d) The 39 customers with zero orders pull it down; among buyers it is 3.32

### Q3

The table is refreshed on data whose last order is 28 September 2026. A customer's last order is
28 August 2026. What recency should the table show, whatever day the refresh runs?

a) 31 days
b) 59 days, if the refresh runs on 26 October
c) 0 days, since the customer ordered in the extract
d) 28 days, a month

### Q4

Kavya wants one check in the refresh that catches recency measured from the wall clock, without
reading any single row. Which check does it?

a) Recency has no missing values
b) The largest recency is under 200 days
c) The smallest recency is 0 days
d) Recency is an integer column

### Q5

An analyst's table shows frequency 1 for every customer. The line was
`frequency=("customer_id", "nunique")`. What should the line be, and why?

a) `frequency=("order_date", "nunique")`, because each order has a date
b) `frequency=("order_id", "count")`, because each order is one row in the group
c) `frequency=("amount", "sum")`, because spend and frequency always move together
d) `frequency=("order_id", "max")`, because the last order id is the count

### Q6

Anand asks how much of the Rs 19,84,00,000 two-quarter book the 40 Business accounts carry,
before the growth team sets a campaign target on spend. Run
`table.groupby("segment")["monetary"].sum() / table["monetary"].sum()`. What does it show, and
what does it mean for a spend target?

a) About 99 percent, so a spend target measures Business and hides every consumer segment
b) About 12 percent, since Business is 40 of the 340 customers on the list
c) About 50 percent, so a spend target is balanced across segments
d) About 99 percent, so the consumer segments can safely be left out of the table entirely

### Q7

In which order do the steps of the Monday table run?

1. read the orders and check the count against the warehouse
2. groupby and agg per customer
3. merge onto the customer list with validate
4. fill the counts of customers with no orders, and fix the dtype
5. measure recency from the data's last date

Which order is right?

a) 2, 1, 3, 5, 4, since the aggregates come first
b) 1, 3, 2, 4, 5, since the merge fixes the grain first
c) 5, 1, 2, 3, 4, since the date is set before anything else
d) 1, 2, 3, 4, 5

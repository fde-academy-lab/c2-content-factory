# Chapter 2 set: the rows that repeat

6 items, about 18 minutes, after chapter 2. Every number here is invented unless it says it is from today's file; the reasoning is the one you ran on Kalpa's export. Items marked Design ask for the best-fit approach, a sizing or the fact that would change it.

Post one line, 6 letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1

A colleague's dedupe of a 300-row export reports 0 duplicates, and a count of distinct order ids returns 284. Each row carries a load timestamp added by the pipeline. What happened?

a) Sixteen orders were lost in the load and need a resend
b) The timestamp made every row unique, so no row matched
c) The dedupe is right, and the id count is off by 16
d) Sixteen rows carry blank order ids that the count skips

### Q2 (Design)

Kalpa's ERP issues one order_id per order and never reuses it. Which key is the best fit for deduplicating Kalpa's orders?

a) customer_id and order_date together
b) Every field, the load timestamp included
c) order_id, the key the ERP issues
d) Every field except the load timestamp

### Q3

An analyst dedupes Kalpa orders on customer_id and order_date. A loyal member places two real orders on the same day. What happens to revenue?

a) It falls, since one real order is set aside as a copy
b) It stays right, since the key still finds true copies
c) It rises, since the key keeps both orders and a copy
d) It stays right, since two orders a day never happen

### Q4

An invented export holds 150 rows and 141 distinct order ids, and 148 of its amounts convert. How many rows sit beyond one per order?

a) 2
b) 7
c) 11
d) 9

### Q5 (Design)

Kalpa's app and its stores each number customers from C-1 upwards, and Meera wants one customer table. Which identity rule is the best fit?

a) The customer id, since each system issues one per person
b) Every field, since only an exact copy is safe to merge
c) Cleaned phone and email, doubtful pairs reviewed
d) The customer's name, since it appears in both systems

### Q6 (Design)

A fuzzy key with no blocking compares every row with every other. About how many comparisons does it make on 10,000 rows?

a) About 10,000
b) About 1 lakh
c) About 100 crore
d) About 5 crore

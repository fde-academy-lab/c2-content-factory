# The case: the Monday suite

> "I want these numbers every Monday, for every segment and channel, computed from the warehouse
> itself. No notebooks, no exports, nothing a person can mistype." Anand Iyer, CFO, Kalpa Retail

Anand's analyst will run six queries every Monday and audit each one line by line, without you
beside him. You have thirty minutes, alone, no hints. Write the six queries under their comment
lines in `sql/C2_W02_D01_02_monday_suite_STUDENT.sql`, or work through
`notebooks/C2_W02_D01_hands_on_STUDENT.ipynb`, which runs the same suite with ten lettered choices.
Then answer the eight items below from your own results.

**The rules the analyst audits against.** Revenue means booked revenue, every status, and the
comment says so. A customer is counted once. Every ratio is divided in numeric and rounded on
purpose. Every list has an `ORDER BY` on a unique key. A step that feeds another step is a named CTE.

Post two lines: the ten letters from the notebook, then the eight letters below, each in item order
with no spaces.

```
Post exactly this shape:
xxxxxxxxxx
xxxxxxxx
```

---

## Part A. The book

Write query 1: orders and revenue per quarter, with the change against Q1 in percent.

### Q1

Your query 1 returns 538 orders and Rs 10,00,00,000 for Q1, and 462 orders and Rs 9,84,00,000 for
Q2. What does its change column read for Q2?

a) -1.6
b) -14.1
c) -16.0
d) +1.6

## Part B. Customers

Write query 2: the customers who bought in each quarter, beside the members on the book.

### Q2

Your query 2 shows 244 customers in Q1 and 227 in Q2, against 340 members on the book. Which
denominator belongs under orders per customer on Anand's sheet?

a) 340, the members on the book, in both quarters
b) 301, the customers across both quarters, in each quarter
c) Each quarter's own buyers, 244 and 227
d) 1,000, the orders, so the ratio reads 1.00

## Part C. The leaves

Write query 3: customers, orders per customer, revenue per order and revenue, per segment and quarter.

### Q3

Your query 3's Retail-Plus rows read orders per customer 2.36 in Q1 and 1.84 in Q2. Which check does
the analyst run on the Q2 figure with a calculator?

a) 1.84 times 140 orders should give Rs 4,13,380
b) 1.84 times 76 customers should give 140 orders
c) 1.84 plus 2.36 should give the two-quarter figure
d) 1.84 over 2.36 should give the revenue change

### Q4

Query 3 has to come back in the same order every Monday. Which ORDER BY does it need?

a) None, since GROUP BY already sorts its groups
b) ORDER BY revenue DESC, the biggest segment first
c) ORDER BY orders_per_customer, the weakest first
d) ORDER BY segment and quarter, a unique pair

## Part D. The typical order and the thin cells

Write query 4, the median order beside the mean per segment and quarter, and query 5, the
segment-quarters with fewer than 30 orders.

### Q5

Your query 4 shows Business's median Q2 order at Rs 8,32,000 and its mean at Rs 10,72,358. What does
the gap tell the analyst?

a) The median was computed on the wrong column
b) Business orders are all close to Rs 10 lakh
c) A few very large orders pull the mean up
d) Business revenue fell because the median fell

### Q6

Your query 5 returns one row: Student in Q1, with 27 orders. What does the suite do with that row?

a) Keeps Student's rates, flagged as a thin sample
b) Drops Student from the sheet until it reaches 30 orders
c) Merges Student into Retail-Core so the cell is larger
d) Raises the threshold until no row comes back

## Part E. What moved, and the sentence

Write query 6: two CTEs, one per quarter, lined up on segment, giving the percentage change in
customers, orders per customer, revenue per order and revenue. Then write the sentence to Anand.

### Q7

In query 6, why does the q2 step repeat the q1 step exactly, with only the quarter filter changed?

a) Postgres requires every CTE in a WITH to share one shape
b) It runs faster when both steps have the same columns
c) The JOIN only works on two steps with identical names
d) So the leaves line up and one step audits both

### Q8

Which sentence goes to Anand?

a) Revenue fell 29.4 percent, so Retail-Plus needs acquisition money.
b) The 1.6 percent fall sits in Retail-Plus frequency.
c) Revenue fell 1.6 percent, spread evenly across the four segments.
d) Revenue is flat, so no segment needs attention this quarter.

---

## What to post, and what the analyst checks

The two letter lines, then your sentence to Anand with its claim, evidence, caveat and next step.
The analyst checks three things before reading your sentence: the eight rows of query 3 add back to
1,000 orders, the change in query 6 matches the revenue in query 3, and no ratio came out whole.

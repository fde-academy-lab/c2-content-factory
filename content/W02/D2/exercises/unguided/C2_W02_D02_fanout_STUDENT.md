# Round 1 set: the join that multiplied

About 15 minutes, alone first, then compare with your neighbour. Eight items. Every item has one
right answer.

Anand asked: "Show me, order by order, what we actually collected against what we booked in Q2."
The platform lead added that the payments feed "sometimes double-posts when the gateway retries".
Kavya's rule for this round is the one on the board: tell her the grain of each table before you
tell her a total.

Post one line, eight letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxxxx
```

---

## Part A. Predict four row counts before running the joins

Items 1 to 4 run on an invented extract, built for this set: six app orders and the eight payment
rows the feed posted against order ids in their range. Write your four numbers on paper before you
look at the options.

`extract_orders` (invented):

| order_id | amount |
|---|---|
| A-1 | 2,400 |
| A-2 | 64,000 |
| A-3 | 1,100 |
| A-4 | 3,300 |
| A-5 | 88,000 |
| A-6 | 900 |

`extract_payments` (invented):

| payment_id | order_id | amount | instalment_no |
|---|---|---|---|
| Q-1 | A-1 | 2,400 | 1 |
| Q-2 | A-2 | 38,400 | 1 |
| Q-3 | A-2 | 25,600 | 2 |
| Q-4 | A-3 | 1,100 | 1 |
| Q-5 | A-3 | 1,100 | 1 |
| Q-6 | A-5 | 52,800 | 1 |
| Q-7 | A-5 | 35,200 | 2 |
| Q-8 | A-8 | 1,750 | 1 |

### Q1. How many rows does `extract_orders JOIN extract_payments ON order_id` return?

a) 6, one row for each order in the extract
b) 8, one row for each payment the feed posted
c) 7, once per payment that finds its order
d) 4, one row for each order that has a payment

### Q2. How many rows does the LEFT join from orders to payments return?

a) 9, the seven matched rows and two unpaid orders
b) 6, since a LEFT join keeps each order exactly once
c) 8, the same as the number of payment rows posted
d) 10, every order and every payment once at least

### Q3. How many rows does the RIGHT join from orders to payments return?

a) 7, since a payment with no order is dropped
b) 6, one row for each order that the extract holds
c) 9, the seven matched rows plus the two unpaid orders
d) 8, each payment once, since orders has unique ids

### Q4. How many rows does the FULL join return, and what does it add over the LEFT one?

a) 9, the same rows as the LEFT join and nothing more
b) 10, the LEFT join's rows plus the payment for A-8
c) 14, the six orders and the eight payments added up
d) 8, one row per payment, since payments is the bigger table

---

## Part B. The same multiplication on Kalpa's Q2

### Q5. The query below reports Rs 19,29,04,410 as "collected" for Q2, against Rs 9,84,00,000 booked. The collections lead reads it and proposes to stand the team down for the quarter. What do you do?

```sql
SELECT SUM(o.amount) FROM orders o
JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2';
```

Which of these do you do?

a) Agree, since every row it sums is a real order that was really paid
b) Hold the number, and count rows in against rows out before anyone reads it
c) Send it with a note that Q2 collections ran ahead of bookings by 1.96 times
d) Rerun it on Q1 first, since a quarter with no comparison proves nothing

### Q6. Q2 holds 462 orders. 216 of them carry two payment rows, and no order carries more than two. How many rows does `orders LEFT JOIN payments`, filtered to Q2, return?

a) 462, since a LEFT join keeps each order exactly once
b) 924, since every order is doubled by the two-row orders
c) 246, the orders that carry a single row or none at all
d) 678, the 462 orders plus one row per two-row order

### Q7. A teammate sends this report, built from one LEFT join of orders to payments for Q2. Which figure tells you it cannot go to Anand?

| channel | booked_as_reported | collected_as_reported | pct_collected |
|---|---|---|---|
| all three | Rs 19,46,59,340 | Rs 9,66,65,820 | 49.7 |

a) Booked, which is about twice the Rs 9,84,00,000 in orders alone
b) The 49.7 percent, since no quarter collects below half its book
c) Collected, which sits below booked and so must have lost rows
d) The channel label, since a report without channels is not one

### Q8. Which change gives you booked and collected on one row per order, so the report above can be rebuilt honestly?

a) Sum DISTINCT o.amount, so that each order amount counts once
b) Switch to an INNER join, so only the matched rows are summed
c) Sum payments per order in a CTE, then LEFT JOIN orders to it
d) Group the joined rows by channel, where the doubling cancels

---

## Check it yourself

After you post, run steps 3 to 7 of `sql/C2_W02_D02_02_fanout_STUDENT.sql` and read rows in against
rows out for yourself. The last query must return two trues before any number from this round
leaves your screen.

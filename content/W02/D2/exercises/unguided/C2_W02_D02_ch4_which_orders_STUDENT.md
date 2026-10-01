# Which Q2 orders were never paid, and which payments did the gateway post twice?

The chapter 4 set. Items 1 and 2 close the chapter live; the rest open the TA-led practice lab or are
worked tonight. Six items on five invented orders and seven invented payments, so none of its numbers
comes from Kalpa's warehouse.

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

## What do you need to know before the items?

**Who needs the answer.** The collections team, who ring every order on the unpaid list, and the
platform lead and Finance, who reverse or refund what is on the double-paid list. A name on the
wrong list is a call to a customer who did nothing wrong.

- An **anti-join** keeps the rows of one table that have no partner in the other, for example a LEFT
  JOIN that keeps only the rows where the payment side is NULL.
- **Never paid** means an order with no payment row at all. A **retry** is one order and instalment
  posted more than once.
- `NULL BETWEEN` two dates is unknown, and WHERE keeps only rows that are true.
- The quarter, Q2, runs from 1 July to 30 September.

The invented `orders`:

| order_id | channel | amount |
|---|---|---|
| V-1 | app | 1,000 |
| V-2 | web | 3,000 |
| V-3 | store | 600 |
| V-4 | app | 2,200 |
| V-5 | web | 800 |

The invented `payments`:

| payment_id | order_id | paid_date | amount | instalment_no |
|---|---|---|---|---|
| R-1 | V-1 | 2026-07-04 | 1,000 | 1 |
| R-2 | V-2 | 2026-07-10 | 1,800 | 1 |
| R-3 | V-2 | 2026-08-10 | 1,200 | 2 |
| R-4 | V-3 | 2026-07-15 | 600 | 1 |
| R-5 | V-3 | 2026-07-15 | 600 | 1 |
| R-6 | V-5 | 2026-10-03 | 800 | 1 |
| R-7 | V-9 | 2026-07-20 | 700 | 1 |

Post one line, six letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1. Which orders does the anti-join return?

```sql
SELECT o.order_id
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE p.order_id IS NULL;
```

Which orders does it return?

a) V-4
b) V-4 and V-9
c) V-4 and V-5
d) V-3 and V-4

### Q2. What does the list return once the quarter's dates sit in WHERE?

A teammate adds the quarter to the same query: `WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30' AND p.order_id IS NULL`. Which orders does it return?

a) V-4
b) V-4 and V-5
c) no orders
d) V-5 only

### Q3. What does it return once the dates move into ON?

The dates move into the join: `LEFT JOIN payments p ON p.order_id = o.order_id AND p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'`, with `WHERE p.order_id IS NULL` kept. Which orders does it return?

a) V-4
b) V-4 and V-5
c) no orders
d) V-5 and V-9

### Q4. Where does V-5 belong for Anand's never-paid question?

V-5 was paid on 3 October, three days after the quarter closed. On the definitions above, which list does V-5 belong on when the collections team asks for the orders never paid?

a) on the double-paid list, since it was paid late
b) on the unpaid list, since nothing arrived within Q2
c) on no list, since it was paid after Q2 closed
d) on the list of payments that match no order

### Q5. What does the double-paid list hold, grouped the right way?

Grouped by order alone, `HAVING count(*) > 1` flags V-2 and V-3. Grouped by order and instalment, what does the double-paid list hold, and how much was posted beyond one payment?

a) V-3's instalment 1, and 600
b) V-2 and V-3, and 1,800
c) V-2's instalment 2, and 1,200
d) V-3's instalment 1, and 1,200

### Q6. Which way of writing the unpaid list stays correct once the feed sends NULL ids?

The feed will soon carry refund rows whose `order_id` is NULL. Which way of writing the unpaid list stays correct?

a) NOT IN, since it checks each order id against every id in the list
b) NOT EXISTS or the LEFT JOIN, since a NULL id matches no order
c) NOT IN and NOT EXISTS alike, since both read one subquery
d) none of them, since a NULL id breaks every anti-join

---

## Where does this skill come back?

In chapter 5, where the two lists sit beneath the page Anand signs, and in the escalated case, where
you pick the anti-join condition and the retry grain on Kalpa's own Q2. The notebook for this chapter
is `notebooks/C2_W02_D02_04_which_orders_STUDENT.ipynb`.

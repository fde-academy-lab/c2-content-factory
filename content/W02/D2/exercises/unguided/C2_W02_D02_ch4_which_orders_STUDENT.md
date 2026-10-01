# Which Q2 orders were never paid, and which payments did the gateway post twice?

The chapter 4 set has six items on five invented orders and seven invented payments, so none of its
numbers comes from Kalpa's warehouse. Items 1 and 2 close the chapter live; the rest open the TA-led
practice lab or are worked tonight.

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

## What do you need to know before the items?

**Who needs the answer.** The collections team rings every order on the unpaid list, and the
platform lead and Finance reverse or refund what is on the double-paid list. A name on the wrong
list means a call to a customer who did nothing wrong.

**The questions on the way.**

- Which orders does the anti-join return?
- What does the list return once the quarter's dates sit in WHERE?
- What does it return once the dates move into ON?
- Where does V-5 belong for Anand's never-paid question?
- What does the double-paid list hold, grouped the right way?
- Which way of writing the unpaid list stays correct once the feed sends NULL ids?

An item marked Design asks for the best-fit approach, a sizing, the fact that would switch it, or the second route.

- **Booked** is every order at its amount. **Collected** is the cash that arrived, each order and
  instalment counted once. The **gap** is booked less collected.
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
d) V-4, V-5 and V-9

### Q4. Where does V-5 belong for Anand's never-paid question? (Design)

V-5 was paid by R-6 on 3 October, three days after the quarter closed. Anand's analyst ties the never-paid list's total to the gap, and since every order paid here was paid in full, the two must agree before the page goes out. Which treatment of V-5 and R-6 answers Anand's never-paid question and lets the list and the gap agree?

a) V-5 on the list, R-6 left out of collected
b) V-5 on the list, R-6 kept in collected
c) V-5 off the list, R-6 left out of collected
d) V-5 off the list, R-6 kept in collected

### Q5. What does the double-paid list hold, grouped the right way?

Grouped by order alone, `HAVING count(*) > 1` flags V-2 and V-3. Grouped by order and instalment, what does the double-paid list hold, and how much was posted beyond one payment?

a) V-3's instalment 1, and 600
b) V-2 and V-3, and 1,800
c) V-2's instalment 2, and 1,200
d) V-3's instalment 1, and 1,200

### Q6. Which way of writing the unpaid list stays correct once the feed sends NULL ids? (Design)

The feed will soon carry refund rows whose `order_id` is NULL. A teammate offers four ways to write Anand's never-paid list:

| Way | What keeps an order on the list |
|---|---|
| NOT IN | `o.order_id NOT IN (SELECT order_id FROM payments)` |
| NOT EXISTS | `NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)` |
| NOT EXISTS in Q2 | the same, with `AND p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'` inside |
| The LEFT JOIN | `LEFT JOIN payments p ON p.order_id = o.order_id` with `WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30' AND p.order_id IS NULL` |

Which way still returns exactly the orders never paid once those rows arrive?

a) NOT IN, against the order_ids in payments
b) NOT EXISTS, for a payment row at any date
c) NOT EXISTS, for a payment row dated in Q2
d) the LEFT JOIN, with Q2's dates kept in WHERE

---

## Where does this skill come back?

It comes back in chapter 5, where the two lists sit beneath the page Anand signs, and in the
escalated case, where you pick the anti-join condition and the retry grain on Kalpa's own Q2. The
notebook for this chapter is `notebooks/C2_W02_D02_04_which_orders_STUDENT.ipynb`.

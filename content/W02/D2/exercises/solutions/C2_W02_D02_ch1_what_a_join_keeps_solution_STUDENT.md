# Solution: which rows does each join keep, drop or repeat?

Answers: 1b 2a 3c 4a 5c 6d

## What does this set test?

The set tests which rows survive a join, counted by hand on tables the chapter never used, and which
table a question has to start from. Items 3, 5 and 6 are design items: four ways to answer the
platform lead, each with the count it reports, where two report the same count and only one of them
counts what he asked about; a row count predicted from the keys alone; and four figures read off one
INNER join, where only one is also the true answer to its question.

## What did the set give you to work from?

> **The client asks.** "Show me, order by order, what we actually collected against what we booked in
> Q2. If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand's analyst audits the statement line by line, and you sign the
collected number. A join that drops an unpaid order hides it from the collections team.

- **Booked** is every order at its amount. **Collected** is the cash that arrived, each payment counted
  once. **Posted** is every payment row the feed holds, repeats included. A **retry** is one payment
  the gateway posted twice.
- The **grain** of a table is what one row stands for: one order in `orders`, one payment event in
  `payments`.
- **INNER JOIN** keeps only the pairs that match. **LEFT JOIN** keeps every row of the table named
  first, with NULL where nothing matched. **RIGHT JOIN** keeps every row of the table named second.
  **FULL OUTER JOIN** keeps both sides. NULL is SQL's mark for "no value here".

The invented `orders`:

| order_id | channel | amount |
|---|---|---|
| A-1 | app | 1,200 |
| A-2 | web | 900 |
| A-3 | store | 2,400 |
| A-4 | app | 600 |

The invented `payments`:

| payment_id | order_id | amount | instalment_no |
|---|---|---|---|
| Q-1 | A-1 | 1,200 | 1 |
| Q-2 | A-2 | 900 | 1 |
| Q-3 | A-2 | 900 | 1 |
| Q-4 | A-3 | 1,400 | 1 |
| Q-5 | A-3 | 1,000 | 2 |
| Q-6 | A-7 | 500 | 1 |

## Why does each key hold, item by item?

### Q1. How many rows does the INNER join return?

`orders o JOIN payments p ON p.order_id = o.order_id`, on the two tables above. How many rows come back?

The key is b, "5, as A-2 and A-3 each come out twice". A-1 matches Q-1 once, A-2 matches Q-2 and its repeat Q-3, and A-3 matches its two instalments, Q-4 and Q-5: 1 + 2 + 2 is 5. A-4 has no payment and Q-6's order, A-7, is not in `orders`, so neither appears.

- a, "4, one row for each order, A-1 to A-4": counts orders, when A-4 has no payment to pair with and A-2 and A-3 each pair twice.
- c, "6, one row for each payment, Q-1 to Q-6": counts payment rows, and Q-6 matches no order.
- d, "3, one row each for A-1, A-2 and A-3": counts the paid orders once each, and a join writes one row for every matching pair, so A-2 and A-3 come out twice.

### Q2. What does the LEFT join, orders first, add?

`orders o LEFT JOIN payments p ON p.order_id = o.order_id`. Which order carries NULL payment columns, and how many rows does the join return?

The key is a, "A-4, and 6 rows". The LEFT join keeps the 5 pairs and adds A-4, the order nobody paid, with NULL payment columns: 6 rows.

- b, "A-7, and 6 rows": A-7 is a payment's order id and is not in `orders`, so a LEFT join from orders never shows it.
- c, "A-4, and 5 rows": forgets that LEFT adds A-4 back.
- d, "no order, and 7 rows": 7 is the FULL join's count.

### Q3. Which query answers the platform lead's question? (Design)

The data platform lead owns the payments feed and asks: "How many payment rows in the feed sit on an order id we never booked?" A teammate tries four ways on the two tables above. Which way, with the count it reports, answers him?

The key is c, "payments LEFT JOIN orders, rows with no order: 1". A payment row on an order id nobody booked shows up only in a query that keeps every payment row and then looks for an empty order side, and the one such row is Q-6, 500 against A-7.

- a, "orders LEFT JOIN payments, rows with no payment: 1": starts from orders, so its one empty row is an order with no payment, A-4, which belongs on Anand's unpaid list; Q-6 never appears, and the count of 1 only looks like the answer.
- b, "payments JOIN orders, rows with no order: 0": the INNER join has already dropped Q-6 before the filter looks for an empty order side, so the filter finds nothing.
- d, "payment rows less order rows, 6 less 4: 2": counts every extra payment row as unexplained, and the 2 nets three different rows against one missing row: Q-3's repeat, A-3's second instalment and Q-6, less A-4, which has no payment row, so 1 + 1 + 1 less 1 is 2.

### Q4. What is wrong with a statement that reads 116 percent collected?

A teammate starts the statement from `payments` and attaches each payment's order. It shows 6 lines and 5,900 of cash against 5,100 booked, so it reads as 116 percent collected. Which reading of it is right?

The key is a, "A-4 is missing, and A-2's retry and A-7's 500 sit in the cash". Starting from payments drops A-4, the one unpaid order, and carries Q-3 (A-2's payment posted a second time) and Q-6's 500, which pays an order Kalpa never booked.

- b, "A-3's two instalments are one payment, counted twice here": A-3's two instalments are two real payments of 1,400 and 1,000.
- c, "the cash is right, since customers may pay before booking": cash against bookings cannot honestly exceed them.
- d, "A-7 is an order paid in advance, and it belongs on the statement": A-7 is missing from the orders table, so Kalpa never booked it.

### Q5. How many rows will a FULL join return, from the key counts alone? (Design)

Before running any join on a new pair of tables, you count keys. Order X appears once in `orders` and three times in `payments`. Order Y appears once in `orders` and never in `payments`. Key Z never appears in `orders` and twice in `payments`. How many rows does a FULL OUTER JOIN return for these three keys?

The key is c, "6". INNER writes a x b per key: X gives 1 x 3 = 3. LEFT adds Y once, RIGHT adds Z's 2 rows: 3 + 1 + 2 is 6.

- a, "4": counts one row per key plus a repeat.
- b, "5": forgets that Z's two payment rows each come out.
- d, "7": counts Y's order twice.

### Q6. Which question is an INNER join the honest choice for? (Design)

A teammate answers four questions from the rows of `orders o JOIN payments p ON p.order_id = o.order_id` on the tables above, and writes beside each the figure those rows give. For which question is that figure also the true answer?

The key is d, "store cash received: 2,400". The join's store rows are A-3's two instalments, Q-4 and Q-5, 1,400 + 1,000, which is 2,400. Store's one order was paid, and Q-6 sits on A-7, which nobody booked under any channel, so the feed holds no other store cash and the true answer is 2,400 as well: the INNER join loses nothing this question needs.

- a, "app orders booked: 1": the join holds A-1 alone for app, and app booked A-1 and A-4, so the true answer is 2; the INNER join hides the unpaid A-4.
- b, "share of booked orders paid: 100 percent": every order in the join has a payment by construction, so the join reads 3 of 3; Kalpa booked four orders and three were paid, so the true share is 3 of 4, 75 percent.
- c, "payment rows with no booked order: 0": the join keeps only payment rows that found an order, so it can only read 0; the feed holds one such row, Q-6, so the true answer is 1.

## Which item is worth arguing about?

On item 4, option c, a pair will point out that customers do pay ahead of delivery in some
businesses. The answer is that "ahead" still means against a booked order: cash with no booked order
behind it goes to the platform lead as a question and stays out of collections. Treat any statement
that reads over 100 percent collected as a warning sign, whatever story explains it.

## Where does this pattern live in production?

Razorpay's Orders API combines several payment attempts under one order, and fetching an order's
payments returns every authorised or failed attempt for it (Razorpay documentation, checked 1 Oct
2026), so every merchant reconciling the two lists makes this chapter's choice of join first.

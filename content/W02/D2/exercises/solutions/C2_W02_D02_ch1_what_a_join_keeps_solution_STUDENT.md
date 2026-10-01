# Solution: which rows does each join keep, drop or repeat?

Answers: 1b 2a 3b 4a 5c 6d

## What does this set test?

The set tests which rows survive a join, counted by hand on tables the chapter never used, and which
table a question has to start from. Items 3, 5 and 6 are design items: the join a different question
needs, a row count predicted from the keys alone, and the one question an INNER join answers
honestly.

## What did the set give you to work from?

> **The client asks.** "Show me, order by order, what we actually collected against what we booked in
> Q2. If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand's analyst audits the statement line by line, and you sign the
collected number. A join that drops an unpaid order hides it from the collections team.

- **Booked** is every order at its amount. **Collected** is the cash that arrived, each payment counted
  once. **Posted** is every payment row the feed holds, repeats included.
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

The key is b, "5, one for each matching pair". A-1 matches once, A-2 twice (Q-2 and its repeat Q-3), A-3 twice (two instalments): 1 + 2 + 2 is 5. A-4 and Q-6 find no partner.

- a, "4, one for each order that has a payment": counts orders, and a join writes one row per matching pair.
- c, "6, one for each payment row": counts payment rows, and Q-6 matches nothing.
- d, "7, every order and every payment": adds both sides, which no join does.

### Q2. What does the LEFT join, orders first, add?

`orders o LEFT JOIN payments p ON p.order_id = o.order_id`. Which order carries NULL payment columns, and how many rows does the join return?

The key is a, "A-4, and 6 rows". The LEFT join keeps the 5 pairs and adds A-4, the order nobody paid, with NULL payment columns: 6 rows.

- b, "A-7, and 6 rows": A-7 is a payment's order id and is not in `orders`, so a LEFT join from orders never shows it.
- c, "A-4, and 5 rows": forgets that LEFT adds A-4 back.
- d, "no order, and 7 rows": 7 is the FULL join's count.

### Q3. Which query answers the platform lead's question? (Design)

The data platform lead asks: "Is every payment row in the feed explained by an order we booked?" Which query answers him?

The key is b, "payments LEFT JOIN orders, reading the order columns". "Every payment row" must all survive, so the query starts from `payments` and reads the order columns; Q-6 shows NULL there.

- a, "orders LEFT JOIN payments, reading the payment columns": starts from orders, so Q-6 never appears.
- c, "orders INNER JOIN payments, counting the matched rows": drops Q-6 too.
- d, "orders LEFT JOIN payments WHERE the payment is NULL": lists unpaid orders, which is Anand's question; the lead asked about payments.

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

Each question below is asked of Kalpa's orders and payments. For which one is an INNER join the honest choice?

The key is d, "For paid orders only, how many days until the first payment?". Days to the first payment exist only for orders that were paid, so the unmatched orders are outside the question by definition.

- a, "How many Q2 orders were never paid at all?": needs the orders nobody paid, which INNER drops.
- b, "What did each channel book in the quarter?": needs every order, paid or not.
- c, "Which payment rows match no order in the orders table at all?": needs payments with no order, which INNER drops.

## Which item is worth arguing about?

On item 4, option c, a pair will point out that customers do pay ahead of delivery in some
businesses. The answer is that "ahead" still means against a booked order: cash with no booked order
behind it goes to the platform lead as a question and stays out of collections. Treat any statement
that reads over 100 percent collected as a warning sign, whatever story explains it.

## Where does this pattern live in production?

Razorpay's Orders API combines several payment attempts under one order, and fetching an order's
payments returns every authorised or failed attempt for it (Razorpay documentation, checked 1 Oct
2026), so every merchant reconciling the two lists makes this chapter's choice of join first.

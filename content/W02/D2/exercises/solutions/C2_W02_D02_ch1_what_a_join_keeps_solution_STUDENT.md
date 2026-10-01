# Solution: which rows does each join keep, drop or repeat?

Answers: 1b 2a 3b 4a 5c 6d

## What does this set test?

Which rows survive a join, counted by hand on tables the chapter never used, and which table a
question has to start from. Items 3, 5 and 6 are design items: the join a different question needs,
a row count predicted from the keys alone, and the one question an INNER join answers honestly.

## Why does each key hold, item by item?

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | predict | b | A-1 matches once, A-2 twice (Q-2 and its repeat Q-3), A-3 twice (two instalments): 1 + 2 + 2 is 5. A-4 and Q-6 find no partner. | a: counts orders, and a join writes one row per matching pair. c: counts payment rows, and Q-6 matches nothing. d: adds both sides, which no join does. |
| 2 | predict | a | The LEFT join keeps the 5 pairs and adds A-4, the order nobody paid, with NULL payment columns: 6 rows. | b: A-7 is a payment's order id and is not in `orders`, so a LEFT join from orders never shows it. c: forgets that LEFT adds A-4 back. d: 7 is the FULL join's count. |
| 3 | design | b | "Every payment row" must all survive, so the query starts from `payments` and reads the order columns; Q-6 shows NULL there. | a: starts from orders, so Q-6 never appears. c: drops Q-6 too. d: lists unpaid orders, which is Anand's question, not the lead's. |
| 4 | trap | a | Starting from payments drops A-4, the one unpaid order, and carries Q-3 (A-2's payment posted a second time) and Q-6's 500, which pays an order Kalpa never booked. | b: A-3's two instalments are two real payments of 1,400 and 1,000. c: cash against bookings cannot honestly exceed them. d: A-7 is missing from the orders table, so Kalpa never booked it. |
| 5 | design | c | INNER writes a x b per key: X gives 1 x 3 = 3. LEFT adds Y once, RIGHT adds Z's 2 rows: 3 + 1 + 2 is 6. | a: counts one row per key plus a repeat. b: forgets that Z's two payment rows each come out. d: counts Y's order twice. |
| 6 | design | d | Days to the first payment exist only for orders that were paid, so the unmatched orders are outside the question by definition. | a: needs the orders nobody paid, which INNER drops. b: needs every order, paid or not. c: needs payments with no order, which INNER drops. |

## Which item is worth arguing about?

Item 4, option c. Customers do pay ahead of delivery in some businesses, and a pair will say so. The
answer is that "ahead" still means against a booked order: cash with no booked order behind it is a
question for the platform lead, never extra collections. The statement over 100 percent is the
chapter's warning sign, whatever story explains it.

## Where does this pattern live in production?

Razorpay's Orders API combines several payment attempts under one order, and fetching an order's
payments returns every authorised or failed attempt for it (Razorpay documentation, checked 30 Sep
2026), so every merchant reconciling the two lists makes this chapter's choice of join first.

# Solution: rows in, rows out, and the difference named

Answers: 1c 2b 3a 4d 5a 6b 7d 8c

## The idea being tested

Every join answers a question about the rows that do not match, so the join is chosen by that
question. Once chosen, it is done only when its row count is explained: rows in from the source table,
rows out from the join, and the difference named. The tiny tables show both failures the count
catches: an INNER join that loses an order quietly, and a LEFT join whose gap still carries a
payment posted twice.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | "Nobody has paid" is a question about orders with no match, which is the anti-join: LEFT JOIN, then keep the rows where the payment side is NULL. | a: an INNER join drops exactly the orders asked for. b: returns every order, paid and unpaid, and leaves the reader to find the NULLs. d: adds payments with no order, which Anand did not ask about. |
| 2 | b | "Every order, paid or not" is the LEFT join, with payments summed per order first. | a: drops the unpaid orders, and the gap with them. c: returns only the unpaid orders. d: adds orphan payments to a report about orders. |
| 3 | a | Days to payment exist only for orders that were paid, so the matched pairs are the honest population, and INNER is the honest choice. | b: keeps unpaid orders whose days to payment are NULL, which is harmless to AVG and misleading to a count beside it. c: returns only the orders with no payment. d: adds payments with no order date. |
| 4 | d | "On either side" is the FULL join: unpaid orders and unclaimed payments in one result. | a: drops both kinds of break. b: shows only the unpaid orders. c: shows only the unpaid orders, with the matches removed. |
| 5 | a | Payment methods exist only for paid orders, so the INNER join answers the question as asked. | b: adds unpaid orders with a NULL method. c: returns only orders with no method at all. d: adds orphan payments that belong to no channel. |
| 6 | b | Four orders in the report against five in the table: the INNER join dropped T-4, and its booked 800 left the gap with it. | a: collected matching the feed is true here and proves nothing about orders. c: a channel split of a report that lost an order still lost it. d: DISTINCT on amounts collapses unrelated payments and hides the question. |
| 7 | d | Booked 5,800 less T-4's 800 never paid is 5,000 truly collected; the feed posted 6,500 because P-5 repeats T-3's 1,500. 5,000 plus 1,500 less 5,800 is 700 more posted than booked. | a: there are no refunds in the tiny tables. b: P-7 never enters a LEFT join from orders. c: T-2's instalments add to exactly its booked 2,000. |
| 8 | c | Count what came in, run the join and count what came out, explain the difference, prove booked survived the join, and only then send. | a: runs the join before knowing what it should return. b: sends the number before the difference is explained. d: sends first and checks afterwards. |

## The part worth arguing about

Item 3. Some of the room will say LEFT is always safer. For a question about paid orders only, an
INNER join is the honest choice, and a LEFT join invites someone to read the unpaid orders' NULLs as
a speed. The answer to "When is an INNER join the honest choice?" is: when the question is about
matched rows only, and the report says so beside the number.

Item 7 is the bridge to round 3. The LEFT join fixed the lost order and left the retry inside
collected, so the gap came out negative. The count of orders closes; the money does not yet.

## Where the pattern lives in production

A revenue bridge is how finance teams explain the move between two numbers that ought to agree:
booked to collected, invoiced to paid, one month's close to the next. Each step names a population
of rows and its value, and the bridge closes to the rupee. A data team that hands Finance a joined
number without that bridge will be asked for it.

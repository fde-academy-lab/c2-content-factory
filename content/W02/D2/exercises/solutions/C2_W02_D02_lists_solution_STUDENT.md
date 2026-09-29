# Solution: the unpaid list and the double-paid list

Answers: 1b 2c 3d 4b 5c 6a 7d 8a

## The idea being tested

Two lists answer Anand's "which orders". The unpaid list is an anti-join, and the only WHERE on the
right-hand table that belongs there is IS NULL on its key; any other condition on that table belongs
in the ON clause, or the LEFT join becomes an INNER one. The double-paid list is a HAVING at the right
grain: a retry is the same instalment posted twice, so the grain is order and instalment, never order
alone.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | The LEFT join keeps T-4 with a NULL paid_date, and NULL BETWEEN anything is unknown, so the WHERE removes it: six rows, the INNER join's answer. | a: the WHERE runs after the join and filters its rows, LEFT or not. c: a date filter removes no repeats. d: P-7 never enters a LEFT join from orders, so it had nothing to lose. |
| 2 | c | In the ON clause the date decides which payments attach, and every order survives; an order with no payment in the window keeps NULLs. | a: keeps T-4, and drops any order whose only payment fell outside the window, which vanishes again. b: the WHERE still filters the NULL rows after the FULL join. d: HAVING filters groups, and a paid_date is not a group property. |
| 3 | d | The LEFT join keeps unpaid orders with a NULL payment_id, and IS NULL on the right side's key keeps exactly those. | a: an INNER join has no NULL payment rows to keep, so it returns nothing. b: an unpaid order's amount is NULL, and NULL = 0 is never true. c: COUNT(*) counts the one NULL-padded row, so no group has a count of zero; COUNT(p.payment_id) would have been right. |
| 4 | b | Two payment rows on one order is also what a legitimate two-instalment order looks like, so the 216 mix instalments with retries until instalment_no splits them. | a: calls every second instalment a double payment and asks the payments team to reverse real money. c: chooses by size a list that is wrong by grain. d: stops the note for a reason that would let the wrong list stand. |
| 5 | c | T-3's two rows carry the same instalment number, the same amount and the same date, which is one payment posted twice. | a: two rows is the symptom both orders share. b: T-2's rows are instalments 1 and 2, a month apart, adding to exactly its booked 2,000. d: T-3 received its 1,500 twice, which is more than it booked. |
| 6 | a | The instalment was due once and posted twice, so one posting of 1,500 is the surplus. | b: counts the legitimate posting as surplus too. c: halves an amount that was posted in full each time. d: compares against booked and misses the extra posting. |
| 7 | d | A payment no order claims cannot be collected against anything in the book; it stays out of the report and goes to the platform lead with its id and amount. | a: puts money in collected with no order behind it, so the report no longer reconciles to orders. b: invents a match. c: loses a real payment without telling anyone who can trace it. |
| 8 | a | With retries removed at order grain, booked less collected is exactly the booked value of the orders with no payment, so the list and the gap must agree to the rupee. | b: the feed's posted total still carries the retries, so this gap is short by the surplus. c: an estimate where an exact sum exists. d: a gap may exist; the check is that it is explained. |

## The part worth arguing about

Item 2, option a. Adding `OR p.paid_date IS NULL` looks like it repairs the query, and on the tiny
tables it does, because every order paid inside the window. Picture an order paid only in October:
its row carries a non-NULL date outside the window, fails both halves of the WHERE, and the order
disappears from a report that promised every order. The ON clause is the one version that keeps every
order under every calendar.

Item 4 is Kavya's review in one item. The count HAVING COUNT(*) > 1 returns is a real count of real
orders, and it is a count of the wrong thing.

## Where the pattern lives in production

Payment gateways retry on timeouts, and every payments team keeps an idempotency key so that a retry
is recognised as the same payment. When the key is missing from an analytics feed, the analyst
rebuilds it from the grain: same order, same instalment, same amount, close in time. The unmatched
payments go to a suspense account and the team that owns the feed, never into revenue.

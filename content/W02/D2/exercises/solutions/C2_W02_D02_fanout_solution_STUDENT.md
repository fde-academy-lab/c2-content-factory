# Solution: the join that multiplied

Answers: 1c 2a 3d 4b 5b 6d 7a 8c

## The idea being tested

A key that repeats on one side multiplies the other side's rows before any number is summed. The
invented extract makes the four row counts countable by hand; the Kalpa items show the same
multiplication producing a number that looks like good news, and the fix that brings both tables to
one row per order before they meet.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | Q-1 to Q-7 each find an order and Q-8 does not, so the INNER join returns seven rows. | a: counts orders, one side's grain only. b: counts Q-8, whose order A-8 is not in the extract. d: counts paid orders and forgets that A-2, A-3 and A-5 each repeat. |
| 2 | a | The seven matched rows, plus A-4 and A-6 with NULL on the payment side, make nine. | b: a LEFT join keeps every order at least once, and more than once when the key repeats. c: the payment count is the RIGHT join's number here. d: ten is the FULL join, which adds Q-8. |
| 3 | d | Each payment matches at most one order, because order_id is unique in orders, so the RIGHT join returns every payment row once: eight. | a: a RIGHT join keeps Q-8 with NULL order columns. b: counts orders, the wrong side. c: the unpaid orders belong to the LEFT join. |
| 4 | b | The FULL join keeps the LEFT join's nine rows and adds Q-8, the payment no order claims: ten. | a: misses Q-8. c: adds the two tables' row counts, which no join does. d: counts payments and loses A-4 and A-6. |
| 5 | b | Rs 19,29,04,410 is 1.96 times booked, and a total that large needs its row count explained first: rows in against rows out shows the join repeated every order that has two payment rows. | a: every row is real, and the order amount is summed once per payment row, which is the fault. c: sends a multiplied number to Anand with a story attached. d: Q1 would fan out the same way and prove nothing about the count. |
| 6 | d | Each of the 216 two-row orders adds one extra row, so 462 plus 216 is 678. | a: a LEFT join keeps each order at least once, never exactly once when the key repeats. b: doubles every order, including those with one row or none. c: subtracts where the join adds. |
| 7 | a | Monday's booked for Q2 is Rs 9,84,00,000, and this report's booked is about twice that, so the orders column was summed once per payment row. | b: a collection rate below half is possible, and here it is an artefact of the doubled booked. c: collected is summed from payments, which the join does not multiply. d: a missing channel split is a presentation problem, and the number is still wrong with it. |
| 8 | c | Summing payments per order first brings them to the orders table's grain, so the LEFT join returns 462 rows and booked equals booked. | a: two different orders with the same amount collapse into one. b: an INNER join still repeats two-row orders and drops the unpaid ones as well. d: grouping after the join sums the repeated rows, so nothing cancels. |

## The part worth arguing about

Item 5, option d. Running a second quarter feels like diligence, and it is a comparison that shares
the same mistake. The check that catches a fan-out is inside the query: orders in, rows out. Kavya's
review sets the order of work: the grain of each table first, the total afterwards.

## Where the pattern lives in production

Every finance dashboard that joins a header table to a line table carries this risk: orders to
payments, invoices to invoice lines, customers to addresses. Data teams guard it with a test that
the joined table has as many rows as its driving table, and pandas guards it with `validate=` on a
merge, which Thursday's session uses as the loud version of today's count check.

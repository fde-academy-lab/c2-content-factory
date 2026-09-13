# Unguided: which join answers this

Five questions somebody at Kalpa actually asks. For each, pick the join that answers it. The wrong
choices are not absurd; each one answers a nearby question, which is what makes this worth doing.

## Q1.

Anand: "Which delivered orders have we not been paid for?" Which one appears?

a) `INNER JOIN` payments, then filter the result on order status
b) `LEFT JOIN` payments, keep rows where the payment is NULL
c) `RIGHT JOIN` payments, keep rows where the order id is NULL
d) `FULL OUTER JOIN`, then filter on either of the sides being NULL

## Q2.

The platform lead: "Is the gateway sending us anything for orders we do not have?" Which one
appears?

a) `LEFT JOIN` from payments, keep the NULL orders
b) `INNER JOIN` both ways, then compare the two counts
c) `LEFT JOIN` from orders, keep the NULL payment rows
d) `FULL OUTER JOIN`, then count every row returned

## Q3.

Marketing: "Total revenue per channel for orders that were actually paid." Which one appears?

a) `LEFT JOIN` payments, and then sum the order amount
b) `INNER JOIN` payments, and then sum the order amount
c) Aggregate payments per order, `INNER JOIN`, then sum
d) `RIGHT JOIN` payments, then sum the payment amounts

## Q4.

Anand: "Show me both sides of every mismatch in one table, so I can see the whole reconciliation
at once." Which one appears?

a) `LEFT JOIN`, run once from each of the two sides
b) Two anti-joins, stacked together with `UNION ALL`
c) `INNER JOIN` with a count comparison printed beside it
d) `FULL OUTER JOIN`, keeping rows where a side is NULL

## Q5.

You: "How much did we actually collect in Q2, one number, safe to send." Which one appears?

a) `SUM(p.amount)` taken over a `LEFT JOIN` from orders
b) Aggregate payments per order, then `LEFT JOIN` and sum
c) `SUM(p.amount)` taken over an `INNER JOIN` to payments
d) `SUM(o.amount)` over a `LEFT JOIN`, booked being collected

## Answering

Post one line: the five letters in order. Then pick Q3 and write one sentence on what option a
would have given you and why nobody would have noticed.

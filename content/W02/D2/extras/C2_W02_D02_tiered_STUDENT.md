# Tuesday's extras

## Recovery: if the fan-out is still a blur

Build your own six-row version. Open a scratch file and write two tiny tables by hand: four
orders and six payments, where one order has two payment rows and one has none.

Now, on paper, write out every row a `LEFT JOIN` produces. Not the count, the rows. Then add the
order amount column and compare it with the sum of the four order amounts.

Do it again with five payments instead of six and see the total change. The point is to feel the
multiplication rather than to learn its name.

Then take the six-row example from today's board and redo step 6 of the guided exercise: roll the
payments up first, and say why the row count is now guaranteed.

## Stretch: three that need a turn you have not been shown

**One.** Some orders in the book were returned, and `refunds` holds a negative row for each.
Compute net collected for Q2 by channel: collected, minus refunds, per channel. You now have two
tables that can both fan out against `orders`. Join them naively first and record what happens to
the row count, then fix it. Write the reconciliation for the two-fan-out case; it is not the same
sentence as today's.

**Two.** Fifty orders were charged twice by a gateway retry. Write one query that returns, per
channel, how much money the retries represent. Then answer in a comment: is that number a gap, a
surplus, or neither, and who at Kalpa should receive it?

**Three.** Today's fix aggregates payments before joining. There is a second way to get the same
answer that does not use a CTE at all, using a correlated subquery in the `SELECT` list. Write it,
confirm it matches, and then write one sentence on which of the two you would put in front of
Anand's analyst and why. This one is about readability rather than correctness, and the honest
answer may not be the clever one.

## If you want tomorrow's advantage

Run this and look at the output:

```sql
SELECT customer_id, sum(amount) AS q2
FROM orders WHERE quarter = 'Q2' GROUP BY customer_id ORDER BY q2 DESC LIMIT 60;
```

Somewhere in that list two customers have exactly the same total. Find them. Tomorrow the head of
Retail-Plus has an opinion about what should happen to them.

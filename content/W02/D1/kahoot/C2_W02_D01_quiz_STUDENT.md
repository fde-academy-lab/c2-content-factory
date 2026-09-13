# Monday's Kahoot: the first day of SQL

Ungraded. Seven questions, twenty seconds each, and the last one reaches back to last week.

## Q1. Which of these runs first?

a) FROM <- correct
b) SELECT
c) ORDER BY
d) WHERE

## Q2. `WHERE count(*) > 5` is refused. Why?

a) `count` requires a named column here
b) WHERE accepts equality tests only
c) No group exists yet when WHERE runs <- correct
d) The table holds fewer than five rows

## Q3. `GROUP BY segment, quarter` on four segments and two quarters returns how many rows?

a) 2
b) 4
c) 8 <- correct
d) 1,000

## Q4. `SELECT order_id FROM orders LIMIT 5` returns which five rows?

a) Whichever five the server hands back <- correct
b) The five with the smallest order id
c) The five most recently placed orders
d) The five largest orders by amount

## Q5. In `WITH a AS (...), b AS (...) SELECT ...`, what can block `b` see?

a) Nothing declared outside itself
b) Only the final SELECT block
c) Every block, including itself
d) Block `a` <- correct

## Q6. Last week's presence counter, in one SQL line. Which is it?

a) `SELECT sum(discount) FROM orders`
b) `SELECT count(discount) FROM orders` <- correct
c) `SELECT count(*) FROM orders`
d) `SELECT count(DISTINCT discount) FROM orders`

## Q7. Return question, one level up

Last week the monsoon discount showed a 6 percent lift while every segment separately fell. Say
in one line what a fair comparison would have needed.

a) A larger sample drawn from the same quarter
b) The same test run on revenue rather than order count
c) Groups alike before the sale, compared within segment <- correct
d) A longer observation window on both sides of the sale

## Trainer note

Q4 is the one to slow down on. A room that answers it right in twenty seconds has usually
memorised it rather than understood it, so the follow-up is worth asking aloud: what would have
to change about the table for the answer to change?

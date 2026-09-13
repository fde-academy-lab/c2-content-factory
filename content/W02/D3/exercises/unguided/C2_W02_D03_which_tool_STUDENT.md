# Unguided: GROUP BY or window

Six questions Marketing might send you. For each, say which tool answers it. The wrong options
are not absurd; most of them answer a nearby question.

## Q1.

"Total Q2 revenue for each segment." Which one appears?

a) `GROUP BY segment`, which collapses to one row each
b) A window function partitioned by the segment column
c) `ORDER BY segment` with a running total taken over it
d) `DENSE_RANK` over segment, then filter to position one

## Q2.

"For every customer, their Q2 revenue and their segment's total beside it." Which one appears?

a) `GROUP BY customer_id, segment`, then read both columns
b) Two queries, joined afterwards on segment
c) A window: `sum(revenue) OVER (PARTITION BY segment)`
d) `HAVING sum(revenue) > 0`, which keeps both levels

## Q3.

"The three biggest spenders in each segment." Which one appears?

a) `GROUP BY segment` with a `LIMIT 3` on the result
b) `ORDER BY revenue DESC LIMIT 3`, run once for each segment
c) `rank() OVER (PARTITION BY segment)`, filtered outside
d) `HAVING count(*) <= 3` after grouping by the segment

## Q4.

"How many customers ordered in each month of Q2." Which one appears?

a) `count(*) OVER (PARTITION BY month)` on the order rows
b) `lag(customer_id) OVER (ORDER BY month)`, and then count
c) `dense_rank() OVER (ORDER BY month)`, and then a sum
d) `GROUP BY month`, counting distinct customers

## Q5.

"Each customer's spend this month next to their spend last month." Which one appears?

a) `GROUP BY customer_id, month`, read two rows
b) A self-join of the monthly table onto itself on month minus one
c) `lag(spend) OVER (PARTITION BY customer_id ORDER BY month)`
d) `min(spend) OVER (PARTITION BY customer_id)` subtracted

## Q6.

"Revenue so far, week by week, without losing the weekly figures." Which one appears?

a) `GROUP BY week` with the weeks ordered ascending
b) `sum(revenue) OVER (ORDER BY week_start)` as a window
c) A `HAVING` clause accumulating across the groups
d) `rank() OVER (ORDER BY week_start)` multiplied by revenue

## Answering

Post one line: the six letters in order. Then pick Q2 and write one sentence on what you would
have to do without a window function, and how many queries it would take.

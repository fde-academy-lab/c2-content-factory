# Solutions: GROUP BY or window

Answers: 1a 2c 3c 4d 5c 6b

## Q1. GROUP BY segment

One number per segment, rows collapse, nothing survives that you need. This is what `GROUP BY` is
for and reaching for a window here is over-engineering.

## Q2. A window partitioned by segment

The question asks for two levels of aggregation in one row: the customer's own figure and their
segment's total. `GROUP BY` cannot do it, because it collapses to one level and the customer's row
is gone.

Option b works and takes two queries and a join. Notice that it gives the same answer: a window is
often the shorter way to do something you could do the long way, which is why the question
"which tool" is really "how many passes over the data".

## Q3. RANK partitioned by segment, filtered outside

Top-N within a group. Option a is the classic wrong answer: `LIMIT 3` takes three rows from the
whole result, not three from each group.

Option b is the honest brute-force version and it needs one query per segment, which stops being
practical the moment somebody adds a segment.

## Q4. GROUP BY month, counting distinct customers

The rows should collapse here; nobody wants the individual orders back. Watch the denominator:
`count(*)` counts orders and `count(DISTINCT customer_id)` counts customers, and the question
asked for customers.

## Q5. LAG partitioned by customer, ordered by month

Option b is what people wrote before window functions existed and it is still correct. It also
breaks silently when a customer skips a month, because "month minus one" has no row to join to,
and `LAG` has the same issue with a different symptom. Neither is automatic; both need a decision
about gaps.

## Q6. A running sum over the week order

The weekly figures have to survive, which rules out any answer that collapses them. The window's
`ORDER BY` is what makes the accumulation deterministic, and `week_start` is unique after the
grouping so it cannot tie.

# Solution: round 3 set, two quarters as named steps

Answers: 1d 2b 3c 4a 5d 6b 7c

## The idea being tested

A CTE is a named step that later steps can read, so a query reads top to bottom in the order its
logic runs. Aggregates skip NULLs, and `avg(x)` is `sum(x) / count(x)`, so the denominator of an
average is whoever has a value. When a missing value means zero in the business, the query says so
with `coalesce`.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | d | A later step can read every earlier step and every table in the database. | a, b and c each drop something the final SELECT can see; order of definition only limits what an earlier step can read. |
| 2 | b | A `CASE` with no `ELSE` gives NULL for Q1 orders, a sum of only NULLs is NULL, and `avg` skips NULLs: the 31 members who stopped buying left the denominator. | a: the `CASE` tests the quarter, so no Q1 amount enters the Q2 column. c: `avg` does not round. d: a CTE is computed once for the query. |
| 3 | c | 107 members in the step, 76 with a Q2 value, so 31 were left out. | a: 91 less 76 compares two quarters' buyers, and some members bought only in Q2. b counts members outside the step altogether. d: `count(q2_spend)` already shows 76. |
| 4 | a | With `coalesce`, both averages divide by the same 107 members, so each is that quarter's revenue over 107, and the ratio of two averages is the ratio of two revenues. | b: `coalesce` replaces NULL and rounds nothing. c: sharing a CTE says nothing about the denominators. d: the equality is arithmetic and holds for any data with a fixed set. |
| 5 | d | The share divides each segment's revenue by the total of both quarters, which is a query of its own, written in brackets as a subquery. | a, b and c are parts of the outer query and need nothing inside it. |
| 6 | b | Frequency fell furthest, 22.0 percent, and it is Week 1's lever at warehouse scale. | a: customers fell 16.5 percent, the second branch. c: rising order value softens the fall and is no headline. d: revenue is the result the branches explain. |
| 7 | c | A comment per step says what it computes and what it divides by, and changes no number. | a hides a step inside a line. b lets two runs return rows in different orders. d changes the numbers. |

## The part worth arguing about

Item 3, option b. Some learners want 120 as the denominator, every Retail-Plus member on the book.
That is a defensible definition too, and it gives the same 29.4 percent fall, because it is also a
fixed set of people. What is never defensible is the hurried denominator, which changes between the
two quarters without anybody deciding it should.

## Where the pattern lives in production

"Average revenue per active user" is the textbook case: when a user who stopped buying drops out of
the average, the metric rises while the business shrinks. Teams guard it by fixing the cohort first
and stating the denominator beside the number.

PostgreSQL 16 documentation, aggregate functions, https://www.postgresql.org/docs/16/functions-aggregate.html (verified 29 Sep 2026)
PostgreSQL 16 documentation, WITH queries, https://www.postgresql.org/docs/16/queries-with.html (verified 29 Sep 2026)

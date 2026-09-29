# Extras: one to stretch, one to recover

Both are optional and neither is graded. Pick the one that matches where you actually are.

---

## Stretch: the suite that checks itself

You finished the suite early and every number matched. Then this one is for you.

**The situation.** Anand's analyst writes back.

> "Your six queries are fine today. What tells me, next Monday, that one of them has quietly gone
> wrong before I read a number from it?"

**What to build.** A seventh query, `suite_7_checks`, that returns one row per check with a column
saying PASS or FAIL, computed with `CASE`. At least these four:

| Check | What it compares |
|---|---|
| The segments add back | The eight segment-quarter order counts summed, against count(*) over orders |
| The customers are people | count(DISTINCT customer_id) against count(*), which must differ |
| No ratio came out whole | Every orders-per-customer value in query 3, tested for a fraction |
| Revenue reconciles | The revenue in query 6's steps, against the revenue per quarter in query 1 |

**The hard part, and the point.** A check that can never fail proves nothing. For each of your four,
write one line saying which mistake would turn it to FAIL, then make that mistake in a copy of the
suite and watch it happen.

**If you want more.** PostgreSQL Exercises, the aggregates category, https://pgexercises.com/questions/aggregates/ (verified 29 Sep 2026)

---

## Recovery: one clause at a time

The morning moved fast, the grouping did not land, and you would rather rebuild it than pretend.
Run each line in `sql/`, one change at a time, and check the number before the next change.

| Step | What you add | The number you should see |
|---|---|---|
| 1 | `SELECT count(*) FROM orders;` | 1000 |
| 2 | `WHERE quarter = 'Q2'` | 462 |
| 3 | Replace count(*) with `count(DISTINCT customer_id)` | 227 |
| 4 | Remove the WHERE, add `quarter,` after SELECT and `GROUP BY quarter` at the end | two rows, 244 and 227 |
| 5 | Add `count(*) AS orders,` to the SELECT | 538 and 462 beside the customers |
| 6 | Add `round(count(*)::numeric / count(DISTINCT customer_id), 2)` | 2.20 and 2.04 |

**The point of it.** Each step adds one clause, so when a number surprises you, the clause you just
added is where to look. Say aloud, at each step, which clause the database ran first.

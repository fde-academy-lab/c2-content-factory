# Which extra fits you tonight: rebuilding the book one clause at a time, finding where Retail-Plus lost its buyers, or making the suite check itself?

All three are optional and none is graded. Each stands on its own, so pick the one that matches
where you are after today's six chapters on Anand Iyer's Monday numbers. Anand, Kalpa Retail's
finance controller, wants the revenue tree every Monday for every segment, computed from the
warehouse itself, and his analyst audits every line. The warehouse is Kalpa's Postgres database,
`kalpa`, and its orders table holds the book: 1,000 orders over Q1 (April to June 2026) and Q2 (July
to September 2026), with each order's segment on the customers table.

---

## Recover: can you rebuild the book's leaves one clause at a time, and say which clause runs first?

This one is for you if the morning moved fast and grouping did not land.

**Who needs the answer.** Anand's analyst reads every query in the order the database runs it, and
every number on his sheet rests on the leaves below. If you can say which clause ran first at each
step, you can explain any number the suite prints.

**The questions on the way.**

1. What does each added clause change in the result?
2. Which clause runs first at each step?
3. What should the comment above the finished query say?

### What does each added clause change in the result?

Open a new query window connected to `kalpa` and build one query, a clause at a time. Run it after
every change and check the number before you make the next one.

| Step | What you add or change | What you should see |
|---|---|---|
| 1 | `SELECT count(*) FROM orders;` | 1000 |
| 2 | Add `WHERE quarter = 'Q2'` before the semicolon | 462 |
| 3 | Change `count(*)` to `count(DISTINCT customer_id)` | 227 |
| 4 | Remove the `WHERE`, put `quarter,` after `SELECT`, and end with `GROUP BY quarter ORDER BY quarter` | Two rows: 244 and 227 |
| 5 | Add `count(*) AS order_rows,` after `quarter,` | 538 and 462 beside the customers |
| 6 | Add `round(count(*)::numeric / count(DISTINCT customer_id), 2) AS orders_per_customer` | 2.20 and 2.04 |
| 7 | Add `HAVING count(DISTINCT customer_id) > 230` before `ORDER BY` | One row, Q1 |

When a number surprises you, the clause you just added is where to look.

### Which clause runs first at each step?

Say it aloud at every step, using the run order: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY,
LIMIT. At step 2 `WHERE` throws away the Q1 rows before anything is counted. At step 4 `GROUP BY`
forms two groups before `SELECT` counts inside each. At step 7 `HAVING` runs after the groups exist
and before `SELECT`, which is why it can test a count that `WHERE` never sees; Q2's 227 customers fall
under the bar and its row goes.

### What should the comment above the finished query say?

It should say what each count counts, in words an auditor can check, for example
`-- order_rows: every order in the quarter; customers: customers who bought in it, each counted once`.
Kavya's rule from chapter 1 is that a count says what it counts, in its name and in the comment above
it.

---

## Practise: did Retail-Plus lose more of its Q1 buyers than Retail-Core, or gain fewer new ones in Q2?

This one is for you if the chapters landed and you want the same methods on a question nobody has
answered yet.

**Who needs the answer.** The head of Retail-Plus decides whether to spend on keeping the members who
buy now or on bringing in members who skipped a quarter. Chapter 3 found Retail-Plus's customers fell
from 91 to 76 and Retail-Core's from 102 to 96, and a net fall hides two movements that point to
different plans.

**The questions on the way.**

1. How many of each segment's Q1 buyers bought again in Q2?
2. How many Q2 buyers had not bought in Q1?
3. Do the three groups add back to each segment's half-year buyers?
4. What does the head of Retail-Plus hear?

### How many of each segment's Q1 buyers bought again in Q2?

Build one row per customer who bought, with the first and last quarter they bought in, as chapter 2's
second route did. A customer whose first quarter is Q1 and last is Q2 bought in both. Complete the
two missing columns yourself.

```sql
WITH per_customer AS (   -- one row per customer who bought, with the quarters they bought in
    SELECT c.segment, o.customer_id,
           min(o.quarter) AS first_q, max(o.quarter) AS last_q
    FROM   orders o JOIN customers c USING (customer_id)
    GROUP  BY c.segment, o.customer_id
)
SELECT segment,
       count(*) FILTER (WHERE first_q = 'Q1')                   AS q1_buyers,
       count(*) FILTER (WHERE first_q = 'Q1' AND last_q = 'Q2') AS kept,
       -- q1_only: bought in Q1 and not in Q2; q2_only: bought in Q2 and not in Q1
       count(*)                                                 AS half_year
FROM   per_customer
GROUP  BY segment
ORDER  BY segment;
```

Then divide `kept` by `q1_buyers` in `numeric`, round on purpose, and keep both counts beside the
share, as chapter 3 did.

### How many Q2 buyers had not bought in Q1?

Your `q2_only` column answers it, and the same count for the whole book should be chapter 2's 57.

### Do the three groups add back to each segment's half-year buyers?

They must, because every customer who bought falls in exactly one of kept, Q1 only and Q2 only.
Chapter 5 counted the half-year from the orders: Business 39, Retail-Core 131, Retail-Plus 107 and
Student 24, 301 in all.

### What does the head of Retail-Plus hear?

Check your numbers against these before you write the line.

| Segment | Q1 buyers | Kept into Q2 | Share kept | Q1 only | Q2 only | Half-year |
|---|---|---|---|---|---|---|
| Business | 36 | 32 | 88.9% | 4 | 3 | 39 |
| Retail-Core | 102 | 67 | 65.7% | 35 | 29 | 131 |
| Retail-Plus | 91 | 60 | 65.9% | 31 | 16 | 107 |
| Student | 15 | 11 | 73.3%, flagged | 4 | 9 | 24 |

Retail-Plus kept its Q1 buyers at the same rate as Retail-Core, 65.9 percent against 65.7. Its
customers fell further because only 16 buyers arrived in Q2 who had not bought in Q1, against
Retail-Core's 29. The head of Retail-Plus hears that the tier keeps its buyers as well as its
neighbour does and wins fewer of the members who skipped a quarter. That holds for the customer
branch only, since chapter 4 found the tier's frequency fell further, 22.0 percent against 16.5.
Student's share rests on 15 customers and goes on the sheet flagged.

---

## Stretch: can the Monday suite tell the analyst, by itself, that one of its numbers has gone wrong?

This one is for you if you finished the take-home and every number matched.

**Who needs the answer.** Anand's analyst writes back to the team.

> "Your suite is right today. What tells me, next Monday, that one of its numbers has gone wrong
> before I read it?"

**The questions on the way.**

1. Which checks can the suite run on itself?
2. How does one query turn each check into PASS or FAIL?
3. Would each check catch the mistake it guards against?
4. Did your checks land where they should?

### Which checks can the suite run on itself?

| Check | What it compares | The mistake it catches |
|---|---|---|
| Segments add back | The four segments' Q1 customers summed, against the book's Q1 customers | A segment lost or counted twice |
| Customers are people | Each quarter's customers against its orders, which must differ | `count(*)` labelled as customers |
| Ratios multiply back | Orders per customer times customers, against the orders, within rounding | Whole-number division |
| Half-year within the tier | Each segment's half-year buyers, against its members on the customer table | Quarter rows added for the half-year |
| The book held | This run's rows and rupees, against last Monday's fingerprint | A book that changed under the suite |

### How does one query turn each check into PASS or FAIL?

The query returns one row per check, stacked with `UNION ALL` as the fingerprint was, and each row
is a `CASE` on a count of the rows that break its rule. Two checks are written; write the other three
the same way. The rounding
allowance is half a hundredth per customer, since the ratio is rounded to two places.

```sql
WITH seg AS (    -- the suite's middle table: each segment and quarter
    SELECT c.segment, o.quarter, count(*) AS orders,
           count(DISTINCT o.customer_id) AS customers
    FROM   orders o JOIN customers c USING (customer_id)
    GROUP  BY c.segment, o.quarter
)
SELECT 'ratios multiply back' AS check_name,
       CASE WHEN (SELECT count(*) FROM seg
                  WHERE abs(round(orders::numeric / customers, 2) * customers - orders)
                        > customers * 0.005) = 0
            THEN 'PASS' ELSE 'FAIL' END AS result
UNION ALL
SELECT 'the book held',
       CASE WHEN (SELECT count(*) = 1000 AND sum(amount) = 198400000 FROM orders)
            THEN 'PASS' ELSE 'FAIL' END
ORDER  BY check_name;
```

### Would each check catch the mistake it guards against?

A check that can never fail proves nothing. In a copy of the suite, make each mistake on purpose and
watch its check turn to FAIL: drop the `::numeric` from the ratio, label `count(*)` as customers, and
build the half-year by adding each segment's two quarter rows.

### Did your checks land where they should?

On today's book all five return PASS. With the cast dropped, Retail-Plus's Q1 ratio prints 2, and 2
times 91 is 182 against 215 orders, so the ratio check fails in all eight rows. With `count(*)` as
customers, Q1 shows 538 customers beside 538 orders, and "customers are people" fails. With the
quarters added, Retail-Plus shows 167 half-year buyers against 120 members and Business 71 against
40, so the tier check fails in every segment.

# Solution: one question, three tools

The executed notebook is `exercises/solutions/C2_W02_D04_three_tools_solution_STUDENT.ipynb`.
Its five placeholders fill as: the set for distinct members, the `::numeric` cast, the `WHERE`
filter on segment, `("customer_id", "nunique")` for members, and the SQL view for Finance.

## The SQL, written first

```sql
SELECT o.quarter,
       count(*) AS orders,
       count(DISTINCT o.customer_id) AS members,
       round(count(*)::numeric / count(DISTINCT o.customer_id), 3) AS per_member
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE c.segment = 'Retail-Plus'
GROUP BY o.quarter
ORDER BY o.quarter;
```

| quarter | orders | members | per_member |
|---|---|---|---|
| Q1 | 215 | 91 | 2.363 |
| Q2 | 140 | 76 | 1.842 |

Without `::numeric`, Postgres divides two integers and returns 2 and 1, Monday's trap. With
`count(*)` in the denominator instead of `count(DISTINCT ...)`, the rate reads 1.000.

## Where each tool breaks if it is written carelessly

| Tool | The careless version | What it reports |
|---|---|---|
| Plain Python | a list of member ids instead of a set | 1.000, a member counted once per order |
| SQL | integer division | 2 and 1 |
| pandas | `("customer_id", "count")` for members | 1.000 again |

## A model note to Kavya

"Retail-Plus members placed 2.363 orders each in Q1 and 1.842 in Q2, a fall of 22 percent,
computed from the warehouse's 355 Retail-Plus orders, and plain Python, SQL and pandas agree to
three places. Plain Python is for showing a new joiner or a reviewer every step, because they
have to check it by hand. SQL is for anything Finance or an auditor reruns, because it runs
where the data lives and gives the same answer to anyone who runs it. pandas is for the
analyst's iteration between those, merging a file or trying five cuts in an afternoon, because
it changes in a line and draws as it goes. I would refuse a hand-edited spreadsheet for Finance's
Monday number, because a typed-over cell leaves no trail back to the warehouse."

## What the debrief listens for

A reason that names who must trust the number. The refusal is the sentence most notes get
wrong: refusing pandas for Finance is defensible only when the reason is where the number is
born, never that pandas is less accurate, since all three agreed to three places.

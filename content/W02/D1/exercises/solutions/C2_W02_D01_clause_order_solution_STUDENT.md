# Solutions: what runs when

Answers: 1a 2d 3c 4d 5c

## Q1. WHERE cannot use the alias

`SELECT` runs after `WHERE`, so at the moment `WHERE` is evaluated the name `revenue` has not been
created. The error is `column "revenue" does not exist`, which sounds like a typo and is really a
timing statement.

The fix is to repeat the expression, or to wrap the query in a CTE and filter outside it.

## Q2. HAVING, once the groups exist

`WHERE` judges one row at a time and has no access to a group that has not been formed. `HAVING`
runs immediately after `GROUP BY` and judges whole groups, which is the only place `count(*) > 100`
is a meaningful question.

## Q3. Refused, and the message says why

`ERROR: column "o.channel" must appear in the GROUP BY clause or be used in an aggregate function.`

`SELECT` has one row per segment to fill and three candidate channels for each. There are two
honest fixes and they answer different questions: add `channel` to the grouping and get twelve
rows, or wrap it as `count(DISTINCT channel)` and keep four.

## Q4. ORDER BY runs after SELECT

Sorting happens on the computed output, so the alias exists by then. This asymmetry is the single
clearest piece of evidence that the written order and the run order differ, which is why it is
worth meeting on the first day rather than the fourth.

## Q5. One run proves nothing

Postgres makes no promise about row order without `ORDER BY`. A sequential scan of a freshly
loaded table often does come back in insertion order, which is exactly why this belief survives:
it is right often enough to feel like a rule and wrong at the worst possible moment, such as after
a table is vacuumed or a parallel scan kicks in.

Option b is the tempting one. Size is not the trigger; the plan is, and the plan can change
without the table changing at all.

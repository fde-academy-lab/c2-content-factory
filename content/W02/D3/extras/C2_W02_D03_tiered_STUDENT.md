# Wednesday's extras

## Recovery: if the three functions still blur

Do this with six numbers and a pen, not with SQL.

Write down: 10, 9, 9, 9, 7, 5. Number them three ways in three columns. Then do it again with
10, 10, 9, 8, 8, 8 and notice that the columns disagree in two places now instead of one.

The rule you are looking for: `RANK` tells you how many rows are ahead of you, `DENSE_RANK` tells
you how many distinct values are ahead of you. Say that sentence out loud against both examples
until it predicts the columns rather than describing them.

Then take today's guided walk, query 3, and change `revenue DESC` to `revenue ASC`. Predict what
happens to all three columns before running it.

## Stretch: three that need something you have not been shown

**One.** The protect list ranks by Q2 revenue. Marketing would rather protect members who are
falling, which is a different list. Build one ranking that combines both: position by Q2 revenue,
but only among members whose September spend is below their July spend. Then write one sentence
on whether combining the two into a single ranking is a good idea or a way of hiding a decision.

**Two.** The running total is against a flat plan line of thirteen equal weeks. Real plans are
not flat. Reshape the plan so it is weighted toward the festive weeks of September, then rerun
the comparison and say what changes about the story you would tell Meera. The SQL is easy; the
question is which version is more honest and why.

**Three.** `RANK` and `DENSE_RANK` both keep ties. There is a third behaviour nobody asked for:
splitting the tie by a second column so it never happens. Write that version, then write one
sentence on why the head of Retail-Plus would be annoyed by it even though it produces exactly
fifty names.

## If you want tomorrow's advantage

Tomorrow the same questions get answered a third time, in pandas, and one of them raises an error
on purpose.

Run this tonight and look at what comes back:

```sql
psql -c "SELECT customer_id, count(*) FROM campaign_exposure
         GROUP BY customer_id HAVING count(*) > 1;"
```

Do not fix anything. Just read what comes back, and think about what a merge on `customer_id`
would do with it.

# Self-check before you hand in Tuesday's take-home

Ten checks. Six or fewer passing means it is not finished.

## The join itself

1. Can the right side of your join carry more than one row per key? If not, the brief's constraint
   is unmet and you need a different pair of tables.

2. Did you take the row count **before** you took any total? Not "did you end up with both
   numbers", but did the count come first. If the total came first, you did not test the habit.

3. Run the query with `INNER` instead of your join type and compare the counts. Can you say what
   the difference is made of? If the counts match, say why.

## The reconciliation block

4. Does your "Difference" line name a business cause rather than a data cause? "450 rows extra"
   is a data cause. "450 orders settled in two instalments" is a business cause.

5. Does your "Therefore" line tell a reader what **not** to do? A therefore that only restates
   the difference is not doing any work.

6. If your difference is zero, does the block say why it is zero? A blank line and a zero look
   identical to a reviewer and mean opposite things.

## The number

7. Total your joined result two ways: over the raw join, and after aggregating the many side
   first. If the two agree, you have proved no fan-out. If they differ, your therefore line has
   to say so.

8. Does any arithmetic in your query touch a column that can be NULL after the join? If yes, is
   there a `coalesce`? Check, do not assume; a single NULL empties a whole aggregate.

## The note

9. Read your four or five sentences and cross out anything that describes what you did. What
   survives should be what the reader should believe and what they should be careful of.

10. Is there one sentence you would add before they use the number? If you cannot think of one,
    either the number is unusually safe, which happens, or you have not looked hard enough. Say
    which of the two it is.

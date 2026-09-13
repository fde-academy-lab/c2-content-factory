# Before Thursday: one question, and a look at a feed

Ten minutes.

## The question to arrive with

You have answered "revenue per segment" twice: in plain Python in Week 1, in SQL on Monday.

Before tomorrow, write one sentence on when you would choose each. Not which is better. When you
would choose each.

Tomorrow a senior analyst asks exactly this in front of the room, and having thought about it for
ninety seconds beforehand is the difference between an answer and a scramble.

## Look at this, and only look

```bash
psql -c "SELECT customer_id, count(*) FROM campaign_exposure
         GROUP BY customer_id HAVING count(*) > 1;"
```

Six rows come back. Do not fix anything. Ask yourself what a merge on `customer_id` would do with
them, and whether you would notice.

## Three words

| Word | What it means here |
|---|---|
| DataFrame | A table in memory, with named columns and an index |
| groupby | Splitting rows by a key so a function can be applied to each group |
| merge | A join, with pandas spelling, and the same fan-out risk |

## One to read, one to watch

- pandas, "10 minutes to pandas", run it cell by cell rather than reading it:
  <https://pandas.pydata.org/docs/user_guide/10min.html> (verified 13 Sep 2026)
- Corey Schafer, "Python Pandas Tutorial Part 8, Grouping and Aggregating":
  <https://www.youtube.com/watch?v=txMdrV1Ut64> (verified 13 Sep 2026)

The current pandas docs cover pandas 3.0, which is what the Codespace runs. Older tutorials show
idioms that have since been removed, so prefer the official guide when they disagree.

## One thing to bring

Tomorrow is the Excel day and it needs the customer table as a CSV. You will export it at the end
of tomorrow's session, so nothing to do tonight beyond knowing it is coming.

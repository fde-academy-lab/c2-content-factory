# Before Tuesday: three words, and one thing to look at

Ten minutes.

## Look at this, and only look

Open a terminal in the Codespace and run:

```sql
psql -c "SELECT * FROM payments ORDER BY order_id LIMIT 12;"
```

Do not analyse it. Read the twelve rows and answer one question for yourself: can the same
`order_id` appear more than once?

Write down what you think that would do to a total. You will find out tomorrow whether you were
right, and the guess is worth more than the answer.

## Three words

| Word | What it means here |
|---|---|
| Join | Attaching one table's rows to another's by matching a column |
| Key | The column the matching happens on, here `order_id` |
| Anti-join | Keeping only the rows that failed to match, which is how you find absence |

## One to read, one to watch

Both checked 13 September 2026.

- SQLBolt lessons 6 to 8, the join lessons: <https://sqlbolt.com/> (verified 13 Sep 2026)
- cudidotdev, "POSTGRESQL JOINS, complete guide in 12 mins":
  <https://www.youtube.com/watch?v=FprFu75BoE4> (verified 13 Sep 2026)

## One sentence to arrive with

Anand's reply to your Monday suite is this: booked revenue is not collected revenue.

Before tomorrow, write one sentence on what could make those two different for a business that
sells things. You will not need SQL for it, and having your own list first is what stops tomorrow
being a syntax lesson.

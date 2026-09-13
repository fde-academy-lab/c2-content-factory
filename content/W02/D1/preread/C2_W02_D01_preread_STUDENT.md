# Before Monday: the vocabulary, and one setup check

Fifteen minutes tonight. Nothing to install by hand.

## The setup check

Open the Codespace and run this in a terminal:

```bash
psql -c "SELECT count(*) FROM orders;"
```

One thousand comes back and you are ready. Anything else, run this and try again:

```bash
bash .devcontainer/load_warehouse.sh
```

If it still fails, post the last line of the output before the session rather than during it.

## Six words you will hear tomorrow

| Word | What it means here |
|---|---|
| Table | Rows of one kind of thing, with named columns. `orders` is one row per order. |
| Query | A description of the result you want. You do not say how to get it. |
| Clause | One named part of a query: `SELECT`, `FROM`, `WHERE` and four more. |
| Aggregate | A function that turns many rows into one value: `count`, `sum`, `avg`. |
| Group | The set of rows sharing a value, which an aggregate then collapses. |
| CTE | A named step inside a query, written `WITH name AS (...)`. |

## One thing to read, and one to watch

- SQLBolt, lessons 1 to 5, which run in the browser with nothing to install:
  <https://sqlbolt.com/> (verified 13 Sep 2026)
- freeCodeCamp.org, "Learn PostgreSQL Tutorial, Full Course for Beginners", the first forty
  minutes only: <https://www.youtube.com/watch?v=qw--VYLpxG4> (verified 13 Sep 2026)

## One question to arrive with

Last week you told Meera that Q1 was Rs 2.10 crore. Tomorrow the warehouse will say something
else, and neither number will be wrong.

Spend two minutes guessing why before you are told. Write your guess down; you will want to know
tomorrow whether you had it.

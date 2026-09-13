# Take-home: one join question of your own, and the check that proves it

## The situation

Anand has the booked-against-collected report. Tomorrow somebody else will ask you for a joined
number, and they will not warn you about their table the way the platform lead warned you about
the gateway.

Tonight you write one join question of your own and prove its answer before anybody asks.

## What to hand in

One `.sql` file containing a single joined query that answers a question nobody asked in class,
using at least two of `orders`, `customers`, `payments`, `refunds`.

Above it, the reconciliation block, filled in with real numbers:

```sql
-- Rows before: ____ , from ____
-- Rows after:  ____
-- Difference:  ____ , because ____
-- Therefore:   ____
```

Then a short note, four or five sentences: what you would say to the person who asked, including
the one sentence you would add before they use the number.

## The constraint that makes this hard

Your query must join at least one pair of tables where a fan-out is **possible**, and your
reconciliation must say whether it happened.

"Possible" means the right side can carry more than one row per key. `orders` to `customers` is
safe, so a query using only those two does not satisfy this. `orders` to `payments` and `orders`
to `refunds` are both unsafe, which is the point.

If your difference line reads zero, you still have to say why it is zero rather than leaving it
blank. A zero you can explain is a finding.

## The self-check

`C2_W02_D02_selfcheck_STUDENT.md` before you hand in. It does not check your SQL.

## Why the reconciliation rather than the query

Anybody can write a join that runs. Today's number came back at twice the truth with every
individual row correct, and the only thing standing between that and a report Finance acts on was
a count somebody bothered to take.

The reconciliation is the deliverable. The query is how you got there.

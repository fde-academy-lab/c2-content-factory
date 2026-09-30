# Pre-read for Tuesday: booked against collected

About twenty minutes tonight, after the take-home. Tuesday opens on this message.

> "Booked revenue is not collected revenue. Some orders are paid in two instalments, some are
> refunded, some were never paid at all. Show me, order by order, what we actually collected against
> what we booked in Q2. If there is a gap, I want to know which orders and which channel."
> Anand Iyer, finance controller, Kalpa Retail

Today every number came from one table, `orders`, plus one lookup to `customers` that could not
change the row count, because each order has exactly one customer. Tomorrow's number needs a second
table whose rows do not line up one to one with the orders, and that changes what a count and a sum
mean.

---

## The words you will meet, and the gap each one fills

| Word | What it means | The question it answers tomorrow |
|---|---|---|
| Join | Lining up rows of two tables on a shared key, such as order_id | Which payments belong to which order? |
| Key | The column two tables share, such as order_id in orders and in payments | What does the database match on? |
| One-to-many | One row on one side can match several rows on the other | Can one order carry more than one payment? |
| INNER JOIN | Keeps only the rows that found a match on both sides | What happens to an order nobody paid? |
| LEFT JOIN | Keeps every row of the left table, matched or not, with NULLs where nothing matched | When a report must show every order, which table goes on the left? |
| Anti-join | A LEFT JOIN kept only where the right side is NULL | Which orders have no payment at all? |
| Row-count check | Rows before the join, rows after, and the difference explained | How do we know the join added or lost nothing? |

---

## One thing to think about

Today's lookup to `customers` kept 1,000 rows as 1,000 rows. Write down, before class, what you
expect the row count to be when 1,000 orders are joined to a payments table, and what would have to
be true of the payments for the count to stay at exactly 1,000.

## The check for tonight

Run this in VS Code against the warehouse and write the number down without looking anything up:

```sql
SELECT count(*) FROM payments;
```

Tuesday's first question is what that number means next to 1,000 orders.

## The line worth carrying in

A join is done when its row count is explained, never when it runs.

## Reading, ten minutes

SQLBolt, Lesson 6, multi-table queries with joins, https://sqlbolt.com/lesson/select_queries_with_joins (verified 29 Sep 2026)

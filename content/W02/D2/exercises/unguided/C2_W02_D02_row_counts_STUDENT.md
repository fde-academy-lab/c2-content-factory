# Unguided: predict the row count

The warehouse holds 1,000 orders and 1,428 payment rows. Of the orders, 450 carry more than one
payment row and 30 carry none. Eight payment rows name an order that is not in the book.

Predict each answer before running anything.

## Q1.

```sql
SELECT count(*) FROM orders o LEFT JOIN payments p USING (order_id);
```

Which one appears?

a) 1,428
b) 1,450
c) 1,000
d) 1,420

## Q2.

```sql
SELECT count(*) FROM orders o INNER JOIN payments p USING (order_id);
```

Which one appears?

a) 1,450
b) 1,000
c) 1,420
d) 970

## Q3.

```sql
SELECT count(*) FROM payments p LEFT JOIN orders o USING (order_id);
```

Which one appears?

a) 1,420
b) 1,450
c) 1,428
d) 1,000

## Q4.

```sql
SELECT sum(o.amount) FROM orders o LEFT JOIN payments p USING (order_id);
```

Which one appears?

a) Roughly twice the true booked total
b) Exactly the true booked total
c) Slightly under the true booked total
d) An error, since amount is ambiguous

## Answering

Post one line: the four letters in order, then one sentence naming which of the four you could
have got wrong without noticing in a real report.

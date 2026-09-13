# Unguided: predict the row count

Four queries against the warehouse. For each one, say how many rows come back **before** you run
it. Then run it. A wrong prediction that you can explain afterwards is worth more than a right
one you guessed.

The warehouse holds 1,000 orders, 340 customers, 4 segments, 3 channels and 2 quarters.

## Q1.

```sql
SELECT quarter, count(*) FROM orders GROUP BY quarter;
```

Which one appears?

a) 1,000
b) 2
c) 4
d) 6

## Q2.

```sql
SELECT c.segment, o.channel, count(*)
FROM orders o JOIN customers c USING (customer_id)
GROUP BY c.segment, o.channel;
```

Which one appears?

a) 07
b) 04
c) 12
d) 03

## Q3.

```sql
SELECT customer_id FROM orders GROUP BY customer_id HAVING count(*) = 1;
```

Which one appears?

a) Every customer who ordered exactly once
b) Every customer who ordered at least once
c) 340, one per customer on the books
d) 1,000, one per order

## Q4.

```sql
SELECT order_id, amount FROM orders LIMIT 5;
```

Which one appears?

a) The five largest orders in the whole book
b) The five oldest orders by order date
c) Five rows, and which five is not promised
d) An error, since LIMIT requires an ORDER BY

## Answering

Post one line: the four letters in order, then one sentence on the prediction you got wrong and
what the picture on the board says about it.

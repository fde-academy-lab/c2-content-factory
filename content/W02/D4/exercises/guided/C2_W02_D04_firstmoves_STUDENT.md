# Guided: the first three moves, built with the trainer

Round 1 and the start of round 2, 15 minutes inside the demonstrations. The trainer types each
move on the warehouse; you answer the item before the cell runs, then check it against the
output. Every item is about the growth team's table: one row per customer, with recency,
frequency and spend.

Post one line, four letters in item order, no spaces:

```
Post exactly this shape: xxxx
```

---

### Q1

In Week 1 you built spend per customer with a loop:

```python
spend = {}
for row in orders.itertuples():
    spend[row.customer_id] = spend.get(row.customer_id, 0) + row.amount
```

The growth team needs the same numbers from the warehouse. Which pandas line gives exactly what
the loop gives?

a) `orders.groupby("customer_id")["amount"].sum()`
b) `orders.groupby("amount")["customer_id"].sum()`
c) `orders["amount"].sum()`, divided by the number of customers
d) `orders.groupby("customer_id")["amount"].mean()`

### Q2

The trainer runs one call for the three measures Marketing asked for:

```python
rfm = orders.groupby("customer_id").agg(last_order=("order_date", "max"),
                                        frequency=("order_id", "count"),
                                        monetary=("amount", "sum"))
```

Which columns does the growth team see in `rfm`, next to the customer id?

a) `order_date`, `order_id` and `amount`, the columns the measures came from
b) `max`, `count` and `sum`, the names of the three functions each tuple applies
c) `last_order`, `frequency` and `monetary`, the names on the left of each tuple
d) one column per customer, holding the three results together as a tuple

### Q3

The table must hold every customer on the list, so the trainer attaches `rfm` to `customers`.
Both hold one row per customer. Which `validate` value states that promise so the refresh stops
if either side breaks it?

a) `"many_to_one"`, since many orders map to one customer
b) `"one_to_one"`, since each side holds a customer once
c) `"one_to_many"`, since a customer has many orders
d) no validate, since the customer list is already clean

### Q4

After the left merge, `frequency` shows as `float64`, and 39 customers show `NaN`. What does the
growth team's table need, and why?

a) Drop the 39 rows, because a customer with no orders is not a customer
b) Leave the NaN, because 0 would be an invented number
c) Convert with `astype("int64")` straight away, since counts are whole numbers
d) Fill with 0 and then convert to `int64`, since no orders means frequency 0

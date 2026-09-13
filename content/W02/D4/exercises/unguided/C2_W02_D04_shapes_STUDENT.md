# Unguided: predict the shape

The warehouse holds 1,000 orders across 301 customers who ordered, 4 segments, 3 channels and 2
quarters. Q2 spans three months.

Say what each call returns before running it.

## Q1.

```python
orders.groupby("customer_id")["amount"].sum()
```

Which one appears?

a) A DataFrame of 301 rows and 2 columns
b) A Series of 301 values, indexed by customer
c) A Series of 1,000 values, one per order row
d) A DataFrame of 1,000 rows and 1 column

## Q2.

```python
orders.groupby(["segment", "quarter"]).agg(n=("order_id", "count"))
```

Which one appears?

a) 4 rows, one for each of the segments
b) 2 rows, one for each of the quarters
c) 6 rows, since two of the pairs are empty
d) 8 rows, one per segment and quarter pair

## Q3.

```python
monthly.pivot_table(index="customer_id", columns="month",
                    values="spend", aggfunc="sum")
```

`monthly` has one row per customer-month for Q2. Which one appears?

a) One row per customer, three columns, gaps as NaN
b) One row per customer-month, with three of the columns
c) Three rows, one per month, customers as columns
d) One row per customer and one column, summed

## Q4.

```python
wide.reset_index().melt(id_vars="customer_id")
```

Which one appears?

a) The original long frame, gaps included as NaN rows
b) The wide frame unchanged, with the index as a column
c) One row per customer, with the months concatenated
d) An error, since melt needs value_vars to be named

## Answering

Post one line: the four letters in order. Then one sentence on which of the four you would check
by running it rather than trusting, and why that one.

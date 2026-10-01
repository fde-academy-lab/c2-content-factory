# Does one line of pandas give the growth team the numbers Week 1's loop gave, for every customer on the list?

> "One table, one row per customer, refreshed every Monday: how recently each customer bought, how
> often, how much. Marketing's analysts live in Python, so build it in pandas, from the warehouse."
>
> The growth team, with the data platform lead, Kalpa Retail

Kalpa Retail's warehouse, its Postgres database, holds 1,000 orders from April to September 2026,
worth Rs 19,84,00,000 at the prices charged, and a customer list of 340 customers. The growth team
wants three numbers per customer: recency, the date of the last order; frequency, the count of
orders; and spend, the value of the orders at the prices charged. In Week 1 you built spend per
customer with a loop and a dictionary. pandas reads the same orders into a DataFrame, a table held in
memory, and `groupby` builds the same totals in one line.

**Who needs the answer.** The growth team, which sends Monday's offers from this table. Each line you
type here is a line of the table they act on, and the row count you read aloud in step 3 decides
whether the customers who never ordered get their first-order nudge.

**The questions on the way.**

- Does one line of `groupby` give the totals Week 1's loop gave, customer by customer?
- Which columns does one `agg` call hand the growth team?
- How many rows does the table have once the customer list is its starting point?

This is built on the screen during chapter 1, and you mirror it line for line in your own notebook,
the one the trainer opens from `notebooks/C2_W02_D04_01_customer_table_STUDENT.ipynb`. Copying is
what this exercise asks of you, since every later chapter adds columns to the table you type here.

## Step 1. Does one line of `groupby` give the totals Week 1's loop gave, customer by customer?

Used at work every time a familiar calculation moves to a new tool and someone asks whether it still
gives the same numbers.

```python
spend_loop = {}                                   # Week 1's accumulator
for row in orders.itertuples():
    spend_loop[row.customer_id] = spend_loop.get(row.customer_id, 0) + row.amount

spend_grouped = orders.groupby("customer_id")["amount"].sum()   # the same, in one line
print(len(spend_loop), len(spend_grouped))
print(all(spend_loop[c] == v for c, v in spend_grouped.items()))
```

Say aloud the three moves `groupby` makes: it splits the orders into one group per customer, applies
a sum to each group, and combines the results into one row per customer. Then say how many customers
each version holds, and whether that is the 340 on the list.

## Step 2. Which columns does one `agg` call hand the growth team?

Used at work whenever several numbers per group are wanted at once, as every customer table does.

```python
rfm = (orders.groupby("customer_id")
             .agg(last_order=("order_date", "max"), frequency=("order_id", "count"),
                  spend=("amount", "sum"))
             .reset_index())
print(rfm.columns.tolist())
print(rfm.head(3))
```

Each name on the left of `agg` becomes a column, and each pair says which column to read and what to
do with it. Say aloud the SQL that asks the same thing: `max`, `count` and `sum` after
`GROUP BY customer_id`.

## Step 3. How many rows does the table have once the customer list is its starting point?

Used at work on every table that a team acts on person by person.

```python
table = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
table = table.assign(frequency=table["frequency"].fillna(0).astype("int64"),
                     spend=table["spend"].fillna(0))
print(len(rfm), len(table), int((table["frequency"] == 0).sum()))
print(table["spend"].sum())
```

`how="left"` keeps every row of the customer list, and `validate="one_to_one"` stops the merge if
either side ever holds a customer twice. Read the three numbers aloud: the rows built from the
orders, the rows in the table, and the customers with a frequency of 0. Then check that spend still
adds up to Rs 19,84,00,000, and say in one sentence to the growth team who the third number is.

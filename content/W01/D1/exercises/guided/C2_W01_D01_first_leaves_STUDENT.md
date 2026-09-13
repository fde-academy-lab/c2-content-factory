# Guided: the first four leaves

Built with the trainer, one line at a time, in your own Codespace. Nothing here is graded and
nothing here is difficult. The point is that every line appears on your screen because you typed
it, not because you copied it.

---

## Before any code: the tree on paper

Draw it before you open the notebook.

```
REVENUE = CUSTOMERS × ORDERS PER CUSTOMER × ITEMS PER ORDER × PRICE PER ITEM − DISCOUNTS
```

Write the five branches down the left of a page. Beside each, write the metric with its numerator
and its denominator. Leave the right-hand column blank; today's numbers go there.

---

## Step 1. Open the workbench

1. Open the Codespace from the repository. It builds itself once and is then yours.
2. Open `notebooks/C2_W01_D01_01_revenue_tree_STUDENT.ipynb`.
3. Run the first cell. It loads thirty Kalpa Retail orders and prints the first one.

**If nothing prints:** the kernel has not started. Wait for the kernel indicator, then run again.

---

## Step 2. Look at one record before you loop over thirty

```python
first = ORDERS[0]
for key, value in first.items():
    print(f"{key:14s} {value!r}")
```

Seven named boxes. `!r` shows you the value as Python holds it, which is how you find out that one
amount is text without anybody telling you.

---

## Step 3. Count, which is the shape of everything

```python
count = 0
for order in ORDERS:
    count = count + 1
print("orders:", count)
```

Three lines: start at zero, walk the list, add one. Say the three parts aloud as you type them.
Every leaf on the tree is a variation of this.

---

## Step 4. Sum, which is the same shape with one thing changed

```python
total = 0
for order in ORDERS:
    total = total + order["amount"]
print("revenue:", total)
```

Run it. It stops. Read the message out loud before you touch anything:

```
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

Four facts in one line. The kind of problem, the operation that failed, what sat on each side, and
where Python gave up. Find the row it means, then fix it with `int()`.

---

## Step 5. Customers, and the first real rate

```python
customers = set()
for order in ORDERS:
    customers.add(order["customer_id"])

orders_per_customer = len(ORDERS) / len(customers)
```

A `set` refuses duplicates, which is exactly what "distinct customers" means. Say the denominator
out loud when you print it: **orders divided by distinct customers, in this window**.

---

## Step 6. Write the four numbers on your paper tree

| Leaf | Yours should read |
|---|---|
| Orders | 30 |
| Revenue | Rs 5,44,810 |
| Customers | 23 |
| Orders per customer | 1.30 |

If any of those disagree, you and the room have different data or different code. Say so now
rather than at the end of the day.

---

## Step 7. The three you cannot compute

Write `unknown` beside items per order, price per item and discounts, and write beside them what
you would have to ask for. That column is the first thing you send back to the business.

# Guided: one accumulator per key

Built with the trainer, in your own Codespace. Yesterday you kept one running total. Today you keep
one per group, and that single change is what the rest of the week stands on.

---

## Before any code: put the ladder on your page

Write the five rungs down the left of a fresh page, with space beside each.

```
1. confirm the drop is real
2. compare like with like
3. decompose along the tree
4. isolate the branch and the segment
5. hypothesise, and say what settles it
```

You will write a number beside each rung as the session reaches it. If a rung has no number beside
it at the end of the day, you skipped it.

---

## Step 1. Rung one, in six lines

```python
revenue = {}
for order in ORDERS:
    q = order["quarter"]
    revenue[q] = revenue.get(q, 0) + order["amount"]
print(revenue)
```

Say the shape aloud as you type it: **look up what is there, or nothing, then add and put it back.**

Write the two revenue figures beside rung one.

---

## Step 2. Meet the `KeyError` on purpose

The tree has a discounts branch, so total the discounts.

```python
discounts = 0
for order in ORDERS:
    discounts = discounts + order["discount"]
```

It stops:

```
KeyError: 'discount'
```

Do not reach for `.get()` yet. First answer the question the error is actually asking:

```python
absent = [o for o in ORDERS if "discount" not in o]
print(len(absent), "of", len(ORDERS))
```

**Then** decide on a default, and write the reason in a comment above the line. The reason is the
deliverable; the default is just a number.

---

## Step 3. Distinct customers needs a set per key

```python
customers = {}
for order in ORDERS:
    q = order["quarter"]
    customers.setdefault(q, set()).add(order["customer_id"])
```

`setdefault` makes the empty set the first time a quarter appears and hands back the existing one
afterwards. Write the two customer counts beside rung two.

At this point one of marketing's claims is already settled. Say which, out loud, before moving on.

---

## Step 4. Write the four numbers once, as a function

```python
def describe(rows):
    people = {o["customer_id"] for o in rows}
    total = sum(int(o["amount"]) for o in rows)
    return {"orders": len(rows), "revenue": total, "customers": len(people),
            "per_customer": len(rows) / len(people),
            "per_order": total / len(rows)}
```

Then break it on purpose: change the last line to `print(...)` and run `describe(q1)["orders"]`.
Read the error, then change it back. You only need to see this once, and seeing it once is the
point.

---

## Step 5. The conversion that must not stop the loop

```python
def to_amount(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default
```

Yesterday one bad value stopped the whole total. Across two hundred rows, stopping on the first one
means you never learn how many there are. Counting them is a finding; crashing is not.

---

## Step 6. Rung three, and the arithmetic that has to close

```python
a, b = describe(q1), describe(q2)
product = (b["customers"] / a["customers"]) \
    * (b["per_customer"] / a["per_customer"]) \
    * (b["per_order"] / a["per_order"])
print(product, b["revenue"] / a["revenue"])
```

Those two numbers must match. If they do not, a factor is missing or counted twice, and nothing
built on the decomposition is safe.

Write all three factor changes beside rung three.

---

## Step 7. Rung four, one call per segment

Call `describe` once per segment per quarter and put the six rows in a table. Circle the segment
that carries the fall.

Write the segment and its number beside rung four. Rung five is the unguided exercise.

# Mid-session: predict before you run

Six cells. For each one, decide what appears **before** you run anything. Then run it and see.

Post one line with your six letters in item order.

```
Post exactly this shape: xxxxxx
```

---

## Q1. What appears?

```python
amount = "4500"
print(amount * 2)
```

Which one appears?

a) `9000`
b) `45004500`
c) `TypeError`, because text cannot be multiplied
d) `4500 4500` with a space between them

---

## Q2. What appears?

```python
prices = [1200, 800, 4500, 1990]
print(sum(prices) / len(prices))
```

Which one appears?

a) `2122.5`
b) `1595.0`, which is the middle of the sorted list
c) `8490`, which is the total of the four values
d) `TypeError`, because a list cannot be divided

---

## Q3. Cells were run in this order: cell 2, then cell 1. What appears?

```python
# cell 1
orders = [{"amount": 900}]

# cell 2
print(len(orders))
```

Which one appears?

a) `1`, because the notebook reads top to bottom whatever the run order
b) `0`, because the list had not been filled when cell 2 ran
c) `NameError`, because `orders` did not exist when cell 2 ran
d) `None`, because `print` returns nothing at all

---

## Q4. What appears?

```python
order = {"order_id": "KR-01001", "amount": 2300}
print(order["discount"])
```

Which one appears?

a) `0`, because a missing key defaults to zero
b) `None`, because the key has no value attached to it
c) `KeyError`, because the key is not in the dictionary
d) `""`, because Python returns an empty value for a missing key

---

## Q5. What appears?

```python
ids = set()
for i in ["C-1", "C-2", "C-1"]:
    ids.add(i)
print(len(ids))
```

Which one appears?

a) `2`
b) `3`, because three values were added to it in the loop
c) `1`, because a set keeps only the value added most recently
d) `TypeError`, because a set cannot hold text values

---

## Q6. What appears?

```python
total = 0
for n in [1000, 2000, 3000]:
    total = total + n
print(total)
```

Which one appears?

a) `3000`, because the loop overwrites the total on every pass
b) `6000`
c) `[1000, 2000, 3000]`, because the values are collected into a list
d) `0`, because the assignment inside a loop does not persist

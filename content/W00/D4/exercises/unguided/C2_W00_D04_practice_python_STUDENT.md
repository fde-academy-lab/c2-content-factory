# Practice set, part 1 of 4: Python

Week 0, for the long weekend. About 45 minutes, on paper first, with no assistant and no notes. The
set is ungraded and yours to keep: answer every item, then check yourself against the self-check key,
and only then run the code to see it for yourself.

Items 1 to 11. Write each answer in the space under its item.

---

## Predict the output

Write exactly what each program prints. When it prints more than one line, write every line in
order.

### 1

```python
a = "5"
b = 2
print(a * b)
```

Your answer: ______________________________

### 2

```python
print(7 // 2, 7 % 2, 7 / 2)
```

Your answer: ______________________________

### 3

```python
total = 0
for n in [4, 1, 3]:
    total = total + n
    print(total)
```

Your answer:

______________________________

______________________________

______________________________

### 4

```python
order = {"item": "samosa", "qty": 4, "price": 15}
print(order["qty"] * order["price"])
```

Your answer: ______________________________

### 5

```python
orders = [
    {"item": "tea", "qty": 2},
    {"item": "coffee", "qty": 1},
    {"item": "tea", "qty": 3},
]
tea = 0
for o in orders:
    if o["item"] == "tea":
        tea = tea + o["qty"]
print(tea)
```

Your answer: ______________________________

### 6

```python
def double(x):
    print(x * 2)

result = double(4)
print(result)
```

Your answer:

______________________________

______________________________

### 7

```python
line = "tea,2,10"
parts = line.split(",")
print(len(parts), parts[-1])
```

Your answer: ______________________________

### 8

```python
values = [30, 10, 1000, 20]
values.sort()
mean = sum(values) / len(values)
mid = len(values) // 2
median = (values[mid - 1] + values[mid]) / 2
print(mean, median)
```

Your answer: ______________________________

---

## Fix the broken line

### 9

This program should print `20`, the cost of two cups of tea at Rs 10 each. It stops on line 3
instead, and the last line of the error reads:

```
TypeError: can't multiply sequence by non-int of type 'str'
```

```python
line = "tea,2,10"
parts = line.split(",")
cost = parts[1] * parts[2]
print(cost)
```

Rewrite line 3 so the program prints `20` from the values in `parts`.

Your line 3: ______________________________________________

### 10

This program should add up the price of an order. Juice is not on the price list yet, so it should
count as nothing and the program should print `25`. It stops on line 5 instead, and the last line
of the error reads:

```
KeyError: 'juice'
```

```python
prices = {"tea": 10, "coffee": 15}
order = ["tea", "juice", "coffee"]
total = 0
for item in order:
    total = total + prices[item]
print(total)
```

Rewrite line 5 so the program prints `25` and still works for any order. Change nothing else.

Your line 5: ______________________________________________

---

## Write a function

### 11

Write a function `total_by_item(orders)`. It takes a list of orders shaped like the list in item 5
and returns a dictionary holding the total quantity of each item. Use a loop and a dictionary, and
import nothing.

For this list:

```python
orders = [
    {"item": "pen", "qty": 3},
    {"item": "notebook", "qty": 2},
    {"item": "pen", "qty": 1},
]
```

`total_by_item(orders)` returns `{"pen": 4, "notebook": 2}`.

```python
# Write your function here.














```

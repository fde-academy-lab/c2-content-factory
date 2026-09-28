# Self-check key: practice set, part 1, Python

Answer every item before reading this. Every output and every error line below was produced by
running the snippet in Python 3.11.

## The answers

| No. | Answer | Kind |
|---|---|---|
| 1 | `55` | Predict the output |
| 2 | `3 1 3.5` | Predict the output |
| 3 | `4`, `5` and `8`, on three lines | Predict the output |
| 4 | `60` | Predict the output |
| 5 | `5` | Predict the output |
| 6 | `8`, then `None`, on two lines | Predict the output |
| 7 | `3 10` | Predict the output |
| 8 | `265.0 25.0` | Predict the output |
| 9 | `cost = int(parts[1]) * int(parts[2])` | Fix the line |
| 10 | `total = total + prices.get(item, 0)` | Fix the line |
| 11 | The function below | Write a function |

## Predicting output, items 1 to 8

Your answer is right when it has the printed values in the printed order and on the printed lines.
Commas between values on one line do not matter, since the items test the values.

| No. | A common wrong answer | Why it is wrong |
|---|---|---|
| 1 | `10` | `*` on a string repeats it, so `"5" * 2` is `"55"` |
| 2 | `3 1 3` or `3.5 1 3.5` | `//` divides and drops the remainder, and `/` always gives a float |
| 3 | `8` alone, or the three values on one line | The `print` sits inside the loop, so it runs three times |
| 5 | `6` or `3` | Only the two tea orders are added, and both are |
| 6 | `8` alone, or `None` alone | A function with no `return` gives back `None`, and the second `print` shows it |
| 7 | `2 10` or `3 tea` | Splitting on two commas gives three parts, and `[-1]` is the last |
| 8 | `265 25`, or the two values swapped | `/` always gives a float, and `print` shows the mean first |

## Fixing a line, items 9 and 10

**Item 9.** Right: both values converted with `int()`. Not right: `float()` on both, which prints
`20.0` where the item asks for `20`; converting only one value, since `int(parts[1]) * parts[2]`
prints `1010`; and typing the numbers in, such as `cost = 2 * 10`, since the item asks for the values
in `parts`.

**Item 10.** Right: `total = total + prices.get(item, 0)`, `total += prices.get(item, 0)`, a guard
such as `if item in prices: total = total + prices[item]`, or a `try` with `except KeyError` that
leaves the total unchanged. Not right: `prices.get(item)` with no default, which stops on the same
line with `TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'`; adding juice to the
price list, which changes another line; and removing juice from the order.

## Writing a function, item 11

One right answer:

```python
def total_by_item(orders):
    totals = {}
    for o in orders:
        item = o["item"]
        totals[item] = totals.get(item, 0) + o["qty"]
    return totals
```

Check yours against three things.

| Check | Right when | What goes wrong otherwise |
|---|---|---|
| It hands the answer back | The function returns the dictionary | Printing it gives the caller `None` |
| It reads every order | A loop runs over the orders and reads each order's `item` and `qty` | Reading only the first order gives one item |
| It starts each item correctly | The example returns `{"pen": 4, "notebook": 2}` | Adding to a missing key stops with `KeyError: 'pen'`; counting orders gives `{"pen": 2, "notebook": 1}`; assigning instead of adding gives `{"pen": 1, "notebook": 2}`; building the dictionary inside the loop gives `{"pen": 1}` |

An `if` and `else` that starts a new item at its quantity and adds to one already seen is just as
right as `get`.

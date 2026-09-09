# Cheat sheet, gap variant: typical, spread and denominators

Week 1, Day 4. Same eight panels with about a quarter of the cells removed.

Fill it in from memory. Check against the full sheet only after you have written something in every blank, since an answer you look up is an answer you forget.

---

## Panel 1: the three "typical" numbers

| | Answers | Reach for it when |
|---|---|---|
| **Mean** | ________________________ | The shape is roughly even |
| **Median** | The record in the middle of the queue | ________________________ |
| **Mode** | The value that repeats most | ________________________ |

**Crux:** nobody is right, they answer ________________________, and the asker rarely says which one they meant.

---

## Panel 2: the one-line skew test

```python
________ / ________
```

| Ratio | Shape | Send |
|---|---|---|
| Close to 1 | ________________ | Either |
| Well above 1 | Right tail, something large | ________ |
| Well below 1 | ________________ | Median |

Run it first on any column you have never seen.

---

## Panel 3: what one record does

```
seven orders             mean Rs 1,676.43   median Rs 1,310
swap the top for 480000  mean Rs ________   median Rs ______
```

**Crux:** the mean ____________, the median moved by ________. Not "a little".

---

## Panel 4: the fence

```python
q1, _, q3 = statistics.quantiles(values, n=4)
iqr   = ________________
upper = ________________
lower = ________________
```

**Crux:** a fence is a ________, never a ____________. An outlier is a finding to investigate before it is a row to delete.

---

## Panel 5: grouping without knowing the categories

```python
buckets = {}
for r in orders:
    key = r[field]
    if ________________________:
        buckets[key] = {"count": 0, "amounts": [], "returned": 0}
    buckets[key]["count"] += 1
    buckets[key]["amounts"].________(r["amount"])
    if r["status"] == "________":
        buckets[key]["returned"] += 1
```

Short form of the same idea: `counts[key] = counts.________(key, ____) + 1`

**Crux:** every hard-coded list of categories is ____________________________________.
Hard-code three and Kalpa has four, and you get `________: '________'`.

---

## Panel 6: count first, then median

| Accumulate one record at a time | Needs the whole group first |
|---|---|
| count, sum, returned count, ________, ________ | ________, ________, the fence |

**Crux:** there is no ________________.

---

## Panel 7: the honest sentence

```
[________________]   [________________]   [________________]
```

Write the sentence for Business, which had 1 returned of 9 orders:

> ________________________________________________________________

**Crux:** the third part is the one that goes missing between your notebook and somebody else's slide.

---

## Panel 8: before you send a rate

| Check | If it fails |
|---|---|
| ________________________________ | It is not ready |
| Any group under your stated floor | ________________________________ |
| Ranked groups of very different sizes | Say what the ranking is partly measuring |
| A mean quoted on a money column | ________________________________ |
| A difference being called real | ________________________________ |

---

## The three lines worth memorising

1. The mean was ________ and the description was ________.
2. On a money column, send the ________, and say that is what you sent.
3. Every rate carries its ____________, or it lies for you while you are not in the room.

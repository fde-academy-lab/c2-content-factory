# Cheat sheet: typical, spread and denominators

Week 1, Day 4. Landscape, eight panels. Print it, keep it beside the keyboard.

---

## Panel 1: the three "typical" numbers

| | Answers | Reach for it when |
|---|---|---|
| **Mean** | Total shared out equally | The shape is roughly even |
| **Median** | The record in the middle of the queue | Money, durations, anything with a tail |
| **Mode** | The value that repeats most | The column is a category |

**Crux:** nobody is right, they answer different questions, and the asker rarely says which one they meant.

---

## Panel 2: the one-line skew test

```python
mean / median
```

| Ratio | Shape | Send |
|---|---|---|
| Close to 1 | Roughly even | Either |
| Well above 1 | Right tail, something large | Median |
| Well below 1 | Left tail, something small | Median |

Run it first on any column you have never seen. It costs one line and it tells you which statistic you are allowed to quote.

---

## Panel 3: what one record does

```
seven values          mean 5,000    median 4,500
last one x8           mean 15,000   median 4,500
```

**Crux:** the mean tripled, the median moved by zero. Not "a little". Zero.

---

## Panel 4: the fence

```python
q1, _, q3 = statistics.quantiles(values, n=4)
iqr = q3 - q1
upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr
```

**Crux:** a fence is a flag, never a delete key. It says look at this record. An outlier is a finding to investigate before it is a row to delete.

---

## Panel 5: grouping without knowing the categories

```python
buckets = {}
for r in records:
    key = r[field]
    if key not in buckets:
        buckets[key] = {"count": 0, "amounts": [], "accepted": 0}
    buckets[key]["count"] += 1
    buckets[key]["amounts"].append(r["amount"])
    if r["outcome"] == "accepted":
        buckets[key]["accepted"] += 1
```

Short form of the same idea: `counts[key] = counts.get(key, 0) + 1`

**Crux:** every hard-coded list of categories is a promise about data you have not read yet. Hard-code three and the file holds four, and you get `KeyError: 'segment_d'`.

---

## Panel 6: count first, then median

| Accumulate one record at a time | Needs the whole group first |
|---|---|
| count, sum, accepted count, min, max | median, quartiles, the fence |

**Crux:** collect the amounts into a list during the pass and take the median after the loop ends. There is no running median.

---

## Panel 7: the honest sentence

```
[the number]   [the denominator]   [what it does not yet support]
```

> `segment_d`: accepted on 7 of 12 records, 58.3 percent. Highest in the file, resting on twelve records; two different outcomes erase the lead.

**Crux:** the third part is the one that goes missing between your notebook and somebody else's slide, so it goes in the sentence rather than in a footnote.

---

## Panel 8: before you send a rate

| Check | If it fails |
|---|---|
| Denominator on the same line as the number | It is not ready |
| Any group under your stated floor | Say so in words, in that line |
| Ranked groups of very different sizes | Say what the ranking is partly measuring |
| A mean quoted on a money column | Replace it with the median |
| A difference being called real | Park it and name what would settle it |

**Crux:** every rate carries its denominator, or it lies for you while you are not in the room.

---

## The three lines worth memorising

1. The mean was right and the description was wrong.
2. On a money column, send the median, and say that is what you sent.
3. Every rate carries its denominator, or it lies for you while you are not in the room.

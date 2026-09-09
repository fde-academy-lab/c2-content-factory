# Day 3 solution, E1. The profiler

### The answer

```
def count_present(rows, field):
    return sum(1 for r in rows if r[field].strip() != "")


def count_converts(rows, field):
    n = 0
    for r in rows:
        try:
            normalise_amount(r[field])
        except ValueError:
            continue
        n += 1
    return n


def profile_field(rows, field):
    return {
        "present": count_present(rows, field),
        "converts": count_converts(rows, field),
        "distinct": len({r[field] for r in rows}),
    }
```

### Line by line

`count_present` tests `.strip() != ""` rather than truthiness, because a field holding a single space is present to a truthiness test and empty to a human.

`count_converts` reuses `normalise_amount` from yesterday rather than calling `int` directly. That is not tidiness. It means the profiler and the cleaner agree by construction about what convertible means, and when the rule changes it changes in one place.

`distinct` counts the raw strings. Counting converted values instead would hide the very thing this column is for, since every unconvertible value would vanish before it was counted.

### What you should have seen

```
  field          present  converts  distinct
  order_id            50         0        49
  customer_id         50         0        47
  segment             50         0         4
  amount              48        44        46
  status              50         0         3
  order_date          50         0        20
  discount            11        11         9
```

`converts` reads zero for every text field. That is correct and worth saying aloud, because a room will read a zero as a failure.

### The field with the unexplained count

`order_id`. Fifty rows, forty nine distinct values, and no other number on the printout accounts for the difference.

### The `discount` decision, written out

```
discount, 11 of 50 present -> keep absent as absent
because absence means no discount was applied, which is a fact rather than a gap
```

### Where this lives in production

Ingestion services profile on arrival and refuse a batch when a count moves outside its expected range. The three-in-the-morning alert is usually a `present` count that dropped, meaning an upstream system quietly stopped sending a field.

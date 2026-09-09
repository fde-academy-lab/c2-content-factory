# Day 3 solutions

Release rule: E1, E2 and E3 at the close of the session, E4 once everyone has stopped working. The take-home solution is released at the start of tomorrow's session.

Today's answers are judgements. Where two answers are defensible this file says so, and says what would settle it.

---

## E1. The profiler

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

---

## E2. Which dataset would you trust

### The answers

1. **A.** B is A after somebody replaced every failure with a stated default of zero.

2. What the colleague did to move each count:

| Count | How it moved |
|---|---|
| `amount` present, 48 to 50 | The two empty amounts were filled with a value |
| `amount` converts, 44 to 50 | The four unreadable amounts became a number |
| `discount` present, 11 to 50 | Thirty nine orders that had no discount were given one |

3. A cleaning step reduces `distinct` when it maps several different input values onto one output value. Five different broken amounts all became `0`, so five distinct values became one.

4. Something close to: "Nothing fails to convert because you replaced everything that failed, so the count you are quoting is a count of your own edits."

5. `distinct` on its own. It is the only one of the three counts that can fall, so it is the only one that can carry bad news. On B alone you would notice that `amount` holds fewer distinct values than a fifty row order book plausibly should, and that `discount` holds nine distinct values across fifty complete entries.

### The part worth arguing about

B is not the work of a careless person. Every move in B is one a reasonable engineer makes under time pressure, and each one individually is defensible if it is written down. What makes B indefensible is that none of it was.

### Where this lives in production

HGNC, 2020. About 27 human genes were formally renamed because spreadsheets silently coerced names like SEPT1 into dates, after a 2016 audit found gene-name errors in roughly a fifth of genetics papers with spreadsheet supplements. No individual coercion was malicious. The damage was that they were invisible.

---

## E3. Classifying four gaps

| # | Answer | Reason |
|---|---|---|
| 1 | Drop the record, into rejects | `amount` is required and the value exists nowhere else, so the order cannot be computed on. It goes to the rejects file with its reason, never to the bin |
| 2 | Keep absent as absent | Absence carries meaning here, so filling it destroys information and gains nothing |
| 3 | Escalate before deciding | A known failed job means the values are recoverable from the source. Defaulting or dropping throws away six orders that somebody can simply re-run |
| 4 | Escalate before deciding | The largest order in the file with no status is a question for the order book owner, and any default you pick moves the biggest number in the dataset |

### The two that could be argued the other way

**Number 2.** Filling `discount` with zero is defensible if every downstream consumer treats zero and absent identically. Settle it by asking one question: does anything downstream distinguish an order with no discount from an order with a zero discount? If nothing does, the default is harmless. If anything does, it is not.

**Number 3.** Keep and flag is defensible if the re-run will take weeks and the analysis cannot wait. Settle it by asking when the job can be re-run. Anything inside your own deadline makes escalate the better answer.

Numbers 1 and 4 are not really arguable. A required field with no recoverable value is a rejection, and the largest record in the file is never a place to apply a silent default.

---

## E4. The full pass

### What you should have seen

```
input 50, clean 44, rejected 6
50 in = 44 profiled + 6 rejected
```

The six rejections, each carrying the interpreter's own wording:

```
KR4210  'twelve'
KR4214  ''
KR4231  '12,400'
KR4235  '24 500'
KR4237  ''
KR4240  'Rs 8000'
```

Total across the 44 that convert: Rs 561,145.

### The two things that needed a decision rather than a cleaning step

**The row.** `order_id` `KR4201` appears twice, on rows that differ only in `order_date`, six weeks apart. No whole-record comparison finds it, because the rows are not identical. Your log should show both rows kept and the pair flagged, with an identity rule proposed and the order book owner named as the decider.

**The value.** One order is Rs 480,000, which is 86 percent of the total and over 160 times the next largest. It converts cleanly and is well formed in every field. Your log should show it kept, with the reason that it is real until somebody says otherwise, and raised.

If you deleted either one, the number you produced may well be more useful and it is no longer defensible, which is a worse trade than it sounds.

### A decisions log that would pass review

```
field           finding                                    choice                      reason
amount          48/50 present, 44/50 convertible           reject the 6 unusable       amount is required
discount        11/50 present                              keep absent as absent       absence means no discount
order_id        1 id on two rows (KR4201)                  keep both, flag the pair    owner decides the identity rule
amount          one order at Rs 480,000, 86% of total      keep, raise with owner      converts cleanly, well formed
```

Four lines. A reviewer who was not in the room can follow every one, which is the only test that matters.

### If your numbers did not reconcile

The usual causes, in the order they occur: an append sitting inside a branch that does not always run, a `continue` placed before the counter, or a filter applied to the clean list after the count was taken. Print the length of every list immediately after you build it and the gap appears in one run.

### Where this lives in production

The decisions log is the artifact that survives you. When somebody asks in six months why revenue for August looks low, the log is what answers it, and its absence is what turns a ten minute question into a week.

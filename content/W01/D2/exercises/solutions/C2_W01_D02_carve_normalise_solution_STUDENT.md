# Day 2 solution: carve out `normalise_amount`

Read the explanation before the answer. The answer alone is worth very little in an interview.

### The decision you were asked to make

Both candidates work. They put the cost in different places.

Returning `None` on failure means every caller has to remember to check, and the check is easy to forget because the code runs fine without it. The reason for the failure is also gone by the time the caller sees the `None`.

Raising means the caller cannot ignore it. The failure arrives with the interpreter's own wording attached, which is the thing you want in the rejects log.

For a cleaning function that feeds a log, raise.

You saw both kinds of raise in notebook 1. `int` raised for you when the text would not convert, and `normalise_amount_strict` raised one you wrote yourself:

```
if value < 0:
    raise ValueError(f"amount below zero: {value}")
```

Raising yourself is what you reach for when a value converts perfectly well and your rule still refuses it. Tonight's take-home has exactly one of those in it.

### The answer

```
def normalise_amount(raw):
    """Return the amount as an integer, or raise ValueError describing what arrived."""
    return int(raw)


def clean_record(record):
    """Return one record with its amount as a number, or raise ValueError saying what arrived."""
    keeper = dict(record)
    keeper["amount"] = normalise_amount(record["amount"])
    return keeper


def clean_records(rows):
    """Call clean_record on every row and keep the failures, each with its reason."""
    clean = []
    rejects = []
    for r in rows:
        try:
            clean.append(clean_record(r))
        except ValueError as e:
            rejects.append({"order_id": r["order_id"], "reason": str(e)})
    return clean, rejects
```

### Line by line

`normalise_amount` converts. `clean_record` builds the cleaned record. `clean_records` owns the decision about what a failure means. Each does one thing and says so in its name, because a function that both converts and decides what failure means is two functions wearing one name.

`except ValueError` names the only failure you predicted. A `KeyError` from a misspelled field still stops the program, which is what you want, because a misspelled field is your bug rather than the data's.

`str(e)` carries the interpreter's wording. Everyone's rejects log then reads the same, and nobody has to maintain a list of invented messages.

The append only happens when `clean_record` returned, so a failure adds to `rejects` and to nothing else. That is what keeps the reconciliation honest.

`dict(record)` copies the record before changing it. Yesterday's `b = a` trap is the reason: without the copy you would be editing the row that is still sitting in `rows`.

### What you should have seen

```
input 30, clean 28, rejected 2
{'order_id': 'KR4210', 'reason': "invalid literal for int() with base 10: 'twelve'"}
{'order_id': 'KR4214', 'reason': "invalid literal for int() with base 10: ''"}
```

### Where this pattern lives in production

Every ingestion service you will work on has a function shaped like `normalise_amount` per field, and a rejects table with an id column and a reason column. The reason column is what the data supplier is sent at the end of the week.
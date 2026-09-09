# Day 2 solutions

Release rule: E1, E2 and E3 at the close of the session. E4 at the close as well, once everyone has stopped working. The take-home solution opens tomorrow's session.

Read the explanation before the answer. The answer alone is worth very little in an interview.

---

## E1. `normalise_amount`

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

---

## E2. Tracing three calls

### The idea being tested

A function hands back exactly one thing: whatever follows `return`. When there is no `return`, it hands back `None`, and `None` is a real value that travels quietly until something tries to use it.

### The answers

| Question | Answer |
|---|---|
| 1. What is in `x`? | `None`. `a` has no `return`. |
| 2. What is in `rec`? | `{'amount': 4500}`. The function changed the dictionary you passed in. |
| 3. What is in `y`? | `4500`, an `int`. |
| 4. `z`, and what appears? | `4500` appears on screen. `z` holds `None`. |
| 5. Which belongs in a pipeline? | `b`. It returns a value and changes nothing you did not ask it to change. |

`x["amount"]` raises:

```
TypeError: 'NoneType' object is not subscriptable
```

### The part worth arguing about

`a` is the dangerous one, and it is dangerous precisely because it appears to work. It changed `rec` in place, so the value really is converted, and a learner who checks `rec` afterwards concludes the function is fine. Then somebody writes `x = a(rec)` and the `None` travels three functions before it lands.

Changing something in place and returning nothing is a legitimate choice in some code. Doing it by accident is not.

### Where this pattern lives in production

Function returns `None` on a path nobody tested, the `None` is stored, and it surfaces hours later as a `NoneType` error in a component that did nothing wrong. Reading the traceback bottom-up gets you to the crash. Finding which function forgot to return is the actual work.

---

## E3. The truncated feed

### The answers

1. Line 48 does not exist. The file ends at line 47.
2. The file has 47 lines. `len(open(path).read().splitlines())` gives it in one line.
3. The transfer was cut off part way through a record. Line 47 is the last line in the file and reads `      "signup_date": "2026-08-10"`, sitting inside the nested customer block of an order whose braces were never closed, and the array itself was never closed either.
4. The parser stops where it runs out of input. That is line 48 column 1, one step past the last thing it could read, and line 48 does not exist. The file went wrong wherever the transfer was interrupted, which is the end of line 47. A parser reports where it gave up, never where the mistake was made. Those two positions are the same only in simple cases.
5. Something close to: "The feed we received is truncated at record 5 of what looks like a longer file, so we have 4 complete records out of the batch. Please resend." What you refuse to do is hand-edit the closing brackets to make it parse. That produces a file that loads and quietly holds a fraction of the data, which is the exact failure mode from this morning.

### Where this pattern lives in production

Truncated payloads are ordinary: a connection drops, a disk fills, a job is killed at a timeout. Pipelines that repair them automatically are how partial data reaches dashboards without anybody knowing. The correct behaviour is to fail, record the batch id, and ask again.

---

## E4. The AI-free lab

### What you should have seen

```
input 24, clean 21, rejected 3
{'order_id': 'KR5303', 'reason': "invalid literal for int() with base 10: 'nine hundred'"}
{'order_id': 'KR5307', 'reason': "invalid literal for int() with base 10: ''"}
{'order_id': 'KR5312', 'reason': "invalid literal for int() with base 10: '1,240'"}
```

Total of the 21 clean amounts: `34515`.

Reconciliation: 24 in, 21 plus 3 out. If your two output files hold fewer than 24 rows between them, records vanished inside your loop, and finding where is more valuable than the totals.

### The defect that behaves differently

`1,240` is the one. The other two are unusable: `nine hundred` is a word and the empty string holds nothing at all. `1,240` is a real number wearing a thousands separator, so it is recoverable, and that makes it a decision rather than a rejection.

You have three defensible answers and one indefensible one.

| Choice | Defence |
|---|---|
| Reject it, note the format in the reason | Safe. The supplier learns their export is wrong. You lose 1,240 from today's total. |
| Strip the comma and convert | Recovers the value. You have now decided that commas are decoration, which is wrong in locales where the comma is the decimal point. |
| Reject it today, ask the supplier, repair tomorrow with a written rule | The one a reviewer will not argue with. |
| Strip every non-digit character from every amount | The indefensible one. It converts `1,240` and also converts `4500 refund` into `4500`. |

If you stripped the comma, you were right that the value is recoverable and you skipped the step where you write down the rule. Write it down now.

### Why your first attempt may have missed it

If you tested only for an empty string, `1,240` sailed past the check and failed later at `int()`. That is the argument for attempting the conversion and catching the failure rather than trying to predict every wrong shape in advance. You cannot list all the ways a value can be wrong. You can catch the one thing that goes wrong when you use it.

### Where this pattern lives in production

Thousands separators, currency prefixes, trailing spaces and locale decimal points are the four most common reasons a numeric column arrives as text. Every mature ingestion codebase has a normaliser for each, and a comment explaining which locale it assumes.

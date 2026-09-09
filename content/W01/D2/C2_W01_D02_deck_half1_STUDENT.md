# Half one: package the logic, survive bad data

Week 1, Day 2. Slide source. One idea per slide.

Position bar, repeated at every section boundary:
`[inline cell] > [packaged decision] > [read the failure] > [log the rejection] > [cross the boundary]`

---

## S1. Package the logic, survive bad data


The three questions this half answers: what do I call again tomorrow, what do I do when a value is wrong, and who finds out.

---

## S2. Where we are

`[inline cell] > [packaged decision] > [read the failure] > [log the rejection] > [cross the boundary]`

Yesterday you answered a question about the records. Today that answer becomes something you can run again on records you have not seen.

---

## S2b. Where this is going

`clean_record`, on three records from today's file:

```
rejected 1011 because: invalid literal for int() with base 10: 'twelve'
rejected 1015 because: invalid literal for int() with base 10: ''
kept     {'id': '1001', 'amount': 4500, ...}
```

One function. Three records. Three outcomes, and the rejected ones say why.

You will have written this within the hour.

---

## S3. The anchor

You have written this cell three times already.

```
total = 0
for r in records:
    if r["outcome"] == "accepted":
        total = total + int(r["amount"])
```

Three copies. One of them has a typo. Which one?

---

## S4. The problem with three copies

A rule that lives in three cells is three rules.

When the rule changes, you have to remember where all three are. The one you forget is the one that ships.

---

## SECTION 1: THE PACKAGED DECISION

`[inline cell] > **[packaged decision]** > [read the failure] > [log the rejection] > [cross the boundary]`

---

## S5. Same rule, one place

```
def accepted_total(records):
    total = 0
    for r in records:
        if r["outcome"] == "accepted":
            total = total + int(r["amount"])
    return total
```

The rule now has a name and one home.

---

## S6. What the name buys you

You can say the name out loud to a colleague.

You can change the rule in one place.

You can run it on a file that arrives next week.

---

## S7. The parameter is the promise

`def accepted_total(records)` says: give me records, I give you a number.

The function cannot see anything you did not hand it. That is the whole of scope for today.

---

## S8. Live demo

Carve `accepted_total` out of the inline cell together.

Then break it: rename the variable outside the function and watch the function keep working.

---

## S9. return against print

```
def fix(record):
    print(record["id"])

result = fix(rec)
```

What is inside `result` now?

---

## S10. The break

```
TypeError: 'NoneType' object is not subscriptable
```

`print` shows a human. `return` hands a value back to the code. A function that only prints returns `None`, and `None` cannot be indexed.

---

## S11. The rule

Print is for you. Return is for the next line of code.

If the caller needs the answer, the function returns it.

---

## S12. Step card, section 1

1. Name the rule with `def`.
2. Take what you need as parameters.
3. Hand the answer back with `return`.
4. Use `print` only to show a human.

---

## SECTION 2: READ THE FAILURE

`[inline cell] > [packaged decision] > **[read the failure]** > [log the rejection] > [cross the boundary]`

---

## S13. Yesterday you saw three of these

A traceback is not the computer being angry. It is the computer telling you where it stopped and what it was holding.

---

## S14. Read it bottom-up

```
Traceback (most recent call last):
  File "clean.py", line 12, in <module>
    total = total + int(record["amount"])
                    ^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'twelve'
```

Last line: what went wrong. Line above it: where. Everything else: how you got there.

---

## S15. The three questions

1. What is the exception type?
2. Which line is mine?
3. What value was it holding?

The third question is the one people skip.

---

## S16. Catching it

```
try:
    value = int(record["amount"])
except ValueError:
    ...
```

You name the exception you expected. Anything else still stops the program, which is what you want.

---

## S17. The trap

```
try:
    value = int(record["amount"])
except:
    pass
```

This runs. It produces a number. The number is wrong and nothing on screen says so.

---

## S18. Watch it happen

Bare except, on today's 30 records:

```
Processed 30 records. Total: 230380
```

Narrow except, same 30 records:

```
Clean 28, rejected 2, total 230380
```

Same number. One of these two lines is a lie.

---

## S19. Which one lied

The first line claims 30 records went into that total. Two of them did not.

A crash costs you an hour. A plausible wrong number costs you the quarter, because nobody goes looking for it.

---

## S20. Step card, section 2

1. Read the traceback from the bottom.
2. Name the exception you expected.
3. Never catch everything.
4. If the count and the claim disagree, the claim is wrong.

---

## SECTION 3: LOG THE REJECTION

`[inline cell] > [packaged decision] > [read the failure] > **[log the rejection]** > [cross the boundary]`

---

## S21. Where does the bad record go

You have three choices when a record will not convert.

Fix it silently. Drop it silently. Set it aside with a reason.

Only the third one survives a question from your manager.

---

## S22. The rejects list

```
def clean_record(record):
    keeper = dict(record)
    keeper["amount"] = normalise_amount(record["amount"])
    return keeper
```

`clean_record` handles one record and decides nothing about failure. `clean_records` handles the list and owns that decision.

```
except ValueError as e:
    rejects.append({"id": record["id"], "reason": str(e)})
```

`str(e)` carries the exact reason the interpreter gave you. You do not have to invent wording.

---

## S23. What a good reason looks like

```
{"id": "1011", "reason": "invalid literal for int() with base 10: 'twelve'"}
{"id": "1015", "reason": "invalid literal for int() with base 10: ''"}
```

Someone who was not in the room can act on both of these.

---

## S24. The reconciliation

30 records in. 28 clean. 2 rejected.

Input equals clean plus rejected. When that sum does not hold, something disappeared and you do not yet know what.

---

## S25. From the field

Knight Capital, 1 August 2012. About USD 440 million lost in 45 minutes.

A deployment reused an old flag. The system did not fail loudly. It kept trading, at speed, on the wrong rule.

The argument for validating early and failing loudly is not a style preference. It is that number.

---

## S26. Interview question

"Why is a bare `except` worse than letting the code crash?"

You can answer this now, with today's two output lines as your evidence.

---

## S27. Step card, section 3

1. Set the bad record aside, never drop it.
2. Carry the interpreter's own reason.
3. Reconcile: input equals clean plus rejected.
4. Ship the rejects list as part of the job.

---

## S28. Crux, half one

You have `clean_record`. That was the promise on the third slide.

A function is a decision you can call again. A named exception is a failure you chose to survive. A rejects log is the difference between a number and a number you can defend.

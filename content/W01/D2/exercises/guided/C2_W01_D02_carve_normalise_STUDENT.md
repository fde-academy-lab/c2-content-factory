# Day 2, E1. Guided: carve out `normalise_amount`

Drop point: the guided build, after functions and error handling. About 40 minutes, trainer-led with the room mirroring.

You already have this inside a loop:

```
amount = int(r["amount"])
```

Working with the trainer, turn it into a named function and give it a rejection path.

Step 1. Write `normalise_amount(raw)` that takes the raw string from the file and returns an integer.

Step 2. Decide what it does when the value will not convert. Two candidates:

| Candidate | What the caller has to do |
|---|---|
| Return `None` on failure | Check the return value on every call and work out why it failed |
| Raise `ValueError` with the interpreter's own wording | Wrap the call once, catch it, and read the reason |

Pick one and say your reason out loud before you write it.

Step 3. Wrap the call in `try` and `except ValueError`, and append the failure to a `rejects` list with the record's id and `str(e)` as the reason.

Step 4. Run it on the 30 records. You are looking for exactly these three lines:

```
input 30, clean 28, rejected 2
{'order_id': 'KR4210', 'reason': "invalid literal for int() with base 10: 'twelve'"}
{'order_id': 'KR4214', 'reason': "invalid literal for int() with base 10: ''"}
```

If your numbers differ, the difference is the exercise.

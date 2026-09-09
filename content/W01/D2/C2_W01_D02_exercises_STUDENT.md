# Day 2 exercises

Four pieces of work. Two are short thinking exercises you do on paper, one is built with the trainer, and one you do alone with no assistance of any kind.

Nothing here rewards typing speed. Every answer is a prediction, a selection, a short repair or a defended choice.

---

## E1. Guided: carve out `normalise_amount`

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

---

## E2. Mid-session: trace three calls on paper

Drop point: the break in the first half. About 15 minutes. No computer. Write your answers down before anyone runs anything.

```
def a(record):
    record["amount"] = int(record["amount"])

def b(record):
    return int(record["amount"])

def c(record):
    amount = int(record["amount"])
    print(amount)
```

For each line below, write what the named variable holds afterwards.

1. `rec = {"amount": "4500"}` then `x = a(rec)`. What is in `x`?
2. What is in `rec` after that same call?
3. `y = b({"amount": "4500"})`. What is in `y`?
4. `z = c({"amount": "4500"})`. What appears on screen, and what is in `z`?
5. One of these three functions is the one you would put in a pipeline. Which, and why?

Then, without running it: `x["amount"]` on the result of question 1 raises something. Name the exception and the exact message.

---

## E3. Mid-session: find the defect the parser is pointing at

Drop point: the break in the second half. About 15 minutes. Open the file, do not repair it.

Run this and read what comes back:

```
import json
with open("C2_W01_D02_data_vendor_truncated_STUDENT.json") as f:
    records = json.load(f)
```

You get:

```
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 48 column 1 (char 1027)
```

1. Open the file and go to line 48. Write down what you find there.
2. How many lines does the file actually have? Use Python to check rather than scrolling.
3. Given your answer to 1 and 2, say in one sentence what happened to this file.
4. The parser named a position. Is the defect at that position? Explain the difference between where a parser stops and where a file went wrong.
5. You cannot reach the vendor until tomorrow and your manager wants the other records now. Write the one sentence you would send back, and say what you would refuse to do.

---

## E4. Unguided: the AI-free lab

Drop point: the second half, after files. About 40 minutes, working alone. Solution released at the close of the session.

This lab is AI-free. No assistant, no autocomplete suggestions accepted, no searching for a finished answer. You have your own notebook from today and the Python documentation. That is the whole toolkit, and the point is to find out what you can do without help.

The file `C2_W01_D02_data_lab_STUDENT.csv` is one you have not seen. It has the same five fields and defects you have not met.

Produce three things:

1. `output/clean.csv`, holding every record whose amount converted, with the amount stored as a number.
2. `output/rejects.csv`, holding every record that did not, with its id and the reason.
3. A reopened count: read both output files back and print one line reconciling them against the input.

Rules that make this the real job rather than an exercise:

- Use the functions you carved this morning. If you find yourself writing a fresh loop, stop and go back for the function.
- Every rejection carries the interpreter's own reason, never wording you invented.
- Reopen both files at the end. Writing a file is not finishing.

When you are done, write down two numbers before you look at anything: how many records went in, and how many are in the two output files together. If those do not match, you have found the most valuable thing in this lab.

One defect in this file behaves differently from the two you met this morning. When you find it, write one line about why it slipped past your first attempt.

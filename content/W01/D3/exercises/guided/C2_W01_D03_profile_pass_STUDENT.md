# How many records did the ERP send, and how many can you use?

> "How many records did you receive, and how many can you use?"
>
> Anand Iyer, finance controller, Kalpa Retail

The export is `data/C2_W01_D03_orders_STUDENT.csv`, Kalpa Retail's Q1 and Q2 orders from the ERP, the
enterprise resource planning system Finance books orders in. The dashboard reads the same export and
puts Q1 at Rs 2.1 crore, and the books, Finance's own record of Q1, say Rs 1,90,00,000.

**Who needs the answer.** Anand Iyer, the finance controller, will not weigh one figure against the
other until the team says what the export holds. Tonight his analyst ties out every figure, matching it
to the books line by line, and every later number in the day stands on these first counts.

**The questions on the way.**

- What type does every value arrive as when the CSV is read?
- How many amounts and statuses are present, convertible and distinct?
- What should the pass do when one of the two fields you counted is missing on some rows?

This is built on the screen during chapter 1, and you mirror it line for line in your own notebook.
Copying is what this exercise asks of you, since every later step reuses the shape you type here.

## Step 1. What type does every value arrive as when the CSV is read?

Used at work on every file you did not write yourself.

```python
import csv
with open(DATA / "C2_W01_D03_orders_STUDENT.csv", newline="", encoding="utf-8") as f:
    raw = [dict(row, line=n) for n, row in enumerate(csv.DictReader(f), start=2)]
print(len(raw), type(raw[0]["amount"]))
```

Say aloud what the second value printed means for every sum you will write today.

## Step 2. How many amounts and statuses are present, convertible and distinct?

Used at work before anyone trusts a total from data they have not counted.

A value is present when the field is not empty and convertible when it reads as the type the field
needs, and the distinct count is how many different values the field holds. Write the three counts
for `amount` and for `status`, one line each. The day's `convert()` turns an amount's text into rupees
and returns a reason in place of a value when it cannot:

```python
present = [r["amount"] for r in raw if r["amount"] != ""]
convertible = [v for v in present if convert(v)[0] is not None]
print("amount:", len(present), "present,", len(convertible), "convertible,", len(set(present)), "distinct")
```

Repeat it for `status`, where convertible means one of the three statuses the export uses:
delivered, returned or cancelled. Write
beside each count one sentence on what it lets you trust.

## Step 3. What should the pass do when one of the two fields you counted is missing on some rows?

Used at work wherever a value is missing and someone else will audit the choice made about it.

Of the two fields you counted, one is missing on some rows. Name it, then fill in the three-way
decision table in your notebook's markdown, one reason per line:

| Decision | What it does to revenue | What it does to the delivered count | Choose it when |
|---|---|---|---|
| Drop the row | | | |
| Fill a stated default | | | |
| Keep and flag | | | |

The row you choose goes into the decisions log, the record of each rule the pass applied with its
reason, and that log is the first thing Anand's analyst will read tonight.

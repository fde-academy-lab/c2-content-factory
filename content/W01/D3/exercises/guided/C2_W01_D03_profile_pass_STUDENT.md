# Guided: the first profile pass, built together

> "How many records did you receive, and how many can you use?"
>
> Anand Iyer, finance controller, Kalpa Retail

This is built on the screen during chapter 1, and you mirror it line for line in your own
notebook. It is the one exercise of the day where copying is the point: the shape you type here is
the shape every later step reuses.

## Step 1. Read the export, and see that everything is text

```python
import csv
with open(DATA / "C2_W01_D03_orders_STUDENT.csv", newline="", encoding="utf-8") as f:
    raw = [dict(row, line=n) for n, row in enumerate(csv.DictReader(f), start=2)]
print(len(raw), type(raw[0]["amount"]))
```

Say aloud what the second value printed means for every sum you will write today.

## Step 2. Profile two fields

Write the three counts for `amount` and for `status`, one line each:

```python
present = [r["amount"] for r in raw if r["amount"] != ""]
convertible = [v for v in present if convert(v)[0] is not None]
print("amount:", len(present), "present,", len(convertible), "convertible,", len(set(present)), "distinct")
```

Repeat it for `status`, where convertible means one of the four statuses the business uses. Write
beside each count one sentence on what it lets you trust.

## Step 3. Walk one missingness decision

One field is missing on some rows. Name it, then fill in the three-way decision table in your
notebook's markdown, one reason per line:

| Decision | What it does to revenue | What it does to the delivered count | Choose it when |
|---|---|---|---|
| Drop the row | | | |
| Fill a stated default | | | |
| Keep and flag | | | |

The row you choose goes into the decisions log with its reason, and the log is the first thing
Anand's analyst will read tonight.

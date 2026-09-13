# Guided: profile, decide, reconcile

Built with the trainer. The order matters more today than on any other day this week: **profile
before you decide, decide before you clean, and record while you do it.**

---

## Before any code: both numbers on your page

Write them at the top.

```
DASHBOARD  Rs 2.10 crore          FINANCE  Rs 1.90 crore          GAP  Rs 20 lakh
```

Underneath, leave four lines blank. Each one gets a cause and a row count as the session finds it.

---

## Step 1. Read the CSV and look at one value

```python
rows = kit.load_csv("C2_W01_D03_orders_STUDENT.csv")
print(repr(rows[0]["amount"]))
```

It prints `'2200'`, with quotes. Monday's `TypeError` was one row; from a file it is every row, and
it is silent until you do arithmetic.

---

## Step 2. Open the JSON, and let it fail

```python
data = kit.load_json("C2_W01_D03_orders_STUDENT.json")
```

```
json.decoder.JSONDecodeError: Unterminated string starting at: line 1397 column 15 (char 27679)
```

Before you theorise, **open the file at that point**. `kit.read_text(...)` and look at the last
sixty characters. The transfer was cut, so the file ends mid-record. A truncated file is not a
corrupt file, and you ask for it again rather than patching it.

---

## Step 3. Profile, and do not fix anything yet

```python
def profile(records, field):
    present = [r for r in records if r.get(field) not in (None, "")]
    convertible = 0
    for r in present:
        try:
            int(r[field]); convertible += 1
        except (TypeError, ValueError):
            pass
    return len(present), convertible, len({r[field] for r in present})
```

Run it on `order_id`, `amount`, `status` and `customer_id`. Write each result on your page.

**The one that matters:** `order_id` is present on 201 rows and has 186 distinct values.

---

## Step 4. Is fifteen repeated ids the whole gap?

Seven percent of rows against a gap of about nine percent of revenue. Close is not equal, and the
arithmetic is the check.

```python
seen, extra = set(), []
for r in rows:
    if r["order_id"] in seen:
        extra.append(r)
    seen.add(r["order_id"])
print(len(extra), sum(int(r["amount"]) for r in extra if r["amount"].isdigit()))
```

If that total is the Rs 20 lakh, you have the cause. If it is not, keep looking.

---

## Step 5. The identity rule, before you remove anything

Group the rows by id and ask two questions of every repeated id.

1. Is every field identical? Then it is a duplicate.
2. Do the dates differ? Then it is the same order twice, and somebody has to pick a date.

This file has exactly one of the second kind. Find it. That is a judgment, and it goes in the log
rather than in the code.

---

## Step 6. The pass, with a reason on every rejection

```python
clean, rejected, seen = [], [], set()
for r in rows:
    if r["order_id"] in seen:
        rejected.append((r, "duplicate order_id, the migration re-ran a batch"))
        continue
    seen.add(r["order_id"])
    ...
```

Every `rejected.append` carries a sentence. Write the sentence as you write the branch, because
writing it afterwards means writing it from memory.

---

## Step 7. The equation, and the bridge

```
INPUT = CLEAN + REJECTED
```

Print all three and check the arithmetic out loud. Then build the bridge from the exported Q1 total
to your reconciled one, one step per cause, and see whether it lands on Rs 1.90 crore.

If it does, **Anand was right**, and you can now prove it in four lines.

---

## Step 8. Recompute Tuesday, and write down what moved

Run yesterday's decomposition on `clean`. Two things happen, and both belong in your note.

1. The revenue drop shrinks a long way.
2. The Retail-Plus finding survives, and its number gets smaller.

Write both. The second one is the honest sentence, and it is what the unguided exercise asks you to
defend.

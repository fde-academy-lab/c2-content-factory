# Half two: cross the file boundary

Week 1, Day 2. Slide source. One idea per slide.

Position bar, repeated at every section boundary:
`[inline cell] > [packaged decision] > [read the failure] > [log the rejection] > [cross the boundary]`

---

## S1. Cross the file boundary


Everything so far lived inside the notebook. Close the notebook and it is gone.

---

## S2. Where we are

`[inline cell] > [packaged decision] > [read the failure] > [log the rejection] > **[cross the boundary]**`

Half one made your rule callable. This half makes your data outlive the kernel.

---

## S3. The anchor

Restart the kernel.

Your 30 records are gone. Yesterday you learned that. Today you do something about it.

---

## S4. Where the records actually come from

Nobody hands you a Python list. Someone sends you a file.

The file was written by a system you do not control, exported by a person you have not met, at a time you did not choose.

---

## SECTION 1: A FORMAT IS AN AGREEMENT

`[inline cell] > [packaged decision] > [read the failure] > [log the rejection] > **[cross the boundary]**`

---

## S5. What a file format is

A file format is an agreement about structure.

CSV agrees: one row per record, one comma between fields, the first row names the fields.

That is the entire agreement. Nothing in it mentions types.

---

## S6. The consequence

Everything you read from a CSV is a string.

```
4500      becomes   "4500"
twelve    becomes   "twelve"
(empty)   becomes   ""
```

The file cannot tell you which one is a number. It never could.

---

## S7. Yesterday's planted bug, revisited

Monday you had one amount stored as text and it broke a comparison.

Write those same records to CSV and that bug vanishes, because now every amount is text. The defect did not get fixed. It got hidden.

---

## S8. So conversion is a decision

You convert on purpose, at a place you chose, with a plan for what happens when it fails.

That plan is the `try` block you wrote in half one. It is already done.

---

## S9. Step card, section 1

1. A format is an agreement about structure.
2. CSV agrees about rows and commas, never about types.
3. Everything you read is a string.
4. Convert on purpose, in one place, with a rejection path.

---

## SECTION 2: OPENING A FILE

`[inline cell] > [packaged decision] > [read the failure] > [log the rejection] > **[cross the boundary]**`

---

## S10. The break, first

```
FileNotFoundError: [Errno 2] No such file or directory: 'data/orderz.csv'
```

Before we open a file correctly, watch what a wrong path says. It names the exact path it tried. Read it out loud and you find the typo.

---

## S11. The path is relative to where the kernel is running

Not to where you think you are. Not to where the file browser is pointing.

`FileNotFoundError` is the cheapest error in this course. It tells you exactly what it looked for.

---

## S12. with open

```
with open("records.csv") as f:
    ...
```

The `with` block guarantees the file closes when the block ends, including when your code raises inside it.

---

## S13. Why that guarantee matters

Without it, a crash mid-loop leaves the file open. On your laptop you get away with it. On a server that runs this a thousand times a day, you run out of file handles.

---

## S14. Step card, section 2

1. Read the path in the error before you edit anything.
2. Paths are relative to the running kernel.
3. Use `with open`.
4. The close is guaranteed even when the code fails.

---

## SECTION 3: CSV WITH NAMES

`[inline cell] > [packaged decision] > [read the failure] > [log the rejection] > **[cross the boundary]**`

---

## S15. Reading by position hurts

```
row[2]
```

What is field 2? You have to go and look. Then someone adds a column and every number shifts.

---

## S16. DictReader

```
import csv

with open("records.csv") as f:
    for record in csv.DictReader(f):
        print(record["amount"])
```

Each row arrives as a dictionary. You already know how to read those.

---

## S17. Where the keys come from

`DictReader` takes its keys from the first row of the file.

Change the header spelling in the file and every `record["amount"]` in your code raises `KeyError`. The header row is part of the contract.

---

## S18. Step card, section 3

1. `csv.DictReader` gives you one dictionary per row.
2. The keys come from the header row.
3. The header row is part of the agreement.
4. Read by name, never by position.

---

## SECTION 4: JSON AND NESTING

`[inline cell] > [packaged decision] > [read the failure] > [log the rejection] > **[cross the boundary]**`

---

## S19. The same agreement, a different shape

```
import json

with open("records.json") as f:
    records = json.load(f)
```

JSON agrees about types and about nesting. CSV agrees about neither.

---

## S20. What nesting looks like

```
{
  "id": "1015",
  "amount": null,
  "source": {"system": "feed_01", "amount_raw": "8400"}
}
```

Record 1015 had an empty amount in the CSV. The JSON still carries the original value, one level down.

---

## S21. The flattening cost

To put that record in a CSV you have to choose: drop `source`, or invent a column called `source_amount_raw`.

Either way the shape changes, and the person downstream has to be told.

---

## S22. When JSON goes wrong

A JSON file is either wholly valid or wholly unreadable. There is no half-parsed JSON.

`json.load` fails with a line and a column. Your exercise this half is one of these.

---

## S23. Step card, section 4

1. `json.load` reads types and nesting.
2. Nested values need a stated flattening rule.
3. JSON parses completely or not at all.
4. The error names a line and a column. Go there first.

---

## SECTION 5: TWO FILES OUT

`[inline cell] > [packaged decision] > [read the failure] > [log the rejection] > **[cross the boundary]**`

---

## S24. One pass, two deliverables

```
clean.csv     the records that converted
rejects.csv   the records that did not, and why
```

Shipping only the first one is shipping half the job.

---

## S25. Writing with names

```
writer = csv.DictWriter(f, fieldnames=["id","segment","amount","outcome","date"])
writer.writeheader()
writer.writerows(clean)
```

You state the field names on the way out. That is you writing the agreement for the next person.

---

## S26. Prove it parses

Writing a file is not finishing. Reopening it and counting the rows is finishing.

30 in. 28 in clean. 2 in rejects. Reopen both and check.

---

## S27. From the field

Public Health England, October 2020. 15,841 COVID cases were dropped from reporting.

A CSV was converted to an old Excel format that has a hard row limit. The rows past the limit were silently discarded. Contact tracing never saw them.

Nobody wrote bad code. Somebody did not know the format's contract.

---

## S28. Interview question

"CSV or JSON for nested records, and what does flattening cost?"

You have both files open in front of you. Answer from those.

---

## S29. Step card, section 5

1. One pass ships clean and rejects.
2. Name the fields on the way out.
3. Reopen both files and count.
4. Input equals clean plus rejected, or something vanished.

---

## S30. Crux, half two

A file format is an agreement about structure, and everything a CSV agrees to is text. Your job at the boundary is to convert on purpose, reject with a reason, and hand on two files instead of one.

---

## S31. Tomorrow

Today you cleaned one record at a time. Tomorrow you point these same functions at the whole dataset and find out how many usable records you actually have.

The functions you carved today get called tomorrow without one edit.

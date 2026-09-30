# Take-home: the fresh export

Due at the start of Monday's session. About ninety minutes.

> "The data team reran both exports overnight. Rebuild Monday's three things from the new files before
> I open the deck, and tell me which numbers moved and why. If you cannot tell me why, I cannot use it."
>
> Meera's chief of staff, Kalpa Retail

The fresh exports are in `data/`: `C2_W02_D05_takehome_customer_table_STUDENT.csv` and
`C2_W02_D05_takehome_raw_export_STUDENT.csv`. They have the same columns as Friday's files and a
different set of customers. The warehouse's totals are unchanged: Rs 10.00 crore for Q1 and Rs 9.84
crore for Q2.

---

## What you ship

1. **Your own workbook, rebuilt.** Start from the workbook you built in the escalated case, not the
   reference deck pack. Paste the fresh exports over the old ones as values and let every formula
   recalculate. Fix anything that breaks, and say in the log what broke.
2. **The change log.** A table with one row for every number on the three deliverables that moved:
   the tree's cells, the protect list's size, cut-off and total, the lookup test, the card sentence.
   Columns: the number, Friday's value from your own workbook, Monday's value, and one sentence on why
   it moved. "A different sample" is a reason only when you can say what in the sample changed.
3. **A screenshot of your Checks tab,** showing what it holds and why, and the note you would send
   the data platform lead if it holds anything.
4. **Three sentences to the chief of staff:** what ties to the warehouse, what moved that matters for
   the growth review, and what is held.
5. **The operating rule in three lines,** one per tool, in your own words.

## Two things to do on the way

- Test the lookup with an id you know is missing from the fresh customer table before you test it
  with one that is there. Find the missing id yourself, from the files; the log says how you found it.
- Read Microsoft's SUBTOTAL page,
  https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939 (verified 29 September 2026),
  and write, as the log's last line, the one situation in which `SUBTOTAL(9)` and `SUBTOTAL(109)`
  give different totals, and which one your foot uses.

## Why an assistant cannot do this for you

The change log needs Friday's values from the workbook you built, and Monday's from files nobody has
explained to you. The screenshot is of your own Checks tab. The missing id is found in the data, and
the log says how. Check yourself against `C2_W02_D05_selfcheck_STUDENT.md` before class.

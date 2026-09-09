# Profile before you touch: load, clean and defend a real dataset

Week 1, Day 3. Slide source. One idea per slide.

Position bar, repeated at every section boundary:
`[profile the columns] > [decide per field] > [find the hidden rows] > [investigate the extremes] > [ship with the log]`

---

## S1. Profile before you touch

Yesterday somebody told you which orders were dirty.

Today nobody tells you.

---

## S2. Two profiles, one question

Two printouts of the same Kalpa Retail order book. Which of these would you trust?

```
                 A                              B
amount    present 48/50  converts 44/50   present 50/50  converts 50/50
          distinct 46                     distinct 42
discount  present 11/50                   present 50/50
```

Take thirty seconds. Then say which, and why.

---

## S3. The answer

A.

B is A after somebody replaced every failure with a stated default of zero.

---

## S4. What B cost

Every count in B moved the way you want counts to move, and the dataset got worse.

Thirty nine orders in B carry a discount that nobody ever recorded.

Six amounts that could not be read are now the number zero, and nothing on the page says which six.

---

## S5. The number that tells you

`distinct` is the only count that fell, from 46 to 42.

Five different broken values collapsed into one. Counts that only ever rise are counts that cannot warn you.

---

## S6. Where we are

`**[profile the columns]** > [decide per field] > [find the hidden rows] > [investigate the extremes] > [ship with the log]`

Profiling is what you do before you have permission to change anything.

---

## SECTION 1: THE PROFILER

`**[profile the columns]** > [decide per field] > [find the hidden rows] > [investigate the extremes] > [ship with the log]`

---

## S7. Monday's counter, grown up

Monday you counted how many orders had a value. That counter is today's profiler with two more questions attached.

---

## S8. Three counts, per field

```
present     how many have anything at all
converts    how many become the type you need
distinct    how many different values there are
```

Three numbers per column. That is the whole tool.

---

## S9. What each one catches

| Count | The question it answers |
|---|---|
| present | Is this field being filled in? |
| converts | Is what is filled in usable? |
| distinct | Is this a category, a free text box, or an id? |

`present` minus `converts` is the number of values that look fine and are not.

---

## S10. Read a real column

```
amount    present 48/50   converts 44/50   distinct 46
```

Two orders have no amount. Four more have something that will not become a number. Forty six different values, so this is not a category.

You have not touched the data and you already know where the work is.

---

## S11. Step card, section 1

1. Profile every field before changing any of them.
2. Three counts: present, converts, distinct.
3. The gap between present and converts is your work list.
4. A count that only rises cannot warn you.

---

## SECTION 2: DECIDING PER FIELD

`[profile the columns] > **[decide per field]** > [find the hidden rows] > [investigate the extremes] > [ship with the log]`

---

## S12. A missing value is a decision

Not a defect to be removed. A decision, with three defensible answers and one written reason.

---

## S13. The three

| Choice | Use it when | It costs you |
|---|---|---|
| Drop the record | The field is required and the record is unusable without it | Every other field on that record |
| Use a stated default | Absence genuinely means something, and you can say what | The ability to tell absent from present-and-equal-to-the-default |
| Keep and flag | You need the record and the gap must travel with it | Every downstream reader has to handle the flag |

---

## S14. Applied to two real columns

`amount` is required. Two orders have none, so they are set aside with a reason.

`discount` is optional and absent on 39 of 50. Absence there means no discount was applied, which is a fact rather than a gap.

Same dataset, same day, opposite decisions, and both are written down.

---

## S15. The one that looks harmless

Filling `discount` with zero is defensible.

It also means you can never again tell an order that had no discount from an order whose discount was zero. That is a decision you are allowed to make once you have said it out loud.

---

## S16. Coercion at dataset scale

Yesterday's `clean_record` already handles one bad value correctly. Point it at fifty and it keeps working, because you wrote it to reject rather than to guess.

Nothing in it changes today. That was the promise.

---

## S17. From the field

HGNC, 2020. About 27 human genes were formally renamed because spreadsheets silently coerced names like SEPT1 into dates.

A 2016 audit had found gene-name errors in roughly a fifth of genetics papers with spreadsheet supplements.

Nobody chose to corrupt anything. A default was applied quietly, at scale, for years.

---

## S18. Step card, section 2

1. Missing is a decision, never a reflex.
2. Drop, default, or keep and flag, each with a written reason.
3. A default you did not state is data you invented.
4. Yesterday's function is today's tool, unchanged.

---

## SECTION 3: THE ROWS THAT HIDE

`[profile the columns] > [decide per field] > **[find the hidden rows]** > [investigate the extremes] > [ship with the log]`

Columns are done. Now the records themselves.

---

## S19. The check that finds nothing

```
duplicate rows by whole-record comparison: 0
```

Clean dataset. Move on.

---

## S20. Except

```
distinct order_ids: 49 across 50 rows
```

Nothing raised. Nothing was highlighted. Two numbers on two different lines disagree, and only you can notice.

---

## S21. The pair

```
KR4201  Retail-Core  1865  returned  2026-08-03
KR4201  Retail-Core  1865  returned  2026-09-14
```

Same order id. Same amount. Same status. Six weeks apart.

---

## S22. So what is it

The same order, exported twice, with the second export stamping the wrong date?

Or a real repeat order that reused an id it should not have?

The data cannot tell you. It never could.

---

## S23. An identity rule is something you state

"Two rows are the same order when they share an order_id and an order_date."

That is a rule. It can be applied by someone else, argued with, and written into a decisions log.

"They look like duplicates" is not a rule.

---

## S24. And who decides

Not you, on your own, on a Wednesday.

You take the pair to whoever owns the order book, with both rows on screen and your proposed rule underneath. That conversation is the job.

---

## S25. Step card, section 3

1. A whole-record check finds only exact copies.
2. Compare the id count against the row count, every time.
3. Write the identity rule down before you delete anything.
4. Who owns the record decides what counts as the same record.

---

## SECTION 4: THE EXTREMES

`[profile the columns] > [decide per field] > [find the hidden rows] > **[investigate the extremes]** > [ship with the log]`

---

## S26. Sort the column and look at the end

```
... 2895, 2930, 2990, 2995, 480000
```

Four ordinary orders and then one that is 160 times the one before it.

---

## S27. What it does to the total

The order book totals Rs 561,145 across 44 usable orders.

That one order is Rs 480,000 of it. Eighty six percent.

Remove it and the total is Rs 81,145.

---

## S28. The instinct, and why it is wrong

The instinct is to delete it. It is ruining every number.

An outlier is a finding before it is a row. Rs 480,000 in a business where a typical order is Rs 800 to Rs 3,000 is either the most interesting customer in the file or a data entry error, and those need opposite responses.

---

## S29. So you investigate

It converts cleanly. It has a customer, a date, a status and a segment like every other order.

Nothing about it is malformed. It is simply large, so it survives cleaning and goes to Thursday as a question rather than a deletion.

---

## S30. Step card, section 4

1. Sort the column and read the tail.
2. An outlier is a finding to investigate.
3. Convertible and extreme means real until someone says otherwise.
4. Record what you kept and why, alongside what you dropped.

---

## SECTION 5: WHAT SHIPS

`[profile the columns] > [decide per field] > [find the hidden rows] > [investigate the extremes] > **[ship with the log]**`

---

## S31. Two artifacts, not one

```
the profiled dataset     the orders you would compute on
the decisions log        every change, and why you made it
```

The first without the second is an opinion.

---

## S32. What a log line looks like

```
amount, 2 orders absent      -> rejected, amount is required, ids in rejects file
discount, 39 orders absent   -> kept absent, absence means no discount applied
KR4201, duplicate order_id   -> both kept and flagged, identity rule pending owner
480000, extreme amount       -> kept, converts cleanly, raised with the owner
```

Four lines. A reviewer who was not in the room can follow every one.

---

## S33. The reconciliation, one level up

Yesterday it was input equals clean plus rejected.

Today it also has to survive drops, defaults and any dedupe you applied. Same check, more ways to fail it.

```
50 in = clean + rejected + anything you removed on purpose
```

---

## S34. Crux

Profiling is what you do before you have permission to change anything.

Every cleaning act is a decision, and a decision nobody wrote down did not happen.

An outlier is a finding to investigate before it is a row to delete.

---

## S35. Tomorrow

You have a dataset you can defend and a whale you decided to keep.

Tomorrow you compute the average order value and find out what that whale does to it.

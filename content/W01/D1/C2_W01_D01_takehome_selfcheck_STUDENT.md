# Take-home self-check

Open this after your run, before tomorrow's session.

These are checkpoints, not answers. Each one is something you can confirm on your own screen in under a minute, and each one holds whichever boundary you chose. If a checkpoint fails, the repair is yours to find, and finding it is the evening's real work.

---

## Checkpoint 1: the stack you are standing on

Your setup cell should be holding **30 records**. Ask it directly with `len(records)` before you trust anything below.

If you see fewer, a cell above it was edited after it ran, and the bench is holding an older list than the one you are reading on screen. Restart the kernel and run every cell from the top.

## Checkpoint 2: the whole file

Every amount in the file, added together with each one converted at the point of use, comes to **Rs 58,210** across all thirty orders.

If the cell stops with a `TypeError` instead of printing, the conversion is missing somewhere. If it prints **Rs 53,710** across twenty-nine orders, the record with the text amount fell out of your loop rather than being converted inside it, and that record is KR4200, which happens to be the largest amount in the file.

## Checkpoint 3: the delivered orders

Today's opening question was answered by **13 delivered orders totalling Rs 25,720**. Your notebook should still be able to reproduce that number tonight, unchanged.

One warning, because this is the mistake that gets made in front of a stakeholder. If your boundary is Rs 2,000, your upper bucket also holds thirteen orders. Those two thirteens are different groups of orders that happen to have the same count, and their totals are different, so name the group every time you report either one.

## Checkpoint 4: your boundary

Find the row for the boundary you chose. Both sides of it should match what your cell printed.

| Your boundary | Above it | At or below it |
|---|---|---|
| Rs 1,000 | 28 orders totalling Rs 56,450 | 2 orders totalling Rs 1,760 |
| Rs 1,500 | 17 orders totalling Rs 42,070 | 13 orders totalling Rs 16,140 |
| Rs 2,000 | 13 orders totalling Rs 35,020 | 17 orders totalling Rs 23,190 |
| Rs 2,500 | 8 orders totalling Rs 23,865 | 22 orders totalling Rs 34,345 |

These figures assume the convention the take-home asked for, where an order sitting exactly on the boundary goes into the lower bucket.

If your counts are right and one of your totals is not, the condition is doing its job and the accumulator underneath it is adding the wrong thing, so read the two lines separately.

## Checkpoint 5: the buckets behave

This one holds for every boundary in the table, so it is the checkpoint to run first when something feels wrong.

Your two bucket counts add to **30**, and your two bucket totals add to **Rs 58,210**.

If either sum comes up short, a record is in neither bucket. The record that goes missing here is almost always KR4200, because its amount is text and an untouched comparison against text stops the loop rather than sorting the order into a bucket. Write that in your challenges log with the error text your kernel printed, and bring it tomorrow, rather than quietly dropping the record so the cell runs clean.

## Checkpoint 6: the default you chose

Totalling the discount field across all thirty records with a default of 0 gives **Rs 250**, which comes from the two records that carry the field at all.

Any other default gives you a number that is not a fact about this file. A default of 100 across the same thirty records gives Rs 3,050, and that number describes your default rather than Kalpa Retail's discounts. If your total reads anything other than Rs 250, read the default you typed before you read your loop.

---

## When a checkpoint fails

Write it in the challenges log, with the checkpoint number, what your screen showed instead, and the exact error text if there was one. Then bring it tomorrow and say it out loud.

A failed checkpoint that you found on your own, at night, with nobody watching, is worth more to you than a clean run, because tomorrow opens on the cell this day ended on and the room moves at the speed of what people are willing to name.

## What no checkpoint can tell you

Whether your two sentences of defence are any good. Every boundary in that table produces correct counts, and correct counts are the easy half.

Read your own two sentences back and ask whether the person who wants a different line would be answered by them, or only told what you chose. If they would only be told, the defence is not finished, and that is the part we discuss tomorrow.

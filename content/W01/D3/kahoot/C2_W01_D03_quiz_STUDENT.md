# Day 3 Kahoot pack

Ungraded. The score is read as a performance indicator for attention and retention, never as a marks component.

Seven items. Item 3 is the trap of the day and item 7 is Tuesday's return question one level up.

Run it at the close. Read the reason line after each item, because the reason is the teaching and the score is not.

Today has no error text to quote, so several items turn on a number that looks right. Slow down on those.

---

## Q1. Profiling

Your profiler reports three counts for every field. Which three?

1. Present, convertible, distinct  <- correct
2. Minimum, maximum and the average of the column
3. Rows read, rows written and rows rejected by the loop
4. Nulls, blanks and whitespace, counted separately per field

**Why:** Present says the box has something. Converts says it is usable. Distinct says what kind of field it is.

---

## Q2. Duplicates

Your dedupe reports 0 duplicates and the distinct order_id count says 49 of 50 rows. What happened?

1. The dedupe crashed silently and returned an empty result
2. Two rows share an id and differ somewhere  <- correct
3. One order_id is empty, so it did not count as distinct
4. The file has 50 rows but one of them is the header row again

**Why:** A whole-record check finds only exact copies. A near-duplicate differs in one field and passes straight through it.

---

## Q3. Coercion (trap)

You replace every failed conversion with a default of zero. The dataset now looks clean. What did you lose?

1. Nothing, since those values were unusable anyway
2. Only the rows that were going to be dropped later in the pass
3. The evidence of which values failed and which zeros are real  <- correct
4. Nothing you can name, because the profile now reports every count as complete

**Why:** This is the trap of the day. Present and converts both rise, distinct falls, and no column left on the page says which zeros you invented.

---

## Q4. Missingness

A field is absent on 39 of 50 orders and absence genuinely means the thing did not happen. What do you do?

1. Keep absent as absent, and write the reason down  <- correct
2. Drop all 39 orders, since the field is incomplete
3. Fill it with zero, because zero is the natural default for a number
4. Fill it with the average of the eleven values that are present

**Why:** Absence carries meaning here, so filling it destroys information and gains nothing. Drop, default and keep-and-flag each need their reason written.

---

## Q5. The decisions log

You dropped 40 records during a cleaning run. Where must that fact be written?

1. In a comment beside the line of code that dropped them
2. In the commit message for the cleaning script
3. Nowhere, as long as the rejects file holds the 40 rows
4. In the decisions log, with the count and the reason  <- correct

**Why:** The rejects file holds the rows. The log holds the decision, which is the part a reviewer six months later needs.

---

## Q6. Outliers

One order is Rs 480,000 in a book where a typical order is under Rs 3,000. It survives cleaning. Why?

1. Because the fence was set too high to catch it
2. Because outliers are always kept and never removed
3. Because it converts cleanly and every field is well formed  <- correct
4. Because removing it would change a total that has already been reported

**Why:** Cleaning removes what cannot be read. That order reads perfectly. Removing it would be an analysis decision wearing a cleaning decision's clothes.

---

## Q7. Return question, Tuesday one level up

Your cleaning loop finished with zero rejects on a file you know is dirty. Name your first two checks.

1. Re-download the file and run the whole thing again from the start
2. Whether the append runs, and whether the except is reachable  <- correct
3. Whether the file opened at all, and whether the path was correct
4. The row count against the header, and the encoding the file was saved in

**Why:** Tuesday you learned to catch narrowly and log every rejection. Zero rejects means either nothing reaches the append or nothing reaches the except.

---

## Distractor audit

Run before release. The correct answer is never the longest option, and correct positions are spread.

| Item | Key position | Key length | Longest option | Key is longest |
|---|---|---|---|---|
| Q1 | 1 | 30 | 58 | no |
| Q2 | 2 | 41 | 60 | no |
| Q3 | 3 | 60 | 77 | no |
| Q4 | 1 | 48 | 67 | no |
| Q5 | 4 | 51 | 54 | no |
| Q6 | 3 | 58 | 71 | no |
| Q7 | 2 | 60 | 72 | no |

Key positions used: slot 1 appears 2 times, slot 2 appears 2 times, slot 3 appears 2 times, slot 4 appears 1 times.

Longest question text: 107 characters. Longest answer text: 77 characters. Check both against the field limits in Kahoot before pasting.

# TA note: the practice lab, Week 1 Wednesday

**TRAINER ONLY.** For the TA running the lab after the second block. The learner file is
`exercises/practice/C2_W01_D03_lab_STUDENT.md`; the key is in
`exercises/solutions/C2_W01_D03_lab_solution_STUDENT.md` (1b 2c 3b 4c 5a 6a 7d 8b 9d 10a 11b).

The set runs about an hour. Release the solution only when a learner has posted all four groups.

| Problem | Minutes | Where learners stall | The one hint to give |
|---|---|---|---|
| 1. Two printouts | 10 | Choosing printout A because "every amount converts" | "Can a Kalpa order be worth Rs 0?" |
| 2. The vendor copy | 15 | Counting 39 rows because the file "should" hold 39 orders, or deleting the segment field | "Print every row whose amount does not convert, and read it." |
| 3. The app's feed | 15 | Re-running `json.load` and stopping at the error | "Chapter 1 recovered the complete records one at a time; reuse that cell." |
| 4. Reconcile the vendor copy | 20 | Reconciling rows and forgetting rupees, or comparing the vendor total with the whole of Q1 | "Sum your clean file over the same 39 order ids." |

## What is in the files, so you are never caught out

- The vendor copy is the export's header line, the same header line again, and the export's first 39
  data rows. `DictReader` reads the repeated header as a record, so the profile shows 40 rows, 39
  amounts that convert, and `segment` holding three values, one of them the word `segment`. The 39
  orders are all Q1, in Retail-Core and Retail-Plus, and total Rs 81,890, which equals the clean
  file over the same ids.
- The JSON feed is the export's first 120 records written as a JSON array and cut inside the 120th
  record's order id, so `json.load` raises `JSONDecodeError: Unterminated string starting at: line
  1397 column 15`. The 119 complete records all carry the same amount text as their CSV rows, the
  spelled-out amount included, which is why item 8's answer is that the feed witnesses what the
  extract held, never whether a value is right. One of the 119 has no `status` key.

## If the room finishes early

Point them at the stretch in `extras/C2_W01_D03_tiered_STUDENT.md`. If the room is behind, cut
problem 3 to its first item and keep problem 4 whole: the reconciliation is the day's habit.

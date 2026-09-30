# Where does the practice lab stall, and which one hint moves each learner on?

**TA note, Week 1 Wednesday. TRAINER ONLY.** For the TA running the lab after the second block. The
learner file is `exercises/practice/C2_W01_D03_lab_STUDENT.md`; the key is in
`exercises/solutions/C2_W01_D03_lab_solution_STUDENT.md` (1b 2c 3b 4c 5a 6a 7d 8b 9d 10a 11b).

The set runs about an hour: four problems that climb from judging two printouts to reconciling a
vendor copy against the learner's own clean file. The ERP is the enterprise resource planning system
Finance books orders in, and the vendor copy and the JSON feed are two more files its team sent.
Release the solution only when a learner has posted all four groups.

## Where do learners stall on each problem, and what is the one hint?

| Problem | Minutes | Where learners stall | The one hint to give |
|---|---|---|---|
| 1. Which of two printouts would you send? | 10 | Choosing printout A because "every amount converts" | "Can a Kalpa order be worth Rs 0?" |
| 2. What does the vendor copy hold? | 15 | Counting 39 rows because the file "should" hold 39 orders, or deleting the segment field | "Print every row whose amount does not convert, and read it." |
| 3. What can the app's feed witness? | 15 | Re-running `json.load` and stopping at the error | "Chapter 1 recovered the complete records one at a time; reuse that cell." |
| 4. Does the vendor copy reconcile with your clean file? | 20 | Reconciling rows and forgetting rupees, or comparing the vendor total with the whole of Q1 | "Sum your clean file over the same 39 order ids." |

## What do the lab's files hold, so that no question catches you out?

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

## What if the room finishes early, or falls behind?

Point a room that finishes early at the stretch in `extras/C2_W01_D03_tiered_STUDENT.md`. If the room
is behind, cut problem 3 to its first item and keep problem 4 whole, since the reconciliation is the
day's habit.

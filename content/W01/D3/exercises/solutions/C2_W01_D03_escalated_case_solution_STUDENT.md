# Solution: the escalated case, the reconciliation Anand can audit

Answers: 1b 2d 3a 4c 5b 6a 7d 8c 9a 10b

The notebook's own letters, in order, are in its solution twin,
`exercises/solutions/C2_W01_D03_ex1_escalated_case_solution_STUDENT.ipynb`: 1b 2c 3d 4b 5a 6c 7b 8d.

## The idea being tested

The whole pass, alone, in the order that makes each step safe: profile, convert with a log, the
identity rule preferring the copy that validates, keep and flag what is real, reconcile rows and
rupees to the books, recompute, and write it down in under 120 words.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | Rows against distinct ids is the cheapest lead on Anand's gap, and it comes before any total. | a: two totals with no explanation is not a reconciliation. c: dropping every repeated row throws away the originals too. d: the gap is information, not a transfer error to resend. |
| 2 | d | The complete records it holds can confirm the CSV field by field. | a: it covers only part of the export. b: merging two sources doubles the orders both hold. c: the records before the cut are still evidence. |
| 3 | a | A failure is counted and logged where anyone can read it. | b: a zero is a claim that the order was worth nothing. c: invents an amount. d: its twin may carry real rupees, as it did today. |
| 4 | c | Keeping the first copy keeps the one whose amount cannot be read and sets aside the twin that carries Rs 1,790; preferring the copy that converts keeps the value. | a: rounding hides the gap. b: an adjustment line closes the gap without a cause. d: a zero makes the unreadable copy look valid, and the first copy still wins. |
| 5 | b | The ERP's key, and the copy that carries a value. | a: keeps copies in revenue. c: finds only exact copies. d: merges real orders placed on one day. |
| 6 | a | The kept copy, the field and the question, so the doubt reaches the people who own the source. | b: leaves the auditor guessing. c: invents a value. d: removes a booked order. |
| 7 | d | Revenue stays whole and the delivered share stays at what was recorded, 57 of 86. | a: removes a booked order from revenue. b and c: each adds a delivery nobody recorded, 58 of 86. |
| 8 | c | Large is not wrong; the record decides. | a and b: fences on size remove real revenue. d: making quarters alike is the opposite of measuring them. |
| 9 | a | A bridge walks the dashboard's figure to the books, each move backed by logged rows, which answers both which and how. | b: an average is neither figure. c: the feed stops at record 120 and repeats the unreadable amount. d: a profile finds defects and proves no total. |
| 10 | b | Marketing is one of the note's readers, and a smaller finding reported first keeps trust. | a: buries it. c: Thursday tests whether it is real; today reports what changed. d: Anand asked which figure is right, so that leads. |

## The part worth arguing about

Item 3, option d. Most of the room will say one amount cannot move a crore, and on the rupees they
are nearly right. The point is the analyst who ties out to the rupee: one unexplained order is
enough to make every other line of the log suspect.

## Where the pattern lives in production

This pass, with its two logs and two reconciliations, is the month-end close between any sales
system and the ledger. The order of the steps is what makes it repeatable by somebody else.

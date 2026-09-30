# Solution: the second case, the auditor's question

Answers: 1b 2c 3a 4d 5c

The notebook's own letters, in order, are in its solution twin,
`exercises/solutions/C2_W01_D03_ex2_auditor_solution_STUDENT.ipynb`: 1c 2d 3b 4a 5c.

Three of the five items are design items: 2, 3 and 5.

## The idea being tested

A log is only as good as the questions it can answer for somebody who was not in the room. The
notebook walks the auditor's first question; these five are the ones she asks next, about the log's
shape, where the rule could have gone wrong, and what happens when the step moves to someone else.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | b | read | The rule set aside 15 rows, 14 in Q1 and 1 in Q2; the unreadable copy is one of the 14, and the largest order and the missing status were kept and flagged. | a: the unreadable amount is one of the 14 Q1 copies, set aside with its twin named, and the rejects log is empty. c: the largest Q2 order is kept and flagged, never removed. d: the order with no status is kept and flagged. |
| 2 | c | design | The rule made a choice only where copies differed, and the two Business rows carry about 98 percent of the rupees, so those four test the choice and the money; 13 of the 15 are identical copies, which test neither. | a: 13 of the 15 are identical copies, so four drawn at random test mostly the easy case. b: file order says nothing about risk. d: the largest rows test the money and never the rule's choice between copies that differ. |
| 3 | a | design | Rows would still tie, since the order would be logged as set aside; Finance booked it, so Q1 as exported less the rupees set aside would fall below the books by its amount, and the bridge would not close. | b: a row logged as set aside still counts in the rows equation. c: the rupee tie to the books would catch it. d: the repeated id is already one of the 15, so the count does not change. |
| 4 | d | read | "Set aside with a reason" is what happened, and each reason is in the log; an auditor reads "dropped" as lost. | a: to an auditor, dropped means gone without a trace. b: the log exists to show every row that left. c: a summary line hides the reasons she asked for. |
| 5 | c | design | Moving the step upstream moves the log with it: the question "why those rows" needs the ERP team's list of what they removed, and your rows and rupees still tie to the books. | a: "why those rows" still needs an answer. b: rows can tie while the rupees miss. d: a fuzzy match on customer and amount removed a real order today. |

## The hands-on picks

The notebook's five letters: 1c 2d 3b 4a 5c. The last check runs your evidence on chapter 6's
colleague's pass as well, and it has to fail there.

## The part worth arguing about

Item 3. The rows equation cannot see a real order set aside by mistake, because the row is still
accounted for. Only the rupee tie to an independent total, Finance's books, catches it, which is why
the reconciliation is done twice.

## Where the pattern lives in production

Internal audit, statutory audit and data governance reviews all ask this question of any pipeline
that removes rows. A log with a reason per row, the kept line named for every copy and two
reconciliations answers it in minutes, whoever runs the step.

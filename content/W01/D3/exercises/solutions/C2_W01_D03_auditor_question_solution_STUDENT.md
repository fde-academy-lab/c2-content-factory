# Solution: the second case, the auditor's question

Answers: 1c 2a 3d 4b 5c

The notebook's own letters, in order, are in its solution twin,
`exercises/solutions/C2_W01_D03_ex2_auditor_solution_STUDENT.ipynb`: 1b 2a 3b 4b 5c.

## The idea being tested

A decisions log is only as good as the questions it can answer from somebody who was not in the
room. Each item is a question an auditor asks, answered from the log and the file.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | The auditor asked about Q1, and 114 Q1 rows in less 100 orders kept is 14. | a: counts both quarters and gives 15. b: the rejects log holds the unreadable amount only. d: counts orders, not rows. |
| 2 | a | A copy is the same order_id, and every one of the 14 has its twin in the clean file. | b: two orders can share an amount. c: a line number says where a row sat, not what it is. d: a customer with two orders has two orders. |
| 3 | d | Rows and rupees by segment show two Business rows carrying about 98 percent of the Rs 19,98,210. | a: hides where the money sits. b: hides the other rows. c: the wrong quarter. |
| 4 | b | "Set aside with a reason" is what happened, and each reason is in the log. | a: "dropped" tells an auditor the rows are gone. c: the log exists to show them. d: deleting evidence is the one thing an auditor never forgives. |
| 5 | c | It states the rule, the evidence and both reconciliations. | a: they were not deleted and were not errors. b: reverses the finding. d: copies are not outliers, which were a separate decision. |

## The part worth arguing about

Item 4. It is one word, and it is the whole case: an auditor reads "dropped" as "lost", and the
rest of the conversation is spent recovering from it.

## Where the pattern lives in production

Internal audit, statutory audit and data governance reviews all ask this question of any pipeline
that removes rows. A log with a reason per row and two reconciliations answers it in ten minutes.

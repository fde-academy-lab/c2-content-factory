# Which answers hold in the second case on the auditor's 14 rows, and why?

Answers: 1b 2c 3a 4d 5c

The internal auditor on Kalpa Retail's finance team asks why 14 Q1 rows were set aside from the
export of orders out of the ERP, the enterprise resource planning system Finance books orders in, and
how she can know nothing else went, and the team answers from its log and from its reconciliation to
the books, Finance's own record of Q1 at Rs 1,90,00,000.

The notebook's own letters, in order, are in its solution notebook,
`exercises/solutions/C2_W01_D03_ex2_auditor_solution_STUDENT.ipynb`: 1c 2d 3b 4a 5c.

Three of the five items are design items: 2, 3 and 5.

## What does the second case test?

The auditor was not in the room, so the log has to answer her questions on its own. The notebook
walks her first question; these five are the ones she asks next, about the log's shape, where the rule
could have gone wrong, and what happens when the step moves to someone else.

## Which letter answers each of her next five questions, and why do the others fail?

### Q1. Why does the set-aside log hold 15 lines when the auditor asked about 14?

The auditor counts 15 lines in the set-aside log and asks why her question was about 14.

The key is b, "A Q2 copy, set aside by the same rule as the 14 copies in Q1". The identity rule, one
row kept per order_id, set aside 15 rows, 14 in Q1 and 1 in Q2, and named for each the twin that stayed,
the other row of the same order. The unreadable copy is one of the 14, and the largest order and the
missing status were kept and flagged.

- a, "The unreadable amount, which the log keeps apart from the copies": the unreadable amount is one of
  the 14 Q1 copies, set aside with its twin named, and the rejects log is empty.
- c, "The largest Q2 order, taken out of Q2 as an outlier": the largest Q2 order was kept and flagged,
  and it is still in Q2.
- d, "The order with no status, which the pass could not place": the order with no status was kept and
  flagged.

### Q2 (Design). Which four set-aside rows should the auditor re-perform?
The auditor will repeat the work herself on four of the 15 set-aside rows, with an hour to do it, and
wants the four that test the rule hardest.

The key is c, "One row from each pair that differed, and the two Business rows". The rule made a choice
only where copies differed, and the two Business rows, Kalpa's sales to companies, carry 98.5
percent of the rupees, so those four test the choice and the money. 13 of the 15 are identical copies,
which test neither.

- a, "Four drawn at random, so that no row is favoured over another": 13 of the 15 are identical copies,
  so four drawn at random test mostly the easy case.
- b, "The first four lines of the log, since the log runs in file order": file order says nothing about
  risk.
- d, "The four largest by rupees, since the money is what she signs for": the largest rows test the
  money and leave the rule's choice between differing copies untested.

### Q3 (Design). Would your evidence catch a real order set aside as a copy?
If one of the 14 had been a real second order that the ERP numbered with a repeated id, what in the
evidence would have shown it?

The key is a, "The rupees would miss the books by the real order's amount". Rows would still tie, since
the order would be logged as set aside. Finance booked it, so Q1 as exported less the rupees set aside
would fall below the books by its amount, and the bridge, the walk from the export's total to the books
one cause at a time, would not close.

- b, "The rows would not tie, since a real order would be gone": a row logged as set aside still counts
  in the rows equation.
- c, "Nothing, since the order would share an id with a kept row": the rupee tie to the books would
  catch it.
- d, "The profile would show a sixteenth id on more than one row": the profile, which counts each
  field's present, convertible and distinct values, already sees the repeated id as one of the 15, so
  its count does not change.

### Q4. What do you change when the auditor reads "dropped" in your log?

The auditor reads the word "dropped" in the log.

The key is d, "The word, to 'set aside', with each row's reason shown beside". "Set aside with a reason"
is what happened, and each reason is in the log, while an auditor reads "dropped" as lost.

- a, "Nothing, since dropped and set aside mean the same to Finance": to an auditor, dropped means gone
  without a trace.
- b, "The count, since a dropped row should not appear in the log": the log exists to show every row
  that left.
- c, "The format, into one summary line so that the log is shorter": a summary line hides the reasons
  she asked for.

### Q5 (Design). What must the reconciliation still carry if the ERP team removes copies at source?
The auditor suggests that next quarter the ERP team remove the copies before the export leaves the ERP.

The key is c, "The ERP team's own log of rows removed, and both totals tied". Moving the step upstream
moves the log with it: the question "why those rows" needs the ERP team's list of what they removed,
and the team's rows and rupees still tie to the books.

- a, "Nothing new, since a clean export needs no set-aside log": "why those rows" still needs an answer.
- b, "The row count the ERP team reports, since the rupees follow the rows": rows can tie while the
  rupees miss.
- d, "A fuzzy match on the export, to catch copies the ERP team missed": a fuzzy match on customer and
  amount removed a real order today.

## Which letters does the notebook take?

The notebook's five letters: 1c 2d 3b 4a 5c. The last check also runs your evidence on the pass
chapter 6's colleague ran, which kept the first copy of every pair and came out Rs 1,790 short of the
books, and the evidence has to fail there.

## Why is item 3 worth arguing about?

The rows equation cannot see a real order set aside by mistake, because the row is still accounted
for. Only the rupee tie to an independent total, Finance's books, catches it, which is why the
reconciliation is done twice.

## Where else is the auditor's question asked?

Internal audit, statutory audit and data governance reviews ask it of any pipeline that removes rows.
A log with a reason per row, the kept line named for every copy and two reconciliations answers it in
minutes, whoever runs the step.

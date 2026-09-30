# Solution: the escalated case, the reconciliation Anand can audit

Answers: 1d 2b 3c 4c 5a 6d 7a 8c 9b 10a

The notebook's own letters, in order, are in its solution twin,
`exercises/solutions/C2_W01_D03_ex1_escalated_case_solution_STUDENT.ipynb`: 1c 2a 3d 4c 5b 6d 7b 8a 9c.

Four of the ten items are design items: 3, 5, 6 and 8.

## The idea being tested

The whole pass, alone, in the order that makes each step safe: profile, the identity rule keeping the
copy whose amount converts, conversion with a rejects log that stays empty on this file, the two
flags, rows and rupees reconciled to the books, Monday's tree recomputed, and the note in under 120
words. The brief's items are the questions that arrive once the numbers land, so each asks for a
judgement the notebook's code does not make for you.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | d | read | 201 rows for 186 ids proves some orders sit on more than one row; how many rupees they carry, and which figure is right, waits for the identity rule and the bridge. | a: calls the books right before a single row has been tied out. b: ignores 15 rows beyond one per order. c: spreads the gap evenly over the extra rows, when two of them carry 98 percent of it. |
| 2 | b | read | The feed was cut from the same extract, so it witnesses what the extract held, never whether a value is right. | a: agreement with a copy of the same extract confirms nothing about the value. c: it stops at record 120 and holds only 19 of Q2's 86 orders. d: the two agree on that amount, which is unreadable in both. |
| 3 | c | design | Two systems issuing their own ids means an id no longer names one order; the source system plus the id does, and today's rule would set aside 312 real orders as copies of each other. | a: a log that records a wrong removal still removes it. b: finds only exact copies, and a real copy that differs in one field survives. d: merges two real orders a customer places for the same amount on one day. |
| 4 | c | predict | Thirteen pairs are identical and one pair's unreadable copy has a readable twin, so the rule settles all fourteen; the pair whose valid copies disagree on a field leaves a fact only the source can settle. | a: thirteen of those questions have nothing in them. b: the unreadable pair needs no question, since its twin carries the value. d: the rule keeps a copy of the disagreeing pair, and the field it keeps is still unconfirmed. |
| 5 | a | design | The order happened, so Q2 as booked keeps it; a plan for Q3 is a forecast, and an order the business says will not recur comes out of its base, labelled. One record, two uses, each stated. | b: removes booked revenue from the quarter Finance reconciles. c: plans on an order the business says will not come back. d: writes an amount nobody booked into both numbers. |
| 6 | d | design | Rejecting what int() refuses would leave about 40 percent of revenue in the log; a rule for a known format, stated and tested, reads both forms exactly and logs only what is still unreadable. | a: leaves about 40 percent of revenue out. b: turns about 40 percent of orders into Rs 0. c: drops the paise from 40 percent of orders and still rejects every amount with a comma. |
| 7 | a | read | The unreadable amount was one copy of a pair; the rule kept the readable twin and set the copy aside with its reason, so conversion afterwards had nothing to reject. | b: conversion runs on every kept row, and every kept amount converts. c: the rule tests whether an amount converts and changes none of them. d: profile() counts values and removes nothing. |
| 8 | c | design | A new export is a new file, and only the whole pass proves it: 100 Q1 orders on 100 rows, nothing set aside, and Q1 on the books. Anything else is a finding about the fix at source. | a: today's bridge proves today's file, and tomorrow's is another. b: rows can tie while the rupees miss, as the colleague's pass showed. d: a bridge on a file nobody profiled can close on the wrong rows. |
| 9 | b | predict | The copies were Q1 orders, so orders per customer carries the correction, 1.449 to 1.246 against Tuesday's 1.65 to 1.25; revenue per order moves from x1.180 to x1.144, a smaller shift, and customers stay at 69. | a: revenue per order moves, by less. c: the copies repeated orders of the same 69 customers, so the customer count never moved. d: x0.763 is the export as delivered today, before any cleaning. |
| 10 | a | read | Anand asked which figure is right, so that leads, then the proof, then the judgement calls, then what the change means for Tuesday's finding. | b: opens on Marketing's question before Anand's. c: makes Anand read the proof before the answer. d: leaves the answer to the last line. |

## The hands-on picks

The notebook's nine letters: 1c 2a 3d 4c 5b 6d 7b 8a 9c. Each check cell recomputes its step by a
second route, so a wrong letter shows as a FAIL on the step it belongs to.

## The part worth arguing about

Item 5. Most of the room will say "remove it" or "keep it", and both are half right. The same record
serves two readers: Finance reconciles what was booked, and a plan forecasts what will recur. Saying
which number serves which decision, and labelling both, is the analyst's job.

## Where the pattern lives in production

This pass, with its logs and two reconciliations, is the month-end close between any sales system
and the ledger. The order of the steps is what makes it repeatable by somebody else, and the recompute
is what makes it worth running: every number already reported from the raw file gets redone.

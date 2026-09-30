# Chapter 6 set: the log the analyst audits

5 items, about 15 minutes, after chapter 6. Every number here is invented unless it says it is from today's file; the reasoning is the one you ran on Kalpa's export. Items marked Design ask for the best-fit approach, a sizing or the fact that would change it.

Post one line, 5 letters in item order, no spaces:

```
Post exactly this shape: xxxxx
```

---

### Q1

A pass reports 500 rows in, 470 kept and 30 set aside, and Q1 comes out Rs 2,100 below the books' Rs 3,20,00,000. What do you do next?

a) Ship it, since the rows reconcile and the gap rounds away
b) Add Rs 2,100 as an adjustment line so the rupees tie
c) Find the set-aside row whose rupees a kept twin lacks
d) Ask Finance whether their books are Rs 2,100 too high

### Q2

Q1 as exported is Rs 50,00,000, the rows set aside carry Rs 4,20,000, and the books say Rs 45,80,000. Does the rupee reconciliation hold, and what does it prove?

a) No, since Rs 4,20,000 is more than 8 percent of Q1
b) Yes, and the clean total equals the books
c) Yes, and it proves no row vanished from the file
d) No, since the rows have not been counted yet

### Q3 (Design)

Put the pass in order for Anand's analyst: 1 apply the identity rule, 2 reconcile rupees to the books, 3 test which amounts convert and log the failures, 4 reconcile rows. Which order holds?

a) 1, 3, 4, 2
b) 3, 1, 4, 2
c) 1, 4, 3, 2
d) 3, 4, 1, 2

### Q4 (Design)

Anand's analyst has an evening to check the pass. Which hand-over is the best fit?

a) The clean file alone, 186 rows to compare by hand
b) A full diff of the raw and clean files, 201 lines
c) The clean file and a line saying 15 rows set aside
d) The logs, the decisions and both totals

### Q5 (Design)

How do you prove a log is complete without trusting the code that wrote it?

a) Count the log's lines and compare with the rows removed
b) Read every line of the log and check each reason
c) Rebuild the clean file from the raw export and the log
d) Rerun the pass and compare the two logs line by line

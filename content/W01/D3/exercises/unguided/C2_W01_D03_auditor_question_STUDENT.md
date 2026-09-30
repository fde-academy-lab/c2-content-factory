# Why were 14 Q1 rows set aside, and how does the auditor know nothing else went?

> "Your log says 14 Q1 rows were dropped. Why those 14, and how do I know nothing else went with
> them?"
>
> The internal auditor, Kalpa Retail finance

The export is Kalpa Retail's file of Q1 and Q2 orders from the ERP, the enterprise resource planning
system Finance books orders in, and it held 201 rows for 186 orders. A profile of it counted, for
every field, the values present, the values that convert and the distinct values. The team's pass then
applied the identity rule, one row kept for each order_id, the number the ERP issues once per order;
converted the amounts, sending any that failed to a rejects log; decided each missing value and the
largest Q2 order; and reconciled rows and rupees to the books, Finance's own record of Q1. Every row
it did not keep went to the set-aside log with its reason, and the decisions log holds each cleaning
rule once, with the rows and rupees it moved. In Q1, 114 rows came in and 100 orders were kept, and Q1
on the clean file equals the books at Rs 1,90,00,000.

A copy's twin is the other row of the same order. Chapter 3 found that two Business rows carry Rs
19,67,560 of the Rs 19,98,210 set aside in Q1; Kalpa's Business segment is its sales to companies,
every order in lakhs. Chapter 2 weighed a fuzzy match, which calls two rows one order when the
customer and the amount match within 60 days.

**Who needs the answer.** The internal auditor decides whether Finance can rely on the team's
reconciliation of Q1 and on the log behind it. A log she cannot follow costs a week of questions, and a
log that fails her tie-out, which matches every figure to the books line by line, costs the team her
trust in everything else it sends.

**The questions on the way.** The notebook walks her first question in five steps: which 14 rows,
whether each one is a copy, which rows carry the rupees, why one copy was chosen over its twin, and
what she signs. She then asks the five questions below:

- Why does the set-aside log hold 15 lines when the auditor asked about 14?
- Which four set-aside rows should the auditor re-perform?
- Would your evidence catch a real order set aside as a copy?
- What do you change in a log whose 14 lines say only "dropped"?
- What must the reconciliation still carry if the ERP team removes copies at source?

Forty minutes in pairs. One of you drives the notebook `notebooks/C2_W01_D03_ex2_auditor_STUDENT.ipynb`;
the other plays the auditor and asks the next question only when the check passes. Swap roles
halfway. When the notebook's walk is done, answer each item below aloud before either of you posts.

**What you post.** The notebook's five letters, then this brief's five, in this shape:

```
Post exactly this shape: notebook xxxxx · brief xxxxx
```

---

### Q1. Why does the set-aside log hold 15 lines when the auditor asked about 14?

The auditor counts 15 lines in your set-aside log and asks why her question was about 14. What is
the 15th line?

a) The unreadable amount, which the log keeps apart from the copies
b) A Q2 copy, set aside by the same rule as the 14 copies in Q1
c) The largest Q2 order, taken out of Q2 as an outlier
d) The order with no status, which the pass could not place

### Q2 (Design). Which four set-aside rows should the auditor re-perform?
The auditor will re-perform your work, repeating each step herself from the raw rows, on four of the
15 set-aside rows, and she has an hour to do it. Which four test your rule hardest?

a) Four drawn at random, so that no row is favoured over another
b) The first four lines of the log, since the log runs in file order
c) One row from each pair that differed, and the two Business rows
d) The four largest by rupees, since the money is what she signs for

### Q3 (Design). Would your evidence catch a real order set aside as a copy?
The auditor asks: if one of the 14 had been a real second order that the ERP numbered with a
repeated id, what in your evidence would have shown it?

a) The rupees would miss the books by the real order's amount
b) The rows would not tie, since a real order would be gone
c) Nothing, since the order would share an id with a kept row
d) The profile would show a sixteenth id on more than one row

### Q4. What do you change in a log whose 14 lines say only "dropped"?

A colleague's set-aside log for another export reads, on each of its 14 lines, only the order_id and
the word "dropped", and the auditor reads it tomorrow. What do you change?

a) Only the word, since the decisions log already holds each reason
b) Relabel all 14 lines 'removed as duplicates', one rule for all
c) Leave the word, and add a line saying the rupees tie to the books
d) Each line, to name the kept row it copies and why this one went

### Q5 (Design). What must the reconciliation still carry if the ERP team removes copies at source?
The auditor suggests that next quarter the ERP team remove the copies before the export leaves the
ERP. What must your reconciliation still carry?

a) Nothing new, since a clean export needs no set-aside log
b) The row count the ERP team reports, since the rupees follow the rows
c) The ERP team's own log of rows removed, and both totals tied
d) A fuzzy match on the export, to catch copies the ERP team missed

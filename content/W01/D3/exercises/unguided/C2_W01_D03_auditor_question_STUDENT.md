# The second case: the auditor's question

> "Your log says 14 Q1 rows were dropped. Why those 14, and how do I know nothing else went with
> them?"
>
> The internal auditor, Kalpa Retail finance

Forty minutes in pairs. One of you drives the notebook `notebooks/C2_W01_D03_ex2_auditor_STUDENT.ipynb`;
the other plays the auditor and asks the next question only when the check passes. Swap roles
halfway. When the notebook's walk is done, the auditor has five more questions, below: answer each
aloud before either of you posts.

```
Post exactly this shape: notebook xxxxx · brief xxxxx
```

---

### Q1

The auditor counts 15 lines in your set-aside log and asks why her question was about 14. What is
the 15th line?

a) The unreadable amount, which the log keeps apart from the copies
b) A Q2 copy, set aside by the same rule as the 14 copies in Q1
c) The largest Q2 order, taken out of Q2 as an outlier
d) The order with no status, which the pass could not place

### Q2 (Design)

The auditor will re-perform your work on four of the 15 set-aside rows and has an hour to do it.
Which four test your rule hardest?

a) Four drawn at random, so that no row is favoured over another
b) The first four lines of the log, since the log runs in file order
c) One row from each pair that differed, and the two Business rows
d) The four largest by rupees, since the money is what she signs for

### Q3 (Design)

The auditor asks: if one of the 14 had been a real second order that the ERP numbered with a
repeated id, what in your evidence would have shown it?

a) The rupees would miss the books by the real order's amount
b) The rows would not tie, since a real order would be gone
c) Nothing, since the order would share an id with a kept row
d) The profile would show a sixteenth id on more than one row

### Q4

The auditor reads the word "dropped" in your log. What do you change?

a) Nothing, since dropped and set aside mean the same to Finance
b) The count, since a dropped row should not appear in the log
c) The format, into one summary line so that the log is shorter
d) The word, to "set aside", with each row's reason shown beside

### Q5 (Design)

The auditor suggests that next quarter the ERP team remove the copies before the export leaves the
ERP. What must your reconciliation still carry?

a) Nothing new, since a clean export needs no set-aside log
b) The row count the ERP team reports, since the rupees follow the rows
c) The ERP team's own log of rows removed, and both totals tied
d) A fuzzy match on the export, to catch copies the ERP team missed

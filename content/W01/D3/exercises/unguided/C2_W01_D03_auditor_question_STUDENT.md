# The second case: the auditor's question

> "Your log says 14 Q1 rows were dropped. Why those 14, and how do I know nothing else went with
> them?"
>
> The internal auditor, Kalpa Retail finance

Forty minutes in pairs. One of you drives the notebook `notebooks/C2_W01_D03_ex2_auditor_STUDENT.ipynb`;
the other plays the auditor, asks the next question only when the check passes, and answers the five
items below aloud before either of you posts. Swap roles halfway.

```
Post exactly this shape: notebook xxxxx · brief xxxxx
```

---

### Q1

The auditor's first question is "which 14?". Which count answers it?

a) Every row in the file less every order kept
b) The rows in the rejects log, both quarters
c) Q1 rows in, less Q1 orders kept
d) The distinct order ids in Q1

### Q2

"How do I know each of the 14 was a copy?" What evidence answers it?

a) Each row set aside shares an order_id with a kept row
b) Each row set aside shares an amount with a kept row
c) Each row set aside sits below the file's line 186
d) Each row set aside belongs to a customer with another order

### Q3

"Two of the 14 carry almost all the rupees." How do you show that?

a) One total for all 14 rows, beside the books
b) The largest row alone, since it dominates the rest
c) The 14 rupee amounts as a share of Q2 revenue
d) Rows and rupees by segment, side by side

### Q4

The auditor reads the word "dropped" in your log. What do you change?

a) Nothing, since dropped and set aside mean the same
b) The word, to "set aside", and show each row's reason
c) The count, since a dropped row should not appear in the log
d) The file, by deleting the 14 rows so the log is shorter

### Q5

Which statement does the auditor sign?

a) Fourteen Q1 rows were errors, deleted to match the books
b) The dashboard was right, and the books are Rs 20 lakh short
c) Fourteen Q1 copies set aside by order_id; both reconcile
d) Fourteen Q1 rows were outliers, removed for the quarter's sake

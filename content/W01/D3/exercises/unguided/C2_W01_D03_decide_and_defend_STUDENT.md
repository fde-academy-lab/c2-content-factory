# Unguided: six calls, each one defended

Alone, no hints. Every item is a real row from today's export and a decision an auditor could ask
about.

Post one line with your six letters, then write the decisions log at the end.

```
Post exactly this shape: xxxxxx
```

---

## Q1. `KR-02063`, amount `twelve`, everything else present and sensible

Which one?

a) Default the amount to zero and keep the row, so the order count holds
b) Replace it with the median amount for that segment, which is the best estimate
c) Reject the row, and record the reason
d) Keep the row with the amount as text and exclude it from sums later on

---

## Q2. `KR-02119`, every field present except `status`, which is empty

Which one?

a) Default it to delivered, since most orders are delivered in this file
b) Reject it, because an order with no status cannot be counted
c) Keep it and exclude it only from the status split, since the amount is fine
d) Look up the customer's other orders and copy the status they usually have

---

## Q3. `KR-02151` appears twice, once dated 25 September and once 2 August

Which one?

a) Keep both, because the dates differ so they are two separate orders
b) Reject both, because you cannot tell which of the two records is right
c) Average the two dates, which puts the order in the middle of the range
d) Keep one, and record which date you took and why

---

## Q4. The vendor export's first two lines are identical header rows

Which one?

a) Reject the second one, because a header read as a record is not an order
b) Keep it, since it has the same shape as every other row in that file
c) Reject both header lines, because the file needs a header to be readable
d) Default its amount to zero, which makes it harmless in every calculation

---

## Q5. `KR-01031`, a corporate order of Rs 4,80,000, four times the next largest

Which one?

a) Reject it, because an outlier of that size distorts every average computed
b) Keep it, because it is a real order
c) Cap it at three times the next largest, which is standard outlier treatment
d) Move it to a separate file so the main analysis is not affected by its size

---

## Q6. Your bridge lands on Rs 1.92 crore and Finance says Rs 1.90 crore

Which one?

a) Report 1.92 and note the difference as within tolerance for an export
b) Adjust your figure to 1.90 so the two systems agree with one another
c) Find the remaining Rs 2 lakh, because a step is missing
d) Ask Finance to recheck their books, since your pass is fully documented

---

## Writing task: the decisions log

Write the log for today's pass. One row per decision, with these columns:

| Field | Issue | Rows | Decision | Reason |
|---|---|---|---|---|

Five rows at most. A reason of "it was wrong" is not a reason. An auditor reads this table and not
your code, so write it for them.

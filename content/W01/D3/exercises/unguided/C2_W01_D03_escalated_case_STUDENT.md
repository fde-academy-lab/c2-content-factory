# The escalated case: the reconciliation Anand can audit

> "Send the reconciliation and the log before the day closes. My analyst checks it tonight, and she ties out to
> the rupee."
>
> Anand Iyer, finance controller, Kalpa Retail

Fifty minutes, alone. Run the full pass on the ERP export, `data/C2_W01_D03_orders_STUDENT.csv`, in
the notebook `notebooks/C2_W01_D03_ex1_escalated_case_STUDENT.ipynb`, and answer the ten items below as you
reach each part. Then write the note to Finance.

**What you post.** Three things, in this order: the notebook's eight letters; this brief's ten
letters; the note to Finance in under 120 words, numbers first.

```
Post exactly this shape: notebook xxxxxxxx · brief xxxxxxxxxx · then the note
```

---

## Part 1. Read and profile

### Q1

Your profile shows `order_id` present on every row and distinct on fewer. Anand has asked which Q1
figure is right. What does that gap tell you to do before any total?

a) Report both totals and let Finance choose between them
b) Find out whether some orders sit on more than one row
c) Drop every row whose order_id appears more than once
d) Ask the ERP team to resend the file without the gap

### Q2

The app's JSON feed fails to parse part way through. How does it enter today's reconciliation?

a) In place of the CSV, since it is the app's own format
b) Merged into the CSV, so no order is lost between them
c) Not at all, since a file that fails once proves nothing
d) As a second witness for the orders it completely holds

## Part 2. Convert with a log

### Q3

One amount will not convert. Which record of it goes to Anand's analyst?

a) Its line, value and reason, in the log
b) A zero in its place, so the quarter's total can run
c) The segment median in its place, with a footnote
d) Nothing, since one amount cannot move a crore

### Q4 (Fix the logic)

A colleague's pass reads as below, and its Q1 lands Rs 1,790 short of the books. Which change fixes
the logic?

```python
rows = read_orders()
kept = keep_first_copy_per_order_id(rows)
clean = [r for r in kept if convert(r["amount"])[0] is not None]
```

a) Round Q1 to the crore before it goes in the note
b) Add a Rs 1,790 adjustment line so the rupees tie
c) Prefer the copy that converts, inside the dedupe
d) Turn every failed amount into zero before the dedupe

## Part 3. The identity rule

### Q5

Some rows share an order_id with another row. Which rule decides the clean file?

a) Keep every row, and flag the pairs for Finance
b) One row per order_id, the valid copy kept
c) One row per whole record, since that is the default
d) One row per customer per day, to be safe

### Q6

A pair of rows shares an id, both valid, and one field disagrees. What does the log say?

a) The kept copy, the field that differs, and a question
b) Nothing, since the pair shares an id and is one order
c) That the pair was averaged into one row
d) That both rows were set aside until the ERP team replies

## Part 4. Two decisions

### Q7 (Design)

One Q2 order has no status. Sized on the clean file, which option keeps Q2 revenue at
Rs 1,87,00,000 and the delivered share where the data supports it?

a) Drop it: Q2 falls by the order, 57 of 85 delivered
b) Default it to delivered: 58 of 86 delivered
c) Impute it from the customer's last order: 58 of 86
d) Keep and flag it: 57 of 86 delivered

### Q8

The largest Q2 order sits far above the next. Which check decides whether it stays?

a) Whether it is more than three times the median
b) Whether it lies above the 95th percentile of Q2
c) Whether the record and its buyer check out
d) Whether removing it makes the quarters look alike

## Part 5. Reconcile, bridge, recompute

### Q9 (Which method answers the question)

Anand asks, "Which Q1 figure is right, and how do you know?" Which method answers him?

a) A bridge to the books, one move per cause
b) The average of the two figures, both in the note
c) A rebuild of Q1 from the JSON feed alone
d) A fresh profile of the export, field by field

### Q10

On clean data, Tuesday's Retail-Plus fall is smaller than first reported. Where does that go in the note?

a) Last, since Anand asked about Q1 and not about Retail-Plus
b) After the reconciliation, smaller number first
c) Nowhere, since Marketing will read it in Thursday's page
d) First, since a changed finding matters more than a total

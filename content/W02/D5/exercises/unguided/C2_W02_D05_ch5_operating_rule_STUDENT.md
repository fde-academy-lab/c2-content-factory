# Which of the week's steps belong in the workbook, which must never be done there, and how do the two stay in step?

Chapter 5 set, six items, after chapter 5: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "Everything you built this week has to survive a room that only has Excel. Which parts belong in
> Excel, which parts must never be in Excel, and how do you keep the two from drifting apart?"
>
> Kavya Nair, senior analyst, Kalpa Retail data team

This week the team answered Kalpa Retail's questions in three tools. On Monday and Tuesday it queried
the warehouse, the Postgres database that holds one row per order and one row per payment and is the
source of truth; Tuesday's report set booked revenue, the value of the orders, against collected
revenue, the money received against them, which needs a join, a query that matches each order with
every payment made against it. On Thursday it built one row per customer in pandas, the Python
library for tables, and today it presents in an Excel workbook. A lookup returns the first row that
matches its key and stops; SUMIFS adds every row that matches. A drift check compares the workbook's
control totals, such as orders and booked revenue per quarter, with the warehouse's on every refresh,
and holds the deck when they differ. Anand Iyer is Kalpa Retail's finance controller.

**Who needs the answer.** Kavya signs the team's operating rule, Anand's analyst audits every number
Finance relies on, and the data platform lead owns the warehouse. A step done in the wrong tool ships
a number nobody can rerun, and a join done in a sheet can report money that customers have paid as
money they owe.

**The questions on the way.**

- What happened when a lookup put collected at Rs 11.84 crore against Rs 19.84 crore booked?
- What does a lookup say is outstanding on four invented orders, and what is?
- Which arrangement fits the booked-against-collected report Anand signs every month?
- Which question can live in a sheet alone, with no warehouse step behind it?
- What does the drift check do when the workbook's Q2 falls short of the warehouse's?
- Which check can disagree with the workbook's collected figure when the workbook is wrong?

Items 2 and 5 use invented figures; the other items use Kalpa's own week.

**What you post.** One line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

### Q1. What happened when a lookup put collected at Rs 11.84 crore against Rs 19.84 crore booked?

To show collected in the workbook without a login, a hurried analyst fills a lookup beside each of
Kalpa's 1,000 orders, `=VLOOKUP(A2, RawExport!A:H, 7, FALSE)`, an exact match on the order id that
fetches paid_amount from the raw export, which holds one row per payment. Added up, collected reads
Rs 11.84 crore against Rs 19.84 crore booked. What happened?

a) The unpaid orders have no payment row, so they pulled the total down
b) It took the first payment of each order and ignored any second one
c) The exact match failed on half the ids, which then returned zero
d) The refunds were netted off the payments before the export was sent

### Q2. What does a lookup say is outstanding on four invented orders, and what is?

Four invented orders: Rs 10,000, paid in two instalments of Rs 5,000; Rs 6,000, paid once; Rs 4,000,
paid in two instalments of Rs 2,000; and Rs 2,000, not yet paid. A lookup fetches the first payment
row of each order, and IFERROR turns the unpaid order's #N/A into zero. Outstanding is booked less
collected. What does the lookup say is outstanding, and what is?

a) Rs 9,000 by the lookup, and Rs 2,000 in truth
b) Rs 2,000 by the lookup, and Rs 2,000 in truth
c) Rs 13,000 by the lookup, and Rs 20,000 in truth
d) Rs 9,000 by the lookup, and Rs 9,000 in truth

### Q3. Which arrangement fits the booked-against-collected report Anand signs every month?

Anand signs the report every month, and his analyst reruns any number before relying on it. Which
arrangement fits?

a) A SUMIFS per order in the workbook over the payment export, refreshed by hand
b) An exact-match lookup per order in the workbook, so nobody needs a login
c) A notebook that computes collected and pastes the figures in as values
d) The join in the warehouse, with a SUMIFS in the workbook as a check on it

### Q4. Which question can live in a sheet alone, with no warehouse step behind it?

The team's rule says the warehouse owns every number Finance relies on. Which of these questions
could be answered in a sheet alone without breaking it?

a) Anand's monthly collected figure, since a SUMIFS adds every payment
b) A one-off look at which cities the protect list sits in, for a meeting
c) The weekly revenue by segment that every growth review reads first
d) Counting each order once in the payment export before Finance sees a total

### Q5. What does the drift check do when the workbook's Q2 falls short of the warehouse's?

On an invented Monday morning, the workbook's Q2 control total reads Rs 9.79 crore and the
warehouse's reads Rs 9.84 crore. Every row in the workbook's export is a real order. What does the
drift check do?

a) Holds the deck until someone knows why, and asks for a fresh export
b) Ships the deck with a footnote that the export may be incomplete
c) Types the warehouse's figure over the workbook's total so the two agree
d) Ships the deck, since every row in the export is a real order

### Q6. Which check can disagree with the workbook's collected figure when the workbook is wrong?

The workbook adds every payment per order with SUMIFS and reaches Rs 19,66,82,820 collected. A second
route shares none of its steps. Which of these is one?

a) The same SUMIFS copied onto a second tab and compared cell by cell
b) The lookup's figure, with the second payments added back by hand
c) The warehouse's payments table joined to its orders and summed
d) The share of orders with a payment row, set against the share collected

# Would you trust the other files the ERP team sent?

> "Before Thursday, run the same pass on everything else the ERP team sent, and tell me what you
> would trust."
>
> Kavya Nair, senior analyst, Kalpa Retail data team

The ERP is the enterprise resource planning system Finance books orders in, and its team sent more than
the orders CSV: a vendor copy of the export and the app's JSON feed, a second file cut from the same
extract, one pull of rows out of the ERP. Today's pass cleaned the orders CSV from 201 rows to 186
orders, one row per order, and landed Q1 on the books, Finance's own record of Q1, at Rs 1,90,00,000. A
profile counts, for every field, the values present, the values that convert and the distinct values.
Monday's revenue tree splits revenue into customers x orders per customer x revenue per order, with each
branch read as Q2's multiple of Q1.

**Who needs the answer.** Kavya Nair, the senior analyst on the team, who checks every number before it
leaves, decides which of these files the team may use beside the orders export. A file trusted on sight
can carry a defect into the next note to Anand Iyer, the finance controller, whose analyst ties out
every figure by matching it to the books line by line. A file thrown out unread loses a check the team
could have run.

**The questions on the way.**

- Which of two profile printouts of one export would you trust?
- What does the vendor copy hold once you profile it?
- Does the app's JSON feed agree with the CSV, and what would that prove?
- Does the vendor copy reconcile to your clean file in rows and in rupees?

About an hour, in the TA-led lab after the second block. The four problems climb from judging two
printouts to reconciling the vendor copy against your clean file. Work in a fresh notebook beside the
day's; the helper and the files are the same (`kit.data_dir()` finds `../data/`). Each problem ends in
lettered items.

**What you post.** One line per problem when it is done, in this shape:

```
Post exactly this shape: P1 xxx · P2 xxx · P3 xx · P4 xxx
```

---

## Problem 1. Which of two profile printouts of one export would you trust?

About ten minutes; used at work whenever a colleague's profile lands before its numbers go to Finance.

Two analysts profiled the same export of 320 rows and sent you their printouts.

| Printout | Rows | Distinct order ids | Amounts convertible | Amounts at Rs 0 | Failures logged |
|---|---|---|---|---|---|
| A | 320 | 305 | 320 | 4 | 0 |
| B | 320 | 305 | 316 | 0 | 4 |

### Q1. Which printout goes to Anand's analyst?

Which printout would you send Anand's analyst?

a) A, since every amount in it converts
b) B, since its four failures are counted and named
c) Either, since the rows and the ids agree across both
d) Neither, since both show copies in the export

### Q2. How many rows sit beyond one per order?

How many rows sit beyond one per order in this export?

a) 4
b) 11
c) 15
d) 19

### Q3. What does the same total on A and B tell you?

Printout A's total and printout B's total over the amounts that convert are the same number. What does
that tell you?

a) The totals agree, so the two printouts are equally sound
b) A's zeros add nothing, which is how its total hides them
c) The four failures carried no rupees, so neither total is short
d) The four failed amounts must all sit in one quarter

## Problem 2. What does the vendor copy hold once you profile it?

About fifteen minutes; used at work on any file a third party sends, before anyone relies on it.

Read `C2_W01_D03_vendor_STUDENT.csv` with the day's `read_orders()` and profile it with `profile()`.
The ERP team says a vendor sent it, copied from the start of the export.

### Q4. How many rows and convertible amounts does the profile show?

How many rows does the profile count, and how many amounts convert?

a) 39 rows, 39 convert
b) 40 rows, 40 convert
c) 40 rows, 39 convert
d) 39 rows, 38 convert

### Q5. What do you do first about a segment value the export never carries?

The segment field holds one more distinct value than the export's own rows carry. What do you do
first?

a) Print the rows whose amount fails, and read each one
b) Add the extra segment to the tree as a new branch
c) Drop the segment field, since one of its values cannot be trusted
d) Ask the vendor for a new file before reading any further

### Q6. What does the vendor copy total over the amounts that convert?

What does the vendor copy total over the rows whose amount converts?

a) Rs 81,890
b) Rs 18,890
c) Rs 8,18,900
d) Rs 81,980

## Problem 3. Does the app's JSON feed agree with the CSV, and what would that prove?

About fifteen minutes; used at work whenever two systems hold the same orders and someone asks
whether they agree.

Recover the complete records from `C2_W01_D03_orders_STUDENT.json` one at a time, as chapter 1 did, and
compare each with the CSV row on the same file line, the row it was cut from.

### Q7. How many feed records are complete, and how many match the CSV's amount text?

How many complete records does the feed yield, and how many carry the same amount text as the CSV
row on the same file line?

a) 120 and 119
b) 119 and 118
c) 120 and 120
d) 119 and 119

### Q8. What can the feed prove about the CSV's amounts?

What can a comparison of the feed with the CSV prove about the CSV's amounts?

a) That they are right wherever the two files agree
b) What the extract carried, with no proof any value is right
c) That the CSV holds no copies among the rows the feed covers
d) Nothing at all, since the feed is cut part way through

## Problem 4. Does the vendor copy reconcile to your clean file in rows and in rupees?

About twenty minutes; used at work whenever a second copy of a quarter's orders turns up and someone
wants to quote it.

Take your clean file from the escalated case, 186 orders, and reconcile the vendor copy against it in
rows and in rupees.

### Q9. What is the vendor copy's row reconciliation?

What is the row reconciliation?

a) 39 rows in equal 39 orders kept, nothing set aside
b) 40 rows in equal 38 orders kept plus 2 set aside
c) 40 rows in equal 40 orders kept, nothing set aside
d) 40 rows in equal 39 orders kept plus 1 set aside

### Q10. What must hold for the vendor copy's rupees to reconcile?

Every vendor order_id is in your clean file. What must hold for the rupees to reconcile?

a) The vendor total equals your clean total for the same ids
b) The vendor total equals Q1 in the books
c) The vendor total is within 1 percent of the clean total
d) The vendor total rounds to the same lakh as the clean total

### Q11. What do you tell Kavya about the vendor copy?

The rupees reconcile. What do you tell Kavya about the vendor copy?

a) It is a clean second source and can replace the export for Q1
b) It confirms the orders it holds to the rupee, and no more
c) It proves the export held no copies among its first rows
d) It is too small to matter, so it stays out of the note

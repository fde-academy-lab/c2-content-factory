# Practice lab: two more files and two printouts

> "Before Thursday, run the same pass on everything else the ERP team sent, and tell me what you
> would trust."
>
> Kavya Nair, senior analyst, Kalpa Retail data team

The ERP is the enterprise resource planning system Finance books orders in, and its team sent more
than the orders CSV. About an hour, in the TA-led lab after the second block. Four problems that
climb: judge two printouts, profile a vendor copy, compare the app's feed with the CSV, then reconcile
the vendor copy against your clean file. Work in a fresh notebook beside the day's; the helper and the
files are the same (`kit.data_dir()` finds `../data/`).

Each problem ends in lettered items. Post one line per problem when it is done:

```
Post exactly this shape: P1 xxx · P2 xxx · P3 xx · P4 xxx
```

---

## Problem 1. Two printouts, about ten minutes

Two analysts profiled the same export of 320 rows and sent you their printouts.

| Printout | Rows | Distinct order ids | Amounts convertible | Amounts at Rs 0 | Failures logged |
|---|---|---|---|---|---|
| A | 320 | 305 | 320 | 4 | 0 |
| B | 320 | 305 | 316 | 0 | 4 |

### Q1

Which printout would you send Anand's analyst?

a) A, since every amount in it converts
b) B, since its four failures are counted and named
c) Either, since the rows and the ids agree across both
d) Neither, since both show copies in the export

### Q2

How many rows sit beyond one per order in this export?

a) 4
b) 11
c) 15
d) 19

### Q3

Printout A's total and printout B's total over the amounts that convert are the same number. What does
that tell you?

a) The totals agree, so the two printouts are equally sound
b) A's zeros add nothing, which is how its total hides them
c) The four failures carried no rupees, so neither total is short
d) The four failed amounts must all sit in one quarter

## Problem 2. The vendor copy, about fifteen minutes

Read `C2_W01_D03_vendor_STUDENT.csv` with the day's `read_orders()` and profile it with `profile()`.
The ERP team says a vendor sent it, copied from the start of the export.

### Q4

How many rows does the profile count, and how many amounts convert?

a) 39 rows, 39 convert
b) 40 rows, 40 convert
c) 40 rows, 39 convert
d) 39 rows, 38 convert

### Q5

The segment field holds one more distinct value than the export's own rows carry. What do you do
first?

a) Print the rows whose amount fails, and read each one
b) Add the extra segment to the tree as a new branch
c) Drop the segment field, since one of its values cannot be trusted
d) Ask the vendor for a new file before reading any further

### Q6

What does the vendor copy total over the rows whose amount converts?

a) Rs 81,890
b) Rs 18,890
c) Rs 8,18,900
d) Rs 81,980

## Problem 3. The app's feed, and what it can witness, about fifteen minutes

Recover the complete records from `C2_W01_D03_orders_STUDENT.json` one at a time, as chapter 1 did, and
compare each with the CSV row on the same file line, the row it was cut from.

### Q7

How many complete records does the feed yield, and how many carry the same amount text as the CSV
row on the same file line?

a) 120 and 119
b) 119 and 118
c) 120 and 120
d) 119 and 119

### Q8

What can a comparison of the feed with the CSV prove about the CSV's amounts?

a) That they are right wherever the two files agree
b) What the extract held, and never whether a value is right
c) That the CSV holds no copies among the rows the feed covers
d) Nothing at all, since the feed is cut part way through

## Problem 4. Reconcile the vendor copy, about twenty minutes

Take your clean file from the escalated case, 186 orders, and reconcile the vendor copy against it in
rows and in rupees.

### Q9

What is the row reconciliation?

a) 39 rows in equal 39 orders kept, nothing set aside
b) 40 rows in equal 38 orders kept plus 2 set aside
c) 40 rows in equal 40 orders kept, nothing set aside
d) 40 rows in equal 39 orders kept plus 1 set aside

### Q10

Every vendor order_id is in your clean file. What must hold for the rupees to reconcile?

a) The vendor total equals your clean total for the same ids
b) The vendor total equals Q1 in the books
c) The vendor total is within 1 percent of the clean total
d) The vendor total rounds to the same lakh as the clean total

### Q11

The rupees reconcile. What do you tell Kavya about the vendor copy?

a) It is a clean second source and can replace the export for Q1
b) It confirms the orders it holds to the rupee, and no more
c) It proves the export held no copies among its first rows
d) It is too small to matter, so it stays out of the note

# Practice lab: two more files and two printouts

> "Before Thursday, run the same pass on everything else the ERP team sent, and tell me what you
> would trust."
>
> Kavya Nair, senior analyst, Kalpa Retail data team

About an hour, in the TA-led lab after the second block. Four problems that climb: judge two
printouts, profile a vendor copy, use the app's feed as a second witness, then reconcile the vendor
copy against your clean file. Work in a fresh notebook beside the day's; the helper and the files are
the same (`kit.data_dir()` finds `../data/`).

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
c) Either, since the rows and ids agree across both
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

a) The two totals agree, so both printouts are equally sound
b) A's zeros add nothing, which is why its total hides them
c) B double-counted four amounts that A correctly left at 0
d) The four failed amounts must all have been in Q2

## Problem 2. The vendor copy, about fifteen minutes

Read `C2_W01_D03_vendor_STUDENT.csv` with the day's `read_orders()` and profile it with `profile()`.
It should hold 39 orders from two segments.

### Q4

How many rows does the profile count, and how many amounts convert?

a) 39 rows, 39 convert
b) 40 rows, 40 convert
c) 40 rows, 39 convert
d) 39 rows, 38 convert

### Q5

The segment field shows one distinct value more than expected. What do you do first?

a) Print the rows whose amount fails and read them
b) Add the extra segment to the tree as a new branch
c) Drop the segment field, since it cannot be trusted
d) Ask the vendor for a new file before reading further

### Q6

Once the row that is not an order is set aside, what is the copy's total over its 39 orders?

a) Rs 81,890
b) Rs 18,890
c) Rs 8,18,900
d) Rs 81,980

## Problem 3. The app's feed as a second witness, about fifteen minutes

Recover the complete records from `C2_W01_D03_orders_STUDENT.json` one at a time, as chapter 1 did, and
compare each with the CSV row on the same file line, the row it was cut from.

### Q7

How many complete records does the feed yield, and how many carry the same amount text as the CSV
row on the same file line, the row each was cut from?

a) 120 and 119
b) 119 and 118
c) 120 and 120
d) 119 and 119

### Q8

The feed and the CSV agree, line for line, on every amount the feed holds. What does that prove about the CSV?

a) That the CSV is clean for every row the feed covers
b) A common source, and nothing about cleanliness
c) That the CSV holds no copies, since the feed holds none
d) Nothing, since a truncated file proves nothing at all

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

a) The vendor total equals your clean total for those 39 ids
b) The vendor total equals Q1 in the books
c) The vendor total is within 1 percent of the clean total
d) The vendor total rounds to the same lakh as the clean total

### Q11

The rupees reconcile. What do you tell Kavya about the vendor copy?

a) It is a clean second source and can replace the ERP export
b) It confirms 39 orders to the rupee, one line aside
c) It proves the ERP export held no copies in its first rows
d) It is useless, since it covers too few orders to matter

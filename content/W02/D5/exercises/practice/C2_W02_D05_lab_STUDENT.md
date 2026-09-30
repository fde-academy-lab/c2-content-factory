# The practice lab: the last mile, four problems

About an hour in the TA-led lab. Four problems, each harder than the one before, and the last one
combines the day's three rounds on a sheet you did not build. Answer every item with a letter; the
solution opens at the end of the lab.

Post exactly this shape, the eighteen letters in item order, no spaces: `xxxxxxxxxxxxxxxxxx`

---

## Problem 1. Who owns it, fifteen minutes

Eight asks the team received this week. For each, pick the tool that owns the number.

### Q1. Anand's Monday revenue by segment, which his analyst audits line by line. Which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q2. A director slices the reconciled tree by city during Monday's review. Which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q3. Removing the double-paid rows before any total is computed. Which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q4. Trying five definitions of an active member this afternoon to see which one separates the members who left. Which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q5. The chief of staff looks up one member by id on a laptop before a call. Which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q6. The booked-against-collected report Finance signs every month. Which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q7. A one-off look at whether returns cluster in one city, for a hypothesis nobody has funded yet. Which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q8. A what-if on next quarter's Retail-Plus recovery, for the growth review. Which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

---

## Problem 2. The misread, twelve minutes

Three draft cards for a front page. For each, pick what a director will misread and why.

### Q9. The card reads "Revenue up 12 percent". What will a director misread?

a) Nothing, since a percentage carries its own meaning
b) Which months grew, and against which, since neither is named
c) The size of the business, since the card carries no chart or table
d) The segment, since the card does not name one

### Q10. The card reads "Retail-Plus lost 15 members". What will a director misread?

a) The direction, since "lost" can mean churned or paused
b) The period, since members are counted every day
c) The cause, since the card does not say why they left
d) The size, since 15 of 91 Q1 members is 16.5 percent

### Q11. The card reads "Q2 orders 462, up from 538 in Q1". What will a director misread?

a) The base, since orders need a share of revenue beside them
b) The period, since Q2 is not spelled out in months
c) The direction, since 462 is 14.1 percent below 538
d) Nothing, since both quarters and both counts are named

---

## Problem 3. Predict the pivot, fifteen minutes

An invented export from Kalpa Retail's app channel, one row per payment: seven orders paid once,
worth Rs 20,000 together; two orders of Rs 40,000 and Rs 60,000, each paid in two instalments; and
one order of Rs 2,000 that the gateway posted twice. Each row carries its order's amount.

### Q12. What does a pivot's Sum of order_amount show for the whole export?

a) Rs 1,22,000
b) Rs 1,24,000
c) Rs 2,22,000
d) Rs 2,24,000

### Q13. After Remove Duplicates on every column, how many rows remain and what does the Sum show?

a) 12 rows, Rs 2,22,000
b) 10 rows, Rs 1,22,000
c) 11 rows, Rs 1,62,000
d) 13 rows, Rs 2,24,000

### Q14. Counting each order once, what is the total?

a) Rs 1,20,000
b) Rs 1,02,000
c) Rs 1,22,000
d) Rs 2,22,000

---

## Problem 4. A sheet you did not build, twenty minutes

A regional team sends Meera's chief of staff their own version of the deck pack. You have ten minutes
before it goes on screen. Four things you notice:

### Q15. Its grand total is Rs 4.10 crore for two quarters the warehouse books at Rs 2.05 crore, and its export has 2,900 rows for 2,000 orders. What do you fix?

a) The date filter, since two periods overlap in the pivot
b) The grain: count each order once before summing
c) The segment mapping, since one segment is counted twice
d) Nothing, since the pivot's Sum is the export's total

### Q16. Its lookup returns a member's revenue for C-0888, an id the team says left last year. What do you fix?

a) The match type: exact, with a visible not-found path
b) The sort order of the ids, so the lookup finds the member
c) The revenue column, which holds last year's figures
d) Nothing, since a departed member keeps their history

### Q17. Filtered to Chennai, the foot of its list does not move. What do you fix?

a) The filter, since Chennai has no members on the list
b) The list size, since the filter cannot reach row fifty
c) The city column, which holds codes the filter misses
d) The foot: SUBTOTAL(109) in place of SUM

### Q18. Its card says a segment fell 25 percent, from Rs 4.00 lakh to Rs 3.20 lakh. What do you fix?

a) Nothing, since Rs 80,000 is a quarter of the segment
b) The base: it is 20 percent, measured on the earlier quarter
c) The period, since one quarter is too short a window to compare fairly
d) The rounding, since the change is 25.0 percent exactly

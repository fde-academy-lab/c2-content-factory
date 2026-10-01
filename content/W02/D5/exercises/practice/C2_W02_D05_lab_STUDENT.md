# Can you place eight asks with their tool, read three front-page cards, predict a hurried pivot and repair a sheet you did not build, in an hour?

The TA-led practice lab, after the afternoon block: four problems, about an hour, each harder than
the one before, and the last one combines the day's chapters on a sheet somebody else built. Answer
every item with a letter; the solution opens at the end of the lab.

> "Everything you built this week has to survive a room that only has Excel. Which parts belong in
> Excel, which parts must never be in Excel, and how do you keep the two from drifting apart?"
>
> Kavya Nair, senior analyst, Kalpa Retail data team

This week Kalpa Retail's data team answered its stakeholders in three tools: SQL in the warehouse, the
Postgres database that holds one row per order and one per payment and is the source of truth; pandas
in a notebook, where an analyst iterates; and Excel, where a director reads, slices and asks what-ifs
without a login. The team's rule: the warehouse owns the number and every join, dedupe and rank
Finance relies on; pandas owns the analyst's iteration until Finance relies on it; the workbook owns
the last mile, on an export that ties. Anand Iyer is Kalpa Retail's finance controller, and Meera
Raghavan its CEO. A front-page card prints its number with its period (the months), its comparison
(what it is set against) and its base (the rupees a percentage is taken of), and measures a change on
the earlier period. A payment export holds one row per payment with the order's amount on every row of
that order; Remove Duplicates deletes rows identical in every column. Q1 runs from April to June 2026
and Q2 from July to September 2026.

**Who needs the answer.** You, practising the day's checks on cases you have not seen. Each problem is
a way the traps arrive at work: in a request, in a draft card, in an export, and in a colleague's
sheet ten minutes before a meeting.

**The questions on the way.**

- Which tool owns each of eight asks the team received this week?
- What will a director misread in each of three draft cards?
- What does a hurried pivot print on an invented export, and what does the honest card say?
- Which repair does a regional team's sheet need first, item by item?

Post one line of eighteen letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxxxxxxxxxxxxxx
```

---

## Problem 1. Which tool owns each of eight asks the team received this week?

Used at work every time a request arrives and someone has to decide where its answer lives.

Fifteen minutes. Eight asks; for each, pick the tool that owns the number.

### Q1. Anand's Monday revenue by segment, which his analyst audits line by line: which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q2. A director slices the reconciled tree by city during Monday's review: which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q3. Counting each order once in the payment export every week, before any total is computed: which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q4. Trying five definitions of an active member this afternoon, to see which one separates the members who stopped buying: which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q5. The chief of staff looks one member up by id on a laptop before a call: which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q6. The booked-against-collected report Finance signs every month: which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q7. A one-off look at whether returns cluster in one city, for a hypothesis nobody has funded yet, when returns sit in neither of the exports the workbook reads: which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

### Q8. A what-if on next quarter's Retail-Plus recovery, asked for in the growth review: which tool owns it?

a) SQL in the warehouse
b) pandas in a notebook
c) Excel on the export

---

## Problem 2. What will a director misread in each of three draft cards?

Used at work whenever a number reaches a page that people read in two minutes.

Twelve minutes. Three draft cards for the front page; for each, pick what a director will misread.

### Q9. The card reads "Revenue up 12 percent". What will a director misread?

a) The rounding, since 12 percent could be anything from 11.5 to 12.4
b) Which months grew, and against which, since neither is named
c) The size of the business, since there is no chart drawn beside it
d) The segment, since the card does not say which one it means

### Q10. The card reads "Student orders, Q2: up 41 percent on Q1". Student, one of Kalpa's four segments, placed 27 orders in Q1 and 38 in Q2, from 20 customers in Q2. What will a director misread?

a) The direction, since a rise in orders can come with falling revenue
b) The period, since orders are counted every day of the quarter
c) The size, since 41 percent sits on 27 orders and 20 customers
d) The segment, since Student is the smallest of the four

### Q11. The card reads "Q2 orders 462, up from 538 in Q1". What will a director misread?

a) The base, since a count of orders needs a share of revenue beside it
b) The period, since Q2 is not spelled out in its months
c) The direction, since 462 is 14.1 percent below 538
d) Nothing, since both quarters and both counts are named

---

## Problem 3. What does a hurried pivot print on an invented export, and what does the honest card say?

Used at work every time an export arrives at a grain nobody stated.

Fifteen minutes. An invented export from Kalpa's app channel holds one row per payment, with each
order's amount on every row of that order. In Q1: six orders paid once, Rs 30,000 together, and two
orders of Rs 20,000 each, paid in two instalments on different dates. In Q2: five orders paid once,
Rs 17,000 together; one order of Rs 40,000, paid in two instalments on different dates; and one order
of Rs 3,000, which the gateway posted twice.

### Q12. What does a pivot's Sum of order_amount print for Q1 and Q2, and what change does it show?

a) Rs 1,10,000 and Rs 1,03,000, down 6.4 percent
b) Rs 70,000 and Rs 60,000, down 14.3 percent
c) Rs 1,10,000 and Rs 1,00,000, down 9.1 percent
d) Rs 1,10,000 and Rs 1,03,000, down 6.8 percent

### Q13. After Remove Duplicates on every column, what change does the pivot show?

a) Down 6.4 percent, since nothing in the export is an exact copy
b) Down 9.1 percent, Rs 1,00,000 against Rs 1,10,000
c) Down 14.3 percent, Rs 60,000 against Rs 70,000
d) Down 10.0 percent, Rs 1,00,000 against Rs 1,10,000

### Q14. Counted once per order, which card goes on the front page?

a) App channel, Q2: Rs 60,000, down 14.3 percent on Q1 (Rs 70,000)
b) App channel, Q2: Rs 60,000, down 16.7 percent on Q1 (Rs 70,000)
c) App channel: Rs 1,30,000 across the half-year, down Rs 10,000
d) App channel, Q2: Rs 60,000, down 9.1 percent on Q1 (Rs 70,000)

---

## Problem 4. Which repair does a regional team's sheet need first, item by item?

Used at work in the ten minutes before somebody else's numbers go on screen with your name beside
them.

Twenty minutes. A regional team sends Meera's chief of staff its own version of the deck pack, and you
have ten minutes before it goes on screen. Four things you notice:

### Q15. Its grand total is Rs 4.10 crore for two quarters the warehouse books at Rs 2.05 crore, and its export has 2,900 rows for 2,000 orders. What do you fix?

a) The date filter, since two periods overlap inside the pivot
b) The grain: count each order once before anything is summed
c) The segment mapping, since one segment is counted twice over
d) Nothing, since a pivot's Sum is the export's own total

### Q16. Its lookup returns a member's revenue for C-0888, an id the team says left last year. What do you fix?

a) The match type: exact, with a not-found path the room can see
b) The sort order of the ids, so the lookup finds the right member
c) The revenue column, which may still hold last year's figures
d) Nothing, since a member who left keeps a row of history

### Q17. Filtered to Chennai, the foot of its list does not move. What do you fix?

a) The filter, since Chennai may have no members on the list
b) The list size, since the filter cannot reach row fifty
c) The city column, which may hold codes the filter misses
d) The foot: SUBTOTAL(109) where it has SUM

### Q18. Its card says a segment fell 25 percent, from Rs 4.00 lakh to Rs 3.20 lakh. What do you fix?

a) Nothing, since Rs 80,000 is a quarter of the segment's revenue
b) The change: 20 percent, measured on the earlier quarter
c) The period, since one quarter is too short to compare
d) The rounding, since the change is 25.0 percent exactly

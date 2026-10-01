# How much did revenue fall from Q1 to Q2, and in which segment and which leaf?

Chapter 2 set, six items, after chapter 2: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "Monday's growth review deck needs three things I can open on my laptop without a login: the
> revenue tree by segment for both quarters, the top-fifty protect list with a lookup so I can find
> any member by id, and one number on the front page with its trend."
>
> Meera's chief of staff, Kalpa Retail

Kalpa's Q1 runs from April to June 2026 and its Q2 from July to September 2026. The warehouse is the
Postgres database the team queried on Monday: it holds one row per order and is the source of truth
every sheet ties back to, and it puts revenue, booked order value in rupees, at Rs 10,00,00,000 in Q1
and Rs 9,84,00,000 in Q2. The raw export the data team sent for the deck holds one row per payment,
with the order's amount repeated on every row of that order, so an order paid in two instalments
sits on two rows, and so does an order the payment gateway posted twice. Excel's Remove Duplicates
deletes the rows that are identical in every column ticked. A first-row flag,
`=IF(COUNTIF($A$2:A2,A2)=1,1,0)` filled down beside the order ids in column A, is 1 on the first row
of each order and 0 on the rest, so adding only the flagged rows counts each order once. Kalpa's four
segments are Retail-Core, Retail-Plus (the paid membership tier), Business and Student, and the
revenue tree splits revenue into customers, orders per customer and revenue per order.

**Who needs the answer.** The chief of staff needs the tree for both quarters on page two, and Meera
Raghavan, Kalpa Retail's CEO, decides from it which branch of the tree the growth plan funds. A pivot
that counts some orders twice puts nearly twice Finance's revenue in front of the directors and can
call a falling segment healthy, which sends the plan after the wrong segment.

**The questions on the way.**

- What does a pivot's Sum show for an invented store's July, and what is its booked revenue?
- How many rows does Remove Duplicates leave on the same export, and what does the Sum then show?
- How many comparisons does the running COUNTIF make on next quarter's export, and what replaces it?
- Which decision would the pivot on the payment rows have misled for Retail-Core?
- Which check can disagree with the flagged pivot when the flag is wrong?
- What do you do when an order-grain export arrives two days after the deck is due?

Every number in items 1 and 2 is invented; items 3 to 6 use Kalpa's own export and warehouse.

**What you post.** One line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

### Q1. What does a pivot's Sum show for an invented store's July, and what is its booked revenue?

An invented export of one Kalpa store's July holds one row per payment, with each order's amount on
every row of that order: 20 orders paid once, worth Rs 50,000 together; 5 orders of Rs 10,000 each,
paid in two instalments on different dates; and 2 orders of Rs 1,500 each, which the gateway posted
twice. What does a pivot's Sum of order_amount show for July, and what is July's booked revenue?

a) Rs 1,56,000 on the pivot, and Rs 1,03,000 booked
b) Rs 1,56,000 on the pivot, and the same booked, since every row is a payment
c) Rs 1,03,000 on the pivot, and Rs 1,03,000 booked
d) Rs 1,53,000 on the pivot, and Rs 1,00,000 booked

### Q2. How many rows does Remove Duplicates leave on the same export, and what does the Sum then show?

The same invented July export. The analyst runs Data, Remove Duplicates with every column ticked,
then reads the pivot's Sum again. How many rows remain, and what does the Sum show?

a) 27 rows, and Rs 1,03,000
b) 29 rows, and Rs 1,06,000
c) 32 rows, and Rs 1,53,000
d) 34 rows, and Rs 1,56,000

### Q3. How many comparisons does the running COUNTIF make on next quarter's export, and what replaces it?

The first-row flag compares each row's order id with every id above it, so row 2 makes one
comparison, row 3 two, and so on: on today's 1,450 rows that is 1,051,975 comparisons. The data
team says next quarter's export will have 145,000 rows. About how many comparisons will the flag
make then, and what should replace it?

a) About 145,000, one a row, so the flag can stay as it is in the sheet
b) About 10.5 billion, so sort by order id and compare each row with the one above
c) About 10.5 billion, so run Remove Duplicates first and flag what is left
d) About 105 million, a hundred times today's, so the flag can stay on a fast laptop

### Q4. Which decision would the pivot on the payment rows have misled for Retail-Core?

On the payment rows, the pivot says Retail-Core, Kalpa's everyday shoppers, grew 1.0 percent from Q1
to Q2. Counted once per order, Retail-Core fell 1.8 percent, from Rs 3,73,070 to Rs 3,66,250. Which
decision would the first reading have misled?

a) Leaving Retail-Core out of the growth plan as the segment that needs nothing
b) Moving Business's invoices into the next quarter to smooth out the company line
c) Pausing the Student segment's campaigns until the next growth review
d) Asking Finance to restate Q1 for the whole company before Monday's deck

### Q5. Which check can disagree with the flagged pivot when the flag is wrong?

The flagged pivot says Q1 is Rs 10,00,00,000 and Q2 is Rs 9,84,00,000. A second route has to share
none of the flagged pivot's steps, so it can fail when the flag is wrong. Which of these is one?

a) A pivot on the flagged rows with quarter in Rows and segment in Columns
b) The count of flags compared with the count of rows that carry a 1
c) The export's paid_amount column, summed by the quarter of each payment date
d) The warehouse's own orders table, one row per order, summed by quarter

### Q6. What do you do when an order-grain export arrives two days after the deck is due?

The data platform lead, who owns the warehouse, offers an export with one row per order, which needs
no flag. It arrives on Wednesday, two days after Monday's growth review. What do you do for Monday?

a) Wait for Wednesday's export and send the tree two days late, since only it is exact
b) Build Monday's tree on the flag, tie it to the warehouse, and switch on Wednesday
c) Build Monday's tree from the customer table split on each customer's last order date
d) Run Remove Duplicates for Monday, and use Wednesday's export only if the totals differ

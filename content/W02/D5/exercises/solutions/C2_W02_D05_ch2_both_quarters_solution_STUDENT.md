# Which answers hold in the chapter 2 set on how far revenue fell from Q1 to Q2, and why?

Answers: 1a 2c 3b 4a 5d 6b

Meera's chief of staff asked for the revenue tree by segment for both quarters, Q1 (April to June
2026) and Q2 (July to September 2026), and every number on the deck has to tie to the warehouse,
which holds one row per order and gave Rs 10,00,00,000 for Q1 and Rs 9,84,00,000 for Q2. The raw
export the deck is built from holds one row per payment, with the order's amount on every row of
that order. Chapter 2 found what a pivot does on that export and how to count each order once with a
first-row flag; counted that way, revenue fell 1.6 percent, Rs 16,00,000, and Retail-Plus, the paid
membership tier, fell steepest, 29.4 percent, because its members ordered less often. Three of the
six items are design items: 3, 5 and 6.

**Who needs the answer.** You, checking your six letters after the lab or tonight. Each wrong letter
here is a wrong page two on Monday: a total near twice Finance's, a segment called healthy that fell,
or a deck held back for an export that could wait.

**The questions on the way.**

- Which idea does the chapter 2 set test: that a total is only right at the grain it was asked at?
- Why does each of the six keys hold, from the invented July to Wednesday's export?
- Why is option c in item 3, Remove Duplicates before the flag, the wrong answer worth arguing about?
- Where does Razorpay, the Indian payment gateway, meet the same two grains?

## Which idea does the chapter 2 set test: that a total is only right at the grain it was asked at?

A Sum adds one value per row, so the question before any pivot is what one row stands for. On an
export with one row per payment, the order's amount repeats, and the Sum counts it once per payment.
The live items size that on an invented store; the design items ask what a flag costs at a hundred
times the rows, which route can disagree with the flag, and how to ship on time while the right export
is on its way.

## Why does each of the six keys hold, from the invented July to Wednesday's export?

### Q1. What does a pivot's Sum show for an invented store's July, and what is its booked revenue?

Twenty orders paid once (Rs 50,000 together), five orders of Rs 10,000 each paid in two instalments,
and two orders of Rs 1,500 each posted twice, with each order's amount on every one of its rows.

The key is a, "Rs 1,56,000 on the pivot, and Rs 1,03,000 booked". The export has 34 rows: 20, plus 10
instalment rows, plus 4 gateway rows. Its Sum is Rs 50,000 plus 10 times Rs 10,000 plus 4 times
Rs 1,500, which is Rs 1,56,000. Each order counted once gives Rs 50,000 plus Rs 50,000 plus Rs 3,000,
which is Rs 1,03,000 booked.

- b, "Rs 1,56,000 on the pivot, and the same booked, since every row is a payment": every row is a
  payment, and booked revenue counts orders, so the order's amount must be added once.
- c, "Rs 1,03,000 on the pivot, and Rs 1,03,000 booked": the pivot adds every row it is given, so it
  cannot show the once-per-order figure on this export.
- d, "Rs 1,53,000 on the pivot, and Rs 1,00,000 booked": Rs 1,53,000 is the Sum after Remove
  Duplicates, and Rs 1,00,000 leaves out the two gateway orders, which were sold.

### Q2. How many rows does Remove Duplicates leave on the same export, and what does the Sum then show?

The same 34 rows, with every column ticked.

The key is c, "32 rows, and Rs 1,53,000". Remove Duplicates deletes rows identical in every column.
The two gateway orders each have two identical rows, so one copy of each goes: 32 rows, and the Sum
falls by Rs 3,000 to Rs 1,53,000. The five instalment orders keep both rows, because their two rows
differ in paid_date.

- a, "27 rows, and Rs 1,03,000": that is one row per order, which Remove Duplicates gives only when
  every repeat is identical.
- b, "29 rows, and Rs 1,06,000": that removes the instalment repeats and keeps the gateway copies,
  the opposite of what the tool does.
- d, "34 rows, and Rs 1,56,000": the tool does remove the two identical copies.

### Q3. How many comparisons does the running COUNTIF make on next quarter's export, and what replaces it?

A design item. The flag compares each row with every row above it: 1,450 rows cost 1,051,975
comparisons today.

The key is b, "About 10.5 billion, so sort by order id and compare each row with the one above". Row
n makes n minus 1 comparisons, so n rows make about n squared over 2: 145,000 times 145,001 over 2 is
about 10.5 billion, enough to freeze a laptop. Sorted by order id, a row is an order's first exactly
when its id differs from the row above, `=IF(A3<>A2,1,0)`, one comparison a row. The better move is
upstream: ask the warehouse for an export at the order grain, and keep the flag as a check.

- a, "About 145,000, one a row, so the flag can stay as it is in the sheet": the running range grows
  with every row, so the count grows with the square of the rows.
- c, "About 10.5 billion, so run Remove Duplicates first and flag what is left": the count is right,
  and Remove Duplicates removes only identical copies, so on Kalpa's export 1,400 of 1,450 rows remain
  and the cost barely moves.
- d, "About 105 million, a hundred times today's, so the flag can stay on a fast laptop": a hundred
  times the rows is ten thousand times the comparisons, so scaling today's count by a hundred
  understates it a hundredfold.

### Q4. Which decision would the pivot on the payment rows have misled for Retail-Core?

On the payment rows Retail-Core grew 1.0 percent; counted once per order it fell 1.8 percent, from
Rs 3,73,070 to Rs 3,66,250.

The key is a, "Leaving Retail-Core out of the growth plan as the segment that needs nothing". The
growth plan funds the branches that fell, so a segment shown rising is the one it leaves alone, and
here that segment fell.

- b, "Moving Business's invoices into the next quarter to smooth out the company line": Business is not
  the segment the wrong reading flattered, and no reading justifies moving invoices.
- c, "Pausing the Student segment's campaigns until the next growth review": Student's reading is not
  the one in question.
- d, "Asking Finance to restate Q1 for the whole company before Monday's deck": Finance's Q1 is right;
  the pivot is what is wrong.

### Q5. Which check can disagree with the flagged pivot when the flag is wrong?

A design item. A second route shares none of the flagged pivot's steps.

The key is d, "The warehouse's own orders table, one row per order, summed by quarter". The warehouse
never saw the export or the flag, so a flag that missed an order or kept a repeat would disagree with
it. Chapter 2's notebook ran this route, and both quarters tied to the rupee, with the order counts.

- a, "A pivot on the flagged rows with quarter in Rows and segment in Columns": the same flagged rows
  rearranged repeat the flag's mistake.
- b, "The count of flags compared with the count of rows that carry a 1": the two counts are the same
  thing counted twice, so they cannot disagree.
- c, "The export's paid_amount column, summed by the quarter of each payment date": that is collected
  money by payment date, which differs from booked revenue by order date even when every step is
  right, so a mismatch proves nothing.

### Q6. What do you do when an order-grain export arrives two days after the deck is due?

A design item. The right export arrives on Wednesday, and the deck goes on Monday.

The key is b, "Build Monday's tree on the flag, tie it to the warehouse, and switch on Wednesday". The
flag gives the right tree today, and the tie to the warehouse proves it; the order-grain export then
replaces a cleaning step that has no record with one that has. The fact that would change the call is
a deadline far enough away for the warehouse team to answer first.

- a, "Wait for Wednesday's export and send the tree two days late, since only it is exact": the
  flagged tree, tied to the warehouse to the rupee, is exact too.
- c, "Build Monday's tree from the customer table split on each customer's last order date": that
  split puts Rs 17.88 crore in Q2, since a customer who bought in both quarters lands wholly in Q2.
- d, "Run Remove Duplicates for Monday, and use Wednesday's export only if the totals differ": Remove
  Duplicates leaves Kalpa's export at Rs 39,40,57,740, nearly twice the warehouse.

## Why is option c in item 3, Remove Duplicates before the flag, the wrong answer worth arguing about?

Because the tool has a name that promises the fix. On Kalpa's export, 450 orders sit on two rows: 400
paid in two instalments, whose rows differ in the amount paid, and 50 posted twice by the gateway,
whose rows are identical. Remove Duplicates takes out the 50 copies, the total moves from
Rs 39,40,95,490 to Rs 39,40,57,740, and the analyst believes the export is clean. The grain is fixed
by naming the key, the order id, and counting each id once.

## Where does Razorpay, the Indian payment gateway, meet the same two grains?

Razorpay's documentation says its orders feature "Combines multiple payment attempts for a single
order", and that on part payments "each partial payment would have a unique payment_id, but will be
tied to the same order_id" (Razorpay documentation, Orders and Payment Links partial payments, checked
30 September 2026). Any merchant who exports payments and pivots on the order amount meets the trap
this chapter staged; one who adds the amount paid per order is answering a collections question,
which chapter 5 takes up.

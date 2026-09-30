# Which extra piece fits where you are after today: the stretch or the recovery?

**Who needs the answer.** You do, before Tuesday: the stretch takes today's payback question further
for anyone who finished early, and the recovery rebuilds each chapter's number for anyone the loops
left behind.

**The questions on the way.** What would marketing's Rs 12 crore buy in revenue Meera could see this
year? Can you rebuild each chapter's number one loop at a time?

Both are optional and neither is graded. Pick the one that matches where you are after today's
chapters, and do it tonight or before Tuesday's session.

---

## What would marketing's Rs 12 crore buy, in revenue Meera could see this year?

This is the stretch, for you if the six chapters and the escalated case felt comfortable and you
finished the take-home early. Finance teams test an acquisition budget this way before they sign
it.

> "Suppose I did give marketing the Rs 12 crore. What would it buy me, in revenue I could see this
> year?"
> Meera Raghavan, CEO, Kalpa Retail

Work in a new notebook on today's file. Every assumption you add is invented, and you label it
invented where it appears. Two facts from today come with you. The booked mean order is Rs 18,160,
Rs 5,44,810 over 30 orders. Meera's growth plan concerns the three consumer segments, Retail-Core,
Retail-Plus and Student, and the orders in those segments average Rs 2,235 each.

- Take an invented cost of Rs 1,500 to acquire one new customer. How many new customers does
  Rs 12 crore buy?
- Value each new customer's first order twice: once at the booked mean, Rs 18,160, and once at the
  consumer segments' mean, Rs 2,235. Write both totals in crore.
- Chapter 3 found 1.30 orders per customer in one quarter. If new customers behave like today's
  customers, how many orders does each place in their first quarter, and what does that do to each
  total?
- Write one line on which of your two totals marketing's case most likely used, and one line on
  what a second quarter of data would have to show before you believed either.

You have done it well if your two first-quarter totals differ by a factor of about eight, and your
last line names a branch and a number that Tuesday's two quarters would produce.

---

## Can you rebuild each chapter's number one loop at a time?

This is the recovery, for you if the loops moved faster than you did today; doing it tonight costs
nothing tomorrow. Every analyst rebuilds a number by hand once before trusting the shortcut that
computes it. Work in a fresh cell of `notebooks/C2_W01_D01_01_four_readings_of_sales_STUDENT.ipynb`,
and run after every step.

- Print the first record on its own, and say each field and its type aloud.
- Write the loop that prints every status and nothing else. Then add a counter above it that counts
  the cancelled orders, and print the counter after the loop. It should print 4.
- Add a running total that sums the amounts of the orders that are not cancelled. If the sum stops,
  read the last line of the message, print the order it stopped on, and convert with int(). It
  should print 535760.
- Make an empty set above a new loop and add each customer id to it. Print its length. It should
  print 23, and 30 would mean you counted rows.
- Divide the number of orders by the length of the set. It should print about 1.30.
- Sort the amounts and print the two in the middle, the 15th and 16th. Their average should be
  2205.

Each chapter was one loop with one decision in it: which orders count, what makes a customer
distinct, and where the middle sits. The checks tell you whether the decision was right before
anybody else reads the number.

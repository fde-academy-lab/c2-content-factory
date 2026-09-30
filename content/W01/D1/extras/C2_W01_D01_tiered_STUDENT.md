# Extras: one to stretch, one to recover

Both are optional and neither is graded. Pick the one that matches where you are after today's
chapters, and do it tonight or before Tuesday's session.

---

## Stretch: what the Rs 12 crore buys at an honest first order

For you if the six chapters and the escalated case felt comfortable and you finished the take-home
early.

> "Suppose I did give marketing the Rs 12 crore. What would it buy me, in revenue I could see this
> year?"
> Meera Raghavan, CEO, Kalpa Retail

Work in a new notebook on today's file. Every assumption you add is invented, and you label it
invented where it appears.

- Take an invented cost of Rs 1,500 to acquire one new customer. How many new customers does
  Rs 12 crore buy?
- Value each new customer's first order twice: once at the booked mean, Rs 18,160, and once at the
  booked median, Rs 2,205. Write both totals in crore.
- Chapter 3 found 1.30 orders per customer in one quarter. If new customers behave like today's
  customers, how many orders does each place in their first quarter, and what does that do to each
  total?
- Write one line on which of your two totals marketing's case most likely used, and one line on
  what a second quarter of data would have to show before you believed either.

**A tell that you have done it well.** Your two first-quarter totals differ by a factor of about
eight, and your last line names a branch and a number that Tuesday's two quarters would produce.

---

## Recovery: the chapters, one loop at a time

For you if the loops moved faster than you did today. Doing this tonight costs nothing tomorrow.
Work in a fresh cell of `notebooks/C2_W01_D01_01_four_readings_of_sales_STUDENT.ipynb`, and run after every
step.

- Print the first record on its own, and say each field and its type aloud.
- Write the loop that prints every status, nothing else. Then add a counter above it that counts
  the cancelled orders, and print the counter after the loop. It should print 4.
- Add a running total that sums the amounts of the orders that are not cancelled. If the sum stops,
  read the last line of the message, print the order it stopped on, and convert with int(). It
  should print 535760.
- Make an empty set above a new loop and add each customer id to it. Print its length. It should
  print 23, and 30 would mean you counted rows.
- Divide the number of orders by the length of the set. It should print about 1.30.
- Sort the amounts and print the two in the middle, the 15th and 16th. Their average should be
  2205.

**What you should end up believing.** Each chapter was one loop with one decision in it: which orders
count, what makes a customer distinct, and where the middle sits. The checks tell you whether the
decision was right before anybody else reads the number.

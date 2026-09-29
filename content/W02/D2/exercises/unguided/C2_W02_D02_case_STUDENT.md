# The escalated case: the report Anand signs

Forty-five minutes, alone, unguided. There are no hints in this brief, and the solution opens at the
close of the session.

---

## The ask

Anand Iyer, finance controller, Kalpa Retail, has read the morning's work and replies:

> "Booked revenue is not collected revenue. Some orders are paid in two instalments, some are
> refunded, some were never paid at all. Show me, order by order, what we actually collected against
> what we booked in Q2. If there is a gap, I want to know which orders and which channel."

The platform lead has repeated the warning that the payments feed sometimes double-posts when the
gateway retries. You sign off the collected number, and Anand will ask how you know it is not
double-counted before he uses it. Kavya reviews your report before it leaves the team, and she reads
the reconciliation before she reads any number.

## Where you work

- Start from `sql/C2_W02_D02_05_case_start_STUDENT.sql`. It runs as it stands against the warehouse,
  and each part below says what you add to it.
- Or work in `notebooks/C2_W02_D02_case_STUDENT.ipynb`, which carries the same five parts as cells
  to complete. Choose one and finish in it.
- Q2 is the quarter, every order in it counts toward booked whatever its status, and the three
  channels are app, store and web.

---

## Part 1. The baseline, from orders alone

Booked by channel for Q2, with the order count beside each channel and the total under them, from
the orders table with no join. This is the number every later part reconciles to, so write it down
before you write any join.

## Part 2. Collected, at order grain, with the count reconciliation above it

Collected by channel for Q2, with payments brought to one row per order before they meet the orders
table, and with a retry counted once. Above the query, as a comment block, write the reconciliation
before you run it: orders in from part 1, rows out from this query, the difference, and what the
difference is made of. After you run it, fill in the numbers and say whether the count closed.

## Part 3. The unpaid list

Every Q2 order with no payment at all: order id, channel, status and booked amount, largest first,
with the count and the booked total by channel under it.

## Part 4. The double-paid list

Every Q2 payment the gateway posted more than once: order id, channel, instalment, the number of
times it was posted and the surplus. A second instalment is a real payment, and your list must hold
retries only, so write one comment line saying what in the data makes a retry a retry. Put the
surplus total by channel under the list.

## Part 5. The report by channel, the checks and the sentence

One table by channel: orders, booked, collected, gap, the unpaid count and value, and the surplus
posted twice. Under it, the checks, each as a query that returns true or false:

1. Booked minus collected equals the unpaid total, by channel and in all.
2. Every payment row in the feed is accounted for: matched to a Q2 order, matched to a Q1 order, or
   matched to no order at all, with the three counts adding to the table's row count.
3. The bridge closes: booked, less the unpaid, equals collected; collected, plus the surplus posted
   twice, equals what the feed posted against Q2 orders.

Then write two sentences to Anand. The first gives him the collected number and the gap, and says
how you know the collected number is not double-counted. The second tells him which orders and which
channel to chase first, and what you are sending to the platform lead.

---

## What you hand in

The SQL file or the notebook, run top to bottom from a fresh connection or a fresh kernel, with every
check reading true, and the two sentences at the end.

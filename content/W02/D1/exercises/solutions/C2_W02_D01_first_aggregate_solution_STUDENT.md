# Which answers hold in the guided build of the segment counts and revenue, and why?

Answers: 1a 2d 3c 4b 5a

The guided exercise built one query a clause at a time, from the whole book to one row per segment and
quarter with its orders, customers and booked revenue, while the trainer said aloud the order in which
the database works. The five items ask what each new clause does before it runs. None of them is a
design item: the guided build is the one place in the day where the trainer chooses every step, and
the design items sit in the chapter sets and the two cases.

**Who needs the answer.** You, after chapter 3, checking five letters. Anand's analyst will ask how any
segment line was built, and the answer is the order the clauses run in.

**The questions on the way.**

- Which idea does this exercise test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this exercise test?

A query is written SELECT first and worked through FROM first: the rows are made, the lookup finds each
order's customer, the groups form, and only then are the counts and sums computed inside each group
and the result sorted. Each item asks what one of those stages does to the rows before the result
shows it.

## Why is each key right, item by item?

### Q1. How many rows does the lookup line leave for the groups to work on?

Kind: predict the output. The key is a, "1,000, since each order finds one customer". Every
order carries one customer id and every id sits once on the customers table, so the lookup adds the
segment to each order and keeps 1,000 rows; step 3's four rows add back to 1,000 orders.

- b, "340, one for each customer on the customers table": the rows come from the orders; the customers
  table only lends each order its segment.
- c, "1,340, the two tables' rows side by side": the lookup puts each order beside its customer, and
  stacks nothing.
- d, "301, one for each customer who bought": that is a count of different customers, which the lookup
  does not compute.

### Q2. How many rows come back once the groups are segment and quarter?

Kind: predict the output. The key is d, 8: four segments times two quarters, each with orders.

- a, 4: the step 3 answer, before the quarter joined the groups.
- b, 2: the step 2 answer, one row per quarter.
- c, 1,000: grouping gathers the orders into groups, one row each, and never returns every order.

### Q3. What can Retail-Plus's Q1 customer count be, before you run it?

Kind: reason to the number before running. The key is c, 91. A count of customers who bought can be no
larger than the tier's orders, 215, and no larger than its members, 120; of the four, only 91 fits
under both, and step 5 prints 91.

- a, 215: the orders, which is what `count(*)` prints; a customer with three orders would count three
  times.
- b, 120: the tier's members, which includes those who bought nothing in Q1.
- d, 250: more than both the orders and the members, which no count of customers can be.

### Q4. In which order does the database work through step 5's clauses?

Kind: order the steps. The key is b, "FROM with the lookup, then GROUP BY, then SELECT, then ORDER BY".
The rows must exist before they can be grouped, the groups must exist before anything is counted
inside them, and the result must exist before it can be sorted.

- a, "SELECT, then FROM with the lookup, then GROUP BY, then ORDER BY": the order the query is
  written in, which is not the order it runs in.
- c, "FROM with the lookup, then SELECT, then GROUP BY, then ORDER BY": computes the counts before the
  groups exist, so there would be nothing to count them in.
- d, "GROUP BY, then FROM with the lookup, then SELECT, then ORDER BY": groups rows before any have
  been read.

### Q5. Which segment's revenue per order fell from Q1 to Q2?

Kind: read the output. The key is a, Student: Rs 990 per order in Q1 and Rs 941 in Q2.

- b, Business: Rs 10,20,767 then Rs 10,72,358, a rise.
- c, Retail-Core: Rs 1,875 then Rs 1,898, a rise.
- d, Retail-Plus: Rs 2,725 then Rs 2,953, a rise, even as its orders fell from 215 to 140.

## Which wrong answer is worth arguing about?

Item 4, option a. The order a query is written in is the order most people read it in, and for a query
this short the difference seems academic. It stops being academic in chapter 3, where a filter on a
count has to wait for the groups to form, and in every query where SELECT names a column nobody grouped
on. Saying the running order aloud at each step is how the room learns to ask which clause a surprise
came from.

## Where does this show up at work?

Every analyst interview that includes SQL asks some version of item 4, usually as "explain the logical
order in which a query runs", and follows it with a query that fails because a clause needed something
an earlier clause had not produced yet.

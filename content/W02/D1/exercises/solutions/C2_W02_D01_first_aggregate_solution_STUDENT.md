# Which answers hold in the guided build of the segment counts and revenue, and why?

Answers: 1a 2d 3c 4a 5d

The guided exercise built one query a clause at a time, from the whole book to one row per segment and
quarter with its orders, customers and booked revenue, while the trainer said aloud the order in which
the database works. The five items ask what each new clause does before it runs. None of them is a
design item: the guided build is the one place in the day where the trainer chooses every step, and
the design items sit in the chapter sets and the two cases.

**Who needs the answer.** You do, when you check your five letters after chapter 3. Anand's analyst
will ask how any segment line was built, and the answer is the order the clauses run in.

**The questions on the way.**

- Which idea does the guided build test: the order the database works through a query's clauses?
- Why does each of the five keys hold, from the lookup's 1,000 rows to Retail-Plus's larger orders?
- Why is option b in item 4, the order the query is written in, worth arguing about?
- Where does item 4 come back in today's interview drill?

## Which idea does the guided build test: the order the database works through a query's clauses?

A query is written SELECT first and worked through FROM first: the rows are made, the lookup finds each
order's customer, the groups form, and only then are the counts and sums computed inside each group
and the result sorted. Each item asks what one of those stages does to the rows before the result
shows it.

## Why does each of the five keys hold, from the lookup's 1,000 rows to Retail-Plus's larger orders?

### Q1. How many rows does the lookup line leave for the groups to work on?

Kind: predict the output. The key is a, "1,000, since each order finds one customer". The lookup
adds each order's segment to its row and changes no row count, so the groups start from the 1,000
orders, and step 3's four rows add back to 1,000.

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

Kind: reason to the bound before running. The key is c, "At most 120, the members, whichever of
them bought". Only members can buy as Retail-Plus, so the count can be no larger than the tier's
120, which is tighter than the 215 orders; step 5 prints 91, so 29 members bought nothing in Q1.

- a, "Exactly 215, one for each order the tier placed": that is `count(*)`, the orders; a customer
  with three orders would count three times.
- b, "Exactly 120, every member of the tier counted once": the count holds only the members who
  bought in Q1, and nothing on the page says all of them did.
- d, "Between 120 and 215, since some members ordered twice": a member who orders twice is still one
  customer, so repeat orders can never lift the count above the 120 members.

### Q4. In which order does the database work through step 5's clauses?

Kind: order the steps. The key is a, "FROM with the lookup, then GROUP BY, then SELECT, then ORDER BY".
The rows must exist before they can be grouped, the groups must exist before anything is counted
inside them, and the result must exist before it can be sorted.

- b, "SELECT, then FROM with the lookup, then GROUP BY, then ORDER BY": the order the query is
  written in, and the database runs it in another.
- c, "FROM with the lookup, then SELECT, then GROUP BY, then ORDER BY": computes the counts before the
  groups exist, so there would be nothing to count them in.
- d, "GROUP BY, then FROM with the lookup, then SELECT, then ORDER BY": groups rows before any have
  been read.

### Q5. Which segment's revenue per order rose the most from Q1 to Q2?

Kind: read the output. The key is d, Retail-Plus: Rs 2,725 per order in Q1 and Rs 2,953 in Q2, up 8.4
percent, even as its orders fell from 215 to 140.

- a, Student: Rs 990 then Rs 941, a fall of 4.9 percent.
- b, Business: Rs 10,20,767 then Rs 10,72,358, up 5.1 percent, the largest rise in rupees and a
  smaller one as a share.
- c, Retail-Core: Rs 1,875 then Rs 1,898, up 1.2 percent.

## Why is option b in item 4, the order the query is written in, worth arguing about?

The order a query is written in is the order most people read it in, and on step 5 reading it that
way gives the right numbers. It gives the wrong expectation in chapter 3, where a filter on a count
has to wait for the groups to form, and in any query where SELECT names a column nobody grouped on.
Saying the running order aloud at each step is how the room learns to ask which clause a surprise
came from.

## Where does item 4 come back in today's interview drill?

The drill asks you to explain the logical order in which a SQL query runs. The answer runs FROM with
its lookup, WHERE, GROUP BY, HAVING, SELECT, ORDER BY and LIMIT, and it explains why SELECT cannot
print a column nobody grouped on and why WHERE cannot test a count.

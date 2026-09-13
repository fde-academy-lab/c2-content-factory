# Tuesday's Kahoot: joins, and the count that catches them

Ungraded. Seven questions, twenty seconds each.

## Q1. A LEFT JOIN keeps every unmatched row from which side?

a) The right side, the one being attached
b) Both sides equally, which is the point
c) Neither, unmatched rows are always dropped
d) The left side, the one named first <- correct

## Q2. 1,000 orders LEFT JOIN payments, where 450 orders carry two payment rows and 30 carry none. How many rows?

a) 1,420
b) 1,000
c) 1,450 <- correct
d) 1,480

## Q3. What does an INNER join do to the orders that were never paid?

a) Removes them, and says nothing about it <- correct
b) Returns them with NULL in the payment columns
c) Raises an error naming every unmatched row
d) Returns them once for each payment attempted

## Q4. "Orders with no payment", in join words. Which is it?

a) INNER JOIN payments, then filter on amount
b) LEFT JOIN payments, keep rows where it is NULL <- correct
c) RIGHT JOIN payments, keep rows where it is NULL
d) FULL OUTER JOIN, then count the rows returned

## Q5. Collected revenue doubled after a join. What do you look at first?

a) The payment amounts, for a currency error
b) The row count before and after the join <- correct
c) The order table, for duplicated order rows
d) The date range, for an overlapping quarter

## Q6. `HAVING count(*) > 1` on payments grouped by order finds what?

a) Payments larger than one rupee
b) Orders with exactly two payments
c) Orders paid more than once <- correct
d) Customers who placed several orders

## Q7. Return question, one level up

Monday you met WHERE and HAVING. One sentence each, and say which one could have found today's
double-posted orders.

a) WHERE filters groups, HAVING filters rows, so WHERE would find them here
b) WHERE filters rows, HAVING filters groups, so HAVING finds them <- correct
c) Both of them filter rows, and HAVING is simply the newer of the two
d) HAVING only ever works with count, so WHERE is the general one

## Trainer note

Q2 is the one worth slowing down on. A room that gets it right has usually added 450 to 1,000 and
stopped, which is the right answer by a wrong route: the 30 unpaid orders still contribute one row
each, and it is worth asking where those 30 went before moving on.

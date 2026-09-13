# Solutions: which join answers this

Answers: 1b 2a 3c 4d 5b

## Q1. LEFT JOIN, keep the NULL payments

The anti-join. Keep every order, then keep only the ones that failed to match. Option a is the
common wrong answer and it is wrong in the worst way: an `INNER JOIN` has already removed exactly
the rows you are looking for, so the query returns nothing and looks like good news.

## Q2. LEFT JOIN from payments, keep the NULL orders

The same pattern, anchored on the other table. The anchor is the choice, and it is the choice
people skip. Ask which side you want to keep everything from before you write the word `JOIN`.

## Q3. Aggregate payments per order, INNER JOIN, then sum

Two things have to be true at once: only paid orders count, and no order may be counted twice.
`INNER` gives you the first. Aggregating payments to one row per order first gives you the second.

Option b gets the filter right and the arithmetic wrong, which is why it is the dangerous one. It
returns a plausible number, per channel, that is roughly double.

## Q4. FULL OUTER JOIN, keeping rows where either side is NULL

Anand asked for one table showing both directions. Option b produces the same information and
makes him read two stacked result sets, which is a worse answer to the question he actually asked
rather than a wrong answer to a different one.

This is the one place `FULL OUTER` earns its keep, and it is worth noticing that the question had
to be phrased that specifically before it did.

## Q5. Aggregate per order first, then LEFT JOIN and sum

`LEFT` rather than `INNER`, because the question is what we collected out of what we booked, and
an unpaid order is part of that story with a collected value of zero.

Then `coalesce`, or the unpaid orders turn the total into NULL. Option a fans out. Option c
silently changes the denominator. Option d assumes the thing the day disproved.

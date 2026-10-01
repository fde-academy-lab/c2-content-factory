# Which of Tuesday's ideas held? Eight Kahoot questions

Eight items, ungraded, scored on correctness and speed together. Item 7 reaches back to Monday, one
level up: Monday separated WHERE from HAVING on one table, and today the same two clauses sit on
either side of a join.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. Orders LEFT JOIN payments. Which side keeps its unmatched rows?

*Tests: a LEFT join keeps every row of the table named first, matched or not.*

- The payments side, so every payment row survives
- The orders side, so an unpaid order stays in  <- correct
- Both sides, so every orphan shows up somewhere
- Neither side, since only the matches come back

---

## Q2. An invented shop: 800 orders LEFT JOIN payments, where 70 orders have two payment rows and every other order has one. How many rows come back?

*Tests: a key that repeats on one side multiplies the other side's rows.*

- 800, since a LEFT join keeps each order once
- 1,600, since the two-payment orders double it all
- 870, one extra row for each two-payment order  <- correct
- 730, since the seventy repeated orders collapse

---

## Q3. Booked against collected, with an INNER join. What happens to the orders nobody paid?

*Tests: an INNER join drops unmatched rows silently, and the gap leaves with them.*

- They drop out, and their gap vanishes with them  <- correct
- They stay in, with zero in the collected column
- They raise an error, since a NULL cannot be summed
- They stay in, with NULL in the collected column

---

## Q4. "Orders LEFT JOIN payments WHERE the payment key IS NULL." What does it list, in Anand's words?

*Tests: the anti-join is the question about rows that found no match.*

- Payments that no order in the book can claim
- Orders with a payment of zero rupees against them
- Orders paid for twice by a gateway that retried
- Orders that were booked and never paid at all  <- correct

---

## Q5. Collected revenue doubled after a join, and every row looks fine. What is the first check?

*Tests: a join is done when its row count is explained.*

- Rows out of the join against orders in  <- correct
- A second quarter, to see whether it doubled too
- The payments table's total, summed on its own
- The largest ten orders, read one at a time

---

## Q6. `GROUP BY order_id HAVING COUNT(*) > 1` on payments. What does it find?

*Tests: the grain decides what a HAVING count is counting.*

- Only the payments a gateway retry posted twice
- Retries mixed with honest two-instalment orders  <- correct
- Only the orders that were paid in two instalments
- The orders with no payment row at all, in full

---

## Q7. The double-paid query filters Q2 orders and keeps instalments posted more than once. Where does each condition go?

*Tests: WHERE filters rows before the groups form, HAVING filters the groups, and a join does not change that (Monday's clause order, one level up).*

- Both in HAVING, since the query has a GROUP BY
- Both in WHERE, since the join runs before either
- The quarter in HAVING, the count in WHERE
- The quarter in WHERE, the count in HAVING  <- correct

---

## Q8. Orders LEFT JOIN payments ON order_id, then `WHERE p.paid_date >= '2026-07-01'`. What happens to the unpaid orders?

*Tests: a condition on the right-hand table in WHERE turns a LEFT join into an INNER one.*

- They stay, since the join was written as a LEFT one
- They vanish, since a NULL date fails the WHERE  <- correct
- They stay, and only the June payments drop out
- They raise an error, since NULL cannot be compared

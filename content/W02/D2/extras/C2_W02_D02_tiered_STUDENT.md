# Which extra should you take tonight: the stretch or the recovery?

Both are optional and neither is graded. Pick the one that matches where you actually are, even when
the other one sounds more appealing.

---

## Stretch: can one query reconcile both sides of the feed at once?

Take this one if you finished the case early and the anti-joins felt easy. The data platform lead
comes back with a second question.

> "Your report explains the orders. I need the other half. Give me one list that shows every order
> with no payment and every payment with no order, side by side, so I can take it to the gateway team
> and to the order system team in one meeting."

Build one query with a FULL OUTER JOIN between orders and payments, at the grain that does not
multiply, which means payments brought to one row per order first. Then split its output into three
labelled groups with a CASE expression:

| Group | How you know a row belongs there |
|---|---|
| Matched | Both the order key and the payment key are present. |
| Order only | The payment side is NULL, so the order was never paid. |
| Payment only | The order side is NULL, so no order can claim the payment. |

Write the reconciliation above the query. Rows out equals matched plus order only plus payment only,
and the payment-only rows, added to the payments matched to Q1 and Q2 orders, account for every row
in `payments`. Write both lines as a comment before you run the query, then prove them with a check
that returns true.

The hard part is the quarter filter. A FULL OUTER JOIN with a quarter filter in WHERE loses the
payment-only rows, because they have no quarter. Decide where the Q2 condition goes, and write one
sentence on why.

Then practise on a second schema, the joins category of PostgreSQL Exercises,
https://pgexercises.com/questions/joins/ (checked 1 Oct 2026). Work the questions in order, and
before running each one, write the row count you expect and the grain of each table in a comment.

You have done it well if your three groups add up to the row count, and your sentence on the quarter
filter names the NULL that WHERE would reject.

---

## Recovery: can you trace the tiny tables again, row by row?

Take this one if the session moved fast, the joins blurred together and you would like to rebuild
them; doing it tonight costs you nothing tomorrow. Every number here is invented.

Open `content/W02/D2/sql/C2_W02_D02_01_what_a_join_keeps_STUDENT.sql` and run it one statement at a
time.

1. Run the setup: two CREATE statements and two INSERTs. Then run `SELECT * FROM tiny_orders;` and
   `SELECT * FROM tiny_payments;` and read both tables aloud: five orders, seven payments.
2. On paper, draw a line from each payment to the order it names. T-2 gets two lines, T-3 gets two
   lines, T-4 gets none, and P-7 points at T-9, which is not there.
3. Count your lines. There are six, and that is the INNER join's row count before you run it. Run the
   INNER join and check that it returns six rows.
4. Now ask what happens to T-4. A LEFT join keeps it, so the answer is six plus one: seven. Ask the
   same about P-7 for the RIGHT join, and about both for the FULL join, and write 7 and 8 before you
   run the four-joins query.
5. Run the trap, the statement started from payments: 4 of the 5 orders and 7,100 of cash against
   5,800 booked. On your drawing, find the order with no line and the payment with no order.
6. Run the last query, the key counts, and check that each key's count in orders times its count in
   payments gives the rows it wrote.

Then open `notebooks/C2_W02_D02_02_why_twice_booked_STUDENT.ipynb` and read its first three levels
only: why Q2's 462 orders become 678 rows, and why the order amount rides every payment row.

By the end you should be able to predict a join's row count from a drawing of the lines between the
two tables, and to see that every number after the join depends on that count being right.

If step 3 surprised you, trace it once more with T-2 alone: one order with two payment lines comes
out as two rows. Chapter 2 is that same fan-out, repeated across Q2's orders.

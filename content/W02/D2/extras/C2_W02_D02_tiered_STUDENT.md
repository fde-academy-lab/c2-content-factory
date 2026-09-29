# Extras: one to stretch, one to recover

Both are optional and neither is graded. Pick the one that matches where you actually are, since the
one that sounds better is rarely the one that helps.

---

## Stretch: reconcile both sides in one query

You finished the case early and the anti-joins felt easy. Then this one is for you.

**The situation.** The data platform lead comes back with a second question.

> "Your report explains the orders. I need the other half. Give me one list that shows every order
> with no payment and every payment with no order, side by side, so I can take it to the gateway team
> and to the order system team in one meeting."

**What to build.** One query with a FULL OUTER JOIN between orders and payments, at the grain that
does not multiply, which means payments brought to one row per order first. Then split its output
into three labelled groups with a CASE expression:

| Group | How you know a row belongs there |
|---|---|
| Matched | Both the order key and the payment key are present. |
| Order only | The payment side is NULL, so the order was never paid. |
| Payment only | The order side is NULL, so no order can claim the payment. |

**The reconciliation, written above it.** Rows out equals matched plus order only plus payment only.
The payment-only rows, added to the payments matched to Q1 and Q2 orders, account for every row in
`payments`. Write both lines as a comment before you run the query, then prove them with a check that
returns true.

**The hard part, and the point.** A FULL OUTER JOIN with a quarter filter in WHERE loses the
payment-only rows, because they have no quarter. Decide where the Q2 condition goes, and write one
sentence on why.

**Then practise on a second schema.** PostgreSQL Exercises, the joins category,
https://pgexercises.com/questions/joins/ (verified 29 Sep 2026). Work the questions in order, and
before running each one, write the row count you expect and the grain of each table in a comment.

**A tell that you have done it well:** your three groups add up to the row count, and your sentence
on the quarter filter names the NULL that WHERE would reject.

---

## Recovery: the tiny tables, traced again

The session moved fast, the joins blurred together, and you would rather rebuild them than pretend.
Then this one is for you, and doing it tonight costs you nothing tomorrow.

**Open `content/W02/D2/sql/C2_W02_D02_01_tiny_tables_STUDENT.sql` and run it one statement at a time.**
Every number here is invented.

1. Run the two CREATE statements and the two INSERTs. Then run `SELECT * FROM tiny_orders;` and
   `SELECT * FROM tiny_payments;` and read both tables aloud: five orders, seven payments.
2. On paper, draw a line from each payment to the order it names. T-2 gets two lines, T-3 gets two
   lines, T-4 gets none, and P-7 points at T-9, which is not there.
3. Count your lines. There are six, and that is the INNER JOIN's row count before you run it. Run
   step 2 of the file and check that it returns six rows.
4. Now ask what happens to T-4. A LEFT JOIN keeps it, so the answer is six plus one: seven. Run step 3
   and find T-4's row with NULLs on the payment side.
5. Ask the same about P-7 for the RIGHT JOIN, and about both for the FULL JOIN. Write 7 and 8 before
   you run steps 4 and 5.
6. Run step 7, the fan-out. It returns 8,500 against 5,800 booked. On your drawing, circle the orders
   with two lines: T-2 adds 2,000 an extra time and T-3 adds 1,500 an extra time, and 5,800 less
   T-4's 800 plus those 3,500 is 8,500.
7. Run step 8, the fix. Five rows, one per order, and T-4 shows a zero after COALESCE.

**What you should end up believing.** A join's row count can be predicted from a drawing of the lines
between the two tables, and every number after the join is only as honest as that count.

**If step 6 surprised you,** trace it once more with T-2 alone: one order, two payment lines, two
rows, and its 2,000 summed twice. That single order is the whole of round 1.

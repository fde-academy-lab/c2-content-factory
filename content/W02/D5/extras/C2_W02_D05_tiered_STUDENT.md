# Tiered extras, Week 2 Friday

Two tasks built in advance: a stretch for anyone who finishes the escalated case early, and a
recovery for anyone the grain lost.

---

## Stretch: the protect list for Q2 alone, and where it disagrees with the two-quarter list

Wednesday's list ranked Retail-Plus members by Q2 revenue in SQL; today's list ranks them across both
quarters from the customer table. The head of Retail-Plus will ask which list to act on.

1. In your workbook, add a column to the raw export that carries `order_amount` only on the first row
   of each order and only when the order falls in Q2.
2. On a new tab, compute each Retail-Plus member's Q2 revenue with `SUMIFS` over that column, and rank
   the members with `COUNTIFS`, breaking ties by id.
3. Put the top fifty by Q2 beside the top fifty across both quarters. Count the members on one list
   and not the other.
4. Look at the fiftieth place on the Q2 list, and say how many rows the list ships if ties rank the
   same.
5. Write two sentences for the head of Retail-Plus: which list answers "who is drifting now", and which
   answers "who has been worth most".

**What you should find.** 76 Retail-Plus members ordered in Q2. Thirty-six members sit on both lists
and fourteen on only one. Check your Q2 total against the warehouse's Retail-Plus Q2 figure, Rs
4,13,380, before you trust the ranking, and apply Wednesday's tie rule at the fiftieth place.

---

## Recovery: the grain, on thirteen rows

If round 1 lost you, start here and do it on paper first.

An invented export from the app channel, one row per payment: seven orders paid once, worth Rs 20,000
together; two orders of Rs 40,000 and Rs 60,000, each paid in two instalments; one order of Rs 2,000
the gateway posted twice. Every row carries its order's amount.

1. Write the rows out: how many does each order occupy? Add them up. You should reach 13 rows for 10
   orders.
2. Add what each row carries. You should reach Rs 2,24,000, which is what a pivot's Sum shows.
3. Cross out only the rows identical to another row in every column. Which one goes? You should keep 12
   rows and Rs 2,22,000.
4. Now keep only the first row of each order. You should reach 10 rows and Rs 1,22,000.
5. Say in one sentence why step 3 did not reach step 4's number.

Then open the companion page, `demos/C2_W02_D05_last_mile_STUDENT.html`, and run experiment A, which
is the same mechanism on five invented rows. Then rerun round 1's unguided set.

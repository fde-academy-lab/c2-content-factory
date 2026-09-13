# Week 2 recap: the fortnight under questioning

Pen and paper. No assistant, no laptop, no notes. About two hours.

Short answers throughout. One or two sentences is the target for most items, and a long answer to
a short question usually means the short answer has not been found yet. Where an item asks for a
number, show the arithmetic beside it.

This is ungraded and it is read carefully. Answer as you would in an interview, in your own words.

---

## Section A. The language

**A1.** `WHERE` and `HAVING` both filter. One sentence each, saying what each one judges and when
it runs.

**A2.** A query has `SELECT sum(amount) AS revenue ... ORDER BY revenue DESC` and it works. The
same alias in `WHERE` fails. Give the single fact that explains both.

**A3.** `SELECT order_id FROM orders LIMIT 5` runs on two machines and returns different rows from
the same unchanged table. Who is wrong, and why?

**A4.** What does `WITH name AS (...)` promise, and what does it not promise?

---

## Section B. Joins

**B1.** `INNER` against `LEFT`: what does each drop and what does each keep? Answer in terms of a
business question rather than in terms of rows.

**B2.** A `LEFT JOIN` from 1,000 orders to payments returned 1,450 rows. Write the four-line
reconciliation: rows before, rows after, the difference, and the therefore.

**B3.** Collected revenue came back at roughly twice the true figure and every individual row in
the result was correct. Explain how both of those can be true at once.

**B4.** 450 orders carried two payment rows each, out of a book of 1,000. Why did that roughly
double the total rather than inflate it by about 45 percent?

**B5.** Write, in words rather than in SQL, how you would find orders that have no payment at all.
Then say what an `INNER` join would have done to that question.

**B6.** Two payment rows sit on the same order. When is that correct and when is it a defect?
What separates the two, and why can a rule not decide it for you?

---

## Section C. Windows

**C1.** Four members with Q2 totals of Rs 9,000, Rs 7,500, Rs 7,500 and Rs 6,200. Give the
sequence returned by `ROW_NUMBER`, by `RANK` and by `DENSE_RANK`.

**C2.** A business owner says: ties must rank the same, and the top fifty must not lose a name to
a tie. Name the function, and say how many rows the report might ship.

**C3.** Give the argument against `ROW_NUMBER` that has nothing to do with fairness.

**C4.** `lag(spend)` on a customer's first month returns nothing. Why is that the correct
behaviour, and what does it do to a flag built on two LAGs?

**C5.** A running total changed between two runs against unchanged data. What was wrong with the
query, and why is that worse than a number that is simply incorrect?

---

## Section D. pandas

**D1.** Split, apply, combine. Which two of the three does `groupby` do for you?

**D2.** A merge returned 346 rows from a 340-row table. Name the argument that would have stopped
it and the error it raises.

**D3.** `validate="many_to_one"` fails on your data. What have you just learned, and about which
of the two tables?

**D4.** You pivot a long frame wide and then melt it back. The result has more rows than you
started with. Why?

---

## Section E. The last mile

**E1.** Two CSVs arrive in the same folder. What do you run before pivoting either, and what
number are you looking for?

**E2.** A pivot total is double what the warehouse says. What did the pivot do wrong?

**E3.** A lookup returns a member for an id that is not in the table. Which part of the formula
caused it, and why is that outcome worse than an error message?

**E4.** Name the three things a front-page number needs beside it, and say what happens when one
is missing.

**E5.** A director changes an input cell and nothing downstream moves. What does that tell you
about the sheet?

---

## Section F. The judgment

**F1.** Same question, three tools. Give the three questions you would ask to decide, and say why
none of them is about syntax.

**F2.** Somebody proposes that Finance's quarter-end number come from a notebook an analyst runs.
Write the refusal in one sentence that does not mention pandas.

**F3.** State the condition that has to hold for anything living in Excel, and say what breaks it
first in a real team under a deadline.

**F4.** Last week you told Meera that Q1 was Rs 2.10 crore. This week the warehouse said
Rs 10.00 crore. Write the sentence you send her.

---

## Section G. The transfer

**G1.** Build 1 opens on Monday in Kalpa Health, a unit you have not seen, with its own
stakeholders and its own data. A director there asks where their growth comes from.

Say in four or five sentences what stays the same in your method and what changes. Be specific
about at least two habits from this fortnight that you would carry across on day one, and name one
thing you would refuse to assume.

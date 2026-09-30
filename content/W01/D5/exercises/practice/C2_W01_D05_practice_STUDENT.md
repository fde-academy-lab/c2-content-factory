# Practice lab: rerun the step where you stalled

Kavya Nair, the morning after a lab: "Tell me which step you stalled on, and show me you can run it
alone on a file you have not seen."

This set runs on the practice export, `data/C2_W01_D05_practice_orders_STUDENT.csv`, with its control
totals in `data/C2_W01_D05_practice_control_STUDENT.csv`. It is a different file from the lab's, with
the week's defects in other places, so nothing from the morning carries across.

**How to run it.** Open a fresh copy of `notebooks/C2_W01_D05_lab_STUDENT.ipynb`, change the two file
names in the first cell to the practice files, and run the week's method again. Start at the step
your TA marked; the four problems below climb from the profile to the note, so start at the problem
that holds your step and carry on from there. About an hour in all.

Answer each item with one letter, in order, and post the letters as one line. The last item of each
problem is a design item: which approach fits, sized how, and what would switch it. Item 16 closes the
set by asking for the order of the method itself.

```
Post one line in this shape: 1x 2x 3x 4x 5x 6x 7x 8x 9x 10x 11x 12x 13x 14x 15x 16x
```

---

## Problem 1: the profile and the decisions (about 15 minutes)

Run the profile and the cleaning pass on the practice export before you answer.

### Item 1

How does your profile tell you whether any rows repeat an order already in the file?

a) Each row is compared with the row directly above it
b) Rows less distinct order ids, a repeat per extra
c) Rows with a Q1 date are counted, then counted again
d) Rows whose amount or customer looks odd are counted

### Item 2

Suppose an amount will not convert to a number, and you can read it without guessing. What goes in the decisions log?

a) Set it to 0 so the quarter still sums, and move on
b) Drop the row, since a value that fails is unusable
c) Read it without guessing, convert, keep and flag it
d) Replace it with the segment's median order, with no note

### Item 3

Suppose an order carries no customer_id, and Anand's analyst will audit the customer count. What do you do?

a) Drop the order, so every remaining row is complete
b) Keep it in revenue, flag it, state customers both ways
c) Count the empty id as one more customer, since it is an order
d) Give it to the Retail-Core customer with the most orders

### Item 4

Kavya asks how you would find repeated orders in this file, and in next month's export of about 5
lakh rows (illustrative). Which approach fits both, sized how?

a) Sort by order id and read down the list, a few minutes on a short file
b) Compare every pair of rows field by field, n times n less one, halved
c) Ask Finance to remove repeated rows before the export is sent
d) Distinct order ids against rows, one cell at either size

---

## Problem 2: the reconciliation (about 10 minutes)

### Item 5

Your pass's order counts land on Finance's control totals in both quarters. What does the count check prove, and what is still open?

a) Every row is accounted for; the rupees are still open
b) The pass is finished, since the orders match to the unit
c) Nothing, because a count check means nothing on its own
d) Every cleaning decision was right, in rows and in rupees

### Item 6

A colleague's Q1 lands on Finance's order count and falls short of its rupee total, with zero rejects reported. Which cause fits all three facts?

a) A repeated row that was kept in the quarter
b) An order dropped without a word in the log
c) An order dated just outside the quarter's end
d) A value that would not convert, set to zero

### Item 7

Next week the practice export arrives with no control totals for Q2. Which check do you still run,
and what does the note then say about Q2?

a) Every value summed or logged; Q2 called unreconciled
b) No check, since a reconciliation needs a total from outside
c) Q2's median order against Q1's, and the note says it held
d) Q1's control total applied to both quarters, as the nearest

---

## Problem 3: the tree and the test (about 20 minutes)

### Item 8

Your tree is built on the clean data. Which branch moved inside Retail-Plus?

a) Customers, since the tier lost members between the quarters
b) Orders per customer, with customers and basket about flat
c) Revenue per order, with customers and frequency flat
d) None of them, since the total held

### Item 9

Kavya asks for Retail-Plus orders per customer, Q1 to Q2, on the clean data. What is the change?

a) -40.0%, counting Q1 rows as they arrived
b) -1.7%, the change in revenue per order
c) -25.0%, counting distinct Q1 orders
d) +33.3%, measured from Q2 back to Q1

### Item 10

A small segment's revenue rose 50 percent on a handful of orders, and Marketing wants budget moved to it. Which approach decides that, sized how?

a) Move the budget now, since its rise is the largest in the file
b) A shuffle test on its few orders this afternoon, fifteen minutes
c) Its count in the caveat, revisited at about 30 orders a quarter
d) Leave it out of the note, since a small segment cannot matter

### Item 11

You test whether Retail-Plus's fall in frequency differs from Retail-Core's by more than chance. What do you shuffle?

a) The orders, one at a time, across the two segments
b) The segment label, across whole customers
c) The quarter label, across every order in the file
d) The amounts, keeping each order's segment fixed

### Item 12

You have fifteen minutes for one shuffle test before the note. Which gap earns it?

a) The smallest segment's large percentage rise, on its few orders
b) The total's small rise, since it rests on every order in the file
c) The branch your tree says moved, shuffled by customer
d) All four segments at once, leading with the smallest p-value

---

## Problem 4: the note (about 15 minutes)

### Item 13

Which claim goes first in the practice note?

a) The branch that moved, in its segment, both ends and its count
b) The total, since it held, so nothing needs attention this quarter
c) The largest percentage fall, as the uncleaned rows first showed it
d) The fastest-growing segment, whatever the count its rate rests on

### Item 14

Marketing pushes on the note: "The tier is tiny. Why should Meera care?" Which answer holds the claim without overclaiming?

a) "You are right, so I will take the tier out of the note before Monday's review."
b) "Its size does not matter, because the p-value settles the question either way."
c) "The members matter less than the total, and the total held all quarter."
d) "Every member is still here, ordering less; the test says if it is chance."

### Item 15

Meera asks what would move Retail-Plus out of your claim and into the caveat. Which fact would?

a) A rerun of the shuffle placing the gap inside chance
b) The total rising again in Q3, so the tier matters less now
c) Student growing faster than Retail-Plus next quarter too
d) Marketing disagreeing with the finding in Monday's review

### Item 16

Next month's export arrives with about 5 lakh rows and no control totals, and Meera wants a first read
in two hours. Which order of your first four moves fits?

a) Decompose, then profile, then one shuffle test, then the note
b) Sum and chart it, then profile, then reconcile what you can
c) Ask Finance for totals, wait for them, then profile and decompose
d) Profile, account for values, ask Finance for totals, decompose

---

## The hands-on part

Write these three numbers from your rerun under your lab note, then check them against the solution:
the rows your pass rejected, Q2 revenue on the clean data, and Retail-Plus's distinct orders in Q2.

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

Answer each item with one letter, in order, and post the letters as one line.

```
Post one line in this shape: 1x 2x 3x 4x 5x 6x 7x 8x 9x 10x 11x
```

---

## Problem 1: the profile and the decisions (about 15 minutes)

Run the profile and the cleaning pass on the practice export before you answer.

### Item 1

Kavya asks how many rows in the practice export repeat an order already in the file. What does your profile say?

a) None, since every row differs from the row above it
b) Four rows: rows less distinct order ids
c) Six rows, counting every row with a Q1 date twice
d) Two rows, the ones whose amount or customer looks wrong

### Item 2

One amount in the practice export will not convert to a number. What goes in the decisions log?

a) Set it to 0 so the quarter still sums, and move on
b) Drop the row, since a value that fails is unusable
c) Read it without guessing, convert, keep and flag it
d) Replace it with the segment's median order, with no note

### Item 3

One Q2 order has no customer_id. Anand's analyst will audit the customer count. What do you do?

a) Drop the order, so every remaining row is complete
b) Keep it in revenue, flag it, state customers both ways
c) Count the empty id as one more customer, since it is an order
d) Give it to the Retail-Core customer with the most orders

---

## Problem 2: the reconciliation (about 10 minutes)

### Item 4

Your pass keeps 75 orders. Finance's control totals list 39 orders in Q1 and 36 in Q2. What does the count check prove, and what is still open?

a) Every row is accounted for; the rupees are still open
b) The pass is finished, since the orders match to the unit
c) Nothing, because a count check means nothing on its own
d) The duplicates were removed correctly, and so was the text amount

### Item 5

A colleague's Q1 comes to Rs 23,18,740 against a control total of Rs 23,21,000, with zero rejects reported. Which row explains the Rs 2,260?

a) A duplicated Retail-Plus row that was kept
b) The order with no customer_id, dropped silently
c) A Business order that fell outside the quarter
d) The amount that would not convert, set to zero

---

## Problem 3: the tree and the test (about 20 minutes)

### Item 6

Total revenue barely moves from Q1 to Q2. Which branch moved inside Retail-Plus?

a) Customers, since the tier lost members between the quarters
b) Orders per customer, with customers and basket about flat
c) Revenue per order, with customers and frequency flat
d) None of them, since the total held

### Item 7

Kavya asks for Retail-Plus orders per customer, Q1 to Q2, on the clean data. What is the change?

a) -40.0%, on all 20 Q1 rows as they arrived
b) -1.7%, the change in revenue per order
c) -25.0%, on 16 distinct Q1 orders
d) +33.3%, measured from Q2 back to Q1 by mistake

### Item 8

Student revenue rises 50 percent from Q1 to Q2. How does it enter the note?

a) As the headline, since it is the largest rise in the file
b) As the action, moving budget to Student next quarter
c) Left out, since a small segment does not matter
d) In the caveat, with its count of two orders then three

### Item 9

You test whether Retail-Plus's fall in frequency differs from Retail-Core's by more than chance. What do you shuffle?

a) The orders, one at a time, across the two segments
b) The segment label, across whole customers
c) The quarter label, across every order in the file
d) The amounts, keeping each order's segment fixed

---

## Problem 4: the note (about 15 minutes)

### Item 10

Which claim goes first in the practice note?

a) Retail-Plus orders per customer fell 25%, 2.00 to 1.50, members flat
b) Revenue held flat, up 0.8%, so nothing needs attention this quarter now
c) Retail-Plus collapsed 40%, and the tier needs a rescue plan before Diwali
d) Student grew 50%, the fastest segment in the file, so it deserves budget

### Item 11

Marketing pushes on the note: "Eight members is nothing. Why should Meera care?" Which answer holds the claim without overclaiming?

a) "You are right, so I will take Retail-Plus out of the note before Monday's review."
b) "Eight is plenty, because the p-value settles the question either way."
c) "The members matter less than the total, and the total held all quarter."
d) "Eight members, all still here, ordering less; the test says if it is chance."

---

## The hands-on part

Write these three numbers from your rerun under your lab note, then check them against the solution:
the rows your pass rejected, Q2 revenue on the clean data, and Retail-Plus orders per customer in Q2.

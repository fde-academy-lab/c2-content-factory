# Can you rerun the step where you stalled, alone, on a file you have not seen?

Kavya Nair, the data team's senior analyst, as the practice lab opens after Friday's sessions: "Tell
me which step you stalled on in this morning's lab, and show me you can run it alone on a file you
have not seen."

**Who needs the answer.** You and your TA need it first: your TA's observation sheet from the lab
noted one step as the one you do not own yet. Meera Raghavan, Kalpa Retail's CEO, needs it on Monday
at her growth review, the meeting that decides where the next quarter's effort goes, with Marketing
and its Rs 12 crore request to win new customers in the room. The note she hears there should come
from someone who can run every step alone, and Anand Iyer, Kalpa Retail's finance controller, reads
every number in it against his books before she does.

**The questions on the way.**

1. What does a new export hold, and what do you decide about each defect?
2. Does the clean data still match Finance's books?
3. Which branch moved, and could chance alone have moved it?
4. What does the note say, and does it hold against a push?

This set runs on the practice export, `data/C2_W01_D05_practice_orders_STUDENT.csv`, with its control
totals in `data/C2_W01_D05_practice_control_STUDENT.csv`. It is a different file from the lab's, with
the week's defects in other places, so nothing from the morning carries across. Items that need
figures the practice export does not hold are set on other exports, and those figures are
illustrative.

Kalpa's segments are Retail-Core, Retail-Plus (the paid members' tier, whose customers are its
members), Student and Business (the corporate book). A control total is the source system's own count
of orders and sum of rupees for a quarter. The revenue tree splits a segment's revenue into three
branches, customers times orders per customer times revenue per order (the basket), and the branch
that moved is the one whose change carries most of the segment's change between the quarters. A shuffle test reassigns a label, such as the
quarter or the segment, at random many times and counts how often chance alone gives a change at
least as large as the real one; that share is the p-value, and 0.05 is the usual bar below which a
change is called more than chance. The week's rule of thumb for a rate: one that rests on fewer than
about thirty orders a quarter is watched until more orders arrive, since it has too few behind it to
lead a note.

To run it, open a fresh copy of `notebooks/C2_W01_D05_lab_STUDENT.ipynb`, change the two file names in
its first code cell to the practice files, and run the week's six steps again: profile, clean with a
decisions log, reconcile, decompose along the revenue tree, test the lead against chance, and write
the note. Start at the problem that holds the step your TA noted and carry on from there; the four
problems climb from the profile to the note, and the set takes about an hour in all.

Answer each item with one letter, in order, and post the letters as one line. Nine of the sixteen
items, the last of each problem among them, are design items: they ask which approach fits, sized
how, and what would switch it.

```
Post one line in this shape: 1x 2x 3x 4x 5x 6x 7x 8x 9x 10x 11x 12x 13x 14x 15x 16x
```

---

## Problem 1: What does a new export hold, and what do you decide about each defect?

At work, this is the first half hour with any extract. The cleaning pass writes a decisions log, one
line per decision with the order id, the decision and the reason, and that log is what an auditor
reads months later. Run the profile and the cleaning pass on the practice export before you start.

### Item 1: What did last month's profile find?

Last month's export profiled like this before any change. Present counts the rows that hold a value in
the field, Convertible counts the values that read as a number (asked only of a field that holds
numbers), and Distinct counts the different values.

| Field | Present | Convertible | Distinct |
|---|---|---|---|
| order_id | 1,240 | | 1,223 |
| customer_id | 1,238 | | 402 |
| amount | 1,240 | 1,236 | 911 |
| segment | 1,240 | | 5 |

Which reading names every finding in it?

a) 17 repeat rows; 2 orders with no customer; 4 amounts that will not convert; a fifth segment
b) 17 repeat rows and 4 amounts that will not convert; every other count is what it should be
c) 1,223 orders from 402 customers at 911 prices in five segments, so the file is clean
d) 17 repeat rows; 2 customers who appear twice; 4 amounts stored as zero; one segment left empty

### Item 2: What do you do with three values that will not convert?

Three values on another export would not convert.

| Value | What else the file says |
|---|---|
| "4.5k" | the supplier's other amounts are whole rupees |
| "TBC" | the delivery note shows the goods shipped |
| "TEST" | the customer_id is the QA team's test account |

Which decisions fit, in the order the values are listed?

a) read as 4,500 and flag; set to zero; drop with a reason
b) hold and ask the owner; hold and ask the owner; drop with a reason
c) read as 4,500 and flag; hold and ask the owner; drop with a reason
d) read as 4,500 and flag; hold and ask the owner; set to zero

### Item 3: Which way finds repeated rows in 5 lakh rows?

Next month's export will be about 5 lakh rows. One way to find rows that repeat an order compares
every pair of rows, n(n - 1)/2 comparisons; another counts each order id in one pass and lists the
ids seen more than once. What does the pair-by-pair way cost at 5 lakh rows, and which way fits
both last month's 1,240 rows and next month's 5 lakh?

a) About 2.5 lakh comparisons, so the pair-by-pair way is fine at either size
b) About 125 billion comparisons, so the one-pass count
c) About 125 billion comparisons, so pairs on a faster machine overnight
d) About 5 lakh comparisons, so either way, since they cost the same

### Item 4: How do 6 orders marked "UNKNOWN" enter the note?

On another team's export, 6 of 1,000 orders carry the customer_id "UNKNOWN", and the file has 400
known customers. Anand's analyst audits the customer count and Meera reads revenue per customer.
Which handling fits, with the counts the note gives?

a) Count "UNKNOWN" as one more customer and give 401, since every order has a buyer
b) Drop the 6 orders so every row is complete, and give 400 customers on 994 orders
c) Give each of the 6 to the busiest customer in its segment, and give 400 customers
d) Keep the 6 in revenue, flagged; 400 customers plus 6 orders with no known buyer

---

## Problem 2: Does the clean data still match Finance's books?

At work, this is the check Finance asks for before it acts on any number an analyst sends.

### Item 5: What went wrong in a colleague's pass, and what did it send?

On a second two-quarter export, Finance's control totals are Q1 Rs 30,00,000 on 410 orders and Q2 Rs
27,00,000 on 395 orders. A colleague's pass summed Q1 Rs 28,20,000 on 410 rows and Q2 Rs 29,40,000
on 403 rows. What went wrong, and what headline did the pass send?

a) A Q1 value lost, Rs 1,80,000; 8 extra Q2 rows, Rs 2,40,000; it sent -10.0 percent
b) 8 extra Q1 rows, Rs 1,80,000; a Q2 value lost, Rs 2,40,000; it sent +4.3 percent
c) A Q1 value lost, Rs 2,40,000; 8 extra Q2 rows, Rs 1,80,000; it sent +4.3 percent
d) A Q1 value lost, Rs 1,80,000; 8 extra Q2 rows, Rs 2,40,000; it sent +4.3 percent

### Item 6: Where does a gap sit when only the file can tell you?

On a third two-quarter export the count check passes: input 2,480 equals kept 2,431 plus set aside 49,
and every order count matches Finance's. The rupee check shows Q1 Rs 14,600 short, and the decisions
log holds no conversion lines; a conversion line records a value the pass read as a number other than
the one the file stored. A second route reaches the same answer by a method independent of the first,
so a wrong step in the first shows up as a disagreement. Which second route finds where the gap sits
using only the file, and what should it show?

a) The 49 rows set aside, summed; they should come to Rs 14,600
b) A shuffle test on Q1's orders; its p-value should fall under 0.05
c) Every value, summed or logged; one is in neither, about Rs 14,600
d) Each quarter's median order; Q1's should sit about Rs 14,600 lower

### Item 7: What does a note say about a quarter with no control total?

Next week's export arrives with no control totals for Q2, and every check you can run inside the file
passes. What does the note say about Q2?

a) Q2 is reconciled, since every check inside the file passed
b) Q2 is unreconciled, and the checks that ran inside the file are named
c) Q2 is unreconciled, and no check is named, since none can run without Finance
d) Q2 is reconciled to Q1's control total, scaled by Q2's order count

### Item 8: In what order do the moves fit a two-hour read?

Meera wants a first read on next month's export in 120 minutes, and it came with no control totals.
You have four moves: profile (20 minutes), account for every value (10), decompose along the revenue
tree (25), and ask Finance for control totals, whose reply takes 90 minutes. The reply must land at
least 15 minutes before the read. Which order meets that?

a) Profile, account for every value, ask Finance, decompose
b) Profile, decompose, ask Finance, account for every value
c) Ask Finance, profile, account for every value, decompose
d) Profile, ask Finance, decompose, account for every value

---

## Problem 3: Which branch moved, and could chance alone have moved it?

At work, this is the call on which branch a CEO opens first, and whether it survives Marketing's
first question.

### Item 9: Which branch carries Retail-Plus's change?

On your revenue tree for the clean practice data, which branch carries most of Retail-Plus's change
between the quarters, and by how much did it move?

a) Orders per member, down 25.0 percent
b) Customers, down 25.0 percent
c) Revenue per order, down 1.7 percent
d) Orders per member, down 40.0 percent

### Item 10: Which tests fit Meera's two questions about Retail-Plus?

Meera asks two questions about the change your tree found inside Retail-Plus. First, could chance
alone have made that change among the tier's own members, from Q1 to Q2? Second, did Retail-Plus's
change differ from Retail-Core's, whose customers are other people? To flip a member is to swap that
member's two quarters, so everything they bought in Q1 counts as Q2 and everything they bought in Q2
counts as Q1. Which tests fit, in that order?

a) Flip each member's own two quarters; shuffle the segment label across whole customers
b) Shuffle the segment label across whole customers; flip each member's own two quarters
c) Deal the quarter label across every Retail-Plus order; shuffle the label across single orders
d) Flip each member's own two quarters; shuffle the segment label across single orders

### Item 11: In how many of the 256 ways to flip Retail-Plus's members is the change at least as large as the real one?

A colleague runs one of item 10's candidate tests, the flip, on your clean data. Take each Retail-Plus
member's two quarters on the branch your tree found. The tier has 8 members, so there are 256 ways to
flip some and keep the rest. In how many is the tier's change at least as large as the real one,
either way, and what is p?

a) 16 of 256, p = 0.0625
b) 32 of 256, p = 0.125
c) 2 of 256, p = 0.008
d) 128 of 256, p = 0.5

### Item 12: What would change the verdict that item 11's count gives?

Item 11's count gives a verdict on the Retail-Plus change. What would change that verdict?

a) 20,000 random flips on today's orders in place of the 256 counted
b) A rerun of today's test with another seed
c) Another quarter of orders in which the fall reverses, tested again
d) Another quarter of orders showing the same fall, tested again

---

## Problem 4: What does the note say, and does it hold against a push?

At work, this is the one page a CEO reads in two minutes, said aloud to a room that disagrees. The
note to Meera runs in four parts, claim, evidence, caveat and action, and she acts on its first line.

### Item 13: Which first line fits the practice note?

Which of these first lines fits the note you write on the practice export?

a) "Retail-Plus fell furthest of the consumer segments, so the tier needs a retention plan now."
b) "Student revenue rose 50 percent, the fastest-growing segment this quarter."
c) "Revenue held, up 0.8 percent and reconciled; no segment moved on enough orders to lead."
d) "Revenue held, up 0.8 percent, so nothing in this quarter needs any attention."

### Item 14: Which answer holds a lead when Marketing says it could be chance?

Last quarter's note, on another export, led with one segment's basket: revenue per order down 8
percent, on 62 orders then 57 from 33 customers, and the test put a change that large, either way, at
1 time in 100. In that review Marketing pushed: "That fall could be chance. Why lead with it?" Which
answer holds the note without overclaiming?

a) "Fair point; I will move it down to the caveat before the note goes out."
b) "It is 62 orders, then 57, from 33 customers, and chance does that 1 time in 100."
c) "It is 99 percent certain, since chance alone makes a fall that large only 1 time in 100."
d) "Marketing wants its budget, so its doubt about chance can be set to one side."

### Item 15: Which line of a colleague's cleaning cell lets the pass look clean?

A colleague's cleaning cell for last month's export is below. One line lets the pass look clean
while it is short in rupees.

```python
kept, total = {}, 0                      # line 1
for r in rows:
    if r["order_id"] in kept:            # line 3
        continue
    try:
        amount = int(r["amount"])        # line 6
    except ValueError:
        amount = 0                       # line 8
    kept[r["order_id"]] = amount
    total += amount                      # line 10
```

Which line is it?

a) Line 1, since the total starts at zero before any order is read
b) Line 3, since it skips a row whose order id is already kept
c) Line 6, since int() fails on a value it cannot read
d) Line 8, where an unread value turns into zero with no log

### Item 16: How much does a p-value of 0.048 wobble at 2,000 shuffles?

Last month's test on a lead came out at p = 0.048 on 2,000 shuffles. The share's own wobble at 2,000
shuffles is about the square root of p(1 - p)/2,000. What is the wobble, and what do you do before
calling the lead real?

a) About 0.005, so run 20,000 shuffles before calling it
b) About 0.0001, so call it real now, since 0.048 is under 0.05
c) About 0.05, so no number of shuffles can ever settle it
d) About 0.005, so call it real now, since 0.048 is under 0.05

---

## Which three numbers does your rerun reach?

Write these three numbers from your rerun under your practice note, then check them against the
solution: Q1 revenue and Q2 revenue on the clean data, and Retail-Plus's distinct orders in Q2.

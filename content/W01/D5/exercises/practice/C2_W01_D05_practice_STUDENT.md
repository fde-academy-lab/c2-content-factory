# Can you rerun the step where you stalled, alone, on a file you have not seen?

Kavya Nair, the morning after a lab: "Tell me which step you stalled on, and show me you can run it
alone on a file you have not seen."

**Who needs the answer.** You and your TA need it. The observation sheet marked one step of your lab
as the one you do not own yet, and Monday's growth review hears a note from someone who can run every
step alone.

**The questions on the way.**

1. What does a new export hold, and what do you decide about each defect?
2. Does the clean data still match Finance's books?
3. Which branch moved, and could chance alone have moved it?
4. What does the note say, and does it hold against a push?

This set runs on the practice export, `data/C2_W01_D05_practice_orders_STUDENT.csv`, with its control
totals in `data/C2_W01_D05_practice_control_STUDENT.csv`. It is a different file from the lab's, with
the week's defects in other places, so nothing from the morning carries across. Items that need
figures the practice export does not hold are set on other exports, and those figures are
illustrative. Kalpa's segments are Retail-Core, Retail-Plus (the paid members' tier), Student and
Business (the corporate book); a control total is the source system's own count of orders and sum of
rupees for a quarter.

To run it, open a fresh copy of `notebooks/C2_W01_D05_lab_STUDENT.ipynb`, change the two file names
in the first cell to the practice files, and run the week's method again. Start at the problem that
holds the step your TA marked and carry on from there; the four problems climb from the profile to
the note, and the set takes about an hour in all.

Answer each item with one letter, in order, and post the letters as one line. Nine of the sixteen
items, the last of each problem among them, are design items: they ask which approach fits, sized
how, and what would switch it.

```
Post one line in this shape: 1x 2x 3x 4x 5x 6x 7x 8x 9x 10x 11x 12x 13x 14x 15x 16x
```

---

## Problem 1: What does a new export hold, and what do you decide about each defect?

At work, this is the first half hour with any extract, and the log an auditor reads months later.
Run the profile and the cleaning pass on the practice export before you start.

### Item 1: What did last month's profile find?

Last month's export profiled like this before any change.

| Field | Present | Convertible | Distinct |
|---|---|---|---|
| order_id | 1,240 | | 1,226 |
| customer_id | 1,238 | | 402 |
| amount | 1,240 | 1,236 | 911 |
| segment | 1,240 | | 5 |

Which reading names every finding in it?

a) 14 repeat rows; 2 orders with no customer; 4 amounts that will not convert; a fifth segment
b) 14 repeat rows and 4 amounts that will not convert; every other count is what it should be
c) 1,226 orders from 402 customers at 911 prices in five segments, so the file is clean
d) 14 repeat rows; 2 customers who appear twice; 4 amounts stored as zero; one segment left empty

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

### Item 4: How do you count orders that have no known buyer?

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

On a third two-quarter export the count check passes: input 2,480 equals kept 2,431 plus set aside 49, and
every order count matches Finance's. The rupee check shows Q1 Rs 14,600 short, and the decisions log
holds no conversion lines. Which second route finds where the gap sits using only the file, and what
should it show?

a) The 49 rows set aside, summed; they should come to Rs 14,600
b) A shuffle test on Q1's orders; its p-value should fall under 0.05
c) Every value, summed or logged; one is in neither, about Rs 14,600
d) Each quarter's median order; Q1's should sit about Rs 14,600 lower

### Item 7: What does a note say about a quarter with no control total?

Next week's export arrives with no control totals for Q2. Your ids-against-rows check and your
every-value-accounted check both pass. What does the note say about Q2?

a) Q2 is reconciled, since the file accounts for every row and value
b) Q2 is unreconciled, and the two checks that did run are named
c) Q2 is unreconciled, and no check is named, since none can run without Finance
d) Q2 is reconciled to Q1's control total, scaled by Q2's order count

### Item 8: In what order do the moves fit a two-hour read?

Meera wants a first read on next month's export in 120 minutes, and it came with no control totals.
You have four moves: profile (20 minutes), account for every value (10), decompose (25), and ask
Finance for control totals, whose reply takes 90 minutes. The reply must land at least 15 minutes
before the read so you can reconcile to it. Which order meets that?

a) Profile, account for every value, ask Finance, decompose
b) Profile, decompose, ask Finance, account for every value
c) Ask Finance, profile, account for every value, decompose
d) Profile, ask Finance, decompose, account for every value

---

## Problem 3: Which branch moved, and could chance alone have moved it?

At work, this is the call on which branch a CEO opens first, and whether it survives Marketing's
first question.

### Item 9: Which branch moved inside Retail-Plus?

On your tree for the clean practice data, which branch moved inside Retail-Plus, and by how much?

a) Orders per member, down 25.0 percent
b) Customers, down 25.0 percent
c) Revenue per order, down 1.7 percent
d) Orders per member, down 40.0 percent

### Item 10: Which tests fit Meera's two questions?

Meera asks two questions about Retail-Plus in the practice export: first, did its 8 members order
less often in Q2 than in Q1; second, did its change differ from Retail-Core's? Which tests fit, in
that order?

a) Flip each member's own two quarters; shuffle the segment label across whole customers
b) Shuffle the segment label across whole customers; flip each member's own two quarters
c) Deal the quarter label across every Retail-Plus order; shuffle the label across single orders
d) Flip each member's own two quarters; shuffle the segment label across single orders

### Item 11: In how many of the 256 flips is the change at least as large as the real one?

For the first question, tally each member's orders in the two quarters from your clean data. A flip
swaps one member's two quarters, and there are 256 ways to flip the 8. In how many is the total change
in orders at least as large as the real one, either way, and what is p?

a) 16 of 256, p = 0.0625
b) 32 of 256, p = 0.125
c) 2 of 256, p = 0.008
d) 128 of 256, p = 0.5

### Item 12: What would change the flip test's verdict on Retail-Plus?

Item 11's flip test answers Meera's first question, whether Retail-Plus's 8 members ordered less
often in Q2 than in Q1. What would change the verdict it gives?

a) 20,000 flips on today's orders in place of 2,000
b) A rerun of today's test with another seed
c) The fall restated as orders per member instead of a percentage
d) The same fall next quarter on the same members, tested again

---

## Problem 4: What does the note say, and does it hold against a push?

At work, this is the one page a CEO reads in two minutes, said aloud to a room that disagrees.

### Item 13: Which first line fits the practice note?

Which of these first lines fits the note you write on the practice export?

a) "Retail-Plus members ordered 25 percent less often, so the tier needs a retention plan now."
b) "Student revenue rose 50 percent, the fastest-growing segment this quarter."
c) "Revenue held, up 0.8 percent and reconciled; no segment moved on enough orders to lead."
d) "Revenue held, up 0.8 percent, so nothing in this quarter needs any attention."

### Item 14: Which answer holds the note against Marketing?

Marketing pushes on the practice note: "Retail-Plus fell 25 percent. Why is that not your headline?"
Which answer holds the note without overclaiming?

a) "You are right, so I will make the tier the first line before Monday's review."
b) "It is 16 orders then 12 from 8 members, and chance does that 1 time in 8."
c) "It is noise: the test came out above 0.05, so the fall did not happen."
d) "A 25 percent fall on a tier this small cannot matter to anyone at Kalpa."

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

Write these three numbers from your rerun under your lab note, then check them against the solution:
the rows your pass rejected, Q2 revenue on the clean data, and Retail-Plus's distinct orders in Q2.

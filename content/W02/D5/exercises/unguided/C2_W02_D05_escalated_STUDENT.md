# Can you build Monday's file alone in fifty minutes and say, part by part, what the chief of staff can trust it for?

The escalated case: fifty minutes, alone, straight after chapter 6. You work in
`notebooks/C2_W02_D05_ex1_escalated_case_STUDENT.ipynb`, which loads the day's two exports and the
warehouse, asks for ten lettered choices in five parts with a check after each part, and ends on two
sentences to the chief of staff.

> "Build me the file I open on Monday: the tree by segment for both quarters, the protect list with
> the lookup, and the front-page number with its trend. I will change things in the room. Tell me
> what I can trust it for."
>
> Meera's chief of staff, Kalpa Retail

Meera Raghavan, Kalpa Retail's CEO, runs Monday's growth review, and her chief of staff opens one file
in front of her and the directors. Kalpa sells to four segments: Retail-Core, its everyday shoppers;
Retail-Plus, its paid membership tier; Business, corporate buyers invoiced in large amounts; and
Student. Revenue is booked order value in rupees. Q1 runs from April to June 2026 and Q2 from July to
September 2026, and the warehouse, the Postgres database that holds one row per order and is the
source of truth, books 538 orders and Rs 10,00,00,000 in Q1 and 462 orders and Rs 9,84,00,000 in Q2.
Those two pairs are Finance's control totals.

You have two exports. The customer table holds one row per customer who ordered between April and
September, with that customer's segment, city, orders and revenue added up over the half-year. The
raw export holds one row per payment, with the order's amount repeated on every row of that order, so
an order paid in two instalments, or posted twice by the payment gateway, sits on two rows. The
revenue tree splits revenue into customers, orders per customer and revenue per order. The protect
list is the fifty Retail-Plus members with the highest revenue, and the lookup finds a member by id.
C-0195 is a Retail-Plus member who placed no orders in the two quarters, so it has no row in the
customer table. The front-page card prints its number with its period, its comparison and its base,
and measures a change on the earlier quarter. A release note says which parts ship on Monday and
which are held, and why.

**Who needs the answer.** The chief of staff opens this file in front of Meera and her directors on
Monday. A number that does not tie, a lookup that answers with somebody else's row, or a card without
its period goes into the meeting's decisions, and the release note is what tells the chief of staff
which parts to rely on.

**The questions on the way.**

- Does your tree for both quarters tie to the warehouse to the rupee?
- Does your protect list hold the right fifty, and does your lookup say when an id is missing?
- Does your front-page card carry its period, its comparison and its base for any scope a director picks?
- What ships on Monday, and what, if anything, is held?
- Do your numbers agree when reached a second way?

## Part 1. Does your tree for both quarters tie to the warehouse to the rupee?

Used at work on every tree a director sees, which has to reproduce the number Finance owns before
anyone slices it.

Ten minutes, the notebook's markers 1 and 2: which line leaves one row per order, and how customers
are counted in each segment and quarter. The checks after the part compare your quarters with
Finance's control totals, orders and rupees, and your Retail-Plus customer counts with the warehouse's.

## Part 2. Does your protect list hold the right fifty, and does your lookup say when an id is missing?

Used at work wherever a list a manager acts on, or a lookup a director types into, is read aloud in a
room where nobody sees the formula.

Ten minutes, markers 3 and 4: which line gives the fifty Retail-Plus members with the highest revenue,
and which lookup returns a member's revenue or a sentence when the id is not in the table. The checks
test your list and your lookup on C-0152, a member who is there, and on C-0195.

## Part 3. Does your front-page card carry its period, its comparison and its base for any scope a director picks?

Used at work on every front page read in two minutes by people who read nothing else.

Ten minutes, markers 5 and 6: which formula is the change from Q1 to Q2, and which share goes beside
the number. The card's scope, all segments, all except Business, or Retail-Plus alone, is the input
a director changes, and the checks compare your Retail-Plus change and your shares with chapter 4's
figures, which the warehouse reproduced.

## Part 4. What ships on Monday, and what, if anything, is held?

Used at work in every release note that tells a stakeholder what to rely on and what waits.

Ten minutes, markers 7 and 8: which comparison says whether the protect list's source table ties,
and which rule turns any set of checks into Monday's release. Part 1 checked the tree; the protect
list was built from the customer table, a different export. The checks compare your source verdict with
the warehouse's count of customers who ordered, and run your rule on three invented sets of checks.

## Part 5. Do your numbers agree when reached a second way?

Used at work on every number that matters, which is reached twice by routes that could disagree.

Ten minutes, markers 9 and 10: which total is what the foot of the list shows when a director filters
it to Mumbai, and which query is the warehouse's own route to the two quarters of booked revenue.
The checks compare your foot with the warehouse's revenue for the list's Mumbai members, and your
query's two quarters with your tree's.

## Which rules does the escalated case keep, from the files it reads to what the release says?

- The data is the day's two exports in `data/` and the warehouse; nothing in them is to be edited.
- Every check reads what your lines computed, so a letter that passes the check has done the work.
- The release says, for each part, whether it ships, and why a held part waits.
- If you finish early, build the same five parts in a workbook: every number a formula over the two
  exports pasted in as values, the inputs in yellow cells, and a Checks tab that reads PASS or HOLD.
- The support TA answers environment problems only.

## How do you post your ten letters and your two sentences?

One line of ten letters in the order of the notebook's markers, then two sentences to the chief of
staff pasted below it: what Monday's file can be relied on for, and anything held, with its reason.

```
Post exactly this shape: xxxxxxxxxx
```

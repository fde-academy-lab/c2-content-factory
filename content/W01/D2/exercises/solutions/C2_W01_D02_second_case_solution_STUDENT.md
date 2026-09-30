# Solution: Marketing's new deck says members spend 7 percent more per order and the web fell hardest: does either claim hold, and whom does the tier call first?

Answers: 1d 2b 3c 4a

The executed notebook is `solutions/C2_W01_D02_ex2_second_case_solution_STUDENT.ipynb`, and its
lettered TODOs run a c b d. Three of the four items are design items: 1, 2 and 4.

The marketing lead's new deck says Retail-Plus members, Kalpa Retail's paid membership tier, spend 7
percent more per order, so the tier is healthy and the answer is still acquisition, and that the
tier's web orders fell hardest, 24 to 9, so the website is to blame. The head of Retail-Plus asks
which members to call first. The tier's same 22 members placed 51 orders in Q1 and 26 in Q2, in
booked revenue, every order placed before any cancellation or return.

## What does the second case test?

Find what a number is made of before agreeing or disagreeing with it. Marketing's 7 percent is one
leaf of the tier's tree, and the leaves multiply to a tier whose revenue fell about 45 percent. The
website claim fails on a segment that uses the same website, and the tier's call list comes from
orders per member, Q1 against Q2.

## Part 1. Does 7 percent more per order make the tier healthy?

### Q1. What does the tier's own tree say to Marketing's 7 percent? (Design)

The tier's leaves are put back together, members times orders per member times revenue per order.

The key is d, "The same 22 members ordered half as often, so tier revenue fell about 45 percent".
Members held at 22, orders per member fell to 0.510 of Q1 and revenue per order rose to 1.070 of it,
and 1.000 times 0.510 times 1.070 is about 0.55. Counted directly, Rs 1,43,550 to Rs 78,300 is 0.545,
about 45 percent down.

- a, "The tier is healthy, since 7 percent more per order outweighs the fall in orders": one leaf
  that rose inside a tier whose orders halved says nothing of its health.
- b, "Tier revenue fell about 42 percent, orders down 49 and value up 7, so it is minor": it adds
  minus 49 and plus 7 as if percentages added, Monday's two lifts turned round.
- c, "New, richer members joined, so acquisition is already working inside the tier": the members
  are the same 22 in both quarters, as chapter 5's overlap of ids showed.

## Part 2. Is the web's fall the website's fault?

### Q2. Which number tests a fault across the whole website? (Design)

Marketing blames the website for the tier's web orders falling from 24 to 9.

The key is b, "Retail-Core web orders on the same website, which held at 13 and 12". A broken
website hurts everyone who uses it, so a comparison segment on the same website is the test, and
Retail-Core's web orders held.

- a, "Retail-Plus app orders, 13 to 8, since the app shares the website's servers": the app is a
  different channel, and it fell too.
- c, "Retail-Plus web orders by month, to see when the members' fall began": timing says when the
  members' fall began and nothing about whether a fault hit everyone on the site.
- d, "The total of all web orders, 44 to 30, since it covers every segment": the total mixes the
  members' fall into everyone else's orders.

## Part 3. Which members does the tier call first?

### Q3. Which of four member lists does the head of Retail-Plus call first?

The head of Retail-Plus asks which of his members to call first.

The key is c, "The 7 who fell from three orders to one, since they slowed most". Seven members fell
from three orders a quarter to one, the largest drop per member, and eleven more fell by one order.

- a, "Members with no order in Q2, since they have stopped altogether": every member ordered in Q2,
  so the list is empty.
- b, "Members who ordered once in Q1, since they are the least attached": they had the least to lose.
- d, "The 11 who fell by one order, since they are the largest group that slowed": the seven carry
  14 of the 25 lost orders against the eleven's 11, so the larger group is the smaller loss.

## Part 4. Which one request goes first?

### Q4. Which request goes first, with the button capped at about 4 of 25 lost orders? (Design)

The tier lost 25 orders between the quarters, and chapter 6 capped the reorder button at about 4 of
them.

The key is a, "The tier's July change log, renewals and support tickets". Most of the 25 lost orders
fall outside the button's ceiling, and the fall began in July, before the break, so the tier's July
change log tests the cause behind the larger part.

- b, "The app's reorder logs by week since the 25 August release": it tests the smaller part, after
  the break, and it is the second request.
- c, "Marketing's new-member sign-ups by month from July": it measures acquisition, which the overlap
  of ids ruled out.
- d, "This export again, cut by city, channel and week from July": the export raised the question
  and cannot test a cause, whatever month it starts from.

# Which answers hold in the drill on a four-stage funnel at an invented bakery app, and why?

Answers: 1a 2c 3b 4d

The drill read one invented week of Kaapi and Co.'s ordering app. Search to product view reads 120
percent per session because the home page's banner opens products without a search, so the step
divides two counts of different sessions. The search team's question is answered among the sessions
that searched. Product view to cart reads 33 percent per session and 58 percent per customer, both
true. A fall that the shop's billing system does not see is a fall in the counting.

**Who needs the answer.** You, to check your four letters. The product lead spends one engineer's
two weeks on whichever step the room says loses customers.

**The questions on the way.**

- What does the drill test?
- Why is each key right, and each other letter wrong?
- Which item is worth arguing about?
- Where does the pattern live at work?

## What does the drill test?

It tests the three ways a funnel step misleads: a step people can skip, two units on one chart, and a
change in the log mistaken for a change in behaviour. Each is a SECTION 7 check moved to a new shop.

## Why is each key right, and each other letter wrong?

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| Q1, the step above 100 percent | a | 6,000 sessions viewed a product and 5,000 searched, because the banner reaches products with no search | b is low and normal for browsing, never above 100; c is 60 percent; d cannot be, since a session counts once at a stage, no matter how many products it views |
| Q2, the search team's rate | c | Among the sessions that searched, the share that went on to a product is one count over a count of the same sessions | a is the 120 percent artefact itself; b turns the step upside down; d divides by sessions that never searched |
| Q3, the step counted in customers | b | 1,400 of the 2,400 customers who viewed a product added to a cart, 58 percent | a assumes the unit changes nothing; c divides by customers who searched, the step before the step before; d puts customers over sessions, two units in one rate |
| Q4, counting or ordering | d | If the billing system's paid orders held while the app's order events fell, customers kept paying and only the log changed | a, b and c each place the fall in time, on a platform or at one step, and a fault in the log that shipped with the update would sit in the same place, so none of them tells counting from ordering |

## Which item is worth arguing about?

Q4's option c. A fall that sits in one step of the payment sounds like a counting problem, since a
renamed event often breaks exactly one step. It is better evidence of a real change, though: starting
payment still logs normally, so the log works, and the customers who started paying stopped
somewhere inside. The only evidence that clears customers entirely is a second record of the same
orders, kept by a system the update did not touch, that did not fall.

## Where does the pattern live at work?

Every product release review asks these three questions in this order: can people skip the step, is
the chart in sessions or in people, and does an independent record agree. Zomato Gold's Android
checkout in SECTION 7 passed all three: nobody skips the last step of a checkout, the rates were per
session throughout, and the order records in `member_months` count the same 27,212 September orders
as the event log, so no orders went missing from the count after the release.

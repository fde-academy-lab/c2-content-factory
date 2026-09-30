# Solution: chapter 2, the tree as metrics

Answers: 1c 2b 3d 4a 5b

## The idea being tested

A branch is a metric only when it is a numerator over a denominator on one definition and one
window. This file fills three of the six branches; items, price and discounts are not in it. The
trap is a fraction built from two reports: booked rupees over delivered orders gives Rs 25,943, an
AOV that matches no definition and multiplies back to Rs 7,78,300. The check is the tree's own
identity: AOV times the orders the revenue was summed over must give that revenue back.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | Revenue and orders are both in the file, so AOV is Rs 5,44,810 / 30 = Rs 18,160. | a and d need list prices and items, which the file does not hold. b needs an item count per order, which it does not hold either. |
| 2 | b | 30 x (Rs 5,44,810 / 21) = Rs 7,78,300, 43 percent above what was booked, because the numerator keeps 9 orders' rupees the denominator dropped. | a would hold only for a booked-over-booked AOV. c would hold only for 21 x Rs 24,800. d: the identity holds for the mean, which is what AOV is. |
| 3 | d | Items and prices are what the deeper tree needs, and it shows which part of the basket moved. | a throws away the fields that answer "which part moved". b needs traffic data, not items. c hides customers, marketing's branch. |
| 4 | a | Rs 5,20,790 / 21 = Rs 24,800, one definition top and bottom. | b is the chapter's trap. c is the booked figure on the wrong definition. d divides by customers, which is revenue per customer, a different branch. |
| 5 | b | The mix happens because two reports count different things; asking first is the one-line prevention, and the identity is the one-line check. | a hides the gap without removing it. c picks a number by its size, not its meaning. d averages two honest numbers into one that matches nothing. |

## The part worth arguing about

Item 3. The deeper tree costs a join, and a team might keep the three-branch tree for speed. It is
the right call only until someone asks which part of the basket moved, and on Tuesday someone
will.

**Kavya's review.** "When two reports feed one fraction, ask each what it counts before you divide."

## Where the pattern lives in production

Reliance reports Jio as 533 million subscribers and revenue per user of Rs 215.6 a month, a tree of
customers times revenue per customer, and investors multiply the branches back. A branch taken
from a different report or period breaks that multiplication.

## Hands-on

Notebook 02's identity table shows Rs 7,78,300 against Rs 5,44,810 and Rs 24,800 for delivered.

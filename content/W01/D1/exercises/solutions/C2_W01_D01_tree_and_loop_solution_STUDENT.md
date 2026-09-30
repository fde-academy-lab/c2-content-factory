# Solution: the tree on the board, then orders and revenue in one loop

Answers: 1c 2a 3b 4d

## The idea being tested

The tree comes before the code. Revenue is customers times orders per customer times revenue per
order, and revenue per order is items per order times price per item, less discounts. Each branch
is a metric with a numerator and a denominator, and each costs something different to move.
Marketing's Rs 12 crore is a bet on the first branch. The loop is the calculator that fills two of
the numbers: it runs once per row, and a row is an order, so it counts orders and sums booked
revenue.

## The table, filled

| Branch | Numerator | Denominator | Today's number |
|---|---|---|---|
| Customers | Distinct customer ids | None, since it is a count | Chapter 3 counts it |
| Orders per customer | Orders | Distinct customers, same window | Chapter 3 counts it |
| Revenue per order | Revenue | Orders, same window | Chapter 4 asks which "typical" is honest |
| Items per order | Items | Orders | Not in this file, which has no line items |
| Price per item | Revenue before discounts | Items | Not in this file |

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | Acquisition buys people who were not buying, and that is the customers branch. | a: new buyers add orders through the customers branch, and orders per customer is how often each buyer returns. b: price is set by the business, and acquisition does not move it. d: a first-order coupon is a cost of acquiring, and the branch it moves is still customers. |
| 2 | a | Orders over distinct customers, with both counted in the same window. | b is the rate upside down. c divides orders by rows, which are orders, so it always gives 1. d is revenue per order, a different branch. |
| 3 | b | A loop over the list runs once per element, and each element is one order: 30 times. | a counts customers, which the loop does not know about. c and d filter by status, which this loop does not do. |
| 4 | d | The loop adds every order with no condition on status, so the total is booked revenue, Rs 5,44,810. | a, b and c each need a condition on status that the loop does not have; chapter 1 adds it. |

## The part worth arguing about

Item 1, option d. Some will argue that an acquisition offer is a discount, and a first-order coupon
does sit on the discounts branch. What the Rs 12 crore buys is customers, and the coupon is one way
of paying for them. Placing a spend on the branch it is meant to move, and its cost on the branch
the cost lands on, is the habit the whole day uses.

**Kavya's review.** "Draw the tree before you open the notebook. If you cannot say which branch a
number fills, you do not yet know why you are computing it."

## Where the pattern lives in production

Metric trees, driver trees and the profitability framework are the same drawing under three names.
Product teams keep one on the wall for their north-star metric, finance teams build plans from one,
and consulting interviews open with one. The loop with a counter and an accumulator is the shape
under every SQL COUNT and SUM the programme reaches in Week 2.

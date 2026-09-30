# Which letters answer the guided walk through the tree and the first loop?

Answers: 1c 2a 3b 4d

## What does the walk test?

The tree comes before the code: revenue is customers times orders per customer times revenue per
order, and revenue per order is items per order times price per item, less discounts. Each branch
is a metric with a numerator and a denominator, and each costs something different to move, so
marketing's Rs 12 crore is a bet on the first branch. The loop is the calculator that fills two of
the numbers: it runs once per row, a row is an order, and with no test on the status it counts
every order and adds up booked revenue.

## What goes in the table?

| Branch | Numerator | Denominator | Today's number |
|---|---|---|---|
| Customers | Distinct customer ids | It has none, since it is a count. | Chapter 3 counts it. |
| Orders per customer | Orders | Distinct customers in the same window | Chapter 3 counts it. |
| Revenue per order | Revenue | Orders in the same window | Chapter 2 measures it, and chapter 4 asks which middle is typical. |
| Items per order | Items | Orders | It is not in this file, which has no order lines. |
| Price per item | Revenue before discounts | Items | It is not in this file either. |

## Why is each key right, and why does each other option fail?

| Item | Key | The question in one line | Why the key holds | Why each other option fails |
|---|---|---|---|---|
| 1 | c | Which branch is marketing's Rs 12 crore for new customers a bet on? | Acquisition buys people who were not buying, and that is the customers branch. | a: new buyers add orders through the customers branch, and orders per customer is how often each buyer returns. b: price is set by the business, and acquisition does not move it. d: a first-order coupon is a cost of acquiring, and the branch it is meant to move is still customers. |
| 2 | a | Which fraction answers how often a customer comes back within the quarter? | It divides orders by distinct customers, both counted in the same window. | b is the rate upside down. c divides by people who registered and never bought in the window, so the rate shrinks for reasons that have nothing to do with coming back. d is revenue per order, a different branch. |
| 3 | b | How many times does the loop's body run on Kalpa's file? | A loop over the list runs once per element, and each element is one order: 30 times. | a: the fields sit inside each record, and the loop walks records. c: the channel is a field the loop reads, and it does not group by it. d: the body runs once for each element, never once for the list. |
| 4 | d | Which reading of sales is the total from a loop that adds every order? | The loop adds every order with no test on its status, so the total is booked revenue, Rs 5,44,810. | a, b and c each need a test on the status that the loop does not have; chapter 1 adds it. |

## Which item is worth arguing about?

Item 1, option d. Some will argue that an acquisition offer is a discount, and a first-order coupon
does sit on the discounts branch. What the Rs 12 crore buys is customers, and the coupon is one way
of paying for them. Placing a spend on the branch it is meant to move, and its cost on the branch
where the cost lands, is the habit the whole day uses.

**Kavya's review.** "Draw the tree before you open the notebook. If you cannot say which branch a
number fills, you do not yet know why you are computing it."

## Where does this pattern show up at work?

Metric trees, driver trees and the profitability framework are the same drawing under three names.
Product teams keep one on the wall for their main metric, finance teams build plans from one, and
consulting interviews open with one. The loop with a counter and a running total is the shape under
every SQL COUNT and SUM the programme reaches in Week 2.

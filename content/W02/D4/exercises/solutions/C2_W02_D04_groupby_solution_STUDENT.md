# Solution: round 1 set

Answers: 1b 2d 3a 4c 5b 6a 7d

## The idea being tested

groupby only knows the keys in the rows it is given, a mean depends on who is in the
denominator, and recency is a fact about the data rather than about the day the notebook runs.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | Filtered to Q2, the rows mention only customers with a Q2 order: 227 of them. | a is the customer list, which groupby never sees. c assumes every buyer bought in both quarters. d confuses orders with customers. |
| 2 | d | The question is about customers who buy, so the denominator is 301 buyers: 1,000 over 301 is 3.32. | a answers a different question, orders per customer on the list. b changes the statistic without fixing the denominator. c: rounding moves nothing at two places. |
| 3 | a | 28 August to 28 September is 31 days, and the data's last date is the only fixed point. | b is recency from the run day, which grows with the calendar. c is recency of the most recent buyer. d guesses a month's length. |
| 4 | c | Someone always bought on the data's last day, so the honest minimum is 0; from the run day it is the gap, 21 days on 19 October. | a passes on the wrong table. b passes on both. d says nothing about the date used. |
| 5 | b | Each row in a customer's group is one order, so counting order ids counts orders. | a counts distinct days, so two orders on one day count once. c is spend. d returns an id, not a count. |
| 6 | a | Rs 19,65,99,040 of Rs 19,84,00,000 is Business: 99.1 percent. A spend target is then a Business target. | b confuses customers with rupees. c is not what the data shows. d draws the wrong decision from the right number: the growth team's campaign is about consumers. |
| 7 | d | Count first, aggregate, attach to the spine, then fix what the merge left missing, then measure recency. | a aggregates before the count is trusted. b merges before there is anything to merge. c sets a date before the data is read, which is the run-day trap in another form. |

## The part worth arguing about

Item 5, option a. On most customers it gives the same number, because most never order twice in
a day, so a spot check of five rows passes. It fails on exactly the heavy buyers the growth team
cares about most. Count the thing you mean: an order is a row with an order id.

## Where the pattern lives in production

A weekly CRM table built from the wall clock is one of the commonest silent bugs in marketing
analytics: every refresh moves customers into "lapsed" without anyone buying anything less.

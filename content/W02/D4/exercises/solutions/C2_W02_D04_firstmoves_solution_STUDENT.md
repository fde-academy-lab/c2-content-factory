# Solution: the first three moves

Answers: 1a 2c 3b 4d

## The idea being tested

Each pandas move today is one the room has already made by hand. The items check that the
translation holds: the loop is a groupby, the tuple names become the columns, the customer list
is the spine and a merge with missing keys changes what a column can hold.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | Split by customer, add the amounts in each group: 301 totals, identical to the loop's dictionary. | b groups by amount, which is not a question anyone asked. c gives one average for everyone. d gives the typical order per customer, not their spend. |
| 2 | c | In a named aggregation the keyword is the output column's name and the tuple is (source column, function). | a would need plain `agg` on columns without names. b is what older dictionary-style calls produced. d is not what pandas returns. |
| 3 | b | The customer list holds each customer once and `rfm` holds each customer once, so the merge is one to one, and saying so makes a repeat raise. | a checks only the right side. c permits a customer to repeat on the right, which is the fan-out. d passes silently on the day the feed changes. |
| 4 | d | No orders means a frequency of 0 and spend of 0, which is a fact about the customer, and then the count can be an integer again. | a drops customers the growth team wants to win over. b leaves a column that sums and averages wrongly. c raises, because NaN cannot become an integer. |

## The part worth arguing about

Item 4, option b. It sounds careful: 0 feels like a value you made up. It is not: the warehouse
holds every order, so a customer with none has placed zero, and writing 0 states that. Recency is
different, and stays missing for these 39, because there is no last order to measure from.

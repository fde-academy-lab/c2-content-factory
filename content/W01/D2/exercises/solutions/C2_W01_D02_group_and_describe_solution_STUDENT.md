# Solution: guided, group, describe, and write it once

Answers: 1d 2b 3a 4c 5b

## The idea being tested

Grouping is one move repeated: a dictionary keyed by the thing you want to compare, updated once per
record. Describing a group needs its typical value and its spread, read off a sorted list. And the
moment the same total is needed twice, it belongs in a function that returns it, because a function
that only prints cannot feed a table.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | d | One count per order, grouped by quarter: 114 in Q1 and 86 in Q2. | a counts distinct customers, which is a different question. b is what a dictionary created inside the loop would leave; this one is created above it. c: each order passes through the loop once. |
| 2 | b | Summing the amounts per quarter gives Rs 2,10,00,000 and Rs 1,87,00,000. | a is revenue per order, a rate. c is the whole file, which no quarter holds. d gives Q2 the first quarter's total, which happens only when the key is ignored. |
| 3 | a | Four segments times two quarters is eight keys, and counting the keys before reading the values catches a segment missing from one quarter. | b drops the quarter from the key, which mixes two quarters into one count. c: a dictionary holds one entry per key, not per row. d keys by customer, which is a different split. |
| 4 | c | Sorted, the 38 amounts run from Rs 860 to Rs 3,000; the middle two average Rs 2,325; the range is Rs 2,140. | a puts the mean, Rs 2,117, in the median's place. b is Retail-Core in Q2. d adds the minimum to the maximum where the range subtracts it. |
| 5 | b | `return total` hands the value to whatever called the function, so a loop can store it in a table. | a prints and returns None. c returns what `print` returns, which is None. d displays the value only when the call is the last line of a cell, and returns None inside the function. |

## The part worth arguing about

Checkpoint 3. Counting the keys feels like a formality, and it is the cheapest check in the day. A
segment that bought nothing in one quarter produces no key at all, and a table built from the
dictionary then has seven rows and nobody notices the missing one. The afternoon's case turns on
exactly that kind of silent loss.

## Where the pattern lives in production

Every `GROUP BY` in SQL and every `groupby` in pandas is this accumulator with the loop hidden, and
both meet later in the programme. The habit of counting groups before reading them is what catches
a join that dropped a category or a filter that emptied a segment.

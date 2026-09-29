# Solution: round 3 set

Answers: 1d 2b 3a 4c 5c 6a 7b

## The idea being tested

The index decides what one row is, the columns decide what is compared across it, and the
aggregation decides what each cell means. Predicting the shape before running a call is the
cheapest check an analyst has.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | d | One group per segment, one sum per group: 4 values. | a is `transform("sum")`, which keeps every row. b and c confuse the group key with the customer. |
| 2 | b | Two keys give one row per pair that exists: 4 segments by 2 quarters is 8, each with the two named measures. | a is the pivoted shape, which groupby does not produce. c transposes it. d is `transform` again. |
| 3 | a | The index is the member, and only the 107 members with a Retail-Plus order appear; one column per quarter. | b assumes the 13 members who never ordered appear. c puts quarters on the rows. d is the order index, the wrong-grain trap. |
| 4 | c | Six months down the side, four segments across. | a swaps index and columns. b is the long form before a pivot. d forgets the columns argument. |
| 5 | c | Growth of a segment is growth of its spend: Rs 26,720 to Rs 35,770 is 34 percent. The default averages orders and understates it. | a measures the typical order, which is a different question. b: here the direction agrees, and in Retail-Core the default flips it, so direction is not safe either. d: both pivots are correct arithmetic; only one answers the question. |
| 6 | a | melt makes one row per member per column: 107 by 6 is 642, zeros included. | b is the long table before the pivot, which had no zero months. c confuses rows with members. d is a groupby by month. |
| 7 | b | "Along a row" means a row per member; "drifting" means months across; summed so each cell is spend; the grand-total check proves nothing was averaged away. | a answers a segment trend. c is the order-index trap. d ranks members and says nothing about drift. |

## The part worth arguing about

Item 5, option b. Direction feels like enough for a head of segment. It was not enough for
Retail-Core this morning, where the averaged pivot said the segment rose 1.5 percent while its
spend fell 1.8 percent. A default that happens to agree today is still the wrong tool.

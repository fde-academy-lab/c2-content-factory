# Solution: round 3, is it every segment, or one?

Answers: 1b 2c 3a 4d 5c 6a 7d 8b 9c 10a

## The idea being tested

The same numbers are needed for every segment and every quarter, so the arithmetic moves into a
function that returns its answer. A function earns trust by reproducing a number already known,
and a split earns trust when the segments roll back up to the total with the right weights. An
average of segment averages gives every segment one vote, whatever its size, and the answer it
gives can reverse a decision.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | A function that prints hands back None, so every cell in the table holds None even though the screen showed the right totals. | a trusts the screen over the value returned. c: each segment writes its own key, so nothing is overwritten. d: storing None raises nothing; the failure arrives later, when someone divides by it. |
| 2 | c | The whole quarter is a case where the answer is already known, so a function that reproduces 114, 86, 69, 1.65 and 1.25 has been tested on real rows. | a checks one number against a tile nobody has checked. b tests the row count and none of the arithmetic. d: reading is no test, and every broken function looked right to its author. |
| 3 | a | The median moved about 3 percent while the maximum reached Rs 29,45,460, so one order stretches the spread; the typical order is steady, and the large one is named separately. | b reads a spread as a level. c reads the small median shift as the whole story and misses the order that stretched the range. d: the median and the range answer different questions and move apart often. |
| 4 | d | 1.12 to 1.06 is 5.3 percent, against the company's 24.6 percent, so the frequency fall sits somewhere else. | a: size alone decides nothing; the segment's own change is small. b: 10.5 percent is the change in its typical order, not in frequency. c: its frequency did fall a little, so "never" is false. |
| 5 | c | 33 orders plus 7 orders is 40, over 32 invented customers, is 1.25. | a gives two customers the same vote as thirty. b adds two rates. d ignores the two frequent buyers entirely. |
| 6 | a | A roll-up that cannot reproduce the known total is wrong, and weighting by customers (total orders over total customers) gives 1.65 to 1.25, a fall of 24.6 percent. | b swaps one unweighted statistic for another. c: rounding changes nothing about the weights. d drops a segment to get a different wrong answer. |
| 7 | d | The tree on his tier, in both closed quarters, gives customers, frequency and order value he can hold against the company's. | a: revenue alone cannot say which branch moved. b tests one branch and assumes the answer. c counts complaints, which says how loud members are and nothing about how often they buy. |
| 8 | b | Test the function on the known totals, then split, then count groups in and rows out, then roll up and check the total. | a and c split before the function is tested. d rolls up before any segment figures exist. |
| 9 | c | The median fell 3.2 percent and the middle half widened only 13.1 percent, so the typical order barely moved. One order of Rs 29,45,460 stretched the range and lifted the mean Rs 1,15,924; without it, Q2's mean is Rs 9,74,750, below Q1's. | a: the mean is the measure one order moves most. b: a range is built from two orders, so it describes the extremes and nothing else. d: the measures agree once each is read for what it describes. |
| 10 | a | A ratio of totals, never a mean of ratios: store the numerators and denominators and divide last, and the region's figure reproduces its own total at every level. | b answers a different question, order value, and leaves the roll-up broken. c: rounding changes nothing about the weights. d throws away every other segment's customers. |

## The part worth arguing about

Item 6. The simple average feels fair because every segment "counts". The question to ask the room
is who the average is about: Meera's question is about customers, and two Student customers should
not weigh the same as thirty-four Retail-Core customers. Which segment carries the fall is the
number you found in your own notebook in the last your-turn cell of the round, and it is the
starting point of the afternoon.

## Where the pattern lives in production

Averages of averages turn up in every regional or category dashboard that shows a "company
average" row computed from the rows above it. It is a staple interview question in GCC analytics
screens ("you have orders per customer for four segments, why can't you average them?"), and it is
the same mechanism behind Simpson's paradox, which later weeks meet on purpose. Functions that print
where they should return break every pipeline that feeds a table, a chart or a report.

## Hands-on picks

Round 3's notebook, `notebooks/C2_W01_D02_03_which_segment_STUDENT.ipynb`, carries `tree_for`,
`describe`, the check against round 2 and the weighted roll-up. Its last your-turn cell is where you
run the tree on all four segments; it has no letters to post.

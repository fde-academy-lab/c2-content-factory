# Solution: what does a typical order look like?

Answers: 1a 2c 3d 4b 5c 6a 7d

## The idea being tested

The mean of the 30 orders is Rs 18,160, and 29 of the 30 orders sit below it. A number that
describes almost no order is a poor answer to "what does a typical order look like", and it is
worse as the value of a new customer's first order, because the acquisition case is priced on it.
The check is a count of orders above the mean, then the sort, then the median. The median is
Rs 2,205, about one eighth of the mean, so a first order is worth about Rs 2,205 and the payback on
acquisition needs about eight times as many orders as the mean suggested.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | 29 of the 30 orders sit below Rs 18,160, so the mean is a number almost no customer spent. | b: the median uses every order to find the middle, and the mean is what one order can drag. c: delivered orders give a higher mean, Rs 24,800, so the change makes the problem worse. d: rounding keeps the same misleading number. |
| 2 | c | One count answers it: if only one or two orders sit above the mean, those orders are what is pulling it. | a recomputes the same statistic on fewer orders. b splits by channel, which shows where the rupees sit and not whether one order dominates. d compares with a window this file does not have. |
| 3 | d | One order of the 30 sits above Rs 18,160; the other 29 sit below it. | a is what a symmetric list would give. b reverses the direction. c: a mean always sits at or below the largest order, so at least one order is at or above it. |
| 4 | b | With 30 orders the middle falls between the 15th and 16th, so the median is their average: Rs 2,110 plus Rs 2,300, over two, is Rs 2,205. | a and c take one of the two middle orders, which is the median of an odd count. d confuses the mean with the middle. |
| 5 | c | The total rises to Rs 1,01,200 over six orders, a mean of about Rs 16,870, while the middle moves from Rs 2,200 to the average of Rs 2,200 and Rs 2,400, which is Rs 2,300. | a moves the median as if it were a mean. b reverses which statistic the large order moves. d ignores that one order carries nearly nine tenths of the new total. |
| 6 | a | Rs 18,160 over Rs 2,205 is about 8.2, so each first order returns about an eighth of what the case assumed, and the payback needs about eight times as many orders. | b confuses how easy an order is to win with what it returns. c: the payback on a customer is paid out of that customer's orders. d invents a second median. |
| 7 | d | On delivered orders the median is Rs 2,060, the middle of the 21 delivered amounts. | a is the booked median, a different definition. b is the delivered mean, the statistic Anand refused. c is the not-cancelled median, a third definition. |

## The part worth arguing about

Item 1, option c. Some will argue that delivered orders are the honest base and so the fix is to
recompute the mean on them. Definitions matter, and round 1 said so. The problem here is the
statistic: a mean on any definition that holds the same order at the top is pulled by it, and the
delivered mean, Rs 24,800, is pulled further. Change the statistic first, then choose the
definition.

**Kavya's review.** "When the mean and the median disagree by a factor of eight, the gap is the
finding. Report the median and say in one line why."

## Where the pattern lives in production

Order values, salaries, house prices, session lengths and claim amounts all have a long right tail,
and every one of them gets reported as a median by teams that have been burned. Product analysts
report median basket size, and payment teams watch the p50 and the p95 of transaction value. The
count above the mean is the fastest one-line test of whether a tail is present.

## Hands-on

The empty your-turn cell of `notebooks/C2_W01_D01_03_typical_order_STUDENT.ipynb` shows the sorted
list when you type the sort into it; what you find at the top is yours to name. Level 4 prints the
booked median, Rs 2,205, and the delivered median, Rs 2,060, which confirm Q4 and Q7.

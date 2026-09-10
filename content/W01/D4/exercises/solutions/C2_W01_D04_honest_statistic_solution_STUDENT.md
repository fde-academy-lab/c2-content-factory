# Day 4 solution, E4. Pick the honest statistic

## The idea being tested

Four data shapes at the top and eleven items on what travels with a number. Choosing a statistic is a judgement about the shape of the column, and the second half of the sheet is about the fact that the number is never the whole deliverable: the count it rests on goes with it, every time.

## The answers

**Answers: 1a 2b 3c 4d 5a 6b 7c 8d 9a 10b 11c 12d 13a 14b 15c**

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | The median describes the order standing in the middle, and one Rs 480,000 order cannot move it. | The mean describes one order out of 44. The maximum and the range each describe the extremes rather than the typical. |
| 2 | b | With no extremes, mean and median agree, so either is honest and the mean is the conventional choice. | The median is equally right here, which is why the question is about which makes no difference. The mode repeats little on continuous minutes. |
| 3 | c | Baskets of one or two with a few of thirty is a long right tail, so the median is the honest choice. | The mean is dragged by the thirties. The maximum describes one basket. The total answers a different question. |
| 4 | d | City is a category, so the only statistic available is the commonest value. | Mean, median and range all need an ordering that city does not have. |
| 5 | a | The commonest amount appears twice in 44, so the mode describes almost nothing. | It does not repeat too often; it barely repeats at all. It is a real statistic and Python has `statistics.mode`. |
| 6 | b | Min and max are the two least typical values in the file, so the range is built entirely from them. | It is one subtraction and easy. It does not ignore the median so much as never involve it. It is often far too large rather than too small. |
| 7 | c | The fence is a way of spotting the tail quickly, and it proves nothing about the order it catches. | It is not a test, and treating it as one is how real orders get deleted. Applying it as a rule before analysis is the anti-pattern. It is not the maximum. |
| 8 | d | A long distance up from the median and a short one down is a long right tail. | Symmetric would need the two distances to be similar. A left tail is the mirror image. A sort does not have errors. |
| 9 | a | The direction of the skew reads straight off sorted values, which is why it is the tell that needs nothing. | Standard deviation, correlation and confidence intervals all need formulas nobody has been given yet. |
| 10 | b | Five returns of twelve is 41.7 percent; six of twelve is 50 percent, so it moves by more than eight points. | 42 and 46 understate it. 58 would need two more returns. |
| 11 | c | On 1,200 records one more return moves the rate by about a tenth of a point. | One point, four points and eight points all belong to much smaller denominators. |
| 12 | d | On 1,200 records one order barely moves it, which is what makes the number worth putting in a sentence. | Recency is not what the twelve-record rate lacks. Reporting both without counts hands the reader the problem. Saying neither ignores that one of them is solid. |
| 13 | a | The count is the denominator, and a rate without it cannot be argued with. | The date, the author and the tool are provenance, which is useful and is not what makes the rate readable. |
| 14 | b | It carries the count, the rate and the reason not to rank on it. | The other three all travel into a slide and cannot be questioned. |
| 15 | c | That no segment in a 44-order file has the base to be ranked is the finding. The numbers are inputs to it. | The best segment is the claim the finding refuses. The median and the mean are numbers, and neither is a finding on its own. |

## The part worth arguing about

Item 15. A room resists it, because a table with a clear winner feels like an answer and a sentence saying the file cannot rank anything feels like a failure. Push on what happens when the winner appears on a slide and one order changes. The finding is the deliverable, and the table is the working.

Item 2 is the other one. Somebody always says the median is safer, always. Ask what safer means on a column with no extremes, and the answer is that it costs nothing and gains nothing, which is worth saying out loud once.

## The hands-on picks

The running half is `notebooks/C2_W01_D04_ex2_hands_on_STUDENT.ipynb`, and its four markers are:

**Answers: 1b 2c 3d 4c**

The executed twin is `C2_W01_D04_ex2_hands_on_solution_STUDENT.ipynb` in this folder.

## Where this pattern lives in production

Any dashboard that shows a conversion rate per segment shows exactly this failure when a segment is small. The rate is arithmetically correct and it moves several points on one event, and nothing on the tile says how many events it rests on.

The interview question is item 13's, and it arrives as "segment A converts at 42 percent on 12 records and segment B at 31 percent on 1,200, which do you trust?" Say B and name the mechanism, then say what you would need before you would quote A at all.

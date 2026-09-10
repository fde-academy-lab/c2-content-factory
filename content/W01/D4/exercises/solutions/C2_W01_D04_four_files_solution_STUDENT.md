# Day 4 solution, E3. Four files, described only by two numbers

## The idea being tested

Two numbers per file, and no data. The whole sheet turns on one comparison: where the mean sits relative to the median, and what the count underneath both of them will bear.

That comparison is the cheapest diagnostic in descriptive statistics and it needs no chart, no library and no formula. A learner who can read four files from eight numbers can read any summary table they are ever handed.

## The answers

**Answers: 1b 2b 3c 4a 5d 6b 7c 8d 9b 10d 11c 12c 13a 14b 15c**

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | File B's mean is Rs 12,753 against a median of Rs 1,910, which is nearly seven times larger. | A's two numbers are within Rs 30 of each other. C leans the other way. D's are within Rs 40. |
| 2 | b | A mean far above a median means a few very large values pulling the average up. | The row count says nothing about shape. The highest median belongs to C. Roundness is a coincidence. |
| 3 | c | C's mean of Rs 2,010 sits below its median of Rs 2,400, which is a long tail of small values. | A and D are balanced. B leans the other way, hard. |
| 4 | a | A's mean and median differ by Rs 30 on 500 rows, which is as symmetric as real money gets. | B and C both lean. D is balanced too and has only twelve rows, which is a different problem. |
| 5 | d | Twelve rows is too small a base for a rate, whatever its mean and median look like. | A, B and C all have enough rows for a rate, though B needs a caveat about its mean. |
| 6 | b | The base is the reason, and it has nothing to do with the two numbers you were given. | Disagreement between mean and median describes B rather than D. Roundness and a missing maximum are not reasons to refuse a rate. |
| 7 | c | The median describes the order standing in the middle, which is what somebody asking for typical wants. | The mean describes one order out of 44. The midpoint of two statistics is a third statistic nobody defined. Both with no comment leaves the reader to choose. |
| 8 | d | Saying which order owns the mean is what stops somebody quoting Rs 12,753 later. | Silence is how the wrong number travels. The file being small is D's problem. Accuracy is the wrong word: both numbers are exact and one describes the file. |
| 9 | b | B's mean describes a single order, so quoting it without a caveat misleads on every reading. | A and C are large and reasonably behaved. D's problem is its count rather than its mean. |
| 10 | d | Only one order sits at or above a mean that one order created, so 43 of the 44 sit below it. | 1 is the count above rather than below. 4 and 22 are the answers you would expect from a symmetric file. |
| 11 | c | Rs 12,753 falls to about Rs 1,900, which is a drop of roughly Rs 10,800. | Rs 100 and Rs 1,000 both understate it by an order of magnitude. Saying it does not fall is the belief the whale exists to break. |
| 12 | c | The maximum next to the mean settles every one of these questions in one glance. | The mode repeats almost nothing on money. The total is the mean times the count, so it adds nothing. Distinct values answer a different question. |
| 13 | a | The arithmetic is right and the description is wrong, which is the whole day in one sentence. | Saying nothing is wrong is the failure. The arithmetic and the rounding are both fine. |
| 14 | b | Agencies report median household income because top incomes drag the mean away from the household in the middle. | The mean does use every household, which is the reason it fails here rather than a defence. The mode and the range answer different questions. |
| 15 | c | The shape decides the number, and both statistics are always available. | Always and never are rules that stop you thinking. Reporting both every time hands the choice to the reader. |

## The part worth arguing about

Item 7 against item 15. Somebody always says report both, and it sounds even-handed. Push on what a reader does with two numbers seven times apart and no shape: they pick the one that suits them. Choosing the number and saying why is the job.

Item 5 is the other. A room resists refusing to quote anything, because refusing feels like failing. The reply is that a rate on twelve records moves by more than eight points when one record changes, so the refusal is the only honest answer available.

## The hands-on picks

The running half is `notebooks/C2_W01_D04_ex1_hands_on_STUDENT.ipynb`, and its four markers are:

**Answers: 1a 2c 3b 4c**

The executed twin is `C2_W01_D04_ex1_hands_on_solution_STUDENT.ipynb` in this folder.

## Where this pattern lives in production

Anscombe's quartet, 1973, is four datasets that share almost identical summary statistics and look completely different when drawn. It is the standing argument that a summary can mislead, and this drill is its cheap version: two numbers per file is enough to tell that something is wrong, and never enough to tell what.

The interview question is item 14's, and it arrives as "mean or median for a money field, and why?" Say the median and name the mechanism, then say what you would put beside it.

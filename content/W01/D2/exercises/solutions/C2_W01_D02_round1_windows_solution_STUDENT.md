# Solution: round 1, is the drop real?

Answers: 1c 2b 3a 4d 5c 6a 7b 8d

## The idea being tested

A drop is confirmed on matched windows before anyone explains it. Two closed quarters of 13 weeks
each compare fairly as totals; a quarter cut short compares fairly only against the same weeks of
the other quarter, or as a rate per week. The check that catches an unmatched window is the first
and last order date of each side, which takes a minute and would have stopped a Rs 12 crore
decision made on a 25.9 percent fall that was never there.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | The change is measured against the starting quarter: Rs 23,00,000 over Rs 2,10,00,000 is 11.0 percent. | a: measuring against Q2 inflates the fall to 12.3 percent. b: the rounded crore figures lose Rs 3,00,000 of the gap. d: the tile covers 11 weeks of Q2, so its fall is a window artefact. |
| 2 | b | The tile stops on 15 September, so it holds 11 weeks of Q2 against 13 of Q1, and two weeks of revenue are missing from one side only. | a: Rs 54,40,050 over Rs 2,10,00,000 is 25.9 percent, so the base is Q1. c: both sides count booked orders, which is consistent. d: the totals are exact to the rupee. |
| 3 | a | The first and last order date of each window, and the weeks between them, show 13 against 11 at once. | b: medians describe a typical order and say nothing about the window. c: customers are the next rung, asked once the windows match. d: the sums are right; the windows are wrong. |
| 4 | d | Rs 2,00,844 less a week, over Q1's Rs 16,15,385, is 12.4 percent. | a: 14.2 percent measures the gap against Q2's rate. b: 25.9 percent is the unmatched totals again. c: 11.0 percent is the closed-quarter fall, a different pair of windows. |
| 5 | c | Find the windows, choose a fair pair, compute, then say the definition and window in the sentence. | a and d compute before the windows are known, which is how the tile's number reached a slide. b computes before choosing the fair pair. |
| 6 | a | Q1 runs 1 April to 30 June, 91 days; Q2 runs 1 July to 30 September, 92 days. Per day, Q2's total is divided by one more day, so its fall reads 0.9 points larger. | b: a rate per day matches the total whenever the windows have equal days. c: the rate divides by calendar days in the window. d: both figures are exact; they answer slightly different questions. |
| 7 | b | Both methods are fair. They differ because a few large Business orders land unevenly inside a quarter, so the first 11 weeks of Q1 hold a different share of its revenue than a weekly average implies. Once a quarter has closed, compare closed quarters. | a and c call a real difference a bug. d averages two honest numbers into one that answers no question. |
| 8 | d | A quarter-to-date comparison uses the same weeks of both quarters, so the first two weeks of Q3 meet the first two weeks of Q2. | a is the tile's error again. b matches the length and mismatches the position in the quarter, where ordering patterns differ. c projects two weeks to thirteen on an assumption nobody has checked. |

## The part worth arguing about

Item 7. Some of the room will want one number, and the honest answer is that both are right
answers to different questions. The rule that ends the argument is operational: once a quarter has
closed, the closed quarters are the comparison, and the 11-week figures are retired.

## Where the pattern lives in production

Every business review that runs mid-quarter faces this. Retail and e-commerce dashboards label
tiles "QTD" and compare them against the prior quarter's full total, and the gap reads as a crisis
until someone checks the dates. Analysts at Indian GCCs call the fix "like for like" or "same
period last quarter", and a screen that asks "sales dropped, how would you investigate?" expects
the window check as the first sentence of the answer.

## Hands-on picks

Round 1's notebook, `notebooks/C2_W01_D02_01_is_the_drop_real_STUDENT.ipynb`, carries the dates,
the weekly rates and the cumulative line with the 11-week cut marked. Its your-turn cells have no
letters to post; the numbers they print are the ones in the table above.

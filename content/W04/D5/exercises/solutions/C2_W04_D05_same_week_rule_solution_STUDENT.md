# Which answers hold in the guided set on the same-week-last-year rule, and why?

Answers: 1c 2b 3c

The guided set built the house bot's rule on twelve real weeks and hid three of them. The rule
copied 14 October 2024 (401,000) into 13 October 2025, then scored an MAE of 62,533 on the three
hidden weeks, every miss too high, because Diwali's week came one week earlier in the 2025 calendar
(20 October against 28 October 2024) and each calendar copy carried a week that sat closer to the
2024 festival.

**Who needs the answer.** You, to check your three letters after the guided build. The planner
books shifts from whichever rule wins, so the scoring has to be right before any code runs.

**The questions on the way.**

- What does the set test?
- Why is each key right, and each other letter wrong?
- Which item is worth arguing about?
- Where does the pattern live at work?

## What does the set test?

It tests the three moves of the day in miniature: copy a week by a stated rule, score the copy only
on weeks it never saw, and read the misses before choosing what replaces the rule. The help fades
from a full working to half to none.

## Why is each key right, and each other letter wrong?

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| Q1, the week the rule copies | c | 52 weeks before Monday 13 October 2025 is Monday 14 October 2024, which shipped 401,000 | a is the week at the same distance from Diwali, the festival-aligned source; b is the week before, which is naive; d adds finance's 4 percent to the right week, which is a different rule |
| Q2, the MAE on three hidden weeks | b | The misses are 32,000, 47,300 and 108,300, all too high; their sum, 187,600, over three is 62,533 | a divides the sum by all twelve rows; c is the sum before dividing; d is one week's miss, Diwali's own week |
| Q3, what replaces it on festive weeks | c | The misses come from the festival moving; copying by distance from Diwali puts each week beside its true partner | a repeats a week that ran at a different point of the festival; b raises copies that already run high; d averages two years on the calendar and keeps the misalignment |

## Which item is worth arguing about?

Q3's option b. Raising the copy by 4 percent looks responsible, since the centre grew about 4
percent a year, and it is exactly finance's rule. On festive weeks it fixes the wrong thing: the
copy is a week out of place, and growth on a week out of place makes the miss bigger. On ordinary
weeks, far from the festival, the same 4 percent is right, which is why finance's rule ties
festival-aligned on the summer weeks of chapter 2.

## Where does the pattern live at work?

Every retailer, airline and payments company that forecasts around a moving festival or holiday
meets it: Diwali, Eid and Easter move between calendar weeks each year. The check before any model is
the same: line the years up by distance from the festival, then compare.

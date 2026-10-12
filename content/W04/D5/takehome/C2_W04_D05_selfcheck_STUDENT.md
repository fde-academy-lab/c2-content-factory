# Did your four-week test give the numbers it should, and did your paragraph say why they moved?

The self-check for tonight's take-home: Flipkart Lucknow's weekly shipments rescored with only the
last four weeks hidden. Illustrative case: the company is real, the situation and the data are
synthetic, built for this class. Open this after your notebook runs.

**Who needs the answer.** You, to know whether your numbers and your call would survive the regional
operations head's first question, and the vendor's sponsor's.

**The questions on the way.**

- Can you say what a shorter test does, in plain words, before any number?
- Did your rules give these forecasts and scores?
- Which numbers should have moved, and why?
- Does your paragraph carry the four things a strong one carries?

## Can you say it in plain words first?

Say each of these aloud, in one sentence, before reading on:

1. A short test judges the week it starts from as much as the rule, because naive and drift are built
   from that one week.
2. A rule that copies last year's weeks never looks at the starting week, so moving the start barely
   moves its score.
3. A forecast made further ahead misses by more, so the last weeks of a forecast are its worst.
4. A test shorter than the plan cannot tell you how a rule does over the whole plan.

If a sentence would not come out, re-read chapter 2's hold-out slides and notebook 02's split cell
before checking numbers.

## Did your rules give these numbers?

**The split.** The origin is the week of 24 August 2026, which shipped 196,600. The four hidden weeks
shipped 238,400, 233,700, 230,300 and 232,200, an average of 233,650.

**The forecasts.** Naive repeats 196,600 four times, so its misses are 41,800, 37,100, 33,700 and
35,600, all too low.

| Week | Actual | House bot | Finance's rule and festival-aligned | Vendor's curve, made from 22 June |
|---|---|---|---|---|
| 31 August | 238,400 | 230,100 | 239,304 | 263,200 |
| 7 September | 233,700 | 213,200 | 221,728 | 244,300 |
| 14 September | 230,300 | 233,400 | 242,736 | 268,700 |
| 21 September | 232,200 | 230,100 | 239,304 | 266,400 |

**The scoreboard.**

| Rule | MAE, four weeks | Weeks too high | Misses priced | MAE, thirteen weeks |
|---|---|---|---|---|
| Finance's rule | 8,104 | 3 of 4 | Rs 4.10 lakh | 6,615 |
| Festival-aligned | 8,104 | 3 of 4 | Rs 4.10 lakh | 6,615 |
| House bot | 8,500 | 1 of 4 | Rs 7.89 lakh | 9,831 |
| Vendor's curve | 27,000 | 4 of 4 | Rs 5.85 lakh | 16,400 |
| Naive | 37,050 | 0 of 4 | Rs 37.05 lakh | 14,923 |
| Drift | 37,439 | 0 of 4 | Rs 37.44 lakh | 14,842 |

The costs are printed to two places; your notebook rounds to one, so Rs 5.85 lakh may print as 5.8
and Rs 37.05 lakh as 37.0. The one check that prints FAIL is the price claim from the thirteen-week
test: here the vendor's Rs 5.85 lakh is more than festival-aligned's Rs 4.10 lakh.

Finance's rule and festival-aligned print the same numbers because these four weeks sit more than
five weeks before Diwali's week, where festival-aligned copies the calendar week a year back plus 4
percent, as finance does.

## Which numbers should have moved, and why?

- **Naive and drift more than doubled.** The week of 24 August shipped 196,600, a dip that sat 37,050
  below the four hidden weeks' average, and both rules start from it. The thirteen-week test started
  from 218,300, close to its hidden weeks' average of 217,746, which is luck in the other direction.
- **The copies of last year moved least.** The house bot, finance's rule and festival-aligned copy
  2025's weeks and never use the origin, so their forecasts did not change at all; only the weeks
  being scored did, which moved their scores by 1,331 and 1,489 a week while naive's more than doubled.
- **The vendor's gap grew.** Its four rows are its forecast for 10 to 13 weeks after 22 June, the
  farthest it looked ahead, and its misses grow with distance: 148 percent above festival-aligned's
  MAE on thirteen weeks, 233 percent on these four. A fair four-week test would need the vendor to
  forecast again from 24 August, which its file cannot do.
- **Priced, the vendor beats the bot.** Its MAE is about three times the bot's, yet its misses cost
  Rs 5.85 lakh against Rs 7.89 lakh, because every vendor miss is too high, where a shipment costs Rs
  5.42, and the bot's big misses are too low, where a shipment costs Rs 25. On four weeks the vendor
  no longer undercuts festival-aligned, whose misses here are small.

The pick does not change: festival-aligned still ties finance's rule for the lowest MAE, and neither
test holds a festive week, so the festival placement still rests on the 2025 back-test.

## Does your paragraph carry the four things?

A strong paragraph names the dip at 196,600 and what it did to naive; names the rules that never look
at the origin; says the vendor's four weeks are its farthest ahead; and ends on one call: keep
festival-aligned, and judge any rule on at least as many hidden weeks as the forecast must reach
ahead, ten here, since a test should be at least as long as the horizon (FPP3, section 5.8, checked 12 October 2026).
A weak one reports the new numbers without the origin week, calls naive "much worse" as if the rule
had changed, or calls the vendor "cheaper" without saying why its misses are cheap.

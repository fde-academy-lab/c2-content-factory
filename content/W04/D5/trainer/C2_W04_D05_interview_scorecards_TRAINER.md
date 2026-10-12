# Interview room: the scorecards for both transcripts and the AI-company variant

**TRAINER ONLY.** The transcripts the room reads, [S] "How do you evaluate a forecast?" and the [D]
dispute the fallback runs, are in `extras/C2_W04_D05_interview_transcripts_STUDENT.md`; this page
scores them. Written for this programme in the style of product-company and GCC screens; the facts
inside are from the case file.

## How is each criterion scored?

The seven criteria, each 0 to 2: 0 absent; 1 present but incomplete, or failing the obvious
follow-up; 2 complete and surviving it. The obvious follow-up includes the technical one: a test that
never lets a model see the weeks it forecasts, a measure that matches what the decision pays, and a
range stated honestly. A weak answer's figure counts toward sizing only in shipments, shifts or
rupees. Every hire-grade 2 below rests on a line the answer says.

## How do the [S] answers score?

| Criterion | Weak | Hire-grade | The hire-grade line that earns it |
|---|---|---|---|
| Clarified the scope | 0 | 2 | Four clarifiers: the decision and how far ahead it must reach (ten weeks), the cost of a miss each way, whether the festival and the sale move, whether any forecast met unseen weeks |
| Named the hidden weeks and the unit | 0 | 2 | Thirteen weeks, 29 June to 21 September 2026, forecast from 22 June, covering the ten-week horizon; MAE in shipments and the quantile loss at 0.82 in rupees, both fixed before scoring |
| Saw the paradox | 0 | 2 | A fit within 1.4 percent beside a hidden-week miss of 16,400, almost all bias (16,108 a week too high); the cheapest raw misses from the forecast that loses once each is moved to its own 0.82 point, Rs 10.0 lakh against Rs 8.8 lakh |
| Sized it with a unit | 0 | 2 | 9,831 against 6,615 against 16,400 shipments a week; Rs 8.8 lakh against Rs 10.0 lakh; 10 of 13 weeks covered |
| Said what would change their mind | 0 | 2 | A sale at a different distance from Diwali re-lines the weeks; a first sale week outside 5.9 percent below to 7.8 percent above re-opens the plan; overtime that absorbs a short week lowers the cushion |
| Tied it to a decision and its cost | 0 | 2 | The plan covers demand in 0.82 of weeks because a late shipment costs Rs 25 and a spare one Rs 5.42, and it covered 10 of the 13 hidden weeks |
| Gave the structure before the number | 1 | 2 | Measures, test set and origin, the baselines, the plan's cushion, what the test cannot see, in that order |
| Total, of 14 | 1 | 14 | |

**Where the weak answer scores its point.** It has a shape (split, train, score, pick), which earns 1
for structure; it fails the obvious follow-up, because a random split lets a model see weeks after the
ones it forecasts. "Within 2 percent" is a fit, and no figure comes in shipments, shifts or rupees.

**What a strong interviewer would still push on, and the reply.**

- "Why thirteen weeks?" The plan's last week is ten weeks past the data, so the test must reach ten
  weeks ahead, and FPP3 puts a test set at about a fifth of the sample, at least as long as the
  horizon. The copies need only a year of history, so they could be tested on far more, from many
  origins through 2025's festival; the real limit is the vendor's file, which holds forecasts from one
  origin only.
- "Your 2.6 percent came from the weeks you score on; isn't that circular?" A little, for every
  forecast alike, which is why each is compared at its own 0.82 point. On these weeks festival-aligned,
  finance's rule and the seasonal naive come out as one forecast, each at Rs 8.8 lakh, so only the
  festival separates them. The point itself is loose: 2.6 percent by pandas' default reading of the
  sorted thirteen, 4.1 by another common convention. A rolling origin would set it on weeks the final
  test never touches.
- "Why would the festival be the easiest stretch to forecast?" On 2025's festival festival-aligned
  missed by 1.4 percent of a festive week, half its 3.1 percent on the ordinary hidden weeks, and that
  borrows the 4 percent measured later. Without it the miss is 10,575 a week, and the raised plan
  covers 2 of the 8 festive weeks instead of 7. One festival cannot size the festive error; it shows
  only that the calendar copy is placed wrong, by 58,250 a week.

## How does the AI-company variant score?

| Criterion | Score | The line that earns it |
|---|---|---|
| Clarified the scope | 2 | The unit (tokens a second at the peak), the latency target, the lead time and what stretches, the cost of a timeout against an idle GPU hour, and whether anything like it has launched |
| Named the hidden weeks and the unit | 2 | Tokens a second; a method tested only on a launch it did not see, and called untested when there is one earlier launch or none |
| Saw the paradox | 2 | The last launch's curve looks like a forecast but cannot be tested on itself, and days from launch fix the launch curve while scrambling the weekly cycle, so both are kept |
| Sized it with a unit | 2 | 2 lakh users, 10 percent in the peak minute, 1,500 tokens a request, all invented: about 5 lakh tokens a second |
| Said what would change their mind | 2 | Waitlist sign-ups before launch and the first hour's tokens a second after it, against the ground-up size |
| Tied it to a decision and its cost | 2 | Capacity booked ahead above the forecast when a timeout costs more than an idle GPU hour, with the latency target setting the headroom and on-demand capacity, rate limits and a waitlist covering the rest |
| Gave the structure before the number | 2 | Size it, check it against history, set capacity to the latency target, say what would move it |
| Total, of 14 | 14 | |

## How do the [D] answers score?

Used in the fallback (part 4, S13, 25 minutes): read in pairs, played, then scored.

| Criterion | Weak | Hire-grade | The hire-grade line that earns it |
|---|---|---|---|
| Clarified the scope | 0 | 2 | Plus 4 and plus 22 against which weeks; which forecast met unseen weeks and which never met a festival; who carries a short week |
| Named the hidden weeks and the unit | 0 | 2 | Thirteen hidden weeks in shipments, and 2025's festival back-tested from 22 September 2025 |
| Saw the paradox | 0 | 2 | Finance's rule ties on the hidden weeks because they hold no festival; the vendor's misses are cheap because they run high |
| Sized it with a unit | 0 | 2 | 20,275 shifts, 3,719 at the peak; 3,082 shifts and about Rs 20.0 lakh over finance's rule; 3,413 to 3,906 shifts needed at the peak week's extremes |
| Said what would change their mind | 0 | 2 | The vendor forecasting 2025's festival from data to September 2025 before Friday; a sale at a different distance from Diwali; a first sale week outside the hidden weeks' range |
| Tied it to a decision and its cost | 0 | 2 | The plan's range priced at its ends, about Rs 2.0 lakh of idle shifts or Rs 5.6 lakh of late shipments for the peak week, and its cost to finance |
| Gave the structure before the number | 0 | 2 | Restate, answer, concede, what would change it, then the plan, its cost, its range and the people |
| Total, of 14 | 0 | 14 | |

**Where the weak answer loses everything.** "Plus 13 percent" is a midpoint of two calendar copies, so
its peak stays on 5 October; percent is no unit for a shift plan, and "machine learning should beat a
rule of thumb" never tests either forecast.

## How do pairs run the mock round on Saturday?

The asker reads one question from either transcript and one follow-up from its table, scores the
answer on the seven criteria above, then the pair swaps. A pair that finishes early takes the AI
variant.

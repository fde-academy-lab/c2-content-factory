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

| Criterion | Weak | Typical | Hire-grade | The hire-grade line that earns it |
|---|---|---|---|---|
| Clarified the scope | 0 | 0 | 2 | Four clarifiers: the decision and how far ahead it must reach (ten weeks), the cost of a miss each way, whether the festival and the sale move, whether any forecast met unseen weeks |
| Named the hidden weeks and the unit | 0 | 1 | 2 | Thirteen weeks forecast from one origin, 22 June, covering the ten-week reach; the miss in shipments and the quantile loss at 0.82 in rupees, both fixed before scoring |
| Saw the paradox | 0 | 0 | 2 | A fit within 1.4 percent beside a hidden-week miss of 16,400, almost all bias; the cheapest raw misses from the forecast that loses at its own 0.82 point; and on these weeks festival-aligned is the seasonal naive plus 4 percent, so they cost the same and only the festival separates them |
| Sized it with a unit | 0 | 0 | 2 | 9,831 against 6,615 against 16,400 shipments a week; Rs 8.8 lakh against Rs 10.0 lakh; 10 of 13 weeks covered |
| Said what would change their mind | 0 | 0 | 2 | A sale at a different distance from Diwali re-lines the weeks; a first sale week outside the hidden weeks' range re-opens the plan; overtime that absorbs a short week lowers the cushion |
| Tied it to a decision and its cost | 0 | 0 | 2 | The plan covers demand in 0.82 of weeks because a late shipment costs Rs 25 and a spare one Rs 5.42, and it covered 10 of the 13 hidden weeks |
| Gave the structure before the number | 1 | 1 | 2 | "Five steps: the test, the measure, the bar to beat, the price, and what the test cannot see", said before any figure, and the answer follows that order |
| Total, of 14 | 1 | 2 | 14 | |

**Where the weak answer scores its point.** It has a shape (split, train, score, pick), which earns 1
for structure; it fails the obvious follow-up, because a random split lets a model see weeks after the
ones it forecasts. "Within 2 percent" is a fit, and no figure comes in shipments, shifts or rupees.

**Where the typical answer scores its two.** A time-ordered hold-out earns 1, held back from 2 by a
length nobody checked and a percent for a unit, and its shape earns 1. Comparing with last year's same
weeks earns nothing for the paradox, since it never asks why a close fit loses. It never prices a
direction or asks about the festival, which is where the hire is decided.

**What a strong interviewer would still push on, and the reply.**

- "Why thirteen weeks?" The vendor's file holds forecasts from one origin only, and thirteen weeks is
  what it covers; the plan's last week is ten weeks past the data, so thirteen also covers the reach
  FPP3 asks a test set to span. The copies need only a year of history, so they could be tested on far
  more, from many origins through 2025's festival, and that rolling test is the next one to run.
- "Your 2.6 percent came from the weeks you score on; isn't that circular?" Yes, and each forecast
  was tuned the same way, which is why each is compared at its own 0.82 point; how much the tuning
  flatters each depends on its own misses. On these weeks festival-aligned,
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
| Clarified the scope | 2 | The unit (requests open at once at the peak, with prompt and answer tokens), the latency target, the lead time and what stretches, the cost of a timed-out request against the idle capacity one request would use, and whether anything like it has launched |
| Named the hidden weeks and the unit | 2 | Requests open at once, with prompt and answer tokens counted apart; a forecast tested only on a launch it never saw and scored by its miss in prompt and answer tokens at the peak minute, and called untested with one earlier launch or none |
| Saw the paradox | 2 | "That curve looks like a forecast, and it is not one until it has predicted a launch it never saw"; days from launch fix the launch curve while scrambling the weekly cycle, so both are kept |
| Sized it with a unit | 2 | 2 lakh users, 1 percent in the peak minute, 1,000 prompt and 500 answer tokens, 10 seconds a stream and 20 open requests a GPU, all invented: about 330 open at once and about 17 GPUs before headroom, with the placeholder checked at about 3 requests a user a day |
| Said what would change their mind | 2 | Waitlist sign-ups before launch and the first hour's requests after it, against the ground-up size |
| Tied it to a decision and its cost | 2 | One more GPU booked when the timeouts it would prevent across the busy minutes cost more than its rent for the whole booking, set per machine as the packer shifts are; the latency target sets the headroom, and a staged rollout, on-demand capacity, rate limits and a waitlist cover the rest |
| Gave the structure before the number | 2 | Size it, check it against history, set capacity to the latency target, say what would move it |
| Total, of 14 | 14 | |

## How do the [D] answers score?

Used in the fallback (part 4, S13, 25 minutes): read in pairs, played, then scored.

| Criterion | Weak | Hire-grade | The hire-grade line that earns it |
|---|---|---|---|
| Clarified the scope | 0 | 2 | Plus 4 and plus 22 against which weeks; which forecast met unseen weeks and which never met a festival; who carries a short week |
| Named the hidden weeks and the unit | 0 | 2 | Thirteen hidden weeks in shipments, and 2025's festival back-tested from 22 September 2025 with the growth flagged: 58,250 against 10,575 with none added, 4,034 with the growth measured later |
| Saw the paradox | 0 | 2 | Finance's rule ties on the hidden weeks because they hold no festival; the vendor's misses are cheap because they run high; and the plan sits within 1 percent of the vendor's eight-week total, 12,819 shipments, so the dispute is which weeks, 291,183 more across 19 October to 2 November |
| Sized it with a unit | 0 | 2 | 20,275 shifts, 3,719 at the peak; 3,082 shifts and about Rs 20.0 lakh over finance's rule; 3,413 to 3,906 shifts needed at the peak week's extremes |
| Said what would change their mind | 0 | 2 | The vendor forecasting 2025's festival from data to September 2025 before Friday; a sale at a different distance from Diwali; a first sale week outside the hidden weeks' range |
| Tied it to a decision and its cost | 0 | 2 | The plan's range priced at its ends, about Rs 2.0 lakh of idle shifts or Rs 5.6 lakh of late shipments for the peak week, and both sides of finance's choice: Rs 20.0 lakh more, against about Rs 103.6 lakh if finance's plan meets the rush |
| Gave the structure before the number | 0 | 2 | Restate, answer, concede, what would change it, then the plan, its cost, its range and the people |
| Total, of 14 | 0 | 14 | |

**Where the weak answer loses everything.** "Plus 13 percent" is a midpoint of two calendar copies, so
its peak stays on 5 October; percent is no unit for a shift plan, and "machine learning should beat a
rule of thumb" never tests either forecast.

## How do pairs run the mock round on Saturday?

The asker reads one question from either transcript and one follow-up from its table, scores the
answer on the seven criteria above, then the pair swaps. A pair that finishes early takes the AI
variant.

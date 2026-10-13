# How does a strong candidate answer "how do you evaluate a forecast?", and the dispute that follows it?

Written for this programme in the style of product-company and GCC screens; the facts inside are
from the case file. A screen is an interview round, and a GCC, a global capability centre, is a
multinational company's own technology and analytics centre in India. The numbers are Friday's
Flipkart case at the Lucknow fulfilment centre. Illustrative case: the company is real, the
situation and the data are synthetic, built for this class. In a real screen, say so in your first
sentence ("in a forecasting exercise on synthetic data for a fulfilment centre"), so nobody takes
the numbers for the company's own.

**Who needs the answer.** You, before any analytics, data-science or AI-startup screen that asks
about forecasts, capacity or planning. The interviewer is deciding whether you test a forecast on
weeks it never saw before you trust its story.

**The questions on the way.**

- Which words does an interviewer expect, and what did this class call them?
- What does the interviewer say, and which clarifying questions come first?
- What structure carries the answer, and which trap is being fished for?
- How do a weak and a hire-grade answer compare?
- What follows up, and which line answers each?
- How does the same question come up at an AI company?
- What does the second transcript, the dispute, ask?
- What does the scorer listen for?

## Which words does an interviewer expect, and what did this class call them?

Use the field's word in the room; the class's word is how you remember it. The last two rows, the
plan share and the quantile loss, go beyond Friday's five topics: the fallback hour and notebook 07's
depth section teach them, and a strong candidate reaches for them only after the four moves land.

| The field's word | What this class called it | What it means |
|---|---|---|
| Seasonal naive baseline | The house bot | A copy of the same week last year |
| Naive baseline | Naive | A repeat of the last week seen |
| Hold-out, or test set | The hidden weeks | The latest weeks, kept out of every rule's forecast and used to score it |
| Typical miss, with a range | The error bar | Festival-aligned's average miss on unseen weeks, 6,615 a week; 5 of the 13 hidden weeks missed by more, so the lowest-to-highest range answers "how wrong could it be" |
| Forecast origin | The week we forecast from | The last week a rule may see |
| Forecast horizon | How far ahead the plan reaches | The farthest week ahead the forecast must reach: ten here, from 21 September to the week of 30 November |
| Rolling-origin back-test, or time-series cross-validation | Rolling the origin | Forecasting again from many origins, each scored on the weeks after it |
| Newsvendor critical ratio, beyond the row | The plan share, 0.82 | Late cost over late plus spare cost: the share of weeks a plan should cover |
| Quantile loss, or pinball loss, at 0.82, beyond the row | The misses priced | Each miss priced by its direction; at Rs 25 late and Rs 5.42 spare it is the quantile loss at 0.82, in rupees |

## Transcript 1: "How do you evaluate a forecast?"

It is tagged [S], a staple asked everywhere, and it is the ladder's last rung, L6: the day's method said in an interview.

### What does the interviewer say?

> "A fulfilment centre has two years of weekly shipments and three forecasts for the coming festive
> season. How do you evaluate a forecast?"

### Which clarifying questions does a strong candidate ask first?

1. "What decision does the forecast feed, and how far ahead must it reach?" The answer sets the
   test's length: shifts for the eight weeks from 12 October to 30 November 2026 are booked from data
   that ends on 21 September, so the forecast reaches ten weeks ahead.
2. "What does a miss cost in each direction?" The answer sets the price: Rs 25 for a late shipment,
   Rs 650 for an idle shift of 120 shipments, so Rs 5.42 for each spare one.
3. "Does the festival fall on the same week every year?" It does not: Diwali moved one week earlier in
   2025 and moves two weeks later in 2026, and the sale moves with it.
4. "Has any of the three been scored on weeks it never saw?" The answer says whether the evidence is a
   fit or a forecast.

### What structure carries the answer?

1. Fix the measures before scoring anything: the average miss in the business's unit, and the same
   misses priced by direction, which is the loss this plan pays.
2. Hold out the latest weeks as the test set, at least as many as the forecast must reach ahead, and
   forecast them from one origin; then roll the origin, since one origin is one draw.
3. Score every forecast against the simplest baselines: the naive and the seasonal naive.
4. Set the plan's level from the two costs, the newsvendor share, and check how often it covered.
5. Name what the test cannot see, and test that another way.

### Which trap is the interviewer fishing for?

The candidate judges by fit ("the model matches two years within 2 percent"), picks the measure after
seeing which forecast it favours, or splits the difference between two forecasts. Each sends an
untested number to the plan.

### How do a weak answer and a hire-grade answer compare?

| | Weak answer | Hire-grade answer |
|---|---|---|
| Said first | "I would train a few models and see which does best." | "Five steps: the test, the measure, the bar to beat, the price, and what the test cannot see." |
| The test | "I would split the weeks 80 to 20 at random, train each model on the 80 and score it on the 20." A random split lets a model learn from weeks that come after the ones it forecasts. | "I hold out the latest thirteen weeks as the test set and forecast all of them from one origin, 22 June. The plan's last week is ten weeks past the data, so thirteen covers the reach." |
| The measure | "RMSE or MAPE, whichever comes out lowest." | "Two, fixed before anyone scores: the average miss in shipments, because shifts are booked in shipments, and the same misses priced at Rs 25 late and Rs 5.42 spare, because that is what this plan pays." |
| The bar to beat | "The vendor's model fits within 2 percent, so it is probably the best." | "The seasonal naive, a copy of the same week last year, misses by 9,831 a week and festival-aligned by 6,615; on these weeks festival-aligned is that copy plus 4 percent, so the gap is the growth. The vendor's curve fits its past within 1.4 percent and misses by 16,400, almost all of it bias that grows with the weeks ahead, the mark of a wrong trend." |
| The price | Not reached. | "Priced as they stand, the vendor's misses cost least, only because it runs high, the cheap side. So the plan books festival-aligned at the forecast, 19,760 shifts, and prices its error bar both ways. One step further, beyond the row: moved each to its own 0.82 point, festival-aligned costs Rs 8.8 lakh, the seasonal naive the same and the vendor Rs 10.0 lakh, so these weeks rule out the vendor and cannot rank my rule above the copy of last year." |
| What the test cannot see | Not reached. | "It cannot see the festival, since the hidden weeks hold none, so I back-test 2025's: the calendar copy missed by 58,250 a week and festival-aligned by 4,034, or 10,575 without the growth measured later. I would roll the origin through that festival before trusting the festive error. Shipments are also only what the centre packed, and the 2025 peak ran on overtime, so demand may have been capped." |
| What would change it | Not reached. | "A sale that opens a different distance before Diwali, which re-lines the weeks; a first sale week outside the range the hidden weeks ran, which re-opens the plan; and overtime that absorbs a short week, which makes a short week cheaper." |

**The answer most candidates give** sits between the two columns: "I would hold out the last couple of
months, compare each model's MAPE with a copy of last year's same weeks, and send the lowest." It keeps
time order and a baseline, which most weak answers lose, and it misses the measure that matches the
plan, the price of each direction and the festival the test cannot see. It scores 2 of 14 on the card.

### What follows up, and which line answers each?

| Follow-up | The hire-grade line |
|---|---|
| "MAE in shipments or MAPE in percent, and when?" | "MAE in shipments when the cost is per shipment and the plan books shipments. To compare centres of different sizes I would use MASE, each miss scaled by the seasonal naive's average miss in training, since the series has a yearly season, or WAPE, the total miss over the total shipped. MAPE explodes when an actual sits near zero, and for the same miss it scores a forecast above the actual worse than one below, since the percent is taken of the smaller number. On these thirteen weeks no actual sits near zero and MAPE ranks the rules as MAE does, so here it changes nothing; at a store with near-zero days it would (Forecasting: Principles and Practice, section 5.8, checked 12 October 2026)." |
| "Suppose the festival moves by three weeks this year. What breaks?" | "Every calendar copy, the seasonal naive and finance's rule, puts the peak three weeks off, the way it put this case's peak two weeks off. A copy by distance from the festival moves with it. I would also check that the sale still opens the same distance before the festival, since the peak follows the sale; if it moves, I copy by distance from the sale." |
| Beyond the row: "You set the cushion on the weeks you scored. Isn't that circular?" | "Yes, and each forecast was tuned the same way, which is why I compare them each at its own 0.82 point; how much the tuning flatters each depends on its own misses. With thirteen weeks the point is loose: read by another common convention it is 4.1 percent instead of 2.6. The cure is a rolling origin: from 29 September 2025 every week has a year behind it, so the copies can be forecast from many origins, 2025's festival included, and the cushion set on weeks the final test never touches." |
| "In your peak week, 1,638 of 3,485 shifts were overtime. What does that do to your plan?" | "The data say overtime carried the 2025 peak, so first I would ask what an overtime shift costs and whether any orders missed their dispatch date, since a capped peak makes every copy of it run low. If overtime can absorb a short week, being short costs only the overtime premium: at one and a half times a shift's cost the share to cover falls to 0.33, at twice it is 0.50, so the plan would sit at or below the forecast. The 0.82, a step beyond the row, holds only while a short shipment is truly late." |
| "What did forecast error cost Zillow, and which guardrail failed?" | "Zillow Offers bought homes to resell, which needed price forecasts three to six months ahead, and it set a public guardrail on its unit economics, what it made or lost on each home, of plus or minus 200 basis points, 2 percentage points, around breakeven. Its forecasts missed in both directions by far more than it had modelled, and unit economics swung about 1,200 basis points, 12 percentage points, to an expected minus 500 to minus 700 in the fourth quarter of 2021. It also bought more homes than planned and ran short of renovation capacity. It wrote down about USD 304 million of homes bought above what they would now sell for, wound the business down and cut about 25 percent of its workforce (Zillow's Q3 2021 shareholder letter, checked 12 October 2026). The guardrail sat on the margin, which suggests the price forecast's error three to six months out was wider than the whole band. And a price forecast used to bid wins most where it guesses high, so the homes Zillow bought carried its errors one way: the letter says it bought homes 'at higher prices than our current estimates of future selling prices'." |

### How does the same question come up at an AI company?

> "We launch a new assistant feature in six weeks. How do you forecast inference demand for launch
> week, and how do you know the forecast is any good?"

The strong candidate clarifies first: "Demand in what unit: requests open at once at the peak, and
how many prompt and answer tokens each? What latency must a user get? How long does it take to add
capacity, and what can stretch within minutes? What does a timed-out request cost us, and what does a
GPU cost for the whole booking? Has this feature, or one like it, launched before?"

Then four steps:

1. **Size it from the ground up.** Say 2 lakh users at launch, 1 percent of them sending a request in
   the peak minute, each request 1,000 prompt tokens and 500 answer tokens (all invented): 2,000
   requests a minute, about 33 a second, carrying 20 lakh prompt tokens and 10 lakh answer tokens a
   minute. At 10 seconds to stream an answer, also invented, about 330 requests are open at once.
   Prompt and answer tokens load a GPU differently, so a load test at the latency target, run on this
   mix, says how many open requests one GPU holds: at 20 (invented), that is about 17 GPUs before
   headroom. Check the placeholder too: if the peak minute runs five times the average, each user sends about 3 requests
   a day, which the product team can confirm.
2. **Check it against history, if there is any.** Line earlier launches up by days from launch day
   for the launch curve, and keep the day of the week for the weekly cycle, since four days after a
   Tuesday launch is a Saturday: the forecast needs both. The copy to beat is the last launch's curve
   scaled by user growth. That curve looks like a forecast, and it is not one until it has predicted a
   launch it never saw, scored by its miss in prompt and answer tokens at the peak minute. With one earlier launch, or
   none, the forecast is untested; say so, and rely on the ground-up size and a similar feature's
   launch.
3. **Set capacity to the latency target, with headroom.** Waiting time climbs steeply as machines
   near full, so the latency target sets how much spare room each minute needs. Book one more GPU in
   advance when the timeouts it would prevent across the busy minutes cost more than its rent for the
   whole booking, the same two-cost arithmetic as the packer shifts, set per machine.
   What stretches covers the rest: a staged rollout to a share of users first, on-demand capacity,
   rate limits and a waitlist.
4. **Say what would move it.** Waitlist sign-ups before launch and the first hour's requests after
   it: if either runs past the ground-up size, the stretch capacity takes the load while more
   is booked.

This variant is written for this programme and quotes no company's figures.

### Which pain points hide inside the question, each with a real case?

| Pain point | The case | The check |
|---|---|---|
| A close fit taken for a good forecast | A 2018 PLOS ONE paper by Makridakis, Spiliotis and Assimakopoulos, on 1,045 monthly series, recalls the forecasting competitions' finding that the models that best fitted the data "did not necessarily" forecast better, and found the machine-learning methods it tested beaten by statistical ones at every horizon it examined, on single monthly series. The M5 competition turned that round on tens of thousands of related daily series with prices and calendar events to learn from: all 50 of its top methods were machine learning, ahead of every statistical benchmark (the M5 accuracy paper, checked 12 October 2026). The data decides which family wins. | Score every model, of either family, on weeks it never saw, against the seasonal naive |
| A forecast with no history | Target Canada: its forecasting and replenishment system needed years of sales history the new stores did not have, so buyers relied on optimistic projections from headquarters, and the item data feeding the system was right about 30 percent of the time. Stores sat barely stocked while distribution centres overflowed, and Target closed all 133 stores, with about 17,600 employees (Canadian Business, "The Last Days of Target"; Target's release of 15 January 2015; both checked 12 October 2026) | With no history, size from the ground up and from a similar launch, and keep capacity that can stretch |
| Price-forecast swings that overran a margin guardrail | Zillow, 2021, above | Size the forecast's error at the horizon the decision needs, and compare it with the margin before committing |
| A calendar week taken for a festival | FADA counts its festive window from the festival each year, 42 days from the first day of Navratri (FADA's release of 7 November 2025, checked 12 October 2026) | Line years up by distance from the festival |
| A model never compared with the simplest baseline | Amazon Science's history of its recommendation algorithm (Larry Hardesty, 22 November 2019): a Prime Video deep-learning recommender first lost to a plain bestseller list; retrained on viewing data in time order and tested on the two weeks after its training cutoff, it beat the list, and beat the older item-to-item method two to one (checked 12 October 2026) | Put the simplest baseline on every scoreboard, and test on the weeks after the training data |

## Transcript 2: when finance and the vendor's sponsor each want their forecast in front of the plan, which goes?

It is tagged [D], a differentiator, and the fallback hour runs it after part 3, the plan quantile,
which goes beyond Friday's five topics. Its numbers use that hour's raised plan, festival-aligned plus
2.6 percent, 20,275 packer shifts; the day itself books 19,760 at the forecast.

### What does the interviewer say?

> "Finance wants last year plus 4 percent; the vendor's sponsor wants the curve at plus 22. Both are
> senior to you, and the plan is due Friday. What do you put in front of the regional operations
> head, and how do you present the error?"

### Which clarifying questions does a strong candidate ask first?

1. "Plus 4 and plus 22 against which weeks of last year?" Both are measured against the same calendar
   weeks, which hold only the tail of last year's festival.
2. "Has either been scored on weeks it never saw?" Both met the thirteen hidden weeks. Finance's rule
   also met 2025's festival in the back-test; the vendor's file holds no forecast of any festival, so
   its festive promise has never been tested.
3. "Who carries the cost of a short week, and who of a spare shift?" The answer says which way to
   lean.

### What structure carries the answer?

Make the four moves from Tuesday (restate, answer from the evidence, concede what is true, say what
would change your mind), then give the plan with its cost to finance, its range in each direction, and
the check that re-opens it.

### Which trap is the interviewer fishing for?

The candidate splits the difference, 13 percent between 4 and 22, or sides with the more senior
person. Both skip the evidence, and the midpoint keeps the calendar copy's peak on the wrong week.

### How do a weak answer and a hire-grade answer compare?

| | Weak answer | Hire-grade answer |
|---|---|---|
| Restate | "The vendor's model is machine learning, so it should beat a rule of thumb." | "Finance wants a rule it can explain, and the sponsor wants a model that fits history closely; both want the plan to hold in the festival." |
| Answer | "Go with the vendor, trimmed toward finance to keep the peace: plus 13 percent." | "Neither goes to the plan as it stands. On the hidden weeks finance's rule ties festival-aligned and the vendor misses by 16,400 a week; on 2025's festival, with no growth added to either, a calendar copy missed by 58,250 a week and festival-aligned by 10,575, or 4,034 with the growth measured later. So the plan is festival-aligned plus 2.6 percent: 20,275 packer shifts." |
| Concede | Nothing conceded. | "To finance: your 4 percent is the growth the training weeks show, and your rule ties ours on the hidden weeks. To the sponsor: over the eight weeks your curve and our plan sit within 1 percent of each other, 12,819 shipments apart, and your misses run to the cheap side. We differ on which weeks: our plan books 291,183 more than your curve across 19 October to 2 November and less in the weeks around them." |
| The cost to finance | Not said. | "The plan books 3,082 more shifts than finance's rule would, about Rs 20.0 lakh at Rs 650 a shift. If the rush lands where festival-aligned puts it, finance's own plan costs about Rs 103.6 lakh in idle shifts and late shipments." |
| The error | One number. | "For the peak week, 19 October, the plan books 3,719 shifts. If demand lands where the hidden weeks' lowest and highest misses would put it, the week needs 3,413 to 3,906 shifts: at the low end about Rs 2.0 lakh of idle shifts, at the high end Rs 5.6 lakh of late shipments. The range of thirteen misses covers roughly six weeks in seven, and misses from one origin move together and include no festival, so the true range is wider." |
| What would change it | Not said. | "A sale that opens at a different distance from Diwali, or the curve beating the seasonal naive on a festival it never saw: I would ask the vendor to forecast 2025's festival from data to September 2025, which can be done before Friday. Once the season starts, a first sale week outside the hidden weeks' range re-opens the plan." |
| The people | Not said. | "I would show each of them the back-test before the meeting, so neither hears it first in front of the operations head, and bring the options with their costs." |

### What follows up, and which line answers each?

| Follow-up | The hire-grade line |
|---|---|
| "Why not average the two and keep both happy?" | "Averaging forecasts usually helps when their errors are independent. These two both put the peak on 5 October, two weeks before the rush, so their average keeps that error, and averaging either with a forecast that places the festival elsewhere would smear the peak across the wrong weeks." |
| "Finance says its rule tied yours. Why not use finance's?" | "On the hidden weeks it did tie, because those weeks hold no festival. On 2025's festival, forecast from 22 September 2025, finance's rule missed by 60,488 a week against festival-aligned's 4,034; even without the growth, festival-aligned's 10,575 is less than a fifth of finance's miss." |
| "The sponsor says the vendor's misses cost least. Answer that." | "As they stand, yes: Rs 11.9 lakh against Rs 13.5 lakh, because it runs high and nobody chose how far. Move each forecast to its own 0.82 point on the same weeks and the comparison is fair: festival-aligned costs Rs 8.8 lakh, the vendor Rs 10.0 lakh. Both were tuned on the weeks they are scored on, so the gap is the evidence and both levels flatter a little." |

## What does the scorer listen for?

When you practise in pairs, the asker scores each of these from 0 to 2: clarified the scope; named
the hidden weeks and the unit; saw the paradox (a close fit, or cheap misses, that do not earn the
plan); sized it with a unit (shipments, shifts or rupees); said what would change their mind; tied
it to a decision and its cost; gave the structure before the number. A 2 also survives the obvious
technical follow-up: a test that never lets a model see the future, a measure that matches what the
decision pays, and an honest range.

Carry four numbers into a real screen and let the rest come out only when asked: the test's length,
the seasonal naive's miss, the winner's miss, and the misses priced in each direction. A string of exact figures sounds rehearsed; four that you can explain sound like work you did.

## Where are the sources?

- Forecasting: Principles and Practice, sections 5.8 to 5.10, on accuracy, quantile scores and the rolling origin: https://otexts.com/fpp3/toolbox.html#sec-accuracy, with the anchors #sec-distaccuracy and #sec-tscv (checked 12 October 2026)
- Zillow's Q3 2021 shareholder letter: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm (checked 12 October 2026)
- Makridakis, Spiliotis and Assimakopoulos, PLOS ONE, 2018: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0194889 (checked 12 October 2026)
- The M5 accuracy competition paper, preprint: https://statmodeling.stat.columbia.edu/wp-content/uploads/2021/10/M5_accuracy_competition.pdf (checked 12 October 2026)
- Canadian Business, "The Last Days of Target", archived: https://www.gwern.net/docs/www/archive.canadianbusiness.com/edd0ae069905e7df1b073ae02516993a2bf4a1b9.html (checked 12 October 2026)
- Target's release of 15 January 2015: https://corporate.target.com/press/release/2015/01/target-corporation-announces-plans-to-discontinue-canadian-operations (checked 12 October 2026)
- FADA's release of 7 November 2025: https://fada.in/images/press-release/1690d68d7a2e6cFADA%20releases%20October%202025%20&%2042-Days%20Festive%20Vehicle%20Retail%20Data.pdf (checked 12 October 2026)
- Amazon Science, "The history of Amazon's recommendation algorithm": https://www.amazon.science/the-history-of-amazons-recommendation-algorithm (checked 12 October 2026)

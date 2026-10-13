# Can you make the day's eight forecasting calls at speed?

This page is the answer sheet, read after the live quiz, which shows each question without its mark.
The quiz has eight items, ungraded and scored on correctness and speed together, with twenty seconds
each and forty for the priced miss in item 7. Seven test the day's five topics, at least one item
each, and one is the return question from Thursday. Each item's Tests line names the topic as the
curriculum words it, so an item dropped for time says what was lost. Two words used below: the house
bot is the seasonal naive at Flipkart, the rule that copies the same calendar week a year back, and
the hidden weeks are the weeks kept out of every forecast so it can be scored on them.

Today's case: Flipkart's Lucknow fulfilment centre must book packer shifts for the eight festive
weeks beginning 12 October to 30 November 2026, with a vendor's forecast 22 percent above last year
and finance's rule at 4 percent. Illustrative case: the company is real, the situation and the data
are synthetic, built for this class. The chai stall in item 8 is invented, as every number about it is.

**Who needs the answer.** The trainer needs it to close the day, and every learner needs it before
Saturday's paper. An item most of the room misses is a call likely to reach the regional operations
head wrong, so the trainer says it again before the room leaves.

**The questions on the way.**

- Which week does a copy of last year use for Diwali 2026's week?
- Which error does each reader need?
- What does a close fit prove?
- What is "good enough" a claim about?
- Which weeks are hidden, and how many?
- How does a flat blend sit over falling cohorts?
- What does the same miss cost, short and over?
- Which comparison reads growth?

---

## Q1. Diwali 2026's week begins 2 November 2026: which 2025 week does the same-week-last-year rule copy into it?
*Tests: Naive, seasonal naive and drift baselines: the house bot's copy is a calendar week, and the festival moved.*

- 20 October 2025, Diwali 2025's own week
- 3 November 2025, two weeks after Diwali  <- correct
- 6 October 2025, the busiest week of 2025
- 27 October 2025, the week after Diwali

---

## Q2. The planner books shifts, and a director compares Lucknow with a centre twice its size: which error does each read?
*Tests: Holding out; MAE and MAPE in the business's units: shipments or percent, and when each.*

- The planner MAE in shipments, the director MAPE in percent  <- correct
- Both MAPE in percent, since a percent is easier to say aloud
- Both MAE in shipments, since a percent divides by the actual
- The planner MAPE in percent, the director MAE in shipments

---

## Q3. A vendor's curve sits within 2 percent of every week it was fitted to: is it a good forecast?
*Tests: Beating the baseline; the vendor curve tested: fit mistaken for forecast, the day's trap.*

- Yes, since a fit that close beats every simple rule
- Yes, if the fit also holds on the festival weeks
- Unknown until it is scored on weeks it never saw  <- correct
- No, since a fit that close is always overfitted, copying noise

---

## Q4. "This forecast is good enough": what is that sentence a claim about?
*Tests: The good-enough call and the forecast note: good enough as a claim about the decision.*

- The model, once it beats every rule on the hidden weeks
- The data, once two years of weeks are on the table
- The vendor, once its contract carries a refund clause
- The decision: would a better forecast change it?  <- correct

---

## Q5. The plan's last week is ten weeks past the data: which weeks do you hide from every forecast before scoring?
*Tests: Holding out; MAE and MAPE in the business's units: the hold-out sits at the end and spans the horizon.*

- A random fifth of all weeks, so every season is tested
- The latest weeks, as far ahead as the plan reaches  <- correct
- The festival weeks, since they matter most to the plan
- The first weeks, so the model learns from the newest data

---

## Q6. From Thursday: blended retention stays flat while every signup month's own retention falls. What is the mechanism, in one sentence?
*Tests: Thursday's blend as a size-weighted average, the return question.*

- The mix shifts toward big young cohorts at their best months  <- correct
- Members who leave stop being counted, so only loyal members remain
- Heavy members order more often, so their orders hold the rate flat
- The dashboard rounds every month to a whole percent, hiding the fall

---

## Q7. Two plans each miss the busiest week by 6,615 shipments, one too high and one too low; a late shipment costs Rs 25 and a spare one Rs 5.42: what does each miss cost?
*Tests: Holding out; MAE and MAPE in the business's units: the same miss, short or over, priced.*

- The same, since both misses are the same size in shipments
- High about Rs 35,800, low Rs 1.65 lakh  <- correct
- High Rs 1.65 lakh, low about Rs 35,800
- Neither can be priced from a miss in shipments alone

---

## Q8. The stall (invented) sold 100 cups on Monday and 60 on the Sunday before: which comparison reads whether it is growing?
*Tests: Trend and seasonality, read before modelling: growth is read a season apart, never between neighbours.*

- Monday over Sunday: up 67 percent
- Monday against last Monday, or a year apart  <- correct
- Sunday against the Saturday just before it
- The fortnight's mean against Monday's 100 alone

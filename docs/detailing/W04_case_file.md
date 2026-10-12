# Week 4, Analyst craft: the case file

Written 12 October 2026 for the Week 4 build. On approval this page becomes
`docs/detailing/W04_case_file.md`, and every day session builds its case from the section below for
its day; the spine (`W04_analyst_craft_spine.md`) says how the day is shaped, and this page says what
it is about. A day session may sharpen a case (a column name, a zone name, a sentence of the ask) and
records the change in its sources list; it may not change a target number without the orchestrator,
because the explorer, the Saturday paper and the other days read these numbers.

**Three rules this page is built on.** Every case is an illustrative case: the company is real, the
situation and the data are synthetic, built for this class, and that sentence opens every case in
every learner file. A public fact about a company comes only from `docs/detailing/W04_research_cases.md`
with its id (M1 to M9, T1 to T3, W1 to W6, Th1 to Th6, F1 to F6, and the interview table's item numbers)
and R2's check date of 12 October 2026, or from a primary source the builder fetched and dated; a
finishing session re-fetches every URL it uses on its day and re-dates it, and a URL that fails reads
"not verified on <date>" and leaves the learner files. Nothing in a case says the company did or
suffered the situation. Every number below that is not a public fact or a toy is a target the day's
generator sets and asserts, and the facts file is the only home a learner file may read it from.

**The register of a ticket.** Company, city and surface; the metric before and after with dates; the
data as tables and columns; the ask with its date; the known caveats; the label line. The ticket is
written for an analyst who has been at the company three weeks: plain, specific, no adjectives.

**The ladder, restated.** L1 understand and count by hand on twelve rows; L2 compute on the full data
in the smallest code; L3 the trap, the denominator, the segment; L4 the caveats and nuances; L5 the
decision with its cost and the stakeholder's objection; L6 interview depth with an AI-company variant.
Each sub-problem below carries: the concept it needs, its everyday analogy, a worked micro-example,
the numbers to target, the trap, what the interviewer listens for and the common wrong answer.

---

## Monday: Uber, Hyderabad. Is the number the scheme pays for measuring what the city wants?

### The ticket

**Uber, Hyderabad, the driver app's peak-hour earnings guarantee (illustrative case: the company is
real, the situation and the data are synthetic, built for this class).**

On Monday 31 August 2026 the Hyderabad city team launched a peak-hour earnings guarantee for enrolled
drivers: a driver who stays online through a whole weekday peak window (two windows a day, each three
hours long, set by the city team) is guaranteed a floor of Rs 300 per peak online hour, and Uber pays
the gap between the driver's trip earnings in the window and the floor as a top-up (the terms are
synthetic). The goal written in the launch note was "more drivers on the road at peak, so riders are
picked up faster".

Six weeks after launch (the weeks beginning 31 August to 5 October 2026) against the six weeks before
(20 July to 24 August 2026):

| Measure | Before | After | Change |
|---|---|---|---|
| Peak online hours (all enrolled drivers) | 118,000 | 146,300 | up 24 percent |
| Completed peak trips | 224,200 | 230,900 | up 3 percent |
| Trips per peak online hour | 1.90 | 1.58 | 1.9 to 1.6 |
| Requests accepted over requests received, at peak | 0.86 | 0.73 | down 13 points |
| Trips cancelled by the driver after accepting, share | 0.04 | 0.09 | up 5 points |
| Peak online hours with no completed trip, share | 0.22 | 0.38 | up 16 points |
| Median rider wait at peak, minutes | 4.8 | 4.6 | barely moved |
| Peak requests that went unfulfilled, share | 0.11 | 0.10 | barely moved |
| Top-up paid | 0 | Rs 1.9 crore | |

All targets; the generator asserts each to the printed precision.

**Data the analyst has.**

| Table | Columns | Rows |
|---|---|---|
| `drivers` | `driver_id`, `home_zone`, `joined_month`, `enrolled` (in the guarantee) | 1,200 drivers, 140 of them joined after the launch |
| `driver_weeks` | `driver_id`, `week_start`, `zone_mode` (the zone where most online time was), `peak_online_hours`, `peak_offers` (every offer the driver saw; a declined request is offered again), `peak_accepted`, `peak_driver_cancels`, `peak_trips`, `peak_hours_no_trip`, `peak_bookings_rs`, `topup_rs`, `offpeak_trips` | twelve weeks for every driver active that week |
| `zone_weeks` | `zone`, `week_start`, `peak_requests` (rider requests, each counted once), `peak_fulfilled` (equal to the zone's completed trips), `median_wait_min` | 12 zones by twelve weeks; three outer zones get few requests at any hour |

Zones are named after Hyderabad localities for relatability (the generator picks twelve); the request
density is synthetic.

**The ask, due Friday, to the city head.** Is the scheme working? Which metric should it pay for?
Is anyone gaming it, and how would we know?

**Known caveats on the ticket.** The monsoon ended inside the after window. 140 drivers joined after
the launch. The app logs a driver as online whenever the driver app is open and the driver is marked
available, wherever the phone is. The three outer zones get few requests at any hour. Drivers can be
online on more than one platform at once, and Uber cannot see the other platforms.

### The twelve rows (L1)

Six drivers, one week before (the week of 10 August 2026) and one week after (the week of 21 September
2026). The generator chooses six real driver ids and writes the rows to the facts file under
`twelve_rows`; the shape to hit:

| Driver | Week | Peak online hours | Requests | Accepted | Trips | What the room should notice |
|---|---|---|---|---|---|---|
| A | before | 10 | 24 | 21 | 21 | an ordinary week |
| A | after | 11 | 25 | 22 | 22 | about the same |
| B | before | 9 | 20 | 17 | 17 | |
| B | after | 10 | 21 | 18 | 18 | |
| C | before | 11 | 25 | 22 | 22 | |
| C | after | 12 | 26 | 23 | 23 | |
| D | before | 10 | 22 | 19 | 19 | |
| D | after | 11 | 23 | 20 | 20 | |
| E | before | 10 | 21 | 18 | 18 | |
| E | after | 16 | 14 | 4 | 3 | hours up, requests down (an outer zone), most declined |
| F | before | 10 | 20 | 17 | 17 | |
| F | after | 14 | 12 | 3 | 2 | the same shape |

Hand count: hours 60 to 74 (up 23 percent); trips 114 to 88 (down 23 percent); trips per online hour
1.90 to 1.19. The twelve rows show the mechanism and not the city totals: two of the six sit in the
idle tail, a third of the sample against 15 percent of drivers city-wide, so the six fall much further
than the city's 1.90 to 1.58, and the city's trips rose 3 percent because 140 drivers joined. Both are
the first L4 caveat and are said on the slide. (Corrected on 12 October 2026: an earlier line printed
110 trips and 1.49, which the rows above do not sum to.)

### The sub-problems

**L1. What does "peak online hours up 24 percent" stand for, and what happened to the six drivers?**
Concept: a proxy, a number that stands in for the thing wanted. Analogy: a canteen pays servers per
token; tokens go from 200 to 400 a day while plates stay at 200, because each plate now gets two
tokens (toy, labelled invented). Micro-example: the twelve rows summed by hand. Numbers: 60 to 74
hours, 114 to 88 trips, 1.90 to 1.19. Trap: none yet. Interviewer listens for: the candidate restates
what the scheme is for (riders picked up faster) before touching a number, and names the unit (hours,
trips, trips per hour). Common wrong answer: "hours are up, so supply is up, so it is working."

**L2. What are the city totals, and what is trips per online hour, week by week?** Concept: a rate as
a ratio of two sums (Week 1 restated), never the mean of per-driver ratios. Micro-example: two drivers
at 2.0 and 1.0 trips per hour with 10 and 1 hours give 21 trips over 11 hours, 1.91, not 1.5. Numbers:
the table above; the twelve weekly values of trips per online hour (the facts file prints all twelve);
the same totals once more in SQL. Trap: "trips per hour fell because demand fell": `zone_weeks`
requests rose slightly (target). Interviewer listens for: the denominator named, the window named, the
second route. Common wrong answer: a mean of driver-level ratios.

**L3. Which drivers and zones drive the fall, and what number should the city team not have
celebrated?** Concept: the segment behind a rate; the mix. Micro-example: 100 drivers at 1.9 trips an
hour plus 20 new "online but idle" drivers at 0.2 bring the city to 1.6 with nobody's driving changed.
Numbers: an idle tail of 180 drivers whose peak online hours rose 2.1 times while their trips fell 12
percent, 70 percent of their new hours logged in the three outer zones; 61 percent of the top-up paid
to driver-weeks with acceptance under 0.5 (targets). The trap, exactly: "Peak online hours up 24
percent: supply target met" and the decision it misleads, a proposal to extend the scheme to two more
cities; the check, trips per online hour and rider wait unchanged; the fix, pay for completed peak
trips with an acceptance guardrail. Interviewer listens for: the candidate asks who controls the
count (the driver controls being online) before blaming anyone. Common wrong answer: "some drivers
are lazy", with no segment and no number.

**L4. What can the data not show, and what would settle each doubt?** Six caveats, each a one-line
check in the notebook: data quality (online means the app is open; the check is hours with zero
requests in zones with requests); mix (the 140 new drivers; the fall restated for drivers present in
both windows, target: the fall survives); seasonality (the monsoon ended; the check is the same
comparison for last year's weeks, which the data does not hold, so the caveat stays open and is
said); interference (drivers on two platforms decline Uber requests while online; the check is
acceptance by hour of day, with the catch that Uber cannot observe the other app); selection (who
enrolled; enrolled against not enrolled before launch); causality (the scheme or the season; only the
A/B test of the redesign, which is the faculty block's, can settle it). Interviewer listens for: what
the data cannot show and how to find out. Common wrong answer: naming "confounders" without one
check.

**L5. Which metric should the scheme pay for, what did the gamed version cost, and what do the three
roles say?** Concept: the north star, guardrails, leading inputs; a cost in rupees. Numbers: the
redesign's definition (the spine's section 5); the cost of the gaming, Rs 1.9 crore times 0.61, about
Rs 1.16 crore over six weeks paid to driver-weeks that accepted under half their offers (target); the saving under the redesign with a
labelled uptake assumption and its range. The three roles: driver operations ("drivers will log off;
supply at peak will fall": true for the idle tail, false for the honest majority, whose hours and
trips the facts file prints); marketing ("the guarantee is on every hoarding; changing terms six weeks
in looks like bait": true, which is why the redesign keeps the floor for drivers who accept); finance
("the fall in bookings per hour is the monsoon's end, not the scheme": partly, which the L4 cuts bound,
and the top-up budget is finance's number). Trap: "pay per completed trip" alone lets drivers
cherry-pick short trips; the acceptance guardrail catches it. Interviewer listens for: the number tied
to a decision and a cost, the objection conceded where true. Common wrong answer: dropping the
guarantee.

**L6. How would you measure the success of a new feature? And how would you measure an AI coding
assistant without rewarding accepted-but-deleted suggestions?** Structure: goal, user, one primary
metric with numerator, denominator and window, two guardrails, one leading indicator, how it would be
tested. The AI-company variant (programme-written, no company figure): the gamed proxy is suggestions
accepted; the outcome is suggested text still present at the next commit; the guardrails are build
failures, revert rate and time to merge; the gaming is short suggestions accepted and deleted; the
test is a holdout of users. Interviewer listens for: structure before the number, the trap seen, a
decision named. Common wrong answer: "acceptance rate, and we would survey the developers".

### Public facts allowed on Monday

| R2 id | Company | The fact, used how | URL (checked 12 October 2026) |
|---|---|---|---|
| M5 | Uber | Monthly Active Platform Consumers defined as unique consumers who completed a ride or received a delivery at least once in a month, averaged over the quarter; a trip counted per paying consumer; Uber One at 46 million members at 31 December 2025. Used on the role cards and in the definition's numerator | https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm |
| M8 | Wells Fargo | The CFPB's USD 185 million in 2016 penalties; the SEC's USD 3 billion settlement in 2020; the SEC order's five facts (no usage condition, debit cards up to four years unused, the silent 2013 addition, simulated funding, contact details changed). L1 and the fallback | https://www.consumerfinance.gov/about-us/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/ ; https://www.sec.gov/newsroom/press-releases/2020-38 ; https://www.sec.gov/files/litigation/admin/2020/34-88257.pdf |
| M8 | US Veterans Affairs | Wait time measured from a "desired date" that staff entered wrongly; the 14-day goal removed from performance contracts. L4 | https://www.vaoig.gov/sites/default/files/reports/2014-08/VAOIG-14-02603-267.pdf |
| M1 | Swiggy | The glossary: MTU, platform frequency, GOV with its denominators; platform frequency 4.53 in the quarter to 30 September 2024. L2's exhibit of a company that writes its denominators down | https://www.bseindia.com/xml-data/corpfiling/AttachHis/2495f39b-e1d1-4018-8f69-6ff250345e98.pdf |
| M9, W4 | Swiggy Instamart | Maxxsaver: over 28 percent of MTUs, AOV up 16 percent to Rs 612, slightly fewer orders per user. L5 | https://www.swiggy.com/corporate/wp-content/uploads/2025/07/Q1-FY2026-Shareholder-letter.pdf |
| M2 | Eternal | NOV = GOV minus discounts; GOV disclosure sunset. L5 | https://www.eternal.com/blog/q1fy27/ |
| M6 | Delhi Metro | 27 lakh ridership against 45 lakh line utilisation in 2018; 64.06 lakh journeys against 82,44,903 boardings in 2026. L3 | https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp ; https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ ; https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 |
| M4 | Airbnb | Nights booked net of cancellations went to minus 4.1 million in March 2020. Notes only | https://www.sec.gov/Archives/edgar/data/1559720/000119312520294801/d81668ds1.htm |
| M5 | Spotify | An MAU is an account with more than zero milliseconds of consumption in thirty days. Notes only | https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm |
| T2 | Aced | What interviewers score: structure, assumptions, scope first, the takeaway before the method. The scorecard | https://www.aced.io/blog/top-data-analyst-interview-questions |
| Interview table | Evan Miller | Peeking inflates false positives; fix the sample in advance. The handoff only | https://www.evanmiller.org/how-not-to-run-an-ab-test.html |

Not to be used: Wells Fargo firing counts, Goodhart's wording, the NHS examples inside Bevan and Hood
(R2, "Unverified, do not use").

### The guesstimate

None on Monday. Tuesday's drivers-at-peak question uses Monday's `zone_weeks` as its synthetic check.

### The Kalpa transfer

The lab's case: the head of Retail-Plus's "reorders per member", inflatable by auto-reorders (the
row). The Monday generator writes `app_reorders` (`reorder_id`, `customer_id`, `placed_ts`,
`product_id`, `value_rs`, `auto`, `status`: cancelled, merged into a later order, pending) for
Retail-Plus members over July to September 2026, with the auto-reorder window fixed at 10 to 30
September 2026 and the comparison at 20 August to 9 September 2026. Plants (TRAINER until the lab):
reorders placed per Retail-Plus member in the window over the comparison prints 1.22; booked revenue
per member (orders of any status) prints 0.96; the auto-reorders are low-value consumables, most
cancelled by members and the rest merged into the next manual order, so none is a separate delivered
order and v4's orders stay frozen. The lab's twelve rows: seven members with their orders and
placements in the two windows, values kept at least 0.05 from 1.22 and 0.96. If no window satisfies
both ratios with v4 untouched, the generator may re-date Retail-Plus orders within July to September
only, keeping every v4 contract line true, and says so in the facts file. The unguided exercise writes
Kalpa's growth-plan north star on the same template: delivered orders per active customer per month,
with revenue per active customer, discount share of booked revenue and the return rate as guardrails,
and add-to-cart events per active app member and new Retail-Plus sign-ups as leading inputs (the
bank's item 25 keys both as leading).

---

## Tuesday: Uber, Hyderabad, one day on. Can the redesign survive one slide, and how many drivers must be online at peak?

### The ticket

**Uber, Hyderabad, the same case (illustrative case: the company is real, the situation and the data
are synthetic, built for this class).**

The city head has asked for the redesign on one slide at the Thursday city review: five minutes,
with the driver-operations lead, the marketing lead and the finance partner in the room. Each loses
something under the redesign and each will say so. The number the slide must explain, because finance
will raise it first: gross bookings per peak online hour fell from Rs 314 in the six weeks before the
launch to Rs 260 in the six weeks after, while the average peak fare stayed at Rs 165 and online hours
rose 24 percent (targets; the arithmetic is Monday's 1.90 and 1.58 trips per hour times Rs 165, rounded
as the generator prints it). The same rupees read three ways: per online hour, down; per active
driver-week, up slightly, Rs 5,817 to Rs 5,861 (bookings grew 3 percent while active driver-weeks grew
2.2 percent; hours do not enter this ratio); per trip, flat.

In the afternoon a second ask from the city head: before the review, roughly how many drivers must be
online at the evening peak on a weekday to keep the median rider wait under five minutes. Fifteen
minutes, no dataset, assumptions stated.

Data: Monday's tables. Caveats: the three objections are each partly right; the peak window is three
hours long; the published figure a validate step would want does not exist in the research ledger.

### The twelve rows (L1)

Monday's twelve rows with `peak_bookings_rs` added, so the room reads the same rupees per online
hour, per driver-week and per trip and sees three different sizes of change: per online hour Rs 313.5
to Rs 196.2 (down more than a third), per driver-week Rs 3,135 to Rs 2,420 (down about a quarter), per
trip Rs 165 on both sides. On the full data at L2 the three point three ways: per online hour falls,
per driver-week rises slightly, per trip holds. (Corrected on 12 October 2026: the six rows' trips fall,
so no per-driver-week rise is possible on them.)

### The sub-problems

**L1. What is the one claim, and which number carries it?** Concept: the title is the claim; one
piece of evidence with its denominator. Analogy: a hostel notice board; "Breakfast survey results"
rewritten as a sentence a warden could act on (toy, R1). Micro-example: the cluttered slide of nine
Monday numbers rebuilt to one claim, one chart, one caveat, one action. Trap: "online hours up 24
percent" as the title (Monday's trap resold). Interviewer listens for: the claim first, the number
with its denominator, the caveat in plain sight. Common wrong answer: a title that is a topic ("Peak
guarantee: six-week review").

**L2. Which denominator does the slide use, and what do the other two say?** Concept: the
denominator is a choice and the slide says which. Numbers: Rs 314 to Rs 260 per online hour; per
driver-week up slightly, Rs 5,817 to Rs 5,861 on Monday's data (6,360 driver-weeks before, 6,500
after); per trip Rs 165 flat; the twelve-week series drawn cluttered, then clear
(the makeover notebook). Trap: reading the per-driver-week rise as the scheme working. Interviewer
listens for: the unit said aloud before the number. Common wrong answer: quoting the one that favours
the claim without saying so.

**L3. Which objection is partly right, and which part?** Concept: defence has a shape: restate until
the owner agrees, answer from the evidence, concede what is true, say what would change your mind.
The three objections and the true part of each are on Monday's L5. Trap: conceding nothing (the
Kahoot's false statement) or everything. Interviewer listens for: the concession made in the open,
the evidence named by line. Common wrong answer: repeating the claim louder.

**L4. What leaves the slide, and where does it go?** Concept: the appendix kept for a named
question. Micro-example: one appendix page per role, each headed by the question that role will ask.
Trap: a caveat moved to the appendix, where its owner finds it and calls the slide dishonest.
Interviewer listens for: what was left off on purpose and why. Common wrong answer: "I put
everything in the appendix".

**L5. How many drivers must be online at the evening peak, and is my number sane?** Concept: a
guesstimate is the same discipline without data: clarify, map, calculate, validate (the row's method).
Analogy: cups of tea the campus canteen sells on a weekday (toy, worked aloud first). The map for the
drivers question: peak requests an hour in the city, trips one driver completes in an hour, the share
of online drivers idle at any moment, a buffer for the wait target; the product is drivers online.
Validate: against the case's own `zone_weeks` (synthetic, labelled on the page) and against a
published figure the ledger does not hold, so the slot reads "to be found" and the finishing session
may fill it with a dated primary source or leave it as a labelled hypothetical. The paired question
against the clock: UPI transactions a day, mapped as active users times payments a day, validated
against 802 million a day in September 2026 (T3), with the catch that a 30-day month and a 31-day month
move the monthly total. Traps: a city of two million people given nine million households (the row's
Kahoot item); a validation in the wrong unit, Delhi Metro's boardings against journeys (M6); a
published number misread by a decimal, Flipkart's 6.3 million concurrent users beside a URL that says
63 million (T3). Interviewer listens for: scope pinned first, every assumption stated so it can be
challenged, the sanity check in the right unit, the takeaway before the method (T2). Common wrong
answer: a confident single number with no range and no check.

**L6. Present the redesign to a non-technical leader in two minutes; present an AI assistant's metric
change to a head of product who quotes acceptance rate in the sales deck.** Structure: claim, one
number with its denominator, the caveat, the action with its cost in rupees and weeks; the objection
"acceptance rate is what customers see in the deck" is partly right, and the answer keeps acceptance
as a leading input under the retained-text north star. Interviewer listens for: the loser could
repeat it accurately. Common wrong answer: method first, nine numbers.

### Public facts allowed on Tuesday

| R2 id | Company or source | The fact, used how | URL (checked 12 October 2026) |
|---|---|---|---|
| T1 | Barbara Minto | The pyramid: the answer first; the SCQ frame. L1 | https://www.barbaraminto.com/ |
| T1 | Storytelling with Data | The declutter makeover (4 January 2011) and the wordy slide makeover; the makeover index. L1 | https://www.storytellingwithdata.com/blog/2011/01/new-years-resolution-declutter-your ; https://www.storytellingwithdata.com/blog/a-wordy-slide-makeover ; https://www.storytellingwithdata.com/blog-summary-page-for-makeovers |
| T1 | Amazon | The 2017 letter: no slides, a six-page memo read in silence, a week or more to write. L3 and the written case | https://www.sec.gov/Archives/edgar/data/1018724/000119312518121161/d456916dex991.htm |
| T2 | Aced | What interviewers score in a guesstimate. L5 | https://www.aced.io/blog/top-data-analyst-interview-questions |
| T3 | NPCI through Outlook Money | 802 million UPI transactions a day on average in September 2026; 24.07 billion in the month. L5's anchor | https://www.outlookmoney.com/banking/upi-processes-2407-billion-transactions-worth-rs-2937-lakh-crore-in-september |
| T3 | Flipkart | 6.3 million concurrent users in a minute (9 October 2026) beside a URL slug that reads 63 million. L5's decimal trap | https://stories.flipkart.com/announcement/india-logs-on-for-the-big-billion-days-flipkart-records-63-million-concurrent-users-as-the-festive-season-opens |
| M6 | Delhi Metro | Boardings against journeys. L5's unit trap | URLs in Monday's table |
| T3 | DMart | FY26 standalone revenue Rs 66,968 crore; 85 stores added to reach 500; about Rs 134 crore a store on the year-end count, about Rs 146 crore on the average count (our arithmetic in R2). The Kalpa lab's anchor | https://nsearchives.nseindia.com/corporate/DMART_02052026173007_ASLPressRelease02052026.pdf |

Not to be used: the Think Insights and Management Consulted pages in the row (403 on 12 October 2026,
R2 "Not yet verified"); IGotAnOffer (not fetched). The four steps stay as the row's method.

### The guesstimate

| Question | Clarify | Map | Calculate | Validate | The catch |
|---|---|---|---|---|---|
| Drivers online at the evening peak on a weekday in Hyderabad (worked together) | Which window, which city, which wait target | Peak requests an hour, trips a driver completes an hour, the idle share, the buffer | The product, with each assumption said aloud | Against `zone_weeks` (synthetic, labelled); the published figure: to be found | The idle share is the assumption that moves the answer most; say so |
| UPI transactions a day (in pairs, seven minutes) | Volume, not value | Active users times payments a day, split person to merchant and person to person | The product | 802 million a day (T3) | A 30-day month against a 31-day month moves the monthly total; compare per-day figures |

### The Kalpa transfer

The lab: every learner presents Monday's Kalpa north star on one slide to a TA playing one Kalpa head,
three minutes, scored on the four moves; then Anand's store question from the row (how many customers
could a new store sign up to Retail-Plus in its first year), mapped as footfall a day, the share who
sign up, the first-year ramp, validated against DMart's revenue per store (T3) with the catch that a
first-year store sells less, which is why DMart reports two-year-old stores separately. No plant today.

---

## Wednesday: Swiggy Instamart, Pune. What goes with what beyond chance, and what is a strip slot worth?

### The ticket

**Swiggy Instamart, Pune, the cart page's "frequently bought together" strip (illustrative case: the
company is real, the situation and the data are synthetic, built for this class).**

The cart page shows a strip of three suggested items under the cart. Until 6 September 2026 the strip
was a curated list by category. On Monday 7 September 2026 it switched to ranking by how often an item
is found in the same cart as the items already in it, counted over the previous four weeks. Toned milk
is in 71 percent of Pune carts, so it now appears beside nearly everything. The strip's click-through
fell from 6.1 percent in the three weeks before the change to 3.8 percent in the three weeks after
(targets).

| Measure | Before (17 August to 6 September) | After (7 to 27 September) |
|---|---|---|
| Strip click-through (clicks over impressions) | 6.1 percent | 3.8 percent |
| Click-through on slots showing milk | 1.2 percent | 1.2 percent |
| Click-through on slots showing any other item | 6.2 percent | 6.4 percent |
| Share of slot impressions showing milk | 2 percent | 50 percent |

**Data the analyst has.**

| Table | Columns | Rows |
|---|---|---|
| `carts` | `cart_id`, `customer_id`, `placed_date`, `zone`, `time_band` (morning, afternoon, evening, night), `cart_value_rs` | 40,000 carts, 1 to 28 September 2026, eight Pune zones |
| `cart_items` | `cart_id`, `item`, `quantity`, `price_rs`, `margin_rs` | about 60 items in the catalogue |
| `strip_log` | `date`, `slot` (1 to 3), `anchor_item`, `suggested_item`, `impressions`, `clicks`, `adds` | daily |

**The ask, due Friday, to the category manager and the growth lead.** Rank the pairs the strip should
show, explain why the click-through fell, and put a rupee value on a strip slot.

**Known caveats on the ticket.** Curd was out of stock in two zones in the third week. The top tenth
of customers place 38 percent of carts (target). The strip itself causes part of the co-occurrence it
measures, since an item clicked from the strip lands in the cart. A cart is one order; a customer is
many carts.

### The twelve rows (L1)

Twelve carts with their items (the generator picks twelve real carts; the shape to hit): milk in 8 of
12; bread in 4, three of them with milk, so bread to milk confidence 0.75 and lift 1.13 (0.75 over
0.67); chips and cold drink in 3 carts each, together in 2, so support 2 of 12, confidence 0.67 and
lift 2.67; ice cream and chocolate sauce together in exactly one cart; curd, eggs, bananas, paneer,
coriander and others filling the rest. Every value at least 0.05 from Kalpa's 0.82, 0.97, 3.1 and 4.0
and from the case's own 0.74, 1.04, 3.4 and 4.6.

### The sub-problems

**L1. Which items go together on the twelve carts, and what does "together" mean?** Concepts, one
at a time: support is counting; confidence shrinks the world to the carts that hold A; lift compares
with chance; lift is symmetric. Analogy: ten tea-stall orders as dots: chai in 6, biscuit in 4, both
in 3; support 3 of 10, confidence 0.5, expected 10 times 0.6 times 0.4 = 2.4 against 3 seen, lift 1.25
both ways; a carry bag in 9 of 10 gives biscuit to bag confidence 0.75 and lift 0.83 (toy, R1).
Numbers: the twelve rows. Trap: confidence read as the answer. Interviewer listens for: the three
questions named (how often, how reliably, against chance). Common wrong answer: "confidence is the
probability they go together".

**L2. What are the three numbers for every pair across 40,000 carts?** Concept: the formula as the
shorthand of L1; `Counter` over `itertools.combinations`. Numbers (targets): milk in 71 percent of
carts; bread 34 percent, eggs 29 percent, curd 26 percent, bananas 23 percent, chips 12 percent, cold
drink 12.3 percent, ice cream 4 percent, chocolate sauce 1.36 percent; bread to milk confidence 0.74
and lift 1.04; eggs to milk 0.73 and 1.03; chips with cold drink support 5.0 percent, lift 3.4,
confidence 0.42 and 0.41; ice cream with chocolate sauce support 0.25 percent (100 carts), lift 4.6.
For every item with support of at least 2 percent, confidence toward milk lies between 0.68 and 0.78
and lift between 0.96 and 1.08. The second route: lift as observed over expected from confidence and
the base rate, asserted equal and symmetric. Trap: "the pairs table is the ranking" (it is the count
the strip already uses). Interviewer listens for: the base rate named. Common wrong answer: ranking by
support.

**L3. Why did the click-through fall, and which slots drive it?** Concept: the popularity trap; a
blended rate as a mix. Numbers: milk slots at 1.2 percent against 6.4 percent for every other
suggestion; half of the impressions showing milk; the blended 3.8 percent reproduced from the two
(targets). The trap, exactly: "click-through fell because shoppers' habits changed after the
monsoon"; the check is click-through by suggested item; the fix is rank by lift above a support floor.
Interviewer listens for: the blend decomposed before a cause is named. Common wrong answer: "the
strip needs a redesign".

**L4. What can the counts not tell us?** Six caveats with one check each: co-occurrence is no proof
of cause (party shoppers buy chips and cold drink together; a chips promotion sells no cold drink to
anyone else; the check is a holdout, which the block and Week 5 own); the heavy-buyer denominator (the
top tenth, 38 percent of carts; lift recomputed per customer rather than per cart, target: milk's lift
unchanged, the chips pair's lift lower); the stock-out (curd's pairs vanish in two zones in week three;
the check removes those zone-weeks); time-band mix (morning carts are milk-heavy; the check is lift by
time band); the strip's own feedback (an item shown is an item added; the check compares carts that
saw the strip with carts on the old app version, which the data marks); the base rate per cart against
per customer. Interviewer listens for: "lift says found together, nothing more". Common wrong answer:
"lift 3.4 means promoting chips raises cold-drink sales by 3.4 times".

**L5. Which three pairs fill the strip, where is the support floor, and what is a slot worth?**
Concepts: the action map (promote, watch, ignore, trap); the support floor; expected value in rupees
with its cost line. Numbers: a floor of 1 percent of carts (400 carts); the value of a slot: 60,000
cart-page views a day in Pune times click-through times an add rate of 0.5 times Rs 9 margin per
added item (the last two labelled assumptions with ranges, from `strip_log` and `cart_items`):
Rs 17,280 a day at 6.4 percent against Rs 3,240 a day at 1.2 percent, a gap of about Rs 4.2 lakh a
month per slot, Rs 12.6 lakh over three slots (targets); the thin pair on the watch list with the
reason (100 carts a month cannot repay a slot); the category manager's objection ("milk is the top
seller and anchors the cart": partly right, since milk belongs in the cart, which is why it needs no
slot). Trap: acting on lift alone; booking gross sales as the benefit with a discount's margin
forgotten. Interviewer listens for: incremental adds times margin, less the cost line, with the
assumption named. Common wrong answer: "promote the highest-lift pair".

**L6. Which measure cannot be fooled by popularity? And how do you evaluate an LLM shopping
assistant's add-on suggestions?** Structure: lift divides by the base rate, so a popular item cannot
inflate it; Amazon's bestseller example (W1); the heavy-buyer fix. The AI-company variant
(programme-written): an assistant that suggests milk is "accepted" often because milk is popular, so
it is scored offline by lift over a popularity baseline on held-out carts and online by a holdout;
the base-rate trap restated for a model. Interviewer listens for: the base rate, the baseline, the
holdout. Common wrong answer: "confidence", or "lift" without the base rate.

### Public facts allowed on Wednesday

| R2 id | Company or source | The fact, used how | URL (checked 12 October 2026) |
|---|---|---|---|
| W1 | Amazon | Counting how often buyers of A also bought B would make Harry Potter and trash bags the top recommendation for everyone; the fix is lift in spirit; years later the base rate had to be measured per purchase because heavy buyers inflate everything; a bestseller list beat a deep model in a Prime Video test. L1, L4, L6 | https://www.amazon.science/the-history-of-amazons-recommendation-algorithm ; https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf |
| W2 | Osco Drug, Teradata | 1992, about 1.2 million transactions, beer and diapers together in the early evening, no documented shelf move; the vivid version largely invented. L2, told as a legend with a true core; "early evening", never a clock time | https://www.theregister.com/2006/08/15/beer_diapers/ |
| M1, W4, T3 | Swiggy Instamart | Instamart AOV Rs 499 in the quarter to 30 September 2024; net AOV Rs 508 by the quarter to June 2026; 1,089 orders per dark store per day across 1,171 stores; Maxxsaver used by over 28 percent of MTUs, AOV up 16 percent to Rs 612, order counts down as carts consolidated, the discount described as margin returned to the user. The company facts of the case and L5's cost line | URLs in Monday's table and https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf |
| W4 | Uber | Consumers using both rides and delivery generated over three times the bookings of single-product consumers; about one in five eligible consumers active in both. L4: an outcome, no proof of cause | the Uber 10-K URL in Monday's table |
| W3 | Walmart | Strawberry Pop-Tarts shipped ahead of Hurricane Frances after sales rose about sevenfold before Charley. The fallback's bridge to Friday | https://openstax.org/books/principles-data-science/pages/1-2-data-science-in-practice ; https://www.newsweek.com/survival-turn-tart-138555 |
| W5 | Agrawal, Imielinski and Swami (1993); Brin and others (1997) | Where the measures come from. Notes only, metadata | https://api.crossref.org/works/10.1145/170035.170072 ; https://api.crossref.org/works/10.1145/253260.253325 |
| R1 3.2 | Practical Business Python | Lift stated correctly as observed over expected. The student reference | https://pbpython.com/market-basket-analysis.html |

Not to be used: the New York Times Hays article and Dillman quote; the Instacart dataset's licence
wording (R2 "Unverified"). IBM's Apriori page is a trainer-only audit item (R1 section 3.2).

### The guesstimate

Orders a dark store handles in a day: clarify (one store, one day, placed orders); map (catchment
households times the share ordering in a week times orders a week, over seven); calculate; validate
against Swiggy Instamart's 1,089 orders per dark store per day in the quarter to June 2026 across
1,171 stores (T3); the catch: Swiggy counts per active store-day, so a new store's days count only
once it is live.

### The Kalpa transfer

The lab's case: merchandising's proposal to pair everything with the Rs 199 phone charger "because it
is in 80 percent of baskets" (the row). The Wednesday generator writes `products` (`product_id`,
`name`, `category`, `list_price`, `unit_cost`; the charger at Rs 199) and `order_items` (`order_id`,
`product_id`, `quantity`, `unit_price`) for v4's 1,000 orders, every order's lines summing to
`orders.amount` exactly, consumer orders of one to about eight lines, Business orders one product in
bulk. Plants (TRAINER until the lab): the basket base is every consumer order with at least one line,
named with its count; the charger in 84 to 85 percent of those baskets, the exact share chosen so that
for the partner item the facts file names confidence toward the charger prints 0.82 and lift 0.97; for
every item with support of at least 2 percent, confidence toward the charger between 0.78 and 0.86 and
lift between 0.93 and 1.02; among pairs with support of at least 5 percent the strongest by lift prints
3.1 at support 6 percent with at least 70 percent of its baskets Retail-Plus; exactly one pair in two or
three baskets at lift 4.0 and support between 0.2 and 0.4 percent, its exact share printed. The lab's
twelve rows: twelve Kalpa baskets with values at least 0.05 from every plant. The unguided exercise:
the charger proposal costed and refused, the strongest pair costed with a labelled uplift assumption,
the thin pair on the watch list.

---

## Thursday: Zomato Gold, Chennai. Who is leaving, and at which step?

### The ticket

**Zomato Gold, Chennai, the membership and the app's order flow (illustrative case: the company is
real, the situation and the data are synthetic, built for this class).**

The membership dashboard reports month-two retention for Chennai as flat at 38 percent for the
reporting months June, July, August and September 2026 (blended: members active in the month over
members who signed up before it). Each signup cohort's own curve falls with age, and each successive
cohort's month-one rate is lower than the one before: January 2026, 58 percent; April, 53; July, 49;
August, 31 (targets). The August cohort was signed up in a sale week on a discounted first month and
is 2.6 times the size of a normal month's cohort. On Monday 14 September 2026 a new checkout flow
shipped on Android; since then members' add-to-cart to order conversion on Android fell from 58 to 44
percent, iOS stayed at 57, and non-members on Android stayed at 52 (targets).

| Measure | Value |
|---|---|
| Members signed up January to September 2026 | 60,000 |
| Normal cohort size | about 5,000; August 13,000 |
| Blended retention, June to September reporting months | 38 percent each month |
| Month-one retention by cohort, January to August | 58, 56, 55, 53, 52, 50, 49, 31 |
| Add-to-cart to order, members, Android, before and after 14 September | 58 to 44 percent |
| The same, members, iOS | 57 to 56 percent |
| The same, non-members, Android | 52 to 51 percent |
| Search to menu view, per session, September | 118 percent |
| Menu view to add-to-cart, per session and per member, September | 34 and 61 percent |

**Data the analyst has.**

| Table | Columns | Rows |
|---|---|---|
| `members` | `member_id`, `signup_date`, `cohort_month`, `signup_channel` (organic, sale), `zone` | 60,000 |
| `member_months` | `member_id`, `month`, `orders` | one row per member per month since signup |
| `events` | `member_id`, `session_id`, `event_ts`, `stage` (open, search, menu_view, add_to_cart, checkout_start, order_placed), `platform` (android, ios, web), `checkout_version` | September 2026 in full; August for comparison |

**The ask, due Friday, to the membership lead.** Is it a cohort problem or an everyone problem?
Which funnel stage owns the loss? What should be fixed first, with the evidence?

**Known caveats on the ticket.** The home carousel opens a restaurant's menu without a search, so
"search" is skippable. Sessions and members are different units, and the dashboard mixes them. The
August cohort was acquired on a discount. The checkout release changed event names for one stage on
Android, which the app team has mapped.

### The twelve rows (L1)

Twelve members from three signup months: four from May, three from June, five from the August sale
cohort, each with an order flag for every month since signup to September. The shape to hit: May 3 of
4 active in month one and 2 of 4 in month two; June 2 of 3 in month one and 1 of 3 in month two;
August 2 of 5 in month one; the blend over all twelve in September at 6 of 12, 50 percent, at least
five points from 38 and from Kalpa's 41 (targets on the rows).

### The sub-problems

**L1. Who entered when, and what happens to each group month by month?** Concepts: fix the entry
moment; the triangle; the blend hides the decline. Analogy: two coaching batches of 10, June and
July; 6 and 4 return in month two (toy, R1). The blend toy: batch A of 100 stood at 50 percent last
month; now A is at 40 and new batch B of 400 at 52.5, so 250 of 500 is still 50 percent while each
batch falls with age (toy, R1). Numbers: the twelve rows. Trap: none yet. Interviewer listens for: the
entry moment fixed before any rate. Common wrong answer: "retention is 50 percent" with no cohort.

**L2. What is every cohort's curve on 60,000 members, and what is the blend made of?** Concept: a
cohort table is one `pivot_table`; the blend is a size-weighted average of cohort rates. Numbers: the
month-one rates above; every cohort strictly falling across its observed ages; the blend for June to
September at 38 percent, reproduced as the weighted average and asserted equal to the direct count
(targets). The trap, exactly: "Blended retention is 38 percent and flat, so nothing changed" and the
decision it misleads: the sale cohort gets no action and the dashboard stays. The check: decompose.
Interviewer listens for: fewer users against less use per user, separated. Common wrong answer:
"impossible".

**L3. Which stage owns the loss, on which denominator, and for whom?** Concepts: stages and their
denominators; the artefact; the unit. Toys: 100 visits, 40 searches, 20 add-to-carts, 10 checkouts,
steps of 40, 50 and 50 percent, overall 10; checkout per session 10 of 50 against per member 10 of 20
(R1). Numbers: search to menu view at 118 percent per session (the carousel skips search, the
artefact); menu view to add-to-cart 34 percent per session and 61 percent per member; add-to-cart to
order for members on Android 58 to 44 after 14 September, iOS flat, non-members flat (targets). The
trap, exactly: "the drop is at add-to-cart to order for everyone": it sits in members on Android after
one date, so the app team is partly right that the stage is fine elsewhere. Interviewer listens for:
tracking and definitions checked before behaviour is blamed (T2). Common wrong answer: blaming the
stage owner from the overall rate.

**L4. What can the table not show?** Six caveats with one check each: selection (the sale cohort
was bought on a discount; its curve beside an organic cohort of the same month, target: the organic
August members retain like July's); censoring (the latest cohorts are young and a member who has not
left is not retained for ever; named for the faculty block); seasonality (exam months in a
student-heavy zone, a labelled hypothetical with the check by zone); the tracking change (the renamed
event on Android; the check uses the app team's mapping and shifts the release date a week either way,
target: the fall holds); sessions against members (the unit named on every chart); before-and-after is
not cause (Zomato Gold's 60 percent frequency rise after joining, Th4, as the self-selection
question). Interviewer listens for: the denominator asked for before a chart is trusted (Th2). Common
wrong answer: "members order more because Gold works".

**L5. What is fixed first, what is the evidence, and what does the sale cohort cost?** Concept: the
fix-first call with its cost; the dispute answered. Numbers: the Android checkout first, the fall's
size in orders a week (target) times an average member order value (a labelled assumption with a
range); the sale cohort's orders over its first three months against an organic cohort's, per member;
the app team's chart (overall conversion, all platforms, flat) answered with the split by platform,
membership and date. Trap: fixing the "loss" at the skippable stage; fixing retention by buying more
sale members. Interviewer listens for: the stage, the cohort it hurts most, the evidence, the cost.
Common wrong answer: "fix retention" with no stage.

**L6. Retention dropped; walk me through your investigation. And how do you separate novelty from
habit in an AI app's cohorts?** Structure (Aced, T2): tracking first, then the definition, then
segments by cohort, platform and region, then fewer users against less use per user, then the funnel
stage. The AI-company variant (programme-written): a launch-week cohort whose day-1 numbers are
novelty, organic cohorts beside it, week-4 retention per cohort, the blended MAU that hides the decay.
Interviewer listens for: the order, and the refusal to name a cause first. Common wrong answer: a
cause in the first sentence.

### Public facts allowed on Thursday

| R2 id | Company or source | The fact, used how | URL (checked 12 October 2026) |
|---|---|---|---|
| Th4 | Zomato | Gold at 1.8 million members in the quarter to March 2023; members' orders about 30 percent of food delivery GOV in March 2023; order frequency rose about 60 percent on average after joining. The company facts of the case; L4's self-selection question | https://www.bseindia.com/xml-data/corpfiling/AttachHis/42b3bf3b-1edb-4da7-849a-87ca9da27ff8.pdf |
| M2, Th1 | Eternal, Blinkit | Q4 retention averaged 46 percent across cohorts and every successive cohort improved; NOV retention 150 percent at Q4, 279 percent at Q12: survivors spend more. L1 | https://www.eternal.com/blog/q1fy27/ |
| Th2 | Swiggy Instamart | The cohort triangle indexed to the Q4 FY24 cohort; weak users weaned away; the denominator question. L1 and the fallback | https://www.swiggy.com/corporate/wp-content/uploads/2025/10/Q2-FY2026-Shareholder-letter.pdf |
| Th3 | Swiggy | MTU up 27.4 percent while platform frequency fell 6.3 percent; over 4 million unprofitable users weaned; one-month retention 61 from 55 percent. L2 and L5 | the Swiggy Q1 FY27 URL in Wednesday's table |
| Th5 | Amplitude | 7 percent day-7 retention as roughly top quartile; enterprise median 2.1 percent; vendor figures with a loose definition. L3's "what good means", with the caveat | https://www.amplitude.com/blog/7-percent-retention-rule |
| M5 | Uber | Uber One at 46 million members. Notes only | the Uber 10-K URL in Monday's table |
| T2 | Aced | Tracking first; segmentation before root cause; fewer users against less use. L6 | https://www.aced.io/blog/top-data-analyst-interview-questions |

Not to be used: current Zomato Gold or Swiggy One member counts (not in the 2026 letters, R2 "Not yet
verified"); a public case of blended-flat-while-cohorts-decline (none verified, so the case stays
synthetic and says so).

### The guesstimate

Riders on the Delhi Metro on a weekday: clarify (journeys, boardings or line use); map (lines times
trains times load, or population times the share using the metro); calculate; validate against 64.06
lakh average daily passenger journeys in 2026 and the record of 82,44,903 boardings on 17 September
2026 (M6, T3); the catch: journeys and boardings are different units, which is Thursday's whole lesson.

### The Kalpa transfer

The lab's case: the head of Retail-Plus's two questions (the row): is the fall everyone or the
monsoon-sale members, and where is the loss. The Thursday generator writes `memberships`
(`customer_id`, `tier`, `member_since`: 120 Retail-Plus members with starts in January to August 2026,
independent of order history, the August monsoon cohort the largest) and `events` (`customer_id`,
`session_id`, `event_type`: visit, search, add_to_cart, checkout; `event_ts`) for Retail-Plus members
over July to September 2026, every app-channel order with exactly one checkout event on its date and no
checkout without an order. Plants (TRAINER until the lab): blended retention 41 percent for July,
August and September under the spine's definitions; every cohort with two observed ages strictly
falling; the August cohort's month-one rate the lowest and the cohort the largest; add-to-cart to
checkout for members at least 15 points below the three weeks before inside Monday's fixed window (10
to 30 September) and within 5 points outside it; at least 20 percent of sessions skipping search;
checkout per session and per member at least 10 points apart. The lab's twelve rows: seven members
from the May and August cohorts tracked July to September, and one member's week of events showing
the skippable stage. If orders-based retention cannot be shaped with v4 frozen, the fallback is app
activity, recorded in the facts file. The unguided exercise: the fix-first call for Kalpa, which the
bank's items 5, 12, 13, 20 to 22, 27, 33 to 35 and 42 test.

---

## Friday: Flipkart, the Lucknow fulfilment centre. How much is coming, and how wrong could we be?

### The ticket

**Flipkart, the Lucknow fulfilment centre, festive packer headcount (illustrative case: the company
is real, the situation and the data are synthetic, built for this class; Flipkart's festive-capacity
statements in F6 are the only public facts used).**

The centre has 104 weeks of outbound shipments, the weeks beginning Monday 30 September 2024 to
Monday 21 September 2026. The festive peak sits in the weeks before Diwali each year: Diwali fell on
Thursday 31 October 2024 (the week beginning 28 October) and Monday 20 October 2025 (the week
beginning 20 October), and falls on Sunday 8 November 2026 (the week beginning 2 November) (F5 and
`facts.yaml`). A packer packs about 120 shipments a shift (target). The planner must book packer
shifts for the eight festive weeks beginning 12 October to 30 November 2026 by Friday.

| Measure | Value (targets unless marked) |
|---|---|
| Ordinary weekly shipments, late 2024 | about 210,000 |
| Underlying growth | about 4 percent a year |
| Festive peak | the three weeks before Diwali at 1.5, 1.9 and 1.7 times the ordinary week; the Diwali week at 1.4; the week after below ordinary |
| Hold-out | the last thirteen weeks, beginning 29 June to 21 September 2026, with the 91 weeks before them for training |
| MAE on the hold-out, shipments a week | naive 21,000; drift 11,500; same-week-last-year 9,200; festival-aligned with drift 8,900; finance's rule 9,600; the vendor 14,800 (the vendor at least 30 percent above the festival-aligned baseline) |
| The vendor's fit on the 91 training weeks | within 2 percent of the actual every week |
| The 2026 festive window, eight weeks | the vendor 22 percent above the 2025 window; finance's rule 4 percent above; the festival-aligned baseline with drift about 6 percent above, its error bar the hold-out MAE (targets) |
| An idle packer-shift | Rs 650 (assumption, range Rs 500 to 800), about Rs 5.4 per over-forecast shipment |
| A late shipment | Rs 25 (assumption, range Rs 15 to 40) per under-forecast shipment |
| The plan quantile from the two costs | 25 over (25 plus 5.4), about 0.82 |

**Data the analyst has.**

| Table | Columns | Rows |
|---|---|---|
| `weekly_shipments` | `week_start`, `shipments`, `packer_shifts_worked`, `overtime_shifts` | 104 weeks |
| `vendor_forecast` | `week_start`, `vendor_shipments`, `kind` (fitted, holdout, forecast) | 91 fitted weeks; 13 hold-out weeks forecast from the data to the week of 22 June, so the hold-out scores a real forecast; the forecast from the week of 28 September to 30 November 2026, made from all 104 weeks |
| `calendar` | `week_start`, `diwali_week`, `sale_week` | 114 weeks, to the week of 30 November 2026 |
| `costs` | `item`, `rs`, `low`, `high` | the two unit costs with their ranges |

**The ask, due Friday, to the FC planner and the regional operations head.** Which forecast goes to
the staffing plan, how wrong could it be in shipments and in rupees, and how many packers per week?

**Known caveats on the ticket.** The festival moves by weeks each year, and the sale weeks move with
it. One spike a year is two observations in two years. A late shipment costs more than an idle shift.
The series is demand clipped by the centre's own capacity in the peak weeks.

### The twelve rows (L1)

The six weeks around Diwali 2024 (beginning 7 October to 11 November 2024) and the six around Diwali
2025 (beginning 29 September to 3 November 2025), with shipments. The hand count: the naive for the
week beginning 20 October 2025 is the week before; the same-week-last-year copy for the 2025 weeks
lands the peak one week late (Diwali moved from the week of 28 October to the week of 20 October); the
festival-aligned copy lands it on the festival. For 2026 the same-week-last-year copy of the week of
20 October 2025 lands on the week of 19 October 2026, two weeks before Diwali's week of 2 November
(targets on the rows).

### The sub-problems

**L1. What shape do the 104 weeks have, and what would three simple rules say for one week?**
Concepts: read the shape first; naive, same-week-last-year, drift, festival-aligned. Analogy: 50, 52,
49, 51 cups on four days, so tomorrow's forecast is 51; Sundays sell 80, so next Sunday's is 80 (toy,
R1). Four panels: trend, seasonality, cycle, noise (toy). Numbers: the twelve rows. Trap: a curve
drawn through every past point called a forecast. Interviewer listens for: the shape read before any
method. Common wrong answer: "fit a model".

**L2. How does each method score on the thirteen weeks it never saw?** Concepts: hold out as many
periods as the horizon; MAE in the business's unit; the scoreboard. Toy: three held-out weeks with
errors 10, 5 and 10 give an MAE of 8.3. Numbers: the MAE table above; the vendor's fit within 2
percent against its hold-out MAE; the second route recomputes MAE from the printed error table. The
trap, exactly: "the vendor curve fits the last two years almost exactly and promises 22 percent", the
decision it misleads (the plan at plus 22), the check (its error on the weeks it never saw), the fix
(the baseline with its error bar). Interviewer listens for: fit and forecast kept apart; the measure
fixed before scoring. Common wrong answer: judging by the fit.

**L3. Which weeks drive each method's error, and which direction is the vendor wrong in?** Concept:
the error's sign; the segment of weeks. Numbers: the vendor's misses concentrated in the two weeks
after the 2025 festival, where it extrapolated the spike; the bot's misses on the misaligned festival
weeks (targets). The trap, exactly: "MAE 14,800 is the vendor's error": its over-forecasts and
under-forecasts cost different amounts, so the same MAE can be cheap or dear. Interviewer listens for:
the direction of the error asked about. Common wrong answer: one number for the error.

**L4. What can two years of weeks not tell us?** Six caveats with one check each: the festival moves
and the sale moves with it (the 2025 window re-forecast from data to September 2025 by both baselines,
errors priced); one spike a year is two observations (said, no check possible); the GST cut that
coincided with the 2025 festival (FADA, F5) as confounding in any national series the vendor trained
on; a new model with no Lucknow history is an assumption (Target Canada, F4); the hold-out holds no
festival, so the festival error is judged on 2025 alone; capacity clips the series. Interviewer
listens for: the hold-out's limit named. Common wrong answer: "two Diwalis make a seasonal pattern".

**L5. Which forecast goes to the plan, how many packers per week, and what does being wrong cost in
each direction?** Concept: asymmetric cost; plan above the middle of the error bar; the plan quantile
as the ratio of the under-cost to the sum of the two. Numbers: the festival-aligned baseline with
drift for the eight weeks, shifts per week as shipments over 120, the plan raised toward the 0.82
quantile of the error bar; finance's 4 percent and the vendor's 22 percent answered; the cost of the
bot's two-week miss (idle shifts in the two early weeks, late shipments in the two late weeks, priced
with the two unit costs, target). The two roles: finance ("last year plus 4 is what the budget holds":
true for the total, wrong for the week-by-week shape) and the vendor's sponsor ("the model fits every
week of history": true, which is the problem). Trap: a plan at the median when a late shipment costs
about 4.6 times what an idle shift costs per shipment (Rs 25 against Rs 5.4); a plan with the festival in the wrong week. Interviewer listens for: the error
in rupees in each direction, the plan tied to the costlier side. Common wrong answer: splitting the
difference between 4 and 22. Priced with the two unit costs, a forecast that errs high can cost less
on the hold-out than one with a lower MAE that errs low: the pack prices every method's hold-out errors
beside its MAE and lets that fact stand, and the plan's case rests on placing the festival in the right
weeks and setting the level at the 0.82 quantile, neither of which a hold-out with no festive week can
test (L4).

**L6. How do you evaluate a forecast? And how do you forecast inference demand around an AI product
launch?** Structure: hold out the latest periods, as many as the horizon; error in the business's
unit; compare with the naive and the seasonal baseline; fix the measure before scoring. The AI-company
variant (programme-written): requests per minute around a launch, the launch spike as the festival, a
hold-out that spans the horizon, asymmetric cost (over-provisioned capacity against timeouts), the
baseline a capacity model must beat. Interviewer listens for: the baseline, the hold-out, the unit, the
direction. Common wrong answer: "we used ARIMA and the fit was good".

### Public facts allowed on Friday

| R2 id | Company or source | The fact, used how | URL (checked 12 October 2026) |
|---|---|---|---|
| F6, T3 | Flipkart | The Big Billion Days 2026: 14 million cubic feet of warehouse space added, more than 2.5 lakh festive jobs, decided weeks ahead; 6.3 million concurrent users in a minute. The company facts of the case and L5 | https://stories.flipkart.com/announcement/flipkarts-big-billion-days-returns-for-its-13th-edition ; the 9 October URL in Tuesday's table |
| F5 | DoPT holiday lists | Diwali on 31 October 2024, 20 October 2025, 8 November 2026. The festival calendar card | https://www.staffnews.in/2023/07/list-of-holidays-2024-dopt-order-reg-gazetted-and-restricted-holidays.html ; https://www.staffnews.in/2024/07/holidays-to-be-observed-in-central-government-offices-year-2025.html ; https://www.staffnews.in/2025/07/list-of-holidays-2026-dopt-order-reg-closed-and-restricted-holidays.html |
| F5 | FADA | The 42-day festive window aligned to the festival each year (22 September to 2 November 2025 against 3 October to 13 November 2024); October 2025 two-wheeler retail 31,49,846 against 12,87,735 in September; part credited to GST cuts. L4 | https://fada.in/images/press-release/1690d68d7a2e6cFADA%20releases%20October%202025%20&%2042-Days%20Festive%20Vehicle%20Retail%20Data.pdf |
| F1 | Makridakis and others, PLOS ONE 2018 | Better fit did not mean better forecasts; Naive 2 beat half the machine-learning methods. L1, L2 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0194889 |
| F2 | The M5 competition | Seasonal naive 0.847 against naive 1.752, ahead of the perceptron (0.977) and random forest (1.010); the winner 0.520; errors weighted by dollar sales. L1 and the Saturday paper | https://mofc.unic.ac.cy/m5-competition/ ; https://raw.githubusercontent.com/Mcompetitions/M5-methods/master/Scores%20and%20Ranks.xlsx |
| F3 | Zillow | A public guardrail of plus or minus 200 basis points, a swing of about 1,200, an inventory write-down of about USD 304 million, the business wound down with about a quarter of the workforce cut. L3 and the fallback | https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm |
| F4 | Target Canada | A forecasting system that needed years of history and buyers who used optimistic projections instead; returns from Week 1 Wednesday in its forecasting role. L4 | https://corporate.target.com/press/release/2015/01/target-corporation-announces-plans-to-discontinue-canadian-operations ; https://advisor.ca/industry-news/industry/why-target-failed-in-canada/ |
| W1 | Amazon | A bestseller list beat a deep-learning model in a Prime Video test. L6 | the Amazon Science URL in Wednesday's table |
| T3 | SIAM | 2.17 crore domestic two-wheeler sales in FY 2025-26. The guesstimate's anchor | https://www.siam.in/news-&-updates/press-releases/x/605 |

Not to be used: M4 and M5 findings beyond scale; Kaggle's data terms; FPP3 sections 5.2 and 5.8 (403 on
12 October 2026; the pack cites the restructured toolbox addresses from R1 section 7 once a session
re-fetches them).

### The guesstimate

Two-wheelers sold in India in a year: clarify (domestic sales, new vehicles); map (households,
ownership, replacement years, first-time buyers); calculate; validate against 2.17 crore in FY 2025-26
(SIAM, T3); the catch: October 2025's retail alone was 31.5 lakh (FADA, F5), so a festive month must
never be annualised.

### The Kalpa transfer

The lab's case: Anand's two forecasts eighteen points apart (the row). The Friday generator writes
`monthly_revenue` (`month`, `revenue_rs`, October 2024 to September 2026, April to September 2026
equal to the monthly sums of `orders.amount`), `vendor_forecast` (`month`, `vendor_rs`, fitted for
October 2024 to March 2026 and forecast for April 2026 to March 2027) and `plan_line_next` (`month`,
`plan_rs`, 15 percent above the same month a year earlier). Plants (TRAINER until the lab): October
2024 and October 2025 each between 1.4 and 1.7 times the mean of their neighbours; the twelve months to
September 2025 three to five percent below the twelve to September 2026; the vendor's fitted values
within 2 percent of the actual; on the six held-out months April to September 2026 the vendor's MAE at
least 30 percent above the seasonal naive's, both printed in Rs lakh with the naive's and the drift's;
the vendor's October 2026 to March 2027 total 22 percent above the actual year before, finance's 4
percent by construction; the month-aligned seasonal naive for October 2026 equal to October 2025's
revenue, a festival month, while the festival-aligned baseline puts the spike in November 2026, both
printed month by month with the plan line. The lab's twelve rows: October to March of both years. The
unguided exercise: Anand's board number with its error bar, which the bank's items 6, 7, 14, 23, 24,
28, 36 to 38, 41 and 43 test.

---

## Saturday: the method moves company

The eight briefs the Saturday session writes, one paragraph each, with the answer grid (what stays:
the method; what changes: the metric, the constraint, the cost of an error; what would change back on
the Retail tables):

| Brief | The method re-posed | Facts allowed |
|---|---|---|
| Ola or Rapido, a two-wheeler ride guarantee in a named city | Monday's: the number the scheme pays for, the guardrail, the gaming | None in R2; every number a labelled hypothetical |
| Blinkit or Zepto, a dark store's bought-together strip | Wednesday's: lift above a floor, the slot's value | Blinkit's 2,443 stores and NOV (M2); Blinkit's steady-state NOV of Rs 11 lakh per store per day (T3); the rest hypothetical |
| Swiggy One, the membership's cohorts | Thursday's: cohorts against the blend, the funnel's units | Swiggy One free delivery in the GOV definition (M1); the rest hypothetical |
| Amazon India, a fulfilment centre's festive staffing | Friday's: the festival-aligned baseline, the asymmetric cost | Amazon Great Indian Festival 2025: over 276 crore customer visits, 70 percent from tier 2 and 3 cities (F6); the rest hypothetical |
| Kalpa Financial Services, Rohan Desai | Which customers to nudge first, where a wrong nudge costs twenty times a wrongful rejection | `docs/07_Client_Zero.md`, Build 2 seeds |
| Kalpa Logistics, the head of operations by role | An on-time delivery rate gamed by re-dating the promise; Diwali parcel volumes forecast | Client zero v2.3 note; the stakeholder's name is open, so the role is used |
| Kalpa Health, Dr Priya Menon | Patient cohorts by first-visit month; the booking-to-visit funnel in dollars | Addendum `health-us-facing` |
| Kalpa Connect, Ananya Bose | Subscriber cohorts under a flat blended churn | Client zero |

The Saturday facts for the paper's real-case items, each with its id: Wells Fargo's silent definition
change (M8), Swiggy's weaned users (Th2, Th3), the M5 scoreboard (F2), Delhi Metro's units (M6),
Flipkart's decimal (T3), Maxxsaver's cost line (W4). The "unverified, do not use" list of R2 is carried
into the Saturday session's sources list so no item reaches for it.

## The interview room across the week: what every transcript carries

Each finishing session writes its day's transcript and AI-company variant from the L6 notes above,
under these headings in this order: the question as the interviewer says it; the clarifying questions
a strong candidate asks; the structure; the trap the interviewer fishes for; a weak answer and a
hire-grade answer side by side in two columns; the scorecard (the spine's seven criteria, each 0 to 2,
scored for both answers, in the TRAINER file); three follow-ups with the line a hire-grade answer
gives each. Every real fact inside carries its R2 id. The line "written for this programme in the
style of product-company and GCC screens; the facts inside are from the case file" opens each. The
fallback days' second transcripts take the row's [D] anchors. Company-specific interview reports for
Walmart Global Tech India, Target in India, Flipkart and Swiggy were not verified (R2), so no
transcript claims to reproduce a company's screen.

# Is the number the scheme pays for measuring what the city wants?

**The ticket. Uber, Hyderabad, the driver app's peak-hour earnings guarantee.**

*Illustrative case: the company is real, the situation and the data are synthetic, built for this class.*

On Monday 31 August 2026 the Hyderabad city team launched a peak-hour earnings guarantee for
enrolled drivers: a driver who stays online through a whole peak window (two windows a day, three
hours each) is guaranteed a floor of Rs 300 per peak online hour, and Uber pays the gap between the
driver's trip earnings in the window and the floor as a top-up. The launch note's goal: "more drivers
on the road at peak, so riders are picked up faster".

| Measure | Before (weeks of 20 Jul to 24 Aug) | After (weeks of 31 Aug to 5 Oct) |
|---|---|---|
| Peak online hours, all enrolled drivers | 118,000 | 146,300, up 24 percent |
| Completed peak trips | 224,200 | 230,900, up 3 percent |
| Trips per peak online hour | 1.90 | 1.58 |
| Offers accepted over offers shown, at peak | 0.86 | 0.73 |
| Accepted trips the driver then cancelled, share | 0.04 | 0.09 |
| Peak online hours with no completed trip, share | 0.22 | 0.38 |
| Median rider wait at peak, minutes | 4.8 | 4.6 |
| Rider requests at peak that went unfulfilled, share | 0.11 | 0.10 |
| Top-up paid | Rs 0 | Rs 1.9 crore |

**Data:** `drivers` (1,200 drivers, 140 joined after the launch), `driver_weeks` (one row per driver
per week: hours, offers, accepted, cancels, trips, hours with no trip, bookings, top-up) and
`zone_weeks` (one row per zone per week: rider requests, fulfilled, median wait). A request one
driver declines is offered to the next, so `driver_weeks` counts offers and `zone_weeks` counts
requests. **The ask, due Friday:** is the scheme working, which metric should it pay for, and is
anyone gaming it? **Caveats:** the monsoon ended inside the after window; 140 drivers are new; the
app counts a driver as online whenever the app is open; three outer zones (Shamshabad, Rajendranagar,
Patancheru) get few requests; drivers can be online on more than one platform; trip earnings are not
in the data, so a week's top-up cannot be rebuilt from its bookings.

**Who needs the answer.** The city head, who decides on Friday whether the scheme continues,
changes or spreads to two more cities.


## What does "peak online hours up 24 percent" stand for, and what did six drivers do?

**Who needs the answer.** The city head, who was about to read a 24 percent rise as success.

**The questions on the way.** What is a proxy? What do six drivers' weeks say, counted by hand? Why
do the six fall further than the city?

### What is a proxy?

A canteen pays its servers per token handed out (invented). Tokens double from 200 a day to 400
while plates stay at 200, because each plate now gets two. That is a **proxy**: a number standing in
for the thing wanted, which drifts once it is paid for. Peak online hours stand in for drivers ready
to pick riders up, and the guarantee paid for the hours.

**Say it to a driver.** "We paid for an open app, and from some drivers an open app is all we got."

### What do six drivers' weeks say, counted by hand?

Twelve rows of the case data: six drivers, one week before the launch (10 August) and one after (21 September):

| Driver | Hours, before then after | Trips, before then after |
|---|---|---|
| A | 10 then 11 | 21 then 22 |
| B | 9 then 10 | 17 then 18 |
| C | 11 then 12 | 22 then 23 |
| D | 10 then 11 | 19 then 20 |
| E, Shamshabad | 10 then 16 | 18 then 3 |
| F, Rajendranagar | 10 then 14 | 17 then 2 |

Add the hours: 60 before, 74 after, up 23 percent. Add the trips: 114 before, 88 after, down 23
percent. Divide once: 114 over 60 is 1.90 trips per hour; 88 over 74 is 1.19.

**The maths, made intuitive.** Picture each hour as a box of trips: E and F added boxes and lost
almost every trip, so trips per box fell for the six together.

### Why do the six fall further than the city?

The city went from 1.90 to 1.58 and the six to 1.19, because two of the six, E and F, are in the
idle tail found below: a third of the sample against 15 percent of drivers city-wide, chosen to show
the mechanism.

**What it cost elsewhere.** Wells Fargo's cross-sell ratio counted accounts per household with no
condition that anyone used them; the bank paid USD 185 million in penalties in 2016 and, in 2020, USD 3
billion to resolve US Justice Department and SEC investigations (CFPB, 8 September 2016; SEC release
2020-38; checked 12 October 2026).

**Explorer scene M1** (`demos/C2_W04_D01_week_explorer_STUDENT.html`, shipped with the week): raise
the guarantee and watch new hours sit still in the outer zones.


## What are the city's totals, and what is trips per online hour?

**Who needs the answer.** The analyst putting one city number on the Friday memo.

**The questions on the way.** How is a rate added up? Did rider demand fall? What does a quick
average say?

### How is a rate added up?

Add every trip, add every hour, divide once. Two invented drivers show why: one makes 2.0 trips an
hour over 10 hours (20 trips), the other 0.5 over 40 hours (20 trips). Together: 40 trips over 50
hours, 0.80. Averaging their two rates gives 1.25, because the slow 40-hour week counts no more than
the busy 10-hour one.

On the full table one `groupby` per window gives 1.90 and 1.58; notebook 03 checks it in SQL.

### Did rider demand fall?

The tempting excuse is fewer riders, but `zone_weeks` says requests rose 1.8 percent, from 251,910
to 256,556. Declined requests are offered again, so offers per request went from 1.07 to 1.35.

### What does a quick average say?

Average each driver-week's own rate and the after window prints 1.71, above the true 1.58: the
true fall is 0.32, and the average shows 0.19 of it, hiding about two-fifths for the same reason as
the two drivers. **The check:** recompute from the sums. Swiggy's letters write each
metric down this carefully: platform frequency is completed orders per transacting user per month,
4.53 in the quarter to 30 September 2024 (Q2 FY25 letter, checked 12 October 2026).

**Say it to a driver.** "We add every trip and every hour first, so a long idle week counts in full."


## Which drivers and zones drive the fall?

**Who needs the answer.** The city head, who is about to extend the scheme to two more cities.

**The questions on the way.** Who sits under one trip an hour, and where? What decision would the
celebrated number have sent?

### Who sits under one trip an hour?

After the launch, 180 drivers, 15 percent of the city, made fewer than one trip per peak online hour,
the idle tail: their hours went to 2.1 times their level while their trips fell 12 percent, and 72
percent of their new hours sat in the three outer zones. The other 880 drivers who joined before the
launch made 1.90 trips an hour throughout. Acceptance alone finds the same 180: none of their weeks
accepted more than 0.46 of its offers, and no other week fewer than 0.78.

### What decision would the celebrated number have sent?

**The plausible wrong memo:** "Peak online hours up 24 percent. Supply target met. Extend the scheme
to two more cities." **The check:** trips per peak online hour fell from 1.90 to 1.58 and the median
wait barely moved. **The fix:** keep the floor only for weeks that accept half the offers shown.

**The maths, made intuitive.** A rate is a blend. 100 drivers at 1.9 trips an hour and 20 new drivers
online as long at 0.2 blend to about 1.62 (invented numbers), though none of the 100 drives differently.

Delhi Metro's "line utilisation" read 45,35,932 on 29 May 2018 against about 27 lakh riders a day,
since a journey across three lines counted three times (LatestLY, checked 12 October 2026).

**Say it to a driver.** "Most of you drove as before; about one driver in seven sat online where
nobody was asking."


## What can the data not show, and what would settle each doubt?

**Who needs the answer.** The finance partner, who will say the monsoon's end explains the fall.

**The questions on the way.** Which doubts does the fall survive? Which stay open?

| Doubt | The check | What it found |
|---|---|---|
| Data quality: online means the app is open | Share of online hours with no trip | 0.22 to 0.38 |
| Mix: 140 new drivers | The rate without them | Still 1.58 |
| Season: the monsoon ended | The three weeks with most requests; the launch week | 1.60; a step from 1.88 to 1.64, requests steady |
| Zones | Core zones only | 1.90 to 1.79: most of the fall is in the outer zones |
| Two apps at once | Hourly data and the other app | Open: Uber cannot see the other app |
| Selection | Who enrolled | Every driver here enrolled, so no group to compare |
| Cause | The scheme or the season | Open until the redesign is tested |

US Veterans Affairs measured waits from a "desired date" schedulers typed in; at Phoenix, 30 of 79
staff interviewed had used the wrong date (VA OIG report 14-02603-267, checked 12 October 2026). A
driver starts every online hour by opening the app, so paying per hour hands the clock to the paid.

**Say it to a driver.** "New drivers and the weather do not explain the fall; it sits in the quiet zones."


## What should the scheme pay for, and what did paying for hours cost?

**Who needs the answer.** The city head, who signs the next six weeks, and finance, who owns the
budget.

**The questions on the way.** What are a north star, a guardrail and an input? What does the
definition say? What did hours cost, and what would the redesign save? What do the roles say?

### What are a north star, a guardrail and an input?

The **north star** is the number the city judges the scheme by: completed peak trips per enrolled
driver online at peak, per week. Three **guardrails** must not get worse while it rises: for riders,
the share of offers accepted (at or above a floor) and the median wait; for the budget, top-up per
trip. Read them as a seesaw: if the north star rises while a guardrail moves the wrong way, riders or
the budget paid for it. An **input** moves first: drivers online in the first hour of each peak
window, and rider requests per online hour by zone. Leading says when a number moves, so acceptance
is a guardrail and a leading number at once.

### What does the full definition say?

| Line | The redesign |
|---|---|
| Numerator | Trips completed inside the peak windows, one per paying rider |
| Denominator | Enrolled drivers online at least one peak hour that week, the count printed |
| Window | The calendar week |
| Exclusions | Trips cancelled by either side, test accounts, trips outside the windows |
| What it does not reward | Hours online; declines; a shrinking base, which lifts the rate with no extra trip |
| Guardrails | Riders: accepted share over a floor, median wait. Budget: top-up per trip |
| Gaming note | Declining and cherry-picking; lost supply; a runaway top-up |

Uber's 2025 annual report (its 10-K) counts an UberX Share ride with three paying riders as three
trips (checked 12 October 2026). The north star read 35.76 trips per online driver-week before and
35.89 after; it would rise if drivers quit, so it is never read without the wait.

### What did hours cost, and what would the redesign save?

Rs 1.9 crore bought 6,700 more peak trips, about Rs 2,836 each, 17 times the Rs 165 fare, and Rs
1.159 crore of it went to driver-weeks that accepted fewer than half their offers: below the floor
the top-up shrank by whatever the next trip earned, so declining cost nothing. The redesign keeps the
floor only for driver-weeks that accept at least half their offers, an accepted trip later cancelled
counting as declined. It saves Rs 92.7 lakh if a fifth of the idle tail's top-up is still paid and
Rs 58 lakh if half is: an assumption with a range, which a test settles.

### What do the three roles say?

Driver operations says drivers will log off: true for the idle tail, and the wait by zone shows any
loss. Marketing says new terms look like bait: true, so the floor stays for drivers who accept.
Finance blames the monsoon: partly, but the rate stepped down in the launch week itself.

A north star read alone misleads the other way too: Maxxsaver helped raise Swiggy Instamart's average
order value 16 percent to Rs 612 while cart consolidation lowered order growth, so orders per user
would have read a success as a fall (Q1 FY26 letter, checked 12 October 2026).

**Explorer scenes M2 to M4:** the seesaw, the definition rebuilt line by line on the twelve rows,
and acceptance turning before bookings per hour.

**Say it to a driver.** "The floor now pays for trips you complete, if you say yes to most offers."


## How would you measure the success of a new feature, in an interview?

**Who needs the answer.** You, in a product or analytics screen.

**The questions on the way.** What does a hire-grade answer do? How does it move to an AI product?

### What does a hire-grade answer do?

It clarifies first (the goal, who is in it, what counts as harm, which decision rides on it, against
what), then gives the structure: goal, a north star with its lines, three guardrails, a leading input,
and a test with zones as its unit. Weak: "hours are up 24 percent, so it works." Hire-grade: "trips
per online hour fell from 1.90 to 1.58, stepping down in the launch week; outer-zone waits fell from
6.6 to 5.95 minutes at about Rs 46,000 per extra trip; I would not extend it, and would test a floor
kept only for weeks that accept most offers." The transcript carries the follow-ups."

### How does it move to an AI product?

An AI coding assistant's team reports suggestions accepted, a proxy it can raise by showing fewer,
safer suggestions. The outcome is suggested text still in the code at the next commit, per developer
with a seat, read beside time to merge; the guardrails are build failures and reverts on suggested
code, security findings and rewritten lines; teams are the test's unit. Programme-written; no company
figure.

## Which real cases show each way a number goes wrong?

- **No usage condition:** Wells Fargo's cross-sell ratio (SEC order, Release 34-88257).
- **The measured start the window:** VA's "desired date" (its Office of Inspector General, 2014).
- **A definition changed in silence:** Wells Fargo's unannounced 2013 addition of remittance
  accounts, 0.04 of that year's 0.11 rise in the ratio (SEC order).
- **A headline moved from gross to net:** Eternal, whose businesses include Zomato and Blinkit,
  stopped disclosing gross order value for net order value (Q1 FY27 letter).
- **A count that goes negative:** Airbnb's nights booked net of cancellations, minus 4.1 million in
  March 2020 (its listing filing, Form S-1, 2020).
- **A bar set at any use at all:** Spotify's monthly active user, any account with more than zero
  milliseconds of consumption in thirty days (annual report, Form 20-F for 2025).

All six were checked on 12 October 2026.


## Which words does the day use?

| Term | What it means |
|---|---|
| Proxy | A number that stands in for the thing wanted |
| Proxy test | Could a team hit this number while the thing it stands for got worse? |
| North star | The one number a plan exists to move |
| Guardrail | A number that must not get worse while the north star rises |
| Leading input | A number that moves before the north star and can be acted on this week |
| Lagging number | A number that confirms the north star after the fact |
| Idle tail | The 180 drivers under one trip per peak online hour after the launch |
| Offer | One rider request shown to one driver |
| Top-up | What Uber pays to lift a driver's peak hour to the Rs 300 floor |
| Bookings | The fares riders paid |
| Gaming | Raising a number without doing what it stands for |


## So is the number the scheme pays for measuring what the city wants?

No. Hours rose 24 percent while trips per peak online hour fell from 1.90 to 1.58 and the wait barely
moved, and Rs 1.159 crore of the Rs 1.9 crore top-up went to driver-weeks that declined most offers.
Judge the scheme by completed peak trips per enrolled driver online at peak, read with acceptance, the
wait by zone and the top-up per trip, and keep the floor only for weeks that accept at least half
their offers. Tuesday puts that on one slide.

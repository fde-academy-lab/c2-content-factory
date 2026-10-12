# Is the number the scheme pays for measuring what the city wants?

**The ticket. Uber, Hyderabad, the driver app's peak-hour earnings guarantee.**

*Illustrative case: the company is real, the situation and the data are synthetic, built for this class.*

On Monday 31 August 2026 the Hyderabad city team launched a peak-hour earnings guarantee for
enrolled drivers: a driver who stays online through a whole peak window (two windows a day, each
three hours long, set by the city team) is guaranteed a floor of Rs 300 per peak online hour, and
Uber pays the gap between the driver's trip earnings in the window and the floor as a top-up. The
goal written in the launch note was "more drivers on the road at peak, so riders are picked up
faster".

| Measure | Before (weeks of 20 Jul to 24 Aug) | After (weeks of 31 Aug to 5 Oct) | Change |
|---|---|---|---|
| Peak online hours, all enrolled drivers | 118,000 | 146,300 | up 24 percent |
| Completed peak trips | 224,200 | 230,900 | up 3 percent |
| Trips per peak online hour | 1.90 | 1.58 | 1.9 to 1.6 |
| Offers accepted over offers shown, at peak | 0.86 | 0.73 | down 13 points |
| Accepted trips the driver then cancelled, share | 0.04 | 0.09 | up 5 points |
| Peak online hours with no completed trip, share | 0.22 | 0.38 | up 16 points |
| Median rider wait at peak, minutes | 4.8 | 4.6 | barely moved |
| Rider requests at peak that went unfulfilled, share | 0.11 | 0.10 | barely moved |
| Top-up paid | Rs 0 | Rs 1.9 crore | |

**Data:** `drivers` (1,200 drivers, 140 joined after the launch), `driver_weeks` (one row per driver
per week: hours, offers, accepted, cancels, trips, hours with no trip, bookings, top-up) and
`zone_weeks` (one row per zone per week: rider requests, fulfilled, median wait). A request one
driver declines is offered to the next, so `driver_weeks` counts offers and `zone_weeks` counts
requests. **The ask, due Friday:** is the scheme working, which metric should it pay for, and is
anyone gaming it? **Caveats:** the monsoon ended inside the after window; 140 drivers are new; the
app counts a driver as online whenever the app is open; three outer zones (Shamshabad, Rajendranagar,
Patancheru) get few requests; drivers can be online on more than one platform.

**Who needs the answer.** The city head, who pays the top-up weekly and decides on Friday whether
the scheme continues, changes or spreads to two more cities.

**The questions on the way.** What does the rise in hours stand for? What do the totals say? Who
drives the fall? What can the data not show? What should the scheme pay for? How is it asked?


## What does "peak online hours up 24 percent" stand for, and what did six drivers do?

**Who needs the answer.** The city head, who was about to read a 24 percent rise as success.

**The questions on the way.** What is a proxy? What do six drivers' weeks say, counted by hand? Why
do the six fall further than the city?

### What is a proxy?

A canteen pays its servers per token handed out (an invented example). Tokens double from 200 a day
to 400 while plates stay at 200, because each plate now gets two. The token was meant to count
plates; once it was paid for, it counted tokens. That is a **proxy**: a number standing in for the
thing wanted. Peak online hours stand in for drivers ready to pick riders up, and the guarantee paid
for the hours.

**Say it to a driver.** "We paid for an open app, and from some drivers an open app is all we got."

### What do six drivers' weeks say, counted by hand?

Six real rows of the data, one week before the launch (10 August) and one after (21 September):

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
almost every trip, so trips per box fell for all six.

### Why do the six fall further than the city?

The city went from 1.90 to 1.58 and the six to 1.19, because two of the six, E and F, are in the
idle tail found below: a third of the sample against 15 percent of drivers city-wide, chosen to show
the mechanism.

**What it cost elsewhere.** Wells Fargo's cross-sell ratio counted accounts per household with no
condition that anyone used them; the bank paid USD 185 million in penalties in 2016 and USD 3 billion
in 2020 (CFPB, 8 September 2016; SEC release 2020-38; checked 12 October 2026).

**Explorer scene M1** (`demos/C2_W04_D01_week_explorer_STUDENT.html`, which ships with the week):
raise the guarantee and watch new online hours sit still in the outer zones.


## What are the city's totals, and what is trips per online hour?

**Who needs the answer.** The analyst putting one city number on the Friday memo.

**The questions on the way.** How is a rate added up? Did rider demand fall? What does a quick
average say?

### How is a rate added up?

Add every trip, add every hour, divide once. Two invented drivers show why: one makes 2.0 trips an
hour over 10 hours (20 trips), the other 1.0 over 1 hour (1 trip). Together: 21 trips over 11
hours, 1.91. Averaging their two rates gives 1.5, which treats one hour like ten.

On the full table one `groupby` per window gives 1.90 and 1.58, and notebook 03 reaches the same
totals in SQL, a second route.

### Did rider demand fall?

The tempting excuse is fewer riders. `zone_weeks` says requests rose 1.8
percent, from 251,910 to 256,556. The two tables agree once you see that a declined request is
offered again: offers per request went from 1.07 to 1.35.

### What does a quick average say?

Average each driver-week's own rate and the after window prints 1.71, above the true 1.58: the
average hides two-fifths of the fall, because a long idle week counts no more than a short busy one. **The check:** recompute from the sums. Swiggy's letters write each
metric down this carefully: platform frequency is completed orders per transacting user per month,
4.53 in the quarter to 30 September 2024 (Q2 FY25 letter, checked 12 October 2026).

**Say it to a driver.** "We add every trip and every hour first, so a long idle week counts in full."


## Which drivers and zones drive the fall?

**Who needs the answer.** The city head, who is about to extend the scheme to two more cities.

**The questions on the way.** Who sits under one trip an hour, and where? What decision would the
celebrated number have sent?

### Who sits under one trip an hour?

After the launch, 180 drivers, 15 percent of the city, made fewer than one trip per peak online hour:
their hours went to 2.1 times their level while their trips fell 12 percent. Every other driver who
joined before the launch, 880 of them, made 1.90 trips an hour before and after. A second route,
acceptance alone, finds the same 180: none of their weeks accepted more than 0.46 of the offers they
were shown, and no other driver's week accepted fewer than 0.78. 72 percent of their new hours sat
in the three outer zones.

### What decision would the celebrated number have sent?

**The plausible wrong memo:** "Peak online hours up 24 percent. Supply target met. Extend the scheme
to two more cities." **The check:** trips per peak online hour fell from 1.90 to 1.58, and the median
wait barely moved, 4.8 to 4.6 minutes. **The fix:** pay for completed peak trips, with a floor on
the share of offers accepted.

**The maths, made intuitive.** A rate is a blend. 100 drivers at 1.9 and 20 idle drivers at 0.2
blend to about 1.62 (invented numbers) with nobody's driving changed.

Delhi Metro's "line utilisation" read 45,35,932 on 29 May 2018 against about 27 lakh riders a day
that February, because one journey across three lines counted three times (LatestLY, checked 12
October 2026).

**Say it to a driver.** "Most of you drove as before; about one driver in seven sat online where
nobody was asking."


## What can the data not show, and what would settle each doubt?

**Who needs the answer.** The finance partner, who will say the monsoon's end explains the fall.

**The questions on the way.** Which doubts does the fall survive? Which stay open?

| Doubt | The check | What it found |
|---|---|---|
| Data quality: online means the app is open | Share of online hours with no trip | 0.22 to 0.38 |
| Mix: 140 new drivers | The rate without them | Still 1.58 |
| Season: the monsoon ended | The three busiest weeks of the twelve | Already 1.60 |
| Zones | Core zones only | 1.90 to 1.79: most of the fall is in the outer zones |
| Two apps at once | Hourly data and the other app | Open: Uber cannot see the other app |
| Selection and cause | Who enrolled; the scheme or the season | Open until the redesign is tested |

US Veterans Affairs measured waits from a "desired date" schedulers typed in; at Phoenix, 30 of 79
staff interviewed said they had used the wrong date (VA OIG report 14-02603-267, August 2014, checked
12 October 2026). A driver starts every online hour by opening the app, so paying per online hour
hands the clock to the person paid.

**Say it to a driver.** "New drivers, the weather and the quiet zones do not explain the fall away."


## What should the scheme pay for, and what did paying for hours cost?

**Who needs the answer.** The city head, who signs the next six weeks, and finance, who owns the
budget.

**The questions on the way.** What are a north star, a guardrail and an input? What does the
definition say? What did hours cost, and what would the redesign save? What do the roles say?

### What are a north star, a guardrail and an input?

The **north star** is the one number the scheme exists to move: completed peak trips per enrolled
driver online at peak, per week. A **guardrail** must not get worse while it rises: the share of
offers accepted (at or above a floor), the median rider wait, and the top-up per completed trip.
Read them as a seesaw: if the north star rises and a guardrail drops, the rise was bought. An
**input** moves first and can be acted on this week: drivers online in the first peak hour, and
rider requests per online hour by zone.

### What does the full definition say?

| Line | The redesign |
|---|---|
| Numerator | Trips completed inside the peak windows, one per paying rider |
| Denominator | Enrolled drivers online at least one peak hour that week, the count printed |
| Window | The calendar week |
| Exclusions | Trips cancelled by either side, test accounts, trips outside the windows |
| What it does not reward | Hours online, offers declined, a shrinking enrolled base |
| Guardrails | Accepted share at or above a floor; median rider wait; top-up per completed trip |
| Gaming note | Each guardrail names the way of hitting the north star it catches |

Uber's 10-K for 2025 counts an UberX Share ride with three paying riders as three trips (checked 12
October 2026). The north star read 35.76 trips per online driver-week before and 35.89 after.

### What did hours cost, and what would the redesign save?

61 percent of the Rs 1.9 crore, Rs 1.159 crore, went to driver-weeks that accepted fewer than half
their offers. If some idle drivers start accepting, so that a fifth to a half of that is still paid,
the redesign saves Rs 58 lakh to Rs 92.7 lakh over six weeks: an assumption with a range, which the
test of the redesign settles.

### What do the three roles say?

Driver operations: "drivers will log off". True for the idle tail, and the wait guardrail shows any
real loss. Marketing: "changing terms looks like
bait". True, so the floor stays for drivers who accept. Finance: "the monsoon explains it". Partly;
the busiest weeks already read 1.60.

A north star read alone misleads the other way too: Swiggy's Maxxsaver raised Instamart's average
order value 16 percent to Rs 612 while cart consolidation lowered order growth, so orders per month
would have read a success as a fall (Q1 FY26 letter, checked 12 October 2026).

**Explorer scenes M2 to M4:** the seesaw of what the scheme pays for, the definition rebuilt line by
line on the twelve rows, and acceptance turning before bookings per hour.

**Say it to a driver.** "The floor now pays for trips you complete, if you say yes to most offers."


## How would you measure the success of a new feature, in an interview?

**Who needs the answer.** You, in a product or analytics screen.

**The questions on the way.** What does a hire-grade answer do? How does it move to an AI product?
Which follow-ups come next?

### What does a hire-grade answer do?

It clarifies first (what the scheme is for, who is in it, what counts as harm), then gives the
structure: goal, user, one metric with numerator, denominator and window, two guardrails, one leading
input, and the test. The trap is naming online hours and stopping. Weak: "hours are up 24 percent, so
it works." Hire-grade: "hours rose 24 percent, yet trips per online hour fell from 1.90 to 1.58 and
waits barely moved; 180 drivers sat idle, mostly in the outer zones; I would pay for completed peak
trips with an acceptance floor and test that before extending it."

### How does it move to an AI product?

An AI coding assistant's team reports suggestions accepted, a proxy gamed by short suggestions
accepted and then deleted. The outcome is suggested text still in the code at the next commit; the
guardrails are build failures, the revert rate and time to merge; the test is a holdout of users.
Programme-written; it names no company figure.

### Which follow-ups come next?

"Online hours rose 24 percent; what do you check before you celebrate?" Trips per online hour and the
rider's wait. "Which guardrail would driver operations fight, and why are they partly right?" The
acceptance floor, since some declines are fair; the floor sits in the gap the data shows. "Drivers
control when they log in; what happens to your number?" The numerator needs a rider's request, so
logging in alone cannot raise it.


## Which pain points has each real case already paid for?

- **A target with no usage condition:** Wells Fargo's cross-sell ratio (SEC order, Release 34-88257).
- **The measured control where the window starts:** VA's "desired date" (VA OIG, 2014).
- **A definition changed in silence:** Wells Fargo's unannounced 2013 addition of remittance
  accounts, 0.04 of that year's 0.11 rise (SEC order).
- **A gross figure read as money earned:** Eternal's move from GOV to NOV (Q1 FY27 letter).
- **A count that goes negative when cancellations are netted:** Airbnb's nights booked, net of
  cancellations, minus 4.1 million in March 2020 (S-1, 2020).
- **An open screen counted as activity:** Spotify's monthly active user, any account with more than
  zero milliseconds of consumption in thirty days (20-F for 2025).

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
| Ratio of sums | Add every numerator, add every denominator, divide once |
| Idle tail | The 180 drivers under one trip per peak online hour after the launch |
| Offer | One rider request shown to one driver |


## So is the number the scheme pays for measuring what the city wants?

No. Peak online hours rose 24 percent while trips per peak online hour fell from 1.90 to 1.58 and the
wait barely moved, and Rs 1.159 crore of the Rs 1.9 crore top-up went to driver-weeks that declined
most offers. Pay for completed peak trips per enrolled driver online at peak, guarded by acceptance,
the wait and the top-up per trip. Tuesday puts that on one slide.

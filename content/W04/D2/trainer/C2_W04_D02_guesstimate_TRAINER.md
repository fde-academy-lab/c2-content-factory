# Guesstimate note, Week 4 Tuesday: what are the day's three estimates, their anchors and their catches?

**TRAINER ONLY.** The worked versions of the day's estimates: drivers at the evening peak (worked with
the room), UPI payments a day (in pairs), and Anand's new store (in the lab). Every value in a chain is
an assumption said aloud with its range.

**Who needs the answer.** The trainer working the chain on the board, and the TA running the lab.

**The questions on the way.** What does each chain multiply out to? Which factor sets the range? What
checks it, and what is the catch?

## How many drivers must be online at the weekday evening peak?

**Who needs the answer.** The trainer at S37 to S42. **The questions on the way.** Which values, which
range, which check?

| Factor | Central | Range | Why |
|---|---|---|---|
| People in the Hyderabad metro area | 1 crore | 0.9 to 1.1 crore | A round number said aloud, to be checked |
| Weekday Uber trips per person | 1 per 100 people | 0.5 to 1.5 per 100 | Counted in trips, so a commuter who rides both ways counts twice; the least known factor |
| Share of the day's trips in the three evening hours | a quarter | 20 to 30 percent | Evening commute |
| Trips a busy driver fits in an hour | 2.4 | 2 to 3 | A peak trip takes about 25 minutes from accepting to dropping |
| Idle share at a given moment | 0.30 | 0.22 to 0.38 | A guess from a busy evening to a slack one; the validate step checks it like for like |
| Buffer for the busiest half hour | 1.15 | 1.10 to 1.25 | The peak inside the peak |

**The chain.** 1 crore x 1 per 100 = 1 lakh trips a day; x a quarter = 25,000 in the window; / 3 hours
= about 8,330 trips an hour. Trips per online driver-hour = 2.4 x 0.70 = 1.68. 8,330 / 1.68 = about
4,960; x 1.15 = about 5,700 drivers.

**The range, one factor at a time.** Trips per person: about 2,900 to 8,600. The evening share and a
busy driver's trips: about 4,600 to 6,800 each. The idle share: about 5,100 to 6,400. People in the
city: about 5,100 to 6,300. The buffer: about 5,500 to 6,200. Trips per person sets the range, and the
chain is a product, so doubling it doubles the answer, to about 11,400. With every factor at its bad end
at once the range is far wider; say which range you are giving.

**The check, like for like.** The case's twelve zones used 0.53 online driver-hours per completed trip
before the launch (118,000 hours over 224,200 trips, median wait 4.8 minutes) and 0.63 after. The chain
puts 1 / 1.68 = 0.60 behind each trip before its buffer, about an eighth more than the window whose
wait met the target, so it errs high; re-run at the case's 1.90 trips an hour it gives 8,330 / 1.90 x
1.15 = about 5,000. Say 5,000 to 5,700. Per request the case reads 0.47, but that divides by requests,
11 percent of which nobody served, while the chain counts trips: compare per trip. The idle share
checks the same way: 1.90 trips x 25 minutes leaves about 0.21 idle before the launch, 0.34 after. The
case pools both daily windows on all seven days (42 hours a week; 256,556 after-window requests are
about 1,018 an hour), so it checks the ratio's size, never the city's count.

**The four-hour window.** Nothing changes at the busiest moment: 25,000 trips over four hours is about
6,250 an hour on average, the buffer for the same busiest half hour rises to about 1.53, and the answer
stays about 5,700. A learner who says about 4,300 has let a longer window shrink the peak.

**The anchor: to be found.** No published figure for Uber drivers online at Hyderabad's evening peak
exists in the research ledger. A search on 12 October 2026 found only undated or decade-old counts of
drivers signed up, which is a different unit, so the slot stays "to be found". In a candidate's mouth
it is "I don't know a public count; I would ask for Uber's own count of drivers online at peak."

**The catch.** A day's trips divided by an hour's rate: 1 lakh / 2.4 = about 41,700 drivers, about
seven times the chain. The case file names the idle share as the factor that moves the answer most;
with trips built up from people, as the spine's L5 asks, trips per person moves it more, and the room is
told so. The idle share is the one factor Monday's data shows moving.

## How many UPI payments happen in India on an average day?

**Who needs the answer.** The trainer at S43 and S44. **The questions on the way.** Which worked chain,
which anchor, which catch?

| Factor | Central | Range |
|---|---|---|
| Active UPI users | about 35 crore (one in four of roughly 140 crore people) | 25 to 45 crore |
| Payments per active user a day | about 2 | 1 to 3 |

**The chain.** 35 crore x 2 = 70 crore, or 700 million, a day (1 crore is 10 million). One factor at a
time: users give 50 to 90 crore; payments a day give 35 to 105 crore, so payments a day set the range.

**The anchor.** An average of 802 million UPI transactions a day in September 2026, and 24.07 billion
in the month worth Rs 29.37 lakh crore (Outlook Money, 2 October 2026, citing NPCI's data; checked 12
October 2026). The worked chain sits 13 percent below: the same order, a little low.

**The catch, and the sharper check.** September has 30 days: 24.07 billion / 30 = 802 million.
Dividing by 31 gives 776 million, about 3 percent low, a slip small beside the estimate's own range.
The same report gives a check that teaches more: Rs 29.37 lakh crore over 24.07 billion is about Rs
1,220 a payment, far above a cup of tea, so the count holds large transfers between people, and the 2
payments a day have to be split between shops and people. The figure of 35 crore active users has no anchor of its own.

## How many customers could a new Kalpa store sign up to Retail-Plus in its first year?

**Who needs the answer.** The TA in the lab. **The questions on the way.** Which chain, which check,
which catch? Anand's question is proposed for client zero v2.3.

| Factor | Central | Range |
|---|---|---|
| Households near the store | 50,000 | 30,000 to 80,000 |
| Share who shop there in year one | 0.4 | 0.25 to 0.5 |
| Share of those shoppers who sign up | 0.05 | 0.02 to 0.08 |
| Visits a month per shopping household | 2 | 1 to 4 |
| Spend per visit | Rs 1,500 | Rs 1,000 to Rs 2,000 |

**The chain.** 50,000 x 0.4 = 20,000 shoppers; x 0.05 = about 1,000 sign-ups.

**The range.** One factor at a time: households give 600 to 1,600 sign-ups, the share who shop 625
to 1,250, the share who sign up 400 to 1,600. The sign-up share sets the range, and the DMart check
cannot reach it; Kalpa's own sign-up rate at its existing stores would be the like-for-like anchor,
and it is not in the lab's data.

**The check.** 20,000 x 2 visits x Rs 1,500 x 12 months = Rs 72 crore a year, about half of DMart's
about Rs 146 crore a store on the average of its opening and closing counts (Rs 66,968 crore over
457.5 stores; Avenue Supermarts release of 2 May 2026, checked 12 October 2026). A first-year store at about
half a mature store's sales passes; a first-year store above a mature store's sales would fail.

**The catch.** A store in its first year sells less than a mature one, and DMart's average spans stores
of several sizes; its release gives stores two years and older their own growth figure, 10.8 percent in
the last quarter of FY26. The year-end count gives about Rs 134 crore, about 9 percent lower.

## Why does the canteen's tea open the dojo?

The warm-up is a toy, invented for this class: 2,000 students x 0.6 who buy tea x 2 cups = 2,400 cups,
validated against the canteen's till or a count at the counter for one busy half hour. It shows the
four steps on numbers nobody will argue with, before the city head's question.

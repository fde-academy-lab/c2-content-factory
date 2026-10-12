# Can the day's slide and the day's estimate survive Kalpa's own questions?

The TA-led practice lab after the afternoon block. The morning's studio and the afternoon's dojo run
once more, on Kalpa Retail, the programme's client: first a three-minute slide to a TA who plays one of
Kalpa's heads, then Anand Iyer's question about a new store, sized from nothing and checked. A short
ladder of practice problems follows for anyone who finishes early or wants another climb.

**Who needs the answer.** Meera Raghavan, Kalpa Retail's CEO, who wants one metric the company
chases, and Anand Iyer, its finance controller, who funds or does not fund a new store.

**The questions on the way.**

- Can your Kalpa north-star slide survive one head's objection?
- How many customers could a new store sign up to Retail-Plus in its first year?
- Can you climb the day's ladder once more, from a title to a combined slide and estimate?

---

## Can your Kalpa north-star slide survive one head's objection?

This comes up at work the first time a metric you wrote meets the people whose targets it replaces.

Fill in `exercises/guided/C2_W04_D02_kalpa_slide_template_STUDENT.md` with Monday's metric, delivered
orders per active customer per month, and its three guardrails. Present it in three minutes to the TA,
who plays the marketing lead, Operations or the head of Retail-Plus and raises one objection. Answer it
in the four moves. The TA hands back the scorer's card: the four parts of the slide and the four moves,
present or absent.

---

## How many customers could a new store sign up to Retail-Plus in its first year?

This comes up at work whenever a store, a branch or a delivery-only warehouse is funded before it exists.

Size it in fifteen minutes, aloud, on one sheet:

| Step | What to do |
|---|---|
| Clarify | Say what counts as a sign-up, which store and which twelve months |
| Map | Build a chain from the households near the store to the members it signs, each factor with a value and a range |
| Calculate | Say the running product aloud |
| Validate | Nobody publishes sign-ups, so turn your shoppers into a year of sales (visits a month and spend per visit, both stated) and set it beside DMart's revenue per store from `data/C2_W04_D02_kalpa_dmart_anchor_STUDENT.csv`: about Rs 146 crore on the average store count, the stores open across the year (the year-end count gives about Rs 134 crore and understates a store); say what the gap tells you, and name the factor the check cannot reach |

The catch to say aloud: a store in its first year sells less than a mature one.

---

## Can you climb the day's ladder once more?

This comes up in every interview loop: the same idea asked at rising difficulty until it breaks.

**P1. Level L1.** Rewrite each topic title as a claim a reader can act on: "Q2 revenue review";
"Retail-Plus update"; "Store sign-ups, September". Invent the finding each claim states and say that
you invented it.

**P2. Level L2.** A food stall (invented for this lab) took Rs 12,000 in a day from 240 orders, with
staff working 40 hours across 5 staff-days. Give sales per order, per staff-hour and per staff-day,
and say which one a scheme that pays staff by the hour should read.

**P3. Level L3.** Write the four moves for the driver-operations lead's objection to the Uber
redesign, "drivers will log off and supply at peak will fall", using the numbers on the morning deck's
S20.

**P4. Level L4.** A Kalpa slide draft carries six elements: the north-star chart, a table of all
orders, the discount share, the return rate, a pie of orders by channel, and a paragraph on method.
Keep two, and name the head whose appendix page receives each of the others.

**P5. Level L5, combining the day.** Anand asks for one slide: should Kalpa fund the new store? Build
it with your estimate from the second part as the evidence (its range and the factor that sets it),
the first-year catch as the caveat, and the action with what it commits and who signs.

**For anyone who stalls on code.** These four lines rebuild the twelve rows' per-driver-week read.
Put them in the only order that runs, as a letter string:

- (p) `print(t[["peak_bookings_rs", "driver_weeks", "rs_per_driver_week"]])`
- (q) `t = rows.groupby("window")[["peak_online_hours", "peak_trips", "peak_bookings_rs"]].sum()`
- (r) `t["rs_per_driver_week"] = t.peak_bookings_rs / t.driver_weeks`
- (s) `t["driver_weeks"] = rows.groupby("window").size()`

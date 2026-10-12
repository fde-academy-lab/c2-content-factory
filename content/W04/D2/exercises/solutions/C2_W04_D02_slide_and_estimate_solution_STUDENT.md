# Which letters answer the guided set on rebuilding a slide and sizing a number?

Answers: 1d 2c 3a

The case: Uber's peak-hour guarantee in Hyderabad, where gross bookings per peak online hour fell from
Rs 314 to Rs 260 at a fare that held at Rs 165 after the launch on 31 August 2026. The set rebuilt
three cluttered slides (A worked, B half worked, C blank) and sized drivers at the weekday evening
peak (the canteen's tea worked, the drivers' chain half worked, UPI left for the afternoon).

## What does the set test?

A slide that carries one claim needs one number that proves it and a denominator that matches the
decision. Slide B's drafted claim is about where the top-up went, so the proving number is the top-up
split. Slide C's claim is about idle drivers, and the scheme pays per online hour, so the evidence is
read per peak online hour. The chain's middle step turns a busy driver's trips into trips per online
driver: 2.4 trips in a busy hour, with 30 percent of online drivers idle at a given moment, is
2.4 x 0.70 = 1.68 trips per online driver-hour.

## Why is each key right, and why does each other option fail?

| Item | Key | The question in one line | Why the key holds | Why each other option fails |
|---|---|---|---|---|
| 1 | d | Which number proves "Rs 1.16 crore of the top-up went to driver-weeks that accepted fewer than half their offers"? | Rs 1.16 crore of the Rs 1.9 crore paid is the claim's own number, with the total it is a share of beside it. | a: Rs 82.3 per trip is the average over every trip, so it cannot say where the money went. b: the per-driver-week read rose 0.8 percent for reasons unrelated to the top-up (bookings up 3.0 percent, active driver-weeks up 2.2 percent). c: rider requests rose 1.8 percent, which is demand, and says nothing about the top-up. |
| 2 | c | Which denominator should slide C's evidence name, given that the scheme pays per peak online hour? | The decision is what the scheme should pay for, and it pays per online hour, so the evidence is read in the unit the money is spent in. | a: per active driver-week counts every driver with a row once and hides how many of their hours were idle. b: per trip is flat at Rs 165 and cannot show idle hours at all. d: enrolment counts sign-ups, which is marketing's unit and was never the scheme's. |
| 3 | a | With 2.4 trips in a busy hour and 30 percent of online drivers idle, what is trips per online driver-hour? | Only the 70 percent with a rider complete trips, so 2.4 x 0.70 = 1.68. | b: 2.40 forgets that idle drivers complete nothing. c: 3.43 divides 2.4 by 0.70, which makes idle time raise output. d: 0.72 multiplies by the idle share, the 30 percent who complete nothing. |

## Which item is worth arguing about?

Item 2. Some will argue for per active driver-week because it is what each driver takes home in a
week. That read rose 0.8 percent, and the rise came from bookings growing 3.0 percent while active
driver-weeks grew 2.2 percent (the 140 drivers who joined after the launch drove only some weeks), so
it would let the slide say "drivers earn more" while the scheme pays for hours that carry no trips.
The slide names the unit the money is spent in; the other reads go in the appendix with a line each
on what moved them.

## Where does matching the denominator to the decision show up at work?

Every pay scheme is a denominator: per hour, per trip, per delivery, per active day. A review slide
that reads the money in a different unit from the one the scheme pays in lets each role pick the read
that flatters it. The same rule decides whether a cloud bill is read per request or per user, and
whether an AI product's cost is read per query or per active seat.

## What does notebook 01 confirm?

`notebooks/C2_W04_D02_01_makeover_and_ledger_STUDENT.ipynb` prints the three reads on the twelve rows
and on all driver-weeks (items 1 and 2), and its ledger cell computes 2.4 x (1 - 0.30) = 1.68 and
about 5,700 drivers (item 3). Hands-on picks: the three predict cells answer a, b and b.

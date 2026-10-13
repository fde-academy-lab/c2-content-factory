# Which letters answer the guided set on rebuilding a slide and sizing a number?

Answers: 1d 2c 3b

The case: Uber's peak-hour guarantee in Hyderabad, where gross bookings per peak online hour fell from
Rs 314 to Rs 260 at a fare that held at Rs 165 after the launch on 31 August 2026. The set rebuilt
three cluttered slides (A worked, B half worked, C blank) and sized drivers at the weekday evening
peak (the canteen's tea worked, the drivers' chain half worked, UPI left for the afternoon).

## What does the set test?

A slide that carries one claim needs one number that proves it and a denominator that matches the
decision. Slide B's drafted claim says "most" of the top-up, so the proving number is a share of the
total: the top-up split. Slide C's claim is about what the scheme now buys, and the guarantee is priced
per online hour, so the evidence is read per peak online hour. The chain's middle step turns a busy
driver's trips into trips per online driver: only the share with a rider completes trips, so at an
idle share of 0.38 it is 2.4 x 0.62 = about 1.49 trips per online driver-hour.

## Why is each key right, and why does each other option fail?

| Item | Key | The question in one line | Why the key holds | Why each other option fails |
|---|---|---|---|---|
| 1 | d | Which number proves "Most of the top-up went to driver-weeks that accepted fewer than half their offers"? | Rs 1.16 crore of the Rs 1.9 crore paid is 61 percent, more than half, so it carries "most" with its total beside it. | a: the per-driver-week read is bookings, which says nothing about where the top-up went (it rose because each driver-week carried about four more online hours). b: Rs 74 lakh is the part that went to everyone else; without the total it cannot show a majority. c: Rs 82.3 per trip is an average over every trip, so it cannot say who received the money. |
| 2 | c | Which denominator should slide C's evidence name for what the scheme running now buys? | The guarantee running now is priced per peak online hour, so the evidence is read in the unit the money is spent in. | a: per active driver-week counts every driver with a row once and hides how many of their hours were idle. b: per trip is what Monday's redesign would pay for, and it is flat at Rs 165, so it cannot show idle hours at all. d: enrolled drivers is marketing's count, and every driver in the data is enrolled, so it divides by a number that never moved with the idle hours. |
| 3 | b | With 2.4 trips in a busy hour and an idle share of 0.38, what is trips per online driver-hour? | Only the 62 percent with a rider complete trips, so 2.4 x 0.62 = about 1.49, and the chain then needs about 6,400 drivers. | a: 0.91 multiplies by the idle share, the drivers who complete nothing. c: 2.02 subtracts a share from a rate, mixing two units. d: 3.87 divides 2.4 by 0.62, which makes idle time raise output. |

## Which item is worth arguing about?

Item 2. Some will argue for per active driver-week because it is close to what each driver takes home
in a week. That read rose 0.8 percent because the average driver-week carried about four more online
hours (18.6 to 22.5) while each hour brought in 17 percent less; the rise sits with the 880 outside
the idle tail, who drove more hours at an unchanged rate, so it would let the slide say "drivers earn
more" while the scheme pays for hours that carry no trips. The slide names the unit the money is spent
in; the other reads go in the appendix with a line each on what moved them.

## Where does matching the denominator to the decision show up at work?

Every pay scheme has a denominator: per hour, per trip, per delivery, per active day. A review slide
that reads the money in a different unit from the one the scheme pays in lets each role pick the read
that flatters it. The same rule decides whether a cloud bill is read per request or per user, and
whether an AI product's cost is read per query or per active seat.

## What do notebooks 04 and 08 confirm?

`notebooks/C2_W04_D02_04_case_one_slide_answer_three_denominators_STUDENT.ipynb` prints the three reads
on the twelve rows and on all driver-weeks (items 1 and 2), and its two predict cells answer c and b.
`notebooks/C2_W04_D02_08_case_guesstimate_drivers_at_peak_STUDENT.ipynb` computes the chain at 2.4 x
(1 - 0.30) = 1.68 and how far the idle share moves it, up to about 6,400 drivers at 0.38 (item 3); its
ledger cell's predict answers a.

# How do you rebuild a cluttered slide, and size a number aloud, one step at a time?

Uber, Hyderabad, the driver app's peak-hour earnings guarantee, one day on. On Monday 31 August 2026
the city team began guaranteeing enrolled drivers Rs 300 for every peak hour they stay online, paying
the gap above their trip earnings as a top-up. Over the six weeks after the launch, peak online hours
rose 24 percent while completed peak trips rose 3 percent, so gross bookings per peak online hour
(what riders paid for trips, divided by the hours drivers were online) fell from Rs 314 to Rs 260 at a
fare that held at Rs 165. The city head takes the redesign to Thursday's city review on one slide, and
before the review wants a rough count of the drivers the weekday evening peak needs.

> Illustrative case: the company is real, the situation and the data are synthetic, built for this class.

**Who needs the answer.** The city head, who has five minutes and one slide, and the analyst who
must size a number with no dataset before the same review.

**The questions on the way.**

- What does a cluttered slide look like once it carries one claim?
- Which number proves a drafted claim, and which denominator should a slide name?
- How does a chain of assumptions multiply out to drivers at the evening peak?

You work this set with the trainer: the first slide and the first estimate are worked in full, the
second of each is half worked, and the third is yours. Post one line, three letters in item order,
no spaces:

```
Post exactly this shape: xxx
```

---

## What does slide A look like once it carries one claim?

This comes up at work whenever a dashboard is pasted into a review deck: someone has to choose the
one sentence the meeting is for.

Slide A arrived titled "Peak guarantee: six-week review" with nine numbers of equal weight. Worked in
full, it becomes four parts:

| Part | What slide A now says |
|---|---|
| 1. The claim, as the title | The scheme is paying for online hours that carry no trips |
| 2. The evidence, with its denominator | A chart of gross bookings per peak online hour over twelve weeks: Rs 314 before, Rs 260 after, the drop in the launch week |
| 3. The caveat, beside the evidence | The monsoon ended inside the window, and last year's weeks are not in the data |
| 4. The action, its cost, who signs | Pay per completed peak trip with an acceptance floor: Rs 58 lakh to Rs 92.7 lakh back over six weeks depending on whether half or a fifth of idle drivers start accepting; the city head signs |

The saving comes from Monday: Rs 1.16 crore of the Rs 1.9 crore top-up went to driver-weeks that
accepted fewer than half the requests offered to them. If a fifth to a half of that is still paid,
because those drivers start accepting, the rest comes back.

---

## Which number proves slide B's drafted claim?

This comes up at work when finance sends a tab of nine money numbers and the slide can show one.

Slide B, half worked. The claim is drafted: "Rs 1.16 crore of the top-up went to driver-weeks that
accepted fewer than half their offers." Finance's tab holds these nine:

| Finance's tab | Before | After |
|---|---|---|
| Gross peak bookings | Rs 3.70 crore | Rs 3.81 crore |
| Bookings per online hour | Rs 314 | Rs 260 |
| Bookings per active driver-week | Rs 5,817 | Rs 5,861 |
| Bookings per trip | Rs 165 | Rs 165 |
| Top-up paid | Rs 0 | Rs 1.9 crore |
| Top-up per completed trip | | Rs 82.3 |
| Top-up to low acceptance | | Rs 1.16 crore |
| Top-up to everyone else | | Rs 74 lakh |
| Rider requests | 251,910 | 256,556 |

Low acceptance means a driver-week that accepted fewer than half the requests offered. An active
driver-week is one driver with a row in the week's table.

### Q1. Which one number from finance's tab proves the drafted claim?

*Level L1 · asked in every analyst screen.*

a) Top-up per completed trip, Rs 82.3 in the six weeks after the launch
b) Bookings per active driver-week, Rs 5,817 before and Rs 5,861 after
c) Rider requests, 251,910 before and 256,556 after the launch
d) Top-up to low acceptance, Rs 1.16 crore of the Rs 1.9 crore paid

---

## Which denominator should slide C name?

This comes up at work whenever one total can be divided by several things and each division tells a
different story.

Slide C, blank. Driver operations' tab shows 180 drivers in the idle tail (Monday's name for the
drivers whose trips per online hour fell under 1.0 after the launch): their online hours rose from
20,000 to 42,000 while their trips fell from 38,000 to 33,440. You write the claim; first choose the
denominator its evidence will name.

### Q2. Design. The scheme pays drivers for each peak hour online. Which denominator should slide C's evidence name?

*Level L2, a design call · asked in GCC and product-company screens.*

a) Per active driver-week, since every driver with a row that week counts once
b) Per completed trip, since a trip is what a rider pays for
c) Per peak online hour, since the scheme pays for each online hour
d) Per enrolled driver, since enrolment is the number marketing reports

---

## How many cups of tea does the campus canteen sell on a weekday?

This comes up in interviews as the warm-up, and at work whenever a number is needed before the data is.

Worked in full, with invented numbers. **Clarify:** one canteen, one weekday, cups and not litres.
**Map:** students on campus x share who buy tea x cups each. **Calculate:** 2,000 x 0.6 x 2 = 2,400
cups. **Validate:** the canteen's till for one weekday, or cups counted at the counter for one busy
half hour.

---

## How many drivers must be online at the weekday evening peak?

This comes up at work when an operations lead needs a number for a meeting that will not wait for data.

Half worked. Clarify: the Hyderabad metro area, Uber only, drivers online at one moment of the
three-hour weekday evening peak, a median rider wait under five minutes. The chain:

| Factor | Value, an assumption said aloud |
|---|---|
| Rider requests an hour | 1 crore people x 1 percent who ride on a weekday x a quarter of the day's trips in the evening / 3 hours = about 8,300 |
| Trips one online driver completes an hour | __________ |
| Buffer for the busiest half hour | 1.15 |
| Drivers online | about 8,300 / the blank x 1.15 = about 5,700 |

### Q3. A busy driver fits 2.4 trips in an hour, and 30 percent of online drivers have no rider at a given moment. Which number fills the blank?

*Level L5 · asked in product-company and consulting screens.*

a) 1.68
b) 2.40
c) 3.43
d) 0.72

---

## What is left for you to size?

The third estimate is the afternoon's paired drill: UPI payments in India on an average day, in
seven minutes, all four steps on one sheet. Bring it to the dojo.

**How do you check your letters against the notebook?** Open
`notebooks/C2_W04_D02_01_makeover_and_ledger_STUDENT.ipynb`: its second and third code cells compute
the three reads of the rupees, and its sixth code cell computes the chain and the drivers online. Change a
letter only if your reasoning changes with it.

**In the interview.** [S] Present a recommendation to a non-technical stakeholder in two minutes.
[S] A guesstimate: how many drivers must be online at the evening peak?

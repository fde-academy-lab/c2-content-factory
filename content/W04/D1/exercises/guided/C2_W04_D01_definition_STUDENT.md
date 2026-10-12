# What does a complete definition of the number the scheme pays for say, line by line?

*Illustrative case: the company is real, the situation and the data are synthetic, built for this class.*

**The ticket, in short.** Uber, Hyderabad, the driver app. From Monday 31 August 2026 an enrolled
driver who stays online through a whole peak window (two windows a day, three hours each) is
guaranteed Rs 300 per peak online hour, and Uber tops up the gap between the driver's trip earnings
and that floor. The launch note's goal: riders picked up faster. Six weeks each side of the launch:

| Measure | 20 Jul to 30 Aug | 31 Aug to 11 Oct |
|---|---|---|
| Peak online hours | 118,000 | 146,300 (up 24 percent) |
| Completed peak trips | 224,200 | 230,900 (up 3 percent) |
| Trips per peak online hour | 1.90 | 1.58 |
| Offers accepted over offers shown | 0.86 | 0.73 |
| Median rider wait at peak, minutes | 4.8 | 4.6 |
| Top-up paid | Rs 0 | Rs 1.9 crore |

The city head asks, by Friday: is the scheme working, which metric should it pay for, and is anyone
gaming it?

**Who needs the answer.** The city head, who pays the top-up every week and decides on Friday
whether the scheme continues, changes or spreads to two more cities. A number that can rise while
riders wait just as long sends money to the wrong drivers, Rs 1.9 crore of it in six weeks.

**The questions on the way.** What should the number count on top? What should it divide by? What
is left out of both counts? Which guardrail catches a driver who picks only easy trips? What does
the finished definition read on the data?

You build this with the trainer in chapter 3, one line at a time. The room calls each letter aloud
before the trainer writes the line. Items marked **Design** ask for the best-fit approach, the fact
that would switch it, or the second route that would confirm a number.

```
Post exactly this shape: xxxx
```

---

## What does a complete definition hold?

A definition you can pay against has seven lines. The first four make the number computable; the
last three make it hard to game.

| Line | What it says, in plain words |
|---|---|
| Numerator | What is counted on top |
| Denominator | What the count is divided by, with that count printed beside the rate |
| Window | The stretch of time each count covers |
| Exclusions | What is left out of both counts, and why |
| What it does not reward | The behaviour the number refuses to pay for, named out loud |
| Guardrails | Numbers that must not get worse while the main number rises |
| Gaming note | For each guardrail, the way of hitting the main number it catches |

The room has already chosen the main number, the **north star** (the one number the scheme exists to
move): completed peak trips per enrolled driver online at peak, per week. A trip is completed when
the rider was picked up and dropped. An **offer** is one request shown to one driver; a request one
driver declines is offered to the next.

---

## What should the number count on top?

The numerator is where a team at Uber, Swiggy or any marketplace decides what it is paying for, so
it is the line every later argument goes back to.

### Q1. Design. Which numerator should the north star count?

a) Peak online hours, summed over every enrolled driver that week

b) Offers accepted inside the peak windows, summed over the week

c) Trips completed inside the peak windows, one per paying rider

d) Trips completed at any hour of the day, peak or not, that week

---

## What should the count be divided by?

A denominator decides who can move the rate without doing the work, which is why a reviewer asks
for its count before trusting any ratio.

### Q2. Which denominator keeps a sign-up who never drives from moving the rate?

a) Every driver enrolled in the scheme that week, whether or not they log in

b) Enrolled drivers online at least one peak hour that week, count printed

c) Drivers who completed at least one peak trip in that same calendar week

d) The peak online hours that enrolled drivers logged that week

---

## What is left out of both counts?

Exclusions are where definitions change quietly, so a written list with a reason for each is what
lets next quarter's number be compared with this one.

### Q3. The window is the calendar week. Which exclusions belong in the definition?

a) Trips in the three outer zones, since riders there are few at any hour of day

b) Drivers who joined after the launch, since they had no week before it

c) The monsoon weeks, since the season moved rider requests in that window

d) Trips cancelled by either side, test accounts, trips outside the windows

---

## Which guardrail catches a driver who picks only easy trips?

A guardrail is the number a reviewer reads beside the north star; marketplaces watch one for each
way the main number can be hit badly.

### Q4. Design. Paid per completed trip, a driver accepts only short or nearby trips and declines the rest. Which guardrail catches it?

a) Accepted share of offers, at or above a floor the city sets

b) Median rider wait at peak, read zone by zone each week

c) Top-up per completed trip, read each week against the budget

d) Peak online hours per enrolled driver, read each week

---

## What does the finished definition read on the data?

Fill each line as the room settles it. Round 3 this afternoon hands this template back to your group,
and the values come from notebook 03, `notebooks/C2_W04_D01_03_definition_and_cost_STUDENT.ipynb`,
whose definition cell prints them for the six weeks before and after the launch.

| Line | Your definition |
|---|---|
| North star | Completed peak trips per enrolled driver online at peak, per week |
| Numerator | |
| Denominator | |
| Window | The calendar week |
| Exclusions | |
| What it does not reward (the behaviour that earns nothing: three things the old number paid for) | |
| Guardrail 1 | |
| Guardrail 2 | |
| Guardrail 3 | |
| Gaming note, one line per guardrail | |

| Read on the data | Before | After |
|---|---|---|
| North star, trips per online driver-week | | |
| Guardrail: offers accepted over offers shown | | |
| Guardrail: median rider wait at peak, minutes | | |
| Guardrail: top-up per completed trip, Rs | | |

**The hands-on part.** Run notebook 03 top to bottom, copy the four pairs of values into the table
above, and post your four letters.

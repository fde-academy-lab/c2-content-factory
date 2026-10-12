# Which of the city's numbers move before the north star, and which guardrail does each proposed north star need?

*Illustrative case: the company is real, the situation and the data are synthetic, built for this class.*

**The ticket, in short.** Uber, Hyderabad, the driver app. From Monday 31 August 2026 an enrolled
driver who stays online through a whole peak window is guaranteed Rs 300 per peak online hour, and
Uber tops up the gap. In the six weeks after the launch, against the six weeks before, peak online
hours rose 24 percent, completed peak trips rose 3 percent, and trips per peak online hour fell from
1.90 to 1.58. The city head asks, by Friday, whether the scheme works, what it should pay for, and
whether anyone is gaming it.

**Who needs the answer.** The city team, who read one dashboard every Monday morning and act on it
that week. A dashboard of numbers that only confirm what already happened lets a drift run for weeks
before anyone sees it; a north star without a guardrail pays for the drift.

**The questions on the way.** Which of eight numbers move first? Which reasons defend two of those
calls? Which guardrail does each of three proposed north stars need?

You sit this set in the practice lab, or in section 8 of the metric clinic if the tentative faculty
block does not run. Every item has one right answer. Items marked **Design** ask for the best-fit
approach, the fact that would switch it, or the second route that would confirm a number.

```
Post exactly this shape: xxx
```

---

## Which words does this set use?

| Word | What it means here |
|---|---|
| North star | The one number the scheme exists to move. Here: completed peak trips per enrolled driver online at peak, per week |
| Leading number | A number that moves before the north star does, which the city team can act on this week, for example by moving drivers toward zones where requests per online hour are high |
| Lagging number | A number that confirms the north star after the trips have happened: a bill, a rating, a departure, a quarter's total |
| Guardrail | A number that must not get worse while the north star rises, because it catches one way of hitting the north star badly. Leading and lagging say when a number moves, and a guardrail is a job a number does, so one number can be both |
| Offer | One rider request shown to one driver; a request one driver declines is offered to the next |

---

## Which of eight numbers move first?

Every operations dashboard at a marketplace sorts its numbers this way, so the team knows which ones
it can still change this week.

| # | A number on the city's dashboard |
|---|---|
| 1 | Rider rating at month end |
| 2 | Share of offers accepted this week |
| 3 | Gross bookings for the quarter |
| 4 | Enrolled drivers online in the first peak hour |
| 5 | Top-up paid for the month |
| 6 | New driver sign-ups this week |
| 7 | Drivers who left the platform the next quarter |
| 8 | Rider requests per online hour, by zone |

### Q1. Which list holds every leading number among the eight, and nothing else?

a) 2, 4, 6 and 8

b) 1, 2, 4 and 8

c) 2, 4 and 8 only

d) 2, 3, 5 and 6

---

## Which reasons defend two of those calls?

A call on a dashboard is only as good as the reason said beside it, because the next person to read
the dashboard will move a number only if the reason convinces them. On the case data the share of
offers accepted fell to 0.729 in the launch week itself and stayed there, while gross bookings per
online hour, the weekly form of number 3, fell to Rs 271 that week, Rs 261.7 the next and Rs 259.1
the third.

### Q2. Which reason defends calling number 2 leading and number 3 lagging?

a) A share always moves before a rupee total, so number 2 must lead number 3

b) The city team reads acceptance every day, while finance reads bookings once a quarter

c) Acceptance hit its new level in the launch week; bookings add up trips already done

d) Acceptance rose after the launch while bookings fell, and a rise leads a fall

---

## Which guardrail does each proposed north star need?

Every proposed north star has a way of being hit while riders are served worse, and a team that
proposes one is expected to name its guardrail in the same breath.

| # | Proposed north star | How it could be hit while riders wait longer |
|---|---|---|
| 1 | Completed peak trips per enrolled driver per week | Drivers accept short trips and decline the rest |
| 2 | Peak online hours per enrolled driver per week | Drivers sit online in zones with no riders |
| 3 | Enrolled drivers | Drivers sign up for the floor and never drive |

| Guardrail | What it reads |
|---|---|
| G1 | Share of offers accepted, at or above a floor the city sets |
| G2 | Share of online hours with no completed trip |
| G3 | Share of enrolled drivers online at least one peak hour that week |
| G4 | Total peak online hours across the city |

### Q3. Design. Which guardrail belongs with each north star, with one guardrail left over?

a) 1 with G2, 2 with G1, 3 with G3

b) 1 with G1, 2 with G4, 3 with G3

c) 1 with G3, 2 with G2, 3 with G1

d) 1 with G1, 2 with G2, 3 with G3

---

## Where do you check your calls on the data?

Open notebook 03, `notebooks/C2_W04_D01_03_definition_and_cost_STUDENT.ipynb`, and find the cell
under "Which number moved first?". It prints the share of offers accepted and the bookings per online
hour for the three weeks after the launch, which are the two numbers Q2 asks you to defend. Then post
your three letters.

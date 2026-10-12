# Does the redesigned scheme survive the three roles, and what would it save?

*Illustrative case: the company is real, the situation and the data are synthetic, built for this class.*

**The ticket, in short.** Uber, Hyderabad, the driver app. From Monday 31 August 2026 an enrolled
driver who stays online through a whole peak window (two windows a day, three hours each) is
guaranteed Rs 300 per peak online hour, and Uber tops up the gap between the driver's trip earnings
and that floor. Over the six weeks after the launch the top-up came to Rs 1.9 crore. Peak online
hours rose 24 percent, completed peak trips rose 3 percent, trips per peak online hour fell from 1.90
to 1.58, and the median rider wait at peak went from 4.8 to 4.6 minutes. The city head asks, by
Friday, whether the scheme works, what it should pay for, and whether anyone is gaming it.

**Who needs the answer.** The city head, who decides on Friday, and the three people in the room
who each lose something under a change: the driver-operations lead (wants drivers online), the
marketing lead (sold the floor on every hoarding) and the finance partner (owns the top-up budget).
A redesign that cannot answer them is dropped, and the city keeps paying for hours.

**The questions on the way.** How much of the top-up went to weeks of declining? What can the
redesign honestly say it saves? Where should the acceptance floor sit? What happens to the north
star when drivers choose when to log in?

This is round 3 of the war game. Your group writes the redesign on the definition template
(`exercises/guided/C2_W04_D01_definition_STUDENT.md`), then answers these four items before the
roles attack. Items marked **Design** ask for the best-fit approach, a sizing, the fact that would
switch it, or the second route that would confirm a number.

```
Post exactly this shape: xxxx
```

---

## What does the redesign pay for?

The redesign keeps the Rs 300 floor and changes what earns it: a driver-week earns its top-up only
if the driver accepted at least the city's floor share of the offers shown, with an accepted trip the
driver then cancels counted as declined. Under the old rule a driver below the floor earned nothing
extra from the next trip, since the top-up shrank by whatever the trip paid, so declining cost
nothing; under the new rule declining costs the week's top-up. The city judges the scheme by its
north star, completed peak trips per enrolled driver online at peak, per week, read beside three
guardrails: for riders, the share of offers accepted and the median rider wait at peak; for the
budget, the top-up per completed trip.

Three facts from the case data:

| Fact | Value |
|---|---|
| Share of the Rs 1.9 crore top-up paid to driver-weeks that accepted fewer than half the offers they were shown | 61 percent |
| The highest share of offers accepted in any week by a driver in the idle tail (the 180 drivers under one trip an hour after the launch) | 0.46 |
| The lowest share of offers accepted in any week by any other driver online that week | 0.78 |

An **offer** is one rider request shown to one driver; a request one driver declines is offered to
the next driver.

---

## How much of the top-up went to weeks of declining?

Finance teams price every gamed number in rupees, because a cost is what moves a budget owner to
change a rule.

### Q1. How much of the Rs 1.9 crore went to driver-weeks that accepted fewer than half the offers they were shown?

a) Rs 74,10,000

b) Rs 1,15,90,000

c) Rs 1,90,00,000

d) Rs 92,72,000

---

## What can the redesign honestly say it saves?

A saving quoted to a finance partner is checked against what people will do under the new rule,
and a number that assumes nobody changes is the first one a finance partner takes apart.

Assume, and say so on your sheet, that some idle drivers would start accepting enough to qualify
under a rule that pays for trips, so that between a fifth and a half of the idle tail's top-up would
still be paid.

### Q2. Design. What saving does your group write on its sheet?

a) Rs 1.159 crore, as every idle-tail week's top-up stops on day one

b) Rs 74.1 lakh, the top-up that every other driver-week received

c) Rs 1.9 crore, as the redesign replaces the whole six weeks' top-up

d) Rs 58 lakh to Rs 92.7 lakh, as a half to a fifth is still paid

---

## Where should the acceptance floor sit?

Every floor, threshold or cut-off a team sets decides who is paid and who is not, so the team says
which people the floor touches before it says the number.

### Q3. Design. The finance partner proposes a floor of 0.86, the city's share of offers accepted before the launch. What does that floor do?

a) It also stops the top-up for honest driver-weeks between 0.78 and 0.86

b) It pays every idle-tail week again, since the floor sits above 0.46

c) It changes nothing, since the city's share after the launch is 0.73

d) It touches no honest driver, since every other week accepted 0.78 or more

---

## What happens to the north star when drivers choose when to log in?

An interviewer at a marketplace asks this follow-up of every metric a candidate proposes, because the
people measured always control part of what is measured.

### Q4. A driver decides when the app is open, so the driver sets the start of every online hour. What does logging in more do to the redesign's north star?

a) It raises the north star, since each extra hour online adds to the count on top of it

b) It makes the north star impossible to compute, since no hour has a fixed start

c) Logging in alone cannot raise it: a completed trip needs a rider's request first

d) It drops the north star to zero, since drivers would stop logging in at all

---

## Where do you check the numbers?

Notebook 03, `notebooks/C2_W04_D01_03_definition_and_cost_STUDENT.ipynb`, prints the split of the
top-up and the saving under both ends of the assumption, in its first two code cells after the
setup. Run them, write your saving with its assumption on the group's sheet, and post your four
letters.

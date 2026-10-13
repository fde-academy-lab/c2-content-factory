# Which number should a plan chase, and which guardrail catches the harmful way of hitting it?

*The driving school is invented for chapter 2, with every number in it. Uber's case is illustrative: the company is real, the situation and the data are synthetic, built for this class.*

**The example, in short.** A driving school (invented) has four instructors who each teach 25
learners a year, 100 in all. Its hoarding prints the share of learners who passed the licence test
among those who took it. In 2025 all 100 took the test and 60 passed, 0.60; in 2026 the instructors
booked the test only for the learners they were surest of, 40 took it and 36 passed, 0.90, so
licences per learner who enrolled fell from 0.60 to 0.36. At Uber's Hyderabad scheme the city team is
choosing the one number its redesigned peak-hour guarantee pays for.

**Who needs the answer.** Every team that writes a growth plan. A north star read alone can sell a
year in which the people served got less, and a guardrail chosen without asking what it catches lets
the harm through.

**The questions on the way.** Which guardrail would have caught the school's 2026 move? Which number
should Uber's redesigned scheme chase? Which budget guardrail catches a top-up that runs away from
the trips it pays for?

Q1 is called aloud at the end of chapter 2, with the trainer; Q2 and Q3 are sat in the practice lab.
Every item has one right answer. Items marked **Design** ask for the best-fit approach, the fact that
would switch it, or the second route that would confirm a number.

```
Post exactly this shape: xxx
```

---

## Which guardrail would have caught the school's 2026 move?

A guardrail is a number watched beside the number being chased, so that hitting it does no hidden
harm. It earns its place by the harmful move it catches.

### Q1. The owner will print next year's pass rate on the hoarding again. Which guardrail beside it would have caught the 2026 move?

a) Learners enrolled, since a larger intake shows families trust the school

b) The pass rate split by instructor, since it shows who teaches best

c) The share of enrolled learners who took the licence test that year

d) The city's pass rate across every school, since it sets the bar

---

## Which number should Uber's redesigned scheme chase?

A north star is the one number that best captures the value the people served get. At Uber's
Hyderabad scheme the people served are riders who ask for a trip at peak.

### Q2. Design. Which number should be the north star of the redesigned peak-hour scheme?

a) Peak online hours per enrolled driver, counted each week

b) Offers accepted over offers shown at peak, counted each week

c) Top-up paid per enrolled driver online at peak, each week

d) Completed peak trips per enrolled driver online that week

---

## Which budget guardrail catches a top-up that runs away from the trips?

The finance partner holds the top-up budget, which reached Rs 1.9 crore in the six weeks after the
launch, and wants one guardrail on the scheme's cost.

### Q3. Design. Which guardrail catches a top-up that runs away from the trips it pays for?

a) Top-up per completed peak trip, read week by week

b) Total top-up paid in the month, read against the month's budget

c) Top-up per peak online hour, since the floor is paid by the hour

d) Top-up per enrolled driver, since enrolment sets who can claim it

---

## Where do you check your calls?

Notebook 02, `notebooks/C2_W04_D01_02_north_star_guardrails_STUDENT.ipynb`, prints the school's
three shares for both years and flags the seesaw with `seesaw(rate, guardrail)`. Notebook 09,
`notebooks/C2_W04_D01_09_north_star_guardrails_cost_STUDENT.ipynb`, prints Uber's north star and its
three guardrails before and after the launch. Then post your three letters.

# The guesstimate: clarify, map, calculate, validate: how do you size and check a number nobody has measured?

This set practises chapter 6, the guesstimate: clarify, map, calculate, validate, on the campus canteen
from the chapter and two checks whose failure is easy to miss. The canteen, its till, the phone pack and the
payments network are invented. Item 1 doubles as the chapter's closing check; the rest are the
evening's practice, or the lab's opening twenty minutes.

**Who needs the answer.** The canteen head (invented), who must order milk for a weekday before any till
report exists, and any interviewer who asks for a number aloud.

The canteen's guesses (invented):

| Factor | Central | Low | High |
|---|---|---|---|
| Students on campus | 3,000 | 2,700 | 3,300 |
| Share who buy tea on a weekday | 0.45 | 0.25 | 0.65 |
| Cups each buyer drinks | 2 | 1.5 | 2.5 |

**The questions on the way.**

- What does clarifying pin down?
- Which chain multiplies out in the right unit?
- Which guess sets the range?
- Which number checks the estimate?
- Which test does a hidden mistake fail?

Post one line, six letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

## What does clarifying pin down?

This comes up in every guesstimate interview: the first minute settles the unit, the period and what
counts, before any number is said.

### Q1. Which question clarifies the canteen's estimate before any number is written?

*Level L1 · the chapter's closing check.*

a) "How many students on campus like tea?"
b) "One canteen, one weekday, cups of tea sold: is that the number?"
c) "What profit does the canteen make on a cup?"
d) "Which supplier delivers the canteen's milk each morning, and at what price?"

---

## Which chain multiplies out in the right unit?

This comes up at work whenever an estimate is built from factors: the units multiply too, and the
chain must end in the unit that was clarified.

### Q2. Which chain multiplies out to cups of tea on a weekday?

*Level L2.*

a) Students on campus x the share who buy tea x cups each buyer drinks
b) Students on campus x cups each buyer drinks / the share who buy tea
c) Students on campus, plus the share who buy tea, plus cups each buyer drinks
d) The share who buy tea x cups each buyer drinks

---

## Which guess sets the range?

This comes up at work when the estimate goes to someone who will spend money on it: they need to know
which guess to replace with a count first.

### Q3. Moving one guess at a time from its low end to its high end, the others held, which guess sets the range?

*Level L3 · tagged [S] in this programme's calibration: a staple of analyst and consulting screens.*

a) Students on campus, since it is the biggest number
b) Cups each buyer drinks, since nobody drinks exactly two cups a day
c) The share who buy: alone it moves 1,500 to 3,900 cups
d) All three equally, since each is multiplied in once

---

## Which number checks the estimate?

This comes up at work the moment an estimate meets a published or counted number: it is a check only
in the same unit, period and definition.

### Q4. Design. Which known number checks the canteen's weekday estimate?

*Level L3, a design call · tagged [S].*

a) The till's cups of tea on an average weekday
b) The month's total takings in rupees, across tea, coffee and snacks
c) The campus head count of 3,000 students
d) The coffee count for the same weekday

---

## Which test does a hidden mistake fail?

This comes up at work when a careful calculation compares two numbers that were never counted the same
way.

### Q5. Design. A classmate says a 28-day phone pack of 1.5 GB a day gives less data a day than a 30-day month at the same rate, since 42 GB is below 45 GB (invented). What is wrong?

*Level L4, a design call · tagged [F]: frequent in global capability centre (GCC) and product-company screens.*

a) Nothing: 42 GB is below 45 GB, so the pack gives less
b) The unit: GB should have been turned into MB before comparing
c) The period: the two run different days, so compare per day, 1.5 GB in both
d) The definition: the pack may count only daytime data, and nobody has checked what the month counts

### Q6. A payments network reports 31 billion transactions in a 31-day month, and a pair estimated 1 billion a day (invented numbers). Which comparison is honest?

*Level L5 · tagged [F].*

a) 31 billion set against the pair's 1 billion, as both are printed
b) 31 billion divided by 30 days, which is about 1.03 billion a day
c) The month's value in rupees set against the pair's count of payments
d) 31 billion divided by the month's 31 days, which is 1 billion a day

---

**What does the chapter add?** Clarify the unit, the period and what counts; map a chain that
multiplies out in that unit; calculate each factor aloud with its range and name the one that sets
the range; validate against a number counted the same way. Chapter 8 sizes Uber's drivers at the
evening peak with the same four steps.

**In the interview.** [S] A guesstimate: how many customers could a new store sign up to a loyalty tier
in its first year?

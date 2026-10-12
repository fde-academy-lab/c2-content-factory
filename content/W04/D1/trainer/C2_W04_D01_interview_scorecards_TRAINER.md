# How do you score Monday's interview answers, criterion by criterion?

**TRAINER ONLY.** The transcripts are in `extras/C2_W04_D01_transcript_STUDENT.md`. Pairs score the
weak and the hire-grade answer in the afternoon's interview room (S45), and the [D] pair in section 9
of the metric clinic if the tentative faculty block does not run. The seven criteria are the spine's,
built on what interviewers score per Aced's guide: structure, assumptions and scope before the method
(case file T2, https://www.aced.io/blog/top-data-analyst-interview-questions, checked 12 October 2026).

**Who needs the answer.** The trainer, who reads the scores back to the room, and any learner who
asks why an answer that sounded confident scored low.

**The questions on the way.** What does each criterion reward, at 0, 1 and 2? How do the [S] answers
score? How does the AI-company variant score? How do the [D] answers score? What do you say when a
pair's scores disagree with yours?

---

## What does each criterion reward, at 0, 1 and 2?

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Clarified scope | Starts on metrics at once | Asks one question, or asks without using the answer | Asks what the feature is for, who it serves and what counts as harm, then builds on the answers |
| Named the denominator and window | A number with no "per" and no period | One of the two | Both, said aloud: per enrolled driver online at peak, per calendar week |
| Saw the paradox | Calls the rise a success | Notices something is off without the number | Names it with numbers: hours up 24 percent while trips per online hour fell from 1.90 to 1.58 and the wait barely moved |
| Sized it with a unit | No size | A size with no unit or no base | A size with its unit and base: Rs 1.9 crore for 6,700 extra peak trips, about Rs 2,836 each, in six weeks |
| Said what would change their mind | Nothing | A vague "more data" | A testable condition: if outer-zone waits went back up to 6.6 minutes without the hourly floor |
| Tied it to a decision and its cost | No decision | A decision with no cost, or a cost with no decision | Hold the extension, one written payout rule, a test by zone, with the cost of the old rule named |
| Gave the structure before the number | Numbers first, structure never | Structure after the numbers | Goal, north star with its lines, guardrails, leading input and test, all before any number |

---

## How do the [S] answers score?

"How would you measure the success of a new feature?", asked of the earnings guarantee.

| Criterion | Weak answer | Why | Hire-grade answer | Why |
|---|---|---|---|---|
| Clarified scope | 0 | Starts on metrics | 2 | Asks the goal, who is in it, what counts as harm, which decision rides on it and against what, then restates the goal as faster pickups |
| Named the denominator and window | 0 | "Hours are up 24 percent" | 2 | Trips completed in the peak windows, per enrolled driver online at peak, per calendar week, with the count printed |
| Saw the paradox | 0 | Calls it a success | 2 | 1.90 to 1.58 trips per online hour, the wait 4.8 to 4.6 minutes and the north star 35.76 to 35.89, against hours up 24 percent |
| Sized it with a unit | 0 | None | 2 | Rs 2,836 per extra trip, 17 fares; about Rs 1.16 crore to declining weeks; about Rs 46,000 per extra outer-zone trip |
| Said what would change their mind | 0 | Nothing | 2 | A testable condition: outer-zone waits back up to 6.6 minutes without the hourly floor |
| Tied it to a decision and its cost | 1 | "Roll it out to more cities" is a decision with no cost | 2 | Hold the extension, one payout rule, a test by zone, the old rule's cost named |
| Gave the structure before the number | 0 | Lists hours, satisfaction and a survey | 2 | Goal, north star with its lines, three guardrails, input and test with its unit, then asks for the numbers |
| **Total, of 14** | **1** | | **14** | |

The three follow-ups and the five harder ones each score 0 to 2 on one question, "did the answer use
a line of the definition or a number from the data?": a 2 names the line or the number.

---

## How does the AI-company variant score?

| Criterion | Hire-grade answer | Why |
|---|---|---|
| Clarified scope | 2 | Asks who it is for, what counts as harm and which decision rides on it, then restates the goal |
| Named the denominator and window | 2 | Kept text per developer with a seat, per week, with the share of seats used printed beside it |
| Saw the paradox | 2 | Acceptance can rise from 30 to 40 percent while merged code stays flat, invented numbers labelled as such |
| Sized it with a unit | 1 | The variant names no company figure by design, so there is no cost or size in rupees or hours |
| Said what would change their mind | 2 | Time to merge not falling while kept text rises |
| Tied it to a decision and its cost | 1 | The renewal decision is named; its cost is not |
| Gave the structure before the number | 2 | Goal, proxy, outcome, what is read beside it, guardrails, input, test, in that order |
| **Total, of 14** | **12** | |

The variant scores lower on sizing and cost on purpose: it has no data, so the room sees which
criteria need numbers.

---

## How do the [D] answers score?

"Three departments each want their own target; how do you get to one, and what do you say to the
teams who lose?"

| Criterion | Weak answer | Why | Hire-grade answer | Why |
|---|---|---|---|---|
| Clarified scope | 1 | "Which team is right?" asks, and asks the wrong thing | 2 | Asks what the scheme is for, which decision the number drives and what each team needs to see |
| Named the denominator and window | 0 | No metric is defined | 2 | The north star per enrolled driver online at peak, per calendar week, the enrolled count printed |
| Saw the paradox | 0 | None | 2 | Hours rose 24 percent while trips per online hour fell from 1.90 to 1.58, so hours cannot be the target |
| Sized it with a unit | 0 | None | 2 | Rs 2,836 per extra trip under the old rule; Rs 82.3 of top-up per trip, half the average fare |
| Said what would change their mind | 0 | "We will revisit" | 2 | Said to the room: revisit the acceptance floor if the wait by zone rises, starting in the outer zones |
| Tied it to a decision and its cost | 0 | Gives each team its own target | 2 | One north star; each team's number gets a named job; finance gets a total cap and the cost per extra trip |
| Gave the structure before the number | 0 | None | 2 | The goal, then "none of your three is the target", then where each number lives |
| **Total, of 14** | **1** | | **14** | |

---

## What do you say when a pair's scores disagree with yours?

Ask the pair to read the line of the transcript that earned the score. A score stands when a line of
the transcript shows it; "it sounded confident" is not a line. Most disagreements are on "sized it
with a unit": a number with no base, such as "Rs 1.16 crore", scores 1 until it says of what and over
how long.

# Day sheet: Week 1 Day 4, Thursday

**TRAINER ONLY.**

---

## The two-minute orientation

| | |
|---|---|
| **Start from** | The cleaned dataset. Concept first: no test catalogue, no formulas, no tables. |
| **Go as far as** | Everyone states a p-value correctly, names the campaign confounder, and ships the one-page note with all three answers. |
| **Stop before** | The t-test family, confidence-interval construction, power, chart libraries. Name each as later. |
| **Comes later** | Week 2 joins the campaigns table properly in SQL and pandas. Week 4 designs the metric the plan chases. |
| **Cut first** | The confidence-interval line, then the mix arithmetic. **Never cut the hand shuffle, the confounder or the note.** |

---

## The running order

| Block | Duration | What happens |
|---|---|---|
| 1 | 10 min | Meera's three questions, sorted into real-or-noise, trust-the-number, cause-or-coincidence |
| 2 | 55 min | Shuffle by hand with ten cards, then the permutation loop in code. The p-value as a share. |
| 3 | 20 min | Statistically real against worth acting on. A confidence interval named and parked. |
| 4 | 25 min | Sample size: Student's 40 percent on twelve against Retail-Plus on sixty-six. The rule of thumb. |
| 5 | 45 min | Correlation against causation on the monsoon sale. Who took it, what a fair comparison needs, the aggregate that flips. |
| 6 | 55 min | The note: guided on Retail-Plus, unguided on Student and the discount |
| 7 | 20 min | Kahoot, close, Saturday preview |

---

## What is planted, and what the room should find

**This section never reaches a learner.**

| Planted | What the room should do | If nobody finds it |
|---|---|---|
| Retail-Plus real but modest: a 32.3 point gap that no shuffle reaches | Run the shuffle and get 0 of 5,000, then write the bound rather than zero | The number comes out whatever they do. The teaching is in how they write it. |
| Student holding exactly 12 orders, 5 then 7 | Notice the base before the percentage, and get p around 0.38 | Ask "how many orders is that 40 percent of?" and wait. |
| The campaign lifting the blend 6 percent while both segments fall 3 | Compute blended first, then split, and meet the reversal | This is block 5 and it is walked. Reveal the three rows one at a time. |

**The exposure table's mix is the whole mechanism:** 50 percent Retail-Plus among the exposed against
40 percent among the control, and Retail-Plus spends 2.5 times more. Do not say that until after the
room has seen the three rows and been surprised.

---

## The deliberate failure, with its exact text

**Block 2, and it is a sentence rather than a stack trace.** Ask somebody to read the result aloud
after the shuffle. Somebody will say, or accept:

> "p = 0.03 means there is a 3 percent chance we are wrong."

Write it on the board **exactly as said**, then write the correct version underneath, then cross the
first one out and leave both up for the rest of the day. Rooms that only hear the correct version
revert under pressure; rooms that watch the wrong one get crossed out do not.

The second failure to stage, if the room is quick: let somebody write `p = 0` after the 0-of-5,000
result. The repair is one sentence about resolution, and it is a sentence they will use in an
interview.

---

## The numbers, so you are never caught out

| Test | Result |
|---|---|
| Retail-Plus against Retail-Core | gap 32.3 points, 0 of 5,000 shuffles, `p < 0.0002` |
| Student, 12 orders, 5 then 7 | a 40 percent rise, 1,914 of 5,000, `p = 0.383` |
| Retail-Plus fall, clean data | 35.0 percent |
| Retail-Core fall, clean data | 2.7 percent |

| Campaign | Exposed | Not exposed | Change |
|---|---|---|---|
| Retail-Plus | Rs 4,850 (30) | Rs 5,000 (40) | down 3.0 percent |
| Retail-Core | Rs 1,940 (30) | Rs 2,000 (60) | down 3.0 percent |
| Everyone | Rs 3,395 (60) | Rs 3,200 (100) | up 6.1 percent |

For the take-home: on clean data web is up 3.4 percent and app is flat, a gap of 3.4 points with
`p = 0.75`. **Tuesday's web finding does not survive the reconciliation**, and that is the take-home's
whole point. Do not mention it in class.

---

## Per-block facilitation

**Block 1.** Sort the three questions on the board before touching anything. If the room cannot tell
them apart now, block 5 will collapse into block 2.

**Block 2.** The cards come first and they are not a warm-up. Do all five steps physically. The
count out of ten written on the board **is** the p-value, and saying that sentence while pointing at
a number somebody just produced is the moment the concept lands.

**Block 3.** Twenty minutes, and the temptation is to spend forty. Name the confidence interval,
say it is Week 4's, and move.

**Block 4.** Ask for the Student percentage first and let somebody be impressed. Then ask how many
orders. The pause is the lesson.

**Block 5.** Reveal the three rows one at a time, blended first. Let the room sit with the
contradiction for a full thirty seconds before anybody explains it. The explanation is worth much
less if it arrives before the confusion.

**Block 6.** Guided on Retail-Plus so they see the shape, then unguided. Ask two learners to read
their Student answer aloud, because that is where "not yet" gets written as "no" and the difference
matters.

---

## Checkpoint questions

1. After block 2: say what the p-value is, in one sentence, without the word probability.
2. After block 4: Student is up 40 percent. What is your one question?
3. After block 5: both segments fell and the blend rose. Who made the error?
4. After block 6: which of Meera's three questions is a yes?

---

## What the room leaves with

A correct p-value sentence, the sample-size instinct, the confounder named, and a one-page note
holding three answers of three different shapes. The last one is the week's deliverable and the
thing Saturday examines.

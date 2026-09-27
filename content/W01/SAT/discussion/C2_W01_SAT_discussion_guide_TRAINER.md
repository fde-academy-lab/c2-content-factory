# Week 1 Saturday: the discussion guide

**TRAINER ONLY.** Led by the Academic TA, after the paper and the break. The paper and its key are
in `paper/` and `answer-key/`; the key file carries every item's key, tag, level, day and interview
anchor.

The discussion is worth more than the marking. Every answer is treated as an interview answer, and
the format is deliberately uncomfortable: papers are swapped, and call-outs are random.

---

## The shape of the four hours

| Block | Duration | What happens |
|---|---|---|
| The paper | 110 min | Pen and paper, AI-free, no notes: 52 objective items. |
| Break | 20 min | Papers stay face down on the desks. |
| Marking | 15 min | Papers swapped and marked against the key, read out by you. |
| Most-missed first | 25 min | The items the room lost most, each one repaired aloud. |
| The interview anchors | 45 min | Ten questions asked aloud as interview questions, with random call-outs. |
| Doubts and the bridge | 25 min | Open doubts, then Monday: the same numbers from the warehouse. |

---

## Marking, 15 minutes

1. Papers swap along the row, so nobody marks their own and nobody marks their neighbour's twice in
   a month.
2. Read the key out section by section from the key file, at a pace a marker can tick to: the
   letters in runs of five, the words and numbers one at a time.
3. The marker writes a tick or a cross beside every item, then the count of ticks as Items right on
   the front page, and hands the paper back.
4. The key file's marking rule decides the edge cases: every correct letter and no other on a
   more-than-one item, the number on an applied maths item, the whole sequence on an ordering item.
   There is no partial credit, because the programme has set no rule for it.

Say once, at the start, that the marker is deciding nothing. Reading somebody else's answer against
the key is the exercise, and it is harder than being marked.

## Most-missed first, 25 minutes

Before the anchors, find the items the room actually lost. Read out the candidate list below and
ask for hands on the paper each person marked: "a cross on item 9?" Write the counts on the board
and take the five highest, in order. A show of hands on the paper you marked is never a show of
hands on your own score, so nobody is exposed.

| Item | What it tests | The trap most papers fall into | The repair, said aloud |
|---|---|---|---|
| 9 and 35 | What a p-value is and is not | Reading p = 0.03 as a 3 percent chance of being wrong | The p-value is computed assuming chance alone; it measures how rare the gap would be in that world, and says nothing about whether the hypothesis is true or the gap is worth acting on. |
| 26 | Reading a shuffle | Calling a 5-point gap significant because it beats most of ten shuffles | Ten shuffles that already reach 6 points say chance makes gaps like this easily; the real gap is unsurprising. |
| 11 | Types from a CSV | Expecting `'4500' > 3000` to compare numbers | In Python 3 the comparison raises a `TypeError`, so the statement is false; the fix is converting at the read, once. |
| 16 and 43 | The mix effect | Treating a total that rose as proof that the parts rose | A total can rise while every segment falls, when the mix shifts toward the richer segment. |
| 21 | A fair comparison | Comparing a 13-week quarter with an 11-week one as they stand | Compare revenue per week, or cut both quarters to the same weeks. |
| 29 | Levers on the tree | Picking the branch that sounds cheapest | Held equal, a 10 percent lift in any branch adds the same revenue; the choice turns on what each costs to move. |
| 41 and 42 | Reconciliation | Logging only the three rejects and forgetting the fourteen duplicates | Every removed row is logged, so the rejects log holds 17, and removing Q1's duplicates shrinks the Q1 to Q2 drop. |
| 46 | Discount arithmetic | Adding the percentages: 10 minus 15 | Multiply the factors: 1.10 times 0.85 is 0.935, so revenue falls 6.5 percent. |

If an item outside this list carries more crosses, it wins its place. The list is a prediction, and
the hands are the evidence.

## The interview anchors, 45 minutes

Ask each anchor aloud as an interviewer would: name the person, then the question, then wait. Give
sixty seconds. After the answer, ask the room what one sentence would make it stronger, and read
the answer below only if nobody gets there. The items listed after each anchor are the ones on the
paper that descend from it.

### 1. [S] Kalpa wants 15 percent growth; draw the revenue tree and name the branch you would investigate first.

*Items 1, 2, 18, 29, 30, 46 and 50.*

A strong answer draws the tree first: revenue is customers, times orders per customer, times items
per order, times price per item, less discounts. It then says that a 10 percent lift in any branch
adds the same revenue, so the first branch to investigate is the one the data says has moved, and
in Kalpa's two quarters the customer count held while orders per customer fell, so frequency is
where the growth leaks. It closes on what would change that choice: the cost of moving each branch.

Listen for a learner who names a branch before drawing the tree. That is the answer interviewers
mark down.

### 2. [S] Sales fell from Q1 to Q2; walk the investigation ladder.

*Items 17, 20, 31, 36 to 39, 48 and 51.*

Five rungs, in this order: confirm the drop is real; compare like with like, which means the same
weeks and the same definitions; decompose along the revenue tree; isolate the branch and the
segment; then hypothesise and name the evidence that would settle it. Kalpa's own case lands on the
fourth rung: customers flat, orders per customer down 10 percent, revenue per order unchanged.

The follow-up worth asking: "which rung did you skip on the paper?" Most people skip the second.

### 3. [S] Mean or median for order value, and why?

*Items 10, 19 and 47.*

Order values are skewed by a few very large orders, so the median describes the typical order and
the mean does not: five orders of 800, 1,200, 1,400, 2,000 and 480,000 rupees have a median of
Rs 1,400 and a mean of Rs 97,080. The mean still matters, because mean times the number of orders is
revenue. The answer is to report both when they diverge and to say why they diverge.

### 4. [S] Finance and the dashboard disagree by Rs 20 lakh; what do you do first?

*Items 5, 25, 28, 40 to 42 and 52.*

Profile the export before arguing about the number: duplicates, the date window, and what each side
counts. Then reconcile counts first and revenue second, line by line, against Finance's books,
which are the reference for money. Ask the second question the first time round, and wait for it:
**what would you refuse to do?** Adjusting your own figure until it agrees. Reconciling and
fabricating differ only in whether the steps are written down.

### 5. [S] What does p = 0.03 mean, and not mean?

*Items 6, 9, 12, 26, 35 and 49.*

If chance alone were at work, a gap at least this large would turn up in about 3 percent of
shuffles, so the gap would be rare under chance. It does not mean a 3 percent chance the finding is
wrong, it does not mean a 97 percent chance it is real, and it says nothing about whether the gap is
large enough to act on.

Take three definitions in a row without comment and write all three on the board. Then ask which
one survives somebody saying "so there is a three percent chance we are wrong".

### 6. [F] Input 200, clean 183, rejected 14: does it reconcile, and what is the missing number?

*Items 5, 40, 41 and 52.*

It does not reconcile: 183 plus 14 is 197, so 3 rows are unaccounted for. Nothing is reported
until those 3 are found, and the usual culprits are rows removed by a step that does not write to
the rejects log, such as a de-duplication, or a line truncated at the read.

### 7. [F] 42 percent on 12 orders against 31 percent on 400; which do you trust?

*Items 14 and 27.*

The 31 percent. On 12 orders a single order moves the rate by more than 8 points, so 42 percent is
five orders out of twelve, and a shuffle would show chance producing gaps like it often. On 400
orders one order moves the rate by a quarter of a point. The 12-order figure is a question to
collect more data on, never a finding, and the Student segment on Thursday was exactly this case.

### 8. [F] Revenue rose after the discount; three reasons that is not proof it worked.

*Items 8, 15, 16, 34 and 43 to 45.*

First, who received it: the discounted customers were already the frequent buyers, so buying
frequency drives both getting the discount and spending, which makes it a confounder. Second, the
mix: half the exposed group was Retail-Plus against forty percent of the control, and within both
segments exposed customers spent less, so the six percent is a mix effect. Third, nothing was held
out: no randomised control, so seasonality and the monsoon itself are not ruled out. The honest
recommendation is to randomise the next campaign inside a segment.

### 9. [D] Your cleaning run reported zero rejects on a file you know is dirty; what do you check?

*Items 4, 11, 13, 23, 24, 32 and 33.*

Treat the zero as a bug in the checker until it is proven otherwise. Check that every field was
converted from text before the rules ran, because a check on a string can pass quietly; check that
input equals clean plus rejected; check that the rejects log is actually being written; and then
plant one row you know is bad and rerun. If the planted row does not land in the log, the run was
never checking anything.

### 10. [D] Write the four-part note for the Retail-Plus finding in four sentences, then defend the caveat.

*Items 7 and 45.*

Claim: Retail-Plus orders per member fell about a third, against 2.7 percent for Retail-Core.
Evidence: chance alone produced a gap this large in none of 5,000 shuffles. Caveat: these are 22
paid-tier members over two quarters, and nothing here says why they bought less. Action: act on it,
and ask the head of Retail-Plus which members to call first.

Then defend the caveat against the room. Listen for a caveat that is a condition rather than a
hedge: "this may not be accurate" is a hedge, while "nothing here measures why they bought less"
names what would change the claim.

---

## Running random call-outs without losing the room

| Do | Do not |
|---|---|
| Name the person, then the question, then wait | Ask the question to the room and take the first hand |
| Give sixty seconds, and let the silence run | Rescue somebody at fifteen seconds |
| Take a wrong answer, write it on the board, and ask the room to repair it | Correct it yourself |
| Come back to the same person later with an easier one | Leave somebody who struggled sitting with it |

The last row matters more than the rest. A learner who is called, struggles and is never called
again learns that being called is a punishment.

---

## Doubts and the bridge into Week 2, 25 minutes

Take open doubts first, for about twenty minutes, then close on this:

> "Anand has his reconciliation. On Monday he asks for the same numbers **every** Monday, computed
> from the warehouse itself, with nothing a person can mistype. The tree does not change. The ladder
> does not change. The tool does."

Then one question to the room, and take three answers: **which parts of this week's work should
never be done in a notebook again, and why?** The answers worth hearing are anything Finance depends
on, anything that has to run unattended, and anything an auditor will read. That is Monday's first
slide.

---

## After the session

Collect the marked papers. Using the key file's items-by-tag list, count the crosses per tag for
each learner and enter that row in the ground team's tracker: one row per learner per week, the
count of items right and the misses by tag. The misses by day point at the day each gap came from,
which is where Monday's remediation starts.

Two things are worth noting beside the tally. Which items more than a third of the room lost: those
come back at one level up in Week 2's return questions. And who answered well when called cold,
which is the mock-interview signal Week 1 produces. The paper is ungraded, never a ranking, and
never read out by name.

# Week 1 Saturday: the discussion guide

**TRAINER ONLY.** The Academic TA leads the Saturday from the break onwards. The paper and its key
are in `paper/` and `answer-key/`, and the Word files there are what the room sits and what you read
from. The key file carries every item's key, tag, level, day and interview anchor, and a paragraph
per item on why the key holds, why each wrong option fails and the interview answer in one breath.

The discussion is worth more than the marking. Every answer is treated as an interview answer, and
the format is deliberately uncomfortable: papers are swapped, call-outs are random, and the last
half hour puts every learner on the interviewer's side of the table.

---

## The shape of the 300 minutes

| Block | Duration | What happens |
|---|---|---|
| The paper | 120 min | Pen and paper, AI-free, no notes: 57 objective items, then the untimed stretch page for anyone who finishes early. |
| Break | 20 min | Papers stay face down on the desks. |
| Marking | 20 min | Papers swapped and marked against the key, read out by you. |
| The solution discussion | 90 min | The most-missed items first (35), then the ten anchors answered aloud as interview answers, with random call-outs (55). |
| The mock-interview round | 30 min | In pairs, each learner asks the other two anchors and one stretch follow-up, then they swap. |
| Doubts and the bridge | 20 min | Open doubts, then Monday: the same numbers from the warehouse. |

---

## Before the paper

Hand out the Word paper face down, one per desk, with a pen. Say three things and nothing else: the
paper is 120 minutes and ungraded, the answer sheet at the back is where every answer goes, and the
stretch page at the end is for anyone who finishes early and is not counted. Then start.

At 90 minutes into the paper, say once that thirty minutes remain. Collect nothing at the end:
papers stay on the desks through the break.

---

## Marking, 20 minutes

1. Papers swap along the row, so nobody checks their own and nobody checks the same neighbour twice in
   a month.
2. Read the key out section by section from the key file, at a pace a marker can tick to: the
   letters in runs of five, the words and numbers one at a time. Say the item number before every
   answer, since the scenario section now runs to Q50.
3. The marker writes a tick or a cross beside every item on the answer sheet, then the count of
   ticks as Items right, out of 57, and hands the paper back.
4. The key file's marking rule decides the edge cases: every correct letter and no other on a
   more-than-one item, the number on an applied maths item, the whole sequence on an ordering item.
   Accept the variants the key gives in brackets, such as 2 for 2.00 on Q46. There is no partial
   credit, because the programme has set no rule for it.
5. The stretch page is not marked. Anyone who wrote on it keeps it for the mock-interview round.

Say once, at the start, that the marker is deciding nothing. Reading somebody else's answer against
the key is the exercise, and it is harder than being marked.

---

## The solution discussion, 90 minutes

### Most-missed first, 35 minutes

Before the anchors, find the items the room actually lost. Read out the candidate list below and
ask for hands on the paper each person marked: "a cross on Q9?" Write the counts on the board and
take the six highest, in order, at about five minutes each. A show of hands on the paper you marked
is never a show of hands on your own score, so nobody is exposed.

| Item | What it tests | The trap most papers fall into | The repair, said aloud |
|---|---|---|---|
| Q9 and Q35 | What a p-value is and is not | Reading p = 0.03 as a 3 percent chance of being wrong | The p-value is computed assuming chance alone; it measures how rare the gap would be in that world, and says nothing about whether the hypothesis is true or the gap is worth acting on. |
| Q26 | Reading a shuffle | Calling a 5-point gap significant because it beats most of ten shuffles | Ten shuffles that already reach 6 points say chance makes gaps like this easily; the real gap is unsurprising. |
| Q11 | Types from a CSV | Expecting `'4500' > 3000` to compare numbers | In Python 3 the comparison raises a `TypeError`, so the statement is false; the fix is converting at the read, once. |
| Q16 and Q43 | The mix effect | Treating a total that rose as proof that the parts rose | A total can rise while every segment falls, when the mix shifts toward the richer segment. |
| Q21 | A fair comparison | Comparing a 13-week quarter with an 11-week one as they stand | Compare revenue per week, or cut both quarters to the same weeks. |
| Q29 | Levers on the tree | Picking the branch that sounds cheapest | Held equal, a 10 percent lift in any branch adds the same revenue; the choice turns on what each costs to move. |
| Q41 and Q42 | Reconciliation | Logging only the three rejects and forgetting the fourteen duplicates | Every removed row is logged, so the rejects log holds 17, and removing Q1's duplicates shrinks the Q1 to Q2 drop. |
| Q46 | Rows counted as customers | Dividing 500 rows by 500 and reading 1.00 as "nobody comes back" | A row is an order. Orders per customer divides by distinct customers: 500 over 250 is 2.00. |
| Q47 | An average of averages | Averaging Rs 2,000 and Rs 12,000 to get the slide's Rs 7,000 | Divide total revenue by total orders, Rs 20.0 lakh over 500, which is Rs 4,000; the 400 Retail orders outweigh the 100 Business ones. |
| Q49 | A whole-record dedupe | Trusting the zero because no two rows match in every field | A re-sent order carries a new timestamp, so whole rows differ; the identity rule, one order_id per order, finds the 40. |
| Q50 | Counts that reconcile while rupees do not | Calling the run clean because 1,160 plus 40 is 1,200 | Rs 88.0 lakh plus Rs 5.0 lakh is Rs 93.0 lakh against Rs 96.0 lakh in, so Rs 3.0 lakh is unaccounted for; nothing goes to Finance until it is found. |
| Q51 | Discount arithmetic | Adding the percentages: 10 minus 15 | Multiply the factors: 1.10 times 0.85 is 0.935, so revenue falls 6.5 percent. |

If an item outside this list carries more crosses, it wins its place. The list is a prediction, and
the hands are the evidence.

On every item, take the wrong answer first. Ask who wrote it, or who nearly did, and have them say
why it looked right; the key file's line for that option names the misconception, and the room
repairs it before you read the key's reason.

### The interview anchors, 55 minutes

Ask each anchor aloud as an interviewer would: name the person, then the question, then wait. Give
sixty seconds. After the answer, ask the room what one sentence would make it stronger, and read
the answer below only if nobody gets there. The items listed after each anchor are the ones on the
paper that descend from it, so a learner who lost those items is a good person to call. Ten anchors
in 55 minutes is about five minutes each, and the last two take the extra.

#### 1. [S] Kalpa wants 15 percent growth; draw the revenue tree and name the branch you would investigate first.

*Q1, Q2, Q18, Q29, Q30, Q46, Q51 and Q55.*

A strong answer draws the tree first: revenue is customers, times orders per customer, times items
per order, times price per item, less discounts. It then says that a 10 percent lift in any branch
adds the same revenue, so the first branch to investigate is the one the data says has moved, and
in Kalpa's two quarters the customer count held while orders per customer fell, so frequency is
where the growth leaks. It closes on what would change that choice: the cost of moving each branch.

Listen for a learner who names a branch before drawing the tree, or who reads orders per customer
off a count of rows. Those are the answers interviewers mark down.

#### 2. [S] Sales fell from Q1 to Q2; walk the investigation ladder.

*Q17, Q20, Q31, Q36 to Q39, Q47, Q53 and Q56.*

Five rungs, in this order: confirm the drop is real; compare like with like, which means the same
weeks and the same definitions; decompose along the revenue tree; isolate the branch and the
segment; then hypothesise and name the evidence that would settle it. Kalpa's own case on Tuesday
lands on the fourth rung. On closed quarters booked revenue fell 11.0 percent, from Rs 2.10 crore to
Rs 1.87 crore; the same 69 customers bought in both, orders per customer fell from 1.65 to 1.25, down
24.6 percent, and revenue per order rose 18.0 percent, mostly from the mix. The segment is
Retail-Plus, whose orders per member fell from 2.32 to 1.18 on the file as exported.

The follow-up worth asking: "which rung did you skip on the paper?" Most people skip the second, and
Q47 is the second rung too: an average of segment averages compares a 100-order segment as if it
were as big as a 400-order one.

#### 3. [S] Mean or median for order value, and why?

*Q10, Q19 and Q52.*

Order values are skewed by a few very large orders, so the median describes the typical order and
the mean does not: five orders of 800, 1,200, 1,400, 2,000 and 480,000 rupees have a median of
Rs 1,400 and a mean of Rs 97,080. The mean still matters, because mean times the number of orders is
revenue. The answer is to report both when they diverge and to say why they diverge.

#### 4. [S] Finance and the dashboard disagree by Rs 20 lakh; what do you do first?

*Q5, Q25, Q28, Q40 to Q42, Q50 and Q57.*

Profile the export before arguing about the number: duplicates, the date window, and what each side
counts. Then reconcile counts first and rupees second, line by line, against Finance's books, which
are the reference for money. Q50 is why the second step exists: rows can close while Rs 3.0 lakh
does not. Ask the second question the first time round, and wait for it: **what would you refuse
to do?** Adjusting your own figure until it agrees. Reconciling and fabricating differ only in
whether the steps are written down.

#### 5. [S] What does p = 0.03 mean, and not mean?

*Q6, Q9, Q12, Q26, Q35 and Q54.*

If chance alone were at work, a gap at least this large would turn up in about 3 percent of
shuffles, so the gap would be rare under chance. It does not mean a 3 percent chance the finding is
wrong, it does not mean a 97 percent chance it is real, and it says nothing about whether the gap is
large enough to act on.

Take three definitions in a row without comment and write all three on the board. Then ask which
one survives somebody saying "so there is a three percent chance we are wrong".

#### 6. [F] Input 200, clean 183, rejected 14: does it reconcile, and what is the missing number?

*Q5, Q40, Q41, Q50 and Q57.*

It does not reconcile: 183 plus 14 is 197, so 3 rows are unaccounted for. Nothing is reported
until those 3 are found, and the usual culprits are rows removed by a step that does not write to
the rejects log, such as a de-duplication, or a line truncated at the read. Then say the rupee half
aloud: even when the rows close, the rupees have to close too.

#### 7. [F] 42 percent on 12 orders against 31 percent on 400; which do you trust?

*Q14 and Q27.*

The 31 percent. On 12 orders a single order moves the rate by more than 8 points, so 42 percent is
five orders out of twelve, and a shuffle would show chance producing gaps like it often. On 400
orders one order moves the rate by a quarter of a point. The 12-order figure is a question to
collect more data on, never a finding, and the Student segment on Thursday was exactly this case.

#### 8. [F] Revenue rose after the discount; three reasons that is not proof it worked.

*Q8, Q15, Q16, Q34 and Q43 to Q45.*

First, who received it: the discounted customers were already the frequent buyers, so buying
frequency drives both getting the discount and spending, which makes it a confounder. Second, the
mix: half the exposed group was Retail-Plus against forty percent of the control, and within both
segments exposed customers spent less, so the six percent is a mix effect. Third, nothing was held
out: no randomised control, so seasonality and the monsoon itself are not ruled out. The honest
recommendation is to randomise the next campaign inside a segment.

#### 9. [D] Your cleaning run reported zero rejects on a file you know is dirty; what do you check?

*Q4, Q11, Q13, Q23, Q24, Q32, Q33 and Q49.*

Treat the zero as a bug in the checker until it is proven otherwise. Check that every field was
converted from text before the rules ran, because a check on a string can pass quietly; check that
the duplicate check is keyed on the identity rule and not on whole records, which is Q49; check
that input equals clean plus rejected; check that the rejects log is actually being written; and
then plant one row you know is bad and rerun. If the planted row does not land in the log, the run
was never checking anything.

#### 10. [D] Write the four-part note for the Retail-Plus finding in four sentences, then defend the caveat.

*Q7, Q45 and Q48.*

Claim: Retail-Plus really is spending less, and the fall is small against the company. Evidence:
its 22 members delivered Rs 1,110 less each in Q2 than in Q1, and chance made a fall that large in
135 of 5,000 shuffles, p = 0.027, while Retail-Core's Rs 110 gap came back in 1,724 of 5,000, p =
0.345, which is the usual wobble; the fall is Rs 24,420 a quarter, 0.19 percent of delivered
revenue. Caveat: the monsoon sale went mostly to Retail-Plus, who spend more anyway, and nothing here
measures why they spent less. Action: test a retention offer on half of Retail-Plus before anything
is rolled out.

Then defend the caveat against the room. Listen for a caveat that is a condition rather than a
hedge: "this may not be accurate" is a hedge, while "nothing here measures why they spent less"
names what would change the claim. Q48 is the same move in a harder room: Marketing pushing a slide,
and the answer that puts the denominator on the table before it argues.

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

## The mock-interview round, 30 minutes

Pairs, seated face to face. One learner is the interviewer and the other the candidate, then they
swap. The interviewer asks two anchors and one follow-up from the stretch page, listens without
helping, and gives one sentence of feedback at the end.

| Step | Duration | What happens |
|---|---|---|
| Set-up | 2 min | Pair the room and hand each pair its anchor pair from the table below. |
| First interview | 12 min | The first interviewer asks two anchors, about four minutes each, then the stretch follow-up. |
| Feedback | 2 min | One sentence that was strong, and one that would have lost the room. |
| Second interview | 12 min | Swap seats, and the new interviewer asks the other anchor pair and its follow-up. |
| Feedback | 2 min | The same two sentences, the other way round. |

Hand the pairs out by counting round the room, so every anchor is asked somewhere and no pair can
pick its favourites:

| Pair count | First interviewer asks | Follow-up | Second interviewer asks | Follow-up |
|---|---|---|---|---|
| 1, 6, 11 and on | Anchors 1 and 7 | Stretch 1 | Anchors 4 and 9 | Stretch 3 |
| 2, 7, 12 and on | Anchors 2 and 8 | Stretch 1 | Anchors 5 and 6 | Stretch 2 |
| 3, 8, 13 and on | Anchors 3 and 10 | Stretch 2 | Anchors 4 and 6 | Stretch 4 |
| 4, 9, 14 and on | Anchors 5 and 8 | Stretch 2 | Anchors 1 and 9 | Stretch 3 |
| 5, 10, 15 and on | Anchors 2 and 6 | Stretch 4 | Anchors 3 and 10 | Stretch 1 |

The follow-up goes after both anchors: the interviewer reads it from the stretch page as "one more
question", which is how a real screen escalates. The candidate answers aloud whether or not they
wrote on the stretch page during the paper.

Walk the room with the key file's stretch answers in hand. Do not correct inside an interview.
Note two or three answers worth replaying, ask their owners' permission, and take one of them to
the whole room at the start of doubts.

What the interviewer listens for, written on the board before the round starts:

1. The first sentence answers the question; the reasoning comes after it.
2. Every number carries its denominator and its window.
3. The candidate names what would change their answer.
4. The answer ends inside sixty seconds, or says why it needs more.

---

## Doubts and the bridge into Week 2, 20 minutes

Take one replayed answer from the mock round first, then open doubts, for about fifteen minutes in
all, then close on this:

> "Anand has his reconciliation. On Monday he asks for the same numbers **every** Monday, computed
> from the warehouse itself, with nothing a person can mistype. The tree does not change. The ladder
> does not change. The tool does."

Then one question to the room, and take three answers: **which parts of this week's work should
never be done in a notebook again, and why?** The answers worth hearing are anything Finance depends
on, anything that has to run unattended, and anything an auditor will read. That is Monday's first
slide.

---

## After the session

The paper carries no marks and ranks nobody. What is kept is the score by topic, so Monday's session
knows what to revisit. Collect the marked papers and, using the key file's items-by-tag list, count
the items each learner got right under each tag and enter that row in the ground team's tracker: one
row per learner per week, the misses by tag and by day. The misses by day point at the day each gap
came from, which is where Monday's remediation starts. The row is never totalled into a mark, never
compared across learners, and never read out by name.

Two things are worth noting beside the topic scores. Which items more than a third of the room lost:
those come back one level up in Week 2's return questions. And who answered well when called cold or
in the mock round, which is the mock-interview signal Week 1 produces.

# Week 1 Saturday: the discussion guide

**TRAINER ONLY.** The Academic TA leads the Saturday from the break onwards. The paper and its key
are in `paper/` and `answer-key/`, and the Word files there are what the room sits and what you read
from. The key file carries every item's key, tag, level, day and interview anchor, and a paragraph
per item on why the key holds, why each wrong option fails and the interview answer in one breath.

The discussion is worth more than the marking. Every answer is treated as an interview answer, and
the format is deliberately uncomfortable: papers are swapped, call-outs are random, and the last
half hour puts every learner on the interviewer's side of the table.

The paper runs in five parts. Parts 1 to 3 climb Kalpa's week: the revenue tree, the Q1
reconciliation, and Meera's three questions for Monday's growth review. Part 4 sets the week's traps
in public cases, each with its source named beside it, and the key's reasons carry what each source
reports; when the room asks about a case, answer from those reasons and add nothing beyond them.
Part 5 is a hypothetical support agent at a food-delivery company such as Swiggy, and every number
in it is illustrative; say so if a learner asks whether it happened.

---

## The shape of the 300 minutes

| Block | Duration | What happens |
|---|---|---|
| The paper | 120 min | Pen and paper, AI-free, no notes: step one's five ratings, then 36 timed items in five parts, then the untimed stretch page for anyone who finishes early. |
| Break | 20 min | Papers stay face down on the desks. |
| Marking | 20 min | Papers swapped and marked against the key, read out by you. |
| The solution discussion | 90 min | The most-missed items first (35), then the ten anchors answered aloud as interview answers, with random call-outs (50), then the room's ratings against its work (5). |
| The mock-interview round | 30 min | In pairs, each learner asks the other two anchors and one stretch follow-up, then they swap. |
| Doubts and the bridge | 20 min | Open doubts, then Monday: the same numbers from the warehouse. |

---

## Before the paper

Hand out the Word paper face down, one per desk, with a pen. Say four things and nothing else: the
paper is 120 minutes and ungraded; step one comes first, a rating from 1 to 4 for each of the five
parts in the box at the top of the answer sheet, given before any item is read; the answer sheet at
the back is where every answer goes; and the stretch page at the end is for anyone who finishes
early and is not counted. Then start.

At 90 minutes into the paper, say once that thirty minutes remain. Collect nothing at the end:
papers stay on the desks through the break.

---

## Marking, 20 minutes

1. Papers swap along the row, so nobody checks their own and nobody checks the same neighbour twice in
   a month.
2. Read the key out part by part from the key file, at a pace a marker can tick to: the letters
   in runs of five, the words and numbers one at a time. Say the item number before every answer,
   since the five parts number straight through to Q36. On the word-bank and match items, Q32 to
   Q36, read the letter and then its word or value, "Q32, d, WHERE", so a marker can check either.
3. The marker writes a tick or a cross beside every item on the answer sheet, then each part's
   ticks in the box beside that part's rating and their total as Items right, out of 36, and hands
   the paper back, so each learner reads their rating against their score part by part.
4. The key file's marking rule decides the edge cases: every correct letter and no other on a
   more-than-one item (Q12, Q17 and Q26), the letter on a word-bank or match item, the number on an
   applied maths item, and the whole sequence on an ordering item (Q8 and Q16). Q1 needs both the
   median and the mean. Q4 and Q15 need the direction as well as the size, so -6.5 and -35.0 match
   the key, and a bare 6.5 or 35.0 does not, since the key names a fall. Q11 and Q28 are true or
   false with the reason, answered with a letter; only Q10 takes T or F. There is no partial
   credit, because the programme has set no rule for it.
5. The Academic TA enters each paper's ticks by seat in
   `answer-key/C2_W01_SAT_item_analysis_TRAINER.xlsx`: 1 for a tick, 0 for a cross and a blank for
   an item left empty, and never a name. Its Discussion sheet gives the most-missed order the
   discussion takes, and any item the workbook flags goes to the tracker's owner with the room's
   rate, because the fault may sit in the item.
6. The same TA types the five step-one ratings from the top of each answer sheet into the workbook's
   Ratings sheet, by seat, 1 to 4 for each part. The sheet sets each part's mean rating beside the
   room's right rate in it, and counts the seats that rated a part 3 or 4 and got under half of it
   right.
7. The stretch page is not marked. Anyone who wrote on it keeps it for the mock-interview round.

Say once, at the start, that the marker is deciding nothing. Reading somebody else's answer against
the key is the exercise, and it is harder than being marked.

---

## The solution discussion, 90 minutes

### Most-missed first, 35 minutes

Before the anchors, take the items the room actually lost, in the order the workbook's Discussion
sheet gives them: the six at the top, at about five minutes each. Ask for hands on the paper each
person marked, "a cross on Q5?", so the room sees the count before the item is discussed. A show
of hands on the paper you marked is never a show of hands on your own score, so nobody is exposed.
The candidate list below is the prediction: the item, the wrong answer it tempts, the question that
sends the room looking for the fault, and the repair said aloud.

| Item | The wrong answer most papers give | Ask the room | The repair, said aloud |
|---|---|---|---|
| Q2, the net-sales cell | (a), 26 orders and Rs 535760, the total the analyst meant | "Read the condition the way Python groups it. What does it give for a cancelled order?" | The right side of the or is a non-empty string, so every order passes and all 30 count; write `status in ("delivered", "returned")` and check the total against the status table's 26 orders and Rs 5,35,760. |
| Q4, the discount's effect | A fall of 5 percent, the two percentages added | "What happens to the price of every unit the extra 10 percent buys?" | The branches multiply: 1.10 times 0.85 is 0.935, a fall of 6.5 percent, and at 15 percent off volume must rise 17.6 percent just to hold revenue. |
| Q5, the quarter counter | (a), 114 and 86 orders and -24.6 percent, the count the analyst meant | "Where is n set back to zero, and which segment runs last?" | The counter restarts for every segment, so each quarter keeps Student's count, 5 and then 7; set it once per quarter, and check that the quarters add back to the file's 200 orders. |
| Q9, the extra next() | (a), 201 and KR-02001, trusting the comment | "Who read the header line, the DictReader or the next()?" | The DictReader reads the header itself, so next() drops the first order; count the rows read against the file's 201 before cleaning anything. |
| Q11, the auditor's copy | (a) or (b), True, trusting rows.copy() to protect the dictionaries | "Draw both lists and the dictionaries they hold. How many dictionaries are there?" | A list copy is shallow: both lists hold the same two dictionaries, and the pass rewrote them; copy each dictionary, or keep the file itself as the evidence. |
| Q12, removing inside the loop | (a) or (e), or only one of (b) and (d) | "Which row did the loop never test, and why do the counts still close?" | Removing from the list being walked skips the row after each removal; walk a copy or build two new lists, then check that every input row landed in exactly one of them. |
| Q14 and Q15, Monday's number | Q14 (c), 11.0 percent, and on Q15 a fall of 49.0 percent | "What has Anand's reconciliation changed since Tuesday?" | The 14 duplicated Q1 rows, Rs 19,98,210, were never in the books: revenue fell 1.6 percent, and Retail-Plus orders per member fell 35.0 percent, from 1.82 to 1.18. |
| Q18, the flipped sign | (a), -880 and 0.021, the class's p beside the new sign | "Which way does the real gap point now, and which way does the count look?" | The count must run in the direction of the claim; a p near 1 on a gap that looked large is the tell that a sign flipped. |
| Q19, the Student line | (c), 0.397 proves the rise is noise | "What separates 'chance explains it easily' from 'chance proves it false'?" | A large share says the data cannot tell a real rise from luck; hold, and re-read at 30 orders with the count beside the rate. |
| Q21 and Q22, the Diwali advice | Q21 (a), repeat it because the total rose; Q22 (d), compare the customers who opt in | "Inside which segment did the sale group spend more?" | Inside both segments the sale group spent 3.0 percent less, so the lift is the mix of who got the sale; Diwali holds back a random share inside each segment and compares within it. |
| Q23, two averages of seven countries | (b), the two figures swapped | "How much does New Zealand's one year weigh in each average?" | Averaging the country averages gives one year the vote of nineteen; say which weighting you used and show the other beside it. |
| Q26, the basketball searches | (b) alone, missing (e), or (a) | "What else rises every winter, and how many terms were tried?" | The season drives both, and among millions of terms some fit by chance; test a correlation on data it was not chosen on, against a seasonal baseline. |
| Q28, per member or per buyer | (a) or (b), True, the buyers' figure is fairer | "Who is missing from the per-buyer figure, and in which quarter did they go missing?" | Members who stopped buying drop out of it, which halves the fall, from about a third of Q1's spend to about a sixth; per member keeps all 22 and shows the fall as it is. |
| Q29, the tool that prints | (a), 'out for delivery' | "What does a function with no return statement hand back?" | The model reads 'None'; a tool returns its result, and the log records what the model actually received. |
| Q31, the looping conversation | (b), the median with C-07 deleted from the log | "Which number does Finance pay, and which describes the typical conversation?" | The median for the typical cost, the sum with every run in it for the bill, and a cap on model calls per conversation to stop the next loop. |
| Q35 and Q36, NULL and integers | Q35 (e), 600, and Q36 (b), 0.375 | "What does AVG do with a NULL, and what type does COUNT(*) return?" | AVG leaves the timeouts out, so report them beside it; an integer over an integer drops the fraction, so multiply by 1.0 before dividing. |

If an item outside this list sits higher on the Discussion sheet, it wins its place. The list is a
prediction, and the sheet is the evidence.

On every item, take the wrong answer first. Ask who wrote it, or who nearly did, and have them say
why it looked right; the key file's line for that option names the misconception, and the room
repairs it before you read the key's reason. On a code item, have one learner trace it aloud at the
board, a line at a time, before the key is read: the fault usually shows on the board a line before
the wrong answer does.

### The interview anchors, 50 minutes

Ask each anchor aloud as an interviewer would: name the person, then the question, then wait. Give
sixty seconds. After the answer, ask the room what one sentence would make it stronger, and read
the answer below only if nobody gets there. The items listed after each anchor are the ones on the
paper that descend from it, so a learner who lost those items is a good person to call. Ten anchors
in 50 minutes is five minutes each, so keep the clock on the board.

#### 1. [S] Kalpa wants 15 percent growth; draw the revenue tree and name the branch you would investigate first.

*Q2, Q4, Q7 and Stretch 1.*

A strong answer draws the tree first: revenue is customers, times orders per customer, times items
per order, times price per item, less discounts. It then says that a 10 percent lift in any branch
adds the same revenue, so the first branch to investigate is the one the data says has moved, and
in Kalpa's two quarters the customer count held while orders per customer fell, so frequency is
where the growth leaks. It closes on what would change that choice, the cost of moving each branch,
which is Q7: acquisition becomes the better spend only if a rupee there buys more revenue than a
rupee spent bringing customers back. Q4 is the tree's arithmetic in one line, since the branches
multiply and a 15 percent discount that lifts volume 10 percent loses 6.5 percent of revenue.

Listen for a learner who names a branch before drawing the tree, or who reads orders per customer
off a count of rows. Those are the answers interviewers mark down.

#### 2. [S] Sales fell from Q1 to Q2; walk the investigation ladder.

*Q5 to Q8, Q14 and Q15.*

Five rungs, in this order: confirm the drop is real; compare like with like, which means the same
weeks and the same definitions; decompose along the revenue tree; isolate the branch and the
segment; then hypothesise and name the evidence that would settle it. Kalpa's own case on Tuesday
lands on the fourth rung. On closed quarters booked revenue fell 11.0 percent, from Rs 2.10 crore to
Rs 1.87 crore; the same 69 customers bought in both, orders per customer fell from 1.65 to 1.25, down
24.6 percent, and revenue per order rose 18.0 percent, mostly from the mix. The segment is
Retail-Plus, whose orders per member fell from 2.32 to 1.18 on the file as exported. Wednesday then
sent the case back to the first rung: 14 duplicated Q1 rows made the drop look larger than it was,
and on the reconciled file revenue fell 1.6 percent and Retail-Plus orders per member 35.0 percent.

The follow-up worth asking: "which rung did you skip on the paper?" Most people skip the second, and
Q14 is the second rung in full: a tile that set 11 weeks of Q2 against 13 of Q1, and a duplicated Q1
set against a clean Q2. Q5 is the first rung's cheapest check, since the quarter counts must add
back to the orders in the file.

#### 3. [S] Mean or median for order value, and why?

*Q1, Q3 and Q31.*

Order values are skewed by a few very large orders, so the median describes the typical order and
the mean does not: five orders of 800, 1,200, 1,400, 2,000 and 480,000 rupees have a median of
Rs 1,400 and a mean of Rs 97,080. The mean still matters, because mean times the number of orders is
revenue. The answer is to report both when they diverge and to say why they diverge.

Q3 puts the choice inside Marketing's payback model, where the Rs 4,80,000 order stays in the file
with a flag because it is a real sale. Q31 asks it again of an agent's bill: one looping
conversation is 81 percent of a shift's cost, so the median describes the typical conversation, the
sum is what Finance pays, and neither answer deletes the loop from the log.

#### 4. [S] Finance and the dashboard disagree by Rs 20 lakh; what do you do first?

*Q9, Q13, Q14, Q16, Q25 and Stretch 3.*

Profile the export before arguing about the number: duplicates, the date window, and what each side
counts. Then reconcile counts first and rupees second, line by line, against Finance's books, which
are the reference for money. In Kalpa's case the Rs 20 lakh was 14 duplicated Q1 rows worth
Rs 19,98,210, which a whole-row check could not see because a re-sent copy carries a different date,
the point of Q13. Q25 is the same disagreement in public: two navigation methods that should have
agreed did not, the discrepancy was reported only informally and never resolved, and the board
traced the loss to a units error.

Ask the second question the first time round, and wait for it: **what would you refuse to do?**
Adjusting your own figure until it agrees. Reconciling and fabricating differ only in whether the
steps are written down.

#### 5. [S] What does p = 0.03 mean, and not mean?

*Q17, Q18 and Stretch 2.*

If chance alone were at work, a gap at least this large would turn up in about 3 percent of
shuffles, so the gap would be rare under chance. It does not mean a 3 percent chance the finding is
wrong, it does not mean a 97 percent chance it is real, and it says nothing about whether the gap is
large enough to act on.

Take three definitions in a row without comment and write all three on the board. Then ask which
one survives somebody saying "so there is a three percent chance we are wrong". Q18 adds the
direction: the count runs the way the claim runs, so a p of 0.981 on a fall of Rs 880 is a sign that
flipped in the code, and it says nothing about the fall.

#### 6. [F] Input 200, clean 183, rejected 14: does it reconcile, and what is the missing number?

*Q9, Q12, Q16 and Q24.*

It does not reconcile: 183 plus 14 is 197, so 3 rows are unaccounted for. Nothing is reported
until those 3 are found, and the usual culprits are rows removed by a step that does not write to
the rejects log, such as a de-duplication, or a row lost at the read, as Q9's extra next() loses
one. Then say the rupee half aloud: even when the rows close, the rupees have to close too, and rows
can close by construction, as Q12's loop shows, while an unreadable row sits among the clean ones.
Q24 is the same count in a spreadsheet, where a formula covered 15 of the sheet's 20 countries.

#### 7. [F] 42 percent on 12 orders against 31 percent on 400; which do you trust?

*Q19 and Q33.*

The 31 percent. On 12 orders a single order moves the rate by more than 8 points, so 42 percent is
five orders out of twelve, and a shuffle would show chance producing gaps like it often. On 400
orders one order moves the rate by a quarter of a point. The 12-order figure is a question to
collect more data on, never a finding, and the Student segment on Thursday was exactly this case:
Q19 writes its line for Meera, and Q33 writes Kavya's floor of 30 into a query.

#### 8. [F] Revenue rose after the discount; three reasons that is not proof it worked.

*Q4, Q20 to Q22 and Q26.*

First, who received it: the sale was aimed at Retail-Plus, whose members buy more often and spend
more in any month, so membership drives both getting the discount and spending, which makes it a
confounder. Second, the mix: half the sale group was Retail-Plus against two in five of the rest,
and inside both segments the sale group spent 3.0 percent less, so the 6.1 percent is a mix effect;
at the other group's mix the sale customers would have averaged Rs 3,104 against Rs 3,200. Third,
nothing was held out, so the season and the monsoon itself are not ruled out, which is how Q26's
basketball searches came to track flu. At 15 percent off, volume must also rise 17.6 percent just to
hold revenue. The honest recommendation is Q22's: hold back a random share inside each segment at
Diwali and compare within the segment.

#### 9. [D] Your cleaning run reported zero rejects on a file you know is dirty; what do you check?

*Q10 to Q13 and Stretch 3.*

Treat the zero as a bug in the checker until it is proven otherwise. Check that every field was
converted from text before the rules ran, because a comparison on text gives a wrong answer without
an error, as '4500' < '30000' does in Q10. Check that the duplicate check is keyed on the identity
rule rather than on whole records, which is Q13, and that the loop tested every row, since Q12's pass
skips the row after each removal and still reconciles. Check that input equals clean plus rejected,
that the rejects log is actually being written, and that the raw rows survived the pass, which
Q11's shallow copy does not allow. Then plant one row you know is bad and rerun. If the planted row
does not land in the log, the run was never checking anything.

#### 10. [D] Write the four-part note for the Retail-Plus finding in four sentences, then defend the caveat.

*Q19, Q28 and Stretch 2.*

Claim: Retail-Plus really is spending less, and the fall is small against the company. Evidence:
its 22 members delivered Rs 1,110 less each in Q2 than in Q1, and chance made a fall that large in
135 of 5,000 shuffles, p = 0.027, while Retail-Core's Rs 110 gap came back in 1,724 of 5,000, p =
0.345, which is the usual wobble; the fall is Rs 24,420 a quarter, 0.19 percent of delivered
revenue. Caveat: August's sale was aimed at Retail-Plus, and nothing here measures why its members
spent less. Action: test a retention offer on half of Retail-Plus before anything is rolled out.

Then defend the caveat against the room. Listen for a caveat that is a condition rather than a
hedge: "this may not be accurate" is a hedge, while "nothing here measures why they spent less"
names what would change the claim. Q28 is the denominator behind the evidence line: per member,
all 22 count, so the members who went quiet show up as the fall they are, where a per-buyer figure
would hide half of it. Q19 is the same note written for Student, with its caveat and the trigger
that would change it.

### The ratings against the work, 5 minutes

Close the discussion on the workbook's Ratings sheet. Read each part's mean rating beside its right
rate, from Part 1 to Part 5, and then name the parts where confidence ran ahead of the work: a
high mean rating beside a low right rate, and above all a part whose last column counts seats that
rated it 3 or 4 and got under half of it right. Say it about the room, never about a seat. Those
parts go on the board as the first line of Monday's revision, because a gap the room did not know it
had is the one an interviewer finds first.

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
pick its favourites. Each anchor appears twice in the table, and each follow-up sits beside an
anchor it extends:

| Pair count | First interviewer asks | Follow-up | Second interviewer asks | Follow-up |
|---|---|---|---|---|
| 1, 6, 11 and on | Anchors 1 and 7 | Stretch 1 | Anchors 4 and 9 | Stretch 3 |
| 2, 7, 12 and on | Anchors 2 and 8 | Stretch 1 | Anchors 5 and 6 | Stretch 2 |
| 3, 8, 13 and on | Anchors 3 and 10 | Stretch 4 | Anchors 4 and 6 | Stretch 3 |
| 4, 9, 14 and on | Anchors 5 and 8 | Stretch 2 | Anchors 1 and 9 | Stretch 3 |
| 5, 10, 15 and on | Anchors 2 and 7 | Stretch 4 | Anchors 3 and 10 | Stretch 2 |

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
> from the warehouse itself, with nothing a person can mistype. The tree and the ladder stay as they
> are; the tool changes."

Point back at Q32 to Q36 on the way out: the room has already read WHERE, HAVING, a NULL and an
integer division on an agent's log, and Monday puts the same clauses on Kalpa's warehouse. Then one
question to the room, and take three answers: **which parts of this week's work should never be done
in a notebook again, and why?** The answers worth hearing are anything Finance depends on, anything
that has to run unattended, and anything an auditor will read. That is Monday's first slide.

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

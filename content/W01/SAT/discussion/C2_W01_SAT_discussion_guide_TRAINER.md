# Week 1 Saturday: the discussion guide

**TRAINER ONLY.** The Academic TA leads the Saturday from the break onwards. The paper and its key
are in `paper/` and `answer-key/`, and the Word files there are what the room sits and what you read
from. The key file carries every item's key, tag, level, day and interview anchor, and a paragraph
per item on why the key holds, why each wrong option fails and the interview answer in one breath.

The discussion is worth more than the marking. Every answer is treated as an interview answer, and
the format is deliberately uncomfortable: papers are swapped, call-outs are random, and the last
half hour puts every learner on the interviewer's side of the table.

The paper runs in five parts, and 21 of its 35 timed items are hard: each takes several dependent
steps on an exhibit, so expect the room's scores to sit lower than on a recall paper. Parts 1 to 3
climb Kalpa's week: the revenue tree, the Q1 reconciliation, and Meera's questions for Monday's
growth review. Part 4 sets the week's traps in public cases, each with its source named beside it,
and the key's reasons carry what each source reports; when the room asks about a case, answer from
those reasons and add nothing beyond them. Part 5 is a food-delivery company that does not exist:
its offer, its agent, its logs and every number in it are illustrative, and it names no real company.

---

## The shape of the 300 minutes

| Block | Duration | What happens |
|---|---|---|
| The paper | 120 min | Pen and paper, AI-free, no notes: step one's five ratings, then 35 timed items in five parts, then the untimed stretch page for anyone who finishes early. |
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
   since the five parts number straight through to Q35. On the match items, Q33 to Q35, read the
   letter and then its value, "Q33, c, 6", so a marker can check either.
3. The marker writes a tick or a cross beside every item on the answer sheet, then each part's
   ticks in the box beside that part's rating and their total as Items right, out of 35, and hands
   the paper back, so each learner reads their rating against their score part by part.
4. The key file's marking rule decides the edge cases: every correct letter and no other on a
   more-than-one item (Q11, Q17 and Q25), the letter on a match item, the number on a worked item,
   and the whole sequence on an ordering item (Q7 and Q15). Q1 needs both the median and the mean.
   Q3 is Rs 2,060 and Q12 Rs 10,930. Q13, Q14 and Q27 need the direction as well as the size, so
   -1.6, -35.0 and -2.5 match the key, and a bare 1.6, 35.0 or 2.5 does not, since each key names a
   fall. Q9, Q10 and Q23 are true or false with the reason, answered with a letter. There is no
   partial credit, because the programme has set no rule for it.
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
person marked, "a cross on Q6?", so the room sees the count before the item is discussed. A show
of hands on the paper you marked is never a show of hands on your own score, so nobody is exposed.
The candidate list below is the prediction: the item, the wrong answer it tempts, the question that
sends the room looking for the fault, and the repair said aloud.

| Item | The wrong answer most papers give | Ask the room | The repair, said aloud |
|---|---|---|---|
| Q2, the net-sales cell | (a), Meera's figure exactly, or (d), the right line with the returns as the gap | "Read the condition the way Python groups it. Which status is Meera's figure missing?" | The right side of the or is a non-empty string, so all 30 orders count, Rs 5,44,810; Meera leaves out only the cancelled orders, so the cell is Rs 9,050 over. |
| Q3, the first order | Rs 2,205, the median of all 30, or Rs 24,800, the delivered mean | "Which orders stay paid for, and which statistic describes the typical one?" | Delivered orders only, and the median, since one Business order is 92 percent of their rupees: the 11th of 21 is Rs 2,060, with the bulk order kept and flagged. |
| Q4, the quarter counter | (a), 114 and 86 rows and -24.6 percent, the count the analyst meant | "Where is n set back to zero, and which segment runs last?" | The counter restarts for every segment, so each quarter keeps Student's count, 5 and then 7; the quarters must add back to the file's 200 rows. |
| Q6, what flips the call | (a) or (b), the changes that help acquisition and still fall short | "Work each change out. Which one moves a ratio past the other?" | Rs 2.00 a rupee against Rs 2.50; only a Rs 800 win-back, Rs 1.88, drops below acquisition, and the turning point is Rs 750. |
| Q8, the extra next() | (d), trusting the pass to notice a missing order | "What count did the pass start from, and where did the lost row go?" | The pass reconciles what it receives, 200 = 185 + 15, so KR-02001 vanishes without a trace; only the file's own 201 rows catch it. |
| Q10, the auditor's copy | (a) or (b), True, trusting the copy | "Draw both lists and the dictionaries they hold. What did the append touch, and what did the pass touch?" | The copy is a new list, so it keeps two rows, but the dictionaries are shared, so its first amount now reads 0; copy each dictionary, or keep the file. |
| Q12, the identity rule | Rs 14,640, trusting the whole-row check | "Which repeat does a whole-row check miss, and why?" | Row 6 repeats KR-02151 with a new date, so only the identity rule catches it; Q2 holds Rs 10,930. |
| Q13 and Q14, Monday's number | Q13 a fall of 11.0 percent, and Q14 a fall of 49.0 percent | "What has Anand's reconciliation changed since Tuesday?" | The 14 copied Q1 rows, Rs 20,00,000, were never in the books: revenue fell 1.6 percent, and Retail-Plus orders per member fell 35.0 percent. |
| Q16, real or the wobble | (b), both tails, or (d), the fall per member written as the tier's | "Which direction does Kavya's rule count, and how many members share the fall?" | 145 of 5,000 shuffles, 0.029, counted in the direction of the fall, and Rs 1,110 for each of 22 members is Rs 24,420 a quarter. |
| Q19, the Student line | (a), 951 worlds, or (c), "the rise is noise" | "Which rows of the table are a rise of 40 percent or more?" | Seven or more of the 12 orders in Q2, 1,985 of 5,000 worlds; a large share says the data cannot tell, so hold and re-read at 30 orders. |
| Q21, two averages of seven countries | (b), the two figures swapped | "How much does New Zealand's one counted year weigh in each average?" | Averaging the country averages gives one year the vote of nineteen: -0.07, which rounds to the published -0.1, against 1.68 by year. |
| Q23, per member or per buyer | (a), True, the fall among members still buying | "Who is missing from the per-buyer figure, and when did they go missing?" | Six members stopped buying, so per buyer shows a sixth of the fall where per member shows a third; the tier includes the members who went quiet. |
| Q27 and Q28, the delivery company's offer | Q27 a rise of 6.8 percent, and Q28 (b), a quarter | "Inside which tier did the offer group spend more? What does 25 percent off do to each order?" | Each tier spent less, so at one mix the offer group is 2.5 percent down; at 25 percent off orders must rise by 1 over 0.75, a third, just to hold revenue. |
| Q29 and Q30, the agent's code | Q29 (d), try and except; Q30 (c) or (d) | "What does a function that runs off its end hand back? What is in history when C calls?" | No error is raised: the model reads 'None', so return the not-found message. The default list is built once, so C's call sends 5 messages; default to None. |
| Q31, the looping conversation | (c), a saving of Rs 42.00, or (b), the median without C-07 | "What does the capped conversation still pay for?" | The median of all seven is Rs 1.60, and C-07 capped at 5 calls still costs Rs 2.00, so the cap saves Rs 40.00. |
| Q32 and Q34 to Q35, SQL | Q32 (b), refund alone; Q34 600 and Q35 0.375 | "What counts as failed? What does AVG do with a NULL, and what type does COUNT(*) return?" | Failures include timeouts, so order_status reaches 34; AVG leaves the timeouts out; PostgreSQL divides integers as integers, so multiply by 1.0 first. |

If an item outside this list sits higher on the Discussion sheet, it wins its place. The list is a
prediction, and the sheet is the evidence.

On every item, take the wrong answer first. Ask who wrote it, or who nearly did, and have them say
why it looked right; the key file's line for that option names the misconception, and the room
repairs it before you read the key's reason. On a code item, have one learner trace it aloud at the
board, a line at a time, before the key is read: the fault usually shows on the board a line before
the wrong answer does. On a worked item, have one learner write the three steps on the board before
anyone says a number.

Two items need their endings said aloud whatever the sheet shows. On Q26, the Bing alert, the first
move is to check the plumbing, and the case ended well: the checks passed, the lift was real, 12
percent and more than 100 million US dollars a year, the best revenue idea in Bing's history. On
Q19, name the thin base: all 12 Student orders came from 2 customers, so one customer's habits could
make the whole rise.

### The interview anchors, 50 minutes

Ask each anchor aloud as an interviewer would: name the person, then the question, then wait. Give
sixty seconds. After the answer, ask the room what one sentence would make it stronger, and read
the answer below only if nobody gets there. The items listed after each anchor are the ones on the
paper that descend from it, so a learner who lost those items is a good person to call. Ten anchors
in 50 minutes is five minutes each, so keep the clock on the board.

#### 1. [S] Kalpa wants 15 percent growth; draw the revenue tree and name the branch you would investigate first.

*Q2, Q6, Q28 and Stretch 1.*

A strong answer draws the tree first: revenue is customers, times orders per customer, times items
per order, times price per item, less discounts. It then says that a 10 percent lift in any branch
adds the same revenue, so the first branch to investigate is the one the data says has moved, and
in Kalpa's two quarters the customer count held while orders per customer fell, so frequency is
where the growth leaks. It closes on what would change that choice, the cost of moving each branch,
which is Q6: on Marketing's own estimates winning a member back returns Rs 2.50 in the quarter for
each rupee against Rs 2.00 for a new customer, and acquisition takes the lead only if a win-back
costs more than Rs 750. Q28 is the tree's arithmetic under a discount: the branches multiply, so 25
percent off needs a third more orders just to hold revenue.

Listen for a learner who names a branch before drawing the tree, or who reads orders per customer
off a count of rows. Those are the answers interviewers mark down.

#### 2. [S] Sales fell from Q1 to Q2; walk the investigation ladder.

*Q4 to Q7, Q13 and Q14.*

Five rungs, in this order: confirm the drop is real, which means each quarter's figure is complete
and free of pipeline errors; compare like with like, which means the same weeks and the same
definitions; decompose along the revenue tree; isolate the branch and the segment; then hypothesise
and name the evidence that would settle it. Kalpa's own case on Tuesday lands on the fourth rung.
On closed quarters booked revenue fell 11.0 percent, from Rs 2.10 crore to Rs 1.87 crore; the same
69 customers bought in both, orders per customer fell from 1.65 to 1.25, down 24.6 percent, and
revenue per order rose 18.0 percent, mostly from the mix. The segment is Retail-Plus, whose orders
per member fell from 2.32 to 1.18 on the file as exported. Wednesday then sent the case back to the
first rung: 14 copied Q1 rows, Rs 20,00,000, made the drop look larger than it was, and on the
reconciled file revenue fell 1.6 percent and Retail-Plus orders per member 35.0 percent.

The follow-up worth asking: "which rung did you skip on the paper?" Most people skip the second, and
Q13 is the second rung in full: a tile that set 11 weeks of Q2 against 13 of Q1, and a Q1 that
still held its copies. Q4 is the first rung's cheapest check, since the quarter counts must add back
to the rows in the file.

#### 3. [S] Mean or median for order value, and why?

*Q1, Q3 and Q31.*

Order values are skewed by a few very large orders, so the median describes the typical order and
the mean does not: five orders of 800, 1,200, 1,400, 2,000 and 4,80,000 rupees have a median of
Rs 1,400 and a mean of Rs 97,080. The mean still matters, because mean times the number of orders is
revenue. The answer is to report both when they diverge and to say why they diverge.

Q3 adds the question of which orders count: a payback model wants orders that stay paid for, so the
figure is the median of the 21 delivered orders, Rs 2,060, with the Rs 4,80,000 Business order kept
in the file with a flag. Q31 asks it again of an agent's bill: one looping conversation is most of a
shift's cost, so the median describes the typical conversation, the sum is what Finance pays, and a
cap on model calls, never a deletion from the log, stops the next loop.

#### 4. [S] Finance and the dashboard disagree by Rs 20 lakh; what do you do first?

*Q8, Q12, Q13, Q15, Q24 and Stretch 3.*

Profile the export before arguing about the number: duplicates, the date window, and what each side
counts. Then reconcile counts first and rupees second, line by line, against Finance's books, which
are the reference for money. In Kalpa's case the gap was 14 copied Q1 rows, Rs 20,00,000 in
Tuesday's file, which Finance's books never held; and a check on whole rows misses any copy whose
date or amount changed on the way, as Q12's KR-02151 shows. Q24 is the same disagreement in public:
two navigation methods that should have agreed did not, the discrepancy was reported only informally
and never resolved, and the board traced the loss to a units error.

Ask the second question the first time round, and wait for it: **what would you refuse to do?**
Adjusting your own figure until it agrees. Reconciling and fabricating differ only in whether the
steps are written down.

#### 5. [S] What does p = 0.03 mean, and not mean?

*Q16, Q17, Q18 and Stretch 2.*

If chance alone were at work, a gap at least this large would turn up in about 3 percent of
shuffles, so the gap would be rare under chance. It does not mean a 3 percent chance the finding is
wrong, it does not mean a 97 percent chance it is real, and it says nothing about whether the gap is
large enough to act on.

Take three definitions in a row without comment and write all three on the board. Then ask which
one survives somebody saying "so there is a three percent chance we are wrong". Q16 and Q18 add the
direction: the count runs the way the claim runs, so say which way you counted. Q16's fall is 145 of
5,000 shuffles in the direction of the fall and 286 counted both ways, and Q18's p of 0.981 on a
fall of Rs 880 is a sign that flipped in the code, and it says nothing about the fall.

#### 6. [F] Input 200, clean 183, rejected 14: does it reconcile, and what is the missing number?

*Q8, Q11, Q15 and Q22.*

It does not reconcile: 183 plus 14 is 197, so 3 rows are unaccounted for. Nothing is reported
until those 3 are found, and the usual culprits are rows removed by a step that does not write to
the rejects log, such as a de-duplication, or a row lost at the read. Then say the harder half
aloud: a pass reconciles the rows it receives, so Q8's order lost at the read leaves the counts
closed, and Q11's loop closes by construction while an unreadable row sits among the clean ones.
The check that catches both is the count against the source. Q22 is the same check in a
spreadsheet, where a formula spanned 15 of the sheet's 20 country rows.

#### 7. [F] 42 percent on 12 orders against 31 percent on 400; which do you trust?

*Q19 and Q32.*

The 31 percent. On 12 orders a single order moves the rate by more than 8 points, so 42 percent is
five orders out of twelve, and a shuffle would show chance producing gaps like it often. On 400
orders one order moves the rate by a quarter of a point. The 12-order figure is a question to
collect more data on, never a finding, and the Student segment on Thursday was exactly this case:
Q19 writes its line for Meera, from 2 customers, and Q32 writes a floor of 30 into a query's
HAVING.

#### 8. [F] Revenue rose after the discount; three reasons that is not proof it worked.

*Q20, Q25, Q27 and Q28.*

First, who received it: the sale went mostly to customers who buy more often and spend more in any
month, so the kind of customer drives both getting the discount and spending, which makes it a
confounder. Second, the mix: inside each segment the discounted customers spent less, so the
headline lift is who got the sale; Q27 is the same pattern at the delivery company, where a 6.8
percent lift becomes a 2.5 percent fall once both groups sit at one mix. Third, nothing was held
out, so the season is not ruled out, which is how Q25's basketball searches came to track flu. A
deeper cut makes it worse: at 25 percent off orders must rise by a third just to hold revenue. The
honest recommendation is Q20's: hold back a random share inside each segment and compare within it.

#### 9. [D] Your cleaning run reported zero rejects on a file you know is dirty; what do you check?

*Q9 to Q12 and Stretch 3.*

Treat the zero as a bug in the checker until it is proven otherwise. Check that every field was
converted from text before the rules ran, because a comparison on text gives a wrong answer without
an error, as '4500' < '30000' does in Q9. Check that the duplicate check is keyed on the identity
rule rather than on whole records, which is Q12, and that the loop tested every row, since Q11's pass
skips the row after each removal and still reconciles. Check that input equals clean plus rejected,
that the rejects log is actually being written, and that the raw rows survived the pass, which Q10's
shallow copy does not allow. Then plant one row you know is bad and rerun. If the planted row does
not land in the log, the run was never checking anything.

#### 10. [D] Write the four-part note for the Retail-Plus finding in four sentences, then defend the caveat.

*Q16, Q19, Q23 and Stretch 2.*

Claim: Retail-Plus really is spending less, and the fall is small against the company. Evidence:
its 22 members delivered Rs 1,110 less each in Q2 than in Q1, and in Kavya's shuffle, which keeps
each member's two quarters together, chance made a fall that large in 145 of 5,000 shuffles, p =
0.029 counted in the direction of the fall; the fall is Rs 24,420 a quarter, 0.19 percent of
delivered revenue. Caveat: counted both ways the share is 0.057, and nothing here measures why the
members spent less. Action: test a retention offer on half of Retail-Plus before anything is rolled
out.

Then defend the caveat against the room. Listen for a caveat that is a condition rather than a
hedge: "this may not be accurate" is a hedge, while "nothing here measures why they spent less"
names what would change the claim. Q23 is the denominator behind the evidence line: per member,
all 22 count, so the six members who stopped buying show up as the fall they are, where a per-buyer
figure would hide half of it. Q19 is the same note written for Student, with its caveat and the
trigger that would change it.

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

Point back at Q32 to Q35 on the way out: the room has already read WHERE, HAVING, a NULL and an
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

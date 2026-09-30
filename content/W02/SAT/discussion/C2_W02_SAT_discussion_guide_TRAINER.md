# Week 2 Saturday: the discussion guide

**TRAINER ONLY.** Led by the Academic TA. The paper the room sits is the Word file in `paper/`; the
key in `answer-key/` carries every item's key, tag, level, day, interview anchor, why the key holds,
why each wrong option fails, the bank items folded into each item, and the answers to the stretch
page.

SQL carries more interview weight than any other analyst skill, so this is the heaviest paper of
the first month. It is also the first paper whose items leave Kalpa: six items take the week's traps
to public cases, and Part 6 sets them in an AI team's tables. The afternoon turns what the paper
found into answers each learner can say aloud.

---

## The shape of the day

```mermaid
flowchart TB
  P["Paper, 120 min"] --> B["Break, 20 min"]
  B --> M["Marking, 20 min"]
  M --> D["Solution discussion, 90 min"]
  D --> I["Mock interviews in pairs, 30 min"]
  I --> X["Doubts and the bridge, 20 min"]
```

| Block | Duration | What happens |
|---|---|---|
| The paper | 120 min | Pen and paper, AI-free, no notes: 35 items in six parts, paced at 117 minutes, then the untimed stretch page for anyone who finishes early. |
| Break | 20 min | Papers stay face down on the desks. |
| Marking | 20 min | Papers swapped and marked against the key, read out by the Academic TA, and the ticks entered by seat in the item-analysis workbook. |
| The solution discussion | 90 min | The most-missed items first (35 min), then the ten anchors answered aloud as interview answers with random call-outs (50 min), and the step-one ratings set against the work (5 min). |
| The mock-interview round | 30 min | In pairs: each learner asks the other two anchors and one stretch follow-up, then they swap. |
| Doubts and the bridge | 20 min | Open doubts, then Monday: Build 1 opens in Kalpa Health. |

Three hundred minutes in all, with no new content anywhere in them.

---

## The paper, 120 minutes

Hand out the Word paper face down and start the time together. Step one on the first page comes
before any item: each learner rates the six parts from 1 to 4 on the answer sheet, as they are
today. Laptops closed and phones away for the whole sitting. Announce the time left at 60 minutes
and at 15 minutes. Say once, before the start, that Parts 5 and 6 name real companies and public
cases: every fact in them is on the page with its source, and Part 6's tables are illustrative, so
nobody needs to know the companies to answer. Anyone who finishes early turns to the stretch page,
which is untimed and uncounted; its four follow-ups come back in the mock-interview round, so a
learner who writes them now has rehearsed.

## Marking, 20 minutes

1. Papers swap along the row, so nobody checks their own paper.
2. Read the key part by part from the key file: letters in runs of five, the word-bank and match
   letters one at a time, numbers one at a time, and each ordering item's sequence slowly, twice.
3. The marker ticks or crosses each item on the answer sheet, writes each part's ticks in the box
   beside that part's rating and their total as Items right, out of 35, and hands the paper back,
   so each learner reads their rating against their score part by part.
4. The key's rule settles the edge cases: every correct letter and no other on a more-than-one item
   (Q11 and Q19), the letter on a word-bank or match item (Q3, Q4 and Q23 to Q26), the number on
   Q17 and Q29 with the working left to the discussion, and the whole sequence on an ordering item
   (Q2 and Q8). There is no partial credit, because the programme has set no rule for it.
5. The Academic TA enters each paper by seat in
   `answer-key/C2_W02_SAT_item_analysis_TRAINER.xlsx`, never by name: the ticks in the Marks
   sheet, 1 for a tick, 0 for a cross and a blank for an item left empty, and the six step-one
   ratings from the answer sheet in the Ratings sheet. Its Discussion sheet gives the most-missed
   order the discussion takes, and any item it flags goes to the tracker's owner with the room's
   rate, because the fault may sit in the item rather than in the room.

Say once, at the start, that the marker decides nothing: reading somebody else's answer against the
key is the exercise. The paper carries no marks and ranks nobody; the misses are counted by topic
only so that Monday's session knows what to revisit.

---

## The solution discussion, 90 minutes

### Most-missed first, 35 minutes

Take the order from the workbook's Discussion sheet: the five most-missed items, from the top. The
candidate list below says what each likely miss tests, the wrong answer most papers will hold, the
question to put to the room before anyone reads the key, and the repair to listen for; an item
outside it that the sheet ranks higher takes its place. If the entry is not finished when the
discussion opens, read the list instead, ask for hands, and write the counts on the board. For each
item, ask "a cross on item 12?", call one person who crossed it to say what they wrote and why it
looked right, then put the question below to the room before reading the repair. The key file's
"Why each answer holds" section has the reason behind every wrong option.

| Item | What it tests | The answer most papers will hold | Ask the room | The repair, said aloud |
|---|---|---|---|---|
| 12 | Counting what each tie rule ships | 51, 51 and 50, reading DENSE_RANK as RANK without the gap | "Read the dense ranks down Exhibit 3A. Where do they fail to climb?" | Two ties, not one: the tie at 48 compresses the dense numbers, so C-0259 reaches 50 and DENSE_RANK ships 52. RANK ships 51 and ROW_NUMBER 50. |
| 15 | LAG across a missing month | C-0161 and C-0171 only, believing LAG steps back a calendar month | "For C-0185's September row, which row does LAG(spend, 1) read?" | LAG reads the previous row, which for C-0185 is July. All four are flagged; a calendar check keeps the two genuine falls, and a month with no order is no reading. |
| 9 | A date filter on a LEFT join | 3 rows or 4, reading the WHERE as if it sat in ON | "O-3 has no payment. What is its paid_date after the join, and what does BETWEEN do with it?" | The WHERE runs after the join and drops O-2 and O-3, and O-1's two instalments repeat it: 2 rows, Rs 2,400. The date belongs in ON, with payments at one row per order first. |
| 33 | NOT IN against a list that holds a NULL | 2, the answer NOT EXISTS gives | "Write out c1 NOT IN ('c2', 'c4', NULL) as three comparisons. What is the last one?" | c1 <> NULL is unknown, so the whole condition is unknown and every row drops: 0. The review would call a working assistant useless. Write the anti-join as NOT EXISTS or a LEFT JOIN with IS NULL. |
| 8 | The order of a reconciliation | Summing the payments before dropping the repeats | "If you sum first, where do the gateway's repeats end up?" | Drop the repeats by order and instalment, sum to one row per order, join, check 462 rows and a gap equal to the unpaid list, then send. Summing first keeps Rs 20,750 in collected. |
| 6 | A denominator that shrank, and the base of a percentage | 40 percent, dividing the gap by the reported figure | "Too high compared with what?" | The CASE with no ELSE leaves the short views out of count, so 30 seconds over 3 views reads 10.0 against 6.0 per view; the overstatement is measured on the true 6.0, about 67 percent, inside the 60 to 80 percent TechCrunch reported for Facebook in 2016. |
| 19 | Which guard stops a double count | Ticking drop_duplicates() | "The six repeated rows differ in one column. Which one, and what does drop_duplicates() do with them?" | They differ in exposed_date, so drop_duplicates() keeps all 346. validate='one_to_one' raises MergeError and a row-count assert fails: those two stop the run. |
| 34 | Peers in a running total | 400, 700, 1200 and 1400, one step per row | "Calls 2 and 3 share a day. Which rows does the frame include for call 2?" | With ORDER BY day alone, calls 2 and 3 are peers and both read the day's close, 1200. Add call_id to the window's ORDER BY and each call gets its own step. |
| 31 | The latest row per key, repeatably | ROW_NUMBER on the date alone | "bot-b finished two runs on 9 September. Which one does your query keep tomorrow morning?" | ROW_NUMBER with the date alone picks one of the pair, so the board can show 0.86 one morning and 0.79 the next; the tiebreaker makes it repeatable. A GROUP BY with two max() calls invents a run. |
| 16 | A total against a run rate | "On plan, and the run rate is on plan" | "How many of the seven bars clear the line?" | The quarter closed on plan, Rs 10 ahead, and six of the last seven weeks sat below the weekly plan; the front-page line carries both, with its period and its comparison. |
| 10 | What leaves when a check fails late | Collected alone, with a footnote | "Which figure passed its checks, and which one rests on the check that failed?" | Booked passed both of its checks, so it goes; collected waits, and the Rs 21,750 goes out as a named open line with an owner and a time. |
| 11 | Checks that see a truncation | Ticking the .xlsx format | "Would the newer format have told anyone on the day?" | It raises the limit and checks nothing. Only a count of each file's records against the rows loaded, and a control total from the labs, compare what arrived with what was loaded. |

When a learner connects Parts 2 to 4 to the week's warehouse, discuss what the room found in class
(the repeats, the unpaid orders, the tie at fiftieth, the members who fell) and nothing beyond it;
the paper names those because the room has already found them. When a learner asks about the real
companies, keep to what each item's source reports and do not add to it.

### The anchors aloud, 50 minutes

Ask each anchor as an interviewer would: name the person, then the question, then wait. Give sixty
seconds. Ask the room for the one sentence that would make the answer stronger, and read the answer
below only if nobody gets there. Five minutes an anchor, with the bridge anchor last. The items under
each anchor descend from it.

#### 1. [S] WHERE against HAVING, one sentence each.

*Items 2 and 32.*

WHERE decides whether to keep one row, judged on that row alone, before any grouping exists. HAVING
decides whether to keep a whole group, judged on the group, after the grouping has happened. Listen
for the answer that says only "rows against aggregates": true, and it predicts nothing new, because
the timing is the answer. Q32 is the proof: bot-c forms no group at all, because WHERE removed its
rows before GROUP BY ran.

#### 2. [S] INNER against LEFT join: what does each drop or keep?

*Items 7, 9 and 33.*

An inner join keeps only the rows that find a partner, so an order with no payment disappears. A
left join keeps every row of the left table and fills the missing side with NULLs, so the unpaid
order stays, which is how Anand's unpaid orders are found: left join, then keep the rows where the
payment's key is NULL. Both can multiply rows, because each keeps every matching pair. The follow-up
to ask: what happens to that left join when a WHERE on the payments table is added? (Q9.)

#### 3. [S] RANK, DENSE_RANK and ROW_NUMBER on a tie.

*Items 12, 13, 31 and 34.*

On a tie, RANK gives the tied rows the same rank and skips the next ones (1, 2, 2, 4), DENSE_RANK
gives the same rank without a gap (1, 2, 2, 3), and ROW_NUMBER gives every row its own number and
breaks the tie arbitrarily. The strong answer adds the business consequence: the Retail-Plus list
ships 51 under RANK, 52 under DENSE_RANK and 50 under ROW_NUMBER, and a ROW_NUMBER with no
tiebreaker can hand two mornings two different leaderboards (Q31).

#### 4. [S] groupby in the split-apply-combine sentence.

*Items 21 and 30.*

groupby splits the rows by a key, applies a computation to each group, and combines the results into
one row per group. pivot_table is the same sentence with two keys, and its default apply step is the
mean, which is why M1's two June orders print as 2000.0 in Q21. The follow-up to ask: which rows
never reach a group at all? (A row whose key is missing, which is the dropna default.)

#### 5. [F] Your LEFT join grew the row count and revenue doubled; name the cause and the check.

*Items 7, 8 and 30.*

The cause is a key that repeats on the right side: an order paid in two instalments, or a payment the
gateway posted twice, appears once per payment row, and its amount is counted again. Neither table
has to hold a duplicate row for this to happen. The check is the row count before and after the
join, then a count of payment rows per order, and the fix aggregates the many side to the join's
grain first. Push until somebody says the duplication happened in the join, then ask what it does to
an evaluation metric (Q30): the model's two misses count twice.

#### 6. [F] Top-3 per segment: GROUP BY or a window, and why?

*Item 14.*

A window. GROUP BY collapses each segment to one row, so the members inside it are gone; a window
function ranks each member within its segment and keeps every row, and the top three are the rows
with rank three or less, filtered outside the window, with the tie rule chosen on purpose.

#### 7. [F] Which merge argument raises on duplicate keys, and which error?

*Items 17, 19, 20 and 22.*

validate, set to the relationship the merge must have, such as 'one_to_one' or 'many_to_one'. When
the keys break it, pandas raises MergeError: "Merge keys are not unique in right dataset; not a
one-to-one merge", before any number is produced. The follow-up to ask: what catches a key that
changed on its way in and so matches nothing? (indicator=True and a count of the matches, Q22.)

#### 8. [F] A pivot's total disagrees with the warehouse; where do you look first?

*Items 18, 24, 25 and 27.*

Upstream of the pivot, at the table it sums: compare the row count with the count of keys, then the
total with the warehouse's control total. In Set 3 six customers sit on two rows each, so the pivot
reads Rs 45,800 over the book; on Friday the raw export repeated every instalment order. A range
that stops short (Q27) fails the same check from the other side.

#### 9. [D] Same question, three tools: how do you choose, and defend one choice?

*Items 5, 26 and 28.*

The number travels in one direction: the warehouse computes the source of truth, pandas carries the
analyst's iteration, and Excel presents it and lets a director explore. A number Finance audits
belongs in the warehouse, because it runs the same way every Monday and anyone can audit the query.
Defend one choice with a reason about who depends on the number, never with a preference for a
tool, and name the second way that would catch a wrong formula (Q28).

#### 10. [D] Kalpa Health asks 'where does our growth come from'; say what stays the same in your method and what changes.

*No paper item; Parts 5 and 6 rehearse it, and this anchor opens the bridge.*

What stays the same are habits: count before you total, name the denominator, say what one row
means, reconcile against the owner's books, and ask who owns the number. The paper has already
carried them outside Kalpa, to a video metric, a public-health dashboard, a gene list, a bank's risk
model and an AI team's tables. What changes is the entity model, the vocabulary and the
stakeholders. The failure to listen for is somebody reaching for Retail's revenue tree in a
diagnostics business without first asking what a sale is there.

### Running random call-outs without losing the room

| Do | Do not |
|---|---|
| Name the person, then the question, then wait | Ask the room and take the first hand |
| Give sixty seconds, and let the silence run | Rescue somebody at fifteen seconds |
| Take a wrong answer, write it on the board, and ask the room to repair it | Correct it yourself |
| Come back to the same person later with an easier one | Leave somebody who struggled sitting with it |

Call on somebody whose paper you have not read, so the call is genuinely cold, and when an answer is
wrong, take the next answer from somebody else before correcting it, so the room does the work.

### Ratings against the work, 5 minutes

Close the discussion on the workbook's Ratings sheet. Its table for the room sets each part's mean
step-one rating beside the part's right rate, and counts the seats that rated a part 3 or 4 and got
under half of it right. Read out the parts where confidence ran ahead of the work, by part and never
by seat, and say what that costs at work: a part rated high and answered badly is where a number
would have shipped wrong from somebody sure it was right. Those parts open Monday's revision.

---

## The mock-interview round, 30 minutes

Pair learners who sat apart during the paper. Each pair plays two rounds of twelve minutes, then the
room takes six minutes together.

| Part | Duration | What happens |
|---|---|---|
| Round one | 12 min | The interviewer picks two anchors from the ten and one follow-up from the stretch page, and asks them in that order. The candidate answers aloud with no paper. |
| Round two | 12 min | They swap seats. The new interviewer may not repeat an anchor the pair has already used. |
| Back to the room | 6 min | Two pairs say which question was hardest to answer aloud, and the Academic TA asks one of those questions to a third person, cold. |

The interviewer holds the key's "In the interview" lines and the stretch answers, and listens for
three things: the answer starts with the business consequence, it names a check with a number, and
it stops when the question is answered. After each question the interviewer gives one sentence of
feedback, and nothing else. The Academic TA walks the room and sits in on pairs that have gone quiet.

---

## Doubts and the bridge, 20 minutes

Take open doubts first, for about twelve minutes. Then close on Monday: Build 1 opens in Kalpa Health
with the Programme Head's online introduction, an unfamiliar unit, unfamiliar data, unfamiliar
stakeholders, and a group of four in place of a room. Anchor 10 is the question the whole build week
asks. End on the sentence, and put it on the board:

```
The method transfers. The domain does not.
```

---

## After the session

Collect the marked papers. The workbook's Tags sheet gives the room's rate per tag and per part,
and its Seats sheet each seat's rate per tag; with the key file's list of items by tag, level, day
and part, the tags show which kind of thinking slipped, and the days point at where each gap came
from. That count by topic is what is kept, and it goes to Monday's session so it knows what to
revisit.

Any item where more than half the papers gave the same wrong answer points at the teaching and
belongs in a follow-up issue for the build team. The paper carries no marks, ranks nobody, and is
never read out by name.

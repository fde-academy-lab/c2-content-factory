# How does the TA run Wednesday's practice lab, what goes first when time is short, and where will learners stall?

**TRAINER ONLY.** This note is for the TA who runs the practice lab after the day, from
`exercises/practice/C2_W02_D03_lab_STUDENT.md`, with the escalated case's parts 3 to 5
(`exercises/unguided/C2_W02_D03_escalated_case_STUDENT.md` and
`notebooks/C2_W02_D03_ex1_escalated_case_STUDENT.ipynb`), the debrief of the room's wrong answers and
the interview drill around it. This page names the plants; no learner file does.

**Who needs the answer.** The TA needs it to decide what the lab runs, and in what order, after an
afternoon whose last 120 minutes went to the IITGN faculty block (tentative), so the trainer's own
afternoon held only chapter 6, the case's first two parts and the Kahoot. The lab has to leave every learner with the case finished, their wrong
answers heard once aloud, the day's habits run on fresh numbers and the interview questions said out
loud. A lab that replays the morning's items sends the room home without the drill and without the
debrief, the two parts nothing else in the day repeats.

**The questions on the way.**

- How does the lab's time run, and who works alone?
- What goes first when the lab runs short?
- Where do learners stall, and what is the one hint for each?
- How does the debrief run, and what does the TA say about each plant?
- Which interview questions does the drill ask, and in what order?
- What does a finished lab look like?
- What if the warehouse will not connect?

Keys: the escalated case, `1c 2b 3b 4a 5a 6c 7b 8b 9c 10b 11d 12b 13d 14c 15d`, of which parts 3 to 5
are items 5, 6 and 13, then 7, 8 and 14, then 9, 10 and 15; the practice set, `cbdabcadbc` for items 1
to 10; the second case, which goes home with the take-home, `ababaabdcd`. The reasons for every letter
are in `exercises/solutions/C2_W02_D03_escalated_case_solution_STUDENT.md`,
`exercises/solutions/C2_W02_D03_lab_solution_STUDENT.md` and
`exercises/solutions/C2_W02_D03_second_case_solution_STUDENT.md`; the executed notebook is
`exercises/solutions/C2_W02_D03_ex1_escalated_case_solution_STUDENT.ipynb`. Release each solution
when its part closes, never during it.

## How does the lab's time run, and who works alone?

The lab's own length is set for the day; its work comes to about 110 minutes, in this order.

| Part | Minutes | Alone or pairs | What it does |
|---|---|---|---|
| 1. The escalated case, parts 3 to 5 | 25 | Alone | Markers 5 to 10 in the notebook and the brief's items 13 to 15: each list's share of its segment, Q2 against plan by the total and the run rate, the two lines and the check before they leave |
| 2. The debrief of wrong answers | 10 | Whole room | The room's most common wrong letters from all five parts, read aloud with the check that catches each, and the plants the room found |
| 3. The practice set | 60 | Alone for problems 1 and 2, pairs for problem 3 | Three rankings predicted on an invented tie (10), GROUP BY or a window for six of Marketing's asks (10), and Kavya's drill on eight invented members (40) |
| 4. The interview drill aloud | 15 | Pairs | Sixty seconds an answer, the partner timing and asking one follow-up, the [D] questions last |

Learners who finish the set early take the stretch: the chapter sets' items not run live in
`exercises/unguided/`, which are items 1, 4 and 5 of chapter 1's set and items 3 to 5 of every other
set, chapters 4 to 6 first. Whatever is left is tonight's work
beside the take-home and the second case.

## What goes first when the lab runs short?

Cut in this order, and stop as soon as the lab fits.

1. The stretch goes home whole.
2. Problem 2 shrinks to item 4, the six asks, and item 5 goes home.
3. The drill shrinks to four questions: RANK, DENSE_RANK and ROW_NUMBER on a tie; the member on
   holiday; the running total that closes below the quarter's total; and "ties rank the same", which
   function and how many rows.
4. Problem 3 keeps items 6, 8 and 9; items 7 and 10 go home.
5. The escalated case's parts 3 to 5 and the debrief stay whole, because the case is the one place the
   learner runs the whole day alone.

## Where do learners stall, and what is the one hint for each?

| Part | Where they stall | The one hint |
|---|---|---|
| Escalated, marker 5 | They pick the running sum, option b, because it looks like the chapter's `sum() OVER` | "Should every Retail-Core row carry the same total, or a total that grows down the list?" |
| Escalated, marker 6 | They pick members over buyers, option b, because a list is a list of members | "Does a protect budget protect heads or rupees?" |
| Escalated, item 13 | They pick c, the same rupees per call, after getting the Rs 60,300 right | "Divide each group's rupees by its members." |
| Escalated, marker 7 | They pick `date_trunc('week', ...)`, option a, the habit from the morning | "Which Monday does 1 July fall under, and is that Monday in plan_line?" |
| Escalated, marker 8 | They pick to date against to date, option a | "Is the question how the quarter stands, or how each week ran on its own?" |
| Escalated, item 14 | They pick the row for the week of 7 September, option a, Rs 8,19,30,010 | "On which day does that row stop?" |
| Escalated, marker 9 | They pick b, both numbers right and the run rate left out | "Which weeks made the lead, and how have the weeks since 10 August run?" |
| Escalated, marker 10 | They pick a, exactly fifty, because fifty is what Marketing asked for | "Did the head of Retail-Plus ask for exactly fifty?" |
| Escalated, item 15 | They pick b, counting plan weeks | "Did the plan-first build lose a plan week, or orders?" |
| Problem 1, item 2 | They write DENSE_RANK as 1, 2, 2, 4 and carry RANK's numbering over | "Count the different amounts from the top, and nothing else." |
| Problem 1, item 3 | They give DENSE_RANK four at a top four, since a top four ships four | "What is DENSE_RANK's largest number for these seven?" |
| Problem 2, item 4 | They mark ask 4 as GROUP BY, picturing months as columns, or ask 5 as GROUP BY | "How many rows does the answer have: one per group, or one per row you started with?" |
| Problem 2, item 5 | They pick the six glued queries because they return the right 18 rows | "How many times does each build read the orders, and what happens when a seventh city opens?" |
| Problem 3, item 6 | They answer five, the ROW_NUMBER habit | "Did V-08 spend less than V-05?" |
| Problem 3, item 7 | They pick V-04 because that member is off the list | "Is V-04's fall real in calendar months, and is being on the list the same question?" |
| Problem 3, item 8 | They take the hurried flag's three | "Which months did LAG read for V-02?" |
| Problem 3, item 9 | They pick a, the figures after the fix | "What does a running total give two rows that share the ORDER BY value?" |
| Problem 3, item 10 | They count figures, option a | "Are you counting members or amounts?" |

## How does the debrief run, and what does the TA say about each plant?

Take the wrong letters in this order, each with a learner who chose it saying why before anyone
corrects it.

1. **Who chose option a on item 7 and option a on item 9?** The plan-first build closes at Rs 9,68,60,180 and
   reports Q2 Rs 15,39,810 short of plan. Set beside Monday's Rs 9,84,00,000 it is Rs 15,39,820 short of
   the quarter itself: the 25 orders of 1 to 5 July fall under Monday 29 June, which `plan_line` does not
   have. Item 15's check catches it in one row.
2. **Who chose option c on item 3 with option a on item 4?** Together they flag 9, the right count, from a window
   that runs across members; the check cell reports 300 rows that cross, one at every boundary between
   the 301 members, which is why the right count did not prove the window right.
3. **Who chose option a on item 2?** The customer id inside the ORDER BY turns RANK into ROW_NUMBER. In Retail-Plus
   that keeps C-0185 and drops C-0242, the planted pair below, by id alone.
4. **What Retail-Plus count did each learner's own run give?** Read two or three learners' sentences
   aloud before saying anything. Then name the plant: C-0185 and C-0242 both booked Rs 3,350 and tie at
   fiftieth, so RANK ships 51. DENSE_RANK ships 52, because a natural tie at 48th, C-0189 and C-0206 on
   Rs 3,480, and the tie at fiftieth each save it a number, so its 50 lands on the 52nd member, C-0259
   on Rs 3,200. Whole ties only ships 49 and drops both members on Rs 3,350, the forty-nine the head
   refused. ROW_NUMBER ships 50 and keeps C-0185 on the lower id. The RANK lists hold 156 members in
   all, so item 11's calls carried to next week are 6, Retail-Plus's 51 less 45. Retail-Plus's list
   carries Rs 3,56,780 of Rs 4,13,380 under RANK, 86.3 percent, against Rs 3,53,430, 85.5 percent, under
   ROW_NUMBER. C-0185 is also one of the seven members whose flag stepped over an empty month (April
   Rs 3,880, May Rs 6,990, June Rs 2,690, July Rs 1,900, no August, September Rs 1,450). Say this only
   if a learner notices it: the member at Retail-Plus's line is also one of the flags the calendar
   check removes.
   If nobody found the tie: "Change the segment to Retail-Plus and count what each rule ships. Do the
   four numbers agree?"
5. **Which nine members does Marketing ring first?** Ask the room to list the nine with their segment
   before naming anything. Three are the planted Retail-Plus fall: C-0161 (July Rs 4,200, August
   Rs 3,100, September Rs 1,900), C-0175 (Rs 4,400, Rs 2,900, Rs 1,600) and C-0171 (Rs 3,800, Rs 2,600,
   Rs 1,400), at places 12, 13 and 16 on Retail-Plus's list. The other six are C-0293, C-0276 and
   C-0288 of Business, at places 4, 6 and 14, and C-0010, C-0049 and C-0030 of Retail-Core, at places 1,
   12 and 16. The seven flags the calendar check removes are C-0282, C-0271 and C-0281 of Business,
   C-0060 and C-0054 of Retail-Core, and C-0216 and C-0185 of Retail-Plus. If nobody notices the
   Retail-Plus three: "Which segment carries three of the nine, and what did those three do in each
   month of Q2?" Those three are the Retail-Plus frequency fall the marketing lead raised at the start
   of the day, and all three are on the call list.
6. **Who chose option a on item 8, and where did item 9's July week come from?** To date and the run rate answer different questions,
   and Meera needs both. If a learner asks where the July week's money came from, send the room to sort
   that week's orders by amount and let them find it: KR-00667, one Business order of Rs 1,98,57,600 on
   13 July 2026, from C-0286, whose Q2 total is Rs 2,08,64,600. Without it the week of 13 July booked
   Rs 67,71,320, below its Rs 75,69,230, and Q2 would have stood Rs 41,05,620 behind plan at
   mid-quarter, so that one order carries the whole mid-quarter lead. Do not name it before somebody
   has sorted.

## Which interview questions does the drill ask, and in what order?

In pairs, sixty seconds an answer, the partner asking one follow-up. The answers are in each chapter
notebook's "In the interview" section and in the day sheet; the drill asks the questions only, the
[D] questions last.

1. [S] What do RANK, DENSE_RANK and ROW_NUMBER give on a tie?
2. [S] Top three per group: GROUP BY or a window, and why?
3. [S] What is the difference between GROUP BY and a window function?
4. [F] Marketing asks for the top fifty customers; your list has fifty rows but only twenty-eight
   names. What happened, and what is your check?
5. [F] Why can a window function not sit inside WHERE, and what do you do instead?
6. [F] Your top-ten list came back with eleven rows. What do you tell the stakeholder, and is it a bug?
7. [F] How would you find customers whose spend fell two months in a row?
8. [F] LAG returned a value for a customer's very first month. What went wrong, and how do you check
   for it in ten thousand rows?
9. [F] What makes a running total deterministic, and how would you notice one that was not?
10. [F] A dashboard says revenue to date is nine times the plan by week seven. What is the likely
    mistake?
11. [D] The business says "ties rank the same"; which function, and how many rows might the top-N
    report ship?
12. [D] A member says they were on holiday in August and should not be flagged. How does your definition
    treat a month with no orders, and why not fill it with zero?
13. [D] Your running total closes below the quarter's total. What do you check first?

## What does a finished lab look like?

Nine letters for the escalated case's parts 3 to 5, ten for the practice set, and a problem 3 file
that passes four checks in this order: the list's count names the rule that made it, the flag carries
the months LAG read, the calls are the overlap of the list and the checked flag, and the running
total's last row equals a sum counted without it, Rs 51,500. Read two files aloud with their authors
before the lab closes, one that passes all four and one that misses a check, with its author's
consent.

## What if the warehouse will not connect?

Pair the learner with a neighbour whose connection works. The escalated case's solution notebook opens
read-only on GitHub with every output showing; problems 1 and 2 can be answered on paper from the
tables printed in the set; problem 3 runs on a `VALUES` list, so any working Postgres session will do,
and it can be worked by hand. The support TA handles environment problems, so the lab TA keeps the room
moving.

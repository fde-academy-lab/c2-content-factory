# How does the TA run Monday's practice lab, what goes first when time is short, and where will learners stall?

**TRAINER ONLY.** For the TA who runs the practice lab after the day, from
`exercises/practice/C2_W02_D01_lab_STUDENT.md`, with the escalated case's parts 3 to 5
(`exercises/unguided/C2_W02_D01_escalated_case_STUDENT.md` and
`notebooks/C2_W02_D01_ex1_escalated_case_STUDENT.ipynb`) and the interview drill around it.

**Who needs the answer.** The TA needs it. The afternoon gives two hours to the IITGN faculty block
(tentative), so the trainer's part ran short, and the lab must leave every learner with the escalated
case finished, their wrong answers heard once aloud, the day's habits run on a new question, and the
interview questions said out loud. A lab that spends its time on the morning's items again sends the
room home without the returns suite and the drill, the two parts nothing else in the day repeats.

**The questions on the way.**

- How does the lab's time run, and who works alone?
- What goes first when the lab runs short?
- Where do learners stall, and what is the one hint for each?
- Which interview questions does the drill ask, and in what order?
- What does a finished lab look like?
- What if the warehouse will not connect?

Keys: the escalated case, `1b 2c 3a 4d 5a 6c 7d 8b 9b 10a 11d 12c 13b 14d 15a`, of which parts 3 to 5
are items 6, 7 and 13, then 8 and 14, then 9, 10 and 15; the practice set, `bdcaadbcdab` for items 1 to
11. The reasons for every letter are in `exercises/solutions/C2_W02_D01_escalated_case_solution_STUDENT.md`
and `exercises/solutions/C2_W02_D01_lab_solution_STUDENT.md`; the executed notebook is
`exercises/solutions/C2_W02_D01_ex1_escalated_case_solution_STUDENT.ipynb`.

## How does the lab's time run, and who works alone?

The lab's own length is set for the day; its work comes to about 110 minutes, in this order.

| Part | Minutes | Alone or pairs | What it does |
|---|---|---|---|
| 1. The escalated case, parts 3 to 5 | 25 | Alone | Markers 6 to 10 in the notebook and the brief's items 13 to 15: spend per member on delivered orders, the half-year, the sample and its fingerprint |
| 2. The debrief of wrong answers | 10 | Whole room | The room's most common wrong letters from all five parts, read aloud with the check that catches each |
| 3. The practice set | 60 | Alone for problems 1 and 2, pairs for problem 3 | Four row counts predicted (10), five clauses put in running order, one placement defended and four requests matched to the piece that answers each (10), and a returns suite for the head of customer service (40) |
| 4. The interview drill aloud | 15 | Pairs | Sixty seconds an answer, the partner timing and asking the follow-up, the design question last |

Learners who finish the set early take the stretch: the chapter sets' items not run live, items 3
onward of each set in `exercises/unguided/`, chapters 4 to 6 first. Whatever is left is tonight's work
beside the take-home and the second case.

For the debrief, take the wrong letters in this order, each with the learner who chose it saying why
before anyone corrects it: item 5, option b (thin by orders, which leaves Business Q2 unflagged);
item 13, option a (the morning's story carried onto delivered orders); item 2, option a (298
"customers" who are rows); item 15, option c (a route that avoids the filter and still agrees with
the fault, because it writes down the same wrong definition).

## What goes first when the lab runs short?

Cut in this order, and stop as soon as the lab fits.

1. The stretch goes home whole.
2. Problem 1 shrinks to items 2 and 4, the HAVING bar and the half-year list, which carry the two
   predictions the room most often gets wrong.
3. The drill shrinks to four questions: the logical order, WHERE against HAVING, LIMIT without ORDER BY,
   and the design question.
4. Problem 3 keeps the suite, the tie-out (item 9) and the sample (item 11); items 8 and 10 go home.
5. The escalated case's parts 3 to 5 and the debrief stay whole, because the case is the one place the
   learner runs the whole day alone.

## Where do learners stall, and what is the one hint for each?

| Part | Where they stall | The one hint |
|---|---|---|
| Escalated, marker 6 | They pick `avg(q2_spend)` because it reads as the average | "Who is inside Q2's average, and who is inside Q1's? Count them before you choose." |
| Escalated, item 13 | They keep the morning's line that frequency led the fall | "Of the three delivered ratios, which is smallest?" |
| Escalated, marker 8 | They predict 56, adding the two quarter counts because orders and rupees added | "Can one customer sit in both quarter rows?" |
| Escalated, item 15 | They choose the book less the cancelled rupees, which never touches the filter | "Which statuses does that route leave in, and what does it print against the faulty Rs 17,26,46,250?" |
| Problem 1, item 3 | They count half-year orders and answer 3 | "Which rows reach the groups at all?" |
| Problem 1, item 4 | They add 244 and 227 | "Can one customer appear in both quarters' lists?" |
| Problem 2, item 6 | They say HAVING waits for SELECT's names | "Which clause runs last, and so which clause can use the names SELECT gives?" |
| Problem 3, the suite | They write `count(*) AS customers` in `per_channel` | "Read the column's name aloud, then say what the function counts." |
| Problem 2, item 7 | They swap WHERE and HAVING in the match | "Which request tests one order, and which tests a count?" |
| Problem 3, item 9 | They expect the customer column to tie out as well | "Can a customer return one order through the app and another through the web?" |
| Problem 3, item 10 | They add the quarter rows, 78 and 76, for the half-year | "Which history group sits in both quarter rows?" |
| Problem 3, item 11 | They sample with `LIMIT 5` alone because it ran once and looked fine | "Would the analyst's rerun tomorrow draw the same five, and what makes it certain?" |

## Which interview questions does the drill ask, and in what order?

In pairs, sixty seconds an answer, the partner asking one follow-up, from the afternoon deck's D18
and D18a. The answers are in the study notes and in the day sheet; the drill asks the questions only.

1. [S] Explain the logical order in which a SQL query runs.
2. [S] WHERE against HAVING, one sentence each.
3. [F] What do `count(*)`, `count(customer_id)` and `count(DISTINCT customer_id)` each count?
4. [F] Why would you compute a KPI in the warehouse rather than in a notebook?
5. [F] Your total matches last week's; is your analysis the same?
6. [F] Orders per customer reads 1 for a segment; what do you check first?
7. [F] An average moved but the total did not, or moved differently; how?
8. [F] When would you use a CTE instead of a subquery?
9. [F] Why can you not add two quarters' customer counts to get the half-year's?
10. [F] What does LIMIT without ORDER BY return?
11. [F] Your KPI moved 30 percent overnight and the data did not change; what do you suspect?
12. [D] Two analysts report different customer counts for one quarter; how do you settle it?
13. [D] An analyst must audit your query: what changes in how you write it, and what would you
    refuse to compute in a notebook?
14. The design question, last: four ways to produce one of today's numbers; which would you choose,
    sized how, and what would make you switch?

## What does a finished lab look like?

Eight letters for the escalated case's parts 3 to 5, eleven for the practice set, and a returns suite
that passes four checks in this order: the definition sits in one place, the customer counts are
distinct counts named for what they count, the channel rows tie out on orders and rupees with a note
on customers, and the sample is ordered on the order id beside the returned book's fingerprint. Read
two suites aloud with their authors before the lab closes, one that passes all four and one that
misses a check, with its author's consent.

## What if the warehouse will not connect?

Pair the learner with a neighbour whose connection works. The escalated case's solution notebook opens
read-only on GitHub with every output showing, problems 1 and 2 can be predicted on paper with the
table printed in the set, and only the running of problem 3 needs the warehouse. The support TA handles
environment problems, so the lab TA keeps the room moving.

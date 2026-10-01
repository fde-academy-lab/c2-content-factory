# How does the TA run Thursday's practice lab, what goes first when time is short, and where will learners stall?

**TRAINER ONLY.** For the TA who runs the practice lab after the afternoon block, from
`exercises/practice/C2_W02_D04_lab_STUDENT.md`, with the chapter sets in `exercises/unguided/` as its
stretch.

**Who needs the answer.** The TA, who has the room for about an hour after a full day and must leave
every learner having predicted a shape before running it, given five asks an owner, and built two
small tables on their own. A lab that spends its hour on the chapter items the afternoon already
tested sends the room home without problems 3 and 4, the only places the lab asks for a table built
from nothing.

**The questions on the way.**

- How long does each part run, and who works alone?
- What goes first when the lab runs short?
- Where do learners stall, and what is the one hint for each?
- What does a finished lab look like?
- What if the notebook will not run?

Keys: problems 1 and 2, `cadbacbda`; the stretch items are keyed in each chapter set's solution file.
Reasons for every letter, and the numbers problems 3 and 4 should reach, are in
`exercises/solutions/C2_W02_D04_lab_solution_STUDENT.md`.

## How long does each part run, and who works alone?

The four problems are the core, about 60 minutes. The chapter sets' remaining 18 items, items 3 to 5
of each set, are the stretch: about 20 minutes for whoever finishes the core early, chapters 4 to 6
first, and tonight's work for everything left.

| Part | Minutes | Alone or pairs | What it tests |
|---|---|---|---|
| 1. Four shapes | 10 | Alone | That the keys decide a result's rows, in four new calls |
| 2. Five owners | 10 | Alone | Who reruns a number decides its tool, in five new asks |
| 3. The most-used channel | 20 | Pairs | A pivot with its `aggfunc` said, a validated merge from the list, and a column that guesses on ties and empty rows |
| 4. The head of Retail-Plus's table | 20 | Pairs | The whole day on one segment: the list as the rows, two quarters as columns, the feed by the rule, the as-of date, three checks and one honest line |
| The core | 60 | | |
| Stretch: the chapter sets' items 3 to 5, 18 in all | About 20, for early finishers; the rest goes home | Alone | The day's six chapters on new numbers, answered in chat as one letter line per set |

## What goes first when the lab runs short?

Cut in this order, and stop as soon as the lab fits.

1. The stretch goes home whole as tonight's work.
2. Problem 2 shrinks to items 5, 7 and 9, the three with the clearest rerunner.
3. Problem 1 shrinks to items 2 and 4, the two whose answer is not the customer list.
4. Problems 3 and 4 stay whole, because they are the only places the lab asks for a table built from
   nothing.

## Where do learners stall, and what is the one hint for each?

| Part | Where they stall | The one hint |
|---|---|---|
| 1 | Item 2: learners multiply 301 by 2, because "customer and quarter" sounds like every pair | "Does a group exist for a customer who never ordered in Q2?" |
| 2 | Item 6: some build a SQL view for a question asked once in a meeting | "Who will rerun this number next week?" |
| 3 | Step 2: the merge from the list leaves the 39 customers' channel counts missing, and `idxmax` stops with `ValueError: Encountered all NA values` | "What count does a customer with no orders have in each channel? Say it in code before `idxmax` runs." |
| 3 | Step 5: nobody expects `idxmax` to answer for a row of zeros | "Run it on one customer who never ordered and read what it returns." |
| 4 | Step 1: the feed's merge raises `MergeError` | "The feed broke its promise. Which of the growth team's rules handles a customer it names twice?" |
| 4 | Step 3: pairs give 33 of 60 against 34 of 60 | "Could a member who bought nothing in Q1 spend less in Q2? Count each group out of the members who could." |
| 4 | The line: pairs write that the sale made reached members spend less, or more | "Does the table say why anyone spent less? Put the two counts side by side, each with its base, and say only what they show." |
| Stretch | The design items: learners pick the most thorough-sounding option and miss the fact in the stem | "What does the stem say about who reruns it, or how big it is? Cross out every option that ignores it." |

## What does a finished lab look like?

Nine letters for problems 1 and 2; for problem 3, the counts 340, 1,000, 98, 39 and 137 and a tie
rule in one sentence; for problem 4, 120 rows, Rs 9,99,150, 60 reached, 33 of the 44 reached members
who bought in Q1 against 34 of the 47 others, a smallest recency of 0, and one line that names both
groups with their bases and claims no cause. A pair that reports 33 of 60 against 34 of 60 has
counted 29 members who bought nothing in Q1, 13 who never ordered and 16 who ordered only in Q2, none
of whom can spend less, and on that base the comparison points the other way. Read two pairs' lines
aloud before the lab closes and ask the room which one Kavya would send back.

## What if the notebook will not run?

Problems 3 and 4 need the helper, the warehouse and the feed file in `data/`. If a learner's
Codespace cannot reach the warehouse, run `bash .devcontainer/load_warehouse.sh` once; if it still
fails, pair them with a neighbour whose notebook runs, since problems 1 and 2 and the stretch need no
notebook at all.

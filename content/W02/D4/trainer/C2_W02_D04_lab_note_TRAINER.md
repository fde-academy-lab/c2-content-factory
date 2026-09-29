# TA note: the practice lab, Week 2 Thursday

**TRAINER ONLY.** For the TA running `exercises/practice/C2_W02_D04_lab_STUDENT.md` after the
second block. About an hour. Release `exercises/solutions/C2_W02_D04_lab_solution_STUDENT.md` in
the last ten minutes, after every learner has posted their letters.

## The run of the hour

| Problem | Minutes | Keys or numbers | Where learners stall | The one hint to give |
|---|---|---|---|---|
| 1. Predict the shape | 15 | 1c 2a 3d 4b | Item 2: learners multiply 301 by 2 and answer 602 | "Does every customer who ordered have an order in both quarters?" |
| 2. Pick the tool | 10 | 5a 6c 7b 8d 9a | Item 7: learners pick pandas because it is the day's tool | "Who is the reader, and what do they need to see?" |
| 3. Channel preference | 15 | 340 rows; 39 with no orders; app 149, store 92, web 60; 98 ties | `idxmax` raises `ValueError: Encountered all NA values` on the 39 rows the merge left empty (two minutes, then move on); then almost nobody asks about ties | "For how many customers is the largest count shared by two channels?" |
| 4. The Q2 table | 20 | 340 rows; Rs 9,84,00,000; as of 28 September; smallest recency 0; 113 with no Q2 order; 109 on a 30-day list, 180 from 19 October | Filtering to Q2 before the groupby and then forgetting to merge onto the customer list, which gives 227 rows | "How many customers does Marketing's table promise?" |

## What to listen for

- In problem 3, the tie rule said aloud. Any rule is acceptable if it is written down; the point is
  that `idxmax` decides by column order when nobody else does.
- In problem 4, the sentence about the 113 customers with no Q2 order: they are exactly who a
  win-back is for, and a Q2-only table cannot see them. A learner who says that has understood why
  the escalated case used both quarters.

## If the warehouse is down

`bash .devcontainer/load_warehouse.sh` rebuilds it in a minute. If a learner's Codespace cannot
reach Postgres at all, problems 1, 2 and 4 run on the take-home snapshot's CSVs with different
numbers; tell them so, and check their answers against the solution's reasoning rather than its
counts.

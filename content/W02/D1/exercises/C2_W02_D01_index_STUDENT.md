# Can the warehouse itself give Anand the Monday numbers, every segment, every week?

> "I want these numbers every Monday, for every segment and channel, computed from the warehouse
> itself. No notebooks, no exports, nothing a person can mistype. Our data team will give you read
> access to Postgres."
>
> Anand Iyer, finance controller, Kalpa Retail

Every exercise today puts Anand Iyer's ask back to you, or a question one of its answers raised. Anand
is Kalpa Retail's finance controller, the warehouse is Kalpa's Postgres database, and the book is its
two quarters of orders, Q1 (April to June 2026) and Q2 (July to September 2026). The day climbs one
case in six chapters, and each chapter has a short set of its own: items 1 and 2 run live in the
chapter's last minutes if the chapter ran to time, and the rest are the practice lab's stretch or
tonight's work. Every stem is a question a Kalpa stakeholder or Kavya Nair, the team's senior analyst,
would ask, and more than a third of the day's items ask you to design the analysis before you judge
one: the best-fit way with its size, the fact that would switch it, or a second route to the same
number.

**Who needs the answer.** You do, when you plan your day. Each file below answers one rung of Anand's
ask, and a rung skipped is a line of Monday's sheet you will build without having practised it.

**The questions on the way.**

- Which six questions does the day climb?
- Which file asks which question, and when do you take it?
- Where are the answers, and when are they released?
- What shape does every post take?

## Which six questions does the day climb?

| Chapter | The question it asks |
|---|---|
| 1 | How many orders, rupees and customers did each quarter book, counted where the book lives? |
| 2 | Does the warehouse tell the same story as the file that Meera Raghavan, Kalpa Retail's CEO, rested her decision on? |
| 3 | Which segment carried the fall from Q1 to Q2, and how often did its customers order? |
| 4 | Which branch of each segment's tree moved, and how much less did each Retail-Plus member spend? |
| 5 | Do the suite's numbers add up the way Anand's analyst will add them? |
| 6 | Will next Monday's run give Anand's analyst the same answer from the same book? |

## Which file asks which question, and when do you take it?

| When | File | The question it asks | Items | Solution |
|---|---|---|---|---|
| Chapters 1 and 3, with the trainer | `guided/C2_W02_D01_first_aggregate_STUDENT.md` | How many orders, customers and rupees did each segment book in each quarter, built one clause at a time? | Five letters; none is a design item, since the trainer chooses every step | `solutions/C2_W02_D01_first_aggregate_solution_STUDENT.md` |
| After chapter 1 | `unguided/C2_W02_D01_ch1_what_the_book_says_STUDENT.md` | How many orders, rupees and customers did each quarter book, counted where the book lives? | Five letters; items 1, 2 and 5 are design | `solutions/C2_W02_D01_ch1_what_the_book_says_solution_STUDENT.md` |
| After chapter 2 | `unguided/C2_W02_D01_ch2_same_story_as_week1_STUDENT.md` | Does the warehouse tell the same story as the file Meera's decision rested on? | Five letters; items 1, 2 and 5 are design | `solutions/C2_W02_D01_ch2_same_story_as_week1_solution_STUDENT.md` |
| After chapter 3 | `unguided/C2_W02_D01_ch3_which_segment_moved_STUDENT.md` | Which segment carried the fall from Q1 to Q2, and how often did its customers order? | Five letters; items 1 and 4 are design | `solutions/C2_W02_D01_ch3_which_segment_moved_solution_STUDENT.md` |
| After chapter 4 | `unguided/C2_W02_D01_ch4_which_branch_moved_STUDENT.md` | Which branch of each segment's tree moved, and how much less did each Retail-Plus member spend? | Six letters; items 1, 2 and 6 are design | `solutions/C2_W02_D01_ch4_which_branch_moved_solution_STUDENT.md` |
| After chapter 5 | `unguided/C2_W02_D01_ch5_does_the_suite_add_up_STUDENT.md` | Do the suite's numbers add up the way Anand's analyst will add them? | Five letters; items 1, 2 and 5 are design | `solutions/C2_W02_D01_ch5_does_the_suite_add_up_solution_STUDENT.md` |
| After chapter 6 | `unguided/C2_W02_D01_ch6_same_answer_next_week_STUDENT.md` | Will next Monday's run give Anand's analyst the same answer from the same book? | Six letters; items 1, 2 and 5 are design | `solutions/C2_W02_D01_ch6_same_answer_next_week_solution_STUDENT.md` |
| The escalated case, alone: parts 1 and 2 in the afternoon, 20 minutes, and parts 3 to 5 in the practice lab | `unguided/C2_W02_D01_escalated_case_STUDENT.md` with `../notebooks/C2_W02_D01_ex1_escalated_case_STUDENT.ipynb` | Does the Monday suite hold on Finance's definition of revenue? | Fifteen letters, the notebook's ten markers and five of the brief's own; items 11, 12, 14 and 15 are design | `solutions/C2_W02_D01_escalated_case_solution_STUDENT.md` and the executed `solutions/C2_W02_D01_ex1_escalated_case_solution_STUDENT.ipynb` |
| The TA-led practice lab, after the day | `practice/C2_W02_D01_lab_STUDENT.md` | Can you run the day's checks on a new question in an hour: four row counts, one running order and one short suite? | Eleven letters and a returns suite; item 10 is design, and the suite is the design work | `solutions/C2_W02_D01_lab_solution_STUDENT.md` |
| The take-home, in pairs or alone, about forty minutes | `unguided/C2_W02_D01_second_case_STUDENT.md` with `../notebooks/C2_W02_D01_ex2_second_case_STUDENT.ipynb` | Is the store booming and the web collapsing, as Marketing says? | Ten letters, the notebook's seven markers and three of the brief's own, and one line for Anand; items 7 to 10 are design | `solutions/C2_W02_D01_second_case_solution_STUDENT.md` and the executed `solutions/C2_W02_D01_ex2_second_case_solution_STUDENT.ipynb` |
| Tonight | `../takehome/C2_W02_D01_brief_STUDENT.md` | What does Kalpa Retail East's first Monday suite say, and does every number on it hold up? Kalpa Retail East is a region invented for the take-home, with a book of its own | A suite of your own, with the checks that prove it | `../takehome/C2_W02_D01_selfcheck_STUDENT.md`, opened once each part is done |

The practice lab also runs the debrief of the room's wrong answers from the escalated case and the
interview drill aloud; the lab set's first line says so.

## Where are the answers, and when are they released?

Every solution is in `solutions/`. The chapter sets' solutions open at the end of the practice lab,
the escalated case's after the lab's debrief, the lab's own when the lab ends, and the second case's
once the take-home is in. Each opens on an answer line and gives, item by item, the question,
the key with why it holds, why each other letter fails and whether the item is a design item, so it
reads with nothing else open.

## What shape does every post take?

Every letter line uses one shape: the letters in item order, no spaces, pasted as one line where the
trainer asks for it when the exercise opens. The chapter sets take five or six letters, the guided
build five, the lab eleven, the second case ten and the escalated case fifteen.

```
Post exactly this shape: xxxxxx
```

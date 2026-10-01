# Which members should Marketing protect before they drift, and is Q2 on track against the plan line?

> "Retail-Plus frequency is the problem, so we want to protect our best members before they drift.
> Give us the top fifty customers by Q2 revenue in each segment, and flag anyone whose monthly spend
> has fallen for two months running. And Meera wants to see revenue accumulate week by week against
> the plan line, so we know by mid-quarter whether we are on track."
>
> The marketing lead, Kalpa Retail

Every exercise today puts the marketing lead's ask back to you, or a question one of its answers
raised. The marketing lead owns acquisition and campaigns at Kalpa Retail, the head of Retail-Plus owns
the paid membership tier and has asked that members who spent the same be ranked the same, and Meera
Raghavan, the CEO, wants Q2 (July to September 2026) read against the plan line. The warehouse is
Kalpa's Postgres database. The day climbs one case in six chapters, and each chapter has a short set of
its own: two of its items run live in the chapter's last minutes if the chapter ran to time, items 2
and 3 in chapter 1 and items 1 and 2 in every other chapter, and the rest are the practice lab's
stretch or tonight's work. Every stem is a question a Kalpa stakeholder or Kavya
Nair, the team's senior analyst, would ask, and more than a third of the day's items ask you to design
the analysis before you judge one: the best-fit way with its size, the fact that would switch it, or a
second route to the same number.

**Who needs the answer.** You need it to plan your day, since each file below answers one rung of the
marketing lead's ask, and a rung you skip is a part of Monday's call list you will build without
having practised it.

**The questions on the way.**

- Which six questions does the day climb?
- Which file asks which question, and when do you take it?
- How many items does the day hold, and how many of them are design items?
- Where are the answers, and when are they released?
- What shape does every post take?

## Which six questions does the day climb?

| Chapter | The question it asks |
|---|---|
| 1 | Which fifty members spent the most in Q2? |
| 2 | Which fifty members lead each of the four segments? |
| 3 | When two members tie at fiftieth place, how many does a list ship, and which rule did the head of Retail-Plus ask for? |
| 4 | Whose monthly spend fell two months running? |
| 5 | Has Q2 revenue kept pace with the plan line week by week, and where did it stand at mid-quarter? |
| 6 | Which listed members does Marketing call first, and does each flag hold up when a member says they were on holiday? |

## Which file asks which question, and when do you take it?

| When | File | The question it asks | Items | Solution |
|---|---|---|---|---|
| Items 2 and 3 live in chapter 1's last minutes; items 1, 4 and 5 in the practice lab or tonight | `unguided/C2_W02_D03_ch1_top_fifty_STUDENT.md` | Which fifty members spent the most in Q2? | Five letters; items 1, 4 and 5 are design | `solutions/C2_W02_D03_ch1_top_fifty_solution_STUDENT.md` |
| Items 1 and 2 live in chapter 2's last minutes; items 3 to 5 in the practice lab or tonight | `unguided/C2_W02_D03_ch2_each_segment_STUDENT.md` | Which fifty members lead each of the four segments? | Five letters; items 1, 4 and 5 are design | `solutions/C2_W02_D03_ch2_each_segment_solution_STUDENT.md` |
| Chapter 3, with the trainer, about fifteen minutes | `guided/C2_W02_D03_tie_STUDENT.md` | How do ROW_NUMBER, RANK and DENSE_RANK treat a tie, and what does the head of Retail-Plus's rule ship for Retail-Core? | Five letters; none is a design item, since the trainer chooses every step | `solutions/C2_W02_D03_tie_solution_STUDENT.md` |
| Items 1 and 2 live in chapter 3's last minutes; items 3 to 5 in the practice lab or tonight | `unguided/C2_W02_D03_ch3_tie_rule_STUDENT.md` | When two members tie at fiftieth place, how many does a list ship, and which rule did the head of Retail-Plus ask for? | Five letters; items 4 and 5 are design | `solutions/C2_W02_D03_ch3_tie_rule_solution_STUDENT.md` |
| Items 1 and 2 live in chapter 4's last minutes; items 3 to 5 in the practice lab or tonight | `unguided/C2_W02_D03_ch4_falling_spend_STUDENT.md` | Whose monthly spend fell two months running? | Five letters; items 1, 4 and 5 are design | `solutions/C2_W02_D03_ch4_falling_spend_solution_STUDENT.md` |
| Items 1 and 2 live in chapter 5's last minutes; items 3 to 5 in the practice lab or tonight | `unguided/C2_W02_D03_ch5_against_plan_STUDENT.md` | Has Q2 revenue kept pace with the plan line week by week, and where did it stand at mid-quarter? | Five letters; items 1 and 5 are design | `solutions/C2_W02_D03_ch5_against_plan_solution_STUDENT.md` |
| Items 1 and 2 live in chapter 6's last minutes; items 3 to 5 in the practice lab or tonight | `unguided/C2_W02_D03_ch6_call_first_STUDENT.md` | Which listed members does Marketing call first, and does each flag hold up when a member says they were on holiday? | Five letters; items 1, 4 and 5 are design | `solutions/C2_W02_D03_ch6_call_first_solution_STUDENT.md` |
| The escalated case, alone: parts 1 and 2 in the afternoon, 20 minutes, and parts 3 to 5 in the practice lab | `unguided/C2_W02_D03_escalated_case_STUDENT.md` with `../notebooks/C2_W02_D03_ex1_escalated_case_STUDENT.ipynb` | What does Marketing get on Monday: each segment's list with its count, the members to ring first, the share of revenue the lists carry, and Q2 against plan? | Fifteen letters, the notebook's ten markers and five of the brief's own; items 11 to 15 are design | `solutions/C2_W02_D03_escalated_case_solution_STUDENT.md` and the executed `solutions/C2_W02_D03_ex1_escalated_case_solution_STUDENT.ipynb` |
| The TA-led practice lab, after the day | `practice/C2_W02_D03_lab_STUDENT.md` | Can you rank a tie, choose GROUP BY or a window, and run the whole day on eight invented members, in an hour? | Ten letters and the drill's queries; items 5 and 10 are design, and the drill's queries are its design work | `solutions/C2_W02_D03_lab_solution_STUDENT.md` |
| The take-home, in pairs or alone, about forty minutes | `unguided/C2_W02_D03_second_case_STUDENT.md` with `../notebooks/C2_W02_D03_ex2_second_case_STUDENT.ipynb` | Should Retail-Core's protect list rank members by how often they ordered in Q2, instead of by how much they spent? | Ten letters, the notebook's seven markers and three of the brief's own, and one line for the marketing lead; items 8 to 10 are design | `solutions/C2_W02_D03_second_case_solution_STUDENT.md` and the executed `solutions/C2_W02_D03_ex2_second_case_solution_STUDENT.ipynb` |
| Tonight | `../takehome/C2_W02_D03_brief_STUDENT.md` | The take-home brief, on a second sample of the warehouse | Queries of your own, with the checks that prove them | `../takehome/C2_W02_D03_selfcheck_STUDENT.md`, opened once each part is done |

The practice lab runs after the day, once the tentative IITGN block has finished, and it also hosts the
escalated case's parts 3 to 5, the debrief of the room's wrong answers and the interview drill aloud.

## How many items does the day hold, and how many of them are design items?

| File | Items | Design items |
|---|---|---|
| The six chapter sets | 30 | 16 |
| The guided build | 5 | 0 |
| The escalated case | 15 | 5 |
| The practice lab | 10 | 2 |
| The second case | 10 | 3 |
| The day | 70 | 26 |

Twenty-six of the day's seventy lettered items, a little over a third, are design items, and every
chapter set and both cases carry at least two of them.

## Where are the answers, and when are they released?

Every solution is in `solutions/`. The guided build's opens when chapter 3 ends, the chapter sets'
solutions open at the end of the practice lab, the escalated case's after the lab's debrief, the lab's
own when the lab ends, and the second case's once the take-home is in. Each opens on an answer line
and gives, item by item, the question, the key with why it holds, why each other letter fails and
whether the item is a design item, so it reads with nothing else open. Where a key rests on your own
Retail-Plus run, the solution says so and leaves the number to your run.

## What shape does every post take?

Every letter line uses one shape: the letters in item order, no spaces, pasted as one line. The chapter
sets and the guided build take five letters, the lab and the second case ten, and the escalated case
fifteen.

```
Post exactly this shape: xxxxx
```

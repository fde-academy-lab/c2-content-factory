# Which exercise follows each chapter on Thursday, and what question does each ask?

> "One table, one row per customer, refreshed every Monday: how recently each customer bought, how
> often, how much, their segment, whether the monsoon sale reached them, and the flags we act on.
> Marketing's analysts live in Python, so build it in pandas, from the warehouse, and make it refresh
> in one run."
>
> The growth team, with the data platform lead, Kalpa Retail

Every exercise today puts the growth team's ask back to you, or a question one of its answers raised.
Kalpa Retail's warehouse, its Postgres database, holds 1,000 orders from April to September 2026 and a
customer list of 340 customers; the campaign platform's feed lists the customers the monsoon sale
reached in August. The day climbs one case in six chapters, and each chapter has a short set of its
own: items 1 and 2 run live in the chapter's last three minutes, and the rest are the practice lab's
stretch or tonight's work. Every stem is a question a Kalpa stakeholder or Kavya Nair, the senior
analyst on the team, would ask, and about a third of the day's items ask you to design the analysis
before you judge one: the best-fit approach with a sizing, the fact that would switch it, or the
second route that confirms a number.

**Who needs the answer.** You, planning the day. Each file below answers one rung of the growth
team's ask, and a rung skipped is a column of Monday's table you will build without having practised
it.

**The questions on the way.**

- Which file asks which question, and when do you take it?
- What goes in the practice lab, and what is its stretch?
- Where are the answers, and when are they released?

## Which file asks which question, and when do you take it?

| When | File | The question it asks | Answer as |
|---|---|---|---|
| Chapter 1, with the trainer | `guided/C2_W02_D04_first_moves_STUDENT.md` | Does one line of pandas give the growth team the numbers Week 1's loop gave, for every customer on the list? | Your own notebook, mirrored line for line |
| After chapter 1 | `unguided/C2_W02_D04_ch1_customer_table_STUDENT.md` | How recently, how often and how much has each of Kalpa's 340 customers bought? | Five letters; items 1, 4 and 5 are design |
| After chapter 2 | `unguided/C2_W02_D04_ch2_exposure_STUDENT.md` | Which customers did the monsoon sale reach, and what did the reached customers spend? | Five letters; items 3 and 5 are design |
| After chapter 3 | `unguided/C2_W02_D04_ch3_months_STUDENT.md` | How far did Retail-Plus members' spend fall from Q1 to Q2, month by month? | Five letters; items 3 and 5 are design |
| After chapter 4 | `unguided/C2_W02_D04_ch4_three_tools_STUDENT.md` | Of the 130 customers the sale reached, how many bought, and do plain Python, SQL and pandas agree? | Five letters; items 3, 4 and 5 are design |
| After chapter 5 | `unguided/C2_W02_D04_ch5_tool_choice_STUDENT.md` | Which tool should own each of Marketing's and Finance's recurring numbers, and which would you refuse for Finance? | Five letters; items 1, 2, 4 and 5 are design |
| After chapter 6 | `unguided/C2_W02_D04_ch6_refresh_STUDENT.md` | Can the table rebuild itself every Monday and refuse to ship when something breaks? | Five letters; items 3 and 5 are design |
| The escalated case, alone, 50 minutes | `unguided/C2_W02_D04_escalated_case_STUDENT.md` with `notebooks/C2_W02_D04_ex1_escalated_case_STUDENT.ipynb` | Can you build the growth team's whole Monday table alone, with both flags, one view and a guarded run, and post four numbers that hold? | Thirteen letters and four numbers; items 5 and 13 are design |
| The second case, in pairs, 40 minutes | `unguided/C2_W02_D04_second_case_STUDENT.md` with `notebooks/C2_W02_D04_ex2_second_case_STUDENT.ipynb` | Did Retail-Plus members order less often in Q2, in plain Python, SQL and pandas, and which tool would you sign for each job? | Six letters and the tool-choice note; items 5 and 6 are design |
| The TA-led practice lab, after the afternoon block | `practice/C2_W02_D04_lab_STUDENT.md` | Can you predict four table shapes, give five asks an owner, name each customer's most-used channel and build the head of Retail-Plus's table, in an hour? | Nine letters, the numbers from problems 3 and 4, and two sentences |
| Tonight | `../takehome/C2_W02_D04_brief_STUDENT.md` | Can you build the Monday table on a staging snapshot you have not seen, and say what its feed did? | A notebook, the table as a CSV, and the self-check |
| Tonight, before you post | `../takehome/C2_W02_D04_selfcheck_STUDENT.md` | Does your take-home reach the numbers a careful pass on the staging snapshot reaches? | Your own numbers against its tables |

## What goes in the practice lab, and what is its stretch?

The lab's core is its four problems, about 60 minutes: problems 1 and 2 ten minutes each, problems 3
and 4 twenty each. Its stretch is the chapter sets' remaining 18 items, items 3 to 5 of each set, for
early finishers, chapters 4 to 6 first; whatever is left is tonight's work.

## Where are the answers, and when are they released?

Every solution is in `solutions/`. The six chapter sets' solutions open at the end of the practice
lab, the two case solutions after the debrief, with their executed notebooks, and the lab solution at
the end of the lab. Each opens on an answer line and gives, item by item, the question, the key with
why it holds and why each other letter fails.

| Solution | The question it answers |
|---|---|
| `solutions/C2_W02_D04_ch1_customer_table_solution_STUDENT.md` | Which answers hold in the chapter 1 set on building one row per customer, and why? |
| `solutions/C2_W02_D04_ch2_exposure_solution_STUDENT.md` | Which answers hold in the chapter 2 set on attaching the monsoon sale to the table, and why? |
| `solutions/C2_W02_D04_ch3_months_solution_STUDENT.md` | Which answers hold in the chapter 3 set on Retail-Plus's months, and why? |
| `solutions/C2_W02_D04_ch4_three_tools_solution_STUDENT.md` | Which answers hold in the chapter 4 set on one question asked in three tools, and why? |
| `solutions/C2_W02_D04_ch5_tool_choice_solution_STUDENT.md` | Which answers hold in the chapter 5 set on which tool owns which number, and why? |
| `solutions/C2_W02_D04_ch6_refresh_solution_STUDENT.md` | Which answers hold in the chapter 6 set on the Monday refresh, and why? |
| `solutions/C2_W02_D04_escalated_case_solution_STUDENT.md` | Which answers hold in the escalated case on building the whole Monday table alone, and why? |
| `solutions/C2_W02_D04_second_case_solution_STUDENT.md` | Which answers hold in the second case on one number in three tools and the note, and why? |
| `solutions/C2_W02_D04_lab_solution_STUDENT.md` | Which answers hold in the practice lab on the day's moves in new questions, and why? |

Every letter line uses one shape: the letters in item order, no spaces, pasted as one line; the
chapter sets take five letters each.

```
Post exactly this shape: xxxxx
```

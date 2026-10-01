# Did Retail-Plus members order less often in Q2, in plain Python, SQL and pandas, and which tool would you sign for each job?

The second case: forty minutes after the break, in pairs. Both partners write the query on paper
first; then one partner drives `notebooks/C2_W02_D04_ex2_second_case_STUDENT.ipynb`, six lettered
choices in four steps, while the other checks each step's numbers against the paper; you swap
drivers at step 3, and the pair writes the tool-choice note together.

> "You did the tree in plain Python in Week 1, in SQL on Monday. Do it a third way now, and tell me
> honestly which tool you would pick for which job, and which one you would refuse for Finance's
> numbers."
>
> Kavya Nair, senior analyst, Kalpa Retail data team

The question all three tools answer is the branch of Week 1's revenue tree that moved: **Retail-Plus
orders per member, Q1 against Q2**. Retail-Plus is Kalpa Retail's paid membership tier; Q1 is April
to June 2026 and Q2 is July to September. A member counts in a quarter if they ordered in it, and
orders per member is a quarter's orders divided by the members who ordered in that quarter, the
retail dossier's frequency. Kalpa's warehouse, its Postgres database, holds the orders and the
customer list, where every customer's segment is recorded.

Plain Python reads the rows and counts them one at a time, the way Week 1 did; SQL runs the count in
the warehouse; pandas reads the rows into a DataFrame and groups them. Anand Iyer, the finance
controller, has an analyst who reruns every number Finance receives, from the warehouse, every
Monday.

**Who needs the answer.** Kavya, who will not let the team quote a number until two tools that share
no code agree on it, and Anand Iyer, whose analyst must be able to rerun whatever the note gives
Finance. A note that picks a tool by habit or by speed puts Finance's number where Finance cannot
rerun it.

**The questions on the way.**

- Which query would the pair write on paper, before any tool opens?
- What does plain Python count, one row at a time?
- Does SQL, where the data lives, give the same number?
- Does pandas, the analyst's bench, give the same number?
- Which size tells the three routes apart, and which tool would the pair sign for each job?

## Part 1. Which query would the pair write on paper, before any tool opens?

Used at work whenever a number must be defined before it is computed, so that two people computing
it compute the same thing.

Six minutes, on paper, both partners. Write the SQL that returns, for each quarter, Retail-Plus's
orders, its members who ordered, and orders per member to three decimal places. Name the two tables
it reads and the column that keeps only Retail-Plus. Keep the paper beside the notebook.

## Part 2. What does plain Python count, one row at a time?

Used at work when a number has to be explained line by line to someone who distrusts it.

Six minutes, the notebook's marker 1: how many members ordered in each quarter, counted from the
lists of customer ids the loop collected.

## Part 3. Does SQL, where the data lives, give the same number?

Used at work whenever a number Finance reruns is defined.

Eight minutes, markers 2 and 3: the expression that gives orders per member to three places, and the
line that keeps only Retail-Plus. Compare the notebook's query with the pair's paper.

## Part 4. Does pandas, the analyst's bench, give the same number?

Used at work on every analyst's iterative question.

Six minutes, marker 4: the method that gives each quarter's members.

## Part 5. Which size tells the three routes apart, and which tool would the pair sign for each job?

Used at work in every tool-choice discussion, and in the design question of an analytics interview.

Fourteen minutes, markers 5 and 6, then the note: which size tells the three routes apart, where a
number Finance reruns every Monday should be computed, and the pair's tool-choice note.

The note has one line per tool, each naming the job the tool owns, the reason, and the rows that tool
fetched from the warehouse for today's two numbers, then one line naming the tool the pair would
refuse for Finance's numbers and why.

## Which rules does the pair keep?

- The three tools must agree to three decimal places before the note is written.
- Every line of the note carries a number: the rows a route fetched, or who reruns the number.
- The refusal names a tool and a reason a finance controller would accept.
- The support TA answers environment problems only.

## How does the pair post its six letters and its note?

One line of six letters in the order of the notebook's markers, then the note below it.

```
Post exactly this shape: xxxxxx
```

# The second case: one question, three tools, and the note to Kavya

Forty-five minutes, in pairs. The room tries the SQL version first; the trainer then runs it
through plain Python and pandas on the screen, and the pairs finish the notebook and the note.

> **The client's ask.** Kavya Nair, senior analyst: "You did the tree in plain Python in Week 1,
> in SQL on Monday. Do it a third way now, and tell me honestly which tool you would pick for
> which job. I will ask you which one you would refuse for Finance's numbers."

## The question every tool answers

Retail-Plus orders per member, Q1 against Q2. It is the node of Week 1's revenue tree that moved,
and on the full warehouse it has one right answer to three decimal places.

## What to do

1. **SQL first, before the notebook.** Write the query that returns, per quarter, the Retail-Plus
   orders, the members and orders per member to three places. Run it against the warehouse. If a
   quarter shows 2 or 1, you have met Monday's trap again; say which one.
2. **The notebook.** Open `notebooks/C2_W02_D04_three_tools_STUDENT.ipynb` and fill its five
   placeholders: the plain Python loop, the SQL statement, the pandas chain and the choice for
   Finance. Every check must pass.
3. **The agreement.** The three tools must agree on both quarters. If one does not, find the
   mistake in that tool before writing anything else; a disagreement is a trap, never noise.
4. **The five asks.** Answer `exercises/unguided/C2_W02_D04_pick_tool_STUDENT.md`, one line of
   reason per letter.
5. **The note to Kavya.** Write it in the format below.

## The note's format

Five sentences, no more:

1. The number, from all three tools, with its definition and period.
2. Plain Python: the job you would give it, with the reason naming who must trust the number.
3. SQL: the job you would give it, with the reason.
4. pandas: the job you would give it, with the reason.
5. The tool you would refuse for Finance's Monday number, and why, in one sentence Anand would
   accept.

## What a strong note shows

A reason per tool names a person and a risk: who reruns it, who audits it, who has to follow it
line by line, and what goes wrong when the number lives in the wrong place. A note that lists
features ("pandas is fast, SQL is scalable") answers a question nobody asked.

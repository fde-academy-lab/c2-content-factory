# Take-home: a tree you can watch, and a file nobody explained

> "By Thursday I want a recommendation on which branch we examine first, and I will ask why you did
> not pick the others."
> Meera Raghavan, CEO, Kalpa Retail

Three parts, about two hours in all. Part 1 is the day's thinking on a business nobody has written
about, and it is the part an interviewer will ask you to talk through. Part 2 is the day's method on
a second sample of Kalpa orders you have not seen. Part 3 is twenty minutes of reading with one
specific thing to cite. Tuesday opens by walking one learner's Part 1 in front of the room.

---

## Part 1. Build: the revenue tree for a business you know, about an hour

Pick a business you can stand in front of this week: the canteen, a kirana store near where you
live, or an app you use most days. A company you have only read about does not count.

- Draw its revenue tree on paper, with every branch in that business's own words. A canteen does
  not have "orders per customer"; it has how many times a week the same person eats there.
- Beside each branch, write the metric as a numerator over a denominator, with the window.
- Beside each branch, write what moving it would cost the owner in the owner's terms, such as "a
  board outside the gate" or "staying open an hour later", and never "marketing spend".
- Name the branch you believe moves most for that business, and defend it with a threshold: "I would
  open this branch first if at least N of every 10 regulars come fewer than M times a week", with
  your N and M, and say what you would open instead if the threshold failed.
- Name the one number you would have to ask the owner for, because you cannot see it from outside.

One page: the drawing, the table, and two sentences.

---

## Part 2. Extend: two tree nodes on a second sample, about forty minutes

A second sample of Kalpa Retail orders sits in `data/C2_W01_D01_takehome_STUDENT.py`. It has the same
fields as today's file and none of the same numbers, so nothing from class can be pasted across.

- Start a new notebook beside the day's notebooks, copy in the setup cell from chapter 1's notebook,
  and point the loader at `C2_W01_D01_takehome_STUDENT.py`.
- Compute two tree nodes, customers and orders per customer, on each of the three definitions of
  sales: booked, not cancelled and delivered. Write each as a numerator over a denominator in a
  markdown cell before the code cell that computes it.
- Compute the typical order on booked and on delivered orders, and say in one markdown line which
  average you chose and why.
- Write one sentence on what surprised you in this file, with the number that surprised you.

Two pieces of process evidence go in the same notebook. The first is the output of every check the
self-check lists, printed by your own cells. The second is a markdown cell headed "What stopped me",
with the last line of the first error you met, the cell that raised it, and the change you made.

Run the notebook from a fresh kernel, top to bottom, before you call it done. The self-check file,
`takehome/C2_W01_D01_selfcheck_STUDENT.md`, lists every number you should reach.

---

## Part 3. Read: the profitability framework, about twenty minutes

MConsultingPrep, the profitability framework: https://mconsultingprep.com/profitability-case-framework (verified 29 Sep 2026)

Read the revenue side of the framework. Then write two lines. The first cites one specific thing
from the page, with the heading it sits under, that today's tree also does or leaves out. The
second says whether that thing would change the tree you drew in Part 1, and how.

---

## What to bring on Tuesday

| Part | What to bring |
|---|---|
| 1 | The page: the tree in the business's words, the table, the branch with its threshold, and the number you would ask for |
| 2 | The notebook, run from a fresh kernel, with its check outputs, the "What stopped me" cell and your sentence on what surprised you |
| 3 | Your two lines, the first citing a heading from the page |

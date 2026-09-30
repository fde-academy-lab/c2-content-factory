# Which branch would you examine first for a business you can watch, and does the day's method hold on a second Kalpa file?

> "By Thursday I want a recommendation on which branch we examine first, and I will ask why you did
> not pick the others."
> Meera Raghavan, CEO, Kalpa Retail

**Who needs the answer.** Meera wants a recommendation by Thursday and will ask why the other
branches were not picked, and Tuesday's session opens by walking one learner's Part 1 in front of the
room. A tree that cannot defend its first branch, or a number computed on the wrong rows, does not
survive either.

**The questions on the way.** What does the revenue tree look like for a business you can stand in
front of, and which branch would you open first there? Do customers, orders per customer and the
typical order come out right on a second Kalpa sample? What does the profitability framework do that
today's tree does, or leaves out?

The take-home has three parts and takes about two hours in all. Part 1 is the day's thinking on a
business nobody has written about, and it is the part an interviewer will ask you to talk through.
Part 2 is the day's method on a second sample of Kalpa orders you have not seen. Part 3 is twenty
minutes of reading with one specific thing to cite.

---

## What does the revenue tree look like for a business you know, and which branch would you open first?

Meera wants the same thing from the team by Thursday, a tree with one branch defended, and an
interviewer will ask you to talk this part through. Allow about an hour.

Pick a business you can stand in front of this week: the canteen, a kirana store near where you
live, or an app you use most days. A company you have only read about does not count. Revenue is
customers, times how often each buys, times what each purchase is worth, and each branch is a
numerator over a denominator in one window.

- Draw its revenue tree on paper, with every branch in that business's own words. A canteen does
  not have "orders per customer"; it has how many times a week the same person eats there.
- Beside each branch, write the metric as a numerator over a denominator, with the window.
- Beside each branch, write what moving it would cost the owner, named as the thing the owner would
  pay for, such as "a board outside the gate" or "staying open an hour later".
- Name the branch you believe moves most for that business, and defend it with a threshold: "I would
  open this branch first if at least N of every 10 regulars come fewer than M times a week", with
  your N and M, and say what you would open instead if the threshold failed.
- Name the one number you would have to ask the owner for, because you cannot see it from outside.

Hand in one page with the drawing, the table and two sentences.

---

## Do the day's numbers come out right on a second Kalpa sample?

Meera's Thursday recommendation will rest on numbers the team computes from files that arrive with
nobody to explain them, as this second sample does. Allow about forty minutes.

A second sample of Kalpa Retail orders sits in `data/C2_W01_D01_takehome_STUDENT.py`. It has the same
fields as today's file, the order id, customer id, segment, channel, order date, amount and status,
and none of the same numbers, so nothing from class can be pasted across. The three readings of sales
are booked (every order placed), not cancelled (booked less the cancelled orders) and delivered (the
orders that reached a customer and stayed). A customer is a distinct customer id, and orders per
customer is orders over distinct customers on the same reading. The typical order is a middle: the
mean is the total over the count, and the median is the middle of the sorted amounts, halfway
between the two middle amounts when the count is even.

- Start a new notebook beside the day's notebooks, copy in the setup cell from chapter 1's notebook,
  and point the loader at `C2_W01_D01_takehome_STUDENT.py`.
- Compute two tree nodes, customers and orders per customer, on each of the three readings of sales.
  Write each as a numerator over a denominator in a markdown cell before the code cell that computes
  it.
- Compute the typical order on booked and on delivered orders, and say in one markdown line which
  middle you chose and why.
- Write one sentence on what surprised you in this file, with the number that surprised you.

Two pieces of process evidence go in the same notebook. The first is the output of every check the
self-check lists, printed by your own cells. The second is a markdown cell headed "What stopped me",
with the last line of the first error you met, the cell that raised it, and the change you made.

Run the notebook from a fresh kernel, top to bottom, before you call it done. The self-check file,
`takehome/C2_W01_D01_selfcheck_STUDENT.md`, lists every number you should reach.

---

## What does the profitability framework add to today's tree, or leave out?

Today's staple interview question, how you would increase sales for an online retailer, can be
answered from either the tree or the framework, so where they differ is part of your answer. Allow
about twenty minutes.

MConsultingPrep, the profitability framework: https://mconsultingprep.com/profitability-case-framework (verified 29 Sep 2026)

Read the revenue side of the framework. Then write two lines. The first cites one specific thing
from the page, with the heading it sits under, that today's tree also does or leaves out. The
second says whether that thing would change the tree you drew in Part 1, and how.

---

## What do you bring to Tuesday's session?

| Part | What to bring |
|---|---|
| 1 | Bring the page with the tree in the business's words, the table, the branch with its threshold and the number you would ask for. |
| 2 | Bring the notebook, run from a fresh kernel, with its check outputs, the "What stopped me" cell and your sentence on what surprised you. |
| 3 | Bring your two lines, the first citing a heading from the page. |

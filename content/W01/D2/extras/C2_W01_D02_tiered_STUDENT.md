# Extras: one to stretch, one to recover

---

## Stretch: the cut that changes the answer

You finished early and the decomposition felt straightforward. Then this.

**The situation.** You cut the fall by segment and found Retail-Plus. You cut it by channel and
found web. Both are true and the same members sit inside both. Marketing now asks the obvious
follow-up:

> "If I fix web, how much of the fall do I get back?"

**What to build.** A two-way table: segment down the side, channel across the top, orders per
customer in each cell, for both quarters, with the change. Twelve cells.

Then answer three questions in writing.

1. Which single cell carries the largest absolute loss of orders? Not the largest percentage, the
   largest count.
2. If web were restored to its Q1 rate **for Retail-Plus only**, how many orders come back, and what
   share of the total fall is that?
3. What does the table say that neither one-way cut said on its own?

**The hard part, and the point.** A two-way cut has twelve cells and roughly sixty-nine customers,
so some cells hold two or three people. Say which cells you refuse to read, and why, before you
answer any of the three questions. A learner who fills in all twelve confidently has missed the
exercise.

---

## Recovery: one accumulator, then two

The grouping did not land and you would rather rebuild it than nod along. Tonight, alone, costs you
nothing tomorrow.

**Work in a fresh cell. One step at a time, running after each.**

1. Count all the orders with yesterday's three lines. No grouping at all.
2. Now count only Q1 orders, with an `if` inside the loop. Then only Q2, by changing one word.
3. You now have the same code twice. That is the problem grouping solves.
4. Make an empty dictionary called `counts`. Inside the loop, print `order["quarter"]` and nothing
   else. Watch the keys go past.
5. Add one line: `counts[order["quarter"]] = 0`. Run it and print `counts`. Every quarter is zero,
   because you overwrite it every time.
6. Change that line to use `.get()` and add one. Run it. It works, and you can now say exactly why
   step 5 did not.
7. Change `+ 1` to `+ order["amount"]`. Same shape, different question answered.

**What you should end up believing.** A grouped accumulator is the ungrouped one with the variable
replaced by a slot in a dictionary. Nothing else changed. If step 5 did not surprise you, run it
again and read the output properly, because the surprise is the lesson.

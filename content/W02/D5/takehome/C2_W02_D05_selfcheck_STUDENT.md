# Self-check before you hand in Friday's take-home

Ten checks.

## The rebuild

1. Did you actually regenerate the data, or did you rebuild the sheet from the same CSV? Check the
   file's modification time. This catches more people than it should.

2. For every number that moved, can you name the cause in terms of what changed in the warehouse?
   Not "the seed changed", which is true and useless. Which orders, which customers.

3. For every number that did **not** move, can you say why it was stable? A figure that is stable
   by design is a good finding; a figure that is stable because you rebuilt nothing is not.

4. Did any formula break rather than just returning a different number? A broken reference after a
   rebuild is the most common way a deck fails on a Monday morning.

## The sheet

5. Open your workbook and change one input cell. Does anything downstream move? If not, something
   below it is a typed number wearing a formula's clothes.

6. Is every input cell visually marked, and is every marked cell actually an input? Both
   directions. A marked cell holding a formula is worse than an unmarked one.

7. Does the first sheet say what the workbook was built from and when? One cell. If a colleague
   opened it cold, would they know which export it came from?

## The operating rule

8. Read your three lines. Are they in your words? If any sentence could be lifted from the deck
   verbatim, you have copied rather than decided.

9. Your fourth line is a condition. What breaks it first in a real team? If your answer is
   "carelessness", think harder: it is usually a deadline and a correction that only exists in one
   place.

## The paragraph

10. Read your four sentences. Is the fourth one about a habit rather than an intention? "I will be
    more careful" is an intention. "I will take the row count before any total, including when I
    am certain" is a habit, because it is checkable.

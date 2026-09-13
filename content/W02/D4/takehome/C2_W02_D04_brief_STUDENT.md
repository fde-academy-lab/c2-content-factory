# Take-home: the tool note, and one column that earns its place

## The situation

The senior analyst asked a question in front of the room and expects a written answer:

> "You did the tree in plain Python in Week 1, in SQL on Monday. Do it a third way now, and tell me
> honestly which tool you would pick for which job."

Tonight you answer it, and you extend the customer table by one column that proves you understood
what the table is for.

## Part one: the tool note

Five sentences. Not four, not a page.

| Sentence | What it has to do |
|---|---|
| 1 | Name what the warehouse owns, and why |
| 2 | Name what pandas owns, and why |
| 3 | Name what plain Python owns, and why |
| 4 | Name one thing you would **refuse** to do in one of the three, and the reason |
| 5 | Name the case where you would change your mind about sentence 4 |

The fourth sentence has to be about audit, ownership or who can read the thing. If it is about
speed or about a library's capabilities, rewrite it.

The fifth sentence is what separates a rule from a slogan. If you cannot think of a case, the rule
is too broad.

## Part two: one more column

Add exactly one column to the customer table that the growth team did not ask for and would thank
you for.

Above it, four comment lines:

```python
# What it is:        in words, not in code
# Why they want it:  the decision it would change
# The cost:          what it assumes, or what it hides
# Refresh safety:    what happens to it when the table is rebuilt on Monday
```

The refresh-safety line is the one most people skip and the one the growth team will hit first.
A column computed from "today" means something different every Monday.

## Constraints

The column must come from data already in the warehouse. No new feeds.

It must survive `validate="one_to_one"` on every merge used to build it. If you need a merge that
cannot, say so and aggregate first.

It must not be a rename or a rescale of a column already there. "Monetary in thousands" is not a
new column.

## The self-check

`C2_W02_D04_selfcheck_STUDENT.md`.

## Why these two together

The note is judgment with no code. The column is code that only works if the judgment is right.
Handing in one without the other is the failure mode this pairing exists to catch.

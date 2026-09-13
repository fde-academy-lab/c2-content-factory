# Take-home: one ranking question, and the impostor beside it

## The situation

Marketing has the protect list. Tomorrow somebody will ask you for a ranking that sounds simple
and is not, and the difference between the two answers will be a list of names that goes to real
people.

Tonight you write one ranking question of your own, then write the `GROUP BY` version that looks
like it answers the same question, and say what separates them.

## What to hand in

One `.sql` file with two queries.

The first uses a window function and answers a question you invented, about Kalpa, that somebody
in Marketing or Finance could plausibly ask.

The second is its impostor: a `GROUP BY` query that a reasonable person would believe answers the
same question. It has to be genuinely tempting. A deliberately broken query does not count.

Above the pair, a comment block:

```sql
-- The question:   in a stakeholder's words
-- The window:     what PARTITION BY and ORDER BY mean here, in one line each
-- The impostor:   what it actually answers instead
-- The difference: one concrete case where they disagree, with numbers
```

## The constraint

Your two queries must return **different results** on the warehouse, and your difference line has
to name a real row where they diverge. Not "they would differ if there were a tie". Find one, or
change the question until you do.

If you cannot make them differ, your window was decorative and the `GROUP BY` was the right tool
all along. Saying that in one sentence is a valid hand-in, and it is worth more than a window
function used for its own sake.

## Also

One sentence, separately: a tie rule you would choose for your question, and the business sentence
that would justify it. Invent the stakeholder; keep them inside the Kalpa world.

## The self-check

`C2_W02_D03_selfcheck_STUDENT.md` before you hand in.

## Why the impostor

Today the room saw three defensible answers to "the top fifty" and only one matched what was
asked. The skill being built is not writing a window function. It is noticing that two queries
which both look right disagree, and being able to say which question each one answers.

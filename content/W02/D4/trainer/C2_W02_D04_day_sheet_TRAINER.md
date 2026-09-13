# Trainer day sheet: Week 2, Thursday. pandas groupby, merge and reshape

TRAINER ONLY.

## The shape of the day

| Block | Minutes | What has to happen |
|---|---|---|
| The growth team's ask | 15 | The room lists the columns and where each comes from |
| read_sql, groupby, agg | 50 | The Week 1 accumulator beside the one-liner |
| merge with validate= | 40 | The MergeError raised on the exposure feed |
| Reshape | 35 | pivot_table and melt, and the wrong-index pivot |
| The three-tool re-expression | 45 | Same node, three tools, on one screen |
| Unguided | 40 | The customer table and the tool note |
| Kahoot and close | 20 | Seven questions |

Total 245 minutes, the longest day of the week.

## Every pandas move lands on something the room did by hand

Say so each time. `groupby` is Week 1's accumulator, `merge` is Tuesday's join, `pivot_table` is a
reshape they have never needed until now. The room has done two of the three already and saying
so is the teaching, not a nicety.

## What is planted in v4

**Never name it.**

| Planted | Found by | Value |
|---|---|---|
| Duplicate customer keys in the exposure feed | A merge that grows the table, then `validate=` | 6 keys |
| A customer whose months pivot wrongly if indexed by order | Reading the row labels of the wrong pivot aloud | The grid comes back under 40 percent filled |

## The failure to stage, with its exact text

Have the room merge the exposure feed with no `validate=` first, and take the row count. 340 in,
346 out. Then have them set `validate="one_to_one"`:

```
pandas.errors.MergeError: Merge keys are not unique in right dataset; not a one-to-one merge
Duplicates in right:
 customer_id
     C-0001
     C-0002 ...
```

The order matters. Growing quietly first, then refusing loudly, is what makes the argument for
`validate=` rather than a slide claiming it is good practice.

## The second failure, which is quieter

The wrong-index pivot. Index by `order_id`, and the call runs and returns a table that is almost
entirely empty and completely meaningless.

Do not point at the emptiness. Ask somebody to read the row labels aloud. "Each row is one order"
is the moment, and it teaches a habit that no total check would have given them.

## The moment the day turns

The senior analyst's question, asked as a person rather than as a slide. Put all three versions of
revenue per segment on one screen at the same time and let the room see that the shortest one is
not obviously the winner.

Then write the three questions on the board and leave them there:

```
Who owns this number?
For how long?
Who has to be able to read it?
```

Run three or four real asks through them out loud. The point lands when somebody notices that
pandas was correct for the afternoon prototype and refused for the quarter-end number, on the same
three questions.

## The refusal

Somebody has to say out loud why Finance's Monday number should not come from a notebook, and the
reason has to be about audit rather than about pandas. If the room reaches for "pandas is slower"
or "it might have a bug", push back: those are technical objections to a procedural problem, and
noticing that reflex in yourself is worth more than the answer.

## Timing pressure

Cut `melt` first, per the row: name it, park it. Then cut the vectorised contrast. Never cut
`validate=` or the three-tool re-expression, which are the day.

## Close-out

Release both solution files. Set the take-home and say that the five-sentence note and the extra
column are one hand-in rather than two: the note is judgment with no code, the column is code that
only works if the judgment is right.

Have everybody export the customer table as a CSV before they leave. Tomorrow needs it and a room
that arrives without it loses twenty minutes.

Preview Friday in one line: Meera's office runs on Excel, and the chief of staff wants three
things that open on a laptop with no login.

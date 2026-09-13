# Provenance: Week 2, Saturday

INTERNAL.

## Where the paper comes from

The curriculum row's Subtopics column carries the week's question set, ten items, questions only.
Structure.md locks the format: derived from the week's interview set, framed for short answers so
papers can be swapped, ungraded, AI-free by format.

The paper expands those ten into twenty-seven items across seven sections. Every one of the row's
ten appears, most of them close to verbatim:

| Row question | Paper item |
|---|---|
| WHERE against HAVING | A1 |
| INNER against LEFT | B1 |
| RANK, DENSE_RANK, ROW_NUMBER on a tie | C1 |
| groupby in the split-apply-combine sentence | D1 |
| Your LEFT join grew the row count and revenue doubled | B2, B3 |
| Top-3 per segment: GROUP BY or a window | C2 |
| Which merge argument raises on duplicate keys | D2 |
| A pivot's total disagrees with the warehouse | E2 |
| Same question, three tools | F1 |
| Kalpa Health asks where growth comes from | G1 |

The seventeen added items come from the weekday interview columns, which the row says calibrate
difficulty. Nothing is invented beyond those two sources.

## Numbers quoted in the paper

Every figure the paper asks a learner to reason about is from the loaded warehouse and is asserted
by `python3 data/generate_client_zero.py --contract`: 1,000 orders, 1,450 join rows, 450 orders
with two payment rows, 30 with none, the tie at position fifty, 340 customers and 346 rows after
an unvalidated merge.

The four Q2 totals in C1 are illustrative rather than drawn from the data, which is why the item
states them.

## Marks language

Structure.md locks this as ungraded and never a marks component. The paper and the discussion
guide both say so and neither uses the words marks, weightage or graded out of. The answer key
gives full-credit answers, which is a description of an answer rather than a score.

## Open, for the reviewer

Section G is one item worth five minutes of writing and it carries the whole transfer into Build 1.
It cannot be marked against a key, and the guide says so. A reviewer who wants it scoreable should
say what they would trade for that, because the alternative is a narrower question that tests
recall rather than transfer.

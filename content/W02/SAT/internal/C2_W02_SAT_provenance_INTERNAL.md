# Provenance: Week 2, Saturday

INTERNAL.

## Where the paper comes from

The paper is the tracker's Week 2 paper from the Saturday item bank (revised format of 19 September
2026), rendered by `scripts/build_saturday_paper.py`: 58 objective items for a 120-minute slot, at
119.5 minutes by the blueprint's pace, 14 easy, 34 medium and 10 hard. The STUDENT paper prints the
Item column only; the TRAINER key carries every other column. The earlier short-answer paper of
27 items was retired when the Saturday row changed to the objective format.

Eight items carry option edits from `data/programme/paper_edits.yaml`, all proposed: in each, the
bank's key was the longest option, which breaks the house distractor rule, so one distractor was
reworded into a sharper near-miss at the key's length. The stems and the keys are the tracker's.
The key file lists the eight, and the edits file says how to accept or reject each one.

## The row's anchors and the items that descend from them

| Anchor on the row | Items |
|---|---|
| WHERE against HAVING | 1, 11, 33 |
| INNER against LEFT | 4, 12, 21, 35 |
| RANK, DENSE_RANK and ROW_NUMBER on a tie | 14, 25, 26, 44 to 47, 54 |
| groupby in the split-apply-combine sentence | 16, 29, 56 |
| The LEFT join that grew the row count | 13, 22 to 24, 34, 40 to 43, 53 |
| Top-3 per segment | 7, 27, 36 |
| The merge argument that raises | 8, 30, 38, 49 |
| The pivot that disagrees with the warehouse | 17, 48 to 51 |
| Same question, three tools | 20, 31, 32, 58 |
| Kalpa Health and what transfers | none; it is the discussion's bridge |

## Numbers in the paper

The scenario sets and the applied maths items state their own numbers, which are the bank's and are
illustrative rather than drawn from the loaded warehouse. Every keyed number was recomputed on
27 September 2026 and holds: 1,050 and 1,020 rows for the left and inner joins of set 1, rank 4 for
member D and dense rank 4 for member F in set 2, five members at dense rank three or less, 1,060
merged rows in set 3, 8 groups, Rs 21 lakh summed against Rs 20 lakh collected, 51 rows under RANK
and 50 under ROW_NUMBER on a tie at fifty, falls of Rs 800 and Rs 300, and 400 customers at 2.5
orders each. The `MergeError` text quoted in the discussion guide was reproduced on pandas 3.0.5.

## Marks language

The paper is ungraded and never a marks component. The STUDENT paper carries a count of items right
and no marks, weightage or total; the key's marking rule decides only whether an item is right.

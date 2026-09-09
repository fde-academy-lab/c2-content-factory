# Data provenance: Week 1, Day 3

Internal working file. Never given to a learner.

## Where this pack's data comes from

Every data file in this folder is generated. Two commands rebuild all of them:

```
python3 data/generate_client_zero.py --version v1            --out content/W01/D3 --stem C2_W01_D03
python3 data/generate_client_zero.py --version w1d3-takehome --out content/W01/D3 --stem C2_W01_D03
```

The generator is seeded, so those commands produce byte-identical files on every machine. Editing a data file by hand breaks that guarantee. Change the generator, rerun the commands, then rerun the verification gate and both notebooks.

## The witnesses this day turns on

`python3 data/generate_client_zero.py --list` prints the full table. The ones Wednesday uses, each verified by running it rather than asserted:

| Witness | Value | What breaks without it |
|---|---|---|
| 50 orders across 49 distinct `order_id` | `KR4201` appears twice | The whole of block two |
| Whole-record duplicates | 0 | The first deliberate failure, which reports nothing |
| The pair's differing field | `order_date`, six weeks apart | The identity-rule discussion, and the ambiguity that makes it real |
| Amounts that fail `int()` | 6: `twelve`, two empty, `12,400`, `24 500`, `Rs 8000` | The gap between present and converts, so the profiler has nothing to find |
| The whale | Rs 480,000, 86 percent of the Rs 561,145 total, next largest Rs 2,995 | The outlier section, and Thursday's mean |
| Student segment | Exactly 12 orders | Thursday's sample-size lesson |
| The truncated feed | Stops at line 47 | Nothing today; it is carried for continuity with Tuesday |
| The companion file | Header row appears twice | Notebook 2 section 6, which is on the cut list |

## The figures this pack quotes

Each is computed from the generated files rather than typed.

| Figure | Value |
|---|---|
| Main file | 50 orders in, 44 profiled, 6 rejected, total Rs 561,145 |
| Raw profile, `amount` | present 48, converts 44, distinct 46 |
| Coerced profile, `amount` | present 50, converts 50, distinct 42 |
| Raw and coerced, `discount` | present 11 becomes present 50 |
| The whale | Rs 480,000, 86 percent of the total, next largest Rs 2,995, middle order Rs 1,955 |
| Take-home file | 41 rows, 40 distinct ids, 38 convert, 3 rejected, total Rs 164,110, largest Rs 96,000 at 58 percent |

## Two things that would quietly break this pack

The near-duplicate twin is drawn from a non-Student order on purpose. If it lands on a Student order the Student count becomes 13 and Thursday's sample-size witness is gone, with nothing raising anywhere.

The whale must stay convertible. If it ever became text it would land in the rejects file, the outlier section would have nothing to investigate, and the day's fourth idea would have no example.

## Conflicts, now closed

Section 9 of `docs/07_Client_Zero.md` recorded four conflicts between that file and the curriculum export. All four were ruled on at v1.1 on 09 September 2026, in the curriculum's favour, and the client-zero file was edited to match rather than the other way round.

Two touched this pack and both settled in its favour, so nothing here changes: v1 at 50 orders is the Wednesday and Thursday dataset, and the near-duplicate pair officially differs on `order_date`, which is what the entity model supports and what this file has always contained.

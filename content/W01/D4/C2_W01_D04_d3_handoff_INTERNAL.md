# Handoff: what Day 3 must produce for this pack to hold

Internal working file. Never given to a learner.

## The problem this file exists to prevent

Thursday's input is Wednesday's output. Wednesday's pack was not built when this pack was built, so this pack ships the cleaned file itself, as `C2_W01_D04_data_cleaned_STUDENT.csv`.

If the Day 3 build produces a different cleaned file, Thursday's entire arithmetic becomes wrong and no script will catch it, since both files would be internally consistent. This file is the reconciliation point, and whichever build runs second reads it first.

## What Day 3 must end with

The Wednesday row states the day's single question as how many usable records the scenario actually has, and names the answer as the input to Thursday's statistics. That answer is fixed here.

| Fact | Value | Where it comes from |
|---|---|---|
| Records in | 50 | `docs/07_Client_Zero.md`, dataset version v1, "50 records" |
| Records removed by the Wednesday pass | 3 | This pack's arithmetic |
| Records out, and Thursday's input | 47 | Both of the above |
| The whale | One order of Rs 480,000, retained because it is real | Client zero v1 planted witnesses; the Wednesday row keeps the whale through cleaning |
| The small segment | `segment_d`, exactly 12 records | Client zero v1, "a Student segment of exactly 12 records so sample size bites" |
| Segment counts after cleaning | `segment_a` 20, `segment_b` 9, `segment_c` 6, `segment_d` 12 | This pack |
| Total amount after cleaning | Rs 846,000 | This pack |

## The three removals, which Day 3 owns

Wednesday's row plants a near-duplicate pair, text-typed values and an absent optional field. Three records leave the file, and each removal must witness exactly one of Wednesday's teaching points:

1. **The near-duplicate loser.** Two records share an id and differ in one field. Wednesday's identity rule keeps one and drops the other. This is Wednesday's headline break, where the whole-record dedupe reports zero while the distinct-id count disagrees.
2. **The record whose amount fails conversion.** Client zero v1 plants an amount spelled "twelve". Tuesday's convert-or-reject function catches it and Wednesday's pass logs it with a reason.
3. **The record missing a required field.** Client zero v1 plants it. Wednesday's three-way missingness decision resolves it as a drop, with the reason written down.

Wednesday's reconciliation line therefore reads `50 in = 47 clean + 3 rejected`, and Thursday opens on the 47.

## What Day 3 must not do

- **Do not drop the whale.** Rs 480,000 is real and Wednesday's row says the whale survives cleaning because it is real. Thursday's entire half one is that record. If Wednesday removes it, Thursday has no lesson.
- **Do not resolve the near-duplicate in favour of a record that changes a segment count.** The four counts above are load-bearing across nine of Thursday's artifacts.
- **Do not change the four segment placeholder values or the five field names**, both of which are carried forward from the shipped Day 2 pack. See `C2_W01_D04_rename_map_INTERNAL.md`.

## The check, whichever build runs second

```
python3 - <<'PY'
import csv, statistics as st, collections
rows = list(csv.DictReader(open("content/W01/D4/C2_W01_D04_data_cleaned_STUDENT.csv")))
amts = [int(r["amount"]) for r in rows]
assert len(rows) == 47
assert sum(amts) == 846000
assert st.median(amts) == 7500
assert max(amts) == 480000
assert dict(collections.Counter(r["segment"] for r in rows)) == {
    "segment_a": 20, "segment_b": 9, "segment_c": 6, "segment_d": 12}
print("Day 4 input intact")
PY
```

If the Day 3 build produces a cleaned file that fails this check, the two packs disagree and one of them has to change. The Day 3 build should adopt this file rather than regenerate one, since nine Day 4 artifacts quote its numbers and only Day 3's decisions log quotes Day 3's.

## One consequence worth knowing

Thursday's pack ships its own copy of the cleaned data. Once Day 3 ships, that file exists in two places, and the Day 3 copy is the canonical one. At that point the Day 4 copy should either be deleted in favour of a documented relative path to Day 3's output, or kept deliberately so Thursday runs standalone in a fresh Codespace. Keeping it is the better call for a room of sixty on a four-day-old environment, and it is the reason it was shipped this way. Record whichever call is made in the Build Tracker.

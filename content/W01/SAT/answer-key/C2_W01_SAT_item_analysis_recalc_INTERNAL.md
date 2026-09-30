# Recalculation manifest: Week 1 item analysis

INTERNAL. Written by `scripts/build_saturday_paper.py --docx` beside the workbook and read by `scripts/xlsx_recalc.py`. As shipped, no marks are entered. The flip marks six seats on the first five items so that seat 1 tops the room and seat 6 sits at the bottom, Q2 is right once in six, and on Q3 the bottom third beats the top third; both flags, the bands and the discussion order must follow. The same six seats rate Part 1 as 3, 4, 2, 3, 1 and 4, so two of them (seats 4 and 6) rated it 3 or 4 and got under half of it right.

```yaml
workbook: C2_W01_SAT_item_analysis_TRAINER.xlsx
verdicts:
- sheet: Discussion
  cell: B2
  expect: No marks entered yet.
- sheet: Ratings
  cell: D43
  expect: '0'
flips:
- name: six seats marked on the first five items
  set:
  - sheet: Marks
    cell: B5
    value: 1
  - sheet: Marks
    cell: C5
    value: 1
  - sheet: Marks
    cell: D5
    value: 0
  - sheet: Marks
    cell: E5
    value: 1
  - sheet: Marks
    cell: F5
    value: 1
  - sheet: Marks
    cell: B6
    value: 1
  - sheet: Marks
    cell: C6
    value: 0
  - sheet: Marks
    cell: D6
    value: 0
  - sheet: Marks
    cell: E6
    value: 1
  - sheet: Marks
    cell: F6
    value: 1
  - sheet: Marks
    cell: B7
    value: 1
  - sheet: Marks
    cell: C7
    value: 0
  - sheet: Marks
    cell: D7
    value: 0
  - sheet: Marks
    cell: E7
    value: 1
  - sheet: Marks
    cell: F7
    value: 0
  - sheet: Marks
    cell: B8
    value: 1
  - sheet: Marks
    cell: C8
    value: 0
  - sheet: Marks
    cell: D8
    value: 1
  - sheet: Marks
    cell: E8
    value: 0
  - sheet: Marks
    cell: F8
    value: 0
  - sheet: Marks
    cell: B9
    value: 0
  - sheet: Marks
    cell: C9
    value: 0
  - sheet: Marks
    cell: D9
    value: 1
  - sheet: Marks
    cell: E9
    value: 0
  - sheet: Marks
    cell: F9
    value: 0
  - sheet: Marks
    cell: B10
    value: 0
  - sheet: Marks
    cell: C10
    value: 0
  - sheet: Marks
    cell: D10
    value: 0
  - sheet: Marks
    cell: E10
    value: 0
  - sheet: Marks
    cell: F10
    value: 0
  - sheet: Ratings
    cell: B5
    value: 3
  - sheet: Ratings
    cell: B6
    value: 4
  - sheet: Ratings
    cell: B7
    value: 2
  - sheet: Ratings
    cell: B8
    value: 3
  - sheet: Ratings
    cell: B9
    value: 1
  - sheet: Ratings
    cell: B10
    value: 4
  verdicts:
  - sheet: Discussion
    cell: B2
    contains: Most-missed first
  - sheet: Discussion
    cell: B5
    expect: '2'
  - sheet: Items
    cell: M6
    contains: fewer than one in five
  - sheet: Items
    cell: M7
    contains: bottom third beat the top third
  - sheet: Marks
    cell: AM5
    expect: top
  - sheet: Marks
    cell: AM10
    expect: bottom
  - sheet: Marks
    cell: AM7
    expect: middle
  - sheet: Ratings
    cell: D43
    expect: '2'
```

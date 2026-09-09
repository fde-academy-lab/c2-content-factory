# Data provenance: Week 1, Day 4

Internal working file. Never given to a learner.

## Where this pack's data comes from

Thursday does not generate data. It consumes Wednesday's output, which is the point of the day.

`data/C2_W01_D04_profiled_STUDENT.csv` is the profiled set that Wednesday's notebook 2 produces at runtime as `output/C2_W01_D03_profiled_orders_STUDENT.csv`. It is reproduced here so Thursday runs standalone in a fresh Codespace, since a room of sixty on a four-day-old environment should not depend on another day's notebook having been run in the right order.

Two commands rebuild it from scratch:

```
python3 data/generate_client_zero.py --version v1 --out content/W01/D3 --stem C2_W01_D03
python3 - <<'PY'
import csv, pathlib
src = pathlib.Path("content/W01/D3/data/C2_W01_D03_orders_STUDENT.csv")
orders = list(csv.DictReader(src.open()))
clean = []
for r in orders:                       # Wednesday's clean_records, unchanged
    try:
        k = dict(r); k["amount"] = str(int(r["amount"])); clean.append(k)
    except ValueError:
        pass
out = pathlib.Path("content/W01/D4/data/C2_W01_D04_profiled_STUDENT.csv")
with out.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(orders[0].keys())); w.writeheader(); w.writerows(clean)
PY
```

The generator is seeded, so both steps produce byte-identical files on every machine. Editing this file by hand breaks that guarantee and silently breaks Wednesday's continuity. Change the generator, rerun both commands, then rerun the verification gate and both notebooks.

## The reconciliation Thursday inherits

```
50 orders in  =  44 profiled  +  6 rejected
```

The six rejections are the amounts that fail `int()`: `twelve`, two empty strings, `12,400`, `24 500` and `Rs 8000`. Wednesday's rejects log records each with its reason.

Wednesday's clean pass is **conversion only**. It does not deduplicate. The near-duplicate pair was a recorded decision, "keep both rows, flag the pair", so `KR4201` reaches Thursday twice and Thursday describes 44 rows containing one unresolved pair. This is deliberate and both notebooks say so aloud.

## The figures this pack quotes

Each is computed from the file rather than typed, and each was confirmed by a cold notebook run in the build session.

| Figure | Value |
|---|---|
| Orders, total | 44, Rs 561,145 |
| Mean, median | Rs 12,753.30 and Rs 1,910.00, a ratio of 6.68 |
| Orders at or above the mean | 1 of 44 |
| The whale | `KR4232`, Rs 480,000, Retail-Core, delivered, 85.5 percent of all revenue |
| Next largest order | Rs 2,995, so the whale is 160 times it |
| Without the whale | n=43, mean Rs 1,887.09, median Rs 1,865.00, which is the mean landing within Rs 22 of the median |
| Min, max, range | Rs 800, Rs 480,000, Rs 479,200 |
| Fence | Q1 Rs 1,287.50, Q3 Rs 2,718.75, IQR Rs 1,431.25, upper fence Rs 4,865.62, catching exactly one order |
| Skew read | median to min Rs 1,110, median to max Rs 478,090, a ratio of 431 |
| Hand-worked seven | 1030, 1145, 1280, 1310, 1865, 2270, 2835; mean Rs 1,676.43, median Rs 1,310; swapping the top for Rs 480,000 gives mean Rs 69,842.86 and the same median |
| Segment counts | Business 9, Retail-Core 14, Retail-Plus 11, Student 10 |
| Segment medians | Rs 2,050, Rs 1,910, Rs 1,435, Rs 1,430 |
| Return rates | Business 1 of 9 at 11.1 percent, Student 2 of 10 at 20.0 percent, Retail-Core 5 of 14 at 35.7 percent, Retail-Plus 4 of 11 at 36.4 percent |
| The swing | One more Business return gives 22.2 percent, behind Student |
| Retail-Core mean | Rs 36,027.14 against a median of Rs 1,910, and Rs 1,875.38 once the whale is removed |
| Take-home, discount cut | present 10 orders at 20.0 percent, absent 34 orders at 29.4 percent |
| Take-home, month cut | 2026-08 holds 43, 2026-09 holds 1, and that one is `KR4201` |

## Two witnesses that changed shape between Wednesday and Thursday

Worth knowing before anyone reports a bug against this pack.

| Witness | As generated | As Thursday sees it |
|---|---|---|
| "a Student segment of exactly 12 records" | 12 Student orders in the raw v1 file | **10**, because `KR4235` and `KR4237` are Student orders whose amounts fail conversion and are rejected on Wednesday |
| "near-duplicate pair sharing an order_id" | 50 rows across 49 distinct ids | Still 2 rows, since Wednesday chose to keep both |

The Student drop is not a defect. Thursday teaches it directly: cleaning decisions change denominators, and the rejects log is the only place that fact is written down. Both notebooks and the study notes call it out.

## The activity holds a second copy

`demos/C2_W01_D04_typical_number_bench_STUDENT.html` embeds the same 44 rows in a `const DATA` array, because it is a single file with no network access. Nothing cross-checks the two at build time.

The build session verified them equal as multisets. Repeat that check after any data change:

```
python3 - <<'PY'
import re, csv, pathlib
D = pathlib.Path("content/W01/D4")
h = (D/"demos/C2_W01_D04_typical_number_bench_STUDENT.html").read_text()
blk = h.split("const DATA = [",1)[1].split("].map",1)[0]
a = sorted((s,int(x),st) for s,x,st in re.findall(r'\["([\w-]+)",(\d+),"(\w+)"\]', blk))
b = sorted((r["segment"],int(r["amount"]),r["status"])
           for r in csv.DictReader((D/"data/C2_W01_D04_profiled_STUDENT.csv").open()))
print("activity matches the CSV:", a == b)
PY
```

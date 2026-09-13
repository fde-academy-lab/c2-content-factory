# Provenance: Week 1 Day 4

**INTERNAL.**

---

## The curriculum row

`docs/curriculum/W1_Data_analysis_found.md`, the Thursday 01 October 2026 row. Client zero is
`docs/07_Client_Zero.md` at v2.2.

---

## The data

`data/generate_client_zero.py`, version `v3`, seed `20260928`.

```
python3 data/generate_client_zero.py --version v3 --out content/W01/D4/data --stem C2_W01_D04
```

| File | What it is |
|---|---|
| `..._orders_STUDENT.csv` | The cleaned two quarters, 186 orders |
| `..._exposure_STUDENT.csv` | 160 customers with their August revenue and whether the monsoon sale reached them |
| `..._campaigns_STUDENT.csv` | The campaign master row |

| Planted | Used by |
|---|---|
| A Retail-Plus fall of 35.0 percent against Retail-Core's 2.7 | The permutation test, which returns 0 of 5,000 |
| Student holding exactly 12 orders, 5 then 7 | The sample-size test, which returns p = 0.383 |
| An exposed group that is 50 percent Retail-Plus against the control's 40 | The Simpson reversal in block 5 |
| Retail-Plus spending 2.5 times what Retail-Core spends | The same |

---

## The statistics, computed rather than asserted

Every figure below is produced by the notebook at seed `20260101` and re-asserted by a `kit.check`.

| Test | Observed | Chance-only worlds | Reported |
|---|---|---|---|
| Retail-Plus against Retail-Core, shuffling members between labels | a 32.3 point gap | 0 of 5,000 | `p < 0.0002` |
| Student, each order landing in either quarter | 5 then 7, a 40 percent rise | 1,914 of 5,000 | `p = 0.383` |
| Web against app, on clean data, for the take-home | a 3.4 point gap | 3,737 of 5,000 | `p = 0.75` |

The Student figure matches the exact binomial: the chance of seven or more heads in twelve fair
flips is 0.387, so the simulation at 0.383 is correct to within its own resolution.

**The web result is deliberate and is the take-home's whole point.** Tuesday's 22 percent web fall
was computed on the export before the reconciliation, and most of it was the duplicated rows, which
sit in Retail-Plus and therefore in web. The segment finding survives the clean pass at 33 percent
and the channel finding does not survive at all. That is not a defect in the data; it is what
happens when a cut is re-run on reconciled numbers, and it is the lesson.

---

## Sources, with the date each was checked

| Link | Role | Checked |
|---|---|---|
| https://seeing-theory.brown.edu/frequentist-inference/index.html | Frequentist inference, both audiences | 05 Sep 2026, row-supplied |
| https://statquest.org/video_index.html | The two hypothesis-testing videos | 05 Sep 2026, row-supplied |
| https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data | Summarising quantitative data | 03 Sep 2026, row-supplied |
| https://www.tryexponent.com/blog/top-data-analyst-interview-questions | Conveying insights to a non-technical audience | 13 Sep 2026, row-supplied |
| https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/ | Hypothesis-testing items | 03 Sep 2026, row-supplied |

**Reachability, checked 13 Sep 2026:** all returned 200 to an automated request.

---

## Built beyond the row, and why

The row's trainer note says to name a confidence interval and park it. The pack names it in the deck
and does not compute one, which matches. The stretch extra asks for the smallest detectable effect
on twelve observations; that is not in the row and it is the natural follow-up an interviewer asks
after "not significant", so it earns its place as an optional extra rather than as content.

# Provenance: Week 1 Day 2

**INTERNAL.**

---

## The curriculum row

`docs/curriculum/W1_Data_analysis_found.md`, the Tuesday 29 September 2026 row, read in column
order. Client zero is `docs/07_Client_Zero.md` at v2.2.

---

## The data

`data/generate_client_zero.py`, version `v1`, seed `20260928`. Regenerate with:

```
python3 data/generate_client_zero.py --version v1 --out content/W01/D2/data --stem C2_W01_D02
```

Asserted by `python3 data/generate_client_zero.py --contract`.

| Planted | Used by |
|---|---|
| Customer count flat at 69 across both quarters | Rung two, which disproves marketing's claim |
| Orders per customer falling 49 percent in Retail-Plus against 5 in Retail-Core | Rung four, the finding of the day |
| The `discount` field absent on 58 of 200 records | The block-5 `KeyError` and the defaults discussion |
| 14 duplicated Q1 rows | **Not today's lesson.** They are here from `v1` and are found on Wednesday. |

The duplicates sit almost entirely in Retail-Plus by design, because a migration re-runs a batch
rather than a random sample. That is what makes Tuesday's 49 percent an overstatement rather than an
error, and it is why Wednesday's clean pass leaves Retail-Plus standing at 35 percent rather than
removing it.

---

## The arithmetic, checked

| Claim in the pack | Source |
|---|---|
| Revenue down 11.0 percent | Rs 2,10,00,000 to Rs 1,87,00,000 |
| Orders per customer down 24.6 percent | 114/69 to 86/69 |
| Revenue per order up 18.0 percent | Rs 1,84,211 to Rs 2,17,442 |
| The decomposition closes | 1.000 x 0.754 x 1.180 = 0.890, against 0.890 |
| Retail-Plus down 49.0 percent | 2.32 to 1.18 orders per member |
| Web down 22.4 percent, store 8.1, app flat | Computed from the same file for the take-home |

Every one of these is re-asserted by a `kit.check` inside the notebook, so a change to the generator
breaks the notebook rather than the lesson.

---

## Sources, with the date each was checked

| Link | Role | Checked |
|---|---|---|
| https://www.tryexponent.com/blog/top-data-analyst-interview-questions | The sales-drop investigation, trainer preparation | 13 Sep 2026, row-supplied |
| https://britinstitute.uk/blog/data-analyst-case-study-interview-questions | The case walkthrough, student reference | 13 Sep 2026, row-supplied |
| https://www.youtube.com/watch?v=9Os0o3wzS_I | Corey Schafer, Functions | 03 Sep 2026, row-supplied |
| https://www.youtube.com/watch?v=NIWwJbo-9_8 | Corey Schafer, try/except | 03 Sep 2026, row-supplied |
| https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data | Summarising quantitative data | 03 Sep 2026, row-supplied |

**Reachability, checked 13 Sep 2026:** all returned 200 to an automated request.

---

## Built beyond the row, and why

The row's technique column does not name a channel cut. The take-home adds one because the row's
own interview angle asks how to make the case to marketing when the data says frequency, and
marketing buys media by channel rather than by segment. The cut is computed from the same file and
invents nothing.

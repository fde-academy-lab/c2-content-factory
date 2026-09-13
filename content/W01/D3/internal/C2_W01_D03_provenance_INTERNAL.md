# Provenance: Week 1 Day 3

**INTERNAL.**

---

## The curriculum row

`docs/curriculum/W1_Data_analysis_found.md`, the Wednesday 30 September 2026 row. Client zero is
`docs/07_Client_Zero.md` at v2.2.

---

## The data

`data/generate_client_zero.py`, version `v2`, seed `20260928`.

```
python3 data/generate_client_zero.py --version v2 --out content/W01/D3/data --stem C2_W01_D03
```

| File | What it is |
|---|---|
| `..._orders_STUDENT.csv` | The ERP export, 201 rows |
| `..._orders_STUDENT.json` | The app feed, truncated mid-record |
| `..._vendor_STUDENT.csv` | The companion export with its header row repeated |
| `..._takehome_STUDENT.csv` | A 97-row second export with **different** defects |

| Planted in the class file | Used by |
|---|---|
| 14 duplicated Q1 rows carrying exactly Rs 20,00,000 | The reconciliation, and the gap Anand names |
| One amount spelled `twelve` | The `ValueError` in block 2 |
| One record with no `status` | The presence count in block 3 |
| `KR-02151` twice, dates differing | The identity rule in block 4, which is the day's judgment |
| The JSON cut mid-string | The `JSONDecodeError` in block 2 |
| The vendor file's repeated header | The profiling discussion, lowest priority |

| Planted in the take-home file | Why it is different |
|---|---|
| A header row pasted into the **middle** of the body | The class file has it in a companion file, so the shape is familiar and the location is not |
| An amount of `-2400` | **It converts without error**, so a pass built on `isdigit` misses it entirely |
| A date written `12/05/2026` | Not a defect at all, and deciding that is the item worth most |
| Six duplicated ids in a different segment | The counts cannot be reused |

---

## The arithmetic, checked

| Claim | Value |
|---|---|
| Input | 201 |
| Clean | 184 |
| Rejected | 17 |
| Reconciles | 184 + 17 = 201 |
| Q1 as exported | Rs 2,09,98,210 |
| Q1 reconciled | Rs 1,89,98,210 |
| Gap | Rs 20,00,000 |

Q1 is Rs 2,09,98,210 rather than exactly Rs 2.10 crore because the `twelve` row's original amount is
lost when the string replaces it. The difference is Rs 1,790, or 0.0085 percent, so both figures
round to the ones the stakeholders quote. That is deliberate: the conversion defect teaches the
discipline without moving the headline, which is the right weight for it.

Every figure is re-asserted by a `kit.check` in the notebook.

---

## Sources, with the date each was checked

| Link | Role | Checked |
|---|---|---|
| https://realpython.com/python-csv/ | Reading and writing CSV, both audiences | 03 Sep 2026, row-supplied |
| https://docs.python.org/3/library/json.html | `JSONDecodeError`, trainer preparation | 03 Sep 2026, row-supplied |
| https://www.youtube.com/watch?v=9N6a-VLBa2I | Corey Schafer, JSON, student reference | 05 Sep 2026, row-supplied |
| https://realpython.com/python-lbyl-vs-eafp/ | LBYL against EAFP, trainer preparation | 03 Sep 2026, row-supplied |
| https://www.youtube.com/watch?v=q5uM4VKywbA | Corey Schafer, the CSV module | 03 Sep 2026, row-supplied |
| https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/ | Cleaning items, trainer preparation | 03 Sep 2026, row-supplied |

**Reachability, checked 13 Sep 2026:** `realpython.com` returned 403 to an automated request, which
is bot filtering rather than a dead page. Flagged for a human to open once. The rest returned 200.

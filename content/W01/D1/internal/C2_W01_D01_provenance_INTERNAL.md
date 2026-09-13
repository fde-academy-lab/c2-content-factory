# Provenance: Week 1 Day 1

**INTERNAL.** What this pack is built from, what was verified, and what was invented.

---

## The curriculum row

Built from `docs/curriculum/W1_Data_analysis_found.md`, the Monday 28 September 2026 row, read in
column order: the business scenario first, the thinking before any tool second, the technique third.

Client zero is `docs/07_Client_Zero.md` at **v2.2, locked 13 September 2026**.

---

## The data

Every file in `data/` is written by `data/generate_client_zero.py`, version `v0`, from seed
`20260928`. Nothing is hand-edited. Regenerate with:

```
python3 data/generate_client_zero.py --version v0 --out content/W01/D1/data --stem C2_W01_D01
```

The contract is asserted by `python3 data/generate_client_zero.py --contract`, which fails loudly
rather than shipping a dataset whose story no longer matches the row.

| Planted | Why, and where it is used |
|---|---|
| One corporate order of Rs 4,80,000 | The mean-against-median reveal in block 5. It carries 88 percent of the file's revenue. |
| One amount stored as the text `"4500"` | The block-4 `TypeError`, which is the day's first deliberate failure |

Both are TRAINER material and appear only in `trainer/` and here.

---

## Invented, and recorded as invented

The curriculum row quotes stakeholder figures in crore while the locked client zero file puts a
typical order between Rs 800 and Rs 3,000. Both are ground truth and they cannot both describe one
small file, so the world was extended rather than either source edited:

1. **Kalpa Retail sells to consumers and to businesses.** Consumer orders sit inside the locked
   Rs 800 to Rs 3,000 band. The `Business` segment sells in bulk to corporate buyers, resellers and
   institutional accounts, and those orders run from Rs 2 lakh upward. The locked file already says
   the band "describes the ordinary population rather than the whole file", and the row's own
   opening line, "one business customer can move an average", only makes sense if this is true.
2. **The Week 1 extract is Kalpa Retail India for two quarters**, not the whole group.
3. **Marketing's Rs 12 crore is the acquisition line of the multi-year growth plan**, not one
   quarter's spend.

None of the three contradicts anything in the locked file. All three are stated here so the next
person does not rediscover the arithmetic.

---

## Sources, with the date each was checked

| Link | Role | Checked |
|---|---|---|
| https://www.hackingthecaseinterview.com/pages/profitability-case-interview | The profitability framework and the revenue tree, trainer preparation | 13 Sep 2026, row-supplied |
| https://www.roadtooffer.com/blog/driver-tree | Driver trees, trainer preparation | 13 Sep 2026, row-supplied |
| https://mconsultingprep.com/profitability-case-framework | The framework, student reference | 13 Sep 2026, row-supplied |
| https://www.youtube.com/watch?v=daefaLgNkw0 | Corey Schafer, Dictionaries, student reference | 03 Sep 2026, row-supplied |
| https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode | Mean, median and mode, student reference | 03 Sep 2026, row-supplied |
| https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning | Codespaces with Jupyter, trainer preparation | 03 Sep 2026, row-supplied |

Links supplied on the curriculum row are the lock rather than a starting point, so none was replaced.

**Reachability, checked 13 Sep 2026 from this session:** every link above returned 200 to an
automated request except `hackingthecaseinterview.com`, which returned 403. A 403 to a script is
normally bot filtering rather than a dead page, so the link is kept and flagged for a human to open
once before it is read aloud in a room.

---

## The gates this pack passed

| Proof | Result |
|---|---|
| `deck_md_check` | PASS, both halves |
| `nb_check` | PASS, 3 notebooks, 18 checks passing |
| `distractor_audit` | PASS, 3 option sets, 18 items |
| `build_cheatsheet` | PASS, 7 panels, 1 diagram, 1 page |
| `verify.py` on the day folder | Recorded in the commit |

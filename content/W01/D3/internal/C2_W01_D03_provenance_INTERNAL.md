# Provenance: Week 1 Day 3

INTERNAL. Where every number, decision and link in the Wednesday pack came from, rebuilt on
29 September 2026 to the standard in `.claude/skills/day-pack-builder/references/the-standard.md`.

## The sources

| Source | What it fixed |
|---|---|
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 | The case, the five rungs, the four traps, the afternoon cases and the lab set |
| `docs/curriculum/W1_Data_analysis_found.md`, the Wednesday row | Scenario, thinking, outcomes, plants, interview anchors, references, Kahoot plan |
| `docs/07_Client_Zero.md`, v2.2, section 7 | Data version v2 and its witnesses |
| `docs/programme/calendar.md` | Wed 07 Oct 2026, W01/D3, teaching, module M1, no faculty block |
| `content/W01/D1` | The form of every family |
| `content/W01/D2/trainer/C2_W01_D02_day_sheet_TRAINER.md` | Tuesday's reported numbers: Retail-Plus 2.32 to 1.18, down 49.0 percent |

## The data

```
python3 data/generate_client_zero.py --version v2 --out content/W01/D3/data --stem C2_W01_D03
```

Rerun on 29 September 2026; the four files came out byte-identical to the committed ones. The CSV
holds 201 rows (the contract's 200 plus the near-duplicate), the JSON feed the first 120 rows cut
inside the 120th record, the vendor copy the header twice and the first 39 data rows, and the
take-home file the v2b sample.

## The plants, and where each is used

| Plant | Student files meet it as | Named only in |
|---|---|---|
| 14 duplicated Q1 rows | Aggregate counts and rupees (186 of 201, 14 in Q1, Rs 19,98,210); the rows found in empty cells | Day sheet |
| The amount `twelve` | "One amount does not convert"; the error read live in an empty cell | Day sheet, lab note |
| The missing status | "Status present on 200"; the three-way decision | Day sheet |
| The near-duplicate pair | Invented pairs INV-11 to INV-13 for the mechanism; the real pair found in an empty cell | Day sheet |
| The truncated JSON line | The error read live in an empty cell; 119 records recovered | Day sheet, lab note |
| The duplicated header | "40 rows, 39 convert, three segments"; found in an empty cell | Lab note |

## Decisions that depart from a source, and why

1. **The whole-record trap reports zero because the file line is in the key.** The spine says "a
   whole-record dedupe that reports zero duplicates". On the v2 file a plain whole-record dedupe
   finds 13 exact copies, not zero. Zero arises honestly when each record carries its file line,
   which round 1's rejects log teaches the room to attach, so round 1's fix becomes round 2's trap.
   The 13 is in the day sheet only.
2. **Round 3 carries two traps.** The spine's four traps across three rounds put the bulk-order trap
   and the counts-reconcile trap together in round 3, since both belong to rungs 4 and 5.
3. **The bulk order is Q2's largest order, KR-02186 at Rs 29,45,460.** v2 lists no bulk-order plant;
   the spine added this trap. The generator's Q2 anchor order is the only order that stands clear of
   the Business band's upper end, so it plays the part. Removing it gives Q2 Rs 1,57,54,540 and a
   17.1 percent drop.
4. **"Counts reconcile while rupees do not" is the keep-first-then-convert pass.** It reconciles
   201 = 185 + 16 and lands Rs 1,790 short, which is the value of the unreadable amount's copy.
5. **Anand's books are Rs 1,90,00,000 to the rupee.** The row quotes "1.9"; the exact figure is the
   generator's `Q1_CLEAN`, whose comment calls it what Finance's books say once the duplicates go.
6. **Revenue is booked value, every status.** Both 2.1 and 1.9 are totals over all statuses in the
   generator's contract, which matches Monday's booked definition. The decks say so on S27.
7. **Percentages are from unrounded ratios.** Retail-Plus falls 35.0 percent (26/22 against 40/22);
   Tuesday's -49.0 percent is quoted from Tuesday's day sheet.
8. **The practice lab's "second export with new defects" is the vendor copy**, since the take-home
   file is the second sample the standard assigns to the take-home.
9. **The afternoon deck has 14 body slides and 5 section openers**, 20 slides with the cover, against
   "about 20".
10. **The previous pack is replaced in full.** The build overwrote every old file whose name fits the
    new pack, and the requester had the last two removed with `git rm` on 29 September 2026:
    `notebooks/C2_W01_D03_01_reconciliation_STUDENT.ipynb`, whose saved outputs named planted
    records, and `demos/C2_W01_D03_identity_rule_STUDENT.html`.

## Invented, and recorded as invented

- Every record in notebook 02's mechanism cells (INV-01 to INV-03, INV-11 to INV-13), in the
  companion's four experiments, in the decision workbook and in the recovery extra.
- Every number in the round sets, the case briefs' distractors, the lab's problem 1 and the Kahoot,
  except where an item says it is the day's.
- The auditor as a person; the section 1a table names no auditor, so the role is unnamed.
- The companion's simulator holds no records; its 72 outcomes are totals computed from the v2 export
  by the script recorded below and embedded as numbers.

## Links, each with the date it was checked

| Link | Checked | Where used |
|---|---|---|
| https://realpython.com/python-csv/ | verified 03 Sep 2026, per the row | Study notes, take-home |
| https://www.youtube.com/watch?v=9N6a-VLBa2I | verified 05 Sep 2026, per the row | Study notes |
| https://docs.python.org/3/library/json.html | verified 03 Sep 2026, per the row | Study notes |
| https://realpython.com/python-lbyl-vs-eafp/ | verified 03 Sep 2026, per the row | Study notes, notebook 01 |
| https://automatetheboringstuff.com/3e/ | verified 03 Sep 2026, per the row | Study notes |

The row's links were not re-fetched in this session; they carry the row's verification dates.

## How the files were built, and the tool versions

| Family | Command |
|---|---|
| Notebooks | `python3 content/W01/D3/internal/C2_W01_D03_build_notebooks_INTERNAL.py` |
| Decks | `python3 scripts/build_deck.py <md> --footer ...`, rendered with `soffice --headless --convert-to pdf` |
| Companion | The page, then `python3 scripts/build_companion.py`; the simulator totals from `internal/C2_W01_D03_companion_totals_INTERNAL.py` |
| Workbook | `python3 content/W01/D3/demos/C2_W01_D03_build_decision_tool_TRAINER.py` |
| Cheat sheet | `python3 scripts/build_cheatsheet.py <md> --verified "29 Sep 2026"` |

Python 3.11.15, nbclient 0.11.0, nbformat 5.11.1, IPython 9.17.1, openpyxl 3.1.5, python-pptx 1.0.2,
LibreOffice 24.2.7.2, Chromium 141.0.7390.37, mermaid-cli 12.0.0 with fonts-crosextra-carlito
installed. mermaid-cli 12 rejects the `-w` flag that `scripts/build_deck.py` and
`scripts/build_cheatsheet.py` pass, which silently turns every slide diagram into code text; the
build ran through a session-local wrapper that drops `-w` and `-H`, and the fix belongs in the shared
scripts.

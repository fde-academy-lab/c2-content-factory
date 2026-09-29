# Provenance: Week 2 Day 5

**INTERNAL.** What this pack is built from, what was verified and when, every decision that departs
from a source, and everything invented.

---

## The sources

Built on 29 September 2026 from, in the ground-truth order CLAUDE.md sets:

1. The requester's brief for this session, which approved the Weeks 1 and 2 spine and set the
   Friday traps, the Excel-first bar and the LibreOffice facts below.
2. `docs/detailing/W01_W02_spine.md`, approved 29 September 2026: Friday's row in the Week 2 table,
   the campus day, and the afternoon-and-lab table.
3. `docs/curriculum/W2_Data_manipulation.md`, the Friday 16 October 2026 row, read in column order;
   `docs/programme/calendar.md` (W02/D5, teaching, M1, no faculty block; W03/D1 Build 1, online
   project introduction).
4. `docs/07_Client_Zero.md` at v2.2 with the GCC addendum of 28 September 2026: data version v4, the
   stakeholders, and the Build 1 seed (Dr Priya Menon; 5 percent growth against a plan of 18; five
   sub-problems).
5. `.claude/skills/day-pack-builder/references/the-standard.md` for form and volume, with
   `content/W01/D1` as the model for form.

## The data

Every file in `data/` comes from `data/generate_client_zero.py`; nothing is hand-edited.

| File | How it was written |
|---|---|
| `C2_W02_D05_customer_table_STUDENT.csv`, `C2_W02_D05_raw_export_STUDENT.csv` | The class exports, version v4, as the generator writes them (`python3 data/generate_client_zero.py --version v4 ...`); already in the folder at the start of the session and not regenerated |
| `C2_W02_D05_takehome_customer_table_STUDENT.csv`, `C2_W02_D05_takehome_raw_export_STUDENT.csv` | `demos/C2_W02_D05_build_takehome_data_TRAINER.py`, which loads the generator, sets its seed to 20261016 and calls its own `build_v4` and `_v4_exports`, because the generator has no take-home switch for v4 and this session may not edit it |

| Planted | Where it is used |
|---|---|
| The raw export at the payment grain: 400 instalment orders and 50 gateway retries, each on two rows | Round 1's trap (notebook 1, half one S12 to S17, the guided file, the deck pack's count-mode flip, the decision tool's Pivot tab defaults) |
| C-0170 absent from the clean table (Retail-Plus, 6 orders, Rs 21,740, rank 5 if present) | Round 1's harder variant (S18, an empty your-turn cell in notebook 1), round 2's live lookup (S28, an empty your-turn cell in notebook 2), the deck pack's Checks tab (which computes the gap but never the id), the debrief |
| The approximate match on C-0170 returning C-0169 (rank 50, Rs 8,580) | Round 2's live moment only; named here, in the day sheet and in the deck pack manifest |
| Take-home: C-0172 absent (Retail-Plus, 6 orders, Rs 14,740, rank 20 if present) | The take-home's self-check reconciliation line, which states that the table must tie, never the id |

C-0170 and C-0169 appear only in `trainer/`, in this file and in the INTERNAL recalc manifest.

## Decisions that depart from a source

| Decision | The source says | Why |
|---|---|---|
| The tree for both quarters is built from the raw export counted once per order | The row: "the chief of staff's three asks are all buildable from the clean export" | The clean customer table has no quarter column; its revenue is summed across April to September. Only the raw export carries order dates, so the quarter split has to come from it. This makes rung 2's fix the source of deliverable 1. |
| The double count is 450 orders, of which 50 are the double-paid retries | The row: "double-counts the fifty double-paid orders"; the spine: "a pivot double-counting the double-paid orders" | The raw export has one row per payment, so the 400 instalment orders also appear twice and carry most of the rupees. The day stages both: Remove Duplicates removes the 50 identical copies and leaves the total at Rs 39.41 crore, which becomes the round's second level. |
| The protect list is the top fifty Retail-Plus members by two-quarter revenue | Wednesday's row: the top fifty by Q2 revenue per segment | The customer table carries two-quarter revenue only. The two-quarter list has no tie at fifty (Rs 8,580 against Rs 8,520), so Wednesday's tie rule is referred to and not re-staged. |
| The lookup trap is taught on C-0195 in learner files | The row: the lookup trap fires on the one absent member | C-0195 is a Retail-Plus member with no orders in the two quarters, so an approximate match returns C-0194 (rank 15, Rs 16,740). It shows the mechanism on real data without naming the plant, and the room meets C-0170 live. |
| The front-page number is Q2 revenue against Q1, with the consumer trend beside it | The row names "one number on the front page with its trend" and leaves the number open | The growth review asks what moved, and Monday's warehouse numbers are the quarters. The company's monthly line is Business invoice timing, so the trend is the consumer line, labelled. |
| XLOOKUP is taught; every workbook computes with INDEX and MATCH | The row: "XLOOKUP for find this member" | LibreOffice 24.2.7.2 returns #NAME? for XLOOKUP (the requester, 29 September 2026, and reproduced in this session), and `xlsx_recalc.py` proves workbooks there. The one XLOOKUP cell in the deck pack (Protect!F8) carries the `_xlfn` prefix and is labelled as computed in Excel and not proved here. |
| The practice lab set lives in `exercises/practice/` and is audited directly | `verify.py` audits guided, unguided, kahoot and exercises folders | `distractor_audit.py` does not include `practice/` when given a folder, so the set was audited by file path. |
| Kalpa's chief of staff and the director are unnamed | The row names neither | Roles only, since no locked source names them. |

## Invented

| What | Where | Labelled |
|---|---|---|
| Members C-0401 to C-0409 and C-0501 to C-0508 | The decision tool's Lookup and Visible total tabs; the companion's experiments B and C | "invented" on the tab and the card |
| Three orders of Rs 1,000, Rs 2,000 and Rs 4,000 | The companion's experiment A | "invented rows" |
| A segment falling from Rs 500 to Rs 400 | The companion's experiment D | "invented numbers" |
| The app-channel export (Rs 20,000 of single orders, two instalment orders, one gateway copy) | The practice lab, problem 3 | "an invented export" |
| A regional team's sheet, including C-0888 and a Chennai filter | The practice lab, problem 4 | Framed as a scenario |
| The director's Rs 5,00,000 | The second case | A stated assumption |
| The draft cards "Revenue up 12 percent", "Retail-Plus lost 15 members", "Q2 orders 462, up from 538" | The practice lab, problem 2 | Draft cards; 462 and 538 are the real quarterly order counts, and 15 is the real fall in Retail-Plus customers (91 to 76) |

## Links, each with its check date

| Source | Checked | Used for |
|---|---|---|
| Microsoft Support, Create a PivotTable: https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576 | verified 29 September 2026 | Pivot steps; "PivotTables built on that data source need to be refreshed" |
| Microsoft Support, XLOOKUP: https://support.microsoft.com/en-au/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929 | verified 29 September 2026 | Exact match is the default; if_not_found is the fourth argument; #N/A when it is missing |
| Microsoft Support, VLOOKUP: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1 | verified 29 September 2026 | range_lookup defaults to approximate match when omitted |
| Microsoft Support, SUBTOTAL: https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939 | verified 29 September 2026 | 109 ignores rows hidden by hand; 9 includes them; filtered rows are excluded by both |
| Exponent, data analyst interview questions: https://www.tryexponent.com/blog/top-data-analyst-interview-questions | verified 13 Sep 2026 on the row; not re-fetched | Interview calibration |
| A video on pivots and lookups | to be found | The row supplies none and none was verified in this session |

## Checked in this session, and not verified in Excel

On LibreOffice 24.2.7.2, 29 September 2026: `SUM` over three rows with one hidden by hand returned 60
and `SUBTOTAL(109)` 40; `_xlfn.XLOOKUP` returned #NAME?; an approximate `VLOOKUP` for a missing
C-0120 among C-0118, C-0119 and C-0121 returned C-0119's value; `COUNTIFS` with a text criterion
`"<"&"C-0120"` compared text. Excel itself was not available, so these are not verified in Excel: the
menu names in the guided file beyond the PivotTable page, Excel reading the export's ISO dates as
dates, the `_xlfn.XLOOKUP` cell computing in Excel, and the charts in the deck pack rendering as drawn.

## Tool versions

Python 3.11.15; pandas 3.0.6; openpyxl 3.1.5; python-pptx 1.0.2; nbclient 0.11.0; LibreOffice
24.2.7.2; Playwright 1.63.0 with Chromium from `/opt/pw-browsers`; mermaid-cli 11.17.0, installed in
the session's scratch space and put first on `PATH` for the deck and cheat-sheet builds, because the
container's mermaid-cli 12.0.0 rejects the `-w` flag that `scripts/build_deck.py` passes and every
diagram fell back to text.

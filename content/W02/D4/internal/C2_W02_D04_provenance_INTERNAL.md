# Provenance: Week 2, Thursday

**INTERNAL.** Where every source, number and decision in this pack came from.

## Sources, in the ground-truth order

| Source | What it gave |
|---|---|
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 | The case, the five rungs, the four traps, the afternoon cases and the lab set; the campus day of two 180-minute blocks and the lab |
| `docs/curriculum/W2_Data_manipulation.md`, Thursday 15 October, all fifteen columns | The scenario and the senior analyst's challenge, the thinking, the agenda, the outcomes, the stop-before line, the client-zero plants, the exercises, the interview angle, the references and the Kahoot plan |
| `docs/programme/calendar.md` | W02/D4, Thu 15 Oct 2026, teaching, Module 1, no faculty block |
| `docs/07_Client_Zero.md`, v2.2 locked, section 1b and section 7 | Kalpa, the GCC frame, the stakeholders, data version v4 and its witnesses |
| `.claude/skills/day-pack-builder/references/the-standard.md` | The bar, the day's shape and the volume per family |
| `content/W01/D1` | The model for form: deck syntax, notebook rhythm, companion build, day sheet |

## The data

| File | How it was made |
|---|---|
| The v4 warehouse, `content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql` | Read only, loaded with `bash .devcontainer/load_warehouse.sh`: 1,000 orders, 340 customers, 1,428 payments, 136 exposure rows, 13 plan rows, 12 refunds |
| `data/C2_W02_D04_exposure_STUDENT.csv` | Written by `data/generate_client_zero.py --version v4`; unchanged in this build, and checked on 29 September 2026 to equal `build_v4()["campaign_exposure"]` row for row |
| `data/C2_W02_D04_takehome_{orders,customers,exposure}_STUDENT.csv` | `internal/C2_W02_D04_build_takehome_data_INTERNAL.py`, which imports the generator, sets `SEED = 20261015` and calls `build_v4()`; nothing in `data/` is edited |
| Every notebook's outputs | `internal/C2_W02_D04_build_notebooks_INTERNAL.py`, executing each notebook cold in its own folder through `scripts/nb_make.py`, against the running warehouse |

## The plants, and where each is used

| Plant | Used in | How the student files stay clean |
|---|---|---|
| 6 duplicated keys in the exposure feed (C-0001, C-0002, C-0003, C-0006, C-0007, C-0009) | Round 2's your-turn cell; the day sheet | The fan-out is shown on four invented customers (C-9001 to C-9004, labelled invented in the notebook, the deck notes and the study notes); the real merge is an empty your-turn cell; exercises use other numbers (a 250-row feed, Rs 52,300) |
| A customer whose months pivot wrongly by order index (the row's) | Round 3, S38 | No single customer is planted by the generator, so the order-index pivot is taught on Retail-Plus as a whole |
| Wednesday's falling members | Escalated case part 3 | The flag is computed across all segments (9 customers) and checked against Wednesday's LAG query without printing who |
| The take-home snapshot's own duplicates and gaps | The take-home | Named only in the day sheet; the self-check gives the numbers to reach and a diagnosis if one is missed |

## Everything invented, and why

- Customers C-9001 to C-9004 and their spends (Rs 12,400, Rs 8,600, Rs 5,100, Rs 1,900), and the
  companion's six reached customers (Rs 9,300, Rs 12,400, Rs 4,200, Rs 8,600, Rs 7,700, Rs 5,100):
  the fan-out mechanism without naming the plant.
- Kalpa Logistics' 500 accounts and 250-row feed, and the Rs 19,84,52,300 total, in the round 2 set:
  a trap that does not echo the plant.
- The run day of Monday 19 October 2026 for recency from the wall clock: the first Monday refresh
  after the session, pinned so the wrong number is exact; `pd.Timestamp.today()` on the build date,
  29 September, would have hidden the trap.
- The chief of staff's words on the last slide and in the pre-read are Friday's row, quoted.

## Decisions that depart from a source

| Decision | Why |
|---|---|
| The spine's trap "groupby dropping customers with no segment" is staged where a reach table starts from the feed and takes segment from the order rows | Every customer in the v4 warehouse has a segment, so the trap needs a table where segment can be missing; this one arises naturally and leaves 23 reached non-buyers out, which gives the trap a business consequence (100 against 82 percent) |
| "Last week's flags" are read as lapsed (60 days, as of the data's last date) and falling (Wednesday's LAG, all segments) | The row names "the two flags" without defining them; these two are the week's, one built on today's recency and one mirroring Wednesday |
| Spend counts every booked order, all statuses | Monday's warehouse tree and Friday's exported customer table both sum every order, so today's table reconciles with both |
| The row's agenda of seven items of 15 to 50 minutes is re-cut into the spine's day | The spine wins over the row; every agenda item keeps a home: ask (the ask), read_sql and groupby (round 1), merge (round 2), reshape (round 3), three tools (second case), unguided (escalated case), Kahoot (close) |
| The room writes the SQL first in the second case, then the trainer runs it through Python | The row's agenda item 5, kept inside the spine's 45-minute pairs slot |
| A practice set and a TA note are added | The spine's lab column; the row has none |
| Twelve interview questions: the row's five and seven case-style follow-ups, tagged | The standard's ten to twelve; follow-ups are the day's traps as an interviewer asks them |
| No decision workbook | The standard's volume table lists the companion only, Friday is the Excel day, and the old pack had none |
| The notebooks' `pd.Timestamp("2026-10-19")` replaces a live `today()` | Reproducible saved outputs; the comment says what it stands for |
| Old file names reused where the new artifact fits (`half1`, `01_customer_table`, `hands_on`, `three_tools`, `pick_tool`, `shapes`, `merge`, `pandas`, `quiz`, `tiered`, `preread`, `notes`, `brief`, `selfcheck`, `day_sheet`, `provenance`) | Every file of the old pack is replaced by a new one of the same name, so nothing below the new standard stays |

## Links, each checked on 29 September 2026

| Link | Check |
|---|---|
| https://pandas.pydata.org/docs/user_guide/10min.html | 200, "10 minutes to pandas, pandas 3.0.6 documentation" (verified 29 September 2026) |
| https://pandas.pydata.org/docs/user_guide/groupby.html | 200, "Group by: split-apply-combine" (verified 29 September 2026) |
| https://pandas.pydata.org/docs/user_guide/merging.html | 200, "Merge, join, concatenate and compare" (verified 29 September 2026) |
| https://pandas.pydata.org/docs/user_guide/reshaping.html | 200, "Reshaping and pivot tables" (verified 29 September 2026) |
| https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html | 200; the validate text quoted in the take-home read from it (verified 29 September 2026) |
| https://pandas.pydata.org/docs/whatsnew/v3.0.0.html | 200, "What's new in 3.0.0 (January 21, 2026)" (verified 29 September 2026) |
| https://pandas.pydata.org/docs/user_guide/index.html | 200, the row's link (verified 29 September 2026) |
| https://pgexercises.com/ | 200, the row's trainer link (verified 29 September 2026) |
| https://www.youtube.com/watch?v=txMdrV1Ut64 | YouTube oEmbed returned the title "Python Pandas Tutorial (Part 8): Grouping and Aggregating" by Corey Schafer; the page itself answered 429, so the content was not watched (verified 29 September 2026) |
| https://www.youtube.com/watch?v=Oo0Mio9Gx4A | oEmbed title "Python Pandas Tutorial: GroupBy + Pivot Tables + Merge", Coding with David; found by search, not used in a learner file, content not watched (verified 29 September 2026) |

## Tool versions the numbers and outputs came from

| Tool | Version |
|---|---|
| pandas | 3.0.6. The spine's defaults were checked on 3.0.5; on 3.0.6 on 29 September 2026, `pivot_table`'s `aggfunc` defaults to `"mean"`, `groupby`'s `dropna` to `True`, `merge`'s `validate` to `None` and `how` to `"inner"`, and `validate="one_to_one"` raises `pandas.errors.MergeError` with the message quoted in the pack |
| PostgreSQL | 16, from `/usr/lib/postgresql/16/bin` |
| SQLAlchemy, psycopg2-binary | 2.1.1 and the current wheel, installed in the build session |
| mermaid-cli | 11.17.0 for the decks and the sheet; the session's own `mmdc` 12.0.0 rejects the `-w` flag `scripts/build_deck.py` passes, so decks rendered code instead of diagrams until 11 was put first on the path |
| LibreOffice with Carlito | the render of both decks, looked at slide by slide |

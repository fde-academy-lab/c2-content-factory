# Provenance: Week 2, Tuesday. Booked against collected

**INTERNAL.** Where every number, decision and link in this pack came from.

## Sources, in the order they were read

| Source | What it gave the pack |
|---|---|
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 | The case, the five rungs, the three traps, the faculty-day shape (morning, then 45 for the case and 15 for the Kahoot) and the practice lab set |
| `.claude/skills/day-pack-builder/references/the-standard.md` | The form and the volume of every family |
| `docs/curriculum/W2_Data_manipulation.md`, Tue 13 Oct row and its IITGN column | The scenario, the thinking, the outcome, the plants, the interview anchors, the references and the Kahoot plan |
| `docs/programme/calendar.md` | W02/D2, Tue 13 Oct 2026, teaching, M1, W2-2 tentative |
| `docs/07_Client_Zero.md`, v4 row of section 7 | The planted witnesses |
| `content/W01/D1` | The model for the form of every artifact |

## The data

The warehouse is `content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql`, written by
`data/generate_client_zero.py --version v4` and loaded with `.devcontainer/load_warehouse.sh`. This
pack reads it and never writes it. Every number was measured on PostgreSQL 16.13 on 29 September
2026 with the warehouse loaded: customers 340, orders 1,000, payments 1,428, refunds 12,
campaign_exposure 136, plan_line 13.

The take-home book is written by `internal/C2_W02_D02_takehome_data_INTERNAL.py` into
`data/C2_W02_D02_takehome_STUDENT.sql`, which loads into its own schema, `takehome`, so it never
touches the warehouse tables. The generator has no second v4 sample; see the change requested below.

## The plants, and where each is used

| Plant | Value | STUDENT files | TRAINER files |
|---|---|---|---|
| Unpaid Q2 orders | 30 orders, Rs 17,54,930; KR-00577 and KR-00582 are the two large ones | None names them; the sql files and your-turn cells let the room find them | Day sheet, case key notebook |
| Gateway retries | 50 orders (22 on Q1, 28 on Q2), Q2 surplus Rs 20,750 | None | Day sheet, case key notebook |
| Orphan payments | 8, KR-90000 to KR-90007, Rs 24,680 | None | Day sheet, case key notebook |
| Instalments | 400 orders, 188 in Q2 (the fan-out's cause, not a plant) | Named as a mechanism; 216 Q2 multi-row orders shown in the round 3 trap | Day sheet |

The rule the STUDENT files follow: no count, id or rupee total of the unpaid, retried or orphan
records, and never the Q2 INNER order count beside the LEFT one. The INNER and WHERE traps are
shown exactly on the invented tiny tables; on Kalpa data they run live from the day sheet and as
your-turn cells with silent checks.

## Decisions that depart from a source

| Decision | Source it departs from | Why |
|---|---|---|
| Trap 3 filters `p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'` | The spine's check used `WHERE p.status = 'ok'` | The v4 payments table has no status column. The quarter cut-off is the filter a hurried analyst adds for "collected in Q2", and it drops the unpaid orders in the same way; checked on PostgreSQL 16.13 on 29 September 2026. |
| A fourth trap: `HAVING count(*) > 1` by order flags 216 Q2 orders | The row says HAVING COUNT(*) > 1 "lists the double posts" | In v4 it also lists the 188 legitimate instalment orders, so the row's own method is a plausible wrong list; the fix groups by order and instalment. |
| The fan-out's doubling comes mostly from instalments | The v4 witness line attributes 1,450 rows to the 50 retries | The 1,450 is 400 instalment orders plus 50 retries; the pack teaches the mechanism on the instalments and keeps the retries for the room to find. |
| "Collected" means cash with each payment counted once | The row does not define it | Anand's question and the platform lead's remark force the definition; the decks and notes state it before any number. |
| Traps 2 and 3 are shown exactly on invented tables in STUDENT files | The standard asks for the trainer's demonstration on Kalpa data | On Kalpa data both wrong numbers give the unpaid count away, which the row says the room must find; the trainer runs them live. |
| The afternoon deck carries 13 slides | The standard's afternoon deck of about 20 | A faculty day gives the trainer 60 minutes of the afternoon, with no second case and no interview drill. |
| No decision workbook | The standard's family list | The volume table sets the floor and does not list it; the companion carries the day's decision. |
| No refunds in the Q2 report | Anand's message mentions refunds | All 12 refund rows sit on Q1 orders; the take-home carries refunds inside its quarter. |

## Invented material

The two tiny tables (5 orders T-1 to T-5, 7 payments P-1 to P-7), labelled invented wherever they
appear; the companion's larger invented sample of 12 orders and 16 payments; the practice lab's
tables; the take-home book in its own schema.

## Links, each checked on 29 September 2026

| Link | Status |
|---|---|
| https://www.postgresql.org/docs/16/tutorial-join.html | 200, "2.6. Joins Between Tables" |
| https://www.postgresql.org/docs/16/queries-table-expressions.html | 200, "7.2. Table Expressions" |
| https://sqlbolt.com/lesson/select_queries_with_joins | 200, lesson 6 |
| https://sqlbolt.com/lesson/select_queries_with_outer_joins | 200, lesson 7 |
| https://sqlbolt.com/lesson/select_queries_with_nulls | 200, lesson 8 |
| https://pgexercises.com/questions/joins/ | 200 |
| https://www.pgtutorial.com/ | 200 |
| https://www.youtube.com/watch?v=aY7z4HcHm5M | oEmbed resolves: "SQL Joins Basics (Visually Explained)", Data with Baraa |

## Tool versions

PostgreSQL 16.13 (Ubuntu 16.13-0ubuntu0.24.04.1). Python 3 with psycopg2-binary and SQLAlchemy for
the notebooks. mermaid-cli 11.17.0 for the deck diagrams, because the container's mermaid-cli 12.0.0
rejects the `-w` flag that `scripts/build_deck.py` passes and falls back to printing the code.
LibreOffice for the render check, with fonts-crosextra-carlito installed.

## Changes requested of shared tools

1. `scripts/build_deck.py` passes `-w 2600` to mmdc, which mermaid-cli 12 no longer accepts, so every
   diagram silently prints as code; it should detect the version or drop the flag.
2. `data/generate_client_zero.py` has no second v4 sample for a take-home; a `v4b` book in its own
   schema would replace this pack's local builder.
3. `docs/07_Client_Zero.md` and the Tuesday row describe HAVING COUNT(*) > 1 as the double-post
   finder and attribute the 1,450 rows to the retries; both should name the instalments.

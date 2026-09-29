# Provenance: Week 2, Monday

INTERNAL. Where every fact, number and link in this pack came from, what was invented, and every
place the pack departs from a source.

## Sources, in the order they bind

| Source | What it gave this pack |
|---|---|
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 | The case, the rungs, the four traps, the faculty-day shape (trainer 180 plus 60, the block 120), the afternoon's case and the lab set, the Postgres checks of 29 September |
| `.claude/skills/day-pack-builder/references/the-standard.md` | The form and the volume of every family |
| `docs/curriculum/W2_Data_manipulation.md`, Monday row, all fifteen columns and the violet column | The scenario in Anand's words, the thinking, the subtopics, the trainer notes, the client-zero column, the exercises, the interview angle, the references, the Kahoot plan, the faculty session W2-1 |
| `docs/programme/calendar.md` and `data/programme/facts.yaml` | The date, Mon 12 Oct 2026; the module; the campus day; the faculty block's status, tentative |
| `docs/07_Client_Zero.md`, section 7, v4 | The warehouse's shape and its witnesses |
| `data/generate_client_zero.py`, last changed in commit ba6643f | Every number in the pack, through the warehouse it writes |
| `content/README.md` and `content/W01/D1` | The folder layout, and the model for form |

## The data

The warehouse file `data/C2_W02_D01_warehouse_v4_STUDENT.sql` is the generator's output, unchanged
and byte-identical to a fresh run of
`python3 data/generate_client_zero.py --version v4 --out <folder> --stem C2_W02_D01` (checked with
`cmp` on 29 Sep 2026). It loads 1,000 orders, 340 customers, 1,428 payments, 136 exposure rows, a
13-row plan line and 12 refunds through `bash .devcontainer/load_warehouse.sh`.

Every number in the pack comes from a query in `sql/` or `exercises/solutions/` run on that load;
the notebooks, the decision workbook's builder and the checks in each notebook read the warehouse
live, so a changed warehouse fails a check rather than shipping a stale number.

## The plants, and where each is used

| Planted in v4 | Used today | Where it is named |
|---|---|---|
| The warehouse holds 1,000 orders where the extract held 186 (the generator's Monday witness) | Round 1, the book checked against Week 1 | The row's own scenario states "one thousand orders" to learners, so the count is in STUDENT files; the day sheet names it as the witness |
| The bulk orders, KR-00667 and KR-00124 | Only if a learner sorts by amount | Day sheet only; no learner file lists the largest orders, and the typical-order slides quote the mean and median only |
| Instalments, gateway retries, unpaid orders, orphan payments | No | Day sheet only, marked "do not raise" |
| The tie at the fiftieth Retail-Plus position, the three falling members | No | Day sheet only |
| Duplicate exposure keys, the unused campaigns table | No; the schema read lists the tables without comment | Day sheet only |

The monthly Retail-Plus chart in notebook 3's Depth section shows order counts per month (72, 72,
71, 47, 47, 46) and names no member, so it does not reveal the falling-spend members.

## Invented, and labelled invented wherever it appears

- The three values 100, NULL and 200 for the AVG mechanism (block `r3_invented_null`, notebook 3,
  slide S37, the cheat sheet, the companion's experiment B). The warehouse holds no NULL in any
  column, so the book's NULLs come from a `CASE` with no `ELSE`.
- The companion's four experiments: 7 orders from 4 customers, three members' spend, six order rows
  from four buyers and five members, and a six-row table for the reload.
- The "reload" in round 1: an `UPDATE` that rewrites two rows with their own values inside a
  transaction that is rolled back. It is a real run on the warehouse, and the warehouse is left as it
  was; the scenario of an overnight reload is invented to motivate it.

## Decisions that depart from a source

| Decision | The source | Why |
|---|---|---|
| The five rungs are the three rounds, the escalated case and the lab's channel tree | The spine lists four rungs for Monday | The prompt fixed five rungs across the rounds, the case and the lab; the fifth is the row's "every segment and channel" |
| The afternoon holds no second case and no 30-minute interview drill | The standard's afternoon | The spine's faculty-day shape: the escalated case (45) and the Kahoot (15), then the block; the interview questions move into each round's close, the notes and the day sheet |
| The escalated case's 45 minutes are split brief 5, build 30, debrief 10 | The standard runs the debrief as its own 15 | The faculty day leaves 45 for the case; the debrief of wrong answers is kept inside it |
| One lookup line, `JOIN customers USING (customer_id)`, in rounds 1 to 3 | The row's stop-before: joins are Tuesday's | The segment lives on the customer, and the row's own agenda asks for revenue per segment and a CTE per quarter "joined on segment"; each order has one customer, so the row count is shown unchanged and the join is named as tomorrow's topic |
| The round-1 LIMIT trap is shown with a reload inside a rolled-back transaction | The spine: "two learners, two answers" | Sixty learners on identical Codespaces get identical unordered rows, so a second learner's different answer is demonstrated as the analyst's rerun after a reload, which is the same mechanism |
| The take-home runs on the warehouse with a new question (Retail-Plus by city) | The standard: a second generated sample with its own plants | The generator writes no second Week 2 sample, and `data/` is not this session's to edit; the take-home's own discovery is that half the city cells are thin |
| The row's tie "in the top ten" | The generator puts the tie at the fiftieth Retail-Plus position | Not today's material; the day sheet records the conflict for Wednesday's session |
| Anand is "CFO" | `docs/07_Client_Zero.md` section 1a calls him finance controller | The row, which binds above the lock, calls him "the CFO, Anand"; this pack follows the row |
| Existing file names kept for rebuilt artifacts | Topic names chosen fresh | The old pack's files could not be deleted in this session, so each was overwritten under its name: `whiteboards/..._execution_order_` holds the board work and the first-use walkthrough, `demos/..._execution_order_` the simulator, and `unguided/..._row_count_` and `_clause_order_` the round 1 and round 2 sets. The SQL files were then renamed into round order on request: 01 to 03 the three rounds, 04 the case, 05 the lab and 06 the take-home; round 1's file was renamed `_01_warehouse_` after it, so each round's SQL file carries its notebook's name |
| One cheat sheet, no visual sheet and no gap variant | The manifest's section 10 | The standard and the W01 model ship one sheet with its PDF |

## Links, each checked on 29 Sep 2026

| Link | Where | What was checked |
|---|---|---|
| https://www.postgresql.org/docs/16/queries-limit.html | Solutions, notes | Checked 29 Sep 2026: returns 200; states that without an ORDER BY giving a unique order, LIMIT returns "an unpredictable subset of the query's rows" |
| https://www.postgresql.org/docs/16/functions-aggregate.html | Solutions, notes | Checked 29 Sep 2026: returns 200; aggregates other than count work on non-null input values, and sum of no rows is null |
| https://www.postgresql.org/docs/16/queries-with.html | Solutions, notes | Checked 29 Sep 2026: returns 200 |
| https://www.postgresql.org/docs/16/functions-math.html | Solutions, notes | Checked 29 Sep 2026: returns 200; "for integral types, division truncates the result towards zero", 5 / 2 is 2 |
| https://sqlbolt.com/ and its lessons 1 to 6 and 12 | Take-home, pre-read, notes | Checked 29 Sep 2026: returns 200; lesson titles read from the index: lesson 4 is filtering and sorting, lesson 5 the review, lesson 6 joins, lesson 12 order of execution |
| https://www.pgtutorial.com/postgresql-tutorial/postgresql-group-by/ | Notes | Checked 29 Sep 2026: returns 200, titled "PostgreSQL GROUP BY" |
| https://pgexercises.com/questions/aggregates/ | Extras | Checked 29 Sep 2026: returns 200 |
| https://learn.microsoft.com/en-us/azure/postgresql/extensions/vs-code-extension/quickstart-connect | Board work, first-use walkthrough | Checked 29 Sep 2026: returns 200; the connect steps, the connection fields and the run shortcut were read from it. The extension's screens were not run in this session, and the walkthrough says so |
| https://www.youtube.com/watch?v=7mz73uXD9DA | Notes | Checked 29 Sep 2026: oEmbed returns "SQL for Data Analytics - Learn SQL in 4 Hours" by Luke Barousse. Its chapter list could not be read, so which of today's topics it covers is not verified; a video for CTEs specifically is to be found |

The row's own references (pgtutorial.com, the PostgreSQL tutorial, SQLBolt, PostgreSQL Exercises)
carry 05 Sep 2026 on the row; each one used here was checked again on 29 Sep 2026.

## Tool versions the numbers and outputs came from

PostgreSQL 16.13; Python 3.11.15; pandas 3.0.6; psycopg2 2.9.13; SQLAlchemy 2.1.1; nbclient 0.11.0;
nbformat 5.11.1; openpyxl 3.1.5; python-pptx 1.0.2; LibreOffice 24.2.7.2; Chromium 141.0.7390.37;
mermaid-cli 11.17.0 for every rendered diagram (the image's mermaid-cli 12.0.0 rejects the `-w` flag
`scripts/build_deck.py` passes, so version 11 was installed in the session's scratch space and put
first on the path for the builds).

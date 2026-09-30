# Provenance: Week 2, Monday

INTERNAL. Where every fact, number and link in this pack came from, what was invented, every place
the pack departs from a source, and the depth loop that checked it.

## Which sources bound the pack, in the order they bind?

| Source | What it gave this pack |
|---|---|
| The requester, 30 September 2026 | The day prompt in `prompts/week_revamp_W02_W03.md`, section 3, with the Week 2 Monday fills: the five rungs as chapters with a sixth on the run that reproduces itself, the four traps, the options (export, query or view; subquery, CTE or temporary table), queries shipped as `.sql` files run through `kit.sql`, the AVG trap on an invented table where the warehouse has no NULL, and the faculty-day shape |
| `data/programme/facts.yaml` | The decisions `chapter-standard`, `four-domains`, `question-ladder`, `self-contained`, `humanizer`, `opus-max` and `anand-finance-controller`; the campus day; the faculty block W2-1 as tentative |
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 | The case, the rungs, the four traps, the faculty-day paragraph (trainer 180 plus 60, the block 120), the afternoon's escalated case and the lab set, the Postgres checks of 29 September |
| `docs/curriculum/W2_Data_manipulation.md`, Monday row, all fifteen columns and the violet column | The scenario in Anand's words, the thinking, the subtopics, the trainer notes, the client-zero column, the exercises, the after-class tasks, the interview angle, the references, the Kahoot plan, the faculty session W2-1 |
| `docs/programme/calendar.md` | The date, Mon 12 Oct 2026; the module; the faculty block W2-1 (tentative) |
| `docs/07_Client_Zero.md`, sections 1a, 1b and 7 (v4) | The people, the GCC frame and the warehouse's shape and witnesses |
| `data/generate_client_zero.py` | Every number in the pack, through the warehouse it writes |
| `.claude/skills/day-pack-builder/references/the-standard.md` and `content/README.md` | The form and volume of every family, and the folder layout |
| The Week 1 packs on main and the Week 1 Thursday recheck on `origin/w01-d4-v3` | The chapter form, the v3 deck form (the map slide titled "Answered in ...", the close answering every smaller question) and the day sheet's form |
| The retail dossier, `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md` | The tree's definitions, linked for depth and never retold |

## Where does the data come from, and how is it proved?

The warehouse file `data/C2_W02_D01_warehouse_v4_STUDENT.sql` is the generator's output, unchanged:
a fresh run of `python3 data/generate_client_zero.py --version v4 --out <folder> --stem C2_W02_D01`
writes a byte-identical file (md5 951e4e8906ae1aaec38df82caaa011b2, checked 30 Sep 2026). It loads
1,000 orders, 340 customers, 1,428 payments, 136 exposure rows, a 13-row plan line and 12 refunds
through `bash .devcontainer/load_warehouse.sh`.

Last week's extract, `data/C2_W02_D01_week1_orders_STUDENT.csv`, is byte-identical to a fresh
`python3 data/generate_client_zero.py --version v3 --out <folder> --stem C2_W02_D01` orders file and to
`content/W01/D4/data/C2_W01_D04_orders_STUDENT.csv` (md5 ac5ee7e6b1c5afd3f509966aad1243ed): the 186
cleaned orders behind the note Meera accepted. Chapter 2 recomputes Week 1's numbers from it.

Every number in the pack comes from a named block of a `.sql` file in `sql/` run on that load, or
from the case notebooks' queries; the notebooks read the warehouse live and assert their numbers, so
a changed warehouse fails a check rather than shipping a stale number. The notebooks are written and
executed cold in their own folder by `internal/C2_W02_D01_build_notebooks_INTERNAL.py`.

The take-home's second book, `data/C2_W02_D01_takehome_STUDENT.sql`, is written by
`python3 content/W02/D1/internal/C2_W02_D01_takehome_data_INTERNAL.py` from seed 20261012 (md5
226c85abf7b9429873a3ed4421207a2a, byte-identical on two runs, checked 30 Sep 2026). It creates the
schema `takehome` with 126 members and 362 orders of Kalpa Retail East, an invented region, and
leaves the warehouse's public tables untouched (seven before and after the load). The script loads
the file and asserts every number the self-check prints; `--check` rebuilds it in memory and
compares. Its three witnesses (integer ratios equal in both quarters, twelve Retail-Plus members who
stopped after Q1, quarters added past the members) are named in the day sheet only.

## Which plants exist, and where is each used?

| Planted in v4 | Used today | Where it is named |
|---|---|---|
| The warehouse holds 1,000 orders where last week's extract held 186 (the generator's Monday witness) | Chapters 1 and 2 | The row's own scenario states "one thousand orders" to learners, so the count is in STUDENT files; the day sheet names it as the witness |
| The two largest bulk orders, KR-00667 (Rs 1,98,57,600, Q2) and KR-00124 (Rs 1,22,77,440, Q1) | Only if a learner sorts by amount | Day sheet only; no learner file lists the largest orders' ids or amounts. Learner files say Business books about 99 percent of the rupees, a fact of the world rather than a plant |
| 450 orders with two payment rows (400 instalments, 50 gateway retries), 30 delivered orders never paid, 8 orphan payments | No | Day sheet only, marked "do not raise" |
| The tie at the fiftieth Retail-Plus position, the three members whose spend falls month on month | No | Day sheet only |
| 6 duplicated keys in the exposure table, the unused campaigns table | No; chapter 1's schema read lists the tables without comment | Day sheet only |

The extract's 69 customers all bought in both quarters, which chapter 2 finds by counting; the pack
says what the count shows and never says how the generator drew the file.

## Which decisions depart from a source, and why?

| Decision | The source | Why |
|---|---|---|
| Six chapters from the spine's four rungs plus the requester's sixth | The spine lists four rungs for Monday | The fills fixed five chapters from the rungs (the fourth rung, the suite the analyst audits, became chapters 4 and 5: the branches with the AVG trap, and the tie-outs) and a sixth on the run that reproduces itself |
| A trap in chapter 2 and one in chapter 5 beyond the spine's four | The spine names four traps for Monday | The standard asks every chapter to stage one. Chapter 2's (a matching total read as a matching story) and chapter 5's (customer counts added across quarters) teach no later day's trap: Tuesday's are joins, Wednesday's windows and ties, Thursday's pandas, Friday's Excel |
| The afternoon holds chapter 6, the escalated case's parts 1 and 2 and the Kahoot | The standard's 180-minute afternoon | The spine's faculty-day shape and the fills: the trainer keeps 60 minutes and the tentative block takes 120; parts 3 to 5, the debrief of wrong answers, the second case and the interview drill move to the lab and the take-home |
| One lookup line, `JOIN customers c USING (customer_id)`, from chapter 3 on | The row's stop-before: joins are Tuesday's | The segment lives on the customer, and the row's own agenda asks for revenue per segment and a CTE per quarter "joined on segment"; each order has one customer, so no row count changes, and every file names the line as a lookup and joins as Tuesday's topic |
| The LIMIT trap shown with a reload inside a rolled-back transaction | The spine: "two learners, two answers" | Sixty learners on identical Codespaces usually receive the same unordered five, so the second answer is demonstrated as the analyst's rerun after a reload, which is the same mechanism |
| The morning deck's cover quote ends at "Nothing a person can mistype." | The row's full message | The full message printed three lines and pushed the cover's chapter strip into its footer; slide S2 carries the message in full |
| The take-home runs on a second book written inside the day folder | The standard: a second sample from `data/generate_client_zero.py` | The shared generator writes no second Week 2 sample and `data/` is not this session's to edit, so a seeded script in `internal/` writes one into its own schema; the shared-tool change to ask for is a `--version v4-takehome` in the generator |
| The Kahoot's return question asks for a fair comparison in words the room used on Week 1 Thursday | The row: "say in one line what a fair comparison would need" | Kahoot items are four-option choices, so the one line became the key: like for like, each segment apart or a held-back group |

## What is invented, and labelled invented wherever it appears?

- The three values 100, NULL and 200 for the AVG mechanism (notebook 4's block `c4_invented_null`,
  morning S56's notes, the cheat sheet and the companion). The warehouse holds no NULL in any
  column, so chapter 4's NULLs come from a CASE with no ELSE.
- The overnight reload in chapter 6 and the escalated case's part 5: an `UPDATE` that rewrites rows
  with their own values inside a transaction that is rolled back. It is a real run on the warehouse,
  which is left as it was; the story of an overnight reload is invented to motivate it. Chapter 1's
  depth section renames a column and saves a view inside a rolled-back transaction the same way.
- Anand's analyst's words on the afternoon cover and chapter 6's first cell, Anand's words opening
  chapters 2 and 5, and the head of Retail-Plus's words opening chapter 4 are written for the pack in
  the voices `docs/07_Client_Zero.md` section 1a gives these people; the row's own words open the
  day and the escalated case.
- The take-home's second book, Kalpa Retail East, its three cities and every row in it (see the data
  section above); the brief says the region is invented.
- The exercise sets' invented rows, each labelled invented in its file: chapter 1's eight cancelled
  orders, chapter 2's items 3 and 4, chapter 3's cities, chapter 4's item 4 and chapter 6's item 4
  order ids.

## Which links does the pack print, each checked on the day it entered?

Every link below was fetched on 30 September 2026 by the session's source check, which quoted each
fact against its page; a claim the check corrected is noted beside it.

| Link | Where the pack uses it | What was checked, 30 Sep 2026 |
|---|---|---|
| https://ypfsresourcelibrary.blob.core.windows.net/fcic/YPFS/JPMorgan%20Management%20Task%20Force%20Regarding%202012%20CIO%20Losses%201-16-13.pdf | Chapter 1: notebook 1, morning S10, the notes | Checked 30 Sep 2026: The task force report of 16 January 2013 (an archival copy in the Yale Program on Financial Stability library; JPMorgan's own copy returns 404). Page 124: "the model operated through a series of Excel spreadsheets, which had to be completed manually, by a process of copying and pasting data from one spreadsheet to another" (CIO's new VaR model). Page 7: cumulative year-to-date losses through 30 June 2012 "had grown to approximately $5.8 billion" |
| https://www.sec.gov/Archives/edgar/data/0000019617/000001961713000077/a8-k.htm | Provenance only | Checked 30 Sep 2026: JPMorgan's Form 8-K of 16 January 2013, which names the task force report and its date |
| https://web.archive.org/web/20260809070448/https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70 | Chapter 2: notebook 2, morning S23, the notes | Checked 30 Sep 2026: The Airbnb Tech Blog, "How Airbnb achieved metric consistency at scale", 30 April 2021; the live Medium page returns a bot wall, so the archived copy of the same URL was read. The quote matches word for word; the story is from years before the post. Corrected: the title's case |
| https://www.eternal.com/blog/q1fy27 | Chapter 3: notebook 3, morning S36, the notes | Checked 30 Sep 2026: Eternal's Q1FY27 shareholders' letter, 22 July 2026: B2C NOV up 54% year on year to INR 31,120 crore; food delivery 20%+ (INR 10,769 crore), quick commerce 86% (INR 17,132 crore), going-out 60% (INR 3,218 crore) |
| https://handbook.gitlab.com/handbook/enterprise-data/platform/sql-style-guide/ | Chapter 4: notebook 4, morning S50, the notes | Checked 30 Sep 2026: "Prefer CTEs over sub-queries as CTEs make SQL more readable and are more performant", quoted with the cut marked; "perform a single, logical unit of work"; "a brief description of what's going on". Corrected: the first quote's cut is now marked |
| https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm | Chapter 5: notebook 5, morning S62, the notes | Checked 30 Sep 2026: Meta's Form 10-K for 2025, filed 29 January 2026: DAP 3.58 billion on average for December 2025 (page 61); the daily active person definition, "who visited at least one of these Family products"; "counting such group of accounts as one person" (pages 4, 28, 65) |
| https://web.archive.org/web/20231125074707/https://www.slideshare.net/Hadoop_Summit/whoops-the-numbers-are-wrong-scaling-data-quality-netflix | Chapter 6: notebook 6, afternoon S4, the notes | Checked 30 Sep 2026: Michelle Ufford, "Whoops, The Numbers Are Wrong! Scaling Data Quality @ Netflix", DataWorks Summit, San Jose, 13 June 2017 (the agenda, archived). Slides 22 to 41: write, audit, publish; RowCount 17240 with NullCount 17240 beside RowCount 16135 with NullCount 21; the row-count rules fail the job and the null-count rule warns. Corrected: the pack no longer says that batch was stopped |
| https://www.youtube.com/watch?v=fXHdeBnpXrg | The notes' reading path | Checked 30 Sep 2026: The talk's video, "WHOOPS, THE NUMBERS ARE WRONG! SCALING DATA QUALITY @ NETFLIX", DataWorks Summit, confirmed by oEmbed |
| https://www.postgresql.org/docs/16/functions-math.html | Chapter 3's trap, notes, cheat sheet | Checked 30 Sep 2026: "for integral types, division truncates the result towards zero"; 5 / 2 is 2 |
| https://www.postgresql.org/docs/16/functions-aggregate.html | Chapter 4's trap, notes, cheat sheet | Checked 30 Sep 2026: avg "Computes the average (arithmetic mean) of all the non-null input values"; "sum of no rows returns null, not zero as one might expect" |
| https://www.postgresql.org/docs/16/queries-order.html | Chapter 6's trap, notes | Checked 30 Sep 2026: Rows without ORDER BY come back "in an unspecified order", which "will depend on the scan and join plan types and the order on disk, but it must not be relied on" |
| https://www.postgresql.org/docs/16/queries-limit.html | Chapter 6's trap, notes, cheat sheet | Checked 30 Sep 2026: Without an ORDER BY that constrains the rows into a unique order, "you will get an unpredictable subset of the query's rows" |
| https://www.postgresql.org/docs/16/queries-with.html | Chapter 4, notes | Checked 30 Sep 2026: WITH queries "are normally evaluated only once per execution of the parent query"; a side-effect-free one referenced once can be folded into the parent query |
| https://www.postgresql.org/docs/16/tutorial-agg.html | Chapter 3, notes | Checked 30 Sep 2026: "WHERE selects input rows before groups and aggregates are computed ..., whereas HAVING selects group rows after groups and aggregates are computed" |
| https://www.postgresql.org/docs/16/sql-createtable.html | Chapter 4's options, notes | Checked 30 Sep 2026: "Temporary tables are automatically dropped at the end of a session, or optionally at the end of the current transaction" |
| https://www.postgresql.org/docs/16/sql-select.html | Notes, board work | Checked 30 Sep 2026: The order a SELECT is processed in, and that an output column's name cannot be used in WHERE or HAVING |
| https://sqlbolt.com/ and its lessons 1, 4, 10, 11 and 12 | Take-home, pre-read, notes | Checked 30 Sep 2026: The index and lesson pages load; lesson 4 covers ORDER BY and LIMIT, lessons 10 and 11 aggregates and HAVING, lesson 12 the order of execution; the index lists a review page where lesson 5 would be |
| https://www.pgtutorial.com/ and its GROUP BY, HAVING, LIMIT and CTE pages | Notes | Checked 30 Sep 2026: Each loads |
| https://pgexercises.com/questions/aggregates/ | Extras | Checked 30 Sep 2026: Loads |
| https://learn.microsoft.com/en-us/azure/postgresql/development/vs-code-extension/quickstart-connect-query | Board work's first-use walkthrough | Checked 30 Sep 2026: "Quickstart: Connect and query PostgreSQL", last updated 28 July 2026: the extension ms-ossdata.vscode-pgsql (version 1.30.1), Ctrl+Alt+D to open the view, Add New Connection, the parameters, Save & Connect, Ctrl+Shift+E to run. The page does not mention Codespaces, so the pack marks the Codespace steps not verified |
| https://www.youtube.com/watch?v=dCNjUOc1cBY, ...=QNfnuK-1YYY, ...=BHwzDmr6d7s, ...=ZnAydTqCtFU | The notes' reading path | Checked 30 Sep 2026: One video per new topic, each confirmed by oEmbed: HAVING against WHERE (Alex The Analyst), the WITH clause (techTFQ), the execution order (ByteByteGo), LIMIT (Alex The Analyst). The Alex The Analyst files are MySQL: PostgreSQL rejects an alias in HAVING and the LIMIT 3,2 form, and the notes say so |


## Which tools made the numbers and outputs?

PostgreSQL 16.13; Python 3.11.15; pandas 3.0.6; psycopg2-binary 2.9.13 (installed in this session with
`pip install psycopg2-binary`, since the restarted container lacked it); nbclient 0.11.0; nbformat
5.11.1; openpyxl 3.1.5; python-pptx 1.0.2; LibreOffice 24.2.7.2 with Carlito (installed in this session
with `apt-get install fonts-crosextra-carlito`); mermaid-cli 12.0.0, whose missing `-w` flag
`scripts/build_cheatsheet.py` works around with `--size`. Both decks were built with
`scripts/build_deck.py` and rendered through LibreOffice to PDF and PNG, and every slide was looked at.

## The depth loop, 30 September 2026

The builder's passes 1 to 3 and the humanizer's read are logged here; the two reviewer passes are
logged below as they run.

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every chapter built from the row, the spine and the domain, in the chapter order? | The previous session's six notebooks held the spine's four rungs as chapters 1 to 4 with chapter 4's second half and chapter 5 carrying the suite the analyst audits, and chapter 6 the run that reproduces itself; chapter 2's list of smaller questions named a question no heading asked | Chapter 2 now asks six questions, each under its own heading, the last being the line Anand's sheet carries about last week's note; the decks, exercises, notes, board work, cheat sheet, day sheet and take-home were built chapter by chapter from the notebooks |
| 2. Domain | The builder | Could a learner who has never worked in a business say, for every chapter, who asks, why the metric matters, what a wrong number costs and which real company faces the same question? | Every notebook's first cell and every deck chapter's map and need slides name who asks, the metric and what a wrong number costs; the real companies' facts had not been checked in this build | A source check fetched every company fact on 30 September 2026 and corrected three: Airbnb's title case and the story's age, GitLab's quote with its cut marked, and Netflix's batch, which the talk shows raising a warning |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with two or more options, a sizing and the best-fit call with what would change it, and is the code its last mile? | Each chapter sizes two to four options on the warehouse before its first build step, and each deck chapter carries the options slide, the switch slide and a picture of the thinking before its code | Nothing to change in the notebooks; the decks were written to the same order |
| Humanizer's read | The builder, and each builder agent on its own files | Does every prose file read as a person wrote it? | The tic scanner was clean on every markdown file and on the notebook build script; the read found staged contrasts only where both halves carry a number, and one fragment stack in a deck note | The fragment stack rewritten; the notes' length kept, since every section carries a worked case and the Week 1 Thursday model runs to the same length |


## The proof run

To be recorded after the reviewer passes and the fixes.

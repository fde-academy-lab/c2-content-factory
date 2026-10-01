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

The warehouse file `data/C2_W02_D01_warehouse_v4_STUDENT.sql` is the generator's output with its
header cut to two lines. A fresh run of `python3 data/generate_client_zero.py --version v4 --out
<folder> --stem C2_W02_D01` writes md5 951e4e8906ae1aaec38df82caaa011b2, whose lines 2 to 4 named the
loader as `psql -f data/warehouse_v4.sql`, which does not exist, and described why payments carry no
foreign key and the exposure table no primary key: Tuesday's orphan payments and Thursday's re-sent
customers, two plants a learner file must not name. Those three lines were replaced with one, using
`sed -i '2,4c\-- Written by data/generate_client_zero.py --version v4, and loaded by: bash
.devcontainer/load_warehouse.sh'`; line 1 and every line from the generator's line 5 onward are
unchanged (checked by diff on 1 Oct 2026), and the shipped file's md5 is
a3977a5ad1021474ecc5adf68f3c97cd. It loads 1,000 orders, 340 customers, 1,428 payments, 136 exposure
rows, a 13-row plan line and 12 refunds through `bash .devcontainer/load_warehouse.sh`.

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
compares without touching any database, and `--check --load` also loads it and asserts. Its three witnesses (integer ratios equal in both quarters, twelve Retail-Plus members who
stopped after Q1, quarters added past the members) are named in the day sheet only.

## Which plants exist, and where is each used?

| Planted in v4 | Used today | Where it is named |
|---|---|---|
| The warehouse holds 1,000 orders where last week's extract held 186 (the generator's Monday witness) | Chapters 1 and 2 | The row's own scenario states "one thousand orders" to learners, so the count is in STUDENT files; the day sheet names it as the witness |
| The two largest bulk orders, KR-00667 (Rs 1,98,57,600, Q2) and KR-00124 (Rs 1,22,77,440, Q1) | Only if a learner sorts by amount | Day sheet only; no learner file lists the largest orders' ids or amounts. The notes' chapter 3 says Business books 99 percent of the rupees, a fact of the world rather than a plant; the second case's brief no longer says it, since it announced that case's key |
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
| The exercise index names no channel for posting letters | The pedagogy reviewer asked for one | The conflict `exercise-channel` in `data/programme/facts.yaml` is open (the spec of 13 September against the handover of 27 September), and a STUDENT file never states an open fact, so the index says the trainer names where each line goes |
| The interview drill holds thirteen questions across two self-study slides | The row's interview angle and the earlier deck's ten | The decks ask three more in their chapter closes (the count variants, "your total matches", CTE against subquery), and the standard wants one list answered in full in the notes and in one breath on the day sheet |
| Chapter 6's crux line orders every audit sample, where it said every list, and ties at a LIMIT cut are not explained | Wednesday's row: ties ranked the same, and the top fifty | The line now says what Monday teaches, a repeatable sample; why a shared value breaks a cut is Wednesday's question |
| The escalated case's item 13 is a reading of the two trees, so the case has four design items | The earlier label, design | It asks the learner to read printed ratios, which is no sizing, switch or second route |

## What is invented, and labelled invented wherever it appears?

- The three values 100, NULL and 200 for the AVG mechanism (notebook 4's block `c4_invented_null`,
  morning S56's notes and the companion's experiment B). The warehouse holds no NULL in any
  column, so chapter 4's NULLs come from a CASE with no ELSE.
- The overnight reload in chapter 6 and the escalated case's part 5: an `UPDATE` that rewrites rows
  with their own values inside a transaction that is rolled back. It is a real run on the warehouse,
  which is left as it was; the story of an overnight reload is invented to motivate it. Chapter 1's
  depth section renames a column and saves a view inside a rolled-back transaction the same way.
- Anand's analyst's words on the afternoon cover and chapter 6's first cell, Anand's words opening
  chapters 2 and 5, the escalated case and the second case, and the head of Retail-Plus's words
  opening chapter 4 are written for the pack in the voices `docs/07_Client_Zero.md` section 1a gives
  these people; the row's own words open the day.
- The take-home's second book, Kalpa Retail East, its three cities and every row in it (see the data
  section above); the brief says the region is invented.
- The exercise sets' invented rows and scales, each labelled invented in its file: chapter 1's eight
  cancelled orders; chapter 2's three changed orders in item 2 (Rs 500 more, Rs 300 less, Rs 200
  less) and its items 3 and 4; chapter 3's cities; chapter 4's book of 2 crore orders and twelve
  Monday queries in item 2 and its five members in item 4; chapter 6's two bad runs in item 2 (a
  day's amounts left empty, a ratio divided as whole numbers) and its order ids in item 4.
- The escalated case's item 15 prints Rs 16,03,44,040, the faulty fingerprint a filter that let the
  163 cancelled orders in would give (816 rows; Rs 8,05,93,520 in Q1 and Rs 7,97,50,520 in Q2); it is
  computed on the warehouse, and the fault is a supposition the item states.
- Finance's ledger and its hash total, 3,27,503, the sum of the order numbers of the 653 orders whose
  status is delivered (the escalated notebook's check under marker 1), and Kalpa's sales ledger, which
  books the app's Business revenue at Rs 4,17,78,440 and Rs 4,23,16,600 (the second case's item 9 and
  the check under its marker 2). Both ledgers are invented to give a check a source outside the
  learner's query; both numbers are computed on the warehouse.

## Which links does the pack print, each checked on the day it entered?

Every link below was fetched on 30 September 2026 by the session's source check, which quoted each
fact against its page; a claim the check corrected is noted beside it.

| Link | Where the pack uses it | What was checked, 30 Sep 2026 |
|---|---|---|
| https://ypfsresourcelibrary.blob.core.windows.net/fcic/YPFS/JPMorgan%20Management%20Task%20Force%20Regarding%202012%20CIO%20Losses%201-16-13.pdf | Chapter 1: notebook 1, morning S10, the notes | Checked 30 Sep 2026: The task force report of 16 January 2013 (an archival copy in the Yale Program on Financial Stability library; JPMorgan's own copy returns 404). Page 124: "the model operated through a series of Excel spreadsheets, which had to be completed manually, by a process of copying and pasting data from one spreadsheet to another" (CIO's new VaR model). Page 7: cumulative year-to-date losses through 30 June 2012 "had grown to approximately $5.8 billion". Checked 1 Oct 2026: 132 pages; section 3 of its contents is titled "The 'London Whale' Story and Senior Management's Response", the name S10's notes use |
| https://www.sec.gov/Archives/edgar/data/0000019617/000001961713000077/a8-k.htm | Provenance only | Checked 30 Sep 2026: JPMorgan's Form 8-K of 16 January 2013, which names the task force report and its date |
| https://web.archive.org/web/20260809070448/https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70 | Chapter 2: notebook 2, morning S23, the notes, the chapter 2 solution | Checked 30 Sep 2026: The Airbnb Tech Blog, "How Airbnb achieved metric consistency at scale", 30 April 2021; the live Medium page returns a bot wall, so the archived copy of the same URL was read. The quote matches word for word; the story is from years before the post. Corrected: the title's case. On 1 Oct 2026 the archive refused the connection and Medium returned 403, so the setting, the chief executive asking "which city had the most bookings in the previous week", was checked against a web search's excerpt of the post, which carries the line |
| https://www.eternal.com/blog/q1fy27 | Chapter 3: notebook 3, morning S36, the notes | Checked 30 Sep 2026: the page carries "B2C NOV grew 54% YoY to INR 31,120 crore" and the revenue and EBITDA lines, and links the letter below; the segment figures are not on this page |
| https://drive.google.com/file/d/1jb9KWd4Ap4RTKHFHxzEOO7jgQqVZEGcd/view | Chapter 3's figures, the notes' reading list, the second case's solution | Checked 1 Oct 2026: Eternal's Q1FY27 shareholders' letter (31 pages), downloaded and read. Page 3: NOV (B2C business) "is defined as the combined net order value (NOV) of consumer facing businesses i.e. food delivery, quick commerce and going-out". Page 4: "B2C NOV grew 54% YoY to INR 31,120 crore"; food delivery (Zomato) "NOV growth reached 20%+ YoY (INR 10,769 crore)"; quick commerce (Blinkit) "NOV grew 86% YoY to INR 17,132 crore"; going-out (District) "NOV growth accelerated to 60% YoY ... to INR 3,218 crore". Page 26: "Hyperpure supplies (B2B business) is our farm-to-fork supplies offering for restaurants in India and sale of items to businesses for onward sales" |
| https://handbook.gitlab.com/handbook/enterprise-data/platform/sql-style-guide/ | Chapter 4: notebook 4, morning S50, the notes, the chapter 4 solution | Checked 30 Sep 2026: "Prefer CTEs over sub-queries as CTEs make SQL more readable and are more performant", quoted with the cut marked; "perform a single, logical unit of work"; "a brief description of what's going on". Corrected: the first quote's cut is now marked. Checked again 1 Oct 2026: the guide cites no test for the performance claim, so the pack no longer says it rests on one; and "Do not use the USING command in joins because it produces inaccurate results in Snowflake", which the pack now quotes beside its own `USING` line |
| https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm | Chapter 5: notebook 5, morning S62, the notes, the chapter 5 solution, the day sheet | Checked 30 Sep 2026: Meta's Form 10-K for 2025, filed 29 January 2026: DAP 3.58 billion on average for December 2025 (page 61); the daily active person definition, "who visited at least one of these Family products"; "counting such group of accounts as one person" (pages 4, 28, 65). Checked 1 Oct 2026: page 4 names the four apps, "Facebook, Instagram, Messenger, and WhatsApp", and says "We estimate that such margin generally will be approximately 3% of our worldwide DAP", which the day sheet's "about 3 percent" repeats |
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

PostgreSQL 16.14; Python 3.11.15; pandas 3.0.6; psycopg2-binary 2.9.13 (installed in this session with
`pip install psycopg2-binary`, since the restarted container lacked it); nbclient 0.11.0; nbformat
5.11.1; openpyxl 3.1.5; python-pptx 1.0.2; LibreOffice 24.2.7.2 with Carlito (installed in this session
with `apt-get install fonts-crosextra-carlito`); mermaid-cli 12.0.0, whose missing `-w` flag
`scripts/build_cheatsheet.py` works around with `--size`. Both decks were built with
`scripts/build_deck.py` and rendered through LibreOffice to PDF and PNG, and every slide was looked at.

## The depth loop, 30 September 2026

The builder's passes 1 to 3 and the humanizer's read are logged here, then the two reviewer passes,
then the second round, which checked only the fixes that changed a method, a key or a number other
files repeat, then a check of the second round's own fixes, which had re-lettered keys and rebuilt
items.

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every chapter built from the row, the spine and the domain, in the chapter order? | The previous session's six notebooks held the spine's four rungs as chapters 1 to 4 with chapter 4's second half and chapter 5 carrying the suite the analyst audits, and chapter 6 the run that reproduces itself; chapter 2's list of smaller questions named a question no heading asked | Chapter 2 now asks six questions, each under its own heading, the last being the line Anand's sheet carries about last week's note; the decks, exercises, notes, board work, cheat sheet, day sheet and take-home were built chapter by chapter from the notebooks |
| 2. Domain | The builder | Could a learner who has never worked in a business say, for every chapter, who asks, why the metric matters, what a wrong number costs and which real company faces the same question? | Every notebook's first cell and every deck chapter's map and need slides name who asks, the metric and what a wrong number costs; the real companies' facts had not been checked in this build | A source check fetched every company fact on 30 September 2026 and corrected three: Airbnb's title case and the story's age, GitLab's quote with its cut marked, and Netflix's batch, which the talk shows raising a warning |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with two or more options, a sizing and the best-fit call with what would change it, and is the code its last mile? | Each chapter sizes two to four options on the warehouse before its first build step, and each deck chapter carries the options slide, the switch slide and a picture of the thinking before its code | Nothing to change in the notebooks; the decks were written to the same order |
| Humanizer's read | The builder, and each builder agent on its own files | Does every prose file read as a person wrote it? | The tic scanner was clean on every markdown file and on the notebook build script; the read found staged contrasts only where both halves carry a number, and one fragment stack in a deck note | The fragment stack rewritten; the notes' length kept, since every section carries a worked case and the Week 1 Thursday model runs to the same length |
| 4. Rigor | A fresh reviewer, read-only, once, 1 October 2026 | Does every number, key, route and fact hold when the pack is sat and rerun cold? | Failed with 4 blockers, 15 majors and 28 minors. Blockers: the warehouse file's header named two plants; the second case's solution claimed the Rs 5,00,000 size line splits the orders as the segment does; the guided build's item 3 had two defensible keys; chapter 1 sized the export at 1,340 rows against its own exercise key. Majors included second routes that could not fail (chapters 4 and 6), 11 genuine design items of 27 labelled, key strings that repeated cycles, lone shortest keys, crashing TODO distractors and checks that passed for wrong letters, two definitions of spend per member, unsourced company facts, and Monday explaining Wednesday's ties | Every finding fixed: the header cut (see the data section); the size line's effect stated with its numbers (50 Business orders filed as consumer ones, the app's consumers reading +94.4 percent, 138 against 188); the guided item asks for the bound; the export sized at 1,000; chapter 4's route is revenue over the 107 counted apart, chapter 6's a count with no sort; design items rebuilt so the learner sizes, counts or reconciles (26 of 73); every key string reshuffled with no lone longest or shortest key; every TODO distractor runs without an error, tested by running all 51 wrong letters, and every wrong letter of a marker with a computed answer fails a check (the second case's marker 7, the switch fact, has none to compute); spend per member defined once; facts sourced or cut; ties left to Wednesday |
| 5. Pedagogy and language | A fresh reviewer, read-only, once, 1 October 2026 | Does the pack teach a room that has never seen it, heading by heading and file by file, in the house voice? | Failed with 26 majors and 43 minors: templated headings (map-slide subtitles, notebook closers, the four solution headings in every file), chapter notebooks that did not stand alone, three terms with two meanings (spend per member, the book, schema), one inflated claim in four files, one slogan in seven places, a moral closer after every real-company paragraph, two renders that failed the projector read, missing predict and fix slides, a STUDENT note without "tentative", and a day sheet pointing at a page that does not exist | Every finding fixed or answered: specific headings in every file; each notebook opens on the case; the three terms defined once; the claim, the slogan and the closers cut; the crux slide a table; the predict and fix slides added; "tentative" beside every mention of the block; the companion's path corrected; the drill made one list of thirteen. One answered, not fixed: the index names no posting channel, since that fact is an open conflict |
| 6. Second round | A fresh reviewer, read-only, 1 October 2026, scoped to the fixes after passes 4 and 5 that changed a method, a key or a number other files repeat | Does each changed key hold, does every wrong letter fail, does any check or stem give a key away, and does any file still state an old number? | Failed with 2 blockers, 6 majors and 9 minors. Every changed key held when sat blind and recomputed, and all 51 wrong letters ran. Blockers: the escalated brief named the status its item 1 asks for, the check under marker 1 carried the key's literal, S16's notes and the notes defined the filter, and item 15's stem named item 1's trap; the second case's opening and item 2's stem gave item 2's key. Majors: key strings that cycled or sat inside another file's (chapter 2's `bcdab`, the lab's items 7 to 11, the escalated case's items 9 to 13, chapter 4's string inside the Kahoot's, the guided build's inside the escalated case's); chapter 4 item 6 and chapter 5 item 5 with only the key on the stem's number; chapter 6 item 5's stem naming item 4's fix; the second case naming its trap in item 8, its stakeholder line and its post line; the second case's marker 5 letter d failing only on a literal; the old second routes in notebook 6 and in S57's notes. Minors: three wrong explanations (chapter 1 item 5 c, chapter 4 item 1 d, the second case notebook's 5 d), escalated marker 9 explaining Wednesday's ties, checks spelling a key's rule beside its marker, marker 7 with no check and no word on why, the day sheet's debrief order against the TA note's, chapter 2's 1,340 export unexplained, and three key rationales echoing the brief | Every finding fixed. The escalated case is titled "Does the Monday suite hold on Finance's definition of revenue?" and states the definition in Anand's words in the brief, the notebook, the notes' case paragraph, S16 and S17; marker 1's check and part 5's rewrites moved into setup helpers that read the learner's own filter; item 15 now supposes the 163 cancelled orders let in (Rs 16,03,44,040, route b Rs 8,05,93,520 plus Rs 7,97,50,520, option c the book less the returned rupees), since a version with the returned orders let in would still tell the room item 1's trap; marker 9's option a is `ORDER BY random()` and the uniqueness check and the 76 customers are gone. The second case describes Business and consumers by who buys; item 2 asks which label keeps every Business order on the Business side next quarter as well as this one; item 8, its stakeholder line and its post line use Marketing's own words; marker 2's check reads its count from the setup cell, marker 5's tests that a channel is named exactly when one fell, and marker 7 prints why it has no check. Re-lettered: chapter 2 item 3 (a), chapter 4 item 6 (d), the guided build's item 4 (a), the lab's item 10 (c), the Kahoot's item 6 (b), the second case's item 8 (c) and the escalated case's item 11 (b); a scan of every key string finds no run of four stepping through the letters and no run of five shared by two files. Chapter 4 item 6 sets two routes on Rs 5,474 and Rs 3,863 apart by where the count comes from (the fix's own 107 rows, or 120 less the 13 who bought nothing), and its item 1 option d now claims nothing to rebuild in a fresh session; chapter 5 item 5 adds a 204 with a false clause and asks which statement holds in full; chapter 6 item 5 defines the sample as the five smallest order ids. Notebook 6 asks whether a count with no sort confirms the five; S57's last note names the route over the same 107; the 1,340 export is 1,000 orders and 340 customers in notebook 2, S24 and the notes. The builder reran all 51 wrong letters: every marker with a computed answer fails a computed check (marker 9's a shares 0 of its five with the rerun; the second case's 5 d fails on "3 of 3 channels fell"), and marker 7, a fact the book does not record, prints why it has none |
| 7. Check of the second round's fixes | A fresh reviewer, read-only, 1 October 2026, scoped to commits 9287096, 01bd541 and 98d20b9 | Does each rebuilt key hold with one defensible option, does anything a learner reads before posting give a key away, is any new distractor a strawman, and does any file still state an old letter or number? | Failed with 6 blockers, 2 majors and 6 minors. Every key held as the intended answer, and every number recomputed. Blockers: the escalated setup cell's new helper named the statuses item 1 asks for; the measure was still called delivered before item 1 (S7's notes, the notes, item 11, item 3's 653, the part 2 heading, the post line, S16 and S17); the second case's item 2 had a second defensible key, since Business or Retail-Plus also keeps every Business order on the Business side, and its setup cell named the segment rule; chapter 5 item 5's option d was true as written; chapter 4 item 6's option b could disagree with some wrong steps. Majors: the escalated item 9's `ORDER BY random()` was a strawman; the second case's opening figure and consumer-tree sentence showed item 8's key. Minors: item 15's option a spelled out the statuses, the reload helper printed item 9's key, the correction helper and its label pointed at item 10's key, chapter 6 item 5's option a referred to a query its stem no longer shows, S17's card stated item 9's rule, and the round-2 row above overclaimed | Every finding fixed. Marker 1's check sets the sum of the order numbers the filter keeps beside the hash total on Finance's ledger, 3,27,503, and marker 2's sets the app's Business side beside the sales ledger's Rs 4,17,78,440 and Rs 4,23,16,600, so no line a learner reads names a status or a segment rule. The escalated case names its measure Finance's book and Finance's revenue throughout the brief, the notebook, S7, S16, S17 and the notes; item 3's option d names no count; item 9's option a sorts after the cut, and four of its five come back after the reload; the reload rewrites the quarter's first web order, picked with `min()`; the correction helper and its check label name no amount; item 15's option a names no status. The second case's item 2 asks for every Business order and no consumer order, with two labels and no more; item 8 sets four splits against each other and asks for the smallest that answers; its opening figure draws Marketing's reading, and its consumer tree is defined at step 3. Chapter 4 item 6's option b divides the step's own rupees by the step's own rows, the fix's average written as a division; chapter 5 item 5's option d claims the half-year should read 159; chapter 6 item 5's option a reruns the service head's query; S17's cards state outcomes. No key letter changed. The builder confirmed these fixes with the proof run below: 51 wrong letters rerun with 0 errors and every marker with a computed answer failing a computed check, the distractor audit, a scan for a lone shortest or longest key, the key-string scan and the searches for every replaced text |


## The proof run

Run on 1 October 2026 on the branch after the check of the second round's fixes, in a container with
PostgreSQL 16.14 started, the warehouse loaded by `bash .devcontainer/load_warehouse.sh`, and
`psycopg2-binary` 2.9.13 and `fonts-crosextra-carlito` installed in the session; the other tools are
the versions listed above.

| Proof | Command | Result |
|---|---|---|
| The gate, with every notebook cold-run in its own folder | `python3 scripts/verify.py content/W02/D1 --execute` | Pass, 0 failures. 62 files named and placed for a teaching day; the six chapter notebooks and both case solutions run cold and clean, and the two TODO twins are skipped by design; 10 notebooks with 125 checks passing and none failing; 11 option files audited; the workbook's 5 verdicts computed and 10 decisions flipped and re-asserted; the companion's 34 controls clicked, none inert and no console error; 82 and 28 slide sources checked, and 112 built slides with no overflowing box |
| The companion | `python3 scripts/build_companion.py content/W02/D1 --check` | Pass: the library is current |
| The programme sync | `python3 scripts/sync_programme.py --check` | Pass: every output is current |
| The warehouse file | Loaded into a fresh database with `psql -v ON_ERROR_STOP=1 -f data/C2_W02_D01_warehouse_v4_STUDENT.sql` | Loads 1,000 orders, 340 customers, 1,428 payments, 136 exposure rows, 13 plan rows and 12 refunds; md5 a3977a5ad1021474ecc5adf68f3c97cd, as the data section records |
| The chapter SQL | Each file in `sql/` run with `psql -f` on that database | Files 01, 02, 04, 05 and 06 run every named block (9, 6, 11, 7 and 7) with no error, file 04's temporary table being its one block with no result set. File 03 runs its 8 blocks with one error, the GROUP BY refusal of block `c3_group_error`, which the file labels as stopping on purpose |
| The take-home book | `psql -f data/C2_W02_D01_takehome_STUDENT.sql`, then the script with `--check` and with `--check --load` | The schema takehome loads 126 members and 362 orders and leaves 7 public tables; `--check` matches a fresh build without touching a database; `--check --load` asserts every self-check number |
| Every wrong letter | Each case solution notebook rerun once per wrong letter, in a scratch copy | 51 runs, 0 errors; every marker with a computed answer fails a computed check, and the second case's marker 7, which asks for a fact the book does not record, prints why it has none |
| The decks | `scripts/build_deck.py` on both sources, then LibreOffice to PDF and PNG | 83 and 29 slides. The building session looked at every slide; this session looked at every slide it changed: the morning's S24 and the afternoon's cover, SECTION 7, S16 and S17 |
| Key strings | A scan of every set's key string | No run of four keys stepping through the letters, no run of five shared by two files, no position past the audit's limits, and no key the lone shortest or longest option in its item |
| Language | The tic scanner over the folder and the notebook builder, and a scan of every added line for dashes, the rupee glyph and the banned words | Clean on 38 files, and no hit |

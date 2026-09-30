# The Week 2 and Week 3 revamp

The requester scheduled this to start after Sunday 4 October 2026, 11 PM IST, once the account's weekly
usage resets. It raises Week 2 (five teaching days) and Week 3 (Build 1 in Kalpa Health, now a
US-facing business) to the chapter standard in full depth. The orchestrating session runs it, and the
steps below are its order.

## 1. Week 1 comes first

Check that main carries all of Week 1: the five chapter packs `content/W01/D1` to `D5`, the retail
dossier in `content/W01/D1/`, and both raised Saturday papers. Finish whatever is still open (one
review, one fix pass, merge) before anything below starts. The Week 2 sessions read the Week 1
packs as the model for the chapter form.

## 2. What the orchestrating session needs

- The merge tool and a fast-forward of its own branch. If either is refused, ask the requester to add
  the allow rules for `mcp__github__merge_pull_request`, `Bash(git merge --ff-only origin/main)` and a
  push of the session's own branch to `.claude/settings.local.json`, and carry on with everything a
  merge does not block.
- One review per pack. Read the pack against `the-standard.md` and the lessons listed in the day prompt,
  fix what is found in one pass (a local agent in a worktree on the day's branch), then open the pull
  request with the `orchestrator-reviewed` label, merge it, and move the board card with
  `python3 scripts/board_sync.py --status W{ww}/D{d} review-1`.

## 3. Week 2: five cloud sessions in parallel

Launch one cloud session per day with `create_session`: source main, outcome branch
`w02-d{n}-chapters`, tags `c2-chapters` and `week-2`. Each gets the day prompt below with its fills.
Move the five board cards to `building` when they start. The Week 2 Saturday paper was raised on
30 September 2026; revisit it only where a rebuilt day changes a number the paper prints.

### The day prompt

````markdown
Raise the Week 2 {DAY} day pack for Cohort 2 ({DATE}) to the chapter standard the requester set on 30 September 2026. One session, one day pack.

**Already decided, so do not stop for approval.** The requester approved the Weeks 1 and 2 spine on 29 September 2026 and raised the standard on 30 September 2026. The decisions are `chapter-standard` and `four-domains` in `data/programme/facts.yaml`. `docs/detailing/W01_W02_spine.md` is gate 2 for this day. State the envelope and continuity in your first message, then build straight through every pass without waiting.

**Read before building, in this order.**
1. `CLAUDE.md`.
2. `.claude/skills/day-pack-builder/references/the-standard.md`: the bar, the chapter, the grid, the volume, each family's form and the depth loop.
3. `docs/detailing/W01_W02_spine.md`: the rule every day follows, the faculty-day paragraph and {DAY}'s row in the Week 2 table.
4. The {DAY} row in `docs/curriculum/W2_Data_manipulation.md`, all columns in order, including the violet IITGN faculty column.
5. The day's line in `docs/programme/calendar.md`, and `docs/07_Client_Zero.md` for the v4 warehouse.
6. The retail dossier, `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`. It is on main once merged; until then, read it from `origin/w01-domain-retail`.
7. `.claude/skills/day-pack-builder/SKILL.md` and its references, and `content/README.md`.

Then read the skills CLAUDE.md routes to for each family, each in full before the pass that uses it.

**The domain.** Kalpa Retail continues, and the room met its story on Week 1 Monday. Link to the dossier by its path; never copy it. Every chapter names:
- the metric at stake;
- who at Kalpa asks for it;
- what a wrong number costs them in rupees, customers or time;
- a real company whose data or finance team faces the same question.

Check each fact about that company today with WebSearch and WebFetch, and record its URL and date in the provenance. A figure you cannot check stays out, or appears only as a labelled illustrative number. Kalpa stays the case.

**The bar, chapter by chapter.** The day is one Kalpa case climbed in about six chapters, each about 30 minutes live. Each chapter is one deck chapter (`## SECTION n:`) paired with one notebook of the same number and title, and each notebook builds on the one before it. A chapter runs:
1. **The need:** the stakeholder's problem, the metric, the decision riding on it and the real company.
2. **The options:** two to four genuinely different ways to answer it. Size each on what separates them: rows scanned, the error it risks, what it assumes. Make the best-fit call and name the fact that would change it.
3. **The build:** the chosen way on Kalpa data, each step predicted before it runs.
4. **The trap:** the plausible wrong number computed the way a hurried analyst would, why it is wrong in business terms, the check that catches it, and the fix with what changed.
5. **The second route:** the same number reached by an independent method and asserted equal.
6. **Kavya's review.**

SQL, pandas or Excel is the calculator, and the code is the chapter's last mile. A syntax or runtime error gets two minutes when it happens and never a trap slot, a chapter or an exercise item. The notebook sizes are 20 to 36 cells, with at least five visuals and five passing checks each. The exercise volume is about 35 items, at least a third of them design items. Both are floors.

**What the Week 1 reviews found. Build it right the first time, because each of these held a pack back from merging.**
1. **Nothing spoils a later day.** No file teaches a trap or a method a later day stages, under any numbers. Later this week: {LATER}. A file may point back at an earlier day's trap by name.
2. **No exercise is answerable cold.**
   - Every distractor is the plausible wrong answer a hurried analyst gives, never a strawman.
   - No key echoes the chapter's slogan.
   - Across a file, the key is sometimes the longest option and sometimes the shortest, never the lone outlier.
   - No later stem announces an earlier item's key.
   - No part or case opening names the trap.
   - A TODO's check cell tests a value the learner computed, in a later cell, and never prints or tests the key's words.
3. **Design items are genuine.** Each makes the learner combine two ideas or take several steps: the best-fit approach with a sizing the learner computes, the fact that would switch it, or the second route. Put some in the escalated and second cases too.
4. **The second route is independent.** A route that re-derives the first route's identity cannot fail when the first is wrong. A literal constant in a "from the logs" check is not a route.
5. **Plants stay unnamed.** Never name a plant in a STUDENT file, including in a depth section, a pre-read or an invented example that reuses the planted value. The plant exception covers only the Saturday paper.
6. **One number, one definition.** Every number repeated across the deck, notebooks, notes, day sheet and keys matches, and a term means one thing everywhere.

**This day.** {SPECIFICS}

{FACULTY}

**What exists.** `content/W02/D{N}` holds the pack built to the 29 September standard, in three 50-minute rounds with no options, no sizing and no second route. Raise it:
- Split each round into the chapters it holds, and write each chapter's options, sizing and second route.
- Rebuild the decks chapter by chapter.
- Add the design items.
- Bring the notes, day sheet, board work, Kahoot and pre-read to the new grid.

Keep every file that already meets the bar, rename or delete the ones the chapters replace, and leave no orphan. The Week 1 Wednesday to Friday packs show the chapter form once they are merged.

**The depth loop.** Passes 2 (domain) and 3 (problem first) are yours. For passes 4 (rigor) and 5 (pedagogy and language), launch one fresh reviewer subagent each with the Agent tool, read-only, once. The rigor reviewer also sits the day's exercises blind from the STUDENT files alone, and checks every STUDENT file against the later days' traps listed above. Fix every finding. A second round runs only when a fix changed a method, a key or a number other files repeat, and it checks only those changes. Log the passes in the provenance.

**Boundaries.**
- Write only under `content/W02/D{N}/`.
- Do not edit shared files: `scripts/`, `.claude/`, `docs/`, `data/`, `CLAUDE.md`, `prompts/` or `wiki/`. Do not touch another day's folder either, because four other sessions are building Week 2 in parallel.
- If a shared tool lacks something, work around it inside the day folder and name the change you would ask for in your final report.

**Proof.**
- `python3 scripts/verify.py content/W02/D{N} --execute` passes with zero failures.
- `python3 scripts/build_companion.py content/W02/D{N} --check` and `python3 scripts/sync_programme.py --check` pass.
- Every `.sql` file runs against Postgres.
- Every deck is built with `scripts/build_deck.py`, rendered through LibreOffice and looked at slide by slide. Install `fonts-crosextra-carlito` if the render lacks it.
- Every notebook is executed cold in its own folder.
- Every exercise, quiz and practice set passes `scripts/distractor_audit.py`.
- The llm-tic-scrubber scanner is clean on every markdown file.

**Ship.** Commit in small commits whose messages say what changed, and push to the branch `w02-d{N}-chapters`. Do not open a pull request. Finish with a report containing:
- the chapters with their notebooks and deck sections;
- each chapter's options, best-fit call and second route, in one line each;
- each trap with its exact wrong number;
- the real company per chapter, with its source;
- the design-item count, with a one-line case for each;
- the depth loop's findings and fixes;
- the verify output;
- everything that departs from the spine or the row, and why.
````

### The fills

#### Week 2 Monday

- `{DAY}`: Monday; `{DATE}`: Mon 12 Oct 2026; `{N}`: 1
- `{LATER}`: Tuesday's join fan-out that doubles collected revenue, the INNER join that hides unpaid orders, and the WHERE on the payments side that turns a LEFT join into an INNER one; Wednesday's ranking of the whole table when the ask was per segment, LAG without PARTITION, a skipped month counted as a fall, and a tie that ships 49 or 51 rows; Thursday's merge that doubles a customer's spend, pivot_table averaging where a total was meant, groupby dropping customers with no segment, and recency measured from today; Friday's pivot that double-counts the double-paid orders, the approximate lookup that returns a neighbour for a missing id, SUM counting rows a filter hid, and a headline with no denominator or period
- `{SPECIFICS}`:

Anand wants the revenue tree every Monday, for every segment and channel, computed from the warehouse itself. The data is the v4 warehouse, generated and loaded as the existing provenance records. The spine's Monday rungs become the chapters:
- Week 1's leaves re-answered in SQL and checked against their Week 1 numbers;
- per segment and quarter;
- two quarters as CTEs;
- the suite Anand's analyst audits;
- a sixth chapter on the Monday run that reproduces itself.

The traps:
- orders per customer returning 1, because Postgres divides integers;
- COUNT(*) counting order rows as customers;
- AVG skipping NULLs without saying so;
- LIMIT without ORDER BY giving two learners two answers.

The options are where the depth is:
- export to pandas, query the warehouse, or save a view;
- a subquery, a CTE or a temporary table;
- each sized on rows moved, what an auditor can rerun, and what breaks when the schema changes.

Queries ship as `.sql` files in `sql/`, and the notebooks run them through `kit.sql`. Where the warehouse has no NULL where the AVG trap needs one, show the trap on a tiny table written in the query and labelled invented.

- `{FACULTY}`: **A faculty day.** The tentative IITGN block W2-1 takes the last 120 minutes. The trainer keeps the morning block and the afternoon's first 60 minutes: chapter 6 (30), the escalated case's first two parts (20) and the Kahoot (10).  The rest of the escalated case, the second case and the interview drill move to the practice lab and the take-home. The day sheet carries empty `sync:module:W02/D1` and `sync:faculty-day:W02/D1` blocks for the sync to fill, and a STUDENT file mentions the block only with the word tentative.

#### Week 2 Tuesday

- `{DAY}`: Tuesday; `{DATE}`: Tue 13 Oct 2026; `{N}`: 2
- `{LATER}`: Wednesday's ranking of the whole table when the ask was per segment, LAG without PARTITION, a skipped month counted as a fall, and a tie that ships 49 or 51 rows; Thursday's merge that doubles a customer's spend, pivot_table averaging where a total was meant, groupby dropping customers with no segment, and recency measured from today; Friday's pivot that double-counts the double-paid orders, the approximate lookup that returns a neighbour for a missing id, SUM counting rows a filter hid, and a headline with no denominator or period
- `{SPECIFICS}`:

Anand asks what was actually collected against what was booked in Q2, order by order and by channel, and the platform lead mentions that the gateway sometimes double-posts. The spine's Tuesday rungs become the chapters:
- two tiny tables traced row by row before any query runs;
- the naive join;
- the row-count check and the revenue bridge;
- the unpaid and double-paid lists;
- the report by channel that Anand signs;
- a sixth chapter on the validation that runs before the number leaves.

The traps:
- a join fan-out that doubles collected revenue while every row looks right;
- an INNER join that hides unpaid orders;
- a WHERE on the payments side that quietly turns the LEFT join into an INNER one.

The row-count reconciliation is the habit the whole day rests on. The options set pre-aggregating payments per order, DISTINCT, a window dedupe and fixing the feed against each other, each sized on this data. Queries ship as `.sql` files in `sql/`.

- `{FACULTY}`: **A faculty day.** The tentative IITGN block W2-2 takes the last 120 minutes. The trainer keeps the morning block and the afternoon's first 60 minutes: chapter 6 (30), the escalated case's first two parts (20) and the Kahoot (10).  The rest of the escalated case, the second case and the interview drill move to the practice lab and the take-home. The day sheet carries empty `sync:module:W02/D2` and `sync:faculty-day:W02/D2` blocks for the sync to fill, and a STUDENT file mentions the block only with the word tentative.

#### Week 2 Wednesday

- `{DAY}`: Wednesday; `{DATE}`: Wed 14 Oct 2026; `{N}`: 3
- `{LATER}`: Thursday's merge that doubles a customer's spend, pivot_table averaging where a total was meant, groupby dropping customers with no segment, and recency measured from today; Friday's pivot that double-counts the double-paid orders, the approximate lookup that returns a neighbour for a missing id, SUM counting rows a filter hid, and a headline with no denominator or period
- `{SPECIFICS}`:

Marketing wants three things: the top fifty members by Q2 revenue in each segment, a flag on anyone whose monthly spend fell two months running, and revenue accumulating against the plan line. The head of Retail-Plus wants ties ranked the same. The spine's Wednesday rungs become the chapters:
- the top fifty overall;
- per segment;
- the tie at fifty;
- falling spend with LAG;
- the running total against plan;
- a sixth chapter on the protect list Marketing acts on.

The traps:
- ranking the whole table when the ask was per segment;
- LAG without PARTITION reading another customer's month;
- a skipped month counted as a fall (the member who says he was on holiday);
- a tie that makes the list ship 49 or 51 rows.

The options set ROW_NUMBER, RANK and DENSE_RANK against the business rule, and a calendar table against LAG. Queries ship as `.sql` files in `sql/`.

- `{FACULTY}`: **A faculty day.** The tentative IITGN block W2-3 takes the last 120 minutes. The trainer keeps the morning block and the afternoon's first 60 minutes: chapter 6 (30), the escalated case's first two parts (20) and the Kahoot (10).  The rest of the escalated case, the second case and the interview drill move to the practice lab and the take-home. The day sheet carries empty `sync:module:W02/D3` and `sync:faculty-day:W02/D3` blocks for the sync to fill, and a STUDENT file mentions the block only with the word tentative.

#### Week 2 Thursday

- `{DAY}`: Thursday; `{DATE}`: Thu 15 Oct 2026; `{N}`: 4
- `{LATER}`: Friday's pivot that double-counts the double-paid orders, the approximate lookup that returns a neighbour for a missing id, SUM counting rows a filter hid, and a headline with no denominator or period
- `{SPECIFICS}`:

The growth team wants one table per customer, refreshed every Monday, built in pandas from the warehouse, carrying recency, frequency, spend, segment, campaign exposure and last week's flags. A senior analyst asks for the tree a third way and an honest tool choice. The spine's Thursday rungs become the chapters:
- recency, frequency and spend with groupby;
- the exposure merge;
- the months pivot;
- one question in three tools;
- the tool-choice note;
- a sixth chapter on the Monday refresh that validates itself.

The traps:
- a merge that doubles a customer's spend;
- `pivot_table` averaging where a total was meant, which is its default;
- `groupby` dropping customers with no segment;
- recency measured from today instead of the data's last date.

Teach the current pandas 3 API and no deprecated idioms, and state the version you checked against. The second case is the three-tool re-expression and the tool-choice note.

- `{FACULTY}`: **Not a faculty day.** The day runs the full grid in the-standard.md, with the module sync block in the day sheet.

#### Week 2 Friday

- `{DAY}`: Friday; `{DATE}`: Fri 16 Oct 2026; `{N}`: 5
- `{LATER}`: nothing later this week; Saturday's recap paper follows, and Week 4's traps (metric design, basket confidence, cohorts, forecasting baselines) stay untaught
- `{SPECIFICS}`:

Meera's chief of staff wants three things she can open without a login:
- the revenue tree by segment for both quarters;
- the top-fifty protect list, with a lookup by member id;
- one front-page number with its trend.

They have to recalculate when a director changes an assumption in the room. The spine's Friday rungs become the chapters:
- a pivot on the clean table;
- the same pivot on the raw export;
- the member lookup;
- the front-page number;
- the operating rule;
- a sixth chapter on the workbook a director can break and the checks that stop them.

The traps:
- a pivot double-counting the double-paid orders;
- an approximate lookup returning a neighbour for a missing id;
- SUM counting rows a filter hid;
- a headline with no denominator or period.

The second case is the operating rule, defended against a director who wants to edit the source. Use only formulas that survive LibreOffice (the companion-builder skill lists them).

- `{FACULTY}`: **Not a faculty day.** The day runs the full grid in the-standard.md, with the module sync block in the day sheet.

## 4. Week 3: Build 1 in Kalpa Health, now US-facing

Client zero section 1c and decision `four-domains` set the frame: Kalpa Health is a US diagnostics and
revenue-cycle business run from Kalpa's GCC, in dollars, with payers, claims, denials and prior
authorisation in its vocabulary. The build week keeps its shape from `docs/detailing/W03_build1_spine.md`.

1. **The US healthcare dossier.** Follow `.claude/skills/day-pack-builder/references/domain-dossier.md`,
   with the retail dossier in `content/W01/D1/` as the model, and put it in `content/W03/D1/`. Research
   it fresh, with every fact checked and dated:
   - how a US lab and its revenue cycle make money: the order, the draw, the result, the claim (837),
     the remittance (835), and the denial with its CARC and RARC codes;
   - who pays: commercial plans, Medicare and Medicaid;
   - the codes: CPT, ICD-10-CM and HCPCS;
   - medical necessity and prior authorisation;
   - HIPAA: the privacy and security rules, minimum necessary, de-identification and the business
     associate agreement;
   - what offshore work from an Indian GCC may and may not touch;
   - the real companies: Quest Diagnostics and Labcorp, and the Indian revenue-cycle and GCC centres
     that serve US providers;
   - where analytics, ML, NLP and agents pay off: denial prediction, coding assistance, prior-auth and
     claim-status agents, and no-show prediction.

   Run one review round before the Week 3 packs start.
2. **The Kalpa Health generator** (`data/generate_kalpa_health.py`) moves to the US setting:
   - dollars and US metro areas;
   - payers;
   - claims billed against payments posted, with denials.

   Keep the five sub-problems and the logic of each plant, keep the output deterministic, and add a
   contract check. Then:
   - rewrite the spine's "The week" section for the US setting;
   - record a decision that the Build 1 rubric's "rupees" reads "dollars";
   - run the sync.
3. **The Week 3 packs** (`D1`, `D3`, `D4`, `D5` and `SAT`) are rebuilt by cloud sessions in parallel.
   Each reads the new dossier, the regenerated data and the spine, and goes as deep as the Week 2 days:
   - the sub-problem briefs sized with options;
   - the checkpoint questions;
   - the mock bank's viva prompts per sub-problem;
   - the GD prompts, which climb in complexity;
   - the panel's question bank.

   Build weeks keep their own shape and carry no practice set.

## 5. Done

Week 2 and Week 3 are done when every pack is merged, every board card is at review-1, and
`python3 scripts/sync_programme.py --check` passes on main.

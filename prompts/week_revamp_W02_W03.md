# The Week 2 and Week 3 revamp

The requester first scheduled this for after Sunday 4 October 2026, then on 30 September asked for it
to run straight away, with every session and agent on the latest Opus model at max effort (decision
`opus-max`; `.claude/settings.json` sets both). The same day the requester raised the standard again
(decisions `question-ladder`, `self-contained` and `humanizer`), so every pack, Week 1 included, is
built or rechecked to that raise, which `the-standard.md` calls the second raise and this plan calls
standard v3. It raises Week 2 (five teaching days) and Week 3 (Build 1 in Kalpa Health,
now a US-facing business) to the chapter standard in full depth. The orchestrating session runs it,
and the steps below are its order.

## 1. Week 1 comes first

Check that main carries all of Week 1: the five chapter packs `content/W01/D1` to `D5`, the retail
dossier in `content/W01/D1/`, and both raised Saturday papers. Finish whatever is still open (one
review, one fix pass, merge) before anything below starts. The Week 2 sessions read the Week 1
packs as the model for the chapter form.

Then Week 1 is rechecked against standard v3, one cloud session per day and one for both Saturday
papers, each given the recheck prompt below with its fills, on branches `w01-d{n}-v3` and
`w01-w02-sat-v3`. The Week 2 paper's recheck waits for the rebuilt Week 2, since a rebuilt day can
change a number the paper prints.

### The recheck prompt

````markdown
Recheck the Week {W} {DAY} day pack for Cohort 2 ({DATE}) and raise it to standard v3. One session, one day pack.

**Already decided, so do not stop for approval.** The pack in `content/W{WW}/D{N}` meets the chapter standard the requester set on 30 September 2026. The same day the requester raised it again: decisions `question-ladder`, `self-contained`, `humanizer` and `opus-max` in `data/programme/facts.yaml`. `the-standard.md` carries all of it. Build straight through without waiting, from branch {BASE}.

**Read first, in this order.** `CLAUDE.md`; `.claude/skills/day-pack-builder/references/the-standard.md`, above all the question ladder, the self-contained rule and the decks; `.claude/skills/humanizer/SKILL.md`; the week's spine in `docs/detailing/`; the day's row in `docs/curriculum/`; the day's own provenance in `internal/`.

**What this pass does.**
1. **Every heading becomes a question.** In every STUDENT and TRAINER file, each heading is a plain, specific question its section answers, understandable on its own. Under each chapter-level heading, **Who needs the answer.** names the person, the decision and the cost of a wrong answer, and **The questions on the way.** lists the smaller questions; each section closes on its answer with its number. On a slide the italic subtitle asks and the action title answers; a chapter opener's title is the chapter's question in about 22 characters and its promise is the full question. The day sheet prints the whole ladder at its top. Read each file's headings alone, in order: they must tell the day's argument.
2. **Every file stands on its own.** Open each deck, notebook, exercise file, case brief, solution file and the take-home alone. Wherever it needs another file to be followed (a scenario, a term, a number, what an earlier chapter found), carry that in, in a sentence or two; a pointer stays only for more depth. A notebook loads its own data and runs cold. Where an earlier finding is a plant, restate the rule the room drew from it, never the planted record.
3. **The decks carry each chapter in full.** A learner who missed the class must follow every chapter from the slides and their notes. After the cover, one slide asks the day's question and lists the chapter questions. Each chapter opens on its question, then a map slide, then about 10 to 14 slides in the notebook's rhythm: the need, the real company, the options with their sizing and the best-fit call, the thinking as a picture, per build step a predict slide, the logic or code in one short block, the result with its numbers as a picture and the check, then the plausible wrong answer, why it is wrong with its check, the fix, the second route, and a close that answers each smaller question beside Kavya's review. Add the slides a thin chapter lacks. Rebuild with `scripts/build_deck.py`, render through LibreOffice with Carlito, and look at every slide: fix overflow, crowding and any picture that does not read.
4. **The humanizer's read, everywhere.** Run the humanizer in file mode over every prose file: notes, cheat sheet, pre-read, board work, day sheet, exercises and solutions, take-home, Kahoot, the deck markdown (slide text and notes), and the notebooks' markdown through the scripts that write them. Keep code, data, paths and links as they are, and keep the standard's recurring bold beats.
5. **Recheck everything.** Every number repeated across files matches; every trap shows its exact wrong number; no STUDENT file names a plant or teaches a later day's trap ({LATER}); every key and distractor passes the audit and reads fairly cold; every link carries its check date.

{SPECIFICS}

**The review.** When the five steps are done, launch one fresh reviewer subagent with the Agent tool and `model: opus`, read-only, once: it runs the headings-only read on every file, opens three files at random alone to test that each stands on its own, looks at every rendered slide, and lists every humanizer pattern still present. Fix every finding. If a fix changes a method, a key or a number other files repeat, a second fresh reviewer checks only those changes.

**Boundaries.** Write only under `content/W{WW}/D{N}/`. Do not edit shared files (`scripts/`, `.claude/`, `docs/`, `data/`, `CLAUDE.md`, `prompts/`, `wiki/`) or another day's folder; name any change a shared tool needs in your report.

**Proof.** `python3 scripts/verify.py content/W{WW}/D{N} --execute` passes with zero failures; `python3 scripts/build_companion.py content/W{WW}/D{N} --check` and `python3 scripts/sync_programme.py --check` pass; every deck is rebuilt and looked at; every notebook runs cold; the tic scanner is clean on every markdown file.

**Ship.** Small commits whose messages say what changed, pushed to `w{WW}-d{N}-v3`. Do not open a pull request. Report: the day's question ladder (the day's question, each chapter's question and its smaller questions); what each file needed to stand on its own; slides added per chapter; the humanizer's main finds; the review's findings and fixes; the verify output; anything left undone and why.
````

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
`w02-d{n}-chapters`, tags `c2-chapters` and `week-2`, and model `claude-opus-5-5`. Each gets the day prompt below with its fills.
Move the five board cards to `building` when they start. The Week 2 Saturday paper was raised on
30 September 2026; revisit it only where a rebuilt day changes a number the paper prints.

### The day prompt

````markdown
Raise the Week 2 {DAY} day pack for Cohort 2 ({DATE}) to standard v3, the chapter standard the requester set on 30 September 2026 and raised the same day. One session, one day pack.

**Already decided, so do not stop for approval.** The requester approved the Weeks 1 and 2 spine on 29 September 2026 and raised the standard on 30 September 2026. The decisions are `chapter-standard`, `four-domains`, `question-ladder`, `self-contained`, `humanizer` and `opus-max` in `data/programme/facts.yaml`. `docs/detailing/W01_W02_spine.md` is gate 2 for this day. State the envelope and continuity in your first message, then build straight through every pass without waiting.

**Read before building, in this order.**
1. `CLAUDE.md`.
2. `.claude/skills/day-pack-builder/references/the-standard.md`: the bar, the chapter, the grid, the volume, each family's form and the depth loop.
3. `docs/detailing/W01_W02_spine.md`: the rule every day follows, the faculty-day paragraph and {DAY}'s row in the Week 2 table.
4. The {DAY} row in `docs/curriculum/W2_Data_manipulation.md`, all columns in order, including the violet IITGN faculty column.
5. The day's line in `docs/programme/calendar.md`, and `docs/07_Client_Zero.md` for the v4 warehouse.
6. The retail dossier, `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`, and the Week 1 packs on main as the model for the chapter form.
7. `.claude/skills/day-pack-builder/SKILL.md` and its references, and `content/README.md`.
8. `.claude/skills/humanizer/SKILL.md`, the read every prose file passes.

Then read the skills CLAUDE.md routes to for each family, each in full before the pass that uses it.

**The domain.** Kalpa Retail continues, and the room met its story on Week 1 Monday. Each file carries what it needs from the dossier in its own words (a term's one-line meaning, a metric's formula, a role) and links to the dossier's section for more depth. Every chapter names:
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

**Every heading is a question, and every file stands on its own.** The question ladder in `the-standard.md` is the form.
- The day asks one question in the stakeholder's words. Each chapter asks the question the previous answer raised: in about 22 characters on the chapter opener and its pill (`## SECTION 2: Leave or buy less often?`), and in full as the opener's promise, the notebook's title cell, the notes' chapter heading and the scenario set's title.
- Under each chapter heading, **Who needs the answer.** names the person, the decision and the cost of a wrong answer, and **The questions on the way.** lists the chapter's four to six smaller questions. Each smaller question is a notebook heading, a notes subheading and a slide's italic subtitle; its answer is the notebook's **What happened.**, the paragraph beneath and the slide's action title.
- No heading is a bare label: "How much is one customer worth across all the years they keep buying?" replaces "Customer lifetime value, simply". Read each file's headings alone, in order; they must tell the day's argument.
- Each deck, notebook, exercise file, case brief, solution file and the take-home is understood with nothing else open: its scenario, its terms, its numbers and what an earlier chapter found (in a sentence, with the number) are on the page. Where the earlier finding is a plant, restate the rule the room drew from it, never the planted record.

**The decks, in depth.** A learner who missed the class follows every chapter from the slides and their notes. After the cover, one slide asks the day's question and lists the chapter questions. Each chapter opens on its question, then a map slide with who needs the answer and the smaller questions as a `timeline`, then about 10 to 14 slides in the notebook's rhythm: the need and who asks; the real company; the options with their sizing and the best-fit call; the thinking as a picture; per build step a predict slide, the logic or code in one short block, the result with its numbers as a picture, and the check; the plausible wrong answer with its exact number, why it is wrong with its check, and the fix; the second route; and a close that answers each smaller question in one line beside Kavya's review.

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

**The depth loop.** Passes 2 (domain) and 3 (problem first) are yours. Before pass 5, run the humanizer in file mode over every prose file: the notes, the cheat sheet, the pre-read, the board work, the day sheet, every exercise and solution file, the take-home, the Kahoot, the deck markdown (slide text and notes) and the notebooks' markdown through the scripts that write them. For passes 4 (rigor) and 5 (pedagogy and language), launch one fresh reviewer subagent each with the Agent tool and `model: opus`, read-only, once. The rigor reviewer also sits the day's exercises blind from the STUDENT files alone, and checks every STUDENT file against the later days' traps listed above. The pedagogy reviewer also runs the headings-only read on every file, opens three files at random alone to test that each stands on its own, looks at every rendered slide, and lists every humanizer pattern still present. Fix every finding. A second round runs only when a fix changed a method, a key or a number other files repeat, and it checks only those changes. Log the passes in the provenance.

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
- The llm-tic-scrubber scanner is clean on every markdown file, and the humanizer's read and the headings-only read are done on every file.

**Ship.** Commit in small commits whose messages say what changed, and push to the branch `w02-d{N}-chapters`. Do not open a pull request. Finish with a report containing:
- the day's question ladder: the day's question, each chapter's question and its smaller questions;
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

   Its headings are questions, per the reference. Run one review round before the Week 3 packs start.
2. **The Kalpa Health generator** (`data/generate_kalpa_health.py`) moves to the US setting:
   - dollars and US metro areas;
   - payers;
   - claims billed against payments posted, with denials.

   Keep the five sub-problems and the logic of each plant, keep the output deterministic, and add a
   contract check. Then:
   - rewrite the spine's "The week" section for the US setting;
   - record a decision that the Build 1 rubric's "rupees" reads "dollars";
   - run the sync.
3. **The Week 3 packs** (`D1`, `D3`, `D4`, `D5` and `SAT`) are rebuilt by cloud sessions in parallel,
   on the latest Opus at max effort, to standard v3: question headings with who needs the answer and
   the questions on the way, every file standing on its own, the humanizer's read and decks in depth.
   Each reads the new dossier, the regenerated data and the spine, and goes as deep as the Week 2 days:
   - the sub-problem briefs sized with options;
   - the checkpoint questions;
   - the mock bank's viva prompts per sub-problem;
   - the GD prompts, which climb in complexity;
   - the panel's question bank.

   Build weeks keep their own shape and carry no practice set.

## 5. Done

Week 1's recheck, Week 2 and Week 3 are done when every pack is merged at standard v3, both Saturday
papers are rechecked, every board card is at review-1, and `python3 scripts/sync_programme.py --check`
passes on main.

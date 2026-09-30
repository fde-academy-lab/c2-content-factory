# The standard a day pack is built to

The bar below was set by the requester on 29 September 2026 (business cases climbed in rungs, traps
that are plausible wrong numbers, and a 360-minute day filled with them) and raised twice on 30
September 2026. The first raise: every domain enters with its story, every technique answers a stated
problem with its alternatives and a sizing, a day runs in about six chapters that each pair one deck
chapter with one notebook, and every pack runs a five-pass depth loop. The second: every heading is a
plain question with the reason for learning it beneath (the question ladder), every deck, notebook,
exercise and paper is understood with nothing else open, every prose file passes the humanizer's read,
and a deck carries each chapter in full depth. Form still follows
`content/W01/D1`: its deck syntax, notebook helper and rhythm, companion build, workbook build and day
sheet are the model, and its rebuild to this bar becomes the model for content too. Where a week has
an approved spine in `docs/detailing/`, that spine sets each day's case, chapters and traps; this page
sets the form and the volume. The mechanics stay in the skills and scripts it points to.

## The bar

- **The domain comes first.** Most of the room has never worked in a business role. The first day a
  domain appears (retail and e-commerce in Week 1, US healthcare in Build 1, financial services in
  Build 2, SaaS and enterprise AI from Week 8) opens on its story from the domain's dossier: how the
  business makes money, who decides what, its metrics as formulas, its language and its compliance,
  which real company Kalpa's unit is like, and why analytics, ML, NLP and agents are needed there.
  Every later chapter names the metric at stake, who asks for it and what a wrong number costs them.
- **One case, climbed in chapters.** Each day is one Kalpa case climbed in about six chapters, each a
  harder business question. A chapter is answered with a number, the number is read as a decision,
  and the next chapter is the question that decision raises. Each chapter also names a real company
  that faces the same question, and a public case study where one sharpens the point, every fact
  checked against a source dated in the provenance.
- **The problem comes before the code.** Every technique arrives as the answer to a stated problem.
  A chapter lays out two to four ways a team could answer it, sizes them (rows, minutes, rupees,
  error), makes the best-fit call with its reason and names the fact that would change it; only then
  is the chosen way built, and the chapter closes by reaching the same answer a second way. Writing
  code is the last mile of a chapter, never its point.
- **Every heading is a question.** A learner who reads only the headings of a file, in order, sees what
  they are learning and why: each heading is a plain, specific question the section answers, the
  lines beneath it say who needs the answer for which decision and list the smaller questions on the
  way, and the section closes on the answer with its number. The question ladder below sets the form.
- **Every artifact stands on its own.** A deck, a notebook, an exercise file, a case brief, a
  take-home and a Saturday paper can each be understood with nothing else open. Each states its
  scenario, explains every term where it first appears, loads or prints every number it uses, and
  says in a sentence or two what an earlier chapter found, with its number, when it builds on it. A
  pointer to another file adds depth and is never needed to follow the page.
- **The wording reads as a person wrote it.** Every prose file passes the tic scanner and the
  humanizer skill's read (`.claude/skills/humanizer`), run in file mode so that code, data, paths and
  links stay as they are.
- **The tool is the calculator.** Python, SQL, pandas or Excel appears because a question needs it,
  after the thinking is drawn. Syntax is taught in passing, inside a chapter, never as a chapter.
- **Every trap is a plausible wrong number.** Each chapter stages at least one: the wrong number or
  output shown exactly, the decision it would have misled, the check that catches it, and the fix.
  A syntax or runtime error is met when it happens and gets two minutes and the last line of its
  trace; it never takes a trap slot, a chapter or an exercise item.
- **Nothing spoils a later day.** No file teaches a trap or a method that a later day stages, under
  any numbers, since the room is meant to meet each one cold; the week's spine lists every day's traps
  and is the checklist. A file may point back at an earlier day's trap by name.
- **Complexity climbs at three scales.** Within a chapter, from a one-line question to a multi-step
  analysis; across the day, from the chapters to the escalated case to the second case; across the
  week, as the data versions grow and the stakeholders push back harder.
- **Interview depth.** The questions are the ones analytics screens in Indian GCCs and product
  companies ask: metric design, a drop investigation, a reconciliation, reading an experiment, SQL
  and pandas semantics, a stakeholder who disagrees, and the design question (which approach, sized
  how, and what would make you switch). Each is answered in full in the study notes and in one breath
  in the day sheet.
- **Depth and breadth, proven by passes.** Every pack runs the five-pass depth loop below before it is
  called done; a pass that finds nothing to fix says so in the provenance.

## The day

Two blocks of 180 minutes and a TA-led practice lab after them, per `data/programme/facts.yaml`.
Lesson material carries durations only.

| Block | Minutes | What runs |
|---|---|---|
| Morning | 180 | The client's ask and the thinking drawn (20); chapters 1 to 5 of about 30 each; a break (10) before chapter 4 |
| Afternoon | 180 | Chapter 6 (30); the escalated case, unguided (50); the debrief of the room's wrong answers (15); a break (10); the second case, in pairs (40); the interview drill aloud, the design question among it (20); the Kahoot and tomorrow's ask (15) |
| After | The lab's length | The TA-led practice lab, run from the day's practice set |

On a domain's first day the domain story takes 45 minutes in place of the 20-minute ask, and chapter 5
moves to the afternoon, whose case blocks give up the difference; the day sheet shows which minutes.

A chapter is about 30 minutes live and runs in a fixed order: **the need** (the stakeholder's
problem, the metric and the decision riding on it, and the real company that faces it), **the
options** (two to four genuinely different ways to answer it, each sized on what separates them,
such as the rows or orders it needs, the error it risks and what it assumes, and the best-fit call
with the fact that would change it; a sizing column where every option scores the same separates
nothing), **the build** (the chosen way on Kalpa data, each step predicted before it runs), **the
trap** (the plausible wrong number, the check that catches it and the fix), **the second route**
(the same answer reached by an independent method, and when to switch; a route that re-derives the
first route's identity cannot fail when the first route is wrong, so it is not a second route), and
**Kavya's review**. The notebook carries more than the live minutes allow, since it is also the
self-study text. A faculty day, a lab day and any other exception take the shape their week's spine
gives them.

## Volume per teaching day

| Family | What the day ships |
|---|---|
| Decks | A morning deck (the ask, the thinking, chapters 1 to 5) and an afternoon deck (chapter 6, the case brief, the debrief of wrong answers, the second case, the interview drill, the close), each chapter opened by its own `## SECTION n:` and matching one notebook by number and title. At least half the slides carry a Mermaid diagram, a chart fence or a data picture. |
| Notebooks | One per chapter, about six, numbered and titled as the deck's chapters, each building on the one before it the way a first agent grows a tool, then several tools, then a loop, then memory: 20 to 36 cells, the chapter's options table and sizing, at least five visuals and five passing checks. The escalated case as a TODO twin with its executed solution; the second case as a notebook with its solution. |
| Exercises | A scenario set of 4 to 6 items per chapter, the escalated case brief in five parts, and the second case brief: about 35 items a day, every stem a business question, none testing syntax alone, and at least a third of them design items (the best-fit approach, a sizing, the alternative and when to switch). |
| Practice lab | A set of three or four problems climbing in difficulty, about an hour of work, with solutions and a TA note. |
| Interview | Ten to twelve questions: the row's anchors plus case-style follow-ups, tagged as the row tags them. |
| Kahoot | Eight items, including the return question from the day before. |
| Companion | A simulator for the day's key decision, where the learner changes one assumption and watches the number and the decision move. |
| Reading | Study notes of about 4,000 to 5,000 words carrying each chapter as a worked case with its options and sizing, the cheat sheet, the board work and tomorrow's pre-read; on a domain's first day, the domain dossier and its one-page card as well. |
| Domain | On a domain's first day: the dossier (study note), its one-page card (cheat sheet), the domain story deck chapter and the trainer's talk track for it. |

## The frame every artifact sits in

The cohort are trainee engineers in the data and AI team of Kalpa's Global Capability Centre, and
the stakeholders are the team's internal clients (`docs/07_Client_Zero.md`, section 1b). Three beats
recur, and each always looks the same, so a room learns to spot them.

| Beat | In the deck | In a notebook | Elsewhere |
|---|---|---|---|
| The client's ask | The cover quotes the stakeholder, and the first slide sets the scene in their words. | The first cell opens on it. | Every exercise stem, both case briefs and the take-home put it back to the learner. |
| Kavya's review | A `**Kavya's review.**` strip closes each chapter. | A quoted review follows each chapter's main result. | The companion's decision card closes on it. |
| The interview question | An `**In the interview.**` strip carries the tagged question. | An `### In the interview` section answers it in full. | The afternoon drill asks it aloud, the day sheet answers it in one breath, and the Saturday paper tests it. |

## The question ladder

The question ladder is the requester's idea of 30 September 2026, given its form here, for making what
a learner is learning, and why, visible at every level of every file. The day asks one question in the
stakeholder's words; each chapter asks the question the previous answer raised; each chapter climbs
through four to six smaller questions, each answered with a number before the next is asked.

| Level | The question | Where it is asked | Where it is answered |
|---|---|---|---|
| The day | The stakeholder's ask, as one question | The morning deck's cover, the day sheet's first line, the notes' title | The afternoon deck's close and the notes' last section |
| A chapter | The question the previous answer raised, in a short form of about 22 characters for the chapter opener and its pill, and in full everywhere else | The `## SECTION n:` title with the full question as its promise, the notebook's title and first cell, the notes' chapter heading, the scenario set's title | The chapter's answer slide, the notebook's last markdown cell, the chapter's last paragraph in the notes |
| A step | One of the chapter's smaller questions: the decision at stake, the options and their sizes, each build step, the trap, the second route, the review | A body slide's italic subtitle, a notebook heading, a notes subheading, an exercise part heading, a board drawing's heading | The slide's action title, the notebook's **What happened.** cell, the paragraph under the subheading |

A heading passes when it:
- is a question a learner could ask in plain words, ending in a question mark;
- makes sense on its own, naming the thing, the group or the number at stake, so "How much is one
  customer worth across all the years they keep buying?" passes where "Customer lifetime value,
  simply" does not;
- is answered in the section under it, with a number where the answer is a number;
- uses no term the file has not yet explained, since a formal name arrives after the problem that
  needs it.

Under every chapter heading, and under a notes or dossier section heading, two short paragraphs
follow. **Who needs the answer.** names the person, the decision the answer feeds and what a wrong
answer costs them. **The questions on the way.** lists the smaller questions in the order the
section takes them, which are the section's objectives. An exercise part heading asks the question the part
practises, and the line beneath it says where that skill is used at work, without naming a trap or
a key. The day sheet prints the whole ladder at its top, and the trainer asks the room each question
before its answer is shown.

**The headings-only read** is the test: read only a file's headings, in order. They should tell the
day's argument as a chain of questions, each following from the answer before it, and each
understandable without the text beneath it. The pass 5 reviewer runs it on every file.

## Executed files, and discoveries that stay with the learner

Every notebook ships executed and no learner file names a plant. Three devices reconcile the two:

1. **The empty your-turn cell.** The markdown above it gives the lines to type, and the cell ships
   with no source, so no saved output names the record and `nb_check.py` passes over it.
2. **Invented numbers for the mechanism.** Where a mechanism needs the plant to show, it is shown on
   a few invented records, labelled invented wherever they appear and recorded in the provenance,
   and the room then finds the real one in the file on its own.
3. **A trap that does not echo the plant.** A quiz or exercise trap uses a different value from the
   planted one.

## Family by family

### Decks, in `slides/`

The syntax is the docstring of `scripts/build_deck.py`, and the look is `scripts/deck_layout.py`
reading `scripts/brand.py`. `half1` is the morning deck and `half2` the afternoon deck.

- A deck teaches on its own. A learner who missed the class can follow every chapter from its slides
  and their notes, so no slide sends the reader to a notebook or the notes for something it needs.
- The morning deck opens on a cover with the client's words (`Quote:` and `Who:`) and a slide that
  asks the day's question and lists the chapter questions in order. Then comes one chapter per
  notebook, each opened by `## SECTION n:` whose title is the chapter's short question and whose
  italic promise is the full question with the decision riding on it, its number and title matching
  the notebook's. The slide after each opener is the chapter's map: **Who needs the answer.** in a
  sentence, and the chapter's smaller questions as a `timeline`.
- A chapter's slides run the notebook's rhythm, about 10 to 14 of them: the need and who asks, the
  real company that faces it, the options with their sizing and the best-fit call, the thinking as a
  picture, and for each build step a predict slide, the logic or code in one short block, the result
  with its numbers as a picture, and the check. Then **the plausible wrong answer** with the exact
  wrong number, **why it is wrong** with the check that catches it, the fix and what it changes, the
  second route, and a close that answers each of the chapter's questions in one line beside Kavya's
  review.
- Every body slide's italic subtitle is the smaller question it answers, ending in a question mark,
  and its action title of at most 54 characters is the answer, so every slide shows a question and
  its answer. A predict slide's title is its question and its body the lettered options, and the next
  slide answers it. Each body slide carries a `notes` fence that opens on LIVE or SELF-STUDY with its
  minutes, says what to say, ask and watch for, and ends on the transition; a self-study slide is
  numbered `D`.
- Numbers go in `stats`, parallel things in `cards`, a run of beats in `timeline`, a proportion in
  `bar`; diagrams are Mermaid, styled with the `known`, `unknown`, `bet` and `bad` classes, and a
  chart that needs real axes is drawn in the notebook and described on the slide.
- The afternoon deck closes on the sentence to the stakeholder, the crux lines the cheat sheet repeats
  word for word, and tomorrow's question, left open.

### Notebooks, in `notebooks/`

The helper is `scripts/c2kit.py`, and `scripts/nb_make.py` assembles a notebook and executes it cold
in its own folder. `content/W01/D1/notebooks/` shows the rhythm; the chapter structure below is the bar.

- One notebook per chapter, named and numbered as the deck's chapter, and each building on the one
  before it: the first cell names the week, the day and the chapter, asks the chapter's question in
  full, gives **Who needs the answer.** and **The questions on the way.**, names the metric at
  stake, and says in a sentence or two what the previous notebook found, with its number, and what
  this one adds.
- A notebook stands on its own. Its setup cell loads its own data, it runs cold with nothing else
  open, and it recomputes or restates whatever it takes from an earlier notebook. Where the earlier
  finding is a plant, it restates the rule the room drew from it, never the planted record.
- A `## The options` section follows the need: a table of the two to four ways to answer it, a sizing
  cell that computes each one's cost on this data (rows touched, seconds, rupees, error), and the
  best-fit call with the fact that would change it. `## A second route` near the end reaches the same
  number another way and asserts the two agree.
- The chapter climbs three or four levels, each a harder form of the question on the same data. Each
  level runs:
  a numbered heading that asks the level's question, `**Predict before you run.**` with lettered
  options, the code, the result as a table or a chart, `**What happened.**` with the answer letter,
  the answer to the heading's question and what the number means for the decision, and a check. The
  notebook's last markdown cell answers each of its questions in one line with its number.
- The trap is its own level: `**The plausible wrong answer.**` computes the wrong number the way a
  hurried analyst would, `**Why it is wrong.**` names the mistake in business terms, a check exposes
  it, and the fix recomputes the number with what changed stated in rupees, customers or rows.
- Charts come from the data at every level that has a number: `kit.columns` for a comparison across
  groups, `kit.line` for a trend or a total against plan, `kit.bridge` for a reconciliation or a
  decomposition, `kit.strip` for a distribution and `kit.bars` for a ranking. Diagrams of the thinking
  come from the other builders.
- `kit.expect_error()` is for a real runtime error met on the way, shown in one cell with its last
  line; the notebook never builds a section around one.
- `### In the interview` answers the chapter's tagged questions in full, the design question among
  them, and a `### Depth:` section holds the stretch material. The last cell calls
  `kit.check_summary()`.
- The escalated case is a TODO twin with its executed solution, per
  `notebook-builder/references/exercise-notebooks.md`, and the second case is a notebook with its
  solution in `exercises/solutions/`.
- A check cell under a TODO checks a value the learner's code computed, in a later cell, and never
  prints or tests the key's words, since a check that reveals the answer before anything runs is a
  worked example with the working removed.

### The companion page, in `demos/`

Build with `scripts/companion/` through `python3 scripts/build_companion.py <page>`; the model page is
`content/W01/D1/demos/C2_W01_D01_revenue_tree_STUDENT.html`.

- The page is a simulator for the day's key decision: a guided walk through the chapters, a control for
  each assumption that matters, the number and the decision redrawn live with `C2K.bridge`,
  `C2K.columns`, `C2K.line` or `C2K.strip`, experiment cards that each change one assumption, and a
  glossary.
- An experiment that would touch a plant runs on invented records, and scrolling stays instant, since
  `html_sweep.py` times out on a button that smooth scrolling is still moving.

### The decision workbook, in `demos/`

Open `content/W01/D1/demos/C2_W01_D01_build_decision_tool_TRAINER.py`, the script that writes the
workbook. A start tab, one tab per taught decision, and an export tab that releases the brief only
when every tab is fixed; yellow inputs (`FFF4C2`); one planted formula defect per tab that the tab's
own check line exposes; and the recalc manifest that `xlsx_recalc.py` runs.

### Exercises, the practice lab, the take-home and the Kahoot

- `exercises/` holds an index, `guided/`, `unguided/` with one scenario set per chapter and the two case
  briefs, `practice/` with the lab set, and `solutions/` with every answer.
- Every exercise file is sat with nothing else open: it carries its case in the stakeholder's words,
  its data or exhibit, and every definition its items use. Each part heading asks the question the
  part practises, with a line beneath on where that skill is used at work.
- The devices are the business ones: choose the decision, spot the plausible wrong output, predict the
  number, fix the logic, order the analysis, and match a question to its method. Every stem is written
  as a question so the distractor audit finds it, and each solution file opens on an `Answers:` line
  and gives, per item, the stem in one line, why the key is right and why each other letter fails, so
  the solution reads without the set beside it.
- The practice set climbs in difficulty, ends on a problem that combines the day's chapters, and has a
  TA note in `trainer/` saying where learners stall and the one hint to give for each problem.
- The take-home runs on a second sample from `data/generate_client_zero.py` carrying its own plants,
  which only the day sheet names, and its self-check lists the numbers a learner should reach.
- Each Kahoot item carries a `*Tests: ...*` line naming what it tests.

### Notes, cheat sheet, board work and pre-read

- The study notes, about 4,000 to 5,000 words on the `study-notes-builder` spine, carry each chapter
  as a worked case with its options, sizing and trap, the interview questions with full answers, and
  a `| Term |` table that the cheat sheet prints in its foot. Their headings are the day's question
  ladder: each chapter heading is the chapter's full question, opens on **Who needs the answer.** and
  **The questions on the way.**, and the chapter closes on its answer.
- The cheat sheet's markdown ships beside the PDF from
  `python3 scripts/build_cheatsheet.py <sheet> --verified "<date>"`, panel one carries the day's
  picture, and each panel's heading is the question the panel answers.
- The board work lists the drawings in the order they go up, as Mermaid, each headed by the question
  it answers, and ends on what is on the board when the day ends.
- The pre-read opens on tomorrow's stakeholder message and carries a vocabulary gap table, one thing
  to think about, the check for tonight and the line worth carrying in, each under a question
  heading.

### Day sheet and provenance

- The day sheet carries the module and date sync blocks (and the faculty-day block on a faculty day);
  the day's question ladder, which the trainer asks the room in order; the five-row envelope of start
  from, go as far as, stop before, comes later and cut first; per block,
  a flow of its parts with minutes and a table of slides, the file beside them, what must land and
  what to cut; every trap with its exact wrong number and the check that catches it; checkpoints; the
  plant table with what to do if nobody finds each; the day's numbers; the interview answers in one
  breath; the practice lab note; and which file serves which moment.
- The provenance carries the sources, the data command, the plants and where each is used, every
  decision that departs from a source, everything invented, each link with its check date, and the
  tool versions the numbers and outputs came from.

## The depth loop

Every pack runs five passes before it is called done, and the provenance logs each: what the pass
asked, what it found and what changed. A pass that finds nothing says so.

| Pass | Who runs it | The question it must answer yes to |
|---|---|---|
| 1. Draft | The builder | Is every chapter built from the row, the week's spine and the domain's dossier, in the chapter order? |
| 2. Domain | The builder | Could a learner who has never worked in a business say, for every chapter, who asks, why the metric matters, what a wrong number costs and which real company faces the same question, from that chapter's own deck, notebook and exercises alone? |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with two or more options, a sizing and the best-fit call with what would change it, and is the code its last mile? |
| 4. Rigor | A fresh reviewer agent | Do the notebooks run cold, does every trap show its exact wrong number and its check, does every sizing's arithmetic hold, is every real-world fact sourced, and would a strong interviewer accept every answer? The reviewer also sits the day's exercises blind, from the STUDENT files alone, and names every key a cue gives away and every item labelled hard or design that one step answers, and checks every STUDENT file against the traps later days stage. |
| 5. Pedagogy and language | A fresh reviewer agent, after the builder has run the humanizer over every prose file | Does each chapter pair one deck chapter with one notebook that builds on the last, does every file pass the headings-only read and stand on its own, does every deck carry each chapter in full, do the devices vary, does every diagram read at print size, and is the language free of the tics the scrubber finds and the patterns the humanizer lists? |

A reviewer writes findings, never edits; the builder fixes and records the fix. Passes 4 and 5 run
once each. A second round runs only when a fix changed a method, a key or a number other files
repeat, and it checks only those changes; every other fix is confirmed by the builder's own proof
run. The orchestrating session's review before merge is one read against this page, and its
findings are fixed in one pass.

## Proof

`python3 scripts/verify.py content/W{ww}/D{d}` runs every gate, and
`python3 scripts/build_companion.py content/W{ww}/D{d} --check` and
`python3 scripts/sync_programme.py --check` follow it. A deck is also rendered through LibreOffice to
PDF and looked at slide by slide, with the Carlito font installed (`fonts-crosextra-carlito`) so
Calibri text measures as it will on a trainer's laptop. Two reads no script makes close the pack:
the headings-only read of every file, and the humanizer's read of every prose file in file mode,
with the notebooks' markdown changed through the script that writes them.

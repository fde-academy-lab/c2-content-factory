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
sets the form. From Week 4 on, a day runs in the shape of "The teaching approach" below: the concept
block (one chapter per row subtopic) and then the case chapters, each chapter paired with one
notebook, with the week's spine setting the minutes and sizes; "Volume per teaching day" and the
five-pass "depth loop" give way to the spine's sizes and the three cold reads, while "The day", "The
question ladder" and every family's form stay in force as this page states them. The mechanics stay
in the skills and scripts it points to.

## The teaching approach

The requester set this on 12 October 2026 for every week, day, Saturday and build brief made from
then on (decision `teaching-approach` in data/programme/facts.yaml), and on 13 October 2026 set how
the concepts and the case share a day (decision `concept-first-case-second`). Weeks 1 to 3 were
built before it and keep their shape until they are rebuilt.

0. **The topics lead.** The deck opens on the day's topic (the row's Day focus column), the week map
   with today lit, the topics slide (every bullet of the row's Subtopics column, verbatim and in the
   row's order, each with the chapter that teaches it, its minutes and its notebook) and a concept
   map: a mermaid map that names the same bullets, each node joined to the earlier and later ideas it
   depends on, with today's nodes lit and the case's node beneath them. The chapters follow the row's
   order unless the week's spine records a reason to teach them in another. Slide five is the case
   ticket in one slide, as the destination the topics will be used on.
   Then the concept block: one chapter per subtopic, about 8 to 25 minutes each and 60 to 120 minutes
   in all, each opener written `## SECTION n: <subtopic>: <short question>?`, with the subtopic as
   the row words it, a short question of about 24 characters that the pills print, and an italic
   promise saying what the chapter delivers. A concept chapter teaches from zero on one simple, complete,
   relatable educational example with invented numbers labelled invented (a canteen that pays per
   token, ten tea-stall orders, two coaching batches, four days of cups), in this order: the broken
   default or the misconception with a prediction, the hand count on the tiny numbers, the picture
   that makes the mechanism visible, the formula or rule named last, a glimpse of three to six lines
   of code that reproduce the count, three to five one-sentence rules a learner photographs, and the
   map node that links the idea to the previous one, the next one and the case chapter that applies
   it. Each concept chapter pairs with one notebook of 8 to 18 cells carrying the same name. The row's
   Subtopics column is the chapter list; a subtopic the spine adds carries "(added by the spine)" and
   its reason, and a subtopic the row carries is never dropped.
1. **The case carries the day.** After the concept block, the case: an engineering case at a company the learners use (Uber,
   Ola, Swiggy, Zomato, Blinkit, Zepto, Flipkart, Amazon India, PhonePe, Google, an AI startup and the
   like) in a named city, state or country: the product surface, the metric, its value before and
   after with dates, the data the analyst holds (tables and columns), the ask, and the caveats already
   known. No stakeholder drama opens a day. Each case carries the line "Illustrative case: the company
   is real, the situation and the data are synthetic, built for this class", claims nothing the company
   actually did, and draws any public fact from a source checked and dated the day it entered. Its data
   come from the day's own seeded generator, and every number a learner sees sits in the day's facts
   file. Kalpa stays the programme's client: the TA lab and one unguided exercise run the same method on
   Kalpa's version of the problem, which keeps the weeks connected and the Saturday bank in reach.
2. **The ladder climbs from a weak learner to a hard interview.** The case breaks into five to seven
   sub-problems, each a level up: L1 the situation understood and counted by hand on about twelve rows;
   L2 the same count on the full data in the smallest code; L3 the trap, the denominator and the
   segment that drives it; L4 the caveats an engineer must name (data quality, mix, seasonality,
   interference, selection, cause); L5 the decision with its cost and the objection it meets; L6 the
   interview as Uber, Swiggy, Google and AI-startup screens ask it, with what the interviewer listens
   for, a weak and a hire-grade answer side by side, the follow-ups, and one AI-company variant of the
   same idea. Every word a newcomer would not know is defined where it first appears.
3. **Every idea is taught in a blend of styles** (`references/teaching-styles.md` gives each style's
   moves): the misconception or the surprise first and a prediction before the reveal (Veritasium); the
   maths derived visually from tiny numbers before the formula is named (3Blue1Brown, StatQuest); a
   line-by-line code-along from the raw table to a working answer (Krish Naik); a connected map of how
   today's idea links to what came before and what comes next (ByteByteGo); a ladder of practice
   problems from easy to interview grade (takeUforward); problem-first interactivity (Brilliant and the
   explorable explanations); and a plain explanation a newcomer could repeat (the Feynman technique).
4. **Each week ships one interactive explorer** that grows day by day: an HTML page with a connected
   map of the week on its home screen and one section per day whose scenes animate the mechanism, let
   the viewer move a control and predict before the reveal, and name the formula last. It reveals no
   planted value and passes `scripts/html_sweep.py`.
5. **Pictures are drawn by our own code**: mermaid for mechanisms and maps, matplotlib for data
   pictures placed by image lines, and short GIFs from our own data with a still beside each.
6. **Volume follows the minutes.** A day runs in the concept block (one chapter per row subtopic,
   60 to 120 minutes in all) and three or four case chapters sized to the remaining trainer minutes,
   with no item, slide or word quota beyond the sizes the week's spine gives; one notebook per chapter
   in both halves, plus the lab notebook. Review is one fresh-graduate read, one hiring-interviewer
   read, one trainer's read with the row open (where is each subtopic taught, or "not found"), one fix
   pass and verify.py, which runs the coverage gate.
7. **Every artefact family carries the approach**, and each may add moves of its own:
   - *Decks* open on the day's topic, the week map, the topics slide, the concept map and the ticket as
     the destination;
     the concept chapters follow, each named by its subtopic and built on its educational example in
     the order item 0 gives; then the case chapters, each one sub-problem with its level (L1 to L6) and
     the subtopics it applies on the opener; inside a case chapter the misconception and a prediction
     come first, then the derivation on the twelve rows, the formula recalled by its concept chapter's
     name, a glimpse of the code, the trap shown exactly, and a map slide that links the idea to
     earlier and later ones.
   - *Notebooks*, one per chapter, named as the chapter is: a concept notebook carries its subtopic in
     its file name and its first heading (`C2_W04_D01_02_north_star_and_guardrails_STUDENT.ipynb`,
     opening `# North-star and guardrail metrics: which number does the plan chase, and which must not
     fall?`), builds the educational example inline, labelled invented and recorded in the facts file
     under `toy_` ids, counts it by hand and by code and asserts the two agree, draws the picture, names
     the formula last and ends on the rules; a case notebook codes along from the raw table, one plain
     sentence above each cell, the hand count first, then the full-data step, the trap, the second
     route asserted equal and the AI-company variant at the end, in ponytail-small code, and its first
     cell names the subtopics it applies and the concept notebooks that taught them.
   - *Exercises* are a ladder from L1 to L6 in the takeUforward manner, each item tagged with its level
     and the kind of company whose screens ask it; worked examples fade (one fully worked, one half
     worked, then blank); at least a third are design items; one re-runs the method on Kalpa; and some
     items hand the learner a plausible wrong answer to debug.
   - *Case studies and briefs* follow the ticket: the situation, the data dictionary, the sub-problems,
     the caveats, the deliverable, and what a strong answer contains.
   - *Projects* (mini projects, build weeks, the capstone) are posed as engineering tickets at a
     relatable company or a Kalpa unit on real, messy data, with milestones that climb the levels and a
     demo and defence questioned at interview grade.
   - *Saturday papers* set their items in cases, climb the levels, and stay interview grade.
   - *Notes and cheat sheets* explain each idea plainly enough to repeat (Feynman), carry the visual
     derivation and the connected map, and close on what an interviewer checks.
   - *Interview preparation* ships transcripts with weak and hire-grade answers side by side, the
     scorecard, the follow-ups, the AI-company variant and a guesstimate with its published anchor.
   - *Across the week*, practice retrieves earlier days (the Kahoot's return questions and spaced recall
     items), interleaves topics once each is learned, and uses peer instruction where a question splits
     the room: predict, vote, discuss with a neighbour, vote again, then the reveal.
8. **The coverage matrix is the day's contract with the row.** Every teaching day ships
   `internal/C2_W{ww}_D{dd}_coverage_INTERNAL.md`, in the shape `references/coverage-matrix.md` sets:
   each row subtopic, verbatim, against its chapter title, its slides, its notebook, its exercise
   items, its Kahoot items and its minutes, then each case chapter against the subtopics it applies.
   `scripts/coverage_check.py`, run by `verify.py`, fails the pack when a subtopic has no chapter or no
   notebook carrying its name, when an entry names a slide, file or item that does not exist, or when
   a case chapter applies no subtopic. The matrix is also the trainer's topic table: the day sheet
   prints it, and the study notes' topic sections follow its order.

## The bar

- **The domain comes first.** Most of the room has never worked in a business role. The first day a
  domain appears (retail and e-commerce in Week 1, US healthcare in Build 1, financial services in
  Build 2, SaaS and enterprise AI from Week 8) opens on its story from the domain's dossier: how the
  business makes money, who decides what, its metrics as formulas, its language and its compliance,
  which real company Kalpa's unit is like, and why analytics, ML, NLP and agents are needed there.
  Every later chapter names the metric at stake, who asks for it and what a wrong number costs them.
- **The topics first, then one case climbed in chapters.** Each day teaches the row's subtopics as
  named concept chapters on educational examples, then climbs one case in three or four chapters,
  each a harder business question. A case chapter is answered with a number, the number is read as a
  decision, and the next chapter is the question that decision raises. In Weeks 1 to 3 each chapter
  also names a real company that faces the same question; from Week 4 on a real company appears
  where it brings a decision and what it cost, every fact checked against a source dated in the
  sources list.
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
| Morning | 180 | The topic, the week map, the topics slide, the concept map and the ticket as the destination (10); the concept block, one chapter per row subtopic of about 8 to 25 minutes (60 to 120); a break (10); the first case chapters on the twelve rows and the full data (the rest) |
| Afternoon | 180, or 60 before an IITGN block | The remaining case chapters (the trap, the caveats, the decision with its cost); the unguided round; the interview room; the Kahoot and tomorrow's ask (15); on a day with no block, the second case, the written case or the studio as the spine sets them |
| After | The lab's length | The TA-led practice lab, run from the day's practice set |

Where the trainer's minutes are tight (a faculty day leaves 240), the concept block takes its minutes
from the beats the case chapters no longer need: a case chapter that once introduced an idea
mid-climb now recalls it by its concept chapter's name in one line and goes straight to the data, and
the week's spine shows, per day, which case beats moved into which concept chapter.

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
| A chapter | The `## SECTION n:` title written `<topic>: <short question>?`: the topic first (for a concept chapter, the row's subtopic as the row words it, which the coverage gate reads; for a case chapter, the case step with the subtopics it applies), then a short question that starts lower-case and runs to about 24 characters, since the pills, the footers and the cover's chapter strip print it (`deck_check.py` measures the built pill); the italic promise beneath says what the chapter delivers or asks the question the previous answer raised in full | The `## SECTION n:` opener, the notebook's file name and first heading (`# Topic: question?`), the notes' chapter heading, the scenario set's title | The chapter's answer slide, the notebook's last markdown cell, the chapter's last paragraph in the notes |
| A step | One of the chapter's smaller questions: the decision at stake, the options and their sizes, each build step, the trap, the second route, the review | A body slide's italic subtitle, a notebook heading, a notes subheading, an exercise part heading, a board drawing's heading | The slide's action title, the notebook's **What happened.** cell, the paragraph under the subheading |

A heading passes when it:
- is a question a learner could ask in plain words, ending in a question mark;
- makes sense on its own, naming the thing, the group or the number at stake, so "How much is one
  customer worth across all the years they keep buying?" passes where "Customer lifetime value,
  simply" does not;
- is answered in the section under it, with a number where the answer is a number;
- uses no term the file has not yet explained, since a formal name arrives after the problem that
  needs it.

A chapter opener is the one heading that leads with a topic. It is written
`## SECTION n: <topic>: <short question>?`, so the topic is the learner's recall handle ("Leading
against lagging indicators"), the short question is what the pills and footers print ("which one
moves first?"), and the italic promise beneath says what the chapter delivers or asks the fuller
question ("Which of the city's numbers moves before the north star, and which only confirms it
later?"). A topic that has a colon of its own splits at the last colon. The day's concept map slide prints every concept chapter's
topic, so a learner who reads only the map and the openers sees the day's topics in the row's order,
and a learner who reads the short questions and the promises sees the day's argument.

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
- The morning deck opens on a cover that names the day's topic (the row's Day focus) and asks the
  day's question, then the week map with today lit, then the topics slide and the concept map (a
  mermaid map of every subtopic in the row's order, today's nodes lit, each node's text the subtopic
  as the row words it), then the case ticket in one slide as the destination. Then comes one chapter
  per notebook: the concept chapters, each opened by `## SECTION n: <subtopic>: <short question>?`
  with the subtopic as the row words it and an italic promise saying what the chapter delivers; then
  the case chapters, each opened the same way with the case step and the subtopics it applies as its
  topic and the decision riding on it in the promise, its number and title matching the notebook's.
  The slide after each opener is the
  chapter's map: the subtopic verbatim, **Who needs the answer.** in a sentence, the chapter's smaller
  questions as a `timeline`, and, on a case chapter, the line "Applies: ..." naming the concept
  chapters it uses. In Weeks 1 to 3 the cover quotes the client (`Quote:` and `Who:`) and the chapter
  titles are short questions, and those packs keep that until rebuilt.
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
  before it. A concept notebook's file name carries its subtopic in snake case
  (`C2_W04_D01_03_leading_against_lagging_STUDENT.ipynb`) and its first cell opens
  `# <the subtopic as the row words it>: <the chapter's question>`, then **Who needs the answer.** and
  **The questions on the way.**, then the educational example's table built inline and labelled
  invented (the one place a notebook may hold records in a cell, since a learner must see all of
  them; the numbers sit in the facts file under `toy_` ids). A case notebook's first cell names the
  week, the day and the chapter, asks the chapter's question in full, gives **Who needs the answer.**
  and **The questions on the way.**, names the metric at stake, names the subtopics it applies and
  the concept notebooks that taught them, and says in a sentence or two what the previous notebook
  found, with its number, and what this one adds.
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
run. From Week 4 on, passes 4 and 5 give way to three cold reads, each by a fresh agent on the Opus
model who writes findings only: the fresh graduate (every word, step and output it could not
picture), the hiring interviewer (every answer a strong screen would reject), and the trainer who did
not write the day, with the row open (each subtopic and the slide, notebook and exercise where it is
taught, or "not found", which is a stop). One fix pass follows. The orchestrating session's review
before merge is one read against this page with the coverage matrix open, and its findings are fixed
in one pass.

## Proof

`python3 scripts/verify.py content/W{ww}/D{d}` runs every gate, `scripts/coverage_check.py` among them
on a teaching day from Week 4 on, and
`python3 scripts/build_companion.py content/W{ww}/D{d} --check` and
`python3 scripts/sync_programme.py --check` follow it. A deck is also rendered through LibreOffice to
PDF and looked at slide by slide, with the Carlito font installed (`fonts-crosextra-carlito`) so
Calibri text measures as it will on a trainer's laptop. Two reads no script makes close the pack:
the headings-only read of every file, and the humanizer's read of every prose file in file mode,
with the notebooks' markdown changed through the script that writes them.

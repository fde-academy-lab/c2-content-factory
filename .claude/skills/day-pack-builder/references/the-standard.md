# The standard a day pack is built to

The bar below was set by the requester on 29 September 2026: business cases climbed in rungs,
traps that are plausible wrong numbers, and a 360-minute day filled with them. Form still follows
`content/W01/D1`: its deck syntax, notebook helper and rhythm, companion build, workbook build and day
sheet are the model, and its rebuild to this bar becomes the model for content too. Where a week has
an approved spine in `docs/detailing/`, that spine sets each day's case, rungs and traps; this page
sets the form and the volume. The mechanics stay in the skills and scripts it points to.

## The bar

- **One case, five rungs.** Each day is one Kalpa case climbed in five rungs, each a harder business
  question. A rung is answered with a number, the number is read as a decision, and the next rung is
  the question that decision raises.
- **The tool is the calculator.** Python, SQL, pandas or Excel appears because a question needs it,
  after the thinking is drawn. Syntax is taught in passing, inside a rung, never as a rung.
- **Every trap is a plausible wrong number.** Each round stages at least one: the wrong number or
  output shown exactly, the decision it would have misled, the check that catches it, and the fix.
  A syntax or runtime error is met when it happens and gets two minutes and the last line of its
  trace; it never takes a trap slot, a chapter or an exercise item.
- **Complexity climbs at three scales.** Within a round, from a one-line question to a multi-step
  analysis; across the day, from the rounds to the escalated case to the second case; across the
  week, as the data versions grow and the stakeholders push back harder.
- **Interview depth.** The questions are the ones analytics screens in Indian GCCs and product
  companies ask: metric design, a drop investigation, a reconciliation, reading an experiment, SQL
  and pandas semantics, a stakeholder who disagrees. Each is answered in full in the study notes and
  in one breath in the day sheet.

## The day

Two blocks of 180 minutes and a TA-led practice lab after them, per `data/programme/facts.yaml`.
Lesson material carries durations only.

| Block | Minutes | What runs |
|---|---|---|
| Morning | 180 | The client's ask and the thinking drawn (20); three rounds of 50, with a 10-minute break before the third |
| Afternoon | 180 | The escalated case, unguided (60); the debrief of the room's wrong answers (15); a break (10); the second case, in pairs (45); the interview drill aloud (30); the Kahoot and tomorrow's ask (20) |
| After | The lab's length | The TA-led practice lab, run from the day's practice set |

A round is 50 minutes: the question and its picture, the trainer's demonstration on Kalpa data, the
trap and its wrong number, the room running a harder variant, and Kavya's review. A faculty day, a
lab day and any other exception take the shape their week's spine gives them.

## Volume per teaching day

| Family | What the day ships |
|---|---|
| Decks | A morning deck of about 40 slides (the ask, the thinking, three rounds) and an afternoon deck of about 20 (the case brief, the debrief of wrong answers, the second case, the interview drill, the close). At least half the slides carry a Mermaid diagram, a chart fence or a data picture. |
| Notebooks | One per round, each climbing four levels in 24 to 36 cells, with at least eight visuals and eight passing checks; the escalated case as a TODO twin with its executed solution; the second case as a notebook with its solution. |
| Exercises | A scenario set of 6 to 8 items per round, the escalated case brief in five parts, and the second case brief: about 35 items a day, every stem a Kalpa business question, none testing syntax alone. |
| Practice lab | A set of three or four problems climbing in difficulty, about an hour of work, with solutions and a TA note. |
| Interview | Ten to twelve questions: the row's anchors plus case-style follow-ups, tagged as the row tags them. |
| Kahoot | Eight items, including the return question from the day before. |
| Companion | A simulator for the day's key decision, where the learner changes one assumption and watches the number and the decision move. |
| Reading | Study notes of about 4,000 words carrying the three rounds as worked cases, the cheat sheet, the board work and tomorrow's pre-read. |

## The frame every artifact sits in

The cohort are trainee engineers in the data and AI team of Kalpa's Global Capability Centre, and
the stakeholders are the team's internal clients (`docs/07_Client_Zero.md`, section 1b). Three beats
recur, and each always looks the same, so a room learns to spot them.

| Beat | In the deck | In a notebook | Elsewhere |
|---|---|---|---|
| The client's ask | The cover quotes the stakeholder, and the first slide sets the scene in their words. | The first cell opens on it. | Every exercise stem, both case briefs and the take-home put it back to the learner. |
| Kavya's review | A `**Kavya's review.**` strip closes each round. | A quoted review follows each round's main result. | The companion's decision card closes on it. |
| The interview question | An `**In the interview.**` strip carries the tagged question. | An `### In the interview` section answers it in full. | The afternoon drill asks it aloud, the day sheet answers it in one breath, and the Saturday paper tests it. |

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

- The morning deck opens on a cover with the client's words (`Quote:` and `Who:`), then a chapter per
  round, each opened by `## SECTION n:` with an italic promise.
- A round's slides run: the question, the thinking as a picture, the demonstration's steps with their
  numbers, **the plausible wrong answer** with the exact wrong number, **why it is wrong** with the
  check that catches it, the fix and what it changes, the harder variant the room runs, and Kavya's
  review.
- Every body slide has an action title of at most 54 characters, an italic subtitle, and a `notes`
  fence that opens on LIVE or SELF-STUDY with its minutes, says what to say, ask and watch for, and
  ends on the transition. A question slide is followed by its answer slide, and a self-study slide is
  numbered `D`.
- Numbers go in `stats`, parallel things in `cards`, a run of beats in `timeline`, a proportion in
  `bar`; diagrams are Mermaid, styled with the `known`, `unknown`, `bet` and `bad` classes, and a
  chart that needs real axes is drawn in the notebook and described on the slide.
- The afternoon deck closes on the sentence to the stakeholder, the crux lines the cheat sheet repeats
  word for word, and tomorrow's question, left open.

### Notebooks, in `notebooks/`

The helper is `scripts/c2kit.py`, and `scripts/nb_make.py` assembles a notebook and executes it cold
in its own folder. `content/W01/D1/notebooks/` shows the rhythm; the round structure below is the bar.

- One notebook per round, named for its question. The first cell names the week, the day and the
  round, states the stakeholder's question, quotes Kavya's review, and says what the previous round
  established.
- The round climbs four levels, each a harder form of the question on the same data. Each level runs:
  a numbered heading that states the claim, `**Predict before you run.**` with lettered options,
  the code, the result as a table or a chart, `**What happened.**` with the answer letter and what
  the number means for the decision, and a check.
- The trap is its own level: `**The plausible wrong answer.**` computes the wrong number the way a
  hurried analyst would, `**Why it is wrong.**` names the mistake in business terms, a check exposes
  it, and the fix recomputes the number with what changed stated in rupees, customers or rows.
- Charts come from the data at every level that has a number: `kit.columns` for a comparison across
  groups, `kit.line` for a trend or a total against plan, `kit.bridge` for a reconciliation or a
  decomposition, `kit.strip` for a distribution and `kit.bars` for a ranking. Diagrams of the thinking
  come from the other builders.
- `kit.expect_error()` is for a real runtime error met on the way, shown in one cell with its last
  line; the notebook never builds a section around one.
- `### In the interview` answers the round's tagged questions in full, and a `### Depth:` section holds
  the stretch material. The last cell calls `kit.check_summary()`.
- The escalated case is a TODO twin with its executed solution, per
  `notebook-builder/references/exercise-notebooks.md`, and the second case is a notebook with its
  solution in `exercises/solutions/`.

### The companion page, in `demos/`

Build with `scripts/companion/` through `python3 scripts/build_companion.py <page>`; the model page is
`content/W01/D1/demos/C2_W01_D01_revenue_tree_STUDENT.html`.

- The page is a simulator for the day's key decision: a guided walk through the rounds, a control for
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

- `exercises/` holds an index, `guided/`, `unguided/` with one scenario set per round and the two case
  briefs, `practice/` with the lab set, and `solutions/` with every answer.
- The devices are the business ones: choose the decision, spot the plausible wrong output, predict the
  number, fix the logic, order the analysis, and match a question to its method. Every stem is written
  as a question so the distractor audit finds it, and each solution file opens on an `Answers:` line
  and gives, per item, why the key is right and why each other letter fails.
- The practice set climbs in difficulty, ends on a problem that combines the day's rounds, and has a
  TA note in `trainer/` saying where learners stall and the one hint to give for each problem.
- The take-home runs on a second sample from `data/generate_client_zero.py` carrying its own plants,
  which only the day sheet names, and its self-check lists the numbers a learner should reach.
- Each Kahoot item carries a `*Tests: ...*` line naming what it tests.

### Notes, cheat sheet, board work and pre-read

- The study notes, about 4,000 words on the `study-notes-builder` spine, carry each round as a worked
  case with its trap, the interview questions with full answers, and a `| Term |` table that the cheat
  sheet prints in its foot.
- The cheat sheet's markdown ships beside the PDF from
  `python3 scripts/build_cheatsheet.py <sheet> --verified "<date>"`, and panel one carries the day's
  picture.
- The board work lists the drawings in the order they go up, as Mermaid, and ends on what is on the
  board when the day ends.
- The pre-read opens on tomorrow's stakeholder message and carries a vocabulary gap table, one thing
  to think about, the check for tonight and the line worth carrying in.

### Day sheet and provenance

- The day sheet carries the module and date sync blocks (and the faculty-day block on a faculty day);
  the five-row envelope of start from, go as far as, stop before, comes later and cut first; per block,
  a flow of its parts with minutes and a table of slides, the file beside them, what must land and
  what to cut; every trap with its exact wrong number and the check that catches it; checkpoints; the
  plant table with what to do if nobody finds each; the day's numbers; the interview answers in one
  breath; the practice lab note; and which file serves which moment.
- The provenance carries the sources, the data command, the plants and where each is used, every
  decision that departs from a source, everything invented, each link with its check date, and the
  tool versions the numbers and outputs came from.

## Proof

`python3 scripts/verify.py content/W{ww}/D{d}` runs every gate, and
`python3 scripts/build_companion.py content/W{ww}/D{d} --check` and
`python3 scripts/sync_programme.py --check` follow it. A deck is also rendered through LibreOffice to
PDF and looked at slide by slide, with the Carlito font installed (`fonts-crosextra-carlito`) so
Calibri text measures as it will on a trainer's laptop.

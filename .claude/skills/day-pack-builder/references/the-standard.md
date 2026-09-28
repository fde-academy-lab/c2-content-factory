# The standard a day pack is built to

The model is `content/W01/D1`, Week 1 Monday, rebuilt on 28 September 2026. Before building a
family, open its file in that folder and build the same shape from the day's own row. This page
says what each family carries and names the file that shows it; the mechanics stay in the skills and
scripts it points to. On content the row wins, and on form this page wins over any older reference.

## The frame every artifact sits in

The cohort are trainee engineers in the data and AI team of Kalpa's Global Capability Centre, and
the stakeholders are the team's internal clients (`docs/07_Client_Zero.md`, section 1b). Three beats
recur, and each always looks the same, so a room learns to spot them.

| Beat | In the deck | In a notebook | Elsewhere |
|---|---|---|---|
| The client's ask | The cover quotes the stakeholder, and the first slide sets the scene in their words. | The first cell opens on it. | The exercises that ask for a decision, and the take-home brief, put it back to the learner. |
| Kavya's review | A `**Kavya's review.**` strip closes each chapter. | A quoted review follows the main result. | The companion's decision card closes on it. |
| The interview question | An `**In the interview.**` strip carries the tagged question. | An `### In the interview` section answers it in full. | The day sheet answers it in one breath, and the Saturday paper tests it. |

## Executed files, and discoveries that stay with the learner

Every notebook ships executed and no learner file names a plant. The model reconciles the two with
three devices:

1. **The empty your-turn cell.** The markdown above it gives the lines to type, and the cell ships
   with no source, so no saved output names the record and `nb_check.py` passes over it. Notebook 2,
   cell 18, is the pattern.
2. **Invented numbers for the mechanism.** The mean against the median is shown on five invented
   orders, labelled invented wherever they appear and recorded in the provenance, so the room learns
   the mechanism on numbers nobody has to trust and then finds it in the file on its own.
3. **A trap that does not echo the plant.** The Kahoot's comparison trap uses "3500" where the plant
   is "4500".

## Family by family

### Decks, in `slides/`

Open `C2_W01_D01_half1_STUDENT.md`. The syntax is the docstring of `scripts/build_deck.py`, and the
look is `scripts/deck_layout.py` reading `scripts/brand.py`, the orientation deck's system.

- A half of 110 to 120 minutes runs to about 27 numbered slides: a cover with the client's words on
  its `Quote:` and `Who:` lines, then four chapters, each opened by `## SECTION n:` with an italic
  promise.
- Every body slide has an action title of at most 54 characters, an italic subtitle, and a `notes`
  fence that opens on LIVE or SELF-STUDY with its minutes, says what to say, ask and watch for, and
  ends on the transition to the next slide.
- A question slide is followed by its answer slide, and a slide the trainer may leave as self-study
  is numbered `D` rather than `S`.
- Parallel things go in a `cards` fence, headline numbers in `stats`, and a run of beats in
  `timeline`. At least one Mermaid diagram sits on every four body slides, styled with the `known`,
  `unknown`, `bet` and `bad` classes the model defines.
- The close carries the sentence to the stakeholder, the crux lines the cheat sheet repeats word for
  word, and tomorrow's question, left open.

### Notebooks, in `notebooks/`

Open `C2_W01_D01_02_first_count_STUDENT.ipynb`. The helper is `scripts/c2kit.py`, and
`scripts/nb_make.py` assembles a notebook and executes it cold in its own folder.

- The day carries one teaching notebook per chapter pair, each of 20 to 28 cells with five or six
  rendered diagrams and five or more checks.
- The first cell names the week, the day and the notebook's place ("Notebook 2 of 4"), states the
  promise, quotes Kavya's review, and says in one line what the previous notebook established.
- Each concept runs in the same order: a numbered heading that states the claim, a
  `**Predict before you run.**` question with lettered options, the code, a `**What happened.**`
  cell giving the answer letter with a table, and a check.
- A staged failure runs inside `with kit.expect_error() as err:`, and the markdown under it quotes
  the full Jupyter traceback in a text fence and reads it from the last line up.
- A milestone carries `### In the interview` with the tagged question and its full answer, and a
  `### Depth:` section holds the stretch material.
- The last cell calls `kit.check_summary()`.
- The hands-on twin and its executed solution follow `notebook-builder/references/exercise-notebooks.md`.

### The companion page, in `demos/`

Open `C2_W01_D01_revenue_tree_STUDENT.html`. Its parts are a guided walk, a calculator, four
experiment cards with sequence popups, a workbench that takes the learner's own numbers, a decision
tree and a glossary.

- The page keeps an empty `<style data-c2kit></style>` and `<script data-c2kit></script>`, and
  `python3 scripts/build_companion.py <page>` fills both from `scripts/companion/`, so every diagram
  comes from the `window.C2K` builders and matches the notebook's.
- An experiment that would touch a plant runs on invented records.
- Scrolling stays instant, because `html_sweep.py` clicks buttons that smooth scrolling is still
  moving and times out on them.

### The decision workbook, in `demos/`

Open `C2_W01_D01_build_decision_tool_TRAINER.py`, the script that writes the workbook, so a fix is a
re-run rather than a hand edit.

- A start tab, one tab per taught decision, and an export tab that releases the paste-ready brief
  only when every tab is fixed.
- Yellow input cells (`FFF4C2`), and one planted formula defect per tab that the tab's own check line
  exposes.
- The recalc manifest, `C2_W01_D01_decision_tool_recalc_INTERNAL.md`, names each verdict and each
  flip for `xlsx_recalc.py`.

### Exercises, take-home and Kahoot

Open `exercises/C2_W01_D01_index_STUDENT.md`.

- The unguided sets are layered by what they test, one on the concept, one on the code and one on
  the operating layer, and every stem is written as a question so the distractor audit finds it.
- Each solution file opens on an `Answers:` line and gives, per item, why the key is right and why
  each other letter fails.
- The take-home runs on a second sample from `data/generate_client_zero.py` carrying its own plants,
  which only the day sheet names, and its self-check lists the numbers a learner should reach.
- Each Kahoot item carries a `*Tests: ...*` line naming what it tests, so an item cut for time says
  what was lost.

### Notes, cheat sheet, board work and pre-read

- The study notes run to about 2,800 words, a fifteen-minute read, on the `study-notes-builder`
  spine, and their `| Term |` table is what the cheat sheet prints in its foot.
- The cheat sheet's markdown ships beside the PDF from
  `python3 scripts/build_cheatsheet.py <sheet> --verified "<date>"`, and panel one carries the day's
  picture.
- The board work lists the drawings in the order they go up, as Mermaid, and ends on what is on the
  board when the day ends.
- The pre-read opens on tomorrow's stakeholder message and carries a vocabulary gap table, one thing
  to think about, the check for tonight and the line worth carrying in.

### Day sheet and provenance

Open `trainer/C2_W01_D01_day_sheet_TRAINER.md` and `internal/C2_W01_D01_provenance_INTERNAL.md`.

- The day sheet carries the module and date sync blocks; the five-row envelope of start from, go as
  far as, stop before, comes later and cut first; per half, a chapter flow with minutes and a table
  of slides, the file beside them, what must land and what to cut; the staged failures with exact
  text; checkpoints; the plant table with what to do if nobody finds each; the day's numbers; the
  interview answers in one breath; and which file serves which moment.
- The provenance carries the sources, the data command, the plants and where each is used, every
  decision that departs from a source, everything invented, each link with its check date, and the
  Python version the error texts came from.

## Proof

`python3 scripts/verify.py content/W{ww}/D{d}` runs every gate, and
`python3 scripts/build_companion.py content/W{ww}/D{d} --check` and
`python3 scripts/sync_programme.py --check` follow it. A deck is also rendered through LibreOffice to
PDF and looked at slide by slide, with the Carlito font installed (`fonts-crosextra-carlito`) so
Calibri text measures as it will on a trainer's laptop.

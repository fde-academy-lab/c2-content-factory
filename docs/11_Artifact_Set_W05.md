# The artifact set from Week 5 on

The requester's direction of 28 October 2026, recorded as decision `w5-artifact-set` in
`data/programme/facts.yaml`. Every teaching day from Week 5 on is built in this set; Weeks 0 to 4
keep the shape they were built in and are not touched. Where this file and an older rule
(`the-standard.md`, `docs/06_Day_Pack_Method.md`, the day-pack-builder skill) disagree about
folders, artifacts or review, this file wins for Week 5 on; their teaching rules still apply.

## Who each folder serves

| Folder | Who opens it | When |
|---|---|---|
| `README.md` | everyone, first | the day on one screen: what is where, in the order it is used |
| `1_in_class_training_content/` | the trainer projects it, learners follow along | in session |
| `2_take_home_mandatory/` | every learner, after class | two to three hours, every day |
| `3_study_material_for_students/` | every learner | after class, and before interviews |
| `4_trainer_only/` | the trainer and the TAs | before and during the day |

```
content/W05/D1/
  README.md
  1_in_class_training_content/
    slides/        C2_W05_D01_slides_STUDENT.md + .pptx, and img/ for the PNGs the deck places
    notebooks/     C2_W05_D01_ch01_<slug>_STUDENT.ipynb ... one per concept chapter
                   C2_W05_D01_case01_<slug>_STUDENT.ipynb ... one per case chapter
                   C2_W05_D01_guided_<slug>_STUDENT.ipynb  the in-session guided exercise
    demos/         C2_W05_D01_<slug>_explorer_STUDENT.html  the day's explorable
  2_take_home_mandatory/
                   C2_W05_D01_practice_set_STUDENT.md + .pdf
                   C2_W05_D01_practice_lab_STUDENT.ipynb
  3_study_material_for_students/
                   C2_W05_D01_study_notes_STUDENT.md + .pdf
                   C2_W05_D01_cheat_sheet_STUDENT.md + .pdf
                   C2_W05_D01_interview_bank_STUDENT.md + .pdf
  4_trainer_only/
                   C2_W05_D01_trainer_guide_TRAINER.md
                   C2_W05_D01_practice_lab_solutions_TRAINER.ipynb
                   C2_W05_D01_sources_INTERNAL.md
                   (build helpers such as make_figures.py, named C2_W05_D01_*_INTERNAL.py)
```

**The README** opens on the run table, because that is what someone opening the folder on GitHub
needs first: one row per block of the day (minutes, who acts: trainer, learner or TA, the file to
open, what the screen should show). Then the setup line ("open notebook ch01, run the first cell,
see the row count"), the rule of one notebook open at a time with kernels shut at the break, the
fallback line (the executed outputs on the projector and the explorable opened as a local file),
and the after-class list with the minutes each takes.

The README is the only file at the day root and the only file without the `C2_W..._D.._` stem.
Every other name follows `C2_W{ww}_D{dd}_{topic}_{AUDIENCE}.{ext}`, AUDIENCE being STUDENT,
TRAINER or INTERNAL. The domain's dossier, on the day a domain enters, sits in
`3_study_material_for_students/` as `C2_W05_D02_domain_<name>_STUDENT.md` with its one-page card beside it.

## 1. Training content (in session)

**The deck**: one per day, authored as markdown in the house deck format and built to `.pptx`
with `scripts/build_deck.py`. It is a picture book with a voice-over.
- A slide body carries at most about 25 words of prose; the rest is a diagram, a chart, a table
  of real numbers, a screenshot of our own output, or code of a few lines.
- Every concept chapter has at least one picture, drawn from tiny numbers before any formula.
- Order: title; the roadmap (the programme's twenty weeks with this week lit and what comes
  next); today's question (the case ticket, one slide); the topics slide and concept map naming
  every row subtopic verbatim with its chapter; the concept chapters in the row's order; the
  case chapters; the interview corner (the row's anchors, each with the shape of a good answer);
  the quiz (the row's Kahoot plan, five questions and the return question); the close (what you
  can now do, tonight's take-home, tomorrow).
- A chapter opener reads `## SECTION n: <relatable title>: <short question>?`, and its italic
  line beneath carries the row's subtopic verbatim and the names learners would search for, for
  example `*Train, validation, test; the seed; the baseline · also searched as: train test
  split, data leakage, baseline model*`.
- Speaker notes give the minutes, the one line to land, the click, and the question to ask.
- No logo of any institution or company appears on any slide or page, and no line names the institute or the programme; a slide header carries only the week, the day and the day's topic (the requester, 28 October 2026).

**Notebooks**: one short notebook per concept chapter (8 to 15 cells) and one per case chapter,
each case notebook building on the one before, plus the guided in-session notebook (the row's
GUIDED exercise, with TODO cells the room fills and the answer in a final cell).
- Data is public and downloaded in code, never generated: the loader cell below, cached so a
  second run reads the local copy. A tiny teaching table may be typed in a cell, labelled
  invented.
- The first cell names the chapter, what the learner will be able to do, and the terms to search.
- Each notebook ships executed, runs cold top to bottom in a Codespace, draws at least one chart,
  and carries at least two checks that print PASS.

```python
# Load the day's public dataset once; later runs read the cached copy.
import io, zipfile, pathlib, urllib.request
import pandas as pd
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)

def fetch(url, name):
    path = CACHE / name
    if not path.exists():
        path.write_bytes(urllib.request.urlopen(url, timeout=60).read())
    return path
```

**The explorable**: one self-contained HTML file per day in `demos/`, the day's visual companion
from zero to the interview, working offline on a projector and a phone with no library and no
network. It runs one skeleton of in-page pages, reached from a top nav and a progress rail: the
story (the day's business situation animated on the real case), the concept map (today's
subtopics, what they rest on and what they feed, the day's path lit in order), one how-it-works
page per row subtopic (the mechanism as a motion graphic with play, step and scrub), the case on
real data (the case steps, the trap shown exactly, the check and the fix), in the field (verified
company scenes, then what each of the six seats does with the idea), the interview room (the
learner picks the clarifying question, orders the whiteboard steps and commits the answer before
the model answer, its two follow-ups and the room's usual wrong answers appear) and check
yourself. On every page the learner commits a prediction, moves one variable and watches a
picture and a number change together, and the rule is named last with the condition that flips
it; a scene that cannot name the row subtopic it serves and the number it changes is cut.
Concept animations run on invented numbers labelled invented; the case and field pages draw real
numbers, exported from the public data by `4_trainer_only/C2_W05_D0n_explorer_data_INTERNAL.py`.
The look and the components live once in `scripts/companion/w5kit.css` and `w5kit.js`, which
`scripts/build_companion.py` inlines, so a day page never carries a hand copy. Every control
writes a readout into the page before it animates, nothing waits behind a locked control, and a
reduced-motion setting shows each animation's end state. It passes `scripts/html_sweep.py`, which
walks every page of it, and the orchestrating session reviews a screenshot of every page at
projector and phone width before it merges. The README run table and the trainer guide name the
page each chapter opens. There is no size cap; the skeleton is the limit.

## 2. Take-home, mandatory (two to three hours)

**The practice set**: one document, markdown that GitHub renders with its diagrams, printed to
PDF with `scripts/build_doc.py`. In this order:
1. How to use it: the time plan and the self-check flow as a diagram.
2. Recap: the theory on one page, with its pictures and rules.
3. Part A, ten practice problems, harder in structure than the Saturday paper: each opens on a
   scenario at a named real company or at Kalpa, reads an exhibit (a diagram, a chart, a table,
   a code output), asks two to four connected questions, and names the seat it is answered from
   (business owner, product manager, solution architect, senior ML engineer, implementation
   engineer, QA). Mix: computation with a judgement, diagnosis of an exhibit, a design or
   trade-off decision, and an interview-style case prompt. Every problem carries an interview
   question an employer has asked or would ask, rewritten around its exhibit.
4. Part B, fifteen to twenty self-check MCQs: one correct, several correct, true or false with
   the reason, assertion and reason, match. No key is the longest option, keys spread across the
   letters, and every distractor is a misconception a learner holds.
5. Part C, after a clear stop line: the answer key, a model solution for every problem (the
   working, the reasoning an interviewer listens for, the common wrong answer), and one line on
   every MCQ option.
6. The self-check guide: score bands and what to revisit, as a diagram.
7. Three to five links to study, each verified with its date.
8. Tomorrow's ten-minute pre-read: five terms, one line each, one picture.

The two to three hours are the practice set alone. The lab below runs in the TA-led practice lab
and is extra practice afterwards; it is never counted in the take-home's hours.

**The practice lab**: one notebook for the TA-led lab and for self-study. It shows the business
before it asks for code: a situation at a real company and its Kalpa twin, the six seats each
asking their question (the table in the week's plan), a scaffolded build with TODO cells and
checks, one assignment on the day's topic, one integration step that reuses an earlier week
(pandas, SQL or statistics), a QA step that tries to break the result, and a five-line write-up
in the claim, evidence, caveat, action shape. Its solutions sit in `4_trainer_only/`.

## 3. Study material (share with students)

- **Study notes**: six to ten printed pages, visual first. Per chapter: the picture, the idea in
  three lines, the worked example, the trap, the interview line. Caselets from real companies with
  dated sources, the six seats applied to the day's case, and where the day sits on the roadmap.
- **Cheat sheet**: one to two pages. The glossary of the day's hard terms (term, plain meaning,
  rule or formula, trap); everything so far since Week 1 in one line each, so it grows across the
  programme; the ML process map with today lit; when-to-use rules; two or three verified tidbits
  from engineering blogs or the news that make an idea stick.
- **Interview question bank**: 25 to 30 questions, tagged [S], [F], [D] as the rows tag them:
  screening staples, technical depth, ML case and scenario, techno-functional and client-facing,
  and behavioural with a technical core. Each carries a model answer (the 30-second version, then
  the depth), what the interviewer listens for, and the common wrong answer.

## 4. Trainer

**The trainer guide** is read in two minutes and used all day: bullets, tables and diagrams, no
paragraphs of story. Its first screen is four tables:
1. The story in two lines (the real case and Kalpa's decision).
2. The run table: block, minutes, slide range, notebook or explorable to open, what must land, what
   to cut if the room is late.
3. Taught before, teach today, do not teach today (the row's STOP BEFORE and COMES LATER).
4. The interview anchors as questions, each with the minute it is asked aloud.

Below the fold:
- How to teach each chapter: the picture to draw, the prediction to ask for before showing
  anything, the misconception to stage, the wrong number shown exactly and its fix, the click in
  the notebook or the explorable, the interview line.
- The day's spotlight lens (the week's plan gives one seat per day) and how to ask it in class.
- The quiz with its keys, ready to type into Kahoot.
- The practice-lab run sheet for the TAs: ten minutes re-running the day's last case notebook on
  the projector, then the lab; per TODO the expected number, the three commonest wrong answers,
  the cut order and the parts never cut; the lab's length stated.
- The fallbacks: downloads or kernels failing for some of the room (pair them, project the
  executed outputs), and what fills the 120 minutes if the tentative faculty block does not run.
- At the end, the sync blocks `<!-- sync:module:W05/D1 -->` and `<!-- sync:faculty-day:W05/D1 -->`
  and the ME1 line where it applies.

**The sources file** (INTERNAL): every dataset with its URL, licence and date checked; every
reference and case fact with its source and date; every image with its licence and attribution.

## Rules kept from earlier weeks

The curriculum row is the contract (its subtopics verbatim and in order, its interview angle, its
STOP BEFORE); concept chapters come before the case; durations only, never clock times; role
labels only in STUDENT files, Kalpa's people the exception; Rs, never the glyph; no em-dashes and
none of CLAUDE.md's banned words; every fact and URL verified and dated; nothing the room is
meant to find is named in a STUDENT file before the session finds it; notebooks executed; MCQ
keys never the longest option.

## Rules dropped from Week 5 on

The exercises, kahoot, preread, extras, whiteboards, data, takehome, cheatsheets, study-notes,
trainer and internal folders (their content lives in the four folders); the INTERNAL coverage
matrix and the three cold-read agents (the orchestrating session reads each pack against its row
instead); the single explorer that grows across a week (one explorable per day); synthetic data
generated by a seeded script (public data, downloaded in code); logos; the Excel forms unless a
day's decision needs a workbook.

## Tools and checks

- Formulas in markdown are written as plain text or code spans (for example
  `threshold = 40 / (40 + 1,200) = 0.032`), never LaTeX, so GitHub and the PDF print the same thing.
- `scripts/build_deck.py` (deck), `scripts/build_doc.py` (markdown with mermaid to PDF),
  `scripts/html_sweep.py` (explorable), `scripts/nb_check.py` (notebooks).
- `python3 scripts/verify.py content/W05/D1` checks the Week 5 layout and names, the style sweep,
  the executed notebooks in `1_in_class_training_content/notebooks/`, the explorable and the deck. A pack
  that fails it is not done; the orchestrating session's one read against the row is the review.

## Models and effort

Planning and critique run on Fable at extra effort (xhigh); each day is built in its own cloud
session on Opus at extra effort; small tasks may run on Fable at medium or high. Max effort is not
used unless the requester asks for it.

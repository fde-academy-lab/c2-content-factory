# Week 5 explorers: the rules every explorer session follows

INTERNAL. Read by the kit session and by each day's explorer session. The requester approved this
rebuild on 29 October 2026 (decision `w5-explorer-companion` in `data/programme/facts.yaml`).

## Why the pages are being rebuilt

The first Week 5 explorables were built to a contract that capped them at about 400 lines, one
question and one or two controls, with three clicks as the whole run order. The requester read
them and found them undercooked: Wednesday's page was one screen with three clicks. Each day's page
is now the day's visual companion from zero to the interview. In the requester's words, in
substance:

- It starts from zero. It opens on the map of the day's concepts and how they interlink, told as
  a storyline that is visualised, never as words drawn in boxes.
- Its visualizers, animations and motion graphics show how each concept works inside, so a
  learner builds the intuition. The tone is intuitive without being childlike.
- It shows interview situations being solved step by step, with the steps drawn, instead of only
  asking the question.
- It carries real company situations where the concept mattered, from the angles of engineering,
  product and business teams.
- It is tight and technically sound, and it climbs structurally from 0 to 100. Several pages,
  icons, buttons and animations are all welcome.

## Read first

1. `CLAUDE.md`, the section "From Week 5 on", and the writing rules under "Hard rules".
2. `docs/11_Artifact_Set_W05.md`, the paragraph "The explorable": the contract.
3. `docs/detailing/W05_research/W05_explorables.md`, section 1. Its ten principles stand, with the
   scope changes its first paragraph records.
4. The skills `companion-builder` (its Rules section binds), `design-taste-frontend` and `dataviz`.
   Name what you took from each in your report.
5. `scripts/companion/W5KIT.md`, once the kit session has written it. Day sessions build only with
   the kit.

## The skeleton every day page runs

| Route | Page | What the learner does there |
|---|---|---|
| `#story` | The story | Plays the day's business situation, animated on the real case, and commits a prediction of the headline number before it appears. Where today sits on the week's growing timeline is shown here. |
| `#map` | The map | Opens the concept map: today's row subtopics, the earlier ideas they rest on and the later ones they feed, with every edge labelled by its relation. The day's path lights in order, and each node opens its page. |
| `#p1` to `#pn` | How it works, one page per row subtopic | Meets the misconception and commits a prediction. Plays the mechanism as a motion graphic on tiny invented numbers labelled invented, with play, step and scrub. Moves one variable in the sandbox. Reads the rule named last, with the condition that flips it. |
| `#case` | The case on real data | Steps through the day's case chapters on the bank's numbers. The trap is shown exactly, then the check that catches it and the fix. |
| `#field` | In the field | Works three or four verified company scenes, each with one control. Then reads the six seats: what the business owner, the product manager, the solution architect, the senior ML engineer, the implementation engineer and QA each do with the idea. |
| `#interview` | Interview room | Works four to six situations, mixing technical, techno-functional, scenario and client-facing. In each, the learner picks the clarifying question, orders the whiteboard steps and commits the answer. Only then do the model answer (the 30-second version), the drawing building step by step, the interviewer's two follow-ups and this room's usual wrong answers (crossed out, each with why) appear. |
| `#check` | Check yourself | Answers six to eight visual checks (predict a number, pick, order, sort into bins), sees the map again with today lit, and reads tomorrow's question. |

Each how-it-works page carries the row's subtopic verbatim as its kicker and the deck chapter's
title and short question as its heading, so the page, the slide and the notebook are one idea
under one name.

## The page rule

- On every page the learner commits a prediction, moves one variable, and watches a picture and a
  number change together. The rule is named last, with the condition that flips it.
- A scene that cannot name the row subtopic it serves and the number it changes is cut. The
  skeleton is the limit, and there is no line cap.
- A motion graphic answers a question asked first. Nothing moves on arrival, and every page
  teaches from its still state.

## The engineering rules

- The page is one self-contained file. It works offline, from disk, on a projector and on a phone
  360 pixels wide.
- No external library, CDN, web font, network call or browser storage is allowed. Icons are inline
  SVG drawn for the kit, dot clouds are drawn on canvas, and the font stack is the system's.
- The kit is inlined by `python3 scripts/build_companion.py <page>`, along with the day's data
  block. A day page never carries a hand copy of kit code, and a gap in the kit goes in your
  report, never into a patch of the kit.
- Every control writes a readout into the page's DOM the moment it is used, before any animation
  runs, so `scripts/html_sweep.py` sees it act.
- No control is disabled until a prediction is made. A reveal used without a prediction says so
  and still reveals.
- Nothing on the page states a prediction's answer before the learner commits or reveals: a
  readout or a numbers card that would give it away shows a question mark until then.
- With reduced motion set, every animation shows its end state.
- Scrolling stays instant.
- Arrow keys step the active animation or page, and a presenter mode enlarges the type.
- Real numbers come only from the public data, through the day's
  `4_trainer_only/C2_W05_D0n_explorer_data_INTERNAL.py`. It uses the week's cached loader, reruns
  the week's pipeline as the day's notebooks do, and writes the JSON that `build_companion.py`
  inlines. Every number on the case and field pages traces to a notebook output or to
  `docs/detailing/W05_research/W05_cases.md`.
- Every company fact comes from a case that `W05_cases.md` marks verified, with its source and date
  on the page. Anything in its "not verified" list stays off the page.
- The page passes `python3 scripts/html_sweep.py` on its folder, which walks every route.
- Screenshot every route with `python3 scripts/explorer_shots.py <page> <scratch dir>` at
  projector and phone width. Look at every picture yourself and fix any overflow, clipping, overlap
  or unreadable label before you push. Screenshots are never committed.

## The writing rules

- Visible text is full, connected sentences.
- No em-dash or en-dash appears anywhere, including code comments, HTML and SVG text.
- None of the CLAUDE.md banned words appear.
- Money is written "Rs", never the glyph.
- Durations only, never clock times.
- Role labels only, except Kalpa's fictional people (Meera, Anand, Kavya, Rohan).
- Every URL carries its checked date on the same line.
- Nothing the room must find in class is named on a page used before that step. The story page
  asks; the case page answers.

## Branches, files and the finish

- **File and links.** Each day keeps its current file name in
  `1_in_class_training_content/demos/`, so the README and the trainer guide keep their links. The
  day session also edits the README's run table and the trainer guide, so each chapter names the
  page (`#p3` and so on) it opens.
- **Branch and pull requests.** Work on the branch your launch prompt names, cut from
  `origin/main`, and push it with `git push -u origin <branch>`. Commit in small commits whose
  messages say what changed. Never open, merge or close a pull request.
- **Gate.** `python3 scripts/verify.py content/W05/D0n` passes, and its last lines go in your report.
- **Report.** Under 400 words:
  - the routes and what each one does;
  - the numbers the page draws and where each comes from;
  - what you cut and why;
  - any gap in the kit;
  - the skills used.

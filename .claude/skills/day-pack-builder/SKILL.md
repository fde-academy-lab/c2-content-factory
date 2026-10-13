---
name: day-pack-builder
description: Build the complete artifact pack for one full day of a cohort training programme, anchored to IITGN Cohort 2. Produces the trainer deck (or the half-one and half-two pair), rich demo notebooks, a toggle-driven activity, guided and unguided exercises with solutions, a shortcut-resistant take-home with a self-check spine, the Kahoot pack, study notes, cheat sheets and the pre-read. Use this skill whenever the request names a day pack, session pack, day build, "Week N Day D", "build Monday's session", the Day 1 introduction pack, or any deck-plus-notebook-plus-exercise set for a training day, even if only one artifact is named, because the pack's parts must stay consistent with each other. Runs from the locked curriculum row and refuses to invent a missing one.
---

# Day Pack Builder

One training day ships as one pack: everything a rotating trainer needs to deliver it and everything a learner needs to relive it. This skill turns one row of the detailed curriculum into that pack, in a fixed order, with approval gates so a wrong direction costs a screenful rather than a finished build.

## Inputs, and when to refuse

Read these before generating anything:

1. The day's row in `docs/curriculum/W{n}_*.md`, **all fifteen columns, in the order the row puts them**.
   The row reads business problem first and technique third, and the pack is built in that same order:
   the business scenario of the day, the thinking trained before any tool, the day focus, the trainer
   agenda, the learner outcome, the subtopics, the trainer notes, the client-zero data (TRAINER ONLY),
   the in-session exercises, the after-class tasks, the interview angle, the trainer resources, the
   student references, the Kahoot quiz plan. Weeks 2, 4, 5, 7, 8, 10 and 11 add a sixteenth, violet
   column: the IITGN faculty session, tentative.
   The Subtopics column is the day's chapter list: copy its bullets verbatim and in order, run
   `python3 scripts/coverage_check.py content/W{ww}/D{d} --matrix` to print the coverage matrix's
   skeleton from them, and write that matrix to `internal/` before any other file, in the shape
   `references/coverage-matrix.md` sets.
2. The day's line in `docs/programme/calendar.md`: its date, its folder slot, the module it posts to and
   any faculty block. Dates come from here and never from memory; the calendar moved by a week on
   21 September 2026 and can move again.
3. `docs/curriculum/Structure.md`: week types, the Saturday recap shape, assessment status, the
   faculty plan's rules, the open decisions.
4. `docs/07_Client_Zero.md`, which is LOCKED at v2.2, with its v2.3 note: the company, the named
   stakeholders, the three threads, the business-question ladder, the entity model, and the dataset
   version the row names in its client-zero column together with what is planted in it.
5. `data/programme/facts.yaml` for the status of any movable fact the pack touches, and
   `docs/06_Day_Pack_Method.md` and `docs/02_Content_Doctrine.md` for the reasons behind the procedure.

Refuse, naming the gap, when any of these hold: the day's row does not exist; the business scenario
column is empty, because a day built without it opens on a technique and that is the failure the
September 2026 review named; the dataset version the row names is described neither in the locked
client zero file nor, marked proposed for v2.3, in the row itself; a reference link on the row carries
no verified date. A pack built on a v2.3 dataset says "proposed for client zero v2.3" in its TRAINER
and INTERNAL files, because the lock may still change it. A plausible day generated around a gap
is the failure this gate exists to stop. Say what is missing and stop.

## The method: the topics first, then the case, and inside every chapter the problem before the code

From Week 4 on (decision `concept-first-case-second`), the day opens on its topic and a concept map
that names every subtopic of the row, in the row's order, then shows the case ticket as the
destination. The concept block teaches each subtopic from zero in its own named chapter on a simple,
complete, relatable educational example with invented numbers, paired with a short notebook of the
same name. The case chapters then apply those ideas to an engineering case at a company the learners
use, each chapter naming the subtopics it applies, and the lab runs the same method on Kalpa. Inside
every chapter the order is the same: the problem on the example or the data, the thinking drawn before
any tool, and the technique built because the question needs it.

In the pack that means: the cover names the topic, slide two is the week map, slide three the topics
slide, slide four the concept map, slide five the ticket; each concept chapter's opener carries its subtopic as the row words it and
its notebook carries the same name; each case chapter's opener names the subtopics it applies; the
exercises carry at least one item per subtopic and the Kahoot at least one; the trainer's day sheet
prints the coverage matrix as its topic table; and the close is the sentence the learner would send
the client, with the topics it used named beside it. Weeks 1 to 3 opened on a stakeholder's words
(Meera Raghavan asks what "sales" is made of before she signs a marketing budget, the room draws the
revenue tree, and only then does Python arrive) and keep that shape until they are rebuilt.

**What is planted in the data is never named to a learner.** The client-zero column is TRAINER ONLY.
The room finds the bulk order by sorting and the duplicates by reconciling. A slide that announces the
plant has spent the lesson. The one exception is the week's Saturday recap paper, which may name a
plant the room has already found in class.

**The interview angle is an output.** The row carries the questions this day equips a learner to
answer, tagged `[S]`, `[F]`, `[SV]` or `[D]`. Questions go into the pack; answers are written here at
the detailing phase and never copied into the curriculum row.

## Movable facts: the module line and the faculty block

Some facts in a pack are not the pack's to fix: the module the day posts to, and on a faculty day the
IITGN block that follows the applied core. The trainer day sheet carries both as sync blocks, so a
confirmation, a moved session or a re-dated calendar reaches the pack with one
`python3 scripts/sync_programme.py` and no hand edit:

```
Module: <!-- sync:module:W02/D1 --><!-- /sync:module:W02/D1 -->

<!-- sync:faculty-day:W02/D1 -->
<!-- /sync:faculty-day:W02/D1 -->
```

Write the empty blocks and run the sync; it fills them. The row's stop-before line is where the
faculty member starts, so the deck, the notebook and the exercises stop there too, and the trainer
sheet says what the block will pick up. A STUDENT file mentions the block only with its status beside
it (tentative, until IIT Gandhinagar confirms), and never names a faculty member. The status words and
what each allows are in `data/programme/facts.yaml`.

## Mental model first, spiral always

Every topic opens by forming the mental model, then walks the whole pipeline shallow, then deepens on revisit. The canonical worked example, kept because the team teaches from it:

Explaining an LLM. Open on an experience everyone has had (type a prompt, get a response, the same shape as hitting a URL and getting a page). Walk the pipeline end to end at one shallow level: the model cannot read the sentence whole, so it breaks it into tokens (what a token is, in one intuitive beat, and that it varies by language); each token becomes an embedding (why numbers at all); position is injected (the same word means different things in different places); meaning lives as nearness in vector space (start with 2D coordinates the room can picture, then say it grows to thousands of dimensions; GPT-3's embedding width was 12,288, and note the correction if anyone says parameters, which run to billions); then inference emits the next token, one at a time, shaped by temperature and the top-k and top-p dials. One connected story, no stop too deep, and every stop gets its own deeper day later. That is the spiral.

Binding rules while building:

- At most four new ideas per two hours of teaching, counted as decision sentences, so a 180-minute block holds six and the day twelve; depth comes from climbing each idea through harder cases, never from adding ideas past the cap. If the row's ideas exceed it, the row is wrong and the build stops.
- Application before theory: the working thing and its output first, the name last.
- Every chapter stages a trap: a plausible wrong number or output, shown exactly, with the decision it would have misled, the check that catches it and the fix. A syntax or runtime error is met when it happens and gets two minutes; it never takes a trap slot.
- Cognitive load is the design constraint: think trainer, psychologist and storyteller at once, and cut breadth before cutting the worked example.
- Durations only, never clock times; role labels only, never trainer names, in anything a student sees.

## The gates

1. **Envelope and continuity.** From the row: the business scenario in one line, what the room already knows, what today must not repeat, what comes later, and which thread of the three (Growth, Trust, Cost and risk) this day advances. One short block, stated to the requester.
2. **The spine, for approval.** Where `docs/detailing/` holds an approved spine for the week, it is this gate for every day it covers: state the envelope, then build from it without stopping. Otherwise, one screen: the row's subtopics verbatim, each with its concept chapter title, its educational example, its minutes and its notebook name; the scenario and the thinking it trains; the domain beat (the story on a domain's first day, the metric at stake after it); the case chapters with each one's question, the subtopics it applies, its options, sizing and second route; the afternoon's cases; the day's minutes against its envelope; the day's mental-model arc in one sentence; the traps with their exact wrong numbers; the activity choice with its toggle; the take-home shape; and the interview questions the day equips. Stop and wait. Nothing downstream is built before the spine is approved.
3. **Build passes**, one artifact family per pass, in this order: the coverage matrix (INTERNAL, from the row's subtopics); deck(s); notebooks; activity; exercises plus solutions; take-home plus self-check spine; Kahoot pack; study notes, cheat sheet and pre-read; the matrix filled in as each family lands. Each pass is a separate generation because mixing them flattens all of them. Then the review in `references/the-standard.md`: the domain pass and the problem-first pass by the builder, then the three cold reads (the fresh graduate, the hiring interviewer, the trainer with the row open) by fresh reviewer agents, each logged in the sources list, and one fix pass.
4. **Verification.** Run the checklist at the end of this file and report results, including what failed and was fixed.
5. **Ship.** Folders and file names per the naming rule below, audience tags mandatory, files presented together.

## The artifact set

The full manifest with per-artifact specifications lives in `references/artifact-manifest.md`. Read it before pass 1 on any new day. `references/the-standard.md` sets the bar, the 360-minute day, the chapter and the volume each family ships, and names `content/W01/D1` as the model for form; read it before each build pass. On a domain's first day, `references/domain-dossier.md` sets the dossier, its card and the story that opens the day. The short form:

| Artifact | Audience | Count per day |
|---|---|---|
| Deck | STUDENT-visible, trainer-driven | 2: the morning deck (half one) and the afternoon deck (half two) |
| Chapter notebooks | STUDENT | One per chapter: a concept notebook of 8 to 18 cells per row subtopic, named by the subtopic, and a case notebook per case chapter, each building on the one before, plus the lab notebook |
| Coverage matrix | INTERNAL | 1, written first and filled as the families land, in the shape `references/coverage-matrix.md` sets; `scripts/coverage_check.py` reads it |
| Domain dossier, card and story | STUDENT, and TRAINER for the story | On a domain's first day only |
| Activity | STUDENT | 0 or 1 |
| Guided + unguided exercises | STUDENT | few, think-heavy |
| Solutions | STUDENT, timed release | one per exercise |
| Take-home | STUDENT | 1, shortcut-resistant |
| Kahoot pack | STUDENT | 1, ungraded, incl. the return question |
| Trainer notes + day sheet | TRAINER | 1 |
| Study notes | STUDENT, after delivery | 1, transcript-revisable |
| Cheat sheet | STUDENT | 0, 1 or more |
| Pre-read + setup for tomorrow | STUDENT, ships tonight | 1 |
| Practice lab set | STUDENT, with a TA note | 1, for the lab after the second block |
| Tiered extras (stretch, recovery) | STUDENT | 1 pair, weekly build allowed |

Saturday recap papers are weekly artifacts taken from the week's paper in the tracker's item bank (`docs/curriculum/Saturday_papers.md`): the STUDENT paper prints the items in parts with each item's format and level, and the key, tags, roles and anchors go to TRAINER files. Build weeks swap this manifest for the build-week pack, and Week 0 days add the diagnostic papers and keys; all three variations are specified in the manifest reference.

## The introduction pack, now in Week 0

Orientation moved to Week 0 Monday on the 21 September calendar. The Programme Head's welcome carries the journey map across twenty weeks, the kinds of week, how a teaching day, a Saturday and a build week run, and the three seats; setup and the self-rating follow. That day ships the introduction pack instead of a standard pack, and it carries no Kalpa material: the tracker keeps client zero for Week 1 Monday, which opens straight on Meera Raghavan's question, so the Week 0 pack stops before it. Read `references/day1-intro-pack.md` before building it; its running order follows the student Week 0 sheet (`docs/journey/Week_0.md`) and its content follows the tracker's Week 0 row.

## Verification checklist

1. The deck opens on the day's topic, the week map, the topics slide and the concept map naming every
   row subtopic verbatim in the row's order with the chapter that teaches it, and the case ticket as
   the destination; every concept chapter's
   `## SECTION` title and its notebook's file name and first heading carry the subtopic as the row
   words it; every case chapter's opener and its notebook's first cell name the subtopics it applies;
   `python3 scripts/coverage_check.py content/W{ww}/D{d}` passes. A pack whose chapters cannot be
   mapped to the row's subtopics fails here.
2. The thinking from column 4 appears as a drawing the room makes before any tool is opened.
3. No student-facing file names anything planted in the dataset. Grep the pack for the plant words from
   the row's client-zero column; every hit must be in a TRAINER or INTERNAL file.
4. The interview questions from column 12 appear in the pack as questions, with their tags, and the
   answers written here are not copied back into the curriculum row.
5. Idea count per block within the cap, counted as decision sentences.
6. Every chapter's trap shows the exact wrong number or output and the decision it would have misled, and the demonstration reproduces it; no trap is a syntax error.
7. Demo notebooks run cold in a fresh Codespace, top to bottom.
8. Deck chapters and notebooks pair one to one by number and title, and the exercises follow the same order.
9. Every link was verified on the day it entered an artifact and carries that date; unverified slots say "to be found".
10. The take-home fails the shortcut test: pasting it into a chat assistant does not produce the deliverable (see the manifest for the resistance patterns).
11. No trainer names, marks, weights or clock times in any STUDENT artifact; Kalpa's fictional stakeholders are named on purpose and are not covered by that rule. Rs, never the currency glyph; no em-dashes; the banned-word scan passes.
12. Distractor audit on every quiz: no key is the longest option, key positions spread.
13. Audience tag present in every file name, and every file inside the subfolder its type belongs in.
14. The study notes and cheat sheet carry the same crux lines the deck closes on.
15. The trainer day sheet names its module and, on a faculty day, carries the IITGN block, both as sync
    blocks, and `python3 scripts/sync_programme.py --check` passes.
16. No STUDENT file states a proposed or open fact, and a tentative one carries the word tentative.
17. Every chapter lays out its options with a sizing and the best-fit call before its code, names the fact that would change the call, and closes on a second route; at least a third of the day's exercise items are design items.
18. Every chapter names the metric at stake, who asks for it, what a wrong number costs and a real company that faces the same question, with each real fact sourced and dated; on a domain's first day the dossier, card and story ship.
19. The sources list logs the builder's two passes and the three cold reads (the fresh graduate, the hiring interviewer, the trainer with the row open), each by a fresh reviewer, and what each changed; a "not found" from the trainer's read is resolved before the pack is called done.
20. The verify run's output, the coverage gate's lines among it, is in the reply before the pack is called done.

## File naming

```
content/W{ww}/D{d}/{folder}/C2_W{ww}_D{dd}_{topic}_{AUDIENCE}.{ext}
content/W{ww}/SAT/{folder}/C2_W{ww}_SAT_{topic}_{AUDIENCE}.{ext}
```

Read `content/README.md` before pass 1: it names the subfolder each artifact belongs in, the different shapes a build day and a Saturday take, and the rule that no file sits loose at a day folder's root. The topic half of the name carries only what the folder and the extension do not already say.

Examples: `slides/C2_W04_D03_half1_STUDENT.pptx`, `notebooks/C2_W04_D03_01_support_confidence_and_lift_STUDENT.ipynb` (a concept notebook, named by its subtopic), `notebooks/C2_W04_D03_07_pairs_table_STUDENT.ipynb` (a case notebook, named by its step), `internal/C2_W04_D03_coverage_INTERNAL.md`, `takehome/C2_W04_D03_brief_STUDENT.md`, `trainer/C2_W04_D03_day_sheet_TRAINER.md`.

## The generation prompt

A paste-ready prompt that drives this skill from a fresh chat lives in `references/generation-prompt.md`. It parameterises week, day and date, enforces the spine gate, and lists the binding rules so a new chat cannot drift from them.

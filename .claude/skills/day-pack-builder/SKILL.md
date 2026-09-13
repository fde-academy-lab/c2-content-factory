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
   student references, the Kahoot quiz plan.
2. `docs/curriculum/Structure.md`: week types, the Saturday recap shape, assessment status, the
   confirmed calendar.
3. `docs/07_Client_Zero.md`, which is LOCKED at v2.2: the company, the named stakeholders, the three
   threads, the business-question ladder, the entity model, and the dataset version the row names in its
   client-zero column together with what is planted in it.
4. `docs/06_Day_Pack_Method.md` and `docs/02_Content_Doctrine.md` for the reasons behind the procedure.

Refuse, naming the gap, when any of these hold: the day's row does not exist; the business scenario
column is empty, because a day built without it opens on a technique and that is the failure the
September 2026 review named; the dataset version the row names is not described in the locked client
zero file; a reference link on the row carries no verified date. A plausible day generated around a gap
is the failure this gate exists to stop. Say what is missing and stop.

## The method: the business problem first, then the thinking, then the technique

The day opens on a situation in a stakeholder's words and the questions they are asking. The second
move is the thinking an analyst uses to break that question down, drawn before any tool is opened. The
technique arrives third, because it exists to answer the question.

In the pack that means: slide one is the scenario, the first drawing is the thinking, the notebook's
first markdown cell is the same scenario, the exercises ask the stakeholder's question back, and the
close is the sentence the learner would actually send. The canonical Week 1 case: Meera Raghavan asks
what "sales" is made of before she signs a marketing budget, the room draws the revenue tree, and only
then does Python arrive as the calculator.

**What is planted in the data is never named to a learner.** The client-zero column is TRAINER ONLY.
The room finds the bulk order by sorting and the duplicates by reconciling. A slide that announces the
plant has spent the lesson.

**The interview angle is an output.** The row carries the questions this day equips a learner to
answer, tagged `[S]`, `[F]`, `[SV]` or `[D]`. Questions go into the pack; answers are written here at
the detailing phase and never copied into the curriculum row.

## Mental model first, spiral always

Every topic opens by forming the mental model, then walks the whole pipeline shallow, then deepens on revisit. The canonical worked example, kept because the team teaches from it:

Explaining an LLM. Open on an experience everyone has had (type a prompt, get a response, the same shape as hitting a URL and getting a page). Walk the pipeline end to end at one shallow level: the model cannot read the sentence whole, so it breaks it into tokens (what a token is, in one intuitive beat, and that it varies by language); each token becomes an embedding (why numbers at all); position is injected (the same word means different things in different places); meaning lives as nearness in vector space (start with 2D coordinates the room can picture, then say it grows to thousands of dimensions; GPT-3's embedding width was 12,288, and note the correction if anyone says parameters, which run to billions); then inference emits the next token, one at a time, shaped by temperature and the top-k and top-p dials. One connected story, no stop too deep, and every stop gets its own deeper day later. That is the spiral.

Binding rules while building:

- At most four new ideas per two-hour block, counted as decision sentences. A day is one block-pair; if the row's ideas exceed the cap, the row is wrong and the build stops.
- Application before theory: the working thing and its output first, the name last.
- One deliberate failure per block, with the exact error text or the exact wrong output.
- Cognitive load is the design constraint: think trainer, psychologist and storyteller at once, and cut breadth before cutting the worked example.
- Durations only, never clock times; role labels only, never trainer names, in anything a student sees.

## The gates

1. **Envelope and continuity.** From the row: the business scenario in one line, what the room already knows, what today must not repeat, what comes later, and which thread of the three (Growth, Trust, Cost and risk) this day advances. One short block, stated to the requester.
2. **The spine, for approval.** One screen: the scenario and the thinking it trains, the deck decision (one deck, or half one and half two when the day carries two arcs), section list per artifact, the day's mental-model arc in one sentence, the deliberate failures with their exact error text, the activity choice with its toggle, the take-home shape, and the interview questions the day equips. Stop and wait. Nothing downstream is built before the spine is approved.
3. **Build passes**, one artifact family per pass, in this order: deck(s); notebooks; activity; exercises plus solutions; take-home plus self-check spine; Kahoot pack; study notes, cheat sheet and pre-read. Each pass is a separate generation because mixing them flattens all of them.
4. **Verification.** Run the checklist at the end of this file and report results, including what failed and was fixed.
5. **Ship.** Folders and file names per the naming rule below, audience tags mandatory, files presented together.

## The artifact set

The full manifest with per-artifact specifications lives in `references/artifact-manifest.md`. Read it before pass 1 on any new day. The short form:

| Artifact | Audience | Count per day |
|---|---|---|
| Deck | STUDENT-visible, trainer-driven | 1, or 2 as half one and half two |
| Demo notebooks | STUDENT | 1 or more, rich, progressive |
| Activity | STUDENT | 0 or 1 |
| Guided + unguided exercises | STUDENT | few, think-heavy |
| Solutions | STUDENT, timed release | one per exercise |
| Take-home | STUDENT | 1, shortcut-resistant |
| Kahoot pack | STUDENT | 1, ungraded, incl. the return question |
| Trainer notes + day sheet | TRAINER | 1 |
| Study notes | STUDENT, after delivery | 1, transcript-revisable |
| Cheat sheet | STUDENT | 0, 1 or more |
| Pre-read + setup for tomorrow | STUDENT, ships tonight | 1 |
| Tiered extras (stretch, recovery) | STUDENT | 1 pair, weekly build allowed |

Saturday recap papers are weekly artifacts built from the week's question set, and build weeks swap this manifest for the build-week pack; both variations are specified in the manifest reference.

## Day 1 exception

The opening day ships the introduction pack instead of a standard pack: the client-zero narrative deck with the mental-map diagrams, the programme and week story, the day-by-day promise, and the session mechanics. Read `references/day1-intro-pack.md` before building it. Client zero locked at v2.2 on 13 September 2026, so the pack is no longer blocked, and it opens on Meera Raghavan's question rather than on a company profile.

## Verification checklist

1. Slide one, and the notebook's first markdown cell, carry the day's business scenario in the
   stakeholder's words. A pack that opens on a topic title fails here.
2. The thinking from column 4 appears as a drawing the room makes before any tool is opened.
3. No student-facing file names anything planted in the dataset. Grep the pack for the plant words from
   the row's client-zero column; every hit must be in a TRAINER or INTERNAL file.
4. The interview questions from column 12 appear in the pack as questions, with their tags, and the
   answers written here are not copied back into the curriculum row.
5. Idea count per block within the cap, counted as decision sentences.
6. Every deliberate failure carries its exact error text or exact wrong output, and the demo reproduces it.
7. Demo notebooks run cold in a fresh Codespace, top to bottom.
8. Deck, notebooks and exercises follow the same segment order.
9. Every link was verified on the day it entered an artifact and carries that date; unverified slots say "to be found".
10. The take-home fails the shortcut test: pasting it into a chat assistant does not produce the deliverable (see the manifest for the resistance patterns).
11. No trainer names, marks, weights or clock times in any STUDENT artifact; Kalpa's fictional stakeholders are named on purpose and are not covered by that rule. Rs, never the currency glyph; no em-dashes; the banned-word scan passes.
12. Distractor audit on every quiz: no key is the longest option, key positions spread.
13. Audience tag present in every file name, and every file inside the subfolder its type belongs in.
14. The study notes and cheat sheet carry the same crux lines the deck closes on.

## File naming

```
content/W{ww}/D{d}/{folder}/C2_W{ww}_D{dd}_{topic}_{AUDIENCE}.{ext}
content/W{ww}/SAT/{folder}/C2_W{ww}_SAT_{topic}_{AUDIENCE}.{ext}
```

Read `content/README.md` before pass 1: it names the subfolder each artifact belongs in, the different shapes a build day and a Saturday take, and the rule that no file sits loose at a day folder's root. The topic half of the name carries only what the folder and the extension do not already say.

Examples: `slides/C2_W04_D03_half1_STUDENT.pptx`, `notebooks/C2_W04_D03_02_baskets_STUDENT.ipynb`, `takehome/C2_W04_D03_brief_STUDENT.md`, `trainer/C2_W04_D03_day_sheet_TRAINER.md`.

## The generation prompt

A paste-ready prompt that drives this skill from a fresh chat lives in `references/generation-prompt.md`. It parameterises week, day and date, enforces the spine gate, and lists the binding rules so a new chat cannot drift from them.

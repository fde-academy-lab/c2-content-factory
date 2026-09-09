---
name: day-pack-builder
description: Build the complete artifact pack for one full day of a cohort training programme, anchored to IITGN Cohort 2. Produces the trainer deck (or the half-one and half-two pair), rich demo notebooks, a toggle-driven activity, guided and unguided exercises with solutions, a shortcut-resistant take-home with a self-check spine, the Kahoot pack, study notes, cheat sheets and the pre-read. Use this skill whenever the request names a day pack, session pack, day build, "Week N Day D", "build Monday's session", the Day 1 introduction pack, or any deck-plus-notebook-plus-exercise set for a training day, even if only one artifact is named, because the pack's parts must stay consistent with each other. Runs from the locked curriculum row and refuses to invent a missing one.
---

# Day Pack Builder

One training day ships as one pack: everything a rotating trainer needs to deliver it and everything a learner needs to relive it. This skill turns one row of the detailed curriculum into that pack, in a fixed order, with approval gates so a wrong direction costs a screenful rather than a finished build.

## Inputs, and when to refuse

Read these before generating anything:

1. The day's row in the curriculum workbook (the week tab): focus, agenda, learner outcome, subtopics, trainer notes, client-zero cell, exercises, after-class tasks, resources, quiz plan.
2. The Structure tab: week types, the Saturday recap shape, assessment status, the client-zero narrative frame.
3. The project method file (06_Day_Pack_Method.md) and the content doctrine, when present in project knowledge.

Refuse, naming the gap, when any of these hold: the day's row does not exist; the client-zero scenario is unlocked and the day's examples need its entities; a reference link on the row is unverified. A plausible day generated around a gap is the failure this gate exists to stop. Say what is missing and stop.

## The method: mental model first, spiral always

Every topic opens by forming the mental model, then walks the whole pipeline shallow, then deepens on revisit. The canonical worked example, kept because the team teaches from it:

Explaining an LLM. Open on an experience everyone has had (type a prompt, get a response, the same shape as hitting a URL and getting a page). Walk the pipeline end to end at one shallow level: the model cannot read the sentence whole, so it breaks it into tokens (what a token is, in one intuitive beat, and that it varies by language); each token becomes an embedding (why numbers at all); position is injected (the same word means different things in different places); meaning lives as nearness in vector space (start with 2D coordinates the room can picture, then say it grows to thousands of dimensions; GPT-3's embedding width was 12,288, and note the correction if anyone says parameters, which run to billions); then inference emits the next token, one at a time, shaped by temperature and the top-k and top-p dials. One connected story, no stop too deep, and every stop gets its own deeper day later. That is the spiral.

Binding rules while building:

- At most four new ideas per two-hour block, counted as decision sentences. A day is one block-pair; if the row's ideas exceed the cap, the row is wrong and the build stops.
- Application before theory: the working thing and its output first, the name last.
- One deliberate failure per block, with the exact error text or the exact wrong output.
- Cognitive load is the design constraint: think trainer, psychologist and storyteller at once, and cut breadth before cutting the worked example.
- Durations only, never clock times; role labels only, never trainer names, in anything a student sees.

## The gates

1. **Envelope and continuity.** From the row: what the room already knows, what today must not repeat, what comes later. One short block, stated to the requester.
2. **The spine, for approval.** One screen: the deck decision (one deck, or half one and half two when the day carries two arcs), section list per artifact, the day's mental-model arc in one sentence, the deliberate failures, the activity choice with its toggle, the take-home shape. Stop and wait. Nothing downstream is built before the spine is approved.
3. **Build passes**, one artifact family per pass, in this order: deck(s); notebooks; activity; exercises plus solutions; take-home plus self-check spine; Kahoot pack; study notes, cheat sheet and pre-read. Each pass is a separate generation because mixing them flattens all of them.
4. **Verification.** Run the checklist at the end of this file and report results, including what failed and was fixed.
5. **Ship.** File names per the naming rule below, audience tags mandatory, files presented together.

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

The opening day ships the introduction pack instead of a standard pack: the client-zero narrative deck with the mental-map diagrams, the programme and week story, the day-by-day promise, and the session mechanics. Read `references/day1-intro-pack.md` before building it. It is blocked until the client-zero name and entity model lock.

## Verification checklist

1. Idea count per block within the cap, counted as decision sentences.
2. Every deliberate failure carries its exact error text or exact wrong output, and the demo reproduces it.
3. Demo notebooks run cold in a fresh Codespace, top to bottom.
4. Deck, notebooks and exercises follow the same segment order.
5. Every link was verified on the day it entered an artifact and carries that date; unverified slots say "to be found".
6. The take-home fails the shortcut test: pasting it into a chat assistant does not produce the deliverable (see the manifest for the resistance patterns).
7. No trainer names, marks, weights or clock times in any STUDENT artifact; Rs, never the currency glyph; no em-dashes; the banned-word scan passes.
8. Distractor audit on every quiz: no key is the longest option, key positions spread.
9. Audience tag present in every file name.
10. The study notes and cheat sheet carry the same crux lines the deck closes on.

## File naming

```
C2_W{week}_D{day}_{artifact}_{AUDIENCE}.{ext}
```

Examples: `C2_W04_D03_deck_half1_STUDENT.pptx`, `C2_W04_D03_demo_02_STUDENT.ipynb`, `C2_W04_D03_takehome_STUDENT.md`, `C2_W04_D03_day_sheet_TRAINER.md`.

## The generation prompt

A paste-ready prompt that drives this skill from a fresh chat lives in `references/generation-prompt.md`. It parameterises week, day and date, enforces the spine gate, and lists the binding rules so a new chat cannot drift from them.

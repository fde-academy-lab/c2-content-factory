---
name: exercise-builder
description: Turn a thinking exercise into a selection device a learner answers as a letter string, and write the solutions file that audits cleanly. Use whenever the work touches an exercise, a quiz, a Kahoot pack, a mid-session drill, a recap paper, an answer key or a solutions file, and whenever an existing exercise asks for prose where a selection would test the same thinking harder. Trigger it on words like exercise, drill, quiz, MCQ, distractor, answer key, solutions, item, or "make this answerable in chat". Covers the device wheel, item sizing from the drop point's minutes, distractor discipline and the audit that proves it.
---

# Exercise builder

An exercise is judged by whether the thinking is heavy and the writing is light. A learner should spend the whole slot deciding and about a minute recording, and the record should be a letter string they paste into chat.

Read `references/device-wheel.md` for the eleven devices with a worked item each, and `references/distractor-discipline.md` before writing any option set.

## Size it from the drop point

Item count comes from the drop point's minutes at about one item per minute. A fifteen-minute mid-session drill carries about fifteen items; a thirty-minute unguided exercise carries about thirty. State the arithmetic in the chat reply, never in the file.

Where a day has two or three unguided exercises, transpose the same devices across them: one on the concept, one on the code, one on the failure or operating layer. The devices repeat, the layer changes.

## What keeps its existing kind

Two exercise kinds are resistance patterns rather than selection devices, and they are not converted:

- **The AI-free lab.** A learner reads a fresh defective file cold and produces real output files. Its resistance is that no assistant has seen the file.
- **The guided carve.** The trainer builds it with the room mirroring. Its value is the mirroring, and a lettered version of it teaches nothing.

Keep both as they are, in kind and in wording. Everything else in the unguided set becomes a selection device.

## The device wheel

Raw-artifact diagnosis · fix a diagram with planted errors · reorder shuffled steps · pick from a lettered bank with a spare · multiple choice · fill the blank in code · find the defect in a snippet · predict the output · match with a spare · true or false · arithmetic on the artifact.

Draw from the wheel rather than repeating one device down the file. A file of eleven multiple-choice items tests recognition eleven times; a file that moves across the wheel tests diagnosis, ordering, prediction and computation.

## The answer format

Every item is answerable as a letter string pasted into chat, and the format line shows the shape in neutral letters that are not the answers:

```
Post one line: 1a 2c 3b 4d 5a 6b 7c 8d 9a 10c
```

Those letters are an illustration of the shape. Check that the illustration is not the key before shipping, which is one of the three things the audit fails on.

## Rules

- Learner-facing only. Any reasoning, rationale, timing, locator or facilitation that sits in an exercise file moves to its solutions file.
- Diagrams as Mermaid fenced blocks, so a learner reads them on GitHub with nothing installed.
- Each exercise gains a hands-on part pointing at its TODO notebook and listing the letters to post.
- The key is never the longest option, and key positions spread across a to d rather than clustering.
- A near-miss that is precise about the wrong grain is the best distractor. A nonsense option gives the answer away by elimination.
- No format line, worked example or preamble contains the true answers.

## The Saturday recap paper

The paper is a different drop point: a pen-and-paper sitting of 60 to 120 minutes, swapped between
learners and marked against a key, so every item must be markable by a peer in seconds and scores must
compare across the room and from week to week. Its items already exist: take them from the week's
paper in the tracker's item bank, `docs/curriculum/Saturday_papers.md`, in the bank's order. Author new
items only for the papers still to be built (Weeks 10, 11, 13 and 14, and the Week 4 Tuesday items),
and then to the same blueprint:

| Type | Minutes per item | What the key holds |
|---|---|---|
| Fill in the blank | 1 | The word, with any accepted variant in brackets |
| True or false | 1 | True or False |
| One correct option | 2 | One letter |
| More than one correct | 2.5 | Every correct letter; partial selection scores nothing |
| Scenario set | 2.5 | One letter per question in the set |
| Applied maths | 4 | The number with its unit, and the working a marker checks |
| Order the steps | 2.5 | The letter sequence |

Size the paper from its slot with those minutes, not one a minute: the blueprint gives the ME1 and ME2
weeks 60 minutes, a typical week 90 to 110 and the heaviest interview weeks 120, and the item counts
follow from the mix. Grade each item easy, medium or hard (roughly a third easy and a fifth hard across
the programme) and tag it `[S]`, `[F]`, `[SV]` or `[D]` with the roles it serves. Every item descends
from an interview question the week's rows carry, named in the bank's anchor column.

Three files, and only the first reaches a learner: the STUDENT paper, which prints the items and nothing
else; the TRAINER key, which carries each item's key, level, tag, roles, day and anchor; and the TRAINER
discussion guide, which runs the marking, takes the most-missed items first as an interview-answer
discussion with random call-outs, and closes on the scores by tag for Monday's remediation read. The
distractor rules above apply to every option set on the paper.

## The solutions file

Keep the sections the existing solutions already have: the idea being tested, the answers, the part worth arguing about, and where the pattern lives in production. Add two things inside that shape:

1. An item-by-item table: item, the key, why it holds, and a why-the-others-fail column carrying one clause per wrong option.
2. The hands-on picks: the TODO notebook's letter string, in order.

The solutions file is the only place the rationale lives. A solutions file is allowed the trainer voice; the exercise file is not.

## Done

- [ ] Item count matches the drop point's minutes at about one a minute, and the arithmetic was stated in the reply.
- [ ] The devices vary across the file and transpose across the day's exercises by layer.
- [ ] Every item is answerable as a letter, and the format line's letters are not the key.
- [ ] Nothing in the exercise file addresses the trainer.
- [ ] Every diagram is a Mermaid fence.
- [ ] The hands-on part points at a TODO notebook that exists.
- [ ] The solutions file keeps its four sections and gains the item table and the hands-on picks.
- [ ] `python3 scripts/distractor_audit.py <exercise file>` reports no failures.
- [ ] A Saturday paper matches its bank paper item for item, prints the items only, and fits its slot by the blueprint's minutes.

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

**Every stem is a business question on Kalpa data.** An item asks which decision a number supports, which of several plausible outputs is wrong and why, what a query or a groupby returns on the day's data, or which fix restores the right number. No item tests syntax alone: an item a learner could answer by knowing the language but not the business teaches the wrong thing for the screens this programme prepares for.

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
- The best wrong option is the plausible wrong number a hurried analyst produces: rows counted as customers, a total over unequal windows, a join that fanned out, an average that averaged averages.
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
the programme) and tag it `[S]`, `[F]`, `[SV]` or `[D]` with the roles it serves. A hard item is several
steps on an exhibit; an obscure fact never makes an item hard. Every item descends from an interview
question the week's rows carry, named in the bank's anchor column.

Three files, and only the first reaches a learner: the STUDENT paper, which prints the items in parts
named for what each shows, with a blueprint on page one (items, minutes and the easy, medium and hard
mix of every part) and each item's format and level beside its number; the TRAINER key, which carries
each item's key, tag, roles, day, part and anchor, the blueprint and what guessing alone would score;
and the TRAINER discussion guide, which runs the marking, takes the most-missed items first as an
interview-answer discussion with random call-outs, and closes on the scores by tag for Monday's
remediation read, which the Academic TA enters in the item-analysis workbook beside the key. The
distractor rules above apply to every option set on the paper.

The bank is the floor, never the ceiling. The week's source file,
`content/W{ww}/SAT/internal/C2_W{ww}_SAT_paper_source_INTERNAL.yaml`, lays five things on it, and
`scripts/build_saturday_paper.py`'s docstring gives the format:

- **Parts**, the printed order. Each part opens on a Kalpa situation in one or two sentences, with
  lettered exhibits where the part or a set needs one. One part, "Read the code, read the data", puts
  a few lines of the week's own notebook code or a small export on the page, and every wrong option is
  a trap the week staged, named in the key. Every bank item prints in a part, except up to six recall
  items (fill in the blank, true or false) that may move to the untimed stretch page to make room for
  harder timed items; the builder refuses a part list that drops a bank item, splits a scenario set or
  moves more than six.
- **New timed items** where the paper runs longer than the bank, each descending from the week's traps
  and anchors, in block-style YAML.
- **An exhibit** for every scenario set, drawn only from the set's own numbers.
- **The reasons** for every item: why the key holds, why each wrong option fails, and the interview
  answer in one breath.
- **An untimed stretch page** of written, interview-grade follow-ups.

`python3 scripts/build_saturday_paper.py W{ww} --docx` writes the paper and the key as Word files in
the format of the requester's baseline diagnostic (`content/W00/D2/paper/C2_W00_D02_diagnostic_STUDENT.docx`),
and the Word paper is what the room sits: its palette, fonts and running header; a first page with
what the paper is for, the rules, step one (each part rated 1 to 4 before any item is read), the
paper at a glance and a pacing ribbon; open question blocks that never split, each exhibit bound to
the first item that reads it; and a one-page answer sheet at the end. The key ends on a marking grid.
For a week with parts it also writes the item-analysis workbook, whose Ratings sheet sets each part's
ratings beside its right rate. Three things in the source file make the Word paper specific rather
than generic, and each is written for the week:

- `purpose`, the paragraph under "What this paper is for": the week's case in its own terms, what the
  paper finds out and how Monday uses it.
- `company`, the Rules table's Company row: the Kalpa company and every person the items name, with
  their role, as the week's own files give them.
- a `label` for every item, two to five words beside its level that say what the item asks the
  reader to do with what is in front of them ("Predict the output", "Spot the double count",
  "Case: Kalpa Retail, Q1 against Q2"), never the key and never a hint at it.

On a Saturday paper the options are of a length as well as of a precision: `scripts/distractor_audit.py`
fails an item whose longest option runs past 30 characters while its shortest is under 60 percent of
it, and the fix is an option edit in `data/programme/paper_edits.yaml`, never a stem or a key.

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

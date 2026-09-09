# The Day Pack Manifest, artifact by artifact

Every specification below binds the build. Where this file and an older day-pack spec disagree, this file wins.

## 1. Deck, one or two per day

One deck carries a single-arc day. A day with two distinct arcs (for example a morning concept arc and an afternoon applied arc) splits into half one and half two, each with its own opening promise and its own close. Split when the second arc would force a mid-deck reset of the mental model; never split to hide an over-full day.

Deck behaviour: visual and thin, narration in the trainer notes, one idea per slide, the day's mental-model diagram repeated at each section boundary with the current part lit, a numbered step card closing every section, and the crux line on the final card. The deck teaches in the spiral order: everyday anchor, whole pipeline shallow, then the day's designated deep stops.

## 2. Demo notebooks, rich and progressive

A notebook is a teaching document that happens to run. Cell order per concept: the idea in one markdown beat; a diagram or mental-model cell; the working demo; its visible output; the deliberate failure with its exact trace; the fix; and, at each milestone, one industry example of the technique in production and one interview question the milestone just made answerable.

Progression is the notebook's spine: build the thing in variations, smallest first, exactly one new element per step. The canonical shape, kept from delivered work: a simple agent loop by hand, then the loop with one tool, then many tools, then one turn, then multiple turns. Apply the same ladder logic to any topic: each notebook section is the previous section plus one decision.

Setup cells sit at the top so the notebook runs cold in a fresh Codespace. Markdown outnumbers code where the concept needs it; walls of text are as banned as walls of code.

## 3. Activity, zero or one per day

Build one when the concept has a decision, a comparison or a hidden intermediate state; otherwise skip. Forms: a single-file HTML page with no browser storage and no API key, or an Excel template with dropdowns and data validation. Interaction is toggle-driven with minimal typing: the learner flips choices and watches consequences. Every activity ends in a state worth screenshotting, and the Excel forms double as takeaway decision tools the learner keeps.

## 4. Guided and unguided exercises, few and think-heavy

Create only what fits the session's real minutes. Guided runs trainer-led with the room mirroring. Unguided runs solo in a break or the second half, no hints, solution released at close. Answers are selection, prediction, repair or short computation, never long typing: the thinking is heavy, the writing is light. Every exercise names its drop point in the agenda.

## 5. Solutions, one per exercise

High-level explanation, the answer, the line-by-line why, then where the pattern appears in production. Release rule: unguided solutions at close of session; take-home solutions open the next session, which begins by walking one.

## 6. Take-home, one per day, shortcut-resistant

Substantial by design and openable the next morning. It must fail the shortcut test: pasting the brief into a chat assistant does not produce the deliverable. Resistance patterns, use two or more:

- The deliverable includes process evidence: challenges-log entries, a comparison of two named tools actually run, a screenshot of an exploration step.
- The task runs on the learner's own artifact from today (their notebook state, their cleaned file), which an assistant has never seen.
- The task requires reading or watching named, verified sources (a blog, a talk, a repository's issues, a newsletter) and citing one specific thing found there.
- The answer format is a defended choice with a threshold, not prose an assistant can pad.
- A self-check spine ships with it: planted checkpoints (a count, a value, a behaviour) the learner verifies alone, so they know they are right before class does.

Exploration links must be verified with a date; a link from memory never ships.

## 7. Kahoot pack, daily, ungraded

Six to eight items per the row's quiz plan, traps included, plus the return question from the previous day one level up. Ungraded, a performance indicator. Distractor audit mandatory.

## 8. Trainer notes and the day sheet

One TRAINER file: the two-minute continuity block from the row (start from, do not repeat, go as far as, stop before, comes later), per-slide Say, Then, Draw, Ask, Trap and Bridge labels, the breaks to run with exact error text, the ranked cut list, and the checkpoint questions. Never merged into any student artifact.

## 9. Study notes, after delivery

Written once the session's real shape is known and revised against the day's transcript when it arrives: what was covered, the worked examples, the failures and their fixes, the crux lines, and the model answers to the day's interview questions. The transcript revision is a standing step, never optional polish.

## 10. Cheat sheets, zero to many

One per major topic when the day earns it; none when it does not. Landscape concept format, six to eight panels, the crux line per topic, and a gap variant with a quarter of the cells blanked for self-testing.

## 11. Pre-read and setup, ships tonight

The next day's vocabulary as a gap sheet plus any setup the learner must complete tonight. Setup for tomorrow shipping tonight is a hard rule with no exceptions.

## 12. Tiered extras

One stretch task for fast finishers and one recovery task for stuck learners, built in advance, allowed to be weekly rather than daily.

## 13. Corrections card, conditional

Whenever a live claim proves wrong, the next session opens on a corrections card: the claim, the correction, the source. A slide, never an apology.

## Weekly and build-week variations

**Saturday recap paper (regular weeks).** Built from the week's question-set row: pen and paper, AI-free, about two hours, short-answer format so peers can cross-evaluate, with the Academic TA's discussion guide and the call-out list. Ungraded.

**Build weeks** swap this manifest for the build-week pack: the five sub-problem briefs (three groups per problem, groups of four), assessor rubric, GD prompts with facilitation notes for the expert days (Friday and Saturday, about 30 minutes per group), the trainer's parallel build, daily checkpoint questions, the presentation scoring sheet, and the catch-up plan. No tests, no Kahoot.

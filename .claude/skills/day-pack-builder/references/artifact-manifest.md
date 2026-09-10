# The Day Pack Manifest, artifact by artifact

Every specification below binds the build. Where this file and an older day-pack spec disagree, this file wins.

## 1. Deck, one or two per day

One deck carries a single-arc day. A day with two distinct arcs (for example a morning concept arc and an afternoon applied arc) splits into half one and half two, each with its own opening promise and its own close. Split when the second arc would force a mid-deck reset of the mental model; never split to hide an over-full day.

Deck behaviour: visual and thin, narration in the trainer notes, one idea per slide, the day's mental-model diagram repeated at each section boundary with the current part lit, a numbered step card closing every section, and the crux line on the final card. The deck teaches in the spiral order: everyday anchor, whole pipeline shallow, then the day's designated deep stops.

## 2. Demo notebooks, rich and progressive

A notebook is a teaching document that happens to run. Cell order per concept: the idea in one markdown beat; a diagram or mental-model cell; the working demo; its visible output; the deliberate failure with its exact trace; the fix; and, at each milestone, one industry example of the technique in production and one interview question the milestone just made answerable.

Progression is the notebook's spine: build the thing in variations, smallest first, exactly one new element per step. The canonical shape, kept from delivered work: a simple agent loop by hand, then the loop with one tool, then many tools, then one turn, then multiple turns. Apply the same ladder logic to any topic: each notebook section is the previous section plus one decision.

Setup cells sit at the top so the notebook runs cold in a fresh Codespace. Markdown outnumbers code where the concept needs it; walls of text are as banned as walls of code.

The full build procedure is the `notebook-builder` skill. Read it before writing a cell. It carries the shared helper module that every notebook in a day imports, the MAP, DO, SEE, CHECK, SUM rhythm per section, the break-it-on-purpose anatomy, and the pick-from-options exercise twin. Its binding numbers: at least three rendered diagram outputs and five passing `check()` calls per notebook, every code cell carrying a saved output, and the whole notebook executed cold from a clean state so it reads on GitHub before anybody presses run. Data comes from `../data/` through the helper's loaders; a notebook that pastes records into a cell has created a second copy of one truth. Each unguided exercise that has a notebook to point at gains a TODO twin at `notebooks/C2_W{ww}_D{dd}_ex{n}_hands_on_STUDENT.ipynb` and a filled, executed solution twin in `exercises/solutions/`. The gate is `scripts/nb_check.py`, which `scripts/verify.py` runs.

## 3. Activity, zero or one per day

Build one when the concept has a decision, a comparison or a hidden intermediate state; otherwise skip. Forms: a single-file HTML page with no browser storage and no API key, or an Excel template with dropdowns and data validation. Interaction is toggle-driven with minimal typing: the learner flips choices and watches consequences. Every activity ends in a state worth screenshotting, and the Excel forms double as takeaway decision tools the learner keeps.

The build procedure for both forms is the `companion-builder` skill. The HTML page carries a guided walk on one Next button with a narration card per event, experiment cards each holding situation, hypothesis, watch for, run, what happened, why it matters, the rule and a sequence popup, diagrams from the shared builder set ported to JavaScript, a decision visual wherever the topic has a choice, a calculator for any rule with a number, and a small glossary of the day's terms. Important text is never grey, every control does something, and nothing is preloaded so no button looks dead. A single page with sections and a left rail is enough for a one-topic day; a grouped title bar arrives only when the day carries several distinct parts. The gate is `scripts/html_sweep.py`.

The Excel side is no longer an alternative to the HTML page. Every teaching day ships **both workbook forms that the day earns**, in `demos/` beside the companion.

**The decision tool**, one per teaching day. One tab per taught decision, each ending in a computed verdict cell holding a sentence a person reads aloud rather than a number. An export tab assembles a paste-ready brief by formula. Yellow cells are inputs and everything else is computed. One planted defect per tab, which the learner finds first, and an interior optimum so fixing one thing does not clear the release. Formulas that survive LibreOffice only: `INDEX` and `MATCH`, `COUNTIF`, `SUMPRODUCT`, `IF`, `AND`, `OR`, `ROUND`, never `XLOOKUP` or a bare `IFS`. Three to five tabs plus the export tab.

**The live miniature**, built where the day also carries a repeatable procedure a learner should run again. A run sheet of the procedure's moves with an observed column the learner fills and a computed status per row, plus a lookup from symptom to first check, fix, evidence and owner.

A small recalc manifest sits beside each workbook, named to the stem rule with the `INTERNAL` audience, naming the verdict cells to assert and the design decisions to flip. `scripts/xlsx_recalc.py` recalculates through LibreOffice headless, asserts every named verdict, applies each flip and asserts the moved verdicts. A workbook whose verdict does not move under any flip is a spreadsheet with words in it.

## 4. Guided and unguided exercises, few and think-heavy

Create only what fits the session's real minutes. Guided runs trainer-led with the room mirroring. Unguided runs solo in a break or the second half, no hints, solution released at close. Answers are selection, prediction, repair or short computation, never long typing: the thinking is heavy, the writing is light. Every exercise names its drop point in the agenda.

The build procedure is the `exercise-builder` skill. Item count comes from the drop point's minutes at about one item per minute, and the arithmetic is stated in the chat reply rather than in the file. Every unguided thinking exercise is a selection device answerable as a letter string pasted into chat, with the format shown in neutral letters that are not the answers. The device wheel is raw-artifact diagnosis, fix a diagram with planted errors, reorder shuffled steps, pick from a lettered bank with a spare, multiple choice, fill the blank in code, find the defect in a snippet, predict the output, match with a spare, true or false, and arithmetic on the artifact; draw across it rather than repeating one device down a file. Where a day carries two or three unguided exercises, transpose the same devices across them by layer: one on the concept, one on the code, one on the failure or operating layer. Diagrams are Mermaid fenced blocks. Each exercise gains a hands-on part pointing at its TODO notebook and listing the letters to post.

Two kinds keep their existing shape rather than becoming selection devices, because their value is the resistance rather than the selection: the AI-free lab, where a learner reads a fresh defective file cold and produces real output files, and the guided carve, whose worth is the room mirroring.

Exercise files are learner-facing only. Any reasoning, rationale, timing, locator or facilitation that sits in an exercise file moves to its solutions file. The gate is `scripts/distractor_audit.py`, which fails a file where a key is the longest option, where key positions cluster, or where a format line contains the true answers.

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

A **visual sheet** ships beside the text sheet, one per major topic, built from the same diagram builders the notebook helper and the companion use, laid out as Mermaid panels in the markdown. It carries pictures and nothing else: the day's flows, stacks, decision trees and matrices on one landscape page, so a learner recovers the shape of the day without reading a sentence. The text sheet stays the eight-panel form it already is; the visual sheet does not replace it.

The landscape PDF is produced through the `fde-cheat-sheets` method. Where that toolchain is unavailable in the session, the markdown with its visual panels ships and the PDF is listed as deferred, naming what was missing. The crux lines on every sheet match the deck's closing cards word for word, because a learner who memorises one and hears the other stops trusting both.

## 11. Pre-read and setup, ships tonight

The next day's vocabulary as a gap sheet plus any setup the learner must complete tonight. Setup for tomorrow shipping tonight is a hard rule with no exceptions.

## 12. Tiered extras

One stretch task for fast finishers and one recovery task for stuck learners, built in advance, allowed to be weekly rather than daily.

## 13. Corrections card, conditional

Whenever a live claim proves wrong, the next session opens on a corrections card: the claim, the correction, the source. A slide, never an apology.

## 14. The first-use walkthrough, in whiteboards/

Any console, editor or tool used for the first time on a day gets a browser-first walkthrough in `whiteboards/`, beside the day's board diagrams. It is written for a learner in front of the screen, not for a trainer describing it.

Numbered steps, each carrying what you type and what you should see. Screens are described by what they ask for rather than by where the button sits, with a note that labels move, because a walkthrough pinned to a label goes wrong the week the vendor renames it. Every trap in it was verified by running it rather than predicted: the wrong default, the setting that looks optional, the state the tool leaves behind. A probe list says what each check tests. The clean-up closes it, so a learner does not leave a machine running. The CLI is an optional appendix rather than the main path.

`whiteboards/` also holds the day's diagrams as Mermaid, so a trainer can draw them on a board from the fence rather than from memory, and so the same shapes reach the deck, the notebook and the companion unchanged.

## 15. Frameworks and formulas

Where a day introduces a named framework, it ships as a page with each letter defined, the situations it applies to, its numbered steps, where the idea came from with dated sources, one case, a without-it and with-it contrast carrying artifact snippets and outcomes, and where the framework stops. A framework taught only in its correct use leaves a learner unable to recognise the wrong use.

Where a day carries a rule with a number in it, that rule ships as a calculator rather than as a formula on a slide: the formula shown, the inputs live, and one sentence saying what the number means once it lands. Convert every formula into a division, a count, a two-by-two or a plug-in strip a learner can run in their head, and verify the simple version against the exact algebra before it ships.

Any framework this programme invented is marked as this programme's own construction, inside the artifact, where the reader needs it. An established name and a name of ours never sit unlabelled in the same list.

## Weekly and build-week variations

**Saturday recap paper (regular weeks).** Built from the week's question-set row: pen and paper, AI-free, about two hours, short-answer format so peers can cross-evaluate, with the Academic TA's discussion guide and the call-out list. Ungraded. It ships in `content/W{ww}/SAT/`, whose folders are `paper/`, `answer-key/` and `discussion/`.

**Build weeks** use the folders `briefs/`, `rubrics/`, `gd/`, `parallel-build/`, `checkpoints/`, `mocks/`, `trainer/` and `internal/`, on their Saturday as well, and swap this manifest for the build-week pack: the five sub-problem briefs (three groups per problem, groups of four), assessor rubric, GD prompts with facilitation notes for the expert days (Friday and Saturday, about 30 minutes per group), the trainer's parallel build, daily checkpoint questions, the presentation scoring sheet, and the catch-up plan. No tests, no Kahoot.

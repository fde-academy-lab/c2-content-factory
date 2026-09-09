# day-build-specs · the spec for every artifact in a day's kit

Read the section for an artifact before building it. Each section says what the artifact is for, its internal rhythm, its rules, and what proves it is done.

## Decks

**For.** Establishing a concept on the projector, and recovering it a month later. One deck per block; each answers one question and ends in a named artifact the next block opens with.

**Rhythm.** Every major topic is a ten-slot concept unit spread over several slides: pain in money, minutes or frustration with a one-keystroke question; ground it; first-principles strip; clearest example; derived framework, simplified and derived in front of the room; steps; worked example; application to the world; gotcha; crux plus transfer question. Inside a unit, use the six beats where they serve: show a familiar situation, ask for a prediction, reveal one mechanism, show its output, change one condition, let the learner diagnose or repair, recall the principle. Diagram before table before worked example. Concept slide then applied slide on the world. Question slide then, immediately, its answer slide: the claim in a tinted band, a row per wrong option saying why it does not hold, a paired mental model.

**Rules.** Copy the approved reference deck by measurement: grid, type, palette, patterns. The heading names the topic; the assertion goes in the lead line. One idea per slide; more slides carrying one idea each. Colour is ink, not wallpaper; at most one tinted band per slide; no bordered tables, no coloured row fills, no dark divider slides; numbered kickers replace dividers. Titles under 54 characters, with a guard proven to fire. Zero meta-content on slides: facilitation and design rationale in speaker notes only. Complete sentences in every cell and callout. Slide kinds to draw from: title, definition with signals, map, two-column, table, quad, numbered steps with a result column, flow with arrows, lanes, artifact with annotation, numbered rules, side-by-side compare, activity, checklist, exploded stack, cycle, question, answer.

**Done.** The PPTX is built, passes the validator, the meta scan, the tic scan and the em-dash scan on the built file, renders to PDF, and the thumbnails were looked at.

## Companion HTML

**For.** Making a concept move on the projector, and letting a learner play with it afterwards. One file, no install, the core runs offline; a web font may load online with a system fallback.

**Unifying model.** An exploded anatomy of the thing being built, every part clickable to the page that builds it; and a build order showing which part each stage adds, what becomes possible, and the limit that sends the learner to the next stage, with two worked uses of the order (diagnosing an inherited system, planning a new one).

**Information architecture.** Title bar grouped by what the learner is doing: understand, build by hand, build without code, test, operate; reference and contact on the right; a left rail listing the current page's sections with active tracking.

**Page kinds and their anatomies.**
- Guided walk: one Next button, a narration card per event, the diagram, the artifact and the meter moving together; a meter that explains itself with a legend and a per-item breakdown on click.
- Experiment cards: situation, hypothesis, watch for, a run button, then what happened, why it matters, the rule, and a sequence-diagram popup. One change per card.
- Classify exercise: lines with lettered choices, per-line feedback, a running score.
- Layer builder: a system map that grows a part per layer, code with the current layer highlighted, a capability line.
- Workbench: a few fields in, real code out (spec, guard, tests), and a verdict that refuses bad inputs.
- Simulator: a stepper of choices, a run with a generated sequence diagram, probes against the configuration, a readiness verdict with reasons, then the console steps and config generated from the choices.
- Ladder pages: options with verified rates and sources, a decision tree, a decision matrix, the same run priced on every option, a calculator for the deciding inequality.
- Playbooks: a pyramid with popups per level, a decision tree for the instrument, methods each opening a worked example with a snippet, an assertion catalogue, gates and pipelines as flowcharts, practices translated into a four-column table, a symptom lookup.
- Frameworks: each letter defined, situations, numbered steps, where the idea comes from with sources, a case, a without-it and with-it contrast with artifact snippets and outcomes, where it stops.
- Formulas: each rule with a number as a calculator showing its formula and a sentence on what the number means.
- Reference: practices with in-place checks and mistakes with how each shows in the artifact; a filterable glossary saying where each term first matters; visual and text cheat sheets, printable; a reader and builder for the day's central artifact; generators for what learners paste elsewhere; a contact popup that composes a mail.

**Builders.** Sequence, flow, vertical flow, pyramid, tree, matrix, ladder and anatomy diagrams generated from data by small functions, so every diagram is consistent and the simulator can draw whatever run it produced.

**Rules.** Important text is never grey. Every control does something. Nothing is preloaded so that a button looks dead. A popup only where it adds a breakdown, a worked example, a sequence, or a why-this-step. Full sentences. Simulation labelled as simulation; prices dated; nothing invented.

**Done.** A headless browser sweep visits every page, clicks every navigation, popup, stepper, run and sample control, records zero console errors, and checks each dropdown by the element at its screen coordinates.

## Notebooks

**For.** Making the learner do the thing, with or without an account, and recovering it a month later.

**Structure.** One concept per notebook, progressive across the day; each carries forward only the code it needs so it runs cold. A shared support module holds the world fixtures, an offline mock that scripts a plausible run, a cost meter that records every call, and the diagram builders. Every notebook opens with a MOCK toggle and a model choice, flips to live with one line, and states the IAM action and model access it needs.

**Rhythm per section: MAP, DO, SEE, CHECK, SUM.** A map cell rendering two diagrams side by side from code (where this notebook sits in the day; what this section adds). A prose cell saying what is about to happen and why. One code cell carrying one idea. Printed output, a trace or a message view. A check cell with assertions that print pass or fail without stopping the class. At the end of each logical group, a summary cell with a diagram and a table.

**Rules.** Diagrams render from code cells so they survive Colab and GitHub. Ship executed from a clean state so outputs show on open. One break-it-on-purpose cell per notebook. One credentials-stripped rerun where a test claims to need nothing. An honest sentence wherever the mock scripts a failure. Meter every call and show the meter. Any file expecting interactive input ends with a comment block of test inputs and expected outcomes. Exercise notebooks use pick-from-options TODOs: a lettered comment above a placeholder; a solution version that executes exists beside it.

**Done.** Every notebook executes with zero errors and every check passing, and the count is reported.

## Exercises

**For.** Making the learner think, on GitHub Discussions, with nothing in the file that is not for them.

**Shape.** Three per session, one per block, about thirty items across six or seven parts, plus one open take-home. Answers as letter strings pasted into chat, with the format shown in neutral letters. A separate answer key holds item-by-item reasoning and a why-the-others-fail column.

**Device wheel.** Read a raw artifact and diagnose; fix a diagram with planted errors; reorder shuffled steps; pick from a lettered bank with a spare; multiple choice; fill the blank in code; find the defect in a snippet; predict the output; match with a spare; true or false; arithmetic on the artifact. Transpose the same devices across the day: exercise one on the concept, exercise two on the code, exercise three on the testing or operating layer. Each exercise carries a hands-on part pointing at a TODO notebook with pick-from-options markers.

**Rules.** Learner-facing only: no trainer voice, locator, timing or facilitation. Diagrams as Mermaid fenced blocks. Distractor discipline: the key is never the most obvious or the longest option, positions spread across a to d, a near-miss precise about the wrong grain is the best distractor, and no format line reveals the answers.

**Done.** The distractor audit is clean and the key is a separate file.

## Excel tools

**For.** Handing the learner a framework they keep and apply to their own work.

**Two kinds per session.** A decision tool: one tab per taught decision, each ending in a computed verdict, and an export tab that assembles a paste-ready brief by formula. A live miniature: a run sheet of scripted moves with an observed column and a computed status, a classifier for the day's central artifact, and a lookup from symptom to first check, fix, evidence and owner.

**Rules.** Yellow cells are inputs; everything else computed. A planted defect per tab the learner finds first. Interior optimum: fixing one thing must not clear the release. Formulas that survive LibreOffice: no XLOOKUP, no bare IFS; INDEX and MATCH, COUNTIF, SUMPRODUCT.

**Done.** Recalculated through LibreOffice headless with verdict strings asserted, then the design decisions flipped and the moved verdicts asserted.

## Cheat sheets

One screen each; visual sheets from the diagram builders and text sheets of code, shapes, formulas, ladders and checklists; landscape concept format; printable; nothing else on them. One per block or per major topic so far.

## Walkthrough

For any console or tool used for the first time. Browser-first markdown: numbered steps, what you type, what you should see, traps verified by running them, a probe list saying what each tests, the clean-up. Screens described by what they ask for, with a note that labels move. The CLI as an optional appendix.

## Trainer playbook

For a trainer reading it live. Front page: slide range to topic with minutes, use case per topic, three things that must land, ranked cut list, slides where the question goes to the room. Per slide, only the fields that apply from Say, Then, Draw, Ask, Trap, Do this, Bridge; Say lines quotable and specific, starting with the use case.

## Study notes

After delivery, from the transcript, through the study-notes skill: a terrain map that fills up session by session, one running thread through every concept, verified field cases, a no-writing self-check, an ordered reading path; markdown and print-ready PDF.

## The numbers that size a day

About 2.5 minutes per interactive slide. Per sixty-minute block: 20 explain and demo, 30 learner work, 5 debrief, 5 flex. About thirty items per twenty-five-minute exercise. Four new ideas per two-hour block. Notebooks of 16 to 25 cells with at least three rendered diagrams and five checks. One planted defect per Excel tab. Fifteen to twenty cases in a regression set, and one failure in n cases moves a rate by 100/n points.

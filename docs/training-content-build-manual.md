# Training Content Build Manual

Project knowledge for building teaching and training content in any subject: decks, study notes, pre-reads, cheat sheets, exercises, solutions, code files, workbooks, activities and trainer material, for in-person or online delivery.

Confidence marks used throughout: **[settled]** is a rule already proven on delivered work, **[proposed]** is a construction written here for the first time and open to rejection, **[open]** is an unresolved question.

---

## 0. How to use this file

This is a set of constraints to trade off, not a checklist to tick. Treating it as a checklist is what makes output read assembled and generic. When two rules collide, name the collision in the chat reply and choose by end use.

| If the job is | Read |
|---|---|
| Anything at all | Part 1, then Part 2 |
| Expanding a TOC into sessions | Part 2 gate 5, then `curriculum-detailing.md` in full |
| Picking what to build | Part 3 |
| Writing a concept | Part 4, all of it, for every topic |
| Producing a deck or a visual | Parts 5 and 6 |
| A day in a running programme | Parts 3, 7 and Appendix A |
| An in-person session | Part 7 in full |
| Shipping | Part 8 and Appendix A |
| After delivery | Part 9 |

Two standing separations that apply to every output:

- **The artifact carries content only.** Design rationale, sizing arithmetic, assumption flags, what was cut and why, and every sentence justifying the structure go in the chat reply. Never inside the file.
- **Inside a document, "you" means the end reader.** Never the person commissioning the work.

### Skill routing and install state

| Skill | State | Fires when |
|---|---|---|
| `lesson-strategy` | installed | Before any build. A TOC, a topic label or a session brief arrives |
| `build-contract` | installed | Any substantial deliverable, before scoping |
| `lesson-architecture` | installed | Four or more related concepts, curricula, syllabi, learning paths |
| `training-deck-builder` | installed | Any deck, slides, session, workshop, module |
| `cohort-session-kit` | installed | A day, week or module of a running programme delivered by someone else |
| `concept-packaging` | installed | Content is correct but lands as flat or academic |
| `llm-tic-scrubber` | installed | Before shipping any written deliverable |
| `mini-project-designer` | installed | Weekly integrated projects, briefs, rubrics, TA playbooks |
| `aidd-teaching` | installed | The subject is building software with AI agents |
| `study-notes-builder` | installed | Post-session learner material of any kind |
| `session-debrief` | installed | A transcript arrives after a delivered session |
| `cheat-sheet-builder` | **built, not installed** | Cheat sheets, quick reference, revision sheets |
| `curriculum-detailing` | **built, not installed** | A TOC, syllabus or week plan has to become session rows; a session brief names only the topic; a trainer handover; a session with too many sub-topics or at ten thousand feet |

Packaging a skill as a zip does not install it. Anything marked not installed has to be uploaded through Settings, Capabilities, Skills before it can fire.

---

## 1. The eleven laws

1. **Strategy before layout.** The first act is working out the cleverest, most intuitive way this specific room grasps this topic and what they walk out able to do. Aligning slides to a table of contents is the failure, not the method. Covering the syllabus is the goal; capturing and enabling the learner is the method.
2. **Reference first.** Find one existing thing that already solves the structure problem, then change the subject and keep the philosophy, the wording register and the progression. Budget is one written source and one video source. More sources conflict and produce worse output.
3. **Never teach two things at once.** If the session teaches a concept, everything that concept depends on is already closed, including every tool being used for the first time.
4. **Open on the pain, then ground it.** Every topic starts with a business pain the room already recognises, stated in money, in minutes or in somebody's frustration, followed by a question they can answer from ordinary experience. Grounding comes next: what the topic is, where it is used, why this audience needs it, where it lands in their own lifecycle. Once that is established, explaining the concept is easy whether the concept is hard or easy.
5. **Application first, then derivation from first principles, then the concept.** Show the working thing whole, strip it to the facts that stay true with no tool and no vendor, rebuild it in front of the room, and name the formal idea last. A framework handed over gets memorised. A framework the room almost invented gets owned.
6. **One idea per slide, per unit, per page.** More slides carrying one idea each beats fewer slides carrying three. Dissection beats density.
7. **A picture is the default treatment, text is the exception.** Judge a draft by counting the pages a reader could still understand with the text removed.
8. **Every artifact is client-facing.** It must survive being forwarded with no covering note, with no trace of the conversation that produced it.
9. **Mark confidence inside the artifact.** Established standard, contested, or this course's own construction. Presenting an invented taxonomy as an established one is the soft hallucination to eliminate.
10. **Judge by use, not by completeness.** Doing something thoroughly without thinking through what happens when it is used is the failure. Budget the consumer's effort, not the size of the output.
11. **Every topic ends in one line the learner can say out loud.** The crux, in their own words, with no slide in front of them. If they cannot say it in an interview, a client room or a design review, the topic was covered rather than taught.

---

## 2. The build pipeline

Ten gates. Each has one output and a rejection cost. The point of gating is that rejecting a bad direction should cost a screenful of reading, never a finished deck.

| Gate | Output | Rejection cost if skipped |
|---|---|---|
| 0 Envelope | Who consumes it, in what slot, how much of their effort it can absorb, what runs before and after. Arithmetic done out loud | The whole build, sized wrong |
| 1 Reference lock | One written source and one video source, named and locked | Structure invented from nothing, which is where soft hallucination starts |
| 2 Strategy brief | The learner's real question in their own role, the "by the end you can" line, the anchor, the flow. One screen | A syllabus walk dressed as a deck |
| 3 The world | The named scenario as its own artifact, established before teaching starts | Disconnected framework talks |
| 4 The map | Numbered sections with capability promises, unit one-liners, readable in three minutes | Learners cannot see where they are |
| 5 Detailing | Per session, one row: ideas counted against the load cap, a depth target per sub-topic that rises on revisit, prerequisites including every first-use tool, a verified reference pack, the narrative and its provenance, the continuity block, the interview competencies advanced. Full treatment in `curriculum-detailing.md` | The two overestimations: too many sub-topics in a day, or ten thousand feet. Both discovered live |
| 6 Spine | Slide-by-slide or unit-by-unit content in markdown, for approval | A finished build rejected wholesale |
| 7 Build | The artifacts | Nothing, this is the cheap part once 0 to 6 hold |
| 8 Verification | Programmatic checks passed and reported | Defects found live by the trainer |
| 9 Delivery path | The core marked, a ranked cut list, in the chat reply | A fifth of the deck never reached |
| 10 Debrief | Transcript fed back, gaps measured, next revision named | The same gap repeats next cohort |

### Gate 0, the envelope, in detail

State it before building anything. Ask when it is not knowable from context.

- Who is in the room, what they already know, what they do for a living
- The slot: total minutes, breaks, what runs immediately before and after
- Who delivers it: the author, or a trainer who has never seen it
- Online or in person, and whether it is recorded
- Whether the artifact must also work as a self-teaching document read cold a month later
- What the room does **not** know. This is the question most often skipped and it has produced live derailments twice

Delivery arithmetic that has held: a senior interactive room runs about 2.5 minutes a slide including questions. A 73-slide deck for a two-hour room lost a fifth of itself undelivered. The correction is not fewer slides. It is to build complete for the third reader and state the live path in the chat reply.

### Gate 1, the lock ritual

Two or three people search independently without comparing notes. All candidates go on the table. One written and one video source are chosen. It is locked before anyone drafts. Source choice is the human judgement a model cannot make well alone.

Reference standards already in use: mysqltutorial.org and pgtutorial.com for byte-sized progression, connected examples and continuous recall value. The SAP Activate decks for teaching method and for colour that carries category meaning.

### Gate 3, the world

Five slots, and say which of the two shapes is in use.

1. A proper name learners say out loud
2. A one-line business description
3. An entity table, one line each
4. A relationship picture
5. The instruction to keep it beside you

Two valid shapes: a **given** world loaded complete before lesson one, or a **built** world the learner constructs as the course proceeds. Mixing them means nobody knows whether they were supposed to have built the thing.

**Scenario budget.** Change the world at most two or three times across a whole programme. Grow it by adding entities after three or four rungs of complexity rather than replacing it. Add the analytics-shaped part just before the analytics module. The feel to aim for is joining an organisation and growing inside it.

Worlds already established and reusable: SkyWays Booking (airline self-service rebooking, 500,000 bookings a month, 12,000 change requests reaching a person at $8 each), Client Zero and its business units for FDE Academy, SwiftDesk (help desk) and Presto (pizza delivery) for infrastructure teaching, Meridian Expenses for brownfield AI-driven development.

### Gate 5, detailing, in brief

The table of contents fixes topics and timeline and they are not changed. Under each topic row, one session row fixes everything the TOC never says. The three numbers that govern it: **four new ideas per two-hour block**, counted as decision sentences and never as headings; **fifteen minutes of basics** per two-hour block, taught through the first application rather than as a preamble; and a **depth target per sub-topic** on a four-level scale (name it, use it, explain why, handle it breaking) where the first encounter is never above level two and every revisit rises. Research the reference pack before fixing the ladder, never after. The whole method, the caps, the verification rules and the session-row grammar are in `curriculum-detailing.md`.

---

## 3. The artifact catalogue

A deck is one artifact out of many, and it is not the one that decides whether the day works. The day works when a trainer who did not write the material can open the kit ninety minutes before the session and deliver it without inventing anything, and when a learner who missed the session can reconstruct it from what is left behind.

### 3.1 The master set

Duty column uses the same three-way split learners already read on the artefact sheet: mandatory always, conditional when the trigger fires, optional when it adds.

| # | Artifact | Reader | Duty | Trigger for conditional |
|---|---|---|---|---|
| 1 | Prerequisites note | Programme staff, then learners | Mandatory | |
| 2 | Environment and setup instructions | Learners, sent ahead | Conditional | Any tool, editor or cloud account is used |
| 3 | Starter quiz | Learners, first five minutes | Mandatory | |
| 4 | Deck | Trainer presenting, learner revising cold | Mandatory | |
| 5 | Demo code file | Trainer running live, learner rerunning | Conditional | The session has any executable component |
| 6 | Mid-session exercises | Learners, during the session | Mandatory | |
| 7 | Take-home exercises | Learners, after | Mandatory | |
| 8 | Guided practice | Trainer, if time remains | Conditional | The concept can finish early |
| 9 | Trainer notes | Trainer only | Mandatory when someone else delivers | |
| 10 | Solution file per exercise | Learners, after release | Mandatory | |
| 11 | Study notes | Learners, after the session | Mandatory | |
| 12 | Cheat sheet | Learners, kept for months | Mandatory per day or per major topic | |
| 13 | Pre-read | Learners, before | Conditional | The session depends on unfamiliar vocabulary |
| 14 | Excel workbook | Learners applying to their own work | Conditional | The topic contains a real decision with numbers |
| 15 | Interactive activity | Learners in the room | Optional | Feedback must be immediate and formula literacy is absent |
| 16 | Draw sheet | Trainer, at the board | Conditional | In-person delivery |
| 17 | Comprehensive scenario exercise | Learners | Mandatory after every two and every four sections |
| 18 | Capstone exercise | Learners | Mandatory at the end of a day or module |
| 19 | Rubric | Evaluator, human or automated | Mandatory alongside anything submitted |
| 20 | Extension and remedial task | The spread in the room | Mandatory, built weekly not daily |
| 21 | Corrections card | Learners, opening the next session | Conditional | Anything asserted live turned out wrong |
| 22 | Detailed curriculum | The builder, the trainer, programme staff | Mandatory for any programme of more than one session | |

Never ship a subset without saying which pieces are missing and why.

### 3.2 The deck

**Three readers, and the third sets the standard:** the trainer teaching from it, the learner in the room, and a learner opening it cold a month later with nobody to ask. Build complete for the third reader, then mark the live path in the chat reply and never on a slide.

Structure:

- Sections, each with a complete arc, opening on a section slide that carries the connection diagram with the current part lit, and closing on a numbered step card
- Numbered kickers on every slide, which give navigation for free
- A map slide repeated at each boundary with the current section marked
- Concept slide, then applied slide, as the default pair for every concept
- Every question gets its answer slide immediately: the question, then the claim in a tinted band, then a row per wrong option saying why it does not hold, then a paired mental model
- After every major topic, a summarise-the-steps slide the learner photographs
- Steps written down, numbered and simplified, in every section. This is the single most-repeated correction

Six slide kinds routinely left out:

| Slide | What it carries |
|---|---|
| **Pain open** | The business pain in one line and the question the room can answer with no framework. Opens every topic |
| **Derivation** | The two or three facts that stay true with no tool, and the framework being built out of them rather than presented |
| **Unlock** | What a learner will be able to do that they cannot do now, stated as capability |
| **Anti-pattern** | The cases where this is the wrong choice, shown beside the cases where it is right |
| **Connector** | One mental model tying the parts into a single picture, placed after the parts are taught |
| **Failure** | The wrong path, with its error and the trace it produces |

Sizing: 26 slides was declared right for a two-hour session with rich diagrams. 35 to 45 is fine when many pages are fast reference or worked pages. The augmentation test is that every added slide carries a diagram, a framework or a summary the trainer would otherwise draw live.

### 3.3 The demo code file

Code files carry more than code.

| Section | Content |
|---|---|
| Setup | Install and configuration first, so a beginner runs it unaided. For cloud work, steps for both a local editor and a hosted notebook |
| Recap | What the previous session established |
| Progressive segments | One per deck section, in order, each runnable alone |
| Expected output | What the correct result looks like, printed |
| The wrong path | A deliberately introduced failure, with the error and the trace |
| Reading the trace | How to read what the failure printed |
| Production notes | What changes in production, as post-cell comments |

The deliberate failure is not enrichment. Interviews ask what happens when this breaks and never about the happy path, so the failure path is the part of the file aligned with how the learning gets tested.

**For any Python file expecting interactive input**, append a comment block at the end listing test input cases: happy path, tool routing, follow-ups, the refusal or no-evidence path, guardrail probes and limitation probes, each with what to expect, so the file can be tested directly from itself.

### 3.4 Exercises

Separate markdown file per exercise, dropped at a named point, scoped strictly to what has been taught by then. Locator line, tasks, answers. No learning objectives, no rationale.

**Three sizes, and all three exist:**

| Size | When | Length | Shape |
|---|---|---|---|
| Mid-session | Inside a segment | 10 to 15 minutes, hard cap | Mixed element types in one sequence, guided with nudges |
| Comprehensive scenario | After every two and every four sections | 15 and 25 minutes | Messy real-world brief, learner derives the numbers, chooses which instruments to apply in what order, stakes quantified in minutes and money |
| Capstone | After all sections of a day or module | Long | Agentic-first where the subject allows, every instrument taught that day re-applied to the system itself, minimum subjective writing, maximum decision-making, ending in certification-style practice |

**A one-line prompt with lettered options is a drill, not an exercise.** Fewer and higher quality wins. The two that worked best put the learner inside the real conversation the frameworks exist for: a gate review where they play the reviewer reading a half-finished board, and a cost-cut ultimatum where engineering wants three more months and the learner has to find the two moves that ship this quarter.

**Answer forms:** selection and repair only, never open writing. Answerable as a short letter string pasted into chat, with an explicit "paste your answers as 1c 2a 3b" line, because a PDF is not fillable over a call. On a learner sheet the example answer string must not match the real key.

**The one thing that stays out of exercises.** The transfer answer in slot 10 is spoken, so it never becomes a written exercise item. It belongs in the trainer notes under **Ask**, in the study notes as a model answer, and on the cheat sheet as the crux line. Turning it into a written task breaks the fifteen-minute cap and produces prose nobody marks.

**Types that work:** read a trace and say what it shows, match to a lettered bank with distractors, choose from options, fix deliberately wrong code, identify what is wrong without fixing, fill one blank line, fill one blank function call, sort into buckets, order shuffled cards, fill a table from a diagram, spot the wrong arrow, pick the best fix, is-this-diagram-correct with a deliberately wrong artefact.

**Do not make every exercise the same.** Different section pattern, heading set and answer-block shape per file. Colour-coded task tags for the element mix, and one green nudge line per task that guides without giving the answer.

**Distractor discipline, audited mechanically every time:** no key is the longest option, no key is the most obvious, key positions spread across a, b, c and d. One pass had nine of twelve keys at position b and four keys as the longest option.

**The strongest exercise devices found so far:**

- Plant a row that cannot be scored at all because it is an outcome rather than a task. It teaches the decomposition rule better than any explanation.
- Design the case so the number **fails** the bar, forcing the learner to apply the corrective move rather than confirming a pass.
- The stretch is a one-number variant of the same case, not a new case. Change one figure and ask which single decision moves.

### 3.5 Solution files

One per exercise. High-level explanation, then the answer, then a line-by-line walkthrough of what and why, then runtime or real-world behaviour, then scenarios and production use cases. Include a "why the others fail" column, decision trees, the concept's history with dated sources, and a short reading list.

**[open]** No rule currently exists for when solutions are released to learners. Proposed default: mid-session solutions at the end of the session, take-home solutions at the start of the next session, capstone solutions after the submission deadline.

### 3.6 Excel workbooks

Present them as frameworks created for learners to apply to their own work. Few tabs, all load-bearing, must feel live.

**Two per session, different in kind, which is what stops them being redundant.** Three kinds exist:

| Kind | Shape | Job |
|---|---|---|
| Decision tool | One tab per taught topic, ending in a computed verdict and a paste-ready export | One task, deep |
| Live miniature | Fixed rows of data plus dropdowns, played in the room with a run sheet of scripted moves | One session, live |
| Portfolio sheet | Fifteen rows applied wide across the learner's own backlog, with a counts view | Many tasks, wide |

Design rules that have held:

- **The export tab is the highest-value idea.** Field name in one column, a formula-assembled value in the next, so the brief can never drift from the numbers.
- **The strongest device is a dropdown that flips a design decision** and changes the whole workbook's behaviour.
- **Prompt assembly.** Each prompt cell concatenates the learner's dropdown answers with literal angle-bracket placeholders for the one or two things only they know. Dark cell fill with light text so it reads as a code block.
- **Tune synthetic data so the optimum is interior**, not at an extreme, or the lesson becomes "always minimise".
- Verify by scripting every move, editing a copy, recalculating and asserting the computed verdict strings. This found four real bugs on one pair and a logic bug on another that a clean recalc did not catch.

### 3.7 Interactive activities **[proposed]**

The gap the workbook cannot fill: things needing immediate feedback with no formula literacy, and things that are spatial or temporal rather than tabular.

Use one when the learning move is **trace a flow, step a machine, drag into an order, or move a slider and watch a threshold cross.** Do not use one where a table would do the same work, because a workbook the learner keeps beats a page they close.

Constraints:

- Single self-contained HTML file, no build step, opens from a link or a file
- No browser storage of any kind, since it fails in the delivery surfaces in use
- Works offline and on a phone, because the room will be on phones
- Ends in a state the learner can screenshot and paste into the submission surface
- The same visual system as the deck, so it reads as one programme

### 3.8 The draw sheet **[proposed]**

Currently the instruction to draw lives as prose inside trainer notes, which is not enough for an in-person room where the board is half the teaching.

A draw sheet is a landscape PDF, one page per drawing, carrying:

- The finished drawing at the top, hand-drawn in the sketchbook language, exactly as it should end up on the board
- The **stroke order**, numbered, so the trainer builds it in the same sequence the explanation runs
- The one sentence said at each stroke
- What to leave blank for the room to fill, and the answer
- A photograph-ready version the trainer can hold up if the board goes wrong

Only draw what adds information not already on a slide. Most slides get none. The drawings worth a sheet are the ones where the building of the picture is the teaching, and the ones a trainer will otherwise redraw badly under time pressure.

### 3.9 Cheat sheets

One or more per day or per major topic, as PDF, professional but well explained, landscape concept format by default.

Two modes, and picking the wrong one is what makes a sheet useless.

| Mode | Reader's state | Organised by | Surface |
|---|---|---|---|
| Concept, the default | Learned it once, needs the whole shape back in a minute, and needs to say it out loud | The shape of the idea | Landscape A3 or A4 |
| Lookup | Mid-task, partial recall, needs a forgotten detail in ten seconds | The moment of use | Portrait A4 |

Rules carried from the research: working memory holds five to nine chunks, so cap a concept sheet at six to eight panels and cut rather than shrink the type. The learning benefit is in making the sheet rather than holding it, so every sheet ships as two PDFs from one source, the reference sheet and a fill-it-yourself gap variant with roughly a quarter to a third of cells blanked.

Three panel types, mixed in the proportion the topic needs: **recall** for the exact form, **decide** for a gate or comparison ending in a choice, **diagnose** for symptom, likely cause and first check.

Every concept sheet carries the crux line for each topic it covers, since the sheet's whole job is giving somebody the shape back in a minute so they can say it out loud.

### 3.10 Study notes and pre-reads

Study notes are governed by `study-notes-builder` and always use it. They are built on a terrain map that fills up session by session, one running thread carried through every concept, verified field cases, a no-writing self-check, and an ordered reading path.

**Pre-reads have no skill yet.** **[proposed]** Until one exists, the pre-read is the cheat sheet's gap variant, handed out before, collected from nobody, with the solid sheet handed out after. This resolves the conflict between wanting a pre-read and refusing to teach the concept before the room has seen it applied: a gap sheet primes vocabulary and shape without giving the explanation away.

### 3.11 Trainer material

Trainer notes are a separate file and never live inside the deck. Anything in a deck that speaks to the trainer gets projected onto a wall in front of learners.

Written for a trainer reading them live: glanceable, fixed label order, short lines, findable in under a second.

Per slide, only the labels that apply: **Say**, **Then**, **Draw**, **Ask**, **Trap**, **Do this**, **Bridge**.

Front matter on one screen: a slide-range-to-topic table with minutes, a use-case-per-topic table, the three things that must land, a ranked cut list, and the slides where the question goes back to the room.

The front matter also carries the **continuity block** copied from this session's row in the detailed curriculum: covered before and at what depth, do not re-teach, the spine case and its current state, fresh cases, case studies with dated sources, first-use tools, the basics budget, and where each idea returns. This is the first thing a trainer reads in their ninety minutes, and its absence is why a trainer opens the material and does not know where to start.

**Say** must be quotable sentences carrying a specific, true, non-obvious detail, and it always starts with use cases.

---

## 4. The unit: how one concept gets taught

Several concept rhythms have accumulated. They are not alternatives and treating them as a menu is what makes output read assembled. **[proposed]** The resolution: one canonical unit, two sanctioned variants, and a device library that plugs into named slots.

The unit runs the same way for every topic, in every subject, with no exceptions for topics that seem too simple or too advanced to need it. A topic that skips the opening pain lands as trivia. A topic that skips the derivation lands as a rule to obey. A topic that skips the closing line lands as something the learner covered and cannot use.

### 4.1 The full unit, the default for every major concept

| Slot | Content |
|---|---|
| 1 The pain | A business pain the room already recognises, in one sentence, stated in money, in minutes or in somebody's frustration, never as a technical absence. Then one thought-provoking question they can answer from ordinary work experience |
| 2 Ground it | What the topic is, where it is used, what the context is, why **this** audience needs it, where it lands in their own lifecycle |
| 3 Strip it to first principles | The two or three facts that stay true with no tool and no vendor, then the question: given only these, what would you build? The room proposes, and the trainer converges on the real design |
| 4 The clearest example | Simple, relatable, instantly picturable. Does not have to use the central case |
| 5 The framework or formula | Derived from slot 3 rather than handed over. Invented if needed, simplified. A division, a count, a 2x2, a quadrant or a plug-in strip. Never algebra, never letters over letters |
| 6 The steps | One at a time, numbered, with the sub-steps of any step still vague |
| 7 One worked example | Through the steps, slightly simple, showing the working and not only the result |
| 8 Apply to the central case | The established world, with the real numbers |
| 9 The gotcha | The failure, the edge, the thing that breaks it |
| 10 Close | The crux in one sayable line, the whole method as a numbered strip the learner photographs, and the transfer question with its sixty-second answer |

Slots 4 and 8 are the two-examples rule made concrete: the clearest example teaches the concept, the connected example proves it lands in their world.

Slots 1, 3 and 10 are the three that get dropped under time pressure, and they are the three that decide whether the learner can use the topic. Slot 1 makes the rest feel necessary rather than arbitrary. Slot 3 makes the framework theirs. Slot 10 is the only part that survives a year.

Not every slot needs a slide. Slot 1 can be a lead line and a spoken question, slot 3 can be one diagram and ninety seconds of discussion, and slot 10 is one card. Ten slots is a sequence to run, not ten pages to fill.

### 4.2 The opening pain

The pain point is the most-skipped and cheapest fix in the whole unit. Three tests: it is stated in the room's own job rather than the subject's vocabulary, it names a consequence rather than a gap, and someone in the room has lived it.

| Weak open | Strong open |
|---|---|
| Models cannot access private data | Your support team answers the same eleven questions forty times a day, and the answers sit in a wiki nobody opens |
| Story splitting matters for agile teams | Two engineers estimate the same story. One says three days, the other says three weeks. Neither of them is wrong |
| Availability is important in cloud architecture | The on-sale opens at ten, the site is down at 10:04, and nobody can tell you which of the nine services caused it |
| Evaluation is a key part of the agentic lifecycle | It passed every test you wrote, went live on Monday, and by Thursday it had quietly refunded four hundred people |

Follow the pain with one question the room can answer with no framework at all. The question is a teaching device wearing a question's clothes, and its answer is the topic. Three forms that work: what would you do if, which of these could you write down as instructions somebody would follow perfectly, and two people give you numbers three times apart so who is wrong.

### 4.3 First principles, six moves

Deriving beats presenting. These are the moves that turn a framework the trainer owns into one the learner owns, and they are what makes application intuitive rather than procedural. Pick one or two per topic, never all six.

| Move | The prompt | Worked |
|---|---|---|
| **Strip it** | What is true here regardless of tool, vendor or framework? | Retrieval rests on three facts: the model has never seen your documents, a context window is finite, and finding the right passage is a search problem. Everything else is engineering on top of those three |
| **Rebuild it** | Given only those facts, what would you build before lunch? | The room proposes chunking, an index and a top-k cut, and the reference architecture then arrives as the thing they almost invented |
| **Derive the number** | Why does the formula have that shape? | One wrong answer costs $32 and one right answer saves $8, so four rights pay for one wrong, so you can afford one wrong in five, which is 80%. The formula becomes obvious rather than memorised |
| **Why this shape** | What constraint forced this artefact to look like this? | A story file carries eight fields because eight separate decisions had to land somewhere and nowhere else would hold them |
| **Remove the tool** | If this framework disappeared tomorrow, what would you still have to build? | Separates the durable idea from the vendor's packaging, and it is what keeps a curriculum alive when the stack turns over inside a year |
| **Flip the decision** | What would have to be true for the opposite choice to be right? | A rule the learner can invert is a rule they own. A rule they cannot invert is one they will apply in the wrong place |

Two failure modes to avoid. Do not run first principles on a concept the room has not seen working yet, because there is nothing to strip. Do not let the rebuild run open-ended: ask the question, take three answers, converge, and move, inside five minutes.

### 4.4 The grammar variant

For anything with a grammar: syntax, a template, a document structure, a decision procedure, a canvas. Replace slots 4 to 7 with:

- **Skeleton before instance.** The abstract shape with placeholders, then its parts numbered and explained
- **How the machine processes it**, plus one usable consequence of that order
- **A ladder of five to seven examples.** Single, then multiple, then computed, then the computed thing named, then a different data type, then the edge case. One new idea per rung, and **every rung prints the real output** rather than describing it

### 4.5 The short unit

For a minor concept that does not deserve ten slots. Fifty to ninety seconds. If it needs longer it is two concepts.

1. A plain one-line definition
2. A concrete contrast with real values
3. What you do about it, which is the beat usually missing and the one that makes the concept the audience's rather than the trainer's
4. A sticky handle

### 4.6 The sizing test

A unit is sized right when this sentence completes without an "and": *after this unit a learner can decide X, which they could not decide before.* Size units by decision, never by term. Byte-sizing a judgement subject by term produces well-formatted trivia.

### 4.7 The device library

Devices attach inside slots. Pick the ones the concept needs, never all of them.

| Device | Slot | What it does |
|---|---|---|
| What it says against what it actually means | 1 | Take a thing they already see and reveal what is under it |
| War story with a number | 1 or 8 | One real consequence, quantified |
| One real artefact decoded | 2 | Hang every concept off a sheet the learner actually holds |
| Nesting | 2 | A is the umbrella, B is the toolkit inside it, C is one tool, and your job is picking the right tool |
| Remove the tool | 3 or 10 | Separates the durable idea from the vendor that packaged it |
| Card per category, same shape | 5 | Instantly comparable |
| Decision rule with a threshold | 5 | Never "it depends" with no rule |
| Derive the number | 5 | Arrive at the formula by counting, so nobody has to memorise it |
| Read the decision tree in words | 6 | Full if-then sentences on their own slide, walking every row |
| Reuse an earlier framework | 8 | Plot the new thing onto a 2x2 already taught, rather than inventing a new picture |
| Paired mental model | 9 or 10 | Two contrasting halves of one sentence |
| Diagnostic footer | 10 | Hands the learner a line to say. They leave with words in their mouth |
| Colour carries meaning | any | The learner reads the colour and knows the category |
| Established framework, marked as such | any | Reassures a senior room that the set is not invented bureaucracy |

### 4.8 The spiral: same data, new tool

The strongest device for a programme teaching several tools over one problem space. Hold the data constant, change the instrument. At each turn the learner already knows what the answer should look like, so all attention goes to the new tool, and the moment the old tool runs out is the argument for the new one.

Three properties, all easy to lose:

- The data is recognisably **the same records**, not a similar dataset. Recognition is the mechanism
- Every turn shows **one thing the previous instrument could not do**, or the new tool looks like a syntax change
- Say the spiral out loud once near the start, so learners stop treating each module as a fresh start

The non-obvious payoff: when trainers change every two weeks, shared data is the only continuity that survives a handover, and it survives only if it lives in the content rather than in a trainer's head. That turns a pedagogy choice into a staffing control.

### 4.9 The witness rule

Before writing any case data, list every teaching point, then plant one feature in the data that **only** that point explains. Without the witness, the slide produces output identical to the one before it and the learner sees nothing.

Build it as a matrix: teaching points as rows, case-data features as columns. An empty row is a point with no witness. An empty column is detail to delete. A heavily marked column is load-bearing and must not be edited casually.

Keep case data small enough to hand-check. Seven rows beats seven hundred, because a learner who can verify the claim starts trusting the material. Make every table self-checkable by hand: show every term or drop the small ones and say so.

Tune case numbers so answers land on memorable anchors. Damages of $8, $32 and $152 against an $8 saving give ratios of 1, 4 and 19 and therefore exactly 50%, 80% and 95%.

### 4.10 Questions and quizzes

- Starter quiz of three or four questions in the first five minutes, **answerable from ordinary work experience**, never from a framework not yet taught, or they produce silence rather than discussion
- Every wrong option is a real thing the room recognises, so the reveal teaches four things at once. The question is a teaching device wearing a question's clothes
- Question variety, one per page: multiple choice, true or false with two large lettered buttons, is-this-diagram-correct with a deliberately wrong artefact
- Remote-friendly answer forms: type A, B or C in the chat, type Y or N. A question the room can answer with one keystroke is the one that gets answered
- The fix that worked: "a new colleague joins Monday, which of these could you write down as instructions they would follow perfectly?" replaced "which of these needs an agent?". Same taxonomy, no jargon, and the reveal defines the whole thing

### 4.11 The recall spine

Four cheap devices that make a course feel like one thing:

1. Linear position: numbered kicker plus a map slide at each boundary
2. The whole family in view: the map repeated with the current section marked
3. **Backward hooks** naming the earlier unit at every reuse. Highest value, most often missed, and they cost four words
4. Forward hooks naming the decision the next section answers

Per-**unit** feedback, not per-course. Course-level feedback says the course was fine. Unit-level feedback says which unit to rebuild.

### 4.12 The transfer layer

Slot 10 exists because the room's real test is not the exercise. In a placement programme it is an interview. In a certification programme it is the exam. In a client programme it is the moment a stakeholder asks why this and not that. All three are the same shape: say the crux out loud, defend the choice, survive two follow-ups.

Every topic carries three things, built at the same time as the rest of the unit.

| Piece | Specification |
|---|---|
| **The crux line** | One sentence, plain words, that stays true after the framework name is forgotten. It goes on the closing card, on the cheat sheet, and in the study notes |
| **The transfer question** | The question this topic actually gets asked as, in the room's own world. An interview question for a placement cohort, an exam-style item for a certification module, a stakeholder challenge for a client programme |
| **The two follow-ups** | Interviewers go three questions deep, and a learner who answers level one and not level two sounds shallow. The two that recur: why did you choose this over the obvious alternative, and what happens when it breaks |

The sixty-second answer to the transfer question gets written out as a model answer. It lives in the study notes and in the trainer notes under **Ask**, never as a written exercise, because the answer is spoken and the exercise rules are selection-only for good reasons.

Three sources already in the unit feed the answer with no extra work: the first-principles strip gives the "why this exists" opening, the decision rule with its threshold gives the trade-off, and the gotcha gives "what happens when it breaks". A topic whose transfer answer cannot be assembled from those three has a hole in one of the three.

---

## 5. Visual system

### 5.1 Which palette

| Palette | Use when | Values |
|---|---|---|
| **Sketchbook** (current premium standard) | Any deck that should feel premium and hand-made rather than corporate | Graphite ink 1F1B16 on aged paper F5F1E8, drafting blue 2D5F7C, burnt sienna C15A3F for the risky or costly parts, muted pine 3F7355 for shippable or correct, sepia 8A7355 for margin notes |
| **SAP Activate multi-colour** | Colour must carry category meaning and the learner reads the colour to know the category | White ground, ink 1F2937; sage green 5C7A52 mandatory, terracotta B8763A conditional or cost, purple 5B4889 optional, blue 3F6B8A tooling, red C0392B critical |
| **Warm sand monochrome** | Colour would be decorative | Ground FBF7F0, ink 2B2620, teal 1E6B7A accent, terracotta B4623A for cost or wrong |

Two palettes are rejected as defaults everyone recognises: amber-and-slate, and plain white with navy.

### 5.2 The sketchbook language

A staff engineer's grid-paper notebook. Hand-drawn boxes with seeded jitter on stroke paths so they are stably irregular. Pen-style curved arrows with drawn arrowheads. Circled hand-drawn step numbers. Hand-lettered section titles via a drawn double-underline stroke. A faint engineering grid on every slide. Dark grid-paper cover, section and closer slides.

The **step card** is the fix for steps never being written down: a titled card of up to six circled hand-drawn numbers connected by a dotted thread, each with a bold head and a one-line explanation. It closes every section and gives the whole-day recall.

### 5.3 Rules that apply to any palette

- **Accent is ink, not wallpaper.** Across 75 reference slides the accent appeared as text 331 times and as a fill 24 times. Flooding table rows and putting a tinted band on every slide is what "obnoxious palette" meant. The hues were never the problem
- Banned: bordered tables, coloured table row fills, more than one tinted band per slide, red or green as fills
- Content occupies the top three quarters. Bottom whitespace is correct and should not be filled
- Greys carry the hierarchy that colour should not be doing
- **Be incremental across slides, not within one.** A five-row table becomes three slides with the same picture growing
- Cohesion comes from **one connection diagram, repeated**: at the front, at each part opener with the current box lit, and at the close with the values filled in
- Diagram labels on a curve sit outside the whole figure at a constant radius with leader lines back to the arc

### 5.4 Register to avoid

The tells that mark a design as templated: tracked-out all-caps eyebrows, meta strings joined with middle dots, tinted near-black, mono data labels, identical rounded cards, generic stock imagery, decorative diagrams. Read `/mnt/skills/public/frontend-design/SKILL.md` before any styling work.

No childish visual register. No cute conceit at the audience's expense.

---

## 6. Language

### 6.1 The sentence rule

Full, complete, coherent, connected human sentences, in every deliverable including planning documents, inside tables and inside callouts. No clipped fragments, no punchy half-sentences, no telegraphic slogan lines. Bullets are fine, and each bullet is a real sentence. The audience is senior and talented, and fragment-style copy reads as offensive to them.

The one sanctioned exception: on a scan surface such as a cheat sheet, table cells and syntax lines are legitimately noun phrases, while every prose line, every judgement column and every trap stays a full sentence, because judgement compressed into a fragment stops transferring.

### 6.2 Headings and leads

**Headings name the topic. The assertion goes in the lead line.** A heading must work as a contents entry and as a recall handle a month later. "The six components of an agent" is a heading. "Six components, no more, no less" is a slogan that tells a learner nothing about what the six are components of.

Rename any heading that gestures rather than names.

### 6.3 Banned and watched

- Banned words: Additionally, Moreover, However, Hence, Thus, Nonetheless, Furthermore, Accordingly, Indeed, Dynamic
- Zero em-dashes. They enter build source as escape sequences, so a literal scan reports zero while the rendered file still shows them. Scan both forms and verify the rendered output
- Register words that get a deck rejected: delve, tapestry, seamless, holistic, myriad, leverage as a verb
- LLM tics that have caused rejections: the antithesis construction, fragment stacking, a repeated bolded label used more than twice, hedge openers, closing slogans, triads
- Avoid words awkward to say aloud. "Rung" was stumbled on live and replaced with "build"
- Plain self-decoding words before formal terms. Introduce the formal term after the learner has seen the problem that needs it
- Read every coined label back for the other meaning a senior reader could take

### 6.4 Zero meta-content

No facilitation instructions, no deck self-reference, no pedagogical scaffolding shown to learners, no design rationale, no programme framing such as agendas, learning objectives or recaps. Teaching intent stays invisible: write "answer this question", never "answer this because it is the point of the task".

Allowed: a title-slide promise, learner-facing activity instructions, a duration, a page identifier.

Bridges and the apex are **not** meta-content and are required: the one question the artifact answers stated at the top, the flow named in plain words before descending, and a content bridge into and out of each part.

Title and opening slides carry no meta framing. No "Day 1 covered X, today covers Y". Just the title, the promise and the sub-pointers.

### 6.5 Terminology

**Verify the client's taxonomy before teaching it.** Framework labels collide. One reference document mapped P0 to P3 onto architectural layers while the client's own swimlane and the delivered Day 1 both defined P0 to P3 as lifecycle phases. Same labels, two different frameworks.

Never blend two sources using the same labels differently. Check the client artefact and the delivery transcript first, teach their definition, and where the second framework is genuinely useful introduce it as a separate axis threading through the phases.

Cap new vocabulary hard. Reuse the frameworks and cases the audience already has before inventing a parallel set. A new named device has to remove confusion rather than merely exist, and its name should decode itself.

---

## 7. The room

### 7.1 Grounding moves, applied live

- **Ground the new thing in the first three minutes.** In one delivery the room did not know the framework the whole session hung on, so it had to be taught at minute one from scratch even though the deck had it at slide 41
- Every "this is hard" gets a "here is why" on the same slide
- Every "where does this go" gets a home slide naming which artefact each consideration lives in
- Scenarios state their objective. A room cannot rank six options without being told what the person is optimising for
- Always ask what the room does not know before building. A sponsor interrupted at minute five to say a core framework was unfamiliar, and the room also did not know two other assumed concepts
- Open every topic on the pain and the question, not on the topic name. A room that has not felt the problem treats the solution as trivia
- Run the derivation out loud. Ask what would have to be true, take three answers, converge in under five minutes, and let the framework arrive as the thing they nearly said. The room defends a framework it helped build and forgets one it was handed

### 7.2 Teachability beats rigour for a first-exposure room

If it cannot be taught in ninety seconds with a 2x2 or one formula, that is not the session version. Keep the rigorous one as an appendix. One scoring framework was abandoned live and replaced with a hand-drawn value-by-complexity 2x2, which worked better.

### 7.3 Timing discipline

- Starter quiz in the first five minutes
- One activity roughly every 45 minutes of a full day, or every 20 to 30 minutes in a dense session
- Mid-session exercise capped at 15 minutes
- **Activities run to a hard seven-minute timer.** A five-minute activity ran 22 minutes and ate the close
- Build rich and cut live. State the ranked cut list in the chat reply

### 7.4 The spoken register

First person, "you guys", "honestly", "I'll be candid with you", plain spoken sentences, and a number in almost every claim.

Patterns that work in front of a room:

- **Own the fact before the fix, and never debate it.** "Things have slowed down, it's fact, we're not debating that." "I'll be honest, dilution happened." "I take that on myself"
- **Show the artifact instead of asserting.** Share the curriculum on screen, grade what is done and not done plainly, anchor claims with a dated concrete
- **Turn a complaint into a design question**, and ask about structure rather than topics. "More than the topics, how do you want these sessions driven?"
- **State the constraint as a market fact, then the workaround with a mechanism.** Practitioners have no bandwidth for notebooks, so architecture on Monday, build individually, random review picks
- **Segment people by behaviour, not seniority.** Doers against managers and talkers, no point mixing
- **Take a learner's idea live and attach its condition.** "It's a good idea, I'll make a note, but it depends on consent"
- **Say the metric out loud with numbers and disclaim the marketing use**, and pair it with the honest alternate metric
- **Close with a dated follow-up and an open door**

### 7.5 The trainer contract

The trainer is the largest uncontrolled variable in a cohort programme, and seniority does not reduce the variance. A trainer from a famous employer with no supplied structure still produced a bad rating. A strong interview predicts almost nothing.

```
Session length              6 hours
Fixed content supplied      4 hours, taught as given
Trainer's own material      1.5 to 2 hours, free to innovate
```

State it in hours, in the kit. The fixed core exists because rigour disappears without it and because industrial examples and scenarios are not something every trainer carries. The free third exists because a trainer forced to read someone else's material for six hours delivers it badly.

A trainer preferring their own examples is reasonable, and it gets bounded rather than refused: their examples go in the free third, and the fixed core keeps the connected scenario intact so the next trainer picks up a thread that is still there.

Expected preparation is ninety minutes with the material before the session, with doubts raised in advance. That is a request a trainer can actually meet, unlike "prepare well".

### 7.6 Moves that compound

The moves that make the effort compound rather than repeat.

| Move | Why it pays |
|---|---|
| The fixed core is a **measurement instrument**, not a compliance rule | It converts a vague quality problem into a completion percentage, and it removes the "nothing was supplied" defence |
| The delivered deck becomes the base, not the source | When a trainer has added live material that worked, extend the delivered file by splicing rather than rebuilding from the original |
| Build rich, cut live | Cutting is cheap in the room and building is expensive the night before |
| Reuse the cohort's own case by default | A fresh domain is a real cost, worth paying only when transfer practice is the goal |
| Bring in one established framework per invented one | It reassures a senior room that the constructions are not invented bureaucracy |
| Name a framework so it decodes itself | Litmus test, go or no-go, decision matrix. The name does the recall work |
| Company-named cases with a disclaimer | Real names carry weight and no association is needed |
| The deliberate failure aligns with assessment | Interviews test the break, so the failure path is the part that transfers to a job |
| Place build weeks in the plan at the start | Retrofitting one after the backlog appears means the backlog has already broken the schedule |
| Feed the transcript back | Free quality assurance, per-learner analytics, and the engagement signal from audio |

### 7.7 Two kinds of week

**Teaching week.** Module to module, the artifact set above, one concept spine.

**Build week, every third week.** Three jobs at once, and the first is the one nobody plans for:

1. It **absorbs the backlog**. Teaching always runs behind by the third week. Five days means three or four on the project and one held back for whatever slipped
2. It runs a **complex scenario** rather than a handed-over project, and real data belongs here because no concept is being taught for the first time
3. The **trainer builds it live**, solving part in the open, setting the next piece, discussing it the next day. The last day or two, learners extend the scenario themselves

---

## 8. Engineering and verification

### 8.1 Instrument the builder

Wrap every element helper to record its bounding box, then check pairwise overlap, past-footer and past-right. This found 21 real collisions on one deck that looked fine in thumbnails.

Defects the geometry audit cannot see, so still render and look: linear bar scales hiding small values beside a large one, negative bar labels colliding with axis labels, long titles wrapping into the lead, a diagonal arrow crossing 2x2 cell labels, an arrow routed between two boxes striking a third box's subtitle.

### 8.2 Known bugs worth checking every time

| Tool | Bug |
|---|---|
| pptxgenjs | `rowH` applies to the header row too, so table height is `rowH x (data rows + 1)`. The single biggest cause of overflow |
| Title length | Georgia bold 25pt over a 12.1 inch column wraps at about 58 characters, and a wrapped title collides with the kicker. Put a guard in the builder and verify it fires |
| reportlab | A table row with more cells than colWidths silently adds an overflowing column. colWidths summing beyond the text column throws an unhelpful NoneType error deep inside layout |
| openpyxl | Form-control checkboxes are unreliable, so use Yes/No data validation. Annotation cells whose text starts with an equals sign are read as formulas and error on recalc |
| Excel | Avoid XLOOKUP and bare IFS in LibreOffice. Recalculate and assert the computed verdicts, not merely the absence of errors |
| SVG through sharp | Marker-end arrowheads do not render on line elements even though they render on path arcs. Draw arrowheads explicitly as a path |
| Landscape PDF | Page CSS `@page { size: A4 landscape }` plus `landscape: true` in the PDF call. Diagrams must be authored wide or they overflow and force extra pages |
| Diagram scaling | A full-width diagram shrunk into a half-slide column drops text to about 3pt. Author a compact variant at that viewBox width instead |

### 8.3 The audits to run before shipping

1. Em-dash scan on both the literal character and the escape sequence, on source **and** rendered output
2. Banned-word scan
3. LLM tic scan
4. Distractor audit: no key longest, key positions spread
5. Geometry audit with a rendered visual pass
6. Excel: script every dropdown combination, not only the ones the run sheet uses. On one workbook this surfaced that the plain workflow build beat the best agentic setting, a restraint lesson stronger than the one designed in
7. Parity: deck, code and exercises in the same segments in the same order
8. Witness matrix: no empty rows

### 8.4 Fact-checking

Brutal real-time fact-checking of technical claims is wanted, not tolerated. Facts cited by product name are verified **before** the session, not after.

Four grades to use when checking claims made live: right, loose, invented-but-sound, wrong. Invented-but-sound claims are kept and the false attribution is dropped, presented as the trainer's own construction. Wrong claims get a corrections card at the front of the next session, as a slide and not an apology.

Anything framework-specific carries a verification date, because the vocabulary in this area turns over inside a year.

### 8.5 What gets caught without being asked

Gaps expected to be caught with no prompting: no chart where a proportion is the point, formulas discussed but never shown, a needed figure left out, and no audit of what each slide and the whole deck is worth once built. Skills exist so these get applied automatically, and not applying them is the failure.

**Audit the build afterwards and show it:** per slide what it is worth and whether it survives a cut, and for the whole deck what a reader gains. Its absence is treated as the work being unfinished.

---

## 9. The loop after delivery

Feed the session recording or transcript back and produce:

- **The delivery-reality numbers.** How many slides were reached, how many minutes of content were not on any slide, which activities overran, which questions repeated
- **The gap table**, anchored to evidence with timestamps
- **The fact-check** of claims made live, graded four ways
- **The prior-knowledge misses**, meaning every point where the room did not know something the build assumed
- **The improvised content that worked**, which gets scripted into the next version
- **The recoverable-assets call**: what to keep, what to repair, what to demote to take-home, what to retire

With audio rather than text there is also an engagement signal about which stretch the room was alive for.

A measured example of what this produces: about 35 of 49 slides reached, about 28 minutes of content not on any slide (all of it asked for by the room), one live replacement that beat the scripted version, two repeated questions and two prior-knowledge misses. Seven gap-fill slides were spliced into the next version from that single measurement.

---

## 10. Blind spots

Named honestly, with the call to make. These are gaps in the current system rather than rules already in force.

| # | Gap | The call **[proposed]** |
|---|---|---|
| 1 | `cheat-sheet-builder` is a standing rule in preferences but is not installed | Upload it before the next session, or the rule cannot fire |
| 2 | No pre-read artifact spec exists | Use the cheat sheet gap variant as the pre-read until a skill exists |
| 3 | The in-person room breaks two visual rules. Body text at 9 to 12pt and footers at 7.5pt are unreadable from the back rows, and the multi-colour palette collapses when a handout is printed in greyscale | Author an in-person variant: minimum 14pt body, and make every colour-coded category also carry a shape or a label so greyscale survives |
| 4 | The board has no artifact. "Diagrams to draw" is prose inside trainer notes | Build the draw sheet in 3.8 for every in-person day |
| 5 | Parity between deck, code and exercises is a stated rule that is never mechanically checked | Add a parity manifest listing segment, slide range, code section and exercise, and assert it in the build |
| 6 | Content handed to a trainer has no version stamp or changelog, so the delivered percentage cannot be measured against a moving target | Stamp every kit with a version and a lock date, and freeze 48 hours before the session |
| 7 | Rubrics are not in the artifact set even though submissions are evaluated automatically against them | Build the rubric with the exercise, never after, because an exercise whose rubric does not yet exist has not been designed |
| 8 | Solutions have no release rule | Adopt the default in 3.5 |
| 9 | The room is bimodal and the deck has one path. Extension and remedial tasks exist weekly but the session itself does not branch | Mark two or three slides per section as the depth layer for the confident half, delivered as a variant and never as a parallel track |
| 10 | A trainer with ninety minutes of preparation has no minimum-viable-run version | The trainer notes front matter now carries two halves: the continuity block from the detailed curriculum (where we are) and the run sheet (the three things that must land, the six slides that carry them, the cut order) |
| 11 | Interactive activities were asked for and had no spec | Adopt 3.7 |
| 12 | Nothing marks which artifacts are learner-facing against internal, which matters because of the zero-meta rule and the branding rules | Put the audience in the file name or a header line on every artifact |
| 13 | Feedback is collected per course, not per unit | Two questions at the end of each unit, since course-level feedback says the course was fine and unit-level feedback says which unit to rebuild |
| 14 | **[open]** Whether weekly assessments continue alongside build weeks | If a build week ends in an assessment, the trainer-builds-live model breaks, because learners optimise for the assessment instead of the exploration. Decide before the day-wise plan goes on the portal |

---

## Appendix A. Ship check

Run every item. Report the result, including the ones that failed and were fixed.

**The gates**

1. Is the envelope stated, with the arithmetic done?
2. Is the reference named and locked, one written and one video?
3. Does the strategy brief exist as one screen, and does it name the learner's own question?
4. Is the world established as its own artifact, and is it the same world as last session?
5. Is the map readable in three minutes?
6. Are prerequisites listed, including every first-use tool?
7. Is any tool used for the first time inside a session that also teaches a concept?
8. Is the concept taught on clean engineered data rather than a real dataset?
9. Does the session row exist, with ideas counted as decision sentences and four or fewer per two-hour block?
10. Does every sub-topic carry a depth target, with no first encounter above level two and every revisit rising?
11. Was the reference pack researched and verified before the ladder was fixed, with a checked date on every slot?
12. Does the continuity block exist with all eight lines, and is the basics budget fifteen minutes or under?

**Every topic, with no exceptions**

13. Does every topic open on a business pain stated in money, minutes or frustration, and never on a technical absence?
14. Does every topic carry one question answerable from ordinary work experience before any framework arrives?
15. Is every framework or formula derived rather than handed over, with the facts it rests on named?
16. Does every major concept follow the full unit, and are slots 1, 3 and 10 present rather than dropped for time?
17. Does every topic end in one crux line a learner can say out loud with no slide?
18. Does every topic carry its transfer question, the sixty-second answer, and the two follow-ups?
19. Can the transfer answer be assembled from the strip, the decision rule and the gotcha? If not, one of the three has a hole
20. Does every concept have both the clearest example and the connected one?
21. Does every teaching point have a witness in the case data?
22. Are the steps written down, numbered and simplified, in every section?

**Production**

23. Would a reader understand the majority of pages with the text removed?
24. Does every question have its answer immediately after it?
25. Do the deck, the code file and the exercises follow the same segment order?
26. Does the code file open with setup and contain a deliberate failure with its trace?
27. Is every mid-session exercise doable in fifteen minutes by selection or repair, with the spoken transfer answer kept out of it?
28. Do the trainer notes exist separately with nothing addressed to the trainer left in the deck?
29. Do the extension and remedial tasks exist before the day?
30. Are invented frameworks marked as constructions and established ones marked as established?
31. Em-dashes, banned words and tics scanned on source and rendered output?
32. Distractor audit passed?
33. Geometry audit passed, with a rendered visual pass?
34. Is the delivery path and ranked cut list in the chat reply rather than on a slide?
35. Is every sentence in the artifact a complete sentence?

## Appendix B. The four prompts

Once the spine is fixed, four prompts make a day, output in markdown. What makes this work is not the model. It is that the reference, the world and the prerequisites were settled first.

1. The deck
2. All the code
3. All the exercises
4. All the activities

Everything upstream of these four is the work. The four themselves are mechanical.

One line belongs in each of the four, because it is the thing most often lost between a good spine and a mediocre build: *run the full unit for every topic, opening on the business pain and the question, deriving each framework from first principles rather than presenting it, and closing on the crux line with its transfer question and two follow-ups.*

## Appendix C. Verified assets worth reusing

Reuse before inventing. All arithmetic below has been verified.

**SkyWays Booking, flight change.** 500,000 bookings a month, 6% ask to change, 60% self-serve, 12,000 reach an agent at $8 for 15 minutes, giving $96,000 a month. Cost per attempt $0.20, of which retries are 47%. Coverage optimum at 50%, giving $5.60 a case against $8.00, with 90% coverage costing $10.00.

**The mishandled bag.** 2,000,000 bags a month, 0.6% mishandled, 55% auto-resolve, 5,400 reach an agent at $10 for 20 minutes, giving $54,000 a month. Damage $40 gives a ratio of 4 and a bar of 80%. A hold cuts damage to $15, a ratio of 1.5 and a bar of 60%. The case is deliberately set at 76% accuracy against an 80% bar, so it clears only once the hold is applied.

**The 1-in-N test.** Rights per wrong equals damage divided by saving. The bar is one wrong affordable in that many plus one. This replaces a break-even accuracy formula and lands within half a point of the algebra.

**The 100-case count.** Replaces a three-term gated-cost formula with a count out of a hundred and no formula on the slide.

**Invented instruments already taught and available for reuse**, all marked in their materials as course constructions: the Chain Multiplier, Weakest-Link Strip, Nine-Buyer, Blast Radius Fraction, Storm Multiplier, Undo Test, Strain Index, Runaway Ratio, Retry Ladder, Brake Menu, Split Test, the ten-step Availability Review, and PATHS for story splitting.

**Established frameworks that fit and reassure a senior room**, always marked as established: arc42 for architecture documentation structure, RACI for artefact ownership, SPIDR for classical story splitting, INVEST for story quality.

# DAY PACK METHOD
## How one training day's artifacts get produced, Cohort 2

This file is project knowledge. It supersedes `03_Day_Pack_Spec.md` where the two disagree, and it is the written form of the approach the `day-pack-builder` skill executes. The skill carries the procedure; this file carries the reasons and the changes.

---

## 1. The teaching method the pack serves

**Mental model first, spiral always.** Every topic opens by forming the mental model in the learner's mind, walks the whole pipeline shallow in one connected story, and deepens only on revisit. The canonical example, kept because the team teaches from it:

Explaining an LLM starts from an experience everyone has had (type a prompt, get a response, the same felt shape as hitting a URL and getting a page). The pipeline is then walked end to end at one shallow level: the model cannot read the sentence whole, so it breaks it into tokens, with one intuitive beat on what a token is and that tokenization varies by language; each token becomes an embedding, with one beat on why numbers at all; position gets injected, with the same-word-different-sentence example; meaning lives as nearness in vector space, pictured first as 2D coordinates and then grown to thousands of dimensions (GPT-3's embedding width was 12,288; the number often misquoted as "12,000 parameters" is the embedding dimension, since parameters run to billions); then inference emits the next token one at a time, shaped by temperature, top-k and top-p. No stop goes too deep, every stop gets its own deeper day later, and the connections are said aloud.

Cognitive load is the design constraint throughout: at most four new ideas per two-hour block, counted as decision sentences. The builder thinks as a trainer, a psychologist and a storyteller at once, and when time pressure bites, breadth is cut before the worked example is.

## 2. What one day ships

| # | Artifact | Audience | Count | Core rule |
|---|---|---|---|---|
| 1 | Deck | STUDENT-visible | 1, or a half-one and half-two pair | Split only when the day carries two distinct arcs, never to hide an over-full day. Visual, thin, spiral-ordered, crux line on the last card. |
| 2 | Demo notebooks | STUDENT | 1 or more | Rich teaching documents: idea, diagram, demo, output, deliberate failure with exact trace, fix, plus an industry example and an interview question at each milestone. Progressive variations, one new element per section (the agent-loop ladder is the canonical shape: by hand, one tool, many tools, one turn, many turns). Runs cold in a fresh Codespace. |
| 3 | Activity | STUDENT | 0 or 1 | Only when the topic has a decision, a comparison or a hidden state. Single-file HTML (no storage, no API key) or an Excel template with dropdowns. Toggle-driven, minimal typing, ends in a screenshot-worthy state, doubles as a takeaway decision tool. |
| 4 | Guided + unguided exercises | STUDENT | Few | Think-heavy, type-light: selection, prediction, repair, short computation. Unguided runs in a break or the second half; solution at close. |
| 5 | Solutions | STUDENT | 1 per exercise | Unguided solutions at close; take-home solutions open the next session, which begins by walking one. |
| 6 | Take-home | STUDENT | 1 | Substantial and shortcut-resistant (section 3). Ships with a self-check spine of planted checkpoints so the learner verifies themselves before class does. |
| 7 | Kahoot pack | STUDENT | 1 | Six to eight items per the row's quiz plan plus the return question one level up. Ungraded, an indicator. Distractor audit mandatory. |
| 8 | Trainer notes + day sheet | TRAINER | 1 | The two-minute continuity block, per-slide labels, the breaks with exact error text, the ranked cut list, the checkpoints. Never reaches students. |
| 9 | Study notes | STUDENT | 1 | Written once the session's shape is fixed and revised against the day's transcript when it arrives. The transcript revision is a standing step. |
| 10 | Cheat sheets | STUDENT | 0 to n | One per major topic when the day earns it; landscape concept format plus a gap variant. |
| 11 | Pre-read + setup | STUDENT | 1, ships tonight | Tomorrow's vocabulary as a gap sheet plus tonight's setup. Hard rule, no exceptions. |
| 12 | Tiered extras | STUDENT | 1 pair | Stretch and recovery, built in advance, weekly build allowed. |
| 13 | Corrections card | STUDENT | Conditional | Whenever a live claim proved wrong: claim, correction, source, as a slide. |

Weekly addition on regular weeks: the Saturday recap paper, built from the week's question-set row, pen and paper, AI-free, about two hours, short-answer so peers cross-evaluate, with the Academic TA's discussion guide. It ships in `content/W{ww}/SAT/` rather than a numbered day folder, since Saturday is not a teaching day. Build weeks swap the manifest for the build-week pack (five sub-problem briefs at three groups each, assessor rubric, GD prompts for the expert's Friday and Saturday, the parallel build, checkpoints, scoring sheet, catch-up plan).

## 3. Shortcut resistance for take-homes

A take-home that a chat assistant can complete from its brief teaches prompt-pasting. Every take-home applies at least two of these patterns:

1. The deliverable includes process evidence: challenges-log entries, a run comparison of two named tools, a screenshot of an exploration step.
2. The task operates on the learner's own artifact from the day, which no assistant has seen.
3. The task requires reading or watching named, verified sources (blogs, talks, repository issues, newsletters) and citing one specific thing found there.
4. The answer is a defended choice with a threshold rather than paddable prose.
5. The self-check spine plants checkpoints (a count, a value, a behaviour) the learner verifies alone.

Exploration links follow the standing verification rule: fetched on the day they enter an artifact, dated on the row, never from memory.

## 4. The build gates

1. **Read the row.** The day's curriculum row, the Structure tab, the client-zero state. Missing row, unlocked scenario where entities are needed, or unverified links mean the build stops and names the gap.
2. **Envelope and continuity**, stated in chat.
3. **The spine, one screen, for approval**: deck decision, section lists, the mental-model arc in one sentence, the failures, the activity toggle, the take-home shape. Nothing downstream is built before approval.
4. **Build passes**, one artifact family per pass: decks; notebooks; activity; exercises with solutions; take-home with spine; quiz; study notes, cheat sheet and pre-read.
5. **Verification**: idea caps, cold runs, segment-order parity, link dates, the shortcut test, the distractor audit, audience tags, the banned-word and em-dash scans.
6. **Ship** into the day folder's subfolders, named `C2_W{ww}_D{dd}_{topic}_{AUDIENCE}.{ext}`, or `C2_W{ww}_SAT_{topic}_{AUDIENCE}.{ext}` on a Saturday. The layout is in `content/README.md` and the verifier fails a file that sits in the wrong folder.

## 5. The Day 1 exception

The opening day ships the introduction pack: the client-zero narrative deck (the company as a story, the mental-map diagrams, the entity picture, the spine vertical against the build-week verticals), the journey map (programme, week and day as capability promises), and the session-mechanics section (the teaching-day shape, the Saturday recap, build weeks, platforms, groups of four, the early-weeks AI policy). The teaching half of Day 1 ships the standard pack as usual. The introduction pack is blocked until the client-zero name and entity model lock.

## 6. What changed against the old spec

1. The deck may split into half one and half two; the old spec assumed one deck.
2. Notebooks are upgraded from demo code to rich teaching documents with milestone industry examples and interview questions.
3. Activities gain the toggle-first, minimal-typing, takeaway-tool rules.
4. Take-homes gain the shortcut-resistance patterns and the self-check spine, and their solutions open the next session.
5. Study notes gain the standing transcript-revision step.
6. Cheat sheets move from one-per-module-close to zero-to-many per day as earned.
7. The daily Neo MCQ pool is removed; Kahoot is the sole daily check and it is ungraded.
8. The Saturday recap paper joins as the weekly artifact on regular weeks.
9. Exercise volume is capped by session minutes rather than by the manifest, with think-heavy, type-light answers.
10. A day folder is a set of subfolders by artifact type rather than a flat list of files, Saturday moves out of the numbered days into `SAT/`, and a day with no session gets no folder at all. `content/README.md` is the layout's home and `scripts/verify.py` enforces it.

## 7. Blind spots this method now covers

Version stamping (every pack carries a lock date and freezes 48 hours before delivery), the corrections card as a standing conditional artifact, the distractor audit on every quiz, the parity check across deck, notebook and exercises, and the rule that a pack is INTERNAL work product until its per-audience files are split out.

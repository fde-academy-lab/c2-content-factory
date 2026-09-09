---
name: lesson-strategy
description: Design how a topic will be taught before building any slide, exercise or document. Use this skill FIRST, before training-deck-builder, lesson-architecture, cohort-session-kit or any build skill, whenever a request hands over a TOC, a syllabus, a topic label, a session brief, or asks to teach or explain something. Trigger it when the input is "here is the TOC, build the deck", "teach X to Y", "cover these topics", or any brief where the temptation is to walk the topic list and dress it. Trigger it for corporate training, cohorts, university programmes, client workshops and internal enablement, in any subject. Do not wait for the words "strategy" or "approach".
---

# Lesson strategy

The most expensive mistake in teaching content is skipping this step. Given a
list of topics, the default move is to put one topic on each slide and make it
look good. That produces a deck that covers the syllabus and teaches nothing,
and it gets rejected for being "structural", "not intuitive", "aesthetic but
not glanceable".

**The first act of building content is not building. It is deciding how the
topic will be taught so the learner grasps it and walks out able to do
something.** That design work is where the effort goes. Covering the TOC is the
goal; capturing and enabling the learner is the method. This skill produces the
strategy. The build skills produce the artefact, and they assume this strategy
already exists.

Do the five steps below in order and write the output as a one-screen strategy
brief before any slide is drafted. Show it for approval, because rejecting a
screen is cheap and rejecting a built deck is not.

---

## Step 1: find the learner's real question

A TOC states topics. It does not state what the learner is trying to learn, and
that is what the teaching has to answer. Restate the day's topic as one question
in the learner's own role.

- TOC: "Solution phase, agentic artefacts, the honest artefact set"
- Learner's question: "When I move from *we are building an agent* to handing
  engineering something buildable, which documents do I owe, which are
  mandatory, which optional, and how do I fill each one for my feature?"

The question is the spine. Every concept in the day either answers part of it or
does not belong. Write the question at the top of the brief and keep it visible.

Test it: could a learner tell, from the question alone, what they will be able
to do by the end? If not, the question is still a topic in disguise.

---

## Step 2: name the clarity outcome

State, in one sentence, what the learner walks out able to DO that they could
not before. Not "understand X". A capability they can be tested on.

The clarity test, applied to the finished deck: **the learner leaves knowing
exactly what they learned, why they learned it, and feeling enabled to do or
know something they could not before, with no ambiguity.** If any part of the
deck leaves that in doubt, that part is the defect.

Write the outcome as a "by the end you can ..." line. It becomes the title
slide's promise and the standard the whole build is judged against.

---

## Step 3: choose the anchor

Find one real artefact, object, decision or scenario that the whole topic can
hang off, and that the learner already recognises or will hold in their hands.
Every concept attaches to the anchor. Without one, a deck is a sequence of
unrelated talks.

Good anchors are concrete and singular:

| The topic is about | A good anchor |
|---|---|
| A set of documents | The one sheet that lists them, colour-coded by duty |
| A decision made repeatedly | One real case run through the decision several times |
| A process with phases | One artefact followed as it matures across the phases |
| A choice between options | One scenario where each option is tried and one wins |
| A capability built in layers | One dataset carried through, each tool doing more |

The anchor is chosen, not derived. It is the human judgement that decides the
most in the whole build. Pick the one that teaches cleanest, not the one that is
most complete.

---

## Step 4: engineer each concept for grasp, not coverage

Act as a content engineer: refactor, restructure, discover, research. For every
concept, decide the cleverest way in, and calibrate the depth to the room:

- **Where a concept is too simple for them, show a more evolved way of doing
  it.** Keep it as a variant for the confident half, never a parallel track that
  confuses the rest.
- **Where a concept is new to them, establish it simply, step by step**, before
  anything depends on it.
- **Wherever a concept could create ambiguity, doubt or a follow-up question,
  simplify it until it cannot.** That is the engineering. If a point keeps
  raising "but what about", the structure is wrong, not the wording.

The concept treatment that has been accepted repeatedly (the grounded unit):

1. **Ground it.** What the topic is, where it is used, why THIS audience needs
   it, where it lands in their own world. This is the step most often skipped and
   its absence is what makes content feel ungrounded.
2. **The clearest example**, simple and relatable, which need not be the anchor.
3. **A simplified framework or formula**, invented if useful, made doable in the
   head. A division, a count, a 2x2, an acronym. Never algebra.
4. **The steps**, one at a time.
5. **One worked example** through the steps.
6. **Apply it to the anchor**, with the anchor's real values.
7. **A real case with a number**: a company, a consequence, a figure.

Woven through: a quiz or thought-provoking question answerable by one keystroke
in the chat (type A/B/C, or Y/N), and a diagnostic line the learner can say.

---

## Step 5: decide the flow, then hand off

Sequence the concepts so each depends only on what came before, and order for
early capability rather than logical completeness. Name the natural decisions,
not the natural topics, and make each segment answer one question.

Then write the brief and stop. The brief is the deliverable of this skill. It
contains:

- The learner's question (step 1)
- The "by the end you can ..." outcome (step 2)
- The anchor, named (step 3)
- The concept list, each with its way-in and its real case (step 4)
- The flow, as an ordered list of segments (step 5)
- Two or three decisions you need from the requester before building

Hand this to `training-deck-builder`, `lesson-architecture` or
`cohort-session-kit`. Those skills build the artefact. They do not re-derive the
strategy, and they must not be started before this brief is approved.

---

## The reference-first law

Before drafting the strategy, choose what it is modelled on. Find one existing
piece of material that already solves the structure problem for this kind of
topic, and adapt it: keep its philosophy, its wording register and its
progression, change only the subject. Inventing structure from a blank page is
hard and produces mediocre results. Adapting a working structure is easy and
produces good ones.

Budget: one written source and one video source, no more. More references
conflict and the output averages them into something that follows none.

---

## What this skill is not

It is not the build. It produces no slides. If you find yourself writing slide
content, stop and return to the brief.

It is not a template to fill. The five steps produce different strategies for
different topics. A strategy that looks like every other strategy has skipped
the thinking.

It does not replace the build skills' own rules on layout, palette, diagrams and
verification. Those still apply, downstream, once the strategy is approved.

---

## Failure modes that have actually happened

- **Walking the TOC.** One topic per slide, dressed. Rejected as structural, not
  intuitive, doing too much. The fix is this whole skill: decide the teaching
  before the slides.
- **A weak anchor.** "The same case from last session" as a one-line callback.
  The anchor has to be grounded properly, often across two pages, with a name and
  real numbers, or it does not anchor anything.
- **Coverage mistaken for teaching.** Every topic present, nothing graspable. The
  clarity test catches this: if the learner cannot say what they can now do, the
  deck failed regardless of completeness.
- **Over-complication.** Trying to do too much, adding structure with nothing
  under it. Simplicity is a structure and a way of thinking, not fewer words or
  fewer diagrams. Substance over style, always.

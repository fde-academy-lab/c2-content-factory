---
name: curriculum-detailing
description: Expand a table of contents into session-level detail a trainer can teach from and a learner can follow. For every session it fixes the ideas counted against a cognitive-load cap, a depth target per sub-topic that rises as the course progresses, prerequisites including first-use tools, a verified reference pack (one popular video, articles, a repo, an architecture diagram, interview questions), the narrative and where it came from, a continuity block saying what was covered, what not to repeat, the spine case state and fresh cases, and the interview competencies the session advances. Use it whenever a TOC, syllabus, week plan or module outline has to become a day-wise or session-wise plan, whenever a session brief names only the topic, whenever a trainer handover is being prepared, or whenever a session has too many sub-topics or sits at ten thousand feet. Runs after lesson-strategy and the lesson-architecture map, before cohort-session-kit. Do not wait for the word detailing.
---

# Curriculum detailing

A table of contents fixes the topics and the timeline. It never says how deep
to go, what the room already knows, which case to carry, what to read first, or
which interview question the session has to make answerable. That layer is
missing from almost every curriculum, and its absence is why a trainer opens
the material ninety minutes before a session and does not know where to start.

This skill builds that layer. The topic list and the timeline are sacrosanct.
Everything under them is decided here.

## Where it sits

```
lesson-strategy        the room's real question, the anchor, the flow
lesson-architecture    the world, the map, the units
curriculum-detailing   THIS SKILL: each session's ideas, depth, references,
                       continuity, interview coverage
cohort-session-kit     the nine artifacts of the day
training-deck-builder  the deck
```

Do not run this before the map exists. Do not run cohort-session-kit until this
has produced the session row, because every artifact in the kit is sized and
scoped by what this skill decides.

## The two failures this skill exists to stop

Both are overestimation, and both come from building blind from a topic label.

| Failure | What it looks like | The tell |
|---|---|---|
| **Too many sub-topics in a day** | Eight ideas in two hours, each with its own jargon, none reaching a worked example. The room leaves overwhelmed and remembers nothing | More than four decision sentences in a two-hour block |
| **Ten thousand feet** | The right topics at the right times, each described rather than taught. No numbers, no failure, no steps. The room leaves underwhelmed and calls it gyaan | A sub-topic with no worked example carrying real values and no gotcha |

The second is less common and more expensive to fix late, because the timeline
was honoured and nothing was learned.

## The eight steps

Run them in this order. Steps 1 and 2 come before any sub-topic ladder is
written, because the count and the research are what stop the two failures.

### Step 1: count the load

An **idea** is anything that needs its own unit, and a unit is anything that
unlocks one decision the learner could not make before. Count the decision
sentences in the session, not the headings.

| Block | Cap on new ideas | Cap on new terms |
|---|---|---|
| Two hours | Four | One per idea, each introduced after the problem it names |
| Three hours | Five | Same rule |
| A full day | Three blocks, one of which is practice with no new ideas. Eight at most | Same rule |

The two-hour cap is the standing rule. The scaling is a construction and is
marked so in `references/cognitive-load.md`, which also carries what counts as
an idea, what does not, and the established research behind the cap.

Over the cap: split the session, defer an idea to its natural later slot, or
demote an idea to a variant of one already there. Never shrink the units to
fit.

### Step 2: research the reference pack, per sub-topic, before fixing the ladder

Building blind from a topic label is what produces both failures. Popular
resources reveal the natural progression and the illustrations that already
work. Engineering resources reveal the depth. Interview questions reveal what
the session has to make answerable.

Five slots per sub-topic, each verified on the day it is added:

1. One popular, well-illustrated video
2. One or two articles or blog posts
3. One repository or engineering implementation
4. One architecture diagram or engineering write-up
5. Interview questions found in the wild, with the level they are asked at

Protocol, verification rules and the difference from the structural reference
lock are in `references/reference-pack.md`. The short version: the lock is one
written and one video source for the SHAPE of the whole family; the pack is
per-sub-topic sourcing for the CONTENT and the learner's further reading. They
are different jobs. A URL from memory is never a reference. Borrow the visual
idea from a video, never the artwork.

### Step 3: set the depth target per sub-topic

Four levels, named so they decode themselves:

| Level | The learner can | The tell in the material |
|---|---|---|
| **L1 Name it** | Recognise it, define it, say where it is used | Grounding and the clearest example |
| **L2 Use it** | Run the steps on a clean case and get the right answer | The steps and one worked example with values |
| **L3 Explain why** | Derive it from first principles, say why it has this shape, say why it fails | The strip, the derived framework, the gotcha |
| **L4 Handle it breaking** | Diagnose it, choose between alternatives with a threshold, design with it | The failure slide, the deliberate failure in code, the decision rule |

Every sub-topic gets a target for THIS session. The first encounter is L1 or
L2. A sub-topic that returns rises at least one level each time. The core
sub-topics of a course reach L4 before it ends. Static depth across a course is
futile, because the room grows and the same explanation stops landing.

`references/depth-targets.md` carries the levels, how each weights the ten-slot
unit, the rising-altitude table aligned with the early-middle-late arc already
used in study notes, and the return question.

### Step 4: find the narrative, and say where it came from

Before writing the ladder, step back and decide the one narrative that makes
depth, breadth, hands-on and the interview question fit in a single arc rather
than four tracks. The narrative is one sentence: a Tuesday morning at the
airline, one passenger, six options and nobody can rank them.

Four sources, and the row records which:

- **Researched**: the narrative exists in the reference pack and is adapted
- **Copied**: the structural reference already does this and the subject changes
- **Invented**: built here, and marked as a construction
- **Hybrid**: any combination, and the parts are named

It cannot be static across topics. A course whose every session opens the same
way reads as a loop. Vary the shape, and let the subject pick it.

### Step 5: write the sub-topic ladder

One entry per idea, in the order they are taught, each carrying:

- The decision sentence
- The depth target for this session
- The interview competencies it advances (from `references/interview-ladder.md`)
- Whether it is new, revisited, or a variant of an idea already present

Order for early capability, never for logical completeness. The learner should
be able to do a whole small thing by the end of the first block.

### Step 6: write the continuity block

This is the part a trainer opens first, and the part every curriculum omits.

| Line | Content |
|---|---|
| Covered before | Each earlier sub-topic this session depends on, the depth it reached, and the session it reached it in |
| Do not re-teach | What is already closed, with the one-line recall permitted |
| Spine case, current state | The world, and every value already decided in earlier sessions |
| Fresh cases | Simpler cases this session can use for its clearest examples |
| Case studies | Real companies with a number and a dated, verified source |
| First-use tools | Every tool or environment the session uses for the first time |
| Basics budget | Minutes allowed on material the room could have read, fifteen at most in a two-hour block |
| Revisited at | Where each of this session's ideas returns and at what level |

The same block is copied into the trainer notes front matter by
cohort-session-kit. The detailed curriculum is the source of truth; the trainer
notes carry the extract.

### Step 7: map the interview coverage

The skill that clears an interview overlaps almost exactly with the skill that
does the job. Interviewers probe nine things, and the session ladder has to
advance them on a schedule rather than by accident:

what you have done · depth of understanding · clarity on concepts · breadth ·
connecting the dots · inner working · why it happens · why it fails · handling
failure

Each idea names which it advances. The course-level check is that all nine are
built before the course ends and that the later sessions weight the last four.
`references/interview-ladder.md` maps each competency to the artifact that
builds it and gives the transfer question shape per depth level.

### Step 8: check

Run `scripts/check_detailing.py` on the detailed curriculum file. It flags
sessions over the idea cap, terms exceeding ideas, ideas without a depth
target, revisited sub-topics whose depth did not rise, reference packs with
unverified or missing slots, missing continuity lines, and sessions with no
transfer question or fewer than two follow-ups.

Then read the whole plan once as the learner would, front to back, and ask at
each session: could I do something new at the end of this that I could not do
at the start, and does the next session assume exactly that and no more.

## The session row

The canonical format is in `references/session-row.md` with a worked example.
The checker parses that format. A curriculum written in any other shape has to
be converted before the checker runs, and the conversion usually exposes the
gaps.

## Starting from scratch without dwelling on basics

Both are required and they are not in conflict once the mechanism is named.

- **From scratch** means no prior knowledge of the topic is assumed, ever
- **Not dwelling** means the basics are taught through the first application
  rather than as a preamble, capped by the basics budget, and anyone who needs
  more gets the weekly remedial task and the pre-read
- The first working thing appears inside the first fifteen minutes. Everything
  the room needs to understand it is taught while taking it apart

## The grilling cadence

Depth is built by being questioned repeatedly, not by being told once.

- Every session's starter quiz carries one **return question**: a transfer
  question from an earlier session, asked one depth level higher than it was
  first asked
- Questions climb with the course. Early sessions ask what the room can answer
  from experience. Middle sessions ask questions that need a framework from two
  sessions back. Late sessions ask questions that combine two strands
- Guidance fades in the same arc: full worked examples early, complete-the-
  missing-step in the middle, build-from-a-brief late

## Before shipping the detailed curriculum

1. Are the topics and the timeline exactly as the TOC gave them?
2. Does every two-hour block carry four ideas or fewer, counted as decision sentences?
3. Does every idea have a depth target, and is the first encounter L1 or L2?
4. Does every revisited idea rise at least one level?
5. Do the core sub-topics reach L4 before the course ends?
6. Does every sub-topic have a reference pack with all five slots verified and dated?
7. Was the pack researched before the ladder was fixed, and does the ladder show it?
8. Does every session carry its narrative and its provenance?
9. Does the continuity block exist with all eight lines?
10. Is the basics budget stated and under fifteen minutes per two-hour block?
11. Does every idea name the interview competencies it advances, and are all nine built by the end?
12. Does every session carry a transfer question with two follow-ups and a return question?
13. Did the checker pass, and were its findings fixed rather than argued with?
14. Read as the learner: does each session end with a new capability and does the next assume exactly that?

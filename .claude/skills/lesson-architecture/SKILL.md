---
name: lesson-architecture
description: Structure a family of related concepts into a navigable map, a repeatable unit anatomy, and one shared worked world. Use this skill whenever the work covers more than one concept that has to be learned in sequence, which includes curricula, syllabi, module maps, learning paths, course outlines, brochures listing what a programme teaches, self-study handbooks, reference material, multi-day training, onboarding tracks, and any deck that walks through a family of related ideas rather than a single argument. Trigger it when the user says curriculum, syllabus, outline, learning path, module list, tutorial, handbook, self-paced, revision material, or asks how to sequence or split topics. Trigger it alongside training-deck-builder whenever a deck teaches four or more related concepts. Do not wait for the word "curriculum".
---

# Lesson architecture

Most teaching material fails at the seams rather than inside a topic. A learner
who cannot see where they are, cannot recall what came before, and has to learn
a fresh example for every concept will forget the whole set regardless of how
good each part was.

Three levels fix that, and all three have to exist. The map tells the learner
where they are. The unit anatomy makes every topic feel like the last one so
attention goes to the content instead of the format. The shared world removes
the cost of learning a new example each time.

Build them in this order: world, map, units. The world constrains what the map
can promise, and the map constrains what each unit is allowed to cover.

---

## Level 1: the world

One named scenario, with its own artifact, set up once before any concept is
taught, and used by every unit afterwards.

The setup artifact carries five things and nothing else:

| Slot | What goes in it |
|---|---|
| Name | A short proper name the learner will say out loud, such as `classicmodels` or `Sunrise Airways` |
| One-line business | What this organisation does, in one sentence a stranger would understand |
| The entity list | Each entity with a one-line purpose, six to nine of them |
| The picture | A relationship diagram showing how the entities connect |
| The instruction | Print it, keep it beside you, you will use it in every unit |

### The witness rule

This is the technique that separates a good shared world from a decorative one.

Before writing a single value into the world, list every teaching point the
course has to land. Then plant, in the data, one feature that only that
teaching point explains. Each such feature is a **witness**: without it, the
lesson that needs it produces output identical to the lesson before it, and
the learner sees nothing.

The reference `inventories` table is seven rows and five columns, and every
column is carrying a witness:

- Two products priced identically at 999.99, so the multi-column sort has a tie
  to break and the second sort key visibly changes the order
- Two rows with a missing colour, so the two null-handling options produce
  visibly different output
- Price and quantity inverted against each other, so sorting by their product
  reorders the list completely rather than reproducing the price order

Run the check mechanically. For each planned unit, name the row or the value in
the world that makes that unit's output different from the unit before it. A
unit with no witness is either teaching nothing new or needs the world extended.

Keep the world small enough to verify by eye. Seven rows beats seven hundred,
because a learner who can hand-check the output trusts the lesson.

### Two ways to hold the world

| Shape | How it works | Use it when |
|---|---|---|
| Given world | Loaded once at the start, complete from day one, never modified | The subject is querying, analysing or deciding against a stable situation |
| Built world | The learner constructs it as the course proceeds, so it grows unit by unit | The subject is designing or building, and the artifact at the end is the proof of learning |

The two reference sites split exactly this way. One hands over a complete
eight-table retailer database before lesson one. The other has the learner
design an inventory system across a whole section, and every later lesson runs
against what they built. Pick one and say which it is. Mixing them means the
learner never knows whether they are supposed to have built the thing.

---

## Level 2: the map

The map is a real deliverable, not a table of contents. It is the artifact a
prospective learner reads in three minutes to decide whether to enrol, and the
artifact a current learner opens to find where they are.

Its shape:

```
Section N. <Plain name of the section>
In this section, you will learn <one sentence, the capability gained>.

- <Unit name> - <verb-first one-liner saying what this unit does for you>
- <Unit name> - <verb-first one-liner>
```

Rules that hold it together:

- **Sections are numbered and named for the task, never for the machinery.**
  "Filtering rows in a table" is a section. "Predicates and operators" is a
  chapter heading from a manual
- **Every section gets its one-sentence promise.** The promise names a
  capability, so a learner can tell whether they already have it
- **Every unit gets a verb-first one-liner.** "Sort rows by one or more
  columns" tells a learner what they get. "ORDER BY clause" does not
- **Five items per section is the working average.** The reference map runs 101
  units across 20 sections, averaging five, ranging from two to twelve. A
  section at twelve is a signal it is really two sections
- **Order for early capability, not for completeness.** The reference course
  puts create, insert and select in section one so the learner does something
  end to end on day one, then goes back and teaches proper design in section
  three. A logically complete ordering that leaves a learner unable to do
  anything for two sessions is the wrong ordering
- **The map stays visible.** In a website it is the sidebar on every page. In a
  deck it is a recurring map slide with the current section marked. In a
  handbook it is the first page and the running header

---

## Level 3: the unit

One unit is one decision or one capability, sized at three to five minutes of
reading or eight to twelve minutes of teaching. Both reference sites print the
estimated reading time on every page, and 3 to 5 minutes is what they land on.

### The nine slots, in this order, every time

| # | Slot | Content |
|---|---|---|
| 1 | Title | The thing, optionally plus its job: "ORDER BY: sorting rows in a query" |
| 2 | Promise | One sentence: "you will learn how to X". Plus the time it takes |
| 3 | The broken default | What happens without this thing, stated first. Then the thing that fixes it |
| 4 | The skeleton | The abstract shape with placeholders, followed by a numbered decomposition of its parts |
| 5 | The machine | How the system actually processes it, plus one consequence the learner can use |
| 6 | The world | A pointer to the shared world, or the small extension this unit needs |
| 7 | The ladder | Five to seven examples in ascending complexity, one variation each |
| 8 | The gotcha | The edge case that bites in production, placed last among the examples |
| 9 | The rules | Four bullets, one rule each, no prose, no closing sentence |

### Slot 3 is the one usually skipped

Both reference pages open by saying what goes wrong without the feature. Rows
come back in an unspecified order. That single line is what makes the rest feel
necessary rather than arbitrary. Write the broken default before writing the
definition, every time.

### Slot 4, skeleton before instance

Give the abstract shape with placeholders first, then number its parts and
explain each. This is a better opener than a worked example for anything with a
grammar: a syntax, a template, a document structure, a decision procedure, a
canvas. The learner gets a slot to hang every later example on.

For topics without a grammar, keep the existing default of picture, then
detail, then worked example.

### Slot 7, the ladder

Each rung isolates exactly one new variation, and the rungs go simplest to
hardest. The reference ladder for sorting runs: one column, then several
columns, then an expression, then an alias for that expression, then a date,
then the null case. Six rungs, six ideas, no rung introducing two things.

Every rung shows the actual output. Never describe a result. Print it. A
learner who cannot see the change cannot learn the change, and a learner who
can hand-check seven rows against the claim starts trusting the material.

### Slot 9, the rules

Four bullets. Each is one complete sentence stating one rule. No summary
paragraph, no "in this tutorial we covered". The rules block is what a learner
photographs, so it has to survive with no surrounding text.

---

## The recall spine

Byte-sized units only work if something carries the learner across them.
Four devices do that, and all four are cheap:

| Device | In a website | In a deck or handbook |
|---|---|---|
| Linear position | Previous and next links at the foot of every page | A numbered kicker on every slide, and a map slide at each section boundary |
| The whole family in view | The sidebar listing every unit, always | The map slide, repeated with the current section marked |
| Backward hooks | The first mention of a prior concept is a link to its unit | The first mention names the unit it came from, in the body text |
| Forward hooks | The next link says what comes after and why | The closing rules slide names the decision the next section answers |

Backward hooks are the highest-value and the most often missed. Every time a
unit uses a concept taught earlier, name that unit at the point of use. It costs
four words and it converts a forgotten topic into a retrievable one.

Add one more the reference sites use and most training does not: **a
one-question feedback control on every unit, not on the whole course.** Was this
unit useful, yes or no. Course-level feedback tells you the course was fine.
Unit-level feedback tells you which unit to rebuild.

---

## Where this pattern breaks

State this honestly whenever the pattern is applied outside its home territory,
because applying it blind produces confident, well-formatted trivia.

**The pattern assumes separable concepts.** It comes from teaching formal
systems where one clause genuinely can be understood without the next. Judgement
subjects are entangled: the choice of autonomy level cannot be taught apart from
the cost of being wrong, because the interaction is the lesson. Slicing
entangled material into isolated units teaches the vocabulary and none of the
skill.

The correction is to **size units by decision, not by term.** A unit is one
decision the learner can make at the end that they could not make at the start.
If two terms only make sense together, they are one unit.

**The pattern assumes a reader who already wants this.** Search-landing pages
need no hook because arrival implies intent. A room of senior people who were
scheduled into a session has no such intent, so the cold open on the failure and
the stakes stays exactly where it is. The nine slots go inside the session, not
in front of it.

**Full self-containment belongs at unit level, not slide level.** A web page is
self-contained because readers land cold. A deck has a linear captive audience,
so repeating context on every slide reads as padding. Self-contain the unit;
connect the slides.

**The register is deliberately flat.** These sites have no voice, no opinion and
no personality, which suits a reference and starves a taught session. Keep the
strong opinions, the invented frameworks and the honest pushback. The structure
is what is being copied, not the tone.

---

## Applying it to each artifact type

| Artifact | The map becomes | The unit becomes | The world becomes |
|---|---|---|---|
| Deck | A section map slide, repeated at each boundary with the current section marked | Four to eight slides covering the nine slots | A world slide near the front, referenced by every applied slide |
| Handbook or self-study doc | The first page, numbered sections with promises | One page per unit, nine slots, three to five minute read | A named setup page with the entity table and the relationship picture |
| Exercise set | A one-line index of which unit each exercise tests | One file per unit, scoped strictly to that unit | Every exercise drawn from the same world, never a fresh scenario |
| Brochure or curriculum doc | Exactly this map, verb-first one-liners included | Not present; the map is the whole artifact | A named case, so the buyer can see what learners will work on |
| Workbook | The tab list, one tab per unit | One tab per unit, ending in a computed result | The pre-filled worked example tab |

---

## The build instruments

`references/build-instruments.md` carries four tools that make the rules above
mechanically checkable rather than a matter of judgement. All four are this
skill's own constructions, not established practice, and the reference file
says so inside itself.

| Instrument | What it catches | When to run it |
|---|---|---|
| The witness matrix | Teaching points with no visible witness, unused case detail, and load-bearing values nobody should edit casually | During case design, before any slide exists |
| The delta line | Slides showing nothing new, and slides carrying two ideas | As a pass over the finished build file |
| The decision sentence | Units sized by term rather than by decision, padded sequences, missing units | While drafting the map |
| The carry-forward chain | Orphaned units and missing prerequisites at the seams | While drafting the map, and again after any reorder |

---

## The check before shipping

Run these in order. Each has a hard answer.

1. Does the world have a name, a one-line business, an entity table and a picture?
2. For every unit, name the witness in the world that makes its output different from the previous unit. Any unit with no witness is cut or the world is extended
3. Does every section of the map have a one-sentence capability promise?
4. Is every unit one-lined with a verb first?
5. Is any section above eight items? Split it
6. Can a learner do something end to end by the end of section one?
7. Does every unit state the broken default before the definition?
8. Does every example show real output rather than describing it?
9. Does every unit end in three to five rules, each a complete sentence, with no closing paragraph?
10. Does every reuse of an earlier concept name the unit it came from?
11. For a judgement subject, is each unit a decision rather than a term?

---

## The reference-first law

This comes before every other rule in this skill, and it is the step most
often skipped.

**The first act of building content is choosing what it is modelled on.** Not
outlining, not drafting. Finding one piece of existing material that already
solves the structure problem for this family of concepts. Inventing structure
from nothing is hard and produces mediocre results; adapting a structure that
demonstrably works is easy and produces good ones.

Once a reference is chosen, the instruction that works is to keep its
philosophy, its wording register and its progression, and change only the
subject. That is a reliable transformation. Building the same thing from a
blank page is not.

### The reference budget

**One written source and one video source. No more.** More references produce
worse output, not better, because the structures conflict and the result
averages them into something that follows none. Two good sources beat six.

### The lock ritual

The choice of reference is the human judgement that decides the most in the
whole build, and it is the one an assistant cannot make well alone. Run it as:

1. Two or three people search independently, without comparing notes
2. All the candidates go on the table together
3. One written and one video source are chosen
4. The choice is **locked** and every unit in the family is built against it

Lock it before drafting. A reference changed mid-build means the units already
written no longer match the ones still to come, and that mismatch is exactly
the structure problem the reference was chosen to solve.

---

## The spiral: same data, new tool

The strongest device for a programme that teaches several tools over the same
problem space, and the one that makes a curriculum feel like one thing rather
than a series of unrelated courses.

Hold the data constant and change the instrument. At each turn, the learner
already knows what the answer should look like, so all their attention goes to
the new tool, and the moment where the old tool runs out is the argument for
the new one.

A worked run of it:

| Turn | Instrument | What the same data teaches |
|---|---|---|
| 1 | Plain language primitives, a list of records | Missing values, filtering, aggregation done by hand |
| 2 | The analysis library | The same operations in one line each, and the first operation the primitives could not do at all |
| 3 | The query language | The same records in a database, the same questions asked declaratively |

Three rules make it work:

- **The data is recognisably the same records at every turn.** Not a similar
  dataset, the same one. Recognition is the whole mechanism
- **Every turn shows one thing the previous instrument could not do.** Without
  that, the new tool looks like a syntax change and the learner asks why they
  are learning it twice
- **Say the spiral out loud once, near the start.** Learners who know the same
  problem is coming back with better instruments stop treating each module as
  a fresh start

This is also the answer to trainer churn. When the trainer changes every two
weeks, the shared data is the only thing carrying continuity across the
handover, and it only survives if it is in the content rather than in a
trainer's head.

---

## The scenario budget

The connected world is not free to change.

- **Establish the scenario before any teaching begins**, as its own artifact
  rather than inside the first lesson
- **Change it at most two or three times across a whole programme.** Every
  change costs the learner a domain to learn, and a course that opens each
  module in a different company is teaching domains rather than concepts
- **Grow the world instead of replacing it.** Add an entity once the learner
  has been through three or four rungs of complexity on the existing ones. Add
  the analytics-shaped part of the world just before the analytics module
  rather than at the start
- The feel to aim for is joining an organisation and growing inside it, where
  the same place gets larger and more detailed rather than being swapped for a
  different place each month

**Concepts and messy real data are never mixed.** Concept teaching runs on
clean, small, engineered data where the answer can be checked by eye. Real
datasets bring volume, missingness and inconsistency, each of which is its own
lesson, and they belong in a build slot after the concepts are secure.

For learners meeting a subject for the first time, use cases are useless until
the concept is clear. The industry framing that motivates a senior audience is
noise to a beginner who cannot yet do the thing.

---

## Two examples per concept

Every concept gets two, and they do different jobs:

1. **The connected example**, drawn from the shared world, which maintains the
   thread and shows the concept in context
2. **The clearest example**, purpose-built if necessary, which shows the
   concept with nothing else in the frame

Lead with whichever is clearer for that concept and always give both. A
concept taught only through the shared world can be obscured by the world's own
complexity. A concept taught only in isolation never joins anything.

## The map hands off to curriculum-detailing (added 3 Sep 2026)

Level 2 fixes sections and units. What it does not fix is how deep each unit
goes in a given session, how many units a session can hold, what the room
already knows, or what each unit was built from. That layer is the
`curriculum-detailing` skill, which runs after the map and before
`cohort-session-kit`, and produces one row per session.

Two things the map needs to carry so detailing can use it:

- **A core mark on the units** whose transfer questions the final quarter
  depends on. Detailing checks that every core unit reaches the top depth level
  before the course ends, and it cannot check what the map did not mark
- **The band of each section**: early, middle or late. Depth targets and the
  question form rise with the band

### The reference lock and the reference pack are different things

The lock above is one written and one video source for the SHAPE of a whole
family, chosen by the lock ritual and locked before drafting. The pack, built
per sub-topic by `curriculum-detailing`, is five verified slots for the
CONTENT: a popular well-illustrated video, one or two articles, a repository,
an architecture write-up, and interview questions with their level. The lock
stays at two because more than two conflict on structure. The pack can hold
five because nothing in it is copied for structure. Never let a pack item
replace the lock, and never let the lock be the only source of content.

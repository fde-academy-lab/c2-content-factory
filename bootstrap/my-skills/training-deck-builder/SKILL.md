---
name: training-deck-builder
description: Build teaching and training slide decks that people actually learn from. Use this skill whenever the user mentions a deck, slides, a presentation, a session, a workshop, a masterclass, a module, a cohort, a curriculum, a lesson plan, a half day or a full day of training, or asks to teach or explain something to a group. Trigger it even when they only describe a session out loud ("Day 3 covers RAG, four hours, mixed room"), paste a curriculum, hand over a content markdown file, or ask to improve, pad, restructure or fix an existing deck. Trigger it for corporate training, bootcamps, university programmes, internal enablement, client workshops and conference teaching, in any subject or technology. Do not wait for the word "deck".
---

# Training deck builder

A deck is judged by one thing: can a learner who was not in the room open it
and learn from it. Everything below serves that.

Work in this order. Do not skip the first two steps even when the request
looks small.

---

## 1. Fit the room before writing a word

Search memory and past conversations for the cohort before asking anything.
Look for: who is in the room, seniority, what they already know, what landed
and what failed in earlier sessions, the running case already in use, the
named devices already taught, the design system already approved, and the
client's own vocabulary.

Then write down the arithmetic, in the chat reply and never in the deck:

| | |
|---|---|
| Total session length | |
| Minus break, arrival, wrap | |
| Live teaching minutes available | |
| Which slot this deck occupies | |
| What runs immediately before and after | |

Budget at roughly **3 to 3.5 minutes per teaching slide**, **under a minute
for a glance-only picture**, and count activity time separately at its stated
duration. A deck that overruns is a deck that gets half delivered.

Ask only what you genuinely cannot infer, and ask it as a short list of
choices rather than open questions. Three questions maximum. Never ask
anything memory already answers.

Read `references/intake.md` for the question set and the defaults to assume
when the user does not answer.

---

## 2. Choose the spine from the content, not from a template

The spine is the subject's own structure, stated in plain English, walked one
part per slide, in order. It is never a pedagogical rhythm laid on top.

Good spines look like: `START, MOVE, CHANGE, ARRIVE, CHECK` ·
`Plan, Act, Observe` · `What it is, where it breaks, what to do instead` ·
`Qualify, Scope, Prove, Sequence`. Plain words, self decoding, five parts
or fewer.

Write the spine as a screenful and show it before building anything large,
so rejecting it is cheap. For a single deck under about 25 slides, build
directly and show the spine inside the reply.

Two rules that decide most of the quality:

- **One or two major frameworks active at a time.** Later sections open up
  one part of the framework already taught rather than introducing a
  parallel one.
- **Plain words before formal terms.** Introduce the formal term only after
  the learner has met the problem that needs it, with an explicit line:
  "this is commonly called X". Do not invent a named device where an
  ordinary word works.

---

## 3. Treat each topic in the way that topic is best understood

There is no single sequence to repeat down the deck. Repeating one shape for
every topic is what makes a deck feel assembled. Pick the treatment that fits
what the topic actually is:

| The topic is | Treat it as |
|---|---|
| A structure or a set of parts | A picture of the whole first, then one slide per part |
| A choice between options | A comparison grid, then the decision rule, then one worked call |
| A procedure | The end-to-end flow, then the steps, then a worked run |
| A distinction people conflate | The two things side by side with real values, then where each fails |
| A taxonomy | A fan-out or a positioning grid, then the table, then a spot-the-type drill |
| A hidden failure mode | The symptom first, then the mechanism, then how it is detected |
| A judgement call with no right answer | Two scenarios that look identical and resolve differently |
| Vocabulary | A nesting or containment picture, then the definitions with examples |

Within a topic, the default order that works is **picture, then detail, then
worked example**. A table that arrives before its picture is the single most
common miss. Vary the shape of each of those three across topics so the deck
does not read as a loop.

`references/topic-treatments.md` has the full catalogue with a concrete
diagram suggestion for each.

---

## 4. Write slides that teach on their own

- **Every title names the thing being taught or the question being
  answered.** Never a narrative moment. "Memory taxonomy: five types,
  storage shape per type" is a title. "The day the pipeline broke" is not.
- **Every slide carries the point plainly, a concrete example with real
  values, and a rule or takeaway.** Real values means `Germany` becomes
  `DE`, not "the value is transformed".
- **One idea per slide.** If two ideas fit, they are two slides.
- **Glance test.** If it is not understandable at a glance it is not
  helpful.
- **Depth for both ends of the room at once.** A lateral beginner gets the
  ground-up explanation, a senior practitioner gets the specific detail they
  have not seen. Slides that only serve one end waste half the room.
- **State definitions explicitly.** Substance-heavy decks fail most often on
  missing definitions and abrupt openings, not on missing narrative.
- **Include an honest "where this fails" slide** for any method being
  taught.
- **Never generic.** This is the cardinal sin.

---

## 5. Zero meta-content, checked mechanically

Nothing on a learner-facing slide may be about the teaching, the trainer,
the session mechanics or the deck itself.

Banned from slides, allowed in speaker notes:

- Facilitation instructions: "ask the room", "take answers by show of
  hands", "give this five minutes", "the room will split here", "do not
  reveal yet", "circulate and check"
- Deck self-reference: "this deck", "the previous slide", "Deck 2 covers",
  "as we saw earlier", "in the next section"
- Programme framing: agenda slides, audience slides, "how this session
  runs", learning-objective lists, recap-of-yesterday slides
- Pedagogical scaffolding shown to learners: beat labels, rhythm markers,
  "the problem / the intuition / the picture" headers
- Design rationale, confidence marking, sizing arithmetic, anything
  explaining why the structure is what it is

Allowed on slides: a one-line promise on the title slide, learner-facing
activity instructions ("in pairs, ten minutes, pick one case"), and a
duration on an activity.

Before delivering, run the scanner:

```bash
python3 scripts/meta_scan.py <content-file-or-deck.pptx>
```

Fix every hit or justify it in the reply. `references/meta-content.md` has
the full pattern list and the rewrite for each.

---

## 6. Visuals that carry information text cannot

Build diagrams, not decoration. Every visual must let a learner see something
they could not read as fast:

nesting and containment · fan-outs · positioning grids on two axes ·
decision trees · before and after value pairs · comparison grids ·
sequences with the mechanism labelled on each edge · state machines ·
band charts placing items into categories · annotated worked traces

Mature register: flat, aligned, thin bordered, generous whitespace. No tilt,
no drop shadows, no saturated colour, no accent stripes under titles, no
decorative bars. One accent colour, used sparingly and always to mean
something.

`references/design-system.md` has the approved palette, typography, slide
kinds and the build pipeline that produces them.

---

## 7. Opening and closing

**Opening.** Three or four questions, no more. Each one plants the topic it
precedes. Collect answers, defer the explanation, and close each loop later
at the slide where the answer becomes useful, with a visible callback band.
Do not open with a recap, an agenda or a cute conceit.

**Closing.** A dense recall table or a numbered rule list, and a short set of
questions the method does not yet answer. No motivational lines. A senior
audience will not read them.

---

## 8. Activities

Selection over typing. Learners pick from MCQs, multi-select, matching to a
lettered bank with distractors, ordering shuffled cards, filling a table from
a diagram, spot-the-wrong-arrow, pick-the-best-fix. Reserve free writing for
three short lines at most.

Size by learner output, not by page count. Count what the learner must
actually produce and keep it inside the slot. Exercises that ate 44 percent
of a session are the reason half a day went undelivered.

Give one fully worked model to pattern-match against before asking for
anything.

---

## 9. Build, then verify

Build with `pptxgenjs`, diagrams as hand-written SVG rasterised through
`sharp`. `references/design-system.md` carries the working builder patterns
and the gotchas that cost real time.

Verification is not optional. Run all of it:

```bash
python3 scripts/qa_deck.py <deck.pptx>
```

It checks: schema validation, em-dashes in both literal and escaped form,
banned words, meta-content patterns, slide and notes counts, and edge-bleed
per slide. Then render to images and look at every slide:

```bash
python3 /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf deck.pptx
pdftoppm -jpeg -r 120 deck.pdf slide
```

Look for text overflow first, then overlaps, then uneven gaps. Fix in the
generator, never by hand-editing the packed XML.

---

## 10. Delivering it

Speaker notes carry everything the trainer needs and the learner must not
see: what to open with, what to put to the room, the trap in the slide, where
to hand a question back to the room, what to cut if time runs short.

In the chat reply, and never in the deck: the arithmetic, what you assumed,
the judgement calls worth overriding, and a cut list in priority order with
what each cut costs.

When an approved deck needs improving, **add, do not rewrite.** Keep every
existing slide untouched and insert context slides around the relevant ones.
Splice by anchor title so the originals are provably unmodified.

---

## Failure modes that have actually happened

- Building the pedagogical scaffold as the content. Named beats, story
  openings and invented devices optimise for the trainer's delivery
  experience instead of the learner's knowledge acquisition. When a teaching
  problem is described, the fix goes into how the subject is sequenced and
  stated, never into visible teaching machinery.
- Meta-slides eating the deck. Audience, programme framing, cohort survey and
  recap slides taught nothing and got a deck rejected outright.
- A table arriving before its picture, so the learner reads rows without a
  mental model to hang them on.
- Inventing a parallel framework in section three when section one's
  framework had a part that could have been opened up instead.
- Presenting an invented taxonomy as though it were an established standard.
  Say plainly which terms are established, which are informal labels teams
  use differently, and which are this course's own construction. That marking
  belongs in the notes, not on the slide.


## VISUAL LANGUAGE: use the reference style (added 21 Aug 2026)

Read `references/reference-style.md` before laying out a single slide. It was
extracted from the two decks Akash named as the bar, and it is not optional.

The one rule that fixes most rejections: **accent is ink, not wallpaper.** In
the reference decks amber appears as text roughly fourteen times more often
than as a fill. Bordered tables, coloured table rows, and a tinted band on
every slide are the pattern that got a build called an obnoxious palette.

Layout is carried by small-caps headers over hairline rules, columns, numbered
rows and borderless tables. Navigation is carried by a numbered kicker on every
slide (`08 · HOW MUCH OF THE WORK`), which removes the need for dark divider
slides entirely.

## LANGUAGE: scrub the tics before shipping (added 21 Aug 2026)

Run the `llm-tic-scrubber` skill on the content file and on the built deck.
The three that have actually caused rejections here:

- The antithesis, "not X, but Y". Say the thing and drop the contrast
- Fragment stacking, "Two questions. Four builds." Write one connected sentence
- A repeated bolded label such as "In plain words:" used more than twice

Every slide title should be an **action title**: a full sentence stating the
point, which the body then proves. "Ninety out of a hundred is worse than none"
is a title. "Coverage analysis" is a label.

## CONVERT FORMULAS, DO NOT IMPORT THEM (added 21 Aug 2026)

Researching a formula and putting it on a slide is half the job. The other half
is turning it into something a product person can do in their head. Convert
every formula into a division, a count, a 2x2 or a plug-in strip, and verify
the simple version against the exact algebra before shipping it.

Four conversions that were accepted, each verified to reproduce the exact
figures: a weighted five-question score became a 2x2 on two questions; a
break-even formula became one division plus one addition; a three-term cost
formula became a table of counting a hundred cases; and a go or no-go became a
four-letter acronym using the client's own word.

## CONTENT PACKAGING (added 21 Aug 2026)

Apply the `concept-packaging` skill alongside this one. The short version:

Every concept gets four beats and nothing else: a plain one-line definition, a
concrete contrast with real values, **what you do about it**, and a sticky
handle (an analogy or a paired mental model). Beat three is the one usually
missing and it is what makes the concept the audience's rather than yours.

**Opening quiz.** Answerable from ordinary work experience, never from a
framework not yet taught. Every wrong option is a real thing they recognise, so
the reveal teaches four things at once. Name the slide where each answer
returns and close every loop. A question requiring the taxonomy you are about
to teach produces silence, which is what happened on the first attempt.

**Title length.** Georgia bold at 25pt over a 12.1 inch column wraps at about
58 characters. Wrapped titles collide with the kicker above them. Put a guard
in the builder that reports any title over 58 characters, and verify it
actually fires, because a guard silently dropped by a later edit reports a
false pass.

## VERIFY THE CLIENT'S OWN TAXONOMY BEFORE TEACHING IT

Framework labels collide. A reference document supplied for this programme
mapped P0 to P3 onto architectural layers (Context, Intelligence, Decision,
Action), while the client's own swimlane and the trainer's own delivery both
define P0 to P3 as lifecycle phases (business case, solution, delivery,
post-launch). Same labels, different frameworks.

Never blend two sources that use the same labels differently. Check the client
artefact and the delivery transcript first, teach their definition, and where a
second framework is genuinely useful, introduce it as a **separate axis that
threads through the phases** rather than as a rival meaning for the same names.

## THE DECK IS A SELF-TEACHING DOCUMENT, NOT A PRESENTATION AID (added 21 Aug 2026)

This correction supersedes any instruction to compress a deck toward a slide
budget. The deck serves three readers, and the third is the one that sets the
standard:

1. The trainer, teaching from it live
2. The learner in the room
3. **A learner opening it cold a month later, with nobody to ask**

Optimising for delivery time produced a deck that failed all three. Every
symptom traced back to compression: a quiz with the answers deferred, four
concepts crammed onto one four-column slide, concepts stated but never applied
to the running case, and headings shortened into slogans.

**Build complete, then mark the live path.** More slides carrying one idea each
beats fewer slides carrying three. State the delivery path in the chat reply,
never as a marker on a slide.

### The five rules that follow

- **Every question gets its answer slide immediately.** Question slide, then
  answer slide with the claim, the explanation, and a row per wrong option
  saying why it does not hold. A deferred answer is useless to reader three
- **One idea per slide, always.** If a slide carries four concerns, it becomes
  four slides. Dissection beats density
- **Concept slide, then applied slide.** Establish what the thing is in general,
  then work it through the running case on the next slide. Without the second
  slide the dots never connect
- **Headings name the topic.** A heading has to work as a contents entry and as
  a recall handle a month later. "The six components of an agent" is a heading.
  "Six components, no more, no less" is a slogan, and it tells a learner nothing
  about what the six are components of. Put the assertion in the lead line,
  where it belongs
- **Applied slides answer "what do I do about it"** in the concrete, using the
  case numbers, not in the abstract

## THE UNIT ANATOMY, FROM THE TUTORIAL REFERENCES (added 30 Aug 2026)

Two independent tutorial sites teaching the same concept landed on the same
nine-slot page anatomy without knowing about each other. Where a deck teaches
four or more related concepts, apply the `lesson-architecture` skill alongside
this one and build each concept as a unit of four to eight slides.

The four transfers that change a deck most:

**State the broken default before the definition.** Both references open by
saying what goes wrong without the thing being taught, in one line, before any
definition appears. That line is what makes the rest feel necessary instead of
arbitrary. It is the missing opener on most concept slides.

**Skeleton before instance, for anything with a grammar.** Show the abstract
shape with placeholders, then number its parts down the side and explain each.
Use this for syntaxes, templates, document structures, decision procedures and
canvases. Keep picture, then detail, then worked example for everything else.

**One rung per slide, and print the output.** The example ladder goes single,
then multiple, then computed, then named, then a different type, then the edge
case, and each rung introduces exactly one new thing. Every rung shows the
actual result rather than describing it. Three rungs compressed onto one slide
is the single compression failure that makes a deck useless a month later.

**Four rules, no closing paragraph.** Each concept ends on a rules slide of
three to five bullets, each a complete sentence stating one rule. That slide is
what a learner photographs, so it must survive with no surrounding text.

## THE WITNESS RULE FOR CASE DATA (added 30 Aug 2026)

Before writing any values into a running case, list every teaching point the
deck has to land, then plant one feature in the data that only that point
explains. Each such feature is a witness. Without it, the slide that needs it
produces output identical to the slide before it and the learner sees nothing.

The reference dataset is seven rows and five columns and carries five witnesses:
two rows tied on price so the second sort key visibly does something, two rows
with a missing value so the null options differ, and a quantity column inverted
against price so the computed sort reorders everything.

Run the check mechanically: for every slide showing a result, name the row or
value that makes that result different from the previous slide. A slide with no
witness is teaching nothing new.

Keep case data small enough to hand-check. A learner who can verify seven rows
against the claim starts trusting the deck.

## THE MAP SLIDE (added 30 Aug 2026)

A numbered kicker gives position but not the whole family. For any deck
covering four or more concepts, add a map slide showing every section with a
one-sentence capability promise, repeated at each section boundary with the
current section marked. Sections are named for the task, never for the
machinery, and each unit under them gets a verb-first one-liner.

Order sections for early capability rather than logical completeness. The
reference course teaches create, insert and select in section one so the learner
completes a full cycle immediately, then returns to proper design in section
three, after the absence has been felt. A complete ordering that leaves the room
unable to do anything for two sessions is the wrong ordering.

Name the earlier unit at every reuse. When a slide uses a concept taught
earlier, say which section it came from in the body text. Four words converts a
forgotten topic into a retrievable one.

## APPLICATION FIRST, CONCEPT AFTER (added 30 Aug 2026)

The default trainer move is to open with theory and arrive at the application
later. Reverse it, every time.

1. **Show the working thing first.** The whole query, the running script, the
   finished output. Complete, before it is understood
2. **Derive how it works from what was shown.** Take it apart in front of the
   room, one element at a time, against the artifact already on screen
3. **Then name the concept behind it.** The formal idea arrives last, attached
   to something the learner has already seen work

This is what the tutorial references do inside every example, and it
generalises to whole sessions. A session that opens with "let us learn what an
agent is" has spent its first fifteen minutes on something the room cannot
attach to anything.

## SLIDES THAT KEEP GETTING LEFT OUT (added 30 Aug 2026)

Four slide kinds that a concept sequence needs and that decks routinely miss.

**The unlock slide, at the front.** What a learner will be able to do by the end
that they cannot do now, and which of those matters most. Stated as capability,
not as topics covered. This is different from a learning-objectives list, which
is programme framing and stays banned: the unlock slide names an ability in the
learner's own terms.

**The anti-pattern slide.** What not to do, beside what to do, both concrete.
Where a thing is needed and where it is not. A concept taught only in its
correct use leaves a learner unable to recognise the wrong use, which is the
form the question actually arrives in.

**The connector slide.** One mental model that ties the session's parts into a
single picture, placed after the parts have been taught rather than before.

**The failure slide.** The wrong path, shown deliberately, with the error and
the trace it produces. Every concept gets one. The happy path is not what gets
asked about in an interview or hit in production.

## DECK AND CODE PARITY (added 30 Aug 2026)

Where a session has a demo code file, the deck and the file are two views of one
sequence and are built in the same segments, in the same order. When the deck
reaches tools, the code file has a tools segment. Every slide showing a result
has the code that produced it at the matching position in the file. Change one,
check the other in the same pass.

Apply the `cohort-session-kit` skill whenever the deck is one artifact in a
programme delivered by someone other than its author. The deck alone is never
the deliverable in that setting.


## STRATEGY BEFORE LAYOUT (added 31 Aug 2026, and it comes before everything above)

This skill builds a deck. It does not decide how the topic is taught. That
decision is made first, by the `lesson-strategy` skill, and this skill assumes a
strategy brief already exists: the learner's real question, the clarity outcome,
the anchor, the concept treatments and the flow.

If you were handed a raw TOC or a topic label with no strategy, stop and run
`lesson-strategy` first. Walking the TOC and dressing it is the single most
common cause of a rejected deck. The symptoms are always the same words:
"structural", "aesthetic but not glanceable", "not intuitive", "doing too much".

## DIAGRAM-FIRST IS THE DEFAULT, NOT AN OPTION (added 31 Aug 2026)

A picture is the default treatment for a concept slide. Text-in-columns is the
exception, used only when a concept genuinely has no shape. A build that reserved
diagrams for 7 of 39 slides was rejected as prioritising structure over
substance. The accepted rebuild ran 27 diagrams across 45 slides.

**Judge a draft by counting the slides a reader could still understand with the
text removed.** If that number is low, the deck is text dressed as slides.

The eight text layout patterns in `references/reference-style.md` are for the
minority of slides that are genuinely a table or a list. They are not the
workhorse. The workhorse is a hand-drawn SVG diagram that carries the idea.

## TWO ACCEPTED PALETTES, CHOSEN BY WHETHER COLOUR CARRIES MEANING (added 31 Aug 2026)

The single-accent amber-on-slate palette in `references/design-system.md` was
rejected as a default everyone recognises. Plain white-with-navy was rejected on
the same ground. Two palettes are now accepted, and the choice is made by one
question: is colour doing teaching work?

**When colour must carry category meaning** (mandatory vs optional, standard vs
gap, one build vs another), use the SAP Activate multi-colour muted set:

    white ground FFFFFF, paper FAF8F5, ink 1F2937, soft 374151, muted 6B7280
    sage green   5C7A52 on C8DDC8 / soft E8F0E6   = mandatory, standard, correct
    terracotta   B8763A on FAD9B5 / soft FBEACA   = conditional, config, cost
    purple       5B4889 on DACFE8 / soft EFE9F5   = optional
    blue         3F6B8A on CCE0EE / soft E4EEF5   = the tooling / evolved layer
    red          C0392B on F5CCD0                 = critical, fails
    Georgia titles 30, Georgia 17 card headings, Calibri 12.5 body,
    Calibri bold letterspaced small-caps kickers

The learner reads the colour and knows the category. That is the whole point,
and a monochrome deck throws it away.

**When colour would be decorative**, use the warm-sand monochrome:

    ground FBF7F0, ink 2B2620, soft 554C42, muted 857A6E, dim AFA396,
    rule E4DACA, panel F3EBDD, one teal accent 1E6B7A (dk 14505C, tint D8E9EC),
    terracotta B4623A reserved for cost, wrong, and the held case

Never use the amber-on-slate palette. Never leave a category-coded deck
monochrome.

## THE SAP ACTIVATE TEACHING MOVES (added 31 Aug 2026, the accepted method)

These seven moves, extracted from the reference decks, make a concept-teaching
deck land. Apply them per concept, not once:

1. **One real artefact decoded, not a topic list.** The whole day hangs off one
   thing the learner holds (a sheet, a document, a case). Every concept attaches
   to it. This is the anchor from `lesson-strategy`.
2. **Colour carries meaning** (see the palette above).
3. **A card per category, same shape each time**, so categories are instantly
   comparable.
4. **A "what it says vs what it actually means" decoded table**: take a thing
   they already see and reveal what is under it. The cleverest single device.
5. **A diagnostic line the learner can say** ("when asked why this is on the
   list, the answer is X, Y or Z, never *I don't know*"). They leave with words
   in their mouth.
6. **A real case with a number** per concept: a company, a consequence, a figure.
7. **A decision rule with a threshold** for every judgement, never "it depends"
   with no rule.

Plus, opening a session or an hour: **the roadmap slide** (N coloured zone
cards, each a letter, a time or phase tag, a title, three sub-bullets, and a
one-line goal footer). It shows the shape of the whole at a glance.

## READ EVERY DECISION TREE IN WORDS (added 31 Aug 2026)

A decision tree, a rule table or a 2x2 gets a companion slide that reads it as
full IF-THEN sentences: "IF the agent takes an action THEN add the autonomy
spec, because a reviewer must see what runs without a person." The diagram shows
the structure; the reading teaches the habit of walking every row instead of
eyeballing it. Never ship the diagram alone. This also means the trainer does
not have to narrate it from the whiteboard.

## SUMMARISE AFTER EVERY MAJOR TOPIC (added 31 Aug 2026)

When a major topic closes, add a slide that compresses its method into a
numbered strip the learner photographs ("the mandatory set in five moves"). One
box per step, the whole method on one row. This is the recall handle for that
topic.

## COHESION FROM ONE REPEATED CONNECTION DIAGRAM (added 31 Aug 2026)

When a deck teaches several parts that connect, draw the connection once as a
diagram (a loop, a flow, a nesting) and repeat it: at the front, at each part
opener with the current part lit, and at the close with the parts filled in.
This single device is what answers "there is no cohesiveness". A numbered kicker
alone does not segregate topics visibly enough; the repeated diagram does.

Section openers may be light slides carrying this diagram with the current part
lit. This is the one permitted exception to the no-divider-slides rule.

## BE INCREMENTAL ACROSS SLIDES, NOT WITHIN ONE (added 31 Aug 2026)

A table or a diagram built up in stages becomes several slides with the same
picture growing, not one finished slide. A five-row decision table was built as
three slides: write the actions, add the two yes/no columns, add the level
column and highlight the deciding row. Each slide introduces exactly one new
thing, and the learner watches it assemble.

## QUESTION VARIETY, ONE PER PAGE (added 31 Aug 2026)

Rotate the question format so the deck does not read as one quiz repeated:
multiple choice; TRUE / FALSE with two large lettered buttons; and IS THIS
DIAGRAM CORRECT, where a deliberately wrong artefact is shown and the room types
C or W. Build the wrong-diagram question by taking a correct one and breaking
exactly one thing (a ceiling set to the most common value instead of the
lowest). Every question gets its answer slide immediately after.

## REUSE AN EARLIER FRAMEWORK RATHER THAN INVENTING A NEW PICTURE (added 31 Aug 2026)

When a later point can be made on a diagram already taught, reuse that diagram
rather than drawing a new device. An irreversible-vs-harmful point was made by
plotting two actions onto the 2x2 the room already knew. Reuse builds recall;
a new picture every slide builds fatigue.

## BRING IN ESTABLISHED FRAMEWORKS WHERE THEY GENUINELY FIT (added 31 Aug 2026)

A senior room trusts content more when it is anchored to a standard they may
recognise. Where a real, established framework fits the topic, use it, and MARK
IT AS ESTABLISHED in a confidence line so it is not mistaken for an invention.
Two that fit agentic-artefact and solution-architecture teaching:

- **arc42**, the standard architecture-documentation template, mapped section by
  section onto whatever document set you are teaching. It reassures the room the
  set is not invented bureaucracy.
- **RACI** (responsible, accountable, consulted, informed) for who owns each
  artefact, one accountable name per row. It also answers "who signs this off"
  and any "permeable barriers" question directly.

Only bring in a framework that genuinely fits and genuinely simplifies. A
framework added because frameworks look impressive is the cardinal sin from the
top of this skill.

## AUDIT THE BUILD AFTERWARDS AND SHOW IT (added 31 Aug 2026)

After building, produce an audit in the chat reply (never in the deck): per
slide, what it is worth and whether it survives a cut; and for the whole deck,
what a reader gains. State the timing arithmetic and a ranked cut list. Absence
of this audit is treated as the work being unfinished. Also check, without being
asked: is there a chart where a proportion is the point, is every formula
discussed actually shown, is any figure the audience obviously needs missing.

## THE AUGMENTATION CEILING (added 31 Aug 2026)

When asked to expand a deck, keep every accepted slide untouched and splice new
ones in by anchor title. 30 to 35 slides is fine for a two-hour session once the
deck also works as a self-teaching document, but "not a whole lot" more. The
purpose of every added slide is that the trainer writes less on the whiteboard,
so each new slide must carry a diagram, a framework, or a summary the trainer
would otherwise have drawn live. A slide that adds only words fails this test.

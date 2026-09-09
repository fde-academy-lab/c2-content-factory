# The terrain map

Part 3 of every note carries the same picture. A learner in session 4 sees a
mostly empty map and a learner in session 26 sees a mostly filled one, and the
difference between two consecutive notes is visible at a glance.

That accumulation is the whole reason the map exists. It answers, in one
figure and without a word of explanation, the four questions every learner in
a long programme carries and almost never asks out loud: what is the whole of
this subject, how much of it do I have, where does today's thing sit, and what
is still ahead of me.

The map is built once per programme and then reused. Restructuring it halfway
through a cohort destroys the accumulation and is the one thing never to do.

---

## Building the terrain

Two bands, because every professional subject has an axis of what you know and
an axis of what you do, and learners lose the second one first.

**Band A, the craft.** The components or layers of the subject itself, five to
nine of them, ordered by dependency where the subject has one and by natural
grouping where it does not.

**Band B, the arc.** The stages of the work the learner will actually do with
the subject, start to finish, four to six of them.

Under five cells in band A is too coarse to show progress. Over nine and the
picture stops working at a glance.

### Where the cells come from, in order of preference

1. **A published standard the programme already follows.** A certification
   syllabus, a professional body's competency map, an accreditation framework.
   Cite it, do not paraphrase it, and use its own words for the cells.
2. **The programme's own module names**, if they were written as capabilities
   rather than topics.
3. **The subject's own structure**, derived and then marked in the artifact as
   the programme's construction rather than an industry standard.

Reusing beats inventing every time, because the learner has already met the
vocabulary. A new named cell has to remove confusion, not merely exist.

### Six worked terrains

| Programme | Band A, the craft | Band B, the arc |
|---|---|---|
| Agentic AI engineering | model behaviour · grounding and retrieval · orchestration · tools and actions · memory and context · evaluation and guardrails · deployment | find · integrate · engineer · launch · defend |
| Data engineering | ingestion · storage · modelling · transformation · orchestration · quality · serving | source · design · build · operate · prove |
| Software architecture | requirements · constraints · structures · crosscutting concepts · technology choice · quality scenarios · evaluation | understand · decide · design · communicate · evaluate |
| Financial analysis | statements · ratios · forecasting · valuation · capital structure · risk | gather · model · test · value · defend |
| Clinical training | anatomy · pathology · diagnostics · therapeutics · monitoring | present · assess · diagnose · treat · follow up |
| Enterprise sales | market · buyer · product · commercial terms · objection handling | prospect · qualify · demonstrate · negotiate · close |

Every one of those band A rows is the subject taken apart along its own joints,
not a generic lifecycle borrowed from somewhere else. That is the test.

---

## Three fill states

Binary coverage runs out by session twelve of a thirty-session programme.
Depth does not.

| State | Meaning | How it is drawn |
|---|---|---|
| Outlined | Not touched yet | Thin grey outline, no fill, label in grey |
| Half | Introduced, seen once, not practised | Outline in ink, half-height accent fill, label in ink |
| Solid | Worked with hands, built something, defended a choice | Full accent fill, label reversed to white |

A session moves one or two cells forward by one state. It rarely moves a cell
two states, and a note claiming it did is usually overstating what happened.
Today's cells carry a thin ink ring so the current session separates from
everything covered before it.

The legend appears once, in the first note of a cohort, and never again.

---

## What was actually covered

Three or four sentences open part 3, under a bold lead, before the figure. They
separate what was worked from what was only mentioned, and that split is what
keeps the fill states honest for the rest of the cohort. Full detail and a
worked block are in `learning-design.md`.

## The coverage line

One plain sentence under the figure. It states position, never progress
against a target.

> You have now built with your hands in four of the seven craft layers and
> been introduced to two more. The delivery arc is complete through Integrate,
> and Engineer opens next week.

Never write "you are 60% through". A percentage of a taxonomy the programme
invented is false precision, and learners notice.

---

## What was left out

Two sentences closing part 3. Name the nearest adjacent thing the session
deliberately did not cover, and say when it arrives. This stops a learner
assuming the topic is closed, and it is what makes the outlined cells mean
something.

> This session did nothing about reranking, which is what you reach for when
> retrieval returns the right ten documents in the wrong order. That is
> session 19.

Almost no study notes do this. It costs two sentences and it is one of the
reasons the note reads as written by someone who knows the whole subject
rather than by someone summarising two hours of it.

---

## The coverage ledger

The ledger is what makes the map accumulate. It lives with the programme, not
with this skill, and it is updated in the same pass that writes the note.

`coverage-ledger.md`, one per cohort:

```
# Coverage ledger, <programme>, <cohort>
Terrain locked <date>. Last updated after session 17.

| Cell | State | Sessions that moved it | What was covered |
|------|-------|------------------------|------------------|
| A1 model behaviour | solid | 3, 4, 7 | Prompting, structured output, choosing a model on cost |
| A2 grounding | solid | 11, 12, 13, 17 | Chunking, embeddings, hybrid search, measuring retrieval |
| A3 orchestration | half | 15 | First state machine built, no persistence yet |
| A4 tools | outlined | | |
| B1 find | solid | 1, 2, 6 | Discovery structure, qualifying, the decision not to build |
```

Rules for the ledger.

- Read it before drawing the map. If it is not supplied, ask once. If it is
  still unavailable, draw the map with only the current session's cells marked
  and say in the caption that prior coverage was not available.
- Update it in the same pass as the note, and hand both files back, so the
  next note starts from a correct picture.
- Never silently downgrade a cell. If a later session shows an earlier claim
  was overstated, correct it and say so in the `what was left out` paragraph.
- The last column is what makes the ledger useful to a human six months later.
  Write it as a real sentence naming specific things, never as a topic word.

---

## Pinning a session to cells

Most sessions pin obviously. The ones that do not are worth thinking about
rather than forcing.

| Session type | Typical pin |
|---|---|
| Technical build session | One or two band A cells, no band B cell |
| Method, process or consulting session | One band B cell, no band A cell |
| Project, lab or capstone sprint | Several band A cells moving to solid, plus one band B cell |
| Tool or platform masterclass | One band A cell, usually to half |
| Guest practitioner or panel | One band B cell to half, and it is honest to mark nothing in band A |
| Revision or consolidation session | No new cells, and the note says so |

A session that appears to touch six cells has almost certainly touched one
properly and mentioned five. Mark the one.

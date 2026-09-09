---
name: study-notes-builder
description: Write the study notes a learner reads after a session has finished, for any subject and any programme. Produces a markdown note and a print-ready PDF built on a terrain map that fills up session by session, one running thread carried through every concept, verified field cases, a no-writing self-check, and an ordered reading path. Use it whenever the deliverable is post-session learner material: study notes, study guides, session notes, class notes, lecture notes, revision notes, a session handout or a learner summary. Trigger it when a transcript, recording, deck, notebook or curriculum row arrives with any instruction to turn it into something for learners. Trigger it for corporate training, bootcamps, cohort programmes, university courses, certification preparation, client enablement, workshops, masterclasses and guest sessions. Use training-deck-builder instead when the artifact is taught from rather than read alone. Do not wait for the words "study notes".
---

# Study notes builder

The learner was in the room. A document that replays what they already heard
is worth nothing to them, and that is what almost every set of study notes
does. A note earns its place only by doing four things the session could not.

| The four jobs | What the note supplies that the session did not |
|---|---|
| **Place** | What was actually covered, where it sits in the subject and the programme, and which moment of the terminal outcome it is a component of |
| **Augment** | The real cases, the numbers and the history the session had no time for |
| **Consolidate** | Two hours of talking compressed into one model the learner can redraw from memory |
| **Transfer** | What this looks like in the work they are being trained for, and where it gets tested |

A section serving none of the four is padding. Cut it.

Three things make a note read as generic, and all three are structural rather
than stylistic: no running thread, no placement, and topics presented as a
list. Fix those and the writing follows.

---

## 1. Intake

Read what exists before asking anything. Search memory and past conversations
for the programme, the cohort, the running case already in use, the vocabulary
already taught and what the previous notes covered.

| Input | Status | What to do with it |
|---|---|---|
| Session transcript or recording notes | Frequently supplied, never assume | The source of truth for what was actually taught |
| Deck, notebook or slides | Sometimes supplied | What was planned, which is not the same thing |
| Curriculum row or syllabus | Usually inferable | Gives the session number, the module and the neighbours |
| Terrain and coverage ledger | Built once per programme | Gives the map its prior fill, see `references/terrain-map.md` |
| Nothing but a topic | Happens often | Build from the syllabus and drop every slot that needs the session itself |

Write the envelope in the chat reply and nowhere else: which programme, which
session, who reads it and when, what the previous note covered so the
callbacks are real, and the reading budget with the arithmetic shown.

### Reading budget

Budget the reader's minutes, not the page count. Reading runs at roughly 220
words a minute for a working adult on unfamiliar technical material, and a
figure costs about 30 seconds.

| Session length | Note size | Figures | Reading time |
|---|---|---|---|
| 60 to 90 minutes | 1,800 to 2,500 words | 4 to 6 | 10 to 13 minutes |
| 2 to 3 hours | 2,800 to 4,000 words | 6 to 10 | 15 to 21 minutes |
| Full day | 4,000 to 5,500 words | 10 to 14 | 22 to 30 minutes, and consider splitting |
| Multi-day module | One note per day | | Never one note per module |

State the reading time once at the top of the note. It is a fact about the
artifact, so it is allowed where commentary about the artifact is not.

### When a transcript is supplied

The transcript is the highest value input available, and most of its value
sits in the places people skip.

1. **Keep the trainer's own words for things.** If the trainer called the
   context window "the desk you are working on", that analogy goes into the
   note and gets extended. Swapping in a better analogy breaks the thread
   between what the learner heard and what they are now reading.
2. **Find where the room got stuck.** Repeated questions, a long silence, the
   same doubt asked twice in different words. Those topics get the most space
   regardless of how much session time they took.
3. **Record what was promised for later** and turn it into a forward hook in
   this note and a callback in the next one.
4. **Do not transcribe.** The note is not minutes and nothing in it should
   read as an account of what happened in the room.

### When nothing but a topic is supplied

Build from the syllabus and the subject. Drop every slot that depends on
knowing what was actually said rather than inventing it. A note that quietly
claims coverage the session did not deliver is worse than a shorter note.

---

## 2. The spine

Ten parts in this order, every time, so the cohort learns the shape once and
then reads for content instead of re-orienting.

| # | Part | Its job | Rough size |
|---|---|---|---|
| 1 | Header block | Session identity, the one-line promise, reading time | 5 lines |
| 2 | What you can now do | Five to seven capability sentences | 150 words |
| 3 | Where this sits | What this session covered, the terrain figure, the placement table, the coverage line, the outcome tie, what was left out | 300 words, 1 figure |
| 4 | The picture to remember | One diagram the learner should be able to redraw | 100 words, 1 figure |
| 5 | The sections | Four to six concepts, each on the unit shape | the bulk |
| 6 | Where this shows up in the work | Three situations where this decides something with a cost attached | 350 words |
| 7 | Try this yourself | The challenge and its self-check | 400 words |
| 8 | Where this gets tested | Four to six questions with model answers | 500 words |
| 9 | Glossary | Term, plain meaning, where it appeared, one example | one table |
| 10 | Go deeper | An ordered path with stated time costs | one table |

Parts 3 and 4 are what stop the note being a recap, and they are the two most
often skipped. Build them first.

Part 3 carries four things in this order, and the first and third are the ones
that get dropped under time pressure.

1. **What this session covered**, in three or four sentences, separating what
   was worked from what was only mentioned. This is the block a learner
   forwards to their manager, so it travels further than anything else in the
   note.
2. **The terrain figure**, marked for this session, with the placement table
   and the coverage line under it.
3. **The outcome tie**, one sentence naming the specific moment inside the
   programme's terminal outcome that today's content is a component of. It is
   the only place in the note allowed to say why something matters, and it
   earns that by naming a moment rather than asserting importance.
4. **What was left out**, two sentences on the nearest adjacent thing this
   session did not cover and when it arrives.

Parts 1 to 5 are in `references/section-craft.md`. Parts 6 to 10 are in
`references/close-out.md`. The reasoning under all of it, the terminal
outcome, the cohort arc and the special cases for the first and last note of a
cohort are in `references/learning-design.md`. Read that one first when
starting a new programme, and once more around the midpoint of a cohort.

---

## 3. The three rules that decide whether it reads as generic

### The running thread

Pick one artifact from the session and follow it from part 4 to the last
section. If the session taught retrieval, follow one query. If it taught
statutory interpretation, follow one clause. If it taught titration, follow one
sample. Every section shows what happens to that same artifact when the new
idea is applied to it.

This is the strongest single move available, because it turns a list of topics
into one continuous demonstration. A note without a thread reads as five
encyclopedia entries stapled together, and that is what generic means.

The test that it works: after every section the reader can answer "what
happened to the query", and the answer is different each time.

### The one picture

Exactly one figure is the picture the learner should be able to redraw from
memory a month later. It goes in part 4, it gets a name, and later sections
refer back to it by that name.

If the content cannot reduce to one picture, the session taught two things.
Say so plainly rather than inventing a diagram that merges them.

### The voice

The note is written in the handover voice: a competent colleague telling
someone who will do the work tomorrow what actually matters. It leads with the
consequence rather than the definition, names the cheap check before the
expensive fix, holds a stance, says what to skip, and admits the honest limit.
Worked pairs are in `references/section-craft.md`.

### The four devices

Four inline devices carry the augmentation. Nothing else in the note gets a
box, a rule or a label. No `Note:`, no `Tip:`, no `Remember:`, no emoji.

| Device | What it holds | How often |
|---|---|---|
| **IN THE FIELD** | A named organisation, what it actually did, one sourced number | Once per section, minimum |
| **WATCH OUT** | The failure that really happens, and the tell that it is happening | Half the sections |
| **ORIGIN** | Where the idea came from, with a date and a name | Twice per note, maximum |
| **CALLBACK** | One line naming the earlier session this rests on | Wherever a real dependency exists |

`CALLBACK` is the cheapest and most valuable of the four. It costs six words,
it forces retrieval of earlier material, and it is the reason a series of
notes is worth more than a folder of documents.

---

## 4. Adapting to the kind of programme

The spine does not change. Four things do.

| Programme type | Terrain comes from | Part 6 becomes | Part 8 becomes | Cases drawn from |
|---|---|---|---|---|
| Corporate or client training | The client's own delivery lifecycle plus the craft layers | The client room and the review | The stakeholder challenge | The client's industry |
| Bootcamp or career cohort | The job's competency map | The first ninety days on the job | The hiring interview | Companies the cohort wants to join |
| University or college course | The syllabus and the discipline's own structure | The lab, the project, the dissertation | The exam and the viva | Published research and industry practice |
| Certification preparation | The certification's published syllabus, cited as such | The situation the certification claims to certify | Exam-shaped items in the real format | The standard's own reference cases |
| Internal upskilling | The team's existing systems and processes | The next sprint or the next incident | The design review | The organisation's own history |
| Workshop or masterclass | One slice of a larger terrain, marked as a slice | The week after the workshop | The conversation with a colleague who was not there | The speaker's own domain |

Everything else, including the ten parts, the unit shape, the devices, the
challenge design and the ship gate, is the same in all six.

---

## 5. Facts, and the rule that protects the programme

Every organisation named, every number and every date is verified before it
ships. Learners repeat these claims in interviews and in front of clients.

- Search for every statistic. If one search does not confirm it, drop the
  number and keep the qualitative claim, or drop the case and find another.
- Never invent a URL. Open every link in part 10 before listing it.
- Name the source inline in a compact form, such as
  `(Stripe engineering blog, 2024)`. A learner who cannot trace a number
  cannot use it.
- Mark any framework the programme invented as the programme's own
  construction, inside the artifact, where the reader needs it. The terrain
  map in part 3 usually is one of these and it carries that marking every time.
- Never state a company case that was not confirmed. A plausible case is worse
  than no case, because it teaches the learner that these notes are decorative.

---

## 6. Build and ship

The markdown file is the source of truth. The PDF is generated from it, so the
two cannot drift.

```
<session-slug>/
  content.md          the note, written to the spine
  figures/*.svg       hand-authored, programme palette
```

    cp assets/content-skeleton.md <session-slug>/content.md
    python3 scripts/build_notes.py <session-slug>/content.md --brand "#1E6B7A"
    python3 scripts/check_notes.py <session-slug>/content.md --minutes 120

`build_notes.py` produces the styled HTML and the PDF from
`assets/template.html` and `assets/notes.css`. Pass `--brand` to set the
programme's accent colour, and `--title-suffix` for the running footer.

Deliver both files. The markdown is what gets posted in the cohort channel and
edited later; the PDF is what gets kept.

Figures are hand-authored SVG following `assets/figure-kit.md`. Mermaid is
usually available and its default styling is instantly recognisable, so use it
only for a flow too intricate to hand-author, and restyle it to the palette
when you do.

---

## 7. The ship gate

`check_notes.py` covers the mechanical half. Read the list for the half a
script cannot see, and clear both before showing the work.

| Check | Passes when |
|---|---|
| Running thread | The same named artifact appears in at least three sections |
| The one picture | One figure is named and referred to by that name later |
| Placement | The terrain figure is present, current cells are marked, the coverage line reads as a plain statement |
| Devices | Every section carries `IN THE FIELD`, and the note holds between 8 and 16 devices |
| Callbacks | At least two, pointing at different earlier sessions by number and by what they taught |
| Numbers | Every statistic carries an inline source |
| Challenge | Solvable with no writing and no code, one item drawn from an earlier session, and the key names which section to re-read for each miss |
| Tested | Every question carries what is being tested and what makes an answer weak |
| Glossary | Only terms the session actually used, each with a real example |
| Go deeper | Every link confirmed live, each with a stated time cost, ordered as a path |
| Sentences | Every bullet is a complete sentence with a verb |
| Register | No banned heading, no em-dash, no hedge opener, no closing slogan |
| Outcome tie | Part 3 names a specific moment in the terminal outcome, not the importance of the topic |
| Covered block | Part 3 separates what was worked from what was only mentioned |
| Arc | Scaffolding matches where the cohort is, per the arc table in `learning-design.md` |
| Size | Inside the word and figure budget for the session length, reading time stated once |

### Headings banned outright

`Introduction`, `Overview`, `Background`, `Key Takeaways`, `Key Concepts`,
`Summary`, `Conclusion`, `Deep Dive`, `What we learned`, `Recap`,
`Wrapping up`, `Final thoughts`, `Let us explore`.

Every heading names its topic and works as a contents entry a month later. The
assertion goes in the first line under the heading, never in the heading.
`Reranking, and why a good retriever still returns the wrong order` is a
heading. `Reranking deep dive` is a label.

---

## Reference files

- `references/learning-design.md` for the terminal outcome, the outcome tie, the cohort arc, the first and last note of a cohort, and the principle behind every element.
- `references/terrain-map.md` for building the terrain once per programme, the three fill states, the coverage ledger, and six worked terrains across different subjects.
- `references/section-craft.md` for the unit shape, the devices, the running thread and one fully worked section.
- `references/close-out.md` for parts 6 to 10, with the five challenge forms and worked examples of each.
- `assets/figure-kit.md` for SVG conventions and six ready figure recipes.
- `assets/content-skeleton.md` is the blank note. Copy it and fill it rather than starting from an empty file.

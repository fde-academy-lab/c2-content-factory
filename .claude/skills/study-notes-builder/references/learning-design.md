# Learning design

The three rules in `SKILL.md` stop a note reading as generic. This file is why
the note is built the way it is, what changes across a cohort, and what a note
must never contain.

---

## The terminal outcome

Every programme is training someone to become something. A note that connects
today's topic only to last week's topic teaches a chain. A note that connects
it to what the learner is becoming teaches a purpose, and purpose is what makes
a tired adult read the second half.

Write the terminal outcome once per programme, as a capability with a witness
attached, and store it beside the coverage ledger.

| Programme | Terminal outcome |
|---|---|
| Forward deployed engineering | Can walk into a client's problem, scope a build in a week, and defend the estimate in a room that is trying to cut it |
| Certification preparation | Can pass the exam and defend an architecture decision against a quality scenario without reaching for the slide |
| Internal data platform upskilling | Can hold the on-call pager and explain a pipeline failure to a business owner inside an hour |
| Undergraduate organic chemistry | Can propose a synthesis route for an unseen target and say where it will fail |

A terminal outcome that could describe any programme in the field has not been
written yet. The witness is what makes it real: the room, the pager, the panel,
the unseen target.

## The outcome tie

Every note carries one sentence naming the specific moment inside the terminal
outcome that today's content is a component of. It sits at the end of part 3
and it is the only place in the note allowed to say why something matters.

| Rejected | Why it fails | Written instead |
|---|---|---|
| This is a key skill for any forward deployed engineer. | Could sit in any note in any week | When a client says the pilot answers badly, the recall check is the first thing you run, and it is the difference between two days and two weeks. |
| Retrieval is foundational to the programme. | Curriculum framing, not outcome framing | In the capstone review you will defend four retrieval decisions to a panel, and chunk size is the one they press hardest. |
| Understanding this will help you in interviews. | Vague on both sides | The follow-up question after "how does RAG work" is almost always "and how would you know it was working", and that is this session. |

The tie earns its place by naming a specific moment. Without one it is
encouragement, and encouragement is cut.

---

## Naming what was actually covered

Part 3 opens with three or four sentences under a bold lead, before the figure.
They name the session, state the ground actually covered, and separate what was
worked from what was only mentioned.

```markdown
**What this session covered.** Two hours on grounding, taken end to end on the
insurance knowledge base. Chunking and embedding were built live and every
learner ran the retrieval themselves. Reranking was demonstrated once and not
built. Hybrid search was mentioned in passing and is not covered here.
```

Three reasons this small block does more work than it looks.

- It is what the learner sends to their manager when asked what the programme
  is doing, which means it travels further than any other part of the note.
- The worked and mentioned split is what feeds the fill states on the terrain
  map, so honesty here keeps the map honest for the rest of the cohort.
- Naming what was mentioned but not covered kills the quiet assumption that
  hearing a term once means holding it.

Someone who missed the session should be able to read those four sentences and
know precisely what they missed and how much of it they can recover from the
note alone.

---

## The first note of a cohort

The first note is the one everyone gets wrong, because it has nothing behind it.

- It carries the terrain legend. No later note repeats it.
- It states the terminal outcome in full, once. Later notes reference it in a
  clause.
- Its `CALLBACK` devices point outside the programme, at knowledge the cohort
  already brought in from their own work. "This rests on the SQL joins you
  already write every week" is a real callback and it does the same job:
  attaching new material to something already held.
- Its challenge has no earlier-session item, because there is no earlier
  session. It is the only note exempt from that rule.
- It may run short. A first note at 2,000 words that establishes the terrain
  cleanly is better than one padded to budget.

## The last note of a cohort

- The terrain map is nearly full, and the coverage line becomes a single clause.
- The challenge draws from four or more earlier sessions rather than one.
- The reading path points at what to read after the programme ends, which is
  the only place a note looks past the last session.

---

## The cohort arc

Scaffolding that helps in week two gets in the way by week twenty. A learner
who has built four retrieval systems does not need the library analogy, and
giving it to them slows the read and mildly insults them. This is the
expertise reversal effect and it is the single most useful thing to build into
a series of notes.

| | Early, first quarter | Middle | Late, final quarter |
|---|---|---|---|
| Picture-able example | Every section, from outside the subject | About half the sections | Rare, because the running thread carries it |
| Worked thread | Every step spelled out with values | Key steps only | The step is named and the reader completes it |
| Challenge form | Sorting bench, false statement | Trace, two-design call | Number call, and items combining two sessions |
| Callbacks | Point at prior knowledge from outside the programme | One to three sessions back | Five or more back, and across strands |
| Coverage line | Full sentence naming both bands | Short sentence | One clause |
| Reading path | Documentation and clear videos | Engineering blogs and applied papers | Papers, and one source that disagrees with the session |
| Glossary | Every new term | New terms only, with earlier ones assumed | Short, and often the terms the field uses inconsistently |

Record where the cohort is on this arc in the coverage ledger, so the arc is
followed rather than remembered.

---

## The principles, and where each one lives

Every element of the note exists because of something known about how people
learn. The useful column is the last one.

| Principle | What it says | The part that implements it | What breaks without it |
|---|---|---|---|
| Retrieval practice | Recalling beats re-reading by a wide margin | The challenge, and every `CALLBACK` | The note gets read once, feels clear, and is gone in a week |
| Spacing and interleaving | Material revisited across time and mixed with other material sticks | The one earlier-session item in every challenge | Each session is learned and forgotten in its own box |
| Generation effect | Producing an answer beats being shown one | The challenge sits before the self-check, never beside it | The reader reads the answers and believes they knew them |
| Concreteness fading | Start concrete, move to the abstract, end with the abstract applied | Move 3 concrete, move 4 the framework, move 5 the thread with real values | Either an abstraction nobody can hold or an anecdote that does not transfer |
| Worked example effect | Novices learn more from a studied example than from solving | The thread worked in full, with the values printed | Learners spend their effort on the mechanics and miss the idea |
| Expertise reversal | The same scaffold that helps a novice slows an expert | The cohort arc above | The notes feel patronising by week twenty and stop being read |
| Dual coding | A picture and words carry more than either alone, if they carry different things | Figures that show what the prose does not restate | Diagrams that decorate, and a reader who skips them |
| Extraneous load | Effort spent on the format is effort not spent on the content | The same ten parts and the same four devices in every note | The reader re-learns the document each time |
| Desirable difficulty | Some friction improves retention | The planted item in the sorting bench that fits none of the buckets | A challenge everyone passes, which measures nothing |
| Feedback specificity | Feedback that names the gap beats feedback that names the score | The pointer telling the reader which section to re-read | The learner knows they were wrong and not why |
| Prior knowledge activation | New material attaches to what is already held | Callbacks, and in the first note callbacks to their own work | Isolated facts with nothing to attach to |
| Elaborative interrogation | Asking why a thing is so deepens the trace | The `what is being tested` line on every question | Answers memorised as scripts and abandoned under a follow-up |

---

## What the note deliberately does not contain

Each of these is common, and each one is absent on purpose.

- **No learning objectives block.** Part 2 is the objectives, written as
  capabilities in the learner's own terms, without the label and without the
  verb taxonomy.
- **No summary at the end.** Re-reading a summary produces the feeling of
  knowing without the knowing. The challenge occupies that slot instead.
- **No difficulty labels** on the challenge. A label tells a learner in advance
  whether to try, and half of them will believe it.
- **No estimated mastery, no progress percentage, no badges.** Position is
  shown by the terrain map, which is honest, and a percentage of an invented
  taxonomy is not.
- **No encouragement.** The note ends at the reading path. A learner who has
  just done the challenge does not need to be told they are doing well by a
  document.

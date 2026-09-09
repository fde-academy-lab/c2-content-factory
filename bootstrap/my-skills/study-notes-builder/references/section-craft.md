# Section craft

Parts 1 to 5 of the note. Part 5 is most of the words, and it is four to six
sections, one per major concept the session taught.

---

## Part 1, the header block

Five lines and nothing else. No framing sentence, no statement of what the
note is about, no reference to what the previous session covered.

```
Session 17 · Grounding and retrieval · <programme>
Getting the right passage to the top of the list, and knowing when it is not there.
14 minute read · 8 figures
```

The second line is the promise: what the reader will be able to do, in one
sentence, in plain words. It is the hardest line in the note and it is worth
rewriting five times.

## Part 2, what you can now do

Five to seven sentences, each naming a capability rather than a topic. The
test is that each one could be checked by watching someone work.

| Rejected | Why | Written instead |
|---|---|---|
| Understand reranking | Cannot be observed | Decide whether a retrieval problem needs a better index or a second ranking pass |
| Learned about chunk sizes | A topic wearing a verb | Pick a chunk size from the shape of the source documents rather than from a default |
| Familiar with evaluation | Vague | Read a recall-at-k number and say whether reranking can help at all |

Number them. Keep them in the order the sections deliver them, so the list
doubles as a contents page without being labelled one.

## Part 3, where this sits

The terrain figure, a three-row placement table, the coverage line, and the
two sentences on what was left out. Full detail in `terrain-map.md`.

The placement table is three rows and it is worth writing carefully, because
it is the part a learner quotes back when someone asks what they are studying.

| | |
|---|---|
| In the subject | One sentence placing the topic among its neighbours |
| In this programme | One sentence on what it depends on and what it unlocks |
| In the work | One sentence on the moment in a real job where this decides something |

## Part 4, the picture to remember

One figure, one name, one paragraph. The paragraph says what the picture shows
and what the reader should be able to reproduce. Later sections refer to the
picture by its name, never as "the diagram above".

Name it after what it does. `The two-stage funnel`, `The cost triangle`,
`The state envelope`. A name that decodes itself gets used in conversation,
and a picture used in conversation has been learned.

---

## Part 5, the unit shape

Teaching a concept in a room and explaining it in a document are different
problems. A room has a trainer who can read confusion and slow down. A
document gets one shot at a tired reader. The order below is the grounded
concept unit compressed for reading.

| Move | What goes there | Length |
|---|---|---|
| 1. The break | One sentence on what goes wrong without this thing | 1 line |
| 2. The thing | One sentence on what it is, in plain words | 1 line |
| 3. The picture-able example | Something outside the subject that the reader can see instantly | 2 to 3 sentences |
| 4. The shape | A figure, a small table, or a numbered procedure. The framework lives here | 1 figure |
| 5. The thread, worked | The running artifact put through this concept, with real values | 4 to 6 lines |
| 6. In the field | The device. A named organisation, what it did, one sourced number | 2 to 3 lines |
| 7. The catch | `WATCH OUT`, or `CALLBACK`, or both where they earn it | 1 to 2 lines |

Move 1 is the one people skip and it is the one that makes everything after it
feel necessary rather than arbitrary. Write it before anything else in the
section.

Move 3 must not be the course's central case. The clearest example teaches the
concept; the connected example proves it lands in their world, and that is
move 5's job.

### The heading

| Rejected | Why | Written instead |
|---|---|---|
| `Reranking deep dive` | A label that tells a reader nothing | `Reranking, and why a good retriever still returns the wrong order` |
| `Retrieval is not enough` | Antithesis, and it asserts in the heading | `What retrieval hands you, and what it does not` |
| `Understanding chunking` | The word understanding does no work | `Chunking, and the size that decides your answer quality` |

---

## The four devices, written out

Devices are blockquotes with a bold label, so the markdown reads correctly on
GitHub and the build script styles them in the PDF.

```markdown
> **IN THE FIELD** · <Organisation> <did this specific thing> and <this
> happened>. (<source>, <year>)

> **WATCH OUT** · A reranker that improves your demo and does nothing in
> production usually means the first stage never retrieved the right document
> at all. The tell is recall at 50 already being low, because reordering
> cannot recover a document that was never in the list.

> **ORIGIN** · The two-stage pattern is older than language models. Web search
> has used a cheap recall pass followed by an expensive precision pass since
> the late 1990s, for the same reason: scoring every document properly is
> unaffordable.

> **CALLBACK** · This rests on the chunking decision from session 12. A
> reranker cannot recover meaning that chunking already cut in half.
```

- `IN THE FIELD` needs a real organisation doing a real thing, searched and
  confirmed. A plausible case is worse than no case.
- `WATCH OUT` names the failure **and the tell**. A failure with no tell is a
  warning rather than something the reader can act on.
- `ORIGIN` needs a date and a name. Vague history is filler.
- `CALLBACK` names the session by number and by what it taught, and there are
  at least two per note pointing at different earlier sessions.

Nothing else in the note gets a callout.

---

## The running thread

One artifact, followed from part 4 to the last section, picked from the
session itself so the learner recognises it.

| Session subject | A thread that works |
|---|---|
| Retrieval and reranking | One question asked against one document set, tracked through every stage |
| State machines | One ticket moving through one graph, with the state printed at each node |
| Scoping and estimating | One client request, from the sentence said on the call to the line in the contract |
| Evaluation | One failing output, traced from the test that caught it back to the cause |
| Statutory interpretation | One clause, read four ways by four canons |
| Titration | One sample, carried through preparation, measurement, error and reporting |
| Financial modelling | One line item, followed from the statement into the forecast and the valuation |

The thread works when a reader can answer "what happened to it" after every
section and the answer is different each time. The thread has failed when it
appears in section one, disappears for three sections, and returns at the end.

Change the thread at most once in a note, and only to prove transfer.

---

## A fully worked section

Written as it would appear in a real note. The `IN THE FIELD` device is left
as a slot on purpose, because putting an unverified company number inside a
reference file is exactly the habit this skill exists to stop. In a real note
that slot is filled from a search and cited inline.

The running thread is one question, `does my policy cover a cracked
windscreen`, asked against a four thousand document insurance knowledge base.

---

### Reranking, and why a good retriever still hands back the wrong order

Retrieval that finds the right document and puts it in position nine is
retrieval that failed, because the model only reads the top few. Reranking is
a second pass that reads the question and each candidate together and reorders
them by how well they actually answer it.

Think about a library catalogue that returns forty books with your keyword on
the spine. The catalogue matched words. A librarian who opens each one and
reads a page can tell you which three are worth carrying home. The catalogue
is fast, cheap and slightly wrong. The librarian is slow, expensive and right.
You want both, in that order.

![The two-stage funnel](figures/05-two-stage-funnel.svg)

*Figure 5. The retriever runs once over everything and is cheap. The reranker
runs only over what survives and is expensive. The cost of the second stage is
set entirely by how many candidates the first stage passes forward.*

Three decisions sit inside it, and only three.

1. How many candidates the first stage passes forward, usually between 20 and 100.
2. How many the reranker keeps, usually between 3 and 10.
3. Whether a candidate below a score threshold is dropped rather than ranked
   last, which is what stops the model answering from a document that does not
   contain the answer.

**The thread.** The question goes to the vector store, which returns 50 chunks.
The correct chunk, from the glass and windscreen annexe, comes back at position
31, because that annexe never uses the word policy and the embedding drifted
toward thirty chunks of general policy language. The reranker reads all 50
against the question and moves the annexe chunk to position 1. The knowledge
base did not change. The embedding model did not change. The document was
always there, in the wrong place.

> **IN THE FIELD** · [Organisation, what it built, the measured effect, source
> and year. Searched and confirmed before this note ships.]

> **WATCH OUT** · A reranker that improves your demo and does nothing in
> production usually means the first stage never retrieved the right document
> at all. The tell is recall at 50 already being low, because reordering
> cannot recover a document that was never in the list.

> **CALLBACK** · This rests on the chunking decision from session 12. A
> reranker cannot recover meaning that chunking already cut in half.

---

### What the worked section is demonstrating

| Move | Where it is |
|---|---|
| The break | The first sentence, before any definition |
| The thing | The second sentence |
| Picture-able example | The library, outside insurance and outside the course |
| The shape | The figure plus the three decisions |
| The thread worked | The paragraph with position 31 in it |
| In the field | The device |
| The catch | `WATCH OUT` and `CALLBACK` |

That section is about 400 words. Five of them plus the surrounding parts land
inside the 2,800 to 4,000 budget with room for the figures.

---

## The handover voice

Register rules stop a note sounding wrong. They do not make it sound like
anyone. The note is written in the handover voice: a competent colleague
telling someone who will do the work tomorrow what actually matters, in the
tone they would use standing at a desk rather than presenting from a stage.

Six markers, each with the version that gets written by default and the version
that carries the voice.

**1. Lead with the consequence, not the definition.**

- Default: "Reranking is a second-stage model that reorders retrieved candidates by relevance to the query."
- Handover: "Retrieval that finds the right document and puts it at position nine is retrieval that failed, because the model only reads the top few."

**2. Name the cheap check before the expensive fix.**

- Default: "To improve retrieval quality, consider adding a reranking stage."
- Handover: "Measure recall at fifty before you buy anything. If the document was never in the list, a reranker cannot find it and you will have spent a week discovering that."

**3. Hold a stance and state it flatly.**

- Default: "There are various approaches to chunk sizing, each with tradeoffs."
- Handover: "Fixed-length chunking is the wrong default for structured documents. Split on the structure the document already has, and only fall back to length when it has none."

**4. Say what to skip.**

- Default: "Several evaluation frameworks are available for retrieval systems."
- Handover: "You need two numbers to start: recall at k, and whether the cited passage actually contains the answer. Everything else in the evaluation literature can wait until those two are stable."

**5. Use a real number instead of a qualifier.**

- Default: "Passing too many candidates to the reranker can significantly increase cost."
- Handover: "The second stage costs roughly what the first stage forwards. Going from 20 candidates to 200 is a tenfold bill for a gain you can usually measure in the second decimal place."

**6. Admit the honest limit.**

- Default: "This approach works well in most production scenarios."
- Handover: "This holds while your documents are prose. Tables and forms break it, and nobody in the field has a clean answer for tables yet."

### What the voice is not

- Not a lecturer. It never explains why it is about to explain something.
- Not a cheerleader. It never tells the reader that a topic is exciting,
  powerful or a game changer, and it never congratulates them.
- Not documentation. Documentation is complete and neutral; this is selective
  and opinionated, and the selection is the value.
- Not a transcript. It never reports what happened in the room.

The test: read a paragraph aloud. If it sounds like something a person would
actually say to a colleague, it passes. If it sounds like something read from
a slide, rewrite it.

---

## Register

The note is read by working adults, several of whom are more experienced than
the trainer in their own field.

- Every sentence is complete. No clipped fragments, no telegraphic lines, no
  slogan endings.
- No sentence exists only to introduce the next sentence.
- Plain words before formal terms, and the formal term introduced after the
  reader has met the problem that needs it.
- Second person means the learner, always.
- No teaching machinery on the page: no learning objectives, no "in this
  section we will", no facilitation notes, no explanation of why the note is
  built the way it is.
- The reading time at the top is the only line about the artifact that is
  allowed, because it is a fact rather than commentary.

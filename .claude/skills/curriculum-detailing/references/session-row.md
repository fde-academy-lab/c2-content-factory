# The session row

One block per session in the detailed curriculum file. The topic and the
timeline come from the TOC and are not changed here. Everything else is
decided here. `scripts/check_detailing.py` parses this exact shape.

## The grammar

```
## S<nn> · <session title as one full sentence saying what the learner can do after it>

Week: <n>
Block: <2h | 3h | day>
Band: <early | middle | late>
Narrative: <one sentence> | provenance: <researched | copied | invented | hybrid> (<from what>)

### Ideas
1. <decision sentence> | depth: L<1-4> | competencies: <n, n> | status: <new | revisited from S<nn> L<n> | variant of idea <n>>
2. ...

### Terms
- <term> (after <the problem it names>)

### Prerequisites
concepts: <list, or none>
first-use tools: <list, or none>

### Continuity
covered before: <sub-topic L<n> at S<nn>; ...> or none
do not re-teach: <list with the one-line recall permitted> or none
spine case: <world> | state: <every value already decided>
fresh cases: <list>
case studies: <company>, <number>, <source> (checked: <yyyy-mm-dd>)
basics budget: <n> min
revisited at: <S<nn> (L<n>); ...> or none

### Reference pack
video: <url> | checked: <yyyy-mm-dd> | job: <what it gives> | why: <one line>
article: <url> | checked: <yyyy-mm-dd> | job: <...> | why: <...>
repo: <url> | checked: <yyyy-mm-dd> | job: <...> | why: <...>       (or: not applicable, judgement topic)
architecture: <url> | checked: <yyyy-mm-dd> | job: <...> | why: <...>
interview: <url> | checked: <yyyy-mm-dd> | level: L<n> | why: <...>

### Transfer
question: <the question this topic gets asked as, in the room's world>
follow-up 1: <why this over the obvious alternative>
follow-up 2: <what happens when it breaks>
return question: from S<nn> (L<n> to L<n>): <the earlier transfer question, one level up>

### Hands-on
mid-session: <exercise shape, capped at 15 min>
take-home: <harder than the mid-session set>
```

Rules the checker enforces are in the script. Rules it cannot check:

- The title is a full sentence about what the learner can do, never a topic
  label
- The narrative varies across sessions. Read five rows in a row and they should
  not open the same way
- The ideas are in teaching order, and the first working thing sits inside the
  first fifteen minutes

## Worked example

The world is Client Zero, business unit Hopscotch, an FDE Academy anchor. The
reference pack is left as placeholders on purpose: references are verified on
the day the row is built and never carried in a template. The checker will
flag every placeholder, which is the intended behaviour.

```
## S07 · Decide when a support bot needs to read your documents and build the smallest version that does

Week: 3
Block: 2h
Band: early
Narrative: A Hopscotch support agent answers the same eleven questions forty times a day, and every answer sits in a 300-page wiki nobody opens. | provenance: hybrid (application-first shape copied from the structural reference; the Hopscotch desk invented)

### Ideas
1. Decide whether a wrong answer comes from the model not knowing or the model not being told | depth: L2 | competencies: 3, 5 | status: new
2. Cut a document into pieces a model can be handed without losing the sentence that matters | depth: L2 | competencies: 3, 6 | status: new
3. Choose how many pieces to hand over, and what it costs to hand over too many | depth: L1 | competencies: 3, 4 | status: new
4. Read a bad answer and say which of the three steps above produced it | depth: L2 | competencies: 8 | status: new

### Terms
- retrieval (after the wiki-nobody-opens problem)
- chunk (after the sentence-split-in-half failure)
- top-k (after the too-many-pieces cost)

### Prerequisites
concepts: what a prompt is and its three parts; what a token is and that a context window has a limit
first-use tools: none

### Continuity
covered before: prompt anatomy L2 at S03; tokens and the context limit L1 at S02
do not re-teach: prompt anatomy (one-line recall: instruction, context, question)
spine case: Client Zero, Hopscotch support desk | state: 11 recurring questions, 40 a day, 300-page wiki, 4 minutes per answer today, one agent at $6 an hour
fresh cases: an open-book exam where you may bring one page; a restaurant menu you cannot memorise
case studies: <company>, <number>, <source> (checked: <yyyy-mm-dd>)
basics budget: 12 min
revisited at: S11 (L3); S19 (L4)

### Reference pack
video: <url> | checked: <yyyy-mm-dd> | job: progression and the two illustrations the room already finds easy | why: <one line>
article: <url> | checked: <yyyy-mm-dd> | job: the plain-words definition and the opening pain | why: <one line>
repo: <url> | checked: <yyyy-mm-dd> | job: the minimal working shape and the two most-reported failures | why: <one line>
architecture: <url> | checked: <yyyy-mm-dd> | job: the components and the boundary where retrieval quality stops being the problem | why: <one line>
interview: <url> | checked: <yyyy-mm-dd> | level: L2 | why: <one line>

### Transfer
question: Your support bot answers wrongly one time in five. Do you retrieve better or train more, and how do you know which?
follow-up 1: Why does a fine-tune not fix a stale fact?
follow-up 2: What breaks first when the wiki grows from 300 pages to 30,000?
return question: from S03 (L1 to L2): you have a prompt with the right instruction and the wrong answer, which of its three parts do you change first?

### Hands-on
mid-session: read four bad answers and sort each into not-known, not-told, or told-too-much
take-home: the same desk with a 3,000-page wiki; recompute the pieces handed over and the cost, and say which idea changed
```

Four ideas, three terms, band early with first encounters at L1 and L2, the
first working thing inside the basics budget, every continuity line present,
the two follow-ups in the standard shapes, and the return question one level up
from S03. The reference pack is the only incomplete part, and it is incomplete
because it is not yet built.

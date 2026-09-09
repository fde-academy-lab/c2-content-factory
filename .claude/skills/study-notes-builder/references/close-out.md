# The closing half

Parts 6 to 10. This is where most study notes collapse into a bullet list of
links and a paragraph of encouragement. It is also where the learner decides
whether the note is worth keeping.

---

## Part 6, where this shows up in the work

Three situations, each one a moment where the topic decides something with a
cost attached. Money, time, rework or risk. A situation with no cost attached
is an illustration, not a situation.

Written as a table, one row per situation.

| What you are looking at | What you check first | What it costs to get wrong |
|---|---|---|
| A pilot answers well on the demo set and badly on the client's real questions | Whether the right passage is in the candidate list at all, before touching the model | Two weeks rebuilding an index that was never the problem |
| The client asks for citations on every answer and the retrieval returns whole pages | Whether chunk boundaries fall on section boundaries in their source format | Citations that point at the right document and the wrong paragraph, which loses the room in a review |
| Latency doubles after adding a second ranking pass | How many candidates the first stage forwards, since the second stage cost scales with it | A per-query cost that only appears once real traffic arrives |

The first column is written as something the reader can picture happening to
them. The third column is what makes the section land, and it is the column
that gets left vague. Put a number, a duration or a named consequence in it.

Adapt the framing to the programme, using the table in `SKILL.md` section 4.
For a university course the third column is the mark lost or the experiment
repeated. For certification preparation it is the exam item failed and why.

---

## Part 7, try this yourself

The constraints are strict and they are what make it get done: no writing, no
code, no environment, solvable in under ten minutes, and checkable by the
learner alone. Anything requiring a keyboard will not be attempted by a
working adult at eleven at night.

Every challenge carries **one item drawn from an earlier session**. That single
rule turns a set of notes into a spaced retrieval system, and it costs one
item. Mark that item only in the answer key, never in the question, so the
learner has to notice it is not from today.

### The five forms, rotated

Do not use the same form twice in a row. Record which form the last note used.

**1. The sorting bench.** Six items, three buckets, place each one.
Plant one item that cannot be placed at all, because it is an outcome rather
than an instance. That single planted row teaches the distinction better than
any explanation.

> Place each of these six retrieval failures into: fix the index, fix the
> chunking, fix the ranking. One of them belongs in none of the three.
> a) The right document is at position 31 of 50.
> b) The right sentence is split across two chunks and neither makes sense alone.
> c) The right document is not in the top 200 at all.
> d) Answers are correct but the citation points at the wrong paragraph.
> e) Users say the system is unhelpful.
> f) Adding a second ranking pass changed nothing.

**2. The two-design call.** Two designs shown side by side. Pick which one
costs more, breaks first, or needs the thing taught today. The answer key
explains the mechanism rather than announcing the winner.

**3. The trace.** A flow drawn as a figure, with values at each step. Say
where the output first goes wrong. This is the strongest form for anything
sequential, and it is the only one that needs a figure.

**4. The false statement.** Four statements, three true, one subtly false.
The false one must be false for a reason taught today, not for a reason of
general knowledge, and it must be plausible enough that a careless reader
would sign it.

**5. The number call.** Three numbers given. Say what decision they force.
Best for anything with a threshold in it. Tune the numbers so the answer lands
on a memorable anchor rather than an arbitrary one.

### The self-check

Placed after the challenge, under a heading that names it plainly. It carries
three things per item and the third is the one that makes the challenge worth
setting.

| Element | What it does |
|---|---|
| The answer | One letter or one word |
| The reasoning | One or two sentences on the mechanism, never just a restatement |
| The pointer | Which section to re-read if this one was missed |

The pointer turns a quiz into a diagnostic. Write it as
`Missed this one? Section 3 is the one to re-read.` and name the section by
its heading, not its number alone.

Optionally add one line before the answers inviting the reader to note how
confident they were on each item before looking. It costs a sentence and it is
one of the better-evidenced study habits.

---

## Part 8, where this gets tested

Four to six questions. Four elements each, and the second and fourth are the
ones that make this section worth more than a list of questions.

```
**Q.** <the question as it would actually be asked, in the asker's own register>

*What is being tested:* <one line on the underlying judgement, not the topic>

**A model answer.** <80 to 140 words, first person, spoken rather than
written, carrying one number or one named tradeoff. It should be sayable out
loud in about forty seconds.>

*What makes an answer weak here:* <one line naming the specific weak move,
such as reaching for the expensive fix before checking the cheap diagnosis>
```

Adapt the source of the questions to the programme, using the table in
`SKILL.md` section 4. Hiring interviews for a career cohort, exam-shaped items
in the real format for certification preparation, the stakeholder challenge
for corporate training, the viva question for a university course.

Two rules that hold across all of them.

- The model answer is spoken language, not written language. Read it aloud. If
  it cannot be said in one breath per sentence, rewrite it.
- At least one question has no clean answer, and the model answer says so and
  then commits anyway. Every real interview and every real review contains one
  of these, and a note that only shows tidy questions has not prepared anyone.

---

## Part 9, the glossary

Four columns. Only terms the session actually used. A glossary that includes
terms the learner has not met is a dictionary, and nobody reads a dictionary.

| Term | In plain words | Where it appeared | An example |
|---|---|---|---|
| Recall at k | The share of the answers you needed that showed up in the top k results | The section on why reranking sometimes does nothing | Of ten questions with a known answer document, seven had it inside the top 50, so recall at 50 is 0.7 |

The fourth column is the one that gets skipped and it is the one that makes the
glossary teach rather than define. Use a real value from the note's running
thread wherever possible, so the glossary reinforces the thread instead of
introducing a new example.

Order the terms in the order they appeared in the note, not alphabetically.
Alphabetical order is for reference works that people arrive at from outside;
this one is read straight through by someone who just read the note.

---

## Part 10, go deeper

An ordered path, not a list of links. Four to seven entries, each with a
stated time cost, each opened and confirmed live before it ships.

| Order | Source | Kind | Why this one | Time |
|---|---|---|---|---|
| Start here | <title>, <author or channel> | Video | It shows the two-stage funnel being built and run, so the shape from part 4 becomes concrete | 14 min |
| Then | <title>, <organisation> | Documentation | The parameter names and defaults you will actually type | 10 min |
| If you want the depth | <title>, <authors, year>, <venue> | Paper | The original result and the honest limitations section | 40 min |
| For a different angle | <title>, <author> | Blog post | A working engineer explaining why they removed it again | 8 min |

Rules that make this section trustworthy.

- Every link is opened and confirmed. A dead link in a learner document is
  noticed immediately and it costs the whole note its credibility.
- The `why this one` column is the point of the table. It says what the source
  does that the others do not, in the reader's terms. Never write
  "a good overview".
- One video maximum for most notes, two if the topic is visual. Choose for
  clarity and pace over production value, and name the channel.
- Include at least one source that disagrees with, complicates or walks back
  the position taught in the session, and say that is what it does. A reading
  list that only confirms the session is marketing.
- Prefer primary sources: the documentation, the paper, the engineering blog
  of the organisation that built the thing. Aggregators and content farms are
  never listed.

---

## The last line

There is no closing paragraph, no encouragement and no summary. The reading
path is the last thing on the page, and the note stops.

If the programme has a fixed place where questions go, one line naming it may
sit under the table. That is operational information the reader needs, and it
is the only thing allowed after part 10.

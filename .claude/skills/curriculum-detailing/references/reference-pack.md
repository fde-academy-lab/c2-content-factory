# The reference pack

Building a sub-topic blind from its label produces the two detailing failures.
Popular resources are popular because they are easily understood, and they
reveal the natural progression and the illustrations that already work.
Engineering resources reveal the depth. Interview questions reveal what the
session has to make answerable. Research all three before the ladder is fixed.

## Two different things, both called references

| | The structural reference lock | The reference pack |
|---|---|---|
| Scope | One whole family of concepts, a course | One sub-topic |
| Count | One written source and one video source, locked | Five slots per sub-topic |
| Job | Copy the SHAPE: philosophy, register, progression | Source the CONTENT: progression, illustrations, depth, interview level |
| Reader | The builder only | The builder, and then the learner as further reading |
| When | Before drafting anything, by the lock ritual | Per sub-topic, before that sub-topic's ladder is fixed |
| Set where | `lesson-architecture`, `build-contract` | This skill |

The lock stays at two sources because more than two conflict on structure. The
pack can hold five per sub-topic because it is not being copied for structure.
Never let a pack item replace the structural reference. Never let the
structural reference be the only source of content.

## The five slots

| Slot | What it gives | What to extract | Do not |
|---|---|---|---|
| **1 Popular video**, well illustrated | The progression a large audience found easy, and the pictures that made it easy | The order it teaches in, the one or two illustrations that carry the idea, the analogy it uses | Copy the artwork. Borrow the visual idea and redraw it in the deck's own system |
| **2 Article or blog**, one or two | Relatable framing, the plain-words definition | The opening pain it uses, the definition in one sentence, any number it cites with its source | Quote it. Paraphrase, and cite |
| **3 Repository or implementation** | The real shape of the code, and the failure modes in its issues | The minimal working example, the setup steps, the two most-reported failures | Use it as the demo file. The demo file is built in the world, in the deck's order |
| **4 Architecture diagram or engineering write-up** | Components, boundaries, and where things break at scale | The component list, the boundary that matters, the number that changes the design | Put the diagram on a slide. Redraw the components in the deck's system |
| **5 Interview questions in the wild** | What the session has to make answerable, and at what level | Three to five questions, each tagged L1 to L4, and the follow-ups interviewers actually ask | Take the question banks' model answers as correct. Verify each against slots 3 and 4 |

A sub-topic that is pure judgement (a way of deciding, not a mechanism) may
have no meaningful repo. Say so on the row rather than filling the slot with
something irrelevant. Every other slot is filled or marked to be found.

## The protocol

1. Search for each slot. Popular first, because popularity is the evidence of
   being understood
2. Fetch every candidate and read it. A search snippet is not a reference
3. Keep one per slot (two for articles). Prefer the one whose progression
   matches the depth target for this session
4. Record on the row: the URL, the date checked, the job it does, and one line
   on why this one over the alternatives
5. Extract what the slot gives, into the ladder. The pack that does not change
   the ladder was not used

## Verification rules

These exist because a hallucinated reference is worse than none. A learner who
follows a dead or wrong link stops trusting the whole pack.

- **A URL from memory is never a reference.** Every URL is fetched on the day
  it is added, and the date is written on the row
- **If it cannot be verified, the slot says "to be found".** Never fill a slot
  to make the row look complete
- **Tool-specific references carry the version they document.** A tutorial for a
  library two major versions ago is a trap, not a resource. The stack turns over
  inside a year and a stale reference has already taught one cohort the old
  manual way of doing something the library now does for them
- **Deprecation check on every slot 3 and 4 item** for a tool topic: is the API
  it shows still the current one. Note the answer on the row
- **Numbers cited from a reference carry the reference.** A figure on a slide
  with no source is a claim the trainer has to defend without help
- **Re-verify each cohort.** A pack verified for the last cohort is a pack to
  re-check, not to reuse. Re-checking is minutes; a broken link in front of a
  room is a session

## What the pack changes in the ladder

The pack is research, and research that does not change the plan was
decoration. After the five slots are filled, the ladder should show:

- An order of ideas that matches the one the popular video found easy, unless
  there is a stated reason to differ
- At least one illustration idea per idea, redrawn in the deck's system and
  attributed as an idea borrowed rather than an image copied
- A depth target for each idea that is at least the level the interview
  questions demand by the session where the idea returns
- A gotcha drawn from the repository's issues or the architecture write-up,
  which is where real failures are documented
- A case study with a number, sourced from slot 2 or 4, dated

## Further reading, for the learner

The pack doubles as the learner's reading path, in this order: the video, then
the article, then the repository, then the architecture write-up, and the
interview questions last with the model answers withheld until the session has
been delivered. The study notes and the cheat sheet carry the same list, so a
learner meets one set of sources, not three.

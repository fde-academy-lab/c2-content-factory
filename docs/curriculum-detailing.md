# Curriculum Detailing

Project knowledge for the layer between a table of contents and a session kit: how deep each sub-topic goes, what the room already knows, which case to carry, what to read first, and which interview question each session has to make answerable. Companion to `training-content-build-manual.md`, which owns the pipeline, the artifact set and the unit. This file owns the detailing gate inside that pipeline.

Confidence marks: **[settled]** is a rule proven on delivered work, **[proposed]** is a construction written here and open to rejection, **[established]** is published research cited as such, **[open]** is unresolved.

---

## 1. The layer that is always missing

A table of contents fixes two things and they are sacrosanct: the topics and the timeline. Every training has one. What it never fixes is everything underneath a topic row.

| The TOC says | The TOC never says | Who pays |
|---|---|---|
| Week 3, session 7, retrieval | How deep. Name it, use it, explain why, or handle it breaking | The trainer, who guesses, and the room, which gets whichever the trainer is comfortable with |
| Two hours | How many ideas two hours can hold before the room stops holding them | The room, which leaves with eight half-ideas |
| The topic | What the room already knows, what not to repeat, where to start | The trainer, who re-teaches session 3 for twenty minutes because nobody said it was closed |
| The topic | Which case carries it, which simpler cases are free to use, which company to cite | The trainer, who invents a fresh domain, and the learner, who now has three worlds to hold |
| The topic | Which video, article, repo and diagram it was built from, and what to read after | The learner, who searches alone and lands on a tutorial two versions old |
| The topic | Which interview question the session has to make answerable | The learner, six months later, in the interview |

Detailing is the act of filling every one of those cells for every session, before the session kit is built. It runs after the strategy brief and the map, and before any artifact. The skill `curriculum-detailing` carries the procedure and a checker; this file carries the knowledge and the reasons.

---

## 2. The two overestimations

Both come from building a session blind from its topic label. Both are overestimations of the room. The first is far more common.

| Failure | What it looks like | Why it happens | The tell in the plan |
|---|---|---|---|
| **Too many sub-topics in a day** | Eight ideas in two hours, a term for each, none reaching a worked example. Overwhelmed room, nothing retained | Sub-topics counted as headings, not as things a mind has to hold. Coverage anxiety | More than four decision sentences in a two-hour block |
| **Ten thousand feet** | The right topics at the right times, each described rather than taught. No numbers, no failure, no steps. Underwhelmed room, calls it gyaan | The timeline was honoured and depth was never set, so the safe altitude won | A sub-topic with no worked example carrying real values and no gotcha |

The second is rarer and more expensive, because the schedule looks fine on paper and nothing was learned. Both are caught by the same two instruments: count the ideas, set the depth.

---

## 3. The load budget

### The rule **[settled]**

In a session of about two hours, more than four new ideas plus a bunch of jargon overwhelms the room. Below two ideas, described rather than worked, underwhelms it.

### What counts as an idea

An idea is anything that needs its own unit, and a unit is anything that unlocks one decision the learner could not make before. Count decision sentences, never headings.

| Counts | Does not count |
|---|---|
| A concept needing its own grounding, example, framework and worked case | A sub-step inside a framework already being taught |
| A framework or formula the learner will apply | A variant of an idea already present, taught as a one-slide difference |
| A decision with a threshold | A term on its own. Terms ride on ideas |
| A failure mode that changes what the learner does | A tool command, once the tool is established |
| A tool used for the first time (a prerequisite and a load at once) | A one-line recall of an earlier session |

### The caps

| Block | New ideas | New terms | Basics budget | Status |
|---|---|---|---|---|
| Two hours | 4 | One per idea, each after its problem | 15 minutes | [settled] |
| Three hours | 5 | Same | 22 minutes | [proposed], scaled |
| Full day | Three blocks, one of them practice with no new ideas, so 8 at most | Same | 45 minutes across the day | [proposed], consistent with one activity every 45 minutes and a build slot |

### Over the cap

Never shrink the units to fit. In order of preference: **defer** the idea to the session where it is naturally needed (most over-full sessions contain one idea that belongs two sessions later), **demote** it to a variant taught as a difference and give it its own unit when it returns, or **split** the session with its own narrative and its own first working thing.

### Starting from scratch without dwelling on basics

Both are required and they stop conflicting once the mechanism is named. From scratch means no prior knowledge of the topic is assumed. Not dwelling means the basics are taught through the first application while taking it apart, never as a preamble, inside the basics budget, and anyone who needs more gets the pre-read before and the weekly remedial task after. The first working thing appears inside the first fifteen minutes.

A session that spends forty minutes on basics did not start from scratch. It started slowly, and the half of the room that knew the basics has already left.

### What is established and what is not

The four-idea cap is a rule from delivered rooms, not derived from research. It sits comfortably with the established finding that working memory holds about four chunks (Cowan, 2001, revising Miller's seven plus or minus two). Cognitive load theory (Sweller, 1988 onward) is the established frame: the load intrinsic to the material, the load added by presentation, and the load spent on understanding. Detailing cuts the second so the room has capacity for the third. Present the cap as the course's rule and the theory as the reason it is plausible, never the other way round.

---

## 4. The depth target

### Four levels **[proposed]**, named to decode themselves

| Level | The learner can | The material must contain | Interview shape it answers |
|---|---|---|---|
| **L1 Name it** | Recognise, define, say where used and why | The pain, grounding, clearest example, crux line | What is X and where would you use it |
| **L2 Use it** | Run the steps on a clean case and get the right answer | Numbered steps, one worked example with values, the spine-case slide | Given this, what do you do |
| **L3 Explain why** | Derive from first principles, say why it has this shape, say why it fails | The strip, the derived framework, the gotcha, the anti-pattern | Why does it work, why this shape, why does it fail |
| **L4 Handle it breaking** | Diagnose live, choose between alternatives with a threshold, design with it | The failure slide, the deliberate failure with its trace, the decision rule | It broke like this, what do you check first. What would make you choose the other option |

This is content depth. The `build-contract` depth dial (Direct, Shaped, Programme) is process depth. Do not use one word for both.

### How the level weights the ten-slot unit

Every major concept still runs the full unit. The level decides where the minutes go.

| Slot | L1 | L2 | L3 | L4 |
|---|---|---|---|---|
| 1 The pain | full | full | one line | one line |
| 2 Ground it | full | short | recall | recall |
| 3 Strip to first principles | skip | one line | full | full, and the room does it |
| 4 The clearest example | full | full | short | recall |
| 5 The framework | presented | presented | derived | derived by the room |
| 6 The steps | shown | full | full | full |
| 7 One worked example | shown | full | full | learner completes it |
| 8 Apply to the spine case | short | full | full | full |
| 9 The gotcha | one line | short | full | full, plus a second failure |
| 10 Close | crux only | crux and steps | all three | all three plus the two follow-ups |

### Four rules

1. **The first encounter is never L3 or L4.** Depth without foundation is ten thousand feet in disguise: it sounds deep and lands as gyaan
2. **A revisited idea rises at least one level.** If it cannot rise, it is a one-line recall, not a revisit
3. **Every core idea reaches L4 before the course ends.** Core means the ideas the final quarter's transfer questions depend on. Name them at the map stage
4. **Depth is set by where the room is, not where the trainer is.** A trainer comfortable at L4 teaches L4 to an L1 room unless the row says otherwise

---

## 5. Rising with the course

Static depth is futile. A room that has built four of something no longer needs the library analogy, and giving it to them slows the session and mildly insults them. That is the expertise reversal effect **[established]** (Kalyuga, Ayres, Chandler and Sweller, 2003), and it is the single most useful thing to build into a series.

The arc uses the same three bands as the study notes, so the two artifacts move together.

| | Early, first quarter | Middle | Late, final quarter |
|---|---|---|---|
| First encounter | L1 or L2 | L2 | L2, with L3 in the same session for the confident half |
| Revisit | Rises one | Rises one | Reaches L4 for every core idea |
| Example order | Clearest first, spine case second | Spine case first, clearest as a one-line recall | Spine case only, plus a second world for transfer |
| Question form | Answerable from ordinary experience | Needs a framework from two sessions back | Combines two strands, or asks what would make the opposite choice right |
| Guidance | Full worked example, every value shown | Complete the missing step | Build from a brief, trainer reviews |
| Failure content | One gotcha, named | The gotcha and how to read the trace | Two failures, learner diagnoses one live |
| Case studies | Company, number, consequence | Company, number, what they changed | Company, number, and one source that disagrees |

The guidance row is the worked-example-to-completion-to-problem sequence **[established]** (Sweller and Cooper, 1985, and the completion strategy that followed). A course that keeps early-band guidance in its final quarter has trained the room to wait for the worked example, and that room fails the interview question that starts with a blank page.

### The grilling cadence

Depth is built by being questioned repeatedly, one level higher each time.

- Every session's starter quiz carries one **return question**: a transfer question from an earlier session, asked one level up
- Early questions are answerable from experience. Middle questions need a framework from two sessions back. Late questions combine two strands
- The return question does three jobs at once: spaced retrieval, a backward hook, and a live reading of whether the room actually rose

| First asked | Returns as |
|---|---|
| L1: what is retrieval, where would you use it | L2: your bot answers wrongly one time in five, retrieve better or train more |
| L2: retrieve better or train more | L3: why does a fine-tune not fix a stale fact |
| L3: why does a fine-tune not fix a stale fact | L4: the wiki grew to thirty thousand pages and answers got worse, what do you check first |

---

## 6. The reference pack

### Research before the ladder, never after

Building a sub-topic blind from its label is what produces both overestimations. Popular resources are popular because they are easily understood, so they reveal the natural progression and the illustrations that already work. Engineering resources reveal the depth. Interview questions reveal what the session must make answerable. Research all three, then write the ladder, and let the research change it. Research that did not change the plan was decoration.

### Two things called references, kept apart

| | The structural reference lock | The reference pack |
|---|---|---|
| Scope | One family, one course | One sub-topic |
| Count | One written, one video, locked | Five slots |
| Job | Copy the shape: philosophy, register, progression | Source the content: progression, illustrations, depth, interview level |
| Reader | The builder | The builder, then the learner as reading path |
| Rule that holds it | More than two conflict on structure | Five do not conflict because nothing is copied for structure |

Never let a pack item replace the structural reference. Never let the structural reference be the only source of content.

### The five slots

| Slot | Gives | Extract | Never |
|---|---|---|---|
| **1 Popular video**, well illustrated | The progression a large audience found easy, and the pictures that made it easy | Its teaching order, the one or two illustrations that carry the idea, its analogy | Copy the artwork. Borrow the visual idea and redraw it in the deck's own system |
| **2 Article or blog**, one or two | Relatable framing, the plain-words definition | Its opening pain, its one-sentence definition, any number it cites with source | Quote it. Paraphrase and cite |
| **3 Repository or implementation** | The real shape of the code and the failures in its issues | The minimal working example, setup, the two most-reported failures | Use it as the demo file. The demo is built in the world, in the deck's order |
| **4 Architecture diagram or engineering write-up** | Components, boundaries, where it breaks at scale | The component list, the boundary that matters, the number that changes the design | Put the diagram on a slide. Redraw |
| **5 Interview questions in the wild** | What must be answerable, at what level | Three to five questions tagged L1 to L4, and the follow-ups actually asked | Trust question-bank model answers. Verify against slots 3 and 4 |

A pure judgement topic may have no meaningful repo. Say so on the row rather than filling the slot with something irrelevant.

### Verification, because a hallucinated reference is worse than none **[settled]**

- A URL from memory is never a reference. Every URL is fetched the day it is added, and the date is on the row
- If it cannot be verified the slot says "to be found". A slot is never filled to make the row look complete
- Tool-specific references carry the version they document. The stack turns over inside a year, and a stale tutorial has already taught one cohort the old manual way of doing something the library now does for them
- Deprecation check on every repo and architecture item for a tool topic, with the answer on the row
- Every number on a slide carries its source, or the trainer defends it alone
- Re-verify each cohort. Minutes to re-check, a session to lose

### What the pack changes

After the five slots are filled the ladder should show: an idea order matching the one the popular video found easy unless a reason is stated; at least one illustration idea per idea, redrawn; a depth target at least as high as the interview questions demand by the session where the idea returns; a gotcha drawn from the repository's issues or the architecture write-up, which is where real failures are documented; and a case study with a number, sourced and dated.

The pack doubles as the learner's reading path, in this order: video, article, repository, architecture, interview questions last with answers withheld until after delivery. Study notes and the cheat sheet carry the same list, so the learner meets one set of sources.

---

## 7. The narrative

Before writing any ladder, step back and decide the one narrative that makes depth, breadth, hands-on and the interview question fit in a single arc rather than four tracks running beside each other. One sentence: a Tuesday morning at the airline, one passenger, six options, and nobody can rank them.

Four sources, and the row records which:

| Source | Meaning | Mark |
|---|---|---|
| Researched | The narrative exists in the reference pack and is adapted | Cite the source |
| Copied | The structural reference already does this and only the subject changes | Name the reference |
| Invented | Built here | Mark as a construction |
| Hybrid | Any combination | Name the parts |

It cannot be static across topics. A course whose every session opens the same way reads as a loop. Vary the shape and let the subject pick it. The ingenuity of the whole craft sits here: the packaging is what makes depth and breadth both fit, and it has to be found afresh per session.

---

## 8. The continuity block

This is what the trainer opens first, and what every curriculum omits. It is why a trainer with ninety minutes of preparation does not know where to start, and why the room hears session 3 again for twenty minutes.

| Line | Content |
|---|---|
| Covered before | Each earlier sub-topic this session depends on, the depth it reached, the session it reached it in |
| Do not re-teach | What is closed, with the one-line recall permitted |
| Spine case, current state | The world, and every value already decided in earlier sessions |
| Fresh cases | Simpler cases free for this session's clearest examples |
| Case studies | Real companies with a number and a dated, verified source |
| First-use tools | Every tool or environment used for the first time |
| Basics budget | Minutes allowed, fifteen at most per two-hour block |
| Revisited at | Where each of this session's ideas returns and at what level |

The detailed curriculum is the source of truth. The trainer notes front matter carries the extract for that session, copied by `cohort-session-kit`. When trainers change every two weeks, this block and the spine case are the only continuity that survives, and both survive only if they live in the content.

---

## 9. Interview skill is job skill

The skill that clears an interview overlaps almost exactly with the skill that does the job. Interviewers probe nine things, and every one of them is also what the work asks on an ordinary day.

| # | Competency | Built by | Level | When |
|---|---|---|---|---|
| 1 | What you have done | Build weeks, projects, the spine case carried end to end | L2 to L4 | Every build week, the capstone |
| 2 | Depth of understanding | The strip, the derived framework | L3 | Middle onward |
| 3 | Clarity on concepts | The pain, grounding, clearest example, crux line | L1 to L2 | Every session |
| 4 | Breadth | The map, the spiral across tools, the comprehensive exercises | L1 across many | Grows with the course |
| 5 | Connecting the dots | Backward hooks, the connector slide, the return question, two-strand exercises | L2 to L3 | Middle onward |
| 6 | Inner working | Skeleton before instance, how the machine processes it, the repo in the pack | L3 | Middle onward |
| 7 | Why it happens | Derive the number, why this shape | L3 | Middle onward |
| 8 | Why it fails | The gotcha, the anti-pattern slide, the deliberate failure with trace | L3 to L4 | Middle, weighted late |
| 9 | Handling failure | The failure slide, diagnose-first exercises, a second failure late, the decision rule | L4 | Late |

Two course-level checks: all nine are advanced before the course ends, and the final quarter weights 6 to 9. Competency 1 is advanced only by building, so a course without build weeks cannot satisfy it and should say so. Record coverage as a matrix, sessions by competencies. An empty column is a gap. A column marked only early is a competency introduced and never deepened.

Every session row names a transfer question in the room's own world, the two follow-ups that recur on every topic (why this over the obvious alternative, and what happens when it breaks), and the sixty-second answer. The answer is spoken, so it lives in the trainer notes under Ask, in the study notes as a model answer, and on the cheat sheet as the crux line. It never becomes a written exercise item.

In a certification module the same ladder reshapes the L3 and L4 questions into exam-style items and the mini-assignment shaped like the real written task. In a client programme they become the stakeholder challenge. The nine competencies do not change. Only the room the learner has to say them in changes.

---

## 10. The session row

One block per session. The topic and the timeline come from the TOC and are not changed. Everything else is decided here, in a fixed shape the checker parses. The full grammar and a worked example are in the skill's `references/session-row.md`.

```
## S07 · <full sentence: what the learner can do after this session>
Week · Block (2h | 3h | day) · Band (early | middle | late)
Narrative: one sentence | provenance: researched | copied | invented | hybrid
### Ideas         numbered, each with depth L1..L4, competencies, status (new | revisited from Sxx Ly | variant)
### Terms         one per idea at most, each "(after <the problem it names>)"
### Prerequisites concepts; first-use tools
### Continuity    the eight lines above
### Reference pack five slots, each with URL, checked date, job, why
### Transfer      question; follow-up 1; follow-up 2; return question (from Sxx, one level up)
### Hands-on      mid-session (15 min cap); take-home (harder)
```

The checker flags: over the idea cap, terms exceeding ideas, a first encounter at L3 or L4, a revisit that did not rise, placeholders or missing dates in the pack, missing continuity lines, a basics budget over the cap, fewer than two follow-ups, no return question, no provenance.

---

## 11. Challenges already seen, and what each one taught

Every rule above was paid for. The evidence, so the rules are not mistaken for preference.

| What happened | The rule it produced |
|---|---|
| A 73-slide deck for a two-hour room lost a fifth of itself undelivered | Count ideas, not slides. Build complete for the cold reader, mark the live path in the chat reply |
| A sponsor interrupted at minute five to say the lifecycle framework was unfamiliar; the room also did not know two other assumed concepts | The continuity block names what is covered and at what depth. The row states what the room does not know |
| A framework the whole session hung on was taught from scratch at minute one because the room did not know it, while the deck had it at slide 41 | Prerequisites are a level of the curriculum. First-use frameworks are prerequisites too |
| About 28 minutes of a delivered session was content on no slide, all of it asked for by the room | The reference pack's interview slot tells the builder what the room will ask. Improvised content that generated discussion gets scripted next time |
| The same question was asked twice in one session | Every "this is hard" gets "here is why" on the same slide. A repeated question is a missing slot 3 |
| A five-minute activity ran twenty-two minutes and ate the close | Activities run to a hard timer, and the basics budget is a number on the row |
| A learner said the first two months went to Python and basic ML | The basics budget, and starting from scratch through the first application rather than a preamble |
| A library was taught the old manual way after the library had automated it | Tool-specific references carry their version and a deprecation check, re-verified each cohort |
| "On paper it looks fine, then it disconnects, we wait two or three weeks and get frustrated again" | Continuity lives in the content: the spine case state and the revisit pointers on every row |
| A cohort's central complaint was no structure and no clarity, and a mid-programme pulse check scored clarity 3.1 out of 5 | The map, the depth target, and a row per session that a learner can read as a promise |
| A trainer from a famous employer, given no supplied structure, was rated 3.75; a strong interviewee talked well and taught badly | The fixed core is two thirds of the session and the row is what the fixed core is measured against |
| An advanced room with no structure had its sessions derailed by debates | Depth targets set for the room, an L3 variant for the confident half, never a parallel track |
| A 3,785-word explainer was rejected as verbal diarrhoea | Ten thousand feet and too many ideas are both verbosity. Fewer ideas, each to a worked example with values |

---

## 12. Blind spots on this layer

Named honestly. The first three are the ones most likely to bite next.

| # | Gap | The call **[proposed]** |
|---|---|---|
| 1 | No detailed curriculum exists yet for any running programme. Every session so far has been detailed inside the session build, which is where the two overestimations enter | Detail one full programme end to end before building its next session, and build the session from the row |
| 2 | The reference pack needs live web access at build time. In a project without it, the slots will be filled from memory, which is the exact failure the verification rules exist to stop | When search is unavailable, every slot reads "to be found" and the chat reply says so. Never a URL from memory |
| 3 | Depth targets and the interview matrix are set by the builder alone. A trainer who disagrees has no channel | Trainer preparation includes reading the row and disputing any depth target before the session, in the same ninety minutes |
| 4 | The three-hour and full-day caps are scaled from the two-hour rule, not measured | Measure the next full day against its transcript and revise the numbers |
| 5 | "Core ideas reach L4 before the course ends" depends on core being named at the map stage, and the map does not yet have a field for it | Add a core mark to the map's unit one-liners |
| 6 | The return question needs an earlier session's transfer question to exist. Session one has none | Session one's return question comes from the pre-read or the baseline diagnostic |
| 7 | A learner who joins late or misses a session breaks the rising arc for themselves | The study notes and the cheat sheet gap variant are the catch-up path; the row's "covered before" line tells them what to read |
| 8 | Nothing says how the detailed curriculum is shown to learners. A row full of depth targets and reference URLs is a builder's document | The learner sees the map, the session title, the transfer question and the reading path. The rest stays with the trainer |
| 9 | **[open]** Whether the idea cap is per trainer-delivered content or per session including the trainer's free third | Count against the fixed core only, and let the trainer's third add at most one idea |

---

## Appendix. The gate, in the manual's pipeline

Detailing is gate 5 in the pipeline in `training-content-build-manual.md`. Its output is the detailed curriculum, one row per session, with prerequisites as one of its lines rather than a separate gate. Its rejection cost if skipped is the two overestimations, discovered live.

Skill routing: `curriculum-detailing` runs after `lesson-strategy` and the `lesson-architecture` map, and before `cohort-session-kit`. It is built and not yet installed until uploaded.

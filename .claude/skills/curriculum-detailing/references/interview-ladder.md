# The interview ladder

The skill that clears an interview overlaps almost exactly with the skill that
does the job. Interviewers ask about what a candidate has done, how deep their
understanding goes, how clear they are on concepts, how broad they are, whether
they can connect the dots, whether they know the inner working, why something
happens, why it fails, and how they handle failure. Every one of those is also
what the job asks on a Tuesday.

So the curriculum builds them on purpose, on a schedule, and the session row
says which ones each idea advances.

## The nine competencies

| # | Competency | Built by | Depth level | Unit slots | When in the course |
|---|---|---|---|---|---|
| 1 | What you have done | Build weeks, projects, the spine case carried end to end | L2 to L4 | 8 | Every build week; the capstone |
| 2 | Depth of understanding | The strip to first principles, the derived framework | L3 | 3, 5 | Middle onward |
| 3 | Clarity on concepts | The pain, the grounding, the clearest example, the crux line | L1 to L2 | 1, 2, 4, 10 | Every session, every idea |
| 4 | Breadth | The map, the spiral across tools, the comprehensive exercises after every two and four sections | L1 across many ideas | Map, recall spine | Grows with the course |
| 5 | Connecting the dots | Backward hooks, the connector slide, the return question, exercises that combine two strands | L2 to L3 | 8, 10, recall spine | Middle onward |
| 6 | Inner working | The skeleton before the instance, how the machine processes it, the repository in the pack | L3 | 3, 5, 6 | Middle onward |
| 7 | Why it happens | Derive the number, why this shape | L3 | 3, 5 | Middle onward |
| 8 | Why it fails | The gotcha, the anti-pattern slide, the deliberate failure with its trace | L3 to L4 | 9 | Middle onward, weighted late |
| 9 | Handling failure | The failure slide, the diagnose-first exercise, the second failure in late sessions, the decision rule with a threshold | L4 | 9, 10 | Late |

Competencies 3 and 4 are built from the first session. Competencies 6 to 9 are
what separate a candidate who studied from one who understands, and they need
the foundation first. A course that reaches for them in week one produces
learners who can recite failure modes they have never seen.

## The course-level check

Two rules, checked at the map stage and again after detailing:

1. **All nine are advanced before the course ends.** Competency 1 is advanced
   only by building, so a course with no build weeks cannot satisfy it and
   should say so
2. **The final quarter weights 6 to 9.** If the late sessions are still building
   3 and 4, the course has stayed at L1 and L2 and the room will fail the
   interview question that starts with "why"

Record the coverage as a matrix: sessions as rows, the nine competencies as
columns, a mark where the session advances it. An empty column is a gap. A
column marked only in early sessions is a competency that was introduced and
never deepened.

## Transfer question shapes, by depth level

The transfer question on every session row is the question this topic actually
gets asked as, in the room's own world. The shape changes with the level.

| Level | Shape | Example on retrieval |
|---|---|---|
| L1 | What is X and where would you use it | What is retrieval and when would a support team need it |
| L2 | Given this situation, what do you do | Your support bot answers wrongly one time in five. Do you retrieve better or train more |
| L3 | Why does this work, why is it built this way, why does it fail | Why does a fine-tune not fix a stale fact, and why does retrieval fix it |
| L4 | It broke like this, what do you check first. What would make you choose the other option | The wiki grew to thirty thousand pages and answers got worse. What do you check first, and at what size would you stop retrieving and start routing |

## The two follow-ups

Interviewers go three questions deep. A learner who answers level one and not
level two sounds shallow, whatever they know. Two follow-ups recur on almost
every topic, so every row carries both:

1. **Why this over the obvious alternative.** Answered by the decision rule with
   its threshold. If the session has no threshold, the learner will say "it
   depends" and stop
2. **What happens when it breaks.** Answered by the gotcha and the failure
   slide. If the session has no failure, the learner has never seen one

The sixty-second answer to the transfer question assembles from three parts
already in the unit: the first-principles strip gives why the thing exists, the
decision rule gives the trade-off, the gotcha gives what breaks. A topic whose
answer cannot be assembled from those three has a hole in one of them.

## Where the answers live

The transfer answer is spoken, so it is never a written exercise item. It goes
in three places:

- The trainer notes, under **Ask**, with the sixty-second model answer
- The study notes, as interview questions with model answers
- The cheat sheet, as the crux line

Written exercises stay selection-only and fifteen-minute capped. The interview
skill is built by being asked out loud, repeatedly, one level higher each time.

## In a certification or client programme

The same ladder holds with the transfer question reshaped. In a certification
module the L3 and L4 questions become exam-style items and the mini-assignment
shaped like the real written task. In a client programme they become the
stakeholder challenge: why this and not that, and what happens when it goes
wrong on our data. The nine competencies do not change. Only the room the
learner has to say them in changes.

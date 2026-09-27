# CONTENT DOCTRINE
## How teaching content for this programme behaves

The content carries the session. Trainers rotate week to week, arrive with varying quality, and cannot be relied on to supply structure, industrial examples, or rigour. Content that assumes a strong trainer produces a weak cohort.

---

## 1. THE BUSINESS PROBLEM COMES FIRST

Every teaching day opens on a business question in a stakeholder's words, trains the thinking an
analyst uses to break that question down, and only then teaches the technique that produces the
answer. **The technique exists because the question demands it.**

**Why.** The 10 September 2026 curriculum review named the failure precisely: a day whose notebook
runs but whose thinking is missing teaches code rather than analysis. Engineers are hired to solve
business problems, and business problems arrive in business words. The job is translation, and
interviews test exactly that: a scenario, your translation, several approaches, and why you chose
yours.

**Rules.**

- The day's row opens with the scenario in the stakeholders' words and the questions they are asking.
  A day pack that opens on a technique has not been built from the row.
- The thinking is written down before any tool appears, and it is what the learner keeps. The Week 1
  canonical example is the revenue tree: revenue is customers, times orders per customer, times items
  per order, times price per item, less discounts. A learner who can state that tree, pick the branch
  the data points at and defend the choice has done data analysis, whatever the tool was.
- The day closes on what the learner would actually send the stakeholder, with its caveat.
- The same business question gets a harder answer with a stronger tool as the programme runs, which
  is how a learner comes to see analysis, machine learning, deep learning and generative AI as
  successive answers to one problem rather than as separate subjects.

**Three threads run the length of the programme**, and two or three of them are open at any time.
Growth is the spine; Trust and Cost are what a skeptic in the room raises against every Growth answer.

| Thread | The question it keeps asking |
|---|---|
| Growth | Where does growth come from, and how do we get more of it? |
| Trust | Can we believe this number? |
| Cost and risk | What does a wrong call cost, and who bears it? |

The threads are fixed in `07_Client_Zero.md` section 3, week by week.

---

## 2. THE CONNECTED SCENARIO (CLIENT ZERO)

One fictional company, one domain, one entity model, established on Day 1 and carried across the programme. FDE Academy calls this client zero.

**Why.** Concept clarity comes from depth on stable ground. Learners at this level cannot absorb a new concept and a new domain in the same session. Switching from Amazon to Uber to Swiggy between examples resets the learner every time.

**Rules.**

- The same entities and the same underlying data are re-expressed as the toolset grows. A list of dictionaries in plain Python becomes a DataFrame in Pandas becomes tables in SQL becomes features in a model becomes a corpus in RAG.
- The teaching moment sits in the contrast. Show what the previous tool could not do, then show the new tool doing it on the same data.
- Module 1, Weeks 1 to 4, teaches in Kalpa Retail only. The review was explicit that switching domain
  in the first module is unfair to a room still learning the tools.
- Every concept gets two examples. Example A runs on the Kalpa Retail spine. Example B comes from
  another Kalpa unit and appears only after the concept has landed, to test transfer. From Week 5 the
  second example rotates in a fixed order: Financial Services first, where error costs are asymmetric,
  then Health, then Connect.
- Build weeks use a different unit from the teaching that preceded them, on real messy data relabelled
  into that unit: Build 1 in Kalpa Health, Build 2 in Kalpa Financial Services, Build 3 in Kalpa
  Connect. That rotation is deliberate training for the interview question the review quoted: "you are
  in a health company now, tell me how you would apply this to our data."
- Kalpa's stakeholders are named and fictional, and a trainer says them from memory. Naming a
  fictional CEO is the opposite of naming a trainer, which never happens in a student file.

**Worked example of the spiral.** Missing values.

| Stage | Tool | Same problem, new expression |
|---|---|---|
| Week 1 to 2 | Plain Python | Loop over a list of dictionaries, find the missing keys, count them, decide what to do |
| Week 2 to 3 | Pandas | `.isna()` on the same records as a DataFrame, then show the operation that plain Python could not do without twenty lines |
| Week 3 to 4 | SQL | The same records as a table. `IS NULL`, `COALESCE`, aggregate with and without the nulls. Show what changes when the data does not fit in memory. |
| Week 5 onward | ML | The same nulls as an imputation decision, with the model outcome attached to each choice |

The learner sees one problem four times and four tools. Four separate example domains would have taught one tool each.

---

## 3. APPLICATION BEFORE THEORY

Show the working thing and its output. Break it down. Then name the concept behind it.

The pattern comes from how good SQL and API tutorials teach: the query is written first, then decomposed, then extended one element at a time. Starting with "let us learn what an agent is" loses the room.

Sequence for any new concept:

1. Working artifact on screen, output visible
2. "What did you just see happen"
3. Decompose the artifact, one element at a time
4. Name the concept and give the minimum theory that makes the decomposition make sense
5. Break it deliberately
6. Rebuild it in a second shape

---

## 4. ONE NEW DIFFICULTY AT A TIME

Never teach a concept and real data together. Real data brings volume, encoding problems, multiple simultaneous defects. Teaching a concept on real data means teaching two things at once and both fail.

Concepts use small, clean, client-zero data. Real data (Kaggle scale, messy) belongs in build weeks, after the concept is established.

The same rule applies to tools. Establish VS Code, the notebook, the connection, and the run loop before the session that depends on them. A session that spends thirty minutes on environment setup has lost thirty minutes of teaching.

---

## 5. DELIBERATE FAILURE

Every session includes a state that breaks on purpose: a wrong output, a stack trace, an anti-pattern that runs but produces the wrong answer.

Interviews ask what happens when things go wrong. They rarely ask what happens when things go right. A learner who has only seen working code cannot answer either the interview question or the debugging task.

Each failure carries four parts: the broken artifact, the exact error text or wrong output, how to read it, the fix.

---

## 6. REFERENCE-ANCHORED PRODUCTION

Before generating anything for a module, lock two sources: one written and one video.

More than two sources produce drift. Their structures conflict, the generated result averages them, and the progression breaks. One good written tutorial that already solves the sequencing problem is worth more than ten scattered references.

Once locked, generation runs against the reference: same philosophy, same progression, same level of hand-holding, adapted to this programme's client zero and toolset.

Sources are found independently by more than one person, compared, then locked. The locked source is recorded against the module in the curriculum map.

---

## 7. THE 60/40 SPLIT

Roughly 60 to 70 percent of a session is fixed by the content. The remaining 30 to 40 percent is trainer discretion.

Fixed: the concept sequence, the demo artifacts, the deliberate failure, the exercises, the quiz.

Discretionary: additional examples, the trainer's own war stories, extra practice, how long to dwell on a sticking point.

A trainer given full freedom skips the rigour. A trainer given no freedom delivers flatly. Coverage of the fixed portion is tracked against the day sheet.

---

## 8. DECK BEHAVIOUR

Decks are visual and thin. Trainer narration lives in the trainer notes, never on the slide.

Slide sequence for a teaching session:

| Slide | Job |
|---|---|
| The business scenario | The stakeholder's words and the questions they are asking. This is slide one, and it is never cut. |
| The thinking | How the scenario breaks down before any tool is opened, usually as one drawing |
| Outcome | What the learner can do by end of day, and what that unlocks next |
| Environment | Tools used today, stated up front so setup problems surface before the demo |
| The artifact | The working thing, with its output |
| Decomposition | Element by element, one slide per element, built progressively |
| Foundations | The minimum theory the decomposition needs. Nothing more. |
| Difference between | Only where two things are genuinely confusable (model against runtime, embedding against index, agent against workflow) |
| Mental model | One diagram that ties the parts together |
| Reading the failure | The error, the trace, how to read it |
| Anti-pattern | What people do that breaks, and why |
| Decision framework | When to use this, when not to |
| Recap and self-check | Questions the learner answers without notes |

Slides carry no text walls, no stock imagery and no decorative diagrams. If a slide has no job, delete it.

---

## 9. EXERCISE TYPES

Mid-session exercises must be small enough to finish in 15 minutes and easy enough that most of the room succeeds. Their job is engagement and immediate reinforcement.

Use these forms:

- Trace the flow
- Predict the output
- Find the mistake
- Fix the broken code
- Fill the blank line or the blank function call
- Match the following
- Choose from options and justify
- Compare two approaches and say when each wins

Guided exercises are trainer-led, step by step, students mirroring on their own machines.

Unguided exercises are attempted in session with no hints. The solution is released at close of session, and the same exercise continues as the take-home assignment.

Fast finishers get a stretch task. Learners who stall get a smaller prerequisite task built from the same material. Both are prepared in advance, not improvised.

---

## 10. INTERACTIVE ARTIFACTS

Some concepts land only when the learner manipulates them. Build these as HTML pages or spreadsheets that run without an API key.

Concrete builds for this curriculum:

| Artifact | Teaches | Shape |
|---|---|---|
| Model picker | Algorithm selection | Dropdowns for data size, label availability, interpretability need, latency budget. Output names the candidate algorithms and the reason each qualifies or fails. |
| SQL execution tracer | Logical execution order | Query on the left, the intermediate result set after FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY on the right |
| Chunking sandbox | RAG chunking | Paste a document, move sliders for chunk size and overlap, see the chunks and the places where a boundary cut a sentence in half |
| Threshold playground | Precision, recall, F1 | Fixed prediction set, one threshold slider, watch the confusion matrix and the three metrics move together |
| Token and cost estimator | Context budgeting | Paste a prompt, pick a model, see tokens and cost |
| Agent trace reader | Agent debugging | A real ReAct trace with tool calls shown. The learner marks the step where the agent went wrong and says why. |
| Retrieval bake-off | Retrieval strategy | Fixed corpus, fixed query, three strategies with their results. Learner ranks them and defends the ranking. |
| Failure injection notebook | Diagnosis | A cell that works, then a cell that breaks. The learner diagnoses from the trace alone before seeing the fix. |

The learner fills the criteria and the artifact responds. Telling someone how to pick a model does not stick. Making them pick one does.

---

## 11. ENVIRONMENT

VS Code, single environment, no exceptions.

- Python and ML: `.ipynb` notebooks. Markdown cells carry the recap, the setup steps, and diagrams. A learner who opens the notebook cold can run it.
- SQL: `.sql` files against a live Postgres instance, run from VS Code through the database connector.
- GitHub Codespaces removes local installation. A trainer needs a GitHub account and a browser.

Demo code files are built progressively, in the same order as the deck. Setup steps sit above the code so any learner can run the file without help.

---

## 12. WHAT IS PLANTED IS NEVER ANNOUNCED

Every dataset the cohort touches is generated from one seed, and every defect in it is a witness for
exactly one teaching point. **Students are never told what is planted.**

The witness list is TRAINER material. It appears in the curriculum row's client-zero column, which is
labelled TRAINER ONLY, and in the trainer notes, and nowhere a learner can read.

**Why.** The room is supposed to find the bulk order by sorting, the fourteen duplicated rows by
reconciling against Finance, and the confounder by comparing segment against aggregate. A slide that
says "we planted 14 duplicate rows in Q1" has spent the lesson before the room has had it. The
discovery is the skill; the defect is only the occasion for it.

**Rules.**

- The student-facing artifacts describe the data's shape and provenance, never its defects.
- The trainer note says exactly what is planted, what the room should find, and what to do if nobody
  finds it inside the time the agenda allows.
- A learner who asks directly is answered with the question back: what would you check?
- After the discovery, naming it is fine and useful. Before it, it is a spoiler.

---

## 13. THE INTERVIEW THREAD IS AN OUTPUT, NOT A GARNISH

Every teaching day carries an interview angle: the questions this day equips a learner to answer,
questions only, tagged by how often the Indian market at the 0 to 3 year band actually asks them.

| Tag | Meaning |
|---|---|
| `[S]` | A staple, asked everywhere |
| `[F]` | Frequent in GCC and product screens |
| `[SV]` | A service-major screen opener |
| `[D]` | A differentiator, where a strong candidate separates |

The tagging is this programme's own calibration and is labelled as such wherever it is printed, so
nobody mistakes it for an employer's published data.

**Rules.**

- The row carries questions. Answers are written at the detailing phase, inside the day pack, never
  in the curriculum row, because an answer in the row becomes the answer everybody gives.
- The Saturday recap paper is drawn from the week's question set and nowhere else.
- A question that the day does not actually equip a learner to answer does not belong on the day.

---

## 14. WHAT COHORT 1 PROVED

The doctrine above exists because of what happened last time. The detail is in `04_Cohort1_Learnings.md`. The short version: students said there was no structure, trainer quality did not track with trainer cost or trainer pedigree, and in a six-month programme a first month that does not grip cannot be recovered later.

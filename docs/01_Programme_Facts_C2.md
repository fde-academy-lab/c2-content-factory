# PROGRAMME FACTS
## PG Diploma in AI-ML and Agentic AI Engineering, IIT Gandhinagar, Cohort 2

This file carries the facts that rarely move, written by hand, and the facts that can still move,
rendered from `data/programme/facts.yaml` by `python3 scripts/sync_programme.py` into the blocks
marked `sync`. Edit the facts file or the workbooks, never a rendered block, then run the sync.

Every movable fact carries a status. A `locked` or `stated` fact may appear in any artifact. A
`tentative` fact reaches a STUDENT file only with the word tentative beside it. A `proposed` or
`open` fact never reaches a STUDENT file, and an `open` one reaches no artifact at all. Roles only
in this file: the repository is public.

<!-- sync:status -->
Facts as of 01 Oct 2026: calendar locked on 21 Sep 2026; IITGN faculty sessions 30 planned, 0 confirmed; client zero v2.2 locked and v2.3 proposed; evaluation locked; 12 decisions open.
<!-- /sync:status -->

---

## SHAPE

| Fact | Value |
|---|---|
| Award | A PG Diploma from IIT Gandhinagar, senate-approved, with regular IITGN alumni status for every graduate. |
| Week 0 | An in-person baseline week from Monday 28 September to Saturday 3 October 2026. It carries no marks and sits outside the 510 hours. |
| Teaching | Twenty weeks from Monday 5 October 2026 to Saturday 20 February 2027, six days a week, residential on the IITGN campus. |
| Cohort | 35 students in nine build-week groups (stated in the handover of 27 September). |
| Intake | 0 to 3 years of experience. |
| Role tracks | GenAI or AI Engineer and Agentic AI Engineer are primary; Data or Business Analyst and entry-level Data Scientist are supported; Forward Deployed Engineer is a fitment layer; Computer Vision is excluded and never claimed. After ME2 each learner declares a primary and a supported track, which decides the job descriptions they are prepared against. |
| Placement | Every student is made interview-ready and is brought three to five opportunities. There is no placement guarantee, and no artifact implies one. |
| Client | Kalpa Group, fictional, locked at v2.2 in `07_Client_Zero.md`. |

## CALENDAR

Locked on 21 September. The day-by-day view, with every day's folder slot, is
`docs/programme/calendar.md`.

<!-- sync:calendar-summary -->
| Week | Mon to Sat | Kind | Module | Focus | Holidays | IITGN sessions |
|---|---|---|---|---|---|---|
| 0 | 28 Sep to 03 Oct 2026 | baseline | none | Week 0: baseline and the engineer's way of working | Fri 02 Oct, Gandhi Jayanti | none |
| 1 | 05 Oct to 10 Oct 2026 | teaching | M1 | Data analysis foundations | none | none |
| 2 | 12 Oct to 17 Oct 2026 | teaching | M1 | Data manipulation at depth | none | 3 (0 confirmed) |
| 3 | 19 Oct to 24 Oct 2026 | build-week | M1 | BUILD 1: Data-to-Insight | Tue 20 Oct, Dussehra (Vijaya Dashami) | none |
| 4 | 26 Oct to 31 Oct 2026 | teaching | M2 | Business and data analyst craft | none | 4 (0 confirmed) |
| 5 | 02 Nov to 07 Nov 2026 | teaching | M2 | Machine learning core + ME1 | none | 5 (0 confirmed) |
| 6 | 09 Nov to 14 Nov 2026 | build-week | M2 | BUILD 2: ML mini | Mon 09 Nov, the Monday after Diwali | none |
| 7 | 16 Nov to 21 Nov 2026 | teaching | M3 | Deep learning essentials | none | 5 (0 confirmed) |
| 8 | 23 Nov to 28 Nov 2026 | teaching | M4 | Transformers and LLM internals | Tue 24 Nov, Guru Nanak Jayanti | 4 (0 confirmed) |
| 9 | 30 Nov to 05 Dec 2026 | build-week | M3 | BUILD 3: DL / LLM mini | none | none |
| 10 | 07 Dec to 12 Dec 2026 | teaching | M5 | Generative AI applied + ME2 | none | 4 (0 confirmed) |
| 11 | 14 Dec to 19 Dec 2026 | teaching | M6 | Retrieval-augmented generation | none | 5 (0 confirmed) |
| 12 | 21 Dec to 26 Dec 2026 | build-week | M6 | BUILD 4: RAG mini | Fri 25 Dec, Christmas Day | none |
| 13 | 28 Dec to 02 Jan 2027 | teaching | M8 | AI agents | none | none |
| 14 | 04 Jan to 09 Jan 2027 | teaching | M7 | Agents in production | none | none |
| 15 | 11 Jan to 16 Jan 2027 | build-week | M9 | BUILD 5: Agentic mini | none | none |
| 16 | 18 Jan to 23 Jan 2027 | teaching | M7 | Major Exam 3, then forward deployed engineering: design to deployment + capstone announced | none | none |
| 17 | 25 Jan to 30 Jan 2027 | capstone | M10 | Capstone sprint 1: frame, propose, walking skeleton | Tue 26 Jan, Republic Day | none |
| 18 | 01 Feb to 06 Feb 2027 | capstone | M10 | Capstone sprint 2: the core, built and measured | none | none |
| 19 | 08 Feb to 13 Feb 2027 | capstone | M10 | Capstone sprint 3: harden, deploy, document, rehearse | none | none |
| 20 | 15 Feb to 20 Feb 2027 | capstone | M10 | Capstone demo and panel defence + closure | none | none |
<!-- /sync:calendar-summary -->

Four kinds of week (Structure tab, locked): Week 0 is the baseline week; regular teaching weeks
are 1, 2, 4, 5, 7, 8, 10, 11, 13 and 14, plus the forward deployed block in Week 16, and all but
Week 16 close on the Saturday recap; build weeks are 3, 6, 9, 12 and 15; capstone weeks are 17
to 20.

The re-cut of 21 September, which the tracker already carries and which stays open to reversal,
is listed in `docs/programme/decisions.md`.

## CREDITS AND HOURS

Senate-approved. Do not restate any other version.

| Component | Hours | Credits |
|---|---|---|
| Theory, including the IITGN faculty sessions | 150 | 15 |
| Practical | 300 | 15 |
| Capstone | 60 | 3 |
| **Total** | **510** | **33** |

Ten modules carry these hours; `08_Modules_and_Credits.md` has them, and every day posts to one
module (the Module column above, with the Week 7 Friday posting to Module 4).

## PHASES

One business question, answered four times with a stronger tool: Weeks 1 to 6 are data analysis
and machine learning, with Builds 1 and 2 and Exam 1; Weeks 7 to 12 are deep learning, LLMs,
generative AI and retrieval, with Builds 3 and 4 and Exam 2; Weeks 13 to 16 are agents,
production and the forward deployed block, with Build 5 and Exam 3; Weeks 17 to 20 are the
capstone in three gates, the demo and defence, and placement. Learners see the same arc as six
steps on their journey sheet: analyst first (1 to 4), machine learning (5 and 6), inside a
language model (7 to 9), generative AI and retrieval (10 to 12), agents (13 to 15) and forward
deployed engineer (16 to 20).

## THE CAMPUS DAY

Two teaching blocks of 180 minutes a day with lunch between them, six days a week, and a TA-led
practice lab after the second block, as the requester set on 29 September 2026. The clock times
live in `data/programme/facts.yaml`; lesson material uses durations only. Sessions do not run past
the agreed close, and AI-free segments stay visibly AI-free.

The teaching day, Monday to Friday: it opens on a Kalpa business question in a stakeholder's
words; the analyst's thinking comes before any tool; the day climbs one case in rungs of rising
difficulty, three rounds in the morning and two cases in the afternoon; every round stages a trap,
a plausible wrong number with the decision it would have misled; learners work in VS Code through
GitHub Codespaces with nothing installed locally; a Kahoot of a few minutes closes the day,
ungraded; exercises are posted on GitHub Discussions, with a take-home and its self-check; the
practice lab runs from the day's practice set; and the setup for tomorrow ships tonight.

On a day that carries an IITGN faculty block, the block runs after the day's applied core, and the
360-minute day holds it whole: the trainer's 240 minutes and the block's 120.

## THE SATURDAY

On a regular week, 300 minutes: a pen-and-paper recap paper of two hours, AI-free and objective,
then a break, the marking, the solution discussion and a paired mock-interview round, as the
requester set on 29 September 2026. The format was revised on 19 September and is locked: fill in the blank,
true or false, one correct option, more than one correct option, scenario sets, applied maths and
ordering, graded easy, medium and hard and tagged to the roles each item serves. The tracker's
blueprint runs the paper 60 minutes in the ME1 and ME2 weeks, 90 to 110 in a typical week and 120
where the interview weight is heaviest (SQL in Week 2, transformers in Week 8); Weeks 1 and 2 run
120, the Week 1 paper carrying new items from its source file beyond the bank. Papers are swapped and marked against
the key, so scores compare across the room and from week to week; the Academic TA leads the
discussion as an interview-answer discussion with random call-outs, and the scores by question
tag feed Monday's remediation read. Ungraded, never a ranking, never a marks component.

The item bank and its key are the tracker's Saturday papers tab, exported to
`docs/curriculum/Saturday_papers.md`. The student paper prints the Item column only.

## THE BUILD WEEK

Locked for Build 1, and the same anatomy runs in every build unless its row says otherwise:

| Day | What happens |
|---|---|
| Monday | The Programme Head introduces the mini projects online: five client-zero sub-problems, groups of four, the week's shape, and the rule that no new material is taught. |
| Monday to Thursday | Groups build, with the trainer's parallel build and daily checkpoints. Wednesday holds the catch-up reserve. |
| Thursday | Mock interviews open: half technical, half a viva on the group's own project; behavioural and HR questioning joins from Mock 3. |
| Friday | The industry expert arrives for two days: business GDs at about 30 minutes per group, and a first tranche of presentations. |
| Saturday | The expert and a senior industry leader who flies in for the day: presentations with live demos, the defence, and grade closure. |

Holidays compress Builds 1 and 2 (Build 1 runs Monday, Wednesday and Thursday; Build 2 opens on
Tuesday), Build 4 moves expert day one to Thursday because Christmas Day is its Friday, and Mock
R5 in Build 5 runs as a two-round simulation. Each build changes the setting: Build 1 in Kalpa
Health, Build 2 in Kalpa Financial Services, Build 3 in Kalpa Connect, Build 4 in Kalpa
Logistics, and Build 5 back in Kalpa Retail at full scale. Build 3 alone carries new content: a
guided NLP track of three short clinics that the project uses and that carries no test. No tests
run in a build week. Build-week assessors are named in the programme's staffing plan, not here.

## THE CAPSTONE

Briefs are announced at the end of Week 16 by theme area, and different groups receive different
briefs. Weeks 17 to 19 run one plan with three gates that fits any brief: the proposal and a
walking skeleton, the measured core, and the deployed and documented system. The live demo and
panel defence run in the first half of Week 20, then closure. Module 10 carries 60 hours, planned
as 18, 18, 18 and 6 across the four weeks. The plan is `docs/curriculum/W17_20_Capstone.md`.

## THE PLACEMENT THREAD

Placement runs from Week 0 and does not wait for Week 20: the baseline card, the daily interview
angle, the Saturday paper, and in every build week the mock interview, the business GD, the
presentation and the live demo. CVs and LinkedIn start in month two; role-track declaration,
positioning, behavioural coaching and a readiness gate follow by Week 14; live interviews run from
Week 15 at the latest, each with a JD-driven preparation slot. The 20-Week Plan's placement column
carries it week by week.

## IITGN FACULTY SESSIONS

About 60 hours inside the 150 theory hours, as 120-minute blocks in seven teaching weeks that end
with retrieval in Week 11; none in build weeks and none from Week 12 onward. Within its week the
block runs after the day's applied core and picks up where the trainer's row stops, so the row's
stop-before line is the faculty member's starting point. The session plan with its references is
`docs/faculty/Sessions.md`; the tracker's violet column carries each block on its day.

<!-- sync:faculty-summary -->
Status: tentative until IIT Gandhinagar, which names the faculty member and confirms each date. 30 sessions of 120 minutes, 60 hours against 60 committed. Within its week the block runs after the day's applied core and picks up where the trainer's row stops.

| Session | Date | Day | Topic | Status | Faculty |
|---|---|---|---|---|---|
| W2-1 | Mon 12 Oct | W02/D1 | Sampling distributions and the central limit theorem | Tentative | to be confirmed by IIT Gandhinagar |
| W2-2 | Tue 13 Oct | W02/D2 | Confidence intervals and the t-test family | Tentative | to be confirmed by IIT Gandhinagar |
| W2-3 | Wed 14 Oct | W02/D3 | Errors, power and sample size; multiple comparisons | Tentative | to be confirmed by IIT Gandhinagar |
| W4-1 | Mon 26 Oct | W04/D1 | Design of experiments: randomised controlled trials and A/B testing | Tentative | to be confirmed by IIT Gandhinagar |
| W4-2 | Wed 28 Oct | W04/D3 | Association rule mining: probability foundations and the Apriori algorithm | Tentative | to be confirmed by IIT Gandhinagar |
| W4-3 | Thu 29 Oct | W04/D4 | Time-to-event analysis: survival curves, censoring and hazard | Tentative | to be confirmed by IIT Gandhinagar |
| W4-4 | Fri 30 Oct | W04/D5 | Time series foundations: autocorrelation, stationarity, exponential smoothing and ARIMA | Tentative | to be confirmed by IIT Gandhinagar |
| W5-1 | Mon 02 Nov | W05/D1 | Linear and logistic regression from first principles | Tentative | to be confirmed by IIT Gandhinagar |
| W5-2 | Tue 03 Nov | W05/D2 | Classifier evaluation: ROC analysis, precision-recall and cost-sensitive decisions | Tentative | to be confirmed by IIT Gandhinagar |
| W5-3 | Wed 04 Nov | W05/D3 | Multicollinearity, identifiability, and explanatory against predictive modelling | Tentative | to be confirmed by IIT Gandhinagar |
| W5-4 | Thu 05 Nov | W05/D4 | The bias-variance trade-off, regularisation and resampling | Tentative | to be confirmed by IIT Gandhinagar |
| W5-5 | Fri 06 Nov | W05/D5 | Decision trees, bagging, random forests and gradient boosting | Tentative | to be confirmed by IIT Gandhinagar |
| W7-1 | Mon 16 Nov | W07/D1 | Feed-forward networks: representation, non-linearity and depth | Tentative | to be confirmed by IIT Gandhinagar |
| W7-2 | Tue 17 Nov | W07/D2 | Backpropagation derived, and gradient-based optimisation | Tentative | to be confirmed by IIT Gandhinagar |
| W7-3 | Wed 18 Nov | W07/D3 | Vanishing and exploding gradients, initialisation, normalisation and regularisation in deep networks | Tentative | to be confirmed by IIT Gandhinagar |
| W7-4 | Thu 19 Nov | W07/D4 | Recurrent networks, LSTM and the path to attention | Tentative | to be confirmed by IIT Gandhinagar |
| W7-5 | Fri 20 Nov | W07/D5 | Subword tokenization and the evaluation of language models | Tentative | to be confirmed by IIT Gandhinagar |
| W8-1 | Mon 23 Nov | W08/D1 | Scaled dot-product attention and the transformer block | Tentative | to be confirmed by IIT Gandhinagar |
| W8-2 | Wed 25 Nov | W08/D3 | Word and sentence embeddings: how they are learned and what their geometry means | Tentative | to be confirmed by IIT Gandhinagar |
| W8-3 | Thu 26 Nov | W08/D4 | Decoding as search: from beam search to sampling methods | Tentative | to be confirmed by IIT Gandhinagar |
| W8-4 | Fri 27 Nov | W08/D5 | Positional encodings, long-context attention and scaling laws | Tentative | to be confirmed by IIT Gandhinagar |
| W10-1 | Mon 07 Dec | W10/D1 | From pretraining to instruction following: instruction tuning, preference optimisation and in-context learning | Tentative | to be confirmed by IIT Gandhinagar |
| W10-2 | Tue 08 Dec | W10/D2 | Constrained decoding: formal grammars, automata and token masking | Tentative | to be confirmed by IIT Gandhinagar |
| W10-3 | Thu 10 Dec | W10/D4 | The statistics of model evaluation: sample size, agreement and significance | Tentative | to be confirmed by IIT Gandhinagar |
| W10-4 | Fri 11 Dec | W10/D5 | The arithmetic of LLM inference: memory, throughput and quantisation | Tentative | to be confirmed by IIT Gandhinagar |
| W11-1 | Mon 14 Dec | W11/D1 | Classical information retrieval: the vector space model, TF-IDF and BM25 | Tentative | to be confirmed by IIT Gandhinagar |
| W11-2 | Tue 15 Dec | W11/D2 | Approximate nearest-neighbour search: LSH, product quantisation and HNSW | Tentative | to be confirmed by IIT Gandhinagar |
| W11-3 | Wed 16 Dec | W11/D3 | Learning to rank, neural rerankers and rank fusion | Tentative | to be confirmed by IIT Gandhinagar |
| W11-4 | Thu 17 Dec | W11/D4 | Evaluating retrieval and retrieval-augmented generation | Tentative | to be confirmed by IIT Gandhinagar |
| W11-5 | Fri 18 Dec | W11/D5 | Long-context behaviour, grounding and hallucination in language models | Tentative | to be confirmed by IIT Gandhinagar |
<!-- /sync:faculty-summary -->

## ASSESSMENT

<!-- sync:evaluation -->
Status: locked. Any file may state the five components, their marks, the marks per event and the week each is earned in. A rubric, and the day of a graded event, may be stated for a build that the rubrics block below carries, and in a STUDENT file only where that block allows learners to see it. Every other rubric and graded-event day, and every pass requirement, waits for the programme handbook, which publishes them before the first graded event, in Week 3. The version in force is proposal-2026-09-25.

| Version | Status | Major exams | Mini projects | Mock interviews | Business GDs | Capstone | Source |
|---|---|---|---|---|---|---|---|
| proposal-2026-09-21 | superseded | 300 | 150 | 200 | 200 | 150 | tracker, Structure tab (Evaluation schema, revised 21 September) |
| proposal-2026-09-25 | locked | 300 | 200 | 150 | 150 | 200 | handover, pages 8, 9 and 13 (proposed to the AOC on 25 September 2026); locked by the requester on 28 September 2026, as the orientation deck (slides 19 to 21) states it |

Exams, locked: ME1 in Week 5, 70 marks, posting to M2; ME2 in Week 10, 100 marks, posting to M5; ME3 in Week 16, 130 marks, posting to M9, the first half of Monday.
Exam day and slot: open. ME1 and ME2 run during their week as a continuous activity; no artifact states a day or a slot until it is fixed.
Ungraded indicators: daily Kahoot, the Saturday recap paper, the Week 0 diagnostic, attendance, practice exercises, the weekly written assignment, engagement.
Attendance, locked: 90 percent minimum over the programme as a whole, recorded in every session, teaching and build weeks alike.
Rubrics settled: Build 1 (W03), locked, by the requester, in session, on 29 September 2026, approving the drafts as written. Every other rubric waits for the programme handbook.
<!-- /sync:evaluation -->

Every graded instrument posts wholly to one module, because the transcript is built per module.
All major exams, mock interviews, presentations and business GDs are AI-free. Mock interviews and
business GDs also feed a separate Placement Index. The scheme was locked on 28 September 2026, so
learners may be told its components, their marks and the week each is earned in. What a file may
say about a rubric, a pass requirement or the day of a graded event follows the rule above.

## PLATFORMS

| Platform | Use |
|---|---|
| VS Code with GitHub Codespaces | The single learner environment. Notebooks are `.ipynb`; SQL is `.sql` against Postgres. |
| GitHub | Exercises (posted on GitHub Discussions), projects, repositories and portfolios. |
| LMS | Content delivery and submissions. |
| Kahoot | The daily ungraded check. |
| CodeChef | Daily coding practice if adopted; the decision is open, so no artifact names it yet. |

This cohort does not use Slack.

## PEOPLE AND BODIES

Roles only. Task owners named in a written document are the Academic TA and the Support TA.

| Role | What it owns |
|---|---|
| Programme Head | The programme, the curriculum lock, the mini-project introductions, escalations. |
| Principal Advisor | Curriculum architecture and assessment; a share of the Build 1 mocks. |
| Data and reporting lead | The score sheet, which is the only thing the AOC sees, and the operational supervision of the TAs. |
| Academic TA | The Saturday discussion, the Week 0 one-to-ones, remediation and the mock share. |
| Support TA | Environment, logistics and learner support. |
| On-ground manager | Campus operations, the daily signals, remediation follow-through, morale and the concern log. |
| In-house and industry trainers | Delivery against the row; industry trainers also assess in build weeks. |
| IITGN faculty (tentative) | The faculty sessions, once IIT Gandhinagar names them. |

Four bodies: IIT Gandhinagar awards the diploma; CDF, also called CAA, is IITGN's not-for-profit
company through which the programme runs; the AOC locks the evaluation scheme and rubrics, receives
every graded score with its type and mode, and approves the faculty plan, and students may write to
it; the delivery partner runs admissions, hospitality, placement and delivery. For B2B and
external-facing documents the brand is IITGN CDF.

## OPEN DECISIONS

<!-- sync:decisions -->
Open decisions:

| Decision | Status | Closed by | What | What it blocks |
|---|---|---|---|---|
| evaluation-lock | closed | the requester, on 28 September 2026 | The evaluation scheme is locked at the 25 September proposal. The parked gateway of 80 percent attendance and quiz completion before mocks and the capstone is not part of the lock, so no artifact states it. | nothing |
| build1-rubrics | closed | the requester, on 29 September 2026 | Build 1's mini project, mock and GD rubrics are approved as drafted, with the mini project scored per group on 34 marks and per learner on 6, and the mock and GD scored per learner. Learners may see them, and Build 1's learner files may name the days of its graded events. Both sit in evaluation.rubrics. | nothing |
| anand-finance-controller | closed | the requester, on 30 September 2026 | Anand Iyer is Kalpa Retail's finance controller, as client zero v2.2 has him, in every pack and paper; where the tracker's Week 1 and Week 2 rows call him the CFO, this decision wins. | nothing |
| saturday-edits-w1-w2 | closed | the requester, on 30 September 2026 | Every option edit and relabelling that data/programme/paper_edits.yaml lays on the Week 1 and Week 2 Saturday papers is accepted, thirty in all; each applies until the tracker's Saturday papers tab carries it, and the sync then reports it folded. | nothing |
| plants-once-found | closed | the requester, on 30 September 2026 | Only the week's Saturday recap paper may name a planted value, and only one the room has already found in class, so the Week 1 Saturday paper keeps the two tracker items that name values planted in the Week 1 Monday dataset (banks 11 and 47, printed as Q32 and Q51 when this was decided and folded since into the deeper items that still print their values); every other learner file names no plant. | nothing |
| tuesday-finding-once-found | closed | the requester, on 1 October 2026 | Week 1 Tuesday's files used after chapter 3, where the room finds that the same Retail-Plus members ordered less often, may state that finding, because chapters 4 to 6 and both afternoon cases are built on it and every file stands alone. Each states the finding on its own page, with its numbers, rather than pointing back to the morning. The pre-read, chapters 1 to 3 and every earlier day's file never name it, and every other day keeps the plant rule as written. | nothing |
| teaching-approach | closed | the requester, on 12 October 2026 | Every week, day, Saturday and project built from 12 October 2026 on is designed, created and taught by the teaching approach in .claude/skills/day-pack-builder/references/the-standard.md. Each day carries an engineering case at a company the learners use, in a named place, with the metric, its values before and after, the data and the ask, labelled illustrative with synthetic data from the day's own seeded generator, and Kalpa carries the same method as the client; each idea climbs a ladder of sub-problems from a hand count a weak learner can do to the depth of Uber, Swiggy, Google and AI-startup interviews, with an AI-company variant; every artefact teaches in the blend of styles in references/teaching-styles.md (Veritasium's misconception and prediction first, 3Blue1Brown's and StatQuest's visual derivation from tiny numbers, Krish Naik's line-by-line code-along, ByteByteGo's connected maps, takeUforward's ladder of problems, problem-first interactivity, the Feynman technique, and more); each week ships one interactive explorer that grows day by day; pictures are drawn by our own code. This decision adds to decision chapter-standard and never replaced it; where the day's shape is concerned, decision concept-first-case-second (13 October 2026) says how the concept chapters and the case chapters share a day. Weeks 1 to 3 keep their shape until rebuilt.<br>Keeps: chapter-standard's chapter unit (one deck chapter paired with one notebook, the problem before the code, a second route, a third of items as design items).<br>Drops: chapter-standard's count of about six chapters and its five-pass loop, for weeks built from Week 4 on, because the requester found Weeks 1 to 3 generic (12 October 2026). | nothing |
| w4-case-led | closed | the requester, on 12 October 2026, accepting the Week 4 plan with its case-led revision | Week 4 is the first week built by decisions teaching-approach and concept-first-case-second. It runs on its approved spine (docs/detailing/W04_analyst_craft_spine.md), whose section 2.0 and each day's concept block were added on 13 October 2026, and its case file (docs/detailing/W04_case_file.md). Each day opens on its topic and concept map, teaches the row's subtopics in named concept chapters on educational examples, then carries an engineering case at a real company in a named place, labelled illustrative, its data synthetic and generated by the day's own seeded script, climbed in case chapters from a hand count on twelve rows to interview depth with an AI-company variant; Kalpa carries the same method in the TA lab and one unguided exercise. The count of about six chapters, the company in every chapter and the volume table of the-standard.md do not apply to Week 4; the chapter unit, one notebook per chapter and the coverage gate do. Review is three cold reads (the fresh graduate, the hiring interviewer and the trainer with the row open), one fix pass and verify.py.<br>Keeps: the chapter unit, one notebook per chapter, the question ladder at the day and chapter level.<br>Drops: the count of about six chapters, the real company in every chapter, the volume table and the five-pass loop, for Week 4, because its spine sizes each day to its minutes and the requester found Weeks 1 to 3 generic (12 October 2026). | nothing |
| concept-first-case-second | closed | the requester, on 13 October 2026, after reading every Week 4 deck | Every teaching day built from 12 October 2026 on teaches the curriculum row's subtopics first and applies them to the case second. The deck opens on the day's topic (the row's Day focus), the week map with today lit, the topics slide and the concept map, which name every bullet of the row's Subtopics column verbatim and in the row's order, each with the chapter that teaches it; then the case ticket in one slide, as the destination. The concept block follows, 60 to 120 minutes, one chapter per subtopic of about 8 to 25 minutes, in the row's order unless the week's spine records a reason to teach them in another, each opener written `## SECTION n: <subtopic>: <short question>?`, with the subtopic as the row words it, a short question of about 24 characters that the deck's pills print, and an italic promise beneath saying what the chapter delivers, each taught from zero on a simple, complete, relatable educational example with invented numbers labelled invented, in the blend of styles (the misconception and a prediction, the hand count on tiny numbers, the picture, the formula or rule named last, a glimpse of code, four rules, the map node), and each paired with one short notebook of 8 to 18 cells whose file name and first heading carry the same subtopic; a concept chapter may open the afternoon, before the case chapter that applies it. The case chapters follow, three or four, each naming the subtopics it applies on its opener and in its notebook's first cell, as decision teaching-approach shapes them; the lab runs Kalpa. Every teaching day ships an INTERNAL coverage matrix (each row subtopic verbatim against its chapter title, slides, notebook, exercise items, Kahoot items and minutes, then each case chapter against the subtopics it applies), and scripts/coverage_check.py, run by verify.py, fails the pack when a subtopic has no chapter or no notebook carrying its name, when a matrix entry names a slide, file or item that does not exist, or when a case chapter applies no subtopic. The row's Subtopics column is the day's chapter list and the curriculum is the contract: a subtopic a spine adds carries "(added by the spine)" and a reason, and a subtopic the row carries is never dropped. Weeks 1 to 3 keep their shape until rebuilt.<br>Keeps: everything in teaching-approach (the case, the ladder, the styles, the explorer, the facts-file rule, the illustrative label, Kalpa in the lab) and the chapter unit of chapter-standard.<br>Drops: the test "a pack whose deck opens on a topic title was not built from the row", because it taught builders to keep topic names out of the titles where the schema needs them; the volume table's count for weeks from Week 4 on, as teaching-approach already dropped it.<br>Applies from W04. | nothing |
| w5-artifact-set | closed | the requester, on 28 October 2026, asking for Week 5 to be built day by day in a leaner artifact set | Every teaching day from Week 5 on is built in the artifact set of docs/11_Artifact_Set_W05.md. A day folder holds a README that opens on the run table and four folders named by who opens them: 1_in_class_training_content (one visual deck with little text, one notebook per chapter and per case chapter, a guided in-session notebook, one lightweight explorable), 2_take_home_mandatory (the practice set for two to three hours, about ten scenario problems with exhibits, fifteen to twenty self-check MCQs, the key and model solutions in the same document, a recap, a self-check guide, a few dated links and tomorrow's pre-read; and the practice lab notebook), 3_study_material_for_students (study notes, a cumulative cheat sheet, an interview question bank with model answers) and 4_trainer_only (the trainer guide of tables, bullets and diagrams, the lab solutions, the sources). Data is public and downloaded in code; a real company and its real data carry the case and Kalpa stays the decision layer. No logo appears in any artifact, and no line names the institute or the programme. Planning and critique run on Fable at extra effort and builds on Opus at extra effort; max effort only on request.<br>Keeps: concept-first-case-second's chapter unit (one chapter per row subtopic in the row's order, its opener in the SECTION form, one notebook per chapter, the case after the concepts), teaching-approach's ladder and blend of styles, the interview angle, the facts-file and dated-source rules, and every writing rule.<br>Drops: for Week 5 on, the exercises, kahoot, preread, extras, whiteboards, data, takehome, cheatsheets, study-notes, trainer and internal folders, whose content moves into the four folders; the INTERNAL coverage matrix and the three cold-read agents, replaced by the builder's verify run and one read against the row by the orchestrating session; teaching-approach's single explorer that grows across a week, replaced by one explorable per day; teaching-approach's synthetic data generated by the day's seeded script, replaced by public data downloaded in code; logos, the institute's name and the programme line on deck dividers; because the requester found the folders hard to navigate, the artifacts too many and too verbose, and the data generation a poor use of the build (28 October 2026).<br>Applies from W05. | nothing |
| w5-explorer-companion | closed | the requester, on 28 October 2026, finding the Week 5 explorables undercooked and asking for each day's HTML to run from zero to the interview, and approving the staggered build on 29 October 2026 | From Week 5 on, each teaching day's explorable is the day's visual companion from zero to the interview, built to the skeleton in docs/11_Artifact_Set_W05.md: the story animated on the real case, the concept map, one how-it-works page per row subtopic with motion graphics, the case on real data, verified company scenes with the six seats, an interview room the learner works step by step, and check yourself. Every page asks a prediction, moves one variable and redraws a picture and a number together. The look and the components live once in scripts/companion/w5kit.css and w5kit.js, inlined by scripts/build_companion.py, and html_sweep walks every page.<br>Keeps: w5-artifact-set's one explorable per day in demos/, offline with no library and no network, the html_sweep rule, the ten principles of W05_explorables.md section 1 (prediction before the reveal, linked views, the wrong default, countable marks with the count beside every percentage, the error drawn before it is named), invented numbers labelled invented in the concept animations, and nothing the room must find named before it is found.<br>Drops: the explorable's limit of about 400 lines, its single question and its one or two controls, the three clicks as the page's whole run order, and invented-only data in the explorable, because the requester found the pages undercooked (28 October 2026).<br>Applies from W05. | nothing |
| w6-build-pack | closed | the requester, on 29 October 2026, after Build 1's groups did not read their briefs, leaned on ChatGPT, could not explain their numbers and spent most of their presentation time re-explaining the problem; spine approved the same day | From Week 6 on a build week ships one pack on its launch day, built to docs/12_Build_Week_W06.md: a README that opens on the week's run table, the ticket and the workbook in 1_project, a template repository in 2_starter_repo, the week's explorer in 3_explorer and the trainer files in 4_trainer_only, so a learner opens four things all week. Build 2 runs one shared problem for every group, a call before the due date on UCI Default of Credit Card Clients (CC BY 4.0) as Kalpa Financial's proof of method, with a constraint card per group from Tuesday's discovery call and a one-number twist on it at Thursday's approach gate. Groups are of three, talks run 12 minutes in slots of 20 at most, every stage of an eight-stage ladder from black box to defence has one workbook page, the breadcrumb notebook is the starter repo's only notebook from Tuesday, and AI runs in two lanes: none for the frame, the gate, the viva and the defence, and logged and explained for code. The Mock R2 viva runs inside Thursday's approach gate, every member questioned, and its technical half is a written sheet.<br>Keeps: the build week's place in the tracker row (the online launch, the daily checkpoints, the trainer's parallel build, Mock R2, the GDs, the presentations with a live demo, grade closure in-week), Kalpa Financial Services and Rohan Desai as the client, Build 2's move of trade-offs under unequal error costs, the 40, 30 and 30 marks per build, w5-artifact-set's public data, executed notebooks and writing rules, and Build 3's tracker row unchanged.<br>Drops: for Build 2, client zero v2.2's five Kalpa Financial sub-problems and the row's three groups per sub-problem, groups of four, presentations of 25 to 30 minutes, the individual Mock R2 of about 20 minutes, the row's fraud figures of a million rows at half a percent positives (the real public fraud table has 284,807 rows at 0.17 percent), and the build-day folders (briefs, rubrics, gd, parallel-build, checkpoints, mocks) for builds from Week 6 on, because the requester found Build 1's long briefs unread and wants one deep problem learned from first principles (29 October 2026).<br>Applies from W06. | nothing |
| w6-open-images | closed | the requester, on 29 October 2026, asking for existing images that depict an idea well | From Week 6 on an openly licensed image (Creative Commons or public domain, from Wikimedia Commons or a source that states the licence) may appear in a deck, an explorer or a document with its attribution line printed beside it. An image of unclear licence, which is most of what an image search returns, is redrawn by our own code, since the repository is public.<br>Keeps: w4-visuals' rule that data pictures are drawn by our own code and mechanisms by mermaid, the measurement of every label before a picture ships, and dated sources.<br>Drops: w4-visuals' "nothing is pasted in from elsewhere" for openly licensed images carrying their attribution, because the requester wants existing images that depict an idea well (29 October 2026).<br>Applies from W06. | nothing |
| w6-poc-mvp | closed | the requester, on 29 October 2026 | Build 2 teaches and practises POC against MVP thinking: why a team proves the method first, what the proof must show, what an MVP adds and what production adds, as the ladder's stages 4 to 6. Build 5 keeps the POC-against-MVP pitch the 20-Week Plan gives it, and pitches what Build 2 taught.<br>Keeps: the 20-Week Plan's Build 5 pitch and every other build's move.<br>Drops: nothing from the plan; it adds the thinking to Build 2 ahead of the pitch (29 October 2026).<br>Applies from W06. | nothing |
| w4-finding-once-found | closed | the requester, on 12 October 2026, accepting the Week 4 plan with its case-led revision | In Week 4, a day's learner files used after the step in which the room finds a planted feature, in class or in the TA lab, which counts as class, may state that finding with its numbers, each on its own page, because the later steps build on it and every file stands alone; a later day's files may restate an earlier day's finding the same way. The pre-read, the earlier steps and every earlier day's files never name it, and the full-data step that finds a plant runs in an empty your-turn cell. This extends decision tuesday-finding-once-found to Week 4. | nothing |
| w4-visuals | closed | the requester, on 12 October 2026, accepting the Week 4 plan with its case-led revision | Week 4 teaches with pictures drawn by our own code (matplotlib in executed notebooks or figure scripts, placed in decks and sheets by an image line), animated GIFs made the same way with a still beside each, mermaid mental maps, and one interactive HTML explorer for the week in the spirit of 3Blue1Brown, Veritasium and ByteByteGo, which passes scripts/html_sweep.py and reveals no planted Kalpa value. Nothing is pasted in from elsewhere. | nothing |
| saturday-w4-shape | closed | the requester, on 12 October 2026, accepting the Week 4 plan with its case-led revision | The Week 4 Saturday runs the locked 300-minute shape with a 120-minute paper (saturday_papers.paper_minutes W04 120). The row's cross-domain transfer drill runs as the paper's last part and as a spoken round after the discussion, and the paired mock-interview round runs on the week's interview transcripts. | nothing |
| reporting-day-line | closed | the requester, on 30 September 2026 | The Week 2 Tuesday interview line asks what you do when the validation fails at the end of reporting day, the wording the Tuesday pack teaches, where tracker v7 said 5 pm. The repository's copy of the tracker carries the change, and the master takes it at its next version. | nothing |
| saturday-interview-grade | closed | the requester, on 30 September 2026 | The Saturday recap papers are interview grade. The tracker's bank sets what is tested, and the week's source file may reword, fold or move any bank item with its reason; about 60 percent of the timed items are hard; every part opens on a Kalpa scenario with its nuance and a visual; blanks are answered from word banks, pairs from match tables, and statements are judged with their reasons. | nothing |
| saturday-real-cases | closed | the requester, on 30 September 2026 | The Saturday recap papers may set items at named, real companies and in public case studies, used directly or as inspiration, alongside Kalpa's own case. Every real fact or figure a paper prints is checked against a primary or reputable source whose URL and date sit in the provenance; a figure that cannot be checked appears only in a hypothetical marked as illustrative, and a named company in a hypothetical reads as one. | nothing |
| w2-set1-fold | closed | the requester, on 30 September 2026, who left the call to the build | The Week 2 Saturday paper folds the bank's Set 1 into a set on the room's own Q2 warehouse, which tests the same fan-out and unpaid-order logic on numbers the room worked with; this replaces the 29 September ruling that kept Set 1 as the bank has it.<br>Drops: the 29 September ruling that kept Set 1 as the bank has it, because a set on the room's own Q2 warehouse tests the same fan-out and unpaid-order logic on numbers the room worked with. | nothing |
| four-domains | closed | the requester, on 30 September 2026 | The programme prepares learners for four domains, and each enters on its story from a domain dossier the first day it appears, with its one-page card and the trainer's talk track. Retail and e-commerce enter on Week 1 Monday (Kalpa Retail; the dossier is content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md). US healthcare enters on Build 1 Monday (Kalpa Health, repositioned as a US-facing business, addendum health-us-facing). Financial services enter in Week 5, where the lending question arrives, and carry Build 2 (Kalpa Financial Services). SaaS and enterprise AI enter in Week 8, as the GCC building AI products, an enterprise brain among them, for Kalpa's units and for US clients. Connect and Logistics get their story when a build first enters them. In every domain, each chapter names a real company that faces the same question, as a likeness with every fact checked and dated, and Kalpa stays the case. | nothing |
| build1-us-data | closed | the requester's repositioning of Kalpa Health, on 30 September 2026 | Build 1's data moves to the US setting of client zero section 1c. data/generate_kalpa_health.py writes a synthetic pack of six US metro areas, patient service centres, commercial, Medicare, Medicaid and self-pay payers, claims billed in dollars, remittance postings keyed in the posting system's own format, and denials in seven reason categories modelled on the X12 claim adjustment reason codes; the two quarters are calendar Q2 and Q3 of 2026. Every planted trap keeps its logic and its counts, and the Build 1 mini project rubric reads "counts and dollars reconcile across files" where it read rupees. | nothing |
| build1-register-from-bookings | closed | the requester, on 1 October 2026 | Build 1's visit register is drawn from the bookings. data/generate_kalpa_health.py writes one register row for every Q3 visit a booking brought to a patient service centre, naming its booking, so the register agrees with both booking files row for row, and a patient who missed a booked slot and was rebooked has a row for the missed slot beside the kept one. The no-show sub-problem keeps its logic, and its numbers are re-planted in the spine's sub-problem 4 row; every other plant keeps its counts. | nothing |
| chapter-standard | closed | the requester, on 30 September 2026 | Every teaching day is rebuilt to the raised standard in .claude/skills/day-pack-builder/references/the-standard.md. The day runs in about six chapters, each one deck chapter paired with one notebook that builds on the one before it; each chapter states the problem and lays out two to four ways to answer it, sized, with the best-fit call and the fact that would change it, before any code, and closes by reaching the same answer a second way; at least a third of a day's exercise items are design items; and every pack runs a five-pass depth loop whose last two passes are fresh reviewers. Weeks 1 and 2 are rebuilt first, Week 1 all at once. Decision concept-first-case-second (13 October 2026) keeps this decision's chapter unit for every week and drops only its count of about six and its five-pass loop for weeks built from Week 4 on. | nothing |
| question-ladder | closed | the requester, on 30 September 2026 | Every heading in a learner file is a plain, specific question the section answers, understandable on its own, with who needs the answer and the smaller questions on the way beneath it, and each section closes on its answer with its number; generic labels such as "Customer lifetime value, simply" are replaced. The day asks one question, each chapter asks the question the previous answer raised, and each chapter climbs through four to six smaller questions. On a slide the italic subtitle asks and the action title answers. The form is the question ladder in .claude/skills/day-pack-builder/references/the-standard.md. From 13 October 2026 a chapter opener's title leads with the chapter's topic and ends on a short question of about 24 characters, which the deck's pills print, and its italic promise says what the chapter delivers (decision concept-first-case-second); every other heading stays a question. | nothing |
| self-contained | closed | the requester, on 30 September 2026 | Every deck, notebook, exercise file, case brief, take-home and Saturday paper is understood with nothing else open. It states its scenario, explains its terms where they first appear, loads or prints the numbers it uses and restates what an earlier chapter found when it builds on it; a pointer to another file adds depth and is never needed to follow the page. Decks carry each chapter in full depth, in the notebook's rhythm. | nothing |
| humanizer | closed | the requester, on 30 September 2026 | The humanizer skill (blader/humanizer at 225a6f3, MIT, in .claude/skills/humanizer) is imported, and every prose file in the programme passes its read in file mode as well as the tic scanner, so that no wording reads as a language model's. | nothing |
| opus-max | closed | the requester, on 30 September 2026 | Every session on this project, and every agent a session starts, runs the latest Opus model at max effort; .claude/settings.json sets the model, the effort level and the subagent model, and every spawned session and agent is given the Opus model explicitly. | nothing |
| rubrics-and-calendar | open | the Programme Head | The component rubrics and the assessment calendar with the day of each graded event from Build 2 on, including the capstone, which the programme handbook publishes before the first graded event, in Week 3. | every rubric and graded-event day after Build 1's |
| w16-proposal-marks | open | the Programme Head and the AOC | Whether the Week 16 solution proposal carries marks, since the scheme has no line for it; the tabs call it assessed. | the Week 16 Wednesday pack's assessment wording |
| recut-2026-09-21 | open | the Programme Head | The re-cut that followed the re-date, which stays open to reversal. | nothing yet, since the tracker already carries it; a reversal would reshape Weeks 1, 3, 4, 6, 7 and 8 |
| exam-days | open | the Programme Head | The length and the paper of each major exam, and the day of ME1 and ME2. | any artifact that would name an exam day or slot |
| faculty-blocks | open | IIT Gandhinagar and the Programme Head | The faculty names and dates from IIT Gandhinagar. How a day absorbs a block was settled on 29 September 2026, when the campus day became 360 minutes, the trainer's 240 and the block's 120. | the faculty lines of 30 day packs in Weeks 2, 4, 5, 7, 8, 10 and 11, which render from sync blocks |
| client-zero-v2-3 | open | the Programme Head | The lock on client zero v2.3. | the Week 1 Friday lab dataset and every pack from Week 10 on |
| build-owners | open | the Programme Head | Mock and GD owners for Builds 2 to 5, and the expert's dates for Build 4 around Christmas. | the build-week trainer sheets from Week 6 on |
| build-sequencing | open | the Programme Head | Whether all five builds move to the sequencing discussed on 15 September, with GDs from day two, mocks in the same window and presentations by one assessor. | the build-week trainer sheets |
| papers-to-build | open | the content team | The Saturday papers for Weeks 10, 11, 13 and 14. The Week 4 Tuesday items, Part 2 of the Week 4 paper, are written as additions in content/W04/SAT/internal, and the requester accepted them with the paper's folds, its stretch-page move and its five edits on 13 October 2026; they reach the tracker at its next version. | the Saturday packs for Weeks 10, 11, 13 and 14 |
| senate-reconciliation | open | the Programme Head and the academic office | Reconciling the senate grading buckets and passing rules (CGPA 7, a Placement Index of 7 and twelve projects) with the 1000-mark pool; the 90 percent attendance minimum is locked. | any pass requirement in any artifact |
| codechef | open | the Programme Head | Whether daily coding practice on CodeChef is adopted; the 20-Week Plan names it and the handover calls it undecided. | any artifact that would name the practice platform |
| restricted-holidays | open | the institute calendar | Whether campus closes on New Year's Day (Week 13 Friday) and on Makar Sankranti (Week 15 Thursday). | the Week 13 Friday and Build 5 Thursday plans |

Known conflicts between the sources, and the working rule until one is fixed:

| Conflict | Sources | What disagrees | Working rule |
|---|---|---|---|
| evaluation-versions | tracker, handover | The tracker's Structure tab (21 September) prints mini projects 150, mocks 200, GDs 200 and capstone 150; the handover says the scheme proposed to the AOC on 25 September is mini projects 200, mocks 150, GDs 150 and capstone 200. | The 25 September version is locked as of 28 September 2026 and may be stated anywhere; the Structure tab's table is superseded until the tracker's next version carries the locked scheme. |
| groups | tracker, handover | The handover plans 35 students in nine build-week groups, while the tracker's build-week anatomy asks for five sub-problems with three groups each, which is fifteen groups. | Build-week packs seed five sub-problems and leave the group-to-problem allocation to the trainer sheet until the Programme Head settles the count. |
| week0-schedule | tracker, journey | The Week 0 tab (21 September) and the student Week 0 sheet (27 September) give different running orders. The tab runs four diagnostic papers of 60, 45, 30 and 30 minutes on Tuesday and puts the project talks on Saturday beside an industry leader session; the student sheet runs one paper of about two hours on Tuesday, moves the introductions to Wednesday afternoon, and gives Saturday to a session with a working forward deployed engineer. On 28 September 2026 the requester's own diagnostic replaced both papers, as one Google Form of forty questions in about 90 minutes. | Week 0 packs follow the student sheet for the running order and the requester's diagnostic for Tuesday, and cite the tracker row for content only. |
| anand-title | tracker, docs/07_Client_Zero.md | The tracker's Week 1 and Week 2 rows call Anand Iyer the CFO, while client zero v2.2's stakeholder table calls him the finance controller of Kalpa Retail. | The requester settled it on 30 September 2026 in favour of finance controller (decision anand-finance-controller), so every pack and paper says finance controller and the tracker's rows are superseded on the title until its next version carries it. |
| journey-tokenization | tracker, journey | The student journey lists tokenization under Week 8, while the re-cut moved it to the Week 7 Friday. | Packs follow the tracker; the journey needs its Week 7 and Week 8 rows corrected before it is republished. |
| journey-holidays | tracker, journey | The student journey lists holidays up to Week 9 only, so Christmas Day in Week 12 and Republic Day in Week 17 do not appear on it. | Packs follow the tracker; the journey adds them when it is next published. |
| journey-capstone | tracker, journey | The journey's capstone rows describe an older sprint plan, with deployment in Week 18, while the tracker's capstone tab puts the proposal and walking skeleton at gate 1, the measured core at gate 2 and deployment at gate 3. | Packs follow the tracker's capstone tab. |
| fde-block-hours | tracker, handover | The 20-Week Plan sizes the Week 16 forward deployed block at roughly 27 hours; the handover says about 30. | Packs size Week 16 from the tracker rows, which are day by day. |
| exercise-channel | docs/03_Day_Pack_Spec.md of 13 September, handover | The day pack spec of 13 September says GitHub Discussions is not used; the handover of 27 September says exercises are posted on GitHub Discussions, which is also what the Cohort 1 learnings and the method retrospective describe. | The handover is later, so exercises are written to be pasted into GitHub Discussions verbatim, with no trainer text inside them. |
| weekly-metrics | docs/01_Programme_Facts_C2.md of 13 September, handover | The facts file of 13 September named a Weekly Academic Score and a Weekly Performance Score over Weeks 2 to 21; the handover of 27 September describes six signals, one tracker and one score sheet, and neither metric. | No artifact names either metric until the Programme Head confirms it survives the re-date. |
| eligibility-thresholds | docs/01_Programme_Facts_C2.md of 13 September, handover | The facts file of 13 September set placement gates of CGPA above 7.0 and attendance above 95 percent; the senate proposal, as the handover reports it, passes on CGPA 7, a Placement Index of 7, twelve projects and 90 percent attendance. | The 90 percent attendance minimum over the programme is locked and may be stated anywhere; no artifact quotes a CGPA, Placement Index or project-count requirement until the senate reconciliation closes. |
<!-- /sync:decisions -->

# Build 2 pedagogy: what the evidence says and what the week does with it

Research note for the Week 6 council, written 29 October 2026. Every source below was opened on 29 October 2026 unless its row says "not verified". Nothing behind a paywall or a bot check was bypassed. The designs fit the draft spine in this folder (`W06_spine_draft.md`): 39 learners in 13 groups of three, one shared lending problem with a constraint card per group, the eight-stage ladder from black box to live demo, Tuesday to Saturday with Monday off.

## 1. Why Build 1 failed, and what each fix has to do

The four symptoms the requester named have four different causes, and each cause asks for a different kind of fix.

| Symptom in Build 1 | Likely cause | What the fix has to do |
|---|---|---|
| Nobody read the 10,000 words; ChatGPT did | The brief was too long for working memory, and no step checked that anyone had read it. Pasting it into a chatbot was the rational move for an overloaded learner. | Cut the reading to a page, release the rest only when a group asks for it, and put a short check on the page that is read. |
| Groups could not explain their own numbers | The product was graded and the understanding was not. A chatbot can produce a number a learner never computed. | Make every number owned by a person, and test that person live. |
| No business nuance | The learners never met the client; the brief handed them every fact at once, so no fact was earned and none felt important. | Make the nuance something a group has to ask for. |
| Seven of ten minutes spent re-explaining the problem | Build 1 already had an answer-first format, so the template was there. The talk was never rehearsed against a clock, and the problem was the only part the group understood well enough to talk about. | Cap the problem at 90 seconds on a run sheet, rehearse twice against a clock, and make the rest of the talk something each member can defend. |

The guiding evidence for a room at 3 out of 10 is Kirschner, Sweller and Clark (2006): minimally guided work is less effective and less efficient for novices, and the advantage of guidance fades only "when learners have sufficiently high prior knowledge to provide internal guidance". The expertise reversal effect (Kalyuga and colleagues, 2003) is the other half: guidance that helps a novice hurts a learner who no longer needs it, so it has to fade as the room climbs toward 8.

## 2. Guided learning that fades

| Technique | What it is | Evidence | The form it takes in Build 2 |
|---|---|---|---|
| Worked example, then completion problem, then independent problem | Learners first study a full solution, then finish a partly solved one, then solve alone, with the solved steps removed one at a time. | Renkl and Atkinson (2003): examples suit early skill acquisition and problem solving suits later stages; fading steps in gradually works because intrinsic load drops as skill grows. Kirschner and colleagues (2006) on guidance for novices. | The breadcrumb notebook is a backward-faded example: stages 0 to 2 are fully worked on Week 5's retail model, stage 3 keeps the code skeleton with the decisions left as TODO, and stage 4 onward is blank. The trainer's full build stays TRAINER only. |
| Subgoal labels | Each step of a procedure carries a short label naming its purpose, so a learner sees the structure of a solution without seeing its content. | Margulieux and Catrambone (2016, CogSci, programming): constructive methods beat passive ones, and learners did best when they got hints about the subgoals or feedback on labels they wrote themselves, not both; "providing too much support can be equally as detrimental as providing too little". | The approach card: the eight ladder stages each written as a question (section 2.1). This is the "solution approach with breadcrumbs". |
| Hint ladder | Hints arrive in a fixed order from a question, to a pointer, to a worked parallel, so a learner takes only as much help as needed. | Collins, Brown and Holum (1991) on scaffolding that ranges "from doing almost the entire task for them to giving occasional hints", and fading that slowly removes it. | Three sealed hints per stage, opened at the daily checkpoint and logged (section 2.1). |
| Parsons problem | Learners put scrambled lines or steps of a correct solution in order, sometimes with decoy steps that carry a common error. | Ericson (2018, Georgia Tech dissertation): Parsons problems were completed significantly faster than fixing or writing code, with the same learning gains. | A ten-minute Parsons card on Tuesday: eleven pipeline steps and three decoys ("fit the scaler on all rows", "pick the threshold at 0.5", "keep the column written after the decision"). |
| Comparing two methods side by side | Learners study two solutions to the same problem on one page and say which is better and when. | Rittle-Johnson and Star (2007), as reported by Harvard GSE: comparing methods side by side produced greater gains in procedural knowledge and flexibility than studying them one at a time; students judged efficiency and accuracy more often. | The A-versus-B sheet at ladder stage 3 (section 2.2). |
| Gradual release ("I do, we do, you do") | Responsibility moves from teacher modelling, to guided practice, to group work, to independent work. | Fisher and Frey, ASCD: focused instruction, guided instruction, collaborative learning, independent learning. | A daily 30-minute opening inside the row's parallel build: 15 minutes "I do" (the trainer thinks aloud through one stage on a small slice, including one mistake caught), 15 minutes "we do" (the room does the same stage on a toy table), then the groups' own work ("you do together") and the passport and viva ("you do alone"). |
| Cognitive apprenticeship | Make expert thinking visible through modelling, coaching, scaffolding and fading, then ask learners to articulate and reflect. | Collins, Brown and Holum (1991): the processes of thinking are invisible in schooling; modelling with real dead ends matters (their Schoenfeld example). | The trainer's think-aloud names one wrong turn every day. The challenges log is the articulation step: one line per decision, in the group's words. |

### 2.1 The approach card with breadcrumbs

The card answers the requester's question of how to hint without handing every group the same answer. It gives the shape of the solution as questions, and each group's constraint card and discovery call make its answers its own.

| Stage | The breadcrumb question on the card | Hint 1 (a question) | Hint 2 (a pointer) | Hint 3 (a worked parallel) |
|---|---|---|---|---|
| 0 The business | Who loses money when this lender is wrong, and how? | "If one loan defaults, whose budget pays?" | Week 5 Friday committee memo | none |
| 1 The frame | At the moment of the decision, what is known, what is predicted, and what changes because of the prediction? | "Which of your columns could the loan officer see at the counter?" | Week 5 Monday framing notebook | A framed fraud problem (a different problem) |
| 2 Requirements | What must the system do, how well, and what may it never do? | "What would the regulator ask about a rejected applicant?" | The FR, NFR and constraints table in the explorer | none |
| 3 Options | What are two ways to make this decision, and what does each cost in rupees, minutes and explanation? | "Could a simple rule do half the job?" | Google's Rules of ML, rule 1 | A filled A-versus-B sheet on churn |
| 4 The POC | Does the model beat doing nothing on the error bill, honestly measured? | "What does approving everyone cost?" | Week 5 Tuesday threshold notebook | A threshold sweep on fraud data, never on the group's own |
| 5 The architecture | Where does the score live, who calls it, and what happens when the curveball lands? | "What breaks if the data arrives a day late?" | The HLD template | none |
| 6 The MVP slice | What is the smallest thing Rohan could use tomorrow? | "What does a loan officer click?" | The starter kit's app stub | none |
| 7 Present and defend | Which one sentence would Rohan act on? | "Say it with the rupee number in it." | The run sheet | none |

Hints are opened only at the daily checkpoint, and each one opened is written into the challenges log. Whether an opened hint costs marks is a rubric question for `data/programme/facts.yaml`; the research supports recording it either way, because the record tells the TA where to coach. Hint 3 is always a worked parallel on a different problem, so a group that opens it learns the method without receiving its own answer. Three groups with different constraint cards will still land on different thresholds, which feeds the Saturday question "why are the others wrong".

The fade across the programme follows the expertise reversal effect and Margulieux's "hints or feedback, not both":

| Build | What the approach card gives |
|---|---|
| Build 2 (Week 6) | All eight breadcrumb questions and three hints per stage |
| Build 3 (Week 9) | The eight questions and hints 1 and 2 only |
| Build 4 (Week 12) | No questions: the group writes its own stage labels and the TA gives feedback on them |
| Build 5 (Week 15) | Nothing beyond the ticket and the rubric |

### 2.2 The A-versus-B sheet

One page, filled at stage 3 and reused on slide 4 and in the viva. It borrows the "alternatives considered" section of Google's design docs (Ubl), which that author calls one of the most important sections because it shows why the chosen design beats the ones a reader would wonder about, and the one-to-two page limit of Nygard's architecture decision records.

| Row of the sheet | Approach A | Approach B |
|---|---|---|
| What it is, in one sentence | | |
| Error bill in Rs at the chosen threshold | | |
| Build time in hours | | |
| Can Rohan explain a rejection to the applicant? | | |
| How it fails, and how you would notice | | |
| Our call, and the one fact that would flip it | | |

Google's Rules of ML gives the room permission to let A be a rule ("If you think that machine learning will give you a 100% boost, then a heuristic will get you 50% of the way there"), and rule 4 makes the simple model the baseline the second is judged against.

## 3. Getting weak learners to read and understand the brief

| Technique | What it is | Evidence | The form it takes in Build 2 |
|---|---|---|---|
| Progressive disclosure | Show the core first and move the rest to a second layer opened on request. | Nielsen Norman Group: it "helps novice users avoid mistakes" and saves time on features they do not need. | Tuesday's reading is one ticket of about 300 words. The data dictionary becomes column cards released when a group names the column it needs. Everything else lives in Rohan's answer sheet. |
| The one-page ticket | The whole ask on one page: who asks, the decision, the metric at stake, the constraint, the deliverable, the day it is due. | Nygard: large specification documents go unread; one to two pages get read and revised. Amazon's 2017 shareholder letter: narratives are read silently at the start of each meeting "in a kind of study hall". | The ticket is read silently by everyone for 6 minutes at the start of Tuesday's group time, on paper or screen, with no AI open. |
| Discovery call where the client answers only what is asked | A role-played client holds the facts and releases each one only to a question that asks for it. | Bano, Zowghi, Ferrari and colleagues (2019, Requirements Engineering): 110 students in 28 groups made 34 kinds of mistakes in role-played elicitation interviews, worst in question formulation, question omission and interview order, and did not improve across three interviews without targeted teaching. The Mom Test (Fitzpatrick, via Shortform): ask about specifics in the past, do not pitch, listen more than you talk. | An 8-minute call per group with "Rohan" on Tuesday, run in three parallel rooms by the trainer and the two TAs (13 calls, about 40 minutes of wall time). Rohan's answer sheet (TRAINER only) holds about 25 facts; a fact nobody asks for stays hidden until the Thursday curveball or the Saturday panel. |
| Question Formulation Technique | Learners produce as many questions as they can, sort them open and closed, then prioritise. | Right Question Institute: four rules (as many as you can, do not stop to discuss or answer, write each as asked, turn statements into questions), then improve, then prioritise. | Ten minutes before the call. Groups produce questions under the four rules, sort them against a category strip (decision, users, error costs, data timing, constraints, success, risks), and send their top seven. Every member asks at least two on the call, which answers Bano's finding on omission and order. |
| Jigsaw | Each member reads one part, meets the members from other groups who read the same part, then teaches it back to their own group. | Aronson's jigsaw.org: segments read only by their owner, expert groups, teach-back, then a quiz. | The ticket and its first column cards split three ways (the client and the decision; the data and its timing; the costs and the deliverable). Each member reads about 150 words, meets the other two members holding the same part across neighbouring groups for 5 minutes, then teaches it in 2 minutes. |
| Readiness check, individual then team | The same short multiple-choice check is taken alone, then again as a group with immediate feedback. | Team-based learning's readiness assurance (Ohio State): it holds each learner accountable to the team and surfaces gaps early. Roediger and Karpicke (2006): testing beat restudying on delayed retention, while restudying felt more confident. | Six items, 4 minutes alone, then 6 minutes as a group. Ungraded, because the programme runs no tests in build weeks; its only consequence is that a group under five of six rereads with a TA before it starts the frame. |
| Restate-back | The team's first output is the client's problem in its own words, checked by the client. | Self-explanation prompts carry a medium effect, g = 0.55 (Bisra and colleagues, 2018, via the TUM Clearinghouse summary). | The last minute of the discovery call: one member, chosen by Rohan, states the decision, the error costs and the deliverable in three sentences. Rohan says "yes" or names the gap. That sentence becomes the first line of slide 1. |

Learner reading load for the whole week, against Build 1's 10,000 words:

| Item | Words |
|---|---|
| The ticket and the group's constraint card | 350 |
| The approach card (questions only; hints are sealed) | 300 |
| The AI sparring card | 200 |
| The numbers passport template | 150 |
| The run sheet and slide skeleton | 250 |
| The GD move card | 150 |
| Column cards, as requested | about 300 |
| Total | about 1,700 |

## 4. AI as a sparring partner

| Technique | What it is | Evidence | The form it takes in Build 2 |
|---|---|---|---|
| Hints-only AI beats answer-giving AI | An AI that gives hints protects learning; an AI that gives answers becomes a crutch. | Bastani and colleagues (PNAS 2025, reported by Knowledge at Wharton): about 1,000 high-school maths students; open GPT-4 lifted practice scores 48 percent and cut exam scores 17 percent against the control; a tutor version giving hints instead of answers lifted practice 127 percent with no exam loss. Lee and colleagues (CHI 2025, Microsoft Research, 319 knowledge workers): more confidence in the AI went with less critical thinking. | The rule is about how AI is used, since banning it cannot be enforced. The sparring card below gives prompts that ask the AI to question, attack or explain back, and none that ask it to produce the group's decision. |
| A course policy that names the tools | CS50 allows its own duck, which is built to guide, and forbids tools that "suggest or complete answers". | CS50 academic honesty policy; Liu, Zenke, Malan and colleagues (SIGCSE 2024): the duck's "pedagogical guardrails" guide students "rather than providing direct solutions". | A one-paragraph Build 2 policy: AI may be used to question, critique and explain; AI may not write the frame, the cost reasoning, the recommendation sentence or the answers in the passport. |
| AI use levels per task | A scale states how much AI each task allows. | AI Assessment Scale (Perkins, Roe, Furze, MacVaugh): five levels from No AI to AI Exploration. | Stages 0 to 2 (business, frame, requirements) at level 1, No AI, on paper on Tuesday. Stages 3 to 6 at level 3, AI Collaboration, logged. Stage 7's defence at level 1, live. |
| Two lanes | Secure tasks verify the learner live; open tasks allow and scaffold AI, and the open lane is not policed. | University of Sydney two-lane FAQ: live questioning after a presentation counts as secure; "don't try to police AI in open tasks"; detection software is unreliable. Mollick's "homework apocalypse": AI text cannot be reliably detected; allow AI on take-home work if students disclose their prompts. | Lane 1 in Build 2: the Tuesday paper frame, the Thursday viva, the passport draws, the Saturday Q&A. Lane 2: the build, the code, the slides. |
| AI in a named role | The AI is cast as mentor, coach, tutor, simulator or student, with a prompt for each. | Mollick and Mollick, "Assigning AI: Seven Approaches" (via Stanford SCALE): keep the student as the human in the loop and guard against over-trust. | The sparring card's five prompts each cast the AI in one role. |
| AI-use log | Every prompt that changed a number, a decision or a slide is recorded with what was kept and how it was checked. | Mollick (disclosure of prompts); the Sydney open lane. | Two extra columns in the challenges log the row already requires ("AI used?" and "How we checked it"), so no new artifact is added. |
| Explain-back gate | Before an AI-written cell is committed, a member who did not prompt it explains it line by line to another member. | Self-explanation, g = 0.55 (Bisra and colleagues, 2018). The AHRQ teach-back tool is the clinical version of the same move (page returned 403; not verified). | A two-minute ritual at every commit of AI-written code; the explainer signs the log line. |

The sparring card (about 200 words, one page):

1. Sceptical risk head (AI as simulator): "Here is our metric and our two error costs. You are Kalpa's head of risk. Argue for the opposite metric. Do not agree with us."
2. Red team (AI as critic): "List three ways this number could be wrong. Do not fix any of them."
3. Interviewer (AI as coach): "Ask me five questions a lending panel would ask about this threshold, one at a time. Do not answer them."
4. Student (AI as student): "I will explain what this cell does. Tell me where my explanation is wrong or vague."
5. Leak hunter (AI as tutor): "Here are our column names and when each is written. Give me the test for leakage, not the answer."

The rule that holds the whole policy together is the passport rule in section 5: any number on any slide can be drawn, and any member reproduces it live from the repository. A group that let AI do its thinking finds that out in front of the panel.

## 5. Assessment nobody can ride

| Technique | What it is | Evidence | The form it takes in Build 2 |
|---|---|---|---|
| Numbers passport | One page per member with the eight to ten numbers the case rests on, each with where it is computed and what it means in one sentence. | Oakley, Felder, Brent and Elhajj (2004): tell teams they "will be examined individually on every aspect of the assignment". Launch School's live assessments leave "no place to hide". | Fields: base rate, the two error costs, the threshold, recall and precision at it, the error bill in Rs, the do-nothing bill, the cross-validation spread, the leaked column and what it did. Each member fills it alone, in their own words, on Thursday morning. At the viva and on Saturday, two numbers are drawn and the member recomputes them from the repository in under 2 minutes. |
| "Not yet" retake | A failed mastery check is recorded as "not yet" with a fixed retake slot, never as a fail. | Launch School mastery-based learning: "Not Yet", then a waiting period and a retake. | A member who cannot reproduce a passport number in Thursday's viva gets one ungraded retake with a TA on Friday, so Saturday's defence is a second exposure, never a first. |
| Random member cold call | The assessor, not the team, picks who answers. | Dallimore, Hertenstein and Platt (2013, via Learning and the Brain): high cold-calling raised voluntary participation and comfort; the 2019 follow-up found women's participation rose more. Numbered Heads Together (Haydon, Maheady and Hunter, 2010): higher quiz scores and on-task behaviour under the random-reporter structure. | Every member rehearses the 90-second opener; the panel draws who delivers it. In Q&A the panel names the member before asking the question. |
| Viva on the group's own work | An oral on the learner's project, built from the project's own decisions. | Sydney: live questioning is the secure lane. Ward and colleagues (2023, DCU interactive orals): in the computing case, consultancy teams advised a client choosing between two technologies, participated as a group and were marked individually; 82 percent of students rated the orals good or very good at encouraging academic integrity. | Mock R2's viva half (Thursday, about 20 minutes each, per the row) draws its questions from four stems: why this metric, what moves if the cost ratio halves, which column you dropped and why, and what would make you switch from A to B. |
| Pre-mortem | The team imagines the project has failed and writes why, before it has. | Klein (HBR, 2007): it makes it safe for people who see weaknesses to voice them during planning. (The often-quoted 30 percent figure was not verified against the 1989 study.) | Wednesday, 15 minutes: "It is Saturday and Rohan rejected your recommendation. Why?" Five minutes alone, three reasons each, then ten minutes to pick the top three to fix or to state as a caveat. The top caveat goes on slide 7. |
| Red-team review between groups | A second group attacks the plan with a set method before the real review. | UK MoD Red Teaming Handbook (third edition, 2021): a red-team mindset any team can apply to its own problems. Structured academic controversy (SERC, Carleton): teams switch sides and argue the other position, then reach a consensus. Murder boards rehearse a hard oral before the real one. | Thursday afternoon, 20 minutes per pair of groups with different constraint cards: 7 minutes each to attack the other's threshold and one passport number with a red-team card (data timing, cost assumption, honesty of evaluation), then each group states in 2 minutes the strongest case for the other's threshold. |
| Team expectations agreement | The team writes and signs how it will work and what happens when someone does not deliver. | Oakley and colleagues (2004): teams of three or four; an expectations agreement; rotating roles; a firing process routed through the instructor. | Tuesday, 10 minutes, five lines: roles, response time, the definition of done, what happens on a missed task, and who raises it with the TA. |
| Peer rating on anchored behaviours | Each member rates themselves and teammates on described behaviours, which flags riders. | CATME (Purdue): five dimensions, contributing, interacting, keeping on track, expecting quality, having relevant knowledge and skills. Oakley and colleagues use peer ratings to set an individual weighting factor. | Five minutes at Saturday's close. Whether it adjusts marks is the evaluation block's decision in `facts.yaml`; as a flag alone it still tells the Programme Head which learner to talk to before Build 3. |

## 6. The 12-minute presentation

Build 1 already had an answer-first format, and the room still spent seven minutes on the problem. The template was never the gap. The fixes below therefore lean on a clock, a run sheet with names on it, and rehearsal, and less on the slide design.

| Technique | What it is | Evidence | The form it takes in Build 2 |
|---|---|---|---|
| Pyramid, answer first, SCQ | Lead with the single point and its support; frame it with situation, complication, question. | Barbara Minto: ideas "organized as a pyramid under a single point"; SCQ for "identifying the question in your reader's mind". | Slide 1 states the recommendation and its error bill in one sentence. Situation, complication and question take 60 seconds, inside slide 1. No slide is titled Agenda, Introduction, Problem statement or About the dataset. |
| Assertion-evidence slides | Each slide's headline is a full-sentence claim, and its body is one picture or chart that proves it. | Penn State (Alley): audiences given assertion-evidence slides understood and remembered more, p < .01 (Garner, Alley and colleagues, 2013); student presenters who built such slides understood their own content better (Aippersbach, Alley and Garner, 2013). | A seven-slide skeleton whose headline boxes are empty sentence frames, for example "At a threshold of __, Kalpa loses Rs __ a month, Rs __ less than today". |
| Fixed slide budget | A hard cap on slides, minutes and font size. | Kawasaki's 10/20/30: no more than 10 concepts in a meeting, finish in 20 minutes to leave time for discussion, 30-point type. | Seven slides, 12 minutes, 24-point minimum on a projector. A backup slide holds the passports. |
| Say what you do, then demo early | State what the thing is in the first sentence and show it working soon after. | Paul Graham, "How to Present to Investors": "Say what you're doing as soon as possible"; demo quickly and keep a local backup. | The live demo runs from minute 3 to minute 6: score one applicant, show the decision and the rupee cost of the error, then change the cost on the constraint card and watch the threshold move. A screen recording and the executed notebook are the backup, as in Build 1. |
| Written memo, read silently | A short narrative replaces slides as the decision document and is read at the start. | Amazon's 2017 letter (six-page narratives, silent reading); Bryar and Carr, Working Backwards (via Next Big Idea Club): writing forces the author to distil ideas. | Optional: a one-page Rohan memo, read silently by the panel for 2 minutes before the talk, so nobody needs the talk to explain the problem. It adds writing load, so it is ranked below the top ten. |
| POC against MVP, FR, NFR, constraints | Separate what the proof showed from what a usable product still needs, and state requirements as functions, qualities and limits. | Lean Startup: the MVP is the first product built to start learning "as quickly as possible". ISO/IEC 25010: a nine-characteristic product quality model, usable as the NFR checklist. Google design docs: goals and non-goals. | Slide 6, "What we proved, and what an MVP still needs", is a three-column table (FR, NFR, constraints) with two non-goals. This plants the Build 5 POC-against-MVP pitch. |
| Run sheet with roles and a timekeeper | Every minute of the talk has an owner, and an outside timer shows time left with coloured cards. | Toastmasters timekeeping (EdUHK club briefing): green at 2 minutes left, amber at 1 minute, red at time up; green means go on, amber means start the conclusion, red means stop. | A member of another group holds the cards. At red plus 30 seconds the panel stops the talk. |
| Murder board rehearsal | A panel of questioners grills the plan before the real review. | Murder board (Wikipedia): used to prepare for demanding oral exams and confirmation hearings. | Two clocked dry runs (section 6.2). |
| What panels score | Interviewers watch structure, reasoning, clarity and business judgment. | BCG case interview page: "how you approach the problem and the quality of your reasoning", "Think Structurally", "Clarify Assumptions", "Show Your Thinking". McKinsey's interviewing page returned 503 (not verified). | The question types are published in advance (metric, threshold, error bill, alternatives, what would change your mind, and why the group with another card chose differently). The questions themselves stay with the panel. |

### 6.1 The run sheet for a group of three

| Minutes | Slide | Who | What is said |
|---|---|---|---|
| 0:00 to 1:30 | 1 | Drawn by the panel | The recommendation and the error bill in one sentence, then situation, complication, question in 60 seconds |
| 1:30 to 3:00 | 2 | Decision owner | What each error costs Kalpa, as one cost picture, and the metric that follows |
| 3:00 to 6:00 | 3 | Builder | The live decision demo |
| 6:00 to 8:00 | 4 | Evaluator | A against B on the error bill, and why we chose |
| 8:00 to 9:30 | 5 | Evaluator | How honest the number is: the do-nothing bill, the cross-validation spread, the leak we caught |
| 9:30 to 11:00 | 6 | Decision owner | What the POC proved, and what an MVP still needs (FR, NFR, constraints) |
| 11:00 to 12:00 | 7 | Builder | What would change our call, the top pre-mortem caveat, and the ask |

Every member speaks for at least three minutes. In the row's Saturday slot of 25 to 30 minutes, the shape is 12 minutes of talk, 12 minutes of questions in role as Rohan's panel (an interactive oral, with the member named before each question), and 2 to 4 minutes for scoring and changeover. That keeps the talk inside the requester's 10 to 15 minutes, and the hard stop sits well under 20.

### 6.2 The rehearsal protocol

| When | Run | Audience | Clock | What changes after it |
|---|---|---|---|---|
| Thursday, late afternoon | Dry run 1 | The red-team partner group | 12 minutes on cards, then a 5-minute murder board | Any section over time loses a slide or a sentence; nobody speeds up |
| Friday | Dry run 2, cold, with the demo started from a fresh kernel | A TA, recorded on a phone | 12 minutes on cards | The group watches the first 90 seconds back; the drawn-opener rule means all three rehearse slide 1 |

The row already asks for two cold demo runs on Friday; dry run 2 is one of them.

## 7. Group discussion for Indian placement rounds

Sources here are practitioner and coaching pages; no official company rubric was found. Hitbullseye lists what assessors look for: knowledge of the topic, teamwork, personal contribution, logical reasoning, creativity and communication, in groups of about 10 to 15 with 2 to 5 minutes to prepare and 10 to 20 minutes to discuss. Its placement page adds the case-based GD, where "the symptoms should not be mistaken for the root problem", and names addressing the whole group and summarising at the end as scored behaviours. The row sets about 30 minutes per GD round on risk and lending, unprepared by design, as a thread separate from the project.

| Technique | What it is | Evidence | The form it takes in Build 2 |
|---|---|---|---|
| Four moves | A learner enters with one of four moves: frame, angle, bridge or close. | Hitbullseye: contribution, logic, teamwork and summarising are scored; short points with data; no interrupting. | The GD move card: Frame ("The decision here is __, and it matters to __"). Angle ("From the __ side, the number that matters is __"). Bridge ("Building on [name]'s point, __" or "I see it differently because __"). Close ("We have heard two positions; __ wins when __, and __ wins when __"). |
| Angle cards | Six named viewpoints a learner can pick up when stuck. | This serves the requester's aim of thinking from several angles; structured academic controversy (SERC) trains arguing the other side. | Customer, lender's profit and loss, risk and regulator, data and model, operations, fairness. |
| Fishbowl practice with observers | Half the room discusses while the other half each scores one speaker on a sheet, then they swap. | Assessor criteria above; Oakley and colleagues on peer feedback against described behaviours. | Wednesday and Thursday, 20 minutes each: 10 minutes of discussion, 10 minutes of observer feedback. The observer sheet has five anchored rows: content with a number, building on others, structure and summary, inviting a quiet member, composure under interruption. |
| Contribution rules | A few hard rules weak speakers can follow under pressure. | Hitbullseye: "quality matters more than quantity"; avoid speaking just to fill time and stating incorrect facts. | Three to five contributions of 20 to 40 seconds; one carries a number; one builds on a named person; if you have not spoken by the midpoint, take the summary. |

## 8. What bootcamps and industry programmes changed

| Programme or study | What they found or changed | What Build 2 takes from it |
|---|---|---|
| Launch School (mastery-based learning) | It argues time-boxed bootcamps produce uneven skills, so it replaced time with mastery: oral technical evaluations, one-to-one live coding interviews, take-home challenges, and "Not Yet" with a retake. | The passport draw, the "not yet" retake on Friday, and the viva as the moment of truth. |
| Tenhunen, Männistö, Luukkainen and Ihantola (2023), review of 127 software engineering capstone studies | Typical capstones run one term with teams of four or five working for a client, deliver prototype-level software, and assess throughout the project in many forms. | Daily checkpoints and stage gates instead of one end-of-week grade, and a client (Rohan) the groups actually talk to. |
| Ward and colleagues (2023), DCU interactive orals, building on Griffith University's practice since 2015 | Orals run as unscripted, scenario-based conversations; computing teams advised a client choosing between two technologies and were marked individually; students rated them highly for integrity and authenticity. | The Saturday questions run in role, and each member is scored individually. |
| Rayid Ghani, Data Science for Social Good and CMU's Scopeathon | "The largest gap is often the lack of a well-designed and well-executed scoping process up front." Scoping covers goals and trade-offs, possible actions, the data on hand, and the analysis with its ethics. | Tuesday is scoping day, and stages 0 to 2 are AI-free and on paper. |
| Oakley, Felder, Brent and Elhajj (2004) | Three- and four-person teams; expectations agreements; rotating roles; individual examination on every part; peer-rating weighting; firing through the instructor. | Groups of three, the five-line agreement, the passport, the peer rating. |
| PBLWorks Gold Standard project design | Critique and revision, reflection, and a public product are among the seven essential elements. | The red-team swap is the critique; the dry runs are the revision; the GitHub README, written answer first, is the public product the 20-Week Plan asks for. |
| Kirschner, Sweller and Clark (2006) | Minimal guidance fails novices until their prior knowledge carries them. | The approach card and the breadcrumb notebook are justified for a room at 3 out of 10, and fade by Build 5. |

## 9. The week on one page

Minutes are durations. The row's own items (the online launch, the allocation, the daily checkpoint, the parallel build, Mock R2, the GDs, the presentations) keep their places; the techniques above sit inside them.

| Day | Ladder stages | Added rituals and their minutes |
|---|---|---|
| Tuesday (online) | 0, 1, 2 | Expectations agreement 10. Silent ticket read 6, jigsaw 10, readiness check 10. QFT 10, discovery call 8 per group in three rooms (about 40 of wall time) ending in the restate-back. Parsons card 10. Stages 0 to 2 on paper with no AI, 30 alone then together. |
| Wednesday | 3, 4 | "I do, we do" opening 30 inside the parallel build. Approach card hints at the checkpoint. A-versus-B sheet 20. Pre-mortem 15. GD fishbowl 20. Recommendation sentence at close-out, per the row. |
| Thursday | 5, 6 | Passports filled alone 20 in the morning. Mock R2 viva with two passport draws, about 20 per learner, per the row. The curveball. Red-team swap 20 per pair. Dry run 1, 17 per group. GD fishbowl 20. |
| Friday | freeze, 7 | "Not yet" retakes with a TA, 5 per learner who needs one. Dry run 2 cold, recorded, 12. GD rounds and the first presentations, per the row. |
| Saturday | 7 | Presentations in a 25 to 30 slot: 12 talk with a drawn opener, 12 questions in role with members named, the rest for scoring. Peer rating 5 at close. |

## 10. The ten that move this room most for the least load

Ranked by how directly each one attacks a Build 1 failure, divided by the minutes it costs learners and the hours it costs staff to prepare.

| Rank | Technique | Failure it attacks | Learner minutes in the week | Staff preparation | Evidence type |
|---|---|---|---|---|---|
| 1 | Numbers passport with live reproduction by a drawn member, and a "not yet" retake | Could not explain their numbers; AI as ghostwriter | About 30 | One template and a draw list | Practitioner (Oakley, Launch School) plus secure-lane policy (Sydney) |
| 2 | The 12-minute run sheet: answer first in 90 seconds, seven assertion-evidence slides, an outside timekeeper with cards | Seven minutes on the problem | Planning only | One skeleton and three cards | Controlled study (Alley, p < .01), practitioner (Minto, Kawasaki) |
| 3 | One-page ticket plus a discovery call where Rohan answers only what is asked, opened by a 10-minute QFT | Nobody read; no business nuance | About 30 | Ticket, a 25-fact answer sheet, three role-players for 40 minutes | Empirical (Bano and colleagues), practitioner (Mom Test, QFT, NN/g) |
| 4 | Two clocked dry runs, the first as a murder board with the red-team partner | Over-running talk; panic under questions | About 30 | One TA on Friday | Practitioner (Toastmasters, murder boards) |
| 5 | The approach card: eight breadcrumb questions with a sealed three-step hint ladder, faded build by build | Lost novices pasting the brief into AI | Built into the work | One card and 24 hints, written once and reused | Experimental (subgoal labels, worked-example fading, expertise reversal) |
| 6 | Two-lane AI policy with the sparring card, an AI-use log folded into the challenges log, and the explain-back gate | AI as ghostwriter | About 10 a day | One page | Field experiment (Bastani), survey (Lee), course policy (CS50, Sydney) |
| 7 | Drawn opener and member-named questions on Saturday | Riders; silent members | Rehearsal of 90 seconds each | None | Field studies (Dallimore, Numbered Heads Together) |
| 8 | The A-versus-B sheet, reused on slide 4 and in the viva | No trade-off thinking; no answer to "why are the others wrong" | 20 | One sheet | Experimental (comparing methods), practitioner (design docs, ADRs) |
| 9 | Jigsaw of the ticket with an ungraded individual-then-team readiness check | Nobody read | 26 | Six items | Experimental (testing effect), practitioner (TBL, jigsaw) |
| 10 | Pre-mortem on Wednesday and red-team swap on Thursday | No business nuance; weak caveats; brittle defence | 35 | Two cards | Practitioner (Klein, MoD handbook, structured controversy) |

The GD move card with fishbowl practice (section 7) would be eleventh. It is cheap, but it serves the GD thread, which the row keeps separate from the project.

## 11. Points the orchestrator has to settle

1. The tracker row says groups of four, three groups per sub-problem, fifteen groups at target intake. The requester's direction of 29 October (in the draft spine) sets 13 groups of three on one shared problem with a constraint card each. The requester wins, and the row needs its keeps and drops recorded.
2. The programme runs no tests in build weeks. The readiness check, the Parsons card and the passport retake are written here as ungraded gates; if any of them is to carry marks, that is a change to the build-week rule.
3. Marks and weights are locked at the build level (mini project 40, mock 30, GD 30), and the Build 2 rubrics are open in `facts.yaml`. Whether an opened hint, the peer rating or the drawn opener moves a mark is the rubric's decision; nothing above assumes a number.
4. The discovery calls need three role-players for about 40 minutes on Tuesday. The row says Build 2 owners are still to be confirmed.
5. The draft spine's constraint cards are the engine that makes three groups' answers differ. Each card should change at least one of the two error costs or add one NFR (for example a reason for every rejection, or a latency ceiling at the app), so that the panel's "why are the others wrong" has a real answer. Those card examples are illustrative and were not taken from a source.

## 12. Sources

All checked 29 October 2026.

| Source | URL | Status |
|---|---|---|
| Renkl and Atkinson (2003), example study to problem solving | https://asu.elsevierpure.com/en/publications/structuring-the-transition-from-example-study-to-problem-solving--2 | Verified (record and abstract) |
| Kirschner, Sweller and Clark (2006), Educational Psychologist 41(2) | https://www.davidlewisphd.com/courses/EDD8121/readings/2006-Kirschner_et_al.pdf | Verified (abstract read) |
| Expertise reversal effect (Kalyuga and colleagues, 2003) | https://en.wikipedia.org/wiki/Expertise_reversal_effect | Verified (secondary); the UOW repository record returned 403, not verified |
| Margulieux and Catrambone (2016), subgoal learning and self-explanation | https://escholarship.org/uc/item/35z8842x | Verified (full text read) |
| Ericson (2018), Parsons problems dissertation | https://hg.gatech.edu/node/603172 | Verified |
| Collins, Brown and Holum (1991), cognitive apprenticeship | https://www.isls-naples.psy.uni-muenchen.de/intro/all-webinars/collins/cognitive-apprenticeship.pdf | Verified (full text read) |
| Fisher and Frey, gradual release, 3rd edition | https://ascd.org/books/better-learning-through-structured-teaching-a-framework-for-the-gradual-release-of-responsibility-3rd-edition | Verified; the LINCS page returned 403, not verified |
| Star and Rittle-Johnson, comparing methods (Harvard GSE) | https://www.gse.harvard.edu/ideas/usable-knowledge/08/12/developing-flexibility-math-problem-solving | Verified |
| Bisra and colleagues (2018), self-explanation, TUM Clearinghouse summary | https://www.clearinghouse.edu.tum.de/wp-content/uploads/2023/09/CHU-KR-25_ENG_Bisra_2018_Selbsterklaerungen.pdf | Verified; the SFU repository sat behind a bot check, not bypassed, not verified |
| Nielsen Norman Group, progressive disclosure | https://www.nngroup.com/articles/progressive-disclosure/ | Verified |
| Jigsaw classroom | https://www.jigsaw.org/ | Verified |
| Bano, Zowghi, Ferrari and colleagues (2019), elicitation interview mistakes | https://par.nsf.gov/biblio/10105611-teaching-requirements-elicitation-interviews-empirical-study-learning-from-mistakes | Verified |
| The Mom Test, three rules (Shortform summary) | https://www.shortform.com/blog/what-is-the-mom-test/ | Verified (secondary); https://www.momtestbook.com/ verified as the book page |
| Question Formulation Technique | https://rightquestion.org/what-is-the-qft/ | Verified |
| Readiness assurance, iRAT and tRAT (Ohio State) | https://ipe.osu.edu/readiness-assurance-tests-team-based-learning-irat-and-trat | Verified |
| Roediger and Karpicke (2006), test-enhanced learning | https://profiles.wustl.edu/en/publications/test-enhanced-learning-taking-memory-tests-improves-long-term-ret/ | Verified |
| CS50 academic honesty policy | https://cs50.harvard.edu/x/honesty/ | Verified |
| Liu, Zenke, Malan and colleagues (SIGCSE 2024), Teaching CS50 with AI | https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf | Verified (full text read) |
| Bastani and colleagues (PNAS 2025), via Knowledge at Wharton | https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education | Verified |
| Lee and colleagues (CHI 2025), GenAI and critical thinking | https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/ | Verified |
| AI Assessment Scale | https://aiassessmentscale.com/ | Verified |
| University of Sydney, two-lane FAQ | https://educational-innovation.sydney.edu.au/teaching@sydney/?p=21264 | Verified |
| Mollick and Mollick, Assigning AI (Stanford SCALE record) | https://scale.stanford.edu/ai/repository/assigning-ai-seven-approaches-students-prompts | Verified; the SSRN page returned 403, not verified |
| Mollick, The Homework Apocalypse | https://www.oneusefulthing.org/p/the-homework-apocalypse | Verified |
| AHRQ teach-back, Tool 5 | https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html | Not verified (403) |
| Ward and colleagues (2023), interactive oral case studies, DCU | https://doras.dcu.ie/30854/1/InteractiveoralassessmentcasestudiesAninnovativeacademicallyrigorousauthenticassessmentapproach%281%29.pdf | Verified (full text read) |
| Dallimore, Hertenstein and Platt, cold-calling, via Learning and the Brain | https://www.learningandthebrain.com/blog/updating-the-great-cold-call-debate-does-gender-matter/ | Verified (secondary) |
| Haydon, Maheady and Hunter (2010), Numbered Heads Together | https://digitalcommons.memphis.edu/facpubs/10545 | Verified |
| Oakley, Felder, Brent and Elhajj (2004), Turning student groups into effective teams | https://www.cs.upc.edu/~idss/WorkingTeams/turnin_student_groups_into_effective_teams.pdf | Verified (full text read) |
| CATME teamwork dimensions | https://info.catme.org/ | Verified; the CMU CATME page returned 404 |
| Klein (2007), Performing a project premortem, HBR | https://hbr.org/2007/09/performing-a-project-premortem | Verified (opening only); the 30 percent figure not verified |
| UK MoD Red Teaming Handbook, third edition | https://www.gov.uk/government/publications/a-guide-to-red-teaming | Verified |
| Structured academic controversy (SERC, Carleton) | https://serc.carleton.edu/sp/library/sac/how.html | Verified |
| Murder board | https://en.wikipedia.org/wiki/Murder_board | Verified (secondary) |
| Barbara Minto, the Pyramid Principle | https://www.barbaraminto.com/ | Verified |
| Penn State, research on assertion-evidence slides (Alley) | https://writing.engr.psu.edu/research.html | Verified |
| Amazon 2017 letter to shareholders | https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders | Verified |
| Bryar and Carr, Working Backwards (Next Big Idea Club) | https://nextbigideaclub.com/magazine/working-backwards-insights-stories-secrets-inside-amazon-bookbite/26769/ | Verified; workingbackwards.com returned 403, not verified |
| Kawasaki, the 10/20/30 rule (Entrepreneur) | https://www.entrepreneur.com/business-news/rule-of-thumb/192718 | Verified |
| Paul Graham, How to Present to Investors | https://paulgraham.com/investors.html | Verified |
| BCG, case interview preparation | https://careers.bcg.com/global/en/case-interview-preparation | Verified |
| McKinsey, interviewing | https://www.mckinsey.com/careers/interviewing | Not verified (503, three attempts) |
| Toastmasters timekeeper briefing (EdUHK club) | https://www.eduhk.hk/cle2/editor_images/documents/clubied/Toastmaster/Briefing%20for%20Time%20keeper.pdf | Verified (club document) |
| Hitbullseye, GD tips | https://mba.hitbullseye.com/acad/Group-Discussion-Tips.php | Verified (coaching site) |
| Hitbullseye, placement GD and PI | https://cpt.hitbullseye.com/interview-process.php | Verified (coaching site) |
| Launch School, mastery-based learning | https://public.launchschool.com/mastery | Verified (the school's own page) |
| Tenhunen and colleagues (2023), capstone review | https://arxiv.org/abs/2301.03554 | Verified |
| CMU Scopeathon, Rayid Ghani on scoping | https://www.cmu.edu/news/stories/archives/2022/april/cmu-scopeathon-ties-data-science-to-better-communities | Verified; the DSSG scoping post returned 503, not verified |
| PBLWorks, Gold Standard project design | https://www.pblworks.org/what-is-pbl/gold-standard-project-design | Verified |
| Google, Rules of Machine Learning | https://developers.google.com/machine-learning/guides/rules-of-ml | Verified |
| Ubl, Design Docs at Google | https://www.industrialempathy.com/posts/design-docs-at-google/ | Verified |
| Nygard, Documenting Architecture Decisions | https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions | Verified |
| ISO/IEC 25010 product quality model | https://iso25000.com/index.php/en/iso-25000-standards/iso-25010 | Verified in part (nine characteristics; four named in the page text) |
| The Lean Startup, principles | https://theleanstartup.com/principles | Verified |
| Google re:Work, Project Aristotle | https://rework.withgoogle.com/en/guides/understanding-team-effectiveness | Not verified (404); not used |
| Thayer and Ko (2017), barriers faced by bootcamp students | https://dblp.org/pid/07/11105 | Not verified (seen in search results only, page not opened); not used |

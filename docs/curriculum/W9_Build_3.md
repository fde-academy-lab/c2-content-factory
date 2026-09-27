# W9 Build 3

## Mon 30 Nov 2026 · Build 3 · Online project introduction; the guided NLP track opens; groups scope their Kalpa Connect sub-problem

### Business scenario of the day

KALPA CONNECT, THE BUILD 3 UNIT. Kalpa Connect sells mobile, broadband and subscription plans to eleven million customers in India. Ananya Bose, its COO, has watched Retail's assistant work take shape and has a harder version of every problem: more tickets, angrier customers, and churn that shows up in support text weeks before it shows up in billing. Her data is real, messy and unfamiliar: support chat transcripts, call summaries, plan changes, network incident logs, and churn outcomes. Groups of four take one of five sub-problems, three groups per sub-problem.
THE FIVE SUB-PROBLEMS, each requiring controlled, structured output with a written contract: (1) Churn early warning from support text plus activity, with the target defined before it is predicted. (2) Ticket triage into a fixed schema, where a malformed output is a failed ticket. (3) Network incident summarisation for the operations desk, with a length and a citation contract. (4) Plan recommendation from chat transcripts, with a refusal rule when the transcript is ambiguous. (5) Support-reply drafting with a cost ceiling per reply and a repeatability requirement.
Every sub-problem is the Week 7 and 8 method under a contract. Your role all week: you are the engineer Ananya will question, and the mock and GD panels will ask for your contract, your dials, your cost per run, and what broke.

MONDAY. The Programme Head introduces the build week online: the five sub-problems, the group-of-four structure, the week's shape, and the AI-free debug drill on Wednesday morning. Ananya's briefing note is in the pack.

### Thinking we train, before any tool

The first move is the output contract: what shape the answer must take, what a violation looks like, what the model must refuse. The second is the cost ceiling from Week 8 Friday. A group that starts from the prompt rather than the contract has skipped the move the week trains.
The forward deployed move of this build is alternatives and ruling out. Every group tables three options for its sub-problem, a rule, a classical text model and an LLM call, scores the cheap ones first on a hold-out it set aside before any modelling, and lets the LLM in only where it beats the baseline by enough to pay for itself.

### Trainer agenda

1. The Programme Head introduces the build week online (60 min).
2. Sub-problem allocation: fifteen groups at target intake, three per sub-problem (30 min).
3. NLP track, clinic 1, on the pack's sample of transcripts: text preparation (cleaning, normalising, sentence and word tokens, stop words, stemming against lemmatisation) and the labelled hold-out set aside before any model (45 min).
4. NLP track, clinic 2: bag of words and TF-IDF with word pairs, and the no-LLM baseline that fits each sub-problem, scored on the hold-out (45 min).
5. Groups scope, write the output contract and dial profile, table their three options, and open the challenges log (rest of day).
6. Close-out: scopes pinned; tomorrow's checkpoint stated (15 min).

### Learner outcome

THIS WEEK DEMONSTRATES: model literacy, unaided debugging, classical NLP used as the honest baseline, and controlled output under a contract and a budget.
TODAY: a scoped sub-problem per group with the output contract drafted, three options tabled, a hold-out set aside, and a live challenges log.

### Subtopics (technique in service of the scenario)

• Online project introduction by the Programme Head
• Five sub-problems, three groups each
• The output contract and the dial profile
• The challenges log opened
• No new teaching content beyond the guided NLP track, which the build itself uses

### Trainer notes

STRUCTURE: groups of four; build Monday to Thursday with the trainer's parallel build and daily checkpoints, and the expert days on Friday and Saturday; the week has no holiday, so the Wednesday catch-up reserve stands.
THE NLP TRACK: three 45-minute clinics (two today, one on Tuesday) and a notebook ladder on the pack's sample. The baseline that fits each sub-problem: a linear classifier on TF-IDF features for churn and for triage, TF-IDF sentence ranking for the incident summary, keyword rules for plan recommendation, and the nearest past reply by TF-IDF similarity for drafting. The track is the one exception to 'no new content in a build week', and it carries no test.
STAFFING: Build 3 mock owners are to be confirmed; behavioural and HR questioning joins the mock from this round, so brief the room today.
THE DRILL: Wednesday morning, observed, assistant-free, each learner debugs a deliberately broken training loop from evidence alone.

### Client zero data (TRAINER ONLY)

Real messy Kalpa Connect data at scale, re-labelled from public sources into the persona: transcripts, call summaries, plan changes, incident logs, churn flags. Not the Retail spine.

### In-session exercises

• Scoping worksheet: task, output contract, refusal rule, dial profile, cost ceiling, and the three options tabled (rule, classical, LLM).
• NLP track notebook 1: text preparation and the hold-out.
• Challenges log, entry one.

### After-class tasks

• Draft the output schema tonight.
• NLP track notebook 2: TF-IDF and the no-LLM baseline on the pack's sample.

### Interview angle

• [S] You have joined a telecom; how would you apply what you did on retail support tickets to our data, and what changes?
• [S] TF-IDF: what does it reward, and where does it fail?
• [F] What is an output contract for an LLM feature, and why does a malformed output count as a failure?
• [F] When would you not use an LLM for a text problem?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Build-week pack: the five briefs with contracts, assessor rubric, GD prompts, the parallel build, checkpoints, the staged broken loops for the drill, the NLP track notebooks with a labelled sample of transcripts, scoring sheet, catch-up plan.
• scikit-learn 1.9 user guide, text feature extraction: bag of words, TF-IDF, n-grams (verified 19 Sep 2026):
https://scikit-learn.org/stable/modules/feature_extraction.html
• scikit-learn example, classification of text documents using sparse features (verified 19 Sep 2026):
https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html
• Jurafsky and Martin, Speech and Language Processing, third edition draft, for text normalisation and the classical baselines (verified 19 Sep 2026):
https://web.stanford.edu/~jurafsky/slp3/

### Student references

• The Week 8 tab is the revision surface; the brief rewards Thursday's dials and Friday's cost model.
• scikit-learn user guide, text feature extraction (verified 19 Sep 2026):
https://scikit-learn.org/stable/modules/feature_extraction.html

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Tue 01 Dec 2026 · Build 3 · Build day two: the no-LLM baseline on the board, then the first prompt under the contract

### Business scenario of the day

KALPA CONNECT, BUILD 3 (context in Monday's row). TUESDAY. Ananya's data lands: chat transcripts full of agent shorthand, call summaries in two languages, and churn flags that arrive weeks after the conversations they belong to. The trainer's parallel build on a smaller slice sets the pace. The rule for the day is baseline first: the no-LLM number goes on the board before any prompt is written.

### Thinking we train, before any tool

The build runs baseline first, so that every later gain has something to be measured against. The first prompt then carries a role and rules in the system prompt, the output contract stated inside it, and examples only where a zero-shot attempt has failed on the hold-out.

### Trainer agenda

1. Daily checkpoint: each group shows its output contract and its hold-out (30 min).
2. NLP track, clinic 3: first prompt patterns: the system prompt, zero-shot against few-shot, the output contract written into the prompt (45 min).
3. The trainer's parallel build shared; groups build the no-LLM baseline, score it on the hold-out, then write the first prompt against the contract (rest of day).
4. Close-out: each group states its baseline number, or names its blocker (15 min).

### Learner outcome

TODAY: a baseline number per group on the hold-out, a first prompt running under the output contract, and the challenges log moving.

### Subtopics (technique in service of the scenario)

• Daily checkpoint: the contract and the hold-out
• NLP track, clinic 3: system prompt, zero-shot against few-shot, the contract in the prompt
• The no-LLM baseline, scored
• The parallel build
• The first prompt under the contract

### Trainer notes

THE DAY CAME BACK: with teaching starting on 5 October, Guru Nanak Jayanti falls in Week 8, so Build 3 has its Tuesday again. Clinic 3 moves here from Wednesday, and Wednesday regains the catch-up reserve.
CLINIC 3 stays at first patterns; prompt techniques compared, structured outputs and function calling belong to Week 10.
PUSH: no prompt before the baseline number is on the board.

### Client zero data (TRAINER ONLY)

Groups work their own scoped cut of the Kalpa Connect data; the trainer's slice stays deliberately smaller.

### In-session exercises

• Checkpoint questions.
• NLP track notebook 3: one task prompted zero-shot and few-shot, scored on the hold-out.
• The baseline number, written and pinned.
• Build time.

### After-class tasks

• Build continues; challenges log entries as they happen.
• PREP: the AI-free debug drill runs tomorrow morning; reread the Week 7 Wednesday diagnosis write-ups.

### Interview angle

• [F] Zero-shot against few-shot: when does an example earn its tokens?
• [F] What goes in a system prompt, and what does not?
• [D] Your LLM version beats the TF-IDF baseline by two points and costs fifty times more per ticket; what do you recommend?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• The parallel build and the checkpoints from the pack.
• Prompt Engineering Guide, the techniques index: zero-shot and few-shot (verified 21 Sep 2026):
https://www.promptingguide.ai/techniques
• Claude Platform Docs, Prompt engineering overview (verified 21 Sep 2026):
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

### Student references

• The Week 8 Friday cost model is the template for this week's cost ceiling.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Wed 02 Dec 2026 · Build 3 · The AI-free debug drill, the catch-up reserve, then the build at pace

### Business scenario of the day

KALPA CONNECT, BUILD 3 (context in Monday's row). WEDNESDAY. The observed, assistant-free debug drill runs in the morning: each learner is handed a broken training loop and diagnoses it from the evidence alone. The catch-up reserve follows for any Week 7 or 8 backlog, and the build then runs at pace against the contract and the cost ceiling.

### Thinking we train, before any tool

Week 7 Wednesday under observation: evidence first, verdict second, no assistant. It is the week's signature assessment moment and runs before build fatigue sets in.
The build then measures every change against Tuesday's baseline number: quality on the hold-out, cost per run against the ceiling, and the contract violations caught.

### Trainer agenda

1. The observed drill, per roster: a broken training loop diagnosed from evidence, with the write-up in the fixed shape (morning).
2. Daily checkpoint: each group states its LLM number beside its baseline number (30 min).
3. Catch-up block from the catch-up plan, for any Week 7 or 8 backlog, released to build time otherwise (up to 90 min).
4. The trainer's parallel build shared; groups build against their output contract and their cost ceiling (rest of day).
5. Close-out: one blocker per group aloud (15 min).

### Learner outcome

TODAY: the drill completed and observed for every learner, an LLM number beside the baseline for every group, and the build moving against the contract and the ceiling.

### Subtopics (technique in service of the scenario)

• The AI-free observed debug drill
• Daily checkpoint: the LLM number beside the baseline
• The catch-up reserve, used or released
• The parallel build
• Build against the output contract and the cost ceiling

### Trainer notes

THE DRILL runs first, before build fatigue sets in; the staged loops come from the pack with fresh seeds.
THE CATCH-UP RESERVE is back now that the week has no holiday; it absorbs teaching backlog by design.

### Client zero data (TRAINER ONLY)

The broken loops are staged identically for every learner; the build continues on each group's scoped brief.

### In-session exercises

• The observed debug drill.
• Checkpoint questions, with both numbers.
• Build time.

### After-class tasks

• Build continues; challenges log entries as they happen.

### Interview angle

• [S] Walk me through debugging a training run that would not converge, from evidence to fix.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• The staged broken loops, the parallel build, the checkpoints and the catch-up plan from the pack.

### Student references

• The Week 7 Wednesday diagnosis write-ups, reread before the drill.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Thu 03 Dec 2026 · Build 3 · Mock R3 opens, with behavioural questioning; build completion

### Business scenario of the day

KALPA CONNECT, BUILD 3 (context in Monday's row). THURSDAY. Mock R3 opens: individual, asynchronous, half technical on deep learning and LLM fundamentals, half a viva on the group's work, with behavioural and HR questioning included from this round. Groups complete the build with quality measured and cost reported.

### Thinking we train, before any tool

The viva probes the contract and the cost model: why this schema, why these dials, what a thousand runs cost, what broke and what you changed. It also asks why an LLM at all: the group shows its no-LLM baseline beside the LLM on quality and on cost per thousand items, and defends the gap. The behavioural half rewards accuracy over polish; oversold claims cost marks.

### Trainer agenda

1. Mock R3 roster through the day: individual, asynchronous, roughly 20 minutes each, behavioural half included (all day).
2. Groups complete the build: the baseline-against-LLM comparison table on quality and cost, decisions documented (all day).
3. Close-out: assessor impressions on the fixed rubric (15 min).

### Learner outcome

TODAY: scheduled learners mocked with the behavioural half live, and the app measurably working within its contract and ceiling.

### Subtopics (technique in service of the scenario)

• Mock R3: technical, viva, behavioural
• Quality and cost measured; the comparison table: no-LLM baseline against the LLM option
• The challenges log as viva material

### Trainer notes

BEHAVIOURAL: from R3 the mock probes self-presentation and project narrative; coach accuracy over polish. STAFFING: Build 3 mock owners to confirm.

### Client zero data (TRAINER ONLY)

The viva half runs on the group's own Kalpa Connect work.

### In-session exercises

• Mock R3 per roster.
• Build completion with measured quality and cost.

### After-class tasks

• Presentation drafted; one cold demo run including a contract violation handled.

### Interview angle

• [S] Tell me about a time a model you built produced an output you could not ship; what did you do?
• [D] Your baseline reaches most of the LLM's quality at a fraction of the cost; what do you recommend to the COO?
• [D] Defend your dial settings and cost ceiling to a COO who wants the reply cheaper and more reliable at the same time.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Mock rubric and scoring sheet from the pack.
• Interview Query, the DL and LLM items for technical-half calibration (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions

### Student references

• The challenges log, reread before the viva.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Fri 04 Dec 2026 · Build 3 · Expert day one: GDs at thirty minutes per group, first presentations

### Business scenario of the day

KALPA CONNECT, BUILD 3 (context in Monday's row). FRIDAY. The industry expert arrives for two days. GD rounds run at about 30 minutes per group on the problem space of automated support and its risks; first presentations run where the roster allows. Builds freeze tonight, and every rehearsal must include the failure path.

### Thinking we train, before any tool

The GD is unprepared by design; the week's problem space, automation that talks to customers, makes the risk argument the centre of every round.

### Trainer agenda

1. The industry expert opens; GD rounds at about 30 minutes per group (rolling roster).
2. Groups not in a GD complete the build and rehearse the demo cold, including a contract violation caught and handled (parallel).
3. A first tranche of presentations before the expert where the roster allows (afternoon).
4. Close-out: Saturday's presentation order drawn (10 min).

### Learner outcome

TODAY: every group through its GD or scheduled for Saturday morning, builds frozen, demos cold-proof with the failure path.

### Subtopics (technique in service of the scenario)

• Expert-led GDs, 30 minutes per group
• Build freeze and cold rehearsal with the failure path
• First presentation tranche

### Trainer notes

DEMO RULE: the rehearsal must include the failure path; a happy-path-only demo scores as incomplete tomorrow. FREEZE tonight.

### Client zero data (TRAINER ONLY)

GD topics run at progressive complexity as a separate thread from the mini project.

### In-session exercises

• GD rounds per roster.
• Two cold demo runs including the failure path, logged.

### After-class tasks

• Final polish only.

### Interview angle

• [F] Take a position on whether a support reply should ever go out without a human reading it, and defend it.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• GD prompts, facilitation notes and the scoring sheet from the pack.

### Student references

• The one-slide answer: contract, baseline number, quality number, cost number, caveat, action.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Sat 05 Dec 2026 · Build 3 · Expert day two plus the flown-in leader: presentations, defence, grade closure, the two-month close

### Business scenario of the day

KALPA CONNECT, BUILD 3 (context in Monday's row). SATURDAY. Ananya's questions get their answers. Groups present with live demos, failure path demanded, before the industry expert and the senior industry leader who flies in for the day. Every Build 3 grade closes today, and with it the first two months of the programme.

### Thinking we train, before any tool

Three groups per sub-problem means the panel hears three contracts for the same job and asks each group why the others chose differently. The closing relay names the arc the room built: records, files, SQL, pandas, models, networks, tokens, controlled output.

### Trainer agenda

1. Remaining GD rounds close in the morning (per roster).
2. Presentations with live demos, roughly 25 to 30 minutes per group, failure path demanded, split between the expert and the flown-in leader (through the day).
3. Rubric scoring rolling; every Build 3 grade closes today (end of day).
4. Two-month close: the arc from Meera's first question to Ananya's assistant said aloud; one improvement per group for the GenAI module (15 min).

### Learner outcome

TODAY: every group presented, demoed and defended, every Build 3 grade closed, and the two-month arc said aloud by the room.

### Subtopics (technique in service of the scenario)

• Remaining GDs
• Presentations with the failure path
• Open questioning
• In-week grade closure
• The two-month arc

### Trainer notes

PANEL SPLIT: the expert and the leader divide the roster; silent teammates get questioned separately. CLOSURE: all grades close today on the fixed rubric.

### Client zero data (TRAINER ONLY)

Demos run cold on the group's Kalpa Connect inputs with the contract enforced in front of the room.

### In-session exercises

• Presentations, demos and defence.

### After-class tasks

• Rest. Week 10 opens the applied GenAI module: Farhan's assistant, built properly, from Kalpa's own policies.

### Interview angle

• [S] Present an LLM feature to a COO and take a challenge on its cost and its failure path.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Presentation format and scoring sheet from the pack.

### Student references

• None tonight.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

# W15 Build 5

## Mon 11 Jan 2027 · Build 5 · Online project introduction; groups scope their Kalpa Retail agent and write its golden trajectories first

### Business scenario of the day

KALPA RETAIL AT SCALE, THE BUILD 5 UNIT. Fifteen weeks ago Meera Raghavan asked where growth comes from and where it leaks. The answers the room gave her by hand are still produced by hand every week. Farhan's assistant has shown that an agent can act inside limits, and now five owners in Kalpa Retail each want one, on real data at full scale and in full mess. Groups of four take one of five sub-problems, three groups per sub-problem.
THE FIVE SUB-PROBLEMS, each an agent that is evaluated, guarded and deployed, with its cost per task reported: (1) For Anand Iyer, the reconciliation agent: it matches payments to orders every night, explains each mismatch and drafts the exceptions note, and it may never write to the books. (2) For the head of Retail-Plus, the retention agent: it finds members whose spend has fallen two months running and drafts a save offer inside a discount limit, with anything above it sent for approval. (3) For the marketing lead, the campaign analyst agent: it answers 'did my campaign work' with a like-for-like comparison, and declines to claim a cause when no fair comparison exists. (4) For the data platform lead, the warehouse question agent: it turns a business question into a read-only query under a row and cost budget, shows the query, and refuses anything that writes. (5) For Farhan Sheikh, the returns agent at full volume: the system of Weeks 13 and 14 on every ticket type, with its every-time pass rate by type.
Every sub-problem is a method from Weeks 1 to 5, now carried out by an agent built with the method of Weeks 13 and 14. Your role all week: you are the engineer these owners will question, and the panels will ask for your golden trajectories, your guardrails, your cost per task, and what broke.

MONDAY. The Programme Head introduces the build week online, under the rule that no new material is taught. Groups scope their agent, decide how much autonomy it needs, write its golden trajectories before any code, and open the challenges log.

### Thinking we train, before any tool

The first move is the least-autonomy rule from Week 13 Tuesday: for each part of the job, a fixed workflow unless the task truly needs the model to choose its next step. The second is Week 14 Monday's: the golden trajectories are written before the agent exists, with the steps that must happen in order, the steps that may happen in any order and the steps that must never happen. An owner's 'never', such as never writing to the books or never claiming a cause without a fair comparison, becomes structure on day one and is not left to a sentence in a prompt.

### Trainer agenda

1. The Programme Head introduces the build week online: sub-problems, groups of four, the week's shape (60 min).
2. Sub-problem allocation: fifteen groups at target intake, three per sub-problem (30 min).
3. Groups scope the agent, choose workflow or agent for each part, write ten golden trajectories with their never steps, and open the challenges log with entry one (rest of day).
4. Close-out: scopes and golden trajectories pinned; tomorrow's checkpoint stated (15 min).

### Learner outcome

THIS WEEK DEMONSTRATES: an agentic system for a named owner that is evaluated, guarded and deployed, with its cost per task reported and its failures shown.
TODAY: a scoped agent with its autonomy justified, ten golden trajectories, each owner's 'never' written as structure, and a live challenges log.

### Subtopics (technique in service of the scenario)

• Online project introduction by the Programme Head
• Five Kalpa Retail owners, three groups each
• Workflow or agent, decided part by part
• Golden trajectories written before any code
• Each owner's 'never' as structure
• The challenges log opened
• No new teaching content

### Trainer notes

STRUCTURE: groups of four for the mini project, the GDs and the presentations; build Monday to Thursday with the trainer's parallel build and daily checkpoints; the industry expert attends Friday and Saturday only; a senior industry leader flies in on Saturday. Grades close in-week.
UNIT: client zero section 5 sends the last build back to Kalpa Retail at scale. The transfer this week runs across five owners and five earlier methods, and no longer across units.
ME3 no longer sits in this week. It moved to early Week 16 on 21 September, so the build, the mock, the GD and the presentation are the only things assessed here.
STAFFING: Build 5 mock and GD owners are to be confirmed. INTERVIEWS: live interviews may be running; a learner released for one hands over to the group and logs it.
ASSISTANTS: permitted on build work in this phase; every line must be defended in the viva.

### Client zero data (TRAINER ONLY)

Real messy Kalpa Retail data at full scale, re-labelled from public sources into the persona: orders, payments, memberships, campaigns, the warehouse and the ticket stream. Not the seeded teaching spine.
PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked): the five sub-problem seeds above, each owned by a stakeholder already in the v2.2 table, so that no new name is added.
The five briefs and the data pack are build-week artifacts.

### In-session exercises

• The autonomy worksheet: each part of the job marked workflow or agent, with the reason.
• Ten golden trajectories, with the never steps.
• Challenges log, entry one.

### After-class tasks

• Groups begin the tool set against their own scope; challenges log entries as they happen.

### Interview angle

• [S] Walk me through how you decide whether a task needs an agent at all.
• [F] Your stakeholder says 'it must never write to the books'; where does that rule live in your system?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Build-week pack: the five Kalpa Retail briefs, the data pack, assessor rubric, GD prompts, the parallel build, daily checkpoints, presentation scoring sheet, catch-up plan.

### Student references

• The Week 13 and Week 14 tabs are the revision surface; the project rewards both weeks' whole method.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Tue 12 Jan 2027 · Build 5 · Build day two: the tool set and the controlled flow, one golden task end to end

### Business scenario of the day

KALPA RETAIL AT SCALE, BUILD 5 (context in Monday's row). TUESDAY. The owners' systems open up: the full warehouse, the payments feed with its retries and orphans, the membership and campaign tables, the ticket stream. The trainer's parallel build on a smaller slice sets the pace. By close of day each group has a tested tool set and a controlled flow that completes one golden ticket end to end.

### Thinking we train, before any tool

Week 13's order holds: tools are tested one call at a time before any loop exists, write tools are narrow and refuse by default, and the owner's limits are edges in the flow. One golden task completed end to end, with its trace, is worth more today than five tools half built.

### Trainer agenda

1. Daily checkpoint: each group answers the day's three checkpoint questions in two minutes (30 min).
2. The trainer builds a smaller slice of one agent in the open and shares the day's progress (60 min).
3. Groups build: the tool set tested call by call, the flow with the owner's limits as edges, tracing on from the first run (rest of day).
4. Close-out: one golden task shown end to end per group, or one blocker named aloud (15 min).

### Learner outcome

TODAY: every group holds a tested tool set, a controlled flow with the owner's limits as edges, and one traced golden task completed end to end.

### Subtopics (technique in service of the scenario)

• Daily checkpoint questions
• The trainer's parallel build, shared in the open
• The tool set, tested one call at a time
• The controlled flow, with limits as edges
• Tracing on from the first run

### Trainer notes

THE PARALLEL BUILD sets pace and shows method without handing over answers. CHECKPOINTS: a group with no end-to-end task by tonight is stuck and should say so today. WATCH FOR: a single broad write tool, or a limit that lives only in the prompt; both are Week 13's planted mistakes returning.

### Client zero data (TRAINER ONLY)

Groups work their own owner's systems; the trainer's slice stays deliberately smaller.

### In-session exercises

• The day's three checkpoint questions per group.
• Build time against the group's own plan.

### After-class tasks

• Build continues; challenges log entries as they happen.

### Interview angle

• [F] Show me one tool from your agent and tell me why it is that narrow.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Parallel build and checkpoint questions from the pack.

### Student references

• Week 13 Monday's tool test sheet is the model for this week's.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Wed 13 Jan 2027 · Build 5 · Build day three: evaluated, guarded and deployed, plus the catch-up reserve

### Business scenario of the day

KALPA RETAIL AT SCALE, BUILD 5 (context in Monday's row). WEDNESDAY. Each owner asks for the same three things by end of day: how often the agent gets it right every time, what stops it doing harm, and what one task costs. The catch-up reserve sits in the morning for any Week 13 or 14 backlog. In the afternoon the agent leaves the notebook and runs as a service.

### Thinking we train, before any tool

The week's forward deployed move is the pitch that separates a proof of concept from a first product. What the group will show on Saturday proves the agent can work on a slice. The page drafted today says what would have to be true before the owner could rely on it every night: the volumes, the hand-over, the on-call, the monthly cost. Naming that gap is what earns trust, and it is the question every client asks second.

### Trainer agenda

1. Daily checkpoint (30 min).
2. Catch-up block from the catch-up plan, for any Week 13 or 14 backlog, released to build time otherwise (up to 120 min).
3. Groups run the trajectory suite with repeated runs, add the guardrails with a test for each, report cost per task, and deploy the agent as a service beyond localhost (rest of day).
4. The proof-of-concept against first-product page drafted (30 min).
5. Close-out: each group states its three numbers and its one open risk (15 min).

### Learner outcome

TODAY: each group holds an every-time pass rate, a tested guardrail for each of the owner's limits, a cost per task, a deployed service, and a draft of the proof-of-concept against first-product page.

### Subtopics (technique in service of the scenario)

• Daily checkpoint
• The catch-up reserve, used or released
• The trajectory suite with repeated runs
• One test per guardrail
• Cost per task
• Deployed beyond localhost
• The forward deployed move: proof of concept against first product

### Trainer notes

THE CATCH-UP RESERVE absorbs teaching backlog by design. PUSH: numbers are stated today, so that Thursday and Friday test them and do not produce them. The deployment target is the one used in Week 14 Friday.

### Client zero data (TRAINER ONLY)

Groups remain on their owner's systems; every claim cites the group's own suite, traces and costs.

### In-session exercises

• Checkpoint questions.
• The three numbers, written and pinned.
• The proof-of-concept against first-product page, draft.

### After-class tasks

• Evidence gaps closed; presentation skeleton drafted on the claim, evidence, caveat, action shape.

### Interview angle

• [S] What is the difference between a proof of concept and a product, for the system you just built?
• [D] State your agent's reliability in one sentence that an owner could repeat to her board.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• The catch-up teaching plan from the pack.

### Student references

• Week 14 Monday's report and Tuesday's reply to the reviewer are the models for this week's evidence.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Thu 14 Jan 2027 · Build 5 · Mock R5 as a two-round simulation; build completion

### Business scenario of the day

KALPA RETAIL AT SCALE, BUILD 5 (context in Monday's row). THURSDAY. Mock R5 runs as a two-round simulation, the shape of a real hiring loop: a technical screen on retrieval, agents and production, and then, for the same learner later in the day, a deep dive on the group's agent with behavioural questioning. Groups complete the build around the roster.

### Thinking we train, before any tool

Round one asks what any screen asks, fast. Round two probes ownership: which component was yours, which decision you would defend, what broke and what you changed. Prepared answers break where the challenges log is thin, and a learner with a live interview this month should treat today as the rehearsal it is.

### Trainer agenda

1. Mock R5 round one per roster: individual, roughly 15 minutes, a technical screen (morning).
2. Mock R5 round two per roster: individual, roughly 20 minutes, a project deep dive with behavioural questioning (afternoon).
3. Groups complete the build around the roster (all day).
4. Close-out: assessor impressions on the fixed rubric (15 min).

### Learner outcome

TODAY: every scheduled learner through both rounds against the fixed rubric, and the build materially complete.

### Subtopics (technique in service of the scenario)

• Mock R5 round one: the technical screen
• Mock R5 round two: the project deep dive, with behavioural questioning
• Build completion
• The challenges log as interview material

### Trainer notes

MOCK R5 runs as two rounds for every learner; the split of minutes between the rounds is proposed and is set with the mock owners, who are to be confirmed. RUBRIC fixed; grades close in-week.
CALENDAR: Makar Sankranti (Uttarayan), Thursday 14 January 2027, is a restricted holiday on the central list and a working day there. If the institute's calendar closes the campus, round one moves to Wednesday afternoon and round two runs on Friday beside the GDs.

### Client zero data (TRAINER ONLY)

The deep dive runs on the group's own Kalpa Retail agent.

### In-session exercises

• Mock R5, both rounds, per roster.
• Build completion.

### After-class tasks

• Presentation drafted; the demo path rehearsed once, with a guardrail refusing live.

### Interview angle

• [S] Walk me through the agent you built: its tools, its flow, its guardrails, and one number you are proud of.
• [D] Tell me about the component you owned, and one decision in it that you would now make differently.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• The mock rubric and scoring sheets for both rounds, from the pack.
• DataCamp, Top 30 Agentic AI Interview Questions and Answers for 2026, for round-one calibration (verified 21 Sep 2026):
https://www.datacamp.com/blog/agentic-ai-interview-questions

### Student references

• The group's challenges log, reread before round two.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Fri 15 Jan 2027 · Build 5 · Expert day one: GDs at thirty minutes per group, first presentations

### Business scenario of the day

KALPA RETAIL AT SCALE, BUILD 5 (context in Monday's row). FRIDAY. The industry expert arrives for two days. GD rounds run at about 30 minutes per group on the problem space of letting software act on a business's behalf; first presentations run where the roster allows. Builds freeze tonight, and every rehearsal shows a guardrail refusing and the agent recovering.

### Thinking we train, before any tool

The GD trains structured articulation under time pressure on the week's problem space; it is scored on the fixed rubric, and it is unprepared by design.

### Trainer agenda

1. The industry expert opens; GD rounds at about 30 minutes per group (rolling roster).
2. Groups not in a GD complete the build and rehearse the demo cold, including a guardrail refusal and the recovery from it (parallel).
3. A first tranche of presentations before the expert where the roster allows (afternoon).
4. Close-out: Saturday's presentation order drawn (10 min).

### Learner outcome

TODAY: every group through its GD or scheduled for Saturday morning, builds frozen, demos cold-proof with the failure path included.

### Subtopics (technique in service of the scenario)

• Expert-led GDs, 30 minutes per group
• Build freeze and cold rehearsal
• The guardrail refusal and the recovery, in every rehearsal
• First presentation tranche

### Trainer notes

ROSTER ARITHMETIC: fifteen groups at 30 minutes is about 7.5 hours of GD, spanning both expert days by design. DEMO RULE: a demo that shows only the successful path scores as incomplete tomorrow. FREEZE tonight.

### Client zero data (TRAINER ONLY)

GD topics run at progressive complexity as a separate thread from the mini project.

### In-session exercises

• GD rounds per roster.
• Two cold demo runs, logged.

### After-class tasks

• Final polish only.

### Interview angle

• [F] Take a position in a group discussion on how much a business should let an agent do unattended, and defend it with one number.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• GD prompts, facilitation notes and the scoring sheet from the pack.

### Student references

• The one-slide answer: claim, evidence, caveat, action.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

## Sat 16 Jan 2027 · Build 5 · Expert day two plus the flown-in leader: presentations, defence, grade closure

### Business scenario of the day

KALPA RETAIL AT SCALE, BUILD 5 (context in Monday's row). SATURDAY. Five owners get their agents. Groups present with live demos before the industry expert and the senior industry leader who flies in for the day, each demo shows a guardrail refusing and the agent recovering, and each group closes on what separates its proof of concept from a first product. Every Build 5 grade closes today. Major Exam 3 opens Week 16 on Monday.

### Thinking we train, before any tool

Three groups per owner means the panel hears three answers to the same question of how much autonomy the job needed, and asks each group why the others chose differently. The closing relay names the arc the room has built since Week 1: a number computed by hand, a query, a model, a network, a prompt, a retrieval system, an agent that acts inside limits.

### Trainer agenda

1. Remaining GD rounds close in the morning (per roster).
2. Presentations with live demos, roughly 25 to 30 minutes per group, the failure path demanded, each closing on proof of concept against first product, split between the expert and the flown-in leader (through the day).
3. Rubric scoring rolling; every Build 5 grade closes today (end of day).
4. Fifteen-week close: the arc from Meera's first question to five agents said aloud; ME3's scope restated for Monday, without marks or slot (15 min).

### Learner outcome

TODAY: every group presented, demoed and defended, every Build 5 grade closed, and the fifteen-week arc said aloud by the room.

### Subtopics (technique in service of the scenario)

• Remaining GDs
• Presentations and live demos, the failure path demanded
• Proof of concept against first product, as the closing slide
• In-week grade closure
• The fifteen-week arc

### Trainer notes

PANEL SPLIT: the expert and the leader divide the roster; silent teammates get questioned separately. CLOSURE: all grades close today on the fixed rubric; the graded components are the GD score, the mini project score including the presentation, and the mock score. ME3 is on Monday in the first half of the day; say its three theme areas and nothing about marks.

### Client zero data (TRAINER ONLY)

Demos run cold against the owner's systems in front of the room.

### In-session exercises

• Presentations, demos and defence.

### After-class tasks

• REVISE: ME3 covers RAG, agents and production; the Week 11, 13 and 14 tabs and your own failure catalogues are the revision surface.

### Interview angle

• [S] Present an agent to the owner of the process it automates, and take a challenge on what it must never do.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Presentation format and scoring sheet from the pack.

### Student references

• The Week 11, 13 and 14 rows, for Monday.

### Kahoot quiz plan

No tests run during build weeks, so no Kahoot today.

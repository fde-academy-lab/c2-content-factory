# W17-20 Capstone

IITGN COHORT 2  ·  WEEKS 17 TO 20  ·  CAPSTONE  ·  ONE PLAN FOR EVERY BRIEF: PROPOSE, BUILD, DEPLOY AND DEFEND ONE KALPA SYSTEM  ·  25 JAN TO 20 FEB 2027

## Wk 16 Sat · 23 Jan 2027 · Announcement

### The question the week answers

What am I building, for whom, and how will it be judged?

### What every group does, whatever its brief

The Programme Head announces the capstone. Each group receives one brief in one theme area, and different groups receive different briefs. Every brief names a Kalpa unit, a stakeholder role, an ask with a solution already attached, and leaves the constraints for discovery to find. The group reads the brief and writes the ten questions it would ask the client.

### The gate, and who reviews

There is no gate. The Programme Head allocates the briefs with each learner's declared role track in view.

### What exists at the gate

Each group holds its brief, the group list, the gate calendar and a repository created from the capstone template.

### How the evidence reads, by kind of system

THEME AREAS (proposed, to be confirmed at the announcement):
1. Decision support from data (analyst track).
2. Prediction under unequal error costs (data science track).
3. Grounded assistants with citations (GenAI track).
4. Agents that act within limits (agentic track).
5. Taking a working system into a new unit's environment (forward deployed fitment).
Each brief sits in one Kalpa unit and in one or two theme areas.

### Mentor and TA notes

Briefs follow the Week 16 shape: a stakeholder's ask and a trainer-only client card, with no data witness unless a client-zero version adds one. Mode and rubric follow the evaluation schema sent to the AOC; confirm both before the announcement. Group size follows the allocation, and every member owns a named component and defends it alone.

### Placement running alongside

Interviews are already running. Each learner's brief is matched to the role track they are interviewing for, so the capstone becomes the project they talk about.

### Interview angle

• [S] What are you building for your capstone, for whom, and why that?

## Wk 17 · 25 to 30 Jan 2027 · Frame, propose, walking skeleton

### The question the week answers

What does this client need, which option do we back, and does the thinnest version run end to end?

### What every group does, whatever its brief

Discovery with the brief's client, played from the client card, and the one-page discovery note. Options that differ in kind, one without AI, quantified; option A recommended with B and C kept on the page. The component sheet with one request traced. The evaluation plan written before the build: the success number, the golden set or hold-out, the baseline. The work split, with one named owner per component. Then the walking skeleton: the thinnest version that runs end to end in the repository, in a container, with the baseline number recorded. The challenges log opens on day one.

### The gate, and who reviews

GATE 1, midweek: the proposal review. A mentor and the Academic TA hear the proposal in fifteen minutes and approve the scope, cut it, or send it back once.
WEEK-END CHECK: the skeleton starts on a clean machine from the README.

### What exists at the gate

The solution file holds pages one to three: the discovery note, the recommendation page and the component sheet. The evaluation plan and the owner list are written, the repository runs a skeleton behind a first pipeline, the baseline number is recorded, and the challenges log is open.

### How the evidence reads, by kind of system

Decision support: the metric defined so it cannot be gamed, reconciled against a source of truth.
Prediction: the baseline to beat, and the two error costs in rupees.
Grounded assistant: the golden question set with expected sources.
Agent: the golden trajectories and the cost per task.
Forward deployed: the constraints the new unit imposes, each with its test.

### Mentor and TA notes

Scope is the commonest failure: approve what the group can finish by gate 3, and write down what was cut. Republic Day, Tuesday 26 January 2027, falls in this week, so gate 1 moves a day. From Week 16 assistants are accelerators with disclosure, and every line must be defended without help.

### Placement running alongside

Interview windows are protected: a learner released for an interview hands over to the group and logs it. A JD-driven preparation slot runs before each interview. The weekly funnel review is internal.

### Interview angle

• [S] Walk me through how you scoped your project.
• [F] What did you decide not to build, and why?
• [D] Your first version had to run end to end in a week; what did you leave out?

## Wk 18 · 1 to 6 Feb 2027 · Build the core, measured

### The question the week answers

Does the core work on the real path, and do the numbers say it is getting better?

### What every group does, whatever its brief

The core features, built against the evaluation harness. Every change that matters is logged with its number, so the group can show a curve and not a claim. The controls that fit the kind of system go in: validation and refusal, guardrails, budget caps. Cost per run or per task is tracked from the first day. The Week 16 pipeline runs on every push. Members review one component that is not theirs, so nobody defends code only they have read.

### The gate, and who reviews

GATE 2, end of week: the mentor checkpoint. A live run on the real path, the evaluation numbers against the baseline, the cost per run, and the design-to-build delta against the Week 17 component sheet.

### What exists at the gate

The core works on the real path, the first evaluation report and the cost sheet exist, the pipeline is green, and the challenges log holds at least one failure that changed the design.

### How the evidence reads, by kind of system

Decision support: the numbers reconcile, and the refresh runs unattended.
Prediction: the model beats the baseline on the chosen metric, with the threshold set from the costs.
Grounded assistant: retrieval and generation scored separately, citations checked.
Agent: trajectory scores, guardrail tests, cost per task.
Forward deployed: the system passes the new unit's constraint tests.

### Mentor and TA notes

A group that is behind cuts scope at this gate, in writing, with the mentor; it does not keep a scope it cannot defend. Watch the commit history for a member who has stopped contributing, and ask that member the gate's questions.

### Placement running alongside

Interviews continue with their preparation slots. The behavioural clinic uses this week's challenges log as the raw material for 'tell me about a time it broke'.

### Interview angle

• [S] How do you know your system works? Show me the number.
• [F] What broke this week, and what did you change?
• [D] A teammate's component failed the evaluation; how did the group handle it?

## Wk 19 · 8 to 13 Feb 2027 · Harden, deploy, document, rehearse

### The question the week answers

Could the client's team run this after we leave, and can each of us defend it?

### What every group does, whatever its brief

Deployment beyond localhost through the pipeline, with a release and a rehearsed, timed rollback. The threat review, the red-team set in the pipeline, and the responsible-use pages agreed with the client. Tests in layers. The documents a successor needs: README, architecture note, runbook, evaluation report, cost model. Feature freeze at midweek and code freeze at the gate. Defence drills: every member answers for their own component and for one that is not theirs. The demo is rehearsed against a clock, including the failure the group will show on purpose.

### The gate, and who reviews

GATE 3, end of week: the dress rehearsal and the freeze. The Programme Head or a mentor asks the panel's questions, and the Academic TA checks the repository against the checklist.

### What exists at the gate

The system is deployed and has a link, the solution file is complete with its risk register, the successor documents and the final evaluation report are written, the rehearsal is recorded, and the tag is frozen.

### How the evidence reads, by kind of system

Every kind: a stranger can start the system from the README, the rollback is timed, and the evaluation report states what the system cannot do.
Forward deployed adds the handover page for the client's team.

### Mentor and TA notes

The demo shows one failure on purpose and the recovery from it, which a panel trusts more than a clean run. No new features after midweek, whatever the group says.

### Placement running alongside

Portfolio pass: the capstone README, the recorded demo and the CV line are written this week, while the detail is fresh. Interviews and their preparation slots continue.

### Interview angle

• [S] Give me the two-minute version of your capstone.
• [F] How is it deployed, and how would you roll it back?
• [D] What can your system not do, and how did you find that out?

## Wk 20 · 15 to 20 Feb 2027 · Demo, defence, closure

### The question the week answers

Can we show it working and defend every decision, in front of people who build such systems?

### What every group does, whatever its brief

The live demo and panel defence run in the first half of the week: the system running, one deliberate failure and its recovery, the numbers, and questions to each member on their own component and on one other. After the defence come written feedback, the finished portfolio, the final external panel mocks, the closure formalities and the start of post-programme support.

### The gate, and who reviews

THE DEFENCE: an industry panel with the Programme Head. The capstone grade closes in the week, on a rubric that balances the repository with the presentation and the defence. Marks and weights live in Structure.

### What exists at the gate

The demo is delivered, the grade is closed, feedback is in writing, the public portfolio page is live, the final mock feedback is given, and the closure checklist is signed.

### How the evidence reads, by kind of system

Every kind: the panel asks each group what it would do differently with four more weeks, and asks each member why their component is built the way it is.

### Mentor and TA notes

Order the demos so that groups with live interviews that week present first. The programme office lists the closure formalities; this tab names none it cannot source.

### Placement running alongside

Final external panel mocks, with written feedback inside the week. Offer support and post-programme support begin. The Week 0 baseline card is read once more beside the final mock.

### Interview angle

• [S] Walk me through your capstone end to end.
• [F] What would you do differently?
• [D] Defend one decision the panel disagreed with.

STANDING RULES FOR EVERY BRIEF. Module 10 carries 3 credits and 60 hours, planned as 18, 18, 18 and 6 hours across the four weeks; the remaining campus hours in these weeks belong to the placement thread. Each group proposes, builds, deploys and defends one Kalpa system end to end. The Week 16 solution file is the template. The challenges log is kept live and becomes interview material. Assistants are accelerators with disclosure, and the defence assumes every decision can be justified without one. Every member owns a named component. Scope is cut in writing at a gate and never silently.

| Module 10 | Wk 17 hours | Wk 18 hours | Wk 19 hours | Wk 20 hours | Total hours | Against Module 10 (60 hours); inputs are in blue |
|---|---|---|---|---|---|---|
| Planning split | 18 | 18 | 18 | 6 | 60 | Reconciles to 60 hours |

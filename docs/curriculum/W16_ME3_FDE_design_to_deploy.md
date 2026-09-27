# W16 ME3 + FDE design to deploy

## Mon 18 Jan 2027 · Major Exam 3, then client discovery · What Dr Menon needs, which is more than what she asked for

### Business scenario of the day

THE WEEK. The week opens with Major Exam 3, in the first half of Monday, and then turns to the forward deployed block. Farhan's assistant now answers Kalpa Retail's customers and acts within limits. Dr Priya Menon, COO of Kalpa Health, has seen it work and wants it in her diagnostics business. The week takes her ask from the first client conversation to a thin slice running in a container with a release, a rollback and a test suite, and one file grows with it: the solution file. On Saturday every group receives its own capstone brief and starts the same walk with a different client.

MONDAY. After the exam, Dr Menon, on a call with the team: "Farhan's assistant is exactly what my customers need. Bookings, report status, home collection, all of it. Copy it into Kalpa Health and have it live next month."
Your role: you are the forward deployed engineer on the call. You may not propose anything until you can say what she needs to change, how she will know it changed, and what her business will not allow.
On the table: what she said she wants and what she needs; who decides, who pays, who uses it and who can block it; the number that would move; what her systems, her data and her regulator allow.

### Thinking we train, before any tool

The four questions from Week 0 return with a client in the room: the pain, the people, the number, the unknowns. A request to copy what worked elsewhere hides three differences the engineer has to find by asking. The problem may differ, since her phone lines may be jammed by one kind of call. The constraints differ, since medical data cannot travel the way an order number can. The cost of a wrong answer differs, since a wrong refund is money and a wrong word about a report is harm.
Discovery is finished when the engineer can write one page the client would sign: the problem in her words, the success number with its guardrail, the people, the constraints, and the open questions with an owner for each. Forward deployed interviews reject most often for proposing before scoping, so the day trains the pause.

### Trainer agenda

1. Major Exam 3: RAG, agents and production. The first half of the day is reserved for it; the length and the paper are the Programme Head's call, and no artifact states marks (first half of the day).
2. Dr Menon's ask, read aloud; every group writes its instinctive proposal in five minutes, and the sheets go on the wall unread (15 min).
3. The discovery conversation as a skill: the four questions at client depth, open against closed questions, asking for a number, asking what would make this fail; the people map of decider, payer, user and blocker (45 min).
4. Simulated discovery, round one: groups interview the client, played from the trainer-only client card, which releases a fact only when the right question is asked (50 min).
5. Constraints discovery: systems, data, regulation, budget and date; each group lists the gaps it will close in round two (20 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a client's ask arrives with a solution attached; discovery finds the problem, the people, the number and the constraints before any proposal.
CAN DO: run a client conversation that surfaces the people, the constraints and a candidate success number, and list the gaps a second round must close.
CAN HANDLE: a senior client who has already chosen the solution and wants a date, and a fact that only surfaces when the right question is asked.
CAN DEFEND: every question on the list, by naming the decision its answer changes.
STATUS: Major Exam 3 is graded, and its marks are stated nowhere here.

### Subtopics (technique in service of the scenario)

• Major Exam 3 (RAG, agents and production), in the first half of the day
• The four questions at client depth: the pain, the people, the number, the unknowns
• Open against closed questions; asking for a number; asking what would make this fail
• The stated problem against the real one, with the evidence for each
• The people map: decider, payer, user, blocker
• Constraints discovery: systems, data, regulation, budget, date
• The gaps list for round two

### Trainer notes

ME3: moved here from Week 15 on 21 September, so that Build 5's mini project, mock and GD no longer share a week with a major exam. It covers RAG, agents and production, and it posts wholly to Module 9. Say the scope aloud and nothing about marks.
START FROM: Week 0's four questions and the framing move drilled in every build week; today raises them from a paper case to a live client.
GO AS FAR AS: every group has run one discovery round and holds a written list of the gaps it must close on Tuesday.
STOP BEFORE: any option, any architecture, any tool.
COMES LATER: Tuesday closes discovery with round two and the one-page note, then turns the note into options and a recommendation; Wednesday draws the components and pitches; Thursday and Friday ship a thin slice; Saturday secures and tests it.
WHAT WAS COMPRESSED: discovery and options now share a day and a half in place of two days. Week 0 taught both moves, and Builds 4 and 5 drilled quantified options and the proof-of-concept pitch, so the second worked quantification and part of the constraints block gave way.
WHAT THE ROOM REVEALS: expect the proposals on the wall to copy the retail assistant; discovery shows why that fails in Kalpa Health. Let the groups say so themselves.
THE CLIENT: the Programme Head or the trainer plays Dr Menon from the client card, in character, and answers only what is asked.
CUT FIRST: the constraints block folds into round two. Never cut the wall of proposals, and never cut Tuesday's second discovery round.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (19 Sep 2026, not yet locked): the Week 16 ask comes from Dr Priya Menon and reuses Kalpa Health as Build 1 left it. No new named stakeholder, no dataset and no planted data witness.
THE CLIENT CARD (trainer only; each fact is released only when a group asks the question that earns it): most calls to her centres ask for report status, and booking is already handled by an app; report content is medical data and her legal team will not let it leave Kalpa Health's own systems; her IT team exposes report status through one internal interface and nothing else; a wrong statement about a report is a clinical risk, so anything about results must hand over to a person; she needs something visible before the next quarterly review.
Nothing a learner reads names these facts.

### In-session exercises

GUIDED: one discovery question improved together, from closed to open, then asked of the client.
UNGUIDED: round one of simulated discovery in groups of four, then the gaps list.
MID-SESSION (15 min): sort twelve statements from round one into known, assumed and must ask.

### After-class tasks

• WRITE: the three questions you most want answered in round two, each with the decision its answer changes.
• READ: the decomposition interview guide, the clarify and scope sections.
• SETUP: nothing to install today.

### Interview angle

• [S] A client says 'we need what that other team has'; what do you ask before you propose anything?
• [F] Walk me through how you would scope an ambiguous customer problem.
• [F] How do you tell the stated problem from the real one, and what evidence do you look for?
• [D] A senior client has already promised her board a date for a solution you think is wrong; how do you run the next ten minutes of that call?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Aced (formerly Exponent), the forward deployed engineer interview guide (verified 19 Sep 2026):
https://www.tryexponent.com/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde
• Aced (formerly Exponent), the decomposition interview guide: clarify, scope, then solve (verified 19 Sep 2026):
https://www.tryexponent.com/blog/decomposition-interview

### Student references

• Aced (formerly Exponent), the decomposition interview guide: clarify, scope, then solve (verified 19 Sep 2026):
https://www.tryexponent.com/blog/decomposition-interview

### Kahoot quiz plan

• Q1: the four questions before any proposal, in order
• Q2: closed or open: five questions sorted fast
• Q3 trap: the client names the solution; is that the problem, true or false
• Q4: decider, payer, user, blocker: match four people from the call
• Q5: which of these is a success number and which is a guardrail
• Return question from Week 14: name two guardrails an agent needs before it acts on a customer's behalf.

## Tue 19 Jan 2027 · Discovery closed, then options, trade-offs and a quantified recommendation · One signed page, three choices, two ruled out, one with numbers

### Business scenario of the day

TUESDAY. The morning closes discovery: a second conversation with Dr Menon on the gaps from Monday, and the one-page note she would sign. She reads it before lunch. "Fine, so it is mostly report-status calls. I still want the assistant. My CFO wants to know what it costs and why we cannot just hire four more people for the phones. Bring me choices, and tell me which one you would bet on."
Your role: you bring her three options that differ in kind, rule two out with reasons she and her CFO would accept, and put numbers on the one you recommend.
On the table: what the options are, including the ones with no AI in them; what you optimise for and what you accept; what each option costs to build and to run, how long until it works and what can go wrong; what is a proof of concept and what is a first product.

### Thinking we train, before any tool

Solution thinking starts wide and narrows on purpose, the Week 0 move at full depth. Options must differ in kind: more people on the phones, a status line that reads the report system and speaks a fixed script, an assistant that answers status and hands results to a person. The criteria are written before the scoring, and each is a quantity: cost to build, cost to run per month, weeks to first value, quality on the client's success number, and the risk carried. The token arithmetic from Week 8 and the cost work from Week 10 give the run cost; a rough effort size gives the build cost; every number carries its assumption.
A proof of concept answers 'can it work' on a slice; a first product answers 'will they use it' end to end. The recommendation names option A and keeps B and C on the page as considered alternates, because a client who sees only one option has been sold to.

### Trainer agenda

1. Simulated discovery, round two, on the gaps from Monday; the success number and its guardrail agreed with the client (40 min).
2. The one-page discovery note, written and pinned; Monday's proposals come off the wall and each group marks what discovery changed (35 min).
3. Dr Menon's reply and her CFO's question; options that differ in kind, with the no-AI option always on the table; ruling-out criteria written before scoring (35 min).
4. Trade-off metrics: what you optimise and what you accept; five measures made into quantities (35 min).
5. Quantifying: run cost from call volumes and tokens, build effort sized in person-weeks, risk named and rated; every number with its assumption (50 min).
6. Proof of concept against first product; option A as the recommendation with B and C as considered alternates (25 min).
7. Guided then unguided: the option table and the recommendation page, then a five-minute challenge round with the CFO's questions (60 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: discovery ends in one page the client would sign; options differ in kind, criteria come before scores, every number carries its assumption, and a proof of concept and a first product answer different questions.
CAN DO: agree a success number and a guardrail with a client, write the one-page discovery note, build an option table with five quantified measures, rule two options out aloud, and write the recommendation page.
CAN HANDLE: a CFO who prefers hiring people, and a number that turns out to rest on a guess.
CAN DEFEND: 'why this and why not that', with the run cost per month and the assumption behind it.

### Subtopics (technique in service of the scenario)

• Discovery, round two; the success number and its guardrail, agreed with the client
• The one-page discovery note (page one of the solution file)
• Options that differ in kind, one of them with no AI
• Ruling-out criteria, written before the scoring
• Trade-off metrics: what you optimise for and what you accept
• Quantifying an option: build effort, run cost per month, weeks to first value, quality on the success number, risk
• Assumptions stated beside every number
• Proof of concept against first product
• The recommendation page: option A, with B and C as considered alternates (page two of the solution file)

### Trainer notes

START FROM: Monday's first discovery round and its gaps list; the token and cost arithmetic from Weeks 8, 10 and 14; the ruling-out move from Build 3, where the LLM had to beat a no-LLM baseline; the quantified options of Build 4.
GO AS FAR AS: every group holds a discovery note the client would sign, an option table, and a one-page recommendation that survives five minutes of the CFO's questions.
STOP BEFORE: components and wiring, which are Wednesday's; vendor selection and real price lists, since prices move and are fixed at the day build.
COMES LATER: Wednesday designs option A, and Wednesday afternoon pitches the solution proposal, which is assessed.
WHAT THE ROOM REVEALS: expect the first tables to score options on words such as 'better' and 'easier'; the challenge round shows that only quantities survive a CFO.
CUT FIRST: the proof-of-concept block folds into the recommendation page. Never cut the second discovery round, the no-AI option or the challenge round.

### Client zero data (TRAINER ONLY)

PROPOSED FOR v2.3: call volumes and staffing figures for Kalpa Health's centres are needed for the run-cost arithmetic and are not in client zero; they are fixed at the day build and recorded in v2.3. Until then this row carries no numbers.
THE CLIENT CARD adds one fact, released on request: hiring for the phone lines has been tried, and attrition undid it.
Token prices are marked as illustrative wherever they appear.

### In-session exercises

GUIDED: one option quantified together on all five measures.
UNGUIDED: round two of discovery and the one-page note; then the group's option table, two options ruled out aloud, and the recommendation page.
MID-SESSION (15 min each): rewrite three closed questions as open ones; sort eight criteria into quantities and adjectives, then rewrite the adjectives as quantities.

### After-class tasks

• WRITE: the recommendation page in your own words, one page.
• PRACTISE: a two-minute spoken 'why this and why not that' for tomorrow's pitch.
• READ: the C4 model home page, the context and container levels, for Wednesday.

### Interview angle

• [S] Give me three ways to solve this and tell me which two you would rule out.
• [F] How do you estimate what an LLM feature will cost to run each month?
• [F] Proof of concept or MVP: what is the difference, and which would you propose first?
• [D] The CFO says four more people on the phones is cheaper than your system; respond with numbers.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Aced (formerly Exponent), the forward deployed engineer interview guide (verified 19 Sep 2026):
https://www.tryexponent.com/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde
• The Week 8 Friday cost model and the Week 10 cost review are the arithmetic to reuse (in the repository once built).

### Student references

• The C4 model, for Wednesday's component sheet (verified 19 Sep 2026):
https://c4model.com/

### Kahoot quiz plan

• Q1: differs in kind or only in size: five option pairs
• Q2: quantity or adjective: six criteria sorted
• Q3: compute the monthly run cost from the volumes and the illustrative price shown
• Q4 trap: the option with the highest quality always wins, true or false
• Q5: proof of concept or first product: four deliverables
• Return question from Monday: which of the four questions finds the blocker.

## Wed 20 Jan 2027 · Solution architecture · Components, their wiring, and the assessed solution proposal

### Business scenario of the day

WEDNESDAY. Dr Menon accepts option A in principle. Her head of IT joins the call: "Before anyone builds, show me what pieces this thing has, which of them touch my report system, what leaves our network, and what happens when a piece fails." In the afternoon each group pitches its full proposal to the client; the pitch is the week's assessed solution proposal.
Your role: you draw the system as components and wires, trace one customer request through it, and pitch the proposal you would sign.
On the table: which components a first version needs and which it does not; what crosses each wire; where data rests and what may leave the network; which pieces you build and which you take as a managed service; what fails, and what the customer sees when it does.

### Thinking we train, before any tool

An architecture is a list of components and the wires between them, and the test of one is a trace: follow a single request from the customer's message to the answer and name every hop, every contract and every place it can fail. A first version lists only the components the thin end-to-end slice needs: the channel, the application service, the model gateway, the retrieval index, the one tool that reads report status, the store for conversations, identity, and the logging and evaluation that watch it. Each wire carries a contract, and each store sits on one side of the privacy line that discovery found.
Build or take as a service is decided per component, on Tuesday's measures; a managed service trades cost and control, and the programme uses cloud services where they shorten the path without hiding the mechanism. Each large decision gets one page: the decision, the options, the reason. The design is kept, because Friday compares it with what was deployed.

### Trainer agenda

1. The head of IT's four questions; the room names the pieces of Farhan's assistant from memory (15 min).
2. Components for a first version: the list, and what each one owns (45 min).
3. Wiring: one request traced end to end; the contract on each wire; where state rests; what fails and what the customer sees (55 min).
4. The privacy line and the limits: what may leave the network, the latency budget, the cost ceiling (30 min).
5. Build or take as a service, per component; one decision written as a one-page decision record (35 min).
6. Groups assemble the solution proposal: discovery note, recommendation page, component sheet (30 min).
7. The assessed pitch: each group presents option A with B and C as considered alternates and takes questions from the client and her head of IT (70 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: an architecture is components and wires; a trace tests it; contracts sit on wires; the privacy line decides where data may rest.
CAN DO: list the components of a first version, draw the wiring, trace one request with its failure paths, and record one decision on a page.
CAN HANDLE: a head of IT who asks what leaves the network, and a component whose purpose nobody can state.
CAN DEFEND: the solution proposal under questions from the client, in business language, with the numbers from Tuesday.

### Subtopics (technique in service of the scenario)

• Components of a first version, and what each one owns
• Wiring: the one-request trace, contracts on wires, where state rests
• Failure paths: what fails and what the customer sees
• The privacy line, the latency budget and the cost ceiling
• Build or take as a managed service, decided per component
• The one-page decision record
• The solution proposal pitched as option A with B and C (assessed); the component sheet is page three of the solution file

### Trainer notes

START FROM: the systems the room has already built, the retrieval assistant of Build 4 and the guarded agent of Build 5; today names their parts as components.
GO AS FAR AS: every group pitches a proposal with a component sheet that survives a one-request trace.
STOP BEFORE: cloud vendor catalogues, networking internals, scaling patterns; one managed service is compared with its self-built twin and the rest are named.
COMES LATER: Thursday puts the application service in a container; Friday releases it and measures the design-to-deployment delta against today's sheet.
THE PITCH: assessed as the Week 16 solution proposal in Module 7. The evaluation schema proposed to the AOC has no separate line for it, so how it counts is an open decision recorded in Structure, and nothing about marks is stated in the room. With more than ten groups the pitches run in two rooms.
WHAT THE ROOM REVEALS: expect the first diagrams to miss the component that checks identity or the one that logs; the trace finds both.
CUT FIRST: the second decision record. Never cut the trace or the pitch.

### Client zero data (TRAINER ONLY)

PROPOSED FOR v2.3: the head of IT at Kalpa Health appears as an unnamed role.
THE CLIENT CARD for today: one internal interface returns report status by booking id; nothing that contains report content may leave Kalpa Health's systems; customers are identified by phone number and booking id.
No dataset and no planted data witness.

### In-session exercises

GUIDED: the trace of one request through Farhan's assistant, on the board.
UNGUIDED: the group's component sheet, its trace with failure paths, one decision record, then the pitch.
MID-SESSION (15 min each): find the missing component in three flawed diagrams; mark on one diagram every wire that crosses the privacy line.

### After-class tasks

• WRITE: the decision record for one decision your group argued about.
• SETUP: Thursday's container setup instructions ship tonight; run the check they end with.
• READ: Docker Docs, 'What is Docker?'.

### Interview angle

• [S] Draw the architecture of a system you built and trace one request through it.
• [F] Which parts of your system would you take as a managed service, and why?
• [F] What happens to the user when your retrieval service is down?
• [D] The client's head of IT says nothing may leave their network; redesign your system in five minutes.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• The C4 model, the context and container levels as the drawing grammar (verified 19 Sep 2026):
https://c4model.com/
• Architectural Decision Records, the one-page decision format (verified 19 Sep 2026):
https://adr.github.io/
• The Twelve-Factor App, for where configuration and state belong (verified 19 Sep 2026):
https://12factor.net/

### Student references

• Docker Docs, What is Docker? (verified 19 Sep 2026):
https://docs.docker.com/get-started/docker-overview/

### Kahoot quiz plan

• Q1: name the component: six descriptions matched
• Q2: the trace: put seven hops in order
• Q3 trap: a diagram without logging; what can you not answer when it fails
• Q4: which wires cross the privacy line
• Q5: build or take as a service: three components decided with a reason
• Return question from Tuesday: two measures that must be quantities before an option is scored.

## Thu 21 Jan 2027 · Deployment, part one · From a laptop to a container anyone can run

### Business scenario of the day

THURSDAY. The proposal is approved for a thin slice: report status only, behind a login, for one centre. The head of IT sets the terms: "It runs on my infrastructure, and I will not install your laptop. Hand me something that runs the same way everywhere, tells me when it is unhealthy, and keeps its secrets out of the code."
Your role: you take a working service, your group's from Build 5 or the starter in the pack, put it in a container with its dependencies pinned, run it beside its store with one command, and hand over an image with a version.
On the table: why 'it works on my machine' fails; what goes into an image and what stays out; how configuration and secrets reach a running container; how the service says it is healthy; how a version is named.

### Thinking we train, before any tool

An environment described in a file can be rebuilt anywhere; an environment that lives on a laptop cannot. An image is that file made real: a base, the pinned dependencies, the code, the command. A container is an image running. Configuration and secrets arrive from outside at run time, so the same image runs in test and in production and no key is ever baked in. A health check lets the platform, and the head of IT, know the service is alive. A version tag on the image is what makes a release, and later a rollback, possible.
Week 14 took a service beyond localhost once; today makes that repeatable by someone who has never met the group.

### Trainer agenda

1. The head of IT's terms; one service is started on a clean machine and fails, and the room reads the error (15 min).
2. Image and container: the environment as a file; the Dockerfile read line by line: base, pinned dependencies, code, command (55 min).
3. Build and run; the deliberate failure: a library missing from the requirements file stops the container with ModuleNotFoundError, and the room fixes the file, never the running container (50 min).
4. Configuration and secrets from outside: environment variables, and an env file that never enters the repository; the health check (45 min).
5. The service beside its store: one compose file, one command; logs read from outside the container (45 min).
6. Guided then unguided: the group's service containerised, tagged with a version, and started by another group from the README alone (70 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: an image is an environment written down, a container is an image running, configuration and secrets come from outside, and a version tag is what a release points at.
CAN DO: write a Dockerfile with pinned dependencies, run the service beside its store with one command, add a health check, and tag the image.
CAN HANDLE: ModuleNotFoundError inside a container, a secret found in the repository, and a service that another group cannot start.
CAN DEFEND: every line of the Dockerfile, and why the fix goes into the file and never into the running container.

### Subtopics (technique in service of the scenario)

• Why 'it works on my machine' fails; the environment as a file
• Image against container; the Dockerfile line by line
• Pinned dependencies and repeatable builds
• Configuration and secrets from outside the image
• The health check
• The compose file: the service beside its store
• Logs from outside the container; the version tag

### Trainer notes

START FROM: the Week 14 deployment beyond localhost and a working Build 5 service; today adds repeatability.
FIRST-USE TOOLS: Docker and the compose file. How they run inside the course environment is decided and verified at the day build, and the setup instructions ship on Wednesday night.
GO AS FAR AS: every group's service starts on another group's machine from the README alone.
STOP BEFORE: orchestration platforms, image optimisation, networking internals.
COMES LATER: Friday builds the image in a pipeline and releases it; Saturday scans it and tests it.
WHAT THE ROOM REVEALS: expect the clean-machine start and the README handover to fail on the first try for many groups; both failures are the lesson.
CUT FIRST: the log-reading block shrinks to a demonstration. Never cut the README handover.

### Client zero data (TRAINER ONLY)

No client-zero data today; the material is a working service, the group's own or the starter in the pack.
THE STAGED FAILURE (trainer only): the starter repository's requirements file omits one library the service imports, so the first container stops with ModuleNotFoundError.
No Kalpa fact is added.

### In-session exercises

GUIDED: the starter service containerised together, including the staged failure and its fix.
UNGUIDED: the group's service in a container, with a health check, a compose file, a version tag and a README another group can follow.
MID-SESSION (15 min each): read a Dockerfile and predict what the image contains; find the secret in three sample repositories.

### After-class tasks

• BUILD: hand your README to someone outside your group and note where they get stuck.
• READ: GitHub Docs, the GitHub Actions quickstart.
• SETUP: Friday's pipeline needs repository permissions; the instructions ship tonight.

### Interview angle

• [S] What is a Docker image, what is a container, and how are the two related?
• [F] How do you keep secrets out of an image and out of a repository?
• [F] Your service works on your laptop and fails in the container; how do you debug it?
• [D] The client's IT team will run your system after you leave; what do you hand over so they never need to call you?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Docker Docs, Get started (verified 19 Sep 2026):
https://docs.docker.com/get-started/
• Docker Docs, Building best practices, for pinned and repeatable images (verified 19 Sep 2026):
https://docs.docker.com/build/building/best-practices/
• Docker Docs, Docker Compose (verified 19 Sep 2026):
https://docs.docker.com/compose/
• The Twelve-Factor App, the config factor (verified 19 Sep 2026):
https://12factor.net/

### Student references

• Docker Docs, What is Docker? (verified 19 Sep 2026):
https://docs.docker.com/get-started/docker-overview/
• GitHub Docs, Quickstart for GitHub Actions, for Friday (verified 19 Sep 2026):
https://docs.github.com/en/actions/get-started/quickstart

### Kahoot quiz plan

• Q1: image or container: five statements sorted
• Q2: read the Dockerfile shown; which line pins the dependencies
• Q3 trap: fix the missing library inside the running container; what happens on the next start
• Q4: where does the API key live: the image, the repository or the environment
• Q5: what a health check tells the platform
• Return question from Wednesday: name the component that a one-request trace most often finds missing.

## Fri 22 Jan 2027 · Deployment, part two · The pipeline, the release, the rollback and the upgrade

### Business scenario of the day

FRIDAY. The slice runs in a container. The head of IT: "Now show me how a change reaches my customers, how I stop a bad one, and how I get back to yesterday in five minutes. You will upgrade a library next month, so show me that does not break anything either."
Your role: you build the pipeline that tests, builds and releases the image, you ship a bad release on purpose and roll it back, and you upgrade one dependency the safe way.
On the table: what must pass before a change is released; what a release is; how a rollback works and how long it takes; how an upgrade is tried before it is trusted; how far the deployed system drifted from Wednesday's design.

### Thinking we train, before any tool

A pipeline is the release checklist made automatic: on every change it runs the tests, builds the image, tags it and deploys it, and it stops at the first failure. For an AI system the tests include the evaluation suite from Weeks 10 to 14, so a change that lowers answer quality fails the pipeline the same way a broken function does. A release is a tag that the running system points at; a rollback points it back at the previous tag, which is why Thursday's version tags matter. An upgrade of a library or a model version is a change like any other: pin the new version on a branch, let the pipeline and the evaluation suite judge it, release it if it passes.
The day closes by laying the deployed system beside Wednesday's component sheet and counting what changed. A practitioner's rule of thumb reads a change of under a fifth as healthy and a change near a half as a sign the design was never understood; the rule is a heuristic, and the count is what matters.

### Trainer agenda

1. The head of IT's three demands; the room writes the release checklist it would follow by hand (15 min).
2. The pipeline: a workflow file in .github/workflows that runs on every push: tests, then the image build, then the tag (55 min).
3. The evaluation suite as a gate: a change that lowers quality fails the pipeline; the deliberate failure stops at the test stage with a non-zero exit code (45 min).
4. Release and rollback: deploy the tagged image to the one target; ship a release with a broken health check on purpose; roll back to the previous tag and time it (55 min).
5. Upgrade: raise one pinned dependency on a branch, let the pipeline judge it, merge it or drop it (40 min).
6. Guided then unguided: the group's own pipeline, one rollback rehearsed, then the design-to-deployment delta counted against Wednesday's sheet (70 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a pipeline is the release checklist made automatic, the evaluation suite is a gate, a release is a tag, a rollback is the previous tag, and an upgrade is a change like any other.
CAN DO: write a workflow that tests, builds and tags on every push, release to one target, roll back, and upgrade a dependency on a branch.
CAN HANDLE: a failed pipeline, a bad release in front of the client, and an upgrade that lowers answer quality.
CAN DEFEND: the rollback, timed, and the delta between the design and what was deployed.

### Subtopics (technique in service of the scenario)

• The pipeline: test, build, tag, deploy, stopping at the first failure
• The workflow file and its triggers
• The evaluation suite as a release gate
• Release as a tag; rollback as the previous tag, rehearsed and timed
• Upgrading a library or a model version on a branch
• The design-to-deployment delta (a practitioner's heuristic, marked as one)

### Trainer notes

START FROM: Thursday's tagged image and the evaluation suites from Weeks 10 to 14.
FIRST-USE TOOLS: GitHub Actions. The deployment target is one environment chosen at the day build from the approved cloud credits, which are not yet decided; this row names no vendor.
GO AS FAR AS: every group ships a release, breaks it on purpose, and rolls back inside five minutes.
STOP BEFORE: promotion across several environments, blue-green and canary releases (named only), infrastructure as code.
COMES LATER: Saturday adds the security scan and the red-team tests to the same pipeline; capstone gates two and three ask for this pipeline on the group's own system.
WHAT THE ROOM REVEALS: expect the first rollback to take far longer than the room predicts, because nobody wrote down the previous tag. Let it happen once.
CUT FIRST: the upgrade block shrinks to a demonstration. Never cut the bad release and its rollback.

### Client zero data (TRAINER ONLY)

No client-zero data today.
THE STAGED FAILURES (trainer only): a test that fails until one line is fixed, so the first pipeline run stops at the test stage; a release whose health check path is wrong, so the target reports it unhealthy.
No Kalpa fact is added.

### In-session exercises

GUIDED: the starter pipeline written together, and its first failing run read line by line.
UNGUIDED: the group's pipeline, one deliberate bad release, one timed rollback, one upgrade on a branch, the delta count.
MID-SESSION (15 min each): put six pipeline steps in order and say which one should fail first; read a failed run's log and name the fix.

### After-class tasks

• WRITE: the runbook page: how to release, how to roll back, who to call.
• READ: the OWASP Top 10 for LLM Applications, the ten titles and the first two entries.
• RECAP: release, rollback and upgrade in one sentence each.

### Interview angle

• [S] What is CI/CD, and what does your pipeline run before a release?
• [F] How do you roll back a bad deployment, and how long does it take you?
• [F] How do you upgrade a model or a library version without breaking production?
• [D] Your release lowered answer quality and no test failed; what was missing from the pipeline, and what do you add?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• GitHub Docs, Quickstart for GitHub Actions: workflow files live in .github/workflows (verified 19 Sep 2026):
https://docs.github.com/en/actions/get-started/quickstart
• GitHub Docs, GitHub Actions documentation (verified 19 Sep 2026):
https://docs.github.com/en/actions
• Martin Fowler, Blue Green Deployment, named only as the next step after a tag rollback (verified 19 Sep 2026):
https://martinfowler.com/bliki/BlueGreenDeployment.html

### Student references

• GitHub Docs, Quickstart for GitHub Actions (verified 19 Sep 2026):
https://docs.github.com/en/actions/get-started/quickstart
• OWASP Top 10 for LLM Applications, 2025, for Saturday (verified 19 Sep 2026):
https://genai.owasp.org/llm-top-10/

### Kahoot quiz plan

• Q1: order the pipeline: five steps
• Q2: which step should fail first when a function breaks
• Q3 trap: roll back by fixing the code quickly; why is that slower than the previous tag
• Q4: what makes an evaluation suite a gate
• Q5: the safe way to try a new library version
• Return question from Thursday: where do secrets live when a container runs.

## Sat 23 Jan 2027 · Security, responsible AI and testing · Then the capstone is announced

### Business scenario of the day

SATURDAY. Kalpa Health's legal counsel joins the last review: "This thing will talk to patients. Show me how it can be attacked, what it will refuse to say, how you test that, and who is called when it gets something wrong." The week closes with the capstone: every group receives its own brief, in its own theme area, and the walk of this week starts again on Monday with a different client.
Your role: you put the slice through a threat review and a test suite, sign the responsible-use checklist for a health deployment, and then open your capstone brief.
On the table: how an LLM system is attacked and which attacks matter for this one; what it must refuse and when it must hand over to a person; what is tested before every release; who acts when it fails in front of a patient.

### Thinking we train, before any tool

Security for an AI system is reviewed at the level of the whole system. The OWASP Top 10 for LLM Applications (2025) is the map: prompt injection, sensitive information disclosure, supply chain, excessive agency and unbounded consumption are the five that bite a first deployment hardest, and Week 14 already built component guardrails against four of them. Today's work is the rest and the view of the whole: secrets that never reach the repository, dependencies that are pinned and scanned, and a check that Week 14's least privilege and budget cap hold across every component.
Testing has layers: unit tests for code, contract tests for structured output, the evaluation suite for quality, and a small red-team set of hostile prompts that runs in the pipeline. Responsible use is decided with the client and written down: what the assistant refuses, when it hands over to a person, what it logs, and how a patient learns they are talking to a machine. The NIST AI Risk Management Framework gives the vocabulary; the page the client signs is short. The choice of five risks is this course's construction.

### Trainer agenda

1. Legal counsel's four questions; the room attacks Friday's slice for ten minutes and lists what worked (20 min).
2. The threat review: the OWASP list as a map, five risks ranked for this system, the controls already built in Week 14 and the ones missing (50 min).
3. Secrets, least privilege and the supply chain: the deliberate failure is a key committed to the starter repository, which secret scanning flags; rotate it and remove it from history (40 min).
4. Testing in layers: unit, contract, evaluation, red-team; the red-team set added to Friday's pipeline (50 min).
5. Responsible use for a health deployment: refusal, handover to a person, logging, disclosure; the incident page (40 min).
6. Unguided: the risk register and the signed checklist close the solution file (30 min).
7. The capstone announced by the Programme Head: theme areas, the brief for each group, the three gates, what is due at gate one (50 min).
8. Kahoot and week close (20 min).

### Learner outcome

UNDERSTANDS: an AI system is attacked as a whole; controls, tests and refusals are decided per risk; responsible use is agreed with the client and written down.
CAN DO: rank five risks for one system, add a red-team set to the pipeline, rotate a leaked key, and write the refusal, handover and incident pages.
CAN HANDLE: a leaked secret, a hostile prompt inside a document, and a counsel who asks who is accountable.
CAN DEFEND: the risk register, line by line, and the capstone scope taken into Monday.

### Subtopics (technique in service of the scenario)

• The threat review, with the OWASP Top 10 for LLM Applications (2025) as the map
• Secrets, least privilege for tools, pinned and scanned dependencies, the budget cap
• Testing in layers: unit, contract, evaluation, red-team, all in the pipeline
• Responsible use agreed with the client: refusal, handover to a person, logging, disclosure
• The incident page: who acts when it fails in front of a customer
• The risk register that closes the solution file
• The capstone announcement: theme areas, briefs, gates

### Trainer notes

START FROM: the Week 14 guardrails for injection, personal data, tool permissions and budget; today moves from the component to the system and does not re-teach them.
GO AS FAR AS: every group closes the solution file with a risk register and a signed checklist, and leaves with its capstone brief read.
STOP BEFORE: penetration-testing tools, compliance regimes by name, model-level safety training.
COMES LATER: the capstone repeats the whole walk on the group's own brief: gate one asks for the discovery note, the recommendation and the component sheet; gate three asks for the pipeline, the tests and the risk register.
THE ANNOUNCEMENT: different groups receive different briefs; the theme areas and the plan are in the 'W17-20 Capstone' tab. No marks or weights are stated in the room.
WHAT THE ROOM REVEALS: expect the ten-minute attack to make the slice reveal its instructions or answer beyond report status. Keep the transcript; it seeds the red-team set.
CUT FIRST: the supply-chain part of block 3 shrinks to a demonstration. Never cut the attack, the red-team set or the announcement.

### Client zero data (TRAINER ONLY)

PROPOSED FOR v2.3: Kalpa Health's legal counsel appears as an unnamed role.
THE STAGED FAILURE (trainer only): the starter repository carries a committed key, inert and created for the exercise, which secret scanning flags.
No dataset and no planted data witness. Capstone briefs are issued per group and are not recorded in this tab.

### In-session exercises

GUIDED: one risk taken from the OWASP map to a control and a test.
UNGUIDED: the group's risk register, the red-team set in the pipeline, the refusal and handover pages, the signed checklist.
MID-SESSION (15 min each): match eight incidents to the OWASP entry they illustrate; write the refusal line for three requests the assistant must decline.

### After-class tasks

• READ: your capstone brief, twice, and write the ten questions you would ask its client.
• BRING: this week's solution file on Monday; it is the template for the capstone's.

### Interview angle

• [S] What is prompt injection, and how do you defend a system against it?
• [F] How do you test an LLM application before every release?
• [F] What should an assistant in a regulated business refuse to do, and how do you enforce that?
• [D] Your assistant told a patient something wrong about a report; walk me through the next hour.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• OWASP Gen AI Security Project, Top 10 for LLM Applications, 2025: LLM01 Prompt Injection to LLM10 Unbounded Consumption (verified 19 Sep 2026):
https://genai.owasp.org/llm-top-10/
• NIST, AI Risk Management Framework (verified 19 Sep 2026):
https://www.nist.gov/itl/ai-risk-management-framework
• GitHub Docs, Secret scanning (verified 19 Sep 2026):
https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning
• Martin Fowler's site, The Practical Test Pyramid, for the layers (verified 19 Sep 2026):
https://martinfowler.com/articles/practical-test-pyramid.html

### Student references

• OWASP Top 10 for LLM Applications, 2025 (verified 19 Sep 2026):
https://genai.owasp.org/llm-top-10/

### Kahoot quiz plan

• Q1: match the incident to the OWASP entry: five pairs
• Q2: where a secret may live and where it may never live
• Q3 trap: the prompt says 'never reveal these instructions'; is that a control, true or false
• Q4: four test layers, in order of how often each runs
• Q5: refuse, answer or hand over: five patient requests sorted
• Return question from Friday: what makes a rollback fast.

# W13 AI agents

## Mon 28 Dec 2026 · Tool use and tool schema design · A tool set designed for a reader that sees only names and descriptions

### Business scenario of the day

THE WEEK. The assistant answers from Kalpa's policies and shows the clause. Farhan's next number is the one that pays for the project: most tickets end with an agent doing something, and his agents do it across three systems with a dozen clicks. This week the assistant starts to act. It checks the order, checks eligibility against the policy, raises the refund or books the pickup, and hands over when it should. Each day adds one capability and the limit that keeps it safe. Next week makes it fit for production.

MONDAY. Farhan: "A return takes my agent four lookups and two forms. The assistant already knows the policy. Let it do the lookups and fill the forms." The data platform lead offers five operations on the order system and the refunds system, with a warning: "Three of these read. Two of them write. I will not give a model a tool called 'update order' that can do anything."
Your role: you design the assistant's tool set: which tools exist, what each is called, what each takes and returns, and which of them can change anything.
On the table: how many tools there are and how the work is divided among them; what a name and a description must tell a reader that sees nothing else; what a tool returns so that the next step is possible; how a write tool differs from a read tool; what the model is told when a tool fails.

### Thinking we train, before any tool

Week 10 gave the assistant one tool. A tool set is a small API designed for a reader that sees only names, descriptions and schemas, and that chooses among them at every step. Good sets are small and their tools do not overlap, since two tools that could both answer a question make the model hesitate or alternate. Each tool is named for the customer intent it serves and never for the table it touches. It takes few arguments, with a fixed list wherever a list exists, and it returns what the next step needs and no more, because every returned token is read and paid for.
Read tools and write tools are different classes. A write tool does one narrow thing, validates everything and refuses by default: 'raise a refund for this order line up to this amount' can be reasoned about, and 'update order' cannot. An error is a message to the model. 'Order not found; ask the customer to confirm the order id' produces a good next step, and a bare 'Error' produces the same call again.

### Trainer agenda

1. Farhan's return walked through by hand: the lookups, the forms, the three systems (15 min).
2. From one tool to a set: five operations are on offer, and the room drafts the tool list before seeing any code (40 min).
3. Names and descriptions as the model's only view: two overlapping tools and the hesitation they cause, then merged or sharpened (45 min).
4. Arguments and returns: fixed lists, few arguments, the return trimmed to what the next step needs, with the token count before and after (45 min).
5. Read against write: the narrow write tool, validation, refusal by default (40 min).
6. Errors the model can act on: the bare 'Error' that produces the same call three times, then the rewritten message (35 min).
7. Guided then unguided: the tool set for returns, each tool with its description, schema, return and error messages, tested one call at a time (60 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a tool set is an API for a reader that sees only names, descriptions and schemas; tools should be few and should not overlap; write tools are narrow and refuse by default; an error is a message to the model.
CAN DO: divide a job into a small tool set, write descriptions and schemas a model can choose between, trim returns, separate read from write tools, and write error messages that lead to a good next step.
CAN HANDLE: two tools the model cannot tell apart, a return so large that it crowds the context, a write tool that is too broad, and an error that triggers the same call again.
CAN DEFEND: every tool in the set, and why the two write tools are as narrow as they are.

### Subtopics (technique in service of the scenario)

• From one tool to a tool set: an API for a model
• Few tools, no overlap, named by customer intent
• Arguments: few, typed, with fixed lists
• Returns trimmed to what the next step needs
• Read tools against write tools; narrow writes that refuse by default
• Error surfaces: messages the model can act on
• Testing a tool one call at a time, before any loop exists

### Trainer notes

START FROM: Week 10 Wednesday's single tool with its checks in code, and Tuesday's schemas; Week 11's retrieval, which becomes one more read tool.
GO AS FAR AS: everyone ships a tool set of five to seven tools for returns, tested call by call, with no loop yet.
STOP BEFORE: the agent loop and patterns (Tuesday), memory (Wednesday), flows and approvals (Thursday). Today nothing chooses a second step.
COMES LATER: Tuesday puts this set inside a loop; Week 14 Tuesday cuts the credentials down to exactly these tools.
NAMED ONLY: the Model Context Protocol, an open standard for exposing tools to models, is named as where shared tool sets are heading and is not used today.
WHAT THE DATA REVEALS: with two overlapping lookups the model alternates between them on the same ticket; the untrimmed order record is many times larger than the five fields the next step needs; the bare 'Error' draws the identical call three times running.
SECOND EXAMPLE: Rohan Desai's collections desk at Kalpa Financial, where 'read the account' and 'promise a payment plan' must be different tools with different limits.
CUT FIRST: the token count on returns shrinks to one tool. Never cut the overlapping tools or the bare 'Error'.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION agent: v4 orders and payments, the Week 11 corpus, and a stub of the refunds system with five operations, three that read and two that write.
PLANTED: two lookups whose first-draft descriptions overlap; an order record whose full return is far larger than the next step needs; a stub error that returns the single word 'Error'.
No new named stakeholder. Students are never told what is planted.

### In-session exercises

GUIDED: one read tool and one write tool designed together, each tested with a single call.
UNGUIDED: the rest of the tool set with descriptions, schemas, trimmed returns and error messages.
MID-SESSION (15 min each): merge or sharpen four pairs of overlapping tool descriptions; rewrite five error strings so that a model would know what to do next.

### After-class tasks

• BUILD: a test sheet for your tool set: one good call, one bad argument and one error per tool, with the message each returns.
• READ: Anthropic Engineering, Writing effective tools for AI agents.
• SETUP: Tuesday needs no new install.

### Interview angle

• [S] How do you design tools for an LLM agent?
• [F] Why would you give an agent five narrow tools and not one general one?
• [F] What should a tool return to the model, and what should it keep back?
• [D] Your agent keeps choosing the wrong one of two similar tools; how do you find out why, and what do you change?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Anthropic Engineering, Writing effective tools for AI agents (verified 21 Sep 2026):
https://www.anthropic.com/engineering/writing-tools-for-agents
• Claude Platform Docs, Tool use with Claude (verified 21 Sep 2026):
https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
• OpenAI API docs, Function calling (verified 21 Sep 2026):
https://developers.openai.com/api/docs/guides/function-calling
• Model Context Protocol, What is the Model Context Protocol? Named only today (verified 21 Sep 2026):
https://modelcontextprotocol.io/docs/getting-started/intro

### Student references

• Anthropic Engineering, Writing effective tools for AI agents (verified 21 Sep 2026):
https://www.anthropic.com/engineering/writing-tools-for-agents

### Kahoot quiz plan

• Q1: read tool or write tool: six operations sorted
• Q2: two descriptions shown; which pair will confuse the model, and why
• Q3 trap: return the whole record so the model has everything, true or false
• Q4: rewrite 'Error' so that the next step is obvious
• Q5: which of three tool names is named for the customer's intent
• Return question from Week 10 Wednesday: who runs the tool, and where does permission live.

## Tue 29 Dec 2026 · Agent patterns · The least autonomy that solves each pile of tickets

### Business scenario of the day

TUESDAY. Farhan sorts a day of tickets into three piles. 'Where is my order' needs one lookup. 'I want to return this' follows the same four steps every time. The third pile is the mess: "It arrived damaged, I was charged twice, and I have moved house." Kavya asks her question before anyone builds: "Which of these piles needs an agent at all? Show me the cheapest thing that solves each pile, and show me what the clever version costs on the easy pile."
Your role: you match each pile to the least autonomy that solves it, build the patterns on the same tickets, and bring the comparison.
On the table: what makes something an agent and not a workflow; what the loop of reasoning, acting and observing looks like; when planning first helps; what a self-check buys and costs; how patterns are compared fairly.

### Thinking we train, before any tool

An agent is a model in a loop that chooses its own next step. It reasons about the state, acts through a tool, observes the result, and repeats until it decides it is done. That loop is ReAct (established: Yao and others, 2022). A workflow is the opposite arrangement: the steps are fixed in code and the model works inside each step. Anthropic's engineering guidance draws the same line, with workflows following predefined code paths and agents directing their own process, and it gives the rule this course adopts as the least-autonomy rule: use the simplest arrangement that solves the task, because autonomy is paid for in latency, cost and unpredictability.
Between the two sit patterns worth knowing by name. A router classifies the ticket and sends it down the right path. Plan-and-execute writes the plan first and then carries it out, which suits a ticket with several independent asks. Reflection has the model check its result against the goal before it finishes (established: Shinn and others, 2023), which catches some errors and doubles some bills. Patterns are compared the way prompts were in Week 10: the same tickets, the same score, and now steps and cost per ticket as well.

### Trainer agenda

1. Three piles of tickets; the room assigns each a way of working before any pattern is named (15 min).
2. The workflow: the four-step return as fixed code, with the model inside each step (40 min).
3. The agent loop: reason, act, observe, repeat; ReAct built on Monday's tool set; the step cap (50 min).
4. The agent on the easy pile: the same return in many more steps, at several times the cost (25 min).
5. The router, then plan-and-execute on the ticket with three asks (45 min).
6. Reflection: the self-check before finishing, what it catches and what it costs (30 min).
7. Guided then unguided: the pattern comparison, with success, steps and cost per ticket for each pile and a recommendation per pile (75 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a workflow fixes the steps and an agent chooses them; autonomy costs latency, money and predictability; the simplest arrangement that solves the task is the right one; patterns are compared on the same tickets.
CAN DO: build a fixed workflow, a ReAct loop with a step cap, a router and a plan-and-execute variant on one tool set, and compare them on success, steps and cost.
CAN HANDLE: a loop that never decides it is done, an agent that spends ten steps on a one-step ticket, and a teammate who wants an agent for everything.
CAN DEFEND: the pattern chosen for each pile, with its numbers, and why the easy piles did not get an agent.

### Subtopics (technique in service of the scenario)

• Workflow against agent: who chooses the next step
• The ReAct loop: reason, act, observe; the step cap
• The least-autonomy rule (adopted from Anthropic's guidance)
• The router
• Plan-and-execute
• Reflection: the self-check and its price
• Comparing patterns: success, steps, cost per ticket

### Trainer notes

START FROM: Monday's tested tool set; Week 10 Monday's habit of comparing on one task with one score.
GO AS FAR AS: everyone ships the comparison table over three piles and at least three patterns, with a recommendation per pile.
STOP BEFORE: memory across conversations (Wednesday), graphs with approvals (Thursday), several agents talking to each other, which this programme names and does not build.
COMES LATER: Thursday turns the recommended arrangement into a controlled flow; Week 14 Monday evaluates the path as well as the result.
WHAT THE DATA REVEALS: on the return pile the fixed workflow matches the agent's success at a fraction of its steps and cost; on the mess pile the workflow fails and plan-and-execute succeeds; with no step cap one ticket keeps looping until the budget is gone.
CUT FIRST: reflection shrinks to a demonstration. Never cut the agent on the easy pile.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION agent: thirty tickets in three piles of ten: single lookup, standard return, several asks at once.
PLANTED: a ticket on which a loop without a step cap never finishes; a pile on which the fixed workflow and the agent succeed equally often.
Students are never told what is planted.

### In-session exercises

GUIDED: the four-step workflow; the ReAct loop with its step cap.
UNGUIDED: the router, the plan-and-execute variant, the full comparison table, the recommendation per pile.
MID-SESSION (15 min each): for eight tasks from five Kalpa units, say workflow or agent and give the reason; read a short ReAct trace and mark each line as reason, act or observe.

### After-class tasks

• WRITE: the recommendation per pile, half a page, numbers first.
• WATCH: How We Build Effective Agents, Barry Zhang, Anthropic.
• READ: Anthropic Engineering, Building Effective AI Agents, the section on when and when not to use agents.

### Interview angle

• [S] What is an AI agent, and how is it different from a workflow or a chain?
• [S] Explain the ReAct pattern.
• [F] When would you choose a fixed workflow over an agent?
• [F] What is plan-and-execute, and what does it fix?
• [D] Your manager wants 'an agent' for a task that four fixed steps solve; what do you build, and how do you explain it?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Anthropic Engineering, Building Effective AI Agents: workflows against agents, and the simplest-solution rule (verified 21 Sep 2026):
https://www.anthropic.com/engineering/building-effective-agents
• Yao and others, ReAct: Synergizing Reasoning and Acting in Language Models, 2022 (verified 21 Sep 2026):
https://arxiv.org/abs/2210.03629
• Shinn and others, Reflexion: Language Agents with Verbal Reinforcement Learning, 2023 (verified 21 Sep 2026):
https://arxiv.org/abs/2303.11366
• Wang and others, Plan-and-Solve Prompting, 2023 (verified 21 Sep 2026):
https://arxiv.org/abs/2305.04091

### Student references

• AI Engineer, How We Build Effective Agents: Barry Zhang, Anthropic (verified 21 Sep 2026):
https://www.youtube.com/watch?v=D7_ipDqhtwk
• Anthropic Engineering, Building Effective AI Agents (verified 21 Sep 2026):
https://www.anthropic.com/engineering/building-effective-agents

### Kahoot quiz plan

• Q1: workflow or agent: five tasks sorted
• Q2: label the three parts of one ReAct turn
• Q3 trap: an agent is always the more capable choice, true or false
• Q4: which pattern suits a ticket with three independent asks
• Q5: the loop never stops; which single setting was missing
• Return question from Monday: why are the two write tools narrow.

## Wed 30 Dec 2026 · Memory and state · The case that resumes tomorrow, and the limit that must not be forgotten

### Business scenario of the day

WEDNESDAY. A customer comes back the next morning: "Any news on my refund?" The assistant greets her as a stranger and asks for her order id again. A long conversation about three orders goes wrong more quietly: by the fortieth message the assistant has forgotten the refund limit it was given at the start, which is Week 8 Friday's overflow in a new place. Farhan: "My agents keep case notes. Yours has amnesia, and when it does remember, I need to know what it is remembering."
Your role: you give the assistant state that survives a long conversation and memory that survives the night, and you decide what it is never allowed to remember.
On the table: what the task needs in order to continue and where that lives; what should outlast the conversation; what happens to the message list as it grows; what gets lost when a history is summarised; what must never be stored.

### Thinking we train, before any tool

Two different things get called memory. State is what the current task needs in order to continue: which order, which steps are done, what is waiting for approval. It is structured, it lives outside the model in a store the application owns, and it is passed in at every step. Memory is what should outlast the conversation: the case history and the customer's stated preferences. It is written on purpose, by a rule, and read back by lookup, which makes it retrieval, with Week 11's discipline and Week 11's staleness problem.
Inside one conversation the context window is the budget from Week 8. The message list is trimmed or summarised before it overflows, and whatever must never be lost, the rules and the limits, is kept outside the part that gets summarised. What may be remembered is a design decision with a privacy side: a payment detail has no place in a memory store, and Week 14 Tuesday returns to that.

### Trainer agenda

1. The customer treated as a stranger, and the limit forgotten at message forty (15 min).
2. State against memory: two lists made from one conversation (35 min).
3. Task state as a structure: the order, the steps done, the pending approval; kept in a store and passed in at every step (50 min).
4. The message list as a budget: trimming and summarising; the summary that drops the refund limit; the rules pinned outside the summarised part (50 min).
5. Long-term memory: what is written, by which rule, keyed by customer and case, and read back by lookup (45 min).
6. What must never be remembered; stale memory, and the address that changed (25 min).
7. Guided then unguided: the stateful assistant that resumes yesterday's case and survives a sixty-message conversation (60 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: state serves the current task and memory outlasts it; both live outside the model; a summarised history can lose a rule; memory is retrieval with a staleness problem; what is stored is a privacy decision.
CAN DO: keep task state in a store, trim and summarise a message list with the rules pinned, write and read long-term memory by customer and case, and exclude what must not be stored.
CAN HANDLE: a limit lost in a summary, a remembered address that is no longer true, and a request to 'just remember everything'.
CAN DEFEND: what the assistant stores, for how long, under which key, and what it refuses to store.

### Subtopics (technique in service of the scenario)

• State against memory
• Task state as a structure, held in a store the application owns
• The message list as a budget: trimming and summarising
• Pinning rules and limits outside the summarised part
• Long-term memory: written by a rule, read by lookup
• Stale memory
• What must never be remembered

### Trainer notes

START FROM: Week 8 Friday's context budget and its silent overflow; Tuesday's loop, which so far forgets everything when the conversation ends.
GO AS FAR AS: everyone ships an assistant that resumes a case the next day and keeps its limits through sixty messages.
STOP BEFORE: memory that rewrites itself, knowledge graphs of customers, shared memory between agents.
COMES LATER: Thursday's checkpoints reuse today's state store; Week 14 Tuesday masks personal data before anything reaches a store.
FIRST-USE TOOLS: a persistence layer for state; LangGraph's persistence and the memory concepts in its documentation are proposed, and are verified at the day build.
WHAT THE DATA REVEALS: the summary of the first forty messages keeps the customer's complaint and drops the refund limit, and the assistant then offers more than it may; the memory store returns an address the customer changed last month.
SECOND EXAMPLE: Ananya Bose's support desk at Kalpa Connect, where a customer's plan history must outlast the chat and the one-time password must never be stored.
CUT FIRST: the stale-address case shrinks to a demonstration. Never cut the summary that drops the limit.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION agent: two long conversations of about sixty messages, and one customer who returns the next day.
PLANTED: a refund limit stated early in a conversation and lost by a naive summary; a remembered delivery address that has since changed; a message in which the customer volunteers a payment detail.
Anand's refund limit is fixed at the day build and recorded in v2.3; until then this row carries no rupee figure. Students are never told what is planted.

### In-session exercises

GUIDED: the state structure and its store; one trimming rule.
UNGUIDED: summarising with pinned rules, the long-term memory write and read, the exclusion rule, the next-day resume.
MID-SESSION (15 min each): sort twelve facts from one conversation into state, memory or never store; read two summaries of the same history and find what each lost.

### After-class tasks

• BUILD: a one-page memory policy for the assistant: what is stored, under which key, for how long, and what is excluded.
• READ: Anthropic Engineering, Effective context engineering for AI agents.
• SETUP: Thursday's graph library installs from the setup cell; the instructions ship tonight.

### Interview angle

• [S] How do agents handle memory? Short-term against long-term.
• [F] A conversation exceeds the context window; what are your options, and what does each lose?
• [F] Where should an agent's state live, and why not in the prompt alone?
• [D] A customer asks your assistant to forget her; what has to be true of your design for you to say yes?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Docs by LangChain, Memory overview (verified 21 Sep 2026):
https://docs.langchain.com/oss/python/concepts/memory
• Docs by LangChain, LangGraph Persistence (verified 21 Sep 2026):
https://docs.langchain.com/oss/python/langgraph/persistence
• Anthropic Engineering, Effective context engineering for AI agents (verified 21 Sep 2026):
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
• Packer and others, MemGPT: Towards LLMs as Operating Systems, 2023, for the idea of paging memory in and out (verified 21 Sep 2026):
https://arxiv.org/abs/2310.08560

### Student references

• Anthropic Engineering, Effective context engineering for AI agents (verified 21 Sep 2026):
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

### Kahoot quiz plan

• Q1: state, memory or never store: six facts sorted
• Q2: the summary kept the complaint and dropped what
• Q3 trap: a bigger context window solves memory, true or false
• Q4: where does task state live, and who owns it
• Q5: the remembered address is wrong; which Week 11 problem is this
• Return question from Tuesday: name the rule for choosing between a workflow and an agent.

## Thu 31 Dec 2026 · Controlled flows · The refund limit becomes an edge that no sentence can move

### Business scenario of the day

THURSDAY. Anand has read Tuesday's comparison and has a condition before any refund leaves the building without a human hand. "Above my limit a named person approves it. Below it I still want the rule on one page that my auditor can read, and I do not want that page to be a prompt." On Wednesday evening a tester got the assistant to approve a refund above the limit by writing three polite and persistent messages.
Your role: you move Kalpa's rules out of the prompt and into the structure of the program, add the approval step, and hand Anand the page.
On the table: why a rule in a prompt can be argued with; what a flow looks like as nodes and edges; what the model decides and what the graph decides; how a flow pauses for a person and resumes; what the auditor reads.

### Thinking we train, before any tool

A rule that lives in a prompt is a request, and a persistent customer can talk a model out of a request. A rule that lives in the structure of the program cannot be argued with. A controlled flow moves the business rules out of the prompt and into a graph. Nodes do the work: a model step, a tool call, a check. Edges carry explicit conditions, and a state object travels along them. The model decides inside a node, and the graph decides what happens between nodes. The refund limit becomes an edge: at or under the limit the flow continues, above it the flow goes to approval, and no sentence from the customer ever reaches that edge.
A human-in-the-loop checkpoint is a node that pauses the flow, saves the state, waits for a named person, and resumes from where it stopped, hours later if need be. The drawing of the graph is also the one-page document the auditor reads. Graph orchestration libraries supply these pieces; LangGraph is proposed, with its persistence and interrupt features, and is verified at the day build. The idea does not depend on any library.

### Trainer agenda

1. The refund above the limit, approved after three persistent messages; the room reads the transcript (15 min).
2. The flow drawn on paper: nodes, edges, conditions, the state object (40 min).
3. The graph in code: the return flow with model nodes, tool nodes and check nodes (55 min).
4. The limit as an edge: the same three messages replayed against the graph (30 min).
5. The human checkpoint: pause, save, wait, resume; an approval given after a restart (50 min).
6. Branches for the mess pile: damaged, charged twice, address changed, each a path with its own checks (30 min).
7. Guided then unguided: the controlled agent with the limit as an edge, one approval checkpoint, and the one-page flow for the auditor (60 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a rule in a prompt is a request and a rule in the structure is a control; the model decides inside a node and the graph decides between nodes; a checkpoint pauses, saves and resumes.
CAN DO: draw a flow as nodes and edges, build it as a graph with a state object, turn a business limit into an edge, add a human approval checkpoint that survives a restart, and produce the one-page flow.
CAN HANDLE: a customer who argues with the limit, an approval that arrives hours later, and a branch nobody drew.
CAN DEFEND: the page to an auditor: where each rule lives, who approves what, and why the prompt is no longer the control.

### Subtopics (technique in service of the scenario)

• A rule in the prompt against a rule in the structure
• Graph-based orchestration: nodes, edges, conditions, the state object
• What the model decides and what the graph decides
• Explicit branching for the mess pile
• The human-in-the-loop checkpoint: pause, save, wait, resume
• The one-page flow as the audit document

### Trainer notes

START FROM: Tuesday's recommended arrangement per pile and Wednesday's state store; both are reused unchanged.
GO AS FAR AS: everyone ships a controlled agent that refuses to cross the limit under pressure, pauses for approval, resumes after a restart, and comes with its one-page flow.
STOP BEFORE: several agents in one graph, agents that rewrite their own graph, distributed execution.
COMES LATER: Week 14 Tuesday adds the guardrails around this flow, and Week 14 Wednesday uses the same checkpoints for recovery from failure.
FIRST-USE TOOLS: the graph orchestration library proposed above; setup instructions shipped on Wednesday night.
WHAT THE DATA REVEALS: the prompt-only rule gives way on the third persistent message and approves the refund; the same three messages against the graph all end at the approval node; an approval given after the process restarts still completes the refund once.
CUT FIRST: the extra branches shrink to one. Never cut the replay of the three messages against the graph.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION agent: the return flow, a named approver role, and the transcript of three persistent messages.
PLANTED: the prompt-only rule that gives way on the third message.
The approver is a role and carries no name. Anand's limit is fixed at the day build and recorded in v2.3. Students are never told what is planted.

### In-session exercises

GUIDED: the flow drawn on paper together; the first three nodes in code.
UNGUIDED: the limit as an edge, the approval checkpoint, one extra branch, the one-page flow.
MID-SESSION (15 min each): for ten Kalpa rules, say prompt or structure and defend two; find the missing edge in three drawn flows.

### After-class tasks

• WRITE: the one-page flow for the auditor, final, with each rule marked where it lives.
• READ: Docs by LangChain, LangGraph Interrupts, the human-in-the-loop section.
• RECAP: what the model decides and what the graph decides, one line each.

### Interview angle

• [S] How do you add a human in the loop to an agent?
• [F] Why not just tell the model 'never refund above the limit'?
• [F] What is graph-based orchestration, and what does it give you over a plain loop?
• [D] An auditor asks how you guarantee that no refund above the limit goes out unapproved; answer without using the word 'prompt'.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Docs by LangChain, LangGraph overview (verified 21 Sep 2026):
https://docs.langchain.com/oss/python/langgraph/overview
• Docs by LangChain, LangGraph Interrupts, for pausing and human-in-the-loop (verified 21 Sep 2026):
https://docs.langchain.com/oss/python/langgraph/interrupts
• Docs by LangChain, LangGraph Persistence, for checkpointers (verified 21 Sep 2026):
https://docs.langchain.com/oss/python/langgraph/persistence
• Anthropic Engineering, Building Effective AI Agents, the workflow patterns (verified 21 Sep 2026):
https://www.anthropic.com/engineering/building-effective-agents

### Student references

• Docs by LangChain, LangGraph overview (verified 21 Sep 2026):
https://docs.langchain.com/oss/python/langgraph/overview

### Kahoot quiz plan

• Q1: prompt or structure: five rules placed
• Q2: who decides inside a node, and who decides between nodes
• Q3 trap: a firmly worded system prompt is a control, true or false
• Q4: the four things a human checkpoint does, in order
• Q5: the approval arrived after a restart; what made that possible
• Return question from Wednesday: a summary dropped the limit; how was the limit protected.

## Fri 01 Jan 2027 · Agent failure modes · Three incidents, read from their traces

### Business scenario of the day

FRIDAY. The pilot's first week produces three incident reports. One ticket made forty tool calls and never finished. One refund was raised twice. One run reported success, and nothing had changed in the refunds system. Farhan: "I cannot fix what I cannot see. For every run I want to know what it did, in what order, what it cost, and whether the thing it says it did is true."
Your role: you make every run leave a record, diagnose the three incidents from those records, and write down the ways this agent fails with the check that catches each.
On the table: what a trace records; what a loop looks like from outside; how a run can report success and be wrong; what stops a runaway; which failures you can fix today and which need next week.

### Thinking we train, before any tool

Agents fail in a few recognisable ways, and each leaves a signature in a trace. A loop repeats the same call with the same arguments. Drift wanders from the customer's goal into neighbouring tasks. Tool misuse picks the wrong tool or a wrong argument. Silent failure reports success without the effect. The defence is designed in from the first version. Every run writes a trace: each step, each tool call with its arguments and its result, the tokens and the cost. A step cap and a budget cap stop the loop. An effect check reads back what a write tool claims to have done. A run that ends by hitting a cap is a failed run, and the ticket goes to a person.
Reading traces is the skill, and it is learned on real ones. The week closes with a failure catalogue for agents, the partner of Week 11's. The double refund is left open on purpose, since its cure, idempotency, belongs to Week 14 Wednesday.

### Trainer agenda

1. Three incident reports; the room guesses each cause before any trace is opened (15 min).
2. The trace: what is recorded at each step; one healthy run read end to end (40 min).
3. Trace one, the loop: the same call forty times; the step cap and the budget cap; a capped run counts as failed (45 min).
4. Trace two, the silent failure: success reported and nothing changed; the read-after-write effect check (45 min).
5. Trace three, the double refund: a retry after a timeout, diagnosed and left open for Week 14 (30 min).
6. Drift and tool misuse on two short traces (30 min).
7. Guided then unguided: tracing added to the controlled agent, the three incidents reproduced and diagnosed, and the agent failure catalogue written (75 min).
8. Kahoot and week close (20 min).

### Learner outcome

UNDERSTANDS: agents fail as loops, drift, tool misuse and silent failure; each has a signature in a trace; caps and effect checks are designed in from the start; a capped run is a failed run.
CAN DO: record a trace for every run, read one end to end, add step and budget caps, add a read-after-write check, and write a failure catalogue with a check per failure.
CAN HANDLE: a run that loops, a run that claims a success it did not achieve, and an incident whose cure is not available yet.
CAN DEFEND: the diagnosis of each incident from its trace, and what changes tomorrow because of it.

### Subtopics (technique in service of the scenario)

• The trace: steps, tool calls, arguments, results, tokens, cost
• The loop and its signature; step caps and budget caps
• Silent failure; the read-after-write effect check
• The double refund, diagnosed and left open
• Drift and tool misuse
• The agent failure catalogue: each failure with its check
• Observability designed in from the first version

### Trainer notes

START FROM: Thursday's controlled agent; Week 11 Friday's failure catalogue as the model for today's.
GO AS FAR AS: everyone ships the traced agent, three written diagnoses and the failure catalogue.
STOP BEFORE: idempotency and retries (Week 14 Wednesday), scoring a path against a golden one (Week 14 Monday), dashboards and alerts (Week 14 Friday).
COMES LATER: Week 14 opens on these traces and scores them.
FIRST-USE TOOLS: a tracing tool; Langfuse is proposed, since it is open source and can be self-hosted, and it is verified at the day build.
CALENDAR: 1 January is a restricted holiday on the central list and a working day. If the institute's calendar closes the campus, today's content moves into the first half of Saturday and the recap paper shortens to 60 minutes.
WHAT THE DATA REVEALS: trace one shows the identical call with identical arguments forty times, caused by the bare 'Error' from Monday; trace two shows a write tool returning 'ok' while a read of the refunds stub shows no refund; trace three shows a timeout followed by a retry, with both requests accepted.
CUT FIRST: drift and tool misuse shrink to one trace. Never cut the silent failure.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION agent: five recorded traces from the pilot.
PLANTED: a loop of forty identical calls; a write that reports 'ok' and changes nothing; a timeout followed by a retry that both succeed; one drifting run; one wrong-tool run.
Students are never told what is planted.

### In-session exercises

GUIDED: the healthy trace read together; the step cap added.
UNGUIDED: the effect check, the three diagnoses, the failure catalogue.
MID-SESSION (15 min each): match five trace excerpts to their failure; write the one-line alert you would want for each of the three incidents.

### After-class tasks

• WRITE: the agent failure catalogue, final, one page, with the check beside each failure.
• RECAP: the four failure signatures from memory; all four are on Saturday's paper.
• READ: Langfuse documentation, the observability overview.

### Interview angle

• [S] What are the common failure modes of LLM agents?
• [F] How do you debug an agent that gives a wrong result?
• [F] How do you stop an agent from looping for ever?
• [D] Your agent told the customer the refund was done and it was not; walk me through how you would find out, and how you would make sure you always find out.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Langfuse documentation, LLM Observability and Application Tracing (verified 21 Sep 2026):
https://langfuse.com/docs/observability/overview
• OpenTelemetry documentation, Traces (verified 21 Sep 2026):
https://opentelemetry.io/docs/concepts/signals/traces/
• Anthropic Engineering, Demystifying evals for AI agents, for the vocabulary of transcripts and traces (verified 21 Sep 2026):
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

### Student references

• Langfuse documentation, LLM Observability and Application Tracing (verified 21 Sep 2026):
https://langfuse.com/docs/observability/overview

### Kahoot quiz plan

• Q1: match the trace excerpt to the failure: four pairs
• Q2: the same call forty times; which two caps were missing
• Q3 trap: the tool returned 'ok', so the refund exists, true or false
• Q4: what a trace records at each step
• Q5: a run ended by hitting the step cap; success or failure, and where does the ticket go
• Return question from Thursday: a rule in the prompt against a rule in the structure; which one is a control.

## Sat 02 Jan 2027 · Saturday recap · The pen-and-paper test, then the interview-answer discussion

### Business scenario of the day

The acting assistant under questioning, from the tool set to the three incident reports. Every question on the paper is one of Farhan's or Anand's first and a technique question second, which is the order interviewers use.

### Thinking we train, before any tool

Saying the week out loud is the interview skill itself.

### Trainer agenda

Four hours, no new content.
1. Recap paper: pen and paper, AI-free, objective, to the blueprint of the 'Saturday papers' tab (110 min).
2. Break (20 min).
3. Marking: papers swapped and marked against the key, read out by the Academic TA (15 min).
4. Solution discussion led by the Academic TA: the most-missed items first, then the interview anchors answered aloud as interview answers, with random call-outs (70 min).
5. Doubts and the bridge: Farhan wants it live, and four people have conditions, which is Monday (25 min).

### Learner outcome

CAN DO: answer the week's business and technique questions on paper without an assistant.
CAN DEFEND: any answer aloud when called; mark a peer's paper against the discussed solution.
STATUS: ungraded; a performance indicator.

### Subtopics (technique in service of the scenario)

THE INTERVIEW ANCHORS (questions only):
• [S] What is an AI agent, and how is it different from a workflow or a chain?
• [S] Explain the ReAct pattern.
• [S] How do you design tools for an LLM agent?
• [S] How do agents handle memory? Short-term against long-term.
• [S] How do you add a human in the loop to an agent?
• [F] When would you choose a fixed workflow over an agent?
• [F] Why not just tell the model 'never refund above the limit'?
• [F] How do you stop an agent from looping for ever?
• [D] Your agent told the customer the refund was done and it was not; how do you find out?
• [D] Your manager wants 'an agent' for a task that four fixed steps solve; what do you build?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: an objective paper to the blueprint of the 'Saturday papers' tab: fill in the blank, true or false, one correct option, more than one correct option, scenario sets, applied maths and ordering, graded easy, medium and hard. Print the Item column only; the key, tag, role and anchor columns stay with the team.
PAPER STATUS: the items and the key for this week are still to be built into the 'Saturday papers' tab; this row's anchors are their source. Trace excerpts make good scenario sets this week.
MARKING: papers swap and are marked against the key, so a score is comparable across the room and from week to week.
DISCUSSION: the Academic TA opens with the most-missed items, then asks the interview anchors aloud as interview answers, with random call-outs.
STATUS: ungraded, AI-free by format; a performance indicator.

### Client zero data (TRAINER ONLY)

Answers cite the week's own tickets, flows and traces. Findings are discussed; plants are never revealed.

### In-session exercises

THE PAPER: objective, pen and paper, AI-free, for a 110-minute slot. The items and the key are still to be built into the 'Saturday papers' tab, to the same blueprint and the same minutes-per-item assumptions as Weeks 1 to 8.
• Marking a peer's paper against the key.
• Random call-outs on the interview anchors: sixty seconds each.

### After-class tasks

• RECAP: rewrite any question you lost marks on, one line each, in your own words.

### Interview angle

The question set in Subtopics is the interview set for the week.

### Trainer resources

• The 'Saturday papers' tab will hold the items and the key once built; this row's anchors are the source for the discussion.
• DataCamp, Top 30 Agentic AI Interview Questions and Answers for 2026, for the anchors' calibration (verified 21 Sep 2026):
https://www.datacamp.com/blog/agentic-ai-interview-questions

### Student references

• Reread the week's rows and your rejected answers; the next paper reuses missed ground one level up.

### Kahoot quiz plan

None. The recap test and discussion replace the quiz.

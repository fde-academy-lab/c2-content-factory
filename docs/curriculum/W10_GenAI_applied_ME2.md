# W10 GenAI applied + ME2

## Mon 07 Dec 2026 · Prompt techniques compared, and system prompts · Which prompt ships, proved on forty tickets

### Business scenario of the day

THE WEEK. Build 3 proved in Kalpa Connect that a model can read tickets under a contract. Farhan Sheikh now wants the same discipline at home: an assistant for Kalpa Retail's support desk that drafts, files and looks things up, and that he can change without fear. The week builds its five working parts: the prompt, the output contract, the first tool, the test suite and the cost review. Answering from Kalpa's own policies is next week's work.

MONDAY. Three of Farhan's team leads have each written a prompt for the first job, which is to read a ticket and say what kind it is and what the customer wants. Farhan: "One is three lines, one is two pages, and one has a dozen examples pasted in. Which do I ship, and how do you know it is better and is more than just longer?" Kavya Nair sets the condition: "Same forty tickets, same scoring, every technique. Keep the simplest one that ties."
Your role: you run the comparison, pick the prompt, and tell the team lead whose prompt lost why it lost.
On the table: what a prompt must contain for a reader that takes every word literally; what examples add and what they bias; when asking the model to reason first pays for its extra tokens; what belongs in the system prompt, which holds on every call, and what belongs in the message.

### Thinking we train, before any tool

A prompt is a specification written for a reader that takes every word literally and knows nothing about Kalpa. Each technique supplies something the bare instruction lacks. A clear instruction with the output named is zero-shot. Worked examples make it few-shot (established: Brown and others, 2020); they teach the format, and they bias the answers toward whatever they over-represent. Room to reason before answering is chain-of-thought (established: Wei and others, 2022), which buys accuracy on multi-step tickets at the price of tokens. Splitting one hard job into two easy calls is decomposition. The system prompt carries the role, the rules and the output shape that must hold on every call.
No technique is believed until all of them are compared on one task, with one fixed test set and one score, which is Week 5's baseline discipline applied to prompts. The simplest prompt that ties wins, because it costs less to run, to read and to maintain. A prompt built from structure keeps working when the model underneath changes, and one built on a lucky phrase stops.

### Trainer agenda

1. Farhan's three prompts read aloud; the room predicts the winner and writes the prediction down (10 min).
2. The task and the yardstick: forty labelled tickets, category and customer ask, one score; the three-line prompt scored as the baseline (35 min).
3. Examples: a few-shot prompt built and scored; the example set that tilts every answer toward one category (45 min).
4. Reasoning room and smaller steps: chain-of-thought and a two-call decomposition on the multi-issue tickets, with the token bill beside each score (45 min).
5. The system prompt: role, rules, output shape; what moves out of the message and why (30 min).
6. Guided then unguided: the comparison table for every technique, the prompt that ships, and its prompt-library entry with the score (55 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a prompt is a specification; each technique supplies something specific; examples bias as well as teach; reasoning room costs tokens; the simplest prompt that ties wins.
CAN DO: score a prompt on a fixed test set, build few-shot and chain-of-thought variants, split a job into two calls, write a system prompt, and keep a prompt library with a score per entry.
CAN HANDLE: an example set that tilts every answer, a longer prompt that scores lower, and a team lead who trusts the prompt that felt best.
CAN DEFEND: which prompt ships and why, with the score and the token bill, and what would change the choice.

### Subtopics (technique in service of the scenario)

• A prompt as a specification: instruction, context, output named
• Zero-shot as the baseline; the fixed test set and the single score
• Few-shot: what examples teach and what they bias
• Chain-of-thought: reasoning room and its token price
• Decomposition: two easy calls in place of one hard one
• The system prompt: role, rules and output shape that hold on every call
• The prompt library: versioned prompts, each with its score
• Prompt patterns that survive a model change

### Trainer notes

START FROM: Build 3's third clinic met the system prompt, zero-shot against few-shot and a contract written into the prompt; Week 8 Thursday fixed the decoding settings, which stay fixed all day so that only the prompt varies.
GO AS FAR AS: everyone ships a comparison table over at least four prompts, a chosen prompt and a library entry with its score.
STOP BEFORE: enforcing the output shape in code (Tuesday), tools (Wednesday), graders beyond exact match (Thursday), retrieval (Week 11).
COMES LATER: Tuesday turns today's named output into a contract a parser can trust; Thursday turns today's forty tickets into a regression suite.
FIRST-USE TOOLS: the course model endpoint, called from a notebook with the key held outside the code. The provider and the model are chosen and verified at the day build from the approved credits, and the setup instructions ship on Saturday night.
WHAT THE DATA REVEALS: the twelve-example prompt tilts most tickets toward the category its examples favour; chain-of-thought wins on the multi-issue tickets and roughly doubles the tokens; the two-page prompt loses to the three-line prompt with a named output. Let the table say it.
ME2 runs this week as a continuous activity with the day not fixed; state its scope aloud and no more.
CUT FIRST: the decomposition demo shrinks to one ticket. Never cut the tilted examples or the token bill beside the score.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION text-eval: forty support tickets drawn from the Week 8 tickets table, labelled by hand with the category and the customer's ask.
PLANTED: a block of multi-issue tickets that a one-line instruction gets wrong; an example set for the few-shot demo in which one category is over-represented.
No new named stakeholder. Students are never told what is planted.

### In-session exercises

GUIDED: the baseline prompt scored together; one few-shot variant built and scored.
UNGUIDED: the chain-of-thought and decomposition variants, the full comparison table, the chosen prompt and its library entry.
MID-SESSION (15 min each): rewrite three vague instructions so that the output is named; predict from five example sets which way each will tilt the answers.

### After-class tasks

• BUILD: a fifth prompt of your own, scored on the same forty tickets, with one sentence on why it won or lost.
• READ: the Prompt Engineering Guide, the few-shot and chain-of-thought pages.
• RECAP: 'the simplest prompt that ties wins', with its reason.
• SETUP: Tuesday's validation library installs from the setup cell; the instructions ship tonight.

### Interview angle

• [S] Zero-shot, few-shot and chain-of-thought: what is each, and when do you use it?
• [S] What goes in a system prompt, and what goes in the user message?
• [F] How do you decide between two prompts?
• [F] Your few-shot prompt works in testing and fails in production; what do you check first?
• [D] A colleague's two-page prompt 'feels better' than your three-line one; how do you settle it, and what do you say when theirs loses?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Prompt Engineering Guide, the techniques index (verified 21 Sep 2026):
https://www.promptingguide.ai/techniques
• Claude Platform Docs, Prompt engineering overview (verified 21 Sep 2026):
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
• Brown and others, Language Models are Few-Shot Learners, 2020 (verified 21 Sep 2026):
https://arxiv.org/abs/2005.14165
• Wei and others, Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, 2022 (verified 21 Sep 2026):
https://arxiv.org/abs/2201.11903

### Student references

• Prompt Engineering Guide, Few-Shot Prompting (verified 21 Sep 2026):
https://www.promptingguide.ai/techniques/fewshot
• Prompt Engineering Guide, Chain-of-Thought Prompting (verified 21 Sep 2026):
https://www.promptingguide.ai/techniques/cot
• Andrej Karpathy, Intro to Large Language Models, a one-hour talk (verified 21 Sep 2026):
https://www.youtube.com/watch?v=zjkBMFhNj_g

### Kahoot quiz plan

• Q1: name the technique: four prompts shown
• Q2: the examples are all refund tickets; which way do the answers tilt
• Q3 trap: the longer prompt is the better prompt, true or false
• Q4: chain-of-thought raised the score and doubled the tokens; when is that worth it
• Q5: system prompt or user message: five lines sorted
• Return question from Week 8 Thursday: the same prompt gave three different replies; which setting made it repeatable.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W10-1 · 120 min · faculty to be confirmed by IITGN.
TOPIC: How a model learns to follow instructions: pretraining, instruction tuning and preference optimisation, and in-context learning, which is why examples work without any training.
PICKS UP WHERE THE ROW STOPS: the row compares prompts by score and never asks why a prompt is obeyed at all.
CONNECTS TO KALPA: the example set that tilted every ticket toward one category.
BY THE END: a learner can describe the three training stages, and can say what in-context learning is and is not.
DOES NOT REPEAT: the comparison of techniques.

## Tue 08 Dec 2026 · Structured and constrained outputs · A contract the ticketing system can trust

### Business scenario of the day

TUESDAY. Monday's prompt names its output, and Farhan's ticketing system needs more than a name. The data platform lead sends the schema: a category from a fixed list, an order id in Kalpa's format, urgency as low, medium or high, a true-or-false refund flag and a one-line summary. "My queue takes JSON that matches this. One malformed record blocks the batch behind it." On the first pilot run, three of two hundred outputs break the parser: one opens with the sentence 'Sure, the JSON is below:', one drops the order id, and one sets urgency to 'very high'.
Your role: you make the assistant's output something a program can trust, and you decide what happens to the record that still fails.
On the table: what an output contract is made of; how far asking nicely gets you; what validation catches and what it cannot; how a decoder can be stopped from writing an invalid token at all; where a ticket goes when every repair fails.

### Thinking we train, before any tool

An output contract has three parts: a schema that says what is allowed, a validator that checks every output against it, and a policy for the output that fails. Enforcement comes in three strengths. Asking for JSON in the prompt is the weakest, and it fails a few times in every hundred. Validating and repairing sends the error text back to the model once or twice and then stops. Constrained decoding is the strongest: the provider or the library masks every next token that would break the schema, so an invalid output cannot be written (established: Willard and Louf, 2023; providers expose it as structured outputs, with limits on which schema features they support).
A valid shape can still carry a wrong value: an order id in the right format that belongs to no order passes every schema check. So the contract ends with semantic checks in code and a failure path that sends the ticket to a person. Build 3's triage sub-problem met this as 'a malformed output is a failed ticket', and today builds the machinery behind that sentence.

### Trainer agenda

1. Three broken records from the pilot run; the room names what broke each one (10 min).
2. The schema: fields, types, fixed lists, required against optional, written as JSON Schema and as a typed model (40 min).
3. Validation: the parser's error and the validator's error read aloud; the two deliberate failures run (35 min).
4. The repair loop: the error text returned to the model, a retry cap, and the token cost of each retry (35 min).
5. Constrained decoding: the same task with the provider's structured output switched on; what it guarantees and what it leaves to code (40 min).
6. Semantic checks and the failure path: the order id that fits the format and matches no order; the human queue (25 min).
7. Guided then unguided: the structured triage feature with its contract, its repair cap and its failure path (35 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a contract is a schema, a validator and a failure policy; enforcement has three strengths; a valid shape can carry a wrong value.
CAN DO: write a schema with fixed lists and required fields, validate model output against it, run a capped repair loop, switch on constrained decoding, and add a semantic check with a human queue behind it.
CAN HANDLE: a JSONDecodeError on a reply that opens with a sentence, a ValidationError on a value outside the list, a repair loop that never converges, and a well-formed order id that matches no order.
CAN DEFEND: which strength of enforcement the ticketing system needs, what it costs, and where a failed record goes.

### Subtopics (technique in service of the scenario)

• The output contract: schema, validator, failure policy
• JSON Schema and a typed model: types, fixed lists, required fields
• Parsing against validating; reading both error messages
• The repair loop with a retry cap, and its token cost
• Constrained decoding and provider structured outputs: what is guaranteed and what is unsupported
• Semantic checks that a schema cannot make
• The failure path: route to a person, log the record

### Trainer notes

START FROM: Monday's chosen prompt with its output named, and the output contracts written in Build 3.
GO AS FAR AS: everyone ships the triage feature returning valid records on the pilot set, with a repair cap of two and a human queue for what still fails.
STOP BEFORE: tools and function calling (Wednesday), grading the content of the summary (Thursday), streaming structured output.
COMES LATER: Wednesday applies the same schema discipline to tool arguments, and Week 13 depends on it for every tool an agent calls.
FIRST-USE TOOLS: a validation library for typed models (Pydantic is proposed, with the version pinned at the day build) and the provider's structured output mode.
WHAT THE DATA REVEALS: the reply that opens with a sentence raises json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0). The urgency of 'very high' raises a ValidationError that reads "Input should be 'low', 'medium' or 'high'" (text checked against Pydantic 2.13 on 21 Sep 2026; recheck at the day build). With structured output on, both vanish, and the order id that matches no order still gets through.
SECOND EXAMPLE: Rohan Desai's loan application summary at Kalpa Financial, where a missing income field must stop the record and must never be filled with a default.
CUT FIRST: the JSON Schema and typed model comparison shrinks to the typed model. Never cut the two error messages or the semantic check.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION text-eval: the forty tickets plus a saved pilot run of two hundred model outputs.
PLANTED: three malformed outputs (a sentence before the JSON, a missing order id, an urgency outside the fixed list); one ticket whose order id fits the format and matches no order in the orders table.
The order id format is whatever the v4 orders table already uses. Students are never told what is planted.

### In-session exercises

GUIDED: the schema written together; the two failures run and read.
UNGUIDED: the repair loop with its cap, structured output switched on, the semantic check, the failure path.
MID-SESSION (15 min each): six model outputs, say which pass the schema and which pass the business; write the failure policy for three fields in one sentence each.

### After-class tasks

• BUILD: add one field to the contract, the product named in the ticket, with its allowed values, and rerun the pilot set.
• READ: JSON Schema, Creating your first schema.
• RECAP: the three strengths of enforcement, weakest to strongest.
• SETUP: nothing to install for Wednesday.

### Interview angle

• [S] How do you get reliable JSON out of an LLM?
• [F] What is the difference between validating an output and constraining the decoder?
• [F] Your parser fails on two outputs in every hundred; what are your options, and what does each cost?
• [D] An output passes the schema and is still wrong; give an example and say where you would catch it.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• OpenAI API docs, Structured model outputs (verified 21 Sep 2026):
https://developers.openai.com/api/docs/guides/structured-outputs
• Claude Platform Docs, Structured outputs (verified 21 Sep 2026):
https://platform.claude.com/docs/en/build-with-claude/structured-outputs
• Pydantic Docs, Models (verified 21 Sep 2026):
https://pydantic.dev/docs/validation/latest/concepts/models/
• Willard and Louf, Efficient Guided Generation for Large Language Models, 2023 (verified 21 Sep 2026):
https://arxiv.org/abs/2307.09702
• Outlines, an open-source structured generation library (verified 21 Sep 2026):
https://github.com/dottxt-ai/outlines

### Student references

• JSON Schema, Creating your first schema (verified 21 Sep 2026):
https://json-schema.org/learn/getting-started-step-by-step

### Kahoot quiz plan

• Q1: schema, validator or failure policy: five statements sorted
• Q2: the reply opens with a sentence before the JSON; which error, and at which character
• Q3 trap: a record that passes the schema is correct, true or false
• Q4: the three strengths of enforcement, in order
• Q5: the repair loop ran five times on one ticket; which rule was missing
• Return question from Monday: the examples were all one category; what happened to the answers.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W10-2 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Constrained decoding from the inside: a schema as a grammar, finite-state machines over tokens, and masking of the next-token distribution; what a grammar can and cannot guarantee.
PICKS UP WHERE THE ROW STOPS: the row uses structured output as a switch.
CONNECTS TO KALPA: the urgency outside the fixed list becomes impossible to write, and the order id that matches no order stays possible.
BY THE END: a learner can draw the state machine for a small schema, and can explain why shape can be guaranteed and meaning cannot.
DOES NOT REPEAT: the repair loop.

## Wed 09 Dec 2026 · Function calling · The assistant looks the order up and stops guessing

### Business scenario of the day

WEDNESDAY. A customer writes: "Where is my order? It was meant to come on Friday." The prototype replies with a confident delivery date that exists nowhere in Kalpa's systems. Farhan: "It must look the order up. It must never guess." The data platform lead agrees to one read-only lookup of order status, on two conditions: "It reads only the orders of the customer who is asking, and I see every call it makes."
Your role: you give the assistant its first tool, decide when it may call it, and show the platform lead the log of every call.
On the table: who actually runs the tool, the model or your code; what the model has to read in order to call it well; when it should call, when it should answer directly and when it should ask the customer a question; what your code checks before it runs anything; what the model is told when the tool fails.

### Thinking we train, before any tool

The model never runs anything. It writes a structured request, a tool name with arguments, and the application decides whether to run it, runs it, and hands the result back so the model can compose the answer. Safety lives in that split, because the code can refuse any request the model writes. The tool's name, description and argument schema are themselves a prompt, so a vague description produces a tool that is never called or is called wrongly, and Tuesday's schema discipline now applies to arguments.
Three decisions belong to the design: when the model should call (the answer lives in a system), when it should answer directly (the answer is already in the conversation), and when it should ask (an argument is missing). A guessed argument is the failure to design out. Permission is checked in code against the signed-in customer and is never left to the prompt. A tool error goes back to the model as data, with a message it can act on.

### Trainer agenda

1. The invented delivery date; the room says where the true date lives and who may read it (10 min).
2. The loop on the board: request, check, run, result, answer; one call traced by hand (35 min).
3. The tool definition as a prompt: name, description, argument schema; a vague description against a precise one (40 min).
4. Call, answer or ask: five customer messages sorted; the missing order id and the clarifying question (35 min).
5. Checks in code before anything runs: the argument validated, the order matched to the signed-in customer, every call logged (35 min).
6. When the tool fails: the error returned as data; a timeout; an order that does not exist (25 min).
7. Guided then unguided: the order-status tool wired into the assistant with its checks and its call log (40 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: the model requests and the application runs; the tool definition is a prompt; permission lives in code; a tool error is data for the model.
CAN DO: define a tool with a precise description and schema, run the request-check-run-result loop, validate arguments, enforce ownership in code, log every call, and return errors the model can act on.
CAN HANDLE: a tool that is never called because its description is vague, an invented order id, a request for another customer's order, and a timeout.
CAN DEFEND: why the permission check sits in code and outside the prompt, and what the platform lead can read in the log.

### Subtopics (technique in service of the scenario)

• The function-calling loop: request, check, run, result, answer
• The tool definition as a prompt: name, description, argument schema
• Call, answer directly, or ask a clarifying question
• Argument validation before anything runs
• Permission in code: the signed-in customer's own orders only
• Errors returned as data: timeout, not found
• The call log

### Trainer notes

START FROM: Tuesday's schemas, now used for arguments; the v4 orders table behind one read-only function.
GO AS FAR AS: everyone ships an assistant that answers order-status questions from the tool, refuses another customer's order, and asks for a missing order id.
STOP BEFORE: more than one tool, loops of calls, planning; all of that is Week 13. Today is one call and one result.
COMES LATER: Week 13 Monday grows one tool into a designed tool set, and Week 14 Tuesday turns today's permission check into a guardrail layer.
WHAT THE DATA REVEALS: with the vague description the model answers from imagination and never calls the tool; with no order id in the message it invents one that fits the format; asked for a neighbour's order, the prompt-only rule gives the status away and the code check refuses. Let the room run all three.
SECOND EXAMPLE: Ananya Bose's plan lookup at Kalpa Connect, where the argument is a phone number and the same ownership rule applies.
CUT FIRST: the timeout case shrinks to a demonstration. Never cut the invented argument or the ownership check.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION v4 orders behind one read-only function for order status, plus ten customer messages.
PLANTED: a message with no order id; a message that asks about an order belonging to another customer; a tool description written vaguely for the first demo.
No Kalpa fact is added beyond the function. Students are never told what is planted.

### In-session exercises

GUIDED: the loop traced by hand, then run once end to end.
UNGUIDED: the precise tool definition, the argument and ownership checks, the error messages, the call log.
MID-SESSION (15 min each): rewrite three vague tool descriptions; sort eight customer messages into call, answer or ask.

### After-class tasks

• BUILD: a second read-only lookup of your choice from the v4 tables, defined and logged the same way; keep the two tools in separate conversations for now.
• READ: the provider's function calling guide, the overview section.
• RECAP: who runs the tool, in one sentence.

### Interview angle

• [S] What is function calling, and who executes the function?
• [F] How does the model decide to call a tool, and what can you do when it does not?
• [F] The model invents an argument the user never gave; how do you prevent it?
• [D] A customer asks the assistant for someone else's order; where exactly is that stopped, and why there?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• OpenAI API docs, Function calling (verified 21 Sep 2026):
https://developers.openai.com/api/docs/guides/function-calling
• Claude Platform Docs, Tool use with Claude (verified 21 Sep 2026):
https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
• Anthropic Engineering, Writing effective tools for AI agents, for the description-as-prompt idea (verified 21 Sep 2026):
https://www.anthropic.com/engineering/writing-tools-for-agents

### Student references

• OpenAI API docs, Function calling, the overview (verified 21 Sep 2026):
https://developers.openai.com/api/docs/guides/function-calling

### Kahoot quiz plan

• Q1: put the five steps of the loop in order
• Q2 trap: the model runs the function, true or false
• Q3: call, answer or ask: four messages
• Q4: where does the ownership check live
• Q5: the tool timed out; what does the model receive
• Return question from Tuesday: a record passes the schema and is wrong; name the check that catches it.

### IITGN faculty session (TENTATIVE)

None today.

## Thu 10 Dec 2026 · Prompt evaluation · A number every time the prompt changes

### Business scenario of the day

THURSDAY. In ten days the drafting prompt has changed twice and the vendor has updated the model once. Farhan's quality lead reads fifty drafted replies a week by hand and says they 'feel worse'. Nobody can prove it either way. Farhan: "I need a number every time someone touches the prompt, before it reaches a customer." Kavya: "Build the test set before anyone edits another word."
Your role: you build the evaluation suite for drafted replies, show that it agrees with the quality lead, and rerun it on the last three versions to find the change that did the damage.
On the table: what 'good' means for a drafted reply, written as checks; which checks code can make; when a model may grade a model, and how you know the grader is right; how a change that hurts quality is caught before release.

### Thinking we train, before any tool

Generation is evaluated the way Week 5 evaluated models: a fixed set, a stated yardstick, a baseline, and no peeking. The set is a golden set of real tickets, each with what a good reply must contain. The yardstick is a rubric of yes-or-no checks: the reply answers the question asked, states only policy that exists, promises nothing the agent cannot deliver, and stays inside the length. Graders are used in order of cost. Code checks come first because they are exact and free. Human labels come next because they define the truth. A model as judge comes last, for scale, and only after its verdicts have been compared with the human labels on the same replies.
A judge model has known biases (established: Zheng and others, 2023): it favours longer answers, the option shown first, and text that resembles its own. The suite then reruns on every change to the prompt, the model or the settings, which is how a silent drop after a vendor update is caught by a number and no longer by a feeling.

### Trainer agenda

1. 'It feels worse': the room says what evidence would settle it (10 min).
2. The golden set: thirty tickets and what a good reply must contain, written before any reply is read (35 min).
3. The rubric as yes-or-no checks; the checks code can make: length, banned promises, a named policy that exists (40 min).
4. A model as judge: the judging prompt, one reply graded, then the judge against the quality lead's labels on twenty replies (45 min).
5. Judge bias run live: the longer reply that invents a policy, and the verdict that flips when two replies swap places (30 min).
6. The regression run: three versions of the prompt through the suite, and the change that did the damage (25 min).
7. Guided then unguided: the evaluation suite with its report, and one failing check traced to a prompt line (35 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: evaluation is a fixed set, a rubric and a baseline; graders are used in order of cost; a judge model is trusted only after it agrees with human labels; every change reruns the suite.
CAN DO: build a golden set, write a rubric of yes-or-no checks, code the exact checks, write a judging prompt, measure its agreement with human labels, and run a regression across prompt versions.
CAN HANDLE: a judge that prefers the longer wrong reply, a verdict that flips with the order, a vendor update that lowers quality without any error, and a stakeholder who trusts a feeling.
CAN DEFEND: the suite's number, how the judge was checked, and which change caused the drop.

### Subtopics (technique in service of the scenario)

• The golden set, written before replies are read
• The rubric as yes-or-no checks
• Code checks first: exact, free, repeatable
• Human labels as the reference
• A model as judge: the judging prompt, and agreement with people
• Judge biases: length, position, self-preference
• The regression suite on every change; silent drift after a model update

### Trainer notes

START FROM: Monday's forty-ticket comparison, which was already a small evaluation; Week 5's test-set discipline.
GO AS FAR AS: everyone ships a suite of at least six checks over thirty tickets, an agreement figure for the judge, and the regression table for three prompt versions.
STOP BEFORE: retrieval metrics (Week 11 Thursday), trajectory evaluation (Week 14 Monday), and statistical tests on the difference between two versions.
COMES LATER: Friday uses this suite as the guard on every saving, and Week 16 Friday puts it into the release pipeline as a gate.
WHAT THE DATA REVEALS: the judge gives its top score to a longer reply that promises a return window Kalpa does not offer; swapping the order of two replies flips about one verdict in five; version three of the prompt dropped the line that forbids inventing policy, and the code check for named policies finds it.
CUT FIRST: the order-swap demo shrinks to two pairs. Never cut the comparison of the judge with the human labels.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION text-eval: thirty golden tickets with their required content, twenty replies labelled against the quality lead's rubric, and three saved versions of the drafting prompt.
PLANTED: a long reply that invents a return window; a pair of replies whose verdict depends on their order; prompt version three with the no-invention line removed.
The invented refund policy of Week 8 Thursday returns here as something a check can catch. Students are never told what is planted.

### In-session exercises

GUIDED: five golden tickets written together; two code checks; the judging prompt.
UNGUIDED: the rest of the suite, the agreement figure, the three-version regression, the damaging change named.
MID-SESSION (15 min each): turn four vague quality wishes into yes-or-no checks; say for six checks whether code, a person or a judge should make them.

### After-class tasks

• BUILD: add five tickets of your own to the golden set, including one the assistant should decline to answer.
• READ: Hamel Husain, Your AI Product Needs Evals, the first two levels.
• RECAP: the order in which graders are used, and why.

### Interview angle

• [S] How do you evaluate the output of an LLM application?
• [F] What is LLM-as-a-judge, and what are its failure modes?
• [F] How do you catch a quality regression when the vendor updates the model?
• [D] Your judge model and your human reviewer disagree on a third of the replies; what do you do before you trust either?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Zheng and others, Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, 2023 (verified 21 Sep 2026):
https://arxiv.org/abs/2306.05685
• Hamel Husain, Your AI Product Needs Evals (verified 21 Sep 2026):
https://hamel.dev/blog/posts/evals/
• Hamel Husain, Using LLM-as-a-Judge for Evaluation (verified 21 Sep 2026):
https://hamel.dev/blog/posts/llm-judge/
• Claude Platform Docs, Define success criteria and build evaluations (verified 21 Sep 2026):
https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### Student references

• Hamel Husain, Your AI Product Needs Evals (verified 21 Sep 2026):
https://hamel.dev/blog/posts/evals/
• Eugene Yan, Evaluating the Effectiveness of LLM-Evaluators (verified 21 Sep 2026):
https://eugeneyan.com/writing/llm-evaluators/

### Kahoot quiz plan

• Q1: code, person or judge: six checks assigned
• Q2: two judge biases named from their symptoms
• Q3 trap: the judge scored it nine out of ten, so it is good, true or false
• Q4: what must exist before the prompt is edited again
• Q5: quality fell after a vendor update and nothing errored; what catches it
• Return question from Wednesday: who runs the tool, and where is permission checked.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W10-3 · 120 min · faculty to be confirmed by IITGN.
TOPIC: The statistics of evaluation: how many examples a test set needs, agreement between graders and Cohen's kappa, a confidence interval on a pass rate, and when a difference between two prompt versions is real.
PICKS UP WHERE THE ROW STOPS: the row stops before statistical tests on the difference between two versions.
CONNECTS TO KALPA: the judge against the quality lead on twenty replies; the intervals of the Week 2 block return.
BY THE END: a learner can compute kappa for a small table, put an interval on a pass rate, and size a golden set.
DOES NOT REPEAT: the rubric and the graders.

## Fri 11 Dec 2026 · Production cost and latency · Cheaper and faster, with the evaluation score beside every saving

### Business scenario of the day

FRIDAY. The pilot handles three hundred tickets a day and Farhan wants all two thousand. Anand Iyer brings back the Week 8 cost model with a ceiling per ticket pencilled in, and Farhan adds a second number: in the agent-assist screen the first words of a draft must appear within two seconds, or his agents stop waiting and type the reply themselves. "Cheaper and faster, and I want Thursday's number to prove it did not get worse."
Your role: you bring the cost per ticket under Anand's ceiling and the first words under two seconds, and every saving you claim carries its evaluation score beside it.
On the table: what can be sent less often or not at all; which tickets a smaller model handles just as well; what a cache saves and when it serves a stale answer; what streaming changes and what it leaves alone; how three numbers are read together.

### Thinking we train, before any tool

Three levers, judged on three numbers. The first lever is to send less: trim the system prompt that Week 8 found on every call, cap the ticket history, and let the provider cache the repeated prefix so that it is billed at a fraction of the normal input price. The second is to send the work somewhere cheaper: a smaller model for the easy tickets and the larger one for the hard ones, chosen by a rule or a classifier, which is model routing. The third is to make the wait feel shorter: streaming puts the first words on screen while the rest is still being written, which shortens the time to the first token the agent sees and leaves the total unchanged.
Every change is read on cost per ticket, latency and Thursday's evaluation score together, and a saving that lowers the score on any slice of tickets is a cost moved onto the customer. The three-number rule is this course's construction. Caching whole answers in your own application is a fourth lever with a sharper edge, because it serves yesterday's answer after the policy has changed.

### Trainer agenda

1. Anand's ceiling and Farhan's two seconds; the room guesses the biggest saving before anything is measured (10 min).
2. The baseline measured: cost per ticket, time to first token, total time, evaluation score (30 min).
3. Send less: the trimmed system prompt, the capped history, the provider's prefix cache, each measured on all three numbers (45 min).
4. Route: easy tickets to a smaller model; the average that holds while the multi-issue slice drops (45 min).
5. Streaming in the agent-assist view; what moved and what did not (25 min).
6. The application cache and its stale answer (20 min).
7. Guided then unguided: the cost review for Anand and Farhan, three numbers per change, one change rejected with its reason (45 min).
8. Kahoot, close, and the ME2 scope stated (20 min).

### Learner outcome

UNDERSTANDS: cost and latency have three levers; every saving is read with the evaluation score; an average can hide a slice that got worse; streaming changes the first token and leaves the total; a response cache can go stale.
CAN DO: measure cost per ticket, time to first token and total time; trim and cache a prefix; route by difficulty; stream a reply; write a cost review with three numbers per change.
CAN HANDLE: a saving that lowers quality on one slice, a cache that serves an outdated policy, and a finance controller who wants the cheapest option.
CAN DEFEND: every accepted saving and the one rejected, with the numbers.

### Subtopics (technique in service of the scenario)

• The baseline: cost per ticket, time to first token, total time, evaluation score
• Token budget discipline: the system prompt and the history
• Provider prompt caching of a repeated prefix
• Model selection by task, and routing; the slice check
• Streaming, and what it changes
• Application-level response caching and staleness
• The three-number rule (course construction) and the cost review

### Trainer notes

START FROM: the Week 8 Friday cost model, which named caching and routing as coming; Thursday's suite, which is today's guard.
GO AS FAR AS: everyone ships a cost review with at least three changes, each with three numbers, and one change rejected.
STOP BEFORE: serving your own model, GPU arithmetic and batch interfaces, which Week 14 Thursday names for agents; prices, which are read from the provider's page at the day build and marked illustrative wherever they are printed.
COMES LATER: Week 14 Thursday returns to the same three numbers for an agent, per task in place of per ticket; Week 16 Tuesday reuses this arithmetic for a client's monthly run cost.
WHAT THE DATA REVEALS: the trimmed and cached prefix is the largest saving and costs nothing in quality; routing holds the average score and drops the multi-issue slice sharply, which is the Week 1 lesson about averages in a new place; the application cache repeats Tuesday's return window after the policy file changed on Wednesday.
ME2 (deep learning, transformers, LLM internals, generative AI) runs this week as a continuous activity; the day is not fixed; state the scope aloud and no more.
CUT FIRST: the application cache shrinks to a demonstration. Never cut the slice check on routing.

### Client zero data (TRAINER ONLY)

PROPOSED FOR CLIENT ZERO v2.3 (21 Sep 2026, not yet locked). VERSION text-eval with Thursday's suite, at pilot volume, with two model sizes available and illustrative prices.
PLANTED: the oversized system prompt carried over from Week 8 Friday; the multi-issue slice that the smaller model fails; a policy file that changes between two runs, so that a cached answer goes stale.
Anand's ceiling per ticket is fixed at the day build and recorded in v2.3; until then this row carries no rupee figure. Students are never told what is planted.

### In-session exercises

GUIDED: the baseline measured together; the prefix trimmed and cached.
UNGUIDED: routing with the slice check, streaming, the cost review with one rejection.
MID-SESSION (15 min each): for five proposed savings, predict which of the three numbers each one moves; find the slice that an average is hiding in two result tables.

### After-class tasks

• WRITE: the cost review, one page, numbers first.
• READ: the provider's prompt caching page, to see what qualifies as a cached prefix.
• PREP: Saturday is revision and the ME2 window; reread the week's five artifacts.

### Interview angle

• [S] How would you reduce the cost of an LLM feature in production?
• [S] What does streaming improve, and what does it leave unchanged?
• [F] What is prompt caching, and when does it help?
• [F] When would you route requests to a smaller model, and how do you know it is safe?
• [D] Your change cut cost by forty percent and the average quality held; what would you check before shipping it?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Claude Platform Docs, Prompt caching (verified 21 Sep 2026):
https://platform.claude.com/docs/en/build-with-claude/prompt-caching
• OpenAI API docs, Prompt caching (verified 21 Sep 2026):
https://developers.openai.com/api/docs/guides/prompt-caching
• OpenAI API docs, Latency optimization (verified 21 Sep 2026):
https://developers.openai.com/api/docs/guides/latency-optimization
• Ong and others, RouteLLM: Learning to Route LLMs with Preference Data, 2024 (verified 21 Sep 2026):
https://arxiv.org/abs/2406.18665

### Student references

• OpenAI API docs, Latency optimization (verified 21 Sep 2026):
https://developers.openai.com/api/docs/guides/latency-optimization
• Claude Platform Docs, Streaming messages (verified 21 Sep 2026):
https://platform.claude.com/docs/en/build-with-claude/streaming

### Kahoot quiz plan

• Q1: which of the three numbers does each of five changes move
• Q2: streaming cut the total time, true or false
• Q3 trap: the average score held after routing, so routing is safe
• Q4: what does a provider's prefix cache need in order to hit
• Q5: the cached answer is wrong today and was right yesterday; what happened
• Return question from Thursday: name two biases of a judge model.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W10-4 · 120 min · faculty to be confirmed by IITGN.
TOPIC: The arithmetic of inference: why output tokens cost more than input tokens, the memory of the KV cache, batching and throughput, and quantisation at recognition depth.
PICKS UP WHERE THE ROW STOPS: the row stops before serving a model and before GPU arithmetic.
CONNECTS TO KALPA: the cached prefix and the two-second first token.
BY THE END: a learner can estimate the KV cache memory for a given context, and can explain the trade between latency and throughput. The block closes the theory that ME2 draws on.
DOES NOT REPEAT: the cost review.

## Sat 12 Dec 2026 · Saturday · Revision, the recap test, and the ME2 window

### Business scenario of the day

Revision and the ME2 window. ME2 covers deep learning, transformers, LLM internals and generative AI; the exact slot is a Programme Head call. The remaining hours are the week's recap paper and the interview-answer discussion.

### Thinking we train, before any tool

Saying the module out loud is the interview skill itself.

### Trainer agenda

Four hours.
1. ME2 window, reserved without stating marks or slot (up to half the block).
2. Recap paper: pen and paper, AI-free, objective, to the blueprint of the 'Saturday papers' tab (60 min).
3. Marking against the key with papers swapped (10 min), then the solution discussion led by the Academic TA: the most-missed items, the interview anchors answered aloud, random call-outs (35 min).
4. Week 11 preview: the assistant has to answer from Kalpa's own policies and show where each answer came from (15 min).

### Learner outcome

CAN DEFEND: the assistant's five working parts end to end under questioning.
STATUS: the recap is ungraded; ME2 is graded and its marks are stated nowhere here.

### Subtopics (technique in service of the scenario)

THE INTERVIEW ANCHORS (questions only):
• [S] Zero-shot, few-shot and chain-of-thought: what is each, and when do you use it?
• [S] How do you get reliable JSON out of an LLM?
• [S] What is function calling, and who executes the function?
• [S] How do you evaluate the output of an LLM application?
• [F] What is LLM-as-a-judge, and what are its failure modes?
• [F] What is prompt caching, and when does it help?
• [F] The model invents an argument the user never gave; how do you prevent it?
• [D] An output passes the schema and is still wrong; where do you catch it?
• [D] Your change cut cost by forty percent and the average quality held; what do you check before shipping?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

SCOPE: say ME2's four theme areas aloud and nothing about marks or weights.
FORMAT: an objective paper to the blueprint of the 'Saturday papers' tab: fill in the blank, true or false, one correct option, more than one correct option, scenario sets, applied maths and ordering, graded easy, medium and hard. Print the Item column only; the key, tag, role and anchor columns stay with the team.
PAPER STATUS: the items and the key for Weeks 10, 11, 13 and 14 are still to be built into the 'Saturday papers' tab; this row's anchors are their source.
MARKING: papers swap and are marked against the key, so a score is comparable across the room and from week to week.
DISCUSSION: the Academic TA opens with the most-missed items, then asks the interview anchors aloud as interview answers, with random call-outs.
STATUS: ungraded, AI-free by format; a performance indicator.

### Client zero data (TRAINER ONLY)

Revision answers cite the week's own artifacts; the exam themes match what the spine already carried.

### In-session exercises

THE PAPER: objective, pen and paper, AI-free, for a 60-minute slot. The items and the key are still to be built into the 'Saturday papers' tab, to the same blueprint and the same minutes-per-item assumptions as Weeks 1 to 8.
• Marking a peer's paper against the key.
• Random call-outs on the interview anchors: sixty seconds each.

### After-class tasks

• REST: Week 11 opens Monday on retrieval; Monday's setup instructions ship on Sunday evening.

### Interview angle

The question set in Subtopics is the interview set for the week.

### Trainer resources

• The 'Saturday papers' tab will hold the items and the key once built; this row's anchors are the source for the discussion.
• DataCamp, Top 36 Generative AI Interview Questions and Answers for 2026, for the anchors' calibration (verified 21 Sep 2026):
https://www.datacamp.com/blog/genai-interview-questions
• DataCamp, Top 36 LLM Interview Questions and Answers for 2026 (verified 21 Sep 2026):
https://www.datacamp.com/blog/llm-interview-questions

### Student references

• Reread the week's rows and your rejected answers; the next paper reuses missed ground one level up.

### Kahoot quiz plan

None. Revision and the recap replace the quiz.

### IITGN faculty session (TENTATIVE)

None. The Saturday block is revision, the recap paper and the ME2 window.

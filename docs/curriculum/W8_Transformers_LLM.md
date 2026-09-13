# W8 Transformers, LLM

## Mon 16 Nov 2026 · Tokenization · What a ticket costs, and why the vendor bills by the token

### Business scenario of the day

Farhan Sheikh runs Kalpa Retail's customer support: two thousand tickets a day, forty agents, an average first reply of eleven hours. He has heard the data team can now read text. "If a model can read a ticket, can it draft the reply? What would that cost per ticket, and why does the vendor quote me by the token, whatever a token is?"
Your role: you explain to Farhan what a token is in his own tickets, cost one day's volume, and tell him why two vendors quote different prices for the same ticket.
On the table: how a model reads text when it cannot read words; why vocabularies exist; what a token count does to a bill and to quality; why the same ticket is longer for one model than another.

### Thinking we train, before any tool

Models read tokens, not words. A vocabulary is built from frequency, so common words are one token and a Kalpa product code shatters into five. Every token is billed, on the way in and on the way out, so tokenization is a cost decision as well as a modelling one, and two vendors with different vocabularies count the same ticket differently.
Farhan's question is the token economy in miniature, and it returns Friday at scale.

### Trainer agenda

1. Farhan's ask; one ticket tokenized by two tokenizers, two counts (10 min).
2. From characters to subwords: why vocabularies exist and what BPE optimises (50 min).
3. Token counts drive cost and quality: one day of tickets costed (45 min).
4. Tokenizer differences across models and what they break (35 min).
5. Guided then unguided: the tokenizer demo on Kalpa tickets, one costed day, one explained surprise (55 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: models read tokens, BPE builds a vocabulary from frequency, every token is billed, and vocabularies differ by model.
CAN DO: tokenize ticket text, count and cost a day's volume, and explain a surprising split.
CAN HANDLE: a product code shattered into five tokens, and two models disagreeing on the same ticket's length.
CAN DEFEND: to Farhan, why the vendor bills by the token and what that does to his budget.

### Subtopics (technique in service of the scenario)

• Characters, words, subwords
• BPE and vocabularies at intuition level
• Token counts against cost and quality
• Tokenizer differences across models
• The tokenizer demo on Kalpa tickets

### Trainer notes

START FROM: Friday's bridge; tokens are what next-token prediction predicts.
GO AS FAR AS: everyone ships the tokenizer demo with one costed day of tickets.
STOP BEFORE: training a tokenizer, attention (tomorrow).
COMES LATER: attention Tuesday, embeddings Wednesday with the classical lineage, decoding Thursday, economics Friday.
WHAT THE DATA REVEALS: a Kalpa product code splits into five tokens and the count surprises; the room explains it from frequency.
CUT FIRST: the second tokenizer comparison. Never cut the costing arithmetic.

### Client zero data (TRAINER ONLY)

VERSION text: the support_tickets table enters, with the reviews from Friday.
PLANTED: product codes that shatter; two tokenizers that disagree on the same ticket.
Farhan Sheikh is the Week 8 stakeholder and returns in Weeks 10 to 15 as the assistant's owner.

### In-session exercises

GUIDED: tokenize and cost one ticket together.
UNGUIDED: the demo on three ticket types with counts, a costed day, one explained surprise.
MID-SESSION (15 min each): predict which of four strings tokenizes longest; halve a ticket's tokens without losing its complaint.

### After-class tasks

• BUILD: cost the same day at two model price points and note the ratio.
• READ: chapter one of the Hugging Face LLM course.
• RECAP: tokens are money, one line with a number.

### Interview angle

• [S] What is a token, and why do token counts decide cost?
• [F] Why does the same text have different lengths in two models?
• [D] A support head asks whether an auto-reply is affordable; walk him from tokens to a monthly number.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Hugging Face LLM course, chapter 1 (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• Karpathy, Zero to Hero, the tokenizer lecture (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html

### Student references

• Hugging Face LLM course, chapter 1 (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1

### Kahoot quiz plan

• Q1: models read what unit
• Q2: BPE merges by what signal
• Q3: a day of tickets is 1.2 million tokens at the price shown; cost it
• Q4 trap: same ticket, two models, two lengths; broken or expected
• Q5: one way to cut a ticket's tokens without cutting its complaint
• Return question from Week 7 Friday: why next-token prediction needs no labelled data, one line.

## Tue 17 Nov 2026 · Attention and self-attention · How the model knows which 'it' the customer means

### Business scenario of the day

Farhan sends a ticket that broke the old rules-based triage: 'Ordered the charger and the case. The case arrived. It does not fit. I want to return it.' The rules flagged 'charger' as the product; the customer means the case. "How does a model know which 'it' is which?"
Your role: you walk Farhan through how a model resolves 'it' across forty tokens, and you show him one case where it will still get it wrong.
On the table: how every token consults every other; what queries, keys and values do; why several heads run at once; why word order has to be injected.

### Thinking we train, before any tool

Attention scores every token pair: each token asks a question (the query), every token offers an answer (the key), and the matching tokens contribute their content (the value). Several heads run those conversations in parallel. The mechanism is order-blind, so position is injected, which is why the room's shuffled ticket barely changes the raw scores.
Farhan's 'it' is resolved by attention weight, and the case where it still fails is the case where the ticket itself is ambiguous.

### Trainer agenda

1. Farhan's broken-triage ticket; the room says which tokens 'it' should look at (10 min).
2. The lookup intuition: every token asks a question of every other (50 min).
3. Queries, keys and values named onto the intuition (50 min).
4. Multi-head; positional information; the shuffled ticket (40 min).
5. Guided then unguided: the attention walkthrough on the ticket, then on a second ticket, the ambiguous case found (50 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: attention scores every pair; queries ask, keys answer, values carry; heads run in parallel; position is injected because the mechanism is order-blind.
CAN DO: walk one attention step by hand on a ticket and read a real attention pattern.
CAN HANDLE: the order-blindness surprise, and a ticket where the referent is genuinely ambiguous.
CAN DEFEND: Q, K and V in one sentence each, to Farhan and to an interviewer.

### Subtopics (technique in service of the scenario)

• The pairwise lookup intuition
• Queries, keys, values
• Multi-head attention
• Positional information
• The attention walkthrough on a ticket

### Trainer notes

START FROM: the long-range failure from Friday; attention arrives as the fix the room already specified.
GO AS FAR AS: everyone completes the hand walkthrough on the ticket.
STOP BEFORE: the scaled dot-product derivation, KV caching, architecture variants.
COMES LATER: embeddings tomorrow explain what the vectors mean; economics Friday explains what all these pairs cost.
WHAT THE DATA REVEALS: shuffle the ticket and the raw pair scores barely move; the room asks for position by name.
CUT FIRST: the second head example. Never cut the hand walkthrough.

### Client zero data (TRAINER ONLY)

VERSION text: Farhan's ticket and a second, genuinely ambiguous one.
PLANTED: the ambiguous referent that attention cannot resolve.
The broken rules-based triage is the same class of failure Build 3 hands to Kalpa Connect.

### In-session exercises

GUIDED: the hand walkthrough on Farhan's ticket, scores on the board.
UNGUIDED: repeat on the second ticket; mark which pair dominates and why; name the ambiguous case.
MID-SESSION (15 min each): match Q, K, V to their jobs; predict which token 'it' attends to in two tickets.

### After-class tasks

• READ: The Illustrated Transformer, first half.
• RECAP: Q, K, V, one sentence each, from memory.

### Interview angle

• [S] Self-attention: what do queries, keys and values each do?
• [F] Why does a transformer need positional information?
• [D] A support head asks why the model got a referent wrong; explain attention and where it cannot help.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Jay Alammar, The Illustrated Transformer (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/
• Hugging Face LLM course, the transformer chapter (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1

### Student references

• Jay Alammar, The Illustrated Transformer, first half (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/

### Kahoot quiz plan

• Q1: who asks, who answers, who carries
• Q2: multi-head buys what
• Q3 trap: shuffle the ticket; what happens to raw attention and why is that a problem
• Q4: position information exists because the mechanism is what
• Q5: read the pattern: which token does 'it' attend to
• Return question from Monday: the product code split into five tokens; explain it and the cost effect.

## Wed 18 Nov 2026 · Embeddings and the classical lineage · Finding the five tickets most like this one

### Business scenario of the day

Farhan's second ask: "When a ticket comes in, find me the five past tickets most like it, so the agent sees how we solved it last time." His team tried keyword search; 'not working' and 'working fine' matched each other. Kavya adds the history question: "Show the room how the field got here: counting words, then word vectors, then vectors that know context. Each step fixed the last one's wall."
Your role: you build the similar-tickets lookup, show Farhan a match that is close and wrong, and explain what nearness captures and misses.
On the table: why counting words fails on 'not working' against 'working fine'; what a word vector adds and where it stalls; what a contextual embedding changes; what a similarity score does and does not promise.

### Thinking we train, before any tool

The classical arc as one morning: bag of words and TF-IDF count, and cannot tell 'not working' from 'working fine'; static word vectors add meaning but give one vector per word regardless of sentence; contextual embeddings give the same word different vectors in different sentences, which is what Farhan's lookup needs.
Similarity in vector space is useful and fallible: a neighbour can be close and wrong, and the room learns to read a nearest-neighbour list critically, which is the judgment the retrieval weeks live on.

### Trainer agenda

1. Farhan's ask and the keyword failure; the room says why 'not working' matched 'working fine' (10 min).
2. The classical arc: counts, TF-IDF, static word vectors, each with its win and its wall (70 min).
3. Contextual embeddings: the same word, different vectors (45 min).
4. Similarity and its limits; the close-and-wrong neighbour (40 min).
5. Guided then unguided: the similar-tickets explorer, five neighbours, one read critically (55 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: the field walked from counting to static vectors to contextual vectors, each fixing the previous wall; similarity is useful and fallible.
CAN DO: compute a similarity, build the similar-tickets lookup, read a neighbour list critically, place the three generations on the lineage.
CAN HANDLE: two same-worded tickets TF-IDF cannot separate, and a neighbour that is close and wrong.
CAN DEFEND: what embeddings capture and miss; it returns verbatim in Weeks 11 and 12.

### Subtopics (technique in service of the scenario)

• Bag of words and TF-IDF, the classical morning
• Static word vectors and their wall
• Contextual embeddings
• Similarity and its limits
• The similar-tickets explorer

### Trainer notes

START FROM: Friday's pre-read seeded the classical vocabulary; the plan's one focused classical-NLP treatment runs as this morning's arc. Flag to the Programme Head if a standalone day is wanted; Friday would then compress.
GO AS FAR AS: everyone ships the explorer with one neighbour read critically.
STOP BEFORE: training embeddings, dimensionality mathematics.
COMES LATER: Weeks 11 and 12 live on today's similarity judgment.
WHAT THE DATA REVEALS: TF-IDF scores the opposite-meaning pair as near-identical; the contextual pair separates them; one neighbour at 0.91 is wrong. Let the room find all three.
CUT FIRST: the static-vector analogy games. Never cut the same-words trap.

### Client zero data (TRAINER ONLY)

VERSION text: the tickets table with planted same-word opposite-meaning pairs.
PLANTED: 'not working' against 'working fine'; a 0.91 neighbour that is wrong.
The explorer is the seed of the Week 11 retrieval system.

### In-session exercises

GUIDED: one TF-IDF score and one similarity together.
UNGUIDED: the explorer on the tickets, five neighbours for three queries, one critical note.
MID-SESSION (15 min each): place six techniques on the lineage map; call trust-or-doubt on four similarity pairs.

### After-class tasks

• READ: The Illustrated Transformer, second half.
• RECAP: the three generations, one wall each.

### Interview angle

• [S] What is an embedding, and what does similarity capture and miss?
• [F] Static against contextual embeddings in one line.
• [D] A support head trusts the similarity score; show him a 0.91 that is wrong and say what that teaches.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Jay Alammar, The Illustrated Transformer, second half (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/
• Hugging Face LLM course, the embeddings material (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1

### Student references

• Hugging Face LLM course, continue from chapter 1 (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1

### Kahoot quiz plan

• Q1: TF-IDF rewards what and misses what
• Q2: static against contextual in one line
• Q3 trap: similarity 0.91 on the pair shown; trust or doubt
• Q4: the same word, two vectors; which generation allows it
• Q5: place three techniques on the lineage fast
• Return question from Tuesday: Q, K, V, one sentence each, no notes.

## Thu 19 Nov 2026 · Decoding controls · Making the draft reply repeatable, and stopping it inventing

### Business scenario of the day

Farhan wants the draft reply. The first prototype writes three different replies to the same ticket on three runs; one of them invents a refund policy Kalpa does not have. "I cannot put that in front of a customer. Make it say the same thing every time, and make it stop inventing."
Your role: you set the generation dials for three jobs, a summary, a field extraction and a draft reply, and you show Farhan which setting produced the invention.
On the table: why the same prompt gives different outputs; what temperature, top-k and top-p each change; when repeatability is required and how it is bought; why an output sometimes runs on until the budget dies.

### Thinking we train, before any tool

Generation samples from a probability list at every step, and the dials reshape that list: temperature flattens or sharpens it, top-k and top-p cut its tail. A support draft wants a sharp list and a fixed seed; a brainstorm wants the tail. Determinism is a setting chosen when a pipeline must be repeatable.
The invented refund policy came from a flat list; the runaway output came from a missing stop, and the room costs that runaway aloud, tying Monday's money lesson in.

### Trainer agenda

1. Three replies to one ticket, one invented; the room guesses the dial (10 min).
2. Greedy against sampling: the probability list every token comes from (45 min).
3. Temperature, top-k and top-p moved live on Farhan's ticket (55 min).
4. Stopping conditions and determinism; the runaway output costed (40 min).
5. Guided then unguided: the controlled-output app for the three support jobs, settings defended (50 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: generation samples from a list; the dials reshape it; determinism is a choice; a missing stop costs money.
CAN DO: set the dials per job, make a reply repeatable, and ship the controlled-output app.
CAN HANDLE: a temperature that invented a policy, and a stop condition that never fired.
CAN DEFEND: which dial for which job, with the invented reply as evidence.

### Subtopics (technique in service of the scenario)

• Greedy against sampling
• Temperature
• Top-k and top-p
• Stopping conditions
• Determinism and seeds
• The controlled-output app for support

### Trainer notes

START FROM: auto-regression from Week 7 Friday; every dial edits the same list.
GO AS FAR AS: everyone ships the app with settings defended per job.
STOP BEFORE: beam search, penalty parameters, provider-specific flags.
COMES LATER: Week 10's structured output assumes today's dials are owned.
WHAT THE DATA REVEALS: the invented policy appears at high temperature; the runaway pads to the budget; both are reproduced and costed.
CUT FIRST: top-k against top-p subtleties. Never cut the three-replies opener or the runaway.

### Client zero data (TRAINER ONLY)

VERSION text: Farhan's ticket set with three prompt jobs.
PLANTED: the high-temperature invention; the missing stop.
The 'stop inventing' ask is the grounding problem Week 11 solves properly.

### In-session exercises

GUIDED: temperature moved live; three outputs read.
UNGUIDED: the app with settings per job and one sentence of defence each.
MID-SESSION (15 min each): match five dial settings to five jobs; spot the setting that produced the output shown.

### After-class tasks

• BUILD: one more support job added with its settings defended.
• RECAP: the dials in one line each.

### Interview angle

• [S] Temperature, top-k and top-p: what does each change?
• [F] How do you make an LLM output repeatable, and when must you?
• [D] The model invented a policy in front of a customer; explain to the support head what happened and what you changed.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Hugging Face LLM course, the generation material (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• Jay Alammar, The Illustrated GPT-2, the sampling visuals (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-gpt2/

### Student references

• Jay Alammar, The Illustrated GPT-2 (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-gpt2/

### Kahoot quiz plan

• Q1: temperature 0 buys what and costs what
• Q2: top-p 0.9 keeps which tokens
• Q3 trap: the extraction job needs which dial profile
• Q4: the output padded to the budget; name the missing setting
• Q5: same prompt, different answers, and Farhan is worried; your one-line reply
• Return question from Wednesday: similarity 0.91 and wrong; what does that teach.

## Fri 20 Nov 2026 · Context windows and the token economy · The cost model for the auto-reply at scale

### Business scenario of the day

Two bills for the same pilot week arrive from two vendors, one five times the other. Anand wants to know why before anything scales to two thousand tickets a day. Farhan wants to know why the assistant sometimes 'forgets the beginning of the ticket'.
Your role: you build the cost model for the auto-reply at scale, find the single biggest saving, and explain the forgetting to Farhan as a budget, not a bug.
On the table: what a context window is and what falls out when it fills; why the prompt and the reply are priced differently; where the waiting happens; what batching trades away.

### Thinking we train, before any tool

The context window is a hard budget: when it fills, the oldest content falls out, and a long ticket history pushes the instructions out first, which is Farhan's 'forgetting'. Prompt tokens and completion tokens are priced differently, so an oversized system prompt dominates a bill. Latency has named sources; batching trades responsiveness for throughput.
The cost model is the week's closing artifact and the interview anchor for engineering roles: tokens per ticket, tickets per day, two price points, the biggest saving named.

### Trainer agenda

1. Two bills, five times apart; the room says what settings could do that (10 min).
2. The context window as budget; the silent overflow (45 min).
3. Prompt against completion cost; the arithmetic on Farhan's volumes (50 min).
4. Latency sources and batching trades (35 min).
5. Guided then unguided: the cost model for the auto-reply, the biggest saving named, the answer to Farhan (60 min).
6. Kahoot and week close (20 min).

### Learner outcome

UNDERSTANDS: the window is a budget, prompt and completion price differently, latency has sources, batching trades.
CAN DO: build the cost model for a stated workload and find the biggest saving.
CAN HANDLE: a window overflow that silently dropped the instructions, and a bill dominated by a system prompt.
CAN DEFEND: the cost model line by line, and the forgetting explained as a budget.

### Subtopics (technique in service of the scenario)

• Context windows as budgets; the silent overflow
• Prompt against completion cost
• Latency sources
• Batching trades
• The cost model artifact

### Trainer notes

START FROM: Monday's token arithmetic and Thursday's runaway; the week closes where it opened, on money.
GO AS FAR AS: everyone ships the cost model with one named saving and the forgetting explained.
STOP BEFORE: caching strategies and model routing, which belong to Week 10 and are named as coming.
WHAT THE DATA REVEALS: the overflow pushes the instructions out and quality drops with no error; the five-times bill is an oversized system prompt on every call.
CUT FIRST: the batching demo. Never cut the overflow.

### Client zero data (TRAINER ONLY)

VERSION text: Farhan's three prompt jobs at daily volume, two vendor price points.
PLANTED: the overflow on a long ticket history; the oversized system prompt.
The cost model is the module's closing artifact and Build 3's budget constraint.

### In-session exercises

GUIDED: cost one job together, prompt and completion separated.
UNGUIDED: the full cost model, the biggest saving, the answer to Farhan.
MID-SESSION (15 min each): find the saving in three billed examples; predict what the overflow drops first.

### After-class tasks

• BUILD: recost at a second price point.
• RECAP: the week in five lines, one per day.
• PREP: Saturday is the week under questioning; Build 3 opens Monday in Kalpa Connect.

### Interview angle

• [S] What is a context window, and what happens when it overflows?
• [F] Why do prompt and completion tokens cost differently, and what does that change about how you design a prompt?
• [D] Estimate the monthly cost of an auto-reply feature for a support desk; what inputs do you need, and where is the saving?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Hugging Face LLM course, for current model-facing framing (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• Karpathy, Zero to Hero, for the internals grounding under the economics (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html

### Student references

• Reread the week's tokenizer and cost notebooks; the numbers are the revision.

### Kahoot quiz plan

• Q1: the window fills; what falls out and what error do you get
• Q2: prompt 4,000 tokens, completion 300; where does the money go
• Q3: name two latency sources
• Q4 trap: batching always helps, true or false
• Q5: the one-line saving for the bill shown
• Return question from Thursday: the assistant invented a policy on Tuesday only; which dial history do you check.

## Sat 21 Nov 2026 · Saturday recap · The pen-and-paper test, then the interview-answer discussion

### Business scenario of the day

Transformer internals under questioning, from Farhan's first ticket to the cost model. Build 3 opens Monday in Kalpa Connect, so today also rehearses the transfer: the same text methods, a telecom company you have not seen.

### Thinking we train, before any tool

Saying the week out loud is the interview skill itself.

### Trainer agenda

Four hours, no new content.
1. Recap test: pen and paper, AI-free, from the week's question set (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped, answers as interview answers, random call-outs (75 min).
4. Doubts and the bridge: Kalpa Connect's tickets and churn, and the AI-free debug drill named so nobody meets it cold (25 min).

### Learner outcome

CAN DO: answer the week's business and technique questions on paper.
CAN DEFEND: any answer aloud; mark a peer's paper.
STATUS: ungraded; a performance indicator.

### Subtopics (technique in service of the scenario)

THE QUESTION SET (questions only; answers built at detailing):
• [S] What is a token, and why do token counts decide cost?
• [S] Self-attention: what do queries, keys and values do?
• [S] What is an embedding, and what does similarity capture and miss?
• [F] Temperature, top-k and top-p: what does each change?
• [F] What is a context window, and what happens when it overflows?
• [F] Why did transformers replace recurrent models?
• [D] Same prompt, different outputs: reassure the stakeholder, then make it repeatable.
• [D] Estimate the monthly cost of an LLM feature: what inputs do you need?
• [D] Kalpa Connect wants churn predicted from support text; say what stays the same in your method and what changes.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper comes from this row's question set; the Academic TA leads; random call-outs.
STATUS: ungraded, AI-free by format.

### Client zero data (TRAINER ONLY)

Answers cite Farhan's tickets, counts and bills.

### In-session exercises

• The two-hour recap test.
• Peer cross-evaluation.
• Random call-outs.

### After-class tasks

• REST: Build 3 opens Monday; the briefs ship when they lock.

### Interview angle

The question set in Subtopics is the interview set for the week.

### Trainer resources

• This row's question set is the paper's source.
• Hugging Face LLM course for any gap found live (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1

### Student references

• Jay Alammar, The Illustrated Transformer, one full reread this weekend (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/

### Kahoot quiz plan

None. The recap test and discussion replace the quiz.

# W8 Transformers, LLM

## Mon 23 Nov 2026 · Attention, self-attention and the transformer block · How the model knows which 'it' the customer means

### Business scenario of the day

Farhan sends a ticket that broke the old rules-based triage: 'Ordered the charger and the case. The case arrived. It does not fit. I want to return it.' The rules flagged 'charger' as the product; the customer means the case. "How does a model know which 'it' is which?"
Your role: you walk Farhan through how a model resolves 'it' across forty tokens, and you show him one case where it will still get it wrong.
On the table: how every token consults every other; what queries, keys and values do; why several heads run at once; why word order has to be injected.

### Thinking we train, before any tool

Attention scores every token pair: each token asks a question (the query), every token offers an answer (the key), and the matching tokens contribute their content (the value). The scores pass through a softmax, so each token's weights over the others sum to one, and they are scaled down first so that long vectors do not push the softmax to its extremes. Several heads run those conversations in parallel. The mechanism is order-blind, so position is injected, which is why the room's shuffled ticket barely changes the raw scores. Attention plus a small feed-forward network, each wrapped in a skip connection and a normalisation, is one transformer block; the 2017 paper 'Attention Is All You Need' stacked six of them to read and six to write, with eight heads in each.
Farhan's 'it' is resolved by attention weight, and the case where it still fails is the case where the ticket itself is ambiguous.

### Trainer agenda

1. Farhan's broken-triage ticket; the room says which tokens 'it' should look at (10 min).
2. The lookup intuition: every token asks a question of every other (50 min).
3. Queries, keys and values named onto the intuition; scores through softmax into weights; one attention step by hand on three tokens (50 min).
4. Multi-head; positional information; the shuffled ticket; the transformer block and the six-layer stack of the 2017 paper on one diagram (45 min).
5. Guided then unguided: the attention walkthrough on the ticket, then on a second ticket, the ambiguous case found (45 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: attention scores every pair; queries ask, keys answer, values carry; softmax turns scores into weights; heads run in parallel; position is injected because the mechanism is order-blind; blocks of attention and feed-forward layers stack into the transformer.
CAN DO: walk one attention step by hand on a ticket, read a real attention pattern, and name the parts of one transformer block.
CAN HANDLE: the order-blindness surprise, and a ticket where the referent is genuinely ambiguous.
CAN DEFEND: Q, K and V in one sentence each, to Farhan and to an interviewer.

### Subtopics (technique in service of the scenario)

• The pairwise lookup intuition
• Queries, keys, values; scores through softmax into weights that sum to one
• One attention step computed by hand on three tokens
• Multi-head attention
• Positional information
• The transformer block on one diagram: attention, feed-forward, the skip connection and the normalisation named; the 2017 paper's stack of six layers to read and six to write
• The attention walkthrough on a ticket

### Trainer notes

START FROM: the long-range failure from last Thursday, and Friday's tokens; attention arrives as the fix the room already specified.
GO AS FAR AS: everyone completes the hand walkthrough on the ticket and labels one block diagram.
STOP BEFORE: deriving the scaling factor, KV caching (Friday names it), and the encoder and decoder families (Wednesday).
COMES LATER: Wednesday explains what the vectors mean and which family reads and which writes; economics Friday explains what all these pairs cost.
WHAT THE DATA REVEALS: shuffle the ticket and the raw pair scores barely move; the room asks for position by name.
CUT FIRST: the second head example. Never cut the hand walkthrough.
CALENDAR: Tuesday is Guru Nanak Jayanti, so Wednesday's pre-read ships tonight.

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
• [S] Walk me through the transformer architecture from the 2017 paper.
• [F] Why does a transformer need positional information?
• [F] Why are attention scores passed through softmax, and why are they scaled first?
• [D] A support head asks why the model got a referent wrong; explain attention and where it cannot help.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Jay Alammar, The Illustrated Transformer (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/
• Hugging Face LLM course, the transformer chapter (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• Vaswani and others, Attention Is All You Need, arXiv 1706.03762: six layers each side, eight heads, model width 512 (verified 19 Sep 2026):
https://arxiv.org/abs/1706.03762
• Hugging Face LLM course, chapter 1, How do Transformers work? (verified 19 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/4

### Student references

• Jay Alammar, The Illustrated Transformer, first half (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/

### Kahoot quiz plan

• Q1: who asks, who answers, who carries
• Q2: multi-head buys what
• Q3 trap: shuffle the ticket; what happens to raw attention and why is that a problem
• Q4: position information exists because the mechanism is what
• Q5: read the pattern: which token does 'it' attend to
• Q6: the 2017 transformer stacks how many layers on each side, with how many heads
• Return question from last Friday: the product code split into five tokens; explain it and the cost effect.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W8-1 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Attention as mathematics: scaled dot-product attention in matrix form, why the scores are divided by the square root of the key width, multi-head attention as subspaces, and the quadratic cost in sequence length.
PICKS UP WHERE THE ROW STOPS: the row does one attention step by hand and stops before deriving the scaling factor.
CONNECTS TO KALPA: Farhan's ticket and its ambiguous 'it'; Friday's cost model, where the quadratic term shows up in the bill.
BY THE END: a learner can write the attention formula, justify the scaling, and count the operations for a ticket of a given length.
DOES NOT REPEAT: the query, key and value intuition.

## Tue 24 Nov 2026 · Guru Nanak Jayanti: gazetted holiday, no session

### Business scenario of the day

No session. Guru Nanak Jayanti.

### Thinking we train, before any tool

None scheduled.

### Trainer agenda

No session; the institute is closed. Wednesday resumes on embeddings; its pre-read shipped on Monday night.

### Learner outcome

No new outcomes.

### Subtopics (technique in service of the scenario)

None scheduled.

### Trainer notes

Nothing to deliver. Tokenization moved to Friday of Week 7, so that this week keeps its four remaining topics whole.

### Client zero data (TRAINER ONLY)

The scenario rests.

### In-session exercises

None scheduled.

### After-class tasks

• OPTIONAL: redo Monday's attention step by hand on a fresh three-token ticket.

### Interview angle

None.

### Trainer resources

None needed.

### Student references

None assigned.

### Kahoot quiz plan

None.

### IITGN faculty session (TENTATIVE)

None. The institute is closed.

## Wed 25 Nov 2026 · Embeddings, with BERT against GPT · Finding the five tickets most like this one, and which model family does the finding

### Business scenario of the day

Farhan's second ask: "When a ticket comes in, find me the five past tickets most like it, so the agent sees how we solved it last time." His team tried keyword search; 'not working' and 'working fine' matched each other. Kavya adds the engineering question: "Two kinds of model came out of the same 2017 paper: one reads and one writes. Tell Farhan which kind finds his similar tickets, which kind drafts his replies, and why you cannot swap them."
Your role: you build the similar-tickets lookup on the right kind of model, show Farhan a match that is close and wrong, and explain what nearness captures and misses.
On the table: why counting words fails on 'not working' against 'working fine'; what a contextual embedding changes; why BERT reads both ways and GPT reads one way; which family serves search and which serves drafting; what a similarity score does and does not promise.

### Thinking we train, before any tool

Counting words cannot tell 'not working' from 'working fine', which is the wall the pre-read ended on, and a static word vector gives one vector per word whatever the sentence. A contextual embedding gives the same word different vectors in different sentences, and the model that produces it is an encoder: it reads the whole ticket in both directions at once. BERT is the standard example (established: Google, 2018, trained by hiding words and predicting them). A decoder reads only leftward and predicts the next token, which is what GPT does (established: OpenAI, from 2018), so it writes. The block is the same and the masking differs, which gives two jobs: encoders for search, classification and similarity, decoders for drafting, and encoder-decoder pairs for turning one text into another.
Similarity in vector space is useful and fallible: a neighbour can be close and wrong, and the room learns to read a nearest-neighbour list critically, which is the judgment the retrieval weeks live on.

### Trainer agenda

1. Farhan's ask and the keyword failure; the room says why 'not working' matched 'working fine' (10 min).
2. The classical arc recalled from the pre-read in one pass: counts, TF-IDF, static word vectors, one wall each; the TF-IDF trap run once (30 min).
3. Contextual embeddings: the same word, different vectors (40 min).
4. Encoders and decoders: BERT reads both ways, GPT writes left to right, the pair turns one text into another; which family serves which of Farhan's jobs (50 min).
5. Similarity and its limits; the close-and-wrong neighbour (35 min).
6. Guided then unguided: the similar-tickets explorer on an encoder's embeddings, five neighbours, one read critically (55 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: the field walked from counting to static vectors to contextual vectors, each fixing the previous wall; encoders read both ways and decoders write left to right; similarity is useful and fallible.
CAN DO: compute a similarity, build the similar-tickets lookup, read a neighbour list critically, and say which model family serves search, classification and drafting.
CAN HANDLE: two same-worded tickets TF-IDF cannot separate, and a neighbour that is close and wrong.
CAN DEFEND: BERT against GPT in three lines (architecture, training task, use), and what embeddings capture and miss; both return in Weeks 11 and 12.

### Subtopics (technique in service of the scenario)

• The classical arc recalled: bag of words, TF-IDF, static word vectors, one wall each
• Contextual embeddings
• Encoder-only, decoder-only and encoder-decoder models: BERT against GPT, masked-word training against next-token training
• Which family for which job: search and classification, drafting, text to text
• Similarity and its limits
• The similar-tickets explorer

### Trainer notes

START FROM: last week's pre-read carried the classical vocabulary, and Build 3's guided NLP track gives TF-IDF its hands-on hour, so the classical arc is a thirty-minute recall today and the freed time goes to encoders against decoders.
GO AS FAR AS: everyone ships the explorer with one neighbour read critically, and sorts Farhan's jobs by model family.
STOP BEFORE: training embeddings, dimensionality mathematics, fine-tuning either family.
COMES LATER: Build 3 uses TF-IDF as the no-LLM baseline; Weeks 11 and 12 live on today's similarity judgment.
WHAT THE DATA REVEALS: TF-IDF scores the opposite-meaning pair as near-identical; the contextual pair separates them; one neighbour at 0.91 is wrong. Let the room find all three.
CUT FIRST: the static-vector analogy games. Never cut the same-words trap.

### Client zero data (TRAINER ONLY)

VERSION text: the tickets table with planted same-word opposite-meaning pairs.
PLANTED: 'not working' against 'working fine'; a 0.91 neighbour that is wrong.
The explorer is the seed of the Week 11 retrieval system.
The explorer's embeddings come from a small open encoder model; the model is chosen and verified at the day build.

### In-session exercises

GUIDED: one TF-IDF score and one similarity together.
UNGUIDED: the explorer on the tickets, five neighbours for three queries, one critical note.
MID-SESSION (15 min each): sort six of Farhan's jobs into encoder, decoder or encoder-decoder; call trust-or-doubt on four similarity pairs.

### After-class tasks

• READ: The Illustrated BERT, first half.
• RECAP: encoder against decoder in two lines, with one of Farhan's jobs for each.

### Interview angle

• [S] What is an embedding, and what does similarity capture and miss?
• [S] BERT against GPT: what differs in architecture, training and use?
• [F] Static against contextual embeddings in one line.
• [F] Why can a generator not read the words to the right?
• [D] A support head trusts the similarity score; show him a 0.91 that is wrong and say what that teaches.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Jay Alammar, The Illustrated Transformer, second half (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/
• Hugging Face LLM course, the embeddings material (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• Jay Alammar, The Illustrated BERT, ELMo, and co. (verified 19 Sep 2026):
https://jalammar.github.io/illustrated-bert/
• Hugging Face LLM course, chapter 1, Transformer Architectures: encoder, decoder and sequence-to-sequence models (verified 19 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/6
• Devlin and others, BERT, arXiv 1810.04805 (verified 19 Sep 2026):
https://arxiv.org/abs/1810.04805

### Student references

• Jay Alammar, The Illustrated BERT, ELMo, and co., first half (verified 19 Sep 2026):
https://jalammar.github.io/illustrated-bert/
• Hugging Face LLM course, chapter 1, Transformer Architectures (verified 19 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/6

### Kahoot quiz plan

• Q1: TF-IDF rewards what and misses what
• Q2: static against contextual in one line
• Q3: which family embeds tickets for search, and which drafts the reply
• Q4 trap: similarity 0.91 on the pair shown; trust or doubt
• Q5: BERT hides words and predicts them; GPT predicts what
• Return question from Monday: Q, K, V, one sentence each, no notes.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W8-2 · 120 min · faculty to be confirmed by IITGN.
TOPIC: How embeddings are learned: the masked-token and next-token objectives, contrastive training of sentence encoders, and the geometry of cosine similarity in high dimensions.
PICKS UP WHERE THE ROW STOPS: the row uses an encoder's embeddings and stops before training embeddings and before dimensionality mathematics.
CONNECTS TO KALPA: the neighbour that scored 0.91 and was wrong.
BY THE END: a learner can state both training objectives, explain what a contrastive loss pulls together and pushes apart, and say why a high cosine score is weak evidence.
DOES NOT REPEAT: BERT against GPT as two jobs.

## Thu 26 Nov 2026 · Decoding controls · Making the draft reply repeatable, and stopping it inventing

### Business scenario of the day

Farhan wants the draft reply. The first prototype writes three different replies to the same ticket on three runs; one of them invents a refund policy Kalpa does not have. "I cannot put that in front of a customer. Make it say the same thing every time, and make it stop inventing."
Your role: you set the generation dials for three jobs, a summary, a field extraction and a draft reply, and you show Farhan which setting produced the invention.
On the table: why the same prompt gives different outputs; what temperature, top-k and top-p each change; when repeatability is required and how it is bought; why an output sometimes runs on until the budget dies.

### Thinking we train, before any tool

Generation samples from a probability list at every step, and the dials reshape that list: temperature flattens or sharpens it, top-k and top-p cut its tail. A support draft wants a sharp list and a fixed seed; a brainstorm wants the tail. Determinism is a setting chosen when a pipeline must be repeatable.
The invented refund policy came from a flat list; the runaway output came from a missing stop, and the room costs that runaway aloud, tying last Friday's money lesson in.

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

START FROM: auto-regression from Week 7 Thursday; every dial edits the same list.
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

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W8-3 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Decoding as search and sampling: greedy and beam search, temperature as a rescaled softmax, top-k and top-p as truncation, and the entropy of the next-token distribution.
PICKS UP WHERE THE ROW STOPS: the row moves the dials live and stops before beam search.
CONNECTS TO KALPA: the reply that invented a refund policy at a high temperature.
BY THE END: a learner can compute a softmax at two temperatures by hand, and can say when beam search helps and when it hurts.
DOES NOT REPEAT: the settings for Farhan's three jobs.

## Fri 27 Nov 2026 · Context windows and the token economy · The cost model for the auto-reply at scale

### Business scenario of the day

Two bills for the same pilot week arrive from two vendors, one five times the other. Anand wants to know why before anything scales to two thousand tickets a day. Farhan wants to know why the assistant sometimes 'forgets the beginning of the ticket'.
Your role: you build the cost model for the auto-reply at scale, find the single biggest saving, and explain the forgetting to Farhan as a budget, not a bug.
On the table: what a context window is and what falls out when it fills; why the prompt and the reply are priced differently; where the waiting happens; what batching trades away.

### Thinking we train, before any tool

The context window is a hard budget: when it fills, the oldest content falls out, and a long ticket history pushes the instructions out first, which is Farhan's 'forgetting'. Prompt tokens and completion tokens are priced differently, so an oversized system prompt dominates a bill. Latency has two named parts: the prefill pass reads the whole prompt at once and sets the time to the first token, and the decode loop writes one token at a time and sets the tokens per second; the KV cache is the memory that stops each new token from re-reading the old ones. Batching trades responsiveness for throughput.
The cost model is the week's closing artifact and the interview anchor for engineering roles: tokens per ticket, tickets per day, two price points, the biggest saving named.

### Trainer agenda

1. Two bills, five times apart; the room says what settings could do that (10 min).
2. The context window as budget; the silent overflow (45 min).
3. Prompt against completion cost; the arithmetic on Farhan's volumes (50 min).
4. Latency sources: prefill against decode, time to first token against tokens per second, the KV cache named; batching trades (35 min).
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
• Latency sources: the prefill pass and the decode loop, time to first token against tokens per second, the KV cache named
• Batching trades
• The cost model artifact

### Trainer notes

START FROM: last Friday's token arithmetic and Thursday's runaway; the module closes where it opened, on money.
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
• [F] Where does the time go in one LLM call, and which part grows with the prompt and which with the reply?
• [D] Estimate the monthly cost of an auto-reply feature for a support desk; what inputs do you need, and where is the saving?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Hugging Face LLM course, for current model-facing framing (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• Karpathy, Zero to Hero, for the internals grounding under the economics (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• Hugging Face LLM course, chapter 1, the text generation inference deep dive: prefill, decode, KV cache, time to first token (verified 19 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/8

### Student references

• Reread the week's tokenizer and cost notebooks; the numbers are the revision.

### Kahoot quiz plan

• Q1: the window fills; what falls out and what error do you get
• Q2: prompt 4,000 tokens, completion 300; where does the money go
• Q3: name two latency sources
• Q4 trap: batching always helps, true or false
• Q5: the one-line saving for the bill shown
• Return question from Thursday: the assistant invented a policy on Tuesday only; which dial history do you check.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W8-4 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Position and scale: sinusoidal and rotary position encodings, why long contexts are hard, and scaling laws at recognition depth.
PICKS UP WHERE THE ROW STOPS: the row treats the context window as a budget and names the KV cache.
CONNECTS TO KALPA: the long ticket history that pushes the instructions out of the window.
BY THE END: a learner can explain how position enters the model, why doubling the context more than doubles the work, and what a scaling law predicts. The block closes the theory that ME2 draws on.
DOES NOT REPEAT: the cost model.

## Sat 28 Nov 2026 · Saturday recap · The pen-and-paper test, then the interview-answer discussion

### Business scenario of the day

Transformer internals under questioning, from Farhan's first ticket to the cost model. Build 3 opens Monday in Kalpa Connect, so today also rehearses the transfer: the same text methods, a telecom company you have not seen.

### Thinking we train, before any tool

Saying the week out loud is the interview skill itself.

### Trainer agenda

Four hours, no new content.
1. Recap paper: pen and paper, AI-free, objective, from the 'Saturday papers' tab (120 min).
2. Break (20 min).
3. Marking: papers swapped and marked against the key, read out by the Academic TA (15 min).
4. Solution discussion led by the Academic TA: the most-missed items first, then the interview anchors answered aloud as interview answers, with random call-outs (60 min).
5. Doubts and the bridge: Kalpa Connect's tickets and churn, and the AI-free debug drill named so nobody meets it cold (25 min).

### Learner outcome

CAN DO: answer the week's business and technique questions on paper.
CAN DEFEND: any answer aloud; mark a peer's paper.
STATUS: ungraded; a performance indicator.

### Subtopics (technique in service of the scenario)

THE INTERVIEW ANCHORS (questions only):
• [S] What is a token, and why do token counts decide cost?
• [S] Self-attention: what do queries, keys and values do?
• [S] What is an embedding, and what does similarity capture and miss?
• [F] Temperature, top-k and top-p: what does each change?
• [F] What is a context window, and what happens when it overflows?
• [F] Why did transformers replace recurrent models?
• [D] Same prompt, different outputs: reassure the stakeholder, then make it repeatable.
• [D] Estimate the monthly cost of an LLM feature: what inputs do you need?
• [D] Kalpa Connect wants churn predicted from support text; say what stays the same in your method and what changes.
• [S] BERT against GPT: architecture, training and use.
• [S] Walk me through the 2017 transformer architecture.
• [F] Where does the time go in one LLM call?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: an objective paper from the 'Saturday papers' tab: fill in the blank, true or false, one correct option, more than one correct option, scenario sets, applied maths and ordering, graded easy, medium and hard. Print the Item column only; the key, tag, role and anchor columns stay with the team.
MARKING: papers swap and are marked against the key, so a score is comparable across the room and from week to week.
DISCUSSION: the Academic TA opens with the most-missed items, then asks the interview anchors aloud as interview answers, with random call-outs.
STATUS: ungraded, AI-free by format; a performance indicator.

### Client zero data (TRAINER ONLY)

Answers cite Farhan's tickets, counts and bills.

### In-session exercises

THE PAPER: objective, pen and paper, AI-free: 59 items for a 120-minute slot (119 minutes at the assumed pace); items and key in the 'Saturday papers' tab.
• Fill in the blank: 10 items
• True or false: 9 items
• One correct option: 15 items
• More than one correct option: 7 items
• Scenario sets, each on one Kalpa situation: 11 items in 3 sets
• Applied maths, with the working shown: 5 items
• Order the steps: 2 items
• Difficulty: 18 easy, 32 medium, 9 hard. Roles served: GenAI, Agentic, FDE, DS.
• Marking a peer's paper against the key.
• Random call-outs on the interview anchors: sixty seconds each.

### After-class tasks

• REST: Build 3 opens Monday; the briefs ship when they lock.

### Interview angle

The question set in Subtopics is the interview set for the week.

### Trainer resources

• The 'Saturday papers' tab holds the items and the key; this row's anchors are the source for the discussion.
• Hugging Face LLM course for any gap found live (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• llmgenai, LLM interview questions by category, a GitHub repository (verified 19 Sep 2026):
https://github.com/llmgenai/LLMInterviewQuestions
• GeeksforGeeks, advanced NLP interview questions (verified 19 Sep 2026):
https://www.geeksforgeeks.org/nlp/advanced-natural-language-processing-interview-question/

### Student references

• Jay Alammar, The Illustrated Transformer, one full reread this weekend (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/

### Kahoot quiz plan

None. The recap test and discussion replace the quiz.

### IITGN faculty session (TENTATIVE)

None. The Saturday block is the recap paper.

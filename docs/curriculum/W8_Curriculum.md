# W8 Curriculum

## Mon 16 Nov 2026 · Tokenization: subwords, vocabularies, and why tokens are money

### Trainer agenda

1. One sentence tokenized by two different tokenizers, different counts, on screen (10 min).
2. From characters to subwords: why vocabularies exist and what BPE optimises (50 min).
3. Token counts drive cost and quality: the arithmetic on real prompts (45 min).
4. Tokenizer differences across models and what they break (35 min).
5. Guided then unguided tokenizer demo on scenario text (55 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: models read tokens rather than words, BPE builds a vocabulary from frequency, and every token is billed, which makes tokenization a cost decision as well as a modelling one.
CAN DO: tokenize scenario text, count and cost it, and explain a surprising split.
CAN HANDLE: a word shattered into five tokens, and two models disagreeing on the same string's length.
CAN DEFEND: why token counts differ across models and what that does to a budget.

### Subtopics

• Characters, words, subwords
• BPE and vocabularies at intuition level
• Token counts against cost and quality
• Tokenizer differences across models
• The tokenizer demo artifact

### Trainer notes

START FROM: Friday's bridge; tokens are the atoms next-token prediction predicts, and that sentence opens the day.
GO AS FAR AS: every learner ships the tokenizer demo with one costed prompt.
STOP BEFORE: training a tokenizer, attention (tomorrow).
COMES LATER: attention Tuesday, embeddings Wednesday carrying the classical lineage, decoding Thursday, economics Friday.
BREAK TO RUN: the shattered word: a domain term splits into five tokens and the count surprises; the room explains it from vocabulary frequency rather than magic.
CUT FIRST: the second tokenizer comparison. Never cut the costing arithmetic.

### Client zero and case studies

TODAY'S DATA: the scenario's own text fields and record vocabulary; the first tokens the room ever counts are their spine's words.

### In-session exercises

GUIDED: tokenize and cost one prompt together.
UNGUIDED: the demo on three scenario texts with counts, costs and one explained surprise, solution at close.
MID-SESSION (15 min each): predict which of four strings tokenizes longest; halve a prompt's cost without losing its instruction.

### After-class tasks

• BUILD: cost the same prompt at two model price points and note the ratio.
• READ: chapter one of the Hugging Face LLM course (link in student references).
• RECAP: tokens are money, one line with a number.

### Trainer resources

• Hugging Face LLM course, chapter 1 (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• Karpathy, Zero to Hero, the tokenizer lecture (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html

### Student references

• Hugging Face LLM course, chapter 1 tonight (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1

### Kahoot quiz plan

• Q1: models read what unit
• Q2: BPE merges by what signal
• Q3: the prompt is 1,200 tokens at the price shown; cost it
• Q4 trap: same string, two models, two lengths; broken or expected
• Q5: one way to cut a prompt's tokens without cutting its meaning
• Return question from Week 7 Friday, one level up: why next-token prediction needs no labelled data, ninety seconds compressed to one line.

## Tue 17 Nov 2026 · Attention: queries, keys, values, and many heads

### Trainer agenda

1. A pronoun resolved correctly across forty tokens, on screen (10 min).
2. The lookup intuition: every token asks a question of every other (50 min).
3. Queries, keys and values named onto the intuition already built (50 min).
4. Multi-head: several conversations at once; positional information in one segment (40 min).
5. Guided then unguided attention walkthrough on a short scenario sentence (50 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: attention scores every token pair, queries ask, keys answer, values carry, and multiple heads run those conversations in parallel; position must be injected because the mechanism itself is order-blind.
CAN DO: walk one attention step by hand on a short sentence and read a real attention pattern.
CAN HANDLE: the order-blindness surprise, and a head whose pattern means nothing.
CAN DEFEND: Q, K and V in one sentence each, which is the standing interview probe.

### Subtopics

• The pairwise lookup intuition
• Queries, keys, values
• Multi-head attention
• Positional information
• The attention walkthrough artifact

### Trainer notes

START FROM: the long-range failure from Friday; attention arrives as the fix the room already specified, per application-before-theory.
GO AS FAR AS: every learner completes the hand walkthrough on the short sentence.
STOP BEFORE: the scaled dot-product formula's derivation, KV caching, architecture variants.
COMES LATER: embeddings tomorrow explain what the vectors mean; economics Friday explains what all these pairs cost.
BREAK TO RUN: order blindness: shuffle the sentence and the raw pair scores barely move; position injection is then the fix the room asks for by name.
CUT FIRST: the second head example. Never cut the hand walkthrough.

### Client zero and case studies

TODAY'S DATA: one short sentence from the scenario's world, small enough to hand-score every pair.

### In-session exercises

GUIDED: the hand walkthrough together, scores on the board.
UNGUIDED: repeat on a second sentence solo and mark which pair dominates and why, solution at close.
MID-SESSION (15 min each): match Q, K, V to their one-line jobs; predict which token attends to which in two sentences.

### After-class tasks

• READ: The Illustrated Transformer, first half (link in student references).
• RECAP: Q, K, V, one sentence each, from memory.

### Trainer resources

• Jay Alammar, The Illustrated Transformer, the visuals to borrow and redraw (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/
• Hugging Face LLM course, the transformer chapter (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1

### Student references

• Jay Alammar, The Illustrated Transformer, first half tonight (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-transformer/

### Kahoot quiz plan

• Q1: who asks, who answers, who carries
• Q2: multi-head buys what
• Q3 trap: shuffle the sentence; what happens to raw attention and why is that a problem
• Q4: position information exists because the mechanism is what
• Q5: read the pattern: which token does the pronoun attend to
• Return question from Monday, one level up: the domain term split into five tokens; explain it and name the cost effect.

## Wed 18 Nov 2026 · Embeddings and the lineage: TF-IDF to word2vec to contextual

### Trainer agenda

1. Two sentences with the same words and opposite meanings; what a bag of words misses (10 min).
2. The classical arc as a focused morning: counts, TF-IDF, static word vectors, each with its one win and one wall (75 min).
3. Contextual embeddings: the same word, different vectors in different sentences (45 min).
4. Similarity in vector space: what nearness captures and what it cannot (40 min).
5. Guided then unguided embedding explorer on scenario text (50 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: the field walked from counting words to static vectors to context-aware vectors, each step fixing the previous wall, and similarity in vector space is useful and fallible.
CAN DO: compute a similarity, read a nearest-neighbour list critically, and place the three generations on the lineage map.
CAN HANDLE: two same-worded sentences that TF-IDF cannot tell apart, and a nearest neighbour that is close and wrong.
CAN DEFEND: what embeddings capture and what they do not, which returns verbatim in the RAG weeks.

### Subtopics

• Bag of words and TF-IDF, the classical morning
• Static word vectors and their wall
• Contextual embeddings
• Similarity and its limits
• The embedding explorer artifact

### Trainer notes

START FROM: the pre-read shipped Friday seeded the classical vocabulary; the plan asks for one focused classical-NLP treatment inside this week and it runs as this morning's arc, so flag to the Programme Head if a full standalone day is wanted instead, since Friday's economics day would then compress.
GO AS FAR AS: every learner ships the explorer with one similarity read critically.
STOP BEFORE: training embeddings, dimensionality mathematics.
COMES LATER: the RAG module lives on today's similarity judgment; say so as the forward hook.
BREAK TO RUN: the same-words trap: TF-IDF scores the opposite-meaning pair as near-identical, and the contextual pair separates them; the wall and the fix in one demonstration.
CUT FIRST: the static-vector analogy games. Never cut the same-words trap.

### Client zero and case studies

TODAY'S DATA: scenario text fields and two planted same-word sentences from its world.

### In-session exercises

GUIDED: compute one TF-IDF score and one similarity together.
UNGUIDED: the explorer on scenario text with a critical note on one neighbour, solution at close.
MID-SESSION (15 min each): place six techniques on the lineage map; call trust-or-doubt on four similarity pairs.

### After-class tasks

• READ: The Illustrated Transformer, second half.
• RECAP: the three generations, one wall each.

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
• Q3 trap: similarity 0.91 on the pair shown; trust or doubt, and why
• Q4: the same word, two vectors; which generation allows it
• Q5: place three techniques on the lineage fast
• Return question from Tuesday, one level up: Q, K, V, one sentence each, no notes.

## Thu 19 Nov 2026 · Decoding: temperature, top-k, top-p, stopping, determinism

### Trainer agenda

1. The same prompt run three times with three different personalities, on screen (10 min).
2. Greedy against sampling: the probability list every token comes from (45 min).
3. Temperature, top-k and top-p, each moved live with outputs read (55 min).
4. Stopping conditions and determinism: when repeatability matters and how to buy it (40 min).
5. Guided then unguided controlled-output app on scenario prompts (50 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: generation samples from a probability list, the three dials reshape that list, and determinism is a setting you choose when a pipeline needs repeatability.
CAN DO: set the dials for a stated purpose and ship the controlled-output app.
CAN HANDLE: a temperature that turned a report into fiction, and a stop condition that never fired.
CAN DEFEND: which dial for which job, with one output as evidence.

### Subtopics

• Greedy against sampling
• Temperature
• Top-k and top-p
• Stopping conditions
• Determinism and reproducibility
• The controlled-output app

### Trainer notes

START FROM: auto-regression from Friday; every dial edits the same probability list, and that single sentence organises the day.
GO AS FAR AS: every learner ships the app with dial settings defended per use case.
STOP BEFORE: beam search, penalty parameters, provider-specific flags.
COMES LATER: the GenAI module's structured-output work assumes today's dials are owned.
BREAK TO RUN: the runaway generation: a missing stop condition pads the output until the token budget dies, and the cost of the padding is computed aloud, tying Monday's money lesson in.
CUT FIRST: top-k against top-p subtleties (state the rule of thumb). Never cut the three-personalities opener or the runaway.

### Client zero and case studies

TODAY'S DATA: scenario prompts (a summary ask, an extraction ask, a drafting ask), so each dial setting maps to a job the spine actually has.

### In-session exercises

GUIDED: move temperature live together and read three outputs.
UNGUIDED: the app with settings per use case and one sentence each of defence, solution at close.
MID-SESSION (15 min each): match five dial settings to five jobs; spot the setting that made the output shown.

### After-class tasks

• BUILD: one more use case added to the app with its settings defended.
• RECAP: the dials in one line each.

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
• Q3 trap: the extraction pipeline needs which dial profile
• Q4: the output padded to the budget; name the missing setting
• Q5: same prompt, different answers, and the stakeholder is worried; your one-line reply
• Return question from Wednesday, one level up: similarity 0.91 and wrong; what does that teach about vector nearness.

## Fri 20 Nov 2026 · Token economics: context windows, cost, latency, batching

### Trainer agenda

1. Two bills for the same workload, one five times the other; the settings did it (10 min).
2. The context window as a hard budget and what falls out when it fills (45 min).
3. Prompt cost against completion cost; the arithmetic on the scenario's workloads (50 min).
4. Latency and batching: where the waiting happens and what batching trades (40 min).
5. Guided then unguided: the cost model for one scenario workload (55 min).
6. Kahoot and week close (20 min).

### Learner outcome

UNDERSTANDS: the window is a budget, prompt and completion price differently, latency has named sources, and batching trades responsiveness for throughput.
CAN DO: build the cost model for a stated workload and find the biggest saving.
CAN HANDLE: a window overflow that silently dropped the instructions, and a bill dominated by an oversized system prompt.
CAN DEFEND: the cost model line by line, which is the week's interview anchor for engineer roles.

### Subtopics

• Context windows as budgets
• Prompt against completion cost
• Latency sources
• Batching trades
• The cost model artifact

### Trainer notes

START FROM: Monday's token arithmetic and Thursday's runaway; the week closes where it opened, on money.
GO AS FAR AS: every learner ships the cost model with one named saving.
STOP BEFORE: caching strategies and model routing, which belong to the GenAI module and are named as coming.
BREAK TO RUN: the silent overflow: the oversized context pushes the instruction out of the window and the output quality drops with no error raised, the quietest failure of the week.
CUT FIRST: the batching demo (state the trade). Never cut the overflow.

### Client zero and case studies

TODAY'S DATA: the scenario's three prompt workloads from Thursday, costed end to end; the cost model is the module's closing artifact.

### In-session exercises

GUIDED: cost one workload together, prompt and completion separated.
UNGUIDED: the full cost model with the single biggest saving named, solution at close.
MID-SESSION (15 min each): find the saving in three billed examples; predict what the overflow drops first.

### After-class tasks

• BUILD: recost the workload at a second model price point.
• RECAP: the week in five lines, one per day.
• PREP: tomorrow's block is the week under questioning; Build 3 opens Monday.

### Trainer resources

• Hugging Face LLM course, for current model-facing framing (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• Karpathy, Zero to Hero, for the internals grounding under the economics (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html

### Student references

• Reread the week's tokenizer and cost notebooks; the numbers are the revision.

### Kahoot quiz plan

• Q1: the window fills; what falls out and what error do you get
• Q2: prompt 4,000 tokens, completion 300; where does the money go at the prices shown
• Q3: name two latency sources
• Q4 trap: batching always helps, true or false, and the trade
• Q5: the one-line saving for the bill shown
• Return question from Thursday, one level up: the report pipeline hallucinated on Tuesday only; which dial history do you check.

## Sat 21 Nov 2026 · Saturday recap: the pen-and-paper test, then the interview-answer discussion

### Trainer agenda

Four hours, no new content.
1. Weekly recap test: pen and paper, AI-free, built from the week's interview question set, short-answer format (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped for peer cross-evaluation, every answer discussed as an interview answer, random call-outs throughout (75 min).
4. Doubt clearing and the bridge: Build 3 opens Monday; the AI-free debug drill is named so nobody meets it cold (25 min).

### Learner outcome

CAN DO: answer the week's interview set on paper, without an assistant, in short-answer form.
CAN DEFEND: any of those answers aloud when called, and mark a peer's paper against the discussed solution.
STATUS: ungraded; the score is a performance indicator the programme reads, never a marks component.

### Subtopics

THE QUESTION SET (questions only; answers are built at the detailing phase):
• [S] What is a token, and why do token counts decide cost?
• [S] Self-attention: what do queries, keys and values each do?
• [F] Why did transformers replace recurrent models?
• [S] What is an embedding, and what does similarity capture and miss?
• [F] Temperature, top-k and top-p: what does each dial change?
• [F] What is a context window, and what happens when it overflows?
• [D] Same prompt, different outputs: reassure the stakeholder, then make it repeatable.
• [D] Estimate the monthly cost of an LLM feature: what inputs do you need?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. The tagging is this programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper is built from this row's question set, framed for short answers (selection, one-liners, small computations) so peer cross-checking works; answers themselves are written at the detailing phase, never improvised on the day.
DISCUSSION: papers swap for peer cross-evaluation; the Academic TA leads the solution walk-through as an interview-answer discussion, with random call-outs throughout.
STATUS: ungraded, a performance indicator rather than a marks component, and AI-free by format.

### Client zero and case studies

Answers must cite the scenario's own numbers and artifacts where the week produced them; the transformer pipeline and the cost model are the reference.

### In-session exercises

• The two-hour recap test on paper.
• Peer cross-evaluation against the discussed solution.
• Random call-outs: the called learner answers aloud in sixty seconds.

### After-class tasks

• RECAP: rewrite any question you lost marks on, one line each, in your own words.

### Trainer resources

• This row's question set is the paper's source; the verified interview banks on the weekday rows calibrate difficulty.
• GeeksforGeeks, Data Analyst interview questions (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/

### Student references

• Reread the week's tabs and your own rejected answers; the next paper reuses missed ground one level up.

### Kahoot quiz plan

None. The recap test and the discussion replace the quiz today.

# W11 RAG

## Mon 14 Dec 2026 · Chunking trade-offs · The first retrieval pipeline, and how the documents are cut

### Business scenario of the day

THE WEEK. Farhan's assistant can draft, file and look an order up. It still cannot answer the commonest question on his desk, which is 'am I allowed to return this?' The answer lives in Kalpa's own documents: the returns and refunds policy, the delivery terms, the support playbook and the product manuals. The week builds the system that finds the right passage, answers from it, shows it, and says so when the documents are silent. Build 4 next week repeats the whole exercise in Kalpa Logistics.

MONDAY. Farhan: "A customer asks whether an opened blender can go back after twelve days. My best agent finds the clause in under a minute. Your assistant answered in two seconds and was wrong." Two quick fixes were tried before the team called you. Pasting every policy into the prompt ran into Week 8's overflow and Anand's bill. Searching the documents first worked until the answer needed two sentences that the splitter had put into different pieces.
Your role: you build the first version end to end, and then you decide how the documents are cut, because every later step inherits that cut.
On the table: what 'find first, then answer' looks like as a pipeline; how big a piece should be; what is lost when a rule and its exception land in different pieces; what the documents' own structure offers; how a cut is tested before it is trusted.

### Thinking we train, before any tool

Retrieval-augmented generation (established: Lewis and others, 2020) is one idea: find the evidence first, then answer only from it, and show it. The thin version runs before anything is tuned: cut the documents into pieces, embed each piece, store the vectors, embed the question, take the nearest pieces, and hand them to the model with the instruction to answer from them alone. It is Week 8 Wednesday's similar-tickets explorer pointed at policies.
The cut decides what can ever be found. A small piece matches a question sharply and loses the condition attached to the rule, so 'opened appliances are not eligible' arrives without 'unless defective'. A large piece keeps the condition and dilutes the match, and it spends the token budget on text nobody asked about. Overlap repairs some boundary losses and duplicates text. A policy's own structure of sections, clauses and tables is usually the most honest boundary. The cut is an experiment with a score, and it is never a default left untouched.

### Trainer agenda

1. Farhan's blender question; the room finds the clause by hand and times it (10 min).
2. The thin pipeline end to end on the returns policy: cut, embed, store, retrieve, answer from the pieces alone (50 min).
3. What the cut did: the rule and its exception in different pieces, and the wrong answer read aloud (30 min).
4. Size and overlap as dials: three sizes and two overlaps on ten questions, scored by whether the needed passage came back (45 min).
5. Structure-aware cutting: sections, clauses and one table; what each extreme breaks (35 min).
6. Guided then unguided: the chunking experiment on the full corpus, the chosen cut and the evidence for it (50 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: retrieval-augmented generation finds the evidence before it answers; the cut decides what can be found; size and overlap trade sharp matching against kept context; a document's structure is the most honest boundary.
CAN DO: build a thin retrieve-then-answer pipeline, cut a corpus three ways, score each cut on a question set, and choose one with evidence.
CAN HANDLE: a rule split from its exception, a table flattened into nonsense, and a piece so large that the answer drowns in it.
CAN DEFEND: the chosen size, overlap and boundaries, with the ten-question score behind them.

### Subtopics (technique in service of the scenario)

• Retrieve, then answer from the evidence alone: the thin pipeline
• Chunk size: sharp matching against kept context
• Overlap: what it repairs and what it duplicates
• Structure-aware splitting: sections, clauses, tables
• What breaks at each extreme
• The chunking experiment: a question set and a score

### Trainer notes

START FROM: Week 8 Wednesday's embeddings explorer and Friday's context budget; Week 10's prompt and evaluation habits. The pipeline is new and none of its parts is.
GO AS FAR AS: everyone has a working thin pipeline and a chunking experiment with a chosen cut.
STOP BEFORE: choosing the embedding model and the store (Tuesday), hybrid search and reranking (Wednesday), formal retrieval metrics (Thursday), citations (Friday). Today's score is simply whether the needed passage came back.
COMES LATER: every later day this week changes one stage and keeps this pipeline.
FIRST-USE TOOLS: a vector column in the course Postgres (pgvector is proposed, since it keeps the environment to one database, and it is verified at the day build) and the small open embedding model carried over from Week 8.
WHAT THE DATA REVEALS: at the smallest size the assistant tells the customer that an opened blender cannot go back, because the exception for defective items sits in the next piece; at the largest size the right section comes back fourth, behind three long pieces about delivery. The clause-level cut wins on the ten questions.
CUT FIRST: the table example shrinks to a demonstration. Never cut the split rule and exception.

### Client zero data (TRAINER ONLY)

VERSION corpus (client zero v2.2): the returns and refunds policy, the delivery terms, the support playbook, the product manuals and anonymised tickets.
PLANTED (v2.2): two documents that contradict on one clause; a question the corpus cannot answer; a manual that uses a term found nowhere else. None of the three is used today.
PROPOSED FOR v2.3 (21 Sep 2026, not yet locked): in the returns policy a rule and its exception sit in adjacent sentences, so that a small fixed-size cut separates them. Students are never told what is planted.

### In-session exercises

GUIDED: the thin pipeline built together on one document.
UNGUIDED: the chunking experiment on the full corpus with three sizes, two overlaps and one structure-aware cut; the chosen cut with its score.
MID-SESSION (15 min each): mark on a printed policy page where you would cut and why; predict for four questions which cut size will fail.

### After-class tasks

• BUILD: write five more questions for the question set from the delivery terms, each with the passage that answers it.
• WATCH: IBM Technology, What is Retrieval-Augmented Generation.
• READ: Pinecone, Chunking Strategies for LLM Applications.
• SETUP: nothing to install for Tuesday.

### Interview angle

• [S] What is RAG, and why use it over fine-tuning or a longer prompt?
• [S] How do you choose a chunk size?
• [F] What is chunk overlap for, and what does it cost?
• [F] How would you chunk a document that is mostly tables?
• [D] Your assistant gave a customer half of a rule; walk me from the symptom back to the cause.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Lewis and others, Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, 2020 (verified 21 Sep 2026):
https://arxiv.org/abs/2005.11401
• Pinecone, Chunking Strategies for LLM Applications (verified 21 Sep 2026):
https://www.pinecone.io/learn/chunking-strategies/
• Chroma Research, Evaluating Chunking Strategies for Retrieval (verified 21 Sep 2026):
https://www.trychroma.com/research/evaluating-chunking
• pgvector, open-source vector similarity search for Postgres (verified 21 Sep 2026):
https://github.com/pgvector/pgvector

### Student references

• IBM Technology, What is Retrieval-Augmented Generation (RAG)? (verified 21 Sep 2026):
https://www.youtube.com/watch?v=T-D1OfcDW1M
• Pinecone, Chunking Strategies for LLM Applications (verified 21 Sep 2026):
https://www.pinecone.io/learn/chunking-strategies/

### Kahoot quiz plan

• Q1: order the six steps of the thin pipeline
• Q2: the answer dropped the exception; which dial do you suspect first
• Q3 trap: bigger pieces always help because they keep more context, true or false
• Q4: what overlap repairs, in one line
• Q5: where would you cut this clause: three options shown
• Return question from Week 8 Wednesday: a neighbour scored 0.91 and was wrong; what does similarity promise.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W11-1 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Information retrieval foundations: the vector space model, term weighting with TF-IDF, and BM25, with the reason each term in the formula is there.
PICKS UP WHERE THE ROW STOPS: the row builds the thin pipeline and treats search as given.
CONNECTS TO KALPA: Week 8's TF-IDF wall, and Wednesday's keyword search for product codes.
BY THE END: a learner can score three documents against a query by hand with TF-IDF, and can explain what BM25's length normalisation and saturation do.
DOES NOT REPEAT: the chunking experiment.

## Tue 15 Dec 2026 · Embedding and vector store choice · Where the vectors live, and who refreshes them

### Business scenario of the day

TUESDAY. The data platform lead reviews Monday's prototype. "Three questions before this goes near production. Where do the vectors live, and is it somewhere I already run? Who refreshes them when Legal changes a policy? And can I ask for delivery terms only, in force today?" Farhan adds a fourth: half his customers write in a mix of Hindi and English, and the prototype's search has been tested only on tidy English questions.
Your role: you choose the embedding model on Kalpa's own questions, choose where the index lives, and show that a changed policy is never answered from its old text.
On the table: how embedding models differ and how a choice is tested; what a vector store does beyond holding a list of vectors; what metadata makes filterable; what happens to the index when a document changes; what a managed cloud retrieval service takes off your hands and what it takes out of them.

### Thinking we train, before any tool

An embedding model is chosen on the questions the business actually gets. A public leaderboard ranks models on other people's data, and ten of Farhan's real questions, the mixed-language ones included, rank them on his. The properties that matter are the text a model was trained on, the length of input it accepts and the width of its vectors, since width is storage and speed.
A vector store is a database with one extra ability: it finds the nearest vectors fast, exactly on a small collection and approximately on a large one, where an index such as HNSW trades a little recall for a lot of speed (established: Malkov and Yashunin, 2016). Everything else is ordinary data engineering. Each piece carries metadata (document, section, type, effective date) so that a search can be filtered before it is ranked. A refresh rule replaces a document's pieces when the document changes, and the old pieces must be gone, because an assistant that cites a superseded clause is worse than one that says nothing. The same index is then set beside one managed cloud retrieval service and compared on setup effort, control, filtering and cost, which is the build-or-buy judgment Week 16 returns to.

### Trainer agenda

1. The platform lead's three questions and Farhan's fourth; the room says which of them Monday's prototype fails (10 min).
2. Choosing the embedding model: two candidates scored on ten real questions, the mixed-language ones included (45 min).
3. The store: a vector column beside the text, the distance operator, exact search, then an approximate index and what it trades (40 min).
4. Metadata and filtering: document type and effective date; filter first, rank second (35 min).
5. Refresh: a policy changes; the stale piece that still answers; the replace-by-document rule (35 min).
6. One managed cloud retrieval service beside the self-built index: effort, control, filtering, cost (25 min).
7. Guided then unguided: the working index with metadata, a refresh script and the comparison note (30 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: an embedding model is chosen on the business's own questions; a vector store is a database with fast nearest-neighbour search; metadata makes a search filterable; an index needs a refresh rule; managed and self-built are compared on stated measures.
CAN DO: score two embedding models on a question set, build a vector index with metadata in Postgres, filter before ranking, refresh a changed document, and write a build-or-buy comparison.
CAN HANDLE: a model that fails on mixed-language questions, a superseded clause that still comes back, and an approximate index that misses a passage exact search finds.
CAN DEFEND: the embedding model, the store and the refresh rule, each with its evidence.

### Subtopics (technique in service of the scenario)

• Choosing an embedding model on your own questions: training text, input length, vector width
• The vector store: vectors beside text, distance, exact against approximate search
• The approximate index at recognition depth, and what it trades
• Metadata and filtering: filter first, rank second
• Index refresh: replace by document; the stale piece
• One managed cloud retrieval service compared with the self-built index

### Trainer notes

START FROM: Monday's pipeline and its chosen cut; the Postgres the room has used since Week 2.
GO AS FAR AS: everyone ships an index with metadata, a refresh script that leaves no stale piece, and a one-page comparison with a managed service.
STOP BEFORE: how an approximate index works inside, quantisation, sharding, multi-tenant design.
COMES LATER: Wednesday adds keyword search beside the vectors; Week 16 Wednesday returns to build-or-buy, component by component.
FIRST-USE TOOLS: the managed retrieval service is one product chosen at the day build from the approved cloud credits, which are not yet decided; this row names no vendor.
WHAT THE DATA REVEALS: the model that leads on tidy English questions drops on the mixed-language ones; after the policy file changes, the old clause still answers until the refresh replaces it; the manual's own term, which appears nowhere else in the corpus, is missed by both models and stays missed until Wednesday.
CUT FIRST: the managed-service comparison shrinks to a read-through of its documentation. Never cut the stale piece.

### Client zero data (TRAINER ONLY)

VERSION corpus (v2.2), with effective dates and document types as metadata.
PLANTED (v2.2): the manual that uses a term found nowhere else, which vector search misses today and keyword search finds on Wednesday.
PROPOSED FOR v2.3 (21 Sep 2026, not yet locked): a second, later version of one policy document, so that a refresh can be tested; ten customer questions in the style of real tickets, four of which mix Hindi and English. Students are never told what is planted.

### In-session exercises

GUIDED: the two models scored on five questions; the index built with metadata.
UNGUIDED: the full ten-question comparison, the filter, the refresh script, the comparison note.
MID-SESSION (15 min each): for six searches, say which metadata filter should run first; read a results list before and after a refresh and spot the stale piece.

### After-class tasks

• BUILD: add a 'document owner' field to the metadata and one query that uses it.
• READ: the pgvector README, the sections on indexes and on distance.
• SETUP: Wednesday's reranking model downloads from the setup cell; the instructions ship tonight.

### Interview angle

• [S] What is a vector database, and how does it differ from an ordinary one?
• [S] How do you choose an embedding model?
• [F] How do you keep a RAG index up to date when the documents change?
• [F] Why filter on metadata before the similarity search?
• [D] Your retrieval works in the demo and fails for half of real customers, who write in two languages at once; what do you test, and what do you change?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• pgvector, open-source vector similarity search for Postgres: HNSW and IVFFlat indexes, cosine and other distances (verified 21 Sep 2026):
https://github.com/pgvector/pgvector
• MTEB Leaderboard on Hugging Face, for shortlisting embedding models and never for the final choice (verified 21 Sep 2026):
https://huggingface.co/spaces/mteb/leaderboard
• Sentence Transformers documentation (verified 21 Sep 2026):
https://sbert.net/
• Malkov and Yashunin, the HNSW paper on approximate nearest neighbour search with Hierarchical Navigable Small World graphs, 2016 (verified 21 Sep 2026):
https://arxiv.org/abs/1603.09320

### Student references

• Pinecone, What is a Vector Database and How Does it Work? (verified 21 Sep 2026):
https://www.pinecone.io/learn/vector-database/

### Kahoot quiz plan

• Q1: leaderboard or your own questions: which decides the embedding model, and why
• Q2: exact or approximate search: what does each trade
• Q3 trap: after a policy changes, adding the new pieces is enough, true or false
• Q4: filter first or rank first, for 'delivery terms in force today'
• Q5: managed or self-built: two measures that favour each
• Return question from Monday: the answer dropped the exception; which dial did it.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W11-2 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Nearest neighbours at scale: exact against approximate search, the navigable small-world graph index and the inverted-file index, product quantisation at recognition depth, and the trade between recall and latency.
PICKS UP WHERE THE ROW STOPS: the row uses an approximate index and stops before how it works inside.
CONNECTS TO KALPA: the passage that exact search finds and the approximate index misses.
BY THE END: a learner can explain how a graph index finds a neighbour without comparing everything, and can name the settings that trade recall for speed.
DOES NOT REPEAT: the choice of store and the refresh rule.

## Wed 16 Dec 2026 · Hybrid search and reranking · Exact codes, loose questions, and the right five pieces

### Business scenario of the day

WEDNESDAY. Farhan's agents try the assistant on real tickets and send back two kinds of failure. A customer quotes a product code from the box, and the search returns blenders in general and never that model's manual. Another asks a loose question, 'can I send it back?', after three messages about a damaged kettle, and the search returns the policy for change-of-mind returns. Kavya: "Meaning search reads the gist and drops the exact word. Keyword search does the reverse. Use both, then let something read each candidate properly before the model sees it."
Your role: you raise retrieval quality on the failing tickets without breaking last Friday's two-second budget.
On the table: why vectors miss exact codes and rare terms; what keyword search adds and what it misses; how two ranked lists are combined; what a reranker does that the first search cannot afford to do; how a vague follow-up becomes a searchable question; how many pieces the model should be shown.

### Thinking we train, before any tool

Dense retrieval matches meaning and blurs exact tokens: a product code shatters into sub-tokens, as Week 7 Friday showed, and its vector sits near every other code. Sparse retrieval (BM25, established in information retrieval since the 1990s) matches the exact term and misses a paraphrase. Hybrid search runs both and fuses the two ranked lists, and reciprocal rank fusion does so from ranks alone, so that no scores need calibrating (established: Cormack and others, 2009).
Retrieval then runs in two stages, because reading carefully is expensive. The first stage is cheap and wide, about fifty candidates. The second is a reranker, a model that reads the question and one piece together and scores the pair, which the first stage could never afford across a whole corpus. The best five go to the model. A vague follow-up is rewritten into a standalone question before any search runs. How many pieces to show is a budget decision with a quality side, read on the three numbers from Week 10 Friday.

### Trainer agenda

1. The two failing tickets; the room predicts which kind of search finds each (10 min).
2. Keyword search beside the vectors: BM25 over the same pieces, and the product code found (40 min).
3. Fusing two ranked lists with reciprocal rank fusion, by hand on five results and then in code (35 min).
4. The reranker: fifty in, five out; what it fixes and what it adds to latency (45 min).
5. Query rewriting: the vague follow-up turned into a standalone question (30 min).
6. How many pieces: three, five and ten, read on cost, latency and answer quality (20 min).
7. Guided then unguided: the retrieval upgrade measured against Tuesday's index on the failing tickets (40 min).
8. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: dense search matches meaning and sparse search matches terms; hybrid search fuses both by rank; a reranker reads the question and the piece together; retrieval runs cheap and wide, then careful and narrow.
CAN DO: add keyword search, fuse two ranked lists, add a reranking stage, rewrite a follow-up into a standalone question, and choose how many pieces to pass on.
CAN HANDLE: a product code that vectors cannot find, a reranker that breaks the latency budget, and a rewritten query that drifts from what the customer meant.
CAN DEFEND: each stage added, with the tickets it fixed and the milliseconds it cost.

### Subtopics (technique in service of the scenario)

• Dense against sparse retrieval: what each finds and misses
• BM25 keyword search over the same pieces
• Hybrid search and reciprocal rank fusion
• Two-stage retrieval: wide and cheap, then a reranker
• Bi-encoder against cross-encoder, at recognition depth
• Query rewriting for follow-ups
• Top-k as a budget decision

### Trainer notes

START FROM: Tuesday's index; Week 7 Friday's shattered product codes and Week 8 Wednesday's TF-IDF recall.
GO AS FAR AS: everyone ships hybrid retrieval with a reranker and a rewriting step, and a before-and-after table on the failing tickets.
STOP BEFORE: training or fine-tuning a reranker, learned sparse models, and query expansion by generating a hypothetical answer, which is named only.
COMES LATER: Thursday scores today's gains properly, the search apart from the answer.
WHAT THE DATA REVEALS: the manual's own term and the product code are found by keyword search and missed by vectors; the reranker lifts the right clause from ninth to first and adds enough latency at fifty candidates to break the two-second budget, so the room has to find the candidate count that fits.
SECOND EXAMPLE: Dr Priya Menon's test catalogue at Kalpa Health, where a test code must match exactly and a described symptom must match by meaning.
CUT FIRST: the top-k comparison shrinks to two settings. Never cut the latency measurement on the reranker.

### Client zero data (TRAINER ONLY)

VERSION corpus (v2.2) with Tuesday's index.
PLANTED (v2.2): the manual that uses a term found nowhere else, which keyword search finds today.
PROPOSED FOR v2.3 (21 Sep 2026, not yet locked): a set of failing tickets, some quoting a product code and some asking a vague follow-up inside a longer conversation. Students are never told what is planted.

### In-session exercises

GUIDED: keyword search added; one fusion worked by hand.
UNGUIDED: the fused search in code, the reranker with its latency measured, the rewriting step, the before-and-after table.
MID-SESSION (15 min each): fuse two five-item ranked lists by hand; rewrite four follow-up messages as standalone questions.

### After-class tasks

• BUILD: find the candidate count at which the reranker fits the two-second budget, and note what it cost in quality.
• READ: Pinecone, Rerankers and Two-Stage Retrieval.
• RECAP: what dense search misses and what sparse search misses, one line each.

### Interview angle

• [S] What is hybrid search, and why combine keyword and vector search?
• [S] What does a reranker do, and why not rerank the whole corpus?
• [F] How does reciprocal rank fusion combine two result lists?
• [F] A user asks 'can I send it back?' in the middle of a chat; how does your retriever know what 'it' is?
• [D] Reranking improved quality and doubled latency; how do you decide whether it ships?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Pinecone, Rerankers and Two-Stage Retrieval (verified 21 Sep 2026):
https://www.pinecone.io/learn/series/rag/rerankers/
• Sentence Transformers, Retrieve and Re-Rank (verified 21 Sep 2026):
https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html
• Manning, Raghavan and Schütze, Introduction to Information Retrieval, Okapi BM25 (verified 21 Sep 2026):
https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html
• Cormack, Clarke and Büttcher, Reciprocal Rank Fusion, SIGIR 2009 (verified 21 Sep 2026):
https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf
• Anthropic Engineering, Contextual Retrieval, for measured gains from hybrid search and reranking (verified 21 Sep 2026):
https://www.anthropic.com/engineering/contextual-retrieval

### Student references

• Pinecone, Getting Started with Hybrid Search (verified 21 Sep 2026):
https://www.pinecone.io/learn/hybrid-search-intro/
• Pinecone, Rerankers and Two-Stage Retrieval (verified 21 Sep 2026):
https://www.pinecone.io/learn/series/rag/rerankers/

### Kahoot quiz plan

• Q1: dense or sparse: which finds each of five queries
• Q2: fuse these two ranked lists; which piece comes first
• Q3 trap: rerank the whole corpus for the best quality, true or false
• Q4: the follow-up says 'it'; what runs before the search
• Q5: reranking added latency; name two ways to get it back
• Return question from Tuesday: the policy changed and the old clause still answered; what was missing.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W11-3 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Ranking as a learning problem: bi-encoders against cross-encoders, how a reranker is trained, and rank fusion as a voting rule.
PICKS UP WHERE THE ROW STOPS: the row uses a reranker and stops before training one, and before learned sparse models.
CONNECTS TO KALPA: the clause lifted from ninth place to first, and the latency it cost.
BY THE END: a learner can explain why a cross-encoder is more accurate and slower, what training pairs it needs, and why fusion by rank needs no score calibration.
DOES NOT REPEAT: the hybrid pipeline.

## Thu 17 Dec 2026 · RAG evaluation · Was it the search or the model?

### Business scenario of the day

THURSDAY. Farhan's quality lead forwards a wrong answer about delivery charges. "Was it the search or the model? I need to know whom to ask for the fix." Anand wants one page before go-live: how often it is right, how often it is wrong, and how often it says it does not know. The team has an end-to-end accuracy of 82 percent on a hand-checked sample, and Kavya does not trust it: "A model can answer correctly from its own memory while your search returns rubbish. That is luck, and luck does not survive a policy change."
Your role: you build the harness that scores the search and the answer separately, and you tell the quality lead which stage owns each failure.
On the table: what a golden set for retrieval contains; how the search is scored without the model; how the answer is scored against what was retrieved; what a right answer on wrong evidence means; what the unanswerable questions are for.

### Thinking we train, before any tool

A retrieval system has two stages, so it gets two scorecards. The search is scored alone, against a golden set of questions that each name the pieces that answer them. Recall at k asks whether the needed piece came back in the top k, precision at k asks how much of what came back was needed, and the reciprocal rank rewards finding it early. The answer is scored against what was retrieved. Faithfulness asks whether every claim in the answer is supported by the retrieved pieces, and relevance asks whether the answer addresses the question. Both use Week 10 Thursday's graders, code first and a checked judge second.
The two scorecards make a diagnosis table, which is this course's construction. Right pieces with a wrong answer is a generation fault. Wrong pieces with a wrong answer is a retrieval fault. Wrong pieces with a right answer is luck, and it is counted as a failure. The golden set includes questions the corpus cannot answer, because 'I do not know' has to be scored as well.

### Trainer agenda

1. The wrong answer about delivery charges; the room votes search or model before looking (10 min).
2. The golden set for retrieval: the questions, the pieces that answer each, and the unanswerable ones (40 min).
3. Scoring the search alone: recall at k, precision at k and reciprocal rank, by hand on three questions and then in code (45 min).
4. Scoring the answer against the evidence: faithfulness and relevance with Week 10's graders (40 min).
5. The diagnosis table: every failure assigned to a stage; the right answer on wrong evidence (30 min).
6. Guided then unguided: the harness run on Wednesday's system, and the one-page report for Anand (55 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: the search and the answer are scored separately; a right answer on wrong evidence is a failure; unanswerable questions belong in the golden set.
CAN DO: build a retrieval golden set, compute recall at k, precision at k and reciprocal rank, grade faithfulness and relevance, fill the diagnosis table, and report three rates to Finance.
CAN HANDLE: an end-to-end accuracy that hides weak retrieval, a judge that marks an unsupported claim as faithful, and a stakeholder who wants one number.
CAN DEFEND: which stage owns each failure, and why 82 percent was the wrong number to trust.

### Subtopics (technique in service of the scenario)

• Two stages, two scorecards
• The retrieval golden set: questions, answering pieces, unanswerable questions
• Recall at k, precision at k, reciprocal rank
• Faithfulness and answer relevance, graded against the retrieved pieces
• The diagnosis table (course construction): generation fault, retrieval fault, luck
• The report: right, wrong, and 'I do not know'

### Trainer notes

START FROM: Week 10 Thursday's suite and graders; Wednesday's upgraded retrieval. Only the retrieval scorecard is new.
GO AS FAR AS: everyone ships a harness with both scorecards over at least twenty-five questions and the one-page report.
STOP BEFORE: graded relevance and nDCG, statistical tests between two systems, online evaluation with live users.
COMES LATER: Build 4 requires these numbers in every group's report; Week 16 Friday puts the harness into the release pipeline.
NAMING: the plan's 'answer relevance' appears in the Ragas documentation as response relevancy; the idea is the same.
WHAT THE DATA REVEALS: end-to-end accuracy reads 82 percent while recall at five is far lower, so a share of the right answers rest on the model's own memory, and faithfulness exposes them; the delivery-charge failure is a retrieval fault; the unanswerable question is answered with confidence, which Friday fixes.
CUT FIRST: precision at k shrinks to a definition and one example. Never cut the right answer on wrong evidence.

### Client zero data (TRAINER ONLY)

VERSION corpus (v2.2) with Wednesday's retrieval.
PLANTED (v2.2): a question the corpus cannot answer, which the assistant answers anyway today.
PROPOSED FOR v2.3 (21 Sep 2026, not yet locked): a golden set in which several questions can be answered correctly from general knowledge while the needed piece is absent from the top five; the 82 percent figure in the scenario. Students are never told what is planted.

### In-session exercises

GUIDED: five golden questions written together; recall at five computed by hand.
UNGUIDED: the full harness, the diagnosis table filled for every failure, the report for Anand.
MID-SESSION (15 min each): compute recall and precision at three for four result lists; assign six failures to search, model or luck.

### After-class tasks

• BUILD: add five unanswerable questions to the golden set and record what the assistant does with each.
• READ: the Ragas documentation, the list of available metrics, the retrieval-augmented generation group.
• RECAP: the three rows of the diagnosis table from memory.

### Interview angle

• [S] How do you evaluate a RAG system?
• [S] Precision at k and recall at k: define each, and say which matters more for a support assistant.
• [F] What is faithfulness, and how is it different from correctness?
• [F] How do you build a golden set when nobody has labelled anything?
• [D] Your RAG system scores 82 percent end to end and retrieval recall is poor; explain how both can be true, and why it matters.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Ragas documentation, List of available metrics: context precision, context recall, response relevancy, faithfulness (verified 21 Sep 2026):
https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
• Es and others, Ragas: Automated Evaluation of Retrieval Augmented Generation, 2023 (verified 21 Sep 2026):
https://arxiv.org/abs/2309.15217
• Manning, Raghavan and Schütze, Introduction to Information Retrieval, Evaluation of ranked retrieval results (verified 21 Sep 2026):
https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html

### Student references

• Ragas documentation, List of available metrics (verified 21 Sep 2026):
https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/

### Kahoot quiz plan

• Q1: compute recall at three from the list shown
• Q2: faithful or correct: four answers sorted
• Q3 trap: the answer was right, so retrieval worked, true or false
• Q4: right pieces, wrong answer; which stage owns it
• Q5: why the golden set holds questions with no answer
• Return question from Wednesday: what a reranker reads that the first search does not.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W11-4 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Measuring ranked retrieval: precision and recall at k, mean reciprocal rank, nDCG with graded relevance, and when a difference between two systems is real.
PICKS UP WHERE THE ROW STOPS: the row stops before graded relevance, nDCG and statistical tests between two systems.
CONNECTS TO KALPA: Wednesday's before-and-after table, tested for whether the gain is more than noise.
BY THE END: a learner can compute nDCG for a short list by hand, and can test the difference between two systems on a shared question set.
DOES NOT REPEAT: the two scorecards and the diagnosis table.

## Fri 18 Dec 2026 · Citations and grounding · Show the clause, say when the documents are silent, and catalogue the failures

### Business scenario of the day

FRIDAY. The assistant promised a customer a free return pickup, and the warehouse charged her for it. Farhan traces it: the support playbook says pickup is free, the returns policy says a fee applies, and the assistant quoted the playbook with total confidence. Anand sets the rule for go-live: "Every answer a customer sees shows the clause it came from. If our documents do not cover it, it says so and hands over. If our documents disagree, I want to know before the customer does."
Your role: you make every answer carry its sources, make the assistant decline when the evidence is missing, surface the contradiction, and close the week with the catalogue of ways this system fails.
On the table: how a citation is produced and how code checks it; when the assistant must say it does not know; what to do when two documents disagree; what goes stale; when a long context window is a fair alternative to retrieval, and what it costs.

### Thinking we train, before any tool

Grounding is enforced in three places. The answer cites the pieces it used by their ids, and code checks that each cited piece exists, was retrieved for this question, and contains the words the sentence leans on; a citation that fails the check makes the answer a failed answer. The assistant declines when the best retrieval score is under a threshold or when the pieces do not contain the answer, and the decline hands over to a person with the question attached. When retrieved pieces disagree, the assistant says so, prefers the document with the authority and the later effective date, and raises the conflict to the document's owner.
A system like this fails in a small number of known ways (established: Barnett and others, 2024, name seven): the content is missing, the right piece is ranked too low, the piece is retrieved and then ignored, the answer is right and incomplete, and so on. The week closes by writing that catalogue for Kalpa, with the check that catches each. Pasting whole documents into a long context window is a fair alternative for a small and stable corpus; its bill follows Week 8 Friday's arithmetic, and models use the middle of a long context less well than its ends (established: Liu and others, 2023).

### Trainer agenda

1. The free pickup that was charged; the room finds the two clauses (10 min).
2. Citations: piece ids in the answer, and the code check that each citation exists, was retrieved and supports its sentence (45 min).
3. Declining: the threshold, the instruction and the hand-over; the unanswerable question answered from nowhere, with a clause number that does not exist (40 min).
4. Conflicting sources: surfaced, ranked by authority and effective date, raised to the owner (30 min).
5. Long context as the alternative: the whole returns policy in the prompt, costed, with the buried clause missed (30 min).
6. Guided then unguided: the cited assistant, and the failure catalogue for Kalpa with one check per failure (65 min).
7. Kahoot and week close (20 min).

### Learner outcome

UNDERSTANDS: a citation is checked by code; declining is a designed behaviour; conflicting documents are surfaced and escalated; a retrieval system fails in a small number of known ways; long context is an alternative with a bill.
CAN DO: produce and verify citations, set a decline rule with a hand-over, detect and rank conflicting pieces, cost the long-context alternative, and write a failure catalogue with a check per failure.
CAN HANDLE: a citation to a section that does not exist, a confident answer to an unanswerable question, two documents that disagree, and a clause missed in the middle of a long prompt.
CAN DEFEND: the go-live rule to Finance: what is shown, when the assistant declines, and who hears about a conflict.

### Subtopics (technique in service of the scenario)

• Mandatory citation, verified by code
• Declining when the evidence is absent; the hand-over
• Conflicting sources: surface, rank, escalate
• Stale data, and the refresh rule from Tuesday
• Long context as an alternative: the cost and the middle of the window
• The failure catalogue: each known failure with its check

### Trainer notes

START FROM: Thursday's harness, which already showed the unanswerable question answered; Week 8 Thursday's invented refund policy, which today can no longer reach a customer.
GO AS FAR AS: everyone ships an assistant whose every sentence about policy carries a verified citation, that declines the unanswerable question, and that flags the pickup-fee conflict; plus the failure catalogue.
STOP BEFORE: knowledge graphs, agentic retrieval across several searches (Week 13 names it), fine-tuning for grounding.
COMES LATER: Build 4 makes citations mandatory in every group's system; Week 13 lets this assistant act on what it finds.
WHAT THE DATA REVEALS: without the check the assistant cites a numbered section that the policy does not contain; the playbook and the policy contradict each other on the pickup fee; with the whole policy in the prompt the clause in the middle is missed and the call costs many times the retrieval version.
CUT FIRST: the long-context block shrinks to the cost arithmetic. Never cut the citation check or the contradiction.

### Client zero data (TRAINER ONLY)

VERSION corpus (v2.2).
PLANTED (v2.2): two documents that contradict on one clause; a question the corpus cannot answer.
PROPOSED FOR v2.3 (21 Sep 2026, not yet locked): the contradiction is placed on the return pickup fee, between the returns policy and the support playbook; one long policy carries its deciding clause mid-document. Students are never told what is planted.

### In-session exercises

GUIDED: the citation format and its code check; the decline rule.
UNGUIDED: conflict handling, the costed long-context comparison, the failure catalogue.
MID-SESSION (15 min each): check six cited answers and mark each citation as valid or invented; match five symptoms to the failure that causes them.

### After-class tasks

• WRITE: the failure catalogue, final, one page, with the check beside each failure.
• READ: Barnett and others, Seven Failure Points, the summary table.
• RECAP: the three places where grounding is enforced.

### Interview angle

• [S] How do you reduce hallucination in a RAG system?
• [S] How do you make an LLM cite its sources, and how do you know the citation is real?
• [F] When should a RAG assistant refuse to answer?
• [F] Two source documents contradict each other; what should the system do?
• [D] With million-token context windows, is RAG still needed? Argue both sides, then decide for a support desk.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Claude Platform Docs, Citations (verified 21 Sep 2026):
https://platform.claude.com/docs/en/build-with-claude/citations
• Barnett and others, Seven Failure Points When Engineering a Retrieval Augmented Generation System, 2024 (verified 21 Sep 2026):
https://arxiv.org/abs/2401.05856
• Liu and others, Lost in the Middle: How Language Models Use Long Contexts, 2023 (verified 21 Sep 2026):
https://arxiv.org/abs/2307.03172

### Student references

• Pinecone, Retrieval-Augmented Generation (verified 21 Sep 2026):
https://www.pinecone.io/learn/retrieval-augmented-generation/
• freeCodeCamp, Learn RAG From Scratch, a tutorial by a LangChain engineer (verified 21 Sep 2026):
https://www.youtube.com/watch?v=sVcwVQRHIc8

### Kahoot quiz plan

• Q1: three places where grounding is enforced
• Q2: the citation points to a section that does not exist; what should the system do with the answer
• Q3 trap: a bigger context window removes the need for retrieval, true or false
• Q4: two documents disagree; name the two tie-breakers
• Q5: match the symptom to the failure: four pairs
• Return question from Thursday: wrong pieces and a right answer; what is it called, and how is it counted.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W11-5 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Why models neglect the middle and invent the rest: how attention spreads over a long context, and hallucination read as a calibration problem.
PICKS UP WHERE THE ROW STOPS: the row cites the finding that the middle of a long context is used less well, and uses it without explaining it.
CONNECTS TO KALPA: the deciding clause missed mid-document, and the section number that does not exist.
BY THE END: a learner can give one mechanism for the middle effect, and can explain why a model's confidence is a poor guide to its truthfulness. This session closes the IITGN strand.
DOES NOT REPEAT: citations and the decline rule.

## Sat 19 Dec 2026 · Saturday recap · The pen-and-paper test, then the interview-answer discussion

### Business scenario of the day

Retrieval under questioning, from the blender that could not go back to the pickup that was not free. Build 4 opens Monday in Kalpa Logistics, so today also rehearses the transfer: the same pipeline, over documents and a business the room has never seen.

### Thinking we train, before any tool

Saying the week out loud is the interview skill itself.

### Trainer agenda

Four hours, no new content.
1. Recap paper: pen and paper, AI-free, objective, to the blueprint of the 'Saturday papers' tab (110 min).
2. Break (20 min).
3. Marking: papers swapped and marked against the key, read out by the Academic TA (15 min).
4. Solution discussion led by the Academic TA: the most-missed items first, then the interview anchors answered aloud as interview answers, with random call-outs (70 min).
5. Doubts and the bridge: Kalpa Logistics, its documents, and what Build 4 asks for in numbers (25 min).

### Learner outcome

CAN DO: answer the week's business and technique questions on paper without an assistant.
CAN DEFEND: any answer aloud when called; mark a peer's paper against the discussed solution.
STATUS: ungraded; a performance indicator.

### Subtopics (technique in service of the scenario)

THE INTERVIEW ANCHORS (questions only):
• [S] What is RAG, and why use it over fine-tuning or a longer prompt?
• [S] How do you choose a chunk size, and what does overlap cost?
• [S] What is a vector database, and how do you choose an embedding model?
• [S] How do you evaluate a RAG system?
• [S] How do you reduce hallucination in a RAG system?
• [F] What is hybrid search, and what does a reranker add?
• [F] What is faithfulness, and how is it different from correctness?
• [F] How do you keep a RAG index up to date when the documents change?
• [D] Your RAG system scores 82 percent end to end and retrieval recall is poor; how can both be true?
• [D] With million-token context windows, is RAG still needed?
• [D] Kalpa Logistics wants the same assistant over its handling manuals; say what stays the same in your method and what changes.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: an objective paper to the blueprint of the 'Saturday papers' tab: fill in the blank, true or false, one correct option, more than one correct option, scenario sets, applied maths and ordering, graded easy, medium and hard. Print the Item column only; the key, tag, role and anchor columns stay with the team.
PAPER STATUS: the items and the key for this week are still to be built into the 'Saturday papers' tab; this row's anchors are their source. Applied maths suits this week well: recall and precision at k, rank fusion by hand, a token bill for a long context.
MARKING: papers swap and are marked against the key, so a score is comparable across the room and from week to week.
DISCUSSION: the Academic TA opens with the most-missed items, then asks the interview anchors aloud as interview answers, with random call-outs.
STATUS: ungraded, AI-free by format; a performance indicator.

### Client zero data (TRAINER ONLY)

Answers cite Kalpa's own documents and numbers. Findings are discussed; plants are never revealed.

### In-session exercises

THE PAPER: objective, pen and paper, AI-free, for a 110-minute slot. The items and the key are still to be built into the 'Saturday papers' tab, to the same blueprint and the same minutes-per-item assumptions as Weeks 1 to 8.
• Marking a peer's paper against the key.
• Random call-outs on the interview anchors: sixty seconds each.

### After-class tasks

• RECAP: rewrite any question you lost marks on, one line each, in your own words.
• REST: Build 4 opens Monday; the briefs ship when they lock.

### Interview angle

The question set in Subtopics is the interview set for the week.

### Trainer resources

• The 'Saturday papers' tab will hold the items and the key once built; this row's anchors are the source for the discussion.
• DataCamp, Top 30 RAG Interview Questions and Answers for 2026, for the anchors' calibration (verified 21 Sep 2026):
https://www.datacamp.com/blog/rag-interview-questions

### Student references

• Reread the week's rows and your rejected answers; the next paper reuses missed ground one level up.

### Kahoot quiz plan

None. The recap test and discussion replace the quiz.

### IITGN faculty session (TENTATIVE)

None. The Saturday block is the recap paper.

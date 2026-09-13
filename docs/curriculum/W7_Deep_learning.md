# W7 Deep learning

## Mon 09 Nov 2026 · Diwali: Monday off, no session

### Business scenario of the day

No session. Diwali holiday, Monday confirmed off.

### Thinking we train, before any tool

None scheduled.

### Trainer agenda

No session. Diwali fell on Sunday 8 November and Monday is confirmed off; the week teaches Tuesday to Friday.

### Learner outcome

No new outcomes.

### Subtopics (technique in service of the scenario)

None scheduled.

### Trainer notes

Nothing to deliver. The week compresses to four teaching days; training dynamics and debugging share Thursday.

### Client zero data (TRAINER ONLY)

The scenario rests.

### In-session exercises

None scheduled.

### After-class tasks

• OPTIONAL: watch 3Blue1Brown's first neural network lesson before Tuesday.

### Interview angle

None.

### Trainer resources

None needed.

### Student references

• 3Blue1Brown, neural networks topic, first lesson (verified 05 Sep 2026):
https://www.3blue1brown.com/?topic=neural-networks

### Kahoot quiz plan

None.

## Tue 10 Nov 2026 · Neuron and network · The first network, and whether it earns the text

### Business scenario of the day

The nudge campaign ran on the Week 5 model. It worked, modestly: repeat purchases up 3 points in the targeted group, well short of what the plan needs. Marketing has a new idea. "We sit on forty thousand product reviews and every product photo. The model only reads numbers. Can it read the reviews?"
Kavya Nair, the senior analyst, sets the condition: "A network is not magic. Before it earns the text, it has to beat the logistic model on the same numbers. If it cannot, the text will not save it."
Your role: you build the first network on the same features and tell Marketing honestly whether it earned the right to read reviews.
On the table: what a neuron and a layer are, in a picture; why stacking them buys anything; what a network does on tabular data that logistic regression cannot; when the answer is 'nothing yet'.

### Thinking we train, before any tool

A neuron is a weighted sum passed through a bend; a layer is many of them; depth stacks bends into shapes a straight line cannot draw. Without the bend, the whole stack collapses to one linear model, which is the day's proof of what the activation is for.
On the customer table the network ties the logistic model, and that is the honest result: tabular data with a dozen features rarely rewards depth. The network earns the text on Friday, when the input becomes a sequence; today it earns only the comparison sentence.

### Trainer agenda

1. Marketing's ask and Kavya's condition; the room says what 'read the reviews' would need (10 min).
2. The neuron: weighted sum, bias, activation, in one picture; the forward pass traced by hand on two neurons (55 min).
3. Layers and depth: why stacking bends buys shape; the collapse without activation (40 min).
4. The baseline net on the customer table against Week 5's logistic model (45 min).
5. Guided then unguided: the network built, scored, and the comparison sentence for Marketing (50 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a neuron is a weighted sum through a bend, depth stacks bends, and without the bend the stack collapses to one linear model.
CAN DO: trace a forward pass by hand and build the baseline net compared honestly against the logistic model.
CAN HANDLE: the no-activation collapse, and a network that fails to beat the simpler model.
CAN DEFEND: what the activation buys, on the board, and why the network has not yet earned the reviews.

### Subtopics (technique in service of the scenario)

• The neuron: weighted sum, bias, activation
• Layers and the forward pass, traced by hand
• Activation choice; why depth helps
• The collapse without activation
• The baseline net against the logistic model

### Trainer notes

START FROM: the bridge course met neurons; the hand trace is the depth check, so run it before assuming anything.
GO AS FAR AS: everyone ships the baseline net with the honest comparison sentence.
STOP BEFORE: backprop (Wednesday), any architecture beyond a plain MLP, any text.
COMES LATER: learning Wednesday, sick runs and brakes Thursday, the bridge to sequences Friday, where the reviews enter.
WHAT THE DATA REVEALS: strip the activations and three layers score exactly like one linear model; the net ties logistic within a point on the customer table. Let the room find both.
CUT FIRST: the second activation comparison. Never cut the hand trace or the collapse.

### Client zero data (TRAINER ONLY)

VERSION v6: the Week 5 feature set, unchanged; the reviews and photos are named today and enter Friday.
PLANTED: the near-tie between the net and the logistic model.
Kavya Nair is the senior analyst the room has been answering to since Week 2; she is named from today.

### In-session exercises

GUIDED: the two-neuron forward pass on paper with real numbers; then the collapse demonstration.
UNGUIDED: the baseline net built, scored, compared, and the one-sentence answer to Marketing.
MID-SESSION (15 min each): compute one neuron's output from given weights; predict what removing the activation does before running it.

### After-class tasks

• BUILD: widen the net by one layer and note what the comparison does.
• WATCH: 3Blue1Brown, 'But what is a neural network'.
• RECAP: the collapse, one line.

### Interview angle

• [S] What does an activation function do, and what happens without one?
• [F] When would a neural network beat logistic regression on tabular data, and when would it not?
• [D] Marketing wants the network because it is newer; your result says it ties the old model. What do you recommend, and what would change your answer?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• 3Blue1Brown, neural networks lessons, the visual grammar to borrow and redraw (verified 05 Sep 2026):
https://www.3blue1brown.com/lessons/neural-networks/
• Karpathy, Neural Networks: Zero to Hero (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• scikit-learn, neural network models, the MLP the room runs (verified 05 Sep 2026):
https://scikit-learn.org/stable/modules/neural_networks_supervised.html

### Student references

• 3Blue1Brown, neural networks topic, first lesson (verified 05 Sep 2026):
https://www.3blue1brown.com/?topic=neural-networks

### Kahoot quiz plan

• Q1: the neuron in three words, in order
• Q2: compute the neuron's output from the weights shown
• Q3 trap: three layers, no activations; how many effective layers
• Q4: what depth buys, one line
• Q5: the net tied the logistic model; which ships and why
• Return question from Week 5: train 100, validation 61; name it and prescribe.

## Wed 11 Nov 2026 · Backprop intuition, optimisers and training · Making the abandoned loop learn

### Business scenario of the day

The network exists; now it has to learn. Kavya hands over a training loop the previous team abandoned with a note that reads 'loss goes to nan after ten steps, gave up'. The app team, which owns the compute budget, asks how many runs this will take and whether each one will cost as much as the last.
Your role: you make the loop train, explain to a non-specialist what happened at step ten, and give the app team a defensible estimate of runs.
On the table: what training minimises and how it moves; how blame flows back through the layers without the calculus; which dial to suspect first when training misbehaves; how many attempts a sensible engineer budgets for.

### Thinking we train, before any tool

Training descends a loss surface; backprop assigns blame backward through the layers along the same wires the forward pass used; the optimiser decides the step, and the learning rate is its size. The learning rate is the first dial to suspect when a run misbehaves: too hot and the loss climbs to nan, too cold and it crawls.
The abandoned loop had a hot rate. Halving it twice heals the run, which is the debugging move the room will reuse for months, and it is the answer to the app team's budget question: a few disciplined runs, not a lottery.

### Trainer agenda

1. The abandoned loop and its note; the room guesses what 'nan at step ten' means (10 min).
2. Loss as the score to descend; the landscape picture (35 min).
3. Backprop intuition-first: blame flowing backward; no calculus wall (55 min).
4. Optimisers at recognition depth; the learning rate as the first dial (40 min).
5. Guided then unguided: heal the abandoned loop on evidence; the run budget for the app team (60 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: training descends a loss surface, backprop assigns blame backward, the learning rate is the first dial to suspect.
CAN DO: run the loop, read the loss falling, heal a hot rate on evidence, and estimate a run budget.
CAN HANDLE: a loss that diverges to nan, one that crawls, and a budget owner who wants a number of attempts.
CAN DEFEND: backprop in ninety seconds with the blame metaphor and one concrete number.

### Subtopics (technique in service of the scenario)

• Loss functions as the descent target
• Backprop, intuition first
• Optimisers at recognition depth
• The learning rate
• The training loop and the run budget

### Trainer notes

START FROM: Tuesday's forward pass; blame flows backward along the same wires, and that sentence is the bridge.
GO AS FAR AS: everyone heals the abandoned loop and writes the run budget in one sentence.
STOP BEFORE: the chain rule written out, optimiser internals, schedules.
COMES LATER: Thursday reads sick runs and applies the brakes; reproducibility lands there too.
WHAT THE DATA REVEALS: the hot rate prints nan within twenty steps; halved twice, it trains. Let the room do the halving.
CUT FIRST: the optimiser comparison (name two, run one). Never cut the nan run.

### Client zero data (TRAINER ONLY)

VERSION v6 with the abandoned training loop staged in the pack.
PLANTED: a learning rate ten times too hot.
The app team's budget question returns in Week 8 as the token economy.

### In-session exercises

GUIDED: one loop run together with the loss narrated.
UNGUIDED: heal the abandoned loop with a deliberately wrong starting rate; write the run budget.
MID-SESSION (15 min each): match four loss curves to their learning rates; say backprop in ninety seconds to a partner.

### After-class tasks

• BUILD: rerun with two seeds and note the loss difference.
• WATCH: Karpathy, the spelled-out backprop lecture, first half.
• RECAP: blame flowing backward, one line.

### Interview angle

• [S] Explain backpropagation to a non-expert.
• [S] Your loss printed nan; your first two moves.
• [F] What does the learning rate control, and how do you choose one?
• [D] The compute owner asks how many training runs you need; give a number and the reasoning behind it.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Karpathy, Zero to Hero, lecture one (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• 3Blue1Brown, the gradient descent and backprop lessons (verified 05 Sep 2026):
https://www.3blue1brown.com/lessons/neural-networks/

### Student references

• Karpathy, Zero to Hero playlist, lecture one first half (verified 05 Sep 2026):
https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ

### Kahoot quiz plan

• Q1: loss went 2.1, 1.4, 0.9; what is training doing
• Q2: loss went 2.1, 5.8, nan; first move
• Q3: backprop assigns what, in which direction
• Q4 trap: tiny learning rate, loss crawling; is the model broken
• Q5: the one dial to suspect first, always
• Return question from Tuesday: strip the activations and say what the stack becomes.

## Thu 12 Nov 2026 · Training dynamics and debugging a run · Diagnose, then stabilise, then reproduce

### Business scenario of the day

Three runs from three team members, same data, three stories: one oscillates, one crawls on the deep variant, one plateaus and the owner wants ten more epochs. Kavya: "Diagnose each from the chart before anyone touches a setting. Then fix it, and make sure I can reproduce your fix tomorrow."
Your role: you read the charts, prescribe, and hand over a run someone else can repeat exactly, because Build 3 will test this skill with no assistant and an observer in the room.
On the table: what a loss curve says and what it hides; how gradients die or blow up with depth; which brake answers which symptom; why an unseeded run cannot be believed.

### Thinking we train, before any tool

The loss curve is the patient's chart: converging, diverging, plateaued, oscillating each have a cause and a first move. Gradients can vanish or explode as depth grows. The three brakes answer named symptoms: regularisation and dropout for memorising, early stopping for the run that keeps going past its best. A run without a seed cannot be debugged, reported or trusted.
Diagnosis before prescription is the discipline, and it is exactly the shape of the Build 3 AI-free drill, so today's exercise is the rehearsal.

### Trainer agenda

1. Three charts, three stories; the room votes on each before anything runs (10 min).
2. The curve vocabulary; vanishing and exploding gradients at intuition level (55 min).
3. The diagnosis exercise: the three staged runs read from evidence alone (45 min).
4. The brakes as prescriptions: regularisation, dropout, early stopping; seeds and the bug report (55 min).
5. Unguided: stabilise one run, seeded, with a write-up someone else can repeat (35 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: the curve is the chart; gradients can die or blow up; each brake answers a symptom; an unseeded run cannot be believed.
CAN DO: diagnose a staged sick run from its curves, apply the matching brake, and ship a stabilised seeded run with a repeatable write-up.
CAN HANDLE: a plateau read as convergence, dropout left on at evaluation, an oscillation read as a hot rate, and two runs of the same code that disagree.
CAN DEFEND: diagnosis before prescription, from evidence; the shape of the Build 3 drill.

### Subtopics (technique in service of the scenario)

• The loss-curve vocabulary
• Vanishing and exploding gradients
• The diagnosis exercise
• Regularisation, dropout, early stopping as prescriptions
• Batch size in one contrast
• Seeds, reproducibility, the bug report

### Trainer notes

START FROM: Wednesday's nan run was the first diagnosis; today builds the chart-reading habit and prescribes on it, one merged arc because Monday was off.
GO AS FAR AS: everyone closes two diagnoses with evidence-first write-ups and ships the seeded stabilised run.
STOP BEFORE: normalisation layers and clipping mechanics (fix names only), brake mathematics.
COMES LATER: Friday bridges to language models; Build 3 replays today under observation with no assistant, and saying so is the motivation.
WHAT THE DATA REVEALS: the deep variant crawls (vanishing gradient); dropout left on at evaluation drags the score; the unseeded double run disagrees. Let the room find all three.
CUT FIRST: the batch-size contrast. Never cut the diagnosis exercise or the seed demonstration.

### Client zero data (TRAINER ONLY)

VERSION v6 with three staged sick runs from the pack.
PLANTED: a hot-rate oscillation, a vanishing-gradient crawl on the deep variant, a plateau; dropout left on at evaluation in the stabilise step.
The staged runs are reused in Build 3's AI-free drill with fresh seeds.

### In-session exercises

GUIDED: diagnose the first run together, evidence before verdict, then apply its brake.
UNGUIDED: diagnose the other two, stabilise one, seed it, write the repeatable note.
MID-SESSION (15 min each): match six curves to one-line diagnoses; pick the brake for three curve stories.

### After-class tasks

• BUILD: rerun the stabilised config with three seeds and report the spread.
• READ: tomorrow's pre-read naming next-token prediction and auto-regression, terms only.
• RECAP: diagnosis before prescription, one line.

### Interview angle

• [F] Vanishing gradients: what they are and what signals them.
• [F] Regularisation, dropout and early stopping: what does each brake?
• [S] Two runs of the same code give different numbers; what is missing?
• [D] A colleague wants ten more epochs on a plateaued run; what do you say, and what would you look at first?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Karpathy, Zero to Hero, the activations-and-gradients lecture (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• scikit-learn user guide, early stopping and regularisation for the MLP in use (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html

### Student references

• Karpathy playlist, the activations-and-gradients lecture, the diagnosis segments (verified 05 Sep 2026):
https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ

### Kahoot quiz plan

• Q1: the curve oscillates; first suspect
• Q2: deep variant crawls, shallow trains fine; name the disease
• Q3: which brake for the curve shown
• Q4 trap: evaluation score below training behaviour, dropout involved; the switch
• Q5: two runs, same code, different numbers; the missing line
• Return question from Wednesday: loss hit nan; the two-step fix and why it works.

## Fri 13 Nov 2026 · The bridge to next-token prediction · Reviews as sequences, and why attention won

### Business scenario of the day

The reviews finally enter. Marketing's forty thousand reviews are text, and text is a sequence: the meaning of 'not worth it' depends on the word before 'worth'. Kavya: "Show me the smallest thing that can read a sequence, and tell me where it breaks. Then tell me why the industry stopped using it."
Your role: you build a tiny model that predicts the next character of Kalpa's own review text, show the room what it forgets over long distances, and connect that failure to the tool Week 8 introduces.
On the table: how raw text becomes training data with no labels; how a model generates one step at a time; why order matters and where memory fails; why attention replaced recurrence.

### Thinking we train, before any tool

Next-token prediction turns raw text into training data with no labels: every position is a question whose answer is the next token. Auto-regression generates one step at a time, feeding its own output back. Sequence models carry memory forward, and that memory fails over long distances, which the room sees when the toy forgets an opening bracket by the closing one.
Attention won because it reads the whole context at once instead of squeezing it through a sequence bottleneck. The concept map from neuron to next-token is the week's assessment, and it is the map Week 8 fills in.

### Trainer agenda

1. Kavya's ask; two review snippets where word order flips the meaning (10 min).
2. Next-token prediction: the task that needs no labels (45 min).
3. Auto-regression: feeding the output back; a tiny character model on review text (40 min).
4. Sequence memory and the long-range failure; why attention replaced recurrence, at intuition level (50 min).
5. Guided then unguided: the concept map from neuron to next-token, drawn and defended (45 min).
6. Kahoot and week close (20 min).

### Learner outcome

UNDERSTANDS: next-token prediction makes training data from raw text, auto-regression generates stepwise, memory fails over distance, and attention reads the whole context at once.
CAN DO: trace an auto-regressive generation by hand and draw the week-to-LLM concept map.
CAN HANDLE: the long-range failure told as evidence rather than history.
CAN DEFEND: why language models train on next tokens, in ninety seconds; a standing interview opener.

### Subtopics (technique in service of the scenario)

• Next-token prediction
• Auto-regression
• Sequence modelling and the long-range problem
• Why attention replaced recurrence
• The concept map artifact

### Trainer notes

START FROM: everything this week; the bridge connects rather than adds.
GO AS FAR AS: everyone draws the map from neuron to next-token unaided.
STOP BEFORE: transformer internals; every named piece gets its day next week.
WHAT THE DATA REVEALS: the recurrent toy forgets the opening bracket by the closing one; the room states what a fix must do before attention is named.
CUT FIRST: the second generation trace. Never cut the concept map.

### Client zero data (TRAINER ONLY)

VERSION text: the reviews table enters; a tiny character-level model over Kalpa review text.
PLANTED: the long-range failure on a bracketed review.
The support tickets enter Monday of Week 8.

### In-session exercises

GUIDED: one generation traced together, token by token.
UNGUIDED: the concept map drawn solo, then defended to a partner.
MID-SESSION (15 min each): order the pipeline cards from raw text to generated token; state the long-range problem in one sentence.

### After-class tasks

• WATCH: the first half of Karpathy's bigram lecture.
• READ: the Week 8 pre-read on classical text lineage (TF-IDF, word vectors), shipped tonight.
• RECAP: why next tokens, ninety seconds, spoken to yourself.

### Interview angle

• [S] Why do language models train on next-token prediction?
• [F] What is the long-range problem, and why did transformers replace recurrent models?
• [D] Marketing asks whether 'reading the reviews' is a solved problem; what do you say a model can and cannot do with text today?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Karpathy, Zero to Hero, the bigram language-model lecture (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• Jay Alammar, The Illustrated GPT-2, the auto-regression visual to redraw (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-gpt2/

### Student references

• Karpathy playlist, the bigram lecture first half (verified 05 Sep 2026):
https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ

### Kahoot quiz plan

• Q1: next-token prediction needs what labels
• Q2: auto-regression feeds what to where
• Q3: the long-range problem in one line
• Q4 trap: attention is faster because it is smaller, true or false
• Q5: place five cards on the concept map fast
• Return question from Thursday: three seeds, three scores; what spread makes you distrust the result.

## Sat 14 Nov 2026 · Saturday recap · The pen-and-paper test, then the interview-answer discussion

### Business scenario of the day

The deep-learning week under questioning, four days compressed by the holiday: the network, the loop, the sick runs, the bridge to text.

### Thinking we train, before any tool

Saying the week out loud is the interview skill itself.

### Trainer agenda

Four hours, no new content.
1. Recap test: pen and paper, AI-free, from the week's question set (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped, answers as interview answers, random call-outs (75 min).
4. Doubts and the bridge: tickets and reviews as text, and the tool that reads them (25 min).

### Learner outcome

CAN DO: answer the week's business and technique questions on paper.
CAN DEFEND: any answer aloud; mark a peer's paper.
STATUS: ungraded; a performance indicator.

### Subtopics (technique in service of the scenario)

THE QUESTION SET (questions only; answers built at detailing):
• [S] What does an activation function do, and what happens without one?
• [S] Explain backpropagation to a non-expert.
• [S] Your loss printed nan; your first two moves.
• [F] Vanishing gradients: what they are and what signals them.
• [F] Regularisation, dropout and early stopping: what does each brake?
• [S] Two runs of the same code give different numbers; what is missing?
• [F] Why did transformers replace recurrent models?
• [D] The network ties the logistic model on tabular data; what do you recommend, and what would change your answer?
• [D] When would you not use deep learning?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper comes from this row's question set; the Academic TA leads; random call-outs.
STATUS: ungraded, AI-free by format.

### Client zero data (TRAINER ONLY)

Answers cite the scenario net's own runs and the review-text toy.

### In-session exercises

• The two-hour recap test.
• Peer cross-evaluation.
• Random call-outs.

### After-class tasks

• RECAP: the week's crux lines from memory.
• REST: Week 8 needs no new setup.

### Interview angle

The question set in Subtopics is the interview set for the week.

### Trainer resources

• This row's question set is the paper's source.
• Interview Query, the deep-learning items (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions

### Student references

• 3Blue1Brown, any lesson that felt shaky (verified 05 Sep 2026):
https://www.3blue1brown.com/?topic=neural-networks

### Kahoot quiz plan

None. The recap test and discussion replace the quiz.

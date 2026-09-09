# W7 Curriculum

## Mon 09 Nov 2026 · Diwali holiday: Monday off (confirmed), no session

### Trainer agenda

No session. Diwali fell on Sunday 8 November and Monday 9 November is confirmed off; the week teaches Tuesday to Friday.

### Learner outcome

No new outcomes.

### Subtopics

None scheduled.

### Trainer notes

Nothing to deliver. The week compresses to four teaching days: the diagnostics and control days merge on Thursday, and the bridge day holds Friday.

### Client zero and case studies

The scenario rests.

### In-session exercises

None scheduled.

### After-class tasks

• OPTIONAL: the classical NLP pre-read ships Friday; nothing due tonight.

### Trainer resources

None needed.

### Student references

None assigned.

### Kahoot quiz plan

None.

## Tue 10 Nov 2026 · The network: neurons, layers, and the forward pass

### Trainer agenda

1. A trained network scoring the scenario outcome on screen, then opened up (10 min).
2. The neuron: weighted sum, bias, activation, in one picture (45 min).
3. Layers and the forward pass traced by hand on a two-neuron net (50 min).
4. Activation choice and why depth helps, at intuition level (40 min).
5. Guided then unguided: the baseline net on the scenario, scored against Week 5's simpler model (55 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: a neuron is a weighted sum passed through a bend, depth stacks bends into expressiveness, and without the bend the whole stack collapses to one linear model.
CAN DO: trace a forward pass by hand and ship the baseline net compared against Week 5's model.
CAN HANDLE: the no-activation collapse, and a net that fails to beat the simpler model.
CAN DEFEND: what the activation buys, on the whiteboard, with the two-neuron trace.

### Subtopics

• The neuron: weighted sum, bias, activation
• Layers and the forward pass
• Activation choice
• Why depth helps
• The baseline net against Week 5's model

### Trainer notes

START FROM: the bridge course met neurons; the hand trace is the depth check, so run it before assuming anything.
GO AS FAR AS: every learner ships the baseline net with the honest comparison.
STOP BEFORE: backprop (tomorrow), any architecture beyond a plain MLP.
COMES LATER: learning tomorrow, diagnostics and the brakes together on Thursday; the bridge to LLMs closes the week.
BREAK TO RUN: the no-activation collapse: strip the activations and watch three layers score exactly like one linear model; the wrong-output that proves what the bend is for.
CUT FIRST: the second activation comparison. Never cut the hand trace.

### Client zero and case studies

TODAY'S DATA: the scenario's feature set from Week 5, unchanged; the net must beat the tuned simple model to earn its keep, and the comparison sentence is the day's artifact.
COMPETENCY BUILT: see inside the black box from day one.
CASE: none cited; the collapse demonstration carries the day.

### In-session exercises

GUIDED: trace the two-neuron forward pass together on paper, numbers real.
UNGUIDED: the baseline net built, scored and compared, no hints, solution at close.
MID-SESSION (15 min each): compute one neuron's output from given weights fast; predict what removing the activation does before running it.

### After-class tasks

• BUILD: widen the net by one layer and note what the comparison does.
• WATCH: 3Blue1Brown's 'But what is a neural network' before tomorrow (link in student references).
• RECAP: the collapse, one line.

### Trainer resources

• 3Blue1Brown, neural networks lessons, the visual grammar to borrow and redraw (verified 05 Sep 2026):
https://www.3blue1brown.com/lessons/neural-networks/
• Karpathy, Neural Networks: Zero to Hero, the spelled-out backprop lecture for depth (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• scikit-learn, neural network models page for the MLP the room actually runs (verified 05 Sep 2026):
https://scikit-learn.org/stable/modules/neural_networks_supervised.html

### Student references

• 3Blue1Brown, neural networks topic, first lesson tonight (verified 05 Sep 2026):
https://www.3blue1brown.com/?topic=neural-networks

### Kahoot quiz plan

• Q1: the neuron in three words, in order
• Q2: compute the neuron's output from the weights shown
• Q3 trap: three layers, no activations; how many effective layers
• Q4: what depth buys, one line
• Q5: the net tied the simple model; which ships and why
• Return question from Week 5, one level up: train 100, validation 61; name it and prescribe.

## Wed 11 Nov 2026 · Learning: backprop intuition, loss, optimisers, learning rate

### Trainer agenda

1. The same net, untrained then trained, side by side (10 min).
2. Loss as the score to descend; the landscape picture (40 min).
3. Backprop intuition-first: blame flowing backward, no calculus wall (55 min).
4. Optimisers and the learning rate: step size as the one dial that matters first (45 min).
5. Guided then unguided training loop on the scenario net (50 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: training descends a loss surface, backprop assigns blame backward through the layers, and the learning rate is the first dial to suspect when training misbehaves.
CAN DO: run the training loop, read the loss falling, and adjust the learning rate on evidence.
CAN HANDLE: a loss that diverges to nan at a hot learning rate, and one that crawls at a cold one.
CAN DEFEND: backprop in ninety seconds with the blame metaphor and one concrete number.

### Subtopics

• Loss functions as the descent target
• Backprop, intuition first
• Optimisers at recognition depth
• The learning rate
• The training loop artifact

### Trainer notes

START FROM: yesterday's forward pass; blame flows backward along the same wires, and saying that sentence is the whole bridge.
GO AS FAR AS: every learner runs the loop and fixes one misbehaving learning rate on evidence.
STOP BEFORE: the chain rule written out, optimiser internals, schedules.
COMES LATER: Thursday reads sick runs and applies the brakes in one arc; reproducibility lands there too.
BREAK TO RUN: the hot learning rate: loss rises then prints nan within twenty steps; the room halves the rate twice and watches it heal, which is the debugging move they will reuse for months.
CUT FIRST: the optimiser comparison (name two, run one). Never cut the nan run.

### Client zero and case studies

TODAY'S DATA: the same net and features; the loop is the artifact and the loss curve is its evidence.

### In-session exercises

GUIDED: one training loop run together with the loss narrated.
UNGUIDED: train to a stated loss with a deliberately wrong starting rate, fix it on evidence, no hints, solution at close.
MID-SESSION (15 min each): match four loss curves to their learning rates; say backprop in ninety seconds to a partner.

### After-class tasks

• BUILD: rerun with two seeds and note the loss difference.
• WATCH: Karpathy's spelled-out backprop lecture, first half (link in student references).
• RECAP: blame flowing backward, one line.

### Trainer resources

• Karpathy, Neural Networks: Zero to Hero, lecture one (verified 05 Sep 2026):
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
• Return question from Tuesday, one level up: strip the activations and say what the stack becomes and why.

## Thu 12 Nov 2026 · Sick runs and the brakes: diagnose, then stabilise (merged day)

### Trainer agenda

1. Four loss curves on screen, one healthy; the room votes (10 min).
2. The curve vocabulary: converging, diverging, plateaued, oscillating; vanishing and exploding gradients at intuition level (60 min).
3. The diagnosis exercise: two staged sick runs read from evidence alone (50 min).
4. The brakes as the prescriptions: regularisation, dropout, early stopping, applied to the runs just diagnosed (55 min).
5. Seeds and reproducibility: the two-runs-two-numbers demonstration and the bug-report rule (30 min).
6. Unguided stabilised run; Kahoot and close-out (45 min).

### Learner outcome

UNDERSTANDS: the loss curve is the patient's chart, gradients can die or blow up with depth, each brake answers a named symptom, and an unseeded run cannot be debugged or believed.
CAN DO: diagnose a staged sick run from its curves, apply the matching brake, and ship the stabilised, seeded run.
CAN HANDLE: a plateau read as convergence, dropout left on at evaluation, and an oscillation read as a hot rate.
CAN DEFEND: diagnosis before prescription, from evidence, which is exactly the shape of Build 3's AI-free drill.

### Subtopics

• The loss-curve vocabulary
• Vanishing and exploding gradients
• The diagnosis exercise, evidence first
• Regularisation, dropout, early stopping as prescriptions
• Batch size in one contrast
• Seeds and reproducibility
• The stabilised run artifact

### Trainer notes

START FROM: Wednesday's nan run gave the first diagnosis; today builds the full chart-reading habit and prescribes on it, one merged arc because Monday was a holiday.
GO AS FAR AS: every learner closes two diagnoses with evidence-first write-ups and ships the stabilised, seeded run.
STOP BEFORE: normalisation layers and clipping mechanics (fix names only), brake mathematics.
COMES LATER: tomorrow bridges to language models; Build 3's observed drill replays today's skill, and saying so is the motivation.
BREAKS TO RUN: the vanishing-gradient crawl on the deep variant; dropout left on at evaluation, found by the room; the unseeded double run closed with the seed rule.
CUT FIRST: the batch-size contrast, then the third brake comparison. Never cut the diagnosis exercise or the seed demonstration.

### Client zero and case studies

TODAY'S DATA: the scenario net in staged sick configurations from the pack, so every learner reads identical evidence; the stabilised run replaces the baseline as the standing model.

### In-session exercises

GUIDED: diagnose the first sick run together, evidence before verdict, then apply its brake.
UNGUIDED: diagnose the second run, choose brakes, ship the stabilised seeded run, no hints, solution at close.
MID-SESSION (15 min each): match six curves to one-line diagnoses; pick the brake for three curve stories.

### After-class tasks

• BUILD: rerun the stabilised config with three seeds and report the spread.
• READ: tomorrow's pre-read naming next-token prediction and auto-regression, terms only.
• RECAP: diagnosis before prescription, one line.

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
• Return question from Wednesday's learning day, one level up: loss hit nan; the two-step fix and why it works.

## Fri 13 Nov 2026 · The bridge to LLMs: next-token prediction and why attention won

### Trainer agenda

1. A tiny character model completing scenario field names on screen (10 min).
2. Next-token prediction: the task that needs no labels (45 min).
3. Auto-regression: feeding the output back, one token at a time (40 min).
4. Sequence memory and the long-range problem; why attention replaced recurrence, at intuition level (50 min).
5. Guided then unguided: the concept map connecting this week to the next (45 min).
6. Kahoot and week close (20 min).

### Learner outcome

UNDERSTANDS: next-token prediction turns raw text into training data, auto-regression generates one step at a time, and attention won because it reads the whole context at once instead of squeezing it through a sequence bottleneck.
CAN DO: trace an auto-regressive generation by hand and draw the week-to-LLM concept map.
CAN HANDLE: the long-range failure that motivates attention, told as evidence rather than history.
CAN DEFEND: why language models train on next tokens, in ninety seconds, which is a standing interview opener.

### Subtopics

• Next-token prediction
• Auto-regression
• Sequence modelling and the long-range problem
• Why attention replaced recurrence
• The concept map artifact

### Trainer notes

START FROM: everything this week; the bridge day earns its keep by connecting rather than adding, and the concept map is the whole assessment.
GO AS FAR AS: every learner draws the map from neuron to next-token unaided.
STOP BEFORE: transformer internals; every named piece gets its day next week, and saying that map aloud is the forward hook.
BREAK TO RUN: the long-range failure: the recurrent toy forgets the opening bracket by the closing one, and the room states what a fix must do before attention is named.
CUT FIRST: the second generation trace. Never cut the concept map.

### Client zero and case studies

TODAY'S DATA: a tiny character-level model over the scenario's own field vocabulary, so the first generation a learner ever reads speaks the spine's language.

### In-session exercises

GUIDED: one generation traced together, token by token.
UNGUIDED: the concept map drawn solo, then defended to a partner, solution at close.
MID-SESSION (15 min each): order the pipeline cards from raw text to generated token; state the long-range problem in one sentence.

### After-class tasks

• WATCH: the first half of Karpathy's bigram lecture before Monday (link in student references).
• READ: the Week 8 pre-read on classical NLP lineage (TF-IDF, word vectors), shipped tonight per the plan's pre-read note.
• RECAP: why next tokens, ninety seconds, spoken to yourself.

### Trainer resources

• Karpathy, Zero to Hero, the bigram language-model lecture (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• Jay Alammar, The Illustrated GPT-2, for the auto-regression visual to redraw (verified 05 Sep 2026):
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
• Return question from Thursday, one level up: three seeds, three scores; what spread makes you distrust the result.

## Sat 14 Nov 2026 · Saturday recap: the pen-and-paper test, then the interview-answer discussion

### Trainer agenda

Four hours, no new content.
1. Weekly recap test: pen and paper, AI-free, built from the week's interview question set, short-answer format (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped for peer cross-evaluation, every answer discussed as an interview answer, random call-outs throughout (75 min).
4. Doubt clearing and the bridge: Week 8 names the empty boxes on the concept map (25 min).

### Learner outcome

CAN DO: answer the week's interview set on paper, without an assistant, in short-answer form.
CAN DEFEND: any of those answers aloud when called, and mark a peer's paper against the discussed solution.
STATUS: ungraded; the score is a performance indicator the programme reads, never a marks component.

### Subtopics

THE QUESTION SET (questions only; answers are built at the detailing phase):
• [S] What does an activation function do, and what happens without one?
• [S] Explain backpropagation to a non-expert in ninety seconds.
• [S] Your loss printed nan: your first two moves.
• [F] Vanishing gradients: what they are and what signals them.
• [F] Regularisation, dropout and early stopping: what does each brake?
• [S] Batch size: what does it trade?
• [D] Two runs of the same code give different numbers: what is missing, and why does a bug report need it?
• [D] When would you not use deep learning?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. The tagging is this programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper is built from this row's question set, framed for short answers (selection, one-liners, small computations) so peer cross-checking works; answers themselves are written at the detailing phase, never improvised on the day.
DISCUSSION: papers swap for peer cross-evaluation; the Academic TA leads the solution walk-through as an interview-answer discussion, with random call-outs throughout.
STATUS: ungraded, a performance indicator rather than a marks component, and AI-free by format.

### Client zero and case studies

Answers must cite the scenario's own numbers and artifacts where the week produced them; the scenario net's own runs and numbers are the reference.

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

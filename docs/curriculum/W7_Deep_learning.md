# W7 Deep learning

## Mon 16 Nov 2026 · Neuron, network and activation functions · The first network, and whether it earns the text

### Business scenario of the day

The nudge campaign ran on the Week 5 model. It worked, modestly: repeat purchases up 3 points in the targeted group, well short of what the plan needs. Marketing has a new idea. "We sit on forty thousand product reviews and every product photo. The model only reads numbers. Can it read the reviews?"
Kavya Nair, the senior analyst, sets the condition: "A network is not magic. Before it earns the text, it has to beat the logistic model on the same numbers. If it cannot, the text will not save it."
Your role: you build the first network on the same features and tell Marketing honestly whether it earned the right to read reviews.
On the table: what a neuron and a layer are, in a picture; why stacking them buys anything; what a network does on tabular data that logistic regression cannot; when the answer is 'nothing yet'.

### Thinking we train, before any tool

A neuron is a weighted sum passed through a bend; a layer is many of them; depth stacks bends into shapes a straight line cannot draw. Running an input through the layers to a prediction is forward propagation, and the room does it by hand before any library does it for them. Without the bend, the whole stack collapses to one linear model, which is the day's proof of what the activation is for. The bend comes in three common shapes: sigmoid squeezes to between 0 and 1 and sits at a yes-or-no output, tanh squeezes to between -1 and 1, and ReLU passes positives and zeroes negatives and is the usual choice inside the network.
On the customer table the network ties the logistic model, and that is the honest result: tabular data with a dozen features rarely rewards depth. The network earns the text on Thursday, when the input becomes a sequence; today it earns only the comparison sentence.

### Trainer agenda

1. Marketing's ask and Kavya's condition; the room says what 'read the reviews' would need (10 min).
2. The neuron: weighted sum, bias, activation, in one picture; forward propagation traced by hand on two neurons (50 min).
3. The three activations on one input range: sigmoid, tanh and ReLU, with where each sits; layers and depth; the collapse without activation (50 min).
4. The baseline net on the customer table against Week 5's logistic model; the network families named on one map (45 min).
5. Guided then unguided: the network built, scored, and the comparison sentence for Marketing (45 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a neuron is a weighted sum through a bend, forward propagation runs an input through the layers, depth stacks bends, and without the bend the stack collapses to one linear model.
CAN DO: trace a forward pass by hand, say where sigmoid, tanh and ReLU each sit and why, and build the baseline net compared honestly against the logistic model.
CAN HANDLE: the no-activation collapse, and a network that fails to beat the simpler model.
CAN DEFEND: what the activation buys, on the board, and why the network has not yet earned the reviews.

### Subtopics (technique in service of the scenario)

• The neuron: weighted sum, bias, activation
• Forward propagation through the layers, traced by hand with real numbers
• The activation family: sigmoid, tanh and ReLU, with the output range and the usual seat of each; softmax named for the many-class output
• Why depth helps; the collapse without activation
• The network families on one map: the feed-forward network used today, the convolutional network for images (named and parked), the recurrent family that arrives on Thursday
• The baseline net against the logistic model

### Trainer notes

START FROM: the bridge course met neurons; the hand trace is the depth check, so run it before assuming anything.
GO AS FAR AS: everyone ships the baseline net with the honest comparison sentence, and can place the three activations.
STOP BEFORE: backprop (Tuesday), any architecture beyond a plain feed-forward network, any text. The convolutional and recurrent families are named on the map and not built; vision stays outside this programme.
COMES LATER: learning Tuesday, sick runs and brakes Wednesday, sequence models and the bridge Thursday, where the reviews enter, and tokens on Friday.
WHAT THE DATA REVEALS: strip the activations and three layers score exactly like one linear model; the net ties logistic within a point on the customer table. Let the room find both.
CUT FIRST: the network-families map, down to two minutes. Never cut the hand trace or the collapse.

### Client zero data (TRAINER ONLY)

VERSION v6: the Week 5 feature set, unchanged; the reviews and photos are named today and enter Thursday.
PLANTED: the near-tie between the net and the logistic model.
Kavya Nair is the senior analyst the room has been answering to since Week 2; she is named from today.

### In-session exercises

GUIDED: the two-neuron forward pass on paper with real numbers; then the collapse demonstration.
UNGUIDED: the baseline net built, scored, compared, and the one-sentence answer to Marketing.
MID-SESSION (15 min each): compute one neuron's output from given weights under sigmoid and under ReLU; predict what removing the activation does before running it.

### After-class tasks

• BUILD: widen the net by one layer and note what the comparison does.
• WATCH: 3Blue1Brown, 'But what is a neural network'.
• RECAP: the collapse, one line.

### Interview angle

• [S] What does an activation function do, and what happens without one?
• [S] Sigmoid, tanh or ReLU: where does each sit in a network, and why?
• [SV] Name the main types of neural network and one job each was built for.
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
• CS231n notes, neural networks part 1, the activation functions section (verified 19 Sep 2026):
https://cs231n.github.io/neural-networks-1/

### Student references

• 3Blue1Brown, neural networks topic, first lesson (verified 05 Sep 2026):
https://www.3blue1brown.com/?topic=neural-networks

### Kahoot quiz plan

• Q1: the neuron in three words, in order
• Q2: compute the neuron's output from the weights shown, under ReLU
• Q3 trap: three layers, no activations; how many effective layers
• Q4: which activation sits at the output for a yes-or-no probability
• Q5: what depth buys, one line
• Q6: the net tied the logistic model; which ships and why
• Return question from Week 5: train 100, validation 61; name it and prescribe.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W7-1 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Why depth and non-linearity: a network as a composition of functions, the universal approximation idea, and what a hidden layer represents.
PICKS UP WHERE THE ROW STOPS: the row traces a forward pass by hand and shows the collapse without an activation, and leaves the why open.
CONNECTS TO KALPA: the baseline net against Week 5's logistic model, since logistic regression is a network with no hidden layer.
BY THE END: a learner can show that stacked linear layers stay linear, state the approximation idea and its limits, and say what width and depth each buy.
DOES NOT REPEAT: the forward pass by hand.

## Tue 17 Nov 2026 · Backprop intuition, optimisers and training · Making the abandoned loop learn

### Business scenario of the day

The network exists; now it has to learn. Kavya hands over a training loop the previous team abandoned with a note that reads 'loss goes to nan after ten steps, gave up'. The app team, which owns the compute budget, asks how many runs this will take and whether each one will cost as much as the last.
Your role: you make the loop train, explain to a non-specialist what happened at step ten, and give the app team a defensible estimate of runs.
On the table: what training minimises and how it moves; how blame flows back through the layers without the calculus; which dial to suspect first when training misbehaves; how many attempts a sensible engineer budgets for.

### Thinking we train, before any tool

Training descends a loss surface: squared error when the target is a number, cross-entropy when it is a class. Backprop assigns blame backward through the layers along the same wires the forward pass used, and each weight then moves by one rule: new weight equals old weight minus learning rate times gradient. The optimiser decides how that step is taken: plain gradient descent follows the slope, momentum keeps some of the last step's direction, RMSProp sizes the step for each weight, and Adam does both. The learning rate is the first dial to suspect when a run misbehaves: too hot and the loss climbs to nan, too cold and it crawls. A network rarely finds the lowest valley on the whole surface; it finds a good one, and that is enough when validation agrees.
The abandoned loop had a hot rate. Halving it twice heals the run, which is the debugging move the room will reuse for months, and it is the answer to the app team's budget question: a few disciplined runs, not a lottery.

### Trainer agenda

1. The abandoned loop and its note; the room guesses what 'nan at step ten' means (10 min).
2. Loss as the score to descend: squared error for a number, cross-entropy for a class; the landscape picture with its many valleys (35 min).
3. Backprop intuition-first: blame flowing backward; one weight updated by hand from a given gradient; no calculus wall (55 min).
4. Optimisers at recognition depth: plain gradient descent, momentum, RMSProp, Adam; full-batch, stochastic and mini-batch updates; the learning rate as the first dial (40 min).
5. Guided then unguided: heal the abandoned loop on evidence; the run budget for the app team (60 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: training descends a loss surface, backprop assigns blame backward, every weight moves by the same update rule, and the learning rate is the first dial to suspect.
CAN DO: update one weight by hand, run the loop, read the loss falling, heal a hot rate on evidence, and estimate a run budget.
CAN HANDLE: a loss that diverges to nan, one that crawls, and a budget owner who wants a number of attempts.
CAN DEFEND: backprop in ninety seconds with the blame metaphor and one concrete number, and what momentum, RMSProp and Adam each add.

### Subtopics (technique in service of the scenario)

• Loss functions as the descent target: squared error for a number, cross-entropy for a class
• Backprop, intuition first: blame flowing backward along the forward wires
• The weight update rule, computed once by hand: new weight equals old weight minus learning rate times gradient
• Full-batch, stochastic and mini-batch gradient descent in one contrast
• The optimiser family at recognition depth: momentum, RMSProp and Adam, with one line on what each adds
• The learning rate; local and global minima at intuition level
• The training loop and the run budget

### Trainer notes

START FROM: Monday's forward pass; blame flows backward along the same wires, and that sentence is the bridge.
GO AS FAR AS: everyone updates one weight by hand, heals the abandoned loop and writes the run budget in one sentence.
STOP BEFORE: the chain rule written out across layers, optimiser equations, schedules.
COMES LATER: Wednesday reads sick runs and applies the brakes; reproducibility lands there too.
WHAT THE DATA REVEALS: the hot rate prints nan within twenty steps; halved twice, it trains. Let the room do the halving.
CUT FIRST: the full-batch against mini-batch contrast; name the optimisers and run one. Never cut the nan run or the hand update.

### Client zero data (TRAINER ONLY)

VERSION v6 with the abandoned training loop staged in the pack.
PLANTED: a learning rate ten times too hot.
The app team's budget question returns in Week 8 as the token economy.

### In-session exercises

GUIDED: one loop run together with the loss narrated.
UNGUIDED: heal the abandoned loop with a deliberately wrong starting rate; write the run budget.
MID-SESSION (15 min each): update one weight by hand from a given gradient and learning rate, then match four loss curves to their learning rates; say backprop in ninety seconds to a partner.

### After-class tasks

• BUILD: rerun with two seeds and note the loss difference.
• WATCH: Karpathy, the spelled-out backprop lecture, first half.
• RECAP: blame flowing backward, one line.

### Interview angle

• [S] Explain backpropagation to a non-expert.
• [S] Write the weight update rule and say what each term does.
• [S] Your loss printed nan; your first two moves.
• [F] What does the learning rate control, and how do you choose one?
• [F] Gradient descent, momentum, RMSProp, Adam: what does each add?
• [D] The compute owner asks how many training runs you need; give a number and the reasoning behind it.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Karpathy, Zero to Hero, lecture one (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• 3Blue1Brown, the gradient descent and backprop lessons (verified 05 Sep 2026):
https://www.3blue1brown.com/lessons/neural-networks/
• CS231n notes, neural networks part 3, the parameter updates section (verified 19 Sep 2026):
https://cs231n.github.io/neural-networks-3/
• Sebastian Ruder, an overview of gradient descent optimisation algorithms (verified 19 Sep 2026):
https://www.ruder.io/optimizing-gradient-descent/

### Student references

• Karpathy, Zero to Hero playlist, lecture one first half (verified 05 Sep 2026):
https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ

### Kahoot quiz plan

• Q1: loss went 2.1, 1.4, 0.9; what is training doing
• Q2: loss went 2.1, 5.8, nan; first move
• Q3: weight 0.50, gradient 0.80, learning rate 0.10; the new weight
• Q4: backprop assigns what, in which direction
• Q5 trap: tiny learning rate, loss crawling; is the model broken
• Q6: which optimiser keeps a memory of the last step's direction
• Return question from Monday: strip the activations and say what the stack becomes.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W7-2 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Backpropagation derived: the chain rule on a computational graph, a two-layer network worked by hand, and the update equations from gradient descent to momentum and Adam.
PICKS UP WHERE THE ROW STOPS: the row teaches backpropagation intuition-first and stops before the chain rule across layers and the optimiser equations.
CONNECTS TO KALPA: the abandoned training loop that goes to nan at step ten.
BY THE END: a learner can derive the gradients of a two-layer network, and can write the update rule of each optimiser and say what its extra terms do.
DOES NOT REPEAT: the single weight updated by hand from a given gradient.

## Wed 18 Nov 2026 · Training dynamics and debugging a run · Diagnose, then stabilise, then reproduce

### Business scenario of the day

Three runs from three team members, same data, three stories: one oscillates, one crawls on the deep variant, one plateaus and the owner wants ten more epochs. Kavya: "Diagnose each from the chart before anyone touches a setting. Then fix it, and make sure I can reproduce your fix tomorrow."
Your role: you read the charts, prescribe, and hand over a run someone else can repeat exactly, because Build 3 will test this skill with no assistant and an observer in the room.
On the table: what a loss curve says and what it hides; how gradients die or blow up with depth; which brake answers which symptom; why an unseeded run cannot be believed.

### Thinking we train, before any tool

The loss curve is the patient's chart: converging, diverging, plateaued, oscillating each have a cause and a first move. Gradients can vanish or explode as depth grows: a sigmoid's slope never exceeds 0.25, so ten sigmoid layers can shrink the signal to about a millionth, which is why deep networks moved to ReLU inside. The three brakes answer named symptoms: regularisation and dropout for memorising, early stopping for the run that keeps going past its best. A run without a seed cannot be debugged, reported or trusted.
Diagnosis before prescription is the discipline, and it is exactly the shape of the Build 3 AI-free drill, so today's exercise is the rehearsal.

### Trainer agenda

1. Three charts, three stories; the room votes on each before anything runs (10 min).
2. The curve vocabulary; vanishing and exploding gradients at intuition level, with the sigmoid arithmetic that starves deep layers and the named fixes (55 min).
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
• Vanishing and exploding gradients, the activation choice behind them, and the named fixes: ReLU inside, skip connections, normalisation layers
• The diagnosis exercise
• Regularisation, dropout, early stopping as prescriptions
• Batch size in one contrast
• Seeds, reproducibility, the bug report

### Trainer notes

START FROM: Tuesday's nan run was the first diagnosis; today builds the chart-reading habit and prescribes on it, as one merged arc.
GO AS FAR AS: everyone closes two diagnoses with evidence-first write-ups and ships the seeded stabilised run.
STOP BEFORE: normalisation layers and clipping mechanics (fix names only), brake mathematics.
COMES LATER: Thursday bridges to language models; Build 3 replays today under observation with no assistant, and saying so is the motivation.
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

• [F] Vanishing gradients: what they are, what signals them, and which activation choices cause or cure them.
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
• Return question from Tuesday: loss hit nan; the two-step fix and why it works.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W7-3 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Why gradients vanish and explode: the product of derivatives through depth, initialisation, normalisation layers and gradient clipping; dropout and weight decay as mathematics.
PICKS UP WHERE THE ROW STOPS: the row gives the names of the fixes and stops before normalisation and clipping mechanics and before the mathematics of the brakes.
CONNECTS TO KALPA: the three staged runs the room diagnosed from their charts.
BY THE END: a learner can show with sigmoid arithmetic why deep layers starve, and can explain what each fix changes in the equations.
DOES NOT REPEAT: reading loss curves.

## Thu 19 Nov 2026 · Sequence models and the bridge to next-token prediction · Reviews as sequences, and why attention won

### Business scenario of the day

The reviews finally enter. Marketing's forty thousand reviews are text, and text is a sequence: the meaning of 'not worth it' depends on the word before 'worth'. Kavya: "Show me the smallest thing that can read a sequence, and tell me where it breaks. Then tell me why the industry stopped using it."
Your role: you build a tiny model that predicts the next character of Kalpa's own review text, show the room what it forgets over long distances, and connect that failure to the tool Week 8 introduces.
On the table: how raw text becomes training data with no labels; how a model generates one step at a time; why order matters and where memory fails; why attention replaced recurrence.

### Thinking we train, before any tool

Text is a sequence, and the first networks built for sequences read one token at a time and carry a memory forward. Gates (the LSTM) decide what that memory keeps, which helps over moderate distances. A reader that runs one pass from each end is allowed only when the whole text is already in hand: in 'the light arrived cracked' and 'the light bag arrived cracked', only the words after 'light' say what it is, so a model classifying a finished review may read both ways, and a model writing the next word may not. An encoder-decoder pair reads the whole input into one summary and writes from it, and that single summary is a bottleneck.
Next-token prediction turns raw text into training data with no labels: every position is a question whose answer is the next token. Auto-regression generates one step at a time, feeding its own output back. Carried memory fails over long distances, which the room sees when the toy forgets an opening bracket by the closing one. Attention won because it reads the whole context at once instead of squeezing it through a sequence bottleneck. The concept map from neuron to next-token is the week's assessment, and it is the map Week 8 fills in.

### Trainer agenda

1. Kavya's ask; two review snippets where word order flips the meaning (10 min).
2. Text into numbers in one move: tokens as ids, ids as vectors; the sequence families on one map: recurrent, gated (LSTM, with GRU named), bidirectional, encoder-decoder, with the job each was built for (45 min).
3. Next-token prediction: the task that needs no labels; auto-regression feeding the output back; a tiny character model on review text (50 min).
4. Sequence memory and the long-range failure; the encoder-decoder bottleneck; why attention replaced recurrence, at intuition level (45 min).
5. Guided then unguided: the concept map from neuron to next-token, drawn and defended, with each family placed on it (40 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a recurrent network carries a memory forward, gates decide what it keeps, reading both ways needs the whole text in hand, an encoder-decoder pair squeezes its input through one summary, next-token prediction makes training data from raw text, and attention reads the whole context at once.
CAN DO: place the recurrent, gated, bidirectional and encoder-decoder families on one map with the job each was built for, trace an auto-regressive generation by hand, and draw the week-to-LLM concept map.
CAN HANDLE: the long-range failure told as evidence rather than history.
CAN DEFEND: why language models train on next tokens, in ninety seconds; a standing interview opener.

### Subtopics (technique in service of the scenario)

• Text into numbers in one move: tokens as ids, ids as vectors
• The sequence families on one map: the recurrent network, the gated network (LSTM, with GRU named), the bidirectional reader, the encoder-decoder pair
• Which family for which job: classifying a finished review against writing the next word
• Next-token prediction and auto-regression
• Sequence memory, the long-range problem and the encoder-decoder bottleneck
• Why attention replaced recurrence
• The concept map artifact

### Trainer notes

START FROM: everything this week; the bridge connects rather than adds. The sequence families are taught at recognition depth: one diagram and one job each.
GO AS FAR AS: everyone draws the map from neuron to next-token unaided, with the four sequence families placed on it.
STOP BEFORE: gate equations, training a recurrent network on real data, transformer internals; every named piece gets its day, starting tomorrow with tokens.
WHAT THE DATA REVEALS: the recurrent toy forgets the opening bracket by the closing one; the room states what a fix must do before attention is named.
CUT FIRST: the second generation trace, then GRU, which is named and not drawn. Never cut the concept map.

### Client zero data (TRAINER ONLY)

VERSION text: the reviews table enters; a tiny character-level model over Kalpa review text.
PLANTED: the long-range failure on a bracketed review.
The support tickets enter tomorrow.
The two 'light' sentences are board examples written by the trainer; they are not in the dataset.

### In-session exercises

GUIDED: one generation traced together, token by token.
UNGUIDED: the concept map drawn solo, then defended to a partner.
MID-SESSION (15 min each): order the pipeline cards from raw text to generated token; match four jobs (classify a review, translate a ticket, write the next word, tag each word) to the sequence family built for each.

### After-class tasks

• WATCH: the first half of Karpathy's bigram lecture.
• READ: the Week 8 pre-read on classical text lineage (TF-IDF, word vectors), shipped tonight.
• RECAP: why next tokens, ninety seconds, spoken to yourself.

### Interview angle

• [S] Why do language models train on next-token prediction?
• [S] RNN against LSTM: what problem does the gate solve?
• [SV] What is an encoder-decoder model, and one task it was built for?
• [F] What is the long-range problem, and why did transformers replace recurrent models?
• [F] When can a model read a sentence in both directions, and when can it not?
• [D] Marketing asks whether 'reading the reviews' is a solved problem; what do you say a model can and cannot do with text today?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Karpathy, Zero to Hero, the bigram language-model lecture (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• Jay Alammar, The Illustrated GPT-2, the auto-regression visual to redraw (verified 05 Sep 2026):
https://jalammar.github.io/illustrated-gpt2/
• Christopher Olah, Understanding LSTM Networks, the gate diagrams to redraw (verified 19 Sep 2026):
https://colah.github.io/posts/2015-08-Understanding-LSTMs/
• Dive into Deep Learning, bidirectional recurrent networks (verified 19 Sep 2026):
https://d2l.ai/chapter_recurrent-modern/bi-rnn.html
• Dive into Deep Learning, the encoder-decoder architecture (verified 19 Sep 2026):
https://d2l.ai/chapter_recurrent-modern/encoder-decoder.html

### Student references

• Karpathy playlist, the bigram lecture first half (verified 05 Sep 2026):
https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ

### Kahoot quiz plan

• Q1: next-token prediction needs what labels
• Q2: auto-regression feeds what to where
• Q3: the long-range problem in one line
• Q4: a finished review is being classified; may the model read both ways, and why
• Q5 trap: attention is faster because it is smaller, true or false
• Q6: place five cards on the concept map fast
• Return question from Wednesday: three seeds, three scores; what spread makes you distrust the result.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W7-4 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Recurrent networks from the inside: the recurrence equation, backpropagation through time, the gates of the LSTM, and why long-range gradients die.
PICKS UP WHERE THE ROW STOPS: the row teaches the sequence families at recognition depth and stops before the gate equations.
CONNECTS TO KALPA: the review whose meaning depends on a word forty tokens back, which sets up Week 8's attention.
BY THE END: a learner can write the recurrence, explain each LSTM gate's job, and say why attention removed the bottleneck.
DOES NOT REPEAT: the map of sequence families.

## Fri 20 Nov 2026 · Tokenization · What a ticket costs, and why the vendor bills by the token

### Business scenario of the day

Farhan Sheikh runs Kalpa Retail's customer support: two thousand tickets a day, forty agents, an average first reply of eleven hours. He has heard the data team can now read text. "If a model can read a ticket, can it draft the reply? What would that cost per ticket, and why does the vendor quote me by the token, whatever a token is?"
Your role: you explain to Farhan what a token is in his own tickets, cost one day's volume, and tell him why two vendors quote different prices for the same ticket.
On the table: how a model reads text when it cannot read words; why vocabularies exist; what a token count does to a bill and to quality; why the same ticket is longer for one model than another.

### Thinking we train, before any tool

Models read tokens, not words. A vocabulary is built from frequency, so common words are one token and a Kalpa product code shatters into five. Every token is billed, on the way in and on the way out, so tokenization is a cost decision as well as a modelling one, and two vendors with different vocabularies count the same ticket differently. Each token id then indexes one row of a learned table, and that row of numbers is what the network computes on; the 2017 transformer used rows of 512 numbers.
Farhan's question is the token economy in miniature, and it returns next Friday at scale.

### Trainer agenda

1. Farhan's ask; one ticket tokenized by two tokenizers, two counts (10 min).
2. From characters to subwords: why vocabularies exist and what BPE optimises (50 min).
3. Token counts drive cost and quality: one day of tickets costed (45 min).
4. Tokenizer families (word, character, subword; BPE, WordPiece and SentencePiece named) and what differences across models break; ids back to text, and ids into vectors (35 min).
5. Guided then unguided: the tokenizer demo on Kalpa tickets, one costed day, one explained surprise (55 min).
6. Kahoot and week close (20 min).

### Learner outcome

UNDERSTANDS: models read tokens, BPE builds a vocabulary from frequency, every token is billed, and vocabularies differ by model.
CAN DO: tokenize ticket text, count and cost a day's volume, and explain a surprising split.
CAN HANDLE: a product code shattered into five tokens, and two models disagreeing on the same ticket's length.
CAN DEFEND: to Farhan, why the vendor bills by the token and what that does to his budget.

### Subtopics (technique in service of the scenario)

• Characters, words, subwords: what each tokenizer trades
• BPE and vocabularies at intuition level; WordPiece and SentencePiece named
• Token counts against cost and quality
• Tokenizer differences across models
• The round trip: text to ids and ids back to text; ids into vectors through the embedding table
• The tokenizer demo on Kalpa tickets

### Trainer notes

START FROM: Thursday's bridge; tokens are what next-token prediction predicts.
GO AS FAR AS: everyone ships the tokenizer demo with one costed day of tickets.
STOP BEFORE: training a tokenizer, attention (Monday).
COMES LATER, all in Week 8: attention Monday, embeddings Wednesday with the classical lineage, decoding Thursday, economics Friday. Tuesday 24 November is Guru Nanak Jayanti.
WHAT THE DATA REVEALS: a Kalpa product code splits into five tokens and the count surprises; the room explains it from frequency.
CUT FIRST: the second tokenizer comparison. Never cut the costing arithmetic.
MODULE: this day belongs to Module 4, Natural Language Processing. It moved here from Week 8 Monday, because Guru Nanak Jayanti takes Week 8's Tuesday and Diwali no longer takes this week's Monday.

### Client zero data (TRAINER ONLY)

VERSION text: the support_tickets table enters, with the reviews from Thursday.
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
• [SV] Word, character or subword tokenization: what does each trade?
• [D] A support head asks whether an auto-reply is affordable; walk him from tokens to a monthly number.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Hugging Face LLM course, chapter 1 (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1
• Karpathy, Zero to Hero, the tokenizer lecture (verified 05 Sep 2026):
https://karpathy.ai/zero-to-hero.html
• Hugging Face LLM course, chapter 2, Tokenizers: word, character and subword (verified 19 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter2/4

### Student references

• Hugging Face LLM course, chapter 1 (verified 05 Sep 2026):
https://huggingface.co/learn/llm-course/en/chapter1/1

### Kahoot quiz plan

• Q1: models read what unit
• Q2: BPE merges by what signal
• Q3: a day of tickets is 1.2 million tokens at the price shown; cost it
• Q4 trap: same ticket, two models, two lengths; broken or expected
• Q5: one way to cut a ticket's tokens without cutting its complaint
• Return question from Thursday: why next-token prediction needs no labelled data, one line.

### IITGN faculty session (TENTATIVE)

TENTATIVE · IITGN faculty session W7-5 · 120 min · faculty to be confirmed by IITGN.
TOPIC: Tokenization as compression: byte-pair encoding worked step by step on a small corpus; cross-entropy and perplexity as the yardstick a language model is trained on.
PICKS UP WHERE THE ROW STOPS: the row explains what BPE optimises and stops before training a tokenizer.
CONNECTS TO KALPA: the product code that shatters into five tokens, and the two vendors whose counts disagree.
BY THE END: a learner can run three BPE merges by hand, and can explain perplexity in one sentence.
DOES NOT REPEAT: the costing of a day of tickets.

## Sat 21 Nov 2026 · Saturday recap · The pen-and-paper test, then the interview-answer discussion

### Business scenario of the day

The deep-learning week under questioning: the network, the loop, the sick runs, the bridge to text. Friday's tokens belong to next Saturday's paper.

### Thinking we train, before any tool

Saying the week out loud is the interview skill itself.

### Trainer agenda

Four hours, no new content.
1. Recap paper: pen and paper, AI-free, objective, from the 'Saturday papers' tab (110 min).
2. Break (20 min).
3. Marking: papers swapped and marked against the key, read out by the Academic TA (15 min).
4. Solution discussion led by the Academic TA: the most-missed items first, then the interview anchors answered aloud as interview answers, with random call-outs (70 min).
5. Doubts and the bridge: tickets and reviews as text, and the tool that reads them (25 min).

### Learner outcome

CAN DO: answer the week's business and technique questions on paper.
CAN DEFEND: any answer aloud; mark a peer's paper.
STATUS: ungraded; a performance indicator.

### Subtopics (technique in service of the scenario)

THE INTERVIEW ANCHORS (questions only):
• [S] What does an activation function do, and what happens without one?
• [S] Explain backpropagation to a non-expert.
• [S] Your loss printed nan; your first two moves.
• [F] Vanishing gradients: what they are, what signals them, and which activation choices cause or cure them.
• [F] Regularisation, dropout and early stopping: what does each brake?
• [S] Two runs of the same code give different numbers; what is missing?
• [F] Why did transformers replace recurrent models?
• [D] The network ties the logistic model on tabular data; what do you recommend, and what would change your answer?
• [D] When would you not use deep learning?
• [S] Sigmoid, tanh or ReLU: where does each sit, and why?
• [S] Write the weight update rule and say what each term does.
• [S] RNN against LSTM: what problem does the gate solve?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: an objective paper from the 'Saturday papers' tab: fill in the blank, true or false, one correct option, more than one correct option, scenario sets, applied maths and ordering, graded easy, medium and hard. Print the Item column only; the key, tag, role and anchor columns stay with the team.
MARKING: papers swap and are marked against the key, so a score is comparable across the room and from week to week.
DISCUSSION: the Academic TA opens with the most-missed items, then asks the interview anchors aloud as interview answers, with random call-outs.
STATUS: ungraded, AI-free by format; a performance indicator.

### Client zero data (TRAINER ONLY)

Answers cite the scenario net's own runs and the review-text toy.

### In-session exercises

THE PAPER: objective, pen and paper, AI-free: 53 items for a 110-minute slot (108 minutes at the assumed pace); items and key in the 'Saturday papers' tab.
• Fill in the blank: 9 items
• True or false: 8 items
• One correct option: 13 items
• More than one correct option: 6 items
• Scenario sets, each on one Kalpa situation: 10 items in 3 sets
• Applied maths, with the working shown: 5 items
• Order the steps: 2 items
• Difficulty: 20 easy, 25 medium, 8 hard. Roles served: GenAI, DS, FDE.
• Marking a peer's paper against the key.
• Random call-outs on the interview anchors: sixty seconds each.

### After-class tasks

• RECAP: the week's crux lines from memory.
• REST: Week 8 needs no new setup.

### Interview angle

The question set in Subtopics is the interview set for the week.

### Trainer resources

• The 'Saturday papers' tab holds the items and the key; this row's anchors are the source for the discussion.
• Interview Query, the deep-learning items (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions
• GeeksforGeeks, deep learning interview questions (verified 19 Sep 2026):
https://www.geeksforgeeks.org/deep-learning/deep-learning-interview-questions/
• Simplilearn, deep learning interview questions (verified 19 Sep 2026):
https://www.simplilearn.com/tutorials/deep-learning-tutorial/deep-learning-interview-questions

### Student references

• 3Blue1Brown, any lesson that felt shaky (verified 05 Sep 2026):
https://www.3blue1brown.com/?topic=neural-networks

### Kahoot quiz plan

None. The recap test and discussion replace the quiz.

### IITGN faculty session (TENTATIVE)

None. The Saturday block is the recap paper.

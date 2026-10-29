# The Mock R2 written sheet's key: what holds, why the rest fail, and how is it marked?

**TRAINER ONLY. PROPOSED marking**, since decision `rubrics-and-calendar` is open: Part A carries 1
mark an item, Part B 1.5 an item and Part C 2 an item, 15 in all, entered as three part scores on
the Mock R2 sheet of `C2_W06_D02_scoring_TRAINER.xlsx`. TA1 marks on Thursday evening.

Answers: 1b 2c 3a 4d 5a 6c 7d 8b

**What the sheet tests, and why on an invented book.** Week 4's metric design, lift and forecasting
baselines and Week 5's accuracy trap, cost threshold, prediction-time question, overfitting and
honest cross-validation, each applied to a card book. The book is a vendor's and every number is
invented, so no item hands a group a number from the Taiwan file or names anything the room finds
in it. The sheet is sat after the gate, so it cannot leak into a viva.

**Timing.** Part A six items at about 2 minutes, Part B two at about 2.5, Part C three at about 4,
which is 29 minutes, inside the 30.

## Which letter holds for each item, and why does each other option fail?

| Item | Key | Why it holds | Why the others fail | Taught in |
|---|---|---|---|---|
| 1 | b | Calling nobody gets the 1,600 payers right, 80 percent, and misses all 400 defaulters at 5 units each, 2,000 units | a reads the default rate as accuracy; c forgets the 5 units a miss costs; d counts only calls as costs | Week 5 Tuesday, the do-nothing matrix |
| 2 | c | Call when p x 5 is above (1 - p) x 1, so p above 1 / (1 + 5), about 0.17 | a is the accuracy line; b is 1 in 5, which drops the 1 in the denominator; d is 5 / 6, the ratio turned upside down | Week 5 Tuesday, what each mistake costs |
| 3 | a | Last month's statement exists on the 1st | b, c and d are all written after the list is built, so a model trained on them reads the future | Week 5 Wednesday, answers from the future |
| 4 | d | A random 200 holds 200 x 0.20 = 40 defaulters, and 110 / 40 = 2.75, the list's lift | a is the precision, 110 / 200, read as a ratio; b divides by a 40 percent base; c divides by a 10 percent base | Week 4 Wednesday, lift; Week 5 Tuesday, precision at k |
| 5 | a | Boosting falls 0.21 from training to validation and still ends below logistic's 0.76; logistic barely moves | b compares a training score with a validation score; c sets a bar nobody set; d hopes a gap closes in use, which it does not | Week 5 Thursday, memorising against learning |
| 6 | c | Pay tied to defaulters reached cannot be raised by calling the easy accounts | a and b are raised by quick calls to anyone; d is raised by keeping a payer on the line | Week 4 Monday, a metric that cannot be gamed |
| 7 | d | A scaler fitted on all rows has seen every held-out fold's values, so each fold's score is flattered | a is true of the labels and misses that the features leak; b reaches the right verdict for a false reason, since scaling never changes a label; c states a true fact that does not make the estimate honest | Week 5 Thursday, cross-validation done right |
| 8 | b | Bills: 0.50 is 60 + 240 x 5 = 1,260; 0.17 is 570 + 70 x 5 = 920; 0.17 is 340 units cheaper while less accurate | a and c defend a number that costs Rohan more; d is false, since accuracy at 0.17 is 68.0 percent | Week 5 Tuesday, where to draw the line |

The keys land on a twice, b twice, c twice and d twice. Item 1's key ties for the longest option,
item 3's is the shortest, and no key is the one longest option.

## How is Part C marked?

Two marks an item: one for the number with its unit, one for the working. A right number with no
working earns one.

| Item | The number | The working a marker checks | The plausible wrong number |
|---|---|---|---|
| 9 | 0.05 costs 1,430 units; calling everyone 1,600; the 0.05 list is 170 units cheaper | 1,800 called minus 395 defaulters = 1,405 wasted; 400 - 395 = 5 missed, x 5 = 25; 1,405 + 25 = 1,430. Everyone: 1,600 payers called = 1,600 wasted, 0 missed | 1,405 for the 0.05 list, which forgets the five missed defaulters |
| 10 | The model's list costs 1,400 units, the rule's 1,472; the model reaches 12 more defaulters, 72 units cheaper | Model: 300 - 150 = 150 wasted; 400 - 150 = 250 missed, x 5 = 1,250; 1,400. Rule: 300 - 138 = 162 wasted; 400 - 138 = 262 missed, x 5 = 1,310; 1,472 | "The model is 12 units better", counting defaulters as units |
| 11 | The model misses by 300 accounts, "same as last month" by 100; the naive forecast was better by 200 accounts | 22 - 19 = 3 points of 10,000 = 300; 22 - 21 = 1 point = 100 | 3 and 1 with no unit, or "the model is better because it is a model" |

## Which interview question does each item come from?

Questions only, with their tags, so a strong learner can practise the spoken version.

| Item | The question an interviewer asks |
|---|---|
| 1, 8 | "Your model is 85 percent accurate. Is that good?" [metrics, cost of errors] |
| 2 | "A false negative costs five times a false positive. Where does the threshold go?" [cost-sensitive threshold] |
| 3 | "Which of your features would not exist at prediction time?" [leakage, prediction time] |
| 4, 10 | "With a fixed budget of calls, which metric do you report?" [precision at k, lift, capacity] |
| 5 | "Your complex model wins on training data. Do you ship it?" [overfitting, model choice] |
| 6 | "How would you measure the team that acts on your list?" [metric design, gaming] |
| 7 | "Walk me through cross-validation without leaking." [validation, pipelines] |
| 9 | "Is the model better than doing the simple thing to everyone?" [baselines, error bill] |
| 11 | "What baseline does your forecast have to beat?" [forecasting, naive baseline] |

# Interview bank: overfitting, regularisation and the simpler model

Week 5, Thursday. 27 questions. Tags: [S] a staple asked everywhere, [F] frequent in global capability centre and product-company screens, [SV] a service-major screen opener, [D] a differentiator. The tags are this programme's own calibration for candidates with zero to three years of experience.

Each answer is a scaffold to reason from, never a paragraph to memorise: the 30-second version, the depth, what the interviewer listens for, the common wrong answer, and two follow-ups. Put your own numbers from this week's notebooks into every answer.

```mermaid
flowchart LR
    A["<b>Screening staples</b><br/>Q1 to Q8"] --> B["<b>Technical depth</b><br/>Q9 to Q17"] --> C["<b>Cases and scenarios</b><br/>Q18 to Q22"] --> D["<b>Client-facing</b><br/>Q23 to Q25"] --> E["<b>Behavioural</b><br/>Q26 and Q27"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class A,B,C,D,E known
```

## Screening staples

### Q1 [S] Overfitting: what it is, how you detect it, how you fix it.

- **30 seconds.** Overfitting is a model learning its training rows so closely that new rows surprise it. I detect it as a gap: a high training score beside a lower validation score, and I always put the baseline next to both. I fix it with a brake (a shallower tree, a stronger penalty) or more rows, and I check the fix on held-out rows.
- **The depth.** On the bank's file a tree with no depth limit scored 99.6 percent on training and 84.1 on validation, below the 88.7 of calling nobody. Its learning curves kept a 16-point gap from 988 to 19,769 rows, so more data did not help; capping depth at 6 closed the gap to under a point.
- **Listens for.** The gap read before the level; the baseline; a fix verified on held-out rows.
- **Common wrong answer.** "Use more data", with no check that the gap closes as rows grow.
- **Follow-ups.** "And if more rows had closed the gap?" (then the model lacked data, and rows are the cheaper fix). "How would you tell overfitting from a leak?" (a leak scores high on validation too).

### Q2 [S] Bias against variance in plain words.

- **30 seconds.** Bias is being wrong in the same way everywhere because the model is too simple. Variance is being wrong in a different way on every new sample because the model learned its training rows too closely. Reducing one usually raises the other, and the best model sits where validation error is lowest.
- **The depth.** On the bank's file a one-question tree sat at 11.3 percent wrong on training and validation alike: bias. The unlimited tree was 0.3 percent wrong on training and 16.5 on held-out rows: variance.
- **Listens for.** Two pictures, with how each looks in a pair of learning curves.
- **Common wrong answer.** "Bias is a prejudiced model." That is a different meaning of the word.
- **Follow-ups.** "Which one does a forest reduce?" (variance). "Which one does a stronger brake add?" (bias).

### Q3 [S] What is regularisation, and what do L1 and L2 do differently?

- **30 seconds.** Regularisation adds a price on large coefficients to the error a model minimises, so it trades a little fit on the training rows for stability on new ones. L2 shrinks every coefficient; L1 can set weak coefficients to exactly zero, so it also picks columns.
- **The depth.** On the bank's file L1 at C = 0.03 kept 20 of 63 one-hot columns and lost 0.0014 validation AUC against the model that kept 45.
- **Listens for.** The trade stated as a trade; the strength chosen on held-out rows.
- **Common wrong answer.** "It improves accuracy." It improves validation accuracy only when the model had variance to remove.
- **Follow-ups.** "When does regularisation not help?" (a model with little room to memorise, like logistic on 24,712 rows and 63 columns). "What do you do when two columns move together under L1?" (expect it to keep one almost by chance; read its picks with care).

### Q4 [S] What is k-fold cross-validation, and how do you choose k?

- **30 seconds.** The training rows are cut into k folds; each fold takes one turn as the exam while the others teach, and the score is the mean of the k exams with their spread. Five or ten is usual: more folds give each model more rows to learn from and cost more runs.
- **The depth.** On the bank's file five folds of about 4,942 customers each gave AUC 0.769 to 0.798, a mean of 0.786 with a spread of 0.014.
- **Listens for.** The spread quoted beside the mean; every learning step inside the folds.
- **Common wrong answer.** "It trains on more data." It is an estimation method; the final model is refit afterwards.
- **Follow-ups.** "What changes with 1,000 rows?" (the spread grows; on German Credit it was about 0.05). "When is shuffling wrong?" (Q16).

### Q5 [S] What is a learning curve, and what can it tell you?

- **30 seconds.** Two lines against the number of training rows: the error on the rows learned from and on held-out rows. A wide gap means variance, two close and high lines mean bias, and the slope says whether more data would help.
- **The depth.** The unlimited tree's gap barely moved from 988 to 19,769 rows (16.8 to 16.2 points), so more data was not its cure.
- **Listens for.** The slope read as a decision about buying data.
- **Common wrong answer.** Confusing it with a training-loss curve over epochs.
- **Follow-ups.** "What would make you ask for more data?" (a held-out curve still falling at the right edge). "What does a held-out curve below the training curve mean?" (usually noise or a small validation set; check the split).

### Q6 [S] Underfitting: how do you spot it and what do you change?

- **30 seconds.** Training and validation scores are both poor and close together, often near the baseline. I add capacity (a deeper tree, interactions), better columns, or loosen a brake that is too strong.
- **The depth.** Logistic at C = 0.0001 scored 0.763 AUC on training and 0.762 on folds; relaxing the brake to C = 0.01 lifted them to 0.788 and 0.784.
- **Listens for.** The baseline in the diagnosis; knowing a brake can cause it.
- **Common wrong answer.** "Collect more data."
- **Follow-ups.** "What if more capacity does not help?" (the columns may hold no signal; revisit the features). "How do you tell underfitting from a bug?" (a model below the baseline on training rows points at a bug).

### Q7 [S] A decision tree, a random forest and gradient boosting, one line each.

- **30 seconds.** A tree asks a chain of questions and can be read aloud. A forest grows many trees on resampled rows and columns and averages them, which lowers the variance of one deep tree. Boosting grows small trees in a chain, each aimed at what the chain still gets wrong.
- **The depth.** On the bank's file under five folds: tuned tree 0.782, forest 0.791, boosting 0.793, braked logistic 0.786.
- **Listens for.** What each does to a tree's weakness, and what it costs to explain.
- **Common wrong answer.** "Boosting is always best."
- **Follow-ups.** "Can a forest overfit?" (Q17). "Which would you show a committee?" (the one it can read, unless the gap pays for the other).

### Q8 [S] What is k-means, and when would you not use it?

- **30 seconds.** k-means groups rows by distance into k clusters with no answer column. Marketing uses it to name segments. I would not use it to predict an outcome, on unscaled columns, or when clusters are not round blobs.
- **Listens for.** Groups against predictions; scaling first.
- **Common wrong answer.** "To find who will buy."
- **Follow-ups.** "How do you choose k?" (try several, read how tight the groups are, and ask whether the business can act on k segments). "What happens without scaling?" (the column with the largest units decides the groups).

<div class="page-break"></div>

## Technical depth

### Q9 [F] Why cross-validation instead of one split?

- **30 seconds.** One split's score carries the luck of which rows landed in the exam. Cross-validation examines every row once and averages, so the score is about the model, and its spread tells me how much luck there was.
- **The depth.** Five deals of 8,238 bank customers moved AUC by 0.004; five folds of 4,942 moved it by 0.03. On five-customer exams of invented shoppers the score ran from 40 to 80 percent.
- **Listens for.** The spread used to judge whether a gap between models is real.
- **Common wrong answer.** "Because it uses more data for training."
- **Follow-ups.** "Then why keep a test set?" (cross-validation was used to choose, so its score is slightly optimistic; the sealed test is opened once). "What does it cost?" (k times the training time).

### Q10 [F] In scikit-learn's LogisticRegression, what does C do, and which way brakes harder?

- **30 seconds.** C is the inverse of the penalty strength, so a smaller C is a stronger brake. C = 100 nearly switches regularisation off.
- **The depth.** On German Credit's 800 rows, C = 0.1 scored 0.784 under five folds and C = 100 scored 0.756.
- **Listens for.** The direction, said without hesitation.
- **Common wrong answer.** "Raise C to regularise more."
- **Follow-ups.** "How do you choose C?" (cross-validate a log-spaced list). "Why does the best C differ between datasets?" (fewer rows per column, more room to memorise).

### Q11 [F] Your cross-validated AUC dropped when you moved preprocessing into a Pipeline. Which number do you report?

- **30 seconds.** The lower one. The earlier number let the exam folds help fit the preprocessing, so it was optimistic.
- **The depth.** On the bank's file the scaler leak was 0.00003 AUC, too small to see. Steps that learn from the answers, such as choosing columns by their link to y, leak far more.
- **Listens for.** Owning the drop as the fix.
- **Common wrong answer.** "Report the higher one; the model is the same."
- **Follow-ups.** "How would you explain the drop to a manager?" (the old number graded the model on rows that helped build it). "Which steps belong in the Pipeline?" (every step that learns from data).

### Q12 [F] Your learning curves show a wide gap that more data barely closes. What is going on, and what do you do?

- **30 seconds.** The model is memorising noise that more rows only add to. A brake fixes it; more rows of the same kind will not.
- **The depth.** The unlimited tree: gap 16.8 points at 988 rows and 16.2 at 19,769. Depth 6 with at least 50 customers per leaf: gap 0.2 points.
- **Listens for.** The flip of "more data cures variance".
- **Common wrong answer.** "Collect even more data."
- **Follow-ups.** "When would more data help?" (when the held-out curve is still falling). "Which brakes would you try first on a tree?" (max_depth and min_samples_leaf).

### Q13 [F] Why does an L1 penalty give a sparse model?

- **30 seconds.** The L1 price grows in a straight line from zero, so for a weak column the saving from a small coefficient never beats the price, and the best value is exactly zero. L2's price flattens near zero, so it shrinks without zeroing.
- **Listens for.** The use: L1 as a column chooser, and its limit with correlated columns.
- **Common wrong answer.** "L1 deletes the least important columns by rank."
- **Follow-ups.** "Would you use L1's picks as causes?" (no; they are choices under one penalty). "What is elastic net?" (a mix of both penalties).

### Q14 [F] What do you tune in a decision tree to control overfitting?

- **30 seconds.** max_depth, min_samples_leaf and min_samples_split, chosen on folds.
- **The depth.** On the bank's file depth 6 with at least 50 customers per leaf won the cross-validated loop at 0.782 AUC; the unlimited tree had 3,662 leaves, 63 percent holding one or two customers.
- **Listens for.** The leaf count read as memory.
- **Common wrong answer.** "The number of features."
- **Follow-ups.** "Why a minimum leaf size?" (each answer must cover enough customers to be a pattern). "How do you tune without a search framework?" (a plain loop over a small grid on the same folds).

### Q15 [F] How do you compare two models fairly?

- **30 seconds.** Same features, same folds, same metric, and the gap read fold by fold. Then I ask whether the gap is worth its cost in money.
- **The depth.** Boosting beat braked logistic on all five folds by 0.003 to 0.014 AUC on the bank's file; under a 5,000-nudge budget that was 0 to 133 extra buyers across folds.
- **Listens for.** Paired comparison; the second test.
- **Common wrong answer.** "Compare the means."
- **Follow-ups.** "What if the winner changes fold to fold?" (the gap is not real). "What metric for a budgeted campaign?" (precision in the top k).

### Q16 [F] When would you not shuffle before cross-validation?

- **30 seconds.** When rows run in time order and the model will score the future. Shuffling lets later rows teach a model graded on earlier ones; folds cut by time are the honest check.
- **Listens for.** Matching the split to how the model is used.
- **Common wrong answer.** "Always shuffle; it removes bias."
- **Follow-ups.** "What else breaks shuffling?" (several rows per customer: group the folds by customer). "What is it called in scikit-learn?" (TimeSeriesSplit, GroupKFold).

### Q17 [F] Can a random forest overfit?

- **30 seconds.** Yes. Averaging lowers the variance of one deep tree, and the forest can still fit noise or a leak, and still has to beat the baseline and the simpler model on the same folds.
- **Listens for.** Averaging understood as a reduction, never an immunity.
- **Common wrong answer.** "No, averaging prevents it."
- **Follow-ups.** "What would you tune?" (minimum leaf size, the share of columns per split). "What does a forest cost you?" (hundreds of trees to explain and monitor).

<div class="page-break"></div>

## Cases and scenarios

### Q18 [D] Your tuned model beats a simpler one by a point and costs ten times more to explain. Which ships, and how do you say it to a team that saw the 100 percent?

- **30 seconds.** I run two tests. Is the point real across the same folds, and is its gain, at the low end, worth more than what the complex model costs to run, monitor and explain? If either fails, the simpler model ships, and I name the gap at which I would switch.
- **The depth.** On the bank's file boosting won every fold (test 1 passed), and under the 5,000-nudge budget its low-end gain was about 42 buyers, Rs 51,000 a campaign, against an extra cost priced (as an assumption) at Rs 75,000, so logistic ships. To the room: "The 99.6 was the tree memorising last quarter's customers; this model is right on customers it has never seen."
- **Listens for.** The clarifying question about cost; the flip condition in rupees; naming the 99.6 openly.
- **Common wrong answer.** "Ship the higher score," or hiding the 99.6.
- **Follow-ups.** "The CMO insists on the higher AUC." (show the bill and the break-even). "What would you monitor?" (the hit rate in the top 5,000 against validation precision).

### Q19 [D] Training 99.6, validation 84.1, calling nobody 88.7. Walk me through your next hour.

- **30 seconds.** Name it as overfitting, worse than doing nothing. Check the split and the baseline, draw the depth curve and the learning curves, pick the depth from validation, re-score with five folds, and send the team the validation number with the baseline beside it.
- **Listens for.** An order of work, and the message to the team.
- **Common wrong answer.** "Switch to a neural network."
- **Follow-ups.** "What if the validation score were 99 too?" (suspect a leak first). "Who needs to hear about it today?" (whoever saw the 99.6).

### Q20 [D] "Boosting moved our AUC from 0.79 to 0.81. Should we deploy it?"

- **30 seconds.** First I ask: on how many folds, with what spread, and what does 0.02 AUC mean in the business's units against what boosting costs to run? The question as asked has no money in it, and the decision does.
- **Listens for.** Reading before answering; refusing to decide on AUC alone.
- **Common wrong answer.** "Yes, higher is better."
- **Follow-ups.** "Suppose it wins every fold." (then test 2 decides). "Suppose the extra cost is zero." (then it ships, with a monitoring owner).

### Q21 [D] You chose 30 features from 20,000 for 104 weekly points. How do you know the selection did not overfit?

- **30 seconds.** Run the whole selection inside folds cut by time, score held-out weeks, and compare with a seasonal baseline. Google Flu Trends ranked 50 million search terms against 1,152 data points and kept terms about high school basketball because basketball season is flu season.
- **Listens for.** Selection treated as part of training; time-aware folds.
- **Common wrong answer.** "The final model is simple, so it cannot overfit."
- **Follow-ups.** "What goes in the model card?" (how many candidates were tried and the held-out stretch). "What would L1 add?" (a penalty that keeps fewer terms).

### Q22 [D] A lending regulator asks why an applicant was refused. Which model do you ship?

- **30 seconds.** The model that can give a reason per applicant, unless the complex one wins fold after fold by more than the spread and a reason can still be produced for it.
- **The depth.** On German Credit the forest's mean beat logistic by 0.007 but won only two folds of five, so logistic at C = 0.1 ships. Caruana and others (KDD 2015) shipped a readable pneumonia model within 0.02 AUC of the black boxes because it could be checked and repaired.
- **Listens for.** The constraint stated before the model.
- **Common wrong answer.** "The forest; we can explain it later."
- **Follow-ups.** "What if the regulator accepts approximate reasons?" (re-run test 2 with that cost). "What QA check runs first?" (shuffled answers: AUC should fall to about 0.5).

<div class="page-break"></div>

## Client-facing and techno-functional

### Q23 [F] Explain overfitting to a marketing head in one minute.

- **30 seconds.** "A student who memorises last year's papers scores 100 on them and 61 on the new exam. Our first model did that with last quarter's customers: near perfect on them, worse than calling nobody on new ones. We now judge every model on customers it has not seen."
- **Listens for.** One picture, one number, the business consequence.
- **Common wrong answer.** The word variance in the first sentence.
- **Follow-ups.** "So how do I know the new number is real?" (it was measured five times on customers the model never saw). "What will it cost me if it is wrong?" (the error bill, Friday).

### Q24 [F] The CMO wants the deepest tree because it scored 99.6. What do you say?

- **30 seconds.** "That score is a memory test on customers we already know. On new customers that tree is wrong 15.9 percent of the time, more than the 11.3 of calling nobody. A depth-6 tree is wrong 10.1 percent of the time and ranks customers best, which is what the campaign needs."
- **Listens for.** Respect, numbers, the baseline, and the campaign's own goal.
- **Common wrong answer.** "You don't understand machine learning."
- **Follow-ups.** "Can't we just use both?" (one campaign, one list). "When would a deeper tree be right?" (when validation, not training, prefers it).

### Q25 [SV] Explain cross-validation to a client who has to sign off the score.

- **30 seconds.** "We tested the model five times, each time on a different fifth of your customers that it had not learned from. The score is the average, and the range tells you how much it could move on a new batch."
- **Listens for.** The range offered unprompted.
- **Common wrong answer.** A description of folds with no reason given.
- **Follow-ups.** "Why five?" (enough runs to see the range, at a cost we can afford). "Is the score guaranteed?" (no; the sealed test and monitoring after launch check it).

## Behavioural, with a technical core

### Q26 [S] Tell me about a time a model looked better than it was.

- **30 seconds.** Situation: this week a teammate's tree scored 99.6 percent on the bank's calls. Task: decide whether Kalpa's campaign could use it. Action: I scored it on 8,238 customers it had not seen (84.1, below the 88.7 of calling nobody), drew the depth curve, and braked it at depth 6. Result: validation error fell to 10.1 percent and the team now reports validation beside training.
- **Listens for.** "I" statements, numbers, and a change in how the team works.
- **Common wrong answer.** A story with no numbers or no action of your own.
- **Follow-ups.** "What would you do differently?" (put the baseline in the first message). "How did the teammate take it?" (share the curve, never the blame).

### Q27 [D] Tell me about a time you recommended the simpler option against pressure.

- **30 seconds.** Situation: boosting beat our logistic model on every fold and the room wanted it. Action: I priced the gain under the 5,000-nudge budget at about Rs 51,000 at the low end and asked what boosting would cost to run; at an assumed Rs 75,000 the simpler model shipped. Result: we agreed the switch rule in rupees, so the decision can change when the numbers do.
- **Listens for.** The flip condition agreed with the room.
- **Common wrong answer.** "I always prefer simple models."
- **Follow-ups.** "What if you had been wrong?" (the rule names when to switch). "Who owned the cost number?" (the platform team, with the business owner).

# The metric trap: interview question bank

Week 5, Tuesday. Twenty-eight questions with model answers. Tags follow the curriculum: [S] a staple asked everywhere, [F] frequent in product and global capability centre screens, [SV] a service-major screen opener, [D] a differentiator. Questions marked *beyond today* go past Tuesday's session and are here because interviewers ask them next.

Use each answer as a scaffold: say the 30-second version in your own words with your own numbers, then go one level deeper only when asked. Never memorise the paragraph.

| Section | Questions |
|---|---|
| Screening staples | Q1 to Q8 |
| Technical depth | Q9 to Q17 |
| ML case and scenario | Q18 to Q22 |
| Techno-functional and client-facing | Q23 to Q26 |
| Behavioural with a technical core | Q27 and Q28 |

## Screening staples: what does the first round check?

### Q1. [S] What is a confusion matrix? Read this one aloud: TP 174, FP 94, FN 754, TN 7,216.

**30 seconds.** It counts each pair of what the model said and what happened. Here, of 8,238 clients the model called 268; 174 of them bought and 94 did not; it left 7,970 alone, and 754 of those bought anyway.

**The depth.** Every classification metric is a ratio of these four cells. The dear cells depend on the business: here the 754 missed buyers cost about Rs 1,200 each, the 94 wasted calls Rs 40 each.

**Listens for.** Cells said as sentences about people; awareness that scikit-learn prints `[[TN, FP], [FN, TP]]`.

**Follow-ups.** "Which cell would you fix first?" (the 754, since each costs thirty times a wasted call). "What is the accuracy, and why is it not enough?" (0.897, against 0.887 for calling nobody).

**Common wrong answer.** Reading the top-left cell of scikit-learn's printout as the true positives.

### Q2. [S] From TP 120, FP 480, FN 280, TN 9,120, compute precision, recall and F1.

**30 seconds.** Precision: of the 600 flagged, 120 were right, 0.20. Recall: of the 400 real positives, 120 were flagged, 0.30. F1 is the harmonic mean, `2 x 0.2 x 0.3 / 0.5 = 0.24`.

**The depth.** Precision and recall share the numerator and differ in the denominator: the flagged column or the real row. F1 sits nearer the lower of the two.

**Listens for.** The sentence before the fraction.

**Follow-ups.** "Which matters more here?" (it depends on what each mistake costs; ask). "What is accuracy?" (0.924, which mostly counts the 9,120 easy negatives).

**Common wrong answer.** Precision as 120 of 10,000.

### Q3. [S] Accuracy is 96 percent on a 96 to 4 split. Is it a good model?

**30 seconds.** I cannot tell yet. Saying no to everyone also scores 96 percent on that split, so I would ask for the true-positive cell and the recall before anything else.

**The depth.** On an imbalanced outcome, accuracy rewards the model that never acts. On the bank campaign we used, calling nobody scored 88.74 percent and the model 89.71 percent, while recall was 0.188.

**Listens for.** The base rate named as the comparison, and one concrete cell asked for.

**Follow-ups.** "When would accuracy be fine?" (near 50:50 with the two mistakes costing about the same). "What would you report instead?" (recall and precision at the chosen line, or precision at k under a budget).

**Common wrong answer.** "96 percent is excellent, ship it."

### Q4. [S] Precision or recall for fraud, and why?

**30 seconds.** It depends on what a missed fraud costs against what a false block costs. If a block can lose a customer, precision leads; if a missed fraud costs far more than a step-up check, recall leads.

**The depth.** Stripe's own guide works a 26 dollar sale at 8 percent margin: a missed fraud costs 38.92 dollars, the profit of 18.71 good sales, so blocking pays once about 1 in 20 blocks is fraud (break-even precision 5.07 percent; Stripe, verified 28 October 2026). PhonePe writes that payments fraud must run "at very high precision", because a blocked genuine transfer is a customer who cannot pay (verified 28 October 2026).

**Listens for.** Two prices asked for before a metric is named.

**Follow-ups.** "And if a false block can be softened to an OTP check?" (the false-block price falls, so recall can lead). "What happens to the threshold for a high-margin merchant?" (it rises).

**Common wrong answer.** "Recall, always, because fraud is bad."

### Q5. [S] A screening test sends every positive for a cheap confirmation test. Precision or recall?

**30 seconds.** Recall. A false alarm costs one cheap confirmation; a miss leaves a sick person untreated.

**The depth.** The 1-in-N test makes it exact: if a confirmation costs Rs 500 and a missed case Rs 50,000, act above `500 / 50,500`, about 1 in 101.

**Listens for.** The cost asymmetry stated in numbers.

**Follow-ups.** "What if the confirmation test is invasive?" (a false alarm gets dear, the line rises). "How would you show the trade-off to a doctor?" (a table of lines with the misses and the false alarms counted per 1,000 patients).

**Common wrong answer.** "Accuracy, since it is a medical test and must be accurate."

### Q6. [SV] What is F1, and when is it the wrong single number?

**30 seconds.** The harmonic mean of precision and recall, which stays low if either is low. It is the wrong single number whenever the two mistakes cost different amounts, because it weighs them equally.

**The depth.** On the bank file the F1-maximising line is 0.154 and leaves a bill of Rs 599,680 at Kalpa's prices; the cost line at 0.032 leaves Rs 279,000.

**Listens for.** "Equal weights" said aloud.

**Follow-ups.** "What is F-beta?" (a weighted F that leans to recall when beta is above 1; a stepping stone, though prices are more honest). "When is F1 a fine choice?" (costs roughly equal and no budget).

**Common wrong answer.** "F1 balances precision and recall, so it is always the safe choice."

### Q7. [S] What threshold does scikit-learn's `predict` use, and why might it be wrong for you?

**30 seconds.** For a probabilistic classifier, `predict` returns the positive class when the predicted probability is above 0.5 (scikit-learn user guide, section 3.3, verified 28 October 2026). That line is right only when both mistakes cost the same.

**The depth.** For Kalpa's nudge the line from the prices is 0.032; for Rohan's loans it is 0.952 on P(repay). scikit-learn 1.9 offers `FixedThresholdClassifier` to set a line and `TunedThresholdClassifierCV` to tune one.

**Listens for.** The default named, and the business reason it moves.

**Follow-ups.** "Where would you store the threshold in production?" (one configuration value, versioned, never buried in code). "How do you test it?" (a row scored just above the line must act, one just below must not).

**Common wrong answer.** "0.5 is the correct probability cut-off."

### Q8. [SV] What is class imbalance, and how do you evaluate honestly under it?

**30 seconds.** One outcome is much rarer than the other, so a model can score high accuracy by ignoring it. Evaluate with the matrix, recall and precision at the chosen line, and precision at k when there is a budget.

**The depth.** Compare every score with the do-nothing rule: on an 11 percent outcome, doing nothing is 89 percent accurate.

**Listens for.** The do-nothing comparison.

**Follow-ups.** "What about resampling or class weights?" (*beyond today*: they change training, and they also inflate the probabilities, which breaks a cost-derived line). "Which split would you use?" (stratified, so each slice keeps the base rate).

**Common wrong answer.** "Oversample until 50:50 and accuracy is fine again."

## Technical depth: how, why and when?

### Q9. [F] How do you set a threshold when the two errors cost differently?

**30 seconds.** Price both mistakes and act when the probability of the good outcome beats `cost of acting wrongly / (cost of acting wrongly + cost of failing to act)`. For a Rs 40 nudge against a Rs 1,200 missed buyer that is 0.032, about 1 in 31.

**The depth.** The same rule as expected value per customer: nudge when `p x 1,200 > (1 - p) x 40`. It assumes honest probabilities, so check calibration or sweep the bill on validation and confirm the minimum sits near the formula.

**Listens for.** The derivation, the assumption, and a check.

**Follow-ups.** "What if the probabilities are not calibrated?" (sweep the threshold on validation and pick the cheapest). "What if there is a budget?" (the budget can bind first; then rank and take the top k).

**Common wrong answer.** "Tune it to maximise F1."

### Q10. [F] *Beyond today.* Your model was trained with `class_weight="balanced"`. Can you plug its probabilities into the cost formula?

**30 seconds.** No. Weighting the rare class pushes every probability up, so the formula's line no longer means what it says.

**The depth.** On the bank file the balanced model's mean prediction was about 0.42 against a true rate of 0.11, and the 0.032 line called 8,237 of 8,238 clients. Either train without the weighting for a cost line, or pick the line by sweeping the bill on validation.

**Listens for.** The link between training choices and the meaning of a probability.

**Follow-ups.** "What is calibration?" (a predicted 0.2 should come true about 20 percent of the time). "How would you check it?" (bin the predictions and compare each bin's mean with its observed rate).

**Common wrong answer.** "Balancing is always good for imbalanced data."

### Q11. [F] What is precision at k, and when do you report it?

**30 seconds.** The share of positives among the top k scored cases. Report it when a budget fixes how many you can act on: 1,000 calls, 250 fraud reviews.

**The depth.** On the bank file the top 1,000 by score held 404 buyers, precision 0.404, against 0.113 for a random 1,000. Flipkart and CMU reported their ratings-fraud model the same way: 211 of the top 250 flagged accounts were fraud (arXiv 1511.06030, verified 28 October 2026).

**Listens for.** The budget as the reason.

**Follow-ups.** "How does it move as k grows?" (falls, towards the base rate). "How do you pick k?" (from capacity, or from the cost line if it binds first).

**Common wrong answer.** "Precision computed at 0.5."

### Q12. [F] A new fraud model catches 40 percent more fraud. What do you check first?

**30 seconds.** Whether it was compared at the same alert volume. More alerts always catch more fraud; that is a threshold change.

**The depth.** Razorpay's engineering blog states the rule: detection is compared "at the same alert volume", because catching more by reviewing more "is a threshold change, not proof that the model improved" (10 September 2026, verified 28 October 2026). Cut both models to the team's review capacity and compare precision there.

**Listens for.** Equal-volume comparison, and capacity as the budget.

**Follow-ups.** "What if the labels arrive weeks late?" (recent positives are missing, so recent precision is understated; wait or estimate). "What else could explain the 40 percent?" (a different time window or base rate).

**Common wrong answer.** "40 percent more fraud caught, ship it."

### Q13. [F] Why does the F1-maximising threshold differ from the cost threshold?

**30 seconds.** F1 treats a false positive and a false negative as equal, while the cost line weighs them by price. With a 30 to 1 ratio, the cost line sits far lower.

**The depth.** Bank file at Kalpa's prices: F1's line 0.154 calls 1,226 and leaves Rs 599,680; the cost line 0.032 calls 7,438 and leaves Rs 279,000.

**Listens for.** A measured example, not only the principle.

**Follow-ups.** "When would they coincide?" (prices roughly equal, by accident of the data). "Which would you show a CFO?" (the cost line, with its bill).

**Common wrong answer.** "F1 is better because it is a standard metric."

### Q14. [D] When does a cost-derived threshold make the model barely matter?

**30 seconds.** When one action is so cheap that doing it for nearly everyone is close to optimal. At 30 to 1 on the bank file, the cost line called nine clients in ten and saved only 4.6 percent over calling everyone.

**The depth.** As the ratio tightens the model's edge grows: about 28 percent at 10 to 1 and 38 percent at 8 to 1. A budget flips it too: under 1,000 calls the ranking cut the bill by about Rs 3.6 lakh against a random list.

**Listens for.** The rule stated with its flip condition.

**Follow-ups.** "So should Kalpa skip the model?" (without a budget, nearly; with one, no). "What would you tell the team that built it?" (where its value is, with the number).

**Common wrong answer.** "A better model always matters."

### Q15. [F] *Beyond today.* What do the ROC curve and AUC measure?

**30 seconds.** The ROC curve plots the true-positive rate against the false-positive rate as the threshold sweeps from 1 to 0. AUC is the area under it: the chance that a random positive scores above a random negative.

**The depth.** AUC measures ranking and ignores the threshold and the prices, so it cannot choose a line. Monday's bank model has AUC 0.76. The IITGN faculty session on Tuesday (tentative) covers both curves.

**Listens for.** "Ranking, not a decision."

**Follow-ups.** "Two models with equal AUC: same decisions?" (no; their curves can cross where your line sits). "What does AUC 0.5 mean?" (ranking no better than chance).

**Common wrong answer.** "AUC is the accuracy of the model."

### Q16. [D] *Beyond today.* Why can AUC mislead on an imbalanced outcome, and when do you prefer a precision-recall curve?

**30 seconds.** With many negatives, a small false-positive rate is still a large number of false alarms, so ROC looks good while precision is poor. The precision-recall curve shows that cost directly.

**The depth.** On 7,310 non-buyers, a 10 percent false-positive rate is 731 wasted calls; even if 600 of the 928 buyers are caught, precision is 600 of 1,331, below one half. Stripe puts it as "The model controls the shape of the precision-recall curve" while the policy picks the point (verified 28 October 2026).

**Listens for.** Counts behind the rates.

**Follow-ups.** "What is the precision-recall baseline?" (the base rate). "Which curve for a 0.5 percent fraud rate?" (precision-recall).

**Common wrong answer.** "AUC is always the best single metric."

### Q17. [F] How do you prove the deployed scorer uses the threshold you chose?

**30 seconds.** A unit test that feeds a row scored just above the line and asserts it acts, and one just below that asserts it does not, plus a daily log of the count acted on and the cut-off.

**The depth.** If Kalpa's line silently reverted to 0.5, the daily calls would fall from thousands to about 3 percent of the list (268 of 8,238 on validation), which the log catches the first day.

**Listens for.** A test and a monitor, each with a number.

**Follow-ups.** "Who may change the threshold?" (the business owner, through a reviewed configuration change). "What else do you log?" (model version and the score distribution).

**Common wrong answer.** "Check that accuracy is unchanged."

## ML case and scenario: can you reason from the decision?

### Q18. [D] Marketing can afford 1,000 calls. Walk me from the score to the list.

**30 seconds.** Score every customer, rank by score, call the top 1,000, and report precision at 1,000 against the base rate with the bill beside it.

**The depth.** On the bank file the cost line wanted 7,438 calls, so the budget binds: the 1,000th score is 0.182, precision there is 0.404 against 0.113, and spend per buyer found is Rs 99 against Rs 147 at 2,000 calls. Keep a small random holdout if Marketing wants to measure the nudge's own effect.

**Listens for.** The binding constraint named; a number for the value.

**Follow-ups.** "The budget doubles: what changes?" (k doubles, precision falls, compare at equal k). "Who owns k?" (Marketing, with Finance).

**Common wrong answer.** "Use the cost threshold and call whoever clears it."

### Q19. [D] The same model in retail and in lending: why are the thresholds opposite, and how do you explain that to each business?

**30 seconds.** In retail the dear mistake is missing a buyer, so we act when P(buy) is above 0.032. In lending the dear mistake is approving a defaulter, Rs 60,000 against Rs 3,000, so we lend only when P(repay) is above 0.952.

**The depth.** Same formula, same quantity (the chance of the good outcome), opposite ends. To Rohan: "We lend only when at least 20 in 21 applicants like this one repay, because one default costs the interest on twenty good loans." To Marketing: "One buyer pays for thirty wasted nudges, so we nudge anyone with at least a 1 in 31 chance."

**Listens for.** Both lines said on the same quantity, and two audiences.

**Follow-ups.** "On a book where 30 percent default, what happens?" (on German Credit at 20 to 1, rejecting everyone nearly ties the model). "What would lower Rohan's line?" (a smaller loss after recoveries).

**Common wrong answer.** "Lending needs a more accurate model."

### Q20. [F] The churn model posts 97.1 percent accuracy. What do you ask?

**30 seconds.** First: what share churned in the window, and how is churn defined? If 2.9 percent churned, saying "stays" to everyone also scores 97.1.

**The depth.** Then ask for the matrix and the recall at the chosen line, and what a retention offer costs against a lost customer, so the line can be set.

**Listens for.** The clarifying question before any verdict.

**Follow-ups.** "Recall is 0.05. Now what?" (the threshold or the features need work; price the line first). "Which seat decides the line?" (the business owner, with the offer's cost).

**Common wrong answer.** "97 percent, great, launch."

### Q21. [D] A payments company has thin-margin and fat-margin merchants. One block threshold or two?

**30 seconds.** Two. The break-even precision depends on the margin, so the line moves per merchant.

**The depth.** Stripe's example: at 8 percent margin a missed fraud costs 18.71 sales' profit, break-even precision 5.07 percent. At 20 percent margin on the same 26 dollar sale it is 6.88 sales and about 12.7 percent, so the fat-margin merchant's line sits higher.

**Listens for.** The arithmetic redone, and the direction.

**Follow-ups.** "What does a false decline cost that the example leaves out?" (lost customers: 33 percent of consumers said they would not shop again after one, per Stripe). "Who configures per-merchant lines?" (a policy table owned by risk, versioned).

**Common wrong answer.** "One threshold keeps it simple."

### Q22. [F] The cost of a missed buyer halves. Recompute and say what changes.

**30 seconds.** The line rises from 1 in 31 to 1 in 16, from 0.032 to 0.0625, and the list shrinks.

**The depth.** On the bank file the calls fall from 7,438 to 5,233 and the model's saving over calling everyone grows from 4.6 to 14.0 percent. Recall still leads, less heavily.

**Listens for.** The direction first, then the numbers.

**Follow-ups.** "And if the nudge price doubles too?" (the ratio is back to 15 to 1 the same way; only the ratio matters to the line). "At what ratio does recall stop leading?" (when the two prices are equal).

**Common wrong answer.** "Halve the threshold."

## Techno-functional and client-facing: can you translate both ways?

### Q23. [F] Marketing wants one number for the dashboard. Which, and what sits beside it?

**30 seconds.** Precision at the day's call volume if a budget applies, otherwise recall at the chosen line; beside it the count acted on and the rupee bill.

**The depth.** One number without its cost is how 96 percent accuracy fooled everyone. The count makes the number checkable; the bill makes it priced.

**Listens for.** A refusal to show accuracy alone, without lecturing.

**Follow-ups.** "They insist on accuracy." (show it beside the do-nothing accuracy). "How often is it refreshed?" (daily, with the cut-off score).

**Common wrong answer.** "Accuracy, since everyone understands it."

### Q24. [D] Explain to the head of risk why his threshold is 0.95 and Marketing's is 0.03, in words he can repeat to his committee.

**30 seconds.** "Your threshold is set by your prices. A default costs you twenty good loans' interest, so the model approves only when at least 20 in 21 applicants like this repay. Marketing's mistake runs the other way, so its line sits at the other end."

**The depth.** Offer the table he will be asked for: at his line, approvals, defaults approved, good applicants turned away and the bill, against approving everyone and rejecting everyone.

**Listens for.** No jargon, and the numbers he can defend.

**Follow-ups.** "What if our loss on default is lower after recoveries?" (the line falls; give the new number). "Can the model be wrong?" (yes; the line says how wrong it may be before acting).

**Common wrong answer.** A lecture on probability calibration.

### Q25. [F] The CFO asks whether the model is worth it, at Rs 40 against Rs 1,200. What do you say?

**30 seconds.** Without a budget, barely: calling almost everyone costs only 4.6 percent more. With the 1,000-call budget, yes: it cuts the bill by about Rs 3.6 lakh in a slice of 8,238 clients against a random list.

**The depth.** State what the model costs to run and monitor, and the condition that would change the answer: a dearer nudge or a tighter budget.

**Listens for.** An honest "barely" with the flip condition.

**Follow-ups.** "Scale that to the whole base?" (state the assumption: the slice is representative). "When would you retire it?" (if the saving falls below its running cost).

**Common wrong answer.** "It is 90 percent accurate, so it pays."

### Q26. [SV] Explain precision and recall to a non-technical stakeholder, one sentence each.

**30 seconds.** Precision: of the people we contacted, how many were the right ones. Recall: of all the right people out there, how many we reached.

**The depth.** Add the trade: lowering the bar reaches more of the right people and contacts more of the wrong ones; the prices decide where the bar goes.

**Listens for.** Plain words and the trade.

**Follow-ups.** "Which one do I care about?" (ask what a wrong contact and a missed person cost you). "Can we have both high?" (only with a better model; the line trades one for the other).

**Common wrong answer.** Formulas read aloud.

## Behavioural with a technical core: what did you do, with what number?

### Q27. [S] Tell me about a time a number looked good and was misleading.

**30 seconds (STAR).** Situation: a propensity model reported 89.7 percent accuracy. Task: decide whether it was ready for a campaign. Action: I put the do-nothing accuracy (88.7 percent) and the matrix beside it and found recall 0.188. Result: we set the line from the prices and reported precision at the budget, 0.404 against 0.113.

**The depth.** Say what you did, in "I" statements, with your own numbers from the lab, and what you would do differently.

**Listens for.** A decision, a number, and the check you added.

**Follow-ups.** "How did the team react?" (name the disagreement and how the numbers settled it). "What check do you now run every time?" (the do-nothing comparison).

**Common wrong answer.** A story with no number in it.

### Q28. [D] A senior stakeholder insists the model be judged on accuracy. How do you handle it?

**30 seconds.** I agree to show accuracy, and I put the do-nothing accuracy and the bill beside it, so the gap is visible in their terms.

**The depth.** Then I ask what each mistake costs them and show the three models that tie on accuracy and differ by thousands of rupees. The decision moves to the bill without a fight over the metric.

**Listens for.** Respect for the stakeholder, and evidence over argument.

**Follow-ups.** "And if they still insist?" (record the decision and its risk, and set a review date). "Who else would you bring in?" (the business owner who pays the bill).

**Common wrong answer.** "I would explain that accuracy is a bad metric."

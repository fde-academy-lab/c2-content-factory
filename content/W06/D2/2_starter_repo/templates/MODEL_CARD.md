# Model card: __TODO__ your model's name

A model card is a short page shipped with a model, so whoever uses it knows what it is for, how it
was tested and where it fails. The nine sections below follow Mitchell and colleagues, "Model Cards
for Model Reporting" (2019), https://arxiv.org/abs/1810.03993 (checked 29 October 2026). Replace each
`__TODO__`; each example is written for Week 5's bank model and shows how long an answer runs.

## What is this model? (Model details)

__TODO__ Who built it, when, which version, which kind of model, and the data's citation and licence.

> Example: Logistic regression, version 1, built by the group for the bank's call list.

## What is it for, and what is it never for? (Intended use)

__TODO__ The decision it feeds, who uses it, and one use that is out of scope.

> Example: Ranks clients for a phone call about a term deposit; never for a decision about credit.

## Which groups of people could it treat differently? (Factors)

__TODO__ The groups you checked, and why each one matters for this decision.

> Example: Age bands, since a call list that skips older clients changes who hears the offer.

## Which numbers measure it, at which threshold? (Metrics)

__TODO__ The error bill and the model metric, the threshold or list size, and the spread across splits.

> Example: The bill of mistakes in rupees at a threshold of 0.032, beside the AUC.

## Which data tested it? (Evaluation data)

__TODO__ The test customers: how many, how they were chosen, and what was done to them first.

> Example: 8,238 clients held out by a stratified split with seed 42 and opened once.

## Which data trained it? (Training data)

__TODO__ The learning customers: how many, and how they differ from the test customers.

> Example: 24,712 clients from the same campaigns, split the same way.

## What are the results, overall and by group? (Quantitative analyses)

__TODO__ The bill against calling nobody and calling everyone, then the same numbers for each group.

> Example: Rs 279,000 against Rs 292,400 for calling everyone, on all 8,238 clients.

## What could go wrong for people? (Ethical considerations)

__TODO__ Who is harmed by each kind of mistake, and what the data holds that it should not.

> Example: A client called again and again bears the nuisance of every wasted call.

## What should a user know before trusting it? (Caveats and recommendations)

__TODO__ The limits, and what must be checked before the model is used on real customers.

> Example: Trained early and used late, the AUC fell from 0.80 to 0.66, so check it every month.

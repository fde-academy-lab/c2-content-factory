# The industry expert's brief: what should your Friday hour show a room building its first credit model?

**TRAINER ONLY.** Written to send to the industry expert before Friday, and for the Programme Head,
who hosts the hour. It names nothing the learners are meant to find in their data, so it can go to
the expert as it stands.

## Who will be in the room, and where are they in their week?

| | |
|---|---|
| The room | 39 trainee engineers in 13 groups of three, in week 6 of a 20-week programme, most of them new to any business role |
| What they built this week | A proof of concept on a public card book (30,000 Taiwanese cardholders, 2005, UCI, CC BY 4.0) for Kalpa Financial, a fictional Indian card issuer with no card history of its own: whom should the collections team call before the due date, when a missed default costs about five times a wasted call |
| What each group carries | One constraint card that changes its answer, such as a different cost ratio, a call capacity, a rule on written reasons or on attributes it may not use, or data that arrives late |
| What comes after your hour | The GD rounds the same day, the build frozen and run cold, and on Saturday a 12-minute talk with a live demo in front of a panel |
| Their weak spot | Explaining their own numbers, and the business around them; in their first build most of their talk time went on restating the problem |

## What do we ask you to show in 40 minutes?

One model you or your team took from proof to production, in credit, collections, fraud or any
decision where one mistake costs more than the other. Anonymise as your employer requires; no
client data on a slide.

| Minutes | Part | The question it answers for the room |
|---|---|---|
| 0 to 5 | The ask, in the business's words | What did the business actually ask for, and what decision did the score feed? |
| 5 to 12 | The proof | What did the POC have to prove, against which baseline, measured how, and what number got the next stage funded? |
| 12 to 20 | From proof to MVP | What did the first usable version add: the data feed, the reason for each decision, the person who acts on the score? |
| 20 to 30 | What broke | What went wrong after launch that validation had not shown: late labels, drift, a feedback loop, a broken feed, a segment that lost out? |
| 30 to 37 | What governance asked for | What did a validator, an auditor or a regulator ask for that the team had not built, and what did it cost to add? |
| 37 to 40 | The one number | The one number you would still defend from that project, and the sentence you said it in |

**What to leave out.** A tour of tools, code on screen, and claims about AI in general. The room
learns most from a wrong turn told in full: what the team believed, what showed it was wrong, and
what changed.

## Which questions will the room ask in the 20 minutes after?

Each group hands the Programme Head one question on paper by minute 35, and the Programme Head
asks them in the order below, calling first on learners who have not spoken this week. The question
kinds are known to the room in advance; these are the ones we expect.

| The kind of question | How a learner is likely to ask it |
|---|---|
| The proof | "When did you know the POC was good enough to fund the next stage?" |
| The baseline | "What simple rule did the model have to beat, and by how much did it?" |
| Late labels | "Defaults show up months later. What did you train on, and how did you check it?" |
| What production showed | "What did the first month in production show that validation did not?" |
| Explanations | "When a customer asked why, what did your system print?" |
| The off switch | "Who could stop the model, and did anyone ever stop it?" |
| Advice for Saturday | "What would you tell a team presenting its first credit model to a panel tomorrow?" |

## What happens around your hour?

| When | What | Who |
|---|---|---|
| Block one, minutes 0 to 40 | Your talk | You; the Programme Head keeps time and shows a card at 5 minutes left |
| Minutes 40 to 60 | The room's questions | The Programme Head picks questioners; TA1 collects the paper questions |
| Minutes 60 to 70 | A five-minute briefing on the GD, then the move to the GD rooms | The Programme Head |
| Block one minute 70 onward | GD room 1, seven rounds of 30 minutes across the day, if you have agreed to chair it (proposed) | You; the prompts and the scoring are in `C2_W06_D02_gd_prompts_TRAINER.md` |
| Saturday | Room B's panel, six talks of 20 minutes, if the Programme Head confirms it (proposed) | You, with TA1 scribing |

**Equipment.** A projector with HDMI and a spare adapter, your own laptop, and a microphone if the
room needs one. The hour is not recorded unless you agree to it.

## What can you lean on if you want a public example?

Each of these was checked on 29 October 2026; use any or none.

| Idea | Where it comes from |
|---|---|
| Putting a model into production can take up to 90 percent of the time and effort, by the author's own estimate | Ketan Doshi's blog, https://ketanhdoshi.github.io/Enterprise-ML-Prod/, checked 29 October 2026 |
| "Don't be afraid to launch a product without machine learning" and "Keep the first model simple and get the infrastructure right" (Rules 1 and 4) | Google, Rules of Machine Learning, https://developers.google.com/machine-learning/guides/rules-of-ml, checked 29 October 2026 |
| A production-readiness rubric of 28 tests in four sections, scored at the weakest section | The ML Test Score, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, checked 29 October 2026 |
| A card launched while its disputes system was "not fully ready", and the orders that followed five years later | CFPB, 23 October 2024, https://www.consumerfinance.gov/archive/newsroom/prepared-remarks-of-cfpb-director-rohit-chopra-on-the-goldman-sachs-and-apple-enforcement-press-call/, checked 29 October 2026 |
| Blocked payments never show their true outcome, so production precision needs counterfactual estimates | Stripe's engineering blog on Stripe Radar, https://stripe.dev/blog/how-we-built-it-stripe-radar, checked 29 October 2026 |

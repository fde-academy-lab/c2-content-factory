# Kalpa Financial Services

Payments and consumer lending. The unit where **the two errors cost different amounts**, and where
almost every label arrives late or never arrives at all.

> Code `FIN`. Introduced as a transfer domain once a concept has landed on the Retail spine, and as
> one of the five build-week sub-problems.

---

## 1. Who runs it, and what each of them wants

| Role | Measured on | What they want to hear | What they will resist |
|---|---|---|---|
| Head of Growth | Approved applications and disbursed volume | That approvals can rise | Any model that refuses more people this quarter |
| Head of Credit Risk | Loss rate on the book | That the book is safe | A loss number computed on a mature cohort rather than a growing one |
| Head of Fraud Operations | Chargebacks paid, and her analysts' workload | That the alert queue will fit in a day | An alert volume set by a probability threshold rather than by capacity |
| Head of Collections | Recovery rate by arrears bucket | That the new script works | A comparison that holds debt age constant |
| Compliance | Findings, and being able to explain a decision | That every decision has a reason a regulator will accept | A reasoning trace nobody has tested |

**The tension that generates most cards here:** growth is measured monthly and risk matures over a
year, so the person who wins this quarter is often the reason the next one is bad. Every honest
metric in this unit is a metric that makes somebody wait.

---

## 2. The data estate

| What exists | The catch it carries |
|---|---|
| Transactions, with a `chargeback_received` flag | The flag lands 45 to 90 days after the transaction, so recent data is labelled clean because nobody has complained yet |
| Analyst review logs, one disposition per reviewed case | Only cases the model surfaced were ever reviewed, so the labels describe the model's own past taste |
| Loan applications with bureau attributes at the time of application | Nothing at all for applications that were rejected |
| Repayment schedules and arrears buckets | Maturity differs by cohort, so a young book has a flattering loss rate by construction |
| Collections contact logs | The easiest bucket was contacted first, which confounds every before-and-after |
| The policy document estate | More than one version of some policies is live at once |

**The absence that defines the unit:** rejected applicants have no outcome. Every credit model in
the world is trained on people it approved, and evaluated on survivors. Naming that unprompted is a
strong interview signal.

---

## 3. The KPIs, and how each one is gamed

| KPI | What people say it is | The denominator that decides it | How it breaks or gets gamed |
|---|---|---|---|
| **Approval rate** | Approvals divided by applications | Which applications arrived, which is a partner's choice not yours | A partner changing its own pre-filter moves this number with nothing changing on your side |
| **Loss rate** | Defaults divided by disbursed | The **mature** book, cohort by cohort | Grow fast and the denominator outruns the numerator, so losses appear to fall while the book gets worse |
| **Fraud detection rate** | Caught divided by total fraud | Total fraud is unknown, since you only see what was reported | Prevention destroys its own labels: a blocked transaction never becomes a chargeback |
| **Alert precision** | True fraud among alerts | The **top N**, where N is what nine analysts can work in a day | A threshold of 0.5 is a number from a textbook. Capacity is the number from the business. |
| **Chargeback rate** | Chargebacks divided by transactions | Only settled months | The current quarter always looks like the best one on record |
| **Collections recovery** | Recovered divided by outstanding | Within an arrears bucket | Roll a new script out to the freshest arrears first and it will beat the old one every time |
| **Cost of an error** | Rarely stated at all | Rupees, on both sides | A blocked good customer leaves quietly and never appears in a fraud report. A missed fraud is visible, so it dominates the conversation and the model. |

**The KPI this unit exists to teach:** value recovered per analyst hour. It forces capacity,
precision and cost into one number that a Head of Fraud Operations can actually act on.

---

## 4. Case families, mapped to modules

| Module | Case family here | The teaching version |
|---|---|---|
| 1 Foundations of AI and Data | Approval and conversion rates across channels with different pre-filters | The denominator lesson with real stakes attached |
| 2 Applied Machine Learning | Fraud detection under extreme imbalance, credit scoring with asymmetric cost, reject inference | Ranking rather than classifying, and a threshold set from a capacity constraint |
| 3 Deep Learning and Neural Networks | Sequence models over a customer's transaction history | Where a feature-engineered baseline should be beaten before anything deeper is justified |
| 4 Natural Language Processing | Merchant name normalisation, dispute narrative classification | Messy short text with high business consequence |
| 5 and 6 Generative AI | Policy and product document retrieval for a servicing team | Where a corpus with two live versions of one policy is the whole lesson |
| 7 Production AI | Drift when underwriting policy changes, and monitoring a model whose labels lag 90 days | Detecting a change you cannot yet measure |
| 8 and 9 Agentic AI | Transaction monitoring and servicing agents, tool authorisation, step-up confirmation | `S-FIN-GA-02`, which is the hardest card in the bank |

---

## 5. The situations hosted here

| Page | Cards |
|---|---|
| [Analytics](Situations-analytics) | `S-FIN-AN-10` to `S-FIN-AN-12` |
| [Machine learning](Situations-machine-learning) | `S-FIN-ML-01` (five hundred alerts a day), `S-FIN-ML-04` to `S-FIN-ML-06` |
| [GenAI and agents](Situations-GenAI-and-agents) | `S-FIN-GA-02` (the agent that read the customer's email), `S-FIN-GA-08` to `S-FIN-GA-10` |

---

## 6. What Financial Services must never be used for

1. **Any real financial data, ever.** The repository is public. Every figure here is generated or
   invented, and it is labelled as such.
2. **A regulatory claim.** Cards can say a regulator would ask for an explanation. No card asserts
   what any actual regulation requires, because nobody in the build has verified it.
3. **A fairness case treated as a maths exercise.** `S-FIN-ML-05` exists because pincode and device
   reconstruct a protected attribute. That card needs a trainer who can hold the room, and it does
   not belong on a Week 5 teaching day.

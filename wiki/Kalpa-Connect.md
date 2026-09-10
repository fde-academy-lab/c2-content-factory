# Kalpa Connect

Mobile, broadband and subscription services. The unit where **the people who make a number look good
have already left**, and where almost every metric is a blend of populations that should never have
been averaged.

> Code `CON`. The home of survivorship, cohort mixing, and the gap between predicting something and
> being able to do anything about it.

---

## 1. Who runs it, and what each of them wants

| Role | Measured on | What they want to hear | What they will resist |
|---|---|---|---|
| VP Subscriptions | Blended retention, on a board slide | That retention improved and there is a reason to be proud of | A within-channel view that shows the improvement was a mix shift |
| Head of Acquisition | Signups this month, cost per signup | That the cheap channel is working | Being charged for what happens to those subscribers next year |
| Head of Retention | Saves, and offers accepted | That targeting the highest churn scores works | Being told the highest scorers have already decided |
| Network Operations lead | Incidents, and mean time to restore | That the network is stable | A definition of incident that cannot be reclassified |
| Head of Support | Containment and cost per contact | That the assistant handles ninety percent | A per-issue count that includes the customer's three retries |

**The tension that generates most cards here:** acquisition is measured monthly and retention over a
year, so a quarter can be won by buying subscribers who will churn after the reporting window
closes. Every survivorship card in the bank has its natural home in this unit.

---

## 2. The data estate

| What exists | The catch it carries |
|---|---|
| Signup date, plan, acquisition channel, cancellation date | Channel mix moves between cohorts, so the blended rate answers a question nobody asked |
| Usage and billing records | Involuntary churn from a failed payment sits in the same column as a decision to leave |
| Support tickets and chat transcripts | The transcripts record what agents said, including what they said wrongly, with no label for which |
| Network incident logs | What counts as an incident is a classification made by the team being measured |
| The plan catalogue, with historical versions | Plans were renamed, so a plan-level trend crosses a rename and looks like a shift in demand |

**The absence that defines the unit:** there is no record of which promotion ran on which channel.
Every before-and-after comparison in Connect is missing the one variable that would explain it, and
asking for it is the move.

---

## 3. The KPIs, and how each one is gamed

| KPI | What people say it is | The denominator that decides it | How it breaks or gets gamed |
|---|---|---|---|
| **Churn rate** | Cancellations divided by the base | The base at the **start** of the period, split voluntary from involuntary | Involuntary churn from failed payments hides inside the same number and has a completely different fix |
| **Retention by cohort** | Share still subscribed at month three | **Within channel**, cohort by cohort | Cut a cheap high-churn channel and the blended rate rises while total retained subscribers fall |
| **ARPU** | Revenue divided by subscribers | Which subscribers, and whether a suspended line counts | Suspending rather than cancelling keeps the numerator and shrinks the denominator |
| **Customer acquisition cost** | Spend divided by signups | Per channel, within an attribution window | A shorter attribution window makes any channel look better |
| **Lifetime value to CAC** | The health of the business | A forecast divided by a fact | LTV is a projection presented as a measurement, and its assumption is rarely written down |
| **Satisfaction** | How customers feel | Respondents, and the response rate | Nine percent response measures the people who still had the energy to answer |
| **Containment** | Contacts resolved without a human | Per **issue**, never per session | A customer who retries four times gives you three extra contained sessions |
| **Mean time to restore** | Incident response | Per incident, with a fixed definition of incident | Reclassify a long incident as three short ones |

**The KPI this unit exists to teach:** absolute retained subscribers alongside the rate. A rate can
improve while the business shrinks, and Connect is where a learner sees that happen with their own
hands.

---

## 4. Case families, mapped to modules

| Module | Case family here | The teaching version |
|---|---|---|
| 1 Foundations of AI and Data | Cohort retention, blended against within-channel, and the definition change in a release | `S-CON-AN-02`, the retention that improved because the unhappy left |
| 2 Applied Machine Learning | Churn prediction, the action window, uplift against propensity, plan recommendation | Predicting churn nobody can act on in time, then fixing the label rather than the model |
| 3 Deep Learning and Neural Networks | Usage sequences and anomaly detection on network telemetry | Where a threshold rule is the baseline that has to be beaten |
| 4 Natural Language Processing | Support ticket triage and routing | Class imbalance and a label taxonomy nobody agrees on |
| 5 and 6 Generative AI | Network incident summarisation, a plan-question assistant | An evaluation set built by the people who wrote the knowledge base, which is the trap |
| 7 Production AI | Guardrails, containment measured honestly, and a control that fails open | `S-CON-GA-16`, where blocks fell to zero for the wrong reason |
| 8 and 9 Agentic AI | Multi-agent escalation between triage, retention and billing | Where handoff between agents becomes the failure surface |

---

## 5. The situations hosted here

| Page | Cards |
|---|---|
| [Analytics](Situations-analytics) | `S-CON-AN-02` (the retention that improved because the unhappy left), `S-CON-AN-08`, `S-CON-AN-09` |
| [Machine learning](Situations-machine-learning) | `S-CON-ML-10` to `S-CON-ML-12` |
| [GenAI and agents](Situations-GenAI-and-agents) | `S-CON-GA-14` to `S-CON-GA-16` |

---

## 6. What Connect must never be used for

1. **A card whose twist is only arithmetic.** Simpson's paradox is a mechanism here, and a card that
   is nothing more than the paradox restated is a riddle rather than a situation.
2. **Real telecom data or any operator's published figures presented as Kalpa's.** Kalpa's numbers
   are invented and labelled as invented.
3. **The first survivorship lesson and the first cohort lesson on the same day.** They are the same
   idea wearing two coats, and a room needs to meet them a week apart.

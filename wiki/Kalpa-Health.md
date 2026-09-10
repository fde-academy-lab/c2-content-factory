# Kalpa Health

Diagnostic labs and clinic operations across India and South-East Asia. The unit where **a wrong
answer has a consequence that is not symmetric**, and where the correct behaviour is sometimes to
refuse.

> Code `HLT`. The home of refusal rules, late labels, and the difference between an output that is
> faithful and an output that is right.

---

## 1. Who runs it, and what each of them wants

| Role | Measured on | What they want to hear | What they will resist |
|---|---|---|---|
| Operations lead, diagnostic labs | Turnaround time and rejection rate | That this month is the best on record | A maturity cutoff that makes the current month unreportable |
| Clinic operations director | Slot utilisation and no-show rate | That empty slots can be predicted away | Arithmetic showing the calls cost more than the slots save |
| Clinical governance lead | Amendments, incidents, complaints | That nothing is being missed | Throughput arguments that trade accuracy for volume |
| Head of Claims | Claim acceptance rate and days to payment | That rejections are falling | A cohort view that shows the current month is simply incomplete |
| Head of Patient Support | Contacts handled, satisfaction | That an assistant can take the load | A refusal set that makes the assistant look less capable |

**The tension that generates most cards here:** clinical caution and operational throughput are both
legitimate, and they point in opposite directions. This is the unit where a learner has to say a
number is not the whole story to somebody whose job is the number.

---

## 2. The data estate

| What exists | The catch it carries |
|---|---|
| Sample registration and test completion timestamps | Rejections are recorded on average nine days after registration, and the lag differs by reason |
| Rejection reasons where present | No field says whether a sample is still in progress, so incomplete and clean look identical |
| Appointment records, booking time, clinic, slot | Operational fields such as `slot_released` are populated **after** the outcome and leak the target |
| Test panels and line items | Panels were unbundled into line items, so test counts and order counts moved in opposite directions |
| Report text, and amendments to reports | The amendment rate is the honest quality metric and nobody wants to own it |
| Claim submissions and adjudications | Right-censored in exactly the same way as rejections, one layer further out |

**The absence that defines the unit:** nothing records why a patient did not arrive. Every no-show
model is built on a target whose cause is unobserved, and every intervention changes the target it
was trained on.

---

## 3. The KPIs, and how each one is gamed

| KPI | What people say it is | The denominator that decides it | How it breaks or gets gamed |
|---|---|---|---|
| **Sample rejection rate** | Rejected divided by registered | Cohorts of samples with a **full maturity window** | Every month looks clean while it is running, and every closed month keeps rising for weeks |
| **Turnaround time** | Registration to report | Per test type, with send-outs separated, at a percentile | Exclude send-out tests and the number is excellent and meaningless |
| **No-show rate** | Missed appointments divided by booked | Booked, with reschedules counted once | A reschedule counted as both a no-show and a new booking double counts the denominator |
| **Slot utilisation** | Slots used divided by slots offered | Slots that could have been filled | Offer fewer slots and utilisation rises |
| **Repeat test rate** | Same test repeated within a window | Repeats that were not clinically intended | A repeat can be a quality failure or good medicine, and the data cannot tell you which |
| **Report amendment rate** | Reports corrected after issue | All issued reports | The one metric here that cannot be gamed upward, which is why it is the one to watch |
| **Refusal correctness** | Whether an assistant declined appropriately | A seeded set of questions it **should** refuse and a set it should not | Over-refusal is invisible to every grounding metric, and it is how staff stop using a tool |

**The KPI this unit exists to teach:** a rate reported only on settled cohorts. Once a learner
internalises that a running period is not comparable to a closed one, half the analytics traps in
the bank become visible on sight.

---

## 4. Case families, mapped to modules

| Module | Case family here | The teaching version |
|---|---|---|
| 1 Foundations of AI and Data | Rejection rate, turnaround time, no-show rate, and the maturity cutoff | `S-HLT-AN-03`, the month that always looks clean |
| 2 Applied Machine Learning | No-show prediction, escalation models, cost asymmetry between the two errors | `S-HLT-ML-02`, where the strongest feature is populated after the outcome |
| 3 Deep Learning and Neural Networks | Structured clinical sequences over a patient's history | Where a point-in-time feature set stops being optional |
| 4 Natural Language Processing | Claims document processing and referral note extraction | Short, high-consequence text with heavy abbreviation |
| 5 and 6 Generative AI | Report summarisation with strict refusal rules, patient support assistants | `S-HLT-GA-03`, and the checks that need no answer key |
| 7 Production AI | Version pinning, frozen regression sets, inter-rater agreement as a noise floor | An evaluation you can re-run on demand |
| 8 and 9 Agentic AI | An assistant that must escalate rather than answer, and how that boundary is enforced | Where "the prompt says not to" stops being a control |

---

## 5. The situations hosted here

| Page | Cards |
|---|---|
| [Analytics](Situations-analytics) | `S-HLT-AN-03` (the month that always looks clean), `S-HLT-AN-16`, `S-HLT-AN-17` |
| [Machine learning](Situations-machine-learning) | `S-HLT-ML-02` (the feature that already knew), `S-HLT-ML-14`, `S-HLT-ML-15` |
| [GenAI and agents](Situations-GenAI-and-agents) | `S-HLT-GA-03` (we changed nothing and it got worse), `S-HLT-GA-17` |

---

## 6. What Health must never be used for

1. **Clinical claims.** No card asserts what a test means, what a result implies, or what a
   clinician should do. Every card is about the operational system around the medicine.
2. **Any real patient data or anything resembling it.** The repository is public and this is the
   unit where that rule matters most.
3. **A regulatory assertion.** Cards may say a governance lead would ask for an audit trail. No card
   states what any actual regulation requires unless somebody has verified it and dated it.
4. **A first modelling lesson.** Consequence asymmetry needs a room that already trusts the trainer.

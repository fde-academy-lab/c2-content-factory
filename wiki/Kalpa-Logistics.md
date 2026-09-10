# Kalpa Logistics

Last-mile delivery and warehousing for every other unit. A cost centre that everybody blames,
measured on a promise it does not fully control.

> Code `LOG`. The home of **time, capacity and the tail**: censored outcomes, quantiles rather than
> means, and the long right-hand end of a distribution that nobody looks at.

---

## 1. Who runs it, and what each of them wants

| Role | Measured on | What they want to hear | What they will resist |
|---|---|---|---|
| Head of Last Mile | On-time percentage and cost per delivery | That the network is improving | A number that keeps undelivered orders in the denominator |
| Warehouse Operations Manager | Picks per hour, dispatch cut-off adherence | That the hub is efficient | A per-line comparison against a hub that handles a different mix |
| Head of Network Planning | Capacity against forecast | That the forecast was right | A forecast measured per hub per day rather than nationally per month |
| Head of Retail (as internal customer) | The delivery promise on the product page | An aggressive number, because it converts | A conservative quantile |
| Head of Customer Experience | Complaints about delivery | A number that predicts complaints | Being told the mean is not the thing that generates them |

**The tension that generates most cards here:** the promise shown to a customer is a commercial
decision with a cost on both sides, and it is made by a unit that does not carry the cost of missing
it. Logistics is where a learner first meets a question with two defensible answers.

---

## 2. The data estate

| What exists | The catch it carries |
|---|---|
| Order, dispatch and delivery timestamps | About four percent of rows have no delivery timestamp, and those are not missing data |
| Pincode, courier partner, weight band, status | Pincodes moved to a partner stop appearing in the dataset entirely |
| Exception codes on failed attempts | The code is chosen by the driver, and "customer unavailable" is the cheapest one to select |
| Driver location pings | High frequency, which tempts a system into replanning more often than a human can follow |
| Warehouse pick and pack times per line | Hubs handle different mixes, so per-hub averages compare different work |

**The absence that defines the unit:** nothing records whether a failed attempt was the customer's
fault or the driver's. The single most consequential field in last-mile operations is self-reported
by the person being measured.

---

## 3. The KPIs, and how each one is gamed

| KPI | What people say it is | The denominator that decides it | How it breaks or gets gamed |
|---|---|---|---|
| **On-time delivery** | Delivered by the promised date | Orders **delivered**, which quietly excludes orders never delivered | The worst outcomes leave the metric entirely, so the number rises as failures rise |
| **Average delivery time** | Mean hours from order to doorstep | Delivered orders only, and a mean rather than a quantile | A promise beaten half the time is broken half the time. The business needs a 90th percentile. |
| **First attempt success** | Delivered on the first visit | Attempts, as recorded by the driver | The exception code is the driver's choice |
| **Cost per delivery** | Total cost divided by deliveries | Per parcel or per order, and multi-parcel orders differ | Splitting an order into parcels improves the per-unit number and costs more in total |
| **Capacity utilisation** | Volume against capacity | Per hub, per shift | A national monthly average hides the two shifts a week that fail |
| **SLA by pincode** | Service level in a region | The pincodes still in the network | Move the slowest pincodes to a partner and the average improves with no operational change |
| **Exception rate** | Deliveries that went wrong | What counts as an exception | Reclassification is free and instant |

**The KPI this unit exists to teach:** a quantile with a stated confidence, and a separate estimate
of the probability of never arriving. Those two together are a promise. A mean is a wish.

---

## 4. Case families, mapped to modules

| Module | Case family here | The teaching version |
|---|---|---|
| 1 Foundations of AI and Data | On-time rates, delivery time distributions, the shape of a right tail | The first time a median and a mean tell different stories about the same file |
| 2 Applied Machine Learning | Delivery-time prediction with censoring, demand and capacity forecasting, slot optimisation | Quantile loss rather than squared error, and censored rows handled rather than dropped |
| 3 Deep Learning and Neural Networks | Sequence models over route and scan events | Where the extra capacity has to earn its place against a strong baseline |
| 4 Natural Language Processing | Address parsing and normalisation for Indian addresses | Accuracy measured on the addresses a human was employed to fix, not the easy ones |
| 5 and 6 Generative AI | Summarising a day's exceptions for a hub manager | An output whose only reader has ninety seconds |
| 7 Production AI | Latency budgets for a driver app, and a p99 that a median hides | Where a service level stops being a model metric |
| 8 and 9 Agentic AI | Exception-handling agents, replanning, and the constraint that a human needs a stable plan | Autonomy limited by human tolerance rather than by capability |

---

## 5. The situations hosted here

| Page | Cards |
|---|---|
| [Analytics](Situations-analytics) | `S-LOG-AN-13` to `S-LOG-AN-15` |
| [Machine learning](Situations-machine-learning) | `S-LOG-ML-03` (the orders that have not arrived yet), `S-LOG-ML-13` |
| [GenAI and agents](Situations-GenAI-and-agents) | `S-LOG-GA-11` to `S-LOG-GA-13` |

---

## 6. What Logistics must never be used for

1. **A first lesson in modelling.** Censoring and quantile loss are hard, and a room meeting its
   first model should not meet them on the same day.
2. **A route optimisation that becomes an operations research course.** The teaching point is the
   constraint nobody wrote down, and the algorithm is not the subject.
3. **Blaming a driver.** The exception-code card is about a measurement system that asks the
   measured party to report on itself. That is a systems point, and it stays one.

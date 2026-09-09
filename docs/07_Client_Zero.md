# CLIENT ZERO
## The one company every example in the programme lives inside

**Status: PROPOSED.** Change to LOCKED with a name and date on sign-off, after which every day pack builds against this file and nothing in it changes without a versioned edit.

Locked by: ______  Date: ______

Client zero is fictional. Any resemblance to a real company is coincidental, and the disclaimer travels with the name wherever it is printed.

---

## 1. The company

| Field | Value |
|---|---|
| Name | Kalpa Group, spoken as "Kalpa" in class |
| What it is | A diversified global conglomerate with five business units in five industries, headquartered in Singapore, with its largest engineering and data centre in Bengaluru |
| Where the cohort sits | The Data and AI team inside Kalpa's Bengaluru global capability centre, which serves all five business units |
| Business model, said from memory | Kalpa runs five businesses that share one customer base and one data platform. Each business unit owns its operations; the Bengaluru centre owns the data, the models and the AI systems that every unit runs on. The cohort is that centre's newest team. |
| Why this shape | It matches the Indian market the cohort is placed into, where most data and AI roles sit inside global capability centres serving several business lines, and it lets a learner grow inside one company for twenty weeks instead of re-orienting to a new firm every session. |

## 2. The five business units

One unit carries the teaching spine. The other four exist for build weeks, so learners tour the whole company at rising technical depth while the daily teaching never changes domain.

```mermaid
flowchart LR
    K[Kalpa Group<br/>Bengaluru Data and AI team]
    K --> R[Kalpa Retail<br/>spine vertical]
    K --> F[Kalpa Financial Services]
    K --> L[Kalpa Logistics]
    K --> H[Kalpa Health]
    K --> T[Kalpa Connect<br/>telecom and subscriptions]
```

| Unit | Business in one line | Interview-classic case families it hosts in build weeks |
|---|---|---|
| Kalpa Retail | Online and in-store consumer commerce across India and South-East Asia | Basket analysis, returns, customer lifetime value, demand forecasting, product search and support assistants |
| Kalpa Financial Services | Payments and consumer lending | Fraud detection under imbalance, credit risk scoring with asymmetric error cost, transaction monitoring agents, policy document retrieval |
| Kalpa Logistics | Last-mile delivery and warehousing for all units | Delivery-time prediction, demand and capacity forecasting, route and slot optimisation, exception-handling agents |
| Kalpa Health | Diagnostic labs and clinic operations | Appointment no-show prediction, claims document processing, patient support assistants with strict refusal rules |
| Kalpa Connect | Mobile, broadband and subscription services | Churn prediction, plan recommendation, support ticket triage, network incident summarisation |

Every build week draws its five sub-problems one from each unit, each morphed from a case the Indian market actually interviews on, so a learner meets fraud, churn, no-shows, delivery times and baskets in the same company rather than in five unrelated datasets. Three groups take each sub-problem, so the panel hears alternate viewpoints on the same business problem back to back.

## 3. The entity model, Kalpa Retail

This is the world the teaching spine lives in from Week 1 to Week 15, re-expressed as the toolset grows: a list of dictionaries in Python, files on disk, tables in Postgres, a DataFrame in pandas, a feature table for models, and a document corpus for retrieval. The records stay recognisably the same throughout, which is what makes each new tool land.

```mermaid
erDiagram
    CUSTOMERS ||--o{ ORDERS : places
    CUSTOMERS ||--o{ EVENTS : generates
    ORDERS ||--o{ ORDER_ITEMS : contains
    ORDERS ||--o{ PAYMENTS : settled_by
    PRODUCTS ||--o{ ORDER_ITEMS : appears_in
    CUSTOMERS {
        string customer_id PK
        string segment
        string city
        date signup_date
        string loyalty_tier "optional, absent on a known subset"
    }
    ORDERS {
        string order_id PK
        string customer_id FK
        date order_date
        number amount "Rs"
        string channel "app, web, store"
        string status "delivered, returned, cancelled"
    }
    ORDER_ITEMS {
        string order_id FK
        string product_id FK
        int quantity
        number unit_price
    }
    PAYMENTS {
        string payment_id PK
        string order_id FK
        number amount_paid
        string method
        timestamp paid_at
    }
    PRODUCTS {
        string product_id PK
        string category
        number list_price
    }
    EVENTS {
        string customer_id FK
        string event_type "visit, search, add_to_cart, checkout"
        timestamp event_ts
    }
```

Segments are four: Retail-Core, Retail-Plus, Business and Student. Amounts are in Rs; a typical order sits between Rs 800 and Rs 3,000.

## 4. The spine dataset, version by version

The same records, growing in shape and dirtiness as the curriculum needs them. Every version is generated deterministically from one seed so all sixty learners hold identical data, and every planted defect is a witness for exactly one teaching point.

| Version | First used | Shape | Planted witnesses |
|---|---|---|---|
| v0 | Week 1, Monday | About 30 flat order records loaded by a setup cell, each with order_id, customer segment, amount, status and order_date, and a nested customer sub-record on some | One amount stored as the text "4500" (the type break); the optional field discount absent on a known subset (the KeyError and .get() lesson) |
| v1 | Week 1, Tuesday to Thursday | 50 records, first as a Python list, then as orders.csv and orders.json | One amount spelled "twelve"; one record missing a required field; a near-duplicate pair sharing an order_id with one differing timestamp; one whale order of Rs 480,000; a Student segment of exactly 12 records so sample size bites; a truncated line in the JSON; a companion file with the header row duplicated |
| v2 | Week 2, Tuesday to Thursday | 1,000 orders and their customers as Postgres tables, plus a payments table | 50 orders with two payments each so a LEFT JOIN grows 1,000 rows to 1,450 and revenue doubles; a handful of orphan rows on each side; exact ties in amount so RANK returns 1, 1, 3; a segment composition that reverses at segment level for the Simpson demonstration |
| v3 | Week 2 Friday, Week 4 | The same tables plus order_items, products and events, and a monthly volume series | One very popular product that yields confidence 0.82 at lift 0.97 (the confidence trap); a growing new-cohort mix that holds blended retention flat at 41 percent while every cohort declines; one funnel stage whose drop is a denominator artefact |
| v4 | Week 4 Friday, Week 5 | The feature table per customer with a provided propensity score column and the modelling target | The return flag as the target at roughly 96 to 4 imbalance; a settlement_status field set after the outcome, which leaks; one curved relationship so residuals bow; two correlated features so a coefficient sign flips when both are included |
| corpus | Weeks 11 and 12 | Kalpa Retail's document estate: returns and refunds policy, delivery terms, the customer support playbook, product manuals, and a bank of anonymised support tickets | Two policy documents that contradict on one clause (the correct-source wrong-answer failure); a question the corpus cannot answer (the refusal lesson); a product manual that mentions a term found nowhere else (the grounding check) |

Build weeks do not use this dataset. They use real, messy data at scale, re-labelled into the Kalpa unit that hosts the sub-problem, because no concept is being taught for the first time and real data is what the brief rewards.

## 5. The metrics the cohort computes again and again

These recur from Week 1 through the capstone, each first done by hand and then automated by the next tool, so the answer is always already known before the new tool arrives.

| Metric | First computed | Returns in |
|---|---|---|
| Orders and revenue by segment | Week 1, plain Python | SQL in Week 2, pandas in Week 2, the feature table in Week 5 |
| Average order value, mean against median | Week 1 Thursday | The stakeholder sentence in Week 2, forecasting in Week 4 |
| Return rate with its denominator | Week 1 Thursday | The modelling target in Week 5 |
| Conversion through the funnel | Week 4 Thursday | Agent evaluation in Week 14 as a cost-per-task analogue |
| Retention by signup cohort | Week 4 Thursday | The churn family in Kalpa Connect build weeks |
| Basket lift | Week 4 Wednesday | Recommendation cases in Kalpa Retail build weeks |
| Cost per run of an AI feature | Week 8 Friday | Every agent and retrieval build from Week 12 onward |

## 6. Domain discipline

- The teaching spine is Kalpa Retail throughout. Teaching weeks never change domain.
- The sanctioned domain excursions are the second-example transfer moments in the doctrine, and they map to the other four units: when a session needs a transfer example after the concept has landed, it draws from Kalpa Financial Services, Logistics, Health or Connect, never from an outside company.
- Build weeks tour the units by design, one sub-problem per unit, and are the only place real data appears.
- Case studies about real companies remain welcome in trainer notes and slides as dated, verified references; they never replace Kalpa as the example the room computes on.

## 7. How the world is introduced

Day 1 opens on Kalpa as a story before any code runs: who the company is, what the five units sell, where the cohort's team sits, and the entity picture drawn on the board. The learner should be able to draw the company from memory by the end of Week 1, because every example for the next nineteen weeks lands inside it. The Day 1 introduction pack carries this narrative and is built only after this file is marked LOCKED.

## 8. What this lock produces next

1. `data/generate_client_zero.py` in the repository: one seeded generator that writes every version in section 4 with its witnesses, so the day packs read data rather than invent it.
2. The Day 1 introduction pack.
3. The Build 1 sub-problem set: five briefs, one per unit, each morphed from an interview-classic case into the Kalpa persona.

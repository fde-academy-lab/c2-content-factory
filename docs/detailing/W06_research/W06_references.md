# Week 6 references: from a vague lending ask to a working ML pipeline

Every link below was fetched on 29 October 2026 from this session, directly, through the session's standard outbound proxy. No reader mirror, cache, archive copy, paywall bypass or login was used. Where a site answered with a block, a paywall, a login wall or a human-verification page, the block is recorded and the item is marked "not verified". Numbers are quoted only where the text was read on the page itself; a search-engine excerpt alone never counts as verification.

Status words used in this file:

| Status | Meaning |
|---|---|
| Verified 29 Oct 2026 | The page or PDF was fetched today and the fact was read in its text |
| Not verified | The page could not be read today (reason given), or the fact was seen only in a search excerpt |
| [India] | An Indian case, regulator or rule |

## 1. What happened to the requester's eight references?

All seven medium.com links and the one towardsdatascience.com link answered HTTP 403 from Cloudflare's bot check on 29 Oct 2026, both to a direct fetch and to the WebFetch tool. The 403 came from the site, not from the session proxy (the proxy logged no relay failure). Towards Data Science now publishes on its own domain, and the same articles at towardsdatascience.com also answered 403. KDnuggets, which carries a republished copy of reference 3, answered 403 too. None of these blocks was worked around.

| # | Requested URL | Result 29 Oct 2026 | Author's own open version | Status |
|---|---|---|---|---|
| 1 | medium.com/@allanouko17/customer-churn-prediction-using-machine-learning-ddf4cd7c9fd4 | 403 (Cloudflare) | None found. github.com profile pages cannot be read from this session (the session's GitHub access is limited to its configured repositories), and search found no repository under that handle | Not verified |
| 2 | medium.com/data-science-collective/stop-guessing-who-will-leave-how-i-would-predict-customer-churn-before-it-happens-300d34cbd13c | 403 (Cloudflare) | Author not identified by search; no open version found | Not verified |
| 3 | medium.com/data-science/predict-customer-churn-the-right-way-using-pycaret-8ba6541608ac | 403 (Cloudflare); KDnuggets repost also 403 | Search listings name Moez Ali, the PyCaret founder, as author (not verified on a page). The PyCaret repository's churn notebook (examples/PyCaret 2 Customer Churn Prediction.ipynb, tag 3.0.0.rc8, read from raw.githubusercontent.com) is by a different author, Alexandre Farias, so it is not the author's own version and is not used | Not verified |
| 4 | medium.com/@muralisuvvani/end-to-end-machine-learning-pipeline-from-raw-data-to-deployment-624e700f6992 | 403 (Cloudflare) | None found | Not verified |
| 5 | medium.com/data-science/enterprise-ml-why-building-and-training-a-real-world-model-is-hard-59d09a430fae | 403 (Cloudflare) | Yes: Ketan Doshi's own blog, https://ketanhdoshi.github.io/Enterprise-ML/ (16 Jun 2021), same title and series | Verified 29 Oct 2026 (blog). The Towards Data Science byline itself could not be read |
| 6 | medium.com/@armankamran/success-factors-for-enterprise-machine-learning-projects-fa3009e7493b | 403 (Cloudflare) | None found | Not verified |
| 7 | medium.com/data-science/enterprise-ml-why-getting-your-model-to-production-takes-longer-than-building-it-e44ef80f8969 | 403 (Cloudflare) | Yes: Ketan Doshi's own blog, https://ketanhdoshi.github.io/Enterprise-ML-Prod/ (28 Jun 2021). The blog title reads "putting your model in production"; a search excerpt of the Towards Data Science page carries the same "up to 90%" sentence as the blog | Verified 29 Oct 2026 (blog) |
| 8 | towardsdatascience.com/what-ive-learnt-building-a-machine-learning-project-for-a-medium-sized-enterprise-ef6960f99bee/ | 403 (Cloudflare) | Author not identified; no open version found | Not verified |

### What reference 5 gives (Ketan Doshi's own blog, verified 29 Oct 2026)

Source: https://ketanhdoshi.github.io/Enterprise-ML/ (checked 29 Oct 2026). Licence not stated on the page, so link and paraphrase only.

1. A demo project starts from a cleaned, labelled, scoped dataset; a real project starts from a blank slate, and finding the data, sourcing the labels and cleaning garbage values ("Unknown" in a churn-reason field is his example) becomes one of the hardest tasks.
2. Someone has already framed a demo problem. In a real project the team must first find the problem and agree the business objective.
3. On a leaderboard, 79.0345 against 79.0312 can move a team hundreds of ranks. In a real project, weeks spent for a one or two percent metric gain may not be worth it, because accuracy is only one factor in the business outcome; shipping a working version, getting feedback and iterating usually matters more.
4. The model-building loop has ten named steps (data discovery, cleaning, EDA, feature engineering, feature selection, model selection, tuning, training and evaluation, inference, repeat), and each trial's features, hyperparameters and metrics should be logged so results can be compared and reproduced.
5. ML work is uncertain: feasibility and timelines are partly guesswork, and the notebook-on-a-snapshot model is cut off from the company's applications and data pipelines, which is where the next hurdle sits.

### What reference 7 gives (Ketan Doshi's own blog, verified 29 Oct 2026)

Source: https://ketanhdoshi.github.io/Enterprise-ML-Prod/ (checked 29 Oct 2026). Licence not stated, so link and paraphrase only.

1. Building the model is "only the tip of the iceberg"; in his experience the second stage, putting it into production, can take up to 90% of the time and effort. This is the author's own estimate, not a measured figure.
2. A model goes into two production environments: one for serving (real-time or batch inference) and one for retraining on fresh data from the warehouse.
3. Integration has two halves: application integration (the model sits inside a business flow, behind an API or a function call, with agreed formats and validation) and data integration (live inference cannot use a static CSV; it needs current data from databases, logs and APIs, with access control, masking of personal data and format handling).
4. Monitoring watches both DevOps signals (latency, uptime) and model quality on live data, sliced by segment, because data drift degrades a model quietly.
5. Five roles meet in one project: data scientist, data engineer, application developer, ML engineer and MLOps. Batch inference is his named example of weekly churn scores driving promotions.

### What the other six references are said to contain (not verified)

For reference 8, a search-engine excerpt shows two lessons: the author was too attached to the CRISP-DM process and lost sight of the real goal of finding potential customers, and early results were presented as confusion matrices when stakeholders cared about what the work achieved. For reference 3, search excerpts say the article treats retention as a subscription business KPI and argues that AUC, accuracy and recall may not suit a churn model whose purpose is a business return. Neither was read on the page, so neither should be taught as the author's words. The PyCaret documentation page that shows how to add a custom metric (add_metric) was read today at https://pycaret.gitbook.io/docs/get-started/functions/others (checked 29 Oct 2026) and is enough to replicate a "profit instead of AUC" metric in class; note that the PyCaret repository's LICENSE now reads "Functional Source License, Version 1.1, MIT Future License" (read 29 Oct 2026), so its code is not plain MIT today.

## 2. Which open references teach the same arc, and what may we do with each?

"Link only" means no licence permitting reuse was found on the page; we may link, cite and paraphrase, and quote a sentence with attribution, but we should not copy figures or text into the repository.

| Reference | URL (checked 29 Oct 2026) | What it gives a weak learner | Licence and what we may do |
|---|---|---|---|
| Google, Rules of Machine Learning (Martin Zinkevich) | https://developers.google.com/machine-learning/guides/rules-of-ml | 43 short rules a newcomer can read one at a time. The ones that map to this week: Rule 1 "Don't be afraid to launch a product without machine learning", Rule 2 "First, design and implement metrics", Rule 4 "Keep the first model simple and get the infrastructure right", Rule 14 "Starting with an interpretable model makes debugging easier", Rule 16 "Plan to launch and iterate", Rule 25 "utilitarian performance trumps predictive power", Rule 29 on training like you serve, Rule 33 (train to 5 January, test from 6 January) | Page footer: content CC BY 4.0, code samples Apache 2.0; last updated 2025-08-25. We may quote and adapt with attribution |
| Google, Introduction to ML Problem Framing (course, about 45 minutes) | https://developers.google.com/machine-learning/problem-framing (with /problem and /ml-framing) | State the goal in non-ML terms first; check a non-ML heuristic as the benchmark; then name the model's output and success metrics that are separate from model metrics. Its own table pairs "Banking app: identify fraudulent transactions" with the model goal "Predict if a transaction was made by the card holder" | CC BY 4.0 (footer); adapt with attribution |
| Google Cloud, MLOps: continuous delivery and automation pipelines in ML | https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning (redirects to docs.cloud.google.com) | Three maturity levels that give POC, MVP and production a concrete meaning: level 0 manual and script-driven, level 1 automated pipeline with continuous training, level 2 automated CI/CD of the pipeline. It also redraws the Hidden Technical Debt picture of how small the ML code is inside a real system | CC BY 4.0 (footer); last reviewed 2024-08-28 |
| CRISP-DM, IBM SPSS Modeler CRISP-DM Guide | https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/18.0/en/ModelerCRISPDM.pdf | Six phases with task checklists. The Business Understanding chapter is the strongest classroom tool: business success criteria, then requirements, assumptions and constraints (security and legal limits on data, deployment needs), risks and contingencies, and a cost and benefit analysis, before any data mining goal | Copyright IBM 1994, 2016. Link only; paraphrase the checklists |
| Made With ML (Goku Mohandas), Product design and Systems design lessons | https://madewithml.com/courses/mlops/product-design/ and https://madewithml.com/courses/mlops/systems-design/ | A two-part template: product design (what and why: users, goals, pains, value proposition, objectives, solution with core features, integrations, alternatives, constraints, out of scope, feasibility) then systems design (how: data, metrics, evaluation, modeling, batch or online inference, feedback). The lessons offer a downloadable ML canvas PDF | Site text "(c) 2025 Anyscale, Inc." so link only. The GitHub repository GokuMohandas/Made-With-ML is MIT licensed (LICENSE read 29 Oct 2026), which covers its code |
| Chip Huyen, Machine Learning Systems Design booklet (2019) | https://huyenchip.com/machine-learning-systems-design/toc.html | Four steps (project setup, data pipeline, modeling, serving). Project setup asks about goals, user experience, performance constraints (precision or recall, which error costs more), evaluation, personalization and project constraints. It ends with 27 open interview questions, one of them on credit card fraud | The GitHub repository has a README and no LICENSE file (checked 29 Oct 2026). Link only |
| Chip Huyen, Stanford CS 329S | https://stanford-cs329s.github.io/ | Course framing: start from every stakeholder's objectives, then the tradeoffs those objectives force; notes later became the O'Reilly book Designing Machine Learning Systems (2022) | No licence stated. Link only |
| Full Stack Deep Learning 2022, Lecture 1 and Lecture 8 (Josh Tobin) | https://fullstackdeeplearning.com/course/2022/lecture-1-course-vision-and-when-to-use-ml/ and https://fullstackdeeplearning.com/course/2022/lecture-8-teams-and-pm/ | Lecture 1: are you ready to use ML (have you tried rules or simple statistics?), pick high-impact and low-cost problems, cost grows super-linearly with the accuracy requirement, and the lifecycle loops back on itself. Lecture 8: plan probabilistically, attach a likelihood of success to each task, and manage leadership's expectations | Course page says the material is "free forever"; no licence stated. Link only |
| The ML Test Score (Breck, Cai, Nielsen, Salib, Sculley), IEEE Big Data 2017 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ (PDF https://storage.googleapis.com/gweb-research2023-media/pubtools/4156.pdf) | 28 tests in four sections (data, model, infrastructure, monitoring). Half a point for running a test by hand, a full point for automating it, and the final score is the minimum across the four sections, which is a ready-made "is this production-ready?" rubric | Paper copyright with the authors and publisher; no open licence. Link and cite; paraphrase the rubric |
| Hidden Technical Debt in Machine Learning Systems (Sculley and nine co-authors), NIPS 2015 | https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html | Names the risks a POC hides: boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration, and changes in the external world | No open licence stated. Link and cite |
| Model Cards for Model Reporting (Mitchell, Wu, Zaldivar, Barnes, Vasserman, Hutchinson, Spitzer, Raji, Gebru), arXiv 1810.03993 | https://arxiv.org/abs/1810.03993 | A short document shipped with a model: intended use, evaluation across groups, and the conditions it was tested in. A lending model card is a natural take-home artefact | arXiv non-exclusive distribution licence (not Creative Commons). Link and cite; write our own card template |
| Datasheets for Datasets (Gebru, Morgenstern, Vecchione, Wortman Vaughan, Wallach, Daumé III, Crawford), arXiv 1803.09010, CACM December 2021 | https://arxiv.org/abs/1803.09010 | Every dataset gets a sheet: motivation, composition, collection process, recommended uses. Pairs with the "where did this data come from?" question in a lending project | arXiv non-exclusive distribution licence. Link and cite |
| Machine Learning Canvas (Louis Dorard, 2015) | https://www.louisdorard.com/machine-learning-canvas (redirects to https://www.ownml.co/machine-learning-canvas) | One page filled before building: what to predict, what decision it feeds, what data it needs, what getting it wrong costs | Footer "(c) 2014 to 2026 OWNML S.A.S. All rights reserved"; the canvas download sits behind an email form and no open licence is shown. Link only; build our own one-page scoping sheet |
| Eugene Yan, How to Write Design Docs for ML Systems (7 Mar 2021) and the ml-design-docs template | https://eugeneyan.com/writing/ml-design-docs/ and https://github.com/eugeneyan/ml-design-docs (README read via raw.githubusercontent.com) | The cleanest HLD to LLD bridge: why and what (motivation, success metrics, functional and non-functional requirements, in and out of scope, assumptions), then methodology (problem statement, data, techniques, validation, human in the loop), then implementation (high-level design, infra, latency, security, data privacy, monitoring, cost, integration points, risks), then alternatives considered. His functional-requirement example for fraud is an upper bound on false positives | Blog "(c) Eugene Yan 2015 to 2026"; the repository has no LICENSE file. Link only |
| Christoph Molnar, Interpretable Machine Learning (3rd edition) | https://christophm.github.io/interpretable-ml-book/ | The "black box to white box" chapter list: logistic regression and decision trees first, then permutation importance, partial dependence, LIME, counterfactual explanations, Shapley values and SHAP | CC BY-NC-SA 4.0. The NC clause bars use in a fee-paying course, so link only |
| Stripe, A primer on machine learning for fraud protection | https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection | Precision, recall and false positive rate computed on ten worked transactions; the tradeoff as a block threshold; why validation curves differ from production curves | Stripe copyright. Link only |

A dataset note that fits the same arc: the UCI "Default of Credit Card Clients" dataset (Taiwan, 30,000 rows, 23 features, Yeh and Lien 2009, DOI 10.24432/C55S3H) and "Statlog (German Credit Data)" (1,000 rows, 20 features, DOI 10.24432/C5NC77) are both CC BY 4.0 on their UCI pages (https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients and https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data, checked 29 Oct 2026). The German page ships a cost matrix that says classing a bad customer as good costs 5 and classing a good customer as bad costs 1, which is a ready-made "honest evaluation" exercise.

### Which reference teaches which step of the arc?

| Step the requester named | Strongest verified references |
|---|---|
| Problem understanding from several angles | Google Problem Framing; CRISP-DM Business Understanding; Made With ML product design; Huyen project setup |
| Black box to white box | Reg B and the CFPB circular (section 3); RBI 2024 and 2026 drafts; Apple Card report; Molnar (link only); Stripe Radar's feature-contribution view |
| Functional and non-functional requirements, constraints | Eugene Yan template; Made With ML constraints; CRISP-DM requirements, assumptions and constraints |
| POC, then MVP, then production | Rules of ML 1, 4 and 16; Google Cloud MLOps levels 0 to 2; Ketan Doshi (production can take up to 90%); ML Test Score; the Apple Card launch (section 3) |
| Approach A against approach B | Upstart tested model against traditional model; Stripe's XGBoost plus DNN against DNN only; Ascarza's risk targeting against lift targeting; Google's non-ML benchmark |
| HLD to LLD | Eugene Yan template; Made With ML systems design; Huyen booklet |
| Security, privacy, governance | RBI Digital Lending Directions 2025; DPDP Rules 2025; RBI 2026 model risk draft; FREE-AI; SR 26-2; model cards; datasheets |
| Honest evaluation | German credit cost matrix; Stripe primer (thresholds and counterfactual evaluation); Rules of ML 33; Ascarza; Hidden Technical Debt (feedback loops) |
| Presenting to a business panel | Google's split between success metrics and model metrics; CRISP-DM success criteria and cost and benefit; FSDL Lecture 8 on expectations; Ketan Doshi on accuracy as one factor among many |

## 3. Which real situations show framing, constraints, governance or evaluation deciding the outcome?

### 3.1 Apple Card and gender (United States, NYDFS report, March 2021)

Source: https://www.dfs.ny.gov/system/files/documents/2021/03/rpt_202103_apple_card_investigation.pdf (checked 29 Oct 2026). Verified.

- The allegation began on Twitter on 7 November 2019: a man reported a credit limit 20 times higher than his wife's, and a customer service agent could not explain the algorithm.
- DFS ran regression analysis on underwriting data for nearly 400,000 New York applicants and found no fair lending violation; women and men with equivalent credit characteristics had similar outcomes.
- At DFS's request the bank explained every complainant's decision with ordinary factors (credit score, indebtedness, income, utilisation, missed payments). The failure was transparency and customer service: a six-month wait to appeal credit terms, and a bank that "seemed unprepared" for outcomes its complex model would produce, under internal deadlines to launch by a set date.
- Path to Apple Card, launched June 2020, enrolled more than 70,000 declined applicants, and nearly 5,000 had been approved by the report's date.
- Teaching point: a model can be lawful and still fail the business because nobody designed the explanation and appeal path.

### 3.2 Apple Card launch readiness (United States, CFPB, 23 October 2024)

Sources: https://www.consumerfinance.gov/archive/newsroom/prepared-remarks-of-cfpb-director-rohit-chopra-on-the-goldman-sachs-and-apple-enforcement-press-call/ and the Goldman consent order https://files.consumerfinance.gov/f/documents/cfpb_goldman-sachs-bank-usa-consent-order_2024-10.pdf (both checked 29 Oct 2026). Verified.

- The Apple and Goldman agreement let Apple seek USD 25 million for each 90-day delay caused by Goldman. On 16 August 2019 a readiness assessment told Goldman's board there were "no significant impediments to launch" while also reporting the disputes system was "not fully ready". The card launched on 20 August 2019.
- Goldman then mishandled hundreds of thousands of disputes, including about 157,000 acknowledgement notices not sent on time.
- Orders: Apple USD 25 million penalty; Goldman at least USD 19.8 million redress and a USD 45 million penalty, and a bar on a new consumer credit card without a credible compliance plan. On 22 September 2025 the CFPB terminated the Apple order after the penalty was paid (https://www.consumerfinance.gov/enforcement/actions/apple-inc/, checked 29 Oct 2026).
- Teaching point: the gap between a working POC and a production system is operational, and a launch deadline does not close it.

### 3.3 Upstart's tested model against a traditional model (United States, CFPB, 6 August 2019)

Source: https://www.consumerfinance.gov/archive/blog/update-credit-access-and-no-action-letter/ (checked 29 Oct 2026). Verified.

- Under its No-Action Letter, Upstart compared its model (alternative data plus machine learning) against a hypothetical traditional model with no machine learning, under an agreed model risk and compliance plan, over 22 months.
- Reported results (provided by Upstart, not replicated by the CFPB): 27% more applicants approved and 16% lower average APRs; across tested race, ethnicity and sex segments, acceptance rates up 23% to 29% and APRs down 15% to 17%; near-prime applicants (FICO 620 to 660) approved about twice as often; applicants under 25 32% more likely to be approved; incomes under USD 50,000 13% more likely. Fair lending tests showed no disparities needing further analysis.
- The CFPB said the letter endorsed no variables or techniques.
- Teaching point: this is approach A against approach B written by a regulator, with the comparison designed before anyone looked at results.

### 3.4 Explain every rejection: ECOA and Regulation B (United States)

Sources: 12 CFR 1002.9 on the CFPB's site, https://www.consumerfinance.gov/rules-policy/regulations/1002/9/ ; CFPB Circular 2022-03, https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ ; the withdrawal notice, 90 FR 20084, https://www.govinfo.gov/content/pkg/FR-2025-05-12/pdf/2025-08286.pdf (all checked 29 Oct 2026). Verified.

- Regulation B: notify the applicant within 30 days of a completed application; the statement of reasons "must be specific and indicate the principal reason(s)"; saying the applicant failed the creditor's internal standards or failed to reach a qualifying score is insufficient; more than four reasons is "not likely to be helpful". Reasons must relate to factors actually scored.
- Circular 2022-03 (26 May 2022) said a creditor cannot use a complex algorithm if that means it cannot give specific and accurate reasons.
- Status change to teach carefully: the CFPB withdrew Circular 2022-03 and Circular 2023-03 in its notice of 12 May 2025 (90 FR 20084). The regulation itself, 12 CFR 1002.9, still reads as above on the CFPB's site today. The ecfr.gov copy redirected to a human-verification page and was not used.

### 3.5 US model risk guidance replaced (Federal Reserve, OCC, FDIC, 17 April 2026)

Sources: SR 26-2, https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm and its attachment https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf (checked 29 Oct 2026). Verified.

- SR 26-2 supersedes SR 11-7 (4 April 2011) and SR 21-8. It is most relevant to banks over USD 30 billion in assets.
- Its footnote 3 puts generative AI and agentic AI models outside the guidance's scope, while its principles apply to traditional statistical models and non-generative, non-agentic AI models, which covers a credit score or fraud classifier.
- It keeps the idea of "effective challenge": critical analysis by objective, qualified and independent people across the model lifecycle.
- The old SR 11-7 page (federalreserve.gov/supervisionreg/srletters/sr1107.htm) now answers 404.

### 3.6 [India] Illegal lending apps that forced the rules (RBI Working Group, 18 November 2021)

Source: https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?ID=1189 (checked 29 Oct 2026). Verified.

- About 1,100 lending apps were available to Indian Android users across 80 or more app stores (1 January to 28 February 2021); about 600 of them were illegal.
- The Sachet portal logged about 2,562 complaints against digital lending apps from January 2020 to March 2021, most against apps of entities RBI does not regulate.
- Follow-up, PIB 17 March 2026: RBI has run a public directory of Digital Lending Apps since 1 July 2025 so a borrower can check an app's link to a regulated entity (https://www.pib.gov.in/PressReleasePage.aspx?PRID=2241255&reg=1&lang=1, checked 29 Oct 2026).

### 3.7 [India] Digital lending rules: 2022 guidelines, consolidated in the 2025 Directions

Sources: Guidelines on Digital Lending, 2 September 2022, https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12382 ; Reserve Bank of India (Digital Lending) Directions, 2025, RBI/2025-26/36, 8 May 2025, https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848 (both checked 29 Oct 2026). Verified.

- The RBI page for the 2022 circular now says it has been repealed and points to the 2025 Directions. The 2025 Directions page carried no repeal notice on 29 Oct 2026.
- Creditworthiness: the lender must capture the borrower's economic profile, at minimum age, occupation and income, before lending, and keep it on record for audit. The 2022 text said this was to assess creditworthiness "in an auditable way".
- Data: collection must be need-based, with prior explicit consent and an audit trail; apps must not access files and media, contact lists, call logs or telephony functions; one-time access to camera, microphone or location only for onboarding or KYC; no biometric storage unless allowed by law. The 2022 text also required data to be stored only on servers in India.
- Borrower protections: a cooling-off period of at least one day to exit without penalty; a Key Fact Statement with the all-in APR; a grievance officer, with escalation to RBI if a complaint is not resolved in 30 days.
- New in 2025: a lending service provider working with several lenders must show the borrower all matching offers, including the names of unmatched lenders; every lending app must be reported on RBI's CIMS portal (by 15 June 2025), certified by the Chief Compliance Officer.
- Teaching point: these are non-functional requirements written by a regulator. Contact-list features, which some apps used for scoring and for harassment-led collections, are simply out of bounds.

### 3.8 [India] Reasons for rejecting a loan, in writing

Sources: RBI circular DBOD.No.Leg.BC.65/09.07.005/2006-07, 6 March 2007, https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=3315 ; Reserve Bank of India (All India Financial Institutions, Responsible Business Conduct) Directions, 2025, RBI/DOR/2025-26/336, 28 November 2025, updated 1 July 2026, https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12968 (both checked 29 Oct 2026).

- 2007 (verified): for all categories of loans irrespective of any threshold, including credit card applications, banks and financial institutions should convey in writing the main reason or reasons for rejecting a loan application. The 2003 rule had covered only loans up to Rs 2 lakh. The page carried no repeal notice today.
- 2025 (verified for AIFIs only): clause 13 of the AIFI directions repeats the rule for EXIM Bank, NABARD, SIDBI, NHB and NaBFID.
- Not verified: the commercial bank version (Responsible Business Conduct Directions, RBI/DOR/2025-26/170, 28 November 2025, updated 1 October 2026; title read on https://rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=13140) keeps its text in a PDF that answered with a human-verification page, so whether the clause carried over for banks could not be read. The NBFC version was not located.
- Teaching point: India's version of "explain every rejection" predates ML, and a lending model has to produce reasons a letter can carry.

### 3.9 [India] RBI on model risk: the 2024 credit draft and the 2026 draft guidance

Sources: draft circular "Regulatory Principles for Management of Model Risks in Credit", 5 August 2024, https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4479 ; press release 2026-2027/528, 24 June 2026, https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=63006 ; draft "Guidance on Regulatory Principles for Model Risk Management, 2026", https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=5089 (all checked 29 Oct 2026). Verified as drafts.

- 2024 draft for credit models: a board-approved policy covering the whole model life cycle; a model inventory; deployment approved by the board's risk committee; objectives and problem statement "clearly defined" as pillars of development; outcomes "consistent, unbiased, explainable and verifiable"; independent validation before deployment and at least yearly, including back-testing and a review for bias or discrimination; overrides documented in an auditable format.
- 2026 draft (all models, including third-party and AI or ML): risk-based model tiering by materiality and complexity, reviewed at least yearly; an inventory naming owners, developers, validators and approvers; "An RE should not use any model that harms consumer"; before development, document the rationale, objectives and scope. For AI models it asks for explainability thresholds set by how material the decision is, compensating controls where full explainability is not achievable, fairness assessment with recalibration or redesign, monitoring of data drift and concept drift, and human oversight with override, suspension and kill-switch arrangements.
- Status: comments were invited until 24 July 2026. Whether the 2026 guidance has been finalised was not verified today, so a STUDENT file can state it only as a draft.

### 3.10 [India] FREE-AI: the RBI committee framework (13 August 2025)

Sources: press release 2025-2026/902, https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=61018 ; report page https://rbi.org.in/scripts/PublicationReportDetails.aspx?ID=1306 (both checked 29 Oct 2026). Verified.

- Seven Sutras (Trust is the Foundation; People First; Innovation over Restraint; Fairness and Equity; Accountability; Understandable by Design; Safety, Resilience and Sustainability), six pillars and 26 recommendations.
- Its indicative risk classes put credit underwriting with the high-risk uses, and it says audits of high-risk uses such as credit decisioning should be detailed and should confirm a controlled way to stop or unwind the AI process.
- Survey numbers: of 612 supervised entities surveyed February to May 2025, only 20.80% (127) were using or developing AI; of 171 NBFCs, 27% used AI in some way; of 583 AI applications in production or development, credit underwriting was 13.70% and customer support 15.60%. Entities preferred simpler models for ease of implementation, legacy fit and explainability.
- It links the 2022 "auditable" creditworthiness rule to AI credit models and suggests customers should have a way to challenge and seek clarification on AI decisions.

### 3.11 [India] Privacy: DPDP Act 2023 and DPDP Rules 2025

Source: PIB, 14 November 2025, https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2190014&reg=48&lang=2 (checked 29 Oct 2026). Verified.

- The Rules were notified in November 2025 with an 18-month phased compliance timeline. Consent notices must be standalone and state the specific purpose; data principals can access, correct, update or erase their data, and requests must be answered within 90 days; breaches must be reported to affected people in plain language.
- The exact commencement schedule for each rule was seen only in search excerpts (rules 1, 2 and 17 to 21 at once, rule 4 after one year, the rest after 18 months) and was not read in the Gazette today, so it is not verified.

### 3.12 [India] MuleHunter.AI: a payments fraud model run by the regulator's subsidiary

Sources: RBI Statement on Developmental and Regulatory Policies, 6 December 2024, item 10, https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=59245 ; PIB, 24 March 2026, https://www.pib.gov.in/PressReleasePage.aspx?PRID=2244478&reg=3&lang=2 (both checked 29 Oct 2026). Verified.

- Reserve Bank Innovation Hub built an AI and ML model to detect mule bank accounts; a pilot with two large public sector banks "yielded encouraging results" (December 2024).
- By March 2026 it was live in 26 banks, and banks were advised to use AI and ML tools and network analytics to find mule networks. No accuracy or false-positive numbers were published in these sources.

### 3.13 Churn: who to target is a framing decision (Ascarza, Journal of Marketing Research, February 2018)

Source: author's post-print on the HBS site, https://www.hbs.edu/ris/Publication%20Files/ascarza_jmr_18_783d54d4-e548-41ed-b1d7-8a180f1ae85a.pdf (checked 29 Oct 2026). Verified. (c) 2018 American Marketing Association, so link and cite only.

- Two field experiments: a wireless provider in the Middle East (a market of more than 4 million subscribers) and a North American membership organisation.
- Targeting by sensitivity to the offer (lift) instead of by churn risk would have cut churn by a further 4.1 and 8.7 percentage points in the two studies.
- In the wireless study the offer barely helped the highest-risk decile (95.3% churn in control, 93.7% treated) and raised churn in decile R3 (9.1% to 11.9%). The overlap between the highest-lift and highest-risk customers was about 50%, no better than chance.
- Teaching point: "predict who will leave" and "predict whom the offer will keep" are different problems, and the business ask usually means the second.

### 3.14 Payments fraud: Stripe Radar (engineering blog, 29 March 2023, and Stripe's ML primer)

Sources: https://stripe.dev/blog/how-we-built-it-stripe-radar (redirected from stripe.com/blog) and https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection (both checked 29 Oct 2026). Verified. Stripe copyright, link only.

- Constraints in numbers: more than 1,000 characteristics per transaction, a decision in under 100 milliseconds, fraud on the order of 1 in 1,000 payments, and 0.1% of legitimate payments incorrectly blocked.
- Approach A against B: dropping the XGBoost half of an XGBoost plus DNN ensemble would have cost 1.5% recall, so the team rebuilt a DNN-only model that kept performance and cut training time by more than 85% (to under two hours).
- Honest evaluation: blocked payments never show their true outcome, so production precision and recall need counterfactual estimates. Retraining last month's model on recent data lifted recall by up to half a percentage point a month. Before release they check block rate, false positive rate and authorisation rate per merchant, because an aggregate gain can hide many small merchants losing.
- Explanation: users see which features pushed a payment towards a decline.

## 4. How do real interviewers frame an ML system design question for credit, fraud or churn?

What was verified: Chip Huyen's booklet, written for ML interview preparation, lists the steps and includes the question "Given a dataset of credit card purchases information, each record is labelled as fraudulent or safe, how would you build a fraud detection algorithm?" and warns that questions are ambiguous on purpose so the candidate must ask for clarification and narrow the scope (https://huyenchip.com/machine-learning-systems-design/exercises.html, checked 29 Oct 2026). Eugene Yan's design doc (section 2), Google's framing course, Stripe's material and the regulators in section 3 supply the credit and fraud specifics.

What was not verified: the ByteByteGo "Machine Learning System Design Interview" chapter redirected to a login page; Patrick Halina's guide (patrickhalina.com) failed with a TLS error and then HTTP 503; no official Meta or Google page describing their ML design round was found. These are left out.

### The walk a strong candidate makes (our synthesis, each step tagged with its source)

| Step | What the candidate does | Source |
|---|---|---|
| 1. Clarify the goal | Ask what decision the score feeds (approve, set a limit, block, call, offer) and state the goal in non-ML terms | Huyen "Goals" and "User experience"; Google Problem Framing |
| 2. Beat a baseline first | Name the current rule or scorecard and say what improvement would justify ML | Google Problem Framing (non-ML benchmark); Rules of ML 1 and 3; FSDL Lecture 1 |
| 3. Requirements and constraints | Functional (reasons for every decline, cap on false positives); non-functional (latency budget, throughput, privacy, cost) | Eugene Yan; Reg B; RBI 2007 and 2025; Stripe (under 100 ms) |
| 4. Frame the ML task and label | Define the label and its window (default in N months, chargeback, churn), and note when the label arrives | Huyen "Data pipeline"; Google ML framing |
| 5. Data and features | Sources, consent, what may not be collected, train and serve parity | RBI Digital Lending Directions; DPDP Rules; Rules of ML 29 and 32 |
| 6. Model choice, A against B | Start interpretable, compare with a stronger model on the same split and the same business metric | Rules of ML 4, 14 and 24; Upstart; Stripe |
| 7. Evaluation | Time-based split, cost-weighted metric, threshold chosen from costs, slices by segment and by protected group | Rules of ML 33; German credit cost matrix; Stripe primer; RBI 2024 draft (bias review) |
| 8. Serving and rollout | Batch or online, shadow or canary, rollback | Ketan Doshi; ML Test Score (Infra); Google MLOps levels |
| 9. Monitoring and feedback | Drift, delayed labels, feedback loops from the model's own decisions | Hidden Technical Debt; Stripe (counterfactual); RBI 2026 draft (drift) |
| 10. Governance | Model card, validation independent of the builder, human override | Model cards; SR 26-2 (effective challenge); RBI 2026 draft (kill switch) |

### Follow-up questions an interviewer can fairly ask (questions only, with tags)

- Your fraud model blocks a payment. How do you ever learn whether it was fraud? [evaluation, selective labels, Stripe]
- Defaults show up 6 to 12 months after a loan is made. What do you train on today, and how do you validate? [label delay, time split]
- The regulator asks why applicant 4,812 was declined. What does your system print? [explainability, Reg B, RBI 2007]
- Precision or recall: which error costs the business more here, and where does the threshold go? [cost-sensitive evaluation, German credit cost matrix]
- Your churn model ranks customers by risk. Is that the list marketing should call? [framing, Ascarza]
- Your new model is better on aggregate AUC. Who could it be worse for? [slicing, Stripe per-merchant check, fairness]
- What data are you not allowed to use, and how would you prove you did not use it? [privacy, RBI data rules, DPDP]
- What would make you stop the model in production tomorrow, and who presses the button? [governance, RBI 2026 kill switch]
- What is your non-ML baseline, and what lift over it pays for the system? [framing, Google, FSDL]
- Training reads a warehouse table; serving reads a live API. What breaks? [training-serving skew, Rules of ML 29 and 31]

## 5. Which images may we legally reuse in a public repository and in slides?

All file pages below were read on 29 Oct 2026 and the licence was taken from the page's own licence block. CC BY-SA means attribution plus share-alike: an image used unchanged on a slide carries the attribution line; a modified version must itself be released under the same licence. CC0 and public domain need no attribution, though giving one is good practice.

House-rule note for the requester: CLAUDE.md (decision `w4-visuals`) says every mechanism diagram is a mermaid fence and every data picture is drawn by our own code, with "nothing pasted in from elsewhere". These files are legally reusable, but placing them in a pack needs the requester's exception; otherwise they serve as references for our own redraws.

| Subject | File page | File URL | Author | Licence | Attribution line |
|---|---|---|---|---|---|
| CRISP-DM cycle | https://commons.wikimedia.org/wiki/File:CRISP-DM_Process_Diagram.png | https://upload.wikimedia.org/wikipedia/commons/b/b9/CRISP-DM_Process_Diagram.png | Kenneth Jensen | CC BY-SA 3.0 | "CRISP-DM Process Diagram" by Kenneth Jensen, Wikimedia Commons, CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0) |
| ML workflow or pipeline (import, process, visualise, model, evaluate) | https://commons.wikimedia.org/wiki/File:Machine_learning_workflow_diagram.png | https://upload.wikimedia.org/wikipedia/commons/a/a4/Machine_learning_workflow_diagram.png | Brylie Christopher Oxley | CC0 | "Machine learning workflow diagram" by Brylie Christopher Oxley, Wikimedia Commons, CC0 |
| MLOps as ML plus DevOps plus data engineering | https://commons.wikimedia.org/wiki/File:ML_Ops_Venn_Diagram.svg | https://upload.wikimedia.org/wikipedia/commons/1/1b/ML_Ops_Venn_Diagram.svg | Cmbreuel | CC BY-SA 4.0 | "ML Ops Venn Diagram" by Cmbreuel, Wikimedia Commons, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0) |
| Data-flow diagram (for HLD) | https://commons.wikimedia.org/wiki/File:Data-flow-diagram-example.svg | https://upload.wikimedia.org/wikipedia/commons/2/2e/Data-flow-diagram-example.svg | AutumnSnow, based on an image by Ilario | CC BY-SA 3.0 or GFDL (dual) | "Data-flow-diagram-example" by AutumnSnow (after Ilario), Wikimedia Commons, CC BY-SA 3.0 |
| Confusion matrix (binary) | https://commons.wikimedia.org/wiki/File:Binary_confusion_matrix.jpg | https://upload.wikimedia.org/wikipedia/commons/3/32/Binary_confusion_matrix.jpg | Errachete | CC BY-SA 4.0 | "Binary confusion matrix" by Errachete, Wikimedia Commons, CC BY-SA 4.0 |
| Confusion matrix (binary, older drawing) | https://commons.wikimedia.org/wiki/File:Binary_confusion_matrix.png | https://upload.wikimedia.org/wikipedia/commons/a/a6/Binary_confusion_matrix.png | Oritnk | CC BY-SA 3.0 or GFDL (dual) | "Binary confusion matrix" by Oritnk, Wikimedia Commons, CC BY-SA 3.0 |
| Confusion matrix (worked example, malignant against benign) | https://commons.wikimedia.org/wiki/File:Confusion_matrix_example.png | https://upload.wikimedia.org/wikipedia/commons/8/85/Confusion_matrix_example.png | Tmkunz | CC0 | "Confusion matrix example" by Tmkunz, Wikimedia Commons, CC0 |
| Precision and recall | https://commons.wikimedia.org/wiki/File:Precisionrecall.svg | https://upload.wikimedia.org/wikipedia/commons/2/26/Precisionrecall.svg | Walber | CC BY-SA 4.0 | "Precisionrecall" by Walber, Wikimedia Commons, CC BY-SA 4.0 |
| ROC curve (sketch style) | https://commons.wikimedia.org/wiki/File:Roc-draft-xkcd-style.svg | https://upload.wikimedia.org/wikipedia/commons/3/36/Roc-draft-xkcd-style.svg | MartinThoma | CC0 | "Roc-draft-xkcd-style" by MartinThoma, Wikimedia Commons, CC0 |
| ROC curve (clean) | https://commons.wikimedia.org/wiki/File:Roc_curve.svg | https://upload.wikimedia.org/wikipedia/commons/1/13/Roc_curve.svg | cmglee, MartinThoma | CC BY-SA 4.0 | "Roc curve" by cmglee and MartinThoma, Wikimedia Commons, CC BY-SA 4.0 |
| ROC curves compared | https://commons.wikimedia.org/wiki/File:ROC_curves.svg | https://upload.wikimedia.org/wikipedia/commons/4/4f/ROC_curves.svg | Sharpr (SVG), after kakau (PNG) | CC BY-SA 3.0 | "ROC curves" by Sharpr after kakau, Wikimedia Commons, CC BY-SA 3.0 |
| Overfitting | https://commons.wikimedia.org/wiki/File:Overfitting.svg | https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg | Chabacano | CC BY-SA 4.0 or GFDL (dual) | "Overfitting" by Chabacano, Wikimedia Commons, CC BY-SA 4.0 |
| Bias and variance against total error | https://commons.wikimedia.org/wiki/File:Bias_and_variance_contributing_to_total_error.svg | https://upload.wikimedia.org/wikipedia/commons/9/9f/Bias_and_variance_contributing_to_total_error.svg | Bigbossfarin | CC0 | "Bias and variance contributing to total error" by Bigbossfarin, Wikimedia Commons, CC0 |
| K-fold cross-validation | https://commons.wikimedia.org/wiki/File:K-fold_cross_validation_EN.svg | https://upload.wikimedia.org/wikipedia/commons/b/b5/K-fold_cross_validation_EN.svg | Gufosowa | CC BY-SA 4.0 | "K-fold cross validation EN" by Gufosowa, Wikimedia Commons, CC BY-SA 4.0 |
| Logistic (sigmoid) curve | https://commons.wikimedia.org/wiki/File:Logistic-curve.svg | https://upload.wikimedia.org/wikipedia/commons/8/88/Logistic-curve.svg | Qef | Public domain | "Logistic-curve" by Qef, Wikimedia Commons, public domain |

Notes and exclusions:

- The CRISP-DM file is described by its uploader as own work based on Figure 1 of IBM's CRISP-DM guide. Commons accepts it under CC BY-SA 3.0, but the underlying figure is IBM's; a redraw of our own is the safer choice for a public repository.
- Excluded: File:Confusion_Matrix_Metrics.png (marked CC0, but its source field cites a third-party paper on skin lesion classification, so the licence chain is unclear) and File:Workflow_of_a_machine-learning-based_AI_system.png (generated with an AI image tool and tagged with two different licences).
- Model drift or concept drift: no Commons diagram was found on 29 Oct 2026 (searches for concept drift, data drift, covariate shift and drift detection returned nothing usable). A lift or gains chart was not found either. Both should be drawn by our own code.
- Commons search was rate-limited (HTTP 429) for part of the session; each file page above was read in full, but other candidates may exist.

## 6. What could not be verified on 29 October 2026?

- All eight requester references (403 from Cloudflare at medium.com, towardsdatascience.com and kdnuggets.com). Only references 5 and 7 have an author's own open version (Ketan Doshi's blog).
- The authorship of references 2, 6 and 8, and any open version of references 1, 2, 3, 4, 6 and 8.
- The text of RBI's Commercial Banks Responsible Business Conduct Directions, 2025 (PDF behind a human-verification page), so whether the written-reasons rule carried over for banks; the NBFC equivalent.
- Whether RBI's 2026 model risk guidance has been finalised since comments closed on 24 July 2026.
- The DPDP Rules' rule-by-rule commencement dates (read only in search excerpts).
- The eCFR copy of Regulation B (redirected to a human-verification page; the CFPB's own copy was used instead).
- The EU AI Act text on eur-lex.europa.eu (the page returned an empty challenge response), so its high-risk class for credit scoring is not cited.
- ByteByteGo's ML system design chapter (login wall), Patrick Halina's interview guide (TLS error, then 503) and any official Meta or Google description of the ML design round.
- The Journal of Big Data telecom churn paper (Ahmad, Jafar and Aljoumaa, 2019, CC BY 4.0 per Crossref): the Springer page returned a client challenge, so its numbers are not cited.
- The Columbia Business School article on Ascarza's work (403); the HBS post-print was used instead.

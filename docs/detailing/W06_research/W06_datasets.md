# Week 6 Build 2: public datasets measured for Kalpa Financial Services

Everything below was checked and computed on 29 October 2026. Each download sits in its own folder under `~/.cache/c2_datasets/`, the profiling scripts sit in `docs/detailing/W06_research/scripts/`, and every file was read with pandas under `python3 -I`. Models are scikit-learn 1.9.1 (logistic regression and HistGradientBoostingClassifier). Unless a line says "five-split mean", a number comes from one stratified 70/30 split with `random_state=42`, which leaves a 9,000-customer test book for the Taiwan data.

## 1. The candidates at a glance

| Dataset | Licence as the source states it | Rows x columns | Target and base rate | Time structure | Verdict |
|---|---|---|---|---|---|
| UCI Default of Credit Card Clients (Taiwan, 2005) | CC BY 4.0 (UCI page) | 30,000 x 25 | Default next month, 22.12% | Six monthly statements, April to September 2005, outcome October 2005 | Best single shared problem |
| Kaggle Credit Card customers (BankChurners) | "CC0: Public Domain" (Kaggle), provenance not traceable to a bank | 10,127 x 23 | Attrited, 16.07% | None stated | Leak exhibit only |
| IBM Telco Customer Churn | No data licence stated by IBM; GitHub repo is Apache 2.0; IBM calls the company fictional | 7,043 x 21 | Churn, 26.54% | None | Out: fictional telco |
| ULB credit card fraud | "Database: Open Database, Contents: Database Contents" (Kaggle); "Public" (OpenML) | 284,807 x 31 | Fraud, 0.1727% | Two days of seconds | Viable second track |
| Hillstrom MineThatData e-mail | No licence stated anywhere | 64,000 x 12 | Visit, conversion, spend; randomised three arms | Two-week response window | Hold until permission |
| HMDA public loan-level data (CFPB) | Public domain (CFPB legal notice) | 29,929 x 99 in the Delaware 2023 slice | Denied, 26.86% | One filing year per pull | Real leak exhibit; alternative second track |

## 2. Each candidate measured

### 2.1 UCI Default of Credit Card Clients (Yeh and Lien 2009)

**Download.** `https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip` returned HTTP 200 and 5,539,494 bytes; the zip holds one file, `default of credit card clients.xls`. Reading it needs the `xlrd` package, which the session had to install.

**Licence.** The UCI page states: "This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license." Checked 29 October 2026. CC BY 4.0 allows redistribution and derived work, commercial use included, with attribution. The citation the page asks for is "Yeh, I. (2009). Default of Credit Card Clients [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H", and the paper is Yeh and Lien (2009), Expert Systems with Applications 36(2), 2473 to 2480. The OpenML copy (data id 42477) labels the same data "CC0", which disagrees with UCI; the build should cite UCI and treat CC BY 4.0 as the licence.

**Shape and target.** 30,000 rows and 25 columns: ID, LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, six repayment statuses (PAY_0, PAY_2 to PAY_6), six bill amounts (BILL_AMT1 to 6), six payment amounts (PAY_AMT1 to 6) and `default payment next month`. The target has 6,636 defaults, a base rate of 22.12%. Amounts are New Taiwan dollars.

**Time structure.** Every customer carries the same six months, September 2005 (suffix 1 or PAY_0) back to April 2005 (suffix 6), and the outcome is October 2005. There is one cohort and one snapshot date, so an out-of-time split across customers is impossible; the six months do allow a real "data lag" test (drop the newest month) and a "late label" test (train on September's lateness as a stand-in for October's default).

**Sensitive attributes.** SEX (11,888 men, 18,112 women; default rate 24.2% against 20.8%), MARRIAGE, AGE (21 to 79) and EDUCATION.

**Missingness.** No cell is empty and UCI states no missing values. Missingness hides inside codes the dictionary does not define (below).

**Real traps found in the file.**

| Trap | What the data shows |
|---|---|
| Two header rows | Row one of the sheet holds X1 to X23 and Y; the real names sit on row two, so `read_excel` needs `header=1`. |
| PAY_0 has no PAY_1 | The September status is named PAY_0 while the bills and payments start at 1, so month alignment by suffix is off by one. |
| Repayment codes the dictionary omits | UCI defines -1 (pay duly) and 1 to 9 (months late). The September column holds -2 for 2,759 rows and 0 for 14,737 rows, so 17,496 of 30,000 values (58.3%) use codes the dictionary does not explain. |
| Code 1 vanishes after September | Status 1 appears 3,688 times in September and 28, 4, 2, 0 and 0 times in August to April, so the coding was not applied the same way across months. |
| Education and marital codes outside the dictionary | EDUCATION 0, 5 and 6 cover 345 rows (default rates 0%, 6.4% and 15.7% against 22.1%); MARRIAGE 0 covers 54 rows. |
| Accounts with nothing owed labelled default | 795 accounts show a zero bill and a zero payment in all six months, and 299 of them (37.6%) are labelled default, well above the 22.1% base. |
| Duplicates | 35 rows repeat another row exactly once ID is dropped; 108 rows sit in groups with identical inputs, and 21 of those groups carry conflicting labels. |
| Negative and over-limit bills | 590 September bills are negative (credit balances) and 2,115 exceed the credit limit. |

**What three weak learners can build in two days.** Day one: frame the October decision, split, score the rule "sort by months late in September" (precision 0.50 and recall 0.50 at status 1 or worse; precision 0.69 and recall 0.32 at status 2 or worse), recode the status columns as categories and fit a logistic regression. Day two: a gradient-boosted model (AUC 0.778, five-split mean), a threshold set from Rohan's cost ratio, a call list sized to the team, and the error bill in cost units. Every column is a thing a weak learner can reason about from first principles: a limit, a bill, a payment, months late.

### 2.2 Kaggle "Credit Card customers" (BankChurners, Sakshi Goyal)

**Download.** Kaggle's public endpoint `https://www.kaggle.com/api/v1/datasets/download/sakshigoyal7/credit-card-customers` answered without a login (a 302 to a signed storage link) and gave a 387,771-byte zip holding `BankChurners.csv`. This is the same anonymous route `kagglehub` uses; no login or bot check was bypassed.

**Licence.** Kaggle's metadata states `"licenseNameNullable":"CC0: Public Domain"`, checked 29 October 2026. The uploader's own description says "I got this dataset from a website with the URL as https://leaps.analyttica.com/home", so the CC0 dedication comes from someone who did not create the data. The provenance cannot be traced to a bank, and the build should treat the licence as uncertain.

**Shape and target.** 10,127 rows and 23 columns; Attrition_Flag has 1,627 attrited customers, a base rate of 16.07%. No time structure is documented: activity columns cover "12 months" and a Q4 to Q1 change, with no date for the attrition event.

**Sensitive attributes.** Gender, Customer_Age, Marital_Status, Dependent_count, Education_Level, Income_Category.

**The two Naive Bayes columns.** The last two columns are named `Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1` and `_2`. They are a classifier's output probabilities for the target and sum to 1. Column 1 alone scores AUC 1.000 and 100% accuracy at 0.5; column 2 is its mirror at AUC 0.000. They leak completely and must be dropped.

**Other real traps.** "Unknown" is a category in Education_Level (1,519 rows), Marital_Status (749) and Income_Category (1,112). Months_on_book equals 36 for 2,463 rows (24.3%), a spike that looks like a filled default. Avg_Open_To_Buy equals Credit_Limit minus Total_Revolving_Bal on every row and Avg_Utilization_Ratio equals their ratio, so three columns carry two facts. With the Naive Bayes columns dropped a gradient-boosted model still reaches CV AUC 0.994; removing the seven 12-month activity and balance columns brings it to 0.789. Whether that activity window overlaps the attrition date is undocumented, which is a temporal-leak risk the data cannot settle.

**Verdict.** A strong leak exhibit, weak as the shared problem because of provenance.

### 2.3 IBM Telco Customer Churn

**Authoritative source.** IBM's Cognos Analytics sample data. IBM's documentation page (`https://www.ibm.com/docs/SSEP7J_11.1.0/com.ibm.swg.ba.cognos.ig_smples.doc/c_telco_dm_sam.html`) says: "This sample data module tracks a fictional telco company's customer churn based on various factors." It states no terms of use. The CSV downloaded from IBM's own GitHub, `https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv` (HTTP 200, 970,457 bytes). That repository is "licensed under the Apache Software License, Version 2" and was "archived by the owner on Jul 22, 2024"; it says nothing separate about the data. The Kaggle copy (blastchar) states "Data files © Original Authors". A Mendeley Data copy claims CC BY 4.0, but it was uploaded by a third party.

**Shape and target.** 7,043 rows, 21 columns, churn 1,869 (26.54%). TotalCharges is stored as text with 11 blank values, all at tenure 0. 22 rows duplicate another once customerID is dropped. TotalCharges tracks tenure times MonthlyCharges with correlation 0.9996. Sensitive attributes: gender and SeniorCitizen.

**Verdict.** Out. IBM calls the company fictional, the data licence is unstated, and a telco does not fit a payments app.

### 2.4 ULB credit card fraud (Kaggle mlg-ulb/creditcardfraud)

**Download.** OpenML's parquet copy, `https://data.openml.org/datasets/0000/1597/dataset_1597.pq` (HTTP 200, 73,231,184 bytes), is the same table and needs no account. Kaggle's anonymous endpoint `https://www.kaggle.com/api/v1/datasets/download/mlg-ulb/creditcardfraud` also serves it.

**Licence.** Kaggle's metadata states `"licenseNameNullable":"Database: Open Database, Contents: Database Contents"`, which is Kaggle's label for the Open Database License 1.0 on the database and the Database Contents License 1.0 on its contents. OpenML states `licence : Public`. Both were checked 29 October 2026. ODbL allows teaching use and redistribution with attribution, and a derived database that is published must stay under ODbL.

**Shape and target.** 284,807 rows and 31 columns (Time, V1 to V28, Amount, Class). Frauds number 492, a base rate of 0.1727%. Kaggle's description: "transactions made by credit cards in September 2013 by European cardholders", "transactions that occurred in two days". The currency of Amount is not stated.

**Time structure.** Time runs from 0 to 172,792 seconds, 48 hours. Day one holds 144,786 rows and 281 frauds (0.194%); day two holds 140,021 rows and 211 frauds (0.151%). Train on day one and test on day two is a real time split.

**Sensitive attributes.** None visible; V1 to V28 are anonymous principal components.

**Real traps.** OpenML marks Time as the row identifier, and scikit-learn's `fetch_openml` drops row-identifier columns (confirmed in `_valid_data_column_names` of scikit-learn 1.9.1), so a learner who loads it that way silently loses the only clock. 1,081 rows repeat another exactly, with 32 frauds among the duplicated rows, and 9,144 repeat once Time is ignored. 1,825 transactions have Amount 0, 27 of them frauds. Predicting "genuine" for everything scores 99.85% accuracy on day two. A default HistGradientBoostingClassifier (with automatic early stopping) collapsed to AUC 0.58 on a random split and 0.84 on the time split, while the same model with `learning_rate=0.05`, `l2_regularization=1.0` and early stopping off reached AUC 0.982 and AUPRC 0.791 on the time split; logistic regression reached AUC 0.958 and AUPRC 0.641.

**A mismatch with the row.** The Build 2 row speaks of "a million rows with five thousand positives" and "half a percent positives". The real table is 284,807 rows at 0.17%. The brief should quote the real numbers.

**What three weak learners can build in two days.** The accuracy trap, a time split, logistic regression against boosting on AUPRC, a review queue of N alerts a day and the money it catches. The features cannot be reasoned about from first principles, so this track trains the metric and the threshold more than the business reading.

### 2.5 Kevin Hillstrom's MineThatData e-mail campaign

**Download.** `http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv` (HTTP 200, 3,964,977 bytes), linked from the author's post of March 2008, `https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html`.

**Licence.** None stated. The post gives the link and invites analysis ("Dazzle our readers with your insights") and carries no licence or copyright line for the data; scikit-uplift's loader documentation calls its copy "a copy of MineThatData E-Mail Analytics And Data Mining Challenge dataset" and states no licence either. Checked 29 October 2026. With no licence the default is all rights reserved, so the build should download it in code only, commit no copy or row-level extract, and ask the author before publishing derived tables.

**Shape and outcomes.** 64,000 rows and 12 columns. "1/3 were randomly chosen" for each of Mens E-Mail (21,307), Womens E-Mail (21,387) and No E-Mail (21,306). Visit rates are 18.28%, 15.14% and 10.62%; conversion 1.253%, 0.884% and 0.573%; mean spend in dollars 1.42, 1.08 and 0.65. Spend is positive on exactly the 578 converting rows. No missing values; no sensitive attributes beyond zip_code type.

**Real traps.** History equals 29.99 for 7,947 rows (12.4%), a floor value that also explains most of the 6,562 exact duplicate rows. The zip_code label is spelled "Surburban" in the data.

**Verdict.** A clean randomised experiment, so it can show a true lift; it cannot show the "cause or mix" problem of sub-problem 5 without an artificial non-random comparison, and its licence is open only by silence.

### 2.6 Other open candidates found

**HMDA loan-level data (US Consumer Financial Protection Bureau).** The CFPB's legal notice states: "Information created by the CFPB is in the public domain and you may reproduce, publish, or otherwise use it." Checked 29 October 2026; the data are filed by lenders and published by the CFPB for the FFIEC, and the notice asks for citation. The data browser API needs no key. The slice measured was `https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?states=DE&years=2023&actions_taken=1,3` (HTTP 200, 11.5 MB): 29,929 Delaware applications from 2023 that were either originated (21,889) or denied (8,040), a denial rate of 26.86%, in 99 columns. The label is the lender's decision, never a repayment outcome.

| Real trap in the HMDA slice | Measured |
|---|---|
| Fields written after the decision | interest_rate is NA or Exempt for 98.4% of denials and 0.7% of originations; that missing flag alone scores AUC 0.982. A boosted model on application fields reaches CV AUC 0.892 and 0.9998 once interest_rate and origination_charges are added. |
| Sentinel and exempt codes | "Exempt" in 789 rows; applicant_age 8888 in 531 rows, a code the field page lists without defining; credit score type 1111 in 790 rows; denial reason 1111 in 486 rows, a code the field page does not list. |
| A field in two formats | debt_to_income_ratio mixes bands ("<20%", "50%-60%") with bare integers 36 to 49 in 12,792 rows, while the field page writes them as "36%". |
| Sensitive attributes | derived_race, derived_sex, derived_ethnicity, applicant_age. Raw denial rates: White 22.5% (17,355 rows), Black or African American 37.7% (5,394), Asian 23.1% (1,384), Race Not Available 30.5% (4,874). |
| Rejection reasons | First denial reason among 8,040 denials: debt-to-income 2,669, credit history 2,202, collateral 1,050, other 834, incomplete application 651. |

**Small UCI credit sets on OpenML.** Australian (40981) and Credit Approval (29) are 690 rows each with anonymised attribute names; OpenML lists both as "Public". They cannot be read from first principles.

**Synthetic or unknown-origin sets, rejected under the no-synthetic rule or on provenance.** PaySim (Kaggle ealaxi/paysim1) states "CC BY-SA 4.0" and describes itself as "a synthetic dataset generated using the simulator called PaySim". The Bank Account Fraud suite (sgpjesus) states "CC BY-NC-SA 4.0", calls itself "synthetic", and the non-commercial term is a risk for a fee-paying programme; its one-million-row tables are the likely origin of the row's "million rows". Kaggle laotse/credit-risk-dataset and rikdifos/credit-card-approval-prediction state "CC0: Public Domain" with no traceable source; the second says "Don't ask me where this data come from, the answer is I don't know!". The Indian L&T vehicle-loan set (avikpaul4u/vehicle-loan-default-prediction) states the licence as "Unknown".

### 2.7 Licence findings only

| Dataset | Finding, 29 October 2026 |
|---|---|
| Home Credit Default Risk (Kaggle competition) | The data sit behind a signed-in acceptance of the competition rules; the unauthenticated API answered `{"code":401,"message":"Unauthenticated"}` and the rules page did not render in this session, so the exact data terms are not verified. Treat as restricted. |
| Give Me Some Credit (Kaggle competition) | Same gate and the same 401. The OpenML mirror (44089) states its licence as "See source" and points back to the competition. Treat as restricted. |
| Lending Club (Kaggle wordsforthewise/lending-club) | Kaggle states "CC0: Public Domain", but the uploader writes that "LendingClub now has a scary 'TOS' popup when downloading the data" and "Worst case, they will ask me/Kaggle to take it down". The CC0 label is not the rights holder's. Treat as restricted. |

## 3. Recommendation

### (a) The single shared problem: the UCI Taiwan card book

UCI Default of Credit Card Clients is the best single dataset. It is real, CC BY 4.0, new to the cohort, small enough for a Codespace, and every column is a thing a weak learner can count by hand. Its traps are real and findable by sorting and reconciling, and its six months support the lag and late-label constraints without inventing anything. Its real-world likeness is Taiwan's 2005 to 2006 card and cash-card debt crisis, which falls in the very months the data cover; the counts in the secondary accounts disagree (300,000 to more than 500,000 debtors), so any number used in class needs a primary source first.

The business question at Kalpa Financial: **"Rohan Desai's card book holds 30,000 cardholders with six monthly statements each. Before October's due date, whom should Kalpa act on (call them, or cut their limit), given a collections team that can reach only N people and a missed default that costs several times a wrongful action, and what is the error bill of the list we hand over?"** This one question carries credit risk, collections prioritisation and the asymmetric threshold of sub-problems 1 and 3. Note that the data describe existing cardholders, so the action is a limit cut or a call rather than an application rejection.

### (b) A second track is viable

ULB fraud is viable as a second track for groups that want the extreme-imbalance problem of sub-problem 2. It is openly licensed, clean, carries a real time split, and its traps (the dropped Time column, the accuracy of 99.85%, the collapsing default model) are real. Its anonymous features mean it trains the metric and the review queue more than business reasoning, and the brief must use the real 0.17% and 284,807 rows. HMDA is the better choice if the second track must carry a real application-time leak, rejection reasons and protected attributes, at the cost of a 99-column table and a label that records the lender's decision. Its Delaware slice also works as a twenty-minute shared exhibit for Wednesday's interview question about "a field in the application data written after the decision", since the Taiwan file has no such column. Churn (BankChurners) and campaign lift (Hillstrom) should not be tracks: one has untraceable provenance, the other has no licence.

### (c) Injected constraint cards, computed on the Taiwan data

Costs are in units where one wrongful action costs 1 and one missed default costs the ratio on the card.

| # | Card (what Rohan says) | What changes, with the number |
|---|---|---|
| 1 | "A missed default costs us five times a wrongful limit cut." | The threshold moves from 0.50 to 0.16 (tuned on validation, theory 1/6 = 0.167). The share of the book acted on rises from 11.4% to 44.5%, and the cost per 1,000 customers falls from 762 to 568 units (25% lower). Acting on everyone costs 779 and on no one 1,106. At the row's ratio of twenty, the theory threshold is 1/21 = 0.048, the model acts on 97.7% of the book, and its cost of 765 is only 1.8% below acting on everyone (779): the right answer at 20:1 is to change the action or the ratio, since the model barely beats "act on all". |
| 2 | "The collections team can call 1,000 of these 9,000 customers this month." | Five-split means: the model's top 1,000 reach 687 defaulters against 666 for the rule "sort by September months late" (21 more, 3%) and about 221 at random. At 2,000 calls the gap widens to 1,079 against 1,010 (69 more, 7%). At 1,000 calls the simple rule is the defensible choice; the model earns its place only at the larger capacity. |
| 3 | "My team is measured on the money it recovers." | Ranking the top 1,000 by probability times September bill captures NT$62.9M of the NT$100.1M defaulted balance (62.8%), against NT$42.7M (42.7%) when ranked by probability alone, while reaching 469 defaulters instead of 676. A different list, from the same model. |
| 4 | "Every adverse action must carry its main reasons." (RBI circular RBI/2006-2007/280 of 6 March 2007 asks lenders to "convey in writing the main reason / reasons" for rejecting loan applications, "including credit card applications"; whether a later master direction restates it is not verified.) | Five-split means: logistic regression with the status codes one-hot scores AUC 0.765 against 0.778 for gradient boosting, a cost of 0.013 for a model whose every reason can be read off a coefficient. The same logistic regression with the codes left as numbers scores 0.717, so coding the statuses right is worth almost four times the model choice. |
| 5 | "Sex, marital status, age and education may not be used." | Five-split mean AUC moves from 0.7779 to 0.7769 (0.001 lower), and on the seed-42 split the top-1,000 list reaches 675 defaulters against 676. At that list, men are flagged at 11.5% and women at 10.9% with the attributes, and 11.3% and 11.0% without them, while the true default rates are 23.9% and 21.0%. Dropping the columns costs almost nothing and leaves the group gap in place, so the fairness check moves from inputs to outcomes by group. |
| 6 | "September's statement lands after the call list is built." | Dropping PAY_0, BILL_AMT1 and PAY_AMT1 cuts the five-split mean AUC from 0.778 to 0.747. The top 1,000 reach 614 defaulters against 563 for the rule "sort by August months late" (51 more), where the gap without the lag was 21. The lag removes the rule's best column and turns the model from optional to necessary. |
| 7 | "October's outcomes arrive in November; train today on what we already know." | Training on April to August with September lateness (status 1 or worse, base 22.7%) as a stand-in label scores AUC 0.747 on the true October outcome and reaches 539 defaulters in the top 1,000, against 0.779 and 680 with the true label (141 fewer per 1,000 calls). The stricter stand-in (status 2 or worse) scores 0.652 and 652. The team has to choose between waiting a month and accepting a proxy, and the number says what the proxy costs. |
| 8 | "Any code not in the data dictionary is a question for my data team, not a guess." | 17,496 September statuses (58.3%) use -2 or 0, which the dictionary omits; 345 rows carry education codes 0, 5 and 6 and 54 carry marital code 0. 795 accounts with no bill and no payment for six months are labelled default 299 times (37.6%), which is 4.5% of all 6,636 defaults. If Rohan rules that an account owing nothing cannot default, relabelling those 299 as non-default drops the base rate to 21.1%, and removing the 795 accounts from the book drops it to 21.7%. |

Two further real constraints are available if the brief needs them: rebalancing the classes (`class_weight="balanced"`) lifts the mean predicted probability from 0.221 to 0.456 and the Brier score from 0.146 to 0.208, so a cost threshold applied to rebalanced scores acts on 99.7% of the book; and the 35 duplicate rows with 21 conflicting groups give a reconciliation exercise. For the second track, the leak card is real on HMDA (missing-interest-rate flag at AUC 0.982; 0.892 against 0.9998 with and without the post-decision fields) and on BankChurners (Naive Bayes column at AUC 1.000), and the capacity card is real on ULB fraud: a review queue of 200 day-two alerts catches 162 of 211 frauds and 16,760 of 26,889 amount units, while ranking by probability times amount catches 102 frauds and 18,780 units.

## 4. Download lines a notebook can use

```python
import io, zipfile, urllib.request, pandas as pd
# UCI Taiwan card default (CC BY 4.0); needs xlrd; real names sit on the second header row
raw = urllib.request.urlopen("https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip").read()
with zipfile.ZipFile(io.BytesIO(raw)) as z:
    cards = pd.read_excel(z.open("default of credit card clients.xls"), header=1)
# ULB fraud (ODbL/DbCL) from OpenML parquet; read directly so the Time column survives
fraud = pd.read_parquet("https://data.openml.org/datasets/0000/1597/dataset_1597.pq")
# HMDA 2023 Delaware, originated or denied (public domain)
hmda = pd.read_csv("https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?states=DE&years=2023&actions_taken=1,3", dtype=str)
```

## 5. Sources, each checked 29 October 2026

- UCI dataset page: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
- UCI download: https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip
- Yeh and Lien (2009) DOI, which resolves to Elsevier: https://doi.org/10.1016/j.eswa.2007.12.020
- OpenML metadata, Taiwan copy: https://www.openml.org/api/v1/json/data/42477
- Kaggle metadata, BankChurners: https://www.kaggle.com/api/v1/datasets/view/sakshigoyal7/credit-card-customers
- IBM Telco documentation: https://www.ibm.com/docs/SSEP7J_11.1.0/com.ibm.swg.ba.cognos.ig_smples.doc/c_telco_dm_sam.html
- IBM Telco GitHub repository: https://github.com/IBM/telco-customer-churn-on-icp4d
- Kaggle metadata, Telco (blastchar): https://www.kaggle.com/api/v1/datasets/view/blastchar/telco-customer-churn
- Mendeley Telco copy: https://data.mendeley.com/datasets/phsxg9ssrf
- Kaggle metadata, ULB fraud: https://www.kaggle.com/api/v1/datasets/view/mlg-ulb/creditcardfraud
- OpenML metadata, ULB fraud: https://www.openml.org/api/v1/json/data/1597
- Hillstrom post: https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html
- scikit-uplift loader documentation: https://www.uplift-modeling.com/en/latest/api/datasets/fetch_hillstrom.html
- CFPB legal notice: https://www.consumerfinance.gov/privacy/website-privacy-policy/
- HMDA data browser API: https://ffiec.cfpb.gov/documentation/api/data-browser/
- HMDA field definitions: https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields
- RBI fair practices circular of 6 March 2007: https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=3315
- Taiwan card crisis case study (figures disagree with other accounts): https://sevenpillarsinstitute.org/case-studies/taiwans-credit-card-crisis
- Kaggle metadata for PaySim, BAF, laotse, rikdifos, L&T and Lending Club: https://www.kaggle.com/api/v1/datasets/view/{owner}/{dataset}

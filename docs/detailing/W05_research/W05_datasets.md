# Week 5 public datasets: verification note

Date verified: 28 October 2026. Every number below comes from code run on this machine against the downloaded files (scripts in `/tmp/claude-0/-home-user-c2-content-factory/3ce39546-7624-54a7-a8da-ce3bf0688b7c/scratchpad/scripts/`, downloads in `/tmp/claude-0/-home-user-c2-content-factory/3ce39546-7624-54a7-a8da-ce3bf0688b7c/scratchpad/datasets/`). Every quote comes from a page or file fetched on that date. Environment: Python 3.11.17, pandas 3.0.6, scikit-learn 1.9.1. All five download snippets were run twice in an empty folder: the first run downloaded, the second read the cache (0.0 to 0.5 s per dataset).

## 1. UCI Bank Marketing (bank-additional-full.csv)

| Fact | Value |
|---|---|
| Source page | https://archive.ics.uci.edu/dataset/222/bank+marketing (verified 28 October 2026) |
| Download | https://archive.ics.uci.edu/static/public/222/bank+marketing.zip, 1,023,843 bytes |
| Inside the zip | `bank.zip` (579,043 bytes, the older 17-column file) and `bank-additional.zip` (444,572 bytes), which holds `bank-additional/bank-additional-full.csv` (5,834,924 bytes), `bank-additional.csv` (4,119-row 10 percent sample) and `bank-additional-names.txt`, plus `.DS_Store`, `.Rhistory` and `__MACOSX` junk |
| Licence (page text) | "This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license." DOI 10.24432/C5K306. Creators S. Moro, P. Rita, P. Cortez |
| Citation the names file asks for | Moro, Cortez and Rita, "A Data-Driven Approach to Predict the Success of Bank Telemarketing", Decision Support Systems, 2014, doi:10.1016/j.dss.2014.03.001 |
| Rows, columns | 41,188 rows, 21 columns (20 inputs and y); 12 exact duplicate rows |
| Target | y = yes in 4,640 rows (11.27 percent), no in 36,548 |
| Period | rows ordered by date, May 2008 to November 2010 (names file) |

Download code (tested):

```python
import io, zipfile, urllib.request, pathlib, pandas as pd
DATA = pathlib.Path("data"); DATA.mkdir(exist_ok=True)
f = DATA / "bank-additional-full.csv"
if not f.exists():
    outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen("https://archive.ics.uci.edu/static/public/222/bank+marketing.zip").read()))
    inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
    f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
bank = pd.read_csv(f, sep=";")
```

The duration sentence, quoted from the `duration` row of the Variables Table on https://archive.ics.uci.edu/dataset/222/bank+marketing and identical in `bank-additional-names.txt` inside the zip (the page writes `y='no'` with single quotes, the file writes `y="no"`):

> last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y="no"). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.

Correlation matrix (Pearson, all 41,188 rows):

| | emp.var.rate | euribor3m | nr.employed |
|---|---|---|---|
| emp.var.rate | 1.0000 | 0.9722 | 0.9070 |
| euribor3m | 0.9722 | 1.0000 | 0.9452 |
| nr.employed | 0.9070 | 0.9452 | 1.0000 |

The three columns take only 10, 316 and 11 distinct values, so they mark the quarter a row was called in.

Sign-flip test (logistic regression of y on standardised columns, C = 1e6 so the penalty is negligible, all rows):

| Column | Alone | All three together | Pair with euribor3m | Pair with nr.employed |
|---|---|---|---|---|
| emp.var.rate | -0.8831 | -0.5506 | -0.0577 | -0.0802 |
| euribor3m | -0.9301 | +0.7781 (sign flips) | | +0.1268 (sign flips) |
| nr.employed | -0.9580 | -1.1911 | -1.0642 | |

Alone, each of the three says "higher rate, fewer subscriptions". Fitted together, euribor3m turns positive. In the full 19-feature model below (C = 1) the standardised coefficients are emp.var.rate -2.1771, euribor3m +0.2728, nr.employed +0.4666: two of the three carry the opposite sign from their single-column fit.

Models without duration (seed 42, stratified 80/20 split: 32,950 training rows, 8,238 validation rows, validation positive rate 11.26 percent; categoricals one-hot encoded, numerics standardised for the logistic model):

| Model | Result |
|---|---|
| Majority baseline (predict no for everyone) | accuracy 88.74 percent |
| Logistic regression, C = 1 | ROC AUC 0.8008; accuracy at threshold 0.5: 90.09 percent |
| Same model, confusion matrix at 0.5 | TP 203, FP 91, FN 725, TN 7,219: precision 0.690, recall 0.219, F1 0.332 |
| Same model at threshold 0.2 | precision 0.452, recall 0.595, F1 0.513, accuracy 87.30 percent |
| Same model at threshold 0.1 | precision 0.333, recall 0.681, accuracy 81.01 percent |
| Decision tree, unlimited depth | train accuracy 99.54 percent, validation accuracy 84.20 percent (below the baseline), depth 35, 4,940 leaves, validation AUC 0.6263 |
| Random forest, 300 trees | validation AUC 0.7872; train accuracy 99.54 percent, validation accuracy 89.60 percent |
| HistGradientBoosting, defaults | validation AUC 0.8141; validation accuracy 90.25 percent |
| Logistic regression WITH duration | ROC AUC 0.9424 (lift +0.1417); accuracy 91.66 percent |
| duration as the only feature | ROC AUC 0.8228, above the whole honest model |

Traps in loading:

- The separator is `;` with quoted headers. `pd.read_csv(path)` with the default comma returns 41,188 rows and one column.
- Two levels of zip. The inner zip also carries `__MACOSX` and `.DS_Store` entries, so read the one member by name.
- `pdays` uses 999 for "never contacted before": 39,673 rows (96.32 percent). The page's "Additional Information" prose describes the older `bank.csv` file, where the sentinel is -1 and `contact` has an `unknown` level; the 21-column file follows the names file inside the zip, where 999 is the sentinel and `contact` has only `cellular` and `telephone`.
- Missing values are the string `unknown`: job 330, marital 80, education 1,731, default 8,597 (20.87 percent), housing 990, loan 990. `default` has only 3 `yes` rows, so one-hot encoding it yields a near-empty column.
- `duration` is 0 in 4 rows and every one of them is y = no, which is the leak in miniature.
- The file is sorted by date and the macro columns identify the quarter, so a random split mixes 2008 and 2010 rows; a split by time is the honest check for Thursday.
- 12 duplicate rows; `campaign` runs up to 56 contacts.

Verdict: carries the whole week. One file serves framing and the baseline (Monday), the 11 percent base rate that makes 90 percent accuracy worthless at recall 0.22 (Tuesday), the duration leak, the 999 sentinel, the unknowns and the collinear trio with the sign flip (Wednesday), the tree at 99.5 versus 84.2 percent and the ensembles (Thursday), and the memo choosing between AUC 0.80 and 0.81 with a cost-based threshold (Friday).

## 2. German Credit (Statlog), OpenML credit-g

| Fact | Value |
|---|---|
| OpenML record | https://www.openml.org/api/v1/json/data/31 (verified 28 October 2026): id 31, name credit-g, version 1, licence "Public", format ARFF, upload date 2014-04-06 |
| OpenML file | https://openml.org/data/v1/download/31/credit-g.arff, cached by scikit-learn as `credit-g.arff.gz`, 36,049 bytes; first fetch 4.8 to 5.1 s, cached fetch 0.01 to 0.5 s |
| UCI page | https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data (verified 28 October 2026), DOI 10.24432/C5NC77, creator Hans Hofmann |
| UCI licence (page text) | "This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license." |
| UCI download | https://archive.ics.uci.edu/static/public/144/statlog+german+credit+data.zip, 29,607 bytes: `german.data` 79,793 bytes, `german.data-numeric` 102,000 bytes, `german.doc` 4,679 bytes, `Index` |
| Rows, columns | 1,000 rows, 20 features and `class`; no missing values (both sources) |
| Target | bad 300 (30.00 percent), good 700; UCI codes 1 = good, 2 = bad |

Download code (tested; scikit-learn caches under `data_home`):

```python
from sklearn.datasets import fetch_openml
credit = fetch_openml(name="credit-g", version=1, as_frame=True, data_home="data").frame
```

The cost matrix, quoted from the "Additional Information" section of https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data (the same text sits in `german.doc`, section 8):

> This dataset requires use of a cost matrix (see below) ..... 1 2 ---------------------------- 1 0 1 ----------------------- 2 5 0 (1 = Good, 2 = Bad) The rows represent the actual classification and the columns the predicted classification. It is worse to class a customer as good when they are bad (5), than it is to class a customer as bad when they are good (1).

The OpenML description (same API record) states it as: "This dataset comes with a cost matrix: Good Bad (predicted) / Good 0 1 (actual) / Bad 5 0. It is worse to class a customer as good when they are bad (5), than it is to class a customer as bad when they are good (1)."

Traps in loading:

- The OpenML frame returns pandas `category` columns with readable labels (checking_status `<0`, `0<=X<200`, `>=200`, `no checking`) and the target as the strings `good` and `bad`; the positive class must be chosen on purpose, and the costly class is `bad`.
- The UCI `german.data` file is whitespace separated with no header, A-codes (`A11`, `A34`) and a 1/2 target; `german.doc` is the only key to the codes.
- `personal_status` folds sex into marital status (`male single`, `female div/dep/mar`), which is a fairness talking point rather than a feature to drop silently.
- Amounts are in Deutsche Mark from 1994; the setting is lending in Hamburg, so the case has to say so.

Verdict: Tuesday's lending transfer. The 5-to-1 cost matrix is documented at the source, so the cost-based threshold has a citable anchor, and 1,000 rows fit a hand-counted confusion matrix.

## 3. Medical Cost Personal (insurance.csv)

| Fact | Value |
|---|---|
| Download | https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv, 54,288 bytes |
| Rows, columns | 1,338 rows, 7 columns: age, sex, bmi, children, smoker, region, charges; 1 duplicate row, no missing values |
| Licence at the source | No LICENSE file in the repository (https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/LICENSE returns 404, checked 28 October 2026). The README at https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/README.md says the files are the data for "Machine Learning with R" by Brett Lantz (Packt) and states: "All of these datasets are in the public domain but simply needed some cleaning up and recoding to match the format in the book." Under Chapter 6 it adds "insurance.csv could not be found online". |
| Kaggle mirror | mirichoi0218/insurance, 55,628 bytes, licence shown as "Database: Open Database, Contents: Database Contents" (https://www.kaggle.com/api/v1/datasets/view/mirichoi0218/insurance, verified 28 October 2026) |
| Charges | min 1,121.87, median 9,382.03, mean 13,270.42, max 63,770.43 dollars; non-smokers 1,064 rows (mean 8,434), smokers 274 rows (mean 32,050) |

Download code (tested):

```python
import pathlib, urllib.request, pandas as pd
DATA = pathlib.Path("data"); DATA.mkdir(exist_ok=True)
f = DATA / "insurance.csv"
if not f.exists():
    urllib.request.urlretrieve("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv", f)
insurance = pd.read_csv(f)
```

Linear regression of charges on all features (one-hot with the first level dropped, in-sample fit): intercept -11,938.54; age +256.86; bmi +339.19; children +475.50; sex_male -131.31; smoker_yes +23,848.53; region_northwest -352.96; region_southeast -1,035.02; region_southwest -960.05. R squared 0.7509, RMSE 6,041.68.

What one coefficient means in dollars: smoker_yes = 23,848.53 says that a smoker is predicted to cost 23,849 dollars a year more than a non-smoker of the same age, bmi, number of children, sex and region. The age coefficient says each extra year of age adds about 257 dollars to predicted charges, everything else held fixed.

What the residual plots show (plot at `/tmp/claude-0/-home-user-c2-content-factory/3ce39546-7624-54a7-a8da-ce3bf0688b7c/scratchpad/datasets/insurance_residuals.png`): the residuals split into bands; they do not bow with age.

- Against age: three flat horizontal stripes. Smokers form two parallel bands at about +7,000 to +9,000 and at about -8,000 to -11,000, present at every age. Non-smokers sit in a tight band around zero with a scatter of large positive outliers: 70 of 1,064 non-smokers (6.6 percent) have a residual above +10,000. Residual means by age bin run from -943 to +949 dollars, so there is no curve in age.
- Against predicted charges: the non-smoker band slopes from about +3,000 at the cheapest predictions to about -5,000 near 17,000 (the straight line over-predicts the cheapest customers), and the smokers, predicted at 23,000 to 40,000, split cleanly into two bands by bmi: bmi below 30 has mean residual -8,790 (129 rows), bmi 30 or more has mean residual +7,820 (145 rows). An additive model cannot express that smoking costs far more when bmi is over 30.

Traps in loading: none in the file itself (clean comma CSV, three string columns to encode). The trap is provenance: the only licence statement is a README claim, and the repository itself says it could not find the file online. The requester decides whether that claim is enough; the Kaggle mirror's licence line is a second statement, not a stronger one.

Verdict: Monday's regression chapter (the residual bands are the reason to look at residuals at all) and Wednesday's feature-engineering reprise, where one interaction feature (smoker and bmi over 30) is the fix the bands point at.

## 4. Olist Brazilian E-Commerce (Kaggle olistbr/brazilian-ecommerce)

| Fact | Value |
|---|---|
| Download | https://www.kaggle.com/api/v1/datasets/download/olistbr/brazilian-ecommerce, 44,717,580 bytes zip, no login needed (HTTP 200, content-type application/zip, under 2 s here) |
| Inside | 9 CSVs, 126,186,995 bytes extracted: orders 17,654,914 (99,441 rows x 8), customers 9,033,957 (99,441 x 5), order_items 15,438,671, reviews 14,451,670, payments 5,777,138, products 2,379,446, sellers 174,703, category translation 2,613, geolocation 61,273,883 |
| Licence | CC BY-NC-SA 4.0, stated in the page's structured data on https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce (`"license":{"name":"CC BY-NC-SA 4.0","url":"https://creativecommons.org/licenses/by-nc-sa/4.0/"}`) and as `licenseName` in https://www.kaggle.com/api/v1/datasets/view/olistbr/brazilian-ecommerce, both verified 28 October 2026; dataset version 2, last updated 1 October 2021 |
| Period | purchases 2016-09-04 to 2018-10-17; order_status delivered 96,478, shipped 1,107, canceled 625, unavailable 609, invoiced 314, processing 301, created 5, approved 2 |
| Repeat purchase | 96,096 distinct customer_unique_id; 2,997 have more than one order (3.12 percent); delivered orders only: 2,801 of 93,358 (3.00 percent); distribution 1 order 93,099, 2 orders 2,745, 3 orders 203, 4 orders 30, maximum 17 |

Download code (tested; the tables are read straight out of the cached zip):

```python
import pathlib, urllib.request, zipfile, pandas as pd
DATA = pathlib.Path("data"); DATA.mkdir(exist_ok=True)
z = DATA / "brazilian-ecommerce.zip"
if not z.exists():
    urllib.request.urlretrieve("https://www.kaggle.com/api/v1/datasets/download/olistbr/brazilian-ecommerce", z)
zf = zipfile.ZipFile(z)
orders = pd.read_csv(zf.open("olist_orders_dataset.csv"))
customers = pd.read_csv(zf.open("olist_customers_dataset.csv"))
```

Traps in loading:

- `customer_id` is one per order (99,441 distinct); the person is `customer_unique_id` (96,096 distinct). A repeat-purchase count on `customer_id` returns zero repeaters.
- The geolocation table is 61 MB and is never needed for a model; open members by name instead of extracting the zip.
- A repeat-purchase label at 3 percent, with 2,745 of the 2,997 repeaters at exactly two orders, leaves almost no signal to learn and makes every accuracy figure look like 97 percent.
- The licence carries a NonCommercial clause. A fee-charging diploma needs a ruling before the file enters a pack.

Verdict: not for Week 5. The signal is too thin for the metric and overfitting days and the licence is the wrong one; hold it for a retail week, with a review or delivery-delay question, once the licence is ruled on.

## 5. IBM Telco Customer Churn

| Fact | Value |
|---|---|
| Download | https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv, 970,457 bytes |
| Rows, columns | 7,043 rows, 21 columns; customerID unique, no duplicate rows |
| Target | Churn = Yes in 1,869 rows (26.54 percent), No in 5,174; by contract: month-to-month 42.71 percent, one year 11.27 percent, two year 2.83 percent |
| Licence at the source | The repository LICENSE file is the Apache License, Version 2.0 (https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/LICENSE, fetched 28 October 2026). The README (https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/README.md) says: "This code pattern is licensed under the Apache Software License, Version 2. Separate third party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses." The CSV has no separate terms in the repository. |
| Kaggle mirror | blastchar/telco-customer-churn, 977,501 bytes, licence shown as "Data files © Original Authors" (https://www.kaggle.com/api/v1/datasets/view/blastchar/telco-customer-churn, verified 28 October 2026) |

Download code (tested):

```python
import pathlib, urllib.request, pandas as pd
DATA = pathlib.Path("data"); DATA.mkdir(exist_ok=True)
f = DATA / "Telco-Customer-Churn.csv"
if not f.exists():
    urllib.request.urlretrieve("https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv", f)
telco = pd.read_csv(f)
telco["TotalCharges"] = pd.to_numeric(telco["TotalCharges"], errors="coerce")
```

Traps in loading:

- `TotalCharges` arrives as text because 11 rows hold a single space; all 11 have tenure 0 (new customers). `pd.to_numeric(errors="coerce")` turns them into NaN, which then needs a decision (fill with 0 or drop).
- `SeniorCitizen` is 0/1 while every other flag is the string Yes or No, so a blanket one-hot pass treats it differently.
- The dataset's own terms are not stated apart from the repository's Apache 2.0, which the README scopes to the code pattern.

Verdict: the fallback classification set, and a good take-home transfer: a clean file in a new domain with a 26.5 percent base rate, so a learner repeats Tuesday's threshold work where accuracy is less misleading and sees the difference.

## Recommendation

Carry the week on UCI Bank Marketing, `bank-additional-full.csv`, from Monday to Friday. It is CC BY 4.0, one 5.8 MB file, 41,188 rows, and every day's lesson is already inside it: the split and the baseline (88.74 percent) on Monday; the metric trap on Tuesday, where 90.09 percent accuracy hides recall 0.219 at an 11.27 percent base rate and a threshold of 0.2 trades it for recall 0.595; the duration leak on Wednesday, worth +0.14 AUC and documented at the source in a sentence the room can read, next to the 999 sentinel, the `unknown` labels and the collinear macro trio whose euribor3m coefficient flips from -0.93 to +0.78; the unlimited tree at 99.54 percent train and 84.20 percent validation on Thursday, with the forest at 0.787 and the boosted model at 0.814 against the logistic 0.801; and a Friday memo that has to choose between 0.801 and 0.814 with a cost-based threshold and the leak left out.

Serve the lending transfer on Tuesday with German Credit (OpenML credit-g, 1,000 rows, 30 percent bad): its 5-to-1 cost matrix is documented at UCI and OpenML, so the cost-based threshold rests on a source rather than an invented number.

Serve the regression chapter on Monday with Medical Cost Personal (1,338 rows): the smoker coefficient of 23,849 dollars is readable by a newcomer and the residuals split into bands by smoking and bmi over 30, which is the one picture that explains why residuals are inspected. Its provenance is the weakest of the five (a README claim of public domain and no licence file), and the requester should rule on it.

Keep Telco as the fallback and the take-home transfer. Leave Olist out of Week 5: 3.12 percent repeaters and a NonCommercial licence.

# Mock R2, the written half: can you check a vendor's card model on paper?

Thirty minutes, alone, on paper. No laptop, no phone, no AI and no notes. Write each letter in the
answer box on the last page, and show your working under each Part C item.

## What has the vendor sent Rohan?

A vendor offers Rohan Desai a scoring model for card defaults and shares its test results on a card
book of its own. **Every number on this sheet is invented**, and none of it comes from your group's
data.

| The vendor's book | |
|---|---|
| Accounts | 10,000 |
| Default next month | 2,000 accounts, 20 percent |
| Held out as a test set | 2,000 accounts, of whom 400 default |
| A missed default (not called, then defaults) | costs 5 units |
| A wasted call (called, then pays) | costs 1 unit |

The **error bill** of a list is 1 unit for every wasted call plus 5 units for every missed default.
A **threshold** is the chance of default above which an account is called.

**Exhibit 1. The vendor's model at three thresholds, on the 2,000 test accounts.**

| Threshold | Accounts called | Defaulters among them | Accuracy |
|---|---|---|---|
| 0.50 | 220 | 160 | 85.0 percent |
| 0.17 | 900 | 330 | 68.0 percent |
| 0.05 | 1,800 | 395 | 29.5 percent |

## Part A: what does each number tell Rohan?

One correct option each, about two minutes each.

<div style="page-break-inside: avoid">

### 1. On the test set, what does calling nobody score?

a) 20 percent accuracy, a bill of 2,000 units

b) 80 percent accuracy, a bill of 2,000 units

c) 80 percent accuracy, a bill of 400 units

d) 80 percent accuracy, a bill of 0 units

</div>

<div style="page-break-inside: avoid">

### 2. Above what chance of default does a call pay for itself?

a) 0.50

b) 0.20

c) 0.17

d) 0.83

</div>

<div style="page-break-inside: avoid">

### 3. The list is built on the 1st, before this month's statement. Which column may it use?

a) Last month's statement balance

b) Payments missed by the month's end

c) Whether collections called this month

d) The amount paid after the due date

</div>

<div style="page-break-inside: avoid">

### 4. The model's top 200 test accounts hold 110 defaulters. How many times the defaulters of a random 200 is that?

a) 0.55 times

b) 1.38 times

c) 5.50 times

d) 2.75 times

</div>

<div style="page-break-inside: avoid">

### 5. Boosting scores AUC 0.95 on its training rows and 0.74 on validation; logistic regression scores 0.77 and 0.76. Which call fits?

a) Ship logistic: boosting memorised

b) Ship boosting: 0.95 beats 0.77

c) Ship neither: both AUCs are below 0.80

d) Ship boosting: its gap will close in use

</div>

<div style="page-break-inside: avoid">

### 6. Rohan wants one number to pay his callers by. Which keeps them working on what the list is for?

a) Calls completed per caller per day

b) Share of the list called by the due date

c) Defaulters reached before the due date

d) Average call length, in minutes

</div>

<div class="page-break"></div>

## Part B: true or false, and why?

Pick the option whose verdict and reason are both right, about two and a half minutes each.

<div style="page-break-inside: avoid">

### 7. Fitting the scaler on all 10,000 accounts before five-fold cross-validation gives an honest estimate. True or false?

a) True, because a scaler never sees the labels

b) False, because scaling changes who defaults

c) True, because every fold then shares the same scale

d) False, because the scaler saw the held-out folds

</div>

<div style="page-break-inside: avoid">

### 8. Since the model's accuracy is highest at 0.50 in Exhibit 1, should Rohan use 0.50?

a) True, because accuracy counts both mistakes

b) False, because 0.17 costs 340 units less

c) True, because 0.50 calls the fewest accounts

d) False, because accuracy is highest at 0.17

</div>

<div class="page-break"></div>

## Part C: what does the arithmetic say?

Write the number with its unit, and the working that gets you there; about four minutes each.

### 9. Using Exhibit 1, what are the error bills of the 0.05 list and of calling every test account, and which costs Rohan less, by how much?

<div style="height:46mm"></div>


### 10. Rohan's team can make only 300 calls. The model's top 300 hold 150 defaulters; the rule "sort by months late" puts 138 defaulters in its top 300. What is each list's error bill on the test set, and how many more defaulters does the model reach?

<div style="height:46mm"></div>


### 11. Over the last six months the vendor's book defaulted at 18, 19, 21, 20, 22 and 21 percent. For next month the model forecasts 19 percent and "same as last month" forecasts 21 percent. The month comes in at 22 percent. How many accounts of the 10,000 does each forecast miss by, and which forecast was better?

<div style="height:46mm"></div>


<div class="page-break"></div>

## Where do your answers go?

Name: ______________________ Group: ______

| Item | Your letter |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |

| Item | Your number, with its unit |
|---|---|
| 9 | |
| 10 | |
| 11 | |

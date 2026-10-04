# Credit Default Risk Prediction

## Problem Statement
Which applicant and credit-history features most reliably predict loan default,
and can a model meaningfully outperform a simple baseline?

## Data Source
[Home Credit Default Risk (Kaggle)](https://www.kaggle.com/competitions/home-credit-default-risk)
- `application_train.csv` — ~307K applicants, 122 features, binary target (`TARGET`: 1 = payment difficulties, 0 = repaid on time)
- Note: dataset is imbalanced (majority class = repaid on time)

## Tech Stack
Python · MySQL · Pandas · NumPy · Matplotlib · Seaborn · scikit-learn · Power BI · Git

## Approach
1. Loaded raw data into a local MySQL database
2. Explored default rates by income, age, education, and employment length using SQL queries
3. Cleaned data and engineered new features (e.g. debt-to-income ratio, credit-to-annuity ratio)
4. Built and validated a baseline (logistic regression) and improved model (Random Forest / LightGBM)
5. Evaluated using AUC-ROC (not accuracy, due to class imbalance)
6. Built a Power BI dashboard summarizing key default-risk drivers

## Key Results
- Best model: _[fill in]_
- AUC-ROC: _[fill in]_
- Kaggle leaderboard percentile (if submitted): _[fill in]_

## Key Findings
- **Age is one of the strongest single predictors of default risk.** Default rate
  declines steadily from ~13.5% at age 21 to ~2.5% at age 68 — roughly a 5x
  difference across the age range. Employment length shows the same pattern
  (11.2% for under 2 years vs. 5.2% for 10+ years), suggesting both reflect
  a broader "financial stability increases with life stage" effect.

- **Education level shows the cleanest trend in the dataset**, with default rate
  falling steadily from 10.9% (lower secondary) to 5.4% (higher education).
  Note: the "academic degree" group (1.8%) has only 164 applicants and should
  be treated with caution given the small sample size.

- **Raw income is not a clean predictor of default risk.** Mid-income applicants
  actually default slightly more often (8.6%) than low-income applicants (8.2%),
  with only high-income applicants showing a clearly lower rate (7.1%).

- **Loan-to-income ratio doesn't behave as expected either.** Mid-ratio applicants
  (2-5x income) default most (8.7%), while both low- and high-ratio groups are
  lower (~7.4%). Likely explanation: lenders may apply stricter approval standards
  to high-ratio applicants, filtering out the riskiest borrowers before approval
  (selection bias) — a reminder that approved-loan data doesn't show the full
  applicant pool.

![Default rate by age] (C:\Users\Ian\OneDrive\Desktop\credit-risk-default-prediction\images\default_rate_by_age.png)

## Dashboard
_[Insert Power BI dashboard screenshot here]_

## Limitations & Next Steps
_[Be honest — what would you do with more time/data? e.g. bring in the linked tables
(bureau.csv, previous_application.csv), try hyperparameter tuning, address class imbalance further]_

## How to Run
1. Clone this repo
2. `pip install -r requirements.txt`
3. Download `application_train.csv` from the Kaggle link above into `/data`
4. Load into MySQL (see `/src/load_data.py`)
5. Run notebooks in `/notebooks` in order

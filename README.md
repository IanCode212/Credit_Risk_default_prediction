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
_[2-4 bullet points, plain English — e.g. "Applicants with X had Y% higher default rates"]_

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

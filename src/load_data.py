"""
Loads application_train.csv into a local MySQL database.

Before running:
1. Install MySQL Server + create a database, e.g.:
     CREATE DATABASE credit_risk;
2. Fill in your credentials below (or better, load them from a .env file
   that's git-ignored — don't commit real passwords).
3. pip install -r requirements.txt
"""

import pandas as pd
from sqlalchemy import create_engine

# --- fill these in ---
DB_USER = "root"
DB_PASSWORD = "your_password_here"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "credit_risk"
CSV_PATH = "../data/application_train.csv"
TABLE_NAME = "applications"
# ----------------------

def main():
    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    print(f"Reading {CSV_PATH} ...")
    df = pd.read_csv(CSV_PATH)
    print(f"Loaded {len(df):,} rows, {df.shape[1]} columns")

    print(f"Writing to MySQL table '{TABLE_NAME}' ...")
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False, chunksize=5000)
    print("Done. You can now query this table from MySQL Workbench or your notebooks.")

if __name__ == "__main__":
    main()

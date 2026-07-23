"""
Data Cleaning Script for Health Behavior Pipeline.
Reads raw data from data/raw/, handles missing values, removes duplicates,
standardizes data types, and exports cleaned dataset to data/interim/.
"""

import pandas as pd
from .utils import load_raw_data, save_interim_data


def run_cleaning_pipeline():
    print("[INFO] Starting raw data cleaning pipeline...")

    # 1. Load Raw Data from data/raw/
    df = load_raw_data("ObesityDataSet_raw_and_data_sinthetic.csv")
    print(f"[INFO] Raw dataset loaded. Initial shape: {df.shape}")

    # 2. Handle Missing Values (if any)
    if df.isnull().sum().sum() > 0:
        print("[INFO] Handling missing values...")
        df = df.dropna().reset_index(drop=True)
    else:
        print("[INFO] No missing values detected.")

    # 3. Define Valid Technical Domain Ranges: 'Column': (min_value, max_value)
    technical_ranges = {
        "FCVC": (1, 3),  # Frequency of consumption of vegetables
        "NCP": (1, 3),   # Number of main meals
        "CH2O": (1, 3),  # Daily consumption of water
        "FAF": (0, 3),   # Physical activity frequency
        "TUE": (0, 2),   # Time using technology devices
    }

    print("[INFO] Applying domain constraints and rounding behavioral features...")
    
    # Explicitly fix NCP upper bound before transformation
    df.loc[df["NCP"] > 3, "NCP"] = 3

    # Apply transformation loop: Round -> Clip -> Cast to int
    for col, (min_val, max_val) in technical_ranges.items():
        df[col] = df[col].round(0).clip(lower=min_val, upper=max_val).astype(int)

    # 3. Standardize Biometric Metrics Precision
    print("[INFO] Standardizing biometric metrics precision...")
    df["Age"] = df["Age"].round(0).astype(int)
    df["Height"] = df["Height"].round(2)
    df["Weight"] = df["Weight"].round(1)

    # 4. Save Cleaned Dataset to data/interim/
    save_interim_data(df, "ObesityDataSet_cleaned.csv")
    print(f"[INFO] Data cleaning completed successfully! Final shape: {df.shape}\n")


if __name__ == "__main__":
    run_cleaning_pipeline()
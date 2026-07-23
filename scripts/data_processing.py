"""
Data Preprocessing Pipeline for Health Behavior Analysis.
Reads cleaned data from data/interim/, performs custom categorical encoding (binary, ordinal, one-hot),
isolates behavioral features from physical metrics, scales continuous variables, and exports artifacts to data/processed/.
"""

import warnings
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

from .utils import get_project_root, load_interim_data, save_processed_data

warnings.filterwarnings("ignore")


def run_processing_pipeline():
    print("[INFO] Starting data preprocessing pipeline...")

    # 1. Load Interim Data
    df = load_interim_data("ObesityDataSet_cleaned.csv")

    # Calculate BMI solely for post-clustering profiling vector
    df["BMI"] = df["Weight"] / (df["Height"] ** 2)
    print(f"[INFO] Dataset successfully loaded from interim. Shape: {df.shape}")

    df_encoded = df.copy()

    # 2. Binary Mapping
    binary_cols = ["family_history_with_overweight", "FAVC", "SMOKE", "SCC"]
    for col in binary_cols:
        df_encoded[col] = df_encoded[col].map({"yes": 1, "no": 0})

    df_encoded["Gender"] = df_encoded["Gender"].map({"Female": 0, "Male": 1})

    # 3. Ordinal Frequency Mapping
    freq_map = {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
    df_encoded["CAEC"] = df_encoded["CAEC"].map(freq_map)
    df_encoded["CALC"] = df_encoded["CALC"].map(freq_map)

    # 4. One-Hot Encoding for Unordered Nominals (MTRANS)
    df_encoded = pd.get_dummies(df_encoded, columns=["MTRANS"], prefix="MTRANS", drop_first=True, dtype=int)

    # 5. Target Label Encoding (Reserved for Validation Only)
    target_mapping = {
        "Insufficient_Weight": 0,
        "Normal_Weight": 1,
        "Overweight_Level_I": 2,
        "Overweight_Level_II": 3,
        "Obesity_Type_I": 4,
        "Obesity_Type_II": 5,
        "Obesity_Type_III": 6,
    }
    df_encoded["NObeyesdad_encoded"] = df_encoded["NObeyesdad"].map(target_mapping)

    print("[INFO] Categorical encoding successfully completed.")

    # 6. Isolate Pure Behavioral and Genetic Features (Exclude Physical Metric Space)
    X_cols = [
        "Age",
        "Gender",
        "family_history_with_overweight",
        "FAVC",
        "FCVC",
        "NCP",
        "CAEC",
        "CH2O",
        "SCC",
        "FAF",
        "TUE",
        "CALC",
        "SMOKE",
    ] + [col for col in df_encoded.columns if col.startswith("MTRANS_")]

    X = df_encoded[X_cols]

    # 7. Isolate Physical Metrics and Targets for Cluster Profiling
    y_class = df_encoded[["NObeyesdad_encoded"]]
    y_bmi = df_encoded[["BMI"]]

    # 8. Apply StandardScaler ONLY to Continuous Variables
    continuous_cols = ["Age", "FCVC", "NCP", "CH2O", "FAF", "TUE"]

    scaler = StandardScaler()
    X_scaled = X.copy()
    X_scaled[continuous_cols] = scaler.fit_transform(X[continuous_cols])

    # 9. Export Fitted Scaler Object
    root = get_project_root()
    models_dir = root / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(scaler, models_dir / "standard_scaler_clustering.pkl")
    print(f"[INFO] Scaler saved to: {models_dir / 'standard_scaler_clustering.pkl'}")

    # 10. Save processed feature matrix and target validation vectors
    save_processed_data(X_scaled, "X_scaled_clustering.csv")
    save_processed_data(y_class, "y_classification.csv")
    save_processed_data(y_bmi, "y_regression_bmi.csv")

    print("[INFO] All processed artifacts exported successfully to 'data/processed/':")
    print(" - X_scaled_clustering.csv (Clustering Input)")
    print(" - y_classification.csv (Post-Clustering Label Profiling)")
    print(" - y_regression_bmi.csv (Post-Clustering Metric Profiling)\n")


if __name__ == "__main__":
    run_processing_pipeline()
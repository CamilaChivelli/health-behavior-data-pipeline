"""
K-Means Clustering Model Training Script.
Fits K-Means (K=4) on standardized behavioral features, assigns cluster labels
to feature matrices and target validation vectors, and exports model artifacts.
"""

import joblib
import pandas as pd
from sklearn.cluster import KMeans

from utils import get_project_root, save_processed_data

OPTIMAL_K = 4


def run_training_pipeline():
    print(f"[INFO] Starting K-Means training pipeline (Optimal K={OPTIMAL_K})...")

    root = get_project_root()
    processed_dir = root / "data" / "processed"

    # 1. Load Processed Datasets from data/processed/
    X_scaled_path = processed_dir / "X_scaled_clustering.csv"
    y_bmi_path = processed_dir / "y_regression_bmi.csv"
    y_class_path = processed_dir / "y_classification.csv"

    if not X_scaled_path.exists():
        raise FileNotFoundError(
            f"Missing processed features at: {X_scaled_path}. Please run data_processing.py first."
        )

    X_scaled = pd.read_csv(X_scaled_path)
    y_bmi = pd.read_csv(y_bmi_path) if y_bmi_path.exists() else None
    y_class = pd.read_csv(y_class_path) if y_class_path.exists() else None

    # 2. Fit Final K-Means Model
    print(f"[INFO] Fitting K-Means model with K={OPTIMAL_K}...")
    kmeans_final = KMeans(n_clusters=OPTIMAL_K, random_state=42, n_init=20)
    cluster_labels = kmeans_final.fit_predict(X_scaled)

    # 3. Assign Cluster Labels to Feature Matrix and Target Validation Sets
    X_scaled["Cluster"] = cluster_labels

    if y_bmi is not None:
        y_bmi["Cluster"] = cluster_labels
        save_processed_data(y_bmi, "y_regression_bmi.csv")

    if y_class is not None:
        y_class["Cluster"] = cluster_labels
        save_processed_data(y_class, "y_classification.csv")

    # 4. Save Trained Model Object
    models_dir = root / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    model_path = models_dir / "kmeans_behavioral_model.pkl"

    joblib.dump(kmeans_final, model_path)
    print(f"[INFO] Fitted KMeans model exported to: {model_path}")

    # 5. Export Processed Feature Matrix with Assigned Cluster Labels
    save_processed_data(X_scaled, "X_scaled_with_clusters.csv")

    print(f"\n[SUCCESS] K-Means model fitted successfully with K={OPTIMAL_K}.")
    print("Observation distribution per cluster:")
    print(X_scaled["Cluster"].value_counts().sort_index())
    print("\n[INFO] Clustering training pipeline completed successfully!\n")


if __name__ == "__main__":
    run_training_pipeline()
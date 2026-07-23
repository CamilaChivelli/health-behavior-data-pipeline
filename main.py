"""
Main Execution Script for the Health Behavior Analysis Pipeline.
Runs the end-to-end data pipeline from raw data cleaning to model training.
"""

from scripts.data_cleaning import run_cleaning_pipeline
from scripts.data_processing import run_processing_pipeline
from scripts.train_clustering import run_training_pipeline


def main():
    print("==================================================")
    print("🚀 STARTING HEALTH BEHAVIOR PIPELINE EXECUTION 🚀")
    print("==================================================\n")

    # Step 1: Clean raw data -> data/interim
    run_cleaning_pipeline()

    # Step 2: Feature Engineering & Scaling -> data/processed
    run_processing_pipeline()

    # Step 3: Train K-Means Model -> models/ & data/processed
    run_training_pipeline()

    print("==================================================")
    print("✅ END-TO-END PIPELINE EXECUTED SUCCESSFULLY! ✅")
    print("==================================================")


if __name__ == "__main__":
    main()
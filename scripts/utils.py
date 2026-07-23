"""
Utility functions for file I/O and path management across raw, interim, and processed data layers.
"""

from pathlib import Path
import pandas as pd


def get_project_root() -> Path:
    """Returns the absolute path to the project root directory."""
    return Path(__file__).resolve().parent.parent


def load_raw_data(filename: str = "ObesityDataSet_raw_and_data_sinthetic.csv") -> pd.DataFrame:
    """Loads raw dataset from data/raw directory."""
    root = get_project_root()
    data_path = root / "data" / "raw" / filename
    if not data_path.exists():
        raise FileNotFoundError(f"Raw data file not found at: {data_path}")
    return pd.read_csv(data_path)


def load_interim_data(filename: str = "cleaned_data.csv") -> pd.DataFrame:
    """Loads cleaned interim dataset from data/interim directory."""
    root = get_project_root()
    data_path = root / "data" / "interim" / filename
    if not data_path.exists():
        raise FileNotFoundError(f"Interim data file not found at: {data_path}")
    return pd.read_csv(data_path)


def save_interim_data(df: pd.DataFrame, filename: str = "cleaned_data.csv") -> None:
    """Saves a DataFrame to the data/interim directory after initial cleaning."""
    root = get_project_root()
    output_path = root / "data" / "interim" / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[INFO] Interim dataset successfully saved to: {output_path}")


def save_processed_data(df: pd.DataFrame, filename: str) -> None:
    """Saves a DataFrame to the data/processed directory."""
    root = get_project_root()
    output_path = root / "data" / "processed" / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[INFO] Processed dataset successfully saved to: {output_path}")
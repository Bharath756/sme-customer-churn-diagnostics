"""
data_prep.py

Purpose:
Reusable data preparation utilities for SME churn diagnostics.
This module handles data loading, cleaning, and basic feature preparation.
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load raw customer data from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the raw data file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """
    return pd.read_csv(file_path)


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning operations.

    Steps:
    - Standardize column names
    - Handle missing values
    - Remove duplicate records

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        Cleaned dataset.
    """
    df = df.copy()

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove duplicate rows
    df = df.drop_duplicates()

    return df


def prepare_churn_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare dataset for churn diagnostics.

    This function can be extended later for:
    - Feature engineering
    - Time-based transformations
    - Label creation

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        Prepared dataset.
    """
    df = basic_cleaning(df)

    return df

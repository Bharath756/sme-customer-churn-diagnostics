"""
churn_metrics.py

Purpose:
Reusable metrics and calculations for churn diagnostics and analysis.
"""

import pandas as pd


def calculate_churn_rate(
    df: pd.DataFrame,
    churn_column: str
) -> float:
    """
    Calculate overall churn rate.

    Parameters
    ----------
    df : pd.DataFrame
    churn_column : str
        Column indicating churn (1 = churned, 0 = active)

    Returns
    -------
    float
        Churn rate as a percentage.
    """
    churned = df[churn_column].sum()
    total = len(df)

    if total == 0:
        return 0.0

    return round((churned / total) * 100, 2)


def churn_rate_by_segment(
    df: pd.DataFrame,
    segment_column: str,
    churn_column: str
) -> pd.DataFrame:
    """
    Calculate churn rate by customer segment.

    Parameters
    ----------
    df : pd.DataFrame
    segment_column : str
    churn_column : str

    Returns
    -------
    pd.DataFrame
        Churn rate by segment.
    """
    summary = (
        df
        .groupby(segment_column)[churn_column]
        .agg(["count", "sum"])
        .reset_index()
    )

    summary["churn_rate_pct"] = (
        summary["sum"] / summary["count"] * 100
    ).round(2)

    return summary

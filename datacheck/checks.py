import pandas as pd
import numpy as np


def check_missing_values(df: pd.DataFrame) -> dict:
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    issues = {}
    for col in df.columns:
        if missing[col] > 0:
            issues[col] = {
                "count": int(missing[col]),
                "percentage": float(missing_pct[col])
            }
    return {
        "status": "⚠️  Issues found" if issues else "✅ No issues",
        "issues": issues,
        "total_missing_cells": int(missing.sum())
    }


def check_duplicates(df: pd.DataFrame) -> dict:
    n_duplicates = df.duplicated().sum()
    return {
        "status": "⚠️  Issues found" if n_duplicates > 0 else "✅ No issues",
        "duplicate_row_count": int(n_duplicates),
        "percentage": round(n_duplicates / len(df) * 100, 2)
    }


def check_constant_columns(df: pd.DataFrame) -> dict:
    constant_cols = [col for col in df.columns if df[col].nunique() <= 1]
    return {
        "status": "⚠️  Issues found" if constant_cols else "✅ No issues",
        "constant_columns": constant_cols
    }


def check_outliers(df: pd.DataFrame) -> dict:
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    issues = {}
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outlier_count = ((df[col] < lower) | (df[col] > upper)).sum()
        if outlier_count > 0:
            issues[col] = {
                "outlier_count": int(outlier_count),
                "percentage": round(outlier_count / len(df) * 100, 2),
                "lower_bound": round(lower, 4),
                "upper_bound": round(upper, 4)
            }
    return {
        "status": "⚠️  Issues found" if issues else "✅ No issues",
        "issues": issues
    }


def check_data_types(df: pd.DataFrame) -> dict:
    type_summary = {}
    suspicious = []
    for col in df.columns:
        dtype = str(df[col].dtype)
        type_summary[col] = dtype
        if dtype == "object":
            suspicious.append(col)
    return {
        "status": "ℹ️  Review suggested" if suspicious else "✅ No issues",
        "type_summary": type_summary,
        "object_columns": suspicious
    }


def check_class_imbalance(df: pd.DataFrame, target_col: str) -> dict:
    if target_col not in df.columns:
        return {"status": "❌ Column not found", "column": target_col}
    counts = df[target_col].value_counts()
    percentages = (counts / len(df) * 100).round(2)
    minority_pct = float(percentages.iloc[-1])
    imbalanced = minority_pct < 20
    return {
        "status": "⚠️  Imbalanced" if imbalanced else "✅ Balanced",
        "column": target_col,
        "class_distribution": percentages.to_dict(),
        "minority_class_percentage": minority_pct
    }
    
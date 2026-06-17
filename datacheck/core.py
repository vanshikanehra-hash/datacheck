import pandas as pd
from datacheck.checks import (
    check_missing_values,
    check_duplicates,
    check_class_imbalance,
    check_outliers,
    check_constant_columns,
    check_data_types,
)


def run_checks(filepath: str, target_col: str = None) -> dict:
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        raise
    except Exception as e:
        print(f"❌ Could not load file: {e}")
        raise

    print(f"✅ Loaded dataset: {df.shape[0]} rows × {df.shape[1]} columns\n")

    results = {
        "shape": df.shape,
        "missing_values": check_missing_values(df),
        "duplicates": check_duplicates(df),
        "constant_columns": check_constant_columns(df),
        "outliers": check_outliers(df),
        "data_types": check_data_types(df),
        "class_imbalance": check_class_imbalance(df, target_col) if target_col else None,
    }

    return results
    
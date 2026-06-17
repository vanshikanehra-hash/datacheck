def print_section(title: str, content: dict):
    print(f"{'─' * 50}")
    print(f"  {title}")
    print(f"{'─' * 50}")

    status = content.get("status", "")
    print(f"  Status : {status}")

    if "total_missing_cells" in content:
        print(f"  Total missing cells : {content['total_missing_cells']}")
        if content["issues"]:
            print("  Columns with missing values:")
            for col, info in content["issues"].items():
                print(f"    • {col}: {info['count']} missing ({info['percentage']}%)")

    if "duplicate_row_count" in content:
        print(f"  Duplicate rows : {content['duplicate_row_count']} ({content['percentage']}%)")

    if "constant_columns" in content and content["constant_columns"]:
        print(f"  Constant columns : {', '.join(content['constant_columns'])}")

    if content.get("issues") and any("outlier_count" in str(v) for v in content.get("issues", {}).values()):
        print("  Columns with outliers:")
        for col, info in content["issues"].items():
            print(f"    • {col}: {info['outlier_count']} outliers ({info['percentage']}%)")

    if "object_columns" in content and content["object_columns"]:
        print(f"  Object-type columns (may need encoding): {', '.join(content['object_columns'])}")

    if "class_distribution" in content:
        print(f"  Column : {content['column']}")
        print("  Class distribution:")
        for cls, pct in content["class_distribution"].items():
            print(f"    • {cls}: {pct}%")

    print()


def print_report(results: dict):
    rows, cols = results["shape"]
    print(f"\n{'═' * 50}")
    print(f"  📊 DATACHECK REPORT")
    print(f"  Dataset: {rows} rows × {cols} columns")
    print(f"{'═' * 50}\n")

    print_section("1. MISSING VALUES", results["missing_values"])
    print_section("2. DUPLICATE ROWS", results["duplicates"])
    print_section("3. CONSTANT COLUMNS", results["constant_columns"])
    print_section("4. OUTLIERS (IQR method)", results["outliers"])
    print_section("5. DATA TYPES", results["data_types"])

    if results["class_imbalance"]:
        print_section("6. CLASS IMBALANCE", results["class_imbalance"])

    print(f"{'═' * 50}")
    print("  ✅ Audit complete. Fix issues above before training your model.")
    print(f"{'═' * 50}\n")
    
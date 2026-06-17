import argparse
from datacheck.core import run_checks
from datacheck.report import print_report


def main():
    parser = argparse.ArgumentParser(
        prog="datacheck",
        description="🔍 Audit any dataset for quality issues instantly."
    )
    parser.add_argument("filepath", help="Path to your CSV file")
    parser.add_argument("--target", help="Target column name (for class imbalance check)", default=None)
    args = parser.parse_args()

    print(f"\n📂 Loading dataset: {args.filepath}\n")
    results = run_checks(args.filepath, target_col=args.target)
    print_report(results)


if __name__ == "__main__":
    main()
    
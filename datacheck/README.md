# 🔍 datacheck — Dataset Quality Checker

> A lightweight Python CLI tool to audit any CSV dataset for quality issues before training ML models.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

-----

## Why?

Bad data = bad models. Before you train anything, you need to know:

- Are there missing values? Where?
- Are there duplicate rows wasting compute?
- Is your target column imbalanced?
- Are there outliers skewing your distributions?
- Do you have useless constant columns?

`datacheck` tells you all of this in one command.

-----

## Installation

```bash
git clone https://github.com/vanshikanehra-hash/datacheck.git
cd datacheck
pip install -e .
```

-----

## Usage

```bash
# Basic audit
datacheck path/to/your/dataset.csv

# With class imbalance check (for classification datasets)
datacheck path/to/your/dataset.csv --target label
```

-----

## Example Output

```
══════════════════════════════════════════════════
  📊 DATACHECK REPORT
  Dataset: 1000 rows × 8 columns
══════════════════════════════════════════════════

──────────────────────────────────────────────────
  1. MISSING VALUES
──────────────────────────────────────────────────
  Status : ⚠️  Issues found
  Total missing cells : 23
  Columns with missing values:
    • age: 15 missing (1.5%)
    • salary: 8 missing (0.8%)

──────────────────────────────────────────────────
  2. DUPLICATE ROWS
──────────────────────────────────────────────────
  Status : ⚠️  Issues found
  Duplicate rows : 12 (1.2%)

──────────────────────────────────────────────────
  4. OUTLIERS (IQR method)
──────────────────────────────────────────────────
  Status : ⚠️  Issues found
  Columns with outliers:
    • salary: 9 outliers (0.9%)

══════════════════════════════════════════════════
  ✅ Audit complete. Fix issues above before training your model.
══════════════════════════════════════════════════
```

-----

## Checks Performed

|Check           |Description                                   |
|----------------|----------------------------------------------|
|Missing Values  |Count and % of nulls per column               |
|Duplicate Rows  |Fully identical row detection                 |
|Constant Columns|Columns with zero variance (useless for ML)   |
|Outliers        |IQR-based outlier detection per numeric column|
|Data Types      |Flags object columns that may need encoding   |
|Class Imbalance |Minority class % in target column (optional)  |

-----

## Project Structure

```
datacheck/
│
├── datacheck/
│   ├── __init__.py
│   ├── cli.py        # Command line interface
│   ├── core.py       # Loads data and runs all checks
│   ├── checks.py     # Individual quality check functions
│   └── report.py     # Formats and prints the report
│
├── tests/
│   └── test_checks.py
│
├── setup.py
├── requirements.txt
└── README.md
```

-----

## Roadmap

- [x] Missing value detection
- [x] Duplicate row detection
- [x] Constant column detection
- [x] Outlier detection (IQR method)
- [x] Data type summary
- [x] Class imbalance check
- [ ] HTML report export
- [ ] Correlation matrix
- [ ] Support for Excel files (.xlsx)
- [ ] Auto-fix suggestions

-----

## Contributing

Contributions welcome! Please open an issue first to discuss what you’d like to change.
Run tests with:

```bash
pytest tests/
```

-----

## Author

**Vanshika Nehra** — B.Tech Data Science, Manipal University Jaipur  
Building toward GSoC 2027 🚀

[![GitHub](https://img.shields.io/badge/GitHub-vanshikanehra--hash-black?style=flat&logo=github)](https://github.com/vanshikanehra-hash)

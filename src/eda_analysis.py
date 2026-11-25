import pandas as pd
import numpy as np
import os

from pathlib import Path

# Project root (parent of src/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "supermarket_large_dataset.csv"
REPORT_PATH = PROJECT_ROOT / "reports" / "EDA_REPORT.md"

def run_eda():
    print(f"Loading dataset from {DATA_PATH}...")
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}.")

    df = pd.read_csv(DATA_PATH, low_memory=False)
    print(f"Dataset loaded successfully. Shape: {df.shape[0]:,} rows x {df.shape[1]:,} columns")

    lines = []
    def w(s=""):
        lines.append(str(s))

    w("# Exploratory Data Analysis (EDA) Report")
    w("## Supermarket Large Dataset (Multi-Store Retail Chain)")
    w("")
    w("### 1. Dataset Overview")
    w(f"- **Total Rows (Transactions/Line items):** `{df.shape[0]:,}`")
    w(f"- **Total Columns (Features):** `{df.shape[1]:,}`")
    w(f"- **Memory Usage:** `{df.memory_usage(deep=True).sum()/1024/1024:.2f} MB`")
    w(f"- **Duplicate Rows:** `{df.duplicated().sum():,}`")
    w("")

    w("### 2. Column Categories & Summary")
    cat_counts = df.dtypes.value_counts()
    w("Data types breakdown:")
    for dt, count in cat_counts.items():
        w(f"- `{dt}`: {count} columns")
    w("")

    w("### 3. Missing Values Check")
    miss = df.isna().sum()
    miss = miss[miss>0].sort_values(ascending=False)
    if len(miss):
        w("| Column | Missing Count | Percentage (%) |")
        w("|---|---|---|")
        for c, v in miss.items():
            w(f"| `{c}` | {v:,} | {v/len(df)*100:.2f}% |")
    else:
        w("No missing values found in the dataset.")
    w("")

    w("### 4. Key Numeric Statistics")
    num = df.select_dtypes(include=[np.number])
    desc = num.describe().T[['count', 'mean', 'std', 'min', '50%', 'max']]
    desc.columns = ['Count', 'Mean', 'Std', 'Min', 'Median', 'Max']
    w(desc.head(15).to_markdown())
    w("")

    w("### 5. Full Column Inventory")
    w("| No | Column Name | Data Type | Non-Null Count |")
    w("|---|---|---|---|")
    for i, c in enumerate(df.columns):
        nn = df[c].notna().sum()
        w(f"| {i+1} | `{c}` | `{df[c].dtype}` | {nn:,} |")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"EDA Report successfully generated at: {REPORT_PATH}")

if __name__ == "__main__":
    run_eda()

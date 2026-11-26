"""
EDA Stakeholder Insights Generator
==================================
This script generates the key findings documented in reports/EDA_STAKEHOLDER_INSIGHTS.md.
It calculates accurate aggregated metrics directly from the cleaned dataset.

Usage:
    python src/eda_stakeholder_insights.py
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_PATH = PROJECT_ROOT / "data" / "supermarket_cleaned.csv"

def generate_stakeholder_insights():
    print("="*70)
    print("GENERATING STAKEHOLDER INSIGHTS")
    print("="*70)

    df = pd.read_csv(INPUT_PATH, low_memory=False)
    print(f"Loaded {len(df):,} rows x {df.shape[1]} columns\n")

    # 1. Financial Overview
    print("\n💰 1. FINANCIAL OVERVIEW")
    total_rev = df['total_amount'].sum()
    total_profit = df['calculated_profit'].sum()
    margin = (total_profit / total_rev) * 100
    aov = df['total_amount'].mean()
    print(f"   Total Revenue: {total_rev:,.0f}")
    print(f"   Total Profit: {total_profit:,.0f}")
    print(f"   Overall Margin: {margin:.1f}%")
    print(f"   AOV: {aov:.2f}")

    # 2. Category Analysis (Correct Aggregated Margin)
    print("\n📦 2. TOP 5 CATEGORIES BY MARGIN %")
    cat = df.groupby('product_category').agg({
        'total_amount': 'sum',
        'calculated_profit': 'sum'
    })
    cat['margin_pct'] = (cat['calculated_profit'] / cat['total_amount']) * 100
    print(cat.sort_values('margin_pct', ascending=False)[['margin_pct', 'calculated_profit']].head(5).to_string())

    print("\n📦 2b. TOP 5 CATEGORIES BY PROFIT VALUE")
    print(cat.sort_values('calculated_profit', ascending=False)[['calculated_profit', 'total_amount']].head(5).to_string())

    # 3. Customer Segments
    print("\n👥 3. TOP SEGMENTS BY PROFIT")
    seg = df.groupby('customer_segment').agg({
        'calculated_profit': 'sum',
        'customer_lifetime_value': 'mean',
        'customer_id': 'nunique'
    }).sort_values('calculated_profit', ascending=False)
    print(seg.head(3).to_string())

    # 4. Top Stores
    print("\n🏪 4. TOP 5 STORES BY PROFIT")
    store = df.groupby('store_id').agg({
        'total_amount': 'sum',
        'calculated_profit': 'sum'
    })
    store['margin_pct'] = (store['calculated_profit'] / store['total_amount']) * 100
    print(store.sort_values('calculated_profit', ascending=False)[['calculated_profit', 'margin_pct']].head(5).to_string())

    # 5. Returns & Complaints
    print("\n⚠️  5. OPERATIONAL BOTTLENECKS")
    ret_rate = (df['return_flag'] == 'Yes').mean() * 100
    comp_rate = (df['complaint_flag'] == 'Yes').mean() * 100
    print(f"   Return Rate: {ret_rate:.2f}% | Complaint Rate: {comp_rate:.2f}%")
    print("   Top Returns by Category:")
    print(df[df['return_flag']=='Yes'].groupby('product_category').size().sort_values(ascending=False).head(3).to_string())

    # 6. Churn Risk
    print("\n🚨 6. CHURN RISK")
    high_churn = (df['customer_churn_risk'] > 0.7).sum()
    high_churn_pct = (df['customer_churn_risk'] > 0.7).mean() * 100
    print(f"   High Risk (>0.7): {high_churn:,} customers ({high_churn_pct:.1f}%)")

    # 7. Payment Methods
    print("\n💳 7. PAYMENT METHOD MIX")
    pay = df.groupby('payment_method')['total_amount'].sum()
    pay_pct = (pay / pay.sum() * 100).round(1)
    print(pd.DataFrame({'amount': pay, 'share_pct': pay_pct}).sort_values('amount', ascending=False).to_string())

    print("\n" + "="*70)
    print("INSIGHTS GENERATED - See reports/EDA_STAKEHOLDER_INSIGHTS.md")
    print("="*70)

if __name__ == "__main__":
    generate_stakeholder_insights()

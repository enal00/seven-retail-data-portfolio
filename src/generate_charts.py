"""
Visualization Generator for README.md
======================================
Generates PNG charts that support the analysis in README.md and
reports/EDA_STAKEHOLDER_INSIGHTS.md. Save output to reports/charts/.

Usage:
    python src/generate_charts.py
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_PATH = PROJECT_ROOT / "data" / "supermarket_cleaned.csv"
CHARTS_DIR = PROJECT_ROOT / "reports" / "charts"
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

def generate_charts():
    df = pd.read_csv(INPUT_PATH, low_memory=False)
    plt.style.use('ggplot')

    # 1. Profit Margin by Category (Top 10)
    cat = df.groupby('product_category').agg({
        'total_amount': 'sum',
        'calculated_profit': 'sum'
    })
    cat['margin_pct'] = (cat['calculated_profit'] / cat['total_amount']) * 100
    top_margin = cat.sort_values('margin_pct', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(top_margin.index[::-1], top_margin['margin_pct'][::-1], color='#2E86AB')
    ax.set_xlabel('Profit Margin (%)')
    ax.set_title('Top 10 Product Categories by Profit Margin (%)')
    for bar, val in zip(bars, top_margin['margin_pct'][::-1]):
        ax.text(val + 0.5, bar.get_y() + bar.get_height()/2, f'{val:.1f}%', va='center', fontsize=9)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / 'profit_margin_by_category.png', dpi=150)
    plt.close()
    print(f"Saved: {CHARTS_DIR / 'profit_margin_by_category.png'}")

    # 2. Top Categories by Profit Value
    top_profit = cat.sort_values('calculated_profit', ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(top_profit.index[::-1], top_profit['calculated_profit'][::-1], color='#A23B72')
    ax.set_xlabel('Total Profit')
    ax.set_title('Top 10 Categories by Total Profit')
    for bar, val in zip(bars, top_profit['calculated_profit'][::-1]):
        ax.text(val + 1000, bar.get_y() + bar.get_height()/2, f'{val:,.0f}', va='center', fontsize=9)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / 'profit_by_category.png', dpi=150)
    plt.close()
    print(f"Saved: {CHARTS_DIR / 'profit_by_category.png'}")

    # 3. Revenue & Profit Trend (Monthly)
    df['transaction_datetime'] = pd.to_datetime(df['transaction_datetime'])
    monthly = df.groupby(df['transaction_datetime'].dt.to_period('M')).agg({
        'total_amount': 'sum',
        'calculated_profit': 'sum'
    })
    monthly.index = monthly.index.to_timestamp()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(monthly.index, monthly['total_amount'], label='Revenue', marker='o', color='#2E86AB')
    ax.plot(monthly.index, monthly['calculated_profit'], label='Profit', marker='s', color='#F18F01')
    ax.set_title('Monthly Revenue & Profit Trend')
    ax.set_ylabel('Amount')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / 'revenue_profit_trend.png', dpi=150)
    plt.close()
    print(f"Saved: {CHARTS_DIR / 'revenue_profit_trend.png'}")

    # 4. Return Rate by Category
    ret = df[df['return_flag']=='Yes'].groupby('product_category').size().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(ret.index, ret.values, color='#C73E1D')
    ax.set_ylabel('Number of Returns')
    ax.set_title('Top 10 Categories by Return Count (Operational Bottleneck)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / 'returns_by_category.png', dpi=150)
    plt.close()
    print(f"Saved: {CHARTS_DIR / 'returns_by_category.png'}")

    # 5. Payment Method Mix (Pie)
    pay = df.groupby('payment_method')['total_amount'].sum()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(pay, labels=pay.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Payment Method Mix (by Revenue Share)')
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / 'payment_method_mix.png', dpi=150)
    plt.close()
    print(f"Saved: {CHARTS_DIR / 'payment_method_mix.png'}")

    # 6. Churn Risk Distribution
    fig, ax = plt.subplots(figsize=(8, 5))
    bins = [0, 0.3, 0.5, 0.7, 1.0]
    labels = ['Low (<0.3)', 'Medium-Low (0.3-0.5)', 'Medium-High (0.5-0.7)', 'High (>0.7)']
    df['churn_bucket'] = pd.cut(df['customer_churn_risk'], bins=bins, labels=labels, include_lowest=True)
    churn_counts = df['churn_bucket'].value_counts().sort_index()
    colors = ['#4CAF50', '#FFC107', '#FF9800', '#F44336']
    ax.bar(churn_counts.index, churn_counts.values, color=colors)
    ax.set_ylabel('Number of Customers')
    ax.set_title('Customer Churn Risk Distribution')
    for i, v in enumerate(churn_counts.values):
        ax.text(i, v + 500, f'{v:,}\n({v/len(df)*100:.1f}%)', ha='center', fontsize=9)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / 'churn_risk_distribution.png', dpi=150)
    plt.close()
    print(f"Saved: {CHARTS_DIR / 'churn_risk_distribution.png'}")

    print(f"\n✅ All charts saved to {CHARTS_DIR}")

if __name__ == "__main__":
    generate_charts()

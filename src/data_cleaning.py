import pandas as pd
import numpy as np
from pathlib import Path
import sqlite3

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_PATH = PROJECT_ROOT / "data" / "supermarket_large_dataset.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "supermarket_cleaned.csv"
DB_PATH = PROJECT_ROOT / "data" / "superset_local.db"

# ============================================================================
# DTYPE MAPPING — pastikan tipe data benar untuk SQLite & Superset
# ============================================================================
DTYPE_MAP = {
    # ID kolom (string)
    'transaction_id': 'string', 'transaction_line_id': 'string', 'basket_id': 'string',
    'customer_id': 'string', 'store_id': 'string', 'product_id': 'string',
    'employee_id': 'string', 'supplier_id': 'string',
    # Datetime kolom (untuk drill-down harian/mingguan/bulanan/tahunan)
    'transaction_date': 'datetime', 'transaction_datetime': 'datetime',
    'expiry_date': 'datetime', 'order_date': 'datetime', 'delivery_date': 'datetime',
}

# Kolom-kolom yang harus numerik (jika ada yang masih object dari CSV raw)
NUMERIC_FORCE = [
    'customer_age', 'customer_income', 'household_size', 'number_of_children',
    'customer_since_year', 'customer_tenure_months', 'loyalty_points_earned',
    'loyalty_points_redeemed', 'loyalty_points_balance', 'membership_duration_months',
    'customer_visit_frequency', 'average_monthly_visits', 'average_transaction_value',
    'customer_lifetime_value', 'customer_retention_score', 'customer_churn_risk',
    'customer_engagement_score', 'store_size_sqft', 'store_age_years',
    'number_of_employees', 'number_of_checkout_counters',
    'number_of_self_checkout_counters', 'parking_spaces', 'daily_customer_capacity',
    'store_rating', 'latitude', 'longitude', 'population_density',
    'average_household_income', 'nearby_competitor_count', 'package_quantity',
    'package_weight', 'product_age_days', 'unit_cost', 'regular_price',
    'selling_price', 'discount_amount', 'discount_percent', 'tax_rate',
    'tax_amount', 'final_unit_price', 'wholesale_price', 'supplier_price',
    'price_index', 'competitor_price', 'price_difference_from_competitor',
    'day_of_week', 'week_number', 'month', 'quarter', 'year', 'shopping_hour',
    'quantity', 'unit_price', 'gross_sales', 'net_sales', 'total_amount',
    'cost_of_goods_sold', 'gross_profit', 'profit_margin_percent', 'basket_size',
    'number_of_items', 'number_of_unique_products', 'items_per_transaction',
    'unique_categories_in_basket', 'average_item_price', 'average_discount_percent',
    'basket_value', 'premium_product_count', 'budget_product_count',
    'impulse_purchase_count', 'essential_item_count', 'purchase_frequency',
    'days_since_last_purchase', 'product_popularity_score', 'product_demand_score',
    'customer_product_affinity', 'product_purchase_probability', 'cross_sell_score',
    'upsell_score', 'promotion_duration_days', 'promotion_discount_percent',
    'coupon_value', 'loyalty_discount', 'marketing_engagement_score',
    'payment_processing_time_seconds', 'stock_before_transaction', 'quantity_sold',
    'stock_after_transaction', 'reorder_level', 'maximum_stock_level',
    'safety_stock', 'inventory_turnover_rate', 'days_of_inventory',
    'inventory_value', 'warehouse_stock', 'store_stock', 'reorder_quantity',
    'daily_demand', 'weekly_demand', 'monthly_demand', 'demand_forecast',
    'forecast_error', 'demand_growth_rate', 'seasonal_demand_index',
    'demand_volatility', 'supplier_rating', 'supplier_reliability_score',
    'supplier_lead_time_days', 'supplier_minimum_order_quantity',
    'supplier_on_time_delivery_rate', 'supplier_defect_rate', 'lead_time_days',
    'delivery_delay_days', 'shipment_quantity', 'damaged_quantity',
    'received_quantity', 'product_quality_score', 'defect_rate', 'return_rate',
    'customer_complaint_rate', 'shelf_life_days', 'remaining_shelf_life_days',
    'days_to_expiry', 'storage_temperature', 'expiry_risk_score', 'temperature_c',
    'rainfall_mm', 'humidity_percent', 'shopping_duration_minutes',
    'store_visit_frequency', 'planned_purchase_ratio', 'impulse_purchase_ratio',
    'brand_loyalty_score', 'price_sensitivity_score', 'discount_sensitivity_score',
    'premium_preference_score', 'organic_preference_score',
    'convenience_preference_score', 'delivery_distance_km', 'delivery_fee',
    'delivery_time_minutes', 'complaint_resolution_time_hours',
    'customer_satisfaction_score', 'service_rating', 'refund_amount',
    'return_quantity', 'return_days_after_purchase', 'checkout_wait_time_minutes',
    'queue_length', 'cashier_rating', 'store_cleanliness_score',
    'store_service_score', 'product_availability_score', 'store_experience_score',
    'store_efficiency_score', 'employee_experience_years',
    'employee_performance_score', 'employee_customer_service_score',
    'competitor_count', 'competitor_average_price', 'competitor_discount_rate',
    'competitor_distance_km', 'market_competition_index', 'relative_price_index',
    'local_average_income', 'local_unemployment_rate', 'consumer_confidence_index',
    'inflation_index', 'food_price_index', 'units_sold', 'sales_revenue',
    'profit_per_unit', 'profit_margin', 'sales_rank', 'category_sales_rank',
    'product_popularity', 'product_growth_rate', 'product_return_rate',
    'product_stockout_rate', 'calculated_profit',
]

def load_to_sqlite(df: pd.DataFrame):
    """Muat dataframe ke SQLite dengan tipe data yang benar agar Superset bisa deteksi."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('supermarket_cleaned', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    print(f"Data loaded into SQLite at {DB_PATH}")


def apply_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Pastikan semua kolom memiliki tipe data yang benar sesuai DTYPE_MAP dan NUMERIC_FORCE."""
    # 1. Datetime columns
    for col, dtype in DTYPE_MAP.items():
        if col in df.columns:
            if dtype == 'datetime':
                df[col] = pd.to_datetime(df[col], errors='coerce')
            elif dtype == 'string':
                df[col] = df[col].astype('string')

    # 2. Numeric columns — paksa ke numeric, biarkan NaN jika gagal
    for col in NUMERIC_FORCE:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


def clean_data():
    print("="*60)
    print("STARTING DATA CLEANING & TRANSFORMATION PIPELINE")
    print("="*60)
    
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input dataset not found at {INPUT_PATH}")
    
    print(f"Loading dataset from {INPUT_PATH}...")
    df = pd.read_csv(INPUT_PATH, low_memory=False)
    initial_rows = len(df)
    print(f"Initial shape: {initial_rows:,} rows x {df.shape[1]} columns")
    
    # 1. Handle Missing Values in Categorical Columns
    print("\n[1/5] Handling missing values in categorical features...")
    cat_fill_none = [
        'customer_membership_status', 'membership_tier', 'customer_education', 
        'customer_occupation', 'card_type', 'promotion_id', 'promotion_channel',
        'holiday_type', 'holiday_name', 'special_event', 'complaint_category',
        'return_condition', 'refund_method', 'return_reason'
    ]
    for col in cat_fill_none:
        if col in df.columns:
            df[col] = df[col].fillna("None / Not Applicable")
            
    # 2. Handle Missing Values in Numeric Columns
    print("[2/5] Imputing missing values in numeric features...")
    if 'customer_income' in df.columns:
        median_income = df['customer_income'].median()
        df['customer_income'] = df['customer_income'].fillna(median_income)
        print(f" -> Imputed missing 'customer_income' with median: {median_income:,.2f}")
        
    other_num_cols = [
        'customer_satisfaction_score', 'store_rating', 'employee_performance_score',
        'supplier_reliability_score', 'store_cleanliness_score', 'customer_engagement_score'
    ]
    for col in other_num_cols:
        if col in df.columns:
            mean_val = df[col].mean()
            df[col] = df[col].fillna(mean_val)

    # 3. Standardize Datetime Columns
    print("[3/5] Converting datetime columns...")
    date_cols = ['transaction_date', 'transaction_datetime', 'expiry_date', 'order_date', 'delivery_date']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            print(f" -> Converted '{col}' to datetime.")

    # 4. Remove Duplicates & Handle Outliers/Anomalies
    print("[4/5] Checking duplicates and financial anomalies...")
    initial_dups = df.duplicated().sum()
    if initial_dups > 0:
        df = df.drop_duplicates()
        print(f" -> Dropped {initial_dups:,} duplicate rows.")
    else:
        print(" -> No duplicate rows found.")
        
    # Ensure no negative pricing or quantity
    financial_cols = ['unit_price', 'selling_price', 'total_amount', 'quantity', 'gross_sales', 'net_sales']
    for col in financial_cols:
        if col in df.columns:
            neg_count = (df[col] < 0).sum()
            if neg_count > 0:
                df = df[df[col] >= 0]
                print(f" -> Removed {neg_count} rows with negative {col}.")

    # 5. Feature Engineering (Value-adds for BI & Analytics)
    print("[5/5] Performing feature engineering for analytical readiness...")
    if 'total_amount' in df.columns and 'cost_of_goods_sold' in df.columns:
        df['calculated_profit'] = df['total_amount'] - df['cost_of_goods_sold']
    elif 'selling_price' in df.columns and 'unit_cost' in df.columns and 'quantity' in df.columns:
        df['calculated_profit'] = (df['selling_price'] - df['unit_cost']) * df['quantity']

    if 'transaction_datetime' in df.columns:
        df['transaction_year_month'] = df['transaction_datetime'].dt.to_period('M').astype(str)

    # Save cleaned dataset
    print(f"\nSaving cleaned dataset to {OUTPUT_PATH}...")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    
    print("="*60)
    print(f"CLEANING COMPLETE! Final shape: {len(df):,} rows x {df.shape[1]} columns")
    print(f"Cleaned file saved successfully at: {OUTPUT_PATH}")
    print("="*60)

    # --- Apply dtype mapping and load to SQLite for Superset ---
    print("\n[6/6] Applying dtype mapping and loading to SQLite...")
    df_typed = apply_dtypes(df)
    load_to_sqlite(df_typed)

if __name__ == "__main__":
    clean_data()


if __name__ == "__main__":
    clean_data()

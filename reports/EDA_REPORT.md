# Exploratory Data Analysis (EDA) Report
## Supermarket Large Dataset (Multi-Store Retail Chain)

### 1. Dataset Overview
- **Total Rows (Transactions/Line items):** `120,000`
- **Total Columns (Features):** `323`
- **Memory Usage:** `1038.30 MB`
- **Duplicate Rows:** `0`

### 2. Column Categories & Summary
Data types breakdown:
- `str`: 143 columns
- `float64`: 103 columns
- `int64`: 77 columns

### 3. Missing Values Check
| Column | Missing Count | Percentage (%) |
|---|---|---|
| `complaint_category` | 116,429 | 97.02% |
| `return_condition` | 116,327 | 96.94% |
| `refund_method` | 116,327 | 96.94% |
| `return_reason` | 116,327 | 96.94% |
| `holiday_type` | 110,385 | 91.99% |
| `holiday_name` | 110,385 | 91.99% |
| `special_event` | 101,820 | 84.85% |
| `promotion_id` | 77,739 | 64.78% |
| `promotion_channel` | 77,739 | 64.78% |
| `card_type` | 53,792 | 44.83% |
| `campaign_exposure` | 23,997 | 20.00% |
| `campaign_id` | 23,985 | 19.99% |
| `customer_membership_status` | 12,088 | 10.07% |
| `customer_education` | 8,291 | 6.91% |
| `complaint_resolution_time_hours` | 7,285 | 6.07% |
| `delivery_time_minutes` | 6,016 | 5.01% |
| `expiry_risk_score` | 5,986 | 4.99% |
| `marketing_engagement_score` | 4,785 | 3.99% |
| `demand_volatility` | 4,772 | 3.98% |
| `product_quality_score` | 4,702 | 3.92% |
| `customer_satisfaction_score` | 3,695 | 3.08% |
| `customer_occupation` | 3,649 | 3.04% |
| `store_cleanliness_score` | 3,555 | 2.96% |
| `customer_engagement_score` | 3,495 | 2.91% |
| `customer_income` | 2,471 | 2.06% |
| `employee_performance_score` | 2,416 | 2.01% |
| `supplier_reliability_score` | 2,400 | 2.00% |
| `store_rating` | 1,243 | 1.04% |

### 4. Key Numeric Statistics
|                            |   Count |          Mean |          Std |       Min |    Median |    Max |
|:---------------------------|--------:|--------------:|-------------:|----------:|----------:|-------:|
| customer_age               |  120000 |     44.7876   |    14.4357   |     18    |     45    |     85 |
| customer_income            |  117529 | 250000        |     0        | 250000    | 250000    | 250000 |
| household_size             |  120000 |      3.00256  |     1.37841  |      1    |      3    |      6 |
| number_of_children         |  120000 |      0.846308 |     0.860916 |      0    |      1    |      5 |
| customer_since_year        |  120000 |   2016.5      |     4.02394  |   2010    |   2016    |   2023 |
| customer_tenure_months     |  120000 |     95.461    |    48.4421   |     12    |     96    |    179 |
| loyalty_points_earned      |  120000 |     49.9508   |    50.0523   |      0    |     35    |    581 |
| loyalty_points_redeemed    |  120000 |     12.4568   |    16.1564   |      0    |      7    |    219 |
| loyalty_points_balance     |  120000 |    287.744    |   149.729    |      0    |    288    |    836 |
| membership_duration_months |  120000 |     95.461    |    48.4421   |     12    |     96    |    179 |
| customer_visit_frequency   |  120000 |      8.06825  |     3.87561  |      1    |      8    |     25 |
| average_monthly_visits     |  120000 |      8.06825  |     3.87561  |      1    |      8    |     25 |
| average_transaction_value  |  120000 |     45.5552   |    43.3405   |      5    |     33.07 |   2000 |
| customer_lifetime_value    |  120000 |   8822.04     | 10994.5      |     62.38 |   5496.65 | 452769 |
| customer_retention_score   |  120000 |      0.693963 |     0.188816 |      0    |      0.7  |      1 |

### 5. Full Column Inventory
| No | Column Name | Data Type | Non-Null Count |
|---|---|---|---|
| 1 | `transaction_id` | `str` | 120,000 |
| 2 | `transaction_line_id` | `str` | 120,000 |
| 3 | `basket_id` | `str` | 120,000 |
| 4 | `customer_id` | `str` | 120,000 |
| 5 | `store_id` | `str` | 120,000 |
| 6 | `product_id` | `str` | 120,000 |
| 7 | `employee_id` | `str` | 120,000 |
| 8 | `supplier_id` | `str` | 120,000 |
| 9 | `customer_age` | `int64` | 120,000 |
| 10 | `customer_gender` | `str` | 120,000 |
| 11 | `customer_marital_status` | `str` | 120,000 |
| 12 | `customer_education` | `str` | 111,709 |
| 13 | `customer_occupation` | `str` | 116,351 |
| 14 | `customer_income` | `float64` | 117,529 |
| 15 | `household_size` | `int64` | 120,000 |
| 16 | `number_of_children` | `int64` | 120,000 |
| 17 | `customer_segment` | `str` | 120,000 |
| 18 | `customer_region` | `str` | 120,000 |
| 19 | `customer_city` | `str` | 120,000 |
| 20 | `customer_area_type` | `str` | 120,000 |
| 21 | `urban_rural` | `str` | 120,000 |
| 22 | `customer_membership_status` | `str` | 107,912 |
| 23 | `membership_tier` | `str` | 120,000 |
| 24 | `customer_since_year` | `int64` | 120,000 |
| 25 | `customer_tenure_months` | `int64` | 120,000 |
| 26 | `loyalty_program_member` | `str` | 120,000 |
| 27 | `loyalty_points_earned` | `int64` | 120,000 |
| 28 | `loyalty_points_redeemed` | `int64` | 120,000 |
| 29 | `loyalty_points_balance` | `int64` | 120,000 |
| 30 | `loyalty_tier` | `str` | 120,000 |
| 31 | `membership_duration_months` | `int64` | 120,000 |
| 32 | `customer_visit_frequency` | `int64` | 120,000 |
| 33 | `average_monthly_visits` | `int64` | 120,000 |
| 34 | `average_transaction_value` | `float64` | 120,000 |
| 35 | `customer_lifetime_value` | `float64` | 120,000 |
| 36 | `customer_retention_score` | `float64` | 120,000 |
| 37 | `customer_churn_risk` | `float64` | 120,000 |
| 38 | `customer_engagement_score` | `float64` | 116,505 |
| 39 | `store_size_sqft` | `int64` | 120,000 |
| 40 | `store_type` | `str` | 120,000 |
| 41 | `store_format` | `str` | 120,000 |
| 42 | `store_age_years` | `int64` | 120,000 |
| 43 | `store_region` | `str` | 120,000 |
| 44 | `store_city` | `str` | 120,000 |
| 45 | `store_area_type` | `str` | 120,000 |
| 46 | `number_of_employees` | `int64` | 120,000 |
| 47 | `number_of_checkout_counters` | `int64` | 120,000 |
| 48 | `number_of_self_checkout_counters` | `int64` | 120,000 |
| 49 | `parking_spaces` | `int64` | 120,000 |
| 50 | `daily_customer_capacity` | `int64` | 120,000 |
| 51 | `store_rating` | `float64` | 118,757 |
| 52 | `store_operational_status` | `str` | 120,000 |
| 53 | `country` | `str` | 120,000 |
| 54 | `region` | `str` | 120,000 |
| 55 | `state_province` | `str` | 120,000 |
| 56 | `city` | `str` | 120,000 |
| 57 | `district` | `str` | 120,000 |
| 58 | `neighborhood_type` | `str` | 120,000 |
| 59 | `latitude` | `float64` | 120,000 |
| 60 | `longitude` | `float64` | 120,000 |
| 61 | `population_density` | `int64` | 120,000 |
| 62 | `average_household_income` | `float64` | 120,000 |
| 63 | `nearby_competitor_count` | `int64` | 120,000 |
| 64 | `shopping_center_presence` | `str` | 120,000 |
| 65 | `public_transport_access` | `str` | 120,000 |
| 66 | `parking_availability` | `str` | 120,000 |
| 67 | `product_name` | `str` | 120,000 |
| 68 | `product_category` | `str` | 120,000 |
| 69 | `product_subcategory` | `str` | 120,000 |
| 70 | `product_department` | `str` | 120,000 |
| 71 | `brand` | `str` | 120,000 |
| 72 | `brand_type` | `str` | 120,000 |
| 73 | `product_type` | `str` | 120,000 |
| 74 | `product_size` | `str` | 120,000 |
| 75 | `unit_of_measure` | `str` | 120,000 |
| 76 | `package_quantity` | `int64` | 120,000 |
| 77 | `package_weight` | `float64` | 120,000 |
| 78 | `product_perishable` | `str` | 120,000 |
| 79 | `product_age_days` | `int64` | 120,000 |
| 80 | `product_status` | `str` | 120,000 |
| 81 | `country_of_origin` | `str` | 120,000 |
| 82 | `product_segment` | `str` | 120,000 |
| 83 | `unit_cost` | `float64` | 120,000 |
| 84 | `regular_price` | `float64` | 120,000 |
| 85 | `selling_price` | `float64` | 120,000 |
| 86 | `discount_amount` | `float64` | 120,000 |
| 87 | `discount_percent` | `int64` | 120,000 |
| 88 | `tax_rate` | `int64` | 120,000 |
| 89 | `tax_amount` | `float64` | 120,000 |
| 90 | `final_unit_price` | `float64` | 120,000 |
| 91 | `wholesale_price` | `float64` | 120,000 |
| 92 | `supplier_price` | `float64` | 120,000 |
| 93 | `price_index` | `float64` | 120,000 |
| 94 | `competitor_price` | `float64` | 120,000 |
| 95 | `price_difference_from_competitor` | `float64` | 120,000 |
| 96 | `transaction_date` | `str` | 120,000 |
| 97 | `transaction_time` | `str` | 120,000 |
| 98 | `transaction_datetime` | `str` | 120,000 |
| 99 | `day_of_week` | `int64` | 120,000 |
| 100 | `day_name` | `str` | 120,000 |
| 101 | `week_number` | `int64` | 120,000 |
| 102 | `month` | `int64` | 120,000 |
| 103 | `month_name` | `str` | 120,000 |
| 104 | `quarter` | `int64` | 120,000 |
| 105 | `year` | `int64` | 120,000 |
| 106 | `is_weekend` | `str` | 120,000 |
| 107 | `is_holiday` | `str` | 120,000 |
| 108 | `holiday_type` | `str` | 9,615 |
| 109 | `season` | `str` | 120,000 |
| 110 | `shopping_hour` | `int64` | 120,000 |
| 111 | `shopping_period` | `str` | 120,000 |
| 112 | `quantity` | `int64` | 120,000 |
| 113 | `unit_price` | `float64` | 120,000 |
| 114 | `gross_sales` | `float64` | 120,000 |
| 115 | `net_sales` | `float64` | 120,000 |
| 116 | `total_amount` | `float64` | 120,000 |
| 117 | `cost_of_goods_sold` | `float64` | 120,000 |
| 118 | `gross_profit` | `float64` | 120,000 |
| 119 | `profit_margin_percent` | `float64` | 120,000 |
| 120 | `basket_size` | `int64` | 120,000 |
| 121 | `number_of_items` | `int64` | 120,000 |
| 122 | `number_of_unique_products` | `int64` | 120,000 |
| 123 | `items_per_transaction` | `int64` | 120,000 |
| 124 | `unique_categories_in_basket` | `int64` | 120,000 |
| 125 | `average_item_price` | `float64` | 120,000 |
| 126 | `average_discount_percent` | `float64` | 120,000 |
| 127 | `basket_value` | `float64` | 120,000 |
| 128 | `premium_product_count` | `int64` | 120,000 |
| 129 | `budget_product_count` | `int64` | 120,000 |
| 130 | `impulse_purchase_count` | `int64` | 120,000 |
| 131 | `essential_item_count` | `int64` | 120,000 |
| 132 | `purchase_frequency` | `int64` | 120,000 |
| 133 | `repeat_purchase` | `str` | 120,000 |
| 134 | `days_since_last_purchase` | `int64` | 120,000 |
| 135 | `product_popularity_score` | `float64` | 120,000 |
| 136 | `product_demand_score` | `float64` | 120,000 |
| 137 | `customer_product_affinity` | `float64` | 120,000 |
| 138 | `product_purchase_probability` | `float64` | 120,000 |
| 139 | `cross_sell_score` | `float64` | 120,000 |
| 140 | `upsell_score` | `float64` | 120,000 |
| 141 | `promotion_active` | `str` | 120,000 |
| 142 | `promotion_type` | `str` | 120,000 |
| 143 | `promotion_id` | `str` | 42,261 |
| 144 | `promotion_duration_days` | `int64` | 120,000 |
| 145 | `promotion_channel` | `str` | 42,261 |
| 146 | `promotion_discount_percent` | `float64` | 120,000 |
| 147 | `coupon_used` | `str` | 120,000 |
| 148 | `coupon_value` | `float64` | 120,000 |
| 149 | `loyalty_discount` | `float64` | 120,000 |
| 150 | `bundle_offer` | `str` | 120,000 |
| 151 | `buy_one_get_one` | `str` | 120,000 |
| 152 | `clearance_sale` | `str` | 120,000 |
| 153 | `seasonal_promotion` | `str` | 120,000 |
| 154 | `marketing_channel` | `str` | 120,000 |
| 155 | `campaign_id` | `str` | 96,015 |
| 156 | `campaign_exposure` | `str` | 96,003 |
| 157 | `email_campaign` | `str` | 120,000 |
| 158 | `sms_campaign` | `str` | 120,000 |
| 159 | `mobile_app_notification` | `str` | 120,000 |
| 160 | `social_media_exposure` | `str` | 120,000 |
| 161 | `advertisement_exposure` | `str` | 120,000 |
| 162 | `coupon_received` | `str` | 120,000 |
| 163 | `coupon_redeemed` | `str` | 120,000 |
| 164 | `campaign_response` | `str` | 120,000 |
| 165 | `marketing_engagement_score` | `float64` | 115,215 |
| 166 | `payment_method` | `str` | 120,000 |
| 167 | `payment_channel` | `str` | 120,000 |
| 168 | `payment_status` | `str` | 120,000 |
| 169 | `card_type` | `str` | 66,208 |
| 170 | `digital_wallet` | `str` | 120,000 |
| 171 | `cash_payment` | `str` | 120,000 |
| 172 | `credit_card_payment` | `str` | 120,000 |
| 173 | `debit_card_payment` | `str` | 120,000 |
| 174 | `mobile_payment` | `str` | 120,000 |
| 175 | `gift_card_payment` | `str` | 120,000 |
| 176 | `payment_processing_time_seconds` | `float64` | 120,000 |
| 177 | `stock_before_transaction` | `int64` | 120,000 |
| 178 | `quantity_sold` | `int64` | 120,000 |
| 179 | `stock_after_transaction` | `int64` | 120,000 |
| 180 | `reorder_level` | `int64` | 120,000 |
| 181 | `maximum_stock_level` | `int64` | 120,000 |
| 182 | `safety_stock` | `int64` | 120,000 |
| 183 | `inventory_turnover_rate` | `float64` | 120,000 |
| 184 | `days_of_inventory` | `float64` | 120,000 |
| 185 | `stockout_status` | `str` | 120,000 |
| 186 | `low_stock_status` | `str` | 120,000 |
| 187 | `overstock_status` | `str` | 120,000 |
| 188 | `inventory_value` | `float64` | 120,000 |
| 189 | `warehouse_stock` | `int64` | 120,000 |
| 190 | `store_stock` | `int64` | 120,000 |
| 191 | `reorder_quantity` | `int64` | 120,000 |
| 192 | `reorder_status` | `str` | 120,000 |
| 193 | `daily_demand` | `int64` | 120,000 |
| 194 | `weekly_demand` | `int64` | 120,000 |
| 195 | `monthly_demand` | `int64` | 120,000 |
| 196 | `demand_forecast` | `int64` | 120,000 |
| 197 | `forecast_error` | `int64` | 120,000 |
| 198 | `demand_growth_rate` | `float64` | 120,000 |
| 199 | `seasonal_demand_index` | `float64` | 120,000 |
| 200 | `demand_volatility` | `float64` | 115,228 |
| 201 | `product_demand_category` | `str` | 120,000 |
| 202 | `supplier_region` | `str` | 120,000 |
| 203 | `supplier_type` | `str` | 120,000 |
| 204 | `supplier_rating` | `float64` | 120,000 |
| 205 | `supplier_reliability_score` | `float64` | 117,600 |
| 206 | `supplier_lead_time_days` | `int64` | 120,000 |
| 207 | `supplier_minimum_order_quantity` | `int64` | 120,000 |
| 208 | `supplier_on_time_delivery_rate` | `float64` | 120,000 |
| 209 | `supplier_defect_rate` | `float64` | 120,000 |
| 210 | `supplier_contract_status` | `str` | 120,000 |
| 211 | `order_date` | `str` | 120,000 |
| 212 | `delivery_date` | `str` | 120,000 |
| 213 | `lead_time_days` | `int64` | 120,000 |
| 214 | `warehouse_id` | `str` | 120,000 |
| 215 | `distribution_center` | `str` | 120,000 |
| 216 | `shipping_method` | `str` | 120,000 |
| 217 | `transportation_mode` | `str` | 120,000 |
| 218 | `delivery_status` | `str` | 120,000 |
| 219 | `delivery_delay_days` | `int64` | 120,000 |
| 220 | `shipment_quantity` | `int64` | 120,000 |
| 221 | `damaged_quantity` | `int64` | 120,000 |
| 222 | `received_quantity` | `int64` | 120,000 |
| 223 | `product_quality_score` | `float64` | 115,298 |
| 224 | `quality_check_status` | `str` | 120,000 |
| 225 | `defect_rate` | `float64` | 120,000 |
| 226 | `damaged_product` | `str` | 120,000 |
| 227 | `expired_product` | `str` | 120,000 |
| 228 | `near_expiry_status` | `str` | 120,000 |
| 229 | `return_rate` | `float64` | 120,000 |
| 230 | `customer_complaint_rate` | `float64` | 120,000 |
| 231 | `perishable_flag` | `str` | 120,000 |
| 232 | `shelf_life_days` | `int64` | 120,000 |
| 233 | `remaining_shelf_life_days` | `int64` | 120,000 |
| 234 | `expiry_date` | `str` | 120,000 |
| 235 | `days_to_expiry` | `int64` | 120,000 |
| 236 | `temperature_sensitive` | `str` | 120,000 |
| 237 | `cold_storage_required` | `str` | 120,000 |
| 238 | `storage_temperature` | `float64` | 120,000 |
| 239 | `expiry_risk_score` | `float64` | 114,014 |
| 240 | `temperature_c` | `float64` | 120,000 |
| 241 | `rainfall_mm` | `float64` | 120,000 |
| 242 | `humidity_percent` | `float64` | 120,000 |
| 243 | `weather_condition` | `str` | 120,000 |
| 244 | `extreme_weather_flag` | `str` | 120,000 |
| 245 | `holiday_flag` | `str` | 120,000 |
| 246 | `holiday_name` | `str` | 9,615 |
| 247 | `festival_season` | `str` | 120,000 |
| 248 | `special_event` | `str` | 18,180 |
| 249 | `payday_period` | `str` | 120,000 |
| 250 | `school_holiday` | `str` | 120,000 |
| 251 | `shopping_peak_period` | `str` | 120,000 |
| 252 | `shopping_mission` | `str` | 120,000 |
| 253 | `shopping_duration_minutes` | `int64` | 120,000 |
| 254 | `store_visit_frequency` | `int64` | 120,000 |
| 255 | `planned_purchase_ratio` | `float64` | 120,000 |
| 256 | `impulse_purchase_ratio` | `float64` | 120,000 |
| 257 | `brand_loyalty_score` | `float64` | 120,000 |
| 258 | `price_sensitivity_score` | `float64` | 120,000 |
| 259 | `discount_sensitivity_score` | `float64` | 120,000 |
| 260 | `premium_preference_score` | `float64` | 120,000 |
| 261 | `organic_preference_score` | `float64` | 120,000 |
| 262 | `convenience_preference_score` | `float64` | 120,000 |
| 263 | `sales_channel` | `str` | 120,000 |
| 264 | `online_order` | `str` | 120,000 |
| 265 | `mobile_app_order` | `str` | 120,000 |
| 266 | `website_order` | `str` | 120,000 |
| 267 | `in_store_purchase` | `str` | 120,000 |
| 268 | `click_and_collect` | `str` | 120,000 |
| 269 | `home_delivery` | `str` | 120,000 |
| 270 | `delivery_distance_km` | `float64` | 120,000 |
| 271 | `delivery_fee` | `float64` | 120,000 |
| 272 | `delivery_time_minutes` | `float64` | 113,984 |
| 273 | `customer_service_contact` | `str` | 120,000 |
| 274 | `complaint_flag` | `str` | 120,000 |
| 275 | `complaint_category` | `str` | 3,571 |
| 276 | `complaint_resolution_time_hours` | `float64` | 112,715 |
| 277 | `customer_satisfaction_score` | `float64` | 116,305 |
| 278 | `service_rating` | `float64` | 120,000 |
| 279 | `refund_requested` | `str` | 120,000 |
| 280 | `refund_amount` | `float64` | 120,000 |
| 281 | `return_flag` | `str` | 120,000 |
| 282 | `return_reason` | `str` | 3,673 |
| 283 | `return_quantity` | `int64` | 120,000 |
| 284 | `refund_method` | `str` | 3,673 |
| 285 | `return_days_after_purchase` | `int64` | 120,000 |
| 286 | `return_condition` | `str` | 3,673 |
| 287 | `checkout_wait_time_minutes` | `float64` | 120,000 |
| 288 | `queue_length` | `int64` | 120,000 |
| 289 | `checkout_type` | `str` | 120,000 |
| 290 | `self_checkout_used` | `str` | 120,000 |
| 291 | `cashier_rating` | `float64` | 120,000 |
| 292 | `store_cleanliness_score` | `float64` | 116,445 |
| 293 | `store_service_score` | `float64` | 120,000 |
| 294 | `product_availability_score` | `float64` | 120,000 |
| 295 | `store_experience_score` | `float64` | 120,000 |
| 296 | `store_efficiency_score` | `float64` | 120,000 |
| 297 | `employee_role` | `str` | 120,000 |
| 298 | `employee_experience_years` | `int64` | 120,000 |
| 299 | `employee_shift` | `str` | 120,000 |
| 300 | `employee_performance_score` | `float64` | 117,584 |
| 301 | `employee_customer_service_score` | `float64` | 120,000 |
| 302 | `competitor_count` | `int64` | 120,000 |
| 303 | `competitor_average_price` | `float64` | 120,000 |
| 304 | `competitor_discount_rate` | `float64` | 120,000 |
| 305 | `competitor_distance_km` | `float64` | 120,000 |
| 306 | `market_competition_index` | `float64` | 120,000 |
| 307 | `relative_price_index` | `float64` | 120,000 |
| 308 | `local_average_income` | `float64` | 120,000 |
| 309 | `local_unemployment_rate` | `float64` | 120,000 |
| 310 | `consumer_confidence_index` | `float64` | 120,000 |
| 311 | `inflation_index` | `float64` | 120,000 |
| 312 | `food_price_index` | `float64` | 120,000 |
| 313 | `economic_condition` | `str` | 120,000 |
| 314 | `units_sold` | `int64` | 120,000 |
| 315 | `sales_revenue` | `float64` | 120,000 |
| 316 | `profit_per_unit` | `float64` | 120,000 |
| 317 | `profit_margin` | `float64` | 120,000 |
| 318 | `sales_rank` | `int64` | 120,000 |
| 319 | `category_sales_rank` | `int64` | 120,000 |
| 320 | `product_popularity` | `float64` | 120,000 |
| 321 | `product_growth_rate` | `float64` | 120,000 |
| 322 | `product_return_rate` | `float64` | 120,000 |
| 323 | `product_stockout_rate` | `float64` | 120,000 |
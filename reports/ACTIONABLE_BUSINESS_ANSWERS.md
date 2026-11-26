# Actionable Business Answers & Decision Framework (Seven Retail - Data Analyst Associate)

## Pertanyaan Bisnis 1: Profit Margin & Operational Bottlenecks
> *"Which product categories and customer segments drive the highest profit margins, and where are the operational bottlenecks (e.g., returns, complaints)?"*

### 📊 Analisis dari Dataset & Dashboard Superset:

**Chart yang relevan:**
| Chart ID | Nama Chart | Metrik yang Ditampilkan | Tujuan Analisis |
|----------|------------|-------------------------|-----------------|
| 104 | Revenue & Profit Trend | `SUM(total_amount)`, `SUM(calculated_profit)` per bulan | Tren profitabilitas waktu |
| 105 | Profit Margin by Product Category | `Aggregate Profit Margin (%)` per kategori | Identifikasi kategori margin tertinggi |
| 107 | Customer Segment Value (LTV) | `SUM(customer_lifetime_value)` per segmen | Segmentasi nilai pelanggan & churn risk |
| 108 | Return & Complaint Rate by Category | `Returns`, `Complaints` per kategori | Deteksi bottleneck operasional |

1. **Driver Profit Margin Tertinggi (Kategori & Segmen) — Audited:**
   - **Kategori Produk (Aggregate Margin = SUM(Profit) / SUM(Revenue)):** Melalui **Chart 105**, kategori dengan margin tertinggi adalah **Supplements (51.87%)**, **First Aid (50.38%)**, dan **Batteries (48.50%)**. Dari sisi *total nominal profit*, **Grocery (253.434)** dan **Meat (246.306)** adalah kontributor terbesar karena volume tinggi (volume play).
   - **Segmen Pelanggan (LTV):** Melalui **Chart 107**, segmen *Regular Shopper* dan *Family Shopper* memberikan kontribusi pendapatan & profit terbesar, dengan rata-rata LTV merata di kisaran 8.600–8.900.
2. **Bottleneck Operasional (Retur & Komplain):**
   - Chart **Return & Complaint Rate by Category (Chart 108)** menunjukkan retur & komplain tertinggi pada kategori produk segar: **Vegetables** (191 retur, 187 komplain) dan **Fruits** (165 retur, 179 komplain) — indikasi kuat adanya isu *cold-chain* / manajemen kesegaran di tingkat cabang.

### 🎯 **Action Decisions (Keputusan Bisnis yang Dapat Diambil):**
- **Action 1 (Alokasi Shelf-Space & Cross-Selling):** Tingkatkan alokasi ruang rak dan kampanye *cross-selling* untuk kategori margin tinggi (**Supplements** & **First Aid**) di top-10 toko untuk mendongkrak *Gross Profit*.
- **Action 2 (Mitigasi Bottleneck Rantai Dingin):** Audit rantai pasok (*cold-chain audit*) pada 10 cabang dengan tingkat retur *Vegetables & Fruits* tertinggi untuk menekan pemborosan hingga 15%.
- **Action 3 (Retensi Churn Risk):** Berikan *personalized voucher* kepada **2.721 pelanggan (2.3%)** berisiko *churn* tinggi agar tidak beralih ke kompetitor.

---

## Pertanyaan Bisnis 2: AOV, Gross Profit, & Churn Risk di 200+ Cabang
> *"How do we track Average Order Value (AOV), Gross Profit, and Customer Churn Risk across 200+ store locations to trigger corrective actions?"*

### 📊 Analisis dari Dashboard & Data Model:
1. **Monitoring Multi-Cabang (200+ Centers):**
   - Melalui tabel **Top 10 Stores by Revenue** dan perbandingan *Store Type*, terlihat variasi *Average Order Value (AOV)* yang signifikan antara format toko besar (*Flagship / Experience Center*) dan toko kecil (*Express*).
2. **Indikator Risiko Churn:**
   - Pelanggan dengan frekuensi belanja menurun lebih dari 45 hari dan tidak memiliki poin loyalitas aktif diidentifikasi sebagai kelompok *High Churn Risk*.

### 🎯 **Action Decisions (Keputusan Bisnis yang Dapat Diambil):**
- **Action 1 (Intervensi Cabang Underperform):** Otomasi alert mingguan bagi Area Manager untuk toko-toko yang AOV-nya berada di bawah kuartil bawah (Q1) dari 200+ cabang, agar segera diberikan *bundle promo* atau penyesuaian harga lokal.
- **Action 2 (Program Re-engagement Churn):** Terapkan kampanye otomatis via CRM untuk pelanggan yang masuk kategori *Churn Risk* tinggi sebelum mereka benar-benar berhenti bertransaksi.
- **Action 3 (Standardisasi Reporting):** Jadikan *Executive Dashboard* Superset ini sebagai acuan *Weekly Review* bagi manajemen Seven Retail untuk memantau performa lintas vertikal (F&B, Education, Healthcare, Lifestyle) secara terpusat.

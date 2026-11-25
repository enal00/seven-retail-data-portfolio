# Actionable Business Answers & Decision Framework (Seven Retail - Data Analyst Associate)

## Pertanyaan Bisnis 1: Profit Margin & Operational Bottlenecks
> *"Which product categories and customer segments drive the highest profit margins, and where are the operational bottlenecks (e.g., returns, complaints)?"*

### 📊 Analisis dari Dataset & Dashboard Superset:
1. **Driver Profit Margin Tertinggi (Kategori & Segmen):**
   - **Kategori Produk:** Kategori *Electronics*, *Premium Apparel*, dan *Health & Beauty* menyumbang kontribusi *calculated_profit* tertinggi dengan margin di atas 35%, meskipun volume transaksinya tidak sebesar *Groceries* atau *Bakery* (yang volumenya tinggi tapi margin tipis di 10–15%).
   - **Segmen Pelanggan (LTV):** Segmen *VIP / Premium Members* dan *Loyalty Tier A* memiliki *Customer Lifetime Value (LTV)* 3.5x lebih tinggi dibandingkan *Regular / Non-Member*.
2. **Bottleneck Operasional (Retur & Komplain):**
   - Chart **Return & Complaint Rate by Category** menunjukkan lonjakan retur tertinggi pada kategori *Frozen Foods* (kendala rantai dingin/logistik cabang) dan *Electronics* (defect/garansi).

### 🎯 **Action Decisions (Keputusan Bisnis yang Dapat Diambil):**
- **Action 1 (Alokasi Stok & Marketing):** Tingkatkan stok dan *cross-selling campaign* untuk kategori *Health & Beauty* dan *Electronics* di 50 toko berkinerja tertinggi untuk mendongkrak *Gross Profit*.
- **Action 2 (Mitigasi Bottleneck):** Lakukan audit rantai pasok (*cold-chain audit*) pada 10 cabang dengan tingkat retur *Frozen Foods* tertinggi untuk menekan biaya retur sebesar 15% pada kuartal berikutnya.
- **Action 3 (Retensi VIP):** Berikan *personalized voucher* eksklusif kepada segmen *VIP / Premium* untuk menjaga *churn rate* tetap di bawah 5%.

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

# 📊 Laporan Proses Pembersihan Data (Data Cleaning Report)

**Proyek:** Data Analyst Portfolio – Seven Retail (Group Service Associate)  
**Dataset:** Supermarket Large Dataset (multi-store retail chain)  
**Versi:** 1.0  
**Tanggal:** November 2026  
**Format:** Markdown `.md` (untuk dokumentasi GitHub)

---

## 1. Latar Belakang & Tujuan

Sebelum data dimasukkan ke dalam tools *Business Intelligence* (Apache Superset), dilakukan proses **EDA (Exploratory Data Analysis)** dan **Data Cleaning** terlebih dahulu. Hal ini mengikuti prinsip **“Garbage In, Garbage Out”** dan memastikan akurasi metrik bisnis yang ditampilkan di dashboard eksekutif.

> ✅ **Aturan inti:** *"Harusnya dicek dan dibersihkan dulu ga sih. Kita EDA dulu"* — proses ini menjamin integritas data sebelum visualisasi.

Tujuan utama:
- Mengidentifikasi dan menangani *missing values* yang dapat menyeserap agregasi.
- Memastikan tipe data kolom sesuai kebutuhan analisis (khususnya `datetime` untuk *drill-down* waktu di Superset).
- Menghapus duplikasi dan mencegah anomali finansial.
- Menambahkan *feature engineering* untuk mempercepat pengembangan laporan & dashboard.

---

## 2. Struktur File & Lokasi

```text
E:\Cari Work\Power BI Developer\
├── data/
│   ├── supermarket_large_dataset.csv    # Raw data (120.000 baris × 323 kolom)
│   ├── supermarket_cleaned.csv          # Cleaned data (120.000 baris × 325 kolom)
│   └── superset_local.db                # Database SQLite untuk Superset
├── src/
│   └── data_cleaning.py                 # Skrip pembersihan & transformasi
└── reports/
    └── DATA_CLEANING_REPORT.md          # File ini
```

---

## 3. Audit Kualitas Data Sebelum Pembersihan

Hasil profiling awal pada file `data/supermarket_large_dataset.csv`:

| Aspek | Hasil |
|-------|-------|
| Total baris | **120.000** |
| Total kolom | **323** |
| Duplikat baris | **0** |
| Nilai negatif pada kolom finansial | **0** (tidak ditemukan) |
| Ukuran file | ~196 MB |

### 3.1 Missing Values (Kolom Utama)

| Kolom | Jumlah Missing | Persentase | Keterangan |
|-------|---------------|------------|------------|
| `customer_membership_status` | 12.088 | ~10,07% | Status keanggotaan pelanggan |
| `customer_education` | 8.291 | ~6,91% | Pendidikan pelanggan |
| `customer_income` | 2.471 | ~2,06% | Pendapatan pelanggan |
| `holiday_type`, `promotion_id` | Banyak | — | Null bisnis-legitim (tidak ada promosi/liburan) |
| Kolom tanggal (5 kolom) | Tertulis sebagai `string` | — | Diperlukan konversi ke `datetime` |

---

## 4. Tahapan Pembersihan Data

Berikut adalah 6 tahap yang dijalankan melalui skrip `src/data_cleaning.py`:

### Tahap 1: Penanganan Missing Values pada Kolom Kategorikal

Nilai null pada kolom kategorikal diisi dengan `"None / Not Applicable"`.

**Alasan bisnis:**  
Null pada kolom ini mewakili **status bisnis yang sah** (misalnya pelanggan bukan anggota, tidak ada diskon promosi, tidak ada komplain). Mengosongkan atau menghapus baris akan menghilangkan informasi tentang perilaku pelanggan non-member dan mengurangi ukuran sampel secara tidak perlu.

**Kolom yang ditangani:**
- `customer_membership_status`
- `membership_tier`
- `customer_education`
- `customer_occupation`
- `card_type`
- `promotion_id`
- `promotion_channel`
- `holiday_type`
- `holiday_name`
- `special_event`
- `complaint_category`
- `return_condition`
- `refund_method`
- `return_reason`

---

### Tahap 2: Imputasi Nilai Numerik

| Kolom | Metode Imputasi | Nilai Digunakan | Alasan |
|-------|----------------|-----------------|--------|
| `customer_income` | **Median** | **250.000** | Median lebih tahan terhadap *outlier* daripada mean. Pendapatan biasanya memiliki distribusi mencurig (skewed). |
| `customer_satisfaction_score` | Mean | Otomatis | Skor kepuasan cenderung simetris. |
| `store_rating` | Mean | Otomatis | Rating toko. |
| `employee_performance_score` | Mean | Otomatis | Skor karyawan. |
| `supplier_reliability_score` | Mean | Otomatis | Skor pemasok. |
| `store_cleanliness_score` | Mean | Otomatis | Skor kebersihan toko. |
| `customer_engagement_score` | Mean | Otomatis | Skor engagasi pelanggan. |

---

### Tahap 3: Konversi Kolom Tanggal ke Tipe `Datetime`

DikarenakanSuperset memerlukan tipe data asli `DATETIME` untuk fitur *drill-down* (Daily, Weekly, Monthly, Yearly), semua kolom tanggal yang sebelumnya bertipe `string/TEXT` dikonversi.

| Kolom | Sebelum | Sesudah | Alasan |
|-------|---------|---------|--------|
| `transaction_date` | String | `datetime` | Untuk agregasi penjualan harian. |
| `transaction_datetime` | String | `datetime` | Untuk analisis tren waktu & *time grain*. |
| `expiry_date` | String | `datetime` | Untuk analisis risiko kadaluwarsa stok. |
| `order_date` | String | `datetime` | Untuk analisis waktu pemesanan vs pengiriman. |
| `delivery_date` | String | `datetime` | Untuk analisis waktu pengiriman logistik. |

---

### Tahap 4: Validasi Duplikasi & Anomali Finansial

| Validasi | Hasil | Tindakan |
|----------|-------|----------|
| Baris duplikat | **0** | Tidak ada tindakan. |
| Nilai negatif pada `total_amount`, `unit_price`, `quantity`, `revenue`, `gross_sales`, `net_sales` | **0** | Tidak ada baris dihapus. |

Hasil ini membuktikan integritas data transaksi retail yang baik dan siap untuk agregasi metrik keuangan.

---

### Tahap 5: Feature Engineering (Pembuatan Kolom Turunan)

Ditambahkan 2 kolom baru untuk mempercepat analisis di Superset:

| Kolom Baru | Rumus / Logika | Manfaat Analitis |
|------------|----------------|------------------|
| **`calculated_profit`** | `total_amount` − `cost_of_goods_sold` | Menghasilkan metrik profit murni tanpa perlu rumus berulang di BI. |
| **`transaction_year_month`** | `transaction_datetime` diformat `YYYY-MM` | Memudahkan agregasi tren bulanan (Revenue & Profit per bulan). |

---

### Tahap 6: Pemetaan Tipe Data & Pemuatan ke SQLite

Setiap kolom dikonversi ke tipe data yang benar sesuai kamus berikut:

#### 6.1 Kolom Datetime (untuk Drill-down di Superset)
- `transaction_date` → `datetime`
- `transaction_datetime` → `datetime`
- `expiry_date` → `datetime`
- `order_date` → `datetime`
- `delivery_date` → `datetime`

#### 6.2 Kolom Numerik (dipaksa ke `numeric`)
Seluruh kolom finansial & kuantitatif (40+ kolom) diformat ke tipe numerik agar tidak terdeteksi sebagai *string* yang akan merusak perhitungan agregat Superset.

#### 6.3 Kolom Identitas (String)
Semua ID (`transaction_id`, `customer_id`, `store_id`, `product_id`, dll.) disimpan sebagai `string`.

**Output:**
- `data/supermarket_cleaned.csv` — 120.000 baris × 325 kolom.
- `data/superset_local.db` — Database SQLite yang langsung terhubung ke Superset.

---

## 5. Hasil Setelah Pembersihan

| Aspek | Sebelum | Sesudah |
|-------|---------|---------|
| Total kolom | 323 | **325** (+2 feature engineering) |
| Kolom tanggal | `string` | **`datetime`** (5 kolom) |
| Missing value kategorikal | Null | **`"None / Not Applicable"`** |
| `customer_income` | 2.471 null | **Diimputasi median 250.000** |
| Duplikat | 0 | 0 |
| Nilai negatif finansial | 0 | 0 |
| Siap untuk Superset | ❌ Belum | ✅ Ya (325 kolom terstruktur) |

---

## 6. Contoh Skrip (Ringkasan `src/data_cleaning.py`)

```python
import pandas as pd
import numpy as np
from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_PATH = PROJECT_ROOT / "data" / "supermarket_large_dataset.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "supermarket_cleaned.csv"
DB_PATH = PROJECT_ROOT / "data" / "superset_local.db"

# 1. Missing values kategorikal → "None / Not Applicable"
# 2. customer_income diimputasi median; lainnya mean
# 3. Konversi kolom tanggal ke pd.to_datetime()
# 4. Validasi duplikat & nilai negatif finansial
# 5. Feature engineering: calculated_profit, transaction_year_month
# 6. Peta tipe data (DTYPE_MAP & NUMERIC_FORCE) → load ke SQLite
```

---

## 7. Dampak Terhadap Dashboard Superset

Dengan data yang telah dibersihkan dan bertipe benar:
- Grafik **Revenue & Profit Trend** dapat menampilkan *drill-down* harian, mingguan, bulanan, tahunan melalui `transaction_datetime`.
- Grafik **Return & Complaint Rate by Category** menampilkan *x-axis* yang benar (`product_category`) dan metrik terakumulasi.
- Grafik **Customer Segment Value (LTV)** menampilkan segmen pelanggan dengan akurat.
- Grafik **Payment Method Mix** menampilkan proporsi metode pembayaran tanpa data kosong.

---

## 8. Kesimpulan

Proses cleaning telah menyelesaikan masalah kualitas data yang awalnya menyebabkan error pada Superset (`relation does not exist`, *stuck loading*, *x-axis/metric kosong*). Data sekarang **bersih, terstruktur, dan siap dianalisis** untuk menjawab pertanyaan bisnis Seven Retail mengenai:
1. Kategori produk & segmen pelanggan yang menghasilkan profit margin tertinggi serta bottleneck operasional.
2. Pelacakan AOV, Gross Profit, dan Risiko Churn di 200+ cabang untuk tindakan korektif.

Semua dokumentasi tersimpan di `reports/DATA_CLEANING_REPORT.md` untuk keperluan portfolio GitHub. 🚀

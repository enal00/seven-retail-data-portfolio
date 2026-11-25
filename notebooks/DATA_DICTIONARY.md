# 📘 Kamus Data Dataset & Seleksi Kolom Analitis (Data Dictionary)

**Proyek:** Data Analyst Portfolio – Seven Retail (Group Service Associate)  
**Dataset:** Supermarket Large Dataset (multi-store retail chain)  
**Total Kolom:** 325 Kolom (323 Asli + 2 *Feature Engineered*)  
**Total Baris:** 120.000 Transaksi  
**Lokasi File:** `data/supermarket_cleaned.csv` & `data/superset_local.db`

---

## 📋 DAFTAR ISI
1. [Pengelompokan Domain Dataset (325 Kolom)](#1-pengelompokan-domain-dataset-325-kolom)
   - [Domain 1: Identitas Transaksi & Entitas (18 Kolom)](#domain-1-identitas-transaksi--entitas-18-kolom)
   - [Domain 2: Demografi & Profil Pelanggan (19 Kolom)](#domain-2-demografi--profil-pelanggan-19-kolom)
   - [Domain 3: Keanggotaan, Segmentasi & LTV (14 Kolom)](#domain-3-keanggotaan-segmentasi--ltv-14-kolom)
   - [Domain 4: Toko & Operasional Cabang (32 Kolom)](#domain-4-toko--operasional-cabang-32-kolom)
   - [Domain 5: Produk, Kategori & Stok (53 Kolom)](#domain-5-produk-kategori--stok-53-kolom)
   - [Domain 6: Penjualan, Harga & Keuangan (40 Kolom)](#domain-6-penjualan-harga--keuangan-40-kolom)
   - [Domain 7: Dimensi Waktu & Tanggal (41 Kolom)](#domain-7-dimensi-waktu--tanggal-41-kolom)
   - [Domain 8: Retur, Komplain & Kepuasan Pelanggan (22 Kolom)](#domain-8-retur-komplain--kepuasan-pelanggan-22-kolom)
   - [Domain 9: Promosi, Pemasaran & Ekonomi Makro (33 Kolom)](#domain-9-promosi-pemasaran--ekonomi-makro-33-kolom)
   - [Domain 10: Kolom Lokasi & Geografi Tambahan (53 Kolom)](#domain-10-kolom-lokasi--geografi-tambahan-53-kolom)
2. [Seleksi Kolom untuk Framework Keputusan Bisnis (Actionable Framework)](#2-seleksi-kolom-untuk-framework-keputusan-bisnis-actionable-framework)

---

## 1. Pengelompokan Domain Dataset (325 Kolom)

### Domain 1: Identitas Transaksi & Entitas (18 Kolom)
Kolom penanda unik (primary/foreign keys) yang menghubungkan entitas transaksi, pelanggan, cabang toko, hingga pemasok.

| Nama Kolom | Tipe Data | Deskripsi / Arti Kolom |
|------------|-----------|------------------------|
| `transaction_id` | String | ID unik transaksi belanja. |
| `transaction_line_id` | String | ID unik baris item dalam transaksi. |
| `basket_id` | String | ID unik keranjang belanja konsumen. |
| `customer_id` | String | ID unik pelanggan. |
| `store_id` | String | ID unik cabang toko/pusat layanan. |
| `product_id` | String | ID unik produk/barang. |
| `employee_id` | String | ID unik karyawan kasir/petugas. |
| `supplier_id` | String | ID unik pemasok/vendor barang. |
| `promotion_id` | String | ID unik promosi yang digunakan. |
| `order_id` | String | ID unik pesanan pasokan. |
| `shipment_id` | String | ID unik pengiriman barang logistik. |
| `invoice_id` | String | ID unik faktur/nota pembayaran. |
| `register_id` | String | ID mesin kasir tempat transaksi diproses. |
| `terminal_id` | String | ID terminal pembayaran EDC/POS. |
| `warehouse_id` | String | ID gudang asal barang. |
| `batch_number` | String | Nomor batch produksi barang. |
| `sku_code` | String | Kode SKU (*Stock Keeping Unit*) produk. |
| `barcode_number` | String | Nomor Barcode/EAN produk. |

---

### Domain 2: Demografi & Profil Pelanggan (19 Kolom)
Atribut yang menggambarkan demografi, latar belakang sosio-ekonomi, dan profil keluarga pelanggan.

| Nama Kolom | Tipe Data | Deskripsi / Arti Kolom |
|------------|-----------|------------------------|
| `customer_age` | Integer | Usia pelanggan (tahun). |
| `customer_gender` | String | Jenis kelamin pelanggan (Male/Female). |
| `customer_marital_status` | String | Status pernikahan (Single, Married, Divorced). |
| `customer_education` | String | Tingkat pendidikan (High School, Bachelor, Master, PhD, None). |
| `customer_occupation` | String | Pekerjaan pelanggan. |
| `customer_income` | Float | Pendapatan bulanan/tahunan pelanggan (diimputasi median 250.000 jika null). |
| `household_size` | Integer | Jumlah anggota keluarga dalam satu rumah. |
| `number_of_children` | Integer | Jumlah anak yang dimiliki pelanggan. |
| `customer_since_year` | Integer | Tahun pertama kali bergabung menjadi pelanggan. |
| `customer_tenure_months` | Integer | Lama durasi menjadi pelanggan (bulan). |
| `urban_rural` | String | Tipe wilayah tempat tinggal (Urban, Suburban, Rural). |
| `country` | String | Negara asal pelanggan. |
| `region` | String | Wilayah/region geografis. |
| `state_province` | String | Provinsi tempat tinggal. |
| `city` | String | Kota tempat tinggal. |
| `district` | String | Kecamatan/distrik tempat tinggal. |
| `postal_code` | String | Kode pos lokasi tinggal. |
| `generation_group` | String | Kelompok generasi (Gen Z, Millennial, Gen X, Boomer). |
| `lifestyle_segment` | String | Kategori gaya hidup pelanggan. |

---

### Domain 3: Keanggotaan, Segmentasi & LTV (14 Kolom)
Metrik analitis perilaku pelanggan, tingkat loyalitas, risiko *churn*, dan nilai masa depan pelanggan (*LTV*).

| Nama Kolom | Tipe Data | Deskripsi / Arti Kolom |
|------------|-----------|------------------------|
| `customer_membership_status` | String | Status keanggotaan (Member / Non-Member). |
| `membership_tier` | String | Tingkatan keanggotaan (Platinum, Gold, Silver, Bronze, None). |
| `card_type` | String | Jenis kartu keanggotaan/kredit yang digunakan. |
| `loyalty_points_earned` | Integer | Poin loyalitas yang diperoleh dari transaksi ini. |
| `loyalty_points_redeemed` | Integer | Poin loyalitas yang ditukarkan pada transaksi ini. |
| `loyalty_points_balance` | Integer | Saldo sisa poin loyalitas pelanggan. |
| `membership_duration_months` | Integer | Durasi berlangganan program keanggotaan (bulan). |
| `customer_visit_frequency` | Integer | Frekuensi belanja bulanan pelanggan. |
| `average_monthly_visits` | Integer | Rata-rata kunjungan ke toko per bulan. |
| `average_transaction_value` | Float | Rata-rata nilai belanja per transaksi (AOV historis). |
| `customer_lifetime_value` | Float | **(LTV)** Estimasi nilai total kontribusi belanja sepanjang masa. |
| `customer_retention_score` | Float | Skor retensi pelanggan (0 - 100). |
| `customer_churn_risk` | Float | **(Churn Risk)** Skor prediksi kemungkinan pelanggan beralih/berhenti (0.0 - 1.0). |
| `customer_segment` | String | **Segmen Pelanggan:** VIP, Loyalty Tier A, Regular, Budget Shopper. |

---

### Domain 4: Toko & Operasional Cabang (32 Kolom)
Informasi mengenai kapasitas toko, performa karyawan kasir, waktu antrean, dan efisiensi operasional cabang.

| Nama Kolom | Tipe Data | Deskripsi / Arti Kolom |
|------------|-----------|------------------------|
| `store_name` | String | Nama toko / nama cabang. |
| `store_type` | String | Format toko (Flagship Store, Express Center, Standard Store). |
| `store_size_sqft` | Integer | Luas area toko dalam kaki persegi (sqft). |
| `store_age_years` | Integer | Usia beroperasinya cabang (tahun). |
| `number_of_employees` | Integer | Jumlah karyawan yang bertugas di cabang. |
| `number_of_checkout_counters` | Integer | Jumlah Meja Kasir Reguler. |
| `number_of_self_checkout_counters` | Integer | Jumlah Meja *Self-Checkout* Mandiri. |
| `parking_spaces` | Integer | Kapasitas tempat parkir kendaraan. |
| `daily_customer_capacity` | Integer | Batas kapasitas maksimal pengunjung per hari. |
| `checkout_wait_time_minutes` | Float | Durasi waktu tunggu antrean di kasir (menit). |
| `queue_length` | Integer | Jumlah orang dalam antrean kasir. |
| `cashier_rating` | Float | Rating penilaian kinerja petugas kasir (1 - 5). |
| `store_cleanliness_score` | Float | Skor kebersihan toko. |
| `store_service_score` | Float | Skor kualitas layanan cabang. |
| `product_availability_score` | Float | Skor ketersediaan barang di etalase. |
| `store_experience_score` | Float | Skor pengalaman belanja keseluruhan di toko. |
| `store_efficiency_score` | Float | Skor efisiensi operasional cabang. |
| `employee_experience_years` | Integer | Rata-rata pengalaman kerja karyawan (tahun). |
| `employee_performance_score` | Float | Skor kinerja karyawan cabang. |
| `employee_customer_service_score` | Float | Skor kepuasan layanan karyawan. |
| *(21 kolom operasional cabang lainnya)* | Mixed | Parameter teknis utilitas toko, AC, pencahayaan, dll. |

---

### Domain 5: Produk, Kategori & Stok (53 Kolom)
Atribut hierarki produk, kategori bisnis, kondisi persediaan (inventaris), dan manajemen logistik.

| Nama Kolom | Tipe Data | Deskripsi / Arti Kolom |
|------------|-----------|------------------------|
| `product_name` | String | Nama lengkap produk/barang. |
| `product_category` | String | **Kategori Utama:** Health & Beauty, Electronics, Frozen Foods, Groceries, Bakery, dll. |
| `product_subcategory` | String | Sub-kategori spesifik produk. |
| `brand_name` | String | Merek / brand produk. |
| `package_quantity` | Integer | Isi jumlah per kemasan. |
| `package_weight` | Float | Berat kemasan produk (kg). |
| `stock_before_transaction` | Integer | Stok barang di rak sebelum transaksi. |
| `quantity_sold` | Integer | Jumlah unit barang yang terjual. |
| `stock_after_transaction` | Integer | Sisa stok barang di rak setelah transaksi. |
| `reorder_level` | Integer | Batas minimum stok untuk pemesanan ulang (*reorder point*). |
| `maximum_stock_level` | Integer | Kapasitas maksimal stok barang di toko. |
| `safety_stock` | Integer | Stok pengaman (*safety stock*) penahan *out-of-stock*. |
| `inventory_turnover_rate` | Float | Tingkat perputaran inventaris toko. |
| `days_of_inventory` | Float | Estimasi hari ketahanan stok tersisa. |
| `shelf_life_days` | Integer | Masa kadaluwarsa simpan produk (hari). |
| `storage_temperature` | Float | Suhu penyimpanan ideal (°C) — krusial untuk *cold-chain Frozen Foods*. |
| `expiry_risk_score` | Float | Skor risiko barang mendekati kadaluwarsa. |
| *(36 kolom stok & supplier lainnya)* | Mixed | Parameter lead time supplier, MOQ, defect rate supplier, dll. |

---

### Domain 6: Penjualan, Harga & Keuangan (40 Kolom)
Metrik moneter, modal (COGS), margin keuntungan, diskon, dan indikator performa penjualan.

| Nama Kolom | Tipe Data | Deskripsi / Arti Kolom |
|------------|-----------|------------------------|
| `quantity` | Integer | Jumlah barang yang dibeli pada baris transaksi. |
| `unit_price` | Float | Harga per unit barang sebelum diskon. |
| `unit_cost` | Float | Modal awal per unit barang (HPP/COGS per unit). |
| `selling_price` | Float | Harga jual efektif per unit setelah diskon. |
| `regular_price` | Float | Harga acuan resmi barang. |
| `discount_amount` | Float | Nilai potongan diskon dalam nominal uang. |
| `discount_percent` | Float | Persentase diskon yang diberikan (%). |
| `gross_sales` | Float | Penjualan kotor sebelum diskon & pajak. |
| `net_sales` | Float | Penjualan bersih setelah dikurangi diskon. |
| `tax_amount` | Float | Jumlah pajak (PPN/VAT) transaksi. |
| `total_amount` | Float | **Total Nominal Pembayaran:** Nilai belanja transaksi bersih. |
| `cost_of_goods_sold` | Float | **COGS / HPP:** Total modal barang terjual dalam transaksi. |
| `gross_profit` | Float | Keuntungan kotor (`gross_sales` - `COGS`). |
| `profit_margin_percent` | Float | Margin keuntungan dalam persen (%). |
| `calculated_profit` | Float | **(Feature Engineered)** Profit murni = `total_amount` - `cost_of_goods_sold`. |

---

### Domain 7: Dimensi Waktu & Tanggal (41 Kolom)
Kolom temporal untuk agregasi *time-series*, analisis tren, dan fitur *drill-down* di Superset.

| Nama Kolom | Tipe Data | Deskripsi / Arti Kolom |
|------------|-----------|------------------------|
| `transaction_datetime` | **DATETIME** | Waktu & tanggal pasti transaksi (digunakan untuk *time grain* Superset: Daily, Weekly, Monthly, Yearly). |
| `transaction_date` | **DATETIME** | Tanggal transaksi saja. |
| `transaction_year_month` | String | **(Feature Engineered)** Format periode `YYYY-MM` untuk agregasi cepat per bulan. |
| `order_date` | **DATETIME** | Tanggal pemesanan pasokan barang ke supplier. |
| `delivery_date` | **DATETIME** | Tanggal pengiriman barang tiba di toko. |
| `expiry_date` | **DATETIME** | Tanggal kadaluwarsa barang. |
| `day_of_week` | Integer | Hari dalam seminggu (1=Senin ... 7=Minggu). |
| `week_number` | Integer | Minggu ke berapa dalam setahun (1-52). |
| `month` | Integer | Bulan transaksi (1-12). |
| `quarter` | Integer | Kuartal transaksi (Q1, Q2, Q3, Q4). |
| `year` | Integer | Tahun transaksi (2023, 2024). |
| `shopping_hour` | Integer | Jam bertransaksi (0-23). |
| *(29 kolom temporal lainnya)* | Mixed | Indikator jam sibuk, shift kerja, durasi waktu pengiriman, dll. |

---

### Domain 8: Retur, Komplain & Kepuasan Pelanggan (22 Kolom)
Atribut kegagalan operasional, retur barang, kategori komplain, dan skor kepuasan pelanggan.

| Nama Kolom | Tipe Data | Deskripsi / Arti Kolom |
|------------|-----------|------------------------|
| `return_flag` | String | Penanda apakah barang dikembalikan (Yes / No). |
| `return_reason` | String | Alasan barang dikembalikan (Defective, Expired, Wrong Item, Customer Mind Change). |
| `return_condition` | String | Kondisi fisik barang yang dikembalikan. |
| `refund_amount` | Float | Total nominal uang yang dikembalikan (*refund*). |
| `refund_method` | String | Metode pengembalian dana (Cash, Store Credit, Original Payment). |
| `complaint_flag` | String | Penanda adanya komplain dari konsumen (Yes / No). |
| `complaint_category` | String | Kategori masalah komplain (Product Defect, Long Wait Time, Rude Service, Expired Product). |
| `customer_satisfaction_score` | Float | Skor kepuasan belanja pelanggan (1.0 - 5.0). |
| `customer_complaint_rate` | Float | Rasio frekuensi komplain dari pelanggan tersebut. |
| `service_rating` | Float | Penilaian kualitas layanan cabang. |

---

### Domain 9: Promosi, Pemasaran & Ekonomi Makro (33 Kolom)
Data promosi, metode pembayaran, cuaca, serta indikator kompetisi dan ekonomi di wilayah cabang.

| Nama Kolom | Tipe Data | Deskripsi / Arti Kolom |
|------------|-----------|------------------------|
| `payment_method` | String | **Metode Pembayaran:** QRIS, E-Wallet, Credit Card, Debit Card, Cash. |
| `promotion_channel` | String | Saluran media promosi (Social Media, In-Store Flyer, Mobile App, Email). |
| `holiday_type` | String | Tipe hari libur (National Holiday, Religious, School Holiday, None). |
| `holiday_name` | String | Nama hari libur spesifik. |
| `special_event` | String | Acara promosi khusus (Payday Sale, Year-End Sale, Flash Sale). |
| `competitor_count` | Integer | Jumlah toko kompetitor di radius sekitar cabang. |
| `relative_price_index` | Float | Indikator harga toko dibanding harga kompetitor. |
| `inflation_index` | Float | Indikator inflasi harga konsumen daerah. |

---

### Domain 10: Kolom Lokasi & Geografi Tambahan (53 Kolom)
Parameter koordinat GPS toko, jarak pengiriman, dan metrik wilayah cabang.

---

## 2. Seleksi Kolom untuk Framework Keputusan Bisnis (Actionable Framework)

Dari 325 kolom di atas, **14 Kolom Utama** dipilih secara spesifik untuk menyusun *Actionable Business Answers & Decision Framework* dalam menjawab 2 pertanyaan bisnis utama Seven Retail (Group Service):

| No | Kolom Terpakai | Tipe Data | Peran & Alasan Penggunaan dalam Keputusan Bisnis |
|---|---|---|---|
| **1** | **`product_category`** | String | **[Pertanyaan 1 Driver Profit & Bottleneck]** Digunakan untuk mengelompokkan profit margin dan mengisolasi kategori barang bermasalah (*Frozen Foods*, *Electronics*). |
| **2** | **`calculated_profit`** | Float | **[Pertanyaan 1 Profit Driver]** Metrik profit murni (`total_amount` - `cost_of_goods_sold`) untuk menghitung kategori produk yang memberikan kontribusi finansial tertinggi. |
| **3** | **`total_amount`** | Float | **[Pertanyaan 1 & 2 Revenue/AOV]** Total transaksi bersih untuk menghitung *Total Revenue* dan *Average Order Value (AOV)* per cabang. |
| **4** | **`customer_segment`** | String | **[Pertanyaan 1 Segmen Pelanggan]** Mengelompokkan konsumen (*VIP*, *Loyalty Tier A*, *Regular*) untuk mengidentifikasi segmen bernilai bisnis terbesar. |
| **5** | **`customer_lifetime_value` (LTV)** | Float | **[Pertanyaan 1 Retensi VIP]** Metrik dasar *Action Decision* retensi segmen VIP agar *churn rate* tetap di bawah 5%. |
| **6** | **`return_flag`** / **`return_reason`** | String | **[Pertanyaan 1 Bottleneck]** Menghitung rasio retur dan mendeteksi masalah rantai dingin (*cold-chain*) logistik pada produk *Frozen Foods*. |
| **7** | **`complaint_flag`** / **`complaint_category`** | String | **[Pertanyaan 1 QA Bottleneck]** Mengisolasi kategori komplain utama untuk pemicu audit *quality assurance*. |
| **8** | **`store_id`** / **`store_name`** | String | **[Pertanyaan 2 Monitoring 200+ Cabang]** Identifikasi lokasi cabang untuk membandingkan kinerja AOV dan Profit antar 200+ pusat layanan Seven Retail. |
| **9** | **`store_type`** | String | **[Pertanyaan 2 Format Cabang]** Membedakan performa *Flagship Store* vs *Express Center*. |
| **10** | **`basket_size`** / **`quantity`** | Integer | **[Pertanyaan 2 Analisis AOV]** Jumlah barang per transaksi untuk mencari pemicu rendahnya AOV di toko yang *underperform*. |
| **11** | **`customer_churn_risk`** | Float | **[Pertanyaan 2 Prediksi Churn]** Skor prediksi *churn* untuk pemicu intervensi CRM re-engagement otomatis. |
| **12** | **`days_since_last_purchase`** | Integer | **[Pertanyaan 2 CRM Alert]** Ambang batas keaktifan belanja (>45 hari) sebelum pelanggan beralih ke kompetitor. |
| **13** | **`transaction_datetime`** | Datetime | **[Pertanyaan 1 & 2 Temporal Drilldown]** Kolom tanggal bertipe `DATETIME` untuk *drill-down* harian, mingguan, bulanan, tahunan di Superset. |
| **14** | **`payment_method`** | String | **[Pertanyaan 1 & 2 Efisiensi Kasir]** Mengukur proporsi metode pembayaran (QRIS, E-Wallet, Card, Cash) untuk efisiensi transaksi. |

---

## 📌 Ringkasan Dokumentasi

File ini tersimpan di: **`notebooks/DATA_DICTIONARY.md`**  
Dapat diakses dan dipublish langsung ke repository GitHub sebagai panduan teknis & analitis lengkap. 🚀

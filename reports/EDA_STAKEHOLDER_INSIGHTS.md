# 📊 EDA Stakeholder Insights — Temuan Utama dari Analisis Data

**Proyek:** Data Analyst Portfolio – Seven Retail (Group Service Associate)  
**Dataset:** Supermarket Large Dataset (120.000 transaksi × 323 kolom)  
**Tanggal Analisis:** November 2026  
**Tujuan:** Memberikan temuan awal dari EDA yang relevan untuk pengambilan keputusan bisnis

---

## 🎯 Ringkase Eksekutif

Dari 120.000 transaksi yang dianalisis, Seven Retail menghasilkan **total pendapatan 11,29 juta** dengan **keuntungan bersih 5,07 juta** dan margin keuntungan keseluruhan sebesar **44,9%**. Terdapat 5 kategori produk terdepan yang mendominasi profit, 5 toko terbaik yang menjadi teladan operasional, serta 2,7% pelanggan dengan risiko *churn* tinggi yang memerlukan intervensi segera.

---

## 1. Kinerja Keuangan Secara Keseluruhan

| Metrik | Nilai |
|--------|-------|
| Total Pendapatan (*Total Revenue*) | 11,29 juta |
| Total Keuntungan (*Gross Profit*) | 5,07 juta |
| Margin Keuntungan Keseluruhan | **44,9%** |
| Rata-rata Nilai Transaksi (*AOV*) | **94,09** |
| Jumlah Transaksi Unik | 120.000 |

**Catatan untuk Stakeholder:** Margin 44,9% adalah angka yang sehat untuk ritel multi-cabang, namun terdapat peluang optimisasi pada kategori dengan margin di bawah rata-rata.

---

## 2. Analisis Kategori Produk — Driver Profit & Margin

Berikut adalah perbandingan antara **Kategori dengan Profit Nominal Tertinggi** (Volume Play) dan **Kategori dengan Margin Persentase Tertinggi** (Value Play):

### A. Top 5 Kategori Berdasarkan Margin Keuntungan (%) — *Aggregate Margin (SUM(Profit) / SUM(Revenue))*
> *Catatan: Ini adalah metrik sesungguhnya (aggregate margin), memperbaiki kesalahan rata-rata per baris sebelumnya.*

| Kategori | Pendapatan | Keuntungan | Margin (%) | Jumlah Transaksi |
|----------|------------|------------|------------|------------------|
| **Supplements** | 152.756 | 79.235 | **51,9%** | 1.521 |
| **First Aid** | 218.498 | 110.079 | **50,4%** | 1.513 |
| **Batteries** | 196.203 | 95.164 | **48,5%** | 1.896 |
| **Kitchenware** | 98.350 | 47.636 | **48,4%** | 1.012 |
| **Accessories** | 185.616 | 89.881 | **48,4%** | 1.897 |

### B. Top 5 Kategori Berdasarkan Keuntungan Nominal Tertinggi (Total Profit) — *Volume Play*

| Kategori | Pendapatan | Keuntungan | Margin (%) | Jumlah Transaksi |
|----------|------------|------------|------------|------------------|
| **Grocery** | 573.786 | 253.434 | 44,2% | 5.734 |
| **Meat** | 552.706 | 246.306 | 44,6% | 5.865 |
| **Bakery** | 471.083 | 226.872 | 48,2% | 5.162 |
| **Fruits** | 511.329 | 223.617 | 43,7% | 5.775 |
| **Vegetables** | 490.631 | 223.551 | 45,6% | 5.552 |

**Temuan Penting:**
- **Supplements** dan **First Aid** memimpin dari sisi efisiensi margin (di atas 50%), meski volume transaksi lebih kecil — cocok untuk strategi *cross-selling* dan penambahan *shelf-space* bernilai tinggi.
- **Grocery** dan **Meat** adalah kontributor *nominal profit* terbesar karena volume transaksi yang sangat tinggi — berfungsi sebagai *anchor categories* untuk lalu lintas pelanggan.
- Bakery berada di posisi unik: memiliki volume tinggi sekaligus margin yang sangat kompetitif (48,2%).

---

## 3. Segmen Pelanggan — Siapa yang Menghasilkan Nilai Tertinggi?

| Segmen | Pendapatan Total | Rata-rata AOV | Total Keuntungan | Jumlah Pelanggan | Rata-rata LTV |
|--------|------------------|---------------|------------------|------------------|---------------|
| Family Shopper | 2.01 juta | 93,98 | 891.627 | 13.541 | 8.864 |
| Regular Shopper | 2,25 juta | 93,40 | 1.01 juta | 15.194 | 8.813 |
| Loyal Customer | 1,37 juta | 95,11 | 613.447 | 9.037 | 8.743 |
| Budget Shopper | 1,70 juta | 94,35 | 764.566 | 11.321 | 8.879 |
| Premium Shopper | 1,12 juta | 93,22 | 502.068 | 7.606 | 8.817 |
| Occasional Shopper | 1,13 juta | 94,99 | 516.157 | 7.625 | 8.824 |
| Deal Seeker | 897.635 | 93,50 | 398.537 | 6.051 | 8.918 |
| Convenience Shopper | 815.707 | 94,64 | 368.350 | 5.424 | 8.659 |

**Temuan Penting:**
- **Family Shopper** dan **Regular Shopper** adalah dua segmen dengan kontribusi pendapatan dan pelanggan terbesar — prioritas untuk program retensi massal.
- LTV rata-rata relatif merata di seluruh segmen (8.659–8.918), menunjukkan tidak ada segmen yang secara signifikan "menggeser" nilai pelanggan.

---

## 4. Top 10 Toko — Pelaku Operasional Terbaik

| Toko | Pendapatan | Keuntungan | Margin (%) | Transaksi |
|------|------------|------------|------------|-----------|
| S00000064 | 64.854 | 32.894 | **50,7%** | 617 |
| S00000167 | 65.802 | 31.354 | 47,6% | 632 |
| S00000161 | 64.131 | 31.078 | 48,5% | 599 |
| S00000136 | 64.654 | 30.975 | 47,9% | 612 |
| S00000143 | 65.878 | 30.339 | 46,1% | 640 |
| S00000121 | 61.776 | 30.310 | 49,1% | 609 |
| S00000095 | 61.276 | 29.989 | 48,9% | 622 |
| S00000146 | 61.075 | 29.726 | 48,7% | 582 |
| S00000119 | 63.584 | 29.584 | 46,5% | 636 |
| S00000032 | 63.217 | 29.558 | 46,8% | 582 |

**Temuan Penting:**
- **S00000064** adalah toko terbaik dengan margin 50,7% — studi kasus ideal untuk ditiru di cabang lain (praktik terbaik stok, tata letak, atau pelatihan karyawan).
- Seluruh 10 toko teratas memiliki margin di atas 46%, menunjukkan konsistensi operasional yang baik di antara pelaku terdepan.

---

## 5. Bottleneck Operasional — Retur & Komplain

| Indikator | Nilai |
|-----------|-------|
| Tingkat Retur | **3,06%** |
| Tingkat Komplain | **2,98%** |

### 5 Kategori dengan Retur Tertinggi:
1. **Vegetables** — 191 retur
2. **Grocery** — 190 retur
3. **Snacks** — 176 retur
4. **Fruits** — 165 retur
5. **Meat** — 156 retur

### 5 Kategori dengan Komplain Tertinggi:
1. **Vegetables** — 187 komplain
2. **Fruits** — 179 komplain
3. **Meat** — 178 komplain
4. **Snacks** — 172 komplain
5. **Grocery** — 158 komplain

**Temuan Penting:**
- Kategori **segmen segar** (Vegetables, Fruits, Meat) mendominasi retur dan komplain — kemungkinan besar terkait kualitas produk, kedaluwarsa, atau rantai dingin (*cold-chain*).
- Tingkat retur 3,06% masih dalam batas normal ritel, namun perlu ditindaklanjuti untuk kategori segar agar tidak menyebar ke kategori lain.

---

## 6. Metode Pembayaran — Preferensi Pelanggan

| Metode | Total Pendapatan | Jumlah Transaksi | Parsentase Pendapatan |
|--------|------------------|------------------|----------------------|
| Credit Card | 3,41 juta | 36.166 | **30,2%** |
| Debit Card | 2,84 juta | 30.042 | **25,1%** |
| Cash | 2,23 juta | 23.801 | **19,8%** |
| Mobile Wallet | 1,71 juta | 18.046 | **15,1%** |
| Gift Card | 556.483 | 5.952 | 4,9% |
| Online Payment | 550.447 | 5.993 | 4,9% |

**Temuan Penting:**
- **Credit Card dan Debit Card** mendominasi dengan kombinasi 55,3% dari total pendapatan.
- **Mobile Wallet** mencatat 15,1% — tren digitalisasi pembayaran yang perlu dipromosikan lebih lanjut untuk mengurangi antrean tunai di kasir.

---

## 7. Risiko *Churn* Pelanggan

| Kategori Risiko | Jumlah Pelanggan | Persentase |
|-----------------|------------------|------------|
| Tinggi (>0,7) | 2.721 | **2,3%** |
| Sedang (0,5–0,7) | 16.442 | 13,7% |
| Rendah (<0,5) | 100.837 | 84,0% |

**Temuan Penting:**
- **2.721 pelanggan (2,3%)** terklasifikasi sebagai risiko *churn* tinggi — kelompok kecil namun strategis untuk intervensi targeted sebelum mereka beralih ke kompetitor.

---

## 8. Program Loyalitas

| Indikator | Nilai |
|-----------|-------|
| Pelanggan Member | 0% *(semua null diimputasi)* |
| Rata-rata Saldo Poin | 288 poin |
| Rasio Poin Ditebus vs Diperoleh | 24,9% |

**Temuan Penting:**
- Hanya **24,9% poin loyalty** yang ditebus dari total yang diperoleh — pelanggan mencatat poin tetapi jarang menggunakan. Ini adalah peluang untuk merancang program redeem yang lebih menarik guna meningkatkan retensi dan frequency belanja.

---

## 9. Perbandingan Tipe Toko

| Tipe Toko | Pendapatan Total | AOV | Keuntungan Total | Transaksi | Margin (%) |
|-----------|------------------|-----|------------------|-----------|------------|
| Supermarket | 4,17 juta | 93,67 | 1,87 juta | 44.492 | 44,9% |
| Neighborhood Store | 2,92 juta | 94,04 | 1,31 juta | 31.103 | 44,9% |
| Hypermarket | 1,76 juta | 94,65 | 789.044 | 18.544 | 45,0% |
| Express Store | 1,55 juta | 95,15 | 698.239 | 16.315 | 45,0% |
| Wholesale Store | 890.879 | 93,32 | 394.473 | 9.546 | 44,3% |

**Temuan Penting:**
- **Supermarket** adalah kontributor pendapatan terbesar, namun margin relatif merata di semua tipe toko (44,3%–45,0%).
- Perbedaan margin antara tipe toko kecil (sekitar 0,7%), menunjukkan efisiensi operasional yang seragam di seluruh format cabang.

---

## 📌 Rekomendasi Tindakan Segera untuk Stakeholder

| Prioritas | Tindakan | Dasar Temuan |
|-----------|----------|--------------|
| **Tinggi** | Audit *cold-chain* pada kategori segar (Vegetables, Fruits, Meat) untuk menurunkan retur & komplain | Tingkat komplain & retur tertinggi ada pada kategori segar |
| **Tinggi** | Program intervensi targeted untuk 2.721 pelanggan risiko *churn* tinggi | 2,3% pelanggan berisiko *churn* tinggi |
| **Sedang** | Tingkatkan *shelf-space* & *cross-selling* untuk kategori margin tinggi (Supplements 51,9% & First Aid 50,4%) di semua cabang | Supplements & First Aid memiliki margin tertinggi (aggregate) |
| **Sedang** | Promosikan penggunaan Mobile Wallet untuk mengurangi antrean kasir | Mobile Wallet hanya 15,1% dibanding Credit/Debit 55,3% |
| **Rendah** | Rancang kembali program redeem poin loyalty (hanya 24,9% ditebus) | Rasio penebusan poin rendah |
| **Rendah** | Pelajari praktik terbaik dari toko S00000064 (margin 50,7%) untuk ditiru ke cabang lain | Toko terbaik memiliki margin 5,8 poin di atas rata-rata |

---

## 📂 File Pendukung

- `reports/EDA_REPORT.md` — Laporan EDA lengkap dengan statistik semua 323 kolom
- `reports/DATA_CLEANING_REPORT.md` — Dokumentasi proses pembersihan data
- `notebooks/DATA_DICTIONARY.md` — Kamus data & definisi kolom
- `reports/BUSINESS_REQUIREMENTS.md` — Pemetaan kebutuhan bisnis Seven Retail ke solusi data
- `reports/ACTIONABLE_BUSINESS_ANSWERS.md` — Jawaban actionable & keputusan bisnis

---

*Laporan ini dihasilkan dari proses EDA otomatis menggunakan Python (Pandas/NumPy) dan siap disajikan kepada manajemen Seven Retail untuk diskusi langkah selanjutnya.* 🚀

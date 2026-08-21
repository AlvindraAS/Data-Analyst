**# 🏗️ Global Food Delivery Market Intelligence Platform**

[![Python]\(https\://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)]\(https\://www\.python.org/)

[![Streamlit]\(https\://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg?logo=streamlit&logoColor=white)]\(https\://streamlit.io/)

[![Plotly]\(https\://img.shields.io/badge/Plotly-5.18%2B-3F4F75.svg?logo=plotly&logoColor=white)]\(https\://plotly.com/)

[![Scikit-Learn]\(https\://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E.svg?logo=scikit-learn&logoColor=white)]\(https\://scikit-learn.org/)

[![Statsmodels]\(https\://img.shields.io/badge/Statsmodels-0.14%2B-005C8A.svg)]\(https\://www\.statsmodels.org/)

[![License: MIT]\(https\://img.shields.io/badge/License-MIT-green.svg)]\(https\://opensource.org/licenses/MIT)

***>*** **\*\*Platform riset pasar, penetapan harga strategis (***\*strategic pricing\****), dan intelijen kompetisi pesan-antar makanan global berbasis data riil dari 10 kota metropolitan lintas 5 benua.\*\***

**## 📚 Sumber Dataset**

Proyek ini merupakan hasil analisis dari dataset Kaggle **Global Restaurant Delivery Intelligence** yang tersedia pada:

[https://www.kaggle.com/datasets/saitejabandaruin/global-restaurant-delivery-intelligence](https://www.kaggle.com/datasets/saitejabandaruin/global-restaurant-delivery-intelligence)

\---

\---

**## 📑 Daftar Isi**

**1.** **[**Ringkasan Eksekutif & Visi Proyek**]\(**#-ringkasan-eksekutif--visi-proyek**)**

**2.** **[**Arsitektur Data & Pipeline Medallion**]\(**#-arsitektur-data--pipeline-medallion**)**

**3.** **[**Skema Dataset & Relational Mapping**]\(**#-skema-dataset--relational-mapping**)**

**4.** **[**Daftar & Metodologi 8 Sub-Proyek**]\(**#-daftar--metodologi-8-sub-proyek**)**

   **-** **[**Sub-Proyek 1: Cross-City Price & PPP Benchmarking**]\(**#sub-proyek-1-cross-city-price--ppp-benchmarking**)**

   **-** **[**Sub-Proyek 2: Platform Commission & Markup Decomposition**]\(**#sub-proyek-2-platform-commission--markup-decomposition**)**

   **-** **[**Sub-Proyek 3: Dynamic Pricing & Surge Intelligence**]\(**#sub-proyek-3-dynamic-pricing--surge-intelligence**)**

   - [Sub-Proyek 4: Promo & Minimum Order Friction Elasticity]\(#sub-proyek-4-promo--minimum-order-friction-elasticity)

   - [Sub-Proyek 5: Sponsored Listing ROI & A/B Testing]\(#sub-proyek-5-sponsored-listing-roi--ab-testing)

   - [Sub-Proyek 6: Market Entry & Whitespace Analysis]\(#sub-proyek-6-market-entry--whitespace-analysis)

   - [Sub-Proyek 7: Membership Pricing Impact & Parity Audit]\(#sub-proyek-7-membership-pricing-impact--parity-audit)

   - [Sub-Proyek 8: Food Price Inflation Tracker]\(#sub-proyek-8-food-price-inflation-tracker)

5\. [Struktur Repositori Direktori]\(#-struktur-repositori-direktori)

6\. [Panduan Instalasi & Eksekusi]\(#-panduan-instalasi--eksekusi)

7\. [Fitur Utama Streamlit Enterprise Dashboard]\(#-fitur-utama-streamlit-enterprise-dashboard)

8\. [Temuan Strategis & Rekomendasi Bisnis]\(#-temuan-strategis--rekomendasi-bisnis)

\---

\## 🎯 Ringkasan Eksekutif & Visi Proyek

Industri \*online food delivery\* global beroperasi di tengah dinamika biaya hidup yang kompleks, perang komisi antar platform, serta perilaku konsumen yang sensitif terhadap biaya tersembunyi. Proyek ini membangun \*\*Global Food Delivery Market Intelligence Platform\*\* terpadu yang membedah perilaku harga, efektivitas komisi, strategi promosi, dan inflasi pangan di \*\*10 kota metropolitan dunia\*\*:

\* \*\*Amerika Utara\*\*: New York City, Los Angeles (USA - \`USD\`)

\* \*\*Eropa\*\*: London, Manchester (United Kingdom - \`GBP\`)

\* \*\*Asia\*\*: Tokyo, Osaka (Japan - \`JPY\`), Mumbai, Delhi (India - \`INR\`)

\* \*\*Amerika Selatan\*\*: São Paulo, Rio de Janeiro (Brazil - \`BRL\`)

\### Cakupan Data

\* \*\*5.000\*\* Restoran

\* \*\*62.417\*\* Item Menu & Nilai Nutrisi

\* \*\*18.887\*\* Rekaman Riwayat Perubahan Harga (\*Time-Series\*)

\* \*\*12\*\* Kategori Kuliner (\*Cuisines\*)

\---

\## 🏛️ Arsitektur Data & Pipeline Medallion

Proyek ini menerapkan arsitektur data \*\*Decoupled Analytics Serving\*\* standar industri. Komputasi analitik berat (Machine Learning, Regresi OLS, konversi PPP, dan pemrosesan time-series) dieksekusi di \*Notebook Layer\* dan disimpan sebagai \*\*Gold Data Marts\*\*, yang kemudian disajikan secara instan (\*zero latency\*) oleh \*\*Streamlit Presentation Layer\*\*.



\`\`\`

[ BRONZE LAYER : RAW CSV DATA ]

├── cities.csv, countries.csv, cuisines.csv, delivery\_metrics.csv

├── menus.csv, nutrition.csv, price\_history.csv, restaurants.csv

└── restaurant\_features.csv, restaurant\_statistics.csv, city\_statistics.csv

│

▼

[ SILVER LAYER : HEAVY ANALYTICS / NOTEBOOKS ]

├── 1. FX Standardization (USD Pivot) & Cost-of-Living PPP Normalization

├── 2. Commission & Fee Decomposition Engine

├── 3. Random Forest Surge Drivers & Spatial Cluster Modeling

├── 4. Econometric OLS Elasticity & Minimum Order Friction Modeling

├── 5. Quasi-Experimental A/B Hypothesis Testing (Welch's t-test / Cohen's d)

├── 6. Supply Scarcity & Demand Appetite Whitespace Scoring

├── 7. Membership Price Parity & Loyalty Permutation Test

└── 8. Time-Series Cumulative Monthly Price Indexing (Base = 100)

│

▼

[ GOLD LAYER : PRE-COMPUTED DATA MARTS ]

├── subproject\_1\_city\_price\_benchmarks.csv

├── subproject\_2\_platform\_markup\_analysis.csv

├── subproject\_3\_surge\_intelligence.csv & subproject\_3\_city\_surge\_summary.csv

├── subproject\_4\_promo\_effectiveness.csv & subproject\_4\_promo\_segment\_kpi.csv

├── subproject\_5\_sponsored\_roi\_analysis.csv & subproject\_5\_city\_ad\_benchmark.csv

├── subproject\_6\_whitespace\_analysis.csv & subproject\_6\_expansion\_recommendations.csv

├── subproject\_7\_membership\_impact\_analysis.csv & subproject\_7\_city\_membership\_summary.csv

└── subproject\_8\_monthly\_city\_inflation.csv & subproject\_8\_city\_inflation\_kpi.csv

│

▼

[ PLATINUM LAYER : SERVING & DASHBOARD ]

└── Streamlit Enterprise Dashboard (app.py) ──▶ Interactive Plotly BI Cockpit

\`\`\`

\---

\## 📁 Skema Dataset & Relational Mapping



\`\`\`

             ┌─────────────────┐

             │  countries.csv  │

             └────────┬────────┘

                      │ (Country)

                      ▼

             ┌─────────────────┐

             │   cities.csv    │◄───(City, Country)───┐

             └────────┬────────┘                      │

                      │ (City, Country)               │

                      ▼                               │

             ┌─────────────────┐             ┌─────────────────────┐

             │ restaurants.csv ├────────────►│ city\_statistics.csv │

             └──┬───────────┬──┘             └─────────────────────┘

                │           │

 (Restaurant\_ID)│           │(Restaurant\_ID)

                ▼           ▼



┌────────────────────────┐  ┌─────────────────────────┐

│  delivery\_metrics.csv  │  │ restaurant\_features.csv │

└────────────────────────┘  └─────────────────────────┘

│           │

(Restaurant\_ID)│           │(Restaurant\_ID)

▼           ▼

┌─────────────────────────┐ ┌─────────────────────────┐

│restaurant\_statistics.csv│ │        menus.csv        │

└─────────────────────────┘ └───────────┬─────────────┘

│ (Menu\_ID)

▼

┌─────────────────────────┐

│    price\_history.csv    │

└─────────────────────────┘

\`\`\`

\| File CSV | Dimensi Data | Kunci Relasi (\*Keys\*) | Deskripsi Isi |

\| :--- | :--- | :--- | :--- |

\| \`cities.csv\` | 10 baris, 9 kolom | \`City\`, \`Country\` | Populasi, luas wilayah, kepadatan, UMR rata-rata, dan \*Cost of Living Index\*. |

\| \`countries.csv\` | 5 baris, 6 kolom | \`Country\` | Wilayah regional, kelompok pendapatan, kode mata uang (\*Currency\*), dan zona waktu. |

\| \`city\_statistics.csv\` | 10 baris, 7 kolom | \`City\`, \`Country\` | Kepadatan restoran, indeks diversitas kuliner, rating kota, dan cakupan pengantaran. |

\| \`cuisines.csv\` | 12 baris, 4 kolom | \`Cuisine\_name\` | Induk kuliner (\*Parent cuisine\*) dan klasifikasi wilayah gastronomi. |

\| \`restaurants.csv\` | 5.000 baris, 17 kolom | \`Restaurant\_ID\` | Profil restoran, status jaringan/lokal, koordinat lintang/bujur, \*price level\*, dan rating. |

\| \`delivery\_metrics.csv\` | 3.187 baris, 10 kolom | \`Restaurant\_ID\` | Ongkir dasar (\*Delivery fee\*), biaya layanan, biaya kemasan, multiplier lonjakan (\*Peak multiplier\*). |

\| \`menus.csv\` | 62.417 baris, 15 kolom | \`Menu\_ID\`, \`Restaurant\_ID\` | Katalog item makanan, kategori (\*Main, Starter, Beverage, Dessert\*), harga, dan mata uang. |

\| \`nutrition.csv\` | 62.417 baris, 11 kolom | \`Menu\_ID\` | Kalori, protein, lemak, karbohidrat, sodium, serta atribut diet (vegan/vegetarian/gluten-free). |

\| \`price\_history.csv\` | 18.887 baris, 5 kolom | \`Menu\_ID\` | Rekaman timestamp perubahan harga, harga sebelumnya (\*Previous\*), dan harga saat ini (\*Current\*). |

\| \`restaurant\_features.csv\` | 5.000 baris, 14 kolom | \`Restaurant\_ID\` | Fasilitas gerai: WiFi, Drive-through, operasional 24 jam, opsi Halal, Vegan, dan alkohol. |

\| \`restaurant\_statistics.csv\` | 5.000 baris, 6 kolom | \`Restaurant\_ID\` | Skor popularitas (0–100), skor persepsi nilai (\*Estimated value score\*), dan rata-rata harga menu. |

\---

\## 🔬 Daftar & Metodologi 8 Sub-Proyek

\### Sub-Proyek 1: Cross-City Price & PPP Benchmarking

\* \*\*Tujuan\*\*: Menghilangkan bias ilusi mata uang (\*currency illusion\*) dalam membandingkan harga makanan antar kota dengan normalisasi \*Purchasing Power Parity\* (PPP).

\* \*\*Metodologi\*\*:

  1. Standardisasi FX ke basis acuan USD ($USD$).

  2. Formula Harga Riil PPP (Basis New York City = 100):

     $$\text{Price}\_{\text{PPP}} = \left( \frac{\text{Price}\_{\text{USD}}}{\text{Cost of Living Index}} \right) \times 100$$

  3. Beban Pendapatan Harian (\*Daily Income Burden\*):

     $$\text{Daily Income Burden (\\%)} = \left( \frac{\text{Price}\_{\text{USD}}}{\text{Average Annual Income} / 365} \right) \times 100$$

\* \*\*Output Data Mart\*\*: \`subproject\_1\_city\_price\_benchmarks.csv\`

\---

\### Sub-Proyek 2: Platform Commission & Markup Decomposition

\* \*\*Tujuan\*\*: Membedah seluruh komponen biaya tambahan yang dibebankan kepada konsumen serta mengukur selisih harga menu dasar (\*dine-in\*) vs harga aplikasi.

\* \*\*Metodologi\*\*:

  1. Alokasi platform per wilayah pasar (\*Uber Eats, DoorDash, Deliveroo, Swiggy, Zomato, iFood\*).

  2. Dekomposisi total biaya layanan tambahan:

     $$\text{Total Fees}\_{\text{USD}} = \text{Delivery Fee} + \text{Service Fee} + \text{Packaging Fee}$$

  3. Rasio \*Fee Overhead\* Konsumen:

     $$\text{Fee Overhead (\\%)} = \left( \frac{\text{Total Fees}\_{\text{USD}}}{\text{Average Menu Price}\_{\text{USD}}} \right) \times 100$$

\* \*\*Output Data Mart\*\*: \`subproject\_2\_platform\_markup\_analysis.csv\`

\---

\### Sub-Proyek 3: Dynamic Pricing & Surge Intelligence

\* \*\*Tujuan\*\*: Mengidentifikasi faktor pemicu lonjakan harga (\*Peak Hour Multiplier\*) dan memetakan koordinat spasial zona lonjakan kritis.

\* \*\*Metodologi\*\*:

  1. Dynamic Surge Delivery Fee riil:

     $$\text{Peak Delivery Fee}\_{\text{USD}} = \text{Base Delivery Fee}\_{\text{USD}} \times \text{Peak Hour Multiplier}$$

  2. Pemodelan Prediktif Machine Learning: \*Random Forest Regressor\* (150 Estimator, Max Depth 10) untuk mengisolasi \*Feature Importance\* (Kepadatan Urban, Zona Cuaca, Rasio Pembatalan).

  3. Segmentasi 4 Zona Spasial (\*Critical Surge $\ge 2.0x$, High Surge $1.5x-1.99x$, Moderate $1.1x-1.49x$, Baseline $<1.1x$\*).

\* \*\*Output Data Mart\*\*: \`subproject\_3\_surge\_intelligence.csv\`, \`subproject\_3\_city\_surge\_summary.csv\`

\---

\### Sub-Proyek 4: Promo & Minimum Order Friction Elasticity

\* \*\*Tujuan\*\*: Menganalisis kurva elastisitas promosi dan efek batas minimum order (\*The Friction Cliff\*) terhadap volume konversi pesanan.

\* \*\*Metodologi\*\*:

  1. Rasio Hambatan Pesanan Minimum (\*Minimum Order Friction Ratio\*):

     $$\text{Friction Ratio} = \frac{\text{Minimum Order Value}\_{\text{USD}}}{\text{Average Menu Price}\_{\text{USD}}}$$

  2. Composite Volume Index:

     $$\text{Volume Index} = (0.60 \times \text{Popularity Score}) + (0.40 \times \text{Normalized Log Reviews})$$

  3. Matriks Kuadran Strategi 2x2 (\*Growth Driver, Basket Maximizer, Organic Frictions-Free, Strict Gatekeeper\*).

\* \*\*Output Data Mart\*\*: \`subproject\_4\_promo\_effectiveness.csv\`, \`subproject\_4\_promo\_segment\_kpi.csv\`

\---

\### Sub-Proyek 5: Sponsored Listing ROI & A/B Testing

\* \*\*Tujuan\*\*: Menguji signifikansi statistik dorongan eksposur iklan berbayar (\*Sponsored Placement\*) terhadap rating dan volume ulasan.

\* \*\*Metodologi\*\*:

  1. \*Quasi-Experimental A/B Testing\*: Uji hipotesis dua sampel \*Welch’s t-test\* & \*Mann-Whitney U Test\* pada kelompok perlakuan (\*Sponsored\*) vs kelompok kontrol (\*Organic\*).

  2. Standardized Effect Size (\*Cohen's d\*):

     $$d = \frac{\bar{X}\_{\text{sponsored}} - \bar{X}\_{\text{organic}}}{s\_{\text{pooled}}}$$

  3. Matriks Evaluasi Kualitas Iklan (Deteksi \*Over-Promoted / Low Quality Listings\*).

\* \*\*Output Data Mart\*\*: \`subproject\_5\_sponsored\_roi\_analysis.csv\`, \`subproject\_5\_city\_ad\_benchmark.csv\`

\---

\### Sub-Proyek 6: Market Entry & Whitespace Analysis

\* \*\*Tujuan\*\*: Menemukan ceruk pasar (\*market gap\*) kuliner dengan tingkat permintaan konsumen tinggi namun pasokan restoran minim di setiap kota.

\* \*\*Metodologi\*\*:

  1. Pangsa Pasokan Kuliner (\*Supply Share %\*):

     $$\text{Supply Share (\\%)} = \left( \frac{\text{Jumlah Restoran Kategori } i}{\text{Total Restoran di Kota}} \right) \times 100$$

  2. Formula Skor Peluang Pasar (\*Whitespace Opportunity Score\*, Skala 0–100):

     $$\text{Whitespace Score} = \text{Demand Score} \times \left( 1 - \frac{\text{Supply Share}}{\text{Max Supply Share}} \right)^{1.5}$$

\* \*\*Output Data Mart\*\*: \`subproject\_6\_whitespace\_analysis.csv\`, \`subproject\_6\_expansion\_recommendations.csv\`

\---

\### Sub-Proyek 7: Membership Pricing Impact & Parity Audit

\* \*\*Tujuan\*\*: Audit transparansi harga menu dasar pada restoran mitra langganan bebas ongkir (\*DashPass, Uber One, Swiggy One equivalent\*).

\* \*\*Metodologi\*\*:

  1. Komparasi harga menu dasar PPP: Uji inflasi harga menu pada restoran \*Membership Partner\* vs \*Non-Member\*.

  2. Formula \*Customer Loyalty Index\* (Skala 0–100):

     $$\text{Loyalty Index} = (0.40 \times \text{Popularity}) + (0.30 \times \text{Review Depth}) + \left( 0.30 \times \frac{\text{Rating}}{5.0} \times 100 \right)$$

\* \*\*Output Data Mart\*\*: \`subproject\_7\_membership\_impact\_analysis.csv\`, \`subproject\_7\_city\_membership\_summary.csv\`

\---

\### Sub-Proyek 8: Food Price Inflation Tracker

\* \*\*Tujuan\*\*: Melacak tren inflasi pangan delivery jangka panjang dan dekomposisi pergerakan harga bulanan per kategori hidangan.

\* \*\*Metodologi\*\*:

  1. Parsing 18.887 rekaman timestamp riwayat harga ke granularitas bulanan (\*Year-Month\*).

  2. Formula Indeks Harga Pangan Kumulatif (\*Base Period = 100\*):

     $$I\_t = I\_{t-1} \times \left( 1 + \frac{\text{Net Monthly Inflation Rate}\_t}{100} \right)$$

  3. Rasio Kenaikan vs Penurunan Harga (\*Hike-to-Cut Ratio\*):

     $$\text{Hike-to-Cut Ratio} = \frac{\sum \text{Price Hike Events}}{\sum \text{Price Cut Events} + \epsilon}$$

\* \*\*Output Data Mart\*\*: \`subproject\_8\_monthly\_city\_inflation.csv\`, \`subproject\_8\_city\_inflation\_kpi.csv\`

\---

\## 📂 Struktur Repositori Direktori



\`\`\`

├── data/                                          # Direktori Dataset Mentah Kaggle

│   ├── cities.csv

│   ├── city\_statistics.csv

│   ├── countries.csv

│   ├── cuisines.csv

│   ├── delivery\_metrics.csv

│   ├── menus.csv

│   ├── nutrition.csv

│   ├── price\_history.csv

│   ├── restaurant\_features.csv

│   ├── restaurant\_statistics.csv

│   └── restaurants.csv

│

├── Output/                                    # Data Marts Output Sub-Proyek 1-8

│   ├── subproject\_1\_city\_price\_benchmarks.csv

│   ├── subproject\_2\_platform\_markup\_analysis.csv

│   ├── subproject\_3\_surge\_intelligence.csv

│   ├── subproject\_3\_city\_surge\_summary.csv

│   ├── subproject\_4\_promo\_effectiveness.csv

│   ├── subproject\_4\_promo\_segment\_kpi.csv

│   ├── subproject\_5\_sponsored\_roi\_analysis.csv

│   ├── subproject\_5\_city\_ad\_benchmark.csv

│   ├── subproject\_6\_whitespace\_analysis.csv

│   ├── subproject\_6\_expansion\_recommendations.csv

│   ├── subproject\_7\_membership\_impact\_analysis.csv

│   ├── subproject\_7\_city\_membership\_summary.csv

│   ├── subproject\_8\_monthly\_city\_inflation.csv

│   └── subproject\_8\_city\_inflation\_kpi.csv

│

├── notebooks/                                     # Jupyter Notebooks Eksekusi Pipeline

│   ├── SubProject\_1\_Price\_Benchmarking.ipynb

│   ├── SubProject\_2\_Markup\_Analysis.ipynb

│   ├── SubProject\_3\_Surge\_Intelligence.ipynb

│   ├── SubProject\_4\_Promo\_Effectiveness.ipynb

│   ├── SubProject\_5\_Sponsored\_ROI.ipynb

│   ├── SubProject\_6\_Whitespace\_Opportunity.ipynb

│   ├── SubProject\_7\_Membership\_Pricing.ipynb

│   └── SubProject\_8\_Inflation\_Tracker.ipynb

├── Dashboard/                                     

│   ├── app.py                                         # Streamlit Enterprise Dashboard

├── requirements.txt                               # Dependensi Lingkungan Python

└── README.md                                      # Dokumentasi Utama Proyek

\`\`\`

\---

\## ⚙️ Panduan Instalasi & Eksekusi

\### 1. Kloning Repositori & Persiapan Lingkungan

\`\`\`bash

\# Clone repositori

git clone [https\://github.com/username/global-food-delivery-intelligence.git]\(https\://github.com/username/global-food-delivery-intelligence.git)

cd global-food-delivery-intelligence

\# Buat virtual environment (Direkomendasikan)

python -m venv venv

source venv/bin/activate  # Untuk Linux/macOS

\# venv\Scripts\activate   # Untuk Windows

\`\`\`

\### 2. Instalasi Dependensi

\`\`\`bash

pip install -r requirements.txt

\`\`\`

\### 3. Eksekusi Pipeline Data Marts (Jupyter Notebook)

Jalankan seluruh notebook di folder \`notebooks/\` untuk menghasilkan file-file data mart \`.csv\` ke direktori kerja utama.

\### 4. Menjalankan Dashboard Interaktif

\`\`\`bash

streamlit run app.py

\`\`\`

Akses dashboard pada peramban Anda melalui URL lokal: \`http\://localhost:8501\`.

\## 🖥️ Fitur Utama Streamlit Enterprise Dashboard

\- \*\*🏛️ Executive Overview & Macro Radar\*\*: Ringkasan performa makro 10 kota, radar chart komparasi stabilitas pasar, dan matriks kesehatan strategis.



\- \*\*🎛️ Dynamic Global Filter Slicers\*\*: Filter interaktif multi-level untuk Negara, Kota, Kategori Kuliner, dan Platform Delivery yang memperbarui visualisasi secara instan.



\- \*\*📊 Visualisasi Berstandar BI (Plotly Native)\*\*: \*Dual Heatmap\*, \*Violin Plot Cuaca\*, \*Scatter Plot Spasial Koordinat\*, \*Kurva Time-Series Interaktif\*, dan \*Matriks Kuadran Strategi\*.



\- \*\*📑 Executive Strategy Memo Generator\*\*: Penghasil memorandum rekomendasi bisnis otomatis untuk target kota yang dipilih dan dapat diunduh dalam format Markdown/CSV.



\## 💡 Temuan Strategis & Rekomendasi Bisnis

\### 1. Penetapan Komisi Berbasis Elastisitas Lokal

Platform tidak boleh menerapkan \*take-rate\* flat lintas negara. Di kota dengan beban PPP tinggi (seperti Delhi, Mumbai, dan São Paulo), komisi nominal yang tinggi menekan volume pesanan harian. Disarankan beralih ke skema \*tiered take-rate\* berbasis volume.

\### 2. Manajemen Hambatan Pesanan Minimum (\*The Friction Cliff\*)

Merchant yang menetapkan \*Minimum Order Value\* melebihi \*\*1.5x harga rata-rata menu\*\* mengalami lonjakan pembatalan pesanan hingga 2.4x. Platform harus merekomendasikan batas minimum pesanan dinamis berdasarkan ukuran porsi (\*single vs family meal\*).

\### 3. Mitigasi Risiko Kualitas Iklan (\*Quality-Gated Sponsored Slots\*)

Listing bersponsor terbukti meningkatkan visibilitas rata-rata sebesar \*\*+45% hingga +75%\*\* ($p < 0.001$). Namun, promosi berbayar pada restoran dengan rating $< 3.8$ justru mempercepat akumulasi ulasan negatif. Platform disarankan menetapkan batas minimum kepuasan operasional sebelum merchant diizinkan membeli slot sponsor.

\### 4. Strategi Penetrasi Ceruk Pasar (\*Whitespace Incubation\*)

Kategori kuliner autentik spesifik (seperti \*Thai & Japanese\* di kota-kota Amerika Selatan atau masakan \*Latin American\* di Asia) memiliki skor peluang pasar tertinggi. Operator \*Cloud Kitchen\* disarankan memprioritaskan kategori ini untuk menghindari perang harga di kuadran \*Red Ocean\*.

\## 🖥️ Link Dashboard Publik

Akses dashboard pada peramban Anda melalui URL: 

\## 👥 Kontributor & Lisensi

Proyek ini dikembangkan untuk kebutuhan analitik pasar, riset akademik, dan portofolio intelijen bisnis.

\- \*\*Lisensi\*\*: Didistribusikan di bawah [MIT License]\(https\://opensource.org/licenses/MIT).
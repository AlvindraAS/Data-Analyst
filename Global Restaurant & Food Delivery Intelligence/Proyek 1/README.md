# 🏗️ Global Food Delivery Market Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.18%2B-3F4F75.svg?logo=plotly&logoColor=white)](https://plotly.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-0.14%2B-005C8A.svg)](https://www.statsmodels.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Platform riset pasar, penetapan harga strategis (*strategic pricing*), dan intelijen kompetisi pesan-antar makanan global berbasis data riil dari 10 kota metropolitan lintas 5 benua.**

## 📚 Sumber Dataset

Proyek ini merupakan hasil analisis dari dataset Kaggle **Global Restaurant Delivery Intelligence** yang tersedia pada:

[https://www.kaggle.com/datasets/saitejabandaruin/global-restaurant-delivery-intelligence](https://www.kaggle.com/datasets/saitejabandaruin/global-restaurant-delivery-intelligence)

---

## 📑 Daftar Isi

1. **[Ringkasan Eksekutif & Visi Proyek](#-ringkasan-eksekutif--visi-proyek)**
2. **[Arsitektur Data & Pipeline Medallion](#-arsitektur-data--pipeline-medallion)**
3. **[Skema Dataset & Relational Mapping](#-skema-dataset--relational-mapping)**
4. **[Daftar & Metodologi 8 Sub-Proyek](#-daftar--metodologi-8-sub-proyek)**
   - **[Sub-Proyek 1: Cross-City Price & PPP Benchmarking](#sub-proyek-1-cross-city-price--ppp-benchmarking)**
   - **[Sub-Proyek 2: Platform Commission & Markup Decomposition](#sub-proyek-2-platform-commission--markup-decomposition)**
   - **[Sub-Proyek 3: Dynamic Pricing & Surge Intelligence](#sub-proyek-3-dynamic-pricing--surge-intelligence)**
   - [Sub-Proyek 4: Promo & Minimum Order Friction Elasticity](#sub-proyek-4-promo--minimum-order-friction-elasticity)
   - [Sub-Proyek 5: Sponsored Listing ROI & A/B Testing](#sub-proyek-5-sponsored-listing-roi--ab-testing)
   - [Sub-Proyek 6: Market Entry & Whitespace Analysis](#sub-proyek-6-market-entry--whitespace-analysis)
   - [Sub-Proyek 7: Membership Pricing Impact & Parity Audit](#sub-proyek-7-membership-pricing-impact--parity-audit)
   - [Sub-Proyek 8: Food Price Inflation Tracker](#sub-proyek-8-food-price-inflation-tracker)
5. [Struktur Repositori Direktori](#-struktur-repositori-direktori)
6. [Panduan Instalasi & Eksekusi](#-panduan-instalasi--eksekusi)
7. [Fitur Utama Streamlit Enterprise Dashboard](#-fitur-utama-streamlit-enterprise-dashboard)
8. [Temuan Strategis & Rekomendasi Bisnis](#-temuan-strategis--rekomendasi-bisnis)

---

## 🎯 Ringkasan Eksekutif & Visi Proyek

Industri *online food delivery* global beroperasi di tengah dinamika biaya hidup yang kompleks, perang komisi antar platform, serta perilaku konsumen yang sensitif terhadap biaya tersembunyi. Proyek ini membangun **Global Food Delivery Market Intelligence Platform** terpadu yang membedah perilaku harga, efektivitas komisi, strategi promosi, dan inflasi pangan di **10 kota metropolitan dunia**:

* **Amerika Utara**: New York City, Los Angeles (USA - `USD`)
* **Eropa**: London, Manchester (United Kingdom - `GBP`)
* **Asia**: Tokyo, Osaka (Japan - `JPY`), Mumbai, Delhi (India - `INR`)
* **Amerika Selatan**: São Paulo, Rio de Janeiro (Brazil - `BRL`)

### Cakupan Data

* **5.000** Restoran
* **62.417** Item Menu & Nilai Nutrisi
* **18.887** Rekaman Riwayat Perubahan Harga (*Time-Series*)
* **12** Kategori Kuliner (*Cuisines*)

---

## 🏛️ Arsitektur Data & Pipeline Medallion

Proyek ini menerapkan arsitektur data **Decoupled Analytics Serving** standar industri. Komputasi analitik berat (Machine Learning, Regresi OLS, konversi PPP, dan pemrosesan time-series) dieksekusi di *Notebook Layer* dan disimpan sebagai **Gold Data Marts**, yang kemudian disajikan secara instan (*zero latency*) oleh **Streamlit Presentation Layer**.

```text
[ BRONZE LAYER : RAW CSV DATA ]
├── cities.csv, countries.csv, cuisines.csv, delivery_metrics.csv
├── menus.csv, nutrition.csv, price_history.csv, restaurants.csv
└── restaurant_features.csv, restaurant_statistics.csv, city_statistics.csv
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
├── subproject_1_city_price_benchmarks.csv
├── subproject_2_platform_markup_analysis.csv
├── subproject_3_surge_intelligence.csv & subproject_3_city_surge_summary.csv
├── subproject_4_promo_effectiveness.csv & subproject_4_promo_segment_kpi.csv
├── subproject_5_sponsored_roi_analysis.csv & subproject_5_city_ad_benchmark.csv
├── subproject_6_whitespace_analysis.csv & subproject_6_expansion_recommendations.csv
├── subproject_7_membership_impact_analysis.csv & subproject_7_city_membership_summary.csv
└── subproject_8_monthly_city_inflation.csv & subproject_8_city_inflation_kpi.csv
│
▼
[ PLATINUM LAYER : SERVING & DASHBOARD ]
└── Streamlit Enterprise Dashboard (app.py) ──▶ Interactive Plotly BI Cockpit

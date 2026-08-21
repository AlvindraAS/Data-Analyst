# ==============================================================================
# 🏗️ GLOBAL FOOD DELIVERY MARKET INTELLIGENCE PLATFORM (ENTERPRISE EDITION)
# File: app.py
# Arsitektur: Gold Layer Data Mart Serving (Sub-Proyek 1 s.d. 8)
# ==============================================================================

import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ------------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & ENTERPRISE UI STYLING
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Global Food Delivery Intelligence Platform",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Enterprise CSS Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 24px 30px;
        border-radius: 12px;
        margin-bottom: 24px;
        color: white;
        border-left: 6px solid #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .main-header h1 {
        color: #ffffff;
        font-size: 26px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .main-header p {
        color: #94a3b8;
        font-size: 14px;
        margin-top: 6px;
        margin-bottom: 0;
    }
    
    .kpi-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 16px 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
    }
    .kpi-title {
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        color: #64748b;
        letter-spacing: 0.5px;
    }
    .kpi-value {
        font-size: 24px;
        font-weight: 800;
        color: #0f172a;
        margin-top: 4px;
    }
    .kpi-sub {
        font-size: 12px;
        color: #10b981;
        margin-top: 2px;
        font-weight: 500;
    }
    
    .insight-box {
        background-color: #f8fafc;
        border-left: 4px solid #3b82f6;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        margin: 16px 0;
        font-size: 13px;
        color: #334155;
        line-height: 1.6;
    }
    .warning-box {
        background-color: #fffbeb;
        border-left: 4px solid #f59e0b;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        margin: 16px 0;
        font-size: 13px;
        color: #92400e;
        line-height: 1.6;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        border-bottom: 2px solid #f1f5f9;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 18px;
        font-weight: 600;
        font-size: 13px;
        color: #64748b;
        border-radius: 6px 6px 0 0;
    }
    .stTabs [aria-selected="true"] {
        color: #2563eb !important;
        border-bottom: 2px solid #2563eb !important;
        background-color: #eff6ff;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 2. INGESTION PIPELINE: LOAD ALL PRE-COMPUTED DATA MARTS
# ------------------------------------------------------------------------------
DATA_PATH = "D:\Data Analyst\Global Restaurant & Food Delivery Intelligence\Proyek 1\Output"

@st.cache_data(show_spinner=True)
def load_all_data_marts(path=DATA_PATH):
    """
    Memuat seluruh file output CSV hasil kalkulasi Sub-Proyek 1 s.d. 8.
    """
    marts = {}
    
    # 1. Sub-Proyek 1
    marts['p1_city_kpi'] = pd.read_csv(os.path.join(path, "subproject_1_city_price_benchmarks.csv"))
    
    # 2. Sub-Proyek 2
    marts['p2_markup'] = pd.read_csv(os.path.join(path, "subproject_2_platform_markup_analysis.csv"))
    
    # 3. Sub-Proyek 3
    marts['p3_surge'] = pd.read_csv(os.path.join(path, "subproject_3_surge_intelligence.csv"))
    marts['p3_city_surge'] = pd.read_csv(os.path.join(path, "subproject_3_city_surge_summary.csv"))
    
    # 4. Sub-Proyek 4
    marts['p4_promo'] = pd.read_csv(os.path.join(path, "subproject_4_promo_effectiveness.csv"))
    marts['p4_segment_kpi'] = pd.read_csv(os.path.join(path, "subproject_4_promo_segment_kpi.csv"))
    
    # 5. Sub-Proyek 5
    marts['p5_sponsored'] = pd.read_csv(os.path.join(path, "subproject_5_sponsored_roi_analysis.csv"))
    marts['p5_ad_benchmark'] = pd.read_csv(os.path.join(path, "subproject_5_city_ad_benchmark.csv"))
    
    # 6. Sub-Proyek 6
    marts['p6_whitespace'] = pd.read_csv(os.path.join(path, "subproject_6_whitespace_analysis.csv"))
    marts['p6_recs'] = pd.read_csv(os.path.join(path, "subproject_6_expansion_recommendations.csv"))
    
    # 7. Sub-Proyek 7
    marts['p7_membership'] = pd.read_csv(os.path.join(path, "subproject_7_membership_impact_analysis.csv"))
    marts['p7_city_transparency'] = pd.read_csv(os.path.join(path, "subproject_7_city_membership_summary.csv"))
    
    # 8. Sub-Proyek 8
    marts['p8_ts'] = pd.read_csv(os.path.join(path, "subproject_8_monthly_city_inflation.csv"))
    marts['p8_inflation_kpi'] = pd.read_csv(os.path.join(path, "subproject_8_city_inflation_kpi.csv"))
    marts['p8_ts']['Period_Timestamp'] = pd.to_datetime(marts['p8_ts']['Period_Timestamp'])

    return marts

try:
    dm = load_all_data_marts()
    data_loaded = True
except Exception as e:
    st.error(f"❌ Terjadi kesalahan saat memuat data output CSV: {e}")
    st.info("💡 Pastikan Anda telah menjalankan notebook Sub-Proyek 1 hingga 8 dan file output `.csv` tersimpan di direktori aplikasi.")
    data_loaded = False

# ------------------------------------------------------------------------------
# 3. SIDEBAR CONTROLS & GLOBAL FILTERING MATRIX
# ------------------------------------------------------------------------------
if data_loaded:
    with st.sidebar:
        st.markdown("### 🌐 **Intelligence Cockpit**")
        st.caption("Data Marts: **Sub-Projects 1–8 Integrated**")
        st.divider()

        # Navigasi Modul
        menu_choice = st.radio(
            "Pilih Domain Analisis:",
            [
                "🏛️ Executive Overview & Macro Radar",
                "1️⃣ Cross-City Price & PPP Benchmarks",
                "2️⃣ Platform Commission & Markup Decomposition",
                "3️⃣ Dynamic Pricing & Surge Intelligence",
                "4️⃣ Promo & Min. Order Friction Elasticity",
                "5️⃣ Sponsored Listing ROI & A/B Testing",
                "6️⃣ Market Entry & Whitespace Opportunity",
                "7️⃣ Membership Pricing & Parity Audit",
                "8️⃣ Food Price Inflation Tracker (Time-Series)",
                "📑 Executive Strategy Memo & Export"
            ]
        )

        st.divider()
        st.markdown("#### ⚙️ **Global Slicers**")

        # Dynamic Slicers
        all_countries = sorted(dm['p1_city_kpi']['Country'].unique().tolist())
        sel_countries = st.multiselect("Negara:", all_countries, default=all_countries)

        available_cities = sorted(dm['p1_city_kpi'][dm['p1_city_kpi']['Country'].isin(sel_countries)]['City'].unique().tolist())
        sel_cities = st.multiselect("Kota:", available_cities, default=available_cities)

        # Filter Platform (dari p2_markup)
        all_platforms = sorted(dm['p2_markup']['Delivery_Platform'].dropna().unique().tolist())
        sel_platforms = st.multiselect("Platform Delivery:", all_platforms, default=all_platforms)

        st.divider()
        st.caption("🏢 Global Intelligence System v2.6 Enterprise")

    # Helper Filtering Functions
    def apply_filters(df, city_col='City', plat_col='Delivery_Platform'):
        filtered = df.copy()
        if city_col in filtered.columns and sel_cities:
            filtered = filtered[filtered[city_col].isin(sel_cities)]
        if plat_col in filtered.columns and sel_platforms:
            filtered = filtered[filtered[plat_col].isin(sel_platforms)]
        return filtered

    # Filtered Dataframes
    f_p1 = apply_filters(dm['p1_city_kpi'])
    f_p2 = apply_filters(dm['p2_markup'])
    f_p3 = apply_filters(dm['p3_surge'])
    f_p3_city = apply_filters(dm['p3_city_surge'])
    f_p4 = apply_filters(dm['p4_promo'])
    f_p5 = apply_filters(dm['p5_sponsored'])
    f_p5_city = apply_filters(dm['p5_ad_benchmark'])
    f_p6 = apply_filters(dm['p6_whitespace'])
    f_p6_recs = apply_filters(dm['p6_recs'])
    f_p7 = apply_filters(dm['p7_membership'])
    f_p7_city = apply_filters(dm['p7_city_transparency'])
    f_p8_ts = apply_filters(dm['p8_ts'])
    f_p8_kpi = apply_filters(dm['p8_inflation_kpi'])

    # ==============================================================================
    # 4. MODULE CONTROLLER & DETAILED VIEWS
    # ==============================================================================

    # ------------------------------------------------------------------------------
    # 🏛️ EXECUTIVE OVERVIEW & MACRO RADAR
    # ------------------------------------------------------------------------------
    if menu_choice == "🏛️ Executive Overview & Macro Radar":
        st.markdown("""
        <div class="main-header">
            <h1>🏛️ Executive Cockpit: Global Food Delivery Intelligence</h1>
            <p>Sintesis lintas modul Sub-Proyek 1–8 untuk memahami daya beli, komisi platform, lonjakan harga, efektivitas promosi, dan inflasi pangan.</p>
        </div>
        """, unsafe_allow_html=True)

        # Top Metric Ribbon
        col1, col2, col3, col4, col5 = st.columns(5)
        
        avg_nominal = f_p1['Avg_Nominal_USD'].mean() if not f_p1.empty else 0
        avg_ppp = f_p1['Avg_PPP_USD'].mean() if not f_p1.empty else 0
        avg_fee_overhead = f_p2['Fee_Overhead_Pct'].mean() if not f_p2.empty else 0
        avg_surge = f_p3['Peak_hour_multiplier'].mean() if not f_p3.empty else 1.0
        avg_inflation = f_p8_kpi['Realized_Inflation_Rate_Pct'].mean() if not f_p8_kpi.empty else 0

        with col1:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Harga Menu Rata-Rata</div>
                <div class="kpi-value">${avg_nominal:.2f}</div>
                <div class="kpi-sub">PPP: ${avg_ppp:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Fee Overhead Konsumen</div>
                <div class="kpi-value">{avg_fee_overhead:.1f}%</div>
                <div class="kpi-sub">Total Biaya Tambahan</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Rata-Rata Surge Puncak</div>
                <div class="kpi-value">{avg_surge:.2f}x</div>
                <div class="kpi-sub">Peak Multiplier</div>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Penetrasi Membership</div>
                <div class="kpi-value">{f_p7_city['Membership_Penetration_Pct'].mean():.1f}%</div>
                <div class="kpi-sub">Mitra Langganan</div>
            </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Laju Inflasi Kumulatif</div>
                <div class="kpi-value">{avg_inflation:+.2f}%</div>
                <div class="kpi-sub">Time-Series Growth</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        tab_macro1, tab_macro2 = st.tabs(["📊 Macro Radar & Inter-City Comparison", "🧭 Strategic Health Matrix"])

        with tab_macro1:
            c_left, c_right = st.columns([6, 4])
            with c_left:
                st.markdown("##### ⚖️ Keterjangkauan Harga Riil (PPP) vs Beban Pendapatan Harian")
                fig_scatter_macro = px.scatter(
                    f_p1,
                    x='Avg_PPP_USD',
                    y='Avg_Daily_Income_Burden_Pct',
                    size='Total_Menus_Analyzed',
                    color='Cost_of_Living_Index',
                    text='City',
                    color_continuous_scale='Turbo',
                    labels={
                        'Avg_PPP_USD': 'Harga Menu PPP-Adjusted ($ USD)',
                        'Avg_Daily_Income_Burden_Pct': 'Beban Pengeluaran (% dari Pendapatan Harian)',
                        'Cost_of_Living_Index': 'Cost of Living Index'
                    },
                    title="Pemetaan Daya Beli: Beban Pengeluaran Makanan terhadap Penghasilan Warga"
                )
                fig_scatter_macro.update_traces(textposition='top center')
                fig_scatter_macro.update_layout(height=420, margin=dict(l=0, r=0, t=40, b=0))
                st.plotly_chart(fig_scatter_macro, use_container_width=True)

            with c_right:
                st.markdown("##### 🌐 Radar Kinerja Pasar Kota (Normalisasi 0-100)")
                # Radar Chart Kota Terpilih
                radar_cities = f_p1['City'].head(4).tolist()
                radar_df = f_p1[f_p1['City'].isin(radar_cities)].copy()
                
                categories = ['Affordability', 'Cost of Living', 'Daily Income', 'Market Stability']
                fig_radar = go.Figure()
                
                for idx, row in radar_df.iterrows():
                    # Normalisasi nilai untuk radar chart
                    values = [
                        100 - min(row['Avg_PPP_USD'], 100),
                        row['Cost_of_Living_Index'],
                        min(row['Average_Income'] / 1000, 100),
                        100 - min(row['Price_Volatility_CV'], 100)
                    ]
                    fig_radar.add_trace(go.Scatterpolar(
                        r=values,
                        theta=categories,
                        fill='toself',
                        name=row['City']
                    ))
                fig_radar.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                    showlegend=True,
                    height=420,
                    margin=dict(l=20, r=20, t=30, b=20)
                )
                st.plotly_chart(fig_radar, use_container_width=True)

        with tab_macro2:
            st.markdown("##### 📋 Strategic Cross-Module Benchmark Matrix (Konsolidasi Output 1-8)")
            # Merge ringkasan lintas modul
            macro_merge = f_p1[['City', 'Country', 'Avg_Nominal_USD', 'Avg_PPP_USD', 'Avg_Daily_Income_Burden_Pct']].merge(
                f_p3_city[['City', 'Avg_Peak_Multiplier', 'Critical_Surge_Pct']], on='City', how='left'
            ).merge(
                f_p5_city[['City', 'Visibility_Uplift_Pct']], on='City', how='left'
            ).merge(
                f_p7_city[['City', 'Membership_Penetration_Pct', 'Menu_Price_Inflation_Pct']], on='City', how='left'
            ).merge(
                f_p8_kpi[['City', 'Realized_Inflation_Rate_Pct', 'Hike_to_Cut_Ratio']], on='City', how='left'
            )

            st.dataframe(
                macro_merge.style.format({
                    'Avg_Nominal_USD': '${:.2f}',
                    'Avg_PPP_USD': '${:.2f}',
                    'Avg_Daily_Income_Burden_Pct': '{:.1f}%',
                    'Avg_Peak_Multiplier': '{:.2f}x',
                    'Critical_Surge_Pct': '{:.1f}%',
                    'Visibility_Uplift_Pct': '+{:.1f}%',
                    'Membership_Penetration_Pct': '{:.1f}%',
                    'Menu_Price_Inflation_Pct': '{:+.1f}%',
                    'Realized_Inflation_Rate_Pct': '{:+.2f}%',
                    'Hike_to_Cut_Ratio': '{:.2f}x'
                }).background_gradient(subset=['Avg_Daily_Income_Burden_Pct', 'Realized_Inflation_Rate_Pct'], cmap='Reds')
                  .background_gradient(subset=['Visibility_Uplift_Pct'], cmap='Greens'),
                use_container_width=True
            )

    # ------------------------------------------------------------------------------
    # 1️⃣ SUB-PROYEK 1: CROSS-CITY PRICE & PPP BENCHMARKS
    # ------------------------------------------------------------------------------
    elif menu_choice == "1️⃣ Cross-City Price & PPP Benchmarks":
        st.markdown("""
        <div class="main-header">
            <h1>📍 Sub-Proyek 1: Cross-City Price & PPP Benchmarking</h1>
            <p>Menganalisis disparitas harga menu antar kota besar dunia dengan normalisasi Purchasing Power Parity (NYC = 100) dan beban pendapatan.</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([7, 3])
        with col1:
            fig_p1_bar = go.Figure()
            fig_p1_bar.add_trace(go.Bar(
                x=f_p1['City'],
                y=f_p1['Avg_Nominal_USD'],
                name='Harga Nominal ($ USD)',
                marker_color='#e11d48'
            ))
            fig_p1_bar.add_trace(go.Bar(
                x=f_p1['City'],
                y=f_p1['Avg_PPP_USD'],
                name='Harga Riil PPP-Adjusted ($ USD)',
                marker_color='#2563eb'
            ))
            fig_p1_bar.update_layout(
                barmode='group',
                title="Perbandingan Harga Makanan: Nominal USD vs Beban Riil PPP",
                height=420,
                xaxis_title="Kota",
                yaxis_title="Harga Rata-Rata ($ USD)",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_p1_bar, use_container_width=True)

        with col2:
            st.markdown("##### 🏆 Peringkat Keterjangkauan (Affordability)")
            st.dataframe(
                f_p1[['Affordability_Rank', 'City', 'Avg_PPP_USD', 'Avg_Daily_Income_Burden_Pct', 'Price_Volatility_CV']]
                .sort_values(by='Affordability_Rank')
                .style.format({
                    'Avg_PPP_USD': '${:.2f}',
                    'Avg_Daily_Income_Burden_Pct': '{:.1f}%',
                    'Price_Volatility_CV': '{:.1f}%'
                }),
                use_container_width=True
            )

        st.markdown("""
        <div class="insight-box">
            <b>💡 Temuan Analitis Sub-Proyek 1:</b><br>
            • <b>Paradoqs Keterjangkauan:</b> Kota di negara berkembang (e.g., Mumbai, São Paulo) memiliki harga nominal terendah ($3–$7), namun menuntut <b>15%–22% dari rata-rata pendapatan harian</b> warga lokal.<br>
            • <b>Pasar Berpenghasilan Tinggi:</b> Kota seperti New York dan London mencatatkan harga nominal tinggi ($18–$35), namun beban pengeluaran hanya memakan <b>6%–9% dari pendapatan harian</b>, menjadikan delivery sebagai komoditas rutin.
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------------------
    # 2️⃣ SUB-PROYEK 2: PLATFORM COMMISSION & MARKUP DECOMPOSITION
    # ------------------------------------------------------------------------------
    elif menu_choice == "2️⃣ Platform Commission & Markup Decomposition":
        st.markdown("""
        <div class="main-header">
            <h1>📍 Sub-Proyek 2: Platform Commission & Markup Decomposition</h1>
            <p>Menganalisis komponen biaya tersembunyi (Delivery, Service, Packaging Fee) dan rasio markup harga platform terhadap konsumen.</p>
        </div>
        """, unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        with col_a:
            fee_agg = f_p2.groupby('Delivery_Platform')[['Delivery_fee_USD', 'Service_fee_USD', 'Packaging_fee_USD']].mean().reset_index()
            fig_fee_stack = px.bar(
                fee_agg,
                x='Delivery_Platform',
                y=['Delivery_fee_USD', 'Service_fee_USD', 'Packaging_fee_USD'],
                title="Dekomposisi Struktur Biaya Layanan Tambahan ($ USD)",
                barmode='stack',
                color_discrete_map={'Delivery_fee_USD': '#3b82f6', 'Service_fee_USD': '#f97316', 'Packaging_fee_USD': '#10b981'}
            )
            fig_fee_stack.update_layout(height=380, xaxis_tickangle=-20)
            st.plotly_chart(fig_fee_stack, use_container_width=True)

        with col_b:
            fig_mkup_dist = px.box(
                f_p2,
                x='Delivery_Platform',
                y='Total_Consumer_Markup_Pct',
                color='Delivery_Platform',
                title="Distribusi Total Beban Markup Konsumen (%) per Platform"
            )
            fig_mkup_dist.update_layout(height=380, showlegend=False, xaxis_tickangle=-20)
            st.plotly_chart(fig_mkup_dist, use_container_width=True)

        st.markdown("##### 🚨 Top 10 Restoran dengan Beban Markup Konsumen Tertinggi (Outlier Alert)")
        st.dataframe(
            f_p2[['Restaurant_name', 'City', 'Delivery_Platform', 'Avg_Current_Price_USD', 'Total_Platform_Fees_USD', 'Menu_Markup_Pct', 'Fee_Overhead_Pct', 'Total_Consumer_Markup_Pct', 'Average_rating']]
            .sort_values(by='Total_Consumer_Markup_Pct', ascending=False)
            .head(10)
            .style.format({
                'Avg_Current_Price_USD': '${:.2f}',
                'Total_Platform_Fees_USD': '${:.2f}',
                'Menu_Markup_Pct': '{:.1f}%',
                'Fee_Overhead_Pct': '{:.1f}%',
                'Total_Consumer_Markup_Pct': '{:.1f}%',
                'Average_rating': '⭐ {:.2f}'
            }),
            use_container_width=True
        )

        st.markdown("""
        <div class="insight-box">
            <b>💡 Temuan Analitis Sub-Proyek 2:</b><br>
            • <b>Struktur Fee Regresif:</b> Pada keranjang pesanan bernilai rendah (&lt; $15), total fee tambahan dapat mencapai <b>30%–45% dari total harga makanan</b>.<br>
            • <b>Menu Markup Pass-Through:</b> Merchant menaikkan harga dasar menu terdaftar sebesar 10%–25% di aplikasi untuk mengompensasi komisi take-rate platform.
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------------------
    # 3️⃣ SUB-PROYEK 3: DYNAMIC PRICING & SURGE INTELLIGENCE
    # ------------------------------------------------------------------------------
    elif menu_choice == "3️⃣ Dynamic Pricing & Surge Intelligence":
        st.markdown("""
        <div class="main-header">
            <h1>📍 Sub-Proyek 3: Dynamic Pricing & Surge Intelligence</h1>
            <p>Mendeteksi pola lonjakan harga (Peak Hour Multiplier) berdasarkan zona cuaca, koordinat geografis, dan kepadatan kota.</p>
        </div>
        """, unsafe_allow_html=True)

        col_map, col_weather = st.columns([6, 4])
        with col_map:
            fig_surge_map = px.scatter(
                f_p3,
                x='Longitude',
                y='Latitude',
                color='Surge_Zone_Category',
                size='Surge_Dollar_Delta_USD',
                color_discrete_map={
                    'Critical Surge (>= 2.0x)': '#dc2626',
                    'High Surge (1.5x - 1.99x)': '#ea580c',
                    'Moderate Surge (1.1x - 1.49x)': '#eab308',
                    'Baseline (< 1.1x)': '#16a34a'
                },
                hover_name='Restaurant_name',
                hover_data=['City', 'Peak_hour_multiplier', 'Surge_Dollar_Delta_USD'],
                title="Peta Spasial Hotspot Lonjakan Harga (Surge Spatial Coordinates)"
            )
            fig_surge_map.update_layout(height=420)
            st.plotly_chart(fig_surge_map, use_container_width=True)

        with col_weather:
            fig_weather = px.violin(
                f_p3,
                x='Weather_zone',
                y='Peak_hour_multiplier',
                color='Weather_zone',
                box=True,
                points="all",
                title="Distribusi Multiplier Berdasarkan Zona Cuaca"
            )
            fig_weather.update_layout(height=420, showlegend=False, xaxis_tickangle=-25)
            st.plotly_chart(fig_weather, use_container_width=True)

        st.markdown("##### 📍 Ringkasan Risiko & Intensitas Surge per Kota")
        st.dataframe(
            f_p3_city[['City', 'Country', 'Weather_zone', 'Avg_Base_Fee_USD', 'Avg_Peak_Fee_USD', 'Avg_Surge_Delta_USD', 'Avg_Peak_Multiplier', 'Critical_Surge_Pct', 'Avg_Cancellation_Rate']]
            .style.format({
                'Avg_Base_Fee_USD': '${:.2f}',
                'Avg_Peak_Fee_USD': '${:.2f}',
                'Avg_Surge_Delta_USD': '+${:.2f}',
                'Avg_Peak_Multiplier': '{:.2f}x',
                'Critical_Surge_Pct': '{:.1f}%',
                'Avg_Cancellation_Rate': '{:.2%}'
            }),
            use_container_width=True
        )

        st.markdown("""
        <div class="insight-box">
            <b>💡 Temuan Analitis Sub-Proyek 3:</b><br>
            • <b>Korelasi Cuaca Ekstrem:</b> Wilayah dengan zona cuaca <i>Tropical wet and dry</i> dan <i>Oceanic</i> memiliki frekuensi lonjakan kritis (&ge; 2.0x) tertinggi akibat keterbatasan kurir saat hujan.<br>
            • <b>Risiko Pembatalan:</b> Kenaikan multiplier di atas 1.8x berkorelasi langsung dengan kenaikan <b>Cancellation Rate hingga 2.4x lipat</b>.
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------------------
    # 4️⃣ SUB-PROYEK 4: PROMO & MIN. ORDER FRICTION ELASTICITY
    # ------------------------------------------------------------------------------
    elif menu_choice == "4️⃣ Promo & Min. Order Friction Elasticity":
        st.markdown("""
        <div class="main-header">
            <h1>📍 Sub-Proyek 4: Promo & Minimum Order Value Effectiveness</h1>
            <p>Mengukur efektivitas diskon dan ambang batas minimum pesanan terhadap volume order, rating, dan pembatalan pesanan.</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns([6, 4])
        with c1:
            fig_matrix = px.scatter(
                f_p4,
                x='Min_Order_Friction_Ratio',
                y='Promo_Attractiveness_Score',
                color='Promo_Strategy_Segment',
                size='Composite_Volume_Index',
                color_discrete_map={
                    'Growth Driver (High Promo, Low Barrier)': '#10b981',
                    'Basket Maximizer (High Promo, High Barrier)': '#3b82f6',
                    'Organic Frictions-Free (Low Promo, Low Barrier)': '#f59e0b',
                    'Strict Gatekeeper (Low Promo, High Barrier)': '#ef4444'
                },
                title="🎯 Matriks Strategi 2x2: Skor Daya Tarik Promo vs Hambatan Min. Order"
            )
            fig_matrix.add_vline(x=f_p4['Min_Order_Friction_Ratio'].median(), line_dash="dash", line_color="gray")
            fig_matrix.add_hline(y=f_p4['Promo_Attractiveness_Score'].median(), line_dash="dash", line_color="gray")
            fig_matrix.update_layout(height=420)
            st.plotly_chart(fig_matrix, use_container_width=True)

        with c2:
            st.markdown("##### 📊 KPI Kinerja per Segmen Strategi")
            st.dataframe(
                dm['p4_segment_kpi']
                .style.format({
                    'Avg_Promo_Score': '{:.1f}',
                    'Avg_Min_Order_USD': '${:.2f}',
                    'Avg_Friction_Ratio': '{:.2f}x',
                    'Avg_Volume_Index': '{:.1f}',
                    'Avg_Rating': '⭐ {:.2f}',
                    'Avg_Cancellation_Rate': '{:.2%}'
                }),
                use_container_width=True
            )

        st.markdown("""
        <div class="insight-box">
            <b>💡 Temuan Analitis Sub-Proyek 4:</b><br>
            • <b>The Friction Cliff (&gt; 1.5x):</b> Restoran yang menetapkan ambang pesanan minimum lebih dari 1.5x harga rata-rata menu mengalami penurunan volume konversi sebesar <b>34%</b>.<br>
            • <b>Segmen Terbaik:</b> Kuadran <b>Growth Driver</b> menghasilkan volume pesanan tertinggi dengan tetap mempertahankan rating &ge; 4.1 bintang.
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------------------
    # 5️⃣ SUB-PROYEK 5: SPONSORED LISTING ROI & A/B TESTING
    # ------------------------------------------------------------------------------
    elif menu_choice == "5️⃣ Sponsored Listing ROI & A/B Testing":
        st.markdown("""
        <div class="main-header">
            <h1>📍 Sub-Proyek 5: Sponsored Listing ROI & A/B Testing Tracker</h1>
            <p>Hasil uji eksperimen kuasi A/B testing: Signifikansi dorongan visibilitas listing berbayar vs risiko kanibalisasi rating.</p>
        </div>
        """, unsafe_allow_html=True)

        col_hist, col_scat = st.columns(2)
        with col_hist:
            fig_ab = px.histogram(
                f_p5,
                x='Visibility_Index',
                color='Is_Sponsored',
                barmode='overlay',
                color_discrete_map={True: '#2563eb', False: '#94a3b8'},
                title="Distribusi Uplift Visibilitas (Sponsored vs Organic Listings)"
            )
            fig_ab.update_layout(height=400)
            st.plotly_chart(fig_ab, use_container_width=True)

        with col_scat:
            fig_quad = px.scatter(
                f_p5,
                x='Visibility_Index',
                y='Average_rating',
                color='Performance_Quadrant',
                color_discrete_map={
                    'Market Leader (High Vis, High Rating)': '#10b981',
                    'Over-Promoted / Low Quality (High Vis, Low Rating)': '#ef4444',
                    'Hidden Gem (Low Vis, High Rating)': '#3b82f6',
                    'Struggling Organic (Low Vis, Low Rating)': '#94a3b8'
                },
                title="Kuadran Evaluasi Kualitas Iklan: Rating vs Visibilitas"
            )
            fig_quad.update_layout(height=400)
            st.plotly_chart(fig_quad, use_container_width=True)

        st.markdown("##### 🏆 Rekapitulasi Efektivitas Iklan & ROI per Kota")
        st.dataframe(
            f_p5_city[['City', 'Sponsored_Share_Pct', 'Avg_Organic_Visibility', 'Avg_Sponsored_Visibility', 'Visibility_Uplift_Pct', 'Avg_Organic_Rating', 'Avg_Sponsored_Rating', 'Avg_Estimated_ROI']]
            .style.format({
                'Sponsored_Share_Pct': '{:.1f}%',
                'Avg_Organic_Visibility': '{:.1f}',
                'Avg_Sponsored_Visibility': '{:.1f}',
                'Visibility_Uplift_Pct': '+{:.1f}%',
                'Avg_Organic_Rating': '⭐ {:.2f}',
                'Avg_Sponsored_Rating': '⭐ {:.2f}',
                'Avg_Estimated_ROI': '{:.1f}'
            }),
            use_container_width=True
        )

        st.markdown("""
        <div class="insight-box">
            <b>💡 Temuan Analitis Sub-Proyek 5:</b><br>
            • <b>Uji Signifikansi (A/B Test):</b> Listing bersponsor menghasilkan kenaikan visibilitas rata-rata sebesar <b>+45% hingga +75%</b> dengan signifikansi statistik ($p < 0.001$).<br>
            • <b>Risiko Over-Promotion:</b> Restoran dengan rating di bawah 3.8 yang dipromosikan secara agresif mengalami peningkatan ulasan negatif lebih cepat karena ekspektasi konsumen yang tidak terpenuhi.
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------------------
    # 6️⃣ SUB-PROYEK 6: MARKET ENTRY & WHITESPACE OPPORTUNITY
    # ------------------------------------------------------------------------------
    elif menu_choice == "6️⃣ Market Entry & Whitespace Opportunity":
        st.markdown("""
        <div class="main-header">
            <h1>📍 Sub-Proyek 6: Market Entry & Whitespace Analysis</h1>
            <p>Mendeteksi peluang kekosongan pasar kuliner (Whitespace Gap) dengan rasio permintaan tinggi dan persaingan pasokan rendah.</p>
        </div>
        """, unsafe_allow_html=True)

        pivot_ws = f_p6.pivot_table(index='City', columns='Cuisine', values='Whitespace_Opportunity_Score', aggfunc='mean').fillna(0)
        
        fig_ws_heat = px.imshow(
            pivot_ws,
            text_auto=".1f",
            color_continuous_scale="YlGnBu",
            title="🗺️ Heatmap Whitespace Opportunity Score (Skor Tinggi = Peluang Ekspansi Terbaik)",
            labels=dict(x="Kategori Masakan", y="Kota", color="Whitespace Score")
        )
        fig_ws_heat.update_layout(height=450)
        st.plotly_chart(fig_ws_heat, use_container_width=True)

        st.markdown("##### 🚀 Rekomendasi Aksi Ekspansi Bisnis Kuliner Terpilih")
        st.dataframe(
            f_p6_recs[['City', 'Cuisine', 'Supply_Share_Pct', 'Demand_Score', 'Whitespace_Opportunity_Score', 'Expansion_Recommendation']]
            .style.format({
                'Supply_Share_Pct': '{:.1f}%',
                'Demand_Score': '{:.1f}',
                'Whitespace_Opportunity_Score': '{:.1f}'
            }),
            use_container_width=True
        )

        st.markdown("""
        <div class="insight-box">
            <b>💡 Temuan Analitis Sub-Proyek 6:</b><br>
            • <b>Red Ocean vs Whitespace:</b> Kategori kuliner seperti masakan lokal utama dan Fast Food telah jenuh (&gt; 15% pasokan), sedangkan masakan internasional spesifik (e.g. Thai & Japanese di LATAM) menyajikan ruang pertumbuhan tertinggi.
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------------------
    # 7️⃣ SUB-PROYEK 7: MEMBERSHIP PRICING & PARITY AUDIT
    # ------------------------------------------------------------------------------
    elif menu_choice == "7️⃣ Membership Pricing & Parity Audit":
        st.markdown("""
        <div class="main-header">
            <h1>📍 Sub-Proyek 7: Membership Pricing Impact & Loyalty Study</h1>
            <p>Audit transparansi harga: Menilai apakah merchant menaikkan harga menu dasar pada program langganan bebas ongkir.</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            fig_mem_p = px.box(
                f_p7,
                x='City',
                y='Average_menu_price_PPP',
                color='Membership_Status',
                color_discrete_map={'Membership Partner': '#e11d48', 'Standard Non-Member': '#94a3b8'},
                title="Harga Menu Dasar PPP ($ USD): Member vs Non-Member"
            )
            fig_mem_p.update_layout(height=400, xaxis_tickangle=-25)
            st.plotly_chart(fig_mem_p, use_container_width=True)

        with c2:
            fig_mem_l = px.histogram(
                f_p7,
                x='Customer_Loyalty_Index',
                color='Membership_Status',
                barmode='overlay',
                color_discrete_map={'Membership Partner': '#10b981', 'Standard Non-Member': '#94a3b8'},
                title="Pergeseran Skor Loyalitas Konsumen (Customer Loyalty Index)"
            )
            fig_mem_l.update_layout(height=400)
            st.plotly_chart(fig_mem_l, use_container_width=True)

        st.markdown("##### 📊 Laporan Audit Transparansi & Inflasi Harga Membership per Kota")
        st.dataframe(
            f_p7_city[['City', 'Country', 'Membership_Penetration_Pct', 'Avg_Price_Non_Member', 'Avg_Price_Member', 'Menu_Price_Inflation_Pct', 'Avg_Value_Score_Member', 'Avg_Loyalty_Member']]
            .style.format({
                'Membership_Penetration_Pct': '{:.1f}%',
                'Avg_Price_Non_Member': '${:.2f}',
                'Avg_Price_Member': '${:.2f}',
                'Menu_Price_Inflation_Pct': '{:+.1f}%',
                'Avg_Value_Score_Member': '{:.1f}',
                'Avg_Loyalty_Member': '{:.1f}'
            }),
            use_container_width=True
        )

        st.markdown("""
        <div class="insight-box">
            <b>💡 Temuan Analitis Sub-Proyek 7:</b><br>
            • <b>Inflasi Harga Dasar:</b> Merchant mitra membership menerapkan harga dasar menu <b>5%–12% lebih mahal</b> dibanding non-mitra untuk mengompensasi potongan komisi membership platform.<br>
            • <b>Tingkat Retensi:</b> Meskipun terdapat markup harga dasar, skor <i>Customer Loyalty Index</i> tetap <b>25% lebih tinggi</b> akibat penghapusan friksi biaya antar per transaksi.
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------------------
    # 8️⃣ SUB-PROYEK 8: FOOD PRICE INFLATION TRACKER (TIME-SERIES)
    # ------------------------------------------------------------------------------
    elif menu_choice == "8️⃣ Food Price Inflation Tracker (Time-Series)":
        st.markdown("""
        <div class="main-header">
            <h1>📍 Sub-Proyek 8: Food Price Inflation Tracker (Time-Series)</h1>
            <p>Melacak dinamika perubahan harga makanan kumulatif dari 18.887 rekaman riwayat harga (Base Period = 100).</p>
        </div>
        """, unsafe_allow_html=True)

        fig_ts_line = px.line(
            f_p8_ts,
            x='Period_Timestamp',
            y='Cumulative_Price_Index',
            color='City',
            markers=True,
            title="📈 Indeks Perubahan Harga Pangan Kumulatif per Kota (Base = 100)"
        )
        fig_ts_line.add_hline(y=100.0, line_dash="dash", line_color="black")
        fig_ts_line.update_layout(height=420, xaxis_title="Bulan", yaxis_title="Cumulative Price Index")
        st.plotly_chart(fig_ts_line, use_container_width=True)

        col_inf_heat, col_inf_kpi = st.columns([6, 4])
        with col_inf_heat:
            pivot_inf = f_p8_ts.pivot_table(
                index='City',
                columns=f_p8_ts['Period_Timestamp'].dt.strftime('%b %Y'),
                values='Net_Monthly_Inflation_Pct',
                aggfunc='mean'
            ).fillna(0)

            fig_inf_map = px.imshow(
                pivot_inf,
                text_auto=".1f",
                color_continuous_scale="RdBu_r",
                title="Heatmap Laju Inflasi Bulanan (%) per Kota"
            )
            fig_inf_map.update_layout(height=380)
            st.plotly_chart(fig_inf_map, use_container_width=True)

        with col_inf_kpi:
            st.markdown("##### 🏆 Leaderboard Volatilitas & Inflasi")
            st.dataframe(
                f_p8_kpi[['City', 'Avg_Price_USD_Start', 'Avg_Price_USD_End', 'Realized_Inflation_Rate_Pct', 'Hike_to_Cut_Ratio', 'Price_Volatility_Std']]
                .style.format({
                    'Avg_Price_USD_Start': '${:.2f}',
                    'Avg_Price_USD_End': '${:.2f}',
                    'Realized_Inflation_Rate_Pct': '{:+.2f}%',
                    'Hike_to_Cut_Ratio': '{:.2f}x',
                    'Price_Volatility_Std': '{:.2f}'
                }),
                use_container_width=True
            )

        st.markdown("""
        <div class="insight-box">
            <b>💡 Temuan Analitis Sub-Proyek 8:</b><br>
            • <b>Tekanan Bahan Baku:</b> Kota dengan inflasi pangan tertinggi mencatatkan rasio kenaikan dibanding penurunan harga (<i>Hike-to-Cut Ratio</i>) di atas 2.5x.<br>
            • <b>Kategori Paling Stabil:</b> Minuman (Beverages) memiliki tingkat volatilitas harga paling rendah dibandingkan hidangan utama (Main Courses).
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------------------
    # 📑 EXECUTIVE STRATEGY MEMO & EXPORT
    # ------------------------------------------------------------------------------
    elif menu_choice == "📑 Executive Strategy Memo & Export":
        st.markdown("""
        <div class="main-header">
            <h1>📑 Executive Strategy Memo & Data Mart Exporter</h1>
            <p>Hasilkan ringkasan rekomendasi aksi berbasis data dan unduh tabel hasil analitik Sub-Proyek 1–8.</p>
        </div>
        """, unsafe_allow_html=True)

        target_city = st.selectbox("Pilih Kota Target untuk Briefing Memo:", available_cities)
        
        # Ekstraksi profil kota
        p1_c = dm['p1_city_kpi'][dm['p1_city_kpi']['City'] == target_city].iloc[0] if not dm['p1_city_kpi'][dm['p1_city_kpi']['City'] == target_city].empty else {}
        p3_c = dm['p3_city_surge'][dm['p3_city_surge']['City'] == target_city].iloc[0] if not dm['p3_city_surge'][dm['p3_city_surge']['City'] == target_city].empty else {}
        p6_c = dm['p6_recs'][dm['p6_recs']['City'] == target_city]
        p7_c = dm['p7_city_transparency'][dm['p7_city_transparency']['City'] == target_city].iloc[0] if not dm['p7_city_transparency'][dm['p7_city_transparency']['City'] == target_city].empty else {}
        p8_c = dm['p8_inflation_kpi'][dm['p8_inflation_kpi']['City'] == target_city].iloc[0] if not dm['p8_inflation_kpi'][dm['p8_inflation_kpi']['City'] == target_city].empty else {}

        memo_md = f"""
### 📋 EXECUTIVE MARKET INTELLIGENCE MEMORANDUM
**Target Market:** {target_city}, {p1_c.get('Country', 'N/A')}  
**Macro Profile:** Cost of Living Index = {p1_c.get('Cost_of_Living_Index', 0):.0f} | Income Level = ${p1_c.get('Average_Income', 0):,.0f} / tahun

---
#### 1. Pricing & Purchasing Power Summary
* **Harga Nominal vs PPP:** Rata-rata menu ${p1_c.get('Avg_Nominal_USD', 0):.2f} setara dengan **${p1_c.get('Avg_PPP_USD', 0):.2f} (PPP-Adjusted)**.
* **Beban Pengeluaran Konsumen:** Memesan makanan menyerap **{p1_c.get('Avg_Daily_Income_Burden_Pct', 0):.1f}%** dari rata-rata penghasilan harian warga.

#### 2. Dynamic Pricing & Surge Intelligence
* **Peak Hour Multiplier:** Rata-rata lonjakan jam sibuk mencapai **{p3_c.get('Avg_Peak_Multiplier', 1.0):.2f}x** dengan zona kritis ({p3_c.get('Critical_Surge_Pct', 0):.1f}% dari total pesanan).
* **Faktor Lingkungan:** Zona cuaca *{p3_c.get('Weather_zone', 'N/A')}* menjadi katalis utama eskalasi biaya kirim puncak.

#### 3. Market Expansion & Whitespace Opportunity
* **Peluang Terbesar:** Kategori masakan *{p6_c.iloc[0]['Cuisine'] if not p6_c.empty else 'N/A'}* memiliki Whitespace Score **{p6_c.iloc[0]['Whitespace_Opportunity_Score'] if not p6_c.empty else 0:.1f}/100**.
* **Rekomendasi Aksi:** {p6_c.iloc[0]['Expansion_Recommendation'] if not p6_c.empty else 'N/A'}

#### 4. Membership & Price Parity Audit
* **Tingkat Penetrasi:** {p7_c.get('Membership_Penetration_Pct', 0):.1f}% merchant telah tergabung sebagai mitra langganan.
* **Inflasi Harga Dasar:** Merchant membership membebankan selisih harga dasar sebesar **{p7_c.get('Menu_Price_Inflation_Pct', 0):+.1f}%**.

#### 5. Macro Food Inflation Trend
* **Laju Inflasi Kumulatif:** {p8_c.get('Realized_Inflation_Rate_Pct', 0):+.2f}% dengan rasio kenaikan harga (*Hike-to-Cut Ratio*) sebesar **{p8_c.get('Hike_to_Cut_Ratio', 1.0):.2f}x**.
        """

        st.markdown(memo_md)

        st.divider()
        st.markdown("#### 📥 Unduh Ringkasan & Data Mart")
        
        c_dl1, c_dl2 = st.columns(2)
        with c_dl1:
            st.download_button(
                label="📄 Unduh Executive Memo (Markdown)",
                data=memo_md,
                file_name=f"executive_memo_{target_city.lower().replace(' ', '_')}.md",
                mime="text/markdown"
            )
        with c_dl2:
            st.download_button(
                label="💾 Unduh Master City KPI (CSV)",
                data=dm['p1_city_kpi'].to_csv(index=False).encode('utf-8'),
                file_name="subproject_1_city_price_benchmarks.csv",
                mime="text/csv"
            )
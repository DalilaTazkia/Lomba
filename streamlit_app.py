import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(
    page_title="BPS Digital",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Data contoh (mock data)
@st.cache_data
def load_data():
    data = {
        "Tahun": [2018, 2019, 2020, 2021, 2022],
        "PDRB (Triliun Rupiah)": [1500, 1600, 1650, 1700, 1800],
        "Inflasi (%)": [3.2, 2.8, 1.6, 1.9, 2.5],
        "Pengangguran (Juta)": [7.0, 6.8, 9.3, 8.5, 7.9],
        "Ekspor (Miliar USD)": [180, 168, 163, 192, 232],
        "Impor (Miliar USD)": [188, 173, 156, 177, 210]
    }
    return pd.DataFrame(data)

df = load_data()

# CSS untuk styling
st.markdown("""
<style>
    .header {
        font-size: 24px;
        font-weight: bold;
        color: #0066cc;
        padding: 10px;
        border-bottom: 2px solid #0066cc;
    }
    .subheader {
        font-size: 18px;
        font-weight: bold;
        color: #0066cc;
        margin-top: 20px;
    }
    .metric-box {
        background-color: #f0f8ff;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .footer {
        margin-top: 50px;
        padding: 10px;
        background-color: #f5f5f5;
        text-align: center;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://www.bps.go.id/assets/img/logo.png", width=100)
with col2:
    st.markdown("<div class='header'>BADAN PUSAT STATISTIK REPUBLIK INDONESIA</div>", unsafe_allow_html=True)
    st.markdown("**Satu Data untuk Indonesia**")

# Menu utama
menu = st.sidebar.selectbox("MENU UTAMA", [
    "Beranda", 
    "Statistik", 
    "Publikasi", 
    "Tabel Dinamis",
    "Tentang Kami"
])

if menu == "Beranda":
    st.markdown("""
    ## Selamat Datang di Portal BPS Digital
    
    Portal ini menyajikan berbagai data statistik resmi yang diproduksi oleh Badan Pusat Statistik.
    """)
    
    # Highlight indikator
    st.markdown("<div class='subheader'>INDIKATOR UTAMA</div>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    with cols[0]:
        st.markdown("<div class='metric-box'>" +
                    "<div>PDRB 2022</div>" +
                    f"<div style='font-size:24px; font-weight:bold;'>Rp {df.loc[4, 'PDRB (Triliun Rupiah)']} T</div>" +
                    "</div>", unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("<div class='metric-box'>" +
                    "<div>Inflasi 2022</div>" +
                    f"<div style='font-size:24px; font-weight:bold;'>{df.loc[4, 'Inflasi (%)']}%</div>" +
                    "</div>", unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("<div class='metric-box'>" +
                    "<div>Pengangguran 2022</div>" +
                    f"<div style='font-size:24px; font-weight:bold;'>{df.loc[4, 'Pengangguran (Juta)']} Juta</div>" +
                    "</div>", unsafe_allow_html=True)
    
    with cols[3]:
        st.markdown("<div class='metric-box'>" +
                    "<div>Ekspor 2022</div>" +
                    f"<div style='font-size:24px; font-weight:bold;'>${df.loc[4, 'Ekspor (Miliar USD)']} M</div>" +
                    "</div>", unsafe_allow_html=True)
    
    # Grafik tren
    st.markdown("<div class='subheader'>TREN EKONOMI 5 TAHUN TERAKHIR</div>", unsafe_allow_html=True)
    
    selected_indicator = st.selectbox("Pilih Indikator:", df.columns[1:])
    fig = px.line(df, x="Tahun", y=selected_indicator, 
                  title=f"Perkembangan {selected_indicator} 2018-2022",
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Statistik":
    st.markdown("<div class='subheader'>DATA STATISTIK</div>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Tabel Data", "Visualisasi", "Unduh Data"])
    
    with tab1:
        st.dataframe(df, use_container_width=True)
    
    with tab2:
        chart_type = st.selectbox("Jenis Visualisasi:", 
                                ["Line Chart", "Bar Chart", "Scatter Plot"])
        
        x_axis = st.selectbox("Sumbu X:", df.columns)
        y_axis = st.selectbox("Sumbu Y:", df.columns[1:], index=1)
        
        if chart_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis)
        elif chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis)
        else:
            fig = px.scatter(df, x=x_axis, y=y_axis)
            
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("**Unduh Data Statistik**")
        st.download_button(
            label="Unduh sebagai CSV",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name='data_statistik_bps.csv',
            mime='text/csv'
        )

elif menu == "Publikasi":
    st.markdown("<div class='subheader'>PUBLIKASI RESMI</div>", unsafe_allow_html=True)
    
    pub_data = {
        "Judul Publikasi": [
            "Statistik Indonesia 2022",
            "Indikator Pasar Tenaga Kerja 2022",
            "Perkembangan Ekspor Impor 2022",
            "Statistik Kesejahteraan Rakyat 2021"
        ],
        "Tahun": [2022, 2022, 2022, 2021],
        "Kategori": ["Umum", "Tenaga Kerja", "Perdagangan", "Sosial"],
        "Link": ["#", "#", "#", "#"]
    }
    pub_df = pd.DataFrame(pub_data)
    
    st.dataframe(
        pub_df,
        column_config={
            "Link": st.column_config.LinkColumn("Unduh")
        },
        hide_index=True,
        use_container_width=True
    )

elif menu == "Tabel Dinamis":
    st.markdown("<div class='subheader'>TABEL DINAMIS</div>", unsafe_allow_html=True)
    
    st.markdown("""
    Fitur ini memungkinkan Anda untuk membuat tabel statistik custom sesuai kebutuhan.
    """)
    
    selected_columns = st.multiselect(
        "Pilih Kolom Data:",
        df.columns,
        default=["Tahun", "PDRB (Triliun Rupiah)", "Inflasi (%)"]
    )
    
    if selected_columns:
        st.dataframe(df[selected_columns], use_container_width=True)
    else:
        st.warning("Silakan pilih minimal satu kolom")

elif menu == "Tentang Kami":
    st.markdown("<div class='subheader'>TENTANG BPS DIGITAL</div>", unsafe_allow_html=True)
    
    st.markdown("""
    **Badan Pusat Statistik (BPS)** adalah Lembaga Pemerintah Non Kementerian 
    yang bertanggung jawab langsung kepada Presiden.
    
    **Tugas Pokok:**
    - Melaksanakan tugas pemerintahan di bidang statistik
    - Menyediakan data statistik berkualitas
    - Mengembangkan sistem statistik nasional
    
    **Kontak:**
    - Email: bpshq@bps.go.id
    - Telepon: (021) 3841195
    - Alamat: Jl. Dr. Sutomo 6-8 Jakarta 10710 Indonesia
    """)

# Footer
st.markdown("""
<div class='footer'>
    © 2023 Badan Pusat Statistik Republik Indonesia<br>
    Seluruh data yang disajikan merupakan data resmi yang dipublikasikan oleh BPS
</div>
""", unsafe_allow_html=True)

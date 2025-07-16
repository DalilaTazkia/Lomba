import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Statistik - BPS",
    page_icon="📊",
    layout="wide"
)

# CSS untuk styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .header {
        color: #0066cc;
        font-size: 24px;
        font-weight: bold;
    }
    .subheader {
        color: #0066cc;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.image("https://www.bps.go.id/assets/img/logo.png", width=150)
st.title("Badan Pusat Statistik Republik Indonesia")
st.markdown("---")

# Menu sidebar
with st.sidebar:
    st.header("Menu")
    menu_option = st.selectbox(
        "Pilih Kategori Data",
        ["Ekonomi", "Sosial", "Pertanian", "Perdagangan", "Lainnya"]
    )
    tahun = st.slider("Pilih Tahun", 2010, 2023, 2023)

# Konten utama berdasarkan menu
if menu_option == "Ekonomi":
    st.header("Data Ekonomi")
    data = {
        "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"],
        "Inflasi (%)": [2.5, 2.7, 2.8, 2.6, 2.4, 2.3],
        "Pertumbuhan Ekonomi (%)": [5.1, 5.2, 5.0, 4.9, 5.1, 5.3]
    }
    df = pd.DataFrame(data)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tabel Data")
        st.dataframe(df)
    
    with col2:
        st.subheader("Grafik Inflasi")
        fig = px.line(df, x="Bulan", y="Inflasi (%)", title="Inflasi Bulanan")
        st.plotly_chart(fig, use_container_width=True)

elif menu_option == "Sosial":
    st.header("Data Sosial")
    # Tambahkan konten untuk data sosial di sini
    st.write("Data kependudukan, kemiskinan, dll.")

# Footer
st.markdown("---")
st.markdown("© 2023 Badan Pusat Statistik - Aplikasi Streamlit")

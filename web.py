import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Statistik - BPS",
    page_icon="📊",
    layout="wide"
)

# CSS sederhana
st.markdown("""
    <style>
    .header { color: #0066cc; font-size: 24px; font-weight: bold; }
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
        ["Ekonomi", "Sosial", "Pertanian", "Perdagangan"]
    )
    tahun = st.slider("Pilih Tahun", 2010, 2023, 2023)

# Konten utama
if menu_option == "Ekonomi":
    st.header("Data Ekonomi")
    data = {
        "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"],
        "Inflasi (%)": [2.5, 2.7, 2.8, 2.6, 2.4, 2.3],
        "Pertumbuhan (%)": [5.1, 5.2, 5.0, 4.9, 5.1, 5.3]
    }
    df = pd.DataFrame(data)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tabel Data")
        st.dataframe(df)
    
    with col2:
        st.subheader("Grafik Inflasi")
        st.line_chart(df, x="Bulan", y="Inflasi (%)")

elif menu_option == "Sosial":
    st.header("Data Sosial")
    st.write("Data kependudukan akan ditampilkan di sini")

# Footer
st.markdown("---")
st.caption("© 2023 Aplikasi Statistik - Dibuat dengan Streamlit")

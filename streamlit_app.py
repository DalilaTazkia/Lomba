import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Solusi IT",
    page_icon="💻",
    layout="wide"
)

# Data contoh
data_kasus = pd.DataFrame({
    "Kasus": [
        "Aplikasi lambat", 
        "Database error", 
        "Server down", 
        "Masalah jaringan"
    ],
    "Solusi": [
        "Optimasi query, tambah RAM, caching",
        "Periksa koneksi, backup data, repair table",
        "Restart service, cek resource, scale up",
        "Cek kabel, restart router, ganti ISP"
    ],
    "Tingkat Kesulitan": ["Sedang", "Tinggi", "Kritis", "Rendah"],
    "Status": ["Teratasi", "Dalam Proses", "Belum", "Teratasi"]
})

data_teknologi = pd.DataFrame({
    "Teknologi": ["Python", "Streamlit", "Pandas", "NumPy", "Scikit-learn"],
    "Kategori": ["Bahasa", "Framework", "Library", "Library", "Library"],
    "Popularitas": ["Sangat Populer", "Populer", "Sangat Populer", "Populer", "Populer"]
})

# Navigasi sidebar
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih halaman:", 
                        ["Beranda", "Kasus & Solusi", "Data Teknologi"])

# Halaman Beranda
if menu == "Beranda":
    st.title("Selamat Datang di Aplikasi Solusi IT")
    st.image("https://via.placeholder.com/800x200?text=Solusi+IT+Modern", use_column_width=True)
    
    st.markdown("""
    ## Tentang Aplikasi Ini
    
    Aplikasi ini dibuat untuk membantu tim IT dalam menangani berbagai kasus teknis 
    yang sering terjadi dalam pengembangan dan maintenance sistem.
    
    **Fitur utama:**
    - Katalog kasus dan solusi IT
    - Database pengetahuan teknologi
    - Panduan troubleshooting terstruktur
    
    ### Cara Menggunakan
    1. Pilih menu **Kasus & Solusi** untuk melihat daftar masalah umum
    2. Cari solusi yang relevan dengan masalah Anda
    3. Untuk data teknologi, buka menu **Data Teknologi**
    """)
    
    st.success("🚀 Aplikasi siap membantu Anda menyelesaikan masalah teknis!")

# Halaman Kasus & Solusi
elif menu == "Kasus & Solusi":
    st.title("Kasus dan Solusi IT")
    st.markdown("Berikut adalah daftar kasus umum beserta solusi yang direkomendasikan:")
    
    # Tampilkan data
    st.dataframe(data_kasus, use_container_width=True, hide_index=True)
    
    # Filter data
    st.subheader("Filter Kasus")
    col1, col2 = st.columns(2)
    with col1:
        tingkat_filter = st.multiselect(
            "Filter berdasarkan tingkat kesulitan:",
            options=data_kasus["Tingkat Kesulitan"].unique(),
            default=data_kasus["Tingkat Kesulitan"].unique()
        )
    with col2:
        status_filter = st.multiselect(
            "Filter berdasarkan status:",
            options=data_kasus["Status"].unique(),
            default=data_kasus["Status"].unique()
        )
    
    # Terapkan filter
    filtered_data = data_kasus[
        (data_kasus["Tingkat Kesulitan"].isin(tingkat_filter)) & 
        (data_kasus["Status"].isin(status_filter))
    ]
    
    st.dataframe(filtered_data, use_container_width=True, hide_index=True)
    
    # Form tambah kasus baru
    st.subheader("Tambahkan Kasus Baru")
    with st.form("form_kasus_baru"):
        kasus = st.text_input("Kasus/Masalah")
        solusi = st.text_area("Solusi")
        tingkat = st.selectbox("Tingkat Kesulitan", ["Rendah", "Sedang", "Tinggi", "Kritis"])
        status = st.selectbox("Status", ["Belum", "Dalam Proses", "Teratasi"])
        
        if st.form_submit_button("Simpan Kasus"):
            new_case = pd.DataFrame([{
                "Kasus": kasus,
                "Solusi": solusi,
                "Tingkat Kesulitan": tingkat,
                "Status": status
            }])
            data_kasus = pd.concat([data_kasus, new_case], ignore_index=True)
            st.success("Kasus berhasil ditambahkan!")
            st.experimental_rerun()

# Halaman Data Teknologi
elif menu == "Data Teknologi":
    st.title("Database Pengetahuan Teknologi")
    st.markdown("Daftar teknologi yang relevan untuk pengembangan solusi IT:")
    
    # Tampilkan data
    st.dataframe(data_teknologi, use_container_width=True, hide_index=True)
    
    # Statistik
    st.subheader("Statistik Teknologi")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Teknologi", len(data_teknologi))
    with col2:
        populer_count = len(data_teknologi[data_teknologi["Popularitas"] == "Sangat Populer"])
        st.metric("Teknologi Sangat Populer", populer_count)
    
    # Grafik
    st.bar_chart(data_teknologi["Kategori"].value_counts())

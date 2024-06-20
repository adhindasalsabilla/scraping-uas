import pandas as pd
import streamlit as st

# Nama file CSV
fn1 = 'imdb_primary_uas.csv'

# Menampilkan judul di halaman web
st.title("Scraping IMDB")

# Membaca file CSV ke dalam DataFrame dengan encoding 'latin1'
df1 = pd.read_csv(fn1, encoding='latin1')

# Menampilkan DataFrame sebagai tabel
st.dataframe(df1)

# Fungsi untuk membuat visualisasi
def visualize_top_10(df):
    # Ambil 10 baris pertama
    top_10 = df.head(10)

    # Ambil kolom yang relevan
    judul_film = top_10['judul']
    rating = top_10['rating']

    # Buat visualisasi
    plt.figure(figsize=(10, 8))
    plt.barh(judul_film, rating, color='skyblue')
    plt.title('Top 10 Rating Film di IMDB')
    plt.xlabel('Rating')
    plt.ylabel('Judul Film')
    st.pyplot(plt)

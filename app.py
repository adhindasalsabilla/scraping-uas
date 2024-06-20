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

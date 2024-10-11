import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import streamlit as st

# Membaca dataset
data = pd.read_csv('Dasboard/main.csv')

# Mengonversi kolom tahun, bulan, tanggal menjadi tipe datetime
data['date'] = pd.to_datetime(data[['year', 'month', 'day']])

# Menyusun ulang data untuk analisis tren
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['day'] = data['date'].dt.day

# Streamlit sidebar
st.sidebar.header('Huairou Air Quality Dashboard')
st.sidebar.image("Dasboard/Huairou.png")

# **Rentang Tanggal**
st.sidebar.subheader('Filter Rentang Tanggal')
min_date = data['date'].min()
max_date = data['date'].max()
date_range = st.sidebar.date_input("Pilih rentang tanggal:", [min_date, max_date])


# Filter dataset berdasarkan rentang tanggal yang dipilih
filtered_data = data[(data['date'] >= pd.to_datetime(date_range[0])) & (data['date'] <= pd.to_datetime(date_range[1]))]

# Menampilkan info dan deskripsi dataset
st.title('Huairou Air Quality Dashboard :sparkles:')
st.subheader(f'Tren Konsentrasi PM2.5 di Distrik Huairou ({date_range[0]} - {date_range[1]})')

# Visualisasi tren PM2.5
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_data['date'], filtered_data['PM2.5'], marker='o', linestyle='-', color='Teal')
ax.set_title('Tren Konsentrasi PM2.5 di Distrik Huairou')
ax.set_xlabel('Waktu')
ax.set_ylabel('Konsentrasi PM2.5 (µg/m³)')
plt.xticks(rotation=45)
plt.grid()
st.pyplot(fig)

# Visualisasi pola konsentrasi PM2.5 setiap jam
st.subheader('Pola Konsentrasi PM2.5 di Distrik Huairou Setiap Jam')
hourly_avg = filtered_data.groupby('hour')['PM2.5'].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
ax.barh(hourly_avg['hour'], hourly_avg['PM2.5'], color='Gold')
ax.set_title('Pola Konsentrasi PM2.5 di Distrik Huairou Setiap Jam')
ax.set_xlabel('Rata-rata Konsentrasi PM2.5 (µg/m³)')
ax.set_ylabel('Jam')
plt.yticks(range(24), ['12 AM','1 AM','2 AM','3 AM','4 AM','5 AM','6 AM','7 AM','8 AM','9 AM','10 AM',
      '11 AM','12 PM','1 PM','2 PM','3 PM','4 PM','5 PM','6 PM','7 PM',
      '8 PM','9 PM','10 PM','11 PM'])
plt.grid(axis='x')
st.pyplot(fig)

# Visualisasi konsentrasi PM2.5 per bulan
st.subheader('Rata-rata Konsentrasi PM2.5 di Distrik Huairou per Bulan')
monthly_avg = filtered_data.groupby('month')['PM2.5'].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(monthly_avg['month'], monthly_avg['PM2.5'], color='Lightcoral')
ax.set_title('Rata-rata Konsentrasi PM2.5 di Distrik Huairou per Bulan')
ax.set_xlabel('Bulan')
ax.set_ylabel('Rata-rata Konsentrasi PM2.5 (µg/m³)')
plt.xticks(range(1, 13), ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'], rotation=45)
plt.grid(axis='y')
st.pyplot(fig)

# Visualisasi heatmap korelasi faktor lingkungan
st.subheader('Korelasi antara PM2.5 dan Faktor Lingkungan')
correlation_matrix = filtered_data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
ax.set_title('Korelasi antara PM2.5 dan Faktor Lingkungan')
st.pyplot(fig)

# Visualisasi arah angin dan PM2.5
st.subheader('Rata-rata Konsentrasi PM2.5 Berdasarkan Arah Angin')
wind_avg = filtered_data.groupby('wd')['PM2.5'].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(wind_avg['wd'], wind_avg['PM2.5'], color='Mediumpurple')
ax.set_title('Rata-rata Konsentrasi PM2.5 Berdasarkan Arah Angin')
ax.set_xlabel('Arah Angin')
ax.set_ylabel('Rata-rata Konsentrasi PM2.5 (µg/m³)')
plt.grid(axis='y')
st.pyplot(fig)

# Menentukan siang atau malam berdasarkan jam
def get_time_of_day(hour):
    if hour >= 6 and hour < 18:
        return 'Siang'
    else:
        return 'Malam'
    
# Visualisasi konsentrasi PM2.5 berdasarkan malam/siang
st.subheader('Rata-rata Konsentrasi PM2.5 di Distrik Huairou per Siang atau Malam')
filtered_data['time_of_day'] = filtered_data['month'].apply(get_time_of_day)
seasonal_avg = filtered_data.groupby('time_of_day')['PM2.5'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(seasonal_avg['time_of_day'], seasonal_avg['PM2.5'], color='Silver')
ax.set_title('Rata-rata Konsentrasi PM2.5 di Distrik Huairou per Siang atau Malam')
ax.set_xlabel('Waktu')
ax.set_ylabel('Rata-rata Konsentrasi PM2.5 (µg/m³)')
plt.grid(axis='y')
st.pyplot(fig)

# Menentukan musim berdasarkan bulan
def get_season(month):
    if month in [12, 1, 2]:
        return 'Musim Dingin'
    elif month in [3, 4, 5]:
        return 'Musim Semi'
    elif month in [6, 7, 8]:
        return 'Musim Panas'
    else:
        return 'Musim Gugur'

# Visualisasi konsentrasi PM2.5 berdasarkan musim
st.subheader('Rata-rata Konsentrasi PM2.5 di Distrik Huairou per Musim')
filtered_data['season'] = filtered_data['month'].apply(get_season)
seasonal_avg = filtered_data.groupby('season')['PM2.5'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(seasonal_avg['season'], seasonal_avg['PM2.5'], color='Lightcoral')
ax.set_title('Rata-rata Konsentrasi PM2.5 di Distrik Huairou per Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Konsentrasi PM2.5 (µg/m³)')
plt.grid(axis='y')
st.pyplot(fig)

# **Copyright**
st.markdown("""---""")
st.markdown("© 2024 Air Quality Analysis | Dibuat oleh Elvan Nasrul")


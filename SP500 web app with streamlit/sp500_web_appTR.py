import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

st.title('S&P 500 Uygulaması')

st.markdown("""
Bu uygulama, **S&P 500**'ün (Wikipedia'dan) ve buna karşılık gelen **hisse senedi kapanış fiyatlarının** (yıl başından bugüne) listesini getirir!
* **Python kütüphaneleri:** base64, pandas, streamlit, yfinance, numpy, matplotlib
* **Veri kaynağı:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('Kullanıcı Giriş Özellikleri')

# S&P 500 verisinin web scraping'i
@st.cache_data(ttl=600)  # Cache the data for 600 seconds (10 minutes)
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# Yan panel - Sektor seçimi
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sektör', sorted_sector_unique, sorted_sector_unique)

# Veriyi filtreleme
df_selected_sector = df[df['GICS Sector'].isin(selected_sector)]

st.header('Seçilen Sektördeki Şirketleri Göster')
st.write('Veri Boyutu: ' + str(df_selected_sector.shape[0]) + ' satır ve ' + str(df_selected_sector.shape[1]) + ' sütun.')
st.dataframe(df_selected_sector)

# S&P500 verisini indirme
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # stringler <-> baytlar dönüşümü
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">CSV Dosyasını İndir</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# Yahoo Finans'tan hisse senedi verisini alın
data = yf.download(
        tickers=list(df_selected_sector[:10].Symbol),
        period="ytd",
        interval="1d",
        group_by='ticker',
        auto_adjust=True,
        prepost=True,
        threads=True,
        proxy=None
    )

# Kapanış Fiyatını Göster
def price_plot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df['Tarih'] = df.index
    fig = plt.figure()
    plt.fill_between(df.Tarih, df.Close, color='skyblue', alpha=0.3)
    plt.plot(df.Tarih, df.Close, color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight='bold')
    plt.xlabel('Tarih', fontweight='bold')
    plt.ylabel('Kapanış Fiyatı', fontweight='bold')
    return st.pyplot(fig)

num_company = st.sidebar.slider('Şirket Sayısı', 1, 5)

if st.button('Grafikleri Göster'):
    st.header('Hisse Senedi Kapanış Fiyatı')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)

import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

st.title('S&P 500 Application')

st.markdown("""
This application fetches the list of **S&P 500** (from Wikipedia) and the corresponding **stock closing prices** (year-to-date)!
* **Python libraries:** base64, pandas, streamlit, yfinance, numpy, matplotlib
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('User Input Features')

# Scraping S&P 500 data
@st.cache_data(ttl=600)  # Cache the data for 600 seconds (10 minutes)
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# Sidebar - Sector selection
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Data filtering
df_selected_sector = df[df['GICS Sector'].isin(selected_sector)]

st.header('Show Companies in Selected Sector')
st.write('Data Size: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)

# Download S&P500 data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Convert string <-> bytes conversion
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# Get stock data from Yahoo Finance
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

# Show Closing Prices
def price_plot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df['Date'] = df.index
    fig = plt.figure()
    plt.fill_between(df.Date, df.Close, color='skyblue', alpha=0.3)
    plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight='bold')
    plt.xlabel('Date', fontweight='bold')
    plt.ylabel('Closing Price', fontweight='bold')
    return st.pyplot(fig)

num_company = st.sidebar.slider('Number of Companies', 1, 5)

if st.button('Show Charts'):
    st.header('Stock Closing Prices')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)

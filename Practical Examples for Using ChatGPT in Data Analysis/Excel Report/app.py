import pandas as pd
import os
import plotly.express as px
import streamlit as st

# Define the path to the data folder
# Veri klasörüne giden yolu tanımlayın
data_folder = 'Excel_Report\data'

# Get a list of all the Excel files in the data folder
# Veri klasöründeki tüm Excel dosyalarının bir listesini alın
excel_files = [f for f in os.listdir(data_folder) if f.endswith('.xlsx')]

# Create an empty dataframe to hold the combined data
# Birleştirilmiş verileri tutmak için boş bir veri çerçevesi oluşturun
combined_data = pd.DataFrame()

# Loop through each Excel file and append its data to the combined_data dataframe
# Her bir Excel dosyasında dolaşın ve verilerini birleştirilmiş_data veri çerçevesine ekleyin
for file in excel_files:
    # Load the Excel file into a dataframe
    # Excel dosyasını bir veri çerçevesine yükleyin
    df = pd.read_excel(os.path.join(data_folder, file))
    
    # Add a column to the dataframe to indicate the source file
    # Kaynak dosyayı belirtmek için veri çerçevesine bir sütun ekleyin
    df['Source'] = file
    
    # Append the data to the combined_data dataframe
    # Kaynak dosyayı belirtmek için veri çerçevesine bir sütun ekleyin
    combined_data = combined_data.append(df, ignore_index=True)

# Drop duplicate rows
# Yinelenen satırları bırakın
combined_data.drop_duplicates(inplace=True)

# Handle missing values
# Eksik değerleri işle
combined_data.dropna(inplace=True)

# Calculate total revenue, expenses, and profit for each category
# Her kategori için toplam geliri, giderleri ve karı hesaplayın
category_data = combined_data.groupby('Category').agg({'Revenue': 'sum', 'Expenses': 'sum'})
category_data['Profit'] = category_data['Revenue'] - category_data['Expenses']

# Create a Streamlit dashboard
# Bir Streamlit panosu oluşturun
st.set_page_config(page_title='Total Revenue, Expenses, and Profit by Category/Kategoriye Göre Toplam Gelir, Gider ve Kâr', page_icon=':chart_with_upwards_trend:')
st.title('Total Revenue, Expenses, and Profit by Category/Kategoriye Göre Toplam Gelir, Gider ve Kâr')
st.subheader('Grouped Data')

# Create an interactive chart using Plotly and display it in the dashboard
# Plotly kullanarak etkileşimli bir grafik oluşturun ve gösterge tablosunda görüntüleyin
fig = px.bar(category_data, x=category_data.index, y=['Revenue', 'Expenses', 'Profit'], barmode='group')
st.plotly_chart(fig)

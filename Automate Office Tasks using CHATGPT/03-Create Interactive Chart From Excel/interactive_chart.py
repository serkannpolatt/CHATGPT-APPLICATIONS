import pandas as pd
import plotly.express as px
import os

try:
    # load the data from the "Data" sheet of the "Financial_Data.xlsx" workbook
    # "Financial Data.xlsx" çalışma kitabının "Veri" sayfasından verileri yükleyin
    data = pd.read_excel("03-Create Interactive Chart From Excel\Financial_Data.xlsx", sheet_name="Data")

    # check if 'Country' and 'Sales' columns exists in data
    # verilerde 'Ülke' ve 'Satış' sütunlarının olup olmadığını kontrol edin
    if 'Country' not in data.columns or 'Sales' not in data.columns:
        raise ValueError("Columns are missing/Sütunlar eksik")
    # group the data by country and calculate the total sales for each country
    # verileri ülkeye göre gruplandırın ve her ülke için toplam satışları hesaplayın
    sales_by_country = data.groupby("Country")["Sales"].sum().reset_index()

    # create the bar chart
    # çubuk grafiği oluştur
    fig = px.bar(sales_by_country, x="Country", y="Sales", title="Financial Data By Country",
                 labels={"Country": "Country", "Sales": "Total Sales"},
                 color_discrete_sequence=["#00008B"])

    # save the chart to the same directory as the workbook
    # grafiği çalışma kitabıyla aynı dizine kaydedin
    fig.write_html("Financial Data By Country.html")

    # display the chart
    # grafiği göster
    fig.show()

except FileNotFoundError as e:
    print(f"{e} not found/bulunamadı")
except ValueError as e:
    print(e)

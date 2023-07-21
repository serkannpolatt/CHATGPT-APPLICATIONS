## English
## Excel Data Report

This project aims to retrieve financial data from a series of Excel files, consolidate the data, and calculate total revenue, expenses, and profit by category. Additionally, it generates an Excel report and an interactive chart based on the data.

### Project Objective

The objective of this project is to provide an automated tool for collecting, analyzing, and reporting financial data. The goals are as follows:

1. **Data Collection:** The project retrieves data from Excel files in a specific format. Each file contains financial data such as revenue, expenses, and other financial metrics for a given period.

2. **Data Consolidation:** The project consolidates the data from all Excel files into a single dataset. This facilitates the comparison and analysis of data from different periods.

3. **Calculations:** The project performs calculations on the consolidated dataset to determine the total revenue, expenses, and profit by category.

4. **Reporting:** The project generates a detailed Excel report using the calculated data. The report includes the total revenue, expenses, and profit amounts categorized by their respective categories.

5. **Data Visualization:** The project creates an interactive chart that visually presents the revenue, expenses, and profit amounts by category.

### How to Use

1. Place the Excel files to be analyzed in the "data" folder located in the project's main directory. The files should have the extension ".xlsx".

2. Run the "main.py" file in the project's main directory. This file consolidates the data, performs calculations, and generates the reports.

3. Once the process is completed, an Excel report named "category_report.xlsx" will be created and saved.

4. Additionally, an HTML file named "category_chart.html" will be generated, containing an interactive chart.

### Requirements

- Python 3.x
- pandas library
- xlsxwriter library
- plotly library
- streamlit library

### Installation


1. Download and install Python 3.x from here.
2. Install the required libraries by executing the following command in the terminal:
 > pip install pandas xlsxwriter plotly streamlit
 
3. Navigate to the main directory of the project and run the "main.py" file.


## Türkçe
## Excel Veri Raporu
Bu proje, bir dizi Excel dosyasından finansal verileri almayı, bu verileri birleştirmeyi ve kategori bazında toplam gelir, gider ve kar hesaplamayı amaçlamaktadır. Ayrıca, bu verileri kullanarak bir Excel raporu ve etkileşimli bir grafik oluşturur.

### Projenin Amacı

Bu proje, finansal verilerin toplanması, analizi ve raporlanması için bir otomatik araç sağlamaktır. Amacı şunlardır:

1. **Veri Toplama:** Proje, belirli bir formatta bulunan Excel dosyalarından verileri alır. Her dosya, bir dönemdeki gelir, gider ve diğer mali verileri içerir.

2. **Veri Birleştirme:** Proje, tüm Excel dosyalarındaki verileri birleştirir ve tek bir veri kümesi oluşturur. Bu, farklı dönemlerdeki verilerin karşılaştırılmasını ve analiz edilmesini kolaylaştırır.

3. **Hesaplamalar:** Proje, birleştirilen veri kümesi üzerinde işlemler yaparak kategori bazında toplam gelir, gider ve kar hesaplar.

4. **Raporlama:** Proje, hesaplanan verileri kullanarak ayrıntılı bir Excel raporu oluşturur. Rapor, kategoriye göre ayrılmış toplam gelir, gider ve kar miktarlarını içerir.

5. **Veri Görselleştirme:** Proje, etkileşimli bir grafik oluşturur. Bu grafik, kategori bazında gelir, gider ve kar miktarlarının görsel olarak sunulmasını sağlar.

### Nasıl Kullanılır

1. Projenin ana dizininde bulunan data klasörüne, analiz edilmek istenen Excel dosyalarını ekleyin. Dosyaların uzantısı .xlsx olmalıdır.

2. Proje ana dizinindeki main.py dosyasını çalıştırın. Bu dosya, verileri birleştirir, hesaplamaları yapar ve raporları oluşturur.

3. İşlem tamamlandığında, category_report.xlsx adında bir Excel raporu oluşturulacak ve kaydedilecektir.

4. Aynı zamanda, category_chart.html adında bir HTML dosyası oluşturulacak ve etkileşimli bir grafik içerecektir.

### Gereksinimler

- Python 3.x
- pandas kütüphanesi
- xlsxwriter kütüphanesi
- plotly kütüphanesi
- streamlit kütüphanesi

### Kurulum

1. Python 3.x'i buradan indirin ve yükleyin.
2. Gereksinimleri yüklemek için terminale aşağıdaki komutu girin:
 > pip install pandas xlsxwriter plotly streamlit
3. Projenin ana dizinine gidin ve main.py dosyasını çalıştırın.
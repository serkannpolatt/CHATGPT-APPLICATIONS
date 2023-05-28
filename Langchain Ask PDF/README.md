## English
## Ask Your PDF
### Purpose
This Python script aims to provide users with the ability to upload a PDF file, extract its text content, and search for answers to questions related to the PDF. The script performs the following operations:

1. Uploads the PDF file and extracts its text content.
2. Splits the text into chunks based on a specified character (separator).
3. Represents the text chunks by creating embeddings using OpenAI Embeddings.
4. Creates a knowledge base from the represented text chunks.
5. Prompts the user to ask a question related to the PDF.
6. Utilizes the OpenAI model to find the most suitable answer to the question and displays the results.

### Functions
**load_dotenv():** Loads environment variables from the .env file.

**main():** The main function that creates the user interface.

**st.set_page_config():** Sets the page configuration for the Streamlit application.

**st.header():** Creates a header tag.

**st.file_uploader():** Provides a file upload area for the user to upload the PDF file.

**PdfReader():** Reads the PDF file using the PyPDF2 library.

**page.extract_text():** Uses the extract_text() function from the PyPDF2 library to extract the text content of a page.

**CharacterTextSplitter():** A class that splits the text into chunks based on a specified character (separator).

**OpenAIEmbeddings():** Represents the text using OpenAI Embeddings.

**FAISS.from_texts():** Creates a knowledge base from the texts.

**st.text_input():** Prompts the user for text input.

**knowledge_base.similarity_search():** Returns documents similar to the question asked by the user.

**OpenAI():** Creates a class for using the OpenAI model.

**load_qa_chain():** Creates a chain for searching for answers to questions using the OpenAI model.

**get_openai_callback():** Retrieves the OpenAI callback function.

### Usage
1. Add the necessary environment variables to the .env file.
2.Run the script.
3. A page with the title "Ask your PDF" will open in your web browser.
4. Under the "Upload your PDF" heading, use the file uploader to upload your PDF file.
5. Once the upload is complete, the text content of the PDF will be automatically extracted and displayed in the interface.
6. Under the "Ask a question about your PDF" heading, you can ask a question related to the PDF.
7. After entering the question, the script will use the OpenAI model to search for the answer, and the results will be displayed in the interface.

### Requirements
- Python 3.x
- dotenv
- streamlit
- PyPDF2
- langchain


## Türkçe
## PDF'nizi Sorun
### Amaç
Bu Python betiği, kullanıcıya bir PDF dosyasını yükleyip metin içeriğini çıkarma ve PDF ile ilgili sorulara yanıtlar arama imkanı sağlamayı amaçlar. Betik aşağıdaki işlemleri gerçekleştirir:
1. PDF dosyasını yükler ve metin içeriğini çıkarır.
2. Metni belirli bir karaktere (ayraca) göre parçalara böler.
3. Metin parçalarını gömmeler oluşturmak için OpenAI Embeddings kullanarak temsil eder.
4. Temsil edilen metin parçalarından bir bilgi tabanı oluşturur.
5. Kullanıcıdan PDF ile ilgili bir soru alır.
6. Soruya en uygun cevabı bulmak için OpenAI modelini kullanır ve sonucu görüntüler.

### İşlevler
**load_dotenv():** .env dosyasından çevre değişkenlerini yükler.

**main():** Ana işlevdir ve kullanıcı arayüzünü oluşturur.

**st.set_page_config():** Streamlit uygulamasının sayfa yapılandırmasını ayarlar.

**st.header():** Başlık etiketi oluşturur.

**st.file_uploader():** Kullanıcıya PDF dosyasını yüklemesi için bir dosya yükleme alanı sağlar.

**PdfReader():** PyPDF2 kütüphanesini kullanarak PDF dosyasını okur.

**page.extract_text():** Bir sayfanın metin içeriğini çıkarmak için PyPDF2 kütüphanesinin extract_text() işlevini kullanır.

**CharacterTextSplitter():** Metni belirli bir karaktere (ayraca) göre parçalara bölen bir sınıf.

**OpenAIEmbeddings():** OpenAI Embeddings kullanarak metinleri temsil eder.

**FAISS.from_texts():** Metinlerden bir bilgi tabanı oluşturur.

**st.text_input():** Kullanıcıdan metin girişi alır.

**knowledge_base.similarity_search():** Kullanıcının sorduğu soruya benzer belgeleri döndürür.

**OpenAI():** OpenAI modelini kullanmak için bir sınıf oluşturur.

**load_qa_chain():** OpenAI modelini kullanarak sorulara yanıt aramak için bir sıra oluşturur.

**get_openai_callback():** OpenAI callback işlevini alır.

### Kullanım
1. .env dosyasına çevre değişkenlerini ekleyin.
2. Betiği çalıştırın.
3. Web tarayıcınızda "Ask your PDF / PDF'nizi sorun" başlığıyla bir sayfa açılacak.
4. "Upload your PDF / PDF'nizi yükleyin" başlığı altında, PDF dosyanızı yüklemek için dosya yükleme alanını kullanın.
5. Yükleme tamamlandığında, PDF dosyasının metin içeriği otomatik olarak çıkarılacak ve arayüzde görüntülenecektir.
6. "Ask a question about your PDF / PDF'niz hakkında bir soru sorun:" başlığı altında, PDF ile ilgili bir soru sorabilirsiniz.
7. Soruyu girdikten sonra, OpenAI modeli kullanılarak sorunun cevabı aranacak ve sonuçlar arayüzde görüntülenecektir.

### Gereksinimler
- Python 3.x
- dotenv
- streamlit
- PyPDF2
- langchain
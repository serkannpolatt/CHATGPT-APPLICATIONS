import streamlit as st


def main():
    # Streamlit sayfa yapılandırmasını özelleştirme
    custom_css = """
        <style>
            .main {
                font-family: 'Helvetica', 'Arial', sans-serif;
                color: #000000;  /* Yazı rengi: Siyah */
            }
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Arial', sans-serif;
                color: #FF0000;  /* Başlık rengi: Kırmızı */
            }
            p, a {
                font-family: 'Georgia', 'Times New Roman', serif;
                color: #FFFFFF;  /* Açıklama rengi: Beyaz */
            }
            .stMarkdown * {
                color: #FFFFFF;  /* Açıklama rengi: Beyaz */
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    st.title("Data Scientist CV")

    # Kişisel Bilgiler
    st.header("Kişisel Bilgiler")
    st.subheader("Ad Soyad")
    st.write("Serkan Polat")

    st.subheader("İletişim")
    st.write("E-posta: itsonlydatahustle@gmail.com")
    st.write("Telefon:xxxxx")
    st.write("LinkedIn: [LinkedIn Profiliniz](https://www.linkedin.com/in/serkan-polat-149360227/)")
    st.write("GitHub: [GitHub Profiliniz](https://github.com/serkannpolatt)")
    st.write("Blog: [Softforware](https://softforware.tech/)")
    st.write("Kaggle: [Kaggle Profiliniz](https://www.kaggle.com/serkanp)")

    # Deneyim
    st.header("Deneyim")

    # Dinosoft Business Solutions
    st.subheader("Dinosoft Business Solutions - Stajyer")
    st.write("Şubat 2023 - Şu Anda")
    st.write("Uzaktan çalışma")

    st.write("""
        - Çeşitli görüntü işleme algoritmaları ve teknikleri üzerinde kapsamlı araştırmalar yaptım ve başarılı bir şekilde projelerime uyguladım.
        - OpenCV ve TensorFlow gibi Python ve ilgili kütüphaneleri etkin bir şekilde kullanarak görüntü verilerini analiz ettim.
        - Ölçeklendirme, dönüşüm ve düzenleme gibi temel veri ön işleme adımlarını gerçekleştirdim ve doğru ve güvenilir görüntü işleme sağladım.
        - Derin öğrenme modelleri, özellikle Konvolüsyonel Sinir Ağları (CNN'ler) geliştirdim, eğittim ve değerlendirdim, önemli sonuçlar elde ettim.
        - Eğitim verilerinin kullanımını maksimize etmek için veri artırma tekniklerini uyguladım ve model performansını artırdım.
        - Görüntü sınıflandırma, nesne tespiti ve yüz tanıma gibi görevler için modellerin performansını değerlendirdim. Hiperparametre ayarlaması yaparak gerekli iyileştirmeleri gerçekleştirdim ve optimal sonuçlar sağladım.
    """)

    # Softforware
    st.subheader("Softforware - Kurucu")
    st.write("Eylül 2022 - Şu Anda")
    st.write("Kendi işim")

    st.write("""
        - Türkçe olarak verdiğim bu blogda, veri bilimi, veri analizi, makine öğrenimi ve genel olarak veri ile ilgili konular hakkında yazılar yazıyorum.
        - Araştırdığım konular hakkında daha kalıcı bir bilgi edinmek istediğim için blog yazısı yazmaya karar verdim.
    """)

    # Kaggle
    st.subheader("Kaggle Master - Serbest Çalışan")
    st.write("Mayıs 2022 - Şu Anda")
    st.write("1 yıl 3 ay")

    st.write("""
        - Veri kümeleriyle çalışmaktan büyük bir tutku duyuyorum ve bu platformda analizlerimi Python kullanarak sergiliyorum.
        - Gerçek hayat problemlerini ele aldığım ve bu alanda ilerlemeler kaydettiğim notebook'ları inceleyebilirsiniz.
    """)

    # Big-A Dijital Dönüşüm
    st.subheader("Big-A Dijital Dönüşüm - Stajyer")
    st.write("Ekim 2022 - Haziran 2023")
    st.write("Hibrit")

    st.write("""
        - NLP (Doğal Dil İşleme) alanında çalışmalara katılıyorum ve verilerden ilgili bilgileri çıkardım.
        - Big-A Digital Transformation'da NLP alanında çalışıyorum. Bu alandaki bilgilerimi kullanarak metin verilerini analiz ettim ve işledim.
        - Ayrıca çeşitli kaynaklardan veri çekme ve ilgili bilgileri çıkarma işlemleri gerçekleştirdim.
        - Python kullanarak Twitter'dan gerçek zamanlı veri topladım ve trend olan kelimelere göre analizler yaptım. Bu sayede ortaya çıkan olayları hızlı bir şekilde tespit edebildim ve takip edebildim.
        - Bu çalışmalarımız, trend olayları etkin bir şekilde izlememize ve hızlı bir şekilde tepki vermeye olanak sağladı.
    """)

    # TEKMAR
    st.subheader("TEKMAR - Tam Zamanlı")
    st.write("Haziran 2020 - Mayıs 2021")
    st.write("1 yıl")

    st.write("""
        - Burada, veri analizi ve donanım konularında hem deneyim hem de bilgi edindim.
        - TEKMAR'da satılan ürünlerin en çok satan ve en az satılan ürünlerini analiz ettim ve analiz sayesinde gereksiz alımları önledim ve satışlarımız arttı.
    """)

if __name__ == '__main__':
    main()

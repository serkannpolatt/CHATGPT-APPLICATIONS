import streamlit as st
from PyPDF2 import PdfFileReader

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        with open(pdf, 'rb') as file:
            reader = PdfFileReader(file)
            num_pages = reader.numPages
            for page_num in range(num_pages):
                page = reader.getPage(page_num)
                text += page.extractText()
    return text

def main():
    st.title("PDF Text Extraction")

    st.sidebar.header("Upload PDFs")
    pdf_docs = st.sidebar.file_uploader("Upload your PDFs", accept_multiple_files=True)

    if pdf_docs:
        st.write(f"Total PDFs: {len(pdf_docs)}")

        st.header("PDF Text Extraction")
        raw_text = get_pdf_text(pdf_docs)
        st.write(raw_text)

if __name__ == '__main__':
    main()

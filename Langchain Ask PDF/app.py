from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF / PDF'nizi sorun")
    st.header("Ask your PDF / PDF'nizi sorun 💬")
    
    # upload file
    # dosya yükleme
    pdf = st.file_uploader("Upload your PDF / PDF'nizi yükleyin", type="pdf")
    
    # extract the text
    # metni çıkar
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # split into chunks
        # parçalara bölün
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
      
        # create embeddings
        # yerleştirmeler oluştur
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)
      
        # show user input
        # kullanıcı girişini göster
        user_question = st.text_input("Ask a question about your PDF / PDF'niz hakkında bir soru sorun:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
        
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_question)
                st.write(response)
                st.write(cb)
                

if __name__ == '__main__':
    main()

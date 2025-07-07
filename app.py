import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# 🔐 Load API key from environment
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error("❌ OPENAI_API_KEY not found. Please set it in your terminal.")
    st.stop()

# 🧾 Streamlit setup
st.set_page_config(page_title="RAGify PDF Assistant")
st.title("📄 RAGify: Ask Questions & Export Clean Text from Your PDF")

# 📤 File uploader
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    # Save uploaded file locally
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF uploaded successfully!")

    # 🧹 Load and split PDF into chunks
    loader = PyPDFLoader("uploaded.pdf")
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(pages)

    # 📝 Combine chunks into clean text
    full_text = "\n\n".join(chunk.page_content for chunk in chunks)

    # 💾 Save clean text to file
    with open("clean_text.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

    # 📥 Download button for clean text
    st.download_button(
        label="📥 Download Clean Text File",
        data=full_text,
        file_name="clean_text.txt",
        mime="text/plain"
    )

    # 🧠 Create FAISS vector index for Q&A
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)
    retriever = db.as_retriever()

    # 🤖 Set up the retrieval-based QA chain
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=retriever
    )

    # ❓ User question input
    question = st.text_input("❓ Ask a question about your PDF")

    if question:
        answer = qa.run(question)
        st.subheader("🧠 Answer")
        st.write(answer)

# RAGify

**RAGify** is a beginner-friendly Python tool that extracts text from a PDF, cleans and formats it, then builds a Retrieval-Augmented Generation (RAG) pipeline using OpenAI and LangChain. Use it to:

- Generate a clean `.txt` version of any PDF (ideal for NotebookLM or Custom GPTs)  
- Split text into chunks, embed them with OpenAI’s embeddings, and store in FAISS  
- Ask questions of your document straight from the command line  

---

## ✨ Features

- **PDF text extraction** via `pdfminer.six`  
- **Automatic text cleaning** and insertion of page breaks  
- **Chunking** using LangChain’s `RecursiveCharacterTextSplitter`  
- **Embeddings** with OpenAI’s `text-embedding-ada-002`  
- **Vector storage** in FAISS (local)  
- **Question-answering** powered by GPT-3.5 or GPT-4  

---

## 🛠 Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/shauny79/RAGify.git
   cd RAGify

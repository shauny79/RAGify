import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

# ✅ Load your OpenAI key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Set it in your terminal environment.")

# ✅ Set the name of your PDF file here
pdf_filename = "mydocument.pdf"

# ✅ Load and split the PDF
loader = PyPDFLoader(pdf_filename)
pages = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(pages)

# ✅ Save clean text to a file (for NotebookLM or backups)
with open("clean_text.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk.page_content + "\n\n")

print("✅ Text saved to clean_text.txt — ready for NotebookLM!")

# ✅ Set up OpenAI embeddings and FAISS vector store
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(chunks, embeddings)

retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=retriever
)

# ✅ Handle optional questions from the command line
import sys

if len(sys.argv) > 1:
    question = " ".join(sys.argv[1:])
    answer = qa.run(question)
    print("🧠 Answer:", answer)

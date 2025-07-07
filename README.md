
````markdown
# 📄 RAGify

**RAGify** is a lightweight local app that lets you:

- ✅ Upload a PDF
- ✅ Extract and download clean text
- ✅ Ask GPT-3.5 questions based on the PDF content (Retrieval-Augmented Generation)
- ✅ Use the clean output in tools like NotebookLM, CustomGPTs, AI agents, or RAG pipelines

Built using Streamlit, LangChain, FAISS, and OpenAI's GPT API.

---

## 🚀 Features

- 🧹 Automatically extracts and cleans PDF text
- 📥 Downloadable `.txt` output
- ❓ Ask GPT-3.5 questions about your PDF
- 🔐 Secure — your OpenAI API key is never saved
- ⚙️ Runs entirely on your local machine

---

## 📦 Requirements

Install all required packages with:

```bash
pip3 install streamlit langchain langchain-community openai faiss-cpu pypdf
````

If `pip3` doesn't work:

```bash
python3 -m pip install streamlit langchain langchain-community openai faiss-cpu pypdf
```

---

## 🧾 How to Run

1. **Open Terminal**

2. **Navigate to the RAGify folder**:

```bash
cd ~/Documents/"GitHub Projects"/RAGify
```

3. **Manually enter your OpenAI API key** (do this every time you run it):

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxx"
```

4. **Start the app**:

```bash
python3 -m streamlit run app.py
```

5. **Open in browser**:
   The app will open automatically at [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Files

| File               | Description                                      |
| ------------------ | ------------------------------------------------ |
| `app.py`           | Main Streamlit app with PDF upload and Q\&A      |
| `rag_pdf.py`       | (Optional) original script for basic RAG setup   |
| `requirements.txt` | Python dependencies for the app                  |
| `start.sh`         | Optional shortcut to launch the app via terminal |
| `HOW_TO_RUN.txt`   | Clear instructions for future use                |
| `README.md`        | This readme file                                 |

---

## 📥 Output

* A `clean_text.txt` file is generated from your PDF.
* You can use this text in:

  * [NotebookLM](https://notebooklm.google.com/)
  * [CustomGPTs](https://chat.openai.com/gpts)
  * LangChain, n8n, or any RAG framework

---

## 🔐 API Key Security

* Your OpenAI API key is **not stored**
* You **manually enter it in Terminal** before running the app
* It only lives for that session

Example:

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxx"
```

---

## 🌱 Future Ideas

* [ ] Support multiple PDFs
* [ ] Deploy on Streamlit Cloud
* [ ] Summarise entire document
* [ ] Save and reload previous chats
* [ ] Use GPT-4 or other LLMs

---

## 👤 Author

Created with ❤️ by [shauny79](https://github.com/shauny79)

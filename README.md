
## 📁 Project Structure

---

## ✅ `README.md` Content

# PDF Question Answering App (Streamlit + RAG)

This project lets you upload a PDF, process it using Retrieval Augmented Generation (RAG), and interactively ask questions about its content via a web-based Streamlit GUI.

---

## 1) Setup Guide

### Required Python Packages

Install all dependencies using pip:

pip install -r requirements.txt


Or manually:
---
pip install streamlit
pip install PyPDF2
pip install langchain
pip install langchain-openai
pip install langchain-community
pip install openai
pip install python-dotenv
pip install faiss-cpu
---

### Environment Setup

1. Create a `.env` file with your OpenAI key:

OPENAI_API_KEY=your-api-key-here


2. Run the app:

streamlit run app.py

---

## 2) Introduction & How It Works

This project uses the following packages in order:

1. `streamlit` – Builds the user interface and handles user interaction
2. `PyPDF2` – Extracts text from PDF files
3. `langchain.text_splitter` – Splits text into manageable chunks
4. `langchain-openai` – Embeds text and sends prompts to OpenAI models
5. `langchain-community.vectorstores.FAISS` – Stores and searches vector embeddings
6. `faiss-cpu` – Backend vector database for similarity search
7. `openai` – OpenAI Python SDK
8. `dotenv` – Loads environment variables like the API key

---

## 3) Logic Overview

Here’s how the entire app works:

1. **PDF Upload**: The user uploads a PDF using the Streamlit interface.
2. **Text Extraction**: The app uses PyPDF2 to extract raw text from all pages of the PDF.
3. **Text Chunking**: The text is split into smaller chunks (1000 characters with 200-character overlap).
4. **Vectorization**: Each chunk is converted into a vector using OpenAI embeddings.
5. **FAISS Indexing**: All vectors are stored in a FAISS vectorstore for similarity search.
6. **User Input**: The user types a question into a text input box.
7. **Similarity Search**: The system searches for the most relevant chunks related to the question.
8. **Answer Generation**: Those chunks are passed to an LLM (gpt-3.5-turbo) via a QA chain that produces an answer.
9. **Response Display**: The answer is shown in the UI.

---

## 4) Flowchart (Mermaid)

flowchart TD
    A[User Uploads PDF] --> B[Extract Text from PDF using PyPDF2]
    B --> C[Split Text into Chunks]
    C --> D[Embed Chunks using OpenAIEmbeddings]
    D --> E[Store in FAISS Vector DB]
    F[User Asks a Question] --> G[Search Relevant Chunks using Similarity Search]
    G --> H[Send Chunks + Question to OpenAI QA Chain]
    H --> I[Return Answer]
    I --> J[Display in Streamlit App]

---

## 5) Weaknesses and Future Improvements

### Weaknesses

* **No file type validation beyond PDFs**: Only supports basic text-based PDFs. Scanned PDFs or images will fail silently.
* **Limited context window**: GPT-3.5-turbo has limitations in how much context it can handle, which may affect longer or complex answers.
* **Local-only FAISS**: The current FAISS vector store is in-memory and not persistent across sessions.
* **Lack of advanced UI**: The interface is minimal, with no file previews or summary outputs.

### Future Improvements

* Add support for OCR (Optical Character Recognition) to handle scanned PDFs using Tesseract or PaddleOCR.
* Store FAISS vector DBs in disk or cloud to preserve session state.
* Add model options like GPT-4 or Claude.
* Summarize PDF contents before Q\&A for quick overview.
* Allow upload of multiple documents and support multi-document QA.
* Add chatbot-style interface for a more natural flow.

---

---

## ✅ `requirements.txt`

streamlit
PyPDF2
langchain
langchain-openai
langchain-community
openai
python-dotenv
faiss-cpu

---


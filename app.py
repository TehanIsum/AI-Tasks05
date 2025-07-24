import streamlit as st
from rag_utils import extract_text_from_pdf, chunk_text, create_vectorstore, answer_question

# Page configuration
st.set_page_config(page_title="PDF Q&A App", layout="wide")
st.title("📄 Chat With Your PDF")

# Session state initialization
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# File upload
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Reading and processing PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        if text:
            chunks = chunk_text(text)
            st.session_state.vectorstore = create_vectorstore(chunks)
            st.success("PDF processed. You can now ask questions!")
        else:
            st.error("No text could be extracted from the PDF.")

# Question input
if st.session_state.vectorstore:
    question = st.text_input("Ask a question about the PDF:")
    if st.button("Get Answer") and question:
        with st.spinner("Thinking..."):
            try:
                answer = answer_question(st.session_state.vectorstore, question)
                st.markdown(f"### 🧠 Answer:\n{answer}")
            except Exception as e:
                st.error(f"Error: {e}")

# Footer
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f2f6;
    font weight: 10px;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    color: #888;
}
</style>
<div class="footer">
    Developed by Tehan Isum
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

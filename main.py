#imports
from utils.data_processing import load_pdf, chunk_text
from utils.embeddings import generate_and_load
from context.retrieval import retrieve
from model.generate import generate
from utils.config import model
import os
import faiss
import streamlit as st
import tempfile


##############################
#    Initializations
##############################
FAISS_INDEX_PATH = "data/faiss_index.index"


#######################################################################
# RAG query and response (using streamlit UI and dynamic file uploads) 
######################################################################
st.title("Medical RAG Assistant")
uploaded_file = st.file_uploader("Upload a medical PDF document", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    raw_text = load_pdf(tmp_path)
    chunks = chunk_text(raw_text)

    generate_and_load(chunks)
    index = faiss.read_index(FAISS_INDEX_PATH)

    query = st.text_input("Enter your question:")

    if query:
        with st.spinner("Generating answer..."):
            top_chunks = retrieve(query, index, chunks)
            response = generate(top_chunks, query)
            st.markdown("### Answer")
            st.write(response)

else:
    st.info("Please upload a medical PDF document to begin.")




import streamlit as st
import os
import tempfile
import sys

# Add parent directory to path for imports
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app'))

from core import load_document, summarize_document, extract_information, analyze_document

st.set_page_config(page_title="Document Analysis Agent", layout="wide")
st.title("Document Analysis Agent")
st.write("Upload a PDF document and analyze it")

# File upload
uploaded_file = st.file_uploader("Upload PDF document", type=["pdf"])
if uploaded_file:
    # Save uploaded file to temp directory
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded: {uploaded_file.name}")
    
    # Load document
    document_text = load_document(file_path)
    if document_text:
        # Create tabs for different functions
        tab1, tab2, tab3 = st.tabs(["Summarize", "Extract Information", "Ask Question"])
        
        with tab1:
            st.header("Document Summary")
            if st.button("Generate Summary"):
                with st.spinner("Generating summary..."):
                    summary = summarize_document(document_text)
                    st.write(summary)
        
        with tab2:
            st.header("Extract Information")
            info_type = st.text_input("What type of information would you like to extract?", 
                                       placeholder="E.g., dates, names, amounts, companies")
            if st.button("Extract") and info_type:
                with st.spinner(f"Extracting {info_type}..."):
                    extracted_info = extract_information(document_text, info_type)
                    st.write(extracted_info)
        
        with tab3:
            st.header("Ask a Question")
            question = st.text_input("What would you like to know about this document?")
            if st.button("Get Answer") and question:
                with st.spinner("Analyzing document..."):
                    answer = analyze_document(document_text, question)
                    st.write(answer)
    else:
        st.error("Failed to load document. Please check if it's a valid PDF.")

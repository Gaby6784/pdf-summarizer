import streamlit as st
import fitz  # PyMuPDF

# Page setup
st.set_page_config(page_title="PDF Summarizer (Lite)")
st.title("PDF Summarizer (Lite Version)")
st.write("Upload a PDF and preview its contents. Summarization is available in the full version.")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Page range input
page_range = st.text_input("Page range to preview (e.g. 1-3). Leave blank to preview all pages:")

if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""

        if page_range.strip():
            try:
                start, end = map(int, page_range.strip().split('-'))
                for page in pdf[start - 1:end]:
                    text += page.get_text()
            except:
                st.error("Invalid page range format. Use something like 1-3.")
                st.stop()
        else:
            for page in pdf:
                text += page.get_text()

    # Preview
    st.subheader("PDF Content Preview")
    st.text_area("Extracted Text (preview only):", text[:2000] + ("..." if len(text) > 2000 else ""), height=200)

    st.info("To unlock summarization and PDF export, get the full version on Fiverr or Gumroad.")
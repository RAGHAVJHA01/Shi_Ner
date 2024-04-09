import streamlit as st
import ocr
import pdf
import entity

def main():
    st.title("Document Text Extractor & Entity Recognition")

    # Sidebar for selecting document type
    document_type = st.sidebar.radio("Select Document Type:", ("Manual Text", "PDF", "Image"))

    text = ""  # Initialize text variable

    if document_type == "Manual Text":
        st.sidebar.write("You selected Manual Text")
        # Text input field for manual input
        manual_text = st.text_area("Enter text here:", "")
        text = manual_text.strip()  # Set text variable to manual_text

    elif document_type == "PDF":
        st.sidebar.write("You selected PDF")
        # Upload PDF file
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

        if uploaded_file is not None:
            text = pdf.extract_text_from_pdf(uploaded_file)
            st.write("Extracted text:")
            st.write(text)

    elif document_type == "Image":
        st.sidebar.write("You selected Image")
        # Get the input image from the user
        input_image = ocr.get_image()

        if input_image:
            text = ocr.perform_ocr(input_image)
            st.header("OCR Text Extraction Results:")
            st.write(text)

    # Entity Recognition section
    if st.sidebar.button("Entity Recognition"):
        if text:
            st.subheader("Automated Entity Recognition:")
            html = entity.recognize_entities(text)
            st.write(html, unsafe_allow_html=True)
        else:
            st.warning("Please input some text before performing entity recognition.")

if __name__ == "__main__":
    main()

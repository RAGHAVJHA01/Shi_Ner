import streamlit as st
from PyPDF2 import PdfReader
import keras_ocr
import tempfile
import os
import spacy
from spacy import displacy

# Function to get image file paths from user using Streamlit's file uploader
def get_image():
    uploaded_file = st.file_uploader("Upload Image File", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        return uploaded_file
    else:
        return None

# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(uploaded_file):
    text = ""
    with st.spinner("Extracting text..."):
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file.seek(0)
            pdf_path = tmp_file.name

        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()

        os.unlink(pdf_path)  # Remove temporary PDF file

    return text

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
            text = extract_text_from_pdf(uploaded_file)
            st.write("Extracted text:")
            st.write(text)

    elif document_type == "Image":
        st.sidebar.write("You selected Image")
        # Get the input image from the user
        input_image = get_image()

        if input_image:
            # keras-ocr will automatically download pretrained weights for the detector and recognizer.
            pipeline = keras_ocr.pipeline.Pipeline()

            # Read the uploaded image
            image = keras_ocr.tools.read(input_image)

            # Perform OCR on the image
            predictions = pipeline.recognize([image])[0]

            # Display the OCR results
            st.header("OCR Text Extraction Results:")
            for text, box in predictions:
                st.write(text)
            text = ' '.join([text for text, _ in predictions])

    # Entity Recognition section
    if st.sidebar.button("Entity Recognition"):
        if text:
            st.subheader("Automated Entity Recognition:")
            nlp_med7 = spacy.load("en_core_med7_lg")
            nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")

            doc_med7 = nlp_med7(text)
            doc_bc5cdr = nlp_bc5cdr(text)

            combined_entities = []

            for ent in doc_med7.ents:
                if ent.label_ != "CHEMICAL":
                    combined_entities.append((ent.start_char, ent.end_char, ent.label_))

            for ent in doc_bc5cdr.ents:
                combined_entities.append((ent.start_char, ent.end_char, ent.label_))

            colors = {
                "DRUG": "lightgreen",
                "DOSAGE": "green",
                "DISEASE": "red",
                "Chemical": "white"
            }

            entities = []
            for start, end, label in combined_entities:
                color = colors.get(label, "white")
                entities.append({"start": start, "end": end, "label": label, "color": color})

            html = displacy.render([{"text": text, "ents": entities, "title": None}],
                                   style="ent", manual=True, options={"colors": colors})

            st.write(html, unsafe_allow_html=True)
        else:
            st.warning("Please input some text before performing entity recognition.")

if __name__ == "__main__":
    main()

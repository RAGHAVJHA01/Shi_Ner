import streamlit as st
from spacy import displacy  # Add this line
from PIL import Image

def show_ui():
    st.sidebar.header("Input Options")
    option = st.sidebar.radio(
        "Choose an option:",
        ("Manual Input", "Upload PDF", "Upload Image")
    )
    if option == "Manual Input":
        text_input = st.text_area("Enter text manually:")
        pdf_file = None
        image_file = None
    elif option == "Upload PDF":
        text_input = None
        pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
        image_file = None
    else:  # option == "Upload Image"
        text_input = None
        pdf_file = None
        image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    return text_input, pdf_file, image_file

def display_output(combined_text, entities, colors):
    st.header("Output")
    st.subheader("Combined Text:")
    st.write(combined_text)
    html = displacy.render([{"text": combined_text, "ents": entities, "title": None}], style="ent", manual=True, options={"colors": colors})
    st.write(html, unsafe_allow_html=True)

import keras_ocr
import streamlit as st

def perform_ocr(input_image):
    pipeline = keras_ocr.pipeline.Pipeline()
    image = keras_ocr.tools.read(input_image)
    predictions = pipeline.recognize([image])[0]
    ocr_text = ' '.join([text for text, _ in predictions])
    return ocr_text

def get_image():
    uploaded_file = st.file_uploader("Upload Image File", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        return uploaded_file
    else:
        return None

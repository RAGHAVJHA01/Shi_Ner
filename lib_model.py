import spacy
from spacy import displacy

nlp_med7 = spacy.load("en_core_med7_lg")
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")

def visualize_entities(combined_text, combined_entities):
    # Your entity visualization code here...

import spacy

def load_spacy_models():
    nlp_med7 = spacy.load("en_core_med7_lg")
    nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")
    return nlp_med7, nlp_bc5cdr

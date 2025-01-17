import spacy
from spacy import displacy

def recognize_entities(text):
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

    return html

def combine_entities(doc_med7, doc_bc5cdr):
    combined_entities = []
    for ent in doc_med7.ents:
        if ent.label_ != "CHEMICAL":
            combined_entities.append({"start": ent.start_char, "end": ent.end_char, "label": ent.label_})
    for ent in doc_bc5cdr.ents:
        combined_entities.append({"start": ent.start_char, "end": ent.end_char, "label": ent.label_})
    return combined_entities

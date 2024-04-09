from transformers import pipeline

class Highlighter:
    @staticmethod
    def highlight_entities(text, entities):
        highlighted_text = ""
        for entity in entities:
            entity_type = entity['entity']
            if entity_type != 'No Entity':
                start, end = entity['start'], entity['end']
                highlighted_text += f"[{entity_type}]: {text[start:end]} "
        return highlighted_text.strip()

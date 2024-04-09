from transformers import AutoTokenizer, AutoModelForTokenClassification

class NERModel:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)

class NERPipeline:
    def __init__(self, model):
        self.pipeline = pipeline("ner", model=model.model, tokenizer=model.tokenizer)

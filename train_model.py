from models import NERModel
from pipeline import NERPipeline, Highlighter

# Load models
disease_model = NERModel("ugaray96/biobert_ncbi_disease_ner")
drug_model = NERModel("chintagunta85/electramed-small-ADE-DRUG-EFFECT-ner-v3")

# Create NER pipelines
disease_pipeline = NERPipeline(disease_model)
drug_pipeline = NERPipeline(drug_model)

# Perform NER for drugs
drug_entities = drug_pipeline.pipeline(text)

# Highlight and print entities
highlighted_drugs = Highlighter.highlight_entities(text, drug_entities)

print("Highlighted Drugs:", highlighted_drugs)

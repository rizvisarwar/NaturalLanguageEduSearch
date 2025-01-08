import spacy
from spacy.training import offsets_to_biluo_tags

# Load a SpaCy model
nlp = spacy.load("en_core_web_sm")

# Define the text and entity annotations
text = "I'm looking for a distance course on Natural Language Processing in English."
entities = [(18, 33, "EDUCATIONAL_GOAL"), (37, 64, "FIELD_OF_STUDY")]

# Create a Doc object
doc = nlp.make_doc(text)

# Convert offsets to BILUO tags
biluo_tags = offsets_to_biluo_tags(doc, entities)

# Print the tokens and their corresponding BILUO tags
for token, tag in zip(doc, biluo_tags):
    print(f"Token: {token.text}, Tag: {tag}")

# Shallow Parsing
# Noun Phrase Detection
import spacy
nlp = spacy.load("en_core_web_sm")

# sentence = "I want to do a Master's on European History in Stockholm Sweden."
# sentence = "I want to study European History in Stockholm Sweden."
sentence = "I'm looking for a distance course on Natural Language Processing in english language."

conference_text = (sentence)
conference_doc = nlp(conference_text)
# Extract Noun Phrases
for chunk in conference_doc.noun_chunks:
    print (chunk)
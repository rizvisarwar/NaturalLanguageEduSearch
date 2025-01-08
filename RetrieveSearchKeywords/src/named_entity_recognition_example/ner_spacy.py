import pandas as pd 
import spacy

nlp = spacy.load("en_core_web_sm")
pd.set_option("display.max_rows", 200)

content = "I want to do a Master's on Information Security in Sweden Stockholm."

doc = nlp(content)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
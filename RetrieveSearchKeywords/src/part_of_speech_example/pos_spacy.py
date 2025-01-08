# POS Part-of-Speech

import spacy

nlp = spacy.load("en_core_web_sm")

# sentence = "I want to do a Masters on Information Security in Stockholm Sweden."
sentence = "I want to study European History in Stockholm Sweden."
#sentence= "I want to do a masters on IT in Sweden"

about_text = (sentence)
about_doc = nlp(about_text)

nouns = []
properNouns = []
for token in about_doc:
    if token.pos_ == "NOUN":
        nouns.append(token)
    if token.pos_ == "PROPN":
        properNouns.append(token)

print('Noun(s): %s' % nouns)
print('Proper noun(s): %s' % properNouns)

# print("Noun(s): ") 

# for element in nouns: 
#     print(element)

# print("Proper Noun(s): ") 
# for element in properNouns: 
#     print(element) 

# for token in about_doc:
#     print(
#         f"""
# TOKEN: {str(token)}
# =====
# TAG: {str(token.tag_):10} POS: {token.pos_}
# EXPLANATION: {spacy.explain(token.tag_)}"""
#     )
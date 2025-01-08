import spacy

class SentenceProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process(self, sentence):
        doc = self.nlp(sentence)
        what = None
        field_of_study = None
        location = []

        for token in doc:
            if token.dep_ == "dobj" and token.head.lemma_ == "do":
                what = token.text
            elif token.dep_ == "pobj" and token.head.text == "on":
                field_of_study = token.text
            elif token.dep_ == "pobj" and token.head.text == "in":
                location.append(token.text)
            elif token.dep_ == "dobj" and token.head.lemma_ == "study":
                field_of_study = token.text

        return what, field_of_study, ' '.join(location)
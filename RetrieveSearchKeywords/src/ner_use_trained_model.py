import spacy

def main(input_text, nlp):
    doc = nlp(input_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)

if __name__ == "__main__":
    nlp = spacy.load("../TrainedModel")
    while True:
        input_text = input("Please enter the text to process (or type 'exit' to quit): ")
        if input_text.lower() == 'exit':
            break
        main(input_text, nlp)
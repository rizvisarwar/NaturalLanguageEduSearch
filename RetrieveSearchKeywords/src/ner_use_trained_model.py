import spacy
import time

def main():
    start_time = time.time()
    nlp = spacy.load("../TrainedModel")
    
    print("Time taken to load the model: %s seconds\n" % (time.time() - start_time))
    
    # testInputText = "I want to do a Master's on Information Security in Germany."
    testInputText = "I want to do a Master's on European History in stockholm sweden."
    # testInputText = "Jag vill plogga Ekonomi i Sverige."
    
    doc = nlp(testInputText)
    for ent in doc.ents:
        print(ent.label_, ent.text)
    
    print("\nProcess finished: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
    main()
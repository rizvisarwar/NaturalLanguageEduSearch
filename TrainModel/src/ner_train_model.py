import spacy
from spacy.training import Example
from annotate_dataset import getTrainingData

def main():
    # Load a small English model
    nlp = spacy.load("en_core_web_sm")

    # Add the new labels to the NER component
    ner = nlp.get_pipe("ner")
    ner.add_label("EDUCATIONAL_GOAL")
    ner.add_label("FIELD_OF_STUDY")
    ner.add_label("LOCATION_COUNTRY")
    ner.add_label("LOCATION_CITY")

    TRAIN_DATA = getTrainingData()

    # Prepare the training data
    examples = [Example.from_dict(nlp.make_doc(text), annotations) for text, annotations in TRAIN_DATA]

    # Begin training
    optimizer = nlp.create_optimizer()

    # Training loop
    for i in range(20):  # Number of training iterations
        for example in examples:
            nlp.update([example], drop=0.5, sgd=optimizer)

    nlp.to_disk("../TrainedModel")

if __name__ == "__main__":
    main()
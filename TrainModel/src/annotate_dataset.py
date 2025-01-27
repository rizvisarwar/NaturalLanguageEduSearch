import re

# Define patterns for automatic annotation
patterns = {
    "EDUCATIONAL_GOAL": r"(Master|Masters|Master's|distance course|distance program|PhD|Bachelor's|Bachelors|Bachelor)",
    "FIELD_OF_STUDY": r"(European History|Physics|Chemistry|Natural Language Processing|Data Science|redovisning|ekonomi|informationsteknik|Computer Science|Information Security|Software Engineering|Accessories Design|Accountancy|Accounting|Administration|Administration Studies|Administration, Business, and Economics|Administrative Law Studies|Adult Education|Advertising|Aeronautical Engineering)",
    "LOCATION_COUNTRY": r"(Germany|Sweden|Canada|Italy|Finland|Sverige|Tyskland|France)",
    "LOCATION_CITY": r"(Berlin|Stockholm|Rome)"
}

# Read sentences from file
with open('data/sentences.txt', 'r', encoding='utf-8') as file:
    texts = [line.strip() for line in file.readlines()]

# Annotate data
annotations = []
for text in texts:
    entities = []
    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            entities.append({"start": match.start(), "end": match.end(), "label": label})
    annotations.append({"text": text, "entities": entities})

# # Print the annotated data
# for item in annotations:
#     print(item)

# Convert JSON to SpaCy training data format
spacy_training_data = []
for item in annotations:
    text = item["text"]
    entities = [(entity["start"], entity["end"], entity["label"]) for entity in item["entities"]]
    spacy_training_data.append((text, {"entities": entities}))

def getTrainingData():
    return spacy_training_data
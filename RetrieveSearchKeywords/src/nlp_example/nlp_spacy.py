from processor import SentenceProcessor

SENTENCE = "I want to do a Masters on Information Security in Stockholm Sweden."

processor = SentenceProcessor()
what, field_of_study, location = processor.process(SENTENCE)
print("What:", what)
print("Field of Study:", field_of_study)
print("Location:", location)
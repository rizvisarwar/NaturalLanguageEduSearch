import speech_recognition as sr
import spacy
from ner_use_trained_model import main  # Import the main function

# Initialize recognizer
recognizer = sr.Recognizer()
nlp = spacy.load("../TrainedModel")

# Capture audio from microphone
with sr.Microphone() as source:
    print("Speak something:")
    audio = recognizer.listen(source, 15)

# Convert speech to text
try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
    main(text, nlp)  # Call the main function with the recognized text
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError as e:
    print(f"Request error: {e}")
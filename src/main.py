import speech_recognition as sr
from datetime import datetime
import os

recognizer = sr.Recognizer()

notes_folder = "notes"

if not os.path.exists(notes_folder):
    os.makedirs(notes_folder)

with sr.Microphone() as source:
    print("Speak your note...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{notes_folder}/note_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(text)

    print("Note saved:", filename)

except sr.UnknownValueError:
    print("Could not understand the audio")

except sr.RequestError:
    print("Speech recognition service unavailable") 

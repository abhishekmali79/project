import speech_recognition as sr
from translator import translate_

# Initialize the recognizer
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")
    # Adjust for ambient noise levels
    r.adjust_for_ambient_noise(source, duration=0.2)
    # Listen for the user's input
    audio = r.listen(source)

try:
    # Use Google Web Speech API to recognize the audio
    text = r.recognize_google(audio)
    translate_(text)
    print("You said:", text)
except sr.UnknownValueError:
    # Error handling for unrecognizable speech
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    # Error handling for API connection issues
    print(f"Could not request results; {e}")


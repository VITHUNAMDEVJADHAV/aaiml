import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load audio file
with sr.AudioFile('speech.wav') as source:
    audio_data = recognizer.record(source)

# Recognize speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcription: " + text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")


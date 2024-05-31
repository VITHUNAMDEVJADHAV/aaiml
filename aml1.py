import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as the source
with sr.Microphone() as source:
    print("Adjusting for ambient noise, please wait...")
    recognizer.adjust_for_ambient_noise(source, duration=10)
    print("Listening...")
    audio_data = recognizer.listen(source)

# Recognize speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcription: " + text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")

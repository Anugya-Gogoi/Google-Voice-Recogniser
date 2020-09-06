import speech_recognition as sr
import pyttsx3

rec=sr.Recognizer()
mic=sr.Microphone(device_index=1)

with mic as source:
    audio=rec.listen(source)

def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('Google says {}'.format(message))
    engine.runAndWait()

print(rec.recognize_google(audio))
speak(rec.recognize_google(audio))

import speech_recognition as sr
from pyaudio import *

reconhecedor = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        audio = reconhecedor.listen(source)
        print(reconhecedor.recognize_google(audio, language = "pt-br"))
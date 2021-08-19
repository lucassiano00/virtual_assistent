from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core
from nlu.classfier import classify
import sys

# Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def temp():

 while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            speak(core.SystemInfo.get_weather(text))
            break


def evaluate(text):
    #Reconhecer entidade do texto. 
    entity = classify(text)
    if text != "":
        if entity == 'time|getTime':
            speak(core.SystemInfo.get_time())
        elif entity == 'time|getDate':
            speak(core.SystemInfo.get_date())

        # Abrir programas
        elif entity == 'open|notepad':
            speak('Abrindo o bloco de notas')
            os.system('notepad.exe')
        elif entity == 'open|chrome':
            speak('Abrindo o google chrome')
            os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')

        # Previsão do tempo
        elif entity == 'weather|getWeather':
            speak('Qual cidade?')
            temp()
        # Saudações    
        elif entity == 'hello|getHello':
            speak('Olá, tudo bem?')

        elif entity == 'farewells|getFarewells':
            speak('Até logo')
            sys.exit()

    print('Text: {}  Entity: {}'.format(text, entity))

# Reconhecimento de fala

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do reconhecimento de fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            evaluate(text)

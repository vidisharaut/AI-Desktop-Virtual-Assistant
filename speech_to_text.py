import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r"C:\Users\rvid2\Documents\My Projects\AI Desktop Assistant\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000,input=True, frames_per_buffer=8192) 
stream.start_stream()

def s2t():
    while True:
        data = stream.read(4096)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            text = f"{text[14:-3]}"
            return text
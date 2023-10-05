#import re
#import random
import pyttsx3
import re

import threading
import time

from vosk import Model, KaldiRecognizer
import pyaudio
import json

import psutil

class EngineProject:

    def __init__(self):

        self.assistant_name_normal = "Aurora"
        self.assistant_name_advanced = "Forex"
        self.user_name = "Nicolás"
        self.command_level_normal = "normal"
        self.command_level_advanced = "advanced"
        self.model = Model(r"D:\Proyectos\Project Aurora\Aurora_project\v-model-small-es-0.42")
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.active = False  # Indica si el asistente está activo o no
        self.waiting_for_input = False

        #TESTEO DE RAM
        #Variable de rastreo de memoria:
        self.max_memory_used = 0

        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=4096)#tamaño anterior < 16384
        self.stream.start_stream()

        #pyTTSx3:
        self.tts_engine = pyttsx3.init()
        # Obtiene todas las voces disponibles
        voices = self.tts_engine.getProperty('voices')

        # Selecciona la voz predeterminada
        self.tts_engine.setProperty('voice', voices[2].id)  # Cambia el índice si es necesario

        # Ajusta la velocidad (rate)
        rate = self.tts_engine.getProperty('rate')  # Obtiene la velocidad actual
        self.tts_engine.setProperty('rate', 145)  # Cambia nuevo_rate al valor deseado

    def speak(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    #TESTEO DE RAM
    #metodo para convertir memoria en MB
    def get_memory_usage(self):
        process = psutil.Process()
        return process.memory_info().rss / (1024 * 1024)  # Convertir a MB

    def activate_assistant(self):
        print("Escuchando activacion")
        while True:
            data = self.stream.read(4896)
            if self.recognizer.AcceptWaveform(data):
                text = self.recognizer.Result()
                recognized_text = text[14:-3].lower()
                #print(recognized_text)
                #TESTEO DE RAM
                #COMPRUEBA RAM AL INICICAR ASISTENTE
                memory_at_activation = self.get_memory_usage()
                print(f"Uso de memoria al activar el asistente: {memory_at_activation} MB")

                if recognized_text == self.assistant_name_advanced.lower():
                    self.command_level = self.command_level_advanced
                    self.active = True
                    print(f"Sistema activado en modo {self.command_level} y escuchando...")
                    engine.command_engine()
                    self.active = False
                    break

                elif recognized_text == self.assistant_name_normal.lower():
                    self.command_level = self.command_level_normal
                    self.active = True
                    print(f"Sistema activado en modo {self.command_level} y escuchando...")
                    engine.command_engine()
                    #TESTEO DE RAM
                    # Medir la memoria al finalizar un comando
                    memory_after_command = self.get_memory_usage()
                    print(f"Uso de memoria al finalizar un comando: {memory_after_command} MB")
                    self.active = False
                    break
                    #TESTEO DE RAM
                    #Calcular la memoria máxima utilizada durante este período
                    max_memory_used_in_period = memory_after_command - memory_at_activation
                    if max_memory_used_in_period > self.max_memory_used:
                        self.max_memory_used = max_memory_used_in_period

                if not self.active:
                    print(f"Memoria máxima utilizada desde la activación hasta el comando: {self.max_memory_used} MB")
                    print("Vuelta a Escuchando activacion")

    def command_engine(self):
        while self.active:
            data = self.stream.read(4896)
            if self.active:
                if self.recognizer.AcceptWaveform(data):
                    text = self.recognizer.Result()
                    recognized_text = text[14:-3].lower()
                    print(recognized_text)
                    if self.command_level == self.command_level_normal:
                        self.command_normal_handle(recognized_text)
                    elif self.command_level == self.command_level_advanced:
                        self.command_advanced_handle(recognized_text)

    def command_normal_handle(self, command):

        # Manejo de comandos normales (todos aquí):
        if self.command_level:

            if command == "hola":
                print(f"Hola {self.user_name}, un gusto poder ayudarte")
                self.speak("Hola "+self.user_name + ", un gusto poder ayudarte")
                self.activate_assistant()


    def command_advanced_handle(self, command):

        # Manejo de comandos avanzados(todos debajo)
        if self.command_level_advanced:
            print(f"Comando avanzado detectado: {command}")
            match = re.search(r'(necesito\s+tu\s+ayuda|ayuda\s+por\s+favor)', command)
            if match:
                print(f"Si, {self.user_name}!")
                self.activate_assistant()


engine = EngineProject()
print("Virtual Assistant - Aurora v0.5 alpha.")
engine.speak("Asistente de comandos de voz inicializado y listo para servir")
engine.activate_assistant()





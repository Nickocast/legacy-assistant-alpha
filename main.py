import random
import re

import threading
import time

import pyaudio
from vosk import Model, KaldiRecognizer
import pyttsx3

import psutil
import json

#Modulos del proyecto
from modules import module_DateTime, module_weather
from commands import commands


class EngineProject:

    #--- Inicializador de variables y requerimientos necesarios del sistema ---#
    def __init__(self):
        #variables del programa#
        self.assistant_name_normal = "Aurora"
        self.assistant_name_advanced = "Charlie"
        self.user_name = "Nicolás"
        self.command_level_normal = "normal"
        self.command_level_advanced = "advanced"
        self.recognize_failed = 0
        self.url = module_weather.url
        self.api_key = module_weather.api_key
        self.url_geo = module_weather.url_geo
        self.city = module_weather.city
        self.time_zone_UNIX = module_weather.time_zone_UNIX

        #Modelo de reconocimiento de lenguaje
        self.model = Model(r"D:\Proyectos\Project Aurora\Aurora_project\languajes_models\v-model-small-es-0.42")
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.active = False  # Indica si el asistente está activo o no
        self.waiting_for_input = False

        # TESTEO DE RAM
        # Variable de rastreo de memoria:
        self.max_memory_used = 0

        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=4096)
        self.stream.start_stream()

        # pyTTSx3:
        self.tts_engine = pyttsx3.init()
        # Obtiene todas las voces disponibles
        voices = self.tts_engine.getProperty('voices')

        # Selecciona la voz predeterminada
        self.tts_engine.setProperty('voice', voices[2].id)  # Cambia el índice si es necesario

        # Ajusta la velocidad (rate)
        rate = self.tts_engine.getProperty('rate')  # Obtiene la velocidad actual
        self.tts_engine.setProperty('rate', 145)  # Cambia nuevo_rate al valor deseado

    #--- Funciones de manejo de variables y Habla ---#
    def name_manager(self):
        name = self.user_name
        return name

    def speak(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    # TESTEO DE RAM
    # metodo para convertir memoria en MB
    def get_memory_usage(self):
        process = psutil.Process()
        memory_usage = process.memory_info().rss / (1024 * 1024)  # Convertir a MB
        return int(round(memory_usage, 1))

    #--- Activador del asistente ---#
    def activate_assistant(self):
        print("Escuchando activacion")
        while True:
            data = self.stream.read(4896)
            if self.recognizer.AcceptWaveform(data):
                text = self.recognizer.Result()
                recognized_text = text[14:-3].lower()
                print(recognized_text)
                # TESTEO DE RAM
                # COMPRUEBA RAM AL INICICAR ASISTENTE
                memory_at_activation = self.get_memory_usage()
                print(f"Uso de memoria al activar el asistente: {memory_at_activation} MB")

                if recognized_text == self.assistant_name_advanced.lower():
                    self.command_level = self.command_level_advanced
                    self.active = True
                    print(f"Sistema activado en modo {self.command_level} y escuchando...")
                    reply = random.choice(["¿En que te ayudo " + self.user_name + "?",
                                           "¿En que te puedo servir?",
                                           "Sí, " + self.user_name,
                                           "Sí, " + self.user_name + " Dime",
                                           "Sí, " + self.user_name + " Dime tu orden",
                                           "¿Que necesitas que realice?",
                                           "¿Que necesitas" + self.user_name + "?",
                                           "Dime tu orden" + self.user_name,
                                           "Dime, " + self.user_name])
                    self.speak(reply)
                    engine.command_engine()
                    self.active = False
                    break

                elif recognized_text == self.assistant_name_normal.lower():
                    self.command_level = self.command_level_normal
                    self.active = True
                    print(f"Sistema activado en modo {self.command_level} y escuchando...")
                    reply = random.choice(["¿En que te ayudo " + self.user_name + "?",
                                           "¿En que te puedo ayudar?",
                                           "¿En que te puedo ayudar " + self.user_name + "?",
                                           "¿Que necesitas?",
                                           "¿Que necesitas" + self.user_name + "?",
                                           "Dime" + self.user_name + " ¿En que te ayudo?",
                                           "Dime, " + self.user_name])
                    self.speak(reply)
                    engine.command_engine()
                    self.active = False
                    break
                    # TESTEO DE RAM
                    # Medir la memoria al finalizar un comando
                    memory_after_command = self.get_memory_usage()
                    print(f"Uso de memoria al finalizar un comando: {memory_after_command} MB")

                    # TESTEO DE RAM
                    # Calcular la memoria máxima utilizada durante este período
                    max_memory_used_in_period = memory_after_command - memory_at_activation
                    if max_memory_used_in_period > self.max_memory_used:
                        self.max_memory_used = max_memory_used_in_period

                # Saludo al inicio del programa si se realiza
                elif re.search(r'buenos días| buenos días aurora|'
                               r'buen día|buen día aurora|buenas tardes|'
                               r'buenas tardes aurora|buenas noches|'
                               r'buenas noches aurora', recognized_text, re.IGNORECASE):
                    greeting = recognized_text
                    self.speak(module_DateTime.initial_greetings(greeting, self.user_name))
                    self.active = False

                # Manejo de agradecimientos
                elif re.search(r'muchas gracias aurora|'
                               r'muchas gracias|'
                               r'gracias|'
                               r'gracias aurora|'
                               r'gracias por el favor aurora|'
                               r'gracias por el favor|'
                               r'gracias por hacerlo aurora|'
                               r'gracias por hacerlo', recognized_text, re.IGNORECASE):
                    tk = recognized_text
                    self.speak(commands.gratitude(tk, self.user_name))
                    print(commands.gratitude(tk, self.user_name))
                    self.active = False

                if not self.active:
                    print(f"Memoria máxima utilizada desde la activación hasta el comando: {self.max_memory_used} MB")
                    print("Escuchando activacion")

    #--- Motor de comandos ---#
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

    #--- Manejador de comandos Nivel Normal ---#
    def command_normal_handle(self, command):

        recognized = command
        #=#=#=#=#=#=# FUNCIONES FUNDAMENTALES #=#=#=#=#=#=#

        #--- Comando para olvidar pedido del comando ---#ORIGINAL
        if re.search(r'(olvídalo|olvídate|no importa|déjalo|'
                     r'no realices nada|no realice nada|no hagas nada|'
                     r'mejor no|nada gracias|nada|que te olvídes)', recognized, re.IGNORECASE):
            self.speak(commands.cut(self.name_manager()))
            self.active = False
            self.activate_assistant()

        ##########COMANDOS DE HORARIO Y FECHA##########
            # --- Comando  de hora actual ---#
        if re.search(r'(qué hora es|qué hora son|'
                         r'cuál es la hora|dime la hora|hora)', recognized, re.IGNORECASE):
                self.speak(module_DateTime.hour_now())
                self.active = False
                self.activate_assistant()

        # --- Comando de hora por país ---#
        """hour_country_pattern = re.search(r'(qué hora es en|qué hora son en|'
                    r'cuál es la hora en|dime la hora de|me la hora de) '
                    r'(' + '|'.join(re.escape(pais) for pais in module_DateTime.hour_zone.keys()) + ')',re.IGNORECASE)
        if hour_country_pattern.search(recognize):
                self.speak(module_DateTime.hour_for_country(recognize))
                self.active = False
                self.activate_assistant()"""

        #--- Comando de fecha actual ---#
        if re.search(r'(qué fecha tenemos hoy|me puedes informar la fecha de hoy|me puedes informar en que fecha estamos|'
                r'necesito saber la fecha de hoy|en qué fecha estamos'
                r'necesito saber en qué fecha estamos|necesito saber la fecha|'
                r'qué día es hoy|en qué día estamos|qué día es hoy)|día de hoy', recognized, re.IGNORECASE):
            self.speak(module_DateTime.date())
            self.active = False
            self.activate_assistant()

        #--- Comando de mes actual ---#
        if re.search(r'en qué mes estamos|que me estámos|que mes estamos|me puedes informar el mes en el que estamos'
                r'necesito saber el mes actual'
                r'necesito saber en qué mes estamos'
                r'qué mes estamos|mes actual|mesa actual|me actual|cuál es el mes actual', recognized, re.IGNORECASE):
            self.speak(module_DateTime.month_now())
            self.active = False
            self.activate_assistant()

        #--- Comando  de año actual ---#
        if re.search(r'(en qué año estamos|qué año es|'
                     r'dime el año actual|dime el año)', recognized, re.IGNORECASE):
            self.speak(module_DateTime.year_now())
            self.active = False
            self.activate_assistant()

        ##########COMANDOS DE CLIMATOLOGÍA##########
        #--- Comando para pedir el clima actual ---#
        if re.search(r'(cuál es la temperatura|cuántos grados está haciendo|cuál es el clima de hoy|'
                     r'cuál es el clima de hoy|qué temperatura hace|cuanta temperatura hace|qué temperatura anuncia hoy|'
                     r'cuántos grados hace|qué clima hace|cómo está el clima|cómo está afuera|cómo están afuera)', recognized, re.IGNORECASE):
            self.speak(module_weather.forecast_for_today(self.user_name, self.url, self.api_key, self.url_geo, self.city, self.time_zone_UNIX))
            self.active = False
            self.activate_assistant()

        if re.search(r'(esta frío|hace calor|tengo que usar campera|tengo que abrigarme|me abrigo)', recognized, re.IGNORECASE):
            self.speak(module_weather.coat_desicion(self.user_name, self.url, self.api_key, self.url_geo, self.city, self.time_zone_UNIX))
            self.active = False
            self.activate_assistant()


        else:
            self.recognize_failed += 1
            self.speak(commands.no_recognize_command(self.user_name))
            if self.recognize_failed >= 3:
                self.recognize_failed = 0
                self.active = False
                engine.activate_assistant()




    #--- Manejador de comandos Nivel Avanzado ---#
    def command_advanced_handle(self, command):

        recognized = command
        #=#=#=#=#=#=# FUNCIONES FUNDAMENTALES AVANZADAS #=#=#=#=#=#=#

        # --- Comando para olvidar pedido del comando ---#
        if re.search(r'(olvídalo|olvídate|no importa|déjalo|'
                     r'no realices nada|no realice nada|no hagas nada|'
                     r'mejor no)', recognized, re.IGNORECASE):
            self.speak(commands.cut(self.name_manager()))
            self.active = False
            self.activate_assistant()


engine = EngineProject()
print("Virtual Assistant - Proyecto Aurora v0.6.16 alpha.")
engine.activate_assistant()
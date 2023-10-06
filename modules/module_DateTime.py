import datetime
import re
import  random

#Diccionario de texto a número horario
mapeo_hora = {
    "cero": 0,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10,
    "once": 11,
    "doce": 12,
    "trece": 13,
    "catorce": 14,
    "quince": 15,
    "dieciséis": 16,
    "diecisiete": 17,
    "dieciocho": 18,
    "diecinueve": 19,
    "veinte": 20,
    "veintiuno": 21,
    "veintidós": 22,
    "veintitrés": 23,
    "veinticuatro": 24,
    "veinticinco": 25,
    "veintiséis": 26,
    "veintisiete": 27,
    "veintiocho": 28,
    "veintinueve": 29,
    "treinta": 30,
    "treinta y uno": 31,
    "treinta y dos": 32,
    "treinta y tres": 33,
    "treinta y cuatro": 34,
    "treinta y cinco": 35,
    "treinta y seis": 36,
    "treinta y siete": 37,
    "treinta y ocho": 38,
    "treinta y nueve": 39,
    "cuarenta": 40,
    "cuarenta y uno": 41,
    "cuarenta y dos": 42,
    "cuarenta y tres": 43,
    "cuarenta y cuatro": 44,
    "cuarenta y cinco": 45,
    "cuarenta y seis": 46,
    "cuarenta y siete": 47,
    "cuarenta y ocho": 48,
    "cuarenta y nueve": 49,
    "cincuenta": 50,
    "cincuenta y uno": 51,
    "cincuenta y dos": 52,
    "cincuenta y tres": 53,
    "cincuenta y cuatro": 54,
    "cincuenta y cinco": 55,
    "cincuenta y seis": 56,
    "cincuenta y siete": 57,
    "cincuenta y ocho": 58,
    "cincuenta y nueve": 59
}

#Obtengo la fecha y la hora actual
now = datetime.datetime.now()

#accedo a los componentes de forma individual
current_year = now.year
current_month = now.month
current_day = now.day
current_hour = now.strftime("%H:%M")

def initial_greetings(greeting, user_name):
    name = user_name
    if re.search(r'buenos días|buenos días aurora|buen día|buen día aurora', greeting, re.IGNORECASE):
        saludo = random.choice(["Buenos días " +name, "Hola " +name, "Buen día "+name])
        return saludo
    elif re.search(r'buenas tardes|buenas tardes aurora', greeting, re.IGNORECASE):
        saludo = random.choice(["Buenas tardes "+name, "Hola "+name])
        return saludo
    elif re.search(r'buenas noches|buenas noches aurora', greeting, re.IGNORECASE):
        saludo = random.choice(["Buenas noches "+name, "Hola "+name])
        return saludo


#la funcion se ejecuta pero devuelve valores 0 en los print de minutos y hora
def handle_hour_in_words(hour_words):
    print(hour_words)
    try:
        hour_words = hour_words.replace(" y ", " ").replace(" ", "")

        words = hour_words.split()
        hour_f = mapeo_hora.get(words[0], 0)
        minutes_f = sum(mapeo_hora.get(word, 0) for word in words[1:])

        print("Horas:", hour_f)
        print("Minutos:", minutes_f)

        # Obtener la hora actual
        current_time = datetime.datetime.now()

        # Crear la hora objetivo
        target_time = current_time.replace(hour=hour_f, minute=minutes_f)

        # Calcular la diferencia de tiempo en minutos
        time_difference = (target_time - current_time).total_seconds() / 60

        # Imprimir los minutos faltantes
        if time_difference > 0:
            reply = f"Faltan {int(time_difference)} minutos para que sean las {hour_words}"

        else:
            reply = f"Ya son más de las {hour_words}"

            return reply

    except Exception as e:
        print("Error:", e)
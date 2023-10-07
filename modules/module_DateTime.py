import datetime
import re
import pytz
import random

# ----------Diccionario de HORA----------#
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

# ----------Diccionario de MESES----------#
meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

# ----------Diccionario de ZONA HORARIA----------#
hour_zone = {
    # --------Sur-América--------#
    'Argentina': 'America/Argentina/Buenos_Aires',
    'Bolivia': 'America/La_Paz',
    'Brasil': 'America/Sao_Paulo',
    'Chile': 'America/Santiago',
    'Colombia': 'America/Bogota',
    'Ecuador': 'America/Guayaquil',
    'Guyana': 'America/Guyana',
    'Paraguay': 'America/Asuncion',
    'Perú': 'America/Lima',
    'Uruguay': 'America/Montevideo',
    'Venezuela': 'America/Caracas',

    # --------América central--------#
    'Costa Rica': 'America/Costa_Rica',
    'El Salvador': 'America/El_Salvador',
    'Guatemala': 'America/Guatemala',
    'Honduras': 'America/Tegucigalpa',
    'Nicaragua': 'America/Managua',
    'Panamá': 'America/Panama',

    # --------Norte América--------#
    'Canadá': 'America/Toronto',
    'Estados Unidos': 'America/New_York',
    'México': 'America/Mexico_City'
}

# Obtengo la fecha y la hora actual
now = datetime.datetime.now()

# Accedo a los componentes de forma individual
current_year = now.year
print(current_year)
current_month = now.month
current_day = now.day
current_hour = now.strftime("%H:%M")


# Manejo de comandos de DateTime
def initial_greetings(greeting, user_name):
    name = user_name
    if re.search(r'buenos días|buenos días aurora|buen día|buen día aurora', greeting, re.IGNORECASE):
        saludo = random.choice([f"Buenos días {name}", f"Hola {name}", f"Buen día {name}"])
        return saludo
    elif re.search(r'buenas tardes|buenas tardes aurora', greeting, re.IGNORECASE):
        saludo = random.choice([f"Buenas tardes {name}", f"Hola {name}"])
        return saludo
    elif re.search(r'buenas noches|buenas noches aurora', greeting, re.IGNORECASE):
        saludo = random.choice([f"Buenas noches {name}", f"Hola {name}"])
        return saludo


def hour_now():
    hour_now = random.choice([f"Son las {current_hour}",
                              f"Es la hora {current_hour}",
                              f"La hora es {current_hour}"])
    return hour_now


def date():
    day = str(current_day)
    month = meses.get(current_month, "Mes no reconocido")
    date_now = random.choice([f"Hoy es {day} de {month}",
                              f"{day} de {month}",
                              f"El día de hoy es {day} de {month}",
                              f"La fecha actual es {day} de {month}"])
    return date_now


def month_now():
    month = meses.get(current_month, "Mes no reconocido")
    month_reply = random.choice([f"El mes actual es {month}",
                                 f"Estamos en el mes de {month}",
                                 f"Estamos en {month}",
                                 f"Estamos en pleno {month}"])

    return month_reply


def year_now():
    year = current_year
    year_reply = random.choice([f"Estamos en el año {year}",
                                f"Estamos en el {year}",
                                f"El año corriente es {year}",
                                f"El año en curso es {year}",
                                f"Nos encontramos en el año {year},"
                                f"Estamos viviendo en el año {year}"])
    return year_reply


def hour_for_country(command):
    # Busca el país dentro del parámetro

    country_match = re.compile(
        r'(qué hora es en|qué hora son en|'
        r'cuál es la hora en|dime la hora de|me la hora de) (' + '|'.join(
            re.escape(pais) for pais in hour_zone.keys()) + ')', command, re.IGNORECASE)

    if country_match:
        # Obtengo el país de la expresión re.
        country = country_match.group(2).capitalize()

        if country in hour_zone:
            # Busca la zona horaria correspondiente
            target_timezone = hour_zone.get(country, '')

            print(f"la hora de ese pais es {target_timezone}")
            reply = random.choice([f"En {country}, ahora mismo deben ser alrededor de las {target_timezone}",
                                   f"La hora en {country}, son las {target_timezone}",
                                   f"De acuerdo a la diferencia horaria, en {country} deberían ser aproximadamente las {target_timezone}.",
                                   f"La hora actual de {country} es {target_timezone}",
                                   f"La hora local en {country} en este momento, son las {target_timezone}"])

            return reply

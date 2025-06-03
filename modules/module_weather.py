import json
import random

import requests
import datetime
import pytz

dictionary_1 = {
    "despejado": "haya cielo despejado",
    "soleado": "esté soleado",
    "mayormente despejado": "esté mayormente despejado",
    "algunas nubes": "haya nubes dispersas",
    "nublado": "esté nublado",
    "parcialmente nublado": "esté parcialmente nublado",
    "lluvia": "haya lluvia",
    "chubascos": "algunos chubascos en la zona",
    "tormentas": "haya tormentas",
    "nieve": "nieve",
    "neblina": "haya neblina",
    "niebla": "haya niebla",
    "nubes dispersas": "hayan algunas nubes dispersas",
    "llovizna": "haya llovizna",
    "aguacero": "haya aguacero",
    "granizo": "granize",
    "nubes": "haya algunas nubes",
    "nubes rotas": "esté cubierto de nubes en un rango del 50 a 70 por ciento",
    "viento": "haya viento",
    "tornado": "probabilidades de tornados en la zona",

}
# Variables API OpenWeather
api_key = "x"
url_geo = "http://api.openweathermap.org/geo/1.0/direct?"
url = "http://api.openweathermap.org/data/2.5/forecast?"
city = "x"
lang = "es"

# Variables modulo
morning = range(6, 12)
afternoon = range(12, 18)
evening = list(range(18, 24) and list(range(0, 6)))

# Obtiene la hora actual en la zona horaria de Argentina
local_timezone = pytz.timezone('America/Argentina/Buenos_Aires')
current_time = datetime.datetime.now(local_timezone)
current_timestamp = current_time.tzinfo

# Convierte la hora actual a una marca de tiempo Unix
time_zone_UNIX = int(current_time.timestamp())


def forecast_for_today(url, api_key, url_geo, city, time_zone_UNIX):
    # Realiza la solicitud de geolocalización para obtener las coordenadas
    url_city_location = f"{url_geo}q={city}&limit=1&appid={api_key}"
    city_confirmed = requests.get(url_city_location)

    if city_confirmed.status_code == 200:
        # Extrae las coordenadas de la respuesta
        data = city_confirmed.json()

        if data:
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]

            # Utiliza las coordenadas para obtener el clima actual
            url_complete = f"{url}lat={latitude}&lon={longitude}&dt={time_zone_UNIX}&appid={api_key}&lang={lang}&units=metric"
            response = requests.get(url_complete)

            if response.status_code == 200:
                weather_data = response.json()

                first_element = weather_data["list"][0]
                second_element = weather_data["list"][0]["weather"][0]

                # Extrae la temperatura actual, la humedad y la presión del diccionario
                current_temperature = first_element['main']['temp_max']
                temperature = round(current_temperature)

                current_description = second_element['description']
                description = current_description

                current_feel = first_element['main']['feels_like']
                feel = round(current_feel)

                return (random.choice(
                    [f"Se espera para hoy, una temperatura máxima de {temperature} grados y {description}.",
                     f"Para hoy se anuncia una máxima de {temperature} grados y {description}.",
                     f"Se pronostica una temperatura de {temperature} grados para hoy, con una sensación térmica de {feel} grados.",
                     f"Se espera para hoy una máxima de {temperature} grados, aunque podría variar a lo largo del "
                     f"día."]))

            else:
                # return "Error en la solicitud de clima para hoy."
                return "Error en la solicitud de clima para hoy."
        else:
            # return "No se encontraron coordenadas para la ubicación especificada."
            return "No se encontraron coordenadas para la ubicación especificada."
    else:
        # return "Error en la solicitud de geolocalización."
        return "Error en la solicitud de geolocalización."


def coat_desicion(name, url, api_key, url_geo, city, time_zone_UNIX):
    url_city_location = f"{url_geo}q={city}&limit=1&appid={api_key}"
    city_confirmed = requests.get(url_city_location)

    if city_confirmed.status_code == 200:
        # Extrae las coordenadas de la respuesta
        data = city_confirmed.json()

        if data:
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]

            # Utiliza las coordenadas para obtener el clima actual
            url_complete = f"{url}lat={latitude}&lon={longitude}&dt={time_zone_UNIX}&appid={api_key}&lang={lang}&units=metric"
            response = requests.get(url_complete)

            if response.status_code == 200:
                weather_data = response.json()

                # print(json.dumps(weather_data, indent=4))
                first_element = weather_data["list"][0]
                current_temperature = first_element['main']['feels_like']
                temperature = round(current_temperature)

                if temperature > 20:
                    return random.choice(["No será necesario un abrigo, hará calor.",
                                          f" Hará calor {name}, no será necesario un abrigo,.",
                                          "No necesitarás un abrigo, tendrás calor.",
                                          f"Tendrás calor {name}, no necesitarás un abrigo.",
                                          "No necesitas abrigarte por ahora.",
                                          f"Por ahora {name}, no necesitas abrigarte."])
                elif temperature > 10:
                    return random.choice(
                        ["No necesitas un abrigo, está lo suficientemente cálido para usar ropa ligera.",
                         f"Está lo suficientemente cálido para usar ropa ligera, no necesitas un abrigo {name}.",
                         "El clima está agradable, estaría bien con ropa ligera",
                         f"estaría bien con ropa ligera {name}, el clima está agradable.",
                         "No hace falta un abrigo",
                         f"No hace falta un abrigo {name}",
                         "No deberías preocuparte por un abrigo, la temperatura está agradable.",
                         f"No deberías preocuparte por un abrigo {name}, la temperatura está agradable.",
                         "Usar ropa ligera será suficiente, el clima está templado.",
                         f"El clima está templado, con ropa ligera será suficiente {name}"])
                else:
                    return random.choice(["Definitivamente, necesitás un abrigo.",
                                          f"Necesitarás un abrigo para cuidarte del frio {name}.",
                                          "Será esencial que lleves un abrigo para mantenerte cálido.",
                                          f"Lleva un abrigo para mantenerte cálido {name}, está frio.",
                                          "No dudes de usar un abrigo, el clima está frío.",
                                          f"El clima está frío, no dudes de usar un abrigo {name}.",
                                          "Te recomiendo llevar un abrigo, está bastante frío.",
                                          f"Está bastante frío, te recomiendo llevar un abrigo {name}.",
                                          "Sin duda, un abrigo será tu mejor aliado para mantener el calor.",
                                          f"Un abrigo será tu mejor aliado para mantener el calor {name}.",
                                          "La temperatura es baja, así que asegúrate de llevar un abrigo contigo.",
                                          f"Asegúrate de llevar un abrigo contigo, la temperatura es baja {name}."])




        else:
            # return "No se encontraron coordenadas para la ubicación especificada."
            return "No se encontraron coordenadas para la ubicación especificada."
    else:
        # return "Error en la solicitud de geolocalización."
        return "Error en la solicitud de geolocalización."


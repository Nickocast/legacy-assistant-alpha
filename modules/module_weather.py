import json
import random

import requests
import datetime
import pytz

dictionary_1 = {
    "despejado": "",
    "soleado": "",
    "mayormente despejado": "",
    "algunas nubes": "con nubes dispersas",
    "nublado": "",
    "parcialmente nublado": "",
    "lluvia": "",
    "chubascos": "",
    "tormentas": "",
    "nieve": "",
    "neblina": "",
    "niebla": "",
    "nubes dispersas": "",
    "llovizna": "",
    "aguacero": "",
    "granizo": "",
    "nubes rotas": "",
    "viento": "",
    "tornado": "",

}

api_key = "a810ccb0b9cb5ba0b21f49978a642466"
url_geo = "http://api.openweathermap.org/geo/1.0/direct?"
url = "http://api.openweathermap.org/data/2.5/forecast?"
city = "General Fotheringham, Córdoba, Argentina"
lang = "es"

# Obtén la hora actual en la zona horaria de Argentina
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

                # print(json.dumps(weather_data, indent=4))
                first_element = weather_data["list"][0]
                second_element = weather_data["list"][0]["weather"][0]
                # print(json.dumps(weather_data, indent=4))
                # print(second_element)

                # Extrae la temperatura actual, la humedad y la presión del diccionario
                current_temperature = first_element['main']['temp_max']
                temperature = round(current_temperature)

                current_description = second_element['description']
                description = current_description

                current_feel = first_element['main']['feels_like']
                feel = round(current_feel)
                # current_humidity = weather_data["humidity"]
                # current_pressure = weather_data["pressure"]

                print(random.choice(
                    [f"Se espera una temperatura máxima de {temperature} grados y {description}.",
                     f"Se espera una máxima de {temperature} grados y {description}.",
                     f"Está haciendo una temperatura de {temperature} grados, con una sensación térmica de {feel} grados.",
                     f"Se espera para hoy una máxima de {temperature} grados, aunque podría variar a lo largo del "
                     f"día.",
                     f"Hay ",
                     f"Se espera que haya "]))

            else:
                # return "Error en la solicitud de clima para hoy."
                print("Error en la solicitud de clima para hoy.")
        else:
            # return "No se encontraron coordenadas para la ubicación especificada."
            print("No se encontraron coordenadas para la ubicación especificada.")
    else:
        # return "Error en la solicitud de geolocalización."
        print("Error en la solicitud de geolocalización.")


forecast_for_today(url, api_key, url_geo, city, time_zone_UNIX)

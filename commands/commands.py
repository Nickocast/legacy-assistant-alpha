import random
import re
from modules import module_DateTime


# Comandos de corte y agradecimiento
def cut(user_name):
    name = user_name
    reply = random.choice([f"Bueno {name}",
                           "Okey",
                           "Entendido, estaré aquí si me necesita",
                           f"Entendido, {name}, estaré aquí si me necesita"])
    return reply


def gratitude(tk, user_name):
    name = user_name
    reply = random.choice([f"De nada {name}",
                           f"de nada {name}, estaré aquí si me necesitas de nuevo",
                           "estaré aquí si me necesitas de nuevo",
                           "no fue nada, llámame si necesitas algo",
                           "Llámame si necesitas algo más",
                           "Solo hago mi tarea",
                           f"No fue nada, solo cumplo mis funciones. {name}",
                           "De nada, estoy aquí para ayudarte",
                           f"De nada {name}, estoy aquí para ayudarte"])
    return reply

# Comandos

import random
import re

# --- Comandos de corte, agradecimiento y comando no interpretado ---#
def cut(user_name):
    name = user_name
    reply = random.choice([f"Bueno {name}",
                           "Okey",
                           "Entendido, estaré aquí si me necesitas",
                           f"Entendido, {name}, estaré aquí si me necesitas",
                           "Está bien"])
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


def no_recognize_command(user_name):

    reply = random.choice([f"No pude entender lo que me dices {user_name}",
                           "No entendí lo que me estás pidiendo",
                           f"No entendí lo que me pides {user_name}",
                           "No entedí",
                           f"No te entendí {user_name}",
                           f"No comprendo lo que me quisiste pedir"])
    return reply

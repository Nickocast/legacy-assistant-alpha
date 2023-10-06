import datetime
from modules import module_DateTime

# Objeto simulado para el motor del asistente (puedes usar uno real si es necesario)
class MockEngine:
    def speak(self, text):
        print("Asistente habla:", text)

hour_f = 17
minutes_f = 00
# Simula el comando que normalmente recibirías por voz
simulated_command = "cuánto falta para que sean las dieciocho y treinta"

# Llama a la función handle_hour_in_words con la entrada simulada y el motor simulado
engine = MockEngine()
module_DateTime.handle_hour_in_words(simulated_command)
print(module_DateTime.handle_hour_in_words())
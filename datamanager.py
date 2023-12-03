import time
import random
from eventos import EventManager  # Acá se importa la clase EventManager del archivo brindado eventos.py

class RealTimeDataManager:
    def __init__(self, event_manager):
        self.data = {"temperatura": 25.0, "humedad": 60.0}  # Se inicializan los datos
        self.event_manager = event_manager  # Se almacena la instancia de EventManager en event_manager

    def start_real_time_updates(self):
        # En este ciclo se generan actualizaciones de los datos, esto en tiempo real
        while True:
            time.sleep(3)  # Se settea el tiempo de actualizaciones a 3 segundos
            self.generate_real_time_data()  # Como el comando lo dice, se utiliza para generar  y notificar los datos actualizados
    
    def generate_real_time_data(self):
        # Los siguientes dos comandos se encargan de actualizar los valores de temperatura y humedad de manera aleatoria
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)
        self.event_manager.notify("data_updated", self.data)  # Se notifican los cambios a los suscriptores

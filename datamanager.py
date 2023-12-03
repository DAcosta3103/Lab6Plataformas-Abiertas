import time
import random
from eventos import EventManager  # Importa la clase EventManager de eventos.py

class RealTimeDataManager:
    def __init__(self, event_manager):
        self.data = {"temperatura": 25.0, "humedad": 60.0}  # Inicializa los datos.
        self.event_manager = event_manager  # Almacena la instancia de EventManager.

    def start_real_time_updates(self):
        # Comienza a generar actualizaciones de datos en tiempo real.
        while True:
            time.sleep(3)  # Espera 3 segundos entre actualizaciones.
            self.generate_real_time_data()  # Genera y notifica los datos actualizados.

    def generate_real_time_data(self):
        # Actualiza los valores de temperatura y humedad de manera aleatoria.
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)
        self.event_manager.notify("data_updated", self.data)  # Notifica a los suscriptores del cambio.

from eventos import EventManager  # Se importa la clase EventManager del archivo eventos.py
from datamanager import RealTimeDataManager  # Se importa la clase RealTimeDataManager del archivo datamanager.py
import threading  # Importa el módulo threading para ejecutar procesos en paralelo
import time  # Importa el módulo time para controlar el flujo del tiempo

def print_data(data):
    print(f"Datos en tiempo real actualizados: {data}")  # Se crea una función callback que imprime los datos actualizados

if __name__ == "__main__":
  manager = EventManager()  # Se crea una instancia de EventManager
  data_manager = RealTimeDataManager(manager)  # Se crea una instancia de RealTimeDataManager

  manager.subscribe("data_updated", print_data)  # Suscribe la función print_data al evento 'data_updated'

  update_thread = threading.Thread(target=data_manager.start_real_time_updates)  # Crea un hilo para las actualizaciones de datos
  update_thread.start()  # Inicia el hilo de actualizaciones

  try:
    # Bucle infinito para mantener el programa corriendo
      while True:  
          time.sleep(1)
  except KeyboardInterrupt:  # Captura la interrupción por teclado para terminar el programa
        print("\nPrograma terminado.")

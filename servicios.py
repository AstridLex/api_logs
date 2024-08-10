import requests
import json
from datetime import datetime

# Configuración del servicio
SERVICIO_NOMBRE = "Servicio3"  # Cambiar para cada servicio
API_URL = "http://localhost:5000/logs"
API_KEY = "clave_unica_servicio3"  # Cambiar para cada servicio

def generar_log():
    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "servicio": SERVICIO_NOMBRE,
        "nivel": "INFO",
        "mensaje": "Hoy comi puré."
    }
    return log

def enviar_log(log):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(log))
    if response.status_code == 200:
        print("Log enviado con éxito.")
    else:
        print(f"Error al enviar el log: {response.status_code}")

if __name__ == "__main__":
    log = generar_log()
    enviar_log(log)

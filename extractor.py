import os
import requests
from dotenv import load_dotenv

# 1. Cargar las variables del archivo .env al sistema
load_dotenv()


def obtener_datos_cripto():
    # 2. Traer la URL desde el entorno seguro
    url = os.getenv("API_URL")

    # 3. Definir qué queremos (Top 10 criptos en USD)
    parametros = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }

    print(f"Conectando a: {url}...")

    try:
        # 4. Hacer la petición 'GET' a la API
        respuesta = requests.get(url, params=parametros)

        # 5. Si la respuesta es 200 (OK), convertimos a JSON (diccionario de Python)
        respuesta.raise_for_status()
        datos = respuesta.json()

        print("¡Conexión exitosa!")
        return datos

    except Exception as error:
        print(f"Hubo un error en la extracción: {error}")
        return None


if __name__ == "__main__":
    resultado = obtener_datos_cripto()
    if resultado:
        # Imprimimos el nombre y precio de la primera cripto (Bitcoin)
        primera = resultado[0]
        print(f"Cripto: {primera['name']} | Precio actual: ${primera['current_price']}")
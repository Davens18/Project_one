# Crypto-Analysis-Pipeline 🚀

Proyecto de extracción y análisis de datos en tiempo real utilizando la API de CoinGecko, Python y Pandas.

## 📋 Descripción
Este proyecto automatiza la obtención de datos de las 10 principales criptomonedas del mercado. Realiza un proceso de ETL (Extract, Load, Transform) básico:
- **Extracción:** Consumo de API REST.
- **Transformación:** Limpieza de datos, manejo de valores nulos y filtrado de tendencias con Pandas.
- **Seguridad:** Gestión de variables de entorno para proteger endpoints.

## 🛠️ Tecnologías Utilizadas
* **Python 3.x**
* **Pandas:** Procesamiento de datos.
* **Requests:** Consumo de APIs.
* **Python-dotenv:** Gestión de variables de entorno.
* **Git/GitHub:** Control de versiones.

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Davens18/](https://github.com/Davens18/)[NOMBRE_DE_TU_REPO].git
2. **Configurar el entorno virtual:**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
4. **Variables de Entorno:**
   Crea un archivo .env en la raíz con:
   API_URL = [https://api.coingecko.com/api/v3/coins/markets](https://api.coingecko.com/api/v3/coins/markets)

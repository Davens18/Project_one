import pandas as pd
from extractor import obtener_datos_cripto


def procesar_datos():
    # 1. Traemos los datos crudos del script anterior
    datos_crudos = obtener_datos_cripto()

    if not datos_crudos:
        print("No hay datos para procesar.")
        return

    # 2. Convertir JSON a un DataFrame de Pandas (Tabla)
    df = pd.DataFrame(datos_crudos)

    # 3. Limpieza: Seleccionamos solo las columnas que nos interesan
    columnas_interes = ['name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']
    df_limpio = df[columnas_interes]

    # 4. Manejo de Nulos: Si alguna moneda no tiene precio, llenamos con 0
    df_limpio = df_limpio.fillna(0)

    # 5. Análisis: Filtrar monedas que hayan subido en las últimas 24h
    ganadoras = df_limpio[df_limpio['price_change_percentage_24h'] > 0]

    print("\n--- TOP 10 CRIPTOMONEDAS ---")
    print(df_limpio.head())

    print("\n--- MONEDAS CON TENDENCIA AL ALZA (24H) ---")
    print(ganadoras[['name', 'price_change_percentage_24h']])

    return df_limpio


if __name__ == "__main__":
    procesar_datos()
"""Funciones para limpieza de los dos datasets"""

def print_data(df):
    """Funcion para observación de datos"""
    print("Shape")
    print(df.shape)
    print("Verifico nulos")
    print(df.isna().sum())
    print("Veo los tipos de datos")
    print(df.dtypes)
    print("Veo las métricas de las casillas numerales")
    print(df.describe())
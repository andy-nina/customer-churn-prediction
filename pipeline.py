import pandas as pd
import sqlite3

def extraer_datos(ruta_csv):
    try:
        df = pd.read_csv(ruta_csv)
        print(f"Datos extraídos: {df.shape[0]} filas, {df.shape[1]} columnas")
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
def transformar_datos(df):
    try:
        df = df.copy()

        df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")
        df["TotalCharges"] = df["TotalCharges"].astype(float)

        df["Churn_flag"] = df["Churn"].map({"Yes": 1, "No": 0})

        print("Transformación completada")
        return df
    except Exception as e:
        print(f"Error en la transformación: {e}")
        return None

df = extraer_datos("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df = transformar_datos(df)

print(df[["TotalCharges", "Churn", "Churn_flag"]].head())
print(df["TotalCharges"].dtype)

def cargar_datos(df, nombre_db, nombre_tabla):
    try:
        conexion = sqlite3.connect(nombre_db)
        df.to_sql(nombre_tabla, conexion, if_exists="replace", index=False)
        conexion.close()
        print(f"Datos cargados en {nombre_db}, tabla '{nombre_tabla}'")
    except Exception as e:
        print(f"Error al cargar en la base de datos: {e}")

df = extraer_datos("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df = transformar_datos(df)
cargar_datos(df, "churn.db", "clientes")

conexion = sqlite3.connect("churn.db")
resultado = pd.read_sql("SELECT Churn, COUNT(*) AS clientes FROM clientes GROUP BY Churn", conexion)
conexion.close()
print(resultado)
import sqlite3
import pandas as pd

conexion = sqlite3.connect("churn.db")

query1 = """
SELECT
    Contract,
    COUNT(*) AS clientes,
    SUM(Churn_flag) AS fugas,
    ROUND(100.0 * SUM(Churn_flag) / COUNT(*), 1) AS tasa_churn_pct
FROM clientes
GROUP BY Contract
ORDER BY tasa_churn_pct DESC
"""

resultado1 = pd.read_sql(query1, conexion)


query2 = """
SELECT
    PaymentMethod,
    COUNT(*) AS clientes,
    SUM(Churn_flag) AS fugas,
    ROUND(100.0 * SUM(Churn_flag) / COUNT(*), 1) AS tasa_churn_pct
FROM clientes
GROUP BY PaymentMethod
ORDER BY tasa_churn_pct DESC
"""

resultado2 = pd.read_sql(query2, conexion)


query3 = """
SELECT
    PaymentMethod,
    Contract,
    COUNT(*) AS clientes,
    SUM(Churn_flag) AS fugas,
    ROUND(100.0 * SUM(Churn_flag) / COUNT(*), 1) AS tasa_churn_pct
FROM clientes
GROUP BY PaymentMethod,Contract
ORDER BY tasa_churn_pct DESC
"""

resultado3 = pd.read_sql(query3, conexion)

conexion.close()

print(resultado1)

print(resultado2)

print(resultado3)
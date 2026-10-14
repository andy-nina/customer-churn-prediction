import sqlite3
import pandas as pd

conexion = sqlite3.connect("churn.db")
df = pd.read_sql("SELECT * FROM clientes", conexion)
conexion.close()

y = df["Churn_flag"]
X = df.drop(columns=["customerID", "Churn", "Churn_flag"])
X = pd.get_dummies(X, drop_first=True)

print(X.shape)
print(y.value_counts())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Entrenamiento: {X_train.shape[0]} clientes")
print(f"Prueba: {X_test.shape[0]} clientes")

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

escalador = StandardScaler()
X_train_esc = escalador.fit_transform(X_train)
X_test_esc = escalador.transform(X_test)

modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train_esc, y_train)

predicciones = modelo.predict(X_test_esc)
print(f"Precision del modelo: {accuracy_score(y_test, predicciones):.1%}")

print("\nMatriz de confusion:")
print(confusion_matrix(y_test, predicciones))

print("\nReporte:")
print(classification_report(y_test, predicciones, target_names=["Se queda", "Se va"]))

coeficientes = pd.DataFrame({
    "variable": X.columns,
    "coeficiente": modelo.coef_[0]
}).sort_values("coeficiente", ascending=False)

print("\nVariables que MAS aumentan el riesgo de irse:")
print(coeficientes.head(6))

print("\nVariables que MAS reducen el riesgo de irse:")
print(coeficientes.tail(6))
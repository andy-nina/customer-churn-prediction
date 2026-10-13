# Customer Churn Prediction: Pipeline de datos y análisis

Pipeline ETL en Python y análisis SQL sobre datos de clientes de una empresa de telecomunicaciones, para entender quiénes abandonan el servicio (churn) y preparar los datos para un modelo predictivo.

## Problema de negocio
Retener a un cliente cuesta menos que conseguir uno nuevo. Este proyecto identifica qué segmentos de clientes concentran el abandono, para orientar acciones de retención.

## Dataset
Telco Customer Churn (Kaggle, IBM): 7,043 clientes y 21 variables (contrato, servicios, método de pago, antigüedad y cargos).

## Pipeline
CSV (Extract) -> Limpieza y transformación con pandas (Transform) -> SQLite (Load) -> Consultas SQL de análisis

### Transformaciones
- `TotalCharges` venía como texto: 11 clientes con 0 meses de antigüedad tenían un espacio en blanco. Se reemplazó por 0 (aún no se les había cobrado) y se convirtió a número.
- Se creó la columna `Churn_flag` (1 = se fue, 0 = se quedó) para facilitar el análisis y el modelo predictivo.

## Hallazgos
De 7,043 clientes, 1,869 abandonaron: una tasa de churn del **26.5%**.

**1. El tipo de contrato es el factor más fuerte.**

| Contrato | Clientes | Tasa de abandono |
|---|---|---|
| Mensual | 3,875 | 42.7% |
| 1 año | 1,473 | 11.3% |
| 2 años | 1,695 | 2.8% |

El 89% de las fugas (1,655 de 1,869) son de clientes con contrato mensual.

**2. El método de pago también marca diferencia.** Quienes pagan con cheque electrónico abandonan en un 45.3%, frente a 15% a 19% en los demás métodos.

**3. El segmento crítico.** Cruzando ambas variables, los clientes con **cheque electrónico y contrato mensual** abandonan en un 53.7%. Son 1,850 clientes (26% de la base) y explican el 53% de todas las fugas. El cheque electrónico sigue siendo el método con más abandono dentro de cada tipo de contrato, así que no se explica solo por el contrato.

**Recomendación:** una campaña de retención dirigida a este segmento (por ejemplo, incentivos para pasar a contrato anual o a pago automático) sería más eficiente que una campaña general.

## Limitaciones
- Los resultados muestran asociación, no causalidad.
- Algunos cruces tienen pocos clientes (por ejemplo, cheque por correo con contrato de 2 años tiene solo 3 fugas), por lo que sus porcentajes son poco confiables.

## Estructura del proyecto
- `pipeline.py`: ETL con funciones de extracción, transformación y carga (genera `churn.db`)
- `consultas.py`: consultas SQL de análisis de negocio
- `explorar.py`: exploración inicial del dataset

## Cómo ejecutarlo
```bash
pip install pandas
python pipeline.py
python consultas.py
```

## Próximos pasos
- Modelo de predicción de churn con scikit-learn
- Evaluación del modelo e importancia de variables
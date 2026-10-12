# Customer Churn Prediction: Pipeline de datos

Pipeline ETL en Python que prepara datos de clientes de una empresa de telecomunicaciones para analizar y predecir el abandono (churn).

## Problema de negocio
Retener a un cliente cuesta menos que conseguir uno nuevo. Este proyecto prepara los datos para identificar qué clientes tienen más probabilidad de irse.

## Dataset
Telco Customer Churn (Kaggle, IBM): 7,043 clientes y 21 variables (contrato, servicios, método de pago, antigüedad y cargos).

## Pipeline
CSV (Extract) -> Limpieza y transformación con pandas (Transform) -> SQLite (Load)

### Transformaciones
- `TotalCharges` venía como texto: 11 clientes con 0 meses de antigüedad tenían un espacio en blanco. Se reemplazó por 0 (aún no se les había cobrado) y se convirtió a número.
- Se creó la columna `Churn_flag` (1 = se fue, 0 = se quedó) para el modelo predictivo.

## Primer hallazgo
1,869 de 7,043 clientes abandonaron: una tasa de churn del **26.5%**.

## Cómo ejecutarlo
    pip install pandas
    python pipeline.py

## Próximos pasos
- Consultas SQL de análisis de negocio
- Modelo de predicción con scikit-learn
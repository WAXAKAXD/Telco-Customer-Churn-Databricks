# Notebooks — Data Engineering & Machine Learning

Esta carpeta contiene los notebooks desarrollados en
Databricks para el procesamiento, transformación,
análisis y predicción del abandono de clientes.

## Objetivo

Implementar un pipeline de datos de extremo a extremo
utilizando Apache Spark, Delta Lake, arquitectura
Medallion y Machine Learning.

## Estructura de notebooks

| Notebook | Descripción |
|---|---|
| 01_Exploracion_Datos | Exploración, procesamiento, entrenamiento y evaluación del modelo |
| 02_Procesar_Nuevos_Clientes | Procesamiento de nuevos archivos CSV y generación de predicciones |

## Arquitectura Medallion

### Bronze — Ingesta de datos

- Lectura de archivos CSV.
- Validación de la estructura de datos.
- Almacenamiento de datos originales.

### Silver — Limpieza y transformación

- Conversión de tipos de datos.
- Tratamiento de valores faltantes.
- Eliminación de registros duplicados.
- Generación de variables para Machine Learning.

### Gold — Datos procesados

- Preparación de variables predictoras.
- Generación de datos para análisis.
- Preparación de información para el modelo.

## Machine Learning

El proyecto utiliza un modelo de regresión logística
implementado mediante PySpark MLlib.

Variables predictoras:

- tenure
- MonthlyCharges
- Contract

La variable objetivo es ChurnLabel, que representa
la permanencia o abandono del cliente.

## Resultados del modelo

| Métrica | Resultado |
|---|---:|
| Accuracy | 78.42% |
| F1 Score | 77.41% |
| AUC ROC | 82.17% |

## Gestión del modelo

El modelo entrenado se registra mediante MLflow
y Unity Catalog, permitiendo reutilizarlo para
generar predicciones sobre nuevos clientes sin
necesidad de entrenarlo nuevamente.

## Automatización

El notebook de procesamiento de nuevos clientes
se ejecuta mediante Databricks Jobs y se integra
con la aplicación web desarrollada en Streamlit.

## Tecnologías utilizadas

- Python
- PySpark
- Apache Spark
- Delta Lake
- Databricks
- MLflow
- Unity Catalog
- Databricks Jobs

# Resultados — Telco Customer Churn

Esta carpeta documenta los resultados obtenidos
durante el procesamiento de datos, entrenamiento,
evaluación y ejecución de la plataforma de
predicción de abandono de clientes.

## 1. Resumen del experimento

| Parámetro | Valor |
|---|---|
| Dataset original | IBM Telco Customer Churn |
| Registros originales | 7,043 |
| Variables originales | 21 |
| Algoritmo | Regresión logística |
| Framework | PySpark MLlib |
| Proporción de entrenamiento | 80% |
| Proporción de evaluación | 20% |
| Semilla aleatoria | 42 |
| Gestión del modelo | MLflow |
| Entorno | Databricks Free Edition |

## 2. Métricas de evaluación

| Métrica | Valor decimal | Porcentaje |
|---|---:|---:|
| Accuracy | 0.7842 | 78.42% |
| F1 Score | 0.7741 | 77.41% |
| AUC ROC | 0.8217 | 82.17% |

Las métricas fueron obtenidas mediante la evaluación
del modelo sobre la partición de prueba del
dataset original.

### Accuracy

Representa la proporción de predicciones correctas
respecto al total de registros evaluados.

### F1 Score

Combina precisión y sensibilidad para evaluar
el desempeño de un clasificador.

En Spark, la métrica F1 del evaluador multiclase
corresponde al promedio ponderado por clase.

### AUC ROC

Evalúa la capacidad del modelo para distinguir
entre clientes que abandonan el servicio y
clientes que permanecen.

## 3. Distribución original de clientes

| Categoría | Clientes | Porcentaje |
|---|---:|---:|
| Permanencia | 5,174 | 73.46% |
| Abandono | 1,869 | 26.54% |
| Total | 7,043 | 100% |

Estos valores corresponden a las etiquetas
originales del conjunto de datos.

## 4. Resultados de predicción

El modelo entrenado fue utilizado para generar
predicciones sobre el dataset original completo.

| Predicción | Clientes | Porcentaje |
|---|---:|---:|
| Permanencia | 5,576 | 79.17% |
| Abandono | 1,467 | 20.83% |
| Total | 7,043 | 100% |

### Probabilidad promedio de abandono

26.52%

Este indicador representa el promedio de las
probabilidades de abandono estimadas por el modelo.

No debe confundirse con el porcentaje de clientes
clasificados como abandono.

## 5. Comparación de resultados

| Categoría | Etiqueta original | Predicción |
|---|---:|---:|
| Permanencia | 5,174 | 5,576 |
| Abandono | 1,869 | 1,467 |
| Total | 7,043 | 7,043 |

Las diferencias entre cantidades agregadas no
representan directamente el número de errores
de clasificación.

Para determinar falsos positivos y falsos negativos
se requiere una matriz de confusión.

Las predicciones sobre el dataset completo tampoco
constituyen una evaluación independiente, debido
a que incluyen registros utilizados para entrenar
el modelo.

## 6. Interpretación de los resultados

El modelo presenta capacidad para distinguir
entre clientes con diferentes probabilidades
de abandono.

El AUC ROC obtenido indica una capacidad de
discriminación superior a una clasificación
aleatoria.

Los resultados permiten explorar estrategias
de identificación de clientes potencialmente
vulnerables al abandono.

Sin embargo, las predicciones deben interpretarse
como estimaciones probabilísticas y no como
certezas sobre el comportamiento futuro.

## 7. Niveles de riesgo

La plataforma permite visualizar clientes
mediante categorías de riesgo:

- Riesgo bajo.
- Riesgo medio.
- Riesgo alto.

Estas categorías se determinan a partir de
las probabilidades estimadas por el modelo.

Los umbrales de clasificación deberán mantenerse
consistentes entre la aplicación web y el dashboard.

## 8. Resultados de automatización

Se realizó una ejecución exitosa del Job
Pipeline_Telco_App en Databricks.

| Parámetro | Resultado |
|---|---|
| Estado | Successful |
| Tiempo de ejecución observado | 2 min 32 s |
| Registros procesados | 7,043 |
| Procesamiento | Bronze, Silver y Gold |
| Inferencia | Modelo registrado en MLflow |

El tiempo corresponde a una ejecución observada
y no representa un promedio de rendimiento.

## 9. Pruebas de escalabilidad

Se propone evaluar el comportamiento de la
plataforma con diferentes volúmenes de datos.

| Registros | Estado |
|---:|---|
| 2,000 | Dataset sintético preparado |
| 7,043 | Procesamiento exitoso |
| 10,000 | Pendiente |
| 50,000 | Pendiente |
| 100,000 | Pendiente |
| 500,000 | Pendiente |
| 1,000,000 | Pendiente |
| 2,000,000 | Pendiente |
| 4,000,000 | Objetivo de escalabilidad |

### Indicadores de rendimiento

- Tiempo total de ejecución.
- Tiempo de procesamiento por capa.
- Registros procesados por segundo.
- Consumo de memoria.
- Tamaño de archivos de entrada y salida.
- Estabilidad del pipeline.
- Capacidad de visualización.
- Disponibilidad de recursos computacionales.

Las pruebas pendientes no constituyen resultados
experimentales obtenidos.

## 10. Archivos de resultados previstos

| Archivo | Descripción |
|---|---|
| model_metrics.csv | Métricas del modelo |
| predictions_summary.csv | Resumen de predicciones |
| confusion_matrix.csv | Matriz de confusión |
| performance_tests.csv | Pruebas de rendimiento |
| risk_distribution.csv | Distribución de riesgo |

Los archivos se incorporarán conforme se obtengan
y verifiquen los resultados correspondientes.

## 11. Limitaciones

- Dataset original de naturaleza ficticia.
- Modelo entrenado con tres variables predictoras.
- Validación externa pendiente.
- Capacidad máxima de procesamiento no determinada.
- Recursos limitados por Databricks Free Edition.
- Posibles diferencias en los umbrales de riesgo
  entre las interfaces de visualización.

## 12. Conclusiones

El proyecto demuestra la integración funcional
de ingeniería de datos, Machine Learning,
automatización y visualización mediante Databricks.

La implementación permite reutilizar un modelo
entrenado para generar predicciones sin repetir
el proceso de entrenamiento.

Los resultados constituyen una base para futuras
mejoras en precisión, escalabilidad, optimización
y validación con datos externos.

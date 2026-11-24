# Testing — Telco Customer Churn

Esta carpeta documenta la estrategia de pruebas
y validación de la plataforma de ingeniería de
datos y predicción de abandono de clientes.

## 1. Objetivo

Verificar el funcionamiento, integridad,
estabilidad y capacidad de procesamiento
de los componentes del sistema.

## 2. Tipos de pruebas

| Tipo | Objetivo |
|---|---|
| Funcionales | Verificar las funcionalidades del sistema |
| Calidad de datos | Validar la integridad de los registros |
| Integración | Comprobar la comunicación entre componentes |
| Machine Learning | Evaluar el comportamiento del modelo |
| Rendimiento | Medir tiempos y capacidad de procesamiento |
| Seguridad | Verificar permisos y protección de recursos |
| Regresión | Detectar errores después de modificaciones |

## 3. Pruebas de calidad de datos

| ID | Prueba | Resultado esperado |
|---|---|---|
| DQ-01 | Validación de columnas | 21 columnas compatibles |
| DQ-02 | Identificadores duplicados | Un registro por cliente |
| DQ-03 | Valores faltantes | Tratamiento según reglas definidas |
| DQ-04 | Tipos de datos | Conversión correcta |
| DQ-05 | Antigüedad del cliente | Valores enteros no negativos |
| DQ-06 | Cargos mensuales | Valores numéricos no negativos |
| DQ-07 | Tipo de contrato | Categorías compatibles |
| DQ-08 | Variable objetivo | Codificación binaria válida |
| DQ-09 | Archivo vacío | Rechazo controlado |
| DQ-10 | Columnas faltantes | Mensaje de validación |

## 4. Pruebas del pipeline ETL

### Bronze

- Verificar la lectura del archivo CSV.
- Validar la estructura de entrada.
- Comprobar el almacenamiento de registros.
- Verificar la creación de tablas Delta.

### Silver

- Verificar la eliminación de duplicados.
- Validar las conversiones de tipos de datos.
- Comprobar el tratamiento de valores faltantes.
- Validar la generación de ChurnLabel.

### Gold

- Verificar la preparación de variables.
- Comprobar la disponibilidad de datos procesados.
- Validar la compatibilidad con el modelo.
- Verificar la integridad de los resultados.

## 5. Pruebas de Machine Learning

| ID | Prueba | Resultado esperado |
|---|---|---|
| ML-01 | Carga del modelo registrado | Modelo disponible |
| ML-02 | Transformación de variables | Vector de características válido |
| ML-03 | Generación de predicciones | Valores binarios 0 o 1 |
| ML-04 | Probabilidades | Valores entre 0 y 1 |
| ML-05 | Integridad de resultados | Una predicción por registro válido |
| ML-06 | Categorías desconocidas | Comportamiento controlado |
| ML-07 | Reutilización del modelo | Inferencia sin reentrenamiento |
| ML-08 | Niveles de riesgo | Clasificación consistente |

## 6. Pruebas de integración

| ID | Componentes | Validación |
|---|---|---|
| INT-01 | Streamlit y Databricks Jobs | Inicio del procesamiento |
| INT-02 | Jobs y Notebooks | Ejecución del notebook |
| INT-03 | Notebooks y Unity Catalog | Acceso a los recursos |
| INT-04 | PySpark y Delta Lake | Lectura y escritura |
| INT-05 | PySpark y MLflow | Recuperación del modelo |
| INT-06 | Resultados y Streamlit | Visualización de indicadores |
| INT-07 | Streamlit y Volumes | Carga y recuperación de archivos |

## 7. Pruebas de la aplicación web

| ID | Prueba | Resultado esperado |
|---|---|---|
| APP-01 | Dataset original | Procesamiento de 7,043 registros |
| APP-02 | Carga de CSV compatible | Procesamiento correcto |
| APP-03 | Ejecución del pipeline | Inicio del Job |
| APP-04 | Estado de ejecución | Información del procesamiento |
| APP-05 | Indicadores | Resultados consistentes |
| APP-06 | Gráficas | Visualización correcta |
| APP-07 | Exportación | Archivo de resultados disponible |
| APP-08 | Archivo incompatible | Mensaje de error controlado |
| APP-09 | Archivo superior a 200 MB | Rechazo de carga |
| APP-10 | Ejecuciones consecutivas | Resultados independientes |

## 8. Pruebas de escalabilidad

Se propone incrementar progresivamente el volumen
de datos para evaluar el rendimiento del sistema.

| Prueba | Registros | Estado |
|---|---:|---|
| PERF-01 | 7,043 | Ejecución exitosa observada |
| PERF-02 | 2,000 | Dataset de prueba preparado |
| PERF-03 | 10,000 | Pendiente |
| PERF-04 | 50,000 | Pendiente |
| PERF-05 | 100,000 | Pendiente |
| PERF-06 | 500,000 | Pendiente |
| PERF-07 | 1,000,000 | Pendiente |
| PERF-08 | 2,000,000 | Pendiente |
| PERF-09 | 4,000,000 | Objetivo futuro |

### Indicadores de rendimiento

- Tiempo total de procesamiento.
- Registros procesados por segundo.
- Tiempo de inferencia.
- Consumo de memoria.
- Tamaño de los archivos.
- Tiempo de respuesta de la aplicación.
- Estabilidad de las ejecuciones.

Las pruebas de mayor volumen estarán sujetas
a los recursos disponibles en Databricks
Free Edition y a las limitaciones de la aplicación.

## 9. Pruebas de seguridad

- Verificar los permisos de Unity Catalog.
- Validar el acceso a los Volumes.
- Comprobar los permisos de ejecución del Job.
- Verificar el acceso al modelo registrado.
- Evitar la exposición de credenciales.
- Revisar los archivos antes de publicarlos.

## 10. Criterios de aceptación

Una ejecución se considera satisfactoria cuando:

- El archivo de entrada es compatible.
- El pipeline finaliza correctamente.
- Los registros cumplen las reglas de calidad.
- El modelo genera predicciones válidas.
- Las probabilidades se encuentran entre 0 y 1.
- Los resultados se almacenan correctamente.
- Los indicadores son consistentes.
- La aplicación permite consultar los resultados.

## 11. Resultados verificados durante el desarrollo

| Componente | Estado |
|---|---|
| Lectura del dataset original | Verificado |
| Procesamiento Bronze | Verificado |
| Procesamiento Silver | Verificado |
| Procesamiento Gold | Verificado |
| Entrenamiento del modelo | Verificado |
| Evaluación del modelo | Verificado |
| Registro del modelo en MLflow | Verificado |
| Recuperación del modelo | Verificado |
| Ejecución de Databricks Jobs | Verificado |
| Despliegue de Streamlit | Verificado |
| Pipeline desde la aplicación | Verificado con dataset original |
| Procesamiento masivo | Pendiente de evaluación |

## 12. Automatización de pruebas

Como trabajo futuro se propone incorporar:

- Pytest.
- Pruebas unitarias de Python.
- Pruebas de transformaciones PySpark.
- Validaciones automatizadas de esquemas.
- Pruebas de integración.
- GitHub Actions.
- Reportes automatizados de resultados.

## 13. Archivos previstos

| Archivo | Descripción |
|---|---|
| test_data_validation.py | Validación de datos |
| test_etl_pipeline.py | Pruebas del procesamiento ETL |
| test_model.py | Validación de predicciones |
| test_app.py | Pruebas de la aplicación |
| test_integration.py | Pruebas de integración |
| test_performance.py | Pruebas de rendimiento |

## 14. Estado actual

Las verificaciones realizadas durante el desarrollo
corresponden principalmente a pruebas manuales
y ejecuciones funcionales en Databricks.

Los casos de prueba y archivos propuestos en
este documento constituyen un plan de validación.

No representan una suite de pruebas automatizadas
implementada ni ejecutada en su totalidad.

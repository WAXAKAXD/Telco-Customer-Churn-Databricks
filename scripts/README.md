# Scripts — Telco Customer Churn

Esta carpeta está destinada a almacenar herramientas
auxiliares para la configuración, automatización,
validación y reproducción del proyecto.

## 1. Objetivo

Facilitar la ejecución y mantenimiento de la
plataforma mediante scripts reutilizables,
independientes de la interfaz gráfica.

## 2. Responsabilidades

- Configuración del entorno de trabajo.
- Preparación de recursos en Databricks.
- Validación de archivos CSV.
- Generación de datasets sintéticos.
- Automatización de tareas repetitivas.
- Exportación de resultados.
- Evaluación del rendimiento.
- Reproducción de experimentos.

## 3. Estructura prevista

| Script | Descripción |
|---|---|
| setup_environment.py | Configuración del entorno |
| setup_catalog.sql | Creación de recursos en Unity Catalog |
| validate_dataset.py | Validación de archivos CSV |
| generate_synthetic_data.py | Generación de datos sintéticos |
| run_pipeline.py | Ejecución programática del pipeline |
| export_results.py | Exportación de resultados |
| benchmark_pipeline.py | Evaluación del rendimiento |

Los nombres anteriores representan herramientas
auxiliares previstas para futuras implementaciones.

## 4. Configuración del entorno

La plataforma utiliza los siguientes componentes:

- Databricks Free Edition.
- Apache Spark.
- Python.
- PySpark.
- Delta Lake.
- MLflow.
- Unity Catalog.
- Databricks SDK.
- Streamlit.

Las dependencias específicas de la aplicación
se documentan en app/requirements.txt.

## 5. Recursos de Databricks

La configuración original del proyecto utiliza:

| Recurso | Nombre |
|---|---|
| Catálogo | workspace |
| Esquema | default |
| Volume | telco_churn |
| Tabla Bronze | bronze_telco |
| Tabla Silver | silver_telco |
| Tabla Gold | gold_telco |
| Tabla de predicciones | gold_predicciones |
| Modelo registrado | telco_churn_model |
| Versión del modelo | 1 |
| Job | Pipeline_Telco_App |

Estos nombres corresponden al entorno original
de desarrollo y pueden requerir modificaciones
al reproducir el proyecto en otro workspace.

## 6. Organización del almacenamiento

Ruta base utilizada durante el desarrollo:

    /Volumes/workspace/default/telco_churn/

Estructura de almacenamiento:

    telco_churn/
    ├── entradas/
    ├── resultados/
    └── mlflow_tmp/

### Entradas

Almacenamiento de archivos CSV utilizados
para generar nuevas predicciones.

### Resultados

Almacenamiento de los archivos generados
durante cada ejecución del pipeline.

### MLflow temporal

Directorio auxiliar para operaciones
relacionadas con la recuperación del modelo.

## 7. Generación de datos sintéticos

Se propone implementar un generador de datasets
compatibles con las 21 columnas del formato Telco.

El generador deberá permitir configurar:

- Cantidad de registros.
- Semilla aleatoria.
- Identificadores únicos.
- Distribución de contratos.
- Antigüedad de clientes.
- Cargos mensuales.
- Servicios contratados.
- Nombre del archivo de salida.

Los datos generados serán utilizados para pruebas
funcionales y de escalabilidad.

No deberán presentarse como registros de
clientes reales.

## 8. Pruebas de rendimiento

Se propone implementar herramientas para
evaluar diferentes volúmenes de procesamiento.

| Nivel | Registros |
|---|---:|
| Funcional | 2,000 |
| Básico | 10,000 |
| Intermedio | 100,000 |
| Avanzado | 500,000 |
| Escalabilidad | 1,000,000 |
| Big Data | 4,000,000 |

Las pruebas deberán registrar:

- Fecha de ejecución.
- Cantidad de registros de entrada.
- Cantidad de registros procesados.
- Tiempo total de ejecución.
- Tiempo por etapa del pipeline.
- Tamaño de archivos.
- Estado de ejecución.
- Errores detectados.

La capacidad máxima del sistema deberá
determinarse mediante pruebas experimentales.

## 9. Automatización del pipeline

El procesamiento actual se ejecuta mediante
Databricks Jobs.

Los parámetros principales son:

| Parámetro | Descripción |
|---|---|
| archivo_csv | Ruta del archivo de entrada |
| id_proceso | Identificador de ejecución |

La automatización auxiliar deberá reutilizar
el Job existente y el modelo registrado,
evitando duplicar la lógica de los notebooks.

## 10. Reproducibilidad

Para facilitar la reproducción del proyecto
se deberán documentar:

- Versiones de las dependencias.
- Configuración del entorno.
- Esquema de los datos.
- Parámetros de entrenamiento.
- Semillas aleatorias.
- Versión del modelo.
- Configuración de los Jobs.
- Permisos de acceso.
- Resultados experimentales.

## 11. Seguridad

Los scripts no deberán contener:

- Tokens de acceso.
- Contraseñas.
- Credenciales personales.
- Secretos de autenticación.
- Información confidencial.

Se deberán utilizar mecanismos de autenticación
y configuración seguros proporcionados por
Databricks.

## 12. Estado actual

El procesamiento principal se encuentra
implementado en los notebooks de Databricks
y en la aplicación Streamlit.

Esta carpeta establece la estructura para
incorporar herramientas auxiliares y mejorar
la reproducibilidad del proyecto.

Los scripts propuestos no representan
funcionalidades implementadas en su totalidad.

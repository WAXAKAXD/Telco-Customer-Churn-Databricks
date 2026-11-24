# Data — Telco Customer Churn

Esta carpeta documenta los conjuntos de datos utilizados
para el desarrollo, entrenamiento y pruebas de la
plataforma de predicción de abandono de clientes.

## 1. Dataset original

El proyecto utiliza el conjunto de datos IBM Telco
Customer Churn, disponible públicamente en Kaggle.

- Registros: 7,043
- Variables: 21
- Formato: CSV
- Dominio: Telecomunicaciones
- Tipo de problema: Clasificación binaria
- Variable objetivo: Churn
- Naturaleza: Datos de ejemplo de clientes ficticios

### Fuente

https://www.kaggle.com/datasets/blastchar/telco-customer-churn

### Archivo original

WA_Fn-UseC_-Telco-Customer-Churn.csv

## 2. Diccionario de datos

| Variable | Tipo | Descripción |
|---|---|---|
| customerID | String | Identificador único del cliente |
| gender | String | Género del cliente |
| SeniorCitizen | Integer | Indicador de adulto mayor |
| Partner | String | Indica si tiene pareja |
| Dependents | String | Indica si tiene dependientes |
| tenure | Integer | Antigüedad del cliente en meses |
| PhoneService | String | Servicio telefónico |
| MultipleLines | String | Múltiples líneas telefónicas |
| InternetService | String | Tipo de servicio de internet |
| OnlineSecurity | String | Servicio de seguridad en línea |
| OnlineBackup | String | Servicio de respaldo en línea |
| DeviceProtection | String | Protección de dispositivos |
| TechSupport | String | Soporte técnico |
| StreamingTV | String | Servicio de televisión |
| StreamingMovies | String | Servicio de películas |
| Contract | String | Tipo de contrato |
| PaperlessBilling | String | Facturación electrónica |
| PaymentMethod | String | Método de pago |
| MonthlyCharges | Double | Cargo mensual del cliente |
| TotalCharges | Double | Cargos acumulados |
| Churn | String | Indicador de abandono del cliente |

## 3. Distribución del dataset original

| Categoría | Clientes | Porcentaje |
|---|---:|---:|
| Permanencia | 5,174 | 73.46% |
| Abandono | 1,869 | 26.54% |
| Total | 7,043 | 100% |

Estos valores corresponden a las etiquetas originales
del dataset y no a las predicciones del modelo.

## 4. Limpieza y transformación

Durante la etapa Silver se realizan las siguientes
operaciones:

- Conversión de tipos de datos.
- Validación de registros.
- Eliminación de duplicados mediante customerID.
- Tratamiento de valores faltantes en TotalCharges.
- Asignación de cero a TotalCharges cuando corresponde
  a clientes con antigüedad de cero meses.
- Generación de la variable objetivo ChurnLabel.

### Codificación de la variable objetivo

| Churn | ChurnLabel |
|---|---:|
| No | 0 |
| Yes | 1 |

## 5. Variables utilizadas por el modelo

El modelo de regresión logística utiliza:

- tenure
- MonthlyCharges
- Contract

La variable Contract se transforma mediante
StringIndexer y OneHotEncoder.

Las variables predictoras se integran mediante
VectorAssembler para generar el vector de características.

## 6. Dataset sintético de prueba

Se generó un archivo adicional para comprobar la
capacidad de la aplicación de procesar nuevos clientes.

### Archivo

telco_prueba_2000.csv

### Características

- 2,000 registros sintéticos.
- 21 columnas compatibles con el dataset original.
- Identificadores independientes.
- Diferentes perfiles de clientes.
- Diferentes contratos, servicios y cargos mensuales.

Este conjunto de datos está destinado a pruebas
funcionales y no constituye evidencia de la precisión
del modelo sobre clientes reales.

## 7. Almacenamiento en Databricks

Los datos se administran mediante Unity Catalog,
Volumes y tablas Delta Lake.

| Capa | Contenido |
|---|---|
| Bronze | Datos originales |
| Silver | Datos limpios y transformados |
| Gold | Datos preparados para análisis y predicción |

## 8. Requisitos para nuevos archivos

Los archivos cargados mediante la aplicación deben:

- Utilizar formato CSV.
- Contener las 21 columnas esperadas.
- Mantener nombres de columnas compatibles.
- Utilizar identificadores únicos por cliente.
- Mantener categorías compatibles con el modelo.
- Respetar el límite de carga de la aplicación.

El límite actual de carga es de 200 MB por archivo.
La capacidad efectiva de procesamiento depende de
los recursos disponibles.

## 9. Escalabilidad

Se propone evaluar progresivamente el rendimiento
del pipeline con los siguientes volúmenes:

| Registros | Estado |
|---:|---|
| 7,043 | Validado con dataset original |


## 10. Consideraciones de uso

Los datos se utilizan con fines académicos,
experimentales y de desarrollo tecnológico.

Antes de redistribuir conjuntos de datos de terceros,
se deberán revisar sus licencias y condiciones de uso.

No se deben publicar datos personales, credenciales
ni información confidencial en este repositorio.

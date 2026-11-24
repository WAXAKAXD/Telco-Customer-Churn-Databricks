# Datos — Telco Customer Churn

| Dataset | Registros | Columnas | Uso |
|---|---:|---:|---|
| IBM original | 7043 | 21 | Entrenamiento y evaluación |
| Sintético | 2000 | 21 | Pruebas funcionales |
| Ejemplo mínimo | 20 | 4 | Prueba de inferencia |

## Archivos

- [Fuente original](original/README.md)
- [Dataset sintético](synthetic/telco_prueba_2000.csv)
- [Ejemplo mínimo](examples/sample_input.csv)
- [Diccionario de datos](data_dictionary.md)

Los dos CSV completos revisados tienen identificadores únicos y el mismo esquema. El original contiene 1869 etiquetas Churn=Yes y el sintético 594. Estas etiquetas no son predicciones. Los datos sintéticos no constituyen evidencia de precisión sobre clientes reales.

## Uso

Descargar el CSV original siguiendo las instrucciones de la carpeta original. Para probar la aplicación, desactivar la casilla de base original, cargar uno de los CSV de ejemplo y ejecutar el pipeline. Los archivos se procesan por separado.

Columnas mínimas: `customerID`, `tenure`, `MonthlyCharges`, `Contract`. Churn es opcional para inferencia. Conservar los nombres y categorías originales. El ejemplo mínimo contiene 20 filas extraídas del dataset sintético; no se ha ejecutado en la aplicación.

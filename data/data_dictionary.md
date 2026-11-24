# Diccionario de datos

| Variable | Tipo lógico | Descripción | Valores observados en el sintético | Obligatoria para inferencia |
|---|---|---|---|---|
| `customerID` | Texto | Identificador único | Identificadores únicos | Sí |
| `gender` | Texto | Género | Female, Male | No |
| `SeniorCitizen` | Entero | Indicador de adulto mayor (0/1) | 0, 1 | No |
| `Partner` | Texto | Tiene pareja | No, Yes | No |
| `Dependents` | Texto | Tiene dependientes | No, Yes | No |
| `tenure` | Entero | Antigüedad en meses | 1 a 72 | Sí |
| `PhoneService` | Texto | Servicio telefónico | No, Yes | No |
| `MultipleLines` | Texto | Líneas múltiples | No, No phone service, Yes | No |
| `InternetService` | Texto | Tipo de internet | DSL, Fiber optic, No | No |
| `OnlineSecurity` | Texto | Seguridad en línea | No, No internet service, Yes | No |
| `OnlineBackup` | Texto | Respaldo en línea | No, No internet service, Yes | No |
| `DeviceProtection` | Texto | Protección de dispositivos | No, No internet service, Yes | No |
| `TechSupport` | Texto | Soporte técnico | No, No internet service, Yes | No |
| `StreamingTV` | Texto | Televisión en streaming | No, No internet service, Yes | No |
| `StreamingMovies` | Texto | Películas en streaming | No, No internet service, Yes | No |
| `Contract` | Texto | Tipo de contrato | Month-to-month, One year, Two year | Sí |
| `PaperlessBilling` | Texto | Facturación sin papel | No, Yes | No |
| `PaymentMethod` | Texto | Método de pago | Bank transfer (automatic), Credit card (automatic), Electronic check, Mailed check | No |
| `MonthlyCharges` | Decimal | Cargo mensual | 0.07 a 120.33 | Sí |
| `TotalCharges` | Decimal | Cargos acumulados | 2.57 a 7962.2 | No |
| `Churn` | Texto | Etiqueta de abandono | No, Yes | No |

En el archivo original, TotalCharges puede contener espacios en blanco y requiere conversión numérica. Churn es la etiqueta objetivo del entrenamiento, no una característica de inferencia.

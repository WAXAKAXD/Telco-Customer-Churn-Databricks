
import streamlit as st
import pandas as pd
import os
import io
import uuid
import time
import plotly.express as px

from databricks.sdk import WorkspaceClient

# CONFIGURACION GENERAL

st.set_page_config(
    page_title="Telco Churn - Customer Analytics",
    page_icon="📊",
    layout="wide"
)

w = WorkspaceClient()

# El Job se configura mediante el recurso telco-job de Databricks Apps.
job_id_config = os.environ.get("TELCO_JOB_ID")
if not job_id_config:
    st.error("Configura el recurso telco-job y la variable TELCO_JOB_ID.")
    st.stop()
JOB_ID = int(job_id_config)

# Ruta del Volume utilizado por los notebooks del proyecto.
# Puede ajustarse al reproducir el proyecto en otro workspace.
VOLUMEN = "/Volumes/workspace/default/telco_churn"

RUTA_ENTRADA = f"{VOLUMEN}/entradas"
RUTA_SALIDA = f"{VOLUMEN}/resultados"

# ENCABEZADO

st.title("📊 Telco Churn - Customer Analytics")

st.markdown(
    "Sistema de predicción de abandono de clientes "
    "mediante Machine Learning"
)

st.divider()

# CARGA DE ARCHIVOS

st.header("1. Cargar base de datos")

archivo = st.file_uploader(
    "Selecciona un archivo CSV",
    type=["csv"]
)

usar_original = st.checkbox(
    "Utilizar la base de datos original",
    value=False
)

datos_validos = False

if archivo is not None:

    try:
        df = pd.read_csv(archivo)

        columnas_requeridas = [
            "customerID",
            "tenure",
            "Contract",
            "MonthlyCharges"
        ]

        faltantes = [
            c for c in columnas_requeridas
            if c not in df.columns
        ]

        if faltantes:
            st.error(
                f"Columnas faltantes: {faltantes}"
            )
        else:
            datos_validos = True

            st.success("Archivo recibido correctamente")

            c1, c2 = st.columns(2)

            c1.metric("Registros", len(df))
            c2.metric("Columnas", len(df.columns))

            st.dataframe(
                df.head(10),
                use_container_width=True
            )

    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")

st.divider()

# EJECUCION DEL PIPELINE

st.header("2. Procesamiento de datos")

st.markdown(
    "Bronze → Silver → Gold → Machine Learning"
)

if st.button(
    "▶ Ejecutar pipeline",
    type="primary",
    disabled=not (datos_validos or usar_original)
):

    try:

        id_proceso = str(uuid.uuid4())
        nombre_archivo = ""

        if not usar_original:

            nombre_archivo = f"{id_proceso}.csv"

            ruta_archivo = (
                f"{RUTA_ENTRADA}/{nombre_archivo}"
            )

            w.files.upload(
                ruta_archivo,
                io.BytesIO(archivo.getvalue()),
                overwrite=True
            )

            st.success("CSV cargado en Unity Catalog")

        ejecucion = w.jobs.run_now(
            job_id=JOB_ID,
            job_parameters={
                "archivo_csv": nombre_archivo,
                "id_proceso": id_proceso
            }
        )

        run_id = ejecucion.run_id

        st.session_state["run_id"] = run_id
        st.session_state["id_proceso"] = id_proceso

    except Exception as e:
        st.error(f"Error al iniciar el pipeline: {e}")

# CONSULTAR ESTADO DEL JOB

if "run_id" in st.session_state:

    run_id = st.session_state["run_id"]

    estado_visual = st.empty()

    try:

        while True:

            run = w.jobs.get_run(run_id=run_id)

            estado = run.state.life_cycle_state.value

            estado_visual.info(
                f"Estado del pipeline: {estado}"
            )

            if estado in [
                "TERMINATED",
                "SKIPPED",
                "INTERNAL_ERROR"
            ]:
                break

            time.sleep(5)

        resultado = run.state.result_state

        if resultado and resultado.value == "SUCCESS":

            estado_visual.success(
                "Pipeline finalizado correctamente"
            )

            st.session_state["proceso_completo"] = True

        else:

            st.session_state["proceso_completo"] = False

            st.error(
                f"El pipeline no finalizó correctamente: "
                f"{run.state.state_message}"
            )

    except Exception as e:
        st.error(f"Error al consultar el Job: {e}")

# VISUALIZACION DE RESULTADOS

if st.session_state.get("proceso_completo", False):

    st.divider()
    st.header("3. Resultados del análisis")

    id_proceso = st.session_state["id_proceso"]

    ruta_csv = f"{RUTA_SALIDA}/{id_proceso}/csv"

    try:

        archivos = w.files.list_directory_contents(
            ruta_csv
        )

        tablas = []

        for elemento in archivos:

            if elemento.path.endswith(".csv"):

                respuesta = w.files.download(
                    elemento.path
                )

                contenido = respuesta.contents.read()

                tablas.append(
                    pd.read_csv(io.BytesIO(contenido))
                )

        if not tablas:
            st.error("No se encontraron resultados CSV")
            st.stop()

        resultados = pd.concat(
            tablas,
            ignore_index=True
        )

        total = len(resultados)

        abandono = (
            resultados["Prediccion"] == "Abandona"
        ).sum()

        permanecen = total - abandono

        probabilidad = resultados[
            "ProbabilidadAbandono"
        ].mean()

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Total de clientes", total)

        c2.metric(
            "Predicción de abandono",
            int(abandono)
        )

        c3.metric(
            "Predicción de permanencia",
            int(permanecen)
        )

        c4.metric(
            "Probabilidad promedio",
            f"{probabilidad:.2f}%"
        )

        # GRAFICAS

        izquierda, derecha = st.columns(2)

        with izquierda:

            riesgo = resultados[
                "NivelRiesgo"
            ].value_counts().reset_index()

            riesgo.columns = [
                "NivelRiesgo", "Clientes"
            ]

            fig = px.pie(
                riesgo,
                names="NivelRiesgo",
                values="Clientes",
                hole=0.55,
                title="Distribución por nivel de riesgo",
                color="NivelRiesgo",
                color_discrete_map={
                    "Bajo": "#2EAD63",
                    "Medio": "#E8B936",
                    "Alto": "#DC4141"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with derecha:

            resultados["Periodo"] = pd.cut(
                resultados["tenure"],
                bins=[-1, 12, 24, 36, 48, 60, 72],
                labels=[
                    "0-12 meses",
                    "13-24 meses",
                    "25-36 meses",
                    "37-48 meses",
                    "49-60 meses",
                    "61-72 meses"
                ]
            )

            agrupados = resultados.groupby(
                ["Periodo", "Prediccion"],
                observed=True
            ).size().reset_index(name="Clientes")

            fig = px.bar(
                agrupados,
                x="Periodo",
                y="Clientes",
                color="Prediccion",
                barmode="group",
                title="Predicción por antigüedad",
                color_discrete_map={
                    "Permanece": "#2EAD63",
                    "Abandona": "#DC4141"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # TABLA DE CLIENTES

        st.subheader(
            "20 clientes con mayor riesgo de abandono"
        )

        st.dataframe(
            resultados.sort_values(
                "ProbabilidadAbandono",
                ascending=False
            ).head(20),
            use_container_width=True
        )

        # DESCARGAR RESULTADOS

        st.download_button(
            label="⬇ Descargar resultados CSV",
            data=resultados.to_csv(index=False),
            file_name="predicciones_telco.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Error al recuperar resultados: {e}")

st.divider()

st.caption(
    "Databricks | Apache Spark | MLflow | "
    "Unity Catalog | Streamlit"
)

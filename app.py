import streamlit as st
import pandas as pd

st.title("Control de Gastos Personales")
st.sidebar.title("Contenido")
contenido=st.sidebar.selectbox("",["Home","Ejerccio 1","Ejerccio 2",
                     "Ejerccio 3","Ejerccio 4"])

if contenido =="Home":
  st.write("Te encuentras en el modulo de home")
  st.subheader("Estudiante")
  st.write ("Franco Olivera Estacion")
  st.write("Modulo: Python Fundamentals")
  st.write("Año:2026")
  st.subheader("Informacion general")
  st.write("""Estudiante de Ingeniería Industrial orientado al análisis de datos,
automatización y mejora de procesos.
""")
  st.subheader("Descripcion del proyecto")
  st.write("""
El proyecto consiste en desarrollar una aplicación web utilizando
Streamlit para presentar y analizar indicadores relacionados con
el proceso de despacho. La aplicación busca facilitar la visualización
de información y el seguimiento de los principales indicadores.
""")
  st.subheader("Tecnologias utilizadas")
  st.markdown("""
🐍 Python
📊 Streamlit
📈 Pandas
📉 Matplotlib
""")
elif contenido ==("Ejerccio 1"):
  st.write("Te encuentras en el modulo de Ejercicio 1")
  st.subheader("Flujo de caja")
  st.markdown("""
Este módulo permite registrar movimientos financieros,
clasificándolos como ingresos o gastos. A partir de los
movimientos registrados se calcula el total de ingresos,
el total de gastos y el saldo final.
""")
  
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

concepto = st.text_input("Concepto")

tipo = st.selectbox(
    "Tipo de movimiento:",
    ["Ingreso", "Gasto"]
)

valor = st.number_input(
    "Valor",
    min_value=0.0,
    step=0.01
)

if st.button("Agregar movimiento"):

    if concepto == "":
        st.warning("Ingrese un concepto.")

    elif valor <= 0:
        st.warning("Ingrese un valor mayor que 0.")

    else:
        movimiento = {
            "concepto": concepto,
            "tipo": tipo,
            "valor": valor
        }

        st.session_state.movimientos.append(movimiento)

        st.success("Movimiento agregado correctamente.")


# Mostrar movimientos
st.subheader("Movimientos registrados")

 if len(st.session_state.movimientos) > 0:

    # Convertir la lista en DataFrame
    df = pd.DataFrame(st.session_state.movimientos)

    st.dataframe(df)

    # Calcular ingresos y gastos
    total_ingreso = df.loc[
        df["tipo"] == "Ingreso",
        "valor"
    ].sum()

    total_gasto = df.loc[
        df["tipo"] == "Gasto",
        "valor"
    ].sum()

    saldo_final = total_ingreso - total_gasto

    # Resultados
    st.subheader("Resultado del flujo de caja")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total de ingresos",
            f"S/ {total_ingreso:.2f}"
        )

    with col2:
        st.metric(
            "Total de gastos",
            f"S/ {total_gasto:.2f}"
        )

    with col3:
        st.metric(
            "Saldo final",
            f"S/ {saldo_final:.2f}"
        )

    # Mensaje según el saldo
    if saldo_final >= 0:
        st.success("El flujo de caja está a favor.")
    else:
        st.error("El flujo de caja está en contra.")
 elif contenido ==("Ejerccio 2"):
  st.write("Te encuentras en el modulo de Ejerccio 2")

 elif contenido ==("Ejerccio 3"):
  st.write("Te encuentras en el modulo de Ejerccio 3")

 else:
  st.write("Te encuentras en el modulo de Ejerccio 4")





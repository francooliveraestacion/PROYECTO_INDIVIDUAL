import streamlit as st
import pandas as pd
import numpy as np
import librería_clases_proyecto1 as evaluar_paciente_completo

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

    st.markdown(
        """
        Este módulo permite registrar movimientos financieros,
        clasificándolos como ingresos o gastos. A partir de los
        movimientos registrados se calcula el total de ingresos,
        el total de gastos y el saldo final.
        """
    )

    # Esta lista se guarda en session_state para no perder los movimientos
    # cada vez que Streamlit vuelve a ejecutar la página.
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Datos que debe ingresar el usuario para registrar un movimiento
    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=0.01, format="%.2f")

    # Al presionar el botón validamos los datos antes de guardar
    if st.button("Agregar movimiento"):
        if concepto.strip() == "":
            st.warning("Ingrese un concepto.")
        elif valor <= 0:
            st.warning("Ingrese un valor mayor que 0.")
        else:
            movimiento = {
                "concepto": concepto.strip(),
                "tipo": tipo,
                "valor": valor
            }

            st.session_state.movimientos.append(movimiento)
            st.success("Movimiento agregado correctamente.")

    st.subheader("Movimientos registrados")

    # Solo hacemos los cálculos cuando ya existe al menos un movimiento
    if len(st.session_state.movimientos) > 0:
        df = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df, use_container_width=True)

        # Separamos ingresos y gastos para obtener el saldo final
        total_ingreso = df.loc[df["tipo"] == "Ingreso", "valor"].sum()
        total_gasto = df.loc[df["tipo"] == "Gasto", "valor"].sum()
        saldo_final = total_ingreso - total_gasto

        st.subheader("Resultado del flujo de caja")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total de ingresos", f"S/ {total_ingreso:.2f}")

        with col2:
            st.metric("Total de gastos", f"S/ {total_gasto:.2f}")

        with col3:
            st.metric("Saldo final", f"S/ {saldo_final:.2f}")

        # Un mensaje simple para interpretar el resultado
        if saldo_final >= 0:
            st.success("El flujo de caja está a favor.")
        else:
            st.error("El flujo de caja está en contra.")

    else:
        st.info("Aún no hay movimientos registrados.")





elif contenido ==("Ejerccio 2"):
  st.write("Te encuentras en el modulo de Ejerccio 2")
  st.title("Registro de productos")

  st.markdown("""Este módulo permite registrar productos utilizando arreglos de NumPy. 
  Cada registro contiene el nombre del producto, su categoría, precio, cantidad y el total de la venta. 
  Los registros se almacenan en un array de NumPy y posteriormente se convierten en un DataFrame para mostrar 
  la información actualizada en pantalla.""")

  if "registros" not in st.session_state:
    st.session_state.registros = np.empty((0, 5), dtype=object)
    st.subheader("Registro de producto")
  nombre = st.text_input("Nombre del producto")
  categoria = st.selectbox( "Categoría", ["Cerveza", "Bebida", "Alimento", "Otro"] )
  precio = st.number_input( "Precio", min_value=0.0, step=0.01 )
  cantidad = st.number_input( "Cantidad", min_value=1, step=1 )
  total = precio * cantidad
  st.write(f"Total: S/ {total:.2f}")
  if st.button("Agregar producto"):
    if nombre == "": st.warning("Ingrese el nombre del producto.")
    elif precio <= 0: st.warning("Ingrese un precio mayor que 0.")
    else:
      nuevo_registro = np.array( [[nombre, categoria, precio, cantidad, total]], dtype=object )
    st.session_state.registros = np.vstack( [st.session_state.registros, nuevo_registro] )
    st.success("Producto agregado correctamente.")
  st.subheader("Registros")
  if len(st.session_state.registros) > 0:
    df = pd.DataFrame( st.session_state.registros, columns=[ "Producto", "Categoría", "Precio", "Cantidad", "Total" ] )
    st.dataframe(df, use_container_width=True)
  else: st.info("Aún no hay productos registrados.")
      
elif contenido ==("Ejerccio 3"):
  st.write("Te encuentras en el modulo de Ejerccio 3")
  st.title("Uso de funciones desde una librería externa")
  if "historico_resultados" not in st.session_state:
    st.session_state.historico_resultados = pd.DataFrame(columns=["paciente", "imc", "clasificacion_imc", "superficie_corporal_m2"] )
  st.divider()
  opcion_funcion = st.selectbox("Seleccione la función que desea ejecutar:",
    options=["Evaluación de Paciente (IMC y Superficie Corporal)"])
  st.subheader("Ingreso de Parámetros")
  if opcion_funcion == "Evaluación de Paciente (IMC y Superficie Corporal)":
    col1, col2, col3 = st.columns(3)

    with col1:
        nombre = st.text_input("Nombre del Paciente", value="Juan Pérez")
    with col2:
        peso = st.number_input("Peso (kg)", min_value=0.1, max_value=300.0, value=70.0, step=0.5)
    with col3:
        altura = st.number_input("Altura (m)", min_value=0.3, max_value=2.5, value=1.70, step=0.01)

    st.write("")
  if st.button("🚀 Ejecutar Función", type="primary"):
        try:
            resultado = evaluar_paciente_completo(nombre=nombre, peso_kg=peso, altura_m=altura)
            st.success("✅ Función ejecutada con éxito")
            st.markdown("### Resultado:")
            res_col1, res_col2, res_col3 = st.columns(3)
            res_col1.metric("IMC", f"{resultado['imc']} kg/m²")
            res_col2.metric("Clasificación", resultado['clasificacion_imc'])
            res_col3.metric("Sup. Corporal", f"{resultado['superficie_corporal_m2']} m²")

            nuevo_registro = pd.DataFrame([resultado])
            st.session_state.historico_resultados = pd.concat(
                [st.session_state.historico_resultados, nuevo_registro],
                ignore_index=True)
        

   
  st.divider()
  st.subheader("📊 Histórico de Resultados Obtendidos")

  if not st.session_state.historico_resultados.empty:
    st.dataframe(st.session_state.historico_resultados, use_container_width=True)
    
    if st.button("Limpiar Histórico"):
        st.session_state.historico_resultados = pd.DataFrame(columns=["paciente", "imc", "clasificacion_imc", "superficie_corporal_m2"] )
        st.rerun()
  else:
    st.info("Aún no se han ejecutado cálculos en esta sesión.")

    
  


else:
  st.write("Te encuentras en el modulo de Ejerccio 4")





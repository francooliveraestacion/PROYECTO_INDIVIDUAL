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
    concepto=st.text_input("Concepto")
    tipo=st.selectbox("Tipo de movimiento:",
                      ["ingreso","Gasto"])
    valor=st.text_input("Valor,min_value==0.0,step=0.01")
    if st.button("Agregar un boton"):
      if concepto == "":
        st.warning("Ingrese un concepto")

      elif valor <=0 :
        st.warning("Ingrese un calor mayor que 0.")
      else:
        movimiento={"concepto":concepto,"tipo":tipo,"valor":valor}
        st.session_state.movimientos.append(movimiento)
        st.success("Movimiento agregado correctamente.")

    st.subheader("Movimientos registrados")
    if len(st.session_state.movimientos) > 0:
     st.dataframe(df)
     total_ingreso = df.loc[df["tipo"] =="ingreso","valor"].sum()
     total_gastos = df.loc[df["Tipo"] == "Gasto","Valor"].sum()
     saldo_final = total_ingresos - total_gastos
      
    st.subheader("Resultado del flujo de caja")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de ingresos", f"S/ {total_ingreso:.2f}")

      
     

    
    
   
          
elif contenido ==("Ejerccio 2"):
  st.write("Te encuentras en el modulo de Ejerccio 2")

elif contenido ==("Ejerccio 3"):
  st.write("Te encuentras en el modulo de Ejerccio 3")

else:
  st.write("Te encuentras en el modulo de Ejerccio 4")





import streamlit as st

st.title("Indicadores De Despacho")
st.sidebar.title("Contenido")
contenido=st.sidebar.selectbox("",["Home","Ejerccio 1","Ejerccio 2",
                     "Ejerccio 3","Ejerccio 4"])

if contenido =="Home":
  st.write("Te encuentras em el modulo de home")
  st.subheader("Estudiante")
  st.write ("Franco Olivera Esatcion")


elif contenido ==("Ejerccio 1"):
  st.write("Te encuentras em el modulo de Ejerccio 1")

elif contenido ==("Ejerccio 2"):
  st.write("Te encuentras em el modulo de Ejerccio 2")

elif contenido ==("Ejerccio 3"):
  st.write("Te encuentras em el modulo de Ejerccio 3")

else:
  st.write("Te encuentras em el modulo de Ejerccio 4")





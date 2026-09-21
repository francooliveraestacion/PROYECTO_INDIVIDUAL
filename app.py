import streamlit as st
import pandas as pd
import numpy as np
from libreria_funciones_proyecto1 import calcular_imc
from librería_clases_proyecto1 import InventarioProducto

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
  if "historial" not in st.session_state: st.session_state.historial = []
  st.header("1. Selección de función")
  funcion_seleccionada = st.selectbox( "Seleccione la función que desea ejecutar:", [ "Calcular IMC" ] )
  st.header("2. Ingreso de parámetros") 
  col1, col2 = st.columns(2)
  with col1: peso_kg = st.number_input( "Peso (kg)", min_value=0.1, value=70.0, step=0.1 ) 
  with col2: altura_m = st.number_input( "Altura (m)", min_value=0.1, value=1.75, step=0.01 )
  st.header("3. Ejecutar función") 
  if st.button("CALCULO IMC"):
    try: # Ejecutar la función de la librería 
      resultado = calcular_imc( peso_kg, altura_m )
      st.success("La función se ejecutó correctamente.") 
      st.subheader("Resultado") 
      col1, col2 = st.columns(2)
      with col1: 
        st.metric( "IMC", resultado["imc"] )
      with col2: 
        st.write("Clasificación") 
        st.info( resultado["clasificacion"] )
      nuevo_registro = { 
      "Función": funcion_seleccionada, 
      "Peso (kg)": peso_kg,
      "Altura (m)": altura_m,
      "IMC": resultado["imc"], 
      "Clasificación": resultado["clasificacion"] }
      st.session_state.historial.append( nuevo_registro ) 
      st.success( "Resultado guardado en el histórico." )
    except Exception as error:
     st.error(f"Error al ejecutar la función: {error}")
  st.header("4. Histórico de resultados")
  if len(st.session_state.historial) > 0:
    df_historial = pd.DataFrame( st.session_state.historial)
    st.dataframe( df_historial, use_container_width=True, hide_index=True )
  else:st.info( "Todavía no se han registrado resultados.")

else:
  st.write("Te encuentras en el modulo de Ejerccio 4")
  st.title("📦  Gestión de Inventario")
  st.write(
        """
        En este ejercicio utilizamos la clase `InventarioProducto`
        desde una librería externa para realizar operaciones CRUD.
        """
    )
  if 'productos' not in st.session_state:
    st.session_state.productos = []
  def crear_producto_form():
    st.header("Crear Nuevo Producto")
    with st.form("crear_producto"):
      nombre = st.text_input("Nombre del Producto")
      costo_unitario = st.number_input("Costo Unitario", min_value=0.01, format="%.2f")
      precio_unitario = st.number_input("Precio Unitario", min_value=0.01, format="%.2f")
      stock_actual = st.number_input("Stock Actual", min_value=0, step=1)
      stock_minimo = st.number_input("Stock Mínimo", min_value=0, step=1)
      submit_button = st.form_submit_button("Guardar Producto")
      if submit_button:
            try:
                if any(p.nombre == nombre for p in st.session_state.productos):
                    st.error(f"Ya existe un producto con el nombre '{nombre}'. Por favor, use un nombre diferente o actualice el producto existente.")
                else:
                    nuevo_producto = InventarioProducto(nombre, costo_unitario, precio_unitario, stock_actual, stock_minimo)
                    st.session_state.productos.append(nuevo_producto)
                    st.success(f"Producto '{nombre}' creado exitosamente!")
            except ValueError as e:
                st.error(f"Error al crear producto: {e}")
   def leer_productos():
   st.header("Listado de Productos")
   if st.session_state.productos:
        productos_data = [p.resumen() for p in st.session_state.productos]
        df = pd.DataFrame(productos_data)
        st.dataframe(df)
    else:
        st.info("No hay productos en el inventario.")
              


   

  
 
  





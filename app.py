import streamlit as st
import pandas as pd
import numpy as np
from libreria_funciones_proyecto1 import calcular_imc
from librería_clases_proyecto1 import InventarioProducto, validar_positivo

st.title("Proyecto Individual")
st.image("personal.png",width=100)
st.sidebar.title("Contenido")
contenido=st.sidebar.selectbox("",["Home","Ejercicio 1","Ejercicio 2",
                     "Ejercicio 3","Ejercicio 4"])
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
  def leer_productos():
    st.header("Listado de Productos")
    if st.session_state.productos:
        tab1, tab2 = st.tabs(["Todos los Productos", "Productos que necesitan reposición"])

        productos_data = [p.resumen() for p in st.session_state.productos]
        df = pd.DataFrame(productos_data)

        with tab1:
            st.subheader("Inventario Completo")
            if not df.empty:
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No hay productos en el inventario.")

        with tab2:
            st.subheader("Productos a Reponer")
            productos_reposicion = df[df['necesita_reposicion'] == True]
            if not productos_reposicion.empty:
                st.dataframe(productos_reposicion, use_container_width=True)
            else:
                st.info("Ningún producto necesita reposición.")
    else:
        st.info("No hay productos en el inventario.")
  def actualizar_producto_form():
    st.header("Actualizar Producto")
    if not st.session_state.productos:
        st.info("No hay productos para actualizar.")
        return

    nombres_productos = [p.nombre for p in st.session_state.productos]
    producto_seleccionado_nombre = st.selectbox("Seleccionar Producto a Actualizar", nombres_productos)
    
    if producto_seleccionado_nombre:
        # Find the product object
        producto_idx = next((i for i, p in enumerate(st.session_state.productos) if p.nombre == producto_seleccionado_nombre), None)
        if producto_idx is not None:
            producto_a_actualizar = st.session_state.productos[producto_idx]

            with st.form("actualizar_producto"):
                st.write(f"Editando producto: **{producto_a_actualizar.nombre}**")
                nuevo_nombre = st.text_input("Nombre del Producto", value=producto_a_actualizar.nombre)
                nuevo_costo_unitario = st.number_input("Costo Unitario", value=producto_a_actualizar.costo_unitario, min_value=0.01, format="%.2f")
                nuevo_precio_unitario = st.number_input("Precio Unitario", value=producto_a_actualizar.precio_unitario, min_value=0.01, format="%.2f")
                nuevo_stock_actual = st.number_input("Stock Actual", value=producto_a_actualizar.stock_actual, min_value=0, step=1)
                nuevo_stock_minimo = st.number_input("Stock Mínimo", value=producto_a_actualizar.stock_minimo, min_value=0, step=1)
                
                update_button = st.form_submit_button("Actualizar")

                if update_button:
                    try:
                        # Validate if the new name clashes with another existing product (if name changed)
                        if nuevo_nombre != producto_seleccionado_nombre and any(p.nombre == nuevo_nombre for p in st.session_state.productos if p.nombre != producto_seleccionado_nombre):
                            st.error(f"Ya existe otro producto con el nombre '{nuevo_nombre}'.")
                        else:
                            # Create a temporary instance to validate values before assigning to the actual object
                            temp_product = InventarioProducto(nuevo_nombre, nuevo_costo_unitario, nuevo_precio_unitario, nuevo_stock_actual, nuevo_stock_minimo)
                            
                            producto_a_actualizar.nombre = nuevo_nombre
                            producto_a_actualizar.costo_unitario = nuevo_costo_unitario
                            producto_a_actualizar.precio_unitario = nuevo_precio_unitario
                            producto_a_actualizar.stock_actual = nuevo_stock_actual
                            producto_a_actualizar.stock_minimo = nuevo_stock_minimo
                            st.success(f"Producto '{nuevo_nombre}' actualizado exitosamente!")
                            # If the name changed, rerun to update the selectbox options
                            if producto_seleccionado_nombre != nuevo_nombre:
                                st.experimental_rerun()
                    except ValueError as e:
                        st.error(f"Error al actualizar producto: {e}")
    def eliminar_producto_form():
     st.header("Eliminar Producto")
     if not st.session_state.productos:
        st.info("No hay productos para eliminar.")
        return

     nombres_productos = [p.nombre for p in st.session_state.productos]
     producto_a_eliminar_nombre = st.selectbox("Seleccionar Producto a Eliminar", nombres_productos)

     if producto_a_eliminar_nombre:
        if st.button(f"Eliminar '{producto_a_eliminar_nombre}'"): # Add a confirmation button
            st.session_state.productos = [p for p in st.session_state.productos if p.nombre != producto_a_eliminar_nombre]
            st.success(f"Producto '{producto_a_eliminar_nombre}' eliminado exitosamente.")
            st.experimental_rerun() # Rerun to update the selectbox and product list
    


              


   

  
 
  





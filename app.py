import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos desde el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Cuadro de Mandos de Anuncios de Coches")

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir histograma')

if build_histogram:  # Si la casilla de verificación está seleccionada
    # Mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:  # Si la casilla de verificación está seleccionada
    # Mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", color="model")
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

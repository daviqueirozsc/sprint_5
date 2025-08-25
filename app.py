import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv')

st.header('Análise Exploratória de Dados (EDA) dos Carros')

hist_button = st.button('Criar histograma de Distribuição de Combustível dos Carros')
        
if hist_button: 
    st.write('Criando um histograma de Distribuição de Combustível dos Carros')
    fig = px.histogram(car_data, x="fuel", title="Distribuição de Combustível dos Carros")
    st.plotly_chart(fig, use_container_width=True)

hist_button2 = st.button('Criar histograma de Distribuição de Cores dos Carros')

if hist_button2:
    st.write('Criando histograma de Distribuição de Cores dos Carros')
    fig = px.histogram(car_data, x="paint_color", title="Distribuição de Cores dos Carros")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de Dispersão entre Quilometragem e Preço dos Carros')

if scatter_button:
    st.write('Criando gráfico de Dispersão entre Quilometragem e Preço dos Carros')
    fig = px.scatter(car_data, x="odometer", y="price", title="Dispersão entre Quilometragem e Preço dos Carros")
    st.plotly_chart(fig, use_container_width=True)


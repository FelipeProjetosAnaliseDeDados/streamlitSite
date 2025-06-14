
# Importações:
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config('Análise Logistica', layout='wide')

# Carregar os dados
df = pd.read_excel("base_logistica_completa.xlsx",sheet_name="Entregas")
# Ler os dados                   
# Tirando dados duplicados   
unique_categoria = df['Categoria'].unique()
unique_tipo_Veiculo = df['Veiculo'].unique()


unique_categoria.append("Todos")


filtro_categoria, filtro_veiculo = st.columns(2)

with filtro_categoria:
    categoria = st.selectbox("Selecione a categoria dos produtos", unique_categoria)
with filtro_veiculo:
    veiculo = st.selectbox("Selecione o veículo",unique_tipo_Veiculo)

# Filtrando categorias

filtro = df[(df['Categoria'] == categoria) &  (df['Veiculo'] == veiculo)]

# Criando as métricas
# Total entregas
total_entregas = len(filtro)
# Soma dos fretes
total_fretes = filtro['Valor_Frete'].sum()

col1, col2 = st.columns(2)

col1.metric("Total de entregas", total_entregas)
col2.metric("Total de fretes ", int(total_fretes))

        


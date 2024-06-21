import streamlit as st
from components import layout
from main import load_and_prepare_data

st.set_page_config(layout='wide')
st.title("Informações Empresariais")

# Criar abas
tab1, tab2 = st.tabs(["Aberturas e Fechamentos", "Atividade e Inatividade"])

# Recebe dados tratados
(df, total_aberturas, total_fechamentos, margem_abertura_fechamento, 
 df_margem_abertura_fechamento, merge_abertura_fechamento,
 total_ativas, total_inativas, margem_ativas_inativas, 
 df_margem_ativas_inativas, merge_ativas_inativas) = load_and_prepare_data()

# Sidebar
ano = st.sidebar.selectbox("Ano", ["Todos"] + list(range(2000, 2025)))
municipio = st.sidebar.selectbox("Município", ["Todos"] + list(df['municipio'].unique()))
porte = st.sidebar.selectbox("Porte", ["Todos"] + list(df['porte'].unique()))
atividade = st.sidebar.selectbox("Atividade", ["Todas"] + list(df['atividade'].unique()))

# Aplicando os filtros de acordo com as seleções na barra lateral
if ano != "Todos":
    df = df[df["abertura"].dt.year == ano]
if municipio != "Todos":
    df = df[df["municipio"] == municipio]
if porte != "Todos":
    df = df[df["porte"] == porte]
if atividade != "Todas":
    df = df[df["atividade"] == atividade]

#construindo a pagina
with tab1:
    titulo_positivo, titulo_negativo = "aberturas", "fechamentos"
    layout.layout(total_aberturas, total_fechamentos, margem_abertura_fechamento, df_margem_abertura_fechamento, merge_abertura_fechamento, titulo_positivo, titulo_negativo)
    
with tab2:
    titulo_positivo, titulo_negativo = "ativas", "inativas"
    layout.layout(total_ativas, total_inativas, margem_ativas_inativas, df_margem_ativas_inativas, merge_ativas_inativas, titulo_positivo, titulo_negativo)

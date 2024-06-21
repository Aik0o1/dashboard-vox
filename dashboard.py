import streamlit as st
from components import layout
from main import load_and_prepare_data
import pandas as pd

df = pd.read_csv("assets/dadosFakess.csv")
    
df['abertura'] = pd.to_datetime(df['abertura'])
df['fechamento'] = pd.to_datetime(df['fechamento'])
df = df.sort_values(by='municipio')

st.set_page_config(layout='wide')
st.title("Informações Empresariais")

# Criar abas
tab1, tab2 = st.tabs(["Aberturas e Fechamentos", "Atividade e Inatividade"])

# Sidebar
ano = st.sidebar.selectbox("Ano", ["Todos"] + list(range(2000, 2025)))
municipio = st.sidebar.selectbox("Município", ["Todos"] + list(df['municipio'].unique()))
porte = st.sidebar.selectbox("Porte", ["Todos"] + list(df['porte'].unique()))
atividade = st.sidebar.selectbox("Atividade", ["Todas"] + list(df['atividade'].unique()))

# Aplicando os filtros de acordo com as seleções na barra lateral
df_filtered = df.copy()

if ano != "Todos":
    df_filtered = df_filtered[df_filtered["abertura"].dt.year == ano]
if municipio != "Todos":
    df_filtered = df_filtered[df_filtered["municipio"] == municipio]
if porte != "Todos":
    df_filtered = df_filtered[df_filtered["porte"] == porte]
if atividade != "Todas":
    df_filtered = df_filtered[df_filtered["atividade"] == atividade]


# Recebe dados tratados
(total_aberturas, total_fechamentos, margem_abertura_fechamento, 
 df_margem_abertura_fechamento, merge_abertura_fechamento,
 total_ativas, total_inativas, margem_ativas_inativas, 
 df_margem_ativas_inativas, merge_ativas_inativas) = load_and_prepare_data(df_filtered)


print(merge_abertura_fechamento)
#construindo a pagina
with tab1:
    titulo_positivo, titulo_negativo = "aberturas", "fechamentos"
    layout.layout(df_filtered, total_aberturas, total_fechamentos, margem_abertura_fechamento, df_margem_abertura_fechamento, merge_abertura_fechamento, titulo_positivo, titulo_negativo, ano, porte, municipio, atividade)
    
with tab2:
    titulo_positivo, titulo_negativo = "ativas", "inativas"
    layout.layout(df_filtered, total_ativas, total_inativas, margem_ativas_inativas, df_margem_ativas_inativas, merge_ativas_inativas, titulo_positivo, titulo_negativo, ano, porte, municipio, atividade)

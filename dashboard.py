import streamlit as st
from components import firstTab, secondTab
from main import load_and_prepare_data
import pandas as pd

df = pd.read_csv("assets\dadosFakes20k.csv")    
df['abertura'] = pd.to_datetime(df['abertura'])
df['fechamento'] = pd.to_datetime(df['fechamento'])
df = df.sort_values(by='municipio')
df['anoAbertura'] = df['abertura'].dt.year
df['mesAbertura'] = df['abertura'].dt.month
df['anoFechamento'] = df['fechamento'].dt.year
df['mesFechamento'] = df['fechamento'].dt.month

st.set_page_config(layout='wide')
st.title("Informações Empresariais")

# Criar abas
tab1, tab2 = st.tabs(["Aberturas e Fechamentos", "Atividade e Inatividade"])

# Sidebar
ano = st.sidebar.selectbox("Ano", ["Todos"] + list(range(2000, 2025)))
municipio = st.sidebar.selectbox("Município", ["Todos"] + list(df['municipio'].unique()))
porte = st.sidebar.selectbox("Porte", ["Todos"] + list(df['porte'].unique()))
atividade = st.sidebar.selectbox("Atividade", ["Todas"] + list(df['atividade'].unique()))

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
 df_porte, df_natureza) = load_and_prepare_data(df_filtered)

#construindo a pagina
with tab1:
    titulo_positivo, titulo_negativo = "aberturas", "fechamentos"
    firstTab.layout(df_filtered, total_aberturas, total_fechamentos, margem_abertura_fechamento, df_margem_abertura_fechamento, merge_abertura_fechamento, titulo_positivo, titulo_negativo, ano, porte, municipio, atividade)
    
with tab2:
    titulo_bar1, titulo_bar2 = "porte", "natureza juridica"
    secondTab.layout(df_filtered, ano, porte, municipio, atividade, titulo_bar1, titulo_bar2)

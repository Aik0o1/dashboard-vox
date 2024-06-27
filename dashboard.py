import streamlit as st
from components import firstTab, secondTab
from main import load_and_prepare_data
import pandas as pd


df = pd.read_csv("assets/dadosFakes20k.csv")    
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
mes = st.sidebar.selectbox("Mês", ["Todos"] + list(range(1, 13)))
municipio = st.sidebar.selectbox("Município", ["Todos"] + list(df['municipio'].unique()))
porte = st.sidebar.selectbox("Porte", ["Todos"] + list(df['porte'].unique()))
atividade = st.sidebar.selectbox("Atividade", ["Todas"] + list(df['atividade'].unique()))

# Aplicando os filtros de acordo com as seleções na barra lateral
df_filtered = df.copy()

if ano != "Todos":
    df_filtered = df_filtered[df_filtered["abertura"].dt.year == ano]
if mes != "Todos":
    df_filtered = df_filtered[df_filtered["abertura"].dt.month == mes]
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


# Ajustar o agrupamento e eixo_x com base na seleção do ano
if ano != "Todos":
    aberturas_por_periodo = df_filtered.groupby('mesAbertura').size().reset_index(name='aberturas')
    fechamentos_por_periodo = df_filtered.dropna(subset=['mesFechamento']).groupby('mesFechamento').size().reset_index(name='fechamentos')
    
    aberturas_por_periodo.rename(columns={'mesAbertura': 'periodo'}, inplace=True)
    fechamentos_por_periodo.rename(columns={'mesFechamento': 'periodo'}, inplace=True)
    
else:
    aberturas_por_periodo = df_filtered.groupby('anoAbertura').size().reset_index(name='aberturas')
    fechamentos_por_periodo = df_filtered.dropna(subset=['anoFechamento']).groupby('anoFechamento').size().reset_index(name='fechamentos')
    
    aberturas_por_periodo.rename(columns={'anoAbertura': 'periodo'}, inplace=True)
    fechamentos_por_periodo.rename(columns={'anoFechamento': 'periodo'}, inplace=True)

merge_abertura_fechamento = pd.merge(aberturas_por_periodo, fechamentos_por_periodo, on='periodo', how='outer').fillna(0)


#construindo a pagina
with tab1:
    titulo_positivo, titulo_negativo = "aberturas", "fechamentos"
    firstTab.layout(df_filtered, total_aberturas, total_fechamentos, margem_abertura_fechamento, df_margem_abertura_fechamento, merge_abertura_fechamento, titulo_positivo, titulo_negativo, ano, porte, municipio, atividade)
    
with tab2:
    titulo_bar1, titulo_bar2 = "porte", "natureza juridica"
    secondTab.layout(df_filtered, ano, porte, municipio, atividade, titulo_bar1, titulo_bar2)

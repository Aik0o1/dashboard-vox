import streamlit as st
import pandas as pd
import plotly.express as px
from mapHeat import plotMap


st.set_page_config(layout='wide')
st.title("Informações Empresariais")

df = pd.read_csv("assets/dadosFakess.csv")
df['abertura'] = pd.to_datetime(df['abertura'])
df['fechamento'] = pd.to_datetime(df['fechamento'])
df = df.sort_values(by='municipio')

# Criar abas
tab1, tab2 = st.tabs(["Aberturas e Fechamentos", "Atividade e Inatividade"])

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


#Total de aberturas, fechamentos e margem
total_aberturas = df['anoAbertura'].count()
total_fechamentos = df['anoFechamento'].count()
margem = total_aberturas - total_fechamentos

# Preparar dados para o gráfico de margem
data_margem = {
    'Tipo': ['Aberturas', 'Fechamentos'],
    'Quantidade': [total_aberturas, total_fechamentos]
}

df_margem = pd.DataFrame(data_margem)


#filtro de dados para grafico de abertura vs fechamentos
aberturas_por_ano = df.groupby('anoAbertura').size().reset_index(name='aberturas')
fechamentos_por_ano = df.dropna(subset=['anoFechamento']).groupby('anoFechamento').size().reset_index(name='fechamentos')

aberturas_por_ano.rename(columns={'anoAbertura': 'ano'}, inplace=True)
fechamentos_por_ano.rename(columns={'anoFechamento': 'ano'}, inplace=True)

dados_combined = pd.merge(aberturas_por_ano, fechamentos_por_ano, on='ano', how='outer').fillna(0)


# graficos
fig_abertura_fechamento = px.line(dados_combined, x='ano', y=['aberturas', 'fechamentos'], 
    title='Número de Aberturas e Fechamentos por Ano',
    labels={'value': 'Quantidade', 'variable': 'Tipo'})
fig_margem = px.pie(df_margem, values='Quantidade', names='Tipo', hole=0.6)

# Gráfico de pizza sem legenda
fig_margem.update_layout(
    showlegend=False,
    margin=dict(t=0, b=0, l=0, r=0),
    height=70  # Ajuste a altura conforme necessário
)
#construindo a pagina
with tab1:
    
    # Separando espaços
    bloco_total_aberturas, blocoTotalFechamentos, blocoMargem = st.columns(3)
    bloco_mapa, bloco_grafico_abertura_fechamento = st.columns(2)
    bloco_grafico_aberturas, bloco_grafico_fechamentos = st.columns(2)
    blocoTabela = st.columns(1)
    
    with bloco_total_aberturas:
        st.metric(label='Total de aberturas', value=total_aberturas)
    with blocoTotalFechamentos:
        st.metric(label='Total de Fechamentos', value=total_fechamentos)
    with blocoMargem:
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label='Margem', value=margem)
        with col2:
            st.plotly_chart(fig_margem, use_container_width=True)
            
    figMap = plotMap(df)
    with bloco_mapa:
        figMap
                    
    with bloco_grafico_abertura_fechamento:
        fig_abertura_fechamento
    
with tab2:
    
    st.write("Loading...")

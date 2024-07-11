import streamlit as st
from components import firstTab, secondTab
from main import load_and_prepare_data
import pandas as pd

# tratamento dos dados recebidos em xlsx

df_real = pd.read_excel("assets/MOCK_DATA.xlsx")
# df_real = pd.read_excel("assets/fed9e65c-3666-49c9-aa95-90ab037802ab.xlsx")

df_real.rename(
        columns={
            "Município Endereço Empresa": "municipio",
            "Porte": "porte",
            "Natureza": "natureza juridica",
        }, inplace=True
    )

# df_real['Data Autenticação'] = df_real['Data Autenticação'].replace('-', None)
# df_real['Data Autenticação'] = pd.to_datetime(df_real['Data Autenticação'], format='%d/%m/%Y', errors='coerce')

df_real['Data Autenticação'] = pd.to_datetime(df_real['Data Autenticação'])
df_real["abertura"] = df_real["Data Autenticação"].where(df_real["Tipo Evento"] == "INSCRIÇÃO DE EMPRESA")
df_real["fechamento"] = df_real["Data Autenticação"].where(df_real["Tipo Evento"] == "PEDIDO DE BAIXA")
df = df_real.sort_values(by="municipio")
df["anoAbertura"] = df_real["abertura"].dt.year
df["mesAbertura"] = df_real["abertura"].dt.month
df["anoFechamento"] = df_real["fechamento"].dt.year
df["mesFechamento"] = df_real["fechamento"].dt.month
anos = sorted(df_real['Data Autenticação'].dt.year.dropna().unique())

# configurações da página
st.set_page_config(layout='wide')
st.title("Informações Empresariais")

# Criar abas
tab1, tab2 = st.tabs(["Aberturas e Fechamentos", "Empresas Ativas"])

# Sidebar
ano = st.sidebar.selectbox("Ano", ["Todos"] + anos)
municipio = st.sidebar.selectbox(
    "Município", ["Todos"] + list(df["municipio"].unique())
)
porte = st.sidebar.selectbox("Porte", ["Todos"] + list(df["porte"].unique()))
atividade = st.sidebar.selectbox(
    "Atividade", ["Todas"] + list(df["Atividade"].unique())
)

# aplicação de filtros
df_real_filtered = df.copy()

if ano != "Todos":
    df_real_filtered = df_real_filtered[
        (df_real_filtered["anoAbertura"] == ano) | 
        (df_real_filtered["anoFechamento"] == ano)]
    
if municipio != "Todos":
    df_real_filtered = df_real_filtered[
        df_real_filtered["municipio"] == municipio
    ]

if porte != "Todos":
    df_real_filtered = df_real_filtered[df_real_filtered["porte"] == porte]
if atividade != "Todas":
    df_real_filtered = df_real_filtered[df_real_filtered["Atividade"] == atividade]

print(df_real_filtered.head(100))
# recebe dados tratados
(
    total_aberturas,
    total_fechamentos,
    margem_abertura_fechamento,
    df_margem_abertura_fechamento,
    merge_abertura_fechamento,
    df_porte,
    df_natureza,
    df_total_ativas,
    servico_mais_ativo,
    servico_menos_ativo,
) = load_and_prepare_data(df_real_filtered)

# construindo a pagina
with tab1:
    titulo_positivo, titulo_negativo = "aberturas", "fechamentos"
    firstTab.layout(
        df_real_filtered,
        total_aberturas,
        total_fechamentos,
        margem_abertura_fechamento,
        df_margem_abertura_fechamento,
        merge_abertura_fechamento,
    )

with tab2:
    titulo_bar1, titulo_bar2 = "porte", "natureza juridica"
    secondTab.layout(
        df_real_filtered,
        ano,
        porte,
        municipio,
        atividade,
        titulo_bar1,
        titulo_bar2,
        df_total_ativas,
        servico_mais_ativo,
        servico_menos_ativo,
    )

footer_html = """<hr/><div style='text-align: right; color: #d9dbdb '>
  <p>Developed with Python, Pandas and Streamlit</p>
</div>"""

st.markdown(footer_html, unsafe_allow_html=True)

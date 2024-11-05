import yaml
from components import firstTab, secondTab
from layout import font, footer, header, sidebar
from main import load_and_prepare_data
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import pandas as pd


with open('config/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

header.header()
# definindo fonte
font.font()

# personalizando a sidebar
sidebar.sidebar()
st.markdown(
    '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

authenticator.login()

if st.session_state["authentication_status"]:
    df_real = pd.read_excel("assets/MOCK_DATA.xlsx")

    df_real.rename(
        columns={
            "Município Endereço Empresa": "municipio",
            "Porte": "porte",
            "Natureza": "natureza juridica",
        },
        inplace=True,
    )

    df_real["Data Autenticação"] = pd.to_datetime(df_real["Data Autenticação"])
    df_real["abertura"] = df_real["Data Autenticação"].where(
        df_real["Tipo Evento"] == "INSCRIÇÃO DE EMPRESA"
    )
    df_real["fechamento"] = df_real["Data Autenticação"].where(
        df_real["Tipo Evento"] == "PEDIDO DE BAIXA"
    )
    df = df_real.sort_values(by="municipio")
    df["anoAbertura"] = df_real["abertura"].dt.year
    df["mesAbertura"] = df_real["abertura"].dt.month
    df["anoFechamento"] = df_real["fechamento"].dt.year
    df["mesFechamento"] = df_real["fechamento"].dt.month
    anos = sorted(df_real["Data Autenticação"].dt.year.dropna().unique())

    st.title("Informações Empresariais")
    st.sidebar.info("Filtros")

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
            (df_real_filtered["anoAbertura"] == ano)
            | (df_real_filtered["anoFechamento"] == ano)
        ]
    if municipio != "Todos":
        df_real_filtered = df_real_filtered[df_real_filtered["municipio"] == municipio]
    if porte != "Todos":
        df_real_filtered = df_real_filtered[df_real_filtered["porte"] == porte]
    if atividade != "Todas":
        df_real_filtered = df_real_filtered[df_real_filtered["Atividade"] == atividade]

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

    tab1, tab2 = st.tabs(["Aberturas e Fechamentos", "Empresas Ativas"])
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

    authenticator.logout()
    footer.footer()
elif st.session_state["authentication_status"] == False:
    st.error('Usuário/senha incorretos')
elif st.session_state["authentication_status"] == None:
    st.warning('Por favor, informe o usuário/senha')
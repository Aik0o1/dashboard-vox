import streamlit as st
from components import firstTab, secondTab
from main import load_and_prepare_data
from layout import header, font, logo, sidebar
import pandas as pd


import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader




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
st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">',unsafe_allow_html=True)
header.header()
st.title("Informações Empresariais")



# definindo fonte
font.font()

# Definindo logo
# logo.logo()

# personalizando a sidebar
sidebar.sidebar()


# Cria abas
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


def loginPage():
    # Carrega a configuração de autenticação
    with open('./config/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Inicializa o autenticador
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
    )

    # Exibe o formulário de login
    authenticator.login('main')

    # Verifica o status de autenticação
    if st.session_state['authentication_status']:
        # Logout e redirecionamento para a home
        if authenticator.logout("Logout"):
            st.session_state.page = 'home'  # Atualiza a página para 'home'
            st.experimental_rerun()  # Reinicia a interface para refletir a mudança de página
        
        # Conteúdo da página autenticada
        with st.container():  # Pode ajustar conforme sua estrutura de layout
            st.success("Login bem-sucedido!")
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
    elif st.session_state['authentication_status'] is False:
        st.error("Username/password is incorrect")
    elif st.session_state['authentication_status'] is None:
        st.warning("Please enter your username and password")


# Controle de navegação
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    # Conteúdo da home
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

    # Botão para ir à página de login
    if st.button("Ir para a página de login"):
        st.session_state.page = "login"

elif st.session_state.page == "login":
    loginPage()
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
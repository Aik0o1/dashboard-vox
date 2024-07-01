import streamlit as st
from graphs import mapHeat, pieMargin, lineChart, graphBar, plotTable


def layout(df, total_positivo, total_negativo, margem, tabela_margem, merge_abertura_fechamento, titulo_positivo, titulo_negativo, ano, porte, municipio, atividade):

    bloco_total_positivo, blocoTotalFechamentos, blocoMargem = st.columns(3)
    bloco_grafico_abertura_fechamento = subtab1, subtab2 = st.tabs(["Gráfico", "Tabela"])
    bloco_mapa, tabela_abertura_fechamento = st.columns(2)
    blocoTabela = st.columns(1)
    
    with bloco_total_positivo:
        st.metric(label='Total de aberturas', value=total_positivo)

    with blocoTotalFechamentos:
        st.metric(label='Total de Fechamentos', value=total_negativo)

    with blocoMargem:
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label='Margem', value=margem)
        with col2:
            st.plotly_chart(pieMargin.graph(tabela_margem), use_container_width=True)


    with bloco_grafico_abertura_fechamento[0]:
        subtab1.plotly_chart(lineChart.graph(merge_abertura_fechamento, titulo_positivo, titulo_negativo, 'periodo'))
        
    with bloco_grafico_abertura_fechamento[1]:
        subtab2.dataframe(merge_abertura_fechamento, use_container_width=True)


    with bloco_mapa:
        st.header("Cidades Destaque")
        st.plotly_chart(mapHeat.plotMap(df))

    with tabela_abertura_fechamento:
        tabela_abertura, tabela_fechamento = st.columns(2)
        with tabela_abertura:
            st.header(" ")
            st.write(plotTable.plotTableTab1(df, 'anoAbertura', 'Aberturas'))
        
        with tabela_fechamento:
            st.header(" ")
            st.write(plotTable.plotTableTab1(df, 'anoFechamento', 'Fechamentos'))


    with blocoTabela[0]:
        st.title("Tabela completa")
        st.write(df)
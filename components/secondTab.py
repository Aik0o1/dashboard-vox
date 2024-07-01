import streamlit as st
from graphs import mapHeat, pieMargin, graphBar, treeMap, plotTable


def layout(df, ano, porte, municipio, atividade, titulo_bar1, titulo_bar2):

    bloco_arvore = st.area_chart()
    # bloco_mapa, bloco_grafico_barras = st.columns(2)
    bloco_mapa, tabela_porte_natureza = st.columns(2)
    # blocoTabela = st.columns(1)

    with bloco_arvore:
        st.plotly_chart(treeMap.plotMapTree(df), use_container_width=True)

    with bloco_mapa:
        st.header("Cidades Destaque")
        st.plotly_chart(mapHeat.plotMap(df))

    with tabela_porte_natureza:
        tabela_abertura, tabela_fechamento = st.columns(2)
        with tabela_abertura:
            st.header(" ")
            st.write(plotTable.plotTableTab2(df, 'porte'))
        
        with tabela_fechamento:
            st.header(" ")
            st.write(plotTable.plotTableTab2(df, 'natureza juridica'))
                    
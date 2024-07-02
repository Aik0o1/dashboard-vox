import streamlit as st
from graphs import mapHeat, pieMargin, graphBar, treeMap, plotTable, stackedBar


def layout(df, ano, porte, municipio, atividade, titulo_bar1, titulo_bar2):

    bloco_arvore = st.area_chart()
    # bloco_mapa, bloco_grafico_barras = st.columns(2)
    bloco_mapa, tabela_porte_natureza = st.columns(2)
    grafico_agrupado_porte, grafico_agrupado_natureza = st.columns(2)

    # blocoTabela = st.columns(1)

    with bloco_arvore:
        st.plotly_chart(treeMap.plotMapTree(df), use_container_width=True)

    with bloco_mapa:
        st.header("Cidades Destaque")
        st.plotly_chart(mapHeat.plotMap(df))

    with tabela_porte_natureza:
        tabela_porte = st.columns(1)
        tabela_natureza = st.columns(1)
        with tabela_porte[0]:
            st.header(" ")
            st.dataframe(plotTable.plotTableTab2(df, 'porte'), height=200, width=500)
        
        with tabela_natureza[0]:
            st.dataframe(plotTable.plotTableTab2(df, 'natureza juridica'), height=200, width=500)

    with grafico_agrupado_porte:
        st.plotly_chart(graphBar.plotGraphBar(df, 'porte', 'Porte'))
        
    
    with grafico_agrupado_natureza:
        st.plotly_chart(graphBar.plotGraphBar(df, 'natureza juridica', 'Natureza Jurídica'))            
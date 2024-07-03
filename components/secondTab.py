import streamlit as st
from graphs import mapHeat, pieMargin, circles, graphBar, treeMap, plotTable, stackedBar


def layout(df, ano, porte, municipio, atividade, titulo_bar1, titulo_bar2, df_total_ativas, servico_mais_ativo, servico_menos_ativo):

    bloco_total_ativas, bloco_cidade_mais_ativa, bloco_cidade_menos_ativa = st.columns(3)
    bloco_arvore = st.area_chart()
    # bloco_mapa, bloco_grafico_barras = st.columns(2)
    grafico_agrupado_porte, empty_col, grafico_agrupado_natureza = st.columns([1,0.1,1])
    bloco_mapa, tabela_porte_natureza = st.columns(2)    

    # blocoTabela = st.columns(1)

    with bloco_total_ativas:
        st.metric(label='Total de ativas', value=df_total_ativas)

    with bloco_cidade_mais_ativa:
        st.metric(label='Atividade destaque', value=servico_mais_ativo)

    with bloco_cidade_menos_ativa:
        st.metric(label='Atividade menos ativa', value=servico_menos_ativo)

    with bloco_arvore:
        st.plotly_chart(treeMap.plotMapTree(df), use_container_width=True)

    with grafico_agrupado_porte:
        st.plotly_chart(circles.graph(df), use_container_width=True)

    with bloco_mapa:
        st.subheader("Cidades Destaque")
        st.plotly_chart(mapHeat.plotMap(df))

    with tabela_porte_natureza:
        tabela_porte = st.columns(1)
        tabela_natureza = st.columns(1)
        with tabela_porte[0]:
            st.header(" ")
            st.markdown("###### Municípios por porte")
            st.dataframe(plotTable.plotTableTab2(df, 'porte'), height=200, width=500)
        
        with tabela_natureza[0]:
            st.markdown("###### Municípios por natureza jurídica")
            st.dataframe(plotTable.plotTableTab2(df, 'natureza juridica'), height=200, width=500)        
    
    with empty_col:
        st.empty()
    
    with grafico_agrupado_natureza:
        st.plotly_chart(graphBar.plotGraphBar(df, 'natureza juridica', 'Natureza Jurídica'))            
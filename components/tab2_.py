import streamlit as st
from graphs import mapHeat, pieMargin, graphBar, treeMap


def layout(df, total_positivo, total_negativo, margem, tabela_margem, merge_abertura_fechamento, titulo_positivo, titulo_negativo, ano, porte, municipio, atividade):

    bloco_total_positivo, blocoTotalFechamentos, blocoMargem = st.columns(3)
    bloco_arvore = st.area_chart()
    bloco_mapa, bloco_grafico_barras = st.columns(2)
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


        
    with bloco_mapa:
        tab1, tab2 = st.tabs(["Mapa", "Tabela"])
        df_filter_map = df.copy()
        if ano != "Todos":
            df_filter_map = df_filter_map[df_filter_map["abertura"].dt.year == ano]
        if porte != "Todos":
            df_filter_map = df_filter_map[df_filter_map["porte"] == porte]
        if atividade != "Todas":
            df_filter_map = df_filter_map[df_filter_map["atividade"] == atividade]

        mapa, tabela = mapHeat.plotMap(df_filter_map)
        with tab1:
            st.plotly_chart(mapa)
        with tab2:
            st.write(tabela)

    with bloco_grafico_barras:
        with st.container():
            grafico_positivo = graphBar.plotGraphBar(df, titulo_positivo, titulo_positivo)
            grafico_negativo = graphBar.plotGraphBar(df, titulo_negativo, titulo_negativo)

            st.plotly_chart(grafico_positivo[0], use_container_width=True)
            st.plotly_chart(grafico_negativo[0], use_container_width=True)
                    
    with bloco_arvore:
        st.plotly_chart(treeMap.showGraph(), use_container_width=True)
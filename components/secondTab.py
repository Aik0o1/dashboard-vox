import streamlit as st
from graphs import mapHeat, pieMargin, graphBar, treeMap


def layout(df, ano, porte, municipio, atividade, titulo_bar1, titulo_bar2):

    bloco_arvore = st.area_chart()
    bloco_mapa, bloco_grafico_barras = st.columns(2)
    blocoTabela = st.columns(1)

    with bloco_arvore:
        st.plotly_chart(treeMap.plotMapTree(df), use_container_width=True)

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
            grafico_porte = graphBar.plotGraphBar(df, titulo_bar1,titulo_bar1)
            grafico_natureza = graphBar.plotGraphBar(df, titulo_bar2, titulo_bar2)

            st.plotly_chart(grafico_porte, use_container_width=True)
            st.plotly_chart(grafico_natureza, use_container_width=True)
                    
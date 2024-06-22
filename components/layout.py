import streamlit as st
from graphs import mapHeat, pieMargin, lineChart, graphBar


def layout(df, total_positivo, total_negativo, margem, tabela_margem, merge_abertura_fechamento, titulo_positivo, titulo_negativo, ano, porte, municipio, atividade):

    bloco_total_positivo, blocoTotalFechamentos, blocoMargem = st.columns(3)
    bloco_grafico_abertura_fechamento = subtab1, subtab2 = st.tabs(["Gráfico", "Tabela"])
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


    with bloco_grafico_abertura_fechamento[0]:
        subtab1.plotly_chart(lineChart.graph(merge_abertura_fechamento, titulo_positivo, titulo_negativo))
        
    with bloco_grafico_abertura_fechamento[1]:
        subtab2.dataframe(merge_abertura_fechamento, use_container_width=True)

    
    with bloco_mapa:
        df_filter_map = df.copy()
        if ano != "Todos":
            df_filter_map = df_filter_map[df_filter_map["abertura"].dt.year == ano]
        if porte != "Todos":
            df_filter_map = df_filter_map[df_filter_map["porte"] == porte]
        if atividade != "Todas":
            df_filter_map = df_filter_map[df_filter_map["atividade"] == atividade]

        st.plotly_chart(mapHeat.plotMap(df_filter_map))

    with bloco_grafico_barras:
        with st.container():
       
            st.plotly_chart(graphBar.plotGraphBar(df, titulo_positivo, titulo_positivo), use_container_width=True)

            st.plotly_chart(graphBar.plotGraphBar(df, titulo_negativo, titulo_negativo), use_container_width=True)

                    

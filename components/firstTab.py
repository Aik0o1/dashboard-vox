import streamlit as st
from graphs import mapHeat, pieMargin, circles, lineChart, graphBar, plotTable,stackedBar, barChartYears, barChartMonths


def layout(df, total_positivo, total_negativo, margem, tabela_margem, merge_abertura_fechamento, titulo_positivo, titulo_negativo, ano, porte, municipio, atividade):

    bloco_total_positivo, blocoTotalFechamentos, blocoMargem = st.columns(3)
    grafico_abertura_fechamento_anual = st.area_chart()
    grafico_abertura_fechamento_mensal = st.area_chart()
    grafico_agrupado_porte, grafico_agrupado_natureza = st.columns(2)
    bloco_mapa,  tabela_abertura_fechamento = st.columns(2)
    
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


    with grafico_abertura_fechamento_anual:
        
        st.plotly_chart(barChartYears.graph(merge_abertura_fechamento))
        
    with grafico_abertura_fechamento_mensal:
        st.plotly_chart(barChartMonths.graph(df))

    with bloco_mapa:
        st.header("Cidades Destaque")
        st.plotly_chart(mapHeat.plotMap(df))

    

    with tabela_abertura_fechamento:
        tabela_abertura, tabela_fechamento = st.columns(2)
        with tabela_abertura:
            st.header(" ")
            st.dataframe(plotTable.plotTableTab1(df, 'anoAbertura', 'Aberturas'))
        
        with tabela_fechamento:
            st.header(" ")
            st.dataframe(plotTable.plotTableTab1(df, 'anoFechamento', 'Fechamentos'))

            
            # with col5:
            #     st.plotly_chart(circles.graph(tabela_margem), use_container_width=True)
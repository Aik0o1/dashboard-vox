import streamlit as st
from graphs import (
    barChartYears,
    barChartMonths,
    mapHeat,
    pieMargin,
    stackedBar,
    circles,
    plotTable,
    graphBar,
    treeMap,
)

# from graphs import mapHeat, pieMargin, lineChart, graphBar, plotTable,stackedBar, barChartYears, barChartMonths


def layout(
    df,
    total_positivo,
    total_negativo,
    margem,
    tabela_margem,
    merge_abertura_fechamento,
):
    # st.image('https://portal.pi.gov.br/jucepi/wp-content/uploads/sites/47/2023/03/jucepi_logo-768x177.jpg')
    bloco_total_positivo, blocoTotalFechamentos, blocoMargem = st.columns(3)
    
    bloco_total_positivo = bloco_total_positivo.container(border=True)
    blocoTotalFechamentos = blocoTotalFechamentos.container(border=True)
    blocoMargem = blocoMargem.container(border=True)
    
    grafico_abertura_fechamento_anual = st.area_chart()
    grafico_abertura_fechamento_mensal = st.area_chart()

    bloco_mapa, tabela_abertura_fechamento = st.columns(2)

    # grafico_portes_individuais, grafico_porte_unificado = st.tabs(['Empresas por porte (visão individualizada)', 'Empresas por porte (visão unificada)'])
    
    grafico_natureza_juridica = st.area_chart()
    grafico_porte_unificado = st.area_chart()
    bloco_arvore = st.area_chart()

    with bloco_total_positivo:
        st.metric(label="Total de aberturas", value=total_positivo)
        st.write(" ")

    with blocoTotalFechamentos:
        st.metric(label="Total de Fechamentos", value=total_negativo)
        st.write(" ")

    with blocoMargem:
            st.metric(label="Margem", value=margem, delta=str(f"{((margem / total_positivo) * 100):.0f}%"))
        # with col2:
        #     st.plotly_chart(pieMargin.graph(tabela_margem), use_container_width=True)
            #st.plotly_chart(pieMargin.graph(tabela_margem, margem), use_container_width=True)

    with grafico_abertura_fechamento_anual:
        st.plotly_chart(barChartYears.graph(merge_abertura_fechamento))

    with grafico_abertura_fechamento_mensal:
        st.plotly_chart(barChartMonths.graph(df))

    with bloco_mapa:
        st.markdown('**Mapa de calor - Aberturas**')
        st.plotly_chart(mapHeat.plotMap(df))

    with tabela_abertura_fechamento:
        tabela_abertura, tabela_fechamento = st.columns(2)
        with tabela_abertura:
            st.markdown("**Aberturas por município**")
            st.dataframe(plotTable.plotTableTab1(df, "anoAbertura", "Aberturas"), use_container_width=True, hide_index=True)

        with tabela_fechamento:
            st.markdown("**Fechamentos por município**")
            st.dataframe(plotTable.plotTableTab1(df, "anoFechamento", "Fechamentos"), use_container_width=True, hide_index=True)

    with grafico_porte_unificado:
        st.plotly_chart(stackedBar.graph(df))

    with grafico_natureza_juridica:
        st.plotly_chart(
            graphBar.plotGraphBar(df, "natureza juridica", "Natureza Jurídica")
        )

    with bloco_arvore:
        st.plotly_chart(treeMap.plotMapTree(df), use_container_width=True)

import streamlit as st
from graphs import (
    barChartYears,
    barChartMonths,
    mapHeat,
    pieMargin,
    stackedBar,
    graphBar,
    treeMap,
    plotTable
)

from relatorio import gerar_relatorio_word

def layout(
    df,
    total_positivo,
    total_negativo,
    margem,
    tabela_margem,
    merge_abertura_fechamento,
):
    bloco_total_positivo, blocoTotalFechamentos, blocoMargem = st.columns(3)
    
    bloco_total_positivo = bloco_total_positivo.container()
    blocoTotalFechamentos = blocoTotalFechamentos.container()
    blocoMargem = blocoMargem.container()
    
    grafico_abertura_fechamento_anual = st.area_chart()
    grafico_abertura_fechamento_mensal = st.area_chart()

    bloco_mapa, tabela_abertura_fechamento = st.columns(2)
    
    grafico_natureza_juridica = st.area_chart()
    grafico_porte_unificado = st.area_chart()
    bloco_arvore = st.area_chart()

    with bloco_total_positivo:
        st.metric(label="Total de aberturas", value=total_positivo)

    with blocoTotalFechamentos:
        st.metric(label="Total de Fechamentos", value=total_negativo)

    with blocoMargem:
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Margem", value=margem)
        with col2:
            grafico_margem = pieMargin.graph(tabela_margem)
            st.plotly_chart(grafico_margem, use_container_width=True)

    with grafico_abertura_fechamento_anual:
        grafico_ano = barChartYears.graph(merge_abertura_fechamento)
        st.plotly_chart(grafico_ano)

    with grafico_abertura_fechamento_mensal:
        grafico_mes = barChartMonths.graph(df)
        st.plotly_chart(grafico_mes)

    with bloco_mapa:
        st.markdown('**Mapa de calor - Aberturas**')
        grafico_mapa = mapHeat.plotMap(df)
        st.plotly_chart(grafico_mapa)

    with tabela_abertura_fechamento:
        tabela_abertura, tabela_fechamento = st.columns(2)
        with tabela_abertura:
            st.markdown("**Aberturas por município**")
            st.dataframe(plotTable.plotTableTab1(df, "anoAbertura", "Aberturas"), use_container_width=True, hide_index=True)

        with tabela_fechamento:
            st.markdown("**Fechamentos por município**")
            st.dataframe(plotTable.plotTableTab1(df, "anoFechamento", "Fechamentos"), use_container_width=True, hide_index=True)

    with grafico_porte_unificado:
        grafico_porte = stackedBar.graph(df)
        st.plotly_chart(grafico_porte)

    with grafico_natureza_juridica:
        grafico_natureza = graphBar.plotGraphBar(df, "natureza juridica", "Natureza Jurídica")
        st.plotly_chart(grafico_natureza)

    with bloco_arvore:
        grafico_arvore = treeMap.plotMapTree(df)
        st.plotly_chart(grafico_arvore, use_container_width=True)

    # Lista de gráficos e nomes para o relatório
    graficos = [
        grafico_margem, 
        grafico_ano, 
        grafico_mes, 
        grafico_mapa, 
        grafico_porte, 
        grafico_natureza, 
        grafico_arvore
    ]
    
    nomes_arquivos = [
        "grafico_margem", 
        "grafico_ano", 
        "grafico_mes", 
        "grafico_mapa", 
        "grafico_porte", 
        "grafico_natureza", 
        "grafico_arvore"
    ]

    # Botão para gerar o relatório
    if st.button('Gerar Relatório'):
        gerar_relatorio_word(graficos, nomes_arquivos, "relatorio")
        st.success('Relatório gerado com sucesso!')


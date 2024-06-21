import pandas as pd
import plotly.express as px

def lineChart(df_filtered):
    aberturas_por_ano = df_filtered.groupby('anoAbertura').size().reset_index(name='aberturas')
    fechamentos_por_ano = df_filtered.dropna(subset=['anoFechamento']).groupby('anoFechamento').size().reset_index(name='fechamentos')

    aberturas_por_ano.rename(columns={'anoAbertura': 'ano'}, inplace=True)
    fechamentos_por_ano.rename(columns={'anoFechamento': 'ano'}, inplace=True)

    dados_combined = pd.merge(aberturas_por_ano, fechamentos_por_ano, on='ano', how='outer').fillna(0)

    # graficos
    fig_abertura_fechamento = px.line(dados_combined, x='ano', y=['aberturas', 'fechamentos'], 
        title='Número de Aberturas e Fechamentos por Ano',
        labels={'value': 'Quantidade', 'variable': 'Tipo'})
    
    return fig_abertura_fechamento
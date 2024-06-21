import pandas as pd
import plotly.express as px

def lineChart(df):
    ativasAno = df[df['status']=="ativa"].groupby('anoAbertura').size().reset_index(name='ativas')
    inativasAno = df[df['status']=="inativa"].groupby('anoFechamento').size().reset_index(name='inativas')

    ativasAno.rename(columns={'anoAbertura': 'ano'}, inplace=True)
    inativasAno.rename(columns={'anoFechamento': 'ano'}, inplace=True)

    dados_combined = pd.merge(ativasAno, inativasAno, on='ano', how='outer').fillna(0)
    
    # graficos
    fig_abertura_fechamento = px.line(dados_combined, x='ano', y=['ativas', 'inativas'], 
        title='Número de empresas ativas e inativas por ano',
        labels={'value': 'Quantidade', 'variable': 'Tipo'})
    
    fig_abertura_fechamento.show()


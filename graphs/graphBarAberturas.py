import pandas as pd
import plotly.express as px

df = pd.read_csv('assets\dadosFakess.csv')

def plotGraphAberturas():
    aberturas_por_municipio = df.groupby('municipio').size().reset_index(name='aberturas')
    fechamentos_por_municipio = df.dropna(subset=['anoFechamento']).groupby('municipio').size().reset_index(name='fechamentos')
    dados_municipio = pd.merge(aberturas_por_municipio, fechamentos_por_municipio, on='municipio', how='outer').fillna(0)
    dados_municipio.rename(columns={'municipio': 'name'}, inplace=True)
    dados_municipio_sorted = dados_municipio.sort_values(by='aberturas', ascending=False)
    dados_municipio_melhores = dados_municipio_sorted.head()
    fig = px.bar(dados_municipio_melhores, x="aberturas", y="name", orientation='h', title='Em abertura',height=300)
    
    return fig
import plotly.express as px

def graph (dados_combinados, titulo_positivo, titulo_negativo, eixo_x):
    fig_abertura_fechamento = px.line(dados_combinados, x=eixo_x, y=[f'{titulo_positivo}', f'{titulo_negativo}'], 
    title=f'Número de {titulo_positivo} e {titulo_negativo} por {eixo_x}',
    labels={'value': 'Quantidade', 'variable': 'Tipo'})
    
    return fig_abertura_fechamento
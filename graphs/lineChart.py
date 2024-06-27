import plotly.express as px
import plotly.graph_objects as go


def graph (dados_combinados, titulo_positivo, titulo_negativo, eixo_x):
    fig_abertura_fechamento = px.bar(dados_combinados['aberturas'], 
    title=f'Número de {titulo_positivo} por mês',
    labels={'value': 'Quantidade', 'variable': 'Tipo'})
    
    anos=list(range(2000,2025))
    fig = go.Figure(data=[
        go.Bar(name='Aberturas', x=anos, y=dados_combinados['aberturas']),
        go.Bar(name='Fechamentos', x=anos, y=dados_combinados['fechamentos'])
    ])

    fig.update_layout(barmode='group')
    
    
    fig_abertura_fechamento = go.Figure()
    fig_abertura_fechamento.add_trace(go.Bar(x=anos,
                    y=dados_combinados['aberturas'],
                    marker=dict(color='#004f89'),  # Cor para aberturas
    name='Aberturas'  # Nome da legenda
    ),
                    
                    )
    fig_abertura_fechamento.add_trace(go.Bar(x=anos,
                    y=dados_combinados['fechamentos'],
                     marker=dict(color='#dfbf5c'),  # Cor para fechamentos
    name='Fechamentos'  # Nome da legenda
                    ))

    fig_abertura_fechamento.update_layout(
        title='Aberturas por mês',
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        bargap=0.3, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
    

    return fig, fig_abertura_fechamento
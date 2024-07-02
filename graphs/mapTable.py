from plotly.subplots import make_subplots

def mapa_tbaela(mapa, tabela):
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.6, 0.4],
        specs=[[{'type': 'scatter'}, {'type': 'table'}]]
    )

    fig.add_trace(mapa, row=1, col=1)
    fig.add_trace(tabela, row=1, col=1)
    
    return fig
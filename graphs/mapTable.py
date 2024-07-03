from plotly.subplots import make_subplots
from graphs import mapHeat, plotTable
import plotly.graph_objects as go

def mapa_tbaela(df):

    mapa = mapHeat.plotMap(df)
    tabela = plotTable.plotTableTab2(df)

    fig = make_subplots(
        rows=1,
        cols=2,
        column_widths=[0.5, 0.5],
        specs=[[{"type": "choropleth"}, {"type": "table"}]],
    )

    for trace in mapa.data:
        fig.add_trace(trace, row=1, col=1)
        
    fig.add_trace(
            go.Table(
                header=dict(
                    values=list(tabela.columns),
                    fill_color="white",
                    align="left",
                ),
                cells=dict(
                    values=[tabela[col] for col in tabela.columns],
                    fill_color="white",
                    align="left",
                ),
            ),
            row=1,
            col=2,
        )

    fig.update_layout(height=600, title_text="Empresas por Município e Ano")
    
    return fig

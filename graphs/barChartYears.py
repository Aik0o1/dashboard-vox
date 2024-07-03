import plotly.express as px
import plotly.graph_objects as go


def graph (dados_combinados):
    
    anos = list(range(2000,2025))
    aberturas = dados_combinados['aberturas']
    fechamentos = dados_combinados['fechamentos']
    
    fig_abertura_fechamento = go.Figure()
    fig_abertura_fechamento.add_trace(go.Bar(x=anos,
        y = aberturas,
        marker = dict(color='#034EA2'),  
        name ='Aberturas',
        text = aberturas
    ))
    fig_abertura_fechamento.add_trace(go.Bar(x=anos,
        y = fechamentos,
        marker=dict(color='#FDC742'), 
        name='Fechamentos',
        text=fechamentos  
    ))

    fig_abertura_fechamento.update_layout(
        title='Aberturas x Fechamentos (por ano)',
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        bargap=0.3, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
    

    return fig_abertura_fechamento
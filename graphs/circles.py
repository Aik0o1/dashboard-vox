import plotly.graph_objects as go
from plotly.subplots import make_subplots

def graph(df):
    # Agrupar por porte e calcular as quantidades
    labels = df.groupby('porte').size().reset_index(name='quantidade')

    # Calcular a soma total de todas as quantidades
    soma_total = labels['quantidade'].sum()

    colors = ['#d8d8d8', '#8acbb5']

    # Preparar valores dinamicamente
    data = []
    
    for i, (porte, quantidade) in enumerate(labels[['porte', 'quantidade']].itertuples(index=False)):
        labels_categoria = ['Total', porte.capitalize()]
       
        data.append(go.Pie(labels=labels_categoria, values=[soma_total, quantidade], name=porte.capitalize()))
        
    fig = make_subplots(rows=1, cols=len(labels), specs=[[{'type':'domain'}]*len(labels)],  subplot_titles=labels['porte'])

    for i, trace in enumerate(data):
        fig.add_trace(trace, 1, i + 1)

    fig.update_traces(hole=.7, hoverinfo="label+percent", marker=dict(colors=colors))
    fig.update_layout(
        title_text="Empresas por porte",
        showlegend=False,
        height=300,
        margin=dict(b=50, r=20, l=20),
        
    )

    return fig

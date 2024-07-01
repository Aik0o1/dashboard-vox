import plotly.graph_objects as go

def graph(df):
    portes = df.groupby('porte').size()

    natureza_juridica = df.groupby('natureza juridica').size()
    
    fig_natureza = go.Figure(
        data=[go.Bar(x=df['natureza juridica'].unique(), y=natureza_juridica)],
        )          
    fig_natureza.update_layout(barmode='stack', title="Naturezas jurídicas")
    
    fig = go.Figure(
        data=[go.Bar(x=df['porte'].unique(), y=portes)],
        )          
    fig.update_layout(barmode='stack', title="Portes")
    
    return fig, fig_natureza
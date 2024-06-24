import plotly.express as px

def plotGraphBar(df, metric, title):
    if metric == 'aberturas':
        data = df.groupby('municipio').size().reset_index(name=metric)
    elif metric == 'fechamentos':
        data = df.dropna(subset=['anoFechamento']).groupby('municipio').size().reset_index(name=metric)
    
    elif metric == 'ativas':
        data = df[df['status'] == "ativa"].groupby('municipio').size().reset_index(name=metric)
    elif metric == 'inativas':
        data = df[df['status'] == "inativa"].groupby('municipio').size().reset_index(name=metric)
    
    data_sorted = data.sort_values(by=metric, ascending=False).head()
    fig = px.bar(data_sorted, x=metric, y="municipio", orientation="h", title=f"{title.capitalize()}", height=250)
    return fig, data
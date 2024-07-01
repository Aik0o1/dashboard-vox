# import plotly.express as px

# def graph(df_margem):
#     fig_margem = px.pie(df_margem, values='Quantidade', names='Tipo', hole=0.7)
#     fig_margem.update_traces(textinfo='none'),

#     fig_margem.update_layout(
#         showlegend=False,
#         margin=dict(t=0, b=0, l=0, r=0),
#         height=100,
#     )

#     return fig_margem

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def graph(df):
    labels = df.groupby('porte').size().reset_index(name='quantidade')
    
    labels_me = ['Total', 'ME']
    labels_mei = ['Total', 'MEI']
    labels_pequena = ['Total', 'Pequena']
    labels_media_grande = ['Total', 'Média/Grande']
    
    sum_outside_me = labels.loc[labels['porte'] == 'me' ]['quantidade'].sum()
    sum_outside_mei = labels.loc[labels['porte'] == 'mei' ]['quantidade'].sum()
    sum_outside_pequena = labels.loc[labels['porte'] == 'pequena' ]['quantidade'].sum()
    sum_outside_media_grande = labels.loc[labels['porte'] == 'media/grande' ]['quantidade'].sum()
    soma_total = labels['quantidade'].sum()

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=1, cols=4, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
    
    fig.add_trace(go.Pie(labels=labels_me, values=[soma_total, sum_outside_me], name="ME"),
                1, 1)
    fig.add_trace(go.Pie(labels=labels_mei, values=[soma_total, sum_outside_mei], name="MEI"),
                1, 2)
    fig.add_trace(go.Pie(labels=labels_pequena, values=[soma_total, sum_outside_pequena], name="Pequenas"),
                1, 3)
    fig.add_trace(go.Pie(labels=labels_media_grande, values=[soma_total, sum_outside_media_grande], name="Médias/Grandes"),
                1, 4)

    fig.update_traces(hole=.7, hoverinfo="label+percent+name", textinfo='none')

    fig.update_layout(
        title_text="Empresas por porte",
                    showlegend=False,
                    height=300,
                    
        annotations=[dict(text='GHG', x=0.08, y=0.5, font_size=12, showarrow=False),
                    dict(text='CO2', x=0.37, y=0.5, font_size=12, showarrow=False),
                    dict(text='H2O', x=0.63, y=0.5, font_size=12, showarrow=False),
                    dict(text='HB20', x=0.92, y=0.5, font_size=12, showarrow=False),
                    
                    ])

    return fig

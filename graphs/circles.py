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

def graph(df_margem):
    labels = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
            "Rest of World"]

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=1, cols=4, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
    
    fig.add_trace(go.Pie(labels=labels, values=[15,16], name="GHG Emissions"),
                1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
                1, 2)
    fig.add_trace(go.Pie(labels=labels, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
                1, 3)
    fig.add_trace(go.Pie(labels=labels, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
                1, 4)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+percent+name", textinfo='none')

    fig.update_layout(
        title_text="Global Emissions 1990-2011",
                    showlegend=False,
                    height=300,
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='GHG', x=0.2, y=0.5, font_size=12, showarrow=False),
                    dict(text='CO2', x=0.3, y=0.5, font_size=12, showarrow=False),
                    dict(text='H2O', x=0.4, y=0.5, font_size=12, showarrow=False),
                    dict(text='HB20', x=0.5, y=0.5, font_size=12, showarrow=False),
                    
                    ])

    return fig
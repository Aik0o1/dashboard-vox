import plotly.graph_objects as go
import plotly.express as px


def graph(df):

    # This dataframe has 244 lines, but 4 distinct values for `day`

    portes = df.groupby("porte").size().reset_index(name="quantidade")

    # natureza_juridica = df.groupby('natureza juridica').size()

    fig = px.pie(portes, values=portes["quantidade"], names=portes["porte"])

    fig.update_traces(hole=0.5, hoverinfo="label+percent")
    fig.update_layout(
        title_text="Empresas por porte",
        showlegend=False,
        height=300,
        margin=dict(b=50, r=20, l=20),
    )

    fig.update_traces(
        textfont_size=16,
        textinfo="label+percent",
        textposition="outside",
        hovertemplate="<b>%{label} </b> <br> Quantidade: %{value}<br>",
    )

    # fig_natureza = go.Figure(
    #     data=[go.Bar(x=df['natureza juridica'].unique(), y=natureza_juridica)],
    #     )
    # fig_natureza.update_layout(barmode='stack', title="Naturezas jurídicas")

    # fig = go.Figure(
    #     data=[go.Bar(x=df['porte'].unique(), y=portes)],
    #     )
    # fig.update_layout(barmode='stack', title="Portes")

    return fig

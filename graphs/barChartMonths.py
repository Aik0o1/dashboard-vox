import plotly.graph_objects as go


def graph(df):
    meses = [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dez",
    ]
    aberturas = df.groupby("mesAbertura").size()
    fechamentos = df.groupby("mesFechamento").size()

    fig_aberturas_months = go.Figure()

    fig_aberturas_months.add_trace(
        go.Bar(
            x=meses,
            y=aberturas,
            marker=dict(color="#034ea2"),
            name="Aberturas",
            text=aberturas,
        ),
    )

    fig_aberturas_months.add_trace(
        go.Bar(
            x=meses,
            y=fechamentos,
            marker=dict(color="#fdb913"),
            name="Fechamentos",
            text=fechamentos,
        )
    )

    fig_aberturas_months.update_layout(
        title="Aberturas x Fechamentos (por mês)",
        legend=dict(
            x=1.0,
            y=1.0,
            bgcolor="rgba(255, 255, 255, 0)",
            bordercolor="rgba(255, 255, 255, 0)",
        ),
        yaxis=dict(showgrid=False, visible=False),
        bargap=0.3,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1,  # gap between bars of the same location coordinate.
    )

    fig_aberturas_months.update_traces(
        textfont_size=16, textangle=0, textposition="outside", cliponaxis=False, hoverinfo='none'
    )
    return fig_aberturas_months

import plotly.express as px
import pandas as pd


def plotMapTree(df):
    dfAtividadeQtd = df.groupby("atividade").size().reset_index(name="Qtd Empresa")
    fig = px.treemap(
        dfAtividadeQtd,
        path=[px.Constant("Atividades"), "atividade", "Qtd Empresa"],
        values="Qtd Empresa",
        title="Empresas por atividade",
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return fig

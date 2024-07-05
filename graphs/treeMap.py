import plotly.express as px
import pandas as pd


def break_text(text, max_length):
    # Quebrar o texto em múltiplas linhas com base no comprimento máximo
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if (
            sum(len(w) for w in current_line) + len(word) + len(current_line) - 1
            < max_length
        ):
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]

    if current_line:
        lines.append(" ".join(current_line))

    return "<br>".join(lines)


def plotMapTree(df):
    dfAtividadeQtd = df.groupby("atividade").size().reset_index(name="Qtd Empresa")
    dfAtividadeQtd["atividade"] = dfAtividadeQtd["atividade"].apply(
        lambda x: break_text(x, 20)
    )

    fig = px.treemap(
        dfAtividadeQtd,
        path=[px.Constant("Atividades"), "atividade"],
        values="Qtd Empresa",
        title="Empresas por Atividade",
    )
    fig.update_traces(
        root_color="lightgrey",
        textfont_size=12,
        hovertemplate="<b>%{label} </b> <br> Quantidade: %{value}<br>",
    )
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return fig

import plotly.express as px


def graph(df_margem):
    fig_margem = px.pie(
        df_margem,
        values="Quantidade",
        names="Tipo",
        hole=0.6,
        color_discrete_sequence=["#034EA2", "#d8d8d8"],
    )

    # Gráfico de pizza sem legenda
    fig_margem.update_layout(
        showlegend=False,
        margin=dict(t=0, b=0, l=0, r=0),
        height=70,
    )
    
    return fig_margem

# import streamlit as st
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# # Função para criar o gráfico de pizza
# def graph(tabela_margem, margem):
#     fig = make_subplots(
#         rows=1,
#         cols=2,
#         specs=[[{"type": "indicator"}, {"type": "pie"}]],
#         subplot_titles=["Margem", "Distribuição de Margem"]
#     )

#     # Indicador de margem
#     fig.add_trace(
#         go.Indicator(
#             mode="number",
#             value=margem,
#             title={"text": "Margem"}
#         ),
#         row=1, col=1
#     )

#     # Gráfico de pizza
#     fig.add_trace(
#         go.Pie(
#             labels=tabela_margem['Tipo'],
#             values=tabela_margem['Quantidade'],
#             textinfo="label+percent"
#         ),
#         row=1, col=2
#     )

#     # Ajuste do layout dos subplots
#     fig.update_layout(
#         margin=dict(t=50, l=25, r=25, b=25),
#         uniformtext=dict(minsize=12, mode="show"),
#     )

#     return fig
import plotly.express as px

def graph(df_margem):
    fig_margem = px.pie(df_margem, values='Quantidade', names='Tipo', hole=0.6)

# Gráfico de pizza sem legenda
    fig_margem.update_layout(
        showlegend=False,
        margin=dict(t=0, b=0, l=0, r=0),
        height=70  # Ajuste a altura conforme necessário
    )

    return fig_margem
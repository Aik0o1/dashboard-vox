import plotly.express as px


def plotGraphBar(df, metric, title):
    if metric == "aberturas" or metric == "fechamentos":
        if metric == "aberturas":
            data = df.groupby("municipio").size().reset_index(name=metric)
        elif metric == "fechamentos":
            data = (
                df.dropna(subset=["anoFechamento"])
                .groupby("municipio")
                .size()
                .reset_index(name=metric)
            )

        data_sorted = data.sort_values(by=metric, ascending=False).head()
        fig = px.bar(
            data_sorted,
            x=metric,
            y="municipio",
            orientation="h",
            title=f"{title.capitalize()}",
            height=250,
        )

    elif metric == "porte" or metric == "natureza juridica":
        if metric == "porte":
            data = df.groupby("porte").size().reset_index(name="quantidade")

        elif metric == "natureza juridica":
            data = df.groupby("natureza juridica").size().reset_index(name="quantidade")

        data_sorted = data.sort_values(by=metric, ascending=False).head()
        fig = px.bar(
            data_sorted,
            x=metric,
            y="quantidade",
            text="quantidade",
            orientation="v",
            title=f"Empresas por {title.lower()}",
        )
        fig.update_layout(yaxis=dict(showgrid=False, visible=False))
        
        fig.update_traces(
            hoverinfo="none",
            textfont_size=16,
            textangle=0,
            textposition="outside",
            cliponaxis=False,
        )
    return fig

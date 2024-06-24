import pandas as pd
import plotly.express as px
import geopandas as gpd
import plotly.express as px

def plotMap(df):

    aberturas_por_municipio = df.groupby('municipio').size().reset_index(name='aberturas')
    fechamentos_por_municipio = df.dropna(subset=['anoFechamento']).groupby('municipio').size().reset_index(name='fechamentos')
    dados_municipio = pd.merge(aberturas_por_municipio, fechamentos_por_municipio, on='municipio', how='outer').fillna(0)
    dados_municipio.rename(columns={'municipio': 'name'}, inplace=True)

    # Carrega os dados dos municípios do Piauí a partir de um arquivo GeoJSON
    gdf = gpd.read_file("https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-22-mun.json")

    #colunas do GeoDataFrame

    gdf = gdf.merge(dados_municipio, on='name')
    # mapa
    figMapa = px.choropleth(gdf,
                        geojson=gdf.geometry,
                        locations=gdf.index,
                        color="aberturas",
                        hover_name="name",
                        projection="mercator",
                        color_continuous_scale="Blues")

    # Atualizar layout do mapa
    figMapa.update_geos(fitbounds="locations", visible=False)
    figMapa.update_layout(
        title_text="Cidades Destaque",
        margin={"r":0,"t":100,"l":0,"b":0})

    return figMapa, dados_municipio

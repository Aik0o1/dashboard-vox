import streamlit as st
from graphs import mapHeat

def blocoMapa(df,ano, porte, atividade):
    df_filter_map = df.copy()
    if ano != "Todos":
        df_filter_map = df_filter_map[df_filter_map["abertura"].dt.year == ano]
    if porte != "Todos":
        df_filter_map = df_filter_map[df_filter_map["porte"] == porte]
    if atividade != "Todas":
        df_filter_map = df_filter_map[df_filter_map["atividade"] == atividade]

    return st.plotly_chart(mapHeat.plotMap(df_filter_map))
    

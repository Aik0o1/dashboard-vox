import pandas as pd

def plotTableTab1(df, metric, title):

    df_metric = df.dropna(subset=[metric]).groupby('municipio').size().reset_index(name=title)
    df_metric = df_metric[['municipio', title]]
    df_sorted = df_metric.sort_values(by=title, ascending=False)
    df_sorted.rename(columns={'municipio': 'Município'}, inplace=True)

    return df_sorted 

def plotTableTab2(df, metric):
    df_grouped = df.groupby(["municipio", metric]).size().reset_index(name="Qtd")
    df_sorted = df_grouped.sort_values(by="Qtd", ascending=False)
    df_sorted.rename(columns={'municipio': 'Município', 'porte':'Porte', 'Qtd': 'Quantidade', 'natureza juridica':'Natureza'}, inplace=True)


    return df_sorted

def plotTable(df):
    # Agrupar por município, ano de abertura e ano de fechamento
    df_aberturas = (
        df.dropna(subset=["anoAbertura"])
        .groupby(["municipio", "anoAbertura"])
        .size()
        .reset_index(name="Aberturas")
    )
    df_fechamentos = (
        df.dropna(subset=["anoFechamento"])
        .groupby(["municipio", "anoFechamento"])
        .size()
        .reset_index(name="Fechamentos")
    )

    # Renomear colunas para permitir junção
    df_aberturas.rename(columns={"anoAbertura": "Ano"}, inplace=True)
    df_fechamentos.rename(columns={"anoFechamento": "Ano"}, inplace=True)

    # Mesclar os DataFrames de aberturas e fechamentos
    df_combined = pd.merge(
        df_aberturas, df_fechamentos, on=["municipio", "Ano"], how="outer"
    )

    # Substituir NaNs por 0
    df_combined = df_combined.fillna(0)

    # Converter colunas numéricas para inteiros
    df_combined[["Aberturas", "Fechamentos"]] = df_combined[
        ["Aberturas", "Fechamentos"]
    ].astype(int)

    # Ordenar por município e ano
    df_combined.sort_values(by=["municipio", "Ano"], inplace=True)

    return df_combined



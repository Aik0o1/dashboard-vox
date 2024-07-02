import pandas as pd


def plotTableTab2(df):
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

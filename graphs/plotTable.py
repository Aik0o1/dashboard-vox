def plotTableTab1(df, metric, title):

    df_metric = df.dropna(subset=[metric]).groupby('municipio').size().reset_index(name=title)

    df_metric = df_metric[['municipio', title]]
    print(df_metric)
    df_sorted = df_metric.sort_values(by=title, ascending=False)
    
    # df_fechamento = df[['municipio', metric]]
    # df_sorted_fechamento = df_fechamento.sort_values(by=metric, ascending=False)
    # print(df)
    return df_sorted 

def plotTableTab2(df, metric):
    df_grouped = df.groupby(['municipio', metric]).size().reset_index(name='Qtd')
    df_sorted = df_grouped.sort_values(by='Qtd', ascending=False)

    return df_sorted
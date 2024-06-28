import pandas as pd

def load_and_prepare_data(df): 
    df['abertura'] = pd.to_datetime(df['abertura'])
    df['fechamento'] = pd.to_datetime(df['fechamento'])
    df = df.sort_values(by='municipio')

    #Total de aberturas, fechamentos e margem_abertura_fechamento
    total_aberturas = df['anoAbertura'].count()
    total_fechamentos = df['anoFechamento'].count()
    margem_abertura_fechamento = total_aberturas - total_fechamentos

    # Preparar dados para o gráfico de margem_abertura_fechamento
    data_margem_abertura_fechamento = {
        'Tipo': ['Aberturas', 'Fechamentos'],
        'Quantidade': [total_aberturas, total_fechamentos]
    }

    df_margem_abertura_fechamento = pd.DataFrame(data_margem_abertura_fechamento)
    

    #filtro de dados para grafico de abertura vs fechamentos
    aberturas_por_ano = df.groupby('anoAbertura').size().reset_index(name='aberturas')
    fechamentos_por_ano = df.dropna(subset=['anoFechamento']).groupby('anoFechamento').size().reset_index(name='fechamentos')

    aberturas_por_ano.rename(columns={'anoAbertura': 'ano'}, inplace=True)
    fechamentos_por_ano.rename(columns={'anoFechamento': 'ano'}, inplace=True)

    merge_abertura_fechamento = pd.merge(aberturas_por_ano, fechamentos_por_ano, on='ano', how='outer').fillna(0)
    
    #Filtro para grafico de porte
    df_porte = df.groupby('porte').size().reset_index(name='quantidade')
    df_natureza = df.groupby('natureza juridica').size().reset_index(name='quantidade')

    # filtro para grafico de natureza
    return (total_aberturas, total_fechamentos, margem_abertura_fechamento, 
            df_margem_abertura_fechamento, merge_abertura_fechamento, df_porte, df_natureza)
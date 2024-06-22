import pandas as pd

def load_and_prepare_data(df):
    #df = pd.read_csv("assets/dadosFakess.csv")
    
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
    
    
    # Total de ativas, inativas e margem_ativas_inativas
    total_ativas = df[df['status'] == 'ativa'].shape[0]
    total_inativas = df[df['status'] == 'inativa'].shape[0]
    margem_ativas_inativas = total_ativas - total_inativas


    data_margem_ativas_inativas = {
        'Tipo': ['Ativas', 'Inativas'],
        'Quantidade': [total_ativas, total_inativas]
    }
    df_margem_ativas_inativas = pd.DataFrame(data_margem_ativas_inativas)

     # Filtro de dados para gráfico de ativas vs inativas
    ativas_por_ano = df[df['status'] == 'ativa'].groupby('anoAbertura').size().reset_index(name='ativas')
    inativas_por_ano = df[df['status'] == 'inativa'].groupby('anoFechamento').size().reset_index(name='inativas')

    ativas_por_ano.rename(columns={'anoAbertura': 'ano'}, inplace=True)
    inativas_por_ano.rename(columns={'anoFechamento': 'ano'}, inplace=True)

    merge_ativas_inativas = pd.merge(ativas_por_ano, inativas_por_ano, on='ano', how='outer').fillna(0)
    
    
    return (total_aberturas, total_fechamentos, margem_abertura_fechamento, 
            df_margem_abertura_fechamento, merge_abertura_fechamento,
            total_ativas, total_inativas, margem_ativas_inativas, df_margem_ativas_inativas, merge_ativas_inativas)
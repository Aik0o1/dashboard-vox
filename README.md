## Dashboard Vox

### Descrição

Este projeto é um dashboard interativo desenvolvido em `Streamlit`, que tem como objetivo exibir dados de empresas registradas à Junta Comercial do Piauí, trazendo números de aberturas, fechamentos, comparativos com filtros personalizáveis e destaques de forma intuitiva.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `assets`: Contém dados de teste gerados pelo site [Mockaroo](https://www.mockaroo.com/).
- `graphs`: Contém os gráficos de margem e mapa de calor, retornados em funções separadas.
- `dashboard.py`: Arquivo principal que executa o dashboard.
- `requirements.txt`: Arquivo de dependências necessárias para rodar o projeto.

## Instalação

Para instalar as dependências do projeto, siga os passos abaixo:

1. Clone este repositório:
    ```bash
    git clone https://github.com/Aik0o1/dashboard-vox.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd dashboard-vox
    ```
3. Instale as dependências utilizando o `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para rodar o dashboard, utilize o comando abaixo:
```bash
streamlit run dashboard.py
```
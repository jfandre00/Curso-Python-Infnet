from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


URL = 'https://www.tiobe.com/tiobe-index/'

def acessar_url(URL):
    try:
        html = urlopen(URL)
    except Exception as ex:
        print("Erro: acesso ")
        exit() # Encerra o programa pois não foi possível acessar a URL
    return html

def exibir_cabecalho(bs):
    print(bs.h1.text)

def obter_tabela(bs):
    # Localizando a tabela
    tabela_html = bs.find('table', id='top20')
    return tabela_html

def converter_tabela(tabela):
    df = pd.read_html(str(tabela))[0] # Convertendo a tabela HTML para um DataFrame
    return df

def limpar_df(df):
    df.drop("Change", axis=1, inplace=True) # Removendo a coluna "Change"
    df.drop("Programming Language", axis=1, inplace=True) # Removendo a coluna "Programming Language"
    #inplace=True: altera o DataFrame original, não criando um novo
    df.rename(columns={"Programming Language.1": "Language"}, inplace=True) # Renomeando a coluna "Programming Language.1" para "Language"
    df.rename(columns={"Change.1": "Change"}, inplace=True) # Renomeando a coluna "Change.1" para "Change"
    df[['Ratings']] = df[['Ratings']].replace("%", "", regex=True).astype(float) # Removendo o caractere "%" da coluna "Ratings" e convertendo para float
    #Regex = True: indica que a substituição será feita com base em uma expressão regular
    df[['Change']] = df[['Change']].replace("%", "", regex=True).astype(float) # Removendo o caractere "%" da coluna "Change" e convertendo para float

    return df

def numero_linguagens(df):
    print("Número de linguagens de programação: ", df.shape[0]) # Exibindo o número de linhas do DataFrame

def linguagem_mais_usada(df):
    print("\nLinguagem de programação mais usada:")
    print(df[df["Ratings"] == df["Ratings"].max()].to_string(index=False)) # Exibindo a linha com a maior quantidade de votos
    #.to_string(index=False): exibe o DataFrame sem o índice

def linguagem_menos_usada(df):
    print("\nLinguagem de programação menos usada:")
    print(df[df["Ratings"] == df["Ratings"].min()].to_string(index=False)) # Exibindo a linha com a menor quantidade de votos
    #.to_string(index=False): exibe o DataFrame sem o índice

def linguagens_subiram(df):
    print("\nLinguagens de programação que subiram no ranking:")
    df_subiram = df[df["Mar 2025"] < df["Mar 2024"]] # Filtrando as linhas onde a coluna "Mar 2025" é menor que a coluna "Mar 2024"
    print(df_subiram.to_string(index=False)) # Exibindo as linhas filtradas
    
def top5_mais_subiram(df_original):
    print("\nTop 5 linguagens de programação que mais subiram no ranking:")
    df = df_original.copy() # Copiando o DataFrame original
    df["Diferenca"] = df["Mar 2024"] - df["Mar 2025"] # Criando uma nova coluna "Diferenca" com a diferença entre as colunas "Mar 2024" e "Mar 2025"
    df = df.sort_values(by="Diferenca", ascending=False).head(5) # Ordenando o DataFrame pela coluna "Diferenca" de forma decrescente e exibindo as 5 primeiras linhas
    print(df[["Language", "Diferenca"]].to_string(index=False)) # Exibindo as colunas "Language" e "Diferenca" sem o índice


html = acessar_url(URL)
bs = BeautifulSoup(html, 'html.parser')
exibir_cabecalho(bs)

tabela_html = obter_tabela(bs)
#print(tabela_html)
df = converter_tabela(tabela_html)
limpar_df(df)
#print(df.head())
#print(df.dtypes) # Exibindo os tipos de dados das colunas
print(df.head(5))

numero_linguagens(df)
linguagem_mais_usada(df)
linguagem_menos_usada(df)
linguagens_subiram(df)
top5_mais_subiram(df)
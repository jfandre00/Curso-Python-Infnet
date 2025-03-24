from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

def acessar_url():
    try:
        html = urlopen(URL)
    except Exception as ex:
        print("Erro: acesso a URL")
        exit() # Encerra o programa pois não foi possível acessar a URL
    return html

def exibir_cabecalho(bs):
    print(bs.h1.text)

def obter_tabela(bs):
    # Localizando a tabela
    tabela_html = bs.find('table', {"class":"wikitable"})
    return tabela_html

def converter_tabela(tabela):
    df = pd.read_html(str(tabela))[0] # Convertendo a tabela HTML para um DataFrame
    return df


def limpar_df(df):
    # Remover a bandeira, que é um ícone
    df.drop("Bandeira", axis=1, inplace=True) #axis=1: remove a coluna
    df = df.rename(columns={"Unidade federativa": "UF"})
    df["Alfabetização (2016)"].replace("%", "", inplace=True, regex=True) # regex=True: indica que a substituição será feita com base em uma expressão regular
    df["Alfabetização (2016)"].replace(",", ".", inplace=True, regex=True)
    df["Alfabetização (2016)"] = df["Alfabetização (2016)"].astype(float)

    df["Mortalidade infantil (2016)"].replace("‰", "", inplace=True, regex=True)
    df["Mortalidade infantil (2016)"].replace(",", ".", inplace=True, regex=True)
    df["Mortalidade infantil (2016)"] = df["Mortalidade infantil (2016)"].astype(float)
    return df

def exibir_uf_maior_alfabetizacao(df):
    print("\nUF com maior percentual de alfabetização:")
    df_temp = df[df["Alfabetização (2016)"] == df["Alfabetização (2016)"].max()]
    
    print(df_temp[["UF", "Alfabetização (2016)"]].to_string(index=False)) #remover o índice

def exibir_uf_menor_mortalidade(df):
    print("\nUF com menor percentual de mortalidade infantil:")
    df_temp = df[df["Mortalidade infantil (2016)"] == df["Mortalidade infantil (2016)"].min()]
    print(df_temp[["UF", "Mortalidade infantil (2016)"]].to_string(index=False)) #remover o índice

html = acessar_url()
bs = BeautifulSoup(html, 'html.parser')
exibir_cabecalho(bs)
tabela_html = obter_tabela(bs)
#print(tabela_html)
df = converter_tabela(tabela_html)
#print(df)

df = limpar_df(df)
print(df[["UF", "Alfabetização (2016)", "Mortalidade infantil (2016)"]]) # Exibindo as colunas "UF", "Alfabetização (2016) e "Mortalidade infantil (2016)"
#print(df.dtypes) # Exibindo os tipos de dados de cada coluna

exibir_uf_maior_alfabetizacao(df) # Exibindo o estado com maior percentual de alfabetização

exibir_uf_menor_mortalidade(df) # Exibindo o estado com menor percentual de mortalidade infantil
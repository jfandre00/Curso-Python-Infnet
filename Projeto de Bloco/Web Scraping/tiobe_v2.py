def criar_df(tabela):
    cabecalho = []
    for row in tabela.find_all('th'):
        cabecalho.append(row.text)
    #print(cabecalho)
    df = pd.DataFrame(columns=cabecalho)
    for linha in tabela.tbody.find_all("tr"):
        colunas = linha.find_all("td")
        mes_ano_atual = int(colunas[0].text)
        mes_ano_anterior = int(colunas[1].text)
        mudanca = None
        linguagem = colunas[4].text
        ratings = colunas[5].text
        change = colunas[6].text
        #print(mes_ano_atual, mes_ano_anterior, mudanca, linguagem, ratings, change)
        df.loc[len(df)] = [mes_ano_atual, mes_ano_anterior, mudanca, linguagem, ratings, change]
    return df
#TP1 - Python para Dados - André Loureiro Montini Ferreira

#Exercício 1

def somaLista(lista):
    '''
    Função que recebe uma lista de números inteiros e retorna a soma de todos os elementos da lista.
    
    Parâmetros:
    lista: lista de números inteiros

    Retorno:
    soma: soma de todos os elementos da lista
    '''
    soma = sum([i for i in lista])
    return soma

#Exercício 2

def removeDuplicados(lista):
    '''
    Função que recebe uma lista contendo elementos repetidos e retorna uma nova lista sem elementos duplicados, mantendo a ordem de aparição dos elementos.
    
    Parâmetros:
    lista: lista de números inteiros

    Retorno:
    lista: lista sem elementos duplicados
    '''
    lista = list(dict.fromkeys(lista)) #transforma a lista em um dicionário, removendo os elementos duplicados, e depois transforma o dicionário em uma lista
    return lista


#Exercício 3

lista_tuplas = [("José", 22), ("Ricardo", 26), ("Ana", 21), ("Maria", 25), ("João", 19), ("Paulo", 20), ("Lucas", 23), ("Mariana", 24), ("Pedro", 18), ("Carla", 27)]

def ordenaTuplas(lista):
    '''
    Função que recebe uma lista de tuplas e retorna uma nova lista ordenada de acordo com a idade dos elementos.
    
    Parâmetros:
    lista: lista de tuplas

    Retorno:
    lista: lista ordenada de acordo com a idade dos elementos
    '''
    lista.sort(key=lambda x: x[1], reverse=False) #ordena a lista de acordo com o segundo elemento de cada tupla, da menor para a maior idade.
    return lista

print(ordenaTuplas(lista_tuplas))

    
#Exercício 4

texto = "O jogo de futebol entre os dois times aconteceu depois de uma chuva forte que alagou o campo, e que muitas pessoas queriam que o jogo fosse cancelado. O jogo acabou empatado."

def contaPalavras(texto):
    '''
    Função que recebe um texto e retorna um dicionário contendo a contagem de cada palavra presente no texto.
    
    Parâmetros:
    texto: texto

    Retorno:
    dicionario: dicionário contendo a contagem de cada palavra presente no texto
    '''
    texto = texto.lower() #transforma todas as letras do texto em minúsculas
    texto = texto.replace(".", "") #remove os pontos do texto
    texto = texto.replace(",", "") #remove as vírgulas do texto
    texto = texto.split() #transforma o texto em uma lista de palavras
    dicionario = {}
    for palavra in texto:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario

print(contaPalavras(texto))

#Exercício 5

def inverterChavesValores(dicionario):
    '''
    Função que recebe um dicionário e retorna um novo dicionário com as chaves e valores invertidos.
    
    Parâmetros:
    dicionario: dicionário

    Retorno:
    dicionario_invertido: dicionário com as chaves e valores invertidos
    '''
    dicionario_invertido = {valor: chave for chave, valor in dicionario.items()}
    return dicionario_invertido

dicionario = {"a": 1, "b": 2, "c": 3, "d": 4}
print(inverterChavesValores(dicionario))

#Exercício 6

def mesclarDicionarios(dicionario1, dicionario2):
    '''
    Função que recebe dois dicionários contendo chaves e valores numéricos e retorna um novo dicionário que contenha todas as chaves de ambos os dicionários. Se uma chave estiver presente em ambos os dicionários, o valor correspondente no novo dicionário será a soma dos valores correspondentes nos dicionários de entrada.

    Parâmetros:
    dicionario1: dicionário
    dicionario2: dicionário

    Retorno:
    dicionario: dicionário contendo todas as chaves de ambos os dicionários
    '''


    dicionario = dicionario1.copy() #cria uma cópia do primeiro dicionário

    for chave, valor in dicionario2.items(): #itera sobre o segundo dicionário
        if chave in dicionario:
            dicionario[chave] += valor #soma os valores correspondentes se a chave estiver presente em ambos os dicionários
        else:
            dicionario[chave] = valor #adiciona a chave e o valor correspondente ao novo dicionário se a chave não estiver presente no primeiro dicionário
    
    return dicionario

dicionario1 = {"a": 1, "b": 2, "c": 3}
dicionario2 = {"b": 4, "c": 5, "d": 6}
print(mesclarDicionarios(dicionario1, dicionario2))

#Exercício 7
def estudaConjuntos(conjunto1, conjunto2):
    '''
    Função que recebe dois conjuntos e retorna um dicionário contendo a união, interseção e diferença (representando os elementos que estão no primeiro conjunto, mas não no segundo) dos conjuntos de entrada.

    Parâmetros:
    conjunto1: conjunto
    conjunto2: conjunto

    Retorno:
    dicionario: dicionário contendo a união, interseção e diferença dos conjuntos de entrada
    '''

    dicionario = {
        "uniao": conjunto1 | conjunto2, #também poderia ser conjunto1.union(conjunto2)
        "intersecao": conjunto1 & conjunto2, #também poderia ser conjunto1.intersection(conjunto2)
        "diferenca": conjunto1 - conjunto2 #também poderia ser conjunto1.difference(conjunto2)
    }
    return dicionario


conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print(estudaConjuntos(conjunto1, conjunto2))

#Exercício 8

def elementosUnicos(lista):
    '''
    Função que recebe uma lista de números inteiros e retorna uma nova lista contendo apenas os elementos únicos da lista original, sem manter a ordem.

    Parâmetros:
    lista: lista de números inteiros

    Retorno:
    lista: lista contendo apenas os elementos únicos da lista original
    '''

    lista = list(set(lista)) #transforma a lista em um conjunto para remover os elementos duplicados e depois transforma o conjunto em uma lista

    return lista

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(elementosUnicos(lista))

#Exercício 9

def conjuntoESubconjunto(conjunto1, conjunto2):
    '''
    Função que recebe dois conjuntos e retorna um valor boleano indicando se o primeiro conjunto é um subconjunto do segundo.

    Parâmetros:
    conjunto1: conjunto
    conjunto2: conjunto

    Retorno:
    booleano: valor boleano indicando se o primeiro conjunto é um subconjunto do segundo
    '''

    booleano = conjunto1.issubset(conjunto2) #verifica se o primeiro conjunto é um subconjunto do segundo

    return booleano

conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}

print("O primeiro conjunto é subconjunto" if conjuntoESubconjunto(conjunto1, conjunto2) else "O primeiro conjunto não é subconjunto") 

#Exercício 10

def leitorDeCSV(arquivo):
    '''
    Função que recebe o caminho de um arquivo CSV como entrada, lê o conteúdo do arquivo e imprime cada linha separadamente.

    Parâmetros:
    arquivo: caminho do arquivo CSV

    Retorno:
    None
    '''

    with open(arquivo, "r") as file:
        for linha in file:
            print(linha.strip()) #imprime cada linha do arquivo, removendo os espaços em branco no início e no final

leitorDeCSV("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex10.csv") #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1

#Exercício 11

def escreverDadosCSV(arquivo, listaDicionarios):
    '''
    Função que recebe o nome de um arquivo CSV e uma lista de dicionários, onde cada dicionário representa uma linha do arquivo. A função cria e escreve os dados no arquivo CSV, incluindo os cabeçalhos.

    Parâmetros:
    arquivo: caminho do arquivo CSV
    listaDicionarios: lista de dicionários

    Retorno:
    None
    '''

    with open(arquivo, "w", encoding="utf-8") as file:
        cabecalho = ",".join(listaDicionarios[0].keys()) #obtém os cabeçalhos do arquivo
        file.write(cabecalho + "\n") #escreve os cabeçalhos no arquivo
        for dicionario in listaDicionarios:
            linha = ",".join([str(valor) for valor in dicionario.values()]) #obtém os valores do dicionário e os converte em uma string separada por vírgulas
            file.write(linha + "\n") #escreve a linha no arquivo
    
    print("Arquivo criado com sucesso!\n")
    return None

listaDicionarios = [
    {"Nome": "José", "Idade": 22, "Sexo": "M"},
    {"Nome": "Ricardo", "Idade": 26, "Sexo": "M"},
    {"Nome": "Ana", "Idade": 21, "Sexo": "F"},
    {"Nome": "Maria", "Idade": 25, "Sexo": "F"}
]

escreverDadosCSV("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex11.csv", listaDicionarios) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1

#Exercício 12

def leitorDeJSON(arquivo):
    '''
    Função que recebe o nome de um arquivo JSON como entrada, lê o conteúdo do arquivo e retorna um dicionário representando os dados contidos no arquivo.

    Parâmetros:
    arquivo: caminho do arquivo JSON

    Retorno:
    dicionario: dicionário representando os dados contidos no arquivo
    '''

    import json

    with open(arquivo, "r", encoding='utf-8') as file:
        dicionario = json.load(file)

    return dicionario

print(leitorDeJSON("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex12.json")) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1

#Exercício 13

def escreverDicionarioEmJSON(arquivo, dicionario):
    '''
    Função que recebe o nome de um arquivo JSON e um dicionário, e escreve o dicionário no arquivo, garantindo que o conteúdo seja formatado corretamente para fácil leitura.

    Parâmetros:
    arquivo: caminho do arquivo JSON
    dicionario: dicionário

    Retorno:
    None
    '''

    import json

    with open(arquivo, "w", encoding='utf-8') as file:
        json.dump(dicionario, file, indent=4)

    print("\nArquivo criado com sucesso!\n")
    return None


dicionario = {
    "Nome": "Marcos",
    "Idade": 22,
    "Sexo": "M"
}

escreverDicionarioEmJSON("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex13.json", dicionario) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1


#Exercício 14

def processadorCSV(arquivo):
    '''
    Função que recebe um arquivo CSV contendo colunas de nome e cidade. A função lê o arquivo e retorna um dicionário onde as chaves são as cidades e os valores são listas de nomes associados a cada cidade.
    
    Parâmetros:
    arquivo: caminho do arquivo CSV

    Retorno:
    dicionario: dicionário onde as chaves são as cidades e os valores são listas de nomes associados a cada cidade
    '''

    dicionario = {}

    with open(arquivo, "r", encoding='utf-8') as file:
        next(file)  # Pula a primeira linha (cabeçalho), caso o CSV tenha cabeçalho. Se não tiver cabeçalho, não precisa dessa linha.
        for linha in file:
            nome, cidade = linha.strip().split(",")
            if cidade in dicionario:
                dicionario[cidade].append(nome)
            else:
                dicionario[cidade] = [nome]
    
    return dicionario

print(processadorCSV("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex14.csv")) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1
print()

#Exercício 15

def conjuntoAPartirTXT(arquivo):
    '''
    Função que recebe um arquivo TXT contendo uma lista de nomes, um por linha. A função lê o arquivo e retorna um conjunto (set) contendo apenas os nomes únicos encontrados no arquivo.

    Parâmetros:
    arquivo: caminho do arquivo TXT

    Retorno:
    conjunto: conjunto contendo apenas os nomes únicos encontrados no arquivo
    '''

    with open(arquivo, "r", encoding='utf-8') as file:
        conjunto = {linha.strip() for linha in file}

    return conjunto

print(conjuntoAPartirTXT("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex15.txt")) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1

#Exercício 16

def indiceInvertido(arquivo):
    '''
    Função que recebe um arquivo TXT e retorna um dicionário onde as chaves são as palavras e os valores são conjuntos de números de linha onde cada palavra aparece no texto.

    Parâmetros:
    arquivo: caminho do arquivo TXT

    Retorno:
    dicionario: dicionário onde as chaves são as palavras e os valores são conjuntos de números de linha onde cada palavra aparece no texto
    '''

    dicionario = {}

    with open(arquivo, "r", encoding='utf-8') as file:
        for indice, linha in enumerate(file, 1): # enumerate começa a contar a partir de 1
            linha = linha.lower().replace(".", "").replace(",", "") # transforma a linha em minúsculas e remove pontos e vírgulas
            palavras = linha.strip().split() # transforma a linha em uma lista de palavras
            for palavra in palavras:
                if palavra in dicionario:
                    dicionario[palavra].add(indice)
                else:
                    dicionario[palavra] = {indice}

    return dicionario

print(indiceInvertido("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex16.txt")) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1



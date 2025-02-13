import time
import sys

TAM = 100_000_001 #criando uma lista de 100 milhões de elementos (forma pythonica)
#Pode fazer sem o underline, mas é uma forma de melhorar a leitura

#TAM = 1_000_000 #criando uma lista de 1 milhão de elementos

ID = TAM - 1 #último elemento da lista

def criar_lista():
    lista = []
    for i in range(1, TAM):
        produto = [i, "Produto " + str(i), i] #id1, produto1, preco1 - até 100 milhões
        lista.append(produto)
    return lista

def pesquisar_lista(lista, id): #vamos pesquisar o último elemento da lista
    for produto in lista:
        if (produto[0] == id):
            return produto
    return None

def criar_dic():
    dic = {}
    for i in range(1, TAM): #criando um dicionário com 100 milhões de elementos
        dic[i] = ["Produto " + str(i), i]
    return dic

def pesquisar_dic(dic, id): #vamos pesquisar o último elemento do dicionário
    return dic[id]

print("Criação da lista")
inicio = time.process_time() #tempo que o programa ficou rodando
lista = criar_lista()
fim = time.process_time() #tempo de execução
print('Tempo em seg.:', fim - inicio)
inicio = time.process_time() 
print("Pesquisando lista")
produto = pesquisar_lista(lista, ID) #pesquisando o último elemento da lista, ele vai rodar até achar o último elemento
fim = time.process_time()
print('Tempo em seg.:', fim - inicio)
print(produto)
lista.clear()

print()
print("Criação do dicionário")
inicio = time.process_time()
dic = criar_dic()
fim = time.process_time()
print('Tempo em seg.:', fim - inicio)
print("Pesquisando dicionário")
inicio = time.process_time()
produto = pesquisar_dic(dic, ID)
fim = time.process_time()
print('Tempo em seg.:', fim - inicio)
print(produto)


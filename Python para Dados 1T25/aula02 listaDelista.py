lista_de_listas = [
    [1, 2, 3],
    ["a", "b", "c"],
    [True, False, True]
]

#Acessando elementos da lista de listas

print(lista_de_listas[0][1]) #2
print(lista_de_listas[1][2]) #c
print(lista_de_listas[2][0]) #True

#Exemplo de uso listas e dicionários

numeros = [10, 20, 30, 40]
pessoas = [
    {"nome": "João", "idade": 20},
    {"nome": "Maria", "idade": 30},
    {"nome": "José", "idade": 40}
]

#Sets - são coleções não ordenadas de elementos únicos (sem elementos duplicados)

#Criando um set

frutas = {"maçã", "banana", "laranja", "maçã", "banana", "laranja"}

#Adicionando elementos a um set

frutas.add("morango")
print(frutas)

#Adicionando elemento que já existe
frutas.add("maçã") #não adiciona
print(frutas)

#União de sets

set1 = {1, 2, 3, 4}
set2 = {1, 2, 5, 6}

uniao = set1.union(set2)
print(uniao)

#Interseção de sets
intersecao = set1.intersection(set2)
print(intersecao)

#Diferença de sets
diferenca = set1.difference(set2)
print(diferenca) #3, 4 pois são os elementos que estão em set1 e não estão em set2

diferenca2 = set2.difference(set1)
print(diferenca2) #5, 6 pois são os elementos que estão em set2 e não estão em set1

#Funcionalidades úteis dos sets
#1. Verificar se um elemento está presente no set
#2. Remover um elemento do set
#3. Limpar todos os elementos do set
#4. Verificar se um set é subconjunto de outro set

#Importante saber:
#.remove dá erro se o elemento não existe
#.discard não dá erro se o elemento não existe

set_novo = {1, 2, 3, 4, 5}
#set_novo.remove(6) #Erro
set_novo.discard(6) #Sem erro
print(set_novo)

A = {1, 2, 3}
B = {3, 4, 5}

#União
uniao = A.union(B)
print(A | B)

#Interseção
intersecao = A.intersection(B)
print(A & B)

#Diferença
print(A - B)
print(B - A)

#Diferença simétrica
print(A ^ B)


#eu tenho uma lista e quero só os elementos unicos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5]
set_lista = set(lista)
lista_sem_duplicados = list(set_lista)
print(set_lista)

#Subset e Superset

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}

print(B.issubset(A)) #True
print(A.issuperset(B)) #True

#Conjuntos imutáveis - frozenset
fs = frozenset([1, 2, 3, 4, 5])
print(fs)
#não é possível adicionar ou remover elementos de um frozenset

#Encontrando elementos comuns entre listas

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comuns = set(lista1) & (set(lista2))
print(comuns)

#Contagem de elementos únicos rapidamente

palavras = "o rato roeu a roupa do rei de roma rato rato".split()
contagem_unicos = len(set(palavras))
print(contagem_unicos) #vai contar quantas palavras únicas tem na lista

#Criando dicionários com set

d = {
    "grupo1" : { 1, 2, 3},
    "grupo2" : { 4, 5, 6},
}

print(d["grupo1"])






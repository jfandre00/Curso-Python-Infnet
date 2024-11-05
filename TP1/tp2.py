# TP2 André Loureiro Montini Ferreira

from random import randint, choice

def menu():
    while True:
        entrada = input("Digite o exercício (1 a 16) ou 0 para sair: ")
        
        try:
            exercicio = int(entrada)
            
            if exercicio == 0:
                print("Saindo...")
                break
            elif exercicio == 1:
                idades = {
                'Alice': 22,
                'Bob': 17,
                'Carol': 19,
                'David': 16
            }
                maiores_de_idade = exercicio1(idades)
                print(maiores_de_idade)
            elif exercicio == 2:
                tupla1 = (1, 3, 5)
                tupla2 = (5, 1, 3)
                exercicio2(tupla1, tupla2)
            elif exercicio == 3:
                lista = [4, 1, 5, 2, 3, 2, 4, 4]
                frequencia = exercicio3(lista)
                print(frequencia)
            elif exercicio == 4:
                dicionario1 = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
                dicionario2 = { 'b': 2, 'c': 3, 'd': 4 }
                exercicio4(dicionario1, dicionario2)
            elif exercicio == 5:
                notas = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5}
                relatorio = exercicio5(notas)
                print(f'Relatório dos Alunos:\n{relatorio}')
            elif exercicio == 6:
                lista = [10, 5, 3, 4, 2, 6, 7, 1, 9, 8]
                exercicio6(lista)
            elif exercicio == 7:
                alunos, notas = exercicio7()
                imprimir_notas(alunos, notas)
            elif exercicio == 8:
                exercicio8()
            elif exercicio == 9:
                palavra = input("Digite uma palavra: ")
                exercicio9(palavra)
            elif exercicio == 10:
                lista_dict_nome_notas = [
                    {'nome': 'Ana', 'nota': 8.5},
                    {'nome': 'Pedro', 'nota': 6.0},
                    {'nome': 'Maria', 'nota': 7.5},
                    {'nome': 'José', 'nota': 5.5},
                    {'nome': 'João', 'nota': 9.0}
                ]
                exercicio10(lista_dict_nome_notas)
            elif exercicio == 11:
                listaFrutas = ['banana', 'maçã', 'uva', 'abacaxi', 'laranja', 'manga', 'melancia', 'morango', 'pera', 'pêssego']
                exercicio11(listaFrutas)
            elif exercicio == 12:
                frutas = list(input("Digite as frutas separadas por espaço: ").split())
                #Vou precisar usar o map abaixo para converter as strings em inteiros	
                quantidades = list(map(int, input("Digite as quantidades separadas por espaço: ").split()))
                exercicio12(frutas, quantidades)
            elif exercicio == 13:
                texto = input("Digite um texto: ")
                exercicio13(texto)
            elif exercicio == 14:
                exercicio14()
            elif exercicio == 15:
                exercicio15('Maria', 25, 'Rio de Janeiro')
                exercicio15('João', 30)
            elif exercicio == 16:
                exercicio16()
            else:
                print("Opção inválida, tente novamente!")
        except ValueError:
            print("Entrada inválida! Digite um número entre 0 e 16.")

def remove_menor(lista):
    '''
    Função que remove o menor elemento de uma lista

    Input: lista de elementos
    Output: lista sem o menor elemento e o menor elemento removido
    '''
    menor = min(lista)
    lista.remove(menor)
    return menor, lista

def imprimir_notas(alunos, notas):
    '''
    Função que imprime os alunos e suas respectivas notas

    Input: lista de alunos e lista de notas
    Output: impressão dos alunos e suas notas

    '''
    for i, aluno in enumerate(alunos):
        print(f'{aluno}: {notas[i]}')

def sortear_numero():
    '''
    Função que sorteia um número aleatório entre 1 e 20

    Input: nenhum
    Output: número sorteado
    '''
    numeroMagico = randint(1, 20)
    return numeroMagico

def tratar_entrada(frutas, quantidades):
    '''
    Função que verifica se o número de quantidades fornecido é igual ao número de frutas fornecido e faz o tratamento necessário conforme as regras do exercício

    Input: lista de frutas e lista de quantidades

    Output: nenhuma
    '''
    while True:
        if len(quantidades) > len(frutas):
            quantidades = quantidades[:len(frutas)]
        elif len(quantidades) < len(frutas):
            print("O número de quantidades fornecido é menor do que o número de frutas.")
            quantidades = list(map(int, input("Digite as quantidades separadas por espaço: ").split()))
        else:
            break

def dividir(n1, n2):
    '''
    Função que recebe dois números e retorna dois outputs, o resultado inteiro e o resto da divisão

    Input: dois números inteiros (n1 e n2)

    Output: resultado inteiro (inteiro) e resto da divisão (resto)
    '''
    if n2 == 0:
        print("Não é possível dividir por zero. Saindo do exercício...")
        return None, None
    else:
        inteiro = n1 // n2
        resto = n1 % n2
        return inteiro, resto

def calcular_total(preco, quantidade=1):
    '''
    Função que calcula o total de uma compra

    Input: preço do produto e quantidade comprada. Caso a quantidade não seja fornecida, será considerada 1 como padrão

    Output: total da compra
    '''
    total = preco * quantidade
    return total

def exercicio1(idades):
    '''
    Função que retorna um novo dicionário que contenha apenas as pessoas maiores de idade

    Input: dicionário com os nomes e idades das pessoas
    Output: dicionário com os nomes e idades das pessoas maiores de idade
    '''
    maiores_idade = {nome: idade for nome, idade in idades.items() if idade >= 18}

    return maiores_idade

def exercicio2(tupla1, tupla2):
    '''
    Função que verifica se duas possuem os mesmos elementos, independentemente da ordem

    Input: tupla1 e tupla2 (tuple) - tuplas a serem comparadas
    Output: mensagem informando se as tuplas possuem os mesmos elementos
    '''
    if set(tupla1) == set(tupla2):
        print("As tuplas possuem os mesmos elementos.")
    else:
        print("As tuplas não possuem os mesmos elementos.")

def exercicio3(lista):
    '''
    Função que retorna a um dicionário contendo a frequência de cada elemento em uma lista
    
    Input: lista de elementos

    Output: dicionário com a frequência de cada elemento
    '''
    frequencia = {elemento: lista.count(elemento) for elemento in set(lista)}
    return frequencia

def exercicio4(dict1, dict2):
    '''
    Função que verifica se um dicionário é subconjunto de outro dicionário
    
    Input: 2 dicionários a serem comparados

    Output: mensagem informando se um dicionário é subconjunto do outro
    '''
    if all(item in dict1.items() for item in dict2.items()) or all(item in dict2.items() for item in dict1.items()):
        print("Um dicionário é subconjunto do outro.")
    else:
        print("Os dicionários não são subconjuntos um do outro.")

def exercicio5(asNotas):
    '''
    Função que verifica se um aluno foi aprovado ou reprovado baseado em sua média

    Input: dicionário com os nomes dos alunos e suas notas

    Output: dicionário agrupando os alunos aprovados e reprovados dentro de listas
    '''
    APROVADO = 7
    relatorio_aprovacoes = {}
    aprovados = [aluno for aluno, nota in asNotas.items() if nota >= APROVADO]
    reprovados = [aluno for aluno, nota in asNotas.items() if nota < APROVADO]
    relatorio_aprovacoes['Aprovado'] = aprovados
    relatorio_aprovacoes['Reprovado'] = reprovados

    return relatorio_aprovacoes

def exercicio6(lista):
    '''
    Função que encontra os dois números cuja soma seja o mais próximo possível de zero, ou seja, a soma dos dois menores elementos da lista

    Input: lista de números

    Output: os dois menores elementos da lista
    '''
    menor1, lista = remove_menor(lista)
    menor2, lista = remove_menor(lista)
    print(f'Menor elemento: {menor1}')
    print(f'2º Menor elemento: {menor2}')

def exercicio7():
    '''
    Função que solicita ao usuário o nome e a nota de vários alunos e retorna duas listas, uma com os nomes e outra com as notas
    
    Input: nenhum
    
    Output: lista de alunos e lista de notas
    '''
    alunos = []
    notas = []
    while True:  
        aluno = input("Digite o nome do aluno (ou 'fim' para encerrar): ").strip()
        if aluno.lower() == 'fim':
            break
        alunos.append(aluno)
        # Verifica se a nota é um float, senão irá pedir para digitar novamente até ser um float
        while True:
            nota = input("Digite a nota do aluno: ")
            try:
                float(nota)
                break
            except ValueError:
                print("Nota inválida! Digite um número.")
        notas.append(float(nota))
    return alunos, notas
        
def exercicio8():
    '''
    Função que implementa um jogo de adivinhação de um número mágico entre 1 e 20

    Input: nenhum

    Output: mensagem informando se o jogador acertou o número mágico
    '''
    TENTATIVAS = 4
    numeroMagico = sortear_numero()
    print("Bem-vindo ao jogo do número mágico!")
    print("Tente adivinhar o número mágico entre 1 e 20.")
    print(f"Você tem {TENTATIVAS} tentativas.")
    for i in range(TENTATIVAS):
        tentativa = int(input(f"Tentativa {i+1}: "))
        if tentativa == numeroMagico:
            print("Parabéns! Você acertou o número mágico!")
            break
        elif tentativa < numeroMagico:
            print("O número mágico é maior.")
        else:
            print("O número mágico é menor.")
    else:
        print(f"Você perdeu! O número mágico era {numeroMagico}.")

def exercicio9(palavra):
    '''
    Função que verifica se uma palavra fornecida pelo usuário é um palíndromo

    Input: palavra a ser verificada

    Output: mensagem informando se a palavra é um palíndromo
    '''
    #Poderia ter feito todo o tratamento de string em uma linha só, mas preferi dividir em várias linhas para facilitar a leitura
    palavra = palavra.strip()
    palavra = palavra.lower()
    palavra = palavra.replace(" ", "")
    if palavra == palavra[::-1]:
        print("A palavra é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")

def exercicio10(aLista):
    '''
    Função que ordena uma lista de dicionários de acordo com a nota de cada aluno usando estruturas básicas de Python

    Input: lista de dicionários com o nome e a nota de cada aluno

    Output: lista de dicionários ordenada de acordo com a nota de cada aluno
    '''
    for i in range(len(aLista)):
        for j in range(i, len(aLista)):
            if aLista[i]['nota'] < aLista[j]['nota']:
                aLista[i], aLista[j] = aLista[j], aLista[i]
    print("Lista de alunos ordenada de acordo com a nota:")
    print(aLista)

def exercicio11(aLista):
    '''
    Função que solicita ao usuário a posição de um elemento na lista e imprime o elemento correspondente, ou encerra o programa caso o usuário digite "sair". Todos os erros de entrada são tratados

    Input: lista de elementos

    Output: elemento correspondente à posição fornecida pelo usuário
    '''

    while True:
        try:
            opcao = input('Digite a posição do elemento que deseja visualizar (ou "sair" para encerrar): ')
            if opcao.lower().strip() == 'sair':
                print('Saindo do exercício 11...')
                break
            opcao = int(opcao)
            print(aLista[opcao])
        except ValueError:
            print('Entrada inválida! Por favor, digite um número.')
        except IndexError:
            print('Esse índice não existe na lista.')

def exercicio12(frutas, quantidades):
    '''
    Função que escolhe aleatoriamente uma fruta da lista fornecida pelo usuário e a quantidade correspondente
    
    Input: lista de frutas e lista de quantidades

    Output: mensagem informando a fruta escolhida
    '''
    #Vamos tratar as entradas seguindo as regras do exercício utilizando a função tratar_entrada
    tratar_entrada(frutas, quantidades)
    escolha = choice(frutas)
    print(f"Joel irá presentear a fruta: {escolha}.")
    
def exercicio13(oTexto):
    '''
    Função que imprime na tela o texto fornecido pelo usuário

    Input: texto a ser impresso

    Output: impressão do texto
    '''
    print(oTexto)

def exercicio14():
    '''
    Função que solicita ao usuário dois números e os envia para a função dividir
    
    '''
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    inteiro, resto = dividir(n1,n2)
    if inteiro is not None:
        print(f"Resultado da divisão: {inteiro}")
        print(f"Resto da divisão: {resto}")

def exercicio15(nome, idade, cidade='Desconhecida'):
    '''
    Função que imprime na tela o nome, idade e cidade de uma pessoa, mas caso a cidade não seja fornecida, a cidade será "Desconhecida" como padrão

    Input: nome, idade e cidade da pessoa

    Output: impressão do nome, idade e cidade da pessoa
    '''
    print(f'{nome} tem {idade} anos e mora em {cidade}')

def exercicio16():
    '''
    Função que envia o preço e a quantidade de um produto para a função calcular_total
    
    Input: nenhum

    Output: total da compra impresso na tela
    '''

    precoTotal1 = calcular_total(20, 2)
    print(f"Total da compra: R$ {precoTotal1:.2f}")

    precoTotal2 = calcular_total(30)
    print(f"Total da compra: R$ {precoTotal2:.2f}")

menu()

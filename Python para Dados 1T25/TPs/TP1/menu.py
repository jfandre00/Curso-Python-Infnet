#TP1 - Python para Dados - André Loureiro Montini Ferreira
#Menu para execução dos exercícios do TP1

from tp1 import *

def menu():
    '''
    Função que exibe um menu com as opções de execução dos exercícios do TP1.

    Parâmetros:
    - Nenhum

    Retorno:
    - Nenhum
    '''
    while True:
        print("\nExercícios do TP1:")
        escolha = input("Digite o número do exercício que deseja executar [1 a 16] ou 0 para sair: ")
        match escolha:
            case "1":
                print(somaLista([1, 2, 3, 4, 5]))
            case "2":
                print(removeDuplicados([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
            case "3":
                lista_tuplas = [("José", 22), ("Ricardo", 26), ("Ana", 21), ("Maria", 25), ("João", 19), ("Paulo", 20), ("Lucas", 23), ("Mariana", 24), ("Pedro", 18), ("Carla", 27)]
                print(ordenaTuplas(lista_tuplas))
            case "4":
                texto = "O jogo de futebol entre os dois times aconteceu depois de uma chuva forte que alagou o campo, e que muitas pessoas queriam que o jogo fosse cancelado. O jogo acabou empatado."
                print(contaPalavras(texto))
            case "5":
                dicionario = {"a": 1, "b": 2, "c": 3, "d": 4}
                print(inverterChavesValores(dicionario))
            case "6":
                dicionario1 = {"a": 1, "b": 2, "c": 3}
                dicionario2 = {"b": 4, "c": 5, "d": 6}
                print(mesclarDicionarios(dicionario1, dicionario2))
            case "7":
                conjunto1 = {1, 2, 3, 4, 5}
                conjunto2 = {4, 5, 6, 7, 8}
                print(estudaConjuntos(conjunto1, conjunto2))
            case "8":
                lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
                print(elementosUnicos(lista))
            case "9":
                conjunto1 = {1, 2, 3}
                conjunto2 = {1, 2, 3, 4, 5}
                print("O primeiro conjunto é subconjunto do segundo" if conjuntoESubconjunto(conjunto1, conjunto2) else "O primeiro conjunto não é subconjunto do segundo") 
            case "10":
                leitorDeCSV("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex10.csv") #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1
            case "11":
                listaDicionarios = [
                {"Nome": "José", "Idade": 22, "Sexo": "M"},
                {"Nome": "Ricardo", "Idade": 26, "Sexo": "M"},
                {"Nome": "Ana", "Idade": 21, "Sexo": "F"},
                {"Nome": "Maria", "Idade": 25, "Sexo": "F"},
                {"Nome": "João", "Idade": 19, "Sexo": "M"},
                ]
                escreverDadosCSV("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex11.csv", listaDicionarios) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1
            case "12":
                print(leitorDeJSON("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex12.json")) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1
            case "13":
                dicionario = {
                    "Nome": "Marcos",
                    "Idade": 22,
                    "Sexo": "M"
                }
                escreverDicionarioEmJSON("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex13.json", dicionario) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1
            case "14":
                print(processadorCSV("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex14.csv")) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1
            case "15":
                print(conjuntoAPartirTXT("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex15.txt")) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1
            case "16":
                print(indiceInvertido("C:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Python para Dados 1T25/TPs/TP1/ex16.txt")) #esse é o caminho do arquivo no meu computador, preciso lembrar de alterar o caminho na hora de entregar o TP1
            case "0":
                print("Até o TP2!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()


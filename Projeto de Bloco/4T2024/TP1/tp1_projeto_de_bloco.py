import os
import time
tarefas = []

def adicionar_tarefa():
    '''
    Função para adicionar uma tarefa à lista de tarefas
    '''
    tarefa = input('Digite a tarefa: ')
    tarefa_a_adicionar = [tarefa, False]
    tarefas.append(tarefa_a_adicionar)
    #q: é possível limpar a tela após adicionar a tarefa?

    os.system('cls')
    print('\033[1;34m\033[1mTarefa adicionada com sucesso!\033[0m')

def exibir_tarefas():
    '''
    Função para exibir as tarefas cadastradas
    '''
    os.system('cls')
    print('-' * 40)
    if len(tarefas) == 0:
        print('Lista Vazia')
    else:
        print('Tarefas cadastradas:')
        for i in range(len(tarefas)):
            status = '\033[1;34m(concluída)\033[0m' if tarefas[i][1] else '\033[1;35m(pendente)\033[0m'
            print(f'{i + 1} - {tarefas[i][0]} - {status}')
    print('-' * 40)
    #Aguardar dois segundos antes de continuar
    time.sleep(2)

def marcar_tarefa_como_concluida():
    '''
    Função para marcar uma tarefa como concluída
    '''
    exibir_tarefas()
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada')
    else:
        tarefa = int(input('Digite o número da tarefa a ser concluída: '))
        if tarefa <= len(tarefas):
            tarefas[tarefa - 1][1] = True
            os.system('cls')
            print('\033[1;34m\033[1mTarefa marcada como concluída!\033[0m')
            time.sleep(1)
        else:
            print('\033[1;4;91mTarefa não encontrada\033[0m')

def remover_tarefa():
    '''
    Função para remover uma tarefa da lista
    '''
    exibir_tarefas()
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada, não é possível remover')
    else:
        tarefa = int(input('Digite o número da tarefa a ser removida: '))
        if tarefa <= len(tarefas):
            tarefas.pop(tarefa - 1)
        else:
            os.system('cls')
            print('Tarefa não encontrada')

def menu():
    '''
    Função para exibir o menu de opções, que chama as funções de acordo com a opção escolhida e trata exceções
    Exibe o menu até que o usuário escolha a opção de sair, e as opções estão coloridas.
    '''
    while True:
        try:
            print('\033[1;4;92mMenu de opções\033[0m')
            print('\033[92m1\033[0m - Adicionar tarefa')
            print('\033[92m2\033[0m - Exibir tarefas')
            print('\033[92m3\033[0m - Marcar tarefa como concluída')
            print('\033[92m4\033[0m - Remover tarefa')
            print('\033[92m5\033[0m - Sair')
            opcao = int(input('\033[1;4;92mDigite a opção:\033[0m '))
            if opcao == 1:
                adicionar_tarefa()
            elif opcao == 2:
                exibir_tarefas()
            elif opcao == 3:
                marcar_tarefa_como_concluida()
            elif opcao == 4:
                remover_tarefa()
            elif opcao == 5:
                break
            else:
                print('\033[1;4;91mERRO! Opção Inválida! Tente novamente\033[0m')
        except ValueError:
            print('\033[1;4;91mERRO! Entre com um número inteiro\033[0m')

menu()
